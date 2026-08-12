# Version Tracker

Tracks the current known versions of Foundry's compositing/look-dev suite and when this file was last checked against Foundry's release-notes pages. Mirrors the Auto-Changelog Rule in `SKILL.md` (Mode 0).

- **last_checked:** 2026-08-12

## Known Versions (as of last_checked)

| App | Latest stable | Latest beta |
|---|---|---|
| Nuke / NukeX / Nuke Studio | 17.0 (2026-02-26) | 17.1 (open beta, 2026-07-02) |
| Mari | 7.5v2 (2026-02-04) | 8.0 (open beta, 2026-07-02) |
| Katana | 9.0 (2026-02-18) | — |

> **Correction from prior tracker version:** the previous entry listed Katana 9.0 as released 2026-03-05. Cross-checked against CG Channel, Animation World Network, and Foundry's own `whats_new_9.0.html` — the confirmed release date is **2026-02-18**. All other prior entries (Nuke 17.0 = 2026-02-26, Mari 7.5v2 = 2026-02-04) were verified correct against official/secondary sources and are unchanged.

## Nuke / NukeX / Nuke Studio (+ Hiero)

| Version | Release Date | Type | Headline Changes | Details |
|---|---|---|---|---|
| 13.0 | 2021-03-17 | Stable | AIR ML toolset (CopyCat, Inference, Deblur, Upscale) launches; Hydra viewer; native Cryptomatte; initial USD (Camera/Light/Axis) load support | [release-notes-nuke-13.0.md](release-notes-nuke-13.0.md) |
| 13.1 | 2021-11-23 | Stable | UnrealReader (beta); full 3D UX redesign; OCIO v2 + ACES 1.2; Encryptomatte; CatFileCreator (PyTorch model import) | [release-notes-nuke-13.1.md](release-notes-nuke-13.1.md) |
| 13.2 | 2022-04-14 | Stable | Top-down node graph rendering (~20% faster); CopyCat multi-GPU training; NDI streaming; OTIO beta in Nuke Studio | [release-notes-nuke-13.2.md](release-notes-nuke-13.2.md) |
| 14.0 | 2022-12-07 | Stable | New USD-based 3D system (beta, parallel to Classic 3D); The Cattery ML model library; UnrealReader out of beta; VFX Ref Platform CY2022 | [release-notes-nuke-14.0.md](release-notes-nuke-14.0.md) |
| 14.1 | 2023-10-13 | Stable (parallel to 15.0, CY2022 platform) | Same feature set as 15.0 minus Apple Silicon native support; GeoMerge redesign; Timeline Disk Cache automation | [release-notes-nuke-14.1.md](release-notes-nuke-14.1.md) |
| 15.0 | 2023-10-13 | Stable | Native Apple Silicon support; CY2023 platform (CentOS 7 → Rocky Linux 9 minimum OS); 64K planar images; OpenAssetIO tech preview | [release-notes-nuke-15.0.md](release-notes-nuke-15.0.md) |
| 15.1 | 2024-06-14 | Stable | USD 3D time-remapping; full OTIO roundtrip; BlinkScript 4-layer channel mapping | [release-notes-nuke-15.1.md](release-notes-nuke-15.1.md) |
| 15.2 | 2025-02-28 | Stable (parallel to 16.0, CY2023 platform) | Graph Scope Variables (GSVs) + Multishot workflow foundations debut; Link Nodes; Quick Export (12x faster) | [release-notes-nuke-15.2.md](release-notes-nuke-15.2.md) |
| 16.0 | 2025-02-28 | Stable | Native Multishot compositing (GSVs mainlined); Roto performance overhaul; macOS moves to FoundryGL (from system OpenGL); Geo modifier default changes ("All" vs "LastModified") | [release-notes-nuke-16.0.md](release-notes-nuke-16.0.md) |
| 16.1 | 2026-02-26 | Stable (parallel to 17.0, CY2024 platform) | New USD 3D system exits beta; initial MaterialX support (MtlXStandardSurface); BigCat large-scale ML training; BasicSurface replaces BasicMaterial in new 3D system | [release-notes-nuke-16.1.md](release-notes-nuke-16.1.md) |
| 17.0 | 2026-02-26 | Stable | **Native 3D Gaussian Splat support** (GeoImport/GeoReference + SplatRender); **Field nodes** (non-destructive volumetric masking of splats/3D data); USD 25.08; CY2025 platform | [release-notes-nuke-17.0.md](release-notes-nuke-17.0.md) |
| 17.1 | 2026-07-02 | Open Beta | Animated Gaussian Splats (GeoSequencer); splat relighting (Direct/Point/Spot lights) in SplatRender; **Hydra 2.0** in the 3D viewer; non-destructive USD export (sublayers/overs); Nuke Studio Compare Versions | [release-notes-nuke-17.1.md](release-notes-nuke-17.1.md) |

## Mari

