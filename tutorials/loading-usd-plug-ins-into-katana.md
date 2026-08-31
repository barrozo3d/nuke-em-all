---
title: Loading USD Plug-ins into Katana
source: Article
url: https://learn.foundry.com/katana/Content/ug/using_hydra_viewer/usd_load_plugins.html
author: learn.foundry.com
ingested: 2026-08-31
app: Katana
version: 9.0v3
tags: [katana, usd, katana-9, beginner]
extraction_status: complete
frames_dir: tutorials/frames/loading-usd-plug-ins-into-katana/
frame_count: 0
frame_status: skipped
---

# Loading USD Plug-ins into Katana

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/using_hydra_viewer/usd_load_plugins.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Loading USD Plug-ins into Katana In Katana 4.5v1, and later, USD plug-ins are enabled by default. You don't need to define any environment variables, you can use USD plug-ins straight away. To use the USD nodes inside versions of Katana earlier than 4.5v1, you must first enable the USD plug-ins so that they are loaded when you open Katana . To do this, you must edit your KATANA_RESOURCES , LD_LIBRARY_PATH ( PATH on Windows ), and PYTHONPATH in your Katana launcher script and add the USD plugin folder. Note: For more information about creating a launcher script for Katana , refer to these Support articles: Linux : Creating a Katana Launcher Script for Linux Windows : Creating a Katana Launcher Script for Windows Add the following lines to your launcher script: Note: KATANA_ROOT represents the path to your Katana install folder, for example: C:\Program Files\Katana4.0v1 Windows set PATH=%PATH%; KATANA_ROOT \plugins\Resources\Usd\lib set KATANA_RESOURCES=%KATANA_RESOURCES%; KATANA_ROOT \plugins\Resources\Usd\plugin set PYTHONPATH=%PYTHONPATH%; KATANA_ROOT \plugins\Resources\Usd\lib\python Linux export LD_LIBRARY_PATH=$LD_LIBRARY_PATH: KATANA_ROOT /plugins/Resources/Usd/lib export KATANA_RESOURCES=$KATANA_RESOURCES: KATANA_ROOT /plugins/Resources/Usd/plugin export PYTHONPATH=$PYTHONPATH: KATANA_ROOT /plugins/Resources/Usd/lib/python Launch Katana using the launcher script and the additional USD node types are available from the node creation menu. Additional USD nodes Additional USD shading nodes A usd menu is also loaded on the Terminal sidebar inside NetworkMaterialCreate nodes. Note: For more information on USD plug-ins for Katana , refer to the Katana USD Plug-ins section in the Developer Guide. Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
Enabling Katana's **USD plug-ins** — automatic from **Katana 4.5v1** onward, and a three-environment-variable launcher-script edit on anything older.

### Summary
From **Katana 4.5v1 and later the USD plug-ins are enabled by default**: no environment variables, the USD nodes are simply there. Before 4.5v1 they had to be switched on by editing `KATANA_RESOURCES`, the library path (`PATH` on Windows, `LD_LIBRARY_PATH` on Linux) and `PYTHONPATH` in a Katana launcher script to point at the shipped USD plug-in folders. Once loaded, the extra USD node types appear in the node creation menu, extra USD shading nodes become available, and a **`usd` menu is added to the terminal sidebar inside NetworkMaterialCreate nodes**.

### Key Steps
1. **Check the version first.** On **Katana 4.5v1 or later**, stop — USD plug-ins are already enabled and no environment variables are needed.
2. On earlier versions, open (or create) your **Katana launcher script**.
3. Add three variables pointing into `KATANA_ROOT/plugins/Resources/Usd/` — the library path, `KATANA_RESOURCES`, and `PYTHONPATH` (exact lines below).
4. **Launch Katana via the launcher script**, not the normal shortcut — the variables only exist in that environment.
5. Confirm it worked: the additional **USD node types** appear in the node creation menu, additional **USD shading nodes** are available, and a **`usd` menu** appears on the terminal sidebar inside **NetworkMaterialCreate** nodes.

### Nodes / Tools / Settings
⚠️ **Version gate:** *"In Katana 4.5v1, and later, USD plug-ins are enabled by default. You don't need to define any environment variables."* Everything below applies only to **earlier** versions.

**`KATANA_ROOT`** stands for the Katana install folder — the page's example is `C:\Program Files\Katana4.0v1`.

**Windows** (added to the launcher script):
```
set PATH=%PATH%;KATANA_ROOT\plugins\Resources\Usd\lib
set KATANA_RESOURCES=%KATANA_RESOURCES%;KATANA_ROOT\plugins\Resources\Usd\plugin
set PYTHONPATH=%PYTHONPATH%;KATANA_ROOT\plugins\Resources\Usd\lib\python
```

**Linux:**
```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:KATANA_ROOT/plugins/Resources/Usd/lib
export KATANA_RESOURCES=$KATANA_RESOURCES:KATANA_ROOT/plugins/Resources/Usd/plugin
export PYTHONPATH=$PYTHONPATH:KATANA_ROOT/plugins/Resources/Usd/lib/python
```

**Three paths, three purposes:** `lib` on the library path (the native libraries), `plugin` on `KATANA_RESOURCES` (the Katana-side plug-in registration), and `lib/python` on `PYTHONPATH` (the Python bindings). All three are required — each variable is appended to rather than replaced.

**What appears once loaded:** additional **USD node types** in the node creation menu; additional **USD shading nodes**; and a **`usd` menu on the terminal sidebar inside NetworkMaterialCreate nodes**.

**Referenced but not ingested:** Foundry Support articles *Creating a Katana Launcher Script* for **Linux** and for **Windows**, and the **Katana USD Plug-ins** section of the Developer Guide.

### Difficulty
Beginner

### Foundry App & Version
Katana 9.0v3 (page served from the current Katana 9.0v3 documentation set), but the page's substance is **historical**: it documents the pre-**4.5v1** setup. On the 9.0v3 the rest of this library covers, the answer is "already enabled".

### Tags
katana, usd, katana-9, beginner

---

## Scope note — why a mostly-historical page is still worth having

`KNOWLEDGE_GAPS_TODO.md` recorded USD plug-in loading as a prerequisite referenced
by the USD material page but never ingested. It turns out to be a **non-problem on
any current Katana**: enabled by default since 4.5v1. That is worth recording
precisely *because* the gap list implied a setup step that no longer exists — a
reader hitting missing USD nodes on a modern Katana should look elsewhere, not at
environment variables.

Its lasting value is the third fact, which is not version-gated: the `usd` menu on
the **NetworkMaterialCreate terminal sidebar** is where USD shading nodes are
reached, connecting this page to the NetworkMaterial set.

---

## Related Tutorials
- [Setting up UsdPreviewSurface Materials](setting-up-usdpreviewsurface-materials.md) — shares `katana` + `usd` + `katana-9`; that page names USD plug-in loading as its prerequisite, which is what this one supplies — and the `usd` menu it adds to the NetworkMaterialCreate terminal sidebar is where its UsdPreviewSurface is reached.
- [Using Native USD Workflows](using-native-usd-workflows.md) — shares `katana` + `usd` + `katana-9`; the whole native USD node set it maps is what becomes available once these plug-ins are loaded — which, on any Katana from 4.5v1, they already are.
- [Creating Shading Networks](creating-shading-networks.md) — shares `katana` + `katana-9`; the terminal sidebar this page adds a `usd` menu to is documented there, including its filter and prepopulated per-renderer terminals.
