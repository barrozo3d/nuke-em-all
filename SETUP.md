# nuke-em-all — Setup Guide

This file serves two purposes:
- **For you (human):** step-by-step instructions to get the skill running on a new machine
- **For Claude:** checklist to follow when the user says "set up this skill", "check if installed", or "new machine setup"

---

## For Claude: Setup Sync Rule

**Every structural change to the skill must update these three files in the same commit.**

A structural change is anything that would affect how someone installs or runs this skill on a fresh machine:
- New pip dependency added to `ingest.py` or any script → update `requirements.txt` + `setup.ps1` (pip install step) + `SETUP.md` (Step 3 or Troubleshooting)
- New system dependency (new tool required) → update `setup.ps1` + `SETUP.md`
- New environment variable required → update `setup.ps1` + `SETUP.md` (add a step + Troubleshooting entry)
- New CLI flag added to `ingest.py` or `select_frames.py` → update `SETUP.md` (Ingest Pipeline Reference section)
- Directory or file renamed/added → update `SETUP.md` (Skill Structure section)
- Git repo URL changed → update `SETUP.md` (Step 2) + `setup.ps1` (clone URL comment)

**Commit + push format for structural changes:**
```
git add ingest.py requirements.txt setup.ps1 SETUP.md
git commit -m "feat/fix: <what changed> + sync setup pack"
git push
```

Never leave setup files out of sync with the actual skill state. The push is mandatory — the GitHub copy is what other machines clone, so a local-only commit is not enough.

---

## For Claude: New Machine Setup Protocol

When the user says any of: "set this up", "new machine", "is this installed", "check dependencies", "help me configure this skill" — follow this checklist in order. Run each check as a shell command, report results, and fix what's missing.

```
CHECKLIST:
1. python --version                          → need 3.10+
2. ffmpeg -version                           → need any version on PATH
3. python -c "import yt_dlp"                 → need installed
4. python -c "import whisper"                → need installed
5. python -c "import torch; print(torch.cuda.is_available())"  → True = GPU ready
6. Test-Path ~\.claude\skills\nuke-em-all\SKILL.md   → need True
```

For anything missing:
- **ffmpeg missing** → `winget install ffmpeg`
- **pip packages missing** → `pip install yt-dlp openai-whisper`
- **torch CPU-only** → `pip install torch --force-reinstall --index-url https://download.pytorch.org/whl/cu128`
- **Skill not found** → `git clone https://github.com/barrozo3d/nuke-em-all.git ~\.claude\skills\nuke-em-all`

After fixing, re-run the checklist and confirm all green before proceeding.

This checklist covers the **ingest/consultant pipeline only**. The optional live Nuke connection (see "Nuke MCP Connection" below) is a separate setup that requires Nuke itself installed and is never assumed to be ready — only walk through it if the user explicitly asks for Mode 4 (live Nuke connection).

---

## System Requirements

| Requirement | Minimum | Recommended |
|---|---|---|
| OS | Windows 10 / macOS 12 / Ubuntu 20.04 | Windows 11 |
| Python | 3.10 | 3.11–3.12 |
| RAM | 8 GB | 16 GB+ |
| GPU | — (CPU works) | NVIDIA RTX (any) for fast Whisper |
| Disk | 5 GB free | 10 GB (Whisper models cache here) |
| Internet | Required for ingest | — |
| Nuke / NukeX / Nuke Studio / Mari / Katana | Not required for consulting | Only needed for Mode 4 (live Nuke connection) or to run generated code |

---

## Step 1 — Install Claude Code

If Claude Code isn't installed yet:
- Download from: https://claude.ai/download
- Or install the VS Code extension: search "Claude" in Extensions

---

## Step 2 — Clone the Skill

Open PowerShell and run:

```powershell
git clone https://github.com/barrozo3d/nuke-em-all.git "$HOME\.claude\skills\nuke-em-all"
```

> If you don't have git: `winget install git`

---

## Step 3 — Run the Setup Script

```powershell
cd "$HOME\.claude\skills\nuke-em-all"
.\setup.ps1
```

The script will:
- Check Python version
- Install `ffmpeg` via winget
- Install `yt-dlp`, `openai-whisper` via pip
- Install PyTorch with CUDA support (if NVIDIA GPU detected)

> **Note:** The CUDA torch download is ~2.8 GB. It may take 10–30 minutes depending on your connection.
> This script does **not** touch the optional Nuke MCP connection — see below for that, separately.

---

## Step 4 — Verify

```powershell
ffmpeg -version
python -c "import whisper, yt_dlp; print('all OK')"
python -c "import torch; print('CUDA:', torch.cuda.is_available())"
```

Expected output:
```
ffmpeg version 8.x ...
all OK
CUDA: True    ← only if NVIDIA GPU present
```

---

## Step 5 — Test Ingest

