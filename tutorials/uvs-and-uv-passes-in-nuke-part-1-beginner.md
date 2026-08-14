---
title: UVs and UV Passes in Nuke: PART 1 [Beginner]
source: YouTube
url: https://www.youtube.com/watch?v=wb1WjHlXbn0
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke (concepts explained via Maya) + Nuke"
version: "not specified (2021 upload, Nuke 13.0 era — see version-tracker.md)"
tags: [compositing, st-map, channels, 3d-system, digital-matte-painting, beginner]
extraction_status: complete
frames_dir: tutorials/frames/uvs-and-uv-passes-in-nuke-part-1-beginner/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# UVs and UV Passes in Nuke: PART 1 [Beginner]

**Source:** [YouTube](https://www.youtube.com/watch?v=wb1WjHlXbn0)
**Author:** Compositing Academy
**Duration:** 15m52s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] detection,
[0:03] review,
[0:05] yzvalue,
[0:06] dysvalue V's in general,
[0:10] ubm pista,
[0:13] UV passes a little bit about UVs in general, and then some of the practical ways that we
[0:19] can actually use them.
[0:20] So again, this is a beginner video.
[0:23] I'm intending to make an intermediate video and then an advanced video about UVs because
[0:27] it's a pretty in-depth topic and there's all kinds of stuff you can do with STMAP and UVs
[0:33] in general on 3D objects as a compositor.
[0:37] So there's some creative ways we can use those in the future.
[0:39] But this is more of a beginner video.
[0:41] I've split it into basically two parts.
[0:45] One goes in my explaining UVs and then the second part will go into Nuke and check out
[0:48] some of this stuff.
[0:50] So if you guys want the project file, it's in the description below for free and you
[0:54] can download.
[0:55] There's a couple assets that come with it so you can actually play around and follow
[0:59] along if you want in terms of using some of these images here.
[1:03] And I've also provided one of the, I've provided this car render for free, just one frame of
[1:09] it from my full Nuke 303 class.
[1:11] And it comes with the UV pass as well so you can actually use this and learn the technique.
[1:18] So without further ado, we'll get into the tutorial.
[1:22] So for the first portion that we're looking at here, it's really just the fundamentals


### Fundamentals of Cg [1:25]
**Transcript (timestamped):**
[1:26] of CG, very much so the basics, but I just want to cover this part in case some people
[1:33] don't have a 3D background.
[1:34] Some compositors actually have no 3D background.
[1:37] But I really highly recommend that you know some 3D as a compositor as it's going to give
[1:42] you really big advantage and you're going to understand where things are coming from
[1:45] when you're working in Nuke.
[1:48] So I really recommend you get into Maya or Blender or one of the other 3D softwares that
[1:53] are widely used and understand these concepts.
[1:56] So we're just going to briefly cover this in Maya as this is an easy way to explain
[2:00] what UVs are.
[2:02] And then we're going to go into more about what we can do with them in Nuke and why they're
[2:06] relevant to us as compositors.
[2:09] So the basics of UVs is very simple.


