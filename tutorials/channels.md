---
title: Channels
source: Article
url: https://learn.foundry.com/mari/7.5/Content/user_guide/channels/channels.html
author: learn.foundry.com
ingested: 2026-09-04
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/channels/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Channels

**Source:** [Article](https://learn.foundry.com/mari/7.5/Content/user_guide/channels/channels.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Channels Channels hold layers stacks, filled with paint layers, procedurals, and adjustments in your project. For example, a project might have channels for diffuse color, displacement, or specularity, but each of those channels contain individual layers for paint, masks, and filters. Channels can then be used in shader inputs so you can adjust the amount of diffuse or specularity, among other things. Mari supports multiple channels. New projects start with a single channel. You can add as many additional channels as you need. A single project can hold all the channel data required for the model - diffuse, dirt, specular, luminescence, displacement, and so on. Each object in a Mari project has its own set of channels. See Working with Objects for details on working with multiple objects. Video: Watch Understanding Shaders and Channels for a brief overview about Channels. This video shows the workflow using Mari 3. Even though the Mari 4 workspace is different, the workflow remains the same. To have a look at the main UI differences, see Mari 3.3 vs 4.0 . Different Ways to Create Channels When you create a channel, you set the color depth and patch size. You can change both of these after creation. If channels are resized after creation, Mari automatically resizes all the layers in the channel’s layer stack. Channels are either color or scalar. See Color Data and Scalar Data for more information. Channels can be created: • using the settings for existing or recently-created channels as a template. • in bulk, using Mari 's inbuilt presets, optionally importing textures into the channel at the same time. • from a preset size, color depth, and type. • entirely custom and ad hoc. • by copying a layer to a new channel (see Layers for details). • by sharing a layer as a new channel (see Layers for details). HDR Channels The dynamic range of luminance in the real world is much greater than the range that is usually displayed on a screen. Low dynamic range (8-bit) color values can represent RGB levels only within the range of 0 (black) to 1 (white). In Mari , using 16-bit or 32-bit color values, you can clone from, or paint through, images outside of the 0 to 1 range. For details on creating and working with channels that support HDR images, see Creating and Deleting Individual Channels . Editing Paint on Your Channels The paint in your channels can be edited or transformed, much the same as with patches. Where the transform functions differ is in how they change the paint on the model. Patches are very specific and only transform paint on the selected UV patch. Channels, on the other hand, can include paint across many patches and faces in their layer stacks. In this way, transforming a channel can affect a larger amount of paint across a greater part of a model, depending on how extensive the paint in the selected channel is. Can't find what you're looking for? Use our feedback widget on the right to request more information.



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
