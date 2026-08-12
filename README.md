# Nuke'Em All

An expert consultant for Foundry's compositing/look-dev suite — Nuke, NukeX, Nuke Studio (+ Hiero), Mari, and Katana — that also builds its own knowledge base by ingesting tutorials, and can optionally drive a real, running Nuke session over MCP.

## What it does

Ask it a question about any of Foundry's five apps and it answers from a growing library of ingested tutorials plus a hand-written reference knowledge base covering compositing nodes, keying, deep compositing, Cryptomatte/ST maps, color management (OCIO/ACES), Nuke Python scripting, Nuke Studio/Hiero editorial workflows, Mari texture painting/UDIMs, and Katana lookdev/lighting/USD. It can also write Nuke or Katana Python for you directly.

## Quick start

```powershell
git clone https://github.com/barrozo3d/nuke-em-all.git "$HOME\.claude\skills\nuke-em-all"
cd "$HOME\.claude\skills\nuke-em-all"
.\setup.ps1
```

Then just ask Claude Code a question — it reads `SKILL.md` automatically. Full setup and troubleshooting details live in `SETUP.md`.

---

## The Ingest Pipeline, in full detail

This is the part of the skill you'd actually touch to extend it: give it a video, an article, or any source of technical knowledge and the skill will trigger the steps to extract, read, organize, cross-reference and push it.

```
ingest.py  ──►  select_frames.py  ──►  Claude Code (extraction)  ──►  validate.py
(Step 1:         (Step 2:                (Step 3:                    (integrity
 transcript)      frame capture)          structured notes)           check)
```

### `ingest.py` — Step 1: data collection (no API calls, no video download)

