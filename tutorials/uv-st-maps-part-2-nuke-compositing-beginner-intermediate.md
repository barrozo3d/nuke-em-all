---
title: UV / ST Maps [Part 2] | Nuke Compositing [Beginner / Intermediate]
source: YouTube
url: https://www.youtube.com/watch?v=0A-DC41U09M
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/uv-st-maps-part-2-nuke-compositing-beginner-intermediate/
frame_count: 0
frame_status: pending-selection
---

# UV / ST Maps [Part 2] | Nuke Compositing [Beginner / Intermediate]

**Source:** [YouTube](https://www.youtube.com/watch?v=0A-DC41U09M)
**Author:** Compositing Academy
**Duration:** 18m26s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py uv-st-maps-part-2-nuke-compositing-beginner-intermediate <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Introduction to ST Map Expression [0:00]
**Transcript (timestamped):**
[0:00] Part 2
[0:05] Part 2 of the UV ST map tutorial. Sorry, it's been a couple of weeks, I've been pretty busy,
[0:12] but more content will be coming a lot more in the next few months here. So this is kind of our
[0:18] part 2 to this video. I hope you guys have checked it out. This is UV, basically part 1 for the CG
[0:26] objects and how we can use it. And you might recognize this pattern here, this green and
[0:30] red that you saw wrapped around our CG objects. So we're going to actually take that concept and
[0:36] just do some of the things that we can actually do in 2D with this. And we don't actually need any
[0:41] CG rendered out for this. We can do it a lot with an expression node and a couple of different things
[0:46] we can do that are kind of interesting with it. So if we get straight to it, we have an expression
[0:51] here and the way we create this basically pattern is with this expression. So if you put in parentheses
[0:58] x plus 0.5 divided by width and we see that that's going into the red channel and y plus 0.5 divided
[1:05] by height and essentially what that does. So if we take out, if we look at the red channel and the width,
[1:10] so I hit R on my keyboard and check out what's happening, we can see it's creating a 0 to 1 ramp
[1:16] in the red channel. And if you look at the green channel, which is the y and the height,
[1:22] we're seeing a 0 to 1 ramp being created in the green channel. So naturally we get a red and green
[1:29] kind of combination, which is creating the yellow up here. And that's what that's doing. And you're
[1:34] asking, well, what is that doing exactly? It's just creating this picture. Essentially, the way you
[1:39] want to think about this is it's a 2D coordinate grid. It's telling Nuke where pixels are on this
[1:45] pattern. So if we just pull the picture really simple, just like a x y grid like this. Basically,
[1:52] if we are to create this pattern, and we move some of the pixels, it's going to understand how to
[1:59] transform them. So if that's confusing you, we're going to show it in just a second here. But that's
[2:05] kind of what this is doing. So we have that expression. And now we're going to go and see
[2:10] what we can do with it. So if we have a normal picture, we just have a grid here, close this
[2:15] stuff. And we have that expression over here, which is creating a UV coordinate. Basically, if we
[2:25] apply a transformation to our coordinates, so I took a grid warp here, and I just kind of pulled
[2:31] some of the points like this. And then I've applied a transformation and kind of scaled it up and just
[2:37] rotated a little bit. If we plug that into the ST map, we can see that's actually being applied
[2:45] to our grid. So even though these two effects here are going on this picture, it's being applied to
[2:54] basically through this ST map to our grid. And you might be asking a question, well, why can't I just
[3:00] copy these and just plug them directly into the grid. And you can actually gives exactly the same
[3:06] result. So in this instance, it's not that useful. But it demonstrates exactly how it's working. So no
[3:11] matter what we do to this picture, it's going to be applied to our secondary or primary source.
[3:19] So furthermore, we can look at how this actually starts to become useful. So we have this picture


### Blending Morphs [3:22]
**Transcript (timestamped):**
[3:26] here, which is the same way we've been starting with, and another one. And what I've done here is
[3:31] applied some basic warps to them. So I've kind of shifted, you can see these dots here, I shifted
[3:36] them upwards. And if I open this grid warp, I've shifted these ones in right in the direction.
[3:44] So now what you can actually do is apply the ST map. And we see that this warp is being applied.
[3:51] But what I've done is put a dissolve between the two. So right now it's only looking at this one.
[3:56] But as a dissolve animates, so I set a keyframe at zero, and I set a keyframe at one on the frame
[4:01] 30, we can see that if I scrub between the two, we're actually morphing between these two
[4:08] transformations seamlessly. So that's really useful because you could do a complex morph,
[4:15] have all of your predetermined positions set and kind of dissolve between a whole bunch of them.
[4:21] So you could have another one here, I could plug in this, and, you know, keep dissolving
[4:27] all the way between the three or four or infinite positions that you have.
[4:33] So that's a really awesome way that you can use that. Further, you can, and probably the most
[4:38] common use of these UV coordinate images, is bringing in or saving lens distortion profiles.
[4:47] So if you guys have done CG composing, you know that we're pretty concerned with
[4:51] matching or removing, let's say, lens distortion from footage, or applying a lens distortion to
[4:57] a CG object to match the footage. So if you're solving a 3D track in another software, and there's
[5:04] other software like 3D equalizer, synthized, Blender, they all have this feature, you can remove
[5:11] or solve the lens distortion, and it will actually give you a picture like this, which is the
[5:17] UV coordinates with that warp applied to it. So to give you a visual understanding, we have a
[5:24] checkerboard here with a simulated lens distortion, you can see that the lines are starting to curve
[5:29] around the edges. If we have it off, you can see they're straight, and we have it on, you can see
[5:34] that it's distorting around the edges of the frame. If we were to solve this camera in another
[5:40] software, it might give you a picture like this to export. And essentially, if we were to plug it
[5:45] into an ST map afterwards, we can see that it's removing that lens distortion. So it's basically
[5:52] doing exactly what we want. So that's kind of how these are useful. And if you start doing tracking
[5:59] other softwares, or you're getting potentially from another match move artist or someone who did
[6:05] your track, they should be supplying you with something for the lens distortion. That looks
[6:11] like this, most likely, unless they can export the actual numbers, which is another way to do it.
[6:16] But that's just to demonstrate how that's kind of used. And here's another way that it's kind of
[6:21] interesting. We have a basic grid here. And I basically all I've done is just taken the same
[6:28] expression and kind of blurred it. But I blurred it through a noise pattern. So we're actually blurring
[6:34] the coordinate system through a pattern. And if we look at the ST map, we can actually see that
[6:40] we're getting this like crazy, weird effect, so that you could create some holographic effects or
[6:45] you know, other stuff like that. And you can blur in the X and Y differently and stuff like that.
[6:50] So you could come up with different ways to use this. And if you guys have other creative ways,
[6:56] by the way, I'd love to hear in the comments, I'm sure other people would as well. So feel free to
[7:00] to post it there. But if we just check out the ST map, that's what we're getting. But if we do the
[7:04] same effect without the ST map, we see that as giving a totally different result, because one is
[7:09] doing this to the image. And one is doing it to the coordinates of the image. So that's, that's
[7:14] how to think of it, basically. So the last way in the most useful way, this is something that
[7:21] probably seniors can even benefit from, or intermediate composters, I suppose, but this is
[7:28] really useful. And I use this on pretty much every CG environment scene that I'm doing. Because I like


### Projecting ST Maps [7:29]
**Transcript (timestamped):**
[7:34] to work in a kind of lightroom style, in terms of composing, like it's kind of just like doing
[7:40] my color grades and stuff like that in a creative way. And so if we have a basic CG scene like this,
[7:47] and you want to apply some color corrections to it, some secondary grading. If we just check
[7:52] out the camera move first, I'll just let it play here, we have this kind of establishing sort of
[7:57] shot kind of a helicopter, you know, flying over an environment type of shot. So it's a wide angle.
[8:05] And we can see, I'll just let it cash all the way through here.
[8:11] We have a scene like that. So if I were to want to do a bit of secondary grading and direct your
[8:17] eye in a certain direction, maybe there's some subject matter, such as maybe this is a character
[8:23] walking up to an important object in our scene. And I want to end, you know, basically like a
[8:28] concept artist, you know, your eye is always going towards the brightest thing in the scene. And maybe
[8:32] we want to just make this area a little bit brighter. And maybe this area is a little bit less
[8:36] important. So we want to darken it so you're not looking over in this basically empty area.
[8:43] And of course, we can just do that with roto shapes, but those roto shapes need to stick to our
[8:47] scene as the camera is flying through like this. And a normal way that a lot of people are doing
[8:54] it and it's totally fine for most instances is just do sees a card, card 3d. So you have like a
[9:00] card and you put a roto shape on it. And you plug that into a camera and then you could kind of draw
[9:05] your shape and it's going to stick in the scene like that. But sometimes you want your your your
[9:11] alphas to actually have the same perspective and actually stick to the CG in whatever shape that
[9:18] it is. And that's why this is really useful. So if I just show you the problem here, if I go to the
[9:23] end of this comp, I've done some color corrections. So if I go before and after a couple of these,
[9:28] you see I've kind of brightened this area a little bit, keyed out the highlights and brought them
[9:32] up just a tiny bit. And then I've just darkened and done some secondary grading, which is kind of
[9:36] creating a natural vignette effect, and is kind of drawing your eye in the direction of the subject.
[9:43] So we're looking in this direction because we have a little bit more bounce light on that
[9:47] hill and a little bit less light in this area. So that's fine. That's all good. But if we scrub
[9:54] through, we see that that's not working. And we can see that there's some weird colors floating
[9:59] around. And that's because our mats aren't tracked. So like for example, this roto shape,
[10:04] it's basically just not sticking. And that's not what we want. So we're going to go back to our
[10:09] technique and create this expression. Same thing. But what you can do beforehand, we're going to
[10:18] basically project this onto a 3d scene. So if I look at the 3d geometry, this is the same geometry
[10:25] from that render. So we have the 2d render, we also have the 3d scene itself. So if I kind of
[10:30] zoom out here, it's a little bit hard to tell. But this is the same scene that we were just looking
[10:34] at. So we can see the spheres here. If I zoom down, you can see some spheres and all those little
[10:41] objects that were sitting there. So this is the same scene as this. And what we want to do is
[10:49] project this pattern onto that scene. And as we know, this pattern stores the movement of whatever
[10:57] it's doing. So if we project it and stick it onto the scene, essentially, we'll be able to just stick
[11:03] any roto shapes we want anywhere we want. And have a lot of flexibility and speed, which is the most
[11:09] important thing. So essentially, what I've done here is create the expression. And we want to put a
[11:14] crop beforehand, and put the crop beyond the borders of the frame. And what this does is actually
[11:21] gives this pattern a bit of over scan. And that's going to help when we project it, you'll see what
[11:27] I'm going to do in a second. I'll demonstrate. But we want that crop beforehand pulling out. And you'll
[11:32] see that dotted line on the outside of the frame if you hit Q on your keyboard to make sure you have
[11:36] the overlay. Another thing we want to do is make sure it has a solid alpha. Because we're projecting
[11:42] it, it's important to have a solid alpha. So I've basically just created a shuffle node and put the
[11:48] alpha to one by pressing that little white button there. So now if we look at that in the 3d view,
[11:54] it's not the best representation, but we can see this pattern is sort of being projected.
[11:59] One other thing to note is to make sure you guys have the crop off for the project 3d. So
[12:07] if I look through the render view, and I hit tab, we can see this is what this is doing. And if I
[12:13] just zoom back a couple frames, so I just kind of scrub back, we can see that pattern is basically
[12:20] extended beyond even what the camera was seeing on the frame that projecting on. So we're projecting
[12:25] on frame 89. If I go back to frame 72, we'll see actually beyond what that camera is seeing. So one
[12:32] important box to check off is the crop. So if I turn that back on, this is by default. So you see by
[12:38] default from the frame 89 looks great. You know, we're getting our pattern projected. But as soon
[12:44] as we zoom back, you know, we can't have our roto shapes going beyond the edge of that projection,
[12:51] which is not what we want. We want to turn that off. And we also want to project only on the front
[12:55] of the geometry. And the last thing, don't have any of these set because you'll get some weird
[13:01] kind of artifacts and stuff like that. So that's how you do it front, turn off the crop, and make
[13:07] sure you have this crop. So we have that over scan, you see if I disable this. Actually, you can't
[13:13] really tell visually, but basically, the math is not the same exactly. So it's like stretching the
[13:19] pixels versus having a detail outside of the frame. So just make sure you have that and this.
[13:26] And now that if we pre comp that out, we're basically done. So now we have this pattern,
[13:30] and I can scrub really fast now, you see that because this is pre comped, we can scrub really,
[13:35] really quickly. And it's not using a 3d, it's not loading this whole 3d scene anymore, we've just
[13:41] created this 2d video. So the render settings, by the way, you want to make sure to render out


### Render settings for ST Map Precomps [13:44]
**Transcript (timestamped):**
[13:48] 32 bit float. And you also want to make sure the compression is set to none. Those two settings are
[13:53] really important for the math, because we're storing a position and usually those kind of utility pass,
[13:58] especially this one, you're going to want the 32 bit and no compression. And I've done a couple
[14:04] tests with this and it is definitely necessary even to turn off the zip compression.
[14:10] So if we check out our result here, we have the image, if we want to just take a checkerboard
[14:16] picture and just stick it in the scene, I'm just going to transform it down, put it in a random
[14:20] spot, and then plug it into the ST map, make sure we're set to RGB. And now if I hit play, you see
[14:26] that it's automatically tracking to our scene. And I don't have a large projection setup anymore,
[14:32] I don't have to load and do all of this again, for every single projection I want to do,
[14:36] I can just put this stuff wherever I want, and it's going to stick and wrap around our geometry
[14:41] and have the perspective. So as we hit play, we can see it kind of wraps. So essentially,
[14:48] we're going to take the same principle, we already have that thing precomped out. And we're just
[14:53] going to apply it to a roto shapes. So I have that image here. And I have our CG scene. I have those


### Applying as a projection [15:00]
**Transcript (timestamped):**
[15:01] same roto shapes that I've done. So for example, I have this roto shape here that brightens this area.
[15:06] It's a very subtle effect, but it's brightening this area. But just before we use it in the mask of
[15:13] the grade, we're applying the ST map, which is going to apply that motion to this alpha. So if I
[15:18] hit a, and I look at it, and I scrub through, you'll see automatically, when it's not enabled,
[15:24] it's not doing anything. And when I enable the ST map, it's sticking to the CG scene.
[15:28] And essentially, also, one important thing that it's kind of a gotcha. And you can mess it up
[15:34] pretty easily because the default is you want to make sure to turn off this clip to, you want to
[15:41] make sure it's set to no clip. And the reason for that is the frame that we've drawn it on. So I drew
[15:46] it on frame 89. We can see I drew a little bit outside of the frame of the video. And if we haven't
[15:51] set the format, we actually get some weird like stretching. But if I turn on no clip,
[15:58] it'll actually maintain what was outside of that area. So always make sure to do that with your
[16:03] roto shapes if you're doing this kind of tracking with these UV coordinates. Same thing with the
[16:11] radial. So if you want to stick, for example, a radial in the settings of the radial, you want to
[16:16] make sure it's set to no clip. So if I look at that alpha, we can see all those rotos are sticking
[16:22] to the scene. I can look at this alpha, I use the radial up here to brighten and you see that it's
[16:27] sticking to the scene. And that's essentially the idea. So that's a really useful way to use it.
[16:32] And it kind of opens up a more creative way to just project a ton of different things without
[16:37] having to, you know, have a ton of different projections, which is going to slow down your
[16:41] script. And that's all what that's all it's about really is speed and efficiency, and getting a good
[16:46] result. Just one important thing I forgot to mention is that there is a little bit of limitation
[16:51] with this technique. And that if there's a lot of overlapping objects, you might have some kind of
[16:55] problems. So I've just done a quick roto shape here along these two geometry. And I've kind of
[17:01] drawn a roto shape, and I've used our ST map, you'll see that if I scrub through, it sticks and
[17:07] there's really no problem in terms of this angle. But if I were to kind of expand that roto shape
[17:14] to the edge of this tube, so let me just double click this. And let's say I put it on the very edge
[17:22] and just kind of put it like this. And it's on the inside, we can see it's inside that cylinder,
[17:32] so it's fine. But if we scroll through, and let me just make sure I have no key frame, we scroll
[17:38] through, we see it's actually projecting through our geometry and onto that ground that's behind.
[17:43] So it's not including itself. And the projectivity occlusion is not that great. So it's not going
[17:48] to be able to do that. So we might have to separate that piece of geometry out or use an ID to kind
[17:55] of remove it behind. So that's just something to keep in mind. If there's a lot of overlapping objects,
[18:02] this technique is not the greatest. But if it's just rocks and pebbles and stuff like that or
[18:08] for soft color grades, this is still a very good method. So just something to keep in mind. So
[18:13] essentially, that's the idea. If you guys liked the video, hit like. I really appreciate it.
[18:18] And if you want to check out the other video, if you haven't seen it, I put it in the description
[18:21] below as well. And thanks so much.



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
