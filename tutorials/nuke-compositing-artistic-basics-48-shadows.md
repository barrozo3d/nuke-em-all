---
title: Nuke Compositing Artistic Basics (4/8): Shadows
source: YouTube
url: https://www.youtube.com/watch?v=SRgXQPPzVc8
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)"
tags: [relighting, grading, compositing, beginner]
extraction_status: complete
frames_dir: tutorials/frames/nuke-compositing-artistic-basics-48-shadows/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Nuke Compositing Artistic Basics (4/8): Shadows

**Source:** [YouTube](https://www.youtube.com/watch?v=SRgXQPPzVc8)
**Author:** Compositing Academy
**Duration:** 6m55s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] All right, so talking about shadows, I just want to teach you guys quickly about a concept


### Shadow Attenuation [0:07]
**Transcript (timestamped):**
[0:07] called shadow attenuation.
[0:10] So some of you, again, might be familiar with some of these concepts, but I just want to
[0:14] go over it so everyone's kind of on the same page.


### Shadow Attenuation [0:17]
**Transcript (timestamped):**
[0:18] So shadow attenuation is basically the softness of a shadow, and we need to know why a shadow
[0:27] is hard, sharp kind of, or soft.
[0:32] And it's important to know that as a compositor, because if you're compositing a shadow, you
[0:36] don't know how sharp or soft or blurry to make it, and you shouldn't just be guessing,
[0:41] you shouldn't just be blurring it until whatever.
[0:44] You need to think about the physical properties of light.


### Physical Properties of Light [0:46]
**Transcript (timestamped):**
[0:50] So there's two relationships that there's two things to consider when we're thinking
[0:56] about the softness of a shadow, and I'm going to show you guys visually.
[1:00] So the first one is the distance.


### Distance [1:02]
**Transcript (timestamped):**
[1:03] Let me get the draw tool.
[1:09] So the first thing is the distance between our light and the distance between the object
[1:18] in relation to the other object.
[1:20] So in our case, this plane and this ground.
[1:25] So the distance between the two.
[1:29] When the floating object, in this case, it could be a tree or it could be whatever, but
[1:35] the closer it is to the ground, otherwise known as the further away it is from the light,
[1:42] but closer it is to the second object, the sharper the shadow is going to become.
[1:46] So if I just play this, you'll see that as our object gets really close to the ground,
[1:51] it becomes a very dense, dark shadow and also very sharp on the edge.
[1:58] And the reason for this is because of the two angles here, which you're going to see
[2:02] in a moment.
[2:03] So if I bring it close to the ground, you get the sharp shadow.
[2:05] If we bring it up, we see that the shadow starts to become much softer, and it's just
[2:12] the way that the light is bouncing around.
[2:14] So we see that this blue line, there's no light going, the light rays are going straight
[2:21] and they're not going inside or underneath this plane.
[2:27] And the closest angle is out here.
[2:30] So basically the distance between these two lines is called the prenumbra, and this is


### Penumbra [2:33]
**Transcript (timestamped):**
[2:35] the softness of your shadow.
[2:37] So it's the tenuation, the level of softness in the shadow.
[2:42] So all you need to remember is the further away it is and the closer it is to, let's
[2:46] say, the ground, it's going to be sharper.
[2:48] If it's higher up or if it's closer to the light but further away from the second object,
[2:53] it's going to be softer.
[2:56] The other relationship we have is the size of the light itself.
[3:01] So that's the second relationship.
[3:03] What I mean by that is a small light is going to cast sharper shadows.
[3:12] So if we have a bright sunny day, the sun is going to act like a small light.
[3:19] It's going to act like a pinpoint small light.
[3:22] And it's going to have more direct shadows, sharper shadows.
[3:26] But if it's a cloudy day, you're going to have softer shadows because the clouds act
[3:31] as a diffusing material.
[3:34] The light is bouncing around in the clouds and now it's acting like a much bigger light.
[3:38] So let's see what happens.
[3:39] We have a small light.
[3:40] Now let's make it into a bigger light.
[3:45] So if we increase the size of our light, you'll see that our shadow becomes much softer.
[3:54] So we sharp shadow with a really small light and a very soft shadow with a large light.
[3:59] And it's because of the angles here of how the light is bouncing around and also the
[4:03] amount of light that's getting underneath.
[4:05] We can see that since the light is coming from a wider source, it's reaching further
[4:11] under our object.
[4:13] Whereas a small light, the rays aren't reaching underneath just because of where the light
[4:17] is placed and how small it is.
[4:20] So that's shadow attenuation.
[4:24] And something we need to think about, for example, a car wheel is touching the ground.
[4:31] So it's going to be a dense, darker shadow than maybe the back of the car, which is a
[4:35] little bit off of the ground.
[4:38] So those are things we might need to consider when we're compositing a shadow.


