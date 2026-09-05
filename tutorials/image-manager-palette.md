---
title: Image Manager Palette
source: Article
url: https://learn.foundry.com/mari/7.5/Content/reference_guide/image_manager_palette.html
author: learn.foundry.com
ingested: 2026-09-04
app: "Mari"
version: "7.5 (learn.foundry.com/mari/7.5; some embedded videos still show the Mari 3 workspace)"
tags: [mari-texturing, projection, color-management, mari-7, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/image-manager-palette/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Image Manager Palette

**Source:** [Article](https://learn.foundry.com/mari/7.5/Content/reference_guide/image_manager_palette.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Image Manager Palette The Image Manager palette and the controls that can be found on it are described in the table below. When controls also bring up additional dialogs, these are referenced for more information. What It Does The Image Manager lets you store and work with images in your project, including using them for brushes and painting through them onto your model. For organization purposes, you can also add custom tabs to the palette by clicking the add tab button. You can also create Image Groups to organize your project’s images. Image Manager Palette Fields Control Type What it does Opens this dialog box Image Info Info Depth information The color depth of the currently selected image in bytes. Channels information The color components of the currently selected image. File Space dropdown File space of the currently selected image from the options: • NORMAL • VECTOR • VECTOR_Y_FLIP • NORMAL_Y_FLIP Tiled Image information Whether the image is tiled - true or false. Height information The height of the currently selected image in pixels. Width information The width of the currently selected image in pixels. Path information The file path to the image that Mari is accessing. If the original image was saved to another location this is the file path shown, not the path to the original file. Image Info User Attributes Comment text field Assign a user-defined comment to the image. MriImportFilePath information The file path to the original image. MriLastImportDateTime information The date and time that the file was first loaded into Mari. Colorspace Colorspace dropdown The colorspace to which the output values are converted. Automatic is determined by the file name, size, and type of data in the image. Tip: You can limit the number of colorspaces available to artists using the Python API registerConfigUiAllowlist() function or the MARI_COLORSPACE_OCIO_UI_ALLOWLIST environment variable. See Help SDK Python Documentation from Mari's UI menus or Environment Variables That Mari Recognizes for more details. Raw Data checkbox If this is enabled, the image data is not converted. Note: As the raw colorspace nullifies the corresponding colorspace transform when either used as the input or output, there is a discrepancy between what is shown in the Image Manage palette thumbnail and the image viewer. This is the expected behavior. button Adds an image to the Image Manager. Open an Image Dialog button Removes the selected image from the Image Manager. button Opens the selected image in another window, where you can crop it. image button Saves the selected image to a file. Save As Dialog Send Image to 2D Paint button Opens your image in the 2D tab. Mari will add a new object and import the image as a Paint Node . The node graph will show Bottom Transparency + Paint node (with the image imported) merged and connected to a channel node. Using 2D Paint Mode image window button Crops the current image. Mari copies the cropped area as a separate image in the Image Manager . The cropped image is part of the project, but won't be saved as a separate image file unless you use the Save As option. Select one of the following crop modes: • Arbitrary - click-and-drag on an arbitrary area of the image. • Fixed - enter a fixed size for the crop box (in pixels) and drag it to the area you want to crop. • Aspect - enter a fixed aspect ratio for the crop box (in pixels) and drag it over the area you want to crop. Once you have selected the crop area, click the mouse button to crop. Colorspace dropdown The colorspace to which the output values are converted. Automatic is determined by the file name, size, and type of data in the image. Raw Data checkbox If this is enabled, the image data is not converted. Note: As the raw colorspace nullifies the corresponding colorspace transform when either used as the input or output, there is a discrepancy between what is shown in the Image Manage palette thumbnail and the image viewer. This is the expected behavior. Image Group window Shader Model dropdown Defines the available shader models you can assign images to. The available options are: • 3Delight Principled • Arnold Standard Surface • Autodesk Standard Surface (1.0.2.x) • BRDF • Principled BRDF • USD Preview Surface • Unreal • VRayMtl • VRayMtl (V-Ray 6) Ingest Template submenu Apply preset configurations for specific texture vendors to the shader model. There are two options: • Apply to Current Shader Model - matches images to streams based on filenames in the selected preset. This will only apply for the Shader model selected in the dropdown. • Apply to All Shader Models -matches images to streams based on filenames in the selected preset. This will be applied across all shader models. Available texture vendors to apply templates to are: • CCO_Textures Friendlyshade • GameTexture • Poliigon • Quixel • RealDisplacementTextures • Substance • TextureHaven • Textures_Com • TexturingXYZ Auto-Assign Images Button Auto-assigns the images in the Image group to the corresponding shader channels, based on naming conventions of images. Search Text input Search for a specific stream in the shader model. Lock Stream Unlocked: Locked: Button Locks the specific stream. When a stream is locked, it will not be altered when the Auto-assign and Ingest template tools are used. You can still manually change the stream by using the image dropdown and picking a new image Stream n/a The shader stream that the image can be assigned to. Image Dropdown Defines the image assigned to the shader stream. Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
The **Image Manager** stores the project's images — for brushes, for painting through, for cropping and for shader assignment — with per-image colorspace handling and an **Auto-Assign** that matches images to shader streams by filename.

### Summary
The Image Manager is where images enter a Mari project, and the reference reveals two capabilities that matter beyond storage. First, **colorspace per image**: a **Colorspace** dropdown (with `Automatic` deciding from filename, size and data type) plus a **Raw Data** checkbox that bypasses conversion — with a documented and deliberately-not-a-bug consequence that a raw image's palette **thumbnail and image viewer disagree**, because raw nullifies the transform on input or output. Colorspace choice can also be constrained studio-wide through the Python API's `registerConfigUiAllowlist()` or the **`MARI_COLORSPACE_OCIO_UI_ALLOWLIST`** environment variable. Second, **Image Groups with shader-model ingest templates**: pick a **Shader Model** (3Delight Principled, Arnold Standard Surface, Autodesk Standard Surface, BRDF, Principled BRDF, USD Preview Surface, Unreal, VRayMtl, VRayMtl V-Ray 6), then apply an **Ingest Template** for a specific texture vendor — **Substance**, **Quixel**, **Poliigon**, **GameTexture**, **TextureHaven**, **Textures_Com**, **TexturingXYZ**, **RealDisplacementTextures**, **CCO_Textures Friendlyshade** — to either the current shader model or all of them, and let **Auto-Assign Images** match by naming convention. The palette also exposes per-image info (depth, channels, **File Space** as `NORMAL` / `VECTOR` / `VECTOR_Y_FLIP` / `NORMAL_Y_FLIP`, tiled, dimensions, path), user attributes including the original import path and first-load timestamp, cropping in three modes, and **Send Image to 2D Paint**.

### Key Steps
1. Add images with the add button; remove with the delete button; organise with **custom tabs** and **Image Groups**.
2. Read the info block — colour **Depth**, **Channels**, **File Space** (`NORMAL`, `VECTOR`, `VECTOR_Y_FLIP`, `NORMAL_Y_FLIP`), **Tiled**, **Height**, **Width**, and the **Path** Mari is actually reading (which is the re-saved location, not necessarily the original).
3. Check **User Attributes** for **MriImportFilePath** (the original file) and **MriLastImportDateTime** (first load).
4. Set **Colorspace** per image, or leave `Automatic` to infer from filename, size and data type; enable **Raw Data** to prevent conversion. ⚠️ Expect the thumbnail and image viewer to differ for raw images — documented as expected behaviour.
5. Constrain the colorspace list for artists via `registerConfigUiAllowlist()` or **`MARI_COLORSPACE_OCIO_UI_ALLOWLIST`**.
6. **Crop** in the image window using **Arbitrary**, **Fixed** (pixel size) or **Aspect** (fixed ratio); the crop becomes a separate image in the project, saved to disk only via **Save As**.
7. **Send Image to 2D Paint** to open it in the 2D tab — Mari adds a new object, imports the image as a **Paint Node**, and wires Bottom Transparency + Paint into a channel node.
8. In an **Image Group**, choose the **Shader Model**, apply an **Ingest Template** for your texture vendor to the current or all shader models, then click **Auto-Assign Images** to match images to streams by filename.
9. Use **Search** to find a stream, and **Lock Stream** to stop an assignment changing.

### Nodes / Tools / Settings
- **Image Manager palette** — add / remove / crop / save-as / **Send Image to 2D Paint**; custom tabs; **Image Groups**.
- Info: Depth, Channels, **File Space** (`NORMAL`, `VECTOR`, `VECTOR_Y_FLIP`, `NORMAL_Y_FLIP`), Tiled, Height, Width, Path; user attributes **Comment**, **MriImportFilePath**, **MriLastImportDateTime**.
- **Colorspace** (with `Automatic`), **Raw Data**; `registerConfigUiAllowlist()`, **`MARI_COLORSPACE_OCIO_UI_ALLOWLIST`**.
- Crop modes: **Arbitrary**, **Fixed**, **Aspect**.
- **Shader Model** list: 3Delight Principled, Arnold Standard Surface, Autodesk Standard Surface (1.0.2.x), BRDF, Principled BRDF, USD Preview Surface, Unreal, VRayMtl, VRayMtl (V-Ray 6).
- **Ingest Template** vendors: CCO_Textures Friendlyshade, GameTexture, Poliigon, Quixel, RealDisplacementTextures, Substance, TextureHaven, Textures_Com, TexturingXYZ — applied to the current or all shader models.
- **Auto-Assign Images**, **Search**, **Lock Stream**.

### Difficulty
Intermediate

### Foundry App & Version
Mari 7.5.

### Tags
`mari-texturing`, `projection`, `color-management`, `mari-7`, `intermediate`

---

## Related Tutorials
- [Painting](painting.md) — the Paint Through workflow that drags images out of this palette onto the canvas.
- [Projectors Palette](projectors-palette.md) — the same colorspace and Raw Data decisions on the projector round trip.

---

> **Provenance.** `learn.foundry.com/mari/7.5` — Foundry's Mari documentation is
> **version-pathed** (`/mari/docs` redirects to `/mari/7.5/Content/learnhome/learn_mari.html`),
> unlike the Katana and Nuke doc sets. Mari is **not installed on this machine**
> (verified 2026-09-04), so unlike the Nuke pages these come from the public site
> rather than a bundled copy, and describe 7.5 rather than a build in use here.
> Several pages carry a note that their embedded video shows the Mari 3
> workspace while the workflow itself is unchanged.
