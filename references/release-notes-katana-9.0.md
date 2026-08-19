---
class: release-notes
verified: partial
sources:
  - https://www.cgchannel.com/2026/02/foundry-releases-katana-9-0/
  - https://learn.foundry.com/katana/content/release_notes/whats_new_9.0.html
  - https://digitalproduction.com/2026/02/11/katana-9-deepens-usd-and-previews-hydra-2/
last_verified: never
version_basis: "katana 9.0"
---
# Katana 9.0 — Release Notes

**Released:** 2026-02-18
**Type:** Stable
**VFX Reference Platform:** CY2025; USD 25.08; Python 3.11.11, Qt 6.5.3, OpenVDB 12.0.0

## Added
- **UsdSuperLayer node** — the headline feature. Provides direct access to a USD Layer at Node Graph level via a foundational SuperTool architecture, with customizable context menus and parameter handlers. Foundry frames this as the basis for future USD-native tool development: consolidating operations into a single layer (rather than a new USD layer per node) gives "huge computational savings." Accessible from Katana's Python API for building custom tools on top of it.
- **UsdGaffer node** — specialized UsdSuperLayer derivative for lighting: filters to light-relevant prims, adds a dedicated light/shadow linking tab built on USD Collections.
- **UsdMaterial node** — lightweight single-shader material creation/editing tool; three modes (create, edit shader, edit material interface). Explicitly scoped as simple/debugging use, not a full look-dev replacement.
- **Hydra 2.0 support (alpha)** — behind the `KATANA_ENABLE_HYDRA2` environment variable. Adds a Hydra 2.0 Viewer tab (USD stages + some Geolib attributes rendered together) and a Hydra Scene Browser tab for prim/data-source inspection and debugging.

## Changed
- USD stages render in the Hydra 2.0 viewport **without** the expansion-based loading used elsewhere in the Scene Explorer/Viewer.
- **Geolib attributes render in Hydra 2.0 but do not yet have full parity with Hydra 1.0** — expect visual/feature gaps if comparing the two viewport paths directly.
- Pricing: Katana Interactive subscription +$670/year (now $4,199/year); Render subscription +$35/year (now $374/year). Rental-only licensing (no perpetual option) — consistent with the rest of the Foundry suite's post-2022/2023 subscription-only direction.

## Breaking Changes & Migration Notes
- **What breaks:** Tutorials describing Hydra viewport rendering without specifying "Hydra 1" vs. "Hydra 2" should be assumed to mean the existing Hydra 1 pipeline — Hydra 2.0 is alpha, opt-in via an environment variable, and not yet at feature parity for Geolib (non-USD-native) attributes.
  **Workaround:** Don't switch production pipelines to Hydra 2.0 based on a tutorial written for 9.0's alpha preview; validate Geolib-attribute coverage first, or wait for Hydra 2.0 to exit alpha in a future release.
- **What's new, not breaking:** UsdSuperLayer/UsdGaffer/UsdMaterial have no confirmed predecessor nodes to migrate from — they're new additions building on the native-USD foundation laid down in Katana 7.0/7.5/8.0.

## Sources
- https://www.cgchannel.com/2026/02/foundry-releases-katana-9-0/
- https://learn.foundry.com/katana/content/release_notes/whats_new_9.0.html
- https://digitalproduction.com/2026/02/11/katana-9-deepens-usd-and-previews-hydra-2/
- https://www.awn.com/news/foundry-releases-katana-90-new-usdsuperlayer
