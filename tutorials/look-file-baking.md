---
title: Look File Baking
source: Article
url: https://learn.foundry.com/katana/Content/ug/look_files/look_file_baking.html
author: learn.foundry.com
ingested: 2026-09-01
app: Katana
version: 9.0v3
tags: [katana, lookdev, nodegraph, katana-9, intermediate]
extraction_status: complete
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
Baking a Katana look into a **Look File** with the **LookFileBake** node by diffing the scene graph in its *original* state against its *modified* state, so the result travels as a recorded list of changes rather than as live recipe.

### Summary
`LookFileBake` takes one input at the point in the node graph where scene data is still in its original state and another where it has been modified; the bake then walks every scene graph location under the root and writes out the differences. Extra inputs can be added, one per output pass, to include multiple passes in the same Look File. The page's central distinction is that the Node Graph is **live recipe** while a Look File is a **baked cache of that recipe's results** — a list of the changes the nodes make to the scene graph, not the nodes themselves — which is what makes it efficient on shots carrying thousands of assets, and also what forces a re-bake whenever a new version of the asset appears.

### Key Steps
1. Add a **LookFileBake** node.
2. Connect one input to the point in the node graph where the scene data is in its **original** state.
3. Connect another input to the point where the scene data is in its **modified** state.
4. To carry more than one output pass in the Look File, **add additional inputs** and connect each to the point where the scene data is set up for that extra pass.
5. Bake. Every location in the scene graph **under the root location** is compared against the equivalent location in the original state, and the differences are written out.
6. To change lighting further on top of what a Look File defines, apply **additional overrides** rather than editing the baked file.
7. When a **new version of the asset** is created, re-run `LookFileBake` in the appropriate Katana project — associated Look Files must be baked out again.
8. If the goal is to hand off **live recipe** from one Katana project to another, do not bake — use **macros** or **LiveGroups** instead.

### Nodes / Tools / Settings
**Node:** `LookFileBake` — writes out Look Files.

**Inputs:**

| Input | Connect to |
|---|---|
| original state | the point in the node graph where the scene data is unmodified |
| modified state | the point where the scene data carries the look |
| *additional inputs* | one per extra **output pass** to include in the Look File |

**What the bake writes out** — the delta between the two states, for every scene graph location under the root:
* **attribute changes** — new attributes, modified values of existing attributes, and attributes that have been **deleted**
* **new locations** added as part of the look — e.g. **face-sets** for a polygon mesh that were not part of the original model, or added lights such as architectural lights on a building

**Look File vs. live recipe** — the distinction the page turns on:

| | Node Graph | Look File |
|---|---|---|
| What it is | live recipe | baked cache of the recipe's *results* |
| Contents | the nodes themselves | a list of the changes those nodes make to scene graph data |
| Why use it | edit and re-evaluate freely | efficiency — thousands of assets need the changes calculated **once**, then recorded |

**Re-baking:** a new version of the asset invalidates its Look Files; re-run `LookFileBake` in the appropriate Katana project.

**Not the tool for recipe hand-off:** to move live recipe between Katana projects, use **macros** or **LiveGroups**.

**Extending a baked look:** further lighting changes on top of a Look File are made with **additional overrides**.

### Difficulty
Intermediate

### Foundry App & Version
Katana 9.0v3 — the version is stated on the page itself, not inferred from the docs set.

### Tags
katana, lookdev, nodegraph, katana-9, intermediate

---

## Scope note — what this page does and does not cover

The page explains **what a Look File bake produces and why**, at concept level. It
does **not** cover the `LookFileBake` node's parameters, the on-disk Look File
format, or the nodes that read a Look File back in (`LookFileAssign`,
`LookFileManager`, `LookFileMaterialsIn/Out`) — none of those names appear in the
text. Its parent page, `ug/look_files/look_files.html`, is a **1,364-char stub**
and does not fill the gap. What is missing is recorded in
`KNOWLEDGE_GAPS_TODO.md` rather than written from model knowledge.

The page also names **macros**, **LiveGroups** and **additional overrides** as
alternatives or complements without explaining them; LiveGroups is covered by
[LiveGroups and LiveShadingGroups](livegroups-and-liveshadinggroups.md).

---

## Related Tutorials
- [LiveGroups and LiveShadingGroups](livegroups-and-liveshadinggroups.md) — shares `katana` + `nodegraph` + `katana-9`; this page names **LiveGroups and macros** as what to use *instead* of baking when the thing being handed between projects is live recipe rather than its results. The two pages are the two halves of one decision.
- [Creating Shading Networks](creating-shading-networks.md) — shares `katana` + `lookdev` + `nodegraph`; the shading network built there is the *modified state* a LookFileBake diffs against the original, so it is what actually ends up inside a Look File.
- [NetworkMaterialCreate](networkmaterialcreate.md) — shares `katana` + `lookdev` + `nodegraph`; the material assignments a NetworkMaterialCreate makes are exactly the attribute changes a Look File records as a delta.
- [GafferThree](gafferthree.md) — shares `katana` + `lookdev` + `katana-9`; the lights a GafferThree rig adds are the "new locations" a bake writes out, and its **Export Rig** is the other route Katana offers for reusing lighting work.
