---
title: RenderOutputDefine
source: Article
url: https://learn.foundry.com/katana/Content/rg/3d_nodes/renderoutputdefine.html
author: learn.foundry.com
ingested: 2026-08-31
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/renderoutputdefine/
frame_count: 0
frame_status: skipped
---

# RenderOutputDefine

**Source:** [Article](https://learn.foundry.com/katana/Content/rg/3d_nodes/renderoutputdefine.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** RenderOutputDefine Specifies output of an image (color, AOV, shadow map, or similar) to a file. In RIB, this means a Display statement. Connection Type Connection Name Function Input input The place in the node graph where you want to define the output settings for rendering. Control (UI) Default Value Function outputName primary Associates a name with the display. Typically primary by default; often shadow for shadow maps, and similar conventions. This name appears in the Render node, along with (or as) the default primary . type color Specifies the type of output. • color - mostly used to render out rgb beauty files, but also can be used for rendering out z, P(point), N(normals), Ci(final shader color) passes. • raw - allows you to directly specify the values for a Display line. Since the output could be anything, Katana doesn't do any colorspace conversion on this output, and can't support tiling. • script - run a script on another RenderOutputDefine, like txmake. • prescript - run a script before the render is started. • none - clears the output. If the output was previously setup by a different RenderOutputDefine node, this removes the entry. includedByDefault Yes When enabled, this Render Definition is sent to the Render node. rendererSettings colorSpace linear Sets the output colorspace used. fileExtension exr Sets the output file format. channel rgba Sets the channels to output. You can also set a user-defined channel from a PrmanOutputChannelDefine node. When fileExtension: exr; convertSettings exrCompression Scanline ZIP Defines the exr compression method to use. All methods are lossless (with the exception of Pixar 24 , which is lossless but quantizes the pixels to 24-bit float). Wavelet is generally preferable as it offers ~2:1 compression even on grainy data. • None - • RLE - • Scanline ZIP - • Block ZIP - • Wavelet - • Pixar 24 - exrBitDepth 16 Sets the floating point precision of the rendered exr file: • 16 - half float. This is recommended for all color passes. • 32 - full float. This is recommended for all ncf data arbitrary output variables (AOVs). exrOptimize Yes When enabled, the exr file is written out in an a manner optimized for efficient random tile-access. These optimizations greatly improve memory usage and performance for programs, which process images in tiles. exrType Tiled Sets whether the exr file is written to support: • Tiled - random tile access. • Scanline - random scanline access. When fileExtension: exr clampOutput No When set to Yes , post-render clamp negative rgb values to 0, and clamp alpha values to 0-1. Note: clampOutput has no effect on NaN and inf values. colorConvert Yes When set to Yes , post-render convert rendered image data from linear to the output colorspace specified in the filename. The default value of Yes is suitable for nearly every situation, since the linear output of the render is converted to the colorspace in the filename. A case where you would want to set this to No is if you know the data being rendered is in a colorspace other than linear, such as the re-projection of a log plate, and you want to name the output file log without a linear to log conversion. When fileExtension: png; convertSettings pngBitDepth 16 Sets the bit depth of the rendered file: • 8-bit • 16-bit When fileExtention: rla; convertSettings rlaBitDepth 16 Sets the bit depth of the rendered file: • 8-bit • 10-bit • 16-bit • 32-bit When fileExtention: tif; convertSettings tifBitDepth 16 The bit depth of the rendered file: • 8-bit • 16-bit • 32-bit tifCompression LZW The tif compression method to use: • None - No compression method is used. • LZW - The LZW compression method is used. This is lossless, so it is usually preferable to use it unless there is an issue with compatibility in the target reader. When fileExtension: tif clampOutput No When set to Yes , post-render clamp negative rgb values to 0, and clamp alpha values to 0-1. Note: clampOutout has no effect on NaN and inf values. colorConvert Yes When set to Yes , post-render convert rendered image data from linear to the output colorspace specified in the filename. The default value of Yes is suitable for nearly every situation, since the linear output of the render is converted to the colorspace in the filename. A case where you would want to set this to No is if you know the data being rendered is in a colorspace other than linear, such as the re-projection of a log plate, and you want to name the output file log without a linear to log conversion. When fileExtension: jpg jpgQuality 100 The quality to use when generating the jpg file. Higher values generate larger file sizes, with 100 representing the best quality image and 0 representing the lowest. rendererSettings parameters continued computeStats None Allows you to compute image statistics as a post process, appending as exr metadata. Select: • None • Raw • Depth Note: In depth mode, zero values and very large values are ignored. In both modes, only the region within the dataWindow is considered. tempRenderLocation N/A cameraName N/A Describes the scene graph location of camera to render from. If empty, render from the camera specified in renderSettings.cameraName at /root . The cameraName parameter options are available by clicking the dropdown menu. For more information, refer to the Scene Graph Location Widget Type in Common Parameter Widgets . locationType local When locationType: file; locationSettings renderLocation Specify the render location, or bring up the file browser or your studio's asset management browser to select the location to use. For more information, refer to the Asset and File Path Widget Types in the Common Parameter Widgets . Note: RenderOutputLocation plug-ins that are shipped as source and can be found in plugins/Src/RenderOutputLocations . Can't find what you're looking for? Use our feedback widget on the right to request more information.



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
