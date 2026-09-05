---
title: Performing a Render
source: Article
url: https://learn.foundry.com/katana/Content/ug/rendering_scene/performing_render.html
author: learn.foundry.com
ingested: 2026-09-04
app: "Katana"
version: "9.0 (learn.foundry.com/katana current docs at ingest; release notes whats_new_9.0)"
tags: [katana, lighting, lookdev, katana-9, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/performing-a-render/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Performing a Render

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/rendering_scene/performing_render.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Performing a Render You can start a render from the Katana UI by clicking Render and choosing a render option, or by right-clicking a node and choosing a render option. Bear in mind that not all options are available from all nodes. Note: For more information about the render options, see Render Types . For more information about which options are available from which node types, see Render Type Availability . To cancel the current render, press Esc , or select Render Cancel Current Render . To cancel all renders, press Shift + Esc on the keyboard or select Render Cancel All Renders . You can repeat the previous render by pressing Ctrl + \ ( backslash ), or choosing Render Repeat Previous Render . Note: You can also perform Preview Renders , Live Renders and Disk Renders using the Katana Queue options, for more information on the Katana Queue , see Katana Queue . Performing a Preview Render You can perform a Preview Render at any 3D node within your recipe. A scene description is generated up to that node. The extent that the scene is generated or deferred depends upon the renderer. The scene description is then sent to the actual production renderer, and the results are visible in the Monitor tab , the Catalog tab and the Monitor Layer in the Hydra Viewer . To perform a Preview Render : Right-click on a 3D node within your Node Graph . Select Preview Render . You can also start a Preview Render from a node currently set with the view flag by selecting Render Preview Render View Node , or by pressing Ctrl + P on the keyboard. Performing Multiple Simultaneous Preview Renders Multiple Preview Renders can be performed simultaneously in Katana . By default, if a Preview Render is already running and you start another, both Preview Renders continue until complete or canceled. Katana does not limit the number of Preview Renders you are able to run simultaneously, you are only limited by hardware capabilities. The ability to run multiple Preview Renders simultaneously is useful as it means you don't need to wait until one render is finished before starting a new one. This can help workflows for lighting artists, for example, as multiple camera angles can be rendered at once, streamlining the process of ensuring lighting is consistent across different shots. Multiple Preview Renders in the Catalog tab Multiple Preview Renders in the Monitor tab Note: You can start multiple Preview Renders by using the Start Multiple Renders dialog that you can find in the KatanaQueue shelf. For more information on the Katana Queue , see Katana Queue . Article: If you are experiencing issues when rendering in Katana , please refer to the Knowledge Base article: Troubleshooting Rendering Issues in Katana . Article: If you are using Linux and are experiencing issues where your render hangs, please refer to the Knowledge Base article: Render Hangs or Never Starts on Linux . Performing a Live Render Live Renders are useful for getting immediate feedback on changes you make to objects, cameras, lights, and materials. Within a Live Render session, changes to materials and object transformations on specified scene graph locations are communicated to the renderer. To start a Live Render : In the Scene Graph tab, check the objects in the Live Render Updates column that you would like to be able to trigger a Live Render to restart when changes are made to those objects. Right-click on the node that you want to start a Live Render from and select Live Render . You can also start a Live Render from a node currently set with the view flag by selecting Render Live Render View Node , or by pressing Ctrl + Shift + P on the keyboard. Adjust the parameters of any object in your Scene Graph that has been included for Live Render Updates . The image in the Monitor tab, Catalog tab and Monitor Layer updates in response to your actions. 3D node parameter values are finalized with all pending changes prior to performing a render. See Global Options to learn more about how to use the controls. See Starting Multiple Renders and Multiple Live Renders with Foresight+ for more information on performing multiple Live Renders simultaneously. Article: If you are experiencing issues when rendering in Katana , please refer to the Knowledge Base article: Troubleshooting Rendering Issues in Katana . Article: If you are using Linux and are experiencing issues where your render hangs, please refer to the Knowledge Base article: Render Hangs or Never Starts on Linux . Preview and Live Rendering with Nuke Bridge Nuke Bridge allows lighting and look development artists to see their work in the context of a Nuke render. You can stream your Katana Preview and Live renders to Nuke running either on your local machine or sitting on the render farm. Nuke Bridge offers three modes of operation depending on how you want to work with your render and composite: Preview Comp mode - Sends a Katana render to Nuke, then streams a comp back for a quick and easy snapshot of the render in the composite. This mode runs Nuke as a background process (locally or remotely). Live Comp mode - Allows you to make changes in the Katana project, such as change the render fed into the Nuke Input Points panel in the Nuke Bridge tab, and see those changes come back from Nuke. This mode also runs Nuke as a background process (locally or remotely). When used together with live rendering, you can adjust scene properties such as lighting, materials or cameras and receive the updated render back through Nuke. Interactive Comp mode - Launches Nuke so you can make edits to both your Katana scene and Nuke script simultaneously. See See a Nuke Comp of Your Project in Katana Using the Nuke Bridge for more information. Executing a Disk Render Disk Renders can only be performed from a Render node. Render nodes acts as a render point within a Katana recipe. To write a render pass to disk: Create a Render node and add it to the recipe. Add the Render node at the point in the recipe where you are happy with the interactive render. Tip: Add a RenderOutputDefine node above the Render node to define the output name, format, and file location. Right-click on the Render node and select Disk Render or Disk Render with Dependencies . The scene graph is generated up to that node and sent to the renderer. The render is saved to your temp directory or, if your recipe has a RenderOutputDefine node upstream of the Render node, the rendered output is saved to the locations specified there. Note: Unlike a Preview Render or Live Render , which show renders in the Monitor tab as they’re generated, the results of a Disk Render are only visible after the render is complete. Warning: Progressive interactive renders, when configured to send image updates (buckets) with high frequency, may flood the message queue of the renderer plug-in's display driver. To prevent this from consuming unreasonable amounts of memory, the queue is limited in size and, when full, results in delays in updates being sent to Katana . A warning is then printed to the Render Log. The size of the queue (as a number of messages) can be specified using the environment variable KATANA_PIPE_MAX_QUEUE_SIZE . The default size is 16384. Rendering From the Command-Line To render a scene from the command-line, you can use both Katana ’s Batch and Script modes: Batch mode - You must provide a filename or asset ID specifying the Katana project to render, the name of the Render node in the specified Katana project from which to render, and the frame range to render. For example, the following command renders the specified Katana project from the MyRenderNode node for frames 1 to 10 : katana --batch --katana-file=/path/to/myscene.katana --render-node=MyRenderNode -t 1-10 Script mode - This mode allows you to execute a Python script in Katana ’s Python environment, so you can perform more complex actions such as changing parameters, creating nodes, or modifying node connections, as well as launching renders. Note: For more information on how to use Batch and Script modes, see Command-line Interface . Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
Start a render from the **Render** menu or a node's right-click menu — **Preview** (static, in the Monitor/Catalog, never written to disk), **Live** (updates as you change flagged objects), or **Disk** (only from a **Render** node).

### Summary
The operational counterpart to *Render Types*. Preview Renders can be started at **any 3D node**, generating a scene description up to that node and sending it to the production renderer, with results in the Monitor tab, the Catalog tab and the Monitor Layer of the Hydra Viewer. **Multiple Preview Renders run simultaneously with no limit imposed by Katana** — only by hardware — which the page frames as a lighting workflow: render several camera angles at once rather than waiting. Live Renders require opting objects in via the **Live Render Updates** column in the Scene Graph tab; only those objects trigger a restart when changed, and 3D node parameter values are finalised with all pending changes before the render runs. Disk Renders are structurally different: they come **only from a Render node**, and without a **RenderOutputDefine** upstream the output lands in your temp directory. The page also documents **Nuke Bridge**, which streams Katana Preview and Live renders to Nuke — locally or on the farm — in three modes: **Preview Comp** (snapshot of the render in the composite, Nuke as a background process), **Live Comp** (change the Katana project and see the result return through Nuke, pairs with live rendering), and **Interactive Comp** (Nuke launched so both the Katana scene and the Nuke script can be edited at once).

### Key Steps
1. Start from **Render ›** an option, or right-click a node — available options depend on the node and on what the renderer plug-in advertises.
2. **Preview Render:** right-click a 3D node › **Preview Render**, or **Render › Preview Render › View Node**, or **`Ctrl`+`P`**.
3. Start as many Preview Renders as the hardware allows — both continue to completion; use the **Start Multiple Renders** dialog in the KatanaQueue shelf for a managed version.
4. **Live Render:** tick the objects in the Scene Graph's **Live Render Updates** column, then right-click the node › **Live Render**, or **Render › Live Render › View Node**, or **`Ctrl`+`Shift`+`P`**. Adjust the opted-in objects and watch the Monitor, Catalog and Monitor Layer update.
5. **Disk Render:** add a **Render** node where the interactive render looks right, put a **RenderOutputDefine** above it to set output name, format and location, then right-click › **Disk Render** or **Disk Render with Dependencies**. Without RenderOutputDefine the result goes to your temp directory.
6. **Cancel:** **`Esc`** or **Render › Cancel Current Render**; **`Shift`+`Esc`** or **Render › Cancel All Renders** for everything.
7. **Repeat** the previous render with **`Ctrl`+`\`** or **Render › Repeat Previous Render**.
8. **Comp in context with Nuke Bridge:** choose **Preview Comp**, **Live Comp** or **Interactive Comp** depending on whether you want a snapshot, a round-trip that reacts to Katana changes, or simultaneous editing of both applications.

### Nodes / Tools / Settings
- **Preview Render** (`Ctrl`+`P`), **Live Render** (`Ctrl`+`Shift`+`P`), **Disk Render** / **Disk Render with Dependencies** (Render nodes only).
- **Cancel Current Render** (`Esc`), **Cancel All Renders** (`Shift`+`Esc`), **Repeat Previous Render** (`Ctrl`+`\`).
- **Render** node (the render point), **RenderOutputDefine** (name, format, location — otherwise temp directory).
- **Live Render Updates** column in the Scene Graph tab — the opt-in that decides what triggers a restart.
- Destinations: **Monitor tab**, **Catalog tab**, **Monitor Layer** in the Hydra Viewer.
- **Katana Queue** / KatanaQueue shelf — **Start Multiple Renders** dialog; **Foresight+** for multiple simultaneous Live Renders.
- **Nuke Bridge** — **Preview Comp**, **Live Comp**, **Interactive Comp**; Nuke local or on the farm.
- Knowledge Base pointers on the page: *Troubleshooting Rendering Issues in Katana*, *Render Hangs or Never Starts on Linux*.

### Difficulty
Intermediate

### Foundry App & Version
Katana 9.0.

### Tags
`katana`, `lighting`, `lookdev`, `katana-9`, `intermediate`

---

## Related Tutorials
- [Render Types](render-types.md) — what each render option actually does.
- [Controlling Live Rendering](controlling-live-rendering.md) — the Live Render controls in detail.
- [RenderOutputDefine](renderoutputdefine.md) — the node this page tells you to put above the Render node.

---

> **Provenance.** `learn.foundry.com/katana` (MadCap Flare). Paths in this doc set
> are not guessable and `Data/Tocs/*` 404s, so this page was reached by crawling
> from `Content/learn_katana.html` → `user_guide.html`, or from a sibling page's
> own links. Reference-guide and user-guide pages carry clean `<title>`s and need
> no `--title` override, unlike `learn.foundry.com/nuke/developers/**`.
