---
title: Nuke Compositing Artistic Basics (6/8): Whitepoint and white balance
source: YouTube
url: https://www.youtube.com/watch?v=VlA6a0IK-Ds
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/nuke-compositing-artistic-basics-68-whitepoint-and-white-balance/
frame_count: 0
frame_status: pending-selection
---

# Nuke Compositing Artistic Basics (6/8): Whitepoint and white balance

**Source:** [YouTube](https://www.youtube.com/watch?v=VlA6a0IK-Ds)
**Author:** Compositing Academy
**Duration:** 5m49s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py nuke-compositing-artistic-basics-68-whitepoint-and-white-balance <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Now we're going to talk about white points, the other very important concept when you're


### White Points [0:02]
**Transcript (timestamped):**
[0:05] composing CG, and what affects white points.
[0:09] So the two or three main things that affect the white point of a camera is the light color.


### Light Color [0:14]
**Transcript (timestamped):**
[0:16] So for example, if we have a white piece of paper and we have an orange light filling
[0:21] the entire room, the white point, we know that the piece of paper is actually white.
[0:27] We know the physical properties of that paper are white, but the light hitting the paper
[0:31] is making it orange.
[0:34] So that would be the white point.
[0:35] We could set the white point to the piece of paper and it would remove the orange from
[0:39] the scene.
[0:42] The other factor that controls it, so it's the light color and also the white balance


### White Balance [0:45]
**Transcript (timestamped):**
[0:47] on your camera.
[0:48] So what is a white balance if you're not familiar with photography?
[0:53] Definitely pick up a photography book once again.
[0:54] I'll keep saying it.
[0:55] If you check this out, this is the same camera.
[0:58] I was just using an iPhone here.
[1:00] It's the same camera taking the picture of this wall with the same lighting.
[1:03] I didn't change the lights.
[1:04] I didn't do anything.
[1:06] But sometimes the white balance on the camera changes.
[1:11] So if you don't manually set the white balance, which is basically just telling the camera,
[1:15] hey, what is white here?
[1:18] So if you have a more expensive camera or you have an app, you can actually set your
[1:22] white balance manually.
[1:27] But sometimes if you see your camera, maybe there's a little bit of a blue tint or an
[1:30] orange tint to your pictures.
[1:33] And that's because of the white balance.
[1:34] It's what the camera thinks is white.
[1:39] So a good way to actually set your white balance on your camera would be to hold up a white


### Set Your White Balance [1:40]
**Transcript (timestamped):**
[1:44] piece of paper, point your camera at it, and some cameras have a custom setting that will
[1:49] say, okay, look at that piece of paper and set the white balance.
[1:53] And it will make that piece of paper white in the camera's vision.
[1:59] But a lot of times that's not done.
[2:01] So we have a white balance that's not exactly white.
[2:05] So that's the two things, the color of the light and the white balance of the camera.
[2:11] So for example, we have our picture here.
[2:15] This is not our plate that we're going to be using for a final one.
[2:18] We see that it's kind of blue hour, but we also have a white balance that's set on this
[2:24] camera.
[2:25] So this probably isn't the true color of the world that we're filming in, to be honest.
[2:30] But that's fine.
[2:31] We can say that these clouds are pure white though because it might be blue hour and everything
[2:41] turns a little bit blue outside.
[2:43] But just to show you, if it was just a white balance issue and we knew that these clouds
[2:48] in real life were actually white and our light source wasn't blue, we could just say, okay,
[2:53] let's set the white point and sample it to that cloud.
[2:57] And now those clouds become pure white.
[3:03] And these things are becoming much more white.
[3:05] So we're actually removing the blue tint from this picture, which may or may not be the
[3:13] correct thing, depending on what the actual light color was in real life.
[3:18] So again, we got to consider both factors.
[3:22] This actually looks kind of cool to remove that blue tint because it actually adds some
[3:26] interesting colors and stuff here.
[3:29] But that's all good to know.
[3:32] But a lot of times we're not changing the white point on our footage.
[3:37] We're actually just trying to match it.
[3:39] So if we have a white ball here that's not matching, we can take that.
[3:49] And what we would do is we would sample something that seems to be white in that scene.
[3:55] So I would take this and maybe sample the cloud.
[3:58] So if you look at the color samples here, you could tell that this is pure white and
[4:02] this is not pure white.
[4:04] So that's what we would change the white of this into being that to make it match.
[4:09] So that would be like this.
[4:11] So we see the difference.
[4:12] And that would be more of a matching white point.
[4:15] However, this would be a little bit different if, again, where this ball is over here and
[4:20] there's an orange street light that is affecting the whites in the scene.
[4:25] So actually it could be a combination of maybe what you would do is first you would match
[4:31] the ball to this, the quote unquote color balance of the scene.
[4:37] So you would match the white of this first.
[4:39] And then we would add orange tint into it because we know like if the orange, let's
[4:44] say the orange was on this side, the orange might make the white point a little bit orange
[4:49] on the left, but the quote unquote pure white would still have this little bit of tint in
[4:55] it.
[4:56] So for example, let's just try to show it.
[5:04] Yeah.
[5:09] So you know, if we had an orange light on that side, so we know that this surface is
[5:19] white, but it's taking some orange light on.
[5:26] But you know, we don't have that.
[5:27] We're not doing this.
[5:28] We still have to match the white point of the color balance, the environment color, and
[5:34] then the white point from if there was a light over here.
[5:38] So those are the things to think about.
[5:41] Yeah, that's pretty much it for white point.



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
