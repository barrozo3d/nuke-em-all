---
title: Render World Position in Blender for Nuke
source: YouTube
url: https://www.youtube.com/watch?v=vrar9ALWG_g
author: Compositing Academy
ingested: 2026-08-14
app: "Blender (position-pass render setup) + Nuke (P-Mask usage)"
version: "not specified (2021 upload, Nuke 13.0 era — see version-tracker.md)"
tags: [compositing, channels, grading, 3d-system, digital-matte-painting, beginner]
extraction_status: complete
frames_dir: tutorials/frames/render-world-position-in-blender-for-nuke/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Render World Position in Blender for Nuke

**Source:** [YouTube](https://www.youtube.com/watch?v=vrar9ALWG_g)
**Author:** Compositing Academy
**Duration:** 5m6s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Hey everyone, welcome to this quick tutorial. This time we're going to quickly talk about
[0:13] how to create a position pass in Blender. So if you guys are a Blender user, you'll
[0:18] know that there's some weird things about Blender, but there's one thing that we can
[0:23] get out of Blender that would be really useful if we can create it. And one thing we need
[0:28] to do when we're creating a position pass is to fix the world orientation to bring it


### World Orientation [0:30]
**Transcript (timestamped):**
[0:33] into Nuke. Because the world orientation is a little bit different, the y-axis needs
[0:37] to be up and down. And that's just going to help us out in Nuke to have that consistency
[0:42] moving across the softwares. So there's a really simple way to create this, and I'll
[0:47] just go over it real briefly. So essentially you just want to select all your objects and


### Assign a New Material [0:51]
**Transcript (timestamped):**
[0:52] assign a new material. So you go to your material tab here, press the little plus icon and we'll
[0:56] create it and call it position. So you'll have a default setup here. This is not a default
[1:01] setup, but this is the already node setup that we're going to need. So I've already
[1:06] created it and it's just easier to explain having it visually laid out. So essentially
[1:11] what you want to do is start by creating a geometry node and you want to plug the position
[1:15] into separate RGB node. So if you guys are Nuke users, as probably most people on this
[1:20] channel are, or not, but basically for the Nuke users, these two nodes that work similar
[1:28] to the shuffle nodes. So essentially we can rearrange the color channels and that's how
[1:32] we're going to orient the world in the correct orientation. So what we need to do is just
[1:38] shuffle the red into the blue, the green into the red and the blue into the green. So basically
[1:43] you should just look like this and that will basically correctly set this up for Nuke.


### Emission Node [1:49]
**Transcript (timestamped):**
[1:49] After that, you want to create an emission node because we want this to not receive light
[1:53] and basically just be a data information pass. So we can create an emission node and plug
[1:58] that result into the color with a strength set to one. And the last thing you want to
[2:02] do is plug this into a mixed shader node with the with a light path node. So you want to
[2:07] say, is there a camera array? And if there is, we want this position pass to appear. And
[2:12] if there's not, we don't want that to appear. And basically plug that into the surface output
[2:18] and that will give you your shader. So it'll look something like this, maybe the colors
[2:21] will be different based on where this is located in the world. The scene I'm working on is
[2:25] quite large. So that's why we have this like green and black. But in the black values are
[2:30] actually negative. So this is actually working correctly. The last thing you want to do is
[2:35] go to your render settings and make sure you have it set to RGBA or actually RGB is fine,
[2:41] but the color depth needs to be full. So we want all of the color data saved in there.
[2:49] And the last thing we can hop into Nuke and see how that looks. So I've already rendered
[2:52] this out. And there's a couple of different nodes I play around with here. But I found
[2:56] one that's pretty good. And is by Franklin VFX.com is where I got this node from. And
[3:04] he's posted it. And it's why I like this node in particular is you just have a color picker
[3:08] and you can plug it in directly. So we have our node here. If I look at the alpha channel
[3:12] and I move this around, we can see we're getting an alpha based on the position of the objects.
[3:18] So I have it set to RGB here because by default, I didn't render that render layer, render
[3:24] pass into a render layer. So that's pretty much it. If we hop into the 3d view, what's
[3:31] great about this P mask node as well, that's this person created, as you have a 3d, basically
[3:37] the idea of what this is going to look like. So you can see it with the position points
[3:42] as well as 3d sphere representing our alpha. And if you guys haven't used these P masks
[3:49] before, essentially, we can take a look at what this does. So this is just a base render
[3:54] of some of the scene I'm working on for a tutorial, a bigger tutorial of becoming out
[3:59] in a few weeks. Supposed to take me a day, but it's taken me much longer because I kind
[4:04] of want ambitious with it. But you'll see what that is in a couple weeks here. But we'll
[4:08] plug this in and plug this into the main scene. And basically, now we can use this alpha to
[4:15] control the brightness of just a specific area. So for example, this turret here might
[4:20] be way too filled and we would want to add contrast to it. So we can say the gamma and
[4:25] we could just gamma down and it's only affecting that specific area. So if you guys have taken
[4:30] some of the other tutorials I've taught, like Nuke 3.0.3, we used a bit of this to darken
[4:35] different areas. But this is just how to get out of Blender and make it useful for basically
[4:43] people who use different softwares. So that's pretty much it for the tutorial. Hope you
[4:47] guys enjoyed and hit like if this is useful to you. If you guys are Blender users, let
[4:51] me know in the comments below as well. I know most of you, I talk about Nuke on this channel,
[4:57] but I'd like to talk a little bit more about Blender as well and how we can combine these
[5:01] two softwares together and get some really awesome results.



---

## Captured Frames

- [1:00] tutorials/frames/render-world-position-in-blender-for-nuke/frame_000.jpg
- [1:45] tutorials/frames/render-world-position-in-blender-for-nuke/frame_001.jpg
- [2:20] tutorials/frames/render-world-position-in-blender-for-nuke/frame_002.jpg
- [3:10] tutorials/frames/render-world-position-in-blender-for-nuke/frame_003.jpg
- [3:45] tutorials/frames/render-world-position-in-blender-for-nuke/frame_004.jpg
- [4:15] tutorials/frames/render-world-position-in-blender-for-nuke/frame_005.jpg

---

## Structured Notes

### Core Technique
Building a world-space position pass in Blender via a custom material (`Geometry` → `Separate RGB` → channel-swizzled `Combine RGB` → `Emission` gated by a `Light Path` "Is Camera Ray" check into `Mix Shader`), with the axes reordered to match Nuke's Y-up convention, then using that RGB position data in Nuke as a P-Mask (a Nukepedia gizmo, "P_Mask" by FranklinVFX) to drive local, position-based corrections.

### Summary
A short cross-application pipeline tutorial: Blender's world axes don't match Nuke's (Blender is Z-up, Nuke expects Y-up), so a naive position pass renders with the wrong axis mapped to each color channel. The fix is a dedicated Blender material assigned to all objects: a `Geometry` node's Position output feeds a `Separate RGB`, whose R/G/B are rewired into a `Combine RGB` with a channel swap (red→blue, green→red, blue→green) to correct the orientation for Nuke. That result feeds an `Emission` node (strength 1) so the pass carries pure position data unaffected by scene lighting, and a `Light Path` node's "Is Camera Ray" output drives a `Mix Shader` so the position data only appears in camera rays (not reflections/shadows/etc.), feeding the material's Surface output. Render settings must use full float color depth (RGB is sufficient; RGBA not required) so negative position values survive — the video notes that black-looking areas in the position pass are actually valid negative values, not a broken render. In Nuke, the rendered position-pass footage is plugged into a "P_Mask" gizmo (from FranklinVFX.com), which offers a color-picker-style pick-a-point-in-3D-space workflow to derive a local alpha/mask from world position — visualized in Nuke's 3D viewer as a sphere at the picked point. That alpha can then drive local corrections (e.g. `Gamma` down on just one turret of a large model) without needing a roto shape or an AOV/Cryptomatte ID mask — referenced as a lighter version of a technique used in an earlier "Nuke 3.0.3" tutorial (title as stated in the video, likely referring to an earlier position-pass darkening tutorial in this creator's catalog).

