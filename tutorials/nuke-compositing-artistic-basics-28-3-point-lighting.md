---
title: Nuke Compositing Artistic Basics (2/8): 3 Point Lighting
source: YouTube
url: https://www.youtube.com/watch?v=EdYZwn8Kwv4
author: Compositing Academy
ingested: 2026-08-14
app: "Cross-app theory (no software shown — lighting terminology used throughout the presenter's Nuke compositing vocabulary)"
version: "not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021)"
tags: [relighting, grading, beginner]
extraction_status: complete
frames_dir: tutorials/frames/nuke-compositing-artistic-basics-28-3-point-lighting/
frame_count: 3
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Nuke Compositing Artistic Basics (2/8): 3 Point Lighting

**Source:** [YouTube](https://www.youtube.com/watch?v=EdYZwn8Kwv4)
**Author:** Compositing Academy
**Duration:** 2m49s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] This is going to be a quick overview of the concept of 3-point lighting.
[0:05] If you come from a photography background or lighting background, this is going to be very simple for you, and you can almost skip it.
[0:11] I'm just going to quickly explain it for those who are not familiar with basic 3-point light setup, because I'm going to be using these terms while I'm compositing CG.
[0:22] These are the terms. 3-point lighting is just kind of a standard lighting setup that people use, that typically looks pretty good, but it's also, it refers to the main light sources in a scene.
[0:36] So if we have three main light sources, this is kind of what the standard lighting setup would look like.
[0:43] And our brightest front-facing light source would be our key light, so this big blue light on the front of this ball.
[0:50] We have a fill light, which is our kind of secondary shadow-filling lighting.
[0:58] This could also be light that's bouncing off of the ground, so it doesn't necessarily have to be a light.
[1:04] For example, if the key light is a sun and there's a gravel ground underneath, some of the light will bounce off the gravel and create a fill.
[1:14] So if we're talking about fill light, we might not actually be talking about light, but rather just the fill, the light filling the shadows.
[1:20] And then we also have a rim light, which is just a light that's usually behind the surface, and it creates a little bit of a highlight, and silhouettes are object, and usually looks pretty good.
[1:30] So if you guys take a second, open up Google Images and type in 3-point lighting, you're going to see really good examples of photography, 3-point lighting.
[1:40] I can't use a lot of those pictures here because they are copyright, but just take Google Images, 3-point lighting, check it out.
[1:46] But this is, for example, if we take down the fill light, you'll see that we see a lot more shadow.
[1:55] So if I'm talking in the composite and say, okay, there's too much fill light in this area, that's what I'm talking about.
[2:03] Or if I'm saying let's bring up the key, if you hear me say the term, let's bring up the key or bring up the key light, that's what we're talking about.
[2:11] We're talking about the main light, which is usually direct light source, like I said.
[2:16] And then we also have the secondary light, fill light, just going through these captions I made.
[2:22] Sometimes they're different colors. You can see I made this one blue and kind of red, just to add some color contrast, which adds a little bit of interest.
[2:30] It really depends on the scene, depends what's being filmed if we're trying to create a mood or something.
[2:36] And then our rim light, so it's kind of what I just said.
[2:40] So that's really just a basic 3-point lighting. So if you hear me say those terms, that is what we're talking about.



---

## Captured Frames

- [0:43] tutorials/frames/nuke-compositing-artistic-basics-28-3-point-lighting/frame_000.jpg
- [1:20] tutorials/frames/nuke-compositing-artistic-basics-28-3-point-lighting/frame_001.jpg
- [1:46] tutorials/frames/nuke-compositing-artistic-basics-28-3-point-lighting/frame_002.jpg

---

## Structured Notes

### Core Technique
Part 2 of 8. Defines the standard photography/CG "3-point lighting" vocabulary (key, fill, rim) that the presenter uses throughout the series when giving grading/compositing notes like "bring up the key" or "there's too much fill light."

### Summary
No software shown — a labeled 3D-viewport diagram of a sphere lit by three lights. Key light is the brightest, front-facing main light source; fill light is the secondary light that softens/fills shadows cast by the key (and doesn't have to be an actual light — it can be indirect bounce, e.g. sunlight bouncing off gravel ground); rim light sits behind the subject, creating a thin highlight/silhouette edge. The demo sphere uses a blue key and reddish fill for color contrast (illustrating how colored 3-point setups can add mood). Reducing the fill light visibly deepens shadow contrast — establishing the vocabulary ("bring up the key," "too much fill") the presenter uses in later grading/compositing discussions throughout the series.

### Key Steps
1. Identify the key light: the brightest, primary front-facing light source in a scene — usually a direct light like a sun or a practical.
2. Identify the fill light: a secondary, dimmer light that fills in shadows cast by the key; can be an actual light or simply ambient/bounce light off nearby surfaces (e.g. sunlight reflecting off gravel).
3. Identify the rim light: positioned behind the subject, creating a thin edge highlight that separates/silhouettes the subject from its background.
4. Use color contrast between key and fill (e.g. cool key + warm fill, or vice versa) as a mood/interest tool depending on the scene.
5. Recognize the practical effect of adjusting each: reducing fill deepens/darkens shadows; raising key brightens the main light read — vocabulary used directly when giving or receiving compositing/grading notes.

### Nodes / Tools / Settings
None — pure lighting-terminology theory illustrated with a labeled 3D diagram (no Nuke UI).

### Difficulty
Beginner — conceptual primer; skippable for anyone with a photography/lighting background per the presenter's own framing.

### Foundry App & Version
Not applicable — no app shown on screen; standard lighting terminology used across any comp/lighting/photography context. 2020 upload, predates this skill's release-notes backfill (starts at Nuke 13.0/March 2021).

### Tags
relighting, grading, beginner

---

## Related Tutorials
**Nuke Compositing Artistic Basics — 8-part series** (this is Part 2 of 8; all parts cross-link to each other):
- Part 1/8: Roles of Production (`nuke-compositing-artistic-basics-18-roles-of-production.md`)
- Part 3/8: Exposure (`nuke-compositing-artistic-basics-38-exposure.md`)
- Part 4/8: Shadows (`nuke-compositing-artistic-basics-48-shadows.md`)
- Part 5/8: Reflections and Fresnel (`nuke-compositing-artistic-basics-58---reflections-and-fresnel.md`)
- Part 6/8: Whitepoint and white balance (`nuke-compositing-artistic-basics-68-whitepoint-and-white-balance.md`)
- Part 7/8: Glows (`nuke-compositing-artistic-basics-78-glows.md`)
- Part 8/8: Camera Artifacts (`nuke-compositing-artistic-basics-88-camera-artifacts.md`)
