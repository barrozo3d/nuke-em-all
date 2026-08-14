---
title: The BEST Way to Use Normals to Relight in Nuke (NEW Toolset)
source: YouTube
url: https://www.youtube.com/watch?v=M-iKJu9hYBk
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/the-best-way-to-use-normals-to-relight-in-nuke-new-toolset/
frame_count: 0
frame_status: pending-selection
---

# The BEST Way to Use Normals to Relight in Nuke (NEW Toolset)

**Source:** [YouTube](https://www.youtube.com/watch?v=M-iKJu9hYBk)
**Author:** Compositing Academy
**Duration:** 8m56s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py the-best-way-to-use-normals-to-relight-in-nuke-new-toolset <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to this video. Today I'm going to be releasing a brand new toolkit for composters for free, which is the Normals Toolkit.
[0:06] So if you watch videos on this channel before, you see me do normals relighting a few different times,
[0:11] whether it's for a CG render and sort of enhancing the different light sources or detail on the surface,
[0:15] or if we're using AI generated normals and enhancing or adding specific light sources to the footage, which is a newer workflow.
[0:22] Both of these workflows still rely on having normals, but the quality of your normals can differ depending on the source that you're getting it from,
[0:29] and so I'm going to show you a few different examples on how we can actually enhance the normal result by using a specific technique.
[0:36] In this toolkit, there are three different nodes that actually work together to solve the entire problem, to make it more systematized and repeatable,
[0:43] especially if you're doing it on a team or if you're doing it for a larger project.
[0:46] So I'm going to hop into Nuke and show you how these three nodes work together to create a better result than just doing a simple relight.
[0:51] Alright, so to give some context on what we're going to try to relight, this is for a digital map painting that I'm working on for a larger sequence
[0:57] for a YouTube video coming out in a few months.
[1:00] So this is going to be a good example for relighting because we can add some more cinematic lighting to this scan that I have of a mountain.
[1:07] So basically I have this mesh that is scanned in Iceland and it's like a huge mesh.
[1:12] This is a few thousand photos basically taken around a mountain, and this gives us a really nice proxy geometry for the base of our map painting.
[1:20] So if I look at this in 2D, we can see that the texture here is pretty nice and it gives us something a little bit easier to work with than just completely two dimensional images,
[1:27] because we get the perspective, we also get the utility passes.
[1:30] Even if it's far away, the extra information can help us do our job.
[1:34] What I want to do is to make this have more cinematic lighting.
[1:37] So this is going to be more of a moody shot.
[1:39] It's going to be a little bit more stormy and all those type of things.
[1:41] So if I look at this without the sort of enhancement that I'm talking about, and we just do the base relighting using a variety of techniques here,
[1:49] this is sort of a good starting point of what I want to do.
[1:52] Now this doesn't have haze yet or anything like that.
[1:54] We're sort of just playing with this idea of sort of a cloudy day with some holes punched into the clouds and lighting the mountain in this nice cinematic way.
[2:02] Now how do we make this better?
[2:03] And what's the problem exactly with this?
[2:05] So if you zoom in here, we can see it looks a little bit CG.
[2:09] We have some very sharp edges, some sort of triangular feeling things.
[2:12] And it just feels a little bit plasticky.
[2:14] It's kind of the same problem that I mentioned on some of those other videos that this is normally the mistake.
[2:19] Anytime you're doing normals, relighting people miss this if they're just doing it for the first time.
[2:23] But it's the most important thing.
[2:25] And so how do we improve it in this example?
[2:27] Now in the past, I would have probably just pulled the highlights and shadows and mixed a few different keys to break up this surface, make it not look so plasticky.
[2:35] But basically this is a better way to actually do it.
[2:37] So this node, what it does is it takes the normals that we have.
[2:41] So this is a low resolution result from the proxy mesh.
[2:44] What we want to do is add high frequency detail mixed into the normals.
[2:48] And so how do we get the high frequency detail first?
[2:50] And then how do we mix it?
[2:52] So that's what the two nodes actually do.
[2:55] So we have the CA detail normals, which will actually extract normals from either the luminance or frequency.
[3:01] So it's either or.
[3:03] And we can actually, by having both, we can target different areas.
[3:06] So that's the first principle here is that we're going to basically either target by doing a frequency separation,
[3:12] which means we're targeting the size of the details on the specific image, not necessarily the luminance, but the size.
[3:18] And then the other one is more just targeting the luminance.
[3:21] So we get something slightly different.
[3:23] And then we have a node called normal mixer.
[3:25] So what this node does is really cool.
[3:27] It basically reorients these normals to all face the same direction so that you're realizing will actually behave properly.
[3:33] You can't have normals pointing in different random directions.
[3:36] Otherwise, it's not going to work.
[3:37] So what this does is actually does a calculation to orient them in the same direction here.
[3:42] So what we can do is we can take our base CG normals like this and we can throw a normal mixer with these two that I just mixed together.
[3:50] Two different types of frequencies that we've kind of targeted.
[3:53] And if we mix this onto the result, this is what we actually get.
[3:56] So if we zoom in here, we can actually see that this is adding detail to the normals, but not only is it adding detail,
[4:02] it's adding it in the correct orientation.
[4:04] So that means we just get the result that we're going to be looking for with our relighting.
[4:08] So if we add this onto here and we just go back to the result.
[4:12] Essentially, we can see like an area over here.
[4:14] If I were to like unplug this and put it back into the basic proxy mesh,
[4:19] we could see it looks a bit flat in CG.
[4:22] We lose all the little micro details, the micro shadows and highlights that we're supposed to get on a terrain.
[4:27] So if I plug that back in, we wait a second, we can see like that detail gets pulled back out and this works pretty well.
[4:33] Now some areas might need to tone it down a little bit.
[4:35] Maybe there's a little bit in bossy if we look at it like that.
[4:38] But really just everywhere is just going to look significantly better.
[4:41] So if I just switch this back once again, just to look at again,
[4:44] we can see that's doing a really nice job just to add detail across the map painting.
[4:48] Now just before I jump into the other examples, it's worth mentioning.
[4:50] If you're interested in more of these creative techniques or how you layer all these images with all these techniques combined,
[4:56] there's a lot of stuff in the advanced classes for people who already know a little bit of Nuke,
[4:59] but they're really looking for creative projects or higher level projects that show a lot more techniques
[5:04] that you can only learn really by doing the job.
[5:07] So let's take a look at a simpler example just to see again the idea and how it goes further.
[5:11] So if we have like an image here that has some normals in it.
[5:14] So I've just took in a sphere here, Nuke put a basic texture on it and we have some basic image here.
[5:19] If we were to just cast light on this using the normals, it would look very flat.
[5:24] So we have to do this approach where we mix the normals in order to get some kind of alpha that's going to represent it properly.
[5:29] And so what we can do is we can use the color of the image to create a bit of a detailed normal pass.
[5:35] And we can take the normals from the render and we use the normal mixer and then we get the best result.
[5:41] Now notice in the detail normals, if you just generate normals from the image and you don't do anything to it and we look at it,
[5:47] that's not that useful because it doesn't follow the curvature of the actual model or the shape of the surface.
[5:53] So why this normal mixer is really cool is because it's taking this, the base as the sort of master normals and adding this to it.
[6:02] So if we create an alpha based on that using this, we can see it's following the curvature of the sphere, but also interacting with the normals.
[6:10] So if we just did normal mask on this very flat image, that's not exactly what we'd want.
[6:14] We have to do a bunch of masking to compensate for it.
[6:16] So by mixing this approach, we get these nice like feathering approach and you know, if we move the light around, we get a result that we would kind of expect.
[6:23] Now what's cool about this is if we wanted to pop out certain details by separating the normal into layers of frequencies like this,
[6:29] we can actually get more control than any other approach really.
[6:33] So if we have like a detailed normals here and let's say I want to make some of the rocks look a little bit more three dimensional.
[6:38] Maybe it's not doing the best job popping those out as much as we want.
[6:42] We can take something like a roto shape and just circle a few of the rocks and create a normals from that.
[6:47] And then taking this result, we can mix that with the one we just saw before.
[6:50] So here's what we have and then we mix that together and now that's going to make those areas look a little bit more three dimensional.
[6:56] If we mix this result onto the base result, this will now follow the curve to the sphere and it has the detail of the normals that we've just added.
[7:04] So if we take this result and we do a bit of a relight on it, essentially we're going to get something that makes it look more 3D in those different areas.
[7:11] So if we just rotate this around again, we get something that we can kind of expect.
[7:15] So if we want to control the height of just those three little dots, we can go back to our detailed normals and maybe we just pull down the strength a little bit
[7:22] and that will make it look less 3D.
[7:24] So we have a lot of control over different specific targeted areas and how much detail we want to pull out or pull in.
[7:30] So really the tool set is just these three nodes.
[7:32] It's the detail normals to generate from images.
[7:35] We have the mixer and then we just have a masking node which is kind of convenient because we have a few different controls like rotation or we can switch to sampling if you want.
[7:44] So if you want to sample from a specific angle, like if I sample down here, it will just automatically orient the light in the right direction.
[7:51] If you'll want to think too much about it.
[7:53] So whichever way you prefer rotation or sampling either works.
[7:56] The nice thing about this normal node as well in terms of the masking one is you also want to make sure that you have a certain angle.
[8:00] We also have softness so we can create something that looks a little bit more specular as well.
[8:04] So if we go here and then we kind of rotate this light around and we increase this a lot, we can get something that looks much more specular.
[8:12] So we could create a nice specular highlight without having to do the full realize setup that new cast by default, which I don't think is that good.
[8:18] It's too many nodes for what you're trying to achieve.
[8:20] Like this is just supposed to be fast.
[8:22] We want to add a specular.
[8:23] We want to relight it without having to open a whole 3D system, you know, for example, most of the time that's overkill.
[8:28] So at least for my personal preference, this is the workflow that I've kind of been establishing.
[8:34] So I wanted to put out there free if other people find it useful.
[8:37] So that's pretty much it.
[8:38] You can grab it on the link here and there's the three nodes here and you can play around with it and a little bit of an example scene that just opened there.
[8:45] And some definition of the specific knobs in the nodes.
[8:48] Pretty simple to figure out, but the workflow is what's more interesting here.
[8:52] I think so that's here for those who want it and that's about it.



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
