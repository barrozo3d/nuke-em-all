---
title: Preserve Quality | Projections in Nuke
source: YouTube
url: https://www.youtube.com/watch?v=8Aki1VR_tX8
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke / NukeX (3D system for projections)"
version: "not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)"
tags: [3d-system, rotopaint, roto, compositing, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/preserve-quality-projections-in-nuke/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Preserve Quality | Projections in Nuke

**Source:** [YouTube](https://www.youtube.com/watch?v=8Aki1VR_tX8)
**Author:** Compositing Academy
**Duration:** 5m33s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey everyone, this is just a quick tutorial on how to preserve quality through projections
[0:06] and also just a quick tip on how to get alphas from rotopaint brushstrokes.
[0:13] This class assumes you already know, it's just a quick tutorial, it already seems that
[0:17] you know how to do a basic clean plate in Nuke and you understand a little bit of the 3D system.
[0:22] If you guys are looking for more of that information, I have a full class about that called Nuke
[0:26] 202 3D compositing masterclass, that's available in the description below.
[0:32] So just to get to the information quickly here, what we're doing is just getting rid
[0:36] of some of the leaves on this stair.
[0:39] So I've already created the projection setup and this is like the final result.
[0:44] So very simple clean plate, tracked it in and just kind of replacing the bad areas.
[0:49] But this is just teaching you guys that there's something you shouldn't be doing with projections.
[0:56] What that is is projecting the entire section of the image that you're working with.
[1:03] So for example, if we're only replacing these leaves, we don't want to re-project the entire
[1:10] video onto the staircase geometry that we created.
[1:13] So there's a cube here, we don't want to re-project and use this whole area.
[1:18] And so the reason for that is if we compare, if we look at the original footage and then
[1:22] we look past the lens distort and the re-distort, so we have our normal undistorting our footage,
[1:29] projecting it, putting it through the scan line render and re-distorting our footage.
[1:35] If we just compare the two and we really zoom in, you'll actually see that there's a slight
[1:41] bit of filtering happening here.
[1:44] You might not be able to tell well on the YouTube stream, but you can see there's a
[1:49] bit of softening happening here through the transforms.
[1:54] So we don't want to re-project the whole area because we're damaging our image.
[1:59] So what we want to do instead is just take a roto paint.
[2:03] I'm going to paint out the areas that are not good, so I'm going to take these and just
[2:10] paint out quickly the leaves just to give us ourself a clean plate.
[2:22] So I'm just going around sampling different areas.
[2:25] And okay, so that should work for the clean plate, just very simple.
[2:32] But the key here is there's a little black arrow in the roto paint node that a lot of
[2:35] people don't know when you're kind of starting out.
[2:37] So if you click that black arrow and you say output mask, set to RGBA alpha.
[2:42] So before I click it, let me just put the viewer and hit A. You see that we have no
[2:47] alpha in this picture, this clean plate that we're creating.
[2:52] But if we output an alpha mask, you'll see now that everywhere that we put a brush stroke,
[2:57] we get an alpha.
[2:59] So now if I pre-multiply that result and put a pre-mult, now we just have the spots that
[3:07] we're replacing.
[3:09] So when we re-project that onto that little card now, we see that we're just getting those
[3:15] areas.
[3:18] And that's going to preserve a lot of your image quality, especially if you're doing
[3:21] a lot of projections over an entire scene.
[3:24] So if I hit play now, you see we're actually preserving the areas around, those are still
[3:29] the original video that we're keeping.
[3:33] And the other thing we can do to preserve quality through projections.
[3:37] So just every time you have a transform or a scan line render, you guys are sampling
[3:43] your picture, meaning you're losing a little bit of quality because you're kind of moving
[3:49] the pixels around a little bit and you're losing a little bit of quality.
[3:54] So if we just, again, we just compare, I'm going to turn off, yeah, let's just compare
[3:58] here.
[4:01] You see we still have a little bit of blurriness kind of happening, especially if you look
[4:05] on the white, it almost looks like it's being blurred by a pixel.
[4:08] If you want to preserve 100% of your image quality, it's not exactly possible, but what
[4:13] we can do is we can switch our filtering to a different type.
[4:17] So if you click in the lens distortion node, you'll see there's a filter set to cubic.
[4:21] Instead, I'm going to send it to this, a length so is four, I don't know exactly how
[4:26] it's pronounced, but this one.
[4:28] And what that does is it just preserves a little bit more of the sharpness in your
[4:32] picture.
[4:33] Also, if you click in the scan line render, we need to do the same thing.
[4:36] So change it from cubic to this one.
[4:40] Same with the re-distort.
[4:41] So we're setting them all to the same filter.
[4:44] And now this way, again, it's still not 100%, but there's a little bit maybe less filtering
[4:50] happening.
[4:51] It's a little bit of a sharper image by using that filter method.
[4:57] And so that's how you can preserve a little bit of your quality through a projection and
[5:02] also how you can easily create alphas based on your brush strokes.
[5:05] So you can just project areas you need.
[5:07] If you like this video, just please hit the like button and subscribe and hit the little
[5:13] bell if you want to be notified every time I have a new video coming out.
[5:16] I'm going to be trying to do short form ones like this, like a quick little video and also
[5:21] kind of mini projects like the last video I posted kind of 20 to 30 minute range.
[5:26] So it's going to be a variation of that kind of content.
[5:28] So subscribe if you want.
[5:30] And thanks for watching.



---

## Captured Frames

- [0:39] tutorials/frames/preserve-quality-projections-in-nuke/frame_000.jpg
- [2:42] tutorials/frames/preserve-quality-projections-in-nuke/frame_001.jpg
- [2:59] tutorials/frames/preserve-quality-projections-in-nuke/frame_002.jpg
- [3:09] tutorials/frames/preserve-quality-projections-in-nuke/frame_003.jpg
- [4:17] tutorials/frames/preserve-quality-projections-in-nuke/frame_004.jpg
- [4:40] tutorials/frames/preserve-quality-projections-in-nuke/frame_005.jpg

---

## Structured Notes

### Core Technique
Two small but high-value habits for cleaner clean-plate projections in Nuke's 3D system: (1) limit a re-projected patch to only the pixels actually needing replacement (via a RotoPaint alpha mask + premult) instead of re-projecting the whole frame, and (2) switch filtering away from the default Cubic to reduce resampling softness through the undistort → project → re-distort chain.

### Summary
Working example: removing unwanted leaves off a staircase using a tracked clean-plate projection setup (undistort → project onto rough 3D geometry via ScanlineRender → re-distort). The presenter points out a common beginner mistake — projecting the *entire* frame onto the geometry re-samples/filters the whole image (undistort, `ScanlineRender`, re-distort each resample pixels), causing a visible softening even where nothing needed fixing. The fix: paint the clean-plate replacement only over the bad areas with `RotoPaint`, then reveal that RotoPaint node's often-missed "output mask" dropdown/arrow — setting it to `rgba.alpha` makes every brushstroke also write an alpha, so a `Premult` after it isolates just the painted patch areas. Projecting that isolated, pre-multiplied patch instead of the full frame preserves image quality everywhere else in the shot. Second tip: every transform/resample stage (`LensDistort`, `ScanlineRender`, re-distort) defaults to Cubic filtering, which introduces its own softening; switching all three to a sharper filter option (referred to on-screen, unclear exact pronunciation — appears to be a Lanczos-family or "Sinc"-type filter) preserves more sharpness through the chain, though the presenter notes 100% lossless quality isn't achievable through any resample.

### Key Steps
1. Build a standard 3D clean-plate projection setup: undistort the plate (`LensDistort`), project it via `Project3D`/`ScanlineRender` onto rough tracked geometry (e.g. a simple card/cube standing in for the staircase), then re-distort the render back to match the original lens.
2. Recognize the problem: projecting the *entire* frame through this chain re-samples every pixel (not just the area being fixed), softening the whole image slightly — visible when A/B-comparing original vs. round-tripped footage zoomed in.
3. Instead of projecting the whole frame, use `RotoPaint` to hand-paint just the clean-plate replacement over the bad area (e.g. sampling clean staircase texture to paint out leaves).
4. In the RotoPaint node, find the small black arrow/dropdown for output mask and set it to `RGBA.alpha` — by default a RotoPaint used purely for painting produces no alpha; enabling this makes every brushstroke area register in the alpha channel.
5. Add a `Premult` node after the RotoPaint so only the painted patch pixels survive with real values elsewhere zeroed — this isolates the replacement to exactly the touched pixels.
6. Feed this isolated, pre-multiplied patch (instead of the full frame) into the projection setup — the re-projected result now only affects the painted area, leaving the rest of the frame untouched at full original quality.
7. Additionally, to reduce resample softening in the areas that do need to go through the projection chain: open `LensDistort`, `ScanlineRender`, and the re-distort node and change the Filter parameter from the default Cubic to a sharper alternative filter (all three nodes should match) — improves sharpness retention through the round-trip, though some softening is unavoidable with any resample.

### Nodes / Tools / Settings
- `LensDistort` — undistort/re-distort the plate; Filter parameter changed from default Cubic to a sharper filter option.
- `ScanlineRender` (or `Project3D`) — projects the clean-plate patch onto rough tracked 3D geometry; same Filter parameter change applies.
- `RotoPaint` — used to hand-paint the clean-plate replacement; **output mask dropdown (small black arrow) set to `RGBA.alpha`** is the key, easy-to-miss setting that makes brushstrokes generate an alpha channel.
- `Premult` — applied after the RotoPaint's alpha is enabled, isolating only the painted patch for projection.
- Filter setting — changed uniformly across LensDistort/ScanlineRender/re-distort from Cubic to a sharper option (name unclear from audio, likely a Lanczos/Sinc-family filter) to reduce cumulative resample blur.

### Difficulty
Intermediate — assumes prior familiarity with Nuke's 3D system and clean-plate projection workflows (explicitly stated as a prerequisite, pointing to the presenter's own "Nuke 202: 3D Compositing Masterclass").

### Foundry App & Version
Nuke / NukeX (3D system/projection setup implies NukeX). Version not stated on screen or in narration. 2020 upload, predates this skill's release-notes backfill (starts at Nuke 13.0/March 2021), so treat as Nuke ~12.x era rather than a specific point release.

### Tags
3d-system, rotopaint, roto, compositing, intermediate

---

## Related Tutorials
[No existing tutorials in the knowledge base share 2+ tags yet — will be cross-linked as more 3D-system/projection-focused entries are ingested.]
