"""
course_subtitles.py — SRT-only batch Whisper transcription for a local
(non-YouTube) course. Subtitle-focused sibling of ingest.py's Step 1: no
tutorials/*.md, no INDEX.md, no knowledge-base ingest of any kind — just the
most accurate .srt file Whisper (large-v3, GPU) can produce for each video,
plus the same accent/mishear-risk flagging built for the Designing Destruction
course (houdini-wand/course_transcribe.py), reused here via `import ingest`
for the shared internals (WHISPER_VOCAB_HINT, slugify, run_safeguards,
_load_whisper_model).

Use this when the goal is precise subtitles for personal study, not a skill
knowledge-base entry. If a full ingest is ever wanted later, the state file
this script writes (source_file/duration/transcript_cached/flags) is a
superset of what course_transcribe.py needs, so nothing here is wasted.

Two outputs per video:
  1. A real .srt file written next to the source video on disk.
  2. A cached Whisper transcript (segments + text) under
     course-ingest/<course-slug>/transcripts/<lesson-slug>.json — gitignored,
     kept so a flag-review pass or a future re-run doesn't need to re-run
     Whisper.

Progress/flags tracked in course-ingest/<course-slug>/state.json (gitignored,
local-only) so reruns skip already-done videos (--force to redo).

The transcript alone is NOT "really really precise" by itself — Whisper can
be confidently wrong on an accented, jargon-dense speaker. The flagging step
(flag_segments) surfaces the lines worth a manual listen; --check-flags /
--resolve-flag / --bulk-resolve / --finalize turn that into an enforced
review pass, same mechanism as the Houdini course used.

Usage:
  python course_subtitles.py --course-root "G:\\...\\Rebelway_Compositing in Nuke" --course-slug rebelway-nuke-comp
  python course_subtitles.py --course-slug rebelway-nuke-comp --week 1
  python course_subtitles.py --course-slug rebelway-nuke-comp --check-flags
  python course_subtitles.py --course-slug rebelway-nuke-comp --resolve-flag <slug> <start> "<note>"
  python course_subtitles.py --course-slug rebelway-nuke-comp --finalize <slug>
"""

import sys, os, re, json, argparse, subprocess
from pathlib import Path
from datetime import datetime, timezone

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace', line_buffering=True)

SKILL_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_DIR))
import ingest  # reuse WHISPER_VOCAB_HINT, slugify, run_safeguards, _load_whisper_model

DEFAULT_COURSE_ROOT = r"G:\Documentos\Cursos\Rebelway_Compositing in Nuke"
DEFAULT_COURSE_SLUG = "rebelway-nuke-comp"
DEFAULT_INSTRUCTOR  = "Rebelway"
DEFAULT_MODEL       = "large-v3"  # accuracy over speed — precision was the explicit ask

# ROOT-CAUSE FIX (2026-08-18), after analyzing Week 1's hallucination clusters:
# every single low-avg_logprob burst (wk1-04, 08, 09, 12, 13) contained random
# words/scripts from OTHER languages bled into what should be pure Russian —
# Spanish ("hijo", "tangos"), English ("marriage is the best heaven",
# "appliances shop", "sinful"), Chinese/Japanese/Korean/Hangul characters
# (第, 宮, 어, 하죠, 있고요), even mid-word ("отоплитеek"). This is Whisper's
# documented multilingual-drift failure mode during low-confidence decoding —
# and this pipeline was feeding it ingest.py's WHISPER_VOCAB_HINT, an
# ENGLISH-language initial_prompt, to prime a RUSSIAN transcription. Whisper's
# initial_prompt is meant to bias the decoder toward the prompt's own
# language/style; a mismatched-language prompt is a known trigger for exactly
# this kind of drift. Replaced with a Russian-language prompt using the
# correct Cyrillic spellings this course's own clean transcripts already
# confirmed (кейинг, вьюер, футаж, etc. — not ingest.py's English hint at all).
COURSE_VOCAB_HINT = (
    "Это урок по композитингу в Nuke от студии Rebelway. Термины: нод, нода, "
    "нодовый граф, вьюер, футаж, цветокор, композ, трекер, трекинг, кейинг, "
    "рото, ротоскоп, денойз, рендер, атрибут, канал, альфа, экспрешн, гизмо, "
    "мёрдж, ACES, OCIO, Cryptomatte, EXR, AOV, Keylight, IBK, CopyCat, "
    "Z-depth, slap comp, proxy."
)

