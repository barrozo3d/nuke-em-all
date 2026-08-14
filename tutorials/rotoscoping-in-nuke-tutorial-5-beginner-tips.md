---
title: Rotoscoping in Nuke Tutorial | 5 Beginner Tips
source: YouTube
url: https://www.youtube.com/watch?v=rBPz0LL0yF0
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "Nuke 13.x (13.1/13.2 — exact 2022 point-release not stated; no version-specific features used)"
tags: [roto, tracking, camera-tracking, compositing, beginner]
extraction_status: complete
frames_dir: tutorials/frames/rotoscoping-in-nuke-tutorial-5-beginner-tips/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Rotoscoping in Nuke Tutorial | 5 Beginner Tips

**Source:** [YouTube](https://www.youtube.com/watch?v=rBPz0LL0yF0)
**Author:** Compositing Academy
**Duration:** 19m16s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.

> Reviewed: the "very short transcript in 'Intro'" warning is expected — that
> chapter is just the spoken title card ("Rotoscoping in Nuke, 5 tips for
> beginners"). The 5 real tips are fully transcribed below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Rotoscoping in Nuke, 5 tips for beginners


### Identify Motion Paths [0:14]
**Transcript (timestamped):**
[0:14] Tip number 1 is to identify motion paths.
[0:18] So what do I mean by this?
[0:19] We have a footage here of a person picking up some objects and moving them to a different
[0:26] spot.
[0:27] Our task was to rotoscope this hand and we wanted to isolate it and create a map.
[0:32] One of the mistakes that beginners might make is kind of arbitrarily placing keyframes on
[0:38] your timeline.
[0:39] So we have a timeline down here in the corner.
[0:41] And sometimes people think you just put a keyframe every 20 frames or every 30 frames
[0:46] or maybe shorter if it's a shorter shot, but we have a lot of frames here.
[0:49] But the problem with this is you end up kind of counter animating your shapes.
[0:56] If we were to look at the motion of this hand and what you want to do always before you
[0:59] start your footage is to watch the whole footage and try to identify some patterns in motion.
[1:05] There are usually some characteristics of motion that are mostly always the same unless
[1:09] you have really chaotic motion, but there are some principles of motion that we're going
[1:13] to talk about briefly that is pretty much the same for most objects.
[1:17] So if we just look at this and kind of play our footage, we can see that the hand is kind
[1:23] of going between actually three different locations.
[1:26] So if we were to just put a keyframe at the beginning and one at the very end, we're actually
[1:31] going to miss one of the spots here.
[1:33] So if I were to kind of draw it out on a just sort of a motion path here, we can see we
[1:39] have like a starting location, which is here.
[1:42] We have like a top location.
[1:44] And then we have sort of an end location like this.
[1:47] And so if we were to just draw that out, it's basically kind of a triangle.
[1:51] So rather than just arbitrarily doing one at the start and one at the end, what you
[1:56] want to do is I place a keyframe at the change of motion.
[2:02] So where an object slows down and starts to change direction, you want to look for those
[2:06] changes of direction, and that's where you start your keyframes.
[2:09] So basically, you would just put a keyframe here at the beginning of your shot, when the
[2:14] hand reaches the top, that's another keyframe, and then we would put one at the end.
[2:19] And that would avoid us making the mistakes of having to counter animate stuff.
[2:22] Because if we put a keyframe at the beginning and one at the end, you know, the roto shape
[2:27] will just slide between those two shapes like this.
[2:30] And then we're going to have to like kind of counter animate it to make sure it goes
[2:33] up and all those kind of things.
[2:35] So you really want to watch the motion, put your keyframes at the key points of motion
[2:39] changes and angle changes.
[2:42] And that will save you actually a lot of time than rather than just arbitrarily putting
[2:45] on random frames.
[2:49] Another thing to note is that usually objects, they kind of ease in and ease out.
[2:54] So that's something to keep in mind.
[2:55] So once you have your main motion points in place, so if you put a keyframe here, here
[3:00] and here, usually objects will kind of, and this is a very chaotic motion, they'll kind
[3:06] of ease in and ease out.
[3:08] So basically, it will kind of slow down here, and it will start to speed up here.
[3:12] So those would be another place you'd kind of put your secondary keyframes is just before
[3:17] the object kind of settles into its next position.
[3:22] So if you look at the motion objects, you know, we, you know, objects will gain speed,
[3:26] but they kind of have to gradually get that velocity and the same with decreasing.
[3:31] So that's something to keep in mind when you're, you're placing your keyframes, look for the
[3:35] directions of motion, make sure your ease in and ease out points are there as well.
[3:41] And that's going to save you a bit of time.
[3:44] Tip number two is separate by objects.


### Separate By Objects [3:45]
**Transcript (timestamped):**
[3:47] So what this means is basically you don't want to wrote objects together, especially
[3:52] if they're on different planes of parallax, or if they're deforming differently from each
[3:58] other.
[3:59] So you can save yourself a lot of time by simply separating the objects by different shapes.
[4:03] So if I go to the keyframe here, we can see I've taken the foreground object and an object
[4:09] that's behind it.
[4:10] And even, even the area that you don't see the rest of the object, you can overlap those
[4:15] two pieces.
[4:16] And that's just going to make it a little bit easier because you can simply just grab
[4:20] the entire shape as the shot is moving, rather than if you were to wrote it like this, where
[4:25] the points are together, maybe do a little bit of better job.
[4:29] But you know, if the points are together like this, these points might slide along the surface.
[4:35] So one of the things you want to do when you're rotoing is not only consider separate objects,
[4:41] but also, and this seems to sort of get looked over when you're beginner potentially is like,
[4:47] you think that the points don't matter kind of on where the edge it is.
[4:52] And that's actually something that's really important because if you let your points slide
[4:55] around on your edge, you think you're just trying to capture the silhouette of the shape.
[5:00] But it's not the case.
[5:01] You can get a little bit of wobbly edge if you put too many keyframes or your, you know,
[5:06] your points are sliding around on the surface like this, like if the shape is kind of going
[5:11] along and this point doesn't say in the same spot.
[5:14] So what I do is I typically look for a feature, you know, if we see that the black line is
[5:20] here on the hat, and I see that there's a point here, I would try to keep that point
[5:24] as close as I can as this, you know, sequence goes on.
[5:29] So that's something to keep in mind.
[5:30] So keep objects separated, keep the points relative to the place that they're originally
[5:35] placed.
[5:37] And you're going to get a more solid roto by doing that.
[5:40] So tip number three, we have stabilize your footage.
[5:44] And basically, this is pretty straightforward, but it's something to think about.


### Stabilize Your Footage (2D Tracking and Stabilizing in Nuke) [5:45]
**Transcript (timestamped):**
[5:49] If you have shaky footage, something like this, if we take a look, we can see this is
[5:55] sort of handheld, let me just kind of zoom in here, sort of handheld footage.
[6:00] And pretty shaky, and all over the place in terms of the motion.
[6:05] And so if we wanted to rotoscope a few of these fruits or kind of the things being carried
[6:12] in this basket here, again, we want to rotate the object separately, maybe we want to isolate
[6:16] one or two of these, we wouldn't want to do every single shape as one shape like the whole
[6:22] silhouette of this thing, maybe we want to color correct those to be different color.
[6:26] So what we could do is take a tracker node, and we'd want to stabilize it, do a roto and
[6:33] basically match move it after.
[6:34] So we would add a track, we take a track and we try to find a feature.
[6:39] This is going to be a little bit trickier because the lighting is changing quite a bit.
[6:42] If we if we look at the footage, the lighting is changing quite a lot in there.
[6:46] So you might have to do a little bit of manual 2D key framing here, but I'm not going to
[6:50] go and do a complete perfect track of this, but just to show the example.
[6:55] So I could set the reference frame where we are in the transform node, and we can try
[7:00] to find a good feature.
[7:01] Also one thing we can sort of turn on in the settings here is adjust for luminance changes.
[7:07] So that will help a little bit with the changing of lighting.
[7:11] I do expect that it will probably go a little bit crazy, but we'll see.
[7:14] So I'm going to use the C and X key on my keyboard, and I'll try to find a feature.
[7:20] Maybe I'll go on the front here because this one's a little bit more in the sunlight.
[7:24] So I hit C, it will track forward.
[7:26] So we can see it's popping off there.
[7:28] So maybe it's not the best feature.
[7:30] We'll see if we can find a different one.
[7:32] Maybe this one here on the corner, we could try that.
[7:35] We could expand our range a little bit and hit C.
[7:37] So that one's working a little bit better.
[7:38] So I can use that one and sticking relatively well.
[7:43] And we can just adjust it as it goes off.
[7:45] So C will track forward.
[7:46] If I hit X, it will track backwards in time.
[7:50] So I can go frame by frame and just make sure I get a couple good frames of this for the example.
[7:58] And if it's not completely perfect, you can always go in there and adjust it.
[8:01] Of course, this window really helps.
[8:03] So pay attention to your sort of stabilized window here and just see if it's kind of jittering.
[8:08] So if it updates properly, which sometimes it kind of lags, but this is a good way to
[8:14] see if it's jumping.
[8:16] So these two frames are good, but between here and here, if it updates, we can see it
[8:22] just hops to the right a little bit.
[8:25] So we can just slightly adjust it over and then just keep doing that until you get a really
[8:32] good result.
[8:33] So I like to make these window really big if you're trying to get a tight sort of track.
[8:37] So I can kind of put it here and step back and forth and just check and try to get that
[8:42] sort of sub pixel accuracy if you can.
[8:45] So that's how you can get really tight tracks as well.
[8:48] So I was going to actually make a different tutorial just on that because it's very useful
[8:53] to know if you watch that sort of sub pixel motion.
[8:56] This window really helps.
[8:58] So just keep stepping through and we can see it jumps off here again.
[9:04] So we just slightly shift it over.
[9:07] And I think that's good enough for the example.
[9:09] If it's a little bit off, we can always fix it later.
[9:11] But that's good enough.
[9:13] What I'll do is I'll go here, export a match move baked.
[9:18] I just like to do it baked just because it doesn't mess up if this thing gets kind of
[9:23] messed up here on accident.
[9:24] So we have our match move and I'm going to also do a stabilized baked.
[9:28] So we have the two of them.
[9:31] Let's get the stabilized baked.
[9:33] Once it's stabilized, once it's matched moves, so we'll put the stabilize on there.
[9:36] Put a roto in between and then we'll put the match move sort of at the end.
[9:42] And so remember our reference frame.
[9:45] So a reference frame was 151, I believe.
[9:50] That's our reference frame.
[9:51] So I'm going to start my roto there.
[9:52] I'm going to close all this stuff.
[9:54] And we'll just roto maybe one of these.
[9:56] We'll just kind of put a quick roto here so we can drag it out.
[10:02] And I'll just drag it behind for now.
[10:04] And I'll just kind of go like this.
[10:06] So something like this, I can select all the points, hit Z and smooth it out.
[10:11] I use that quite a lot.
[10:12] I like to work with the Beze Curve.
[10:14] Some people prefer to work with the B-splines.
[10:17] I just find it easier to have the control.
[10:20] So I like to just like them and hit Z to kind of smooth the corners.
[10:25] And we have something like this and we can view it.
[10:27] And this should stick a little bit closer.
[10:29] So you see, if we were to just roto on the normal footage, the difference is quite large
[10:33] if I just step between the two frames.
[10:35] But if I'm looking at the stabilized version, if I step between those two frames, you see
[10:39] it's already done most of the work for us.
[10:42] And if we were to roto without the stabilize a bunch of these different ones, we might be
[10:46] a little bit off in our track.
[10:48] One might go up a little bit, another one might go a little bit differently.
[10:51] And then you're going to get all kinds of jittering.
[10:53] So this is why stabilizing is really great.
[10:55] It's kind of getting the general motion for this large area.
[11:01] And so if your camera's moving, if it's panning, you can stabilize that.
[11:04] If it's an object that's moving independently like this one, you can stabilize that as well.
[11:09] So just things to think about.
[11:11] Think about the motion and think about how you can get rid of it, do your work and then
[11:15] reapply that motion back.
[11:17] So once we've got a roto, I'll just do another frame here.
[11:20] We can always just adjust the lines as we need to just make sure it's like really tight.
[11:26] And I'll just do like three frames here.
[11:30] And yes, I think it's actually there.
[11:35] We're just not seeing it because it's in the shadow.
[11:37] So I like to step between my frames here and see, doesn't feel like any point is kind of
[11:42] moving.
[11:44] And if it is, we want to make sure that's not doing that.
[11:46] So we can try to remove that sort of jump, make those jumps very, very small.
[11:53] So something like this, I think it's a little bit off still.
[11:57] It's hard to tell with the light here.
[11:59] That's changing so much.
[12:01] But really, it's easier to just kind of look at the point.
[12:07] So something like that is probably good enough for now.
[12:10] And that's good enough.
[12:12] And now we have an alpha.
[12:13] So we have our alpha here.
[12:15] If we want to use this back on our main footage, we reapply the motion with the transform match
[12:18] move.
[12:19] And now if I watch those three frames, it's going to move with the footage.
[12:22] So the movie, we're kind of reapplying that shakiness.
[12:25] And we have all of that there.
[12:28] And actually, what we can even do is now that we've done this here, this transform stabilize.
[12:34] We don't want to run the whole footage through stabilize because you're going to get a little
[12:37] bit of filtering.
[12:38] It's going to blur your picture a little bit.
[12:39] So you actually don't want to stabilize and do your work here.
[12:43] This is more just like a preview.
[12:44] So once we're done with it, we can kind of just unplug it.
[12:47] And we actually have the roto here with the match move.
[12:50] So you don't even, stabilize doesn't do anything at this point.
[12:52] We can just kind of disable it or keep it there.
[12:55] It doesn't really matter.
[12:58] And then what we can do is just use this as like a color grade.
[13:01] So we can plug it in like this mask.
[13:03] And then we could use that in whatever way we're trying to achieve here.
[13:06] So we can change the color of this thing.
[13:09] We could blur out our alpha a little bit and just the basic stuff.
[13:14] So we have that kind of sticking.
[13:16] So that's something to think about.
[13:18] Stabilize your shots when you can.
[13:19] If there's a lot of motion, it's going to help.
[13:20] And especially if there's a lot of objects, you can also do planar tracks.
[13:26] If you have an arm that's sort of swinging or a character that's moving a certain way,
[13:31] there's different, you can use other types of tracks.
[13:33] It's not just the 1D track that we've done here.


### Primary and Secondary Forms [13:42]
**Transcript (timestamped):**
[13:42] So the next thing we want to think about are primary and secondary forms.
[13:46] So when you're rotoscoping, typically there are complex shapes that we can break down
[13:53] into smaller and simpler forms.
[13:56] And so this is just a video.
[13:58] We have this kind of rooster walking here.
[14:03] And this is an example of this.
[14:05] So we did talk about separating things by objects.
[14:09] Easily identifiable objects.
[14:10] You can, like these leaves, it's very obvious which are separate.
[14:14] But with complex forms that have overlapping shapes, you can also do the same thing.
[14:19] You can actually break them down into simpler shapes.
[14:22] So an example of this might be taking the body of this thing.
[14:28] And we can sort of like, we could do a roto of just, you know, maybe the general outline
[14:34] of the body.
[14:36] And sometimes some of the smaller feathers might pop up independently.
[14:42] So rather than doing that on the overall silhouette, like adding to this main body
[14:46] shape like this, we wouldn't want to just keep adding little shapes every time something
[14:50] pops up.
[14:53] So what you can do is simply create smaller forms.
[14:57] And whenever those small shapes break the main silhouette, that is a good way to do
[15:03] it because you'll kind of save yourself a little bit of work there.
[15:09] So if I switch this to a different color, we can see that.
[15:12] So we see a primary form, the little bumps that create secondary forms.
[15:17] And this is a pretty useful technique.
[15:19] And you can as many of them as you need to, depends on the complexity of the form that
[15:25] you're doing.
[15:26] You know, for example, this might be another example, you know, if you're doing this sort
[15:30] of tail thing here, you could do maybe like the main one, and then you could break the
[15:34] smaller ones off because they're going to be, they're going to be moving pretty differently.
[15:38] So you could break it up into as many forms as you need, depending on the motion.
[15:42] And of course, you want to look at the motion beforehand as well.
[15:45] So this is the same idea as we have the main body.
[15:47] We can break that into two different shapes.
[15:49] We could have the wing.
[15:50] I'll just do a real quick sloppy one, just for the example.
[15:55] And we could just like make a different color to see a little bit better.
[15:59] So that would be another secondary form.
[16:01] So you see, it's not like one object is just one shape.
[16:05] It's like we're breaking it into many different things.
[16:07] And that's going to make it easier to animate because we can just, you know, we can rotate
[16:10] it and things like that.


### Use Rotational Points [16:13]
**Transcript (timestamped):**
[16:13] The last one we have here is using rotational points.
[16:17] Now that we know about primary and secondary forms, this is sort of a similar concept,
[16:21] but really just breaking those primary and secondary forms into their independent motion
[16:27] paths.
[16:28] So most forms, unless you have like really deformable object, isn't going to change size
[16:34] that much.
[16:35] So really, if you can just separate your objects into sort of based on their pivots, the general
[16:41] size of those independent shapes that you draw won't change that much.
[16:45] So really, you can kind of rotate them and just move them around rather than moving a
[16:49] bunch of points.
[16:51] So if we're looking at this sort of dog kind of jumping here, there's a lot of motion going
[16:58] on, but the general volume isn't deforming that much.
[17:03] The muscles and skin are stretching, but obviously the bone structure is going to stay the same.
[17:08] So what you want to do is separate this into many different shapes and just basically do
[17:14] it how it's kind of structured in the animal.
[17:16] So you would kind of do this area first.
[17:19] We could separate this into one shape.
[17:23] We could separate it here like this, and we could do another shape maybe for the ankle
[17:27] area like this.
[17:31] And this is just a very, very quick and sloppy one, but it'll get the idea across and then
[17:38] we could do another one on the bottom if we want.
[17:41] We could separate that into three shapes.
[17:43] Maybe you could do two shapes if you want to do it that way.
[17:47] So as this kind of goes, what's nice about this is if, for example, this bottom part
[17:52] rotates here, we can just rotate that form and just put it here and then kind of go like
[17:58] this.
[17:59] Same with this guy.
[18:00] We can just take this and move it over.
[18:03] And I'm trying to line up my points.
[18:04] Remember what I said earlier, trying to keep the points in the same area.
[18:07] So I'll try to find a point, like the very corner of his sort of, I guess this would
[18:12] be like the angle here.
[18:14] Finding that corner point and then trying to get that lined up and then trying to get
[18:17] the rest of the points following.
[18:21] Move them over and then hit Z to smooth.
[18:24] And that's good enough.
[18:26] So you can see how it's a little bit helpful to just kind of separating the different
[18:31] shapes here.
[18:32] We can have them overlap and it doesn't matter.
[18:35] And it helps us kind of keep our points more clean as well rather than having one shape
[18:40] with like tons and tons of points.
[18:42] So that's basically it.
[18:45] Yeah, just keep that in mind.
[18:46] If objects are rotating, it's a really good opportunity to use different shapes because
[18:52] we do have this pivot point.
[18:53] If you hold control, you can put the pivot point on the rotation and we can just rotate
[18:59] and it will pivot around that point.
[19:00] So a lot of real objects will rotate around a different center point and you can utilize
[19:06] that to save a little bit of time.
[19:09] And that's basically it.
[19:10] So that's five tips for beginners to increase your speed with Roto.



---

## Captured Frames

- [1:39] tutorials/frames/rotoscoping-in-nuke-tutorial-5-beginner-tips/frame_000.jpg
- [4:10] tutorials/frames/rotoscoping-in-nuke-tutorial-5-beginner-tips/frame_001.jpg
- [6:55] tutorials/frames/rotoscoping-in-nuke-tutorial-5-beginner-tips/frame_002.jpg
- [8:03] tutorials/frames/rotoscoping-in-nuke-tutorial-5-beginner-tips/frame_003.jpg
- [10:29] tutorials/frames/rotoscoping-in-nuke-tutorial-5-beginner-tips/frame_004.jpg
- [15:12] tutorials/frames/rotoscoping-in-nuke-tutorial-5-beginner-tips/frame_005.jpg
- [17:23] tutorials/frames/rotoscoping-in-nuke-tutorial-5-beginner-tips/frame_006.jpg

---

## Structured Notes

### Core Technique
Five workflow/methodology principles for faster, more stable RotoPaint/Roto work in Nuke: keyframe placement driven by actual motion-direction changes (not arbitrary intervals), separating roto shapes by object/parallax plane, stabilizing shaky footage before rotoing then re-applying the motion, decomposing complex silhouettes into primary + secondary shapes, and using each shape's rotation pivot instead of animating every point by hand.

### Summary
A pure-methodology beginner tutorial (no scripting, no exotic nodes) built around five real production examples. **Tip 1 (frame_000, hand reaching between 3 basket positions):** watch the whole shot first and place keyframes only at direction-change points (not evenly-spaced intervals) to avoid "counter-animating" the shape between two extremes; add secondary keyframes just before a shape settles into its next position, since real motion eases in/out rather than moving at constant velocity. **Tip 2 (frame_001, overlapping foreground/background market produce):** rotoscope different objects — especially ones on different parallax planes or that deform independently — as separate shapes rather than one combined silhouette, and keep each control point anchored to the same physical feature/edge-detail across frames rather than letting points slide freely along the silhouette (sliding points cause a wobbly-looking roto even with plenty of keyframes). **Tip 3 (frames_002/003/004, shaky handheld market-basket footage):** for camera/subject shake, `Tracker` a stable feature (toggle "adjust for luminance changes" if lighting shifts during the shot), export both a **baked Stabilize** transform and a **baked Match-Move** transform, sandwich a `Roto` between them (Stabilize → Roto → MatchMove) so the roto itself is drawn on the *stabilized* plate where the shape barely moves frame-to-frame — the stabilize window (viewer's tracked-patch preview) is the main tool for judging whether a track is holding, and should be enlarged for sub-pixel accuracy work; once rotoed, the Stabilize node can be disabled/removed since it was only a drawing aid, and the roto + MatchMove pair travels with the original shaky footage. **Tip 4 (frame_005, a walking rooster):** break complex, overlapping silhouettes into a primary "main body" shape plus smaller secondary shapes wherever a detail (a feather, a wing) pops in and out of the main silhouette, rather than repeatedly editing one mega-shape's point count. **Tip 5 (frame_006, a sled dog's legs on snow):** once shapes are separated into primary/secondary forms, further split them along an object's actual joints/pivots (a bone structure doesn't change volume much even when skin/muscle stretches) so each piece can be **rotated around a Ctrl-set pivot** rather than hand-animating every point — faster and more stable for jointed/rotating motion.

### Key Steps
1. Watch the full shot before placing any keyframes; sketch (mentally or literally) the object's motion path to find real direction-change points — that's where keyframes go, not at arbitrary fixed intervals.
2. Add secondary/ease keyframes just before a shape settles at each direction-change point, since motion naturally eases in and out.
3. Split any composited elements that sit on different parallax planes, or that deform independently of each other, into separate `Roto`/`RotoPaint` shapes instead of one combined shape.
4. Anchor each control point to a specific, trackable feature on the subject's edge and keep it there frame-to-frame — don't let points "slide" freely along the silhouette even if the outline still reads correctly, since sliding points are what causes edge wobble.
5. For shaky/handheld shots: add a `Tracker`, pick a stable high-contrast feature, enable "adjust for luminance changes" if lighting shifts, track forward/backward (C/X hotkeys) and nudge frame-by-frame using the tracker's stabilized-preview window until the patch stops jumping.
6. Export the track twice from the Tracker: **Stabilize (baked)** and **Match-Move (baked)** — "baked" so neither breaks if the Tracker node is later modified.
7. Build the chain Stabilize → `Roto` → Match-Move; draw the roto shape against the now-mostly-static stabilized plate, where frame-to-frame point movement is minimal, instead of against the raw shaky footage.
8. Once the roto is complete, the Stabilize node has served its purpose (drawing aid only) and can be disabled — do not leave the whole shot running through Stabilize for final output, since it re-filters/softens the image; only the Roto + Match-Move pair is needed downstream (e.g. as a `Grade`/color-correct mask).
9. For complex silhouettes, draw one primary shape for the main mass, then add small secondary shapes only where a detail breaks the primary silhouette (rather than repeatedly re-editing the primary shape's point count).
10. For rotating/jointed parts, split primary/secondary shapes further along the object's actual joints, and animate by rotating each shape around a Ctrl-placed pivot point rather than hand-keying every control point.

### Nodes / Tools / Settings
- **Core Nuke:** `Roto`/`RotoPaint` (Bezier curves preferred by the author over B-splines for point control; select-all + `Z` to smooth corners), `Tracker` (reference frame, "adjust for luminance changes" toggle, C = track forward / X = track backward, stabilized-preview window for judging track quality), `Transform` (Stabilize-baked and Match-Move-baked exports from the Tracker), pivot-point rotation via Ctrl-drag on a shape's transform handle
- **Workflow pattern:** Stabilize → Roto → Match-Move (roto against a stabilized plate, then re-apply the original motion) — a general-purpose pattern for rotoscoping any moving/shaky subject, not specific to any one shot type
- **No scripting, no gizmos, no gradle/AOV work** — this is pure interactive-tool methodology

### Difficulty
Beginner — explicitly framed as five foundational tips; no Python, no expressions, no advanced nodes, just disciplined use of Roto/Tracker.

### Foundry App & Version
Nuke. No version-specific features referenced (Tracker/Roto/Transform have been stable across many releases); per this skill's version-tracker, a 2022 upload falls in the Nuke 13.1 (Nov 2021) → 13.2 (Apr 2022) window, but nothing in this tutorial would behave differently on adjacent versions.

### Tags
roto, tracking, camera-tracking, compositing, beginner

---

## Related Tutorials
- Why your VFX Tracks aren't "Sticking" (and how to Fix it) (`why-your-vfx-tracks-arent-sticking-and-how-to-fix-it.md`) — shares `tracking`, `camera-tracking`, `compositing`, `roto`; that tutorial diagnoses why a track *slides* (lens distortion/vignette), this one covers how to place keyframes and stabilize footage *before* rotoing so a track/roto sticks well from the start — complementary reading.
- Tracking Concepts in Nuke for Beginners (`tracking-concepts-in-nuke-for-beginners.md`) — shares `tracking`, `camera-tracking`, `beginner`; that video explains the parallax/triangulation fundamentals behind the 2D tracking this tutorial's stabilize-before-roto technique depends on.
- [2/3] Nuke Tutorial Series (CRACKS, Keentools, Smartvectors) (`23-nuke-tutorial-series-cracks-keentools-smartvectors.md`) — shares `tracking`, `camera-tracking`; that video's per-region tracking-method selection (SmartVector/KeenTools/blended dual-track) and SmartVector edge-extension technique is an advanced counterpart to this tutorial's beginner keyframe/stabilize fundamentals.

Revisit once other tracking-focused tutorials (e.g. the 2024 Mocha+Nuke tracking video, once ingested) land in the index.
