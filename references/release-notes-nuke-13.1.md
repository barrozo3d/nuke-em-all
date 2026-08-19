---
class: release-notes
verified: partial
sources:
  - https://learn.foundry.com/nuke/content/release_notes/nuke_13.1.html
  - https://www.cgchannel.com/2021/11/foundry-ships-nuke-13-1/
  - https://www.cgw.com/Press-Center/News/2021/Foundry-Releases-Nuke-13-1-with-Focus-on-Streaml.aspx
last_verified: never
version_basis: "nuke 13.1"
---
# Nuke 13.1 — Release Notes

**Released:** 2021-11-23
**Type:** Stable
**VFX Reference Platform:** CY2020/2021 transition (not explicitly stated in Foundry's marketing release notes; treat as unconfirmed — cross-check the official PDF release notes if precision matters)

## Added
- **UnrealReader (beta, NukeX/Studio only)** — live link to Unreal Engine, connects to the Unreal Editor for live renders with layer/pass separation.
- **3D UX redesign** — 3D transform handles fully reworked to match Katana's manipulator conventions: multi-axis manipulation, local/world/screen space toggles.
- **OCIO v2 support** — new GPU-accelerated OCIO v2 implementation improving playback performance and viewer color consistency; native ACES support with reduced reliance on baked LUTs.
- **ACES 1.2 configuration** — additional colorspace conversions and HDR output transforms.
- **CatFileCreator node** — loads third-party PyTorch models (via TorchScript) into Nuke's `.cat` machine-learning format for use with CopyCat/Inference.
- **Encryptomatte node** — native tool for authoring custom Cryptomattes from within Nuke (companion to native Cryptomatte from 13.0).
- Cryptomatte matte-removal shortcut: `-` (minus) modifier now supported for excluding IDs from a matte selection.
- Extended Hydra viewer support to macOS (hdStorm 3D renderer).
- Timeline/project improvements: copy-paste of clips and sequences between projects, copy-paste between Timeline and Node Graph, per-clip FPS override on import, per-frame metadata access, five new soft effects (ModifyMetadata, ColorLookup and OCIO variants).

## Changed
- **Shake to Disconnect** is now enabled by default (previously opt-in) — dragging a node away with a shake gesture disconnects it from the graph.
- Monitor Out parameters reorganized; added annotation and cursor overlay support on monitor output.
- Project load times improved 25–30% for scripts saved in 13.1 format.

## Removed / Deprecated
- **ACES 1.0.3 configuration removed** — scripts pinned to ACES 1.0.3 will need to be migrated to ACES 1.2 or a newer OCIO config.

## Breaking Changes & Migration Notes
- **What breaks:** Old tutorials relying on ACES 1.0.3 colorspace names/config will fail to load that config in 13.1+.
  **Workaround:** Re-target the script's OCIO config to ACES 1.2 (or later) and remap any ACES 1.0.3-specific colorspace names to their 1.2 equivalents.
- **What breaks:** Tutorials that manually drag nodes off the graph expecting them to stay connected (relying on the old default) may see nodes disconnect unexpectedly, since Shake to Disconnect is now on by default.
  **Workaround:** Disable Shake to Disconnect in Preferences > Behaviors if the old (no auto-disconnect) behavior is wanted.

## Sources
- https://learn.foundry.com/nuke/content/release_notes/nuke_13.1.html
- https://www.cgchannel.com/2021/11/foundry-ships-nuke-13-1/
- https://www.cgw.com/Press-Center/News/2021/Foundry-Releases-Nuke-13-1-with-Focus-on-Streaml.aspx
