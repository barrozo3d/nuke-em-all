---
title: F_ReGrain
source: Article
url: file:///C:/Program%20Files/Nuke17.1v1/Documentation/html/content/reference_guide/furnacecore_nodes/f_regrain.html
author: Nuke 17.1v1 bundled documentation
ingested: 2026-09-04
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
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
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Nodes / Tools / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Foundry App & Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]
