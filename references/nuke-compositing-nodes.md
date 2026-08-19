---
class: topic-reference
verified: no
sources: []
last_verified: never
version_basis: "unknown"
# WARNING: written from model memory, not ingested from a source.
# Do not cite as authority. If a tutorial disagrees, the tutorial wins.
---
# Nuke / NukeX Node Reference

Core node catalog for Nuke's compositing toolbar, organized the way Nuke itself groups them. Use this for "what node do I need" questions; use `nuke-python-scripting.md` for automating any of this.

## Image
Load/view/render image sequences and generate built-in elements.
- `Read` / `Write` — ingest and render footage; `Read` has per-channel/layer selection and a frame-range clamp; `Write` drives the render queue (Render/Write nodes get batched in the Render dialog or via command-line `nuke -x`).
- `Constant`, `ColorBars`, `CheckerBoard`, `ColorWheel` — synthetic test/generator patches.
- `Camera`, `ReadGeo`, `WriteGeo` (3D-context image/geo I/O — see 3D section).

## Draw
Vector and paint-based tools.
- `RotoPaint` — combined roto shapes + paint strokes in one node (superset of the older separate `Roto` and `Paint` nodes); shapes and strokes share one timeline of per-point keyframes, cusping, feather.
- `Roto` — shapes-only rotoscoping (lighter weight than RotoPaint if no paint needed).
- `Grain`, `Sparkles`, `LightWrap`, `Vectorfield` — stylized/simulated draw effects.

## Time
- `TimeOffset`, `Retime`, `OFlow` (NukeX, optical-flow-based retime/motion-vector generation), `Kronos` (NukeX, higher-quality optical-flow retime/frame-blend), `AppendClip`, `TimeClip`, `FrameHold`, `FrameRange`.

## Channel
Manage channels/layers (not just RGBA — Nuke natively supports arbitrary extra channels/AOVs per stream).
- `Shuffle` / `ShuffleCopy` — remap/copy layers into RGBA or between named layers (essential for AOV work).
- `Copy`, `Merge` (see below — Merge is technically channel-aware too), `Remove`, `AddChannels`, `Layer Contact Sheet`.

## Color
- `Grade` — offset/multiply/gamma per-channel color correction with a blackpoint/whitepoint model; the default general-purpose color-correct node.
- `ColorCorrect` — grouped shadow/midtone/highlight controls (saturation, contrast, gamma, gain, offset per range) — the more "colorist-friendly" alternative to stacking Grades.
- `HueCorrect`, `HueShift`, `Saturation`, `ColorLookup` (custom curve-based LUT), `OCIOColorSpace` / `Colorspace` (color-management conversions — see below), `Clamp`.
- **Color management:** Nuke ships with OCIO (OpenColorIO) config support; the project's working colorspace, the Read/Write per-node colorspace, and the viewer LUT are three independent settings that must agree — a very common beginner bug is a "double color-managed" or "un-managed" image from mismatching these.

## Filter
- `Blur`, `DirBlur` (directional/zoom blur), `Sharpen`, `Median`, `Erode`/`Dilate` (`FilterErode`), `EdgeDetect`, `Convolve` (custom kernel), `VectorBlur` (motion-vector-driven blur, needs a motion/velocity channel), `Defocus` (physically-based depth-of-field blur, distinct from a plain Gaussian Blur — reacts to a Z-channel or explicit defocus map).

## Transform
- `Transform` (2D translate/rotate/scale/skew, with a `CornerPin` sibling for 4-point pinning), `CornerPin2D`, `Tracker` (2D point tracking; also drives CornerPin/Transform/Roto/etc. via "Export" link), `Reformat`, `Crop`, `Position`.
- `CameraTracker` (NukeX) — full 3D camera solve from 2D footage; produces a solved `Camera` + point cloud usable in the 3D system.

