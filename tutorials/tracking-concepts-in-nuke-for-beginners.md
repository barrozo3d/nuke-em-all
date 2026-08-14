---
title: Tracking Concepts in Nuke for Beginners
source: YouTube
url: https://www.youtube.com/watch?v=lpyZsAoiFMc
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke / NukeX (3D camera tracking/CameraTracker require NukeX; 2D Tracker and PlanarTracker are Nuke-tier)"
version: "not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)"
tags: [tracking, camera-tracking, 3d-system, beginner]
extraction_status: complete
frames_dir: tutorials/frames/tracking-concepts-in-nuke-for-beginners/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Tracking Concepts in Nuke for Beginners

**Source:** [YouTube](https://www.youtube.com/watch?v=lpyZsAoiFMc)
**Author:** Compositing Academy
**Duration:** 15m22s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Welcome to the first lesson on 3D cameras and parallax.
[0:05] Through this lesson, we're going to learn about the difference of the different types of tracks you can do,
[0:11] and how to differentiate and how to know which one to actually use in any given scenario.
[0:16] There's a lot of different methods you can use, but we need to go over all of them and understand just a little bit of the behind-the-scenes of how they're working to know which one to use.


### Basic Tracking [0:19]
**Transcript (timestamped):**
[0:27] So if you come through this lesson, you should already know basic 2D tracking, which is just the tracker node in Nuke.
[0:32] Essentially what this node is doing is just tracking one individual point.
[0:37] So if I pause the video here, and we look at... here we go, pause the video here.
[0:47] You can see that this 2D track is just tracking this corner point.
[0:51] So it's only tracking the motion of this cube in the foreground.
[0:56] It's not tracking everything in the scene. It's not going to work for all those things.
[1:00] So what we need to understand is the concept of parallax.
[1:04] Parallax means that objects in the foreground move much more than objects that are further away if a camera is moving.
[1:11] So you can see if you look at the word parallax here, and you look at the word parallax up here,
[1:18] this one is moving much quicker across our screen than this one back there.
[1:23] Same with cubes. So stare at this cube, and stare at this cube.
[1:27] You'll see that this cube is going to go off of our computer screen much faster than the cube.
[1:33] That's much further away.
[1:35] So you can see as the camera zooms past, this one goes away, and this one is still in the middle.
[1:43] So now if we...
[1:46] So yeah, that's the concept of 2D tracking. It only tracks one point in one plane of parallax.
[1:52] The next kind of track we have is a planar track.
[1:56] And a planar track is not quite a 3D track, but it's kind of tracking one plane of parallax.
[2:03] So it's kind of tracking this entire surface here.
[2:06] And if we were to stick a texture like a brick wall or graffiti or something like that,
[2:11] we could stick it on this planar track, and it's going to stick.
[2:15] Even though the movement of the very front of this cube is a little bit different than the movement of the back.
[2:21] We're tracking that entire plane and perspective.
[2:26] So that's good to know.
[2:27] And it's also good to know that how a planar track works is it's not actually tracking four individual points.
[2:33] It's tracking the surface or the pattern of the surface that it's looking at.
[2:40] So a good surface to planar track needs a little bit of texture.
[2:45] So like maybe a brick wall or a surface that has tracking markers on it.
[2:50] So that's good to note.


### Fullon 3D Tracking [2:52]
**Transcript (timestamped):**
[2:53] And lastly we have the full-on 3D camera track.
[2:57] And the way a 3D camera track works...
[3:01] So we can see here, this is a 3D camera track.
[3:05] The way a 3D camera track works is actually not just that these are all 3D points immediately.
[3:11] The way the computer is understanding it is each one of these little individual orange dots is actually a 2D track.
[3:21] So the computer is trying to do...
[3:22] If you do an auto 3D track in Nuke, it is individually tracking all of these thousands of points of contrast.
[3:32] So from those 2D points, from our 2D video, because our video is just a flat screen.
[3:38] That's what the computer thinks.
[3:40] It doesn't understand that there's a cube back here and there's a cube up here.
[3:43] It doesn't understand these spatial differences.
[3:46] But when you throw thousands of these 2D points into a scene,
[3:50] it measures the difference between all of these points and the speed at which they're moving across your scene.
[3:56] It measures the parallax difference.
[3:59] This is essentially a very important concept for 3D tracking and to know that this is what's happening.


### triangulation [4:06]
**Transcript (timestamped):**
[4:06] So I'm going to reiterate this concept with a couple more diagrams from the top down.
[4:09] So if you look at the same scene from the top down, we can see here's our camera and there's some cubes going backwards in space.
[4:18] So if I hit play, we can see the cubes that are further away from the camera are in frame for much longer than the ones that are in the very foreground.
[4:32] So if you look here very closely, just the two cubes have numbers next to them.
[4:37] We can see that the closer cube goes off the screen faster than the one further away.
[4:42] So this is kind of the calculation that's happening behind the scenes in the camera tracker node in Nuke.
[4:49] And this is how we start to build a 3D world from a 2D video.
[4:54] So the goal of this is to build a 3D world that matches over the real world of the 2D video.
[5:00] So if you go to the next frame, so this is again the concept I just explained,
[5:04] computer only sees 2D video.
[5:06] So this orange line, it doesn't understand that this green cube is further away or these cubes are closer.
[5:13] But once we throw a lot of 2D tracking points and measure the difference,
[5:18] it starts to actually understand that these points are in 3D space and it starts to make the calculations of where they are.
[5:26] So from that 2D line, which is our video, starting to understand a 3D matrix.
[5:32] And once we have those kind of points thrown everywhere, what it starts to do is a process called triangulation.
[5:41] So triangulation is calculating the difference between those points,
[5:46] the speed at which they're moving in relation to the camera as well.
[5:51] And it's starting to build a 3D matrix or like a plane.
[5:55] Just think of the 3D space, it's like a volume.
[5:59] And it's also starting to understand the camera's movement.
[6:04] So we're solving the actual camera's movement.
[6:06] So now we have a 3D camera that matches the real world's camera that we filmed with.
[6:12] And it matches all the motion and the speed of that camera.
[6:15] So if we fade away here, camera motion solved, our 3D scene is built.
[6:21] And we see a little green lines here that represent the camera's motion over time.
[6:27] So this is very important.
[6:30] And another important concept to know is that triangulation, it's called triangulation because it requires 3 points.
[6:36] And the way mathematically this is all calculated, you don't need to know the math behind it.
[6:41] But you do need to understand that you need to have at least 3 points for a successful triangulation to happen.
[6:49] So for example, if you're trying to track a scene and get a 3D track,
[6:52] and you don't have at least 3 good points, preferably at least 6 at all times,
[6:57] you might get a little bit of an error in your 3D camera.
[7:01] And it's not going to move the same way as your real camera, which is not good
[7:05] because we're trying to stick things into the real world with the 3D track.
[7:10] And also it's good to know that it's always, yeah, so you can see here there's always at least 3 at all times being seen.
[7:21] And that's why these triangles can be drawn.
[7:25] And then this blue line is showing that all the points that weren't seen at the same time,
[7:30] so you can see these two points weren't seen at the same time, it's actually inferring the distance between them.
[7:37] So it's measuring all of these things.
[7:39] And now we have a 3D world that is measurably the same as our 2D video.
[7:45] So how to use all this stuff is the question.


### when to use [7:46]
**Transcript (timestamped):**
[7:50] Well, you need to know when to use which tool.
[7:55] And that's a problem of kind of troubleshooting and experience and looking at a scene and determining,
[8:01] you know, do I need a full 3D track for the scene or can I just do a 2D track?
[8:05] You know, a 2D track is faster, a planar track is faster.
[8:08] A 3D scene track is going to be a little bit more time consuming to get accurate.
[8:13] So you need to look at a scene and understand what do I use in this scenario.
[8:17] So I'm going to get my drawing tool here as we play the scene.
[8:21] Just going to turn off the volume of it and hit play.
[8:25] So we can see, what do we see when we're looking at the scene?
[8:28] How is this scene moving?
[8:30] We can see that the person is walking, so there's movement.
[8:34] It's not just rotation, the person is moving through the scene.
[8:37] So we know there is translation in the scene, we know there is rotation in the scene.
[8:42] So what that means, this is the first of our two kind of 3D tracks.
[8:47] And it's called a free move.
[8:50] So let me get free move.
[8:57] And this is the term used for this kind of camera motion.
[9:01] It means you have translation and rotation.
[9:05] And that essentially means that we're going to need probably a 3D track.
[9:11] Because if we look closely, we can see that this plane moves differently than these mountains.
[9:19] And it moves differently than the sky back here.
[9:22] So there's a lot of different planes of motion between all of this space.
[9:28] And so if you're going to replace this scene with, let's say a snowy scene,
[9:34] we want to make this an entire snowy scene.
[9:36] That means we need to replace this ground with some snow.
[9:41] And maybe there's some particles of snow flying through our scene.
[9:45] So that means we're walking through the particles.
[9:48] And we have our snowy caps and everything up here.
[9:52] So that's going to be a 3D track.
[9:54] However, it is good to know that it's depending on what you're doing.
[9:59] So if you look at these mountains, they all kind of move the same way.
[10:03] There's not a lot of parallax between them.
[10:05] They're all kind of sticking together and they're not moving differently
[10:09] versus the mountains compared to this ground.
[10:11] So if our goal is to actually just replace the mountains, just the mountains and not anything else,
[10:16] we could probably do a 2D track of just maybe this rock.
[10:20] And it would save you so much time.
[10:22] So you just do a 2D track of this rock and then we can take our new picture
[10:27] and stick in our new mountain in this area.
[10:29] And we don't need to worry about the whole 3D track.
[10:32] Another example is maybe, hey, maybe you just don't like the rocks in this area here.
[10:39] We don't like the rocks in this area.
[10:41] We want to replace it with something else, some different rocks.
[10:44] Well, this would be a good example of a planar track.
[10:47] We don't need to track all the mountains and the sky and everything back here.
[10:51] We just need to track this plane of parallax.
[10:55] And they're pretty much all on the same plane because it's all almost flat ground.
[10:59] So we would just do a planar track of this surface and that would be good enough for that case.
[11:06] So knowing what you need and knowing which tool to use is important.
[11:11] It's going to save you lots of time.
[11:13] So another example of a second type track.
[11:15] So we said, again, this one is a free move.
[11:18] Free move.
[11:20] You should remember this term because we're going to use this in Nuke when we start opening the camera tracker.


### nodal pan [11:27]
**Transcript (timestamped):**
[11:27] But our second one is called a nodal pan.
[11:30] So this is the second term you should remember.
[11:32] This means that the camera is only rotating from its center point.
[11:36] It could be up or down, left to right.
[11:38] It doesn't matter.
[11:39] But if you hit play, you'll see that all the objects are kind of moving at the same speed relative to each other.
[11:47] So that's very important.
[11:50] And that means you won't need to have to worry about parallax between those objects if the camera is moving only on a rotation.
[12:01] And this means there's only rotation in this video.
[12:06] So that means there's no, like the person filming this video is not walking.
[12:11] There's no movement between the objects.
[12:14] So if you look, this tree and this tree aren't moving differently.
[12:18] They're moving together.
[12:19] There's no parallax in this scene.
[12:22] So essentially what you could do is you can pretty much probably 2D track anything in the scene.
[12:28] If you want to replace this area, if you wanted to replace something on that tree, maybe just this area to detract something.
[12:36] So you could 2D track everything here because you do not need to worry about parallax difference.
[12:42] So to simplify, if you're trying to build a scene near the first time, to simplify, you could just shoot it as a nodal pan and you don't walk around and it's going to be much easier to composite.
[12:53] However, the camera moves are a bit less interesting.
[12:57] Alternatively, so there's a problem with the 2D track.
[13:02] We're just doing a 2D track.
[13:03] Maybe you want to replace the sky in the scene, which we're going to do probably with this shot.
[13:07] If we just track this point up here, or maybe we just 2D track something over here, it would work for the overall motion.
[13:14] However, these points are going off the screen at some point.
[13:18] So there's not a lot of good points here that are on the screen the entire time.
[13:23] So we can see this point goes off the screen.
[13:26] This point's going off.
[13:28] All these points are falling off the screen at some point.
[13:33] So what you can do is do a nodal pan 3D track.
[13:38] And what this does is it's just like a 2D track on steroids.
[13:42] So all it's doing is tracking a ton of little points everywhere and it's analyzing that 2D motion.
[13:49] So it's tracking points everywhere and we're getting a 3D camera for this nodal pan.
[13:56] So now we can easily replace the sky because we have a track of all the objects in the scene.
[14:04] So that's good to know the difference between the nodal pan and a 3D track.
[14:10] They're both a 3D track, but one has movement and parallax.
[14:14] So it's more complicated.
[14:16] Whereas this is mostly just a 2D.
[14:18] Everything's moving relatively the same to each other.
[14:22] And the last example here, we have some cars in the mountain back there.
[14:27] And this actually has some parallax, but in Y, in the Y axis.
[14:31] So the camera's moving up, which is the Y axis.
[14:34] And if we look here, so we can see that if we look at the blue car and look at the mountains,
[14:39] the blue car is moving off your video frame much faster.
[14:43] So if you're going to do something that you want to replace this entire landscape,
[14:47] again, you're going to need to do a 3D track to do stuff like that.
[14:50] If you're just going to replace something on the back mountain,
[14:53] maybe you could get away with just 2D tracking that mountain.
[14:56] Or maybe there's not even a good point on that mountain.
[14:58] So you could just planar track this part of the mountain here.
[15:03] So that's all good things to know.
[15:06] So that's the difference between the main tracks here and just a bit of background knowledge.
[15:20] Thank you.



---

## Captured Frames

- [0:47] tutorials/frames/tracking-concepts-in-nuke-for-beginners/frame_000.jpg
- [2:03] tutorials/frames/tracking-concepts-in-nuke-for-beginners/frame_001.jpg
- [3:05] tutorials/frames/tracking-concepts-in-nuke-for-beginners/frame_002.jpg
- [4:32] tutorials/frames/tracking-concepts-in-nuke-for-beginners/frame_003.jpg
- [6:21] tutorials/frames/tracking-concepts-in-nuke-for-beginners/frame_004.jpg
- [7:15] tutorials/frames/tracking-concepts-in-nuke-for-beginners/frame_005.jpg
- [9:57] tutorials/frames/tracking-concepts-in-nuke-for-beginners/frame_006.jpg
- [12:15] tutorials/frames/tracking-concepts-in-nuke-for-beginners/frame_007.jpg

---

## Structured Notes

### Core Technique
A conceptual (no node-build) primer on the three tracking methods available in Nuke — 2D point tracking, planar tracking, and full 3D camera tracking — explained through the underlying concept of parallax and triangulation, plus a decision framework (free-move vs. nodal-pan camera motion) for picking the fastest adequate tracking method for a given shot rather than defaulting to a full 3D track.

### Summary
Explained entirely through animated diagrams (cubes/parallax word demo, top-down scene views, a live "Triangulation & Camera Solve" point graph) rather than a live Nuke build. Establishes parallax as the foundation concept: closer objects appear to move faster across frame than distant objects as a camera moves, and this differential motion is what any tracker measures. 2D tracking (the `Tracker` node) follows a single point in one plane and doesn't account for other planes of parallax. Planar tracking follows an entire textured surface/pattern (needs some surface detail like a brick wall or applied tracking markers) as one plane — good for sticking a flat texture onto a surface even if its near/far edges technically move at slightly different speeds. Full 3D camera tracking works by running thousands of individual 2D point trackers simultaneously across frame, then measuring the relative parallax differences between all of them to infer depth and solve both a 3D point cloud and the camera's own 3D motion — a process called triangulation, which mathematically requires a minimum of 3 simultaneously-tracked points at any given frame (6+ recommended) to solve reliably; points not visible at the same time have their relative distance inferred rather than directly measured. The video then teaches a decision framework for picking the right/fastest tool: a "free move" camera (has both translation and rotation, e.g. a person walking with a camera) generally requires a full 3D track if elements at different depths need separate treatment — but if only one flat, single-parallax-plane region needs replacing (e.g. only the mountains, which move together with little internal parallax), a much faster 2D or planar track of just that region is sufficient, skipping the full 3D solve entirely. A "nodal pan" camera (rotation only around a fixed center point, no translation) has effectively zero parallax between objects at different depths, meaning ordinary 2D tracking usually suffices everywhere in frame — except when points need to persist beyond the frame edges (e.g. replacing a sky where tracked points eventually leave frame), in which case a "nodal pan 3D track" (essentially many simultaneous 2D trackers solved into a 3D camera, without needing real parallax data) is used instead, purely to keep persistent off-screen point data rather than to resolve depth.

### Key Steps
1. Recognize parallax as the core concept underlying every tracking method: nearer objects move faster across frame than farther objects when a camera moves, and trackers measure this differential motion.
2. Use a 2D `Tracker` when only a single point/plane of motion needs to be followed and there's no need to account for other parallax planes in the scene.
3. Use a planar tracker when an entire flat, textured surface needs a texture/element stuck to it (e.g. replacing signage or wall texture) — requires the surface to have enough visual texture/pattern (brick, graffiti, applied tracking markers) for the algorithm to lock onto.
4. Use a full 3D camera track (`CameraTracker`) when multiple depths/planes of parallax in the scene need to be resolved together, understanding internally that it works by running thousands of 2D point trackers and triangulating their relative motion into a 3D point cloud + solved camera.
5. Ensure at least 3 (ideally 6+) simultaneously-tracked points are visible at all times for a reliable triangulation solve — fewer good points risks an inaccurate camera solve that won't match the real camera's motion, breaking the illusion of inserted 3D elements sticking to the plate.
6. Before tracking, classify the shot's camera motion: "free move" (translation + rotation present, e.g. camera physically moving through the scene) generally implies real parallax between depth planes and likely needs a full 3D track if multiple depths must be treated independently.
7. Even on a free-move shot, check whether the actual task only touches one low-parallax region (e.g. replacing just a background mountain range that moves together as one plane) — if so, a much cheaper 2D or planar track of just that region can replace a full 3D solve.
8. Classify a "nodal pan" shot (camera rotating only around a fixed point, no translation) as having effectively no parallax between objects at different depths — ordinary 2D tracking of points anywhere in frame is typically sufficient for the whole scene.
9. On a nodal pan shot, fall back to a "nodal pan 3D track" specifically when a 2D-tracked point would otherwise leave frame before the task is done (e.g. sky replacement) — this uses the 3D camera tracker's many-simultaneous-2D-point approach purely to maintain persistent tracking data beyond the visible frame, not because real depth/parallax needs solving.

### Nodes / Tools / Settings
- `Tracker` — Nuke's 2D point tracking node; tracks a single point/plane of motion.
- Planar tracker (e.g. `PlanarTracker`) — tracks an entire flat, textured surface as one plane rather than individual points.
- `CameraTracker` — NukeX's 3D camera-tracking node; internally runs many simultaneous 2D point trackers and triangulates them into a solved 3D camera + point cloud.
- Camera motion vocabulary used as Nuke terminology when configuring CameraTracker: "free move" (translation + rotation) vs. "nodal pan" (rotation-only around a fixed center).

### Difficulty
Beginner — explicitly framed as the first lesson on 3D cameras/parallax in the presenter's tracking curriculum; conceptual grounding before hands-on node work.

### Foundry App & Version
Nuke / NukeX — 3D camera tracking (`CameraTracker`) is a NukeX-tier feature; 2D `Tracker` and planar tracking are available in base Nuke. Version not stated on screen or in narration. 2020 upload, predates this skill's release-notes backfill (starts at Nuke 13.0/March 2021), so treat as Nuke ~12.x era rather than a specific point release.

### Tags
tracking, camera-tracking, 3d-system, beginner

---

## Related Tutorials
- Why your VFX Tracks aren't "Sticking" (and how to Fix it) (`why-your-vfx-tracks-arent-sticking-and-how-to-fix-it.md`) — shares `tracking`, `camera-tracking`; that video's troubleshooting builds directly on this one's triangulation/point-count fundamentals.
- Rotoscoping in Nuke Tutorial | 5 Beginner Tips (`rotoscoping-in-nuke-tutorial-5-beginner-tips.md`) — shares `tracking`, `camera-tracking`, `beginner`; that video's stabilize-before-roto technique depends on the same 2D-tracking fundamentals taught here.
- Ray Render in Nuke Tutorial | Compositing 3d Reflections (`ray-render-in-nuke-tutorial-compositing-3d-reflections.md`) — shares `3d-system`, `camera-tracking`; that video's proxy-geometry projection setup assumes the solved 3D camera track this video explains the mechanics of.
- Re-lighting Real Footage | Nuke Compositing [Advanced] (`re-lighting-real-footage-nuke-compositing-advanced.md`) — shares `3d-system`, `camera-tracking`; same relationship — depends on a solved 3D track this video explains from first principles.
- Nuke Compositing Technique | Card3D + PixelsToPos [Beginners] (`nuke-compositing-technique-card3d-pixelstopos-beginners.md`) — shares `camera-tracking`, `3d-system`, `beginner`; applies `PointsTo3D` triangulation (referencing this video's explanation of the concept) to anchor a Card3D-based correction/element to a tracked scene.
