---
title: Moire Patterns | Nuke Tutorial [Intermediate]
source: YouTube
url: https://www.youtube.com/watch?v=gS4zXJ6sLs8
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "Nuke 13.x (13.1/13.2 — exact 2022 point-release not stated)"
tags: [procedural-texture, gizmo, compositing, st-map, rotopaint, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/moire-patterns-nuke-tutorial-intermediate/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Moire Patterns | Nuke Tutorial [Intermediate]

**Source:** [YouTube](https://www.youtube.com/watch?v=gS4zXJ6sLs8)
**Author:** Compositing Academy
**Duration:** 7m5s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Introduction to moiré [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to another video. This time we're going to talk about how to make a
[0:13] Moire effect in Nuke. And I think I'm pronouncing it right, but you know, there's some different
[0:19] sources out there when you Google it. That kind of pronounced it differently, but according
[0:24] to Wikipedia, it's Moire, so this is how it's pronounced in French. So hopefully that's
[0:30] right. But basically this effect is, you know, basically two intersecting lines and it creates
[0:36] this sort of pattern. And you see this kind of effect if you're walking, you know, maybe
[0:41] behind some kind of chain link fences and they're overlapping. You also see it looking
[0:46] at like LED screens if you're filming it. So you may have seen something like this before.
[0:52] And so this effect is really useful, especially for the screens, because you can make like
[0:55] really old looking screens and all those type of effects. And you know, there's shows and
[1:01] stuff like that that have done prominent effects. So if you look at something like WandaVision,
[1:05] you know, you can look at the big wall they did and you're seeing this effect being warped
[1:10] in there. And actually it's a pretty straightforward effect. It's not that hard to create. So that's
[1:14] what this video is about. And yeah, we'll get into it. So basically, this effect really


### Creating the line pattern [1:18]
**Transcript (timestamped):**
[1:20] just consists of making two sine waves and intersecting them and kind of rotating them.
[1:27] So it's actually very simple. And the way you can do this is using expression though.
[1:32] And you can just do the expression, you can do it in the alpha channel or the color channels.
[1:38] You could just do sine X. And then you're going to get this like sort of sine wave across,
[1:45] you know, horizontally across your screen. If you want to make those lines bigger, you
[1:49] can divide it by number. So you can divide it by like, let's say 10. And you'll see that
[1:54] the lines get thicker. So basically, you want to create that pattern. And I left the lines
[1:58] really thin because this effect is more prominent when there's a lot of intersecting lines.
[2:03] So basically, I created a node that kind of just does this automatically. So I don't have
[2:07] to type expressions. Because I use these lines pretty frequently when I'm doing like patterns
[2:12] and stuff like that. So I find this useful. And the other thing you want to do, the other


### Offset and transform nodes [2:13]
**Transcript (timestamped):**
[2:18] node I found here, this is off Nucopedia. So I'll just attach these two in a new script
[2:22] if you guys want them. But this is offset nodes. So basically, just makes it easy to
[2:27] if you have like a checkerboard. And if you move it, like for example, if I move this
[2:31] horizontally, wherever or however far I move it off this side of the screen, it will reappear
[2:36] over here. So basically, if I offset it, you'll see as I shift it, it's coming back on this
[2:42] side of the screen. So that's all it does. And that just makes it easier for this effect.
[2:48] So basically, what you want to do is after we have one line, we want to do another one,
[2:53] just a copy of it. And I'll just I just offset it by 20 pixels. So I just basically transform
[2:58] in x 20 pixels. And so we just want to kind of misalign those lines a little bit. And


### Interference and rotation [3:04]
**Transcript (timestamped):**
[3:04] then what we can do is also rotate it. So the rotation is actually mainly where its effect
[3:08] is coming from. So if you rotate one of the lines, and you mask the other one, you'll
[3:14] start to see this sort of interference pattern happening. So if we kind of turn it back to
[3:19] zero, just to show you guys. So we have zero, nothing's really happening, a little bit's
[3:24] happening because this might be not completely over each other. But if we really the rotation
[3:29] is causing this effect, you see immediately starts to happen as soon as we add that rotation.
[3:35] So that's pretty cool. But one way we can make this more interesting is to actually do a


### Distortion techniques [3:36]
**Transcript (timestamped):**
[3:39] little bit of a grid warp, and you'll get more of those like kind of organic more effects
[3:44] in there. So you can add some slight warps to one of the patterns. So if I turn on the
[3:48] grid warp, you'll see that we can actually get these like circular patterns in here.
[3:53] And that's pretty cool, because you can kind of, you know, animate this in a way that,
[3:58] you know, maybe if you know, if you're doing some kind of really cool fact where like an
[4:02] arm is coming through a screen or someone's passing through a surface, you could kind
[4:06] of warp these patterns around that object that's like passing through. Or if you're
[4:12] doing some kind of zoom in, and you're doing some kind of matrix type of thing, you could
[4:16] you could play with the distortion and sort of drive it that way. Another way you could
[4:22] kind of drive the distortion would be just using a UV pattern, and then kind of ST mapping
[4:28] it on. And what you can do is do a roto paint. So again, there's a story out there on my
[4:34] channel about UVs ready. So if I go to the roto paint, you can go to where is it here,
[4:41] the smear, and we can just make that bigger and then I can just kind of draw and you'll
[4:47] see that that pattern kind of gets distorted. And what's nice about doing it that way is
[4:52] you can actually animate that stroke. So if you go into the roto paint, go to the stroke
[4:56] tab, you can kind of animate that thing. So you could do some kind of crazy, you know,
[5:02] animation passing through there. So that's just another way to do it. But we've already
[5:07] got the pattern working here. If you want to make it look more like a television screen,


### Adding color and final look [5:12]
**Transcript (timestamped):**
[5:12] and add those rainbow colors, it's really just the same technique we use multiple times
[5:16] in different tutorials on the channel ready, which is how to make a rainbow. So there's
[5:20] a video called how to make a rainbow nuke, which basically, I'll cover it about five
[5:24] seconds here, but you can find the full video, just basically going linear to HSV, doing
[5:30] this in the shuffle node, and converting it back. And that's going to make a rainbow
[5:35] automatically. But if you apply that directly to the pattern, and basically, before that,
[5:43] I just shuffled out the alpha into all the channels. So all the color channels, red,
[5:47] green, blue, alpha, they all match this. So you can see I've just done this into all the
[5:51] channels. But if you apply this directly, it doesn't look that great. It's kind of, you
[5:57] know, I mean, there's like rainbow in there, but it's not, it's not rolling into the highlights
[6:02] in the way that we would like. So what you can do is simply blur your picture. So you're
[6:06] kind of averaging it so that the ridges are like the whitest part, and then the kind of
[6:12] troughs, I guess, are like the darkest, and then you convert it into this rainbow space.
[6:18] So now your lines, instead of looking something like this, which isn't that useful, it looks
[6:22] more like this. And you can take that pattern and multiply it against the original. So here's
[6:28] our original. Here's a little rainbow blurred version we did, and then we just multiply
[6:32] it against it. And now if we hit play, we have this sort of like television moire effect
[6:38] that's kind of animated. So hopefully that is useful. And you know, you can mix that
[6:43] in and use it as kind of a render pass or something you mix in in your composite if
[6:48] you're doing these type of effects. And that's a pretty quick and simple way to do it. There
[6:53] might be other ways to do it out there and definitely play around with it. I'll also
[6:57] attach the links there if you want to read more about this effect, like the more of the
[7:01] science behind it. But yeah, hopefully that's useful.



---

## Captured Frames

- [1:45] tutorials/frames/moire-patterns-nuke-tutorial-intermediate/frame_000.jpg
- [2:58] tutorials/frames/moire-patterns-nuke-tutorial-intermediate/frame_001.jpg
- [3:29] tutorials/frames/moire-patterns-nuke-tutorial-intermediate/frame_002.jpg
- [3:48] tutorials/frames/moire-patterns-nuke-tutorial-intermediate/frame_003.jpg
- [4:47] tutorials/frames/moire-patterns-nuke-tutorial-intermediate/frame_004.jpg
- [6:22] tutorials/frames/moire-patterns-nuke-tutorial-intermediate/frame_005.jpg
- [6:32] tutorials/frames/moire-patterns-nuke-tutorial-intermediate/frame_006.jpg

---

## Structured Notes

### Core Technique
Procedurally generating a Moiré interference pattern (the visual "beating" effect from two overlapping fine line/grid patterns, as seen filming LED screens or through chain-link fences) using a `sin(x)` expression to build thin repeating line patterns, offsetting and rotating a duplicate against the original to create the interference, then optionally warping with `GridWarp` or an animated `RotoPaint` stroke and colorizing through a blur→HSV rainbow pass for an old-CRT-television look.

### Summary
A short, focused procedural-pattern tutorial. The base pattern (frame_000/001) comes from a single `Expression` node: `sin(x)` on the alpha (or color) channel produces a repeating sine-wave line pattern across the frame; dividing `x` by a number (e.g. `sin(x/10)`) thickens the lines — thin lines are kept deliberately, since the Moiré effect reads more strongly with more intersecting lines per area. The author has a personal Nukepedia gizmo that automates this line-generation (so no manual expression typing is needed day-to-day) plus a companion **Offset** gizmo that wraps content back onto the opposite edge when shifted (useful for tiling this pattern, similar to a `Checkerboard`). A duplicate of the line pattern is nudged (`Transform` ~20px in X) to slightly misalign it from the original (frame_002), and — critically — **rotated**: rotation of one copy relative to the masked-off other is what actually produces the interference "beating" pattern; at 0° rotation almost nothing happens, but interference appears immediately once rotation is introduced (frame_003 shows the un-rotated warped-grid state, for contrast). For a more organic look than pure straight-line interference, a `GridWarp` applied to one of the two line layers produces circular/swirled Moiré patterns (frame_004) — useful as an animatable effect for a hand or object passing through a screen surface, or a "matrix zoom" style distortion. An alternative, more art-directable distortion driver is an animated `RotoPaint` stroke (Smear tool, sized up) whose stroke tab can be keyframed over time to drive organic warping through the pattern (frame_006) — cross-referenced to the channel's own UV-workflow tutorial for the underlying ST-map/UV distortion-driving technique. To finish it as a "TV screen" look: shuffle the alpha into all of R/G/B/A so the pattern is neutral gray across channels, `Blur` it (averages ridges to white, troughs to black instead of a hard sine edge), then run the same Linear→HSV→shuffle "rainbow" trick used elsewhere on this channel (cross-referenced to the dedicated "How to make a rainbow" Nuke tutorial) to colorize it (frame_005 shows the resulting magenta/orange banded rainbow interference pattern) — applying the rainbow trick to the sharp unblurred pattern directly looks flat, so the blur step first is what makes the color roll convincingly into highlights/shadows. Finally, `Multiply` the colorized rainbow pattern against the original sharp Moiré pattern to combine detail with color, producing an animated CRT/old-screen Moiré effect usable as a render pass or comp element (e.g. the "old TV" look used in shows like WandaVision).

### Key Steps
1. Generate a thin repeating line pattern with an `Expression` node: `sin(x)` (or `sin(x/N)` to thicken the lines) on alpha or a color channel. Keep lines thin for a stronger Moiré effect (more intersections per area).
2. (Optional/author's convenience) Wrap this into a reusable gizmo, plus a companion **Offset** gizmo (Nukepedia) that wraps shifted content back onto the opposite edge — useful for tiling the line pattern like a `Checkerboard`.
3. Duplicate the line layer; `Transform` it slightly off-axis from the original (e.g. 20px in X) so the two copies aren't perfectly stacked.
4. **Rotate** the duplicate relative to the (masked) original — this rotation is what actually generates the Moiré interference pattern; without rotation, little to no interference appears even with the copies offset.
5. For a more organic, non-linear interference look: apply `GridWarp` to one of the two line layers before combining — produces circular/swirling Moiré patterns instead of straight banding, and can be animated to simulate an object passing through the pattern.
6. Alternative distortion driver: an animated `RotoPaint` stroke (Smear brush, enlarged) whose Stroke tab is keyframed over time, used as an ST-map-style UV distortion source for more art-directed, hand-animated warping (cross-referenced to this channel's UV/ST-map tutorial).
7. To colorize as an old-TV look: `Shuffle` the pattern's alpha into all of R/G/B/A (neutral grayscale across channels), `Blur` it so ridges read as bright and troughs as dark (rather than a hard binary sine edge), then convert Linear→HSV, remap, and shuffle back to RGB (the same "rainbow" technique used in this channel's dedicated rainbow tutorial) to get smooth color banding.
8. `Multiply` the blurred/colorized rainbow pass against the original sharp Moiré pattern to recombine fine interference detail with the rainbow coloring, yielding the final animated CRT/television Moiré effect — usable as a standalone render pass mixed into a larger composite.

### Nodes / Tools / Settings
- **Core Nuke:** `Expression` (`sin(x)` / `sin(x/N)` for line generation), `Transform` (small offset + rotation between two copies), `Shuffle` (alpha → all RGBA channels), `Blur`, `Multiply` merge, HSV round-trip (Linear→HSV via `Colorspace`/`Shuffle`, remap, back to RGB) for the rainbow coloring pass
- **`GridWarp`** (built-in Nuke node) — used for organic/circular Moiré distortion instead of pure straight-line interference
- **`RotoPaint`** — Smear brush with an animated Stroke tab, used as an alternative, hand-art-directable distortion driver via ST-map-style UV warping
- **Nukepedia gizmos:** a personal line-pattern generator gizmo (automates the `sin(x)` expression) and a companion **Offset** gizmo (wrap-around edge offset, like a tileable `Checkerboard`)
- **Real-world reference cited:** chain-link fence overlap, filming LED/CRT screens, and the WandaVision "big wall" VFX sequence as a prominent production example of this effect

### Difficulty
Intermediate — the underlying idea (two rotated line patterns interfering) is simple, but building it cleanly requires comfort with expressions, offset/rotate node chaining, and the HSV rainbow-coloring trick as a supporting technique.

### Foundry App & Version
Nuke. Version not stated on screen; per this skill's version-tracker, a 2022 upload falls in the Nuke 13.1 (Nov 2021) → 13.2 (Apr 2022) window. No version-specific features used — `Expression`, `Transform`, `GridWarp`, `RotoPaint`, and Shuffle/Colorspace have been stable across many releases.

### Tags
procedural-texture, gizmo, compositing, st-map, rotopaint, intermediate

---

## Related Tutorials
- Nuke Tutorial | Compositing a Rainbow [Intermediate] (`nuke-tutorial-compositing-a-rainbow-intermediate.md`) — this Moiré tutorial explicitly reuses that video's Linear→HSV "rainbow" technique (blur → HSV round-trip → multiply) as its final colorization step.
- 360 Spherical LatLong Textures | Nuke Tutorial (`360-spherical-latlong-textures-nuke-tutorial.md`), Mixed Medium VFX P1 (`mixed-medium-vfx-p1-blender-nuke-ai-embergen-vr-tutorial.md`), and A new way to design VFX | Gravity Sketch + Nuke (`a-new-way-to-design-vfx-virtual-reality-gravity-sketch-nuke-tutorial.md`) — all build procedural patterns for creative/technical purposes using expression-driven and gizmo-based Nuke techniques from the same channel's toolkit.
