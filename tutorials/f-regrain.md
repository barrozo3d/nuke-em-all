---
title: F_ReGrain
source: Article
url: file:///C:/Program%20Files/Nuke17.1v1/Documentation/html/content/reference_guide/furnacecore_nodes/f_regrain.html
author: Nuke 17.1v1 bundled documentation
ingested: 2026-09-04
app: "NukeX (FurnaceCore)"
version: "Nuke 17.1v1 (bundled documentation, Documentation/html/content)"
tags: [furnace, nukex, grain, nuke-17, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/f-regrain/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# F_ReGrain

**Source:** [Article](file:///C:/Program%20Files/Nuke17.1v1/Documentation/html/content/reference_guide/furnacecore_nodes/f_regrain.html)
**Author:** Nuke 17.1v1 bundled documentation
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** F_ReGrain F_ReGrain is used to add grain to a sequence. It is designed to sample an area of grain from one image and then to generate unlimited amounts of this grain with exactly the same statistics as the original. This new grain can then be applied to another image. See also Grain and ScannedGrain . Inputs and Controls Connection Type Connection Name Function Input Grain The image from which grain is sampled. When a Grain input is supplied, F_ReGrain automatically switches to using grain sampled from this input. However, the supplied grain stocks are still available. Src The image to which the grain is added. Control (UI) Knob (Scripting) Default Value Function F_ReGrain Tab Grain Type grainType Preset Stock Selects whether the grain is sampled from the Grain input or from a set of standard stocks. • Preset Stock - grain characteristics are sampled from the film stock specified in the Preset Stock field. • From Grain Clip - samples and reconstructs the grain characteristics from the Grain input. Preset Stock presetStock FUJIF250under 2K The film stock that grain characteristics are sampled from when Grain Type is set to Preset Stock . Grain Amount amount 1 Adjusts the brightness of the grain. Setting this to 0 adds no grain. Grain Size size 1 Adjusts the size of the grain granules. The larger the value, the bigger and softer the granules. Output output Result Sets whether to render the result or a test image. • Result - shows the Src input with the grain applied. • Grain Plate - shows a test image with the grain applied. This test image is composed from a section of the input image surrounded by a uniform solid color sampled from the image with the grain applied. If the inner area is indistinguishable from the outer area, then you have a good grain sample. Analyse analyse N/A Click to begin analysis of the source. Press this button if the input clip from which the grain was analyzed has changed, but you do not want to move the analysis region to trigger re-analysis. Note: A warning displays when the input clip changes. Analysis Region Analysis Region BL regionBL N/A A selection box that marks the region of image used to analyze the grain when Grain Type is set to From Grain Clip . This part of the frame must contain no image detail, only grain. • Analysis Region BL - controls the position of the bottom left corner of the analysis region. • Analysis Region TR - controls the position of the top right corner of the analysis region. Analysis Region TR regionTR N/A Analysis Frame frame 1 Sets the frame to sample the grain from. Grain Colour Space grainColourSpace sRGB This tells F_ReGrain what color space the grain sample clip was in when the grain originated. Setting this correctly ensures that the grain is not exaggerated by any color space conversions prior to sampling. • Cineon • sRGB • Linear Advanced Process Red processRed enabled Disable this if you do not want to process the red channel. Red Amount redAmount 1 Sets the brightness of the grain in the red channel. Red Size redSize 1 Adjusts the size of the grain granules in the red channel. Process Green processGreen enabled Disable this if you do not want to process the green channel. Green Amount greenAmount 1 Sets the brightness of the grain in the green channel. Green Size greenSize 1 Adjusts the size of the grain granules in the green channel. Process Blue processBlue enabled Disable this if you do not want to process the blue channel. Blue Amount blueAmount 1 Sets the brightness of the grain in the blue channel. Blue Size blueSize 1 Adjusts the size of the grain granules in the blue channel. Advanced Grain Response Apply Grain In srcColourSpace Grain Colour Space Sets what color space the grain sample is re-applied to the image: • Cineon / sRGB / Linear - the grain sample is applied in the specified space. • Grain Colour Space - the grain sample is applied in the color space set in the Analysis Range Grain Colour Space field. Low Gain lowGain 1 Adjusts the gain of the grain in the lowlights. Mid Gain midGain 1 Adjusts the gain of the grain in the midtones. High Gain highGain 1 Adjusts the gain of the grain in the highlights. Use Sampled Response useResponse disabled Enable this control to scale the brightness of the grain as a function of the luminance of the Grain image. Sampled Response Mix responseMix 1 Decreasing the Sampled Response Mix control reduces the effect of the response curves until, at 0, they have no effect on the output. Note: This control is only available if Use Sampled Response is enabled. Sample Grain Response sample N/A Click to update the response curves from the current frame. Multiple clicks accumulate the grain response rather than resetting every time. Note: This control is only available if Use Sampled Response is enabled. Reset Grain Response reset N/A Click to reset the grain curves to their default (flat) response. Note: This control is only available if Use Sampled Response is enabled. Draw Response drawResponse disabled Overlay the response curves on the bottom left corner of the viewer. Note: This control is only available if Use Sampled Response is enabled. About about N/A Displays a dialog containing information about this node. Step-by-Step Guides Using F_ReGrain Nuke 17.1v1 docs:



---

## Structured Notes

### Core Technique
Sample grain from a clean, detail-free patch of one image — or from a supplied film stock preset — and synthesise unlimited grain with the same statistics onto another image.

### Summary
F_ReGrain is the classic regrain workflow: match the grain of a plate onto a CG element so the two sit in the same stock. It works either from a **Grain** input (sampling an **Analysis Region** that must contain *only grain, no image detail*) or from a **Preset Stock** list, defaulting to `FUJIF250under 2K`, and it switches to the sampled route automatically when a Grain input is connected. The verification tool is **Output → Grain Plate**: a test image made of a section of the input surrounded by a flat colour sampled from it, with the grain applied — **if the inner area is indistinguishable from the outer area, the sample is good.** Beyond amount and size it exposes full per-channel control (red, green and blue each with their own process toggle, amount and size), a **Grain Colour Space** for where the sample originated and an **Apply Grain In** space for where it is re-applied, and tonal shaping through Low/Mid/High Gain plus an optional **sampled response** curve that scales grain brightness by the luminance of the Grain image.

### Key Steps
1. Connect **Src** (the image to receive grain) and, for sampled grain, **Grain** (the image to sample from). Connecting Grain switches **Grain Type** to `From Grain Clip` automatically.
2. Place the **Analysis Region** (`regionBL` / `regionTR`) over a patch containing **no image detail, only grain**, and set **Analysis Frame** (default `1`).
3. Set **Grain Colour Space** (`Cineon` / `sRGB` / `Linear`, default `sRGB`) to whatever the grain sample was in when it originated — getting this wrong exaggerates the grain through the colour-space conversion.
4. Or skip sampling: leave **Grain Type** on `Preset Stock` and choose from **Preset Stock** (default `FUJIF250under 2K`).
5. Set **Grain Amount** (`1`; `0` adds none) and **Grain Size** (`1`; larger = bigger and softer granules).
6. **Verify with Output → Grain Plate** — when the inner section is indistinguishable from the surrounding flat colour, the sample is right. Switch back to `Result` for the real output.
7. Press **Analyse** when the input clip has changed but you do not want to move the analysis region to trigger re-analysis (a warning appears when the input changes).
8. Refine per channel: **Process Red / Green / Blue** with individual **Amount** and **Size** — the route for matching a stock whose grain is not neutral across channels.
9. Shape tonally with **Low Gain**, **Mid Gain**, **High Gain**, and set **Apply Grain In** to the space the grain should be re-applied in.
10. For a luminance-dependent response, enable **Use Sampled Response**, click **Sample Grain Response** (repeated clicks *accumulate* rather than reset), blend with **Sampled Response Mix**, inspect with **Draw Response**, and start over with **Reset Grain Response**.

### Nodes / Tools / Settings
- **F_ReGrain** (NukeX / FurnaceCore). Inputs: **Grain**, **Src**. *See also* **Grain** and **ScannedGrain** (the page's own cross-reference).
- **Grain Type** (`grainType`, `Preset Stock` | `From Grain Clip`), **Preset Stock** (`presetStock`, `FUJIF250under 2K`).
- **Grain Amount** (`amount`, `1`), **Grain Size** (`size`, `1`), **Output** (`output`, `Result` | `Grain Plate`), **Analyse** (`analyse`).
- **Analysis Region BL / TR** (`regionBL`, `regionTR`), **Analysis Frame** (`frame`, `1`), **Grain Colour Space** (`grainColourSpace`, `sRGB`).
- Per channel: `processRed`/`redAmount`/`redSize`, `processGreen`/`greenAmount`/`greenSize`, `processBlue`/`blueAmount`/`blueSize`.
- **Apply Grain In** (`srcColourSpace`), **Low/Mid/High Gain** (`lowGain`, `midGain`, `highGain`).
- **Use Sampled Response** (`useResponse`), **Sampled Response Mix** (`responseMix`, `1`), **Sample Grain Response** (`sample`), **Reset Grain Response** (`reset`), **Draw Response** (`drawResponse`).
- Step-by-step guide: *Using F_ReGrain*.

### Difficulty
Intermediate

### Foundry App & Version
NukeX 17.1v1 (FurnaceCore). The page names **Grain** and **ScannedGrain** as the alternatives in the same area.

### Tags
`furnace`, `nukex`, `grain`, `nuke-17`, `intermediate`

---

## Related Tutorials
- [F_DeFlicker2](f-deflicker2.md) — the other FurnaceCore node working on image statistics over time.
- [F_WireRemoval](f-wireremoval.md) — its **Filter Size** control exists precisely because a repair filter can mistake wire detail for grain.

---

> **Provenance.** Ingested from the documentation **bundled inside Nuke 17.1v1**
> on this machine (`Documentation/html/content/`), so the `url:` is a local
> `file://` path and is not reachable from another machine. It is first-party
> Foundry documentation for the exact installed build, which makes it a better
> version witness than the public docs site: what is written here is what this
> Nuke does. The page's own footer stamp (`Nuke 17.1v1 docs`) is preserved in the
> Raw Data.

> **On the Furnace suite.** These are the **FurnaceCore** nodes bundled with
> **NukeX** — the surviving subset of the original Furnace plug-in suite, which
> is why this skill's gap list called them "legacy and partly superseded". They
> are not deprecated: they ship in 17.1 and several remain the fastest route to a
> result the modern toolset reaches only through much more setup. Where a newer
> node genuinely supersedes one, the docs say so themselves in a *See also* line,
> preserved in each entry.
