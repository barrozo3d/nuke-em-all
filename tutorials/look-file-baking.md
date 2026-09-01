---
title: Look File Baking
source: Article
url: https://learn.foundry.com/katana/Content/ug/look_files/look_file_baking.html
author: learn.foundry.com
ingested: 2026-09-01
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/look-file-baking/
frame_count: 0
frame_status: skipped
---

# Look File Baking

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/look_files/look_file_baking.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Look File Baking Look Files are written out by using the LookFileBake node. Using this node you have to set one input to a point in the node graph where the scene data is in its original state and another to indicate the point in the node graph where the scene data is in its modified state. If you want to include multiple output passes in the Look File you can add additional inputs to connect to points in the node graph where the scene data has been set up for that extra pass. During LookFileBake every location in the scene graph under the root location is compared with the equivalent scene graph location in the original state. What is written out into the Look File are all the changes, such as changes to attributes (new attributes, modified values of existing attributes, and any attributes that have been deleted). The details of any new locations that have been added are also written out. This means that new locations that are part of the 'look' can be included, such as face-sets for a polygon mesh that weren't part of the original model, or to add lights such as architectural lights on a building. One important thing to note here is that while the nodes in the Node Graph represent live recipe, the Look File is a baked cache of the results of those nodes: it's a list of all the changes that the nodes make to the scene graph data rather than the recipe itself. One of the main reasons for using Look Files rather than keeping everything as live recipe is efficiency. If you have thousands of assets, like you could in a typical shot from a CG Feature or VFX film, it can be inefficient to keep everything as live recipe. The Look Files allow the changes needed to be calculated once and then recorded as a baked list by comparing the state of the scene graph data before and after the filters. If you want to make additional changes in lighting on top of those defined by a Look File you still can do so by using additional overrides. If a new version of the asset is created, any associated Look Files need to be baked out again by re-running the LookFileBake in the appropriate Katana project. Conversely, if you want to hand off live recipe from one Katana project to another one you should use macros or LiveGroups instead. Can't find what you're looking for? Use our feedback widget on the right to request more information.



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
