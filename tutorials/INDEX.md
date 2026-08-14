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
- **App:** Nuke
- **Version:** Nuke 13.x (13.1/13.2 — exact 2022 point-release not stated on screen; Classic 3D system only, predates the 14.0-beta USD 3D overhaul)
- **Tags:** compositing, 3d-system, digital-matte-painting, roto, rotopaint, intermediate
- **Summary:** Converts a flat photo (or CG 360° render) into a seamless lat-long/equirectangular sky texture two ways — a Nukepedia `PolarDistort` gizmo patched with Roto/Crop reorganization, and a cleaner built-in `SphericalTransform` fisheye round-trip (rotate 90° to center the pole, patch, convert back) — plus a seam fix via `Offset` + `RotoPaint`, previewed live with a lat-long→rectilinear `SphericalTransform` (no Sphere/ScanlineRender needed). Closes with a production VR/game example: checking a nebula sky matte-painted onto a 360°-rendered CG dome.
- **File:** tutorials/360-spherical-latlong-textures-nuke-tutorial.md
- **Related:** Grading Highlights and Pools of Light | Nuke Compositing (`grading-highlights-and-pools-of-light-nuke-compositing.md`) — shares `compositing`, `digital-matte-painting`, `intermediate`.


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
- **App:** Nuke
- **Version:** not specified
- **Tags:** compositing, particles, gizmo, procedural-texture, 3d-system, digital-matte-painting, advanced
- **Summary:** Builds a fully art-directable sci-fi laser-scan reveal with no simulation software: hand-animated `RotoPaint` stroke alphas over CG rock crevices, reprojected through a static camera onto the geometry, masked against a secondary procedural pattern (`HexFlow`, `ProjectionBuddy` gizmo on P-channel data) for internal detail, plus god rays and re-projection back into the CG renderer (and Blender) for accurate reflections/light contamination. Also documents the author's rejected look-dev experiments (UV-projected grids, P-noise edge detection, the free `PScatter` gizmo) as a case study in effect design iteration.
- **File:** tutorials/create-a-movie-quality-sci-fi-laser-effect-in-nuke.md
- **Related:** Build Entire FX with ONE Pass - Nuke Tutorial (`build-entire-fx-with-one-pass---nuke-tutorial.md`) — shares `procedural-texture`, `gizmo`, P-channel/position-data driven effects.


### Create 3D Noise | Nuke Compositing
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=4uHLGGcQzzM
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)
- **Tags:** compositing, channels, aovs, procedural-texture, intermediate
- **Summary:** Drives the `Expression` node's `noise(R,G,B)` function from a CG position pass (`ScanlineRender` Shader tab surface-point output, channel `P`) so the resulting noise pattern is locked to the object's surface in 3D space rather than sliding in screen space. A custom `scale` slider controls frequency; a `Grade` node (Black Clamp unchecked — position data goes negative) with per-channel gain gives independent X/Y/Z axis scaling. Practical demo: adds extra water-drip detail/highlights with a faked 1px-offset drop-shadow for pseudo-3D relief on a CG car's wheels.
- **File:** tutorials/create-3d-noise-nuke-compositing.md
- **Related:** Build Entire FX with ONE Pass - Nuke Tutorial (`build-entire-fx-with-one-pass---nuke-tutorial.md`), Nuke Tutorial | Compositing a Rainbow [Intermediate] (`nuke-tutorial-compositing-a-rainbow-intermediate.md`) — shares `compositing`, `channels`, `procedural-texture`, `intermediate`.


### This Forgotten VFX Trick Is Still Shockingly Effective
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=8yOyb0Uyq6s
- **Author:** Compositing Academy
- **App:** Nuke / NukeX
- **Version:** not specified
- **Tags:** 3d-system, compositing, tracking, roto, cryptomatte, digital-matte-painting, intermediate
- **Summary:** Applies the classic video-game "sprite card" trick (2D texture on a single 3D polygon, convincing up to ~70-90° viewing angle) to merge a practical saliva element onto a CG dragon's mouth via a tracked `Card3D`/`ScanlineRender` card, instead of simulating saliva in CG. Covers aspect-ratio matching, UV flip/flop/turn correction, RotoPaint stencil masking, extending a too-short element with `Retime` in motion/frame mode (subtle reverse-jiggle), and — the key problem-solving beat — abandoning the 3D card system for the handful of frames where the angle breaks the illusion, hand 2D-tracking the source footage directly instead.
- **File:** tutorials/this-forgotten-vfx-trick-is-still-shockingly-effective.md
- **Related:** Nuke Compositing Technique | Card3D + PixelsToPos [Beginners] (`nuke-compositing-technique-card3d-pixelstopos-beginners.md`) — shares `3d-system`, `camera-tracking`, the Card3D/ScanlineRender sprite-card technique.


### Re-lighting Real Footage | Nuke Compositing [Advanced]
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=VYjmvB6d9NA
- **Author:** Compositing Academy
- **App:** Nuke / NukeX (3D camera tracking + Real Light node require NukeX)
- **Version:** not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)
- **Tags:** relighting, 3d-system, camera-tracking, channels, aovs, digital-matte-painting, advanced
- **Summary:** Derives synthetic depth/position/normal utility passes from live-action footage via a solved 3D camera + `DepthGenerator` (works best with high parallax), then uses them for three techniques: fog (inverted/graded depth pass as a haze mask), position-based selection (a Nukepedia 3D-position-picker samples a point in the position-pass image to generate an alpha that sticks to that surface point across the whole shot, no roto needed), and relighting (`Shuffle` copies the normals pass into the main stream, feeding a `RealLight` node with Material/Camera/Light for a fake golden-hour rim light). Utility passes must be written at 32-bit float with no compression to avoid data corruption.
- **File:** tutorials/re-lighting-real-footage-nuke-compositing-advanced.md
- **Related:** Grading Highlights and Pools of Light | Nuke Compositing (`grading-highlights-and-pools-of-light-nuke-compositing.md`), Physics of Light for VFX Artists [Updated] (`physics-of-light-for-vfx-artists-updated.md`) — shares `relighting`; Create 3D Noise | Nuke Compositing (`create-3d-noise-nuke-compositing.md`) — shares `channels`, `aovs`.


### Nobody's Ever Made VFX This Way (New Tech)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=3d9ycMKf65U
- **Author:** Compositing Academy
- **App:** Nuke (mentioned only — final compositing pass not shown on screen)
- **Version:** not specified
- **Tags:** virtual-production, compositing, camera-tracking, gaussian-splats, digital-matte-painting, intermediate
- **Summary:** Behind-the-scenes pipeline case study (not a node tutorial): a CG dragon (iCandy XYZ) is shot on location in an Icelandic cave using Lightcraft Jet Set's real-time phone-based AR camera tracking, a photogrammetry cave reconstruction built from crowd-sourced tourist photos (since the site couldn't be pre-scanned), and an XGrids handheld LiDAR scanner producing a dense point cloud/Gaussian splat for track refinement and lighting reference. Nuke is named as the finishing/compositing tool but not demonstrated on screen.
- **File:** tutorials/nobodys-ever-made-vfx-this-way-new-tech.md
- **Related:** First entry tagged `virtual-production`/`gaussian-splats` — cross-reference against Nuke 17.0/17.1's native Gaussian Splat toolset (`references/release-notes-nuke-17.0.md`, `release-notes-nuke-17.1.md`). Can I Create a Speeder Chase on a TINY Greenscreen? (`can-i-create-a-speeder-chase-on-a-tiny-greenscreen.md`) — shares `virtual-production`, `compositing`, BTS pipeline-case-study format.


