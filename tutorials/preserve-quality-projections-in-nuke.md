---
title: Preserve Quality | Projections in Nuke
source: YouTube
url: https://www.youtube.com/watch?v=8Aki1VR_tX8
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/preserve-quality-projections-in-nuke/
frame_count: 0
frame_status: pending-selection
---

# Preserve Quality | Projections in Nuke

**Source:** [YouTube](https://www.youtube.com/watch?v=8Aki1VR_tX8)
**Author:** Compositing Academy
**Duration:** 5m33s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py preserve-quality-projections-in-nuke <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


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
