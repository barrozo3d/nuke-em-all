---
title: Why your VFX Tracks aren't "Sticking" (and how to Fix it)
source: YouTube
url: https://www.youtube.com/watch?v=ntx0Tm4ZYds
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/why-your-vfx-tracks-arent-sticking-and-how-to-fix-it/
frame_count: 0
frame_status: pending-selection
---

# Why your VFX Tracks aren't "Sticking" (and how to Fix it)

**Source:** [YouTube](https://www.youtube.com/watch?v=ntx0Tm4ZYds)
**Author:** Compositing Academy
**Duration:** 8m33s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py why-your-vfx-tracks-arent-sticking-and-how-to-fix-it <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Explaining Tracking Problems in Nuke [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, in this video we're going to talk about a very common problem with tracking in CG elements, whether it's 2D or planar tracking.
[0:07] Sometimes when you're tracking something, no matter what you do, the track seems to fail.
[0:12] And there are a number of ways to improve track quality, but knowing where the actual problem lies and understanding the fundamentals is actually more important than understanding the tools in Nuke, which are pretty simple tools in themselves.
[0:23] Now this is just the footage of the shot and there are some hidden characteristics of the lens that are affecting not only the track, but also the CG integration.
[0:31] And if you aren't aware of these concepts before you begin a shot, you'll actually never be able to make CG look seamlessly integrated.
[0:38] Now before we jump into the useful techniques in showing you where these hidden problems are in this footage that affect the track in CG integration,
[0:44] I also want to mention that this is actually a brand new project in the Nuke beginner series.
[0:48] So I continue to add new projects to this series here of practice projects and footage and assets that will make you a high level compositor.
[0:56] And we have some pretty cool new ones that we went to, pretty extensive lengths, like we hiked up a canyon in Iceland just to get this footage for set extensions and CG integration and full CG shots like this one as well.
[1:05] So if you're looking for a more advanced path of Nuke or you just want to have a more structured learning, that's available in the description below.
[1:12] So before we start any track, we should think about what kind of track should this be and how far do we need to actually go for this shot.


### Analyzing the Shot [1:14]
**Transcript (timestamped):**
[1:20] Like most of the time 3D tracks can be overkill if it's just a very simple camera move like this one.
[1:25] So this is not quite a nodal pan, meaning that the camera is actually moving through space.
[1:30] And how we know that is because this pole and this background are moving separately.
[1:34] That means that the camera is not on a tripod and just rotating.
[1:37] However, we can almost treat it like a nodal pan, at least for this whole area because it's all so distant and far away and pretty much behaving as if it's all in one parallax plane.
[1:47] So if we're thinking about this area, just putting something right there, we don't need to do a 3D track for that.
[1:53] We can just do 2D track or we could do a planar track.
[1:56] So here I've done two different approaches on putting the track in the shot.


### 2D Or Planar Track [1:57]
**Transcript (timestamped):**
[1:59] So we tracked in this castle and I've just roughly mask it behind the hill for now.
[2:03] We're not really working on the CG integration at this point.
[2:06] So the idea here is to check our track.
[2:08] So this is a 2D track.
[2:09] It's just a tracker node.
[2:11] I also did a planar tracker node.
[2:12] So this tutorial is not about those very basic nodes or those concepts.
[2:15] If you took it in the beginner series, you've already learned those concepts.
[2:19] So essentially what we have here is this 2D tracked in and just masked in there.
[2:24] And maybe at first glance, you might think that this is actually fine.
[2:28] Now, depending on the level of production, level of QC,
[2:31] if something slipped by in, let's say, lower level production or let's say,
[2:36] cheaper production, then let's say, feature film.
[2:38] But feature film, this would not pass QC.
[2:41] And the reason why is if we zoom in, sometimes you need to scrub quickly


### Checking the Lens Characteristics [2:45]
**Transcript (timestamped):**
[2:45] to actually QC your work and to check it.
[2:47] But you'll actually notice if you pay attention to the windows,
[2:50] where are the edges touching and are things sliding around.
[2:55] And we can actually see at the end, it's kind of sliding.
[2:57] Now, is this just a bad 2D tracked?
[3:00] Did I do this improperly?
[3:02] Basically, what I tracked here was just one point here.
[3:05] Well, that's not actually what is causing this tracking problem.
[3:09] So it's actually because of the lens distortion.
[3:11] If we don't have a lens distortion profile, that's going to cause some warping on the footage
[3:16] and then your things will look like they're sliding.
[3:18] But your track actually might be perfectly fine.
[3:20] We talked about lens distortion earlier in some of the beginner classes as well.
[3:23] But if we don't have a lens distortion profile,
[3:25] if we don't have this grid that we've shot, maybe they swapped the lens
[3:29] or they just didn't shoot the grid, what are we supposed to do in the situation
[3:33] where we get this sliding?
[3:35] So if I stabilize this, so I have the match move which applies the tracking data,
[3:39] if I invert that, and we can actually see this much clearer
[3:43] because sometimes it's hard to see it when you're just looking at it
[3:45] and maybe you just don't even notice it's quite doing that.
[3:48] I always check my tracks with the stabilize.


### Revealing The Problem [3:50]
**Transcript (timestamped):**
[3:50] So if we invert that motion and we kind of lock off that area of the frame,
[3:54] so this will no longer move there we tracked.
[3:57] But the footage still is going to move, so if I hit play,
[4:00] now this problem is going to become much more apparent.
[4:02] And to make it even more obvious, what you can do is scrub really fast on your timeline.
[4:07] And now we can really see where this is sliding.
[4:11] So you can see like it's totally just coming off the edges here.
[4:15] Like if we check it here, you can see the whole thing is sliding
[4:18] even though it is tracked in there.
[4:20] And this is really related to the lens distortion.
[4:22] It's not so much the track.
[4:24] Now the other thing that is interesting here that you might not have noticed
[4:28] if you just, you know, let's just watch it in motion again.
[4:31] We might think that, okay, it's just maybe slipping a little bit if you see it.
[4:35] But what else is happening because of this lens?
[4:38] The other thing that's happening is there's actually a vignette affecting the entire shot,
[4:42] which changes the black levels on the entire shot.
[4:45] So if you pay attention to the center of the sky here,
[4:48] look at the level of brightness, especially where the black levels are touching this castle.
[4:53] Look at the black levels and let's go back in time.
[4:56] You'll notice that it actually gets darker.
[4:58] And so this is because there's a vignette coming from the lens,
[5:01] which is darkening the sky and the actual black levels.
[5:03] So we need to animate the color grades that we apply to our CG in order to match this perfectly.
[5:09] Otherwise, you might match it on, you know, one frame, let's say our reference frame or start frame, frame 77.
[5:14] Everything might look perfect.
[5:16] You might do your perfect job, but at the beginning it won't match anymore.
[5:20] And you'd be like, well, I thought I matched the black levels.
[5:22] And so there's a few different techniques that are related to integration there.
[5:26] So how can we solve this lens problem?
[5:29] That's what this tutorial is about, is how do we solve this?
[5:32] Well, one thing you could do to reduce some of that stretching right off the bat,
[5:36] instead of tracking one point, is to do a planar track.
[5:39] So if you track an area, you know, it's going to actually force some of that perspective.
[5:45] And basically put some of that warp directly into your CG,
[5:49] because it's going to be tracking, you know, the shape and the pattern, rather than a single point of contrast.
[5:54] And so if we actually look at, this is a planar track stabilized, and we kind of do the scrub thing,


### Solving Lens Distortion [5:59]
**Transcript (timestamped):**
[6:00] we can see it's still sliding a little bit, but actually it's much, much better.
[6:04] So this is where planar track can actually be very useful for if you don't have lens distortion,
[6:08] or you just want to track something quickly.
[6:11] So that would solve us pretty close, but there's still that little bit of slide there,
[6:16] and how can we just fix that at the end?
[6:18] So that would just be a little bit of a manual adjustment.
[6:20] So what I did here was I just did a very rough roto with a blend.
[6:25] So I use an eye transform node, and this is on Nucopedia as well.
[6:28] You can just Google eye transform, Nucopedia.
[6:31] And it's just a soft transformation.
[6:34] So we can like subtly shift down the edge to make sure that everything sticks,
[6:38] and we can do that.
[6:39] I did it in a few different areas, and then just animate that.
[6:42] So if we look at the stabilized result, and we look at the beginning and the end,
[6:46] what I'm doing is I'm shifting up the side of this thing with the footage that is warping.
[6:52] So we're just applying a very subtle warp to the footage.
[6:55] And now if we check this out, and we just hit play, and we just look at this,
[7:00] it's actually sticking much better.
[7:02] And so a combination of those two techniques, we're doing a planar track to get rid of some warping,
[7:07] we're doing some hand warping to fix that, is not uncommon.
[7:11] And here's the other key idea.
[7:13] Sometimes these lens distortion profiles, I've gotten them before where they're actually not 100% perfect.
[7:19] For whatever reason, maybe it's coming from a match with company, maybe they didn't have a grid.
[7:23] You can't always 100% trust this lens distortion profile in some circumstances.
[7:28] And that little warp, you might have to adjust it as well.
[7:32] When you get into stereo composing, it can get even more complicated than this with various things there.
[7:38] But that's not for the tutorial.
[7:40] So that's pretty much it for how we can do this.
[7:42] Now for the vignette, essentially, it's just a manual adjustment as well.


### Correcting for The Vignette [7:44]
**Transcript (timestamped):**
[7:47] So what I did for the vignette was pretty much just a very soft roto on the edge of the frame.
[7:52] And then as we kind of slide away, it's taking the grid away.
[7:57] So you almost don't want to track this color grade at all.
[7:59] And you can slightly just darken your footage as that vignette is coming in.
[8:03] So it's literally just slightly darkening it down.
[8:07] And then we're compensating for that lens to make sure that everything actually looks like it was photographed in the same circumstance here.
[8:14] So that's pretty much it for this tutorial.
[8:16] Make sure to hit thumbs up if you guys want to see more tutorials like this.
[8:19] And if you want to grab the project files for this, like I said, it's in the course and there's a bunch of other projects to make it the absolute best new training out there.


### Project Files [8:20]
**Transcript (timestamped):**
[8:26] And I'm continuing to add even more projects this year.
[8:29] So it's going to be a pretty extensive update.



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
