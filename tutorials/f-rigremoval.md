---
title: F_RigRemoval
source: Article
url: file:///C:/Program%20Files/Nuke17.1v1/Documentation/html/content/reference_guide/furnacecore_nodes/f_rigremoval.html
author: Nuke 17.1v1 bundled documentation
ingested: 2026-09-04
app: "NukeX (FurnaceCore)"
version: "Nuke 17.1v1 (bundled documentation, Documentation/html/content)"
tags: [furnace, nukex, clean-plate, roto, nuke-17, advanced]
extraction_status: complete
frames_dir: tutorials/frames/f-rigremoval/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# F_RigRemoval

**Source:** [Article](file:///C:/Program%20Files/Nuke17.1v1/Documentation/html/content/reference_guide/furnacecore_nodes/f_rigremoval.html)
**Author:** Nuke 17.1v1 bundled documentation
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** F_RigRemoval F_RigRemoval eliminates unwanted objects, or rigs, from image sequences without the need for accurate rotoscoping or keying to produce a clean plate. The rig removal algorithm works by estimating the background motion between successive frames, ignoring the foreground object, and then using the motion information to look forward and backward in the sequence in order to find the correct piece of background to fill in the missing region. See also RotoPaint and Project3D . Inputs and Controls Connection Type Connection Name Function Input RigMask An optional mask to designate the rig area to remove. Src The source image containing the unwanted object or rig. The source may contain an alpha channel to define the rig area. Control (UI) Knob (Scripting) Default Value Function F_RigRemoval Tab Rig Region rigRegion Box Defines the area to repair: • Box - repair the area inside a rectangular box, controlled by the Rig Region Box controls or the on-screen box. • Src Alpha - repair the region defined by the alpha of the Src input. • Src Inverted Alpha - repair the region defined by the inverted alpha of the Src input. • RigMask Luminance - repair the region defined by the luminance of the Rig Mask input. • RigMask Inverted Luminance - repair the region defined by the inverted luminance of the Rig Mask input. • RigMask Alpha - repair the region defined by the alpha of the Rig Mask input. • RigMask Inverted Alpha - repair the region defined by the inverted alpha of the Rig Mask input. Frames Searched framesSearched Forward and Backward Select whether to search forwards, backwards, or in both directions to find missing data. • Forward and Backward - searches before and after the current frame. • Forward - searches frames after the current frame. • Backward - searches frames before the current frame. Frame Range frameRange 4 Sets the number of frames the algorithm looks forwards and backwards in the sequence to find the missing data. If you are getting red pixels, then increase this value. Frames Used in Range framesUsed Half of Frames If the Frame Range is set to a large number, the rendering time can be prohibitive. Frames Used in Range may speed up the repair by not using every frame to fill the foreground region, effectively skipping frames. However, this may reduce the quality of the result. • All Frames - use every frame in the specified frame range to construct the repair. • Half of Frames - use every other frame in the specified frame range to construct the repair. • Quarter of Frames - use every fourth frame in the specified frame range to construct the repair. • 10% of Frames - use every tenth frame in the specified frame range to construct the repair. • Max 25 Frames - use no more than 25 frames from the specified frame range to construct the repair. This option can be useful if Frame Range has been set to a very large number. Max Rig Movement maxRigMove 30 To avoid perspective changes, F_RigRemoval searches for the missing data inside an area immediately around the Rig Region . Max Rig Movement defines the width of this area (in pixels). Fast movement in the Src input may require a higher value than slow movement. Rig Region Box Rig Region BL regionBL N/A The rectangular area used to define the repair when Rig Region is set to Box . • Rig Region BL - controls the position of the bottom left corner of the rig region. • Rig Region TR - controls the position of the top right corner of the rig region. Rig Region TL regionTR N/A Advanced Filtering filtering Medium Sets the filtering quality. • Low - low quality but quick to render. • Medium - uses a bilinear filter. This gives good results and is quicker to render than high filtering. • High - uses a sinc filter to interpolate pixels giving a sharper repair. This gives the best results but takes longer to process. Luminance Correct lumCorrect disabled Enable this to correct for luminance changes from information taken from other frames. This is particularly important if the lighting changes throughout the sequence. Perspective Correct perspCorrect disabled Enable this to correct for minor perspective changes. Overlap Correct overlapCorrect 1 The repair is built up using slices of information from other frames in the sequence which are then overlapped and blended to give a more natural looking repair. This value controls how much the regions overlap. Increasing this value too much degrades image sharpness. Repair Fail Marker Opacity failOpacity 0.5 Sets the level of transparency of the red pixels used to show where the repair has failed. Preserve Alpha preserveAlpha disabled Enable this to preserve the original alpha channel. By default, the alpha channel is set to white where the repair has failed and black everywhere else. About about N/A Displays a dialog containing information about this node. Step-by-Step Guides Using F_RigRemoval Nuke 17.1v1 docs:



---

## Structured Notes

### Core Technique
Remove a rig or unwanted object **without accurate roto or keying** by estimating background motion around it, then looking forwards and backwards through the sequence for the real background to fill the hole.

### Summary
F_RigRemoval's premise is that the background behind a rig is usually visible in *some other frame*, so the repair should be found rather than painted. It estimates background motion between successive frames while ignoring the foreground object, then reaches `Frame Range` frames in either direction (default `4`) to source the fill. The region to repair can come from a simple **Box** or from six mask routes — the Src alpha, the RigMask luminance or alpha, and the inverse of each. The two controls that decide whether it works are **Frame Range** and **Max Rig Movement** (default `30` px), the latter constraining the search to an area immediately around the rig so perspective changes do not corrupt the fill; fast movement needs a larger value. Failure is visible rather than silent: **red pixels mark where the repair failed**, the docs' own advice being to increase Frame Range when they appear, and **Repair Fail Marker Opacity** controls how strongly they show.

### Key Steps
1. Connect **Src** (containing the rig) and optionally **RigMask**.
2. Choose **Rig Region**: `Box` (drag `regionBL`/`regionTR` or the on-screen box), `Src Alpha`, `Src Inverted Alpha`, `RigMask Luminance`, `RigMask Inverted Luminance`, `RigMask Alpha`, or `RigMask Inverted Alpha`.
3. Set **Frames Searched** — `Forward and Backward` (default), or one direction only when the far side of the shot has no usable background.
4. Set **Frame Range** (default `4`). ⚠️ **Red pixels in the output mean the repair failed — the documented fix is to raise this value.**
5. Control cost with **Frames Used in Range**: `All Frames`, `Half of Frames` (default), `Quarter of Frames`, `10% of Frames`, or `Max 25 Frames` for a very large range. Skipping frames is faster and may reduce quality.
6. Set **Max Rig Movement** (default `30` px) to the width of the search band around the rig — raise it for fast movement, keep it tight to avoid perspective error.
7. In **Advanced**, set **Filtering** (`Low` / `Medium` bilinear / `High` sinc), and enable **Luminance Correct** when the lighting changes across the sequence and **Perspective Correct** for minor perspective change.
8. Tune **Overlap Correct** (default `1`) — the repair is assembled from overlapping slices taken from other frames; more overlap blends more naturally but too much degrades sharpness.
9. Set **Repair Fail Marker Opacity** (default `0.5`) to control the red failure overlay, and enable **Preserve Alpha** if the original alpha must survive — by default alpha is written white where the repair failed and black elsewhere, which doubles as a failure matte.

### Nodes / Tools / Settings
- **F_RigRemoval** (NukeX / FurnaceCore). Inputs: **RigMask** (optional), **Src**. *See also* **RotoPaint** and **Project3D** (the page's own cross-reference).
- **Rig Region** (`rigRegion`, `Box`) with the seven region sources; **Rig Region BL / TR** (`regionBL`, `regionTR`).
- **Frames Searched** (`framesSearched`, `Forward and Backward`), **Frame Range** (`frameRange`, `4`), **Frames Used in Range** (`framesUsed`, `Half of Frames`).
- **Max Rig Movement** (`maxRigMove`, `30`).
- **Filtering** (`filtering`, `Medium`), **Luminance Correct** (`lumCorrect`, off), **Perspective Correct** (`perspCorrect`, off), **Overlap Correct** (`overlapCorrect`, `1`).
- **Repair Fail Marker Opacity** (`failOpacity`, `0.5`), **Preserve Alpha** (`preserveAlpha`, off). **About** (`about`).
- Step-by-step guide: *Using F_RigRemoval*.

### Difficulty
Advanced

### Foundry App & Version
NukeX 17.1v1 (FurnaceCore).

### Tags
`furnace`, `nukex`, `clean-plate`, `roto`, `nuke-17`, `advanced`

---

## Related Tutorials
- [F_WireRemoval](f-wireremoval.md) — the same repair problem for thin wires, with its own tracker and four repair algorithms.
- [F_Align](f-align.md) — GME alignment, useful when a clean plate has to be brought into the shot.

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
