---
title: After Effects to Nuke:  1 Hour FREE Course | Compositing in Nuke
source: YouTube
url: https://www.youtube.com/watch?v=pyiyfadan6c
author: Compositing Academy
ingested: 2026-08-17
app: Nuke
version: unspecified
tags: [nodes-vs-layers, roto, masking, merge-operations, grading, node-cloning, keyer, glow, particles-generator, chromatic-aberration, lens-distortion, grain, write-node, compositing, beginner]
extraction_status: complete
frames_dir: tutorials/frames/after-effects-to-nuke-1-hour-free-course-compositing-in-nuke/
frame_count: 12
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# After Effects to Nuke:  1 Hour FREE Course | Compositing in Nuke

**Source:** [YouTube](https://www.youtube.com/watch?v=pyiyfadan6c)
**Author:** Compositing Academy
**Duration:** 71m27s | 34 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] If your goal is to step up from short films up to feature film level visual effects, then stick around for this video because this video is designed for you.
[0:07] If you're like me starting out in visual effects, you're probably an After Effects user. You've probably done some Andrew Kramer tutorials, the OG, and maybe some of your own short films.
[0:15] This is where I started in visual effects as well, but if you want to go professionally, you have to transition to Nuke.
[0:19] When I was younger, I was always going out and shooting films with my friends. The process of coming up and shooting a story, filming, and adding visual effects.
[0:25] I had a green screen out of hang on the back of a garage, key it out and add some effects, or enter small competitions.
[0:30] At the time, I didn't even know what the term compositor was. However, once I learned about Nuke, I was hooked once I saw the potential.
[0:36] So this is a clip from way back in high school, a little short film with lightsabers on After Effects and then a shot I did on the rise with Skywalker with Nuke.
[0:44] So this video is aimed towards my prior self, people out there who want to transition from After Effects and work on feature films.


### The Project [0:49]
**Transcript (timestamped):**
[0:49] So if you stick around for this tutorial, this will be the first shot that we comp in Nuke.
[0:53] We're just going to be working with still images here, so I'm going to give you guys a few images to work with.
[0:57] We'll start to see how this node-based workflow is actually working.
[1:02] I'll compare it against After Effects and show you guys how we can take a very basic composite that isn't really finalized.
[1:08] Then we can kind of add those creative adjustments to get something that looks a bit more polished.
[1:14] So the first thing you're going to want to do is download Nuke Non-Commercial.


### Downloading Nuke [1:15]
**Transcript (timestamped):**
[1:17] It is free for non-commercial use. You can use it for all your personal projects, your demo reel.
[1:22] It's a pretty good deal and there's very few limitations. You can render up to HD and there's no problem.
[1:27] So the link for that is in the description and you'll want to make sure you launch Nuke X.
[1:31] It comes with two versions when you download it and one says X on it.
[1:34] It just has all the features when you launch the X versus the non-X version.
[1:37] So that's all you really need to know. So just make sure you launch that when you start.
[1:40] So if you download the project file zip that's included in the description as well,
[1:44] you'll get a few images here that you can drag into After Effects the way you normally start in After Effects.
[1:49] So I'm just going to compare the two interfaces real quick and then we'll kind of explain more of the Nuke's interface after that.
[1:54] So we'll make some comparisons along the way just so you can transfer your knowledge really quickly.
[1:58] But in After Effects, if we start here, the normal you have your images on your sort of media project file over here
[2:05] and when you drag one in, it will create a new composition.
[2:07] And when you create a composition in the composition settings, you see it's automatically grabbing the format.


### Nuke [2:10]
**Transcript (timestamped):**
[2:12] So Nuke is a little bit different. If we open up Nuke, this is what it's going to look like.
[2:16] And if we drag it in an image the same way we just in After Effects, we can take an image and just drag it in.
[2:21] And we get a little node down here, which is a read node.
[2:24] Now by default, we don't see anything. So what you actually have to do is click the node and hit one on your keyboard.
[2:29] And this is going to create a yellow line and there's this little node here called viewer.
[2:34] So if I just move it up here so I can see it, we see this little viewer node.
[2:39] And the way you can navigate this little node graph is by holding your middle mouse on your keyboard
[2:43] and you can click and drag these nodes around and you'll see this connection.
[2:47] So whatever this viewer is connected to is what we're going to see in our window here.
[2:51] So that's a bit different than After Effects whenever you just put all your toggles on your visibility layers, which are these eyeballs here.
[2:58] It's kind of like that in Nuke, but whenever we want to turn something off,
[3:02] we just look at the layer we want to look at.
[3:04] So we'll just grab another image here. We'll go here, we'll grab the soldier image and we'll bring it in.
[3:09] And then we have two images. So if we select the other one and we hit one, we'll see we're looking at that image now.
[3:14] So we can swap between the two by hitting one. You can also hit one and then click on this one hit two.
[3:20] So you can hit one and two on your keyboard and switch between them easily.
[3:23] So that's kind of useful if you're working at different parts of your composite.
[3:26] So in After Effects, if we were to do the same thing, we can bring in our guy, we can put it on top.


### Layers VS Nodes [3:27]
**Transcript (timestamped):**
[3:31] And automatically they start being layered together.
[3:34] In Nuke, it's a little bit different. This is where people start to get tripped up in Nuke.
[3:38] There's two places that people start to get confused and overwhelmed right away.
[3:41] And it's actually really not as complicated as it seems, but it's just something that coming from After Effects, you don't understand the purpose of why it's doing this.
[3:49] So if we want to merge this guy over this background, we just need to do a merge node.
[3:53] But there's one extra node that we have to do and we're going to explain it just a second.
[3:57] But if we just click this and we hit M, we can say merge and then we would say A over B.
[4:02] So we work from top to bottom in Nuke. We don't work bottom up.
[4:07] So here the bottom layer would be the background and we work upwards. It's just opposite in Nuke.
[4:12] And so the way you can think of it is each one of these images coming in, A over B is a new layer.
[4:19] So you could have many layers. If I just select these and hit Ctrl C, Ctrl V, it's going to be built out like this.
[4:25] So we'll always be going down. You'll always see that your B pipe is pointing down.
[4:29] You'll see these layers coming in over and it's kind of like a painting.
[4:33] So background to foreground, the same as After Effects, except we're just working in a tree.
[4:37] Now the only thing is where people get tripped up here is if you view this node.
[4:43] So we hit 1 again to look at the node that we want to see.
[4:46] You'll see that we're not actually seeing this guy over the background.
[4:50] And this is a PNG. So it does have an alpha, but Nuke doesn't automatically apply the alpha to the image in some cases.
[4:57] And this is where people get confused and they're like, it's a PNG. It has an alpha. Why is it not just merging over like After Effects?
[5:04] There's one node you have to put and it's called pre-mult. So if you hit Tab on your keyboard and you type pre-mult,


### Premult [5:07]
**Transcript (timestamped):**
[5:10] that's how you can get a pre-mult node and that will automatically make this work.
[5:14] So essentially what's happening if we just compare the idea to Photoshop real quickly is the same as in Photoshop.
[5:21] If you have an image and you want to apply like a mask, we can create a little mask layer here.
[5:26] You see that there's an alpha, but it's separated from the RGB.
[5:29] So there's the colors of the image and then there's an alpha of the image.
[5:32] And it's really important to always think of these things as two different things.
[5:36] And all that pre-mult node does is apply the stored alpha in the image.
[5:41] So if we look at the image and we hover our mouse over the viewer and hit A,
[5:46] we can actually see that there's an alpha stored in the image.
[5:49] And so it's just taking that and multiplying that against the colors of the image.
[5:53] In other words, it's applying the cutout just as it did in Photoshop we just saw.
[5:58] So After Effects automatically does that and Nuke it doesn't.
[6:01] And later on, that's actually really, really useful that it doesn't do that,
[6:05] but we don't need to talk about it really in this tutorial since this is a beginner tutorial.
[6:09] So before we continue further, I'm just going to explain the layout a little bit more


### Interface [6:13]
**Transcript (timestamped):**
[6:13] and we'll also compare to After Effects to see where the similar effects will be and those type of things.
[6:19] So over here on the right side is your properties panel.
[6:23] And this allows you to control different effects and different nodes.
[6:26] So if you want to create a node, again, we kind of did it real quick,
[6:29] but if you click down here and hit Tab and you type something,
[6:33] it'll open this window and you can access all your nodes here.
[6:36] So there's a lot of nodes that we'll use and it's good to like start to memorize them,
[6:40] but you also have this panel over here where you can access them.
[6:43] So these are all the nodes that you can use in Nuke and you can click in here and find them.
[6:47] A lot of them you're not going to know what to do at the start.
[6:50] So we'll just talk about a few by typing them.
[6:52] So we hit Tab and we'll say Blur and then we can create a blur node.
[6:56] And so the control for the blur node would be here.
[6:59] And if we take the blur and we plug it into the layer or sorry, the image, we can view it.
[7:04] So we want to make sure we're viewing it.
[7:06] If we're not viewing it, we're not going to see anything happen.
[7:08] So make sure we click it and hit one and then we can just start to increase that.
[7:11] And you'll see that the image starts to get blurred.
[7:14] And you see that I've put it off to the side here.
[7:16] So we can have different composites going in different directions here,
[7:19] which is what's interesting about Nuke.
[7:20] And you'll see how that becomes really beneficial later on.
[7:23] But if we view here, we had this blurred image.
[7:26] If we view here, we just have our normal composite.
[7:28] So to go over a few other just quick shortcut keys and things you'll need to know,
[7:33] we have up here some sliders.
[7:35] This will kind of adjust your viewer brightness.
[7:37] So it's not going to permanently affect the image.
[7:39] It's just if we want to kind of brighten it to see some details like maybe we're working in the shadow area, for example.
[7:45] This is the gamma control.
[7:46] So gamma and gain are a little bit different.
[7:49] This is gain and this is gamma, this one right here.
[7:52] And you see that when we bring this one up, it looks a little bit foggier.
[7:55] It's a little bit different.
[7:56] And if we bring it down, it gets more contrast.
[7:58] And so we'll explain that later on in some more advanced tutorials if you're interested in, you know,
[8:02] the actual curves and why that's doing that behavior.
[8:06] But just to know that those are there is brightness and gamma, which looks a little bit different.
[8:13] So also you can move around by holding middle mouse drag by zooming in and out.
[8:17] So you can hold middle mouse and you can zoom in with the mouse or you can click and click your middle mouse in and drag it around like that.
[8:24] You can also hit F on your keyboard to frame up your shot.
[8:28] So we're not going to have to use Z or any shortcut key like that in After Effects.
[8:32] We can just use them in a mouse a little time.
[8:34] The other thing I did here, I just brought in a video file.
[8:36] If you have a video file, you can just drag it in.
[8:39] This is an image sequence actually, but if I view this and then hit F by holding my mouse over to frame it up,
[8:46] you can see there's some video of embers here.
[8:49] This, if we drag on this timeline, that's how you play.
[8:52] So it's a little bit different than After Effects where it's sort of a timeline.
[8:56] This is just showing the frame number and if we switch the input, it'll switch to the frame range of the video.


