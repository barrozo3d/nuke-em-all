---
class: release-notes
verified: partial
sources:
  - https://learn.foundry.com/mari/7.5/Content/release_notes/7.x/Mari_7.5v1_ReleaseNotes.html
  - https://www.cgchannel.com/2025/12/foundry-releases-mari-7-5/
  - https://www.cgchannel.com/2025/09/foundry-releases-mari-7-5-in-beta/
last_verified: never
version_basis: "mari 7.5"
---
# Mari 7.5 — Release Notes

**Released:** 2025-12-03 (public beta posted 2025-09-15)
**Type:** Stable
**VFX Reference Platform:** CY2023 (unchanged again — third consecutive release on this spec; libraries individually bumped: FBX 2020.3.7, libxml2 2.13.8, OpenSSL 3.0.16, zlib 1.3.1, OpenEXR 3.1.13)

## Added
- **Multi-Paint system** — paint or project into **up to 8 channels simultaneously** (developed with Wētā FX). This is the "8-stream Multi-channel Paint node" capability referenced elsewhere in this skill's notes.
- **Texture Transfer** (new Bakery feature) — streamlines transferring textures/node graphs between objects with different UV layouts, with automatic or manual UV mapping.
- **Image Manager redesign** — Groups replace tabs; batch drag-and-drop into the Multi-Paint palette with automatic channel assignment.
- Multi-Paint support added to Paint, Paint Buffer Eraser, Blur, Warp, Slerp, and Clone Stamp tools.
- 54 new skin textures + 3 animal maps from Texturing XYZ; new brush set from Bradford deCaussin.

## Patch notes — Mari 7.5v2 (2026-02-04)
- Bug-fix point release. Known issues carried from 7.5v1 (see below) — check the official point-release notes if a specific fix needs confirming.

## Known Issues
- **Roller Brush + Jittering Brush (Jitter per Tip)**: produces a gradient effect instead of distinct per-tip colors when both are combined.
- **2D Paint Mode**: switching tabs between 2D/3D resets the 2D camera to an incorrect position.

## Changed
- Windows 11 and Rocky Linux/RHEL 9 now required (bumped from Windows 10+ in 7.1).
- Pricing: $86/month or $689/year individual; $1,229/year teams (+$60/year over 7.1).

## Breaking Changes & Migration Notes
- **What breaks:** Multi-channel paint tutorials predating 7.5 describe single-channel (or manually-multiplexed) painting workflows — the native 8-channel Multi-Paint system changes the recommended approach for multi-map texturing (e.g., painting albedo+roughness+normal simultaneously).
  **Workaround:** Prefer native Multi-Paint over manual per-channel painting-then-merging workflows shown in pre-7.5 tutorials; old single-channel techniques still work, they're just no longer the fastest path.
- Windows 10 is no longer supported as of this release — pipelines still on Windows 10 must upgrade to Windows 11 to run Mari 7.5+.

## Sources
- https://learn.foundry.com/mari/7.5/Content/release_notes/7.x/Mari_7.5v1_ReleaseNotes.html
- https://www.cgchannel.com/2025/12/foundry-releases-mari-7-5/
- https://www.cgchannel.com/2025/09/foundry-releases-mari-7-5-in-beta/
