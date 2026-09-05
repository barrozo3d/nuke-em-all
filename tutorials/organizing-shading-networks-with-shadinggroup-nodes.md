---
title: Organizing Shading Networks with ShadingGroup Nodes
source: Article
url: https://learn.foundry.com/katana/Content/ug/adding_assigning_materials/using_the_shadinggroup_node.html
author: learn.foundry.com
ingested: 2026-09-04
app: "Katana"
version: "9.0 (learn.foundry.com/katana current docs at ingest; release notes whats_new_9.0)"
tags: [katana, lookdev, nodegraph, macro, katana-9, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/organizing-shading-networks-with-shadinggroup-nodes/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Organizing Shading Networks with ShadingGroup Nodes

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/adding_assigning_materials/using_the_shadinggroup_node.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Organizing Shading Networks with ShadingGroup Nodes Organizing Shading Networks with ShadingGroup Nodes Using the ShadingGroup Node Menu options Rearranging Ports Within ShadingGroups Sharing and Reusing ShadingGroups with Macros The ShadingGroup node is designed to keep your workspace organized by allowing you to group sections of your shading node network together. Inside a ShadingGroup node, there are fixed input and output bars, which are used to connect the nodes within the group to the rest of the network. This also means you are able to view and access the input and output ports of the nodes within the group on the exterior of the ShadingGroup node. These features of ShadingGroup nodes help to provide the artist with a user friendly interface and enables you to hide any unnecessary details from your shading node network. The ShadingGroup node Note: The ShadingGroup node is designed to be used within the NetworkMaterialCreate node and can therefore only be created whilst inside the NetworkMaterialCreate node. Using the ShadingGroup Node To create a ShadingGroup: Hit Tab . Type and select ShadingGroup from the Foundry nodes. You can jump inside the ShadingGroup in the same way as the NetworkMaterialCreate, by holding Ctrl and clicking with the Middle-mouse button or by clicking the enter node button. You can either create nodes directly inside the ShadingGroup or you can cut-and-paste existing nodes from your network, into the group. To connect shading nodes within the group to input and output sidebars: From your shading node, click the input parameter that you would like to be fed in. Click anywhere on the fixed INPUT bar on the left to create a port and path for that specific parameter. Click on the output parameter that you would like to be read out. Click anywhere on the fixed OUTPUT bar on the right to create a port and path for that specific parameter. Connecting a shading node within a ShadingGroup to the INPUT and OUTPUT sidebars Tip: The INPUT and OUTPUT bars are filterable in the same way as the terminals on a NetworkMaterialCreate node. Enter a string in the Filter bar to search. When you exit a ShadingGroup node, you'll see that the input and output parameters are visible on the outside of the node. You can now connect these up to the rest of your network. Connecting the ShadingGroup node to the rest of the Network In the same way as any node within a NetworkMaterialCreate node, you can collapse and expand the ShadingGroup using Alt + 1, Alt + 2 and Alt + 3 . This helps to keep the whole section organized. Tip: When collapsed, hovering over the shading node while pressing and holding the X key will temporarily expand it. It will collapse when released. Menu options From inside the ShadingGroup, right-click on one of your ports to bring up the options menu. From here, you can: Jump to the node it's connected to. Delete the port. Rename the port. ShadingGroup port menu options Tip: When renaming a port, you can use fullstops in between names to create nested pages. This is a great way of customizing your interface for input and output ports. Rearranging Ports Within ShadingGroups You can rearrange the order of your ports within a ShadingGroup, allowing you to customize its inputs and outputs. Rearranging ports allows you to organize your ShadingGroups easily. Changes made to the order of Input and Output ports made within the ShadingGroup are reflected on the ShadingGroup node when viewed within a Network Material context, such as NetworkMaterialCreate or NetworkMaterialEdit. Rearrange Input and Output ports by middle-mouse clicking the port you wish to move and then dragging it within its respective sidebar. Nested or grouped ports can also move between or out of groups by middle-mouse dragging the chosen port between groups. The order of rearranged ports is reflected in the ShadingGroup node once you exit the group. ShadingGroup with default port arrangements. The same ShadingGroup, with ports rearranged. Note: You can rearrange ports within LiveShadingGroups. However, if the LiveShadingGroup is locked, ports cannot be rearranged or edited. Sharing and Reusing ShadingGroups with Macros Macros enable you to wrap any single node, or ShadingGroup, and publish them so that their state is saved and they can be recalled in other shading networks. Saved macros can be added to a shader network as you would add a regular node, including from the Tab node creation menu. To create a macro in a shading network: Select the part of the shading network you want to save as a macro. Press G on the keyboard to convert the selected nodes into a ShadingGroup. The target shading nodes in the tree The target nodes collapsed into a group Note: If you're creating a macro from a single node, you don't need to create a group. Double-click the group, or use the keyboard shortcut E , to open its controls in the Parameters tab. Click the wrench icon and select Save as Macro . By default, macros are saved in your home directory in .katana/Macros/_User and are automatically assigned the suffix _User . See Macros for more detailed information. To add a macro to your shading network, press Tab on the keyboard and start typing the name of your macro. Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
Group a section of a shading network inside a **ShadingGroup** node, wiring the nodes within it to fixed **INPUT** and **OUTPUT** sidebars so only the ports you choose appear on the group's exterior.

### Summary
ShadingGroup is the organisational primitive of the NetworkMaterialCreate workflow, and it **can only be created inside a NetworkMaterialCreate node**. Inside it are fixed input and output bars: you click a node's input parameter and then the INPUT bar to create a port and a path for that specific parameter, and the same on the output side — which means the group's external interface is something you author deliberately rather than inherit. Ports can be reordered by middle-click-dragging within their sidebar, including moving nested ports between or out of groups, and the order is reflected on the node once you exit. Ports right-click to a menu that jumps to the connected node, deletes, or renames — and **renaming with full stops creates nested pages**, the same interface-shaping trick used for promoted parameters. The collapse controls match the rest of the workflow (**`Alt`+`1/2/3`**, with **`X`** held to temporarily expand a collapsed node), and both sidebars are filterable like NetworkMaterialCreate's terminals.

### Key Steps
1. Inside a NetworkMaterialCreate, press **`Tab`**, type and select **ShadingGroup** from the Foundry nodes.
2. Enter it by holding **`Ctrl`** and clicking the middle mouse button, or with the enter-node button — the same as NetworkMaterialCreate.
3. Create nodes inside it, or cut and paste existing nodes from the network into the group.
4. **Wire the inputs:** click the shading node's input parameter, then click anywhere on the fixed **INPUT** bar on the left to create a port and path for that parameter.
5. **Wire the outputs:** click the output parameter, then anywhere on the fixed **OUTPUT** bar on the right.
6. Filter long sidebars by typing in the **Filter** bar — they behave like NetworkMaterialCreate terminals.
7. Exit the group and connect the now-visible external ports to the rest of the network.
8. **Reorder ports** by middle-click-dragging within a sidebar; nested or grouped ports can be dragged between groups or out of them. The new order shows on the node after exiting.
9. Right-click a port for **jump to connected node**, **delete**, or **rename** — and use full stops when renaming to create **nested pages**.
10. Collapse and expand with **`Alt`+`1`**, **`Alt`+`2`**, **`Alt`+`3`**; hold **`X`** over a collapsed node to expand it temporarily.

### Nodes / Tools / Settings
- **ShadingGroup** — created only inside **NetworkMaterialCreate**; fixed **INPUT** / **OUTPUT** sidebars.
- Navigation: **`Tab`** to create, **`Ctrl`**+middle-click or the enter-node button to enter, **`Alt`+`1/2/3`** collapse states, **`X`** to peek.
- Port right-click menu: jump to node, delete port, rename port (full stops → nested pages).
- Middle-click-drag to reorder ports, including across nested groups.
- Sharing: the page's closing section covers reusing ShadingGroups as **macros**.
- ⚠️ Mentions **LiveShadingGroups** only in passing — ports can be rearranged in one, but not if it is **locked**.

### Difficulty
Intermediate

### Foundry App & Version
Katana 9.0.

### Tags
`katana`, `lookdev`, `nodegraph`, `macro`, `katana-9`, `intermediate`

---

## Related Tutorials
- [Building Materials Using NetworkMaterialCreate](building-materials-using-networkmaterialcreate.md) — the only place a ShadingGroup can be created.
- [Node Parameters and Interface Controls](node-parameters-and-interface-controls.md) — promotion reaches parameters inside ShadingGroups.
- [LiveGroups and LiveShadingGroups](livegroups-and-liveshadinggroups.md) — the still-undefined term this page also only references.

---

> **Provenance.** `learn.foundry.com/katana` (MadCap Flare). Paths in this doc set
> are not guessable and `Data/Tocs/*` 404s, so this page was reached by crawling
> from `Content/learn_katana.html` → `user_guide.html`, or from a sibling page's
> own links. Reference-guide and user-guide pages carry clean `<title>`s and need
> no `--title` override, unlike `learn.foundry.com/nuke/developers/**`.
