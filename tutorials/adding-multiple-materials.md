---
title: Adding Multiple Materials
source: Article
url: https://learn.foundry.com/katana/Content/ug/adding_assigning_materials/multiple_materials_materialstack_node.html
author: learn.foundry.com
ingested: 2026-09-04
app: "Katana"
version: "9.0 (learn.foundry.com/katana current docs at ingest; release notes whats_new_9.0)"
tags: [katana, lookdev, katana-9, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/adding-multiple-materials/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Adding Multiple Materials

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/adding_assigning_materials/multiple_materials_materialstack_node.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Adding Multiple Materials Having a chain of Material nodes would soon clutter up a recipe. To avoid this, create multiple materials within one node using the MaterialStack node. Adding a Material To add a material inside the MaterialStack node: 1. Select Add Add Material . A new material is added to the Add list. 2. Enter a new name in the name parameter. 3. Follow steps 2 to 5 in Adding a Shader to a Material Location . To add a material from a look file inside the MaterialStack node: 1. Select Add Add Look File Material . A new material is added to the Add list. 2. Enter a new name in the name parameter. 3. Follow steps 3 to 6 in Creating a Material from a Look File . To add a material as a child of an existing material: 1. Select a material in the Add list. 2. Select Add Add Child Material . A new material is added below the selected material. 3. Enter a new name in the name parameter. 4. Make any changes needed to the parameters, you can also add additional shaders. Note: The parent has to be within the MaterialStack node, otherwise the menu options are not available. To add Material nodes from the Node Graph into the MaterialStack node, Shift +middle-click and drag the nodes into the Add list. Duplicating a Material To duplicate a material within the MaterialStack node, select the material node in the Add list, right-click, and select Duplicate Material . Disabling a Material To disable a material within the MaterialStack node, select the material node in the Add list, right-click, and select Ignore Material (or press D ). Deleting a Material To delete a material from the MaterialStack node, select the material node in the Add list, right-click, and select Delete Material (or press Delete ). Moving Materials Within the Add List To move materials within the Add list, middle-click and drag. Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
Use one **MaterialStack** node to hold many materials — including look-file materials and child materials — instead of chaining Material nodes and cluttering the recipe.

### Summary
A short, purely operational page, and the answer to a real problem: a chain of Material nodes quickly becomes unreadable. MaterialStack keeps them in a single node's **Add list**, where materials can be created from scratch, created **from a look file**, or nested as **child materials** under an existing entry — with the constraint that the parent must itself be inside the MaterialStack for the child option to appear. Existing Material nodes can be pulled in from the Node Graph by **`Shift`+middle-click-dragging** them into the Add list, and entries can be duplicated, reordered by middle-click-drag, disabled with **Ignore Material** (**`D`**), or deleted.

### Key Steps
1. **Add a material:** **Add › Add Material**, name it in the `name` parameter, then attach shaders exactly as in *Adding a Shader to a Material Location*.
2. **Add a look-file material:** **Add › Add Look File Material**, name it, then follow *Creating a Material from a Look File*.
3. **Nest one:** select an entry in the Add list, then **Add › Add Child Material**. ⚠️ The parent must be **inside** the MaterialStack or the menu option is unavailable.
4. **Import existing nodes:** **`Shift`**+middle-click-drag Material nodes from the Node Graph into the Add list.
5. **Duplicate:** right-click the entry › **Duplicate Material**.
6. **Disable without deleting:** right-click › **Ignore Material**, or press **`D`**.
7. **Delete:** right-click › **Delete Material**, or press **`Delete`**.
8. **Reorder:** middle-click and drag within the Add list.

### Nodes / Tools / Settings
- **MaterialStack** node and its **Add list**.
- Menu: **Add Material**, **Add Look File Material**, **Add Child Material**.
- Right-click: **Duplicate Material**, **Ignore Material** (**`D`**), **Delete Material** (**`Delete`**).
- **`Shift`**+middle-click-drag to import Material nodes; middle-click-drag to reorder.

### Difficulty
Intermediate

### Foundry App & Version
Katana 9.0.

### Tags
`katana`, `lookdev`, `katana-9`, `intermediate`

---

## Related Tutorials
- [Material Basics](material-basics.md) — the shader-attachment steps this page defers to, and the node it replaces a chain of.
- [Building Materials Using NetworkMaterialCreate](building-materials-using-networkmaterialcreate.md) — the modern equivalent for multiple materials.

---

> **Provenance.** `learn.foundry.com/katana` (MadCap Flare). Paths in this doc set
> are not guessable and `Data/Tocs/*` 404s, so this page was reached by crawling
> from `Content/learn_katana.html` → `user_guide.html`, or from a sibling page's
> own links. Reference-guide and user-guide pages carry clean `<title>`s and need
> no `--title` override, unlike `learn.foundry.com/nuke/developers/**`.
