---
title: This FREE Tool Warps Images in a Way You’ve Never Seen
source: YouTube
url: https://www.youtube.com/watch?v=y3tFCa0U9Yo
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/this-free-tool-warps-images-in-a-way-youve-never-seen/
frame_count: 0
frame_status: pending-selection
---

# This FREE Tool Warps Images in a Way You’ve Never Seen

**Source:** [YouTube](https://www.youtube.com/watch?v=y3tFCa0U9Yo)
**Author:** Compositing Academy
**Duration:** 4m58s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py this-free-tool-warps-images-in-a-way-youve-never-seen <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Have you ever dreamed of a visual effects tool, one so real you could almost feel it?
[0:07] As it turns out, the tool is real.
[0:20] Until now we've been stuck with just a few different ways to warp images, but what if
[0:24] you want images to flow along a path?
[0:27] That's what this tool does.
[0:28] The other tools are not really meant for bending things in a significant way, especially
[0:32] when there are many different directional changes.
[0:35] In the past I've solved this problem using a VR headset and creating these 3D strips of
[0:40] geometry which you can import into Nuke and put a texture on it.
[0:44] But I want to create a tool that's just inside Nuke.
[0:46] So here's the concept.
[0:47] We draw a roto spline and then we determine a distance away from the center of the spline.
[0:53] With this we can create a tunnel around that roto shape.
[0:57] This allows us to have the UV coordinates to flow images down the path of that tunnel
[1:02] that we've just created.
[1:04] So the input is just a sliding image.
[1:05] The two ways we use this is stretching the image or flowing an image down the path.
[1:09] So we'll talk about stretch first.
[1:11] So let's see how this works.
[1:12] I have an image here that I created earlier that flows from left to right.
[1:17] So you always want your image to start on the left because that's the start of the path
[1:20] and the end of the path is on the right side.
[1:22] So now what we need to do is draw a roto spline that this will stick to.
[1:25] So if I click my roto spline and I go here and choose open spline, we can draw any path
[1:29] we want and simply hit enter.
[1:32] And now we go to flow warp and we say sample roto.
[1:35] And you can see our image automatically warps to the path.
[1:38] So if I close this, hit play and let's just check it out.
[1:40] We can see that this is working pretty well right off the bat.
[1:43] Now we have a bunch of controls here that we can do to modify the look of this.
[1:47] Let's say we want to make this a little bit wider, for example.
[1:49] We can click here and we can go to distance and something like, you know, go from 30 to
[1:53] 80 and we can make this a wider looking effect.
[1:56] We also have a number of samples.
[1:57] So if there's not enough samples, let's say we have two low samples, you get a little
[2:01] bit blurring in here.
[2:02] So you just want to increase this to a higher number.
[2:04] And the other thing you can do is if you still see a little bit of stretching or blurring
[2:08] here, we can just add a tiny bit of blur to the UV blur and that will actually smooth
[2:13] out the effect across the path.
[2:15] Now this will cause a little bit of artifacting around the edges.
[2:18] But I've added a control here called erode edge.
[2:20] So you can just erode in the edge a tiny bit and that will fix that up.
[2:24] And now we have a nice looking effect flowing smoothly across our path.
[2:28] The other thing you can do here is crop off the edges if you need to.
[2:31] So you can put a crop node and add a little bit of smoothness so that we just fade off
[2:34] the edges easily.
[2:36] And then that's going to have a nice tapering effect on the edges.
[2:39] Additionally, you have some controls for the taper.
[2:41] So if you want to increase or decrease the width of the start and end points, we have
[2:45] control for that.
[2:46] So if I decrease these to zero, you see we have like this nice tapered pointing effect.
[2:50] That's what you're looking for.
[2:52] And so you can go pretty extreme with these warps.
[2:54] Like here I'm warping around the Nuke logo, which has a lot of curvature.
[2:57] And to do this otherwise would be pretty difficult.
[3:00] And this is another quick example of taking this stock element from the Compositing Academy
[3:04] Look Dev Pack.
[3:05] There's 200 of these energy effects that you can get.
[3:08] And we're essentially flowing this onto a path.
[3:10] So something that's very straight.
[3:12] We can flow this around edges and we can create new designs by warping a bunch of these together.
[3:17] A big part of Composers' jobs is to redirect stock elements and be creative with these
[3:21] elements.
[3:22] So here's another example where we have some particles shooting from left to right.
[3:25] So I've oriented them.
[3:27] Now if we put this through Flow Warp, we could take this and we can make those particles
[3:30] flow around something.
[3:32] So if something, maybe that character lands on the ground and shoots up some sparks or
[3:35] some large impact around two characters fighting or happening.
[3:39] This is where we need to be creative and actually think of the use cases here.
[3:43] Now here's the flow technique.
[3:45] Here's another creative example.
[3:46] I just took a roto shape and pulled out one of the edges to create this comet like roto
[3:51] shape and then I grade it and I put a quadratic Luma key on it, which is again video on my
[3:57] channel.
[3:58] Check it out.
[3:59] So we get this nice little light fall off.
[4:01] And now if I squeeze this and I do an offset, which essentially just makes it go off of
[4:05] the right side of the image and come back onto the left side of the image, we have this
[4:09] sort of little comet shape that's flowing along here.
[4:11] And if we put that through the Flow Warp, we can actually get something that looks like
[4:16] an image shooting around our, you know, basically our picture.
[4:19] So we could create all kinds of particle effects using this.
[4:22] So that's the technique using the flow instead of stretching an image the whole width.
[4:27] We just slide images across the dimension.
[4:31] Now if you're an advanced user and you want to experiment more with this, if you go inside
[4:34] the node itself, you can actually link these points instead of using the roto shape, you
[4:39] can link them to something manually.
[4:41] So we could create different types of effects like this.
[4:43] So the free download is in the description below.
[4:46] And if you like this video, make sure to hit thumbs up so I can keep making more videos
[4:49] like this.



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
