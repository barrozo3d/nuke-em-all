---
title: This ONE Step Makes CG Look Cinematic (Most Artists Skip It)
source: YouTube
url: https://www.youtube.com/watch?v=twEVqozvpMk
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/this-one-step-makes-cg-look-cinematic-most-artists-skip-it/
frame_count: 0
frame_status: pending-selection
---

# This ONE Step Makes CG Look Cinematic (Most Artists Skip It)

**Source:** [YouTube](https://www.youtube.com/watch?v=twEVqozvpMk)
**Author:** Compositing Academy
**Duration:** 6m38s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py this-one-step-makes-cg-look-cinematic-most-artists-skip-it <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] What's up guys, this is a little mini 5 minute tutorial on some CG compositing techniques that I've learned over the last few years working on films like Spider-Verse, Star Wars, Avengers and more
[0:10] Though a lot of beginners doing visual effects, they don't realize that you don't just go from your CG render, you know, the lighting to the final shot in like color grading and resolve
[0:20] There's actually CG compositing in between, which is an invaluable step in refining the lighting and making those really small details pop out
[0:29] So this is just a few techniques, if you want to get the full class, I'm actually adding this entire project to the new beginner series, which is available in the link below
[0:37] But I want to explain a few things that are useful, especially when you're working on feature film or even animated film, they use a specific term
[0:45] And that term is called first read or second read, but when you first read this image, when you first see it, and what is your media impression and where does your eye go?
[0:55] So this of course is trained over time, but it's also sort of a subconscious thing that supervisors are often looking for and as a senior compositor, or as you get more experiences in compositing, you're going to be able to essentially read images in this way more naturally as well
[1:10] So one of the things that these supervisors and art directors are going to look for, and your job as senior compositor to know equally as well is to be able to see silhouettes and see where your eye is being drawn
[1:25] And so when we look at this image, my first read, my first impression starts to go actually back here, back to the most high contrast thing. We also see some of this and maybe here
[1:37] But what exactly is the story that we're trying to tell in this image? Remember, your eyes are going to go to the most contrast thing or the most sharp thing. So we can reduce where your eye goes by doing the opposite of those things
[1:51] So if we want to draw the eye to something, what do we need to do? We need to add contrast or brightness to it. So, and that is typically the case. Or the alternative would be we reduce contrast somewhere else so that, you know, that would be the case
[2:05] But my other problem with this image is that the last thing that I'm kind of reading here is actually the area that we're supposed to be looking at, which is the character
[2:14] And, you know, we could do a very silhouette shot where we barely see anything and he's more of a backlit thing and we want to bring out the edge
[2:22] That's one style of a shot that we could do, but I didn't want to direct it in that way
[2:27] I wanted to actually like read and see the face of the person
[2:30] And so part of the problem here is that the silhouette is not very clear of what's going on. So if we look at this, essentially the gun and the face are almost blending together
[2:39] So what we want to do to increase contrast, which is to draw the eye in is we're going to take one of the light groups and the light group is a little bit different than an AOV
[2:50] And we're going to bring it up. So light group, I'll just say LG, a little bit different than AOVs. AOVs, as we know, are the passes
[2:58] All the passes reflection, specular diffuse, etc, etc. We're to know what AOVs are. Light groups are combinations of those things, but really all you can think of it as is there's an orange light group for the orange light here
[3:11] So this would be like one light group, and then there would be another light group for the greenish blue light on the left side. So those are the two light groups that we can control
[3:20] Sometimes when you're controlling light groups, it can conflict a little bit with AOVs. The math won't add up exactly the same because maybe they would be always slightly separately
[3:28] So what I'm trying to say there is sometimes you'll just do light groups or sometimes they'll use AOVs, but sometimes you're not going to be doing both because they'll conflict with each other
[3:37] So in this cop, I wanted to just use the light groups rather than breaking into every layer because you know the lighting is pretty good here and we have like most information that we need
[3:46] So that is one thing to consider. So what do we want to do? I'm going to use the light group to increase the contrast on the face
[3:54] So I'm going to bring up the orange light, but we want to bring up the orange light everywhere. I don't want to just make it brighter
[3:59] Really what I want to do is create readable silhouettes and add contrast. So I want to create a silhouette on this gun
[4:06] I want to basically see the edge of the gun, which I can't because it's too dark
[4:10] And we're going to do that by actually just brightening up this area right here. So we're just going to brighten up just behind
[4:15] And we can use a 3D position mat tracked onto the face to basically bring that up
[4:22] And once that's done, this area will be brighter. So literally we're just brightening the face and cutting it out away from the gun. Pretty simple
[4:29] Now also other things we could do, we could also bring up maybe the tip of the gun. That would be kind of cool. We could bring up the specs like here
[4:35] Maybe that would be another contrast point. We want to draw the viewer so we could just like, you know, if there's two points of contrast, maybe that's a bit brighter
[4:44] And then this is a bit brighter. So we're kind of, you know, if the person's eyes are moving on this image, we're going to look in this direction
[4:51] We want to use the perspective of the gun as sort of a tool to drive the eye towards the viewer
[4:58] And the camera's also pushing in towards the shot. So that this very linear line as well is going to help us sort of draw everything in
[5:07] And because this is out of focus and this is sharper, your eye is going to want to go away from the out of focus thing in this direction
[5:13] But it would be still nice to see a little bit of that breaking against the edge of the background
[5:19] And, you know, yeah, we're not seeing much of that right now. Like I'm not even reading the edge of this gun. So we could, you know, either relight it or just bring up the tip here
[5:28] Which is pretty much what I did in the actual. So let's just take a look here at the actual comp. So we just go to, and these are very small adjustments, by the way
[5:35] They're not like massive adjustments. So that's the tweaks. We're just bringing up those little areas, bringing up this and bringing up that
[5:41] But keeping the gun relatively the same. We could also bring up the reflections out of the side of the gun if you wanted, just like a tiny bit here
[5:48] The other thing I did was I also just targeted the sunglasses and brought that up a tiny bit. I wanted to actually keep the bring up this eye light slightly
[5:55] So I put the reflection of the light. I put the light very specifically in scene so it reflects here and looks similar to an eye light
[6:02] So on animated films actually, especially they spend a lot of time always trying to get spec in the eyes and even though we have sunglasses
[6:08] We can still read that it's going to read a bit better as eyes and sunglasses versus just being a black thing
[6:13] So that's more of a lighting thing, but composters have to understand lighting pretty much equally as well
[6:19] Because we need to refine it to the final lighting. That's what composters are literally doing
[6:24] So those are a few things we can do and now we can talk about specifically how we're going to do it using some position data
[6:30] Or we can track down some rotos and things like that



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