### Project Settings [9:00]
**Transcript (timestamped):**
[9:03] And if we switch to global, it'll switch to the project settings of the frame range.
[9:08] And if you want to access your project settings to set the frame range or the resolution,
[9:12] you know, for example, in After Effects when we create a new composite in the composition settings,
[9:17] you see it's automatically grabbing the width and height of the image that we dragged in.
[9:21] And Nuke is not doing that. So if we go here and we hover over the mouse, sorry, the no-graph area and we hit S,
[9:28] that will access your project settings.
[9:32] And, you know, we'll want to make sure that we're working the format that the image is set to.
[9:36] So if we go back to our image here and click 1, we can see the image is this size, 1456 by 816.
[9:44] And all the images we're working with in this specific project are that size.
[9:47] So you want to make sure your format is set to that.
[9:51] And if you drag in an image, it'll actually create these additional formats down here at the bottom where you see that that format is there.
[9:58] So we have some standard formats. Like if you're working on YouTube, maybe 1920 by 1080, something like that would be what you render out and maybe you're working.
[10:05] But if we're working with something that's not standard, if you drag it into Nuke, it'll appear down here and we can just click that and set our project to that resolution.
[10:14] So that's another place that people will get tricked up a little bit is with formats because After Effects is automatically handling that for you.


### Color Channels [10:21]
**Transcript (timestamped):**
[10:21] So now we're just going to talk about the color channels real quick and the alpha channel again just to make sure that we get the concept.
[10:27] And we'll do a little bit of a roto just to do that because it's a very common process and you're probably familiar with doing it in After Effects.
[10:33] So to see different color channels and maybe you're not even familiar with what color channels are,
[10:39] but the color channels just represent each amount of color in each channel.
[10:44] So an image is made up of red, green and blue and so we can look at those channels independently.
[10:48] So if we look at this merge node and we click over our viewer and hit R, we'll see that the areas that are the most red will become, it'll kind of be a black and white representation.
[10:58] But the areas that have the most red will be the brightest areas.
[11:01] So you see like this area that's more blue is going to be a little bit darker.
[11:07] So if we go to the green channel or the blue channel, like if we say the blue channel, for example, we hit B, you see the areas that are yellow are getting darker,
[11:16] but the areas that are blue are staying bright.
[11:18] So we know there's more blue in this area.
[11:21] We can also hit alpha, which again is just our guy.
[11:24] But if we want to create a mask for this guy, how would we do it?
[11:28] So in After Effects, you would just go to your layer, you go to your pen tool and you would just quickly round the head here and we would just hit this.


### Masking / Roto [11:30]
**Transcript (timestamped):**
[11:36] And it would automatically cut that out in Nuke.
[11:38] It's a little bit different.
[11:39] We need to cut out this guy and his alpha by another alpha.
[11:43] So how we do that is we create a Roto node.
[11:45] So we can hit Tab and hit type Roto and you get the Roto node.
[11:49] The other way you can do it is hit O on your keyboard.
[11:53] If we double click that Roto node, we'll have the properties here and we'll have this little panel on the side.
[11:59] So if we hit Q on our keyboard when your mouse is pointing over the viewer and you'll see that we keep having to do the keyboard shortcuts where your mouse is pointing, it's important you're doing that.
[12:09] So pointing over here, make sure Q is on, you'll say overlay on and you'll see the little format here.
[12:15] If we click around, we can do the same effect.
[12:19] And we close the curve here.
[12:21] So that's how you can create new curves.
[12:23] You can just draw them and hit Enter and then you'll see that they stack up here.
[12:26] And if we are viewing that Roto node, so let's go to the view and hit A, we'll see that those two are stored there.
[12:33] So we can view something else even though we're not working on it.
[12:36] See how the Roto node is not connected to anything, but we can be viewing the soldier.
[12:40] So if I hit 1, I'm viewing the soldier.
[12:42] We see the overlay from the Roto node even though it's not even connected.
[12:46] So that's just something that you can keep in mind is like the overlay can be sort of from a different layer.
[12:53] But right now it's not doing anything because you can see that these nodes are not connected.
[12:57] And so how do we connect these nodes?
[12:59] If I view this and hit A, we do have an alpha, but we want to cut this out by this.
[13:03] So all we do is we create a merge node by hitting M and we can say A over B,
[13:09] but we don't want it to be over because we don't want to merge something over.
[13:13] We want to mask it.
[13:14] So if we switch this to mask, you'll see that this Roto alpha is now masking the layer that's being connected with here.
[13:22] So we have that result and if we merge it over A over B, we have the result that we're expecting.
[13:28] So that's the difference between After Effects is just that the nodes are kind of separated.
[13:33] And this is actually pretty useful because you can say what's cool about it is you can mask different layers because it's a tree.
[13:40] So you can do another merge node and you can say we can take that Roto and we can mask the background and we can switch it to mask.
[13:47] And so you can see how that could be start to be interesting when you have many, many layers.
[13:52] And it might not click yet, but when you start doing with 10, 20, 30 layers,
[13:56] it's really useful to have things displayed in a tree like this.
[14:00] Another thing I just did it, but you can press space to full screen different areas.
[14:05] If you're pointing over, if you just want to see everything laid out, you can also hit space on this area.
[14:11] Hit F to just get it bigger.
[14:13] So those are just some extra shortcut keys there.
[14:15] I'm going to delete this now because we don't need it, but that's just how you can apply a Roto shape really quickly on a layer that has an alpha already.
[14:24] So just to mention some other things real quick, if you wanted to do the opposite, we'll just do it real quick anyway.
[14:29] So I'll just create a Roto node and I'm just going to do a stencil instead of a mask.
[14:33] So operations that the stencil and then the same thing.
[14:37] So if we click around, it would just stencil it out.
[14:39] So that's just useful to know.
[14:40] That's kind of how you would invert it.
[14:42] And that's a useful thing to see.
[14:45] Otherwise you can have it set the mask and you could use an invert node.
[14:49] So you can hit Tab and type invert.
[14:51] I wouldn't do it that way, but just to know that that node is there is pretty useful.
[14:55] One other thing and just to, I know I'm going fast, but there's a lot of things to cover.
[15:00] So if we want to, if we wanted to make this Roto node have color in it, because right now it only has an alpha, right?
[15:07] It says Roto and it says alpha.
[15:09] And one thing to know is if you want to know what's coming out of a node, you can look at these little colorful boxes here.
[15:15] So this one has red, green and blue and an alpha.
[15:18] So we have the colors of the image and the alpha, the little white box.
[15:21] But we see here it's only giving us a white box.
[15:23] So how could we, if you wanted this to just be a solid, like we want to create a solid in After Effects, we go here, we do a new solid and we would pull this over and then we just select the color and we'd have a solid here,
[15:35] but it doesn't have an alpha.
[15:36] So we would go here and kind of mask it out.
[15:39] Like that's how we would create this red block over this image.
[15:42] If we wanted to do the same thing, we need to give this some colors.
[15:46] So if we switch the Roto node and set this outputting alpha, we just switch it to RGB and A.
[15:51] So it will give us colors and an alpha.
[15:53] And so if we switch that, you'll see now that in our red, green, blue channels, we had RGB, we'll see that white is there.
[16:01] And we can give it some color.
[16:03] So we could go over to our shape by clicking it.
[16:07] So we click the layer first and then we go to the shape tab and then we can just adjust the colors that is coming out of this.
[16:13] And if we were to merge this now, so we hit click it, hit M, A over B, now we can see that that is being merged over.
[16:20] So you see it's a little bit semi-transparent because in our shape, I did affect the alpha.
[16:26] So we have red, green, blue and then alpha is at point A once.
[16:29] So it's going to be a little bit transparent.
[16:31] So if I were to want that solid, I would just push that up so it's completely solid.
[16:34] So that's just why, you know, when you start to look at these nodes, you'll see all of these things as this RGBA or just alpha.
[16:42] And so again, remembering to always think of these things different, like in Photoshop, if we just think of the color and the alpha as something that's separate,
[16:49] we can control them separately and that's going to help us a lot.
[16:53] So to further emphasize that example, we could blur this by hitting B on our keyboard and then we could blur just that specific element and then it's being merged over.
[17:05] And so wherever you're placing these effects are, it's only going to affect the nodes that are before it.
[17:12] So let's just delete all of this and do it again.
[17:14] So if we wanted to blur just the background, we could put a blur node and then we put it in between these nodes that are connecting and we would just blur it like this.


### Nodes VS Precomping [17:17]
**Transcript (timestamped):**
[17:25] If we wanted to just blur the guy so you can hit delete and delete it, put a blur node here and we'll just blur the guy like this.
[17:32] And we are only blurring your guy.
[17:34] If you want to blur them together, we put it after those nodes and we just blur it together.
[17:39] And so that's how we can construct our image and how the tree and the order of things matters.
[17:46] So now that we saw how the order of things matter, what is it compared to After Effects and the precomp workflow?
[17:54] So in After Effects, if we wanted to blur these layers together, I mean, there would be two ways to do it.
[18:00] You could use an adjustment layer, just delete this.
[18:02] You could use an adjustment layer to affect everything, which we don't need to do in Nuke because you saw that if I want to do everything, I just put it after.
[18:10] But the other way to do it would be to merge things together and make them like a precomp.
[18:16] So I'm going to take these two things, I'm going to bring in this mist here.
[18:20] I'm going to put it over our image.
[18:22] I'm just going to drag it in and I'm just going to scale it down.
[18:26] I'm not going to make it transparent or anything.
[18:28] I'm just going to put these two layers together.
[18:30] So if you wanted to blur the guy and the smoke together, normally what you have to do is you select those two layers by hitting Shift and you would go to Layer and you would precompose it.
[18:39] So you precomp those two together and now we would apply the effect to that layer because they're now merged together.
[18:45] So we could say we go here, we could put a Gaussian blur and then we would drag it to our precomp and then we would just blur the precomp.
[18:53] So you can see these are blurring together.
[18:55] Now in Nuke, we don't need to actually precomp anything.
[18:58] We can do renders and precompning layers.
[19:01] We don't need to talk about it necessarily in this case, but if we bring in a smoke element here, so I'll go here, I'll grab our mist, I'll drag it in and then we will merge them together just like how we did in After Effects.
[19:14] So you see one thing real quick, you'll see that it is a JPEG so there's no alpha.
[19:19] So it's going to get a little bit confusing so you'll watch.
[19:21] So we'll take this and we'll merge it over and you'll see that it comes in like semi-transparent, right?
[19:27] It's kind of like a plus.
[19:30] Whereas here, you see when we merge it over, it's a black square.
[19:34] So what we want to do to just make it solid because it doesn't have an alpha, it doesn't know what should be solid and what shouldn't be.
[19:41] So that's the thing with Nuke that, again, beginners will be a little bit tripped up on.
[19:45] It's just like you have to think of the alpha separately.
[19:47] So if it doesn't have an alpha, we just want to give it one.


