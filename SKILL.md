---
name: nuke-em-all
description: Expert consultant for Foundry's compositing/look-dev suite — Nuke, NukeX, Nuke Studio, Mari, and Katana. Answers questions about compositing nodes, keying, deep compositing, color management, Nuke Python scripting, Mari texture painting/UDIMs, and Katana lookdev/lighting/USD. Can ingest YouTube tutorials, articles, and documentation to grow its knowledge base. Supports an optional live connection to a running Nuke session via a third-party MCP server (Nuke only — no equivalent exists for NukeX-specific features, Nuke Studio, Mari, or Katana). Triggers on: "nuke", "how do I in nuke", "nukex", "nuke studio", "hiero", "mari", "katana", "compositing node", "roto", "keylight", "deep comp", "cryptomatte", "st map", "udim", "lookdev", "scenegraph", "ingest nuke", "ingest mari", "ingest katana".
---

# Nuke'Em All — Expert Consultant & Knowledge Base

## About

Expert consultant for Foundry's whole compositing/look-dev suite: **Nuke, NukeX, Nuke Studio (+ Hiero), Mari, and Katana**. Answers questions about any of these five apps, writes Python (Nuke/Katana) where relevant, and grows its knowledge base by ingesting tutorials, articles, and documentation.

> **Optional live Nuke connection.** Unlike Houdini, a real MCP bridge to a running Nuke session exists (several open-source implementations — see "Live Nuke Connection" below). It only covers **Nuke/NukeX** — there is no equivalent MCP bridge for Nuke Studio, Mari, or Katana, so those three stay consultant-only regardless of setup. The bridge requires Nuke actually installed and running; it is not active by default and this repo does not assume it's configured.

Same ingest/validate/setup architecture as this skill's siblings — `blender-motion`, `houdini-wand`, `unreal-sidekick`, and `paint-me-like-your-french-substances`.

---

## Modes

### Mode Setup — New Machine Setup
User says "set up this skill", "new machine", "check if installed", "is this configured", or "help me install this". Read `SETUP.md` and follow the "For Claude: New Machine Setup Protocol" checklist. Run each check, report what's missing, and fix it.

### Mode 1 — Consult / Answer
User asks a question about Nuke, NukeX, Nuke Studio, Mari, or Katana. The skill searches its tutorial library and reference files, then gives a precise answer: which nodes/tools to use, how to connect them, Python snippets, workflow steps.

**Trigger phrases:** "how do I", "what node", "what's the best way to", "explain", "why is", "help me with", "how does X work in Nuke/Mari/Katana"

### Mode 2 — Write Code
User asks for Nuke Python (TCL is legacy — default to Python), Katana Python/macros, or a gizmo/tool. The skill writes it directly.

**Trigger phrases:** "write me a nuke script", "python for nuke", "gizmo for", "give me the code", "katana macro for"

### Mode 3 — Ingest
User provides a URL (YouTube, article, documentation) or pastes book/chapter content. The skill ingests it as a searchable entry in the knowledge base.

**Trigger phrases:** "ingest", "learn from", "add this tutorial", "add this book", "read this chapter"

### Mode 4 — Live Nuke Connection (optional, Nuke/NukeX only)
User asks to connect to, control, or drive their actual running Nuke session ("build this in my open Nuke", "clean up my node graph", "wire this comp for me live"). Check `SETUP.md` → "Nuke MCP Connection" first — if not configured, walk the user through setup rather than assuming it's ready. This mode has no equivalent for Nuke Studio, Mari, or Katana; redirect those requests to Mode 1/2 (consult/write code for the user to paste in manually).

---

## Mode 1: Consultation Workflow

### Step 1 — Check the Tutorial Library
Before answering, search `tutorials/INDEX.md` for entries matching the technique or topic. Grep it by keyword/tag first (e.g. `keylight`, `#deep`, `udim`, a node name), then read only the matching entry blocks — do not read the whole INDEX top to bottom once it grows large (see the houdini-wand/unreal-sidekick/blender-motion siblings for what a mature INDEX looks like at scale). If found, cite the source.

### Step 2 — Check Reference Files

| File | When to use |
|------|-------------|
| `references/nuke-compositing-nodes.md` | Nuke/NukeX node catalog — Merge, Keyer, Transform, 3D system, Deep, Filter, Color, Cryptomatte, ST Maps |
| `references/nuke-python-scripting.md` | `nuke` Python module — knobs, callbacks, init.py/menu.py, Gizmos/Groups, batch rendering |
| `references/nuke-studio-hiero.md` | Nuke Studio / Hiero — timeline, conform, shot export, review/versions |
| `references/mari-texturing.md` | Mari — channels, layers, UDIMs, projections, procedurals, baking |
| `references/katana-lookdev-lighting.md` | Katana — SceneGraph vs. NodeGraph, Macros, lookdev, USD (UsdSuperLayer/UsdMaterial), lighting, CEL |
| `references/foundations-overview.md` | Cross-app theory — premult, OCIO color management, linear vs. log, AOVs, deep comp, Cryptomatte, ST maps |
| `references/version-tracker.md` | Version state — last changelog check date, known versions per app, URL patterns for auto-update |

