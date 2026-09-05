---
title: Editing Materials With The NetworkMaterialEdit Node
source: Article
url: https://learn.foundry.com/katana/Content/ug/adding_assigning_materials/using_networkmaterialedit.html
author: learn.foundry.com
ingested: 2026-09-04
app: "Katana"
version: "9.0 (learn.foundry.com/katana current docs at ingest; release notes whats_new_9.0)"
tags: [katana, lookdev, nodegraph, katana-9, advanced]
extraction_status: complete
frames_dir: tutorials/frames/editing-materials-with-the-networkmaterialedit-node/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Editing Materials With The NetworkMaterialEdit Node

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/adding_assigning_materials/using_networkmaterialedit.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Editing Materials With The NetworkMaterialEdit Node The NetworkMaterialEdit nodes allow artists to edit network materials, by adding or removing shading nodes from an existing network, as well as by creating new connections or breaking existing connections. You can also modify any of the parameters of shading nodes in an existing network. The NetworkMaterialEdit node uses a Scene Graph location , set in the Node Parameters , which stores information about how a Network Material was created using the material.layout attribute. The Scene Graph location could be brought in through a look file and could have been created in a different department, with the original material network in a separate project. This workflow allows artists to have full control of the Network Material without needing to go back and edit the original material network. Any upstream changes to the original material network change the material.layout attribute causing the NetworkMaterialEdit node to update to reflect those changes. Inside a NetworkMaterialCreate node Inside a NetworkMaterialEdit node The contents of NetworkMaterialEdit nodes are drawn in the same style that was introduced for NetworkMaterialCreate nodes, with exposed ports on shading nodes and a left-to-right node layout. If the network material you are editing was created using a NetworkMaterialCreate node, the material network layout inside the NetworkMaterialEdit node is an exact duplicate of the original layout. If the network material you are editing was created using the legacy NetworkMaterial workflow, the shading nodes in the NetworkMaterialEdit node are automatically arranged in the node graph. Using a NetworkMaterialEdit node to edit a legacy NetworkMaterial Note: For more information on the NetworkMaterialCreate node, refer to Building Materials Using NetworkMaterialCreate . At first, the shading node network within a NetworkMaterialEdit node appears slightly dimmed to indicate that no changes have been made since the network was created, this can be changed using the NME Filter buttons . Once a change is made to a node inside a NetworkMaterialEdit node, the node is marked with a yellow stripe to indicate that its parameters have been edited. Similarly, any new nodes are marked with a green stripe. This makes it easy to track any changes that you make within the NetworkMaterialEdit node, in comparison to the original NetworkMaterialCreate node. Nodes which are left disconnected from the output inside the original NetworkMaterialCreate node are disabled within a NetworkMaterialEdit node and marked with a padlock symbol to indicate they cannot be edited from with the NetworkMaterialEdit node. If you disconnect a node completely from within a NetworkMaterialEdit node, that node is marked with a red stripe. Yellow stripe indicates an edit. Green stripe indicates a new node. Padlock symbol indicates a disabled node. Red stripe indicates a disconnected node. This workflow allows artists to make adjustments to their shading node network without overriding the original. This can be useful when working on one asset across multiple shots as you are not constrained by how the original network material was set up, so small changes can be made on a per-shot basis. NetworkMaterialEdit nodes combine the functionality of the existing NetworkMaterialParameterEdit and NetworkMaterialSplice node types, but in a UI that is visually representative of how the material was originally authored. Filtering within NetworkMaterialEdit The NetworkMaterialEdit node UI features the NME Filter options. These buttons allow you to dim nodes within the Node Graph for node states which are not toggled on. This is especially useful when working with large shading node networks as it allows you to focus your attention on a clear section of the node graph. - Edited nodes - New nodes - Unchanged nodes - Disconnected nodes For example, to highlight which nodes are new to the NetworkMaterialEdit node, turn on the New button and turn off the Edited , Unchanged , and Disconnected buttons. If you would like all nodes to be fully visible and none to appear dimmed, turn on the Edited , New , Unchanged , and Disconnected buttons. How to Use the NetworkMaterialEdit Node Create a NetworkMaterialEdit node by pressing Tab and typing NetworkMaterialEdit . Connect the NetworkMaterialEdit node to your network. Note: The NetworkMaterialEdit node must be downstream of the original NetworkMaterialCreate node information, whether that information has come from a look file or the NetworkMaterialCreate node itself. Open the Parameters of the NetworkMaterialEdit node by hovering your mouse over the node and pressing E , or by clicking the Edit flag on the node. Use Ctrl + Middle Mouse button to drag the NetworkMaterial from the Scene Graph to the sceneGraphLocation field in the NetworkMaterialEdit Node Parameters . Click the Enter button on the NetworkMaterialEdit node to view the shading node network and start editing. Note: Shading nodes within a NetworkMaterialCreate node that are not contributing to the final material are missing important attributes, making it hard to reconnect them from a NetworkMaterialEdit node. These nodes are locked from within the NetworkMaterialEdit node. Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
**NetworkMaterialEdit** edits a network material **non-destructively from downstream** — adding, removing, connecting or disconnecting shading nodes and changing parameters — by reading the `material.layout` attribute at a scene graph location rather than opening the original network.

