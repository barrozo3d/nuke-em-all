---
title: Nuke Compositing Artistic Basics (7/8): Glows
source: YouTube
url: https://www.youtube.com/watch?v=FFutBgMZBLo
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)"
tags: [compositing, grading, digital-matte-painting, beginner]
extraction_status: complete
frames_dir: tutorials/frames/nuke-compositing-artistic-basics-78-glows/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Nuke Compositing Artistic Basics (7/8): Glows

**Source:** [YouTube](https://www.youtube.com/watch?v=FFutBgMZBLo)
**Author:** Compositing Academy
**Duration:** 6m30s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] The next one we want to talk about is post-processing effects and layering.


### Post-Processing Effects and Layering [0:07]
**Transcript (timestamped):**
[0:11] These are the last things you do in your comp.
[0:14] It's glows, it's things that are happening in the lens, stuff like that.
[0:19] Let's talk about a couple of them.
[0:21] One would be called Bloom.
[0:23] If we have a really bright scene, I've overexposed the scene and created some bloom.


### Bloom [0:26]
**Transcript (timestamped):**
[0:28] What is bloom?
[0:29] It could be smudging that's in your lens.
[0:33] It's something that happens when it's overexposed.
[0:36] It's like a broad glow coming from a brighter light source.
[0:40] This is what bloom looks like.
[0:42] You'll see that it's coming over the trees.
[0:46] We know that the real world, the light is not in front of the trees.
[0:50] This bloom, logically, it's not in front of the trees in real life.
[0:54] That's not a volume of smoke here.
[0:57] That's something else.
[0:58] There's some mist in the air.
[1:00] There might be some light, but that's not the same thing.
[1:02] This is bloom.
[1:04] Bloom is happening inside the lens, inside the camera.
[1:07] It can happen in your eyes as well.
[1:09] It can be a glow.
[1:12] You need to understand that glows or any post-processing effect is the last thing to happen.
[1:19] Nothing can go over the top of this glow.
[1:22] I'll show you what I mean in a second by that.
[1:26] That's bloom and what it looks like.
[1:29] We also have one that looks similar to bloom, but it's not the same.


### Lens Diffusion [1:31]
**Transcript (timestamped):**
[1:31] It's called lens diffusion.
[1:33] A way you can create this is just basically blur your picture and then just merge it back
[1:38] over itself as a screen.
[1:40] You can even do it over.
[1:41] It doesn't make a difference.
[1:42] Then just mix it down very, very low.
[1:46] That would be if your lens has some smudges on it.
[1:52] There's a little bit of light scattering across the surface of the glass.
[1:56] That would be lens diffusion.
[1:58] It's not exactly the same because lens diffusion is just overall blurring effect being added
[2:05] over the top.
[2:07] Whereas bloom is more in the highlights and it's creating a glow from the highlights.
[2:13] They look similar, but they're not the same.
[2:15] Sometimes you can use both.
[2:19] We're not adding anything fake to our shot, so we're not going to be doing those, but
[2:23] it's good to know about them.
[2:26] The other thing we need to understand, what I said just a couple of seconds ago, I said
[2:31] that glows are happening in the lens.
[2:35] Objects never pass in front of a glow because it's happening last.
[2:41] It's not happening in the real world.
[2:42] If we look at this, this would never happen.
[2:45] We have a glowing object like this.
[2:49] The glow itself, this glow, the effect coming off, that's not something that is
[2:55] in the atmosphere around the object.
[2:57] It's something happening optically in the camera or in your eye.
[3:02] It's just from the light scattering and bouncing around imperfectly.
[3:09] This glow would not look like this in real life.
[3:13] How it would look is like this.
[3:15] If we have our glowing object and we have an object in front, we see that the glow is
[3:21] actually wrapping around the object in front.
[3:25] That's just because it's an optical illusion basically with our eyes.
[3:31] That's really, really important to know is if you're adding a glow like we do in our
[3:36] car scene, the smoke that we add after, we don't want the smoke to be going over the
[3:43] top of the glow.
[3:45] We want the smoke to cut away from the object, but the glow would wrap around it like this.
[3:54] Just remember, that's wrong, that's right.
[3:57] Don't ever, if you're ever putting an object in front and you see your glow is behind,
[4:02] you need to make that glow wrap.
[4:04] That's what the light wrap note is for.
[4:07] There's another way to do this instead of using a light wrap.
[4:14] We have a radio here and we have the second object placed over the top.
[4:19] Instead of having the glow underneath and then wrapping a second, for example, we have
[4:26] the glowing object underneath and then we put an object over and then we put light wrap,
[4:31] the light wrap effect to get that.
[4:33] Instead of doing that, there's another way to do it, we'd be just putting the second
[4:37] object over and then you do a luminance key and you key out the object.
[4:43] You get the object but also with the cutout of the object in front.
[4:49] Then we would pre-multiply that and glow it.
[4:51] You see automatically that glow is in the shape wrapping around our object that's in
[4:55] front.
[4:56] If you plus that back over, you see that the glow is in the shape of this.
[5:05] It's not the same as that.
[5:08] That's wrong, this is right.
[5:10] It still looks a little bit weird, so maybe you would want to add an extra light wrap
[5:13] just to get the very hot edge.
[5:17] If this is a very bright object, the glow would be quadratic.
[5:20] It would be falling off quadratically.
[5:22] I talk about that in my photo-real compositing class as well, about quadratic fall off.
[5:27] If you guys are interested, you can take that class if you haven't.
[5:32] This helps that sell that illusion as well.
[5:35] I put that light wrap as well and it just helps blend the edge into the other object.
[5:42] Either of these are right.
[5:43] If we look at this one or we look at this one, they look a little bit different.
[5:48] I actually like this one better.
[5:50] This one seems to fall off a little bit too much here.
[5:53] This one seems a little bit more realistic.
[5:56] You can see this one's less quadratic.
[6:01] It's kind of too, I don't know.
[6:02] If you look at the difference, this one just looks better.
[6:05] Play around and you can even practice just creating that scene yourself.
[6:10] Try to get the glow wrapping around an object in the front.
[6:13] I just did it with two spheres.
[6:17] It's very simple.
[6:19] The exponential glow node will be provided to you if you don't already have it in the
[6:23] script at the top of the script.
[6:27] That'll be there.



