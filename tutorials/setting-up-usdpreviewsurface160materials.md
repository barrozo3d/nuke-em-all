---
title: Setting up UsdPreviewSurface&#160;Materials
source: Article
url: https://learn.foundry.com/katana/Content/ug/using_hydra_viewer/usd_setting_up_materials.html
author: learn.foundry.com
ingested: 2026-08-24
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/setting-up-usdpreviewsurface160materials/
frame_count: 0
frame_status: skipped
---

# Setting up UsdPreviewSurface&#160;Materials

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
