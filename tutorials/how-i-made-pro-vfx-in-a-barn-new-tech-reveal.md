---
title: How I Made Pro VFX in a BARN! (New Tech REVEAL)
source: YouTube
url: https://www.youtube.com/watch?v=TUPGJj4TjMk
author: Compositing Academy
ingested: 2026-08-17
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-i-made-pro-vfx-in-a-barn-new-tech-reveal/
frame_count: 0
frame_status: pending-selection
---

# How I Made Pro VFX in a BARN! (New Tech REVEAL)

**Source:** [YouTube](https://www.youtube.com/watch?v=TUPGJj4TjMk)
**Author:** Compositing Academy
**Duration:** 8m53s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py how-i-made-pro-vfx-in-a-barn-new-tech-reveal <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] This is the most insane way to do virtual production.
[0:03] We're in the middle of Canada transforming a simple barn into a virtual production set
[0:08] with a brand new product from LightCraft, Jet Set Cine.
[0:11] With this new product that only requires an iPhone and a Cine camera,
[0:15] we're going to prove that virtual production doesn't require multi-million dollar LED stages.
[0:20] All you actually need is a bit of craftiness and some wheel power.
[0:24] So stick around to the end of this video.
[0:26] We're going to show you the entire behind the scenes process of everything it took to produce it.
[0:30] And now we're going to show you the final result.


### Final Shot [0:32]
**Transcript (timestamped):**
[0:35] Material Handlers, this is a reminder to please keep your hands inside of the railing system at all times.
[0:42] So you might be wondering how exactly can you do this yourself and what tools we use.
[0:48] We're going to reveal the secrets in this video with your new or very experienced in the industry.


### Behind the Scenes Intro [0:50]
**Transcript (timestamped):**
[0:52] You're going to see some new combination of techniques here that I don't think can really be seen anywhere else.
[0:56] We're using Nuke Blender,
[0:58] which is a new product that we've been using for a long time.
[1:01] So we're going to show you the results of this.
[1:03] We're going to show you the results of this.
[1:05] We're going to show you the results of this.
[1:07] We're going to show you the results of this.
[1:09] I don't think can really be seen anywhere else.
[1:10] We're using Nuke Blender and Jet Set, which is on an iPhone.
[1:14] And the Sony FX3, which is the same camera used to film the creator.
[1:17] This video is going to be split into three different parts for the making of.
[1:21] First, we're going to talk about set building, scene planning and kid bashing.
[1:24] Then we're going to talk about practical effects in the VFX workflow.
[1:27] And then we're going to reveal the new virtual production pipeline that makes this whole production process to be really simple.


### Set Building & Scene Planning [1:34]
**Transcript (timestamped):**
[1:34] So I didn't have a huge amount of time or a team of VFX artists to put this together.
[1:38] So first part of this journey is going and finding a catwalk and finding these in real life.
[1:42] Relatively cheap is not that easy.
[1:44] I looked at some junkyards and eco centers and, you know, it's a big piece of metal, so it can be kind of expensive.
[1:49] So the solution that came up with was, I think, pretty interesting.
[1:52] My wife and I, we were shopping at different places looking for basically props.
[1:56] And we found some rubber mats that actually had the pattern that looked like the surface of a catwalk.
[2:01] I knew that also lighting was going to be coming from below.
[2:04] So the second problem I had was I need a way to raise these off the green screen and have somewhat of a gap between the floor and the walkway.
[2:11] So the solution we came up with was essentially using wood from these eco centers because it's cheap.
[2:17] We painted black and we aligned these across two different ladders that were parallel to each other.
[2:22] And this would give us the sort of structure underneath the rubber so it doesn't bend.
[2:26] And we can align these on top of the platform and now we have something that looks visually pretty much the same as a catwalk.
[2:32] For the background and rest of the virtual environment, I kitbashed using some big, medium, small assets, which is pretty much just like playing with Legos,
[2:38] except you're trying to come up with interesting compositions and lighting it in interesting ways.
[2:42] And I thought that these factory catwalks can be an interesting way to have 3D layered parallax.
[2:49] And it would also be a good way to connect the feet of the character to the grounds.
[2:53] So we don't have feet on a green screen, which is good to avoid.
[2:56] And the main principle I thought was really interesting was that the floor pieces are going to be repeated.
[3:01] So this means I can film in multiple set locations virtually while reusing the same set floor over and over.
[3:07] So I can make it look like you're in one section of the factory or another section by just keep reusing the same floor pieces over and over.