# CORRECTED after smoke-testing 2 real lessons (2026-08-18): the course audio
# is not accented English, it's Russian narration ("russian teacher" was
# literal). English loanword terms get spoken with Russian phonetics/grammar
# ("нод"/"нода" for node, "вьюер" for viewer, "футаж" for footage/plate,
# "цветокор" for color-correct, "композ" for comp) rather than substituted
# for an unrelated English word, so the English-mishear model from
# houdini-wand doesn't apply. This list instead catches Whisper mistranscribing
# one Russian loanword/technical term as another — used by flag_segments()'s
# near-miss check.
ACCENT_RISK_VOCAB = [
    "нод", "нода", "вьюер", "футаж", "цветокор", "композ",
    "трекер", "трекинг", "нюк", "мёрдж", "мерж", "мердж", "рото", "ротоскоп",
    "кейинг", "кейнг", "денойс", "денойз", "маска", "нойз", "рендер", "чекер",
    "атрибут", "проперти", "канал", "альфа", "premult", "unpremult",
    "экспрешн", "гизмо", "плагин", "проект", "шот", "паблиш",
    "roto paint", "rotopaint",
]
# "roto paint"/"rotopaint" added after real Week-1 evidence (2026-08-19, during
# translation pass): wk1-13 (Adding Grain) had a Whisper mishear "Rata Paint"
# at 724.82s (coherent read from context is the RotoPaint node) that slipped
# through flag review because RotoPaint wasn't in this list yet - the near-miss
# checker only catches vocab it's told to watch for.
# Corrections after real Week-1 evidence (2026-08-18):
# - "нодовый" removed: fuzzy-matched the extremely common word "новый" (new)
#   in real transcripts ("тут новый формат в проекте" flagged as a false
#   mishear) - a bare-word collision, not a real risk.
# - "кеинг" -> "кейинг": Whisper consistently and correctly transcribes
#   "keying" as "кейинг"/"кейинга"/"кейинге" (with й) across every real
#   sample seen; the old spelling was simply wrong and flagged the CORRECT
#   transcription as a near-miss of itself.
# - bare "кей" removed: fuzzy-matched "окей" (a common, unrelated filler
#   word meaning "okay") on nearly every occurrence - would have flooded
#   every lesson in the course with false positives.
# Corrections after real Week-2 evidence (2026-08-18, post prompt/language
# fix): "кейнг" (no й) and "мердж" (with д) turned out to be Whisper's
# consistent, correct spelling in multiple clean, low-avg_logprob contexts —
# same pattern as денойс/денойз (both legit phonetic variants of "denoise").
# Added as their own recognized entries rather than treated as mishears of
# кейинг/мерж, since exact-match short-circuits the near-miss check (see
# flag_segments) - both spelling variants now coexist without flagging each
# other. "кейнг" alone (7 flags in one wk2 lesson) would have been the single
# biggest source of false-positive review noise for the rest of the course
# if left uncorrected.

# avg_logprob threshold: evidence-based for THIS course, not reused from
# houdini-wand's -0.35 (that was tuned for English). Sampling 2 real lessons
# (317 + ~180 segments) showed a clean trimodal split for Russian: the bulk of
# correct speech sits at -0.5 to 0, a second cluster of correct-but-short
# repeated phrases sits around -0.7 to -1.5, and genuine hallucinated gibberish
# (confirmed by reading the text — mixed Cyrillic/Latin nonsense like
# "отоплитеek", "Qwaleel", "Jashtag") sits at -4.8 to -5.04 — a wide, empty gap
# with zero segments between -1.5 and -4.8. -2.0 sits safely inside that gap.
AVG_LOGPROB_FLAG_THRESHOLD = -2.0

# compression_ratio is NOT a useful signal for this course: real, correct
# Russian segments span the same 1.24-2.33 range as the transcript's overall
# max, so the English-tuned >=2.2 cutoff flagged the majority of CORRECT
# segments as false positives (e.g. "Посмотрим через вьюер." at cr=2.28 is
# fine). Set high enough to effectively disable it rather than delete the
# check outright, in case a genuinely repetitive/degenerate segment ever
# exceeds this course's observed ceiling.
COMPRESSION_RATIO_FLAG_THRESHOLD = 3.0

