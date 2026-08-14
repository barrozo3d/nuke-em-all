---
title: VFX Techniques: Impressions V.S Reality | Nuke Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=SKwymheLksc
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/vfx-techniques-impressions-vs-reality-nuke-tutorial/
frame_count: 0
frame_status: pending-selection
---

# VFX Techniques: Impressions V.S Reality | Nuke Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=SKwymheLksc)
**Author:** Compositing Academy
**Duration:** 7m42s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py vfx-techniques-impressions-vs-reality-nuke-tutorial <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] So another important concept that we want to talk about as a composer looking at a shot
[0:15] is impressions versus reality, right?
[0:19] So the further something away from the camera is, we can sort of compress whatever that thing
[0:27] is into a simplified form.
[0:30] And this is kind of how painters think about things as well, when you're painting a forest.
[0:35] They're not painting every single individual leaf with every single individual vein on
[0:40] each leaf, for example.
[0:42] They're just using one dot of color with maybe a specular highlight that's slightly desaturated.
[0:48] And that's kind of the same concept.
[0:51] It's like you're taking something complex, you're simplifying it for the distance that
[0:55] we're looking at it.
[0:56] So that's kind of the impression on the viewer versus the reality of what it actually is.
[1:02] And so this is happening a lot even in this shot.
[1:04] So for example, if we just think about this for a moment, this is one way to look at it.
[1:14] So we have the city here.
[1:16] So this is a perfect example.
[1:17] We could make an entire city from a noise pattern.
[1:21] We could just take a noise pattern, we could make some areas brighter, we could make some
[1:25] areas darker, and then just break up the colors.
[1:27] And we get the impression that there's a city down here.
[1:29] But actually it's just a noise pattern.
[1:32] In this example, we didn't use a noise pattern.
[1:33] I actually use a picture that I've taken over Los Angeles.
[1:37] And I'll give you guys that picture to do the matte painting with.
[1:40] And there's a whole bunch of pictures we're going to use here.
[1:43] But we're still getting that sort of feeling.
[1:46] And I just wanted to show you because you could do it with a noise pattern and probably
[1:49] get a very similar result.
[1:50] You might have to spend a little bit more time getting the little clusters.
[1:55] So you see there's kind of a cluster here and there's a little bit more density in certain
[1:59] areas.
[2:00] So if you study cities and the layout of a city, you're going to see these kind of clusters
[2:05] and then you're going to see these roads that are maybe a little bit more dispersed.
[2:09] But everything is going to be connected.
[2:10] So there's going to be roads that need to connect to transport materials or whatever
[2:15] it is.
[2:16] So when you're designing something, you want to design it.
[2:20] You don't just want to put a random noise pattern if you're doing the look dev or something.
[2:24] You want to think about the purpose of the thing you're designing.
[2:29] What is the story behind it?
[2:30] What is the reason that things exist?
[2:33] And it's the same for all of this here.
[2:35] All of this stuff has a purpose.
[2:36] I'm thinking about the story about what this place might be.
[2:40] Maybe this is underground mining facility.
[2:43] That's how I was thinking about it.
[2:44] So I was like, well, maybe they're transporting some kind of oil or some kind of materials
[2:48] down into this maybe underground facility.
[2:51] So in my mind, I was coming up with a story and then designing around that story after
[2:56] I had kind of determined what I wanted to do.
[3:00] But continuing with the impression versus reality, we can see the same thing up here.
[3:04] So we have these meteors, all these little floating rocks, but we also see ones that
[3:10] are much, much smaller.
[3:12] So we see ones that are kind of really tiny dots.
[3:17] And we're just using some noise patterns in there.
[3:20] Very dispersed, but it still gives us the impression that those are actual rocks.
[3:26] And so we have some CG rocks to start with.
[3:28] So some of these are actual CG, but we want to still give the impression that this asteroid
[3:33] field continues much further.
[3:35] And again, so we're just simplifying.
[3:37] We're just saying, well, maybe some of the ones that are really, really far away will
[3:40] catch highlights.
[3:41] So you'll see that some are brighter and then some are darker.
[3:44] You'll see that some have a little bit less highlight.
[3:47] So based on the rotation of that rock or how it's catching your reflection, we need to
[3:52] break up the highlights.
[3:54] We don't want them all to be one.
[3:57] You wouldn't want to simply just put white dots everywhere because it's not going to
[4:01] give you the impression that some are more reflective, some are more of a flat surface.
[4:07] You know, a flat surface is going to reflect more the highlight that's casting onto it
[4:13] versus like a more broken up rock.
[4:16] So to give that impression, we're breaking up the highlights.
[4:19] We're having some brighter and some darker.
[4:22] And same with all this stuff, right?
[4:23] So we have like all this cloud stuff, which is giving us the impression that it's pushing
[4:28] through dirt.
[4:29] And we're also leaving like a hole in the cloud.
[4:33] So this ship is so big that it's actually reducing, it's kind of making it darker behind.
[4:38] So it's actually pushing all the light dust kind of in front of it and leaving that darker
[4:43] area.
[4:46] And so those are all little things we want to think about.
[4:48] Same with all this kind of stuff.
[4:50] We have all this impression of these giant boulders and all this kind of stuff up here,
[4:53] but these are through the map painting and stuff like that.
[4:55] So it doesn't really go with this concept completely, but just things to look at and
[5:00] think about.
[5:01] So always think about how can I compress things down based on the distance?
[5:05] And this doesn't only apply to patterns like noise patterns, it also applies to like motion.
[5:11] So you could kind of get the feeling that this dust cloud is moving.
[5:14] We could even take a picture of a dust cloud.
[5:18] And one trick you can do to give the impression of motion or the impression of moving clouds
[5:24] is to key the highlights.
[5:26] So you can key like the brightest bits.
[5:28] You see like there's a brighter spot here.
[5:30] You could key that spot and then make that spot like animate a little bit faster than
[5:36] the rest of the cloud around it.
[5:38] And what that will do is actually give you the impression of parallax.
[5:42] So even though it's not true parallax, the length of the shot is only from one to 230.
[5:49] So we only have maybe like a couple seconds here.
[5:52] The shot's not like 10 minutes long.
[5:54] So by the time that that effect would break, it wouldn't work anymore.
[5:58] It still gives us the impression.
[5:59] So that's how we can like fake a parallax, fake 3D without truly doing the whole 3D process.
[6:07] So the more ways we can sort of give impressions, the better.
[6:11] This is the same also for this missile.
[6:13] So this is an impression thing.
[6:14] I didn't actually simulate any effect for this missile.
[6:20] And why would I?
[6:21] Because look at the sizes on the screen.
[6:22] We're not going to simulate a super highly detailed fire coming off of this.
[6:29] This is just a couple of grades, some basic noise and some clouds that it's going through.
[6:37] So we'll talk about that once we get into how it's made and everything like that.
[6:40] But you also see there's a slight trail of smoke.
[6:43] And again, that's just some noise patterns and some rotos.
[6:46] And we're using it on some 3D geometry as well.
[6:49] But we'll talk about all of that.
[6:51] But again, even the windows up here, so the ship didn't actually have windows.
[6:57] And do we need to model an interior for the ship?
[7:01] Absolutely not.
[7:02] We don't need to waste time doing that.
[7:03] We can just take a picture of a city and just put some simple windows in there and give
[7:09] the impression that this thing has all of this detail there.
[7:15] So those are all the kind of things you want to think about.
[7:18] And same for this, we're giving the kind of impression of lightning bolts, but we're not
[7:24] simulating it.
[7:25] We're actually using a pattern.
[7:26] So I'm going to show you guys how we did that.
[7:28] So it's just about simplifying, getting the feeling of things.
[7:32] And yeah, that's about it.
[7:36] So we'll talk about some different concepts next.



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
