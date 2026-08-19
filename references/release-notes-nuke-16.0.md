---
class: release-notes
verified: partial
sources:
  - https://learn.foundry.com/nuke/content/release_notes/nuke_16.0.html
  - https://www.cgchannel.com/2025/02/foundry-releases-nuke-16-0/
  - https://www.animationmagazine.net/2025/02/foundry-releases-nuke-16-0-featuring-native-variable-enabled-workflows/
last_verified: never
version_basis: "nuke 16.0"
---
# Nuke 16.0 — Release Notes

**Released:** 2025-02-28 (beta posted 2024-12-12)
**Type:** Stable
**VFX Reference Platform:** CY2024 (full support); OpenAssetIO upgraded to v1.0.0-rc.1.0

## Added
- **Native Multishot compositing workflow**, built on Graph Scope Variables (GSVs):
  - **VariableSwitch** — switch between shots/scopes via variables.
  - **VariableGroup** — define variables and scopes.
  - **Variables Panel**.
  - Command-line render support with variable specification (render specific shots/scopes from the CLI).
- **Link Nodes** — linked node copies with override capability.
- **GeoXformPrim** — create/edit scene-graph transforms in the new USD-based 3D system.
- **GeoConstrain** — prim constraints: LookAt, Transformation, Parent modes.
- **Roto performance overhaul** — caching, playback, interactivity, motion blur all improved.
- **Quick Export** — up to 12x faster compressed-video export (ProRes/DNxHD/DNxHR/H.264).
- **ScanlineRender2**: motion blur and AOV improvements; foundation work for the raytracing architecture matured further in 17.0.
- **Nuke Studio**: Multichannel Soft Effects (edit multilayer EXRs' visibility/values directly on timeline); Contact Sheet for multi-shot review/comparison.
- **BlinkScript editor overhaul**: IDE-style editor with find/replace, autofill, error accordion; Library Files for code reuse across kernels; Safety Rails to catch common authoring errors before compile.

## Changed
- **macOS now uses FoundryGL instead of the deprecated system OpenGL** — relevant if a tutorial troubleshoots viewport/OpenGL driver issues on Mac; those steps may no longer apply.
- **Geo modifier nodes now default to "All" instead of "LastModified"** in the 3D system — a tutorial written pre-16.0 that relies on the old "LastModified" default will produce different results if followed verbatim on 16.0+ without checking this knob.
- **GeoMerge/GeoScene nodes now display the A pipe by default** (previously a different default pipe was shown).

## Breaking Changes & Migration Notes
- **What breaks:** Any tutorial relying on the pre-16.0 default of Geo modifier nodes ("LastModified") will get different results when followed on 16.0+ without manually resetting the knob.
  **Workaround:** Explicitly set the modifier scope knob to "LastModified" if replicating an older tutorial's exact behavior is required; otherwise "All" is usually the more predictable choice going forward.
- **What breaks:** macOS-specific viewport/OpenGL-driver troubleshooting steps from pre-16.0 tutorials are obsolete since the viewport now runs on FoundryGL, not system OpenGL, on Mac.
  **Workaround:** Ignore legacy OpenGL driver-update advice for Mac; FoundryGL issues are debugged differently (check Nuke's own release notes/known-issues per point release instead).

## Sources
- https://learn.foundry.com/nuke/content/release_notes/nuke_16.0.html
- https://www.cgchannel.com/2025/02/foundry-releases-nuke-16-0/
- https://www.animationmagazine.net/2025/02/foundry-releases-nuke-16-0-featuring-native-variable-enabled-workflows/