---

## Captured Frames

- [0:42] tutorials/frames/nuke-compositing-artistic-basics-78-glows/frame_000.jpg
- [2:49] tutorials/frames/nuke-compositing-artistic-basics-78-glows/frame_001.jpg
- [3:21] tutorials/frames/nuke-compositing-artistic-basics-78-glows/frame_002.jpg
- [4:26] tutorials/frames/nuke-compositing-artistic-basics-78-glows/frame_003.jpg
- [4:55] tutorials/frames/nuke-compositing-artistic-basics-78-glows/frame_004.jpg

---

## Structured Notes

### Core Technique
Part 7 of 8. Distinguishes bloom from lens diffusion, establishes that glows/post-processing effects are optically the *last* thing to happen (in the lens/eye, not the scene) and therefore must never be occluded by objects placed in front of a glowing element — and demonstrates two ways to make a glow correctly wrap around a foreground object: a `Light Wrap`-style node, or a manual luminance-key + pre-multiply + glow build.

### Summary
Bloom is defined as a broad glow radiating from an overexposed/bright light source, caused by scattering inside the camera lens (or the eye) — not something physically present in the scene's atmosphere (the example: bloom appearing to sit "in front of" trees, which could never happen with real atmospheric light/smoke). Lens diffusion is visually similar but distinct — created by blurring the image and screening/merging it back over itself at low opacity, simulating light scattering across smudges/imperfections on the glass; bloom concentrates specifically in the highlights, while lens diffusion is a more uniform overall softening. The key rule: since glows/post-processing happen optically after the real scene (in the lens/eye), they must never be visually blocked by something placed in front of the light source in the composite — if an opaque object sits between camera and a glowing light, the glow should wrap around that object's silhouette, not disappear behind it. Two methods are demonstrated on a simple two-sphere test scene (bright glowing sphere + dark sphere in front): (1) the standard `Light Wrap` node/effect placed after compositing the foreground object over the glow; (2) an alternative manual technique — place the foreground object over the glowing element, luminance-key the combined result to isolate just the glow-shape (which naturally excludes the now-opaque foreground silhouette), `Premult`, apply an exponential glow, then `Plus`/screen that back over the comp, producing a glow correctly wrapped around the foreground object's edge with no extra node needed. The manual method is judged by the presenter to look slightly more realistic/less "too quadratic falloff" than the pure Light Wrap result in this test, though either is presented as valid; adding a subtidal light-wrap pass on top of the manual method for just the brightest hot edge is suggested as an optional refinement. Notes the glow's falloff should be quadratic (cross-referenced to the presenter's separate photo-real compositing class), and that the `Exponential Glow` node used is provided in the accompanying project script.

### Key Steps
1. Distinguish bloom (concentrated broad glow specifically from bright highlights/overexposed light sources, caused by lens/eye scattering) from lens diffusion (a more uniform blur-and-screen-merge-back-at-low-opacity softening simulating a smudged/imperfect lens surface) — visually similar but different causes and looks.
2. Internalize the core rule: glows and other post-processing/lens effects are the very last thing applied in a real optical system — nothing in the actual scene can occlude them, so in comp, no foreground object should ever visually cut off or sit in front of a glow's edge; instead the glow must wrap around that object's silhouette.
3. Build a simple two-object test (a bright/glowing element behind, an opaque element in front) to practice and verify correct glow wrapping before applying it to production shots.
4. Method A — dedicated node: composite the foreground object over the glowing background element first, then apply a `Light Wrap`-style node/effect to bleed the background glow color around the foreground object's edge.
5. Method B — manual luminance-key build: composite the foreground (opaque) object over the glowing element first (so the glow is naturally occluded/cut correctly by the object's silhouette in the beauty), then take a `Keyer` (luminance key) of that combined result to isolate just the bright glow-source shape (now automatically excluding the foreground object's silhouette), `Premult` that isolated matte, apply an `Exponential Glow`/blur to it, and `Plus` (additive screen) it back over the composite — the resulting glow naturally wraps around the foreground object's edge because it was derived from the already-occluded shape.
6. Compare results side by side: judge whether the Light Wrap or the manual luminance-key method reads more realistic for the specific shot — the presenter preferred the manual method here, finding the pure Light Wrap result fell off "too quadratically" for their test scene.
7. Optionally layer an additional subtle light-wrap pass on top of the manual method to add just a very hot, bright rim at the object's edge for extra sell.
8. Keep glow falloff quadratic (not linear), matching real-world light falloff behavior (cross-referenced to the presenter's separate class on quadratic falloff in photo-real compositing).

### Nodes / Tools / Settings
- `Light Wrap` — standard node/technique for bleeding a background glow's color around a foreground object's silhouette edge.
- `Keyer` (luminance key) — manual-method alternative: keys the bright glow-source shape out of the already-composited (foreground-occluded) beauty, so the resulting matte is naturally already wrapped correctly.
- `Premult` — applied to the keyed glow-source matte before glowing it.
- `Exponential Glow` (referred to as a specific gizmo/node provided in the accompanying project script) — glow/blur applied to the isolated, pre-multiplied glow-source matte.
- `Plus` (additive/screen merge) — re-composites the isolated, glowed matte back over the shot.
- Quadratic falloff — the correct physical falloff curve for glow intensity, referenced from the presenter's separate photo-real compositing class.

### Difficulty
Beginner — conceptual lesson (bloom vs. lens diffusion, glow-occlusion physics) plus a straightforward node recipe (Keyer → Premult → Glow → Plus) as the practical alternative to a dedicated Light Wrap node.

### Foundry App & Version
Nuke — version not stated on screen or in narration. 2020 upload, predates this skill's release-notes backfill (starts at Nuke 13.0/March 2021), so treat as Nuke ~12.x era rather than a specific point release.

### Tags
compositing, grading, digital-matte-painting, beginner

---

## Related Tutorials
**Nuke Compositing Artistic Basics — 8-part series** (this is Part 7 of 8; all parts cross-link to each other):
- Part 1/8: Roles of Production (`nuke-compositing-artistic-basics-18-roles-of-production.md`)
- Part 2/8: 3 Point Lighting (`nuke-compositing-artistic-basics-28-3-point-lighting.md`)
- Part 3/8: Exposure (`nuke-compositing-artistic-basics-38-exposure.md`)
- Part 4/8: Shadows (`nuke-compositing-artistic-basics-48-shadows.md`)
- Part 5/8: Reflections and Fresnel (`nuke-compositing-artistic-basics-58---reflections-and-fresnel.md`)
- Part 6/8: Whitepoint and white balance (`nuke-compositing-artistic-basics-68-whitepoint-and-white-balance.md`)
- Part 8/8: Camera Artifacts (`nuke-compositing-artistic-basics-88-camera-artifacts.md`)
