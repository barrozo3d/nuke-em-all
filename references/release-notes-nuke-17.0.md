---
class: release-notes
verified: partial
sources:
  - https://learn.foundry.com/nuke/content/release_notes/nuke_17.0.html
  - https://www.cgchannel.com/2026/02/foundry-releases-nuke-17-0-nukex-17-0-nuke-studio-17-0/
  - https://digitalproduction.com/2026/02/26/nuke-17-0-rewires-3d-and-adds-gaussian-splats/
last_verified: never
version_basis: "nuke 17.0"
---
# Nuke 17.0 — Release Notes

**Released:** 2026-02-26 (beta posted 2025-11-18)
**Type:** Stable
**VFX Reference Platform:** CY2025; USD 25.08

## Added
- **Native 3D Gaussian Splat support** — the headline feature of this release. Splats (`.ply` / `.splat`) import and render via **GeoImport**/**GeoReference** inside the USD-based 3D system, with a dedicated **SplatRender** node handling rendering (including motion blur).
- **Field nodes** — a new toolbar of nodes for creating, combining, and transforming "Fields," giving non-destructive, volumetric-style manipulation/masking of Gaussian Splats and other 3D point data (isolate/mask splat regions without baking).
- **USD/3D system overhaul** (continuing the maturation started in 16.1):
  - Advanced import dialog with payload management and filtering.
  - New **Axis** node with constraint types: LookAt, Parent, Transformation, Translation, Rotation, Scale.
  - **Snapshot** function to disconnect nodes from live USD data while retaining their current state.
  - Non-destructive USD authoring with manual overrides.
- **MaterialX support matures**: MtlXStandardSurface remains the entry point; workflow refined for texture/control customization.
- **GeoProjectUV** — "sticky projections" via the Constrain toolset; ScanlineRender adds Cylindrical and UV-Unwrap projection modes.
- **Ray tracing & motion blur**: ScanlineRender ray-depth control, improved motion-blur sampling, new shutter-behavior parameters.
- **Artistic Annotations expansion**: redesigned Paint brush with eyedropper, Vanishing brush (fades over time), Clone/Dodge/Burn carried over from 16.1, centralized Annotations Panel.
- **BigCat** (large-scale CopyCat training) gains validation-dataset support and perceptual loss functions.
- **Graph Scope Variables**: further Python callback and node-label visibility integration; deeper 3D-system integration.
- **Format/codec**: NotchLC MOV codec (Windows/Linux), HDR MOV metadata support, native ACES 2.0 (ACEScg + OCIO Studio configs).
- **Node graph readability**: updated node naming/color coding, mask icons, Live Read indicators for external data sources.
- **Python API**: expanded annotation API — creation, management, comment/note editing, brush-settings configuration scriptable from Python.

## Changed
- **Pricing**: annual subscription increases — Nuke +$190/yr, NukeX +$250/yr, Nuke Studio +$310/yr, Render licenses +$22/yr. Nuke Indie unchanged at $499/yr.
- Deep-composite rendering 1.88x faster than 16.x; TVIScale upscaling up to 98x faster on GPU / 26x faster on CPU (carried over/refined from 16.1's numbers).

## Breaking Changes & Migration Notes
- **What breaks:** As with 16.1, any tutorial referencing beta-era USD 3D system node names/parameters (pre-16.1) is at high risk of being stale — 17.0 continues restructuring this system (new Axis node with constraints, Snapshot function, new import dialog) on top of 16.1's changes.
  **Workaround:** Treat any pre-16.1 "new 3D system" (not Classic 3D) tutorial as needing a node-by-node sanity check against the current toolset before following it literally.
- **What breaks:** Tutorials demonstrating Gaussian Splat workflows on Nuke versions before 17.0 don't exist as native workflows — prior to 17.0 there was no native splat import/render pipeline in Nuke at all (splats had to be handled via third-party gizmos or exported point-cloud proxies).
  **Workaround:** Any "how to bring Gaussian Splats into Nuke" tutorial predating 17.0 is either using a workaround/gizmo that's now unnecessary, or is not applicable — use the native GeoImport/GeoReference + SplatRender + Field nodes workflow instead.

## Sources
- https://learn.foundry.com/nuke/content/release_notes/nuke_17.0.html
- https://www.cgchannel.com/2026/02/foundry-releases-nuke-17-0-nukex-17-0-nuke-studio-17-0/
- https://digitalproduction.com/2026/02/26/nuke-17-0-rewires-3d-and-adds-gaussian-splats/
- https://www.aswf.io/blog/materialx-implementation-underway-in-foundrys-nuke-17-0/