### Key Steps
1. In Blender, select all objects that should contribute to the position pass.
2. Create and assign a new material (named e.g. "position") to those objects.
3. Add a `Geometry` node and connect its Position output into a `Separate RGB` node.
4. Rewire the split channels into a `Combine RGB` node with a channel swap: red input → blue output, green input → red output, blue input → green output — this re-orients Blender's Z-up world position data to match Nuke's Y-up convention.
5. Feed the recombined RGB into an `Emission` node's Color input, strength set to 1, so the position data isn't affected by scene lighting/shading.
6. Add a `Light Path` node and use its "Is Camera Ray" output to control a `Mix Shader` between the emission shader and nothing — ensures the position pass only renders on primary camera rays.
7. Plug the `Mix Shader` result into the material's Surface output.
8. In Blender's render settings, set color depth to Full (RGB channels are sufficient; negative values in the "black" areas are expected/correct for a large scene — not a broken render).
9. Render out the position pass (as its own render layer/pass if you want it isolated from beauty, or with RGB used directly).
10. In Nuke, read the rendered position-pass footage and plug it into a "P_Mask" gizmo (Nukepedia, credited to FranklinVFX.com) — it exposes a color-picker-style control to sample a 3D world position directly from the position-pass image and generate a corresponding alpha/mask.
11. Preview the pick in Nuke's 3D viewer, which shows the sampled point as a 3D sphere alongside the position-pass point cloud, for visual confirmation of what area the mask covers.
12. Use the resulting alpha to drive a local, non-rotoscoped correction — e.g. plug it as a mask into a `Grade`/`Gamma` node to darken or add contrast to just one region of a large model (demonstrated darkening a turret on a ship-like CG asset).

