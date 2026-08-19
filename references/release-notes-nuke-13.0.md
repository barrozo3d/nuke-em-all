---
class: release-notes
verified: partial
sources:
  - https://learn.foundry.com/nuke/content/release_notes/nuke_13.0.html
  - https://www.cgchannel.com/2021/03/foundry-ships-nuke-nukex-nuke-studio-nuke-indie-13-0/
last_verified: never
version_basis: "nuke 13.0"
---
# Nuke 13.0 — Release Notes

**Released:** 2021-03-17
**Type:** Stable
**VFX Reference Platform:** CY2020 (Python 3.7.7, OpenEXR 2.4.2, Boost 1.70.0)

## Added
- **AIR (Artificial Intelligence Research) machine learning framework**, NukeX/Studio only, requires an NVIDIA GPU (compute capability 3.0+):
  - **CopyCat** — trains a neural network on a before/after pair of frame sequences to learn and repeat an effect (roto, paint, degrain, etc.).
  - **Inference** — applies a trained `.cat` model to footage.
  - **Deblur** — ML-based motion blur removal.
  - **Upscale** — ML-based 2x image upscaling.
- **Hydra viewer** — new 3D viewport renderer (Windows/Linux only at launch) built on USD's Hydra, aligning Nuke's 3D viewport with Katana, Solaris, and usdview. Adds OIT (order-independent transparency) sampling controls, light/material/shadow toggles.
- **Native USD support (initial)** — Camera, Light, and Axis nodes can load data directly from `.usd`/`.usda`/`.usdc` files. USD library upgraded to 20.08.
- **Native Cryptomatte** — Cryptomatte is now a built-in plug-in (previously a third-party gizmo), with a simplified UI and vertical matte lists. Basic functionality shipped in beta.
- **Monitor Out overhaul** — extended across the whole Nuke family; floating monitor windows, independent output transforms per monitor, AJA/Blackmagic device controls.
- **HDR Display (macOS, beta)** — HDR monitoring on compatible Macs via sRGBf/P3 gamut display.
- **Sync Review** expanded from playback-only sync to also sync timeline edits, viewer state, and bin changes across artists.
- HieroPlayer annotations integrated into the main Nuke Studio/Hiero annotation system.

## Changed
- OCIO Roles are now prioritized by default in colorspace dropdowns — Roles appear in the main cascading menu, with raw Colorspaces demoted to a sub-menu. Scripts/tutorials that assume the old colorspace-first menu layout will look different.
- Licensing: this is the last Nuke family line sold under a perpetual-license-first model before Foundry began phasing perpetual licenses out (see Nuke 14.0 notes for the 2023 subscription-only cutover).

## Known Issues
- Cryptomatte (native, beta) does not support Encryptomatte nodes yet (Encryptomatte itself shipped in 13.1).
- Potential AJA driver issues reported on macOS 11.0 (Big Sur) at launch.

## Breaking Changes & Migration Notes
- **What breaks:** Tutorials showing the old third-party Cryptomatte gizmo UI (horizontal matte list, separate install) will look and behave differently from the new native Cryptomatte node.
  **Workaround:** Use the native `Cryptomatte` node shipped with Nuke 13.0+; matte list is now vertical, and manual `+`/`-` picking works the same conceptually but the node's picker UI has moved.
- **What breaks:** Any tutorial demonstrating GPU-accelerated ML tools (CopyCat, Inference, Deblur, Upscale) on non-NVIDIA hardware (e.g., AMD, Apple Silicon-only setups) will not work — AIR tools require an NVIDIA GPU on this release.
  **Workaround:** No AMD/Metal support existed at this point; this only changed with GPU-vendor-agnostic improvements in later releases (verify per-version — Apple Silicon ML support arrived with 15.0's native ARM build, not necessarily full ML GPU parity).

## Sources
- https://learn.foundry.com/nuke/content/release_notes/nuke_13.0.html
- https://www.cgchannel.com/2021/03/foundry-ships-nuke-nukex-nuke-studio-nuke-indie-13-0/
