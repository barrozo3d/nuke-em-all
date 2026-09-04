---
title: F_DeFlicker2
source: Article
url: file:///C:/Program%20Files/Nuke17.1v1/Documentation/html/content/reference_guide/furnacecore_nodes/f_deflicker2.html
author: Nuke 17.1v1 bundled documentation
ingested: 2026-09-04
app: "NukeX (FurnaceCore)"
version: "Nuke 17.1v1 (bundled documentation, Documentation/html/content)"
tags: [furnace, nukex, denoise, nuke-17, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/f-deflicker2/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# F_DeFlicker2

**Source:** [Article](file:///C:/Program%20Files/Nuke17.1v1/Documentation/html/content/reference_guide/furnacecore_nodes/f_deflicker2.html)
**Author:** Nuke 17.1v1 bundled documentation
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** F_DeFlicker2 F_Deflicker2 is used to remove flicker - particularly flicker that is localized and dependent on the geometry of the scene (that is, flicker that is not present across the whole of the image), such as that caused by an un-synchronized fluorescent light in a shot. Note: F_DeFlicker2 looks at input frames outside the current frame when performing calculations, and therefore can be a computationally expensive node. As such, using more than two instances of F_DeFlicker2 in a node tree will dramatically increase render times. It is strongly advised therefore, that you render each instance out separately. Inputs and Controls Connection Type Connection Name Function Input Src The sequence requiring deflicker. Control (UI) Knob (Scripting) Default Value Function F_DeFlicker2 Tab DeFlicker Amount amount 0.3 Reduces flicker without removing it entirely; lower values leave more flicker behind. Block Size blockSize 9.6 Defines the width and height of the control block (in pixels) centered around a particular pixel analysed by the deflicker algorithm. Note: The default value avoids the loss of detail and noisy motion fields associated with higher and lower Block Size , and rarely needs adjusting. Use Motion useMotion enabled Enables a second deflicker pass using motion-compensated frames. This can improve results in areas where there is fast motion, where the initial deflicker pass may have introduced blurring. Vector Detail vectorDetail 0.2 Set the density of the motion vectors used when Use Motion is turned on. The maximum value of 1 generates one vector per pixel, producing the most accurate vectors, but taking longer to render. The default value of 0.2 generates a vector at every fifth pixel. Analysis Range range 2 The number of frames searched each side of the current frame when calculating the flicker. Higher values may give better results, but can also bring in erroneous information and take longer to process. About about N/A Displays a dialog containing information about this node. Step-by-Step Guides Using F_DeFlicker2 Nuke 17.1v1 docs:



---

## Structured Notes

### Core Technique
Remove **localised** flicker — flicker that depends on scene geometry rather than affecting the whole frame — with a block-based analysis, optionally refined by a second motion-compensated pass.

### Summary
F_DeFlicker2 targets the case a global level-match cannot fix: an unsynchronised fluorescent tube, or any flicker that varies across the image. It analyses a control block around each pixel (**Block Size**, default `9.6` px, which the docs say rarely needs adjusting because higher *and* lower values both cost — detail loss on one side, noisy motion fields on the other), searches **Analysis Range** frames either side of the current one (default `2`), and can run a second pass on motion-compensated frames via **Use Motion** to fix the blurring the first pass can introduce in fast motion. The most operationally important line on the page is a performance warning: F_DeFlicker2 reads frames outside the current one, so **more than two instances in a node tree dramatically increases render time**, and Foundry strongly advises rendering each instance out separately.

### Key Steps
1. Connect the flickering sequence to **Src**.
2. Set **DeFlicker Amount** (default `0.3`) — it *reduces* rather than eliminates; lower values deliberately leave more flicker behind.
3. Leave **Block Size** at `9.6` unless there is a reason: the default is tuned between detail loss and noisy motion fields.
4. Keep **Use Motion** enabled to run the second, motion-compensated pass — this is what recovers areas of fast motion the first pass blurred.
5. Tune **Vector Detail** (default `0.2` = a vector every fifth pixel; `1` = one vector per pixel, most accurate and slowest) when Use Motion is on.
6. Raise **Analysis Range** (default `2` frames either side) for a better estimate, accepting that too wide a range pulls in erroneous information and costs time.
7. ⚠️ **Keep to at most two instances per script**, and render each one separately — the node reads neighbouring frames, so instances compound.

### Nodes / Tools / Settings
- **F_DeFlicker2** (NukeX / FurnaceCore). Input: **Src**.
- **DeFlicker Amount** (`amount`, `0.3`), **Block Size** (`blockSize`, `9.6`).
- **Use Motion** (`useMotion`, enabled), **Vector Detail** (`vectorDetail`, `0.2`).
- **Analysis Range** (`range`, `2`) — frames searched each side of the current frame.
- **About** (`about`). Step-by-step guide: *Using F_DeFlicker2*.

### Difficulty
Intermediate

### Foundry App & Version
NukeX 17.1v1 (FurnaceCore).

### Tags
`furnace`, `nukex`, `denoise`, `nuke-17`, `intermediate`

---

## Related Tutorials
- [F_ReGrain](f-regrain.md) — the other FurnaceCore node concerned with per-frame image statistics.
- [F_Align](f-align.md) — FurnaceCore's alignment node.

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
