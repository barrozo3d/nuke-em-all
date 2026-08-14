---
title: 3D Laser Effect | Nuke Compositing Tutorial (Higx Point Render)
source: YouTube
url: https://www.youtube.com/watch?v=R9zvo0T_PjY
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke / NukeX (RayRender for the ambient occlusion pass requires NukeX)"
version: "Nuke 14.x (author explicitly mentions the Higx Point Render plugin is used in the Nuke 14 splash screen — consistent with a 2023 upload; Classic 3D system)"
tags: [3d-system, gizmo, particles, motion-graphics, projection, grading, digital-matte-painting, advanced]
extraction_status: complete
frames_dir: tutorials/frames/3d-laser-effect-nuke-compositing-tutorial-higx-point-render/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# 3D Laser Effect | Nuke Compositing Tutorial (Higx Point Render)

**Source:** [YouTube](https://www.youtube.com/watch?v=R9zvo0T_PjY)
**Author:** Compositing Academy
**Duration:** 13m46s | 13 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.

> Reviewed: the "very short transcript in 'Conclusion'" warning is expected —
> that chapter is just the sign-off ("...and that's about it"). All real
> content is in the preceding chapters.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Composers are mostly known for being asset assemblers.
[0:08] Near the end of the post-production pipeline, we bring together one cohesive image using
[0:11] many different pieces.
[0:13] However, composers also create various types of assets and templates of their own.
[0:17] We do this by using various noise setups or particle simulations, as well as 2D elements.
[0:22] Nuke does have its own particle simulator, which you can see here, but in this tutorial,
[0:26] we're going to be talking about the point render plugin by Higgs, which is for Nuke,
[0:30] and it creates particle-like effects or motion graphic style effects.
[0:34] So we're only going over one example in this tutorial, but I do recommend checking it out.
[0:37] This is a pretty awesome plugin.
[0:39] You can do a lot with it.
[0:40] It's even used in the Nuke 14 splash screen, so it's pretty widely used.


### Example Shot [0:43]
**Transcript (timestamped):**
[0:44] We're going to be going over how to create this motion graphic style effect in Nuke.
[0:49] Primarily, we are using the Higgs point render plugin to create this effect, but there are
[0:54] multiple layers being used.
[0:56] So this is just a graphic I made for the last tutorial, which is just explaining what a
[1:01] lidar projection is.
[1:02] So I figured some people might be interested just to see some of the creative techniques
[1:06] that we can apply to get different types of effects similar to this.


### Basics of Point Render [1:10]
**Transcript (timestamped):**
[1:10] So for those who are not familiar, I'll just do a really quick rundown, and then I'll run
[1:14] into how I did the setup.
[1:17] But basically, the plugin has different nodes that we can scatter points along basic geometric
[1:24] surfaces or geometry that we can bring in.
[1:27] And so here we have a point plane, and basically it's creating all these points along the position
[1:32] pass of this.
[1:34] Basically will be a card, and we can control the amount of points that scatter on the surface.
[1:39] So for example, in the point plane, we can increase the width and height, and you'll
[1:43] see that there are more points that appear.
[1:45] So we put it through a point render, and that's how we get these type of renders in
[1:49] Nuke.
[1:50] If we put point fractal node, we can put some different shapes through there, so we can
[1:55] actually distort this and do all kinds of motion graphic style effects here.
[2:00] So we can offset this and we can make it look like it was animating through.
[2:05] We could reduce the amplitude, or we could change some of these settings that are kind
[2:08] of behaving like noise.
[2:10] And so that's like a really quick and simplified version of what this plugin is capable of.
[2:16] I will say the plugin is extremely capable in doing a number of things, so this is a
[2:20] very, very basic explanation.
[2:23] But that's just for the people who have never seen it before, and now we'll continue on
[2:27] to kind of what I did with this, and if you're interested in picking up the plugin, you can
[2:31] do that.
[2:32] The main part of this effect is actually using the lighter scan that I got from the real


### UV Projecting Scatter Points [2:33]
**Transcript (timestamped):**
[2:37] scene.
[2:38] If you plug it in directly, so I just put a constant into the OBJ that I have of this
[2:43] scan, and I put a point geosource UV, which is basically scattering those points except
[2:50] on the geometry that we're bringing in.
[2:51] Now by default, it comes in looking like this, and that's because the UVs of this object
[2:55] are kind of weird because it's coming from an auto UV that the lighter scan actually
[3:01] did, so if you look at what that does, this is the texture that comes with the lighter
[3:05] scan by default, and you can see there's sort of these patches in different areas, so there's
[3:09] an auto UV layout that probably Polycam is just sort of creating in the app, and then
[3:14] that's how it's texturing the surface.
[3:16] Now we're not really using any of the texture or anything like that, but that's just why
[3:21] it looks like that, and this is, so this we know is our UV layout.
[3:26] So basically what I wanted to do was to replace the UVs here so that the points would scatter
[3:31] in a way that it looked like we're coming from the camera.
[3:34] And so essentially what you want to do is UV project and replace the UVs of this geometry.
[3:41] So in Nuke, there's a node called UV project.
[3:44] Not project 3D, but UV project, and so if I switch this Geosource node to this here,
[3:50] so this is just a temporary camera at a UV project, so I'll just switch this over, and
[3:55] you'll see that now we have a much cleaner result.
[3:57] So essentially what it is is if I just zoom out, I just created a new camera here.
[4:01] This is not like an animated camera or anything, it's just the default camera node, and essentially
[4:06] if I move this around, we can see that the points will actually come from the perspective
[4:11] of that camera.
[4:12] And so that's a pretty cool technique because now we can animate this and we can have points
[4:17] that look like they're moving around on the surface.
[4:21] Also if we were to reduce the number of points, so I could say the point density here and
[4:25] just bring it down a bit, and that's going to give us a little bit more of that effect
[4:28] but exaggerated.
[4:30] And so you see that those points are all coming from this camera.
[4:34] And so that's pretty much the bulk of the effect.
[4:37] So if I actually switch over here to the actual setup I did here, so I'll just switch this
[4:42] over, it's the exact same setup except from an animated camera.
[4:46] So if I just look at this, we have this camera that I just keyframed and swinging around
[4:51] the environment.
[4:52] So if I open the geometry at the same time here with the transform, you can see this
[4:56] is the camera motion we have.
[4:58] And then I also have the shot camera which is actually going the other way around.
[5:02] So this camera goes this way, even though it's not previewing correctly here, the cameras
[5:07] are swinging both directions.
[5:10] And so if I just go back to start here and take a look at what that looks like, about
[5:14] frame 100, I think 106 is when it starts.
[5:18] We did have a little bit of error here but one other thing I was doing was I put a sphere


### Sphere Blocker [5:22]
**Transcript (timestamped):**
[5:23] with a merged geo over our scan because if you just plug in the UV project with our sort
[5:29] of projection camera directly into the lighter scan, this is the effect which is what we
[5:33] expect, right?
[5:34] It's projecting out the points from the angle that the camera is swinging around.
[5:39] But what I wanted to do was reveal this effect sort of spreading over time.
[5:44] And so what I did was I took a sphere and I parented it to the camera.
[5:49] So I took the camera's position, so if I double click the camera and I open two panels
[5:54] here so I can see both at the same time, I basically just control drag the translate
[5:58] and put it into the sphere so that the sphere will actually stick to the position of the
[6:02] camera.
[6:03] So you can see that as the camera starts moving around, the sphere is following.
[6:07] But I key frame the scale so that the sphere would just get bigger over time.
[6:13] And so what that does, if we don't put a texture in the sphere and we're merging it with the
[6:18] merge geo, essentially it's locking the projection.
[6:21] And so what does that mean?
[6:23] If we're blocking the projection where the sphere is, it's not going to project the
[6:26] UVs past the sphere.
[6:28] So we only see the dots appearing within the sphere that's there.
[6:33] And so when we actually look at that effect, I'll go to the precomp here.
[6:36] If we look at that effect, we see that it's giving us those points spreading across the
[6:42] surface.
[6:43] And so I'll give it a second to cash here just so we can see it in real time here.
[6:47] But that's sort of what the effect looks like.
[6:49] And what's interesting about it is that those points are moving up and down along the geometry
[6:53] as our camera is moving around, which gives us that sort of effect where it feels like
[6:57] there's kind of lasers shooting out onto the surface.
[7:02] Now the next part of what I did was essentially the same exact technique, except rather than


### Sphere Dots [7:04]
**Transcript (timestamped):**
[7:07] projecting the points onto the environment, I just did the same point render setup, but
[7:11] only with the spheres.
[7:12] We don't have the geometry in this setup at all.
[7:14] We just have a constant plug in the sphere so it will catch the material and make the
[7:18] points appear.
[7:19] And we're doing the same UV project, the same camera, same geometry, and the same geosource
[7:25] except no geometry.
[7:26] The only difference is here is that we have in the point render, there's a setting called


### Occlusion [7:30]
**Transcript (timestamped):**
[7:30] a collusion.
[7:31] And what you can do is you can plug in a scanline render with another geometry.
[7:37] So basically just cutting out the sort of the lidar scan from our points.
[7:43] And so that's just going to give us this pass by itself.
[7:46] So if I just let that play, we see that we get that secondary effect of these sort of
[7:49] points going around.
[7:51] And I thought that was a cool effect to just combine on top.
[7:54] So we have like the scan going there and we have the sphere that's sort of containing
[7:59] it.
[8:00] So as the effect spreads, we get this halo that's kind of going around.
[8:03] And by having it on a separate layer, it allows me to fade that off over time if I want.
[8:10] The next part of this is just normal post effect work.
[8:13] So we're just doing an exponential glow, plusing it back on, giving it a little bit of a glow


### Post Glows [8:15]
**Transcript (timestamped):**
[8:17] here.
[8:18] There's a cool technique here and where I'm using these convolve filters.
[8:21] I've created a library of convolve filters, like sort of random colors and stuff, because
[8:26] it's a really awesome way to create flares.
[8:28] So I've created a library of about, I think, 300 of these.
[8:31] And essentially you can just inject colors by using a convolve.
[8:36] And in the convolve, we say use input channels.
[8:38] So you take this multicolored sort of abstract effect and we put it onto the image.
[8:44] And what that gives us is these really, really nice flares.
[8:48] And it's not the sort of typical flare you see from like a camera pointing a spotlight
[8:53] towards you, but it is sort of a realistic flare in the sense that you get these sort
[8:57] of abstract highlights overlapping each other.
[9:01] And that's a very unique way to create a flare.
[9:03] And so we can take this result and plus it over our image.
[9:08] So when we have that explosion, we're getting a cool flare.
[9:10] And now we don't really want that sharp edge.
[9:12] So what I did was I created another glow on top.


### Residual Points [9:15]
**Transcript (timestamped):**
[9:15] And if we just let that play, we see it gives us a little bit of a more integrated edge
[9:19] where it feels hot on the edge.
[9:21] And if we step forward a few frames, we can actually, maybe we can jump down in the script
[9:26] to just look at the result of that.
[9:28] So we can see that's a result.
[9:29] We get this exploding light effect.
[9:32] And we have these rings that feel like they're actually flaring out from the light source.
[9:36] And so if I let that play just by itself.
[9:38] We see that those rings are expanding.
[9:41] And so that's just the post effect on top of that.
[9:44] And I did have sort of a residual layer of points in the background.
[9:49] So you see this dark blue that's behind the whole projected effect.
[9:53] And that's essentially just another point set up with the same geometry, except I just
[9:58] darkened it and made it a little bit blue.
[10:00] And so that's just fading on in the background just to give something sort of like slowly
[10:05] illuminating behind.
[10:07] As if something was left behind when that laser has passed over it.
[10:11] So that was the idea behind that.
[10:13] So if I let that play, you can see that's that's the effect that we're getting from
[10:17] all of those layers combined.
[10:19] The next thing in the composite here is adding some geometry for the camera.
[10:24] So all I did was model a really simple little triangle here in Blender.
[10:29] It's literally just like a square and I just moved vertices in.
[10:31] So if you just look at the geo, we can see what that looks like.
[10:35] That's just a square with the vertices kind of shrunk.
[10:38] I used a transform geo to plug in an axis on the axis branch, the camera that's moving.
[10:44] And so what that does is it allows us to essentially, let's just take a look, load the geo here


### Attaching Geo Camera [10:45]
**Transcript (timestamped):**
[10:51] and look at the transform geo.
[10:52] That'll just stick it to the camera and looking at the same angle as the camera.
[10:56] So I just wanted something to represent, you know, the direction that the camera is looking
[11:00] in.
[11:01] So I put a wireframe shader onto it.
[11:04] So we get this out of the render, just a basic wireframe on a geometry and then just turning
[11:09] that green to kind of make it pop a little bit and putting this over the image.
[11:14] So now we have something that we can actually look at to get the idea of what this effect
[11:19] is supposed to be, which is a camera projecting out laser beams essentially.
[11:24] And then the next step here would be the actual beams themselves.
[11:28] So this is similar to the God Ray tutorial I did.
[11:32] If you watch that tutorial on my channel, it's the same technique except we're doing


### Godray Technique [11:33]
**Transcript (timestamped):**
[11:36] it with really, really small points in the point render.
[11:39] This is what the render looks like.
[11:41] It's the same geometry and the same technique we used before except I reduced the number
[11:45] of points to a really low number.
[11:47] And so you get sort of a more sparse effect of these dots moving around.
[11:53] The reason I did that was because when I do the God Ray, if I set the center point to
[11:59] the camera, everything pulls towards the camera.
[12:01] So if I brighten that up, you can see what that looks like.
[12:03] It's pulling all those points to the camera.
[12:05] I just manually keyframed the center looking at where the camera is traveling.
[12:10] So this is a 2D effect.
[12:11] These rays aren't actually 3D.
[12:12] It's all screen space, but it looks 3D.
[12:15] So that's an interesting thing we can do.
[12:18] And so a little bit of color correction, a little bit of a glow.
[12:22] And then we get these rays.
[12:24] If we plus that over, that gives us this effect.
[12:27] So if we go down, that's pretty much all of it.
[12:30] So if I just let it play here, we can look at the effect here.
[12:34] So that screen space effect is giving us something that feels like light rays are being projected
[12:38] outward.
[12:39] So that's it for this effect, for the primary aspect of it.
[12:42] I guess at the end here, we do a little sort of a fade into a wireframe and then into just
[12:47] a simple textured representation and then the final texture.
[12:52] So that's literally just a merge that's been key mixed on some of the different layers.
[12:57] So for example, I just took the geometry with a wireframe and we just fade that on to kind


### Wireframe and Checkerboard [13:02]
**Transcript (timestamped):**
[13:03] of see that.
[13:04] And we also have a checkerboard assigned to that same geometry on another layer.
[13:09] And we just, I did it multiply an ambient occlusion against it to give it a slight shadow.
[13:15] So we can see a constant and ambient occlusion, the geometry and then a ray render.
[13:20] That's how you create the ambient occlusion, which is being multiplied on, which gives
[13:24] you just this little shadow effect.
[13:27] And then it's just being merged over with this mix being kind of brought down.
[13:32] And finally, the same idea here, we have the geometry with the texture just being brought
[13:36] down.
[13:37] So that's about it for this tutorial.
[13:38] If you guys thought this was cool or you liked it, make sure to hit the like button or subscribe


### Conclusion [13:39]
**Transcript (timestamped):**
[13:43] and that's about it.



---

## Captured Frames

- [1:45] tutorials/frames/3d-laser-effect-nuke-compositing-tutorial-higx-point-render/frame_000.jpg
- [3:55] tutorials/frames/3d-laser-effect-nuke-compositing-tutorial-higx-point-render/frame_001.jpg
- [6:07] tutorials/frames/3d-laser-effect-nuke-compositing-tutorial-higx-point-render/frame_002.jpg
- [7:51] tutorials/frames/3d-laser-effect-nuke-compositing-tutorial-higx-point-render/frame_003.jpg
- [8:44] tutorials/frames/3d-laser-effect-nuke-compositing-tutorial-higx-point-render/frame_004.jpg
- [10:00] tutorials/frames/3d-laser-effect-nuke-compositing-tutorial-higx-point-render/frame_005.jpg
- [11:04] tutorials/frames/3d-laser-effect-nuke-compositing-tutorial-higx-point-render/frame_006.jpg
- [12:03] tutorials/frames/3d-laser-effect-nuke-compositing-tutorial-higx-point-render/frame_007.jpg

---

## Structured Notes

### Core Technique
Building a "LiDAR laser scanning" motion-graphics effect using the third-party **Higx Point Render** plugin to scatter camera-projected points across a real-world LiDAR/photogrammetry scan, with a growing sphere used purely as a projection-blocking mask to reveal the scatter spreading outward over time — plus supporting layers (occlusion halo, residual afterglow, screen-space GodRays, custom convolve-filter flares) and a simple wireframe camera-representation geo.

### Summary
Introduces Foundry-ecosystem plugin **Higx Point Render** (credited as used in the actual Nuke 14 splash screen, confirming this is Nuke 14.x-era content) as a particle/motion-graphics point-scattering system: a `PointPlane`/`PointGeoSourceUV` scatters points across a surface's position pass or UVs, `PointRender` renders them, and `PointFractal` can distort the scatter pattern (frame_000/001 show the basic point-plane/point-render node chain). The actual project uses a **LiDAR/photogrammetry scan** (a Polycam OBJ export, complete with a messy auto-UV texture atlas the tutorial explicitly ignores) as the scatter surface. Because the scan's native UVs are unusable for a "points radiating from the camera" look, the fix is `UVProject` (not `Project3D`) fed a plain, non-animated default `Camera` node plugged into `PointGeoSourceUV` — this re-derives the scatter surface's UVs from that camera's perspective, so as the camera (or a duplicate driving camera) moves, the scattered points visually crawl across the surface as if radiating from the lens (frame_002 shows the animated-camera version of this rig, with both a driving camera and a separate "shot" camera swinging in opposite directions). To reveal this effect **spreading over time** rather than covering the whole scan instantly, a `Sphere` is parented to the driving camera (its translate literally control-dragged from the camera's transform into the sphere's) and its scale is keyframed to grow — merged into the scene geometry via `MergeGeo` with no texture on the sphere itself, it purely blocks/limits how far the UV-projected points are allowed to render, so points only appear within the sphere's current radius (frame_003 shows the resulting radiating-scan-line silhouette). A second, simpler pass repeats the exact same camera/UVProject/PointGeoSourceUV rig but scatters points onto the sphere itself (no scan geometry) with the Point Render's **occlusion** setting fed a `ScanlineRender` of the scan geometry, so the sphere's points are cut wherever the actual scan would occlude them — producing a secondary "halo" layer (frame_004) that can be independently faded, layered over the main scan-scatter effect. Standard post stacking follows: exponential `Glow` plussed back on; a large personal library (~300) of **abstract multicolor "convolve filter" images**, applied via a `Convolve` node set to "use input channels," used purely as a flare-injection trick — the convolved result is `Plus`ed over the image for organic, non-lens-flare-looking overlapping-highlight flares (frame_005); another `Glow` softens the hard flare edge for a "hot" integrated look; a **residual points layer** — the same point setup, darkened and tinted blue, faded in behind everything — simulates an afterglow left behind once the "laser" has passed (frame_006). A simple **camera-representation geo** (a hand-modeled Blender square with pulled-in vertices, `TransformGeo`'d onto an `Axis` parented to the driving camera, rendered with a green `Wireframe` shader) visualizes the implied camera/laser-source direction in-frame. The beam itself reuses the exact same Point Render technique at very low point density fed into `GodRays`, with the GodRays' center point manually keyframed to track the camera's screen-space position rather than fixed — screen-space only (not true 3D), but reads convincingly as 3D beams because the source point tracks the actual camera motion (frame_007). The video closes on a simple reveal sequence: wireframe fades into a checkerboard-textured pass (multiplied against a `RayRender` Ambient Occlusion pass for a soft contact shadow) and finally the real texture, cross-dissolved via key-mixed Merges.

