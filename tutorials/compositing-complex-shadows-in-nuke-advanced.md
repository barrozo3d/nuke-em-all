---
title: Compositing Complex Shadows in Nuke [Advanced]
source: YouTube
url: https://www.youtube.com/watch?v=Yb3Cn3JnkUI
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "not specified (2021 upload, Nuke 13.0 era — see version-tracker.md)"
tags: [compositing, relighting, grading, roto, channels, gizmo, color-management, advanced]
extraction_status: complete
frames_dir: tutorials/frames/compositing-complex-shadows-in-nuke-advanced/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Compositing Complex Shadows in Nuke [Advanced]

**Source:** [YouTube](https://www.youtube.com/watch?v=Yb3Cn3JnkUI)
**Author:** Compositing Academy
**Duration:** 19m13s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Traditional Methods for Shadows [0:00]
**Transcript (timestamped):**
[0:00] Hey everyone, welcome to this advanced compositing tutorial about creating complex shadows in Nuke.
[0:15] So you might be wondering why this is an advanced tutorial and you're seeing a cube here sitting
[0:18] on the ground.
[0:21] And if you guys are familiar with basic CG compositing, taking an alpha and kind of multiplying
[0:26] it down against a plate, you might not know that it can get a little bit more complicated
[0:31] than that.
[0:32] And this is an example of where this kind of happens.
[0:34] So we have this cube here sitting and it's passing across some other shadows.
[0:39] So we have what are called double shadows.
[0:42] And basically we don't want to create a double shadow in those areas, otherwise it's not
[0:47] going to look right.
[0:48] So if we look at the traditional way of doing this, I'll go to a little example here.
[0:53] This would be method one.
[0:54] So I'm going to split this into different methods and talk about some things as well
[0:58] as some advanced methods.
[1:00] We can make this a little bit better as well.
[1:03] But if we want to just look at the basic method, we have a normal alpha.
[1:07] It's kind of a crappy one, but good enough for the tutorial.
[1:09] I've just kind of eroded it and graded it to kind of make that a little bit better.
[1:15] And a slight edge blur and then we just kind of stick it on the plate with a grade and we
[1:20] have a cube.
[1:21] And if we just let that play, we can immediately, hopefully immediately see the problem.
[1:27] And basically we have a double shadow, which that's not what's going to happen in real
[1:31] life.
[1:32] And so we need to deal with this as a compositor.
[1:35] So one way of doing it would kind of made this one yellow because sometimes it works
[1:39] and sometimes it doesn't.
[1:41] This would be the quick solution if you want to quickly just try to get something real
[1:45] fast.
[1:46] What you could do is take the footage, take again that same grade, but stencil out the
[1:54] dark areas from that grade.
[1:56] So we would stencil it and that kind of works, but it doesn't give the best edges sometimes
[2:00] and you can see it's not blending perfectly.
[2:03] So that's not the best way of doing it.
[2:08] And then we can talk about this method.
[2:09] So it's a shadow clean plate.
[2:11] There's many ways to do this.
[2:13] Some people are using some advanced merge operations.
[2:16] I've seen some people talk about that online.
[2:19] My method is pretty straightforward.
[2:21] It's relatively simple, but there might be better ways.
[2:24] But in general, it's worked for me.
[2:25] So this is what I'm going to talk about in this example.
[2:30] So before I get into the full method, this would be, this is what we're going to talk
[2:36] about as well.
[2:38] So shadow attenuation.
[2:39] I've made a full video on this, but your first instinct when you're composing this
[2:44] cube might be to simply kind of blur this cube to match the shadow of the plate.
[2:50] And that wouldn't actually be correct because we have to understand what's happening with
[2:55] shadows in real life in order to composite them realistically.


### Shadow Attenuation Explained [2:58]
**Transcript (timestamped):**
[2:59] So yeah, go check out that video.
[3:01] It's one of the first ones I posted, but basically it's this concept, which is it's not only
[3:06] the light size that determines the softness of a shadow, it's also the distance to the
[3:10] object.
[3:12] So this is a pretty good example scene because we have this tree where if we look at the
[3:16] shadow, if we look at the base of it, it's about this thick, we can kind of circle the
[3:22] attenuation here, the feathering.
[3:25] And we can look here and it's a little bit smaller.
[3:27] And then towards the base, it's starting to get sharp.
[3:29] So we know that it's pretty much direct sunlight and it's giving us sharp shadows, but the
[3:33] taller and further way that shadow is from the object casting it, the softer that becomes.


### Other integration stuff [3:40]
**Transcript (timestamped):**
[3:40] So we'll kind of talk about briefly how to make that.
[3:43] And then also some other things I did with the shadow that makes it a little bit better
[3:47] than just a CG shadow on a plate, which is I've kind of faked some reflections in this
[3:53] cube.
[3:54] So if we look at the original CG cube, let's go here just to the basic comp, we can see
[4:01] it doesn't feel like this light is kind of interacting with the cube.
[4:05] So what I've done is kind of rotoscoped in and created this fake reflection from where
[4:10] the really bright areas are.
[4:12] So that just kind of gives us illusion that there's a you can actually see reflection
[4:15] on the ground and kind of a reflection of the shadow.
[4:18] So I've kind of just wrote that and then also on this side as well, we have this really
[4:21] blown out area.
[4:22] So we just want to integrate that a little bit better with some some grades.
[4:26] So those are all things we can do.
[4:28] And the last thing that we can do is if we let this play, this still feels pretty CG
[4:33] if you just look at the original.
[4:35] And one of the reasons is this is because the shadow is perfectly casting onto a flat ground
[4:41] and usually CG grounds are going to be flat, they're not going to be matching perfectly.
[4:44] So what you can do is do some eye transforms and some noise patterns to kind of make this
[4:50] shadow ripple across the surface.
[4:52] So you see these trees, there's kind of indentation into the road.
[4:56] So we want that CG to kind of copy that.
[4:59] So if we play this, we can see that it's kind of changing shape.
[5:02] If you look closely at the edge, it's kind of rolling across the surface of this dirt
[5:07] road or or kind of appears to be so we're kind of giving the illusion of that.
[5:12] So I'm going to talk about the method now and kind of go through this part.
[5:17] So this is the more advanced part.
[5:18] We're going to talk about the color space we can work in here.
[5:22] So basically what this method consists of is we want to create a rather than just grading


### Shadow Cleanplate [5:25]
**Transcript (timestamped):**
[5:26] down and using a multiply, we want to create what's called like a shadow clean plate.
[5:33] And essentially what that looks like is something like something like this.
[5:37] So we want a greater footage in a way that kind of flattens it out.
[5:40] So we want to squash the highlights and kind of roll them off and get them really close
[5:45] to where the shadows are.
[5:47] So this method kind of does that.
[5:49] And then we basically will just mask that through our alpha.
[5:53] So we have our alpha of our cube, our shadow.
[5:57] And we're just going to mask that clean plate and merge it over.
[6:00] So that's what's going to give us this better result.
[6:04] So basically how you do this, you have the footage and you want to convert it to HSV.
[6:11] So if you convert it to HSV, a color space node and you switch the out to HSV.
[6:16] And what this space is is hue, saturation and value.
[6:20] So hue is stored in the red channel, saturation is stored in the green channel and value basically
[6:26] luminance is stored in the blue channel.
[6:30] And the reason we're doing this is because we want to only roll off the highlights, but
[6:35] not really affect the color.
[6:36] So what we're doing essentially is just separating the colors from the luminance.
[6:41] And it's pretty much as simple as that.
[6:43] So what we want to do now is do a kind of a Luma key stack.
[6:48] So we basically just copy and paste this like a whole bunch of times.
[6:51] So if we do this, the way to do this is really simple.
[6:55] Just put a key or node.
[6:59] And again, only paying attention to the blue channel in this color space.
[7:04] Put the key or node, put a grade node, plug it into the mask.
[7:08] Don't even you just leave that default settings most of the time and then you can just set
[7:11] the gain to 0.5.
[7:14] And that and that's what we're going to copy and paste.
[7:17] So basically you want to do that and just copy and paste it a whole bunch of times until
[7:21] we get like a really flat image.
[7:23] So if we just step through in the viewer, I'm just going to step down this kind of chain
[7:27] here and we can see if you watch the highlights that they become more and more flat and closer
[7:32] to the shadow area.
[7:33] So I'm going to step down.
[7:34] There's like a whole bunch of them here.
[7:37] So just go down all the way to the bottom.
[7:41] So now you see we have all this detail here, but it feels really flat and there's not like
[7:44] a big, I mean, it's not perfect, but it gets you pretty close.
[7:49] So at the end here, the last thing you'll do is you want to copy back in the red and
[7:54] the green channel from the original, which is again, we talked about in the hue saturation
[7:59] value.
[8:00] We're just copying the hue and saturation back into this chain because we don't want
[8:03] to affect the colors of the image with all of these corrections, just the luminance.
[8:11] We copy that back in.
[8:12] I've done a little bit of a blur because it just helps kind of hide the edge that we're
[8:16] kind of combining there.
[8:19] And then what we do is convert that back.
[8:21] So the color space note again, but now it says in hue saturation value because that's
[8:26] what we're working in and out is linear.
[8:28] So we're going back into the original color space that we were in.
[8:33] And essentially we have something like this.
[8:34] So we have the original footage and this darkened shadow plate, I guess you could call it.
[8:41] So we could close this and take a look at what that looks like.
[8:46] So one other thing I did was, so I did a slight color correction as well, because I wanted
[8:51] to make it a little bit blue.
[8:52] Because if you look at the original shadows of the plate, they have a little bit of a
[8:56] slight blue tint cooler colors in there.
[9:00] So basically I just want to do that.
[9:03] And one thing you want to also do is I'll show you in a second here.
[9:08] Let me just, so we'll mask it off and go to the original and let that play.
[9:15] And that's what that kind of looks like.
[9:16] I think my cache is loading there.
[9:17] That's why you're seeing some glitches.
[9:18] But if we let that load for a second, we can see that's working pretty well.
[9:23] So one thing I didn't mention in that kind of part there was this.
[9:28] So one thing I do with the shadow clean plate is I try to maintain as much of the original
[9:33] footage as possible.
[9:35] So if I just do the shadow clean plate and I disable these two notes here, you'll see


### Blending original plate [9:40]
**Transcript (timestamped):**
[9:40] that as my shadow crosses where the real shadows are, we're getting a little bit of a shift
[9:46] in contrast and texture, which we don't really want because that's not kind of breaks the
[9:49] illusion.
[9:51] So we want to maintain just those areas.
[9:54] So what I usually do is kind of just take a key mix note and take the original shadows
[10:00] and kind of rotoscope them.
[10:02] So I just want to keep those areas and I key mix that on top of the shadow plate.
[10:06] So this is a shadow plate.
[10:07] And you can see in the shadow plate, we have a little bit of artifacts and some stuff in
[10:12] the darker areas.
[10:13] And we can really easily fix that by just bringing in the original shadows.
[10:17] So that's all we're doing.
[10:18] Just kind of combine those two shadow clean plate with the real shadows.
[10:25] And so if we look at this result, we get this nice effect here.
[10:30] So one other thing that I did, let me just go back here.
[10:36] So these, I've kind of labeled everything in the script.
[10:38] So if you guys download it, it should be all pretty clear.
[10:41] I didn't want to create it from scratch because there's a lot of things here and it would
[10:44] be a very long video.
[10:46] But if I explain it, hopefully you guys will be able to go through and kind of practice
[10:49] yourself and look at the script as well.
[10:53] So some of the other things going on here, I did a little bit of a shadow attenuation


### Other details [10:55]
**Transcript (timestamped):**
[10:58] here, which is using an eye blur.
[11:00] This is a custom note of Nucopedia.
[11:03] It just basically blurs things in a more realistic way.
[11:08] I'm not going to do a whole video on it right now, but basically this is better than a feather.
[11:12] It just feathers it off in a way that kind of fades off similar to a shadow attenuation.
[11:18] So I'll stick that at the top of the script as well.
[11:20] If you guys want to download that.
[11:22] I think the note is by, let me just see.
[11:26] Looks like Moritz-Ish, if I'm saying that correct.
[11:28] So that's who created that.
[11:30] Really useful note.
[11:31] So definitely recommend getting that.
[11:35] So basically, if you look at it, I just done a feather with a roto and then I'm just kind
[11:40] of softening the further away part and keeping the base sharp because again, shadow attenuation.
[11:47] Another thing I did was to get this shadow rolling across the surface and not feeling
[11:52] flat like that.
[11:54] I've done the eye distort method.
[11:56] So basically we're just taking a noise pattern like this, slightly pushing the blacks into
[12:01] the negatives.
[12:02] So the way eye distort works is it wants negative values.
[12:05] It wants positive and negative values to push the pixels left and right.
[12:10] So basically we turn off the black clamp.
[12:12] We shove it down a little bit and we can blur it slightly.
[12:17] And then what I've done is just copy the red into the backward U channel and the green
[12:21] into the backward V channel.
[12:24] And these are two just empty channels.
[12:26] So there's nothing there.
[12:28] We're just kind of putting something in that channel and this channel and then we're just
[12:31] putting the eye distort and set the eye distort to the backward channel and that will use that
[12:37] channel to distort the image.
[12:39] So basically we're just distorting the image by that noise pattern that we've created.
[12:43] So if you look at the edges and now you look at the edges, as this thing goes, it's going
[12:48] to basically distort along that pattern.
[12:53] One other thing I did was a little bit of an eye transform.
[12:56] Again, another custom note I'll put at the top of the script.
[13:00] And I kind of just, I can see this like ridge of dirt here.
[13:03] So all I did was I put a little roto shape here and then just shoved any pixels that
[13:07] crossed that ridge up a little bit.
[13:09] So as it crosses, the shadow will kind of bend just across that little dirt ridge there.
[13:15] And that just gives it a tiny bit more realism.
[13:19] So that's how we got the shadow.
[13:21] And then some other things I did, if I go to the final thing here, I added a little bit
[13:27] of ambient occlusion.
[13:28] So if I look at it without and with, this is just a fake ambient occlusion.
[13:32] I don't have a render here for it.
[13:33] So I just kind of faked it.
[13:35] And that just helps sell kind of the edge where it's contacting.
[13:40] You're always going to have a little bit of darker edge where you're contacting edges.
[13:45] And that's going to help us sit in quite a lot.
[13:48] And basically, yeah, so if you look at the blacks of some of these rocks, like it's a
[13:52] little bit darker, so we can go darker than the shadows of these trees.
[13:56] There's a lot of bounce light in the scene.
[13:58] So the shadow shouldn't be super dark because we see that everything is not super dark.
[14:03] But in the crevices, you can see the very darkest parts do go kind of darker.
[14:08] So we can, we have a little bit of room to go darker with that.
[14:13] So how do I do the ambient occlusion?
[14:18] Relatively straightforward, we just take a cube alpha and I've kind of just blurred
[14:23] it outwards and then masked it by the shadow.
[14:27] So let me say that again.
[14:29] Here's the shadow.
[14:31] Here's the blurred cube and then just masking it.
[14:34] So essentially that's just giving us like a little bit of an edge within the shadow
[14:39] alpha.
[14:40] So we're creating a dark edge where the two objects are meeting.
[14:45] And stepping through, if you see these expression nodes in here, I'm really only using them
[14:51] as the same as a shuffle node, basically.
[14:54] So for example, I wanted to put the red channel into the alpha channel because I was doing
[14:59] those corrections in this kind of RGB area.
[15:05] But I want them to be in the alpha channel because that's what I'm using to drive this
[15:10] color grade because it's looking at the mask RGBA.alpha.
[15:16] So that's how I did this.
[15:18] Again, I used like an inverted Luma key.
[15:21] So that's like the technique I talked about earlier to just protect some of the little
[15:24] rocks and stuff that it crosses over.
[15:26] I don't want to over darken anything with this ambient occlusion.
[15:32] So if we step down further, this is the cube.
[15:36] I'll just talk about how I graded it real quick here.
[15:39] And then that will be it for the tutorial.
[15:42] So we have this original cube here.
[15:46] The background is kind of baked into the original render.
[15:48] So if I put a pre-mult on here, it's basically doing that.
[15:53] So it's just how I rendered out of Arnold, just a real quick render and image plane was
[15:58] sort of baked in there.
[16:00] Not completely intentional, but it's just quick and easy.
[16:02] So there's our cube.
[16:03] We pre-multiply it and that's what we have.
[16:10] So one thing I needed to do was if I pre-multiply that and merge it over the original image,
[16:18] let me just show you.
[16:19] If a pre-multiplyed CG put it over the original image, it's hard to tell here, but there's
[16:26] a little bit of a bright edge in the CG, kind of just a little bright edge on the bottom
[16:30] there.
[16:31] And that's easy fix.
[16:32] We can just do an edge extend.
[16:34] So I've just done an edge extend, which kind of pushes out the edges around.
[16:40] And that will basically just, if I pre-multiply it, it gets rid of that bright edge.
[16:44] So if I compare, you see the bright edge and then now the bright edge is gone.
[16:48] So just a little CG fix.
[16:52] Brighten the top, shadows on top.
[16:54] So I did some rotos to just very slightly adjust the, basically, let me just put it
[17:01] over the background so we can see.
[17:05] We'll just put it like this and put it like this.
[17:10] Okay.
[17:11] So these corrections, I was just kind of brightening the top here because the shadow on the top
[17:17] wasn't really matching kind of the plate.
[17:20] So it was kind of too dark.
[17:23] So I just wanted to balance that out a little bit better, kind of brighten up the shadow
[17:26] a little bit and maybe brighten up the highlights very slightly.
[17:31] And then I wanted to add some fake reflections.
[17:33] So looking at this frame is a good example.
[17:36] It looks kind of flat still.
[17:38] So if I switch the pre-multi here, you see that I've kind of just rotoscoped a little
[17:43] bit of a fake reflection here.
[17:45] And this lines up with the CG shadow.
[17:48] So it looks kind of weird here, but if you look at it over the final comp, it looks correct.
[17:53] So that rotoscope lines up with the CG shadow.
[17:57] So if I just move that out of the way, that's all it's doing.
[18:00] It's just brightening, but I don't want to put a brightening everywhere because now it
[18:03] just looks weird.
[18:04] You just want to put it right on the edge like this.
[18:08] And then it starts to look like an actual reflection of the ground that it's kind of
[18:13] sitting on.
[18:16] And yeah, so these are also little tiny tweaks after that, nothing new information.
[18:22] So I won't go on too much more.
[18:25] Blacks adjustment at the very end and then the pre-multiply.
[18:29] And then of course we can do a keyer of the highlights, pre-multiply it and put it below
[18:35] just to bloom out the highlights of that box.
[18:39] So it feels like it's really bright because this is a really bright scene.
[18:43] So it's kind of overexposed.
[18:44] So we're going to get more glow because of the exposure.
[18:47] So if we just turn that off and on, you see that just kind of helps it sit in that scene.
[18:53] And then just some fake camera movement and basically some extra stuff there.
[18:59] But that's basically it.
[19:00] The script is in the description below.
[19:03] If you guys aren't already subscribed, I'd really appreciate it or hit the like button
[19:07] if you thought it was useful.
[19:10] And yeah, there will be more on the way.



---

## Captured Frames

- [1:25] tutorials/frames/compositing-complex-shadows-in-nuke-advanced/frame_000.jpg
- [3:20] tutorials/frames/compositing-complex-shadows-in-nuke-advanced/frame_001.jpg
- [7:40] tutorials/frames/compositing-complex-shadows-in-nuke-advanced/frame_002.jpg
- [9:45] tutorials/frames/compositing-complex-shadows-in-nuke-advanced/frame_003.jpg
- [11:05] tutorials/frames/compositing-complex-shadows-in-nuke-advanced/frame_004.jpg
- [12:45] tutorials/frames/compositing-complex-shadows-in-nuke-advanced/frame_005.jpg
- [15:50] tutorials/frames/compositing-complex-shadows-in-nuke-advanced/frame_006.jpg
- [17:45] tutorials/frames/compositing-complex-shadows-in-nuke-advanced/frame_007.jpg

---

## Structured Notes

### Core Technique
Building a "shadow clean plate" (an HSV-luma-flattened version of the background plate) and masking it through the CG shadow alpha, instead of simply multiplying a CG alpha over the plate — avoids "double shadows" where a CG shadow crosses an existing real shadow.

### Summary
The tutorial composites a CG cube onto a forest-path plate that already has real tree shadows crossing the ground. A naive alpha-multiply approach produces a visible "double shadow" where the CG shadow overlaps a real one. The video walks through why (shadow attenuation depends on both light size AND distance-to-object, so a real shadow's edge softness varies along its length) then builds a shadow clean plate: convert the plate to HSV via `Colorspace`, chain ~8-10 copies of `Keyer` (blue/luminance channel) → `Grade` (mask input, gain 0.5) to progressively flatten highlights toward shadow-black without touching hue/saturation, then copy the original red/green (hue/saturation) channels back in and convert back to the original colorspace with a second `Colorspace` node. The flattened clean plate is masked by the CG shadow's alpha and merged over the plate — this reads as a shadow because the plate's own contrast/texture is preserved (unlike a flat multiply). A `KeyMix` blends the clean-plate shadow area with the real, un-flattened plate texture so the composite doesn't lose detail where they overlap. Final polish: an EyeBlur gizmo (Nukepedia, by "Mairs"/similar) for shadow attenuation (soft-at-distance falloff via roto-driven feather rather than a uniform blur), an EyeDistort gizmo fed a blurred/clamped noise pattern (pushed into negative values, copied into backward-U/backward-V channels) to make the shadow ripple realistically across the uneven dirt road surface, an EyeTransform gizmo to bend the shadow across a small ridge in the ground, fake rotoscoped reflections and a blown-highlight grade on the cube to sell contact, a cheap ambient-occlusion fake (blurred cube alpha masked by the shadow alpha, protected by an inverted Luma key so small rocks aren't over-darkened), Edge Extend before premult to kill a bright fringe on the CG render, and a Keyer-driven bloom pass on the cube's highlights.

### Key Steps
1. Identify the double-shadow problem: naive `Multiply`/stencil of a CG alpha over a plate breaks where the CG shadow crosses a real shadow already in the footage.
2. Convert the plate to HSV with `Colorspace` (in: linear/original, out: HSV) — hue in red channel, saturation in green, luminance/value in blue.
3. Build a luma-key stack: chain repeated `Keyer` (reading only the blue/value channel) → `Grade` nodes (each Grade's mask input fed by the paired Keyer, gain set to 0.5) — copy/pasted many times in series to progressively roll off and flatten the highlights toward the shadow value.
4. Copy the original red (hue) and green (saturation) channels back into the flattened chain (only luminance was being corrected) with a `Copy`/expression node, plus a slight blur to hide the seam.
5. Convert back to the original colorspace: second `Colorspace` node, in: HSV, out: linear — this produces the "shadow clean plate."
6. Mask the shadow clean plate through the CG shadow's alpha and merge it over the original plate.
7. Use a `KeyMix` with a rotoshape to bring back the real (un-flattened) plate texture in areas where real shadows already existed, avoiding a texture/contrast shift.
8. Add shadow attenuation via the EyeBlur gizmo (Nukepedia) driven by a roto shape — softer falloff farther from the object, sharp at the base, instead of a uniform Blur/Feather.
9. Fake ground-ripple in the shadow: create a noise pattern, push blacks negative (disable black clamp), blur slightly, copy red channel → backward-U and green channel → backward-V (empty channels), feed into an `EyeDistort` gizmo set to use those backward channels — distorts the shadow edge to appear to roll over the dirt road's surface irregularities.
10. Use an `EyeTransform` gizmo + roto shape to bend the shadow where it crosses a small ridge in the ground for extra realism.
11. Grade/roto in fake reflections on the cube (rotoscoped, aligned to the CG shadow) and a slight highlight/shadow-top rebalance so the CG cube doesn't look flat/uncontacted.
12. Add fake ambient occlusion: blur the CG alpha outward, mask by the shadow alpha, protect small rocks with an inverted Luma key so AO doesn't over-darken detail already in shadow.
13. Premult the CG render, use `Edge Extend` before the premult to remove a bright fringe artifact at the CG edge, then key/premult the highlights and put a bloom pass below for exposure-driven glow.
14. Finish with expression nodes used purely as channel shufflers (e.g. copying a correction from RGB into the alpha channel to drive a mask-by-alpha grade) and fake camera movement.

### Nodes / Tools / Settings
- `Colorspace` — in→HSV (first pass, separates hue/sat/luminance into R/G/B) and HSV→in (second pass, reverts to original colorspace after correction)
- `Keyer` — reads blue (value/luminance) channel only, chained repeatedly to build a progressive flattening stack
- `Grade` — mask input fed by paired Keyer, gain = 0.5, default settings otherwise, chained ~8-10x
- `Copy` / expression — restores original hue (red) and saturation (green) channels post-flattening; also used purely as a Shuffle substitute to move a correction's red channel into the alpha channel
- `Blur` — slight blur to hide the seam where hue/sat is copied back over the flattened luminance chain
- `KeyMix` — blends the real (un-flattened) plate texture back into shadow-clean-plate areas using a rotoshape mask
- `EyeBlur` (Nukepedia gizmo, credited to "Mairs"/similar spelling in video) — roto-driven distance-based feather/attenuation, more realistic than a uniform Blur
- Noise generator → blur → black-clamp disabled, values pushed negative; red channel → backward-U, green channel → backward-V
- `EyeDistort` (Nukepedia gizmo) — set to use backward-U/backward-V channels to ripple the shadow edge across uneven ground
- `EyeTransform` (Nukepedia gizmo) — roto-shape-driven local pixel push to bend the shadow across a ground ridge
- `Roto`/`RotoPaint` — fake reflections on the cube, ambient-occlusion protection mask, shadow-clean-plate blend mask, ridge-bend mask
- Inverted `Luma key` — protects small rocks/detail from over-darkening by the fake AO pass
- `Edge Extend` — removes a bright fringe artifact around the premultiplied CG cube edge
- `Premult` — standard premultiply of the Arnold-rendered CG cube (background baked into the render/image plane)
- `Keyer` (on cube highlights) + `Premult` + merge-under — bloom pass for the overexposed/bright scene
- Fake camera movement (unspecified transform/shake node) added at the end for extra realism

### Difficulty
Advanced

### Foundry App & Version
Nuke (core toolset only — no NukeX-exclusive features required; the EyeBlur/EyeDistort/EyeTransform tools are third-party Nukepedia gizmos, not native nodes). No on-screen version number visible in the captured frames and none stated in the transcript. Video published 2021 — falls in the Nuke 13.0 era (13.0 released 2021-03-17, 13.1 released 2021-11-23); see `references/version-tracker.md`.

### Tags
compositing, relighting, grading, roto, channels, gizmo, color-management, advanced

---

## Related Tutorials
- [Nuke Compositing Artistic Basics (4/8): Shadows](nuke-compositing-artistic-basics-48-shadows.md) — the theory (shadow attenuation, light size vs. distance) this tutorial applies practically
- [Nuke Tutorial | Compositing a Rainbow \[Intermediate\]](nuke-tutorial-compositing-a-rainbow-intermediate.md) — shares the HSV round-trip (Colorspace in/out, isolate hue/sat from luminance) technique used here for the shadow clean plate
- [Grading Highlights and Pools of Light | Nuke Compositing](grading-highlights-and-pools-of-light-nuke-compositing.md) — related highlight-rolloff grading approach
- [I Made VFX Relighting WAY Better in Nuke](i-made-vfx-relighting-way-better-in-nuke.md) — shares the relighting/gizmo-driven realism theme
- [2 Expert VFX Tips to PERFECTLY Blend CG](2-expert-vfx-tips-to-perfectly-blend-cg.md) — shares the painted-light/fake-reflection contact-selling technique used on the cube here
