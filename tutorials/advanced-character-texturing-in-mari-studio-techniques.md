---
title: Advanced Character Texturing in Mari: Studio Techniques
source: YouTube
url: https://www.youtube.com/watch?v=ZWH2RY0eRv8
author: FlippedNormals
ingested: 2026-08-17
app: Mari
version: unspecified
tags: [node-based-workflow, texture-projection, teleport-nodes, roughness, high-frequency-detail, character-texturing, lookdev, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/advanced-character-texturing-in-mari-studio-techniques/
frame_count: 10
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Advanced Character Texturing in Mari: Studio Techniques

**Source:** [YouTube](https://www.youtube.com/watch?v=ZWH2RY0eRv8)
**Author:** FlippedNormals
**Duration:** 25m50s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi, I'm Henning from FlipMummals and in this video I'm going to be showing you my approach to texturing characters in Mari.
[0:08] This is a talk I originally had in Turin at a Vue conference about a month ago and we're just going through the whole thing here, so this talk is publicly available.
[0:16] This doesn't really require any knowledge of Mari whatsoever and it's really more to show my overall workflow when approaching characters instead of highly specific tools and tips in Mari.
[0:27] So with that said, let's get started. As you can see in the interface, Mari is node based and this is extremely helpful when you're working on large characters.
[0:36] Not just is it easier to visualize, it's just easier to reuse different nodes as well. You can make a node friends up here and you can just reuse this in 200 different places if you want to.
[0:46] And if you change this one here, it's just going to update in other places. So nodes are extremely powerful when it comes to texturing.
[0:54] So this is my overall node graph of the whole thing. We have the base color, then we have the roughness and we have additional masks down here as well.
[1:03] And the roughness and the diffuse, they go into a general material. This is an AI standard surface, which is the one that Arnold uses.
[1:11] So you can preview this with some accuracy directly in the viewport right here, which is phenomenal.
[1:17] So this video is going to be in a few different parts. We're going to be going through my overall workflow for painting, which is the core thing for everything.
[1:23] Then we're going to be going through my base color, the teleport masks, the roughness and some additional masks as well.
[1:29] This is a workflow you can use in a professional VFX Studio and this is one I've used many, many times on a bunch of projects before.
[1:35] So we are going to be starting off with my overall workflow for nodes. This is going to seem a little bit complicated, but trust me, once you get a hang of this, this is very simple.
[1:44] It's equivalent to having layers in something like Painter where you have a fill layer here and you have a fill layer on the bottom, which just will have different colors.
[1:53] Maybe this one here is one color. This one here is another color. And you just want this to be the base and have something that is being masked out at the top.
[2:01] So we're simply just masking out this one here and we're painting in this one. So layers are a lot simpler to use than nodes, but they were a lot less flexible.
[2:10] So the workflow here is essentially the same, just with a few more nodes enabled.
[2:16] So what we're doing is we're hitting the tab key and we just type color and this is going to give us a constant color.
[2:21] Like so, if you have the F key, you can just zoom in right away on this. So this is going to be the background.
[2:27] So we are going to go in here and just give this a general background color like so. Make sure this is filled in all the way.
[2:34] If you go down here, it's going to fill with opacity. We're just going to fill this all the way.
[2:37] So just find something that you think would work as a background color. Then we hit OK.
[2:42] And now we have it right here, Ctrl C, Ctrl V to copy paste it. And we can make this be the top one, which is going to essentially is going to color the whole thing.
[2:52] This is the one we're going to be coloring in. Then we select the top and the bottom, hit the M key for merge.
[2:58] And this is going to create a merge node for us. You really need a merge node so that you can blend these two together.
[3:04] So if now we're to view the merge node, you can see that this is going to be displaying only the top one, which looks like this.
[3:10] So we can just go in here, we can change the color. The advantage of this workflow is that you can really change the color and value.
[3:16] So these nodes at any point. Then we are going to hit the P key and we are going to just enable raw data.
[3:23] Just make sure this is a pure raw data node. We go to color and we again, just make sure this here is indeed filled black.
[3:30] This means that whatever we plug in here into the mosque, it's now going to entirely disappear.
[3:35] So we're not going to see only the background node. So plug this into the mosque.
[3:39] And now you can see again, this is exactly the same as this one. So we are only seeing the background node now.
[3:46] The advantage of this workflow is we can have just straight up paint in the paint node and we can bake this down on a B key.
[3:52] And now this has indeed been baked down.
[3:55] If you want to see this in 3D space without just it being flat, we can tap key, tap B, RDF, and we can now plug this into the diffuse slot.
[4:03] And we can just click here. Like I mentioned, nodes are a little bit more complicated to work with.
[4:07] But once you've set this up and you understand the setup, it's really flexible.
[4:10] So the gist of this whole workflow is we can now paint in the paint node, which is right here, which is plugged into a mosque.
[4:15] And this means that we can now make this area here brighter. This looks trivial and this looks like a simple little thing.
[4:23] But obviously, you can just paint this in. You could, of course, just have a paint node and just paint in whatever colors you want to.
[4:28] But the advantage of this workflow is that we can now change the background color at any point.
[4:34] Just go here. We can just change this. So instead of having to go in and grade everything now, we can simply go in and just change the color and the values.
[4:43] If you're painting everything in one simple paint layer, you will have to go in and use tons of great nodes or painting over all this kind of stuff.
[4:49] But this is really easy to work with now. Also, the second advantage is that we now get a mosque and this mosque can be reused in tons of different places.
[4:58] So let's say that this is a character where you're constantly painting areas like the eyes or ears and different channels like the speckler roughness, the diffuse and just tons of areas you need to use the same ones.
[5:11] You can paint a mosque once and you can keep reusing them.
[5:14] So if you want to change your color, you can very easily do that without any trouble. This again sounds trivial, but it's a really, really, really powerful workflow.
[5:21] And this is one we're going to be using throughout the whole video now. So let's delete all of this.
[5:26] And then we're going to be going through my main node setup right here.
[5:31] The next thing I want to talk about is how to project images. This is something you're going to be doing for basically every single character.
[5:36] And it's incredibly powerful. Click the image manager. We can just dock this over here. Hit the pin key right there.
[5:41] And now this is pinned so we can just drag images in here directly.
[5:45] We can find some images in the Explorer. These are some just some really quick images I took of myself and just did a super great in Photoshop, but they work pretty well.
[5:53] So we are just going to be killing the window and then we are just going to be using the window up here instead.
[5:58] So what we can do now is we can use essentially the same workflows I had before where we can have a base color here.
[6:04] Often I prefer to make this a really extreme color so that you can see which parts you project it on.
[6:10] In this case we just can make this pink and then we are going to kill these nodes and then hit the P key and then we just want this to be a transparent node.
[6:18] So we have something just to draw on top of or paint on top of.
[6:21] Remove raw data and then we can just plug this into the over and then we can simply start to project the images.
[6:28] So simply take the image, drag it out like so and we can now go to the side view and we can now straight up start to project this.
[6:35] You can of course do this in other software as well, but the advantage here is you can warp this to a degree that you can't really do in other software.
[6:42] So now for instance we can just straight up start to paint this in like so in areas you want to like so we can just make this flat.
[6:49] So it's a bit easier to see the exact texture. We can also just hit stamp as well.
[6:53] This is going to stamp down the whole thing like so and we can just start to move this around and I can see my really nasty graded skin right here.
[7:01] You can just a warp tool and we can just drag this out over the whole character and this is really powerful because now we can start to really warp this around like so.
[7:10] I really really like this feature because the way Maya works is we have a paint buffer.
[7:15] We aren't actually painting directly on top of the surface. We're painting on a glass pane almost.
[7:21] We can also add more resolution to this and we can just drag this around.
[7:24] Little tip, you can just select a point, hold on the control key and anywhere you can just drag this around like so.
[7:30] So this is a really really handy way to project your textures. You can toggle the grid as well to see this and then we can hit the B key to bake this down and this is going to be incredibly nasty.
[7:39] But it hopefully shows the approach to texturing.
[7:43] We can also just go into the lights and we can just reduce the intensity because this is far too strong now.
[7:49] We can just set this to one and there we go. So what you can do now is you can take the image and you can use this in multiple places.
[7:55] You would probably want to spend a bit more time getting some high quality images like from Texturing X, Y, C or something like that because you don't want to do self-unfotage.
[8:04] Sometimes images like this are actually kind of nice as well because there's a lot of weird variety in them and sometimes that's really nice to have as a base for texturing.
[8:12] So this is something I'm doing a lot whenever I'm texture painting.
[8:15] I'm just doing a base with these images right here and just have something down.
[8:21] So projecting using the Painter tool and then using the Warp tool to really refine it where it is.
[8:28] For a character that's more creature like than this, the Warp tool is phenomenal since you're never going to find images that fit perfectly.
[8:34] So simply projecting onto this is a phenomenal way to do this.
[8:38] Then let's talk about teleport nodes. Teleport nodes are phenomenal.
[8:41] Like we talked about, you can make different masks like this.
[8:44] This is what I often do when I'm starting off a project.
[8:47] I simply paint a lot of masks because I know we're going to be reusing these masks over and over and over again.
[8:52] So ears, T-zones, the eyes, sharp, eyes, broad, lips, nose.
[8:57] We also bring in the displacement as well from Cbrush.
[9:00] So the process here is very simple. You simply paint this.
[9:03] So you can just go in here and just paint and you can move from this.
[9:06] It's very simple stuff.
[9:07] If you see an area that needs to be improved, we can do this.
[9:09] And then if you want to, for instance, bring this in to a different spot, we can go into the beautiful nodes we just painted here.
[9:17] And we can just start to bring this in.
[9:19] So the beautiful thing about teleport nodes is that you don't need to have all the spaghetti that you often have in node systems.
[9:27] Meaning you don't have to plug this into a bunch of different nodes.
[9:30] You can simply teleport them out.
[9:32] So how this works is you select the node you want, hit the tab and you do teleport.
[9:37] And we have two nodes. We have the broadcaster and the receiver.
[9:40] Broadcaster is going to send out the info and receiver is going to receive it.
[9:43] It's almost like a radio.
[9:44] This is a radio tower and this is the actual radio that you're listening to.
[9:47] So broadcaster here and we can just add this to the node and then we can type, for instance, mask, nose.
[9:54] And then in another area, we can go down here now.
[9:58] We can go maybe to the node set we just had.
[10:00] We can do teleport.
[10:01] We can do teleport receiver.
[10:02] And now we can find this node that we just created this mask knows.
[10:06] And now you can see this right here.
[10:08] And this is the exact same data.
[10:09] So this is incredibly handy for building up different masks, which is something we're going to be using a lot.
[10:13] So teleport nodes, absolute game changer.
[10:16] Now let's go over my overall workflow for texture painting anything like this.
[10:21] In this case, we are dealing with the base color.
[10:23] So I often start off with a projected base like this.
[10:27] This is using better images than what I just showed you, but this is still exactly the same process.
[10:31] You're just spending some more time on this and you're really just trying to make sure this is a bit better.
[10:35] I'm just going to make a BRDF material here as well.
[10:37] Just so we can see this in 3D space, a bit easier.
[10:40] So we can just plug this in right here like this and we can just see this by hitting the one key.
[10:45] So you can see what this looks like.
[10:47] Often I'm starting off with a quick projection like this and then I go back to refiner afterwards.
[10:51] Because if you're going to be painting a lot on top after, then you can get away with a lot of different things.
[10:57] Just be sure you don't have any obvious seams.
[10:59] Then I'm going through and I'm huge shifting this to fit the character I want.
[11:04] In this case, I want a really green version of it.
[11:06] Then we're going and we're grading the character just to make it fit a bit better.
[11:10] A lot of this honestly comes from look-to-feedback, meaning I've taken this into Arnold to render and then I'm getting feedback that actually the map is too bright.
[11:17] Then I go back and add a grade node to this.
[11:19] Then we are doing what I talked about before where we're hand painting.
[11:23] This is where we are using a merge node like this.
[11:27] We have a color on top and then we have a mask like this.
[11:30] This is the painted mask. This is what I've actually done in terms of painting.
[11:34] You can see there are some areas that are a bit rough in terms of this, but usually you're fine with that.
[11:39] Of course, I recommend going and fixing this, but a lot of times you don't really see this until you go into the actual mask like this to see them.
[11:46] The advantage here is again that if you go into this, we can now change the paint amount entirely to what we want.
[11:52] We can go in here, we can continue to paint on this like so.
[11:55] If you want to, we can now go in and change the color as well.
[11:59] Instead of having to re-grade this, that can be very painful because you need tons of grade nodes that can be imprecise,
[12:04] we can now very easily just change the actual color like this.
[12:08] We can of course change the amount.
[12:11] If we want to use this mask somewhere else as well, you can very easily do that.
[12:16] The first portion is to do a base, then we grade it, and then we're painting on top of this.
[12:22] Then we're adding some yellows. There's subtle here, but there are some yellows around here.
[12:27] Just add some color variety. Then we're adding some blues here as well.
[12:30] In this case, it's actually a little bit too uniform.
[12:33] What I can do, I can select this mask and I can start to break it up with maybe a mask like this.
[12:37] We can really easily work with feedback.
[12:41] That's one of the advantages of working with a node-based system like so.
[12:44] Addressing feedback is something I find to be a lot easier than a layer-based stack,
[12:48] simply because it's a bit easier to visualise this.
[12:52] This of course could be done in a layer stack without any problem, but in general using nodes in a production is phenomenal.
[12:57] Then we are adding a tri-planer.
[12:59] A tri-planer is a way to add a lot of variety to your textures in a very short amount of time
[13:05] by simply projecting images from three different angles.
[13:08] If we were to click on this one now, you can see that we have some images here,
[13:11] but we can now repeat in different amounts and we can rotate them around like so.
[13:15] It's simply three planes that blend.
[13:18] Unlike a tile that's going to produce UV seams, this is not going to produce these seams.
[13:23] It's going to produce seams where the planes are blending though.
[13:26] If you have a plane here and a plane here, it's going to be a seam in the middle,
[13:29] but usually you can't really see it and you can also change the blend amount of this as well.
[13:35] Then I do a bit more custom painting.
[13:38] This is the one that comes from LookDev where I needed to make this area here a bit brighter
[13:46] and this here to be a bit more pink and also a bit brighter.
[13:49] You can see that it looks a little bit rough in the actual painting, but in LookDev it actually works,
[13:53] which is incredibly important to keep in mind because it's so easy to be focused entirely on what your flat color map looks like
[13:59] instead of being holistic about it and thinking about what does the final result actually look like
[14:04] with lights and motion blur and all sorts of stuff in shot.
[14:07] Then I'm going over and I'm adding a bit of the displacement map into it.
[14:11] As you can see, this is a simple teleport node, which is what we used before.
[14:15] I can simply import this in one spot and I can grain this up
[14:18] and we're just adding a little bit of displacement into the model.
[14:22] You've got to be careful with this because this is going to very easily make the character look dirty,
[14:28] which is not what we want.
[14:30] We just want to help the displacement a little bit like this.
[14:33] A lot of people really recommend against putting ambient occlusion cavities and all this kind of stuff into your textures
[14:39] and there is an argument to this, but it also just helps a little bit.
[14:43] It's a bit of a cheat, but sometimes it can be really nice to do this.
[14:46] And also in characters like this, which is more of an ogre character, he's supposed to be a little bit dirty.
[14:50] Having some dirt in your wrinkles and pores can actually just help sell the look as well.
[14:55] Then we're using texture overlays.
[14:57] This is when I'm deliberately going over the whole character to break it up.
[15:01] You can of course get a lot of variety just with hand painting stuff,
[15:04] but honestly you need some texture overlays just to break this up further.
[15:07] So here you can see that we are using tiles.
[15:09] Tiles are fantastic because they allow you to really quickly just add a lot of variety.
[15:14] You can see though that there are seams here and that is a problem,
[15:18] but honestly oftentimes you can't really tell, particularly when you start to blend it.
[15:22] You can see here now that yes, you technically can see it if you know what to look for,
[15:25] but when you're looking at the character like this, you really can't see what's going on.
[15:29] And if you can see it, then you can go in and fix it.
[15:31] But using tiles like this can really help to bring in lots of variety.
[15:35] You can set this to soft light or overlay or screen and you can just start to blend this in like so.
[15:41] This is a marble texture I got from textures.com years ago.
[15:44] And marble is surprisingly effective at looking like skin with the correct tile amount.
[15:49] And then you can see we're still painting on masks because we don't want this in certain areas.
[15:53] And this is a mask we could again reuse.
[15:55] So we're really using the same workflow as we had in the painting example over and over and over again
[16:02] where we use a merge, then we are painting this out with a paint node going into the mask.
[16:08] Then we are continuing to add additional nodes into this.
[16:11] This is another marble node, which is really handy.
[16:13] It just allows me to get a lot of variety.
[16:15] You can go in and grade this up and down and you can just get a bit more variety into this.
[16:19] And then we're just adding one more image like this.
[16:21] In this case, this image here is something that I straight up painted on top of it.
[16:25] So this is not a tile or anything like this.
[16:27] It is simply painted with the painter tool just add a bit more variety in certain areas.
[16:31] You can see here we have a bit more grunge in these specific spots.
[16:35] And then finally for the color map, I'm going to integrate this map a bit better with the sculpting.
[16:40] So the seabrook sculpt has a lot of pimples and blemishes and such.
[16:45] So what I'm doing is I'm simply polypainting a black and white mask in seabrook
[16:50] that I'm bringing into Mari.
[16:52] So this is where all my pimples are.
[16:54] And then I'm simply adding a lot of variety to this.
[16:57] Integrating the scope of what's happening in Mari is really beneficial
[17:00] because then you're thinking holistically about it.
[17:02] You're not just thinking about the texture map and the seabrook sculpt.
[17:04] You're really thinking about the whole thing as one asset.
[17:07] And this just adds a bit of variety.
[17:09] You can't just paint this.
[17:10] So you have to paint and sculpt this at the same time.
[17:12] And now if you're looking the pure beard, yeah, if you can see that this now looks like a nice, simple color map.
[17:18] There's nothing too fancy about this.
[17:20] It's a fairly methodical workflow that you can keep refining over and over again.
[17:24] And I highly recommend again that you bring this into Arnold or your look-dev solution as quickly as you can.
[17:30] So that you can see this in shot.
[17:32] This all goes into the color channel right here.
[17:34] And I also have a broadcaster here as well, which allows me to use this entire channel in a different spot.
[17:40] Next, let's talk about the roughness.
[17:42] The roughness is almost entirely made out of teleport nodes and the node setup we had in the beginning when I was painting.
[17:47] So we have a base color, which is whatever this is.
[17:51] Then we have one that's darker and then we paint over and then we have a receiver, which is just the nose in this case.
[17:57] Now you're hopefully starting to see the benefit of this for node setup where we can really change this quickly.
[18:02] So now we can very easily change the roughness amount for the nose, for instance.
[18:07] So we can go in here, we can change the color of this.
[18:09] We can now change this to be rougher or smoother right away.
[18:13] This is something I highly recommend doing more procedurally like this because you get feedback on this all the time, particularly when you put this into look-dev.
[18:20] So we keep doing this here and you can see here we have really dark lips and we can go in here.
[18:24] We can change the amount at any point.
[18:27] It's just a really nice and simple method.
[18:29] So the roughness for me is a very soft map.
[18:34] I find that way too many people screwed this up by simply taking the color map, turn this in the black and white and then they're going to be on the way.
[18:41] Let's talk about that real quick. Why that's a terrible idea.
[18:44] We are looking at our color map real quick.
[18:46] What we have are areas that are darker and brighter.
[18:49] We can go down here.
[18:50] We can just check change this illuminance.
[18:52] You can see that around the ears, the eyes, the nose and the mouth and in general spots like this, it's darker.
[19:01] If we simply convert this to black and white map and use this as a roughness map, these areas here are going to be smoother, meaning they're going to be shiny.
[19:09] And areas like this are going to be duller simply because dark means smooth and bright means dull.
[19:16] But this isn't really what's causing something to be dull or shiny.
[19:21] Instead, what's causing something to be dull or shiny would be the overall surface.
[19:25] If you have a surface that is a perfect mirror surface like this, the rays goes in and they go out.
[19:29] So it's a perfect mirror.
[19:30] But if a surface is like this and the rays goes in and out, now it's going to be broken up.
[19:35] And this is what causes the right in the roughness map.
[19:38] It's not if something is black or white.
[19:41] So you have to build a roughness map in conjunction with the height or normal bumper or whatever you want to call it, whatever breaks up your surface.
[19:49] So we're really just building a very simple map like so.
[19:52] And these values here are based around what works in look at them.
[19:56] This is not something I can just intuitively know.
[19:59] We have to plug this into look at them and we have to see what works.
[20:03] And we just keep doing this until we find something that works in terms of values.
[20:07] You have to go back and forth a lot when it comes to this, seeing what values are going to be working.
[20:12] You really can't just know what something is going to look like until you see this in shot.
[20:17] And then we're plugging into displacement as well.
[20:19] This is the same thing as we did before.
[20:20] This is technically not physically accurate because in this case, what we're saying is that the poor,
[20:26] something going inwards will be smoother and something going outwards is going to be a bit duller, but it still helps kind of sell the illusion.
[20:33] So this is one of those things that works, but it's not super accurate.
[20:37] And then I'm doing what I told you not to do where I'm taking the whole color map, the saturating and plugging in the top.
[20:42] The reason I'm doing this at this stage is because it still adds a bit of surface variety, which can be nice.
[20:47] You just have to know what you're doing and you have to test this out often.
[20:51] You can just go in here and just change it intensive to something really low just so you get a bit of breakup.
[20:55] But you don't get the full spectrum.
[20:57] But in this case, regardless of that, it's still my painted maps here from teleport nodes that are doing the heavy lifting.
[21:05] So often this is what a full roughness map for production looks like.
[21:09] You can really get away with a lot of things if you're sculpting is nice or if your high frequency is nice.
[21:14] And then I'm doing the same thing for additional maps as well.
[21:16] This is where I'm tiling a nice bump map around or an old map in Arnold and I just need to have a mask for it so that it doesn't go over the eyes or lips.
[21:24] So we're just painting this in the same way.
[21:25] And this doesn't take a lot of time at all.
[21:28] We're using simple teleport nodes here and just bringing these in right away.
[21:31] And we're doing the same thing for the SSS amount because I need to have less subsurface in certain areas.
[21:37] In this case, I want a bit more on the lips and on the nose and we want a bit more here and we want a bit more on the ears.
[21:45] And we can just really control this and a bit less on a T zone because this is where bones are.
[21:49] Then we export this out.
[21:50] So we can very easily change the value of these ones once we see that we need more or less SSS or more or less spec in Arnold.
[21:57] Then there's a very less thing.
[21:58] I'm going to be showing you how I'm doing high frequency and Mari for this character.
[22:01] I did do this in Seabrooch, but doing this Mari is also really powerful, particularly if you're in a production.
[22:07] So what I have here is a simple standard surface.
[22:09] Just hit the tab key and type standard surface and then just hit enter.
[22:13] We have a standard surface.
[22:14] I've only changed some slight things here like you can change the roughness.
[22:17] So this isn't super shiny like this as many as you see what's going on.
[22:20] And we can also just change the color a little bit and then we go all the way down to the bottom and we change the bump weight to one.
[22:26] And we can change the bump mode to accurate as well, though this makes it a little bit slower.
[22:31] Then I have a paint note, which is filled in with gray and we have a bump channel as well.
[22:37] So this is very simple material channel and a layer.
[22:40] Then I'm using the flip normal face kit, which has a really nice image like this that we can use.
[22:45] And then we can simply just start to paint like so.
[22:47] And you can see how nice this looks already.
[22:50] We get pretty much instant nice pores this way.
[22:54] Now you need, of course, a really high quality map like this.
[22:58] Again, this is why I'm using the flip normal face kit for this.
[23:01] Then we just warp this around and go over here.
[23:05] You can warp this like so and able to grid again, make this a little bit less.
[23:08] And we can just drag this into position like so.
[23:11] And again, since we are painting on a glass paint, the paint buffer, we can erase from this as well.
[23:16] And we can keep warping, keep moving the camera like so.
[23:19] Then we hit the B key for bake and hey, we now have high frequency in this area like so.
[23:24] So this is a really powerful way to do high frequency.
[23:27] You can also, of course, do tile balls as well, which is really useful.
[23:30] But in this case, I'm at least making a base with this map.
[23:35] So we can just go in here and just paint this in.
[23:37] And yeah, just making sure this here is properly done.
[23:41] So I'm just going to be spending a bit more time just doing this.
[23:43] This is really just for demonstration purposes.
[23:45] This is something I would be spending a significant more amount of time on when I'm doing this for a real production over my own characters.
[23:53] So I'm just going in here and just painting this in and just trying to make sure this looks really nice.
[23:58] So the advantage of doing this in texturing is if your model changes, you can very easily transfer this from one model to another.
[24:06] If you do this in Seabrooch and your model changes and you have 100 million polygons, it's really difficult to work with.
[24:13] You can also see how fast that is to simply project this along as well.
[24:17] So using alphas and seabrooch is obviously fast, but here you can really just paint the whole thing over.
[24:23] You can do something similar in Seabrooch, but you really don't have the warp tool to the same degree.
[24:28] And in Seabrooch, this is based on your polycount while in Mari, this is based on texture resolution.
[24:33] And all computers in the world are going to be able to have more texture resolution than polycount.
[24:38] So you simply just get a lot more resolution out of this.
[24:42] So simply doing this, you get a lot more high frequency details into your characters really fast.
[24:47] Now, as a last thing, Mari has a really nice non-commercial version that you can really use for learning and for creating really cool characters.
[24:54] There are some restrictions, but these restrictions are honestly quite trivial compared to some other non-commercial versions out there.
[25:02] So you can really easily paint high quality characters with this version here.
[25:07] So it's phenomenal for learning.
[25:09] So if you're interested in really making high quality characters for VFX production, I highly recommend Mari.
[25:15] For VFX, Mari is used a lot and one of the reasons is because of flexibility with nodes,
[25:20] but also just pure power you can get from Mari, which you really can't get in painter to the same degree.
[25:26] Both tools are phenomenal and it's not really a versus here.
[25:30] It's not really a fight between which one is best.
[25:33] They're both fantastic tools for different purposes, but I really like Mari.
[25:37] I use Mari a lot from a personal use and it's just a powerful and flexible tool.
[25:43] So I really hope you enjoyed this video.
[25:45] Let me know what you think in the comments and let me know if you want to see more Mari content in the future.



---

## Captured Frames

- [3:04] tutorials/frames/advanced-character-texturing-in-mari-studio-techniques/frame_000.jpg
- [7:01] tutorials/frames/advanced-character-texturing-in-mari-studio-techniques/frame_001.jpg
- [8:38] tutorials/frames/advanced-character-texturing-in-mari-studio-techniques/frame_002.jpg
- [9:52] tutorials/frames/advanced-character-texturing-in-mari-studio-techniques/frame_003.jpg
- [13:08] tutorials/frames/advanced-character-texturing-in-mari-studio-techniques/frame_004.jpg
- [17:12] tutorials/frames/advanced-character-texturing-in-mari-studio-techniques/frame_005.jpg
- [19:01] tutorials/frames/advanced-character-texturing-in-mari-studio-techniques/frame_006.jpg
- [20:49] tutorials/frames/advanced-character-texturing-in-mari-studio-techniques/frame_007.jpg
- [22:47] tutorials/frames/advanced-character-texturing-in-mari-studio-techniques/frame_008.jpg
- [23:24] tutorials/frames/advanced-character-texturing-in-mari-studio-techniques/frame_009.jpg

---

## Structured Notes

### Core Technique
A studio-production character-texturing workflow in Mari (a conference talk repurposed as a tutorial, by Henning/FlippedNormals), built entirely around Mari's **node-based** paint system rather than a layer stack: a repeated "background color → paint-node mask → merge" pattern is used for every single map (base color, roughness, spec, SSS, bump masks) so that colors/values/masks stay independently editable after the fact instead of requiring re-painting or re-grading. The talk explicitly frames this as the professional VFX-studio approach — optimized for iterating on LookDev/Arnold feedback rather than for a "finished" flat color map.

### Summary
**Core node pattern [frame 000, 3:04]:** a Color node (background) is duplicated, the copy becomes the "paint target," a transparent raw-data Paint node is masked in, and the two are combined with a Merge node. Painting only ever happens in the mask; the underlying color/value nodes stay live and editable at any time, so a color-note change or a completely different background color instantly propagates everywhere that mask is reused — avoiding the "re-grade everything" problem of a flat painted layer. Baking (B key) flattens a paint node once needed, but the setup underneath stays modular.

**Texture projection & Warp tool [frames 001-002, 7:01/8:38]:** reference photos (even rough, self-shot ones) are dragged into the Image Manager, projected onto the mesh from a side/front camera view via Paint + Stamp, then aggressively reshaped with the **Warp tool** — because Mari paints onto a "paint buffer" (a glass pane in front of the surface, not literally on the UV'd surface), the Warp tool can distort a projected photo to fit a character's geometry far more than projection-only workflows in other software allow. This is called out as especially valuable for creature/non-human characters where no reference photo will ever fit perfectly.

**Teleport nodes [frame 003, 9:52]:** a Broadcaster node (named e.g. "mask_nose") + matching Receiver node let any mask/map be reused anywhere in the node graph without wiring a literal connection across the whole graph — avoiding node-graph "spaghetti." The described production habit: paint a full library of reusable masks up front (ears, T-zone, eyes-sharp, eyes-broad, lips, nose, ZBrush-imported displacement) before doing any color work, since the same regions get reused across base color, roughness, spec, and SSS maps.

**Base color build order [frame 004, 13:08]:** (1) quick projected-photo base for overall placement, (2) hue-shift + grade pass to match the target character's color story, (3) hand-painted color-variation layers (yellows, blues, etc.) via the merge/mask pattern above, broken up further with a second mask if a color read as too uniform, (4) a **Tri-Planar** node projecting a texture from three perpendicular axes to add cheap large-scale variety without UV-seam artifacts (seams instead appear only where the three planes blend, usually invisible) — demonstrated with a plain marble texture, noted as surprisingly effective as a skin-variation base at the right tile scale, (5) **tile overlays** (Soft Light/Overlay/Screen blend modes) for further breakup, again masked out of unwanted areas, (6) a hand-painted ZBrush polypaint mask (pore/blemish placement) imported and blended in so the color map and the sculpt read as one integrated asset rather than two disconnected passes.

**LookDev-driven iteration [frame 005/006, 17:12/19:01]:** repeatedly stressed that map values are tuned by round-tripping into Arnold/LookDev and reacting to how the shot actually reads (motion blur, lighting, etc.) — never by eyeballing the flat 2D map in isolation.

**Roughness map — why "color map desaturated" is wrong [frame 007, 20:49]:** the common shortcut of desaturating the color map into a roughness map is called out as a fundamental error: roughness is a physical property of *microsurface scattering* (a mirror-flat surface reflects rays coherently = shiny/low-roughness; a broken-up surface scatters rays = rough/dull), not a function of albedo brightness — dark areas of a color map (eyes, nostrils, mouth corners) aren't inherently smoother just because they're dark. Correct roughness maps should instead be built from the same teleport-node mask library (independently painted per-region, e.g. rougher lips, smoother nose) tuned against real LookDev feedback; the video does still show a low-opacity desaturated-color layer added *on top* as a cheap extra-variety pass, but only as a minor supplement to real painted roughness values, with an explicit caveat that this is a "cheat," not the base technique.

**Additional production maps:** bump/SSS-amount maps built the same teleport-node-masked way (e.g. more SSS on lips/nose/ears, less on the bony T-zone); a tiled "old-skin" bump texture masked away from eyes/lips using a reused mask; ambient-occlusion/cavity baked into color maps as a deliberate "cheat" that's debated in the industry but can help sell dirt/grime on appropriately dirty characters (called out as valid specifically for this ogre-type character).

**High-frequency pore detail directly in Mari [frames 008-009, 22:47/23:24]:** a simple StandardSurface material with Bump Weight = 1 and Bump Mode = "accurate" (slower but higher quality) is fed a gray Paint node in its bump channel; a high-resolution pore/skin-detail reference image (from the FlippedNormals Face Kit) is projected and Warped into place per-region exactly like the earlier color-projection workflow, baked with B, and produces near-instant realistic pore detail. Framed as an alternative/supplement to sculpting pores in ZBrush — texture-resolution-based detail (Mari) scales with available texture resolution rather than polycount (ZBrush), so it transfers freely across topology/model changes and is generally cheaper to push further than a hyper-dense sculpt.

**Mari Non-Commercial:** the free non-commercial license is called out as fully sufficient for learning and personal character work, with comparatively trivial restrictions versus other apps' free tiers.

### Key Steps
1. Build every paintable map (not just color) from the same reusable pattern: a Color node → duplicate as paint target → transparent Paint node → Merge, so masks and base values stay independently tunable after painting.
2. Project reference photos onto the mesh via the Image Manager + Paint/Stamp, then use the Warp tool to distort the projection to fit the character's actual geometry — critical for any non-human/creature character.
3. Build a library of reusable region masks (ears, T-zone, eyes, lips, nose, sculpt-derived masks) early, using Broadcaster/Receiver teleport-node pairs to reuse each mask across color, roughness, spec, and SSS without literal node-graph wiring.
4. Layer base color: quick photo projection → hue/grade match → hand-painted color variation → Tri-Planar projection for cheap large-scale variety → tiled overlays (blend modes) for fine breakup → sculpt-derived polypaint mask for integration with the ZBrush pass.
5. Never derive a roughness map by desaturating the color map — build it from independently painted, per-region masks reflecting actual microsurface scattering, validated in LookDev/Arnold, not from albedo brightness.
6. Round-trip every map into LookDev/a renderer (Arnold) repeatedly and tune values based on the rendered result in shot (lighting, motion blur), not the flat 2D texture in isolation.
7. For high-frequency pore/skin detail, project and Warp a high-res reference photo into a StandardSurface's bump channel (Bump Weight 1, Bump Mode "accurate") rather than relying solely on a sculpted pass — texture-resolution-based detail transfers across model/topology changes more cheaply than polycount-based sculpted detail.

### Nodes / Tools / Settings
Color (constant color node), Paint (with "raw data" toggle for a transparent paint layer), Merge (A-over-B style blend for the color/mask pattern), Grade, Teleport Broadcaster / Teleport Receiver (named cross-graph mask/map reuse), Tri-Planar (3-axis projection to avoid UV seams), tile/overlay blend modes (Soft Light, Overlay, Screen), Warp tool (paint-buffer-based projection distortion), Stamp tool, BRDF / StandardSurface (Arnold "AI StandardSurface") material preview node with Bump Weight and Bump Mode (accurate vs. fast), Image Manager (pinned panel for dragging in reference photos), Bake (B hotkey).

### Difficulty
Intermediate (studio-production workflow) — assumes basic familiarity with node-based compositing/texturing concepts (masks, merges) but is explicitly pitched as not requiring prior Mari knowledge; the value is in the professional workflow philosophy (reusable masks, LookDev-driven iteration, correct roughness theory) more than in specific tool mechanics.

### Foundry App & Version
Mari (non-commercial version usable for the same workflow). No specific version number stated. Renders/previews shown via Arnold's AI StandardSurface.

### Tags
node-based-workflow, texture-projection, teleport-nodes, roughness, high-frequency-detail, character-texturing, look-dev, intermediate

---

## Related Tutorials
Shares the node-based Color+Paint+Merge mask pattern, Teleport Broadcaster/Receiver workflow, and Triplanar-projection technique with Introduction to Mari for Complete Beginners - 1 Hour Quick Start Guide (`introduction-to-mari-for-complete-beginners---1-hour-quick-start-guide.md`) — that video teaches these same fundamentals from scratch (interface, paint buffer, node graph basics) as the on-ramp to this video's production character-texturing workflow.