### Basics of Uvs [2:10]
**Transcript (timestamped):**
[2:13] So you have this texture that's wrapped onto this cube here.
[2:18] And essentially what you're doing is you're wrapping a 2D image onto a 3D model.
[2:23] So essentially what you have to do is take a 3D model and you need to unwrap it.
[2:28] So this is the unwrapped model.
[2:30] So you can see if you imagine like a piece of paper, you know, if you were to cut this
[2:33] cube up and flatten it.
[2:36] This over here on the right is essentially what that is.
[2:39] It's just a flat version of the model.
[2:43] And if I turn on the texture view, we can see that we're mapping this kind of colorful
[2:47] checkerboard texture onto this model.
[2:51] And if we hit this button here and I select one of the faces, you'll see that this face
[2:56] here when I'm selecting the top of the cube is actually highlighting this specific square.
[3:00] So we know that that texture here, so you can see the numbers 8, 1, 1, 2 are being mapped
[3:07] onto the top of that cube.
[3:08] So we're essentially just taking a 2D picture, putting it on there.
[3:12] Of course you can manipulate UVs if you're in a 3D software.
[3:16] So you can grab this UV and I can move it around.
[3:18] And it's not going to change the geometry.
[3:20] It's only mapping, it's only changing the way this 2D texture is being mapped onto that
[3:24] geometry.
[3:26] So we can slide that around and now you see that the top here is 2334.
[3:33] And also what you notice is that the side here is a bit stretched and diagonal.
[3:37] And that's because you can see if we turn off the view, you can see that these lines
[3:41] are diagonal.
[3:42] So we're trying to map a straight image onto a warped UV.
[3:48] So that's kind of a problematic area.
[3:50] So that's not how you want to map your UVs.
[3:52] You want to make it so the lines flow the correct direction.
[3:56] So that's essentially what UVs are.
[3:59] And so when you're getting a UV pass in Nuke, you're essentially getting this layout, this
[4:07] kind of layout, and you can remap a new texture in Nuke onto this layout.
[4:12] So if I have these cubes like this, I can put a different texture and it's going to
[4:18] wrap onto the different sides of the cube without going back into 3D.
[4:22] And so the reason for this is because you can save time and production.
[4:25] And if you want to change or add some texture to CG that has already been rendered, you
[4:30] can just do it quickly in post-production and you don't need to re-render or go relight
[4:36] anything.
[4:37] You can actually just do it in Nuke.
[4:39] So that's the reason we want to talk about UVs.
[4:41] And now we'll start to get into other things we can do with UVs and just a couple examples
[4:47] and going over it.
[4:50] So as we covered in the previous section, this is kind of the same concept and we're
[4:55] just looking at this inside of Nuke now.
[4:57] So I've kind of just laid it out on top here as the 2D view and then we have the 3D object
[5:03] underneath.
[5:04] So on the left side here, we have the unwrapped cube.


### Unwrapped Cube [5:05]
**Transcript (timestamped):**
[5:06] So this is brought in from Maya, this cube.
[5:10] And the cube is unwrapped like so.
[5:12] So we can see the 2D layout and we can see the numbers on here.
[5:15] So for example, that is again that top face, we have the numbers 8, 1, 1, 2 and we can
[5:21] see those on the top here.
[5:22] And just to remind you guys, this picture with all the numbers, that's just for referencing
[5:26] where things are on the cube.
[5:27] It doesn't mean all these numbers, they don't mean something special, it's just a reference
[5:31] texture.
[5:33] So we can see that that's wrapped around the object here.
[5:37] And on the right here, we have one that's called a normalized UV layout, which means
[5:43] every single face is mapped basically over the same image.
[5:47] So all of them are mapped exactly the same way.
[5:50] So if we change the image here, it's going to change all the sides exactly the same.
[5:55] So it's not wrapping around really, all the faces are exactly the same.
[6:00] So that's a little bit less useful, but this is actually important to know because by default
[6:05] Nuke is actually doing this with a default cube.
[6:09] It's creating this normal, it's called a normalized UV layout.
[6:14] So again, so this is kind of when I keep saying U and V, this is what this is referring to.
[6:21] It's just an X and Y representation, so an X and Y coordinates of a 2D image.
[6:29] And the reason we don't use X and Y, we use the letters U and V is just because in 3D
[6:34] we're already using the term X, Y and Z pretty frequently.
[6:37] So it's just confusing to have the same letters.
[6:41] So U is horizontal and V is that vertical line here.
[6:46] So that's UVs, but now we only want to talk about UV renders.
[6:53] So we can actually render out a special image.
[6:55] So if we go down here, this is a cube that's been rendered.
[6:58] So we just have a cube with a basic texture on it.
[7:02] And we also have a cube, the same cube, with this special image.
[7:07] And these images are, I'm going to get into it more in the intermediate video on how we
[7:12] can actually create these special ramps.


