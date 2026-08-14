---
title: Compositing EPIC VFX Godrays | Nuke Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=PqbqxnBFOHg
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/compositing-epic-vfx-godrays-nuke-tutorial/
frame_count: 0
frame_status: pending-selection
---

# Compositing EPIC VFX Godrays | Nuke Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=PqbqxnBFOHg)
**Author:** Compositing Academy
**Duration:** 18m0s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py compositing-epic-vfx-godrays-nuke-tutorial <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] If you've ever went walking in the morning, you've probably seen something like this before.
[0:24] Rays of light passing through mist or atmosphere.
[0:27] In this tutorial, we're going to be talking about the interaction between the rays of
[0:31] light themselves and the pools of light that are created on the surface that it's being
[0:36] projected onto.
[0:38] This is a method that can be used for full CG environments.
[0:42] You can also mix this method with plates and stuff like that, but it's great for having
[0:47] a light that's actually including shapes that we can see and the light source is kind of
[0:52] moving.
[0:53] We have clouds or we have something passing over.
[0:57] That's what this sweeping light effect is kind of good for.
[1:02] Towards the end of this tutorial, we'll look at how to get some of the particles in there,
[1:06] how to make those cut into the god ray, and how to get multiple layers crossing over each
[1:12] other, and also some problems that we can run into with screen space god rays.


### Basic Godray [1:15]
**Transcript (timestamped):**
[1:19] If we start looking at this and we look at the most basic god ray, this would be one
[1:24] possible approach of making a god ray.
[1:26] You kind of create some kind of alpha.
[1:29] We punch a few holes in it and that's what we want to create the god ray through.
[1:33] So we would kind of put it into position and put the god ray node.
[1:38] And when you have the god ray node, you can move the center around so we could put it
[1:41] here and we could either scale up.
[1:43] You could also scale down from another direction, but essentially the same thing.
[1:46] We get some rays from that and you can adjust the size with your noise.
[1:51] So you can adjust those ray sizes by reducing the noise size or adding contrast by gamma
[1:57] and down.
[1:59] So this pattern is kind of helping it.
[2:02] So the same thing here.
[2:05] It's the same exact idea with a volume rays node.
[2:07] Pretty much works the same way.
[2:09] Just a little bit different way to control it, but you can put the volume ray node behind
[2:13] and you put the position kind of behind that light source and it'll do that effect.
[2:19] Now if we want the god rays to actually interact and create pools of light, this technique


### Interactive Ground Godray [2:20]
**Transcript (timestamped):**
[2:24] is not going to be the way to do it because we need to have an alpha that represents the
[2:27] ground.
[2:28] So the trick with this is to actually flip it.
[2:31] We want to create the interactive matte first.
[2:35] So we want to start with noise.
[2:38] We actually want the noise to be kind of on the ground.
[2:41] So I'm going to show this with a CG environment after.
[2:43] I'm just doing a quick 2D example first.
[2:46] So the noise here, we're just doing a corner pin and kind of getting it on the ground.
[2:52] And rather than god rain down from a light source, we're actually god rain through these
[2:57] sort of interactive points.
[3:00] So we create the god ray node and we scale up.
[3:04] So I put the center up where the light source would be and I scale basically down, which
[3:08] creates this sort of god ray.
[3:13] What that allows us to do is to have a matte that represents both the god ray, which is
[3:17] this, but also the interactive point.
[3:20] And so if I gamma down this matte here to something that looks like this and we merge
[3:27] these together, you can see that each god ray is getting its own pool of light at the
[3:32] bottom.
[3:33] And when we animate this noise, it's going to look like the god rays are actually casting
[3:37] light on those positions.
[3:40] So we have the rays actually matching up.
[3:42] And we could of course blur this a little bit if you wanted.
[3:45] And we can control the mats independently, or we could even, you know, gamma up and have
[3:50] a bit more god rays or however you want to do it.
[3:53] But fundamentally, this is the idea.
[3:57] But with a CG environment, we can do the same thing with a position pass.
[4:01] So we can create a 3D noise with not a 3D noise, but a 2.5D noise that runs across the
[4:07] position pass.
[4:08] And fundamentally do the same exact trick with the CG environment.
[4:11] So that's what we're going to do in just a second here.


