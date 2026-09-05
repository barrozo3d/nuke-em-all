---
title: Controlling Live Rendering
source: Article
url: https://learn.foundry.com/katana/Content/ug/rendering_scene/controlling_live_rendering.html
author: learn.foundry.com
ingested: 2026-09-04
app: "Katana"
version: "9.0 (learn.foundry.com/katana current docs at ingest; release notes whats_new_9.0)"
tags: [katana, lighting, katana-9, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/controlling-live-rendering/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Controlling Live Rendering

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/rendering_scene/controlling_live_rendering.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Controlling Live Rendering To start a Live Render : In the Scene Graph tab, check the objects in the Live Render Updates column that you would like to be able to trigger a Live Render to restart when changes are made to those objects. Right-click on the node that you want to start a Live Render from and select Live Render . You can also start a Live Render from a node currently set with the view flag by selecting Render Live Render View Node , or by pressing Ctrl + Shift + P on the keyboard. Adjust the parameters of any object in your Scene Graph that has been included for Live Render Updates . The image in the Monitor tab, Catalog tab and Monitor Layer updates in response to your actions. 3D node parameter values are finalized with all pending changes prior to performing a render. You can control Live Rendering behavior in a number of ways. For example, you can change which material and light edits trigger a Live Render, and when Live Render updates should take place. • In the Monitor and Scene Graph tabs as well as in the menu bar, you can choose how Live Rendering should take place with the 3D Update Mode. • In the Viewer tab, you can change from which render view point to Live Render. See more about the controls at Global Options . Note: Not all nodes have an immediate effect on the Live Render. For example adding a PrimitiveCreate node does not cause the new primitive to appear because adding new geometry is not supported in the render plug-ins. Note: The view node changes in the Node Graph tab are not reflected in the Scene Graph tab when the 3D Update Mode is set to Manual. Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
Live Rendering is **opt-in per object**: tick locations in the Scene Graph's **Live Render Updates** column, and only changes to those objects restart the render.

### Summary
Short and operational, and it carries two caveats worth more than its length. **Not all nodes affect a Live Render** — the page's own example is that adding a **PrimitiveCreate** node does *not* make the new primitive appear, because adding new geometry is not supported in the render plug-ins; a Live Render is for adjusting what already exists, not for building. And when **3D Update Mode is set to Manual**, view-node changes in the Node Graph are **not reflected in the Scene Graph tab**, which looks like a broken UI if you do not know it. Beyond that: 3D node parameter values are finalised with all pending changes before a render runs, the update behaviour (including which material and light edits trigger a restart, and when updates happen) is controlled by **3D Update Mode** from the Monitor tab, the Scene Graph tab or the menu bar, and the **Viewer tab** selects which viewpoint is live-rendered.

### Key Steps
1. In the **Scene Graph tab**, tick the objects you want to be able to trigger a restart in the **Live Render Updates** column.
2. Right-click the node to render from › **Live Render**; or **Render › Live Render › View Node**; or press **`Ctrl`+`Shift`+`P`**.
3. Adjust parameters on any opted-in object — the **Monitor tab**, **Catalog tab** and **Monitor Layer** update in response.
4. Set **3D Update Mode** (Monitor tab, Scene Graph tab, or menu bar) to control which material and light edits trigger a Live Render and when updates occur.
5. Change the live render viewpoint from the **Viewer tab**; see **Global Options** for the controls.
6. ⚠️ Do not expect new geometry to appear — **PrimitiveCreate** and similar have no immediate effect, because adding geometry is not supported in the render plug-ins.
7. ⚠️ With **3D Update Mode = Manual**, view-node changes in the Node Graph will **not** show in the Scene Graph tab.

### Nodes / Tools / Settings
- **Live Render Updates** column (Scene Graph tab) — the per-object opt-in.
- **Live Render** — right-click a node, **Render › Live Render › View Node**, or **`Ctrl`+`Shift`+`P`**.
- **3D Update Mode** — Monitor tab / Scene Graph tab / menu bar; **Manual** decouples the Scene Graph tab from view-node changes.
- **Viewer tab** — chooses the live render viewpoint; **Global Options** for the full control set.
- Outputs: Monitor tab, Catalog tab, Monitor Layer.
- Limitation: new geometry (e.g. **PrimitiveCreate**) does not appear — unsupported in the render plug-ins.

### Difficulty
Intermediate

### Foundry App & Version
Katana 9.0.

### Tags
`katana`, `lighting`, `katana-9`, `intermediate`

---

## Related Tutorials
- [Performing a Render](performing-a-render.md) — the full set of ways to start a render.
- [Render Types](render-types.md) — including the `makeInteractive` motion-blur caveat for Live Renders.

---

> **Provenance.** `learn.foundry.com/katana` (MadCap Flare). Paths in this doc set
> are not guessable and `Data/Tocs/*` 404s, so this page was reached by crawling
> from `Content/learn_katana.html` → `user_guide.html`, or from a sibling page's
> own links. Reference-guide and user-guide pages carry clean `<title>`s and need
> no `--title` override, unlike `learn.foundry.com/nuke/developers/**`.