### Practical FX [3:13]
**Transcript (timestamped):**
[3:14] Part two, filming practical effects.
[3:18] So one of the things that can make CG environments feel very dull is the lack of motion.
[3:22] There's a number of ways to add interesting motion to shots.
[3:25] But one of the ways I wanted to do this was to have lots of different moving VFX elements.
[3:29] First, I have smoke, I have acid barrels, I have sparks, and I have the camera and the parallax of the objects passing over each other.
[3:36] We started with shooting the smoke and these were captured on ProRes RAW using the Sony FX3.
[3:41] So this means I can use them later in other projects as well because I'm always trying to build my own VFX element library.
[3:46] So if you want these, they're in the Composite Academy smoke bundle if you want them for your own projects.
[3:51] So we use a variety of smoke machines and dry ice techniques filmed on black screens to get a set of different motions.
[3:57] Additionally for the really thick self-shadowing stuff, I use EmberGen because it's fast for medium distance simulations and it works really great.
[4:04] And mixing CG assets with practical effects around the edges can really enhance the level detail and the randomness.
[4:10] And also EmberGen lets us control the self-shadowing and the amount of rim light we need on that thicker smoke.
[4:16] So it's really important for the density.
[4:18] So thin smoke and thick smoke is something that you really need to consider when you're composing a shot.
[4:22] I knew the character was going to be walking past some large acid barrels.
[4:26] These barrels were kind of an experiment to figure out.
[4:28] I didn't know exactly what was going to work here.
[4:30] Well, I knew I wanted them to be kind of strange looking on the surface, but not like rippling like soap bubbles.
[4:37] The way we came to an interesting result was to shoot some glow sticks with glow in the dark paint mixed with various thicknesses of liquid soap.
[4:45] And this with an air compressor blowing down from the top gave some interesting results.
[4:48] And this was all lit using a black light.
[4:51] So in Nuke, I key mixed these various recordings together to create a continuous rippling effect.
[4:56] And essentially this 2D video pattern is going to be wrapped onto some proxy geometry that I can just grab out of blender on top of the cylinders.


### Lightcraft Jetset Virtual Production [5:05]
**Transcript (timestamped):**
[5:11] Continuing with the cost-effective filmmaking techniques, I didn't want to run out green screen stage because I wanted to take time experimenting with this new technology.
[5:18] See how it works and get a feel for how I was going to use it.
[5:21] Found out my wife's grandparents have a barn that hay used to be stored in the top floor, but it's no longer in use.
[5:27] So this means we have a very dark, basically large space, which is really what I needed for a cinematic backlit shot.
[5:33] Because the actor is going to be need to be a certain distance away from the green screen.
[5:37] So we can light the green screen, but keep the actor dark.
[5:39] And you need a fairly big space to be able to do this.
[5:42] So some of the budget we invested into various aperture lights, which allows me to control the whole onset lighting from my phone.
[5:48] Which means I can relight the actor based on where we're going to orient them to the virtual set.
[5:53] And this is really useful because I can just control all of the lights from my camera.
[5:57] So I have my rig, I have my lighting set up, and I also have the virtual scene all controlled from my iPhone.
[6:03] Next I'm loaded in the CG set into the app.
[6:05] So Jet Set makes it very simple.
[6:07] Placing the origin is essentially where we want to snap our CG scene to.
[6:11] I chose to keep using the bottom corner of the catwalk and I could snap my scene to various locations virtually.
[6:17] So this means if I rotate the whole virtual set and I want to film in different angles, you can.
[6:21] And you can use the green screen key or AI matte to basically pre-vis or pre-visualize what you're doing.
[6:28] So one really interesting thing I wanted to show this virtual production sequence was the unique ability that Jet Set has.
[6:33] Which is not just having a background replacement like an LED stage, but rather having CG assets that pass in front of the character.
[6:41] So if you actually load the app, you'll see that you can actually occlude your hand behind CG objects using the LiDAR scanner on your phone.
[6:48] And so this helps for pre-vis, it's not the final result, but it helps direct the scene and discover shots like a filmmaker would.
[6:54] The big difference between the free version and the cine version is that you're tracking your cine camera.
[6:59] The app calculates the offset between the iPhone and the cine lens by doing a lens calibration process.
[7:05] So you temporarily attach this Aksun SEMA, which is processing both cameras and comparing the features internally.
[7:11] Once you're done, the Aksun can come off and now you're ready to film.
[7:15] And you can do a LiDAR scan as well, which will be really useful for aligning tracks later on if you need to.
[7:20] So you have the scan of your real set that can be overlaid on your virtual set.
[7:24] So after you start filming, all of this 3D tech, this data will be basically packaged up.
[7:28] And you can export it to any 3D software you want, using Blender or Nuke, whatever it is.
[7:34] Jet Set makes it very simple.
[7:35] They have essentially a system on the back end called AutoShot that essentially speeds up this whole process.
[7:40] So what they're essentially doing here is actually creating not just like a camera tracking app for one angle,
[7:45] but actually it's a virtual production pipeline.
[7:47] Thanks to the team at Lightcraft for sponsoring this video.
[7:50] You should definitely check out and download their app.
[7:52] If you have an iPhone, it's called Jet Set.
[7:54] You also have a free version that you can just use and play around with and start to see how this can be used creatively.
[7:59] After using the product, I will be using this on other virtual production shoots that I'm directing.
[8:03] I think it's very useful creatively as a filmmaker to just move around and have a sense of where you are.
[8:09] And you're not shooting into the green void.
[8:11] That's the biggest value add I see here, as well as the speeding up on the back end of just getting everything delivered
[8:17] and being able to sort of cut out some of that manual tedious work that's normally involved.


### Conclusion [8:22]
**Transcript (timestamped):**
[8:22] So guys, if you want to see the Nuke compositing portion of these shots,
[8:25] there are going to be a bunch of tutorials coming on this YouTube channel soon.
[8:28] If you're a filmmaker, CG artist, or VFX composer that wants to add Nuke compositing to your arsenal,
[8:33] we've built the easiest, most comprehensive path in the Nuke beginner series.
[8:37] This leverages my background as a VFX artist working on films like Star Wars, Avengers, Across the Spider-Verse, and more.
[8:42] So check out the courses if you're interested.
[8:44] We have stuff for all skill levels.
[8:45] And that's about it for the video, guys.
[8:47] Make sure to hit like on the video so we can keep making more videos like this.
[8:50] And let me know what you thought in the comments below.



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
