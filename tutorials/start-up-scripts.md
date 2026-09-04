---
title: Start-up Scripts
source: Article
url: https://learn.foundry.com/nuke/developers/latest/pythondevguide/startup.html
author: learn.foundry.com
ingested: 2026-09-04
app: "Nuke / NukeX / Nuke Studio (start-up mechanism is common to all)"
version: "not specified (dev guide served at /latest/; the page's own plug-in-path examples are Nuke 6.2v4-era)"
tags: [python-scripting, pipeline, gizmo, nuke-startup, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/start-up-scripts/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Start-up Scripts

**Source:** [Article](https://learn.foundry.com/nuke/developers/latest/pythondevguide/startup.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Start-up Scripts  This section describes the scripts that NUKE runs on start-up. Evaluation Order  NUKE initialization scripts are run in reverse order of the NUKE plug-in path. At start-up, the default NUKE plug-in path is as follows: [‘/home/nukeuser/.nuke’, ‘/usr/local/NUKE/6.2/plugins’, ‘/usr/local/Nuke6.2v4/plugins/user’, ‘/usr/local/Nuke6.2v4/plugins/icons’, ‘/usr/local/Nuke6.2v4/plugins’] This example shows the NUKE plug-in path for NUKE 6.2v4 and a user called ‘nukeuser’. In this case, scripts in ‘/usr/local/Nuke6.2v4/plugins’ are run first, with scripts in ‘/home/nukeuser/.nuke’ run last. You can query the plug-in directory using nuke.pluginPath(). If necessary, you can prefix additional directories to the path by calling nuke.pluginAddPath(), or append them using nuke.pluginAppendPath(). You can also edit the path by modifying the NUKE_PATH environment variable. In each plug-in directory, NUKE first executes the init.py file (if one exists), followed by the menu.py file (again, if one exists). menu.py  Any file called menu.py that is placed in one of NUKE’s plug-in path directories is automatically read when NUKE starts in an interactive session. It is not read, however, when NUKE is launched for a command-line session or render. Because of this, you should use menu.py exclusively for commands that are only relevant to interactive sessions. A typical example would be adding favorites to the File Browser or creating custom menus and hotkeys. For more details, see Customizing the UI . init.py  Any file called init.py that is placed in one of NUKE’s plug-in path directories is automatically read whenever NUKE is launched. In other words, this file is read for both command-line and interactive sessions. Note that you should not use init.py for any commands that create UI elements, as this may lead to errors or prevent NUKE from launching. Here are some examples of what the init.py file is typically used for (though depending on your workflow, most of these can live in the menu.py file instead if they’re not needed in command-line sessions): adding custom plug-in paths - see Installing Plug-ins setting knob defaults - see Defining Knob Defaults setting custom formats - see Formats .



---

## Structured Notes

### Core Technique
Nuke's start-up sequence: every directory on the plug-in path is scanned, and in each one Nuke runs `init.py` first and then `menu.py` — `init.py` in **every** session including command-line renders, `menu.py` **only** in an interactive GUI session.

### Summary
This page defines where studio customisation actually lives in Nuke: the plug-in path, the `init.py` / `menu.py` split, and the `NUKE_PATH` environment variable. Initialization scripts run in **reverse order of the plug-in path**, so the deepest system directory executes first and `~/.nuke` executes last — which is what lets a user override a facility setting. The plug-in path can be read with `nuke.pluginPath()`, prefixed with `nuke.pluginAddPath()`, appended to with `nuke.pluginAppendPath()`, or set from outside Nuke with `NUKE_PATH`. The load-bearing rule is that `menu.py` is skipped entirely for command-line sessions and renders, so anything that builds UI belongs there and nothing that builds UI belongs in `init.py`, where it can error or stop Nuke launching.

### Key Steps
1. Query the current plug-in path with **`nuke.pluginPath()`** — it returns a list, ordered with `~/.nuke` first and the application's own `plugins` directory last.
2. Understand the **evaluation order**: initialization scripts run in *reverse* order of that list, so `/usr/local/Nuke<ver>/plugins` runs first and `~/.nuke` runs last. Last writer wins, which is why per-user settings override facility ones.
3. In each plug-in directory Nuke executes **`init.py` first, then `menu.py`** — both optional, both picked up automatically by filename.
4. Put anything needed in **both** interactive and command-line sessions in **`init.py`**: custom plug-in paths (see *Installing Plug-ins*), knob defaults (see *Defining Knob Defaults*), custom formats (see *Formats*).
5. Put **interactive-only** code in **`menu.py`**: custom menus, hotkeys, File Browser favourites (see *Customizing the UI*). It is not read for a command-line session or render.
6. **Never create UI elements from `init.py`** — the page warns this "may lead to errors or prevent NUKE from launching". This is the single most consequential rule on the page.
7. Extend the path from inside Nuke with **`nuke.pluginAddPath()`** (prefixes, so it wins) or **`nuke.pluginAppendPath()`** (appends, so it loses).
8. Extend it from outside Nuke by setting the **`NUKE_PATH`** environment variable — the route to use when the same paths must apply to every artist on a facility.

### Nodes / Tools / Settings
- **`init.py`** — read on *every* launch, interactive and command-line. Plug-in paths, knob defaults, custom formats. No UI code.
- **`menu.py`** — read only in an *interactive* session. Menus, hotkeys, File Browser favourites.
- **`nuke.pluginPath()`** — returns the ordered plug-in path list.
- **`nuke.pluginAddPath(path)`** — prefixes a directory to the path.
- **`nuke.pluginAppendPath(path)`** — appends a directory to the end of the path.
- **`NUKE_PATH`** — environment variable holding additional plug-in directories.
- Default path shape (from the page's own Nuke 6.2v4 example, in the order *listed*): `~/.nuke`, `/usr/local/NUKE/<ver>/plugins`, `<install>/plugins/user`, `<install>/plugins/icons`, `<install>/plugins`.

### Difficulty
Intermediate

### Foundry App & Version
Nuke / NukeX / Nuke Studio — the start-up script mechanism is shared across all three. Version not specified: the guide is served from the `/latest/` documentation path, but the concrete plug-in-path examples on the page are Nuke 6.2v4-era and use a `NUKE/6.2` directory layout. The mechanism itself (`init.py`, `menu.py`, `NUKE_PATH`, `nuke.pluginPath`) is unchanged in current releases.

### Tags
`python-scripting`, `pipeline`, `gizmo`, `nuke-startup`, `intermediate`

---

## Related Tutorials
- [Installing Plug-ins](installing-plug-ins.md) — where to *put* the gizmos and scripts this page's path mechanism then finds.
- [Customizing the UI](customizing-the-ui.md) — the interactive-only code that belongs in `menu.py`.
- [Break up your "PERFECT CG" Renders with this FREE Plugin](break-up-your-perfect-cg-renders-with-this-free-plugin.md) — a third-party plug-in whose installation depends on this path mechanism.

> **Note on code in the Raw Data.** The article fetcher strips quote characters out of inline code, so the captured page text reads `nuke.menu( Nodes ).addCommand( ... )`. Quotes are restored in the notes above; the identifiers, argument order and values are unchanged from the source page.