| Function | What it does |
|---|---|
| `_default_whisper_model()` | Picks the default Whisper model size — `small` if a CUDA GPU is available, `base` otherwise. Overridable with `--whisper-model`. |
| `slugify(text)` | Turns a title into a filesystem-safe slug (`tutorials/<slug>.md`) — lowercases, strips punctuation, collapses whitespace to hyphens, caps at 80 chars. |
| `_ytdlp_cmd()` | Builds the base yt-dlp command. Defaults to forcing the `android` player client to dodge YouTube's "Sign in to confirm you're not a bot" 429s; switches to `cookies.txt`-based auth automatically if that file exists in the skill directory. |
| `check_prerequisites()` | Verifies `yt-dlp` is importable (hard requirement, exits if missing); detects whether `ffmpeg` and `whisper` are available (soft — pipeline degrades gracefully without them). |
| `get_info(url)` | Runs `yt-dlp --dump-json` and parses the result: title, uploader, duration, chapters, video ID. |
| `WHISPER_VOCAB_HINT` | A domain-vocabulary string (Nuke/NukeX/Mari/Katana terms: keylight, Cryptomatte, ST map, UDIM, scenegraph, etc.) fed to Whisper as an `initial_prompt` so it transcribes jargon correctly instead of mishearing it (e.g. "Katana" → "Cadana"). |
| `_load_whisper_model(model_name)` | Loads (and caches) a Whisper model, suppressing the noisy first-download progress bar in favor of one clean notice. |
| `whisper_transcribe(audio_path, model_name)` | Runs Whisper transcription with the vocab hint applied. |
| `download_audio(url, tmp)` | Downloads and extracts audio as mp3 (one automatic retry on YouTube throttling failures). |
| `ytdlp_captions(url, tmp)` | Fallback path when Whisper isn't installed or transcription fails: pulls YouTube's own auto-captions and strips VTT markup down to plain text (no per-sentence timestamps in this path). |
| `segment_by_chapters(transcript, chapters)` | Buckets the transcript into per-chapter sections (or one "Full Content" section if the video has no chapters), preserving a per-sentence `(timestamp, text)` list per section — this is what lets Step 2 pick *content-anchored* frame moments instead of guessing blind percentages. |
| `download_video_low(url, tmp)` | Downloads the lowest-quality video stream available (reused by `select_frames.py` — frame pixels don't need to be high-res). |
| `extract_frames(video_path, timestamps, out_dir)` | Runs `ffmpeg -ss <t> -frames:v 1` per timestamp to grab exact stills. |
| `_detect_hallucination(text)` | ASR-hallucination guard: flags a chapter if one content word repeats ≥8 times in its last 50 words (a classic Whisper infinite-loop symptom). |
| `run_safeguards(ch_transcripts)` | Runs all Step-1 quality checks: per-chapter transcript emptiness/shortness, total-transcript-length thresholds (<500 chars = critical, <1200 = warning), and the hallucination check above. Returns `(warnings, critical)`. |
| `_print_safeguard_report(warnings, critical)` | Prints the safeguard findings to the console during the ingest run (`[SAFEGUARD] All checks passed` or a WARNING/CRITICAL list). |
| `build_safeguard_section(warnings, critical)` / `append_safeguard_note(content, note, level)` | Render safeguard findings as a `## Ingest Safeguard Report` markdown block and persist it *inside* the tutorial file — so a `needs-review` flag stays auditable later instead of only ever existing in a terminal that's since closed. Shared with `select_frames.py`, which appends its own frame-capture-time findings into the same section. |
| `build_raw_md(...)` | Assembles the actual `tutorials/<slug>.md` file: YAML frontmatter (title/source/url/author/tags/extraction_status/frame_status) + the chapter-by-chapter timestamped transcript + a `Structured Notes` skeleton full of `[PENDING EXTRACTION]` markers for Step 3 to fill in. |
| `update_index_pending(info, slug, filename, is_yt)` | Appends (or refuses to duplicate) a pending stub entry in `tutorials/INDEX.md`. |
| `update_readme_tutorial_count()` | Recomputes the real on-disk tutorial count and rewrites this README's `**N tutorials ingested**` line — runs automatically at the end of every ingest so the number never goes stale. |
| `fetch_article(url)` | Non-YouTube path: fetches a plain HTML page, strips scripts/styles/tags, and extracts a title + up to 8000 chars of body text for text-only ingestion. |
| `resolve_epic_url(url)` | **Nuke-specific.** Epic Games community pages (`dev.epicgames.com`) embed YouTube videos but block yt-dlp directly (Cloudflare + CSRF). This extracts the readable slug from the URL path, searches YouTube (`ytsearch1:`) for the first match, prints a verification box (title/channel/duration/URL) so a wrong match can be caught before it's ingested, and returns the resolved YouTube URL. Triggered automatically in `main()` whenever the input URL contains `dev.epicgames.com`; `--youtube-url <url>` overrides it with a known-correct URL instead of trusting the search. |
| `find_duplicate_by_video_id(video_id, exclude_name)` | Dedup guard — searches existing tutorial files for the same 11-char YouTube video ID (catches re-ingests where the uploader renamed the video, which a slug/URL-only check would miss). |
| `main()` | Orchestrates all of the above: resolve Epic URLs if needed → fetch metadata → transcribe → segment → run safeguards → write the `.md` file → update `INDEX.md` and `README.md` → `git add` + `commit` + `push`. Flags: `--whisper-model {tiny,base,small,medium,large}`, `--skip-video` (permanently marks `frame_status: skipped`, text-only), `--youtube-url <url>` (override Epic auto-resolution), `--force` (overwrite even if `extraction_status: complete`). |

**Run it:** `python ingest.py "<url>"` from this skill's own directory.

### `select_frames.py` — Step 2: content-aware frame capture

| Function | What it does |
|---|---|
| `parse_timestamp(raw)` | Accepts plain seconds (`"485"`) or `mm:ss` / `h:mm:ss` (`"8:05"`) — Claude picks these by hand after reading the timestamped transcript, not by blind percentage splits. |
| `read_frontmatter_field(content, key)` / `set_frontmatter_field(content, key, value)` | Regex-based YAML-frontmatter getter/setter used to read `frame_status`/`url` and write back `frame_count`/`frame_status`/`frame_selection`. |
| `main()` | Guards against re-capturing an already-`complete` or `skipped` file (unless `--force`), clears stale frames from a prior capture, downloads the low-quality video via `ingest.download_video_low()`, extracts the requested frames via `ingest.extract_frames()`, appends a `## Captured Frames` section, and updates frontmatter. Does **not** commit — that happens together with the Structured Notes in Step 3. |

**Run it:** `python select_frames.py <slug> <ts1> <ts2> ...` (4-8 timestamps is typical) after reading the transcript in `tutorials/<slug>.md`.

### Step 3 — Extraction (done by Claude Code, not a script)

Claude reads each captured frame with the Read tool (which supports images), identifies which app/panel is shown (Nuke node graph vs. viewer, Katana scenegraph, Mari viewport), lists exact node/tool names and parameter values, fills in every `[PENDING EXTRACTION]` marker in the Structured Notes (Core Technique, Summary, Key Steps, Nodes/Tools/Settings, Difficulty, Foundry App & Version, Tags), cross-links related tutorials sharing 2+ tags, sets `extraction_status: complete`, and commits `tutorials/<slug>.md` + `INDEX.md` together.

### `validate.py` — post-ingest integrity checker

| Function | What it does |
|---|---|
| `fail(msg)` | Records a failure message and prints it immediately; feeds the final pass/fail summary. |
| `get_tutorial_files()` | Lists every `tutorials/*.md` file except `INDEX.md`. |
| `parse_index_refs()` | Extracts every `**File:** tutorials/...` reference out of `INDEX.md`. |
| `get_notes_content(content)` | Pulls the `## Structured Notes` section body out of a tutorial file. |
| `is_youtube_source(content)` / `parse_duration_secs(content)` | Read `source:` frontmatter and the `**Duration:**` line. |
| `get_transcript_text(content)` | Reconstructs the raw transcript text from the `## Raw Data` section (stripping out any `## Ingest Safeguard Report` box first, since that has its own `---` divider that would otherwise be mistaken for the section boundary). |
| `check_tutorials()` | Runs checks 1–4 and 8–10: no `[PENDING EXTRACTION]` markers, no `extraction_status: pending`, no `app`/`version` PENDING placeholders, no empty `tags: []`, no `PLACEHOLDER` URLs, structured notes ≥200 chars for YouTube sources, and a transcript-length sanity check (≥3 chars/sec of runtime) for videos over 3 minutes. |
| `check_index()` | Runs checks 5–7: no duplicate `INDEX.md` entries, every disk file is indexed, no `INDEX.md` entry points at a missing file. |
| `check_script_drift()` | Cross-skill check (warn-only, never fails the run): compares this repo's shared helper functions (`slugify`, `download_audio`, `ytdlp_captions`, `segment_by_chapters`, `_detect_hallucination`, `append_safeguard_note`, `find_duplicate_by_video_id`) against the same functions in every sibling skill installed on the same machine, and warns if a copy has drifted — catching an intentional fix in one skill that never got ported to the others. Note: `resolve_epic_url()` is Nuke-specific and deliberately excluded from this comparison — it has no equivalent in the sibling skills. |
| `main()` | Runs all checks, prints a pass/fail summary, exits 1 on any failure. |

**Run it:** `python validate.py` after a batch of ingests, or any time you want to sanity-check the library.

### Extending this pipeline

- **New source type** (e.g. a forum thread, a PDF, another game-engine community-page pattern like `resolve_epic_url()`): follow the `fetch_article()` (generic HTML) or `resolve_epic_url()` (URL-redirect-then-delegate-to-YouTube) pattern — fetch/resolve, then feed the result through the normal `is_yt`/`is_yt=False` path in `build_raw_md()`.
- **New quality check**: add a check function inside `check_tutorials()`/`check_index()` in `validate.py`, following the existing `fail(msg)` pattern.
- **New safeguard**: add a check inside `run_safeguards()` in `ingest.py`, appending to `warnings`/`critical` — it'll automatically get persisted via `build_safeguard_section()`/`append_safeguard_note()`.
- **New reference file**: add `references/<topic>.md`, then add it to the table in `SKILL.md` → "Step 2 — Check Reference Files" so Claude knows when to reach for it.
- **Point it at a live Nuke session**: see "Live connection" below — no pipeline code changes needed, it's a separate MCP layer covering Nuke/NukeX only.

---

## Every mode this skill supports

| Mode | Trigger phrases | What happens |
|---|---|---|
| **Setup** | "set up this skill", "new machine", "check if installed", "is this configured", "help me install this" | Walks the `SETUP.md` "For Claude: New Machine Setup Protocol" checklist (Python/ffmpeg/yt-dlp/whisper/torch/skill presence), reports what's missing, fixes it. |
| **1 — Consult / Answer** | "how do I", "what node", "what's the best way to", "explain", "why is", "help me with", "how does X work in Nuke/Mari/Katana" | Searches `tutorials/INDEX.md` + the 7 `references/*.md` files, then answers with Approach / Step-by-Step / Key Settings / Python (if applicable) / Gotchas / Related Entries — always states which of the five apps the answer applies to. |
| **2 — Write Code** | "write me a nuke script", "python for nuke", "gizmo for", "give me the code", "katana macro for" | Writes real Nuke or Katana Python directly (TCL only mentioned for legacy-script maintenance) — states app/context, uses `nuke.nodes.X()` over `nuke.createNode()` for non-interactive generation, cites the reference file the pattern came from. |
| **3 — Ingest** | "ingest", "learn from", "add this tutorial", "add this book", "read this chapter" | Runs the full 3-step pipeline above, unprompted through all three steps (does not wait to be asked for Step 2/3). |
| **4 — Live Nuke Connection (optional, Nuke/NukeX only)** | "build this in my open Nuke", "clean up my node graph", "wire this comp for me live", "connect to my running Nuke session" | Checks `SETUP.md` → "Nuke MCP Connection" first — walks through setup if not configured, otherwise drives the live session. No equivalent for Nuke Studio, Mari, or Katana; those requests are redirected to Mode 1/2. |

**Auto-Changelog Rule (Mode 0 — Version Check):** at the start of every consultation, if `references/version-tracker.md`'s `last_checked` date is over 7 days old, the skill fetches the release-notes URLs for each app, checks for versions not yet in the Known Versions table, and if found researches headline changes and creates `references/release-notes-<app>-<version>.md` — so recommendations don't quietly go stale as Foundry ships new features (e.g. Nuke 17.0's Gaussian Splat support, Katana 9.0's UsdSuperLayer). Skipped when the user is clearly in a hurry.

## Live connection (optional, Nuke/NukeX only)

Nuke ships no built-in MCP bridge, but two independent, third-party open-source projects wrap a Nuke-side addon + local MCP server:

| Option | Coverage | License | Notes |
|---|---|---|---|
| `CreativeLyons/nuke-mcp2` | Broader (tested Nuke 13.x–15.x), more tool categories (camera tracking, deep comp, template/toolset management, CopyCat/ML, keying, batch processing) | — | Recommended default — automated `setup.bat`/`setup.sh` installer, default port 9876 |
| `dughogan/nuke_mcp` | Smaller surface area, course-backed (fxphd "Build Your Own AI Copilot in Nuke") | MIT | Simpler minimal alternative — `pip install fastmcp` + a socket-server addon in `~/.nuke/python` |

Both require Nuke actually installed and running; neither is active by default and this repo does not assume either is configured. **Covers Nuke/NukeX only** — no MCP bridge exists for Nuke Studio, Mari, or Katana, so those three stay consultant-only (Mode 1/2) regardless of setup. Full setup steps: `SKILL.md` → "Live Nuke Connection", `SETUP.md` → "Nuke MCP Connection".

## Repo structure

```
nuke-em-all/
├── SKILL.md               ← main skill instructions Claude reads
├── README.md               ← this file
├── SETUP.md               ← human + Claude setup guide
├── CODE_OF_CONDUCT.md     ← purpose/ethics statement
├── setup.ps1              ← Windows automated installer (ingest pipeline only)
├── ingest.py               ← Step 1: transcript/metadata collection (no video/frames)
├── select_frames.py        ← Step 2: content-aware frame capture (Claude picks timestamps)
├── validate.py              ← post-ingest integrity checker
├── requirements.txt        ← pip dependency list
├── references/             ← Nuke/Mari/Katana knowledge base (7 files)
│   ├── nuke-compositing-nodes.md
│   ├── nuke-python-scripting.md
│   ├── nuke-studio-hiero.md
│   ├── mari-texturing.md
│   ├── katana-lookdev-lighting.md
│   ├── foundations-overview.md
│   └── version-tracker.md
└── tutorials/
    ├── INDEX.md            ← searchable catalog of all ingested tutorials
    └── *.md                ← one file per ingested tutorial
```

## Sibling skills

Same ingest/validate/setup architecture as this skill's siblings — `blender-motion`, `houdini-wand`, `unreal-sidekick`, and `paint-me-like-your-french-substances` — each covering a different DCC/VFX toolset. `validate.py`'s drift check compares shared pipeline internals across all five and warns (never fails) if a copy has drifted.

## Status

Public personal project, no warranty. **3 tutorials ingested** (count auto-updates on every `ingest.py` run — do not hand-edit this line).
