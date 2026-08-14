---
title: Build Entire FX with ONE Pass - Nuke Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=WBqp4UbqPJ0
author: Voxyde VFX
ingested: 2026-08-11
app: "Nuke / NukeX"
version: "not specified"
tags: [compositing, cryptomatte, st-map, merge, channels, aovs, grading, gizmo, procedural-texture, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/build-entire-fx-with-one-pass---nuke-tutorial/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Build Entire FX with ONE Pass - Nuke Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=WBqp4UbqPJ0)
**Author:** Voxyde VFX
**Duration:** 56m50s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Without a doubt, one of the most versatile AOVs or render passes that you can always include in your CG render is going to be the World Position Pass.
[0:14] This pass is an absolute banger. You can do so many things with it. And in this tutorial, really, I'm just going to cover some of the techniques.
[0:24] There's still a lot of things you can do with it outside of the techniques that I'm going to show you. And really, when we look at our World Pass, so in this tutorial, we're going to go from this render, this very simple flat looking render to this result that we have here.
[0:40] So if we take a closer look, we can obviously see there's this big ball setting circle happening around our logo. But there's even a lot of extra detail added into our actual 3D object. So if we look one more time at our base render and we compare it with the end result, we can see that we added some noise, some scratches, even a little bit of extra noise only on certain parts of the render.
[1:08] So really, there's a lot of stuff you can do at the base level. If we just look at our base render, if we just inspect our position pass, really, it's just going to store for each pixel the World Position of that pixel in 3D space.
[1:23] So this information by itself is not really helpful unless we use these elements, this information in certain ways, which I will show you with this tutorial.
[1:34] And hopefully by the end of this video, you will also have maybe a better understanding of the powerful workflows which we can do in Nuke. We don't really have to do everything in 3D. I know that a lot of our students, a lot of viewers watching this channel are mainly dealing with 3D and mainly Houdini.
[1:52] But I will highly encourage you to give Nuke a shot. You can get the free non-commercial version of Nuke, which has very few limitations. And in fact, you will be able to follow along with this tutorial and get this result yourself.
[2:04] You can download the project files. I will include this render as well and a couple of textures that we'll be using. So if you haven't already give it a shot, it will 100% I will guarantee that it will level up your game.
[2:16] It will make you a better 3D artist by knowing compositing, by knowing how the Nuke workflow goes. It will just help you overall see things better, know ahead of time what can be done in comp, what can be done in 3D, because everything done in comp is going to be a lot faster and a lot easier and with more control a lot of the times.
[2:36] And this effect right here that we have this pulsating circle gradient thing, I actually did this exact thing in production. I received a 3D render of the CD and I was supposed to do this kind of effect in Houdini.
[2:49] But I got away with just doing this in Nuke and it was super fast to set up, super fast to render. So a lot of these techniques are also very crucial in production, especially if you're a freelancer, if you're working maybe in a smaller studio.
[3:02] The turnover for projects, the deadlines are a lot shorter, so these techniques can be really life saving. Anyway, give Nuke a shot, enough rambling. Let's start from the beginning. I will just start from the base render here.
[3:15] I'll just copy and paste this over here and recreate this entire chain. Actually, before we do this, let's just inspect all of the different layers that we're going to create. So we start with the base render and we just split the AOVs and recreate the beauty.
[3:29] We have two AOVs just so we get the reflections and the diffuse. Then our first layer is really going to be our first pass for some noise. So we already can see some breakup in our texture.
[3:42] Then using the world pass, we can map a costume texture which we have, which is just a scratches texture, which looks something like this. We'll map this using the world coordinates onto our objects moving forward.
[3:56] We will have, let's see, just a quick color correction pass. And actually before our color correction, let's just look at this pass. We can see that on the lowest level of this 3D object.
[4:08] So this is really just a texture, by the way, this entire 3D scene is just one texture which I created in cops in Houdini. This is actually a lower quality version of the texture that we'll be building in our next workshop coming soon.
[4:23] Motion graphics in Houdini, so stay tuned for that. We are still currently adding stuff to the workshop, so it's going to be pretty big with a lot of different stuff.
[4:31] So if we go back, we have this added texture on top, which we can see here. And this is to show how we can isolate certain regions of our render.
[4:41] In this case, like I mentioned, kind of like the floor of our 3D objects. If we go forward, we add our indirect emission backs. So this is pretty much just from our original render.
[4:53] If we move forward, we have just a simple setup for our logo, which looks something like this. Again, really just mapping a texture using the world position, isolating it with the crypto mat, combining it with some passes and some glows.
[5:08] We get our emissive logo on top. And then finally, we have our first layer. Now, this is really just a simpler version of what we will actually create for our circle pulsating effect.
[5:22] So this is kind of like a fake global illumination of that version. We can ignore this for now. This is what we will end. This is really what we will end at the end.
[5:33] Moving forward, we have a distortion layer based on our pulsating effect. And really, we can just move on to our pulsating effect, which looks something like this.
[5:44] If we break this layer by layer, we have our original gradient here. We break this up with some coloring and some separation here. Then we actually break it up with some noise.
[5:55] We add some god rays on top of this. We add some glow. And then we just plus this on top. And this is how we get our final effect.
[6:03] So with that being said, this will be a quick overview. And now let's start over right in the beginning. We will start with our render. Let's do a shuffle here and recreate our main beauty.
[6:15] In the label, I will place the value in one expression, which we can use to filter out in this case, our combined diffuse dome. Let's do a merge and let's do a dot here, duplicate this with LC and let's connect this over.
[6:32] Now, if I'm going a little bit too fast, let's set this to plus and our second shuffle here should be combined glossy reflection dome.
[6:41] If you haven't already, take a look into our free intro to nuke for 3d artist course where I start from the beginning and go over what all of these shuffle nodes are what they do, some basic shortcuts, the basics of a beauty rebuild and also a lot of stuff that you can do with the passes.
[6:58] So that course, if you haven't taken it already should really be your first exposure to nuke and it's free part of our intro series. So no reason to not take it. And now going back to our setup here, we have our basic beauty rebuild.
[7:12] I only added a dome light. Obviously, I could have spent a lot more time making this actually good in 3d. The better your base render is, the better your overall result will be obviously.
[7:24] But in this case, I wanted something simple in 3d so I can showcase the dramatic effect that compositing can do for us. So right away, the first thing that we can do is break up this texture and we can use a if I drop here a P noise advanced.
[7:40] This node is a custom gizmo. You can find this on eucopedia or if you have installed the new survival toolkit, this will be included in the toolkit. I will highly recommend that you install the entire toolkit or if you just want to grab this gizmo quick, you can find this on eucopedia.
[7:57] Now I'll do a postage stamp and point back to our render. This is like an object merge in Houdini. Just so I can start organizing things a little bit and we can hide the wiring with alt H. Let's go ahead and connect this over.
[8:11] And if I set the position data here, we can set this to P, which is our world pass. And we can see already that we have a noise mapped onto our geometry. This is using the world position data to create rather to generate this noise pattern.
[8:28] So this is already one of the things that we can do. Although two layers of this noise. Let's first start with just merging this over with a multiply. Obviously, this is a little bit too strong. I can couple this with a grade node and I can increase the gamma here.
[8:44] One something a little bit more subtle. So this can be our large pattern noise. We can also play around with our seed if we need something differently. And our size here size should be a little bit larger. And we'll just do another version of this. I'll press I'll see to duplicate.
[9:01] And for this one, let's do something a little bit rougher. I'll increase the gain here, maybe decrease the size. Let's try something like this. And we can, and we can do another merge here. Let's set this to multiply and let's already check the result.
[9:17] We can also decrease the mix value here if we want, or we can maybe go back to our grade node, increase the gamma, maybe let's try something like this. Let's maybe introduce even more noise, make this a little bit grungier. We'll do something like this. Obviously, you can use your own grunge texture.
[9:37] It will probably have a different result. And with the next step, I will actually show you how you can map textures using this position data. So we know we have the SD map. And in this case, we also have UVs on our passes here. So it's probably we should use the UVs to do this kind of thing.
[9:58] But let's say that, for example, maybe we don't have access to the UVs, we forgot to add them or our 3d artists didn't include them, but they did include the world position. What we can do is we can just set our red value for the UVs. We can just set this to be our X coordinate.
[10:17] And for the green value of our UVs, we can just set this to be our Z coordinate. So we will get Z and X, and we'll get this nice spread. Now, this technique doesn't really work if we had a lot of debt on our scene. So if our this only works, if I go back to the RGB view, this only works because we don't really have a lot of height on these elements.
[10:41] So we will see that on these parts over here, where we have our height, it only works on the X and Z directions. And it kind of breaks a little bit on the Y. In this case, it's going to be fine. And we can do a separate setup to get our Y coordinates as well. But we don't really have to go that far for this example.
[11:00] But anyway, let's do another postage stamp. Let's point back to our render. And from here, we will do a shuffle. Let's hide the connection. We want to do a shuffle on our P value. And we'll grab, like I said, the X will become our red channels and not the Y, but the Z value will become our green channels. And we don't need blue or alpha.
[11:25] And this now becomes our UV coordinates. We can see we have green and red values. And I'll go ahead and just grab the texture that I use this scratches texture, which I will also include with downloads if you want to use this as well. This is also something that I build really quickly in cops in Houdini, super handy for these kinds of things.
[11:44] Let's make sure that this is set as a raw data. And we only have one channel here, the red channel. This is why it's all red. Let's do a shuffle. And let's grab the red and populate our RGB channels by holding down alt. And actually, I'll get rid of the alpha. Don't really need the alpha for what we're doing here. Let's plug this. So this will be our source. And I'll point the ST map to our coordinates here.
[12:14] For the UV channels. These are now the RGB values. So here we'll just set the UV channels to RGB. Now we can see that it kind of works at only a certain part. And this is because the ST map really prefers working, we can see that if I were to sample this area, we have negative ranges. The ST map really prefers ranges only from zero and one.
[12:37] So what we can do to repeat the texture and have only positive ranges, first of all, we can just add an expression. And to get rid of the negative ranges, we can just do an absolute function on our channel. So here we'll do apps. And in between parentheses, we will just do our so this will be our red channel. We can see this is this kind of mirrors the red channel.
[12:58] And we need the next hour green. So we will do an absolute function on our green values as well. And if I go to the ST map now, we can see that we have kind of mirrored our texture. So this is how we can achieve this kind of look. We can also remap or affect the tiling here. If I do a grade node and let's make sure that the grade node by default comes with the black clamp on this completely ruins our ST map.
[13:24] So make sure to uncheck this. If I now increase our gain value, we can see that we can affect the tiling. But at a certain point, the values go above one at around this area here. If I were to just preview the values, we can see that if I sample this area, we have 1.6 for our red values.
[13:43] So again, the ST map once values between zero and one, we can do a simple expression here, we can just say instead of our, we will do our module also percentage sign one. So this means that whenever our red values are above one, they will kind of reset back to zero.
[14:01] So 1.6 becomes 0.6 and 2.6 again becomes 0.6. And let's do the same thing. G let's do a percentage sign one. So G module one. And now hopefully we can see that we can safely retile our texture however we want.
[14:20] We don't really see a lot of that tiling problem that I was talking about earlier with the Y coordinate. It would only be noticeable if our kind of like our cubes were really tall.
[14:31] But anyway, from here, we can if we just merge this over with a plus operation, for example, it doesn't really look all that convincing. And this is because usually with plus types of operations for the textures, we want to reuse our main light in the background.
[14:50] So I will just add another dot over here to grab our render. I will do a grade node with G. And I'll just increase the contrast here. Let's do something like this. And let's multiply this over our stretches.
[15:06] So I'll multiply this we have this. Then when we plus this over, we will have our lighting information back into this channel.
[15:13] Now, probably we can increase on our grading here, we can maybe bump up our values here slightly, or we can even do this after the SD map, we can even increase the values here and try to bring back a little bit more of our
[15:30] scratches. Let's maybe do for the scratches, I kind of want them to be smaller. So hopefully this will make our scene feel a little bit more massive. So just increase our tiling here, we'll do something like this. And let's play around more with our brightness.
[15:47] Maybe try to find a cool balance here. But already we can see with these adjustments, we add a lot of personality and detail to our scene. Now, obviously, this is just our direction, you might not want this to be as grungy and as kind of like rough, but it is to showcase some of the examples that you can do with the
[16:07] world pass. Now let's map one more texture. Let's duplicate the setup that we have here, duplicate all of these nodes with all C, we'll have to reconnect our postage stamp. So let's point this back to our render. And let's bring our next texture, which should be this kind of like the cells pattern that I have here, I will just copy and paste this node over here.
[16:30] And I'll just replace this in the shuffle. So this goes here, our shuffle makes everything black and white. And if we just look at the result, we should have already the same kind of tiling that we had earlier, which is great. Let's leave things as they are for now. And if I just want to multiply this over, we can see that this will quickly erase, take over most of our scene, probably here we'll need to increase our gamma. So it's not as noticeable.
[17:00] So this is a decent result as it is. This is again one of the things that we can do. But let's say that I only want a little bit of breakup, I just want this to appear on the lowest levels of our scene. So from our render here, our poster stem will do another shuffle, we'll grab our position pass. And we don't really need any connections here, except we will plug the y value. So the height of our objects will plug this inside
[17:29] the alpha. If I press a we let's, we don't kind of we kind of see a little bit of this I'm not sure how noticeable this is. But let's do a great node, let's set this to run over the alpha. And let's remap our value. So if I decrease the white point, this is kind of like a feet range in Houdini, if I decrease the max value that we have over here, hopefully we can see that we can start to isolate certain parts of our render. So now we only have a we have a black mask over the lowest
[17:59] level of our texture. When you do things like this, it's always really cool experimenting with the offset which kind of pushes the entire gradient along the values here. In this case, it's not necessarily will set this back to zero. But now that we have this, let's use this as a mask in another grade node here. So let's go back to RGB view by pressing a I'll do another great node with G point the mask to this message that we just created. And if I
[18:29] were to set the gain here to zero, we can see now that our texture only exists on the lowest floor and we can go back to our grade and adjust exactly how this happens. Maybe this is where we can play around with the offset and maybe we can push this texture further down and maybe include a little bit of these other blocks around the floor as well. So we can do something like this.
[18:51] This we want as a multiply operation, but we don't really want to affect the parts that aren't coming through from our mask. So we can also do here we can grab the mask of this merge and point this back to our grade that we had over here and will set the operation to invert. And now we can see that this texture will only affect with a multiply it will only affect the lowest level of our floor. And now we can go back to our
[19:21] texture here in our grade, and maybe we can increase our gain and maybe bring back some of the contrast with the gamma adjustment. And this is the result that we get and probably I can maybe make this a little bit sharper even play around more with our offset. So hopefully if I decrease the offset I'm kind of bringing the entire texture up, we get something like this. And I think this maybe too much contrast.
[19:50] We can go back and readjust and these are now the options that we have and we can see that with this extra layer we just add a little bit more break up in our materials. I can go also back to our tiling here and I can tell this even more.
[20:05] I can make this a little bit smaller here have some higher frequency detail across our scene. Again, we can do this. We can also just color this differently if we really wanted so I can give this
[20:17] a different color and we have something like this actually this looks pretty cool. I'm probably going to use this in the final render result as well. This is actually really cool. I probably should have done this from the beginning. So this is with and without the grade.
[20:33] I think this is cool because it adds a little bit of color break up as well. It's not this entire area full of gray. Maybe I can now go back to the offset here. Maybe bring this further up if I want to.
[20:48] What I think you get the point by now let's do something like this. Maybe make this blue a little bit more subtle with the mixed value. So this should be okay. And in the original render I added a color correction node. We can add this with C.
[21:04] I just went to the shadows here and in the gamma I just reduced the red channels and increase the blue. We get something like this. Don't worry we'll adjust this in a second but we'll set this here and then in our ranges. I can also maybe play around more a little bit with our midpoint here.
[21:22] And I will just reduce the overall mix value just so we get a little bit of a subtle blue coloring in the back here. And maybe I can just go back to the beginning and in our reflection domes we can actually start making a little bit of adjustments here as well.
[21:38] Maybe pump in a little bit more gamma if I want and for the other one. I think this should be okay. Maybe this is too much contrast. Our other gamma. We'll do something like this. Now the next layer that we can add here we can add back only our indirect emission passes. So we can just grab one of these shuffles. Let's copy and paste this over here and we'll point back to our render. So I'll just grab this and I'll shift select the shuffle here. Press shift Y.
[22:08] And we can also create a forward connection and maybe we can do a postage stamp in between and then alt H to hide the connection. And here we want to...
[22:18] Here we need our... It really should have been in the combined emission but the way Karma does things it didn't give me this layer here but if we look in the combined diffuse we have the emission showing here.
[22:31] So now if we just duplicate this shuffle and we connect this over I can grab only our dome contribution of the combined diffuse. So we have this and then we have this. And from this if we do a merge between these two layers I can set the operation here to difference and extract just the contribution of our light.
[22:49] So sometimes I had to do this as well because I just couldn't get the emission to show up properly in the passes and we'll do the same thing for our reflections as well. So just duplicate this entire setup and we'll select here our entire combined lossy reflections and then we'll just select our dome light contribution.
[23:09] So we have this and this. The difference will be this and now we can just merge these back together. We'll set this to plus and we have our indirect emission. And this layer will just merge on top with a plus operation.
[23:24] So this here to plus and maybe make a little bit more room. And for the colors here let's add a grade node for our diffuse one. Maybe lower this slightly and I also want to lower this for our reflections as well. But maybe actually let's bring this back for our diffuse. We'll do something like this and something like this should be okay. We'll probably have to come back later to these values when we add our...
[23:52] When we remake our logo as well. But for now this should be okay. So we can actually set up our logo right now. Let's do another poster stamp same deal. Actually what we want is the same kind of texture that we used here with the cells.
[24:10] So we just want to duplicate this setup one more time. Let's alt C and duplicate this over connect this back to our render our poster stamp. So this is again select this select this with shift shift Y will create a forward connection.
[24:26] So this is our tiling. We want to isolate this only on our logo. So I included a crypto matte pass for this. I'll point this back to the render and I will control select the logo. Let's maybe control click until we get this turned yellow and then we have the alpha for this. So after this grade we can do a merge point this to our crypto matte. Let's make sure that we are in RGB view and operation here should be I believe out.
[24:54] I can never tell. Let's maybe try in. It's either in or out if you want to isolate the element with the alpha of the belayer. So this is looking okay. We will probably have to readjust our grading here for the texture. We can also go to our tiling here. Maybe change this a little bit. Make this smaller. Another thing that we can also do is if we want to move our texture around we can also play around with the offset if we want kind of like a different seed different placement.
[25:24] Of this texture. It's also something that we can do but I'll just actually leave this at zero kind of like this mirror pattern that we get. It's kind of interesting. Now one more thing to make this texture a little bit more believable a little bit more 3D. We can just grab a shuffle node which we can point back to our render.
[25:41] And here I've also included an ambient occlusion layer. So this is going to be the AO drag everything over to connect to RGB view or other channels. Let's do now a multiply from our texture. We'll multiply this with the AO and we can see that this is the result if I reverse the order with shift text. We can see that this is now from our ambient occlusion. So now this feels a little bit more 3D. So this should be okay. We can just color this and give this some glow from here. Let's do a great.
[26:11] And we'll set the blue values to zero and maybe just remove a little bit of green. We'll do something like this. Let's do a crop and we'll use AP glow.
[26:23] AP glow you should be familiar by now I use this in all of my Nuke tutorials. So this is my favorite exponential glow. You can get it from Nukeopedia as well. And it also comes in style with the Nuke survival toolkit.
[26:39] So we'll also combine this with a saturation here maybe make this a little bit more pale and we'll just merge this on top. We'll set this to plus. Here we can also something that I didn't do in the original result. We can also add some God rays but we might come back to do this later.
[26:57] But let's just merge everything on top of our main chain. We'll set this to plus and we might need some color adjusting here. Let's maybe just go to our texture and maybe I'll just bump up the overall intensity here. Try to get a cool result. Let's do something like this.
[27:17] Pretty okay with this. Maybe not so much contrast. I'll increase the gamma. Let's do something like this and we can come back now to our global illumination pass here the indirect emission and maybe reduce a little bit of the brightness right around our logo. We'll do something like this.
[27:37] Another cool and super simple thing that we can do to add some life into this render is if we grab our indirect emission pass. Let's do a great note here. I will lower the gain value to something like 0.3 and I want to flicker this mix value on and off. So we have a little bit of this flickering throughout our animation and we can just hook this up with an expression. If I click over the value and press equal sign will grab an expression here and expression will be random.
[28:06] And in between parentheses will do here frame and let's divide this by five. The more you divide this the larger the division number here is the slower this will be so five in my case was a pretty good speed. If you want this to flicker faster you will just use a lower amount.
[28:24] And if we catch a few frames we should see a little bit of this kind of like movement on our on this pass. And we kind of want the same thing for our logo as well. And we want the same values here. We can do a great note. Let's maybe add this directly on our texture here which kind of controls the overall intensity.
[28:50] And I will just copy and paste the same expression. So if we go back here let's grab this and let's also paste this over here. And because this is based the seed of the random is based on the frame we will have the exact same flickering happening. If we wanted a different seed we would just have to add a value to our frame. We will do something like this to get a different seed. But in this case we want the exact same value.
[29:15] And if we go to our final result let's maybe let's instead gain this up so it kind of like flickers more intense but probably this is too much. Let's do something like one point fifteen should be okay. And now we have this flickering as well. So now we can finally move on to the actual effects layers which will be the pulsating circle. We will again start with a poster stamp. Let's head over back to our render link these over.
[29:44] And what we need essentially is just going to be a gradient across our 3D scene. Now we can do this based on the world position pass. We can do this with AP met again. This will be from new copedia with the new survival toolkit. Go ahead and grab this note as well.
[30:03] By default the image here will be set to be our world position and based on our coordinates we can generate kind of like a very simple way that we can get the distance in Houdini. This is kind of like a distant node based on our zero zero zero world coordinate. If I press a we should see this gradient. If I were to decrease our radius we can see kind of like this distance node which is exactly what we need.
[30:30] And we'll set the fall of here will leave this as linear and we'll just increase this until we grab all of our or rather most of our geometry here. And once we have this one to zero gradient we can just simply remap these values. If I were to we can remap the values with an ST map node. So this will be our ST map. We want to grab the alpha we just have an alpha here so we will set the UV channels to the
[31:00] look on our alpha in our AP met and let's press a go back to RGB view and I will just create a very simple ramp over here and we want this ramp to be horizontal and so I will just grab this zero point the black point I will set this over here and this one over here and I will just set the X value here to zero and we can set the Y coordinate here. Let's also keep this at zero.
[31:26] Let's set four point zero the Y coordinate to be zero as well. And this X coordinate here this really should be the our entire way. So we can just set this to 1920. And now with this ramp this one to zero value that we have laid out straight over here horizontally will be now will now become our values from over here. So where we have one on our ramp we will get one on our gradient here as well. And this will just make sense when we plug this over. So the source will be our
[31:55] ramp. Let's head over back and now we can see exactly what's happening. Let's make sure that we are not in the alpha mode we are in RGB mode. So now for example if I were to grab a grade node on our ramp and I were to decrease the gamma here. If I look at the result now we can see that this affects it over here. So not super useful so far but if we add another grade node on our alpha here from the AP met I'll set the channels to affect only our alpha.
[32:23] I will remove the black clamp and what we can do is we can expand our distance here or not rather expand but we can push this out or in with this offset value. So when we do this and we preview the result over here in RGB view and I go back to the grade node.
[32:42] We can see that as I increase or decrease the offset we can also affect our mapping here. And what we want to do is simply repeat our values. Let's head over back to this grade node press a when our values from the offset. We can see that as I expand this further our values go above one. So here we have a value of 8.1.
[33:05] We can repeat the values back between the zero and one ranges in the same way that we did for our UVs. Whenever we want to remap values to be only between zero and one we can add an expression.
[33:19] And in this case we want to affect the alpha. So here we'll do alpha. It's actually going to be underscore a.
[33:27] Let's do a percentage sign one. So a module one we can see now that our pattern repeats and as I push our offset out we will just keep repeating the same gradient.
[33:38] And now this gradient will be remap with our estimate. If I go back to RGB view and finally increase our offset. Now we can see we get exactly the result that we are after.
[33:49] We can now control our ramp a little bit better here with some gamma adjustments. Maybe I can drop this even further down or I can even go back to our ramp here and I can make this entire ramp maybe a little bit shorter.
[34:03] We can see this now in our estimate and but probably I want to control this with our gamma. We can even control this with our black point and our white point.
[34:14] We can do something like this. And in the original example I just overlaid a couple of these layers. So I wanted one that gives me kind of like a field look like this.
[34:23] And let's just do another gray note for the same ramp. And here I want to squeeze things really close to the end.
[34:32] So let's actually leave the white point as one and I'll just increase the black point here and maybe the gamma as well. And let's just merge this on top.
[34:40] So we have set this to plus. We have a nice sharp leading edge and we can also see this now in our main effect.
[34:49] And we'll just go back over here and we can play around more with our colors and these adjustments will probably come back to.
[34:58] So after we add the rest of our setup.
[35:01] But now if I just animate the offset value here we can either keyframe this or we can just add an expression here.
[35:08] Let's do equals and let's do let's give this frame divided by 50 maybe.
[35:16] Let's hit play see and check the speed.
[35:20] I think 50 is what I used in the original example.
[35:24] So I'm pretty OK with this speed. This looks pretty good.
[35:28] We can also maybe see that the time gap between the pulses is maybe a little bit too long.
[35:34] So I might want to increase the frequency.
[35:36] Easy way that we can do this is really just duplicating the grade note that we have over here.
[35:42] Let's see to duplicate this note.
[35:45] I'll drag this over here and this layer this version of our grade.
[35:50] We can just we can just use a different value in the offset here.
[35:54] So if I do equals we can push this forward by just adding to this value.
[35:59] So in this case I want this to be halfway in between completion.
[36:03] So we'll just do here plus 0.5.
[36:05] And if I now merge these back together let's set the operation here to multiply.
[36:12] And if we go back to our SD map we have now this result.
[36:15] And let's press play.
[36:17] And this is how we can add pulses in between each pulses.
[36:22] I'm not sure if this is too fast.
[36:23] But another way that we can control the frequency is if we go back to our APMAT.
[36:28] We can simply increase the original gradient on which this entire effect is based.
[36:33] So if I were to increase our radius here we really just expand our original circle.
[36:40] And this will also affect our frequency as we can see.
[36:44] But probably the speed is still we just have too much speed here.
[36:49] Let's maybe just lower the speed by half.
[36:52] So I'll just go inside the first grade node.
[36:54] And if I want this lower I'll just increase the division amount.
[36:58] Let's do divide by 100.
[37:00] And let's also make sure that it's the same value over here in our duplicate.
[37:05] And hopefully now this will be a little bit more manageable.
[37:09] So between increasing the gradient and increasing the time division here
[37:14] we can control the frequency, the size and everything.
[37:18] So this is really our directable.
[37:20] And I think this is slightly better.
[37:22] Probably it's still too fast.
[37:24] I would say we would just have to increase this to 150.
[37:27] So I'll leave this up to you.
[37:29] Now from here we pretty much have the base of what we need.
[37:32] It's only going to be a matter of fitting this more into our shot.
[37:37] And one of the things that I want to do is to kind of like have this circle
[37:41] appear as if it's spawning from our logo here.
[37:46] So I kind of want to mask out the logo.
[37:49] We can do another crypto mat back to our render and we'll grab our logo one more
[37:55] time and here we'll just do a grade node point this to our crypto mat and also
[38:00] the gain value to zero.
[38:01] So now this is masked with our logo.
[38:04] Let's see what other things we can do here.
[38:08] We can already we will want to break this up with some noise, of course.
[38:14] And we can let's do another dot over here.
[38:19] Maybe we'll do something like this and we'll use our P noise advanced.
[38:23] Point this back to our render point this back to the position.
[38:27] And we have our noise here.
[38:30] Let's maybe see the settings.
[38:34] We'll do something like this and we'll just multiply this over our gradient.
[38:38] So we'll set this here to multiply.
[38:40] And at this point, we already have a lot of elements.
[38:43] Let's maybe do a grade node.
[38:46] I'll want a couple of grade nodes because one of these I will want a sharp outline
[38:51] on our leading edge here.
[38:54] And for this one, I kind of want this to be a little bit more subtle.
[38:58] Let's go ahead and also I want to color this individually.
[39:02] So this layer, this base layer, I'll set the color here to a nice orange.
[39:08] And I'll just merge over our leading edge with a plus operation.
[39:12] So we have something like this.
[39:13] And now from here, we can start adding our God rays.
[39:17] So we'll just do a God rays node.
[39:19] I'll drag this over to the side.
[39:21] Let's go ahead and we'll just want to affect our position here.
[39:25] We'll set the Y position to something like 100 and maybe just use our scroll.
[39:29] We'll now to increase this further.
[39:32] We'll set the steps here.
[39:33] Let's increase this to 10.
[39:35] And let's set the two color here.
[39:37] We'll set this to zero and we'll just increase the gamma.
[39:39] So we have the nice fade in.
[39:41] So with another grade node, we can obviously make things a little bit more noticeable
[39:46] on our God rays and we will just merge this over our result.
[39:50] Let's set this to plus and already we have a lot going.
[39:54] Let's also crop out our God rays there.
[39:57] And now we can start introducing.
[39:59] Let's do a crop.
[40:00] Let's do our AP glow as well.
[40:03] And here we'll want something nice and contrasty.
[40:07] We'll do something like this.
[40:08] Let's merge this over with a plus operation.
[40:12] And this is really the last layer that we need here.
[40:17] We can pretty much just merge this entire chain onto our existing or rather our main chain.
[40:24] And here this will be a plus operation.
[40:27] So this is how we can add our own costume effects.
[40:31] So if I press play, let's load a few frames, see what we get.
[40:34] This is pretty close to the original result that I got.
[40:38] Obviously, there's now a lot of things that we can control.
[40:41] We can go all the way back to our original ramp and we can make some changes even here.
[40:47] We can make this ramp overall a little bit sharper.
[40:51] We can go to our effects.
[40:54] Let's go to our setup here before our gradients and all that stuff.
[40:59] Maybe I can increase the bleeding edge.
[41:02] And also I might want to color this just slightly towards orange.
[41:07] Maybe introduce some mixed values.
[41:09] Let's maybe brighten this up.
[41:11] Let's go to our noise settings here.
[41:13] I might want maybe a little bit less noise.
[41:16] So let's reverse the order and it's A over B.
[41:19] Maybe decrease the mix size.
[41:23] We can do something like this.
[41:25] We'll go to our God rays after the grade here.
[41:29] I can here we can maybe set the gamma to a lower value and probably just
[41:35] let's go back to this orangey here.
[41:37] Make this a little bit more orange, increase the reds maybe.
[41:42] Now not worth spending too much time finessing.
[41:45] Don't want to force you to watch me adjust all of these values.
[41:48] But we have our main effects layer.
[41:51] If we go forward in time, one thing that I would like to do is maybe
[41:55] fade this off towards the edges here.
[41:57] We can go all the way back to our original layer over here.
[42:02] And with the same AP matte, let's just do a copy of this and point this back
[42:07] to our render.
[42:08] And if I press A, we can use this radius here, maybe a lower amount.
[42:14] We can use the same value to just multiply over our effects.
[42:17] So we'll set this operation to multiply.
[42:20] And if we go forward, we can kind of see that with this, we just
[42:24] fade this off towards the edges.
[42:25] We can probably preview this from our final result instead.
[42:29] Let's press A, go back to RGB view.
[42:31] And we can see that this is the result that we get.
[42:34] Maybe we can go back and actually we probably need to introduce this right
[42:40] after our coloring here.
[42:43] Let's do a dot and drag everything up with control.
[42:46] And let's just drop this AP matte down below.
[42:50] And actually, because this is an alpha channel, we should use a gray node
[42:55] instead and point this to our mask.
[42:57] And now set this to zero and let's do invert.
[43:01] So hopefully now we should see that when our circle expands, it will be a
[43:07] little bit cut off from our mask that we created here with the AP matte.
[43:11] And maybe we can make this radius even smaller.
[43:14] So now when I go to our final result, probably this is too much.
[43:18] Let's maybe increase this back.
[43:20] So this looks about right.
[43:21] This is with and without our grade.
[43:24] But we can see that when our circle is near our logo, we do have the original
[43:30] intensity that we had.
[43:31] So it's kind of like an exponential decay now, which makes things a little bit
[43:35] more realistic.
[43:36] And it's sort of like the energy we're having this energy kind of like die off
[43:41] the further it expands.
[43:42] Maybe we will like a little bit more noise.
[43:45] Let's go back to our P noise advance.
[43:47] Just increase the gain here a little bit, add a little bit more
[43:51] crispier details in this energy.
[43:53] And now that we have this layer, one other thing that we can add is a fake
[43:59] global illumination kind of like indirect emission from this layer, mostly
[44:04] to isolate these very dark parts of our geometry.
[44:08] What we can do is if we grab our render and do a shuffle, we can grab from
[44:14] here, let's shuffle out the AO.
[44:17] And if we do a grade and invert our values, we can see that we have this
[44:22] mask on all of these shadowy parts of our render.
[44:26] So now we can just multiply this with the mask that we get or rather the effect
[44:31] that we have probably right after our masking here with the logo.
[44:36] So I will just do a postage stamp and grab and link this up to the result
[44:42] from the grade.
[44:43] And now we can drag this over here, press alt H to hide the connection.
[44:48] And let's go ahead and just multiply this over our ambient occlusion pass.
[44:53] So we get something like this with a grade node, we can now start adjusting
[44:56] things slightly.
[44:58] Let's do another grade over here as well.
[45:01] We can kind of see that this can or has the potential to be like a nice
[45:06] indirect emission pass.
[45:08] We will just have to color this.
[45:10] Let's do a grade here.
[45:12] And let's also choose that nice orange color.
[45:15] And one more thing that we can add on top of this is if we do a blur, we can
[45:20] kind of expand out our this fake indirect emission pass with something like
[45:26] this, maybe do another grade node, do a gamma adjustment.
[45:30] And I will just multiply this layer over with the same ambient occlusion pass
[45:35] that we had originally with our shuffle.
[45:37] So if I set this to multiply, we are now kind of integrating this layer with
[45:42] our render, if I were to bypass this node.
[45:45] And we can also add this on top of what we have from over here.
[45:49] So if we do a merge between these two layers, let's set this to plus.
[45:54] We now kind of have the best of both worlds.
[45:56] We have an indirect emission that's more on the reflection channels and one
[46:01] that's more on the diffuse, which is going to be this layer over here.
[46:04] But probably I can scale down the gamma.
[46:08] And now I can do some individual grade adjustments for both of these layers.
[46:12] We want this to be fairly subtle, something more like this.
[46:16] And if we merge this on top, hopefully this will give us a just a
[46:21] better integration of our effects.
[46:24] So if we preview both of them at the same time, we can kind of see we get
[46:28] just a little bit more of this light right into our shadows.
[46:33] Maybe we can increase things further.
[46:37] Maybe we can bring back a little bit of brightness into this layer, I would say.
[46:43] So this is with and without.
[46:46] I think this really helps to integrate things a little bit better.
[46:49] And this is really the last layer that we can add.
[46:52] And now that we have this, we can do a really quick distortion layer on top as well.
[46:58] And usually with distortions, I like to add them below the actual effects.
[47:03] So if this is the effect and our geometry is here, I like to have
[47:07] the distortions only on the geometry.
[47:09] We can do this very simply.
[47:10] If I were to start, we can just do a noise here.
[47:15] We want red and green values for the distortion.
[47:18] So I'll just disable the green and blue and only work with the red for now.
[47:24] Let's go ahead and make this a little bit more smooth.
[47:27] I'll reduce the gain and maybe increase.
[47:30] And for the gamma, let's actually leave this at point five.
[47:33] And I would like to use a grade node.
[47:36] Let's uncheck black clamp and let's only work with the red channels.
[47:41] Or though in this case, we just have the red channel, so it doesn't matter.
[47:44] We will just push the offset in.
[47:46] So we have negative values as well because the distortion needs positive and negative ranges.
[47:51] So now with the offset value set to around negative point five, we can see that these
[47:58] some of these areas over here have negative ranges and some of these bright areas have
[48:03] positive ranges.
[48:04] And we want to do the same kind of setup for our for the green channel.
[48:09] So I can just duplicate this layer.
[48:11] I'll set this only to green and I will just change the Z value here.
[48:15] So we get a different seed and we can merge these together.
[48:19] We'll set this to plus.
[48:20] So this is our distortion layer.
[48:22] We will need to shuffle this into our main chain.
[48:25] So we'll just place a shuffle node, point the layer to our distortion or rather our
[48:31] noises and the RGB layers here.
[48:34] Let's shuffle them inside a new layer.
[48:37] I'll name this one.
[48:38] Let's do distortion and we just need really our red and green values.
[48:44] We'll we can keep the blue.
[48:45] It won't bother us.
[48:46] We'll hit OK.
[48:47] We have a layer called distortion.
[48:49] So now if we drop down and I distort, we can let's preview the results over here and set
[48:55] the UV channels to our distortion layer.
[48:57] And now I can just increase our UV scale.
[49:00] Let's increase this all the way to 100.
[49:03] And this doesn't give us the correct results.
[49:06] And this is because here in our shuffle, the input by default, this is B, but really we
[49:13] should change this.
[49:14] We can see we want to bring the colors from input A.
[49:17] So we will change this to A.
[49:19] And now our distortion has the correct look.
[49:22] So I will just increase this.
[49:24] We'll leave this as 100.
[49:26] And now if we go back to our noises, if I want a little bit more detail here, I can
[49:31] just increase our gain values in both of these.
[49:35] So as I increase the gain values, we can see we get a little bit more crunchier detail
[49:39] here, which might be something that we want.
[49:41] I think I do in this case.
[49:43] And we just want to mask this out with the layer that we already have.
[49:48] So over here, or actually over here, we just our mask, let's go ahead and we can do a
[49:55] multiply over our noise with the result from our effects.
[50:00] We'll set this to multiply.
[50:02] So now we will only have values inside our region here.
[50:07] So if I go back to the distort, we can see now that it's only affecting these areas.
[50:12] We can also maybe blur our mask a little bit.
[50:14] So on this layer that we're ringing in, we can just increase the blur here to smooth
[50:19] out this masking.
[50:21] And now if we check, we have something like this.
[50:23] And if we want to increase the overall distortion, we can just bump up the values here.
[50:29] We can even add a secondary gray node, which we can control from over here.
[50:34] Although let's not forget to uncheck black clamp because we need the negative ranges as
[50:39] well.
[50:40] So we can do something like this.
[50:41] I can play around maybe on our grade.
[50:44] We can play around with the offset and try to maybe center this noise a little bit better.
[50:49] So let's do something like this.
[50:50] So we have our distortion and to introduce a little bit of chroma, a little bit of RGB
[50:55] split in this, make it just a little bit cooler.
[50:58] It's a very simple setup.
[51:00] We just need three different versions of our ID stored values per each individual channel.
[51:06] So RGB.
[51:07] If we do a shuffle, for example, we can just keep our red channels.
[51:12] We can duplicate this over.
[51:14] Let's also add a node over here.
[51:16] We'll grab this, duplicate this over, connect this back, duplicate this one more time.
[51:22] And we just manually split up all of our channels here.
[51:25] We just want our green.
[51:27] And finally, we just need our blue.
[51:30] And now if we do a merge between all of these layers and set operation to plus, we have
[51:36] our original result.
[51:38] But now we can affect the distortion individually per channel.
[51:42] So so we can just grab some of these values and we can see if I moving closely that that
[51:48] if I grab the green values, we can do something like this.
[51:52] And it's really, I don't really have a rule for this.
[51:55] Just just change the distortions to something that looks cool.
[52:00] But we do have now some chroma distortions as well.
[52:04] Let's maybe check out some different frames as well.
[52:07] I just play around with the values until you get something that you like.
[52:11] Honestly, should be OK.
[52:13] And this will be our final result.
[52:15] Of course, at the end, you can still add some final post processing.
[52:19] We can maybe introduce a little bit of contrast.
[52:22] Usually I like to do a diffusion pass as well.
[52:26] And in this case, I might want to increase the size here, maybe lower the amount.
[52:32] We can do an AP vignette just because we're really cool and maybe decrease this.
[52:39] We can also do I like usually the chromatic spin.
[52:44] And all of these are from the survival toolkit with chromatic spin.
[52:49] We had some nice chroma around the edges, but the defaults are too strong.
[52:53] So just decrease the size.
[52:55] We can do something like this.
[52:56] But really at this point, I'm pretty much just stretching the length of this
[53:00] tutorial finally just drop down some green and you are good to go.
[53:04] Let's do here another preset.
[53:06] This should be OK.
[53:07] And we can call this come finished.
[53:08] And these are some of the things that we can do with the world position.
[53:13] And now a really cool thing that we can do is if we go back to our mask here,
[53:18] we have a circular gradient, but using the same world position.
[53:23] If we do a shuffle, we can do a gradient that's let's grab from our position.
[53:30] Let's maybe do a gradient on the X direction.
[53:34] So I'll plug this actually in the alpha and we have this.
[53:37] But we want to normalize this because here we have negative ranges.
[53:40] Let's do a grade node, get rid of the black clamp.
[53:43] So this to alpha and let's set the black point to be negative one or so.
[53:49] And the white point is looking fine.
[53:52] And we'll just replace this.
[53:53] Let's add a dot and replace the AP map with this.
[53:57] So now if we look at our estimate, we have some nice vertical scan lines.
[54:03] And if we look at our final result from over here, we have a different result.
[54:08] Or rather, our pulsating is now going in a different direction.
[54:13] So we can go back to our gradient.
[54:14] We can further control, maybe increase the spacing between our gradients here.
[54:20] So now this is the result that we get, which I think is pretty cool.
[54:23] And I had to do this effect as well.
[54:26] Again, over a city, this really works well when you have when you kind of want
[54:31] to have a pulsating thing or scan lines traveling across a scene.
[54:35] It's a really way to do something like this.
[54:37] And just for fun, we can also grab our Z value and if I plug this
[54:42] inside the alpha, we should get horizontal lines instead, which we can see over here.
[54:48] Now, let's do one more thing for fun if we duplicate this setup.
[54:53] And for this one, I use the X values and I were to merge these together.
[55:00] Let's set the operation here.
[55:02] Let's try multiply and see what happens if we get both X and Z directions.
[55:07] Well, actually, now we multiply, we get what we had with our AP map,
[55:12] which is pretty fun, which is a circular gradient, but it's starting from a different place.
[55:17] And this is probably because the coordinates get messed up.
[55:19] Let's see what happens if we just plus them together.
[55:22] So if we plus them together, apparently we get diagonal lines, which I'm sure when we
[55:28] actually do the math that everything adds up, it's not really kind of like the waffle
[55:32] pattern that I was expecting.
[55:34] That's probably because we kind of we should probably we would probably need to do two
[55:40] different streams.
[55:41] So we might not need to merge this over here, but rather duplicate the entire setup.
[55:48] Let's maybe place this over here.
[55:51] And if I connect this over like this, we should merge these two together.
[55:58] And if I now set the operation here to multiply, we actually get the waffle pattern that we
[56:05] actually want.
[56:05] So the world position pass, hopefully from now on, you will always add this to your
[56:09] renders.
[56:10] And I really hope this also helped you see what possible things you can do directly in
[56:15] Nuke.
[56:15] And I will encourage you one more time to give Nuke a shot.
[56:17] I promise you it will make you a better 3D artist.
[56:21] And I know I went a little bit fast, maybe over this entire setup.
[56:26] This tutorial is based on the assumption that you already are familiar with a lot of
[56:30] the Nuke workflows.
[56:31] Again, if you're not, check out our intro to Nuke for 3D artists, free to enroll.
[56:36] And as always, for more courses and tutorials, check out voxside.com and I will see you next time.



