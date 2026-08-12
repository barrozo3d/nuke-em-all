# Nuke'Em All

A Claude Code skill: an expert consultant for Foundry's compositing/look-dev suite — Nuke, NukeX, Nuke Studio (+ Hiero), Mari, and Katana — that also builds its own knowledge base by ingesting tutorials, and can optionally drive a real, running Nuke session over MCP.

## What it does

Ask it a question about any of Foundry's five apps and it answers from a growing library of ingested tutorials plus a hand-written reference knowledge base covering compositing nodes, keying, deep compositing, Cryptomatte/ST maps, color management (OCIO/ACES), Nuke Python scripting, Nuke Studio/Hiero editorial workflows, Mari texture painting/UDIMs, and Katana lookdev/lighting/USD. It can also write Nuke or Katana Python for you directly. The knowledge base currently holds 2 fully-extracted tutorials plus one cross-reference stub pointing to a shared Houdini/Nuke fire-FX breakdown extracted in full over in `houdini-wand`.

## Quick start

```powershell
git clone https://github.com/barrozo3d/nuke-em-all.git "$HOME\.claude\skills\nuke-em-all"
cd "$HOME\.claude\skills\nuke-em-all"
.\setup.ps1
```

Then just ask Claude Code a question — it reads `SKILL.md` automatically. Full setup and troubleshooting details live in `SETUP.md`.

## How it works

**Consulting.** Every question is answered against `tutorials/INDEX.md` plus 7 `references/*.md` files (nuke-compositing-nodes, nuke-python-scripting, nuke-studio-hiero, mari-texturing, katana-lookdev-lighting, foundations-overview, version-tracker).

**Growing the library.** Say "ingest this: [URL]" and a three-step pipeline runs:
1. `ingest.py` — pulls a YouTube transcript (Whisper, with per-sentence timestamps) or article text, no video download, no API calls.
2. `select_frames.py` — Claude reads the timestamped transcript, picks 4-8 moments that actually show a technique, and this script captures just those frames.
3. Claude reads the captured frames and the transcript, writes structured notes (technique, steps, settings, tags), cross-links related tutorials, and commits everything to this repo.

`validate.py` is a post-ingest integrity checker (no `[PENDING]` leftovers, no broken INDEX cross-references, transcripts long enough to be real) — run `python validate.py` after a batch of ingests.

**Live connection (optional, Nuke/NukeX only).** Nuke ships no built-in MCP bridge, but two independent open-source community projects wrap a Nuke-side addon + local MCP server: `CreativeLyons/nuke-mcp2` (recommended default, broader version coverage, more tool categories) and `dughogan/nuke_mcp` (simpler, course-backed, MIT-licensed). Covers Nuke/NukeX only — no bridge exists for Nuke Studio, Mari, or Katana. See `SKILL.md` → "Live Nuke Connection" for full setup.

## Repo structure

```
nuke-em-all/
├── SKILL.md               ← main skill instructions Claude reads
├── README.md               ← this file
├── SETUP.md               ← human + Claude setup guide
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

Public personal project, no warranty. 2 tutorials ingested as of 2026-08-12.