### Matching the Blacks [4:45]
**Transcript (timestamped):**
[4:45] Also we need to consider matching the blacks, of course.
[4:48] So I taught this in my Nuke 101 class, but I'm just going to bring it up once again quickly.
[4:55] One of the things we need to consider with the blacks is there's two factors, primarily,
[5:01] to the level of black in an object.
[5:06] The first one is distance from the camera and if there's atmosphere.
[5:10] So we can see further away through the air, light is bouncing around and becoming a bit
[5:16] blue.
[5:17] It's absorbing some of that light.
[5:21] So we're getting a bit of a blue tint further away and a slight blue haze even here.
[5:26] So the darkest thing, if we gain up, is those hills.
[5:30] There's nothing pure black inside.
[5:32] So that's the first consideration.
[5:34] The second consideration we need to think about is light contamination.


### Light Contamination [5:35]
**Transcript (timestamped):**
[5:38] So if there was an orange light up here, some of the blacks of this might become a little
[5:43] bit contaminated orange.
[5:45] So light and atmosphere are the primary effects on the black point.
[5:52] So if we just look at what this does, so what we need to do with each of these is match
[6:01] the black of the sphere to something that's directly near it.
[6:06] So if we just scrub forward, that would be this here.
[6:10] So if we just gamma up, this is the darkest thing near the sphere.
[6:14] So we would say, okay, let's match the black point of this to that.
[6:18] And then we would do the same with this sphere.
[6:20] We would say, okay, let's match the black point of this sphere to there and the last
[6:26] sphere to the hill.
[6:30] And this is what we get.
[6:31] So if we have our non-matching black points, you don't feel the distance and when we match
[6:35] our black points, you can see, so this is not matching and this is matching.
[6:40] So we can see the relationship is kind of better.
[6:46] So those are the things to consider with shadows when we're compositing.
[6:49] And yeah, we can move on from that.



---

## Captured Frames

- [1:51] tutorials/frames/nuke-compositing-artistic-basics-48-shadows/frame_000.jpg
- [2:10] tutorials/frames/nuke-compositing-artistic-basics-48-shadows/frame_001.jpg
- [3:45] tutorials/frames/nuke-compositing-artistic-basics-48-shadows/frame_002.jpg
- [5:26] tutorials/frames/nuke-compositing-artistic-basics-48-shadows/frame_003.jpg
- [6:10] tutorials/frames/nuke-compositing-artistic-basics-48-shadows/frame_004.jpg

---

## Structured Notes

### Core Technique
Part 4 of 8. Two physically-grounded shadow rules for convincing compositing: shadow attenuation (what makes a shadow hard/sharp vs. soft/diffuse) driven by object-to-surface distance and light source size, and black-point matching, driven by atmospheric distance and light contamination.