---

## Captured Frames

- [0:35] tutorials/frames/build-entire-fx-with-one-pass---nuke-tutorial/frame_000.jpg
- [8:20] tutorials/frames/build-entire-fx-with-one-pass---nuke-tutorial/frame_001.jpg
- [12:30] tutorials/frames/build-entire-fx-with-one-pass---nuke-tutorial/frame_002.jpg
- [18:20] tutorials/frames/build-entire-fx-with-one-pass---nuke-tutorial/frame_003.jpg
- [31:55] tutorials/frames/build-entire-fx-with-one-pass---nuke-tutorial/frame_004.jpg
- [39:10] tutorials/frames/build-entire-fx-with-one-pass---nuke-tutorial/frame_005.jpg
- [56:05] tutorials/frames/build-entire-fx-with-one-pass---nuke-tutorial/frame_006.jpg

---

## Structured Notes

### Core Technique
Using the World Position (P) AOV in Nuke to drive procedural, 3D-space-aware texture mapping, region masking, and an animated pulsating-ring energy effect — entirely in 2D comp, without re-rendering the 3D scene.

### Summary
Starting from a flat CG beauty render (rebuilt from Karma AOVs) and its World Position pass, Voxyde VFX layers up surface breakup (multi-scale procedural noise driven by 3D position, plus real textures projected via a fake-UV STMap trick built from World Position X/Z), isolates specific regions of the render by height or by Cryptomatte ID, fakes indirect-light bounce, and finally builds a pulsating expanding-ring FX layer around a logo using a World-Position-derived radial distance gradient, an animated repeating ramp, god rays and glow. It closes with bonus scanline/diagonal-waffle patterns made from raw World Position channels — demonstrating that a single AOV (P) is enough to drive most position-aware compositing tricks without touching the 3D scene again.

