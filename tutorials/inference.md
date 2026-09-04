---
title: Inference
source: Article
url: https://learn.foundry.com/nuke/content/reference_guide/air_nodes/inference.html
author: learn.foundry.com
ingested: 2026-09-04
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/inference/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Inference

**Source:** [Article](https://learn.foundry.com/nuke/content/reference_guide/air_nodes/inference.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Inference The Inference node applies a .cat file supplied by the CopyCat node to create the effect modeled by the network across the input image. See CopyCat for more information. Note: Certain controls are not available in the timeline version of this node, such as GPU-related controls. Inputs and Controls Connection Type Connection Name Function Input Input The image to which the CopyCat .cat file is applied. Control (UI) Knob (Scripting) Default Value Function Inference Tab Local GPU gpuName N/A Displays the GPU used for rendering when Use GPU if available is enabled. Local GPU displays Not available when: • Use CPU is selected as the default blink device in the Preferences . • no suitable GPU was found on your system. • it was not possible to create a context for processing on the selected GPU, such as when there is not enough free memory available on the GPU. You can select a different GPU, if available, by navigating to the Preferences and selecting an alternative from the default blink device dropdown. Note: Selecting a different GPU requires you to restart Nuke before the change takes effect. Use GPU if available useGPUIfAvailable enabled When enabled, rendering occurs on the Local GPU specified, if available, rather than the CPU. Note: Enabling this option with no local GPU allows the script to run on the GPU whenever the script is opened on a machine that does have a GPU available. You should also select this if you wish to render from the command line with the --gpu option. See Nuke 17 Release Notes for more information on the GPUs Nuke supports. Model File modelFile N/A The path to the CopyCat .cat file you want to use to apply the effect modeled by the network. You can enter the file path manually or click the directory icon to browse to the .cat file's location. Channels In channelsIn None The channels the model expects as input. Channels Out channelsOut None The channels the model expects as output. Optimize for Speed and Memory inferencePrecision disabled When enabled, use 16-bit half-float precision instead of Nuke 's standard 32-bit float precision. Enabling this control produces results more quickly, uses less GPU memory, and can handle larger images, but can result in artifacts with some trained networks. Note: This control is hidden when Use GPU if available is disabled. Step-by-Step Guides Import Pre-Trained PyTorch Models Can't find what you're looking for? Use our feedback widget on the right to request more information.



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
