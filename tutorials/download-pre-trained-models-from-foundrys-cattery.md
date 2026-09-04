---
title: Download Pre-Trained Models from Foundry's Cattery
source: Article
url: file:///C:/Program%20Files/Nuke17.1v1/Documentation/html/content/comp_environment/air_tools/cattery.html
author: Nuke 17.1v1 bundled documentation
ingested: 2026-09-04
app: "Nuke"
version: "Nuke 17.1v1 (bundled documentation, Documentation/html/content)"
tags: [copycat, ai-tools, machine-learning, gizmo, nuke-17, beginner]
extraction_status: complete
frames_dir: tutorials/frames/download-pre-trained-models-from-foundrys-cattery/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Download Pre-Trained Models from Foundry's Cattery

**Source:** [Article](file:///C:/Program%20Files/Nuke17.1v1/Documentation/html/content/comp_environment/air_tools/cattery.html)
**Author:** Nuke 17.1v1 bundled documentation
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Download Pre-Trained Models from Foundry's Cattery The Cattery is a library of free, third-party machine learning models created using CopyCat. This forum helps to bridge the gap between academia and production, giving you access to different ML models that run in Nuke. The Cattery includes state-of-the-art models addressing segmentation, depth estimation, optical flow, upscaling, denoising, and style transfer, with plans to expand the models hosted in the future. Click the Cattery icon in Nuke toolbar or go to https://community.foundry.com/cattery to get started. Pick a model that you want to try out and click the Download button in the description. Tip: Each model has a Category and Description, so you can easily see what might be useful for you. Locate the .zip file in your download location and unzip it. Inside the file, locate the Cattery directory and paste it into your .nuke directory. The location of the .nuke directory is OS-specific: • Linux: /home/login name/.nuke • macOS: /Users/login name/.nuke • Windows: ~\.nuke Note: On Windows , the .nuke folder can be found under the directory pointed to by the HOME environment variable. If this variable is not set (which is common), the .nuke directory will be under the folder specified by the USERPROFILE environment variable - which is generally of the form drive letter :\Documents and Settings\ login name \ or drive letter :\Users\ login name \ To find out if the HOME and USERPROFILE environment variables are set and where they are pointing at, enter %HOME% or %USERPROFILE% into the address bar in Windows Explorer. If the environment variable is set, the folder it’s pointing at is opened. If it’s not set, you get an error. Your .nuke directory should look something like this: Back in Nuke, click the Cattery icon and select Update . Your selected model is added to the Cattery menu. Click the model menu item to add a gizmo containing your model to the Node Graph. Nuke 17.1v1 docs:



---

## Structured Notes

### Core Technique
Install a free third-party ML model from Foundry's **Cattery** by unzipping its `Cattery` directory into your `.nuke` folder, then **Cattery icon → Update** to have the model appear in the Cattery menu as a gizmo.

### Summary
The Cattery is Foundry's library of free, third-party machine-learning models built with CopyCat, hosted at `community.foundry.com/cattery` and reachable from the Cattery icon in the Nuke toolbar. The catalogue covers **segmentation, depth estimation, optical flow, upscaling, denoising and style transfer**, each entry carrying a Category and Description so a model can be judged before download. Installation is a plug-in-path operation, not an import: unzip the download, find the `Cattery` directory inside, and paste it into `.nuke` — `/home/<login>/.nuke` on Linux, `/Users/<login>/.nuke` on macOS, `~\.nuke` on Windows. The Windows detail is the one that actually costs time: **`.nuke` sits under `HOME` if that variable is set, and under `USERPROFILE` if not — and it commonly is not**; entering `%HOME%` or `%USERPROFILE%` in Explorer's address bar tells you which. After **Update**, the model appears in the Cattery menu and clicking it drops a **gizmo containing the model** into the Node Graph.

### Key Steps
1. Click the **Cattery icon** in the Nuke toolbar, or go to `https://community.foundry.com/cattery`.
2. Pick a model — read its **Category** and **Description** to judge fit — and click **Download** in its description.
3. Locate the `.zip` in your download folder and unzip it.
4. Inside, find the **`Cattery` directory** and paste it into your `.nuke` directory.
5. Resolve `.nuke` for your OS: **Linux** `/home/<login name>/.nuke`, **macOS** `/Users/<login name>/.nuke`, **Windows** `~\.nuke`.
6. ⚠️ **On Windows, find `.nuke` properly:** it lives under the directory pointed to by **`HOME`** — but that variable is commonly unset, in which case it is under **`USERPROFILE`** (typically `C:\Users\<login name>\`). Type `%HOME%` or `%USERPROFILE%` into the Explorer address bar: if the variable is set the folder opens, otherwise you get an error.
7. Back in Nuke, click the **Cattery icon** and select **Update**.
8. The model now appears as an item in the **Cattery menu** — click it to add a **gizmo containing the model** to the Node Graph.

### Nodes / Tools / Settings
- **Cattery** — library of free third-party ML models made with CopyCat; `https://community.foundry.com/cattery`; toolbar icon inside Nuke.
- Model categories available: **segmentation, depth estimation, optical flow, upscaling, denoising, style transfer**.
- Install path: the `Cattery` directory from the downloaded `.zip`, pasted into `.nuke`.
- `.nuke` locations: Linux `/home/<login>/.nuke`, macOS `/Users/<login>/.nuke`, Windows `~\.nuke` resolved via **`HOME`**, falling back to **`USERPROFILE`**.
- **Cattery icon → Update** to register a newly added model; the model then arrives as a **gizmo**.

### Difficulty
Beginner

### Foundry App & Version
Nuke 17.1v1. The page sits in `comp_environment/air_tools/` alongside the AIR (AI Research) toolset; the models are third-party and free, created with CopyCat.

### Tags
`copycat`, `ai-tools`, `machine-learning`, `gizmo`, `nuke-17`, `beginner`

---

## Related Tutorials
- [Inference](inference.md) — the node that runs a `.cat` model; this page supplies the models its coverage note recorded as missing.
- [CopyCat](copycat.md) — the trainer every Cattery model was built with.
- [Installing Plug-ins](installing-plug-ins.md) — the general `.nuke` / `NUKE_PATH` plug-in-path mechanism this install is one instance of.

---

> **Provenance.** Ingested from the documentation **bundled inside Nuke 17.1v1**
> on this machine (`Documentation/html/content/`), so the `url:` is a local
> `file://` path and is not reachable from another machine. It is first-party
> Foundry documentation for the exact installed build, which makes it a better
> version witness than the public docs site: what is written here is what this
> Nuke does. The page's own footer stamp (`Nuke 17.1v1 docs`) is preserved in the
> Raw Data.
