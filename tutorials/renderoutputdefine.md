---
title: RenderOutputDefine
source: Article
url: https://learn.foundry.com/katana/Content/rg/3d_nodes/renderoutputdefine.html
author: learn.foundry.com
ingested: 2026-08-31
app: Katana
version: 9.0v3
tags: [katana, aovs, channels, katana-9, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/renderoutputdefine/
frame_count: 0
frame_status: skipped
---

# RenderOutputDefine

**Source:** [Article](https://learn.foundry.com/katana/Content/rg/3d_nodes/renderoutputdefine.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** RenderOutputDefine Specifies output of an image (color, AOV, shadow map, or similar) to a file. In RIB, this means a Display statement. Connection Type Connection Name Function Input input The place in the node graph where you want to define the output settings for rendering. Control (UI) Default Value Function outputName primary Associates a name with the display. Typically primary by default; often shadow for shadow maps, and similar conventions. This name appears in the Render node, along with (or as) the default primary . type color Specifies the type of output. • color - mostly used to render out rgb beauty files, but also can be used for rendering out z, P(point), N(normals), Ci(final shader color) passes. • raw - allows you to directly specify the values for a Display line. Since the output could be anything, Katana doesn't do any colorspace conversion on this output, and can't support tiling. • script - run a script on another RenderOutputDefine, like txmake. • prescript - run a script before the render is started. • none - clears the output. If the output was previously setup by a different RenderOutputDefine node, this removes the entry. includedByDefault Yes When enabled, this Render Definition is sent to the Render node. rendererSettings colorSpace linear Sets the output colorspace used. fileExtension exr Sets the output file format. channel rgba Sets the channels to output. You can also set a user-defined channel from a PrmanOutputChannelDefine node. When fileExtension: exr; convertSettings exrCompression Scanline ZIP Defines the exr compression method to use. All methods are lossless (with the exception of Pixar 24 , which is lossless but quantizes the pixels to 24-bit float). Wavelet is generally preferable as it offers ~2:1 compression even on grainy data. • None - • RLE - • Scanline ZIP - • Block ZIP - • Wavelet - • Pixar 24 - exrBitDepth 16 Sets the floating point precision of the rendered exr file: • 16 - half float. This is recommended for all color passes. • 32 - full float. This is recommended for all ncf data arbitrary output variables (AOVs). exrOptimize Yes When enabled, the exr file is written out in an a manner optimized for efficient random tile-access. These optimizations greatly improve memory usage and performance for programs, which process images in tiles. exrType Tiled Sets whether the exr file is written to support: • Tiled - random tile access. • Scanline - random scanline access. When fileExtension: exr clampOutput No When set to Yes , post-render clamp negative rgb values to 0, and clamp alpha values to 0-1. Note: clampOutput has no effect on NaN and inf values. colorConvert Yes When set to Yes , post-render convert rendered image data from linear to the output colorspace specified in the filename. The default value of Yes is suitable for nearly every situation, since the linear output of the render is converted to the colorspace in the filename. A case where you would want to set this to No is if you know the data being rendered is in a colorspace other than linear, such as the re-projection of a log plate, and you want to name the output file log without a linear to log conversion. When fileExtension: png; convertSettings pngBitDepth 16 Sets the bit depth of the rendered file: • 8-bit • 16-bit When fileExtention: rla; convertSettings rlaBitDepth 16 Sets the bit depth of the rendered file: • 8-bit • 10-bit • 16-bit • 32-bit When fileExtention: tif; convertSettings tifBitDepth 16 The bit depth of the rendered file: • 8-bit • 16-bit • 32-bit tifCompression LZW The tif compression method to use: • None - No compression method is used. • LZW - The LZW compression method is used. This is lossless, so it is usually preferable to use it unless there is an issue with compatibility in the target reader. When fileExtension: tif clampOutput No When set to Yes , post-render clamp negative rgb values to 0, and clamp alpha values to 0-1. Note: clampOutout has no effect on NaN and inf values. colorConvert Yes When set to Yes , post-render convert rendered image data from linear to the output colorspace specified in the filename. The default value of Yes is suitable for nearly every situation, since the linear output of the render is converted to the colorspace in the filename. A case where you would want to set this to No is if you know the data being rendered is in a colorspace other than linear, such as the re-projection of a log plate, and you want to name the output file log without a linear to log conversion. When fileExtension: jpg jpgQuality 100 The quality to use when generating the jpg file. Higher values generate larger file sizes, with 100 representing the best quality image and 0 representing the lowest. rendererSettings parameters continued computeStats None Allows you to compute image statistics as a post process, appending as exr metadata. Select: • None • Raw • Depth Note: In depth mode, zero values and very large values are ignored. In both modes, only the region within the dataWindow is considered. tempRenderLocation N/A cameraName N/A Describes the scene graph location of camera to render from. If empty, render from the camera specified in renderSettings.cameraName at /root . The cameraName parameter options are available by clicking the dropdown menu. For more information, refer to the Scene Graph Location Widget Type in Common Parameter Widgets . locationType local When locationType: file; locationSettings renderLocation Specify the render location, or bring up the file browser or your studio's asset management browser to select the location to use. For more information, refer to the Asset and File Path Widget Types in the Common Parameter Widgets . Note: RenderOutputLocation plug-ins that are shipped as source and can be found in plugins/Src/RenderOutputLocations . Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
Defining a render output — a beauty pass, an AOV, a shadow map or a script hook — with Katana's **RenderOutputDefine** node, including the per-format file settings (EXR compression, bit depth, tiling) that decide what the compositor downstream actually receives.

### Summary
RenderOutputDefine specifies the output of an image to a file; in RIB terms it authors a `Display` statement. Each node names one output (`primary` by default, `shadow` for shadow maps by convention), picks a `type` that decides whether it is a rendered pass, a raw Display line, or a script hook, and then exposes a per-file-format settings block — EXR, PNG, RLA, TIF and JPG each expose different controls. The page is where the render-pass conventions live: which bit depth to use for colour versus data AOVs, which EXR compression is safe, and when `colorConvert` should be turned off.

### Key Steps
1. Place a **RenderOutputDefine** node at the point in the node graph where the output should be defined; its single `input` carries the scene it applies to.
2. Set **`outputName`** — `primary` by default (the beauty/default pass), conventionally `shadow` for shadow maps. This name is what appears in the **Render** node.
3. Choose **`type`**: `color` for rendered passes, `raw` to write a Display line verbatim, `script` / `prescript` for script hooks, or `none` to clear an output a previous RenderOutputDefine established.
4. Leave **`includedByDefault`** on (`Yes`) so the Render Definition is sent to the Render node; turn it off for outputs that should exist but not render by default.
5. Under **`rendererSettings`**, set `colorSpace` (default `linear`), `fileExtension` (default `exr`) and `channel` (default `rgba`) — a user-defined channel can come from a **PrmanOutputChannelDefine** node.
6. For EXR, set the `convertSettings`: `exrCompression`, **`exrBitDepth` — 16 (half) for colour passes, 32 (full float) for data AOVs**, `exrOptimize` for tile-access efficiency, and `exrType` (Tiled or Scanline).
7. Decide the two post-render controls: **`clampOutput`** (clamps negative RGB to 0 and alpha to 0–1 — no effect on NaN/inf) and **`colorConvert`** (linear → the colorspace named in the filename).
8. Optionally set **`computeStats`** (`None` / `Raw` / `Depth`) to append image statistics to the EXR metadata as a post process.
9. Point the output at a camera with **`cameraName`** — leave it empty to inherit `renderSettings.cameraName` at `/root`.
10. Set **`locationType`**; with `file`, use `locationSettings → renderLocation` to pick the path via the file browser or the studio's asset-management browser.

### Nodes / Tools / Settings
**Node:** `RenderOutputDefine` — "Specifies output of an image (color, AOV, shadow map, or similar) to a file. In RIB, this means a `Display` statement."
**Input:** `input` — the place in the node graph where the output settings are defined.

**Top-level controls:**

| Control | Default | Function |
|---|---|---|
| `outputName` | `primary` | Associates a name with the display. Typically `primary`; often `shadow` for shadow maps. Appears in the Render node. |
| `type` | `color` | See the table below. |
| `includedByDefault` | `Yes` | When enabled, this Render Definition is sent to the Render node. |

**`type` values:**
- `color` — mostly rgb beauty files, but also `z`, `P` (point), `N` (normals) and `Ci` (final shader colour) passes.
- `raw` — directly specify the values for a Display line. Because the output could be anything, Katana does **no colorspace conversion** and **cannot support tiling**.
- `script` — run a script on another RenderOutputDefine, such as `txmake`.
- `prescript` — run a script before the render is started.
- `none` — clears the output; removes an entry a different RenderOutputDefine previously set up.

**`rendererSettings`:** `colorSpace` = `linear` · `fileExtension` = `exr` · `channel` = `rgba` (a user-defined channel can be set from a **PrmanOutputChannelDefine** node) · `computeStats` = `None` | `Raw` | `Depth` (appends image statistics as EXR metadata as a post process; in Depth mode zero and very large values are ignored, and in both modes only the region within the `dataWindow` is considered) · `tempRenderLocation` · `cameraName` (scene graph location of the camera; **if empty, renders from the camera in `renderSettings.cameraName` at `/root`**).

**EXR `convertSettings` (`fileExtension: exr`):**
- `exrCompression` = `Scanline ZIP` — options `None`, `RLE`, `Scanline ZIP`, `Block ZIP`, `Wavelet`, `Pixar 24`. **All lossless except `Pixar 24`**, which is lossless but quantizes pixels to 24-bit float. **`Wavelet` is generally preferable — roughly 2:1 even on grainy data.**
- `exrBitDepth` = `16` — **`16` (half float) recommended for all colour passes; `32` (full float) recommended for all ncf data arbitrary output variables (AOVs).**
- `exrOptimize` = `Yes` — writes the file optimized for efficient random tile-access, greatly improving memory use and performance for programs that process images in tiles.
- `exrType` = `Tiled` — `Tiled` (random tile access) or `Scanline` (random scanline access).

**Post-render controls (EXR and TIF):**
- `clampOutput` = `No` — post-render, clamp negative rgb values to 0 and alpha to 0–1. ⚠️ **No effect on NaN and inf values.**
- `colorConvert` = `Yes` — post-render, convert rendered image data from linear to the output colorspace specified *in the filename*. The default suits nearly every situation. **Set it to `No` when the data being rendered is already in another colorspace** — the page's example is the re-projection of a log plate that should be named `log` without a linear→log conversion.

**Other file formats:** `pngBitDepth` = `16` (8 / 16) · `rlaBitDepth` = `16` (8 / 10 / 16 / 32) · `tifBitDepth` = `16` (8 / 16 / 32) with `tifCompression` = `LZW` (`None` or `LZW`; LZW is lossless and usually preferable unless the target reader has a compatibility issue) · `jpgQuality` = `100` (100 best, 0 lowest).

**Location:** `locationType` = `local`; with `file`, `locationSettings → renderLocation` takes a path, the file browser, or the studio's asset-management browser. **RenderOutputLocation plug-ins ship as source in `plugins/Src/RenderOutputLocations`.**

**Referenced widget docs (not ingested):** the Scene Graph Location Widget Type and the Asset and File Path Widget Types, both in *Common Parameter Widgets*.

### Difficulty
Intermediate

### Foundry App & Version
Katana 9.0v3 (page served from the current Katana 9.0v3 documentation set)

### Tags
katana, aovs, channels, katana-9, intermediate

---

## Scope note — what this page does and does not cover

This is the **node parameter reference**. The user-guide page it belongs to,
*Setting up a Render Pass*, is **777 characters** and says only that
RenderOutputDefine is the node used to define render outputs — so this reference
is where the render-pass knowledge actually lives, and it is what was ingested.

Not covered here and not ingested: how a render is actually launched
(`performing_render.html`), interactive/live rendering
(`controlling_live_rendering.html`), render types
(`render_types.html`), and the OpenEXR header metadata page. All are recorded with
verified URLs in `KNOWLEDGE_GAPS_TODO.md`. The whole `ug/rendering_scene` section
is thin — the largest page in it is 8,440 characters.

---

## Related Tutorials
- [Compositing with EXR Files | FREE VFX Explosions](compositing-with-exr-files-free-vfx-explosions.md) — shares `channels` + `aovs`; **the other end of the same pipe.** The `exrBitDepth`, `exrCompression` and `exrType` settings defined here are precisely what determines the EXR that Nuke tutorial opens and unpacks.
- [Shuffle and Channel Management | Nuke Compositing](shuffle-and-channel-management-nuke-compositing-beginner-intermediate.md) — shares `channels` + `aovs`; the `channel` parameter and any PrmanOutputChannelDefine channels written here are the channels Shuffle addresses downstream — Katana decides what exists, Nuke decides what is used.
- [GafferThree](gafferthree.md) — shares `katana` + `katana-9`; GafferThree builds the lights, and `outputName: shadow` is the conventional output for the shadow maps those lights cast.
- [Creating Shading Networks](creating-shading-networks.md) — shares `katana` + `katana-9`; the `Ci` (final shader colour) pass this node can output is the result of the NetworkMaterialCreate shading network built there.
- [NetworkMaterialCreate](networkmaterialcreate.md) — shares `katana` + `katana-9`; the `Ci` (final shader colour) pass defined here is the rendered output of the material that node builds.
