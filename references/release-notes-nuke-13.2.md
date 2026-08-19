---
class: release-notes
verified: partial
sources:
  - https://learn.foundry.com/nuke/content/release_notes/nuke_13.2.html
  - https://www.cgchannel.com/2022/04/foundry-ships-nuke-nukex-nuke-studio-nuke-indie-13-2/
  - https://www.foundry.com/news-and-awards/nuke-13-2-released
last_verified: never
version_basis: "nuke 13.2"
---
# Nuke 13.2 — Release Notes

**Released:** 2022-04-14
**Type:** Stable

## Added
- **NDI streaming support** in Monitor Out, plus multiple simultaneous output streams, AJA T-Tap Pro support, and improved Blackmagic Design device integration.
- **OpenTimelineIO (OTIO) support (beta)** in Nuke Studio's Timeline.
- Non-linear dissolves on the Timeline.
- Rotatable pivot points and a new free-rotation algorithm for 3D geometry manipulation.
- ARRI SDK 7.0.0 available as beta (alongside the existing 6.2 SDK used for legacy ARRIRAW files).
- Blackmagic RAW SDK upgraded to 2.2, expanding supported camera models.

## Changed
- **Node graph rendering switched to top-down, node-by-node evaluation** instead of the previous scanline-by-scanline on-demand approach — Foundry reports internally-tested scripts rendering ~20% faster on average, some up to 1.5x faster.
- **CopyCat** (NukeX ML toolset) sped up: up to 30% faster single-GPU training, plus new multi-GPU and multi-channel training support.
- **UnrealReader** (beta) gets a visual stencil-layer picking workflow, environment-variable support, and expanded EXR compression options.

## Breaking Changes & Migration Notes
- **What breaks:** Legacy ARRI RAW files handled by tutorials using the old SDK path may decode slightly differently once the ARRI SDK 7.0.0 beta path becomes the eventual default in later releases (7.0.0 is beta-only in 13.2; the older 6.2 SDK is still default here).
  **Workaround:** For 13.2, no action needed — 6.2 SDK remains default. Track ARRI SDK defaults in later version notes when the switch to 7.0.0 becomes permanent.
- **What changes visually:** Any tutorial timing/comparing render speed before vs. after 13.2, or describing "scanline rendering," is describing pre-13.2 internals; the top-down node-graph evaluation model is a different rendering strategy and may change apparent render order/caching behavior in complex graphs (though not typically final-pixel results).

## Sources
- https://learn.foundry.com/nuke/content/release_notes/nuke_13.2.html
- https://www.cgchannel.com/2022/04/foundry-ships-nuke-nukex-nuke-studio-nuke-indie-13-2/
- https://www.foundry.com/news-and-awards/nuke-13-2-released
