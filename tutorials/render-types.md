---
title: Render Types
source: Article
url: https://learn.foundry.com/katana/Content/ug/rendering_scene/render_types.html
author: learn.foundry.com
ingested: 2026-09-04
app: "Katana"
version: "9.0 (learn.foundry.com/katana current docs at ingest; release notes whats_new_9.0)"
tags: [katana, lighting, katana-9, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/render-types/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Render Types

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/rendering_scene/render_types.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Render Types Katana has a number of context-sensitive render options, available through the right-click menu on nodes. Renderer plug-ins advertise the methods they support, so the right-click menu render options shown depend on the node selected and the methods advertised in the renderer plug-in. Note: For more information about which options are available from which nodes, see Render Type Availability . For more information about how to start a render, see Performing a Render . All render options send the scene graph, as generated at the selected node, to the selected production renderer. The exact options you see may vary, depending on the configuration of your studio’s plug-ins, but the default set is: Preview Rendering Preview Render - The render is a static image, displayed in the Monitor tab, Monitor Layer and Catalog tab. The image is not written to disk. Live Rendering Live Render - Similar to Preview Render , except that under Live Render , changes to the camera, lights, materials, or geometry transformations result in updates to the image displayed in the Monitor tab Monitor Layer and Catalog tab. See Changing How to Trigger a Live Render for more on which activities trigger a Live Render , and how to edit them. Note: Motion blur in Live Rendering is not supported for interactive cameras. To enable motion blur in a live render session, set the camera’s makeInteractive parameter to No . If you bring in an animated camera through an Alembic or other external file, the camera keeps its animation, even when makeInteractive is set to No . Tip: To stop any current render, including Live Rendering , either press Esc or select Render Cancel Current Render in the menu bar. To stop all renders, press Shift + Esc or select Render Cancel All Renders . Alternatively, starting a new Live Render automatically stops the previous Live Render and doesn't need to be specifically canceled using either of the methods above. It is possible to perform multiple Live Renders simultaneously using the experimental option in the Start Multiple Renders script for the Katana Queue . For more information, see Katana Queue . Profile Rendering Preview Render with Profiling - This performs a normal Preview Render , but also captures information about which Ops have run, the amount of CPU used by them to cook locations, and the amount of memory used for attributes and Lua scripts. Note: For more information, see Geolib3-MT Profiling . Disk Rendering Disk Render - the scene is written to disk, at the location specified in a Render node, and for this reason, is only available from Render nodes. Disk Render with Dependencies - writes a Disk Render , along with any dependencies of the Render node, to disk. Render Dependencies Only - renders just dependencies to disk. Render Farms Any render farm plugins that you have set up in Katana can be accessed here from any 3D node. Katana ships with a render queue system called Katana Queue . Katana Queue - Send a Preview , Live or Disk Render to the Katana Queue . Renders sent to Katana Queue can be viewed in the Katana Queue tab. Note: For more information, see Katana Queue . Disk Render Dependencies Katana offers the option of rendering any dependencies before either Preview or Live Rendering. See Setting up Render Dependencies for more on dependencies. 3D nodes have a right-click menu sub-heading, Disk Render Dependencies that holds the following options: Before Preview Renders - when selected, render dependencies (such as shadow maps) are rendered to disk before performing a Preview Render . Before Live Renders - when selected, render dependencies are rendered to disk before Live Rendering . Before Profiling Renders - when selected, render dependencies are rendered to disk before Profile Rendering . Disk Render Upstream Render Outputs Nodes that have rendered 2D images from other Katana nodes as dependencies have a right-click menu sub-heading, Disk Render Upstream Render Outputs that holds the following options: Preview Renders: Unless Already Cached - when selected, during a Preview render all incoming image dependencies are rendered to disk, unless they have already been rendered to disk and cached. Preview Renders: Always - when selected, during a Preview render all incoming image dependencies are rendered to disk, regardless of whether they are already cached or not. Disk Renders: Always - this is for information only. This option cannot be changed. During a disk render , all incoming image dependencies are rendered to disk, regardless of whether they are already cached or not. Debugging 3D nodes have a right-click menu sub-heading Debugging , which offers options to view debug information in a text editor. The options are: Debugging Open Filter Text Output in your text editor - displays the Katana filters used to traverse the scene graph. Debugging Open your renderer’s debug file type Output in your text editor - displays the debug file type of your selected renderer. Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
Katana's render options are **context-sensitive**: renderer plug-ins advertise which methods they support, so the right-click menu shows only what the selected node and the installed plug-in can actually do.

### Summary
The reference half of the rendering pair. Every option sends the scene graph *as generated at the selected node* to the production renderer; the default set is **Preview Render** (static, displayed, never written to disk), **Live Render** (the same but updating on changes to camera, lights, materials or geometry transforms), **Preview Render with Profiling** (a normal preview that also captures which Ops ran, the CPU they used to cook locations, and the memory used for attributes and Lua scripts — Geolib3-MT profiling), and the disk family: **Disk Render**, **Disk Render with Dependencies**, **Render Dependencies Only**. Two operational details are easy to lose: **starting a new Live Render automatically stops the previous one**, so it needs no explicit cancel; and **motion blur in Live Rendering is not supported for interactive cameras** — set the camera's `makeInteractive` parameter to **No**, and note that a camera animated in via Alembic or another external file keeps its animation even then. The page also documents dependency behaviour — **Disk Render Dependencies** (render shadow maps and similar before Preview, Live or Profiling renders) and **Disk Render Upstream Render Outputs** (`Unless Already Cached` / `Always` for previews; always, unchangeably, for disk renders) — plus a **Debugging** submenu that opens the Katana filters used to traverse the scene graph, or the renderer's own debug output, in a text editor.

### Key Steps
1. Right-click the node you want to render from — the options shown depend on the node type and the renderer plug-in's advertised methods.
2. **Preview Render** for a static image in the Monitor tab, Monitor Layer and Catalog tab; nothing is written to disk.
3. **Live Render** when you need changes to camera, lights, materials or geometry transforms to update the displayed image.
4. ⚠️ For motion blur under Live Rendering, set the camera's **`makeInteractive`** to **No** — interactive cameras do not support it. Alembic/external animated cameras keep their animation regardless.
5. Stop a render with **`Esc`** / **Render › Cancel Current Render**, or all with **`Shift`+`Esc`** — but note **a new Live Render cancels the previous one by itself**.
6. **Preview Render with Profiling** to capture Ops run, CPU used cooking locations, and memory used by attributes and Lua scripts (see Geolib3-MT Profiling).
7. **Disk Render** from a Render node; **Disk Render with Dependencies** to include the node's dependencies; **Render Dependencies Only** for just those.
8. Send work to a farm plug-in, or to the bundled **Katana Queue** (Preview, Live or Disk), and watch it in the Katana Queue tab.
9. Set **Disk Render Dependencies** per render kind — **Before Preview Renders**, **Before Live Renders**, **Before Profiling Renders**.
10. Set **Disk Render Upstream Render Outputs** for image dependencies — **Preview Renders: Unless Already Cached**, **Preview Renders: Always**; **Disk Renders: Always** is informational and cannot be changed.
11. Use the **Debugging** submenu to open the traversal filters, or the renderer's debug file type, in a text editor.

### Nodes / Tools / Settings
- **Preview Render**, **Live Render**, **Preview Render with Profiling**, **Disk Render**, **Disk Render with Dependencies**, **Render Dependencies Only**.
- **Katana Queue** (ships with Katana) and any configured render farm plug-ins; Katana Queue tab.
- **`makeInteractive`** camera parameter — set to **No** for motion blur in Live Renders.
- **Disk Render Dependencies**: Before Preview / Live / Profiling Renders.
- **Disk Render Upstream Render Outputs**: Unless Already Cached, Always (previews); Always (disk, fixed).
- **Debugging** submenu — filter text output; renderer debug output.
- Referenced: *Render Type Availability*, *Geolib3-MT Profiling*, *Setting up Render Dependencies*, *Changing How to Trigger a Live Render*.

### Difficulty
Intermediate

### Foundry App & Version
Katana 9.0.

### Tags
`katana`, `lighting`, `katana-9`, `intermediate`

---

## Related Tutorials
- [Performing a Render](performing-a-render.md) — how to actually start each of these.
- [Controlling Live Rendering](controlling-live-rendering.md) — the Live Render opt-in and update modes.

---

> **Provenance.** `learn.foundry.com/katana` (MadCap Flare). Paths in this doc set
> are not guessable and `Data/Tocs/*` 404s, so this page was reached by crawling
> from `Content/learn_katana.html` → `user_guide.html`, or from a sibling page's
> own links. Reference-guide and user-guide pages carry clean `<title>`s and need
> no `--title` override, unlike `learn.foundry.com/nuke/developers/**`.
