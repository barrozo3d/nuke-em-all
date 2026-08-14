---
title: [2/3] Nuke Tutorial Series (CRACKS, Keentools, Smartvectors)
source: YouTube
url: https://www.youtube.com/watch?v=dLrJhqqNMrk
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke / NukeX (SmartVector requires NukeX)"
version: "Nuke 13.x (13.1/13.2 — exact 2022 point-release not stated)"
tags: [tracking, camera-tracking, 3d-system, projection, channels, grading, digital-matte-painting, advanced]
extraction_status: complete
frames_dir: tutorials/frames/23-nuke-tutorial-series-cracks-keentools-smartvectors/
frame_count: 0
frame_status: pending-selection
---

# [2/3] Nuke Tutorial Series (CRACKS, Keentools, Smartvectors)

**Source:** [YouTube](https://www.youtube.com/watch?v=dLrJhqqNMrk)
**Author:** Compositing Academy
**Duration:** 56m1s | 15 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py 23-nuke-tutorial-series-cracks-keentools-smartvectors <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Introduction (Hit Like!) [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to part 2 of this Nuke series about how to go about creating this shot.
[0:16] So we're gonna talk about some different things than part 1.
[0:19] If you haven't seen the other parts, you can check out the trailer for this Nuke series
[0:23] and part 1.
[0:24] So those videos are on my channel.
[0:27] But yeah, so this one we're gonna talk about primarily how to go about doing the cracks
[0:32] on the face in 2D, in 3D, and some of the tracking solutions we can use to kind of approach
[0:39] this and also analyzing the shot before we approach it so we know what, which tool to
[0:46] use in which situation.
[0:47] So before you start doing things, it's good to know to kind of have an idea and see the
[0:53] problem areas of your shot before you approach it.
[0:56] So that's kind of generally how I approach shots is I look at it, I try to figure out
[1:01] based on the motion, based on the angles, what's gonna be the best thing in which area.
[1:06] So I'm not just gonna start doing a 3D track overall.
[1:09] You don't wanna be heavy handed on one technique and then it turns out you're either using
[1:13] a technique that takes too long or you're using a technique that's not gonna work.
[1:19] So you could do a certain type of track that would work for everything but maybe it takes
[1:24] way, way longer.
[1:26] So part of it is about saving time.
[1:29] So that's something to think about.
[1:32] So yeah, basically part two, we're gonna talk about setting up before creatives to the tracking,
[1:38] blending 2D textures, 2.5D enhancements, we're using some of the 3D mix with 2D textures,
[1:46] using UV space for lighting, 3D enhancement, 3D ambient inclusion, displacement, and then
[1:52] creating crack mats.
[1:54] So I'll talk about what that is.
[1:56] So this is basically what you need to do.
[1:59] You can pause this video if you're actually doing this project because this is a list
[2:02] of pretty much the order of how I would approach this if you're trying to do this project.
[2:07] So really when you're doing this, you wanna have your tracks all set up and then build
[2:12] out your cracks in this order.
[2:13] So I'm not gonna re-explain this but that's kind of the order of what you should do and
[2:18] you'll be ready for part three of the series if you've already done all of these things.
[2:24] So yeah, we'll get into it.
[2:26] First thing I'm gonna talk about is looking at this shot.
[2:29] So we'll just look at the original footage and sort of just play through and I can just
[2:36] kind of scrub through real roughly.


### Shot Tracking [2:38]
**Transcript (timestamped):**
[2:39] So one of the things I'm looking at when I'm looking at footage is how things move and
[2:44] when things, where things overlap.
[2:47] So if I take a Roto Paint, this is kind of what I briefly mentioned in the first video
[2:54] but I just wanna kind of point it out.
[2:57] So let's just get a color here.
[3:00] So one of the things that I'm looking at when I'm looking at this is this could either
[3:06] be a planar track, stuff like this could be planar track but I wouldn't wanna necessarily
[3:12] planar track here because we have warping.
[3:14] So the neck is going to be deforming and deforming is not the best situation for a planar track.
[3:20] So immediately when I'm looking at the shot, I'm already thinking smart vectors.
[3:25] If you do have mocha, there's a new, I think it's a Power Mesh tracker that can do deforming
[3:32] planar tracking basically but I don't have a mocha license so basically I'm just working
[3:36] in nuke.
[3:37] So smart vector is gonna be something that I'm looking at.
[3:41] So rather than doing a planar track and a smart vector, this area probably work as a
[3:46] smart vector as well.
[3:47] So that's what I'm thinking.
[3:48] So when I'm looking at this, I'm like, okay, well, this whole area, we already solved it
[3:52] with smart vectors.
[3:55] Same for over here, a smart vector is gonna work in most of this and if we gain up, we
[4:00] can see where there's detail and where there's not.
[4:03] So there's a little bit of detail in hand.
[4:04] So smart vector actually works for all of this area as well.
[4:09] The one area it doesn't work is basically this cloth which I think I'll talk about in
[4:14] the next video because this is more when we're putting the effects on.
[4:18] But there is one area here that's kind of a problem area and it's because there's all
[4:22] these basically vertical lines with no tracking features and the lighting is changing on it.
[4:29] So you can't really smart vector that and you'll see if you try to smart vector it,
[4:33] you're gonna get warping and stuff like that.
[4:35] So basically what we're gonna have to do in part three when we do the tracking for this
[4:39] area, you'll basically have to do a track here and a track here and we'll just blend
[4:44] those two tracks together.
[4:46] So using ST maps, we can blend the motion of these two transformations and solve this
[4:50] entire area by combining and dissolving basically rotoscoping those patterns together.
[4:58] So we can kind of mix tracks.
[5:00] And then the last thing and the biggest part of our shot is the face.
[5:03] So we could do some areas with smart vectors on this, you know, we could totally do smart
[5:08] vectors in a lot of areas.
[5:09] The areas smart vector is not gonna be great is where there are parallax and overlap.
[5:14] So you see here, we have that on the nose.
[5:17] So we have this area that's gonna be revealed behind and that's not gonna be a great place
[5:21] for smart vectors.
[5:25] We also have the same kind of problem down here.
[5:27] We have some overlap, which we wherever there's overlap, you're gonna have issues with smart
[5:33] vector.
[5:34] If we draw this out, this is the overlap area where the chin is gonna come across.
[5:41] So we see the chin is gonna come this way.
[5:43] So really what you are gonna want to do is a smart vector and rotoscope off this moving
[5:52] overlapping object.
[5:53] So basically we would chop off this chin area, we would roto it off and then we would smart
[5:59] vector everything below.
[6:00] So it's smart vector, all of this stuff.
[6:04] And let me just erase all this now.
[6:06] So let me just explain this concept a little further.
[6:08] So if we smart vector down here, we rotoscope off the chin.
[6:16] And then the area that it overlaps what we want to do is basically do an in paint.
[6:22] So in paint node, we can kind of do it's kind of like an edge extend.
[6:25] So we're kind of extending this smart vector track data and we want to extend it past the
[6:30] point where there's overlap.
[6:32] So that's kind of what we're gonna do for the tracking of that.
[6:37] And the same actually applies for areas that kind of fall off like over here when there's
[6:42] like an edge that the smart vector doesn't know what to do on the very edge.
[6:46] It does a really great job in the center, but on the edges, you might see a little bit
[6:49] of warping.
[6:51] So we would track the inside like this.
[6:54] And then we would do kind of an in paint and kind of edge extended outward.
[6:59] So the tracking data is gonna basically come from the area that's working.
[7:03] And that's how you can kind of track areas that have those edge issues with smart vectors.
[7:07] And that's not something people really talk about a lot with smart vectors.
[7:11] But it is something that is really useful to know that you can kind of do those type
[7:14] of things.
[7:17] One thing to know if you if you aren't familiar with smart vectors, by the way, you know,
[7:20] you can just type in smart vectors on YouTube, you're gonna find, I think the foundry even
[7:24] has some tutorials, how to approach smart vectors and all that stuff.
[7:28] So if you guys don't know how to use that, my goal with the channel is not to sort of
[7:33] reinvent the wheel with tutorials already exist.
[7:36] So you can go find that information.
[7:40] So that's how we would approach the tracking.
[7:42] So we're not going to use smart vectors on the face, we're going to use 3D.
[7:44] So that that overlap problem won't won't be a factor and we'll have the benefit of working
[7:50] in UV space by using a keen tools face tracker.
[7:55] So if you guys don't have keen tools for this project, it's okay, I'm providing the 3D track
[7:59] face so you can get some experience and see what it's like to work with a match moved head,
[8:05] basically.
[8:06] But they do have a free trial on the website.
[8:08] So if you want to learn how to use their software, I believe you can just download it for free.
[8:13] You can even try out in this project and see the workflow.
[8:18] So that's basically how we'll approach the tracking of the shot.
[8:22] And then the other thing I want to say, I guess we'll just create a new row of paint
[8:26] here.
[8:29] Just switch to a color.
[8:31] So one other thing is areas with parallax, we want to treat differently than areas that


### 2D VS 3D [8:32]
**Transcript (timestamped):**
[8:37] have no parallax and that's just going to save us time.
[8:39] So I kind of briefly mentioned that as well in the first video, but so areas like here,
[8:45] this is kind of not completely intuitive.
[8:47] But if you're looking at it, you'll actually see it.
[8:50] So for example, here, we're looking at it pretty much straight on the whole time.
[8:54] There is obviously motion of this, but you know, like if I were to place a 3D crack here,
[8:59] you're not going to feel that much of a parallax difference.
[9:05] Whereas if we're looking more on the like a glancing angle, like over on the side of
[9:08] the face, there's going to be more parallax on those areas.
[9:11] So that's where we would want to use 3D.
[9:14] So we would use 3D more in those areas.
[9:18] So we can actually, once we have the 3D model, we're going to take this area and essentially
[9:22] displace it outwards.
[9:24] So we're going to add actual depth to it and same up here.
[9:28] So we can actually do some depth up here.
[9:30] And these areas are going to actually feel it because there's more kind of rotation happening,
[9:35] whereas this is facing us more directly.
[9:38] So basically these areas will be like 2.5D.
[9:43] So we're kind of projecting onto a 3D model.
[9:48] So it's kind of 3D, but it's still using 2D textures.
[9:52] Whereas these areas are actually truly 3D because we're actually creating 3D geometry
[9:56] from 2D textures, which is basically the same thing as going into CG or Maya or something
[10:01] like that, except we're just doing it in Nuke.
[10:05] Same over here.
[10:06] We use 3D over here because we can actually, really what you want is you want 3D.
[10:13] So you kind of want to feel some slight edge break up on the very edge and you're going
[10:19] to feel the parallax a little bit more because it's kind of on the edge.
[10:24] So I didn't displace it that much.
[10:27] I didn't go like crazy with it if you look at the final comp, but we can get some very
[10:30] slight stuff like this, which gives it a little bit nicer quality.
[10:35] So that's kind of the way I'm breaking down the shot.
[10:39] And of course, we have the rest of the down here, which is 2D.
[10:44] So this is all 2D solution.
[10:49] So this is a very laggy roto paint, but yeah, there you go.
[10:53] So that's kind of breaking down at least the how to approach the shot.
[10:58] So again, I always do this.
[10:59] I don't draw it out, but I do think about this when I look at a shot.
[11:03] I'll look at a shot, think about it, and try to figure out the best solution before I start
[11:08] just throwing solutions at it because you don't want to waste time.
[11:12] This working this way, not being heavy handed and doing the same thing for everything is
[11:18] going to save you lots of time.
[11:21] So that's the setup.
[11:23] Now we'll actually talk about going about it.
[11:26] I'll show you what I did.
[11:27] I'll give you some tips on the Smart Vector and the 3D track.
[11:31] There's already really extensive tutorials on Keen Tools face tracking, so I'll just briefly
[11:35] explain what I did with this and briefly explain the Smart Vectors because like I said, there's
[11:40] really a lot of information already exists.
[11:43] If you're not familiar with these two things, you can find the information and it's going
[11:47] to be a better tutorial than if they were to have a one hour tutorial on Keen Tools,
[11:52] it's going to be very, very in depth.
[11:54] This was actually my first project using this.
[11:57] Their information that they have is really great for that.
[11:59] So yeah, we can take a look at that now and then we'll talk about more of the creative
[12:03] stuff in terms of the texturing of this face.


### Keentools [12:10]
**Transcript (timestamped):**
[12:11] So now we're going to talk about the Keen Tools part here with Face Builder and Face
[12:14] Tracker.
[12:16] So for those of you who want to do the optional part of doing this part of the project, you
[12:22] can definitely go ahead and go to the website and get these.
[12:25] So basically the difference between Face Builder and Face Tracker, Face Builder will basically
[12:29] create the 3D model and Face Tracker will stick it to your footage and track it.
[12:34] So it's really simple.
[12:37] But yeah, if you guys don't have that or you can't get it, we also have the 3D head provided
[12:43] and you can at least see what it's like to work with a 3D tracked model like I said.
[12:48] So we have that here and that will be in the project file, there's actually a collection
[12:55] of nodes at the top that will kind of be given to you in a script.
[13:00] So that's pretty useful.
[13:03] But yeah, let's just briefly talk about what I did here.
[13:05] So basically I didn't have, so basically Face Builder, you can have multiple photographs
[13:10] of someone's face from different angles and you can try to basically model a more accurate
[13:15] representation to the face and this is really useful for.
[13:20] Now I didn't take the time and do that but I did have enough of a rotation in this shot
[13:24] that I can still work with something.
[13:26] So basically what I did was I frame-holded the start of the shot and I frame-holded the
[13:30] end.
[13:31] So we have these two different angles that we can work from which gives us a similar
[13:36] kind of working condition to taking pictures from different angles of the face.
[13:42] So basically all I did after that was I set the frame range of one of these to 170 and
[13:47] then I set another one to 171.
[13:50] So basically what I'm doing with this is I'm using the pen clip and so now if I go between
[13:56] frame 170 and 171 they are one frame apart and that's kind of what the Face Builder
[14:03] is wanting is to have multiple frames in a sequence one frame after the other and then
[14:09] you can kind of build a face based on that.
[14:11] So that's why we're doing the append clip.
[14:12] If you guys don't know this node, you can think of it like DaVinci Resolve or something
[14:18] where you put one clip after the other in a timeline.
[14:22] That's basically what it's doing.
[14:23] So we're kind of freezing this frame putting it on the frame 170.
[14:27] We're kind of freezing this frame and then moving it on the frame 171 and then we're
[14:32] putting them right after each other.
[14:33] So now you see if I go from 170, 171, you can switch between.
[14:38] And then if you do a Face Builder node and you plug it in, you can plug it in here and
[14:45] we'll go to the start frame.
[14:47] All right.
[14:49] And then basically we can just look here, hit align face and boom, we already get a
[14:55] 3D model.
[14:56] So now what you can do is start to line this up a little bit more so you can grab these
[14:59] pins, you can move them over and start to line up the edges.
[15:05] And so this is actually kind of deforming the model more accurately to the face.
[15:11] So if we were to look at this in 3D, that's kind of what it's doing.
[15:15] So some of the chin area as well, something I noticed is you want to grab some of these
[15:19] lower pieces and push them under and then kind of pull the chin down so that you kind
[15:24] of get the pieces, you know, the shape of the jawline.
[15:30] And that's kind of how I went about doing this.
[15:32] So I went around, look at different areas, make sure that they're kind of lined up.
[15:38] And also what's really great about this is face tracker can actually track expressions.
[15:45] So you can actually, you know, track eyelids and stuff like that.
[15:48] I didn't track the expressions on this project because I didn't need to.
[15:51] There's not that much motion going on.
[15:53] But if there's someone talking and stuff like that, you can actually move the expressions
[15:57] independently.
[15:58] You can actually open the mouth and move the eyelids and stuff like that, which is really
[16:02] really cool, especially for moving stuff.
[16:07] So you see I went here and then I will go to the next frame.
[16:10] Let's turn that go to the next frame.
[16:14] A line face.
[16:17] Make sure we go there.
[16:22] Yeah, let's try that again.
[16:25] Line face.
[16:26] All right, there we go.
[16:29] And then it's kind of lined up and then we would need to move this over, make sure this
[16:33] is rotated behind and essentially just go around and tweak it.
[16:43] So the more frames you have, the more accurate this model is going to be.
[16:47] So if you had three or four pictures, which is more how face builder I think is intended
[16:51] to be used, you could probably get a really, really accurate 3D model.
[16:56] In my case, I think I just used two frames or maybe I used three.
[17:02] But now if I switch between those two frames, you'll see that we're starting to get something
[17:06] closer.
[17:07] And then if it's off in some places, you can go back and tweak it and push these points
[17:10] around.
[17:14] And that's kind of how it works.
[17:17] So you see now it's getting closer.
[17:21] But yeah, sometimes you'll adjust it on the last frame, you'll need to go back and adjust
[17:24] it again.
[17:26] So it's really just a back and forth and you just need to kind of tweak those settings
[17:29] and kind of line things up.
[17:30] So maybe the eyelids need to be lower.
[17:33] Maybe this needs to be wider.
[17:38] And so that's how I went about doing it.
[17:39] And it does take a little bit of time.
[17:40] You still need to have some patience and just like any type of tracking, you know, it's
[17:44] not some instantaneous thing, but it is a very, very great tool to have.
[17:50] So after that, you basically will just plug it into a face tracker and you can check out
[17:56] face tracker.
[18:00] And I think I started my shot later on in time.
[18:03] I didn't actually do from frame 200.
[18:07] But basically you go ahead and basically track after that.
[18:10] And it's sort of like any other type of tracking.
[18:14] You have the track tools up here, you can go in, you can adjust the points, you can keyframe
[18:19] them across time.
[18:21] One thing I noticed is really the keyframes definitely help.
[18:25] So you want to set like a keyframe of a pin, go back in time, set another keyframe and
[18:31] then you can refine the track between those two points.
[18:34] And if it's sliding, you work between those two points and adjust it.
[18:39] So that's how I basically went about using it.
[18:41] And that gives us the 3D model.
[18:43] So now we have the 3D model of the head and we can do everything we can do with the 3D
[18:48] model.
[18:49] So this is our head geometry and we have that tracked to our footage.
[18:53] That's being projected onto in this case.
[18:54] But yeah, so that's really, really awesome.
[18:59] And later on in part three, I actually talk about using some of that head for interactive
[19:05] light as well.
[19:06] So I actually use, don't think I mentioned this, but let me just show you because it's
[19:10] kind of cool.
[19:13] So as the cracks appear, we can even use this 3D model to like cast light onto, which is
[19:20] going to give us like those little hints or pools of light on different facing angles
[19:26] of the face.
[19:28] So that would be really hard to achieve just, you know, doing a 2D, you're gonna have to
[19:31] like roto shapes or something.
[19:33] But as the cracks are expanding, I used 3D lights moving with them.
[19:38] So it kind of creates this more realistic effect, which is, let's just go here.
[19:46] Yeah.
[19:47] So you can see it's subtle, but it gives us, you know, all those subtle little layers,
[19:51] you see the nose starts to light up as the cracks are coming and the cheek is lighting
[19:56] up.
[19:57] So we get that nice result because we have the 3D model from FaceTracker.
[20:03] So that's how we went about doing that.
[20:04] The model is there so you can use it.
[20:07] Now I'm gonna talk about the smart vector part briefly, just how we can go about creating
[20:12] it and then I'll talk more in detail a little bit on how we can extend it like I was showing
[20:19] in the draw over.


### Smartvectors and Inpaint [20:22]
**Transcript (timestamped):**
[20:23] So if we look a little bit closer on the smart vectors and how this is done, so there's actually
[20:27] two ways we can do this in terms of kind of extending smart vectors.
[20:32] I'm gonna explain both ways.
[20:35] I actually use both methods in this particular shot because I was getting different results.
[20:40] So basically, yeah, so the smart vector has a little setting here called in-paint map region.
[20:46] And if we take a look at in the smart vector, we view it and switch to the smart vector
[20:51] channel.
[20:52] And if we turn that on and off, we can actually see that it's kind of extending the tracking
[20:58] data from the smart vector.
[21:00] So all of this stuff down here, all these colors, it's basically telling the image how
[21:04] to move in X and Y.
[21:06] So these are kind of the vectors it's generating and it's telling the direction in which to
[21:11] kind of stick the pixels.
[21:14] And so you can plug in a mat here.
[21:16] So I have a roto basically around again the chin area, like we said, where it's kind of
[21:23] overlapping.
[21:24] So basically, I just want to use the tracking data from down here and kind of extend it
[21:27] under.
[21:28] And that will basically just keep it so it's kind of all sticking on the neck if we want
[21:32] to add details under the chin, which is what we do want to do.
[21:36] So that's kind of how you can do it.
[21:37] You just basically go in smart factor, make sure you check that on, check to make sure
[21:41] you have a mat and then you can adjust the mat dilation, which will kind of just erode
[21:47] it in and out.
[21:48] So you can kind of adjust where that starts to happen.
[21:52] So that's the first way you can do it.
[21:53] The other way you can do it, whoops, let me close this.
[21:58] So the other way you can do it is if you want a little bit more control than that, essentially
[22:04] what you can do is render out your smart factor like normal, plug it into a vector distort.
[22:10] So again, if you guys aren't familiar with smart factors, just type it in, you'll find
[22:13] videos on how to just the basics of it.
[22:16] But if we go to the vector distort, you can output a ST map.
[22:21] So if we switch back to normal and just close this stuff, give it a second to load, and
[22:31] it will take a second.
[22:32] So we have our normal ST map.
[22:34] And if you see these colors, it's because the blue channel is solid.
[22:38] So it's not the normal red and green.
[22:40] But actually it's just because there's an extra blue channel, but that doesn't really
[22:43] do anything.
[22:44] So for example, you could just get rid of the blue channel and it's going to look like
[22:49] our familiar pattern here.
[22:51] So it really is just creating a, so if you see this, you're like, well, why is it not
[22:55] the red and green?
[22:56] It is, it's just creating a blue channel, which gives us the perception of kind of these
[23:00] different colors here.
[23:02] But it's the same as the normal one, which is like this.
[23:05] So we have this result.
[23:07] But by actually using an in paint node and a roto node separately, rather than doing
[23:13] it through the smart vector node, we actually have a little bit more control.
[23:17] So you can do that same technique of rotoscoping something and extending it directly on these
[23:24] coordinate patterns, I suppose.
[23:26] So I'll show you exactly how I did it.
[23:29] Down here, I used basically another smart vector and some of the edges were causing
[23:35] problems with the effects area.
[23:38] So if I just go to the comp and I show it, if we go in on this area here, and if I turn
[23:44] that off, I'll just turn it off real quick so you can see.
[23:48] So here's the little in paint node with a roto.
[23:52] So I actually rotoed on the edge of this.
[23:54] If I turn it off and just let it load for a second, you'll see that we can see these
[24:00] pixels stretching.
[24:01] So really all the way around, I was getting the stretching on the edge.
[24:05] And by just doing the roto and kind of doing in paint, you can extend and you see that
[24:09] now it's not stretching anymore.
[24:12] So what's great about the in paint node is you can go in here and see just plug in a
[24:18] source and a mat.
[24:20] And basically the way it works is it just kind of the same same idea.
[24:23] It kind of pushes the pixels.
[24:25] So I would play around with that, play around with the settings.
[24:28] It really, it's very straightforward.
[24:30] You have a direction and an amount.
[24:33] And it's just saying, you know, the amount is kind of how far it's pulling that color
[24:38] and the direction is the direction that it's going in.
[24:42] And so that's why it's kind of nice to do this separately rather than doing all through
[24:45] the smart vector node because you can actually control the direction.
[24:49] If you watch these little lines here, it's kind of hard to see, but you can kind of see
[24:52] you have a little bit more control over that.
[24:56] And you can kind of control like smoothness and stuff like that.
[24:58] So you just have a couple more sliders to play with in terms of like getting that edge
[25:03] to look really good.
[25:06] So there's also tutorials on that on YouTube if you need like a really in depth like every
[25:09] single slider, but rather than focus on every slider, I think it's more important to focus
[25:14] on the methods and where to use these these type of things.
[25:19] So that's kind of how you can approach it.
[25:21] If you're doing the project, you know, you can try to do two different versions.
[25:26] So basically what I did, I just ran out of smart vector with no, sorry.
[25:31] Yeah, I ran out.
[25:32] I think I ran out of smart vector with basically no mat plugged in just like straight up almost
[25:37] the fault settings, high detail and you just run it out.
[25:43] And then you can just start sticking stuff on and then see where the problems start to
[25:46] occur, which is why I saw the chin.
[25:49] I saw the edge here.
[25:51] So I think I use that default render and started to just fix that one in the UV coordinate
[25:59] texture rather than going back and fixing it through this.
[26:04] So one thing to keep in mind is the same rules apply to these UV coordinates.
[26:10] When you render these out, they go to the vector store.
[26:12] So basically you render out the smart vector.
[26:14] It gives you this, run it through the vector store, which gives you, you know, basically
[26:19] this with different colors.
[26:22] And you can pre comp this again.
[26:25] So you can save this out as just a as a picture and that's going to make your sticking stuff
[26:29] really fast.
[26:31] So if you if you were to write this out and save it, making sure you set 32 bit, which
[26:37] is explained in my other tutorials, you're going to get that basically sticking and now
[26:43] you can just put all your textures on and not think about the tracking at all.
[26:46] So you can just go straight into the creative.
[26:48] So that's why I like to do this is the start of the project, just set up all your tracking,
[26:51] do your face to your body area, and then you can just go straight to the creative.
[26:57] So we have this plugging in here and then you can see I'm doing a bunch of ST maps.
[27:01] So basically I'm just taking a bunch of pictures, effects and sticking them through that ST map.
[27:10] And so if we just go up here.
[27:13] Yeah, so that's pretty much it for the tracking.
[27:15] So if you guys are looking at this kind of get the smart factor track, three is done for you.
[27:21] So now we're going to start talking about the 2.5 d enhancement.
[27:24] So just my general workflow for that part.
[27:27] And then I'll start kind of going into the 3d stuff after that.


### 2d Textures [27:35]
**Transcript (timestamped):**
[27:35] So talking about some of the 2d textures.
[27:39] So basically, yeah, if we start going to the cracks now, so we have all our tracking, we can use our
[27:43] smart factors to basically stick stuff.
[27:46] Always keep in mind your reference frame for your smart factors.
[27:49] So that's the frame that you decided that's where you're going to line everything up on.
[27:53] So keep that in mind.
[27:55] So most of this stuff is just color integration now.
[27:58] So it's kind of, you know, just color corrections and stuff like that.
[28:01] But there is one specific trick that I'll kind of show you guys that really helps,
[28:06] especially with, you know, lighting that is changing.
[28:10] So we can see here, I just took a picture and kind of another picture, another angle.
[28:15] I provided you guys some textures and I kind of just rotoscoped some pieces,
[28:19] do some little chunks, paying close attention to the edge.
[28:22] You see that I'm not just doing, you know, if I delete all these little pieces here,
[28:27] that would be very CG looking.
[28:29] You know, you want to break up those edges and try to get something that look organic.
[28:34] So then I do some some stenciling kind of noise patterns and maybe stenciling some rotos.
[28:39] And then basically just sticking that image on in different areas.
[28:44] So you can see that's kind of adding some of these these pieces here.
[28:48] But one thing I did that is a very useful technique.
[28:52] We'll save you a lot of time is we take the original picture.
[28:55] So we have some let me just disable this.
[28:57] I can actually show it over the final here.
[29:01] So we have like this picture, which I've kind of you can see done the same thing.
[29:05] I've kind of just masked it and cut it up.
[29:07] We can see the lighting doesn't really match.
[29:10] I've kind of done some general grays to just get it roughly in place.


### Frequency Separation for Lighting [29:13]
**Transcript (timestamped):**
[29:14] But then I kind of kind of left it there.
[29:17] So one thing you can actually do is basically it's similar to our frequency separation.
[29:22] So I have a video on that and I'm going to do this technique a couple of times in the video.
[29:26] So if you haven't seen the video on frequency separation, you can go to the channel and find it.
[29:32] But basically you want to separate separate out the detail from this original footage
[29:36] and and rather than using the detail, we're just going to use the general lighting
[29:42] and kind of apply it to these textures that we're kind of sticking on.
[29:45] So essentially what we can do is just blur the picture and multiply that onto our texture.
[29:52] So you see that it's grabbing the colors and it's grabbing the luminance from the picture.
[29:58] And we're just multiplying that on.
[29:59] And then when we stick that texture back on, we're saving a lot ourselves a lot of time
[30:05] in terms of color integration.
[30:06] So I'm not having to go here and roto and darken this area and roto and brighten this area.
[30:12] It's already grabbing the colors and doing that for us.
[30:15] And what's great about this is it's dynamic.
[30:17] So as this warps and rotates, this is going to adjust in luminosity across time.
[30:24] So, you know, it's going to change with the picture, basically.
[30:27] And we could we could go in here and make some slight adjustments to make this a little bit better.
[30:31] You see, maybe it's a little bit too bright here and maybe we could go slightly darker here.
[30:37] So we could still do some little manual tweaks.
[30:39] I didn't do any more tweaks after this because, you know, in the final comp,
[30:44] you're not really seeing it anyway, because, you know, it's it's a there's a bunch of effects and stuff.
[30:48] So I was happy with that level of integration.
[30:51] But if you really want to be picky about it, you know, we could probably improve this a tiny bit.
[30:56] But in general, just getting those technique or using that technique, rather,
[31:02] is going to help you a lot because you can see it just makes everything sit together.
[31:08] And maybe sometimes you don't want to grab the skin tones that are underneath.
[31:11] So what you can do if you just want the luminosity is just to desaturate
[31:17] that kind of incoming image and just go like this.
[31:20] You can just pull the saturation down a bit and you're still getting the lighting,
[31:24] but you're not getting the colors.
[31:25] So maybe you're trying to apply something that's a slightly different material.
[31:29] So you wouldn't want to grab the skin tones, but you still want that luminance that's coming from over here.
[31:35] So that's something to keep in mind.
[31:38] So that's how we can use kind of the frequency separation in a different way
[31:42] to grab lighting from or rather integrate pictures into an image.


### More Texturing [31:49]
**Transcript (timestamped):**
[31:49] And then so something like this.
[31:51] So basically the same concept, you know, taking some pictures of cracks,
[31:57] just doing some some contrast and some of so you can see it.
[32:00] Some of this is manual work I did with grades.
[32:03] So when I'm sticking this over, I was just disable all this stuff for a second.
[32:10] If you give a second to load.
[32:11] All right.
[32:12] So if we disable all that, yeah, that's what it looks like basically straight over.
[32:16] So obviously not matching at all.
[32:18] So some of the color corrections I did were just darkening.
[32:25] And sometimes with this luminance trick, obviously, we got some really nasty dark edges after that.
[32:31] But sometimes with this luminance trick, you need to.
[32:35] You need to.
[32:37] I'll do the luminance trick and I'll put a grade before and kind of counter it to just kind of bring the values back up.
[32:45] But here it's obviously all over the place.
[32:46] So obviously some of these other corrections kind of balance that out.
[32:51] But you see that it just gives us a nice starting place to do stuff like that.
[32:57] So yeah, so that's kind of what we did there.
[33:01] Like I said, you could probably blend this a little bit further.
[33:04] Like I said, you could probably blend this a little bit further.
[33:06] Like I'm looking at it now and it's like, OK, well, that looks a little bit too blurry.
[33:12] But usually I design a shot for the final comp.
[33:15] I don't design it for each step along the way.
[33:19] You know, I only care about the final image.
[33:21] I don't really care about, you know, if every single thing is like perfect along the way.
[33:27] So if you can see it, you can see it.
[33:29] If you can't, my opinion, you know, don't waste your time on it.
[33:33] So that's kind of how I approach it.
[33:36] So the next part we can talk about is this same process, but we're going to talk about it
[33:41] in terms of the using some of those techniques on the 3D.
[33:45] So I'll talk about the 2.5 D first.
[33:48] So I'm not going to talk about the effects in this video that will come in part three.
[33:52] So I'm going to skip down here to where we start to get to the face.
[33:57] So we'll work backwards to do the energy cracks in the next video.
[34:04] Yeah, I think.
[34:05] But basically a good way to approach this is at least get all your textures in there.
[34:09] So if you're doing the project, get all your textures.
[34:11] Make sure everything's sticking and then we'll be able to integrate the the cracks later on.
[34:18] So yeah, we'll talk about the 2.5 D cracks first because that's easier.
[34:23] And then we'll talk about the 3D cracks last.
[34:27] So 2.5 D cracks.


### UV Space Head 2.5 Cracks [34:30]
**Transcript (timestamped):**
[34:30] So basically this is easier to do in UV space because we can work flat and we can do some
[34:36] tricks with that frequency separation like I just showed you.
[34:40] So by working in UV space, we're going to do some really awesome stuff with that.
[34:44] So if we flatten out our face, same as the last tutorial posted, you can find that video as well.
[34:51] We take our picture, we project it onto the model and then we render it out into a square
[34:56] format.
[34:57] In UV space.
[34:58] So now we have a flattened face model and this actually moves with the video.
[35:02] So if I kind of scrub through, you'll see that the this face is stabilized, but the lighting
[35:07] is not.
[35:08] So this is really key so you can see that the lighting moves.
[35:11] If I just give it a second to catch a couple frames here, I can show it easier.
[35:17] So we see 250.
[35:19] Here's the lighting 300.
[35:21] Here's the lighting and then we can go to the very end.
[35:24] And see the lighting changing.
[35:25] You see everything is sticking except the lighting because we stabilize the face.
[35:31] So if we hop through, we can see that the lighting is moving independently, which is
[35:37] really awesome because now what we can do is just integrate our textures on the one
[35:41] frame and use that moving lighting to kind of do that same sort of effect.
[35:47] So if we go down here, we can see that the lighting is moving independently.
[35:53] Basically, what I did was I have the face here and I merged the texture over.
[35:59] So let's give it a second here.
[36:02] I think I didn't actually use this texture in the end.
[36:05] I think I merged a different texture over it.
[36:07] So I was just merging a couple different layers of texture.
[36:10] So I've kind of provided you guys those images that you can take and kind of place in there.
[36:17] But again, I'm doing the same type of thing.
[36:19] So I'm taking a base integration, which is this.
[36:22] And then I'm doing that kind of trick to take that flatten phase, do a slight correction
[36:28] maybe to the brightness, but then we're just multiplying it on.
[36:31] And also just to mention in the multiply, you want to make sure to usually just output RGB.
[36:38] It looks like I did RGB on this one, but usually just want to switch the output RGB.
[36:42] So we don't want to affect the alpha.
[36:43] We're really just trying to affect the color.
[36:46] So that might have been a little mistake that I just left RGB, but it doesn't look like it really made a difference.
[36:52] But you can see the difference that just sits in.
[36:55] And what's great about this is by doing it this way, instead of just starting with this picture,
[37:00] rotoscoping where the light is and doing the corrections, this is going to change with the picture.
[37:05] So if I turn it on and I switch frames to the very end, you'll notice that triangle of light that's moving across the cheek
[37:12] is actually affecting our new CG textures.
[37:16] So if we just continue down here, the same concept applies.
[37:19] So we can see I actually covered up some of those textures with a better looking texture.
[37:23] I just thought that the scale looked better and it's more interesting.
[37:27] The cracks are a little bit wider.
[37:29] So just design wise, we can kind of run our effects through and see them a bit better.
[37:34] So I thought that that was just a creative choice there.
[37:38] But same concept, right?
[37:39] So I kind of did a base integration to this level.
[37:42] And then, you know, basically just blurring the picture and then kind of multiplying it on.
[37:51] So you see that that's kind of what it does by blurring it.
[37:53] We're just getting the lighting where we're getting rid of all the detail.
[37:56] And that blurred picture we can just use as like a light map, essentially.
[38:04] And it looks like I did some very small tweaks to that map here.
[38:07] But again, those are just like normal things.
[38:09] If you see something is a little bit too bright, it's not going to give you 100% perfect solution, right?
[38:14] But it will give you a very good one and it's going to do the animation for you.
[38:18] So if you see little things are a little bit too bright, a little bit too bark, you can just, you can kind of just, you know, go tweak them.
[38:27] And again, I didn't run the whole picture back through as a projection.
[38:31] So what I normally do is I work on it in this flat space.
[38:34] And then I go back and I delete basically the picture or either just kind of disconnect it.
[38:41] So the reason I do that is because I only want to take the cracks or the changes I did.
[38:46] And that's all I want to output through that scanline render.
[38:50] So when I'm done with it, this will be your final layer.
[38:53] And if you hit play on this, you'll see that it's like the CG cracks by themselves with the lighting moving on it.
[39:04] So that's basically how you do it.
[39:06] And you just merge this over like a normal picture and that's basically it.
[39:10] So you can merge this over.
[39:13] So we have something like this and we have like CG cracks with lighting.
[39:16] So that's the 2D solution, 2.5 D, I guess.
[39:21] But you can see now if we look at some areas here, this looks a little bit bumpier.
[39:25] We have some specular highlights and some of this stuff looks more 3D.
[39:29] So now I'm going to go into talking about how we can do that, which is a little bit more complicated than what we just did.
[39:34] But fundamentally, it's the same idea.
[39:38] So we'll go up to that area.
[39:42] And you'll notice something I'm doing the way I'm structuring this script is I have my main B pipe going straight down, all the layers going into it.
[39:53] But you'll notice I have this this chain off to the left here and this is my UV face.
[39:59] And the reason I'm doing that is because there's a lot of layers relying on that light map that I create.
[40:06] So I'm creating that face and I'm just blurring it out and then using that same texture for kind of color correcting all the new textures that I'm applying.
[40:18] And I don't want to copy and paste that 100 times.
[40:21] So that's why I keep it off the left.
[40:23] And every time I need that kind of light texture, I can just grab it from the left and kind of pipe it into what I'm doing over in different areas.
[40:32] So this is the 3D part now.
[40:34] So we have basically just more cracks, different textures, stuff like this.
[40:40] We do some color corrections.
[40:42] We scale it down.
[40:43] We do the normal stuff.
[40:46] And then we do our kind of lighting effect here.


### 3D Displacement Cracks [40:49]
**Transcript (timestamped):**
[40:50] But then we start to go into using displacement.
[40:53] So essentially what we can do is we can create a height map from this and we can use this, especially it's just black and white and cracks the darkest part.
[41:01] So actually works really well for this type of effect.
[41:04] So what I did was before I ran this effect out, like this could be the 2D effect.
[41:09] You could run it straight out and it's exactly what we just did.
[41:12] But instead of doing that, what you can do is create a black and white alpha.
[41:17] So if you look at the alpha here.
[41:21] Yeah, so actually we did like a key.
[41:23] So I did some color corrections on it and I did a lumens key.
[41:26] So I tried to create an alpha that's the you have to think of it in 3D, right?
[41:30] So the white parts are going to be pushed out more.
[41:33] The black parts won't be pushed out.
[41:35] And I kind of frame hold that because we don't want it to move.
[41:40] We're in UV space, so we don't want it to move.
[41:43] And we can use this as a displacement map.
[41:45] So now if I plug that into a geo using a displaced geo, so we have our head and then we have a displaced geo.
[41:52] We'll give that a second.
[41:54] Displacement takes a while.
[41:56] So it can be kind of a heavy thing, especially to render out.
[42:00] It will definitely take a little bit of time.
[42:03] You probably have to walk away for 20 minutes or something unless you have a render farm.
[42:07] But if we go in 3D, you can see it's calculating.
[42:13] And maybe I won't let this calculate if it takes forever.
[42:20] Because I have a feeling it's going to take a while.
[42:23] Okay, so actually it's going there.
[42:26] So we give it a second.
[42:31] Usually I try not to look at this in 3D space because it kind of just slows everything down.
[42:35] But maybe if this tutorial, if it'll actually load.
[42:39] But usually when you're dealing with displacement, yeah, best to just stay out of 3D if you can.
[42:45] But okay, so if we can zoom in here, at least we get some kind of representation of what's actually happening.
[42:50] And let's just try to see.
[42:53] So you can actually see that this is 3D.
[42:56] So we're actually creating 3D cracks on the face, which is giving us a little bit of parallax in the cracks.
[43:03] We're going to get these bumps coming out of the cheek.
[43:06] And that's just going to give us a slightly higher quality result.
[43:11] So we get a slight bump coming out just to make it feel more texture.
[43:17] And something else I did was I took that same head.
[43:21] So basically I provided two heads, you guys.
[43:23] I provided one just straight out of Keen Tools that can be used.
[43:28] But then there's another one that comes with a Transform Geo.
[43:32] And basically you just want to keep these two together like this.
[43:35] You want to keep them together.
[43:36] You can place the displacement in between.
[43:39] But as long as you keep those together, it'll be fine.
[43:41] But basically the only difference of this model is it's subdivided, which means there's a lot more resolution.
[43:47] So that these displaced geos will give us nice edges and nice quality.
[43:51] So you need a higher resolution model to do a good displacement.
[43:58] So I basically just went Maya and subdivided it.


### Ambient Occlusion [44:00]
**Transcript (timestamped):**
[44:01] Very simple.
[44:02] You can do it in Blender as well.
[44:04] You basically just go in and use a smooth modifier on your geometry.
[44:08] Same exact concept.
[44:10] So I did the same thing here, but I took the same model,
[44:14] displaced it with the same map.
[44:16] But I rendered out of a ray render with a Amming Occlusion shader,
[44:22] which gives us this map.
[44:24] And this might be a little bit too much displacement relative to the other one.
[44:29] Let me see.
[44:30] I think this one looks like it's a bit more.
[44:32] Yeah, it looks like I might have actually displaced this one a little bit too much,
[44:35] but no big deal.
[44:37] It kind of looks like I just graded it up a little bit, a slight blur.
[44:41] And that's just going to give us some nicer shadows to make it look a little bit more 3D.
[44:45] So we can kind of multiply that over.
[44:50] So what I normally do with the Amming Occlusions, I merge it over a white constant.
[44:54] So you get it on white, and then you can just simply multiply this over your image at the end.
[44:59] So now we have like contact shadows in the cracks that we displaced.
[45:04] So I did that same technique, I think three times on the shot.
[45:07] I have one on the forehead, one on the left side.
[45:10] But they're all using the same method here.
[45:15] Right.
[45:16] So we have that.
[45:17] And we also, if I enable and disable the Amming Occlusion, you see,
[45:20] we just get some slight cracks and stuff like that.
[45:23] We could adjust it more and perfect further, but I think I'm happy with the result in terms of for what I'm using it for.
[45:30] That's the thing, right?
[45:31] Like these shots, you can spend infinite amount of time.
[45:33] I could give myself still 20 or 30 notes on this if I wanted to just keep pushing it, pushing it, pushing it.
[45:40] But in general, you just have to decide when to stop on something.
[45:44] Really like notes you can give endlessly.
[45:47] So I think that's just something to think about as well.
[45:52] It's like what level of detail are you working for?
[45:54] Are you working for film?
[45:55] You're working for TV?
[45:56] In this case, I'm doing it for YouTube.
[45:59] So yeah, yeah, more cracks, same concept.
[46:04] So that's pretty much it for the displacement 3D part.
[46:09] Hopefully you guys understand it again.
[46:10] If you guys are doing the project file, you have email support.
[46:13] So you can shoot me a question and I'll help you out if you get stuck on something, if the video is not clear.
[46:21] So the last thing I want to talk about was the last thing here.
[46:25] We had the crack mats.
[46:27] So one thing before we move into part three is we want to create some crack mats.
[46:33] So basically alphas that represent where all the cracks are.
[46:37] So basically once you've placed all your CG cracks on your face, now we need to create a crack.
[46:42] So we need to create an alpha basically where all those cracks are.


### Crack Matte [46:45]
**Transcript (timestamped):**
[46:47] And one way to do this is actually sort of like frequency separation again.
[46:52] So we have this, if we go back to our flattened head and just give it a second.
[46:59] Actually, you know what, I think it shuffled it dark.
[47:04] Let's just see here.
[47:05] So I have the flat head and then I merged the changes over.
[47:10] So I merged our CG over it.
[47:12] So I basically put this off into its own little stream here and I wanted to create an alpha that represents where all the cracks are.
[47:18] Now immediately, you know, you can see hopefully Lumen's key is not going to work for this because we have shadows, we have highlights.
[47:26] Luma key is not going to pull out the cracks.
[47:29] But if we do frequency separation, it can.
[47:32] So if you blur the picture and we divide it, you see that we've kind of isolated the cracks very quickly.
[47:38] So what you can do from that is do a Lumen's key and then we basically have an alpha that represents a cracks without having to trace over 100 cracks and spend hours trying to do that.
[47:49] So that would not be a very efficient way to create that type of alpha frequency separation.
[47:54] I think it's probably the only way you're going to do it.
[47:57] So knowing that technique is going to save you a lot of time right here.
[48:02] So once you have that, I kind of just remastered by the head.
[48:06] So we have something that looks like this.
[48:08] And then ultimately I kind of just output it through a scanline render at the end there.
[48:14] And so maybe some of these little things were little tweaks in terms of where the cracks appear.
[48:19] So I did some slight adjustments to the mat.
[48:22] Like maybe, you know, we didn't want we didn't want the frequency separation happening in the eyes.
[48:27] We didn't want that as part of that alpha.
[48:29] So I kind of just, you know, stencil out some pieces and kind of go about it like that.
[48:37] But you'll see later on in the next video, we'll use that to kind of basically mask some of the effects.
[48:48] So one thing that probably some people are going to get confused on this is the part of the tutorial.
[48:53] I think people will probably most likely get confused on is this area.
[48:57] So part of the crack mat that's a little bit tricky is the 3D displacement crack mats.
[49:06] Because if we just simply keep it in 2D, like for example here, we're working in UV space in the flattened space.
[49:15] And we did our, you know, creating that alpha.
[49:18] That all makes sense.
[49:19] But what about the cracks that we displaced the model in 3D?
[49:24] This technique doesn't work completely because the position changes after the displacement is applied.
[49:32] So a better way to explain that if I go up to it and look.
[49:37] So if I were to just go into 2D version where I did this, these cracks.
[49:42] So basically I was kind of, let's just go here.
[49:45] I was doing the same thing.
[49:46] I was basically just, let's just create an alpha so I can explain this easily.
[49:54] Let's see here.
[49:58] Yeah, so we have a cracks and basically I was kind of lining those up with, yeah, let me just put an alpha here.
[50:11] Okay.
[50:13] So the way I kind of did it was I was merging it here.
[50:18] That's why it's mixed half.
[50:21] There we go.
[50:24] So that's kind of where I'm pulling in from the left.
[50:26] So I have that flattened face.
[50:27] I keep pulling it in and then add my new stuff.
[50:30] And then I just will use this as a reference as to where these cracks are going to appear.
[50:35] See that this is not actually connected to anything.
[50:37] So I'm using it as a reference.
[50:39] But one problem with that is if we were to just do the same frequency separation to get that alpha, the position changes in 3D.
[50:49] So because it's displacing, these cracks and everything is kind of being pushed around.
[50:55] So actually what you need to do is to create a new channel.
[51:00] So this is kind of advanced.
[51:02] But I have a video about the shuffle node.
[51:05] I think at the end of it, I talk about this specific thing.


### Advanced Crack Matte [51:08]
**Transcript (timestamped):**
[51:08] Where you can kind of store channels in these, you can create layers and kind of store them in here.
[51:14] So essentially what I did to solve this problem was I did illuminance key of the cracks, which is giving us kind of the alpha that we're going to want later on.
[51:23] And I shuffled it in as a new channel.
[51:25] So if you open the shuffle node, you can see how it's set up.
[51:30] So in, I have RGBA and then I created a new channel called crack mat.
[51:35] So to create a new channel, you can go there and hit new and you just kind of hit OK and you'll get all these channels here.
[51:42] And after this node, you'll see that we actually have a new layer here stored, just like the alpha stored here.
[51:49] So that's pretty useful because now if we just go to the end here and we run it through the scan line render just like normal,
[51:56] making sure to check channels to all.
[51:59] So you want to render all the channels.
[52:01] If we go here to the result and then we look, we'll still have that stored here.
[52:07] So if I switch that layer, you'll see we actually have that alpha stored.
[52:12] So that's one way to do it.
[52:14] And the difference with and the reason we have to do it that way is because this displacement is actually affecting this layer.
[52:21] So if I go to this scan line render and just show you guys, I'll give it a second here.
[52:30] So this is probably where people will get confused.
[52:33] You don't have to do this if you don't want to do the 3D displacement.
[52:38] That's up to you.
[52:39] But yeah, I assume this is probably where people get confused because especially beginners when you're doing like shuffle and stuff like that and creating layers.
[52:50] It's kind of an organization thing.
[52:52] And if you don't fully understand the concept, it's kind of confusing.
[52:56] But once you grasp that concept, and that's why I recommend you go check out that shuffle video.
[53:01] It helps understand why we're doing it.
[53:05] And it's not and it's not the only time you'll have to do this.
[53:08] Sometimes you'll have to create a layer before you run it off scan line.
[53:11] It's a very common thing once you start to get into more advanced compositing.
[53:17] So OK, let me just disable the displace to show you.
[53:22] You see that this alpha is actually slightly changing because of this displacement.
[53:26] So that's why we need to do it this way.
[53:29] Because otherwise these cracks, they won't line up with the main layer, which is this layer.
[53:36] They won't line up.
[53:37] They'll be kind of flat because we're pushing them around.
[53:40] So hopefully that makes sense.
[53:42] And then basically what you do is you take this layer and you will go combine it with the full crack matte.
[53:51] So we have like this one that we created and then we add over the cracks that are 3D displaced.
[54:00] So basically like that.
[54:02] And you see I did some weird shuffling here.
[54:05] And basically all I'm doing is shuffling out the crack matte layer.
[54:10] So if you've done CG compositing, it's the same thing.
[54:12] It's like when you have a CG EXR, you shuffle it out.
[54:15] So you're shuffling out that layer.
[54:17] And then all I did was kind of put the alpha and all the color channels just so I could see it.
[54:22] It's just nice to see.
[54:24] And then what I did was copy the original alpha of these, this texture into this layer and pre multiply it.
[54:33] So now we have just the cracks with a solid alpha.
[54:36] And by doing it this way, we can merge this over our final kind of crack matte alpha.
[54:46] So that's kind of advanced stuff.
[54:48] But hopefully that makes sense.
[54:50] And yeah, so in part three, you will be ready if you get to this point and you can get these created.
[54:57] You'll be ready to start putting the effects through, which will be the whole next part where I'll explain how I went about creating these patterns and flowing them through the face.


### Part 3 Stuff [55:00]
**Transcript (timestamped):**
[55:10] We'll do some other advanced stuff as well, which is animating some roto strokes.
[55:16] So I animated a bunch of roto strokes on the 3D face to kind of draw the path.
[55:21] So if I actually look at this and I hit play, you'll see some of these roto strokes, they're actually like drawing up the face.
[55:32] And that will like reveal the effects that we create.
[55:35] So that will all be in the next video.
[55:36] But I think that's good for this video and you guys will have a lot to work on in the meantime.


### END, Hit LIKE! [55:40]
**Transcript (timestamped):**
[55:41] So yeah, that's pretty much it.
[55:43] Hopefully you guys enjoyed.
[55:45] And if you're not already subscribed, you know, subscribe if you like this kind of stuff and hit like if you found it useful.
[55:54] That's pretty much it.



---

## Structured Notes

### Core Technique
Part 2/3 of the flagship series: analyzing a shot region-by-region to pick the *cheapest sufficient* tracking/integration method per area (SmartVector vs. KeenTools 3D face track vs. blended dual-tracks), extending SmartVector data past overlap/edge failure zones with InPaint, using a KeenTools-tracked 3D head to work in UV space for texture integration and lighting-stabilized color-matching (frequency separation reused as a lighting-grab tool, not just a skin-retouch tool), 3D `DisplaceGeo` crack detail with Ambient Occlusion contact shadows, and — the video's most advanced single technique — preserving crack-matte alignment through 3D displacement by shuffling the alpha into a custom channel *before* the displaced geometry is rendered through ScanlineRender.

### Summary
Opens with a **shot-analysis methodology**: before touching any tracker, look at where the footage has parallax/overlap/deformation and route each region to the cheapest technique that will actually hold — SmartVector for most of the body (frame_000, RotoPaint marking analysis zones over the plate), a blended dual-track via ST maps for one problem area with vertical lines and no trackable features, and a full KeenTools 3D face track for the face specifically because SmartVector breaks down wherever there's overlap/parallax (the nose, the chin crossing in front of the neck). A **SmartVector edge-extension technique** most tutorials skip: where SmartVector data is unreliable at overlap boundaries or clip edges, `Roto` off the unreliable region, then either (a) plug that roto as a mask into SmartVector's built-in "in-paint map region" option (with mat-dilation control), or (b) for more control, render the SmartVector out through `VectorDistort` to an ST map, then drive a separate `RotoPaint` + `IPaint`(In-Paint) node pair on the raw coordinate/ST-map image itself — extending track data past the break point with independent direction/amount/smoothness controls the built-in option doesn't expose. **KeenTools FaceBuilder/FaceTracker workflow** (frame_001, live in Nuke's 3D viewer): with only one clip and no separate reference photos, `AppendClip` two frame-holds of the same shot (start and end frame, each pinned to adjacent frame numbers like 170/171) to fake FaceBuilder's expected multi-angle-photo input; run FaceBuilder, hit "align face," then manually drag pins to fit the model to each frame — more frames/angles = a more accurate model. Once built, FaceTracker tracks the model to the footage like any other tracker (keyframe pins at two points in time, refine the track between them) — the result is a UV-space-capable 3D head that stays locked to the plate. That same 3D head later drives an interactive light: 3D lights parented to move with the expanding cracks cast onto the head's actual geometry, producing believable pools of light on the nose/cheek that would need manual roto-shape work in pure 2D. **UV-space texture integration with lighting stabilization** (frame_002/004, flattened face in UV space): project the plate onto the tracked 3D head and render to a flat square UV-space image — this stabilizes the *geometry* but not the *lighting*, meaning any texture merged onto that flat UV image can be relit for free by multiplying in a heavily blurred (optionally desaturated, to keep only luminance not skin-tone) copy of the original plate as a dynamic light-map — as the real light moves across the face over time, new CG textures merged in UV space inherit that same moving light automatically, without hand-animated roto grading. The scanline-rendered result is then isolated to *just the new crack layers* (by deleting/disconnecting the original picture before the final render) so it merges cleanly back over the main comp as an additive CG layer. **3D displacement cracks** (frame_005): key/grade a black-and-white alpha from the flattened crack texture (white = pushed out, black = stays flat), frame-hold it (irrelevant since UV space doesn't move), and feed it into `DisplaceGeo` on the tracked head — used only on higher-parallax/glancing-angle regions of the face where 3D depth actually reads, vs. cheaper flat 2D-in-UV-space treatment on more front-on areas (a repeated theme from Part 1: never use a heavier technique than the shot needs). A subdivided, higher-poly version of the same head (built in Maya, "same could be done with a Subdivide modifier in Blender") is swapped in wherever displacement happens, since low-res geometry displaces with visibly bad/blocky edges. **Ambient occlusion contact shadows:** re-render the same displaced geometry through a `RayRender` with an AO shader, merge that AO pass over a white `Constant`, then `Multiply` it over the final image for cheap contact-shadow grounding in the cracks — repeated on 2-3 separate crack regions using the same method. **The advanced crack-matte-through-displacement problem** (frame_006/007, the video's most technical segment): a straightforward frequency-separation-based crack alpha (blur the flat UV image, divide to isolate high-frequency detail, then Luma-key it) works fine for purely-2D-in-UV-space cracks, but breaks for the 3D-displaced cracks, because `DisplaceGeo` physically moves pixel positions — so an alpha derived *after* displacement no longer lines up with anything, and one derived *before* displacement doesn't reflect the post-displacement position either. The fix: Luma-key the crack alpha *before* displacement, then `Shuffle` that alpha into a brand-new custom channel (not standard RGBA — create a new channel name like "crack matte" via the Shuffle node's channel dropdown → New) on the pre-displacement image, so the alpha data travels *through* the DisplaceGeo/ScanlineRender pipeline as a channel riding along with the actual displaced geometry (ensure ScanlineRender's "channels" is set to "all" so custom channels survive the render) — the resulting output then has a correctly-displacement-aligned alpha stored in that custom channel, extracted afterward and pre-multiplied to combine with the rest of the (non-displaced) crack matte into one unified alpha covering the whole face.

### Key Steps
1. Before tracking anything, walk the footage and classify each region: flat/no-parallax/no-overlap → SmartVector; deforming/no-trackable-features → blend two tracks via ST maps; overlap/parallax (face) → full 3D track (KeenTools).
2. Extend unreliable SmartVector regions (overlap edges, clip edges) with either SmartVector's built-in "in-paint map region" + mask + mat-dilation, or — for finer control — `VectorDistort` → ST map → separate `RotoPaint` mask + `IPaint`(In-Paint) node with independent direction/amount/smoothness sliders.
3. Build a 3D face track without extra reference photos: `AppendClip` two frame-holds of the same shot at different times (pinned to adjacent frame numbers) to satisfy FaceBuilder's multi-photo expectation; run FaceBuilder → align face → manually drag pins to fit per-frame; more frames = more accuracy. Feed the built model into FaceTracker and keyframe/refine pins across time like a standard track.
4. Once locked, use the 3D head for more than tracking: parent 3D lights to move with expanding effects for interactive lighting/pools-of-light on the geometry — far cheaper than hand-rotoing light shapes in 2D.
5. Project the plate onto the tracked head and render to a flat square UV-space image — this stabilizes geometry but leaves lighting moving naturally, which is the property the next step exploits.
6. Merge new CG/photo textures onto the flat UV-space image; grab a **dynamic light-map** by heavily blurring a copy of the original UV-space plate (desaturate first if you only want luminance, not skin-tone color) and `Multiply` it onto the new texture — as the plate's real lighting animates, the new texture inherits that same lighting automatically without manual roto-grading.
7. Isolate only the newly-added layers before the final render: disconnect/delete the original base picture from the chain right before the `ScanlineRender` so the rendered-out result is just the new CG cracks (with inherited lighting) as a clean additive layer to merge over the main comp.
8. For 3D crack detail: grade/key a black-and-white height alpha from the UV-space crack texture (white = raised), frame-hold it, feed into `DisplaceGeo` on the tracked head — reserve this for high-parallax/glancing-angle regions only; flatter, more front-on regions don't need it.
9. Swap in a subdivided (higher-poly) version of the same tracked head wherever displacement is applied, to avoid blocky/low-quality displaced edges.
10. Add contact shadows: re-render the displaced geometry through `RayRender` with an Ambient Occlusion shader, merge the AO pass over a white `Constant`, `Multiply` over the final image.
11. Build a 2D-only crack matte via frequency separation: blur the flat UV crack texture, divide the original by the blur to isolate high-frequency detail, Luma-key that to get a clean alpha — much faster than manually rotoscoping every crack.
12. For crack mattes on **displaced** (3D) cracks specifically: Luma-key the alpha *before* the DisplaceGeo is applied, `Shuffle` it into a new custom channel (create via Shuffle's channel-name "New" option) on the pre-displacement image, ensure the `ScanlineRender`'s channel output is set to render all channels — this rides the alpha through the displacement pipeline correctly aligned; extract the custom channel afterward, premultiply, and combine with the 2D-region crack matte into one unified alpha.

### Nodes / Tools / Settings
- **Core Nuke/NukeX:** `SmartVector` (in-paint map region + mat dilation option), `VectorDistort` (SmartVector → ST map), `RotoPaint`/`Roto`, `IPaint`/In-Paint (direction/amount/smoothness controls), `AppendClip` (fake multi-frame FaceBuilder input), `Project3D`/UV-space flatten-and-render workflow, `Blur` + `Multiply` (dynamic light-map from a blurred plate), `DisplaceGeo`, `RayRender` (Ambient Occlusion shader), `Constant` + `Multiply` (AO contact-shadow application), frequency separation (`Blur` + divide) for crack-alpha isolation, `Shuffle` (custom channel creation — critical for the displacement-crack-matte fix), `ScanlineRender` (channels output set to "all")
- **KeenTools (third-party plugin, not Foundry):** **FaceBuilder** (builds a 3D face model from multiple photos/frames — pin-fitting workflow) and **FaceTracker** (locks that model to footage over time) — a 14-day free trial is available; this was the author's first project using it
- **Reused technique from another tutorial in this KB:** frequency separation, applied here not for skin retouching but as a general-purpose "grab lighting, discard detail" integration trick — same underlying math (blur + divide/multiply), different purpose
- **Cross-app note:** the subdivided high-res head was built in Maya; the author notes a Subdivide/Smooth modifier in Blender achieves the same result

### Difficulty
Expert — assumes working knowledge of SmartVector, ST maps, UV-space compositing, and Nuke's 3D system already; the displacement-crack-matte channel-shuffling technique in particular is explicitly flagged by the author as the part most viewers will find confusing.

### Foundry App & Version
Nuke / NukeX — `SmartVector` and `VectorDistort` are NukeX-exclusive nodes. Version not stated on screen; per this skill's version-tracker, a 2022 upload falls in the Nuke 13.1 (Nov 2021) → 13.2 (Apr 2022) window. Uses only the Classic 3D system (Project3D, DisplaceGeo, RayRender, ScanlineRender) — predates the 14.0-beta USD 3D overhaul.

### Tags
tracking, camera-tracking, 3d-system, projection, channels, grading, digital-matte-painting, advanced

---

## Related Tutorials
- [1/3] Nuke Tutorial Series (Practical SFX, Lighting, Script Overview) (`13-nuke-tutorial-series-practical-sfx-lighting-script-overview.md`) — direct prequel; that video previews this one's tracking/UV-space/KeenTools techniques at a roadmap level, this video delivers the node-level detail.
- Rotoscoping in Nuke Tutorial | 5 Beginner Tips (`rotoscoping-in-nuke-tutorial-5-beginner-tips.md`) and Why your VFX Tracks aren't "Sticking" (`why-your-vfx-tracks-arent-sticking-and-how-to-fix-it.md`) — share `tracking`/`camera-tracking`; both are about disciplined track/roto setup, complementary to this video's per-region tracking-method selection.
- How to DENOISE your CG in POST (`how-to-denoise-your-cg-in-post-blender-nuke-tutorial.md`) — shares the underlying "flatten to UV/projection space, do the hard work there, project back" pipeline shape, applied to a different problem (denoise vs. lighting integration).
- [3/3] Nuke Tutorial Series (Flow Paths, FX Integration, Design) (`33-nuke-tutorial-series-flow-paths-fx-integration-design.md`) — direct sequel; puts this video's tracking/UV-space/crack-matte work to use with the actual energy-effect kitbashing and animated reveals.
- Track Any Surface with This Mocha + Nuke Trick! (`track-any-surface-with-this-mocha-nuke-trick.md`) — shares the theme of picking the right specialized tracker (there: Mocha for planar surfaces; here: KeenTools FaceTracker for 3D face geometry) when Nuke's native tools fall short.
