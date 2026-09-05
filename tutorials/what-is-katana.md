---
title: What is Katana?
source: Article
url: https://learn.foundry.com/katana/Content/ug/preface/what_is_katana.html
author: learn.foundry.com
ingested: 2026-09-04
app: "Katana"
version: "9.0 (learn.foundry.com/katana current docs at ingest; release notes whats_new_9.0)"
tags: [katana, scenegraph, lookdev, lighting, usd, katana-9, beginner]
extraction_status: complete
frames_dir: tutorials/frames/what-is-katana/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# What is Katana?

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/preface/what_is_katana.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** What is Katana ? Katana was originally designed to solve problems with scalability and flexibility; how to carry out look development and lighting in a way that could deal with potentially unlimited amounts of scene data. It also needed to be flexible enough to deal with the requirements of modern CG Feature and VFX production for customized workflows, with the capability to edit or override anything. Katana leverages renderers’ support for recursive procedurals, where arbitrary scene data can be created on demand. The Katana approach is to have a single procedural that is powerful enough to handle arbitrary generation and filtering. Essentially, this is a procedural given a custom program in the form of a tree-based description of filters. At render time, Katana 's libraries are called from within this procedural to calculate scene data as the renderer demands. What Can Katana Do? Katana allows you to define what to render by using filters that can create and modify 3D scene data. A node-based interface allows users to define which filters to use, and interactively inspect their results. Using filters you can arbitrarily create and modify scene data. You can, for example: • Bring 3D scene data in from disk, such as from an Alembic geometry cache or camera animation data. • Create a new instance of a material, such as a 3Delight shader. • Create cameras and lights. • Manipulate transforms on cameras, lights and other objects. • Use rule based expressions to set what materials are assigned to which objects. • Isolate parts of the scene for different render passes. • Merge scene components from a number of partial scenes. • Specify which AOV's you want to use for multiple passes in a single render.. • Use Python scripting to specify arbitrary manipulation of attributes at any location in the scene hierarchy. The scene data to be delivered to the renderer is described by a tree of filters, and the filters are evaluated on demand in an iterative manner. Katana is designed to work well with renderers that are capable of deferred recursive procedurals. Using recursive procedurals, the tree of filters is handed directly to the renderer, with scene data calculated on demand, as the renderer requests it (lazy-evaluation). This is typically done by a procedural inside the renderer that uses Katana libraries, during render, to generate scene data from the filter tree. Katana can also be used with renders that don't support procedurals or deferred evaluation, by running a process that evaluates the scene graph and writes out a scene description file for the renderer. This approach is without the benefits of deferred evaluation at render time, and the scene description file may be very large. Note: Since Katana 's filters deliver per-frame scene data in an iterable form, Katana can also be used to provide 3D scene data for processes other than renderers. At its core, Katana is a system for the arbitrary creation, filtering, and processing of 3D scene data, with a user interface primarily designed for the needs of look development and lighting. Katana is also designed for the needs of power users, who want to create custom pipelines and manipulate 3D scene data in advanced ways. Scene Graph Iterators The key to the way Katana executes, filters, and delivers scene data on demand, is that scene data is only ever accessed through iterators. These iterators allow a calling process (such as a renderer) to walk the scene graph and examine any part of the data on request. Since that data can be generated as needed, a large scene graph state doesn't have to be held in memory. In computer science terms, it is the responsibility of the calling process to maintain its own state. Katana provides a functional representation of how the scene graph should be generated, that can be statelessly lazily-evaluated. At any location in the scene hierarchy Katana provides an iterator that can be asked: • What named attributes there are at that location? • What are the values for any named attribute (values are considered to be vectors of time sampled data)? • What are the child and sibling locations (if any)? Katana in Look Development and Lighting Katana ' s scene generation and filtering are presented as a primary artist facing tool for look development and lighting by having filter functions that allow you to perform all of the classic operations carried out in look development and lighting. Primarily: • Creating instances of shaders, or materials, out of networks of components • Assigning shaders to objects • Creating lights • Moving lights • Changing visibility flags on objects • Defining different render passes Katana ' s node-based interface provides a natural way to create recipes of which filters to use. Higher-level operations that may require a number of atomic level filters working together can be wrapped up in a single node so that the final user doesn't have to be concerned with every individual fine-grain operation. Multiple nodes can also be packaged together into single, higher-level compound nodes. Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
Katana describes a scene as a **tree of filters** handed to the renderer as a single recursive procedural, with scene data generated lazily on demand through **iterators** rather than held in memory.

