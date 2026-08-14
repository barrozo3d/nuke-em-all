---
title: Nuke Compositing Artistic Basics (8/8): Camera Artifacts
source: YouTube
url: https://www.youtube.com/watch?v=bmwOCLwiYM0
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke (theory-focused; real reference footage inspected in Nuke's viewer, chromatic-aberration/bokeh matching workflow set up for later lessons)"
version: "not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)"
tags: [compositing, defocus, digital-matte-painting, beginner]
extraction_status: complete
frames_dir: tutorials/frames/nuke-compositing-artistic-basics-88-camera-artifacts/
frame_count: 4
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Nuke Compositing Artistic Basics (8/8): Camera Artifacts

**Source:** [YouTube](https://www.youtube.com/watch?v=bmwOCLwiYM0)
**Author:** Compositing Academy
**Duration:** 5m28s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- WARNING: Very short transcript (37 chars) in 'Intro'

---

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Camera Artifacts
[0:34] Chromatic Aberration


### Chromatic Aberration [0:45]
**Transcript (timestamped):**
[0:56] Chromatic Aberration is the bending of light in a lens in an imperfect way.
[1:03] Some of the light is coming through the lens at an angle that is starting to distort the color a little bit.
[1:11] What that does if we look close, if we look at highlights, and this is filmed through a Sony Zeiss lens,
[1:20] so more expensive lenses have less chromatic aberration, but you'll still see some of that chromatic aberration.
[1:28] Sometimes directors will film intentionally to get that effect because they like that effect.
[1:35] If we look at what chromatic aberration is, if we see these white highlights over here, if we look just on the edge,
[1:41] we see that there's a little bit of green fringe around the edge, and that's chromatic aberration.
[1:48] It's the splitting of light coming through the lens, so the rays of light are not perfectly parallel.
[1:54] I know that it's a white light, but the edges are a little bit of chromatic aberration.
[2:01] That can happen, and it can happen with different colors as well.
[2:05] Sometimes you can have a little bit of purple on the edge, sometimes you can have a little bit of red and blue.
[2:11] That's something you need to zoom in and you look around, you look at your edges and you say,
[2:16] I don't see any edges that have chromatic aberration when I'm putting my CG in and can I match that?
[2:24] That is something to think about. Let me actually grab the main footage because the real plate that we're using is this one.
[2:34] This one has really clear chromatic aberration on it.
[2:38] You can see here's the green around the edge, but if we look up here, here it is again.
[2:44] The bright green on the edge, we actually see some purple, a little bit of purple on some of these edges.
[2:50] So green and purple are showing up in this footage.
[2:53] We're going to actually learn how to match that chromatic aberration, that lens distortion that's happening.
[3:02] It's not lens distortion, but that's something to think about.
[3:06] You see that blue edge, cyan looking edge on the edges here.
[3:11] That's chromatic aberration.
[3:13] The other thing we need to think about is camera defocus.


### Camera Defocus [3:15]
**Transcript (timestamped):**
[3:16] If something is out of focus, it's a bit blurry.
[3:19] This is a pretty simple one. It's kind of self-explanatory.
[3:23] If we look at our plate here and we look at this ground, we see all the edges are pretty sharp.
[3:28] There's not a lot of blurring happening.
[3:30] If we look further away, we can see our rocks are a bit out of focus. They're a bit blurry.
[3:36] So for adding something CG, we need to consider where it is in space and if it's out of focus or if it's in focus.
[3:43] Sometimes it can be in and out of focus at the same time.
[3:46] So we're going to learn about depth of field once we get to the defocusing lecture
[3:51] and how to fade things in and out of focus based on the depth from the real camera.
[3:56] So we're going to learn about that.


### Bokeh [4:00]
**Transcript (timestamped):**
[4:00] Then we also have kind of an effect that's happening.
[4:07] These little out of focus dots, there is an actual term for them and they're called bokeh.
[4:14] It's spelled like this. It looks like it's spelled bokeh, but it's actually pronounced bokeh.
[4:20] So we're going to be learning how to create those and when we place something out of focus, how to make it have that bokeh effect.
[4:33] So I actually took a picture of just the light.
[4:36] So this is with the same camera, just with a little something on the floor and really, really out of focus.
[4:44] And you see that's a bokeh being created.
[4:48] It's kind of the way the light is coming through the lens.
[4:53] Different lenses will produce different bokehs.
[4:56] So you can actually Google images, type in bokeh, B-O-K-E-H.
[5:02] And you're going to see all kinds of different bokeh effects and you'll see a lot in photography because it's really artistic.
[5:08] And you can actually use it in a way that is really aesthetic if you do it the right way.
[5:14] So that's pretty much it.
[5:16] And also the other one we have a little bit that we might talk about is Glint.
[5:21] But this one actually might belong more in the next lesson.
[5:24] So we'll go on to that next.



---

## Captured Frames

- [1:41] tutorials/frames/nuke-compositing-artistic-basics-88-camera-artifacts/frame_000.jpg
- [2:38] tutorials/frames/nuke-compositing-artistic-basics-88-camera-artifacts/frame_001.jpg
- [3:28] tutorials/frames/nuke-compositing-artistic-basics-88-camera-artifacts/frame_002.jpg
- [4:44] tutorials/frames/nuke-compositing-artistic-basics-88-camera-artifacts/frame_003.jpg

---

## Structured Notes

### Core Technique
Part 8 of 8 (series finale). Introduces three lens/camera artifacts a compositor must observe in the real plate and later replicate on CG/added elements to sell integration: chromatic aberration, defocus, and bokeh.

### Summary
Chromatic aberration is explained as the imperfect bending/splitting of light through a lens, most visible as colored fringing (commonly green and/or purple/cyan) around the edges of bright highlights — demonstrated on footage shot with a Sony Zeiss lens, and more clearly on the actual production plate being used for the class's car shot, where green and purple fringing is clearly visible around highlight edges. Framed as something more expensive lenses reduce but rarely eliminate entirely, and something directors sometimes intentionally amplify for stylistic effect; the compositor's job is to inspect the plate's edges closely and match that same fringing on any inserted CG elements. Camera defocus is covered briefly as the self-explanatory blur applied to out-of-focus regions, illustrated by comparing sharp near-ground detail against progressively blurrier distant rocks in the plate — flagged as requiring a fuller depth-of-field lesson later in the course to fade CG elements in/out of focus based on their distance from the real camera. Bokeh is introduced as the specific out-of-focus highlight-dot pattern created by a lens, demonstrated with reference footage of an extremely defocused light source; different lenses produce visibly different bokeh shapes/characters, and the presenter points to Google Images searches as a fast way to study varied real-world bokeh looks before attempting to fake it on CG lights. Briefly mentions "glint" as a related artifact that will actually be covered in the next (separate, non-series) lesson rather than here.

### Key Steps
1. Inspect the real plate closely (zoomed in on bright highlight edges) to identify whether chromatic aberration is present, and what colors it fringes toward (commonly green and purple/cyan, sometimes red/blue) — sample directly from the actual production plate being matched, not a generic assumption.
2. When adding CG or other inserted elements, match that same chromatic-aberration fringing on their highlight edges so they don't read as artificially "clean" compared to the real footage.
3. Assess camera defocus/depth of field in the plate by comparing sharpness across depth — near/ground-level detail typically stays sharp while distant elements (background rocks, etc.) go progressively softer — noting this requires a full depth-of-field treatment (covered in a separate future lesson) to correctly fade CG elements in and out of focus based on their distance from the real tracked camera.
4. Recognize bokeh as the specific shape/character of out-of-focus highlight points produced by a given lens (demonstrated via extremely defocused reference footage of a light source) — different lenses yield visibly different bokeh shapes, so reference real bokeh examples (e.g. via image search) before replicating it on CG light sources.
5. Note "glint" as a related but separate artifact deferred to the next lesson outside this 8-part series.

### Nodes / Tools / Settings
None built in this segment — theory/observation lesson using real reference footage viewed in Nuke's viewer (including a color-sample circle used to isolate/inspect a specific fringe color on a highlight edge), setting up techniques (chromatic aberration matching, defocus/depth-of-field, bokeh creation) that are built out in later, non-series lessons.

### Difficulty
Beginner — observational/diagnostic lesson training the eye to spot lens artifacts in a plate before attempting to replicate them; the actual node-based techniques for each are deferred to dedicated future lessons.

### Foundry App & Version
Nuke — version not stated on screen or in narration. 2020 upload, predates this skill's release-notes backfill (starts at Nuke 13.0/March 2021), so treat as Nuke ~12.x era rather than a specific point release.

### Tags
compositing, defocus, digital-matte-painting, beginner

---

## Related Tutorials
**Nuke Compositing Artistic Basics — 8-part series** (this is Part 8 of 8, the series finale; all parts cross-link to each other):
- Part 1/8: Roles of Production (`nuke-compositing-artistic-basics-18-roles-of-production.md`)
- Part 2/8: 3 Point Lighting (`nuke-compositing-artistic-basics-28-3-point-lighting.md`)
- Part 3/8: Exposure (`nuke-compositing-artistic-basics-38-exposure.md`)
- Part 4/8: Shadows (`nuke-compositing-artistic-basics-48-shadows.md`)
- Part 5/8: Reflections and Fresnel (`nuke-compositing-artistic-basics-58---reflections-and-fresnel.md`)
- Part 6/8: Whitepoint and white balance (`nuke-compositing-artistic-basics-68-whitepoint-and-white-balance.md`)
- Part 7/8: Glows (`nuke-compositing-artistic-basics-78-glows.md`)
- Skill Up with Nuke | How To Think Like A Pro Compositor (`skill-up-with-nuke-how-to-think-like-a-pro-compositor.md`) — shares `defocus`; that video's CG-to-plate matching also covers focus-matching via an inverted defocus control mask.
