---
title: Projectors
source: Article
url: https://learn.foundry.com/mari/7.5/Content/user_guide/projectors/projectors.html
author: learn.foundry.com
ingested: 2026-09-04
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
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
