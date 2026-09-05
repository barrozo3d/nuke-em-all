---
title: Render Types
source: Article
url: https://learn.foundry.com/katana/Content/ug/rendering_scene/render_types.html
author: learn.foundry.com
ingested: 2026-09-04
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
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
