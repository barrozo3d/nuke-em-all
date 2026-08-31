---
title: Creating Shading Networks
source: Article
url: https://learn.foundry.com/katana/Content/ug/adding_assigning_materials/creating_shading_networks.html
author: learn.foundry.com
ingested: 2026-08-31
app: Katana
version: 9.0v3
tags: [katana, lookdev, nodegraph, katana-9, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/creating-shading-networks/
frame_count: 0
frame_status: skipped
---

# Creating Shading Networks

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/adding_assigning_materials/creating_shading_networks.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Creating Shading Networks Creating Shading Networks NetworkMaterialCreate Overview The Node Menus Connecting Shading Nodes Organizing a Shading Network with Dot Nodes Hiding Node Connections Customizing Drawing Style for Node Connections This topic explains how to use the NetworkMaterialCreate node to build a shading node network. Note: To learn about the NetworkMaterialCreate node parameters, see NetworkMaterialCreate . This example illustrates the difference between the previous, and new workflows for building materials. Both networks function in the same way and have the same end result. Previous NetworkMaterial workflow VS current NetworkMaterialCreate workflow Rendered result for both workflows NetworkMaterialCreate Overview The NetworkMaterialCreate node is created in the same way as any other node, hit Tab , select it from the menu and place it in your node graph. To jump inside the node, you can: Ctrl + Middle-mouse click on the node. Click the enter node button. Select the node and hit Ctrl + Enter . Inside the NetworkMaterialCreate node is a fixed sidebar on the right, which shows each NetworkMaterial and their terminals for each renderer you have set up with Katana . This sidebar functions in the same way as the Network Material node in the previous workflow, but all the terminals are prepopulated so the user doesn’t need to add them manually. The sidebar can be hidden and exposed using the collapse and expand tabs. Note: By default, a NetworkMaterialCreate node provides one NetworkMaterial location. If you would like to discover how to set up multiple NetworkMaterial locations within one NetworkMaterialCreate node, see Multiple NetworkMaterials with NetworkMaterialCreate . The NetworkMaterialCreate node Inside the NetworkMaterialCreate node At the top of this bar there is a Filter which allows you to enter a string to search for a specific terminal. For example, start typing ‘displacement’ and the list filters down to only show the terminals containing the word displacement. This is useful especially if you have multiple renderers or NetworkMaterials set up. Under the Filter bar is the name of your Network Material, you can rename this from the Parameters tab, by double clicking your Network Material or selecting it and pressing Enter on the keyboard. The fixed terminal sidebar Note: Renaming the node itself won’t change the name you’ll see on the terminal sidebar. The Network Material name can be changed from the Parameters Node Parameters tab. The Node Menus To create a shading node, press Tab from inside a NetworkMaterialCreate node to bring up the node creation menu, and type the node name. As you're typing, the menu will filter down. When inside a NetworkMaterialCreate node, the menu is limited to show your default renderer nodes, and a few standard Katana nodes, only the nodes you are able to use are visible. The nodes have a colored stripe on the left to indicate whether they belong to a renderer or whether they are standard Katana nodes. For example, the 3Delight shading nodes are color-coded with a red stripe and the Katana nodes appear yellow. Colored stripes in the node creation menu indicate group type You can alter the node menu to display shading nodes from your other renderers. To do this: Hold Shift and hit Tab . Select the required renderer. Hit Tab again to bring up the node menu for your selected renderer. The S key is a 3Delight keyboard shortcut which brings up the node creation menu for 3Delight shading nodes. This can be useful if you want to switch back and forth between two renders as you can use the S key to bring up 3Delight shading nodes whilst using Tab to bring up the node menu for a different renderer. Tab Node menu for selected renderer. S Node menu for 3Delight shading nodes. Shift + Tab Select renderer to change node menu. Note: It is possible to change the nodeType from within a shading node's parameters. Values of any parameter names that overlap between node types will be remembered and no changes will be lost if you want to switch back and forth. Connecting Shading Nodes Setting up shading nodes within the NetworkMaterialCreate node is designed to make things as simple as possible for artists. Shading networks set up inside the group feature a left-to-right workflow which is well suited to working with a large number of shading nodes. The shading nodes themselves are designed and optimized for creating materials, as the input and output ports are all visible and clearly labeled. Tip: You can rename the shading nodes by selecting the node, hitting Enter , and typing the new name. You can also show and hide the Filter function on selected nodes using the Alt + Enter keyboard shortcut. Shading Node UI Tip: Some pairs or groups of nodes that are normally used together or that rely on each other, are automatically created when you place one of the nodes. For example, if you place a file node, a place2DTexture node is automatically created. To link shading nodes together, click once on a parameter port to begin drawing the connection, and then click once on the other shading node's port to connect the two nodes together. Invalid target ports are grayed out and disabled to show which connections are available. The input and output ports are all color-coded to indicate which connections can be made. You can only connect the compatible data types, for example, int to int and float to float. Tip: Hover your cursor over the input/ouput port to see what data type it provides/receives. Tip: Hover over a connection and press ' / ' on your keyboard to follow the connection to its connected node. Tip: To select all upstream nodes from a selected node in the Network Material context, you can use Ctrl + Left Arrow . Or to select all downstream nodes from that node, use Ctrl + Right Arrow . Data Type Color Codes: color float / array_float int matrix normal point string vector disabled misc Connecting shading nodes Once your shading nodes are connected to the terminal sidebar, the network is now set up and your NetworkMaterial is in your Scene Graph under /root/materials by default. Note: To learn how to change your NetworkMaterial scene graph location and other NetworkMaterialCreate parameters, see NetworkMaterialCreate . Tip: In the same way as the terminal sidebar, you can type in the Filter field of the shading nodes to quickly search for an input/output, even if the menu is not expanded. You can show and hide the Filter function on selected nodes using the Alt + Enter keyboard shortcut. The arrows on the shading nodes show if a page is expanded: - A downwards-facing arrow means the page is expanded. - A right-facing arrow means the page is collapsed. You can click on the page titles to expand/collapse pages so that you can hide certain sections. To collapse/expand the entire shading node, you can click the expand/collapse state button at the top-left of a node or use the keyboard shortcuts: Tip: You can use the preference nodegraph defaultShadingNodeViewState to set the default expand/collpase state of new nodes. ALT + 1 - Collapse completely. ALT + 2 - Expand to show connected ports. Tip: The example shows just connections exposed, but you can expose the pages containing the connected inputs and outputs, such as Base by enabling the showPagesConnectedOnly control in the Preferences under nodegraph . ALT + 3 - Fully expand pages and connections. When collapsed, you can hover over a shading node while pressing and holding the X key and it will temporarily expand. It will collapse when released. If a node is collapsed, you can also drag a connection over the node to automatically expose compatible connections. The node collapses again automatically after connecting the input or output. The same is true if you change you mind and drop the connection outside the node. A collapsed dlPrincipled target node with no exposed connections Dragging a connection over the node auto-expands compatible connections The auto-collapsed node after a connection is made You can hover over a connection to display a tooltip detailing the node the connection originates from and the node it is connected to downstream. The data types of each connection are also shown. Organizing a Shading Network with Dot Nodes Dot nodes can help you organize complex shading networks to make them easier to read. For example, you can bend connections around notes for other artists or use a Dot to connect a single output to multiple inputs. Using Dot nodes to bend connections Splitting an input using a Dot node You can add a Dot like any other node, by pressing Tab and then typing Dot into the node finder, but the fastest way to add a Dot node is to press . (period) on your keyboard. Like other nodes, the Dot node sticks to your pointer and you can click anywhere in the shading network to place it. Alternatively, you can add Dot nodes when hovering over a connection to insert the Dot between nodes or you can drag a node output and then add a Dot node to create a Dot chain. Adding a Dot node to a connection Adding multiple Dot nodes to create a chain Dot nodes in shading networks are omnidirectional, meaning you can connect to them and drag outputs from them in any direction. They can have as many output connections as you like, but only one input connection. Hiding Node Connections In node-heavy shading networks, the connections between nodes can cause confusion if you're looking for a particular input. You can show and hide node input connections to clean up the network by navigating to Edit Toggle Input Connection Visibility or by using the Alt + H keyboard shortcut. Tip: You can also show and hide the Filter function on selected nodes using the Alt + Enter keyboard shortcut. Select the node or nodes you want to affect in the shader tree. In this example, the Diffuse and Roughness nodes. Navigate to Edit Toggle Input Connection Visibility or use the Alt + H keyboard shortcut to hide the input connections on the selected nodes. Deselect the nodes to see the effect. You can select a node in the tree to temporarily display its input connections. When the inputs are hidden, the connections on the node are still filled to indicate that a hidden connection exists. Select the nodes and navigate to Edit Toggle Input Connection Visibility or use the Alt + H keyboard shortcut to show the input connections on the selected nodes. Tip: Hold Alt + H with no selection to temporarily show hidden connections. Customizing Drawing Style for Node Connections Go into Edit Preferences nodegraph Under the networkMaterialNodegraph page, modify the connectionStyle preference. There are three options: Line - all connections are straight Short Curve - This will enforce a curve at the point of which it meets the port, similar to the one used when connections are made against a Dot node in this context Bezier Curve - This is the default for the material context, connections are drawn as bezier curves For the above, these options will be set within the layout preferences and not saved as part of the materials created. Your browser does not support the video tag. Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
Building a renderer shading network inside Katana's **NetworkMaterialCreate** node — the current workflow that replaces the older Network Material node, where the NetworkMaterial terminals are prepopulated in a fixed sidebar instead of being added by hand.

### Summary
NetworkMaterialCreate is a group you jump *inside* to author a shading network left-to-right, wiring renderer shading nodes into terminals that Katana has already created for every renderer configured in the session. The page contrasts it directly with the previous NetworkMaterial workflow — both produce the same rendered result, but the terminals no longer have to be added manually — and once the network reaches the terminal sidebar the NetworkMaterial appears in the Scene Graph under `/root/materials` by default. Most of the page is the node-graph craft that makes large networks workable: type-checked, colour-coded ports, three expand/collapse states, Dot nodes for routing, hideable input connections, and a preference for how connections are drawn.

### Key Steps
1. Create a **NetworkMaterialCreate** node like any other — `Tab`, type the name, place it in the node graph.
2. Jump inside it: **Ctrl + Middle-mouse click**, the **enter node** button, or select it and press **Ctrl + Enter**.
3. Read the **fixed terminal sidebar** on the right: one entry per NetworkMaterial, with terminals prepopulated for every renderer set up with Katana. Collapse/expand it with its tabs; filter it by typing (e.g. `displacement`) into the **Filter** field.
4. Name the NetworkMaterial from the **Parameters → Node Parameters** tab, or double-click it, or select it and press **Enter**. Renaming the *node* does **not** change the name shown on the terminal sidebar.
5. Create shading nodes with **Tab** from inside the node. The menu is restricted to your default renderer's nodes plus a few standard Katana nodes, and only nodes you can actually use are shown. To reach another renderer's nodes, hold **Shift + Tab**, pick the renderer, then **Tab** again.
6. Wire nodes up: click once on a port to start the connection, click once on the target port to complete it. Invalid targets are greyed out, and only compatible data types connect (`int`→`int`, `float`→`float`).
7. Connect the network into the terminal sidebar — at that point the NetworkMaterial exists in the Scene Graph under `/root/materials` by default.
8. Manage density with the three view states — **Alt+1** collapse completely, **Alt+2** expand to connected ports, **Alt+3** fully expand pages and connections — and hold **X** over a collapsed node to peek at it.
9. Route with **Dot** nodes: press **.** (period) to place one, or hover a connection to insert it inline. A Dot takes **one input** and as many outputs as needed, and is omnidirectional.
10. Clean up visually: **Alt + H** (or *Edit → Toggle Input Connection Visibility*) hides input connections on selected nodes, and *Edit → Preferences → nodegraph → networkMaterialNodegraph → connectionStyle* sets how connections are drawn.

### Nodes / Tools / Settings
**Node:** `NetworkMaterialCreate` — the current node for authoring shading networks. It supersedes the previous **Network Material** node workflow; the page shows both side by side and states they function the same way with the same end result, the difference being that NetworkMaterialCreate's terminals are prepopulated rather than added manually. By default it provides **one** NetworkMaterial location (multiple locations are a separate topic).

**Entering the node:** `Ctrl` + Middle-mouse click · the enter-node button · select + `Ctrl` + `Enter`.

**Terminal sidebar:** fixed, right-hand side; one block per NetworkMaterial with its terminals per configured renderer; collapse/expand tabs; **Filter** field for substring search across terminals.

**Naming:** the NetworkMaterial name is set in **Parameters → Node Parameters**, by double-clicking it, or by selecting it and pressing `Enter`. ⚠️ Renaming the node itself does not rename the terminal-sidebar entry.

**Node creation menu (inside NetworkMaterialCreate):**

| Shortcut | Effect |
|---|---|
| `Tab` | Node menu for the selected renderer (filters as you type) |
| `Shift` + `Tab` | Choose which renderer the node menu shows |
| `S` | 3Delight-specific shortcut for the 3Delight shading-node menu |

Nodes carry a **coloured left stripe** for their group: 3Delight shading nodes red, standard Katana nodes yellow. `nodeType` can be changed from within a shading node's parameters, and values of parameter names shared between the two types are remembered, so switching back and forth loses nothing.

**Connecting:** click a port to start, click the target port to finish. Invalid targets are greyed out and disabled. Ports are colour-coded by data type and only compatible types connect. Data-type colour codes cover: `color`, `float` / `array_float`, `int`, `matrix`, `normal`, `point`, `string`, `vector`, `disabled`, `misc`. Hover a port for its data type; hover a connection for a tooltip naming the origin node, the downstream node and the data types; hover a connection and press `/` to follow it to its connected node.

**Selection:** `Ctrl` + `Left Arrow` selects all upstream nodes, `Ctrl` + `Right Arrow` all downstream — in the Network Material context.

**Auto-created pairs:** some nodes that are always used together are created together — placing a `file` node automatically creates a `place2DTexture` node.

**Shading-node view states:** `Alt`+`1` collapse completely · `Alt`+`2` expand to show connected ports · `Alt`+`3` fully expand pages and connections. Also: the expand/collapse button at a node's top-left; page-title click to expand/collapse individual pages; a downward arrow means expanded, a right-facing arrow collapsed. Hold `X` while hovering a collapsed node to expand it temporarily. Dragging a connection over a collapsed node auto-exposes compatible connections and re-collapses after the connection is made or dropped outside.

**Renaming / filtering shading nodes:** select + `Enter` to rename; `Alt` + `Enter` shows/hides the Filter function on selected nodes; the Filter field searches inputs/outputs even when the menu is not expanded.

**Preferences (`Edit → Preferences → nodegraph`):**
- `defaultShadingNodeViewState` — default expand/collapse state for new nodes.
- `showPagesConnectedOnly` — expose only pages containing connected inputs/outputs.
- `networkMaterialNodegraph → connectionStyle` — **Line** (straight) · **Short Curve** (curves at the port, like a Dot-node connection here) · **Bezier Curve** (**default** in the material context). These live in the layout preferences and are **not** saved as part of the materials created.

**Dot node:** `.` (period) is the fastest way to place one; also `Tab` → `Dot`, inserting on a hovered connection, or dragging an output then adding a Dot to build a chain. Omnidirectional; **one input, any number of outputs**. Used to bend connections around notes and to split one output to several inputs.

**Hiding connections:** *Edit → Toggle Input Connection Visibility* or `Alt` + `H` on selected nodes. Hidden inputs still render as *filled* ports so the hidden connection is discoverable; selecting a node temporarily shows its inputs; holding `Alt` + `H` with nothing selected temporarily reveals all hidden connections.

**Scene graph result:** once wired to the terminal sidebar, the NetworkMaterial appears under `/root/materials` by default (the location is a NetworkMaterialCreate parameter).

### Difficulty
Intermediate

### Foundry App & Version
Katana 9.0v3 (page served from the current Katana 9.0v3 documentation set)

### Tags
katana, lookdev, nodegraph, katana-9, intermediate

---

## Scope note — what this page does and does not cover

This is the **workflow** page for NetworkMaterialCreate, not the parameter
reference. It says so twice and points at the `NetworkMaterialCreate` reference
page for parameters (including changing the NetworkMaterial's scene graph
location), and at a separate page for **multiple NetworkMaterials in one
NetworkMaterialCreate**. Neither is ingested; both are recorded in
`KNOWLEDGE_GAPS_TODO.md` with verified URLs.

**Material stylesheets are not here.** One of C1's six zero-corroboration terms
was `material stylesheet` / `stylesheet`, and the materials section was the
plausible home for it — it is not on this page (zero occurrences), and it is not
at any of the obvious Katana doc paths, all of which 404. Recorded as still
unlocated rather than assumed absent from the product.

---

## Related Tutorials
- [Setting up UsdPreviewSurface Materials](setting-up-usdpreviewsurface-materials.md) — shares `katana` + `lookdev` + `nodegraph`; that page builds a UsdPreviewSurface *inside* a NetworkMaterialCreate and wires it to the `usdSurface` terminal, so it is this page's workflow applied to a specific USD shader — read this one first for the node itself.
- [GafferThree](gafferthree.md) — shares `katana` + `lookdev` + `katana-9`; GafferThree assigns shaders to lights from its own object table, the counterpart to authoring geometry materials as a shading network here.
- [LiveGroups and LiveShadingGroups](livegroups-and-liveshadinggroups.md) — shares `katana` + `nodegraph`; a completed shading network is exactly the kind of self-contained node group a LiveGroup publishes and reloads across projects.
- [OpScript Tutorials](opscript-tutorials.md) — shares `katana` + `nodegraph`; where this page wires materials by hand in the node graph, OpScript's `Interface` API creates and edits the underlying scene graph locations procedurally.
- [RenderOutputDefine](renderoutputdefine.md) — shares `katana` + `katana-9`; the `Ci` (final shader colour) pass it can output is the rendered result of the shading network authored here.
- [NetworkMaterialCreate](networkmaterialcreate.md) — shares `katana` + `lookdev` + `nodegraph`; **the parameter reference this page defers to twice.** `rootLocation` (default `/root/materials`) is the scene graph location referred to here, and Namespaces, the Material Scenegraph and Interface Controls live there.
- [Multiple NetworkMaterials with NetworkMaterialCreate](multiple-networkmaterials-with-networkmaterialcreate.md) — shares `katana` + `lookdev` + `nodegraph`; the network built here can feed **several** NetworkMaterials in one node, so variants share their common shading nodes instead of duplicating them.