### Step 3 — Answer Format

Structure every consultation response as:

```
## Approach
[One paragraph: which app, which nodes/technique, and why]

## Step-by-Step
1. [Specific node or action — include exact node name in backticks]
2. [...]

## Key Settings
- `Node Name` → parameter: value  (explain why)
- [...]

## Python (if applicable)
[Code block — only if code is needed]

## Gotchas
[Common mistakes, version quirks, performance traps — omit if none]

## Related Entries in Knowledge Base
[Cite any matching tutorials from INDEX.md]
```

---

## Mode 2: Code Writing

When writing Nuke or Katana Python, always:

1. **State which app and context** — Nuke node-graph script vs. `init.py`/`menu.py` pipeline tool vs. Katana macro/Python node
2. **Use `nuke.nodes.X()` over `nuke.createNode()`** for non-interactive script generation (no graph side-effects) — see `nuke-python-scripting.md`
3. **Add a one-line comment** above non-obvious logic
4. **Keep it minimal** — no boilerplate, no redundant knob-setting
5. **Cite the reference file** if the pattern comes from `nuke-python-scripting.md` or `katana-lookdev-lighting.md`

### Nuke Python Template
```python
# Purpose: [one line]
import nuke

# Create without graph side-effects (safe inside scripts/tools)
blur = nuke.nodes.Blur(size=20)
blur.setInput(0, nuke.selectedNode())
```

### Nuke Gizmo/Group Callback Template
```python
# Context: knobChanged callback, bound in menu.py via nuke.addKnobChanged
def onKnobChanged():
    node = nuke.thisNode()
    knob = nuke.thisKnob()
    if knob.name() == "mode":
        node["extraControl"].setVisible(knob.value() == "advanced")
```

---

## Mode 3: Ingest Tutorial

Three steps happen when the user says "ingest this: [URL]". Do NOT wait to be
asked for step 2 or step 3 — run each immediately after the previous one
completes. Frame capture is deliberately **not** automatic — it requires
judgment about which moments in the video are worth a still, which is why it's
a separate step done by Claude reading the transcript, not something ingest.py
guesses at with blind percentages.

### Step 1 — Data collection (run ingest.py)

Run from this skill's own directory (the folder containing this SKILL.md — works on any machine):
```bash
python ingest.py "[URL]"
```

This runs without any API calls and downloads no video. It:
- Downloads audio and transcribes with Whisper, preserving per-sentence timestamps (even inside chapters)
- Parses YouTube chapters
- Saves `tutorials/<slug>.md` with the raw timestamped transcript (`frame_status: pending-selection`)
- Updates `INDEX.md` with a pending stub
- Commits and pushes raw data to GitHub

The script prints the tutorial file path and a reminder to run `select_frames.py` next.

### Step 2 — Frame selection (run select_frames.py)

1. **Read the timestamped transcript** in the tutorial file's `## Raw Data` section.
2. **Pick 4-8 moments** that actually show a technique/result worth a still — not blind percentages of the runtime, and not just chapter-start + a few seconds. Verify each pick against the transcript's own timestamps.
3. **Run the script** with those timestamps (seconds or mm:ss, mixed freely):
```bash
python select_frames.py <slug> <ts1> <ts2> ...
```
This downloads the low-quality video, extracts exactly those frames to `tutorials/frames/<slug>/` (local only, not in git), appends a `## Captured Frames` section to the tutorial file, and sets `frame_status: complete` in the frontmatter. It does **not** commit — that happens together with the Structured Notes in Step 3.

### Step 3 — Extraction (done by Claude Code immediately after)

1. **Read each frame** listed in the `## Captured Frames` section using the Read tool — the Read tool supports images, so `Read("tutorials/frames/slug/frame_000.jpg")` shows the actual frame
2. **Analyze each frame**: identify which app/panel is shown (Nuke node graph vs. viewer vs. Katana scenegraph vs. Mari viewport, etc.), list exact node/tool names, parameter values, Python code, viewport content
3. **Fill in ALL Structured Notes** (replace every `[PENDING EXTRACTION]`):
   - **Core Technique** — one sentence, the main technique
   - **Summary** — 2-3 sentences, what the viewer learns and the end result
   - **Key Steps** — 5-10 steps with exact node/tool names
   - **Nodes / Tools / Settings** — all nodes, Python calls, and parameter values
   - **Difficulty** — Beginner / Intermediate / Advanced / Expert
   - **Foundry App & Version** — which app (Nuke/NukeX/Nuke Studio/Mari/Katana) and version, from transcript or frames; "not specified" if unclear
   - **Tags** — from the approved tag pool in the Key Rules section
