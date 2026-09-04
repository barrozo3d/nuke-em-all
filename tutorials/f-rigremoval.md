---
title: F_RigRemoval
source: Article
url: file:///C:/Program%20Files/Nuke17.1v1/Documentation/html/content/reference_guide/furnacecore_nodes/f_rigremoval.html
author: Nuke 17.1v1 bundled documentation
ingested: 2026-09-04
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
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