### Key Steps
1. Rebuild the beauty from split AOVs (Shuffle diffuse/glossy-reflection dome passes, Merge with Plus) as the base for every layer that follows.
2. Break up surface detail with `P_NoiseAdvanced` (Nukepedia / Nuke Survival Toolkit gizmo), feeding the World Position AOV directly into its position input — this generates noise mapped in true 3D space, independent of UVs. Stack 2 copies at different size/gain, merge with Multiply, tame with Grade (gamma).
3. Fake UVs from World Position when real UVs are missing: Shuffle the P pass so X→red, Z→green; feed that into an `STMap` node's UV input with a real texture (e.g. a scratches map) plugged into Source.
4. Fix STMap's 0–1 range requirement with Expression nodes: `abs(r)`/`abs(g)` kill negative coordinates, then `r%1`/`g%1` wrap everything back into 0–1 for seamless tiling. A Grade's gain before the STMap controls tiling frequency — its "black clamp" must be unchecked or it destroys the coordinate data.
5. Multiply the mapped texture with a contrast-boosted copy of the beauty before merging it back with Plus, so added detail still respects the original lighting.
6. Isolate a height band (e.g. only the floor) using P's Y channel as an alpha mask: Shuffle P.y → alpha, Grade to threshold/offset the band, then use it as a mask input (invert as needed) on a Grade/Merge to confine a texture layer to that region only.
7. Isolate a specific object (the logo) with Cryptomatte: Merge operation `in`/`out` against the crypto alpha masks a texture onto just that object; multiply with the shuffled AO pass to ground it in the existing shading.
8. Fake indirect-light bounce: Merge (operation = `difference`) between a combined AOV (diffuse or reflection) and its dome-only contribution isolates the light's indirect contribution; Plus it back on top. Animate a believable flicker via a Grade `mix` expression: `random(frame/5)` — larger divisor = slower flicker; reuse the identical expression on a second node for synced flicker, or add an offset to the frame for a different seed.
9. Build the pulsating-ring base: `AP_Matte` (Nukepedia / Survival Toolkit) fed the World Position pass generates a radial distance gradient from world origin (0,0,0) with a radius/falloff control. Remap that gradient through an `STMap` sourced from a horizontal black→white `Ramp`, using `alpha%1` (same wrap trick as step 4) so the gradient becomes a repeating band pattern instead of a single falloff.
10. Animate the pulse via an expression on the remap Grade's offset — `frame/50` (or `/100` for slower) — and add a secondary pulse by duplicating that Grade with `offset+0.5`, then Merge (Multiply) the two for pulses-between-pulses.
11. Composite the ring: base gradient colored orange, a sharp "leading edge" copy merged in Plus, `P_NoiseAdvanced` breakup multiplied in for crunch, a `GodRays` node (position/steps/2-color falloff) for streaks, `AP_Glow` (the exponential glow gizmo used throughout all this author's tutorials) for bloom — merged Plus onto the main chain; mask with the logo Cryptomatte so the ring reads as emitting from the logo, and fade it with distance via a second AP_Matte radius used as an exponential-decay multiply mask.
12. Add screen-space distortion below the FX layer (only warping the geometry, not the ring): two `Noise` nodes (red channel = X offset, green = Y offset, different Z seed per channel, offset pushed negative for a +/- range), shuffled into a custom "distortion" layer, fed to `IDistort`'s UV channels at high UV-scale (~100); blur/multiply the distortion by the FX mask so it's confined to the ring area.
13. Add a cheap chromatic-aberration look: split the composited result into 3 separate R/G/B-only streams, nudge each channel's distortion slightly differently, recombine with Plus.
14. Bonus: raw World Position channels make other patterns for free — Shuffle P.x or P.z directly into alpha (Grade black-clamp off, black point ≈ -1 to normalize the negative range) gives vertical/horizontal scanlines instead of a radial gradient; Multiply two *separately streamed* directional gradients (not the same stream twice) together produces a diagonal "waffle" grid.
15. Finish with standard post: contrast bump, `Diffusion`, `AP_Vignette`, "Chromatic Spin" (Survival Toolkit), grain.

### Nodes / Tools / Settings
- **Core Nuke:** Shuffle, Merge (`plus`/`multiply`/`difference`/`in`/`out`, invert option), Grade (gain/gamma/offset/mix, masked, black-clamp toggle), STMap, IDistort, Noise, Ramp, Crop, Expression
- **Nukepedia / Nuke Survival Toolkit gizmos:** `P_NoiseAdvanced` (3D-position-driven procedural noise), `AP_Matte` (world-position-driven radial/directional distance matte), `AP_Glow` (exponential glow), `GodRays`, `AP_Vignette`, "Chromatic Spin"
- **AOVs used:** World Position (P), Cryptomatte, Ambient Occlusion (AO), combined diffuse / glossy-reflection dome passes
- **Key expressions:**
```
abs(r)                  # kill negative UV coordinates before STMap
r % 1                   # wrap/repeat coordinates into 0-1 range
mix = random(frame/5)   # synced flicker on indirect-emission Grade
offset = frame/50       # animated ring-expansion driver
```
- **Render source note:** Karma-rendered AOVs; author notes Karma didn't populate the expected "combined emission" layer directly, requiring the difference-of-doms workaround (step 8) instead.

### Difficulty
Intermediate — assumes solid familiarity with core Nuke workflows (the author explicitly builds on his free "Intro to Nuke for 3D Artists" course); individual techniques (STMap tiling, world-position matting) are simple once explained, but the full pipeline stacks many interlocking layers.

### Foundry App & Version
Nuke / NukeX — works with the free non-commercial version per the author. Specific version number not stated in the transcript or visible on screen.

### Tags
compositing, cryptomatte, st-map, merge, channels, aovs, grading, gizmo, procedural-texture, intermediate

---

## Related Tutorials
- [Skill Up with Nuke | How To Think Like A Pro Compositor](skill-up-with-nuke-how-to-think-like-a-pro-compositor.md) — shares `compositing`, `grading`, and use of the same community Nuke Survival Toolkit gizmo pack; a general problem-solving framework vs. this tutorial's single-AOV technique deep-dive.
- [Nuke Tutorial | Compositing a Rainbow [Intermediate]](nuke-tutorial-compositing-a-rainbow-intermediate.md) — shares `compositing`, `channels`, `procedural-texture`, `intermediate`; both build procedural color/pattern effects purely from channel manipulation.
