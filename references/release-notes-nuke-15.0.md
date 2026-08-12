# Nuke 15.0 — Release Notes

**Released:** 2023-10-13 (public beta posted 2023-09-02, updated for final release)
**Type:** Stable
**VFX Reference Platform:** CY2023 (Rocky Linux 9 replaces CentOS 7 as the supported Linux distro — a minimum-OS change)

## Added
- **Native Apple Silicon support** — up to 20% faster general processing on M-series Macs vs. Rosetta emulation.
- Extended high-resolution support for images up to 64K on planar operations.
- Faster CopyCat training via distributed processing across multiple machines (up to 50% faster).
- GeoMerge node redesign: Merge Layers, Duplicate Prims, Flatten Layers, Flatten to Single Layer modes.
- 3D Viewer selection tools: dedicated toolbar, two-tier selection.
- Scene Graph Popup for USD Mask-knob navigation.
- ScanlineRender2 raytracing enhancements.
- Saturation slider in the Viewer.
- Timeline review auto-selection under playhead; multi-playhead comparison.
- Multi-pixel Blink effects available at the timeline level.
- Machine Learning Inference as a timeline soft effect.
- Automatic (background) Timeline Disk Cache refresh.
- OpenColorIO 2.2 alignment with OCIOZ support.
- OpenAssetIO tech preview integration extended.
- ARRI Alexa 35 HDE format support; ARRI Image SDK updated to 8.0.0.

## Changed
- **Minimum supported Linux distro changes from CentOS 7 to Rocky Linux 9** as part of VFX Reference Platform CY2023 compliance. Studios on CentOS 7 pipelines must upgrade OS to run Nuke 15.0.

## Breaking Changes & Migration Notes
- **What breaks:** Any pipeline/render-farm tooling still targeting CentOS 7 will not be able to run Nuke 15.0 natively.
  **Workaround:** Upgrade render nodes/workstations to Rocky Linux 9 (or stay on Nuke 14.1, the CY2022-platform parallel release, until the OS migration is complete).
- **What breaks:** Tutorials demonstrating GPU-based ML training (CopyCat) on Intel Macs pre-15.0 won't show the Apple Silicon-native speed characteristics; expect training-time claims in older tutorials to be conservative for M-series users on 15.0+.

## Sources
- https://learn.foundry.com/nuke/content/release_notes/nuke_15.0.html
- https://www.cgchannel.com/2023/10/foundry-releases-nuke-15-0/
- https://www.digitalmediaworld.tv/vfx/foundry-nuke-15-0-goes-for-speed-with-apple-silicon-ml-and-usd-3d-updates