### Key Steps
1. Bring in a LiDAR/photogrammetry scan (e.g. a Polycam OBJ export) as 3D geometry; ignore its native auto-UV texture atlas — it isn't used for this technique.
2. Scatter points onto the scan via `PointGeoSourceUV` → `PointRender` (Higx Point Render plugin); by default this follows the scan's messy native UVs.
3. Replace those UVs with a camera-relative projection: plug a plain `Camera` node into `UVProject` (not `Project3D`) feeding the geosource, so points appear to radiate from that camera's perspective; animate the camera (or a dedicated driving camera separate from the "shot" camera) to make the scatter visually sweep across the surface.
4. To reveal the effect growing over time instead of covering everything instantly: create a `Sphere`, control-drag the driving camera's translate into the sphere's translate so it follows the camera's position, keyframe the sphere's *scale* to grow over time, leave the sphere untextured, and `MergeGeo` it into the scan geometry — this blocks/limits the UV-projected points to only render within the sphere's current radius.
5. Build a secondary "halo" pass: repeat the same camera/UVProject/PointGeoSourceUV rig scattering points onto the sphere alone (no scan geometry), and set Point Render's **occlusion** input to a `ScanlineRender` of the scan geometry so the halo points are correctly cut behind the scan — keep this as its own layer so it can be faded independently.
6. Post-process: exponential `Glow` plussed on for bloom.
7. Build organic, non-standard flares from a personal library of abstract multicolor "convolve filter" images: `Convolve` (mode = use input channels) that image against the render, `Plus` the result over the main image, then add a second `Glow` to soften the flare's hard edge.
8. Add a "residual" afterglow layer: duplicate the point setup, `Grade` it darker and tint it blue, fade it in behind the main effect to suggest lingering energy after the "laser" passes.
9. Visualize the implied camera/beam source: model a simple low-poly shape (e.g. in Blender), `TransformGeo` it onto an `Axis` parented to the driving camera, shade it with a green `Wireframe` material, render and merge over the image.
10. Build screen-space "laser beam" rays: reuse the same low-point-density Point Render setup, feed it into `GodRays`, and **manually keyframe the GodRays center point to track the camera's screen-space position** over time (rather than a fixed center) — purely 2D/screen-space, but reads as 3D because the source point follows real camera motion; finish with light color correction/glow and `Plus` over.
11. Finish with a simple reveal: key-mixed `Merge`s crossfading wireframe → checkerboard-textured pass (multiplied against a `RayRender` Ambient Occlusion pass for contact shadow) → final texture.

