# Knowledge Gap To-Do List

Generated 2026-08-20 from a library-wide gap analysis (85 ingested tutorials
checked against `SKILL.md` scope + all `references/*.md`). Every gap below was
**measured** — each line records how many tutorial files actually mention the
topic — not guessed. Ingest with `python ingest.py "[URL]"` from this directory,
then run the mandatory extraction pass (see `SKILL.md` Mode 3).

> **How the counts were taken.** Case-insensitive regex over all 85 tutorial
> files (not `INDEX.md`, which counts tags rather than content). Two rounds: the
> first pass over-reported and was corrected by hand, which is the standing rule
> of this program — *suspect the instrument before the data*. Specifically,
> `nuke\.python|nukescripts` matched **0** files and looked like a total gap,
> but `\bnuke\.[a-z]` matches **26** — the Nuke Python API is well covered and
> was nearly listed as missing. Likewise a substring search for `mari` matched
> 15 files, almost all of them noise (`primaries`, `marine`); whole-word `\bmari\b`
> matches **2**. **Re-measure before trusting any number here.**

## Pending

### 1. 🟡 Katana — **6 tutorials** (was ZERO; D4b started 2026-08-24, continued 2026-08-31)

`SKILL.md` advertises Katana ("lookdev/lighting/USD", trigger words `katana`,
`scenegraph`), and `references/katana-lookdev-lighting.md` plus **seven** Katana
release-notes files exist. But **not one ingested tutorial mentions Katana**
(0 of 85 files; the 5 `INDEX.md` hits are tag text only).

This is the single largest hole in the skill: a whole advertised application
with reference files but no ingested source material. It is also the case the
cleanup plan's D4 batch called out as the reason to start here.

> **D4b progress — 6 Foundry doc pages ingested and extracted** (3 on
> 2026-08-24, 3 on 2026-08-31). The "zero tutorials for an advertised
> application" hole is open no longer, but each item below is only partly
> covered. What is ingested is listed per item; what is still missing is left
> unticked and **not guessed at**.

- [~] **Katana fundamentals** — scene graph, Ops/OpScript, Live Groups
      ✅ `opscript-tutorials.md` — `Interface` API: CreateChild and its
      infinite-recursion trap, the three guards (CEL match / location-path
      if-else / `OpArgsBuilders.StaticSceneCreate`), DeleteChild vs
      DeleteChildren vs DeleteSelf, CopyLocationToChild across inputs.
      ✅ `livegroups-and-liveshadinggroups.md` — the LiveGroup node: an external
      Katana project as node contents, reloaded automatically (scene load, before
      batch render) or manually; the source's first root-level Group node defines
      its user parameters and children; `.livegroup` vs `.katana` on disk
      (uncompressed ASCII XML vs a gzip-compressed `.tar`); Publish… /
      Publish and Finish Editing Contents…; the Import Livegroup dialog's
      **Types → macros** option; publishing sources through the Asset API.
      ❌ Still missing: a general scene-graph orientation ("Getting Started"),
      and **LiveShadingGroups** — named in that page's own title and breadcrumb
      but never defined anywhere in its body, so it is recorded as a gap rather
      than inferred.
