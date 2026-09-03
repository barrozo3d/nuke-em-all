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

🔴 A COURSE THAT DECLARES THE `translation` MODULE OVERWRITES ITS OWN `.srt`.
`cmd_write_pt_srt` calls `write_srt(translated, srt_path)` — the SAME path. So on
`rebelway-nuke-comp` the file beside the video is the pt-BR deliverable, not the
engine's transcription output, and a raw byte-compare against the Russian
transcript reports 109/109 FAIL on a perfectly healthy engine. That is the check
being wrong, not the engine. The first version of this script did exactly that.

So the comparison is split into what the engine actually authors and what it
does not:

  * the CUE SKELETON — cue numbering, timecode formatting, blank-line
    separation, cue count, trailing newline. `write_srt` owns every byte of it,
    on every course, translated or not. It is compared byte-for-byte ALWAYS, and
    a difference here is always a failure.
  * the TEXT — owned by the transcript, or by the translation pass downstream of
    it. On a course with no `translation` module the text must match too, and a
    divergence is a real defect. On a translated course it is expected, and
    `commit_translation` is what guards it (segment count, timings within 0.01s,
    non-empty, not a no-op).

Exit 0 = every compared lesson reproduced what the engine authors.
Exit 1 = at least one differed in a way the engine is responsible for.
Exit 2 = nothing could be compared (which is NOT a pass — see the coverage note).
"""

import argparse
import ast
import json
import sys
import tempfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SKILL_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_DIR))

from course_engine_loader import load_course_engine

_ce = load_course_engine(SKILL_DIR)


def course_outputs(skill_dir, slug):
    """The `outputs` tuple of the COURSE dict whose slug is `slug`, or None.

    ⚠️ Read by AST, never imported. The two skills declare COURSE in differently
    named files (`course_transcribe.py`, `course_subtitles.py`) and importing
    either drags in `ingest` and the whisper stack — a heavyweight import, and a
    side-effecting one, inside a script whose whole guarantee is that it changes
    nothing. `slug` and `outputs` are plain literals in both, so parsing is
    enough and cannot execute anything.
    """
    for path in sorted(skill_dir.glob("course_*.py")):
        try:
            tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
        except SyntaxError:
            continue
        for node in tree.body:
            if not isinstance(node, ast.Assign):
                continue
            if not any(getattr(t, "id", None) == "COURSE" for t in node.targets):
                continue
            if not isinstance(node.value, ast.Dict):
                continue
            found = {}
            for k, v in zip(node.value.keys, node.value.values):
                if isinstance(k, ast.Constant) and k.value in ("slug", "outputs"):
                    try:
                        found[k.value] = ast.literal_eval(v)
                    except ValueError:
                        pass
            if found.get("slug") == slug and "outputs" in found:
                return tuple(found["outputs"])
    return None


def cue_skeleton(text):
    """Every line `write_srt` authors on its own: indices, timecodes, blanks.

    Text lines are replaced by a marker rather than dropped, so a cue that lost
    or gained a text line still reads as a structural difference.
    """
    out = []
    for line in text.splitlines():
        s = line.strip()
        if s == "" or s.isdigit() or "-->" in s:
            out.append(s)
        else:
            out.append("\x00TEXT")
    return out


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

    outputs = course_outputs(SKILL_DIR, args.course_slug)
    if outputs is None:
        print(f"  ⚠️ no COURSE dict with slug {args.course_slug!r} found in "
              f"{SKILL_DIR.name}/course_*.py —\n"
              f"     treating the .srt as untranslated, which is the STRICTER reading.")
        outputs = ()
    translated_course = "translation" in outputs

    ok = text_only = structural = skipped = 0
    skip_reasons = {}
    mismatches = []
    stamped = unstamped = 0
    ledger_missing = []

    for slug, entry in state.get("lessons", {}).items():
        if args.limit and (ok + text_only + structural) >= args.limit:
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
            at = a.decode("utf-8", "replace")
            bt = b.decode("utf-8", "replace")
            if cue_skeleton(at) == cue_skeleton(bt):
                text_only += 1
                # The .srt differs from the transcript, so this lesson HAS been
                # translated on disk. If the ledger does not say so, the ledger
                # is under-recording something that demonstrably happened.
                if translated_course and entry.get("pt_br_srt_written") is not True:
                    ledger_missing.append(slug)
            else:
                structural += 1
                mismatches.append((slug, srt, a, b))

    compared = ok + text_only + structural
    print(f"\n  compared     : {compared} lesson(s)")
    print(f"    identical  : {ok}")
    note = ""
    if text_only:
        note = ("   (expected: this course declares the translation module)"
                if translated_course else "   ⚠️ UNEXPECTED on an untranslated course")
    print(f"    text-only  : {text_only}{note}")
    print(f"    STRUCTURAL : {structural}")
    print(f"  course outputs: {', '.join(outputs) if outputs else '(none declared)'}")
    print(f"  protocol mix : {unstamped} pre-stamp, {stamped} stamped "
          f"({'BOTH sides covered' if unstamped and stamped else 'ONE side only'})")
    print(f"  skipped      : {skipped}")
    for why, n in sorted(skip_reasons.items(), key=lambda kv: -kv[1]):
        print(f"      {n:4d}  {why}")

    if mismatches:
        print("\n  STRUCTURAL MISMATCHES (the engine is responsible for these):")
        for slug, path, a, b in mismatches[:10]:
            print(f"    {slug}\n      {path}")
            if args.show_diff:
                al = a.decode("utf-8", "replace").splitlines()
                bl = b.decode("utf-8", "replace").splitlines()
                for i, (x, y) in enumerate(zip(al, bl)):
                    if x != y:
                        print(f"      first diff at line {i+1}:\n"
                              f"        on disk: {x!r}\n        engine : {y!r}")
                        break
                else:
                    print(f"      identical for {min(len(al), len(bl))} lines, "
                          f"then length differs ({len(al)} vs {len(bl)})")

    if ledger_missing:
        print(f"\n  ⚠️ LEDGER UNDER-RECORDS TRANSLATION: {len(ledger_missing)} lesson(s) have a"
              f"\n     translated .srt on disk but no `pt_br_srt_written` in state.json."
              f"\n     Not an engine defect -- the disk is right and the ledger is silent --"
              f"\n     but `module_status` reports the translation module unfinished for them.")
        for s in ledger_missing[:5]:
            print(f"       {s}")
        if len(ledger_missing) > 5:
            print(f"       ... and {len(ledger_missing) - 5} more")

    # ⚠️ Coverage rule: zero comparisons is not a pass.
    if compared == 0:
        print("\n  ⚠️ NOTHING WAS COMPARED. This is not a pass -- check --course-root, and\n"
              "     that transcripts/ and the .srt files are present on this machine.")
        return 2
    if structural:
        print("\n  RESULT: FAIL -- the engine does not reproduce those .srt files.")
        return 1
    if text_only and not translated_course:
        print("\n  RESULT: FAIL -- the cue skeleton matches but the TEXT differs, on a course"
              "\n     that runs no translation module. Nothing downstream should have"
              "\n     rewritten those lines, so this is the engine or the transcript cache.")
        return 1
    if text_only:
        print(f"\n  RESULT: PASS -- {ok} byte-for-byte, {text_only} identical in every byte the"
              "\n     engine authors (cue numbering, timecodes, cue count, separators);"
              "\n     their text differs only because the translation pass overwrote the"
              "\n     same .srt. Timing preservation is exactly what that proves.")
    else:
        print("\n  RESULT: PASS -- every compared lesson reproduced byte-for-byte.")
    if not (unstamped and stamped):
        print(f"\n  ⚠️ COVERAGE: only ONE side of the protocol boundary was covered"
              f" ({unstamped} pre-stamp, {stamped} stamped)."
              "\n     🔴 This is NOT fixable by re-running with different arguments. Phase 4"
              "\n     deliberately does not backfill `protocol_version`, so EVERY already-"
              "\n     finalized lesson is pre-stamp and always will be. The stamped side"
              "\n     becomes coverable only when a lesson is seeded under PROTOCOL_VERSION"
              "\n     >= 1 -- i.e. by a new ingest, not by a re-run of this script.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
