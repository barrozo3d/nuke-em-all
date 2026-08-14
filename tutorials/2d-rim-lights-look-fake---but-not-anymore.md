---
title: 2D Rim Lights Look FAKE - But Not Anymore
source: YouTube
url: https://www.youtube.com/watch?v=WcB524Y32Io
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/2d-rim-lights-look-fake---but-not-anymore/
frame_count: 0
frame_status: pending-selection
---

# 2D Rim Lights Look FAKE - But Not Anymore

**Source:** [YouTube](https://www.youtube.com/watch?v=WcB524Y32Io)
**Author:** Compositing Academy
**Duration:** 3m54s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py 2d-rim-lights-look-fake---but-not-anymore <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to this tutorial. We're going to be talking about a new way to create
[0:04] a rim light on 2D images, just requiring an alpha, doesn't actually require normals or
[0:10] position or anything like that. So there's a few different ways to do this as a compositor
[0:15] that you may have done in the past if you're ever integrating foreground footage with background
[0:19] footage or you're doing some kind of graphics like a title sequence of a movie. So this is
[0:25] what we have. You might think that the first way intuitively might be something like an
[0:29] emboss node, you want to just create a rim light on the edge of something, you know,
[0:33] we could take an emboss, we could shift it around a little bit because it has an angle
[0:37] control. The problem with this is that we don't actually have softness, you always get
[0:41] to sort of very graphic look, it doesn't look like a light, unless it's a very pinpoint
[0:46] perfect light. So it's kind of limiting in terms of the things we can actually do with
[0:50] this. And that was kind of one typical way to do it is to use an emboss. So that's pretty
[0:56] simple. But there's another way here that another manual way is to take a transform
[1:00] node and to take your original image. And we just shift it down by a pixel or two, and
[1:05] we stencil it out from itself so we can create the little edge, which is cool. But if you
[1:10] want to extend that light, what you could do is take a God Ray and extend it out, and
[1:14] then plus that back on. So we just have a stencil God Ray, and you can blur it if you
[1:19] want and kind of plus that back on us to save all the blur for a second just to take a look
[1:23] at it. And that kind of looks like a rim light and we can fake that effect. We can rotate
[1:27] that God Ray around a tiny bit. So if you just move the X and Y position, we're faking
[1:32] basically just a very simple 2D rim light. So 2D composing tricks, nothing extremely
[1:37] fancy here, but it is useful to know if you aren't already aware of that technique.
[1:43] So where this can be more interesting is how would we make this look like a soft light?
[1:49] How do we cast soft shadows onto this because most lights are not perfectly harsh. And it
[1:54] just looks a little bit better to have some kind of attenuation on the shadow. And the
[1:58] way I was thinking about this is like, you know, normally you just take a blur, but that
[2:02] doesn't actually look like a shadow attenuation. It kind of just looks like it's blurred everywhere.
[2:07] So I put together a custom node that actually solves this problem. And so remember, this
[2:11] is not, we're not talking about light wrap here, we're not talking about essentially
[2:15] what this would be where we have a light source behind the object, something like a very like
[2:19] a glowing orb, we mask it, and we plus that back over, that would be more like a light
[2:24] wrap, we're not talking about that, we're talking about casting light onto the edge
[2:27] of the object. So what this tool does is essentially this, I'll turn off the smoothing for a sec.
[2:34] Here's our original image. Here's a grade putting it back on. So this looks pretty similar
[2:38] to the God Ray effect that we just had. But we have a smoothing control. So if I increase
[2:42] the smoothing, if we pay attention to this edge, remember, this is what the God Ray look
[2:46] looks like. And this is how it would probably be done currently. So we can increase the
[2:51] softness. Now, if you watch where the softness is occurring, it's occurring on the further
[2:56] parts of the shadows, not just the entire thing, we're not just blurring the picture.
[3:00] So let's go back to the blurred image and just compare what that looks like this really look
[3:04] a blurred image. Whereas this attenuates off of the picture. So if I increase or decrease,
[3:11] we have some pretty cool controls here. We have a fall off control as well. So we can
[3:15] actually spread that. And that's pretty much it. So it's just a nice tool for creating
[3:20] these effects. I've added some rotation controls. And you don't have to mess around with God
[3:24] Ray or anything like that. You basically just get this nice simulated light effect from
[3:29] behind that it makes it feel like an actual light versus just like blurring things. And
[3:34] I thought that was pretty useful, especially for like kind of graphic stuff, which I'm
[3:37] doing some projects right now that involve a little bit of this. And I thought that this
[3:42] was a nice effect. So there's a free download, I compiled this in a specific version of Nuke.
[3:46] So I haven't tested every single version or anything like that. There's one that you
[3:49] guys want, you can just shoot a message in the comments or something. But that's pretty
[3:53] much it.



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
