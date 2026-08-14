---
title: The BEST Way to Use Normals to Relight in Nuke (NEW Toolset)
source: YouTube
url: https://www.youtube.com/watch?v=M-iKJu9hYBk
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "not specified — free 3rd-party gizmo set (Normals Toolkit: CA Detail Normals, Normal Mixer, CA_NormalMask) by Compositing Academy. CONFIRMED NOT Nuke's native Gaussian Splat / SplatRender relighting (Direct/Point/Spot lights, added Nuke 17.1) — same disambiguation as H7dBKDLXwPo and 8f2w7JxRaq4; this toolkit is 2D-normals-based, has nothing to do with Gaussian Splats or the 3D system"
tags: [relighting, gizmo, digital-matte-painting, compositing, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/the-best-way-to-use-normals-to-relight-in-nuke-new-toolset/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# The BEST Way to Use Normals to Relight in Nuke (NEW Toolset)

**Source:** [YouTube](https://www.youtube.com/watch?v=M-iKJu9hYBk)
**Author:** Compositing Academy
**Duration:** 8m56s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below. Condensed transcript summary (full timestamped version retained in git history at commit f9ef145):

[0:00] Releasing a free "Normals Toolkit" — three nodes that work together to fix normals-relighting quality issues, whether from CG renders or AI-generated normals.
[1:00] Example subject: an Iceland photogrammetry mountain scan (thousands of photos → proxy mesh) being turned into a moody cinematic digital matte painting.
[1:41] Baseline relight without the toolkit looks "plasticky" — sharp, triangulated highlights from the low-res proxy mesh's normals.
[2:37] CA Detail Normals extracts high-frequency detail from an image via luminance OR frequency-size separation (can use both to target different areas).
[3:23] Normal Mixer re-orients the detail normals to match the base normals' facing direction before blending — necessary because relight math breaks with inconsistently-oriented normals.
[3:53] Mixed result recovers micro-shadow/highlight detail lost in the flat proxy-mesh relight; toggling the node on/off live shows the before/after.
[5:11] Simpler CG sphere example: generating detail normals straight from an image without mixing doesn't follow the model's curvature; Normal Mixer fixes this by using the base normals as the "master" orientation.
[6:23] Roto-shape-targeted detail normals let you selectively pop specific features (e.g. a few rocks) more three-dimensional, with adjustable strength.
[7:30] Third node, CA_NormalMask, converts the combined normals into a light mask: rotation or click-to-sample light direction, plus a softness control that goes from diffuse-like falloff to a tight specular highlight — avoids needing Nuke's full 3D-system ReLight setup ("overkill... too many nodes") for fast 2D relight/specular work.
[8:34] Free download, three nodes plus an example scene.

---

## Captured Frames

- [0:03] tutorials/frames/the-best-way-to-use-normals-to-relight-in-nuke-new-toolset/frame_000.jpg
- [1:41] tutorials/frames/the-best-way-to-use-normals-to-relight-in-nuke-new-toolset/frame_001.jpg
- [2:37] tutorials/frames/the-best-way-to-use-normals-to-relight-in-nuke-new-toolset/frame_002.jpg
- [3:53] tutorials/frames/the-best-way-to-use-normals-to-relight-in-nuke-new-toolset/frame_003.jpg
- [5:14] tutorials/frames/the-best-way-to-use-normals-to-relight-in-nuke-new-toolset/frame_004.jpg
- [6:42] tutorials/frames/the-best-way-to-use-normals-to-relight-in-nuke-new-toolset/frame_005.jpg
- [8:04] tutorials/frames/the-best-way-to-use-normals-to-relight-in-nuke-new-toolset/frame_006.jpg

---

## Structured Notes

### Core Technique
Releases a free 3-node "Normals Toolkit" gizmo set that fixes the classic "plasticky/CG" look of normals-based relighting by extracting high-frequency detail normals from an image (via luminance or frequency-size separation) and re-orienting/mixing them onto a low-resolution base normal pass, so the relight picks up believable micro-shadows and micro-highlights instead of flat CG facets.

### Summary
The video diagnoses the standard mistake in normals relighting: using a low-res proxy-mesh normal pass (e.g. a photogrammetry scan) directly produces sharp, triangulated, "plasticky" highlights because the normals lack surface micro-detail. The fix is a 3-node toolkit: CA Detail Normals extracts extra normal detail from a 2D image by either luminance or frequency-size separation (targeting either brightness variation or the physical size of details — using both together lets you target different kinds of surface detail independently); Normal Mixer takes this extracted detail and the base (master) normals and re-orients the detail normals to face the same direction as the base — critical because relighting math breaks if normals point in inconsistent directions — then blends them together; a CA_NormalMask node turns the combined normals into a directional light mask, with controls for rotation or click-to-sample light direction, and a softness control that can push the result from soft diffuse-like falloff to a tight specular highlight. Demonstrated on two examples: (1) an Iceland mountain photogrammetry scan being turned into a moody cinematic digital matte painting — before/after comparison shows the detail-normals mix recovering all the micro-shadow/highlight detail that a flat proxy-mesh relight loses; (2) a simpler CG sphere example showing how targeted roto-shape-driven detail normals can selectively "pop" specific surface features (e.g. making a few rocks read more 3D) with fine per-region strength control, and how the CA_NormalMask's softness knob can fake either a diffuse relight or a fast specular highlight without opening Nuke's full 3D system/relight setup (author explicitly calls the native ReLight-via-3D-system route "overkill" and not great for this kind of fast 2D work).

### Key Steps
1. Start from any normal pass (CG render normals, AI-generated normals, or photogrammetry-scan proxy-mesh normals) — quality varies by source, and this toolkit exists to compensate for that.
2. Feed the source image (color/texture, not the normals) into CA Detail Normals; choose luminance-based or frequency-size-based extraction (or both, separately, to target different surface qualities) to generate a high-frequency detail normal map.
3. Feed the base/master normals and the extracted detail normals into Normal Mixer — it automatically re-orients the detail normals to match the base normals' facing direction before blending, so the combined result stays physically coherent for relighting.
4. Plug the mixed normals into CA_NormalMask to generate a light-direction mask: set light angle via rotation control or by directly sampling a point in the viewer (auto-orients the light toward that sample).
5. Adjust the softness control on CA_NormalMask to move between a broad diffuse-style falloff and a tight, rotatable specular highlight — a fast way to add believable specular without building a full 3D relight/ReLight setup.
6. For selective detail-popping (e.g. making specific rocks/features read more 3D): draw a roto shape over just those features, generate detail normals from that isolated region, mix it into the combined result, and use per-region strength to dial the effect up or down without affecting the rest of the surface.
7. Compare with/without the detail-normals mix live (toggle the node) to confirm the fix — the flat/plasticky proxy-mesh look should recover convincing micro-shadow and micro-highlight variation once mixed in.

### Nodes / Tools / Settings
- CA Detail Normals — free Compositing Academy gizmo; extracts high-frequency normal detail from a 2D image via luminance separation or frequency/size-based separation (selectable)
- Normal Mixer — free Compositing Academy gizmo; re-orients a detail-normal input to match a base/master normal input's facing direction, then blends them (prevents relight artifacts from inconsistently-oriented normals)
- CA_NormalMask — free Compositing Academy gizmo; converts normals into a directional light/relight mask; controls include rotation, click-to-sample light direction, and softness (diffuse to specular)
- Roto shape — used to isolate specific surface regions for targeted detail-normal generation/mixing
- Contrasted against: Nuke's native 3D-system-based ReLight workflow, described by the author as "overkill" and too many nodes for fast 2D relighting tasks

### Difficulty
Intermediate — requires understanding of normal maps and relighting fundamentals, but the toolkit itself is designed to reduce node-graph complexity versus a manual approach.

### Foundry App & Version
Nuke; exact version not stated on-screen. This is a free third-party/house gizmo set (Normals Toolkit), not a bundled Nuke feature. Explicitly confirmed NOT related to Nuke's native Gaussian Splat/SplatRender relighting toolset (Direct/Point/Spot lights in SplatRender, added Nuke 17.1) — this toolkit operates entirely on 2D normal passes and has no connection to the 3D Gaussian Splat system. Same disambiguation pattern as "I Made VFX Relighting WAY Better in Nuke" (H7dBKDLXwPo, CA Relight gizmo) and to be re-verified against "Finally! The Volumetric Tool Nuke Has Always Needed" (8f2w7JxRaq4) in this same batch.

### Tags
relighting, gizmo, digital-matte-painting, compositing, intermediate

---

## Related Tutorials
- I Made VFX Relighting WAY Better in Nuke (tutorials/i-made-vfx-relighting-way-better-in-nuke.md) — shares relighting, gizmo; same channel's other free relighting gizmo (CA Relight), same "not native SplatRender" disambiguation.
- 2 Expert VFX Tips to PERFECTLY Blend CG (tutorials/2-expert-vfx-tips-to-perfectly-blend-cg.md) — shares relighting; covers painted-light/RotateNormals technique that this toolkit's Normal Mixer partially automates.
- Can I Create a Speeder Chase on a TINY Greenscreen? (tutorials/can-i-create-a-speeder-chase-on-a-tiny-greenscreen.md) — shares relighting, gizmo, digital-matte-painting; that BTS case study used the channel's CA_Relight gizmo and Nuke map-painting/projection on the same kind of Iceland photogrammetry-scan terrain.
