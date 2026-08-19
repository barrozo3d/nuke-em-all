---
class: release-notes
verified: partial
sources:
  - https://learn.foundry.com/katana/content/release_notes/whats_new_8.5.html
last_verified: never
version_basis: "katana 8.5"
---
# Katana 8.5 — Release Notes

**Released:** 2026-02-18 (announced alongside Katana 9.0)
**Type:** Stable — **parallel release track**: identical feature set to Katana 9.0, pinned to the older VFX Reference Platform for studios not ready to move.
**VFX Reference Platform:** CY2024 (vs. CY2025 used by the simultaneously-released Katana 9.0); USD 25.08; Python 3.11.7, Qt 6.5.3, OpenVDB 11.0.0

## Added
- **UsdSuperLayer node** — foundational node providing direct access to a USD Layer at Node Graph level, with a customizable context menu and parameter handlers, copy/paste support, and color-coded prim-state icons (unchanged / edited / locally created). Intended as a base for building more efficient custom USD tools (accessible via Katana's Python API).
- **UsdGaffer node** — a specialized node derived from UsdSuperLayer, purpose-built for lighting workflows: filters the tree view to lighting-relevant schemas (UsdLuxBoundableLightBase, UsdLuxLightFilter) and adds a dedicated linking tab for light/shadow linking relationships via USD Collections.
- **UsdMaterial node** — lightweight tool with three modes: create a single-shader material, edit an existing shader prim, or edit a material's interface (promoted properties). Explicitly positioned as *not* a full look-dev solution — simple edits/debugging only.
- **Hydra 2.0 rendering (experimental)**: new Hydra 2.0 Viewer tab for viewport rendering of USD stages + some Geolib attributes, and a Hydra Scene Browser tab for inspecting Hydra prims/data sources.

## Breaking Changes & Migration Notes
- **What's new, not breaking:** UsdSuperLayer/UsdGaffer/UsdMaterial are additive — no removals confirmed in the fetched notes.
- Hydra 2.0 is experimental/behind a preview path in this release — do not expect full parity with the existing Hydra 1 viewport (attribute/AOV coverage gaps are expected; see the Katana 9.0 notes for the environment-variable gate).

## Sources
- https://learn.foundry.com/katana/content/release_notes/whats_new_8.5.html
