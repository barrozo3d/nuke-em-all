---
title: Start-up Scripts — Nuke Python API Reference
source: Article
url: https://learn.foundry.com/nuke/developers/latest/pythondevguide/startup.html
author: learn.foundry.com
ingested: 2026-09-04
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/start-up-scripts-nuke-python-api-reference/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Start-up Scripts — Nuke Python API Reference

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
