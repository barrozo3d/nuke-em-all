---
title: 2 Expert VFX Tips to PERFECTLY Blend CG
source: YouTube
url: https://www.youtube.com/watch?v=DFb9dnOWTxw
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "not specified"
tags: [relighting, grading, roto, compositing, digital-matte-painting, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/2-expert-vfx-tips-to-perfectly-blend-cg/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# 2 Expert VFX Tips to PERFECTLY Blend CG

**Source:** [YouTube](https://www.youtube.com/watch?v=DFb9dnOWTxw)
**Author:** Compositing Academy
**Duration:** 9m50s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Can you see which object here is fake?
[0:04] Did you catch it?
[0:04] Let's show it again.
[0:05] Something in this scene is fully virtual while everything else is real.
[0:10] If you said the cup, you fell for my trap, it's actually real.
[0:13] However, I have surrounded the cup by virtual objects.
[0:16] In this video, I'm going to talk about two concepts you can use to blend objects
[0:19] virtually with real footage that I've used professionally as a compositor.
[0:23] Many beginner VFX artists think you only need an HTRI to light your object in a real scene,
[0:28] and that's all you do.
[0:29] This is merely the starting point for CG integration.
[0:33] So technique number one is to paint with light.
[0:35] So there are a lot of concepts that can go into matching lighting contrast saturation hue.
[0:40] So if we look at our raw render here and we look at these coins,
[0:44] this is rendered with an HTRI, but it doesn't match still.


### CG Integration Study in Nuke [0:45]
**Transcript (timestamped):**
[0:47] So you can see our little pools of light essentially are not crossing over and integrating
[0:54] our coins here.
[0:54] And now you could, of course, try to match all these things perfectly in CG.
[0:58] You could try to do a better shadow, but you would be moving these lights around in 3D space.
[1:02] And just for these coins, that could be a pretty time consuming process.
[1:06] So it's not exactly the most efficient to actually do some of these things in lighting.
[1:11] Just because you can doesn't necessarily mean it's actually faster.
[1:14] So in compositing, this is really, really fast.
[1:16] So essentially what we can do in compositing is just essentially roto some shapes and track them
[1:21] onto our CG.
[1:22] So something like this would be a mix of basically roto shapes tracked on,
[1:27] or you could use 3D position mats to essentially stick on your color grades.


### PMattes in Nuke [1:30]
**Transcript (timestamped):**
[1:31] In addition, you could use normals relighting to catch some of the edge highlights.
[1:36] So I'll show some of that now.
[1:37] But basically the main idea is here is we just need to match the saturation,
[1:41] which is a little bit less saturated and the highlights a bit brighter.
[1:44] Some of the angled surfaces are going to hit differently with the lighting.
[1:48] And in our shadow, we're going to get a little bit less saturated and also maybe catch some
[1:51] reflections based on the orientation of some of these coins.
[1:56] So if we just look at a few of those changes here, here is the portion of my script that is
[1:59] related to the coins.


### CG Grading [2:00]
**Transcript (timestamped):**
[2:01] So if we just take a look at it, essentially, it's very simple.
[2:04] There's nothing really complex going on.
[2:06] Now the CG is actually rendered on one frame because we have a camera that only rotates.
[2:10] It's called a nodal pan.
[2:11] So if you're unfamiliar with those concepts, I check out the Nuke beginner course because
[2:15] we talk about some of those concepts as well as working in an unpre-multiply space.
[2:20] So if you're a complete beginner, highly recommend it.
[2:22] But essentially what we have here, really just some simple grades.
[2:26] So first, I'm just darkening the edges here to get a bit more shadow.
[2:29] And again, contact shadow.
[2:31] I always think of shadows in terms of kind of layers.
[2:34] It just helps me think about it.
[2:36] So there's kind of a broad shadow, but maybe there's a contact shadow.
[2:38] It's a little bit darker right underneath.
[2:41] And so next, we add a little bit of highlights on the surfaces.
[2:44] Like I said, at a glancing angle, we have the Fresnel effect, but also we have bumps on the


### Relighting with Normals in Nuke [2:45]
**Transcript (timestamped):**
[2:49] surface that will just catch direct lighting.
[2:52] So essentially what we have here is just something like the normals.
[2:55] We rotate the normals.
[2:57] This node is, you can find on Nucopedia, it basically just allows you to rotate these.
[3:02] The normals are basically representing the direction that the face is angled,
[3:07] but we can rotate them if we want to get a little bit of an alpha based on,
[3:11] if we want to catch some highlights.
[3:12] So you can rotate them around, you just play with these numbers.
[3:14] You get an alpha matte.
[3:16] And essentially you can just plug this into a color grade and then we can just pop out
[3:20] some of the surface detail here.
[3:22] And so I did that twice.
[3:24] And then in the light areas, that's basically what's happening.
[3:28] Again, these are just roto shapes and all the stuff will be tracked on because we have a


### Grading with Rotos [3:30]
**Transcript (timestamped):**
[3:33] single frame that we apply essentially the motion to at the end.
[3:37] So we go through here, we desaturate the highlights a little bit,
[3:40] which is a very common characteristic of highlights.
[3:42] So you should get less saturated.
[3:45] So we get like this, essentially a little bit darker, a little bit less saturated overall.
[3:50] And again, playing around with more contact shadows,
[3:54] maybe playing with the reflection itself.
[3:58] We can actually fake a bit of reflection by essentially rotoing a softer.
[4:02] It's not actually a shadow.
[4:03] It's more of a reflection.
[4:05] And so I was looking at some reference, I actually took some photos of gold coins
[4:09] to look at what real ones would look like before I did this, pretty much the same condition,
[4:13] which by the way is not cheating.
[4:14] If you look at films like Iron Man or a ton of films,
[4:17] they always try to get some kind of real reference and shoot it,
[4:22] or you just try to find some reference online, which you can also do.
[4:25] So the last thing here, a little bit of relighting again, which again, just the normals.
[4:30] But I wanted to catch some of this blue reflection that's a bit in the window.
[4:35] And based on the reference I took had this in it.
[4:37] So we can just get a bit of that, the light in the shadow area.
[4:41] And that really helps just to blend everything together.
[4:44] So you can see it's just a stack of color grades.
[4:46] But if you miss some of the color grades, this is where people don't really understand
[4:50] compositing.
[4:51] They think it's just like a single color grade.
[4:53] But really, this is what compositing looks like in the vast majority of cases
[4:57] where you're dealing with full CG or CG integration.
[5:00] There is these micro decisions that stack up over time.
[5:04] And that is essentially what makes something look real.
[5:06] It's not going to be one color grade or one warmth edition or something like that.
[5:11] So another part we can talk about light hits.
[5:13] Now, there's a lot of things going into detailing this book with compositing.
[5:16] But I'll talk just specifically about one part because it relates to this painting light concept.
[5:21] So essentially, if we just roto on some shapes, this is literally just a roto shape being plugged
[5:26] into a mask here.
[5:27] But there's a little bit of a trick in terms of the way that you can apply essentially the


### Pulling out Detail with Luma Keyer [5:30]
**Transcript (timestamped):**
[5:32] grade to this rather than just brightening it up and adding some color to it.
[5:36] So oftentimes you want to think about what it is that you're compositing.
[5:39] What is the material and how is the light reflecting?
[5:41] So typically a beginner might approach this in a way of just taking a roto
[5:46] and maybe brightening it up like this.
[5:47] So we would just take it in a roto and maybe we brighten it up like this.
[5:52] And then we add a little bit of color to it.
[5:54] This gives a very flat look even if we punch this up a little bit more.
[5:58] And the reason this is because you want to think about the way the material is actually
[6:01] behaving.
[6:01] There might be some materials that behave like this and that's fine.
[6:04] But a lot of cases and a lot of times it's actually a multi-layered sort of color grade.
[6:10] And so if we imagine that this is a dark purple book, there might be some small fibers on this
[6:16] book that reflect a little bit differently.
[6:17] And also those fibers are a lighter color than the book itself, which means they reflect more
[6:22] light.
[6:23] So if we think about that fundamental sort of physics-based approach first,
[6:27] like what is the color that's reflecting back?
[6:29] What is the material made of?
[6:31] Essentially the way that you can break it up instead is to actually pull a lumache,
[6:35] let's say, of the surface and we could try to get some of those fibers out of the book.
[6:38] And we mask that against the little roto shape that we did.
[6:41] So we use this alpha to grade up first, which is going to essentially bring up the little
[6:48] highlights.
[6:48] So if we break this into two grades, we can actually see the difference here between something that
[6:53] kind of can pull out detail and sort of maintain the feeling of lighting versus a very flat looking
[6:59] light, essentially.
[7:00] Even if we take some of the color out, we always see this very flat looking thing.
[7:04] I've seen a lot of beginners do the same exact mistake where they're not thinking about the
[7:08] materials and thinking about the way light reflects, which is ultimately what you're
[7:12] trying to do.
[7:12] So technique number two is finding connection points.
[7:15] And this is sort of a methodology that I've constructed where I'm basically scanning back
[7:19] and forth between my CG objects and reality.


### Spotting Differences [7:20]
**Transcript (timestamped):**
[7:22] And I'm looking for every detail I can find.
[7:25] And it's sort of an iterative process to feel, you know, make sure that nothing feels out of
[7:29] place.
[7:29] So if I'm looking at this book, for example, specific things that I'm looking for are things
[7:34] like shadow softness, depth of the shadows.
[7:37] What are the, how dark do they go?
[7:39] Depth of field, exposure.
[7:41] All of these things are essential things that we need to match.
[7:44] There are hue variations, surface imperfections, texture size, texture sharpness.
[7:49] These are all things that I'm looking around and trying to match, essentially.
[7:53] And, you know, I kind of think of it like scanning back and forth.
[7:56] If I'm looking here, I'm also looking here and making these comparisons over and over
[8:00] and over.
[8:01] Now, to give you a very concrete example in this shot, we can look at it.
[8:04] So one area we could actually get tricked on this is if we're making a comparison from
[8:08] here to here, we could actually get a little bit tripped up as a compositor if you're just
[8:12] looking at this and not thinking about the fundamental principles at the same time.
[8:16] Because if I was just making a comparison here to here, we would say that this is much
[8:19] brighter and that that is the intensity that this reflection should be.
[8:24] But you need to remember that this book reflects differently.
[8:26] So I had some photo reference of a dark book just like this and it actually was much darker
[8:30] than the table itself.
[8:32] So you need to remember, yes, we're matching things, but we also need to remember the principles
[8:37] under which we're operating, which is if this is a darker book, it's reflecting less light
[8:42] back.
[8:42] A white object and a black object don't reflect the same amount of light back to the viewer.
[8:47] And so that's where you can get tricked when you're trying to match things.
[8:50] Keep that in mind as well.
[8:52] It's not just matching, but also matching and then comparing against the things you know.
[8:56] And so another example of this would be this little highlight on the book.
[9:00] So I know that a surface that has been worn down over time, let's say this is an older book,
[9:05] maybe it got rubbed up against other books and you know, over time it got a little bit smoother,
[9:10] which is what happens if you if you ever were a kid and you had a rock that you put into a rock
[9:14] polisher and it's a bit more reflective, that's what happens.
[9:17] And so we can look at reflection like the edge of this book here, which has this little blue
[9:21] specular highlight running down the surface and we can match that we can add a bit of that in the
[9:25] edge using the same techniques I just showed, bit of normals, bit of rotoscoping, things like that.
[9:29] And essentially just make those connection points more obvious and make things feel more integrated.
[9:34] So hopefully those two techniques help you out.
[9:36] If you want to learn this kind of stuff, I have over 25 hours and a bunch of bonus projects
[9:40] you can go through in the beginner series, which is really the best place to start if you want
[9:43] to get into this kind of stuff and get up to that high level with your own projects.



---

## Captured Frames

- [0:44] tutorials/frames/2-expert-vfx-tips-to-perfectly-blend-cg/frame_000.jpg
- [1:16] tutorials/frames/2-expert-vfx-tips-to-perfectly-blend-cg/frame_001.jpg
- [2:55] tutorials/frames/2-expert-vfx-tips-to-perfectly-blend-cg/frame_002.jpg
- [3:37] tutorials/frames/2-expert-vfx-tips-to-perfectly-blend-cg/frame_003.jpg
- [5:47] tutorials/frames/2-expert-vfx-tips-to-perfectly-blend-cg/frame_004.jpg
- [6:35] tutorials/frames/2-expert-vfx-tips-to-perfectly-blend-cg/frame_005.jpg
- [8:04] tutorials/frames/2-expert-vfx-tips-to-perfectly-blend-cg/frame_006.jpg

---

## Structured Notes

### Core Technique
CG integration is not one HDRI-lit render plus a single color grade — it's dozens of stacked micro-decisions built in comp: hand-rotoed/tracked "painted light" (contact shadows, glancing-angle highlights, faked reflections) driven by a rotated-normals alpha matte, plus a disciplined "connection points" methodology of continuously comparing CG against real reference while remembering that different materials (a dark book vs. a bright table) legitimately reflect light differently, so naive 1:1 brightness matching between them is a trap.

### Summary
Compositing Academy demonstrates, on a real coin-and-book tabletop shot with a CG cup/coins hidden among real props, that an HDRI-lit render is only a starting point, not the finish line. Technique 1, "paint with light": rather than re-lighting in 3D (slow, for what should be a fast comp fix), roto shapes are tracked onto the single-frame CG render (the camera is a nodal pan, so only one CG frame needed rendering, with tracking applied at the end) to add contact shadows (layered — broad shadow, then a darker contact shadow underneath), glancing-angle Fresnel highlights, desaturated highlight areas (a common real-world highlight characteristic), faked soft reflections roto'd in based on photographed real-object reference, and colored light bounce (e.g. a blue window reflection found in reference photos). Edge/surface highlights specifically are pulled from a `RotateNormals` (Nucopedia gizmo) alpha matte fed into a `Grade`, done multiple times for different light directions. A key sub-technique for surface detail: instead of just brightening a roto'd region flatly (which looks "flat" and fake), pull a luma key of the surface's own texture/fiber detail and use that as the grade's alpha, so brightened highlights follow the material's actual micro-texture — reasoned from first principles about what the material is and how it reflects light. Technique 2, "finding connection points": a disciplined scanning methodology of repeatedly comparing every visual property (shadow softness/depth, DOF, exposure, hue, surface imperfections, texture size/sharpness) between the CG and real elements, while remembering that materials don't reflect equally — e.g. a dark book will legitimately read darker than a bright table surface even in identical lighting, so matching brightness 1:1 between mismatched materials is the actual mistake, not a lighting failure.

### Key Steps
1. Recognize that an HDRI-lit CG render is a starting point, not a finished integration — pools of light, shadow contrast, and highlight behavior will not automatically cross over and match the real plate.
2. Rather than iterating lighting setups in 3D (slow, especially for small objects like coins), roto shapes and track them onto the CG render in comp for fast, art-directable light/shadow painting.
3. Since the shot is a nodal pan (rotation-only camera), render just one CG frame and apply the tracked motion to the whole roto/grade stack at the end rather than animating shadows per frame.
4. Layer shadow types: a broad ambient-occlusion-style shadow, then a separate, darker "contact shadow" directly underneath contact points.
5. Add glancing-angle highlights using a `RotateNormals` gizmo (Nucopedia) — rotate the normals pass to generate an alpha matte representing which surfaces catch light from a given direction, feed that alpha into a `Grade`; repeat with different rotation values for multiple light directions/highlight passes.
6. Desaturate highlight regions specifically — a common real-world characteristic of specular highlights that's easy to skip.
7. Fake soft reflections with a roto shape (not a shadow — a distinct, softer, brighter shape) informed by real photographed reference of similar objects/materials in similar lighting.
8. Add colored bounce/reflection details found in reference photography (e.g. a blue window reflection) via another `RotateNormals`-driven pass, applied specifically in shadow regions.
9. For surface highlight detail (e.g. worn/polished book edges, fiber texture): avoid simply brightening a flat roto shape — pull a luma key of the material's own texture (fibers, grain, imperfections) and use that luma matte as the `Grade`'s mask, so the added light follows the material's actual surface detail rather than reading as a flat painted highlight.
10. Apply the "connection points" comparison methodology: continuously scan back and forth between CG and real elements checking shadow softness/depth, depth of field, exposure, hue variation, surface imperfections, texture size and sharpness.
11. Guard against the brightness-matching trap: different materials (e.g. a dark book vs. a light table) legitimately reflect different amounts of light even under identical illumination — don't force 1:1 brightness matching between visually different materials; reason from the material's actual reflectance first.
12. Source real reference photography of comparable materials/objects under similar lighting before finalizing comp decisions — treated as standard practice (referenced as common in productions like Iron Man), not "cheating."

### Nodes / Tools / Settings
- `RotoPaint`/Roto shapes — tracked onto a single CG frame for contact shadows, highlights, faked reflections, and colored bounce light
- `RotateNormals` (Nucopedia gizmo) — rotates the normals pass to generate directional alpha mattes for highlight/relight passes, used multiple times per shot
- `Grade` — driven by RotateNormals alpha mattes and by luma-keyed surface-texture mattes for material-aware highlight detail
- Luma key of surface texture (as opposed to a flat roto) — mask source for physically-motivated highlight detail on fibrous/textured materials
- Single-frame CG render + tracked motion — render-saving technique for nodal-pan (rotation-only) camera shots, referenced back to the channel's beginner series

### Difficulty
Intermediate

### Foundry App & Version
Nuke. No on-screen version banner or OCIO metadata visible in the captured frames — version not specified.

### Tags
relighting, grading, roto, compositing, digital-matte-painting, intermediate

---

## Related Tutorials
Shares `relighting`/`RotateNormals`-driven highlight technique with Transform your FLAT Green Screen into Cinematic Lighting (`transform-your-flat-green-screen-into-cinematic-lighting.md`) — both use normals-derived alpha mattes to add directional light/highlights in comp rather than re-rendering. Also shares the nodal-pan single-frame-render optimization with How I Use Compositing to Skip THOUSANDS of Hours Rendering (`how-i-use-compositing-to-skip-thousands-of-hours-rendering.md`). Shares `relighting`, `grading`, `roto`, `compositing` with Nuke Compositing Tutorial: Integration Sketching (`nuke-compositing-tutorial-integration-sketching.md`) — that video's value-conflict/dynamic-range diagnostic methodology closely parallels this one's "finding connection points" approach, applied to a keyed live-action character rather than CG. Also shares the fake-reflection/contact-selling technique with Compositing Complex Shadows in Nuke [Advanced] (`compositing-complex-shadows-in-nuke-advanced.md`), which rotoscopes similar fake ground reflections on its CG cube.