### Godray on CG Position Pass [4:15]
**Transcript (timestamped):**
[4:15] So if we go here and we take a look at the position pass, this is what we need to do
[4:20] to create that noise running across the surface.
[4:24] So to do that, it's actually pretty easy.
[4:26] We can do a expression.
[4:29] And what we want to do in the expression node, we have the color channels here.
[4:33] I do have a video on my channel that goes into this, how to make this a tool if you
[4:37] want, kind of a 2.5D noise that you can kind of tool up and use again.
[4:44] But in this case, we don't actually need to do that.
[4:46] All we need to do is go to the last box here, which is the alpha.
[4:49] And we want to type noise RGB and with commas in between like this.
[4:56] And if we look at the resulting alpha of that, you notice that we have a noise pattern all
[5:01] over the surface.
[5:03] So this is great, but it's not moving.
[5:06] So we can't do anything with that.
[5:08] So we want to put a grade node just before.
[5:13] And in the grade node, you see it breaks.
[5:15] So first thing we want to do is uncheck the black clamp because the position pass has some
[5:19] negative values and stuff like that to make it work.
[5:22] And that's killing it.
[5:23] So we want to turn that off.
[5:25] And what we can do now is pretty interesting.
[5:28] To make this animate, we want to go to the offset and we can actually just increase this.


