---
title: Nuke Compositing Artistic Basics (5/8) - Reflections and Fresnel
source: YouTube
url: https://www.youtube.com/watch?v=YeGZP5xlBGg
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke (theory-focused; real-world reference footage viewed in Nuke's viewer, no node-graph build)"
version: "not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)"
tags: [relighting, digital-matte-painting, beginner]
extraction_status: complete
frames_dir: tutorials/frames/nuke-compositing-artistic-basics-58---reflections-and-fresnel/
frame_count: 4
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Nuke Compositing Artistic Basics (5/8) - Reflections and Fresnel

**Source:** [YouTube](https://www.youtube.com/watch?v=YeGZP5xlBGg)
**Author:** Compositing Academy
**Duration:** 4m57s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Okay, so one thing about reflection I just wanted to discuss about is the concept of the
[0:08] for now effect.
[0:10] And this effect is important when we're compositing because we need to know how reflective things
[0:15] need to be if we're compositing different things.
[0:18] So let me just write it out.
[0:20] It's spelt like this.
[0:23] It's spelt like that, but it's actually pronounced for now.
[0:29] And this effect is, I can show it pretty simply, I've actually taken video here of
[0:34] a puddle near where we composited our car.
[0:37] And if you notice the reflection is almost white here.
[0:41] It's very, very reflective.
[0:43] So what you need to know about the for now effect is that if you're at more of a glancing
[0:48] angle to a reflective surface, it's going to appear more reflective than if you're looking
[0:54] at it straight on.
[0:57] So if you're looking at this puddle, it's very, very reflective.
[0:59] It's almost white.
[1:00] However, if we were looking straight down at it, it would be almost not reflective.
[1:04] It would be a dark reflection.
[1:06] If you don't believe me, I did walk forward here and you'll see that the reflection reduces
[1:12] as we look straight down at it.
[1:15] So the more of a glancing angle and the lower we are to that reflection, the more reflective
[1:21] it becomes.
[1:23] And this is the same for the side of a car surface.
[1:26] If we're looking straight at a car and it might be a little bit less reflective than
[1:32] if we're looking at it from, let's say, standing behind the car and looking at the side of
[1:36] a car.
[1:38] So that's something you need to understand about reflections.
[1:41] So if you watch here, you see it's a little bit darker.
[1:43] There's less reflection.
[1:45] And as we lower the camera, it becomes more reflective.
[1:52] And you can Google, you know, there's all physics diagrams and all kinds of stuff you
[1:55] can Google.
[1:56] If you Google the Fresnel effect, there's like an entire 20-minute video explaining this
[2:02] effect.
[2:03] But that's pretty much all you need to really understand to composite.
[2:06] It's just that more of a glancing angle, stronger reflection.
[2:12] The other concept you need to understand is specular versus reflection.
[2:15] So if you've done CG, you already understand this.
[2:19] But some people here have no CG background, which is fine.
[2:22] I know a lot of composers actually who don't know how to do any 3D modeling or anything
[2:26] like that.
[2:27] You don't necessarily have to.
[2:29] I think it's a good supplement and I actually do those things on my free time.
[2:33] But it's not a requirement.
[2:36] But I would recommend learning a little bit of 3D and some basic lighting and stuff like
[2:41] that.
[2:42] But I just want to explain a very simple concept in lighting that is specular versus reflection.
[2:48] So in this puddle, all these little white things we're talking about, that is all just
[2:56] one reflection.
[2:57] In the real world, there's only reflection.
[2:59] There's no specular and reflection.
[3:02] But in CG world, we do separate those terms.
[3:05] We say, oh, look at the specular and look at the reflection.
[3:09] Specular would be these brighter ripples that you see.
[3:14] So there's some specular highlights.
[3:16] So it's basically just little highlights on the reflection.
[3:19] That's what a specular reflection is.
[3:20] So we can see those little highlights.
[3:23] And then the broader reflection would just be the normal reflection.
[3:27] So if we're saying, hey, we want to increase the spec, which is the short for specular,
[3:32] we want to increase the spec in this area.
[3:35] We want to increase the specular in this area.
[3:36] It just means bring up the little details, the little white highlights in the reflection.
[3:44] So that's spec and reflection.
[3:48] And a little bit about the Fresnel effect.
[3:51] Again, you can see the Fresnel effect here, just with the footage of waves.
[3:57] So some of these, some of this is shadow, but it's also the fact that the surface of
[4:04] the wave here is facing us, but then the top of the wave is facing, it's more flat.
[4:11] It's more at a glancing angle.
[4:12] It's more reflective than the front of the surface.
[4:15] And that's just the reflection.
[4:17] There might be a bit of shadow.
[4:18] It's hard to know exactly what this, but more likely than not, it's actually just the Fresnel
[4:24] effect.
[4:25] That's why you see these darker areas and the brighter areas.
[4:29] So we're going to have to deal with that on our car, because we have windows facing in
[4:33] different directions.
[4:37] So I filmed this puddle standing outside like a weird person for you guys.
[4:41] You guys got to appreciate that.
[4:43] And these are from Wellington, New Zealand.
[4:48] So that's where I'm making this project.
[4:51] So we can move on to the next project, next lecture here.



---

## Captured Frames

- [0:40] tutorials/frames/nuke-compositing-artistic-basics-58---reflections-and-fresnel/frame_000.jpg
- [1:03] tutorials/frames/nuke-compositing-artistic-basics-58---reflections-and-fresnel/frame_001.jpg
- [3:16] tutorials/frames/nuke-compositing-artistic-basics-58---reflections-and-fresnel/frame_002.jpg
- [3:53] tutorials/frames/nuke-compositing-artistic-basics-58---reflections-and-fresnel/frame_003.jpg

---

## Structured Notes

### Core Technique
Part 5 of 8. Explains the Fresnel effect (glancing-angle surfaces reflect more strongly than surfaces viewed straight-on) and the CG-specific distinction between "specular" and "reflection," both needed to judge how reflective a composited surface (car body, windows, puddles) should look from a given camera angle.

### Summary
Illustrated with real reference footage of a puddle and ocean waves filmed by the presenter (not a Nuke node build — a theory lesson viewed in Nuke's viewer). The Fresnel effect: a reflective surface viewed at a glancing/grazing angle (camera low, looking across the surface) appears much more reflective — the puddle looks almost white/mirror-like — while the same surface viewed straight-on/from directly above appears far less reflective, closer to its base dark color; demonstrated live by the presenter walking toward the puddle and watching the reflection weaken as the viewing angle steepens. The same principle applies to a car's painted surfaces and, notably, its windows, which face different directions and therefore need different reflectivity treatment depending on their angle to camera. Second concept: in the real world there's only one physical phenomenon (reflection), but CG workflows conventionally split it into "specular" (the small, bright highlight glints riding on top of a reflective surface, e.g. the little white ripples catching light on the puddle) versus the broader base "reflection" itself — compositing notes like "bring up the spec" specifically mean boosting those small highlight details, not the overall reflection. Fresnel is also shown driving the varied light/dark banding seen across ocean wave surfaces, since each wave facet sits at a different angle relative to camera.

### Key Steps
1. Recognize the Fresnel effect rule: the more glancing/grazing the viewing angle to a reflective surface (camera low, looking across it), the stronger/brighter the reflection appears; viewed straight-on/from above, the same surface reflects far less and reads closer to its base color.
2. Apply this when compositing reflective CG or real elements at different camera angles in the same shot — e.g. a car's side panels and windows will each need a different reflectivity treatment depending on their individual angle relative to camera, not one uniform reflection value.
3. Distinguish "specular" from "reflection" in CG-authoring/note-giving vocabulary: specular = the small, bright highlight glints/ripples sitting on top of a reflective surface; reflection = the broader base mirror-like image itself. In reality both are the same physical phenomenon, but CG pipelines and comp notes treat them separately (e.g. "bring up the spec" = boost just the small highlights).
4. Recognize Fresnel-driven banding on complex reflective surfaces like ocean waves: different facets of the same surface sit at different angles to camera, producing visibly brighter (glancing-angle) and darker (straight-on) bands even without added shadow.

### Nodes / Tools / Settings
None — pure optical-theory lesson illustrated with real-world reference footage (puddle, ocean waves) viewed directly in Nuke's viewer; no node graph built in this segment.

### Difficulty
Beginner — conceptual lesson in reflection/Fresnel judgment, useful before grading reflectivity or specular passes on CG/composited surfaces.

### Foundry App & Version
Nuke — version not stated on screen or in narration. 2020 upload, predates this skill's release-notes backfill (starts at Nuke 13.0/March 2021), so treat as Nuke ~12.x era rather than a specific point release.

### Tags
relighting, digital-matte-painting, beginner

---

## Related Tutorials
**Nuke Compositing Artistic Basics — 8-part series** (this is Part 5 of 8; all parts cross-link to each other):
- Part 1/8: Roles of Production (`nuke-compositing-artistic-basics-18-roles-of-production.md`)
- Part 2/8: 3 Point Lighting (`nuke-compositing-artistic-basics-28-3-point-lighting.md`)
- Part 3/8: Exposure (`nuke-compositing-artistic-basics-38-exposure.md`)
- Part 4/8: Shadows (`nuke-compositing-artistic-basics-48-shadows.md`)
- Part 6/8: Whitepoint and white balance (`nuke-compositing-artistic-basics-68-whitepoint-and-white-balance.md`)
- Part 7/8: Glows (`nuke-compositing-artistic-basics-78-glows.md`)
- Part 8/8: Camera Artifacts (`nuke-compositing-artistic-basics-88-camera-artifacts.md`)