### Preserve Quality | Projections in Nuke
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=8Aki1VR_tX8
- **Author:** Compositing Academy
- **App:** Nuke / NukeX (3D system for projections)
- **Version:** not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)
- **Tags:** 3d-system, rotopaint, roto, compositing, intermediate
- **Summary:** Two clean-plate-projection habits: (1) don't re-project the whole frame through undistort→project→re-distort — paint only the bad area with `RotoPaint`, enable its easy-to-miss output-mask dropdown (`RGBA.alpha`) so brushstrokes carry alpha, then `Premult` to isolate just that patch before projecting, preserving quality everywhere else; (2) switch `LensDistort`/`ScanlineRender`/re-distort filtering from default Cubic to a sharper filter to reduce cumulative resample softening.
- **File:** tutorials/preserve-quality-projections-in-nuke.md


### Mixed Medium VFX P1 | Blender, Nuke, Ai, Embergen, VR Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=2V7eYe8D3nY
- **Author:** Compositing Academy
- **App:** Nuke (cross-platform with Blender + AI upscaling; EmberGen appears in Part 2, not here)
- **Version:** Nuke 13.x (13.1/13.2 — exact 2022 point-release not stated; Classic 3D system only)
- **Tags:** compositing, 3d-system, procedural-texture, gizmo, ai-tools, digital-matte-painting, advanced
- **Summary:** Experimental "2D→3D→2D→3D" pipeline: reverse-engineers an AI concept image into Nuke procedural textures (`CellNoise`, `Glass` gizmos), displaces them onto Blender geometry and renders in Cycles, then re-imports that render into Nuke to abstract further via tiling + `PolarDistort` into radial "eye" patterns, re-projects onto a 3D Cylinder for an animated fractal element, and finishes with targeted-highlight grading plus a Topaz Gigapixel AI-upscale pass to recover detail lost from repeated resampling. Part 1 of a two-part "Stormy Crystal Skull" project.
- **File:** tutorials/mixed-medium-vfx-p1-blender-nuke-ai-embergen-vr-tutorial.md
- **Related:** Stormy Crystal Skull Part 2 (`stormy-crystal-skull-nuke-blender-ai-embergen-mixed-vfx-medium-part-2.md`) — direct continuation; 360 Spherical LatLong Textures | Nuke Tutorial (`360-spherical-latlong-textures-nuke-tutorial.md`) — shares the `PolarDistort` gizmo used for a different purpose.


### How I Made a FULL Star Wars Cinematic from JUST One Screenshot
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=6hArU1CgJUA
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified
- **Tags:** 3d-system, compositing, gizmo, motion-graphics, digital-matte-painting, roto, advanced
- **Summary:** Builds a holographic "activation" transformation on a Blender-rigged Sith Trooper (Alembic + camera exported into Nuke) by layering multiple animated procedural patterns from the paid `ScreenFX` plugin (grid drips, "Polyflow" path-traveling shapes, dot patterns), projected onto the 3D model via `UVProject`/`Axis` so the effect follows the actual geometry, combined with `EdgeDetect`-on-normals edge highlights, faked interactive glow, and glitchy edge break-up for a concept-art-matching red/black hologram wipe.
- **File:** tutorials/how-i-made-a-full-star-wars-cinematic-from-just-one-screenshot.md
- **Related:** Create a Movie Quality Sci-Fi Laser Effect in Nuke (`create-a-movie-quality-sci-fi-laser-effect-in-nuke.md`) — shares `3d-system`, UV/position-projected reveal-pattern technique.


### Ray Render in Nuke Tutorial | Compositing 3d Reflections
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=UQlTyaVKog4
- **Author:** Compositing Academy
- **App:** Nuke / NukeX (RayRender, AmbientOcclusion, camera-tracked 3D projections)
- **Version:** not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)
- **Tags:** 3d-system, camera-tracking, digital-matte-painting, advanced
- **Summary:** True ray-traced 3D reflections built entirely in Nuke via `RayRender` (not `ScanlineRender`, which can't ray-trace). A solved 3D camera track projects live footage onto rough proxy `Cube`/`Card` geometry hand-built to match nearby real objects (bench, wall), giving spatially-accurate reflections; distant elements use either a flat graded sky photo or a true 360° photo mapped onto a surrounding sphere. A separate `ScanlineRender` alpha isolates just the reflective object for masking, and a RayRender-based `AmbientOcclusion` pass adds contact shadow. Also covers a simplified flat-card "window reflection" variant.
- **File:** tutorials/ray-render-in-nuke-tutorial-compositing-3d-reflections.md
- **Related:** Re-lighting Real Footage | Nuke Compositing [Advanced] (`re-lighting-real-footage-nuke-compositing-advanced.md`) — shares `3d-system`, `camera-tracking`, `digital-matte-painting`, `advanced`; Preserve Quality | Projections in Nuke (`preserve-quality-projections-in-nuke.md`) — shares `3d-system`.


### How to use NUKE to Composite Blender Renders
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=peygC-ZxaP8
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified
- **Tags:** aovs, cryptomatte, channels, color-management, grading, compositing, intermediate
- **Summary:** Free one-click Blender-to-Nuke plugin auto-wires denoised, correctly-named AOV/Cryptomatte exports from Blender's compositor, paired with a Nuke "CG Compositing Template" that unpacks diffuse/specular/transmission/indirect-lighting so each is independently gradeable (HueCorrect on diffuse color, masked Grade on glossy indirect via a Cryptomatte object matte, direct object recoloring via Cryptomatte). Critical caveat: Blender denoises AOV layers independently, so color-type passes must be re-premultiplied before recombining or the result gets dark/damaged edges versus the true beauty render.
- **File:** tutorials/how-to-use-nuke-to-composite-blender-renders.md
- **Related:** Build Entire FX with ONE Pass - Nuke Tutorial (`build-entire-fx-with-one-pass---nuke-tutorial.md`) — shares `cryptomatte`, `aovs`.


### Stormy Crystal Skull | Nuke, Blender, Ai, Embergen, Mixed VFX Medium Part 2
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=prhQhQ5AnNM
- **Author:** Compositing Academy
- **App:** Nuke (cross-platform: EmberGen storm sim + Blender/Adobe Medium CG asset; compositing techniques are pure Nuke)
- **Version:** Nuke 13.x (13.1/13.2 — exact 2022 point-release not stated; Classic 3D system only)
- **Tags:** compositing, merge, channels, st-map, gizmo, grading, fx-simulation, lighting, advanced
- **Summary:** Part 2 of the Stormy Crystal Skull project — the CG side is fast (EmberGen storm sim into an FBX skull collider, Blender VDB import, Adobe-Medium-sculpted interior cracks), but the real technique is doing all art direction in Nuke comp instead of 3D: two un-animated storm-light renders `Plus`-combined and independently flickered via Grade + the Nukepedia Expression Generator gizmo, lightning-pattern footage `STMap`-projected onto the skull's UV pass then masked to only the storm's bright regions (+ hand-painted RotoPaint for randomness) so it reads as happening *inside* the volume, a Glass-node edge distortion using the render's own alpha as displacement, PMatte-driven eye brightening, log-space sharpening, and a `VolumeRays` "Copy to Group" trick to preserve overscan.
- **File:** tutorials/stormy-crystal-skull-nuke-blender-ai-embergen-mixed-vfx-medium-part-2.md
- **Related:** Mixed Medium VFX P1 (`mixed-medium-vfx-p1-blender-nuke-ai-embergen-vr-tutorial.md`) — direct prequel; Build Entire FX with ONE Pass - Nuke Tutorial (`build-entire-fx-with-one-pass---nuke-tutorial.md`) — shares `compositing`, `merge`, `channels` and the position-pass-masking philosophy.


### Nuke Compositing Artistic Basics (1/8): Roles of Production
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=cQV6c291fBU
- **Author:** Compositing Academy
- **App:** Cross-app theory (no software shown)
- **Version:** not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021)
- **Tags:** compositing, beginner
- **Summary:** Part 1/8 of the "Artistic Basics" series. No software shown — whiteboard overview of VFX studio production roles (Match Move, Effects, Texturing/Shading, Rigging, Animation, Lighting, Editorial) and where the compositor sits at the end of the pipeline, reconciling mismatched assets handed off from every department. Frames the rest of the series' simulated production hand-off (plate, elements, lit CG car, tracked ground/camera).
- **File:** tutorials/nuke-compositing-artistic-basics-18-roles-of-production.md
- **Related:** All 8 parts of this series cross-link to each other — see Part 2/8 (`nuke-compositing-artistic-basics-28-3-point-lighting.md`) through Part 8/8 (`nuke-compositing-artistic-basics-88-camera-artifacts.md`).


