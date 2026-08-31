---
title: Composition Arcs - Understanding LIVRPS
source: Article
url: https://learn.foundry.com/katana/Content/ug/usd/composition_arcs_livrps.html
author: learn.foundry.com
ingested: 2026-08-31
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
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
