---
title: How to DENOISE your CG in POST | Blender & Nuke Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=uReRex8xPqs
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-denoise-your-cg-in-post-blender-nuke-tutorial/
frame_count: 0
frame_status: pending-selection
---

# How to DENOISE your CG in POST | Blender & Nuke Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=uReRex8xPqs)
**Author:** Compositing Academy
**Duration:** 16m4s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py how-to-denoise-your-cg-in-post-blender-nuke-tutorial <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to this tutorial. This time we're going to talk about how to remove noise
[0:14] from CG renders in post. So we're dealing with some blender renders here, but this really
[0:20] applies to any, you know, renders that you're getting. If you have noise in them, which usually
[0:26] is happening in glossy reflections or secondary light bounces, so like global illumination
[0:32] and just not having enough samples in different areas is where you're going to see this problem.
[0:37] So we're going to talk about that in the second part of this video. And then the first part,
[0:43] I'm going to explain just for the people who want the creative aspect of where this light
[0:47] is coming from in this particular shot. We're still using the example I used a couple other
[0:51] videos, but I'm just going to explain how I created these kind of CG, I don't know,
[0:56] force field waterfalls kind of thing. And then we bring this into Blender and we will
[1:02] use this as a mission shader, which is creating this basically lighting up the scene for an
[1:07] interactive light pass. And yeah, when you're using a mission shader, or you know, if you're
[1:14] in a different software, if you're in Arnold and Maya, it's the same thing. If you're using
[1:18] kind of the indirect lighting, you're going to have you're going to have to throw a lot
[1:22] more samples at it most of the time. And this is where noise can happen. And again, in the
[1:28] glossary reflections as well. So that will always be explained. And yeah, we'll get into
[1:32] it. So how's this done? This is just a brief quick overview, because this is not the main


