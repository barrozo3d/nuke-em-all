---
title: Nuke Tutorial | Keying with Math Expressions [Intermediate]
source: YouTube
url: https://www.youtube.com/watch?v=uEzjEizAi3o
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)"
tags: [keying, compositing, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/nuke-tutorial-keying-with-math-expressions-intermediate/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Nuke Tutorial | Keying with Math Expressions [Intermediate]

**Source:** [YouTube](https://www.youtube.com/watch?v=uEzjEizAi3o)
**Author:** Compositing Academy
**Duration:** 5m41s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, just back here with another tutorial. This is a quick example of where we can use the expression node and a couple of basic math expressions to pull different types of keys that you might not otherwise be able to get easily.
[0:16] So if you want this project file, this is kind of the example shot I'm using here. It's just one thing I did in this project. You'll get this entire script and everything in the description below if you're interested.
[0:29] But basically what we're doing in this is just a quick example is, so these cars had some really highly saturated tail lights. So if I just zoom in here before these two grades, we see that the glow has this kind of almost over saturated ring around it.
[0:47] And so to solve that problem, I just kind of desaturated and did a little bit of a hue correction to kind of fix that effect. But in order to do that, we're plugging that into a mask, which means I had to have a good alpha around the edges, which is looking like this.
[1:04] So in order to get an alpha that looks like that, if I just zoom out here, intuitively, you might be like, well, that's pretty simple. We could just go to the key here. We could just check off the green and the blue.
[1:18] So you might try that. That might be your first intuition. And then you go to the alpha and you get something like this. So you can kind of play around, try to isolate that red area.
[1:28] But this is actually not the best key that you can get of that area. And there's a better way to do it. And also we're kind of getting all of the sky alongside our key, which is not exactly what we want.
[1:39] So there's other ways to do it. You might think you could do a hue correct. You could plug it in. You could, I'm just showing you a couple of different ways. You might not be familiar with these ways. So it might be helpful as well.
[1:52] You could go to the red suppress. You could take out the red of the image. And then you could minus that from the original. So I do a minus and invert it. So I just hit Shift X to invert the two inputs there.
[2:07] And we can see, okay, there's something kind of useful there. We could shuffle this red channel into the alpha. And that gives us actually kind of a decent result. But that's a lot of steps to kind of get a key of this area.
[2:21] And we're also still getting these kind of, I guess, bouquets that are in the background. So there is a better way for this shot. And it happened to be with just a really simple expression.
[2:32] So I'm going to teach you guys this technique. There's two expressions that I find pretty useful. And I use them occasionally. And I figured I'd share those with you. So if you plug in the expression node, what I was seeing here was if I was looking at the three color channels, looking at the red, and then green and blue, I could see there's a pretty significant difference between, for example, the red and the blue channel.
[2:56] So what you really want to do is find the difference between red and blue channels. So you're basically just subtracting the channels. But I wanted to actually take an average of the green and the blue first. So I want to take the green and the blue, average them together, and then have the red channels track that.
[3:14] So all you need to do really is just do green minus blue.
[3:19] I'm sorry, green plus blue divided by two. So that's going to give you the average of the green and the blue channel.
[3:28] So if I look at the alpha, that's the result. And then I'm just going to chuck another parentheses on there.
[3:35] And say R minus. So we want to say red subtract the average of the two other channels. And we hit enter. And you can see that basically gives us a key of this area, which is actually a pretty good key.
[3:50] If you compare it to the hue correct, it's a bit similar. But it's, you know, quick, simple expression, we don't have to mess around with doing hue corrections and minus and shuffles and stuff like that.
[4:01] Or, you know, grading up the white and black point.
[4:05] Another expression that is pretty useful for pulling a similar type of key is a really simple expression.
[4:13] So if you type in R minus G, so red minus the green channel, and then say multiplied by control.
[4:22] And what we do here now is we go up to the user tab, you go to the manage user knobs, and you want to add a floating point slider called control.
[4:33] And if you hit enter and you make that hit OK, this slider will allow you to adjust that key. So it's going to be multiplying the green channel.
[4:43] And the red is subtracting away from it. So this expression is particularly useful if you're removing tracking marker nodes, if you guys are ever removing sometimes they use pink tracking markers on set, which is the kind of the opposite of this like chroma, chroma green.
[4:59] So this is a really good way to isolate those. So if we go to that. So this is actually the result that's giving us. So if I move this slider around, you can see it's really isolating the red of the tail.
[5:13] Lights of this car and I can actually shift this beyond one here and I can shift it up and really isolate into that area with, you know, pretty good precision that, you know, maybe a normal here is not going to give you.
[5:27] So that's really the techniques. Two simple expressions. I'll chuck both of the expressions in the description below as well. And, you know, hopefully that helps out. So thanks so much.



---

## Captured Frames

- [0:29] tutorials/frames/nuke-tutorial-keying-with-math-expressions-intermediate/frame_000.jpg
- [1:18] tutorials/frames/nuke-tutorial-keying-with-math-expressions-intermediate/frame_001.jpg
- [2:07] tutorials/frames/nuke-tutorial-keying-with-math-expressions-intermediate/frame_002.jpg
- [3:35] tutorials/frames/nuke-tutorial-keying-with-math-expressions-intermediate/frame_003.jpg
- [4:22] tutorials/frames/nuke-tutorial-keying-with-math-expressions-intermediate/frame_004.jpg
- [5:00] tutorials/frames/nuke-tutorial-keying-with-math-expressions-intermediate/frame_005.jpg

---

## Structured Notes

### Core Technique
Pulling a clean single-color isolation matte (e.g. saturated red tail-lights) with a channel-math `Expression` node instead of a standard Keyer, HSV isolation, or manual channel-subtraction chain.

### Summary
Working shot: a car with over-saturated red tail-light glow needs a desaturating hue correction, which requires a clean alpha mask of just that red glow area. The obvious approaches — a `Keyer` isolating green+blue, or a manual red-suppress-and-subtract chain (invert, minus, shuffle red into alpha) — either grab unwanted background (sky, bokeh) or take too many nodes for a mediocre result. The presenter instead plugs an `Expression` node and writes two small channel-math formulas directly against the RGB channels to isolate the target hue with far fewer nodes and cleaner edges, then shows a second, more general-purpose variant with a user-added slider for interactive control — useful for isolating other saturated markers (e.g. pink tracking dots) too.

### Key Steps
1. Identify the problem area: a highly saturated single-hue region (red tail-light glow) needs its own alpha for a downstream Grade/HueCorrect fix, and is bleeding into the sky/background with a standard `Keyer`.
2. Try the "intuitive" approaches first (for comparison): `Keyer` with green+blue checked, and a red-suppress/invert/`Merge` (minus)/`Shuffle`-red-to-alpha chain — both work partially but are noisy or overly long.
3. Add an `Expression` node. Formula 1 (channel-difference key): compute the average of green and blue — `(g+b)/2` — then subtract that average from the red channel: `r-((g+b)/2)`. This isolates the "most red" content in the scene into a clean grayscale key, comparable in quality to the manual hue-correct chain but in one node.
4. Formula 2 (adjustable variant): `r-g*control` — red minus green, multiplied by a user-defined slider. Add the slider via the node's User tab → Manage User Knobs → New → Floating Point Slider, named `control`.
5. Animate/scrub the `control` slider to interactively tighten or loosen the isolation — can be pushed beyond a value of 1 for extra-aggressive isolation.
6. Note the general use case for formula 2: isolating on-set tracking markers of a strongly saturated color (e.g. pink markers, which are the "opposite" of chroma green) for removal/paint work.
7. Feed the resulting Expression-node alpha into the downstream correction (HueCorrect/Grade via a `Merge` "minus"/mask setup) instead of the alpha from the standard Keyer chain.

### Nodes / Tools / Settings
- `Expression` node — the core tool; channel-math formulas entered per output channel: `r-((g+b)/2)` (difference-from-average key) and `r-g*control` (adjustable variant using a custom slider).
- User Knob: custom `Floating Point Slider` named `control`, added via Manage User Knobs, driving the second expression's aggressiveness (can exceed 1.0).
- `Keyer` (luminance/HSV key, labeled `Keyer2 (luminance key)` in the node graph) — shown as the standard/intuitive first attempt for comparison.
- `HueCorrect` — used for the actual desaturation/hue fix once a clean alpha mask exists.
- `Merge` (operation "minus", with invert/Shift+X input-swap) — used in the manual red-suppress comparison chain.
- `Shuffle` — used to move the isolated red channel into the alpha channel in the manual comparison chain.

### Difficulty
Intermediate — requires comfort with Nuke's `Expression` node syntax and per-channel math, though the formulas themselves are simple.

### Foundry App & Version
Nuke — version not stated on screen or in narration. 2020 upload, predates this skill's release-notes backfill (starts at Nuke 13.0/March 2021), so treat as Nuke ~12.x era rather than a specific point release.

### Tags
keying, compositing, intermediate

---

## Related Tutorials
- Parallax HAX | Nuke Compositing [Advanced] (`parallax-hax-nuke-compositing-advanced.md`) — shares the self-referencing/user-knob expression-driven approach to building a reusable, tunable effect (there: parallax speed; here: keying math) instead of manual per-shot values.
