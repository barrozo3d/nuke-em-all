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


### Grading Highlights and Pools of Light | Nuke Compositing
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=F6Ru0K0PwZM
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)
- **Tags:** compositing, grading, relighting, digital-matte-painting, intermediate
- **Summary:** Theory/process preview from Compositing Academy's "Nuke 404: Advanced Grading and Relighting" course. Breaks specular highlight response into a "four layers of pinging" model per light pool — broad diffuse absorb, mid glossy scatter, hot mirror pings, and sparse far-field glints — hand-painted with a layered RotoPaint node over a Tokyo-alley photo to build a convincing night relight/matte painting.
- **File:** tutorials/grading-highlights-and-pools-of-light-nuke-compositing.md
- **Related:** Skill Up with Nuke | How To Think Like A Pro Compositor (`skill-up-with-nuke-how-to-think-like-a-pro-compositor.md`), Build Entire FX with ONE Pass - Nuke Tutorial (`build-entire-fx-with-one-pass---nuke-tutorial.md`) — shares `compositing`, `grading`.


### 360 Spherical LatLong Textures | Nuke Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ifsOs84Ps2g
- **Author:** Compositing Academy
- **App:** [PENDING]
- **Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/360-spherical-latlong-textures-nuke-tutorial.md


### Transform your FLAT Green Screen into Cinematic Lighting
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=7cYK2CKjp2k
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified (ACES OCIO config; consistent with Nuke 15.x-17.x)
- **Tags:** relighting, ai-tools, gizmo, compositing, roto, grading, intermediate
- **Summary:** Uses the Beeble/Bevel AI tool to derive a full PBR pass set (Albedo, Normal, Roughness, Specular, Metallic, Depth, roto) from ordinary green-screen footage, then relights it in Nuke via Bevel's plugin node (`PBRController` + `BevelEnvironmentLight`/Directional/Point lights). Also builds a free alternative using the community `ReflectionBuddy` gizmo fed the Bevel normals + an HDRI to create a steerable, per-material mirror reflection (sharp for eyes/metal, soft for cloth) so a CG explosion element reflects convincingly on the subject, finished with manual roto touch-ups to avoid an over-clean "plastic" relit look.
- **File:** tutorials/transform-your-flat-green-screen-into-cinematic-lighting.md
- **Related:** Grading Highlights and Pools of Light | Nuke Compositing (`grading-highlights-and-pools-of-light-nuke-compositing.md`), Physics of Light for VFX Artists [Updated] (`physics-of-light-for-vfx-artists-updated.md`) — shares `relighting`, `grading`.


### Physics of Light for VFX Artists [Updated]
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=goTeNehxrhY
- **Author:** Compositing Academy
- **App:** Cross-app theory (no software shown)
- **Version:** not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021)
- **Tags:** relighting, grading, digital-matte-painting, beginner
- **Summary:** Pure animated-diagram terminology primer (no software shown) distinguishing physicist vs. CG-artist vocabulary: specular/diffuse reflection maps to "glossiness" in CG; smooth surfaces give sharp mirror highlights, microscopic roughness scatters them into soft broad ones; color diffuse/absorption is a separate subsurface-scatter process giving a material its base color; specular highlights are view-dependent per the angle of incidence. Theory foundation for the channel's practical grading/relighting videos.
- **File:** tutorials/physics-of-light-for-vfx-artists-updated.md
- **Related:** Grading Highlights and Pools of Light | Nuke Compositing (`grading-highlights-and-pools-of-light-nuke-compositing.md`) — shares `relighting`, `grading`, `digital-matte-painting`.


### Nuke Tutorial | Keying with Math Expressions [Intermediate]
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=uEzjEizAi3o
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)
- **Tags:** keying, compositing, intermediate
- **Summary:** Pulls a clean single-hue isolation matte (saturated red tail-light glow) using an `Expression` node instead of a standard `Keyer` or manual channel-subtraction chain. Two formulas: `r-((g+b)/2)` (difference-from-average key) and an adjustable `r-g*control` variant driven by a custom user slider — the latter also useful for isolating on-set tracking markers of a strong saturated color.
- **File:** tutorials/nuke-tutorial-keying-with-math-expressions-intermediate.md


### Why your VFX Tracks aren't "Sticking" (and how to Fix it)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ntx0Tm4ZYds
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified
- **Tags:** tracking, camera-tracking, compositing, roto, gizmo, intermediate
- **Summary:** Diagnoses why a seemingly good 2D/planar track "slides" on hard edges — usually uncorrected lens distortion plus a shot-varying vignette, not a bad track. Shows the stabilize-and-invert diagnostic trick to reveal footage warp, prefers planar over single-point 2D tracking to reduce slip, hand-fixes remainders with the free `EyeTransform` gizmo, and manually roto-darkens frame edges over time to compensate for the vignette instead of trying to bake it into a static CG grade.
- **File:** tutorials/why-your-vfx-tracks-arent-sticking-and-how-to-fix-it.md
- **Related:** first entry tagged `tracking`/`camera-tracking` — future tracking tutorials should cross-link here.


### Nuke Tutorial | Compositing a Rainbow [Intermediate]
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=1lmyihzZHio
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)
- **Tags:** compositing, channels, procedural-texture, intermediate
- **Summary:** Builds a true full-spectrum rainbow procedurally via an HSV round-trip: a `Ramp` converted to HSV (`Colorspace`), its Value channel shuffled into Hue with Saturation/Value forced to 1 (`Shuffle`), then converted back to linear. Optionally bent into a circular rainbow with the Nukepedia `PolarDistort` gizmo, with `Grade` gamma controlling color order and `Crop` fixing bounding-box edge cases. Compares favorably to the built-in `Flare` "LG Rainbow" preset, which lacks the full color spectrum.
- **File:** tutorials/nuke-tutorial-compositing-a-rainbow-intermediate.md
- **Related:** Build Entire FX with ONE Pass - Nuke Tutorial (`build-entire-fx-with-one-pass---nuke-tutorial.md`) — shares `compositing`, `channels`, `procedural-texture`, `intermediate`.


### Create a Movie Quality Sci-Fi Laser Effect in Nuke
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=OJJ9hu6smqk
- **Author:** Compositing Academy
- **App:** [PENDING]
- **Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/create-a-movie-quality-sci-fi-laser-effect-in-nuke.md


### Create 3D Noise | Nuke Compositing
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=4uHLGGcQzzM
- **Author:** Compositing Academy
- **App:** [PENDING]
- **Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/create-3d-noise-nuke-compositing.md

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
