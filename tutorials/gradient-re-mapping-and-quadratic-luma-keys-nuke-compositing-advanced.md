---
title: Gradient Re-Mapping and Quadratic Luma Keys | Nuke Compositing [Advanced]
source: YouTube
url: https://www.youtube.com/watch?v=yLnSZxwlOyA
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/gradient-re-mapping-and-quadratic-luma-keys-nuke-compositing-advanced/
frame_count: 0
frame_status: pending-selection
---

# Gradient Re-Mapping and Quadratic Luma Keys | Nuke Compositing [Advanced]

**Source:** [YouTube](https://www.youtube.com/watch?v=yLnSZxwlOyA)
**Author:** Compositing Academy
**Duration:** 15m7s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py gradient-re-mapping-and-quadratic-luma-keys-nuke-compositing-advanced <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey everyone, welcome to another tutorial. This time we're going to talk about gradient remapping inside of Nuke and what exactly that is and how we can use it.
[0:15] So if you guys are familiar with Photoshop, you might be familiar with a technique called gradient remapping, which is essentially just taking a black and white image like this and remapping multiple color values into it.
[0:29] So from the 0 to 1, so white being 1 and 0 being black, we can shove a bunch of different color values into that range.
[0:39] And essentially we can actually do this in Nuke and I don't think a lot of people are aware of this technique with the ST map.
[0:46] So normally how we use an ST map, you guys should already be familiar as this advanced tutorial.
[0:51] It's basically just for UV sticking textures onto UV renders out of CG.
[0:58] So that's mainly what it's used for, but we can use it for a variety of different things.


### Examples [1:00]
**Transcript (timestamped):**
[1:03] So this technique is actually really great for a couple different things, flares, skies, fire jet engines, underwater light fall off and whatever galaxy kind of space effects you're doing.
[1:15] So if you have that, I'll pull it open here.
[1:20] So here's a couple different examples visually.
[1:22] So obviously skies are going to benefit a lot from this because there's a lot of gradation in there.
[1:29] So we can see some jet engines have a lot in there.
[1:33] So we have some white going to orange and then on the very edge is kind of pinkish tone.
[1:37] And even though almost looks like some kind of white on the edge, maybe some air or something like that.
[1:44] So these kind of effects really benefit from this fire is another good one.
[1:49] Underwater effects, volumetric depends on the camera and the lighting, but you know, even here we can see it's kind of white in the center, kind of falling into a very light desaturated purple and then into these kind of blueish tones and then also into these darker tones.
[2:05] So if you were to do that traditionally, you're going to have to stack a lot of basically radials and color grades and keyers and stuff like that to try to get that nice fall off.
[2:16] Again, lens flares and all that stuff.
[2:19] So if we get into exactly how we can do this, it's pretty simple.
[2:24] Basically, I'll just create a scratch one here, put a radio and we'll grab an ST map.
[2:32] And make sure that the ST map portion is plugged into the image that you're putting into it.
[2:38] You want to remap the colors and the colors that you want to remap goes into the source.
[2:43] So I'm going to take a constant, choose a color and we'll just grab something here.
[2:48] And maybe we'll go with this kind of weird color and plug that into the source.
[2:55] And so what you want to do in here is you want to go to the ST map and switch the UV channels to RGB.
[3:01] And we can check off one of these channels.
[3:05] So it's only going to grab one basically alpha from whatever channel you're selecting.
[3:10] So I'm just going to turn off the green channel just so it's grabbing only the red channel from this radio.
[3:16] And essentially the way this works is pretty weird, but it's kind of like this.
[3:22] So if I show you essentially what you put in the bottom left corner is the black.
[3:27] So if you look here at a radio, that would be this area around and then on the right side is the white.
[3:35] So that's how the colors are going to remap.
[3:37] So if I put this green cube, I put a transform, put it on the left side.
[3:44] And also the way this note is working is kind of tricky.
[3:48] It's only looking at the bottom row of pixels.
[3:51] So if I put the green cube here and I look at it, nothing's going to happen.
[3:55] But if I put this green cube on the bottom and I turn this and I look at this, you can see it's starting to do something here.
[4:02] So we can see something's happening.
[4:03] So let's put another color, copy paste it, stick it in and let's change the color to something else and move it next to it.
[4:15] So again, if you remember, I said on the left side is black and on the right side is white.
[4:20] So if you look at our picture here, where it's more white is going to appear more, this purple color.
[4:27] So essentially it's already doing the remap.
[4:29] And if I blur our colors together, we'll get a nicer fall off.
[4:33] So if I just blur the colors a little bit like this and now I look at the ST map, we can see that it's starting to do that gradient remapping effect.
[4:44] One thing you can do is if you're not liking how the colors are kind of falling off here, we can shift them around essentially with these transforms.
[4:54] So if I shift one of these colors further over to the left or further over to the right, it's going to shift essentially where those colors are remapping into our 0 to 1 image.
[5:06] So for example, if I want, let's go to our image here and we'll mask it by the radio just so we can see exactly what that's looking like.
[5:14] So this is what our image is looking like.
[5:16] If I want more green in that image, I'm going to go here and I'm going to pull this purple over just a little bit.
[5:24] So we have more green and I'll just pull the green over and scale it up.
[5:30] Again, it doesn't matter what's happening up here.
[5:32] It only matters the bottom pixels on the frame.
[5:35] And I look at this.
[5:36] So now you can see we have more green inside of that picture.
[5:40] And again, I could just take the X, translate and move it back and forth and I can slide those colors around how I want.
[5:49] And it's going to be better if I give alphas to these.
[5:54] So I'm going to use a shuffle node here and just make sure we have alpha on both of these constants so that if they are overlapping,
[6:03] we're not going to get some kind of transparent color shift there.
[6:12] So that's kind of what we do.
[6:13] We have just a constant solid alpha.
[6:15] We can translate them left and right and that's going to decide where the colors are remapping in this image.
[6:22] So if I put a transform here, it'll be easier and I can just shift it.
[6:27] So I type negative 50 and I just kind of play around.
[6:31] You'll see that that color is sliding around in our radio.
[6:35] So that's essentially the concept.
[6:38] Now, of course, you can...
[6:40] So I'm going to go here in this example.
[6:42] So this is the example I had here and I masked it.
[6:45] So that's the example and I can take the transform I put after the two of these guys and shift it around.
[6:53] And you'll see that that's giving a nice effect there.
[6:57] So, of course, you can add more colors.
[7:00] So here's three colors being put in and again, only the bottom pixel matters.
[7:05] So it doesn't matter if they're not stacked.
[7:08] You can just kind of quickly place them and you'll get an effect like this.
[7:12] If I turn the blur off, you'll see it's a very harsh remap and I'm just using a normal radio.
[7:18] And if I shift them around, I can see that that's shifting around in the way that I would expect.
[7:24] And I can blur that together and get a nice result and mask it by itself because this is kind of destroying the alpha there.
[7:33] So we'll just kind of mask it back and get something like that.
[7:36] So that's going to give us something we can actually use and make a lens flare or whatever you're doing.
[7:39] And that's going to work for any black and white image.
[7:43] So again, if you have a roto shape, you can remap the roto shape through a feather.
[7:47] So I'm just feathering this roto shape here.
[7:49] We just look at it.
[7:50] It looks like that.
[7:51] The remap set to the red channel and essentially that's the effect.
[7:58] So that's pretty cool.


### Quadratic Luma Key [8:00]
**Transcript (timestamped):**
[8:00] Some other examples of what I did with this.
[8:04] This is not necessary, but I took this concept a little bit further and made a quadratic Luma key tool.
[8:13] So I use this in my Nuke 4.4 class.
[8:16] If you guys are interested in taking that, it's more of an intermediate course, kind of mid-level sort of.
[8:21] It's available in the description below if you're interested.
[8:25] Advanced color grading and relighting.
[8:28] But essentially what this Luma Nets key does is if we open it up, I'll just show you what it is.
[8:36] Essentially what I'm taking here is the same gradient remap technique.
[8:39] So I'm using the ST map, but I'm using essentially roto shapes with a quadratic falloff inside of them.
[8:47] And this is going to give us a nice roll off of the highlights, unlike a normal keyer.
[8:52] So a normal keyer is going to give us something like this.
[8:55] So if I go here, just set these back to default.
[8:59] Let's say, like my previous tutorials, if you looked at my YouTube channel, we're talking about glossiness.
[9:05] On some asphalt.
[9:07] Normally you'd have to stack a lot of keyers to get nice, pingy highlights on some rocks like this.
[9:13] So I would have to go here in my Luma Nets key and I would have to try to isolate.
[9:18] Okay, let's just try to get the very highlights on some of these rocks.
[9:22] Okay, that's going to work for the pings of the rocks.
[9:25] But what if I want some highlights around those rocks?
[9:29] Well, I'd have to go here with another keyer and do something like this.
[9:33] And then I had to stack these together and it's kind of a process.
[9:37] So basically I created a tool called Quadratic Luma Key, which kind of does this automatically.
[9:43] So it's using this exponential glow.
[9:49] And essentially when you're shifting the key, it's just sliding it left and right in this ST map.
[9:54] So it's doing the same thing I just showed you with the colors, except we're doing it with this quadratic falloff effect.
[10:01] And it's really not advanced or anything.
[10:03] A few guys are like tool makers out there. You're probably looking at this like it's really simple.
[10:07] There's people out there definitely better than me at making tools and stuff like that.
[10:11] But I think this is pretty useful for what it is.
[10:14] So basically if I shift that key around, you'll see that not only am I getting some broad kind of key in there,
[10:22] but I'm also getting the little pings of highlights automatically.
[10:26] So I'm not having to stack a bunch of keys.
[10:28] Again, if we go back and compare, we see that's kind of flat and then we have the pings, but they're not together.
[10:34] So this quadratic luma key is kind of doing that.
[10:37] And I can adjust the gamma over the multiply in there as well.
[10:42] And there's different modes that I put in here as well.
[10:44] So you can switch the type of falloff if you want to play around with that.
[10:48] So this is free. If you guys want to download that, the description below as well.
[10:52] Quadratic Luma Key. You can open it up and see how I did it.
[10:55] It's basically the same as this, but just using what I just showed.
[10:59] So this is also a really good technique for remapping P-bubbles.


### Remapping P Bubbles [11:00]
**Transcript (timestamped):**
[11:05] Sometimes P-bubbles have that already in there in kind of in the settings, but a lot of times they don't.
[11:12] And sometimes you want a quadratic falloff in a P-mat.
[11:16] For example, if you're relighting a CG scene, you're going to want that nice falloff in your alphas to kind of create lights in that scene.
[11:24] So, yeah, by default, a lot of times it doesn't have the right falloff you want.
[11:29] So essentially you can take a normal linear kind of falloff like this radio here.
[11:34] And I can just chuck on a quadratic luma key and just play around with the key.
[11:39] And you're going to see that it kind of gives it that quadratic look pretty quickly.
[11:43] And I don't have to do that much to it.
[11:47] So that's kind of how it works.
[11:49] And I can just switch the mode and it's going to give me different falloffs on that alpha.
[11:54] So that's pretty useful as well.
[11:56] If you're doing, you know, maybe you're doing a car driving at night and you want to draw some headlights.
[12:02] Normally you'd have to mess around with a roto shape and it's kind of annoying.
[12:08] Let's switch this to RGBA.
[12:12] So this is the quadratic luma key.
[12:14] I'm going to pull that out so it has the effect that I want.
[12:21] Something like this.
[12:22] And you see that the way it's falling off kind of feels quadratic.
[12:26] And you can slide that key around like this.
[12:33] So the roto shape by default does have a couple of settings in here.
[12:37] You should probably know if you're an advanced user, but sometimes it doesn't look the same way that you want.
[12:41] So just keep that in mind.
[12:44] And that's basically it.


### Other Examples [12:45]
**Transcript (timestamped):**
[12:46] So here's another practical example, I guess, of using this technique.
[12:53] So we have a black and white image.
[12:55] And one thing that this technique doesn't like is super whites.
[12:59] So if you have some values that are over one, it's going to sort of break.
[13:03] So again, this kind of square that's searching the bottom pixel is looking for zero to one values.
[13:10] So I'm usually looking for things past one.
[13:13] But if you really want to do some super whites, I've played around with converting the image to log space and then doing it there.
[13:20] And you can kind of get away with some stuff.
[13:23] So you can play around with different techniques to do that.
[13:28] But usually zero to one is fine.
[13:30] And then you can grade that image as well as your control image.
[13:34] So if I remap that to the colors I'm putting in, so I have a couple of like sunset type of colors here.
[13:39] I can put a grade beforehand and just essentially adjust the fall off of those colors quite easily.
[13:49] You see, if I go past one and starts to break, so if I put the white clamp, it's going to fix that problem mostly.
[13:57] So if you still push it around, it's sort of weird, but generally zero to one is working pretty well.
[14:06] And yeah, that's pretty much it.
[14:08] And the other thing here, so I just, this is another example here.
[14:11] So you can see this is three colors.
[14:15] And that's giving this result.
[14:17] And then we can put a fourth color like the blue in there.
[14:19] And we start to get some more blue in the shadows.
[14:22] And we have some very like slightly magenta in the very dark shadows.
[14:26] And I can shift that around with my transform.
[14:31] So if I shift it around here, you can see that's how it works.
[14:36] Sometimes I use this as like a base image.
[14:39] So I'll use this ST map kind of as like a base color contamination image.
[14:45] And then I'll just multiply that against the original.
[14:47] So I'm taking the original picture and multiplying that color result.
[14:52] So we can kind of mix the two and get better lumens kind of range there without having to mess around too much.
[15:00] So that's basically the concept.
[15:01] Hope you guys got something useful out of the video.
[15:03] And hit like if you liked it.
[15:05] And thanks so much.



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
