---
title: UsdSchemaSet
source: Article
url: https://learn.foundry.com/katana/Content/rg/usd_nodes/usdschemaset.html
author: learn.foundry.com
ingested: 2026-08-31
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/usdschemaset/
frame_count: 0
frame_status: skipped
---

# UsdSchemaSet

**Source:** [Article](https://learn.foundry.com/katana/Content/rg/usd_nodes/usdschemaset.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** UsdSchemaSet A USD schema is structured data that determines the role of a prim on the stage. Schemas provide a framework to define common types and are essentially the blueprint for specific objects or behaviors within the stage. The schema specifies attributes such as size, height, display color, and other characteristics that make up the object. Creating a prim of a certain type directly assigns a predefined schema, dictating its properties and behavior. The UsdSchemaSet node associates an additional type or category of behavior and data with a prim. By setting the schema in the node, you indicate that this specific prim should be handled using an additional defined set of attributes and behaviors particular to that schema. For example, you could use UsdSchemaSet to add shadow properties to a light giving it attributes that it normally wouldn’t have. With the UsdSchemaSet you are setting a schema using an API (like a MaterialBindingAPI or VisibilityAPI). API schemas ending in "API" are designed to be applied to prims to add supplementary capabilities or attributes to an existing prim non-destructively (without altering the original type of the prim). This flexibility allows artists and TD’s to create more complex and layered scene descriptions while maintaining a clear and efficient structure. There are many schemas available such as lights, shadows, render-specific attributes, and you also have the flexibility to create custom schemas to suit your specific needs. Example: Imagine you have a light in your 3D scene. By default, this light doesn't cast shadows. If you want it to, you can use the UsdSchemaSet to add a "ShadowAPI" schema, providing new attributes related to shadows. This way, without changing the original light, you add the ability for it to cast shadows in your scene, showcasing how schemas in USD let you flexibly add features to prims. In the UsdSchemaSet node, you can pick an API Schema from a list that automatically updates itself. This keeps the list current, even if new items are added after setting up Katana or with updated USD versions. This way, you always see the most up-to-date options available and can integrate schemas beyond Katana's original set. Note: For more information on USD schema see The USD Glossary . Video: Discover how you can use schemas to access various APIs parameters - Katana 8.0 | Access API parameters with USD schemas . Apply Schemas to a Prim You can apply multiple schemas to a prim. For example, if we take a diskLight created with UsdPrimCreate we can add a cone shaping by applying a schema. In the viewer monitor select display and untick default lighting . Create a plane using another UsdPrimCreate , specify the primPath (for example /bg) but this time set the type to Plane . This will be the background for the light to shine on. Without it the light would be invisible. Set the plane’s axis to Y under properties and increase length and width to 10 . Let’s now create a UsdPrimCreate node and in primPaths specify the path where your new diskLight prim will reside in the USD scene hierarchy. (For example /light) Set the type parameter to DiskLight . Increase the exposure property of the diskLight under properties inputs . For example, set it to 20 to enhance it’s visibility. You can then apply a ShapingAPI on top of the light using the UsdSchemaSet node. To do this follow these next steps: Create a UsdSchemaSet node, then drag and drop the diskLight prim path (in this example /light) from the Scene Explorer into primPaths using your middle mouse button. Change type to ShapingAPI . Then adjust the angle in properties inputs shaping cone and the focus in shaping to control the cone's opening and achieve your desired light shape. This now means that the diskLight, which already has properties like diffuse, color, intensity, exposure will also inherit all the attributes of the ShapingAPI, such as angle, softness, focus, and other ShapingAPI properties. The diskLight now has an enhanced set of properties, combining both its inherent attributes and those inherited from the ShapingAPI, enabling more nuanced control over its visual appearance and behavior in the scene. Controls Control (UI) Default Value Function primPaths none Specify locations where API Schemas are applied. Schemas are generated at each specified path, following the order in which they are listed. type none Choose the type of API Schema to create from the list. This list is updated in real-time. This ensures it includes newer schemas beyond Katana's original set, providing you with the latest options. listPosition prepend Specifies how the API Schema is added to the scene. Options are: append - integrates new schemas by positioning them at the end of the list, ensuring they are evaluated after existing values, and thereby, allowing them to potentially override preceding definitions. prepend - adds one or more schemas to the front of the list, causing them to be evaluated before, and potentially overridden by values added later or in subsequent layers. delete - removes one or more schemas from the list, preventing their properties from influencing the composed prim in the scene. reset to explicit - Ignoring all previously compiled schemas, this operation sets the list strictly to the defined value(s), providing a clear and explicit new starting point for schema evaluation. "list" specifically refers to the finalized list of all values and properties applicable to a prim, derived after evaluating all USD layers and compositional arcs. For more information, refer to the USD Glossary under List Editing . properties n/a A list of dynamically generated properties and settings depending on which type of API Schema type is selected. Can't find what you're looking for? Use our feedback widget on the right to request more information.



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
