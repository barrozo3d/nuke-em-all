---
title: Nuke Compositing Artistic Basics (1/8): Roles of Production
source: YouTube
url: https://www.youtube.com/watch?v=cQV6c291fBU
author: Compositing Academy
ingested: 2026-08-14
app: "Cross-app theory (no software shown — VFX pipeline/production-role overview, applicable to any comp app including Nuke)"
version: "not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021)"
tags: [compositing, beginner]
extraction_status: complete
frames_dir: tutorials/frames/nuke-compositing-artistic-basics-18-roles-of-production/
frame_count: 4
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Nuke Compositing Artistic Basics (1/8): Roles of Production

**Source:** [YouTube](https://www.youtube.com/watch?v=cQV6c291fBU)
**Author:** Compositing Academy
**Duration:** 10m33s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Welcome to the class. We're going to jump right in. I'm going to go through a couple of theory lessons.
[0:07] This first section is theory lessons before we start doing the compositing.
[0:12] I'm not going to drag it on and make it way too long, but I'm going to touch on a couple of those subjects
[0:18] just to make sure we have a little bit of a foundation before we jump in and actually start compositing the shot.
[0:25] I'm going to bring up the theory as well when we're compositing, because sometimes it's a bit easier to learn
[0:32] while we're actually doing it rather than just looking at too much theory.
[0:37] Quickly, I'm just going to explain to you guys how production works in a Visual Effects Studio
[0:41] if you're talking about a big production studio or even medium-sized, for that matter, Visual Effects House.


### Workflow [0:49]
**Transcript (timestamped):**
[0:49] This is the workflow and the order of operations for a Visual Effects Studio.
[0:59] I'm going to get my draw tool here. You can see compositors were always at the end.
[1:06] If you're working on a team, and this project pretty much acts like we're acting on a team,
[1:12] I'm going to be providing you guys some assets, some footage, and that would be normal.
[1:17] If you're working on a team in a Visual Effects Studio, this is how you would be working.
[1:21] That's trying to simulate that.
[1:23] I'm going to quickly, you guys might have different levels of experience, so I don't know what you know or don't know.
[1:29] I'm just going to very lightly touch on these different topics just so we can get everybody on the same page.
[1:37] Quickly, going over what each of these departments, what are these people doing,
[1:42] and why does it have to go through all these people before we get to do anything to the shot?
[1:48] If we just talk about what this is, we have Match Move.
[1:52] Match Move is basically 3D camera tracking and camera solving.
[1:56] If you've taken my previous new courses, we actually did some of that on our own.
[2:01] Depending on the studio you're working in, sometimes you'll need to do your own 3D tracks.
[2:06] If you're working in a big studio, actually there's an entire department that does the 3D tracking for you.
[2:12] You'll actually just get the 3D camera and you'll actually get some ground geometry already given to you, depending on the size of the studio.
[2:21] If you're working more on a freelance job or you're working on your own projects, you're going to have to know how to do that yourself, the Match Move.


### Match Move [2:27]
**Transcript (timestamped):**
[2:28] That's why I teach it because the best way to learn is your own projects.
[2:32] It's really important to be able to track stuff if you want to learn how to compose it.
[2:38] But then again, if you're in a big production movie, some of those things are going to get handed to you to speed up the process.
[2:46] Next, we would be going... There's two different paths here. I've done two different sides here.


### Effects [2:52]
**Transcript (timestamped):**
[2:54] The left side is talking about if we're doing something like an explosion and the right side is talking about something like a car.
[3:01] I'm going to go over the left side first. Effects is pretty self-explanatory.
[3:05] These are people who simulate explosions, they simulate geometry, crumbling, they can do tornadoes and stuff like that.
[3:15] They're really into particles and oceans and stuff like that.
[3:18] It's a heavy computer simulation and they'll render out an image sequence or movie file of that CG.
[3:27] When they do that, they'll hand that off to the texturing and shading team.
[3:33] Sometimes they'll do it themselves. Let's say if it's an ocean, they're going to simulate the waves and then they'll give it to a team of people that will make those waves look real.
[3:44] They're going to add the foam to it, they're going to add textures and all kinds of stuff.
[3:49] Lastly, they would hand it off to the lighting team so they would just match the light of the real footage if we're talking about a real composite.
[3:58] Let's say we're talking about a movie like Pirates of the Caribbean.
[4:01] We might have an ocean that was simulated by the effects team.
[4:08] Then it was shaded and then the lighters, if there's some real footage, maybe we're standing on a pirate ship and the ocean is in the background, the lighters would match the light direction of the waves.
[4:20] Lastly, that would be handed off to the compositor to make it look real and add the final touches.
[4:25] We're getting an asset that has a lot of work already done to it, but a lot of times it still needs quite a lot of work to vary in degrees.
[4:34] Sometimes you get good CG, sometimes you get CG that it's pretty off and the compositors are basically pulling off miracles.
[4:42] That's what we're known for.
[4:45] Compositors are kind of a jack of all trades.
[4:47] You need to know a little bit of every piece, maybe a little bit of particle simulation, maybe a little bit of camera tracking, some very basic modeling and probably a deeper understanding of lighting.
[5:01] A compositor needs to have, what's most important for a compositor really is an understanding of lighting and compositing because they're close to each other and you need to have that photographic eye.
[5:12] You need to also understand a little bit about cameras.
[5:15] That's where we are in the pipeline.
[5:17] If we explain it for a CG model, we would be matching, let's say it's a car, so this is what we're doing in our class.


### Rigging [5:21]
**Transcript (timestamped):**
[5:27] We have a 3D camera tracked scene.
[5:30] We have a car model that was already created, so I modeled that car.
[5:34] That car has been textured and shaded.
[5:37] We don't have any rigging, so what rigging is, is if you have a character, you need to have some muscles inside of it and some skeletal structures.
[5:47] If we use an example, let's say we're talking about an avatar.
[5:55] Somebody had to model the avatar, texture it, and then they give it a skeletal and skin system.
[6:01] Then they'll hand it off to the animation team to actually make it move.
[6:04] Then it will be handed off to a lighter to light it to the scene and then a compositor will bring it together.
[6:10] That's the workflow of things.
[6:14] Tracking, then you model it, texture it, give it a system if it needs one.
[6:20] Animate it if it needs it, depending on what the object is, and then we light it and composite it.
[6:27] The compositor, sometimes we have to fix the lighting.
[6:31] Sometimes the lighting, they get it relatively close, but it's not a holly percent.
[6:36] Sometimes it's pretty far off, so that's all good to know.


### Assets [6:40]
**Transcript (timestamped):**
[6:41] That's kind of the overview of the roles of production and where we sit in the pipeline.
[6:46] That's what we're going to be simulating in this class. We're at the end of this pipeline.
[6:49] We're getting stuff from all these people. How can we make it all come together?
[6:53] Just to show you this in another way, this is what you could expect in this class.
[6:58] If this was a real production and you were getting assets from other people, this is what you would be receiving.
[7:04] You would be receiving, let me get my tool again.
[7:11] We have our background footage here, so that's called our plate.
[7:16] This comes from a department that would be called editorial.
[7:20] They specialize in bringing in elements and footage for you.
[7:25] This is given to you from these guys.
[7:32] Then we have some elements, so we have some rain elements, some textures, and we also have a sky element.
[7:39] We're going to have to bring these together.
[7:42] We're going to have to take all these assets and make them match.
[7:46] We have a car from lighting and we have a ground plane from lighting as well.
[7:52] We need to make those work together with our footage.
[7:56] Then we also have from match move, they've just supplied us.
[7:59] This is me making these things for you guys, but we're talking hypothetical.
[8:03] They've supplied us with a ground plane that's already tracked in case we need it.
[8:08] If we want to replace part of the ground or project some puddles or something like that,
[8:13] stuff we're going to do in this class, we're going to project some things on the ground.
[8:17] We have a camera, so in case we want to add some 3D elements or something sticking in the scene,
[8:23] we already have the two fundamental things we need, so we don't need to waste time solving it.
[8:29] We also have a lens distortion solved, so we don't have to worry about trying to draw the lines and get the distortion.
[8:35] All of this is done for you and you just get to do your job as a compositor to make that shot come together.
[8:42] Then last we have our effects.
[8:45] Just something to note here, you'll notice sometimes effects team will send their effects over to lighting
[8:54] and then lighting will send it to the compositor.
[8:56] But sometimes effects will just send it directly to you and lighting will send you other stuff.
[9:02] But then you see there's a problem because this effect doesn't match the lighting of our car and the lighting of our plate.
[9:17] So you can see how that would be a problem, but that's our job.
[9:21] Our job is to bring all these elements together and make them match, make them work together.
[9:27] We certainly can do that with our effects.
[9:29] We can do some tricks here to make this look like it's filmed in this environment or make it look like it's coming from the headlights of this car.
[9:39] Composers can get away with a lot of stuff.
[9:41] There's a lot you can do.
[9:42] You should think really open-minded.
[9:45] A lot of times it's a hack.
[9:48] Sometimes it's just thinking outside the box to try to solve a problem.
[9:54] But if we're supplied with these things, we basically build the scene and we also have a lot of creative control.
[10:00] So we're going to create our own elements as well.
[10:04] So the compositor, we've been given all these elements, but we're also going to create our own elements.
[10:09] Maybe we'll create some drip elements simulated in Nuke or in 2D.
[10:15] There's other things we can create.
[10:18] So we're going to do all that kind of stuff and bring all this together.
[10:23] So that's just the overall production workflow.
[10:25] That's what we're going to be doing in this class.
[10:27] And yeah, let's move on to some concepts.



---

## Captured Frames

- [1:00] tutorials/frames/nuke-compositing-artistic-basics-18-roles-of-production/frame_000.jpg
- [4:15] tutorials/frames/nuke-compositing-artistic-basics-18-roles-of-production/frame_001.jpg
- [7:11] tutorials/frames/nuke-compositing-artistic-basics-18-roles-of-production/frame_002.jpg
- [9:00] tutorials/frames/nuke-compositing-artistic-basics-18-roles-of-production/frame_003.jpg

---

## Structured Notes

### Core Technique
Part 1 of 8. A theory-only overview of standard VFX studio production pipeline roles (Match Move, Effects, Texturing/Shading, Rigging, Animation, Lighting, Editorial) and where the compositor sits at the very end of that chain — framing context for the rest of the "Artistic Basics" series, which simulates receiving assets from each of these departments.

### Summary
No software shown — a whiteboard/slide-style lecture. Walks through the standard order of operations in a mid-to-large VFX studio: Match Move (3D camera tracking/solving — sometimes handled by a dedicated department, sometimes the compositor's own job on smaller teams/freelance work) feeds into two parallel paths — an Effects path (simulation artists doing explosions, fluids, destruction, particles → handed to Texturing/Shading → Lighting to match the real plate) and a CG-asset path (a modeled object like a car, optionally Rigging + Animation for characters, then Lighting). Both paths converge at the Compositor, who is described as "a jack of all trades" needing baseline knowledge of particle sim, camera tracking, basic modeling, and especially a strong understanding of lighting and a "photographic eye," since CG lighting handed off to comp is often close but rarely 100% correct — fixing that gap is core compositor work. Previews the class's own simulated production hand-off: a background plate (from Editorial), rain/texture/sky elements, a lit car + tracked ground plane (from Lighting), a pre-solved camera + lens distortion (from Match Move), and effects elements that may not yet match the plate's lighting — establishing that the compositor's job across this whole series is to make all of these disparate, imperfectly-matched elements look like they belong in the same shot.

### Key Steps
1. Recognize the studio pipeline order: Match Move (camera tracking/solving) → splits into (a) Effects → Texturing/Shading → Lighting, and (b) CG asset modeling → Rigging/Animation (if needed) → Lighting → both converge at the Compositor.
2. Understand each department's deliverable: Editorial supplies the background plate; Match Move supplies a solved camera, tracked ground geometry, and lens distortion data; Lighting supplies lit CG assets (e.g. a car) and a lit ground plane; Effects supplies simulated elements (e.g. rain) that may or may not already be lighting-matched to the plate.
3. Recognize the compositor's core value-add: reconciling mismatches (e.g. an effects element lit differently than the car/plate), fixing "relatively close but not 100%" CG lighting, and creatively solving problems the other departments didn't fully resolve.
4. Adopt the "jack of all trades" mindset for compositors — baseline fluency in particle simulation, camera tracking, basic modeling, and especially lighting/photographic judgment, since these adjacent skills inform better compositing decisions even when another department did the primary work.

### Nodes / Tools / Settings
None — pure pipeline/production-role theory, no Nuke UI or nodes shown; sets up the practical shot-building work in the rest of this 8-part series.

### Difficulty
Beginner — conceptual/theory primer, no software operations.

### Foundry App & Version
Not applicable — no app shown on screen; pipeline concepts apply across any studio/compositing package. 2020 upload, predates this skill's release-notes backfill (starts at Nuke 13.0/March 2021); the rest of this series is hands-on in Nuke.

### Tags
compositing, beginner

---

## Related Tutorials
**Nuke Compositing Artistic Basics — 8-part series** (this is Part 1 of 8; all parts cross-link to each other):
- Part 2/8: 3 Point Lighting (`nuke-compositing-artistic-basics-28-3-point-lighting.md`)
- Part 3/8: Exposure (`nuke-compositing-artistic-basics-38-exposure.md`)
- Part 4/8: Shadows (`nuke-compositing-artistic-basics-48-shadows.md`)
- Part 5/8: Reflections and Fresnel (`nuke-compositing-artistic-basics-58---reflections-and-fresnel.md`)
- Part 6/8: Whitepoint and white balance (`nuke-compositing-artistic-basics-68-whitepoint-and-white-balance.md`)
- Part 7/8: Glows (`nuke-compositing-artistic-basics-78-glows.md`)
- Part 8/8: Camera Artifacts (`nuke-compositing-artistic-basics-88-camera-artifacts.md`)