WEEK_DIR_RE = re.compile(r"^week\s*(\d+)$", re.IGNORECASE)
FILE_ORDER_RE = re.compile(r"^(\d+)[\s_.\-]+(.+)$")
VIDEO_EXTS = (".mp4", ".mkv", ".mov")


def flag_segments(segments):
    """Same three-signal triage as houdini-wand/course_transcribe.py's
    flag_segments() (low-confidence / accent-risk near-miss / decode-window
    near-duplicate) — see that file's docstring for the evidence behind each
    threshold. Kept as an independent copy (not shared via import) since the
    vocab pool differs per course and the two DCC skills stay decoupled."""
    import difflib

    flagged = []
    dup_at = {}  # original segment index -> True if near-duplicate of segments[index-1]
    for i, seg in enumerate(segments):
        reasons = []
        if seg.get("avg_logprob", 0) <= AVG_LOGPROB_FLAG_THRESHOLD:
            reasons.append(f"low avg_logprob ({seg['avg_logprob']:.2f})")
        if seg.get("no_speech_prob", 0) >= 0.5:
            reasons.append(f"high no_speech_prob ({seg['no_speech_prob']:.2f})")
        if seg.get("compression_ratio", 0) >= COMPRESSION_RATIO_FLAG_THRESHOLD:
            reasons.append(f"high compression_ratio ({seg['compression_ratio']:.2f})")
        # Dropped "temperature fallback > 0" as a standalone flag reason after
        # sampling: 51 of 91 flags on the wk1-04 test lesson were temperature
        # fallback alone, and every sample checked was a correct, coherent
        # sentence. Whisper's own internal retry heuristic (tuned around
        # English compression-ratio/logprob defaults) triggers far more often
        # on this course's short, rapid technical narration without it
        # correlating with an actual transcription error — pure noise here,
        # unlike houdini-wand's English course where it was informative.

        text = seg.get("text", "")
        # Cyrillic + Latin (loanwords like "TAP" appear verbatim in Latin
        # script mid-sentence) — a Latin-only regex would never match this
        # course's Russian ACCENT_RISK_VOCAB at all.
        words = re.findall(r"[a-zA-Zа-яА-ЯёЁ']+", text.lower())
        single_vocab = [v for v in ACCENT_RISK_VOCAB if " " not in v]
        multi_vocab = [v for v in ACCENT_RISK_VOCAB if " " in v]
        candidates = [(w, single_vocab) for w in words]
        for n in {len(v.split()) for v in multi_vocab}:
            candidates += [(" ".join(words[i:i+n]), multi_vocab) for i in range(len(words) - n + 1)]

        near_misses = set()
        for cand, pool in candidates:
            if cand in pool:
                continue
            close = difflib.get_close_matches(cand, pool, n=1, cutoff=0.82)
            if not close:
                continue
            match = close[0]
            shorter, longer = sorted([cand, match], key=len)
            if longer.startswith(shorter) and len(longer) - len(shorter) <= 3:
                continue
            near_misses.add(f"'{cand}' ~ '{match}'")
        if near_misses:
            reasons.append("possible mishear: " + ", ".join(sorted(near_misses)))

        if i > 0:
            prev_text = segments[i - 1].get("text", "").strip()
            ratio = difflib.SequenceMatcher(None, prev_text.lower(), text.strip().lower()).ratio()
            if ratio >= 0.85 and prev_text:
                dup_at[i] = True
                reasons.append(f"near-duplicate of previous segment ({ratio:.2f} similarity) — likely decode-window repeat")

        if reasons:
            flagged.append({
                "start": seg.get("start"), "end": seg.get("end"),
                "text": text.strip(), "reasons": reasons, "_idx": i,
            })

    # Second pass: a lone near-duplicate pair is usually genuine repeated
    # speech during a live demo (e.g. "Удалим нод." x3 while deleting three
    # separate nodes). A RUN of 3+ *consecutive original-transcript indices*
    # all near-duplicating their immediate predecessor (= 4+ total repeated
    # utterances back to back) is a different, much more dangerous pattern —
    # real examples found in this course: "Нюк." repeated 11x over 20s,
    # "Средний клавиша." repeated 6x within the same single second. That's
    # not natural speech, it's a decode-loop hallucination the low-avg_logprob
    # check misses entirely (a short correct word like "Нюк" scores fine on
    # confidence). run_safeguards()'s _detect_hallucination() also misses
    # these since it only scans the last-50-words tail of the WHOLE
    # transcript, not a sliding window, so a mid-video burst is invisible.
    #
    # Computed from dup_at (keyed by real segment index) rather than from
    # position within the filtered `flagged` list — an earlier version used
    # list position and wrongly merged wk1-06's 20 genuinely separate
    # near-duplicate pairs (scattered across 3:58-19:21, ~15 min apart) into
    # one fake "20x burst" just because every flagged segment in that lesson
    # happened to be a near-duplicate, with nothing of a different reason
    # between them in the filtered list to break the run.
    dup_indices = sorted(dup_at)
    runs = []
    run = []
    for idx in dup_indices:
        if run and idx == run[-1] + 1:
            run.append(idx)
        else:
            if len(run) >= 3:
                runs.append(run)
            run = [idx]
    if len(run) >= 3:
        runs.append(run)

    by_idx = {f["_idx"]: f for f in flagged}
    for run in runs:
        total_repeats = len(run) + 1  # + the un-flagged first occurrence that started the run
        for idx in run:
            by_idx[idx]["reasons"].append(
                f"part of a {total_repeats}x repeat-loop burst — check with --lesson --force"
            )

    for f in flagged:
        f.pop("_idx", None)
    return flagged


