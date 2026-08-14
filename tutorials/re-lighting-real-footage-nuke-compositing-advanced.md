---
title: Re-lighting Real Footage | Nuke Compositing [Advanced]
source: YouTube
url: https://www.youtube.com/watch?v=VYjmvB6d9NA
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke / NukeX (3D camera tracking + Real Light node require NukeX)"
version: "not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)"
tags: [relighting, 3d-system, camera-tracking, channels, aovs, digital-matte-painting, advanced]
extraction_status: complete
frames_dir: tutorials/frames/re-lighting-real-footage-nuke-compositing-advanced/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Re-lighting Real Footage | Nuke Compositing [Advanced]

**Source:** [YouTube](https://www.youtube.com/watch?v=VYjmvB6d9NA)
**Author:** Compositing Academy
**Duration:** 16m26s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, just here with another tutorial. This is a technique that a lot of people seem not to know about.
[0:06] So I figured I'd put a video up and just quickly go over what this topic is about.
[0:11] So if we look at our original footage here, this is what we're starting with.
[0:15] So this is about 100 frames long, just a drone shot rotating around this hill.
[0:21] And so I'm not going to play the whole thing because it's not cached, but that's kind of what we have.
[0:28] So this is kind of rotation. So what's really cool about this specific technique I'm going to teach you guys is with the depth generator node.


### The Depth Generator Node [0:32]
**Transcript (timestamped):**
[0:35] Just a quick example of what we can actually do with that depth generator pass.
[0:39] This is just a quick comp. By no means would be completely final, but this is sort of like a real light using kind of a depth pass,
[0:49] normal pass and position pass. So I'll just quickly go over those individually so we can see how to get this sort of result.
[0:58] So what we have here is a 3D camera tracked scene. So I already have solved the 3D camera.
[1:04] So if I hit tab here, you can see if I double click the point cloud, you'll see that we have this already solved.
[1:13] So if you have this setup already solved, and this technique really works best with shots with a lot of parallax.
[1:21] So you see our cameras rotating and traveling quite a bit in this scene, which is what's going to allow us to do this effectively.
[1:30] So if I double click the depth generator node, we have a couple settings in here when we're using it.


### Depth Generator Node [1:31]
**Transcript (timestamped):**
[1:36] So to get those maps that we need, it's really simple.
[1:40] And pretty much if you hover over any of these with your mouse, it describes pretty in detail what each slider does.
[1:47] For example, depth detail, noise, strength, if you hover over easily, okay, matching pixels in between frames, increase to force the matches.
[1:57] For example, where fine details are missed.
[1:59] So you can play around with these settings when you're going to use this, but you don't have to really mess around with it that much.
[2:05] So all you really need to do is hook in your camera and hook in your source, and you analyze the sequence.
[2:11] And after you've done that, what you want to do, I'll create a fresh one just to show you guys.
[2:17] So I'm going to plug in my camera and plug in my source footage.
[2:23] And so what you want to do is you want to have this set to depth 1 over Z, which is the default.
[2:31] And you also want to export these two other maps here.
[2:34] So we want position, and normally these two channels aren't actually here.
[2:38] So what you normally have to do is click this box, go down to new, and you'll type in position.
[2:44] And then you'll hit this button RGBA, and it will automatically fill these boxes with red, green, blue, alpha in the new channel position.
[2:52] And you do the same thing for this normal point.
[2:56] So you say surface normal, go to new channel, say normals.
[3:02] You press this button.
[3:04] So it's going to create a channel named normals, or channel set called normals, with these channels stored in it.
[3:11] So if that's confusing to you, if you're a complete beginner, this might be a little bit complicated.
[3:16] I have classes going over channels and 3D system and CG compositing, so that's all available in the description below if you're interested.
[3:24] But so this is what we have, and we hit OK.
[3:26] And so what we're going to get now is if you were to analyze the sequence, I'm not going to do it because it takes a couple minutes to process.
[3:33] If you analyze the sequence, and you'll notice that you actually get your channels here now.
[3:39] So we have a depth channel, a normals channel, and a position pass channel, or channel set rather.
[3:47] So if I look at position, normals, or depth, we have all those utility passes.
[3:54] And if you guys aren't familiar with utility passes, again, that's covered in my Nuke 303 CG compositing course on how to use those channels.
[4:03] So I'll just give you guys a couple examples of how to actually use them here with what we're working with.
[4:10] So let's take our pre-comp footage.
[4:14] So what I did was I took that depth generator and I wrote it out.
[4:17] So I took it and I saved out a file called depth underscore, you know, the three hashtags, so it'll render out an image sequence.
[4:26] And then I set it to 32-bit float.
[4:30] This is important. It's under the data type. You want to set it to 32-bit float.
[4:35] And you want to turn off the compression.
[4:37] And these two settings are important because these special utility passes.
[4:42] So we're storing 3D data sort of in these pictures.
[4:46] So, you know, distance across this geometry is what's being stored.
[4:53] So we have to make sure there's no compression. Otherwise, you'll lose some of that data.
[4:58] But once you have this rendered out, let me show you guys what it's actually useful for.
[5:01] So I'm going to start with depth because that's the most easy to explain.
[5:06] So let me just re-render that. That's supposed to be depth.
[5:12] Okay, so we have our footage and we have our depth pre-comp.
[5:17] See this one's called depth.
[5:19] And if now if I shuffle out the depth into the RGB and A, just so we can see it here in RGB and A,
[5:26] we see that we have this kind of foggy image here.
[5:30] And that's representing the distance from the camera of our hill.
[5:34] So it's actually created this depth map just from our live footage, which is really awesome.
[5:40] So what I can do is I inverted this picture and then I graded it down.
[5:48] So if you look here in the grade, it's set to 0.99.
[5:52] So I took this black point slider and I started sliding it all the way up until I start to see something.
[5:58] And you see that the image starts to kind of pop in and out.
[6:01] So then I just take my up and down arrow keys and just adjust that until we start to get like a kind of a faded gradient result.
[6:09] And that's what I want.
[6:10] So what I'm doing is actually kind of creating like fog across our real scene.
[6:15] So now that I have this alpha that we have created, if I look at the RGB and A channel, that's what we've created.
[6:21] And by the way, when I was grading this, I made sure to switch this to RGB and A.
[6:27] I plug this into a grade and we say it's being masked by the alpha RGB dot alpha.
[6:34] So the alpha that we just created over here.
[6:36] And now when I'm lifting, we're actually adding something that looks like fog to our scene.
[6:43] So this is how you could create fog in a scene that has absolutely no fog.
[6:47] And normally you'd have to do roto shapes or something like that.
[6:51] But if you can get away with this, if there's a lot of parallax in your scene, you can actually use this depth map to create a more realistic fog.
[6:59] And what's really awesome about this as well is, you know, you can play with your level of fog really easily.
[7:04] I just go to the black point and I click after the two numbers and I start using my up and down arrow keys.
[7:09] You see, I can slide that fog along the surface.
[7:14] So you could do all kinds of effects with this.
[7:16] You can make it look like you're flying through a cloud.
[7:18] You know, you could, you know, easily adjust your fog levels in this way.
[7:25] So this is just another example, a softer fog.
[7:30] So we just compare the two alphas.
[7:31] That was a little bit more harsh.
[7:33] This one, I played a bit with the gamma and the black point.
[7:37] So that's how you can play around with the depth.
[7:40] Okay, so the next one we have here is the position.
[7:42] So I have the depth, normals and position.
[7:45] Those are the three we rendered out.
[7:47] So I have our basic footage here and I have shuffled out the position pass into the RGB and a.
[7:58] So that takes the position channel set and it puts it into our normal red, green, blue, alpha image.
[8:05] So our normal kind of image data stream.
[8:09] That's kind of how you can think of it.
[8:12] So this tool is a custom tool.
[8:14] You can download this script if you're interested.
[8:17] This was made by Adrienne Herr in 2016.
[8:20] I think it's available on Nucopedia.
[8:21] You can also find it there.
[8:22] But if you want to just get it here in the script, you can download it as well for free.
[8:28] So what this tool does is I explained it in my Nuc 303 class CG composing class.
[8:34] But you can take this little picker here and we have this really bizarre colorful image.
[8:41] And what this image actually is representing is the 3D data in our scene.
[8:46] So if I hit the alpha while I'm taking this color picker.
[8:49] So I'm sampling by holding a control or command on Mac.
[8:55] Is it?
[8:56] Yeah, I think it's command using a Windows keyboard at the same time here.
[9:00] But yeah, so holding command on Mac or control on Windows, you see this number is changing while I'm sampling it.
[9:06] But if I hit the alpha channel, you'll see actually what's happening here is we're getting a 3D bubble based on the position that we've rendered out.
[9:15] So I can move this thing around and create an alpha based on this position.
[9:21] And you see we have a lot of detail.
[9:23] We have all these little trees and all the little bumps that we got from the parallax.
[9:27] And so that's why I said it works a little bit better when your shot has a lot of parallax.
[9:31] It captures a lot of detail.
[9:33] So we can use this alpha.
[9:35] Let's say if I stick it on the top of this hill, we have that alpha saved here.
[9:39] And now if I go to a color grade, you can see we can grade the top of that hill based on that alpha.
[9:45] And what's awesome about this is it's going to stick to our surface.
[9:49] So if I hit play, that alpha is actually going to stick to our scene.
[9:53] And we don't have to do anything like placing cards or anything like that.
[9:57] We just have a color correction that's sticking and we have a really nice alpha, especially on the edges with the trees.
[10:04] So that's really a pretty cool example of, you know, you can get creative with this and come up with different ideas.
[10:12] The last one we have is the normals.


### Normals [10:15]
**Transcript (timestamped):**
[10:16] And so normals are used for relighting scenes or CG or whatever you're doing.
[10:24] Basically normals just stores the direction of a face of geometry.
[10:31] We don't have any geometry here. It's just a 2D image.
[10:34] But if we just take a look at what the normals pass looks like, it looks really crazy.
[10:39] But what we need to do is we need to shuffle that into our main image.
[10:44] So we have our footage here and we have our depth kind of pre-comp that I saved out over here.
[10:52] So we'll take the depth pass and what we need to do is say we create a shuffle node.
[10:59] And we say, I'll just restart it just so it's easier visually.
[11:05] So I plug it in and plug in A.
[11:08] And what I want to do is I want to copy what's in this picture into this data stream.
[11:13] And the reason we have to do that is because that's how this node is going to recognize it.
[11:17] So they need to be in the same stream.
[11:20] You can't have the normals here and the color picture here.
[11:24] So what we do is, so we say from A, so we see in the shuffle node, we see B and B.
[11:34] We want to copy the data in from A and put that into B.
[11:38] So we want to switch this to A and say normals.
[11:43] And then we want to copy that into the B stream for normals.
[11:49] So I'm going to switch this little box to normals.
[11:52] And then I'm just going to take this and drag it.
[11:56] So you see that these lines are copying.
[11:58] So we see from A into B, so this is B, A into B and we're copying the normals.
[12:05] So normals red, normals green, normals blue.
[12:07] So we've copied that channel.
[12:09] So now if I view this and I look at the channel normals, we'll see that that data is there.
[12:14] And if I look beforehand, you see it's not there.
[12:17] So that's what we've done.
[12:18] We've just copied this layer sort of into this stream.
[12:25] All right, so now that we've done that, if we go to the real light node,


### The Real Light Node [12:27]
**Transcript (timestamped):**
[12:30] and if you've used this node, you know how it works.
[12:34] But basically you need to plug in a material.
[12:36] So you can plug in a nuke material, like basic material is one.
[12:40] You could also type in a fog.
[12:43] That's another one.
[12:44] This is more of a metallic looking material.
[12:47] But you need your camera, your material and your color, which is your background.
[12:51] And also light.


### Direct Light [12:52]
**Transcript (timestamped):**
[12:52] So I'm using a direct light, which is like a sun.
[12:55] And if we look at that and double click in the real light node,
[12:59] and you'll see that I've set the normal vectors to normals.
[13:02] So it's picking up that channel that we created.
[13:05] And now we can actually create a light based on that scene.
[13:08] So we're getting an alpha that looks like this.
[13:11] And if I just quickly show you what that looks like through a grade.
[13:16] So I've created that alpha and I'm plugging that into a grade and grading a little bit of orange.
[13:21] And you can see now we're actually starting to get some kind of light hitting on the tips of these hills.
[13:27] So it actually looks like now we're getting like a sunset.
[13:30] So this is a way you could create like a golden hour effect, kind of cheat it.
[13:34] And that's pretty cool.
[13:36] And also what's awesome about this is you can rotate this light.
[13:39] So if I double click that light and I rotate it,
[13:43] we can see that that actually can be manipulated.
[13:47] You know, if we want light on this side of the hill, we can do that.
[13:51] We can rotate this light around in 3D space and get different results.
[13:56] So you see now we have the light on this side.
[13:59] So you could use multiple, you could create multiple alphas with this
[14:03] and you know, totally realize a scene, you know, using this technique.
[14:08] So those are the main three main techniques.
[14:12] I'll just show you guys again what I started the video with here combining all those techniques.
[14:16] And this is just again a really quick comp.
[14:19] This is not, you know, final quality.
[14:22] You would need a lot of finessing to make it 100% realistic.
[14:26] But if I just break it down here and go through,
[14:31] this is just sort of the real light that we have using those techniques.
[14:35] So we have the original and we have kind of a foggy sort of golden hour effect starting to happen here.
[14:41] Again, you would have longer shadows and more highlights on the rocks
[14:46] and maybe more reflections and pinging highlights and all kinds of stuff.
[14:50] You really, really want to make it more realistic.
[14:53] But again, this is just to demonstrate the class.
[14:57] So I'm not going to go through it entirely because I've already explained the techniques,
[15:03] but maybe the one you guys are curious about is the fog.


### Fog [15:06]
**Transcript (timestamped):**
[15:07] So just to show you guys how I did it,
[15:10] it's just the depth pass doing the black and white balance grade,
[15:15] or sorry, white point and black point grading.
[15:19] And what I did was actually took a gray constant and graded up a little bit of sunlight into it using a radio.
[15:29] And I just masked that by the depth.
[15:32] So we get this kind of sunlight filling the volume of the smoke that we've created.
[15:38] And then I just basically put that over the top and that's how we get that sort of effect there.
[15:44] And then again, just a little bit of relighting on the tops and some final color grading at the end
[15:51] and just a crop to give it a bit of a wide sort of look.
[15:55] So you can make this more realistic as well.
[15:57] You can break it up with the atmosphere and all kinds of stuff.
[16:00] If this was like a final production shot, but hopefully you guys got something useful out of this video.
[16:06] And again, if you like the video, hit like.
[16:08] It really helps with the YouTube algorithm and helping the channel grow.
[16:12] And it will allow me to produce more content like this.
[16:15] And if you really like it, hit the subscribe button as well.
[16:17] And you can hit the little bell to get notified every time I put a new video out.
[16:22] And yeah, so thanks for watching.



---

## Captured Frames

- [0:35] tutorials/frames/re-lighting-real-footage-nuke-compositing-advanced/frame_000.jpg
- [2:11] tutorials/frames/re-lighting-real-footage-nuke-compositing-advanced/frame_001.jpg
- [5:26] tutorials/frames/re-lighting-real-footage-nuke-compositing-advanced/frame_002.jpg
- [8:41] tutorials/frames/re-lighting-real-footage-nuke-compositing-advanced/frame_003.jpg
- [11:05] tutorials/frames/re-lighting-real-footage-nuke-compositing-advanced/frame_004.jpg
- [13:16] tutorials/frames/re-lighting-real-footage-nuke-compositing-advanced/frame_005.jpg
- [13:56] tutorials/frames/re-lighting-real-footage-nuke-compositing-advanced/frame_006.jpg

---

## Structured Notes

### Core Technique
Deriving synthetic depth, position, and normal utility passes from ordinary live-action footage — using a solved 3D camera track and the `DepthGenerator` node — to relight, fog, and color-grade real footage as if it were CG, entirely without roto or 3D geometry.

### Summary
Starting from a ~100-frame drone shot circling a hill (high-parallax footage, 3D camera already tracked/solved), the video shows how `DepthGenerator` synthesizes depth, position, and normal utility passes purely from parallax across frames — the more camera movement/parallax in a shot, the better the derived passes. Three independent techniques are demonstrated: (1) **Fog** — invert and heavily grade the depth pass (black point pushed to ~0.99) into a soft alpha, then use it to mask a `Grade`/lift so distance-based haze appears in a scene that had none, with black-point scrubbing letting the fog "travel" through the volume; (2) **Position-based selection** — shuffle the position pass into RGB/A, then use a custom Nukepedia 3D-position-picker tool (Adrienne Herr, 2016) to sample a point in the colorful position-encoded image and generate a alpha "bubble" around that 3D location (e.g. the top of a hill) that sticks naturally to the surface across the whole shot with no roto/tracking needed, then color-correct through that mask; (3) **Relighting** — shuffle the normals pass into the main image's `normals` channel set via `Shuffle` (copying from stream A into stream B so the Real Light node can read it), then feed a `RealLight` node a material (Basic Material, or presets like Fog/metallic), a Direct light (sun-like), the camera, and the background/color, producing a lightable alpha that can be graded orange for a fake "golden hour" rim/highlight look and re-oriented in 3D by rotating the light. All three passes are combined at the end into a rough demo comp (fog + relight + grade + crop) to fake a sunset atmosphere over the drone footage. Critical technical note: when writing out these utility passes (e.g. as `depth.####.exr`), they must be rendered at **32-bit float** with **no compression**, since they encode real-valued 3D distance/position/direction data that any lossy or lower-precision format would corrupt.

### Key Steps
1. Solve/import a 3D camera track for the shot (a point-cloud/solved scene is a prerequisite) — works best on shots with strong parallax (camera rotating and translating through the scene, not locked-off).
2. Add a `DepthGenerator` node; plug in the camera and the source footage; leave most sliders (depth detail, noise, matching strength) at default — hover tooltips explain each if tuning is needed.
3. In the DepthGenerator, keep the default depth output (`1/Z`), and additionally create two new output channel sets via the "New" + RGBA button: one named `position` (world-space XYZ) and one named `normals` (surface normal direction) — these aren't present by default and must be explicitly added.
4. Run "Analyze Sequence" (takes a couple of minutes) to actually compute the depth/position/normals data across all frames.
5. Write out each needed pass (e.g. depth) to its own EXR sequence at **32-bit float**, with **compression turned off** — required to preserve the real-valued 3D data without corruption.
6. **Fog recipe:** Shuffle the depth pass into RGB+A, invert it, then push a `Grade` node's black point up toward ~0.99 (fine-tune with arrow-key nudges) until a soft gradient/faded alpha appears; mask a second `Grade` (lift) by that alpha (set to `rgba.alpha`) to add distance-based haze/fog into footage that had none; scrub the black point value to move the fog "front" through the scene.
7. **Position-pick recipe:** Shuffle the position pass into RGB+A (produces a strange, colorful image encoding 3D coordinates); use the free Nukepedia position-picker tool (Adrienne Herr, 2016) — hold Ctrl (Windows) / Cmd (Mac) and click-sample a point on the viewer while viewing the position channel to generate an alpha "bubble" centered on that exact 3D location; feed that alpha into a `Grade`/color-correct to isolate and adjust just that surface region (e.g. the crest of a hill), which then sticks accurately to the moving footage across the whole shot with no roto or additional tracking.
8. **Relight recipe:** Add a `Shuffle` node; set input A to the `normals` channel set and copy it into the main image's `normals` channels in stream B (so the normals data lives in the same stream as the color footage — required for the Real Light node to see it).
9. Add a `RealLight` node; assign it a Material (e.g. Basic Material, or a Fog-type/metallic-look material), the solved camera, the background/color input, and a Light (Direct light used here, standing in for a sun); in the RealLight node, set the Normal Vectors parameter to the `normals` channel copied in the previous step.
10. The RealLight node outputs a lighting alpha; feed it into a `Grade` and push warm/orange color to fake directional sunset/golden-hour light hitting the hilltops; rotate the Direct light node in 3D to change which side of the terrain catches the light.
11. Combine fog + position-based touch-ups + relight + a final overall color grade + a widescreen crop to assemble a rough atmospheric "golden hour" look over the original flat drone footage (acknowledged as a non-final demo — real production work would add longer shadows, more highlights/reflections, and further pinging-highlight detail per the channel's companion grading videos).

### Nodes / Tools / Settings
- `DepthGenerator` — synthesizes depth/position/normal utility passes from a solved 3D camera + 2D footage via parallax analysis; requires "Analyze Sequence" to run; default depth output is `1/Z`; position/normals must be added as new RGBA channel sets manually.
- `Shuffle` — used to view/extract passes into RGB+A for grading, and to copy the `normals` channel set from stream A into stream B ahead of the Real Light node.
- `Grade` — used repeatedly: inverted+black-point-pushed depth for fog; masked lift for fog application; orange push on the RealLight alpha for golden-hour color.
- Third-party Nukepedia position-picker tool (Adrienne Herr, 2016) — Ctrl/Cmd-click sampling on a position-pass image to generate a 3D-location-based alpha "bubble" that sticks to the surface across the shot.
- `RealLight` — NukeX 3D relighting node; inputs: Material (Basic Material / Fog / metallic presets), Camera, background Color, and one or more Lights; requires a `Normal Vectors` channel set (the copied `normals` stream) to compute shading.
- Direct light (3D light type within the Real Light setup) — stands in for a sun; rotatable in 3D to change lighting direction/side.
- Write node settings: **32-bit float** data type, **compression off** — mandatory when rendering out depth/position/normal utility passes to preserve real-valued 3D data.

### Difficulty
Advanced — combines 3D camera tracking, multi-channel AOV/utility-pass workflows, and the NukeX-only Real Light relighting system; explicitly flagged [Advanced] by the channel and assumes familiarity with channels/3D system concepts from the presenter's own prerequisite course.

### Foundry App & Version
Nuke / NukeX — the Real Light node and full 3D camera-tracking/DepthGenerator workflow are NukeX-tier features. Version not stated on screen or in narration. 2020 upload, predates this skill's release-notes backfill (starts at Nuke 13.0/March 2021), so treat as Nuke ~12.x era rather than a specific point release.

### Tags
relighting, 3d-system, camera-tracking, channels, aovs, digital-matte-painting, advanced

---

## Related Tutorials
- Grading Highlights and Pools of Light | Nuke Compositing (`grading-highlights-and-pools-of-light-nuke-compositing.md`) — shares `relighting`, `digital-matte-painting`; this video's presenter explicitly references that companion class's "pinging highlights" concept as the next step of realism after this relighting pass.
- Physics of Light for VFX Artists [Updated] (`physics-of-light-for-vfx-artists-updated.md`) — shares `relighting`; theory foundation referenced directly in this video's "color diffuse" discussion.
- Create 3D Noise | Nuke Compositing (`create-3d-noise-nuke-compositing.md`) — shares `channels`, `aovs`; both drive comp-side effects from CG/synthetic utility passes (position/normals) rather than roto or re-rendering.
- Ray Render in Nuke Tutorial | Compositing 3d Reflections (`ray-render-in-nuke-tutorial-compositing-3d-reflections.md`) — shares `3d-system`, `camera-tracking`, `digital-matte-painting`, `advanced`; both derive convincing CG-like results from a solved 3D camera track over live-action footage without full production geometry.
- Tracking Concepts in Nuke for Beginners (`tracking-concepts-in-nuke-for-beginners.md`) — shares `3d-system`, `camera-tracking`; that video explains the triangulation/parallax fundamentals behind the solved 3D camera track this tutorial assumes as a prerequisite.
