---
title: Channels
source: Article
url: https://learn.foundry.com/mari/7.5/Content/user_guide/channels/channels.html
author: learn.foundry.com
ingested: 2026-09-04
app: "Mari"
version: "7.5 (learn.foundry.com/mari/7.5; some embedded videos still show the Mari 3 workspace)"
tags: [mari-texturing, udim, mari-7, beginner]
extraction_status: complete
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
A **channel** holds a layer stack — paint layers, procedurals and adjustments — and feeds shader inputs; each object in a project has its own set, and each channel carries its own colour depth and patch size.

### Summary
Channels are the organising unit above layers and below shaders: a project might hold diffuse, dirt, specular, luminescence and displacement channels, each containing its own layers, masks and filters, and each usable as a shader input. New projects start with one and take as many as needed, and **every object in a project has its own set of channels**. Colour depth and patch size are set at creation and changeable later — resizing a channel **automatically resizes every layer in its stack**. Channels are either **colour or scalar**, the distinction that separates image data from masks, heights and normals. The HDR discussion is the practically useful part: 8-bit values represent RGB only within 0–1, while **16-bit or 32-bit channels let you clone from or paint through images outside that range**. The page also draws the line against patches: patch transforms touch one UV patch, whereas a channel transform reaches across every patch and face its layer stack covers.

### Key Steps
1. Create channels for the maps the shader needs — diffuse, dirt, specular, luminescence, displacement.
2. Set **colour depth** and **patch size** at creation; both can change later, and all layers in the stack resize with the channel.
3. Choose **colour or scalar** deliberately — scalar for non-colour data such as masks, heights, normals and depths.
4. Create channels by any of the documented routes: from an existing or recent channel as a template; **in bulk from Mari's presets**, optionally importing textures at the same time; from a preset size/depth/type; fully custom; by **copying** a layer to a new channel; or by **sharing** a layer as a new channel.
5. Use **16- or 32-bit** channels when you need to clone from or paint through HDR images outside 0–1.
6. Wire channels into shader inputs to control how much diffuse, specularity and so on the shader receives.
7. Transform paint at the channel level when the change should span many patches — use patch transforms when it must not.

### Nodes / Tools / Settings
- **Channel** — holds a layer stack (paint layers, procedurals, adjustments); per-object; feeds shader inputs.
- Creation-time settings: **colour depth**, **patch size**; both editable later, with automatic resize of all layers.
- **Colour vs scalar** channels (see Color Data / Scalar Data).
- **HDR**: 8-bit clamps to 0–1; 16-bit and 32-bit allow cloning from and painting through out-of-range images.
- Creation routes: template from existing/recent, bulk from presets (with optional texture import), preset size/depth/type, custom, copy a layer, share a layer.

### Difficulty
Beginner

### Foundry App & Version
Mari 7.5.

### Tags
`mari-texturing`, `udim`, `mari-7`, `beginner`

---

## Related Tutorials
- [Working With Patches](working-with-patches.md) — per-channel patch resolution, and how patch transforms differ from channel transforms.
- [Managing Projects](managing-projects.md) — the Channels tab that scans a root path for existing textures.
- [Projectors](projectors.md) — batch unproject/project across multiple channels.

---

> **Provenance.** `learn.foundry.com/mari/7.5` — Foundry's Mari documentation is
> **version-pathed** (`/mari/docs` redirects to `/mari/7.5/Content/learnhome/learn_mari.html`),
> unlike the Katana and Nuke doc sets. Mari is **not installed on this machine**
> (verified 2026-09-04), so unlike the Nuke pages these come from the public site
> rather than a bundled copy, and describe 7.5 rather than a build in use here.
> Several pages carry a note that their embedded video shows the Mari 3
> workspace while the workflow itself is unchanged.