### Merging images [19:50]
**Transcript (timestamped):**
[19:50] So to give it a solid alpha just so that this will be black and this will be white like how it is,
[19:56] we want to do a shuffle node.
[19:57] So we type shuffle and then what we're going to do is we're going to hit this little white button here.
[20:02] So without having to explain this whole shuffle node, this isn't really necessary for beginners.
[20:06] Again, don't get overwhelmed.
[20:08] It actually is really easy but all we need to do is if we press that little white button and we hit A,
[20:13] you'll see that there's a solid alpha now and when you merge it over, it's going to block the other image kind of like how we would expect.
[20:21] So the other thing we want to do is we want to scale this down so we can do the same as what we did in After Effects.
[20:26] So we kind of scale it down and put it next to the guy.
[20:29] So how we can scale images in Nuke is to create a transform node.
[20:32] So we'll hit after and hit T on the keyboard or type transform and then we can just scale it down.
[20:39] So you'll have the controls for the node if it's double clicked and you have Q.
[20:44] So your overlay is on.
[20:45] We have our little transform controls.
[20:48] In After Effects, we can just click the different layers and scale them.
[20:51] But in Nuke, we've got to double click the node that we want to control here.
[20:54] So I'm going to put it here and next to the guy like this.
[20:57] And so we don't need to pre-comp these layers now.
[21:01] It's already done.
[21:02] If we wanted to blur these layers together, we just put the blur between these nodes here.
[21:07] So we put the blur here and then we just blur and you see that those two layers are being blurred together.
[21:13] So just the order of our nodes and the way we design this tree is going to be essentially,
[21:19] it's sort of like a logic of the way things are flowing and the effects are always in between where the merges are.
[21:27] So one other thing to mention is if you do put a transform node after an image that doesn't have an alpha,
[21:32] it will actually automatically create an alpha as well.
[21:35] So you see that the little white thing is appearing.
[21:37] So if we merge it over, it will do the same result.
[21:40] So if I merge it over, hit Q, take the scale, scale down a little bit, it is doing that effect.
[21:45] And if I disable that, you see it's that transparent.
[21:48] So that's again, just like a little quirk of Nuke that when you're starting out, you're like,
[21:52] well, if I just merge it over, why is it semi-transparent?
[21:56] But if I scale it down, then suddenly it becomes solid.
[21:59] It's just adding an alpha there because it thinks that you're probably trying to merge an image over another image.
[22:05] So that's why I explained it with the shuffle node first and then the transform.
[22:09] But you actually don't need the shuffle node, you can just do it and it's going to automatically create it.
[22:13] So if you ever see a problem where it's like doing stuff that you don't expect, you probably don't have an alpha.
[22:18] That's probably what's happening.
[22:19] So just keep that in mind.
[22:22] So I want to go over a few merge operations that are present in After Effects that you might be familiar with.


### Blend Modes / Operations [22:25]
**Transcript (timestamped):**
[22:27] So if I just go over into our project and I bring in our mist again, you might be familiar when you, if you hit F4,
[22:35] you can switch between these modes here and then these are all your kind of blending operations similar to Photoshop.
[22:41] And so add is going to make it kind of add over the top.
[22:45] We could do a multiply, we could do a screen.
[22:49] There's different ones that we can do here.
[22:51] Multiply would be another big one.
[22:52] So you get this type of effect.
[22:53] It's the same in Nuke with our merge operations.
[22:56] So that knowledge is really going to transfer over if you're familiar.
[22:59] So if you do a merge node and we do A over B at the beginning and we switch it to plus.
[23:05] Right now it's not going to do anything because again, it doesn't have an alpha.
[23:08] But if it had an alpha, so let's give it an alpha by hitting transform and we'll move it around a little bit.
[23:14] So if it's set to over and it has an alpha, it's just going to be like a merge like we just saw.
[23:19] But if we switch it to plus, it's going to be that kind of that transparency result where it's adding over the top and multiply.
[23:26] It's going to sort of cut through like this.
[23:29] So you can see the same effect that we just saw in After Effects.
[23:33] If you want to compare color correction in After Effects versus Nuke, I'm going to do a grade node.
[23:38] So I'm going to hit G on my keyboard or you can hit tab and type grade.


### Grading [23:39]
**Transcript (timestamped):**
[23:42] So this is the most common grade node.
[23:44] The other one that you might be kind of familiar with if you're coming from After Effects is the curve tool, but it's called color lookup.
[23:50] So if you type the color lookup and you plug this in and you click on the master right here, you'll recognize this curve probably if you're coming from Photoshop and stuff like that.
[23:59] The grade node does the same thing.
[24:01] It's used in a different way.
[24:02] It's actually faster.
[24:03] I actually prefer this versus using a color lookup all the time.
[24:07] Most people, once you use this, you're not going to actually want to go back and have to use a curve every single time because you can do the majority with basically these two sliders, the gain and the gamma.
[24:16] That's what you're going to use the most often.
[24:19] So if we just use the grade node and plug it in, I'm just going to gamma down a tiny bit and you'll see that we're adding contrast overall to the scene.
[24:27] And if we were to go in After Effects and try the same thing, we could go, let's create an adjustment layer so we do it to everything.
[24:33] So we'll create an adjustment layer and then we'll just do a curve.
[24:36] We'll plug it in and we'll just pull down the center here and you see we're adding contrast.
[24:41] So it's the same thing.
[24:42] We can adjust the white point here so we can grab the top corner.
[24:45] We can push it over.
[24:46] And if you want to adjust sort of like this in Nuke, you can do the same.
[24:52] So let's bring the gamma back up and we can push up like this and that's going to brighten like that.
[24:57] So if we wanted to do that in After Effects, let's bring that back up and then I'll just get rid of the center point here actually.
[25:05] So we'll just create a new curve and then we would just pull up towards the top and you see that that's visually the same.
[25:11] So we're doing a gain and that's how that effect is happening.
[25:15] So on that curve, we're just doing it in a different way.
[25:19] So gain, gamma, that's a very common S curve.
[25:23] So what you're doing is you're adding contrast and you're bringing up the highlights.
[25:27] So in After Effects, you might be familiar with doing that.
[25:30] So you would bring it up like this and then you pull it down like this.
[25:33] And that's why it's called an S curve because it's creating something that looks like an S but it gives you that sort of film grade that is very common.
[25:40] So you can push it too far, it's a little bit too far for this shot, but that's just to know what we're doing.
[25:45] It's good to know though that a gamma is sort of in the center of the curve and the multiply is when, not when we have the second point here,
[25:53] but when we pull up this point here, that's kind of what we're doing.
[25:58] Now if you want to go further and we want to adjust different colors, we can put a new grade node here.
[26:03] I'll just delete the old one out of the little color wheel.
[26:05] We can split it into the colors and we can adjust the colors this way.
[26:08] So we want to take red out of the image, we can do that.
[26:11] We want to take green out of the image, we want to take blue out.
[26:14] And so that's the same thing as going into your curves here and going to your different color channels and basically just manipulating those there.
[26:23] So you can do the same thing.
[26:24] The other way you can do it, I don't really do it this way, but you could disable these and then just start pulling down.
[26:31] Like you just affect only the red channel, for example, so you could gamma down only in the red channel.
[26:36] I don't typically work like that, but you can get some interesting effects by just, you know, disabling the color channels.
[26:42] I prefer to just work with the color wheels with all the channels enabled for the most part.
[26:47] But that's pretty much it for the basic color correction and we can continue on.
[26:52] So one last thing I'm going to mention is node cloning.
[26:57] And so if you're familiar with the pick whip in After Effects, that's something that might confuse you if you're transitioning over.
[27:04] And you want to make things move together and you're not exactly sure how to do that if they're on different layers.
[27:09] So let's say we have a mist and we bring in here and let's say we want these two to move together, but we don't want to pre comp them together for some reason.
[27:18] Like maybe there's just a reason we want to do that and we're moving this guy around.


### Pikwip VS Transform [27:19]
**Transcript (timestamped):**
[27:22] We want that to move with it.
[27:23] We would go here and we would grab the pick, pick whip and we drag it to our guy and then they'll move together.
[27:30] And so there is a way to do that in Nuke.
[27:32] So you can create a transform node and merge this over again.
[27:36] So we have an alpha and we can scale down and we'll put it behind and then we'll view when they're merged over.
[27:41] So how could we get those two layers to have a relationship to each other?
[27:45] What you can actually do is create another transform node and you can stack transform nodes like this.
[27:50] And what we want to do is press Alt K.
[27:54] I would be option K on Mac if you're doing it on Mac.
[27:58] And you'll see this little orange line between the two nodes here.
[28:02] We can drag it and put it on the other layer.
[28:05] So it means that these are basically doing the same transform.
[28:08] So if we double click that, make sure that we're doing the right layer here.
[28:13] Because if we still have this one open, you might get confused.
[28:15] So make sure the last one that you double clicked will be the one that's being controlled in your sort of viewer here.
[28:22] So I'm going to close the other one just so it's not confusing.
[28:25] And if we double click it and we move it, you'll see that both layers move together now.
[28:29] So these nodes are a clone and that's how you could make them move together.
[28:34] Alternatively, like we mentioned earlier, you could just have them on the same layer like so.
[28:40] And then we could put a node after and then they would move together like this as well.
[28:45] So that's just a different way.
[28:46] For some reason, your node tree needs to be in a different order.
[28:50] You know, maybe there's some effects being applied to the background, but not the foreground, but they move together, for example.
[28:56] So that's just to know if you're trying to do a pick whip or a parent, essentially, that is the way you would do it.
[29:03] So the next thing we'll mention is to merge different images that are different size over each other.
[29:08] This is where, again, beginners get tripped up.
[29:10] It's always the pre-mult thing.
[29:11] It's always this and it's always the two different size of image.
[29:15] But once you get past those two, a little bit of confusion versus after effects, I promise you, there's no other huge hurdle of understanding.
[29:24] It's just those really simple things.
[29:25] So here we have this 1456 by 816 and then we have this thing that was filmed on an iPhone vertically.


