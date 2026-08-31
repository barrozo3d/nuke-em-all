---
title: UsdPrimCreate
source: Article
url: https://learn.foundry.com/katana/Content/rg/usd_nodes/usdprimcreate.html
author: learn.foundry.com
ingested: 2026-08-31
app: Katana
version: 9.0v3
tags: [katana, usd, scenegraph, nodegraph, katana-9, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/usdprimcreate/
frame_count: 0
frame_status: skipped
---

# UsdPrimCreate

**Source:** [Article](https://learn.foundry.com/katana/Content/rg/usd_nodes/usdprimcreate.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** UsdPrimCreate In USD, a prim (short for primitive) is the fundamental building block of a scene. A prim represents a single element in the scene graph hierarchy and describes various types of entities and structures. Examples include points, cubes, materials, meshes, and xforms. The hierarchical locations of prims can be used to structure your scene before importing components into the prims. Note: This node is the USD equivalent of Katana’s PrimitiveCreate node. UsdPrimCreate creates a prim defined by the type , which is selected from a list of available USD prim types. The primSpec specifier determines how the prim is treated during composition and has the following options: define - create the primitive in the scene. over - a prim that is used only to override opinions that exist in the scene. class - for defining default attributes using a class template. By default, only the final, composed prim receives the new primitive using the primSpec specifier, with all others in the prim hierarchy affected using “over”. This is to avoid overwriting the PrimSpecs in lower layers that go to compose the final prim. However, if you want to use the same specifier throughout the prim hierarchy, check primSpecHierarchy . Katana interrogates the USD version in use to obtain a complete list of prim types to populate the type dropdown. Once a type is selected, Katana then obtains all the properties for that prim type and populates the properties for further customization. Note: For more information on prims, see Native USD Prims in the user guide, and Pixar's USD Glossary . Tip: To create simple geometry, it may be easier to use the UsdCapsuleCreate , UsdConeCreate , UsdCubeCreate , UsdCylinderCreate , UsdPlaneCreate , UsdSphereCreate , or UsdVolumeCreate nodes (which are derived from UsdPrimCreate), as this skips the step of needing to choose the prim type . It creates the geometry and shows the relevant geometry's properties immediately on adding it to your node graph. Note: There are also more specific nodes, such as UsdLight , UsdCamera , UsdScope and UsdXform nodes, which allow you to create different types of prims directly. Inputs Connection Type Connection Name Function Input in The incoming scene graph data that the node will operate on or modify. Controls Control (UI) Default Value Function primPaths none Specify locations where prims are to be created, such as /geo. Prims are generated at each specified path, in the order listed. primSpec define Choose the specifier for the prim. This is the role or function of the prim in the scene description. • define - defines a new, complete specification for a prim and its properties within a layer. • class - defines a prim meant to act as a template for other prims. It ensures uniformity and reusability throughout the scene by allowing other prims to adopt or specialize it, inheriting its characteristics. • over - indicates that the prim is an override. It's used to non-destructively modify prims defined in lower-priority layers. A prim with an "over" specifier is meant to modify or extend the properties or hierarchy of existing prims, without redefining them entirely. For more information, refer to the USD Glossary under specifier . type none Choose the type of prim to create at the position hierarchy defined by primPath . primSpecHierarchy off If checked, create all prims in the primPaths hierarchy using the primSpec . If unchecked, all prims except the last one, will apply the primSpec in an "over" manner to avoid primSpecs in lower-order layers being overwritten. properties n/a A dynamically generated list of properties and settings for the selected prim type . Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
Creating USD prims with **`UsdPrimCreate`** — choosing the prim `type` from whatever the installed USD version offers, and choosing the **`primSpec` specifier** that decides whether the prim defines, templates or overrides what already exists in the composed scene.

### Summary
A prim is USD's fundamental building block — one element of the scene graph hierarchy, from points and cubes to materials, meshes and xforms — and `UsdPrimCreate` is the node that makes one, described by the page as **the USD equivalent of Katana's `PrimitiveCreate`**. Its `type` dropdown is not a fixed list: Katana interrogates the USD version in use for the available prim types, then populates the node's properties from the selected type. The subtle control is `primSpecHierarchy`: by default only the **final** prim in a path gets the chosen specifier and every ancestor is created as an `over`, specifically so that PrimSpecs in lower layers are not overwritten.

### Key Steps
1. Wire the incoming scene into the node's `in` input — the scene graph data the node operates on.
2. Set **`primPaths`** to the locations where prims should be created (e.g. `/geo`). **Prims are generated at each path, in the order listed.**
3. Choose **`type`** from the dropdown, which Katana populates by interrogating the USD version in use.
4. Let Katana fill in **`properties`** — the list is generated dynamically from the selected prim type.
5. Choose the **`primSpec`** specifier — `define`, `class` or `over` — according to whether you are creating, templating or overriding.
6. Leave **`primSpecHierarchy` off** unless you specifically want the specifier applied to *every* prim in the path. Off means ancestors are created as `over`, protecting lower-layer PrimSpecs.
7. For simple geometry, **skip this node**: `UsdCubeCreate`, `UsdSphereCreate` and their siblings are derived from it, skip the type-choosing step, and show the relevant geometry properties immediately on being added.
8. For lights, cameras, scopes and transforms, use the dedicated `UsdLight`, `UsdCamera`, `UsdScope` and `UsdXform` nodes instead.

### Nodes / Tools / Settings
**Node:** `UsdPrimCreate` — creates a prim defined by `type`. ⚠️ **"This node is the USD equivalent of Katana's `PrimitiveCreate` node."**

**What a prim is (from the page):** "In USD, a prim (short for primitive) is the fundamental building block of a scene. A prim represents a single element in the scene graph hierarchy and describes various types of entities and structures." Examples given: points, cubes, materials, meshes, xforms. **Prim hierarchy locations can be used to structure a scene *before* importing components into the prims.**

**Input:** `in` — the incoming scene graph data the node operates on or modifies.

**Controls:**

| Control | Default | Function |
|---|---|---|
| `primPaths` | none | Locations where prims are created (e.g. `/geo`). **Generated at each path, in the order listed.** |
| `primSpec` | `define` | The prim's role in the scene description — see below. |
| `type` | none | The type of prim to create at the hierarchy position given by `primPath`. |
| `primSpecHierarchy` | off | Apply `primSpec` to **all** prims in the path, rather than only the last. |
| `properties` | n/a | **Dynamically generated** for the selected prim `type`. |

**The three `primSpec` specifiers:**
- **`define`** — "defines a new, complete specification for a prim and its properties within a layer." Creates the primitive in the scene.
- **`class`** — "defines a prim meant to act as a template for other prims," for uniformity and reusability: other prims adopt or specialize it and inherit its characteristics. Used for defining default attributes via a class template.
- **`over`** — "indicates that the prim is an override… used to **non-destructively** modify prims defined in lower-priority layers." It modifies or extends the properties or hierarchy of existing prims **without redefining them entirely**.

⚠️ **`primSpecHierarchy` is the one to understand.** By default **only the final, composed prim receives the new primitive using the chosen `primSpec`; every other prim in the hierarchy is created with `over`** — deliberately, "to avoid overwriting the PrimSpecs in lower layers that go to compose the final prim." Checking `primSpecHierarchy` applies the same specifier throughout the hierarchy, which is what overwrites them.

**The type list is derived, not authored.** "Katana interrogates the USD version in use to obtain a complete list of prim types to populate the `type` dropdown. Once a type is selected, Katana then obtains all the properties for that prim type and populates the properties for further customization." — the same live-from-USD behaviour `UsdSchemaSet` shows for API schemas.

**Derived and adjacent nodes:**
- **Derived from `UsdPrimCreate`, for simple geometry** (they skip the type-choosing step and show the geometry's properties immediately): `UsdCapsuleCreate`, `UsdConeCreate`, `UsdCubeCreate`, `UsdCylinderCreate`, `UsdPlaneCreate`, `UsdSphereCreate`, `UsdVolumeCreate`.
- **More specific nodes for other prim kinds:** `UsdLight`, `UsdCamera`, `UsdScope`, `UsdXform`.

**Referenced but not ingested:** *Native USD Prims* in the user guide, and Pixar's *USD Glossary* (including its entry on **specifier**).

### Difficulty
Intermediate

### Foundry App & Version
Katana 9.0v3 (page served from the current Katana 9.0v3 documentation set)

### Tags
katana, usd, scenegraph, nodegraph, katana-9, intermediate

---

## Scope note

This completes the `UsdPrimCreate` / `UsdSchemaSet` gap item, which
`KNOWLEDGE_GAPS_TODO.md` had carried as one line covering two nodes. The pair
divides cleanly: **`UsdPrimCreate` creates a prim of a type; `UsdSchemaSet`
applies an additional API schema to a prim that already exists.** Both derive
their UI from the installed USD version rather than from anything Foundry
hand-authored.

The seven derived geometry nodes and the four specific prim nodes are **named
here but not ingested individually** — the page's own guidance is that they are
`UsdPrimCreate` with the type pre-chosen, so they are recorded as covered by
this entry rather than listed as eleven separate gaps.

---

## Related Tutorials
- [UsdSchemaSet](usdschemaset.md) — shares `katana` + `usd` + `scenegraph`; **the other half of the pair.** This node creates a prim of a given type; that one applies an additional API schema to a prim that already exists — and its worked example builds its `DiskLight` and background `Plane` with exactly this node.
- [Using Native USD Workflows](using-native-usd-workflows.md) — shares `katana` + `usd` + `scenegraph` + `nodegraph`; the map that lists this node under **Prims** and describes the dynamic-UI behaviour documented here — properties "populated by the USD version used… defined within the USD API itself".
- [OpScript Tutorials](opscript-tutorials.md) — shares `katana` + `scenegraph` + `nodegraph`; OpScript's `Interface` API creates and deletes scene graph locations procedurally on the Katana side, the same authoring job this node does declaratively on the USD side.
- [Importing USD Data](importing-usd-data.md) — shares `katana` + `usd` + `scenegraph` + `nodegraph`; shows where this node sits in the import workflow — laying out a typed hierarchy first, then bringing components into those locations.
- [Composition Arcs - Understanding LIVRPS](composition-arcs---understanding-livrps.md) — shares `katana` + `usd` + `scenegraph`; the `primSpec` specifiers and the `primSpecHierarchy` default that protects lower-layer PrimSpecs are the node-level expression of that strength ordering.