### How I Use Compositing to Skip THOUSANDS of Hours Rendering
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=PNE9YMD64xM
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified
- **Tags:** compositing, 3d-system, digital-matte-painting, denoise, grading, gizmo, intermediate
- **Summary:** Six render-cost-saving compositing techniques: match real flicker to CG lights via `CurveTool` data copied into a desaturated multiply `Constant`; fake small bokeh lights with eroded `Checkerboard` + `Noise` (or the `ScreenFX` plugin); half-res render defocused elements; substitute 2.5D card projections for distant/nodal-pan-only 3D elements (single frame reused); denoise flickering specular by projecting the render back onto geometry and blending frames; mix a slow path-traced hero pass with a fast real-time-engine pass for cheap extra detail on secondary defocused elements.
- **File:** tutorials/how-i-use-compositing-to-skip-thousands-of-hours-rendering.md
- **Related:** How to DENOISE your CG in POST | Blender & Nuke Tutorial (`how-to-denoise-your-cg-in-post-blender-nuke-tutorial.md`) — covers technique 4 in full. Shares `3d-system`/`ScreenFX` with Create a Movie Quality Sci-Fi Laser Effect in Nuke and How I Made a FULL Star Wars Cinematic from JUST One Screenshot.


### Nuke Compositing Artistic Basics (2/8): 3 Point Lighting
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=EdYZwn8Kwv4
- **Author:** Compositing Academy
- **App:** Cross-app theory (no software shown)
- **Version:** not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021)
- **Tags:** relighting, grading, beginner
- **Summary:** Part 2/8 of the "Artistic Basics" series. Defines key/fill/rim lighting vocabulary used throughout the presenter's grading/compositing notes ("bring up the key," "too much fill") via a labeled 3D-viewport sphere diagram — key is the brightest front light, fill softens shadows (can be bounce light, not necessarily a real light), rim creates a silhouette edge from behind.
- **File:** tutorials/nuke-compositing-artistic-basics-28-3-point-lighting.md
- **Related:** All 8 parts of this series cross-link to each other — see Part 1/8 (`nuke-compositing-artistic-basics-18-roles-of-production.md`) and the rest of the series files.


### Nuke Compositing Artistic Basics (3/8): Exposure
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=xFUOuK3lFro
- **Author:** Compositing Academy
- **App:** Nuke (theory-focused)
- **Version:** not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)
- **Tags:** grading, digital-matte-painting, beginner
- **Summary:** Part 3/8 of the "Artistic Basics" series. Explains why a real camera exposure can never show full highlight AND full shadow detail at once (unlike HDR, which merges bracketed exposures and reads as unrealistic for video), and why grading CG/matte-paint elements to retain "impossible" full-range detail is the most common tell that a shot looks fake — especially in sky replacements.
- **File:** tutorials/nuke-compositing-artistic-basics-38-exposure.md
- **Related:** All 8 parts of this series cross-link to each other — see Part 1/8 (`nuke-compositing-artistic-basics-18-roles-of-production.md`) and the rest of the series files.


### Nuke Compositing Artistic Basics (4/8): Shadows
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=SRgXQPPzVc8
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)
- **Tags:** relighting, grading, compositing, beginner
- **Summary:** Part 4/8 of the "Artistic Basics" series. Shadow attenuation physics (object-to-surface distance and light-source size both govern hard vs. soft shadow edges) demonstrated in a live 3D scene, plus black-point matching — sampling the darkest tone in the plate adjacent to each CG element and grading its black point to match, since atmospheric distance and light contamination mean pure black rarely exists in real footage.
- **File:** tutorials/nuke-compositing-artistic-basics-48-shadows.md
- **Related:** All 8 parts of this series cross-link to each other — see Part 1/8 (`nuke-compositing-artistic-basics-18-roles-of-production.md`) and the rest of the series files.


### Nuke Compositing Artistic Basics (5/8) - Reflections and Fresnel
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=YeGZP5xlBGg
- **Author:** Compositing Academy
- **App:** Nuke (theory-focused; real reference footage)
- **Version:** not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)
- **Tags:** relighting, digital-matte-painting, beginner
- **Summary:** Part 5/8 of the "Artistic Basics" series. The Fresnel effect (glancing-angle surfaces reflect far more strongly than surfaces viewed straight-on) demonstrated live with real puddle/wave footage, plus the CG-specific vocabulary split between "specular" (small bright highlight glints) and "reflection" (the broader base mirror image) — both needed to judge per-angle reflectivity on car panels/windows.
- **File:** tutorials/nuke-compositing-artistic-basics-58---reflections-and-fresnel.md
- **Related:** All 8 parts of this series cross-link to each other — see Part 1/8 (`nuke-compositing-artistic-basics-18-roles-of-production.md`) and the rest of the series files.