### Different Size Images [29:33]
**Transcript (timestamped):**
[29:33] And so if I want to merge this over the other one, remember there's no alpha.
[29:37] So we're going to see the semi-transparent weird result by default.
[29:41] So again, if we hit T, it's going to create an alpha through that transform node and then it's going to be merged over.
[29:47] But you see that it's not size to the project size.
[29:50] And after effects, we do the same thing.
[29:52] It would be kind of scaled off of your video.
[29:54] So what we can do is take the transform and just scale it down and we could bring it in like that.
[29:59] And so that would be a perfectly fine way of bringing in an image and making it fit.
[30:04] The other way we could do it, if you wanted it just to automatically fit to this project size 1456 would be to put a reformat node.
[30:15] And so reformat node allows you to change the size of a node.
[30:18] And so by default, if you set your project size correctly, if you hit S, which I believe it'll be delivered like this to you automatically.
[30:25] So your project size should be this 1456.
[30:28] If that is set by default, the node will reformat whatever this thing is to the project size.
[30:35] So this thing is coming in as 1080 by 1920.
[30:38] It's going to automatically go to the project size.
[30:40] But you see that the way if you view it, you see that the way it's reformatting it, it's just cropping off the top and the bottom, which maybe that's not what you want.
[30:48] So there's different resize type here.
[30:50] And so you can switch it to height.
[30:52] So to take this vertical video, it'll shrink it down into that rectangle format that we're working in.
[30:57] And it'll create this weird stretch pixel effect.
[31:00] And the reason it's doing that is because this dotted line is the pixels that are being calculated.
[31:05] So it's only calculating the pixels inside your bounding box.
[31:09] So that's what this is called.
[31:10] It's called a bounding box, these dotted line.
[31:12] And essentially what you could do is just press this little button here that says black outside and it will just get rid of everything out there.
[31:19] The reason it does that is just because the edge, it's not calculating it beyond that.
[31:23] And it's just stretching the color because it doesn't know what to do.
[31:26] So you just click the little black outside button and it fixes it.
[31:29] The other way you could do it is if you leave it off and you hit T and you create the alpha, it'll automatically just discard everything that's not being calculated outside of the bounding box.
[31:39] So if you merge it over, same result.
[31:42] It's fitting perfectly to a video and that's good to go.
[31:45] The other thing to note is if you scale this up and you see that that dotted line is going beyond your frame, again, our bounding box is going beyond the frame.
[31:53] But the term for that, important to know because when you're talking about it, if you don't know what the term is, it's called overscan.
[31:59] So any pixels that are outside of the frame are called overscan.
[32:02] And sometimes you want some pixels to be outside of the frame because let's say you want to animate this clip moving into the frame, right?
[32:09] You want to have some data that's out there.
[32:11] So that's just important to know.
[32:13] Overscan pixels are outside of the frame that we can see.
[32:17] And the reason that can be useful as well is if we blur this image, so we'll put a blur node and we'll just blur it.
[32:25] So that blur is taking the average of all the colors.
[32:28] And so if there was no pixels outside of this frame, it would just be pulling in black here.
[32:33] So for example, to show to kind of show that, let's just disable the blur for a second and we'll use another node that's very common called the crop node.
[32:41] And we'll crop it and the crop will automatically cut the pixels to the edge of the video.
[32:46] And so now you see that that dotted line, if I hit disabled, if you press the note, it will disable the effect.
[32:53] You see that the pixels that are outside there are getting cut off because our dotted frame is no longer showing that overscan.
[32:59] And so if we were to blur it now, you see that the edge, there's nothing for it to pull in.
[33:04] There's no colors for it to pull in.
[33:05] So that's why it's useful to have some overscan sometimes.
[33:08] But at the same time, if you have a really big bounty box, and let's say we've scaled up this image, you know, we've let's say we brought in this Ember video and we've scaled it and we've rotated it and we put it like this.
[33:21] And we have like all this giant, you know, pixels out here, every frame is calculating all this stuff that we actually don't see.
[33:29] And so if we were to like take this and then we blur it, it's blurring the pixels in here, but it's also blurring all the pixels out here.
[33:37] So it's going to slow down your computer if it's wasting that processing power to blur all these pixels.
[33:41] And so this is where the crop node would be useful.
[33:44] But again, we just said that we can't crop it because I'm sorry, we can't crop it because there's not pixels to pull in, but we can crop it and then double click the crop node.
[33:53] And then just there's actually a little line here if we hit Q, make sure overlays on we just expand it.
[33:58] So we give it enough overscan so that it doesn't have that blurring issue.
[34:02] But at the same time, we're not processing all of the pixels that are like way, way outside of the video frame.
[34:08] So that's where the crop node comes in.
[34:10] It becomes an optimization issue when you have like things that you've massively scaled up and then, you know, it's just wasting processing and it will happen.
[34:18] That's like a media issue that people run into.
[34:20] You scale two images that don't fit together and then your computer starts slowing down.
[34:25] If you start having some really slow stuff or something like that, zoom out, check this little dotted line.
[34:31] That's most often the issue that beginners run into.
[34:35] It's very, very common even to make that mistake, you know, just working.
[34:39] So definitely check your bounding box is something that I would recommend.
[34:44] And so this is good and we could switch this video clip here to a plus.
[34:49] And then we could, you know, see instead of having it over black, we have some of those like embers blown of the video.
[34:56] We're going to make this look better.
[34:57] This is just a quick example.
[34:58] That's just kind of a quick and dirty example.
[35:01] But yeah, that is something to know with merging images that are different sizes over each other.
[35:07] So next we're going to talk about how to take this image and bring it into a composite that is sort of more final.
[35:13] So I'm going to give you guys my full node tree here.
[35:15] One of the best ways to learn new is to learn from other people's scripts.
[35:19] So I provided you guys my simple script here.
[35:21] You'll be able to step down.
[35:23] One really good way to learn is take the viewer node and just look at each layer to understand what the person's logic was.
[35:29] And that's a really, really good way to follow and understand what the decisions were to kind of make the composite work.
[35:36] And so I can step down this comp and I can look at every single layer, every single color correction that's being done here.
[35:42] And you can see exactly how it's done.
[35:45] So that is available for you guys.
[35:47] We're going to rebuild this from scratch in this video.
[35:49] So not to worry, but that is there.
[35:52] I'll leave it in the script on this side here.
[35:55] So this viewer node is here.
[35:57] This is the example we just did.
[35:59] And I'll start building it from here.
[36:00] Again, we'll have our elements.
[36:02] And I also provided you guys with one extra node called exponential glow.
[36:05] The way you can save this is a custom node, but you can save it by pressing this little thing.


### Starting the Composite [36:08]
**Transcript (timestamped):**
[36:10] A little kind of a wrench here and hitting create.


### Saving a node [36:12]
**Transcript (timestamped):**
[36:14] And then if you just type a name, it'll save this in your nodes that you can search later.
[36:19] So if you say X glow, X glow like this and hit enter, whenever you hit tab, you can type that and you'll actually get that node.
[36:28] And so all this node is, is just a better glow than the normal glow.
[36:31] There's a normal glow in Nuke called glow.
[36:34] This one just looks a little bit better because if we hit, if you put it on something to show you,
[36:39] if we create a radio node, which is just a circle, I'll just turn the softness to zero and then I'll plug the glow into the radio.
[36:47] You see what the normal glow looks like.
[36:49] And then if we put an exponential glow and switch our viewer, it's a little bit better.
[36:53] It just kind of falls off nicer.
[36:55] And that's something you'll learn about as time goes on, exponential glow and quadratic falloff and those type of things.
[37:01] We're not going to go deep in those concepts in this video, but it is better.
[37:05] So save it and it'll make your stuff look better.
[37:08] So with that in mind, we'll start building this composite.
[37:13] So now we're going to start the composite.
[37:15] One thing to mention is we want to look at our pictures first.
[37:18] So we have all of our pictures laid out here and we have the basic start for our script, which is what I'll give you guys to set up.


### Opening the Project [37:22]
**Transcript (timestamped):**
[37:24] Also, to keep your script organized, you can add these little elbows, these little dot nodes by holding control and then clicking on these pipes in between the nodes.
[37:33] And that just helps you keep these strict lines.
[37:35] I always give a little bit of space and usually I will always add the nodes vertically and then we just connect it over to the right.
[37:41] And that's really good way to keep your scripts organized.
[37:43] So first thing we want to do is look at our images.
[37:46] We can see here that he's a little bit out of focus on his back arm and shoulder and he's in focus towards the camera.
[37:52] So what we want to actually do to make this look kind of cool is make it look like a long focal length lens.
[37:57] So a longer lens is going to have a shallower depth of field.
[38:00] Depth of field is where you have a certain portion of your frame that's in focus and the rest is out of focus and you get a bokeh background.
[38:09] So some of you guys might know what that is.
[38:11] Some might not, but just speaking broadly here, that's what we're going to do.
[38:14] So basically we need to do reframing the background and make it look out of focus.
[38:18] So I'm going to put a transform node by hitting T.


### Defocus and Position [38:19]
**Transcript (timestamped):**
[38:20] I'm going to scale it up and I'm going to start to position it in a place that makes sense.
[38:25] He's lit from the top left, so I want to have something that sort of justifies that kind of lighting.
[38:30] And I'll just play with the position here to get something along those lines, move it into place and make it look like these mountains are the trees are pretty far behind him.
[38:40] So something like this would be good.
[38:42] I'm going to have it more on the left as well because I do want to add a smoke element back there.
[38:46] So if I put just, you know, white, it's going to be hard to see any additional layers of elements and that wouldn't be as interesting.
[38:53] So something like this is going to work.
[38:55] It doesn't matter that our image is really low res because we're going to make it out of focus anyways.
[38:59] So one thing we want to do before we add the defocus is remember our good habits.
[39:04] As soon as we scale that picture up, we're going to have a really, really big bounty box and we don't really want to do that because if we had a defocus node,
[39:10] and this is kind of like a blur, but it acts more like a camera defocus,
[39:13] it's going to defocus all these pixels that are out here and that's going to waste a lot of computer memory.
[39:18] So what we're going to do is add a crop node after the transform and then just pull that a little bit outside the edges so that we don't run into the issue that we talked about earlier.
[39:26] And now if we add the defocus, double click it and we can increase that amount.
[39:31] We'll start to see that that looks like a camera defocus.
[39:33] So let's look at the result of the merge by pressing one and we can get something interesting like that.
[39:39] So we can scale that up and down.
[39:41] Now one thing to note visual as a visual difference is if you plug in the blur node and we blur it
[39:47] and we compare to the focus, I'll press one and look at this and press one and look at this, they actually do a different thing.
[39:53] So to see that we get these sharp circular bokeh highlights and that's what a camera does when it's the focused image versus blur, which is not as photorealistic.
[40:02] So it is better to use this in this type of scenario.
[40:06] It's a good thing to understand visually that there is a difference there.
[40:10] So if we look at our guy, there's a few things we got to fix on him as well because this was cut out just roughly Photoshop.
[40:16] The edge is not matching the focus.
[40:19] If we look at him, you see that we have like a dark and sharp edge where it should just be kind of out of focus on that edge.
[40:25] So what we can do is just add a simple edge blur.
[40:27] So we add an edge blur node and this will just blur around the edge and we can increase this amount until it matches the focus.
[40:35] And the way to match it is to look at the highlights, try to find circular highlights is even better to look for.
[40:40] But even just the edges and you can see how wide the edges are and try to match that.
[40:44] We could do some more advanced edge fixes and edge extends, but I'm not going to get into it in this tutorial just to not overcomplicate things for beginners.
[40:52] So this is perfectly fine for what we're doing.
[40:54] And what we can do is we can isolate this effect because if we're doing an edge blur, what it's doing is it blurs the edge all the way around.
[41:01] But we don't want to blur this side.
[41:03] So we want to isolate it.
[41:04] So we press O and we can plug in this little mask input.


