---
title: Shuffle and Channel Management | Nuke Compositing [Beginner / Intermediate]
source: YouTube
url: https://www.youtube.com/watch?v=giI8elFp4QQ
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "Nuke 12+ (new Shuffle node UI explicitly referenced; 2021 upload, Nuke 13.0 era — see version-tracker.md)"
tags: [compositing, channels, aovs, grading, digital-matte-painting, roto, rotopaint, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/shuffle-and-channel-management-nuke-compositing-beginner-intermediate/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Shuffle and Channel Management | Nuke Compositing [Beginner / Intermediate]

**Source:** [YouTube](https://www.youtube.com/watch?v=giI8elFp4QQ)
**Author:** Compositing Academy
**Duration:** 25m3s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to this video. This is just a visual explanation kind of going over the shuffle node, which I think a lot of beginners kind of starting out kind of struggle with.
[0:11] And probably for good reason, because if we look at the old shuffle node, it's super confusing, not intuitive.
[0:17] But I'm going to really kind of break down the new shuffle node and kind of put this to rest, hopefully.
[0:24] So we can go over this kind of visually, understand what this is actually doing, and hopefully get a better understanding of it.
[0:31] And then later on in the video, I'll go over some more intermediate uses of the shuffle node.
[0:37] So if you're not a beginner, you know, maybe you could skip past this part and maybe you'll get something out of this, potentially.
[0:43] So first I'll start off with just really the basics of it, and kind of what the shuffle node is used for.
[0:49] And so if you're being confused with this, hopefully this should help.
[0:52] So if we get to it here, I'll just quickly go over the basics of the Nuke interface again, which is here we have channel sets or layers.
[1:03] So again, in the EXR picture, we have multiple channels, channel sets that can be stored and accessed here.
[1:11] So for example, this car is not just this red, green, blue render of a car.
[1:17] We can actually hop into one of these layers and see different aspects.
[1:21] For example, if you want to see just a reflection layer, we can look at that and see just a reflection here.
[1:28] So that's this tab, the layer slash channel set.
[1:31] And we have this layer here, which is the specific color channel that we're looking at.
[1:37] So red, green, blue means it's combining the three of these.
[1:40] But if we hit red, green, or blue on our keyboard, RGB, we can see that that little tab up here is changing RGB.
[1:47] And we can go to alpha as well.
[1:49] And there's one more tab up here that is less commonly used, but it's still there.
[1:54] And this is the specific channel that is shown when you're looking at the alpha channel.
[2:02] So if that's confusing, it kind of is.
[2:05] But if you look at the alpha channel, we're looking at just the actual alpha of this car.
[2:09] But if you want to see something else in this alpha channel, so if you just want to quickly access it by hitting A on your keyboard,
[2:15] you can actually replace what you're seeing in that alpha channel by using this little box here.
[2:20] So maybe we want to actually see the depth of this car easily.
[2:24] So we can actually just switch it to depth.
[2:26] And if we go to the alpha channel, now we're not actually seeing the alpha, we're seeing the depth of the car.
[2:31] So if I take the gain and I slide it down and hit these little arrows here, we can actually see the depth of the car stored.
[2:41] It's not actually changing the channel.
[2:43] It's just seeing it's changing the channel that we're looking at in this here.
[2:48] So that's that's kind of confusing a little bit, but usually I just keep it on RGBA.alpha.
[2:52] Because when I hit the alpha on my keyboard, I want to actually see the alpha of the car.
[2:59] So if we continue on here, we just look at this.
[3:03] So this is our basic render.
[3:05] If we look at this here, so we have the RGB layer, which is made up of the three color channels.
[3:12] Like we've talked about probably a few times.
[3:15] But if we look at the first use of a shuffle node, so if I create a shuffle node at the top here,


### Shuffle Node [3:18]
**Transcript (timestamped):**
[3:21] I create a shuffle node.
[3:24] So this is our new Nuke 12 shuffle node.
[3:27] If I just look at what this is doing, essentially what's happening here is this node is passing through the color channels.
[3:36] So if we're looking at, if you look at it like this, we see that from the B input, so this B pipe, like our main information pipe,
[3:47] you're getting the red, green and blue channels.
[3:50] And these lines show what information is actually passing through the shuffle node.
[3:56] So the red is going into the red.
[3:59] So red is staying the same.
[4:01] Green is going to the green and blue is going to the blue.
[4:04] So because they're going into themselves, nothing's actually changing.
[4:07] This is actually just doing nothing right now.
[4:10] So if I go to the shuffle and I actually show you guys this in live, let me just make this bigger.
[4:19] So if I go to here, so I say I have the shuffle node here and I take the RGB red and I put it to this little black button.
[4:29] I can actually delete the red channel by doing this.
[4:31] So if I press this black button, you'll see the red channel actually disappears and the combined layer, the RGB combined layer is turning cyan
[4:40] because we only have the green and the blue channels remaining.
[4:44] So if I reconnect that red back into the red, we'll see we have our normal render.
[4:49] Again, I can do it with the green just to demonstrate further.
[4:52] So we have red and blue and that's mixing into purple because we don't have a green channel.
[4:58] Less commonly used, we could actually just disconnect all of these, just press zero on all of them.
[5:05] So this will make them empty and the white ones will make them solid white.
[5:09] But if we make them empty and I could put the blue channel into the red channel, so I can actually rearrange the color channels in a way that they weren't arranged before.
[5:19] And now you'll see that the taillights that used to be red are actually now blue because we've just rearranged the channels.
[5:26] They're not particularly useful, but it's just to demonstrate how this works.
[5:31] So normally we just drag it straight across like this and the alpha.
[5:39] So that's the way the actual node works, but the way it's used and most practical is that we can basically pull out layers.
[5:50] Again, our layers are stored here and we can bring them into their red, green and blue main layer that we work in.
[5:58] So this is the layer that we render out every time we save an image.
[6:01] We're rendering out the red, green and blue layer.
[6:04] So if I want to be able to adjust some of these layers that are stored in this picture and color grade them easily,
[6:10] what we want to do is pull one of these layers out.
[6:13] For example, let's say refraction.
[6:14] We want to take all the information in refraction and put it into the red, green and blue layer.
[6:19] So that's what the shuffle is actually used for.
[6:21] It's taking these layers and putting them into the red, green and blue layer so we can access them easily.
[6:26] So if I take the shuffle node and I just switch this little box here to refraction, you'll see that now our image changes.
[6:36] So our red, green and blue layer, which is originally just our car, is now replaced by the refraction layer.
[6:44] So if we look at this, we see it's pretty self-explanatory with that concept.
[6:49] So it says refraction red.
[6:50] So the red channel in the refraction layer is now replacing the red, green, blue dot red channel.
[6:58] So the refraction green channel is now replacing the red, green, blue green channel.
[7:03] So we're placing the color channels in the red, green and blue layer.
[7:07] Essentially, that's how it works.
[7:09] So we can shuffle all different layer.
[7:11] So we go refraction here if we switch it.
[7:15] And we'll see that now we have the refraction in this layer.
[7:18] And you'll be asking if you haven't done CG compositing before, I have a full course on CG compositing.
[7:25] But again, the reason we're pulling these layers out from their original saved position in this EXR file is because we want to easily color correct them and do stuff to them.
[7:37] So if we go back into the original comp for this shot, we can see we have all kinds of shuffle notes happening here.
[7:42] We have a reflection shuffle node, specular and specular indirect, and a bunch of different shuffle nodes pulling out different layers from that picture and putting them into the red, green and blue.
[7:54] And the reason we're doing that is we can easily color correct those layers and recombine them with those adjustments made.
[8:02] So for example, I just wanted to go to the reflection layer.
[8:07] I have it shuffled out here reflection into the red, green, blue.
[8:10] And I can go there and check on a color grade.
[8:14] I can crank up the reflection and make us a really reflective car.
[8:17] And then when we've combined them all back together using a plus merge, we can see that that adjustment is only being made on the reflection layer.
[8:28] So that's the real main use for shuffle.
[8:30] And I just wanted to explain a little bit deeper and more visual.
[8:34] So hopefully that kind of gets idea across there.
[8:37] So if anyone's confused, still hopefully that will clear it up.
[8:41] The other use for it.
[8:43] So that's the main use really is mostly used in CG composing.
[8:47] But the other use we have is sometimes I use it for if we have an image like this, we have this video taken in just a red, green, blue video.
[8:57] It doesn't come with an alpha because it's just a video.
[9:00] And if we were to want to mask this, like let's say we want to roto off this guy off the background and I took a roto note and I made a mask.
[9:09] You'll see that it's cutting out properly.
[9:12] So it's just cutting out the red, green, blue.
[9:14] But our video doesn't have an alpha.
[9:16] So if I go to the alpha channel, you'll see everything is just black.
[9:19] And if you merge this over another picture, you'll see that we get this kind of plus looking effect.
[9:24] And that basically means that Nuke doesn't understand what's supposed to be opaque and what's supposed to be transparent.
[9:30] And that's because our original video doesn't have an alpha.
[9:33] So a very simple solution.
[9:35] You just create a shuffle node and instead of it being like this, which is how it normally looks by default,
[9:41] you just press this little white button here and give it a solid alpha.
[9:45] So if you look at the alpha channel, I've hit disable on the shuffle node.
[9:48] You'll see that we're just getting a solid white channel there in the alpha channel.
[9:54] So we mask it off, merge it over and problem solved.
[9:58] So without the shuffle and with the shuffle, we see that it fixes that problem.
[10:03] Of course, that's one way of creating alpha.
[10:06] You could do it another way.
[10:08] You could do a roto with the output set the alpha and it will create an alpha for that.
[10:13] And you could pre multiply that and merge it over and that's going to give the same result.
[10:17] So those two things are exactly the same, but this does have a benefit knowing that you can create alpha channels.
[10:24] And occasionally you'll need to do that to create a solid alpha or delete an alpha, etc.
[10:30] So that's kind of how the that's relevant.
[10:34] So that's the basic uses and most common.
[10:37] So if you understand those two things, you're probably good to go.
[10:40] The more advanced or intermediate, I guess would be these situations.
[10:45] And essentially what we can do with the shuffle is we can carry channels down the pipe.
[10:53] So this is going to get a little bit more complicated, but hopefully we can keep it understandable here.
[10:58] So we have this video here.
[11:01] This is not exactly practical, but I just want to show you how it works.
[11:04] And then I'm going to show you an actual practical new script that I use this in.
[11:10] But I just want to show how it works first.
[11:12] So we have the basically just the video and we opened up the shuffle.
[11:17] Actually, let's just create a new shuffle.
[11:19] So let's say we want to shuffle this alpha into this picture that doesn't have an alpha.
[11:27] We could do that so we can create a shuffle node and plug it in.


### Create a Shuffle Node [11:28]
**Transcript (timestamped):**
[11:32] So we see that the B is being plugged in and we also have a little arrow here that's a so I can actually plug the A into here.
[11:40] And from this I can switch this second box down here into a and switch it to RGB.
[11:48] So right now, again, it's doing nothing because we see that the lines red is going to red, green, blue, alpha, they're all just going straight and connecting in.
[11:57] But instead I can switch it from this a box that we just created into this output layer.
[12:04] So if I take the alpha from the a layer, so I grab this and I put it into the output from the shuffle node into the alpha channel.
[12:13] You see if we look at the alpha channel now, we have the car alpha stored in there.
[12:18] So if I were to pre multiply this, we see that the car alpha is cutting out the picture.
[12:25] So you can also do this with a copy node.
[12:29] So you could copy an alpha to alpha.
[12:31] So just to show you, you can obviously do the same thing with this and pre multiply and you're going to get the same result.
[12:37] What's better with the shuffle node, especially the newer one is it's not just with alphas and it makes it much easier.
[12:45] So if we go to, let's say I want to copy the depth channel from this car.
[12:51] So I want to copy this layer.
[12:54] And if I gain down on this layer, we can see that the depth from the camera information is stored in here.
[13:01] So if I switch the a to depth, you'll see that it's automatically detecting that channel and that's stored in the layer with this, which is depth dot Z.
[13:11] And what I can do is I can store that in this output from the shuffle.
[13:18] So I go back to the red, green, blue while I'm doing this and just look at our original image.
[13:23] I'm going to switch the output layer to depth and I'm going to copy the depth from a from a into this output layer.
[13:32] And if we look at the shuffle, nothing is actually changing in the red, green, and blue because we haven't we haven't shuffled or changed anything in the red, green, blue output layer.
[13:43] So that's kind of what we're doing here.
[13:45] So we're just affecting only the depth.
[13:47] So if you look at the channel or sorry, the layer and go to the depth, we'll see that that's actually stored there now.
[13:54] So if I go further down this comp and I put my viewer here, you'll see that that information is being carried down the stream.
[14:02] So essentially what we can do and the reason we're doing this is because we can store channels or layers in this B pipe.
[14:12] And we can bring them down all the way and use them later on in the comp.
[14:17] And if you're doing a pretty small comp or you know you're not doing more complex stuff yet, again, this is more intermediate.
[14:23] It might not be relevant to you yet, but eventually it will be.
[14:27] And that's why we're talking about this.
[14:29] So now that that is stored in there, let's go back to our red, green, blue.
[14:35] So we have this picture.
[14:37] We have this information that's hidden, but it's stored in this information pipe that we've created.
[14:43] If we want to get that information back out into the red, green, and blue, we can actually do that.
[14:48] So we put another shuffle at the end here.
[14:50] And I'll just create a fresh one.
[14:53] So I'll create a new shuffle, plug it in here, and then I will shuffle the depth into the Alpha channel.
[15:03] Just to see if that information is carried.
[15:05] So we look at this.
[15:07] Now we look at the Alpha.
[15:08] If we gain down, we can actually see that yes, in fact, we've copied that and now it's in the, we've moved that information into the Alpha channel.
[15:18] So that's pretty cool.
[15:20] So we can kind of copy those channels, bring them down through the comp without having to take this thing, paste it down here,
[15:27] and then shuffle out the depth and do all of that.
[15:32] Any time we need that depth channel, we can basically just grab it and pull it out of the comp, out of the stream, whenever we want.
[15:41] So that's kind of one use, and that's not exactly practical.
[15:45] I'll show you practical use of this in a second here.
[15:49] This is another example doing the same exact thing.
[15:52] A little bit more practical because this would actually be kind of useful and sometimes they'll do this in productions.
[15:58] So we have our original video here and I've de-grained it.
[16:04] So kind of a de-noise version of this footage.
[16:07] And what I've done is, what I want to do is shuffle this de-grained version into its own hidden channel in here.
[16:19] So whenever I need the de-noise version of the footage, I don't have to keep de-noising it.
[16:23] I don't have to keep going up to the top of my composite and grabbing these and pasting them.
[16:27] I'll have it stored in this information pipe whenever I need it.
[16:32] So essentially what we can do here is we go to the shuffle.
[16:35] This is the default.
[16:38] I'm going to do the output layer.
[16:40] I'm going to create a new layer.
[16:42] I'm going to say de-noise.
[16:44] And then I'm just going to hit this little button here and it will create the channels to fill that layer and hit OK.
[16:50] And from the A input, I'll switch it to red, green, blue, alpha.
[16:55] And now what I'm going to do is just drag this box into here.
[17:00] So now what we've done is, if we look at our RGBA, it's still the same.
[17:06] But if we switch to the de-noise channel that we just created, we'll see that if I zoom in real close here,
[17:13] we're storing that de-noised version of our footage in this information stream.
[17:21] So now if we want to do a projection or something later on, like for example, I'm later on down my comp.
[17:26] I've been working on this comp for a while and if this comp was really big, for example, we just extended it way down.
[17:32] I've done a bunch of stuff, but hey, I want to go in here and paint out some of these little rocks.
[17:37] As we know, we want to work on the de-grained or de-noised version of the shot.
[17:42] So what I can do is put a new shuffle node here.
[17:47] Let's put a shuffle and plug it in.
[17:54] And I'll switch this out to the de-noised channel that we created.
[18:00] And now we see, if we zoom in here, make sure I'm looking at the RGBA channel.
[18:08] And so when I pull that out, we can see that I'm getting the version without the grain.
[18:14] So essentially I'm pulling out that version. Now I can do my clean plate.
[18:18] So I would do a frame hold. Maybe I'll do my, let's do it on the frame I'm on.
[18:23] So on frame 84.
[18:26] So now that we're looking at the de-noised version, we've pulled it out into the red, green, blue alpha layer.
[18:35] I could do some clean plating here and just paint out whatever I need to paint out.
[18:41] And then you could add your grain back on top.
[18:45] I'm just going to put a simple grain node here for now. I'm not going to match it perfectly.
[18:50] And then you would merge this back over. So I guess you could...
[18:57] Let's just make sure here.
[19:00] So I'll switch this to Alpamask RGBA.alpha.
[19:05] So I'm creating an alpha with my brush strokes. That's a little trick here.
[19:08] If you guys don't know it, there's a little arrow here.
[19:11] And you can say AlpamaskRGBA.alpha on the Rotopaint.
[19:15] And we can pre-multiply this.
[19:19] So now we've de-grained, done our painting, and we've...
[19:24] Now we can merge this back over our original image.
[19:27] And if this video is moving, we're obviously going to need to have a camera and other stuff to make this stick.
[19:34] But that's the concept. You can see how this is useful.
[19:37] Because whenever we need the Denoise, we can just shuffle it right back out.
[19:40] And I can just keep doing that over and over. Every time I need that Denoise footage, I can do that little shuffle trick here.
[19:46] And just copy it instead of copying different setups from the top.
[19:53] Especially if you're doing keys and stuff like that, that's going to be useful to have a Denoise stored in your information pipe whenever you need it.
[20:02] So one last example of this, another practical example.
[20:06] This is probably the most complicated example.
[20:09] It's exactly the same thing we're doing here.
[20:11] So essentially I have this little sign here that's behind and occluded by a bunch of wires.
[20:18] So this is available in my Nuke 404 class, which again, all the stuff is available in the description below.
[20:24] But essentially, yeah, we have a sign that's kind of occluded by a bunch of wires.
[20:29] And there's some lights that go around the rim of this sign.
[20:35] So I actually use a little bit of this channel management to be able to do this effect more easily.
[20:41] So essentially, let's just look at how it's made.
[20:43] So if I look at how it's made, we just have a simple constant.
[20:47] I've done a little roto here, just a little, a tiny little line, and I'm masking out a checkerboard.
[20:53] So you see that we get this little checkered pattern here.
[20:56] And I've kind of just duplicated it and made like a frame.
[20:59] And what these are are kind of little light bulbs that are kind of around the sign.
[21:03] So I've made them yellow and done all that.
[21:07] So that's kind of the frame of the sign.
[21:09] And what I've done here is I put a shuffle node.
[21:12] So this is where we're doing this kind of storing the information and pulling it back out later.
[21:17] So I've taken the red channel, just one of these channels that I've created.
[21:22] And I've created, actually, no, I've taken all the channels here, it looks like.
[21:25] I basically put them into a new channel called strip lights.
[21:30] So I just went to new, I said strip lights.
[21:33] And then I basically created this and I hit OK.
[21:37] And then I just take the normal colors of this layer and store them into this new layer.
[21:43] And okay, so I plus it over like normal.
[21:47] So again, we're looking at the red, green, blue, like basically normal composite right now.
[21:52] But we have this in the background.
[21:54] So if I'm looking at this, this merge node, and if I switch to the layer, I see that that new layer stored in here.
[22:03] So if I ever need to just access the light bulbs of this comp, I can switch to the strip lights layer.
[22:08] And you see that I have access to them right there.
[22:11] So we go down in the comp, we go further.
[22:14] I've added some stuff, some text on that sign.
[22:17] And I've kind of masked that out.
[22:20] And then I've stenciled it by these wires.
[22:24] So I have an alpha of the wires that are in front of this kind of sign here.
[22:31] So this is the original picture.
[22:32] We have all these crazy wires.
[22:34] And so I've basically made an alpha of that stenciled out from the red, green, and blue picture.
[22:41] But I've also got second stencil here, which is a channel merge.


### Channel Merge [22:44]
**Transcript (timestamped):**
[22:46] So we can see that using the channel merge node, I've taken the channel of the RGBA.alpha and I've stenciled it from the strip lights.alpha.
[23:00] And I've outputted a new strip lights.alpha.
[23:03] So if I look at the strip lights layer and hit the alpha channel, you see what this is doing is also stenciling it out by those wires.
[23:11] So now I have that layer stored and whenever I need to just color correct or do something with the light bulbs, I have that stored in this hidden layer here.
[23:20] And I've used that channel merge to make sure that that's being affected also by the wires.
[23:26] So if we go back to the RGBA, the normal picture, and we merge it over, okay, fine.
[23:31] So we haven't done anything.
[23:32] We haven't done anything with that strip lights layer yet.
[23:37] However, you can see I've broken this down into its own little section here and I've used that shuffle.
[23:43] So here I'm pulling out that strip lights layer and I'm pre multiplying it.
[23:48] So I'm just getting the strip lights with the wires, including it.
[23:51] So this is why this is useful because if I didn't use shuffles in this instance, I would have had to go up here and copy this entire portion of the script.
[24:02] And I would have had to paste it and also mask it by this, these wires.
[24:09] So I would have had to do something like this in order to get the same kind of thing.
[24:13] You know, I would have had to do some complicated or copied setup that's much bigger.
[24:17] But by using the shuffles, I didn't have to do that.
[24:20] So I shuffle it back out, pre multiply it and now I can glow those light bulbs and plus them over the top.
[24:26] So you see that we're only affecting those yellow lights that are around the frame and they're included properly by the wires.
[24:34] And we're also adding a little bit of glint to those as well.
[24:38] And that's just one way to use channel management, I guess, layer shuffling downstream of information.
[24:48] So that's one example and hopefully that's kind of useful to you guys.
[24:52] Hopefully you guys can understand shuffle a bit more now.
[24:55] And if you found this video useful, as always, hit the like button and subscribe.
[24:59] It really helps the channel and thanks so much.



---

## Captured Frames

- [1:15] tutorials/frames/shuffle-and-channel-management-nuke-compositing-beginner-intermediate/frame_000.jpg
- [3:50] tutorials/frames/shuffle-and-channel-management-nuke-compositing-beginner-intermediate/frame_001.jpg
- [4:35] tutorials/frames/shuffle-and-channel-management-nuke-compositing-beginner-intermediate/frame_002.jpg
- [6:30] tutorials/frames/shuffle-and-channel-management-nuke-compositing-beginner-intermediate/frame_003.jpg
- [8:10] tutorials/frames/shuffle-and-channel-management-nuke-compositing-beginner-intermediate/frame_004.jpg
- [9:15] tutorials/frames/shuffle-and-channel-management-nuke-compositing-beginner-intermediate/frame_005.jpg
- [13:00] tutorials/frames/shuffle-and-channel-management-nuke-compositing-beginner-intermediate/frame_006.jpg
- [21:15] tutorials/frames/shuffle-and-channel-management-nuke-compositing-beginner-intermediate/frame_007.jpg

---

## Structured Notes

### Core Technique
A visual, from-first-principles explanation of the (new-style, Nuke 12+) `Shuffle` node: what layers/channel sets are, how Shuffle routes individual color channels between input pipes and the output RGBA layer, and — the intermediate payoff — how to use Shuffle (and `Copy`) to "carry" arbitrary extra channels (depth, a denoised plate, a custom layer) silently down through a comp's B-pipe for later retrieval, instead of re-copying whole node chains.

### Summary
Opens with Nuke interface fundamentals for true beginners: a rendered EXR isn't just RGB — it stores multiple "layers"/channel sets (reflection, refraction, depth, specular, etc.) accessible via the layer dropdown, plus a separate, less-obvious "alpha channel" sub-selector that lets the alpha slot display a different stored channel (e.g. depth) without altering the actual alpha data — a common beginner confusion point the video explicitly untangles. Demonstrates the `Shuffle` node's core mechanic with its line-diagram UI: by default every channel passes straight through to itself (a no-op); clicking a channel's black button disconnects/deletes it (e.g. removing red turns the image cyan); channels can be deliberately cross-wired (e.g. blue into red) to scramble colors, purely to prove how the routing works. The main practical use in CG compositing: pull a stored EXR layer (e.g. "refraction") into the main RGB output layer via Shuffle's second/"A" input and per-channel output picker, so it can be graded directly — real production comps stack many such Shuffles (reflection, specular, specular indirect, etc.), each isolating one AOV for independent color correction before recombining everything with a `Merge` (plus/add operation). A second beginner use: fixing footage that has no real alpha channel (plain video, no CG render) — a naive `Roto` mask over such footage merges incorrectly (a "plus"-looking double-image artifact) because Nuke has no opacity information; the fix is a `Shuffle` with its alpha button set to solid/white, giving the plate a constant alpha of 1 so subsequent roto/premult/merge behaves correctly (equivalent to a Roto node with alpha output + Premult, but demonstrating that Shuffle itself can manufacture alpha channels). The intermediate section covers "carrying channels down the pipe": a `Shuffle` can copy any channel (e.g. a depth channel, `depth.Z`) from a secondary "A" input into a new/custom output layer of the main B-pipe stream, without altering the visible RGB image at that point in the script — the data rides along silently and can be pulled back out with a second `Shuffle` later downstream, whenever needed, without re-fetching or re-copying earlier node chains. Two practical applications: (1) storing a de-grained/denoised version of a plate in a hidden custom layer (e.g. named "denoise") early in the script, so any later clean-plate/paint work can pull the denoised version back out via Shuffle, work on it, then merge the result back over the original — avoiding repeated denoise operations or copy-pasted setups; (2) a more complex real-shot example (a sign with light-bulb trim occluded by foreground wires): a custom "strip lights" layer is built from a roto'd checkerboard/light pattern, stored via Shuffle into its own hidden layer, then correctly matted by the wires' alpha using a `ChannelMerge` (stencil operation) which writes the result into `striplights.alpha` — later in the script that fully-prepped hidden layer is shuffled back out, premultiplied, glowed, and plussed over the final comp, avoiding a large duplicated/re-masked copy of the earlier node chain.

### Key Steps
1. Understand layer/channel-set fundamentals: a rendered EXR stores multiple named layers (color, reflection, refraction, depth, specular, etc.), selectable via the viewer's layer dropdown; a separate sub-selector controls what's actually displayed when viewing the "alpha channel" slot (can show something other than true alpha, e.g. depth, without changing the underlying data).
2. Create a `Shuffle` node and observe its default line-diagram: red→red, green→green, blue→blue, alpha→alpha — a complete no-op until channels are rewired.
3. Delete a channel by clicking its black disconnect button (e.g. remove red → image reads cyan); reconnect to restore.
4. Cross-wire channels (e.g. blue into red's output slot) to scramble/rearrange colors — demonstrates routing but isn't typically useful on its own.
5. For the main CG-compositing use case: on the Shuffle's "A" input dropdown, select a stored EXR layer (e.g. "refraction"); the output RGB then displays that layer's red/green/blue instead of the original beauty render.
6. Grade the isolated layer independently (e.g. boost a reflection layer's intensity with a `Grade`), then recombine all the separately-graded layer-shuffles with a `Merge` set to Plus/Add — each layer's correction only affects that layer's contribution to the final image.
7. For footage lacking a real alpha (plain video, not CG): add a `Shuffle`, set its alpha output to the solid/white toggle instead of passing through the (nonexistent) source alpha — gives the plate a constant, correct alpha of 1 so downstream `Roto`/`Premult`/`Merge` composites cleanly instead of producing a double-image "plus" artifact.
8. To carry a channel downstream: add a `Shuffle`, plug the source footage into its "A" input, select the desired channel/layer on the A side (e.g. `depth.Z`), create/select a custom output layer name (Nuke will auto-generate the required channels for a new layer name), and drag that channel into the corresponding output slot — the main RGBA output is left untouched, but the extra data now rides invisibly in the stream.
9. Retrieve a carried channel later in the script with a second `Shuffle`: select the custom layer on its "A" input and route it into whatever output channel is needed (e.g. back into Alpha, or into RGB for viewing/editing).
10. Practical pattern — hidden denoised plate: shuffle a denoised/de-grained version of the footage into a custom layer (e.g. "denoise") early in the comp; anywhere later that the clean version is needed (clean-plating, painting, keying), shuffle it back out, do the work (e.g. `RotoPaint` with alpha driven from brush strokes via "AlphaMaskRGBA.alpha", `Premult`), then `Merge` the result back over the main image — regrain afterward to match if needed.
11. Practical pattern — occluded element isolation: build a custom element (e.g. a roto'd light-strip pattern) in its own hidden layer via Shuffle; use `ChannelMerge` (a stencil/matte operation) to correctly occlude that hidden layer's alpha by a foreground element's own alpha (e.g. wires in front of a sign), writing the result back into that custom layer's alpha; later, shuffle the fully-matted hidden layer back out, premultiply, add a glow, and `Merge` (plus) it into the final comp — avoids duplicating and re-masking a large chunk of the earlier script.

### Nodes / Tools / Settings
- `Shuffle` (new-style, Nuke 12+) — core node throughout; per-channel line-diagram routing between input(s) and output RGBA; black button disconnects/deletes a channel, white button forces solid/constant value; second "A" input lets a different layer/channel set be selected and routed into the output alongside/instead of the primary "B" input
- Layer/channel-set dropdown (viewer + node "layer" knobs) — selects which stored EXR layer is being viewed or operated on (reflection, refraction, depth, specular, custom layers, etc.)
- Alpha-channel display sub-selector — lets the viewer's alpha slot show an arbitrary stored channel (e.g. depth) for inspection without altering the real alpha data
- `Grade` — used per-isolated-layer to color-correct a single AOV (e.g. reflection) independently after it's been shuffled into RGB
- `Merge` (Plus/Add) — recombines independently-graded layer-shuffles back into the final composite
- `Roto` / `RotoPaint` — mask/paint source; alpha can be explicitly set to "AlphaMaskRGBA.alpha" to drive alpha from brush strokes; used with a shuffled-out denoised plate for clean-plating
- `Premult` — standard premultiply step after manufacturing or restoring an alpha channel
- `ChannelMerge` — used as a stencil operation to matte one hidden custom layer's alpha by another element's alpha (e.g. occluding wires), writing the result into the custom layer
- `Copy` — mentioned as an alternative to Shuffle for simple single-channel copies (e.g. alpha to alpha), though Shuffle is preferred for its broader layer-management flexibility
- Custom output layers — created via the Shuffle's "new layer" option (auto-generates the required channel set for a given layer name, e.g. "denoise" or "striplights")

### Difficulty
Beginner (channel/layer fundamentals, basic Shuffle routing, alpha-fixing) progressing to Intermediate (carrying channels downstream, hidden-layer production patterns)

### Foundry App & Version
Nuke (native `Shuffle`, `Grade`, `Merge`, `Roto`/`RotoPaint`, `Premult`, `ChannelMerge`, `Copy` — no third-party gizmos). Explicitly references "the new Nuke 12 shuffle node" as the one being taught (vs. an older, more confusing Shuffle UI in earlier versions). Video published 2021 — falls in the Nuke 13.0 era (13.0 released 2021-03-17); see `references/version-tracker.md`.

### Tags
compositing, channels, aovs, grading, digital-matte-painting, roto, rotopaint, beginner, intermediate

---

## Related Tutorials
- [Nuke Tutorial | Keying with Math Expressions [Intermediate]](nuke-tutorial-keying-with-math-expressions-intermediate.md) — shares the channel-math/expression fundamentals theme, working directly with individual RGBA channels rather than stock tools.
- [Create 3D Noise | Nuke Compositing](create-3d-noise-nuke-compositing.md) — shares `channels`/`aovs`; both pull position/utility-pass channels out of a CG render's stored layers to drive further comp work, the same layer-access fundamentals this video explains.
- [360 Spherical LatLong Textures | Nuke Tutorial](360-spherical-latlong-textures-nuke-tutorial.md) — shares `compositing`, `digital-matte-painting`; both are toolset/fundamentals-style explainer videos aimed at demystifying a commonly-misunderstood Nuke concept.
- [Nuke Compositing an Advanced CG Shockwave | VFX (LookDev)](nuke-compositing-an-advanced-cg-shockwave-vfx-lookdev.md) — shares `channels`, `aovs`; that video's deep-compositing/AOV-heavy workflow depends on exactly the layer-shuffling fundamentals taught here.
- [Compositing with EXR Files | FREE VFX Explosions](compositing-with-exr-files-free-vfx-explosions.md) — directly relevant: a full applied walkthrough of Shuffle/AOV fundamentals on a real multi-pass explosion render, validating the recombined result against the original beauty before grading.
