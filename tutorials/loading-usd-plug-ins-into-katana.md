---
title: Loading USD Plug-ins into Katana
source: Article
url: https://learn.foundry.com/katana/Content/ug/using_hydra_viewer/usd_load_plugins.html
author: learn.foundry.com
ingested: 2026-08-31
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
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
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Nodes / Tools / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Foundry App & Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]