### Adjusting CG Godrays [5:29]
**Transcript (timestamped):**
[5:33] And you'll notice that the noise will actually flow across the surface.
[5:37] So this is how we can create the base for our interactive effect here.
[5:42] There will be one problem with doing this is if you offset it and you sample and you
[5:46] look at the alpha that we're creating, the value.
[5:50] If we go kind of like negative with this, you'll notice that we have some negative values,
[5:55] which is not good with alphas.
[5:56] We want to have 0 to 1.
[5:58] So after the expression, you'll need to put a clamp so that we have a nice 0 to 1 alpha.
[6:03] And that's what we have now.
[6:04] So what we can also do is replace the red, green and blue channels so we can get rid
[6:09] of this position pass.
[6:10] And we want to replace all the channels with this resulting noise pattern that we've created.
[6:15] So we can just put a shuffle node at the end and say we want to put alpha into all the
[6:20] channels like this.
[6:21] So if I hit RGB and A, all the channels look the same, which will work really well for
[6:25] when we put the God Ray effect on top of this.
[6:28] So we have these nodes that's kind of creating it and we have this node that we were doing
[6:33] the offset.
[6:34] So that's where we can go back and animate it.
[6:37] The other thing we can do here is we can actually go to the gain or the multiply and we can
[6:42] actually go into the colors and we can increase the scale if you want to make it bigger in
[6:48] one direction.
[6:50] So we have X, Y and Z represented here.
[6:53] So you can basically just play around with these and see how you like it.
[6:58] Same with the offset.
[6:59] That's kind of offsetting it in all directions sort of, but if you want the God Ray to flow
[7:03] in one direction, you can go into the offset and just offset one of the colors and you
[7:08] see it flows in one direction now.
[7:10] So if you're creating a cloud passing over, this is actually a really great way to get
[7:17] those light effects all over your environment.
[7:21] So this is pretty cool effect.
[7:23] Now all we need to do is create the God Ray.
[7:25] So I'll just go here.
[7:27] We have some kind of gray background first.
[7:29] So I'm going to fix that by masking based on the beauty.
[7:33] I'll just mask that so we don't have that kind of gray because I have the alpha here
[7:38] of the actual scene, which is like this is just like the base, base render.
[7:45] And now we can mask that and we're good.
[7:47] Now we're ready for the God Ray.
[7:49] So I'll put a God Ray node here and we will put the center up in the corner and close
[7:56] these panels.
[7:58] Take a look at that and we'll just decrease the scale a bit.
[8:02] First thing you'll need to increase the steps here so we can increase that to a higher number,
[8:05] let's say 10.
[8:06] You can also hit max, but you know, that's not going to be what we want in this case.
[8:11] So we can move this up and scale it down and we can move it up further.
[8:20] And that's kind of good.
[8:22] We can gain this up a little bit, see how it looks.
[8:25] It's a little bit easier to tell once we start looking at a scene though.
[8:29] So if we take our two mats that we've created, this one and this one, let's apply it to the
[8:38] actual base beauty of the scene.
[8:40] So first I'll take the interactive mat and I'll just kind of gain down everything except
[8:47] the light rays.
[8:48] So I'm going to take the grade, I'm going to invert that so there's a little invert button
[8:52] and gain down.
[8:54] So now we're getting the spots that are only, you know, kind of in the alpha here.
[9:01] We can also do the opposite so we can do the same mat, but not invert it and we can just
[9:07] kind of gain up a little bit so we can see what's happening.
[9:11] And so maybe that's too small of lights, but we'll see how it looks.
[9:15] We'll take the God rays and we'll kind of plus this over or we can do it over.
[9:20] Over it actually better in this case.
[9:22] We kind of want it to include and not brighten the highlights necessarily.
[9:27] So over is fine.
[9:30] And this is kind of what we have.
[9:31] Now this is too bright so we can bring this down a bit.
[9:35] And to make this look better, I think we could just make the noise much bigger.
[9:40] So now we can start to play with the noise size and see what that looks like.
[9:46] Part of the problem is, yeah, we just need to have big, big pools of light being created
[9:52] to make that a little bit more convincing here.
[9:55] We can also match the color a bit better.
[9:57] So you know, these are white, whereas it feels like we have a bit of a warmer thing.
[10:02] You know that the material is warm itself.
[10:04] I think it just looks a bit more natural if we throw a tiny bit of color into it.
[10:11] Another thing we can do is in the God ray setting, there's from and to color.
[10:16] So you can basically like kind of fade off the ends of them a little bit so it feels
[10:21] like it's not just like completely sort of a linear effect, but rather it's kind of falling
[10:26] off from a source and that's going to help.
[10:31] So let's just see what else can we do here.
[10:33] Yeah, so I'll make the spots a little bit bigger.
[10:36] So I'll go back to our little size control that keep going back and just keep playing
[10:41] with the size and just see what we can do here.
[10:47] Let's just play around with the scale.
[10:49] I think it just needs to be something probably like this.
[10:55] Sometimes you get a bit of a harsh fall off because of the noise that we used.
[11:00] So you get these sort of harsh edges.
[11:03] If we look at the alpha, we can actually see that.
[11:08] So what we can do is we can actually blur this alpha a bit as well.
[11:12] So if I go here, blur the alpha and then I'll just put this back over itself.
[11:20] So we get this kind of like foggy looking effect around it and we can take a look at
[11:25] what that looks like.
[11:27] And you see how it kind of softens the edge a little bit so we're not getting such harsh
[11:32] edges and it feels a little bit more natural.
[11:35] That allows us to kind of control how broad those rays go and starts to look a bit more
[11:41] realistic.
[11:42] Now, we're going for a pretty contrasty scene so we're going for like dark shadows and stuff
[11:47] like that.
[11:48] If we had a fill light, we could play it like that too where we don't completely gain to
[11:54] zero here.
[11:55] We could have some fill if we want so we could just kind of bring it up a tiny bit.
[12:01] But I kind of like the contrasty look.
[12:03] It gives it that really dramatic sort of spotlight effect.
[12:07] And that's kind of it.
[12:08] That's kind of how we can get the effect and you just play with the noise and you could
[12:11] do more than one noise pattern.
[12:13] So we have like the big, broad one that we've done now and we can animate that sweeping
[12:17] through so we can just play with our offset and that's just going to feel like those
[12:23] rays are going through.
[12:25] So if we were to keyframe that over time, that's what that's going to look like.
[12:29] So you could do like a helicopter or something.
[12:31] You could do some really crazy stuff this way.
[12:34] And even if it was just one singular alpha with a P-mat, you could do the same idea here.
[12:42] So I think that's pretty much it for this effect.
[12:46] I'll go into the comp now to show how I did just some of the particle effects being mixed
[12:54] in there.
[12:55] But fundamentally it's just this and then playing around a lot with like the look and
[12:59] the timing just to really dial it in.
[13:02] Maybe you could make your fall off look nicer.
[13:05] You could, you know, once you break up the rays as well, it helps a lot.
[13:09] So we're going to talk about that.
[13:10] But fundamentally the main techniques are not that complicated.
[13:16] It's always just about dialing everything in, which means the motion, how much of it
[13:21] on certain parts of the sequence.
[13:23] Like if you're starting a shot versus your end, what are you trying to tell here?
[13:28] The other thing I guess I could mention is let's go here to my actual comp.


