---
title: Ray Render in Nuke Tutorial | Compositing 3d Reflections
source: YouTube
url: https://www.youtube.com/watch?v=UQlTyaVKog4
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke / NukeX (RayRender, AmbientOcclusion, and camera-tracked 3D projections all require NukeX)"
version: "not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)"
tags: [3d-system, camera-tracking, digital-matte-painting, advanced]
extraction_status: complete
frames_dir: tutorials/frames/ray-render-in-nuke-tutorial-compositing-3d-reflections/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Ray Render in Nuke Tutorial | Compositing 3d Reflections

**Source:** [YouTube](https://www.youtube.com/watch?v=UQlTyaVKog4)
**Author:** Compositing Academy
**Duration:** 22m44s | 9 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Hey everyone, this is just a quick tutorial on how to create a 3D reflection inside of Nuke.
[0:05] So this is not the 2D trick method that we can use to kind of create some fake reflections.
[0:10] These are actually ray traced reflections inside of Nuke.
[0:14] So if you could just take a moment and hit the like button and subscribe as it really
[0:17] helps with the YouTube algorithm and supporting the channel and trying to get the start here.
[0:24] The channel is pretty new.
[0:25] I don't have that many followers or anything like that yet, but I hope to produce a lot
[0:28] more content like this.
[0:29] So if you guys could just take a second and just do that, that would be really big help
[0:32] for me.
[0:34] So this is the effect we're going to be creating.
[0:35] We have a sphere here that's chrome and this is completely fake.
[0:39] And it's inside of Nuke.
[0:40] We're not going in Maya or Blender or anything like that.
[0:44] And this effect is achieved entirely in the ray render node inside of Nuke.
[0:51] So how do we do this?
[0:53] Actually, the setup is not that complicated.
[0:56] And I can actually provide you guys the project file if you want to have some assets to play
[1:00] with.
[1:01] So I'm providing you guys with this footage here, just a little kind of astroturf area
[1:07] with a bench.
[1:08] And then we have a sky picture.
[1:11] And then we also have a 360 picture and just a picture of the opposite angle.
[1:18] So I'm going to teach you guys two ways to actually create this reflection.
[1:21] There's a cheap way and there's kind of the right way.
[1:25] The reason I like teaching both ways is because sometimes you're in a pinch and sometimes you
[1:31] don't have all the rendered assets that you need.
[1:35] Or you might not have a 360 picture like this.
[1:39] So what I'm teaching you how to do is even if you don't have a 360 camera or you are
[1:44] receiving this footage from somebody else, you'll still be able to create a reflection
[1:48] for those shots using these techniques, using the kind of hacking, compositing way.
[1:54] And as a compositor, you want to always be thinking how to get the result no matter what
[2:00] you have and being resourceful.
[2:02] So that's really important.
[2:03] So without dragging that on too long, let's get to actually how to create this effect.
[2:10] So what we're going to do, first you need a 3D camera track.


### 3d Camera Track [2:12]
**Transcript (timestamped):**
[2:14] So I've provided you guys with that in the script file.
[2:17] So you guys don't need a 3D camera track.
[2:19] This tutorial is not about 3D camera tracking.
[2:21] If you need to find that, I have other information on that.
[2:24] So if we just start with our shot here, I'll just go over here so the track is here.
[2:32] I've basically tracked this scene and I've placed a card on the ground plane of this
[2:41] scene.
[2:43] So again, if you don't know 3D tracking, I do have other tutorials out there for that.
[2:48] And if we just look through our camera, let's just merge this over so we can see.
[2:57] And let's put it as a wireframe.
[2:58] So I'm going to put a wireframe shader just to show you guys that there is in fact a 3D


### Wireframe Shader [2:59]
**Transcript (timestamped):**
[3:04] track scene here.
[3:05] So this is just a, the wireframe texture is, it just creates this kind of, you can see
[3:10] the polygons of your geometry.
[3:13] And I'm just putting that onto the card that I've placed on the ground plane.
[3:16] So that's what we're going to start with.
[3:18] We have a ground and a 3D tracked scene with a camera.
[3:24] So what we actually need to do to make a convincing reflection is we actually need to project
[3:31] this footage onto the ground around the object that we're reflecting.
[3:36] So if you look at our footage here, we see that this sphere is actually reflecting the
[3:42] grass that's sitting on and everything around.
[3:44] So all we need to do is we put that ground plane into 3D space and we're going to re-project
[3:50] this plate that we're filming with.
[3:53] So this video that we're looking through, we're going to project that onto the geometry.
[4:00] So that's the first step.
[4:01] So we're going to create that card and that's been given.
[4:03] So you guys start with the card.
[4:05] Next thing we need to do is we create a sphere.


### Create a Sphere [4:06]
**Transcript (timestamped):**
[4:08] So I put a sphere here and just put it into 3D space in the right spot.
[4:15] So it's just a basic sphere.
[4:17] And if I hit play here, you'll see once we get it, once it caches, that this video is
[4:26] kind of playing through.
[4:30] The caching is not that great in nuke when you're playing it for the first time, but you
[4:34] can see the video is rotating around and projecting that image onto the card.
[4:41] So we're just using the video, a normal project 3D node.
[4:46] We've hooked in our camera and then we plug that texture into a card.
[4:50] So now it's shooting that video out from our camera onto the card.
[4:57] And the next thing we're going to do is we want to put a reflection node on the sphere.
[5:04] And the other thing we need to do is a normal scan line render won't work for this.
[5:09] So we're going to delete the scan line render.
[5:11] And I'm going to create a node called ray render.
[5:15] You guys might be familiar with this node already, but this tutorial is still going
[5:19] to be useful for you because it's going to teach you how to mix projections and still
[5:23] get a reflection.
[5:25] So if you guys already know how to use this, it's still a useful tutorial, I think.
[5:29] So we're going to plug in a ray render node and we're going to look through that result.
[5:34] And what we can see already is if we actually see that this is already kind of working,
[5:39] this effect is sort of already working.
[5:40] We have a sphere that is reflecting the ground around it.
[5:46] So we can see that if we just disable the reflection and enable, it's actually ray-tracing
[5:51] this reflection.
[5:53] So the difference between the scan line and the ray trace, the scan line render is good
[5:57] for elements and smoke effects and some lights and stuff like that.
[6:03] But if you're going to create a reflection or some actually physically accurate shadows,
[6:08] you need to use the ray render node.
[6:11] So we're already most of the way there, but we want to make this a lot better.
[6:16] And something that's important about reflections is they need to be spatially accurate.
[6:23] If you were looking at this ball, you would think that, well, maybe we're going to be
[6:26] reflecting more of this bench and this bench is right next to the ball.
[6:31] So we should be seeing some of that actually in this reflection.
[6:35] But the problem is we're projecting this entire image onto a flat plane.
[6:40] So it can't accurately, this ball can't accurately reflect what's sitting next to it, which is
[6:47] this bench.
[6:49] So what we need to do is we need to start building a simple model build of the geometry


### Model Build [6:52]
**Transcript (timestamped):**
[6:54] that sits around this sphere.
[6:56] And we can do that just inside of Nuke.
[6:59] So we're going to just expand this a little bit.
[7:03] And I'm going to create a cube node and just plug that in.
[7:11] And I'm going to scale it down because it's huge.
[7:13] Our scene is kind of tiny.
[7:14] So I'm going to scale it down.
[7:17] And I'm going to set the divisions to one and one because I don't need the cube to have
[7:22] a bunch of subdivisions.
[7:23] It just makes it harder to grab inside of Nuke sometimes.
[7:27] And what I'm going to do is I'm going to plug the same project 3D node that's giving our
[7:33] card a texture.
[7:34] I'm going to plug that straight into the cube as well.
[7:37] So now that image is being projected onto the card and onto the cube.
[7:41] So if I move the cube around, you see that the texture is changing.
[7:44] That's because we're not applying the texture as a texture to the cube.
[7:49] We're applying it as a projection.
[7:51] So just imagine that that video is starting in the camera and being projected out and it's
[7:58] wrapping around our geometry.
[8:02] So our goal with this is we need to kind of line it up with where it is in the real world.
[8:06] So the easiest way to do that is to look at the projection and line it up to the ground
[8:10] plane.
[8:11] So that's where this thing starts on this flat plane.
[8:16] It's right here on this card.
[8:18] So all we need to do is take the cube and put the front of the cube on the front of
[8:21] the real box here.
[8:23] So we're going to line it up and just slide it over until you start to see that the box
[8:31] lines up.
[8:32] So something like this.
[8:35] And just going to keep moving it.
[8:38] And you see there's still a little bit of an edge here on the ground.
[8:42] You see how that edge doesn't line up with the cube.
[8:44] So we just need to rotate our cube just a little bit.
[8:47] So I'm going to take the cube and just rotate it in the Y. So I'm just slightly rotating
[8:53] it.
[8:54] So if you look at this edge as well, you see this is the, if we look at the footage, this
[8:59] kind of curved wire is the edge of that cube.
[9:03] So in our 3D, we're just going to take it and rotate it so that that edge lines up with
[9:09] our fake edge.
[9:10] So I'm going to rotate it like that and just line it up here.
[9:19] And one thing we can do to also make this a little bit better is I have a lens distortion


### Lens Distortion [9:22]
**Transcript (timestamped):**
[9:23] node provided to you guys as well.
[9:25] And we're going to undistort our footage that's coming in.
[9:29] So that's just going to help a little bit with, and there's very little distortion on
[9:34] this.
[9:35] So it's not going to make a big impact, but that is something that is kind of necessary
[9:42] depending on the camera you're filming with.
[9:44] So this was filmed on an iPhone.
[9:45] This is very little distortion.
[9:48] So next thing we're going to do is, sorry, my whack of mess up there a little bit.
[9:57] So we got that cube lined up and we're just going to shrink it in the Z a little bit.
[10:04] So I'm holding command and shift on a Mac to make sure that we have these scale selectors
[10:10] there.
[10:11] I think that would be control shift on Windows, but I'm just scaling that into place and making
[10:18] sure at the bottom of our projection that it's lined up.
[10:22] And it doesn't matter if the cube is sticking to the ground a little bit.
[10:25] You're not going to see that anyways.
[10:27] And then I'm going to scale it up until it starts to hit the edge of the wood.
[10:33] So now if you rotate it around, you see it actually lines up with the real world.
[10:37] So now if we scrub through, we see that that kind of sticking, that image is sort of sticking.
[10:45] It's not 110%, it's not a perfect lineup, but for the sake of this tutorial, it's going
[10:51] to do good enough for our reflection.
[10:56] So I'm going to copy the cube and I'm going to do the same exact thing for the other side.
[10:59] So I'm just going to copy it, plug it into our scene and plug it into our project 3D
[11:04] and just slide this over until we hit our other little side of our bench here.
[11:14] And that's what we're going to get.
[11:15] We got something like this.
[11:17] And lastly, we're going to duplicate that cube, plug it into our projection again.
[11:25] And we're going to move it up this time and scale it down in the Y and scale it in our
[11:31] X. And then just shift it over.
[11:35] So what we're doing is we're creating the top part of the bench.
[11:39] And yeah, Nuke's transform tools, still not the best.
[11:46] They really need to fix it, but they do not think it's priority.
[11:54] But yeah, so this is sort of close here.
[11:57] So you can see we're starting to basically rebuild our real world in CG.
[12:04] All right, this is pretty good.
[12:08] So this is going to give something to our sphere to reflect.
[12:11] So we're basically building the CG world out just so that we can get a reflection of
[12:16] those objects in the proper way.
[12:19] And since this is closer, it's going to reflect differently than something that's very far.
[12:23] So if we just take a look at our ray render again and we go back out into the 2D, I'm
[12:27] going to close all this.
[12:31] Now we can see we start to see some of our pieces actually wrapping and being close.
[12:37] So for example, I take the sphere and I move it, we're going to see as it gets closer to
[12:42] that object, it's actually reflecting it.
[12:46] So if I put it really, really close, you can even put it inside of it like that.
[12:53] And it's reflecting the edges, which is a pretty cool effect.
[12:56] So you can do all kinds of stuff with this.
[12:57] You can create even a basic window, you can use the same technique.
[13:02] And I'll show you guys that briefly after.
[13:05] Actually, I'll just show you right now.
[13:06] It's very simple.
[13:08] So the same technique you can take a plane or sorry, a card and plug it in.
[13:20] Let's close everything so we can see what we're doing.
[13:23] So this is the same principle of what we're doing, but a very, very simplified version
[13:28] is just a reflection, a card.
[13:31] And then just taking another card, I'm going to take the, actually sorry, I'm going to
[13:39] take this 360 picture and put it on a sphere instead.
[13:42] So let's take a sphere and we plug this picture into it.
[13:47] And we'll plug that into a ray render just quickly.
[13:50] You guys don't have to follow along with this one.
[13:52] It's just to demonstrate the principle.
[13:57] Let's pretty see node and scale up that sphere.
[14:04] So it's big.
[14:08] And if we reduce the size of our card, we're going to see what's happening here.
[14:12] So this is kind of hard to see.
[14:14] So I'm just going to reduce the size.
[14:17] So here's our little reflective card.
[14:20] And here's our camera.
[14:23] So that is automatically going to reflect whatever is opposite of it.
[14:28] So if we're looking at this, it's hard to see a little bit, but this card here is reflecting
[14:34] the sphere around it.
[14:35] So you understand if you have a 3D camera track and you have a window, you can just stick
[14:39] a reflective card on that window and then put another image opposite of it.
[14:46] So it doesn't matter what image you use.
[14:48] So if you don't have, for example, this 360 photo of the place that you filmed, it doesn't
[14:52] matter.
[14:53] You can still do this and just take a different photo that looks like it would be something
[14:57] that would be behind the glass that you're filming.
[15:01] So that's essentially the principle.
[15:03] But we're doing a more advanced version, which is actually building it out into the actual
[15:09] spatial scene that it is.
[15:12] So we can continue to build this.
[15:13] I'm not going to build out the whole thing.
[15:14] I'm going to switch over here to whatever I've already done.
[15:17] So this is what I built out.
[15:19] And I just put this little barrier here, the wall.
[15:22] You could even put the plant.
[15:23] You see the plant is not built out here, this little pot with the plant.
[15:29] You could put a cylinder and you'd build it out if you want.
[15:34] So that works for the foreground stuff.
[15:36] It works for all the stuff directly around.
[15:38] And that's going to give you a pretty good reflection as it is.
[15:41] But the next thing we need to do is we need to give it something to reflect in the sky.
[15:46] So if we look at what we have just done and we just look at the result, we see that we
[15:52] have a black sky.
[15:53] There's nothing to reflect.
[15:56] So what we need to do is just any picture of a sky.
[15:59] I just took a 2D picture and kind of graded it up and put it on a sphere.
[16:04] So if I zoom out and look at that sphere, this is all it is.
[16:08] Just straight on the sphere and I transformed it to kind of scale it.
[16:13] So that's all we got.
[16:15] And now if you look at the ray render, we can see that we filled in that black with the
[16:22] sky.
[16:23] So this is the kind of quote unquote cheap version.
[16:28] And this will get you, if you don't have the 360 picture or anything like that, this is
[16:32] still going to work for you and you can still get a reflection.
[16:37] But I also did take this 360 picture.
[16:39] So this is just better because this is actually going to give us everything else that was
[16:44] actually beyond.
[16:46] So we have our close objects that we modeled.
[16:48] So we have this bench and we have this little wall here and everything.
[16:51] But we have these really objects that are further away like the sky and the house and
[16:55] the chairs.
[16:56] I don't want to model all those things because they're so far away from the camera.
[17:01] But if you do have a 360 picture, you can use that instead.
[17:04] So I'm going to switch it over to that because that's going to give us a better result.
[17:07] So if I just take a look at that result, you can see that's a much, much better result.
[17:13] If you want to learn how to take 360 pictures, you can do it with any camera.
[17:17] You can take an iPhone, you can take an Android phone and there's a lot of apps even to take
[17:21] 360 pictures.
[17:23] And any of those are going to work for getting a reflection map.
[17:27] And you can plug that straight into your sphere.
[17:30] Okay, so this is working pretty well.
[17:33] You notice that all these weird things are happening in the background and that's just
[17:36] because we're kind of looking at the picture that we placed behind.
[17:43] So what we want to do is we don't want to be our final image.
[17:47] We don't want to kind of output through this ray render.
[17:50] We just want to get the ball.
[17:51] We just want to get the ball out of the ray render.
[17:53] So what we need to do is just off to the side, create a scan line render.


### Scanline Render [17:56]
**Transcript (timestamped):**
[17:57] I'll just do it separately.
[17:59] I'm going to create a scan line render, plug it into the same camera and then I'm going
[18:04] to plug the object into the same sphere that we're wanting to keep.
[18:10] And this scan line render is just going to give us an alpha of that ball.
[18:16] And we can use that to mask it out from this ray render result because we don't want all
[18:21] this weird stuff and we don't want to re-project our whole environment.
[18:24] We just want to, because that's going to actually distort and blur our image a little bit.
[18:29] We want to have control.
[18:31] So what we do is we just mask that out and then we have just our reflective ball.
[18:37] And this allows us to just A over B, merge it over our image.
[18:41] So here's our background and here's our ray render result that was we stenciled out, our
[18:47] masks to out and that's what we got.
[18:49] We have a reflective sphere.
[18:52] And lastly what we can also do is another technique.
[18:55] So what we want to do also to make it a little bit more convincing, we want to add what's


### Ambient Inclusion [18:58]
**Transcript (timestamped):**
[18:58] called ambient inclusion.
[19:00] And we can do this inside of Nuke as well with the ray render.
[19:02] So if we just take a look at what that is, it takes a second to process there.
[19:09] So what this is doing is it's creating a contact shadow between the two pieces of geometry
[19:15] inside of Nuke.
[19:16] So that makes it a lot more convincing.
[19:20] You see it before and then after.
[19:22] It really feels like a more of an object is there.


### Create an Ambient Occlusion [19:24]
**Transcript (timestamped):**
[19:24] So how do we create an ambient inclusion?
[19:27] This is very simple.
[19:28] So we can just take the same setup we did.
[19:31] We take our reflective sphere, the same geometry we used and just copy it.
[19:36] And we copy our ground plane.
[19:39] So we just take those two pieces of geometry and we plugged it into an ambient occlusion
[19:44] though.
[19:45] So you can just type it in ambient occlusion and make sure you have it plugged into like
[19:50] a constant or something like that.
[19:53] And we can just take a look at the result.
[19:55] If we look at the render, it takes a little bit of time to process that.
[20:01] And again, so you need to use the ray render node for this as well, not the scan line render.
[20:05] If you plug in a scan line render, this is not going to work.
[20:08] So the ray render is good for reflections and good for this ambient occlusion pass.
[20:14] So this is a pretty good result.
[20:15] And the last thing we need to do is if I just go back to frame, I'm going to go back to
[20:19] the start frame here, frame 55, just to show you guys a problem that you might see.
[20:28] So we see that our geometry, so at the start frame here, we see that our geometry is kind
[20:33] of ending here, like the card is not long enough.
[20:36] So we're seeing the edge of the card.
[20:38] So either you can scale this card to be really, really huge or you can just merge a white
[20:44] constant underneath to just fill in that black hole that's in the back there.
[20:50] And that's going to allow us to do a multiply.
[20:53] So if we do multiply, it's going to get rid of all the white and keep the dark areas.
[20:58] And we see that that gives us our nice shadow effect.
[21:04] And lastly, what you can do to make it a little bit more realistic if you want is I
[21:07] did a luminous key of the highlights of the ball we have.
[21:13] I did a luminous key and I pre-multiplied that result.
[21:17] So we just keep the brighter areas of the sky.
[21:20] And I did an exponential blow and just screened that over just to get a slight glow on the
[21:25] surface of this chrome ball to make it look a little bit more convincing.
[21:31] Again if you were doing this for real and you wanted to do the full proper way of doing
[21:35] this, you would of course need to make sure you have your lens undistorted and lens distorted
[21:43] at the end of your ray render.
[21:45] So redistort.
[21:49] So that would be something that you want to make sure you do.
[21:51] And also you would put grain here as well.
[21:54] So you match your film grain to make this more convincing.
[21:56] But this is just a quick tutorial on how to make a reflection work for you.
[22:00] So that's basically it.
[22:01] I hope you guys enjoyed.
[22:03] I'm going to put the link in the description below if you want to download the project
[22:06] files.
[22:07] And it's a pretty straightforward tutorial.
[22:10] And the other thing I want to introduce you guys to is I have a website here.
[22:15] It's called gumroad.com slash compositing academy.
[22:20] So if you type in this address gumroad.com slash compositing academy.
[22:24] I have like a little email list I'm building up that I'm going to be releasing like much
[22:29] of larger classes on my own website and kind of off to the side.
[22:33] So if you guys want to keep up to date with that kind of stuff, that would be great if
[22:39] you're interested.
[22:40] So yeah, that's basically it.
[22:41] Thanks.



---

## Captured Frames

- [2:58] tutorials/frames/ray-render-in-nuke-tutorial-compositing-3d-reflections/frame_000.jpg
- [5:40] tutorials/frames/ray-render-in-nuke-tutorial-compositing-3d-reflections/frame_001.jpg
- [7:11] tutorials/frames/ray-render-in-nuke-tutorial-compositing-3d-reflections/frame_002.jpg
- [9:44] tutorials/frames/ray-render-in-nuke-tutorial-compositing-3d-reflections/frame_003.jpg
- [14:20] tutorials/frames/ray-render-in-nuke-tutorial-compositing-3d-reflections/frame_004.jpg
- [17:07] tutorials/frames/ray-render-in-nuke-tutorial-compositing-3d-reflections/frame_005.jpg
- [18:16] tutorials/frames/ray-render-in-nuke-tutorial-compositing-3d-reflections/frame_006.jpg
- [19:55] tutorials/frames/ray-render-in-nuke-tutorial-compositing-3d-reflections/frame_007.jpg

---

## Structured Notes

### Core Technique
Creating genuine ray-traced 3D reflections entirely inside Nuke (no external renderer) by combining a solved 3D camera track, a hand-built rough proxy model of the surrounding environment, footage re-projected onto that geometry, and Nuke's `RayRender` node (not `ScanlineRender`, which cannot ray-trace reflections or ambient occlusion).

### Summary
Two approaches to a chrome-sphere reflection composited into real footage of a backyard bench/patio, both starting from a pre-solved 3D camera track: the "cheap" version projects the live footage flat onto a single ground-plane card, which is fast but spatially wrong (nearby objects like a bench won't show up correctly in the reflection because everything is flattened onto one plane); the "right" way rebuilds a rough low-poly proxy of the immediate environment (simple scaled/rotated `Cube` primitives standing in for the bench, wall, planter) using the *same* re-projected footage as texture, lined up by eye against the projected image so it "sticks" as the camera moves. Distant elements (sky, background houses) are handled without modeling: either a flat 2D sky photo graded and stuck to a distant sphere (cheap/no-360-photo fallback), or — for a much better result — a genuine 360° photo of the location mapped onto a sphere surrounding the whole scene. The actual reflective object (a chrome sphere) is rendered through `RayRender`, which unlike `ScanlineRender` can physically ray-trace reflections and ambient occlusion off the surrounding proxy geometry. A separate `ScanlineRender` of just the reflective sphere produces a clean alpha to mask/stencil only the ball out of the messy RayRender beauty pass (which also shows the ugly proxy geometry) before merging it back over the original plate. A second `RayRender`-based `AmbientOcclusion` pass (fed the same reflective object + ground geometry) generates a believable contact shadow beneath the object. Final polish notes: fill exposed proxy-geometry edges/gaps with a white constant and multiply to fake soft contact shadowing, add a subtle glow via a luma-keyed/pre-multiplied/exponential-blurred screen pass on the highlights, and always undistort before projection and re-distort after the RayRender for lens accuracy, plus match grain at the end.

### Key Steps
1. Start from a pre-solved 3D camera track of the plate (out of scope for this tutorial itself).
2. Create a ground-plane `Card` positioned/oriented to match the real ground in the tracked scene; optionally verify alignment with a wireframe shader.
3. Re-project the live footage onto that card using `Project3D` fed by the tracked camera, so the plate "wraps" correctly onto the ground geometry as the camera moves.
4. Add a `Sphere` primitive at the location where the reflective object should sit.
5. Delete/avoid `ScanlineRender` for the reflective object — instead create a `RayRender` node, since only RayRender can physically ray-trace true reflections (and later, ambient occlusion); ScanlineRender is fine for elements/smoke/some lights but not reflections or accurate shadows.
6. Verify the basic reflection already works once RayRender is hooked up, but recognize the flat single-card projection is spatially wrong — nearby objects (e.g. a bench) won't appear correctly in the reflection because everything projects onto one plane.
7. Build simple proxy geometry for everything close to the reflective object: duplicate/add `Cube` primitives (divisions set to 1×1 to keep them simple to manipulate), scale/position/rotate each to roughly match a real nearby object's footprint (e.g. bench sides and top), and feed each cube the *same* `Project3D` texture stream used for the ground card so the real footage wraps around them too.
8. Line up each proxy cube by eye against the projected footage — match edges visible in the projection (e.g. a curved wire/edge in the plate) by rotating/scaling/translating the cube until the CG proxy edge lines up with the photographed edge; scrub through frames to confirm it "sticks" as the camera moves (doesn't need to be perfect).
9. Undistort the incoming footage with a `LensDistort` node before projecting, for extra accuracy (impact is small on lightly-distorted footage like an iPhone shot, but matters more on stronger lenses).
10. For distant elements with no nearby geometry needed: either (a) cheap fallback — grade a flat 2D sky photo and place it on a large distant sphere, filling the RayRender's black background/sky gap, or (b) better — map a genuine 360° photo of the actual filming location (shot on any phone with a 360 camera app) onto a surrounding sphere, giving accurate reflections of everything beyond the modeled foreground (sky, distant buildings, furniture) without having to model any of it.
11. The same core principle (camera track + a reflective card/geometry + an opposite-facing image plugged in) also works for simple flat reflective surfaces like windows — put a reflective card where the window glass is and any plausible "what's behind the glass" image on a card/sphere facing it.
12. Once the environment and reflective object render correctly through RayRender, don't use that beauty pass directly — add a separate `ScanlineRender` fed the same camera and only the reflective object geometry, producing a clean alpha matte of just that object.
13. Use that alpha to mask/stencil the RayRender result down to only the reflective object, discarding the ugly visible proxy geometry and any projection distortion/blur elsewhere in frame; `Merge` (over) that masked result onto the original background plate.
14. For contact shadowing: duplicate the reflective object geometry and the ground geometry, feed both into an `AmbientOcclusion` node (also RayRender-based — ScanlineRender will not work for this), and use the resulting occlusion pass to darken the contact area for a noticeably more convincing "object is really there" feel.
15. Fix visible edges of finite proxy geometry (e.g. the ground card's edge appearing in early/extreme frames) either by scaling the card much larger, or simpler: merge a white `Constant` in behind it to fill the resulting black gap, then `Multiply` that combined pass over the shot so the white areas vanish and only the intended dark/shadow areas remain.
16. Optional final polish: `Keyer` (luminance key) the brightest highlight areas of the rendered reflective ball, `Premult`, apply an exponential `Blur`/glow, and `Screen`-merge it back over the ball for a subtle bloom; always re-distort with the same lens-distortion values used to undistort earlier; add matching film grain at the very end for full production integration.

### Nodes / Tools / Settings
- `RayRender` — the core node; performs true ray-traced rendering (reflections, ambient occlusion) that `ScanlineRender` cannot produce; used for both the beauty pass of the reflective object and the ambient occlusion pass.
- `ScanlineRender` — deliberately used in two places despite RayRender being the star: (1) as the source of a clean alpha matte of just the reflective object, for masking; explicitly stated as unusable for reflections or ambient occlusion.
- `Project3D` — projects the live-action plate footage from the tracked camera onto all proxy geometry (ground card + cubes), so real footage textures the environment rather than a flat UV-mapped texture.
- `Card` — flat plane standing in for the ground; also demonstrated as a simple reflective surface for a window-style reflection trick using an opposite-facing image.
- `Cube` (multiple, divisions set to 1×1) — rough proxy geometry for nearby real objects (bench sides/top, low wall), scaled/rotated/positioned by eye to match the projected footage.
- `Sphere` — the reflective chrome object itself; also used (scaled large, surrounding the scene) to hold either a flat graded sky photo or a full 360° environment photo for distant reflections.
- `LensDistort` — undistort before projection, re-distort after the RayRender, to preserve lens accuracy through the projection round-trip.
- `AmbientOcclusion` (RayRender-based) — fed duplicated object + ground geometry to generate a contact-shadow pass.
- `Constant` (white) + `Multiply` — fills exposed proxy-geometry edge gaps (black holes at frame extremes) so they read as clean instead of artifacted.
- `Keyer` (luminance key) + `Premult` + `Blur` (exponential) + `Screen` merge — optional glow/bloom pass on the reflective object's brightest highlights.
- Wireframe shader — optional visual aid to confirm the 3D-tracked scene/geometry placement is correct.

### Difficulty
Advanced — combines 3D camera tracking (assumed as prerequisite, not taught here), hand-built proxy geometry matching, projection texturing, and NukeX's ray-tracing-specific nodes (RayRender, AmbientOcclusion), explicitly labeled as going beyond simpler 2D reflection tricks.

### Foundry App & Version
Nuke / NukeX — `RayRender` and `AmbientOcclusion` are NukeX-tier ray-tracing nodes; the 3D camera-tracked projection workflow also implies NukeX. Version not stated on screen or in narration. 2020 upload, predates this skill's release-notes backfill (starts at Nuke 13.0/March 2021), so treat as Nuke ~12.x era rather than a specific point release.

### Tags
3d-system, camera-tracking, digital-matte-painting, advanced

---

## Related Tutorials
- Re-lighting Real Footage | Nuke Compositing [Advanced] (`re-lighting-real-footage-nuke-compositing-advanced.md`) — shares `3d-system`, `camera-tracking`, `digital-matte-painting`, `advanced`; both derive convincing CG-like results (relighting vs. reflections) from a solved 3D camera track over live-action footage, without full production 3D geometry.
- Preserve Quality | Projections in Nuke (`preserve-quality-projections-in-nuke.md`) — shares `3d-system`; that video's projection-quality tips (limiting re-projected area, filter choice) apply directly to the Project3D-heavy proxy-geometry workflow taught here.
- Tracking Concepts in Nuke for Beginners (`tracking-concepts-in-nuke-for-beginners.md`) — shares `3d-system`, `camera-tracking`; that video explains the triangulation/parallax fundamentals behind the solved 3D camera track this tutorial assumes as a prerequisite.