### Rotoscoping in Nuke Tutorial | 5 Beginner Tips
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=rBPz0LL0yF0
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not version-specific (2022 upload, Nuke 13.1/13.2 window)
- **Tags:** roto, tracking, camera-tracking, compositing, beginner
- **Summary:** Five methodology tips for faster/more stable RotoPaint work: place keyframes at real motion-direction changes rather than fixed intervals; separate shapes by object/parallax plane and keep points anchored to fixed features instead of letting them slide; stabilize shaky footage with a baked Tracker (Stabilize → Roto → Match-Move chain) so the roto is drawn against a near-static plate; decompose complex silhouettes into primary + secondary shapes; and animate jointed/rotating parts via each shape's pivot point instead of hand-keying every control point.
- **File:** tutorials/rotoscoping-in-nuke-tutorial-5-beginner-tips.md
- **Related:** Why your VFX Tracks aren't "Sticking" (and how to Fix it) (`why-your-vfx-tracks-arent-sticking-and-how-to-fix-it.md`) — shares `tracking`, `camera-tracking`, `compositing`, `roto`; How SMART is State of the Art A.I Rotoscoping? (`how-smart-is-state-of-the-art-ai-rotoscoping.md`) — shares `roto`, `tracking`, `compositing` (manual fundamentals vs. AI-assisted follow-up).


### 2 Expert VFX Tips to PERFECTLY Blend CG
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=DFb9dnOWTxw
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified
- **Tags:** relighting, grading, roto, compositing, digital-matte-painting, intermediate
- **Summary:** Two CG-integration techniques on a real tabletop shot with a hidden CG cup/coins: "paint with light" — roto shapes tracked onto a single nodal-pan CG frame for layered contact shadows, `RotateNormals`-driven directional highlight mattes, desaturated highlights, faked reflections from real photo reference, and luma-keyed (not flat-brightened) surface-texture detail — and "finding connection points," a disciplined scan-and-compare methodology across shadow softness/DOF/exposure/hue/texture, while guarding against the trap of matching brightness 1:1 between materials that legitimately reflect light differently (a dark book vs. a bright table).
- **File:** tutorials/2-expert-vfx-tips-to-perfectly-blend-cg.md
- **Related:** Transform your FLAT Green Screen into Cinematic Lighting (`transform-your-flat-green-screen-into-cinematic-lighting.md`) — shares normals-derived directional relighting mattes. How I Use Compositing to Skip THOUSANDS of Hours Rendering (`how-i-use-compositing-to-skip-thousands-of-hours-rendering.md`) — shares the nodal-pan single-frame render optimization.


### Nuke Compositing Artistic Basics (6/8): Whitepoint and white balance
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=VlA6a0IK-Ds
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)
- **Tags:** grading, color-management, compositing, beginner
- **Summary:** Part 6/8 of the "Artistic Basics" series. Distinguishes the two causes of a shot's white point — light color vs. camera white balance — and demonstrates the core CG-matching workflow: sample a known-white reference point in the plate near a CG element, and grade the element's white to match it (plus layering in local colored-light contamination separately if a practical light is present).
- **File:** tutorials/nuke-compositing-artistic-basics-68-whitepoint-and-white-balance.md
- **Related:** All 8 parts of this series cross-link to each other — see Part 1/8 (`nuke-compositing-artistic-basics-18-roles-of-production.md`) and the rest of the series files.


### Nuke Compositing Artistic Basics (7/8): Glows
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=FFutBgMZBLo
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)
- **Tags:** compositing, grading, digital-matte-painting, beginner
- **Summary:** Part 7/8 of the "Artistic Basics" series. Distinguishes bloom from lens diffusion, establishes that glows happen optically last (in the lens/eye) so foreground objects must never occlude them, and shows two ways to wrap a glow around a foreground object: a `Light Wrap` node, or a manual `Keyer` (luminance key) → `Premult` → `Exponential Glow` → `Plus` build derived from the already-occluded beauty.
- **File:** tutorials/nuke-compositing-artistic-basics-78-glows.md
- **Related:** All 8 parts of this series cross-link to each other — see Part 1/8 (`nuke-compositing-artistic-basics-18-roles-of-production.md`) and the rest of the series files.


### Nuke Compositing Artistic Basics (8/8): Camera Artifacts
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=bmwOCLwiYM0
- **Author:** Compositing Academy
- **App:** Nuke (theory-focused; real reference footage)
- **Version:** not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)
- **Tags:** compositing, defocus, digital-matte-painting, beginner
- **Summary:** Part 8/8 (series finale) of the "Artistic Basics" series. Trains the eye to spot chromatic aberration (colored fringing on highlight edges, matched from the real plate), camera defocus (sharpness falling off with distance, deferred to a future depth-of-field lesson), and bokeh (lens-specific out-of-focus highlight shapes) — all to be replicated on inserted CG elements.
- **File:** tutorials/nuke-compositing-artistic-basics-88-camera-artifacts.md
- **Related:** All 8 parts of this series cross-link to each other — see Part 1/8 (`nuke-compositing-artistic-basics-18-roles-of-production.md`) and the rest of the series files. Also shares `defocus` with Skill Up with Nuke | How To Think Like A Pro Compositor (`skill-up-with-nuke-how-to-think-like-a-pro-compositor.md`).


### How I Faked a $200M Movie Scene (In my DRIVEWAY!)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=dbkOqzRvWKY
- **Author:** Compositing Academy
- **App:** Nuke (mentioned only — compositing node work not shown on screen)
- **Version:** not specified
- **Tags:** compositing, roto, digital-matte-painting, camera-tracking, intermediate
- **Summary:** BTS production-planning case study for a low-budget Templar VFX set extension (no green screen, no set, driveway shoot). Key transferable technique: previs-driven drone camera placement (matched real lens focal length in Blender + laser-measured altitude) chosen specifically so the walking actor's silhouette never breaks the horizon — meaning a simple projected roto rectangle substitutes for full character rotoscoping, controlling compositing cost before Nuke work even starts. The actual Nuke finishing pass (color corrections, 3D CG grades, lens simulation) is summarized verbally only, not shown on screen.
- **File:** tutorials/how-i-faked-a-200m-movie-scene-in-my-driveway.md
- **Related:** Nobody's Ever Made VFX This Way (New Tech) (`nobodys-ever-made-vfx-this-way-new-tech.md`) — shares the BTS/pipeline-case-study format (Nuke mentioned but not demonstrated).


### A new way to design VFX | Virtual Reality | Gravity Sketch + Nuke Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=wEHiUNE66fk
- **Author:** Compositing Academy
- **App:** Nuke (cross-platform with Gravity Sketch, a third-party VR modeling app)
- **Version:** Nuke 13.x (13.1/13.2 — exact 2022 point-release not stated)
- **Tags:** compositing, procedural-texture, gizmo, motion-graphics, intermediate
- **Summary:** Bridges 2D procedural texture design in Nuke (a bidirectional GodRay gizmo + tiling + `PolarDistort` for spectrum-mapped rainbow/energy patterns) with VR-native NURBS modeling in Gravity Sketch — export a static frame of an animated texture as a VR reference material, sculpt geometry around it in true stereo 3D using Revolve/Surface/polar-symmetry Stroke tools (impractical to loft in Nuke, Houdini, or Maya), layer multiple materials for cheap parallax, then bring the geometry back into Nuke to reapply the *original animated* texture to its UVs.
- **File:** tutorials/a-new-way-to-design-vfx-virtual-reality-gravity-sketch-nuke-tutorial.md
- **Related:** 360 Spherical LatLong Textures (`360-spherical-latlong-textures-nuke-tutorial.md`), Mixed Medium VFX P1 (`mixed-medium-vfx-p1-blender-nuke-ai-embergen-vr-tutorial.md`) — share the `PolarDistort` gizmo and/or the "texture in Nuke → geometry in another tool → back to Nuke" pipeline shape.