## Keyer
- `Keylight` — Foundry's own bundled bluescreen/greenscreen keyer (the de facto default for most productions).
- `IBK` (Image-Based Keyer, `IBKColour`/`IBKGizmo`) — generates a clean-plate-derived key, strong for uneven/dirty screens.
- `Primatte`, `Ultimatte` — third-party-style keyers also bundled.
- `Despill` — removes residual screen-color spill after keying, usually chained right after the keyer.
- `EdgeBlur`, `EdgeExtend` — matte edge cleanup.

## Merge (2D)
- `Merge2` — the workhorse compositing operator; the "operation" dropdown (`over`, `plus`, `multiply`, `screen`, `difference`, `stencil`, `mask`, etc.) is Nuke's implementation of standard Porter-Duff-style compositing math plus blend modes. Inputs are labeled A/B with a Mask input; the "mix" slider blends the operation result back toward B.
- `Premult` / `Unpremult` — convert between premultiplied and non-premultiplied alpha; a huge fraction of "why does my comp have black fringing" bugs are premult-order mistakes around a Merge or color op.

## 3D System
Nuke's 3D system is a node-based scene graph living alongside the 2D graph, viewed through a `Viewer` in 3D-viewer mode.
- `Scene` — collects multiple 3D objects into one scene graph node.
- `Camera` / `Axis` / `Light` — standard 3D scene primitives; a `Camera` can come from `CameraTracker`'s solve or be hand-keyed.
- `ReadGeo` / `Card` / `Sphere` / `Cylinder` — geometry sources (imported meshes or Nuke primitives), often used for projection setups (project a 2D paint/plate onto rough 3D geo to handle parallax).
- `Project3D` — projects a 2D image through a camera onto 3D geometry.
- `ScanlineRender` — rasterizes the 3D scene back to 2D (Nuke's built-in renderer; not a path tracer — good for projections/set-extension geo, not final-quality CG shading).
- Materials/shading in the 3D system are comparatively basic vs. a real DCC — the 3D system exists primarily to solve *compositing* problems (projections, camera-matched geo, parallax-correct paint) rather than to replace a renderer.
- Nuke 17.0+ adds native **Gaussian Splat** support and **Field nodes** for non-destructive masking/manipulation of 3D/volumetric data (splats and beyond) — see `version-tracker.md`.

## Deep Compositing (NukeX)
Deep data stores multiple samples per pixel at different depths (from a Deep-enabled renderer's EXR output), letting compositors merge CG and live-action with correct occlusion without pre-flattening.
- `DeepRead` / `DeepWrite`, `DeepMerge`, `DeepRecolor`, `DeepToImage` / `DeepFromImage`, `DeepExpression`, `DeepCrop`, `DeepTransform`.
- Typical use: composite multiple deep CG renders (fg character, bg environment, sim/FX layer) with correct intersection/occlusion, then flatten to a normal 2D image only at the end of the chain.

## Other notable systems
- `Gizmo` / `Group` — user-bundled sub-graphs; a Gizmo is a saved, distributable Group (optionally with compiled/hidden internals) — the standard way studios ship reusable tools/templates.
- **CopyCat** (NukeX, ML-based) — trains a small neural network inside Nuke to learn an image transform from paired examples (e.g. paint-fix propagation, degrain, style match) and bakes it into an `Inference`-compatible model usable as a node.
- `Cryptomatte` — ID-matte system (originally a Psyop/community standard, natively supported) for extracting per-object/per-material mattes from a single multi-channel EXR without re-rendering.
- `STMap` — remaps an image using a separately-rendered UV/ST coordinate pass (common for lens-distortion undistort/redistort, or projecting textures via a UV pass instead of a 3D projection).

## ST Maps, UDIMs, and Mari/Nuke interplay
Nuke doesn't paint textures itself, but frequently consumes Mari-authored/baked UDIM texture sets (e.g. for projection setups or matte-painting texture prep) and produces/consumes ST maps for distortion work — see `mari-texturing.md` for the UDIM/painting side of that pipeline.
