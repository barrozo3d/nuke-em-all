---
title: Painting
source: Article
url: https://learn.foundry.com/mari/7.5/Content/user_guide/painting/painting.html
author: learn.foundry.com
ingested: 2026-09-04
app: "Mari"
version: "7.5 (learn.foundry.com/mari/7.5; some embedded videos still show the Mari 3 workspace)"
tags: [mari-texturing, projection, mari-7, beginner]
extraction_status: complete
frames_dir: tutorials/frames/painting/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Painting

**Source:** [Article](https://learn.foundry.com/mari/7.5/Content/user_guide/painting/painting.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Painting Painting Paint Tools Painting a Constant Color Customizing Your Brush “Painting Through” an Image Clone Stamping Baking Paint onto the Model Blurring Baked Paint Read about elements of painting within Mari and the different tools you can use to achieve this. Familiarize yourself with features and functionality, as well as specific workflows you might be interested in. Here are some painting basics to get you started. Painting in Mari is similar to other standard paint programs. Paint using the various tools, then bake it onto your model. Most tools work on unbaked paint, but one or two also work directly on the baked paint on the surface. Each tool has a set of keys that control how it works. By default, the option keys for the current tool are shown on-screen at the top of the canvas. You can also use the Multi-Paint mode to paint into multiple shader streams at once. This painting method is a useful way to save time when working with texture packs and speeding up the painting process. More information can be found at Multi-Paint . Paint Tools To select a tool, select from your shelves or the Tools toolbar: Paint tools Select Available in Multi-Paint Transform Selected Objects Paint Available in Multi-Paint Roller Available in Multi-Paint Blur Available in Multi-Paint Paint Buffer Eraser Available in Multi-Paint Vector Paint Paint Through Available in Multi-Paint Gradient Clone Stamp Available in Multi-Paint Warp Available in Multi-Paint Slerp Available in Multi-Paint Pinup Available in Multi-Paint Towbrush Available in Multi-Paint Marquee Select Available in Multi-Paint Transform Paint Buffer Available in Multi-Paint Zoom Paint Buffer Vector Inspector Eye Dropper Painting a Constant Color 1. Click to select the Paint tool. 2. Click and drag to paint on the model. Video: You can paint a straight line by clicking one end point, moving the cursor, pressing Shift and clicking the second end point (watch this quick demo ) or pressing Shift and holding down the mouse button while moving horizontally or vertically (watch this quick demo ). These videos show the workflow using Mari 3. Even though the Mari 4 workspace is different, the workflow remains the same. To have a look at the main UI differences, see Mari 3.3 vs 4.0 . Customizing Your Brush 1. On the Tools toolbar, select a painting tool such as Paint , Blur , Vector Paint , Paint Through , Gradient , and Clone Stamp . 2. Open the Shelf palette: • from the View menu, select Palettes Shelf , or • right-click in the toolbar area and select Shelf from the dropdown menu. The Shelf palette displays. The Shelf palette contains seven shelves: • Menu - items that you can select from the F9 pie selection control menu. • Personal - selected items you use regularly. • Basic Brushes - a set of predefined basic brushes. • Hard Surface Brushes - a set of predefined hard surface brushes. • Organic Brushes - a set of predefined organic brushes. • Brad's New Brushes - a set of predefined brushes. • Project - items just for the current project. 3. Click the shelf where your brush is stored. 4. Click your brush to select it. 5. Open the Tool Properties palette and change the Brush Properties . Tip: There are many options for customizing your brush, including setting values for Paint , Pressure , Radius , Rotation , Bitmaps to use, Geometry and Noise . You can test the brush in the scratch pad at the bottom of the Tool Properties palette. 6. To save your customized brush, on the Tool Properties toolbar of your selected painting tool, drag the brush icon to the Shelf palette's shelf you selected previously. The modified brush displays in the selected shelf. “Painting Through” an Image 1. Open the Image Manager palette. 2. To load an image, click , navigate to and select the image file, and click Open . A thumbnail of the image displays, along with information about the selected image. 3. In the Tools toolbar, click (the Paint Through tool). 4. Drag and drop the image from the Image Manager to the canvas. 5. Adjust the image size and position: To... Do this... Resize Grab and drag its edges or corners, or press Ctrl / Cmd + Shift then click and drag. Move Grab the “handle” in the center of the image (or press Shift and click anywhere on the image), and drag. Rotate Click and drag outside the image, or press Ctrl / Cmd and drag inside the image. Press Shift when dragging outside the image to rotate in increments. Crop Double-click the image in the Image Manager , drag the area you want to crop, and click . Change the opacity In the Tool Properties palette, select Texture Preview , and change the Preview Alpha (enter a number or drag the slider). Pre-multiply alpha if your image has transparency. Reset the image In the Tool Properties palette, select Texture Transform Reset . 6. Paint! Tip: You can quickly switch between the Paint and Paint Through tools by pressing P and U . To hide the image, hold the ? key, to paint the whole image onto the model in one step, press the ' (apostrophe) key. Toggle repeat image to paint past the edge of the floating image and have the paint continue, by pressing the ; (semicolon) key. Note: When using this tool in Multi-Paint, only one stream will be visible as the Paint Through tool preview. This is the Primary Stream, which is indicated by the white eye icon ( ). Clone Stamping 1. Click to select the clone stamping tool. 2. Use the Source menu on the toolbar to select where to take the clone source from. You can select the current paint target, an image, or any of the paint layers in the project. 3. If you’re using an image as your clone source, hold down the Ctrl / Cmd key over the image and click to select the clone source point. Tip: When cloning from a paint layer, you can clone directly from the surface. In this mode, the tool clones the paint from the paint layer surface straight up into the paint buffer directly above that point. This lets you copy the model's surface into the paint buffer so you can edit it and then re-bake. To use this mode, hold down Shift + Ctrl when you click to set the origin point. For Mac, this shortcut is Cmd + Ctrl . 4. Paint to clone your selection on the model. Moving and Warping Paint To move paint on the model before baking: 1. In the Tools toolbar, click to select the Transform Paint Buffer tool. See Toolbars .. 2. Left-click anywhere on the paint buffer and drag to move the painting around on the model. 3. Ctrl / Cmd +left-click and drag to rotate the painting, or left-click and drag outside the paint buffer. 4. Ctrl / Cmd + Shift +left-click and drag to resize the painting, or grab the corners of the paint buffer and drag. Tip: The paint buffer is visible on-screen as a white box, but it may be larger than the view window and not visible. It becomes obvious if you move or resize the painting. To reset the paint buffer to its default values click the Reset button in the Painting palette under Paint Buffer Transform . You can also click the Reset Paint Buffer Transform button on the Paint Buffer toolbar. To warp paint before baking: Using this tool... You can... Warp Shift +click and drag to create a warp grid. Click and drag the points around to warp the paint. To increase or decrease the grid resolution, press the up or down arrow keys. Slerp Use the Slerp Mode menu on the toolbar to set the mode (from Pull , Grow , Shrink , or Rotate ). Click and drag to apply your effect. Erase distortion by selecting the Erase r mode. Pinup Shift +click to set “pins”. Then click and drag to move the pins. You can use pins to protect parts of the paint that you don't want affected by the distortion. Baking Paint onto the Model To bake paint onto your model: 1. Make sure all patches you want to bake are selected. 2. Do one of the following: Type shortcut key or click on status bar icon B Tip: Whenever you change your view of the model, it bakes automatically. You can change this setting in the Painting Palette under Projection Settings Projection if required. You can change this setting in the Painting Palette under Projection Settings Projection if required. Blurring Baked Paint 1. Click to select the blur tool. 2. Left-click and drag to blur paint baked on the surface. Tip: As with the paint tools, you can edit the blur brush tip. When you have finished blurring the paint, you need to bake. Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
Paint into the **paint buffer** with one of Mari's tools, then **bake** it onto the model — with **Paint Through** (an image dragged from the Image Manager onto the canvas) as the projection-painting route.

### Summary
The painting overview, and the page that connects the paint buffer to everything else. Most tools work on **unbaked** paint in the buffer; one or two act directly on baked paint on the surface, and each tool shows its option keys at the top of the canvas by default. **Multi-Paint** mode paints into several shader streams at once, which is how texture packs get built without repeating work — the tool list marks which tools support it (most do; Paint Buffer Eraser, Vector Paint, Gradient, Zoom Paint Buffer, Vector Inspector and Eye Dropper are among those listed without the Multi-Paint marker). The section that matters for the projection-painting gap is **"Painting Through" an Image**: load an image into the **Image Manager**, select the **Paint Through** tool, drag the image onto the canvas, then resize, move, rotate and crop it interactively before painting. The shortcut set is worth memorising — **`P`** and **`U`** swap between Paint and Paint Through, holding **`?`** hides the image, **`'`** paints the whole image onto the model in one step, and **`;`** toggles repeat so paint continues past the floating image's edge.

### Key Steps
1. Select a tool from a shelf or the **Tools** toolbar; read its option keys at the top of the canvas.
2. Paint into the buffer, then **bake** onto the model — most tools never touch baked paint directly.
3. Use **Multi-Paint** to paint into multiple shader streams simultaneously when building texture packs.
4. **Customise a brush:** pick a painting tool, open the **Shelf** palette (View › Palettes › Shelf, or right-click the toolbar area), choose a shelf and brush, then edit **Brush Properties** in the **Tool Properties** palette.
5. Test in the **scratch pad** at the bottom of Tool Properties, then save by dragging the brush icon from the Tool Properties toolbar onto a shelf.
6. **Paint Through:** open the **Image Manager**, load an image, select the **Paint Through** tool, and drag the image from the palette onto the canvas.
7. Position it — **resize** by dragging edges/corners or `Ctrl`/`Cmd`+`Shift`+drag; **move** via the centre handle or `Shift`+click-drag; **rotate** by dragging outside the image or `Ctrl`/`Cmd`+drag inside (hold `Shift` for increments); **crop** by double-clicking it in the Image Manager.
8. Set opacity in **Tool Properties › Texture Preview › Preview Alpha**, and **pre-multiply alpha** if the image has transparency; reset with **Texture Transform › Reset**.
9. Use the shortcuts: **`P`** / **`U`** to swap Paint and Paint Through, **`?`** (held) to hide the image, **`'`** to paint the whole image in one step, **`;`** to toggle repeat past the image edge.
10. Paint a straight line by clicking one end, moving, then `Shift`+clicking the second — or `Shift`+drag horizontally/vertically.

### Nodes / Tools / Settings
- **Paint tools:** Select, Transform Selected Objects, Paint, Roller, Blur, Paint Buffer Eraser, Vector Paint, **Paint Through**, Gradient, **Clone Stamp**, Warp, Slerp, Pinup, Towbrush, Marquee Select, Transform Paint Buffer, Zoom Paint Buffer, Vector Inspector, Eye Dropper — with per-tool Multi-Paint availability.
- **Shelf palette** shelves: Menu (the `F9` pie menu), Personal, Basic Brushes, Hard Surface Brushes, Organic Brushes, Brad's New Brushes, Project.
- **Tool Properties** — Brush Properties (Paint, Pressure, Radius, Rotation, Bitmaps, Geometry, Noise), scratch pad, **Texture Preview › Preview Alpha**, **Texture Transform › Reset**.
- Shortcuts: `P` / `U`, `?` (hide), `'` (whole image), `;` (repeat), `Shift`-click for straight lines, `F9` pie menu.
- Related topics on the page: Painting a Constant Color, Clone Stamping, **Baking Paint onto the Model**, Blurring Baked Paint.

### Difficulty
Beginner

### Foundry App & Version
Mari 7.5; embedded demo videos show the Mari 3 workspace with the workflow unchanged.

### Tags
`mari-texturing`, `projection`, `mari-7`, `beginner`

---

## Related Tutorials
- [Image Manager Palette](image-manager-palette.md) — where Paint Through images live and how their colorspace is set.
- [Painting Palette](painting-palette.md) — paint buffer depth and size, and the source grade applied when cloning or painting through.
- [Projectors](projectors.md) — the other route for getting an external image onto the model.

---

> **Provenance.** `learn.foundry.com/mari/7.5` — Foundry's Mari documentation is
> **version-pathed** (`/mari/docs` redirects to `/mari/7.5/Content/learnhome/learn_mari.html`),
> unlike the Katana and Nuke doc sets. Mari is **not installed on this machine**
> (verified 2026-09-04), so unlike the Nuke pages these come from the public site
> rather than a bundled copy, and describe 7.5 rather than a build in use here.
> Several pages carry a note that their embedded video shows the Mari 3
> workspace while the workflow itself is unchanged.
