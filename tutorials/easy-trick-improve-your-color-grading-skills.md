---
title: EASY TRICK: Improve your Color Grading skills
source: YouTube
url: https://www.youtube.com/watch?v=dVN7IK1GsLA
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "not specified -- no title bar or About dialog in any frame; the viewer does show an ACES OCIO config"
tags: [grading, channels, color-management, compositing, beginner]
extraction_status: complete
frames_dir: tutorials/frames/easy-trick-improve-your-color-grading-skills/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# EASY TRICK: Improve your Color Grading skills

**Source:** [YouTube](https://www.youtube.com/watch?v=dVN7IK1GsLA)
**Author:** Compositing Academy
**Duration:** 4m17s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, in this video we're going to take a look at how to do a targeted hue shift using some basic techniques.
[0:06] So this is before we had some footage that we shot a prop that's casting some bounce lighting onto our character.
[0:12] But I wanted it to be more like an orange lantern type of color.
[0:15] And this is kind of just a quick shift of color that we can do here.
[0:19] Now we don't want to shift the colors of everything.
[0:21] We really just want to target one set of colors and shift it into another color channel.
[0:26] So the technique is actually very, very simple.
[0:28] It's actually just using the copy node, but we have to actually remember the principles of the color channels first and why this technique actually works.


### Concept [0:30]
**Transcript (timestamped):**
[0:36] So I'm going to explain that right now.
[0:38] So basically we have an image that's made up of red, green and blue, which most of you guys already know.
[0:42] So if I want to make this a little bit more orange, orange is a combination of red and a little bit of green.
[0:49] So essentially what we want to do is take some of the red channel, which we can see here, compared to the green,
[0:55] which is darker in this area, and we want to bring some of this part of the red channel into the green channel.


### Mixing channels [1:00]
**Transcript (timestamped):**
[1:00] So we're just mixing the channels together a little bit.
[1:03] So why this works is, you know, basically like this.
[1:06] So we have red and green, which makes a yellow, but we don't want yellow.
[1:10] We want orange.
[1:11] So we want red and a little bit of green.
[1:13] So we can take down the green and we get orange.
[1:17] So basically what we want to do is actually mix in a little bit of the red channel into the green channel,
[1:23] but not completely because we don't want to get yellow, like I just said.
[1:26] So let's take a look at what that actually looks like.
[1:29] It's pretty straightforward.
[1:30] If I set this back to zero, if I copy the red channel into the green channel, again, the red channel looks like this.
[1:36] The green channel looks like this.
[1:37] It's darker.
[1:38] So I know that it's going to get hit in the right places.
[1:41] We're getting the color into the right places.
[1:43] So if I set this to one, you see that we're getting the result that we expected.
[1:46] It's kind of a yellowish green.
[1:48] It's not exactly, you know, perfectly yellow, but it's pretty much what we're expecting here.
[1:52] So what you can do is red to green and then I just shift this down a tiny bit and we're going to start to get something that looks like orange.
[1:57] So if I disable, you have something that's reddish and then we have something that is orange.
[2:02] And, you know, we can do some enhancement after that where we can, you know, key the highlights and things like that to make this look more metallic.
[2:08] Those are things that are unrelated, but the technique here of just huge shifting by mixing the channels is a really powerful and simple technique.


### Color channel ratio [2:15]
**Transcript (timestamped):**
[2:15] So, you know, it's good to remember that the color channels are just a ratio of colors.
[2:20] So if we have a hundred percent white, remember that's going to be one, one, one in all the color channels.
[2:25] And if we have some different color, it's a different ratio of colors.
[2:28] And so another thing to remember in the future is if you're desaturating, what you're actually doing is just bringing the color channels closer together.
[2:36] So if we're desaturating, what's happening is it's finding a luminance value and kind of evening them out together.
[2:41] So the color channels become the same when you're desaturating to zero.
[2:45] So if I take a colorful image, desaturated to zero, red, green, and blue are all equal.
[2:50] So it's doing the same thing.
[2:51] It's just making the ratio equal.
[2:53] But if we play around with that ratio by dissolving or mixing the color channels together, which is what this copy note is doing, it's not the same as a huge shift.
[3:01] A huge shift is going to shift all the colors around.
[3:03] It's not exactly the same thing.


### Other ways [3:05]
**Transcript (timestamped):**
[3:05] So this is a really good way to get very smooth gradients and that color shift without having like weird targeted blobs.
[3:11] So there's many other ways to do this.
[3:13] This is not like a one trick kind of thing on how you can do a color correction.
[3:17] There are many different ways to do targeted color corrections.
[3:19] And these are some of them.
[3:20] We have hue correction, which is probably the most common.
[3:22] We have HSV tool, which you can target different range, kind of similar to resolve.
[3:27] And you can also do a keer targeting, you know, like a red keer, for example.
[3:31] So those would be other ways to do it.
[3:33] But most people don't know about the copy technique.
[3:35] It's pretty good to just mix the channels around and get a good result.
[3:38] So I do think the result for this is actually sometimes better than using these other tools.


### Conclusion [3:40]
**Transcript (timestamped):**
[3:42] For example, if I do a hue shift, we could, you know, bring up the green in the red area.
[3:47] So we go to the green and bring up in the red areas.
[3:50] And you can see that some of the edges are not perfect.
[3:53] So we can see that fall off is not 100% getting exactly what we want.
[3:57] And you can try to mess with this and play around with it.
[3:59] But sometimes you're not getting the perfect blend.
[4:02] And the same with the HSV tool.
[4:03] You can run into similar issues where it's not a perfect blend.
[4:06] You're getting a harsh matte.
[4:08] Even same with the keer node.
[4:10] This one's probably a little bit better, but similar results.
[4:13] So that's about it, like I said.
[4:15] And leave a like if you liked this video.



---

## Captured Frames

- [0:45] tutorials/frames/easy-trick-improve-your-color-grading-skills/frame_000.jpg
- [1:30] tutorials/frames/easy-trick-improve-your-color-grading-skills/frame_001.jpg
- [2:00] tutorials/frames/easy-trick-improve-your-color-grading-skills/frame_002.jpg
- [2:40] tutorials/frames/easy-trick-improve-your-color-grading-skills/frame_003.jpg
- [3:20] tutorials/frames/easy-trick-improve-your-color-grading-skills/frame_004.jpg

---

## Structured Notes

### Core Technique
A targeted hue shift (e.g. turning a reddish bounce-light color into orange) can be achieved by partially mixing one color channel into another with a `Copy` node — since a color is just a ratio between R/G/B, copying part of the brighter channel (red) into the darker channel (green) shifts the hue smoothly, without the harsh/imperfect falloff edges typical of `HueCorrect`, the HSV tool, or a `Keyer`-based approach.

### Summary
Compositing Academy demonstrates a simple but underused targeted-hue-shift technique: to turn reddish bounce lighting on a character into a warmer orange-lantern color, use a `Copy` node to partially blend the red channel into the green channel (not fully — full red+green mixing gives yellow, not orange), scaled down via the copy's mix control until the desired orange balance is reached. The underlying principle explained: RGB channels are simply a ratio (pure white = 1,1,1 in all channels; desaturating to zero works by bringing all channel values toward a shared luminance value, evening the ratio rather than removing color information), so deliberately un-evening that ratio — mixing part of one channel into another — reproduces real color-theory mixing (red+green=yellow; red+less green=orange) directly in the image's own channel data. The channel-copy technique is contrasted with three more common targeted-correction tools — `HueCorrect`, the HSV tool (similar to Resolve's qualifier), and `Keyer`-based (e.g. a red key) corrections — noting that all three can produce visibly imperfect falloff/edges or a "harsh matte" look at the boundary between corrected and uncorrected regions, whereas the channel-mix approach tends to give a smoother, more natural gradient since it operates on the image's inherent luminance relationships rather than an externally-defined selection range.

### Key Steps
1. Identify the target hue shift in terms of RGB channel math — e.g. orange = red plus a smaller amount of green (not equal red+green, which yields yellow).
2. Compare the source channels visually (e.g. view the red channel alone, then the green channel alone) to confirm which channel is naturally brighter/darker in the region you want to shift, so you know the copy will land correctly.
3. Add a `Copy` node and copy the brighter channel into the target channel. **Confirmed exactly** [frame_001, frame_002]: the node is `Copy2`, its first row set to `Copy channel` **`rgba.red`** → **`rgba.green`** with all three remaining rows at `none`, `Layer Copy` none, `Set BBox to` **union** with metadata and range from **B**, `mask` none, `(un)premult by` none. The backdrop it sits in is labelled **"hue shift by mixing channels"** [frame_001].
4. Set the copy's mix/amount to see the full effect, then adjust until the desired hue is achieved. **The set finally pins the number this entry never carried**: `mix` reads **0.065** at 1:30 [frame_001] and **0.35** at 2:00 [frame_002].
    ⚠️ Two caveats on the recorded procedure. **Neither frame shows `mix` at 1**, and between the two captures the value goes **up**, not down — so "set to 1 first, then dial down" is not what these two moments show. Treat **0.35** as the settled working value and the 1-then-downward procedure as narration.
5. Layer supplementary unrelated corrections afterward if needed — these are separate from the core channel-mix hue-shift technique. One such node is captured directly beneath the `Copy` in the properties bin [frame_001]: a `Grade16` on `channels rgb` with `blackpoint` 0, `whitepoint` 1, `lift` 0, **`gain` 0.2**, `multiply` 1, `offset` 0, `gamma` 1, `mix luminance` 0, `mix` 1.
6. Remember the ratio principle for grading generally: full white is equal values across all channels; desaturating toward zero works by pulling all channels toward a shared luminance value (evening the ratio), while a channel-mix hue shift deliberately un-evens the ratio in a controlled way.
7. Compare against alternative targeted-correction tools when precision at the correction's edge matters. **All three comparisons are built in the script and captured in one shot** [frame_004], each in its own backdrop:
    - `Keyer1 (red keyer)` → feeding a `Grade3` through its **mask** input (teal backdrop)
    - `HSVTool1` → feeding a `Grade1` through its **mask** input (green backdrop)
    - `HueCorrect1`, standing alone (purple backdrop)
    That the first two drive Grades *through mask inputs* while HueCorrect works directly is the structural reason their edges behave differently — the entry described the comparison but not how it was wired.

### Nodes / Tools / Settings
- `Copy` — core technique node. As configured [frame_001, frame_002]: `rgba.red` → `rgba.green` on row 1 only, `Set BBox to` union / metadata B / range B, **`mix` 0.35** (0.065 at an earlier moment). Partially copies one color channel's data into another to achieve a targeted, smooth hue shift based on the image's own luminance ratios
- `HueCorrect` — common alternative targeted-hue tool; can show imperfect falloff at the correction's edge. In the script it is `HueCorrect1`, used on its own with no mask [frame_004]
- `Grade` — the supplementary correction layered after the hue shift; the captured one (`Grade16`) runs `gain` **0.2** with everything else at default [frame_001]
- HSV tool — range-based color targeting (compared to DaVinci Resolve's qualifier); similar edge-falloff imperfections possible
- `Keyer` (e.g. red key) — selection-based targeted correction; generally the best of the three alternatives shown but still not as smooth as the channel-mix approach in this example. Wired as `Keyer1 (red keyer)` → **mask** input of `Grade3` [frame_004]
- Plate: `Plate_Denoised_00##.exr`, **HD_1080 1920×1080**, viewer display transform **`sRGB (ACES)`** [frame_000]
- Script furniture: `RED_CHANNEL` / `GREEN_CHANNEL` / `BLUE_CHANNEL` backdrops feeding a `Dissolve1` for the channel-comparison of Key Step 2, a `Saturation 0` backdrop for the ratio demonstration, and `Constant1` / `Constant2` (red and green) for the colour-mixing demonstration [frame_000, frame_003]
- The menu bar carries two custom toolsets, **`AlexsTools`** and **`CompAcademy`** — worth knowing when a menu path in this author's tutorials does not exist in stock Nuke [frame_000]

### Difficulty
Beginner

### Foundry App & Version
Nuke. **The version is still not determinable** — no title bar, About dialog or version banner appears in any frame.

⚠️ **But the "no OCIO metadata visible" half of this note was wrong, and the re-capture is what exposed it.** The viewer's display-transform field reads **`sRGB (ACES)`** in three frames [frame_000, frame_001, frame_002] — direct evidence of an ACES OCIO config, which is exactly the metadata the note said was absent. The original note was written against the 256×144 blind-era captures, where that field is a few illegible pixels; at 1280×720 it is plain text. **A negative finding recorded against unreadable frames is not a finding** — it only records the resolution.

### Tags
grading, channels, color-management, compositing, beginner

---

## Frame verification (2026-09-02)

| | |
|---|---|
| **Corrected** | the Foundry App & Version note claimed **no OCIO metadata was visible**. It is: the viewer reads **`sRGB (ACES)`** in three frames. That note was written against the 256×144 captures this re-grounding replaced. The version itself remains genuinely unknown — no title bar or About dialog anywhere in the set. |
| **Added** | the number the technique turns on — `Copy` **`mix` 0.35** (and 0.065 at an earlier moment), which the entry had described only as "dial it down" [frame_001, frame_002]; the Copy node's full configuration; the supplementary `Grade16` at `gain` **0.2** [frame_001]; the wiring of all three alternative approaches, including that `Keyer1` and `HSVTool1` drive Grades through **mask** inputs while `HueCorrect1` stands alone [frame_004]; the plate name and format; and the two custom menu toolsets, `AlexsTools` and `CompAcademy` [frame_000]. |
| **Confirmed** | the core claim, precisely: `rgba.red` copied into `rgba.green`, at a partial mix, in a backdrop the author labelled **"hue shift by mixing channels"**. And the three tools the entry says are compared — `HueCorrect`, `HSVTool`, `Keyer` — are all present, in that comparison, by name. |
| **Flagged as unverified** | the "set mix to 1 first, then dial down" procedure. Neither captured value is 1, and `mix` **increases** between the two frames (0.065 → 0.35) rather than decreasing. The technique is confirmed; the order of operations described around it is not. |

ℹ️ **`frame_003` (2:40) is a browser, not Nuke** — a colour-matching web app
titled **Color Master** running on `localhost:3000`, with an RGB wheel reading
R 0.64 / G 0.53 / B 0.56 and a `NEXT CHALLENGE` button. It is a teaching aid for
the colour-theory half of the argument (red + less green = orange), and it
grounds the reasoning rather than any Nuke setting.

✅ **This entry is the clearest argument for the re-capture itself.** Its old
frames were 256×144 and were cited nowhere in the notes because they grounded
nothing. The same five moments at 1280×720 produced a working parameter value
(`mix` 0.35), a full node configuration, a wiring diagram for the comparison,
and the correction of a false negative about OCIO. **The moments were never the
problem here; the pixels were.**

---

## Related Tutorials
Shares channel-math grading fundamentals with Nuke Tutorial | Keying with Math Expressions [Intermediate] (`nuke-tutorial-keying-with-math-expressions-intermediate.md`) and Nuke Tutorial | Compositing a Rainbow [Intermediate] (`nuke-tutorial-compositing-a-rainbow-intermediate.md`) — all three build effects from first-principles RGB channel relationships rather than pre-built color tools.
