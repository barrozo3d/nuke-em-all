---
title: Parallax HAX | Nuke Compositing [Advanced]
source: YouTube
url: https://www.youtube.com/watch?v=avtDQcZNThI
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "not specified (2021 upload, Nuke 13.0 era — see version-tracker.md)"
tags: [compositing, roto, rotopaint, st-map, channels, procedural-texture, grading, digital-matte-painting, advanced]
extraction_status: complete
frames_dir: tutorials/frames/parallax-hax-nuke-compositing-advanced/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Parallax HAX | Nuke Compositing [Advanced]

**Source:** [YouTube](https://www.youtube.com/watch?v=avtDQcZNThI)
**Author:** Compositing Academy
**Duration:** 27m3s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Welcome to this quick tutorial about creating some cheap parallax hacks in Nuke.
[0:12] This is a different tutorial, but I found it useful as I was messing around on a project
[0:18] I'm working on that will be coming out.
[0:22] I thought this would be cool for a YouTube tutorial as it's useful and pretty quick and
[0:26] easy to do.
[0:28] So, basically there's a way to cheap parallax without having to worry about 3D projections
[0:34] and all these longer processes.
[0:37] And as a compositor, I'm always thinking about level of detail and how to get things quicker
[0:41] and easier and to kind of get the impression of certain things.
[0:46] And thinking that way can save you a lot of time.
[0:49] So basically what this effect is, is if we have like a normal zoom, something like this,
[0:54] that's just like a, this is just a JPEG basically, and we're just pushing into it.
[0:58] So it's basically really simple, just to transform, animating the transform a little bit bigger.
[1:05] But what we can actually do is this effect.
[1:08] So we can actually fake parallax.
[1:09] So this is a fake push in.
[1:11] And we have, if you look over here and you look over here and you should look at the
[1:15] buildings and the way things are moving, it feels much more 3D than this.
[1:20] So this looks very 2D and flat and not so interesting.
[1:23] This kind of brings some life into it and gives us some interest.
[1:28] Now if this is a feature film, it probably wouldn't pass QC or something like that.
[1:33] Unless you know it's out of focus, which in this case, it actually will be in the end.
[1:37] The end comp will actually be something that's about a focus and a character coming towards
[1:41] the camera and kind of a rack focus happening.
[1:45] So in this case, it actually works pretty well.
[1:48] Yeah, I'm going to cover just how we can kind of create that.
[1:51] And there's a couple of different things going on here.
[1:54] So one, we have the parallax of the buildings.
[1:58] So the buildings that are closer feel like they're moving towards us quicker.
[2:02] We also have some parallax in the reflections of the glass.
[2:05] And that kind of helps sell this motion as well.
[2:08] And then obviously we have a couple extra little things that just to bring some movement
[2:12] in this camera, like some kind of moving water and some headlights kind of changing
[2:17] luminosity.
[2:20] Just to give this impression that when this is out of focus, we have some movement in
[2:24] the water and some maybe cars driving on the highway or something like that.
[2:29] So that's a couple different techniques in there, but I'll cover those two ones just
[2:34] at the end.
[2:35] But I'm going to talk about the parallax concept and how we can sort of do that.


### Parallax Review [2:40]
**Transcript (timestamped):**
[2:40] So just a quick review of parallax in a very basic way.
[2:45] Obviously if we zoom into a picture like this, there's no parallax between these three objects
[2:51] as they're all moving together.
[2:52] So that's really like our 2D zoom.
[2:54] And that's pretty much what this is, is a 2D zoom.
[2:57] But then we have parallax.
[3:01] We'll just take a look at it.
[3:02] And this is what parallax kind of looks like.
[3:04] So we can see objects that are closer, move much faster, relative to each other.
[3:09] And so that's an interesting way of thinking about it is if you think of a scale as a multiplier,
[3:17] you can essentially cheat parallax quite easily by thinking this way.
[3:22] So what I mean by that is, I'll show you with expressions and I'll show you with just some
[3:28] really simple transforms.


### Easy Parallax Technique [3:30]
**Transcript (timestamped):**
[3:30] So let's say we want this ball to be very close to the camera, like the blue one.
[3:35] So I'm going to start with just a static picture just to show you guys the easy way to do this.
[3:40] So we have the, let's see, which one is the blue one?
[3:45] This is the blue one.
[3:47] So this is the blue one.
[3:48] And I'm going to set a keyframe on the scale on this transform.
[3:54] And at the end, I'll just scale it up a certain amount.
[3:58] We'll say to 1.9.
[4:00] So this thing will basically come towards us at that speed.
[4:05] Now the very simple way of doing this would be just copying this transform.
[4:09] So I'm going to delete this and just copy it.
[4:12] So now we'll see that these two are moving at the same speed.
[4:16] And the very quick and easy way, again, to do this would be just lower this number.
[4:20] So a lower percent of this curve is the way you could think of it.
[4:25] So we could say 1.5.
[4:27] So now if you watch them, let's do a lower number so that we get a little bit more of
[4:31] an exaggerated effect.
[4:33] So now we can see that this one's moving much slower towards us, the green one.
[4:38] And if I clear my cache here, just make sure I don't have a duplicate keyframe here, which
[4:47] I do.
[4:49] So let me just set that to 1.2.
[4:52] So OK, so that one looks like it's a little bit further away now.
[4:56] And we can continue through with this.
[4:58] So if we copy this transform, put it on the red one, we'll make the red one even further.
[5:03] So we make the last number lower.
[5:07] So our last keyframe, which is 1.2, I'm going to make it 1.1.
[5:12] So that red one will move even less.
[5:14] So it's going to look like that one's even further away.
[5:17] And of course, we could apply that to a background and apply, put our last keyframe to, you know,
[5:25] let's say 1.05.
[5:28] And now we have the impression that this whole scene is like 3D.
[5:32] This is just with a couple 2D spheres scaling them at different speeds.
[5:37] And you know, we're always starting your keyframe at 1, and then we're just changing that last
[5:41] scale number.
[5:43] So if you had a lot of objects, it would be kind of annoying to go through and set the
[5:48] scale manually and all of them trying to figure out where they are relative to each other.
[5:53] So there is a way to do this using some basic expressions, which is what I did here, which
[5:59] is doing the exact same effect.


### Expression Linking for Parallax [6:00]
**Transcript (timestamped):**
[6:02] But instead of just changing the last number and kind of guessing, we can sort of set an
[6:07] expression here.
[6:08] So what we want to do is just take the red scale and drag it into the green scale.
[6:12] And that's going to make them stick together.
[6:13] But that's not doing exactly what we want, because we want the green one to move slower
[6:18] or a percentage of the red one.
[6:21] So what we can do is basically just do a multiply.
[6:24] So if we right click and say, modify expression or edit expression, we can take this scale
[6:30] and multiply it by a percent.
[6:32] So we'll say 0.3.
[6:34] So it'll move 30% relative to the red one.
[6:38] That's kind of what we're aiming for.
[6:40] The problem with this is on the first frame, if we apply this, it'll scale way down to
[6:46] like a small dot here.
[6:48] So that's not exactly what we want.
[6:51] So what we can do is we can add the 0.7 back.
[6:56] So we would say plus 0.7, because we want the first frame to be one, meaning the scale
[7:02] is one to one, and it's not going to change.
[7:04] So if we add that, and now we hit play, we see that the green one is feeling like it's
[7:09] further away relative to the red one.
[7:13] Now this is not exactly quicker than what we did before.
[7:16] You say, well, this is kind of a longer process than what we did before.
[7:20] What we can do is instead of doing this expression, because we have to do some manual math here,
[7:27] we're doing 0.3 and 0.7 and all this stuff.
[7:30] That's not exactly ideal.
[7:33] So what we can do is first we could solve for this 0.7, meaning if we do a little bit
[7:40] of math, we can get rid of this manual input, which is us just doing mental math to get
[7:48] this working.
[7:50] The reason we're doing this is so we don't have to do any mental math, and we can change
[7:53] this later on and make multiple objects cohesively move.
[7:59] So essentially what we want to do is we want to get that 0.7 mathematically.
[8:04] So if we take this expression and we put something in parentheses, we want to say we want to
[8:11] get this number to equal 0.7.
[8:16] If we take the animation and we subtract 1 from it, so 1 minus the scale, essentially
[8:31] what we can do is times 0.3.
[8:34] So we're taking this whole expression and we're subtracting it from 1.
[8:40] So if we take 1 minus 0.3, that's going to give us 0.7, which is exactly what we're looking
[8:48] for.
[8:49] The problem is this variable is animated.
[8:55] So even though it's going to give us the result that we want, let me subtract 8 off
[8:59] of there.
[9:00] So you see that the result is 1, which means our math is correct.
[9:04] So 1 minus the animation times 30%, this gave us 1, but this is not going to work if I apply
[9:11] it because basically it's always subtracting from itself.
[9:15] What you're doing is you're taking this whole expression and you're subtracting basically
[9:22] the opposite from it.
[9:23] So what you can do is instead of this being an animated number, this is an animated variable,
[9:28] you can say on which frame.
[9:30] So if we say frame 38, which is our starting frame, essentially now it's doing the same
[9:38] thing.
[9:39] So you see on our start frame, this is giving us the result of 1, which is what we want.
[9:46] We want it to be 1.
[9:49] And the reason we add this whole expression is instead of just adding 0.7, is because
[9:55] now we can change this into essentially something that can be modified.
[10:01] So with this whole expression, I'm going to change this little multiply, which is controlling
[10:08] how much it moves relative to this red object.
[10:11] I'm going to say times movement.
[10:16] Times movement.
[10:18] And so it says there's nothing named movements.
[10:21] We need to create a new variable.
[10:23] So what we can actually do is go into the node tab here and say manage user knobs and
[10:27] we're going to say we're going to add a floating point slider and we're going to say maximum
[10:33] 2, minimum 0.
[10:35] And we'll call it movement and then label it movement.
[10:39] And hit OK.
[10:40] And now if we slide this slider and we hit play, we can actually adjust how much this
[10:47] screen sphere will move relative to the red one.
[10:53] So if I put it above 1, it'll actually feel like it's closer to the camera.
[10:58] And if I put it below 1, it's going to start to feel further away.
[11:01] You see always on the start frame though, nothing is actually happening.
[11:05] And that's why we did that little bit of extra math, subtracting this here basically to get
[11:14] that effect.
[11:16] So I'll put the expression in the description below if you guys want to play around with
[11:22] it.
[11:24] And that will definitely kind of help.
[11:25] So you can now take this expression and you could put it on multiple objects and have
[11:30] them all moving differently and feeling like things are more 3D or less 3D.
[11:38] So what we can do for our scene here to take this concept further is essentially if you
[11:47] watched my last video about UV and basically creating blending morphs and stuff like that,
[11:54] we can blend some of these transformations that we've done and create multiple parallax
[11:59] planes using basically ROTOS.


### UV Coordinates for Parallax [12:00]
**Transcript (timestamped):**
[12:03] So if we create our little expression here, which creates the UV coordinate system, so
[12:10] you can go check that video.
[12:13] Basically I've basically just formatted it to our project size, which is 2K.
[12:17] I've cropped it outward to give a little bit of parallax and done the expression, which
[12:22] gives us this pattern and the expression is seen here.
[12:26] So if you're totally lost, I would really recommend you go check out those two videos.
[12:31] And essentially what you can do is we know closer objects will move more than once further
[12:41] away.
[12:42] If we just start with that concept, we can kind of go further.
[12:48] So let's take this picture.
[12:50] I'm just going to take the picture and restart it over here.
[12:54] Make a really simplified version.
[12:57] So essentially what I'm going to do is I'm just going to get a base scaling going on
[13:02] in our scene.
[13:03] So we can go here on this frame and set a keyframe at 1 and then go to our last keyframe
[13:08] and we'll set it to 1.09.
[13:11] So we get this kind of a push in.
[13:13] So if you watch it, it just looks like a 2D zoom at this point.
[13:18] So nothing spectacular.
[13:21] But if we start going on with our concept, we have this sort of UV coordinate system here
[13:31] and we'll copy our transform onto that and we'll call this one, we'll rename it and say
[13:37] far or let's just say most parallax.
[13:45] Most parallax and then we'll say medium parallax.
[13:49] Medium parallax.
[13:51] And so on the medium parallax one, we'll set the transform instead of 1.09, we'll set
[13:56] it to 1.05.
[13:59] And so we have these two.
[14:00] And essentially what we want to do is we want to have the most parallax areas be on
[14:04] the areas that are most close to us.
[14:06] So for example, this building.
[14:09] So I'm going to do a key mix, say A, B and then mask it.
[14:17] So the most parallax will appear through our alpha.
[14:21] And if I draw our roto, let me just close some of these here and we'll draw our roto
[14:27] shape here and then feather it off basically down the direction of the building.
[14:36] Something like this.
[14:38] I mean, we might need to adjust the shape.
[14:44] But and then what we're going to do is an ST map.
[14:46] So do ST map and we'll plug that into that key mix and plug this result into our image.
[14:55] Set the UB channels RGB.
[14:57] All right.
[14:58] And if we hit play, we could see starting to get some kind of interesting effect.
[15:03] If we look closely at this building, it's actually moving a little bit faster than the
[15:08] rest of our shot.
[15:10] And something we need to actually do is make this roto kind of stick to where it is so
[15:16] that it kind of moves with the shot.
[15:18] So if we copy our most parallax and we put it on our roto shape there and we check this
[15:25] out, now this will kind of stick a little bit with our building.
[15:30] So if we just take a look at that, what that is looking like, we can see that this is starting
[15:36] to move more like a 3D object, but everything else is still a little bit 2D kind of looking.
[15:43] So we're going to need to make a couple more parallax planes with this.
[15:50] So one way we can visualize this is I could just do a roto paint over it to help us understand
[15:56] exactly what we're doing.
[15:58] If you guys haven't already got it.
[16:02] If I just take this brush here and I'll write some numbers, I say, okay, so this is 1.09
[16:08] and then it's decreasing the further away we go.
[16:11] So we've done we've mixed 1.09 with 1.05.
[16:14] So right now everything else is 1.05 moving this much.
[16:20] But what we can do is we'll say, okay, we'll keep this building as 1.05.
[16:26] But we'll make this area back here.
[16:29] We'll say we'll draw another roto shape, something like this.
[16:34] We'll say this is 1.02.
[16:35] Let me draw it down here.
[16:38] 1.02.
[16:40] And we'll feather that off in different direction.
[16:44] And then we can draw ones that are really far away.
[16:46] So we'll draw another roto.
[16:49] I will say 1.01.
[16:53] So these things will move the least and probably back here as well will be 1.01.
[16:58] 1.01.
[17:00] And so that's kind of what we're doing with splitting this image into parallax planes with
[17:03] roto shapes, feathering them together, and then we're blurring or blending those transformations.
[17:09] So right now we only have 1.09, 1.05 using one single roto shape, which is here.
[17:17] But let's try continuing this.
[17:19] So I'm going to copy this one.
[17:20] I'm going to call it less parallax.
[17:22] I'm going to set the last key frame to, let's say, what do we say, 1.02.
[17:31] Less parallax.
[17:33] Plug it into there.
[17:35] And we'll key mix that over the top of it.
[17:37] So we'll say A over B. We'll put our roto shape here.
[17:44] And I'm going to make this one a little bit bigger.
[17:46] So we'll draw kind of a square, something like this.
[17:54] We might have to tweak it so we don't get too much blurring or anything like that.
[17:59] I'm also going to copy the animation to the roto shape.
[18:01] So it kind of sticks.
[18:04] And then we're going to feather it out.
[18:07] So we're going to feather this towards the camera.
[18:10] So feather and something like this.
[18:16] You can feather it and get this effect.
[18:21] So it's not a perfect effect, obviously.
[18:23] It might not pass QC on feature film or something.
[18:27] But eventually this shot is actually going to be out of focus.
[18:29] So I'll show you guys what this kind of will give us.
[18:33] But let's just see what that looks like now.
[18:35] So we have another plane of parallax.
[18:37] So this roto shape kind of sticking here.
[18:38] If we kind of look at it, it's starting to feel a bit more 3D.
[18:44] We have a little bit of stretching here, which we can reduce with some more blurring and
[18:48] feathering a little bit.
[18:49] But you see that it's starting to give us something much more interesting than just
[18:54] this 2D zoom we compare.
[18:57] Here's the parallax.
[18:59] And here's the 2D zoom.
[19:02] So I'm going to quickly just see if we can do something about this blurring here.
[19:06] It's not, like I said, it's not going to work 100% perfectly because of this specific technique
[19:11] and how it works.
[19:13] If you really wanted to make this QC proof, you'd have to split this into different layers
[19:18] and stuff like that.
[19:20] But for this tutorial, we won't do that.
[19:24] And I'm always considering level of detail, like I said.
[19:27] And this specific shot that I'm working on, I will show you guys, is much more out of
[19:33] focus so you won't be able to tell anyways.
[19:35] So let's just take a look at how that looks.
[19:41] So cleared a little bit of the stretching there.
[19:44] There's a little bit of stretching, but we could also blur it.
[19:50] We could kind of blur the building into it as well because the building is going away
[19:53] from us.
[19:54] So it would be okay to do that.
[19:56] And we're going to hide that stretching a little bit.
[20:03] So now I think it's starting to look pretty good.
[20:09] We could, I'm just going to pull that back just a little bit just to hide that.
[20:20] And that should work.
[20:22] And then we'll do one more plane.
[20:23] So we'll just say least parallax.
[20:27] We'll just least parallax.
[20:31] And then we'll key mix that over the top as well.
[20:34] So pull this down, pull this in A over B, same thing.
[20:39] Put this here, copy this here, put a roto shape, put the mask and take a look.
[20:46] And we'll just draw that roto shape in the very back areas.
[20:49] So we'll just draw back here and we'll feather that out in the areas that it would sort of
[20:56] be further away and then we'll pull it towards us.
[21:06] And I'll do the same over here.
[21:08] So I'm going to make it kind of this alleyway is going to be much further away and pull
[21:15] this towards us a little bit so that we have this fake parallax coming towards.
[21:22] And make sure that I've set my number.
[21:23] Did I set my number here?
[21:24] I'll set it to 1.01.
[21:28] Just make sure that that's updated.
[21:30] OK, so now if you take a look, we should have some pretty substantial parallax here.
[21:43] So we basically cheated this effect and we have different layers of parallax just from a 2D image.
[21:48] And looking pretty good.
[21:51] We have a little bit of stretching and stuff like that.
[21:53] But for this type of effect, that's to be expected.
[21:57] This effect will actually work really well on organic surfaces.
[22:01] So if you have less things overlapping like where we're having a little problem here, we could.
[22:10] That would probably not be as apparent on, you know, hills and stuff like that.
[22:15] So this could definitely work on something like that.
[22:20] Right. So that's pretty cool.
[22:21] And we have something that looks better than just a 2D zoom.
[22:25] And we didn't have to model anything.
[22:26] So this took, you know, a fraction of the time.
[22:29] And depending on your shot, you could probably get away with it.
[22:33] So one other thing we can do to make this a little bit more convincing is we have a lot of buildings here.
[22:38] And, you know, something I did for this specific shot was, you know, these reflections are here.
[22:44] And, you know, the traditional long, long way of doing it, if you really needed a very high quality would be, you know,
[22:50] replacing all these windows and doing a CG reflection, which is totally fine to do.
[22:54] And depending on what you're working on is a good approach.
[22:59] However, what I did just for the level of quality I needed was essentially one way of cheating it would be to basically just paint out the reflections.


### Fake Window Parallax (Simple) [23:00]
**Transcript (timestamped):**
[23:11] So I just did a roto paint before all this scene parallax stuff that we did.
[23:18] So I just do this beforehand, I paint out the reflections and minus it from the original image so we can have the reflections by themselves.
[23:26] And then we can just add a very slight transform and we can mask the reflections by the window frames.
[23:35] So as the picture will move, if we just look at it on a static image, it'll just look like these reflections are sliding horizontally and kind of slightly upwards.
[23:45] But if you kind of mask it behind the windows and different little surfaces, you can kind of give the illusion that these are reflections.
[23:52] So when the camera is actually moving, so if I look at the moving camera, once we have a moving camera, it's going to look like these reflections are moving with us.
[24:04] So that's just a pretty much an XY transform timed up a little bit with this push in.
[24:09] So if you look at the push in, we have these kind of fake reflections in the building, which kind of gives us a little bit more of a convincing result that we're flying through rather than just zooming into a picture.
[24:20] And so that's pretty much it for the effect.
[24:23] Some other things I did with this shot, it's not a final shot or anything.
[24:27] This is still very much work in progress for a different project.
[24:32] But this is something I just defocused as well, because there's going to be a character very much in the foreground.
[24:39] So it's going to rack focus onto this person.
[24:41] So as the camera goes on, it goes very out of focus like this, which really also helps with our parallax effect because you're any little stretching or anything like that.
[24:50] That's happening is very much not visible or not apparent if you're not looking for it.
[24:55] So in this case, it works pretty well.
[24:58] And you see that the parallax in the windows works pretty well because it brings some motion into the bouquets.


### Extra Tricks [25:00]
**Transcript (timestamped):**
[25:04] So it's making them flicker a little bit.
[25:05] They seem to be moving, which really gives us the impression that we're flying.
[25:10] Something else that they have this shot that's sort of unrelated to this specific tutorial, but maybe you guys are curious is if you just bring more motion into a still image like this.
[25:21] There's a couple of little tricks you can do, for example, you know, just running a noise pattern through some reflections to get them the water kind of looking like water.
[25:31] Another thing you can do is I kind of ran a animated noise pattern through the highlights.
[25:37] And when this is in focus, it looks pretty strange.
[25:40] But I was designing the shot for being out of focus.
[25:43] So if we actually look at what that's doing, if you take a luminance key.
[25:47] And essentially just ski our shot.
[25:51] So I wanted these cars to look like they're kind of moving without having to manually drive them and everything like that.
[25:56] You could use some particles or something as well.
[25:58] If you want to test some some cars driving down the highway.
[26:02] But in this instance, I just did a key of the highlights and I did a noise pattern, animated like this.
[26:10] And then just masking it through the highlights and using this alpha, I just basically brightened up the image.
[26:17] In various areas.
[26:18] And what that does through our defocus is it makes our bouquets kind of flicker.
[26:24] So you can you get this sort of glinting effect that things are moving.
[26:28] And you get this type of effect when a camera is moving through an environment.
[26:31] You're not going to get completely static bouquets everywhere because there's things that are being occluded and going behind objects and stuff like that.
[26:39] So you get this sort of glinting effect.
[26:41] And that's just a quick way to do it.
[26:44] And again, considering level of detail, you don't need to be scientific about everything necessarily as long as you're getting the impression that you want from the viewer.
[26:54] So that's basically it.
[26:55] Hopefully you guys enjoyed.
[26:56] And if you did hit the like button and subscribe if you're not already.
[27:00] And yeah, there'll be more on the way.



---

## Captured Frames

- [1:10] tutorials/frames/parallax-hax-nuke-compositing-advanced/frame_000.jpg
- [4:00] tutorials/frames/parallax-hax-nuke-compositing-advanced/frame_001.jpg
- [9:00] tutorials/frames/parallax-hax-nuke-compositing-advanced/frame_002.jpg
- [10:40] tutorials/frames/parallax-hax-nuke-compositing-advanced/frame_003.jpg
- [15:00] tutorials/frames/parallax-hax-nuke-compositing-advanced/frame_004.jpg
- [18:20] tutorials/frames/parallax-hax-nuke-compositing-advanced/frame_005.jpg
- [23:20] tutorials/frames/parallax-hax-nuke-compositing-advanced/frame_006.jpg
- [25:50] tutorials/frames/parallax-hax-nuke-compositing-advanced/frame_007.jpg

---

## Structured Notes

### Core Technique
Faking 3D parallax from a single flat 2D still image, entirely in 2D compositing — splitting the image into multiple depth "planes" via feathered roto shapes, animating each plane's `Transform` scale by a different multiplier of a single master push-in curve (via a self-referencing expression), and blending the planes together with `KeyMix`. No 3D projection, camera track, or geometry is used.

### Summary
A cheap, compositor's-shortcut alternative to true 3D-projection parallax: instead of projecting a still onto 3D geometry and moving a camera through it, this technique fakes the parallax purely with 2D transforms at different scale-animation speeds. The core insight is a "scale as multiplier" trick: keyframe a master `Transform`'s scale from 1 to some end value (e.g. 1.9) as the push-in curve, then give every other depth layer its own `Transform` whose scale is linked to the master via an expression that multiplies the master's *offset from 1* by a percentage — objects meant to feel closer get closer-to-100% of the master's motion, objects meant to feel farther get a smaller percentage, and background gets almost none. The video builds this up from a naive "just lower the end keyframe number by hand" version (works but requires manual guessing per object) to a proper self-normalizing expression (`1 - (master_scale.frame(startframe) - master_scale) * percent`, using a `frame()` lookup to fix the animated-variable self-reference bug) exposed as a single user-added "movement" slider knob (0–2 range) per layer, so relative speed becomes a single tunable number instead of mental math. Applied to a real cityscape push-in, the image is split into parallax "planes" using feathered roto shapes (closer buildings get a shape with more scale-multiplier, farther background less), each plane pair blended with `KeyMix` (A over B, masked by the roto), and an `STMap` is used to re-map/crop the source into a UV coordinate space beforehand (referencing an earlier UV-morphing video) to give extra room for the parallax crop. Roto shapes are keyframed/copy-animated along with their plane's transform so they visually stick to the moving geometry. The technique stacks 3-4 planes (most/medium/less/least parallax) to build up a convincing multi-depth push-in from one image, with stretching/warping artifacts at plane boundaries hidden via extra blur/feathering — acceptable because the target shot will be heavily defocused (rack focus) in the final composite, so imperfections aren't visible. Bonus techniques covered: faking sliding window reflections (roto-paint out real reflections, subtract to isolate them, animate a slight XY transform timed to the push-in, mask behind window shapes) for extra parallax-in-reflections realism, and faking distant motion/sparkle (animated noise pattern keyed through the highlights via a Luminance key, used as a mask to locally brighten areas) to make out-of-focus bokeh highlights flicker like moving traffic/lights without actually animating anything.

### Key Steps
1. Start from a single still image (a "2D zoom" baseline: one `Transform` with scale keyframed from 1 at the start to a push-in value like 1.09 at the end).
2. Duplicate the master `Transform` onto separate depth-plane copies, but instead of independently hand-tuning each end-keyframe value, link each copy's scale to the master via an expression.
3. Build the self-normalizing expression: `1 - (master.frame(startframe) - master) * movement`, where `movement` is a new user-added floating-point slider knob (min 0, max 2) exposed per layer via "Manage User Knobs" — this guarantees frame-1 scale is always exactly 1 (no snap/pop) regardless of the movement value, and `movement` above 1 makes the layer feel closer/faster, below 1 makes it feel farther/slower.
4. (Optional prerequisite, referenced from an earlier UV video) Build a UV-coordinate re-map with an `STMap` cropped outward to the working resolution (2K in this case), giving overscan room for the parallax crop before compositing planes together.
5. Draw a feathered `Roto` shape around the nearest depth element (e.g. a foreground building), feathered off in the direction depth recedes.
6. `KeyMix` (A over B) the "most parallax" transform layer over the base "medium parallax" layer, masked by that roto shape.
7. Copy the plane's `Transform` animation onto its roto shape as well, so the mask sticks to the moving geometry instead of staying static.
8. Repeat for additional depth planes (medium → less → least parallax), each with a progressively lower `movement` value, each masked in via its own roto shape and `KeyMix`, building up 3-4 total depth layers.
9. Clean up stretching/warping artifacts at plane boundaries with extra `Blur`/feathering on the roto masks — acceptable since the shot will be heavily out-of-focus in the final comp.
10. For fake window-reflection parallax: pre-pass a `RotoPaint` to paint out real window reflections from the plate, then subtract the painted-out version from the original to isolate the reflections as their own element; apply a slight independent XY `Transform` (timed to the main push-in) to that isolated reflection layer and mask it behind the window shapes so reflections appear to slide as the "camera" moves.
11. For fake distant motion/sparkle: key the highlights with a `Luminance key`, generate an animated procedural noise pattern, mask the noise through the highlight key's alpha, and use that to locally brighten small areas — creates a flickering/glinting bokeh effect that reads as distant moving lights/traffic once defocused, without animating any actual geometry.

### Nodes / Tools / Settings
- `Transform` — the core tool; per-plane scale animated (keyframe 1 → end value, or expression-linked to a master), the only "3D-feeling" driver in the whole technique
- Self-referencing expression on scale: `1 - (masterScale.frame(startFrame) - masterScale) * movement` — uses `.frame(N)` to sample the master curve's start value and avoid the animated-self-reference bug
- User knob: custom floating-point slider "movement" (min 0, max 2), added via Manage User Knobs, one per depth layer, drives relative parallax speed
- `Roto` — feathered depth-plane masks, animated/copy-linked to their layer's Transform so they track the moving image
- `KeyMix` — A-over-B blend of each depth-plane pair, masked by the corresponding roto shape
- `STMap` — UV-coordinate remap/crop step (built from an earlier tutorial's UV expression) giving overscan room before compositing planes
- `RotoPaint` — paints out real window reflections to isolate them as a separate element (subtract from original to extract)
- `Merge` (subtract) — isolates the painted-out reflection element from the original plate
- `Luminance key` / `Keyer` — isolates highlights for the noise-driven sparkle/flicker trick
- Procedural noise (animated) — masked through the highlight key alpha, used to locally brighten small regions for a flickering-bokeh effect
- `Blur` — extra feathering/blur at plane boundaries and on the receding building to hide stretching artifacts

### Difficulty
Advanced

### Foundry App & Version
Nuke (core toolset only — `Transform`, `Roto`, `KeyMix`, `STMap`, `RotoPaint`, `Merge`, `Keyer`/`Luminance key`, `Blur`, and user-knob expressions are all native; no third-party gizmos required). No on-screen version number visible in the captured frames and none stated in the transcript. Video published 2021 — falls in the Nuke 13.0 era (13.0 released 2021-03-17); see `references/version-tracker.md`.

### Tags
compositing, roto, rotopaint, st-map, channels, procedural-texture, grading, digital-matte-painting, advanced

---

## Related Tutorials
- [Nuke Tutorial | Keying with Math Expressions [Intermediate]](nuke-tutorial-keying-with-math-expressions-intermediate.md) — shares the self-referencing/user-knob expression-driven approach to building a reusable, tunable effect instead of manual per-shot values.
- [Nuke Compositing Tutorial: Integration Sketching](nuke-compositing-tutorial-integration-sketching.md) — shares the "level of detail" / good-enough-for-the-shot mindset explicitly argued in both videos (this one's stretching artifacts are acceptable because of an upcoming defocus, same pragmatic reasoning).
- [Compositing in UV space with Projections | Nuke [Advanced]](compositing-in-uv-space-with-projections-nuke-advanced.md) — shares the `st-map`/UV-coordinate-system technique this video explicitly references as a prerequisite ("go check that video").
- [UVs and UV Passes in Nuke: PART 1 [Beginner]](uvs-and-uv-passes-in-nuke-part-1-beginner.md) — covers the UV/`STMap` fundamentals this video assumes as prior knowledge.
