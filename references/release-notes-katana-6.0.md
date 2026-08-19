---
class: release-notes
verified: partial
sources:
  - https://www.cgchannel.com/2022/12/foundry-ships-katana-6-0/
  - https://learn.foundry.com/katana/content/release_notes/whats_new_6.0.html
last_verified: never
version_basis: "katana 6.0"
---
# Katana 6.0 — Release Notes

**Released:** 2022-12-16
**Type:** Stable
**VFX Reference Platform:** CY2022 (Python 3.9.10, Qt 5.15.2, OpenEXR 3.1.4, Boost 1.76.0)

## Added
- **Material Soloing** — preview individual sections of a shading network in isolation, inside NetworkMaterialCreate nodes, via a solo icon or keyboard shortcuts 1–9.
- **Performance tab** — new analytics panel with a heat-map overlay on the Node Graph; shows node counts, high-cook-time nodes, elapsed/CPU time, and operation counts from profiling data.
- **LiveShadingGroups** — reusable material-network sections using LiveGroup-style functionality inside NetworkMaterialCreate, for sharing material sub-networks across shots/assets.
- 3Delight renderer updated to 2.9.8.

## Changed
- **NetworkMaterialEdit interface**: the deprecated "Defaults" subtab is replaced by a "Parameters" subtab for consistency with NetworkMaterialCreate. Parameters can now be promoted directly, viewed in the Material Interface, and jumped to via a quick-navigation button.

## Breaking Changes & Migration Notes
- **What breaks:** Tutorials referencing the "Defaults" subtab in NetworkMaterialEdit are describing a UI element removed in this release.
  **Workaround:** Use the "Parameters" subtab instead — the parameter-promotion workflow it exposes supersedes the old Defaults tab's function.

## Sources
- https://www.cgchannel.com/2022/12/foundry-ships-katana-6-0/
- https://learn.foundry.com/katana/content/release_notes/whats_new_6.0.html
