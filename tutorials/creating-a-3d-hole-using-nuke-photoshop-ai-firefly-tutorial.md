---
title: Creating a 3D Hole using Nuke + Photoshop A.I (Firefly) Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=8QEGlRX-kH4
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/creating-a-3d-hole-using-nuke-photoshop-ai-firefly-tutorial/
frame_count: 0
frame_status: pending-selection
---

# Creating a 3D Hole using Nuke + Photoshop A.I (Firefly) Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=8QEGlRX-kH4)
**Author:** Compositing Academy
**Duration:** 10m13s | 9 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py creating-a-3d-hole-using-nuke-photoshop-ai-firefly-tutorial <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to part two of this series here. And this time we're going to use Nuke
[0:10] camera projections to project AI generated images to create a 3D DMP effect with this
[0:15] hole in the ground. Now, these are pretty standard camera workflows or camera projection
[0:20] workflows rather in Nuke. So even if you're kind of new to camera projections or DMP,
[0:24] this will be useful for you. I just think that the added element of generative AI on
[0:29] top of this and generating potentially from different angles to fix the stretching that
[0:34] happens with camera projections is an interesting evolution of this workflow. And so that's
[0:38] kind of what this was the purpose of this doing this project for me was to just see
[0:43] if this is a viable workflow. And I do think it is. So first, I'm going to show you what


### Photoshop Layers [0:47]
**Transcript (timestamped):**
[0:47] I did from the first camera projection. I rendered out a still image from Nuke using
[0:52] TVI scale first to reformat it to be twice the size. It's a little bit better than just
[0:56] a reformat notes. If you type in TVI scale, you'll find that I just want to start with
[1:00] higher res so that the generative AI would have something better to work with and potentially
[1:04] give higher res textures that we can downscale later. And so this was the base, just the
[1:09] grass kind of clean plated from our one of our previous videos. And if you're not familiar
[1:13] with the Photoshop workflow of how to use generative AI, I check out the last video I just posted,
[1:17] which kind of shows the way that I think this is going to be the most useful. So I'm not
[1:21] going to recover those topics that I already did. So just to show the layers though, in
[1:26] case anyone wants to see this was the first layer giving it some prompts. I think what
[1:29] was the prompt here, it was deep hole in the ground, artillery hole in the ground, grass
[1:33] hanging on the edge of the whole chunks of dirt. And it gave us weird rock in the center,
[1:37] but this side was actually pretty good. And so I just continue generating here, circle
[1:41] out that rock and then try it again. And that's giving some pretty decent results right off
[1:45] the bat. But I did want to make it bigger. And so employing the techniques I mentioned
[1:49] in the last video, I kind of clone stamp roughly down, and you can see the edges all soft and
[1:54] it's not very well integrated. But that's not really what we're worried about, because
[1:57] we just need to hint at the eye what we're trying to do. And so if you generate on top
[2:01] of that, we can clean up that edge. And it does all the work for us to get that nice
[2:06] grass and stuff hanging over the edge. And so I think that was the remainder of the layers,
[2:10] I think I adjusted a little bit further. And that was the first pass. Now if I take that


### Stretched Projection [2:15]
**Transcript (timestamped):**
[2:15] image I projected in nuke, I projected on the lighter scan, the flattened one that I did
[2:19] in the previous video, it could also just be a flat card, pretty much was just a flat
[2:23] card in terms of the shape of it. But if you project that out from the beginning frame,
[2:27] where I painted it, and put it on, that's our hole in 3D. And if I play, you'll see that we
[2:33] have a projection. Now you'll see immediately the problems that are associated with projections.
[2:36] We see it starts to stretch towards the end and stuff like that. But it is tracking well,
[2:40] and we have everything in a good starting place. And so this is what I want to experiment with
[2:45] was is to go further in the frame range and generate again, except from a different angle
[2:50] to see if we can fix this stretching effect that is normally happening. And that's a normal
[2:55] workflow for DMP anyway, to project images from different angles. But if we can generate it,
[2:59] it should save us some time. So the next thing I did was take that stretch projection frame,