Run a quick test without downloading the full video:
```powershell
cd "$HOME\.claude\skills\nuke-em-all"
python ingest.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --skip-video
```

Step 1 alone (`ingest.py`, with or without `--skip-video`) never downloads video anymore — it only collects transcript + metadata, so this test runs in ~2 minutes either way. `--skip-video` instead permanently marks the tutorial `frame_status: skipped` (use it for text-only ingests where frame capture will never apply); without it, frames stay `pending-selection` until you run `select_frames.py`.

---

## Nuke MCP Connection (optional, Nuke/NukeX only)

This is a **separate, manual, opt-in setup** — not part of `setup.ps1`, and not required for consulting or ingesting. It connects Claude directly to a *running Nuke session* so it can create/wire nodes and drive the comp live. Requires The Foundry's Nuke actually installed. No equivalent exists for Nuke Studio, Mari, or Katana.

Two documented third-party (non-Foundry) options — full detail and repo links in `SKILL.md` → "Live Nuke Connection":

- **`CreativeLyons/nuke-mcp2`** (recommended default — broader Nuke version support, automated `setup.bat`/`setup.sh`, more tool categories including camera tracking/deep comp/CopyCat).
- **`dughogan/nuke_mcp`** (simpler, MIT-licensed, course-backed — good minimal alternative).