### Nodes / Tools / Settings
- **Higx Point Render (third-party Nuke plugin, not Foundry-native, but used in the actual Nuke 14 splash screen):** `PointPlane`, `PointGeoSourceUV`, `PointRender`, `PointFractal` (distortion/shape variation), Point Render's built-in **occlusion** input (fed a `ScanlineRender` for correct depth cutting)
- **Core Nuke/NukeX:** `UVProject` (camera-relative UV re-derivation — explicitly distinguished from `Project3D`), `Camera` (both a static default-camera trick and a fully animated driving camera), `Sphere` + keyframed scale + `MergeGeo` (projection-blocking reveal mask), `Axis`/`TransformGeo` (camera-parented geo), `Wireframe` shader, `GodRays` (center point keyframed to camera screen position), `Convolve` ("use input channels" mode for image-based flares), `Glow` (exponential), `RayRender` (Ambient Occlusion pass), `Grade`, key-mixed `Merge`s
- **Asset source:** a LiDAR/photogrammetry scan (Polycam-style OBJ export) as the base scatter geometry; a personal library of ~300 abstract multicolor "convolve filter" flare-source images
- **Cross-reference:** the GodRays/beam technique is explicitly noted as reusing the author's separate "Compositing EPIC VFX Godrays" tutorial's core trick, just fed with sparse Point Render points instead of that video's source

### Difficulty
Advanced — requires comfort with Nuke's 3D system (camera-parenting, geo merging, projection blocking) and a paid third-party plugin (Higx Point Render); individual techniques (UVProject-from-camera, sphere-as-projection-mask) are conceptually simple once explained but assume 3D-system fluency.

### Foundry App & Version
Nuke / NukeX (RayRender's Ambient Occlusion pass is NukeX-only). Version not stated numerically, but the author explicitly says the Higx Point Render plugin is used in the real Nuke 14 splash screen — strong contextual evidence this is Nuke 14.x-era content, consistent with a 2023 upload per this skill's version-tracker (14.0 shipped Dec 2022, 14.1 Oct 2023). Uses only the Classic 3D system — predates the 14.0-beta USD 3D overhaul, though the two shipped in the same version window.

### Tags
3d-system, gizmo, particles, motion-graphics, projection, grading, digital-matte-painting, advanced

---

## Related Tutorials
No existing knowledge-base entries currently use the Higx Point Render plugin or the camera-parented-sphere-as-projection-mask technique — this is the first tutorial covering either. Revisit once "Compositing EPIC VFX Godrays" (explicitly cross-referenced by this video as covering the underlying GodRays technique in more depth) is ingested from this same 2023 batch.