### Additional Photoshop Layers [3:01]
**Transcript (timestamped):**
[3:05] I rendered it out, and I extended it with another generative AI to see will be down below in the
[3:11] hole, because we know the hole is not flat on the surface. So we want to see everything underneath.
[3:14] And then we're going to patch it again over the top. So this is the back wall and the ground is
[3:20] what we're trying to create. And so the first result was weird, it looked like an egg yolk or
[3:23] something. So I changed it, I also wanted to see more on the wall of the grass to see if we could
[3:28] get more layers of parallax. Because if we just see the back wall, it's going to feel a bit 2D.
[3:32] So part of the trick of this, I wanted to get like the edge wall that will overlap on the back
[3:37] wall. So if you can get at least three layers, it's going to feel a bit more 3D. So that's where
[3:41] understanding parallax is important. But just a bit more painting here and just generative fills.
[3:46] So you can see the process of just some different layers here, try to get something better on the
[3:50] bottom. And I also even took some areas that I thought were good, like over here. I just cut
[3:55] this out and flipped it, and then put this here and generate around it. And again, it's the same
[4:00] technique as the last video, when it has something on the edge to touch, it's going to give results
[4:05] that blend nicely with that edge. And so just keep doing that over and over. It kept wanting to
[4:11] generate these giant sticks for some reason. So that was something that it kept having a problem
[4:15] with. But it's not a perfect tool yet, but it is a tool that you can certainly use. So a little bit
[4:21] of manual clone stamping here, and then just finishing it up at the end. And that was the
[4:28] back wall and the floor. So this is another thing that we're going to project in new.


### Second Projection [4:30]
**Transcript (timestamped):**
[4:32] So again, this is looking at the stretch projection. And then this is bringing in the new image
[4:36] with the generated from a new angle. And then I just did a bit of corrections on this layer,
[4:42] adjusting the perspective a bit to match better, some small comp brightness adjustments and things
[4:47] like that, and cut it out with a roto. So we give it an alpha and we multiply that. And essentially
[4:53] after that, we want to project it onto not just a flat cylinder, but we want to create something
[4:57] that will give the illusion or enough breaking up of that parallax. So we read it as a rough


### Geometry Creation [5:02]
**Transcript (timestamped):**
[5:03] surface. So what I took was a cylinder, and I lined up with that lidar geo so I could see the
[5:08] other projection if I load the other projection here. And so that's what this looks like. And then
[5:14] I just took a some noise patterns and stuff like that with a displaced geo to get the broken up edge
[5:20] and lined it up with the where the back wall would be. And so we get the side walls and we get the
[5:25] broken up feeling. And I did emerge geo with another cylinder for the bottom. So that would be the
[5:30] ground plane of the bottom of the hole. And so that's what that starts to look like. And another
[5:36] card with a displaced geo just to give the wall a bit closer to the camera. So we feel more
[5:41] parallaxes if we can get some things closer and some things further, we're going to feel that
[5:45] distance a bit more. And so we merge that over. That's what we get. And now you notice we're seeing
[5:50] underground right now. So after this, we're going to add back the top of the grass. So if we add
[5:56] that layer back over, that's what that looks like. So we're starting to cover up back on the top area.


