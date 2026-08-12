# Nuke 17.1 — Release Notes

**Released:** 2026-07-02 (open beta; no stable release date announced yet as of 2026-08-12)
**Type:** Beta

## Added
- **Animated Gaussian Splats**: new **GeoSequencer** node processes sequences of imported USD, PLY, or SPLAT files, enabling splats to animate over time (17.0 only supported static splats).
- **Splat relighting**: the **SplatRender** node gains basic relighting support for Direct, Point, and Spot lights placed in the 3D system — splats are no longer "baked lighting only."
- **Hydra 2.0 support in the 3D viewer**: replaces/augments the Hydra 1 viewer path; adds the ability to preview individual AOVs (e.g., depth, position) directly in the viewport.
- **Non-destructive USD export**: workflows can now explicitly define sublayers and export specific scene modifications as overrides ("overs") instead of needing to flatten the whole scene between departments/pipeline stages.
- **Nuke Studio**: Annotations gain geometric shapes (rectangles, arrows); Contact Sheet now operates per-sequence; new **Compare Versions** feature for A/B comparison within the timeline.

## Changed
- Minimum supported OS bumped: Windows 11, Rocky Linux 9.0, macOS 15.0+.

## Breaking Changes & Migration Notes
- **What breaks:** Tutorials on relighting Gaussian Splats via workarounds (baking splats to point clouds, faking relight via compositing tricks) predate native splat relighting — 17.1 makes those workarounds largely unnecessary for basic Direct/Point/Spot light setups.
  **Workaround:** N/A — use native SplatRender relighting for basic cases; complex/area-light splat relighting may still need older workaround techniques since only Direct/Point/Spot are supported in this beta.
- **What breaks:** USD export workflows demonstrated on 17.0 or earlier that require a full scene flatten before handing off between departments are no longer strictly necessary — 17.1's non-destructive export (sublayers + overs) changes the recommended pipeline handoff pattern.
  **Workaround:** Prefer the new sublayer/overs export approach for 17.1+ pipelines; the old flatten-everything approach still works but discards non-destructive editability on the receiving end.
- Since this is an **open beta**, treat all details here as subject to change before stable release — do not assume final node names/behavior are locked.

## Sources
- https://www.cgchannel.com/2026/07/foundry-releases-nuke-17-1-in-open-beta/
