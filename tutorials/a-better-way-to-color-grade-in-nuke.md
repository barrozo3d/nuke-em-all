---
title: A BETTER way to Color Grade in Nuke
source: YouTube
url: https://www.youtube.com/watch?v=fNxqXKuAr4A
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/a-better-way-to-color-grade-in-nuke/
frame_count: 0
frame_status: pending-selection
---

# A BETTER way to Color Grade in Nuke

**Source:** [YouTube](https://www.youtube.com/watch?v=fNxqXKuAr4A)
**Author:** Compositing Academy
**Duration:** 5m18s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py a-better-way-to-color-grade-in-nuke <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Today we're releasing the Hue Qualifier for Nuke. This is the best way to make highly targeted color adjustments directly inside of Nuke.
[0:06] Inspired by DaVinci Resolve's Hue Qualifier, this tool has an intuitive, easy interface.
[0:12] You can move the sliders around and feather to specific ranges.
[0:15] It also allows you to lock the ranges together, so you don't have to adjust each one.
[0:19] Alright, so let's take a look at the Hue Qualifier and how it works and why it's better.
[0:23] So, the reason I wanted to make this tool is because if you ever use the Resolve's Hue Qualifier, it's really visual,
[0:28] it's really easy to adjust things and adjust the ranges together.
[0:31] And right now, in Nuke, the best way to do it, alternatively, would be the HSV tool.
[0:35] But it's not easy to adjust those ranges together and it's not a visual or intuitive interface like this is.
[0:41] So, if we want to select, for example, this mountain, we want to key it, we want to adjust the colors or contrast in that specific area,
[0:47] there's a few ways you could think about doing it.
[0:49] Now, you wouldn't want to use something like a Hue keyer because the blue in the mountain is basically almost the same blue as in the sky.
[0:56] The difference is that the brightness and saturation is a little bit different, but the actual Hue is very similar.
[1:03] And how you can actually know this is if you plug in a color space note and you switch the input from linear to HSL or HSV,
[1:12] we can look at just the Hue by looking at the red channel.
[1:14] And if we do that, we can see the Hue of these two, the mountain and sky are almost the same.
[1:19] So, if we use a Hue keyer, we're not going to be able to separate the mountain from the sky very easily if we try to target some of the blue areas.
[1:26] So, that's why it would be a HSV tool where you could do something similar.
[1:29] But if we look at the HSV tool, all the ranges are these sort of default knobs that are in there and you can't adjust them together.
[1:35] So, let's look at Hue qualifier and we can close this and just select this area.
[1:40] So, just control shift to get an average.
[1:43] We'll click our little thing here and hit apply sample.
[1:46] And this will update the interface automatically so we can see a visual and these can be slid around.
[1:51] So, if we slide this around and we want to expand the lumens range, we could get more of the sky or we could expand the saturation range or adjust where that's being targeted.
[1:59] So, if there's different areas of this sort of blueish tint area, we can kind of slide this around.
[2:05] Another way to do it is if we wanted to just get the mountain, we could select the range.
[2:09] So, we do control shift, we'll hit apply sample again.
[2:13] We can get our initial alpha here and we can expand the range.
[2:16] So, we could go to add the range and then we could just select another color sample like this and say apply sample.
[2:22] And this will automatically adjust the range to apply that additional selection that we've added.
[2:27] So, that is a good way to do it without trying to figure out which one of these you need to adjust.
[2:31] So, it's good to have both but it's really nice to have the ability to add different samples of color.
[2:37] And the last thing here is that we can expand these keys together.
[2:40] So, because we're keying the Hue saturation and lumens at the same time,
[2:45] sometimes you want to adjust that together.
[2:47] So, these are locking the ranges here which can give you a really nice blend on your alphas to get a very specific color key.
[2:54] Now, one more cool feature that this has, it's important to note is if you have a very bright scene where the values are going way above one.
[3:00] So, I'll take this image here and I'll just kind of push the values up.
[3:04] If you want the Hue qualifier to basically see that range, it has a little button here that says analyze input.
[3:10] And it will actually, if we press this button, it will actually switch to HDR mode and this will actually adapt to the range that your image actually has.
[3:19] So, anything above this little line here is above one and so we can still target different ranges here by pulling this around and selecting that range.
[3:28] It's still going to detect things above one correctly and so this is just a nice button.
[3:33] So, you see SDR mode and HDR mode.
[3:36] Most of the time you don't need to switch this manually but if you want to set some of the luminous max manually,
[3:40] you can but most of the time you just press analyze input and it will work for you.
[3:45] Now, the important part to just reiterate here is when you're selecting a color, you're selecting not just a color but the brightness of that color or the saturation of this color.
[3:54] So, these three reds are all technically red but you can see if we wanted to target one of these individually or we wanted to expand the range to having all of them,
[4:03] this is really what the Hue qualifier is meant for.
[4:06] So, here's another quick example of just a scene where you might want to use a Hue qualifier.
[4:10] So, I wanted to basically take the scene and maybe if we want to make it a little bit more cool, we want to remove some of the yellow greens in here but keep some of the cooler greens.
[4:20] What we can do is we can just do a Hue qualifier and target the sort of yellow greens.
[4:24] Now, this image is not 444 so you're going to see some a little bit of compression and you're going to see some blockiness.
[4:30] That's not because of the tool, it's because of the image that we're giving it.
[4:33] Whereas the other image I was looking at was from a ProRes raw video.
[4:37] But anyways, we can still use it.
[4:39] You can actually get a good map from the still by just blurring it a little bit.
[4:42] So, we'll select those kind of yellow greens and then we can just blur that map that's coming out and then we can just take some of the yellow greens out.
[4:49] So, if I want to make it feel like those purple flowers are continuing, maybe we get a little bit of a cooler scene and that gives us like a nice effect that we can still keep the greens.
[4:59] We're not just saying take out the green, we're taking out the yellow greens out of the field here just to get a little bit more of a cinematic look.
[5:07] So, that's pretty much it for this tool.
[5:09] You can download it for free in the description below if you have Nuke Indy or Nuke Commercial.
[5:13] It'll work for you and that's pretty much it.
[5:16] Make sure to hit thumbs up if you like the video.



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