- [~] **Katana lookdev + lighting workflow** — Material/NetworkMaterial nodes,
      GafferThree, light linking, render passes
      ✅ `gafferthree.md` — the Gaffer object table, lights/rigs/light
      filters/sky domes, Template Materials and Look File materials,
      aim/point/orient constraints, and CEL-based light **and** shadow linking
      with `LightLinkResolve`.
      ✅ `creating-shading-networks.md` — **NetworkMaterialCreate as its own
      topic**: the fixed terminal sidebar (terminals prepopulated per configured
      renderer, versus the older Network Material node where they were added by
      hand), the `Tab` / `Shift`+`Tab` / `S` node menus and their renderer colour
      stripes, type-checked colour-coded port connections, the `Alt`+`1`/`2`/`3`
      view states, Dot-node routing (one input, many outputs), `Alt`+`H` input
      hiding, the `connectionStyle` preference, and the result landing under
      `/root/materials`.
      ✅ `renderoutputdefine.md` — **render passes**: `outputName`
      (`primary` default, `shadow` by convention), the `type` values
      (`color` for beauty/`z`/`P`/`N`/`Ci`, `raw` for a verbatim Display line
      with no colorspace conversion and no tiling, `script`/`prescript` hooks,
      `none` to clear a prior output), `includedByDefault`, and the per-format
      settings — `exrBitDepth` 16 half for colour vs 32 full float for data
      AOVs, `exrCompression` (all lossless bar `Pixar 24`; `Wavelet` ~2:1 even
      on grainy data), `exrOptimize`/`exrType`, `clampOutput`, `colorConvert`,
      `computeStats`, `cameraName`, `locationType`/`renderLocation`.
      ❌ Still missing: the **NetworkMaterialCreate parameter reference**
      (the workflow page defers to it twice), **multiple NetworkMaterials in one
      NetworkMaterialCreate**, and material Look Files end-to-end.
- [~] **Katana + USD** — USD scene assembly in Katana, Hydra viewer
      ✅ `setting-up-usdpreviewsurface-materials.md` — UsdPreviewSurface inside
      NetworkMaterialCreate, the `usdSurface` terminal, MaterialAssign, Hydra
      Viewer preview (Basic Material off; shadows from all/selected lights),
      and UsdUVTexture + `UsdPrimvarReader_float2` (`varname` = `st`).
      ❌ Still missing: **USD scene assembly** (UsdIn and friends), the Hydra
      Viewer as a topic, UsdPrimCreate / UsdSchemaSet, and loading the USD
      plug-ins (referenced as a prerequisite, not ingested).

> **Verified doc URLs for the topics still open above** (all returned HTTP 200
> on 2026-08-31; Foundry's docs are MadCap Flare and the paths are not guessable
> — these were crawled from `Content/learn_katana.html` → `user_guide.html` /
> `reference_guide.html`, since `Data/Tocs/*` 404s and `Data/Search.js` is a
> stemmed index with no usable path list):
>
> | Open topic | URL (prefix `https://learn.foundry.com/katana/Content/`) |
> |---|---|
> | USD scene assembly | `ug/usd/building_usd_scenes.html`, `ug/usd/loading_usdin_assets.html`, `ug/usd/importing_usd_data.html` |
> | Hydra Viewer as a topic | `ug/using_hydra_viewer/using_hydra.html` |
> | UsdPrimCreate / UsdSchemaSet | `rg/usd_nodes/usdprimcreate.html`, `rg/usd_nodes/usdschemaset.html` |
> | USD plug-in loading (prerequisite) | `ug/using_hydra_viewer/usd_load_plugins.html` |
> | NetworkMaterialCreate **parameter reference** | `rg/3d_nodes/networkmaterialcreate.html` |
> | Multiple NetworkMaterials in one node | `ug/adding_assigning_materials/networkmaterialcreate_multi_nm.html` |
> | Assigning materials / MaterialStack | `ug/adding_assigning_materials/material_basics.html`, `ug/adding_assigning_materials/multiple_materials_materialstack_node.html`, `ug/adding_assigning_materials/using_networkmaterialcreate.html` |
> | Launching / performing a render | `ug/rendering_scene/performing_render.html` (8,440 chars — the largest in that section) |
> | Render types | `ug/rendering_scene/render_types.html` |
> | Live / interactive rendering | `ug/rendering_scene/controlling_live_rendering.html` |
> | OpenEXR header metadata | `ug/rendering_scene/openexr_header_metadata.html` |
>
> ⚠️ **`ug/adding_assigning_materials/adding_assigning_materials.html` is a
> 1,893-char section overview, not a topic page** — it was the obvious-looking
> URL for NetworkMaterial and is nearly content-free. The substantive page is
> `creating_shading_networks.html` (11,513 chars, `NetworkMaterial` × 26),
> **ingested 2026-08-31**. Check article length before ingesting a section index.
>
> ⚠️ **Confirmed twice.** The same trap caught render passes: the user-guide
> page `ug/rendering_scene/setting_up_render_pass.html` is **777 characters** and
> only says that RenderOutputDefine is the node used. The real content is the node
> reference `rg/3d_nodes/renderoutputdefine.html` (6,092 chars), **ingested
> 2026-08-31**. The whole `ug/rendering_scene` section is thin — every page
> measured, largest 8,440 chars. **For Katana, `rg/` node references are often the
> substantive source and `ug/` pages the stub** — the opposite of the usual
> guide-vs-reference assumption.
>
> ❗ **`material stylesheet` / `stylesheet` — one of C1's six zero-corroboration
> terms — is still unlocated.** The materials section was the plausible home and
> does not contain it (zero occurrences on any page checked), and every obvious
> path 404s (`ug/material_stylesheets/…`, `ug/stylesheets/…`,
> `rg/3d_nodes/materialstylesheet.html`). Recorded as unlocated, **not** as absent
> from the product.
>
> The full USD node reference index is `rg/usd_nodes/usd_nodes.html` (40 nodes)
> and the USD user-guide index is `ug/usd/usd-katana.html` (45 topics).