### Summary
The design rationale page, and the one that explains why Katana behaves unlike a conventional 3D application. It was built for scalability and flexibility — look development and lighting over potentially unlimited scene data, with the ability to edit or override anything. Rather than building a scene in memory, Katana leverages renderers' support for **recursive procedurals**: a single powerful procedural is given a tree-based description of filters, and at render time Katana's libraries are called from inside that procedural to calculate scene data as the renderer demands it. The mechanism underneath is the **scene graph iterator** — data is *only* ever accessed through iterators that can be asked what attributes exist at a location, what their values are (as vectors of time-sampled data), and what the child and sibling locations are. Because generation is stateless and lazy, a large scene graph state never has to be held; in the page's own framing, maintaining state is the *calling* process's responsibility. The page is honest about the fallback: with renderers that lack procedurals or deferred evaluation, Katana evaluates the scene graph and writes a scene description file instead — losing the deferred benefits, and producing files that may be very large.

### Key Steps
1. Think in **recipes of filters**, not in a scene you build: nodes define which filters create and modify 3D scene data, and you inspect results interactively.
2. Bring data in from disk — Alembic geometry caches, camera animation — rather than authoring it.
3. Create material instances (e.g. a 3Delight shader), cameras and lights, and manipulate their transforms as filter operations.
4. **Assign materials by rule** using expressions rather than per-object assignment — the scalability argument in practice.
5. Isolate parts of the scene for **different render passes**, merge components from partial scenes, and specify the **AOVs** for multiple passes in a single render.
6. Use **Python scripting** for arbitrary attribute manipulation at any location in the hierarchy.
7. Understand the evaluation contract: the filter tree is handed to the renderer and evaluated **lazily**, per location, on request.
8. Package higher-level operations into single nodes, and groups of nodes into **compound nodes**, so the final user is not exposed to every atomic filter.

### Nodes / Tools / Settings
- **Recursive procedurals** — the renderer-side mechanism Katana targets; the filter tree is handed over and evaluated on demand.
- **Scene graph iterators** — the only access path to scene data; answer: which named attributes exist here, their values (vectors of time-sampled data), and the child/sibling locations.
- **Lazy / stateless evaluation** — no large scene graph state held in memory; the calling process maintains its own state.
- **Scene description fallback** — for renderers without deferred evaluation; loses the benefits, files may be very large.
- Capability list: Alembic import, shader instances, cameras and lights, transforms, rule-based material assignment, pass isolation, scene merging, **AOVs**, Python attribute manipulation.
- Noted aside: because filters deliver per-frame scene data in iterable form, Katana can feed processes other than renderers.

### Difficulty
Beginner

### Foundry App & Version
Katana 9.0 (page is version-independent design rationale).

### Tags
`katana`, `scenegraph`, `lookdev`, `lighting`, `usd`, `katana-9`, `beginner`

---

## Related Tutorials
- [Using the Scene Graph](using-the-scene-graph.md) — the same model from the operator's side.
- [OpScript Tutorials](opscript-tutorials.md) — the Python/Lua attribute manipulation this page describes in the abstract.

---

> **Provenance.** `learn.foundry.com/katana` (MadCap Flare). Paths in this doc set
> are not guessable and `Data/Tocs/*` 404s, so this page was reached by crawling
> from `Content/learn_katana.html` → `user_guide.html`, or from a sibling page's
> own links. Reference-guide and user-guide pages carry clean `<title>`s and need
> no `--title` override, unlike `learn.foundry.com/nuke/developers/**`.
