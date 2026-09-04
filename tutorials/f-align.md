---
title: F_Align
source: Article
url: file:///C:/Program%20Files/Nuke17.1v1/Documentation/html/content/reference_guide/furnacecore_nodes/f_align.html
author: Nuke 17.1v1 bundled documentation
ingested: 2026-09-04
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
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
