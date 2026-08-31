---
title: Importing USD Data
source: Article
url: https://learn.foundry.com/katana/Content/ug/usd/importing_usd_data.html
author: learn.foundry.com
ingested: 2026-08-31
app: Katana
version: 9.0v3
tags: [katana, usd, scenegraph, nodegraph, katana-9, intermediate]
extraction_status: complete
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
Bringing USD data into Katana **natively** — without converting it to Katana locations and attributes — either by loading whole stages with `UsdSubLayerAdd` or by assembling one in-scene from the five composition-arc nodes.

### Summary
Native USD workflows leave the data as USD, so it can be manipulated by the native USD nodes inside Katana, which the page frames as a speed and interoperability win; `UsdToKatana` conversion remains available when Katana-side data is actually needed. From there the page is a decision guide across the composition arcs: `UsdSubLayerAdd` for whole stages and LayerStacks, `UsdPayloadSet` for deferred-loadable heavy or animation-free assets, `UsdReferenceSet` for property overrides, `UsdInheritSet` for propagate-once updates across many instances, and `UsdSpecializeSet` for overrides that must never be overridden downstream.

### Key Steps
1. Decide first whether the data should stay native. **Native USD does not convert to Katana locations and attributes**, which is where the speed and interoperability come from — `UsdToKatana` is there if conversion is genuinely needed.
2. To bring in a **complete stage**, use **`UsdSubLayerAdd`** — it loads layers at the root level without defining a prim path.
3. To **build a hierarchy first**, use **`UsdPrimCreate`** to create typed locations (point, cube, material, xform…) and then bring components into them.
4. For assets that are heavy, or that carry no animation or transformations (the page's example is a **t-pose character**), bring them in with **`UsdPayloadSet`**, then reference look and animation on top.
5. Use the **Payload working set** to choose whether payloads load. ⚠️ **Payloads that are not loaded are still visible in renders** — the same principle as deferred loading.
6. Override specific properties of a prim with **`UsdReferenceSet`** — e.g. replacing that t-pose character's transforms with animated ones.
7. Where many instances should track one source, use **`UsdInheritSet`**: update the inherited-from prim once and every inheriting prim updates.
8. Where an aspect must never be overridden further downstream, use **`UsdSpecializeSet`** — overrides at the specialized level are **always stronger than any further references**.
9. Consult **Help → Example Projects → Native USD** for worked scenes showing how assets are brought in.

### Nodes / Tools / Settings
**The premise:** "Native USD workflows do not convert the data to Katana locations and attributes, so the data can be manipulated with native USD nodes inside Katana. This brings a lot of benefits in terms of speed and interoperability." Conversion via **`UsdToKatana`** remains an option.

| Node | What it is for |
|---|---|
| `UsdPrimCreate` | Create hierarchy locations of various types (point, cube, material, xform…) to define a scene hierarchy **before** bringing components into those locations. **Dynamic** — the prim-type dropdown updates from the USD version in use and parameters are created by querying USD. |
| `UsdSubLayerAdd` | Add layers. **A layer is a single USD file on disk (`usda`, `usd`, `usdc`, `usdz`)** and one of the fundamental building blocks of the stage. Subsequent layers define new prims or override existing ones. Sublayers build **LayerStacks** — stacks of layers — and load at root level **without defining a prim path**, useful for complete stages or for layering prims that share a hierarchy. |
| `UsdPayloadSet` | Load payloads. Typical use is an asset with **no animation or transformations** (a t-pose character), with look and animation/layout referenced on top. Also for large FX or heavy elements, because payloaded prims can be **chosen to load or not** via the **Payload working set**. |
| `UsdReferenceSet` | Override certain properties of a prim — e.g. overriding a t-pose character's transforms with animated transforms. |
| `UsdInheritSet` | Inherit hierarchy and properties from one prim to another. **Update the source and every inheriting prim updates** — useful across many instances, since the edit is made once. |
| `UsdSpecializeSet` | Create a specialized prim from another. The difference from inheritance: **overrides at the specialized level are always stronger than any further references**, so it is the tool for guaranteeing an aspect is never overridden. |

⚠️ **The payload detail worth remembering:** *"Payloads which aren't loaded are still visible in renders — same principle as deferred loading."* Not loading a payload is a **working-set / interactivity** decision, not an exclusion from the render.

**`UsdInheritSet` vs `UsdSpecializeSet`** is the distinction the page is really drawing: both propagate from a source prim, but specialization wins against downstream references while inheritance does not.

**Referenced but not ingested:** *Composition Arcs — Understanding LIVRPS*, OpenUSD's *USD Glossary*, and the shipped example scenes at **Help → Example Projects → Native USD**.

### Difficulty
Intermediate

### Foundry App & Version
Katana 9.0v3 (page served from the current Katana 9.0v3 documentation set)

### Tags
katana, usd, scenegraph, nodegraph, katana-9, intermediate

---

## Scope note

This is the *choosing* half of native USD import — which arc to use and why. The
**mechanics** of LIVRPS ordering live in *Composition Arcs — Understanding
LIVRPS*, which is referenced here and by `using-native-usd-workflows.md` and is
**still not ingested**; it is the most-referenced uningested Katana page in the
library and is recorded as such in `KNOWLEDGE_GAPS_TODO.md`.

---

## Related Tutorials
- [Using Native USD Workflows](using-native-usd-workflows.md) — shares `katana` + `usd` + `scenegraph` + `nodegraph`; the map that lists these five arcs under **Composition** and names LIVRPS as their ordering — this page is the same set explained by *purpose* rather than by category.
- [UsdPrimCreate](usdprimcreate.md) — shares `katana` + `usd` + `scenegraph` + `nodegraph`; the node used here to lay out a hierarchy before components arrive, documented in full — including the `primSpec` specifiers that decide whether such a location defines or overrides.
- [UsdSchemaSet](usdschemaset.md) — shares `katana` + `usd` + `scenegraph`; once data is in natively, that node is how an existing prim gains extra capability non-destructively, the same "layer it on rather than redefine it" principle these composition arcs are built around.