### Gradient Ramps [7:14]
**Transcript (timestamped):**
[7:15] So these gradient ramps are basically telling Nuke the 3D coordinate system even though you
[7:21] don't have a 3D model anymore.
[7:23] So this is a 2D image rendered from a 3D object.
[7:26] So we only have 2D images, but this one is special.
[7:31] So we can basically use this to wrap textures around the 3D model without having to actually
[7:37] load the 3D model into Nuke.
[7:39] So I don't need to actually go and load and bring the entire model in from Maya.
[7:45] So if this was a character or something more complicated, we don't need to bring in the
[7:48] character model.
[7:49] We just need to have a 2D render of the UV pass here.
[7:54] And so with this UV pass, if we plug it into an ST map node, we can switch the ST map to
[8:01] switch it to RGB.
[8:04] And essentially what that does, and the reason we switch it to RGB is because this is saved
[8:09] in the red, green, and blue channel.
[8:12] So we can see we're in the normal layer here, which is the red, green, and blue.
[8:17] And if we switch from red and green, we can see there's some kind of information in these
[8:21] gradients.
[8:22] And so by setting that to RGB and plugging in a source, which is another picture, it
[8:28] will wrap around that object.
[8:30] So you see we have a picture, a 2D picture of some vines here.
[8:36] And when I plug it through the ST map, it's wrapping around that 3D cube without having
[8:43] a 3D model involved.
[8:44] It's just using 2D.
[8:46] So this is basically just a 2D trick, and we can retext your 3D objects very quickly
[8:51] without having to render them.
[8:53] So I can move this texture around.
[8:56] If I go to here, I switch the transform, you see I can move these vines instantly, and
[9:03] I'm not doing any kind of re-rendering or anything like that.
[9:07] It's just a cheat, basically.
[9:09] And then we have down here just some lighting so we can multiply some lighting on there.
[9:14] And that's just a simple example of UVs.
[9:16] So you're like, well, why wouldn't we just take the vines and render these in CG?
[9:23] Probably you would with vines because you're going to get better looking vines than maybe
[9:27] a 2D image.
[9:28] But there are certain aspects that you might want to do in compositing, such as if you're
[9:35] going to simulate water running down this cube, that's going to be an expensive thing
[9:39] to do, and it's going to take you a lot of time.
[9:42] Whereas if this is far enough away from the camera, we can take a video of raindrops
[9:47] on glass, and then we could just put that on the cube, and now it's going to look like
[9:50] the raindrops are running down the cube.
[9:53] And we didn't have to go into Houdini or do any kind of advanced simulation.
[9:57] We're basically just saving time and saving money.
[10:00] So again, that depends on your shot.
[10:03] It depends on how far away this thing is from the camera.
[10:08] So if it's a hero shot and you're looking really up close, you're probably going to
[10:10] need some 3D drips.
[10:12] But if it's something that's a little bit further away, we can use 2D tricks like this
[10:16] and save production time.
[10:19] And essentially, that's how you have to always think of things with CG is if you can save
[10:24] time, save money, and it's pretty important to think that way.
[10:30] So this is another example.
[10:33] I've given you guys a free, basically, frame from my full class, which is the CG Compositing
[10:38] class.
[10:39] Some of you guys have probably already taken this class.
[10:42] So this video is a little bit more in depth on the UVs.
[10:45] But we have, this is almost an eight hour class on CG compositing specifically.
[10:51] So yeah, so this is kind of just more on this.
[10:55] So we have a car render, so a beauty.
[10:58] And this doesn't have any layers, it's just a JPEG.
[11:01] And we have a UV render of this car as well.
[11:06] So we also have something called the UV layout, which again, I told you guys about with the


