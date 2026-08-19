---
class: release-notes
verified: partial
sources:
  - https://www.cgchannel.com/2026/07/foundry-releases-mari-8-0-in-open-beta/
last_verified: never
version_basis: "mari 8.0"
---
# Mari 8.0 — Release Notes

**Released:** 2026-07-02 (open beta; no stable release date announced yet as of 2026-08-12)
**Type:** Beta
**VFX Reference Platform:** CY2025 (jumps forward from CY2023 used in 7.5 — skips CY2024 entirely)

## Added
- **Compare node** — A/B wipe comparisons between the outputs of different Node Graph streams, for iterating on materials/variants without leaving the graph.
- **Hex Tile node** — minimizes visible texture repetition by tiling/blending in a hexagonal grid instead of a conventional rectangular one.
- **Color Remap node** — centralizes color grading (hue, saturation, exposure, gamma) in a single node.
- **49 new math nodes** — arithmetic, trigonometry, conditional logic, and randomization operations added to the Node Graph (over 50 new nodes total per some secondary coverage — treat "50+" as approximate, 49 math nodes is the figure from the CG Channel writeup).
- **Trackball navigation** — alternative camera-control scheme alongside the standard Orbit tool.
- Project Archiving indicator — visual marker in the library for archived projects.

## Changed
- Windows 11 and Rocky Linux/RHEL 9 required (unchanged from 7.5).
- Pricing: individual unchanged ($86/month or $689/year); team subscriptions $1,289/year (+$60 over 7.5).

## Breaking Changes & Migration Notes
- **What breaks:** Nothing confirmed as removed — this is an additive node-graph expansion. Since it's an **open beta**, treat exact node names/behavior as provisional until stable release.
  **Workaround:** N/A yet — re-verify against the stable 8.0 release notes once published.
- The jump from CY2023 (Mari 7.5) straight to CY2025 (Mari 8.0) means any pipeline tooling gated on VFX Reference Platform CY2024 compatibility should double check library versions (Python, OpenEXR, etc.) rather than assuming an incremental step.

## Sources
- https://www.cgchannel.com/2026/07/foundry-releases-mari-8-0-in-open-beta/
