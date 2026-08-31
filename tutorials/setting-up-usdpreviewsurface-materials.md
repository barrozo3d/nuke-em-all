---
title: Setting up UsdPreviewSurface Materials
source: Article
url: https://learn.foundry.com/katana/Content/ug/using_hydra_viewer/usd_setting_up_materials.html
author: learn.foundry.com
ingested: 2026-08-24
app: "Katana"
version: "9.0v3"
tags: [katana, usd, lookdev, nodegraph, katana-9, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/setting-up-usdpreviewsurface-materials/
frame_count: 0
frame_status: skipped
---

# Setting up UsdPreviewSurface Materials

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/using_hydra_viewer/usd_setting_up_materials.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Setting up UsdPreviewSurface Materials You can use UsdPreviewSurface shading nodes to build USD materials. You can then assign these materials to your object and view the result in the Hydra Viewer . UsdPreviewSurface shading node types are accessible from the USD shading node creation menu inside NetworkMaterialCreate nodes. To use UsdPreviewSurface to display materials in the Hydra Viewer : Load the USD plug-ins into Katana by following the steps in the Loading USD Plug-ins into Katana topic. Create a NetworkMaterialCreate node and jump inside it, or jump inside an existing NetworkMaterialCreate node. Note: If you are using an existing NetworkMaterialCreate node, you may need to refresh the Sidebar Terminal to see the usd outputs. To do this, open the Parameters for the NetworkMaterialCreate node and choose Shelf Actions Refresh Sidebar Terminal . Press Shift + Tab to open the renderer selection menu and choose USD . Press Tab to open the USD shading node creation menu. Select UsdPreviewSurface and place the node. Connect the surface output from the UsdPreviewSurface node to the usdSurface input under the usd drop-down in the Terminal sidebar. Open the Parameters for the UsdPreviewSurface and make the required adjustments. Use a MaterialAssign node to assign the material to your geometry. Note: For more information about assigning materials, see the Assigning Materials and Textures section of the Material Basics topic. In the Viewer tab, click View and disable Basic Material to preview your USD material. In the Viewer tab, click View and choose Shadows from All Lights to preview your material with shadows. If you only want selected lights to cast shadows, you can use the Shadows from Selected Lights option. Basic Material off No Shadows Basic Material off Shadows from All Lights You can assign texture maps to UsdPreviewSurface shading nodes using UsdUVTexture node types. To assign a texture map to the diffuseColor parameter in your UsdPreviewSurface shading node: Create a UsdUVTexture node, open the Parameters , and enter the file path in the file parameter. Connect the rgb output from the UsdUVTexture node to the diffuseColor input of the UsdPreviewSurface node. Create a UsdPrimvarReader_float2 node and plug the result output into the st input on the UsdUVTexture . Within the UsdPrimvarReader_float2 , set the varname parameter to st . The texture can now be seen on the object in the Hydra Viewer . Basic Material off, Shadows from All Lights Video: For a full tutorial series on using USD Preview Surface materials, take a look at our Setting Up USD Preview Surface Materials course. Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
Building a USD material in Katana from `UsdPreviewSurface` shading nodes inside a **NetworkMaterialCreate**, wiring it to the `usdSurface` terminal, assigning it with **MaterialAssign**, and previewing it live in the Hydra Viewer — including texture lookup via `UsdUVTexture` fed by a `UsdPrimvarReader_float2`.

### Summary
`UsdPreviewSurface` is the portable USD surface shader, and in Katana it is authored like any other renderer's shader graph: inside a NetworkMaterialCreate node, with USD selected as the renderer, then connected to the `usdSurface` input on the Terminal sidebar. Assignment is ordinary MaterialAssign; the payoff is that the Hydra Viewer previews the result directly, with optional shadows from all or only selected lights, once **Basic Material** is disabled in the Viewer's View menu. Texturing follows the standard USD pattern — a `UsdUVTexture` node reading a file, its `rgb` output into `diffuseColor`, and a `UsdPrimvarReader_float2` with `varname` set to `st` supplying the UV coordinates.

### Key Steps
1. Load the USD plug-ins into Katana first (see the *Loading USD Plug-ins into Katana* topic) — the USD shading nodes are not available otherwise.
2. Create a **NetworkMaterialCreate** node and jump inside it, or enter an existing one. On an existing node the USD outputs may not appear until the terminal is refreshed: **Parameters → Shelf Actions → Refresh Sidebar Terminal**.
3. Press **Shift + Tab** to open the renderer selection menu and choose **USD**.
4. Press **Tab** to open the USD shading node creation menu, select **UsdPreviewSurface**, and place the node.
5. Connect the node's `surface` output to the `usdSurface` input, found under the `usd` drop-down in the Terminal sidebar.
6. Open the UsdPreviewSurface **Parameters** and set the surface values.
7. Assign the material to geometry with a **MaterialAssign** node (see *Material Basics → Assigning Materials and Textures*).
8. In the **Viewer** tab, open **View** and **disable Basic Material** — until this is off, the viewer shows its default shading rather than your USD material.
9. Still under **View**, choose **Shadows from All Lights** to preview with shadows, or **Shadows from Selected Lights** to restrict casting to chosen lights.
10. To texture a parameter: create a **UsdUVTexture** node and set its `file` parameter, connect its `rgb` output to the UsdPreviewSurface `diffuseColor` input, then create a **UsdPrimvarReader_float2**, plug its `result` output into the UsdUVTexture's `st` input, and set the reader's `varname` to `st`. The texture then appears on the object in the Hydra Viewer.

### Nodes / Tools / Settings
**Nodes:** NetworkMaterialCreate (container for the shading graph) · UsdPreviewSurface (USD surface shader) · UsdUVTexture (texture read) · UsdPrimvarReader_float2 (UV/primvar lookup) · MaterialAssign (assignment to geometry).

**Connections:** UsdPreviewSurface `surface` → `usdSurface` (under the `usd` drop-down in the Terminal sidebar) · UsdUVTexture `rgb` → UsdPreviewSurface `diffuseColor` · UsdPrimvarReader_float2 `result` → UsdUVTexture `st`.

**Parameters:** UsdUVTexture `file` (texture path); UsdPrimvarReader_float2 `varname` = `st`.

**UI / shortcuts:** **Shift + Tab** — renderer selection menu (choose USD); **Tab** — shading node creation menu; **Parameters → Shelf Actions → Refresh Sidebar Terminal** on an existing NetworkMaterialCreate whose `usd` outputs are missing.

**Viewer (Hydra) settings:** View → **Basic Material** (must be *disabled* to see the USD material); View → **Shadows from All Lights**; View → **Shadows from Selected Lights**.

**Prerequisite:** USD plug-ins loaded into Katana.

**Referenced elsewhere on the page:** a Foundry course, *Setting Up USD Preview Surface Materials*, is linked as a fuller tutorial series — not ingested here.

### Difficulty
Intermediate

### Foundry App & Version
Katana 9.0v3 (current Katana documentation set)

### Tags
katana, usd, lookdev, nodegraph, katana-9, intermediate

---

## Related Tutorials
- [GafferThree](gafferthree.md) — shares `katana` + `lookdev`; GafferThree lights are what the Hydra Viewer's **Shadows from All Lights / Selected Lights** preview options here are casting from, and both assign materials through the same Katana mechanisms.
- [OpScript Tutorials](opscript-tutorials.md) — shares `katana` + `nodegraph`; `UsdPrimvarReader_float2` reads a primvar (`st`) off the geometry, which is the attribute-to-shader transfer that OpScript can author or override at the scene graph level.
- [LiveGroups and LiveShadingGroups](livegroups-and-liveshadinggroups.md) — shares `katana` + `nodegraph`; the NetworkMaterialCreate setup built here is exactly the kind of self-contained node group a LiveGroup is meant to publish and share between departments.
- [Creating Shading Networks](creating-shading-networks.md) — shares `katana` + `lookdev` + `nodegraph`; this page builds a UsdPreviewSurface *inside* a NetworkMaterialCreate, and that page documents the node itself — the terminal sidebar, port type-checking and view states used here.
- [NetworkMaterialCreate](networkmaterialcreate.md) — shares `katana` + `lookdev` + `nodegraph`; `rootLocation` is what decides where the `usdSurface`-terminated material built here lands in the scene graph.
- [Using Native USD Workflows](using-native-usd-workflows.md) — shares `katana` + `usd` + `nodegraph`; **the map this page is one instance of** — it names the whole native USD node set, including the `UsdMaterial` / `UsdMaterialAssign` route worked through here.
- [UsdSchemaSet](usdschemaset.md) — shares `katana` + `usd` + `katana-9`; `MaterialBindingAPI` is named there as an API schema, and this page is the material-assignment workflow such a binding expresses on the native USD path.
