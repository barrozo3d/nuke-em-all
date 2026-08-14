---
title: Mixed Medium VFX P1 | Blender, Nuke, Ai, Embergen, VR Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=2V7eYe8D3nY
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke (cross-platform: Blender + AI image generation + Nuke 2D/3D pipeline; EmberGen mentioned as a topic but not actually used in this Part 1 — appears in Part 2)"
version: "Nuke 13.x (13.1/13.2 — exact 2022 point-release not stated; Classic 3D system only)"
tags: [compositing, 3d-system, procedural-texture, gizmo, ai-tools, digital-matte-painting, advanced]
extraction_status: complete
frames_dir: tutorials/frames/mixed-medium-vfx-p1-blender-nuke-ai-embergen-vr-tutorial/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Mixed Medium VFX P1 | Blender, Nuke, Ai, Embergen, VR Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=2V7eYe8D3nY)
**Author:** Compositing Academy
**Duration:** 26m18s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.

> Reviewed: the "empty transcript in chapter 'Part 2'" safeguard warning refers to
> an 8-second sliver at the very end of the video (26:10-26:18) where the author
> just says a one-line sign-off into the actual Part 2 topic ("we'll start talking
> about the CG [skull] in this") with no further narrated content in this video —
> not a transcription failure. The full 26-minute Part 1 content is intact above.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to this tutorial. This is an experimental tutorial, so it's not geared
[0:13] towards production workflows, it's really just more experimental stuff with different
[0:16] softwares, combining them in different ways that may have not been done before, so that's
[0:22] something I like to do in my free time, is just kind of trying to combine different ideas,
[0:26] new technologies with old technologies, new ways of doing things with old ways of doing
[0:30] things. So that's kind of what we're going to be talking about in this one. So we're
[0:35] using AI, we're using Blender, using EmberGen, Nuke, and a little bit of VR sculpting as
[0:42] well. So that's the kind of topics we're going to cover in this video. And by the way, if
[0:47] you guys want to let me know in the comments below, if you want more experimental stuff
[0:50] like this on this channel, you can let me know, or if you want it only geared towards
[0:53] like production stuff, you can let me know that as well. Potentially I'm thinking about
[0:58] opening a secondary YouTube channel just for the sort of experimental stuff. So that's
[1:03] just some of the thought process there. Yeah, so let me know. But this is kind of what we're
[1:08] going to talk about in this video. And we have a number of things going on here. So I'll
[1:13] kind of break this down, it might be kind of a long video, so you can check out the sort
[1:16] of, I guess the tags on the bottom of the sort of timeline and you can skip to different
[1:22] parts if you're interested. But yeah, we're going to kind of step through this one part
[1:25] at a time. So the first part I'm actually going to go through is the frame. So how was
[1:31] this frame created? And it was sort of made by accident, I was kind of just playing around
[1:36] with different things. And so I'm going to open up that script, and we'll kind of take
[1:40] a look at it. And these are like sandboxes, by the way, so they're going to be kind of
[1:44] messy scripts, because they're really just brainstorming. So these are just, you know,
[1:50] this is a little bit more structured here, but you know, you can see this one's just
[1:53] kind of chaotic. So I know that's going to be another comment. Hey, these are kind of
[1:57] crazy scripts and stuff. But when I'm brainstorming, I'm just playing around with ideas. I'm just
[2:03] pushing everything and kind of coming up with ideas. It's not sort of something that's being
[2:06] handed off to people. So I know those are those are kind of the comments that people
[2:11] might kind of pick up right away. But yeah, so this is kind of how I started here. So


### Ai Concepts [2:15]
**Transcript (timestamped):**
[2:16] actually started by generating some different AI pictures here. I had a rough idea of a
[2:22] shot that I wanted to do and start to work on. And it was actually completely different
[2:27] than the sort of end result. So it kind of started down a path and then kind of just
[2:32] kind of deviated off of that path. And that's what's kind of fun of doing your own projects.
[2:37] You don't really have set rules what you can do. So yeah, I mean, you guys can go check
[2:42] out the video on the AI thing, you know, how to do descriptions and stuff like that. I
[2:46] think I did a few maybe two months ago or something like that. Go check out that video.
[2:50] But these are great for inspiration because these are all made by, you know, computer and
[2:55] your prompt. So if you have a rough idea, you can get something that's kind of interesting.
[3:00] And so I found this one and I really liked this sort of pattern. One one way I've started
[3:08] to think about these AI tools when I'm approaching them, in terms of concepting a scene is to
[3:14] think in terms of level of detail. So you can think in terms of like giving descriptions
[3:19] that are more wide sort of angle wide wide shot. And then you can do descriptions that
[3:25] are more close up like the materials themselves. So it's a really good way to concept out.
[3:31] Yeah, basically level of detail. So it's like if you think of a painter and you think of,
[3:36] you know, the landscape, the painter, if he's painting a tree, he'll just paint one leaf
[3:40] and it's a green dot. But if you want to see the leaf up close, you know, that's a different
[3:45] description. So you can get those those kind of zoom in to your scene. And that's how you can
[3:49] sort of concept the scene using these tools. So this is a material that I found was interesting.
[3:55] And what I wanted to do was kind of try to recreate this in 3D in Blender. And first off,
[4:02] the first thing you're going to want to know is that this is not physically based rendering AI
[4:07] tools. Like this looks very painterly. There's some parts that look kind of physically rendered
[4:11] like some kind of reflections that maybe could be kind of realistic, it looks kind of glass like.
[4:17] But if you were to try to render this in a physically based rendering, you're not going to
[4:20] be able to recreate this exactly how it is because the AI is kind of mixing, you know,
[4:26] paintings and pictures and all kinds of things. So there are some parts that feel sort of kind
[4:33] of physical, like in terms of like the way the exposure looks, it looks pretty cool. But you
[4:38] know, you see the slide here, and that doesn't actually cast on anything, you know, we say a
[4:42] little bit there, but maybe it's not actually casting. So just keep that in mind, the lights are
[4:47] not physically accurate. So if you're going to try to recreate it, it'll probably look a little bit
[4:51] different already from the get go, which is actually kind of a cool thing to know. So the way I
[4:57] started with this, in my mind, was to kind of look at this and sort of break down the forms and
[5:03] shapes into basically simple things that I can recreate. So like for example, if you kind of
[5:10] study this picture, you can kind of go in here and if I take a roto paint, you know, I want to look
[5:16] at, you know, what are the simplest forms that I can identify that I can start to recreate. And so
[5:22] if I look at stuff like this, people who are more generalists are already going to kind of know,
[5:28] you know, what this kind of looks like, looks like a the Voronoi sort of cell kind of pattern. And
[5:34] you can, you can see these here. So these are the kind of things that immediately kind of stood
[5:39] out to me is like, okay, I know how to create these sort of shapes. And that's where I'm going to
[5:44] start. So I'm kind of breaking this down and looking for these kind of things. And that's,
[5:49] that's immediately the first thing that I saw. There's other things in here. So you can see this
[5:54] is a little bit similar. It's kind of a sort of a grid. But the grid is a little bit warped around
[5:59] the edges. So it's a little bit more organic. But it's still kind of just if you look at it,
[6:03] it's really just kind of a grid of sort of squares. So that's another thing to pay attention to. And
[6:11] that's kind of kind of how I went about breaking it down. And I was going to kind of create those
[6:16] texture patterns and displace them from a 3d model. Once we hop into 3d. So rather than doing
[6:22] these textures in, in like blender or Maya, like there are texture editors, some material editors
[6:28] in those softwares. But, you know, for example, the one I just kind of pointed out, it might be a
[6:34] little bit difficult to get that sort of warp and stuff like that. So it's easier just to do it in
[6:39] Nuke if you're familiar with Nuke already. So basically, I started with a cell noise like this
[6:46] one here, I wanted to create this surface. So I started with a cell noise and cell noise, this is


### Noise Patterns [6:48]
**Transcript (timestamped):**
[6:51] a, yeah, this is a sort of custom note on Nucopedia. I think it's called, I think it's called cell
[6:57] noise on Nucopedia, you can type it in. I'll probably try to link it in the description there
[7:01] just for the people who want it. Yeah, cell noise, and then you can basically modify it, it just
[7:07] gives you a bunch of noise patterns that, you know, are better than sort of the sort of standard
[7:13] one that's in Nuke, you know, 3d softwares have a lot more noise patterns than Nuke sometimes. If
[7:20] you look at like Sima 4d, and you go look at what noise patterns they have, they have like a ton of
[7:24] noise patterns that they can use. So hopefully, Nuke will implement some more in the future. But
[7:28] fortunately, somebody's already created a node called this, maybe it has the information here,
[7:33] but I'll touch in the description. So this is what we get. And we can play with the size here. We
[7:39] can animate it and stuff like that. And we can add contrast if we want to do stuff like that.
[7:44] So that's kind of what we get. This is kind of very basic pattern. But what we can do is we can
[7:52] kind of, we can add some contrast to it and get something a little bit closer. So if we see,
[7:56] just adding a little bit of contrast, we already get something that's somewhat kind of close,
[8:01] you know, you get these sort of randomness and smaller ones, but it already feels a little
[8:06] bit similar. It's not too far off. So I did that and I kind of broke it up with another noise
[8:11] pattern. So it's just like a noise and then multiplying it. So a little bit of break up and
[8:16] you get these sort of peaks and troughs of different shapes here. And I played around with
[8:22] different variations of this. So that's what all these are. It's kind of a mess here. But I was just
[8:26] quickly, quickly iterating coming up with ideas in sort of a sandbox type of way here. So here's
[8:33] another one. This is kind of interesting. I didn't use, I don't know if I use this one, but I did
[8:39] a posterize on it, which you can get sort of these like circular illustrative patterns, which is
[8:45] pretty cool because like I said, I don't think I use them this project, but it's pretty cool technique
[8:50] because you can just like animate this. And then you have like these crazy, I don't know, sort of
[8:57] illustrative circles here. And you could totally use this like a force field or something like that.
[9:03] Whatever you want to use it for, you could use this as a displacement map on a 3D object. So you
[9:08] could actually, you know, create a really cool effect by doing that. So one of the ways I like
[9:14] to think is really like this. It's very simple. I like to think 2D, 3D, 2D, 2D. And then, you know,
[9:28] kind of converting between these spaces over and over. And you're going to see throughout this video
[9:32] how it's a really weird workflow, but it can create some really interesting results because you can go
[9:37] 2D and then you can go 3D again. So you'll see what I mean. This might sound like nonsense right now.
[9:42] But as I progress in the video, you're going to see sort of the sort of concept behind it. So
[9:48] let me just step through a few more of these examples because I think they're kind of interesting.
[9:51] People might find them interesting. So another cell noise edge detect instead. If we look at the
[9:56] Alpha channel, we get something a little bit crazier. And then you could just play around with
[10:01] like inverting it or just playing with the contrast playing with the levels of those patterns. So this
[10:06] is the pattern I kind of outputted. And you see that this sort of organic pattern with some of
[10:11] these sort of grid things in there. You know, why was I creating this? Again, I was going back to
[10:17] this picture and trying to look at some of the things underneath and maybe just trying to create
[10:21] something similar. And yeah, maybe it's not exact, but it was kind of closer or similar. So that's
[10:29] kind of what these patterns are created different variations. And like this one is a little bit
[10:34] different, but it's a really cool pattern. And the way that one's created again, it's just a cell
[10:38] noise and then doing an edge detect on a different sort of scale. So you can erode these things and
[10:44] you can get different shapes. And like I said, that would be kind of hard to do if you're just hopping
[10:49] straight into a 3D software. You know, Blender has a pretty good like material editor, but at
[10:57] the same time, you don't have the level of control you have in Nuke. And if I wanted to warp this,
[11:01] you can do it in here. If I want to animate it, you can do it really quickly in here as well.
[11:06] So that's just, it's just my preference to do it that way. So again, here's another one,
[11:12] edge detect, doing the same kind of idea here. This time I use a little bit of a noise pattern
[11:17] off the side, I hit replace, it's just grabbing the format. So all it's doing is I just want to make
[11:21] sure that these are always in the same format, probably didn't even need to hear, but that's
[11:25] just a little trick. And then I'm using the glass node again from Nucopedia. And this is just a
[11:31] really easy way to distort things. So yeah, we can just kind of warp using one noise, like this one,
[11:37] to warp another one. So we can kind of mess up the edges a little bit, get them a little bit more
[11:41] organic, rather than like a standard circles everywhere. And then we can, you know, just
[11:46] continue down that path. So here's another example, kind of the last one, maybe. Yeah,
[11:53] something like that. So that's the way I kind of mentally was breaking these down and trying to
[11:59] sort of reverse engineer those AI renders, like, can you recreate those? And I did a bunch of different
[12:04] techniques here, you know, here's another one, this basically just different cell noises,
[12:10] in different sizes, and you can stencil them from each other. You know, for example, I created a
[12:15] cell noise here, just added a bunch of contrast, like this, and then just use that to mask the other
[12:21] one. So then you get like shards. And then that's something you could, you know, you could animate
[12:26] both of those and you could create a crazy force field type of thing, whatever you want to do.
[12:31] It's kind of cool. So I don't want to go on too long in this part of the tutorial. But here's
[12:37] some more shapes, just to show you like the amount of variation that you can do. And you can do this
[12:41] pretty quickly. So it's not something that's going to take, you know, hours and hours. So even if
[12:47] you don't use some of them, it's totally okay. So that's kind of the idea, breaking it down.
[12:54] So that's the sort of 2D part, just getting some textures that we're going to bring into Blender
[12:58] after. And I guess we'll hop into the Blender part next. So the next part of creating this frame is
[13:05] actually creating a render from all of these pieces. So I'll open up the Blender scene. I'll show you
[13:10] what I did with all these textures. And yeah, how we go from there. Alright, so onto the Blender


### Blender [13:16]
**Transcript (timestamped):**
[13:18] part. This is the kind of Blender scene that creates the frame. And you might be wondering why
[13:23] it's in a stacked sort of pattern here. And so if we look back at the kind of concept we had,
[13:32] which is this sort of AI thing, you can see it's in kind of multiple layers, we have like a top
[13:37] layer, that's kind of glass, and then we have like sort of orange lines on the peaks of the glass.
[13:41] And then we have underneath a bunch of, you know, kind of star shapes and red stuff,
[13:47] kind of red lights underneath, kind of sub dermal. So the way I came up and kind of conceptualized
[13:52] was something like this, where we have multiple layers of textures being displaced. And some of
[13:57] these are on multiple different layers that we can't see because this is not rendered yet. So
[14:02] we see there's one layer here and if I click, there's actually two right on top of each other.
[14:06] And that creates the kind of gold leafs on the edges. So I just read this out, I'll show you
[14:09] guys what it looks like. So we'll just switch to cycles. We'll give it a few seconds here to load
[14:15] and it'll give us kind of a preview. So this will take a few seconds. And one important thing to
[14:23] note is that our angle is going to matter a lot with the lighting because it's so reflective.
[14:29] So this is kind of what the base looks like, we have some red lights underneath,
[14:32] so reflecting underneath, kind of hitting stuff. And we have the kind of surface reflections
[14:38] hitting the sides here. So I kind of like the way that this looked. But if we kind of rotate and
[14:42] put our camera a little bit lower, we're going to get a little bit more of that Fresnel effect,
[14:46] where we get more surface reflections. It's going to look a little bit closer to a concept where we
[14:50] have those kind of glancing angle reflections and stuff underneath. So like I said, the other one's
[14:56] not physically accurate, this is more physically accurate. So I like the way this looked, I thought
[15:01] this result was pretty good. And yeah, I'll just kind of rotate to some different angles here. So
[15:06] you could use this for many different things, like different angles could be used for sort of
[15:09] different things here, I suppose. So if I run it from the top, it looks a bit different. So where
[15:15] this project sort of deviated, I suppose, is kind of what I was doing was kind of playing ground
[15:20] with rotating it here, and placing the camera on the side. So I have these like orbs in here that
[15:26] are just emissive lights that kind of reflect. So if I place the camera in here and give a few
[15:31] seconds to render, we can see we get a really, really different result. So we can see something
[15:39] kind of interesting here. Maybe the edges and the facetting doesn't hold up quite as much on the
[15:45] metal that's really close to the camera. But some interesting shapes and forms being created.
[15:50] It's not the highest quality render from this perspective. But I actually did use this angle
[15:56] for something. So I'll show you guys what we do with Nuke with this angle. And I kind of rendered
[16:00] a camera zooming through the kind of the layers here. And that's actually how part of the frame
[16:07] was created. So I'll show you guys kind of the end result of that in just a second here. So yeah,
[16:14] these are just basically surfaces with those textures I created in Nuke displaced and then
[16:19] some shaders on there as well to break up the highlights. I'm not going to go into too much
[16:23] detail on the displacements and every single material. If you guys want like a mini class on
[16:30] that, maybe I'll do one. Just depends if people actually are looking for that kind of thing.
[16:34] You can let me know. But yeah, that's kind of how we get to this point. So
[16:40] we'll hop back into Nuke here and take a look at the sort of 2D side again. So essentially,
[16:47] this is the render we get. And let me just find the animated one. I have an animated one here. So


### Nuke 2d [16:48]
**Transcript (timestamped):**
[16:55] essentially what I did was I took this scene and I pushed the camera through. So I'll just let it
[17:00] play a few frames. We see there's some noise and stuff. We could have done some more samples,
[17:04] but I was just testing different angles and testing different renders. So I just let it render for
[17:09] maybe like an hour or two hours or whatever, get a few frames and just see like what angles are kind
[17:14] of interesting. And so this is kind of cool. There's some stuff that looks broken though.
[17:19] And I was like, it's not that good of a render. Maybe the top view is better. I kind of like the
[17:25] way the glass looks though, when you kind of zoom in, you see all the bending of light and you see
[17:29] all the layers. That stuff is kind of interesting. So I was kind of looking at this like, well,
[17:33] maybe I could salvage this render and do something with it. And that's kind of where,
[17:40] like I said, the sort of project takes a little bit of a left turn in terms of what it was going
[17:45] to be. But let's go back into the 2D part now. So again, we talked 2D, 3D, and now we're back
[17:50] in 2D again. And what I decided to do was kind of cut this render up into pieces. So I'm going to go
[17:57] up here into this kind of mess of a script and just kind of step through and just show the kind
[18:05] of randomness that this will kind of generate. I'll just kind of straight it out here as we look
[18:10] at it. You can see some stuff is disabled and enabled here because you see that this is sort of
[18:14] the experimentation phase. So some of it's just, yeah, you know, back and forth. But let's look
[18:20] at this. So what I did was I started to kind of just cut off the top and just focus on like one
[18:24] half of it. And I started to do some like tiling. Because I wanted to figure out a way to make this
[18:29] render look better. And it wasn't that interesting. And there's no exact end goal in mind. So I didn't
[18:34] really have any limitations of, you know, the direction I had to work in. So I started to tile it.
[18:40] Starts to give us sort of a nice kind of interesting pattern, I suppose, especially on the bottom.
[18:45] And then if we just keep going,
[18:50] then I did a polar distort here, which is pretty cool, because then we get something really
[18:55] interesting where this is starting to look like an actual piece, like we could use this for something,
[19:00] for sure. That's what's going on my mind. I'm looking at that, you know, almost looks like an
[19:04] I have Sauron type of thing or something like you have like an eye or an iris. And of course,
[19:09] you can control your tiles. You could just increase these or decrease these and the end,
[19:13] you're going to change your shape like this. So you start to really get into the abstract
[19:18] kind of style here. And so I did this multiple different ways. So I took the same render, I
[19:24] would stencil off the bottom, I would tile it in different ways. So I kind of took the render,
[19:30] flipped it over itself. So you get two sides, and then tile that. And now you see, we get a
[19:35] different result. So it's really just a combination of flipping it, tiling it, and polar distorting
[19:41] it. And so you get these different sort of combinations of kind of fractal fractal, S I
[19:47] suppose it's not completely a fractal, but this sort of style of thing. And then I just kind of
[19:52] started stacking these renders together. So we have stuff like this, you get these different
[19:57] things here. And then I had something kind of interesting here, I was like, well, that's kind
[20:02] of cool. But maybe, you know, we could force the perspective a little bit, because, you know,
[20:08] it's not very thick here, you know, maybe we want to have this part be longer, like we want to be
[20:12] inside of a tube. So what I did was I did a polar disorder again, which kind of flattens it out into
[20:18] texture space, and then put this onto a cylinder. And what does that do? Basically, it just puts
[20:24] it into sort of a three dimensional space again. So remember, I said 2d 3d 2d. Now we're back in
[20:30] 3d again. So this is kind of interesting because we can fly a camera through this. So essentially,
[20:38] we get some crazy fractal stuff. And if I let this load, I was actually going to use this
[20:44] as part of the eye of that skull that I was showing you guys originally. Let's just let this play.
[20:49] And then we can kind of let's just see if we have a think we have a video here somewhere.
[20:56] Yeah, I just loaded an MP4. So we have this thing. And this is kind of the end result. So we have
[21:03] this cool thing where we have all these shifting motions and layers and yeah, just from tiling
[21:10] renders and kind of warping them and doing different things there, kind of salvage that render that
[21:15] wasn't maybe wasn't that interesting. It was kind of interesting, but maybe it could be better, you
[21:19] know. So that's kind of what we get. And one thing to mention as well is let's see.
[21:27] One thing I did as well, just to give a little bit of parallax, I just duplicated the sort of
[21:31] cylinders here. And just to give a little bit of parallax between those two shapes, which we get
[21:36] sort of, yeah, just a little bit more interest, I guess, in terms of the overlap between those two
[21:41] things, it gives a little bit more than just like a two dimensional feel, which is not what you want
[21:45] necessarily. So that's kind of the end result. And this was actually, like I said, going to be one
[21:51] of the eyes in that skull. I showed originally was going to be zooming into it or something,
[21:56] kind of abstract art, but it ended up just looking kind of interesting as a frame. So that kind of
[22:03] render on the outside is, yeah, basically just what I showed. We have it here. I just did some
[22:10] color corrections on it. So if I just step through just a bunch of color corrections, it's a little
[22:15] broken here because I switched into aces. But yeah, we have just a bunch of color corrections that
[22:21] kind of different areas. And the nice thing about this, by the way, is because you render it out of
[22:26] CG, you can control different aspects of this sort of fractal. So like if I want to control the depth
[22:32] and stuff like that, I have all of those extra layers that I can sort of pop out. And you see
[22:37] like the distance, for example, the depth pass, I could grade the back different than the foreground.
[22:42] So I can control that sort of effect there, which is going to look pretty cool when you're
[22:48] working in a sort of a fractal type of way here. So this is kind of the frame and, yeah,
[22:55] just frame holding at one point in time. But you could you could just play it through and you're
[22:59] going to have different shapes on every single frame, which gives you different stuff. And it's
[23:03] red here, which is different than the final result because I used it for another sort of piece that
[23:08] was very similar. So there was a couple of these that I was playing around with.
[23:15] Yeah, don't want to spend too much time on each part because the video is already going to be
[23:18] pretty long. So I know I'm stepping through pretty quick here. But, you know, just color corrections,
[23:23] hue shifts, popping out the highlights, you know, targeting some of the highlights to give a little
[23:26] more contrast. Because if you kind of do this D sat thing, if you grade it, if you desaturate and
[23:32] you tint something, you're going to lose sort of the feeling of range. So what you want to do is kind
[23:36] of target the highlights and desaturate them a little bit, it'll give more of a feeling of range.
[23:41] It's pretty common technique with a lot of things. So just keep that in mind.
[23:47] And yeah, just stepping down more color corrections, and that's basically it for the frame.
[23:53] And then we can just add some little subtle glows here. So I use those sort of, I guess,
[23:58] the miss of lights that I had put in there as kind of lights in the frame.
[24:02] And that's basically it for this part. Just step down here. Just seeing if there's anything else
[24:08] here. Here's an interesting part to mention. Because I'd warped this picture so many times,


### Ai Detailer [24:10]
**Transcript (timestamped):**
[24:12] reprojected and done all these things, we lose a little bit of quality. We see we see a little bit
[24:16] of sort of sampling here in our kind of pattern. And I was like, well, that's not great. Like,
[24:24] could we could we make that a little bit better? And there's a tool called topaz upscaling. And
[24:30] you can a gigapixel, I guess the product is. So what I did was I took this render
[24:36] and to fix these edges, because we've sampled it so many times and done so many crazy stuff,
[24:40] we just use the AI upscaler. And essentially, it's going to give it a slight illustrative look,
[24:45] but we can kind of smooth out some of the edges here. And then we can kind of blend those two
[24:49] renders together. So at least we can get some of the detail back on the edges. Of course,
[24:56] our colors are changing a slight bit. I do think that this workflow will become more prominent
[25:01] in the future. And maybe we'll maintain highlights and stuff and the colors a little bit in a more
[25:06] perfected way. But regardless, we still get these nice smooth edges restored here. And then we can
[25:13] just sort of, yeah, kind of patch that into different areas. So I kind of key makes the upscaled
[25:18] image into different areas. So we get some smoother edges. And I put a slightly focus as well,
[25:24] just to soften it, because the focus is eventually going to be kind of on the on the center here.
[25:28] So but I just wanted to fix like little weird sharp edges that kind of come through. So that's
[25:34] how you can use an AI upscaler to essentially, I don't know, it works for still images. There is
[25:40] a upscaler for video as well that they have I haven't used it quite that much yet. I've been
[25:45] experimenting with it. But it's good to know that those workflows exist if you're ever in a sort of
[25:51] problem with that. Especially if you're doing something with like a lot of texture, and you
[25:55] need to maintain those details. So continuing through, I guess we're on to the skull part now.
[26:01] So this will be like the second half of the tutorial, we covered the frame, we'll start talking about
[26:07] the CG in this.


### Part 2 [26:10]


---

## Captured Frames

- [3:00] tutorials/frames/mixed-medium-vfx-p1-blender-nuke-ai-embergen-vr-tutorial/frame_000.jpg
- [7:00] tutorials/frames/mixed-medium-vfx-p1-blender-nuke-ai-embergen-vr-tutorial/frame_001.jpg
- [14:15] tutorials/frames/mixed-medium-vfx-p1-blender-nuke-ai-embergen-vr-tutorial/frame_002.jpg
- [18:55] tutorials/frames/mixed-medium-vfx-p1-blender-nuke-ai-embergen-vr-tutorial/frame_003.jpg
- [20:35] tutorials/frames/mixed-medium-vfx-p1-blender-nuke-ai-embergen-vr-tutorial/frame_004.jpg
- [21:05] tutorials/frames/mixed-medium-vfx-p1-blender-nuke-ai-embergen-vr-tutorial/frame_005.jpg
- [24:30] tutorials/frames/mixed-medium-vfx-p1-blender-nuke-ai-embergen-vr-tutorial/frame_006.jpg

---

## Structured Notes

### Core Technique
An experimental "2D → 3D → 2D → 3D" pipeline: AI-generated concept art is reverse-engineered into Nuke procedural noise patterns, displaced onto Blender geometry and rendered, then the render itself is re-imported into Nuke and abstracted further with tiling/polar-distort/cylinder-projection tricks to generate fractal-like VFX elements — finished with an AI upscaler (Topaz Gigapixel) to recover detail lost from repeated resampling.

### Summary
Compositing Academy's self-described "sandbox" video (frame 000 shows the messy, unstructured node-graph browser used throughout) walks through building one frame of a larger "Stormy Crystal Skull" piece (see Part 2 / the separate "Stormy Crystal Skull" video). Starting from an AI-generated reference image, the author breaks its visual patterns down into primitive shapes he can recreate procedurally (Voronoi-like cells, warped grids), builds them in Nuke with the Nukepedia `CellNoise` gizmo (frame 001 shows the resulting sprawling noise-experimentation node tree) rather than Blender's material editor — reasoning that Nuke gives finer procedural control and it's a workflow he already knows. Those 2D textures get displaced onto simple Blender geometry (frame 002: a subdivided plane with a displacement/geo-node modifier visible in the outliner) and lit/rendered in Cycles at different camera angles to get physically-plausible reflections. The Blender render is then pulled back into Nuke's 2D side and abstracted further: cropped, tiled, flipped-and-tiled, and pushed through a Nukepedia `PolarDistort` node to fold the tiled render into an iris/eye-like radial pattern (frame 003 — the red/orange radial "Sauron eye" result), then that same distorted texture is wrapped onto a 3D cylinder and a camera flown through it to generate an animated fractal render (frames 005–006 — cyan/blue radial ring and kaleidoscope-style renders used as sci-fi "portal"/"eye" elements). A duplicated, offset cylinder pair adds cheap parallax. The chain finishes with color grading (targeted highlight desaturation to preserve a feeling of dynamic range rather than a flat overall desaturate+tint), subtle glow from the render's own emissive light layers, and — because the image had been resampled/reprojected so many times that fine edges went soft — a pass through Topaz Gigapixel AI upscaler, key-mixed back in only where edge sharpness needed restoring, plus a slight defocus to hide the seam since that area was meant to fall out of focus anyway.

### Key Steps
1. Break an AI-generated reference image into recognizable procedural primitives (Voronoi/cell patterns, warped grids) by eye — this is a concepting/analysis step, not a node operation.
2. Build matching procedural textures in Nuke rather than a 3D app's material editor: Nukepedia `CellNoise` as the base pattern, pushed through Grade (contrast) to sharpen cell definition, layered with a second Noise multiplied in for surface breakup, and `Posterize` for illustrative circular-ring variants.
3. Warp organic edge variation into an otherwise-regular pattern using the Nukepedia `Glass` node, distorting one noise pattern with another so edges read as organic rather than perfectly circular/gridded.
4. Export these 2D textures out of Nuke to use as **displacement maps** on simple geometry in Blender; light and render in Cycles, checking multiple camera angles since a highly reflective/glass-like material is extremely angle-of-incidence sensitive (lower camera angle = more Fresnel-driven surface reflection read).
5. Bring the Blender render back into Nuke's 2D side: crop to isolate a region, `Tile`/repeat it, flip-and-tile for symmetry, then `PolarDistort` (Nukepedia) to fold the tiled pattern into a radial "iris/eye" composition — tile-count and distort settings directly control how abstract/fractal the result reads.
6. Go back to 3D a second time: re-apply `PolarDistort` to flatten the pattern into texture space, then project/wrap it onto a **Cylinder** in Nuke's 3D system and fly a `Camera` through it — this produces an animated radial/fractal element (the "eye" shapes used later as a Stormy Crystal Skull element) purely from re-projected 2D texture, no new 3D modeling.
7. Add cheap parallax: duplicate the cylinder, offset it slightly so the two overlapping radial layers separate visually as the camera moves, avoiding a flat 2D look.
8. Color-finish: multiple `Grade`/`ColorCorrect` passes (partially in ACES), targeted highlight desaturation instead of a global desaturate+tint (preserves a sense of dynamic range), plus subtle `Glow` sourced from the render's own emissive/light elements.
9. Recover fine detail lost from repeated resampling/reprojection: run the frame through **Topaz Gigapixel** (external AI upscaler, not a Nuke node), then `Merge`/key-mix the upscaled pass back in only around soft edges, adding a touch of defocus to blend the seam in the area that was going to be out of focus anyway.

### Nodes / Tools / Settings
- **Core Nuke:** Grade, Noise, Posterize, Crop, Merge (key-mix), Transform, Camera (3D), Cylinder (3D geometry), ScanlineRender (implied for the 3D cylinder fly-through)
- **Nukepedia gizmos:** `CellNoise` (Voronoi/cell-pattern generator — author notes Nuke's native noise options are more limited than dedicated 3D packages like Cinema 4D), `Glass` (distortion/warp using a second image as a displacement source), `PolarDistort` (rectangular↔polar remap — same gizmo family as the "360 Spherical LatLong Textures" tutorial, used here for an artistic radial-abstraction effect rather than sphere-wrapping)
- **External / cross-app tools:** AI image generator (unnamed, for concept reference only), Blender (Cycles render engine, displacement modifiers, camera framing for Fresnel-driven reflections), Topaz Gigapixel (AI upscaler, used as a detail-recovery pass, not part of the Nuke graph)
- **Workflow shorthand the author repeats throughout:** "2D → 3D → 2D → 3D" — procedural texture (Nuke) → displaced render (Blender) → abstraction via tiling/polar-distort (Nuke) → re-projection onto new 3D geometry (Nuke 3D) — a repeatable pattern for turning a single render into many derived VFX elements.

### Difficulty
Advanced — not because any single node is complex, but because the workflow chains speculative, iterative decisions across three tools with no fixed end goal; following along requires comfort experimenting rather than a fixed recipe.

### Foundry App & Version
Primarily Nuke, with Blender (Cycles) for the intermediate 3D render and an external AI upscaler (Topaz Gigapixel) — genuinely cross-platform, not a stub case, since the Nuke-side techniques (CellNoise/Glass/PolarDistort procedural texturing, the 2D-to-3D cylinder re-projection trick) are the majority of the runtime and are Nuke-specific enough to be the primary extraction target here. EmberGen (mentioned in the video title) does not actually appear in this Part 1 — it belongs to Part 2 ("Stormy Crystal Skull... Part 2", prhQhQ5AnNM), the direct continuation of this same project. Nuke version not stated on screen; per this skill's version-tracker, a 2022 upload falls in the 13.1 (Nov 2021) → 13.2 (Apr 2022) window. Uses only the Classic 3D system (Cylinder/Camera/ScanlineRender) — predates the 14.0-beta USD 3D overhaul.

### Tags
compositing, 3d-system, procedural-texture, gizmo, ai-tools, digital-matte-painting, advanced

---

## Related Tutorials
- Stormy Crystal Skull | Nuke, Blender, Ai, Embergen, Mixed VFX Medium Part 2 (`stormy-crystal-skull-nuke-blender-ai-embergen-mixed-vfx-medium-part-2.md`) — direct continuation of this project (Part 2), covering the CG skull itself and the EmberGen storm-simulation work referenced in this video's title.
- 360 Spherical LatLong Textures | Nuke Tutorial (`360-spherical-latlong-textures-nuke-tutorial.md`) — shares the Nukepedia `PolarDistort` gizmo, used there for sphere-wrapping and here for artistic radial abstraction; useful to read together to see the same node used for two very different purposes.