def course_ingest_dir(course_slug):
    return SKILL_DIR / "course-ingest" / course_slug


def state_path(course_slug):
    return course_ingest_dir(course_slug) / "state.json"


def load_state(course_slug, course_root):
    p = state_path(course_slug)
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {
        "course": "Rebelway Compositing in Nuke",
        "instructor": DEFAULT_INSTRUCTOR,
        "source_root": course_root,
        "whisper_model": DEFAULT_MODEL,
        "lessons": {},
        "last_updated": None,
    }


def save_state(course_slug, state):
    """Atomic write — see houdini-wand/course_transcribe.py's save_state() for
    why (avoids a truncated read if two processes touch state.json at once)."""
    state["last_updated"] = datetime.now(timezone.utc).isoformat() + "Z"
    p = state_path(course_slug)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, p)


def lesson_slug(week, order, topic_raw):
    return ingest.slugify(f"rebelway-nuke wk{week} {order:02d} {topic_raw}")


def scan_course(course_root):
    """Walk 'Week N'/*.{mp4,mkv,mov}, parse order + topic from each filename's
    leading number (both '01_topic.ext' and '01 Topic.ext' source-naming
    styles appear in this course, unlike the pre-normalized Houdini course)."""
    root = Path(course_root)
    found = []
    for week_dir in sorted(root.iterdir()):
        if not week_dir.is_dir():
            continue
        m = WEEK_DIR_RE.match(week_dir.name)
        if not m:
            continue
        week = int(m.group(1))
        for f in sorted(week_dir.iterdir()):
            if not f.is_file() or f.suffix.lower() not in VIDEO_EXTS:
                continue
            fm = FILE_ORDER_RE.match(f.stem)
            if not fm:
                print(f"[WARN] Filename doesn't start with a lesson number: {f.name} - skipping")
                continue
            order = int(fm.group(1))
            topic_raw = fm.group(2)
            found.append({"week": week, "order": order, "topic_raw": topic_raw, "path": f})
    found.sort(key=lambda x: (x["week"], x["order"]))
    return found


def probe_duration(video_path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(video_path)],
        capture_output=True, text=True
    ).stdout.strip()
    try:
        return float(out)
    except ValueError:
        return None


