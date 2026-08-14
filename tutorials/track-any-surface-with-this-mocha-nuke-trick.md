---
title: Track Any Surface with This Mocha + Nuke Trick!
source: YouTube
url: https://www.youtube.com/watch?v=vgNTBxOXna0
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/track-any-surface-with-this-mocha-nuke-trick/
frame_count: 0
frame_status: pending-selection
---

# Track Any Surface with This Mocha + Nuke Trick!

**Source:** [YouTube](https://www.youtube.com/watch?v=vgNTBxOXna0)
**Author:** Compositing Academy
**Duration:** 10m36s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py track-any-surface-with-this-mocha-nuke-trick <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


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
