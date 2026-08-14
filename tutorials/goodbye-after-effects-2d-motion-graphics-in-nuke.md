---
title: Goodbye After Effects!  2D Motion Graphics in Nuke!
source: YouTube
url: https://www.youtube.com/watch?v=QRAsWDehxhA
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "not specified"
tags: [motion-graphics, gizmo, compositing, 3d-system, digital-matte-painting, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/goodbye-after-effects-2d-motion-graphics-in-nuke/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Goodbye After Effects!  2D Motion Graphics in Nuke!

**Source:** [YouTube](https://www.youtube.com/watch?v=QRAsWDehxhA)
**Author:** Compositing Academy
**Duration:** 14m30s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Screen Graphics
[0:09] We've all been there, hand-animating, small graphics, watching the timeline tick away with
[0:14] creatively limiting tools.
[0:16] But does it really have to be this way?
[0:18] In the next few minutes, I'm going to show you a brand new set of tools that's going
[0:20] to change your Nuke workflow forever.
[0:23] ScreenFX is a plugin that gives you a set of tools to do glitches, 2D motion graphics,
[0:28] color distortions, transitions and more.
[0:30] But before we dive into the plugin, I want to show you guys how we captured the footage
[0:33] you just saw with the help of the sponsor of this video.
[0:36] Whether you're on set or adding it virtually, Smoke and Haze is one of the best ways to


### Smoke Ninja Pro Reveal [0:38]
**Transcript (timestamped):**
[0:41] add color and adjust contrast to make better silhouettes.
[0:44] And this is the secret to these shots, a portable smoke machine.
[0:50] This is PMI Gear's Smoke Genie and their newest product, the Smoke Ninja Pro.
[0:55] The Smoke Ninja Pro is a handheld, non-toxic, portable smoke machine that can produce steam,
[1:00] dry ice effects as well as haze if you want to create Godraiser lift the background using
[1:06] various attachments.
[1:07] Whether you're using an on set or you want to shoot your own visual effect stock footage,
[1:11] this is the perfect solution.
[1:12] And if you're on set and you need to fill a large volume of space, you can check out
[1:16] the Smoke Genie Event Kit.
[1:18] Contained in a compact box, you'll get 3 smoke machines you can attach together or use
[1:22] remotely to fill larger spaces.
[1:25] This is great if you need a really smoky scene or filling a large volume.
[1:29] Here you can see the before and after effect.
[1:32] So if you're an independent filmmaker or visual effects artist or you're on set, you
[1:36] can check out the links in the description below to learn about their offerings.
[1:40] Alright guys, so we're checking out screen effects, what is this, how does it work and


### ScreenFX Introduction [1:42]
**Transcript (timestamped):**
[1:44] how is it useful.
[1:45] So essentially what I want to demonstrate in this, without going through every single
[1:49] knob and every single note, because that would be a pretty long video, I'm going to do a
[1:53] quick overview of the nodes, but also show how they work together and also some creative
[1:57] uses that you can use them in actual shots.
[2:00] So I'll open up one or two shots and show you how I use them.
[2:03] And you know, you can use them differently because the main principle here is that this
[2:06] package, these are not assets.
[2:09] So an asset by its nature is not customizable and it's not, you know, ready for modification
[2:15] for look development, whereas tools are customizable with a lot of controls for variation, and
[2:21] they can be modified for creative notes.
[2:22] So these are all tools with me anticipating what kind of notes might I receive if I was
[2:28] using these tools, if I was working for a client or working with a team, where we want
[2:32] to control and create maybe a retro effect or a sci fi effect or a hologram effect where
[2:38] those all look quite different from each other.
[2:40] So here's just one of the nodes of many.
[2:42] So this is from the motion graphics shape generators, all these orange ones here are
[2:47] different types of shapes and motions and animations.
[2:49] So I just grabbed one single node from the section.


### PolyFlow [2:52]
**Transcript (timestamped):**
[2:52] And let's just take a look at it to get an idea.
[2:53] So this one is called poly flow.
[2:55] I really like this one.
[2:56] It's kind of unique motion and style you can get into this.
[2:59] So essentially what we have here is something called rain offset.
[3:02] So we can basically split this up.
[3:05] And when we hit play, we'll actually see that they are kind of flipping down.
[3:08] So we get this natural motion that would be pretty difficult to achieve if we were to
[3:12] do it manually because we can't just break something up with noise.
[3:14] If we look close at how they're animating in, they're actually fading on and off.
[3:18] And we have things like a fade control or the rain offset like I showed, we have center
[3:23] size so we can actually spread this effect or edge size if we want to have more of a
[3:26] gradient taper.
[3:27] So we have a lot of control here right off the bat.
[3:30] We have things like different color modes.
[3:32] So one of the things that I wanted to do when I was building this for myself was just treat
[3:37] these almost like CG assets.
[3:38] Like what if we get a note and we want to break up the colors of these?
[3:41] We want different variation.
[3:43] Well, I added a bunch of different color modes in different patterns stored within the note
[3:47] itself.
[3:48] So in the same way as if you had a CG asset and you had an ID pass where you would use
[3:53] the red, green and blue channels to target different areas.
[3:56] This is the same principle except we're doing it with various little shapes and various
[4:00] patterns that are stored within the note itself.
[4:03] So pretty cool, pretty simple.
[4:05] We also have things like sides.
[4:07] So if you want to have different types of shapes, we can do that.
[4:09] So a lot of sci-fi motion graphics type of things, you know, we want a variation like
[4:14] this.
[4:15] We want to have a bunch of shapes and styles depending on what you're doing.
[4:17] So you can get very, very different looking effects here.
[4:20] And you know, if we were to increase something like the size or decrease rather, we could
[4:25] decrease the number and we'd see that essentially we have a tiny effect or we could have a really
[4:30] huge effect like this, which is going to look totally different.
[4:34] We could turn on the fill and then we have something that looks very, very different.
[4:38] So I actually use this effect, you know, in combination with itself.
[4:41] So you could take these bigger shapes, mask them against smaller shapes from the same
[4:45] node and you can get all kinds of really cool variation.
[4:48] So that's just one single node out of this pack here.


### Offset Tools [4:52]
**Transcript (timestamped):**
[4:52] So let's talk about some more effects and how they combine with each other.
[4:55] So in the offsets and positions, there's a bunch of things that will basically scatter
[5:00] your image or duplicate your image.
[5:02] There's all kinds of different creative, basically move your image around and distort it type of
[5:07] things.
[5:08] Similar to other transition and color effects we'll talk about later, but I want to talk
[5:12] about these two and then show you how I use those in combination with the one we just
[5:17] talked about, which is poly flow in the final shot.
[5:20] So first, let's just see what these two are.
[5:23] So if I have this kind of stock image here, that already looks kind of like something
[5:26] like a final effect, and I put the blocky lines on it and hit play, we could see that
[5:31] basically what's happening is it's being distorted directly through these like squares
[5:36] that are going up the image or these rectangles rather.
[5:38] So if I hit bar preview mode, we can actually see where those are.
[5:42] We can adjust the size and all of these things offset all kinds of controls and how much
[5:46] they're going to offset the image underneath.
[5:48] So that's what this tool is doing.
[5:50] And we have another one that's a little bit similar, but it's a slightly different effect.
[5:53] It's like a warping bar.
[5:54] It's more of a distortion that's going down the image, which sometimes happens on these
[5:57] older TVs.
[5:58] And there's a bunch of controls here as well.
[6:01] There are different styles of the warp bar you can use that will affect color and various
[6:06] other things as well.
[6:07] Now let's see how we combine that together to make a TV effect.
[6:10] A very simple three step process.
[6:12] So here we have a poly flow, which remember it creates a bunch of these tiny little shapes.


### Creating a TV Motion Graphic [6:13]
**Transcript (timestamped):**
[6:16] If you make it really, really small, it almost looks like pixels.
[6:19] So we can zoom in here.
[6:20] I put them diagonal, which maybe that wouldn't happen to CRT TV, but you know, create a freedom
[6:25] do whatever you want.
[6:26] So I wanted to make them more a little bit more sci-fi and exaggerated effect, but still
[6:31] feeling bound in the reality that we understand.
[6:34] So still feels like some kind of scan line effect going down.
[6:37] And then I put a warp bar right after that.
[6:40] So if we look at that, we have a bar that's distorting over the top.
[6:43] So now they're working together.
[6:45] And then for the blocky lines, I didn't actually use this as an offset because you can actually
[6:50] create an alpha from these as well.
[6:52] If you just have it in the preview mode, I just use it as a grade to kind of swipe over
[6:57] the top.
[6:58] So hit play with all three of those effects working together.
[7:01] Now we have something that's starting to get layered and feeling a little bit more convincing.
[7:04] We can control the timing of all these independently.
[7:07] So and that was all just for the off effect of the screen.
[7:10] This is not even before I started adding the logo and the graphics and all these things.
[7:15] That's simply for like the dim, the quote unquote dim pixels of this screen.
[7:20] Those are the few layers I used and combined together.
[7:23] So that's essentially what we got for like a base layer.
[7:26] And you can start to see how, you know, as we start to stack them and we get more complex
[7:30] look to have effects, we're going to need a lot of variation control.
[7:33] Okay, so I'm going to talk about another part of that shot and how I created some of the
[7:37] actual graphics for it.


### Creating Sci-Fi Motion Graphics [7:38]
**Transcript (timestamped):**
[7:39] So I'm just going to be going through a bunch of different nodes that we haven't talked
[7:42] about yet.
[7:43] But it's more interesting, I think, to look at these nodes rather than just like, hey,
[7:46] here's a bar generator.
[7:48] I think it's just more interesting to look at here it is in a shot and here's how it's
[7:51] being combined because you'll start to see immediately rather than just like looking one
[7:56] note at a time.
[7:57] Just to give you guys some ideas how this is constructed, it's very simple, actually.
[8:01] It's this is pretty much just like a really, I don't know, $10 model off the internet or
[8:06] something.
[8:07] And I just rendered some wireframes out of blender and basically just a few different
[8:11] colors here, which gives it a little bit more of a layered look to start with.
[8:15] And that means we could we could distort it differently and things like that.
[8:19] So again, if we just take a wireframe that has some colors and we multiply it against
[8:24] poly flow, well, now we're going to start to get something that has like what looks
[8:28] like different colored pixel effects.
[8:30] So we're already getting that sci-fi look pretty quickly.
[8:32] So if I continue down where it starts to get interesting now is where we combine some of
[8:37] these other offset controls.
[8:39] So at one point, the hologram starts in the center of the screen and then it kind of jumps
[8:43] up to the left side top corner.
[8:45] And so I'm using this node called jitter duplicate.
[8:48] So what this node does is essentially splits the color as it's being duplicated around
[8:53] randomly.
[8:54] And so that's going to save you a lot of work of, you know, having to transform and merge
[8:58] it back on itself and doing some kind of chromatic aberration node and some kind of a glass warp.
[9:03] You know, there's so many nodes that you'd have to do to just do something simple like
[9:07] this and it would be slow.
[9:09] So this is GPU accelerated.
[9:10] It's almost instantaneous.
[9:11] You can see I'm playing back and basically near real time with something that is already
[9:16] fairly complex.
[9:18] So we can keep going down.
[9:20] Basically same idea here.
[9:22] Actually, I'll show this.
[9:23] So here's the fact that if I had the blocky lines offset, it gives us these nice, you
[9:27] know, distortions right through there as it's teleporting.
[9:30] So it's really the layering of these effects where this tool starts to shine.
[9:35] So we have something like grid drips.
[9:37] This is kind of like sort of a matrixy type of rain and you can do it in both directions.
[9:43] If you multiply that against a poly flow, we get the pixel effect again, and then we
[9:47] start to merge all these together.
[9:50] I used again the poly flow node.
[9:52] This probably was my favorite one using this just for the holograms I needed for this specific
[9:56] shot.
[9:56] But this one, I just use some big squares in it.
[9:59] And then when you play that and you kind of merge it over itself, we get these really
[10:03] big squares.
[10:04] What I was doing it for was just to blend the black levels a little bit because it just
[10:09] looks better than I have a pitch black screen.
[10:11] So in the final shot, I'll show it at the end, but it kind of breaks up those blacks
[10:15] a bit.
[10:16] And then we add a little bit of bar graphs down here.
[10:19] So that's another node we have.
[10:20] This node is really, really extensive.
[10:22] There's a ton of presets, even though it looks basic here.
[10:26] There's a ton of like cap controls.
[10:28] You can taper them, gradient them off.
[10:30] So if we look a little further down, these ones are a little bit more complex.
[10:34] If we look at the generated results of these, there's a bunch of different controls here.
[10:39] So we could control like thickness, fade, break up.
[10:42] We could remove them.
[10:43] There's different color styles, different color schemes, etc.
[10:48] So I took a dark one over a bright one and just merged it over the image.
[10:52] And then I did like another one as well.
[10:54] I think I just blurred it a bit again to kind of blend those black levels and we get a nicer
[11:00] feeling effect.
[11:01] Maybe there's some kind of inner reflections happening on this old TV.
[11:04] We're going to think about the quality of the glass we're shining through.
[11:08] And then we can just keep going down and we get something like this.
[11:11] And then I added some text effects.
[11:15] This is actually just off mucus.
[11:16] There's a typing node that will like animate text.
[11:20] So you can just paste a whole block of text in there.
[11:22] So that wasn't part of this plugin, but useful to know if you're looking.
[11:26] It created some graphs.
[11:28] So there's some graphs on the bottom, for example, one of the nodes we have in the plugin
[11:32] is basically a bunch of different graphs and animations built into that as well,
[11:36] because that's a common effect that you need.
[11:39] Things like stacked bars, you know, that's pretty useful as well.
[11:43] That if you want to have like loading bars.
[11:45] So we have some various loading things here with a random numbers.
[11:49] The kind of things you'd see in motion graphics a lot was what I was trying to go for.
[11:52] It's like really hit as much possible to solve a lot of it.
[11:57] So if you look here, there's also this one, which is pretty cool.
[12:02] This is called dot grids and we can generate dots spawning in various patterns.
[12:07] So this is just one pattern of many in this node.
[12:11] So very useful for motion graphics against.
[12:15] We did this like kind of scanning effect going down.
[12:19] And then let's see if I go down the way.
[12:22] If there's anything else worth mentioning in this particular shot.
[12:26] I mean, this is the final panel that I was putting into the screen here.
[12:29] So there's a lot going on here.
[12:31] And once we add the essentially reflections over the top of this,
[12:36] we had the transitions, the transit transitions from the Compositing Academy logo
[12:39] at the beginning, if you remember the original shot.
[12:43] One more cool node here is the sort of sci fi rings that are appearing around the engines here.
[12:48] You see that they're sort of circling around.
[12:51] So essentially what that is is this node called sci fi rings, the node.
[12:57] And if I hit play, we can actually see what that looks like.
[13:00] This node can actually do quite a lot.
[13:01] You can scale these and animate them in a lot of different ways.
[13:04] Here it's fairly subtle, but I basically put it onto a card
[13:07] that matches up with the model rotating.
[13:10] So this card is actually kind of rotating around.
[13:13] And then when we look through the perspective,
[13:15] writing that 2D motion graphic onto what is essentially a card that matches our render.
[13:21] So if I hit play, it's a little bit hard to tell here.
[13:24] But once we look at it like this, yeah, that's what's happening.
[13:29] We have just some things that are saying, hey, this engine is spinning.
[13:33] And then we want to like visualize that in like a cool way.
[13:35] So that's that's kind of what this is.
[13:37] So everything I'm trying to design with a purpose as well,
[13:39] just sort of, you know, same things with visual facts.
[13:42] What's the story?
[13:43] What are we designing for?
[13:44] But now we have the tools to do it much, much faster to do this manually.
[13:48] We'll be so long.
[13:50] And that's the point here with all these tools is like, how much ground can we cover
[13:53] with a ton of presets and tons of tools and get most of the way there?
[13:58] So that is it for this YouTube video.


### Info - Watch Part 2 [14:00]
**Transcript (timestamped):**
[14:00] I'm going to put the part two of this video as a walkthrough on a separate link in the description.
[14:06] So if you want to watch every single node,
[14:09] we're going to go through all of these in detail.
[14:11] That will be a separate video.
[14:12] I just want don't want to make this specific video overly long
[14:15] because YouTube doesn't like that.
[14:17] So that video will be there for the people who want that really in detailed look
[14:22] on all of the nodes.
[14:23] And that's about it for this video, guys.
[14:24] So if you like it, hit thumbs up and I can keep making more content like this.



---

## Captured Frames

- [2:52] tutorials/frames/goodbye-after-effects-2d-motion-graphics-in-nuke/frame_000.jpg
- [4:20] tutorials/frames/goodbye-after-effects-2d-motion-graphics-in-nuke/frame_001.jpg
- [5:23] tutorials/frames/goodbye-after-effects-2d-motion-graphics-in-nuke/frame_002.jpg
- [5:53] tutorials/frames/goodbye-after-effects-2d-motion-graphics-in-nuke/frame_003.jpg
- [6:40] tutorials/frames/goodbye-after-effects-2d-motion-graphics-in-nuke/frame_004.jpg
- [8:45] tutorials/frames/goodbye-after-effects-2d-motion-graphics-in-nuke/frame_005.jpg
- [12:02] tutorials/frames/goodbye-after-effects-2d-motion-graphics-in-nuke/frame_006.jpg
- [12:52] tutorials/frames/goodbye-after-effects-2d-motion-graphics-in-nuke/frame_007.jpg

---

## Structured Notes

### Core Technique
Replace hand-animated 2D motion graphics (traditionally an After Effects job) with the GPU-accelerated `ScreenFX` plugin's library of customizable, near-real-time procedural nodes (shape/pattern generators, offset/distortion tools, transitions), layering multiple nodes together — masked and multiplied against each other — to build complex sci-fi HUD/hologram/CRT-screen graphics directly in Nuke's compositing pipeline, including 3D-tracked screen graphics projected onto a card that matches a rotating CG model.

### Summary
Compositing Academy tours the `ScreenFX` plugin (its own commercial Nuke plugin) for building 2D motion graphics — glitches, transitions, color distortions, HUD/hologram/CRT effects — without leaving Nuke or hand-animating in After Effects. Central to the workflow is `PolyFlow`, a shape generator with a "rain offset" control that fades/flips small shapes on and off for organic-feeling motion hard to fake with plain noise, plus size/edge/fade controls and built-in ID-pass-style color modes (like a CG object-ID pass, used to target different shape regions independently) and shape/side variation for sci-fi vs. other looks. Two offset/distortion tools — a "blocky lines" node (image scattered/distorted through animated rectangles, also usable as a swipe-transition alpha via its preview mode) and a "warp bar" (CRT-style vertical scan distortion) — are layered with PolyFlow (shrunk to near-pixel size) to build a convincing retro TV static/off-screen effect in three simple layers, each independently timed. For a sci-fi hologram graphic, a cheap Blender wireframe render (multiple flat colors for later independent targeting) is multiplied against PolyFlow for a colored-pixel look, then combined with `JitterDuplicate` (randomly splits/duplicates color as an effect appears, replacing what would otherwise require manual Transform+Merge+chromatic-aberration+glass-warp node chains, GPU-accelerated to near-real-time) to fake a teleport/materialize jump. Additional nodes covered: `GridDrips` (Matrix-style rain pattern, multiplied against PolyFlow for more pixel texture), large-square PolyFlow variants used purely to break up flat black levels for a more "glass/screen" feel, an extensive bar-graph generator (many presets: thickness, fade, break-up, color schemes/taper), a dot-grid pattern generator (multiple spawn patterns) for scanning-line effects, and a "sci-fi rings" animated-ring node applied to a 3D-tracked card that rotates in sync with a CG engine model, so the 2D graphic reads as projected onto the rotating 3D surface in perspective. A separate free Nucopedia text-typing node (not part of the ScreenFX plugin) is used for animated text blocks.

### Key Steps
1. Start from a single shape/pattern generator (`PolyFlow`) and explore its core controls: rain offset (fade/flip animation of individual shapes), center/edge size (spread vs. gradient taper), color modes (ID-pass-style per-shape/per-pattern targeting), and shape/sides count for stylistic variation.
2. Combine a shrunk-down PolyFlow (near-pixel scale) with a `Warp Bar` node (CRT-style vertical scan distortion) and a `Blocky Lines` node (used here as a swipe-transition matte via its alpha/preview mode) to build a layered, independently-timed off-screen/CRT-static base effect in three simple steps.
3. For CG-sourced graphics: render a cheap low-poly wireframe (e.g. from Blender) with multiple flat colors baked in, so later nodes can target different colored regions independently — same principle as a CG ID/Cryptomatte pass but authored directly into the asset's colors.
4. Multiply a colored wireframe render against a `PolyFlow` pattern to get a colored-pixel/sci-fi hologram texture quickly.
5. Use `JitterDuplicate` to fake a teleport/materialize "jump" — it randomly splits and duplicates color as the effect plays, replacing a manual Transform + Merge + chromatic-aberration + glass-warp node chain with one GPU-accelerated node running near real time.
6. Layer a `GridDrips` (Matrix-rain-style) pattern multiplied against PolyFlow for additional pixel-scale texture/detail.
7. Use large-scale PolyFlow squares merged over themselves purely to break up otherwise pitch-black regions of a screen graphic, simulating inner-glass reflections/imperfections rather than a flat black.
8. Add a bar-graph generator node (extensive presets: thickness, fade, break-up, taper, multiple color schemes) layered dark-over-bright and blurred slightly to blend black levels for a more "screen-glass" feel.
9. Add a dot-grid pattern generator (multiple built-in spawn patterns) for scanning-line/HUD-style detail.
10. Add animated text via a separate free Nucopedia typing gizmo (outside the ScreenFX plugin) for readable HUD text blocks.
11. For graphics that need to sit convincingly on a rotating/moving 3D object (e.g. sci-fi rings circling an engine): place the 2D `ScreenFX` graphic (e.g. "Sci-Fi Rings" node) onto a 3D card tracked/matched to the CG model's rotation, so the 2D motion graphic reads as if physically projected onto the rotating 3D surface when viewed through the camera.
12. Design every graphic element with narrative purpose (what story beat is this graphic communicating), using the plugin's speed to iterate through many looks quickly rather than hand-building each element from scratch.

### Nodes / Tools / Settings
- `PolyFlow` (ScreenFX shape generator) — rain offset, center/edge size, fade, color modes (ID-pass-style per-shape targeting), shape/sides count, fill toggle; usable at both pixel-scale and large-scale
- `Warp Bar` (ScreenFX) — CRT-style vertical scan-line distortion, multiple styles affecting color/warp
- `Blocky Lines` (ScreenFX) — animated rectangle-driven image distortion/offset; also usable as an alpha-based swipe-transition matte via preview mode
- `JitterDuplicate` (ScreenFX) — GPU-accelerated random color split/duplicate for teleport/materialize/glitch jumps, replacing a manual Transform+Merge+chromatic-aberration+glass-warp chain
- `GridDrips` (ScreenFX) — Matrix-style rain pattern generator
- Bar-graph generator (ScreenFX) — extensive preset library for loading bars/data graphs (thickness, fade, break-up, color schemes, taper)
- Dot-grid pattern generator (ScreenFX) — multiple spawn patterns for scanning/HUD dot effects
- "Sci-Fi Rings" node (ScreenFX) — animated ring graphic, applied via a 3D-tracked card matched to a rotating CG model for perspective-correct screen-graphic projection
- Nucopedia text-typing gizmo (free, not part of ScreenFX) — animates typed text blocks
- Cheap multi-color Blender wireframe render — used as an ID-pass substitute to target regions for independent grading/pattern targeting

### Difficulty
Intermediate

### Foundry App & Version
Nuke (3D system used for the card-projected sci-fi rings). No on-screen version banner or OCIO metadata visible in the captured frames — version not specified.

### Tags
motion-graphics, gizmo, compositing, 3d-system, digital-matte-painting, intermediate

---

## Related Tutorials
Shares the `ScreenFX` plugin with Create a Movie Quality Sci-Fi Laser Effect in Nuke (`create-a-movie-quality-sci-fi-laser-effect-in-nuke.md`), How I Made a FULL Star Wars Cinematic from JUST One Screenshot (`how-i-made-a-full-star-wars-cinematic-from-just-one-screenshot.md`), and How I Use Compositing to Skip THOUSANDS of Hours Rendering (`how-i-use-compositing-to-skip-thousands-of-hours-rendering.md`) — all use ScreenFX's procedural pattern library for sci-fi/hologram/glitch effects.