def ensure_lessons(state, course_root):
    videos = scan_course(course_root)
    for v in videos:
        slug = lesson_slug(v["week"], v["order"], v["topic_raw"])
        if slug in state["lessons"]:
            continue
        rel_path = str(v["path"].relative_to(Path(course_root))).replace("\\", "/")
        state["lessons"][slug] = {
            "week": v["week"],
            "order": v["order"],
            "topic_raw": v["topic_raw"],
            "source_file": rel_path,
            "duration_sec": probe_duration(v["path"]),
            "srt_written": False,
            "transcript_cached": None,
            "safeguard_warnings": [],
            "safeguard_critical": [],
            "needs_review": False,
            "flagged_segments": [],
            "flagged_segments_reviewed": False,
            "flag_resolutions": {},
            "last_transcribed": None,
            "pt_br_srt_written": False,
        }
    return state, videos


def format_srt_timestamp(seconds):
    if seconds < 0:
        seconds = 0
    ms = int(round((seconds - int(seconds)) * 1000))
    s = int(seconds)
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def write_srt(segments, srt_path):
    lines = []
    for i, seg in enumerate(segments, start=1):
        start = format_srt_timestamp(seg["start"])
        end = format_srt_timestamp(seg["end"])
        text = seg["text"].strip()
        lines.append(str(i))
        lines.append(f"{start} --> {end}")
        lines.append(text)
        lines.append("")
    srt_path.write_text("\n".join(lines), encoding="utf-8")


def _flag_key(flag):
    return str(flag["start"])


def unresolved_flags(entry):
    resolutions = entry.get("flag_resolutions", {})
    return [f for f in entry.get("flagged_segments", []) if _flag_key(f) not in resolutions]


def cmd_check_flags(state, slug_filter):
    lessons = state["lessons"] if slug_filter in (None, "all") else {slug_filter: state["lessons"].get(slug_filter)}
    if slug_filter not in (None, "all") and lessons.get(slug_filter) is None:
        print(f"ERROR: '{slug_filter}' not found.")
        sys.exit(1)
    any_unresolved = False
    for slug, entry in lessons.items():
        if entry is None:
            continue
        unresolved = unresolved_flags(entry)
        if not unresolved:
            continue
        any_unresolved = True
        print(f"{slug}: {len(unresolved)} unresolved flag(s)")
        for f in unresolved:
            mm, ss = int(f["start"]) // 60, int(f["start"]) % 60
            print(f"    [{mm}:{ss:02d}] {f['text'][:90]}")
            print(f"        reasons: {f['reasons']}")
    if not any_unresolved:
        print("[CLEAN] No unresolved flags.")


def cmd_resolve_flag(state, course_slug, slug, start, note):
    entry = state["lessons"].get(slug)
    if entry is None:
        print(f"ERROR: '{slug}' not found.")
        sys.exit(1)
    matches = [f for f in entry.get("flagged_segments", []) if abs(f["start"] - start) < 0.5]
    if not matches:
        print(f"ERROR: no flagged segment near start={start} in {slug}.")
        sys.exit(1)
    entry.setdefault("flag_resolutions", {})
    for f in matches:
        entry["flag_resolutions"][_flag_key(f)] = note
    save_state(course_slug, state)
    print(f"Resolved {len(matches)} flag(s) at ~{start}s in {slug}: {note}")


def cmd_resolve_range(state, course_slug, slug, start, end, note):
    entry = state["lessons"].get(slug)
    if entry is None:
        print(f"ERROR: '{slug}' not found.")
        sys.exit(1)
    entry.setdefault("flag_resolutions", {})
    matches = [f for f in entry.get("flagged_segments", []) if start <= f["start"] <= end]
    if not matches:
        print(f"ERROR: no flagged segments in [{start}, {end}]s in {slug}.")
        sys.exit(1)
    for f in matches:
        entry["flag_resolutions"][_flag_key(f)] = note
    save_state(course_slug, state)
    print(f"Resolved {len(matches)} flag(s) in [{start}, {end}]s in {slug}: {note}")


def cmd_bulk_resolve(state, course_slug, slug, note):
    entry = state["lessons"].get(slug)
    if entry is None:
        print(f"ERROR: '{slug}' not found.")
        sys.exit(1)
    entry.setdefault("flag_resolutions", {})
    unresolved = unresolved_flags(entry)
    for f in unresolved:
        entry["flag_resolutions"][_flag_key(f)] = note
    save_state(course_slug, state)
    print(f"Bulk-resolved {len(unresolved)} flag(s) in {slug}: {note}")


