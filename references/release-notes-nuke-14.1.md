---
class: release-notes
verified: partial
sources:
  - https://learn.foundry.com/nuke/content/release_notes/nuke_14.1.html
  - https://www.cgchannel.com/2023/10/foundry-releases-nuke-15-0/
last_verified: never
version_basis: "nuke 14.1"
---
# Nuke 14.1 — Release Notes

**Released:** 2023-10-13 (announced alongside Nuke 15.0)
**Type:** Stable — **parallel release track**: same feature set as Nuke 15.0, but pinned to the older VFX Reference Platform for studios not ready to move pipelines forward.
**VFX Reference Platform:** CY2022 (vs. CY2023 used by the simultaneously-released Nuke 15.0)

## Added
- Same headline features as Nuke 15.0 (see `release-notes-nuke-15.0.md`) *except* native Apple Silicon support, which is 15.0-only.
- Extended high-resolution support for planar 3D operations up to 64K.
- GeoMerge node: four new modes — Merge Layers, Duplicate Prims, Flatten Layers, Flatten to Single Layer.
- Improved 3D Viewer selection tools with a dedicated toolbar and two-tier selection.
- Scene Graph Popup in the Mask knob for filtering 3D scene data.
- ScanlineRender2 updates: new raytracing subsystem for improved shadows.
- Faster CopyCat training via distributed training across multiple machines; multi-resolution training cuts training time up to 50%.
- Machine Learning Inference available as a timeline soft effect.
- Saturation slider added to the Viewer.
- Timeline Review: auto-selection of shots under the playhead, multi-playhead frame comparison, multi-pixel Blink effects on timeline, automatic (background-refreshing) Timeline Disk Cache.
- OpenColorIO v2 alignment with an improved Output Transform subsection; OpenAssetIO tech preview.
- ARRI Alexa 35 camera support in the File Format SDK.

## Changed
- Timeline disk cache now refreshes automatically in the background rather than requiring a manual re-cache after edits.

## Breaking Changes & Migration Notes
- **What breaks:** Nothing 14.1-specific — this is a platform-pinned twin of 15.0. The main practical risk for a consultant: a tutorial that says "Nuke 14" without specifying 14.0 vs. 14.1 may actually be describing either the pre-USD-3D-parity 14.0 baseline or the 15.0-equivalent feature set in 14.1 — check which sub-version before assuming feature availability.
  **Workaround:** Treat "Nuke 14.1" tutorials as functionally equivalent to Nuke 15.0 tutorials (minus Apple Silicon-specific notes) for compositing/3D workflow purposes.

## Sources
- https://learn.foundry.com/nuke/content/release_notes/nuke_14.1.html
- https://www.cgchannel.com/2023/10/foundry-releases-nuke-15-0/
