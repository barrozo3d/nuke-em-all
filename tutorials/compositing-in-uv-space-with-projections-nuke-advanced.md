---
title: Compositing in UV space with Projections | Nuke [Advanced]
source: YouTube
url: https://www.youtube.com/watch?v=F-q8tgk8QCc
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/compositing-in-uv-space-with-projections-nuke-advanced/
frame_count: 0
frame_status: pending-selection
---

# Compositing in UV space with Projections | Nuke [Advanced]

**Source:** [YouTube](https://www.youtube.com/watch?v=F-q8tgk8QCc)
**Author:** Compositing Academy
**Duration:** 44m40s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py compositing-in-uv-space-with-projections-nuke-advanced <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to this tutorial.
[0:11] This is going to be a bit of a longer tutorial.
[0:13] There's going to be a couple of examples here, but we're going to be talking about how to
[0:17] take projections and move them into UV space and a couple of examples of what we can do
[0:22] with that technique.
[0:24] So this is the last example I'll go over, but just to show you guys, it's kind of like
[0:28] this manhole cover flying away and turning into a cloth.
[0:33] So some kind of weird effect and leaving a hole behind.
[0:37] And obviously, our footage is something just like this.
[0:40] So we're kind of taking projections and baking their movement into a moving object.
[0:47] So that's kind of one way we can use these, but there's actually a number of ways.
[0:50] So what I'm going to do is split this video into a couple of different chapters.
[0:55] And so we'll talk about a couple of different things here.
[0:58] But first, if you haven't seen these videos, I recommend you check these out, like the
[1:02] basics, the fundamentals of what are UVs and just understanding those basic concepts before
[1:08] we move into something more advanced like this video.
[1:12] So these are the things we're going to talk about in the first chapter.
[1:15] We'll talk about why it's useful to work in UV space a couple of reasons.
[1:20] So we can blend multiple projections in UV space.
[1:23] We can stabilize, extract textures.
[1:26] So that will be the first part here.
[1:28] And I'll use a shot down here that I've taken with a drone.
[1:31] And then we have another one that is removing perspective and working to the space.
[1:35] So that's another use case for this sort of workflow.
[1:40] And you'll see why that's useful.
[1:41] And then we'll talk about lastly how to bake projections onto an object, which is what
[1:45] we saw just that quick video there and how to patch in high resolution textures into
[1:50] projections if you need to.
[1:53] So there's a bunch to cover there.
[1:55] And yeah, we'll start talking about it with the first one.
[1:57] So if we look at this shot, just to reiterate the basic concept, you guys already know this


### UV Space explained [1:58]
**Transcript (timestamped):**
[2:03] probably, but you know, a basic projection looks like this.
[2:06] We have our footage that's undistorted.
[2:11] And we're basically projecting that onto a card that's been placed in the proper position,
[2:16] you know, which you can determine from the point cloud or the other methods I've talked
[2:19] about before.
[2:21] So you can basically open this up and we can see this is a projection.
[2:24] So if we were to play this footage, and we give it a second here to cash.
[2:31] So you can see Nuke is doing a cash here.
[2:33] And if I scrub through, we'll actually be able to preview the projection.
[2:36] So you can see the projection is rotating on this card.
[2:40] But so what's interesting about this is if you notice, let's just play the footage first
[2:45] so we can see the footage.
[2:46] The footage is this kind of drone shot rotating over this landscape.
[2:53] And there are some kind of violent turns in the footage.
[2:57] So you know, that's something that could actually remove with this technique.
[3:00] You know, you could use a planar track in some of this specific case scenario, you could
[3:04] use a planar track to stabilize and remove motion as well.
[3:09] But I want to cover the 3D UV method because it expands much further what we can do.
[3:14] So so we see this thing kind of turning here.
[3:17] And what's interesting is if you look in 3D space, you'll notice it's kind of stabilized.
[3:22] Like we see the frame rotating, but the image itself is staying in place on the card.
[3:28] And that's because the camera is projecting the image and the image is moving with the
[3:32] camera.
[3:33] But it's happening.
[3:34] Basically, if you place this 3D object or 3D card in the right spot, it's going to look
[3:39] like everything's kind of stabilized.
[3:41] So yeah, it's kind of a glitchy cache here.
[3:45] Hard to play kind of in 3D.
[3:46] That's kind of a nuke's thing there.
[3:48] But yeah, you can see that basically the frame rotates around meanwhile it's staying in position.
[3:55] So one other thing to note with this, if I can fix my cache here, one of the things note,
[4:02] so since this is a projection, obviously if we move this card around, you see that that
[4:06] image is moving around.
[4:07] So it's a projection.
[4:08] It's not in texture space.
[4:10] And this is really a key concept as we move further into this kind of video is you need
[4:15] to understand the difference.
[4:16] A texture, just to remind you guys, obviously if you stick a texture on a card and you move
[4:21] it around, it's not going to move.
[4:24] It's going to stay on the card.
[4:26] So basically what we want to do in this kind of video here is to convert this projection
[4:31] into UV space and make it a texture.
[4:33] And then you'll see the potential of what you can actually do with that.
[4:39] So the way we do this is we take the projection and what we can do in the scanline render
[4:46] is switch it to UV.
[4:49] So there's this little box here if you double click the scanline render and we switch it
[4:53] from perspective, which is the normal result we get from the scanline.
[4:57] So if we were to go back and just look at the normal result, give it a second to load
[5:02] here.
[5:04] If we look before and after, before, after, there's no difference.
[5:08] So we're basically projecting it from the camera, not doing any frame holds or anything.
[5:11] So it really shouldn't see any difference because the camera is just following what's
[5:15] happening there.
[5:17] But if we switch this projection mode to UV, it's going to render out the texture space
[5:23] of the card.
[5:25] So what that means is basically it's looking at the UVs of this card, which is, again,
[5:32] go check out those videos, but we have a square card and now it's just looking at the texture.
[5:37] So basically, that's just something to consider.
[5:42] So it doesn't even matter really where the camera is.
[5:46] So for example, if I move this camera here and we move in UV space, you see it's basically
[5:53] just taking the texture and rendering it out.
[5:58] And basically what that allows us to do is now we're working in texture space.
[6:04] So one thing before I start talking about this, it's useful to when you're rendering
[6:10] in UV space, so in projection mode UV, you want to render in squares because usually
[6:15] a UV layout is going to be at least for, you know, you don't want to stress UVs basically.
[6:20] So you don't want to be changing formats and all kinds of stuff.
[6:23] Really if you're in UV space, you want to be working in squares.
[6:25] So there's two things you need to do.
[6:26] You need to plug in a background into a square format, which is, so I just plug in a 4K square.
[6:32] And I also went to the card and I turned off image aspect.
[6:36] So that's not going to grab the 16 by 9 aspect ratio, which is kind of this wider sort of
[6:42] footage here.
[6:43] It's not going to grab that aspect ratio.
[6:46] So if I click that, you'll see that it actually changes the shape of our card and it makes
[6:50] it not a square.
[6:52] So we don't want to be doing that and switching back and forth.
[6:55] So always just check that off if you're planning to go to UV space.
[6:59] If you're working with 3D geometry, a little bit more complex, you won't need to worry about
[7:02] it.
[7:03] But if you're working with planes, something you need to think about.
[7:07] Okay.
[7:08] So now that we've kind of talked about that, we're in texture space.
[7:11] This is kind of what the workflow looks like.
[7:13] So we have like the projection render into UV space, and then we can do our work in texture
[7:18] space here.
[7:19] And then we can reapply this as a texture rather than a projection.
[7:25] So that might be confusing, but I'm going to go over it.
[7:27] So we'll just talk it through.
[7:29] So what's one thing that we can do with this?
[7:32] So now that this is in UV space, it's kind of stabilized.
[7:35] So if I were to kind of play this through, you'll notice that instead of our whole video
[7:40] rotating, like the original footage, the frame is actually rotating around the landscape
[7:47] rather than the whole thing rotating.
[7:48] So you see nothing's moving.
[7:49] It's kind of stabilized.
[7:51] And this is really useful for kind of like matte painting.
[7:55] So if we wanted to map paint on this landscape, you know, we don't want to work on a footage
[7:59] that's rotating like crazy.
[8:00] We can stabilize it, put it into this 2D space, and we can bring something like this into
[8:05] Photoshop so we could render this picture out, do a map painting on it, and then we can reapply
[8:10] the motion.
[8:11] So that's kind of what we're doing here.
[8:13] So one other reason this is useful is because we can take different parts of the video.
[8:19] So let's say the start part of the video, I have it frame held here.
[8:25] The starting frame, so 1979 is the starting frame and 2100 is the end frame.
[8:30] So you see that there's some different coverage happening here.
[8:33] We have just give it a second to load.
[8:37] We have this one that you don't see the green landscape up here.
[8:41] And then we have this one that has green landscape up here, but it's missing the other side.
[8:46] So what we can do is we could blend those together.
[8:48] So if I do a key mix and blend those two frame holds together, you see now we can see more
[8:53] of the entire landscape.
[8:54] So kind of what we're doing is blending multiple viewpoints of the camera.
[8:59] And we're getting this overall texture of the entire environment.
[9:04] And the reason this is useful is because you don't want to have to paint a map painting
[9:08] from multiple different angles if you don't have to.
[9:11] Sometimes you have to, but by building your map painting out or by building your scene
[9:18] into kind of a UV space if it's possible, like in this case it is.
[9:23] We could do this and now we could just export this or do a map painting directly on this.
[9:27] So we have both parts of the picture.
[9:30] We have it and we could just frame hold this.
[9:32] So this would just be a texture now and then we could reapply that onto the card.
[9:38] So that's kind of the concept.
[9:39] So let's just see exactly what happens here.
[9:42] So if I take a roto paint, let's take a roto paint here.
[9:46] I think I'd have it and merge it over.
[9:50] So I'm going to get rid of the frame holds for now.
[9:52] I'm just going to show a really basic example of sticking something.
[9:55] So basically what I did is I just drew.
[10:00] Let's just go here.
[10:01] So we have this thing we can plug in the roto paint background and then hit the little replace button.
[10:07] That's a really useful trick, by the way, if you guys don't know that if you do that, all it does is.
[10:12] I'll quickly explain it.
[10:13] All it does is if I have a roto paint, you notice that the default format is ultra HD 4K
[10:19] because that's the format the drone footage is in.
[10:22] But you see, it doesn't match our kind of UV space square.
[10:25] So I don't want to go here and reformat and do all this stuff like that to kind of match this format, which is 4K square.
[10:33] So I don't want to worry about that.
[10:34] So all I do is plug in the background here, hit the little replace button and you see it grabs the format from the thing coming into it.
[10:42] And that's all it's doing there.
[10:43] So we can plug that in now and you see now we can easily draw on stuff and it's it's matching the format.
[10:50] I just like to keep these road paints separate rather than keeping them in the stream and you'll see why in just a second here.
[10:55] So now that we've got that, what we want to do is if we render this through the same thing.
[11:02] So basically what you do is you have your projection set up, go into UV space, do your stuff here, map painting, projections, whatever you're doing.
[11:10] And then copy that same geometry.
[11:13] So we have a card and we'll plug that into the result.
[11:17] But you notice we're not using the project 3D.
[11:20] We're not using a projection anymore.
[11:21] We're using this as a texture.
[11:23] So it's going directly into the picture.
[11:25] So if you've done this right and you go through the scan line render, it should map perfectly.
[11:29] So if you compare, let's compare to the undistorted because that's so we have this and we have this give a second year.
[11:37] So you see that the line and everything is matching.
[11:40] And then that would kind of stick.
[11:41] So if I were to play this through, you can play through the sequence here, give a second to load.
[11:46] And now all of our stuff is sticking.
[11:49] And this is pretty big footage.
[11:51] So that's why it's a bit slow to cash.
[11:53] But you guys can see the kind of example there.
[11:56] It sticks as we step through.
[11:59] And that's a good way to work.
[12:00] So one other thing I want to mention is really if you're doing projections and stuff, you don't want to re projecting entire original footage.
[12:10] And because you're going to basically blur it a little bit because every time you put something through a transform or scan line render.
[12:16] You're kind of losing a little bit of detail.
[12:18] So we don't want to take this entire landscape, add our stuff on top and then put it through the scan line render.
[12:25] Rather, what you can do is take the format, the 4k square and we'll paste it here.
[12:31] And then we'll just once we're done doing a work, we'll just switch it to from the mainstream into the reformat here.
[12:38] And so all we're doing is we're only putting our changes out and then we'll merge that over as a layer.
[12:44] And so that's going to be kind of maintaining the original image quality.
[12:48] We're not going to put this entire all these pixels through the whole scan line render.
[12:52] We're only going to take the changes or the matte painting or whatever we're doing and merge that over as a layer.
[12:59] So it's really useful to work this way because we could work in UV space.
[13:04] We can do our work here.
[13:05] But then when we're done, we have all of our, let's say, let's just move this over for a second here.
[13:11] So let's say we have a bunch of, you know, roto paints or stuff going on here, we're merging it over.
[13:17] Once we're done, we can just switch that to reformat and then just make sure, you know, basically like what I said.
[13:23] So that's kind of the concept of the introduction of why this is useful.
[13:28] Basically, it's really great for sticking stuff.
[13:31] It's really great for doing some other stuff.
[13:34] So let's talk about the other examples here.
[13:37] Another example, we have removed perspective and work in 2D space.
[13:40] So this one, I didn't do a 3D track.


### UV Perspective Warping [13:41]
**Transcript (timestamped):**
[13:42] I just took a still image and I just lined up a card into that.
[13:51] So we can see that that's kind of here.
[13:54] So if we zoom in, we can see our kind of tiles here and they're going into the perspective and the card matches the perspective.
[14:03] So if we render that now into UV space, so if you go to normal perspective, let's just show kind of compare.
[14:11] Normal perspective is just going to be, you know, your image projected.
[14:15] But if we switch it to UV, you see that we're rendering basically the top down view of this square.
[14:21] And we are kind of stretching it because this is actually a rectangle.
[14:24] So, you know, one thing you could do if you wanted to be more cautious, you could make this a square because UVs are kind of squares.
[14:34] So you're kind of wasting resolution there.
[14:38] But you could do it that way if you want to keep the proportions.
[14:42] But in this instance, it's fine to kind of keep it sort of a stretch rectangle.
[14:47] But basically what you're doing, okay, so we're back in the 4K square.
[14:51] We made sure to turn off the image aspect and we have this sort of tiles here.
[14:57] And this is a great way to, you know, do some effects or we could change some of these tiles.
[15:03] Maybe we have a picture of a tile.
[15:04] We could just easily put the tile on any of these.
[15:08] And if we were doing this normally, we would have to corner pin a bunch of stuff and, you know,
[15:12] have to squeeze the textures and try to get the perspective and doing it a bunch of different ways and projecting it.
[15:19] It's just annoying, you know, it's not a good way to work.
[15:21] So if you hop into UV space, do the changes here.
[15:25] So we can just take like a texture or something like this, stick it over one of these tiles,
[15:29] and then as we render it back out, you'll see that the perspective is already grabbed.
[15:35] And obviously you could, if there's some defocus and stuff like that, you could chuck it.
[15:40] And you could, you know, slightly match those type of things as well.
[15:44] So you can lower the quality if it gets too sharp.
[15:46] But this is really great because imagine if our camera starts walking up these stairs and looking down at these.
[15:53] This texture is going to work because it's high resolution.
[15:57] Something you'll see is if I were to work in this perspective and I were to project a bunch of different little changes,
[16:03] like if I were to work from here and projecting a bunch of stuff, if we walk up the stairs and look down at it,
[16:10] you're going to see stretching from the projection.
[16:12] And you could project from that top view and that's something you can do.
[16:16] But there are some instances where you want to work in UV space because you'll maintain texture quality and you won't get stretching like a normal projection.
[16:24] So that's just something to keep in mind.
[16:26] It's just, it's basically it's just easier and you can have a little bit more control over texture quality.
[16:32] So that's another example, getting rid of perspective and doing that sort of thing.
[16:37] So now I'm going to go into a longer example here. I'm going to do a quick model build of this kind of piece of geometry to show you another.


### Modelbuild Example [16:44]
**Transcript (timestamped):**
[16:46] Removing perspective and why it's useful because we can actually run textures through
[16:53] different angles. So I'm going to do a real quick camera track here and then I'll continue the video because I'm not going to make a camera tracking tutorial.
[17:02] So I'm just pause here, do a camera track and then we'll get back to it.
[17:08] All right guys, so I've done a real quick camera track and we can see our point cloud here.
[17:12] So I've exported these separately are undistorted and our camera so we can get our undistorted footage and we can get our camera.
[17:20] We don't really need the point cloud.
[17:22] I don't think beyond this.
[17:24] So next thing we're going to do is we'll take our footage and we'll plug in a model builder node.
[17:31] I don't use the model builder that often usually I will export to Maya and just because it's easier to model and sort of do UVs can do it in blender as well.
[17:41] I don't think the free version Nuke allows you to export geo if I'm correct.
[17:47] So you would have to do your 3D tracking blender or something like that to be able to work in 3D outside of Nuke.
[17:53] But that's something to keep in mind.
[17:56] But basically we can just use the model builder here and chuck in the camera.
[18:00] So basically the way the model builder works I'm not going to do kind of a full description of this because there's already videos out there on this.
[18:10] So I don't want to reinvent the wheel here in terms of what exists.
[18:14] But we're going to plug in the model builder and let me just make sure our point cloud is lined up here because it looks like our camera is a little bit skewed.
[18:23] So let me just double check this.
[18:27] Yeah so we have our ground plane.
[18:31] Just fix our camera here.
[18:35] Our ground plane looks like our curve is going vertical so it might actually be correct.
[18:43] So let's just work with it.
[18:45] So basically hop into the camera view and double click the model builder.
[18:52] And we have this.
[18:54] So what we want to do is we're going to need to line up a point here.
[19:02] So we want to create a plane card.
[19:06] So we'll create a card here.
[19:08] We have our camera locked and we're looking through our camera view and we're looking at the model build node.
[19:12] And so what we want to do is chuck in a card and it'll create a card like this.
[19:16] And basically the way it works we just grab the points and we want to line it up.
[19:21] So I'm going to line it up on a visible point so we have a sort of a dark dark piece of dirt here.
[19:27] And then we can just start to match this perspective.
[19:31] So I'm going to find another point that is obvious.
[19:33] So maybe the edge of that rust or something near there and then we'll grab the other corners and start to get it in perspective.
[19:41] And so we'll do something like this.
[19:48] I'm going to put it at the edge of the top of the curve.
[19:50] The curve is a little bit the curve is a little bit curved.
[19:54] So we could be really accurate and model that curve.
[19:56] I'm not going to do it for this tutorial.
[19:58] But if you were doing this as a final shot it's something you probably want to do.
[20:02] So you need to model this kind of accurately if you have stuff happening.
[20:06] So you'll see.
[20:08] I'm just going to move this over.
[20:10] OK. So we have like a marker to compare to.
[20:12] So right on the edge of that black dirt and let's get a marker over here.
[20:17] That we can see.
[20:21] If I move this point we're going to do on the edge of that yellow.
[20:25] Sorry.
[20:27] The red rust.
[20:29] Just grab these purple points here.
[20:31] OK. On the edge and on the edge.
[20:33] So now what we want to do basically just go to a different position in the video.
[20:37] So we'll go somewhere else.
[20:39] You see it's completely off and then we grab the corner and we want to slide that into place.
[20:43] So we want to line it back up where it was.
[20:46] So right on the edge of that black dirt.
[20:48] Let's see if our points over here align and they're off a little bit.
[20:52] So we want to take this point and just move it on the edge and we can compare.
[20:58] So if you help if you hit alt and the left or right arrow keys you can actually jump between your two keys.
[21:04] It's a good way to compare frames so we can see in this example it's a little bit in the rust there.
[21:13] And here it's a little bit off so we would want to just slide that over.
[21:21] Maybe slide this guy over a little bit.
[21:27] So something like that.
[21:29] It's a little bit closer.
[21:35] Let's just double check our other edge.
[21:37] So here we're off again.
[21:40] So just make sure we get right on that point and we can compare.
[21:44] Still a little bit off.
[21:46] So just make sure those two points are pretty close.
[21:50] So this is relatively close.
[21:52] We have a tiny bit of sliding over there.
[21:58] Just make sure.
[22:00] So this is also one of the reasons I don't prefer to model build because it's kind of tricky to do the points.
[22:12] Easier to use a point cloud and sort of model it in Maya.
[22:16] But I think it's sticking relatively well.
[22:20] Good enough for the video and we'll just hop back go to frame 60 and just double check again.
[22:24] So is this sticking?
[22:26] It looks like it's sticking.
[22:29] Relatively close.
[22:31] I think the sides slightly off but it might be also a slightly inaccurate track or something like that.
[22:37] But like I said I'm just trying to demonstrate the concept so I'm not going to try to perfect this track or anything like that or go back.
[22:43] So this is good enough.
[22:45] So we have this piece of geometry here.
[22:47] What you can do is switch to if you go over here.
[22:53] Sorry click off here and we go over here.
[22:56] Let's just make sure.
[23:00] Okay so there we go.
[23:02] We'll hit the edit button and go over here and say what we can do is select edges.
[23:06] So we're going to select a couple of edges here and then just right click and we'll just extrude them.
[23:12] So we go to extrude and just kind of pull these out like that.
[23:18] And we'll do the same thing for up here.
[23:20] So we're going to go to the top right click extrude.
[23:23] Push these out.
[23:25] And like I said geometry is not completely accurate here.
[23:27] What we want to do is if you really want to do this accurately you probably do something like this and then you extrude again.
[23:37] And then you could push it back.
[23:39] So you do a little bit more accurate modeling of the space there.
[23:43] You can see this is totally off but I just want to go through this quickly and demonstrate the idea.
[23:48] So if we scrub through this should stick relatively well and you can see the concept.
[23:56] So we have this piece of geometry and now what do we want to do with this in UV space?
[24:00] So one thing we actually need to do is because we extruded faces the UVs will only be created for the faces that were there by default.
[24:06] So what we need to do is there's actually a little UV editor in this.
[24:11] So if we select faces so let's go to right click and do face selection.
[24:19] We can select some of these guys and you'll see when we select it.
[24:23] Just select the face.
[24:25] When we select it you're seeing the edge selected but you're not seeing the face and that means the UVs are kind of stuck underneath there.
[24:31] And that's like I said we just created that face and that's why.
[24:35] So we can do can drag around and do this.
[24:38] So we can do can drag around here the controls are slightly different.
[24:42] Like I said I don't use this very much but for the tutorial sake it'll be good so other people can kind of if they don't have the full version of Nuke or they don't want to learn another three they can use this method.
[24:54] So what we can do is kind of go here and let's just switch to vertex selection actually.
[25:01] So if we go to vertex selection.
[25:07] We'll go here and yeah so if you grab these points you'll start to see that it's kind of stuck underneath.
[25:13] And so see if I can zoom in here.
[25:15] Do command drag.
[25:17] So it's kind of it's really finicky I don't find the UV editor Nuke that great but it will it will work.
[25:26] So we can just like basically pull the points and you'll see that they're kind of double stacked underneath each other.
[25:34] And then we can kind of pull these out and we'll see that those UVs are kind of fixed then.
[25:40] And that's going to allow us to work better in texture space.
[25:46] So we have that and then again on the top we extruded some faces.
[25:50] So we're going to need to pull these out.
[25:53] And there should be actually another vertices here because we extruded twice.
[25:57] So you'll see that there's sort of doubled up there.
[26:01] So the way I'm going to do is like this.
[26:03] So just kind of un un pull these out.
[26:09] And I'm trying to make the UVs relative size to the actual size of the geometry.
[26:15] So what I mean by that is you see that I made this piece much thinner than these ones.
[26:20] So I'm making the UV thin sort of like that the same proportions.
[26:24] So if we run a texture across it it's not going to stretch.
[26:32] So we can go here and just kind of pull these out.
[26:40] So if you were to do this in Maya it would be much faster because you can do planar projections.
[26:44] You can do I mean you can do UV projections in Nuke but not you know.
[26:50] It's not that it's not that good of a workflow I think you know sometimes it's better to just
[26:56] like you know I'm not I'm not somebody who believes in sort of just doing everything in Nuke.
[27:04] I use whatever tool is the best for whatever it is and Nuke is great for a lot of stuff.
[27:10] But if it's some if it's really fast in another software easily I'll just hop in there.
[27:14] Takes 30 seconds to import our geo and do it that way.
[27:20] Okay so we have something like that we've unwrapped the UVs and then we can select these and we want
[27:24] to squeeze these down into the zero to one UV space. So kind of have something there.
[27:32] And okay that's good. So now what we can do is take the model builder take the selected geometry
[27:37] and bake it out. So now we have a card in the shape of all the stuff that we just did.
[27:43] So we close the model builder double click the card just to check it out and we have it there.
[27:49] So my axis is kind of weird in the world. My world axis is kind of tilted. I didn't fix it in the
[27:53] track there. So you know ideally if you're doing this final production you want to orient your world
[27:58] the y-axis with the the real world but this will be fine. It's not not a big deal. So we'll take
[28:06] this and now what we're going to do is project 3d. So we'll take the same camera we're going to
[28:11] project the same footage and plug it into the image and now we'll see that we have our curb
[28:16] in 3d here and let's just make sure our frame range. So the project settings are set to that
[28:22] drone shots. You'll see that a couple times through this tutorial we're going to keep going to this
[28:27] weird frame range but the frame range of this video is 50 to 99. So the frame ranges are different.
[28:34] So one way you can do that is to set the frame rate put a frame range node and plug it in
[28:41] and then every time you view it let's just set the frame range to the actual footage. So if we
[28:46] look at the footage you see when we're looking at the footage if it's set to input it's 50 99.
[28:51] So I'm going to set this 50 to 99 and then every time I look at that frame range is automatically
[28:56] going to jump to that correct area that we're working in there. So normally if you're doing a
[29:03] shot your settings would be set to the frame range of the shot but we have multiple different
[29:07] examples in the script so that's just something it's a little bit annoying but something you have
[29:11] to work with. So now we have this projected out so now we're going to go back into the concept
[29:18] we were talking about earlier which is UVs. So I'm going to copy the original footage down here
[29:23] and in this scan line remember we want to put it in a square it's just going to be easier so I'm
[29:30] going to reformat it to we'll say I'll just say square 2k we can do 4k square as well
[29:37] square 2k and then switch the mode to UV. So now we have the UVs unwrapped and we can see that we
[29:45] have this curve removed all the perspective of all the curves and everything like that. So
[29:52] what we could do is we could take a roto paint node and again replace format merge it over
[29:58] and take the brush thing here roto paint and we'll just take the brush and what I'm going to do
[30:10] is I'm going to take a stroke and just draw it straight or kind of straight if I can draw a straight
[30:14] line. So that's good enough we'll just do we'll do a crooked straight line and so what we'll do is
[30:24] we'll go to the start frame of that also one thing we're gonna that might help us actually yeah
[30:31] we want to make sure we set the life to all so all frames there so if we kind of scrub through
[30:37] it's gonna go there. So what we want to do is go to the start frame I'm going to go to the
[30:43] roto paint node and set the stroke to zero so right on end set key at zero and then at the end
[30:50] I'm going to set the key to one so what is that going to do it's going to make it that this stroke
[30:55] kind of draws down the surface and now I'm going to reapply this as a texture so we go back here
[31:03] again we don't want to reapply the curb texture so once we're done using it as a reference
[31:08] we just want to grab the format and then apply the geometry so we can put the geometry back on
[31:16] and put the scan line back on we don't need to set a background actually let's just check here I
[31:24] don't think we do but let's just check should go to the right format okay so yeah this this footage
[31:33] is 1080p so one thing you want to do is in our in our final thing here we'll want to reformat that
[31:41] to 1080p so this is the downside of working with multiple footages of different resolutions in one
[31:50] script because if you don't plug in a background here this the scan line render basically all the
[31:57] nodes in nuke if you guys don't already know this if I create a roto node by default it's going to 4k
[32:02] because that's my project size if I don't have a background plugged in here by default it's going
[32:06] to 4k because that's my project size so I have to plug in a manual reformat here
[32:12] because my project size doesn't match my original footage so okay we have this stroke here and then
[32:19] we merge it over and then let's see what happens so we have it here make sure we set the scan line
[32:26] to perspective so we're going from UV to perspective and now we can see what happened so we we went from
[32:34] UV mode worked in UV mode we did an animated roto stroke we just do it straight down
[32:41] and then we converted it back to perspective and now the roto stroke follows the geometry so if I
[32:45] play this you'll see that that animation will follow the actual geometry that we've modeled
[32:52] and it might not stick perfectly like I said I didn't spend a lot of time you saw on the model
[32:56] builder the track it's really just to demonstrate you can see it's sliding there a little bit but
[33:01] it's really to demonstrate how this is useful and things you could do with it so imagine if you
[33:07] wanted a if you wanted to composite a crack you know like an actual crack we could take a texture
[33:14] and crack it down this concrete wall and have it like splitting open or something like that
[33:20] that's this is kind of a one way you could do it you could kind of have that geometry
[33:25] get rid of the perspective and then that's going to make your texturing so much easier because
[33:28] you can just make a crack it's straight you can design the edges of it and you're not having
[33:33] to grid warp and do a bunch of stuff like that you're just working in UV space so
[33:40] you could put a little glow on there and then there you go that's there's your tutorial so
[33:46] that's basically all of those concepts now that we understand hopefully understand basically
[33:54] the main idea is just this if you guys can just remember this
[33:58] go to UV space do it here go back to perspective that's really a really powerful technique so
[34:04] here's the advanced I wouldn't say it's that advanced but it's just something up through together


### Baking Movement [34:08]
**Transcript (timestamped):**
[34:11] of this kind of manhole thing the thing we started with here it's the same exact idea except now
[34:17] instead of just using stationary geometry we're actually using an animated olympic geometry so
[34:25] what i've done here for you guys is i've created an end cloth simulation in Maya and i've exported
[34:31] it as an olympic so what does this look like it just looks like this we have this sort of
[34:39] i don't know cloth simulation i just took like a circle and kind of turned it into a cloth
[34:45] so this is imported from Maya and yeah so we can work with this and bake a projection into the
[34:52] motion so i'm just gonna walk you through real quick and if you guys want to do this project i
[34:57] kind of set up here so you have like the three pieces of geometry that this scene requires
[35:03] which is the animated thing we also have a sort of the ground around so we can do that for some
[35:10] shadows and stuff and then we also have like a tunnel sort of basically just a cylinder going down
[35:17] so that's some assets you guys can play with and i'll just walk through my comp now and yeah
[35:25] so we have the scanline render let's go to scanline render
[35:31] so again first things first
[35:34] oh sorry we'll go to the top one here so first things first we have our thing and again projection
[35:41] mode uv in this case i didn't reformat it to a square um i probably should have but it doesn't
[35:49] matter that much but it's just better to do it that way and what i've done is i frame hold it on
[35:54] the first frame so we have we can see that the texture lines up there so that's what it is
[36:00] and i've done some paint so i've kind of removed um some of the highlights on this thing because
[36:07] i wanted to animate the highlights so i wanted to make it a really flat texture uh the frame
[36:13] range thing again is just the fixing the thing we said it's just kind of fix it when i'm viewing it
[36:17] it just sets our frame range properly and that i've reapplied it as a texture so again uv space
[36:24] do your changes uv space do your changes go back to texture space and now we see that if we play
[36:35] it's going to take a little bit to cache here i have a lot of stuff i probably needed uh actually
[36:39] empty my cache but if we basically play through um that texture that manhole is going to stick
[36:49] now so that texture actually sticks to that geometry in the proper way so let me go here
[37:00] i'm just going to change my project settings here quick so it's easier for this example
[37:05] because it keeps uh going to the wrong frame range so yeah it's basically sticking now and
[37:12] what else can we do with this so uh the reason this is rendering so slow is because for the final
[37:17] render i switched the anti-aliasing to high so if you turn it off uh you see some kind of nasty
[37:24] edges so we want to switch that to high when you're done with comp it's not even giving us that good
[37:29] of edges there um so you can do some stuff to fix that as well but uh some other things i did with this
[37:37] i took the same geometry and uh i rendered out a kind of specular pass so one thing about
[37:45] projections that make them look fake as soon as you start moving them around is that if you move
[37:50] an object around you're going to have reflections moving on the surface of that object it's not
[37:54] just going to be a flat picture that just doesn't react to the environment so one thing you can do
[38:01] is if i step through here i took that same geometry and i applied a basic material to it
[38:07] um and the basic material has some settings here like diffuse and specular um and so i just
[38:12] wanted to get some of those nice specular highlights on that cloth as it flies away
[38:17] and that we can actually kind of just uh use here so i did a multiply which just gives it a little bit
[38:25] of shading um basically so i really should just drop the quality of these i'm gonna turn off the
[38:33] motion blur and everything so i can kind of show this video faster because uh i don't know what
[38:39] want to wait around for that so i'm gonna turn off the motion blur so it'll just render it faster
[38:45] and so you'll see that this is actually uh doing this uh i guess i use this more for like a slight
[38:51] shadow rather than um the specular highlights so i did uh i kind of gained it so we just only get
[38:59] these shadow areas and everything else is white and then i kind of just multiplied that so what's
[39:04] that's going to do is create some slight shadows on the inside and this is where i did the spec map
[39:12] so here's the actual specular one it's the same concept so i have the geometry uh let's plug it
[39:18] in here so basically i have a the geometry plugged into a fog which is basically just a specular type
[39:25] of texture um that looks like this so it's catching all these weird highlights and then i'm masking that
[39:31] through the actual highlights of the texture so we have the manhole and i do a luma key of the
[39:37] manhole to kind of get the little metal pieces and i just mask that through the fog texture
[39:42] and what that's going to do let me just turn off the motion blur again so we can actually maybe play
[39:47] quickly um so now that's going to give you these like rolling highlights on that projection and it's
[39:53] going to make it feel more real than if we just if we just project that still image onto a warping
[39:59] geometry you're not going to get those nice little moving highlights and that's what makes
[40:05] things feel real so you can see that something like that is much cooler for an effect so yeah if
[40:14] you guys look open the script it's available for download description it's just a light and a fog
[40:19] in the geometry so you guys can dig through and sort of play around there so now what do we have
[40:25] we have something that looks like this uh it's still a little bit flat but we still have some
[40:31] nice highlights and some interaction going on there uh the last thing we could do is um
[40:38] you could add some ambient occlusion so here we can just take a multiply and render out ambient
[40:45] occlusion pass so the way you do that uh constant ambient occlusion geometry and array render so you
[40:52] can just stack those together and you can render out this ambient occlusion pass uh and multiply
[40:58] it against it so you're going to get those inner uh self-contacting shadows which is going to make
[41:03] it look even more real as it's bending so you start to get some inner shadows there and it looks better
[41:13] so it's going to really give you the ripple effects and yeah that's basically it um
[41:18] so we'll go here let me just double check
[41:25] looks like i actually turned my ambient occlusion maybe slightly off in my render so maybe i
[41:32] actually add a little bit back my final render looks like a left off the ambient occlusion let's just see
[41:41] yeah i might have actually taken off the ambient occlusion because i thought it was a little bit
[41:44] much um it looked sort of like making it look a little bit mushy um so you know you can take
[41:51] the ambient occlusion and like play it way down um or something like that might be nice some slight
[41:59] ambient occlusion there um so yeah that's basically it uh the other things here
[42:07] it's just the manhole thing so basically i just took the other geometry which is the tunnel
[42:12] and we don't do any projections or anything we just use it as a normal um sort of thing here
[42:20] and we just apply texture so i just took a concrete texture so i took like a concrete wall
[42:25] from unsplash just free roti free stuff um i kind of shifted the top because i wanted to create like
[42:31] an edge of where the concrete is so if you look at like where the concrete is um basically what i
[42:38] did here was i kind of shifted it to create like a fake metal uh ring just to give it some more depth
[42:45] because this looks a little bit fake when you have that kind of uh perfect cg edge so you want to get
[42:50] that uh layer of texture there um so yeah just a bunch of color corrections to make it look like
[42:57] there's some light coming in um and then you know other stuff here just to make it kind of more
[43:05] interesting and of course you can do a shadow as well so i just rotoscoped a circle when that
[43:13] thing was kind of nearby and fake a shadow as it's passing over and then this is kind of the same
[43:22] thing i render another ambient inclusion pass just to fake some more shadow and then you get
[43:29] this which if we play you know looks like this
[43:36] so yeah that's pretty much it um i don't know if i should re-add that ambient inclusion or not maybe
[43:42] it might need it back um might have let it off in the final render on accident there but i think it
[43:49] probably looks okay without it um i don't know this is this is the problem being sort of a
[43:55] perfectionist you can go you see a million different things this is nowhere near perfect


### End [44:00]
**Transcript (timestamped):**
[44:00] it's really just a youtube example but hopefully you guys have gotten a lot of video the script is in
[44:05] the uh description below um so the reason i wanted also this video just to end this uh this video here
[44:12] is i'm doing a much longer tutorial that involves pretty much these techniques and some of what i
[44:18] described here and it'll probably be like an hour long tutorial on youtube sort of a mini class
[44:23] out there for free and that's what i'm working on right now so that should be out in the next few
[44:28] weeks here and that's gonna be really cool uh something that you could put in your demo
[44:32] reel even so uh that'll be coming and yeah thanks so much hit like if you liked it subscribe uh that's
[44:38] about it



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
