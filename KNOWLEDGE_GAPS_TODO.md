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

### 1. 🟡 Katana — **14 tutorials** (was ZERO; D4b started 2026-08-24, continued 2026-08-31)

`SKILL.md` advertises Katana ("lookdev/lighting/USD", trigger words `katana`,
`scenegraph`), and `references/katana-lookdev-lighting.md` plus **seven** Katana
release-notes files exist. But **not one ingested tutorial mentions Katana**
(0 of 85 files; the 5 `INDEX.md` hits are tag text only).

This is the single largest hole in the skill: a whole advertised application
with reference files but no ingested source material. It is also the case the
cleanup plan's D4 batch called out as the reason to start here.

> **D4b progress — 14 Foundry doc pages ingested and extracted** (3 on
> 2026-08-24, 11 on 2026-08-31). The "zero tutorials for an advertised
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
      ✅ `networkmaterialcreate.md` — the **parameter reference** the workflow
      page defers to twice: `rootLocation` (default `/root/materials`),
      Add NetworkMaterial / Add Namespace and the Material Scenegraph
      (Renderers / Terminals / Interactive / Color; middle-mouse drag;
      Namespaces nest, nothing goes under a NetworkMaterial), and
      **Interface Controls** — `state` visibility/lock, `targetType`,
      `targetName`, `definitionStyle` operator-tree vs conditional state
      expression, and the sixteen comparison ops.
      ✅ `multiple-networkmaterials-with-networkmaterialcreate.md` — **multiple
      NetworkMaterials in one node**: Add NetworkMaterial / Add Namespace,
      middle-mouse arrangement mirrored into the Scene Graph tab and terminal
      sidebar, per-material renderer/terminal counts, interactive state and
      colours — with the measured payoff, **27 nodes → 19 by sharing 8**.
      **The three NetworkMaterial items are now one complete topic across three
      entries** (workflow / parameter reference / multi-material).
      ❌ Still missing: **Node Parameters and Interface Controls** (how a
      parameter is promoted in the first place — the step *before* every
      Interface Control), and material Look Files end-to-end.
