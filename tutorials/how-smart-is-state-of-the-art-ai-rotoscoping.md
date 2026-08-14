---
title: How SMART is State of the Art A.I Rotoscoping?
source: YouTube
url: https://www.youtube.com/watch?v=AinQkgdR6b8
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-smart-is-state-of-the-art-ai-rotoscoping/
frame_count: 0
frame_status: pending-selection
---

# How SMART is State of the Art A.I Rotoscoping?

**Source:** [YouTube](https://www.youtube.com/watch?v=AinQkgdR6b8)
**Author:** Compositing Academy
**Duration:** 19m23s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py how-smart-is-state-of-the-art-ai-rotoscoping <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Rotoscoping has always been one of the most time consuming tasks in VFX, tracing objects
[0:04] by hand to cut them out perfectly.
[0:05] Today we're testing AI powered roto by the Foundry.
[0:08] In order to test this properly, I came up with a few benchmarks that I think might be
[0:12] useful to see how this smart roto compares against some of these fundamental concepts
[0:17] of rotoscoping.
[0:18] So some of the examples we're going to look at is something like a straight profile shot.
[0:22] So this should be the most straightforward one, but we have different things going on.
[0:26] It's not a linear camera move.
[0:27] The camera's rotating in different ways.
[0:29] So we have nonlinear rotation.
[0:31] We have scale that's changing of the object getting closer.
[0:34] So the roto shape should get bigger if it's going to be smart about this.
[0:38] And we'll see if that can help us.
[0:39] And it's kind of a long frame range as well.
[0:41] So that's a lot of frames that you have to normally roto, but it wouldn't be like an
[0:44] overly complicated shot either.
[0:46] Now we're going to step into a more advanced example such as basically more motion blur.
[0:51] So I have this camera flying past here just to see how it's going to deal with edges that
[0:55] are a little bit lower contrast and we sort of lose the perception of the edge a little
[0:59] bit.
[1:00] So it's going to be a little bit trickier, but there's still some indication of where
[1:03] the edges are.
[1:04] I did also throw a little bit of extra challenge into it such as the light basically changing
[1:09] color or moving or shifting slightly on the edges.
[1:11] So you can see here at the beginning our hand is like a certain amount of brightness.
[1:16] And at the end it's a little bit brighter and maybe it's shifted up and now it's gotten
[1:19] a little bit dark on the finger.
[1:20] So we want to see how does it deal with slightly changing conditions because that's going to
[1:24] be a realistic scenario for roto.
[1:26] It's not going to be a perfect lighting condition every time.
[1:30] Then we're going to test occlusion.
[1:31] So we want to see how does smart roto handle or deal with objects passing in front of our
[1:37] roto shapes.
[1:38] Is it going to throw the shapes off or is it going to maintain the profile throughout
[1:41] that action?
[1:44] Then we can test one more thing, same shot as before as the motion blur shot, but we're
[1:48] going to do something called loss profile.
[1:50] So instead of us seeing this two dimensional profile that stays the same as we sort of
[1:56] look at it, the silhouette isn't changing if we think of it as a two dimensional object.
[2:02] This would be the opposite of that.
[2:04] So if we look at the thumb for example and we look at the end of the shot, the perspective
[2:08] is completely changed.
[2:09] So we want to see how it deals with situations where the profile is not predictable throughout
[2:14] the entire result and see if it can maintain some sort of stickiness to that as it's morphing
[2:20] through that shape.
[2:21] And then the last test I want to do is an undefined profile.
[2:25] So this would be the hardest one, but we have a shape that's just basically morphing.
[2:30] So we have this person walking and we're going to try to roto some of the dress and see can
[2:36] it deal with a very undefined profile, something that's basically unpredictable in terms of
[2:42] how that shape is going to look in the next few frames.
[2:45] So that is basically the benchmarks I think are useful and it goes back to those first


### Current Problems with Segmentation [2:50]
**Transcript (timestamped):**
[2:50] principles of rotoscoping.
[2:53] So before we jump into smart roto, there's one thing I want to bring up that you might
[2:56] be thinking about.
[2:57] AI segmentation, which is generating an AI roto automatically already exists.
[3:02] There's a bunch of models that have been improving as well.
[3:05] But if we think about what actually the problems with rotoscoping are, you'll realize that these
[3:09] are not actually the one click solution that often they're sold to be.
[3:13] And the reason for that is because the standards on feature film versus social media are drastically
[3:19] different.
[3:20] So if we look at something like a segment anything, we put this on, we can see there's
[3:23] some jagged edges and things that this would be good enough for a garbage mat, which is
[3:27] actually useful for lighting slap comps and different things in production.
[3:31] But for a final result, this is not going to work very well.
[3:34] So we can't really use that as a final result.
[3:36] And so what this VITMAT does is it takes a rough roto or a rough alpha and essentially
[3:41] can sort of do something that looks a little bit almost like a key.
[3:45] But if we look at the result, it can definitely clean up some edges.
[3:48] So this is a very useful tool.
[3:49] And sometimes you can extract some hair detail and different things like this by using these
[3:53] tools together with these sort of improvement models.
[3:56] But still it's not quite what we need.
[3:58] You can still see there's some jagged edges.
[4:00] And if we look at the final result, there's a little bit of like webbing between the fingers
[4:04] and it's just not close enough for final results still.
[4:08] So although it can help in some situations to maybe blend it in.
[4:11] This is why Smart Roto was, I think, created because you need that fine tune control that
[4:16] artists can fix and make that perfect result that we expect.
[4:19] And so here's another example of a shot that these AI segmentation models would have a problem
[4:24] with is if we try to just use a segment anything, we can get a coarse roto and maybe we could
[4:29] try using VITMAT on this as well.
[4:31] We get something slightly better, but still we see some jagged result and we're getting
[4:34] a little bit of that webbing in between the fingers.
[4:37] So it's not quite understanding, especially in a lower contrast shot.
[4:40] It doesn't have the intelligence to give you perfect results.
[4:44] So anyone telling you that that's the case is probably doing social media content or
[4:49] a broadcast content that doesn't have the same standard as feature film.
[4:52] So Smart Roto I think is going to be for artists that really want that higher level result.
[4:57] So let's give Smart Roto a shot and see what we can get for a mat here.


### Trying Smart Roto [5:00]
**Transcript (timestamped):**
[5:00] So I'm just going to try to roto this thumb and see how many frames can it generate instead
[5:04] of me having to roto it, especially as it scales and moves away and rotates and all those
[5:09] different factors we have.
[5:10] So I'm going to quickly roto this and then we can take a look at the next steps.
[5:14] Okay, so now I have a base shape here.
[5:18] I'm going to go to the Smart Roto tab, which is what comes with Smart Roto.
[5:21] And it's pretty simple actually.
[5:23] So if you read the documentation, they basically say you need at least two good frames to start
[5:27] with which gives it some indication of how the shot is going to progress.
[5:30] So I have one frame here.
[5:31] Now one of my favorite features is that I played with is actually really cool.
[5:36] So if we go back in time in the timeline and I want to set up my second frame to give
[5:41] it a good reference, there's a button here that's basically the center button, which
[5:45] is going to do that big transformation for you.
[5:48] It's going to run Smart Roto on one frame.
[5:50] So I'm going to hit this one time and see that it actually snapped to position.
[5:54] So it's not 100% perfect, but this is our hero frame that we need to align.
[5:58] But just this alone is really cool that it can sort of snap things into position and
[6:02] give us a really good 80% of the way there.
[6:05] And we just adjust the points very slightly like this.
[6:08] So that alone is a pretty cool time saving feature.
[6:12] Definitely one of the coolest features I saw as part of this.
[6:15] So go through smoothies out a little bit and then we'll get a good hero result as well.
[6:21] Okay, so now we have two hero frames, one at 221 and one at 157.
[6:27] So I'm going to run Smart Roto just between these frames.
[6:30] And actually, you know what?
[6:31] We'll run it all the way to the end of the sequence.
[6:33] And you know, even though I don't have a third key frame here and just see like how far is
[6:37] this going to go before it starts to get confused or if it does get confused.
[6:41] So I'm going to hit create smart keys and I'm going to start do one to 250.
[6:47] And I'm going to do it backwards because my two key frames are mostly at the end of the
[6:51] sequence.
[6:52] So rather than starting at the beginning, which is going to be drastically different
[6:55] and there's a little challenge that through in here where the hand actually closes, I'm
[6:58] going to run it backwards because this is where our actual key frames are starting.
[7:01] So we'll set this to backwards and we'll let it go and see what the result comes up with.
[7:06] All right, so we have back our first results.
[7:08] It took me about three minutes on my machine or about two minutes 40, I think.
[7:12] I have an RTX 3090.
[7:13] So it's mostly GPU process and it's done, you know, a pretty decent amount of frames
[7:18] here.
[7:19] So we started back on this frame so we can look at our original frame.
[7:23] So it did roto all the way to the end.
[7:25] If we look close, it's doing a pretty good job.
[7:32] I would say like maybe I could adjust like this one point and just refine it so you can
[7:36] basically just say run it again, it will go between the key frames.
[7:40] So so nice thing about this is you could use the end frame here like 249 and just, you
[7:45] know, add one key.
[7:47] And so if we go backwards in time between the two existing key frames, that's probably
[7:50] the most interesting part here between the two hero key frames I gave.
[7:55] This is looking pretty solid.
[8:00] Maybe we could adjust the very base of this like by like a pixel or something and maybe
[8:03] add an additional frame.
[8:05] But for the most part, this is looking pretty good.
[8:08] So what's interesting about this is like because I use the white hand as well, it's not the
[8:13] easiest thing to planar track necessarily.
[8:15] There's not a lot of high frequency detail.
[8:18] I actually did that on purpose because I want to see like, how does it compare to a planar
[8:22] tracker that has texture detail to stick to easily without being slightly thrown off.
[8:27] And so as we go back in time here, let's go back to our last key frame was 157.
[8:31] So anything before this is now generated key frame result as well.
[8:35] So we can see it's slightly off here.
[8:37] So what we could do, we could go here and just add one key frame.
[8:41] What's nice about having this smart roto base is it's basically just saving you time of
[8:45] getting that 80% of the orientation correct and scaling correct.
[8:51] It's actually pretty interesting how it's scaling all these points as we zoom out here.
[8:57] Now one interesting part was when it started to turn.
[9:00] I didn't give it any indication of hero key frames here yet.
[9:03] So the fact that it started to get that base orientation closest is pretty interesting
[9:08] as well.
[9:09] But it does go a little bit off.
[9:10] So I think you'd need like maybe five or six key frames across the whole sequence to make
[9:14] this sort of stick all the way through.
[9:17] But the fact that I started with just two is pretty interesting.
[9:20] So again, we'll go towards the end here.
[9:23] We use the smart roto as the base.
[9:24] We'll give it a few hero key frames.
[9:27] And now we have five hero key frames overall.
[9:29] And we could run this again and get an even tighter result.
[9:32] So let's see how that does.
[9:34] And also I'm going to remove the smart keys just so it gives us a clean result.
[9:37] So I'll say remove, we'll delete these.
[9:39] And now we just have our hero key frames replaced.
[9:41] Okay, so I ran it again.
[9:42] So we got another two minutes here.
[9:44] So probably around five minutes total of using smart roto and five key frames.
[9:50] And this is what I have.
[9:51] And this is looking pretty solid.
[9:53] It's sticking almost all the way through until we have like even here when it starts to bend,
[10:01] it's interesting.
[10:02] I haven't put place any hero key frames here and it still does stick a little bit.
[10:05] But here it starts to go off.
[10:07] When everything starts to come together, it does break apart here.
[10:10] So I think you would need more hero key frames around when there's a significant shift.
[10:15] But for the most part, it's still saving a lot of time here.
[10:18] And what's interesting about this is maybe it's better than an actual planar track as
[10:22] well because the points are still kind of shrink almost shrink wrapping to the shape
[10:27] as the scale is going as well.
[10:29] And the perspective of having a slight shift.
[10:31] So I do think this is almost, it almost feels like a slightly smarter planar track that
[10:36] actually just knows where it is on the edges that doesn't rely so much on just the texture
[10:40] of the thing we're trying to roto.
[10:42] So that's pretty interesting for the first test.
[10:44] Now one thing to remember is I do one shape on the thumb, but smart roto can run on 10
[10:50] shapes at the same time.
[10:51] So you could draw all these fingers, put five key frames, and then you'd have all of the
[10:54] fingers in almost the same amount of time.
[10:57] So that's worth noting as well.
[10:59] So let's try it on test number two with more motion blur.
[11:02] So this is not something that if you were to, you know, try to planar track would be


### Motion Blur Shot [11:03]
**Transcript (timestamped):**
[11:06] very ideal because there's a lot of motion blur.
[11:09] There's not a lot of texture detail.
[11:10] It's low contrast.
[11:11] It's not an ideal situation for a planar track especially.
[11:14] So if we're making a comparison to that as well, it's worth noting.
[11:18] So I'm going to try to roto this sort of pinky finger where it's low contrast in the middle.
[11:22] We have motion blur and we get some interesting overlap at the end.
[11:25] So the fingers going to overlap.
[11:26] We have occlusion and then we have a pretty defined profile at the beginning.
[11:31] So I'll give it three key frames.
[11:33] Let's say one here, one at the end and then one at the beginning and we'll see if that's
[11:38] enough to basically track this through.
[11:46] And here's the result.
[11:47] It ran about 10 seconds very quick and this is sticking pretty good.
[11:52] It did a good job even as we're flying in crazy here.
[11:57] I did trick it with my little purple light here.
[11:59] So we see as the purple edge comes in, it's thinking that this is the finger.
[12:02] So we could just adjust that one frame.
[12:06] And so those kind of drastic color shifts are probably of course going to throw this type
[12:10] of thing off.
[12:11] But it's interesting just to see and see how it thinks.
[12:15] So if I just adjust that shape and add one key there, we can always rerun it and I'll
[12:19] just tweak it on this frame as well because this shape is pretty different.
[12:22] Okay, so we got a few more key frames in here.
[12:24] Let's run it again.
[12:25] And this is our result.
[12:26] So this is looking pretty good.
[12:28] I didn't spend too long on this either and it stuck to the outside edge pretty well.
[12:32] So it's definitely speeding up the process.
[12:34] And it didn't completely go off like crazy on the occlusion.
[12:38] I had a little bit of problems when the sort of the color shifting and the pattern looks
[12:42] a little bit different.
[12:43] But I think that's to be expected.
[12:45] I think as we see drastic shifts, you'll have to add a few more key frames in those spots.
[12:49] If you're having most of that sequence covered, it's definitely saving time.


### Occlusion Shot [12:53]
**Transcript (timestamped):**
[12:53] All right, so let's try something a little bit harder.
[12:57] Let's try some real occlusions really passing over the fingers here.
[13:00] So one of the things mentioned in the documentation is if you create multiple shapes, in other
[13:05] words, instead of like the prior examples, just doing one shape, I'm going to draw three
[13:09] shapes on a finger and see if those other shapes help maintain it because the more
[13:14] shapes you have, apparently it informs the other ones how they're supposed to say similar.
[13:20] So what I think I'm going to do is I'm going to put three shapes on this finger at the
[13:24] beginning.
[13:25] We'll try to do it right here in the middle as well.
[13:28] And then we'll do one at the end and see if it gets thrown off as that occlusion goes
[13:32] across that leaf pattern and see if that's going to affect it.
[13:36] Now we also have some shadowing on the fingers as well.
[13:38] So the colors are shifting a little bit.
[13:40] So various factors here that could be interesting to test.
[13:45] So I have my quick rotor here on the finger and then we'll jump to the end where it can
[13:49] still see the finger.
[13:50] Let's see if the smart rotor will just jump on there and it did a good job.
[13:55] So we're just running it on one frame, getting it mostly aligned, like I said.
[13:58] So that's how we can set up our hero keyframes faster than doing the hero keyframes completely
[14:03] by hand.
[14:04] So we can get that approximation, which is really nice.
[14:08] So I'll just finish this up.
[14:10] Now for that middle frame, let's see if it can approximate that without me having to
[14:14] align it manually.
[14:15] I doubt it because this pattern is right in front, but let's try it.
[14:18] So I'll try it.
[14:20] And actually it did a pretty good job.
[14:22] So it actually can see the upper part here and understands the relationship between the
[14:26] different parts.
[14:27] So I think that's the key here.
[14:28] If you just had one part passing behind the shape, it probably is not going to quite understand,
[14:32] but having those additional shapes when their occlusion is going to be necessary.
[14:36] So that's very interesting that even the one frame auto line was able to get us most of
[14:42] the way there for our hero alignment here.
[14:45] So I'll just clean that up.
[14:46] All right.
[14:47] So here's the first result.
[14:49] When it's not occluding, it's all sticking pretty well.
[14:51] When we get some pretty heavy occlusion, it does start to jump around and break.
[14:55] So we're going to need more key frames when it's getting heavily occluded like this.
[15:01] And so let's just clear the current keys.
[15:04] Let me add maybe like four frames in that heavier section with occlusion and see if it's
[15:10] going to be better.
[15:11] Okay.
[15:12] So here is the result again.
[15:14] And again, it's jittering a little bit.
[15:15] So I did add a few key frames in here.
[15:17] I added about five or four or five different key frames in the middle.
[15:22] And the smart road was actually causing more problems than it's helping with.
[15:25] So the way I would look at this is I would just, if there's heavy occlusion and you're
[15:29] losing half of your shape there, I would use this auto line feature to get the approximation
[15:35] because that was working really well to just get it in the main place.
[15:38] But letting it auto run just through heavy occlusion is probably not going to be a good
[15:42] idea.
[15:43] So the good thing about this is we can run smart keys on only portions of our sequence.
[15:47] So if there's all of this part of the frame range where we don't require Roto and all
[15:51] of this part, then we can save ourselves some time.
[15:53] But I wouldn't run the smart key frames through heavy occlusion based on what I'm seeing here.


### Perspective Shift Shot [15:56]
**Transcript (timestamped):**
[15:57] So our next test here is the lost profile.
[15:59] So I want to give it some main hero indication of each profile.
[16:03] So I think there's at least four or five keys that I want to do here.
[16:07] So this is kind of what I've done.
[16:08] Any major shift of perspective I've given it and also all the way back at the beginning
[16:12] of the sequence, I gave it one frame.
[16:14] So can it do the rest and save us some time?
[16:17] But we still give it an indication of what's happening, which I think based on what I'm
[16:21] seeing here is going to give it some kind of result.
[16:22] So let's let this run and see if it does a good job.
[16:25] And here's the result.
[16:26] So we can see this end where I've given it a few key frames is doing a good job for the
[16:33] most part.
[16:36] Now this is interesting because there's no clearly defined line of what we could actually
[16:39] Roto on this hand.
[16:40] And this is where you would use like overlapping shapes and different things like that.
[16:43] So it's interesting to see how it's interpreting this part here.
[16:47] But as long as we're keeping the edge, that's really what we're concerned about.
[16:51] The only part where it slides is maybe where we had a bigger gap of key frames.
[16:54] So here it's still doing a pretty good job on the, I would say 80% of the placement,
[17:00] but it's just like small areas like this where it doesn't understand that that's part of
[17:03] the hand, especially because again, like I said, I threw that purple light on there,
[17:06] which might be throwing off what it thinks is the edge.
[17:09] It might be looking at the edge color as well.
[17:12] So some materials have for now, they have different reflections, specular surfaces.
[17:16] So I do think it is a realistic result to have some sort of not perfect base color to
[17:21] test with, but we could throw one additional key frame on there just to get that little
[17:25] edge.
[17:27] And it's still, it's still helping out here.
[17:29] So we can give it that one.
[17:31] And so here's the result with two extra keys there.
[17:33] And this is doing pretty good now.
[17:35] So it does feel nice to have, it feels iterative, it feels like you're working with the computer
[17:39] to like give it an idea of what it is, but it's still saving you time on like every single
[17:44] point or every minor adjustment.
[17:46] So that's how it feels working with this.
[17:48] And it's very interesting.
[17:50] It feels like, like I said, like sort of a smart planar tracker that doesn't require
[17:55] all the detail a planar tracker would require.


### Lost Profile Shot [17:57]
**Transcript (timestamped):**
[17:58] And the final test here is I did this dress that's kind of waving around.
[18:05] I ran this, I basically put three keys, I put one at the beginning here, shape like
[18:09] this, and one here and one here.
[18:12] Now maybe I need to break that up into more shapes.
[18:14] I'm not exactly sure, but it's hard to break this into shapes because the fabric is basically
[18:19] flowing in so many directions.
[18:20] So I did run Smart Roto on this and it does get thrown off quite a bit.
[18:25] So with a completely undefined profile, that's not quite predictable in terms of the motion
[18:32] across frames.
[18:33] It's probably not going to do as good of a job.
[18:35] So that's basically the test I did on this one.
[18:40] But it is interesting to know where it's going to be useful and where it's not going to be
[18:43] useful.
[18:44] I think, like I said, that's probably a less useful scenario.


### Conclusion [18:45]
**Transcript (timestamped):**
[18:46] So overall, I think it's a very interesting tool.
[18:48] I think it's going to save sections of Roto in entire shots.
[18:52] So even if it doesn't cover every single occlusion or drastic change, I think there's a lot of
[18:57] Roto that's just tedious.
[18:59] Rotations or secondary rotations or you imagine objects, you know, a hand is a good example,
[19:03] because a finger has multiple rotation points.
[19:05] So if it's solving all of those rotations plus the camera at the same time, when the profile
[19:10] is not drastically changing, it's still saving quite a lot of time.
[19:14] And in the arsenal that we have, I think it's a very useful addition.
[19:18] That's about it for this video.
[19:19] If you liked it, make sure to hit thumbs up and comment what you think.



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
