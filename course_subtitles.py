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

# ─────────────────────────────────────────────────────────────────────────────
# PHASE 1 (houdini-wand/ULTIMATE_PIPELINE_PLAN.md §2.1) — name the seams
# WITHOUT moving code.
#
#   COURSE  — what this course IS: root, slug, instructor, on-disk layout,
#             which output modules run.
#   PROFILE — everything TUNED AGAINST EVIDENCE from this course's language and
#             audio: prompt, vocab pools, detector thresholds, detectors on/off.
#
# ⚠️ This file is the REASON the split exists. It and course_transcribe.py are
# "one engine wearing two coats" (§1.3): 19 shared functions, 8 byte-identical,
# and of the 11 that differ, the causes are language profile / course layout /
# which output modules run — exactly the three dicts below. Read the two
# PROFILEs side by side and the §2.1 claim is either obvious or falsified.
#
# ⚠️ Nothing has MOVED yet, by design. Phase 2 extracts the engine.
# ─────────────────────────────────────────────────────────────────────────────

COURSE = {
    "slug":       "rebelway-nuke-comp",
    "root":       r"G:\Documentos\Cursos\Rebelway_Compositing in Nuke",
    "instructor": "Rebelway",
    "model":      "large-v3",   # accuracy over speed — precision was the explicit ask

    # On-disk layout: `Week N`/ directories (note the space, and the free-form
    # capitalisation) holding `01_topic.ext` OR `01 Topic.ext` — both source
    # naming styles appear, unlike the pre-normalized Houdini course whose
    # filenames were already `..._wk<N>_<topic>.mp4`. This pair of regexes is
    # the whole of scan_course()'s ~29% divergence from its houdini twin.
    "week_dir_re":  re.compile(r"^week\s*(\d+)$", re.IGNORECASE),
    "file_re":      re.compile(r"^(\d+)[\s_.\-]+(.+)$"),
    "video_exts":   (".mp4", ".mkv", ".mov"),

    # ⚠️ NOT COURSE["slug"], and not equal to it either — lesson_slug() has
    # always built from the shorter "rebelway-nuke" while the state file and
    # course-ingest dir use "rebelway-nuke-comp". Deriving one from the other
    # would rename every finalized lesson. Frozen identity; treat it as data.
    "lesson_slug_prefix": "rebelway-nuke",

    # Seed for a state.json that does not exist yet. ⚠️ KEY ORDER IS LOAD-BEARING
    # -- see the note in houdini-wand's COURSE dict.
    "state_defaults": {
        "course": "Rebelway Compositing in Nuke",
        "instructor": "Rebelway",
        "source_root": None,
        "whisper_model": "large-v3",
        "lessons": {},
        "last_updated": None,
    },

    # Output modules (§2.1 — these COMPOSE). Decision #4: output policy is
    # per-course, and THIS course got pt-BR while destruction stays English.
    # ⚠️ The absence of "knowledge-base" here is the whole reason this script
    # exists separately from course_transcribe.py: subtitles for personal study,
    # no tutorials/*.md, no INDEX.md. Phase 3 makes that a composition choice
    # rather than a fork.
    "outputs":      ("subtitles", "translation"),
    # ── layout + ledger shape, consumed by course_engine.course ──────────────
    "layout": "numbered",
    "lesson_slug_fmt": "{prefix} wk{week} {order:02d} {topic_raw}",
    # ⚠️ KEY ORDER IS LOAD-BEARING -- see houdini-wand's note.
    "lesson_seed": {
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
    },
    # Empty on purpose: this course runs no knowledge-base module, so finalize
    # marks only the review flag. §1.4 -- the modules were always separable.
    "finalize_keys": (),
    "translate_to": "pt-BR",
}

DEFAULT_COURSE_ROOT = COURSE["root"]
DEFAULT_COURSE_SLUG = COURSE["slug"]
DEFAULT_INSTRUCTOR  = COURSE["instructor"]
DEFAULT_MODEL       = COURSE["model"]

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

