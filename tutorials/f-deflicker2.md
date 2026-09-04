---
title: F_DeFlicker2
source: Article
url: file:///C:/Program%20Files/Nuke17.1v1/Documentation/html/content/reference_guide/furnacecore_nodes/f_deflicker2.html
author: Nuke 17.1v1 bundled documentation
ingested: 2026-09-04
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
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