### Top Layer [6:00]
**Transcript (timestamped):**
[6:01] And I'll go through that now this top layer. So the top layer is actually being branched off from
[6:05] the original projection. So we have the original projection, we have the back wall and the bottom
[6:10] being merged in. I also did a little bit of sidewall geo there. And so that's the thing that we're
[6:15] seeing. But here I've branched off the pipe here to create a new sort of patch that we're going to
[6:21] create. And how we do this is we actually just because this is the way that this generated was
[6:27] the grass was over this something dark, it's pretty easy to create an alpha, we can just key it out
[6:31] with the lumic here. So we get this alpha here. And I solidified it a little bit. And if we
[6:37] pre multiply, that's going to be the patch that we put over the top again on that flat top ground
[6:41] plane that we already have. So if I mask this out, this is what we're slapping over the top.
[6:47] And I did add a little bit more around. So I took a branch off here, gave it a solid alpha,
[6:52] and I masked that just to give some more grass and stuff like that around, we wouldn't necessarily
[6:56] have to project all this area. But this is just fast, and I'm just putting a patch over. So I put
[7:01] this over the top like this. So these are the two things that we're going to project
[7:04] onto a ground plane. One important thing to note here is I did a little bit of a
[7:08] unpremult of roto paint and a pre malt and that's going to fix some dark edges on the grass.
[7:13] If I compare, let's go to frame, I think it's one, actually, we could just do this frame,
[7:18] let's just check this frame. And I'll just disable that correction and enable. So that's just a
[7:25] simple edge fix because we had that semi transparent grass over the darkness, we're going
[7:29] to have dark edges. So that's how you would fix that. It's actually similar to what I teach in
[7:33] my keen class with the edge painting and edge fixes, very common workflow to just extend the edges.
[7:38] So on pre malt, we paint but only in the RGB. And then we pre malt again. And then just some more
[7:45] corrections to fix some stretching a little bit sharpening because sometimes the AI will generate
[7:50] some softer and some sharper details. And you need to blend those things together.
[7:54] And then we have something like this, we project it out. And that's going to move with our image.
[8:00] Now one extra thing I did here, and this is pretty cool to know and useful is towards the end of the
[8:06] sequence. This started to stretch a little bit, you can see it's horizontally stretched. It's the
[8:10] same thing we were seeing before. Remember, when you're looking at the projection, it looks a bit
[8:15] stretched when we go further and further. And so one way you can actually fix that is to not


### Parallax Cheats [8:20]
**Transcript (timestamped):**
[8:20] just project onto a flat surface. Because we know that maybe the some of this grass is hanging
[8:24] over the edge. And so what I did here to prevent some of that stretching was essentially just take
[8:30] a card and displace it with a ramp. So if you take a black and white ramp, you're saying that
[8:36] we want to bend part of the card and not bend the other part. And so what that does is we can ignore
[8:42] this part that's straight up. But if you look just at the end here, what we're actually doing is just
[8:45] trying to get a bit of a bend. And that's what I'm projecting the grass onto. So rather than
[8:49] projecting on a flat card on the surface, we're just getting a little bit of that bend. And that's
[8:54] going to change the perspective of the projection as time goes on. And that's going to actually help
[8:59] prevent that stretching. So there's different ways to do that. Like I mentioned in the Clean Planting
[9:03] tutorial posted two videos ago, you can do eye transforms, just different techniques you can do
[9:07] to prevent or distort things in different ways when you're dealing with projections. And that's one
[9:12] way we can do it. And so now emerges over the top. And we have something that's covering up those
[9:18] areas. And that's working pretty well. Now the rest of these little projections and patches you see
[9:23] in the script here are just corrective patches, dissolves and stuff like that. And that's the
[9:27] techniques I talked about in the clean planning tutorial two videos ago. So if you're new to
[9:32] clean planning projections, all those things I recommend checking out Nuke 202, because that
[9:36] really dives into the 3d system and getting comfortable with those things. And so that's
[9:40] linked in the description as well. But that's about it for this tutorial. Hopefully you guys found
[9:44] this useful and you can start to apply this in other creative ways. I think there are a lot of


### Conclusion [9:45]
**Transcript (timestamped):**
[9:48] other creative ways. I've been experimenting with this on different projects. And I've seen a lot
[9:52] of interesting things that we can do with this. If you start to think outside the box a little bit.
[9:57] And so this is just one test I've done. But I do think that this scales into a lot of different
[10:01] scenarios that are very interesting. So if you liked it, press the like comment, tell me what you
[10:06] think about this workflow as well. If you've experimented with this at all. And that's about it.



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