### Masked Effects [41:05]
**Transcript (timestamped):**
[41:07] So let many nodes, even the grade node, for example, this little side arrow has a mask input and will isolate the effect through that roto shape.
[41:14] So if we take the roto shape and double click, we turn our overlay on and we just draw a roto around this area.
[41:20] And then we view this node, make sure we're looking at it.
[41:23] You'll see if I zoom in here that the edge blur is only being applied within the alpha.
[41:27] And so that's good, but we don't want to have a sharp, you know, cutoff where that effect ends.
[41:31] So what we can do with the roto points is hold control and just soften them off a little bit.
[41:36] And that's going to be good enough for what we're doing.
[41:39] So that's a good result.
[41:40] And now we can look at this and it looks like he's fading back out of focus.
[41:44] We could brighten the edge slightly, but like I said, we won't nitpick too much on this comp.
[41:50] One of the reasons I moved this down, like we said, was to get the smoke element in there because we didn't want to put it over something really bright.
[41:57] So let's go grab our smoke element and we can put some just an additional layer of contrast between them.
[42:03] And that will give it a little bit more interest.
[42:05] So we can grab this guy, I'll hit control V so we leave the original up there and just control control C control V rather.
[42:11] And we'll put a transform node and we'll merge it over.
[42:15] So of course, this is not what we want.
[42:17] We want that to be kind of, you know, transparent.
[42:21] One mistake that you will make probably is doing this plus operation.
[42:26] And in some cases is kind of technically works, but it's actually you're going to get slapped on the wrist if you ever do this in the visual effects studio because it's not actually what you're supposed to do.


### Compositing Smoke [42:30]
**Transcript (timestamped):**
[42:34] It's smoke over black, it works, but if you do it over things that have any kind of light, this is actually incorrect because smoke should not brighten something that is behind.
[42:44] So you should never be plussing a smoke over.
[42:47] And even though you may have learned to do it this way at After Effects or Photoshop, there's tutorials out there to show this.
[42:52] The technically correct way is slightly different.
[42:55] So I'm going to teach you guys this early on just so you have a good habit.
[42:58] So we're going to keep it as an over.
[43:00] But what we're going to do is we're going to give this an alpha.
[43:04] And so right now it doesn't have an alpha, but what we can do is create an alpha from the luminance or the brightness of the image.
[43:10] So we're going to use a keyer node.
[43:12] What this node does is it looks at the brightness of the image and creates an alpha channel.
[43:16] So if we hit A, we see that there's now an alpha channel.
[43:18] If I hit D on the keyboard to disable it, you see it's no longer there.
[43:22] So it's creating that alpha channel, which if we do over, you see that it's doing a similar effect now.
[43:28] So if I disable the keyer and enable, you see that's doing that.
[43:32] There's a slight difference visually though.
[43:34] So if we take the two, I'll just show you to compare.
[43:37] I'll make this one a plus.
[43:39] So the same thing as we had before.
[43:41] And you see if we look real close, it's brightening what's behind.
[43:44] And then this one is actually occluding what's behind.
[43:47] So smoke occludes.
[43:48] It doesn't brighten.
[43:49] And so that's an interesting thing to keep in mind.
[43:54] Now, what we can do as well is we can grade this a little bit to get it in the color tones that our image is in.
[44:01] So I'm just going to move it into a more interesting place real quick.
[44:04] And maybe we'll just flip it over so I can grab these little things and just flip it like this.
[44:09] So we can use maybe the bottom half or scale it in different ways.
[44:14] We can even create another transform and just kind of play around with the position.
[44:18] So maybe something like that.
[44:21] I'll just keep playing with it to get something that looks interesting.
[44:25] You know, maybe something like this.
[44:32] And it's also going to look kind of weird because like I said, the colors are matching.
[44:36] So we're going to put a grade note before the keyer.
[44:38] That would affect the keyer slightly, but we're not going to worry about it right now because I don't want to worry about the...
[44:42] There's a workflow called Unpremult.
[44:44] We're not going to get into it in this video.
[44:47] We're just going to keep it simple.
[44:49] We're just going to go to the multiply and we're just going to put a little bit of blue into it.
[44:53] So if you notice everything is kind of neutral.
[44:56] It's pretty neutral, but there's a slight kind of blue color in there.
[45:00] We don't want to be this reddish color.
[45:02] We just want to get those tones of yours slightly similar.
[45:05] And also we could make it a little bit more transparent and we also need to defocus it.
[45:09] So again, what we want to do is we're going to copy this defocus and we're going to paste it on here.
[45:15] Now what we're going to do is take that defocus and just reduce it a tiny bit.
[45:19] So we'll kind of pretend that that's a little bit closer to us.
[45:22] And so it would be a little bit less out of focus.
[45:26] And that's why we're not using the same defocus.
[45:28] The other way we could do it, if you want it to keep it the same, you can have one defocus note after and it would just defocus everything.
[45:34] So this will be fine.
[45:36] What we can also do is take the alpha here and we will reduce it.
[45:42] So there's different ways we can do that.
[45:44] One way we'll just do it through the merge note for now to keep it simple.
[45:47] There's a mix option.
[45:49] So if I double click this merge note, we can just bring the mix down and we can make it a little bit more see-through that way.
[45:56] So there's a few ways to do it.
[45:58] If you continue down the path of learning Nuke, we'll learn some different ways.
[46:01] But this is keeping it simple.
[46:03] And we'll just tweak the color a tiny bit more on the smoke.
[46:07] I realized it's slightly too blue versus a little bit of this kind of greenish tint there.
[46:12] So all we can do is just take this and we just pull over a tiny bit and we'll see that that starts to match a tiny bit better.
[46:19] So we just need to make sure we have those colors a little bit closer there.


### Color Match [46:20]
**Transcript (timestamped):**
[46:23] And that's pretty good.
[46:25] So the colors can be pretty small differences, but when you look close, you want to make sure that those are matching.
[46:32] So continuing forward here, we're going to add some fire back here and we're also going to start to match the contrast a tiny bit.
[46:37] So if you notice how bright his armor is and how bright the sky that's reflecting is, we have some bright sky.


### Contrast Match [46:39]
**Transcript (timestamped):**
[46:44] But if you look at the value of the sky, it could be a lot brighter just to make it feel like that punchy contrast.
[46:50] And that's what we want to add first.
[46:52] So we'll just after the defocus note before the smoke, we'll add a grade.
[46:56] And we'll just start to increase the gain a bit and then we can just bring down the gamma a tiny bit.
[47:01] And that's just going to help our image feel a bit more punchier and that's going to help that blend together.


### Fire Compositing [47:05]
**Transcript (timestamped):**
[47:06] So that's a good starting point.
[47:08] Another thing we can do now is grab that fire element.
[47:10] So we'll copy and paste.
[47:11] So copy it paste control C control V and we'll merge it over.
[47:16] It doesn't have an alpha in this case.
[47:18] So we're going to plus it.
[47:20] And by the way, if it's over with an up without an alpha, it's already a plus, but just to know that.
[47:26] And then I'm going to position this so it's not so intense.
[47:28] I just want to be kind of something subtle and in the background.
[47:31] So I'll just kind of move it off to the side here and we'll just use maybe the bottom corner of it.
[47:36] Just to just to hint that something is going on back here.
[47:39] We're thinking about the story.
[47:40] We're trying to think about why is there light on his right side?
[47:44] Maybe there's a fire right in front of him that he's standing in front of.
[47:48] And we're going to add some embers and stuff like that.
[47:50] But maybe the forest behind him is on fire so we can kind of justify that and play with the position here until we get something that you like.
[47:58] One thing is it's just like a pattern.
[48:00] So part of being compositor is designing shots with either the map painting or the elements themselves and trying to just find areas that you think look cool.
[48:09] And it doesn't conflict too much with your eye and where you're looking.
[48:12] And so I just spend like a few minutes playing around with the position of things.
[48:16] If I were to go up and grab the position I already did and paste it here, I'll just use that position.
[48:24] So this is what I picked before.
[48:26] And I think this was a pretty good position.
[48:28] We can mask this off and we're also going to have to do some color matching here because it's really, really red.
[48:32] If you notice it's kind of very red compared to him.
[48:35] And right now it feels a bit disconnected.
[48:37] So we need to kind of roto off some pieces so we don't have just things that we're distracting.
[48:42] If you notice here it's kind of pulling your eye.
[48:45] We don't want to look straight to there.
[48:47] We want to be looking at him and also make the colors better.
[48:50] So let's do the colors first.
[48:52] We'll do a gray note.
[48:54] And what we want to do is we want to reduce some of the red to make it a bit more yellowish.
[48:59] So we're going to go into the colors here.
[49:01] We're going to reduce a bit of the red and that's going to bring it to something less red and will also reduce the blue.
[49:07] If you reduce blue, what do you get on the opposite side of the color rail is yellow.
[49:11] So if you actually reduce blue, you're going to get more yellow in the image.
[49:14] And so you can do it that way.
[49:16] And then what we can do is add some contrast to it.
[49:19] So the colors are feeling more correct, but it feels very flat.
[49:23] And it doesn't feel like punchy like this.
[49:26] So what we can do is another gray note, close everything else, we'll gain it up a bit and we'll get it down.
[49:32] Just add that punchiness to it.
[49:36] And that's something that's a little bit closer.
[49:38] So let's look at it just before the de-focus to see what we have.
[49:41] So that's kind of interesting.
[49:43] We want to make it look like fire.
[49:44] So looking at it before the de-focus can help.
[49:47] And then the other thing we can do is another trick.
[49:50] So another trick that after the de-focus, you know, you see these little circles that come from the bokeh highlights.
[49:57] We can actually add more of those by targeting the highlights and boosting them just a tiny bit.
[50:01] So if you take a key or note and you plug it in, remember we said the key creates an alpha based off of the brightness.
[50:09] So we're going to use this alpha, not as an alpha that we're using, but as a, just as a control to target and grade just the highlights.
[50:16] So if we view this and we hit A, we can see this.
[50:19] And if you pull this bar over, you'll see that it kind of crunches down towards the brightest areas of your image.
[50:24] So we're going to crunch it down a tiny bit like that.
[50:26] And this alpha is what we're going to use to color grade.
[50:31] So we plug it in another grade and then use the little mask input and plug it into this alpha.
[50:37] So if you view here and now we use these controls, we say you can see here it says mask RGBA alpha.
[50:43] So it's using the alpha that's created here.
[50:45] And if you view it, there's the alpha.
[50:47] And now if we gain up, it'll only boost through there.
[50:49] So if you look real close, you can see that just the highlights, the very tips of the fire getting brighter.
[50:55] And what that does visually after a defocus is it's going to give these little sort of boosts in the bokeh highlights.
[51:02] So if you boost it up a tiny bit, you'll see the circles.
[51:04] Only a few of them get boosted out, but it seems to add more detail.
[51:07] Gives a little bit of that punchier look that we're going for.
[51:10] And we can push it a little bit further here even.
[51:13] And maybe we need to expand our key here so we can grab that little bar.
[51:17] And if we move it over, different areas will be affected as well.
[51:22] So we can push it up much further and then we get something kind of like this.
[51:25] And you start to get something that's kind of nice.
[51:27] So we'll put our roto note here and we're going to cut off this side.
[51:31] So we're going to switch the roto to a stencil.
[51:34] And then we'll take the roto, double click it, cue for the overlay, and then we'll draw a circle here.
[51:38] And then we'll just hold control to grab these points and just feather it outward.
[51:42] And we can just reduce the brightness by essentially stenciling it out.
[51:46] So we don't want to be looking there, but maybe just a hint of something that's kind of interesting.
[51:52] So there are more ways we can balance this image out even more.
[51:55] So right now as a compositor, my eye is going here.
[51:58] It still feels a bit, it's just like your eyes going here.
[52:01] If you just zoom out and let's look at this as almost an abstraction, you know, you have like this just black hole kind of thing.
[52:07] And also like you're not feeling the connection between this light and what's off screen.
[52:11] And of course this fire might be in front of him, so you wouldn't see it behind him.
[52:15] But what I like to do as an artist, I like to try to hint to those light directions as much as I can.
[52:21] And so what we can do is we can put a grade note after our defocus and our other grade note here.
[52:26] And we're going to plug it into a radio.


