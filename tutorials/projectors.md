---
title: Projectors
source: Article
url: https://learn.foundry.com/mari/7.5/Content/user_guide/projectors/projectors.html
author: learn.foundry.com
ingested: 2026-09-04
app: "Mari"
version: "7.5 (learn.foundry.com/mari/7.5; some embedded videos still show the Mari 3 workspace)"
tags: [mari-texturing, projection, mari-7, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/projectors/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Projectors

**Source:** [Article](https://learn.foundry.com/mari/7.5/Content/user_guide/projectors/projectors.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Projectors In Mari , projectors store the specific camera details of a particular view - the rotation, zoom, and orientation of the view, plus the current paintable area, the painting mode, and mask settings. Think of this as being like a bookmark for the exact view you currently have in Mari . You can use a projector to take “snapshots” of your paint buffer, work on them externally, and then project the changes back onto your model. For example, you can use projectors to easily flip back and forth between Mari and Photoshop ® , editing a texture in Photoshop ® , then projecting it back onto your model and checking it in Mari . Once you have created a projector, you can use it to project and unproject on and off the image: • Unproject takes everything visible from the paint buffer and saves it as a file. • Project reads a file and projects it back onto the model. Unprojecting takes the surface currently visible in Mari and exports it to a file. This includes everything on the surface, just as it appears onscreen - it's like taking a snapshot of the model as you can see it right now. So a particular unprojected file could include parts of several meshes. Once you have unprojected to a file, you can edit the file in your paint editor of choice. When you're happy with the file, you can then flip back to Mari and project it back onto the view. By restoring the original projector, you can be sure that you're looking at the exact same view as the snapshot was originally taken from. When you select the projector and click Import (to the buffer) or Project (import and bake), Mari projects the file onto the model in the correct place. So, once you've set up a particular projector, you can quickly flip between Mari and another editor. You only need to set the target and source files for unproject/project once, and then it's just a click to move back and forth between Mari and your external editor. To make it easier when you're working on projects with multiple channels, there is also a batch mode for both unproject and project . This lets you unproject multiple channels at once , or project a set of files back on to multiple channels at the same time . And to make it even easier to quickly project and unproject, there are Quick modes for both. These project and unproject from the current view, without you having to create a specific projector. There is also support for unprojecting to a layered .psd file. As with the standard project and unproject features, you can quickly unproject to a layered .psd file without having to create a projector. In addition, you can also project on to models using .fbx files created by 3rd party software such as Maya. Importing the model, cameras, and textures enables you to quickly create textured models using Mari projectors. Tip: If you only require a single camera view point, use the Camera Load Camera option from the Mari menubar. Projectors also allow you to export a turntable view of your model. The turntable takes the model as you can see it through the current shader, and creates a series of images showing the model rotating through an axis. You can include custom text or thumbnails of reference images in the turntable. You can create: • Render turntables - this exports a single channel, and lets you pick the shader and lighting to use. • Diagnostic turntables - these export a set of channels, using the default shader and flat lighting, to help you check the current look. The Projectors palette shows the projectors currently defined for the project. Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
A **projector** stores a view — rotation, zoom, orientation, paintable area, painting mode and mask settings — as a reusable bookmark, so you can **unproject** what you see to a file, edit it elsewhere, and **project** it back onto exactly the same view.

### Summary
This is the camera-projection workflow the gap named. A projector is not a camera so much as a **saved view state plus a file round-trip**: *Unproject* saves everything visible in the paint buffer to a file — a snapshot of the surface as it appears on screen, which may include parts of several meshes — and *Project* reads a file back onto the model. Because restoring the projector restores the exact view, the returning image lands in the right place, which is what makes the Mari↔Photoshop loop practical: set the source and target files once, then it is one click each way. Beyond the basic pair there are **batch modes** (unproject or project across **multiple channels at once**), **Quick modes** that work from the current view without creating a projector at all, support for unprojecting to a **layered `.psd`**, and projection onto models using **`.fbx` files from third-party software such as Maya** — importing model, cameras and textures together to build textured models quickly. Projectors also export **turntables**: **Render turntables** (single channel, your choice of shader and lighting) and **Diagnostic turntables** (a set of channels, default shader and flat lighting, for checking the look), optionally with custom text or reference thumbnails.

### Key Steps
1. Create a projector to bookmark the current view — rotation, zoom, orientation, paintable area, painting mode, mask settings.
2. **Unproject** to write everything visible in the paint buffer out to your **Output File Path**.
3. Edit the file in your paint editor of choice.
4. Return to Mari, restore the projector to guarantee the identical view, and use **Import (to the buffer)** for unbaked paint or **Project (import and bake)** to bake it on.
5. Set the source and target files **once** — after that the round trip is a single click each way.
6. Use **batch mode** to unproject several channels at once, or project a set of files back onto several channels together.
7. Use **Quick** unproject/project when you do not need a saved view — they work straight from the current one.
8. Unproject to a **layered `.psd`** when the external edit needs layers; this also works in Quick mode.
9. Project onto models with **`.fbx` files from third-party tools** (e.g. Maya), importing model, cameras and textures together. 💡 For a single viewpoint, the page suggests **Camera › Load Camera** instead of a projector.
10. Export a **turntable** — **Render** (one channel, chosen shader and lighting) or **Diagnostic** (several channels, default shader, flat lighting) — with optional custom text or reference thumbnails.

### Nodes / Tools / Settings
- **Projector** — stores rotation, zoom, orientation, paintable area, painting mode, mask settings.
- **Unproject** (buffer → file) and **Project** (file → model); **Import (to the buffer)** vs **Project (import and bake)**.
- **Batch** unproject/project across multiple channels; **Quick** modes with no projector; layered **`.psd`** unproject.
- **`.fbx`** projection from third-party software; **Camera › Load Camera** for a single viewpoint.
- **Turntables**: Render (single channel, chosen shader/lighting) and Diagnostic (multiple channels, default shader, flat lighting).
- The **Projectors palette** lists the projectors defined for the project.

### Difficulty
Intermediate

### Foundry App & Version
Mari 7.5.

### Tags
`mari-texturing`, `projection`, `mari-7`, `intermediate`

---

## Related Tutorials
- [Projectors Palette](projectors-palette.md) — every control behind these actions, including the colorspace handling.
- [Painting](painting.md) — the paint buffer a projector snapshots, and the Paint Through alternative.
- [Channels](channels.md) — what batch project/unproject iterates over.

---

> **Provenance.** `learn.foundry.com/mari/7.5` — Foundry's Mari documentation is
> **version-pathed** (`/mari/docs` redirects to `/mari/7.5/Content/learnhome/learn_mari.html`),
> unlike the Katana and Nuke doc sets. Mari is **not installed on this machine**
> (verified 2026-09-04), so unlike the Nuke pages these come from the public site
> rather than a bundled copy, and describe 7.5 rather than a build in use here.
> Several pages carry a note that their embedded video shows the Mari 3
> workspace while the workflow itself is unchanged.
