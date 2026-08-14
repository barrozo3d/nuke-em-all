---
title: Grading Highlights and Pools of Light | Nuke Compositing
source: YouTube
url: https://www.youtube.com/watch?v=F6Ru0K0PwZM
author: Compositing Academy
ingested: 2026-08-12
app: "Nuke"
version: "not specified (2020 upload, predates this skill's release-notes backfill which starts at 13.0/March 2021 — likely Nuke ~12.x era)"
tags: [compositing, grading, relighting, digital-matte-painting, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/grading-highlights-and-pools-of-light-nuke-compositing/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Grading Highlights and Pools of Light | Nuke Compositing

**Source:** [YouTube](https://www.youtube.com/watch?v=F6Ru0K0PwZM)
**Author:** Compositing Academy
**Duration:** 17m35s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Welcome to this tutorial. This is a quick tutorial about some of my techniques and mental process about a technique I call highlight stacking or four layers of ping.
[0:12] This is a free preview of a class we were releasing in about a week or two here, Nuke 404, which is advanced grading and relighting.


### Advanced Grading [0:21]
**Transcript (timestamped):**
[0:23] We take a picture like this and we transform it into a picture like this. We use a variety of advanced compositing techniques to achieve this result.
[0:32] That would be about $12-$15 when it comes out. If you want to be notified, you can sign up in the description below and I'll send out an email pretty soon.
[0:40] You can enjoy this free preview of just a mental process of mine in terms of how to stack and think about lighting.
[0:51] The concept of, and I called it the four layers of ping, which is talking about specular highlights.


### Specular Highlights [0:56]
**Transcript (timestamped):**
[1:00] What I mean by this is, if we're going to start building up the interactive light bounces around our light here, we need to understand how to do it.
[1:11] It's not just as simple as taking a grade and a radio. This might be your intuition.
[1:20] You go here and there's a light bouncing off of these lights. We'll just go here and we'll just place a grade and we'll just grade it up.
[1:27] We'll start to put some green around it. Let's actually do this on our comp real quick just to show you that we're working out up here.
[1:35] If I put this here, we'll say, okay, let's actually do it before. We would put it underneath our light. We'd do our grade or whatever.
[1:46] We would look at that and let's just go here. Something like that. That's actually not the way to do this. That would be the base layer, but it's not that simple.
[2:00] I'll show you why. If I just stack a couple radials here, like I said, this is probably the intuition.
[2:05] Honestly, this is how a lot of Photoshop artists are doing it and Lightroom and stuff.
[2:10] I would say that's not advanced and it's not necessarily considering material properties.
[2:22] It's kind of like what my first lesson was about, about specular and glossiness and those things that we need to consider about reflections.
[2:32] This is not exactly a realistic result. Maybe this is the wrong color, but I can tweak it.
[2:38] I just want to show you guys the wrong way before I show you the way that I'm thinking about it.
[2:43] Not to say that my way is the only right way and there's probably other ways that people think about it,
[2:49] but I have a mental way of breaking it down that I think will be useful to you if you're learning this.
[2:54] There's some kind of bounce light, but it doesn't really feel like it's coming from that light.
[3:00] Let's compare that to my comp and we'll see exactly the difference.
[3:04] Here's that versus what I just showed. Let's just take a look back.
[3:11] There's a lot of reflections happening here. There's different material properties.
[3:18] You see the metal pipes and the metal pieces are pinging out differently than the surface materials.
[3:25] You see some reflections are catching at glancing angles.
[3:29] We also have versus just a broad color, we actually have light hitting surfaces like this on the side of this lantern that's off.
[3:38] Some of the wires are catching highlights differently because they're closer.
[3:42] We have light catching over in these clothing, whatever is hanging over here.
[3:48] Some details catching on the side of signs and all these tiny details.
[3:55] The way I'm mentally breaking it down is, and this is why I called the class the lecture, four pings.
[4:05] Essentially what this means is I'll just draw it out for you how I mentally think about it, which is a useful way to break it down.
[4:16] Let's do this, set this to all, and I'm going to draw it after the lights that we did here.
[4:25] If I'm thinking about this again, it's the pools of light idea.
[4:29] Our first area is the bounce light.
[4:33] Let's just say we started near the wall, so what's closest to everything nearby.
[4:39] We're going to see that this whole area is going to be lit up.
[4:43] This area is going to be lit up and then obviously the area furthest away down here is going to be lit up.
[4:51] This is going to be decayed a little bit, so this is not going to be as bright as the ones that are closer.
[4:56] You're thinking about that quadratic decay, so let me switch to a different color.
[5:02] I'm thinking about that quadratic decay, so here it's going to be really bright.
[5:08] Then let's see, go to a warm color and then here it's going to start to fall off.
[5:14] Of course the final one, which is like our broad fall off, is kind of like this super broad one like this.
[5:24] We want these lanterns to still light up this alleyway, so we created our lights to be bright enough.
[5:30] Obviously it's going to be dimmer further away.
[5:34] This is like the pools of light idea, but within each pool, this is where the concept of the four pings comes in.
[5:42] Let's say I'm doing this area down here, so let's just say we're going to focus on this pool of light.
[5:50] We'll say it's like the ground pool or something.
[5:53] We're going to have this broad diffuse that's happening.
[5:57] Like I talked about in the earlier physics of light lecture, we have the color diffuse.
[6:02] Then we also have the specular pings that are going to happen.
[6:07] That happens in almost rings, so towards the hotter areas, we're going to have different types of pings.


### Reflection [6:17]
**Transcript (timestamped):**
[6:17] If there's a reflection, the color diffuse is actually absorbing the material.
[6:21] It's like the broad radial, like I just showed you.
[6:24] It's kind of the broad just color that's absorbing the material.
[6:28] If we imagine that this is a reflection, and these are going to reflect down into the ground,
[6:34] but they're not going to reflect like a mirror.
[6:37] They're going to reflect sort of like distorted and everything like that.


### Pinging Highlights [6:44]
**Transcript (timestamped):**
[6:44] We're going to get a bunch of pinging highlights.
[6:47] Essentially what's going to happen is we're going to have really bright ones.
[6:50] Let me do the colors again.
[6:53] We're going to have the really bright reflections, like where the mirror is.
[6:59] We have the mirror.
[7:01] These are going to be the hottest pings of highlights.
[7:05] What's also happening is the broader specular highlights.
[7:09] Some of that's scattering across the surface as a glossy reflection.
[7:12] That's why I taught you guys about glossiness first.
[7:14] What's happening is almost like the mirror.
[7:18] It's almost mirror like these reflections.
[7:20] They're really bright.
[7:21] They're going to catch the really contrast.
[7:23] The secondary ones are where the light is scattering along the surface, depending on the material surface.
[7:29] You'll have less strong pings, but you still have some kind of pings falling off in a kind of a radial around this area.
[7:38] You might catch some pings in different areas around up here, stuff like that.
[7:43] But they're not going to be as intense as the ones in the very center, because that's almost a reflection.
[7:48] Then we're going to have maybe even some subtle pings that kind of fall off in areas outside,
[7:56] which is like the third pink, so I'm doing green to show that color.
[8:00] You see all of these different types of highlights that are appearing everywhere.
[8:04] Finally, we have something that is not within this pool of light that's still reflecting these lights.
[8:14] That is kind of these angle of incidence reflections, just materials and surfaces that are at the right angle to catch reflections, even when they're really far away.
[8:25] That's where all the main glints kind of speculate or highlights are happening.
[8:30] Occasionally you'll get one that's way out here, so this light is actually reflecting, giving a mirror reflection to something that's way out here.
[8:40] This surface here is reflecting back to us.
[8:47] I guess if your eye is here, this is your eyeball.
[8:52] This is an eye. This is coming back to us.
[8:56] That's how I'm thinking of it.
[8:59] I'm breaking it down and like, okay, most of it's isolated.
[9:02] We're going to get, and this is one pool of light.
[9:05] If we're thinking about this concept just for this one light, let me desaturate this.
[9:10] Let's say pool of light 2. The second pool is here.
[9:13] The third pool is here. These are the regions that are going to get pools of light.
[9:17] This same pinging concept, I'm going to do it throughout the whole area.
[9:22] I'm going to also think about the materials I'm looking at.
[9:25] I'm not just going to randomly put dots everywhere like I just explained.
[9:28] I'm going to look at this and say, okay, well, a metal pipe is probably less glossy than an asphalt surface.
[9:38] Meaning less glossy, meaning a sharper reflection.
[9:41] I'm going to go here. I'm going to ping specific sharp highlights on this pole.
[9:46] This is going to catch our main contrasting highlights.
[9:51] Then we're going to have these glossy pinging highlights.
[9:56] Let me just put this as a let's opaque on this wall here.
[10:00] The wall is not going to be completely just lighting up the area equally.
[10:03] The wall is made of plaster or something like that.
[10:06] It's going to be pinging in a little bit of a broader highlight, something like this.
[10:10] It's still broken up a little bit, but it's still pinging highlights in a little bit.
[10:15] It's still the same concept.
[10:18] I'm just saying before it's arbitrary number, but that's usually the amount of layers you need.
[10:24] You need at least four layers of the highlights to start to get something convincing.
[10:28] If you just do one layer, usually it's not going to work.
[10:31] Again, you maybe have some little pings in here that are a little bit less bright.
[10:38] It's still catching a little bit, but not as much.
[10:42] Same concept for all of these pools.
[10:45] That's how you break it down.
[10:47] Our fourth pinging, which is outside of the pool.
[10:51] We have three pings inside.
[10:54] Essentially, what you're doing is a quadratic fall-off of pinging highlights.
[10:58] Again, the lights, it's really hot in center and it falls off quickly.
[11:02] It's falling off, sort of like this.
[11:06] It's sort of falling off quadratically.
[11:10] Just like our exponential glow, but with pinging highlights.
[11:16] Here, maybe this vent here.
[11:19] I'm looking around at the materials.
[11:21] You've got to think about the surfaces.
[11:23] It's not so simple just to randomly put colors everywhere.
[11:25] You want to look at this thing's metal.
[11:28] It's going to have more mirror-like reflections at a further distance.
[11:32] Maybe this vent, we might catch some glancing angle highlights on this surface from our light.
[11:40] That's our fourth pinging.
[11:42] Again, I'm going to look around the scene and logically think about what surfaces might catch that.
[11:47] It's a painting.
[11:49] It's not 100% photo-accurate, but if it looks like it, that's all that matters.
[11:55] I might say, this surface here is a little bit further away.
[11:59] Maybe we'll paint a pinging highlight on that edge.
[12:03] Or maybe we'll paint something just like catching, just up here a little bit.
[12:07] This is the fourth pinging, the furthest away one that I'm doing here.
[12:12] Let's look around here.
[12:16] You could look at this thing here and say, on the edge of that little metal bar,
[12:20] we're going to catch some little highlights on the edge of that.
[12:23] That's how I'm thinking about it.
[12:25] That's how we're going to approach this.
[12:27] Maybe I'll split into another video because I know this one's already getting long.
[12:30] I guess this is the theory lesson of the way I break it down.
[12:36] I did so for my map painting here.
[12:40] Let's go down.
[12:42] I'll just show you again, like my comp.
[12:45] We have this thing.
[12:47] We have, again, the broad diffuse.
[12:50] You see, it's absorbing the color, but nothing's really looking reflective.
[12:54] We layered this below our light sources.
[12:59] We create the light sources first, and then we go back and we do the interactive.
[13:03] Now we have layer one, which is the hotter pings, but maybe not the hottest.
[13:09] There's pings that are close, but there's going to be even more.
[13:13] That would be the second layer of pinging.
[13:17] Then what we do is, we start to boost in the very center.
[13:21] Let me go back.
[13:23] Sorry, let me just do this quick.
[13:27] I started with the pool of light, which is the green dots out here,
[13:34] which is the diffuse.
[13:36] Then maybe some slight pings.
[13:38] Then we have the yellow.
[13:40] I started with the yellow pings, which is...
[13:46] Let's see.
[13:48] I just want to make sure I can show you guys without confusing you here.
[13:54] That's the green, diffused, broader pool of light.
[13:57] Then we start to bring in the yellow, which is these middle pinging highlights.
[14:06] Then I boosted those highlights, and I put some small pings on top of that.
[14:10] You see, I stacked some really bright reflections right in there on the center.
[14:19] That's the red highlight.
[14:22] I guess that's the way I explain it.
[14:24] Hopefully that makes sense to you guys.
[14:26] I don't think anyone ever explained it to me like this,
[14:29] but that's how I've mentally broken down for this project.
[14:34] Let's see.
[14:36] Then we have our lights that we built already.
[14:42] Of course, and then again, I went back.
[14:46] I said, okay, this is a pretty good result, but there's still some areas that feel only diffused.
[14:51] That's what I'm looking out for.
[14:53] I'm looking at this area and saying, where's the pings?
[14:58] If you don't see pings, it's probably not right.
[15:01] If you see what I did here, at the end there, I was looking at it,
[15:05] and I'm like, okay, it still feels flat in some areas.
[15:08] I went back with a paintbrush and a keer.
[15:11] I'm going to show you guys how to do this in the next lesson, actually.
[15:14] This is just the theory lesson.
[15:16] We see I went back and started pinging out a little bit more on some of these surfaces.
[15:20] They're not as small of pings.
[15:24] Like I said, they're glossy.
[15:26] You see how I blurred those yellow dots?
[15:29] They're a broader ping of highlight, but they're still this ping.
[15:34] Let's see.
[15:36] Continuing, and then I even added some more.
[15:40] I went back with a tiny paintbrush, add the tight pings really on the little surfaces.
[15:44] I'm looking at the angle of surfaces around.
[15:49] It might catch a highlight there, so I go there and I paint it.
[15:54] Let's continue on.
[15:58] Again, I'm doing this layering technique on the wall.
[16:02] That's how I approach it.
[16:05] Let's see.
[16:07] Continue through.
[16:09] That's pretty much it depth for that area.
[16:11] Later on in the comp, maybe at the very end, I added some more.
[16:14] You see our ground doesn't look very reflective.
[16:18] That's going to come in a later part of the comp where I really ping out highlights more.
[16:23] Let's go to the end here.
[16:27] Just let the end load here for a second.
[16:30] The reflections are going to need that same concept of pings and quadratic falloff.
[16:37] I do it in its own part of the comp because it's just easier.
[16:42] This all looks complicated if you're just looking at it, but it's not.
[16:47] It's just the way I'm mentally breaking it down.
[16:50] Like I said, you have the very hot ones.
[16:52] You have some glossy ones around it.
[16:54] Then you have the diffuse and a little bit of glossy ones that are fought for their way.
[16:59] We'll explain the reflection part next, but we're going to focus just on getting this effect for the lamp.
[17:05] Let's move on to the next lesson and do that.
[17:09] Alright guys, thanks for watching the video.
[17:12] I hope you appreciated the free preview of this class.
[17:15] I'll be releasing a few other free previews as well.
[17:18] If you're interested in this or other classes, all the information is in the description below.
[17:24] If not, if you just want free content on YouTube, that's fine too.
[17:28] I'd appreciate a like if you can as it helps the YouTube algorithm out.
[17:32] Thanks so much.



---

## Captured Frames

- [0:25] tutorials/frames/grading-highlights-and-pools-of-light-nuke-compositing/frame_000.jpg
- [4:20] tutorials/frames/grading-highlights-and-pools-of-light-nuke-compositing/frame_001.jpg
- [6:50] tutorials/frames/grading-highlights-and-pools-of-light-nuke-compositing/frame_002.jpg
- [9:45] tutorials/frames/grading-highlights-and-pools-of-light-nuke-compositing/frame_003.jpg
- [13:05] tutorials/frames/grading-highlights-and-pools-of-light-nuke-compositing/frame_004.jpg
- [16:30] tutorials/frames/grading-highlights-and-pools-of-light-nuke-compositing/frame_005.jpg

---

## Structured Notes

### Core Technique
Hand-painting believable specular "pings" (highlight hotspots) with a layered RotoPaint approach — the "four layers of pinging" mental model — to relight/grade a still photo into a moody, glossy night-alley matte painting.

### Summary
Theory/process preview from Compositing Academy's "Nuke 404: Advanced Grading and Relighting" course. The artist explains why a single broad radial grade under each light reads as flat and unconvincing, and instead breaks specular response into four concentric "pings" per pool of light: (1) a broad diffuse color-absorb layer, (2) mid-range glossy highlights that scatter along a surface depending on material roughness, (3) hot mirror-like pings at the true reflection angle, and (4) sparse far-field glint pings on surfaces angled just right to catch the light from a distance (angle-of-incidence reflections). He stresses reading material properties per-surface (metal pipe = sharp/mirror-like vs. plaster wall = broad/soft) rather than randomly scattering highlights, and demonstrates building the effect live over a Tokyo-alley photo comp, layering RotoPaint brush strokes from broad/dim to small/bright on top of the base grade and light-pool diffuse layers.

### Key Steps
1. Grade/build the base "pools of light" — broad soft falloff regions (quadratic decay) around each practical light source in the plate.
2. Within each pool, lay a broad diffuse "color absorb" layer first (the material's base color response, not yet reflective).
3. Add layer 2: mid glossy pings — scattered, softer-edged highlights following surface roughness, concentrated nearer the light.
4. Add layer 3: hot/mirror pings — small, bright, high-contrast dots only where the surface is glancing exactly at the light (metal edges, wet ground, glass).
5. Add layer 4: sparse far-field pings outside the main pool — isolated glints on surfaces angled to catch a reflection from far away (treat the "eye"/camera as the reflection target).
6. Use a RotoPaint node with multiple brush layers (visible as stacked `Brush1xx` shapes in the Roto/Paint list) to hand-paint each ping layer directly over the plate, blurring/softening the broader layers and keeping the hottest layer tight and small.
7. Merge the painted RotoPaint output back over the base grade/diffuse comp; iterate by reviewing "where's the ping missing" on flat-looking areas and going back in with a small paintbrush.
8. Repeat the same four-layer logic per light pool across the whole frame, and again later for reflective surfaces (e.g. wet ground) as a separate comp pass.

### Nodes / Tools / Settings
- `RotoPaint` — core tool for hand-painting each highlight layer; multiple named brush shapes (`Brush118`, `Brush119`, `Brush120`, `Brush121`...) stacked as separate strokes/layers inside one RotoPaint node, each with its own color/opacity/softness.
- Node graph shows a `Merge` chain compositing the RotoPaint output over upstream grade nodes, feeding a labeled `FINAL` output node.
- Roto shapes are also used as planning annotations (white circle outlines) directly over the plate to block out where each "pool of light" and ping ring will sit before painting.
- Background Renders / RotoPaint auto-render progress bar visible — RotoPaint is being cached/rendered as strokes are added.
- No numeric grade values are readable on screen; the technique is presented as an artistic/perceptual model rather than a parameter recipe.

### Difficulty
Intermediate — no complex node scripting, but requires strong grounding in light/material theory (this is a follow-up to the channel's "Physics of Light" lecture) and manual paint-layering discipline.

### Foundry App & Version
Nuke — version not stated on screen or in narration. 2020 upload, predates this skill's release-notes backfill (which starts at Nuke 13.0/March 2021), so treat as Nuke ~12.x era rather than a specific point release.

### Tags
compositing, grading, relighting, digital-matte-painting, intermediate

---

## Related Tutorials
- Skill Up with Nuke | How To Think Like A Pro Compositor (`skill-up-with-nuke-how-to-think-like-a-pro-compositor.md`) — shares `compositing`, `grading`.
- Build Entire FX with ONE Pass - Nuke Tutorial (`build-entire-fx-with-one-pass---nuke-tutorial.md`) — shares `compositing`, `grading`.
- Physics of Light for VFX Artists [Updated] (`physics-of-light-for-vfx-artists-updated.md`) — shares `relighting`, `grading`, `digital-matte-painting`; that video is the theory foundation for this one's "four layers of pinging" technique.
- 360 Spherical LatLong Textures | Nuke Tutorial (`360-spherical-latlong-textures-nuke-tutorial.md`) — shares `compositing`, `digital-matte-painting`, `intermediate`; that tutorial builds a spherical/lat-long sky matte painting, this one a hand-painted night relight matte painting — same discipline, different projection problem.
