---
title: A BETTER way to Color Grade in Nuke
source: YouTube
url: https://www.youtube.com/watch?v=fNxqXKuAr4A
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke (Indy / Commercial)"
version: "not specified — free 3rd-party gizmo (CA_HueQualifier2) by Compositing Academy, downloadable for Nuke Indy or Commercial licenses"
tags: [grading, color-management, gizmo, keying, compositing, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/a-better-way-to-color-grade-in-nuke/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# A BETTER way to Color Grade in Nuke

**Source:** [YouTube](https://www.youtube.com/watch?v=fNxqXKuAr4A)
**Author:** Compositing Academy
**Duration:** 5m18s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below. Condensed summary of the transcript (full timestamped version retained in git history at commit 3abf32c):

[0:00] Releasing the Hue Qualifier for Nuke — a highly targeted color-adjustment tool inspired by DaVinci Resolve's Hue Qualifier.
[0:31] The stock alternative in Nuke is the HSV tool, whose ranges are separate knobs that can't be adjusted together, and aren't visual.
[0:47] Demonstration problem: a mountain and sky share nearly the same Hue (only brightness/saturation differ), so a Hue keyer can't separate them — proven by plugging a Colorspace node (linear to HSL/HSV) and reading the red channel as Hue.
[1:40] Using the qualifier: Ctrl+Shift-drag to sample an average color, click Apply Sample to auto-populate the hue/saturation/luminance range graph, then drag range handles to expand/narrow.
[2:05] Add Range mode: sample a second, disjoint color and merge it into the existing key.
[2:37] Range-lock option keeps hue/sat/lum moving together for a cleaner key.
[2:54] Analyze Input button auto-switches SDR to HDR mode so sampled ranges still register values pushed above 1.0.
[3:45] Reiterates that a color sample targets hue AND brightness/saturation together — three "reds" can differ in brightness/saturation while sharing hue.
[4:06] Second example: qualify yellow-greens in a landscape shot, blur the resulting matte for a soft map, then cool/desaturate just that range while preserving other greens — fast secondary color push.
[5:09] Free download in the description for Nuke Indy or Nuke Commercial license holders.

---

## Captured Frames

- [0:06] tutorials/frames/a-better-way-to-color-grade-in-nuke/frame_000.jpg
- [1:14] tutorials/frames/a-better-way-to-color-grade-in-nuke/frame_001.jpg
- [1:40] tutorials/frames/a-better-way-to-color-grade-in-nuke/frame_002.jpg
- [2:13] tutorials/frames/a-better-way-to-color-grade-in-nuke/frame_003.jpg
- [2:47] tutorials/frames/a-better-way-to-color-grade-in-nuke/frame_004.jpg
- [3:10] tutorials/frames/a-better-way-to-color-grade-in-nuke/frame_005.jpg
- [4:20] tutorials/frames/a-better-way-to-color-grade-in-nuke/frame_006.jpg

---

## Structured Notes

### Core Technique
Introduces CA_HueQualifier2, a free Compositing Academy gizmo that ports DaVinci Resolve's visual Hue Qualifier workflow into Nuke — click-sample a color region, then adjust linked hue/saturation/luminance range sliders on a single visual graph to pull a targeted secondary key, instead of hand-tuning Nuke's native HSV tool's disconnected range knobs.

### Summary
The video opens by diagnosing why Nuke's stock HSV tool and a simple Hue keyer struggle on a mountain-vs-sky shot: plugging a Colorspace node set to HSL/HSV and inspecting the red (Hue) channel shows the mountain and sky share nearly the same hue — only brightness/saturation differ — so a pure hue key can't separate them, and HSV's individual range knobs aren't adjustable together. CA_HueQualifier2 fixes this with a Resolve-style single graph showing linked hue/saturation/luminance range bars: Ctrl+Shift-drag to sample an average color, click Apply Sample to auto-populate the ranges, then drag the range handles directly to expand/narrow the selection. An Add Range mode lets you sample a second, non-contiguous color and merge it into the existing key. A range-locking option keeps hue/sat/lum moving together for a cleaner key edge. For HDR footage (values pushed above 1.0), an Analyze Input button auto-switches the tool from SDR to HDR mode so the sampled ranges still register values above white. A second example demonstrates a practical grading use: qualifying and isolating yellow-greens in a landscape shot (blurring the resulting matte for a soft map) to cool the scene while preserving other greens — a fast secondary-color push rather than a full segmentation task.

### Key Steps
1. Insert the CA_HueQualifier2 gizmo on the shot; open its Qualifier panel.
2. Ctrl+Shift-drag in the viewer over the target color region to get an averaged sample.
3. Click Apply Sample — the hue/saturation/luminance range graph auto-populates and the resulting matte previews live.
4. Drag the range handles on the graph directly to expand or narrow the hue/sat/lum window (all editable on one visual plot, unlike stock HSV's separate knobs).
5. To add a second, disjoint color region to the same key: switch to Add Range mode, sample again, hit Apply Sample — the new range merges into the existing selection.
6. Optionally lock hue/saturation/luminance ranges together so they scale as one unit for a cleaner matte edge.
7. For bright/HDR plates (values above 1.0), click Analyze Input to switch the tool from SDR to HDR mode so range selection still tracks values above white (manual luminance-max override also available but rarely needed).
8. Use the resulting matte to drive a secondary grade (e.g. isolate yellow-greens, blur the matte for a softer map, then desaturate/cool only that range) while leaving the rest of the image's greens untouched.

### Nodes / Tools / Settings
- CA_HueQualifier2 — free Compositing Academy gizmo; Properties panel labeled "QUALIFIER"
- Panel controls seen: Apply Sample button, Add Range mode, hue/saturation/luminance linked range graph (wheel + bar sliders), range-lock toggle, Analyze Input (SDR/HDR mode switch)
- Comparison/diagnostic tool: Colorspace node set to convert linear to HSL/HSV, inspecting the red channel to visualize Hue directly (used to prove why a plain Hue keyer fails on the mountain/sky example)
- Stock Nuke tool referenced as the prior alternative: HSV tool (its ranges can't be adjusted together, no visual sampling)

### Difficulty
Intermediate — requires understanding HSV color theory and secondary-key workflows, but the tool itself is designed to be visual/intuitive.

### Foundry App & Version
Nuke (Indy or Commercial license — gizmo explicitly stated to work on both tiers); exact Nuke version not stated on-screen. CA_HueQualifier2 is a free third-party/house gizmo, not a native Nuke node.

### Tags
grading, color-management, gizmo, keying, compositing, intermediate

---

## Related Tutorials
- EASY TRICK: Improve your Color Grading skills (tutorials/easy-trick-improve-your-color-grading-skills.md) — shares grading, compositing; another Compositing Academy color-grading technique video.
- I Made VFX Relighting WAY Better in Nuke (tutorials/i-made-vfx-relighting-way-better-in-nuke.md) — shares gizmo, compositing; same channel's pattern of releasing free custom gizmos alongside a demo video.
