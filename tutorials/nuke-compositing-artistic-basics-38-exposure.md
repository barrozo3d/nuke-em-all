---
title: Nuke Compositing Artistic Basics (3/8): Exposure
source: YouTube
url: https://www.youtube.com/watch?v=xFUOuK3lFro
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke (theory-focused; brief node-graph glimpses of over/underexposed and HDR tone-mapped comparisons)"
version: "not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)"
tags: [grading, digital-matte-painting, beginner]
extraction_status: complete
frames_dir: tutorials/frames/nuke-compositing-artistic-basics-38-exposure/
frame_count: 4
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Nuke Compositing Artistic Basics (3/8): Exposure

**Source:** [YouTube](https://www.youtube.com/watch?v=xFUOuK3lFro)
**Author:** Compositing Academy
**Duration:** 3m32s | 3 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Exposure, Camera Exposure, Light and Shadow
[0:08] This is important because if we break these rules too far, our CG is going to look fake.


### Camera Exposure [0:10]
**Transcript (timestamped):**
[0:15] So we need to understand a very basic understanding of camera exposure and the rules we can put, the bounds that we're playing in this game here.
[0:28] So if we have our footage here, this is an example of overexposed.
[0:33] So if I just increase exposure, you guys know what an overexposed photo looks like.
[0:38] The highlights are getting blown out and you're losing all of the detail in the highlights.
[0:44] But we're also seeing more detail in the shadows.
[0:47] We have a normal exposure and then we have an underexposed shot.
[0:52] So you see we have more detail in the highlights, but we're obviously losing some of the lower end and it's a bit darker overall.


### HDR [1:00]
**Transcript (timestamped):**
[1:01] So you've probably heard or you may have heard the term HDR or High Dynamic Range.
[1:07] And what that looks like is basically you're taking the two and you're compositing them together essentially.
[1:17] So if we take a look at what that looks like, let's use a different picture as an example actually.
[1:23] So we have our normal picture, we have our overexposed picture.
[1:28] You see in our normal picture we have all the detail in the sky, but all the trees are pretty dark.
[1:34] But if we overexpose our picture, we have all the detail in the trees.
[1:39] An HDR photo is essentially taking multiple exposures and combining them together, usually three exposures.
[1:47] But this is what the HDR version looks like.
[1:51] So here's the normal and here's the HDR version.
[1:54] So it's not realistic, it looks aesthetic in some ways and sometimes in photography we're doing HDR photography on purpose.
[2:04] But usually when you're dealing with film and trying to make something look real, we don't want to do this.
[2:10] We don't want to see all the detail in the shadows and the highlights at the same time.
[2:15] Because that's just not how the camera works when we're filming video.
[2:21] A video doesn't film HDR video, so you have to either be in a normal exposure or overexposed or underexposed.
[2:30] You're not going to have all three at the same time.
[2:33] So if you grade your CG to have all the detail in the shadows, even though it's there, it's going to look fake.
[2:40] So that's why I'm kind of teaching you guys this, just quickly going over it.
[2:43] Because if you don't understand the relationship between highlights and shadow, I can show you the grade node, but you don't know what you're doing.
[2:50] You're going to grade it the wrong way in a physically inaccurate way.
[2:55] So again, relationship is broken between the highlights and shadows and we want to avoid trying to make our CG not look HDR, basically.
[3:08] This is really common if you see newer people doing matte paintings or sky replacements.
[3:15] If it's a bright day, you might not see all the detail in the clouds.
[3:19] It depends on the lighting, of course, but it's just all good things to note.
[3:24] So that's just a quick overview of exposure and a couple things to keep in mind.
[3:29] Yeah, so let's move on.



---

## Captured Frames

- [0:33] tutorials/frames/nuke-compositing-artistic-basics-38-exposure/frame_000.jpg
- [0:47] tutorials/frames/nuke-compositing-artistic-basics-38-exposure/frame_001.jpg
- [1:28] tutorials/frames/nuke-compositing-artistic-basics-38-exposure/frame_002.jpg
- [1:51] tutorials/frames/nuke-compositing-artistic-basics-38-exposure/frame_003.jpg

---

## Structured Notes

### Core Technique
Part 3 of 8. Explains why a single real camera exposure can never show full highlight *and* full shadow detail simultaneously, and why grading CG to look "HDR" (detail everywhere at once) is the most common tell that gives away a fake/matte-painted shot.

### Summary
Compares over-exposed (blown highlights, more shadow detail), normal, and under-exposed (crushed shadows, more highlight detail) versions of the same footage side by side in the Nuke node graph (backdrops labeled "Over-exposed / Detail in highlights lost" and similar). Explains HDR photography as literally compositing multiple bracketed exposures together to reveal detail in both shadows and highlights simultaneously — demonstrated with a landscape example where the normal exposure has full sky detail but dark trees, the overexposed version has bright/detailed trees but a blown sky, and the HDR merge shows both at once, which reads as distinctly "not realistic," an aesthetic photography technique rather than how a real video camera captures a single frame. Since video never captures HDR in-camera (a shot is always in one exposure state at a time — normal, over, or under), grading CG to preserve full detail in both shadows and highlights simultaneously breaks that physical relationship and immediately reads as fake — flagged as a very common mistake in beginner matte paintings and sky replacements (e.g. showing full cloud detail on a bright day when the real exposure wouldn't retain it).

### Key Steps
1. Understand the three exposure states a real camera/shot exists in at any moment: normal, overexposed (blown highlights, more shadow detail visible), or underexposed (crushed shadows, more highlight detail visible) — never all three/full range at once in a single video frame.
2. Understand HDR as a compositing technique (typically merging ~3 bracketed exposures) that reveals detail in both shadows and highlights simultaneously — recognizably "not realistic" for video, even though used intentionally in still photography.
3. When grading CG or matte-painting a sky/environment to integrate with a plate, deliberately preserve the same broken highlight/shadow relationship the real footage's exposure has — don't let CG elements retain full detail in areas that would be blown or crushed in the real camera's actual exposure state.
4. Watch specifically for this mistake in matte paintings and sky replacements: a bright-day sky replacement showing full, crisp cloud detail everywhere is a common beginner tell that the exposure relationship wasn't respected.

### Nodes / Tools / Settings
No specific node techniques taught (conceptual lesson); brief node-graph glimpses show labeled backdrop groups comparing "Over-exposed / Detail in highlights lost" vs. normal vs. an "HDR Tone-mapped" merge result, illustrating the concept rather than teaching a build.

### Difficulty
Beginner — conceptual grading/exposure primer, prerequisite understanding before using the Grade node meaningfully (explicitly stated: "I can show you the grade node, but you don't know what you're doing" without this foundation).

### Foundry App & Version
Nuke — version not stated on screen or in narration. 2020 upload, predates this skill's release-notes backfill (starts at Nuke 13.0/March 2021), so treat as Nuke ~12.x era rather than a specific point release.

### Tags
grading, digital-matte-painting, beginner

---

## Related Tutorials
**Nuke Compositing Artistic Basics — 8-part series** (this is Part 3 of 8; all parts cross-link to each other):
- Part 1/8: Roles of Production (`nuke-compositing-artistic-basics-18-roles-of-production.md`)
- Part 2/8: 3 Point Lighting (`nuke-compositing-artistic-basics-28-3-point-lighting.md`)
- Part 4/8: Shadows (`nuke-compositing-artistic-basics-48-shadows.md`)
- Part 5/8: Reflections and Fresnel (`nuke-compositing-artistic-basics-58---reflections-and-fresnel.md`)
- Part 6/8: Whitepoint and white balance (`nuke-compositing-artistic-basics-68-whitepoint-and-white-balance.md`)
- Part 7/8: Glows (`nuke-compositing-artistic-basics-78-glows.md`)
- Part 8/8: Camera Artifacts (`nuke-compositing-artistic-basics-88-camera-artifacts.md`)