- [~] **Katana + USD** — USD scene assembly in Katana, Hydra viewer
      ✅ `setting-up-usdpreviewsurface-materials.md` — UsdPreviewSurface inside
      NetworkMaterialCreate, the `usdSurface` terminal, MaterialAssign, Hydra
      Viewer preview (Basic Material off; shadows from all/selected lights),
      and UsdUVTexture + `UsdPrimvarReader_float2` (`varname` = `st`).
      ✅ `using-native-usd-workflows.md` — **USD scene assembly**: the whole
      native USD node set by family (Composition / Prims / Properties / Output /
      Other / SuperTools), **LIVRPS** composition ordering, `UsdPrimCreate` and
      `UsdSchemaSet` building their UI dynamically from the USD version in use,
      Pattern-Based Collections as the USD analogue of CEL, `UsdLayerWrite`
      (`.usda`) and `UsdPythonWrite` as escape hatches, `UsdToKatana` /
      `KatanaToUsd`, the `UsdGaffer` / `UsdSuperLayer` SuperTools, the Scene
      Explorer's unified USD+Katana scene graph, and USD property inspection in
      the Attributes tab. **This is the orientation map; it defers detail to
      fourteen other pages**, which is what makes the USD node references worth
      ingesting next.
      ✅ `usdschemaset.md` — **`UsdSchemaSet` in depth**: API schemas (names
      ending `API` — `MaterialBindingAPI`, `VisibilityAPI`, `ShadowAPI`,
      `ShapingAPI`) applied to a prim **non-destructively, without altering its
      original type**; the worked ShapingAPI-on-a-DiskLight example; `primPaths`
      order, a `type` list that refreshes in real time (so it covers schemas
      newer than Katana's own set), dynamically generated `properties`, and
      `listPosition` — the USD list-editing semantics append / prepend / delete /
      reset to explicit, where list means the composed result after all layers
      and arcs.
      ✅ `usdprimcreate.md` — **the other half of the pair**: prims at each
      `primPaths` entry in listed order; a `type` dropdown Katana fills by
      interrogating the installed USD version; the `primSpec` specifiers
      `define` / `class` / `over`; and `primSpecHierarchy`, off by default so
      only the final prim takes the specifier and ancestors are created as
      `over` — deliberately, to avoid overwriting lower-layer PrimSpecs. The
      seven derived geometry nodes and `UsdLight`/`UsdCamera`/`UsdScope`/
      `UsdXform` are covered by that entry rather than listed as separate gaps.
      ✅ `importing-usd-data.md` — **importing USD data**: native import leaves
      the data as USD rather than converting to Katana locations/attributes
      (`UsdToKatana` stays available), then a purpose-led guide to the five
      composition arcs — `UsdSubLayerAdd` (whole stages, LayerStacks, root-level
      with no prim path), `UsdPayloadSet` (heavy or animation-free assets, the
      Payload working set, and the trap that **unloaded payloads still render**),
      `UsdReferenceSet`, `UsdInheritSet` (update once, all instances follow) and
      `UsdSpecializeSet` (overrides always beat further references).
      ✅ `composition-arcs---understanding-livrps.md` — **LIVRPS**: the six layer
      types in strength order (Local / Inherits / Variants / References /
      Payloads / Specializes, strongest first), which is what
      `using-native-usd-workflows.md` and `importing-usd-data.md` both deferred
      to. Foundry's per-arc summary, **not** the OpenUSD specification —
      *LIVRPS Strength Ordering* in the USD Glossary remains uningested.
      ✅ `loading-usd-plug-ins-into-katana.md` — **USD plug-in loading**, and the
      answer is that it is a **non-problem on any current Katana**: enabled by
      default since **4.5v1**. The pre-4.5v1 launcher-script setup (three
      variables into `KATANA_ROOT/plugins/Resources/Usd`) is recorded as
      historical. The one non-version-gated fact: it adds a `usd` menu to the
      **NetworkMaterialCreate terminal sidebar**.
      ❌ Still missing: the Hydra Viewer as a topic (**its page is a 1,025-char
      stub and no alternative was locatable**).

> **Verified doc URLs for the topics still open above** (all returned HTTP 200
> on 2026-08-31; Foundry's docs are MadCap Flare and the paths are not guessable
> — these were crawled from `Content/learn_katana.html` → `user_guide.html` /
> `reference_guide.html`, since `Data/Tocs/*` 404s and `Data/Search.js` is a
> stemmed index with no usable path list):
>
> | Open topic | URL (prefix `https://learn.foundry.com/katana/Content/`) |
> |---|---|
> | Hydra Viewer as a topic | ⚠️ **not located** — `ug/using_hydra_viewer/using_hydra.html` is a 1,025-char stub |
> | USD plug-in loading (prerequisite) | `ug/using_hydra_viewer/usd_load_plugins.html` (2,041) |
> | Node Parameters and Interface Controls (parameter promotion) | not yet located — referenced by `rg/3d_nodes/networkmaterialcreate.html` |
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
> ❗ **Three for three, and it now has numbers for the whole USD area.** Every
> remaining candidate was measured on 2026-08-31 before choosing:
>
> | Page | Chars | |
> |---|---|---|
> | `rg/3d_nodes/networkmaterialcreate.html` | **8,074** | ingested |
> | `rg/usd_nodes/usdschemaset.html` | 5,996 | |
> | `ug/usd/native-usd-workflows.html` | 5,361 | |
> | `ug/adding_assigning_materials/networkmaterialcreate_multi_nm.html` | 5,151 | |
> | `ug/usd/what_is_usd.html` | 4,506 | |
> | `rg/usd_nodes/usdprimcreate.html` | 3,914 | |
> | `ug/usd/importing_usd_data.html` | 3,282 | |
> | `ug/using_hydra_viewer/usd_load_plugins.html` | 2,041 | |
> | `ug/usd/loading_usdin_assets.html` | **1,298** | ⚠️ stub |
> | `ug/usd/building_usd_scenes.html` | **1,234** | ⚠️ stub |
> | `ug/using_hydra_viewer/using_hydra.html` | **1,025** | ⚠️ stub |
>
> ⚠️ **Two URLs recorded earlier in this file as targets are stubs.**
> "USD scene assembly" was pointed at `building_usd_scenes.html` (1,234) and
> "Hydra Viewer as a topic" at `using_hydra.html` (1,025). Neither carries the
> content. The substantive USD pages are **`native-usd-workflows.html` (5,361)**
> and **`importing_usd_data.html` (3,282)**; the USD node references
> (`usdschemaset` 5,996, `usdprimcreate` 3,914) are richer than either.
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

> 🔎 **Discovery attempt, 2026-08-31 — what could and could not be found.**
> ✅ **INGESTED 2026-09-01 — `look-file-baking.md`.**
> `ug/look_files/look_file_baking.html` (**2,466 chars**) — the `LookFileBake`
> node, its original/modified inputs, the extra input per output pass, and the
> live-recipe-vs-baked-cache distinction. This was the **last located,
> reachable, substantive Katana page** on this list; Katana **8 → 9** entries.
> Its parent `ug/look_files/look_files.html` is a **1,364-char stub**.
>
> ⚠️ **The topic is only partly closed, and the entry says so in its own scope
> note.** The page is concept-level: it does **not** document the `LookFileBake`
> node's parameters, the on-disk Look File format, or the nodes that read a Look
> File back in — `LookFileAssign`, `LookFileManager`, `LookFileMaterialsIn/Out`
> are not named anywhere in the text. **No page has been located for any of
> them**, and nothing was written from model knowledge to cover the gap.
> - [ ] **Look File read-back nodes** — `LookFileAssign`, `LookFileManager`,
>       `LookFileMaterialsIn` / `LookFileMaterialsOut`. Likely under
>       `rg/3d_nodes/`, which **cannot be crawled** (see the warning below), so
>       this needs a different entry point than the one that found the rest.
>
> **Confirmed NOT locatable**, after specific attempts rather than assumption:
> * **Node Parameters and Interface Controls** (parameter promotion). The obvious
>   candidate `ug/working_with_nodes/node_parameter_basics.html` is substantive at
>   **6,474 chars** but was measured for the actual terms and contains
>   **zero** occurrences of *promot\**, *Interface Control*, *user parameter* or
>   *Edit User Parameters*. It is a different topic. `rg/3d_nodes/networkmaterial\
>   interfacecontrols.html` 404s.
> * **LiveShadingGroups** — four path guesses under `ug/livegroups/` and
>   `rg/misc_nodes/` all 404.
> * **Hydra Viewer as a topic** — `hydra_viewer.html` and
>   `using_the_hydra_viewer.html` both 404; only the 1,025-char stub exists.
>
> ⚠️ `rg/3d_nodes/3d_nodes.html` **cannot be crawled** — it returns 26KB with
> **zero** `.html` links, so its node list is built client-side. The
> `Content/learn_katana.html` → `user_guide.html` / `reference_guide.html` route
> does not reach it. Any future search for a 3D node reference page needs a
> different entry point.

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

### 3. 🟡 CopyCat / Cattery — **2 tutorials** (was 1, and that 1 was not real)

> **2026-09-04 — partly closed, and the old count was wrong.** This item read
> "1 tutorial". Re-measured against the 100 files as they stood: `copycat|cattery|inference`
> matched **0** in tutorial *bodies*. The 1 was an `INDEX.md` tag hit, which this
> file's own header warns about ("INDEX.md, which counts tags rather than
> content"). The gap was a true zero, slightly worse than recorded.
>
> Two Foundry reference-guide pages ingested and extracted (text-only):
> `copycat.md` and `inference.md`.

- [x] **CopyCat training workflow** — data prep, crop, epochs, reading the loss
      curve, when it beats roto by hand
      ✅ `copycat.md` — **NukeX and Nuke Studio only** (absent from base Nuke).
      Input / Ground Truth / Preview (Preview is held *outside* the data set and
      only appears once the first two are connected); `Total Steps = Epochs *
      Data Set / Batch Size`; Epochs default 10000; Batch Size Auto or manual
      (docs report 4–16 typical, must be ≤ the number of image pairs); Crop Size
      256 and named as the first knob to reduce when memory or time bites; Model
      Size small/medium/large; Initial Weights None / Checkpoint / Deblur /
      Upscale / Human Matting; multi-resolution training (up to 2× faster, three
      stages at 1/4, 1/2 and full res, **disable above ~100 pairs**, and stopping
      early can mean the model never trains at full resolution); checkpoint `.cat`
      every 1000 steps and contact-sheet `.png` every 100; the Progress tab's
      Step/Loss curve with Log Scale, Smoothness 0.6 and Show Original Curve.
- [~] **Cattery models** — installing/using pretrained models (upscale, matte,
      depth) via the Inference node
      ✅ `inference.md` — the **applying** half: Model File, read-only Channels
      In/Out, GPU controls, and Optimize for Speed and Memory (16-bit half float
      instead of 32-bit — faster, less GPU memory, larger images, artifacts with
      some networks). Two placement facts worth keeping: Inference is **not**
      NukeX-restricted, so a `.cat` trained on a NukeX seat applies on a base
      Nuke seat; and the timeline version of the node drops the GPU controls.
      Also names *Import Pre-Trained PyTorch Models* as the route for externally
      trained models.
      ❌ Still missing: **the Cattery library itself** — browsing or downloading
      Foundry's pretrained community models, where the downloaded files install
      on the plug-in path, and the per-model notes those downloads carry.
      CopyCat's Deblur/Upscale/Human Matting weightings are pretrained starting
      points for *training* and are **not** the Cattery catalogue; treating them
      as the same thing would be manufacturing coverage. A coverage note in
      `inference.md` records this too, so the entry cannot be misread as complete.

### 4. ✅ `menu.py` / `init.py` pipeline customisation — **CLOSED 2026-09-04** (was ZERO)

Three Foundry Python dev-guide pages ingested and extracted (text-only), taking
`menu.py|init.py` from **0 of 85** to **3 of 100**:

- [x] **Nuke startup/customisation** — `init.py` vs `menu.py`, `NUKE_PATH`,
      plugin discovery, adding menus and shortcuts
      ✅ `start-up-scripts.md` — the evaluation order (initialization scripts run
      in **reverse** plug-in-path order, so `~/.nuke` runs last and overrides
      facility settings), `init.py` in every session including command-line
      renders vs `menu.py` in interactive sessions only, and the rule that UI
      code in `init.py` "may lead to errors or prevent NUKE from launching".
      `nuke.pluginPath()` / `pluginAddPath()` (prefix) / `pluginAppendPath()`
      (append) / `NUKE_PATH`.
      ✅ `installing-plug-ins.md` — `~/.nuke`, typed sub-directories registered
      from `init.py`, a shared network repository via `NUKE_PATH`, the `menu.py`
      `addCommand` + `nuke.createNode` entry that makes a gizmo clickable,
      per-user (`os.getenv("USER")`) and per-show (`SHOW`) path patterns guarded
      by `os.path.isdir`, and the explicit warning never to install into Nuke's
      own application directory.
      ✅ `customizing-the-ui.md` — the eight addressable menus (Nuke, Windows,
      Nodes, Properties, Animation, Viewer, Node Graph, Axis), `nuke.menu` /
      `nuke.toolbar` / `addMenu` / `addCommand` / `addSeparator` / `findItem` /
      `invoke` / `setEnabled`, icons and `index=`, hotkey modifiers (`ctrl+`/`^`,
      `alt+`/`#`, `shift+`/`+`), and `nuke.knobDefault`. Two traps recorded:
      binding a hotkey means **replacing the whole menu item**, and an item
      disabled with `setEnabled(False)` **keeps firing its hotkey**.

> ⚠️ **Ingest lesson — the Nuke dev guide puts site chrome in its `<title>`.**
> The first collect landed as `start-up-scripts-nuke-python-api-reference.md`
> ("Start-up Scripts — Nuke Python API Reference"). A slug built from chrome is
> frozen identity the moment it is committed, so the collect was **reverted** and
> re-run with `--title "Start-up Scripts"`. **Always pass `--title` for
> `learn.foundry.com/nuke/developers/**` pages.** The *reference guide*
> (`/nuke/content/reference_guide/**`, e.g. CopyCat, Inference) and the Katana
> docs carry clean titles and need no override — the difference is per-doc-set,
> not per-site.

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