### Uv Layout [11:07]
**Transcript (timestamped):**
[11:10] cube.
[11:11] So instead of it being a cube, we can see it's just this car cut up into pieces and
[11:18] put flat.
[11:19] So we can see all the pieces here.
[11:21] And if we want to put, for example, let's say we want to put a color wheel on the back
[11:27] of this car here.
[11:29] So if you look at the car, let's say I want to put this picture onto the back of this
[11:35] car.
[11:36] Well, I'm going to go here to the UV layout to figure out where to place it.
[11:39] So I go to the UV layout.
[11:40] I look for the piece and I actually unwrapped this car because I modeled it.
[11:45] So this is actually the piece.
[11:48] So I can place that cube.
[11:49] So what I've done is I've taken the cube, I've reformatted it into a square.
[11:53] It's just a bit easier because these UV layouts are usually square.
[11:59] So I've reformatted it to being a square as well.
[12:02] And then I've just transformed it.
[12:05] And we can basically just move it around.
[12:08] And I could, oops, I'll grab it here, put it on the back of the bumper.
[12:12] And now if I run it through the ST map, so I plug in the UV render and I plug in the
[12:17] picture that we've just placed.
[12:19] And I've used this, you see I'm doing two different things here.
[12:21] I'm using this as reference, like this kind of merge over here.
[12:25] And on the left here, I'm actually doing the ST map.
[12:29] So this is just for reference.
[12:31] That's all this is for.
[12:33] So we transform that and we can ST map it.
[12:36] And you'll see we get this result where it's folding on the back here.
[12:40] And if I merge that picture, this result from the ST map over the top of our render, we
[12:47] can see that's been placed on the car.
[12:51] And we can, of course, move this around so I can take the transform, hit use up and down
[12:56] arrow keys and slide this around.
[12:58] And it's going to wrap around the CG model.
[13:00] And again, we're just dealing with two 2D images.
[13:03] We have the beauty render of the car and we have the UV render.
[13:09] So that's pretty cool.
[13:11] So one thing you might be confused about is you look at this thing and you're like, well,
[13:15] I didn't unwrap this model.
[13:16] And if you have a really complex model, you might have a lot more pieces than this.
[13:19] So you're like, well, where do I, you know, how do I, you know, if I want to put a color
[13:24] reel on the top of this tire here, you might be confused when you look at this picture.
[13:30] And then you're going to be moving this color reel everywhere.
[13:32] Like, well, I don't know which piece is the right spot to put it.
[13:36] And that's where this tester material comes in.


### Tester Material [13:37]
**Transcript (timestamped):**
[13:39] So that's where that material we've been using.
[13:41] If we plug that in to the ST map and then we just let that go around the car.
[13:49] That's why this material is useful is because we can see all these colors and they correspond
[13:53] to this picture in this square image.
[13:56] So for example, we see this three here and a four, three and four next to each other.
[14:02] The three is white and their four is pink.
[14:05] So if we look at this thing, where is a three white and a four pink?
[14:08] What's right here?
[14:10] So three and four right here.
[14:12] And if we go to the corresponding place on our template, we see that that area is right
[14:18] here.
[14:19] So that's what that's just telling us.
[14:20] It's just telling us where on this thing it's going to land.
[14:24] So three and four.
[14:25] So if I put my color wheel over in that spot in the three and four and then I plug that
[14:31] into the ST map, you can see that is being wrapped onto the right place.
[14:37] So that's what the tester material is for.
[14:39] It just helps if you don't know where to place things.
[14:43] And that's one way to do it.
[14:45] There's many ways.
[14:47] But yeah, so hopefully that helps out some people.
[14:50] And we can slide it around here.
[14:53] That's how it works.
[14:55] So this is again, it's 15 bucks if you guys want a full CG composing class, which has
[15:02] a lot more detail than this about different things.
[15:05] This is one aspect of CG composing.
[15:06] I'm going to make another video, more intermediate UV uses.
[15:11] So we're going to get into more advanced stuff, how we can actually generate these use expressions
[15:17] to generate these patterns.
[15:19] And eventually after that, I have some plans to do an advanced UV video on YouTube, which
[15:24] is going to be things that even senior composters will probably benefit from if you're a senior
[15:30] compositor following this channel.
[15:33] So I kind of have a range of people here.
[15:34] So I'm going to try to post beginner and intermediate content most of the time and occasionally post
[15:41] senior level tutorials out here so that people can get use out of it.
[15:45] So if you guys liked the video, hit the like button and it helps out a lot.
[15:49] And thanks for checking it out.



---

## Captured Frames

