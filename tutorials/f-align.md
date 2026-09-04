---
title: F_Align
source: Article
url: file:///C:/Program%20Files/Nuke17.1v1/Documentation/html/content/reference_guide/furnacecore_nodes/f_align.html
author: Nuke 17.1v1 bundled documentation
ingested: 2026-09-04
app: "NukeX (FurnaceCore)"
version: "Nuke 17.1v1 (bundled documentation, Documentation/html/content)"
tags: [furnace, nukex, tracking, nuke-17, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/f-align/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# F_Align

**Source:** [Article](file:///C:/Program%20Files/Nuke17.1v1/Documentation/html/content/reference_guide/furnacecore_nodes/f_align.html)
**Author:** Nuke 17.1v1 bundled documentation
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** F_Align F_Align takes two sequences that were shot of the same scene and lines them up spatially. It uses Global Motion Estimation (GME) to calculate a four-corner pin so that each frame in one shot (the source input) will be aligned with the corresponding frame in a second shot (the reference input). The result is the source image which has been repositioned to line up with the reference image. Inputs and Controls Connection Type Connection Name Function Input Ref The reference image used to align the source image. Src The source image to align. Control (UI) Knob (Scripting) Default Value Function F_Align Tab Analyse analyse N/A Click to begin analysis of the input clips and calculate a corner pin. Interrupting the analysis will not delete the corner pin keys that have already been calculated. Render During Analysis renderOn enabled When enabled, this toggle causes the effect to update the time line and render a freshly analyzed frame in the Viewer so you can see the progress of the effect. Note: Disabling this control may speed up the general analysis. Clear Analysis clear N/A Click to delete all key frames from the corner pin controls, allowing you to force a re-analysis if you feel the need to. Analysis Range range Source Clip Range This controls the range of frames any analysis runs over: • Specified Range - reads the Analysis Start and Analysis Stop fields for the range of frames to analyze. • Source Clip Range - automatically determines the range of frames to analyze from the length of the clip attached to the Src input. • Current Frame - the analysis occurs only on the current frame. This is useful for correcting any errors that may have occurred while analyzing the entire clip. Analysis Start start 0 The first frame analyzed if Analysis Range is set to Specified Range . Analysis Stop stop 100 The last frame analyzed if Analysis Range is set to Specified Range . Scale scale disabled Indicates whether the calculated corner pin can include a scaling factor. Rotate rotate enabled Indicates whether the calculated corner pin can include rotations. Translate translate enabled Indicates whether the calculated corner pin can include translations on the x and y axes. Perspective perspective disabled Indicates whether the calculated corner pin can include perspective transforms. Analysis Region Analysis Region BL regionBL N/A The region analyzed to calculate the four-corner pin. This is especially useful when doing any form of frame locking, in which case, go to the lock frame, look at the reference clip and position the box over the area you want locked. • Analysis Region BL - controls the position of the bottom left corner of the analysis region. • Analysis Region TR - controls the position of the top right corner of the analysis region. Analysis Region TR regionTR N/A Advanced Accuracy accuracy 0.9 Controls the time/accuracy trade off. Higher values slow the analysis, but can produce better result. Filtering filtering Medium Sets the filtering quality: • Low - low quality but quick to render. • Medium - uses a bilinear filter. This gives good results and is quicker to render than High quality filtering. • High - uses a sinc filter to interpolate pixels giving a sharper repair. This gives the best results but takes longer to process. Invert invert disabled Enable this control to use the inverse of the calculated four-corner pin during render. Advanced Four Corner Pin Bottom Left pinBL N/A The bottom left corner pin calculated during the analysis pass. Bottom Right pinBR N/A The bottom right corner pin calculated during the analysis pass. Top Left pinTL N/A The top left corner pin calculated during the analysis pass. Top Right pinTR N/A The top right corner pin calculated during the analysis pass. About about N/A Displays a dialog containing information about this node. Step-by-Step Guides Using F_Align Nuke 17.1v1 docs:



---

## Structured Notes

### Core Technique
Line up two sequences shot of the same scene by using **Global Motion Estimation (GME)** to calculate a four-corner pin that repositions the **Src** clip onto the **Ref** clip, frame by frame.

### Summary
F_Align solves the two-plate alignment problem — a witness camera, a second take, a re-shoot element — by analysing global motion between the reference and the source and baking the result into an animated four-corner pin. Which transform components the pin is allowed to use is explicit: **Rotate** and **Translate** are on by default, **Scale** and **Perspective** are off, so the solve is constrained to what you actually expect to differ unless you widen it. The **Analysis Region** box matters more than its plain name suggests — for frame locking you go to the lock frame, look at the reference, and place the box over the area that must stay locked. Analysis is a discrete pass driven by the **Analyse** button, interrupting it keeps the keys already calculated, and **Clear Analysis** is the deliberate way to force a redo.

### Key Steps
1. Connect **Ref** (the image to align *to*) and **Src** (the image to be moved). The output is Src repositioned onto Ref.
2. Set **Analysis Range** — `Source Clip Range` (default, derived from the Src length), `Specified Range` (uses **Analysis Start** / **Analysis Stop**, defaults 0 and 100), or `Current Frame` to fix a single bad frame after a full pass.
3. Constrain the solve: **Rotate** and **Translate** default **on**, **Scale** and **Perspective** default **off**. Enable only what the shot genuinely contains.
4. Place the **Analysis Region** with **Analysis Region BL** / **TR** — for frame locking, do this on the lock frame while looking at the reference clip, over the area you want held.
5. Press **Analyse**. Leave **Render During Analysis** on to watch progress in the Viewer, or disable it to speed the analysis up.
6. Raise **Accuracy** (default `0.9`) for a better solve at the cost of time; set **Filtering** to `High` (sinc) for the sharpest result, `Medium` (bilinear) as the default compromise, `Low` for speed.
7. Inspect or hand-correct the baked result in **Advanced Four Corner Pin** — `pinBL`, `pinBR`, `pinTL`, `pinTR` hold the animated corners.
8. Enable **Invert** to apply the inverse of the calculated pin at render — the route for pushing something back into the original plate's space.
9. Use **Clear Analysis** to delete all corner-pin keys and force a clean re-analysis.

### Nodes / Tools / Settings
- **F_Align** (NukeX / FurnaceCore). Inputs: **Ref**, **Src**.
- **Analyse** (`analyse`), **Render During Analysis** (`renderOn`, on), **Clear Analysis** (`clear`).
- **Analysis Range** (`range`, `Source Clip Range`) with **Analysis Start** (`start`, 0) / **Analysis Stop** (`stop`, 100).
- Transform components: **Scale** (`scale`, off), **Rotate** (`rotate`, on), **Translate** (`translate`, on), **Perspective** (`perspective`, off).
- **Analysis Region BL / TR** (`regionBL`, `regionTR`).
- **Accuracy** (`accuracy`, `0.9`), **Filtering** (`filtering`, `Medium` — Low / Medium bilinear / High sinc), **Invert** (`invert`, off).
- **Four Corner Pin**: `pinBL`, `pinBR`, `pinTL`, `pinTR`. **About** (`about`).
- Step-by-step guide referenced by the page: *Using F_Align*.

### Difficulty
Intermediate

### Foundry App & Version
NukeX 17.1v1 — FurnaceCore nodes are NukeX, not base Nuke.

### Tags
`furnace`, `nukex`, `tracking`, `nuke-17`, `intermediate`

---

## Related Tutorials
- [F_Steadiness](f-steadiness.md) — the same GME four-corner-pin machinery aimed at one clip instead of two.
- [F_RigRemoval](f-rigremoval.md), [F_WireRemoval](f-wireremoval.md) — the repair half of the FurnaceCore set.

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
