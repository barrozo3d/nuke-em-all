---
title: Nuke Tutorial | Compositing a Rainbow [Intermediate]
source: YouTube
url: https://www.youtube.com/watch?v=1lmyihzZHio
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)"
tags: [compositing, channels, procedural-texture, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/nuke-tutorial-compositing-a-rainbow-intermediate/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Nuke Tutorial | Compositing a Rainbow [Intermediate]

**Source:** [YouTube](https://www.youtube.com/watch?v=1lmyihzZHio)
**Author:** Compositing Academy
**Duration:** 8m43s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Introduction to nuke rainbows [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to another class here. This is just about how to create a rainbow effect inside of Nuke.
[0:07] If you're going over from Photoshop or something like that, multicolor gradients like this are pretty simple.
[0:13] But in Nuke, there's no simple way to actually do it. But it is actually a pretty easy technique.
[0:18] I'm just going to go over it quickly here and show you guys exactly how I created this effect.
[0:24] Just a quick example, breaking up through some noise and stuff like that and how you could actually use this in a shot.
[0:31] I'm going to go through that quickly. I'll also show you guys the preset that exists.
[0:37] But it's not 100% a rainbow. That's the downfall of this specific preset.
[0:44] We'll show you guys exactly how to do that. We're going to start by creating a ramp.


### Understanding HSV color space [0:47]
**Transcript (timestamped):**
[0:50] The key to this technique is actually using the color space node. We're going to be converting.
[0:57] If you never use this node and you're not familiar, essentially what we can do is we can double click this node.
[1:05] We can see that there's all these different types of settings here.
[1:08] But what we're concerned with is the one that says HSV. What that means is hue, saturation, and value.
[1:17] If I get my drawing tool here, what's going to happen with these three color channels?
[1:24] We're saying we're inputting a linear image. This is really not an in-depth video about color spaces.
[1:31] It's just a really brief explanation. If you guys already know a lot about color space, you can probably skip this quick part.
[1:38] Essentially what we're doing here is we're going to convert the red, green, and blue image into hue.
[1:45] This is going to go into red channel. This will go into red channel.
[1:51] Hue, which is the specific color, saturation, and this will go into green channel, and value, which is basically the luminance.
[2:02] This will go into blue channel. Hue is the range of colors. If we convert this into hue, there's no range of colors here.
[2:13] It's going to be empty. Saturation is also going to be empty because there's no difference in the color channels here.
[2:20] That channel will be empty. We do have a difference in value here because we have 0 and 1. That's the difference in value.
[2:28] That's going to be what's going to happen when we convert this image in this color space.
[2:34] If that's really confusing, you do just watch and you'll see exactly how it works.


### Creating the rainbow ramp [2:39]
**Transcript (timestamped):**
[2:39] Now that we have our ramp, I'm going to create a color space node and set that to HSV, like I just said.
[2:47] Immediately you'll see exactly what I just explained. The red, green, and blue channel, the red and green are empty and the blue has something.
[2:57] It's because there's no color differences in the hue and there's no difference in the saturation. Those channels are empty.
[3:06] What we need to do here is essentially, it's kind of a nuke trick to be able to do this.
[3:11] What we want to do is create a range of all of the hues that are possible.
[3:16] What we need to do is create a shuffle node.
[3:19] Because our blue channel has the 0 to 1 value, we can get the entire color spectrum by using this ramp.
[3:30] Essentially, all you need to do is, after you've converted it to this HSV, you take the V channel, which is the blue channel, and we want to shuffle this into hue.
[3:42] We're going to put it into the red channel.
[3:45] Then the next thing we need to do is we want to have 100% saturation in this picture.
[3:51] We want to have the full saturation of each color.
[3:54] In the green channel, we want to shuffle it to solid 1.
[3:58] In the blue channel, we also want to shuffle it to a solid 1 because we don't want the rainbow to get darker.
[4:05] If we copy this color space again, we paste it after, and you just hit swap.
[4:12] Now it's going to swap back to linear.
[4:14] Now you see it's actually created a rainbow.
[4:18] That's essentially how you do it.
[4:20] You just need to do linear to HSV, shuffle the channels like this.
[4:25] You shuffle the blue into the red, and then the green and the blue channel are just solid.
[4:31] Then you convert it back.
[4:33] Now you have a rainbow ramp that essentially you can control.
[4:37] It's going to automatically create that rainbow through that gradient.
[4:43] What's also pretty cool about this is, if we want to make that a circular rainbow,


### Circular rainbow remapping [4:44]
**Transcript (timestamped):**
[4:49] is if we were putting it inside of a shot or something like that, we also have a node here.
[4:54] This is a custom node from Nukepedia.
[4:56] You can get it in the script below if you want.
[4:58] Free download from Daniel Velikov in 2015.
[5:04] Essentially, if you guys have an After Effects background, it's just a polar coordinates node, but it's in Nuke.
[5:10] If we throw that on there, it's going to automatically remap our image to be a circular image.
[5:17] If we want to get rid of all this red on the outside, what we can do is just crop down to where our rainbow ends and just get something like that.
[5:27] It's going to remap.
[5:29] I'm going to put another crop.
[5:31] It's kind of a problem here.
[5:33] The bounding box for image needs to go all the way to the frame.
[5:37] This crop is not doing that, so I'm just going to put another crop right after.
[5:42] You'll see the bounding box goes to the edge of the frame.
[5:47] Now if we do the polar distort, it's going to wrap it like that.


### Adjusting colors and blending [5:51]
**Transcript (timestamped):**
[5:52] There's one other problem we have here.
[5:54] You see that red is supposed to be on the outside, purple is supposed to be on the bottom, and it's not exactly doing that.
[6:01] What we can do is put a grade node before the color space.
[6:05] I'll put a grade node here.
[6:07] If you adjust the gamma, you can actually shift these colors along the spectrum.
[6:12] That gives us a little bit of control in our colors here.
[6:18] You can also adjust the black point and white point if you want to go crazy and have multiple ripples of this kind of rainbow effect in here.
[6:26] Usually you just need the gamma and that's going to get you what you want.
[6:30] Alternatively, if you want to make this rainbow a bit thinner and you want to adjust it, again, you can go back to your ramp.
[6:36] Make the ramp a little bit smaller and then you would just adjust again your crop.
[6:42] You would just adjust the crop to that region.
[6:45] Make sure the bounding box goes to the frame and then do the polar distort.
[6:50] Then of course you could take this and take it further and then all it did was blur it a little bit, multiply it through a little bit of noise.
[6:58] This is probably going to appear in some clouds or mist or volume because that's usually where this is happening.
[7:05] You can transform it and move it around or do whatever.
[7:09] Also, I have a link below if you guys are interested in reading about the science of rainbows because it's basically just an optical effect.
[7:17] It's not a physical thing in the real world.
[7:19] This is a link that you can just read a little bit about it and understand what you're doing.
[7:25] Also, I just wanted to show you guys one last thing, which is the flare node that some of you guys might notice and be like,


### Alternative methods and conclusion [7:26]
**Transcript (timestamped):**
[7:31] Hey, there's already a node that creates a rainbow in Nuke.
[7:34] If you go to the flare and you go to presets and you say LG Rainbow, it kind of gives you a rainbow.
[7:41] But if you notice, it doesn't have the full color spectrum in here.
[7:44] I guess it's just not as flexible as using this technique.
[7:52] You can use that if you're just trying to create something like a lens flare or something like that.
[7:58] It has a couple settings here like chroma shift and stuff like that, which is useful.
[8:02] But again, it's just giving you these colors here so you're not getting the exact effect of a full rainbow, which is what we're creating here.
[8:12] So that's essentially the technique.
[8:14] Hopefully you guys got something out of it.
[8:16] Hit like if you like content like this.
[8:18] Again, I'm trying to create beginner content as well as kind of more intermediate and advanced content.
[8:24] I guess this would be more of an intermediate tutorial.
[8:27] So I know some of you guys are more advanced.
[8:30] I'll try to label each video on kind of what level I'm aiming for with each tutorial.
[8:35] So hopefully that saves you guys some time if you already know what I'm talking about.
[8:40] So thanks.



---

## Captured Frames

- [1:08] tutorials/frames/nuke-tutorial-compositing-a-rainbow-intermediate/frame_000.jpg
- [2:47] tutorials/frames/nuke-tutorial-compositing-a-rainbow-intermediate/frame_001.jpg
- [4:14] tutorials/frames/nuke-tutorial-compositing-a-rainbow-intermediate/frame_002.jpg
- [5:10] tutorials/frames/nuke-tutorial-compositing-a-rainbow-intermediate/frame_003.jpg
- [5:47] tutorials/frames/nuke-tutorial-compositing-a-rainbow-intermediate/frame_004.jpg
- [7:34] tutorials/frames/nuke-tutorial-compositing-a-rainbow-intermediate/frame_005.jpg

---

## Structured Notes

### Core Technique
Building a true full-spectrum rainbow gradient procedurally by converting a black-to-white `Ramp` into HSV space, remapping value into hue, and forcing saturation/value to 1 — then optionally polar-warping it into a circular rainbow with a Nukepedia `PolarDistort` node.

### Summary
Nuke has no built-in multicolor-gradient tool (unlike Photoshop), and the built-in `Flare` node's "LG Rainbow" preset doesn't cover the full color spectrum. Instead, the video builds a true rainbow from scratch using an HSV round-trip trick: a linear black-to-white `Ramp` is converted to HSV via `Colorspace`, its resulting Value channel (blue, holding the 0-1 gradient) is shuffled into the Hue channel (red), and Saturation/Value are forced to solid 1 so colors don't darken — then a second `Colorspace` set to HSV→linear (swap direction) converts it back, producing a full rainbow gradient. A Nukepedia `PolarDistort` node (Daniel Velikov, 2015 — Nuke's answer to After Effects' Polar Coordinates) can bend this linear ramp into a circular rainbow ring; a `Grade` node's gamma before the HSV conversion shifts the color order along the ring, and black/white point can create multiple repeating rainbow bands. Finishes with a stylistic pass (blur + multiply through noise) to fake the effect appearing in cloud/mist/volume, and a side-by-side comparison against the built-in `Flare` "LG Rainbow" preset to show why it falls short (limited color range).

### Key Steps
1. Create a `Ramp` node (linear black-to-white vertical gradient) as the base gradient driving the rainbow.
2. Add a `Colorspace` node set to convert `linear → HSV`. In HSV mode, Hue lands in the red channel, Saturation in green, Value (luminance) in blue — on a black/white ramp, only the Value/blue channel has meaningful data (0 to 1); hue and saturation are empty.
3. Add a `Shuffle` node: shuffle the Value/blue channel into the Hue/red channel (so the ramp's brightness range becomes a full hue sweep), and force green (saturation) and blue (value) channels to solid 1 so the rainbow stays fully saturated and bright rather than darkening toward one end.
4. Add a second `Colorspace` node, again set to HSV, but with the conversion direction swapped (`HSV → linear`) to convert the manipulated HSV data back into a viewable RGB rainbow gradient.
5. (Optional, circular rainbow) Add the Nukepedia `PolarDistort` node (Daniel Velikov, 2015 — free download, Nuke equivalent of After Effects' Polar Coordinates) after the rainbow ramp to remap it into a circular/ring shape.
6. Before the polar distort, add two `Crop` nodes in sequence: the first crops the ramp down to where the desired rainbow band ends (removing the outer flat red); the second re-establishes the crop's bounding box out to the full frame edge (a Nuke quirk — the first crop's bounding box doesn't reach the frame, which breaks the polar remap without this second crop).
7. If the color order comes out wrong (e.g. red should be on the outside, purple at the bottom, but isn't), insert a `Grade` node before the first `Colorspace` and adjust gamma to rotate/shift the hue order around the spectrum; black point/white point can be pushed further to create multiple concentric rainbow rings.
8. To make the rainbow band thinner, shrink the source `Ramp` region and re-adjust the crop region accordingly before the polar distort.
9. Optional finishing: blur and multiply the rainbow through a noise pattern, then transform/position it, to fake it appearing within cloud, mist, or volumetric haze in a shot.
10. For comparison: the built-in `Flare` node → Presets → "LG Rainbow" gives a quick fake rainbow with controls like chroma shift, but does not cover the full color spectrum — fine for a lens-flare-style effect, not a true rainbow.

### Nodes / Tools / Settings
- `Ramp` — base linear black-to-white gradient (the "canvas" the rainbow is built from).
- `Colorspace` (used twice) — first instance: `linear → HSV`; second instance: `HSV → linear` (direction swapped) to convert back to viewable RGB after the hue manipulation.
- `Shuffle` — moves the HSV Value/blue channel into the Hue/red channel; sets green (saturation) and blue (value) channels to solid 1.
- `PolarDistort` — third-party Nukepedia gizmo by Daniel Velikov (2015), free download; performs polar-coordinate remapping (linear gradient → circular/ring rainbow), equivalent to After Effects' Polar Coordinates effect.
- `Crop` (x2, stacked) — first limits the ramp to the desired rainbow band; second forces the bounding box back out to the full frame so the polar distort doesn't clip incorrectly.
- `Grade` — inserted before the first Colorspace; gamma shifts color order around the spectrum, black/white point can multiply the rainbow into repeating bands.
- `Flare` node, "LG Rainbow" preset — the built-in alternative shown for comparison; has chroma-shift controls but incomplete color spectrum.
- Finishing touches (unnamed in transcript): Blur + Multiply through a noise source to integrate the rainbow into cloud/mist/volume; Transform to reposition.

### Difficulty
Intermediate — requires understanding of HSV color space and channel manipulation via Shuffle, though the node chain itself is short.

### Foundry App & Version
Nuke — version not stated on screen or in narration. 2020 upload, predates this skill's release-notes backfill (starts at Nuke 13.0/March 2021), so treat as Nuke ~12.x era rather than a specific point release.

### Tags
compositing, channels, procedural-texture, intermediate

---

## Related Tutorials
- Build Entire FX with ONE Pass - Nuke Tutorial (`build-entire-fx-with-one-pass---nuke-tutorial.md`) — shares `compositing`, `channels`, `procedural-texture`, `intermediate`.
- Create 3D Noise | Nuke Compositing (`create-3d-noise-nuke-compositing.md`) — shares `compositing`, `channels`, `procedural-texture`, `intermediate`; both build procedural patterns purely through channel/expression manipulation.