### Script Example [13:30]
**Transcript (timestamped):**
[13:34] So this is the one that I did and we can just step through.
[13:39] So I created the alpha here and then I basically just got ray it from that.
[13:45] And then we kind of put it over.
[13:47] But I did also do a negative God ray from our object that's passing through.
[13:52] And basically you're just taking the alpha of this thing and doing a God ray from that
[13:57] alpha.
[13:58] So if we have the alpha of the triangle and we're doing a God ray, we can create something
[14:04] like that.
[14:05] And we can also row to it on certain parts to just make it a little bit sharper if we
[14:10] need to and kind of cut into the God ray to make it look like the object is passing
[14:14] through.
[14:15] And when you're doing that, you can basically the mouth that you stencil it will make it
[14:22] look like it's further inside or rather the God ray is closer to the camera and not blocking
[14:29] the object.
[14:30] So if I put it at zero, it looks like this object is sitting behind the God ray versus
[14:35] one where it feels like it's cutting it out.
[14:37] And you can always play with it somewhere in the middle too, especially if it's passing
[14:40] through.
[14:42] This is something you'd probably want to animate.
[14:44] So that's something to keep in mind.
[14:46] So we'll talk about the particles next.


### Godray Dust [14:50]
**Transcript (timestamped):**
[14:50] So for the dust element, I have a whole bunch of dust elements here that I kind of brought
[14:55] in.
[14:56] But essentially without the dust element, we have something that's just like the God ray.
[15:00] And then when you start to bring it in, it just gives a bit of texture to that light,
[15:05] which is really pretty awesome.
[15:07] Now not always is that the case because it depends on the particle size in the air.
[15:13] If you have a big cloud or like steam over a lake or something like that, the noise is
[15:19] going to be bigger.
[15:20] Or if you have fine particles of dust in the air, maybe it's a garage, they're going to
[15:25] be smaller.
[15:26] So it's not always just random particles in the air.
[15:30] You got to think about the size of the particles or the kind of volume you're shining light
[15:35] through.
[15:37] So that's kind of what we have here.
[15:39] Some finer dust that's blowing around.
[15:42] And basically, yeah, it's just a clip of some dust here.
[15:46] And the trick here is to take the alpha or not the alpha, the RGB and alpha if you want
[15:54] and multiply it against that image.
[15:57] So if I have that disabled, you see I kind of graded it just a bit brown and then I'm
[16:02] just multiplying a precomp of the God rays that I did up in the top of the composite.
[16:08] So it just kind of helps cut it out, makes it feel like the light is hitting all those
[16:13] particles on that layer.
[16:16] And it starts to become more convincing the more layers you add.
[16:19] So I added a whole bunch of different layers here.
[16:25] Some at different depths.
[16:26] You notice we're out of focus in the foreground.
[16:29] So I added some particles just in the foreground that pass over everything just to give some
[16:33] sense of scale and distance.
[16:36] So those are things you want to think about.
[16:38] And we'll just step down all the way here.
[16:41] And then there's some lens flare stuff going on that I might do another tutorial on some
[16:45] of the lens flare stuff.
[16:46] But that's kind of just of it.
[16:49] I did do a bit of a sharpening like crazy on this just because it's going on YouTube


### Improvements [16:50]
**Transcript (timestamped):**
[16:53] and Vimeo and compression kills really small particles.
[16:58] So it's almost like invisible.
[17:00] So I kind of sharpen it like almost too much on purpose.
[17:05] But yeah, that's kind of the effect.
[17:07] And this is the overall look that you can get.
[17:10] Again, you can go further with this.
[17:13] If this is like feature film and you needed some god rays, for example, like something
[17:18] you could do even more.
[17:20] You have like the shadow cutting out.
[17:22] You could put another god ray behind.
[17:25] And just so you see some shapes in that cut out or just some stuff going on in the background
[17:29] subtly or even some very foreground subtle god rays coming over the camera.
[17:35] You could flare up this corner and have have some subtle hazing coming from off screen.
[17:41] So there's all kinds of more things you can do depending on the amount of time you want
[17:45] to spend on things.
[17:46] So you know, I'm not going to spend time on this, but I think this is a pretty cool result.
[17:50] And hopefully that was useful for somebody.
[17:53] So if you guys liked it, hit the like button or subscribe if you're not already.
[17:58] And that's about it.



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