- [2:15] tutorials/frames/uvs-and-uv-passes-in-nuke-part-1-beginner/frame_000.jpg
- [4:00] tutorials/frames/uvs-and-uv-passes-in-nuke-part-1-beginner/frame_001.jpg
- [5:10] tutorials/frames/uvs-and-uv-passes-in-nuke-part-1-beginner/frame_002.jpg
- [7:20] tutorials/frames/uvs-and-uv-passes-in-nuke-part-1-beginner/frame_003.jpg
- [8:10] tutorials/frames/uvs-and-uv-passes-in-nuke-part-1-beginner/frame_004.jpg
- [11:05] tutorials/frames/uvs-and-uv-passes-in-nuke-part-1-beginner/frame_005.jpg
- [12:20] tutorials/frames/uvs-and-uv-passes-in-nuke-part-1-beginner/frame_006.jpg
- [13:45] tutorials/frames/uvs-and-uv-passes-in-nuke-part-1-beginner/frame_007.jpg

---

## Structured Notes

### Core Technique
Fundamentals of UV coordinates and UV render passes: what UVs are (a 2D unwrap of a 3D model's surface, X/Y renamed U/V to avoid clashing with 3D's X/Y/Z), what a rendered "UV pass" encodes (world UV coordinates baked into an image's R/G channels as a gradient, standing in for the full 3D model), and how the `STMap` node uses that UV pass to re-project or replace a 2D texture onto CG geometry in comp — without ever loading the 3D model into Nuke.

### Summary
Part 1 of a beginner→intermediate→advanced UV series. Opens with pure 3D fundamentals demonstrated in Maya (not Nuke) for viewers without a 3D background: a numbered/checkerboard texture is wrapped onto a cube, and selecting a face shows exactly which square of the flat "unwrapped" 2D layout maps to it; dragging a UV point in the unwrap view distorts only the texture mapping, not the geometry, and stretched/diagonal UV shells are called out as a mapping problem to avoid. Explains the distinction between a genuinely unwrapped UV layout (each face maps to a different part of the texture) versus a "normalized" UV layout (every face maps to the exact same square — Nuke's built-in default cube uses this simpler kind). Moves into Nuke to explain what a UV render pass actually is: a 2D image where the R and G channels encode a smooth gradient corresponding to the model's U and V coordinates — it looks like colored gradient ramps but is actually 3D positional data flattened into 2D, letting Nuke "know" the 3D coordinate system without ever loading the actual model. Demonstrates plugging that UV pass into an `STMap` node set to RGB channels (because UV data lives in red+green), with a new 2D source texture (a vine photo) plugged into the STMap's second input — the vines wrap around the cube's rendered shape purely as a 2D operation, and can be repositioned instantly with a `Transform` with no re-render needed. Extends to a real production example: a rendered car beauty pass, its corresponding UV render, and the car's "UV layout" (all body panels cut apart and laid flat, reformatted into a square) are used together to place a decal (a color wheel graphic) precisely on the rear bumper — position the decal within the flat UV layout reference, transform it, then run the UV render + positioned decal through an `STMap` and merge the result over the beauty render. For cases where the correct UV-layout location isn't obvious (complex models with many pieces), introduces a "tester material" — a colorful numbered checker texture pre-applied through the STMap so every numbered square is visible directly on the 3D-looking rendered surface, letting the artist visually match a UV-layout region (e.g. "3" and "4") to its real-world location on the model before placing artwork there. Explicitly frames all of this as a time/cost-saving compositing trick (re-texturing, adding water/rain-drip elements, etc. without going back into 3D or simulation software) that's most appropriate when the CG element isn't a hero close-up.

### Key Steps
1. (Conceptual, in Maya) Understand that a UV unwrap is a 2D "flattened" layout of a 3D model's surface — selecting a face on the model highlights the corresponding square in the flat layout.
2. Distinguish a genuinely unwrapped layout (each face → distinct texture region) from a "normalized" layout (every face → the same square, e.g. Nuke's default built-in Cube geometry).
3. Understand axis naming: U = horizontal, V = vertical, in a 2D texture-space coordinate system — named U/V specifically to avoid clashing with 3D's X/Y/Z.
4. In Nuke, read in a rendered "UV pass" — a 2D image whose R and G channels contain a smooth gradient encoding each pixel's U/V coordinate on the original 3D model (this stands in for the model itself; no 3D geometry needs to be loaded).
5. Plug the UV pass into an `STMap` node's first input; set the STMap's channels to RGB (since UV data is carried in the red/green channels).
6. Plug a new 2D texture (photo/graphic) into the STMap's second input — the STMap remaps/warps that 2D texture to follow the original model's surface, wrapping it convincingly around the CG shape using only 2D operations.
7. Reposition the applied texture instantly with a `Transform` upstream of the STMap input — no 3D re-render required.
8. For production use on a complex asset (e.g. a car): obtain the beauty render, its UV render, and its flat UV layout reference image.
9. In the UV layout reference, locate the flat "piece" corresponding to the target placement area (e.g. rear bumper), reformat/crop it to a square if needed, and transform a new graphic/decal into that piece's position (using a `Merge` purely as visual reference against the layout, separate from the actual STMap chain).
10. Run the UV render + positioned decal through the `STMap`, then `Merge` the STMap's output over the beauty render — the decal now appears correctly wrapped and positioned on the CG surface.
11. When the correct UV-layout region isn't obvious (many small pieces on a complex model), first run a colorful numbered "tester material" texture through the same STMap chain to visually cross-reference numbered squares in the flat layout against their real location on the rendered model, before placing final artwork.

### Nodes / Tools / Settings
- `STMap` — core node; Channels set to RGB (UV data lives in R/G); Input 1 = UV render pass, Input 2 = new 2D texture/decal to be wrapped/mapped
- `Transform` — repositions/animates the mapped 2D texture without any 3D re-render (upstream of the STMap's texture input)
- `Merge` — composites the STMap's remapped output over the beauty/CG render; also used separately, purely as a visual reference aid, to preview decal placement against the flat UV-layout image before running it through the STMap
- UV render pass — a rendered 2D image (not a geometry) whose R/G channel gradients encode the model's UV coordinates; substitutes for loading actual 3D geometry into Nuke
- "Tester material" / numbered checker texture — a reference texture run through the STMap to visually map UV-layout regions to their corresponding location on the rendered model

### Difficulty
Beginner

### Foundry App & Version
Nuke (native `STMap`, `Transform`, `Merge` — no third-party gizmos); the UV/unwrap fundamentals segment is demonstrated in Maya, not Nuke, purely for conceptual explanation. No on-screen version number visible in the captured frames and none stated in the transcript. Video published 2021 — falls in the Nuke 13.0 era (13.0 released 2021-03-17); see `references/version-tracker.md`.

### Tags
compositing, st-map, channels, 3d-system, digital-matte-painting, beginner

---

## Related Tutorials
- [UV / ST Maps [Part 2] | Nuke Compositing [Beginner / Intermediate]](uv-st-maps-part-2-nuke-compositing-beginner-intermediate.md) — direct sequel (Part 2/2), continues into intermediate UV-expression techniques for generating UV patterns.
- [Compositing in UV space with Projections | Nuke [Advanced]](compositing-in-uv-space-with-projections-nuke-advanced.md) — the advanced-tier follow-up this series builds toward, applying UV-space compositing to full projection/relighting workflows.
- [Parallax HAX | Nuke Compositing [Advanced]](parallax-hax-nuke-compositing-advanced.md) — uses an ST map/UV-coordinate remap as a prerequisite step, referencing this series' UV fundamentals directly.
- [Nuke Compositing Technique | Card3D + PixelsToPos [Beginners]](nuke-compositing-technique-card3d-pixelstopos-beginners.md) — shares the beginner-level "avoid going back into 3D" time-saving compositing philosophy, applied via a different mechanism (tracked-camera anchoring instead of UV remapping).
- [Gradient Re-Mapping and Quadratic Luma Keys | Nuke Compositing [Advanced]](gradient-re-mapping-and-quadratic-luma-keys-nuke-compositing-advanced.md) — the advanced-tier repurposing of the exact `STMap` node covered here, redirected from UV-pass texture wrapping into color-gradient remapping.
