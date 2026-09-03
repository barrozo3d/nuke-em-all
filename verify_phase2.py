#!/usr/bin/env python3
"""
verify_phase2.py — Phase 2's success criterion, run NON-DESTRUCTIVELY.

ULTIMATE_PIPELINE_PLAN.md Phase 2: *"re-running a finalized lesson through the
new engine reproduces its existing .srt byte-for-byte — pick lessons from both
courses, and from both sides of the destruction course's protocol boundary."*

That criterion could not be run on the machine where the engine was extracted:
`course-ingest/` lives only on the machine holding the courses. This script is
the handoff.

⚠️ IT DOES NOT RE-RUN WHISPER, AND IT WRITES NOTHING. It feeds each lesson's
ALREADY-CACHED transcript through the extracted engine's `write_srt()` and
compares the bytes against the `.srt` sitting next to the source video. That is
exactly what the criterion asks — does the engine reproduce the file — without
`--force`, without touching `state.json`, and without `--rescan-flags`, which
would reset `flagged_segments_reviewed` on every finalized lesson.

    python verify_phase2.py --course-slug designing-destruction \\
                            --course-root "G:\\...\\Designing Destruction In Houdini"

    python verify_phase2.py --course-slug designing-destruction \\
                            --course-root "..." --limit 20 --show-diff

Exit 0 = every compared lesson reproduced byte-for-byte.
Exit 1 = at least one differed (the finding).
Exit 2 = nothing could be compared (which is NOT a pass — see the coverage note).
"""

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SKILL_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_DIR))

from course_engine_loader import load_course_engine

_ce = load_course_engine(SKILL_DIR)


def main():
    ap = argparse.ArgumentParser(description="Phase 2 criterion, non-destructive")
    ap.add_argument("--course-slug", required=True)
    ap.add_argument("--course-root", required=True,
                    help="the course's video root, so source_file resolves")
    ap.add_argument("--limit", type=int, default=0, help="compare at most N lessons")
    ap.add_argument("--show-diff", action="store_true",
                    help="print the first differing line of any mismatch")
    args = ap.parse_args()

    state_path = SKILL_DIR / "course-ingest" / args.course_slug / "state.json"
    if not state_path.exists():
        print(f"ERROR: {state_path} not found. Run this on the machine holding the course.")
        return 2
    state = json.loads(state_path.read_text(encoding="utf-8"))
    root = Path(args.course_root)

    ok = diff = skipped = 0
    skip_reasons = {}
    mismatches = []
    stamped = unstamped = 0

    for slug, entry in state.get("lessons", {}).items():
        if args.limit and (ok + diff) >= args.limit:
            break
        cached = entry.get("transcript_cached")
        src = entry.get("source_file")

        def skip(why):
            nonlocal skipped
            skipped += 1
            skip_reasons[why] = skip_reasons.get(why, 0) + 1

        if not cached:
            skip("no cached transcript"); continue
        cpath = Path(cached)
        if not cpath.is_absolute():
            cpath = SKILL_DIR / "course-ingest" / args.course_slug / "transcripts" / cpath.name
        if not cpath.exists():
            skip("cached transcript file missing"); continue
        if not src:
            skip("no source_file"); continue
        srt = (root / src).with_suffix(".srt")
        if not srt.exists():
            skip("no .srt on disk"); continue

        try:
            segments = json.loads(cpath.read_text(encoding="utf-8")).get("segments", [])
        except Exception:
            skip("cached transcript unreadable"); continue
        if not segments:
            skip("cached transcript has no segments"); continue

        # Protocol boundary: a lesson seeded before stamping existed has no
        # protocol_version. Both sides are worth reporting separately -- the
        # criterion explicitly asks for lessons from both.
        if entry.get("protocol_version") is None:
            unstamped += 1
        else:
            stamped += 1

        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "regen.srt"
            _ce.write_srt(segments, out)
            a, b = srt.read_bytes(), out.read_bytes()
        if a == b:
            ok += 1
        else:
            diff += 1
            mismatches.append((slug, srt, a, b))

    print(f"\n  compared     : {ok + diff} lesson(s)")
    print(f"    identical  : {ok}")
    print(f"    DIFFERING  : {diff}")
    print(f"  protocol mix : {unstamped} pre-stamp, {stamped} stamped "
          f"({'BOTH sides covered' if unstamped and stamped else 'ONE side only'})")
    print(f"  skipped      : {skipped}")
    for why, n in sorted(skip_reasons.items(), key=lambda kv: -kv[1]):
        print(f"      {n:4d}  {why}")

    if mismatches:
        print("\n  MISMATCHES:")
        for slug, path, a, b in mismatches[:10]:
            print(f"    {slug}\n      {path}")
            if args.show_diff:
                al, bl = a.decode("utf-8", "replace").splitlines(), b.decode("utf-8", "replace").splitlines()
                for i, (x, y) in enumerate(zip(al, bl)):
                    if x != y:
                        print(f"      first diff at line {i+1}:\n        on disk: {x!r}\n        engine : {y!r}")
                        break
                else:
                    print(f"      identical for {min(len(al), len(bl))} lines, "
                          f"then length differs ({len(al)} vs {len(bl)})")

    # ⚠️ Coverage rule: zero comparisons is not a pass.
    if ok + diff == 0:
        print("\n  ⚠️ NOTHING WAS COMPARED. This is not a pass -- check --course-root, and\n"
              "     that transcripts/ and the .srt files are present on this machine.")
        return 2
    if diff:
        print("\n  RESULT: FAIL -- the engine does not reproduce those .srt files.")
        return 1
    print("\n  RESULT: PASS -- every compared lesson reproduced byte-for-byte.")
    if not (unstamped and stamped):
        print("  ⚠️ ...but only ONE side of the protocol boundary was covered. The criterion\n"
              "     asks for both; re-run without --limit, or on the other course too.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
