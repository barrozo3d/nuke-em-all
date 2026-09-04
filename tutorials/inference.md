---
title: Inference
source: Article
url: https://learn.foundry.com/nuke/content/reference_guide/air_nodes/inference.html
author: learn.foundry.com
ingested: 2026-09-04
app: "Nuke / NukeX / Nuke Studio (a timeline version exists with GPU controls removed)"
version: "Nuke 17 (the page cites the Nuke 17 Release Notes for supported GPUs)"
tags: [copycat, ai-tools, machine-learning, nuke-17, beginner]
extraction_status: complete
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
Apply a trained `.cat` file across a whole sequence with a single node: point **Model File** at the network CopyCat produced and let **Inference** reproduce the learned effect on its Input.

### Summary
Inference is the playback half of Nuke's CopyCat workflow — it takes one image input and one `.cat` model file and applies the modelled effect. Its control set is deliberately small: **Model File**, the read-only **Channels In** / **Channels Out** the model expects, GPU selection, and **Optimize for Speed and Memory**, which drops from Nuke's standard 32-bit float to 16-bit half float for faster, lighter, larger-image inference at the risk of artifacts with some trained networks. Two placement details matter in practice: the **timeline version of the node omits the GPU controls**, and the node is not restricted to CopyCat's own output — the page's step-by-step guide is *Import Pre-Trained PyTorch Models*, so externally trained models converted to `.cat` run through this same node.

### Key Steps
1. Connect the image to process to **Input**.
2. Set **Model File** to the `.cat` file — type the path or click the directory icon. Coming from CopyCat, its **Create Inference** button builds this node with the path already filled in.
3. Check **Channels In** and **Channels Out** — read-only, reporting what the model expects to receive and produce. A channel mismatch here is the first thing to check when output looks wrong.
4. Leave **Use GPU if available** enabled and confirm **Local GPU** names a real device; it reads `Not available` when Preferences' default blink device is CPU, when no suitable GPU is present, or when a context could not be created (usually insufficient GPU memory). A GPU change requires restarting Nuke.
5. Enable **Optimize for Speed and Memory** for 16-bit half-float inference when speed, GPU memory or image size is the constraint — and check for artifacts, since not every trained network survives the precision drop. The control is hidden when GPU use is disabled.
6. Rendering from the command line: enable **Use GPU if available** and pass `--gpu`.
7. To run a model trained outside Nuke, follow the page's linked step-by-step guide **Import Pre-Trained PyTorch Models** and load the resulting `.cat` here.

### Nodes / Tools / Settings
- **Inference** — single **Input**; a timeline version of the node exists with GPU-related controls unavailable.
- **Model File** (`modelFile`) — path to the `.cat` file.
- **Channels In** (`channelsIn`) / **Channels Out** (`channelsOut`) — default `None`; the channels the model expects in and out.
- **Optimize for Speed and Memory** (`inferencePrecision`, disabled) — 16-bit half float instead of 32-bit; faster, less GPU memory, larger images, possible artifacts. Hidden when **Use GPU if available** is off.
- **Local GPU** (`gpuName`) / **Use GPU if available** (`useGPUIfAvailable`, enabled) — same semantics and same restart requirement as on CopyCat; also the control to enable for `--gpu` command-line renders.
- Linked step-by-step guide: **Import Pre-Trained PyTorch Models**.

### Difficulty
Beginner

### Foundry App & Version
Nuke, NukeX and Nuke Studio — unlike CopyCat, Inference is not NukeX-restricted, so a `.cat` trained on a NukeX seat can be applied on a base Nuke seat. The timeline version of the node drops the GPU controls. Nuke 17-era documentation (cites the *Nuke 17 Release Notes* for supported GPUs).

### Tags
`copycat`, `ai-tools`, `machine-learning`, `nuke-17`, `beginner`

---

## Related Tutorials
- [CopyCat](copycat.md) — trains the `.cat` file this node consumes; read them together.
- [How SMART is State of the Art A.I Rotoscoping?](how-smart-is-state-of-the-art-ai-rotoscoping.md) — shares `ai-tools`.

---

> **Coverage note — CLOSED the same day it was written.** This note originally
> recorded that neither this page nor `copycat.md` documented **the Cattery
> library itself** — browsing or downloading Foundry's pretrained community
> models, or where the downloaded files install. That gap is now filled by
> [Download Pre-Trained Models from Foundry's Cattery](download-pre-trained-models-from-foundrys-cattery.md),
> ingested from the Nuke 17.1v1 bundled documentation on this machine.
>
> The distinction the original note drew still holds and is worth keeping:
> CopyCat's `Deblur` / `Upscale` / `Human Matting` / `Checkpoint` weightings are
> pretrained starting points for **training**, and are **not** the Cattery
> catalogue — the Cattery ships finished models you install as gizmos and run
> through this node. Two different things that sound alike.
