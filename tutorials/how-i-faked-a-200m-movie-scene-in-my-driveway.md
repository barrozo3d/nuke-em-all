---
title: How I Faked a $200M Movie Scene (In my DRIVEWAY!)
source: YouTube
url: https://www.youtube.com/watch?v=dbkOqzRvWKY
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-i-faked-a-200m-movie-scene-in-my-driveway/
frame_count: 0
frame_status: pending-selection
---

# How I Faked a $200M Movie Scene (In my DRIVEWAY!)

**Source:** [YouTube](https://www.youtube.com/watch?v=dbkOqzRvWKY)
**Author:** Compositing Academy
**Duration:** 6m2s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py how-i-faked-a-200m-movie-scene-in-my-driveway <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, in this video I'm going to be pulling back the curtain on how I created this medieval,
[0:03] Templar cinematic that looks like it belongs in the movie, but really was just shot in a snowy driveway.
[0:08] Many people think that the secret to achieving blockbuster visuals is just unlimited resources.
[0:13] Now don't get me wrong, big studios are known for throwing money at their problems,
[0:16] but how can independent filmmakers achieve the same results?
[0:20] I'm going to show you my approach to how I planned, filmed, and composited this VFX set extension together.
[0:25] Watch to the end if you want to see the full sequence.
[0:28] So guys, I got to clear something up. On one of the last videos on this channel,
[0:31] we used a barn and a green screen to kind of do something similar.
[0:34] We were doing more cost-effective filmmaking and visual effects.
[0:37] Somebody called me out in the comments and said, hey, all I need is a gigantic barn and, you know, that's how you did it.
[0:42] And, you know, fair enough, but I really believe that if there is a will to create, there's a way to do it.
[0:47] And I want to prove it in this video. So here's the challenge.
[0:49] No green screen, no set, no big lights.
[0:52] All we're going to do is shoot in a driveway using a camera and a drone,
[0:56] as well as using Blender and Nuke paired together.
[0:59] And the most important part here is careful planning of your visual effects, which can help reduce your cost.
[1:04] Hopefully this goes well.
[1:06] So since we're doing a Templar sequence, before we even think about visual effects, I need to get some armor.


### Getting the Costume [1:10]
**Transcript (timestamped):**
[1:11] Now that means I need to find a blacksmith.
[1:13] Music
[1:19] You got the box. Let's do it. Let's see what we got.
[1:23] Music
[1:27] See if it... Oh, shit.
[1:29] Music
[1:32] So if you notice what's good about this, well, first of all, it's heavy. This is like a real metal.
[1:37] But it's also not a perfect mirror.
[1:40] So we're not going to have all the reflections of the environment that we're replacing.
[1:42] So this is totally going to work.
[1:44] Music
[1:46] So we've got the biggest piece, which is the helmet, but we need to go to the fabric store to get the cape.
[1:50] And this is not my specialty. My wife actually specializes in fashion design.
[1:54] So she's going to help me out here.
[1:56] Now, one thing we've learned about finding fabric is you can't cheap out on this part.
[2:00] If you try to cheap out on the fabric, you'll be able to tell that the thickness and the weight
[2:04] and the way the fabric drapes is not high quality.
[2:08] In addition, higher quality fabrics reflect the light differently,
[2:11] which is going to be apparent in the final filmed composite.
[2:15] So while she's going and starting out the costume, I'm going to start the CG build.
[2:19] First, I'm going to start my CG build with some simple props, basic models like columns and background architecture


### CG Build [2:20]
**Transcript (timestamped):**
[2:25] with some kid bashing and layout can build the composition.
[2:28] Keep it simple, but effective.
[2:29] I need to maintain cost constraints, which means simple textures, repeated objects and controlled lighting.
[2:35] One key theme to remember here is we don't need infinite complexity to make a high budget looking shot.
[2:40] Even in movies like Dune, some of the most cinematic shots are created in scenes that are essentially


### Artistic Principles [2:42]
**Transcript (timestamped):**
[2:44] concrete blocks or simple forms.
[2:46] The difference is the director as well as the VFX team and cinematographers know how to control
[2:51] level of detail as well as using camera angles and lighting to their advantage.
[2:55] As I started building out the CG scene, I was keeping a very specific aesthetic in mind.
[3:00] But one scene that's always stuck in my head was a scene from Star Wars The Last Jedi,
[3:04] the scene with the white planet and the red dirt underneath.
[3:06] Another scene with a similar color palette was this scene from Star Trek, where the color
[3:10] palette was these red, white and a little bit of yellow.
[3:13] So with these colors in mind, it went with red, white, black and an accent of gold.
[3:18] Operating as an independent filmmaker here, I know one thing that's really going to help is previs.


### Previs [3:20]
**Transcript (timestamped):**
[3:22] If I plan my camera angles beforehand against the CG environment, I'll know where to place myself when I film.
[3:28] This is going to be especially useful for the drone shot, which needs to be precisely measured.
[3:32] Here I'm using measurements to know where to place the drone when I film.
[3:35] I also know the focal length of the real lenses I'm shooting with and the drone, so I can plug this data directly into the blender cameras when I'm preparing.
[3:42] So before we go out to film, I want to remind you of the premise of this video.
[3:45] How can we control costs?
[3:47] The drone shot, if we actually shoot it at the right angle, we can reduce the cost and not have to do any rotoscoping at all.
[3:53] Essentially from the drone, we project a rectangle rotor shape down onto the ground of the snow.
[3:58] What we're trying to do is cut out the walking actor and keep the surrounding real ground that we can blend into the CG environment.
[4:04] If the drone was just a few meters lower and the person's silhouette breaks the horizon, now you have to get into rotoscoping, which increases your cost.
[4:12] So this is where if you're directing your own visual effect shots, you can control costs and still get the same effect.
[4:17] The final touches on our CG, we need to add a bit of motion to the scene.
[4:20] So I'm going to use flags, snow particles, a bit of subtle animation on the background characters,
[4:26] and the rest will come from the real filmed plate of the actress.


### Filming [4:30]
**Transcript (timestamped):**
[4:33] Without a green screen, we can still film the person to extract later.
[4:36] This avoids green reflections and a windy environment.
[4:38] I threw down a few tracking markers for the drone shot placed along the walking path.
[4:48] Using the measurements from Blender, comparing against the altitude and a laser distance measurement, I shot the footage.
[4:54] I shot the handheld shots with my FX3 and a gimbal.
[4:58] Now onto the last part to bring it all together, compositing.


### Compositing [5:00]
**Transcript (timestamped):**
[5:01] Compositing is essential to making your shots look cinematic.
[5:04] Here, there are hundreds of small color corrections to direct your eye and to do 3D color grades on your CG environment.
[5:10] It can also do things like simulate lens characteristics or boost highlights on the real footage to enhance the look.
[5:16] So let's check out the final result.
[5:24] The final result is a beautiful, beautiful, and very realistic shot.
[5:31] If you're somebody who's trying to combine virtual with real or you're trying to get into visual effects studios,
[5:36] we have the most extensive Nuke course available in the description below.
[5:39] So check it out if you're interested.
[5:41] This is based on my years of experience working in the film industry.
[5:44] I'm a big fan of the camera.
[5:46] I'm going to use the camera to shoot the video.
[5:48] I'll be doing a few more videos to make sure that you guys are not going to miss any of the new videos.
[5:52] Also, check out a few of the new videos that are available in the description below.
[5:55] So check it out if you're interested.
[5:57] This is based on my years of experience working in the film industry on films like Avengers, Star Wars, Spider-Verse, and more.
[6:03] Make sure to hit thumbs up guys on the video if you want to see more videos like this.
[6:07] And thanks for checking it out.



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
