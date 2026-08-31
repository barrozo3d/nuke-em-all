---
title: LiveGroups and LiveShadingGroups
source: Article
url: https://learn.foundry.com/katana/Content/ug/livegroups/livegroups.html
author: learn.foundry.com
ingested: 2026-08-31
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/livegroups-and-liveshadinggroups/
frame_count: 0
frame_status: skipped
---

# LiveGroups and LiveShadingGroups

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/livegroups/livegroups.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** LiveGroups and LiveShadingGroups A LiveGroup node provides a way for you to import another Katana project into the current project, and reload it every time the current project is updated, either automatically (for example, on scene load or before batch rendering) or manually (through context menu options). A LiveGroup node’s source is expected to contain a Group or Group-like node in its root level. When loading a LiveGroup source scene, the first loaded Group node in the source scene defines the user parameters and child node contents of the target LiveGroup. LiveGroups provide a number of useful constructs for collaborative work between users, for sharing nodes between show, sequence, and shot levels, and for users working in parallel on the same shot. There are two primary cases for using LiveGroups: collaborative work between departments and collaborative work within a department. As an example of collaborative work between departments, an FX artist would pass a Katana project to a lighting artist that can then use that project as part of a lighting scene by loading it into a LiveGroup node. In this example, the FX artist is only interested in publishing their setup, while the lighting artist is only interested in importing the published project, as shown in the diagram below: As an example of collaborative work within a department, a shot or sequence lighting artist would make changes to a LiveGroup source on a shot, and could then publish the source scene back to the shot or sequence for other lighting artists to pick up, as shown in the diagram below: In addition to the existing .katana file extension, the .livegroup file extension has been introduced. For backwards compatibility, it is still possible to use a Katana project with the .katana file extension as a LiveGroup source. When publishing new LiveGroup sources using the Publish... or Publish and Finish Editing Contents... menu options, the .livegroup file extension is used. Any Katana project file can be used as a source of a LiveGroup node, and LiveGroup sources can be published as assets through Katana ’s Asset API. When a LiveGroup node’s contents are exported to a file, the .livegroup file extension is used to create it. When a LiveGroup is imported, you can choose whether to import either .katana or .livegroup files. Files with the extension .macro are not listed by default but if there are macros present in the file structure, you can select the macros option in the Types field in the Import Livegroup dialog. For more information on Asset Management and the asset publishing process, see Asset Management , or Asset Management System Plug-in API . By default, exported .katana files are binary, gzip-compressed archives in a .tar format, containing an XML scene description file as data. This format is archived and compressed because nodes may contain binary data. In contrast, the .livegroup extension uses uncompressed, unarchived, ASCII files in a format similar to .katana but with a dedicated extension for LiveGroup sources. This means that LiveGroups, by default, are written as plain text, uncompressed XML files. While .katana files contain project settings in addition to the nodes of the node graph document, as they represent Katana projects, .livegroup files only contain the XML representation of the parameters and children of the Group node that controls the LiveGroup interface and contents. Can't find what you're looking for? Use our feedback widget on the right to request more information.



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
