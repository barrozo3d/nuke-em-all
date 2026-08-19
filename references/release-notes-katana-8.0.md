---
class: release-notes
verified: partial
sources:
  - https://www.cgchannel.com/2024/12/foundry-releases-katana-8-0/
  - https://learn.foundry.com/katana/content/release_notes/whats_new_8.0.html
last_verified: never
version_basis: "katana 8.0"
---
# Katana 8.0 — Release Notes

**Released:** 2024-12-10
**Type:** Stable
**VFX Reference Platform:** CY2024 (Python 3.11.7, Qt 6.5.3, PySide 6.5.3, USD 24.05)

## Added
- **USD native exporting** (see Katana 7.5 — same feature set, newer platform): UsdLayerDefine/UsdLayerExport, KatanaToUsd conversion node.
- **Pattern-Based Collections**, 8 new native USD nodes, USD interactive transformation, USD debugging tools (Text View tab, FnErrorAPI/FnWarningAPI), USD metadata support, Viewer enhancements — all identical to 7.5's feature list.
- **Python profiling** added to the Performance tab (analyze application performance, not just scene-cook performance).

## Changed
- **Node Graph traversal ported from Python to C++** (matches 7.5).
- USD metadata now displays in the Attributes tab for both prims and properties.
- **Interactive transformations are available exclusively in "Single Path" mode** — a scoping restriction worth flagging for anyone following a multi-path-selection tutorial.

## Removed / Deprecated
- **`onTraversalVisit()` Python implementations are deprecated.** Custom 3D nodes must use `NodeTypeBuilder` going forward.
- **`GeolibRuntimeTransaction` is now an interface-only class** — code instantiating it directly (rather than through the proper API surface) will break.

## Breaking Changes & Migration Notes
- **What breaks:** Custom 3D node plug-ins implementing `onTraversalVisit()` directly are using a deprecated pattern as of 8.0.
  **Workaround:** Migrate custom 3D node logic to `NodeTypeBuilder`-based implementations.
- **What breaks:** Any code directly instantiating `GeolibRuntimeTransaction` (rather than obtaining it through the standard runtime API) will fail, since it's now interface-only.
  **Workaround:** Obtain transactions through the documented runtime API entry points instead of direct instantiation.
- **What breaks:** Tutorials demonstrating multi-path interactive transformation in the Viewer predate the "Single Path" mode restriction, or describe a workflow no longer directly available in 8.0's interactive-transform mode.
  **Workaround:** Use Single Path mode for interactive USD-prim transforms in 8.0; multi-selection transform workflows need a different (non-interactive) approach.

## Sources
- https://www.cgchannel.com/2024/12/foundry-releases-katana-8-0/
- https://learn.foundry.com/katana/content/release_notes/whats_new_8.0.html
