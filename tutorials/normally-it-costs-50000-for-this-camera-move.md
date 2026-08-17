---
title: Normally it costs $50,000+ For This Camera Move
source: YouTube
url: https://www.youtube.com/watch?v=GG7c29nWD68
author: Compositing Academy
ingested: 2026-08-14
app: "Blender (concept directly transferable to Nuke's Card3D/ImagePlane workflow); Nuke used briefly for slap-comp review"
version: "not specified"
tags: [3d-system, camera-tracking, compositing, digital-matte-painting, virtual-production, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/normally-it-costs-50000-for-this-camera-move/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Normally it costs $50,000+ For This Camera Move

**Source:** [YouTube](https://www.youtube.com/watch?v=GG7c29nWD68)
**Author:** Compositing Academy
**Duration:** 8m57s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below. Condensed transcript summary (full timestamped version retained in git history at commit da2ee98):

[0:00] Goal: take a real, camera-tracked drone move (orbiting a green-screen subject) and exaggerate it to feel like an action-scene car-chase camera, without reshooting. Studio terms: "re-rack," "reposition," or "card rig."
[0:51] Because the subject is 2D footage on a flat projected card (not a real 3D character), exaggeration has hard limits.
[1:51] Technique: duplicate the tracked camera; exaggerate only the duplicate; stay close enough to the original that the projection still reads.
[2:43] Side-to-side/orbit rotation breaks the illusion past roughly 15-20°; forward/backward push-in/out is far more forgiving and can go extreme, even enabling a "camera handoff" from a distant virtual camera into the real tracked camera's position.
[3:38] Before/after: default tracked drone orbit (rough "lighting slap comp") vs. the exaggerated version with added tilt, camera shake, and push in/out — much more intense and interesting.
[4:45] Author stresses the principle is 3D-app-agnostic (Blender/Unreal/Houdini) — translate/rotate/curve-adjustment concepts transfer directly.
[5:16] In Blender: two cameras (original tracked + modified), plate projected via a custom "Image Plane" tool (Compositing Academy Patreon) that mimics Nuke's Card3D/ImagePlane workflow — camera-facing card, texture always sourced from the ORIGINAL unmodified camera so perspective stays correct.
[6:39] Camera shake added via free tools (e.g. Ian Hubert's "Camera Shakeify" for Blender, equivalents exist for Houdini/Unreal).
[7:07] Preferred non-curve-editor method: parent the modified camera to an empty placed at the orbit center, rotate the empty for clean orbiting motion.
[7:59] Final rig: modified camera + orbit-empty + shake, all nested under a master empty that can be animated to make the "vehicle" fly through space, carrying along any placeholder foreground geometry (a rock stand-in).

---

## Captured Frames

- [0:20] tutorials/frames/normally-it-costs-50000-for-this-camera-move/frame_000.jpg
- [2:00] tutorials/frames/normally-it-costs-50000-for-this-camera-move/frame_001.jpg
- [3:38] tutorials/frames/normally-it-costs-50000-for-this-camera-move/frame_002.jpg
- [4:06] tutorials/frames/normally-it-costs-50000-for-this-camera-move/frame_003.jpg
- [5:16] tutorials/frames/normally-it-costs-50000-for-this-camera-move/frame_004.jpg
- [6:14] tutorials/frames/normally-it-costs-50000-for-this-camera-move/frame_005.jpg
- [7:44] tutorials/frames/normally-it-costs-50000-for-this-camera-move/frame_006.jpg

---

## Structured Notes

### Core Technique
The "re-rack," "reposition," or "card rig" technique (studio terms for the same trick): take a camera-tracked 2D plate projected onto a 3D card/image-plane, duplicate the tracked camera, and animate the duplicate's motion (shake, push in/out, limited orbit) independently of the original to exaggerate a real camera move — without re-shooting or fully rebuilding a 3D scene, because the plate stays a flat projected card.

### Summary
Starting from a drone-shot green-screen plate that was camera-tracked and orbits the subject in a smooth circular pattern, the goal is to make the move feel more like an "action-scene car chase" camera without having actually filmed one. Because the subject is 2D footage projected onto a flat card (not a real 3D character), the exaggeration has hard limits: side-to-side (orbit) rotation breaks the illusion fast (roughly 15-20 degrees max before the flat-card nature becomes visible), but forward/backward push-in/push-out is much more forgiving and can go quite extreme — enabling a "camera handoff" effect where a virtual camera pushes in from far away toward where the real tracked camera actually sits. The technique: duplicate the tracked camera, keep the duplicate close enough to the original that the projection still reads correctly, and add secondary motion — camera shake (via a free shake-rig tool, e.g. Ian Hubert's "Camera Shakeify"), tilt, and push in/out — either by adjusting the new camera's animation curves directly, or (the presenter's preferred, curve-free method) by parenting the new camera to an empty/axis placed at the desired orbit center and simply rotating that empty. The projected plate itself uses a custom Blender "Image Plane" tool (available on the channel's Patreon) that mimics Nuke's Card3D/ImagePlane workflow — a camera-facing card that projects footage from the original (unmodified) tracked camera, with extra controls for projection distance. The final rig nests: modified camera → parented to orbit-empty → the whole assembly parented to a master empty that can be animated to make the "vehicle" fly through space, with the plate and any placeholder geometry (a rock stand-in) locked to it. Before compositing, the shot is checked as a rough "lighting slap comp" (quick key + projection) to confirm the exaggerated move still reads believably. The author stresses the concept is 3D-app-agnostic (Blender/Unreal/Houdini all work the same way) — it's the translate/rotate/curve-adjustment principle that matters, not the specific software.

### Key Steps
1. Camera-track the real plate first — this is what supplies the correct perspective shift of the real subject; the technique only works because the projection is anchored to a validated track.
2. Project the plate (rough key/slap comp) onto a camera-facing card/image-plane driven by the ORIGINAL tracked camera — the texture must come from the unmodified camera so the projection stays perspective-correct regardless of what the new camera does.
3. Duplicate the tracked camera to create a second, "modified" camera that will carry the exaggerated move.
4. Respect the projection's limits: keep side-to-side/orbit rotation small (~15-20° max) since a flat 2D card breaks the illusion fast under wide angular change; forward/backward push in-and-out is much more forgiving and can be pushed further, even into a full "camera handoff" from far away into the original camera's position.
5. Add secondary motion to the modified camera: apply a camera-shake tool/preset (e.g. Camera Shakeify for Blender, or an equivalent rig in Houdini/Unreal) for handheld-feeling jitter.
6. Instead of hand-animating curves on the new camera, place an empty/axis at the intended orbit center, parent the modified camera to it, and rotate the empty — this produces clean orbiting motion without curve-editor fiddling.
7. Nest the whole rig (modified camera + its orbit-empty + shake) under a master empty/null that can itself be animated, so the entire camera assembly (plus any placeholder foreground geometry) can be moved together to simulate the "vehicle" traveling through the scene.
8. Validate with a rough lighting slap comp (quick key, projected into place) before committing further compositing/lighting work, to confirm the exaggerated move still reads as attached to the subject.

### Nodes / Tools / Settings
- Image Plane tool — custom Blender add-on by Compositing Academy (Patreon-distributed) for camera-facing projected cards with configurable projection distance; explicitly described as replicating Nuke's Card3D + ImagePlane workflow, with extra Blender-specific controls
- Camera Shakeify — free third-party camera-shake tool by Ian Hubert (Blender); equivalent tools exist for Houdini/Unreal
- Empty/Axis object — used as a rotation pivot for orbit motion via parenting rather than manual curve animation
- Nuke — used briefly for a rough "lighting slap comp" review (quick key + projection) shown in one frame; the core rigging work is entirely in Blender

### Difficulty
Intermediate — conceptually simple (duplicate camera, animate secondary motion, respect projection limits) but requires solid understanding of camera tracking and 3D projection to avoid breaking the illusion.

### Foundry App & Version
Not a Nuke-specific tutorial — the rig is built and demonstrated in Blender. Nuke is referenced twice: (1) as the direct conceptual origin of the Image Plane/Card3D projection technique being replicated in Blender, and (2) briefly on-screen for a slap-comp review pass. No Nuke version is stated or relevant here.

### Tags
3d-system, camera-tracking, compositing, digital-matte-painting, virtual-production, intermediate

---

## Related Tutorials
- Nuke Compositing Technique | Card3D + PixelsToPos [Beginners] (tutorials/nuke-compositing-technique-card3d-pixelstopos-beginners.md) — shares 3d-system, camera-tracking; covers the native Nuke Card3D/ImagePlane workflow this video's Blender tool replicates.
- Can I Create a Speeder Chase on a TINY Greenscreen? (tutorials/can-i-create-a-speeder-chase-on-a-tiny-greenscreen.md) — shares the same "speeder" vehicle CG asset and Iceland/action-sequence project, compositing, virtual-production.
- Render World Position in Blender for Nuke (tutorials/render-world-position-in-blender-for-nuke.md) — shares cross-app Blender-to-Nuke pipeline pattern, 3d-system.
- How I Made Pro VFX in a BARN! (New Tech REVEAL) (tutorials/how-i-made-pro-vfx-in-a-barn-new-tech-reveal.md) — shares the "expensive technique made affordable with clever practical tricks" theme and the same channel's BTS case-study style.