General shape of the setup (exact steps live in the chosen repo's own README — verify against it, since these are independently-maintained community projects, not part of this skill):
1. Confirm Nuke is installed (`nuke --version`).
2. Clone/download the chosen MCP repo.
3. Run its installer (or manually place its Nuke-side addon script in `~/.nuke/` per its instructions) so a socket/MCP server starts inside Nuke.
4. Install its Python-side MCP server dependencies (e.g. `pip install fastmcp` for `dughogan/nuke_mcp`).
5. Point Claude Desktop/Claude Code's MCP config at that server (each repo provides or generates the config snippet).
6. Restart Nuke and Claude, then test with a trivial request ("add a Blur node") before relying on it for real work.

---

## YouTube Bot Detection / SABR streaming (cookies.txt)

`ingest.py` automatically passes `--extractor-args youtube:player_client=web_embedded` on every call that doesn't have a `cookies.txt` present. This needs no setup — it's built into `_ytdlp_cmd()` in `ingest.py`. History of why:

- Originally the plain `web_safari` default client started throwing HTTP 429 + `Sign in to confirm you're not a bot` on many videos, so the `android` client was forced instead (its single combined mp4, itag 18, needed no PO token).
- As of 2026-08, `android`'s itag-18 stream started tripping YouTube's **SABR-only streaming experiment** on some connections: the download would repeatedly die mid-transfer with `Connection aborted` after ~1%, even across retries, `--limit-rate`, or a fresh yt-dlp nightly (see [yt-dlp#12482](https://github.com/yt-dlp/yt-dlp/issues/12482)). `web_embedded` sidesteps this — it doesn't need a PO token (unlike bare `web`/`mweb`), doesn't hit the `tv` client's DRM flag, and exposes real audio-only (opus/m4a) and video-only DASH streams, so `download_audio()` requests `bestaudio/best` and `download_video_low()` requests `bestvideo[height<=240]` directly instead of being stuck with one flaky muxed format.
- `web_embedded` requires solving YouTube's JS "n-challenge" (via `deno`, see the Deno section above) and a yt-dlp build recent enough to ship the bundled EJS challenge solver — the nightly/`--pre` channel pulled in by `requirements.txt` (see below) covers this; if you installed yt-dlp long ago via a plain `pip install yt-dlp`, re-run `pip install -U --pre "yt-dlp[default]"` to pick up EJS support.

If a video *still* fails under `web_embedded` too (rare — seen mainly on age-restricted or region-locked videos), fall back to cookies. Chrome 127+ broke yt-dlp's automatic cookie extraction (`--cookies-from-browser` fails with DPAPI error), so this has to be manual:

1. Install the **"Get cookies.txt LOCALLY"** extension in Chrome/Edge/Firefox
2. Go to **youtube.com** while logged in to your Google account
3. Click the extension icon → **Export** → save as **`cookies.txt`**
4. Place `cookies.txt` in `~/.claude/skills/nuke-em-all/` (same folder as `ingest.py`)
5. `ingest.py` detects it automatically and switches to cookie auth (dropping the `web_embedded`-client arg) — no other changes needed

> `cookies.txt` is in `.gitignore` and will never be committed to GitHub.

---

## Troubleshooting

**`ffmpeg: command not found` after install**
Open a new PowerShell window — PATH updates don't apply to the current session.

**`ModuleNotFoundError: No module named 'whisper'`**
```powershell
pip install openai-whisper
```

**`CUDA: False` when you have an NVIDIA GPU**
```powershell
pip install torch --force-reinstall --index-url https://download.pytorch.org/whl/cu128
```

**Git push fails (authentication)**
```powershell
git config --global credential.helper manager
```
Then re-run the push — Windows Credential Manager will prompt for GitHub login.

**Whisper model download on first run**
The first time Whisper runs it downloads the model (~150 MB for `base`, ~461 MB for `small` — the default on CUDA machines). ingest.py prints a single "downloading weights (one-time)" notice instead of a progress bar. This is normal — subsequent runs use the cached model.

**No Foundry apps installed — skill still works**
The nuke-em-all skill operates in consultant mode by default (no direct app connection required). You don't need Nuke, Mari, or Katana installed to ask questions, get Python code, or ingest tutorials. You only need Nuke installed for the optional Mode 4 live connection, or any of the five apps to actually run generated code.

**Nuke MCP connection not responding**
Confirm Nuke is actually running with the addon loaded (check its menu for an "MCP" entry, per the chosen repo's docs), confirm the local server process is running, and confirm the port (default 9876 for `nuke-mcp2`) isn't blocked by a firewall. This connection is entirely separate from this skill's own scripts — if it's broken, `SKILL.md` Mode 1/2 (consult / write code) still work normally.

---

## Skill Structure (reference)

```
nuke-em-all/
├── SKILL.md               ← main skill instructions Claude reads
├── README.md               ← human-facing overview
├── SETUP.md               ← this file
├── CODE_OF_CONDUCT.md     ← purpose/ethics statement
├── setup.ps1              ← Windows automated installer (ingest pipeline only)
├── ingest.py               ← Step 1: transcript/metadata collection (no video/frames)
├── select_frames.py        ← Step 2: content-aware frame capture (Claude picks timestamps)
├── validate.py              ← post-ingest integrity checker
├── requirements.txt        ← pip dependency list
├── references/             ← Nuke/Mari/Katana knowledge base
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

---

## Ingest Pipeline Reference

The pipeline is two scripts, run in sequence — frame capture is a deliberate,
content-aware step done by Claude Code, not something either script guesses at:

```
Step 1 — collect transcript only, no video/frames:
python ingest.py <url>
python ingest.py <url> --skip-video            article/text-only ingest, no frames ever
python ingest.py <url> --whisper-model medium  best accuracy, much slower
# Default model is auto-selected: "small" when a CUDA GPU is available, else "base".
# Pass --whisper-model explicitly to override either way.
python ingest.py <url> --force                 re-collect even if extraction_status: complete (overwrites Structured Notes)

Step 2 — after reading the timestamped transcript, capture the chosen moments:
python select_frames.py <slug> <ts1> <ts2> ...   seconds or mm:ss, e.g. 10 60 4:20 8:05
python select_frames.py <slug> ... --force       re-capture even if frame_status: complete
```

`ingest.py` refuses to overwrite a tutorial `.md` whose frontmatter already has `extraction_status: complete`, to protect hand-written Structured Notes from being wiped by an accidental re-ingest. Pass `--force` only when you intend to discard the existing extraction and will re-run the extraction pass afterward. `select_frames.py` has the same guard on `frame_status: complete`.

Pipeline stages:
1. yt-dlp metadata + chapter list
2. Whisper transcription (or yt-dlp captions fallback), per-sentence timestamps preserved even inside chapters
3. Transcript segmented by chapter
4. Write `tutorials/<slug>.md` (`frame_status: pending-selection`) + update `INDEX.md` + git push — **no video download, no frames yet**
5. Claude Code reads the timestamped transcript and picks 4-8 content-anchored moments (not blind percentages)
6. `select_frames.py <slug> <timestamps>` downloads the low-quality video, extracts exactly those frames to `tutorials/frames/<slug>/`, sets `frame_status: complete` — not committed yet
7. Claude Code vision-reads each captured frame (Nuke node graph, Katana scenegraph, Mari viewport, Python code) and writes the Structured Notes (core technique, steps, nodes/tools, tags)
8. Auto cross-linking with existing tutorials (2+ shared tags)
9. Update `INDEX.md`, commit `.md` + `INDEX.md` together, git push

## Frame capture height (`INGEST_FRAME_HEIGHT`)

Frames are captured at **1080p** in this skill (dense DCC UI — Nuke's node graph and properties panels), set by
`DEFAULT_FRAME_HEIGHT` at the top of `ingest.py`. The value is per-skill on
purpose: `download_video_low()` itself is drift-gated across all five skills, so
its source stays identical while only the constant changes.

Raise or lower it for a single run without editing anything:

```
# PowerShell
$env:INGEST_FRAME_HEIGHT = "1080"; python ingest.py <url>
# bash
INGEST_FRAME_HEIGHT=1080 python ingest.py <url>
```

Why it matters: frames are how a claim gets checked against what was actually on
screen, and text that cannot be read cannot settle anything. Frames below **480p**
count as blind-era and `reground_frames.py` treats them as needing re-capture.
Raise this when a tutorial is a UI-heavy screencast and lower it only if disk or
bandwidth genuinely bites — the cap exists for download cost, not quality.

> This variable existed for weeks before being documented here, and so defaulted
> to 720p everywhere by accident. Per the Setup Sync Rule at the top of this
> file, a new environment variable must be added here in the same change.

## Note: captured frames are local-only

`tutorials/frames/` is gitignored — frame images never sync to GitHub. On a fresh
clone, `frame_status: complete` in a tutorial's frontmatter refers to frames that
existed on the machine that ingested it; the durable knowledge is the extracted
Structured Notes, not the images. If you need the stills again on this machine,
re-capture them with:

```
python select_frames.py <slug> <ts1> <ts2> ... --force
```

(timestamps are listed in the tutorial file's "Captured Frames" section).

## Ingest environment variables

Three knobs, all optional, all read at ingest time. Defaults are what every
batch run has used — set them only for a specific reason.

| variable | default | what it does |
|---|---|---|
| `INGEST_FRAME_HEIGHT` | per-skill (see above) | max height for the frame-capture download |
| `INGEST_PROMPT_PRIMING` | `1` (on) | extend Whisper's `initial_prompt` with this video's own title, chapter titles and technical description terms |
| `INGEST_CAPTION_CROSSCHECK` | `1` (on) | fetch YouTube's auto-captions as a second, independent ASR witness and report Whisper spans it does not support |

```
# PowerShell
$env:INGEST_PROMPT_PRIMING = "0"; python ingest.py <url>
# bash
INGEST_CAPTION_CROSSCHECK=0 python ingest.py <url>
```

**`INGEST_PROMPT_PRIMING`** — a tutorial description usually names the exact
nodes being demonstrated, and `--dump-json` already fetched it before any audio
is decoded. Priming makes Whisper far likelier to emit `Cull Volume` than
`call volume`, attacking the mishear class at the source instead of detecting it
afterwards. Candidates are ranked chapter titles → video title → technical
tokens from the description, capped at Whisper's ~224-token prompt window.

> ⚠️ Non-Latin-script metadata is **dropped, never transliterated**. A
> wrong-language `initial_prompt` is the single most expensive bug in this
> pipeline's history — an English hint driving a Russian decode bled Spanish,
> Hangul and Chinese into five lessons. A Japanese title appended to an English
> prompt is that same mistake through a different door.

**`INGEST_CAPTION_CROSSCHECK`** — Whisper fabricates over silence; Google's ASR
generally emits nothing there. So a Whisper segment with no caption counterpart
in its window is a fabrication *candidate*, reported in the Ingest Safeguard
Report. Turn it off to skip one extra yt-dlp call per ingest.

> ⚠️ It reports, it never overrules. Auto-captions carry their own errors, so
> disagreement means "listen to this span", not "Whisper is wrong". An empty
> result can also mean the video simply has no caption track — **no witness
> available is not the same as no problems found**, and the run prints which of
> the two it got.

## Shared engine (`_shared/course_engine`)

The local-course pipeline's core lives in a **sibling repo**, not in this one:

```
~/.claude/skills/
  _shared/          <- github.com/barrozo3d/course-engine
  houdini-wand/
  nuke-em-all/
```

Clone it once per machine, beside the skills:

```powershell
git clone https://github.com/barrozo3d/course-engine.git "$HOME\.claude\skills\_shared"
```

**You do not have to.** Each skill ships a generated snapshot at
`vendor/course_engine/`, so a standalone `git clone <this skill>` runs fine
without `_shared/`. Cloning `_shared/` is what you want when you intend to
*change* the engine — a fix made there reaches every skill at once, which is the
entire reason it is one repo rather than a copy per skill.

Every run prints which one it loaded:

```
[engine] course_engine 0.1.0 from _shared/     <- editable, shared
[engine] course_engine 0.1.0 from vendor/      <- snapshot, standalone clone
```

> ⚠️ That line is not noise, and `INGEST_ENGINE_QUIET=1` suppressing it is a
> trade you should make deliberately. A vendored snapshot quietly standing in for
> a newer shared engine is the same failure this repo keeps meeting in other
> forms — an empty Prefetch folder reading as "nothing ran", a permission-denied
> log reading as "no events". Missing evidence must not look like a clean result.

After changing anything in `_shared/course_engine/`, regenerate the snapshots and
commit them with your change:

```powershell
python "$HOME\.claude\skills\_shared\sync_vendor.py"          # write
python "$HOME\.claude\skills\_shared\sync_vendor.py" --check  # report drift only
```

`vendor/` is **generated — never hand-edit it.** An edit there is lost on the
next sync and silently diverges from `_shared/` until then.