### This ONE Step Makes CG Look Cinematic (Most Artists Skip It)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=twEVqozvpMk
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified
- **Tags:** aovs, grading, compositing, roto, intermediate
- **Summary:** Explains the CG-compositing step most beginners skip between lighting render and color grading: engineering "first read/second read" (where the eye lands first/second) by selectively boosting contrast on Light Groups (full per-light-source recombinations, distinct from individual AOVs) isolated with tracked 3D position mattes — brightening a character's face away from a blending gun silhouette, adding secondary contrast points along the intended eye path, and placing a deliberate eye-light reflection in sunglasses so they read as eyes.
- **File:** tutorials/this-one-step-makes-cg-look-cinematic-most-artists-skip-it.md
- **Related:** How to use NUKE to Composite Blender Renders (`how-to-use-nuke-to-composite-blender-renders.md`) — shares AOV/light-component selective grading. 2 Expert VFX Tips to PERFECTLY Blend CG (`2-expert-vfx-tips-to-perfectly-blend-cg.md`) — shares position-matte-driven targeted highlight technique.


### How to DENOISE your CG in POST | Blender & Nuke Tutorial
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=uReRex8xPqs
- **Author:** Compositing Academy
- **App:** Nuke (cross-platform: Blender is the source of the CG render being denoised; the technique itself is pure Nuke)
- **Version:** Nuke 13.x (13.1/13.2 — exact 2022 point-release not stated); Classic 3D system only
- **Tags:** denoise, projection, compositing, grading, advanced
- **Summary:** Removes render noise from a glossy CG element in post instead of re-rendering with more samples: `Project3D` the live render onto its own scene geometry, flatten to UV space (factors out camera/geometry motion), then either `TimeEcho` (frame-average) small high-frequency noise, or for larger low-frequency blotches that also carry real lighting change, TimeEcho + manually frame-hold two clean "key" frames and `Dissolve`/crossfade between them with animated timing — then project the cleaned UV-space result back through the original camera. Also covers the paid Neat Video ReduceNoise plugin as a strong single-pass alternative, plus a bonus tip: render a plain ramp through the same geometry once as a 2D grade/lookup map so later color tweaks skip re-touching the heavy 3D scene.
- **File:** tutorials/how-to-denoise-your-cg-in-post-blender-nuke-tutorial.md
- **Related:** How I Use Compositing to Skip THOUSANDS of Hours Rendering (`how-i-use-compositing-to-skip-thousands-of-hours-rendering.md`) — that video cites this one as covering its "technique 4" in full; shares `denoise`, `compositing`, `3d-system`/`projection`.


### Goodbye After Effects!  2D Motion Graphics in Nuke!
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=QRAsWDehxhA
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified
- **Tags:** motion-graphics, gizmo, compositing, 3d-system, digital-matte-painting, intermediate
- **Summary:** Tour of the `ScreenFX` plugin's GPU-accelerated node library for building 2D motion graphics (glitches, HUD/hologram/CRT effects, transitions) directly in Nuke instead of After Effects: `PolyFlow` shape generator (rain-offset fade animation, ID-pass-style color modes), `Warp Bar` + `Blocky Lines` combined into a 3-layer retro-TV static effect, `JitterDuplicate` for teleport/glitch jumps (replaces a manual Transform+chromatic-aberration+glass-warp chain), `GridDrips`, bar-graph and dot-grid generators, and a 3D-tracked-card technique for projecting a 2D "Sci-Fi Rings" graphic onto a rotating CG model in correct perspective.
- **File:** tutorials/goodbye-after-effects-2d-motion-graphics-in-nuke.md
- **Related:** Shares the `ScreenFX` plugin with Create a Movie Quality Sci-Fi Laser Effect in Nuke, How I Made a FULL Star Wars Cinematic from JUST One Screenshot, and How I Use Compositing to Skip THOUSANDS of Hours Rendering.


### 2D Rim Lights Look FAKE - But Not Anymore
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=WcB524Y32Io
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** specific version not stated on screen — free gizmo compiled for one particular Nuke version
- **Tags:** compositing, gizmo, grading, digital-matte-painting, beginner
- **Summary:** Compares three ways to fake a soft rim light on flat 2D alpha-only graphics: a quick but graphic `Emboss` approach, a manual `Transform`+stencil+`GodRay` fake, and a free custom gizmo whose smoothing control attenuates specifically at the edge (true light falloff) rather than uniformly blurring — explicitly distinguished from "light wrap" (a light source behind the object bleeding onto edges) since this casts light onto an already-composited shape's front edge instead.
- **File:** tutorials/2d-rim-lights-look-fake---but-not-anymore.md
- **Related:** Transform your FLAT Green Screen into Cinematic Lighting (`transform-your-flat-green-screen-into-cinematic-lighting.md`), 2 Expert VFX Tips to PERFECTLY Blend CG (`2-expert-vfx-tips-to-perfectly-blend-cg.md`) — share the gizmo-solves-a-lighting-problem-via-alpha-or-normals pattern.


### Planning out a Visual Effects Shot | Blender and Nuke
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=mToElxsVvZY
- **Author:** Compositing Academy
- **App:** Not applicable — pre-production planning in Blender's EEVEE viewport; no Nuke nodes shown
- **Version:** not applicable
- **Tags:** digital-matte-painting, compositing, beginner
- **Summary:** Free "Nuke 606" course preview on shot-planning methodology, not a node walkthrough: sourcing/iterating a composition in Blender's fast EEVEE viewport, rule-of-thirds and subject-facing composition logic, and the key compositor insight that a wide shot deliberately maximizes mid-ground/background real estate compositors can cheat as 2D (matte painting, depth hazing, layering) since parallax is minimal that far back. Closes with a converging-leading-lines technique for directing viewer attention, plus a "learn in a T-shape" career-advice aside (go deep in compositing, broad in adjacent skills like lighting/3D/photography).
- **File:** tutorials/planning-out-a-visual-effects-shot-blender-and-nuke.md
- **Related:** Skill Up with Nuke (`skill-up-with-nuke-how-to-think-like-a-pro-compositor.md`), Physics of Light for VFX Artists [Updated] (`physics-of-light-for-vfx-artists-updated.md`) — all three are theory/methodology videos rather than node recipes.