### Summary
Demonstrated with a live 3D scene (a plane floating above a ground surface, lit by a point light): shadow softness ("shadow attenuation") is governed by two relationships. First, the distance between the casting object and the surface it shadows onto — closer to the surface (or equivalently, farther from the light) produces a denser, sharper-edged shadow; raising the object increases the penumbra (the soft transition band) and produces a much softer shadow, because light rays can wrap further underneath the higher object. Second, the size of the light source itself — a small/pinpoint light (like direct sun on a clear day) casts sharp, hard-edged shadows, while a large/diffused light (like an overcast sky, where clouds scatter and enlarge the effective light source) casts soft shadows, because light reaches further underneath the object from a wider source. Practical compositing implication given: a car wheel touching the ground should read a denser/sharper shadow than the underside of the car body sitting slightly off the ground. Second half covers black-point matching: pure black rarely exists in real footage because of two factors — atmospheric distance (light scattering through air adds a blue haze/tint the further back an object is, lifting its blacks) and light contamination (a nearby colored light bleeding a tint into nearby "black" areas). Practical fix demonstrated in the Nuke node graph: sample the darkest tone in the plate immediately adjacent to each CG element (e.g. a rock/hill near a rendered sphere) and match/gamma each CG element's black point to that locally-sampled reference rather than leaving it at a synthetic pure black — shown side-by-side as a clearly weaker "non-matching" result vs. a convincing "matching" result that reads as properly integrated into the scene's depth.

### Key Steps
1. Understand shadow attenuation rule 1 (distance): the closer a floating/elevated object is to the surface below it, the sharper and denser the cast shadow; the higher/farther the object is from that surface, the softer and more spread the shadow (larger penumbra).
2. Understand shadow attenuation rule 2 (light size): a small/pinpoint light source (direct sun) casts hard, sharp-edged shadows; a large/diffused light source (overcast sky, bounce light) casts soft shadows, because a wider light can send rays further underneath the shadowing object.
3. Apply both rules together when judging or painting a shadow's softness for a CG element — e.g. a car wheel in contact with the ground gets a dense, sharp shadow, while the car's underside further from the ground gets a softer, lighter one.
4. For black-point matching: recognize that real-world blacks are rarely pure black due to (a) atmospheric scattering — objects further from camera pick up a blue-ish haze that lifts their black level, and (b) light contamination — nearby colored light sources tint supposedly-black areas.
5. Sample the darkest tone in the live-action plate immediately adjacent/nearest to each CG element (not a generic scene-wide black point).
6. Grade/gamma each CG element's black point to match that locally-sampled reference value rather than leaving it at a default pure black — repeat per-element if multiple CG objects sit at different depths/distances in the shot.
7. Compare non-matched vs. matched results — matched black points make CG elements read as properly embedded at their correct depth in the scene; unmatched pure blacks break the sense of distance/depth.

### Nodes / Tools / Settings
No single node is the star of this lesson (conceptual/theory-driven), but the node graph shown for black-point matching uses a `Grade`-style gamma/black-point adjustment per CG sphere, driven by a locally-sampled reference color/swatch pulled from the plate next to each element — consistent with a `ColorPicker`/`Grade` gamma workflow referenced from the presenter's prior "Nuke 101" class.

### Difficulty
Beginner — conceptual lesson in physically-based shadow and black-level judgment, prerequisite grounding before grading CG shadows/blacks by eye.

### Foundry App & Version
Nuke — version not stated on screen or in narration. 2020 upload, predates this skill's release-notes backfill (starts at Nuke 13.0/March 2021), so treat as Nuke ~12.x era rather than a specific point release.

### Tags
relighting, grading, compositing, beginner

---

## Related Tutorials
**Nuke Compositing Artistic Basics — 8-part series** (this is Part 4 of 8; all parts cross-link to each other):
- Part 1/8: Roles of Production (`nuke-compositing-artistic-basics-18-roles-of-production.md`)
- Part 2/8: 3 Point Lighting (`nuke-compositing-artistic-basics-28-3-point-lighting.md`)
- Part 3/8: Exposure (`nuke-compositing-artistic-basics-38-exposure.md`)
- Part 5/8: Reflections and Fresnel (`nuke-compositing-artistic-basics-58---reflections-and-fresnel.md`)
- Part 6/8: Whitepoint and white balance (`nuke-compositing-artistic-basics-68-whitepoint-and-white-balance.md`)
- Part 7/8: Glows (`nuke-compositing-artistic-basics-78-glows.md`)
- Part 8/8: Camera Artifacts (`nuke-compositing-artistic-basics-88-camera-artifacts.md`)
