---
title: Finally! The Volumetric Tool Nuke Has Always Needed
source: YouTube
url: https://www.youtube.com/watch?v=8f2w7JxRaq4
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "not specified — free/paid 3rd-party plugin ('Volumetric Noise' by Compositing Academy), a standalone procedural volumetric cloud/fog render engine. CONFIRMED NOT related to Nuke 17.0's native Gaussian Splat/Field-node volumetric masking toolset (GeoImport/GeoReference, SplatRender, Field nodes) — this is a fully separate CG cloud/fog GENERATOR, not a splat-masking system. Same disambiguation pattern as H7dBKDLXwPo and M-iKJu9hYBk."
tags: [volumetrics, gizmo, 3d-system, digital-matte-painting, fx-simulation, compositing, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/finally-the-volumetric-tool-nuke-has-always-needed/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Finally! The Volumetric Tool Nuke Has Always Needed

**Source:** [YouTube](https://www.youtube.com/watch?v=8f2w7JxRaq4)
**Author:** Compositing Academy
**Duration:** 16m51s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Recently I was traveling across Iceland for a month, filming a variety of projects for this channel.
[0:04] One of the most incredible places was this canyon.
[0:07] As I flew my drone up through the canyon, I couldn't help but notice the parallax of these clouds.
[0:12] As a VFX artist, the incredible sense of 3D stood out to me, and I wanted to be able to create this kind of effect directly inside of Nuke.
[0:18] So I created a tool that actually makes this possible.
[0:21] The volumetric noise plugin for Nuke is a native volumetric rendering engine that allows you to arc-direct these 3D volumes.
[0:27] These two shots have CGI clouds.
[0:29] In this tool, I wanted to make the ability to actually arc-direct these volumes.
[0:33] That means different style controls, directional shaping, layered parallax, real lighting controls, and occlusions.
[0:44] We're going to compare the old-fashioned technique with traditional noise and show why volumetric noise is superior to this approach.
[0:51] So before we jump into this plugin and looking at all the settings and seeing how this works,
[0:55] I want to explain why we're doing this in the first place, and some of the real benefits you actually get out of using a tool like this,
[1:01] and why I made it in the first place.
[1:03] We've all used traditional noise, 2D noise, just a simple pattern generation, and maybe you animate it and create some simple atmosphere effects.
[1:10] That's a very common thing to do in compositing.
[1:13] But with volumetric noise, we can get a bunch of benefits that you can't do with this approach.
[1:16] A few of those reasons is light and shadow is the first one.
[1:20] Because this is truly 3D, we can actually control the light scattering, and we can get nice shadows in here as well, so we can get variation like this.
[1:28] It's not feeling too dimensional, so that alone allows us to create volumes that is just already difficult to do with just the 2D noise,
[1:35] because this is very flat, there's no sense of light direction even in this.
[1:39] Another one is layered motion.
[1:41] So if you were to animate this 2D pattern, even though it's self, even though it's just a evolve here,
[1:46] this looks something like this, it's not that interesting.
[1:49] But if we can do the same thing with the volumetric noise, here we automatically get this layered motion type of effect.
[1:55] Especially with the light and shadows, you can accentuate that effect quite a bit.
[1:59] So this already just gives you a really good start, even without the camera moving.
[2:02] So our next point here is that we have camera parallax.
[2:05] So obviously we can fly into this, it's real 3D, this is not a 2D trick, this cloud effect, it's a real render engine that gives you 3D clouds.
[2:12] So essentially you can fly over it, you can fly through it, which is for different types of effects.
[2:17] That's a pretty tricky thing to do in composing normally.
[2:19] So for example, in this shot where camera parallax is really apparent, our drone is flying straight down.
[2:25] We want to create all those layers or parallax, and that would be kind of annoying to do with normal 2D noise.
[2:30] So here I have four different volumetric render setups, basically at just different distances.
[2:36] It was easier to set up four different cubes, but we have one here that creates kind of the base layer,
[2:41] and then we have another one that creates some whispies or closer camera.
[2:44] As I hit play, you can see why the parallax is so important.
[2:47] Even if this was on 2D, we wouldn't get that sense of 3D that you get with a real cloud.
[2:54] So there's this one, then we have another one that's a little bit closer,
[2:57] and we can see those black levels are all kind of adjusting and layering over each other.
[3:01] And then we have another one that's even closer, just to give those tiny whispies and things that are super close to camera.
[3:07] So with all that, you can get some pretty interesting looking effects when you start layering it all up together.
[3:12] So in this shot, we're at a cloud where we're kind of flying through it.
[3:15] This is essentially made up of a few layers as well, so I kind of put one on the left side, put one on the right side,
[3:20] just so I can control the clouds individually, gives them some different variation.
[3:24] And then one maybe on the top of the screen, it's a bit more whispy and kind of hanging down on the screen.
[3:29] And maybe lastly, we just have like the very thick one that we're flying through in the very beginning.
[3:33] So a few grades and things like that to get the exact fade that I was looking for, but essentially same idea.
[3:40] And the old way of doing this would have been just taking like a bunch of these 2D noise cards and trying to slide them towards the camera
[3:46] and then just kind of fading them off either manually or linking them to the distance to camera and fading it.
[3:51] But it never looks as good as a true 3D volume. It's always kind of a trick.
[3:55] And we get the top edges of things as well, so we can actually get light on the edges if we have something that's more dense.
[4:00] So even though I did do some not very dense ones in the example, it could be thicker clouds you're flying through as well,
[4:06] which this approach just wouldn't work at all.
[4:08] We also have realistic density distribution.
[4:11] I've seen some 3D noise things out there before, but they don't erode the volumes in ways that are super interesting.
[4:18] And that's really what I wanted to build in this tool is not just creating the same simple pattern within 3D space,
[4:23] but rather we have actual density distribution.
[4:26] That's what happens on the real clouds that we looked at on those reference shots that we started with.
[4:31] So we have like thicker stuff and then we have this kind of tearing and then we have some that are kind of like whispy and on the edges.
[4:37] So we have all of this variation and we also have the ability to essentially control this from any direction we want.
[4:44] And it's not just like a hard cut edge that we're sort of like down here is a little bit harder, but we can control and fade that in if we want to.
[4:53] So this level of, I guess, hardness or the level of depth that we sort of erode into, this is all controllable within the tool.
[5:01] So it's really art-directable, these type of density distributions.
[5:05] And then lastly, we obviously have 3D occlusion.
[5:07] So we can actually take our 3D volume and we can occlude it against any depth data.
[5:12] So I've created some depth data from the drone footage I shot.
[5:15] And then now we have a visualizer that allows us to see where the 3D clouds are going to be spawned.
[5:20] And if I turn on occlusions, this cloud will get cut out by the depth data.
[5:23] So whether you're using a full CG environment or using plate footage and generating depth maps via various techniques, you can do this approach.
[5:31] So here's without occlusions.
[5:32] You can see it's just going through the hill.
[5:33] If I enable occlusions, I can see the hill actually cuts out and it's kind of cutting against the hill in a nice way.
[5:38] We have some controls as well with how that blend actually happens.
[5:41] So let's take a look at some of the presets in this tool.
[5:43] I'm not going to go through every single knob and setting in this video.
[5:46] I'm going to make a separate video for the people who download it and they want to see exactly how to control everything.
[5:51] But just to give a quick creative overview on how we can use this and start to get familiar.
[5:56] So essentially, we have a few presets that are already pre-coded in.
[6:00] So you can get like a basic cloud.
[6:01] You can get like ground fog.
[6:03] There's a different variations of ground fog.
[6:05] So you can get a wispier fog, different little wispies as well.
[6:10] Ones that are a little bit more curly than others.
[6:13] We have like a simple volume.
[6:14] If you just want to start with something thicker and then do the erosions yourself, that sometimes can be useful.
[6:20] There's also things like scalable cloud scapes.
[6:23] So some of these are sort of contained within a box and they're stuck the box.
[6:27] If you move the box around, the cloud will move with the box.
[6:31] But if you have one that's like world space, it's essentially some box that you can scale and we'll just keep generating noise within 3D space.
[6:37] So that's a different type of way to work with this.
[6:41] You also have things like backlit fog.
[6:43] So just to show you some of the shading effects that you can get with this.
[6:46] We can make this fog a little bit thinner or softer as well.
[6:49] So there's lots of control we have over this.
[6:52] Then we have something like a wispy cloud.
[6:56] So a little bit different than maybe a basic cloud.
[6:58] A few variations just to get started.
[7:00] Usually I just like to start with the basic cloud and you start to play with it.
[7:03] So let's take a closer look at how this is actually working.
[7:05] So the main plugin is this node.
[7:07] But there's a few nodes that will come around it in a template.
[7:10] So we can plug in depth data.
[7:11] So for example, I have a basic 3D scene here that I've set up with just a little bit of ground terrain.
[7:16] So we can take a look at some ground effects and just a dude standing here for a sense of scale.
[7:22] And we also have the camera.
[7:24] So 3D camera.
[7:25] We have a 2D roto.
[7:26] If you want to roto out certain parts, we'll take a look at that in a little bit.
[7:30] And we have a volume container.
[7:32] So this is actually what drives where this effect is going to appear in 3D space.
[7:35] So if we view the, there's a preview cube node here.
[7:38] If we view that and we click our container, we can move our container around and all that noise is going to spawn within the container.
[7:44] So this gives us a nice interface to scale our spawn points essentially and see where we're doing things in 3D space.
[7:51] We can also do some simple cuts here as well.
[7:53] So if we want to cut off an edge, there are some extra controls for eroding edges, which is better than doing it this way.
[7:59] I try to cut it with the 3D cube.
[8:01] This is more just for placement.
[8:03] If we want to move things around or maybe we want to see how it looks, we smoosh it into the terrain a little bit more things of that nature.
[8:09] All right.
[8:09] So part two of this video, we're going to speed run the rest of these options here just so we can see what all this does without making the video is super long.
[8:16] There will be a longer, more detailed video for the people who want it.
[8:18] So just to give an idea.
[8:20] So we have all these controls here.
[8:22] If you want to address density, for example, gain, gamma and density, you're all kind of control together.
[8:27] So we can control really the softness of the clouds and the sharpness of sort of where they peak together as well as density.
[8:34] So if increased, it'll have more lighting decrease could be a little bit thinner.
[8:38] So all the settings you expect from a volume.
[8:42] There's some quality and rendering settings that we won't go into in this video.
[8:45] And then there's a bunch of a road setting.
[8:47] So this is really where you dial in the look.
[8:49] There's different types of roads.
[8:50] Some come directly from the edges.
[8:52] So for example, we can a road the tops and the bottoms, but we can also control how intense or how deep that erosion goes.
[8:59] So if we kind of pull that back, we can see actually restores some some edges so we can pull all these down back to zero and we get sort of closer to the original volume.
[9:08] And we have global erosions as well.
[9:10] So these are not related to the edges, but rather sort of just eats into the clouds from all directions.
[9:15] So we can see if I reduce that it becomes more of a solid volume versus like the harsher eating and we can soften that look as well.
[9:23] So there's sort of these softening controls.
[9:26] So like I said, in the longer video, we go in a lot more detail just to grasp the deeper concepts underneath.
[9:33] There are these distortion fields as well.
[9:35] So one interesting thing is that once the base noise is generated, there is distortion and turbulence.
[9:40] And so what these do is it actually takes the noise and kind of pushes it around in 3D space.
[9:45] You can imagine there's like an invisible grid over the top of the noise and you're pushing that through that sort of distortion grid.
[9:52] So you can change the size of that grid and there's some creative techniques we go into in the longer video that I can show.
[9:58] And it's pretty cool for it, especially for animated clouds.
[10:01] You can get some very interesting results there.
[10:04] Now lastly, there's like fades.
[10:06] So if you want like a softer fade, you can fade off like the right side.
[10:09] For example, it's more of a gradual fade.
[10:11] So the edge breaks up edge breakups and the crumbles are really for this cloudy look.
[10:17] Whereas the phase is if you just need to have a soft fade off.
[10:20] Now here's the occlusion setting so we can use enable occlusion and that will cut it out against whatever depth that you give it.
[10:25] So there's P data or depth data.
[10:27] Now, because this is not supporting deep compositing, there are some extra controls here so you can bias it.
[10:32] So it's kind of like pushing it further into depth or or closer to us.
[10:37] You can either way.
[10:38] And there's also some essentially contour softness.
[10:41] So what this does is because sometimes P data will have aliasing or depth data like this.
[10:47] What this contour softness does is actually a 3D blur.
[10:51] It's not a 2D effect to the data coming in, but rather it's taking the actual 3D position data and scattering it in 3D space,
[10:58] which is really cool because you can you can fix a lot of those alias problems.
[11:01] And that will for the majority of shots, you can actually just have the P in depth that will and that will be enough.
[11:06] You won't need the deep.
[11:06] Now, if you have extreme motion blur or tiny, tiny edges like leaves or tiny grass, you're still going to want a deep compositing approach.
[11:14] So the goal of this plug-in is to support maybe 60 70% of situations, but you know, not situations like that.
[11:21] We also have manual masks.
[11:22] So if I plug in a roto here, we can eject any kind of alpha we want into the cloud.
[11:27] So if I hit this enable, essentially it's putting it at a certain distance into the into the clouds, basically like a deep merge.
[11:34] You can think of it like that if you're familiar with deep compositing.
[11:37] But what this useful for is if you have like a roto of a person, for example, and it had motion blur, we could project that into the clouds.
[11:45] It looks like the person standing in the center of the cloud.
[11:47] Essentially, it's a way to inject data into the center with motion blur.
[11:50] So it's a bit different than peer depth because we can get those soft edges.
[11:54] So just nice to have as an alternative.
[11:57] There's also some optimization controls.
[11:58] So we don't want to process clouds.
[12:00] We talked more about it in the technical video, but we don't want to process areas that don't have any clouds.
[12:04] So we can turn on optimization slicing.
[12:06] So this is essentially previewing what is being calculated within this space.
[12:10] And we can adjust this and reduce our calculation size if something is off screen or there's a lot of empty space.
[12:16] Empty space is not good.
[12:17] We don't want to calculate that space.
[12:19] So we can we can slice those off.
[12:21] And we can also use something called space skipping, which will also skip empty spaces a little bit better.
[12:26] There's a calculation going on in here that sort of surges for empty spaces.
[12:30] You got to be careful with it not to reduce quality, but sometimes this can reduce the calculation as well.
[12:34] Just to mention as well, the debug, you can actually hit a heat map and you can see what is actually being calculated.
[12:39] So if I turn on space skipping with the heat map, you can see it actually is reducing the amount of calculations necessary.
[12:45] Or if I turn on the slicing optimization, we can cut off parts that it doesn't even matter if it's especially if it's like underneath the the ground plane.
[12:52] So there's a bunch of controls here to optimize the render speed.
[12:56] Honestly, the render speed is pretty fast in general.
[12:58] Like you can even at high samples, you can actually iterate pretty quickly and it renders in maybe a half a second or a second per frame.
[13:07] So it's pretty fast.
[13:08] So you don't have to do crazy optimization, but I did want to include it all these settings just in case.
[13:13] So we can if we have a very heavy scene or you're trying to do really dense clouds, maybe you'll need those settings.
[13:19] We also have lighting and shading so we can control the base cloud color and the sunlight color.
[13:23] So that's going to be like sort of the ambient color and the light that's actually hitting it.
[13:28] We have the intensity of the ambient so we can bring that up and have more balance if you want.
[13:32] And we can also turn out scattering.
[13:34] This will give a little bit more realistic results sometimes if you're doing a lot of backlighting stuff.
[13:38] So in the example of the backlit fog, this is turned on and you can essentially have like a fall off of light inside the volume itself.
[13:47] Whereas the direct light is not going to have that sort of fall off.
[13:50] So that's kind of what this is talking about.
[13:53] Shadows, we have shadow steps.
[13:54] It's kind of shadow quality.
[13:56] And we also have the shadow intensity if you want to manually just reduce certain things.
[14:00] We can also do the bias like a bias is not probably photo real in terms of the actual scattering, but sometimes you just want to adjust the look.
[14:06] Like if I just wanted to cheat this little bit and like pull the shadow up a little bit higher.
[14:11] This is cool because you can just sort of make it look slightly different.
[14:15] Even though it's kind of a cheat, it's nice control to have to be able to modify where those shadow rays are starting.
[14:20] We also have things like shadow jitter.
[14:22] If you have any any distinct lines that are a little bit too sharp, you can kind of soften those things.
[14:27] That's pretty much it for the lighting.
[14:29] Now we also have motion blur.
[14:30] We can actually output motion vectors from the clouds.
[14:33] So this will get the motion vectors from the camera as well as the movement of the clouds themselves.
[14:37] So if we switch this to velocity and we output this right now, there's no velocity because the camera isn't moving on the first frame.
[14:44] But if we move into let's say the first frame, we can get motion vectors.
[14:48] So this is pretty good for motion blur.
[14:49] And motion blur on clouds is pretty forgiving.
[14:52] We don't need to do completely rendered heavy motion blur on this.
[14:57] Most situations going to work perfectly fine.
[14:59] So this is better than a 2D solution actually gives us a motion vector.
[15:03] So you would render this separate.
[15:05] You'd have the beauty and you'd render the vector separately as a precomp.
[15:08] And then you just do your normal vector blur and that will add the motion blur.
[15:11] Now lastly, one of my favorite controls is this preview mode.
[15:15] So this if it's normally set to render, but if we switch it to points, we can get a point cloud.
[15:21] And if we do a position to points right after that and set it to RGB, we'll see the 3D clouds in 3D space.
[15:27] This is very, very useful for essentially knowing where we want to place this.
[15:31] So if we like 5 view this at the same time so you can see our container, I double click that.
[15:36] We can move this around and we can see that that point cloud moves with the box here.
[15:42] So if we play with our erosion controls here and we go down here and let's say, let's say we want to road the right side.
[15:48] So we wrote it, we can see that that's happening in real time and we can see all the holes and different things,
[15:53] which is really cool, especially for trying to figure out your occlusions or just exactly where you want to see that noise appearing within 3D space.
[16:00] Very, very useful.
[16:01] I've used it every time I've sort of been as I've been building this tool.
[16:05] So switch this back.
[16:07] And that's fine.
[16:07] And there's other controls here like sparsity.
[16:09] So if you increase this, it'll just render a few less points.
[16:13] If you just don't want so many in 3D space, maybe it's a little bit heavy if you have a very heavy cloud in general,
[16:18] hasn't been heavy, but just in case.
[16:20] And also, if you don't see anything appearing, just double check your preview alpha cutoff.
[16:25] So it's searching for a certain level of alpha, but if it's a very, very low density cloud, it might not be seeing it.
[16:32] So you just want to reduce that number to a lower number.
[16:35] So if it's a very high number, it's not going to show you your full cloud.
[16:39] It's only showing you the densest parts of your cloud like this.
[16:42] So you just got to lower that down to something that is capturing the entire volume essentially.



---

## Captured Frames

- [0:12] tutorials/frames/finally-the-volumetric-tool-nuke-has-always-needed/frame_000.jpg
- [1:20] tutorials/frames/finally-the-volumetric-tool-nuke-has-always-needed/frame_001.jpg
- [2:36] tutorials/frames/finally-the-volumetric-tool-nuke-has-always-needed/frame_002.jpg
- [5:12] tutorials/frames/finally-the-volumetric-tool-nuke-has-always-needed/frame_003.jpg
- [7:05] tutorials/frames/finally-the-volumetric-tool-nuke-has-always-needed/frame_004.jpg
- [8:22] tutorials/frames/finally-the-volumetric-tool-nuke-has-always-needed/frame_005.jpg
- [15:15] tutorials/frames/finally-the-volumetric-tool-nuke-has-always-needed/frame_006.jpg

---

## Structured Notes

### Core Technique
Introduces "Volumetric Noise" — a free/paid third-party native volumetric rendering engine plugin for Nuke that generates true 3D CGI clouds/fog directly inside the node graph (not a 2D noise trick), with art-directable density erosion, layered parallax, real 3D lighting/shadows, motion vectors, and occlusion against depth data — built explicitly to replace the old "stack several 2D noise cards and fade by camera distance" fake-volumetric technique.

### Summary
Inspired by real drone footage of cloud parallax in an Iceland canyon, the author built a genuine 3D volumetric renderer as a Nuke plugin, arguing traditional 2D noise atmosphere tricks fail on four fronts that this tool fixes: (1) light and shadow — because the noise is a true 3D volume, it can be lit and shadowed like a real cloud instead of reading flat; (2) layered motion — animating the volume naturally produces parallax-rich layered movement that a 2D pattern can't replicate; (3) camera parallax — since it's a real 3D render engine, the camera can fly through/over the volume with correct depth cues, demonstrated by stacking up to 4 volume containers at different distances to build cumulative parallax layers; (4) realistic density distribution and erosion — dedicated erosion controls (edge erosion plus global/all-direction erosion) sculpt believable torn, wispy, thick-vs-thin cloud structure rather than a uniform noise pattern, fully art-directable per direction. A 3D occlusion system lets the volume cut out against depth data (from a full CG scene's P-pass or from photogrammetry/generated depth on plate footage), with bias and "contour softness" controls (a true 3D blur/scatter on the depth data itself, not a 2D blur) to fix depth-data aliasing — sufficient for ~60-70% of shots; extreme motion blur or fine detail (leaves, grass) still needs full deep compositing. The tool ships with presets (basic cloud, several ground-fog variants, simple volume, scalable/world-space cloudscapes, backlit fog, wispy cloud) and is driven by a small node template: the main Volumetric Noise node, a 3D volume-container cube that defines where noise spawns in space, a preview-cube node, an optional 2D roto for masking, plus scene camera/geometry. Key controls include gain/gamma/density (softness vs. sharpness of the cloud peaks), edge vs. global erosion, distortion/turbulence fields (push the base noise through a 3D distortion grid for animated, non-repetitive movement), edge fades, occlusion (with bias + contour softness), manual mask injection (project a roto — e.g. a person silhouette with motion blur — into the volume like a deep-merge, so it reads as embedded in the cloud), render optimization (slicing + space-skipping with a heat-map debug view to visualize what's actually being calculated), motion-vector output (renders separately as a precomp velocity pass, comped with a standard vector blur — clouds tolerate soft motion blur well so this is usually sufficient), lighting/shading (ambient/base cloud color, sunlight color and intensity, an out-scattering toggle for backlit falloff, shadow steps/intensity/bias/jitter), and a "points" preview mode that renders the volume as a 3D point cloud (via Position-to-Points, viewed as RGB) for fast, real-time placement/erosion feedback without waiting on full raymarched renders — described as one of the most useful features while iterating.

### Key Steps
1. Set up a basic 3D scene: camera, any needed CG/proxy geometry (e.g. ground terrain, a scale reference), and optionally depth/position data for occlusion.
2. Add the Volumetric Noise node plus its supporting template nodes: a volume-container cube (defines the 3D spawn region), a preview-cube node (visualizes the container in the viewer), and an optional 2D roto for masking.
3. Move/scale the container cube in 3D to place and size where the volume noise will spawn.
4. Pick a starting preset (basic cloud, ground fog variants, simple volume, scalable/world-space cloudscape, backlit fog, wispy cloud) as a base rather than starting from raw settings.
5. Dial in density via gain/gamma/density controls, then sculpt shape with edge erosion (per-direction: top/bottom/etc.) and global/all-direction erosion for a torn, layered, realistic cloud structure instead of a uniform blob.
6. Add distortion/turbulence to push the base noise through a 3D distortion field for non-repetitive, animated movement — tune the field's grid size for different creative results.
7. For camera-parallax-heavy shots (e.g. a drone flying straight down through clouds), stack multiple volume containers at different distances (e.g. 4 cubes: base layer, mid wispies, close wispies) rather than relying on one container, to build up layered depth.
8. Enable occlusion and feed it depth/P data (from CG or generated from plate footage) so the volume correctly cuts out against real-world geometry; use bias to push the cut closer/further and contour softness (a true 3D scatter on the depth data) to fix depth-map aliasing.
9. Optionally inject a roto mask (e.g. a person's silhouette with motion blur) to embed foreground elements inside the cloud volume, deep-merge-style.
10. Tune render-speed optimizations if needed: slicing to skip empty regions, space-skipping to auto-detect and skip empty 3D areas, verified visually via the heat-map debug overlay — though the plugin already renders quickly (roughly 0.5-1 second/frame even at high samples) so this is rarely necessary.
11. Set up lighting: base/ambient cloud color, sunlight color/intensity, enable out-scattering for backlit fog looks, and dial shadow steps/intensity/bias/jitter for the desired shadow quality and softness.
12. Render a separate motion-vector/velocity pass (camera + cloud movement) as a precomp, then apply a standard vector blur in comp rather than relying on expensive native motion blur.
13. While iterating, switch preview mode to "points" (paired with Position-to-Points, viewed as RGB) to see the volume as a fast-updating 3D point cloud for placement and erosion feedback; adjust sparsity and the preview alpha cutoff if points don't appear (low-density clouds need a lower cutoff to show the full volume, not just the densest core).

### Nodes / Tools / Settings
- Volumetric Noise — third-party plugin/main node (Compositing Academy); Properties panel sections: Presets, Noise Settings, Volume Transform, Quality, plus separate Erosion, Distortion, Occlusion, Lighting/Shading, Motion, and Preview control groups
- Volume-container cube node — defines the 3D spawn region for the noise, moved/scaled in 3D
- Preview-cube node — visualizes the container bounds in the 3D viewer
- 2D Roto — optional mask input for manual injection (deep-merge-style embedding of foreground elements into the volume)
- Inject 2.5D Mask (seen in node graph) — related mask-injection node in the plugin's template
- Position to Points — native Nuke node used with the plugin's "points" preview mode to visualize the volume as a real-time-friendly point cloud
- Controls: gain/gamma/density, edge erosion (per-direction) + global erosion, distortion/turbulence field size, edge fades, occlusion (bias, contour softness/3D blur), optimization (slicing, space-skipping, heat-map debug), motion-vector/velocity output, lighting (ambient/sunlight color+intensity, out-scattering toggle), shadows (steps, intensity, bias, jitter), sparsity, preview alpha cutoff

### Difficulty
Advanced — a full volumetric-rendering feature set (erosion, distortion fields, occlusion against depth data, lighting/shadow) aimed at compositors already comfortable with 3D concepts and depth/position passes; author explicitly defers most detailed knob-by-knob explanation to a separate longer tutorial for people who download the tool.

### Foundry App & Version
Nuke; exact version not stated on-screen. Volumetric Noise is a third-party plugin (Compositing Academy), not a Foundry-native feature. Explicitly confirmed NOT related to Nuke 17.0's native Gaussian Splat support or Field nodes (non-destructive volumetric masking of splats/3D data) — this plugin is a standalone procedural cloud/fog RENDER engine, conceptually closer to a Houdini pyro/volume system ported into Nuke's node graph than to Nuke's native splat-masking tools. Same "not native" disambiguation pattern as "I Made VFX Relighting WAY Better in Nuke" (H7dBKDLXwPo) and "The BEST Way to Use Normals to Relight in Nuke" (M-iKJu9hYBk).

### Tags
volumetrics, gizmo, 3d-system, digital-matte-painting, fx-simulation, compositing, intermediate

---

## Related Tutorials
- I Made VFX Relighting WAY Better in Nuke (tutorials/i-made-vfx-relighting-way-better-in-nuke.md) — shares gizmo, same channel's pattern of releasing paid/free native-feeling 3rd-party tools alongside a demo, same disambiguation-from-native-splat-features theme.
- The BEST Way to Use Normals to Relight in Nuke (NEW Toolset) (tutorials/the-best-way-to-use-normals-to-relight-in-nuke-new-toolset.md) — shares gizmo, compositing; same "not native Gaussian Splat toolset" disambiguation.
- Can I Create a Speeder Chase on a TINY Greenscreen? (tutorials/can-i-create-a-speeder-chase-on-a-tiny-greenscreen.md) — shares Iceland drone-footage sourcing and digital-matte-painting/compositing pipeline overlap (same filming trip referenced).