### 2. Mari — **2 tutorials** (thin for an advertised application)

Whole-word `\bmari\b` matches **2 of 85** files
(`advanced-character-texturing-in-mari-studio-techniques.md`,
`introduction-to-mari-for-complete-beginners---1-hour-quick-start-guide.md`),
and `\budim\b` also matches only **2**. `references/mari-texturing.md` and five
Mari release-notes files exist against that.

- [ ] **Mari UDIM workflow in depth** — patch management, resolution per UDIM,
      exporting to a renderer
- [ ] **Mari projection painting** — camera projection, image manager, paint
      buffer, and the bake-down to channels

### 3. CopyCat / Cattery — **1 tutorial** (Nuke's ML toolset)

`copycat|cattery|inference` matches **1 of 85**. This is a flagship modern Nuke
feature (train a network on a few hand-done frames, infer the rest) and the
library has effectively nothing on it.

- [ ] **CopyCat training workflow** — data prep, crop, epochs, reading the loss
      curve, when it beats roto by hand
- [ ] **Cattery models** — installing/using pretrained models (upscale, matte,
      depth) via the Inference node

### 4. `menu.py` / `init.py` pipeline customisation — **ZERO**

`menu.py|init.py` matches **0 of 85**. `references/nuke-python-scripting.md`
covers the API itself, and 26 tutorials use `nuke.*` calls — but nothing covers
**where studio customisation actually lives**: plugin paths, menu building,
toolbars, startup scripts.

- [ ] **Nuke startup/customisation** — `init.py` vs `menu.py`, `NUKE_PATH`,
      plugin discovery, adding menus and shortcuts

### 5. Furnace / F_ plugin suite (NukeX) — **ZERO**

`furnace|f_` matches **0 of 85**. Low priority — the Furnace tools are legacy
and partly superseded — but it is a genuine zero in an advertised NukeX area.
Ingest only if a good source appears; do not manufacture coverage.

## Notes on what is NOT a gap

Measured and healthy, recorded so nobody "fills" a gap that does not exist:

| Topic | Files (of 85) |
|---|---|
| Grade / colour correction | 60 |
| Gizmos / toolsets | 53 |
| Roto / RotoPaint | 51 |
| OCIO / ACES / colour management | 51 |
| 3D system / ScanlineRender / raytrace | 29 |
| `nuke.*` Python API | 26 |
| Expressions / TCL | 23 |
| Keying / Keylight / despill | 19 |
| STMaps | 19 |
| Lookdev | 17 |
| Cryptomatte | 14 |
| USD | 13 |
| Nuke Studio / Hiero / timeline | 12 |
| Camera tracking | 12 |
| Deep compositing | 11 |

## Completed

(none yet — this list was created 2026-08-20 and nothing on it has been ingested)
