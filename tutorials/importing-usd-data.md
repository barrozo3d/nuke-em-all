---
title: Importing USD Data
source: Article
url: https://learn.foundry.com/katana/Content/ug/usd/importing_usd_data.html
author: learn.foundry.com
ingested: 2026-08-31
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/importing-usd-data/
frame_count: 0
frame_status: skipped
---

# Importing USD Data

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/usd/importing_usd_data.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Importing USD Data Importing USD Data Native USD workflows do not convert the data to Katana locations and attributes, so the data can be manipulated with native USD nodes inside Katana. This brings a lot of benefits in terms of speed and interoperability. Note: You still have the option to bring data across to Katana using UsdToKatana conversion nodes if needed. There are various ways of bringing in USD data natively. You can bring in entire USD stages using the UsdSubLayerAdd node, or build your stage inside Katana using the various composition arcs below: UsdPrimCreate - Used to create hierarchy locations of various types eg. point, cube, material, xform, etc. These can be used to define a scene hierarchy before bringing in components to the locations. This node is dynamic, so the prim type dropdown will update with prim options from the version of USD being used and parameters will be created automatically by querying the USD. UsdSubLayerAdd - A layer is one of the fundamental building blocks of the USD stage. Subsequent layers can define new prims or override prims that were already on the stage. A Layer is a single USD (usda, usd, usdc, usdz) file saved to disk. Sublayers are used to create LayerStacks, which are just as they sound - stacks of layers. They can be used to load layers to the root level without defining a prim path, this can be useful for bringing in complete stages, or layering various prims with the same hierarchy. UsdPayloadSet - Used for loading payloads to the scene. Any data can be brought in as a payload, a common use would be an asset with no animation or transformations, for example, a t-pose character. The look and animation/layout would then be referenced on top. They can also be used to bring in large FX or particularly heavy elements because prims brought in through Payloads have the added benefit of being chosen to be loaded or not through the Payload working set. Payloads which aren’t loaded are still visible in renders - same principle as deferred loading. UsdReferenceSet - Used to make overrides to certain properties of a prim, for example, overriding a t-pose character’s transforms to the animated transforms. UsdInheritSet - For inheriting hierarchy and Properties from one prim to another. If the prim being inherited from is updated, all prims inheriting it will also be updated. Useful for multiple instances of a prim as you’ll only need to make updates once. UsdSpecializeSet - Similar to inheritance where you can create a specialized prim from another prim. The difference being the overrides on the specialized prim level will always be stronger than any further references. This can be useful for ensuring certain aspects are never overridden. Note: To learn about the composition arcs, see Composition Arcs - Understanding LIVRPS . For more information and examples, see OpenUSD's USD Glossary . Tip: To see example scenes and varying examples of how assets are brought in, you can look at the example projects at Help Example Projects Native USD . Can't find what you're looking for? Use our feedback widget on the right to request more information.



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