| Version | Release Date | Type | Headline Changes | Details |
|---|---|---|---|---|
| 6.0 | 2022-12-14 | Stable | Roller Brush; USD material authoring (Arnold/RenderMan shaders); perpetual licenses discontinued for new purchases (subscription-only) | [release-notes-mari-6.0.md](release-notes-mari-6.0.md) |
| 7.0 | 2023-12-04 (v2: 2024-03-12) | Stable | The Bakery (Vulkan GPU baking engine replaces old baker); Bubbles/Camouflage procedurals; automatic project backups | [release-notes-mari-7.0.md](release-notes-mari-7.0.md) |
| 7.1 | 2024-12-09 | Stable | 2D Paint Mode (native, no external app needed); Switch node for texture variants; "Custom Procedurals" renamed to "Smart Masks" | [release-notes-mari-7.1.md](release-notes-mari-7.1.md) |
| 7.5 | 2025-12-03 (v2: 2026-02-04) | Stable | **Multi-Paint: up to 8-channel simultaneous painting** (built with Wētā FX); Texture Transfer (Bakery UV-remap feature); Windows 10 support dropped (Win 11 required) | [release-notes-mari-7.5.md](release-notes-mari-7.5.md) |
| 8.0 | 2026-07-02 | Open Beta | A/B wipe Compare node; Hex Tile node; Color Remap node; 49 new math nodes; CY2025 platform (skips CY2024) | [release-notes-mari-8.0.md](release-notes-mari-8.0.md) |

## Katana

| Version | Release Date | Type | Headline Changes | Details |
|---|---|---|---|---|
| 6.0 | 2022-12-16 | Stable | Material Soloing; Performance tab with heat-map overlay; LiveShadingGroups; "Defaults" subtab replaced by "Parameters" | [release-notes-katana-6.0.md](release-notes-katana-6.0.md) |
| 6.5 | 2023-11-01 | Stable (parallel to 7.0) | Native USD workflow nodes debut (UsdActiveSet family); Scene Explorer USD support; Geolib3-MT (Experimental) removed | [release-notes-katana-6.5.md](release-notes-katana-6.5.md) |
| 7.0 | 2023-11-01 | Stable | Native USD framework goes mainline; Live Rendering ~2x faster; native USD nodes get distinct blue styling in Node Graph | [release-notes-katana-7.0.md](release-notes-katana-7.0.md) |
| 7.5 | 2024-12-09 | Stable (parallel to 8.0) | USD native exporting debuts (UsdLayerDefine/UsdLayerExport, KatanaToUsd); Pattern-Based Collections; Node Graph traversal ported Python→C++ (custom-action compat risk) | [release-notes-katana-7.5.md](release-notes-katana-7.5.md) |
| 8.0 | 2024-12-10 | Stable | Same USD export toolset as 7.5 on CY2024 platform; `onTraversalVisit()` deprecated (use NodeTypeBuilder); GeolibRuntimeTransaction now interface-only | [release-notes-katana-8.0.md](release-notes-katana-8.0.md) |
| 8.5 | 2026-02-18 | Stable (parallel to 9.0) | UsdSuperLayer/UsdGaffer/UsdMaterial nodes debut; Hydra 2.0 experimental preview (Viewer + Scene Browser tabs) | [release-notes-katana-8.5.md](release-notes-katana-8.5.md) |
| 9.0 | 2026-02-18 | Stable | **UsdSuperLayer** node-graph-level USD Layer access (Python API-accessible, foundation for future USD-native tools); UsdMaterial for quick look edits; Hydra 2.0 alpha (`KATANA_ENABLE_HYDRA2`, no Geolib-attribute parity yet); rental-only licensing | [release-notes-katana-9.0.md](release-notes-katana-9.0.md) |

## URL Patterns for Auto-Update

- Nuke/Hiero/Nuke Studio release notes: `https://learn.foundry.com/nuke/content/release_notes.html` (per-version pages live at `release_notes/nuke_<version>.html`)
- Mari release notes: check `https://www.foundry.com/products/mari/new-releases` (redirects to `https://campaigns.foundry.com/products/mari/whats-new`) and `https://learn.foundry.com/mari/Content/release_notes/`
- Katana release notes: `https://learn.foundry.com/katana/content/release_notes.html` (per-version pages live at `release_notes/whats_new_<version>.html`) — also check `https://www.foundry.com/news-and-awards/` for major-version announcements and CG Channel (`cgchannel.com`), which tends to cover releases same-week with precise dates in the article byline/URL — useful as a fast secondary check when Foundry's own marketing pages omit exact release dates (they often do).
- General Foundry news/releases: `https://www.foundry.com/news-and-awards`

## Auto-Changelog Rule (Mode 0 — Version Check)

See `SKILL.md` for the full trigger/steps. Summary: if `last_checked` is more than 7 days old at the start of a consultation, fetch the URLs above, diff against the Known Versions tables, and if a new version is found, create/update a `references/release-notes-<app>-<version>.md` file, then update the relevant table row and `last_checked`.

**Pattern to remember when checking for new versions:** Foundry consistently ships each major/minor release as a **pair** — the new version on the current VFX Reference Platform, plus a parallel release (Nuke `x.1`/`x.2`, Katana `x.5`) carrying the same features but pinned to the prior platform generation. Both usually ship the same day. Check for both when a new version lands.
