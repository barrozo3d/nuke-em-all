---
title: Material Basics
source: Article
url: https://learn.foundry.com/katana/Content/ug/adding_assigning_materials/material_basics.html
author: learn.foundry.com
ingested: 2026-09-04
app: "Katana"
version: "9.0 (learn.foundry.com/katana current docs at ingest; release notes whats_new_9.0)"
tags: [katana, lookdev, cel, scenegraph, katana-9, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/material-basics/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Material Basics

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/adding_assigning_materials/material_basics.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Material Basics Note: The following steps are part of a legacy workflow, as of Katana 3.2 you can create materials using NetworkMaterialCreate nodes. For more information and workflow examples, see Building Materials Using NetworkMaterialCreate . Creating a Material The first stage in creating a material is the creation of that material’s location. This is the scene graph location that acts as a container for one or more shaders. To create a material location: 1. Create a Material node and add it to your recipe. Materials are usually created in their own branch and a Merge node is used to connect them to the rest of the recipe. If you need multiple materials, use a MaterialStack node. See Adding Multiple Materials for more information. 2. Select the Material node and press Alt + E . The Material node becomes editable within the Parameters tab. 3. Enter the material’s name in the name parameter. Although strictly not needed as Katana handles name clashes gracefully, it is good practice to name the material, as the name is used for both the node name and the material’s scene graph location. 4. In the namespace parameter, enter the location below /root/materials to place the material. By default, the material is placed below /root/materials in the scene graph. If namespace is not blank, the material is placed below /root/materials/ namespace . Some of the most common namespaces are included as a dropdown to the right of the parameter. You can also specify nested namespaces, for instance, if the namespace parameter is geo/metals , the material is placed in the scene graph below /root/materials/geo/metals . Adding a Shader to a Material Location A material location needs to have one or more shaders attached. To add shaders to the material location: 1. Follow steps 1 to 4 in Material Basics above to create a material location. 2. Click Add shader and select a shader type. The list of shader types varies depending on the renderers installed. 3. Add a shader to the new shader type’s parameter. You can: • Click to the immediate right of the shader type and select the shader from the list. OR • Browse for a shader with Browse... and navigate to the shader using the Shader Browser dialog, select it and click Accept . 4. If you want to set any of the shader’s parameters to non-default values, expand the parameters for the shader by clicking and enter the changes where needed. 5. Repeat steps 2 to 4 for any additional shaders for this material. A possible combination might be a surface shader and a displacement shader. Material locations can have shaders from more than one renderer, only shaders for the appropriate renderer are selected at render time. This makes it possible for a single material to control how an object looks in a number of different renderers. Editing a Material Once a material is created, it is not locked down. Later in the recipe, you can edit the material using another Material node. To edit a material location: 1. Create a Material node and connect it to the recipe downstream of the target material. 2. Select the Material node and press Alt + E . The Material node becomes editable within the Parameters tab. 3. Select edit material in the action parameter dropdown. 4. Enter the scene graph location of the material to edit in the location parameter within the edit parameter grouping. See Manipulating a Scene Graph Location Parameter for details on scene graph location parameter fields. The shaders and their current parameter values are displayed below. 5. Edit the shaders for that material location wherever needed. This includes adding additional shaders. Overriding a Material As a material location can be assigned to multiple pieces of geometry, sometimes a geometry-specific change is needed. One way to perform this change is to use a material override. You point the Material node at the location(s) to override. Then any changes made are stored on the materialOverride attribute of the location. It is also possible to override material locations directly. In this case, the override acts in the same way as an edit. You can also override multiple materials at once, but only edit one. To override the material at a geometry location: 1. Create a Material node and connect it to the recipe downstream of the target material. 2. Select the Material node and press Alt + E . The Material node becomes editable within the Parameters tab. 3. Set the action dropdown to override materials . 4. Assign the scene graph locations of the geometry locations to the CEL parameter (located in the overrides parameter grouping). See Assigning Locations to a CEL Parameter for more on using CEL parameter fields. 5. In the Scene Graph tab, select the material location of the material assigned at the geometry location (or select Select In Scene graph on the materialAssign attribute of the geometry location). 6. Middle-click and drag from the attribute to override to the Drop Attributes Here hotspot at the top of the attrs parameter grouping. The attribute displays within the attrs parameter grouping and can now be overriden inside the Parameters tab. All changes you make are added as attributes to the location(s) specified by the CEL parameter (under the materialOverride attribute). Assigning Materials and Textures As mentioned in the introduction, a material location needs to be associated with a geometry or light location. This is achieved with the MaterialAssign node. To assign a material to a scene graph location: 1. Create a MaterialAssign node and connect it to the recipe after both the geometry and material locations have been created. 2. Select the MaterialAssign node and press Alt + E . The MaterialAssign node becomes editable within the Parameters tab. 3. Add the scene graph locations where the material is to be assigned to the CEL parameter. See Assigning Locations to a CEL Parameter for more on using CEL parameter fields. 4. Enter the scene graph location of the material to assign in the materialAssign parameter. See Manipulating a Scene Graph Location Parameter for details on scene graph location parameter fields. Tip: The best way to enter a material into the materialAssign parameter is to Shift +middle-click and drag from the Material node in the Node Graph tab to the materialAssign parameter. This creates an expression linking the material created by the Material node to the materialAssign parameter. Shaders may be responsible for how a geometry location is rendered, but a lot of the time, the richness of the render comes from a number of asset-specific textures. These textures sometimes need to be passed to the shader on a per-asset basis. Katana provides a number of ways to assign textures to assets depending on your pipeline. For more information on textures, refer to Handling Textures . Forcing Katana to Resolve a Material By default, Katana connects a geometry or light location with its respective material using the location’s materialAssign attribute. This attribute points to where the material is located within the scene graph. At render time, an implicit resolver copies the material, pointed to by the materialAssign attribute, to the geometry or light’s location. For more on implicit resolvers and their benefits, see Turning on Implicit Resolvers . You can force material resolving at an earlier point within a recipe using the MaterialResolve node. To force materials to be resolved earlier within the recipe, create a MaterialResolve node and connect it to the recipe at the point materials should be resolved . Using Face Sets When assigning materials to assets, it is often useful to break up the asset into smaller parts based on its faces. This allows different materials to be assigned to the different parts. Creating a Face Set Face sets are just a list of faces for a particular polymesh or subdivision surface. To create a face set: 1. Create a FaceSetCreate node and connect it to the recipe at the point you want to create the face set. 2. Select the FaceSetCreate node and press Alt + E . The FaceSetCreate node becomes editable within the Parameters tab. 3. Add to the meshLocation parameter the polymesh or subdivision surface scene graph location. For more on editing a scene graph location parameter, see Manipulating a Scene Graph Location Parameter . 4. Enter the name of this face set in the faceSetName parameter. This is the name that is displayed in the Scene Graph tab below the meshLocation scene graph location. 5. Switch the Viewer tab into face set selection mode by: • selecting the polymesh or subdivision surface in the Scene Graph tab and clicking in the Viewer tab, or • Shift +middle-click and drag the FaceSetCreate node onto the icon, or • middle-click and drag the selection parameter name onto the icon. 6. Select the faces for this face set. You can: • Select individual faces or marquee select multiple faces. • Use the Shift key while selecting to toggle whether a face is included, or the Ctrl key to remove faces, or hold Ctrl + Shift to add faces. • Select Selection X-ray Selection in the Viewer tab to toggle between only selecting the faces that are visible, and selecting all faces encompassed by the selection. 7. When you are happy with the selection, click next to the selection parameter and then select Adopt Faces From Viewer . The Viewer tab exits face selection mode and the currently selected faces are copied to the selection parameter. Tip: You can invert the selection using the invertSelection checkbox. Using two FaceSetCreate nodes, this feature, and an expression between the selection parameters, you can assign materials to both halves of an asset. Editing a Face Set If you need to edit an existing face set, you can: • Shift +middle-click and drag the FaceSetCreate node onto the icon, or • middle-click and drag the selection parameter name onto the icon. This puts the Viewer tab into face selection mode and enables you to edit the faces selected following the steps from Step 6 in Creating a Face Set . Assigning Materials to a Face Set Assigning materials to a face set is done in the same way as assigning a material to any other location. Using a MaterialAssign node to edit the materialAssign attribute of the face set’s scene graph location. Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
The **legacy** material workflow: a **Material** node creates a material *location* under `/root/materials`, shaders are attached to it, and a **MaterialAssign** node binds that location to geometry or lights through a CEL statement.

### Summary
⚠️ **The page opens by declaring itself legacy** — as of Katana 3.2, materials are built with **NetworkMaterialCreate**. It remains essential reading because it defines the vocabulary everything else assumes: a material is a *scene graph location* acting as a container for one or more shaders, placed under `/root/materials` (or a nested `namespace` below it), and it is connected to geometry only by the **`materialAssign`** attribute, which an **implicit resolver** acts on at render time by copying the material to the geometry's location. The page distinguishes three operations that are easy to conflate: **edit** (change the material itself, one at a time), **override** (a geometry-specific change stored on the **`materialOverride`** attribute, and you can override many at once), and **assign**. It also covers the pipeline-relevant details — a single material location may hold shaders from **multiple renderers**, with only the relevant ones selected at render time; **MaterialResolve** forces resolution earlier in the recipe; and **face sets** (via **FaceSetCreate**) break a mesh into named face lists so different materials can be assigned to parts of one asset.

### Key Steps
1. **Create the location:** add a **Material** node — usually in its own branch, joined back with a **Merge** — and press **`Alt`+`E`** to make it editable in the Parameters tab.
2. Set **`name`** (used for both the node name and the scene graph location; Katana handles clashes gracefully but naming is good practice) and **`namespace`** to place it below `/root/materials/<namespace>`. Nested namespaces work — `geo/metals` yields `/root/materials/geo/metals`.
3. **Attach shaders:** click **Add shader**, choose a shader *type* (the list depends on installed renderers), then pick the shader from the list or via **Browse…** in the Shader Browser. Expand to set non-default parameters.
4. Repeat for additional shaders — a surface plus a displacement shader is the page's example. **Shaders from several renderers can coexist** on one material location.
5. **Edit later** with a second Material node downstream: set **`action`** to `edit material` and point **`location`** at the material to change.
6. **Override per-geometry** instead: set **`action`** to `override materials`, put the geometry locations in the **CEL** parameter, then middle-click-drag the attribute to override onto the **Drop Attributes Here** hotspot in the `attrs` grouping. Changes are written under **`materialOverride`** on the CEL-matched locations. You can override many materials at once, but edit only one.
7. **Assign:** add a **MaterialAssign** node downstream of both the geometry and the material, set its **CEL** to the target locations and **`materialAssign`** to the material location. 💡 The page's own tip: **`Shift`+middle-click-drag from the Material node into the `materialAssign` field** to create an expression link rather than a static path.
8. **Force early resolution** with a **MaterialResolve** node where materials should be resolved, instead of leaving it to the render-time implicit resolver.
9. **Split an asset by faces:** add **FaceSetCreate**, set **`meshLocation`** to the polymesh or subdivision surface and **`faceSetName`** to the name that will appear under it in the Scene Graph, then assign different materials to the resulting face sets.

### Nodes / Tools / Settings
- **Material** node — `name`, `namespace`, `action` (create / `edit material` / `override materials`), `location`, CEL, `attrs`; **`Alt`+`E`** to edit.
- **MaterialAssign** — CEL + `materialAssign`; **MaterialResolve** — forces early resolution; **MaterialStack** — many materials in one node; **Merge**; **FaceSetCreate** (`meshLocation`, `faceSetName`).
- Attributes: **`materialAssign`** (the link), **`materialOverride`** (where overrides are stored).
- `/root/materials` and nested namespaces; the Shader Browser; **implicit resolvers** at render time.
- ⚠️ Legacy as of Katana 3.2 — the current route is **NetworkMaterialCreate**.

### Difficulty
Intermediate

### Foundry App & Version
Katana 9.0, documenting a pre-3.2 workflow that is still supported and still defines the underlying model.

### Tags
`katana`, `lookdev`, `cel`, `scenegraph`, `katana-9`, `intermediate`

---

## Related Tutorials
- [Building Materials Using NetworkMaterialCreate](building-materials-using-networkmaterialcreate.md) — the workflow that supersedes this one.
- [Adding Multiple Materials](adding-multiple-materials.md) — MaterialStack, referenced here.
- [Using the Scene Graph](using-the-scene-graph.md) — implicit resolvers, which this page depends on.
- [GafferThree](gafferthree.md) — Template Materials and light linking on the lighting side.

---

> **Provenance.** `learn.foundry.com/katana` (MadCap Flare). Paths in this doc set
> are not guessable and `Data/Tocs/*` 404s, so this page was reached by crawling
> from `Content/learn_katana.html` → `user_guide.html`, or from a sibling page's
> own links. Reference-guide and user-guide pages carry clean `<title>`s and need
> no `--title` override, unlike `learn.foundry.com/nuke/developers/**`.
