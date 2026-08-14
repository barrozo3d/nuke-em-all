---
title: This Forgotten VFX Trick Is Still Shockingly Effective
source: YouTube
url: https://www.youtube.com/watch?v=8yOyb0Uyq6s
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/this-forgotten-vfx-trick-is-still-shockingly-effective/
frame_count: 0
frame_status: pending-selection
---

# This Forgotten VFX Trick Is Still Shockingly Effective

**Source:** [YouTube](https://www.youtube.com/watch?v=8yOyb0Uyq6s)
**Author:** Compositing Academy
**Duration:** 16m15s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py this-forgotten-vfx-trick-is-still-shockingly-effective <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to this tutorial. We're going to be talking about how to merge practical saliva that was filmed with a CG dragon and how I brought these two things together.
[0:08] So there's always multiple ways to do things. You could use a full CG saliva, you could use some practical elements.
[0:13] I've always been interested in merging practical with VFX. That's why I like compositing. A lot of it is merging filmmaking with real footage.
[0:21] And so this is one approach that you can use. And there's different scenarios you can use it. So it's not just for saliva.
[0:27] There's different situations that this sort of line of thinking can be pretty useful. Now, this is part of the CG integration masterclass that just released.
[0:34] So if you're looking for practice to do more CG integration, working with high quality assets and just improving your demo reel for more opportunities, check out that in the link in the description below.
[0:44] Now, in the full course, there's some extra techniques as well with particles and creating dragon breath and pushing the effect a little bit further than just the one single element.
[0:52] And now let's check out the tutorial.
[0:53] Okay, guys, so we're going to talk about adding these saliva. And this is a really cool fun technique. This can be used in all kinds of different shots, the specific technique.
[1:02] But this one is going to be pretty interesting because there's a bit of complex motion and maybe a little bit of retiming or adjusting the timing to get it to work,
[1:10] as well as paying attention to aspect ratio and just if the specific technique we're using breaks at a certain angle, what do we do in that situation?
[1:19] So before we jump into this, let's talk about the element. This is a practical element shot with the iCandy XYZ guys, the guys who made the dragon.
[1:27] So they did this really awesome element that was actually used for different project there, but it looked perfect and they were willing to give it.
[1:33] So big thanks to them on letting us use this. So definitely go check out their website if you ever need a high quality 3D monster or creature or anything like that.
[1:44] So those guys are really awesome. This is perfect for what we need. We just need to get it to track on properly.
[1:49] So I've already done the tracking of the cards in 3D space. But before we get into the technicals of this, let's just talk about the actual technique itself.
[1:57] So if we think about what we're doing, this is an old video game technique from like the 80s or even the 70s, I believe they were doing it.
[2:05] Old video games like how do we get something that looks 3D but just put it on a 2D plane? You're probably familiar with this.
[2:10] If you run around in a video game, you ever look at the grass? It's usually all on sprites. They're just these two dimensional planes.
[2:16] And if we reveal the plane, it's actually just a 2D video or 2D texture sitting on one single polygon.
[2:22] So if I rotate it, it looks 3D, but we can't go like 90 degrees otherwise it just disappears.
[2:29] So we can go maybe about 70 degrees before it starts to break. We can go all the way to maybe about there even before that this plane starts to become obvious that we're not looking at a 3D effect.
[2:40] But composters, we're doing this trick all the time and there's a lot of scenarios where it's more cost effective to do this than to do an entire effect simulation.
[2:48] That's where asset libraries come in, we're putting them on 2D cards and all that kind of thing.
[2:52] And sometimes you can lock the rotation of the card to always face the camera. That's what they do in video games.
[2:57] This card, no matter where you look at it from, will always face you. So it keeps rotating around and you just don't see it rotating.
[3:04] But some sprites will actually have a freedom of rotation, like I said, to about maybe 70 degrees.
[3:11] So we can rotate them a little bit. Now this concept is what I was thinking about when I was putting the saliva on the dragon.
[3:19] Now our card is tracking on the CG. It's not just like 2D card we put into space. It is tracked to the mouth of the actual CG monster here.
[3:32] So if I look at the rotation of the card, let's just put it on the tracker board to see it and hit play.
[3:38] You can see it's actually orienting and translating the same way that the mouth does.
[3:44] So if I put this over the CG just as a tracker board, we see it's tracked to the side of the mouth on the left side.
[3:51] So I've given you one on the left side and on the right side. So if I put these both together in a scene,
[3:59] and throw them both on there, and we can grade one a little bit differently. Maybe we'll grade this one like a little bit blue or something.
[4:09] Then we'll grade this one a little bit red, just so we can see the difference.
[4:15] Now, essentially it's a little mini triangle. But you can see that we're still following the principle of like,
[4:24] we're seeing this at a quarter, three quarter angle, I guess. So this whole sprite approach is going to work because we're following this technique.
[4:32] So here it is in 3D space. But we see both of them. So if I disable the left one just to see, we're not going beyond that 70 degrees here.
[4:40] There is one moment that our right card, I think it's the right saliva card, goes a little bit beyond where this technique will work.
[4:50] So right about frame 316, we're almost at that 90 degree angle. So we're going to almost lose the effect.
[4:56] The left side card is still fine. But this right side card, we're going to lose those a few frames, like three or four frames, where it's not going to work.
[5:04] But we're composters, we've got to be problem solvers. How do we fix it on those few frames? How can we essentially see that effect on just those essential frames there?
[5:15] That's the problem we'll solve next. But let's just get the texture working first before we dive into that.
[5:21] So I'll delete the, I'll just unconnect that for now. And we'll just start assigning the texture of this video.
[5:30] So first thing to pay attention to before we start just throwing stuff on a 3D card.
[5:34] What is the aspect ratio of this card? The aspect ratio meaning the ratio between the width and height.
[5:41] This is a perfect square. It's not a rectangle. And our video is a rectangle. We look at it. It's wider than it is taller.
[5:48] So first thing is to make your life easier, always match the aspect ratio of the texture to the 3D thing that you're putting on.
[5:56] So we want to make this a square. So we can put it into a square. We can scale that up a little bit.
[6:02] And then we can move that into place like so. And we'll plug it into the texture on the card and see where does that put us.
[6:10] It's going to be pointing the wrong way. The UVs are incorrect. So we're going to need to flip that around.
[6:15] Because right now the snout needs to be there and snout is right there. So we need to rotate that by negative 90 degrees rotation.
[6:24] Or maybe it's positive. Let's see. But you can do it inside the reformat as well. So I already know what it is because I mess with it.
[6:30] You do a flip, flop, and a turn. And that will basically make sure that we're pointing at the right way.
[6:38] So you just keep rotating this until it's pointed the right way if you look at 3D space. But I already did it.
[6:46] So I know that those three is what you need. Otherwise you can just manually rotate it with a transform.
[6:53] So once we got that, now we can start to align this. So we can use the X and Y, the transform to start to get the edges of the saliva lined up with the edges of our dragon.
[7:05] We can scale this down a little bit maybe. And really luckily this element is timed so well that we don't have to do any kind of crazy warping or anything like that to get this to work.
[7:18] We just need to get it lined up. So if we hit play on this, it already works pretty well out of the box.
[7:25] Now we do have a moment where the mouth starts to close a little bit too fast and we start to see the teeth of the practical effect which we don't want.
[7:33] So we need to make the effect last a little bit longer. But other than that, our element does work pretty well.
[7:42] So even here, it's working pretty well. We just need to mask it so we don't see it at the beginning. And then we can just continue to mask it.
[7:50] So that's going to be some animated rotos where you're just going to cut off the top and the bottom.
[7:55] Now you can do that before you put it through the scanline render or after. It doesn't matter. It's probably easier before if you just take this and you can do plugging your roto like this.
[8:05] So it'll grab the format, hit replace. What that does is it makes the roto copy the square format, but replace, make sure it delete all the data that's there or the alpha rather.
[8:16] So what we do is we just circle. Let's do a stencil actually. We'll do a stencil. And then I can just take a roto and just chop off the top of the model.
[8:30] So we'll just chop off this and we'll say stencil. And then we can do the same thing for the other side.
[8:39] This. And then we can just chop off the rest as well. Do a rough, rough shape here.
[8:49] Good done a mask, but we might need to like move these around. So that's fine. So that's all good. Get this. And now we can look at it.
[8:57] We might need to adjust that black point there to get rid of the. The grain and such you can use a little bit key to sort of extract that.
[9:06] So that would be the clean way, but we'll just do it in a real quick version right now.
[9:10] Now, additionally, you can use maybe a little bit of a gamma if you want to see a bit more of it and then push the black point down slightly and we'll just put saturation at zero to get rid of any weird colors that are in there.
[9:24] So if you want to increase thickness, that would be a simple way to do it.
[9:30] And yeah, something like that. We can play around with that more. You can really you can really dial this in too.
[9:35] Now, the other thing you're going to do is there's motion blur on the dragon. So once we activate motion blur, let's say we put 15 samples, that's going to look a lot more natural.
[9:45] But for the sake of being fast right now, we'll leave it off just because I want to be able to visualize this quick.
[9:53] So it's working pretty well. But at the end, the mouth starts to come in like I said.
[9:58] So what you could do is do first of all, pause the video, see if you can figure it out.
[10:03] How would you deal with this problem? How do you deal with it?
[10:06] The video being too short. See if you can have that problem solving.
[10:11] Because your job, if you were doing this on your own, is really to figure it out.
[10:16] Not to be shown. So see if you can figure it out.
[10:19] If you can't, we'll continue. So do a I'm going to do an overflow.
[10:24] And there's a few different ways you can do it. There's not one right way really.
[10:29] But let's say that around, I don't know, let's say 330. It's still pretty good.
[10:37] Because I'm going to cut it off on the top of the gums. So here it's still fine.
[10:41] What you could do is just reverse the footage. So on this on the overflow, I can set this to frame.
[10:49] And that will re time into the current frame. So instead of actually, sorry, we want to set the method to motion and set the input timing to frame.
[10:59] So it'll blend the motion, but the timing is based on the current frame.
[11:03] So in other words, if we type three, if we type the current frame 330 and set a key,
[11:08] but then we go 10 frames in advance and say instead of it being on 340, which is what it would normally be, we set it 320.
[11:16] So as it goes forward 10 frames, the video plays backwards 10 frames.
[11:21] So if we look at this, all we're doing is making that extend longer. That's what we're doing.
[11:28] So we're not really perceiving that that that the footage is reversing. We can get away with some of the trick.
[11:34] So we can set this to zero and then set this to one.
[11:38] And then this is just going to continue jiggling around for a few more frames.
[11:43] And as he closes his mouth, as he closes his mouth, we can just wrote it off.
[11:53] Now we might need to shift that the texture on the x a little bit. So let's see if we adjust this down.
[12:01] We might need to animate exactly where it is on the x slightly if it if it goes off center a little bit.
[12:06] So a little bit of a manual adjustment on the x and y transform just to slide it just to make sure our edge is always sticking so that it's always on the mouth.
[12:16] So even here, yeah, even here, it kind of continues down.
[12:22] So basically, I would just finish this off by rowing off on the edges.
[12:30] Make sure you have the motion blur on so that it's not sticking out.
[12:36] And make sure that we don't have overly bright areas where it's shadowed.
[12:41] So to detail this up, you want to go in here maybe the road.
[12:45] So, you know, just darken around the gums, for example, so you could let's see, we go back in time here.
[12:54] We pull this down.
[12:59] And then we could darken, let's say, the top of the bottom, something like this.
[13:09] And we'll just grab the format again, hit replace so that this is matching square.
[13:14] And then we'll just blur that a tiny bit.
[13:17] So we're kind of fading it up.
[13:20] We don't want to see the edges like super exaggerated there.
[13:24] That's a little better.
[13:27] We could just darken it just a little bit more.
[13:32] And yeah, you can dial us in, like I said, but this is the main idea.
[13:38] Okay.
[13:41] All right, so that's the main idea there on the left side.
[13:46] Now you do the same thing on the right side.
[13:48] So you would just take the right saliva, you know, and line that up.
[13:53] So let's say this actually, let's just see what our existing one looks like.
[14:02] See if all the work we did can transit over.
[14:05] It kind of translates, but you might need to adjust the X and Y position to get it to look natural.
[14:12] And then the other thing that I did was essentially masked it behind various features.
[14:17] So if I look at mine here, what I did was stencil it behind different areas.
[14:26] So I think here I use the top of the mouth to just chop it off.
[14:30] But I also used some of these mattes I already have, like the edges of the lips.
[14:37] And then that's just, I'm just using that to roto off the edge, so I don't have to do it manually.
[14:41] So you can do it either way, like the way I showed before, or just do it this way.
[14:46] And you can also, you know, cut off the teeth if you wanted, if you wanted to be behind some of the teeth
[14:50] or in front of some of the teeth, it's up to you.
[14:54] And as long as we're getting this effect in there and not sticking out in any odd way.
[15:02] So I have the left side, I have the right side. This is the right side.
[15:06] I use the other clip that's very similar.
[15:09] Same approach.
[15:12] Now, the trick here is when it faces us at that 90 degree angle and it breaks, which it does,
[15:18] I basically just manually took a piece of the video and just grabbed a few frames where it's jiggling around,
[15:25] but it's facing us. I didn't even use a 3D system.
[15:28] You see there's no scan line, there's no card, nothing.
[15:31] I just took a piece of the video where it's jiggling and just on those two or three frames,
[15:34] I just replaced it and just 2D tracked it by hand with a, you know, X, Y, you know,
[15:39] it's only like three frames. So you can just kind of track it on there, add a little bit of motion blur.
[15:44] Now we're covering that little 90 degree turn where essentially, you know, this is not going to cover, right?
[15:50] So those few frames, we're going to lose it.
[15:53] We can just 2D track it from the front point of view and get the jiggling saliva that we need there.
[15:58] And that's pretty much it. So use the crypto mats to your advantage.
[16:02] Use the rotos to your advantage as well.
[16:05] Follow the rules of this technique and you'll be able to get your saliva looking pretty good.
[16:10] And that's about it for this specific video on the saliva.



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
