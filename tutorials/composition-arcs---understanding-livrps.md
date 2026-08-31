---
title: Composition Arcs - Understanding LIVRPS
source: Article
url: https://learn.foundry.com/katana/Content/ug/usd/composition_arcs_livrps.html
author: learn.foundry.com
ingested: 2026-08-31
app: Katana
version: 9.0v3
tags: [katana, usd, scenegraph, katana-9, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/composition-arcs---understanding-livrps/
frame_count: 0
frame_status: skipped
---

# Composition Arcs - Understanding LIVRPS

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/usd/composition_arcs_livrps.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Composition Arcs - Understanding LIVRPS Composition Arcs - Understanding LIVRPS Understanding the composition rules Layer Types In order to put together a scene, you will need to use different types of layers. When working with USD, there is a set of rules defining which layers override others. Understanding and composing this hierarchy is key to building a scene. There are six types of layers in USD. Layers that are “higher on the list” have stronger opinions than those lower down. Understanding the composition rules Get to grips with USD layers and composition arcs in this video exercise. Using simple cube prims, learn how to compose scenes in Katana with multiple layer types and see LIVRPS in action. Tip: This project can be opened directly from Katana from Help Example Projects Native USD which you can use to follow along with the exercise or quiz yourself. Layer Types Local Local describes a layer that is made locally. This means that any further changes made after you’ve composed your stage, will be stored as local value. They contain opinions on properties (e.g. cube size, colour etc.) and will override others. Inherits Inherits will take on the properties and hierarchy defined in the prim they’re inheriting from. This will remain “live” and therefore will always reflect updates on its “base”, as long as no further local overrides are made. Variants Prims can have variants, which are groups of properties that you can switch between. References References enable the reuse and assembly of content by incorporating the contents of one layer into another. References can be versioned, and allow local changes to be made, without impacting the original file. Payloads Payloads are similar to references. A heavy or complex layer could be brought in as a payload in order to avoid processing and improve performance. Specializes A specialize acts as the baseline values and is overridden by higher layers and arcs. Note: For more information, see LIVRPS Strength Ordering in OpenUSD's USD Glossary. Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
**LIVRPS** — the six USD layer types in strength order, and the rule that decides which layer's opinion wins when several describe the same property.

### Summary
Composing a USD scene means stacking layers, and USD defines a fixed order deciding which ones override which. The six types are **Local, Inherits, Variants, References, Payloads, Specializes** — **layers higher on that list have stronger opinions than those lower down**. Local edits sit at the top and win; Specializes sits at the bottom and acts as a baseline that everything above can override. The page pairs the list with a video exercise built on simple cube prims, and the project ships with Katana under **Help → Example Projects → Native USD**.

### Key Steps
1. Recognise that composing the layer hierarchy **is** scene building in USD — "understanding and composing this hierarchy is key to building a scene."
2. Read the order as a strength ranking: **L**ocal, **I**nherits, **V**ariants, **R**eferences, **P**ayloads, **S**pecializes — **higher on the list wins**.
3. Expect anything you change after composing the stage to be stored as a **Local** opinion, which therefore overrides what is beneath it.
4. Use **Inherits** where a prim should stay *live* against a base — it keeps reflecting updates to that base **as long as no further local overrides are made**.
5. Use **Variants** where a prim needs switchable groups of properties.
6. Use **References** to assemble and reuse content — they can be **versioned**, and local changes can be made **without impacting the original file**.
7. Use **Payloads** for a heavy or complex layer, to avoid processing it and improve performance.
8. Use **Specializes** for baseline values you expect higher layers and arcs to override.
9. Work through the shipped exercise from **Help → Example Projects → Native USD** to see the ordering in practice on cube prims.

### Nodes / Tools / Settings
**LIVRPS — the six layer types, strongest first:**

| # | Layer type | What it does |
|---|---|---|
| **L** | **Local** | A layer made locally. **Any further changes made after composing the stage are stored as a local value.** Holds opinions on properties (cube size, colour…) and **overrides others**. |
| **I** | **Inherits** | Takes on the properties and hierarchy of the prim it inherits from. Stays **"live"** and always reflects updates on its base — **as long as no further local overrides are made**. |
| **V** | **Variants** | Groups of properties on a prim that can be **switched between**. |
| **R** | **References** | Reuse and assembly by incorporating one layer's contents into another. **Can be versioned**, and allow local changes **without impacting the original file**. |
| **P** | **Payloads** | Similar to references. A **heavy or complex** layer brought in as a payload to avoid processing it and **improve performance**. |
| **S** | **Specializes** | Acts as the **baseline values**, and is **overridden by higher layers and arcs**. |

⚠️ **The single rule that makes the acronym useful:** *"Layers that are 'higher on the list' have stronger opinions than those lower down."* Local wins over everything; Specializes loses to everything.

**Shipped exercise:** the page's video exercise composes scenes from simple cube prims across multiple layer types. **The project opens directly from Katana at Help → Example Projects → Native USD**, and the page suggests using it to follow along or to self-test.

**Referenced but not ingested:** *LIVRPS Strength Ordering* in OpenUSD's USD Glossary — the authoritative specification behind this summary.

### Difficulty
Intermediate

### Foundry App & Version
Katana 9.0v3 (page served from the current Katana 9.0v3 documentation set). LIVRPS itself is **USD**, not Katana-specific — the ordering is defined by OpenUSD and applies wherever USD composition happens.

### Tags
katana, usd, scenegraph, katana-9, intermediate

---

## Scope note — the page two other entries kept pointing at

Both `using-native-usd-workflows.md` and `importing-usd-data.md` defer to this
page for LIVRPS, making it **the most-referenced uningested page in this library**
until now. It is short (2,265 characters) but it is the piece those two were
missing: they name the arcs and say what each is *for*, and this one says which
**wins**.

⚠️ **What it is not.** This is Foundry's one-paragraph-per-arc summary, not the
specification. The real model — including how the arcs interact across composed
layer stacks — is *LIVRPS Strength Ordering* in OpenUSD's glossary, which is
**not ingested**. Treat the table above as the ordering, not as the full
semantics.

---

## Related Tutorials
- [Importing USD Data](importing-usd-data.md) — shares `katana` + `usd` + `scenegraph`; that page picks an arc **by purpose** — payload for heavy assets, inherit to propagate once, specialize when nothing may override — and this one supplies the ordering that makes those choices consequential.
- [Using Native USD Workflows](using-native-usd-workflows.md) — shares `katana` + `usd` + `scenegraph`; it lists the Composition nodes (`UsdSubLayerAdd`, `UsdInheritSet`, `UsdReferenceSet`, `UsdPayloadSet`, `UsdSpecializeSet`) and states they are "determined by LIVRPS ordering" — the ordering set out here.
- [UsdPrimCreate](usdprimcreate.md) — shares `katana` + `usd` + `scenegraph`; its `primSpec` specifiers (`define` / `class` / `over`) and the `primSpecHierarchy` default that protects lower-layer PrimSpecs are the node-level expression of exactly this strength ordering.
