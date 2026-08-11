# Nuke'Em All — Tutorial & Knowledge Base Index

This is the skill's growing knowledge base, covering Nuke, NukeX, Nuke Studio, Mari, and Katana. Every ingested tutorial, article, and book excerpt is listed here.

**To add a tutorial:** say "ingest this: [URL]" and the skill will fetch, structure, and add it here automatically.
**To add a book chapter:** paste the content and say "ingest this chapter from [Book Title]".
**To search:** look for tags matching the technique or app you need.

### Skill Up with Nuke | How To Think Like A Pro Compositor
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=tLQfGjHpsd8
- **Author:** Foundry
- **App:** Nuke + Nuke Studio
- **Version:** not specified on screen (ACES 1.1 OCIO config consistent with recent Nuke 15.x-17.x)
- **Tags:** compositing, nuke-studio, color-management, ocio, tracking, keying, roto, grading, defocus, edge-extend, chromatic-aberration, editorial, conform, beginner, intermediate
- **Summary:** Official Foundry video (compositor Peter Timberlake) teaching a five-skill problem-solving framework rather than one technique — use what you know, Google relentlessly, ask forums/Discord, read the information already in the plate, and critique your own work relentlessly — applied live to a real multi-element shot build using Timberlake's free practice plates and the community Nuke Survival Toolkit gizmo pack. Covers Nuke Studio's token-based export/re-import workflow (Build Track from Export Structure), OCIO/ACES 1.1 setup, Tracker-based stabilization, a reversible white-balance "neutral grade" trick, Luma-key sky replacement with reference-driven color matching, and CG-to-plate matching (shadow contrast via pre-Grade desaturation, focus matching via an inverted defocus control mask, Lens Edge Extend for key-edge cleanup, and chromatic-aberration matching). Strong general-purpose compositing methodology, not just a node recipe.
- **File:** tutorials/skill-up-with-nuke-how-to-think-like-a-pro-compositor.md
- **Related:** Build Entire FX with ONE Pass - Nuke Tutorial (`build-entire-fx-with-one-pass---nuke-tutorial.md`) — shares `compositing`, `grading`, and the same Nuke Survival Toolkit gizmo pack.


### Build Entire FX with ONE Pass - Nuke Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=WBqp4UbqPJ0
- **Author:** Voxyde VFX
- **App:** Nuke / NukeX
- **Version:** not specified
- **Tags:** compositing, cryptomatte, st-map, merge, channels, aovs, grading, gizmo, procedural-texture, intermediate
- **Summary:** Uses the World Position AOV alone to drive procedural texture breakup (fake UVs via STMap + world-space X/Z), region masking (height bands, Cryptomatte), faked indirect bounce, and a full pulsating expanding-ring FX layer around a logo (radial distance matte → repeating ramp → animated offset → god rays/glow), plus bonus scanline/waffle patterns — all in comp, no re-render needed.
- **File:** tutorials/build-entire-fx-with-one-pass---nuke-tutorial.md
- **Related:** Skill Up with Nuke | How To Think Like A Pro Compositor (`skill-up-with-nuke-how-to-think-like-a-pro-compositor.md`) — shares `compositing`, `grading`, and the same Nuke Survival Toolkit gizmo pack.


### [CROSS-REFERENCE ONLY] Fire FX in Houdini, Blender and Nuke
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=NRM-e4ECT7c
- **Author:** Anton Dann
- **App:** Not specified (implied Nuke comp step)
- **Tags:** compositing, aovs, cross-platform-reference
- **Summary:** Cross-platform VFX breakdown (Blender camera tracking → Houdini fire sim/render → Nuke comp). The Nuke-side technique is a fast AOV beauty rebuild (volume pass split sun/dome, fire AOV, scatter pass, holdouts from a Solaris background-plate LOP) placing simulated fire over live-action footage — not shown in step-by-step detail. The bulk of the technical content is Houdini simulation/rendering, so the full extraction lives in the **houdini-wand** skill, not here.
- **Full extraction:** `houdini-wand/tutorials/fire-fx-in-houdini-blender-and-nuke.md` (https://github.com/barrozo3d/houdini-wand/blob/master/tutorials/fire-fx-in-houdini-blender-and-nuke.md)
- **⚠ Do not re-ingest this URL in nuke-em-all** — this stub exists only so this index surfaces the tutorial by search; ingesting it here would fork the content. If new Nuke-specific detail is found, add it to the canonical file in houdini-wand instead.

---

## Tag Reference

### By App
`#nuke` `#nukex` `#nuke-studio` `#hiero` `#mari` `#katana`

### By Compositing Technique
`#compositing` `#keying` `#roto` `#rotopaint` `#tracking` `#camera-tracking`
`#3d-system` `#deep-compositing` `#cryptomatte` `#st-map` `#merge` `#channels` `#aovs`
`#defocus` `#gaussian-splats` `#field-nodes`

### By Color/Pipeline
`#color-management` `#ocio` `#grading`

### By Scripting
`#python-scripting` `#gizmo` `#group` `#copycat`

### By Nuke Studio / Hiero
`#editorial` `#conform` `#review`

### By Mari
`#mari-texturing` `#udim` `#projection` `#procedural-texture` `#baking`

### By Katana
`#scenegraph` `#nodegraph` `#macro` `#lookdev` `#lighting` `#usd` `#cel`

### By Level
`#beginner` `#intermediate` `#advanced` `#expert`

### By Version
`#nuke-16` `#nuke-17` `#mari-7` `#mari-8` `#katana-8` `#katana-9`

### By Source Type
`#book` `#youtube` `#article` `#foundry-docs`
