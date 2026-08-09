# Mari Texturing Reference

Mari is Foundry's node-free-at-the-surface, layer-based 3D texture painting application, built for painting directly on very high-resolution meshes (its original selling point vs. Photoshop/Substance-era tools was handling film-resolution assets across many UDIM tiles without choking).

## UDIMs
The core tiling convention Mari popularized (originally a Weta Digital in-house numbering scheme, "U-Dim" = "U-DImension"). Instead of one 0-1 UV square, a model's UVs are laid out across a grid of numbered tiles (1001, 1002, 1003 … incrementing left-to-right, bottom-to-top), each tile getting its own full-resolution texture image. This is *the* reason Mari scales to hero-asset detail: a character's head can be tile 1001, torso 1002, etc., each painted/exported at full 4K+ without one giant shared texture. UDIM output is the standard interchange format most renderers and Nuke/Katana pipelines expect for high-detail texture sets.

## Channels and Layers
- A **Channel** in Mari corresponds to a shader input (Diffuse/BaseColor, Roughness, Normal, Displacement, etc.) — analogous to Ucupaint's channel concept in Blender, but Mari's channel system predates and is more industry-standard.
- Each Channel holds its own **Layer stack** (paint layers, procedural layers, adjustment layers, layer masks) — Photoshop-familiar workflow, but every stroke is projected onto the actual 3D mesh in the viewport rather than a flat 2D canvas.
- **Layer types:** Paint layers (raw brush strokes), Procedural layers (noise, gradients, cavity/AO-driven masks generated from mesh geometry), Group layers, Adjustment layers (color correct, levels) — all non-destructively stacked with blend modes and opacity, same mental model as Photoshop/Nuke's Merge stack.

## Projections
Mari paints via **projection**, not literal per-pixel UV editing: the current camera view projects your brush strokes onto the mesh surface, then bakes that projection into the underlying UDIM texture data. Multiple projection angles let you paint around a full 3D object without UV-seam visibility issues, since Mari resolves overlapping projections per-pixel using camera-facing weighting.

## Procedurals
Mari ships built-in procedural nodes (noise, cellular, gradient, curvature/cavity masks derived from mesh normals/AO) that can drive masks or generate base texture detail without hand-painting — heavily used for grime/wear/edge-damage masks (e.g. "dirt accumulates in cavities, wear happens on convex edges" driven procedurally rather than painted by hand).

## Baking / Export
- **Bake** flattens the full layer stack (per channel) down to a single set of UDIM image tiles — the deliverable that actually ships to a renderer/game engine, since the layer stack itself is a Mari-only authoring format.
- Multi-channel bakes export each shader input (Diffuse, Roughness, Normal, etc.) as its own UDIM tile set, matching what a Nuke matte-painting pipeline or a Katana/USD lookdev pipeline expects to ingest as textures on a `UsdMaterial`/shader network.

## Where Mari sits in a Nuke-suite pipeline
Mari-authored textures commonly feed: Katana lookdev (UDIM texture sets wired into shader networks on assets), and Nuke matte-painting/projection setups (a Mari-painted texture projected via Nuke's 3D system `Project3D` onto rough geo for parallax-correct set extensions). Cross-reference `nuke-compositing-nodes.md`'s "3D System" and "ST Maps, UDIMs" sections, and `katana-lookdev-lighting.md` for the lookdev side.
