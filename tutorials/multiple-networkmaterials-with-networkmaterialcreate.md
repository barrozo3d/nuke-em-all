---
title: Multiple NetworkMaterials with NetworkMaterialCreate
source: Article
url: https://learn.foundry.com/katana/Content/ug/adding_assigning_materials/networkmaterialcreate_multi_nm.html
author: learn.foundry.com
ingested: 2026-08-31
app: Katana
version: 9.0v3
tags: [katana, lookdev, nodegraph, katana-9, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/multiple-networkmaterials-with-networkmaterialcreate/
frame_count: 0
frame_status: skipped
---

# Multiple NetworkMaterials with NetworkMaterialCreate

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/adding_assigning_materials/networkmaterialcreate_multi_nm.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Multiple NetworkMaterials with NetworkMaterialCreate You can create multiple NetworkMaterials within one NetworkMaterialCreate node. This allows you to share shading nodes across different network materials , reducing the number of nodes needed when creating variants of a material. Video: For a full tutorial series on managing multiple materials within a NetworkMaterialCreate node, take a look at our Creating Multiple Materials using NetworkMaterialCreate course. The Material Scenegraph within the NetworkMaterialCreate Parameters allows you to organize your NetworkMaterials through rearranging and adding Namespaces . Adding a Namespace in your Material Scenegraph creates a group in your Scene Graph tab, which can parent multiple Network Materials and other Namespaces for the purpose of organization. Note: For more information about the Material Scenegraph , refer to the Organizing NetworkMaterials and Namespaces section of this topic. For more information about the NetworkMaterialCreate Parameters , see NetworkMaterialCreate . Adding a New NetworkMaterial To add a new NetworkMaterial to a NetworkMaterialCreate node: Open the NetworkMaterialCreate node Parameters by activating the edit flag. Click the plus button and select Add NetworkMaterial . A new NetworkMaterial is created. New NetworkMaterial in the Material Scenegraph Change the name of the new NetworkMaterial by selecting it and pressing Enter on the keyboard, or by double-clicking. New NetworkMaterial in the terminal sidebar Adding a New Namespace To add a new Namespace to a NetworkMaterialCreate node: Open the NetworkMaterialCreate node Parameters by activating the edit flag. Click the plus button and select Add Namespace . A new Namespace is created. New Namespace in the Material Scenegraph Change the name of the new Namespace by selecting it and pressing Enter on the keyboard, or by double-clicking. New Namespace in the terminal sidebar Note: You can also add NetworkMaterials and Namespaces through the menu options when right-clicking within the NetworkMaterialCreate Material Scenegraph . Organizing NetworkMaterials and Namespaces You can organize your NetworkMaterials and Namespaces through the NetworkMaterialCreate Material Scenegraph in node Parameters . Use the middle-mouse button to click and drag the NetworkMaterials and Namespaces into the structure you require. This structure is reflected in the Scene Graph and the terminal sidebar inside the NetworkMaterialCreate node. Note: Rick-click in the Material Scenegraph to delete and duplicate NetworkMaterials and Namespaces as well as fully expand or collapse them. NetworkMaterials and Namespaces organized in the Material Scenegraph NetworkMaterial and Namespace structure in the Scene Graph NetworkMaterial and Namespace structure reflected in the terminal sidebar The Material Scenegraph also provides some information about each NetworkMaterial . You can see how many renderers and terminals are connected to each NetworkMaterial , set the interactive state of a NetworkMaterial , and assign it a color. Note: For more information about the NetworkMaterialCreate node parameters, see NetworkMaterialCreate . The color helps to distinguish multiple NetworkMaterials at a glance. These colors are represented on the NetworkMaterial names on the terminal sidebar within the NetworkMaterialCreate node. The NetworkMaterials and Namespaces can be collapsed and expanded using the arrows on the terminal sidebar. Workflow Example In this example there are two robot characters each requiring a different material variation. The ability to create multiple NetworkMaterials from one NetworkMaterialCreate node is very useful in this situation as each material variation uses some of the same textures and masks. Each of the robots' materials share a transmission mask, roughness and emissive texture files, and require the same glass shader. Using a separate NetworkMaterialCreate node for each NetworkMaterial would require a lot of duplicated nodes resulting in more nodes overall. This simple example shows how sharing parts of the network reduces duplication. In production scripts featuring hundreds of nodes, the power of multiple NetworkMaterials within a single NetworkMaterialCreate node is far greater. A NetworkMaterialCreate node with one NetworkMaterial location for a white material. Duplicates highlighted. A NetworkMaterialCreate node with one NetworkMaterial location for an orange material. Duplicates highlighted. Using one NetworkMaterialCreate node with two NetworkMaterials means that they can share sections of the shading node network, in this case, the 8 highlighted nodes. This reduces the number of nodes from 27 over two separate NetworkMaterialCreate nodes, to 19 nodes in one NetworkMaterialCreate node by sharing 8 nodes. A NetworkMaterialCreate node with two NetworkMaterial locations. Shared nodes highlighted. Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
Holding **several NetworkMaterials inside one NetworkMaterialCreate node** so that material variants share the parts of the shading network they have in common, instead of duplicating them across one node per material.

### Summary
A NetworkMaterialCreate node is not limited to one NetworkMaterial. Adding more lets variants share shading nodes — the page's worked example takes two robot materials that both need the same transmission mask, roughness and emissive textures and the same glass shader, and shows the node count falling from **27 across two separate NetworkMaterialCreate nodes to 19 in one, by sharing 8 nodes**. The **Material Scenegraph** in the node's Parameters is where they are added, renamed, coloured and arranged, with **Namespaces** acting as organisational groups; that structure is mirrored in the Scene Graph tab and in the terminal sidebar inside the node.

### Key Steps
1. Open the **NetworkMaterialCreate** node's Parameters by **activating the edit flag**.
2. Click the **plus button** and choose **Add NetworkMaterial**. (Right-clicking inside the Material Scenegraph offers the same options.)
3. Rename it by selecting it and pressing **Enter**, or by double-clicking.
4. Add organisational groups the same way: **plus button → Add Namespace**, then rename. A Namespace creates a group in the **Scene Graph** tab that can parent multiple NetworkMaterials and other Namespaces.
5. Arrange the hierarchy by **middle-mouse dragging** items in the Material Scenegraph. The structure is reflected in both the Scene Graph and the terminal sidebar.
6. Right-click in the Material Scenegraph to **delete**, **duplicate**, or fully **expand/collapse** NetworkMaterials and Namespaces.
7. Assign each NetworkMaterial a **colour** so they can be told apart at a glance — the colour appears against the NetworkMaterial's name in the terminal sidebar.
8. Read the per-NetworkMaterial information in the Material Scenegraph: how many **renderers** and **terminals** are connected, and its **interactive** state.
9. Wire the shared part of the network once and branch it into each NetworkMaterial's terminals — that sharing is the entire point.
10. Collapse and expand NetworkMaterials and Namespaces from the **arrows on the terminal sidebar** as the network grows.

### Nodes / Tools / Settings
**The capability:** multiple NetworkMaterials inside one `NetworkMaterialCreate`, so shading nodes can be shared across different network materials, "reducing the number of nodes needed when creating variants of a material."

**Adding items** — Parameters (edit flag active) → **plus button** → `Add NetworkMaterial` or `Add Namespace`. Also available by right-clicking inside the Material Scenegraph.
**Renaming** — select and press `Enter`, or double-click.
**Arranging** — **middle-mouse drag** within the Material Scenegraph.
**Right-click menu** — delete, duplicate, fully expand, fully collapse.

**What a Namespace is:** adding one "creates a group in your Scene Graph tab, which can parent multiple Network Materials and other Namespaces for the purpose of organization." Organisational, not material.

**Three views of one structure.** The arrangement built in the **Material Scenegraph** is reflected in the **Scene Graph tab** and in the **terminal sidebar** inside the node. The sidebar's NetworkMaterials and Namespaces collapse and expand from their own arrows.

**Per-NetworkMaterial information in the Material Scenegraph:** the count of connected **renderers**, the count of connected **terminals**, the **interactive** state, and a **colour** — which is carried onto the NetworkMaterial's name in the terminal sidebar specifically so several can be distinguished at a glance.

**The worked example, with its numbers.** Two robot characters need different material variations. Both share a transmission mask, roughness and emissive texture files, and require the same glass shader.
- One NetworkMaterialCreate per material: **27 nodes**, with the shared portion duplicated.
- One NetworkMaterialCreate with two NetworkMaterials: **19 nodes**, by **sharing 8**.

The page is explicit that this is a small illustration: *"In production scripts featuring hundreds of nodes, the power of multiple NetworkMaterials within a single NetworkMaterialCreate node is far greater."*

**Referenced but not ingested:** the *NetworkMaterialCreate* parameter reference (ingested separately — see Related), and a Foundry course, *Creating Multiple Materials using NetworkMaterialCreate*.

### Difficulty
Intermediate

### Foundry App & Version
Katana 9.0v3 (page served from the current Katana 9.0v3 documentation set)

### Tags
katana, lookdev, nodegraph, katana-9, intermediate

---

## Scope note

This closes the last of the three NetworkMaterial items D4a recorded. The set now
reads as one topic across three entries: **`creating-shading-networks`** is the
workflow inside the node, **`networkmaterialcreate`** is the parameter reference,
and this page is the multi-material case. All three cross-reference each other in
Foundry's own docs, and now do so in the library.

The Foundry **course** named here (*Creating Multiple Materials using
NetworkMaterialCreate*) is a video series, not a doc page, and is **not**
ingested — recorded so a later pass does not read its absence as an unfilled
documentation gap.

---

## Related Tutorials
- [NetworkMaterialCreate](networkmaterialcreate.md) — shares `katana` + `lookdev` + `nodegraph`; **the parameter reference this page defers to twice.** The Material Scenegraph columns used here — Renderers, Terminals, Interactive, Color — and the `rootLocation` those NetworkMaterials are created under are documented there.
- [Creating Shading Networks](creating-shading-networks.md) — shares `katana` + `lookdev` + `nodegraph`; the workflow *inside* the node — the terminal sidebar, port type-checking and Dot routing you use to build the shared network this page then branches into several NetworkMaterials.
- [Setting up UsdPreviewSurface Materials](setting-up-usdpreviewsurface-materials.md) — shares `katana` + `lookdev` + `nodegraph`; a single NetworkMaterialCreate wired to one `usdSurface` terminal — the one-material case this page generalises.