### Tracking Concepts in Nuke for Beginners
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=lpyZsAoiFMc
- **Author:** Compositing Academy
- **App:** Nuke / NukeX (3D camera tracking requires NukeX)
- **Version:** not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)
- **Tags:** tracking, camera-tracking, 3d-system, beginner
- **Summary:** Conceptual primer (diagrams, no node build) on 2D tracking, planar tracking, and full 3D camera tracking, explained through parallax and triangulation (minimum 3, ideally 6+, simultaneous points needed for a reliable 3D solve). Teaches a decision framework: "free move" camera motion (translation + rotation) usually needs a full 3D track unless only one low-parallax region needs replacing; "nodal pan" motion (rotation only) has near-zero parallax so 2D tracking usually suffices, except when points leave frame, requiring a "nodal pan 3D track" purely for persistent off-screen data.
- **File:** tutorials/tracking-concepts-in-nuke-for-beginners.md
- **Related:** Why your VFX Tracks aren't "Sticking" (`why-your-vfx-tracks-arent-sticking-and-how-to-fix-it.md`), Rotoscoping in Nuke Tutorial | 5 Beginner Tips (`rotoscoping-in-nuke-tutorial-5-beginner-tips.md`) — shares `tracking`, `camera-tracking`; Ray Render in Nuke Tutorial (`ray-render-in-nuke-tutorial-compositing-3d-reflections.md`), Re-lighting Real Footage (`re-lighting-real-footage-nuke-compositing-advanced.md`) — shares `3d-system`, `camera-tracking`.


### This FREE Tool Warps Images in a Way You’ve Never Seen
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=y3tFCa0U9Yo
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified
- **Tags:** gizmo, roto, procedural-texture, motion-graphics, compositing, intermediate
- **Summary:** Free custom `FlowWarp` gizmo samples a hand-drawn open `RotoShape` spline to build a UV "tunnel" around the path, letting a flat left-to-right image stretch-to-fit or continuously flow along any curved path (distance/samples/UV-blur/erode-edge/taper controls) — solving multi-directional bends other Nuke warp tools can't handle, without building 3D geometry strips. Creative examples: warping energy-trail stock elements around the Nuke logo, redirecting particle streams around an impact point, and building a looping comet trail from a tapered quadratic-luma-keyed roto shape.
- **File:** tutorials/this-free-tool-warps-images-in-a-way-youve-never-seen.md
- **Related:** Goodbye After Effects! 2D Motion Graphics in Nuke! (`goodbye-after-effects-2d-motion-graphics-in-nuke.md`), Create a Movie Quality Sci-Fi Laser Effect in Nuke (`create-a-movie-quality-sci-fi-laser-effect-in-nuke.md`) — share roto/procedural stock-element redirection themes.


### Moire Patterns | Nuke Tutorial [Intermediate]
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=gS4zXJ6sLs8
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** Nuke 13.x (13.1/13.2 — exact 2022 point-release not stated)
- **Tags:** procedural-texture, gizmo, compositing, st-map, rotopaint, intermediate
- **Summary:** Builds a Moiré interference pattern (as seen filming LED/CRT screens, e.g. WandaVision's "big wall" effect) from a `sin(x)` Expression line pattern, offset + rotated against a duplicate copy (rotation is what actually produces the interference), optionally warped via `GridWarp` or an animated `RotoPaint` stroke for organic distortion, then colorized with a blur→Linear-HSV "rainbow" pass (reused from the channel's dedicated rainbow tutorial) and multiplied back over the sharp pattern for a final animated old-TV Moiré effect.
- **File:** tutorials/moire-patterns-nuke-tutorial-intermediate.md
- **Related:** Nuke Tutorial | Compositing a Rainbow [Intermediate] (`nuke-tutorial-compositing-a-rainbow-intermediate.md`) — this video reuses that one's HSV rainbow-coloring technique directly.


### I Brought a Greenscreen in Arctic Conditions for this Film
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=EDPoJuffubU
- **Author:** Compositing Academy
- **App:** Nuke (mentioned only — compositing node work not shown on screen)
- **Version:** not specified
- **Tags:** compositing, roto, tracking, digital-matte-painting, procedural-texture, intermediate
- **Summary:** BTS pipeline case study (part 1/3): arctic on-location green-screen rig built into real ice, practical prop design favoring a lit, marker-tracked beach ball over real glass (avoids unwanted reflections/breakage risk), Polycam scanning, `KeenTools` prop tracking, and an "invisible visual effects" clean-plate step (remove the practical prop before compositing in its CG replacement). Actual Nuke compositing described only verbally, not shown on screen.
- **File:** tutorials/i-brought-a-greenscreen-in-arctic-conditions-for-this-film.md
- **Related:** Nobody's Ever Made VFX This Way (New Tech) (`nobodys-ever-made-vfx-this-way-new-tech.md`), How I Faked a $200M Movie Scene (In my DRIVEWAY!) (`how-i-faked-a-200m-movie-scene-in-my-driveway.md`) — share the BTS/pipeline-case-study format.