### Overview [1:36]
**Transcript (timestamped):**
[1:38] point of this video. But just for those who are interested, this is just a different element
[1:44] similar to the one that we were using on the shockwave. But this is a different looking
[1:48] one. So we have one that looks more like a growing kind of force field type of effect
[1:53] here. And what we can do with this element is kind of layer it over itself. So I just kind of
[2:00] played around with different shapes and just trying to find different options of something
[2:05] that looks like it was flowing. So I wanted to do something that looked kind of like a flowing
[2:09] force field. So something a little bit liquid, like so I thought this one was kind of interesting.
[2:16] And I basically just time offset and merge it onto itself. So if we go back in time, or maybe
[2:23] forward in time, let's see what happens here. We can see I kind of layered it over itself. So we
[2:29] have like the main effect. And then we start to time offset and merge that over itself. And what
[2:34] that does is gives us just a sense of layering and depth to the to the effect. And then I basically
[2:41] just kind of rotated this and scaled it. So what I did was I modeled a really basic card that's
[2:47] just like bent that kind of goes with the scene. And then I just duplicated it a whole bunch of
[2:55] times around that center core as the force field generator kind of turns on, I was just thinking
[3:01] like, Oh, this is kind of supposed to be some sort of generator for force fields. So of course,
[3:06] you want to start designing the fact from story first. But yeah, so this is kind of how I went
[3:12] about doing it. And what you get is something like this. So basically, on each of these cards,
[3:19] it's the same exact card just duplicated a bunch of times, we just take that effect that's
[3:22] spreading. And we do a little bit of a time offset on all of those so that they kind of come out at
[3:28] different times. And then we can get something kind of cool like this. So this gives us interesting
[3:35] alpha to start with. And if I let that play, we'll just let it go here. Yeah, so we can see it kind
[3:44] of spreads out like this. So we're kind of getting these shapes that look sort of liquidy in a way.
[3:50] And yeah, that's basically it. But what we can do now is to get a more realistic lighting,
[3:57] rather than just simply, we could fake it if we had to, we could do it, we could fake it,
[4:03] we could blur these out and do it that way if we have no other option. But if you have the time
[4:08] and you have the option, what you can do is render this out as a 2D texture rather than rendering
[4:13] it out directly to the scan line. And that's what I did. So I actually did that and brought these
[4:18] back into Blender and then use them as an emission shader. So I basically applied that material
[4:24] onto each of these. And then I just rendered that whole scene out as a very glossy scene to get
[4:30] basically an interactive light pass. So we get something like this. So as those those kind of
[4:37] waterfalls are coming out, we get something that gives us some really nice reflections that would
[4:41] be really, really hard to achieve a nuke because you know, it's real reflections, we're getting
[4:45] glossier reflections based on the spec maps, and the roughness of each of these materials. So
[4:52] that's just something that's kind of cool to see. And that's just a different way of working with
[4:57] those kind of elements as well as to kind of bring them between 2D or 3D. There's it's really
[5:02] just up to you creatively. So one other thing I did that's kind of useful to mention is I like
[5:08] to get into 2D as much as I possibly can when I'm working, meaning so I render one of these out
[5:15] like a ramp. So basically, I just took the same geometry and put a ramp starting white and then
[5:20] black on the end. And then I can just use this as a map to adjust the like basically grade it without
[5:27] having to go back into the 3D system because this was kind of heavy having all of these rendered.
[5:31] So that's just a general advice is if you can get out of the 3D system and do stuff after, that's
[5:38] just generally going to speed you up as a workflow type of thing. So we can use this thing and kind
[5:44] of adjust, adjust that that ramp. And we can kind of crunch it like this so we could we could crunch
[5:54] it. And we could use that to color grade different aspects of it. So correction control kind of
[6:03] thing, but it just shows you a different way to work with these 2.5D kind of renders, I suppose.
[6:10] But yeah, that's basically for this part. Now we can talk about how to fix some of the noise that
[6:14] we're seeing in here. So if you look, and this this already had a decent amount of samples, but this
[6:19] is a very glossy scene. The whole scene is basically metallic. And I will put a caveat and say, you
[6:27] know, this technique works in some instances, if there's a lot of overlapping geometries, and, you
[6:33] know, a lot of complex camera movement or bending materials, this is probably not going to be the
[6:37] best technique. But for an environment scene, sometimes it's really, really useful to do this
[6:42] technique. And but of course, it's going to be always better to go back and just throw tons of
[6:47] samples at it if you have, you know, infinite time or resource to just increase and do it that way.
[6:52] So yeah, we'll get into that part now. So this technique is actually relatively simple. All we
[7:00] need to do is take our render and project it onto the model of the scene. So you basically want to
[7:06] bring in an Olympic export from whatever software you're using. And we can project it. So we have
[7:16] like the render and we're projecting the render the whole time, basically onto that geometry. So it
[7:21] lines up perfectly. So you see that everything is lining up. There's some overlapping stuff. But in
[7:27] this example, we're just going to talk about this specific area. So I solve the noise in three
[7:34] different ways actually on this. So we're going to talk about just this area, I'll talk about this
[7:38] area separately and then also that one. So sometimes you need to approach things differently based on
[7:43] what's happening. And in this case, you know, this is a very flat surface that's always facing us. So
[7:49] it's an easier problem to solve. Because it's not really overlapping a bunch of a bunch of times
[7:55] with with objects. So basically, if we just watch it, we can see there's if let's just let it play,
[8:02] we can see there's a bunch of noise kind of dancing. And it's like kind of lower frequency noise,
[8:07] it's not like really small noise like this, you see how this is kind of high frequency, smaller
[8:12] dots and these are much larger. So that also plays a role in how we are going to approach it. But
[8:19] basically, all did take that render, projected onto the model, we're not frame holding the camera,
[8:24] we're letting it play the whole way through. And we're going to put it into UV space. So if you go
[8:30] watch the UV UV baking tutorial, if you're not familiar with UV space, because we're going to use
[8:35] it a lot on this channel, because it's really, really good workflow for like a ton of different
[8:39] things. So yeah, basically, UV, and you and we can basically see that that model on wrapped here,
[8:46] and the render is live on this. So actually, if I play this, I don't know if it's going to play in
[8:51] real time. It might be a little bit heavy. Yeah, I don't think this is going to play in real time.
[8:58] So I can't really show it. But basically, you see that everything is not moving. We but we can see
[9:02] the noise quite easily. So we can see all that weird kind of black stuff. And one way to solve
[9:09] that area that I was just mentioning is really just a very simple method. So time echo. So we're


### Time Echo [9:12]
**Transcript (timestamped):**
[9:13] just averaging across different frames to reduce the noise. So again, if you have like flickering
[9:19] lights, like crazy, if you have, you know, characters passing in front, or, you know, there's a lot
[9:27] of stipulations that you're going to need to think about, if this method will work for you or not.
[9:31] But if you don't have those situations, this is a good method to do this. So basically, just do a
[9:36] little bit of time echo. And then you will just reapply it as a texture, and then back into
[9:42] perspective. So if you have no idea what I'm talking about, go watch the video on projecting and
[9:49] working in UV space, because this is this whole method right here is kind of covered. But basically,
[9:55] doing this through and with CG renders is really great technique. So that's one way to do it. And
[10:02] we get a better result like this. So if we take a look at the start, you see a little bit of it,
[10:07] the pattern still. And if we want to be really picky, we could blur some of that noise out. Or we
[10:13] could do dissolving framehold method, which I'm going to show in just a second. But you'll see if
[10:18] I play at least on the middle frames here, it's looking pretty good. You know, we're not seeing
[10:23] like this is this constant bubbling effect that we have here. No, see, we're seeing a much smoother
[10:29] result. And we're not paying attention to all the weird stuff down here. This is only for this area.
[10:33] So it's solving one area at a time. So that would solve that area. The other way we can do it is
[10:43] similar, but not exactly the same. So if we look at this back wall, we still want to maintain that
[10:48] lighting that's changing. So sometimes, you know, if you do the time echo method, you might not feel
[10:55] that sense of lighting changing in the same way you would. So another way to do it would be


