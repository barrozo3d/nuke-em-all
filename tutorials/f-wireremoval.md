---
title: F_WireRemoval
source: Article
url: file:///C:/Program%20Files/Nuke17.1v1/Documentation/html/content/reference_guide/furnacecore_nodes/f_wireremoval.html
author: Nuke 17.1v1 bundled documentation
ingested: 2026-09-04
app: "NukeX (FurnaceCore)"
version: "Nuke 17.1v1 (bundled documentation, Documentation/html/content)"
tags: [furnace, nukex, clean-plate, roto, tracking, nuke-17, advanced]
extraction_status: complete
frames_dir: tutorials/frames/f-wireremoval/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# F_WireRemoval

**Source:** [Article](file:///C:/Program%20Files/Nuke17.1v1/Documentation/html/content/reference_guide/furnacecore_nodes/f_wireremoval.html)
**Author:** Nuke 17.1v1 bundled documentation
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** F_WireRemoval F_WireRemoval is particularly good at removing wires over heavily motion blurred backgrounds or wires over smoke, dust, or clouds. It can be used to remove each wire in a sequence or to quickly create a clean plate which can then be tracked into place. F_WireRemoval also incorporates a tracker which automatically tracks a moving wire through a clip. This tracker has its own control panel, which will float inside the Viewer if you have checked Show On Screen Controls in the F_WireRemoval controls. See also RotoPaint . Inputs and Controls Connection Type Connection Name Function Input CleanPlate An optional input to allow you to supply a clean plate. This is used by the Clean Plate repair mode which will warp the clean plate onto the current frame and use the warped image to reconstruct the background behind the wire. Source The clip containing the wire to be removed. Control (UI) Knob (Scripting) Default Value Function F_WireRemoval Tab setUserKeyFrame N/A Create user key frame - creates a user key frame. deleteUserKeyFrame N/A Delete user key frame - deletes a user key frame. snapToWire N/A Snap to wire - finds the edges of the wire and snaps the edges of the region onto them. trackBwd N/A Track backwards - plays backwards through the sequence tracking from frame to frame. stepBwd N/A Step backward - tracks backwards one frame. stepFwd N/A Step forward - tracks forward one frame. trackFwd N/A Track forwards - plays forwards through the sequence tracking from frame to frame. smartTrack N/A Smart track - tracks from beginning to end of frame range in an intelligent order. deleteTrackKeysBwd N/A Delete track key frames backwards - deletes track key frames backwards through the sequence until either a user key frame or the beginning of the sequence is reached. deleteTrackKeyStepBwd N/A Delete track key frame and step backward - deletes a track key frame and steps backwards one frame. deleteTrackKey N/A Delete track key frame - delete the current track key frame. deleteTrackKeyStepFwd N/A Delete track key frame and step forwards - deletes a track key frame and steps forwards one frame. deleteTrackKeysFwd N/A Delete track key frames forwards - deletes track key frames forwards through the sequence until either a user key frame or the end of the sequence is reached. deleteAllTrackKeys N/A Delete all track key frames - deletes all track key frames from the sequence. deleteAll N/A Delete all track and user key frames - deletes both track key frames and user key frames. Type wireType Three Points Controls the number of points on the on-screen wire tool. Choose the number of points needed to describe the wire you wish to remove. • Two Points - choose this if your wire is straight. • Three Points - choose this if your wire is a simple curve. • Five Points - choose this if your wire has an s-shaped curve. On-Screen Wire onScreenWire Show Sets the display mode for the on-screen wire tool. • Show - shows both points and lines. • Hide - hides both points and lines. • Points only - only shows the points. Show On Screen Controls showUI disabled Shows or hides the tracker panel in the Viewer. Output output Source Sets the output mode for F_WireRemoval. • Source - output the untouched source image. Use this output mode to position the on-screen wire tool over the wire you wish to remove. • Repair - output the repaired source image, with the wire removed from under the on-screen tool. • Wire Matte - renders a matte for the wire. This may be useful if the wire has been tracked but cannot be repaired using F_WireRemoval and other techniques have to be used. • Repair Matted - output the repaired source image and a matte in the alpha channel. If you want, you can manually adjust your image further using the matte. Track Range range Source Clip Range Sets the range of frames to track the wire over. • Specified Range - use the Track Start and Track End controls to specify the range over which to track the wire. • Source Clip Range - track the wire over the entire range of the Source clip. Track Start start 0 Specifies the start of the tracking range when Track Range is set to Specified Range . Track End end 100 Specifies the end of the tracking range when Track Range is set to Specified Range . Repair repairMethod Spatial Sets the algorithm used to remove the wire from under the grain: • Spatial - this method uses a slope dependent filter that interpolates across the wire at the most likely angle, given the image behind the wire. It uses information from the current frame only. • Temporal With Static Scene - this method uses LME to align frames from before and after onto the current frame. This is useful for sequences where the wire is moving and where the motion in the rest of the scene is non-uniform. • Temporal With Moving Scene - also aligns frames from before and after onto the current frame, but uses GME. This is useful for sequences where the wire is moving and the motion in the rest of the scene is fairly uniform. • Clean Plate - choose this method if you have a clean plate you wish to use for the repair, or if F_WireRemoval does not do a good job of removing the wire from each frame. Filter Size filterSize 5 If the wire you are trying to remove has details within it (for example, a steel wire in which the twisted threads are reflecting light), then the algorithm may leave these alone, thinking that they are grain. In this situation, you can decrease the filter size. Temporal Offset tempOffset 1 Sets the time offset of the additional frames to use for the Temporal With Static Scene or Temporal With Moving Scene methods. This determines which two frames before and after the current frame are used to fill in the background behind the wire. Luminance Correct lumCorrect disabled Enable this where there are global luminance shifts between one frame of the sequence and the next, or between a frame of the sequence and a clean plate you are using for the repair. Note: The Spatial repair mode does not benefit from Luminance Correction . Lum Block Size lumBlockSize 31.12 Altering the Lum Block Size could produce a better result if Luminance Correction is not performing as expected. Points Point 1 point1 N/A The position of the start point on the wire. Point 2 point2 N/A The position of the point on the wire between the start point and the mid point. This is only active if Type is set to Five Points . Point 3 point3 N/A The position of the mid point on the wire. Point 4 point4 N/A The position of the point on the wire between the mid point and the end point. This is only active if Type is set to Five Points . Point 5 point5 N/A The position of the end point on the wire. Start Width startWidth 15.56 The width of the wire at Point 1 of the on-screen wire tool. End Width endWidth 15.56 The width of the wire at Point 5 of the on-screen wire tool. This allows you to make your repair region wider at one end than the other, for example, where there is motion blur on the wire. Overall Width overallWidth 15.56 Alter the width of the repair region along its entire length, and for all key frames. About about N/A Displays a dialog containing information about this node. Step-by-Step Guides Using F_WireRemoval Nuke 17.1v1 docs:



---

## Structured Notes

### Core Technique
Track a wire with an on-screen 2/3/5-point tool that has its own tracker panel, then repair underneath it with one of four algorithms — spatial interpolation, two motion-compensated temporal methods, or a supplied clean plate warped onto the frame.

### Summary
F_WireRemoval is the FurnaceCore node with the most workflow in it, and the docs single out where it excels: wires over **heavy motion blur, smoke, dust or cloud** — exactly the backgrounds that defeat paint. The wire is described by an on-screen tool of **Two Points** (straight), **Three Points** (simple curve, the default) or **Five Points** (s-curve), with **Start Width**, **End Width** and **Overall Width** so the repair band can widen where the wire motion-blurs. A built-in tracker — shown in the Viewer when **Show On Screen Controls** is enabled — offers step, track, **Smart track** (which tracks the range in an intelligent order rather than linearly), **Snap to wire** (finds the wire edges and snaps the region onto them), user key frames, and a full family of key-deletion commands. **Repair** picks the algorithm: `Spatial` (current frame only, a slope-dependent filter interpolating across the wire), `Temporal With Static Scene` (**LME**, for non-uniform scene motion), `Temporal With Moving Scene` (**GME**, for fairly uniform scene motion), or `Clean Plate` (warps the supplied plate onto the frame). **Output** can render `Source`, `Repair`, `Wire Matte`, or `Repair Matted` — so when the repair fails, the tracked matte is still a deliverable for another technique.

### Key Steps
1. Connect **Source** (with the wire) and optionally **CleanPlate**.
2. Set **Output** to `Source` first — that mode exists so you can position the on-screen wire tool over the untouched image.
3. Choose **Type**: `Two Points` for a straight wire, `Three Points` (default) for a simple curve, `Five Points` for an s-curve. Place `point1`–`point5`.
4. Set the repair band: **Start Width** and **End Width** (both `15.56`) to widen one end where the wire blurs, **Overall Width** to scale the whole band across all key frames.
5. Enable **Show On Screen Controls** to float the tracker panel in the Viewer, and use **Snap to wire** to fit the region to the wire's actual edges.
6. Track with **Track forwards / backwards**, **Step forward / backward**, or **Smart track** (tracks the range in an intelligent order). Set **Track Range** to `Source Clip Range` or `Specified Range` with **Track Start** / **Track End**.
7. Manage keys deliberately: **Create / Delete user key frame**, and the track-key commands — delete forwards, backwards, one key, key-and-step either way, all track keys, or all track *and* user keys. Deleting track keys stops at a user key frame.
8. Choose **Repair**: `Spatial` (default; current frame only), `Temporal With Static Scene` (LME — non-uniform scene motion), `Temporal With Moving Scene` (GME — fairly uniform scene motion), or `Clean Plate`.
9. For either temporal method set **Temporal Offset** (default `1`) — which frames before and after supply the background.
10. Reduce **Filter Size** (default `5`) when the wire has internal detail — a steel wire whose threads catch light can be mistaken for grain and left behind.
11. Enable **Luminance Correct** for global luminance shifts between frames or against a clean plate (⚠️ it does **not** benefit `Spatial`), and adjust **Lum Block Size** (`31.12`) if the correction misbehaves.
12. Set **Output** to `Repair`, or to `Wire Matte` / `Repair Matted` when the wire tracks well but needs another technique to finish.

### Nodes / Tools / Settings
- **F_WireRemoval** (NukeX / FurnaceCore). Inputs: **CleanPlate** (optional), **Source**. *See also* **RotoPaint**.
- Tracker commands: `setUserKeyFrame`, `deleteUserKeyFrame`, `snapToWire`, `trackBwd`, `stepBwd`, `stepFwd`, `trackFwd`, `smartTrack`, `deleteTrackKeysBwd`, `deleteTrackKeyStepBwd`, `deleteTrackKey`, `deleteTrackKeyStepFwd`, `deleteTrackKeysFwd`, `deleteAllTrackKeys`, `deleteAll`.
- **Type** (`wireType`, `Three Points`), **On-Screen Wire** (`onScreenWire`, `Show` | `Hide` | `Points only`), **Show On Screen Controls** (`showUI`, off).
- **Output** (`output`, `Source` | `Repair` | `Wire Matte` | `Repair Matted`).
- **Track Range** (`range`), **Track Start** (`start`, 0), **Track End** (`end`, 100).
- **Repair** (`repairMethod`, `Spatial` | `Temporal With Static Scene` (LME) | `Temporal With Moving Scene` (GME) | `Clean Plate`), **Temporal Offset** (`tempOffset`, `1`).
- **Filter Size** (`filterSize`, `5`), **Luminance Correct** (`lumCorrect`, off), **Lum Block Size** (`lumBlockSize`, `31.12`).
- Points `point1`–`point5`; **Start Width** / **End Width** / **Overall Width** (`startWidth`, `endWidth`, `overallWidth`, all `15.56`). **About** (`about`).
- Step-by-step guide: *Using F_WireRemoval*.

### Difficulty
Advanced

### Foundry App & Version
NukeX 17.1v1 (FurnaceCore).

### Tags
`furnace`, `nukex`, `clean-plate`, `roto`, `tracking`, `nuke-17`, `advanced`

---

## Related Tutorials
- [F_RigRemoval](f-rigremoval.md) — the same repair-from-other-frames idea for larger objects, without the dedicated tracker.
- [F_ReGrain](f-regrain.md) — the grain/detail distinction behind this node's **Filter Size** control.
- [F_Steadiness](f-steadiness.md) — GME, the estimator behind `Temporal With Moving Scene`.

---

> **Provenance.** Ingested from the documentation **bundled inside Nuke 17.1v1**
> on this machine (`Documentation/html/content/`), so the `url:` is a local
> `file://` path and is not reachable from another machine. It is first-party
> Foundry documentation for the exact installed build, which makes it a better
> version witness than the public docs site: what is written here is what this
> Nuke does. The page's own footer stamp (`Nuke 17.1v1 docs`) is preserved in the
> Raw Data.

> **On the Furnace suite.** These are the **FurnaceCore** nodes bundled with
> **NukeX** — the surviving subset of the original Furnace plug-in suite, which
> is why this skill's gap list called them "legacy and partly superseded". They
> are not deprecated: they ship in 17.1 and several remain the fastest route to a
> result the modern toolset reaches only through much more setup. Where a newer
> node genuinely supersedes one, the docs say so themselves in a *See also* line,
> preserved in each entry.