### Summary
This is the per-shot override workflow for look development, and the reason it exists is departmental: the scene graph location it edits may have arrived **through a look file, created in a different department, with the original material network in a separate project**. The node reads `material.layout` from that location, so it can reconstruct and present the network without the authoring project — and because it reads that attribute live, **upstream changes to the original network propagate**, updating the NetworkMaterialEdit to reflect them. Its editing state is legible at a glance through node striping: the network starts **dimmed** (nothing changed yet), an edited node gains a **yellow stripe**, a new node a **green stripe**, a node you disconnect a **red stripe**, and nodes that were already disconnected from the output in the original are **disabled and padlocked** — they cannot be edited from here. The **NME Filter** buttons (Edited / New / Unchanged / Disconnected) dim whichever states are toggled off, which is how large networks stay workable. It consolidates what used to be the **NetworkMaterialParameterEdit** and **NetworkMaterialSplice** node types into a UI that matches how the material was actually authored.

### Key Steps
1. Point the node at the **Scene Graph location** of the network material in its Node Parameters — the location carrying `material.layout`.
2. Expect a faithful layout when the material came from a **NetworkMaterialCreate** (an exact duplicate of the original), and an **automatically arranged** graph when it came from the legacy NetworkMaterial workflow.
3. Edit freely: add or remove shading nodes, make or break connections, change any parameter — none of it overrides the original network.
4. **Read the stripes:** yellow = parameters edited, green = newly added, red = disconnected here, padlock = disabled because it was already disconnected from the output upstream.
5. Use the **NME Filter** buttons — **Edited**, **New**, **Unchanged**, **Disconnected** — to dim the states you are not working on; turn all four on to see everything undimmed.
6. Rely on live propagation: upstream changes alter `material.layout` and the NetworkMaterialEdit updates to match.
7. Reach for this rather than duplicating a network when the **same asset needs small per-shot changes across multiple shots**.

### Nodes / Tools / Settings
- **NetworkMaterialEdit** — Scene Graph location parameter; reads the **`material.layout`** attribute.
- Node state striping: **yellow** (edited), **green** (new), **red** (disconnected), **padlock** (disabled, was already disconnected upstream); whole network **dimmed** until first change.
- **NME Filter** buttons: Edited / New / Unchanged / Disconnected.
- Supersedes **NetworkMaterialParameterEdit** and **NetworkMaterialSplice**.
- Same node drawing style as NetworkMaterialCreate: exposed ports, left-to-right layout.

### Difficulty
Advanced

### Foundry App & Version
Katana 9.0.

### Tags
`katana`, `lookdev`, `nodegraph`, `katana-9`, `advanced`

---

## Related Tutorials
- [Building Materials Using NetworkMaterialCreate](building-materials-using-networkmaterialcreate.md) — the authoring side whose layout this reproduces.
- [Node Parameters and Interface Controls](node-parameters-and-interface-controls.md) — promotion works identically here.
- [LiveGroups and LiveShadingGroups](livegroups-and-liveshadinggroups.md) — the other cross-department sharing mechanism.

---

> **Provenance.** `learn.foundry.com/katana` (MadCap Flare). Paths in this doc set
> are not guessable and `Data/Tocs/*` 404s, so this page was reached by crawling
> from `Content/learn_katana.html` → `user_guide.html`, or from a sibling page's
> own links. Reference-guide and user-guide pages carry clean `<title>`s and need
> no `--title` override, unlike `learn.foundry.com/nuke/developers/**`.