### Secondary Grades [52:27]
**Transcript (timestamped):**
[52:28] I like to use these radials for this sort of pools of light concept.
[52:32] So if we turn on our overlay, essentially the radio is just creating the circle here like we did earlier.
[52:39] And we're going to put it over on this side and we're going to use that to just boost up the side.
[52:45] So just boost it up in the game.
[52:47] We can kind of brighten what's back there just a tiny bit and that's going to help make it not so dark.
[52:54] We can even add a bit of gamma which would actually decontrast it a slight bit.
[52:58] So we can have a slight gamma, a slight gain which actually boosts the highlights and just make that circle a little bit bigger.
[53:05] And we'll kind of have something more like that.
[53:08] And then we can add a tiny bit of color to it if you want so we can add a slight bit of warmth into that side.
[53:13] So it feels like there's just some light casting.
[53:16] And if we just disable that and enable it, so disable and enable.
[53:21] You see how just those slight grade corrections, we can guide the eye in certain directions here.
[53:27] So continuing forward, we can do another one here.
[53:30] We did this little spot correction.
[53:32] We can do another spot correction here.
[53:33] I typically try to avoid areas that look very cut out like very dark on something bright.
[53:38] It can happen but I try to avoid those areas if possible.
[53:42] So I'll put a radio here and then I'll move it to area so put it down.
[53:47] We don't actually need to see it while we're doing it but we can just grab it and put it here.
[53:50] And then we'll just take this gray note and we'll just kind of darken that a little bit.
[53:55] You don't want to be looking there, right?
[53:57] And those areas of high contrast is where you're going to look.
[53:59] So we can adjust this one a little brighter maybe just behind him.
[54:03] It gives a little bit more of that hot feel behind.
[54:06] We could desaturate that slightly more potentially but we'll leave it at that for now.
[54:12] And we'll start to bring out some details on this guy.
[54:16] So I'm going to expand our comp just to make everything really clean.


### Cleaning Up Script [54:17]
**Transcript (timestamped):**
[54:20] One thing we can do if you want to start organizing your script is to label things.
[54:25] So you can actually hit tab and type backdrop and it will create this note that surrounds the other notes.
[54:30] Which is useful for just grabbing stuff but what you can also do is double click it and you can put labels.
[54:35] So we'll just say smoke element and then we can do the same thing for this guy up here.
[54:42] Move all these and then we'll just put a backdrop around it and call it fire trees.
[54:49] And you can change the colors of these notes as well so you can, you know, if it's fire we can make it orange, etc.
[54:56] Usually I try to use desaturated colors because if you stare at colors too much it'll actually affect your perception of color.
[55:02] You'll actually burn the colors into your eyes.
[55:04] It sounds kind of ridiculous but it is true.
[55:06] You have to be careful looking at really saturated colors because it'll distort your perception.
[55:11] So I'll try to use a little bit desaturated and continue forward here.


### Metal Glow [55:15]
**Transcript (timestamped):**
[55:16] So the next thing we're going to actually do is we're going to start to make his metal look a little bit more hot.
[55:21] Because if we look at the highlights they look a little bit clumpy right now.
[55:24] And what happens with really bright metal when it reflects something like fire is that the very, very highlights will get almost blown out.
[55:32] And there will be a tiny bit of glow.
[55:34] So what we're going to do is we're going to isolate the highlights of the armor.
[55:37] And we're going to paint out those highlights and add a slight glow just to give it a little bit more of that metallic feeling.
[55:43] So now we're going to add that glow and how we're going to do it is we're going to start with a keier node.
[55:47] And we're going to plug it in off of this branch so we're not actually not going to do it on the same layer.
[55:52] We're going to have the glow coming in as a plus because it doesn't need to be something that's solid.
[55:56] So if it's something like a glow usually you can think of it like that.
[55:59] You don't have to think of it as something that needs an alpha necessarily.
[56:02] It's going to be plus down at the end.
[56:03] But we're going to use the alpha that we create from this keier node to isolate different parts of the metal.
[56:08] So if you look at this and hit one and we hit A on our keyboard to look at the alpha.
[56:13] We're going to crunch this way, way down until we just get the very small details of the metal.
[56:17] And what we can do is we're going to do a pre-mult.
[56:20] So you remember if we have an alpha that's stored in the image and pre-multed it applies the cutout to the colors.
[56:27] So it'll apply that change that we've made and now we just have those areas.
[56:31] And now what we can do is we can take a mask, so O and then M,
[56:36] and mask off the side that is in the fire like this.
[56:40] Hit enter and then we get that.
[56:45] And now what we'll do is we'll grab our little exponential glow node that we have and we'll put it on the end.
[56:53] So now it's going to only glow those highlights.
[56:56] Now this might be too intense.
[56:57] It's going to be way too intense, but let's just put it over.
[57:00] And then we can adjust it.
[57:02] So we'll put it to A plus B.
[57:04] Right now it's over, but we'll set it to A plus.
[57:08] And then we have something like this.
[57:09] Now this is way too bright.
[57:10] It looks like overblown.
[57:11] So we want to keep this as a really subtle effect.
[57:13] So we're going to take the brightness and put it really, really low.
[57:16] And then we're going to take the spread and put it low as well.
[57:18] We want it to be like a very tight glow.
[57:20] It's just on the edge.
[57:22] So we can actually maybe we can brighten that tiny bit and just try to find the right spot for that.
[57:28] So we can do something like that.
[57:31] Then we can plus it on.
[57:33] And something like that looks kind of good.
[57:35] Now at the top it might be a little bit too much.
[57:37] So we might need to adjust specific areas.
[57:40] Another thing we can do to make it look better is if we desaturate just the very highlights,
[57:45] it's going to always help.
[57:47] So I'm going to go here with the keyer node before and we're going to desaturate the highlights of the very hot metal areas.
[57:56] So I'll do the same thing.
[57:58] I'll target those areas.
[58:00] And I'll just take a saturation node.
[58:02] So if you hit type saturation and you plug that into the mask and then we pull it down.
[58:09] What it's going to do is it's going to take some of the color out of the very, very bright areas.
[58:13] And that can help sometimes by just not having everything in one color.
[58:18] It kind of feels a little bit more two-tone.
[58:20] So if it's disable it and enable it, it just adds a tiny bit of color into the range there.
[58:25] And it's a very subtle effect.
[58:27] We don't want it to overdo this otherwise it's not going to look good.
[58:30] So some of the white areas are not working so well.
[58:32] So we want to make sure that those are not included in the mask.
[58:35] So what you can do is take another roto shape on the same layer by double clicking.
[58:40] We'll draw it over the areas that we don't want.
[58:43] So I'll draw around those white areas.
[58:48] And then over here we can click this little sort of stacked square icon
[58:53] and switch it from an over to a minus.
[58:55] So it's actually subtracting away.
[58:57] So if you look at the alpha in here, it's actually subtracting all within one node.
[59:02] And then that's what our resulting glow looks like.
[59:06] And then we're just putting it only on certain areas.
[59:09] And that's a pretty cool result that we just start to feel a little bit more photographic
[59:13] by blowing out certain areas.
[59:17] Now the next thing we're going to do is create some embers flying in the foreground
[59:21] to give a little bit more depth to the image.
[59:23] Because having something really close to the camera is just an interesting trick
[59:26] that filmmakers use a lot and visual effects artists use a lot to give more depth.
[59:30] Especially in these very shallow images where we're very zoomed in on somebody.
[59:34] And so here's what we did in the script before and you'll see it.
[59:38] We have a few of these burning little flakes of embers going in front of the character


