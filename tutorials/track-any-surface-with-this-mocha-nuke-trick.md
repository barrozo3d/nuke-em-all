---
title: Track Any Surface with This Mocha + Nuke Trick!
source: YouTube
url: https://www.youtube.com/watch?v=vgNTBxOXna0
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke / NukeX, cross-platform with Mocha Pro (third-party planar tracker, sold separately/bundled by Boris FX — not a Foundry product but ships a Nuke corner-pin exporter)"
version: "Nuke 15.x (2024 upload; no other version-specific features referenced)"
tags: [tracking, camera-tracking, roto, grading, compositing, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/track-any-surface-with-this-mocha-nuke-trick/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Track Any Surface with This Mocha + Nuke Trick!

**Source:** [YouTube](https://www.youtube.com/watch?v=vgNTBxOXna0)
**Author:** Compositing Academy
**Duration:** 10m36s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Introduction Explanation [0:00]
**Transcript (timestamped):**
[0:00] In this shot, we're going to go through the process of doing a mocha planar track for a logo replacement.
[0:05] Whenever you're doing a clean plate, you need to make sure to have a very solid track, which allows you to stabilize and create many layers of paint for the removal.
[0:13] While initially it might look straightforward, if you look closely at this video as it plays, we can see several factors that affect the track.
[0:19] Here we have three big factors. One is luminous changes from the shadows and reflections, we have occlusions from the object passing over, and we have a perspective shift that's non-planar.
[0:29] So we're going to show how to track the surface in mocha. So we're going to hop into nuke here.


### Nuke Planar Track Problem [0:31]
**Transcript (timestamped):**
[0:33] We're actually not going to use the nuke planar track in this specific scenario because it wasn't doing that great of a job.
[0:38] So this is when you need to hop into mocha, which has a more robust planar tracker.
[0:42] But just for people who are just using nuke, there is a little setting that can make these types of tracks a little bit easier sometimes.
[0:49] And if you double click the roto node and you go into tracking, there's a little button here that says adjust for luminance changes.
[0:55] And this can help on these sort of shots where the lighting is changing across the surface.
[0:59] But nuke was actually having a hard time with it even after a frequency separation, which is actually what we're going to do to help out mocha.
[1:06] So mocha was sliding a slight bit as well. So this technique of using frequency separation is a way to sort of reduce the amount of light changes that's happening and track the texture of the surface, which is exactly what we're trying to do.


### Frequency Separation for Tracking [1:09]
**Transcript (timestamped):**
[1:18] So if you haven't seen my video on frequency separation, make sure to check that out.
[1:22] It explains this whole concept of what it actually is that we're doing here.
[1:25] But the note setup is pretty simple. We basically just take a blur, we blur our picture and we subtract it from the original.
[1:31] What this gives us is this result that looks a little strange, but we can see the pattern is a little bit more obvious now.
[1:38] It's not changing as much. So if we're tracking the top of this leaf, for example, the part that's not being occluded by much, we can track a little bit further down as well before the jacket crosses over.
[1:47] So the jacket occlusion, again, was the other problem we had. So we're going to track a little bit of the leaf because it has a very distinct pattern and also maybe a little bit lower.
[1:56] Now we're not going to track all the way over here because the logo that I was putting actually doesn't actually really extend to this position.
[2:02] So the non-planar warping problem we have is not going to be an issue with the tracking.
[2:07] We're really just going to track the portion that's actually a planar surface or mostly planar surface, which is facing towards us.
[2:14] So we do this blur minus and we grade it up.
[2:17] And the other thing I did just to help it out was there's a little bit of a reflection in here or maybe that's the edge of the shadow that we're seeing in the frequency separation.
[2:25] So I just took a roto and set it to RGBA and so we're creating a black roto and I'm just erasing that little thing that's kind of around the leaf because I don't want that to mess up our track.
[2:35] So sometimes just doing these little manual pre-setups before you start doing tracking can help just so you don't grab areas and throw off the track.
[2:44] So after that I basically shuffled it in a solid alpha and then we're going to set it over to Mocha.
[2:49] So if you haven't used Mocha before, there's actually a free trial so you can click that in the description below if you want to check out Mocha.


### Mocha Planar Tracking [2:50]
**Transcript (timestamped):**
[2:55] It's a really simple software but every compositor at some point is going to have to pull out Mocha.
[3:00] It's just almost a necessary sort of secondary skill set.
[3:03] At some point you're going to have a track that you can't get just using Nuke's tools and Mocha has really good tool set for that.
[3:10] So if you double click this here we can launch the Mocha UI and it will pull in this plate and everything we've done to it into their interface.
[3:17] So once we hop into Mocha, this is what the interface looks like if you haven't used it before.
[3:21] It's a super simple software for the majority of what you need it for which is just getting a good planar track.
[3:26] So we're going to go through it really quick and not have to go through every single button but really just what you need to use this software.
[3:33] So we're going to go here and click the little spline layer tool and we're going to zoom in and select our patterns.
[3:40] I'm going to select around the leaf and a little bit down around the logo as well.
[3:44] So we can track some of that information and it might be useful to keep the scale.
[3:48] And then I can right click to end that selection and we can also hit the little perspective.
[3:53] So these are the things that's going to track here. Sometimes it helps to hit perspective.
[3:56] If you hit mesh, this is actually for a different type of tracking where you can do warping tracks and things like that.
[4:03] But we're not doing that here. Really we just need this mostly planar surface is what we're going to stabilize.
[4:09] So we also want to get rid of the occlusion.
[4:12] So if we do another spline layer, so we click this little thing again, we're going to select around the jacket and then just right click when you're done.
[4:20] And turn off this little process wheel here so we can turn that off.
[4:25] And I'll just quickly roto the jacket before we track anything because we want to say that we're not tracking any of this jacket or the occlusions because this is going to pass over our other shape.
[4:35] So any layer that's above the base layer that you're tracking will actually subtract from that tracking information.
[4:42] So I'll just go forward in time, find it where it crosses and then just move these points and it will automatically create a keyframe and then I can just continue forward again, move it again.
[4:53] And again, the other shapes not tracking yet because again, we haven't we haven't started the track.
[4:58] So we go all the way through and we just get all the points where we have occlusions.
[5:03] Go back to the very beginning and there we go.
[5:06] So let's click this guy go back to where I put the original keyframe so I can see on this little green marker here and then we'll just hit track forward and this is going to do a really solid job of getting this track and you see as the occlusion goes over it's not breaking it's not sliding everywhere.
[5:22] It's really stuck to the leaf that we're trying to track and go back here and also track backwards.
[5:27] So we'll just say track backwards so we can go all the way to the start of the frame range and now we have a solid track all the way through.
[5:33] Now, if you click this little grid thing, it's kind of like how it works in new can you see the grid of where the perspective and everything that we're seeing so we can see it's tracking.
[5:42] But I like to work with planner tracks that are essentially all the way to the edge of the frame and if you're not familiar with that workflow I'd really check out the beginner series where we do a bunch of planner tracks.
[5:53] You'll already know about these concepts.
[5:55] So if you're a complete beginner highly recommend that if you're trying to learn new can end these core concepts.
[6:00] But if you already know that you know what we're doing so we're going to hit this little button here that says we're going to expand the planar surface to the edge of the frame so this is really important when you want to export it back to nuke.


### Exporting Mocha Tracks [6:02]
**Transcript (timestamped):**
[6:10] We don't want to have we're not trying to shrink an image down to this we're trying to stabilize the frame and do paint on the frame so we hit this button here.
[6:18] What it actually does is we can also hit this button so show the planar surface.
[6:22] It puts the corners to the edge of the frame of the video and that's going to help us stabilize this thing.
[6:28] It looks kind of crazy and weird when we play through but once we stabilize it you'll see exactly what we're doing here so you just got to hit that button and then you're basically done with mocha that's it so it's really simple and then you just go to export track and we want to find nuke corner pin dot N K.
[6:44] We say copy to clipboard and we can copy it and now we'll hop back to Nuke and just paste into the node graph and you'll have your your mocha corner pin.
[6:53] The next thing we do is we paste it in and we have our node and we can plug it into our footage to check what happens so it's going to look crazy at first and that's fine but we want to do is hit invert so we're inverting the motion and essentially removing the motion from the area that we tracked.


### Nuke Importing Mocha Track [7:00]
**Transcript (timestamped):**
[7:07] So if we look at this and we hit play.
[7:10] Everything everywhere else around the frame is going to rotate like crazy and going to look bit strange but if we look into the area that we're actually tracking this is pretty solid now it's not 100% perfect there might be some small jitter and again because this bucket is actually not a perfectly flat surface.


### Checking Track Quality [7:20]
**Transcript (timestamped):**
[7:24] So this is where we're going to employ more advanced techniques.
[7:27] We're going to use things like grid warping I transforms etc to essentially match the motion but a good way to check the stabilized motion is to just draw a grid over your footage.
[7:37] This is just a technique I like to do because you can your eyes kind of understand what's going on a little bit better take the number increase it.
[7:44] And maybe we want to shrink it down so we could not decrease the line size but what we could do is hit replace so we have our grid by itself.
[7:53] We could transform it and we could just scale that down maybe merge it over the top like this and then we'll just move that into place like this.
[8:04] And then we have a little bit of a better idea because we can see in relation to the squares that it's in how how close is our track and this is very very close there's like a very slight amount of warping on the edges here.
[8:16] There's a little bit of motion blur and things like that but that's that's all good we can add that so for the center part here it's pretty solid it's really just on the edge if you wanted to extend the logo all the way here that's where you do a grid warp to match this.
[8:28] Now there are other techniques you could use you can use keen tools geotracker if you wanted to track the cylinder as if it was a cylinder instead of a planar surface but you know this is also a viable solution so whichever technique works but this technique is actually very strong for any type of surface.
[8:45] Sometimes you have non perfect sort of planar rotations and that's a very common thing with paint work is kind of manually fixing them with with various warping techniques.
[8:56] So now that we have this you can essentially apply all of your paint as if you were just removing this object so what you could do is you could take a color we'll just do a very basic example here she will just do a solid color just to show it.
[9:08] So what we'll just grab a solid color and I'll just paint a little bit here.
[9:12] And I'm going to merge this as a separate layer just so we have an idea so I'm going to switch this to all frames the paint exists forever.
[9:19] I'm going to hit replace and then I'm just going to merge this over the top of this guy just so we can get a little quick preview here.
[9:25] So we have this over this and we'll just hit play and now it becomes a little bit more obvious where the advanced paint is going to come in here because we can see all of the light changes that are actually happening you know I sampled the perfect color of that blue but you can see the extent of which the shades and the gradients are changing on the surface and this is where paint work can be sort of a gotcha where you're like hey it's just a white bucket looks pretty simple.
[9:48] But then you look closer and you see that there are double shadows there are all these things are reflections there's parallax in this highlight.
[9:55] And so these are where you get into more advanced techniques for actual paint work so that's about it for the tracking portion of this tutorial hopefully that's helpful for you guys to get tracking these type of surfaces.
[10:07] If you're interested in actually doing the paint work for the shot and actually having the footage this is going to be included in the beginner series as another bonus project so I continue to add more bonus projects to that series.


### Bonus Material [10:10]
**Transcript (timestamped):**
[10:17] So anyone who's already enrolled you'll continue to get upgrades and extra shots like this to practice on so we're going to go through the entire paint process of how to layer this together and there are dozens of layers and techniques we can use there that will really help you guys out.
[10:32] And that's about it for the tutorial so thanks so much guys and that's about it.



---

## Captured Frames

- [0:19] tutorials/frames/track-any-surface-with-this-mocha-nuke-trick/frame_000.jpg
- [1:31] tutorials/frames/track-any-surface-with-this-mocha-nuke-trick/frame_001.jpg
- [3:40] tutorials/frames/track-any-surface-with-this-mocha-nuke-trick/frame_002.jpg
- [5:06] tutorials/frames/track-any-surface-with-this-mocha-nuke-trick/frame_003.jpg
- [6:22] tutorials/frames/track-any-surface-with-this-mocha-nuke-trick/frame_004.jpg
- [7:10] tutorials/frames/track-any-surface-with-this-mocha-nuke-trick/frame_005.jpg
- [8:04] tutorials/frames/track-any-surface-with-this-mocha-nuke-trick/frame_006.jpg
- [9:19] tutorials/frames/track-any-surface-with-this-mocha-nuke-trick/frame_007.jpg

---

## Structured Notes

### Core Technique
Getting a rock-solid planar track for a difficult logo-removal/clean-plate shot (uneven lighting, an object occluding the surface, a non-planar edge) by pre-conditioning the footage with frequency separation before handing it to Mocha's planar tracker, then round-tripping the result back into Nuke as a `CornerPin` to stabilize the surface for paint work.

### Summary
The shot has three named problems working against a track: luminance changes (shadows/reflections crossing the surface), occlusion (an object/jacket passing in front), and a non-planar perspective shift at the surface's edge (frame_000 shows the source footage with the tracked leaf-patterned bucket and jacket occlusion). Nuke's own planar `Tracker`/`Roto` node (with its "adjust for luminance changes" option) was tried first but couldn't hold — even after adding frequency separation to help it — so the workflow moves to **Mocha** (third-party, Boris FX; free trial available), described as a near-mandatory secondary skill every compositor eventually needs since Mocha's planar tracker outperforms Nuke's built-in one on hard surfaces. Before tracking, **frequency separation** is used purely as a tracking aid, not a beauty pass: `Blur` the plate, subtract the blur from the original (frame_001/002 show the resulting high-frequency-only "Freq Separation" result — a spiky, contrasty edge-pattern render that isolates surface texture from the lighting/shadow changes riding on top of it), then `Grade` it up for contrast — this gives Mocha a texture pattern to lock onto that barely changes even as real-world lighting shifts across the surface. A small manual `Roto` (set to output RGBA, painted black) removes a stray reflection/shadow-edge artifact the frequency-separation pass introduced near the tracked leaf, specifically so it doesn't distract the tracker; the cleaned result is shuffled into a solid alpha before export to Mocha. **In Mocha:** draw a spline-layer selection around the trackable pattern (the leaf plus a bit of the logo area — frame_003/004 shows this selection over the frequency-separated footage), enable "Perspective" tracking (not "Mesh," which is for warping/deforming tracks, not needed here since the surface is treated as mostly planar); draw a *second* spline layer around the occluding object (the jacket) with tracking disabled, and manually keyframe that shape frame-by-frame as it crosses — any layer stacked above the base tracked layer subtracts from that layer's tracking data, so this occlusion shape must exist (even un-tracked) before running Track Forward/Track Backward on the base layer (frame_005 shows the tracked jacket-occlusion shape mid-track). Once tracked cleanly through the whole occlusion pass, click "expand planar surface to the edge of frame" (critical — the goal is stabilizing the full frame for paint, not cropping to the tracked patch) and "show the planar surface," then Export Track → Nuke CornerPin.nk → Copy to Clipboard, and paste directly into Nuke's node graph as a ready-made `CornerPin` node. Plugging it into the footage and checking **Invert** removes the tracked motion from that region (frame_006/007 show the plate mostly stabilized to a green-square reference with the surrounding background swinging wildly, as expected — everything *outside* the tracked/inverted region distorts, which is normal). **Verifying track quality:** overlay a `Grid` node (increase line count, shrink/scale it, `Merge` over the stabilized footage) as a visual reference — small warps or motion blur near the edges of the tracked area are expected and acceptable; if the surface isn't perfectly planar (e.g. a curved bucket), residual edge drift is fixed downstream with `GridWarp`/`IDistort`-family 2D correction, or by switching to a true cylindrical/geometric tracker like KeenTools GeoTracker if the extra accuracy is worth the setup cost — the author frames the Mocha-planar approach as "viable and strong for any type of surface" regardless. Finally, a quick paint preview (a flat sampled-color solid merged over the stabilized plate, set to persist across all frames) demonstrates why real paint work on this kind of surface is deceptively hard — even a "simple white bucket" turns out to have double shadows, reflections, and highlight parallax once you actually study the stabilized footage closely (frame_007), which the video frames as the reason this is only the tracking half of a larger paint-removal project (continued in the author's paid course).

### Key Steps
1. Identify the specific factors working against the track before choosing a tool: luminance/shadow changes across the surface, occluding objects passing over it, and any non-planar perspective shift.
2. Try Nuke's native planar `Tracker`/`Roto` first, including its "adjust for luminance changes" option; if it still slides, move to Mocha rather than fighting Nuke's tracker further.
3. Pre-condition the plate with frequency separation specifically as a tracking aid: `Blur` the image, subtract the blur from the original, `Grade` up the result — isolates stable surface texture from the lighting variation riding on top of it, giving the tracker a more consistent pattern to lock onto.
4. Manually clean up any stray artifacts the frequency-separation pass introduces (reflections, shadow edges) with a quick black `Roto` (RGBA output) before tracking, so the tracker doesn't grab distracting regions.
5. Export the cleaned plate to Mocha (double-click the Nuke node that launches the Mocha UI, or open it directly).
6. In Mocha: draw a spline-layer selection around the actual trackable, mostly-planar pattern; enable Perspective tracking (Mesh is for warping/deforming tracks — not needed for a planar surface).
7. Draw a second spline layer around any occluding object, leave tracking off, and manually keyframe it frame-by-frame across the occlusion — any layer above the tracked base layer subtracts from that layer's track data, so the occlusion shape must exist before tracking the base layer.
8. Set a starting keyframe on the base layer, Track Forward, then Track Backward to cover the full frame range.
9. Use Mocha's grid overlay to visually confirm the track is holding through the occlusion without sliding.
10. Click "expand planar surface to the edge of frame" and "show the planar surface" — critical for exporting a stabilization track meant to cover the whole frame for paint work, not a cropped patch.
11. Export Track → Nuke CornerPin.nk → Copy to Clipboard; paste directly into Nuke's node graph as a ready CornerPin node; plug it into the footage and enable Invert to stabilize the tracked region (everything else in frame will appear to swing/distort — expected).
12. Verify track quality visually: overlay a scaled-down `Grid` merged over the stabilized footage and check how well it holds relative to the grid lines; minor edge warping/motion blur is normal.
13. For any remaining edge drift from a non-perfectly-planar surface, correct downstream with `GridWarp`/2D distortion nodes, or consider a dedicated geometric tracker (e.g. KeenTools GeoTracker for a cylindrical surface) if warranted.
14. Preview paint feasibility with a flat sampled-color solid merged over the stabilized plate (set to persist all frames) — reveals real-world shading complexity (double shadows, reflections, highlight parallax) that a flat "just paint it out" assumption would miss.

### Nodes / Tools / Settings
- **Core Nuke/NukeX:** native planar `Tracker`/`Roto` ("adjust for luminance changes" option), `Blur` + subtract (frequency separation setup), `Grade`, `Roto` (RGBA output for cleanup mattes), `Shuffle` (solid alpha), `CornerPin` (Mocha-exported, Invert toggle), `Grid` node (track-quality visual check), `GridWarp`/`IDistort`-family nodes (residual edge-drift correction)
- **Mocha Pro (third-party, Boris FX):** spline-layer tool, Perspective vs. Mesh tracking modes, per-layer track-subtraction stacking behavior (occlusion layers above the base layer remove their region from the base track), Track Forward/Backward, "expand planar surface to edge of frame," "show planar surface," Export Track → Nuke CornerPin.nk
- **Alternative mentioned for non-planar surfaces:** KeenTools GeoTracker (true cylindrical/geometric tracking instead of a planar approximation)
- **Cross-referenced techniques:** frequency separation (author's own dedicated tutorial), planar-track workflow fundamentals (author's paid beginner series)

### Difficulty
Intermediate — requires comfort with planar tracking concepts and a willingness to leave Nuke's native toolset for Mocha when needed; the frequency-separation pre-conditioning trick and the occlusion-layer-subtracts-from-base-track behavior in Mocha are the two "aha" details most likely to be new even to viewers who already know basic tracking.

### Foundry App & Version
Nuke / NukeX, cross-platform with Mocha Pro (Boris FX, not a Foundry product, but ships a native Nuke CornerPin exporter). Nuke version not stated on screen; per this skill's version-tracker, a 2024 upload falls in the Nuke 15.x window (15.0 Oct 2023 → 15.1 Jun 2024 → 15.2 Feb 2025). No version-specific Nuke features referenced.

### Tags
tracking, camera-tracking, roto, grading, compositing, intermediate

---

## Related Tutorials
- Rotoscoping in Nuke Tutorial | 5 Beginner Tips (`rotoscoping-in-nuke-tutorial-5-beginner-tips.md`) and Why your VFX Tracks aren't "Sticking" (`why-your-vfx-tracks-arent-sticking-and-how-to-fix-it.md`) — share `tracking`, `camera-tracking`; both are about getting a track to hold reliably, at different points on the beginner→troubleshooting spectrum from this video's Mocha-specific hard-case workflow.
- [2/3] Nuke Tutorial Series (CRACKS, Keentools, Smartvectors) (`23-nuke-tutorial-series-cracks-keentools-smartvectors.md`) — shares the theme of picking the right third-party/specialized tracker (there: KeenTools FaceTracker for 3D face geometry; here: Mocha for planar surfaces) when Nuke's native tools fall short.