### Break up your "PERFECT CG" Renders with this FREE Plugin
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Nk6iluY4shE
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified
- **Tags:** gizmo, procedural-texture, digital-matte-painting, compositing, aovs, intermediate
- **Summary:** Dedicated tutorial for the free `PScatter` gizmo (author's own plugin), which scatters an arbitrary 2D image — not just noise — across a CG surface using an object-space position-reference pass (works from Blender/Houdini/Maya), with density and scatter-scale controls. Demonstrated adding scratch/dirt texture as a masked `Grade` multiply for surface wear, and scattering animated patterns (masked by render alpha) as a look-dev starting point for camouflage/force-field-impact effects.
- **File:** tutorials/break-up-your-perfect-cg-renders-with-this-free-plugin.md
- **Related:** Referenced (as a rejected look-dev experiment) in Create a Movie Quality Sci-Fi Laser Effect in Nuke (`create-a-movie-quality-sci-fi-laser-effect-in-nuke.md`) — this is PScatter's dedicated tutorial. Shares position-data-driven texture technique with Create 3D Noise | Nuke Compositing and Build Entire FX with ONE Pass - Nuke Tutorial.


### Compositing in UV space with Projections | Nuke [Advanced]
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=F-q8tgk8QCc
- **Author:** Compositing Academy
- **App:** Nuke / NukeX (ScanlineRender UV mode, ModelBuilder, Project3D, RayRender/AmbientOcclusion)
- **Version:** not specified on screen; 2021 upload, close to the Nuke 13.0 launch (2021-03-17) — likely Nuke 12.2/13.0-era
- **Tags:** 3d-system, digital-matte-painting, rotopaint, procedural-texture, advanced
- **Summary:** Switches `ScanlineRender`'s projection mode from Perspective to UV to convert a moving 3D projection into a stabilized, camera-independent 2D texture — enabling matte-painting on blended frame-held views, perspective-free texture editing (tiles), animated RotoPaint strokes that automatically follow hand-built proxy geometry (`ModelBuilder` + manual UV unwrap), and baking a static texture onto deforming Alembic geometry (cloth sim) with dynamic `RayRender`-based specular/AO relighting layered back on top so it doesn't look like a flat pasted image.
- **File:** tutorials/compositing-in-uv-space-with-projections-nuke-advanced.md
- **Related:** Ray Render in Nuke Tutorial (`ray-render-in-nuke-tutorial-compositing-3d-reflections.md`), Re-lighting Real Footage (`re-lighting-real-footage-nuke-compositing-advanced.md`) — shares `3d-system`; Preserve Quality | Projections in Nuke (`preserve-quality-projections-in-nuke.md`) — shares the re-project-only-the-change principle.


### Nuke Compositing an Advanced CG Shockwave | VFX (LookDev)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ErwClH-dQA0
- **Author:** Compositing Academy
- **App:** Nuke / NukeX (deep compositing requires NukeX)
- **Version:** Nuke 13.x (13.1/13.2 — exact 2022 point-release not stated)
- **Tags:** compositing, 3d-system, deep-compositing, st-map, projection, gizmo, fx-simulation, grading, expert
- **Summary:** Advanced concept-level (not node-by-node) breakdown of "kitbashing" a complex glassy shockwave/explosion entirely from generic pre-rendered stock energy elements, re-mapped so aggressively their circular/spherical origin disappears: `PolarDistort` circle-to-line unwrap + `STMap` onto scene UVs with an expanding `PMatte` reveal for a "contact energy" pass; a 3D `Sphere` with `UVProject`-doubled texture layers and `DisplaceGeo` radial-gradient-driven pinch-to-sphere shape animation for the main shockwave; `Glass` (per-channel IDistort) for chromatic-aberration refraction; `Deep`/`DeepMerge` occlusion against scene geometry; Cryptomatte-isolated per-piece UV rescaling; a deliberate, disciplined color scheme (monochromatic base + small accent-hue "pops," Doctor-Strange-style) applied via the channel's own Linear-HSV rainbow trick; and lens flares built from frame-held/dissolved stock elements studied against real reference footage.
- **File:** tutorials/nuke-compositing-an-advanced-cg-shockwave-vfx-lookdev.md
- **Related:** Nuke Tutorial | Compositing a Rainbow (`nuke-tutorial-compositing-a-rainbow-intermediate.md`), 360 Spherical LatLong Textures (`360-spherical-latlong-textures-nuke-tutorial.md`) — shared `PolarDistort`/rainbow techniques; Build Entire FX with ONE Pass (`build-entire-fx-with-one-pass---nuke-tutorial.md`) — shared position/UV-pass-driven comp-FX philosophy.


### EASY TRICK: Improve your Color Grading skills
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=dVN7IK1GsLA
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified
- **Tags:** grading, channels, color-management, compositing, beginner
- **Summary:** Targeted hue shift via a `Copy` node partially blending one RGB channel into another (e.g. red into green to turn reddish bounce light orange, not yellow) — leverages the fact that color is just a channel ratio (desaturating evens the ratio; this technique deliberately un-evens it). Compared against `HueCorrect`, the HSV tool, and `Keyer`-based selection, all of which can show harsher/imperfect falloff at the correction edge versus the smoother channel-mix gradient.
- **File:** tutorials/easy-trick-improve-your-color-grading-skills.md
- **Related:** Nuke Tutorial | Keying with Math Expressions [Intermediate], Nuke Tutorial | Compositing a Rainbow [Intermediate] — share first-principles RGB channel-math grading technique.


### Nuke Compositing Tutorial: Integration Sketching
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=p7_PYigrOgM
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified on screen; 2021 upload, close to the Nuke 13.0 launch (2021-03-17) — likely Nuke 12.2/13.0-era
- **Tags:** compositing, grading, roto, relighting, intermediate
- **Summary:** Methodology clip (from a longer "Nuke 505" course) showing how to visually diagnose and sketch fixes for a keyed character not yet sitting into a night cityscape plate: RotoPaint annotations flag problems, then rough Grade tests explore fixes — lifted blacks, missing motivated rim light, unnatural inherited highlights, "value conflict" (extreme bright against extreme dark pulling the eye), and coincidental edge alignment creating a false bad-key look. Stresses matching foreground/background dynamic range, meeting halfway rather than only pushing one side, and saving broad grades for last.
- **File:** tutorials/nuke-compositing-tutorial-integration-sketching.md
- **Related:** Grading Highlights and Pools of Light | Nuke Compositing (`grading-highlights-and-pools-of-light-nuke-compositing.md`) — shares `grading`, `relighting`; 2 Expert VFX Tips to PERFECTLY Blend CG (`2-expert-vfx-tips-to-perfectly-blend-cg.md`) — shares `relighting`, `grading`, `roto`, `compositing`.


### I Made VFX Relighting WAY Better in Nuke
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=H7dBKDLXwPo
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified — third-party gizmo ("CA Relight"), NOT Nuke's native Gaussian Splat relighting (SplatRender Direct/Point/Spot, added in Nuke 17.1)
- **Tags:** relighting, gizmo, compositing, 3d-system, intermediate
- **Summary:** Custom gizmo "CA Relight" extends screen-space normals-based relighting with depth+normals-derived self-shadowing/occlusion (a gap pure normals relighting can't fill), a top-down multi-light placement UI (vs. raw XYZ knobs, with keyframing and Shift-drag height control), and HDRI Reflect/Diffuse modes with a 3D dome visualization + "flat floor" reprojection option for physically accurate parallax. Validated against a test sphere and ray-traced render. **Version note: this is a third-party plugin, unrelated to Nuke 17.1's native SplatRender relighting feature** — do not conflate the two.
- **File:** tutorials/i-made-vfx-relighting-way-better-in-nuke.md
- **Related:** Direct follow-up to Transform your FLAT Green Screen into Cinematic Lighting (`transform-your-flat-green-screen-into-cinematic-lighting.md`) and 2 Expert VFX Tips to PERFECTLY Blend CG (`2-expert-vfx-tips-to-perfectly-blend-cg.md`) — share `relighting`. Can I Create a Speeder Chase on a TINY Greenscreen? (`can-i-create-a-speeder-chase-on-a-tiny-greenscreen.md`) — shares `relighting`, `gizmo`; the CA_Relight gizmo covered here is used in that pipeline case study.


### How SMART is State of the Art A.I Rotoscoping?
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=AinQkgdR6b8
- **Author:** Compositing Academy
- **App:** Nuke (SmartRoto add-on)
- **Version:** Nuke 17.x + SmartRoto plugin (Foundry AI-roto add-on, released ~July 2026)
- **Tags:** roto, ai-tools, compositing, tracking, nuke-17, intermediate
- **Summary:** Benchmarks Foundry's paid SmartRoto AI-roto add-on against 5 hard test shots (profile, motion blur, occlusion, lost profile, undefined profile). Workflow: draw base shape, mark hero keyframes with one-click auto-align snap, run Create Smart Keys to propagate. Handles moderate variation well with 2-5 hero keys and multi-shape mutual stabilization; breaks down under heavy occlusion, drastic color shifts, and undefined/flowing profiles.
- **File:** tutorials/how-smart-is-state-of-the-art-ai-rotoscoping.md
- **Related:** Rotoscoping in Nuke Tutorial | 5 Beginner Tips (`rotoscoping-in-nuke-tutorial-5-beginner-tips.md`), Why your VFX Tracks aren't "Sticking" (`why-your-vfx-tracks-arent-sticking-and-how-to-fix-it.md`) — share `roto`, `tracking`, `compositing`.


### Compositing Complex Shadows in Nuke [Advanced]
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=Yb3Cn3JnkUI
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified (2021 upload, Nuke 13.0 era)
- **Tags:** compositing, relighting, grading, roto, channels, gizmo, color-management, advanced
- **Summary:** Builds an HSV-flattened "shadow clean plate" (chained Keyer/Grade highlight rolloff, masked back through hue/saturation) to avoid double shadows where a CG shadow crosses real ones, plus EyeBlur/EyeDistort/EyeTransform gizmo tricks for attenuation, ground-ripple, and contact realism.
- **File:** tutorials/compositing-complex-shadows-in-nuke-advanced.md


### [1/3] Nuke Tutorial Series (Practical SFX, Lighting, Script Overview)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=NHeqhKOLFgU
- **Author:** Compositing Academy
- **App:** Nuke (overview/roadmap video — live compositing shown but not stepped through node-by-node)
- **Version:** Nuke 13.x (13.1/13.2 — exact 2022 point-release not stated)
- **Tags:** compositing, roto, rotopaint, grading, fx-simulation, digital-matte-painting, intermediate
- **Summary:** Part 1/3 of a flagship demo-reel-shot series (a cracking clay/plaster bust with glowing energy effects). Covers the compositing-iteration mindset (fixing competing highlights, saturation, flatness across versions), practical effects (real modeling-clay + Halloween face-paint sculpt) and practical Rembrandt two-light + bounce-card lighting used to shoot the base plate, a tour of the paid project's stock LookDev-library assets (liquid/nebula/ember sims, a cloth UV pass, Tilt-Brush flow-path geometry, KeenTools-tracked 3D face geo), and a guided click-through of the finished script's structure — SmartVector skin/body tracking, a "darken-then-Plus" habit for every crack-glow effect, IDistort perspective warps to bend 2D elements along the body's form, "Daisy chain" precomp organization for reused stock elements, 3D vs. 2D crack treatment based on parallax, UV-space lighting-stabilized texture integration via the KeenTools track, and `PolarDistort`-wrapped eye effects. Sets up Parts 2 and 3, which cover each technique in node-level detail.
- **File:** tutorials/13-nuke-tutorial-series-practical-sfx-lighting-script-overview.md
- **Related:** [2/3] and [3/3] Nuke Tutorial Series (once ingested) — direct continuations of this same shot/project. 360 Spherical LatLong Textures (`360-spherical-latlong-textures-nuke-tutorial.md`) and others — share the `PolarDistort` gizmo.


### Nuke Compositing Technique | Card3D + PixelsToPos [Beginners]
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=w5xFpajzC8s
- **Author:** Compositing Academy
- **App:** Nuke
- **Version:** not specified (2021 upload, Nuke 13.0 era)
- **Tags:** compositing, camera-tracking, 3d-system, gizmo, grading, roto, beginner
- **Summary:** Beginner shortcut for sticking 2D color corrections/elements to a tracked 3D scene using the "ImagePlane" (Card3D-based) and "Pixels2Position" Nukepedia gizmos instead of full ST-map projections — sample a 3D point, dial in the card's distance, done.
- **File:** tutorials/nuke-compositing-technique-card3d-pixelstopos-beginners.md


### [2/3] Nuke Tutorial Series (CRACKS, Keentools, Smartvectors)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=dLrJhqqNMrk
- **Author:** Compositing Academy
- **App:** Nuke / NukeX (SmartVector/VectorDistort require NukeX)
- **Version:** Nuke 13.x (13.1/13.2 — exact 2022 point-release not stated)
- **Tags:** tracking, camera-tracking, 3d-system, projection, channels, grading, digital-matte-painting, advanced
- **Summary:** Part 2/3 of the flagship series. Per-region tracking-method selection (SmartVector vs. KeenTools 3D face track vs. blended dual-track via ST maps), SmartVector edge-extension past overlap/edge failures (built-in in-paint-map-region, or VectorDistort→ST map→manual RotoPaint+InPaint for more control), the KeenTools FaceBuilder/FaceTracker workflow (faking multi-photo input via AppendClip of two frame-holds), UV-space texture integration with a dynamic blurred-plate light-map for free lighting-matched CG textures, 3D DisplaceGeo crack detail + RayRender Ambient Occlusion contact shadows, and the video's most advanced technique: preserving crack-matte alignment through 3D displacement by Shuffling the alpha into a custom channel *before* DisplaceGeo/ScanlineRender so it survives the position change correctly.
- **File:** tutorials/23-nuke-tutorial-series-cracks-keentools-smartvectors.md
- **Related:** [1/3] Nuke Tutorial Series (`13-nuke-tutorial-series-practical-sfx-lighting-script-overview.md`) — direct prequel; Rotoscoping in Nuke Tutorial (`rotoscoping-in-nuke-tutorial-5-beginner-tips.md`), Why your VFX Tracks aren't "Sticking" (`why-your-vfx-tracks-arent-sticking-and-how-to-fix-it.md`) — shared tracking fundamentals; How to DENOISE your CG in POST (`how-to-denoise-your-cg-in-post-blender-nuke-tutorial.md`) — shared UV/projection-space pipeline shape.


### Render World Position in Blender for Nuke
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=vrar9ALWG_g
- **Author:** Compositing Academy
- **App:** Blender (position-pass render setup) + Nuke (P-Mask usage)
- **Version:** not specified (2021 upload, Nuke 13.0 era)
- **Tags:** compositing, channels, grading, 3d-system, digital-matte-painting, beginner
- **Summary:** Blender-side material setup (Geometry→Separate RGB→axis-swizzled Combine RGB→Emission gated by Light Path) to render a Nuke-Y-up-correct world-position pass, then uses it in Nuke via the "P_Mask" gizmo to pick-a-point-and-mask a local correction without rotoscoping.
- **File:** tutorials/render-world-position-in-blender-for-nuke.md


### Can I Create a Speeder Chase on a TINY Greenscreen?
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=KLNmQtwj5Pc
- **Author:** Compositing Academy
- **App:** Nuke + Blender (mixed pipeline)
- **Version:** not specified — CA_Relight gizmo visible briefly (same tool as "I Made VFX Relighting WAY Better in Nuke")
- **Tags:** compositing, relighting, gizmo, digital-matte-painting, projection, fx-simulation, virtual-production, intermediate
- **Summary:** Full-pipeline BTS case study: Iceland volcano drone photogrammetry → CG vehicle built to a 3D-scanned actor's dimensions (practical rig was just bike parts on a broomstick against a garage greenscreen) → Nuke map painting/multi-camera projection to blend photography onto CG terrain → FX element compositing (smoke, debris, template sparks/lasers) → final integration via the CA_Relight self-shadowing gizmo. Nuke UI shown on-screen only once (the CA_Relight graph); mostly narrated pipeline montage.
- **File:** tutorials/can-i-create-a-speeder-chase-on-a-tiny-greenscreen.md
- **Related:** I Made VFX Relighting WAY Better in Nuke (`i-made-vfx-relighting-way-better-in-nuke.md`), Nobody's Ever Made VFX This Way (New Tech) (`nobodys-ever-made-vfx-this-way-new-tech.md`), I Brought a Greenscreen in Arctic Conditions for this Film (`i-brought-a-greenscreen-in-arctic-conditions-for-this-film.md`).


### Parallax HAX | Nuke Compositing [Advanced]
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=avtDQcZNThI
- **Author:** Compositing Academy
- **App:** [PENDING]
- **Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/parallax-hax-nuke-compositing-advanced.md

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