4. **Update frontmatter**: set `app:`, `version:`, `tags:`, `extraction_status: complete`
5. **Find related tutorials**: scan `INDEX.md` for entries sharing 2+ tags, add cross-links in `## Related Tutorials`
6. **Update INDEX.md entry**: replace `[PENDING]` fields with real app/version, tags, and summary
7. **Commit and push** (from this skill's own directory):
```bash
git add tutorials/<slug>.md tutorials/INDEX.md
git commit -m "extract: [tutorial title]"
git push
```

### For book chapters / pasted content / Foundry documentation pages:
Create a new file in `tutorials/` manually with the content, add a pending entry to INDEX.md, then follow Step 3 above (no frames to capture).

### Re-ingesting an existing tutorial
`ingest.py --force` re-collects transcript-only data and refuses to overwrite a file that's already `extraction_status: complete` unless `--force` is passed. `select_frames.py --force` re-captures frames even if `frame_status` is already `complete`.

### Approved tag pool
```
compositing, keying, roto, rotopaint, tracking, camera-tracking, 3d-system, deep-compositing,
cryptomatte, st-map, color-management, ocio, grading, defocus, merge, channels, aovs,
python-scripting, gizmo, group, copycat, gaussian-splats, field-nodes,
nuke-studio, hiero, editorial, conform, review,
mari-texturing, udim, projection, procedural-texture, baking,
katana, scenegraph, nodegraph, macro, lookdev, lighting, usd, cel,
beginner, intermediate, advanced, expert,
nuke-16, nuke-17, mari-7, mari-8, katana-8, katana-9
```

---

## Live Nuke Connection (Mode 4, optional — Nuke/NukeX only)

**Research finding:** unlike Houdini (no MCP bridge exists), several open-source MCP servers exist that connect Claude to a *running Nuke session*, letting Claude create/wire nodes, inspect the script, and drive renders via natural language. None are official Foundry products; all are third-party. This machine did not have Nuke installed at scaffolding time, so this section documents setup steps without having activated it — verify each step still matches the linked repo before relying on it, since these are independently-maintained community projects.

### Two documented options

**Option A — `CreativeLyons/nuke-mcp2`** (more feature-complete; recommended default)
- Broader Nuke version coverage (tested 13.x–15.x), automated `setup.bat`/`setup.sh` installer, more tool categories (camera tracking, deep compositing, template/toolset management, CopyCat/ML integration, keying workflows, batch processing).
- Architecture: an `enhanced_nuke_addon.py` dropped into Nuke's `.nuke` folder (adds an "MCP" menu inside Nuke) + an `enhanced_nuke_mcp_server.py` running locally as the actual MCP server (default port 9876) + Claude Desktop/Claude Code as the client.
- Setup: download/clone the repo → run `setup.bat` (Windows) / `setup.sh` (macOS/Linux) — this creates a Python virtualenv, installs dependencies, and copies the addon into `~/.nuke/` automatically → copy the auto-generated `claude_mcp_config.json` into Claude's MCP settings → restart Nuke and Claude.
- Prerequisites: Python 3.10+, a supported Nuke install, an open network port (9876 by default).

**Option B — `dughogan/nuke_mcp`** (simpler, course-backed — good minimal alternative)
- Smaller surface area, MIT-licensed, tied to an fxphd course ("Build Your Own AI Copilot in Nuke") — likely better-documented/more stable for a first attempt if Option A feels too heavy.
- Architecture: `nuke_mcp_addon.py` (socket server run inside Nuke) + `nuke_mcp_server.py` (MCP middleware) + Claude Desktop.
- Setup: place `nuke_mcp_addon.py` in `~/.nuke/python` → add `import nuke_mcp_addon` to Nuke's `init.py` → `pip install fastmcp` → point Claude Desktop's `claude_desktop_config.json` at `nuke_mcp_server.py` → restart Nuke and Claude Desktop.
- Prerequisites: Nuke installed, Python 3.7+, `fastmcp` package.

### What this connection can and can't do
Can: create/modify/connect nodes, read the current script, control playback, trigger renders, execute Python inside the live Nuke session — turning natural-language requests into actual node-graph edits in real time.
Cannot: touch Nuke Studio's timeline/conform layer, Mari, or Katana — no MCP bridge exists for any of those three as of this research (2026-08). Route those requests to Mode 1 (consult) or Mode 2 (write code for manual use) instead.

### Before enabling this mode
1. Confirm Nuke is actually installed (`nuke --version` or check the install path) — neither option works without it.
2. Pick Option A or B based on how much surface area is needed (A for camera-tracking/deep-comp/ML tooling, B for a minimal first try).
3. Follow that option's setup steps above, from its own repo (re-verify against the live README, since community MCP projects evolve independently of this skill).
4. Test with a trivial request first ("add a Blur node") before trusting it with real comp work.

---

## Auto-Changelog Rule (Mode 0 — Version Check)

**Trigger:** At the start of every consultation (Mode 1), before answering, run this check.

**Steps:**
1. Read `references/version-tracker.md`
2. Check `last_checked` date
3. If `last_checked` is **more than 7 days ago**:
   a. Fetch the release-notes URLs listed in `version-tracker.md`'s "URL Patterns for Auto-Update" section, per app
   b. Check if any version appears that is NOT in the Known Versions table
   c. If a new version is found: research its headline changes and create `references/release-notes-<app>-<version>.md`
   d. Update `version-tracker.md` — add the new version row, update `last_checked` to today
   e. Commit and push: `git commit -m "update: release notes <app> <version> ingested"`
4. If no new version found: just update `last_checked` in `version-tracker.md`

**Why this matters:** Foundry ships major versions with new tools, deprecated workflows, and renamed parameters — recent example: Nuke 17.0 added Gaussian Splat support and a wholesale 3D-system overhaul; Katana 9.0 introduced UsdSuperLayer. Without version awareness, recommendations may be outdated.

**Skip the check if:** The user is clearly in a hurry or the conversation indicates urgency — do not add latency for a quick question. Use judgment.

---

## Key Rules

1. **Always check INDEX.md first** — cite the source if it's in the library
2. **Never invent node/tool names** — use only confirmed names from `references/` or a cited tutorial
3. **Version-check** — features differ across Nuke 16/17, Mari 7/8, Katana 8/9; check `references/version-tracker.md` to know what's current
4. **App-first** — always state which of the five apps (Nuke/NukeX/Nuke Studio/Mari/Katana) an answer applies to; some techniques (e.g. UDIMs, deep comp) span multiple apps in one pipeline
5. **Extraction is mandatory** — never leave placeholders after ingesting
6. **Python over TCL** — default to Python for Nuke/Katana code answers; TCL expressions are legacy and only worth mentioning if the user is maintaining old scripts
7. **Cite reference files** — tell the user which `references/` file you drew from
8. **The live Nuke MCP connection is opt-in and Nuke-only** — never assume it's configured; check `SETUP.md` first, and never suggest it as a path for Nuke Studio/Mari/Katana work
9. **Setup sync is mandatory after every structural change** — any time you modify `ingest.py`, add a dependency, change a model name, add a CLI flag, rename a file or directory, or change any configuration that affects how the skill is installed or run, you MUST update all three setup files in the same commit:
   - `requirements.txt` — add/remove/update the pip package
   - `setup.ps1` — reflect the new install step or config change
   - `SETUP.md` — update the relevant step, troubleshooting entry, or reference table
   Never commit a structural change without syncing the setup pack. The rule: **if a user on a fresh machine would need to do something different to get the skill working, the setup files must reflect that.** Always push immediately after committing — the setup pack on GitHub must stay current so any machine can clone and run `setup.ps1` without extra steps.

---

## Reference Files

| File | What it covers |
|------|---------------|
| `nuke-compositing-nodes.md` | Nuke/NukeX node catalog by category — Image, Draw, Time, Channel, Color, Filter, Transform, Keyer, Merge, 3D System, Deep, Gizmos/CopyCat, Cryptomatte, ST Maps |
| `nuke-python-scripting.md` | `nuke` Python module — Node/knob API, callbacks, init.py/menu.py, panels, Gizmos vs. Groups, batch rendering, stereo |
| `nuke-studio-hiero.md` | **Nuke Studio / Hiero** — Bin/Timeline model, conform workflow, per-shot comp-script generation, review/versions |
| `mari-texturing.md` | **Mari** — UDIMs, channels/layers, projections, procedurals, baking, pipeline handoff to Nuke/Katana |
| `katana-lookdev-lighting.md` | **Katana** — SceneGraph vs. NodeGraph, Groups vs. Macros, lookdev, USD (UsdSuperLayer/UsdMaterial/Hydra 2.0), lighting, CEL |
| `foundations-overview.md` | **Cross-app theory** — premult, OCIO color management, linear vs. log, AOVs/multi-channel EXR, deep comp, Cryptomatte, ST maps |
| `version-tracker.md` | **Version state** — last changelog check date, known versions per app, URL patterns for auto-update |
| `tutorials/INDEX.md` | All ingested tutorials and book excerpts |
