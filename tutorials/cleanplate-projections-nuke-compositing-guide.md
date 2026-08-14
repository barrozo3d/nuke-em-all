---
title: Cleanplate Projections | Nuke Compositing Guide
source: YouTube
url: https://www.youtube.com/watch?v=mEeCZFjpO8s
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/cleanplate-projections-nuke-compositing-guide/
frame_count: 0
frame_status: pending-selection
---

# Cleanplate Projections | Nuke Compositing Guide

**Source:** [YouTube](https://www.youtube.com/watch?v=mEeCZFjpO8s)
**Author:** Compositing Academy
**Duration:** 12m42s | 10 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py cleanplate-projections-nuke-compositing-guide <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Clean Plates
[0:04] Clean plates are the unseen visual effects in the visual effects world where artists paint out and remove objects,
[0:09] so you'll never see them in a film if they've been done correctly.
[0:12] There are different levels of detail for different productions, so television, episodic and films have different requirements.
[0:17] My background is working to feature films, so we'll be talking about the techniques used for this level to work professionally.
[0:21] By the end of this video, you'll be able to look at a scene and break down the steps necessary to approach a clean plate with moderate difficulty,
[0:28] as well as understanding different methods of 3D reconstruction that we can use.


### Overview [0:30]
**Transcript (timestamped):**
[0:32] So this is the scene we're going to be looking at, and we have a camera that kind of pushes in here.
[0:37] The first thing that we actually need to do is establish 3D for basically everything that is not the object that we're going to be removing.
[0:45] So we're going to be removing this object that's in the center, and also flattening the grass just a tiny bit around it.
[0:51] So we need to have 3D for the area behind and the rocks that are a bit vertical.
[0:56] The three primary techniques we can use are cards, point cloud meshes, or a lighter scan.
[1:01] So we need to have a ground plane and some kind of vertical geometry or proper 3D geometry for the rocks, and an area that's behind the rocks.
[1:10] If we do it like this instead, this would be the alternative, and this would be kind of a mistake.
[1:15] So if you project this whole image onto just a flat card, you're going to actually lose the three dimensionality of these rocks,
[1:22] and it's going to feel like you have a stretched projection.
[1:24] So beginners might make this mistake sometimes, and you'll notice in their projections they're looking stretched,
[1:29] and that's because they're not actually building out the geometry properly and layering it together.
[1:34] So using the first method, it looks like this.


### Methods of 3d [1:35]
**Transcript (timestamped):**
[1:36] We get a basic point cloud from the camera track, and then after that we just place some geometry flat and a little bit vertical where the rocks are.
[1:44] The second method is trying to achieve the same result except with the point cloud generator.
[1:48] So if you go to vertex selection, and we select the vertices like this, and then we go to groups, and we say create group,
[1:55] it will create this group here that we can click on and say bake selected group to mesh.
[2:00] And when you do that, you can get this geometry that represents across your point cloud.
[2:05] It's a little bit better for organic scenes as well, whereas cards sometimes could be better for flat surfaces.
[2:10] So this is kind of what that would look like.
[2:12] Our last method here is using a lighter scan, which is more accurate than the point cloud mesh,
[2:17] and this can be captured using an iPhone Pro, which has a lighter scanner built in,
[2:22] and we can reconstruct the 3D scene using this depth data that comes from the laser.
[2:27] So this is showing where the lighter scanner is on an iPhone, and this is me using Polycam just shooting some LiDAR and getting a capture.


### Polycam [2:29]
**Transcript (timestamped):**
[2:36] So it's really easy.
[2:37] You just basically film, and it uses the lighter scanner in the back.
[2:40] You can also use the photogrammetry mode if you don't have the scanner,
[2:43] and that will also give you a high quality model out of the application.
[2:46] So Polycam is a sponsor on this video, but I thought it would be a good fit for this channel because I've been using their software for a few years,
[2:53] and I think it's really convenient to have a lighter scanner in your pocket being able to capture large scale environments,
[2:59] either for lining 3D up or doing projections directly.
[3:03] The photogrammetry side is really good for assets as well to get detailed assets and not have to worry about the processing time or dealing with that on the computer.


### Fixing Geo [3:11]
**Transcript (timestamped):**
[3:11] Now I did use a lighter scan for this specific project, even though we could have done it with either of the methods there,
[3:18] but basically one thing you need to do is delete the object that you're trying to clean plate out because we don't want to project onto this.
[3:25] So basically what I did was bring in Blender and delete the faces, and you get a geometry that looks like this,
[3:30] but after that you can go to the vertices and just merge them all to the center.
[3:35] So you can do this in Maya as well.
[3:36] It doesn't really matter.
[3:37] You just need to basically fill the gap so that we have a solid geometry that we can project onto.
[3:42] So you can see here I just merged the vertices, and that's basically how we get a mesh that we can project onto, but not on the object that we're removing.
[3:50] So that's kind of what we got, and it doesn't matter that the texture is stretched because we're not actually using this texture that came with the lighter scan.
[3:57] So one important principle is to use what's real and use multiple projections.


### Use what's real [3:59]
**Transcript (timestamped):**
[4:02] So if I just do a very simple projection setup here with one projection, we can see something like this.
[4:08] So I go to the last frame here and I'm projecting this image.
[4:11] So just to quickly run through it, I'm just doing a frame hold here, and I am painting out on that frame.
[4:18] Now normally you would do an undistort and you would do your paint and then you would read a story at the end.
[4:24] But since we're dealing with grass and really small details and everything is in the center of the frame and it's an iPhone,
[4:30] which has low lens distortion relative to other lenses, I basically just turn them off here because the sampling is kind of making it a little bit blurry,
[4:37] which we don't have to do if there's no noticeable sliding.
[4:40] So that's just a quick thing to point out.
[4:43] But anyways, we have a frame hold, we have the paint, and we're projecting onto the lighter scan that we've taken, and this is kind of what we have.
[4:51] But the idea is with multiple projections is to use what's real from different angles.
[4:57] So from our first angle here, we see that this rock is actually covered by the object that we're trying to remove.
[5:03] But on the left side, we see this rock that's uncovered.
[5:06] So when we're painting it out, we're actually kind of having to restore the rock that's here.
[5:11] But if we actually go earlier into the video and we go backwards in time, we can actually see that rock.
[5:17] So we don't actually want to make up what's there because at the start of the video, we're kind of losing detail if we do it that way.
[5:24] So rather, what you want to do is do at least two projections, if not more, to establish as much real information as we can.
[5:32] So here we might project the left side to get to this detail and then more towards the beginning before the rock gets covered up.
[5:39] We would project another projection here.
[5:41] And basically, you just have multiple patches of projections that you layer over, just A over B after that point.
[5:48] Another technique that we need to keep in mind when doing clean plates is to dissolve your patches.


### Dissolve patches [5:52]
**Transcript (timestamped):**
[5:53] So a lot of times when you're doing projections, one projection will only work for like a certain portion of the frame,
[6:00] which means like your geometry might not be completely perfect or you might see from a slightly different angle of that geometry.
[6:07] So the projection doesn't work from every single angle.
[6:10] And that means we have to be kind of dissolving to account for those perspective changes.
[6:15] Now this can be a bit difficult to describe just through a video tutorial because you really have to see the really small details and parallax shifts that are happening in footage,
[6:22] which takes a lot of like scrubbing back and forth and looking very close.
[6:26] So the best way to actually learn this is just by practice and actually running into the problems.
[6:31] But I'll explain the example quickly here, kind of where we use this example.
[6:35] So up on this part of this precomp, if you look at this rock towards a certain frame, it starts to look a little bit flat,
[6:43] which is actually not what it looked like in the real plate.
[6:46] So if I compare to the real plate, you see the angle of this corner here.
[6:49] It's a little bit different. It's kind of being shifted.
[6:52] And so this is where we need to create multiple patches to make sure that the angle is changing with the perspective and the parallax.
[6:59] That's actually in the real geometry.
[7:01] So your geometry will never be 100% perfect, 100% lined up.
[7:04] So that's where the 2D techniques and also dissolving multiple projections comes in.
[7:10] So if we look here, if we go towards the end of the shot, what I did here is a patch.
[7:15] So if I disable it and I go to this frame and I re-enable it, you see I'm kind of correcting where our perspective started to shift
[7:22] and kind of just putting a patch over this area, which is bringing some sharpness back as well.
[7:26] Now this projection actually only works for a few frames.
[7:29] If I go backwards in time, we see that it starts to become a little bit flat again.
[7:33] And so either there's multiple ways you can correct this.
[7:36] You could use tools like an eye transform.
[7:39] So if I create eye transform node, you can get this on Wikipedia.
[7:43] If you just type in eye transform, you can use a grid warp and you can use other just 2D tricks to kind of force the perspective,
[7:51] meaning you would take this corner and just shift it over just a tiny bit so that it kind of matches with the plate.
[7:56] So if you look at the plate, we could just shove it over a tiny bit and kind of correct the angle that's not correct with the geometry and projection.
[8:04] So you would use these just before you project it.
[8:07] So just before the project 3D, you kind of correct the patch.
[8:10] The other way to do it is to use another projection.
[8:12] So what I did here was I go backwards in time where it starts to break.
[8:17] Usually with patches, you want to see like what's the last good frame that's kind of working and then go backwards in time and where it starts to break.
[8:25] Is where you're going to have to do some more work.
[8:27] So you would create a patch here and you would dissolve forward in time to create that seamless transition.
[8:34] So it's pretty difficult, but it takes practice.
[8:36] So we can look here at what I did.
[8:38] So I go to the key mix and what I did here was actually restored some of the original plate again after I've done some projections.
[8:45] So I kind of bring it back and then I frame hold that and create a new patch.
[8:50] And so this is going to work for just a few frames.
[8:53] This is like only five frames that were actually using this new patch.
[8:56] So if I look at the merge and we see what that changed by disable it and enable it, we see that we're just correcting the angle on just a few frames just to get that perspective to work.
[9:07] Another thing we want to do is to hide your tracks.


### Break up parallax [9:09]
**Transcript (timestamped):**
[9:10] So that is to say, we want to basically try to blend our patches in a way that the viewer is not going to perceive that we might be losing a slight amount of parallax through our projections.
[9:21] So for example, if we're projecting on the grass, grass is going to have like, you know, an infinite amount of parallax planes because each piece of grass technically has parallax in front of the other.
[9:33] Now, unless we plan on replacing the whole ground with CG grass and that's that could happen on a film where you just use CG grass, you know, you might have to come up with other ways to kind of fake that parallax.
[9:45] And so the two main ways of doing that in this scenario would be either to have a card that you have lots of subdivisions.
[9:52] So if you create a card, you were to increase these rows and columns to a high number and use a displacement.
[9:58] So you can use a displaced geo with like a noise pattern, like really small.
[10:03] You could do it that way and you could kind of just mess up this card a lot to kind of give it some little spikes to kind of simulate that movement of the grass over each other.
[10:12] The other way is to just blend the edges where that parallax issue might be obvious.
[10:19] And so in this case, that's kind of what I did.
[10:22] I just took a roto shape and I used a fractal blur.
[10:26] I'll attach it in the description where you can get this node.
[10:29] Essentially what it does is it just if you have a blurred alpha like this or a sharp alpha, I suppose, and you look at the alpha, it's just breaking up the edge through noise.
[10:40] So it's kind of going to make it harder to see where we place that CG patch over the real footage.
[10:46] And that's going to help us kind of blend across what we're trying to add.
[10:50] So this is kind of what I add over and I'm putting this over the shot.
[10:53] So we're kind of replacing some different things and cleaning it up.
[10:56] And we're also flattening the ground a bit because originally there was a hill here, so I kind of flattened it so there would be less of a hill.
[11:02] But I'm also just using this technique to kind of break up the edge.
[11:06] So that's something that you can keep in mind just to hide any areas that the parallax is going to change slightly.
[11:13] So the last concept we'll talk about is projecting from the maximum resolution point of view.


### Project from Max Res [11:18]
**Transcript (timestamped):**
[11:18] And all that means is to find an area that is the highest amount of pixels for what we're projecting.
[11:24] So if we're here at this sequence and we go further, if we're projecting this rock, for example, we might want to go closer to it where this is actually bigger on the screen
[11:33] because it means that there are more pixels, meaning it's higher quality.
[11:36] Especially if we were walking even further away than this, this rock is going to get really small.
[11:41] So if you project from there and then we walk really close to it, you're going to see that it's going to become blurry as we get closer and closer.
[11:47] So in general, we want to be at the closest point of view where we still can see things and that's going to be where you project.
[11:54] Now, if your perspective changes too much, that's where we go back to the technique we talked about earlier, where we do dissolves between the patches so that we don't perceive any color changes or perspective changes being stretched from a different angle.
[12:09] That's about it for this tutorial.
[12:11] So if you guys liked it, make sure to hit like and subscribe.
[12:14] And for anyone who wants the project files, these will be added to Nuke 202.
[12:18] So if you've already taken that class, you'll have this additional project added and you can play with it there.


### NK202 [12:23]
**Transcript (timestamped):**
[12:23] If you're a complete beginner looking for a full course on the 3D system in Nuke, I'd recommend checking out Nuke 202 because we cover concepts such as camera movements, parallax tracking, triangulation, camera projections, and a lot more.
[12:35] So you can go check that out on compositingacademy.com and the link is in the description.



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