def cmd_finalize(state, course_slug, slug):
    entry = state["lessons"].get(slug)
    if entry is None:
        print(f"ERROR: '{slug}' not found.")
        sys.exit(1)
    unresolved = unresolved_flags(entry)
    if unresolved:
        print(f"[BLOCKED] {slug} has {len(unresolved)} unresolved flag(s). "
              f"Run --check-flags {slug} to see them, then --resolve-flag or --bulk-resolve each before finalizing.")
        sys.exit(1)
    entry["flagged_segments_reviewed"] = True
    save_state(course_slug, state)
    print(f"[FINALIZED] {slug}: {len(entry.get('flagged_segments', []))} flag(s), all resolved.")


def cmd_write_pt_srt(state, course_slug, course_root, slug, json_path):
    """Validates and commits a Portuguese translation produced by a translation
    pass (a forked Claude subagent, not Whisper — see course_subtitles.py's
    header). This is the mechanical safety net for that judgment-call work,
    same "structural, not just apologized for" philosophy as --finalize
    refusing on unresolved flags. Refuses (exit 1, writes nothing) unless ALL
    of the following hold:
      1. The lesson is finalized (flagged_segments_reviewed) - never translate
         a still-flagged transcript, that would launder an ASR error into a
         confident-looking Portuguese sentence.
      2. The translated JSON has EXACTLY the same segment count as the cached
         Russian transcript, in the same order.
      3. Every translated start/end matches the original's, within 0.01s -
         catches a translator that reordered, merged, or dropped segments
         while translating.
      4. No translated segment is empty/whitespace-only.
      5. The translated text as a whole is not byte-identical to the Russian
         original (a no-op "translation" would silently pass every other
         check).
    On success: writes the final .srt to the exact video path (overwriting
    the transcription-phase Russian .srt that's there now - PT-BR only is the
    user-confirmed final deliverable), marks pt_br_srt_written, saves state.
    """
    entry = state["lessons"].get(slug)
    if entry is None:
        print(f"ERROR: '{slug}' not found.")
        sys.exit(1)
    if not entry.get("flagged_segments_reviewed"):
        print(f"[BLOCKED] {slug} is not finalized yet (flagged_segments_reviewed=False). "
              f"Run the flag-review pass and --finalize {slug} before translating.")
        sys.exit(1)
    if not entry.get("transcript_cached"):
        print(f"ERROR: {slug} has no cached transcript to validate against.")
        sys.exit(1)

    cache_path = SKILL_DIR / entry["transcript_cached"]
    original = json.loads(cache_path.read_text(encoding="utf-8")).get("segments", [])
    translated = json.loads(Path(json_path).read_text(encoding="utf-8"))

    if len(translated) != len(original):
        print(f"[BLOCKED] Segment count mismatch: original={len(original)}, translated={len(translated)}. "
              f"Translation must be 1:1 with the original transcript - no merging/splitting/dropping segments.")
        sys.exit(1)

    for i, (o, t) in enumerate(zip(original, translated)):
        if abs(o.get("start", 0) - t.get("start", 0)) > 0.01 or abs(o.get("end", 0) - t.get("end", 0)) > 0.01:
            print(f"[BLOCKED] Segment {i} timing mismatch: original=({o.get('start')},{o.get('end')}) "
                  f"translated=({t.get('start')},{t.get('end')}). Timings must be preserved exactly.")
            sys.exit(1)
        if not t.get("text", "").strip():
            print(f"[BLOCKED] Segment {i} (start={t.get('start')}) has empty translated text.")
            sys.exit(1)

    orig_joined = " ".join(s.get("text", "") for s in original)
    trans_joined = " ".join(s.get("text", "") for s in translated)
    if orig_joined.strip() == trans_joined.strip():
        print(f"[BLOCKED] Translated text is byte-identical to the Russian original - looks like a no-op, not a real translation.")
        sys.exit(1)

    video_path = Path(course_root) / entry["source_file"]
    srt_path = video_path.with_suffix(".srt")
    write_srt(translated, srt_path)

    entry["pt_br_srt_written"] = True
    entry["pt_br_translated_at"] = datetime.now(timezone.utc).isoformat() + "Z"
    save_state(course_slug, state)
    print(f"[TRANSLATED] {slug}: {len(translated)} segments written to {srt_path}")


