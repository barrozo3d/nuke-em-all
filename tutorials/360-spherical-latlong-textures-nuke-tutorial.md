---
title: 360 Spherical LatLong Textures | Nuke Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=ifsOs84Ps2g
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "Nuke 13.x (13.1/13.2 — exact 2022 point-release not stated on screen or in transcript)"
tags: [compositing, 3d-system, digital-matte-painting, roto, rotopaint, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/360-spherical-latlong-textures-nuke-tutorial/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# 360 Spherical LatLong Textures | Nuke Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=ifsOs84Ps2g)
**Author:** Compositing Academy
**Duration:** 15m59s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Hello guys, welcome to this tutorial. This time we are going to talk about how to texture
[0:13] a sphere and basically how to take a normal photograph and kind of convert it into a lat
[0:19] long texture that we can basically wrap around and it works for any camera angle. So this
[0:24] is really good for if you have scenes that have a large skybox around in the distant area
[0:31] and you want to fly a camera through the sphere. So if you are doing a jet flying or maybe
[0:36] a ship flying in space or something like that, this technique is going to work for those
[0:41] kind of scenes and basically any scene that has a sky and you want to see different angles
[0:45] in the same shot. And this technique can also be used for getting textures out into different
[0:51] software. So if you are doing like a VR game or something like that, like I have an example
[0:56] here I will show at the end of the video which is basically just taking some nebulas that
[1:01] were kind of just released as a pack. So there is a bunch of the nebula textures that you
[1:05] can find on Compositing Academy and basically how I am using these for a VR environment
[1:12] and how this technique actually applies into that sort of realm as well. So basically what
[1:18] we are going to look at first is just a picture from Unsplash here and we have this sky and
[1:24] if we wanted to apply this onto a sphere directly, this is the problem that you are going to
[1:29] immediately see. So if we have the picture, we plug it in, we give it an alpha here so
[1:33] we shuffle in an alpha, we plug it into a sphere and we go in 3D. Immediately you are
[1:38] going to see a few problems and that is we have a scene and that is very easy to fix
[1:43] but we also have this pole. So basically if you guys are familiar with like if you have
[1:49] ever seen a texture of like earth, like an earth texture or earth cloud map texture,
[1:54] these are called lat long textures and these textures basically have some kind of warping
[2:01] near the top which allows it to be wrapped around the sphere properly and if you don't
[2:05] have that kind of warping, that intentional warping that is kind of around the top of
[2:09] the picture, it doesn't wrap around a sphere properly and so 360 cameras will automatically
[2:15] give you this but if you are working with like a picture that is 180 degrees or even
[2:20] just you know not even 180 degrees but just facing one direction, we need to actually
[2:25] add that so this is useful for like matte painting and stuff like that. So if we look
[2:30] at an example, I am going to show you two different methods here of how you can do this.
[2:34] I prefer this second method but I am going to show this one first because it will just
[2:38] kind of make things familiar with the approach that we are taking on these. So essentially
[2:43] what we have is a picture and we have this custom node. We have a few nodes here, I will
[2:47] probably drop the script in, you can download it and play around to see if you can figure
[2:51] it out but we have two custom nodes which is polar distort and offset and these are


### Polar Distort [2:52]
**Transcript (timestamped):**
[2:55] really nice especially offset for this. We also have spherical transform which is you
[3:00] know has a few more controls than polar distort but sometimes you know I don't like to use
[3:05] this node because just a little bit longer of a process whereas this gives kind of the
[3:09] same result but it is there in case you are working in a studio and maybe you don't have
[3:14] the access to custom tools off Nucapedia. So we will talk about that in just a second
[3:19] but we have the picture, what we are doing is we are taking a polar distort and we are
[3:23] converting it from rectangular to polar and essentially what this is doing is just kind


### Rectangular to Polar [3:24]
**Transcript (timestamped):**
[3:29] of wrapping this on like a pseudo sphere and you can see we have the same problem that
[3:33] we saw on our 3D sphere and we have this kind of pole on the top here and what we can do
[3:39] is pretty simple, we just take the normal picture like the original starting picture
[3:44] we have here and I will just disable the transform and what we are doing is we are just taking
[3:48] a roto shape in the center and we are just mixing the original image with the polar distorted
[3:55] image so we get something like this where we are just patching in the center and then
[3:59] what I am doing is I am taking a transform and scaling up the clouds, moving the original
[4:03] picture, fine maybe a good position to kind of blend the two images and then what we do
[4:08] is we just basically polar distort it back and if we polar distort it back you will see
[4:12] that this sort of top area if we go here you will see that it is actually stretching and
[4:17] kind of wrapping around the top and that is actually what you do want. The problem with
[4:22] polar distort is kind of custom node it doesn't work great with formats that are not square
[4:27] so that means you are going to have to do a lot of like reformat to square and then
[4:31] do this and that is not the greatest for like filtering and stuff like that so for example
[4:38] this is kind of a better way to do it so usually what I will do is I will just do a polar
[4:41] distort, I will mix the texture, convert it back and make sure it works but then what
[4:46] you want to do is basically reorganize these nodes so that you are not warping the entire
[4:51] original picture so we can actually reorganize those nodes in a more efficient way here and
[4:57] that will basically avoid that problem so essentially what we do is we just copy these
[5:01] nodes so I copy I will just kind of recreate it here, just copy these two, we copy the
[5:06] roto that we used in the kind of the key mix here, we pre multiply it so that it will
[5:12] multiply and then we just have the patch basically and then we can crop it you need to put a
[5:18] crop before the polar distort to kind of work properly and after that we can just put the
[5:23] polar distort back on and you will see that it is kind of wrapping around the top there
[5:28] and all we do is we just merge that picture over the original picture and you will see
[5:33] that we have that warped top and we are not really affecting the rest of the image, we
[5:37] didn't have to reformat to square or anything like that and we kind of avoid blurring our
[5:41] picture too much because if you do all those steps it kind of blurs your picture so that
[5:45] is the easier way to do it, preview it doing this method and then just your final method
[5:50] you just kind of reorganize your nodes in this sort of way. Another way to preview this
[5:54] to make sure it is working is to use a spherical transform node so if you put a spherical transform


### Spherical Transform Node [5:56]
**Transcript (timestamped):**
[6:01] node at the end here and we plug it in, I will just do a new one and we want to say lat
[6:06] long to rectilinear so we can say so we can see the input is a lat long which is what
[6:12] we are trying to create but we want to output this rectilinear so we switch that and what
[6:17] this basically gives you is you are kind of sitting inside your sphere and you don't have
[6:21] to do a sphere, a scan line render and a camera and a bunch of nodes and see if it looks good
[6:27] we can just use this node right here and basically this focal length is kind of like your camera
[6:32] so imagine there is a camera sitting inside the sphere so if you reduce the focal length
[6:35] make it a bit wider we can kind of see what is happening here so if you read here it says
[6:40] control alt left mouse drag in the viewer so if we have our overlay on by hitting Q
[6:44] and pointing over and we do that so control alt left click and then I start to drag around
[6:49] in the viewer we can actually rotate the camera and look around to see if that sky is looking
[6:54] how we want it and so if there is not enough texture resolution there we can play around
[6:59] with our original texture we can scale it and stuff like that but it is a really easy
[7:02] way to just get a sense of the 3D effect that we have here and so that is basically the
[7:09] quick concept around how to get that now the seam is pretty simple to fix we can see a
[7:13] seam here and that is a very simple fix to do so we can go basically to this sort of
[7:22] image here and all we want to do is an offset and then we can just add a number here so
[7:29] we say 200 or something like that we just increase that number and then we can basically
[7:33] just roto paint that seam out so we would just go here to roto paint and then we would
[7:38] just kind of make that a seamless image so we just go here set the opacity low set the
[7:43] hardness low and then we can just kind of quickly blend those two images together and I will
[7:48] just kind of do a rough job here since this is just kind of a quick demonstration so you
[7:52] see we can hide that seam and if we go back to the spherical transform and disable and
[7:59] enable we should be able to see that that seam has kind of been erased so that is kind
[8:04] of the quick idea not to spend too long on the seam there and we will just kind of move
[8:09] on here so this is the same technique down here just using a spherical transform this
[8:15] is why I kind of put it down here as an alternative it is not my favorite way of doing it because
[8:20] there is just a lot of settings you have to memorize and probably the best thing to do
[8:23] would just be to like save the settings in these two and save these as like a tool set
[8:29] so you can save your tool set if you don't have to remember but there are a few ways
[8:33] to do it here so I will just explain it real quick before we go on to this method which
[8:37] I think is the fastest and easiest so we have spherical transform and essentially what you


### Spherical Transform [8:39]
**Transcript (timestamped):**
[8:42] want to do in spherical transform is you switch it from lat long to projection fisheye and
[8:48] you can kind of play with the focal length here as well which will kind of change the
[8:53] way that this scales so if I do it from scratch here plug it in we will switch it to fisheye
[9:03] and you can play with these settings here so if you play with the sensor size if you
[9:07] increase this number here it will basically kind of shrink it down and you will see it
[9:12] is still not giving us a circle that we need so you can decrease the focal length to a
[9:17] wider focal length and you will see that we now have our entire sphere in here so the
[9:22] sensor size will kind of play with the format and usually you just want to keep it kind
[9:26] of square and getting it all seen there so something like this is probably fine we can
[9:32] try to maybe maximize the resolution just keep the circle going just directly to the
[9:36] edge and so now the trick here is we see that our pole is not facing us so it is not easy
[9:41] to paint it out with an image that looks like this so really what you want to do is you
[9:46] want to take the pan tilt roll you want to rotate this by 90 degrees so you see we are
[9:51] getting a very basically similar result to the polar distort except it is kind of in
[9:56] a square format and it is basically the same idea after that just patching a picture take
[10:01] this picture key mix it in and essentially after that we want to go to the spherical
[10:07] transform at the end and we just want to invert those two so instead of saying the projection
[10:13] as lat long we are saying the projection is fisheye and we are converting it back into
[10:18] lat long which gives us this result back and we are good to go we have basically an image
[10:23] that kind of works now of course we didn't do it for the bottom half of the image and
[10:27] you can do it if you want because we are going to have the seam and those kind of problems
[10:30] I am just doing a quick demonstration how you can get that proper kind of stretching near
[10:34] the top of the frame so I prefer this way it is very very simple we also have this so
[10:40] it is a similar concept we have the original image we I think I painted out the bird here
[10:46] I think there is like a bird in this picture but all we can do here is we pull it and
[10:51] distort it and now all we do is just mix the top of this picture with the original so here
[10:58] is the original picture mixed in so I used the roto shape just to mix those two together
[11:03] and essentially what that does is all the same work that we had to do with these nodes
[11:07] but we can do it just in a different way and we have that proper stretching and if we wrap
[11:11] this on the sphere it already works so much easier much less nodes you don't have to think
[11:16] about too much and keeping it simple which I like so after that we can paint out our
[11:21] seam so we offset it we roto paint out the seam we are good to go and then I think what
[11:26] I did here is I kind of flipped the image I did the same thing so I kind of mirrored
[11:30] it offset it again to make sure there is no seams just paint out the seams and then kind
[11:35] of key mix that back on so now we have this like cloud image that you know maybe if we
[11:38] are flying really high in the sky maybe you could put some ocean down here instead it
[11:42] would make more sense but it is just demonstration so make sure there is no seams in there and
[11:48] we can preview it again using our spherical transform so again make sure we go lat long
[11:54] directed linear and now we have our controls if we turn our overlay on with Q we can do
[11:58] control alt left mouse click and we can kind of spin around here and just make sure our
[12:02] texture is good it doesn't work from all the angles and stuff like that so kind of just
[12:06] spinning around randomly here and if you see some textures that maybe are a little bit
[12:10] too stretched that is where you want to go in and you want to play with your resolution
[12:13] so if it is the case that things are a little bit too big or too stretched that is where
[12:19] you are going to have to start shrinking your images down and kind of maybe adding more
[12:23] images so the resolution and the size of things is still something you are going to have to
[12:28] play with visually at the end result you know so I will explain that a little bit more in
[12:33] another example coming up here with a kind of space example but again if we preview this
[12:38] in 3D it is kind of working the technique is kind of working here we have a sphere with
[12:43] no seams no poles and stuff like that so that is closer to the result that we would probably
[12:48] need so we have another example down here this is something I was doing for like a VR environment
[12:54] I have this render here this is a render just a very basic CG environment for some kind
[13:00] of VR stuff that I am doing and basically this is rendered out from a 360 degree camera
[13:07] in CG so you can get these renders out very easily if you are familiar with any 3D package
[13:14] you just google how do I get a 360 camera in whatever software and so I render this out
[13:19] and basically I am using the same technique to kind of do this sort of space nebula and
[13:24] kind of put it behind these kind of windows this is going to be kind of like a glass dome
[13:29] in space kind of thing and so it is a really good way to kind of design things for a 360
[13:35] degree environment because we can easily see the layout of the CG scene as well as our
[13:42] sky that we are kind of map painting and so again if we have our 3D render with 360 degrees
[13:49] as well as our proper lat long with the stretching of course if it is not stretching at the
[13:53] top you know something is wrong you want the stretching near the poles that is kind of
[13:57] telling you that it is correct and if we have something like that we can do a spherical
[14:01] transform at the end and this is a low resolution CG render so you can see it is kind of blurry
[14:05] there it is not the highest quality just for the example but again we have our spherical
[14:10] transform we can do our little trick here rotate around and give it a second here give
[14:16] it a second to cash and we should be able to rotate around kind of in real time and we
[14:20] can get a sense for how that 360 degree environment is going to look so it is kind of a finicky
[14:26] that controls in terms of kind of spinning around here not exactly the best so you can
[14:31] play with these numbers on the side so I can say just an x I can just increase that number
[14:36] I can just use my arrow keys up spin around and just see if the lighting is working all
[14:41] these kind of things so we have like a light source from a galaxy we have a light direction
[14:44] in CG and these are the kind of things I am going to be paying attention to for doing
[14:48] some kind of 360 degree environment you know is that map painting lining up and those kind
[14:54] of things so that is about it basically how to you know get images looking like this very
[15:01] very useful especially you know if you have a whole bunch of pictures that you are map
[15:04] painting with like these these are the nebulas you can find these in the description if you
[15:08] guys need any textures like this but it is pretty awesome pretty awesome technique and
[15:14] you know you can stack different pictures as well like shrink them down and you know
[15:18] if you need more detail in certain spots you know something I have seen a lot specifically
[15:23] in like VR environments is they don't have a good sense of scale meaning like sometimes
[15:27] the stars look too big and that is kind of a map painting thing that is more an artistic
[15:33] thing you need to pay attention to rather than like this is a technical tutorial but just
[15:37] keep that in mind if you are doing any kind of map painting you know pay attention to
[15:41] stuff like this where it doesn't look good where you have stars that are too big the
[15:44] sense of scale doesn't make sense those are the things that you kind of want to improve
[15:48] there and pay attention to but yeah that is about it and thanks so much for watching hit
[15:53] like if you guys found it useful and that is about it.



---

## Captured Frames

- [1:33] tutorials/frames/360-spherical-latlong-textures-nuke-tutorial/frame_000.jpg
- [3:29] tutorials/frames/360-spherical-latlong-textures-nuke-tutorial/frame_001.jpg
- [5:28] tutorials/frames/360-spherical-latlong-textures-nuke-tutorial/frame_002.jpg
- [6:32] tutorials/frames/360-spherical-latlong-textures-nuke-tutorial/frame_003.jpg
- [8:42] tutorials/frames/360-spherical-latlong-textures-nuke-tutorial/frame_004.jpg
- [10:07] tutorials/frames/360-spherical-latlong-textures-nuke-tutorial/frame_005.jpg
- [13:07] tutorials/frames/360-spherical-latlong-textures-nuke-tutorial/frame_006.jpg
- [14:10] tutorials/frames/360-spherical-latlong-textures-nuke-tutorial/frame_007.jpg

---

## Structured Notes

### Core Technique
Converting a flat/rectilinear photo (or a 360° CG render) into a seamless lat-long (equirectangular) texture by artificially warping the poles, so it wraps cleanly onto a sphere/skydome from any camera angle — done two ways: the custom `PolarDistort` gizmo method, and the built-in `SphericalTransform` fisheye round-trip method.

### Summary
Compositing Academy explains why a plain photo breaks when projected onto a sphere in Nuke's 3D view: it shows a visible seam (left/right edge mismatch) and a "pole" pinch at the top, because true lat-long textures need deliberate warping near the poles that a flat photo doesn't have. Frame 000 shows this exact failure case — a flat sky image wrapped on a `Sphere` in the 3D viewer with a visible pole artifact. The video demonstrates two fixes: (1) a Nukepedia `PolarDistort`/`Offset` gizmo pair that converts rectangular↔polar, patched with a `Roto` mask and reorganized (via `Crop` before `PolarDistort`) so only the center patch gets warped instead of the whole image, keeping the rest of the picture sharp; (2) a cleaner method using the built-in `SphericalTransform` node set to `fisheye` projection, rotated 90° in pan/tilt/roll so the pole faces the camera, patched, then flipped back to `lat long` projection — described by the author as the fastest/simplest of the two. Both methods are checked via a second `SphericalTransform` (lat-long → rectilinear) at the end of the chain, which turns the 2D image into an interactively-navigable fake-camera preview (Ctrl+Alt+drag in the viewer) without needing an actual `Sphere` + `ScanlineRender` + `Camera` setup. The seam itself is fixed separately with `Offset` + `RotoPaint` (low opacity/hardness cloning). The video closes with a real production use case: texturing a 360°-rendered CG environment (a "glass dome in space" VR scene) with a nebula sky, using the same lat-long/rectilinear preview trick to check lighting and pole placement before committing to a full 3D render — frames 006–007 show a CG interior/dome render with a starfield mapped as its lat-long sky.

### Key Steps
1. Diagnose the problem: project a flat rectangular photo onto a `Sphere` in Nuke's 3D view — a visible seam (edge wrap) and pole pinch appear because the image lacks lat-long-style pole warping (see frame_000).
2. **Method A — PolarDistort gizmo:** feed the image into a `PolarDistort` node (Nukepedia gizmo) set rectangular→polar; this "pseudo-sphere" wrap reproduces the pole pinch predictably.
3. Patch the pole: `Roto` a circular shape at the center, use it to key-mix the original (unwarped, transformed/scaled-up) picture over the polar-distorted one so only the pole region is patched.
4. Reorganize for efficiency: `Crop` the patch region before re-applying `PolarDistort` (back to polar→rectangular) so only the small patched area gets warped/re-blurred, not the whole frame — avoids unnecessary filtering/blur on the rest of the image. `Merge` the patched piece back over the original.
5. Preview without a full 3D setup: add a `SphericalTransform` node at the end, set Input=lat long, Output=rectilinear — this simulates sitting inside the sphere; adjust `focal_length` (acts like a virtual camera lens) and Ctrl+Alt+drag in the viewer (with the Q overlay on) to look around and check pole/texture quality (frame_003).
6. **Method B — SphericalTransform fisheye round-trip (preferred/faster):** on the original image, set `SphericalTransform` to lat long → fisheye; tune `focal_length` (wider = full circular fisheye visible) and keep sensor size roughly square (frame_004).
7. Rotate `pan/tilt/roll` by 90° so the pole area faces the viewer/center of the fisheye circle instead of the edge — makes it paintable (frame_005 shows the rotated fisheye circle with pole facing camera).
8. Patch the now-centered pole the same way (`Roto` + key-mix against the original), then add a second `SphericalTransform` set to fisheye → lat long to convert back — yields a properly pole-warped lat-long image with far fewer nodes than Method A.
9. Fix the horizontal seam: `Offset` the image ~200px, `RotoPaint` over the seam at low opacity/hardness to blend it invisibly, then offset back — verify by toggling the final `SphericalTransform` preview on/off.
10. Production example: render a 360° camera pass directly from any DCC (author notes this is a one-Google-search setup in most 3D packages), bring the equirect render into the same lat-long/rectilinear `SphericalTransform` preview to spin around and check that stars/lighting/pole placement read correctly before finalizing the matte-painted sky (frames 006–007).
11. Artistic note (not technical): watch for scale mismatches in VR/360 skies — e.g. stars painted too large read as fake; this is a matte-painting judgment call, not a node setting.

### Nodes / Tools / Settings
- **Core Nuke:** `Sphere` (3D), `ScanlineRender`/3D viewer (for the initial failure demo only — bypassed later via `SphericalTransform` preview), `Roto`, `RotoPaint` (low opacity + low hardness for seam cloning), `Transform`, `Crop`, `Merge` (key-mix / over), `Offset`
- **`SphericalTransform`** (built-in Nuke node) — the star of Method B; toggled between `lat long ↔ fisheye` and `lat long ↔ rectilinear` projections; `focal_length` controls virtual-lens FOV, `pan/tilt/roll` rotates the projection so the pole lands somewhere paintable, sensor size affects framing/aspect
- **Nukepedia gizmos (Method A):** `PolarDistort` (rectangular ↔ polar remap) and a companion `Offset` gizmo — noted as not working well with non-square formats, requiring extra reformatting compared to Method B
- **Interaction:** viewer overlay toggle `Q`, then Ctrl+Alt+left-mouse-drag to orbit the fake camera inside a `SphericalTransform`-previewed lat-long/fisheye image
- **Source assets:** Unsplash sky photo (2D matte-painting case) and a low-res CG 360° camera render with a nebula texture pack (VR/game-environment case)

### Difficulty
Intermediate — no scripting, but requires spatial intuition about lat-long/equirectangular projection math and comfort reorganizing node trees for efficiency (Method A's crop-before-distort reorganization in particular).

### Foundry App & Version
Nuke (2D + Classic 3D system only — `Sphere`/3D view and `SphericalTransform` predate the USD-based 3D system that began beta in 14.0; nothing here uses or is affected by that overhaul). Exact point release not stated on screen or in the transcript; per this skill's version-tracker, a 2022 Compositing Academy upload falls in the Nuke 13.1 (Nov 2021) → 13.2 (Apr 2022) window.

### Tags
compositing, 3d-system, digital-matte-painting, roto, rotopaint, intermediate

---

## Related Tutorials
- Grading Highlights and Pools of Light | Nuke Compositing (`grading-highlights-and-pools-of-light-nuke-compositing.md`) — shares `compositing`, `digital-matte-painting`, `intermediate`; that tutorial builds a hand-painted night relight matte painting, this one builds a spherical/lat-long sky matte painting — same discipline, different projection problem.

- A new way to design VFX | Virtual Reality | Gravity Sketch + Nuke Tutorial (`a-new-way-to-design-vfx-virtual-reality-gravity-sketch-nuke-tutorial.md`), Mixed Medium VFX P1 (`mixed-medium-vfx-p1-blender-nuke-ai-embergen-vr-tutorial.md`), Nuke Compositing an Advanced CG Shockwave (`nuke-compositing-an-advanced-cg-shockwave-vfx-lookdev.md`), and [1/3] Nuke Tutorial Series (`13-nuke-tutorial-series-practical-sfx-lighting-script-overview.md`) — all also use the `PolarDistort` gizmo, each for a different purpose than this tutorial's sphere-wrapping.

- Shuffle and Channel Management | Nuke Compositing [Beginner / Intermediate] (`shuffle-and-channel-management-nuke-compositing-beginner-intermediate.md`) — shares `compositing`, `digital-matte-painting`; both are toolset/fundamentals-style explainer videos aimed at demystifying a commonly-misunderstood Nuke concept.

No other existing knowledge-base entries share enough tags for a strong cross-link yet. Revisit once other `digital-matte-painting` or `3d-system` tutorials (e.g. the 2024 "Blender + Nuke A.I Enhanced Digital Matte Painting Workflow" video, once ingested) land in the index.
