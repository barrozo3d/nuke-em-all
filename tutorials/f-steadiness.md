---
title: F_Steadiness
source: Article
url: file:///C:/Program%20Files/Nuke17.1v1/Documentation/html/content/reference_guide/furnacecore_nodes/f_steadiness.html
author: Nuke 17.1v1 bundled documentation
ingested: 2026-09-04
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/f-steadiness/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# F_Steadiness

**Source:** [Article](file:///C:/Program%20Files/Nuke17.1v1/Documentation/html/content/reference_guide/furnacecore_nodes/f_steadiness.html)
**Author:** Nuke 17.1v1 bundled documentation
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** F_Steadiness F_Steadiness uses Global Motion Estimation (GME) to calculate a four-corner pin, so that camera motion within a single shot can be smoothed out over a range of frames or removed by locking to a specific frame. Inputs and Controls Connection Type Connection Name Function Input Src The source clip to stabilize. Control (UI) Knob (Scripting) Default Value Function F_Steadiness Tab Analyse analyse N/A Click to begin an analysis of the input clip and calculate a corner pin. Interrupting the analysis will not delete the corner pin keys that have already been calculated. Render During Analysis renderOn enabled When enabled, this toggle causes the effect to update the time line and render a freshly analyzed frame in the Viewer so you can see the progress of the effect. Note: Disabling this control may speed up the general analysis. Clear Analysis clear N/A Click to delete all key frames from the corner pin controls, allowing you to force a re-analysis if you feel the need to. Analysis Range range Source Clip Range This controls the range of frames any analysis runs over: • Specified Range - reads the Analysis Start and Analysis Stop fields for the range of frames to analyze. • Source Clip Range - automatically determines the range of frames to analyze from the length of the clip attached to the Src input. Analysis Start start 0 The first frame analyzed if Analysis Range is set to Specified Range . Analysis Stop stop 100 The last frame analyzed if Analysis Range is set to Specified Range . Mode mode Smooth This controls whether F_Steadiness is smoothing the shot while keeping the overall camera motion, or locking the shot to a single frame to completely remove camera motion. It can be set to: • Incremental Lock - calculates the pin that takes each frame to the lock frame. This calculates the pin by working from the lock frame out to each frame, calculating the GME between each frame incrementally and accumulating it to create the corner pin. • Absolute Lock - this also calculates a pin that takes each frame to the lock frame. However, it does so by doing GME directly from the frame in question directly to the lock frame. • Smooth - in which case, the shot is smoothed for a range of frames described by the Smoothing control. Use Smooth to keep the overall camera motion, but to smooth out sharp bumps and kicks. Scale scale disabled Indicates whether the calculated corner pin can include a scaling factor. Rotate rotate enabled Indicates whether the calculated corner pin can include rotations. Translate translate enabled Indicates whether the calculated corner pin can include translations on the x and y axes. Perspective perspective disabled Indicates whether the calculated corner pin can include perspective transforms. Analysis Region Analysis Region BL regionBL N/A This is the region analyzed to calculate the four-corner pin. This is especially useful when doing any form of frame locking, in which case, go to the lock frame, look at the reference clip and position the box over the area you want locked. • Analysis Region BL - controls the position of the bottom left corner of the analysis region. • Analysis Region TR - controls the position of the top right corner of the analysis region. Analysis Region TR regionTR N/A Advanced Smoothing smooth 10 Controls the range of frames to average motion over when Mode is set to Smooth . Lock Frame lockFrame 0 Controls the frame locked to when Mode is set to either of the lock modes. Note: Frame 0 for F_Steadiness is frame 1 in NukeX . Therefore, if you are looking at frame 3 in the Viewer and want to use that frame as the lock frame, you need to enter 2 as the Lock Frame value. Accuracy accuracy 0.6 Controls the time/accuracy trade off. The higher this is, the slower the analysis, but you have a better likelihood of a good result.v Filtering filtering Medium Sets the filtering quality. • Low - low quality but quick to render. • Medium - uses a bilinear filter. This gives good results and is quicker to render than High filtering. • High - uses a sinc filter to interpolate pixels giving a sharper repair. This gives the best results but takes longer to process. Invert invert disabled When enabled, the inverse of the calculated four-corner pin is used during render. This works best with the lock modes, and can be used to track static locked-off plates back into a shot. Auto Scale autoScale 1 Automatically fills in the black gaps at the edges of the Src by scaling the output image up. A value of 1 scales the image up until no black is visible, whereas a value of 0 disables scaling and leaves the black edges untouched. Advanced Four Corner Pin Bottom Left pinBL N/A The bottom left corner pin calculated during the analysis pass. Bottom Right pinBR N/A The bottom right corner pin calculated during the analysis pass. Top Left pinTL N/A The top left corner pin calculated during the analysis pass. Top Right pinTR The top right corner pin calculated during the analysis pass. About about N/A Displays a dialog containing information about this node. Step-by-Step Guides Using F_Steadiness Nuke 17.1v1 docs:



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
