---
title: Break up your "PERFECT CG" Renders with this FREE Plugin
source: YouTube
url: https://www.youtube.com/watch?v=Nk6iluY4shE
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/break-up-your-perfect-cg-renders-with-this-free-plugin/
frame_count: 0
frame_status: pending-selection
---

# Break up your "PERFECT CG" Renders with this FREE Plugin

**Source:** [YouTube](https://www.youtube.com/watch?v=Nk6iluY4shE)
**Author:** Compositing Academy
**Duration:** 4m7s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py break-up-your-perfect-cg-renders-with-this-free-plugin <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to this tutorial. We're going to be talking about how to scatter details and break up your perfect looking CG with position data.
[0:07] So I'm releasing a free plugin. It's called Pscatter, and it helps you do this process. I've never seen a plugin that actually scatters images along position data in a random way.
[0:17] So I wanted to put one together and it's been really useful for me. So hopefully you guys will find it useful as well.
[0:22] And just for quick context, if you don't know, this position data can come out of Blender, Houdini, Maya, it doesn't really matter. 3D position data is a universal render pass that you can use.
[0:34] So here's my render. We have this lander that's coming towards the camera. It's kind of a zoom in shot. So I'm not showing the final scene here.
[0:41] If you want to see the final scene, by the way, in a few weeks, we're going to be showing this full VFX sequence I've been directing. So make sure you subscribe.
[0:48] But this is what we have. So we have like a before and just an after some little scratch details and things like that.
[0:55] And how we're doing this is this position data and the Pscatter plugin. So this plugin essentially, I'll show it with color reels first.
[1:04] So I have my position data, which is rendered out of Blender. This is position reference data, which means it sticks to the object. It's not world position.
[1:12] And using this data, we can stick images onto our CG. So here I am just plugging the position data into a simple picture of a color wheel.
[1:20] And when I put this on here, you'll see we actually scatter that image a whole bunch of times all over the 3D model.
[1:26] If I hit play, you'll see that these images actually stick, which this is really useful because we can break up surfaces. We could add dirt, snow, whatever it is you want to add.
[1:36] Now we have control instead of just using something like a noise pattern, which is useful to scatter sometimes onto a model.
[1:43] Having images is actually much more powerful. So if I take this, you're going to need to adjust these depending on the size of your position data.
[1:51] If you're doing a really large scale world, it might come in looking weird. So you need to play around with the size here.
[1:56] So basically, I've added a density control and it's scattering points randomly across the position data.
[2:02] And we also have scatter scale so we can we can increase the scale and we're going to get those color wheels kind of spawning bigger.
[2:09] So that is how it works. Now it's not that interesting with color wheels. Obviously, we want to do something useful.
[2:14] So here I've just taken a scratch texture from textures.com and basically cropped it in.
[2:21] So I did a little crop here with a softness control just to feather off the edges and essentially just do a little bit of a piece scatter.
[2:28] And this piece scatter can give us some nice scratches on our surface and we can use this to kind of grade our CG.
[2:33] So if we have our original CG here, we could take a grade node, we could plug that into the mask and maybe we just do a little bit of a multiply up.
[2:41] Now, maybe it's a little bit too uniform and we could break that up with other things like PMATS or other various methods.
[2:47] But this is essentially the idea. We want to break up CG. We don't want perfect soft looking CG or CG that just looks not dirty.
[2:55] And that's just a good way to add a little bit of realism. So the plugin is going to be there.
[2:59] And there's some interesting things that you can do with this as well that I think would be a hard thing to do otherwise.
[3:06] So things like this, I was kind of playing with this concept of playing with some various animation patterns and then basically scattering that onto the CG.
[3:14] Now you need to mask this out. So sometimes you get this color in the background. You just mask it by your rendered alpha.
[3:21] But something like this could be the starting point for a look development of something like maybe a camouflage tank, like a sci-fi tank or something like that,
[3:30] where maybe you want to do army stealth camouflage effect or some kind of force field that gets hit and impacted and maybe some kind of reaction across the surface of your CG.
[3:42] This is how we would start to do it. Now, this is not obviously a final effect, but it gives you an idea of scattering videos onto your 3D models,
[3:50] which is really, really cool. So there's a lot of creative use and I'm sure I'll show some other demos in the future of how you can actually use this.
[3:57] That's just where my brain was kind of messing around a little bit. So hopefully you guys find that useful. The download link is in the description below.
[4:03] Make sure to hit the thumbs up and I'll keep making more videos like this. Thanks.



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
