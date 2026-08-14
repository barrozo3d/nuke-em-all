---
title: Normally it costs $50,000+ For This Camera Move
source: YouTube
url: https://www.youtube.com/watch?v=GG7c29nWD68
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/normally-it-costs-50000-for-this-camera-move/
frame_count: 0
frame_status: pending-selection
---

# Normally it costs $50,000+ For This Camera Move

**Source:** [YouTube](https://www.youtube.com/watch?v=GG7c29nWD68)
**Author:** Compositing Academy
**Duration:** 8m57s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py normally-it-costs-50000-for-this-camera-move <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In this video, we're going to talk about how to take a real camera move that has been camera tracked
[0:04] and exaggerate the movement to make it more interesting.
[0:07] In our example scene here, we have a shot where a person was sitting on a green screen
[0:10] and we're going to be taking this person and making them traveling on a vehicle going super fast
[0:15] and this was filmed using a drone. So the drone is basically oriented and locked onto the subject
[0:20] and will orbit around in a circular pattern around the person, which gives a pretty cool effect by itself.
[0:26] But we want to exaggerate that camera move and make it actually more extreme
[0:30] just to give the action into the sequence. In a large VFX studio, this is usually called a
[0:34] re-rack or a reposition. Sometimes in studios, they'll also call it a card rig
[0:39] and essentially that's what we're going to be doing this video.
[0:41] So first I want to kind of explain this concept and break it down because there's some things we can do
[0:45] with this technique and there's some things we can't do and it's important to understand what exactly we're trying to achieve here.
[0:51] So first we have a camera track to start with. So the camera, the blue camera here is the real camera
[0:56] pointed at the subject and we're orbiting around in this sort of spherical pattern,
[1:00] which is why I like this drone technique, by the way. You can get really cool effects with
[1:04] a drone flying in super interesting ways that you wouldn't be able to do with a handheld gimbal
[1:08] or really any other mechanism. Really the feeling I wanted to mimic in a sequence that I'm directing
[1:13] is this kind of effect where there's a car traveling with the actor and basically driving
[1:18] with the actor to create an action scene. So if we expect that this type of camera is going to be moving in that way,
[1:24] there's going to be some secondary motion that would be more interesting than maybe what you would get
[1:28] on a perfectly smooth drone. And so that might be things like the camera shaking or pushing in or pushing out
[1:33] in more extreme ways that you could safely get close to the actor by doing. And so this is what I had in my head
[1:38] when I was directing the sequence. I wanted to have something similar to this effect,
[1:41] but we're going to do it with a drone instead to show that really any filmmaker, if you use the right tools
[1:46] and resources can pull off these effects if you know the techniques. So if we go back to our little diagram here,
[1:51] we have the drone in the normal camera track pattern. But what we're going to do is create a duplicate
[1:56] camera and we're going to exaggerate the effect. So I created this little diagram here. So if I press this
[2:00] button, here's what we're going to be doing. So we're going to duplicate the camera and we're going to
[2:04] add different noise patterns and different, basically just adjust the curves, but make sure we're staying
[2:09] close enough to the original camera that the effect still works. So because the person is
[2:14] essentially going to become a 2D footage on a three dimensional plane, we can't go all the way
[2:20] around the person. That doesn't make sense because it's a 2D video, you know, you can't, it's not a
[2:24] 3D character, but we can go to some certain degree of freedom here without breaking the effect.
[2:29] And it's very common in visual effects studios to do this to sort of repositioning effect. So here
[2:34] you can see as long as we're kind of in the right perspective of the original camera, we're getting
[2:38] something that's better than just like a person on a 2D plane and then just creating virtual camera.
[2:43] That's why you want to track your camera first because you're getting the perspective shift
[2:47] of the real person and then we're just kind of pushing it a little bit. Now, if I would have
[2:51] pushed this up a little bit too much, let's say we push the side to side more exaggerated,
[2:55] it's going to break probably, you know, maybe 15 or 20 degrees is not going to go that far. So
[3:01] there is some limitation on the side to side, how far you can go there. But something that's
[3:06] interesting is if we reduce the side to side, keep it a little bit closer to the original camera,
[3:10] and we increase the forward and back, that's something you can actually get away with because
[3:14] the perspective is more forgiving. And so you could do a really extreme camera move from being
[3:20] very, very far away and pushing into where the real camera sits. Sometimes this is called a camera
[3:26] handoff as well. So you could switch from a virtual camera and go into the real camera essentially
[3:32] by doing this effect. So this is the before and after just to give you an idea of what the result
[3:38] will actually be. So if we just look at this with just the default drone camera that's camera tracked
[3:43] and our guy is in there, this is called a lighting slap comp. So we've just put a rough key
[3:47] and projected this person into the right spot in 3D. So we can see like it does feel a little bit
[3:52] linear. It's kind of cool like to see the motion and some rocks and parallax and things like that.
[3:56] But could we make this more interesting? So if I disable this layer here and resolve and then we
[4:01] look at this version. So this is with the exaggerated camera move. So basically, I've added some tilt
[4:06] to the camera and I'm also adding camera shake, pushing a little bit closer, a little bit further,
[4:11] creating a little bit more parallax with foreground of the actual vehicle. So this gives us all this
[4:15] more interest versus just this perfectly horizontal orbit, which and you know, just the shake alone
[4:21] is a really big helping factor here to make this feel more intense. And so once the shot is done
[4:26] and we have like all the effects and the things that are becoming off of this and the full composite,
[4:30] it's going to be pretty insane. We also can play with things like the flare. So if we get close to
[4:35] the light here, we can flare up the camera and do different cool effects like that by having that
[4:40] just a little bit of extra freedom to direct exactly what you want. Now before we jump into the
[4:45] blender side, just to show what I did with the virtual camera, by the way, it doesn't matter
[4:48] if it's blender unreal, Houdini, these are principles, these are more important than
[4:52] which 3d software you use. It's just the idea and the concept. And once you know that it's like,
[4:57] okay, translate, rotate, adjust the curves, cool, you get the idea. It's also worth noting if you're
[5:01] not on the email list already, this is part of some new content coming out in the next few months.
[5:05] I'll be working with a team of artists to direct the sequence and it's going to be insane. So make
[5:09] sure you subscribe because it's going to be something that I don't think you can find these
[5:12] combination of workflows anywhere else. So we're here in Blender and this is kind of what it looks
[5:16] like. So this essentially is two cameras. We have the original camera and we have the modified
[5:23] camera. So if I just go here and we select the original and we just take a look. Yeah, this is
[5:29] the original. And then we have the second camera, which is this modified camera. And then we have
[5:35] a projection of the slap comp or the rough key that I did into the right position. So I'm using
[5:41] an image plane note. It's available on the Composite Academy Patreon, by the way. That's already
[5:45] posted there. It's a custom tool I made for creating image planes within Blender to make it an easier
[5:50] process similar to the way it works in Nuke, but with a bit more controls for specific scenarios
[5:54] like this. Otherwise, you can build this manually. All it really is is just a card that rotates and
[6:00] faces the camera and you can project out to certain distances. So there are different scenarios where
[6:05] you might want to animate that distance and I'll do some more future tutorials on some different
[6:10] concepts like that. But essentially, that's what it is. Just a camera projection from the original
[6:14] camera. So that's the important part of what I just said. The original camera is the one that is the
[6:19] projection camera. The texture comes from this non modified camera onto the plane. So that will
[6:25] make it so even though it looks weird here in like 3D, you know, if we look at the perspective of the
[6:30] guy, if we zoom in, it looks pretty weird. But if we look through the actual perspective, we see that
[6:35] it always matches because it's camera tracked. So the perspective matches here. And now we just
[6:39] need to duplicate the camera and add some kind of camera shakes. So you can find camera shake tools
[6:45] for free. There's a bunch of them on like Blender Market. If you're using Houdini on real, it's
[6:49] probably the equivalent in those softwares. Ian Huber has a pretty cool one called camera shakeify.
[6:55] And you could just throw that onto the new camera to add that motion or that adjustment to exaggerate
[7:01] some handheld feeling into it. And he has some pretty cool presets on that. So that's what I did
[7:07] first on the modified camera. And then what I also did was I basically just put an empty or
[7:13] something like that. Basically, you just need to put something in the center and parent the new
[7:18] camera to it and rotate that a little bit how you want to exaggerate it. So rather than messing
[7:23] with the curves, I didn't want to go too much into the curves of the modified camera. If you just
[7:29] parent that new camera to any kind of empty and Blender like an axis and you just rotate that empty,
[7:36] as long as your center point is at the center of where you want to be orbiting, because that's how
[7:40] this camera is moving, it's orbiting around the center, you put it there, you parent the new camera
[7:44] to it, and then you just rotate that around and now you can get the exaggerated camera motion. So
[7:48] that's pretty much really all it is, is just kind of grouping things together, adding a little bit
[7:54] of motion and that's basically it. Now, essentially at the end here is taking all of these things
[7:59] together and parenting it to a master sort of empty that is basically making the vehicle fly
[8:06] through space and that's how we're getting those things. So if I just re-enable the rock place
[8:13] holder, we can see that. So we're locked onto it right now, but if I just don't lock onto it,
[8:17] we can see like all of that in an isolated system, you don't want to think of the scene moving yet,
[8:23] you just want to think like how does the camera, how do you exaggerate it cool, none of it moves
[8:26] yet and then you take all of that, parent it to a master and then just slide that through and
[8:31] essentially you can get something like this. But that's essentially the main concepts. So yeah,
[8:37] hopefully that is useful for somebody. I'm working on the scene right now, we got a whole sequence
[8:41] working on and all the assets are insane, the effects are insane, so I can't wait to show you
[8:44] guys what this is going to look like when it's done. So this is not comp, obviously it's not
[8:48] even lit, but this is what previous looks like, I guess the previous stage when you're blocking it
[8:52] out and yeah, hopefully that's useful for somebody.



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
