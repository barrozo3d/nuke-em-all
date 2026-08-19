---
class: release-notes
verified: partial
sources:
  - https://www.foundry.com/news-and-awards/foundry-releases-mari-70
  - https://www.cgchannel.com/2023/12/foundry-releases-mari-7-0/
last_verified: never
version_basis: "mari 7.0"
---
# Mari 7.0 — Release Notes

**Released:** 2023-12-04
**Type:** Stable
**VFX Reference Platform:** CY2023; USD 23.05

## Added
- **The Bakery** — new Vulkan-based texture baking engine (replaces the previous baking system). GPU-accelerated on NVIDIA RTX and AMD 6000-series GPUs and newer. Batch-bakes maps like curvature, thickness, displacement, and occlusion.
- Two new procedural texturing nodes: **Bubbles** and **Camouflage**.
- 60 additional bundled grunge maps (contributed by Mari expert Johnny Fehr).
- **Automatic project backups** — regular auto-save with revert-to-any-previous-state, locally or across a network.
- Fuzzy search in the Node Graph; node favoriting; Houdini-style node disconnection gesture.
- Redesigned USD importer for clarity.
- Shader updates: Autodesk Standard Surface and V-Ray 6 (VRayMTL) improved for closer viewport/final-render visual parity.
- **Team licensing** for Mari (admin-managed license pools), matching the model Nuke adopted around the same period.

## Patch notes — Mari 7.0v2 (2024-03-12)
- New **Gaussian2D blur filter**.
- Improved Bakery workflow/performance when importing meshes without UVs.

## Changed
- Compatible with Windows 10+ and Rocky Linux/RHEL 9.

## Breaking Changes & Migration Notes
- **What breaks:** Tutorials describing the pre-7.0 (pre-Bakery) baking workflow — the old baking system's UI/nodes are replaced by The Bakery's Vulkan-based pipeline. Baking node names and the batch-bake workflow differ from earlier versions.
  **Workaround:** Re-map old baking steps onto The Bakery's batch-bake dialog; GPU acceleration requires NVIDIA RTX or AMD 6000-series+ — older/unsupported GPUs fall back to (slower) non-accelerated baking.

## Sources
- https://www.foundry.com/news-and-awards/foundry-releases-mari-70
- https://www.cgchannel.com/2023/12/foundry-releases-mari-7-0/
