---
title: How to use NUKE to Composite Blender Renders
source: YouTube
url: https://www.youtube.com/watch?v=peygC-ZxaP8
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-to-use-nuke-to-composite-blender-renders/
frame_count: 0
frame_status: pending-selection
---

# How to use NUKE to Composite Blender Renders

**Source:** [YouTube](https://www.youtube.com/watch?v=peygC-ZxaP8)
**Author:** Compositing Academy
**Duration:** 9m10s | 9 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py how-to-use-nuke-to-composite-blender-renders <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Today I'm releasing a free plugin that connects Blender and Nuke together and in just one click, combines these softwares seamlessly.
[0:06] If this is your first time checking out the channel, my name is Alex Hanaman, I'm a Senior Visual Effects Artist,
[0:10] I've been working in the VFX industry for the last 10 years on films like Star Wars, Avengers, Spider-Verse and more.
[0:16] On this channel, I'm sharing a lot of the techniques I learned along the way and also combining them with independent filmmaking workflows.
[0:22] Blender and Nuke together, I believe, is the best combination if you want to be a one-man VFX studio or a small team punching high above your weight.
[0:29] If you're a filmmaker looking to do green screen virtual production or if you want to do full CG shots with a high-end finish,
[0:36] then this plugin is designed to connect these two softwares and give you those possibilities.
[0:39] What this plugin does is in just one click, in Blender, you can click and generate your node graph in the compositor.
[0:45] This generates all of your AOVs denoised properly with naming conventions and goes directly into Nuke.
[0:51] In Nuke, the download also comes with the CG Compositing Template, which breaks out your AOVs properly,
[0:56] which means you can color grade all of the aspects in your CG.
[0:59] If you've never worked with AOVs before, I'm going to show a little bit of that later in this tutorial if you're a beginner.
[1:03] But even for intermediate users or people who just want to see what this is all about, you can see how this plugin works and we're going to dive into it.


### Blender Plugin Download [1:09]
**Transcript (timestamped):**
[1:09] Alright guys, so the first thing you're going to want to do is click the link in the description to download this plugin.
[1:13] So what this will give you is these two files.
[1:16] So one is a Python script that drops directly into Blender and another is a Nuke template that you can open.
[1:21] So there's a template you can save in your menu, as well as an example scene with some CG renders that you can play around with if you're unfamiliar with the AOV setup from Blender.
[1:29] So the free download button is here and then we can move on.


### Installing the Plugin [1:32]
**Transcript (timestamped):**
[1:32] So to install this plugin is super easy, just like any other plugin, edit, preferences, add-ons, click the little arrow and say install from disk and simply choose the Python script we downloaded and hit enable.
[1:43] So again, what we're trying to do is get all of our renders out with all of the layers properly denoised and utilities into a template into Nuke.
[1:50] So first thing you want to do to set up your renders, go to your output, set to OpenEXR multi-layer and set an output wherever you're rendering it and just call it utilities.


### Setting up EXRs in Blender [1:56]
**Transcript (timestamped):**
[1:58] That's going to be all your utility passes coming out of this panel.
[2:00] Now we want to go to our, basically, our passes here and enable everything that we need.
[2:05] So pretty much all of this stuff, we want the denoising data as well.
[2:08] We don't need the indexes and we just need all of these passes here.
[2:11] Also, you want to enable your crypto mats and that will also be stored in this EXR.
[2:15] So you can think of it like two renders that come out of Blender.
[2:17] In the right panel, we get utilities and crypto mats.
[2:20] We can target specific objects in different ways and in the compositing tab, we get AOVs.
[2:25] So we can target lighting and materials and break them apart.
[2:28] Now in the compositing tab, you want to hit use nodes and we can see all of our passes are enabled here.
[2:34] And now we just hit this little button.


### Denoising AOVs in Blender [2:35]
**Transcript (timestamped):**
[2:35] So this is what the plugin is doing.
[2:36] It's going to wire all of this up for you.
[2:38] So it's going to set up all the denoising properly, all of the channels properly with the correct naming, which is going to drop directly into the Nuke template.
[2:45] So the only thing you need to do here is go to your file output.
[2:48] So this will be the second EXR that gets rendered and this will be your AOVs.
[2:51] So whatever you want to call it.
[2:53] That's just a separate file that will be rendered.
[2:55] So I usually put them in the same directory, denoised and then utilities.
[2:59] So two EXRs.
[3:00] All right guys.
[3:01] So this is the template that you'll get for free if you download the script.


### Nuke Blender CG Template [3:02]
**Transcript (timestamped):**
[3:04] So essentially you can save this in your Nuke menu by just going to your little toolbar here and hitting create.
[3:09] You can type a name for it.
[3:11] So you always have this and it will pair with your Blender plugin.
[3:14] So this sets it up for you.
[3:16] So it'll work for any shot and it's actually set up properly.
[3:18] I've seen a few templates out there online that are missing a few key elements that are very important, which is mainly this right here.
[3:25] So a little bit more of an advanced concept.
[3:28] If you're a beginner, you don't probably understand premultification yet.
[3:30] I highly recommend checking out the Nuke beginner series if you're unfamiliar with AOVs or what even you're looking at right now.
[3:37] Essentially, but basically for the intermediate people, you need these on premults here to work with the Blender AOV template.
[3:46] So essentially what we have here is, for example, just as a quick rundown, we have the diffuse separated from the specular, separated from transmission, which is something like a window that you're seeing through and then separated through, let's say, the haze.
[4:00] If there's haze in your scene, you can control it just here.
[4:02] So we have all the elements separated.
[4:04] And if we want to, you know, let's say we want to change the color of just this barrel, we could go to the diffuse color, which is just the pure color without the lighting.
[4:12] We can see the lighting here, and we can see the indirect lighting here, but just the color itself, we can go to the barrel.
[4:18] And let's say we want to get target the reds, we can use a hue correct and just go to the reds and maybe just boost the saturation a little bit in that area and then go back to the lighting.
[4:28] And now we have this adjustment being made without affecting the lighting and all the other aspects of our image.
[4:33] So another example is like, maybe we just want to boost a little bit of the reflection on this barrel, maybe in the indirect bounce area.
[4:40] We can go to the glossy indirect and we can see just the reflection by itself.
[4:44] And then we could just throw on a little grade here.
[4:46] If we want to boost it, we can use the grade just boost up here, but we don't want to apply it everywhere.
[4:52] Just want to apply to the barrel.
[4:53] So what we do is we can grab our utilities.
[4:56] So here's our two renders.
[4:57] This is the one from the basically blended node panel.
[5:01] And this is the one from the main panel, like I explained earlier.
[5:04] So here we can just copy this node and we can extract the crypto mats from it.


### Blender Cryptomattes in Nuke [5:09]
**Transcript (timestamped):**
[5:09] So this is the crypto mat node and simply so like this barrel, grade it up here and now put it into the grade mask.
[5:16] And now we're just grading up the reflection of just this object.
[5:19] Now when it gets recombined with the direct reflections and the material, essentially we have a result that looks like this, which we can just boost up the reflection like that.
[5:29] The other key component here, just as another example for crypto mats, because crypto mats is a big one.
[5:35] We could just grab the utilities again, plug it in and we could do a crypto mat.
[5:41] And let's say we just want to shift the color of the center cube here.
[5:44] Key aspect here is we can there's different types of crypto mats.
[5:47] We can separate by material, by asset, but we'll just like by object and we'll just control click this one.
[5:53] And then we can just pull it over here and we can make that a cube yellow.
[5:58] So that's the quick rundown of why this is useful.
[6:01] Now, on a very simple scene like this, it's not exactly that useful, right?
[6:04] It's just three objects, but when you have hundreds of objects or you have at least an environment, or you want to use the depth pass to create fog or mist or volume raise or mask elements behind different objects.
[6:16] When you get into more interesting and complex compositing, you know, basically you want to make your shots look like a movie, then you have to do this process.
[6:24] It's not a process you can skip.
[6:26] This is where you get cinematic look, but this is the key component is having this template that works.
[6:31] So one aspect here for the intermediate users, basically blender denoises these passes separately.
[6:39] So some renders are doing it slightly differently where if you if you compare it to the beauty will be exactly exactly the same.
[6:45] If you do it this way, it won't be so you look very close.
[6:49] The denoising is done very slightly differently.
[6:54] So all you need to know really is you do need to use this template and you cannot subtract one of these passes from the main beauty.
[7:02] So this is more of an advanced concept just speaking to the advanced users here.
[7:05] Sometimes you can pull out one pass and recombine it, but in this workflow, rendering out of blender, it's not going to work because the denoising is being done individually to these these layers here.
[7:15] Now, another little bit more of an advanced concept for those who are interested.
[7:20] This is just a barrel with a little bit of motion blur on one frame, and this is where this part matters.
[7:26] And you've seen it left out of various videos.
[7:30] So you need to have this here.


### Premult Issues [7:31]
**Transcript (timestamped):**
[7:32] And basically why that is is if you take the beauty of that image, you put it over a gray background.
[7:37] This is what we should expect.
[7:38] We have soft edges and all that stuff.
[7:40] And if we don't do this, we have those on pre multiply off.
[7:44] And we recombine all of our AOVs like we would.
[7:50] And we merge it over.
[7:51] We're going to get some dark edges, right?
[7:53] So we need to make sure that these are here.
[7:55] And the reason for this, like why are we only on pre multiplying the color passes?
[8:00] It's basically these ones get pre multiplied, but the lighting passes don't.
[8:07] So you see the lighting passes have a hard edge.
[8:09] They don't have the alpha in there, but the diffuse color does.
[8:12] And so it's already it's multiplying those together.
[8:16] And so without getting too far into the math of it, really all you need to know is that.
[8:20] Yes, in fact, we will always want to work on pre multiplied when we're recombining together.
[8:24] And this is the past that has the pre multiply already in it.
[8:28] So those color passes need to be on pre multiplied first so we can work in a nice workflow, not damage our edges, change our colors, have full control, recombine it.
[8:40] And we got this nice exact matching result with the beauty render here.
[8:45] But this is the way that I found that works really well, especially when you have not a full CG scene and you're adding multiple elements over each other.
[8:53] Hopefully you found this useful.


### More Info [8:55]
**Transcript (timestamped):**
[8:55] The download link is in the description below.
[8:57] If you never use Nuke before, you can check out the Nuke beginner series and that will get you started on how you can do this kind of work to your renders and get to that level.
[9:05] And that's about it. Thanks.



---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Nodes / Tools / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Foundry App & Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]
