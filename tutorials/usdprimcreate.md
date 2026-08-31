---
title: UsdPrimCreate
source: Article
url: https://learn.foundry.com/katana/Content/rg/usd_nodes/usdprimcreate.html
author: learn.foundry.com
ingested: 2026-08-31
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
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
