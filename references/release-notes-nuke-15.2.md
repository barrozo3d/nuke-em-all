# Nuke 15.2 — Release Notes

**Released:** 2025-02-28 (announced alongside Nuke 16.0; beta posted 2024-12-12)
**Type:** Stable — **parallel release track**: same headline features as Nuke 16.0, but stays on the older VFX Reference Platform for studios not ready to update.
**VFX Reference Platform:** CY2023 (vs. CY2024 used by the simultaneously-released Nuke 16.0)

## Added
- **Multishot workflow foundations — Graph Scope Variables (GSVs)**: define variables/scopes usable across multiple contexts in a single script.
  - **VariableSwitch** node — switch between shots/scopes using variables.
  - **VariableGroup** node — define variables and scopes.
  - **Variables Panel** for interacting with GSVs directly.
  - GSV support extended into LiveGroups and command-line rendering.
- **GroupView** — view multiple Group nodes' contents simultaneously.
- **Link Nodes** — create a linked copy of a node whose changes propagate back to the source, with optional per-copy knob overrides.
- **Roto performance overhaul** — caching, playback, interactivity, and motion blur all sped up significantly.
- **Quick Export** — up to 12x faster compressed-video exports (ProRes, DNxHD, DNxHR, H.264) versus the previous export pipeline.

## Breaking Changes & Migration Notes
- **What breaks:** Nothing 15.2-specific to flag beyond the general multishot/GSV learning curve — this is new functionality, not a removal. Tutorials predating GSVs simply won't reference them; that's fine, GSVs are additive.
  **Workaround:** N/A.
- **Note for the consultant:** Multishot/GSV terminology (VariableSwitch, VariableGroup, GSV) first appears here and in Nuke 16.0 simultaneously — any tutorial mentioning these nodes is necessarily 15.2/16.0 or newer.

## Sources
- https://learn.foundry.com/nuke/content/release_notes/nuke_15.2.html
- https://www.cgchannel.com/2025/02/foundry-releases-nuke-16-0/
