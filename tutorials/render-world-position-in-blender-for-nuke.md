---
title: Render World Position in Blender for Nuke
source: YouTube
url: https://www.youtube.com/watch?v=vrar9ALWG_g
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/render-world-position-in-blender-for-nuke/
frame_count: 0
frame_status: pending-selection
---

# Render World Position in Blender for Nuke

**Source:** [YouTube](https://www.youtube.com/watch?v=vrar9ALWG_g)
**Author:** Compositing Academy
**Duration:** 5m6s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py render-world-position-in-blender-for-nuke <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


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
