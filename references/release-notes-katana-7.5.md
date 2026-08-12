# Katana 7.5 — Release Notes

**Released:** 2024-12-09 (announced alongside Katana 8.0)
**Type:** Stable — **parallel release track**: same new feature set as Katana 8.0, pinned to the older VFX Reference Platform for studios not ready to move.
**VFX Reference Platform:** CY2023 (matching Katana 7.0; vs. CY2024 used by the simultaneously-released Katana 8.0). USD upgraded to 24.05 within this platform pin.

## Added
- **USD native exporting** — exporting *from* Katana's Native USD stage becomes possible for the first time, via:
  - **UsdLayerDefine** — defines a layer-composition scope.
  - **UsdLayerExport** — exports stage changes between the define/export node pair as a whole layer.
- **KatanaToUsd node** — converts Geolib scene-graph data to USD without baking layers; supports materials, lights, all mesh types, and custom attributes.
- **Pattern-Based Collections (PBC)** — integrates USD 23.11 collections with a new widget and **UsdCollection** node; CEL-like path-based prim selection with union/difference/intersect/complement operations.
- **8 new native USD nodes**: UsdCamera, UsdLight, UsdScope, UsdXform, UsdMaterialAssign, and additional transform-related nodes.
- **USD interactive transformation** — viewer manipulators now work directly on native USD prims via a `makeInteractive` parameter (translate/scale/rotate).
- **USD debugging**: new USD Text View tab (contribution layers or composed stage); `FnErrorAPI` / `FnWarningAPI` schemas.
- **USD metadata support** in the Attributes tab (prim + property metadata, dedicated metadata buttons).
- **USD Viewer enhancements**: native camera/light locators visible in the Viewer; cameras selectable via the Look-Through menu.

## Changed
- **Node Graph traversal ported from Python to C++** for improved interactivity on large graphs — this is a performance change with a real API consequence (see Breaking Changes).

## Breaking Changes & Migration Notes
- **What breaks:** Custom actions/plug-ins built against Katana ≤6.5's `CommonNodesAPI`/`Nodes3DAPI` that rely on the old Python-based Node Graph traversal may break or behave differently after the Python→C++ port.
  **Workaround:** Review any custom action code touching Node Graph traversal against the current `CommonNodesAPI`/`Nodes3DAPI` docs for this version; this is explicitly called out by Foundry as a compatibility risk for post-6.5 custom tooling.

## Sources
- https://learn.foundry.com/katana/content/release_notes/whats_new_7.5.html