### 2D Embers [59:40]
**Transcript (timestamped):**
[59:43] just to feel like there's a fire towards us.
[59:45] And so usually you can do that with a stock element or something like that.
[59:50] But we're just going to create it in nuke with a noise pattern.
[59:53] So you might be familiar with noise patterns from After Effects or sort of generated clouds and Photoshop.
[59:57] Same idea.
[59:59] So we're going to use some noise patterns and just do a very simple still frame
[60:03] since we're doing a still frame.
[60:05] But it'll just get you comfortable using the noise pattern as well.
[60:08] So if you hit a tab and type noise, it's going to give you this node here.
[60:12] And so what we're going to do is we're going to gamma it down and we're going to make the points really be small.
[60:16] Like very, very small like this.
[60:18] We can gain it up to make them a little bit brighter, gamma down.
[60:21] We only want a few of them. We don't want to go crazy with it.
[60:23] And we'll do another noise pattern.
[60:25] So we have another one.
[60:27] And then we'll make that one smaller but not quite as small.
[60:30] Kind of like bigger clouds like that.
[60:32] And then what we can do is take this one and mask it by the other one.
[60:35] So we're going to mask the small points.
[60:37] And so what we have instead of just having a ton of small points is some small points have been like masked out.
[60:43] And you'll have to play with the scale and the size a bit.
[60:45] So I'll just do this real quick and then I'll grab the one I already did because I kind of played with the size.
[60:50] But this will be good.
[60:51] And what we can do is we grade it up.
[60:54] We'll give it a bit of color.
[60:56] So we'll give it a little bit of yellowish orange yellow.
[61:00] And then what we can do is we can gamma a little bit of red.
[61:03] So by doing this separately, multiplying a bit of color and then gamma,
[61:07] the gamma will affect more in the edges because the gamma typically affects more in the shadows and the mid tones
[61:12] and the multiplying gain is more towards the highlights.
[61:14] So we can just pull that in a tiny bit like that.
[61:17] And you know, while it's not obvious here, once we defocus this, it's going to start to look like something.
[61:22] So if you start defocusing these points and making them bigger,
[61:25] we're going to get these sort of, you know, out of focus spheres.
[61:30] And it's not bright enough so we can't see much.
[61:32] So we'll take another grade and just boost it a lot until we start to see something.
[61:37] And you see we have this, which is starting to look interesting.
[61:41] Now, it doesn't look like they're in motion.
[61:43] So what actually happens with something that's out of focus and in motion is it creates a streak.
[61:48] So if we go back to the one that I did, you see how they look more like streaks.
[61:52] And so we need to actually make them move and add motion blur to them so we can create these streak effects
[61:57] and then we will defocus them.
[61:59] So before we defocus, we're going to need to add some motion to these.
[62:03] So I'll just expand the script and we'll continue and we'll do that.
[62:06] So the way we're going to do this, first I'm just going to reduce this a tiny bit more with the bigger clouds.
[62:10] We just want a few of these points.
[62:12] If there's too many, it's going to look, it's going to look sort of chaotic.
[62:16] So I just want a few and then I'm going to put a transform node.
[62:20] I'm going to middle mouse click and so we can see the whole timeline.
[62:23] If you kind of middle mouse click and drag, you'll see like a certain amount of frames.
[62:27] But if you middle click, it'll show you the whole frame range there.
[62:29] I have it set to global.
[62:30] So I'm going to go to frame zero by just clicking it and then I'm going to hit create a transform node.
[62:35] So we haven't talked about keyframing yet, but one thing you can do is you can right click and say set key.
[62:41] And then you can move to another frame.
[62:43] You can move the position and it will automatically create a keyframe.
[62:46] See how it turns blue and then down here it turns blue.
[62:49] Just to make this a bit easier, I'm going to middle mouse drag over these frames so you can just see the frames you're working with.
[62:53] So you see that it moves from those two positions.
[62:56] Now we're designing this shot as a still image.
[62:59] So we're kind of doing a cheat here.
[63:01] And so what I'm going to do is I'm going to move it off the video kind of like this.
[63:06] And then at the end I'm going to move it kind of far away.
[63:08] And so we're going to design everything else on frame five.
[63:11] So what I'm going to do is I'm going to turn the motion blur on by clicking here and saying one.
[63:16] And what it does is it gives a streak.
[63:18] So you see it'll go from our first position all the way to our last one and that's creating the motion blur.
[63:24] And now we'll just continue working on frame five.
[63:27] We'll ignore that this is animated.
[63:29] If we were doing video, obviously we need to do some different things.
[63:32] But this is just to show how to use motion blur, how to do a simple keyframe,
[63:35] and then how we can defocus these to create this effect.
[63:39] Now if they don't look long enough, we can adjust the shutter speed.
[63:43] So that is the setting on the camera on how long an image is being exposed per frame.
[63:49] So if you're familiar with photography, that's what shutter means.
[63:52] And if we increase that, it's going to increase the length of these sort of little embers that we're creating here.
[63:59] So I'm not really reading them very well.
[64:01] So I'm going to increase the brightness, maybe by a lot.
[64:05] So I'll just increase the number by a lot.
[64:07] And they're a little bit yellow for me.
[64:09] I want them to be more orange so we can just add a little bit more color.
[64:13] And the nose that we already did, something like that is kind of good.
[64:18] And instead of doing anything else to transform, if I don't like the position,
[64:22] because this is creating the motion blur, I don't want to mess with this,
[64:25] what I'm going to do is create another transform node, close everything else,
[64:29] and then I'll just move it back over.
[64:31] So now I can play around with that position, find something that looks cool,
[64:36] and just have a few embers that look like they're blowing in front of the camera.
[64:41] And I would probably try to darken specific ones like this one.
[64:45] I would probably darken, maybe I would brighten some here,
[64:47] because I want some more on that side.
[64:49] So I'm not going to spend too much time nitpicking each ember.
[64:53] But if you were to design this and you want to have specific elements that look a specific way,
[64:58] it's worth the time to invest by playing around with these values.
[65:02] And there's no way to just type in numbers.
[65:05] You shouldn't type numbers.
[65:06] You should play around with these sliders and play with the size and play with the amount,
[65:10] just to get, or even the seed.
[65:13] If you play with the Z, it's kind of like adjusting the seed.
[65:17] So we can keep messing around with the different cloud size.
[65:20] So this one maybe looks better.
[65:22] So you see I just adjusted the size of the bigger clouds that we created,
[65:25] and it just gave us a different random sample of points.
[65:30] And that's kind of it.
[65:32] And what you could do, and what I did in my original script,
[65:34] was I did two variations of this.
[65:37] So I broke it off into another direction.
[65:39] So to show this.
[65:41] I had some motion blurring in one way, and some motion blurring in another way.
[65:45] And I merged these two together to make it feel like the particles are blowing in different directions.
[65:49] Because they shouldn't all be flowing in the same direction.
[65:52] And if you had an element or a video, they're blowing in all different directions.
[65:56] So I just quickly did it this way.
[65:58] So you can look at the script and study it.
[66:00] I really recommend doing that to see exactly how I did it.
[66:03] And then I use a frame hold on frame five, which is between the frames,
[66:07] just to make sure that we're on a frozen frame there.
[66:10] So if you want to do a similar effect, I just delete the node,
[66:13] and then we can hit tap and do frame hold.
[66:15] And it will frame hold the frame that you're currently on, so frame five.
[66:18] So if we drag this, they won't move anymore.
[66:21] If we disable it, you'll see that they're kind of sliding around.
[66:24] Which I didn't want to deal with the animation just because we're doing the basics here.
[66:28] And dealing with motion and designing the motion is a whole different process.
[66:32] And so we're just doing a still image.
[66:34] So that's a good point to end the embers.
[66:36] It looks pretty good.
[66:38] You'll have to play around with it.
[66:39] And just to get comfortable, that's the good way to get comfortable,
[66:42] especially with noise nodes.
[66:43] These are really creative nodes, but they're only creative if you play with them.
[66:47] And you just have to play around to get good at doing it.
[66:51] So the next thing we're going to do is add chromatic aberration.
[66:54] We're going to do a very cheap and quick version of that.
[66:57] So there's a node called transform mask.
[67:00] Transform mask.
[67:01] So the mask is on the end.
[67:02] It's not the same as transform.
[67:04] Essentially, what does node is actually used for is moving stuff around,


### Chromatic Abberation [67:07]
**Transcript (timestamped):**
[67:08] but through a roto shape.
[67:09] So that's what it's normally used for.
[67:11] It has a mask input.
[67:12] So if you look at the normal transform, it doesn't have the little triangle on the edge.
[67:15] Whereas this one does.
[67:16] So that's what it's normally used for.
[67:18] But it does give you some alternative options in this extra bar here.
[67:22] This is channels.
[67:23] So if we split this to RGB, we can actually just move one channel.
[67:27] And what that does is it simulates chromatic aberration,
[67:30] which is something that happens when the light is splitting in the lens because lenses aren't perfect.
[67:35] And so you'll notice this on different things.
[67:37] So if we uncheck the green and the blue and what we're going to do is zoom in here.
[67:41] We'll zoom in quite a lot.
[67:42] And in the translate X, we'll say 1.5 pixels.
[67:46] And what this does, if we view it, you'll see that we get this sort of color splitting on the edges.
[67:51] And it's simulating the imperfections in a camera lens.
[67:56] Now, you know, this might be too strong and we might, we might mask it off or things like that.
[68:02] But, you know, people typically will overdo this.
[68:04] It's kind of a trope in visual effects.
[68:05] You see it very, very overdone, especially motion graphics and stuff.
[68:08] You'll see like a ton of this effect being applied.
[68:11] So I think 1.5 is good.
[68:12] You can even mix it down slightly if you didn't want to do exaggerated.
[68:15] But that's a pretty cool effect that we can do.
[68:17] The other thing we can do just before it is we can hit tab and save lens distortion.
[68:22] So that's another node that you can actually get real lenses.
[68:27] And so this is typically used in CG composing workflows.
[68:30] So you want to switch this from undistorted to re-distorted.


### Lens Distortion [68:35]
**Transcript (timestamped):**
[68:35] And after that, you'll want to take this little slider here and just push it up a tiny bit and begin to add some fake lens distortion around the edges.
[68:43] So that's going to add the curvature you would see around a lens.
[68:47] So the piece of glass curves around the edge.
[68:49] And so that's kind of what we're simulating here.
[68:51] The last thing we're going to do here at the end is add film grain.


### Grain [68:54]
**Transcript (timestamped):**
[68:55] So in film cameras, there are grain and in digital cameras, there's sensor noise.
[68:59] So sometimes the term is used a little bit interchangeably, but that is technically correct.
[69:04] So we're going to do just the grain node and there's some presets here.
[69:08] If we zoom in, we can see what it's doing is adding grain over the shot.
[69:11] And there's different size and intensity here for different color channels.
[69:15] So most often there would be more grain in the blue channel than the other channels just because there's typically less light.
[69:21] But we can switch the preset here.
[69:24] So we can do this one.
[69:25] I think the preset GT5274, it looks pretty good.
[69:30] It's like a bit smaller grain.
[69:32] It just looks, yeah, overall pretty nice grain.
[69:35] And that will also kind of cover up any imperfect edges sometimes in compositing.
[69:40] So it's always good to have grain.
[69:41] You always want to have grain for sure because that gives it that kind of film quality that we're going for.
[69:46] Also, you want to make sure to uncheck apply only through alpha.
[69:49] Sometimes you can forget this and that's not good because sometimes an alpha will get carried down this stream.
[69:54] And we haven't really talked about, you know, data going down streams and a little bit more complex subjects, but that is the case sometimes.
[70:00] So we just want to make sure that's also applies to the entire image.


