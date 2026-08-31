---
title: Using Native USD Workflows
source: Article
url: https://learn.foundry.com/katana/Content/ug/usd/native-usd-workflows.html
author: learn.foundry.com
ingested: 2026-08-31
app: Katana
version: 9.0v3
tags: [katana, usd, scenegraph, nodegraph, katana-9, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/using-native-usd-workflows/
frame_count: 0
frame_status: skipped
---

# Using Native USD Workflows

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/usd/native-usd-workflows.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Using Native USD Workflows Using Native USD Workflows Nodes for Native USD Stage Creation and Manipulation Scene Explorer USD Properties Viewable in the Attributes Tab Nodes for Native USD Stage Creation and Manipulation We introduced new nodes coupled with an underlying framework that allows for native USD manipulation. Composition • UsdInheritSet • UsdPayloadSet • UsdReferenceSet • UsdSpecializeSet • UsdSubLayerAdd Prims • UsdCamera • UsdMaterial • UsdLight • UsdPrimCreate • UsdSchemaSet • UsdScope • UsdXform • UsdCapsuleCreate • UsdConeCreate • UsdCubeCreate • UsdCylinderCreate • UsdPlaneCreate • UsdSphereCreate • UsdVolumeCreate Properties • UsdActiveSet • UsdAttributeSet • UsdCollection • UsdMaterialAssign • UsdMetadataSet • UsdKindSet • UsdPrimvarSet • UsdRelationshipSet • UsdStageDefine • UsdTransformSet • UsdTransformEdit • UsdVariantSet Output • UsdLayerDefine • UsdLayerExport • UsdLayerExportGroup Other • UsdLayerWrite • UsdPythonWrite • KatanaToUsd • UsdToKatana SuperTools • UsdGaffer • UsdSuperLayer Note: A full set of links to the reference guide topics for each node can be found in USD Nodes . The nodes are classified according to the following types: Composition - New nodes for scene composition are determined by LIVRPS ordering. These are guidelines ordered by Local, Inherits, VariantSets, References, Payload, and Specializes that determine how pieces of a 3D scene work together effectively. For example, UsdSubLayerAdd to add a layer to the stage. See Composition Arcs - Understanding LIVRPS and Importing USD Data for more information about this. See USD Nodes: Composition for links to the reference guide topics. Note: In Katana 7, VariantSets are not included for authoring but you can change which variant is used via the UsdVariantSet node. Prims - The following nodes to let you create and modify schemas. UsdPrimCreate for prim generation and overriding, and UsdSchemaSet to assign a schema API to a prim. For both nodes, Katana speeds up the workflow by tailoring the UI to the selected prim or schema type automatically. Simply select a type, and the node properties are dynamically populated by the USD version used, with its parameters defined within the USD API itself. See Native USD Prims . A cube type with matching parameters generated dynamically. Additionally, there are more specialised nodes, such as UsdCamera , UsdScope and UsdXform nodes, based on the UsdPrimCreate but with parameter tailored for each purpose, allowing you to create different types of prims easily. For cameras, see Creating Native USD Cameras . For creating or editing lights, you can use UsdGaffer or UsdLight . See Lighting USD Scenes . For creating or editing materials, you can use UsdMaterial . See Materials in USD Scenes . See USD Nodes: Prims for links to the reference guide topics. Properties - New nodes for essential stage modifications. For example, UsdTransformSet and UsdTransformEdit to apply a transform to a prim, and to enable viewer manipulators for native USD. See Native USD Transformations . USD’s Pattern-Based Collections (PBC) is also integrated into Katana. Similar to Katana’s CEL, the PBC widget and UsdCollection node allows you to use, define and modify USD collections, helping make workflows more efficient. See Pattern-Based Collections with USD . For more about assigning materials in USD, see UsdMaterialAssign Workflows . See USD Nodes: Properties for links to the reference guide topics. Output - You can now use UsdLayerExport and UsdLayerDefine to bake native USD layers. See Native USD Layer Export . See USD Nodes: Output for links to the reference guide topics. Other - We’ve added a UsdLayerWrite node so that you can take or create a scene description stored as .usda, edit it, and manually write it to the stage. This is useful when you need to quickly add content to locations in the scene. Plus, UsdPythonWrite gives you the power of Python to author USD layers and to easily prototype inside of Katana. To make workflows more flexible, UsdToKatana and KatanaToUsd let you convert USD data into Katana data, and vice versa. You also can use USD Text View to view .usda data based on the selected node, helping with debugging. SuperTools - Katana’s UsdSuperLayer and UsdGaffer let you create multiple prims inside one USD layer, helping your scene management and performance. See UsdSuperLayer Framework to learn about the system, and see Using UsdGaffer for to learn how to make use of this for lighting. Scene Explorer The Scene Explorer tab provides a unified scene graph view of both USD and Katana data so that you can easily traverse and manipulate the hierarchical structure of the entire asset library. For more information see Using the Scene Explorer . USD Properties Viewable in the Attributes Tab We’ve integrated USD property inspection into the Attributes tab, making it easy to check the attributes, relationships and metadata for prims and properties in the scene. Just click on a prim in the Scene Explorer to see the data in the Attributes tab. See Inspecting USD Properties Using the Attributes Tab . Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
Assembling and editing a USD scene **natively** in Katana — the node families that create, compose, modify and export USD stages without round-tripping through Katana's own scene graph, plus the Scene Explorer and Attributes tab that make the result inspectable.

### Summary
Katana ships a set of native USD nodes over an underlying framework for direct USD manipulation, grouped into Composition, Prims, Properties, Output, Other and SuperTools. Composition follows **LIVRPS** ordering (Local, Inherits, VariantSets, References, Payload, Specializes), and the prim nodes are notable for building their own UI: pick a type on `UsdPrimCreate` or a schema API on `UsdSchemaSet` and the parameters are **populated dynamically from the USD version in use**, defined by the USD API itself rather than hand-authored by Foundry. The **Scene Explorer** then presents USD and Katana data in one unified scene graph, and the **Attributes tab** exposes a prim's attributes, relationships and metadata.

### Key Steps
1. Compose the stage with the **Composition** nodes — `UsdSubLayerAdd` to add a layer, plus `UsdInheritSet`, `UsdPayloadSet`, `UsdReferenceSet` and `UsdSpecializeSet` — ordered by **LIVRPS**.
2. Create prims with **`UsdPrimCreate`** (generation and overriding) and assign a schema API with **`UsdSchemaSet`**. Select the type and the node's properties populate themselves from the USD version in use.
3. Reach for the tailored variants where they fit rather than the generic node: `UsdCamera`, `UsdScope`, `UsdXform` are `UsdPrimCreate` with purpose-built parameters, and `UsdCapsuleCreate` / `UsdConeCreate` / `UsdCubeCreate` / `UsdCylinderCreate` / `UsdPlaneCreate` / `UsdSphereCreate` / `UsdVolumeCreate` cover the primitives.
4. Light with **`UsdGaffer`** or **`UsdLight`**, and author materials with **`UsdMaterial`**, assigning them via **`UsdMaterialAssign`**.
5. Modify the stage with the **Properties** nodes — `UsdTransformSet` and `UsdTransformEdit` for transforms (the latter enabling **viewer manipulators for native USD**), plus `UsdActiveSet`, `UsdAttributeSet`, `UsdMetadataSet`, `UsdKindSet`, `UsdPrimvarSet`, `UsdRelationshipSet`, `UsdStageDefine` and `UsdVariantSet`.
6. Select sets of prims with **Pattern-Based Collections (PBC)** — the PBC widget and the `UsdCollection` node, which the page describes as **similar to Katana's CEL**.
7. Bake layers out with **`UsdLayerExport`** and **`UsdLayerDefine`** (and `UsdLayerExportGroup`).
8. Drop to text or Python when it is faster: **`UsdLayerWrite`** takes or creates a `.usda` scene description, lets you edit it and write it manually to the stage; **`UsdPythonWrite`** authors USD layers in Python for prototyping inside Katana.
9. Cross the boundary with **`UsdToKatana`** and **`KatanaToUsd`** when data needs to move between the two representations.
10. Inspect and debug: the **Scene Explorer** gives one unified scene graph over USD *and* Katana data; clicking a prim there shows its attributes, relationships and metadata in the **Attributes tab**; and **USD Text View** shows the `.usda` for the selected node.

### Nodes / Tools / Settings
**The native USD node set, by category** (a full set of reference-guide links is in *USD Nodes*):

| Category | Nodes |
|---|---|
| **Composition** | `UsdInheritSet` · `UsdPayloadSet` · `UsdReferenceSet` · `UsdSpecializeSet` · `UsdSubLayerAdd` |
| **Prims** | `UsdCamera` · `UsdMaterial` · `UsdLight` · `UsdPrimCreate` · `UsdSchemaSet` · `UsdScope` · `UsdXform` · `UsdCapsuleCreate` · `UsdConeCreate` · `UsdCubeCreate` · `UsdCylinderCreate` · `UsdPlaneCreate` · `UsdSphereCreate` · `UsdVolumeCreate` |
| **Properties** | `UsdActiveSet` · `UsdAttributeSet` · `UsdCollection` · `UsdMaterialAssign` · `UsdMetadataSet` · `UsdKindSet` · `UsdPrimvarSet` · `UsdRelationshipSet` · `UsdStageDefine` · `UsdTransformSet` · `UsdTransformEdit` · `UsdVariantSet` |
| **Output** | `UsdLayerDefine` · `UsdLayerExport` · `UsdLayerExportGroup` |
| **Other** | `UsdLayerWrite` · `UsdPythonWrite` · `KatanaToUsd` · `UsdToKatana` |
| **SuperTools** | `UsdGaffer` · `UsdSuperLayer` |

**Composition — LIVRPS.** Composition node ordering is determined by **LIVRPS**: **L**ocal, **I**nherits, **V**ariantSets, **R**eferences, **P**ayload, **S**pecializes — "guidelines … that determine how pieces of a 3D scene work together effectively."
⚠️ **Version note carried from the page:** *"In Katana 7, VariantSets are not included for authoring, but you can change which variant is used via the `UsdVariantSet` node."*

**Prims — the dynamic UI is the point.** `UsdPrimCreate` handles prim generation *and overriding*; `UsdSchemaSet` assigns a schema API to a prim. For both, **Katana tailors the UI to the selected prim or schema type automatically** — select a type and the node properties are **dynamically populated by the USD version used, with parameters defined within the USD API itself**. (The page's example: a cube type with matching parameters generated dynamically.) `UsdCamera`, `UsdScope` and `UsdXform` are built on `UsdPrimCreate` with parameters tailored per purpose.

**Properties — Pattern-Based Collections.** USD's **PBC** is integrated into Katana: the **PBC widget** and the **`UsdCollection`** node let you use, define and modify USD collections. The page positions it explicitly as **"similar to Katana's CEL."**

**Other — the escape hatches.** `UsdLayerWrite` takes or creates a scene description stored as **`.usda`**, lets it be edited and written manually to the stage — "useful when you need to quickly add content to locations in the scene." `UsdPythonWrite` gives **Python authoring of USD layers** for prototyping inside Katana. `UsdToKatana` / `KatanaToUsd` convert between USD and Katana data in both directions. **USD Text View** displays `.usda` data for the selected node, for debugging.

**SuperTools.** `UsdSuperLayer` and `UsdGaffer` **create multiple prims inside one USD layer**, for scene management and performance.

**Scene Explorer.** A **unified scene graph view of both USD and Katana data**, for traversing and manipulating the whole asset library's hierarchy.

**Attributes tab.** USD property inspection is integrated: click a prim in the Scene Explorer to see its **attributes, relationships and metadata**.

**Referenced pages (not ingested):** *Composition Arcs — Understanding LIVRPS*, *Importing USD Data*, *Native USD Prims*, *Creating Native USD Cameras*, *Lighting USD Scenes*, *Materials in USD Scenes*, *Native USD Transformations*, *Pattern-Based Collections with USD*, *UsdMaterialAssign Workflows*, *Native USD Layer Export*, *UsdSuperLayer Framework*, *Using UsdGaffer*, *Using the Scene Explorer*, *Inspecting USD Properties Using the Attributes Tab*, and *USD Nodes*.

### Difficulty
Intermediate

### Foundry App & Version
Katana 9.0v3 (page served from the current Katana 9.0v3 documentation set). ⚠️ The page itself carries a **Katana 7** caveat about VariantSet authoring, quoted above and not generalised to 9.0v3 — it is recorded as the page states it.

### Tags
katana, usd, scenegraph, nodegraph, katana-9, intermediate

---

## Scope note — an orientation page, and the map it provides

This is the **orientation page for native USD in Katana**: it names the whole node
set and says what each family is for, then defers the detail to fourteen other
pages. It is the map, not the territory — but it is the map that was missing, and
it is what makes the individual USD node references worth ingesting next.

⚠️ **It was reached by correction.** `KNOWLEDGE_GAPS_TODO.md` originally recorded
`ug/usd/building_usd_scenes.html` as the "USD scene assembly" target; that page is
**1,234 characters** and carries none of this. Measuring the whole USD area found
this page at **5,361**. Both facts are now in that file.

Still open in this bullet, with measured sizes: `rg/usd_nodes/usdschemaset.html`
(5,996), `rg/usd_nodes/usdprimcreate.html` (3,914),
`ug/usd/importing_usd_data.html` (3,282), and
`ug/using_hydra_viewer/usd_load_plugins.html` (2,041). The Hydra Viewer page
itself is a **1,025-char stub**.

---

## Related Tutorials
- [Setting up UsdPreviewSurface Materials](setting-up-usdpreviewsurface-materials.md) — shares `katana` + `usd` + `nodegraph`; that page is one concrete instance of this map — the `UsdMaterial` / `UsdMaterialAssign` route named here, worked through end to end for a UsdPreviewSurface.
- [GafferThree](gafferthree.md) — shares `katana` + `scenegraph` + `katana-9`; **`UsdGaffer` is the USD-native counterpart of the GafferThree lighting node**, listed here under SuperTools, so the two pages describe the same job in Katana's two scene representations.
- [OpScript Tutorials](opscript-tutorials.md) — shares `katana` + `scenegraph` + `nodegraph`; this page positions USD's **Pattern-Based Collections as "similar to Katana's CEL"**, and CEL is exactly what scopes an OpScript — the same selection problem solved twice, once per representation.
- [NetworkMaterialCreate](networkmaterialcreate.md) — shares `katana` + `nodegraph` + `katana-9`; materials in the native USD path go through `UsdMaterial` rather than NetworkMaterialCreate, so the two are the parallel material-authoring routes this map distinguishes.
