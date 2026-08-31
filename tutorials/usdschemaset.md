---
title: UsdSchemaSet
source: Article
url: https://learn.foundry.com/katana/Content/rg/usd_nodes/usdschemaset.html
author: learn.foundry.com
ingested: 2026-08-31
app: Katana
version: 9.0v3
tags: [katana, usd, scenegraph, lighting, katana-9, intermediate]
extraction_status: complete
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
Applying an **API schema** to an existing USD prim with **`UsdSchemaSet`** — adding a supplementary set of attributes and behaviours *non-destructively*, without changing the prim's original type.

### Summary
A USD schema is the blueprint that determines a prim's role on the stage: creating a prim of a given type already assigns it a predefined schema. `UsdSchemaSet` associates an *additional* one — an **API schema**, the kind whose name ends in `API` (`MaterialBindingAPI`, `VisibilityAPI`, `ShadowAPI`, `ShapingAPI`) — layering extra attributes onto a prim without altering what it is. The page's worked example turns a plain `DiskLight` into a cone-shaped light by applying `ShapingAPI` on top of it, and the node's `listPosition` control exposes the USD **list-editing** semantics that decide whether a schema is evaluated before or after everything else.

### Key Steps
*The page's worked example — shaping a light with `ShapingAPI`:*
1. In the viewer monitor, select **display** and **untick `default lighting`** so the scene's own light is what you see.
2. Create a background with a **`UsdPrimCreate`**: set `primPath` (e.g. `/bg`) and `type` to **`Plane`**. ⚠️ **Without it the light would be invisible** — there is nothing for it to shine on.
3. Under the plane's **properties**, set `axis` to **Y** and increase `length` and `width` to **10**.
4. Create a second **`UsdPrimCreate`**: set `primPaths` to where the light should live (e.g. `/light`) and `type` to **`DiskLight`**.
5. Raise the light's **`exposure`** under `properties → inputs` — the page uses **20** — to make it visible.
6. Create a **`UsdSchemaSet`** node and **middle-mouse drag the diskLight's prim path from the Scene Explorer into `primPaths`**.
7. Set `type` to **`ShapingAPI`**.
8. Shape the cone with `properties → inputs → shaping → cone → angle`, and `focus` under `shaping`.
9. The result: the diskLight keeps its own `diffuse`, `color`, `intensity` and `exposure` **and** inherits `angle`, `softness`, `focus` and the rest of ShapingAPI.
10. Where several schemas are involved, set **`listPosition`** to control evaluation order — `prepend` (default) is evaluated first and can be overridden later; `append` is evaluated last and can override what came before.

### Nodes / Tools / Settings
**Node:** `UsdSchemaSet` — associates an additional type or category of behaviour and data with a prim.

**What a schema is (from the page):** "structured data that determines the role of a prim on the stage… essentially the blueprint for specific objects or behaviors." It specifies attributes such as size, height and display colour. **Creating a prim of a certain type directly assigns a predefined schema.**

**API schemas — the non-destructive part.** Schemas **ending in `API`** are "designed to be applied to prims to add supplementary capabilities or attributes to an existing prim **non-destructively (without altering the original type of the prim)**." Named examples: `MaterialBindingAPI`, `VisibilityAPI`, `ShadowAPI`, `ShapingAPI`. Many exist — lights, shadows, render-specific attributes — and **custom schemas can be created**.

**The page's other example:** a light that does not cast shadows by default gains shadow attributes by applying `ShadowAPI` — new capability, original light untouched.

**Controls:**

| Control | Default | Function |
|---|---|---|
| `primPaths` | none | Locations where API schemas are applied. **Schemas are generated at each specified path, in the order listed.** |
| `type` | none | The API schema to create. **The list updates in real time**, so it includes schemas newer than Katana's original set. |
| `listPosition` | `prepend` | How the schema enters the list — see below. |
| `properties` | n/a | **Dynamically generated** from whichever API schema `type` is selected. |

**`listPosition` — USD list editing:**
- **`append`** — positions new schemas at the **end** of the list, so they are evaluated **after** existing values and can potentially **override preceding definitions**.
- **`prepend`** (default) — adds to the **front**, so they are evaluated **before**, and can potentially be **overridden by values added later or in subsequent layers**.
- **`delete`** — removes one or more schemas from the list, preventing their properties from influencing the composed prim.
- **`reset to explicit`** — ignores all previously compiled schemas and sets the list strictly to the defined values, "providing a clear and explicit new starting point for schema evaluation."

⚠️ **"List" has a specific meaning here**, quoted from the page: *the finalized list of all values and properties applicable to a prim, derived after evaluating all USD layers and compositional arcs* — i.e. the composed result, not the node's own parameter. See the USD Glossary under *List Editing*.

**The real-time schema list is worth noting on its own:** because `type` refreshes itself, the node picks up schemas added after Katana was set up or introduced by a newer USD version — coverage is not frozen at install time.

**Referenced but not ingested:** *The USD Glossary* (schemas, and *List Editing*), and a Foundry video, *Katana 8.0 | Access API parameters with USD schemas*.

### Difficulty
Intermediate

### Foundry App & Version
Katana 9.0v3 (page served from the current Katana 9.0v3 documentation set). The page references a **Katana 8.0** video for the same feature; recorded as stated, not generalised.

### Tags
katana, usd, scenegraph, lighting, katana-9, intermediate

---

## Scope note

This is one half of the `UsdPrimCreate` / `UsdSchemaSet` gap item. **`UsdPrimCreate`
is not ingested** (`rg/usd_nodes/usdprimcreate.html`, 3,914 chars) — it appears
here only as the node that creates the prims the example then applies a schema to,
and it is recorded as still open in `KNOWLEDGE_GAPS_TODO.md`.

The `listPosition` semantics are USD list editing, not a Katana invention; the page
defers to the USD Glossary for the full model, and that glossary is not ingested
either.

---

## Related Tutorials
- [Using Native USD Workflows](using-native-usd-workflows.md) — shares `katana` + `usd` + `scenegraph`; the map that lists `UsdSchemaSet` under **Prims** and describes exactly the behaviour documented here — parameters *"dynamically populated by the USD version used, with its parameters defined within the USD API itself"*, which is the real-time `type` list and the generated `properties` seen on this node.
- [GafferThree](gafferthree.md) — shares `katana` + `lighting` + `scenegraph`; **the same job in the other scene representation.** GafferThree shapes lights from its object table with constraints and linking; here a plain `DiskLight` gains cone `angle`, `softness` and `focus` by applying `ShapingAPI` on top of it.
- [Setting up UsdPreviewSurface Materials](setting-up-usdpreviewsurface-materials.md) — shares `katana` + `usd` + `katana-9`; `MaterialBindingAPI` is named here as an API schema, and that page is the material-assignment workflow such a binding expresses in the native USD path.
- [UsdPrimCreate](usdprimcreate.md) — shares `katana` + `usd` + `scenegraph`; **the other half of the pair** — it creates a prim of a given type, where this node applies an additional API schema to one that already exists. The `DiskLight` and background `Plane` in the example above are both built with it.
