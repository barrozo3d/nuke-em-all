# Version Tracker

Tracks the current known versions of Foundry's compositing/look-dev suite and when this file was last checked against Foundry's release-notes pages. Mirrors the Auto-Changelog Rule in `SKILL.md` (Mode 0).

- **last_checked:** 2026-08-09

## Known Versions (as of last_checked)

| App | Latest stable | Latest beta | Notes |
|---|---|---|---|
| Nuke / NukeX / Nuke Studio | 17.0 (released 2026-02-26) | 17.1 (open beta, 2026-07) | 17.0: native 3D Gaussian Splats support, new Field nodes (non-destructive 3D/volumetric masking), largest 3D-system overhaul yet (USD import/manipulation, camera/lighting/materials), USD 25.08, VFX Reference Platform 2025. 17.1 beta adds splat relighting and Hydra 2.0 support in the 3D viewer. |
| Mari | 7.5v2 (stable, 2026-02-04) | 8.0 (open beta, 2026-07) | 7.5: up to 8-stream Multi-channel Paint node. 8.0 beta headline feature: A/B wipe comparison between different parts of the node graph (material iteration/variants). |
| Katana | 9.0 (released 2026-03-05) | — | New UsdSuperLayer node (node-graph-level access to a USD Layer, foundation for future USD-native tools), new UsdMaterial node for quick look edits on incoming/converted USD looks, Hydra 2.0 support in alpha (USD + Geolib rendering in one viewer). |

## URL Patterns for Auto-Update

- Nuke/Hiero/Nuke Studio release notes: `https://learn.foundry.com/nuke/content/release_notes.html`
- Mari release notes: check `https://www.foundry.com/products/mari/new-releases` and `https://learn.foundry.com/mari/Content/release_notes/`
- Katana release notes: check `https://www.foundry.com/news-and-awards/` (Foundry announces major Katana versions there) and CG Channel (`cgchannel.com`) tends to cover releases same-week — useful as a fast secondary check.
- General Foundry news/releases: `https://www.foundry.com/news-and-awards`

## Auto-Changelog Rule (Mode 0 — Version Check)

See `SKILL.md` for the full trigger/steps. Summary: if `last_checked` is more than 7 days old at the start of a consultation, fetch the URLs above, diff against the Known Versions table, and if a new version is found, create/update a `references/release-notes-<app>-<version>.md` file, then update this table and `last_checked`.