### Write File [70:05]
**Transcript (timestamped):**
[70:05] And the very last node we'll create is a write node.
[70:08] So if you wanted to save this out as a picture, you want to save it out as a JPEG or a video.
[70:13] We didn't do video in this time, but you just want to save as a JPEG.
[70:16] You give it a file name.
[70:17] So we can say file name dot JPEG and it will automatically detect the format, the file type, and we can adjust the quality, for example.
[70:25] If you were to do it dot MLV, it's going to give you the options for a movie file, etc.
[70:31] So that's good to know.
[70:32] Also, we're not doing image sequences yet, but if you did want to set out to save out a set of images instead of a video, which typically loads better and faster nuke,
[70:42] you can do the underscore and then three hashtags and then, for example, JPEG or another file format that's common is EXR.
[70:50] So it would just save out a folder of images instead and you can load those into nuke as well.
[70:54] But that's all just to say those are some different options, but dot JPEG will work if you want to save out your picture.
[71:01] That's about it for this project.


### END + Future Courses! [71:02]
**Transcript (timestamped):**
[71:02] So congrats on getting to the end.
[71:04] Not everyone probably made it through.
[71:05] So, you know, project complete.
[71:07] Big congrats having the guts to push it through.
[71:09] It's not always easy to transition from after effects to nuke, but I promise you it's worth it in the end and the level of composing that you can get to and the complexity that you can really dial in on the details.
[71:19] It's going to be worth it in the end, especially if you want to work on films, if that's your goal.
[71:24] So we do have more tutorials that are available on the channel.



---

## Captured Frames

- [6:20] tutorials/frames/after-effects-to-nuke-1-hour-free-course-compositing-in-nuke/frame_000.jpg
- [13:09] tutorials/frames/after-effects-to-nuke-1-hour-free-course-compositing-in-nuke/frame_001.jpg
- [17:50] tutorials/frames/after-effects-to-nuke-1-hour-free-course-compositing-in-nuke/frame_002.jpg
- [20:30] tutorials/frames/after-effects-to-nuke-1-hour-free-course-compositing-in-nuke/frame_003.jpg
- [24:30] tutorials/frames/after-effects-to-nuke-1-hour-free-course-compositing-in-nuke/frame_004.jpg
- [27:30] tutorials/frames/after-effects-to-nuke-1-hour-free-course-compositing-in-nuke/frame_005.jpg
- [32:00] tutorials/frames/after-effects-to-nuke-1-hour-free-course-compositing-in-nuke/frame_006.jpg
- [43:30] tutorials/frames/after-effects-to-nuke-1-hour-free-course-compositing-in-nuke/frame_007.jpg
- [48:30] tutorials/frames/after-effects-to-nuke-1-hour-free-course-compositing-in-nuke/frame_008.jpg
- [56:00] tutorials/frames/after-effects-to-nuke-1-hour-free-course-compositing-in-nuke/frame_009.jpg
- [61:00] tutorials/frames/after-effects-to-nuke-1-hour-free-course-compositing-in-nuke/frame_010.jpg
- [67:30] tutorials/frames/after-effects-to-nuke-1-hour-free-course-compositing-in-nuke/frame_011.jpg

---

## Structured Notes

### Core Technique
A full beginner onboarding course for After Effects compositors switching to Nuke, built as a single practical shot (a helmeted character composited into a misty forest, with added smoke, fire, metal-highlight glow, foreground embers, and a film-look finishing pass). Structured entirely around "here's the AE concept, here's the Nuke equivalent" comparisons — layers vs. nodes, pick-whip vs. node cloning, adjustment-layer curves vs. Grade nodes — rather than teaching Nuke in isolation, so every technique is anchored to a specific AE mental model being translated.

### Summary
Frame 000 [6:20] shows the base composite (character over a misty mountain plate) mid-interface-tour. Frame 001 [13:09] captures the core mental-model shift of the course: a Roto shape is created disconnected from anything (viewable via the "1"/"A" viewer-input hotkeys even while unplugged), then wired into a Merge node set to **mask** (not over) to cut the character's alpha with the roto shape — contrasted directly against After Effects' single-layer masking. The chapter also covers building a Roto node's RGB+A output to fake a solid, stencil vs. mask inversion, and inserting a Blur node mid-tree so it only affects nodes upstream of it — the core "order in the node tree determines what's affected" lesson. Frame 004 [24:30] covers grading: Grade node's gain/gamma sliders are framed as the fast equivalent of an After Effects adjustment-layer S-curve, with per-channel color wheels used instead of per-channel curve tabs for isolating red/green/blue. Frame 005 [27:30] covers **node cloning** (Alt+K / Option+K to drag a clone-relationship line between two Transform nodes so they share transform values) as the direct Nuke equivalent of After Effects' pick-whip parenting, without pre-comping the layers together. Frame 006 [32:00] covers merging differently-sized, alpha-less footage: hitting T on a Transform node auto-generates an alpha sized to the source format so a smaller/rotated clip (e.g. vertical phone footage) merges correctly instead of showing the default semi-transparent result. Frame 007 [43:30] is the smoke-compositing chapter's key technical point: rather than merging a black-background smoke element with **plus** (which brightens what's behind it — physically wrong), a Keyer node derives an alpha from the smoke's luminance so it can be merged with **over**, which correctly occludes what's behind it, matching how real smoke behaves; color/defocus/opacity are then grade-matched to the plate via a pre-Keyer Grade, a copied Defocus, and the Merge node's Mix slider. Frame 008 [48:30] is the fire-compositing chapter, which reuses the same alpha-via-luminance approach before contrast-matching the plate first (gain up / gamma down on the sky) so the fire has something punchy to sit against. Frame 010 [61:00] is the 2D-embers chapter: a Noise generator node (gamma crushed, gain pushed) is used to fabricate a sparse field of small bright particles for extreme foreground depth, entirely procedural — no stock element. Frame 011 [67:30] is the finishing-pass result after Chromatic Aberration (a masked Transform's per-channel split, translating just the red channel ~1.5px), Lens Distortion (re-distort mode, small push for edge curvature), and film Grain (per-channel intensity, "apply only through alpha" unchecked so grain covers the whole frame including comped edges) have all been layered on top. The Metal Glow chapter (not directly framed but transcribed in full) is a notable technique: a Keyer isolates only the brightest metal highlights, Pre-multiplied, masked to the fire-facing side of the character, run through an exponential Glow node set to **plus** at very low brightness/spread for a tight subtle highlight bloom, then desaturated slightly in that same highlight range via a Saturation node fed by the same keyed mask (with a subtractive Roto shape carved out of blown-out white areas that shouldn't get the effect) — a stack of very small, additive refinements rather than one strong pass.

### Key Steps
1. Understand the fundamental AE→Nuke shift: nodes are separate/branching operations wired explicitly, not stacked layers — order in the tree, not stacking order, determines what an effect touches.
2. Build alpha-driven cutouts with Roto → Merge(mask), not Roto → Merge(over), to punch a hole using one layer's alpha against another.
3. Use Grade (gain/gamma, or per-channel color wheels) as the fast day-to-day color-correction node instead of ColorLookup/curves.
4. Use node cloning (Alt/Option+K, drag the clone line between two identical nodes on different branches) to replace After Effects' pick-whip parenting without pre-comping layers.
5. For alpha-less or differently-sized footage, generate a Transform-node alpha (hotkey T) so merges size correctly against the project format.
6. For elements without a real alpha (smoke, fire), derive one from luminance via a Keyer node and merge with **over** (occlude) rather than **plus** (brighten) — plus is only correct for pure-additive light elements like glow or embers.
7. Grade-match added elements (color wheel nudges, Defocus depth-matching, Merge Mix opacity) before worrying about anything more advanced.
8. Layer highlight-only effects (glow, desaturation) through a Keyer-derived, Roto-refined mask rather than applying them globally, and keep each pass subtle — several small stacked adjustments read better than one strong one.
9. Fabricate procedural foreground depth cues (embers/particles) with a Noise generator node instead of sourcing stock footage.
10. Finish with a standard film-look stack: masked per-channel Transform for chromatic aberration, Lens Distortion (re-distort mode) for edge curvature, and Grain (per-channel, "apply only through alpha" off) last.
11. Output via a Write node — single file (`name.jpg`) for a still, or `name_###.jpg`/`.exr` for an image sequence, which loads/plays back faster in Nuke than a video file.

### Nodes / Tools / Settings
Roto (mask/stencil operations, RGB+A shape-color output), Merge (over / mask / stencil / plus / minus operations, Mix slider), Premult, Transform (alpha generation via T, Alt/Option+K node cloning), ColorLookup vs. Grade (gain/gamma/per-channel color wheels), Keyer (luminance-derived alpha for occlusion-correct compositing), Defocus, Glow (exponential, plus-mode, brightness/spread), Saturation (masked, for selective highlight desaturation), Noise (generator, used as a fake-particle/embers source), Transform used with channel-split + per-channel translate for Chromatic Aberration, LensDistortion (undistorted vs. re-distorted modes), Grain (per-channel size/intensity presets, e.g. "GT5274"), Write (still vs. `###` image-sequence output, JPEG/EXR/MOV).

### Difficulty
Beginner (explicitly framed as an AE-to-Nuke onboarding course) — assumes existing After Effects compositing fluency and translates each concept 1:1, but does cover some genuinely intermediate ground (luminance-keyed occlusion vs. additive merging, node cloning, masked selective grading) by the back half.

### Foundry App & Version
Nuke (non-commercial/free download referenced early in the video). No specific version number stated.

### Tags
nodes-vs-layers, roto, masking, merge-operations, grading, node-cloning, keyer, glow, particles-generator, chromatic-aberration, lens-distortion, grain, write-node, compositing, beginner

---

## Related Tutorials
Shares the Shuffle/channel-fundamentals and multi-pass compositing groundwork with Shuffle and Channel Management | Nuke Compositing [Beginner/Intermediate] (`shuffle-and-channel-management-nuke-compositing-beginner-intermediate.md`) — both are structured as foundational onboarding for compositors new to Nuke's node-based workflow. Shares the luminance-Keyer-driven, occlusion-correct smoke/fire compositing technique with Compositing with EXR Files | FREE VFX Explosions (`compositing-with-exr-files-free-vfx-explosions.md`) — that video applies the same Keyer+Premult+exponential-glow build to a full multi-pass EXR explosion render, a more advanced version of this course's single-plate fire/smoke/glow chapters. Shares the masked, additive exponential-Glow-on-highlights technique with A Senior Compositor's Creative CG Workflow REVEALED (`a-senior-compositors-creative-cg-workflow-revealed.md`) — that video's "2-3 stacked glow layers, never one exponential glow" guidance is the advanced-shot version of this course's single subtle metal-highlight glow pass.
