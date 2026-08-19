---
class: release-notes
verified: partial
sources:
  - https://learn.foundry.com/nuke/content/release_notes/nuke_14.0.html
  - https://www.cgchannel.com/2022/12/foundry-releases-nuke-14-0/
  - https://www.cgchannel.com/2023/01/nuke-to-go-subscription-only/
last_verified: never
version_basis: "nuke 14.0"
---
# Nuke 14.0 — Release Notes

**Released:** 2022-12-07
**Type:** Stable
**VFX Reference Platform:** CY2022 (Python 3.9.1, Qt 5.15.2, OpenEXR 3.1.4, Boost 1.76.0; ARRI Image SDK 7.0.0, Sony SDK 4.21.0, R3D SDK 8.3.0)

## Added
- **New USD-based 3D system (beta)** — a completely separate, parallel 3D pipeline from the "Classic" 3D system, built around a native USD scene graph. Ships with 40+ nodes at launch (~80% of the Classic system's node coverage): geometry creation/editing, lights, cameras, point clouds, depth data. This runs *alongside* Classic 3D, not replacing it, at this stage.
- **The Cattery** — free library of third-party, open-source ML models pre-converted to Nuke's `.cat` format (segmentation, depth estimation, optical flow, upscaling, denoising, style transfer) for use with the Inference node.
- **CopyCat human-matting checkpoint** — new pretrained checkpoint accelerates training for human-matting tasks up to 10x; PyTorch upgraded to 1.12.1 with ~20% additional speedup on NVIDIA Ampere GPUs.
- **UnrealReader out of beta** (NukeX/Studio) — adds custom render-pass support, OCIO colorspace matching, improved sequence picking, and light-object metadata access.
- Full OCIO soft-effect support in HieroPlayer; HDR colorimetry metadata support for monitor output.
- OCIO 2.1.2 and ACES 1.3 support with new studio and CG configs.
- **Team licensing (login-based)** extended across the whole Nuke family with admin controls.

## Changed
- Licensing direction shift: Foundry began moving the whole Nuke family toward subscription-only licensing around this release cycle — see Breaking Changes below (the formal cutover for *new* perpetual-license sales landed in January 2023, shortly after this release).

## Breaking Changes & Migration Notes
- **What breaks:** Perpetual (buy-once) licensing for new Nuke/NukeX/Nuke Studio/Hiero/Nuke Render purchases was discontinued industry-wide by Foundry effective **January 2023** (existing customers could still buy perpetual licenses through 2023-12-31). Tutorials or setup guides describing "buy a perpetual Nuke license" no longer reflect how new seats are purchased.
  **Workaround:** New seats are subscription-only (~$3,299–$5,499/year depending on edition as of the 2023 pricing). Existing perpetual licenses continue to work and can still be upgraded/maintained under their own terms — this does not retroactively revoke old licenses.
- **What breaks:** Tutorials built entirely around the "Classic" 3D system are unaffected by the new USD-based 3D system in 14.0 (it's opt-in/beta and parallel) — but tutorials that *do* start using the new USD 3D nodes should be treated as early/beta-era workflows; node names and behavior in this beta 3D system changed substantially in 14.1, 15.0, 15.1, 16.0/16.1, and especially 17.0.
  **Workaround:** For any tutorial using the new (non-Classic) USD 3D nodes from 14.0, treat it as documenting an early beta UI — expect significant node/parameter renames by 16.1/17.0; verify against the current version's Scene Graph/3D nodes before following it step-by-step.

## Sources
- https://learn.foundry.com/nuke/content/release_notes/nuke_14.0.html
- https://www.cgchannel.com/2022/12/foundry-releases-nuke-14-0/
- https://www.cgchannel.com/2023/01/nuke-to-go-subscription-only/
