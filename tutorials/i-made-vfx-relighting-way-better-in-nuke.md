---
title: I Made VFX Relighting WAY Better in Nuke
source: YouTube
url: https://www.youtube.com/watch?v=H7dBKDLXwPo
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/i-made-vfx-relighting-way-better-in-nuke/
frame_count: 0
frame_status: pending-selection
---

# I Made VFX Relighting WAY Better in Nuke

**Source:** [YouTube](https://www.youtube.com/watch?v=H7dBKDLXwPo)
**Author:** Compositing Academy
**Duration:** 8m7s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py i-made-vfx-relighting-way-better-in-nuke <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello guys, welcome to this video. We're going to be talking about relighting in comp with a brand new tool set that we're releasing that speeds up your workflow and expands your capabilities.
[0:07] So if you've seen the video a few months ago I posted about relighting, you saw how we can use normals to enhance or add light onto our actors.
[0:15] But something I realized experimenting on some various projects and in our most recent project, I use relighting pretty extensively and I realized there are a few gaps still in the workflow that needed to be patched.
[0:24] So this tool set makes it a lot easier to do complex relighting and fills in the gaps to cover this essential workflow.
[0:29] Alright, so let's check out two of the shots from the last project that we released on this channel, which was a pretty big sequence that required relighting in very specific scenarios.
[0:38] So here, if we look at this first shot, we have this vehicle driving past some blue light sources, basically lava terrains here.
[0:46] So we want to cast a little bit of light out of the character and you know, this is something that the lights are kind of passing the character.
[0:53] So there's some parallax and various different things that are going on here.
[0:57] And then we have a second shot that's much more complicated, which is there's actually some explosions landing all around the character and basically flying past.
[1:05] So that means we need to have the ability to not only animate these lights moving through space, but also cast shadows, basically self shadowing onto the character.
[1:14] So for example, if we look at a frame here, we can see like the arm itself is actually occluding the face because it would the explosions below the arm.
[1:23] So we need to have actual shadows and normals don't actually do this.
[1:27] So our tool basically enhances your ability to cast shadows and to quickly and accurately place the light sources.
[1:34] So this is the CA relight tool.
[1:36] I'm not going to go through every single knob in this tool in this video.
[1:39] I just want to give a quick overview so you have an understanding of what it does and what's the purpose.
[1:43] So basically what this tool does is first of all, it gives us a custom interface to make placing lights easier.
[1:51] Messing with an XYZ knob to place a light is the most unintuitive way to place 3D objects.
[1:57] I don't think it's the best way.
[1:59] And so what this tool said does is it creates a new type of interface that essentially you can think of it like a top down view.
[2:05] So if we imagine our actor is sitting in the center of our depth, so maybe you have a generated depth map from zero to one, our actor sitting at about halfway.
[2:14] So point five.
[2:15] So this represents our actor as if we were looking down.
[2:18] And so this also represents our light.
[2:20] So if I grab this, basically, dot here, I can rotate this light around and visually and intuitively move our lights in a way that makes it much more easier to animate.
[2:28] So when I'm doing those explosions and they're flying past, I can just set a key frame here.
[2:33] I could drag this up and it's going to fly past.
[2:36] And I'll have to think about rotation values and that type of thing.
[2:39] And so if I wanted to create a new light, I could double click and I could create a new light source.
[2:43] So our custom tabs here also separated out so it's all clean.
[2:46] You don't have a million knobs all stacked vertically, but we can just go through and control each light.
[2:51] I can remove light, for example.
[2:54] And so we have other things that we can control, for example, like the softness of the light or how it falls off in the normals of themself.
[3:00] One of the other nice features here is if I hold shift, how do we move the lights up and down?
[3:05] We can basically just increase the height.
[3:07] So this will make it move vertically or or lower like this.
[3:11] So if I want to have a light source near the ground, for example, when the explosion is going off on the near the bottom of the character.
[3:18] And you see, we're getting actual occlusion in the light source here.
[3:21] So this is not what normals would normally do.
[3:23] I'm going to turn off occlusion just to demonstrate this.
[3:25] So the normals relighting would actually look like this typically.
[3:28] And this is why it always looks a little bit fake.
[3:31] Unless you're going to rotoscope every occlusion, you're not going to get a result that looks real.
[3:36] So you need to have occlusion.
[3:37] And so by combining the depth and the normals, we can actually generate this occlusion.
[3:41] And we get a much more realistic result, even though this is just in screen space.
[3:46] Like we don't have an actual 3D model here, but we're basically simulating a similar effect without having to have that additional complexity.
[3:53] So the multi light tool is the most useful, I think, in this tool.
[3:56] We also have the other ways to relight if you want.
[3:58] So if you want to use an HDRI, for example, we can switch to HDR mode.
[4:01] Here we have our different modes in the tab.
[4:03] So I can say, HDR, reflect, HRI diffuse.
[4:05] So we'll do it.
[4:06] HRI reflect just to show.
[4:08] And this is basically a mirror like reflection, which we could blur the HRI if you wanted to adjust that effect.
[4:14] Or we could do an HRI diffuse, which gives you a little bit more of a diffuse result right out of the box.
[4:18] So to give you an idea of where HRI could be useful on an animated scene like this.
[4:22] Basically, our character is driving past a bunch of small blue light sources that might be flickering, that might be behaving in different ways.
[4:28] And so this could be a scenario where you don't want to use the multi light tool.
[4:31] You just want more of an automated result.
[4:33] So what I did here is render out a 360 cube map from Blender.
[4:37] And this gives me all of my light sources with the correct emission values.
[4:40] So we're going to get different variations in light.
[4:43] And we can apply this through the HRI and basically cast that light back onto the actor.
[4:47] This is essentially the same thing as what we were doing if we were doing like a CG integration in real life, except we're doing the opposite effect.
[4:53] So here, if we compare, we can see it on a sphere and we can also see it on the character.
[4:56] This is if the character is a pure mirror like effect.
[4:59] So if you want it, if you had metallic bits on the person, you wanted to key mix those together.
[5:03] Again, watch my other video on it.
[5:05] I explained how some parts are more metallic, some are more diffuse.
[5:08] You know, that's going to be something you need to consider.
[5:10] But this is just to compare the position of that reflection to make sure everything's working well.
[5:14] And we have it the same effect applied to a sphere, which is just putting our real light tool directly into the normals and the depth of a sphere.
[5:21] We also can compare that against a ray render to actually make sure that, you know, the result is correct.
[5:25] And we can see that it is.
[5:27] We have a similar result here.
[5:28] And so we know that the normals are actually casting right onto this person.
[5:32] One of the things that's always tricky with HDRI lighting is knowing where the HDRI is reflecting onto the actor if you're doing relighting.
[5:40] So one of the things I added was this ability to go into this 3D dome mode.
[5:44] And what it does is basically projects it outwards onto a dome.
[5:48] And we can see that, you know, basically we can align our HDRI in the right position.
[5:53] So we know where's this light supposed to be coming from.
[5:55] And so we can go back to reflect mode or we could go to diffuse mode, HDRI diffuse.
[6:00] And so if you look at an HDRI diffuse, it would look something like this as we drive past our light sources.
[6:04] So we can see here as we pass this blue pool, which is in front of us, we get a little bit of light.
[6:09] Now, some of the splashes are in comp.
[6:10] So they were not in the rendered 360.
[6:13] So if you wanted to have every single element, you do you want to run your out of 360 as well for that?
[6:18] You have a very complex scene, but this is good enough for what I needed.
[6:21] So we're just getting some a little bit of blue light casting onto the person with the vehicle.
[6:25] So we get some flickering with some variation as we're flying over those smaller light sources.
[6:30] Maybe some we can definitely pull it down a little bit, but this is like a render pass, right?
[6:34] It's something you're supposed to mix in, maybe not just take it right out of the box,
[6:38] but we could use the reflection one to add some metallic bits, use the diffuse one to close them more flat.
[6:43] And we can layer this back together.
[6:45] And lastly, we could even use the multi light one as either just a mask if you wanted to,
[6:49] just to add the inclusion to the HGRI mode if you need that.
[6:53] Now, just to give a little bit more details on some of the extra little knobs in there,
[6:56] there are some ways to just affect the look of certain things.
[6:59] So if we have like reflect mode and we want to just affect the fall off or just kind of play with the normals to cheat the look.
[7:05] A lot of times we're just trying to cheat it to get the impression of what we're going for.
[7:08] So all of this is going to be a hack if we're generating normals anyway.
[7:12] So really, we just want the visual result that we're looking for.
[7:14] So one other cool feature is if we go to the dome mode again,
[7:17] there's actually one feature in here that allows us to see the actual floor.
[7:21] So a lot of times when you're doing a CG object, a real footage,
[7:26] we actually re projected on a flat dome, we don't project it onto a completely spherical dome.
[7:30] That's because the light source, the ground is closer to the actor.
[7:33] It's not this huge sphere that's just surrounding you.
[7:36] And so the same principle applies here.
[7:38] So we can turn on flat floor and it will basically re project the HRI and to something that's closer to the actor.
[7:44] So those reflections will be slightly more accurate than just projecting from something very far away.
[7:48] And that will make the parallax actually more accurate as well, especially on a scene like this.
[7:52] So having the combination of the different methods is going to be the best.
[7:55] You want to check out the link below for the CA relight tool or check out the full project we did a few weeks ago.
[7:59] If you want to learn more about the techniques that went into this entire project and there's a lot more,
[8:03] that'll be coming in the next few weeks in the full stack filmmaker course.



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