### Finding Key Moments [11:02]
**Transcript (timestamped):**
[11:02] finding key moments and frameholding it and dissolving between them. So basically, what we can do is
[11:08] take this same render, project it onto that scene. So now we're projecting out of the back wall.
[11:15] So this is a different geometry. So let's just look at it. Close this stuff. So we see we're
[11:22] just projecting the live render camera is moving, we're not frameholding anything.
[11:27] And we're looking at it in the UV space. So we said, see it's set to UV. And again, we're doing a
[11:35] time echo. So you notice with specifically this one with the noise back here, again, it's that low
[11:42] frequency kind of big noise, we see those big like black chunks there. And at the start, it's
[11:48] pretty bad, you know, that that's not going to necessarily get solved by just a time echo. So
[11:53] rather than only doing a time echo, first, we can start with it to get just a slightly better
[11:58] result with in terms of the noise and the smoothness of it. So let's just see what that does. We just
[12:05] give it a second. And it will smooth it out a little bit. So you see it's already doing a little
[12:11] bit of a better job, but it's not perfect. So what we can do is find the good frames. So find good
[12:16] frames across the sequence. So what I mean by good frames is we just want to look where there's not
[12:22] that much stuff going on. So we can go forward. And maybe this is a good frame. But the next frame
[12:27] we would need to find is where the lighting changes. So we can look here and we see it looks more
[12:31] metallic. So we could say frame 88, and frame, I guess 104 is where the difference is because
[12:38] there's not much change happening in between. But it does the lighting does start to change
[12:43] around this point. So we would want to dissolve into this lighting. So that's what we're going to do.
[12:48] And the time echo it, which gets rid of some of the noise nature of it. Give it a second.
[12:59] And then we can frame hold on those two frames. And then we're just dissolving between. So we see
[13:03] here and here, we've taken those two good frames, and then I've taken it dissolved, and I've animated
[13:10] the basically which frame we're looking at across those frames. So on 88, we're looking at frame 88.
[13:17] On frame 104, we're looking at frame 104. So across there, we're just we're just blending between
[13:24] those two pictures now, instead of seeing all the bubbly kind of stuff happening in between,
[13:30] we're just doing dissolves. And that's a really common technique. If you're dealing with this
[13:35] problem is to take multiple patches, CG patches and blend between them. If you if you really can't
[13:41] solve the noise, this is going to this is going to work in a lot of cases. So that's a really
[13:46] powerful technique. And then basically, you can just reapply that as a as a texture and then run
[13:53] it back out as a render camera. So again, that's all covered in the UV baking tutorial. So go check
[13:59] that out. If you haven't seen it. So yeah, that will give us a nice result. And if we were to play,
[14:06] let's go to frame 88. And we would need to add more patches. So I only did it between these two
[14:12] frame ranges, but we would need to do it all the way through. But if we just let it play, it's going
[14:17] to take a little bit to load here, because it's still kind of a heavy scene, you see that there's
[14:21] really we've knocked out almost all the noise on that wall. And we're still getting the lighting
[14:26] changed towards the end there where we get the reflections coming in. So we might need to change
[14:31] the timing that dissolve, just to make sure that the timing of the light is still exactly the same
[14:37] if you want to be really picky about it. But I think the method is there so you guys can understand
[14:41] it. So I'm not going to be like too picky with my own project here. So this is what we got.
[14:49] And one other thing we can talk about is the non free method. You know, if you have a new


### Non-Free Method [14:51]
**Transcript (timestamped):**
[14:56] indie or you have your own new license or you're working in studio, you probably already know about
[15:01] this. This is neat videos product reduce noise. And this, I mean, it's just, I don't even know
[15:09] how this thing works, but it's just an amazing denoiser. And I think it's still the best in the
[15:14] industry. And, you know, it's intended for film grain or sensor noise, but actually it works really
[15:22] well and CG stuff as well. So basically, if you take a reduced noise, this is the non free way
[15:27] of doing it. But if you take a reduced noise, you know, some of the high frequency stuff down here,
[15:32] if we put a reduced noise on that, it just knocks it out completely. So it's a really,
[15:36] really awesome way of doing that. And you see, we're not having to crank up the samples in,
[15:42] in a render engine to try to, you know, get rid of all of the noise in a glossier area.
[15:48] So that would basically solve it. And that's how we solve three different areas,
[15:52] slightly differently. But all the concepts kind of tied together there. So that's basically it
[15:57] for this tutorial. You found it useful. Hit that like button. And it really helps. And thanks so much.



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
