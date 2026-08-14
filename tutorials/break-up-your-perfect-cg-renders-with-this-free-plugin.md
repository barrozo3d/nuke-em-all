---
title: Break up your "PERFECT CG" Renders with this FREE Plugin
source: YouTube
url: https://www.youtube.com/watch?v=Nk6iluY4shE
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "not specified"
tags: [gizmo, procedural-texture, digital-matte-painting, compositing, aovs, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/break-up-your-perfect-cg-renders-with-this-free-plugin/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Break up your "PERFECT CG" Renders with this FREE Plugin

**Source:** [YouTube](https://www.youtube.com/watch?v=Nk6iluY4shE)
**Author:** Compositing Academy
**Duration:** 4m7s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to this tutorial. We're going to be talking about how to scatter details and break up your perfect looking CG with position data.
[0:07] So I'm releasing a free plugin. It's called Pscatter, and it helps you do this process. I've never seen a plugin that actually scatters images along position data in a random way.
[0:17] So I wanted to put one together and it's been really useful for me. So hopefully you guys will find it useful as well.
[0:22] And just for quick context, if you don't know, this position data can come out of Blender, Houdini, Maya, it doesn't really matter. 3D position data is a universal render pass that you can use.
[0:34] So here's my render. We have this lander that's coming towards the camera. It's kind of a zoom in shot. So I'm not showing the final scene here.
[0:41] If you want to see the final scene, by the way, in a few weeks, we're going to be showing this full VFX sequence I've been directing. So make sure you subscribe.
[0:48] But this is what we have. So we have like a before and just an after some little scratch details and things like that.
[0:55] And how we're doing this is this position data and the Pscatter plugin. So this plugin essentially, I'll show it with color reels first.
[1:04] So I have my position data, which is rendered out of Blender. This is position reference data, which means it sticks to the object. It's not world position.
[1:12] And using this data, we can stick images onto our CG. So here I am just plugging the position data into a simple picture of a color wheel.
[1:20] And when I put this on here, you'll see we actually scatter that image a whole bunch of times all over the 3D model.
[1:26] If I hit play, you'll see that these images actually stick, which this is really useful because we can break up surfaces. We could add dirt, snow, whatever it is you want to add.
[1:36] Now we have control instead of just using something like a noise pattern, which is useful to scatter sometimes onto a model.
[1:43] Having images is actually much more powerful. So if I take this, you're going to need to adjust these depending on the size of your position data.
[1:51] If you're doing a really large scale world, it might come in looking weird. So you need to play around with the size here.
[1:56] So basically, I've added a density control and it's scattering points randomly across the position data.
[2:02] And we also have scatter scale so we can we can increase the scale and we're going to get those color wheels kind of spawning bigger.
[2:09] So that is how it works. Now it's not that interesting with color wheels. Obviously, we want to do something useful.
[2:14] So here I've just taken a scratch texture from textures.com and basically cropped it in.
[2:21] So I did a little crop here with a softness control just to feather off the edges and essentially just do a little bit of a piece scatter.
[2:28] And this piece scatter can give us some nice scratches on our surface and we can use this to kind of grade our CG.
[2:33] So if we have our original CG here, we could take a grade node, we could plug that into the mask and maybe we just do a little bit of a multiply up.
[2:41] Now, maybe it's a little bit too uniform and we could break that up with other things like PMATS or other various methods.
[2:47] But this is essentially the idea. We want to break up CG. We don't want perfect soft looking CG or CG that just looks not dirty.
[2:55] And that's just a good way to add a little bit of realism. So the plugin is going to be there.
[2:59] And there's some interesting things that you can do with this as well that I think would be a hard thing to do otherwise.
[3:06] So things like this, I was kind of playing with this concept of playing with some various animation patterns and then basically scattering that onto the CG.
[3:14] Now you need to mask this out. So sometimes you get this color in the background. You just mask it by your rendered alpha.
[3:21] But something like this could be the starting point for a look development of something like maybe a camouflage tank, like a sci-fi tank or something like that,
[3:30] where maybe you want to do army stealth camouflage effect or some kind of force field that gets hit and impacted and maybe some kind of reaction across the surface of your CG.
[3:42] This is how we would start to do it. Now, this is not obviously a final effect, but it gives you an idea of scattering videos onto your 3D models,
[3:50] which is really, really cool. So there's a lot of creative use and I'm sure I'll show some other demos in the future of how you can actually use this.
[3:57] That's just where my brain was kind of messing around a little bit. So hopefully you guys find that useful. The download link is in the description below.
[4:03] Make sure to hit the thumbs up and I'll keep making more videos like this. Thanks.



---

## Captured Frames

- [0:55] tutorials/frames/break-up-your-perfect-cg-renders-with-this-free-plugin/frame_000.jpg
- [1:20] tutorials/frames/break-up-your-perfect-cg-renders-with-this-free-plugin/frame_001.jpg
- [1:56] tutorials/frames/break-up-your-perfect-cg-renders-with-this-free-plugin/frame_002.jpg
- [2:14] tutorials/frames/break-up-your-perfect-cg-renders-with-this-free-plugin/frame_003.jpg
- [2:33] tutorials/frames/break-up-your-perfect-cg-renders-with-this-free-plugin/frame_004.jpg
- [3:06] tutorials/frames/break-up-your-perfect-cg-renders-with-this-free-plugin/frame_005.jpg

---

## Structured Notes

### Core Technique
The free `PScatter` gizmo scatters an arbitrary 2D image (not just a noise pattern) randomly across a CG surface using a position-reference render pass (object-space P data, from any 3D app), giving art-directable, image-based surface breakup — dirt, scratches, snow, camouflage/impact patterns — instead of a "too perfect" clean CG render.

### Summary
Compositing Academy releases `PScatter`, a free Nuke plugin the author built after finding no existing tool that scatters arbitrary images (not just noise) across a 3D surface using position data. Fed an object-space position-reference pass (rendered from Blender, but the technique works with position data from Houdini, Maya, or any 3D app since it's a universal pass type), PScatter repeats and randomly places a source image across the model's surface, sticking to it as the object moves. Demonstrated first with a color wheel to show the mechanics (density controls how many points are randomly scattered across the position data; scatter scale controls the size of each scattered instance; results need re-tuning per scene scale, since a large-scale world's position data will scatter oddly at default settings), then practically with a cropped/feathered (softness-controlled) scratch texture from textures.com, used as a `Grade` mask (multiplied) onto the CG beauty to add surface wear — flagged as still needing further breakup (e.g. via position mattes) to avoid looking too uniform. A creative extension scatters an animated pattern (rather than a static texture) across a model, masked by the render's own alpha to remove background bleed, suggested as a starting point for look-dev on effects like camouflage, stealth patterns, or a force-field impact reaction traveling across a CG surface.

### Key Steps
1. Render an object-space (not world-space) position-reference pass from any 3D application (Blender, Houdini, Maya) — this data "sticks" to the model's own surface rather than to world coordinates.
2. Feed that position pass into `PScatter` along with a source image to scatter (a texture, a scratch/dirt image, or even an animated pattern).
3. Tune `density` to control how many random scatter points are placed across the position data.
4. Tune `scatter scale` to control the size of each individual scattered image instance.
5. Re-tune density/scale per shot — position data from a large-scale world will scatter unexpectedly at default settings tuned for a smaller object, so settings aren't universal across scenes.
6. For practical surface-wear use: source a texture (e.g. a scratch/dirt image from textures.com), crop it with a softness-feathered edge, and scatter it via PScatter.
7. Use the scattered result as a `Grade` mask (multiplied onto the CG beauty) to add wear/dirt/scratches without a uniform, obviously-repeated look; combine with additional breakup methods (e.g. position mattes) if the result reads too uniform on its own.
8. For animated/creative pattern use: scatter an animated source pattern (rather than a static image) across the model, and mask out any background color bleed using the CG render's own alpha channel.
9. Treat this as a fast look-dev starting point for effects like camouflage/stealth patterns or a traveling force-field/impact reaction across a CG surface — not a finished effect on its own.

### Nodes / Tools / Settings
- `PScatter` (free custom gizmo, author's own plugin) — scatters an arbitrary source image across a 3D surface using an object-space position-reference render pass; controls include density (point count) and scatter scale (instance size)
- Object-space position-reference (P) pass — universal 3D render pass type (works from Blender, Houdini, Maya, etc.), distinct from world-position; required input for PScatter to stick images to the model's own surface
- `Crop` (with softness) — feathers the edge of a source texture before scattering
- `Grade` (masked, multiplied) — applies the scattered result as a wear/dirt breakup mask onto the CG beauty
- Render alpha — used as a mask to remove background bleed when scattering an animated pattern

### Difficulty
Intermediate

### Foundry App & Version
Nuke. No on-screen version banner or OCIO metadata visible in the captured frames — version not specified.

### Tags
gizmo, procedural-texture, digital-matte-painting, compositing, aovs, intermediate

---

## Related Tutorials
`PScatter` is the same plugin referenced (as a rejected look-dev experiment) in Create a Movie Quality Sci-Fi Laser Effect in Nuke (`create-a-movie-quality-sci-fi-laser-effect-in-nuke.md`) — this video is its dedicated tutorial. Shares position-data-driven procedural texture technique with Create 3D Noise | Nuke Compositing (`create-3d-noise-nuke-compositing.md`) and Build Entire FX with ONE Pass - Nuke Tutorial (`build-entire-fx-with-one-pass---nuke-tutorial.md`).