def main():
    parser = argparse.ArgumentParser(description="SRT-only batch Whisper transcription for a local course")
    parser.add_argument("--course-root", default=DEFAULT_COURSE_ROOT)
    parser.add_argument("--course-slug", default=DEFAULT_COURSE_SLUG)
    parser.add_argument("--week", type=int, default=None, help="Only process this week")
    parser.add_argument("--lesson", default=None, metavar="SLUG", help="Only process this exact lesson slug (e.g. for a targeted re-transcribe)")
    parser.add_argument("--whisper-model", default=DEFAULT_MODEL)
    parser.add_argument("--force", action="store_true", help="Re-transcribe even if already done")
    parser.add_argument("--limit", type=int, default=None, help="Only process the first N matching videos (smoke testing)")
    parser.add_argument("--rescan-flags", action="store_true",
                         help="Re-run flag_segments() against already-cached transcripts (no Whisper re-run)")
    parser.add_argument("--check-flags", nargs="?", const="all", default=None, metavar="SLUG")
    parser.add_argument("--resolve-flag", nargs=3, metavar=("SLUG", "START", "NOTE"))
    parser.add_argument("--bulk-resolve", nargs=2, metavar=("SLUG", "NOTE"))
    parser.add_argument("--resolve-range", nargs=4, metavar=("SLUG", "START", "END", "NOTE"))
    parser.add_argument("--finalize", metavar="SLUG")
    parser.add_argument("--write-pt-srt", nargs=2, metavar=("SLUG", "JSON_PATH"),
                         help="Validate and commit a Portuguese translation (JSON list of {start,end,text}, "
                              "1:1 with the cached original) as the lesson's final .srt")
    parser.add_argument("--list", action="store_true", help="List all discovered lessons with slugs and status")
    args = parser.parse_args()

    if args.write_pt_srt:
        slug, json_path = args.write_pt_srt
        state = load_state(args.course_slug, args.course_root)
        cmd_write_pt_srt(state, args.course_slug, args.course_root, slug, json_path)
        return

    if args.list:
        state = load_state(args.course_slug, args.course_root)
        state, videos = ensure_lessons(state, args.course_root)
        save_state(args.course_slug, state)
        for v in videos:
            slug = lesson_slug(v["week"], v["order"], v["topic_raw"])
            entry = state["lessons"][slug]
            status = "done" if entry["srt_written"] else "pending"
            print(f"[{status:7s}] wk{v['week']} {v['order']:02d}  {slug}")
        return

    if args.check_flags is not None:
        state = load_state(args.course_slug, args.course_root)
        cmd_check_flags(state, None if args.check_flags == "all" else args.check_flags)
        return

    if args.resolve_flag:
        slug, start, note = args.resolve_flag
        state = load_state(args.course_slug, args.course_root)
        cmd_resolve_flag(state, args.course_slug, slug, float(start), note)
        return

    if args.resolve_range:
        slug, start, end, note = args.resolve_range
        state = load_state(args.course_slug, args.course_root)
        cmd_resolve_range(state, args.course_slug, slug, float(start), float(end), note)
        return

    if args.bulk_resolve:
        slug, note = args.bulk_resolve
        state = load_state(args.course_slug, args.course_root)
        cmd_bulk_resolve(state, args.course_slug, slug, note)
        return

    if args.finalize:
        state = load_state(args.course_slug, args.course_root)
        cmd_finalize(state, args.course_slug, args.finalize)
        return

    if args.rescan_flags:
        state = load_state(args.course_slug, args.course_root)
        n_flagged_total = 0
        for slug, entry in state["lessons"].items():
            if not entry.get("transcript_cached"):
                continue
            cache_path = SKILL_DIR / entry["transcript_cached"]
            if not cache_path.exists():
                continue
            cached = json.loads(cache_path.read_text(encoding="utf-8"))
            flagged = flag_segments(cached.get("segments", []))
            entry["flagged_segments"] = flagged
            entry.setdefault("flagged_segments_reviewed", False)
            if flagged:
                n_flagged_total += 1
                print(f"{slug}: {len(flagged)} segment(s) flagged")
        save_state(args.course_slug, state)
        print(f"[DONE] Rescanned. {n_flagged_total} lesson(s) have flagged segments.")
        return

    import shutil
    if not shutil.which("ffmpeg"):
        print("[FATAL] ffmpeg not found on PATH - required for Whisper's internal audio decode. Aborting.")
        sys.exit(1)
    try:
        import whisper  # noqa: F401
    except ImportError:
        print("[FATAL] openai-whisper not installed (pip install openai-whisper). Aborting.")
        sys.exit(1)

    state = load_state(args.course_slug, args.course_root)
    state["whisper_model"] = args.whisper_model
    state, videos = ensure_lessons(state, args.course_root)
    save_state(args.course_slug, state)

    if args.lesson is not None:
        videos = [v for v in videos if lesson_slug(v["week"], v["order"], v["topic_raw"]) == args.lesson]
        if not videos:
            print(f"[FATAL] No video matches --lesson {args.lesson}.")
            sys.exit(1)
    if args.week is not None:
        videos = [v for v in videos if v["week"] == args.week]
    if args.limit is not None:
        videos = videos[:args.limit]

    if not videos:
        print("[INFO] Nothing to do for the given filter.")
        return

    print(f"[INFO] Loading Whisper model '{args.whisper_model}' once for this batch of {len(videos)} video(s)...")
    model = ingest._load_whisper_model(args.whisper_model)

    transcripts_dir = course_ingest_dir(args.course_slug) / "transcripts"
    transcripts_dir.mkdir(parents=True, exist_ok=True)

    for i, v in enumerate(videos, start=1):
        slug = lesson_slug(v["week"], v["order"], v["topic_raw"])
        entry = state["lessons"][slug]
        video_path = v["path"]

        if entry["srt_written"] and entry["transcript_cached"] and not args.force:
            print(f"[{i}/{len(videos)}] SKIP (already done): {slug}")
            continue

        print(f"[{i}/{len(videos)}] Transcribing: {video_path.name}  -> {slug}")
        # language="ru": course audio is confirmed Russian throughout (see
        # course_subtitles.py header) - pinning it removes any per-file
        # language-detection ambiguity rather than relying on autodetect.
        # condition_on_previous_text=False: Whisper's default conditions each
        # ~30s window's decode on the PREVIOUS window's output text. Once a
        # window hallucinates, that garbage becomes the context for the next
        # window, compounding the error - the likely mechanism behind Week
        # 1's long repeat-loop bursts (11x, 20x) rather than isolated blips.
        # Disabling it makes each window decode independently, so one bad
        # window can't drag the next ones down with it.
        result = model.transcribe(
            str(video_path), initial_prompt=COURSE_VOCAB_HINT,
            language="ru", condition_on_previous_text=False,
        )

        srt_path = video_path.with_suffix(".srt")
        write_srt(result.get("segments", []), srt_path)

        cache_path = transcripts_dir / f"{slug}.json"
        cache_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

        ch_transcripts = ingest.segment_by_chapters(result, None)
        warnings, critical = ingest.run_safeguards(ch_transcripts)
        ingest._print_safeguard_report(warnings, critical)

        flagged = flag_segments(result.get("segments", []))
        if flagged:
            print(f"      [ACCENT CHECK] {len(flagged)} segment(s) flagged for manual review:")
            for f in flagged[:5]:
                mm, ss = int(f["start"]) // 60, int(f["start"]) % 60
                print(f"        [{mm}:{ss:02d}] \"{f['text']}\" — {'; '.join(f['reasons'])}")
            if len(flagged) > 5:
                print(f"        ... and {len(flagged) - 5} more (see state.json)")

        entry["duration_sec"] = entry["duration_sec"] or probe_duration(video_path)
        entry["srt_written"] = True
        entry["transcript_cached"] = str(cache_path.relative_to(SKILL_DIR)).replace("\\", "/")
        entry["safeguard_warnings"] = warnings
        entry["safeguard_critical"] = critical
        entry["needs_review"] = bool(critical)
        entry["flagged_segments"] = flagged
        entry["flagged_segments_reviewed"] = False
        entry["last_transcribed"] = datetime.now(timezone.utc).isoformat() + "Z"

        save_state(args.course_slug, state)  # persist after every video

    print(f"[DONE] Processed {len(videos)} video(s) for {'week ' + str(args.week) if args.week else 'all weeks'}.")


if __name__ == "__main__":
    main()