### Nodes / Tools / Settings
- Blender: `Geometry` node (Position output)
- Blender: `Separate RGB` / `Combine RGB` — used purely as a channel-swizzle (Nuke-style shuffle) to remap Z-up axes into Nuke's Y-up convention: R→B, G→R, B→G
- Blender: `Emission` shader — Color = the swizzled position data, Strength = 1
- Blender: `Light Path` node — "Is Camera Ray" output
- Blender: `Mix Shader` — gated by Is Camera Ray, feeds material Surface output
- Blender: Render settings — Color Depth = Full (float), RGB channels sufficient (RGBA not required)
- Nuke: `P_Mask` (Nukepedia gizmo by FranklinVFX.com) — color-picker-driven world-position-to-alpha sampling tool, with a 3D-viewer preview of the picked point
- Nuke: `Grade`/`Gamma` — masked by the P_Mask alpha to apply a local, position-driven correction without rotoscoping

### Difficulty
Beginner

### Foundry App & Version
Cross-application: Blender (for the position-pass material/render setup — no Blender version stated) feeding Nuke (for the P_Mask gizmo usage — third-party Nukepedia tool, no native-Nuke-only features required). No on-screen version numbers visible in the captured frames and none stated in the transcript. Video published 2021 — falls in the Nuke 13.0 era (13.0 released 2021-03-17); see `references/version-tracker.md`.

### Tags
compositing, channels, grading, 3d-system, digital-matte-painting, beginner

---

## Related Tutorials
- [Create 3D Noise | Nuke Compositing](create-3d-noise-nuke-compositing.md) — shares the position-pass-as-data-carrier theme; that video drives a `noise()` expression from position-pass channels rather than a pick-a-point mask, but both treat a position render as raw XYZ data to be manipulated in Nuke.
- [Nuke Compositing Technique | Card3D + PixelsToPos [Beginners]](nuke-compositing-technique-card3d-pixelstopos-beginners.md) — shares the theme of deriving a usable mask/anchor from 3D spatial data without rotoscoping, though that video samples 3D points from a tracked camera rather than a rendered position pass.
- [Planning out a Visual Effects Shot | Blender and Nuke](planning-out-a-visual-effects-shot-blender-and-nuke.md) — shares the Blender-to-Nuke cross-application pipeline theme (`compositing`, `digital-matte-painting`).
