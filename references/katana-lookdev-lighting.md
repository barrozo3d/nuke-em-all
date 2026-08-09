# Katana Look Development & Lighting Reference

Katana is Foundry's asset-based look-development and lighting application — the "assembly and lighting" layer that sits between asset creation (modeling/texturing/rigging done elsewhere) and final rendering, built to scale to full production-sized scenes (hundreds of assets, USD-driven asset resolution, per-shot lighting variation).

## SceneGraph vs. NodeGraph
These are Katana's two core, tightly linked concepts:
- **SceneGraph** — the actual data tree describing the scene at any point in the network: a hierarchy of **locations** (paths, like a filesystem — `/root/world/geo/char/head`), each carrying **Attributes** (geometry references, material bindings, transforms, render settings, arbitrary metadata). This is what actually gets sent to the renderer.
- **NodeGraph** — the node-based "recipe" of operations (a chain of nodes) that *produces* a given state of the SceneGraph. Each node reads the incoming SceneGraph, modifies/adds/prunes locations or attributes, and passes it downstream — conceptually similar to how a Nuke node chain produces an image, except the "image" here is a hierarchical scene description.
- You inspect the SceneGraph at any point in the chain via the Scenegraph tab (a live, navigable tree view synced to whichever node's output you're viewing).

## Groups vs. Macros
- **Group node** — bundles a chain of child nodes into one collapsed node purely to simplify/organize a NodeGraph; still fully editable by entering the group, and not inherently reusable/shareable as a distinct tool.
- **Macro** — a Group-like container that is explicitly published/saved as a reusable, distributable node type (parameters exposed on the macro's own interface) — the Katana equivalent of a Nuke Gizmo: build once, reuse across shots/shows.

## Look Development
Katana's lookdev workflow centers on building and iterating shading networks per asset (often authored once per asset and referenced into many shots), with strong support for:
- Material overrides/variants at specific SceneGraph locations without duplicating the whole shading network.
- Live, interactive viewport feedback via the renderer's IPR (interactive preview render) — Katana is render-agnostic at the API level (works with Arnold, RenderMan, V-Ray, etc. via renderer plugins), so the exact shading-node vocabulary depends on which render delegate/plugin is in use.

## USD in Katana
Katana natively supports USD (Universal Scene Description) as both an input format (referencing USD-authored assets into a scene) and an internal working representation for parts of the graph.
- **UsdSuperLayer** (new in Katana 9.0) — gives node-graph-level, dynamic access to a live USD Layer, intended as the foundation for future specialized USD-native tools with large computational savings over previous USD-conversion approaches.
- **UsdMaterial** (Katana 9.0) — a lightweight node for making quick edits on incoming USD looks, or on looks converted from Katana's native shading via a KatanaToUsd-style workflow.
- **Hydra 2.0** (alpha in 9.0) — a unified viewer/rendering framework spanning both USD and Katana's native Geolib scene representation, part of Foundry's broader USD-standardization push across the Nuke/Katana/Mari suite.

## Lighting
Lighting in Katana is built the same NodeGraph-driven way as lookdev: light-rig nodes placed/instanced across the SceneGraph, often parameterized so the same lighting setup can be re-targeted across many shots in a sequence with per-shot overrides layered on top rather than rebuilt from scratch. Because the SceneGraph is asset/location-based rather than a flat scene, lighting TDs commonly work with CEL (Catalog Expression Language) — Katana's location-matching query syntax — to target lights/overrides at specific locations or groups of locations by pattern rather than hand-picking each one.

## Where Katana sits relative to Nuke/Mari
Katana consumes Mari-authored (or other DCC-authored) UDIM texture sets in its shading networks, and its rendered output (typically multi-AOV EXR, often Deep-enabled) is the input Nuke compositors build final shots from — see `nuke-compositing-nodes.md`'s Deep Compositing and Channel sections for the comp-side half of that pipeline.