PROFILE = {
    "name":     "russian-native",
    "language": "ru",

    # --- decoder priming -----------------------------------------------------
    # ⚠️ THE most expensive single line in this pipeline. Feeding ingest.py's
    # ENGLISH WHISPER_VOCAB_HINT to a RUSSIAN decode caused Week 1's
    # multilingual-drift disaster (Spanish, Hangul and Chinese bleeding into
    # five lessons). The prompt belongs to the LANGUAGE — never to the engine,
    # and never inherited from a sibling skill. See the block above.
    "initial_prompt":   COURSE_VOCAB_HINT,
    "near_miss_vocab":  ACCENT_RISK_VOCAB,

    # --- flag 1: Whisper's own confidence signals ----------------------------
    # -2.0 sits inside a wide EMPTY measured gap (correct speech -0.5..-1.5,
    # gibberish -4.8..-5.04, nothing between). houdini-wand's English profile
    # uses -0.35 — the same knob, an order of magnitude apart, which is the
    # clearest single proof that these thresholds are language-scoped.
    "avg_logprob_max":       AVG_LOGPROB_FLAG_THRESHOLD,
    "no_speech_prob_min":    0.5,
    # Effectively disabled, not deleted: real correct Russian spans the same
    # 1.24-2.33 range as the transcript max, so English's 2.2 flagged mostly
    # CORRECT segments. Left as a high ceiling in case a genuinely degenerate
    # segment ever exceeds this course's observed range.
    "compression_ratio_min": COMPRESSION_RATIO_FLAG_THRESHOLD,
    # ⚠️ OFF here, ON in houdini-wand. 51 of 91 flags on the wk1-04 test lesson
    # were temperature-alone and every sample checked was correct, coherent
    # speech — Whisper's retry heuristic is tuned around English defaults and
    # fires constantly on short, rapid Russian technical narration. Pure noise
    # on this course, informative on the English one.
    "flag_temperature_fallback": False,

    # --- flag 2: near-miss ---------------------------------------------------
    # ⚠️ Cyrillic AND Latin: loanwords ("TAP", "premult") appear verbatim in
    # Latin script mid-sentence, and a Latin-only regex — houdini's — would
    # never match this course's Cyrillic vocab at all. The CHARSET is part of
    # the language profile, not an implementation detail.
    "word_re":           re.compile(r"[a-zA-Zа-яА-ЯёЁ']+"),
    "near_miss_cutoff":  0.82,
    "near_miss_suffix_tolerance": 3,

    # --- flags 3 & 7 ---------------------------------------------------------
    "near_duplicate_ratio": 0.85,
    "repeat_run_min":       3,   # real finds: "Нюк." 11x over 20s, "Средний
                                 # клавиша." 6x inside one second.
    # ⚠️ NOT cosmetic, and not unifiable with houdini-wand's
    # "run-start-included". This strategy annotates ONLY records that are already
    # flagged, never creates one, and does not sort. Its keying by original
    # transcript index is itself a bug fix: an earlier version used position in
    # the filtered list and merged wk1-06's 20 genuinely separate near-duplicate
    # pairs, ~15 min apart, into one fake "20x burst". Switching strategies would
    # rewrite flags on 109 finalized lessons — decision #1.
    "repeat_burst_strategy": "flagged-only",

    # --- flags 4-6: NOT PORTED HERE ------------------------------------------
    # ⚠️ Recorded as absent rather than silently missing. These three structural
    # detectors were built in houdini-wand on 2026-09-02 and deliberately not
    # back-ported in Phase 0, because porting them means re-running flags on 109
    # finalized Russian lessons and decision #1 forbids retroactive re-runs.
    # Two of them would also fire ZERO times here by measurement: the Russian
    # corpus's observed max is 44 c/s against a 100 c/s threshold.
    # Phase 2 gives them a home; until then this is a knowingly empty seam.
    "flag_duration_overrun": False,
    "impossible_rate_cps":   None,
    "clamped_span":          None,
}

WEEK_DIR_RE   = COURSE["week_dir_re"]
FILE_ORDER_RE = COURSE["file_re"]
VIDEO_EXTS    = COURSE["video_exts"]



# ── Phase 2: the shared engine (ULTIMATE_PIPELINE_PLAN.md §2.2) ───────────────
#
# These operations used to live here as a full second copy of the same code that
# sits in the sibling course script. They now come from `_shared/course_engine`,
# per decision #2 (shared, NOT cloned): one place to fix a bug, one place to keep
# the explanation of why a threshold is what it is.
#
# ⚠️ The names below are re-bound at module level ON PURPOSE, so every existing
# call site in this file keeps working untouched. That is what "thin adapter"
# means here — the engine moved, the script's own shape did not.
#
# ⚠️ Provenance is PRINTED on every run (_shared/ vs vendor/). A vendored
# snapshot silently standing in for a newer shared engine is the same
# missing-evidence-as-clean-result shape this project keeps getting bitten by.

from course_engine_loader import load_course_engine
_ce = load_course_engine(SKILL_DIR)

_ENGINE = _ce.CourseEngine(SKILL_DIR, COURSE["state_defaults"])

course_ingest_dir   = _ENGINE.course_ingest_dir
state_path          = _ENGINE.state_path
load_state          = _ENGINE.load_state
save_state          = _ENGINE.save_state
cmd_check_flags     = _ENGINE.cmd_check_flags
cmd_resolve_flag    = _ENGINE.cmd_resolve_flag
cmd_resolve_range   = _ENGINE.cmd_resolve_range
cmd_bulk_resolve    = _ENGINE.cmd_bulk_resolve

probe_duration      = _ce.probe_duration
format_srt_timestamp = _ce.format_srt_timestamp
write_srt           = _ce.write_srt
_flag_key           = _ce.flag_key
unresolved_flags    = _ce.unresolved_flags

def flag_segments(segments, week=None):
    """Adapter over course_engine.detect.flag_segments — the SHAPE of the flags
    lives in the engine; every Russian-tuned threshold, the Cyrillic charset and
    the repeat-burst strategy arrive from PROFILE above.

    ⚠️ No `duration_sec` parameter, deliberately: this profile leaves the
    structural detectors (4-6) off, so there is nothing here to pass it to. See
    the PROFILE note on why they were not back-ported."""
    return _ce.flag_segments(segments, PROFILE, week=week)


def lesson_slug(week, order, topic_raw):
    return _ce.lesson_slug(COURSE, ingest.slugify, week=week, order=order, topic_raw=topic_raw)


def scan_course(course_root):
    """Adapter -- the walk lives in course_engine.course, selected by
    COURSE["layout"] ("numbered" here: `Week N`/`01 Topic.ext`)."""
    return _ce.scan_course(course_root, COURSE)


def ensure_lessons(state, course_root):
    return _ce.ensure_lessons(state, course_root, COURSE, ingest.slugify)


def cmd_finalize(state, course_slug, slug):
    _ce.finalize(state, slug, COURSE, lambda st: save_state(course_slug, st))


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
            flagged = flag_segments(cached.get("segments", []), entry.get("week"))
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

        flagged = flag_segments(result.get("segments", []), entry.get("week"))
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
