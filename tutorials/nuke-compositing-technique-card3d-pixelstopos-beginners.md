---
title: Nuke Compositing Technique | Card3D + PixelsToPos [Beginners]
source: YouTube
url: https://www.youtube.com/watch?v=w5xFpajzC8s
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/nuke-compositing-technique-card3d-pixelstopos-beginners/
frame_count: 0
frame_status: pending-selection
---

# Nuke Compositing Technique | Card3D + PixelsToPos [Beginners]

**Source:** [YouTube](https://www.youtube.com/watch?v=w5xFpajzC8s)
**Author:** Compositing Academy
**Duration:** 15m32s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py nuke-compositing-technique-card3d-pixelstopos-beginners <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to this quick beginners tutorial about the card 3D and image plane.
[0:08] So an image plane, this is just the name that someone gave it, but this is a gizmo or tool
[0:13] set available on Nukepedia that essentially utilizes the card 3D in Nuke.
[0:19] So it's using this card, but essentially what it's doing is speeding up the process of using
[0:25] this a little bit.
[0:26] So a few months ago, I made a tutorial about how to stick color corrections to CG scenes
[0:31] using ST maps and stuff like that.
[0:33] And that's a more advanced technique of doing a similar effect to what we're going to talk
[0:37] about here.
[0:38] So if you're more in the beginner range, this is going to be helpful for you.
[0:42] And this is applicable to live action footage or CG scenes.
[0:46] So you can use this technique in either one.
[0:49] But essentially what we have here is a shot I filmed in New Zealand, just kind of zooming
[0:54] in, walking here.
[0:55] And then I have a color correction that I've kind of stuck to this tree and you can see
[0:59] it kind of tracks along there.
[1:02] And yeah, that's basically what it's doing.
[1:04] And it's a very quick way to do things like this.
[1:07] And the reason this is useful is because you can stick color corrections or you can stick
[1:11] elements very quickly and populate a scene without having to go into 3D space and try
[1:17] to figure out how to get this placed here.
[1:21] So these two gizmos are available in the script.
[1:24] You can download the project file.
[1:25] It just gives you the footage and these.
[1:28] Otherwise you could just search them on Nucopedia.
[1:30] The other note we're going to talk about is called pixels to position, which is essentially


### Pixels 2 Position [1:32]
**Transcript (timestamped):**
[1:35] the same as points to 3D.
[1:37] If you guys are familiar with this, if not, that's fine because we're going to talk about
[1:42] it.
[1:43] But essentially what it does is if we have a 3D camera already tracked, it allows us
[1:47] to figure out where different things are in a scene.
[1:50] So for example, where is this tree?
[1:53] And if we want to figure out the 3D point of where this is, we can convert this 2D video
[1:59] and find 3D point.
[2:00] So that's what the story is about.
[2:02] And yeah, we'll get into it.
[2:04] So essentially very simple.
[2:06] If you take the image point note, which is provided here, and we'll grab it.
[2:13] And we'll also grab the camera from the 3D track.
[2:15] I'll just restart this area down here and start from scratch.
[2:18] So we'll paste the camera and we'll paste.
[2:22] We'll just do a roto shape for an image.
[2:25] And I'll just set it to leave it at alpha for now.
[2:28] So we're going to do this as like a color correction.


### Color Correction [2:29]
**Transcript (timestamped):**
[2:31] And essentially what we want to do is if you double click the image plane node.
[2:37] So this is again, like I said, it's a card 3D kind of wrapped up into this tool.
[2:41] And essentially what it's doing, I'll do it first and then kind of explain it.


### Set a Reference Frame [2:45]
**Transcript (timestamped):**
[2:45] But first you want to set a reference frame.
[2:47] So let's say we want to color correct the bottom of this tree.
[2:50] So we'll go to the frame that we're creating the correction on.
[2:55] And it's essentially projecting out from this frame.
[2:57] So frame 4.
[3:00] So if I just draw something here, the roto shape very quickly, draw a really basic shape.
[3:09] So that's drawn on frame 4.
[3:11] So that's our reference frame.
[3:12] So I'll make sure to set that in the tool, set that to 4.
[3:16] The distance, we don't know the distance yet.
[3:18] So I'll explain that in just a second.
[3:19] So let's just plug that in and see exactly what that's doing first.
[3:23] So plugging the mask input into the image plane, we can grade up and we see that that's
[3:28] happening.
[3:29] So if we start to play through this footage, we see that actually it starts to kind of
[3:33] stick with the scene, but it seems to not be sticking correctly to the tree entirely.
[3:40] And that's because our distance is not correct.
[3:42] So essentially what we're doing if we go into 3D space here is it's taking this card 3D.
[3:50] So if you just imagine, let's just draw it here.
[3:53] I'll just do a draw tool.
[3:56] So if you imagine that this tool creates a card, but it's to the scale of the camera
[4:01] frustum.
[4:02] So if we take and we look at this, so this basically this triangle that's coming out of
[4:07] the camera is the view of where the camera is seeing.
[4:10] And essentially it's creating a card along these corners.
[4:15] This is a bad drawing, but it'll work.
[4:18] So this is basically creating a card along these lines here.
[4:24] And the distance setting.
[4:25] So if you look in the tool, it says distance is our Z distance.
[4:29] So basically how far away whatever we want to kind of project onto is from the camera.
[4:37] So if our tree is somewhere over here, that would be our distance.
[4:40] So we need to figure out how far is that point from our camera.
[4:45] So again, so that card is going to be projected out in this triangle, always scaling to these
[4:51] points and we can even have some over scan on there.
[4:53] But basically it's just doing that.
[4:56] It's scaling out a long triangle until that distance is achieved.
[5:01] So the question you might ask is, okay, well, if you understand that concept, basically
[5:05] we just need to get our roto shape at the correct distance in 3D space.
[5:09] How do we find the point in 3D space?
[5:13] So one way, which is not the most efficient way, is to look at the point cloud that's
[5:17] generated automatically by your camera tracker.
[5:21] So you can see a bunch of points.
[5:22] And this scene is not a great example of where this would be particularly useful because,
[5:27] well, you can't really tell where the tree is.
[5:29] And maybe it's the points right here, but it's not the best representation just due
[5:35] to the nature of how the scene is shaped.
[5:38] So another way to do this would be using this tool.
[5:41] So we need to figure out what 3D point this bottom of the tree is, where the position
[5:47] is.
[5:48] So essentially we could use this tool, which is Nuke's points to 3D.
[5:52] I'll explain it very briefly, but I'm going to also explain this tool, which does the
[5:56] exact same thing.
[5:58] It's just less glitchy.
[5:59] So for whatever reason points to 3D, it's sort of hit or miss.
[6:04] Sometimes I've had great success with it.
[6:06] Sometimes it just doesn't work that great.
[6:08] This scene in particular or whatever reason, it's not working well with this camera.
[6:11] I even know the track seems to be working fine.
[6:15] Sometimes this will not work perfectly, but the way it works is very simple.
[6:18] If you click in the points to 3D, you have three points.
[6:22] This is point A, point B, and point C. So essentially what we're doing is triangulation.


### Triangulation [6:27]
**Transcript (timestamped):**
[6:27] And if you guys don't know what triangulation is, I have a video.
[6:30] I'll try to link it in the thing here, basically explaining what this concept is.
[6:36] We need to define three points throughout the frame range of our video.
[6:42] And it will try to determine, based off of those three positions that we've determined
[6:46] at different times, where a point is.
[6:50] So if I do a fresh points to 3D, I'm not going to run it through because it's not giving
[6:54] me the best result on this particular shot.
[6:56] And I'll show you why.
[6:59] So if we take point A here, so I'm just creating a new one and we say, okay, so we want to
[7:04] figure out, let's say this little white dot on the bottom of the tree, we set point A
[7:09] to that position at the start of our video.
[7:12] And we say set frame.
[7:14] And essentially what we want to do is we want to create these points relatively far from
[7:20] each other in terms of time.
[7:23] So you want to not just put all the points that, you know, on frame one, two, and three,
[7:27] you want to like go like halfway and then a little bit further so that there's this kind
[7:31] of traveled a little bit further.
[7:34] So point B, it's about 30 frames in.
[7:36] So we set that, go here, set the position on the dot there and we'll just say set frame.
[7:47] And don't forget to say set frame, otherwise it just totally doesn't work at all.
[7:51] And then point C.
[7:55] And we'll place it there.
[7:57] And essentially what you normally do is you hit calculate and you'll see sometimes this
[8:02] gives us results that are good and sometimes it doesn't.
[8:04] And that's why I also wanted to bring in this custom gizmo because in this particular instance,
[8:08] for whatever reason, it's not giving the best result.
[8:11] So we'll just run it through and we can see exactly what it's supposed to do.
[8:17] So essentially what it does is supposed to tell us a 3D point.
[8:21] So this is the 3D point that it's determined.
[8:25] And it's also giving us a 2D track.
[8:28] But this 2D track seems to be off and that's why I've used this custom gizmo, which I much
[8:32] prefer this one anyway.
[8:33] It's just much easier.
[8:34] But that's essentially the concept.
[8:36] So now we're going to do the same exact thing with this tool, but it works a little bit
[8:42] differently.
[8:43] So pixels to position.
[8:44] It's a custom one.
[8:45] This is again available right here.
[8:46] You can download it.
[8:48] And basically the same exact concept, plug it in the camera, you plug in the footage
[8:53] and you notice I've undistorted our footage as well because we want it to, we don't want
[8:57] to work on a distorted footage if we're dealing with a 3D track or stuff like that.
[9:03] So just make sure you have the undistorted.
[9:04] And if you don't know where this is coming from, if you're familiar with 3D camera tracking,
[9:09] this is automatically created in our setup here.
[9:12] Or you can generate this manually using other methods.
[9:17] So pixels to position.
[9:19] This is a custom no, but basically same as that concept.
[9:22] We go to a frame.
[9:24] Make sure we have the overlay on.
[9:25] So if I hover over and hit Q, we have overlay on.
[9:28] I'm going to select the point, but this time there's no point A, point B kind of interface
[9:34] here.
[9:35] You just use your sampling.
[9:36] So if I hold control, you see that little red selector.
[9:39] So I'm just going to do the same thing and select our point here and say add point.
[9:44] And you see that it's captured that position on frame three.
[9:48] So it's doing the same exact thing we just did.
[9:50] So I'm going to go forward in time and do the same thing.
[9:54] Hold the same point and say add point.
[9:58] And let's just take a look at the node.
[10:00] So immediately you see this node without even having to solve the entire frame range has
[10:04] already determined something.
[10:06] And it's much more accurate than our points to 3D.
[10:09] So that's why I prefer this tool in general.
[10:11] It just seems to work more of the time and it's much faster.
[10:16] So even with just two points is figured out pretty much perfectly this point in 3D space.
[10:23] So essentially what you do now is you can either export this as a 2D track if you want
[10:27] a 2D track of that area or you can export an axis which is basically a 3D point space
[10:33] which will give you something like this.
[10:35] But what we're going to use it for is really just a reference for where to place our image
[10:39] plane.
[10:40] So if we go back to our image plane setup and we look at where this thing is falling.
[10:47] If I double click the image plane, we can adjust the distance.
[10:50] Just make sure we have two properties, two basically more than one property sets.
[10:55] We can see them both at the same time.
[10:56] So I want to make sure that we have this node open the property panel as well as this one
[11:01] at the same time.
[11:02] And that will allow us to see both of these in 3D.
[11:06] And so essentially we just want to make that distance sit on top of that pixel or that
[11:11] point rather.
[11:13] So if you just adjust this, you'll see as I use my arrow keys up and down, it's pretty
[11:18] much just shifting the position.
[11:19] We can just line it up at that point.
[11:22] And now we know that this card is sitting right on the tree, at least relative to the
[11:28] right side of the tree.
[11:30] We know this tree is not flat by the way.
[11:32] So there's a little bit of downsides to this.
[11:35] Like we don't have a 3D geometry that's going to match perfectly.
[11:39] But it is going to stick pretty dang close.
[11:40] And this can speed up your roto quite a lot if you're trying to rotoscope or something
[11:44] like this.
[11:45] So we see on this side, it's actually sticking more accurately than it is on this side of
[11:49] the tree.
[11:50] And that's because obviously this is a 3D tree.
[11:52] It's not a 2D surface.
[11:55] But it still helps you out because you can take the roto shape.
[11:57] And if you're just trying to roto this real quickly, you can just kind of adjust those
[12:01] points over time.
[12:02] And as that shot plays through, we just saved a lot of work having to do that kind of stuff.
[12:09] So that's pretty much the concept.
[12:11] And that's a really beginner method.
[12:14] This tool, it's pretty much the same as like proprietary tool that like a lot of studios
[12:19] will have.
[12:20] So it's pretty much the equivalent.
[12:22] And it's a very, very common technique.
[12:24] Sometimes if you have a complex shot, you might have hundreds of these being used.
[12:29] So let's just see.
[12:31] Yeah, that's pretty much it.
[12:33] I think just remember that card 3D, it's not running through a scan line render.
[12:38] So it's not the same as a card doing something like this.
[12:43] You could achieve the same result by doing, if I just copy it real quick here, you could
[12:47] achieve the same exact result that we've done by doing a roto projecting it.
[12:53] So you do a project 3D.
[12:57] And frame holding the camera on the frame that we are projecting from.
[13:02] So we'd say our reference frame is frame four.
[13:05] And then we would have to go here, scale up the card, so if you scale the card, and then
[13:10] we place the card into position.
[13:11] You see it's doing the exact same thing.
[13:13] So this whole setup has basically created the whole thing.
[13:16] But we have all these nodes instead of this one.
[13:19] And we're running it through a scan line render, which is actually rendering out.
[13:22] And it's just a bit heavier.
[13:25] And if you have a lot of these in your script, it's going to take longer.
[13:27] So this is just a time saver.
[13:28] It's pretty much what it is.
[13:30] You can also, of course, not just do for color corrections.
[13:33] You could always put some elements or something.
[13:36] If you have some smoke in a scene.
[13:38] We could switch this to emerge instead of a grade.
[13:42] And then we could just scale this down.
[13:46] And then we could mask, essentially mask the noise.
[13:49] And then we could have an element sitting around that basically area.
[13:52] And it'll sit around the base of the tree.
[13:55] So that's a very quick way to have that and 3D track it without having to go in and do
[13:59] projections.
[14:03] So that's pretty much it.
[14:04] I'll chuck the camera up here in the script so you guys can play around with this if you
[14:08] want to practice.
[14:09] And I'll just leave some of the stuff that was here.
[14:11] Let me put back the grade so that you guys have it set up with the color correction.
[14:19] Because this is more commonly what I use it for, I would say, is just color correcting
[14:23] different areas.
[14:24] One downside, again, is that this card is because of scaling outward from the camera.
[14:32] It's not going to be great if you're scaling a very flat, like, wide ground.
[14:36] For example, because this card is basically sort of facing us.
[14:42] So the card is always kind of facing the camera.
[14:45] It's not, let's say, parallel to the ground.
[14:49] It's always kind of facing this direction, which for a lot of purposes it works really
[14:55] well.
[14:56] But if you're flying across the land, for example, that's a point where you probably
[15:00] would want to hop into 3D and use a normal card and a normal setup.
[15:05] For example, if we wanted to color correct this entire ground, we would want a 3D geometry,
[15:10] not this method.
[15:12] So that's pretty much it.
[15:13] If you found this useful, hit the like button, subscribe, and I have more beginner content
[15:19] coming as well as intermediate and advanced that's been in the works for quite some time.
[15:23] So I'll have some more announcements on that in the next month or month and a half, I expect.



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
