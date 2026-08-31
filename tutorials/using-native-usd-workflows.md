---
title: Using Native USD Workflows
source: Article
url: https://learn.foundry.com/katana/Content/ug/usd/native-usd-workflows.html
author: learn.foundry.com
ingested: 2026-08-31
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
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
