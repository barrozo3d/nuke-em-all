# Nuke 16.1 — Release Notes

**Released:** 2026-02-26 (announced alongside Nuke 17.0)
**Type:** Stable — **parallel release track**: carries almost all of Nuke 17.0's feature set, but pinned to the older VFX Reference Platform for studios not ready to move.
**VFX Reference Platform:** CY2024 (vs. CY2025 used by the simultaneously-released Nuke 17.0)

## Added
- **USD-based 3D system out of beta** — the new 3D system (introduced as beta in 14.0, iterated through 14.1/15.x/16.0) is production-ready here, bringing native USD into Nuke for pipeline continuity.
- New shader nodes: **ReflectiveSurface**, **BasicSurface**, **WireframeShader**.
- **Initial MaterialX support**: **MtlXStandardSurface** node to view/render Autodesk Standard Surface MaterialX shaders inside the new 3D system; previewable via the Hydra viewer, renderable via ScanlineRender2.
- New geometry/light/material nodes: GeoImport, GeoScene, GeoCamera, GeoEditCamera, GeoProjectUV, ConstantShader, FillShader, MergeLayerShader, Project3DShader, GeoBindMaterial, GeoDistantLight, GeoDiskLight, GeoSphereLight, GeoDomeLight, GeoEditLight, GeoMask, GeoClearMask, GeoPython.
- **Artistic Annotations**: Clone, Dodge, and Burn brushes; centralized Annotations Panel for tracking feedback threads.
- **BigCat** — extends CopyCat to train a single model across dozens or hundreds of images, with automatic data augmentation and custom loss functions (large-scale ML training, vs. CopyCat's traditional single-shot training).
- **Graph Scope Variables**: Python callback support for GSV events; root-node knob expressions (e.g., first_frame, last_frame, fps can now be driven by GSVs).
- **Performance**: TVIScale upscaling up to 98x faster on GPU / 26x faster on CPU; deep-composite rendering 1.88x faster.

## Breaking Changes & Migration Notes
- **What breaks:** Tutorials built on the *beta* USD 3D system from 14.0–16.0 may reference nodes/parameters that were renamed or reorganized once the system matured out of beta in 16.1/17.0.
  **Workaround:** For any beta-era (pre-16.1) USD-3D-system tutorial, verify node names against the current Scene Graph / 3D nodes toolbar rather than assuming 1:1 parity — this is the single biggest "looks different now" risk area in the whole Nuke line.
- **What breaks:** `BasicSurface` replaces the older classic `BasicMaterial` shader in workflows using the new 3D system — tutorials referencing "BasicMaterial" in the *new* USD-based 3D system (not Classic 3D, where BasicMaterial still exists) should use `BasicSurface` instead.
  **Workaround:** Swap `BasicMaterial` → `BasicSurface` when working in the new 3D system; Classic 3D's BasicMaterial node is unaffected.

## Sources
- https://learn.foundry.com/nuke/content/release_notes/nuke_16.1.html
- https://www.cgchannel.com/2026/02/foundry-releases-nuke-17-0-nukex-17-0-nuke-studio-17-0/
