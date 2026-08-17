---
title: Houdini FX, Solaris & Nuke -  Full VFX Course
source: YouTube
url: https://www.youtube.com/watch?v=LBAXQC5maVY
author: Voxyde VFX
ingested: 2026-08-14
app: "Nuke (canonical here — cross-platform course, see note below) + Houdini/Solaris (source sim/render side, summarized)"
version: "not specified"
tags: [compositing, aovs, cryptomatte, channels, digital-matte-painting, projection, st-map, gizmo, camera-tracking, fx-simulation, 3d-system, advanced]
extraction_status: complete
frames_dir: tutorials/frames/houdini-fx-solaris-nuke---full-vfx-course/
frame_count: 12
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini FX, Solaris & Nuke -  Full VFX Course

**Source:** [YouTube](https://www.youtube.com/watch?v=LBAXQC5maVY)
**Author:** Voxyde VFX
**Duration:** 198m39s | 9 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Overview & Setup [0:00]
**Transcript (timestamped):**
[0:00] Let's start by doing a quick rundown over the entire project and see exactly what we
[0:13] are going to be creating.
[0:14] And we can start here at the SOP level where we have our character.
[0:19] So if we go inside the character geometry container, this is just a simple USD import.
[0:24] So all of the files provided will be in USD format.
[0:27] And you can download everything, including the render files and assets that we are going
[0:32] to be using and also the completed project file in case you get stuck.
[0:35] So you can check it out and see exactly how I built everything.
[0:39] So this will be our character with a simple walk animation.
[0:43] And if I go up, we have our effects containers over here.
[0:46] So the first one will be for our cloth.
[0:49] If I step inside, we can see the final result will be this vellum simulation of the cloth
[0:54] with some wind pushing our cloth in this left to right direction, which will also be the
[0:59] same direction for all of the other layers as well.
[1:02] We can see that this isn't really a huge network here.
[1:04] This is a pretty simple simulation, but there are a few tips and tricks we're going to discuss
[1:10] here.
[1:11] And not only for this cloth simulation, but for all of the layers, we're going to discuss
[1:15] a lot of different setups and shortcuts that we can take to achieve a very art-directable
[1:20] result.
[1:21] All right, so this will be our cloth.
[1:23] Let's go up.
[1:24] Let's go into our effects shirt.
[1:26] So we are going to grab the shirt from our character, and we are going to simulate this
[1:30] as well.
[1:31] We are going to do a very interesting thing here, which is to use the ripple solver to
[1:36] generate sort of like this wind passing through our cloth.
[1:40] So we can see that we're not really using any collision and everything is driven by this
[1:45] ripple solver.
[1:46] We can go to the file cache here and we can preview the result, which looks something
[1:50] like this.
[1:51] So this will be pretty fun to set up.
[1:53] Let's go up and let's go forward to our smoke and dust elements.
[1:58] And again, this is, we can see for our pyro, this is a very simple setup.
[2:03] Let's preview the result.
[2:04] So here it is, just some smoke blowing from the side driven by mostly wind and turbulence.
[2:10] And over here to the right, we have our dust setup, which is going to be particles advected
[2:16] by this wind velocity.
[2:18] And we are going to scatter a bunch of small rocks.
[2:21] So let's maybe close in on one of this.
[2:23] It's really just a simple sphere with some noise applied to generate sort of like a small
[2:28] rock and this will be our dust layer.
[2:31] So this is pretty much all we are going to do into SOPS.
[2:34] The setups themselves are pretty simple, but like I said, I'm also going to show you a
[2:38] lot of cool tips and tricks to optimize the setups and sort of cheat with a lot of these
[2:45] simulations to get them to work exactly how we need them.
[2:48] And then we are also going to render everything in Solaris.
[2:51] So I'm going to cover the entire workflow.
[2:54] If I go inside this SOP context and hold down N, I can jump to the LOPS context from over
[2:59] here.
[3:00] This is really handy to do.
[3:02] We can jump to LOPS and then we can jump back to the object level if we want.
[3:06] So we can see that this is pretty fast.
[3:08] And this is usually the way I prefer working.
[3:10] Now here in the stage context, we are going to recreate this entire chain.
[3:14] We can see that this again isn't really such a big network here because we only have a
[3:20] few elements.
[3:21] So we are going to bring in our camera and then we are going to layer our character with
[3:26] all of the effects emulated, so the shirt and the cape.
[3:30] And we are also going to create the material for the cape directly inside of Solaris with
[3:35] material X.
[3:36] So we'll also take a look into that.
[3:39] After that, we can layer in our smoke.
[3:41] So our volumes and then on top of that, we'll bring our dust.
[3:47] Finally we do some very simple light setup.
[3:50] We can see I'm just using a physical sky and a distant light doing some camera adjustments
[3:55] here.
[3:56] And then we are going to split all of the layers that we are going to render.
[4:00] So we'll have four total layers that we'll export over to Nuke.
[4:04] And this will be the Solaris setup.
[4:06] And after we have all of our render layers, we can jump into Nuke.
[4:10] And this is what we are going to be creating over here.
[4:13] We can start all the way at the top.
[4:15] So here we'll have a background smoke.
[4:18] And on top of this, we are going to layer our character.
[4:21] So it's pretty much going to mimic the Solaris setup, if I'm going to be honest.
[4:26] So back over in Nuke, over our character, we're going to layer our foreground smoke
[4:32] like so.
[4:33] Then we are going to bring in the eyes where we are going to do some glow and a little bit
[4:38] of optical flare effect here.
[4:40] And then over this we'll bring in our dust, which is the final layer.
[4:44] And finally, we'll do some grading, post-processing, and also the final crop to give this that
[4:50] cinematic anamorphic look.
[4:52] And this will be the comp.
[4:53] So again, we are going to explore a bunch of different tips and tricks.
[4:57] So for example, for our character, if I look at this, I'm going to show you a way that
[5:02] we can get a Fresnelpaz going by exporting some custom AOVs from Houdini.
[5:08] We're also going to layer some custom scratches on top of our armor directly inside of Nuke.
[5:13] And we're going to explore a bunch of tricks like this to really fine tune the final render.
[5:18] And now since we are in Nuke, if I press S and go to my project settings, we can go to
[5:24] the color tab and we can see that the color management here is set to OCIO.
[5:28] And the default option here for the OCIO config is going to be this aces.
[5:33] And you can see this because it's offscreen, but the default config here is this aces 1.2
[5:39] or whatever the latest version of aces you are using.
[5:43] But you can see here that I have a different config, which is this Houdini config.
[5:47] And this is the configuration that I grabbed from the Houdini folder.
[5:52] So if you go to your documents folder inside your Houdini folder, where you have the packages
[5:57] and all of the configurations, you will have this OCIO folder.
[6:02] And I grabbed this config from here.
[6:04] So this is the configuration that Houdini uses by default.
[6:07] And really all I did is just point the configuration file to this file over here.
[6:12] So we can see that this is an OCIO format.
[6:14] And this will mean that I'm going to get consistent results between what I'm previewing in Houdini
[6:19] with Karma and what I'm going to import into Nuke.
[6:23] And if I go step over to Houdini and inside Solaris, let's go to any one of these layers
[6:29] and I just want to show you how to set this up.
[6:32] So if I press Shift R, so we can go inside the render view.
[6:36] We can see that as I look at this render and if I look at the file that I've exported
[6:41] or rather imported into Nuke, so this base file over here, we have the same result.
[6:45] Now it's not really the same frame.
[6:47] Let's go to 1054 here as well, just so it's consistent.
[6:51] So we can look at this and then we look at this as well.
[6:54] So we can see we have exactly the same colors.
[6:57] Now in Houdini there's a few things that we have to do here and if we go to where it says
[7:02] Karma over here at the top, we can turn on this color correction toolbar which is off
[7:07] by default.
[7:08] So let's make sure that this is turned on.
[7:10] And the default color space here, if we look at this dropdown, the default setting here
[7:15] is going to be loot and gamma.
[7:17] So this is what it looks like and this is the basic version without any high dynamic range
[7:23] colors.
[7:24] Let's make sure that we are using OpenColorIO over here and this option for sRGB display
[7:29] will be fine but this option where it says Untone Map, this refers to the configuration
[7:35] that I've imported into Nuke over here.
[7:38] So for example, if you want to work in the regular ACES color space, let's switch this
[7:43] over to ACES 1.2, we see that everything is a little bit darker but we still have high
[7:48] dynamic color ranges.
[7:50] And if I were to switch over to Houdini, we can also set this to be the regular ACES configuration
[7:56] so I can turn this on and we can see now that it looks like this version over here.
[8:01] So this is something important to take into account right as you start the project to
[8:06] make sure that you're working in the correct color space from the start.
[8:10] So I'm going to switch this back to the default Untone Map and this is the config that I'm
[8:14] going to be using but like I said, you can use the regular ACES as well.
[8:18] And one final thing to take into account here, we have to go to the Edit Settings and OCI
[8:23] settings over here and we have to make sure that our EXR files here are exported in the
[8:29] ACES CG color space.
[8:31] So by default I think this was set to one of these other settings.
[8:36] So I think the default is set to sRGB Texture.
[8:39] Let's just make sure that we are exporting in this ACES CG color space and again this
[8:44] is to ensure that whatever we are seeing here we'll see in Nuke as well.
[8:48] So we can actually now start building the project from scratch and we can start directly
[8:53] inside of Solaris to bring all of the assets that we need.
[8:56] So let's go ahead and I will just recreate the entire chain over here to the right.
[9:02] I will start with a sublayer and just bring in the camera.
[9:06] I can also rename this to camera or cam.
[9:09] So let's point our file to the camera USD layer.
[9:12] So this is what's included in the downloads.
[9:15] Let's go ahead and bring this up and I will duplicate this sublayer over here to the right
[9:19] and let's bring in our character.
[9:22] Let's point this first.
[9:23] We'll go inside our Carebase and we have this Carebase USD.
[9:28] Let's start with this and this is the character without any animations applied to it.
[9:32] So this has all of the look they've already done here.
[9:35] So we have all of the material assignments and everything we need.
[9:39] In fact, we can go ahead and if I were to just drop down a physical sky just real quick
[9:45] so we can preview this.
[9:47] If I press Shift R we should see all of our materials.
[9:50] So we don't have to worry about recreating all the materials and all that boring stuff.
[9:55] Now we can go ahead and let's merge our camera with our character.
[10:02] And because I want to see my scene graph I will switch to my Solaris context which is
[10:08] kind of the same setup as the regular Solaris desktop here.
[10:13] The only difference is that I place the scene graph tree and the scene graph details over
[10:16] to the side so it's more vertical just because it kind of makes more sense to me this way.
[10:20] So let's go back to our chain here and we can already see what we have.
[10:25] So our camera and the character with all of the mesh components and our material components.
[10:31] And from here what we can do is simply sublayer our animation.
[10:34] So this is a separate file.
[10:36] Let's drop another sublayer under our character and I can even rename this to Anim and we'll
[10:43] go ahead and point to our carewalk.usd and we can see this is the benefit of the USD workflow
[10:50] is we can now essentially replace the animation without losing any of our look depth.
[10:58] So if I press Shift R we'll still have all of the material assignments and all the settings
[11:02] from our character base file.
[11:06] And this animation layer by itself, this character walk.usd is only containing our mesh information.
[11:14] So it's basically just replacing all of these mesh components here with their animated versions.
[11:19] So let's also check to see that our camera is working.
[11:23] So we have our camera and we can also just let's just drop a physical sky for now because
[11:29] we are going to need this later anyway down a merge from here and let's preview the result.
[11:36] Actually let's also drop down a Karma render settings because we're also going to need
[11:41] a few of these layers and we can set this to Karma XPU.
[11:46] I believe all of the layers I rendered by using the XPU engine.
[11:50] So not the regular CPU but you can use the CPU version if you want.
[11:55] Let's make sure that our camera is pointing to our cam 2 and you can also decide on the
[12:00] output path that you want over here.
[12:02] For the resolution we are also going to use 1080p and I can close this for now and let's
[12:09] go to our Karma XPU render view.
[12:12] So this is kind of working.
[12:14] The reason that this is blurry is because we have to set the focus point for our camera.
[12:19] So let's go ahead, press Shift-R to cancel the render.
[12:22] Let's drop down an edit camera here right at the end and we'll point to our cam 2 for
[12:29] primitives and we can go to sampling and we will have to animate our focus distance to
[12:34] match the character as it's moving forward.
[12:37] So if I go outside in the perspective window and I turn on my grid, our camera is roughly
[12:44] 19 units away from our character when he starts to walk because he's starting the walk at
[12:50] origin here at 0, 0, 0.
[12:52] And also the animation we can see that we are working with the frame range 1001 to 1120
[12:59] at the end.
[13:00] And also if I check this animation we see that we have around 50 frames of free roll
[13:04] and this is for the cloth simulation mainly.
[13:07] So the ranges that I'm gonna work with is going to be from 950 to 1120 but we are only
[13:13] going to render from frame 1001.
[13:16] Let's also maybe hide the lights in our viewport.
[13:19] So we start at the origin here with our animation and our camera is like I said around 19 units
[13:26] apart.
[13:27] So let's go to our focus distance here.
[13:29] Let's set or create.
[13:30] We'll set the distance here to 19 at a keyframe with Alt and Left click and we'll move further
[13:37] away and we are going to scroll the timeline and let's go right at the end at the last
[13:42] frame so 1120 and we can actually press enter in our viewport to also see our focal point
[13:49] and since this is an animated value now I can just simply drag this over here until it
[13:54] matches with our character.
[13:56] So let's make sure that this remains that the focus remains on the character.
[13:59] This will automatically add a keyframe now that I moved this in the viewport for this
[14:03] value of 315.
[14:05] Let's also shift click this value so we can look at our keyframe so I can press F and
[14:11] by default it creates this base year interpolation.
[14:14] Let's grab the keyframes and set this to a linear interpolation.
[14:18] And now essentially the focus should follow our character and it does.
[14:22] So if I go back inside the camera view and press shift R now we should no longer see
[14:27] this blurriness.
[14:29] Of course our sky is blurry in the back but we don't really have to worry about sky because
[14:34] we are not going to render this so I can actually just go to the physical sky and turn off render
[14:39] light geometry.
[14:40] Okay so we are off to a good start.
[14:43] We can now focus on the simulations.


### Cloth Simulation [14:45]
**Transcript (timestamped):**
[14:46] So let's go ahead cancel the render here with shift R go back to our object view and
[14:52] I'm actually going to set this back to my build desktop here and now we are at the
[14:58] sub level.
[14:59] Let's just ignore all of these layers for now.
[15:02] Maybe we can keep the LOP import camera.
[15:04] So this brings our camera from the stage context over to subs.
[15:10] So all we have to do here is if I go back to LOPs we can grab this cam sub layer press
[15:15] Ctrl C go back to object and the LOP should be pointing to our cam sub layer and the primitive
[15:22] we actually have to grab from over here but we can see we have this slash cam too so this
[15:28] will be our primitive path and we just have to make sure that this matches.
[15:32] So now we have our camera at the sub level as well.
[15:36] Let's go ahead and drop down AEG container and we will import our character so we'll
[15:42] name this to import care and we'll do a USD import and let's bring in only our walk animation
[15:50] because we only need the geometry so we are not interested in all of the other material
[15:55] assignments and stuff like that.
[15:57] And let's also unpack and let's keep this as primitive so we can later select our shirt
[16:03] and disconnected from our character.
[16:06] So we'll just do a null here and this will be our out character.
[16:10] We are not going to do really anything else here.
[16:13] This is mainly just so we can preview our simulated layers on top of our geometry.
[16:19] So when I go up and we create all of the layers we can jump inside the camera and we can preview
[16:24] how this looks at the sub level and get a better idea on how it's also going to look
[16:28] when it's rendered.
[16:29] So we are going to start with our cloth.
[16:32] So let's do a geocontainer.
[16:34] I'll rename this to FX underscore cloth and let's step inside.
[16:38] Let's do another USD import and we'll bring in our character.
[16:44] So here we have it.
[16:45] And if I also show a lot of objects so we can see our character now obviously this cloth
[16:51] is an animated we can see that as I go to the first frame so in this case it's going
[16:55] to the animation starts at 950 with those 50 frames of pre-roll.
[17:01] If I go to the beginning let's maybe reset our viewport or go up here we can see that
[17:06] the cloth is right on top of our character and we can start working on the simulation.
[17:11] So let's go back inside and we want to unpack this as well and we'll just unpack this to
[17:16] polygons directly so now we can access all of our polygons and we can do proper simulation.
[17:23] Now we'll also need to collide with our character so we can go up and let's grab our character
[17:28] from over here and I will press Ctrl C and we'll just object merge this here.
[17:34] And for this we'll also need to unpack this so we have access to all of the polygons otherwise
[17:40] the collisions won't work because this is still packed primitives as we can see here packed
[17:45] USDs.
[17:46] So let's drop an unpack and let's also drop a convert and now we have access to all of
[17:51] the individual polygons as we can see.
[17:54] So for our cloth we could pretty much simulate this directly on our character so for example
[18:01] if I drop down a vellum configure cloth this will be our first input and our third input
[18:08] the collision will point to our convert here.
[18:11] Let's maybe drop down a null and let's rename this to Geo call for geometry collision.
[18:17] This node will configure all of our vellum settings for us so here we can configure stretch
[18:23] and bend settings that determine how the cloth moves but we will leave these settings at
[18:29] their default values for now and let's just place this inside a vellum solver right away
[18:35] and see what we get and with most vellum simulations you will probably need to increase the sub steps
[18:41] so let's just increase this to a value of three for now and let's press play and see
[18:46] what we get.
[18:47] So I'm going to let this run for a few frames and check the result.
[18:51] So if I preview this we can see right away that the cloth is quite stretchy now we can
[18:58] probably fix this when we increase the sub steps so I believe the final value here for
[19:03] the subsets will be around five which will sort of deter a little bit of this stretchiness
[19:09] but as I preview this we can see that the cloth for the most part sticks pretty good for our
[19:16] character which is what I'm looking for but when we are going to add the wind we are going
[19:23] to have some trouble holding the cloth onto our character especially around the hood area
[19:29] around the head here.
[19:30] Now for the cloth settings that I used if I go to the vellum constraints option here
[19:36] for the bend I used a lower value here so we can see we have this very very low value
[19:42] here 0.0001 so I just went one step below the default value to this value over here so
[19:50] this will mean that it's easier to deform and this will create more wrinkles and the
[19:55] cloth will have more features.
[19:57] One other way that we can dampen some of this stretchiness here is to increase this damping
[20:03] ratio here for our bend so I usually always like to increase this one just because it
[20:09] makes the simulations a little bit more stable from what I found and in this case this is
[20:14] a very sensitive value as well I just use a damping ratio here of 0.02 and for the most
[20:21] part I left all of the other settings as they are.
[20:24] Let's also add our wind so we can step inside the vellum solver and we'll drop down a pop
[20:30] wind and attach it to our force output and for the wind settings that I used I set the
[20:37] wind velocity so this is the direction I set this to 1, 0 and 1 which is going to be 1
[20:42] on this x direction and 1 in this z direction so the resulting vector will be this diagonal
[20:49] vector that points in both directions and for wind speed I used a value of 1.5 and I
[20:55] just increased the amplitude here so this will add some noise to our wind I just increased
[21:00] this to 1 and the rest of the settings I left them as they are so if I go up and preview
[21:06] this result let's see what we get.
[21:09] Now this is still currently a little bit too stretchy but like I said this will be tapered
[21:14] down by increasing the sub steps and also if you want the geometry to hold together more
[21:20] tightly you can increase the constraint iteration as well you can try a value of 150 if you think
[21:26] the cloth is too stretchy so let's leave this to simulate for a few more frames and see
[21:32] how it holds up when the character starts to walk.
[21:35] Okay so now that we have quite a bit of frames here to work with we can check the simulation
[21:41] and I'm pretty okay with it for the most part now right away what I'm noticing here is that
[21:48] as my character moves forward the hood part here starts to fall off it starts to gradually
[21:55] pull back on the head here and if I simulate further we can see that it eventually falls
[22:01] off almost entirely so we will need to force our hood part to stick with our geometry and also
[22:09] we can force some other parts we can make sure that some of this shoulder over here to the side
[22:16] and maybe over here to the waist as well we can also attach these points to make sure that the
[22:23] cloth doesn't do any doesn't have any unexpected behavior. Now what I want to showcase here if
[22:29] I look through the camera and I play this animation for a bit we can see that this
[22:35] cloth here in the front is a little bit too static and this is because if we preview it from the side
[22:42] as our wind is pushing the cloth in this direction so diagonally and our character is moving forward
[22:50] and when our character moves forward it sort of negates as we can see here it negates this
[22:57] direction that we want for our cloth so as a result it kind of sticks to the geometry quite a bit
[23:03] and this is again because the character is being translated forward and we can see that we have a
[23:08] lot of collision action going on here even though we have quite a strong wind so I want to somehow
[23:15] have the wind affect our cloth but not worry about this collision that's happening because our
[23:22] character is moving forward and what we can do is we can cancel the translation of our character
[23:29] mesh without losing the walk-in animation simulate the cloth in this state and then apply the translation
[23:38] back after we create the simulation so what I mean by this is if we go to our geometry collision here
[23:45] let's maybe make some room so from our convert I can do an extract centroid which will give me
[23:51] a point right in the center of our geometry so if I look at the result here let's run this over
[23:58] detail and for method we can keep this as a center of mess now we see we only have one point I think
[24:04] where I have to reset my viewport here so we we end up with this one point let's maybe set this
[24:10] here to points and also let's increase the guide here so I'll set the point size here let's increase
[24:18] this to a value of 10 so now this point will represent my geometry if I template this on top
[24:24] let's take a look all right so here we have it this point now will always be in the center of our
[24:29] geometry and we can use the position information from this point to subtract it from the geometry
[24:34] now to make this simpler we are only interested in the z value of this point so we can drop down a
[24:42] transform from here and set the scale on the x to zero and also the scale on the y to zero so now
[24:49] we only have this z translation okay so we can see that it's perfectly matching our mesh and now
[24:56] all we have to do is subtract this position so let's drop down an attribute vop from our mesh
[25:03] and let's plug our point as the second input let's grab the position so inside from op input two
[25:09] let's do an import an import point attribute the pt num let's promote this to a constant and keep this
[25:15] at zero because we only have one point and now what we can do is just simply subtract our position
[25:21] with this position and let's plug this into the p and as a result this is what we get now our character
[25:28] walks into place and we still have the position information from our extracted point here so if
[25:36] let's drop down a null and also rename this to extracted pt now to apply back this translation
[25:44] to our static mesh we can do the same thing with an attribute vop by adding the position
[25:51] we can do the same thing to reapply this position let's simply duplicate this attribute vop so let's
[25:58] rename this to negate p and let's rename this to add so it's pretty much the same operation
[26:05] from our static mesh we are going to add this value now so instead of a subtract here we can drop
[26:11] down an add and let's add these up and we should have our original result so if I preview this now
[26:19] we can see that there's virtually no difference between where we started so let's go to our convert
[26:25] here and also look at this and we can see it's the exact same result and now the only difference is
[26:31] that we can apply this to our cloth as well so just for example I can simply grab the cloth as it is
[26:39] at rest I plug this inside our attribute vop operation here with the add let's preview this
[26:46] and let's also preview our character with w we can see as I scroll back from the beginning
[26:53] we don't have any simulations but now this will stick to our character so hopefully you can tell
[26:59] where I'm going with this we are going to simulate cloth on this static version of the character
[27:06] and then after we do our simulation we will apply back this position that we extracted here so now
[27:13] when I will simulate this the wind is always going to be pointing in this direction and it's always
[27:19] going to be on top of our character and not have the collision of our character moving forward
[27:25] interfere that much with our simulation so this will be a lot more are directable and a lot easier
[27:31] to work with and get predictable results in terms of simulation and like I mentioned earlier we also
[27:37] want to stick some points of this cloth directly to our mesh we can assign these let's go ahead and
[27:45] let's create a group over here after our mesh let's set this to point and let's rename the
[27:51] to stick and we can simply select some points here let's grab some over here at the top maybe we can
[27:59] select this with our brush selection so let's set this to brush and let's make sure that this is
[28:05] only selecting visible objects so I'll press shift v which turns on this select only visible
[28:11] geometry and let's go ahead and re-select this this part over here maybe some on the shoulder as well
[28:18] and like I mentioned maybe on the side here so let's press enter this will be our selection so now
[28:25] we can append a vellum attached to geometry in between here so after our vellum cloth we will
[28:31] drop a vellum attached to geometry plug this here and let's go to the top let's preview the result
[28:38] we'll go here for our group type let's set this to point and we'll select our stick group that we
[28:44] created so we can preview our constraints over here as well now if let's press w to view this in
[28:51] wireframe we can see that there's quite a bit of a gap here especially on the side and this means
[28:57] so the default settings here we can see for the wrestling scale of one this will mean that this
[29:04] distance between the constraints will be kept throughout the simulation now I want the cloth
[29:11] to be really close to the geometry so I can in fact set the rest scale here to zero and this
[29:17] will mean that when the simulation runs these points here will snap directly onto our character mesh
[29:24] and they will be kept there throughout the simulation so this wrestling scale will depend on
[29:29] what kind of look you're going for but in this case since our wind is pushing the cloth in this
[29:34] direction I'm totally fine with having this point stick directly on the surface of our geometry
[29:41] all right so I believe we are now ready to run a final simulation so back to our vellum solver
[29:48] I'll increase the sub steps here to five and we can just do a file cache and before we actually
[29:54] save this out and run the final simulation there's also one thing to take into account here we are
[30:00] going to need a rest attribute later when we do our shading in karma so after our group
[30:09] node over here let's also drop down a rest position stop and record this rest state where
[30:15] our geometry is unmoving and I believe now we have all the attributes that we need and we can go ahead
[30:21] and run a file cache on this let's simulate the entire frame range and I'll just rename this to
[30:27] cloth steam and we'll press save to disk so now we can preview our result and let's also template
[30:34] our geometry our collision geometry but the static version and if I look at this we can see now as I
[30:41] press play that our geometry or rather our cloth isn't intersecting as much with our characters
[30:49] so it's not getting pushed into our character here and we can see now that we maintain this gap
[30:54] between the character and the cloth like over here as well which wouldn't be possible otherwise as the
[30:59] cape would be sticking over to this side if the character was also moving forward so again this
[31:04] will give us a lot more art direct ability now it doesn't really make any sense physics wise but this
[31:12] is what will look better in our shot we have a few problems here we can see that the character
[31:18] is protruding with our cloth a lot more so we made a mistake initially in our setup if I look at my
[31:25] the result of this negation here so the negate p attribute vop let's go back to our first frame 950
[31:33] if I look at the result here from where we started with our convert we can see that the mesh jumps
[31:40] a little bit when we do this negation and this is because this extract centroid operation here is
[31:48] kind of giving us a point that's a little bit further and this is because this is calculated at
[31:53] the center of mass so this snap here this slight snap between position is kind of unavoidable
[32:00] and this means that our the initial position of our cloth is a little bit offset from where our mesh
[32:07] is originally so if I preview the cloth and I also template this we can see now that the character is
[32:13] protruding our cloth whereas if I bypass this node we have the correct result so really all we have
[32:19] to do to fix this is add this attribute vop so this negate p let's turn this back on we can also
[32:25] duplicate this by holding alt and I will apply this operation to our cloth as well let's go ahead and
[32:31] get rid of this template display and I'll just plug this directly here so now when I preview the result
[32:37] we can see that the cloth snaps a little bit forward as well and now this will match perfectly
[32:43] with our character the problem here where we apply the same operation the same negate operation to
[32:48] our cloth is that this is a moving point right so let's not forget that this moves in space
[32:55] so when we preview the result of this negate we will also apply this translation and we only
[33:00] want to snap our cloth into place at the first frame so our original 950 so we can just do a
[33:08] time shift for our extract p and we can freeze this at frame 950 so now our point is frozen so we
[33:17] only need this cloth essentially to work at the first frame and now again let's just template
[33:23] the mesh here and we can see that this is working and this means now that when we simulate on the
[33:28] first frame we no longer have to worry about this intersection so we can also see this right over here
[33:33] if I bypass this negate that we apply to our cloth as well that our this is where the mesh
[33:39] protrudes our cloth and this is what's going to make it like completely stick to this part so with
[33:46] all cloth simulations we have to make sure that the collision geometry is not intersecting the
[33:51] cloth that we are trying to simulate so that's something I forgot to do in the first place
[33:55] and we can go ahead now and let's resave this simulation so let's check our new simulation
[34:01] and let's preview this with the static collision and everything lines up perfectly now so finally
[34:08] we can add back our position so the translation we'll just drag the attribute further down and
[34:15] let's apply again we are just applying the transform information from our extracted p and
[34:21] let's preview this let's show a logic so we have our mesh underneath and finally
[34:26] everything's working now this isn't updating properly we can move up to the top level
[34:31] let's preview this through our camera and this is what we end up with so we have no collisions and
[34:36] we can see that the cloth is moving a lot more freely now that we don't have to worry about
[34:43] this forward translation that I keep bringing up and we can see how much more fluid this cloth
[34:50] really is now we can also preview this from the side and we can see that there is this nice gap
[34:56] between the mesh and this overall results in a lot more wrinkles but like I said this gives us
[35:02] the option to control the simulation and make it behave however we want so this whole cancelling of
[35:09] translation and adding this back in is something that comes up all the time in vfx in fact in
[35:16] one of my latest courses anime run effects we use the same method here to simulate our cloth and also
[35:23] we simulated some of these other effects such as this dust kickback that we're having over here
[35:29] and one of the particle layers as well we simulated on a static mesh that's animating at
[35:37] origin and then we reapplied that extracted transformation so if you want to see how I build
[35:42] this entire shot you can check out this course it's called anime run effects and it's available on my
[35:48] website boxside.com and in fact this transform cancelling thing we are going to do for our
[35:55] shirt as well so from here we can drop down a null and we are pretty much finished with the cloth so
[36:01] let's rename this to out cloth now because we are going to bring this later in Solaris it's worth
[36:07] getting rid of some of these attributes we can see that by default Vellum likes to add a lot of
[36:13] attributes here that we don't really need and it's only going to make our life harder later down the
[36:19] later down the road so let's drop down an attribute delete and let's select only the attributes that
[36:24] we want we are going to want our velocity our rest as well so this is this attribute that we
[36:31] created here this is used for shading and for vertex attributes we are going to we probably
[36:37] don't need the UV because we are going to map different things on the rest but let's keep the
[36:42] UVs as well and for the primitive attributes we don't really need any of this so we can delete
[36:48] null selected and we are only going to keep these attributes and we can also probably get rid of any
[36:54] groups as well so let's drop down a groups delete and we'll get rid of all of these groups so now
[37:00] we have a clean mesh with only the attributes that we need and one other thing that we will add here
[37:06] we might as well add this now let's maybe hide other objects we want to add some thickness to this
[37:12] so let's do a Vellum post process and I usually like to run this node after the simulation for
[37:19] most of the cloth simulations that I do let's also increase the spatial blur here which will
[37:25] smooth out some of these nasty looking wrinkles so I'll just increase this to maybe 0.4 and we want
[37:32] to let's extrude by thickness and I believe the default value of 1 and wire divisions 8
[37:38] should work so this is adding our thickness here if you want a super smooth result you can also
[37:44] turn on subdivisions here you can set this to loop we can see that this is taking a while so this
[37:49] is making the mesh a lot heavier if we can look at the wireframe we can see now that we double
[37:55] the subdivisions this smooths out everything so it gives a nicer result but in this case I found
[38:02] that it wasn't really making too much of a difference from this camera at least so I turned this off in
[38:09] my case we might come back to this simulation later after we get our shirt going but for now this is
[38:15] it for our cloth and let's move forward with the shirt so let's start working on the shirt now so


### Shirt Ripples [38:18]
**Transcript (timestamped):**
[38:22] I'll go up and I'll create a new geocontainer and I'll rename this to effects underscore shirt
[38:28] and we'll have to grab the shirt directly from our mesh let's grab our character from over here
[38:35] Ctrl C and I will just do an object merge bring this over in this shirt network and we will have
[38:42] to unpack this as well because we still are working with the packed usd's let's go ahead and drop an
[38:48] unpack and a convert so now if I press S we can go ahead and select the shirt maybe let's press 4
[38:56] and go into polygon selection because this makes a bit more sense and I'll just press delete from
[39:01] over here and let's delete non-selected so now we have our shirt we will go to the first frame where
[39:08] our character is at rest and we are going to do sort of a similar thing where we simulate at world
[39:15] origin and then we reapply the transforms of our character but in this case we are going to simulate
[39:23] a static mesh and we are going to point the format with our moving character so from over here where
[39:31] we select only our shirt let's go ahead and do a time shift and I will freeze this at frame 950
[39:37] so this is static now and just to make things easier I'm also going to do some transform
[39:44] operations here to bring this over to the center of our scene so we can just use a match size node
[39:51] for this which brings it in the center and I will also turn on this option scale to fit so I can make
[39:57] this a little bit bigger just so we have further control over the simulation so this is also something
[40:04] really common where you scale up your sources to match a given unit length size so if I hold down
[40:12] spacebar and press 4 or 3 and go to one of these orthographic views we can see here we have the one
[40:19] unit mark so this currently has a height of around one meter I can increase the target size here
[40:27] let's maybe make this bigger so let's work with roughly three units and we are going to use the
[40:35] ripple solver to generate these waves that move along the shirt and if I were to use the ripple
[40:41] solver on the shirt as it is originally at around one unit height the waves we generate would be
[40:48] sort of big and more rough so like I said we want further control I'll just increase the size here
[40:54] because we are going to reapply this transformation the reverse of this transformation later anyway
[41:00] because we have moved it so we might as well scale it and make our life easier let's go
[41:06] ahead and press spacebar 1 to go into perspective and because like I mentioned we have to reverse
[41:11] this transform operation we can stash the transform so we'll just turn on this option
[41:17] and later down the road we are going to create our simulation over here and if I drop another match
[41:24] size from here with this one we can check this restore transform option and it will move it back
[41:31] where it was so if I look at my convert we can see that the short shirt is exactly where we want so
[41:36] in between we can do here whatever we want and then we will reapply the original size and space
[41:43] it has relative to the world so let's go ahead and check out the ripple solver let's drop this down
[41:50] so ripple solver will place our mesh as our first input let's go ahead and get rid of this match size
[41:57] connection for now and this can also take in a displaced geometry now in this case we don't
[42:03] really have it so we'll just use the same input as our displaced geometry so the normal static mesh
[42:09] and finally this will take a collide geometry as the third input so for this we are just going
[42:14] to generate some spheres on this side that will cause all of the ripples to happen so
[42:21] let's go ahead and we can use a simple scatter for this but I'll show you the problem here let's
[42:27] go ahead and drop a scatter let's drop the force total count maybe to 4 and I will turn off relax
[42:33] iterations and for the global seed I will just give this an expression which is dollar sign F
[42:39] and this will mean that we randomize the seed each frame and now these are points so we have to use
[42:45] actual geometry in order for this to work so we'll just use a sphere we'll drop down this sphere
[42:50] let's set this to polygon and maybe we can increase the frequency it doesn't really matter that much
[42:56] and we'll use a copy to points and copy this onto our scatter points so now we have a geometry here
[43:02] we can also template our shirt and maybe we can reduce the size of this sphere so I'll just drop
[43:09] down the sphere size from over here let's maybe use point two and now essentially if I plug this
[43:15] directly as our third input here we should already start to see our ripples happening let's leave
[43:22] all of the default settings for now and press play all right so here we have it not that great of a
[43:28] result and this is because first of all we need more resolution on our mesh and the best way to do
[43:35] this to also maintain or rather preserve the UVs is to just simply subdivide the geometry so from
[43:42] this match size let's actually maybe drop a null here and rename this here to geo so we can plug
[43:48] more in between I'll just drop down a subdivide here and if I press space bar five we can see that
[43:55] with the subdivisions we maintain our UVs which is the important part here let's maybe just increase
[44:01] the depth here to a value of two and let's take a look at the ripple server now we should have a
[44:07] lot more details and we can see that we do have more details here of course it's worth
[44:13] appending a normal stop here and getting rid of some of these weird looking normals and maybe we
[44:19] can go even a step further for our subdivisions but I think for the most part this should be fine
[44:27] we can see that even with a lot more subdivisions this is very this it's still a very fast simulation
[44:33] so it might be worth having more subdivisions but for the original example I use the value of two
[44:39] we don't really want this ultra crisp wave detail action going we can see that the more subdivisions
[44:47] we have the finer the result is so the finer wrinkles we would have essentially but we don't
[44:53] really need this much I think a value of two for the subdivide works slightly better here
[44:59] this is the result that we are getting now we can see that this is maybe a little bit too chaotic so
[45:07] we are spawning collision spheres each frame and we want something a little bit more controlled
[45:14] so what we can do instead of spawning these many points each frame we can use a pop simulation
[45:22] instead and instead of this scatter here we'll use our mesh to generate particles so I'll drop
[45:29] down a pop network let's place this on our geo and actually I'll get rid of the scatter
[45:35] so inside this pop net we can go to our source scatter on the surfaces should be fine and let's
[45:42] go to the birth tab and let's spawn a lot less particles so let's maybe use a value of four
[45:50] and we also want to have a little bit of life to our particles so and let's actually go up
[45:57] let's make sure the simulation starts at frame 950 okay and if I press play this is what we get
[46:04] so this is a little bit more controlled as we can see maybe we can increase the birth rate here
[46:09] let's try a value of 10 and like I said we'll decrease the life here let's maybe use 0.7 and also
[46:16] it's always worth introducing some variations so let's use live variance 0.35 let's turn off the
[46:22] guide because we don't need to see the geometry and go up and let's press play maybe this is a
[46:28] little bit too much but let's check our result so it's a lot more calm now and we are starting to get
[46:36] the result that we are after now I want the ripples to only go from left to right to match our wind
[46:44] so we will only need collision right on this part over here and there's a lot of different ways that
[46:50] we can do this we can either use a group and use a bounding box to select only parts here
[46:57] but what I did in the original file is I just used a clip so after our pop net I drop down a clip
[47:04] and I press enter and I just turn this around hold control turn this 90 degrees and let's keep the
[47:11] points on this side so I'll reverse the keep operation here and maybe I'll also if I preview
[47:17] the geo as well and go back to my clip I can also maybe skew this more towards only on this side so
[47:25] now if I look at the result we can see that we are only spawning collisions on this side and as a
[47:32] result we'll have waves that now go in the direction as our wind so it kind of feels like there's this
[47:40] wind force that's actually pushing our our shirt but it's really just ripples and we can see that
[47:47] this is a festimulation and a pretty easy setup so this is more on the side of a cheap effect this
[47:55] isn't really necessarily physically accurate at all but it's something that gives the illusion that
[48:01] wind is affecting the shirt as well and we don't have to deal with any collisions and stuff like
[48:07] that so in my hero power up course we did in fact simulate this shirt as well let's see if we can see
[48:15] this now the shirt is slightly moving so it's being affected by all of this energy and the way that I
[48:21] simulated the shirt here and the pants as well is by using the valence solver so more in the
[48:27] traditional way that you will simulate cloth and we made sure to take care of collisions and
[48:33] intersections with the body and accessories that are on top of the shirt and stuff like that so
[48:39] it's a lot more setup and overall harder to do but obviously this will give you the physically
[48:44] correct result by using the valence solver approach so you can check out this course if you want to see
[48:50] how to properly simulate the cloth or rather the shirt in more of the traditional way so now for our
[48:56] ripple solver settings let's maybe first increase the size of our sphere so the size of the geometry
[49:05] matters quite a bit here we can go step further let's use 0.25 so the bigger the collision geometry
[49:12] is the stronger the waves will be so if I press simulate now we can see that maybe this is a
[49:18] little bit too strong let's let's keep this at 0.2 and let's take a look at some of the
[49:22] solver settings here for the wave speed I want this to move rather fast so I set this to a value of
[49:29] 4 in the original example so we can see now that this is a lot more chaotic of course this is now
[49:35] crumpling everything I've way too much so this is where the rest spring option comes into place so
[49:41] I set this to a value of 2 these kind of go hand in hand and also the conservation value here let's
[49:48] set this to a value of 0.4 and the conservation is is basically the dampening of the ripples the
[49:55] lower you set this value the faster the ripples will sort of dissipate so if I press play this is
[50:03] the result and I also increase the thickness here we can give this a 2.5 value which will make our
[50:11] waves a little bit stronger as well it will treat this geometry as a thicker mesh so these are the
[50:18] values I used and for the simulation we can leave these steps as they are so if I press play this is
[50:24] the result so we can see that after the first few frames our waves start to accumulate and we kind
[50:30] of get this feeling that the wind is pushing the shirt also I might want to adjust this clip so we
[50:37] don't really want any particles spawning too much in the center here so let's go to our clip here
[50:43] and let's drag this further away and now maybe I can increase the scale of the sphere so let's use
[50:50] 0.25 because I can see that the ripples are getting quite low in amplitude so let's maybe check this
[50:56] all right so this is what we are looking for maybe the speed is too high but I will let you adjust
[51:03] these settings until you get the desired look maybe we can go even one step further for our size
[51:09] okay maybe this is way too much we can see something weird is happening here so let's
[51:14] drop this back to 0.25 and I think this will be fine so we take some fine tuning and adjusting but
[51:20] these are mainly the three settings that you have to play around with and after you get the right
[51:24] values here let's go ahead and we can just do a file cache on this and I will rename this to
[51:31] shirt sim and save to disk and this should be super fast and this was done almost right away
[51:37] and now what we have to do is let's move this back into place so we will use this match size
[51:43] reverse thing here so with the restore transform option and this is now placed where the character
[51:50] is and we will simply point deform it by using the original shirt so let's grab our blast and
[51:57] our time shift let's maybe move things around so this is the frozen shirt let's drop a point deform
[52:05] from our simulated shirt and our frozen shirt should be our rest so the second input in our
[52:12] point deform and third input for our point deform is going to be our moving shirt so this is before
[52:19] the time shift where our shirt has all the animation so if I look at the point deform now we should see
[52:25] our simulated cloth matching the movement of our regular shirt and this is the result so we can see
[52:33] that everything works there are a few settings here on the point deform that we can take into
[52:37] account but for the most part we can see that the default settings the default values over here give
[52:43] us a pretty good result so we can also overlay this with our cloth and our character let's go ahead
[52:50] and drop a null here and I'll rename this to out shirt let's go up and let's preview everything
[52:57] together and for our import character let's go ahead and remove the shirt from here so press S
[53:04] grab this shirt and press delete just so we can preview this without the shirt because we are
[53:08] replacing this and if I go up we should only see the shirt with our wrinkles and maybe to preview
[53:14] this faster I will disable this valon pose process just for now so we have a little bit faster
[53:20] playback let's go in our camera and let's press play so this is what we get and we can see this
[53:26] very cool effect that matches the width of our cloth we also have this sort of wind affecting
[53:33] the shirt as well so this is a really cheap effect really fast setup and we can see that it holds up
[53:41] of course this works for this shot because it's pretty static the movement of the character is
[53:47] not super fast and dynamic so it probably doesn't hold up in some cases but it can work in some of
[53:54] these slower moving cinematic shots and it's just fun to do things a little bit differently now
[54:00] we run into a small problem here where the shirt because we don't have proper collisions
[54:06] it's going to protrude a little bit with our mesh and there's a very easy fix for this we can go
[54:12] back inside our shirt container here let's show objects and from our point deform what we are
[54:19] gonna do and I do this all the time with cloth simulations to sort of force them into place
[54:25] without too much work I can press S and go to my point selection with two let's grab a point that's
[54:33] around the area that we are interested in so maybe this one I'll press T to drop down a transform
[54:39] node let's press M to switch the gizmo to worldview and I'll just drag this point out and then I can
[54:46] use the scroll wheel if I scroll up I can turn on the soft selection radius here and as I scroll up
[54:54] I increase the soft selection radius and I'll just drag this out slightly until it no longer intersects
[55:00] so what's cool about this and why this works with cloth simulations and this probably doesn't work
[55:06] with any other type of simulation is that the topology is consistent between frames so because
[55:13] the topology doesn't change this transformation here this soft transformation will be preserved for
[55:20] all of the frames so if I preview this let's go to our null we can see that let's maybe go up we can
[55:27] see that and let's turn off the cloth we can see now that this transformation gets applied for all
[55:34] of the frames now we have a lot of stuff here that's not really working well with our mesh but this
[55:40] is obscured by the cloth anyway so I will be okay with that so we can preview a few more frames but
[55:47] I think everything holds up nicely for the most part we can see here at this frame for example
[55:54] we also have this protrusion with our cloth so what we can do is jump inside our cloth and
[56:01] after our group delete here let's show objects we can do the same thing for our cloth I will go to
[56:07] the last note here press S grab one of these points up here at the top press T go into transform mode
[56:15] move this around a little bit and then increase with my scroll wheel the soft selection and I'll just
[56:21] move things slightly till it no longer intersects all right so as long as these soft transform
[56:29] operations are really subtle just enough so that it doesn't further protrude with other
[56:35] geometries these are completely fine and it's something I do in production all of the time we
[56:41] can see that the simulation movement is preserved throughout the whole duration anyway so if I go
[56:48] to this frame and disable this we can see this popping happening here and we can probably we
[56:55] probably need to check all the frames and make sure that we don't have any other intersections
[56:59] and stuff like that but this will be up to you because you will probably have different results
[57:05] anyway and now we can move forward and now finally we can take care of the smoke and dust so we'll


### Smoke & Dust [57:07]
**Transcript (timestamped):**
[57:12] create a new geocontainer and this will be our effects smoke and dust let's disable maybe all
[57:20] of this we only really need to preview our geometry and I'll preview the out character without this
[57:25] blasting here let's step inside let's show all objects we'll need to reference our character
[57:33] here so we know where the bounds of our simulation should be and we can start by creating the source
[57:40] so let's just simply drop a box from here I'll press enter so we have the gizmo controls and
[57:47] I'll just scale this up and try to match roughly the walking distance that the guy travels here
[57:55] so maybe something like this will be fine we also want to have some room here in the back as well
[58:01] and of course we need to raise this up a bit now the thickness of this box matters quite a bit
[58:07] because we are going to create volumes based on this so the thicker we have this box the more
[58:15] smoke we are going to generate and we only really want to generate a bit so I'll just keep this
[58:21] I'm just eyeballing this value and I know this from previous experiments that this is roughly what
[58:26] I want just have a little bit of thickness so it's not really thin like a sheet of paper so we
[58:34] can settle for something like this and come back later and adjust maybe raise this up slightly
[58:39] and we actually need this to be on the ground we can link up these two values here so I'll right
[58:45] click copy parameter paste relative references below and I'll divide this value by two so now this
[58:52] will be always on the ground and let's also look through the camera and make sure that our box isn't
[58:58] showing here so with this camera viewport selected I can hold down control and press 2 and in this
[59:05] viewport in the side view here I can press space bar F and we can maybe bring this a little bit
[59:11] closer we just have to avoid the box showing in this camera view here so we can actually bring
[59:18] this way closer we don't really we want to have some space here just so we have realistic results
[59:24] and something like this should be fine like I mentioned we can come back and adjust this maybe
[59:30] this box is even a little bit too big so I'll scale this down on all sides here and this should be
[59:36] fine maybe make this thinner let's go back to a single view and let's turn this into a volume so
[59:43] we'll do VDB from polygons we'll turn on fog VDB disable distance VDB and let's reduce the voxel
[59:51] size the final resolution that I used was 0.02 let's set this to 0.05 for now and we want to
[59:59] introduce some noise to this fog so this will be our density source and with any pyro simulation we
[60:05] want to have a lot of variation in the density source so let's do a volume noise fog from here
[60:13] we'll set the operation to multiply and we also want to enable remap values here let's expand this
[60:22] and let's set this to B spline and I'll add another point here and just drag this down so we have this
[60:28] exponential ramp thing going and I'll even squeeze these values a little bit we just want to generate
[60:34] small patches of smoke which will be pushed around by the wind and because we are going to animate
[60:40] these values so let's also go here and turn on animation let's check our pulse duration and I
[60:47] think maybe the default values will be fine so we can see that because we animated this density here
[60:55] we'll generate some smoke coming from over here and then it's gonna go from over here and over
[60:59] time with enough pre-roll it's going to very easily fill up this entire space that we need
[61:05] we will maybe come back to this later let's go ahead and set up our pyrosolver setting so I'll go to
[61:11] the first frame 950 let's drop down this pyrosolver and let's set the voxel size here to 0.05 and in
[61:19] fact we can link this up so I will copy parameter and let's paste relative references for our VDB
[61:26] from polygons and let's take a look at the settings here so right away because we want this to be a
[61:33] very chaotic moving smoke and have that feeling of energy and fast movement I straight up increased
[61:41] the timescale here and I used a value of 1.7 and because this is now increased we are probably going
[61:48] to need more sub steps so I will just increase the max sub steps here to a value of 2 let's go
[61:55] further to our bounds and we can give this a container where our simulation can live so if I
[62:04] we can turn on limit maximum size and I'll press enter and let's make sure that this encapsulates
[62:10] encapsulates our box so I will hold down shift and template my box as well and use my box as a
[62:17] reference here so this is where our smoke is allowed to be and we can squeeze this and also here
[62:26] at the ground and up here at the top we don't really care that much but something like this will
[62:33] be fine let's also go to collision and we want to collide with our floor so we will go to ground
[62:39] planes and we will set this y ground plane let's close below and the value of 0 will be fine which
[62:46] is where our ground is let's go to sourcing and here we can disable or we can get rid of all of
[62:53] our sources we only really need the density here for our fields we can turn off dissipation because
[63:01] when our smoke reaches the bounds of this container it will no longer simulate so we don't really need
[63:07] to worry about dissipation let's also turn off the flame field here and in the shape tab let's for
[63:13] now turn on our wind and we don't really need this buoyancy option here but because we are not using
[63:18] temperature fields for the wind speed I used a value of 2.2 so I want this to be moving quite fast
[63:26] for the wind as well and the wind direction the value of 1 on the x will give us the direction
[63:31] that we need but I decided to push the smoke downwards a little bit as well so I set the
[63:37] second value here which is the y value to a negative 0.2 so let's see what these settings will give
[63:43] us for now and we are not going to use the built-in pyrosolver microsolvers at the sub level over
[63:50] here we're going to dive inside and use our own guess microsolvers but let's see how this looks
[63:56] for now okay so we are off to a good start and this is roughly the speed that I'm going for
[64:04] we can see that very quickly we can fill up this entire region which is great we might want a little
[64:10] bit more smoke in the back so I can increase or maybe reposition this box a little bit so it covers
[64:17] more on the backside of the character and now we have to readjust our container as well so let's
[64:24] make sure we are not cutting off the smoke that we want okay let's go back so this will be fine
[64:31] for now this preview is not entirely accurate because we can change the shading later in
[64:37] rendering so we can drop down a pyro big volume and just increase the density and also let's
[64:44] tint this smoke a little bit so it's more so it's better representing of the colors that we are
[64:51] going to end up with okay so we have something like this and we can look through our camera sort of
[64:57] get a feel where we're at okay let's now work on our guess microsolvers so we can really get the
[65:04] look that we are after and we'll double click the pyrosolver to jump inside and we're going to plug
[65:10] everything inside this advection output let's start with a guess turbulence and right away if we look
[65:17] at the default settings we actually have to preview this I'll pin this at the top level here so we
[65:23] can actually see what we're doing right away we have a little bit of turbulence so this is already
[65:29] looking a lot better and depending on the kind of result that you're going for and how chaotic you
[65:35] want the simulation to be these settings will matter a lot but generally what I like to do
[65:40] especially with these type of simulations is use a noise for larger movement changes so I will
[65:48] increase the scale here quite a bit and also the swirl size by a lot and let's preview this now
[65:56] so this will create the general motion of our smoke and we can see now that we really start to have
[66:04] a lot of features in our smoke and a lot of breakup and really just a lot of chaos so now
[66:10] it's starting to actually feel like a sandstorm and on top of this I like to layer a smaller
[66:17] version of this noise so we can actually rename this to turbulence big and we can duplicate this
[66:24] and this will be let's go with turbulence small and we'll just simply merge these together and
[66:30] this one will be designated for smaller features so smaller breakups and stuff like that and let's
[66:39] reduce the scale here quite a bit because we also will reduce the swirl size so if we compare these
[66:45] two we can see the difference and again this is just for smaller breakups and this isn't
[66:51] going to be necessarily super noticeable if I play this it's not entirely accurate what we're
[66:58] previewing here because we don't have enough voxel resolution so when we increase the voxel size
[67:05] or rather decrease it to increase the overall resolution for the smoke this second gas turbulence
[67:11] will be a lot more noticeable all right and as the final thing we can also introduce some gas
[67:18] disturbance so let's drop down a gas disturb and this will sort of be even smaller breakup of our
[67:25] noise plug this here and the default strength of 25 was fine I just changed the mode here to block
[67:32] based which gives the best results and also I will turn on this rotational force option here
[67:39] which will mean essentially that the gas disturb will affect the parts of the smoke that are moving
[67:45] faster it will affect those parts more and leave the calmer parts undisturbed and this is what's
[67:52] going to create a nice variation in the features otherwise if we don't turn this on and we keep
[67:58] the same gas disturb intensity throughout the whole simulation it's really going to break up the smoke
[68:04] too much and it will sort of diffuse everything so that's definitely a look that you can go for
[68:10] and it's possible that you may actually need this in certain types of simulations but in this case
[68:17] we don't want that so we will turn on this option and let's go up to our pyrosolver settings and
[68:23] let's just increase the voxel size for the original simulation that I did I used a voxel size of 0.02
[68:32] so let's set this up here and let's play the simulation for a bit and also let's go back to
[68:38] our pyrosolver and not forget to turn on some settings in the output tab here let's only export
[68:45] our density and we'll also need our velocity so we don't really need any of these other fields
[68:50] let's also convert this to vdb just because it's lighter and it's always worth doing and we have
[68:56] this option here add weight to velocity field so let's turn this on because in the fields tab or
[69:01] rather the shape tab we are using this field option here we want to add this to our simulation
[69:08] I don't really know why this option isn't turned on by default or why this is even an option
[69:14] because we always want to have the correct velocity being exported by the noise but whatever
[69:22] just turn this on and again this is to export the correct velocity so we can run this now for a few
[69:28] frames we can see now that this is running a lot slower and this is and this is of course a normal
[69:34] thing with all kinds of simulations I'll just let this run for a few frames so we can already see
[69:40] a lot of cool features starting to form here and it looks a lot more like an actual sandstorm
[69:47] let's maybe increase the density even more just to see these features better and let's maybe go up
[69:54] and I have a distant light here and we can turn on the normal lighting option here and maybe I can
[70:00] increase the intensity let's increase this and the shadows okay so we end up with something like this
[70:09] and let's look through our camera so this is pretty good already now if I check my grid here if I go
[70:17] to the information this is the grid that we are dealing with now which is roughly 450 on the widest
[70:25] dimension here so the z which is still pretty low we are only running 10 million voxels it's
[70:33] honestly kind of low we can probably go even further we can probably set the voxel size here to 0.015
[70:41] for production I might use 0.001 and this will of course give you a better result overall for this
[70:48] tutorial I'll keep the size as it is and I'll leave it up to you to simulate at a higher resolution
[70:54] if you want to so from here I can just do a file cache and I'll just save this as let's use a smoke
[71:01] and I will save to disk and this will be our smoke simulation and now that we have the smoke we can
[71:08] start working on the dust let's check maybe some few frames here and for the most part I'm pretty
[71:13] happy with this some of the main settings to take into account is of course all of the gas
[71:18] micro solver settings here so our noise settings and the disturbed one and also the volume noise
[71:25] fog options here give a different result so for example if I wanted more smoke I can simply drag
[71:32] over this point here and allow less noise to really eat away our density source so let's maybe
[71:38] bring this down back and this is completely up to you depending on what kind of look you're going for
[71:44] and let's maybe preview through our camera as well and we have a lot of details here and variation
[71:50] so this will be fine let's go ahead and drop a null from here and let's rename this to let's go
[71:58] without SMK for smoke and now we can use the velocity field here to affect our particles
[72:06] let's start from roughly the same source so we want to have a source for the particles that's sort
[72:12] of the same as our initial box for the smoke so from our box here I can press S and press 4 and
[72:21] just select this polygon over here because we only really need a thin surface so I'll press delete
[72:27] and let's go ahead and disconnect this blast node and start a separate chain over here to the left
[72:32] and for this blast let's delete unselected so we only have this plane here now let's create our
[72:38] source so we want to scatter some points and we want to randomize these points per frame we will go
[72:44] to our global seed here and let's use the dollar sign ff expression let's disable iteration relax
[72:51] iterations here and we'll have to readjust this force total count let's just spawn a few points for
[72:58] now maybe let's also press D and go to the geometry here and reduce the point size back to a value of
[73:05] 3 so this is the source that we have right now now we can use this source as it is directly inside a
[73:10] pop network and we would get a pretty good result but usually what I like to do is introduce some
[73:17] noise into this as well so following the same principles that we did for our density here
[73:23] where we added the noise let's create a noise attribute so let's drop down an attribute adjust
[73:29] float let's rename this to noise and we will set the operation let's set always pattern type let's
[73:37] use noise and we can preview this if I click on this icon over here we can see our noise pattern
[73:43] and we also want to animate this so let's turn on anime noise and probably the pulse duration of one
[73:50] should be fine and what we can do from here let's maybe let's turn off our visualizer let's use a
[73:58] blessed node and let's get rid of any points that are above a certain value of this noise
[74:06] attribute that we created so over here we can run this over points and here we'll say that
[74:13] we'll add an expression and say that if this noise value is bigger than 0.5 we'll get rid of those
[74:20] points so it will create these patches of points and as a result the simulation will have a sort of
[74:27] clustering nature to it which overall gives a little bit better result let's maybe adjust our
[74:35] noise now and we can play around with the remap ranges here we can maybe get rid of more points
[74:42] we can also increase or decrease the element size maybe we can decrease this slightly we can also
[74:48] go to our fractional settings and if I increase this roughness value we can start to introduce more
[74:54] stray points so we can also have just slightly more variation and if I increase the force total
[75:00] count we can see the pattern that we have here we don't really need as many points obviously we can
[75:07] go back to this value and bring in more particles if we want but this will be a good source to start
[75:14] with so from here we will do a pop network let's run this from frame 950 and go back let's step
[75:22] inside and for our pop sources because we don't have any surfaces we'll set this to all points and
[75:29] let's disable the guide let's go to our birth tab and let's maybe make this last one second for now
[75:37] we'll come back and readjust this but first we want to add back them with our velocity field so let's
[75:42] do a pop add back by volumes let's go up and let's grab our smoke and let's paste this over here in
[75:50] our soap let's the field name will look for velocity which is what we want add action type let's use
[75:56] update position and let's use velocity update let's do final velocity so with these options we will
[76:02] have the most accurate advection so it will move one to one with our velocity field so if I press
[76:08] play now we can see that this is what we have and for the most part we are getting what we want let's
[76:14] maybe turn the display here let's maybe use pixels instead we can also preview this through our camera
[76:19] we can see that we have this kind of obvious pattern to our particles here and they have this
[76:25] gapping step between them and this is because the velocity is roughly moving at the same speed
[76:32] we can alter this a little bit if we turn on this use of expression we can modify this velocity
[76:37] scale per point so this parameter is called well scale so let's go ahead and type here well scale
[76:44] and we will do a multiply equals and we'll multiply this with a random value for each
[76:50] particle that goes maybe from 0.5 to 1.5 so this will give us enough difference between each point
[76:58] to break up this sort of stepping uniform result that we get here so let's generate a random value
[77:05] based on our seed and then we can do a fit 0,1 expression and we want to map the 0 to 1 ranges
[77:15] that the random generates to a value of 0.5 like I said and let's do 1.5 for our higher end and now
[77:24] if I replay the simulation we have a lot more variation and we successfully broke up that
[77:32] weird looking stepping shape so press play and now we can also probably tell that a life expectancy
[77:40] of 1 should be fine in this case I think we might want to spawn more or less particles I think we
[77:47] maybe won less particles so let's go to our scatter here and just reduce this maybe to a
[77:53] maybe to 1500 instead of 3000 so we end up with something like this which is closer to what I
[78:01] originally had I think and we can see that a lot of these particles that are being pushed out of the
[78:08] area where our velocity field is when they no longer find any velocities to be advected by we can
[78:15] see that they start to freeze and we can just go ahead and delete these let's use a geometry
[78:22] vop here we will need to grab the speed of the particle so from the velocity we will compute
[78:29] the magnitude so let's use a length node and this will give us the speed and we can compare this
[78:36] let's drop down a compare and we'll say that if this is less than or equal to zero we are going
[78:43] to go ahead and remove those points so we will do an if block over here and this will be our
[78:51] condition the bool result of our compare and over here we will do a remove point and we will run
[78:58] this over all of our points so we will just grab the ptnum value here and point it to our ptnum
[79:04] and we can see now that this removes all of those particles that are stuck so when a particle no
[79:10] longer has any velocity to it we will just remove it because we don't really care about it it probably
[79:16] doesn't make a lot of difference in this case I think you can simply skip this operation honestly
[79:22] if you want but it's still something worth knowing how to do because you might apply this at other
[79:28] simulations so this is it for our particles and we can also overlay this with our smoke and see
[79:35] how these line up let's maybe use the second preview here and this is what we end up with maybe the
[79:41] particles are moving a little bit too fast so what we can do is go back inside here and for our
[79:47] random destination values here we can go from 0.3 let's use a maximum value of 1 so this will mean
[79:55] that at most they will receive the full force of our velocity and not go above that so this should
[80:02] prevent our particles to really going way too further out of our velocity so I think maybe this
[80:07] is matching the smoke a little bit better for the most part okay so this will be fine let's go ahead
[80:15] and we mentioned in the beginning of the course that we are going to render these as geometry so
[80:22] we are going to create a simple sphere and let's set this to polygon and just increase the frequency
[80:29] here a bit and we will noise this up with a mountain sop all right let's let's disable noise along
[80:36] vector and I want to use a worldly cellular noise to start with let's increase the element size
[80:44] decrease the amplitude so we can see that this worldly noise gives us this kind of rocky shape
[80:49] by default which is really great for this kind of operation maybe we can also play around with
[80:55] offset until we get something that looks a little bit cooler so maybe something like this might increase
[81:01] the amplitude even more let's decrease the maybe we'll keep the element size as this and we'll use
[81:08] a second noise on top of this just to add even more details so smaller frequency or rather higher
[81:14] frequency details for this operation we can do something like this now because we are going to
[81:19] use motion blur on this doesn't really matter that much the shape that we end up with we just
[81:26] want to make sure that it's a little bit irregular so we're not dealing with just a simple sphere
[81:32] we also want this to be right at the origin in order for the copy to points to work properly so
[81:38] let's also do a match size which brings it right here where we want it and now we can grab our
[81:45] particles let's do a copy to points from our sphere and plug our particles as the template points
[81:52] and let's see what we end up with let's also pack an instance our geometry so we don't waste any
[81:58] memory trying to replicate the actual geometry on all of the points and we can see that this is now
[82:04] very fast operation of course we'll have to modify some attributes on our particles
[82:09] let's start by doing an attribute randomize and let's take a look at our p-scale so we'll set
[82:14] the attribute name here p-scale let's use distribution we'll use one of these other ones
[82:20] let's try custom ramp and let's say that we want to fit the lowest and maximum values we'll go from
[82:28] 0.2 to maybe 0.6 which should give us enough variation between the size let's also turn this
[82:36] into a b-spline ramp and we will do another exponential ramp over here which really is the
[82:42] best for this kind of distribution for the points and we will need to decrease the global scale
[82:48] overall until we match the size that we need so let's maybe start with a value of 0.01 and also
[82:56] turn on show all objects and look at our character as well okay and we can maybe look through our
[83:05] camera and this is what we have we might want to increase this global scale let's maybe try
[83:10] 0.02 we shouldn't really go too high above we will need to come back to this value after we
[83:17] do some test renders and check out the motion blur because this scale will really affect the final
[83:23] output that we have so it's not really worth spending a lot of time at this point adjusting the
[83:28] scale but we are roughly in the ballpark of what we need now whenever we are working with particles
[83:34] we have to go to the option here and let's turn on to use the C-Detribute ID otherwise the p-scale
[83:40] will change for each particle each frame and this is not what we want one other thing that we can
[83:46] randomize also is going to be the orientation so let's also do another attribute randomize
[83:52] let's randomize our n attribute and for this we'll use inside sphere which will just give all of our
[84:00] particles a random orientation so we can maybe zoom in on some of these and we can see as I turn
[84:06] this on and off they're all facing the same direction now and with this they're all facing a
[84:11] random direction also for this we want to turn on the C-Detribute option here and for the most part
[84:17] this is all we have to do for our dust layer and the only thing left to do here is maybe clean up
[84:25] all the attributes to prepare this for bringing it into Solaris so let's get rid of any attributes
[84:31] that we don't need we'll drop an attribute delete we will want to keep our n and p-scale which is the
[84:39] attributes that we adjusted here so we will obviously want to keep those let's delete non-selected
[84:44] and we also want to keep our velocity and this will be necessary for motion blur and these are
[84:50] pretty much all the attributes that we need we might want to increase their life a little bit
[84:56] longer some of these particles that have a lower advection scale might die off a little bit too
[85:03] soon so we can go inside the pop net and we can increase the life expectancy let's maybe just
[85:08] double this and I can reset the simulation all right so we can go in our camera and we can preview
[85:13] this and I can pretty much say that we are off on the right track like I mentioned earlier we'll
[85:21] probably need to come back and adjust the p-scale here but we can save out this simulation and because
[85:26] we want to adjust the p-scale later let's go ahead and do a file cache before our attribute
[85:32] randomized nodes we'll drop a file cache here and this will be our dust prt and we are going to save
[85:39] this to disk and from here we can do another null here we can do another null and I'll rename this
[85:45] to out dust prt and with this we have everything we need we can now import all of these layers in
[85:53] Solaris and settings up and start working on our render layers now we can bring all of our elements


### Solaris Setup [85:58]
**Transcript (timestamped):**
[86:01] into Solaris and let's start by bringing in the character related items which is the shirt and
[86:07] cloth and let's start actually with the shirt which is the easiest one let's go ahead and step
[86:12] inside here I will grab this null here out shirt and I will control C and let's go ahead and press
[86:20] N and jump over to the lob stage and over here where we have our character let's do let's do a
[86:27] sub import first of all to bring in our shirt and we want to sub layer this over our existing shirt
[86:35] that we have and this means that we are going to retain this material assignment so we don't have to
[86:40] reparent everything this will essentially just overlay the mesh of this shirt let's jump into
[86:47] the Solaris desktop here that I have and for this layering to work we need to have the same path that
[86:54] we have for our shirt we need to have the same path over here so if I look at this sub layer here
[87:01] which is going to be our character we have this character group so this chr group and inside this
[87:08] we will find our body group which is another group and then finally here we should have our
[87:14] shirt mesh which is this shirt 001 so we have to match this path that we have so in our sub
[87:21] import let's go ahead and try to match this for the import path prefix let's place this inside the
[87:27] chr group and then inside the body so now we roughly have the same thing the mesh name has to be
[87:34] the same as it is also so if we look at this again this mesh name will be shirt 001 and this is mesh
[87:42] 0 which is the default that Houdini gives us let's jump back to the object context here and let's jump
[87:48] back in our affects shirt container and over here where we have our let's know the edit one we can
[87:55] just simply append a name sop and this will override the name that we have and for this we want to give
[88:01] this name here let's set this to shirt underscore 001 so you can use whatever name you want here it
[88:08] just has to match the naming convention that we decided for our character and we can see this in
[88:14] our scene graph here the mesh name updated to this shirt 001 so now let's jump back to Lops
[88:22] if we do a sub layer from our anim node we can simply point our sop import let's plug this as our
[88:31] second input here and when we do this we can see that the shirt updated and even though we don't
[88:37] have the same topology so if we move over here and I press shift w to preview the wireframe we can see
[88:42] that the because we added the subdivisions we don't have the same topology but because we are using
[88:48] the same name and path this will replace our original mesh entirely and we still have the
[88:55] material assignment so if I press shift r we don't have any light here let's maybe go to our
[89:01] last node here where we also have the physical sky so I'll just do a quick preview let's maybe
[89:06] increase the light intensity or maybe increase the exposure we can see that this works now so our
[89:13] material assignment was preserved and this is the simulated shirt which has all of the wrinkles
[89:20] from the ripple deformer so it's a pretty cool way to work this way in Solaris I think it's just a
[89:25] matter of getting used to working this way but once you do you can really start to take advantage
[89:31] of all of the benefits that the usd pipeline provides so this will be our shirt and we can
[89:37] go ahead now and let's bring in our cloth so let's step inside here and for this let's grab this
[89:44] control c bring this over to lops and do another sop import because we don't have any pre-existing
[89:51] material for this so I'm just gonna paste the sop f here and we will simply do a merge and just merge
[89:56] this in our chain and we can check some frames here and see that this is working let's maybe
[90:03] go back here and not forget to turn on our valon post process back so we get our thickness as well
[90:10] now we don't have to worry about any sub layering here because we don't have an existing material
[90:15] for our cloth we are going to create this ourselves let's maybe still place this inside the character
[90:23] folder at least so in our sop import here we can set this in the car directory and let's maybe
[90:30] also make a new directory let's place this in car slash cloth all right so we can see this hierarchy
[90:37] here and when we go to our merge we are going to have everything nicely organized let's go ahead
[90:42] and create this material so after our sop import let's do a material library and let's step inside
[90:50] we will do a karma material builder we can rename this to cloth and let's step inside here and get
[90:58] rid of these because we won't need only the standard surface let's just start with some basic values
[91:04] here i'll just drop down the base a bit to check that this is working and for the specular i'll just
[91:09] increase the roughness let's go up let's go up one more level and let's let's autofill materials
[91:16] which will bring the materials in this material library and also use this to assign it to the
[91:21] geometry and we can drag our cloth path right over here inside the geometry path and now if
[91:28] i do a test render let's maybe set this to okay this is set to karma exp so this is fine now if i go back inside our cloth
[91:36] we should see our material updating so we can see that this works and we can start building the material
[91:42] let's set the base back to a value of one and i just want to map a few noises on this texture that sort of
[91:49] will be this dirt layer so we are going to keep this fairly simple although you can build quite complex
[91:57] shaders with material x so let's just go ahead and drop down a mtlx fractal 3d and if we plug this
[92:05] directly inside the base color we should already start to see something and we do so here we have it
[92:12] we will need to adjust some settings here but first we will need to make this pattern a little bit
[92:17] smaller so we can map this to the position so we can drop an mtlx position node which essentially
[92:26] just brings our wall position but this will make it so that the noise doesn't stick to our cloth
[92:32] and this is why we created that rest attribute on the geometry so the way we import attributes is by
[92:38] using a prem var reader and in here we just have to specify what attribute we want var name will be
[92:45] rest and the signature is going to be float tree so if i plug this now in our position so this
[92:51] works exactly how it would in vops as far as the noise being generated on the position we just have
[92:57] a few different settings here so spread shift r and if i preview some more frames we can kind of see
[93:03] that the the noise is sticking to the surface of the cloth and it's moving alongside with it so this
[93:11] is what we want and in between here if i multiply the value of this position we can decrease the
[93:18] scale of the noise so we can do a multiply here and let's set the signature to vector 3 f a and
[93:25] if i increase this now we can see we modify the scale of the noise let's do something like this
[93:32] and go inside our fractional node and i will i will increase the lecunarity to start and maybe
[93:40] also let's leave the amplitude as one and this diminished value can also have a big impact
[93:46] on how our noise looks let's maybe do something like this i can maybe decrease the lecunarity and
[93:52] increase the octave levels instead so i think this is starting to look kind of like dust of
[93:59] course this is way too white so we can drop a ramp in between and this will be the karma ramp
[94:05] constant not the regular ramp parameter let's use this one instead and the signature here let's use
[94:13] let's keep this as vector and for the colors we want to use instead of white let's use something
[94:19] like a sand color so i'll go towards this orangey color and let's desaturate this a bit and drop
[94:26] down the intensity so let's do something like this i'm not gonna spend too much time adjusting all
[94:32] of these settings because i will i will let you do this just so i'm not wasting too much time and
[94:38] for the most part this is already starting to look kind of the way i want i might also want to
[94:44] introduce a little bit of brightness or value in this other color here which is our blacks
[94:52] let's leave this like so and maybe i can play around with the scale of this so i think this is
[95:00] starting to look pretty decent this obviously needs a lot more fine tuning than this let's maybe for
[95:07] now just decrease the overall value and saturation and we can settle for something like this maybe
[95:14] finally let's decrease the diminished value here a little bit as well all right and we can do the
[95:20] same thing to layer an additional noise on top of this so we can just go ahead and grab all of
[95:27] these layers let's grab these three ones and hold down alt to duplicate let's plug this to preview
[95:34] just this new layer and for our work we want to offset this value a little bit so we can just do
[95:41] an add here and offset this value like so all right just so it's a different pattern and we might
[95:48] want to let's increase this and let's make this a little bit more white all right let's do something
[95:55] like this uh diminish this even more or rather decrease the diminish value here okay and we'll
[96:02] just simply add these layers together so we'll do an add here and now we have just two layers of noise
[96:09] again to just have a little bit more variation now this doesn't look all that great because we really
[96:15] need to spend a little bit more time adjusting the values here i might also want to use a b-spline
[96:20] value here and i can squeeze this white noise a little bit more to something like this okay but
[96:28] hopefully this gives you an idea on how easy it is to create some interesting materials directly
[96:33] inside of karma we also see a little bit of protrusions over here with our shirt and again
[96:39] all we have to do is simply go inside grab the mesh with an edit node and use a soft transform
[96:45] to bring this further out so that it doesn't intersect or we can grab the shirt that's underneath
[96:51] and push this down in the opposite direction now in my original renders i also used um i also used
[96:59] some fabric textures from megascans so i downloaded the this fabric cloth cotton material here and i
[97:07] used only the roughness and the normal textures from this so i'm gonna go ahead and bring this
[97:12] in the material x editor so we can do an empty lx image node and let's point let's go ahead and
[97:21] grab the normal here and this signature should be a vector tree and let's also grab the roughness
[97:29] let's go ahead and look for our roughness let's take care of the normal first so this has to be
[97:34] plugged first inside a normal map node and then this is going to be plugged inside the geometry
[97:42] inside the normal and we can see this pattern now here we also see that this is a little bit too big
[97:49] for our shirt or rather our cloth so we can change this if we bring out our texture coordinates
[97:57] plug this as our text coordinates which is the default by default but now since we have this
[98:01] we can use a multiply in between and we can set this to a vector 2 fa and if i increase the scale
[98:08] here we will pretty much increase the tiling so now this will tile a little bit more and
[98:15] and the pattern will be smaller and we'll do the same thing let's also plug our roughness so this
[98:21] will be the normal and we want to use the same texture coordinates for our roughness so again
[98:26] this will be our roughness and the signature should be float here plug this in our specular and inside
[98:33] the specular roughness so we end up with this pretty basic i would say but this is again just to
[98:41] give you an idea on some of the things that are possible here we can get pretty advanced with
[98:47] shaders so there's definitely a lot of options that you have and this will be fine for our cloth so
[98:52] we can go back up and this will be everything we need for our character in fact we can probably
[98:59] look at this through our camera and this is the result let's maybe go ahead and change our sky
[99:06] slightly let's lower this a little bit and in the original example i think i used a lower altitude
[99:13] here so it's something like a sunset sun we can also maybe preview the sky for now so i did something
[99:19] like this and i think i used a light that comes over from this side so let's increase the solar
[99:27] azimuth which is basically the rotation of the sun around the orbit so i think i did something like
[99:34] this in the original in the original renders we can see that we have a very sharp shadow here so
[99:40] we can soften this by increasing the angular size so if i set this to 10 we have smoother
[99:46] shadows which i'm not sure how physically accurate it is or not but in my case i like having softer
[99:55] shadow in general with all of the renders maybe we can increase this even further to a value of 20
[100:00] and to have more information i also used a directional light as well or rather a distant
[100:07] light let's drop this here and we will merge this in our lights part over here let's bring this up
[100:14] and for our distant light we can turn on the visibility of our lights and i just want a light
[100:20] that points directly straight down so that's coming from above i'll hold down control and rotate this
[100:27] 90 degrees let's maybe turn off the physical sky for now so we can focus on our distant light
[100:32] and maybe i'll just turn this lightly over our character so this is the direction that i ended
[100:38] up with this is mainly to get a little bit more highlights in our smoke but also our character
[100:45] and overall it's just nicer to have additional light information than not having it at all
[100:51] and later we will export passes for all lights individually so let's turn back our physical
[100:57] sky and in order to split up the uovs per light we will have to turn on some options here we will
[101:02] go in the sun tab for our sky and inside the light we have to set some lpe tags for each light so
[101:09] let's set or create this will be our sun go over to the sky and this will be our sky and then our
[101:17] distant light let's go over to karma tab and we have this lpe tag here set or create and this will
[101:23] be distant all right and we'll set up all of the aovs a little bit later we still have to bring in
[101:30] our effects layers first let's go back to our object viewport and let's step inside our smoke
[101:37] and we'll start with our volume so i will grab this out smk let's go back to lops and we'll do a
[101:44] sub import let's bring this in here and from here what we can do let's give this a path so let's
[101:52] place this inside an effects folder or container and let's place this under smoke and here we have
[101:59] our hierarchy we can also see that we are bringing in both the density and the velocity field now we
[102:06] don't really need the velocity field so we can get rid of this let's do a stage manager from our
[102:12] sopping port and we'll scroll or rather use the drop down here to go to our velocity and I'll
[102:18] just select this and press delete so now we only have our density and we can merge this and let's
[102:25] do a material library from here and let's create a pyro material we'll step inside we'll do a karma
[102:34] pyro material and we can get rid of these aovs let's go ahead and remove this and we can also get
[102:41] rid of the material properties and the inputs so we only want this pyro shader usually I like to
[102:47] link the density scale and the shadow density so I will right click copy parameter and paste relative
[102:54] references and I'll just start with a value of five and we'll work from here depending on how this
[103:01] looks in the render so let's go up I'll rename this to let's do fg smoke so this will be our
[103:07] foreground smoke and we'll use the same smoke for our background we'll just push it further back and
[103:13] scale it up a little bit but anyway from here let's go ahead and auto fill materials and assign this
[103:19] to the geometry let's drag our smoke layer over here and we can do a merge and let's bring this in
[103:27] our chain and we can go to the karma render settings here and let's preview this from our camera
[103:33] press shift r and let's also make sure that this is running on the xpu and we'll give this a second
[103:39] so this is the result and now that I'm seeing this we can adjust the lights further let's maybe
[103:45] disable the distant light for now and we might want to go to our sun settings here let's maybe
[103:52] decrease the solar altitude even more and we can play around with azimuth maybe I also want to make
[103:59] this slightly thicker so I'll go to the material and I will increase the density scale try maybe
[104:06] seven we can further control the density in comp later don't have to worry too much about this now
[104:14] but it's still going to be helpful to get us as close as possible to the result that we want
[104:20] maybe this is too strong I might want to preview some other frames as well all right actually I think
[104:27] this is I think this is looking fine obviously you are free to experiment and use whatever values
[104:33] you see fit let's go ahead and press shift r and let's go up so this will be our foreground smoke
[104:40] and we'll do the same setup really for our background smoke let's go ahead and we'll make some room here
[104:48] and I'll actually just duplicate all of these nodes so the stage manager and the material
[104:53] library and for the stage manager we want to change the name here so this original one that we did is
[104:59] using this path here we can update the path let's try instead of smoke let's set this to bfg smoke
[105:07] let's use underscore and for our second one this one let's rename this to bg smoke and we will also
[105:16] need to update our material library here so let's drag our fg smoke again over here and for our
[105:24] second one we'll drag the bg smoke the reason that we have to modify the path is that if we have the
[105:31] same path for both objects Solaris will simply overlay them instead of combining them so when we
[105:38] set up a different path even though they're the same simulation and the same object as long as they
[105:43] have a different path they will be treated as different objects so with this stage manager
[105:50] I can grab this handle here for the bg smoke and I can drag this further back maybe and let's also
[105:57] scale this up a little bit and drag this even more let's maybe see how this will look in our
[106:04] main chain so I'll just simply merge this here as well and we can see that when we merge everything
[106:09] now we have both objects showing and grab our handle back our gizmo and maybe I have to push
[106:16] this further back do something like this and we'll do I think this looks all right maybe we need this
[106:23] even bigger we just want to make sure that we don't have a completely dark background and for
[106:30] this background layer we want to increase the thickness even more so I will disable the merge
[106:35] with our foreground so we can only focus on this background smoke let's go to our camera and press
[106:41] shift R and like I said for this let's go back in our foreground smoke now I should rename this
[106:47] probably to bg smoke and we will have to update our material library as well so let's use bg
[106:53] smoke okay and step inside and I'll just increase the density here let's maybe try double so 15
[107:00] okay so we end up with something like this and again this is simply just to avoid having a
[107:06] completely dark background we can preview some other frames as well and in my case I think this
[107:11] will be just fine so let's go up and this will be our smoke let's press shift R and I'll actually
[107:18] disable both of these merges for now let's make some room and let's work on our dust so I will go
[107:25] to the object again and let's grab our dust layer from over here so we'll grab this dust PRT
[107:32] and we will paste this inside a new SOP import SOP path over here and we'll place this again in the
[107:39] effects layer and this will be under a dust group let's use a merge and let's just simply merge
[107:47] this directly in our comp and see what we get now by default this SOP import isn't recognizing
[107:55] our packed primitive so if I drop down this dust layer here we can see we have access to all of the
[108:03] thousands of points here and this is not really what we want we want to treat this as a point
[108:09] instancer which will be a lot faster so let's go to primitive definition here and let's check this
[108:15] packed primitives and we want to set this to create point instancer so now we can see we no longer
[108:21] have a layer for each one of the points we only have this instances object and as a result we
[108:28] should be able to I mean it still needs a second to update everything but this is a lot faster and
[108:35] more efficient and it makes sense that we want to work with packed primitives since they are packed
[108:39] primitives at the SOP level now for this layer like I mentioned when we created it we are concerned
[108:45] a lot with the motion blur here so let's go to our karma render settings and in the camera effects
[108:52] we have motion blur turned on by default but we want to turn on this instance velocity blur so
[108:59] these are all instances and they have the velocity attribute so let's turn on velocity blur and see
[109:05] what we get so this press shift R so we can see that the velocity blur is working and we also have
[109:13] the depth of field affecting these and this is pretty much all we need for this layer I can
[109:19] check a few more frames and I think I'm pretty happy with this result to be honest and it's very
[109:24] close to what I rendered originally now you can also assign a material for this because we haven't
[109:31] over here we see that these are a little bit brownish by default and this is because we are
[109:36] absorbing the color of the sun and the sky and I think honestly this will work just fine because
[109:43] we can do a lot of further grading and adjusting later in comp so you can assign a material to this
[109:49] if you want to but I will just leave this as it is and we can move forward and set up all of the
[109:55] render layers and for our render layers let's go ahead and start with the simplest one which is going


### Renders & AOVs [109:56]
**Transcript (timestamped):**
[110:02] to be this smoke here in the back so this is without any of the other layers let's go in Solaris
[110:09] and we'll create separate chains for all of our layers I'll go ahead and press shift R to get
[110:16] out of render view and let's go ahead and just enable all of our other layers as well so the
[110:21] smoke and also this distant light now we want to get rid of all the objects except this
[110:29] background smoke so let's do a prune here which is essentially like a blast and we'll select our
[110:38] background smoke and we are going to prune unselected and we have an error happening over here we are
[110:45] not seeing our background smoke and we can see that this is red which probably means something went
[110:50] wrong and I think this is because I have an existing chain that already uses the same naming
[110:56] convention here so I think that we can see that as I turn this node on enough we get it back so
[111:04] let's go back to our prune over here and into our karma render settings let's go inside the cam
[111:11] and if we do a test render we can see that we no longer have our lights and this is because we
[111:18] got rid of our lights as well so let's also bring our lights here I'll do slash lights which is where
[111:24] all of our lights are placed by default and now we should also have the sky and sunlight so let's
[111:30] set up the aovs for this we're gonna go ahead and for the karma render settings let's go to image
[111:37] output and we don't really need the beauty for this because we are going to recreate this we'll go to
[111:42] the volume and we'll want to have the direct volume and indirect volume as well and for the
[111:48] direct volume we want to split this per lights let's also go to our filters and we are going to use
[111:55] the optics and video optics the noisier on all of these aovs so let's select our direct volume
[112:03] distance we don't need the c aov which is the beauty pass so we have our direct volume distance
[112:11] our sky and sun and we also want this indirect volume the indirect volume is basically the
[112:18] bounces and speaking of which let's go to limits here and we'll disable the reflection diffuse
[112:25] limits we only want to increase this volume limit let's maybe let's use a value of one maybe actually
[112:32] set this to a value of two so let's press shift r and let's see what we get and we'll run this for
[112:38] a second we can already start to preview some of these aovs let's maybe close this and let's go to
[112:45] our render outputs here we can check out our distant light okay so we can see maybe this is too dark
[112:53] let's go to some of these other ones let's go to our sun and this is pretty dark as well let's try
[112:59] the sky most of these are pretty dark because when we add them together we'll get the final result
[113:05] back but we can see how smooth this result is in a relative short time and from my experience the
[113:12] let's go here this nvidia optics denoiser is works really well in a lot of cases but it works especially
[113:20] well with volumes so i highly recommend using this whenever you want to render especially
[113:26] layers like this where it's just volumes this is a match made in heaven so from here we can go ahead
[113:32] and probably for this we can disable the depth of field we can bring it back or we can use a
[113:40] de-focus in yoke ourselves we might not want this just to preserve some of this detail let's maybe
[113:46] go to our beauty output here we want to maintain as much detail in this layer as possible so this
[113:53] will be fine for our background layer and from here we can make sure that the camera is pointing
[114:00] to the correct camera and you can give this a file path and file name make sure you're rendering as
[114:06] exr and we can do a usd render up from here let's select render specific frame range and we want to
[114:14] render from 1001 and we want the delegate here to be karma xpo and most of these settings should be
[114:21] fine for the most part and you can hit render to disk and for our foreground smoke we can pretty
[114:29] much use the same setup let's go ahead and just duplicate all of these nodes and inside this
[114:35] prune node let's go ahead and we want to keep let's get rid of all of these the primitive patterns
[114:41] here we want to keep our character because we want the smoke to be obscured by the character mat
[114:49] and we will need to bring in our foreground smoke this let's actually this replaced our character
[114:56] so let's just manually add our character layer like so so these are the layers that we need
[115:02] let's make a quick render preview and see how this works with the default settings okay and again
[115:09] we forgot to bring in the lights as well so let's also do slash lights here all right so we can see
[115:15] that the character isn't actually we are rendering with the mat but this isn't entirely accurate because
[115:23] in our filter step here already in our let's go to the image output and aovs we unchecked the beauty
[115:31] here so we have to check this and now we sort of have the correct result let's also make sure
[115:37] that we go back to our limits here and let's reset these to the default settings and we'll keep the
[115:43] volume limit as two now we don't really need to see the materials on our character in fact we said
[115:49] that we are going to render this as a mat object so let's do a geometry render settings after our
[115:56] prune and let's point this to our character and we'll go all the way down here to let's go to
[116:03] shading hold out mode let's set or create and we'll set this to mat and now we should have the original
[116:11] result that we had but now we don't have to worry about any reflections and stuff like that being
[116:16] computed on our character and we are only exporting our smoke and again we can check all of our
[116:23] aovs here so we can check the distant one the sky and the sun and also the indirect one which is the
[116:30] bounces and all of these are looking fine we have a lot of stuff to play around with for the most
[116:35] part I think this is it for this foreground layer so again you can set a name for this and a path
[116:43] and we can go ahead and render the same frame range here and render to disk and let's also take
[116:49] care of the dust as well since this is since it will be again a very simple setup we are actually
[116:57] let's start with a fresh chain for this because we are going to need rather different settings
[117:04] we are going to use a prune node and we want to keep only our character and let's manually select
[117:13] our effects and let's select our dust and we will prune unselected so the reason we want our character
[117:19] as well is because we want the particles to be obscured by the mat of the character so in fact
[117:26] we can go ahead and alt drag this render geometry settings for our character and connect this over
[117:33] here and we'll just do a fresh set of karma render settings for this and we'll make sure that this is
[117:41] 1080p and that this is pointing to the right camera and again you will have to set file path name
[117:47] and destination render engine let's set this to xpu and let's take a look at our default settings
[117:55] again so press shift r and again we forgot to set up the lights let's bring in the lights as well
[118:03] we don't really need any aovs for this because it won't really give us that much of an advantage
[118:10] we only need to make sure that this is using the correct camera settings so let's go to the camera
[118:16] effects here and for the motion blur again we will need to turn on this instance velocity blur so I
[118:22] think this is all we need here really let's preview the render and this is it so like I mentioned
[118:29] earlier when we were creating this layer we might have to go back and adjust the p scale so we might
[118:36] want to make these slightly smaller but I think this is actually looking pretty good I'll leave
[118:42] this up to you if you decide that these particles should be smaller all you need to do is reduce
[118:49] the p scale on the particle simulation so we can go ahead and duplicate our render op and we can
[118:55] also render this to disk and finally we can take care of our character let's start again with another
[119:03] one of these prune nodes and we don't need our effects dust we will mainly focus on the character
[119:09] and the lights but we do want the shadow of the smoke of the foreground smoke to affect the character
[119:18] so we will need to bring in our foreground smoke as well so let's go to our effects to fg smoke
[119:26] and this will be fine now we don't want to see the smoke we only want the smoke to affect the
[119:32] shadow so we will need some render geometry settings for the smoke let's maybe go up here and
[119:40] let's point this to our again we'll go to effects fg smoke and for the options that we need we have
[119:49] to go to shading and we need this render visibility so let's set or create and the option that we
[119:55] want to choose here is going to be invisible to primary rays so this will mean that the smoke
[120:02] itself will not be rendered but any interaction that it has with objects will be rendered so it
[120:08] will render all of the shadows caused by the smoke and also the reflections so this is what we want
[120:15] and maybe we can choose another frame here where the smoke is more in front of our character let's
[120:21] do another karma render settings node and again i'll use hd tv and xpu and we'll need to point to
[120:30] our camera here so let's take a look at what we have so hopefully we can see now this part here
[120:36] in the back which is a lot more in shadow and this is where our smoke is on top of our character so
[120:42] we must maintain this interaction between the character and the smoke now for the aovs that
[120:47] we need here we do need quite a few aovs so let's go to the image output and we can leave the beauty
[120:54] for this to be honest we probably don't need it but we'll just keep this on let's go in our diffuse
[121:00] tab and we will want the combined diffuse and we will split this per light and also then in
[121:07] reflections we will want the combined glossy reflections and also split this per light in our
[121:13] lights and emission we can probably check the direct emission to isolate our eyes which has
[121:20] an emissive material but we are going to create the eyes layer using a different way so we don't
[121:26] have to worry about this so with all of our diffuse and reflections aovs when we put them together
[121:32] we'll recreate this render that we have here we do need some extra utility aovs however so we'll go
[121:39] inside the extra render vars here let's hit this plus let's first get our cryptomat for the material
[121:47] id so we'll scroll all the way here and we'll use cryptomat material name and this automatically
[121:53] sets everything up let's use another one and we'll grab the uv information so we can map
[122:00] different textures inside of nuke later let's rename this to uv we'll leave the format as
[122:07] half three but for data type we want to use a tree float or rather a float tree as it says over here
[122:14] and the source type will be a prem var and really the attribute name is uv but when we switch over
[122:22] to solaris some of the attributes get renamed and in this case uv is named st all right we don't have
[122:30] to worry about the pixel filter and we need a couple more aovs as well let's hit the plus one
[122:38] more time and in order to create a fresnel shader in nuke the fresnel shader is basically just a dot
[122:45] product between the camera origin and the surface normals of the object so we will have to grab
[122:53] there is a preset that hudini set up for us here for ray origin and then we'll do one more
[123:00] for our normal so let's scroll all the way down and let's select here let's go to our end and we'll
[123:08] choose this smooth normal preset and we will press start and let's take a look at some of these layers
[123:13] so we have all of these combined diffuse and combined glossy reflection and we can check some
[123:19] of these out and the combined diffuse is mostly for our cloth and stuff like that and then we have
[123:25] the combined glossy reflection which is all of the specular and reflective information and finally
[123:32] we have our crypto material to separate all objects that have very different material we have our
[123:38] geometric normal and again this is used later in nuke with our ray origin to create that
[123:45] fresnel shader so this will make sense in a second and finally we also have our uv and this is going
[123:52] to be all we need so with this being said we can duplicate this usd render op and we can also render
[123:58] this to disk and like i mentioned if you don't want to set all of these renders up yourself but you
[124:04] want to follow along with the compositing part i've included all of the render files you just have to
[124:10] download them following the link in the links file and this was it for the hudini part so now
[124:15] let's jump over in nuke and now in nuke we are going to start from the back and work our way


### Nuke BG & Character [124:16]
**Transcript (timestamped):**
[124:23] towards the front so this means that we are going to start with our background smoke now again i've
[124:29] included these renders that i'm using here in the link in the downloads archive in case you want
[124:35] to follow along so i'm just gonna start i'm just gonna press lc and just duplicate this read node
[124:42] so this will be the background noise let's start splitting up the aovs and rebuild this
[124:47] so we are going to use a shuffle and just to reiterate this if i press s and go to my project
[124:53] settings these are the settings that i'm using so 1001 to 1120 full hd 1080p and inside the colors
[125:03] i'm using that hudini configuration and color management set to ocio so back to our shuffle
[125:09] node we want to see the aovs that we are shuffling so we're gonna go to this node label here and in
[125:15] between brackets we will add the expression value in one all right and now if i go to the shuffle
[125:22] node and select one of these aovs let's start with our direct volume distance we are also going to
[125:29] have the title of this aov over here in the shuffle let's add a dot over here with control
[125:36] and we will do a merge let's go ahead and duplicate both of these nodes without c
[125:42] and we are going to connect a new aov here so for the second one we are going to use
[125:49] i think we only need the sky and indirect volume so let's select our direct volume sun
[125:55] and i'll add another dot here let's set this merge operation i'll set this to plus and we are going
[126:01] to create one more duplicate with all of these nodes and let's hook this up over here and this final
[126:08] one we want to use the indirect volume so when we merge all of these together and also let's
[126:13] reverse the order here so it's a the layer that we add is going to be layer a so i can select the
[126:21] merge node and press shift text on both of these and if i compare the results we have what we are
[126:26] looking for we are missing the light information from our sky but i didn't end up using that one
[126:33] in the original comp so from here really it's just a matter of preference more or less i will go to
[126:40] the distant light pass over here i'll drop a gray node with g and i just want to crank up the
[126:47] contrast a little bit so i'll decrease the gamma and increase the gain and i'll add another gray
[126:53] node and for this gray node we can go to the color wheel here and let's reduce the red or rather the
[127:00] blue and increase the red so we make it a little bit brownish to match the overall look that we are
[127:06] going for let's look at our sun and maybe for this one i can drop down a gray node and i can just
[127:12] increase the gain and for the indirect volume let's drop another gray node and maybe for this
[127:17] we can increase the gamma a little bit maybe the gain as well make this pop a little bit more
[127:22] so now if i go to the result and compare it with what we had we skewed the color a little bit and
[127:29] we made the highlights pop some more and we can while selecting the end result here i can increase
[127:37] the gain maybe and see exactly what we are doing maybe i can add some contrast here as well and i
[127:43] think this indirect volume was maybe a little bit too high we can also add another gray here and in
[127:50] these shadows we can introduce maybe a little bit more red just so we have more variation in the
[127:57] color okay so this is a subtle difference here but i think this is already starting to look pretty good
[128:05] from our last merge result we can add another gray and maybe we can reduce the gamma overall
[128:13] and maybe increase the gain just so we have a slight touch of contrast here what i did in the
[128:19] original comp also was i created a noise layer so i'm just gonna drop down a noise and let's take a
[128:27] look at the settings here i want to stretch this horizontally so let's go to our scale and i'll just
[128:33] increase the scale on the width and i also want to animate the translation here on the x direction
[128:40] so i will right click this value and let's add expression which will be based on our frame number
[128:46] so this is exactly how it would work in Houdini when you are mapping certain stuff to time or frame
[128:52] and in this case we're going to use let's do frame and let's multiply this by 50 and see what speed
[128:59] this will provide for us all right so maybe this is too slow we kind of want to match the speed of
[129:06] wind here so let's go back and let's double this or maybe even triple this let's use 150 as the
[129:13] expression all right so now this is more accurate to what we had and we also want to introduce a
[129:19] little bit of animation on this this z value here which will evolve our noise let's add another
[129:27] expression here based on our frame for this one this is a very sensitive value so i will do frame
[129:33] and i will divide this let's maybe divide this by 20 and let's take a look all right so this is
[129:40] pretty close to our smoke simulation i would say now i can drop down a grade node from our
[129:48] main chain and let's use the mask let's point the mask to our noise and now if i drop down again
[129:55] we have these darker patches on our smoke now let's maybe also go back to our noise
[130:02] and adjust the noise settings here i might want to make this not as detailed so i will decrease the
[130:10] lecunarity and we can also play i will increase the size a little bit so we can see this noise
[130:15] pattern on top of our smoke layer and when we play these two together this will just add it this is
[130:23] very subtle but it will add a little bit of detail and variation in our smoke simulation
[130:29] and maybe i'll go back to this first grade node here and let's bump up the brightness
[130:34] slightly more all right and we can preview this with and without this grading adjustment for
[130:40] from our smoke and one final thing that i like to do with a lot of these volume layers is we can
[130:47] drop down a blur from here so i'll press B and i will increase the size of this blur quite a lot
[130:54] let's maybe use 200 and i will merge this on top of what we had so i'll press M drop down a new merge
[131:00] and we can see when we add a blur on top it kind of diffuses everything and fills up the screen
[131:07] a little bit more but we still retain some of the sharp details of our original smoke simulation
[131:13] now of course by default this is too much so for this merge node i can just drop down this mix value
[131:19] which is just which is just going to reduce the opacity of this blur layer we just want to introduce
[131:26] a little bit of this blurring diffusion thing going on and really i just think this looks a
[131:32] little bit better one other thing that we can do with this layer because we are not concerned with
[131:38] interactions with our characters maybe we can even use some of the built-in motion blur that
[131:44] Nuke provides us so after our last merge here with our shuffles we can drop down a motion blur
[131:51] and let's take a look at the settings here let's maybe decrease the shutter time to 0.4
[131:58] and i'll increase the samples and this just smears everything in the direction that the wind is
[132:03] blowing and you might not want this but i found that this helps slightly for this layer and let's
[132:11] preview the final result and preview some other frames and i think this looks fine so we can
[132:16] compare it with what we had and what we end up with so we can already see quite a big difference
[132:21] and now we can layer the character on top so let's grab our character layer from over here
[132:28] so this is just the read node i will just paste this over here so we can start fresh this is
[132:33] our character and let's just copy one of these shuffle nodes with our expression i'll just control
[132:39] C and paste this over here so for our character we will need to handle the shuffle nodes a little
[132:47] bit differently because we have alpha information and we have to deal with the edges of our character
[132:54] so if i press A we can see the alpha the way that we handle color correction with shuffles in this
[133:00] case is going to be by unpromoting all of our AOVs and then premolting the final result and this
[133:07] is because we have aliasing on our edges so you see if i zoom in real close here on the edge of our
[133:13] character we have this gradient of a few pixels that slowly go from white to black and this area
[133:21] over here which has a lot of these gray values will cause issues for us when we are going to color
[133:27] correct so let's go back to our shuffle let's bring back some of the AOVs that we need let's
[133:33] start with combine the diffuse distant and to get rid of this aliasing here we will also want to
[133:40] bring in on this second layer let's use our alpha from the original render and let's plug this in our
[133:47] output as well so now if i press A our AOV also has this alpha information and if i drop an
[133:54] unpromote node after the shuffle this will now get rid of our aliased edges so we can see as i
[134:01] disable this this is what we get and now after this we can drop down a gray node and do our color
[134:07] correction like so and at the end when we put all of the AOVs together we will bring in our aliased
[134:14] edges back so we'll see this in a second let's maybe go ahead and drop down a merge from here
[134:20] and let's grab both of these layers so the shuffle and unpromote press ALT C and let's hook these
[134:27] over here and let's connect these up and reverse the order here with shift x all right and slowly
[134:33] build our network for this second shuffle let's use the combined diffuse sky and let's grab all of
[134:41] these press ALT C let's hook these up for this third one let's grab our final combined diffuse
[134:48] which is our sun and i'll get rid of this gray node for now and i'll grab all of these three
[134:54] nodes and i'll press ALT C to duplicate all of them and let's connect these again and here
[134:59] we'll need a new merge so let's do a merge from here and link everything up and all of these merge
[135:06] nodes actually i should have set the operation to plus before i copied them so let's just i'm just
[135:12] gonna do this real quick so i'll go over each and every one of these and set them to plus so now for
[135:19] our other three duplicates we'll bring in the let's see our combined glossy reflections so reflection
[135:26] distance let's go reflection sky and reflection for our last one we'll use this sun one okay so when
[135:34] we add everything together we can see we get the final result so if i compare my original render
[135:40] with this result we have virtually the same thing and now like i mentioned let's bring back our alias
[135:46] edges we all all we need to do is copy the alpha from our original render to this new result so from
[135:54] over our last node here let's drop down a copy node with k and i'll point the b layer to our
[136:02] original render i'll add a new dot here so again over here where i'm connecting this copy node this
[136:09] is pointing to the original render here let's go over to our copy node and we want the a layer to be
[136:17] the original render so we'll reverse the order with shift x and if i press a we have this original
[136:23] alpha now and we can use a premult and now this will bring back our edges and also because we have
[136:30] the alpha channel back let's do a merge and let's place this on top of our smoke and now we have the
[136:37] character set up we can go through all of the aovs and let's start adjusting these so we can
[136:42] drop down a grade node and it's the same process for all of these layers and this is really the
[136:47] fun part doing the look dev like so so maybe i want to focus more on my sunlight i can drop down
[136:55] the diffuse light slightly and for all of these grade nodes i probably want to use a little bit
[137:01] more red and i can reduce the blue channel and increase the red let's go to our sky one and see
[137:08] what happens when we we can also probably reduce this a little bit we don't want so much bounce
[137:13] lighting from our sun or rather our sky and we do want it from our sun so with this grade node on
[137:20] our sun layer we can either increase this maybe drop down the gamma a little bit let's go to our
[137:27] glossy reflection layers this is the distant one i can maybe drop this down slightly for our sky
[137:34] maybe we can also drop this as well and again we want more emphasis on our sun so maybe i can increase
[137:42] the sun value here and we can see this brings up our light that's coming from the side so already
[137:48] we have a better integration now with our smoke if i drop down another merge here just to demonstrate
[137:53] this and let's point this to our character this would be our default look without any modifications
[138:01] and this is with all the grading adjustments so we really have control by splitting up the
[138:07] lights in this way and adjusting directly in comp because we don't have to bake any decisions so
[138:13] we have to re-render it in hudini and stuff like that so this is really the optimal way to work
[138:18] let's get rid of this merge now i also want to add a little bit more dust on this metal here
[138:24] just to sort of blend him even more on this very chaotic desert sandstorm shot but really i just
[138:31] want to show you some of the many cool things that we can do directly in yoke to affect our render
[138:37] so i'm gonna grab a scratched metal textures that i got from megascans and really you can use any
[138:45] texture that you want so let's go ahead and copy this let's preview this this is the texture that
[138:51] i got you can find a lot of these textures online even for free so really any kind of tile textured
[138:58] with scratch surfaces will work just fine for this or you can even create some noise layers directly
[139:05] here in nuke that you can use instead of a texture so to map this on our camera we will need the uv
[139:11] pass that we've also exported in the renders i will duplicate one of the shuffle nodes and let's
[139:17] connect this over here now to our main render and i'll bring this to the side maybe i'll arrange it
[139:25] like this and let's look for let's grab our uv extra and from our texture we will drop down an
[139:34] sd map so this will be our source and we'll point the sd map to our shuffle and for the uv channels
[139:41] let's use rgb and here we have it so if i press play we can see now that the texture sticks on our
[139:47] character we can safely ignore what's happening on the cloth here this is mainly me not setting up
[139:54] the uv properly inside the fudini probably but we are not really interested in this part either way
[140:01] we only want this to affect our metal speaking of which let's go ahead and use the cryptopass to
[140:08] separate our materials so i'll create a duplicate of the shuffle here let's also point this back to
[140:14] our render and we will actually we don't need a shuffle for this so let's get rid of this and
[140:20] let's use a cryptomat node and let's point this to our main render and we can see the separate
[140:27] id that we get for each object that has a different material assignment and to select the one that we
[140:34] are interested in i'll just hold down control and i will click on the id that we need and we see if i
[140:40] press a this will create an alphapass for us with that object and from our sd map now we can drop
[140:46] down another merge node and let's use for the merge operation we'll use in so now we have this
[140:52] crash surface only on our metal and we can do a merge and for this merge layer we probably
[141:00] should merge this before our pre-mult here we really want this pre-mult to be the last layer
[141:07] that we add to our character just to ensure that we maintain those aliased edges and for the operation
[141:14] here we want to use plus and let's take a look at the final result that we get now obviously we have
[141:20] to adjust this texture a little bit so let's go to our read node for our texture i'll drop down a
[141:28] grade node and let's reverse the values here so i will decrease the white point and increase the
[141:34] black point until this goes kind of the other way around and we want to make the scratches this white
[141:41] color and we can play around with the gamma a little bit as well and let's preview the result now
[141:48] so we are getting slightly closer after our in node where we mask it with the cryptomad let's add a
[141:56] grade node and we can further refine this here so i'll drop down the gain and i'll add another
[142:01] grade node and let's skew the color here towards our red tone so i'll decrease the blue channel and
[142:09] increase the red so we match it with our desert colors maybe we can decrease the gain even more
[142:17] and let's maybe go back to our grade for the texture and let's do some adjusting like this
[142:23] okay now obviously you should spend a little bit more time to really integrate this better
[142:29] but for now i will leave this as it is and one other thing that i want to show you and this
[142:34] isn't maybe completely necessary for this shot but we can see that with this texture mapping we
[142:41] really shouldn't get this much color right on the edges of our surfaces and over here as well where
[142:49] the metal meets this piece of cloth if i look this weird edge that we are getting here is from our
[142:57] uv because we have motion blur baked in this uv pass and this is noticeable here where we see
[143:03] this gradient for the pixels this might make it hard where we have a lot of intersecting objects
[143:10] here for our mapping to properly integrate and what we can do here for this layer is we can use a
[143:19] Fresnel shader to darken the texture that's around the edges of the object so to create this Fresnel
[143:25] shader this is where we have to use our other passes so i'll just drop another dot here let's
[143:32] add another shuffle and actually we don't need the alpha for this one so i'll get rid of this
[143:37] connection and for the other shuffle that we need the other aovs let's bring in our ray origin
[143:45] and let's create a duplicate and let's point this here as well and we'll bring our normal so when we
[143:52] do a dot product between these two layers this works exactly like how we would in Houdini we are
[143:58] going to get a gradient based on which normals align with the direction of our camera so if i drop a
[144:07] dot product from here and this will be a vector tree signature we'll place this here and we might not
[144:14] see this right away in the result and this is because our values are super high here let's maybe do a
[144:21] clamp for both of these so add a clamp here and we can already start to see this let's duplicate
[144:26] this one and also clamp the values of our n all right so now maybe we can see this better if i drop
[144:32] down a grade node and decrease the gamma and play around with the white and black point we can see
[144:38] this Fresnel result that we get and in a lot of other render engines including karma this is called
[144:47] a camera facing ratio but really i'm just used to calling it Fresnel from redshift but this is all
[144:54] this is really it's just highlighting the areas that are facing the camera more which is exactly
[145:00] what we need we can see that as i adjust these values we can isolate these parts of the objects
[145:05] here that are ignoring the edges so we'll use this as a mask and let's go back to before we did our
[145:14] grading so after our masking here after this merge we can just throw do another grade and let's point
[145:21] this to our dot product result over here maybe i'll bring this closer and let's preview the result of
[145:28] the pre-mold and with this new grade node if i drop the gain now we can start to see our edges
[145:34] here disappearing and let's use as a mask input let's use the rgba red channel and we actually
[145:42] want the reverse of this so let's invert our result and this is what we get i can set the gain
[145:47] here to zero and go back to the grade node of our dot product and i can start to play around with the
[145:54] values directly here so if i check the result now with and without we can hopefully see that this
[146:01] allows us to integrate our texture a little bit better now all of this wasn't super necessary
[146:08] if i disable this layer when we add our other smoke layer and the dust and everything on top
[146:15] this won't be super noticeable but i still wanted to showcase some of these techniques
[146:21] in case you might need them for a project later down the road and overall i might want to bring
[146:27] down the gain here we really want this to be quite a subtle effect so this will be our character and
[146:34] let's go ahead and add our foreground smoke and now that i'm seeing this i might want to go back
[146:40] to my background smoke and for this grade node i'll drop down another grade node and this is a little
[146:45] bit too red so i might just want to add a slightly more yellow so i'll just increase the green channel


### FG & Post Process [146:52]
**Transcript (timestamped):**
[146:52] here for our foreground smoke we want to use the same setup that we have for our background smoke so
[146:59] i'll just go ahead and copy all of these layers i'll press ctrl c and just bring them down here
[147:04] and grab the read node from my original comp with the foreground smoke so this layer let's press
[147:11] ctrl c and i'll paste this here and because this is kind of the same volume layer we should maintain
[147:18] all of our AOVs here with the direct volume distance on and indirect volume and we don't have
[147:26] indirect volume here let's swap this for our sky layer and let's merge all of these together
[147:33] and we have kind of the same result of course we still we copied this with our grade nodes as well
[147:38] but this will be fine for now and we can merge this on top of what we have and let's set this merge
[147:46] operation we can keep this operation as over but what we're gonna do is let's set this to plus
[147:53] and the problem here when we set this layer to plus is that we lose any obscuration that happens
[148:01] for our character so we are no longer getting the thickness of our smoke so the end result here
[148:07] that we get from the combination of our AOVs if i press a we don't have any alpha information
[148:13] but our original render has this alpha information so just as an example if i merge this on top of
[148:21] our chain without processing our AOVs so if i look at this result and let's reverse the order here
[148:27] and i look at the result we get after we separate the AOVs now if we ignore all of the color
[148:34] corrections we can see that this one obscures our character a lot more especially in these areas
[148:40] over here we get the correct result we can see that the character is a lot less bright so to bring
[148:47] some of these obscuration back we can use the alpha channel from our render so this layer here
[148:54] to darken everything before we add the smoke on top here so let's just drop a grade node and point
[149:01] this to our render and let's preview the RGB channels if i drop the gain here to zero and make
[149:09] this completely black if i do a merge and merge this over our character because we have on this
[149:16] grade node because we have this alpha channel this merge will only affect our render where we have
[149:22] all of these white values so where this has strong white values we will have a darker image so as a
[149:29] result we can go here and we can see we can preview this with or without and we can see that everything
[149:34] is way darker so this is really just isolating the obscuration that happens from our smoke so now
[149:40] when we preview this with the smoke on top we have the correct result so we have now what we would have
[149:46] had originally if i just merge this on top directly only now we can add another grade node here which
[149:52] runs only on the alpha channel and if i play around with the black and white point we can
[149:59] further adjust this obscuration so i can if i increase the gamma we can see we have more obscuration
[150:06] we can also play around with the point and the black point and we can sharpen up this alpha
[150:12] contrast so if i preview the alpha channel we can determine exactly how strong we want the
[150:18] obscuration to be so the darkening but it's probably best to preview this from our end result here
[150:24] and again if i disable this we can see the result that we get so we can come back to this in a
[150:29] second let's maybe just take care of some of our gradings for the volume so i might want to increase
[150:37] most of these and okay this looks fine let's maybe crank up the contrast here as well and for our
[150:45] sky we might want to decrease this a little bit and let's also make this more red as well
[150:53] and let's take a look okay so now this is starting to look fine and one other thing that i did was
[150:59] i grabbed another copy of this distance so with a grade node i can just merge this on top of everything
[151:07] and let's say this 2 plus and i can use this for some very strong highlights so i can decrease
[151:13] let's maybe preview the result here so for this grade node i can decrease this and just get
[151:19] isolate a little bit more of the highlights of this smoke so if i preview this we just get a
[151:25] slight more kick in our foreground smoke and finally we'll do the same thing that we did earlier
[151:31] so from our merge shuffles here let's drop down a blur node and we'll blur everything
[151:39] and just merge this on top let's preview the result let's increase this slightly and we'll just merge
[151:45] this here and reduce this mix overall so this again will add even more diffusion for everything
[151:52] and we can see these parts over here it really helps to blend everything together this blurring
[151:57] diffusion thing can is also something of a fake gi look which is why it usually works so well and
[152:06] a very cool thing that happens is also that it brightens up the blacks so they're not completely
[152:13] dark which is a little bit unnatural so i always do this blur layer trick let's move forward with
[152:21] the eyes now and for this we will need to reference the Crypto Matte from our original render so i'll
[152:28] use a poster stamp node which is essentially like the object merge in hudini point this to this
[152:35] render of the character and i'll bring this down below so we can work on our eye layer over here
[152:42] and i'll just hide this connection with alt h and we will use a Crypto Matte node from here
[152:48] let's go ahead and hold down control and select our eyes so now we have this alpha layer and we can
[152:55] turn this into a white rgba layer if i drop down a shuffle i can grab this alpha layer and while
[153:01] holding down alt i'll connect this to all of our nodes so we just have this layer here essentially
[153:07] if i were to merge this directly on top we can see we have this result now this isn't what we want
[153:14] let's get rid of the merge and obviously we'll have to make this green we'll do this in a second
[153:19] what i want to do and this is just a cool trick that i found along the way to add a little bit
[153:24] more gradient so we have a stronger value that's in the center we can do a blur and i'll increase
[153:32] the value here slightly and i'll merge this on top of the shuffle and if i set the operation to
[153:39] multiply we can see we have this really cool gradient happening here and i can adjust the value
[153:45] of the blur node to determine the value of this gradient and also if i do a grade node after the
[153:52] multiply i can increase the black point and make this even more apparent even more obvious
[153:58] let's maybe actually play around with the gamma and white point so we end up with something like
[154:04] this we can see this maybe better on this side i might want to adjust this blur node more the
[154:12] reason that we do this is simply so it's not just a flat color which can kind of look a little bit
[154:18] weird it's always just better to have more variation so now we can make this green and add our glow
[154:26] but one other thing that i want to do before that the problem when we do this operation is if i look
[154:33] at my alpha channel now this also affects our alpha so we will drop down a copy node with k
[154:39] and let's reference back our original alpha from the crypto matte layer so let's do a to b reverse
[154:46] the order and if i press a we have the original alpha now so we can merge this properly on top
[154:52] so now when we add a grade node i can go to the gain here and decrease these channels and increase
[154:58] the green and maybe also i want to leave some of this some of this red value so we have a bit of
[155:04] yellow maybe so some variation in these greens let's do something like this and i can merge this
[155:11] now on top and see the result let's set the operation to plus and let's take a look pretty
[155:18] okay now what i want to happen is i want to kind of fake a little bit of the obscuration we would
[155:25] get from our smoke so if i preview this result as it is because this eyes layer is on top of
[155:33] everything we won't get any interaction with the smoke that's that physically would be on top of
[155:39] our eyes so we should have some obscuration from our foreground smoke and we can use our foreground
[155:47] smoke layer over here to darken the values of our eyes but i decided to use a noise layer instead
[155:56] so in fact i'm going to grab this noise layer that we created here i'm just gonna go ahead and grab
[156:01] and duplicate this over here and for this layer i'll just decrease the size slightly and let's
[156:08] do this before we do this grading before we turn the eyes greens let's use a merge and let's set
[156:15] the operation here to multiply so if i turn this let's maybe reverse the order if i turn this one
[156:21] enough we can see this result and i can increase the gain of the smoke and maybe the lecunarity as
[156:28] well and we can see the result that we get so this is the noise that's on top okay and maybe this is
[156:34] a little bit too fast now for this effect so i can go to the transform option here and let's
[156:40] reduce the speed and if we go back to our multiply if i preview some frames now we can see how the eyes
[156:48] start to flash a little bit so we have all of this variation in our values that kind of mimic
[156:55] this foreground smoke layer so now if i look at the result we sort of have this fake obscuration
[157:02] going on for our eyes so they're not entirely emissive throughout the whole shot and this becomes
[157:09] a lot more obvious when we add the glow and the flare so let's do that i'll drop down a crop from
[157:15] the grade and then we can use the ap glow node so this is a free exponential glow available on
[157:23] eucopedia and you can find a link for this in the links file from the downloads let's maybe reduce
[157:29] the source wide i'll leave the response as it is and i'll increase the intensity slightly and we'll
[157:35] just merge this with a plus operation on top and let's preview the final result we might want to
[157:42] maybe increase this even further and we can see that with this extra layer of noise we also get a
[157:49] lot more variation in the glow as well which looks a lot cooler and for the flaring effect we can drop
[157:56] down a radial and i will squeeze this a little bit so let's turn back on our overlays and i'll hold
[158:03] down control and grab the handle below here and i'll just squeeze both of these together like so
[158:09] i'll drop down a convolve node let's use this as our filter and point the image to our glow
[158:17] so let's take a look at the result and we can also merge this after our glow and we can see now the
[158:24] result let's set this to plus and preview the final thing here and we also have now this very subtle
[158:31] layer of flaring you can obviously still if i drop down a gray node after the convolve we can increase
[158:38] the gain and the gamma to make this even more obvious but i want this fairly subtle i'll do
[158:45] something like this now we need to spend a bit more time adjusting everything especially our
[158:51] noise and maybe the original grade might want to introduce even more green here but i'll leave
[158:56] it up to you to decide and with this we pretty much have all of our render layers all that's
[159:02] left to do is some post processing but before we go to that i just want to show you a cool trick
[159:08] that i did in the original render we can over here where we determine the obscuration for our
[159:16] foreground smoke this alpha channel so again it's this layer that darkens everything what i did here
[159:22] was i added another gray node and again i will set this on the alpha and i want to use this to
[159:29] darken everything a lot more so maybe i can decrease the black point and i'll increase the gamma
[159:36] like so until we obscure it until we obscure our character quite a lot so let's maybe do something
[159:43] like this and i animated the mix value in the beginning of our animation so we went from a mix
[159:50] value of one i animated this to zero and we can see that as i decrease this mix value bring back
[159:57] our character so in the beginning it's a lot more emphasis on the silhouette of the character and the
[160:02] eyes and then we can bring some of the focus back on everything else so this is what i did i just
[160:08] right click to set a keyframe for a value of one on the mix and i went forward maybe 50 frames so with
[160:15] frame 1050 we can add another keyframe for a value of zero here so now our character is slowly
[160:23] fading in through the smoke throughout the first 50 frames of our shot and now that i'm saying this
[160:30] we can probably adjust our flare a little bit or maybe we can adjust the glow instead
[160:37] let's set this to a slower or i will set this to a lower intensity so for our post-process effects
[160:45] i'll start with an overall grade node and i'll just increase the gamma increase the contrast a
[160:52] little bit and let's punch up the gain slightly and what i want to do is add some defocus to this
[160:59] so let's drop down a defocus node and i want to randomize this defocus value i want this to sort
[161:05] of flicker a little bit just to kind of match this shaky camera movement so it feels kind of like
[161:12] it's coming in and out of focus and we can do this with an expression let's right click and add
[161:17] expression and we can start with a random so let's use random value here that's based on our frame
[161:26] and if i leave this as it is and we can check our curve editor we can see that by default this is
[161:33] a really chaotic value so to spread out this pattern here let's go back to our expression i can also
[161:40] press equal sign on my keyboard we can lower this seed value for our frame so if i divide this by
[161:47] five we essentially spread out this randomness so maybe i want to reduce the frequency even more
[161:54] let's divide this by value of seven okay so i think this might be fine now i want to also
[162:01] affect the amplitude overall because we can hardly notice a value of one pixel so let's go back to
[162:08] our expression and let's multiply this with 10 all right so now we can actually see this in our
[162:15] result here and this will be fine for now and what i want to happen is that i want this defocus value
[162:21] to be zero most of the time and just have these occasional bumps that's driving this whole thing
[162:28] so we can see that as this expression is currently we never really have a value of zero we are always
[162:35] kind of in between one and ten so what we can do here is going back to the expression i can put all
[162:42] of this inside a parenthesis and if i subtract a value of five we are also pushing these in the
[162:50] negative values now i don't really want negative values i want all of the negative values on this
[162:55] side to be clamped to zero so let's go back and let's also clamp this entire value we will do a
[163:02] clamp here for this entire value and let's add a comma at the end here and clamp from zero to ten
[163:09] and close parenthesis hit okay and now we can see all the values are clamped so we'll have these
[163:14] occasional spikes that go up to a value of five and all we have to do if we want to increase this
[163:20] amplitude is go back here and let's maybe say that we want to work from zero to ten we can multiply
[163:26] this value here with 20 and we can subtract a value of 10 so let's maybe just render a few
[163:33] frames here and see how this looks all right so now we have this occasional defocusing to go along
[163:39] with our shaky camera and we can also see how our eyes start to flicker a little bit which helps to
[163:46] sell more this idea that the smoke is in front of our character another thing that we can add on top
[163:53] of everything here as a post processing effect is a bit of a lens dirt texture so i grabbed one
[164:01] i have one over here which i used in the original example which looks like this and again you can
[164:07] find a lot of these textures if you just type on google i think lens dirt you will really find a
[164:13] lot of these kinds of textures now we can simply merge this on top and if i set operation to plus
[164:21] this is what we get we can maybe drop down a grade node and of course we'll have to decrease the
[164:26] scale i might decrease the gain as well and let's add another grade node and also make this
[164:34] thin this towards the colors that we need we can do something like this now i only want this to
[164:40] affect the fringes of our comp so i'll just drop down with o i can place down a roto and i'll just
[164:48] make a selection here let's add a blur to this and feather this out and we can drop down another
[164:54] grade node and point this mask to our roto and just decrease the gain so we don't have this much
[165:01] in front of our character and more towards the edges and i just realized we forgot about our
[165:07] dust layer so this should be before all of our post processing so after our eyes we can go ahead
[165:14] and add our dust as well and it's going to be this layer here let's not forget this this will be a
[165:20] very simple add operation as well in fact it's kind of the same thing that we are doing here with our
[165:26] lens there to be honest so i can grab all of these layers Ctrl C and paste them here and let's point
[165:32] to our dust and we will merge this on top with a plus operation and let's take a look here before
[165:40] post processing we will need to adjust our grading so let's increase this and for this grade we still
[165:48] want to use this roto shape here because we don't want to obscure our character too much we want to
[165:54] keep this area especially around the eyes more in focus so for this grade node i might want to
[166:03] increase this and let's make this even more red to something like this but this is pretty much
[166:10] it for the dust layer a very simple add operation like i mentioned maybe add more yellow here we
[166:16] can use another copy of this dust let's drop down a grade node point to our dust render and use this
[166:24] as a sort of layer for highlights so i'll increase the black point here and decrease the white so we
[166:30] just have these tiny specks of lights and i'll merge this with our result and set this to plus
[166:38] just so we have a small bump in our highlights preview the final look so this is what this
[166:44] extra layer will do for us and again it's always just better to have some variation and going back
[166:51] to the end of our comp here a couple more things that we can add here is going to be a vignette
[166:57] effect i have a custom vignette node from new cap idea as well which you can find again in the links
[167:04] file let's use ap vignette so this is just to darken the edges which is a very obvious thing to do if
[167:12] you ask me especially for this kind of character focus shot and we can play around with the settings
[167:18] here a little bit decrease the falloff and play around with the aspect ratio and size and we'll
[167:24] do something like this and one other extra thing we can add some chromatic aberration and my favorite
[167:31] note for this is again from new cap idea which is going to be let's use chromatic spin and this is a
[167:39] very subtle effect but i think it works really nice in this case so i decided to use this this is
[167:46] completely up to you if you want to use chromatic aberration or not i might just want to decrease
[167:52] the size and protect the center a little bit more so it's mostly again for our edges here and this is
[168:00] pretty much it the only thing left to do here is use a crop node so we can get the anamorphic
[168:07] format which is this one at the end 2.35 and 1 and i can hide these controls with q so we can
[168:13] preview the final result and this is pretty much it for the comp and with this we have reached the
[168:19] end of this course so i hope you found this course useful and that you learn some new things and
[168:24] hopefully we'll see each other again in a new course let's take a look and see how we can take the


### Blizzard comp [168:27]
**Transcript (timestamped):**
[168:29] exact same renders that we have already and turn this from a sandstorm a desert sandstorm into a
[168:35] winter blizzard like this so this is the difference between the comps and if i pull back here we can
[168:43] see that we are really using this is over here to the left is going to be the desert sandstorm
[168:48] variation meaning our original comp and over here to the right we have this winter version and we can
[168:56] see that these follow almost exactly the same structure really all this is at the end of the
[169:01] day is just adjusting our grade nodes from a dark orange to a light blue and in between in some of
[169:09] these places we have a bit of changes in our structure but for the most part we can see that
[169:14] these are almost exactly the same as far as the building blocks are concerned so we are going
[169:20] to start with our original comp over here and we can see that if i go to the result of this
[169:27] VG smoke we have everything in this dark orange color so we might as well just start from the top
[169:34] and i will preview the result of our combined shuffles over here which is this and i'm just
[169:41] going to go ahead and get rid of all of our grade nodes and start with each of these by dropping
[169:47] down a saturation node and setting the saturation here to zero so i want all of these passes let's
[169:53] maybe just drop down a grade node here and let's preview this and i will just increase the gain
[169:58] and the gamma and this is really what we are going to what we are going to do for a lot of
[170:03] these shuffle nodes so for this other one we'll drop another saturation set to zero drop a grade
[170:09] node increase the gamma all right and for the third one as well saturation zero let's preview this
[170:17] and let's increase the gain here so this is our filled one this third shuffle layer here all right
[170:24] so if we preview the result now we can already see that it's starting to look like a snow blizzard
[170:31] we want to introduce a bit of blue on all of these passes simply because if i want this shot to be in
[170:38] the middle of the day with a clear sky the snow will most likely reflect some of that sky color
[170:44] and that's where we get a lot of our blue colors so after all of these grade nodes let's start with
[170:51] the first one and for our shuffle layers let's actually go to our node settings here and in
[170:56] between brackets i will type in the expression value in one so we see what we are shuffling here
[171:04] now we have the information here in our shuffle node i'm just gonna go ahead and copy this for our
[171:09] second shuffle node and our third one as well just because it's a little bit easier to work this way
[171:16] so for our distant light let's go to our grade and let's go to the gain here and reduce the green
[171:26] and the red and just increase the blue maybe this is a little bit too much i'll bring in some of the
[171:31] red back let's preview let's preview all of these for now and let's grab this third one and i'll
[171:39] press D so we can disable this and now we can focus on our sun let's also for our sun it doesn't
[171:46] make sense to tint this in a blue spectrum but we are going to do this anyway because it doesn't
[171:52] really make sense to have this yellow color and maybe for our sun we might also want to introduce
[171:59] more contrast so i'll just decrease the gamma and increase the gain and also use my multiply here
[172:06] to push these values we can see over here we get these very nice highlights when we increase the
[172:12] gain and let's bring our indirect volumes so this will act like a fill light and i'll drop down a grade
[172:19] again we will do our blue coloring here something like this and i might want to make this a little
[172:26] less obvious okay so if i disable this um maybe this is too much let's do something like this
[172:34] preview some more frames and i'm pretty happy with this obviously you are free to experiment with
[172:39] the values and the grade notes but this is overall the process that we are going to use for most of
[172:45] the layers we have our second grade note here which introduces more noise and variation i'm gonna go
[172:53] ahead and get rid of this so just delete this we don't really want to have these dark spots all around
[173:00] because we want this to be a brighter scene overall we have a secondary layer here which
[173:07] pushes our highlights if i look at the grade note which points to our distant light we can see that
[173:12] we might want to increase the gain here to something like this and this will be our highlights so
[173:19] i'm going to keep this i think it's pretty cool another grade note uh after everything just to
[173:25] push the gain uh rather the gamma a little bit i might as well keep this and then we have this blur
[173:31] trick that we keep doing which softens up everything so i definitely want to keep this looking at this
[173:38] i might want to introduce even more blue color but for now this will be fine we can move forward
[173:44] and let's take a look at our character so if i just paste the character as it is we can see that this
[173:50] doesn't blend at all with what we have so we are going to have to adjust a lot of things here
[173:55] this layer that we created that's adding a lot of these extra detail on our metallic arms so the
[174:04] dust scratches we are going to recreate a different layer that's going to act as a coating of snow on
[174:13] our entire character so in fact i'm going to just grab all of these notes here that represent
[174:20] this extra layer that we created so i'm just going to grab all of these and get rid of it
[174:26] and for now we are only going to focus on our character let's go ahead and let's start by
[174:32] removing all of our grade notes so really we are going to start the grading from scratch
[174:38] okay and we are going to go one by one so we are going to look at the diffuse distant and
[174:44] let's drop down a grade i definitely want to increase this color here so i'm going to i'm going
[174:49] to grab the gain and the gamma and just push these out by a lot and add another grade note and we
[174:55] might as well introduce our blue colors right right now so i'm just going to reduce the red
[175:02] and increase the blue so we end up with something like this we don't want to go too much into the
[175:07] blue tint we want to keep it fairly realistic i would say let's look at our diffuse sky so
[175:15] let's drop another grade and let's push this out we also want a lot of this sky color as well we
[175:20] can see that this is already tinted blue and this is because directly in our render we have absorbed
[175:28] this blue color from the sky but i will probably this is so for this gray note for the luminosity
[175:35] or rather the values we probably don't want this to be this bright so let's keep it like this
[175:43] and let's not add a second grade note for our blue colors for now let's take a look at the result
[175:50] all right it's pretty good let's look at the result with our diffuse sun so we also want to push
[175:56] these out let's go for another gray node and i'll just increase the gamma so i will start with the
[176:03] gamma because this brightens everything a lot more and for this as well because this is too yellow
[176:10] from our sun i might as well drop a saturation before our grade and set this to zero let's go
[176:17] back here and let's add a second grade node and again let's push out the blue values okay let's
[176:24] preview this so it's already starting to look pretty good let's look at our reflection layers
[176:30] add a grade node let's push these out i think this is already looking pretty good by just adjusting
[176:35] the gamma for our reflection sky let's go ahead and again push out the gamma and we need to get
[176:45] rid of this yellow so another saturation here set to zero and another grade node after our first
[176:52] grade node and we will just push in some of these blue values right so if i look at this it's already
[176:59] starting to look pretty good let's look at the result merged on top of our snow and i already
[177:05] like how this is looking and we really honestly just eyeballed all of these values and because
[177:11] i previously did this scump before recording i kind of know what the values on the grade nodes are
[177:17] supposed to be but the proper way to do this would be to preview the final result so with the snow
[177:23] and then go one by one layer so if i disable all of these merge nodes here with d we can go one by
[177:30] one so we can see what the distant light provides and then i would enable the second shuffle and
[177:37] and do our grading adjustments and and go forward to the next merge node and then do this adjustment
[177:43] so probably on this diffuse sun the grading for the values are a little bit too high i might want
[177:51] to drop this down a bit and maybe four hours sky as well then i can enable the reflections and
[178:00] i might want to increase the reflections to be honest to something like this and let's enable
[178:08] the last one and again i might want to push the gain here a little bit more i think it's already
[178:14] starting to look pretty good it's starting to blend in a lot more with our snow of course after all
[178:20] of these merge nodes where we recreate the beauty we can add a grade node on top of everything and
[178:25] i might want to push in our black values a little bit so we can go to our lift values here and i
[178:33] want to just introduce in our very dark spots a little bit of blue so i will just increase this
[178:40] obviously this is too much let's do 0.01 instead maybe even less let's do 0.05 something like this
[178:49] and let's also introduce a little bit of green as well so 0.0025 half of this
[178:56] all right and this will just bump up our darks a little bit just because if i look at this dark
[179:02] spot it doesn't really blend in with our lighting in the shot and of course we can pile on more
[179:11] gray nodes here so i might want to gain everything up slightly like this and i think this will be
[179:18] fine for now we can come back later because we have to add on top the other layers as well
[179:23] let's take a look at how we can create a coating of snow over this character we are going to start
[179:30] the same way that we did with NastyMap by using the UV channels so let's grab one of these shuffle
[179:36] nodes i'll just paste this over here let's point to our render and let's arrange these nodes slightly
[179:44] let's go ahead and look at our UVs so let's shuffle this UV extra and now this will be in our RGB
[179:51] slot so for our snow texture i got one from Megascans and it's going to be this frost textures from
[180:00] the imperfection categories you can use really whatever textures you want so if you have bridge
[180:06] you can use this texture or you can grab one from any place that you know or you can even use a noise
[180:13] texture directly inside of Nuke so if i drop down a noise we can use this as well so if you adjust
[180:20] some of these settings here you can get a very similar a very similar result but for my case
[180:26] i'm just going to use this texture that i already have which looks like this all right so we are
[180:32] going to map this on our character let's drop down a NastyMap node this will be our source and our
[180:39] NastyMap will point to our shuffle and for the UV channels here because we shuffle the UVs into our
[180:46] RGB channels we are going to use the RGB channels for the UV channels here so this almost works
[180:54] we can see that it's the same result that we had when we added our dust scratches in the previous
[180:59] lesson we do have this problem on the cloth of the character the mapping is not entirely correct here
[181:08] what's happening here if we look at the UV channels and i'm going to make a separate video about this
[181:14] where i go a little bit more in depth so i'm just going to give you the short version of what's
[181:18] happening we can see if i look at the pixel information so i'm just gonna go ahead and
[181:23] hold ctrl shift and sample a region here let's sample this region we can see that the values
[181:30] on the red and green channels which is our U and V coordinates these the red channels go
[181:37] above a value of one so we have 1.3 and the NastyMap node wants to use values between zero and one
[181:46] so we need basically a way to remove this one in front of our value so this 1.32 value becomes
[181:55] 0.32 and to do this we can just drop down an expression node and for our expression we are
[182:02] going to type R which will grab the values of our red channels as it is and then we are going to
[182:08] say floor and in between parentheses we are going to type R again so now if i sample this we can see
[182:15] if i do control shift drag now we have a value of 0.31 and if i disable this we have the original
[182:22] 1.31 value so this one that's in front of the decimals becomes zero and now if i look at the
[182:29] result of our SdMap we can see that we have the proper tiling now we might as well do this for
[182:35] our green channels as well so we can avoid having values over one and we are going to say g minus
[182:43] floor and in parentheses g and again i will go a little bit more in depth into a separate video
[182:49] that i plan to make on the SdMap node so i'm going to explain a little bit more about these
[182:54] expressions in that video so we are going to go back to our result and we have the proper mapping now
[183:01] and we can see that this pattern is quite big here so we can tile our textures if we add a
[183:09] great node after the UV channels so over here and if i reduce the white point we can see that we
[183:17] make this pattern smaller so we are essentially just repeating the pattern over our character so
[183:23] this works exactly how it would work in a 3d software where you just increase the tiling of
[183:29] the texture so let's maybe set the white point to a value of 0.35 and for the most part i'm pretty
[183:37] happy with how this looks now this texture if i do a merge and i grab this and just place it over
[183:43] our character obviously we are not going to get the correct result here we can also preview this
[183:49] with our smoke in the background we really want this texture to only affect the right side of our
[183:56] character to sort of match the direction from where the wind is blowing our snow and in order to
[184:03] isolate this right part of our character we can use our normal channels or rather our normal
[184:10] AOV so from over here before our UV shuffling let's go ahead and copy paste this node and we want to
[184:19] grab our normal AOV okay and for the normals if we grab our red channel so if i press R we can preview
[184:28] our red channel we see that we already have this sort of gradient that's across the side of our
[184:35] character and really what we can do here is simply remap these values now i'm going to shuffle let's
[184:42] press R again so we can go to our regular display i'm just going to place place our red channel
[184:48] in the alpha slot so if i press A we have the same thing here and i will drop down a great node
[184:54] and let's set the channels to only affect our alpha and if i play around with the white and
[185:00] black point we can control how this gradient affects our character so i'm going to kind of reverse
[185:06] the gradient that we get by pushing the black point out and bringing the white point in and we can
[185:13] also now play around with the gamma as well and also the gain so if i do this we can start to see
[185:20] we get exactly the result that we want which is we are isolating the right side of our character
[185:27] so i'm just going to adjust these values a little bit like so and from our ST map let's press A again
[185:35] to go to the RGB display i'm going to drop a gray node and point the mask to our alpha and now if i
[185:42] drop down the gain let's also invert this result and now this texture will match this direction
[185:48] that the wind is blowing and if i go to the final comp we can see this here and i think this is
[185:55] already looking pretty good if i disable this we can see the result now another thing that we have
[186:02] to take into account here is we can see if i disable this this part over here is a lot more
[186:09] dark so we are not really receiving the shadows from our renders and we can just grab the information
[186:17] that we have from our merge results so after our last grade here for our character i'll do another
[186:25] grade node and place it over to the side and connect this here and i'm just going to create a
[186:30] contrasty look here to isolate our shadows i'm going to push the white point in and maybe increase
[186:37] the gamma here just so we have a very contrasty difference between shadows and highlights so let's
[186:45] do something like this and i want to also do a white clamp as well and now we can use this
[186:52] information and we are going to point to the red channel to mask what we have the result of our
[186:58] sd maps so over here after our grade i'll add another grade let's point to our highlights
[187:05] that we created here with this gray node and for the mask we are going to look at our red because
[187:13] this thing that we created doesn't have this highlight information on our alpha channel so
[187:18] we are going to use the red channel instead and now we can just simply decrease the gain and let's
[187:25] also invert the result okay so we can see now that as i drop down the gain we start to get a little
[187:30] bit more of our shadows back from the original render so if i look at the final result now
[187:37] if i disable this gray node we see that we have a much more blended result and if i turn the whole
[187:45] sd map thing on and off we end up with this so we still have some texture detail in our shadowy
[187:53] spots but it's not as obvious and again this is with the shadows and this is without and we can
[188:00] still do from here another gray node and we can adjust the gain here directly or maybe we want
[188:06] more contrast and there's a lot of options that we have right now we can go around and let's play
[188:14] with this with this highlight pass that we created so if i look at the final result and adjust this
[188:19] gray node we can maybe increase or rather decrease the power of our shadow slightly but for the most
[188:26] part i am pretty happy with this result and we can see over here especially if i disable this
[188:33] layer we can see how much this extra texture helps us to blend in our character with the environment
[188:41] all right so we can move forward and let's take a look at our foreground smoke our first merge
[188:47] here will be for the overall darkening so this is what controls the thickness of the fog that's on
[188:55] top we probably want less of this so we can go to our grade here for the alpha let's preview the
[189:02] result with a and i'm just gonna go ahead and i want to make this a little bit thinner so let's
[189:09] get rid of some of this brightness like so and let's just preview the result at the end here and i'll
[189:17] press a of course we will need to do the grading for all of these layers so let's go ahead and get
[189:24] rid of all of the grade nodes and we want to do the same thing really that we did for our background
[189:29] smoke so let's add a saturation set to zero for all of these and i'm just gonna go ahead and copy paste
[189:37] this saturation with a value of zero and let's go to our first one add a grade node let's increase
[189:45] the gain this will be our distant light we'll do something like this with a second grade node
[189:51] we are going to bring in the blues let's go forward and this will be our sky so of course we will
[189:58] need to increase this as well maybe not too much let's leave this as it is and go to our let's take
[190:05] a look at the shuffles here we might need the expression to see what we are shuffling this is
[190:11] the sun so for this let's do a grade node and then just i'm just gonna push out the gain here a lot
[190:19] so we get more highlights let's take a look let's also add another gray node for our sun and we are
[190:26] going to grab some blue values here and we have another gray node at the end we might as well
[190:32] brighten this as well and a second gray node so this second gray node we can see that removes some
[190:38] of this blue so we might as well get rid of this and let's take a look at the final result that we
[190:44] have so far all right and let's preview some other frames probably this we removed too much of the
[190:52] thickness of the smoke let's go back to our grade and let's preview the alpha here yeah this is too
[191:00] dark now so let's bring this back slightly so we do want the snow to obscure our character
[191:08] do something like this and let's preview the result now all right all right so here we can see it on
[191:13] this frame as well but maybe this is still too much let's go to our grade just decrease the gamma
[191:22] and let's take a look at our AOVs here let's maybe just separate these one by one and see exactly
[191:28] what each of these provide i'll bring in the second one and probably this needs a little bit more
[191:35] contrast okay and our third one we can maybe bring in our sun for this third one a lot more
[191:44] so i think this looks a lot better now we really want this to be rather bright okay so this will be
[191:49] fine and we can move forward for our eyes this will be super simple let's just look at the final
[191:56] result and let's take let's find our grade node which introduces the green so it's going to be this
[192:02] one over here after the multiply and i'm just gonna reduce the red and just increase the blue
[192:09] let's do something like this bring in a lot of blue and i can also use this multiply value to push the
[192:15] overall values a lot more so we get our glow back and let's take a look at the glow let's maybe
[192:23] increase the intensity here let's take a look at the flare result so for this gray node we can see
[192:30] that the convolve result looks pretty good but this gray node is pushing out the blue so we can
[192:37] just bring this back and also increase the multiply here so if i look at the result this is pretty
[192:44] much what we can do for the eyes so i think this looks all right let's move forward with our dust
[192:51] let's take a look at how it looks right now and in our previous comp we created this dark layer of
[192:59] dust so this works for a sandstorm but for our blizzard we can remove this entirely and just
[193:06] focus on our particles as they are we are only going to use the plus operation if i look at the grade
[193:14] node so the result as it is we are going to need to bring in the color here for our snow
[193:21] and let's take a look so already this is looking a lot better we might need to adjust this gain
[193:29] probably and because we brighten the snow particles quite a lot we can soften this result a little bit
[193:38] if we add a motion blur before our grading so i'm just gonna place a motion blur here and the
[193:44] default values are rather high so i'm just gonna set the shutter time here to maybe 0.3 and i'm
[193:51] also going to increase the samples to a value of 7 so if i look at the result with the grade if i
[193:57] turn this on and off we can see that this will help to smooth out everything a lot better let's
[194:04] take a look at the final comp and maybe the motion blur is still too aggressive let's use a 0.2
[194:12] shutter time so something like this and for our grade node let's also drop a second grade node and
[194:18] push in a little bit of blue values for this layer as well and i'm pretty fine with this for the most
[194:25] part i do want to darken this layer around our character so we can press o in our comp and just
[194:34] simply do a quick mask around the character let's take a look at the result press a i'll drop
[194:41] a blur node with b and i'm just going to feather this out and just increase the size by quite a lot
[194:48] so maybe something like 400 and then for our snow let's drop another grade node use this as our mask
[194:57] and let's just drop down the gain here and let's preview the result and press a to go back to the
[195:03] rgb view so let's decrease this and we can see with this grade node we isolate this part that's
[195:11] right in front of our character so i don't really want to obscure our character too much
[195:16] let's maybe go back here and let's just set this to a value of 0.5 so our snow will be 50%
[195:23] more transparent right in front of our character and one final thing that i want to do with this
[195:28] snow particles is add a little bit of highlights so i'm just going to drop down a grade and point
[195:34] to our render and with this grade node i'm going to reduce the gamma and increase the gain so we
[195:41] just get we kind of isolate some of these particles maybe i want to push in a little bit more gain
[195:48] so i'm just going to use the multiply values here and let's also do a saturation to get rid of this
[195:55] brown color so i'll set this to zero and i'm just going to merge this on top and this is without
[196:01] the motion blur so set this to plus and as a result if i take a look here if i disable this
[196:07] we can see now that some of these snow particles will have a little bit of highlight to them
[196:14] so this will help us to achieve a little bit more variation and we might want to increase the gamma
[196:22] here slightly okay this is too much but something like this will be fine and this is pretty much
[196:29] our comp after this we have another gray node which really in this case brightens up everything
[196:37] way too much so i'm just gonna reduce this slightly and we can choose to keep the defocus
[196:43] or not in this case i chose to get rid of the defocus and we also have this dirt texture that's on
[196:50] top of everything so for this all we have to do is just go to the last gray node here and push all
[196:56] of the values in the blue ranges so we can take a look at the result and finally we have our transform
[197:04] which pushes the render down a little bit we have this chromatic spin effect so you can also
[197:10] choose to keep this or not finally we also have the vignette node now in this case it looks pretty
[197:18] good with the dark version but what i did instead was use coloring here so i just increase this
[197:25] and push this towards white and then i just decrease the amount so we can achieve a sort of
[197:32] focusing around our character by brightening the edges of our comp instead of darkening them
[197:39] and this will be up to you if you want to darken the edges or brighten them or not use any at all
[197:45] and then finally we have a final gray node over everything maybe this is also pushing the values
[197:52] too much so i might disable this and a crop to get our anamorphic display so 2.35 and 1 and this
[198:01] is basically it we can preview some other frames and see how everything is looking but for the most
[198:06] part i'm pretty happy with this and we can see how quickly we can achieve a vastly different result
[198:12] so this is also a good thing to know how to do all of this because in an rnd setting in a studio
[198:20] workflow you can very easily create iterations and variations on any given shot so hopefully this
[198:27] gave you a little bit more insight into why compositing is very powerful and why it's a very
[198:32] useful skill to have and this was it for this lesson so hopefully we'll see each other again
[198:38] in a new course



---

## Captured Frames

- [0:20] tutorials/frames/houdini-fx-solaris-nuke---full-vfx-course/frame_000.jpg
- [20:00] tutorials/frames/houdini-fx-solaris-nuke---full-vfx-course/frame_001.jpg
- [45:00] tutorials/frames/houdini-fx-solaris-nuke---full-vfx-course/frame_002.jpg
- [70:00] tutorials/frames/houdini-fx-solaris-nuke---full-vfx-course/frame_003.jpg
- [95:00] tutorials/frames/houdini-fx-solaris-nuke---full-vfx-course/frame_004.jpg
- [125:00] tutorials/frames/houdini-fx-solaris-nuke---full-vfx-course/frame_005.jpg
- [131:00] tutorials/frames/houdini-fx-solaris-nuke---full-vfx-course/frame_006.jpg
- [145:00] tutorials/frames/houdini-fx-solaris-nuke---full-vfx-course/frame_007.jpg
- [154:00] tutorials/frames/houdini-fx-solaris-nuke---full-vfx-course/frame_008.jpg
- [163:00] tutorials/frames/houdini-fx-solaris-nuke---full-vfx-course/frame_009.jpg
- [168:30] tutorials/frames/houdini-fx-solaris-nuke---full-vfx-course/frame_010.jpg
- [195:00] tutorials/frames/houdini-fx-solaris-nuke---full-vfx-course/frame_011.jpg

---

## Structured Notes

## Cross-platform canonical-location note

This is a full VFX course by Voxyde VFX: a walking-character-in-a-sandstorm shot built end-to-end (198m39s, 9 chapters). By runtime, Houdini/Solaris content (chapters 1-6, ~124 min / ~62%) is the majority; Nuke content (chapters 7-9, ~74 min / ~38%) is the minority by time but is a **substantial, self-contained final act** — not a token wrap-up. Per this ecosystem's cross-platform convention (canonical extraction lives with the skill matching the majority content, with an index-only cross-reference stub elsewhere), the default expectation would be **houdini-wand canonical**. This agent deviated from that default and made **nuke-em-all canonical** instead, for these reasons:
1. The Nuke portion (3 full chapters) teaches a complete, reusable methodology — AOV-driven "rebuild the beauty from split light passes" compositing, a from-scratch Fresnel/camera-facing-ratio shader built from raw AOV data (ray-origin · normal dot product), UV-pass-driven texture projection with wraparound-UV fixing, Cryptomatte-driven material isolation, and — uniquely instructive — a full non-destructive "reskin" of the exact same AOV structure from a desert sandstorm into a snow blizzard purely through re-grading, demonstrating why AOV-split comping is valuable in a production/iteration context. This is arguably the single most complete AOV-rebuild masterclass in this skill's whole library.
2. This agent was first to touch the video (no existing entry in houdini-wand's INDEX.md as of 2026-08-14) and had already collected the raw transcript here before this evaluation, so building the canonical file in the skill that will get the most reuse out of it (nuke-em-all) avoids a second multi-hour download+transcribe cycle for no benefit.
3. A cross-reference stub has been added to `houdini-wand/tutorials/INDEX.md` pointing back here, per the established convention, so the Houdini/Solaris side (cloth vellum sim, ripple-solver "cheat" wind effect, pyro smoke/dust, USD/Solaris layering, look-dev, AOV render-layer setup) remains discoverable from that skill even though the full write-up lives here. If Houdini-side technical depth is needed later, extract it fully into houdini-wand instead of expanding this file.

### Core Technique
End-to-end VFX pipeline for a cinematic character shot: Houdini SOPs for effects sourcing (vellum cloth, ripple-solver "wind" cheat, pyro smoke, particle dust), Solaris/USD for scene assembly, look-dev, and AOV-split rendering, and — the section extracted in full depth here — Nuke for reconstructing the beauty image from split-light AOVs, building a Fresnel shader from raw position/normal data, projecting UV-mapped detail textures, and non-destructively re-grading the entire comp into a completely different environment (desert sandstorm → snow blizzard) without touching the 3D render.

### Summary

**Houdini/Solaris side (chapters 1-6, summarized — full technical depth belongs in houdini-wand if extracted there):**
- **Setup:** USD-based character/camera/animation pipeline (separate USD layers for base look-dev, animation, camera — swap animation without losing material assignments). Nuke/Houdini color-management parity achieved by exporting Houdini's own OCIO config and pointing Nuke's project settings at the same file (instead of default ACES), with EXRs exported in ACES CG — critical so what's previewed in Karma matches what's loaded in Nuke.
- **Cloth simulation:** Vellum cloth sim on a cape/hood. Key trick: **cancel the character's forward translation before simulating** (extract the character's centroid position via `Extract Centroid`, subtract it from both collision geometry and cloth via Attribute VOPs, simulate on the now-static mesh, then re-apply the translation afterward) — this stops the character's forward motion from fighting the wind direction and fully "eating" the wind's visual effect, at the cost of physical accuracy (acceptable for art-directed VFX work). Additional production tips: low bend-constraint value for more wrinkles, higher bend-damping-ratio for stability, `Vellum Attach to Geometry` with rest-scale 0 to hard-pin specific points (hood/shoulder/waist) to the body, soft-transform nudges on individual points post-sim to fix small intersections (works reliably because cloth-sim topology is consistent frame to frame), and `Rest Position` capture pre-cache for later shading use.
- **Shirt ripples:** A cheap alternative to full cloth sim — the **Ripple Solver** run on a *static, world-centered* copy of the shirt mesh (same translation-cancel trick as the cloth), driven by a POP-network-spawned particle stream (not a per-frame scatter) used as ad-hoc "collision" geometry that triggers ripples only from the wind-facing side (isolated via a `Clip` node). Result: convincing "wind pushing fabric" motion with zero real collision detection — explicitly framed as a fast, non-physical "cheat" appropriate for slower/calmer shots, contrasted against the full Vellum-based shirt sim used in the author's other (paid) course for faster/more dynamic action.
- **Smoke & dust:** Pyro smoke sourced from a `VDB from Polygons` fog volume with an animated, remapped `Volume Noise Fog` density source (patchy, not uniform). Inside the Pyro Solver: layered `Gas Turbulence` (large-scale "big" + small-scale "small" noise merged together) plus a `Gas Disturb` with **Rotational Force** enabled (concentrates the disturbance on faster-moving parts of the smoke only, avoiding over-diffusing calm regions) for a chaotic "sandstorm" look. Dust is a POP-network particle sim advected by the smoke's own velocity field (`POP Advect by Volumes`, Final Velocity update), with per-particle velocity-scale randomization to break up uniform "stepping," dead/stuck-particle removal via a speed-threshold VOP, then instanced with small noise-displaced spheres (`Copy to Points`, packed instancing) with randomized scale and orientation for rock-like dust motes rendered with velocity-blur.
- **Solaris/USD assembly:** Sub-layering shirt/cloth meshes onto the existing character USD by matching scene-graph paths exactly (preserves material assignments without re-authoring them) — a core USD-workflow lesson. Cloth material built from scratch in a Karma Material Builder using MaterialX fractal-noise nodes mapped via a `rest` primvar (not raw world position, so the noise sticks to the moving cloth) plus Megascans fabric roughness/normal maps. Lighting: a Physical Sky (softened via increased angular size) plus a supplementary Distant light, each tagged with per-light LPE names for later AOV splitting. **Render-layer strategy:** four separate USD render layers (BG smoke, FG smoke, dust, character) each built via `Prune` node scene selection, with `invisible to primary rays` used on the FG smoke when compositing it onto the *character* render layer (so the smoke casts correct shadows/occlusion onto the character without actually rendering as visible geometry in that pass) and `shading holdout mode = matte` used to render the character as a pure holdout matte under the smoke layers. AOVs exported: split diffuse/glossy-reflection per light (sun/sky/distant), indirect volume bounces, Cryptomatte (material ID), UV pass, and — critically for the Nuke Fresnel trick below — raw **ray-origin** and **smooth-normal** AOVs.

**Nuke side (chapters 7-9, full depth — this is the canonical content for this skill):**
- **AOV-driven beauty reconstruction:** Rather than using the rendered beauty pass directly, the whole comp is built by `Shuffle`-ing out each split-light AOV (per-light diffuse, per-light glossy reflection, sky/sun/distant indirect volume, etc.), individually grading each one, then `Merge`-ing them back together with `plus` operations to reconstruct — and then deliberately deviate from — the original beauty. This is the load-bearing technique of the whole section: because the final look is built from independently-gradable light components rather than a baked beauty, the entire environment can later be changed (see the blizzard reskin) without a single Houdini re-render.
- **Alias-safe AOV compositing:** Splitting/regrading AOVs independently breaks anti-aliased edges (aliased edge pixels are semi-transparent blends that don't survive independent per-layer grading correctly). Fix: **unpremult** all AOV layers immediately after shuffling (before any grading), do all color work on unpremultiplied data, recombine, then as the very last step **copy the alpha from the original beauty render** and **premult** once at the end — this restores clean anti-aliased edges that would otherwise be destroyed by the intermediate per-AOV math.
- **Fresnel/camera-facing-ratio shader built from raw AOVs:** Because the render exported a raw **ray-origin** AOV and a raw **smooth-normal** AOV, a from-scratch Fresnel effect is built entirely in comp: a `DotProduct` node (vector3 signature) between the two (each `Clamp`ed first, since raw values are far outside 0-1), refined with a `Grade` (gamma/white-black point) — this reproduces exactly the "camera facing ratio" concept from renderers like Redshift, and is used as an edge-darkening mask so a projected scratches/dust texture doesn't wrap unrealistically hot around silhouette edges.
- **UV-pass texture projection:** A tileable detail texture (metal scratches, later reused as a snow-frost texture) is projected onto the character using the exported **UV AOV** fed into an `STMap` node. Gotcha: Solaris/Karma's exported UVs can exceed the 0-1 range (e.g. 1.32), which `STMap` requires to be wrapped — fixed with an `Expression` node computing `R - floor(R)` (and the same for G) to strip the integer part and get proper tiling, a general-purpose UV-wraparound fix worth remembering for any USD/Solaris-to-Nuke UV pipeline. A `Grade` on the shuffled UV channels (reducing white point) controls texture tile density, matching "increase tiling" in a 3D app.
- **Cryptomatte-driven masking:** `Cryptomatte` isolates specific mesh/material IDs (e.g. just the metal armor, or just the eyes) from the beauty render by Ctrl-clicking directly in the viewer, used to constrain the projected scratch texture (or, for the eyes, to build a green emissive glow layer) to only the intended surface.
- **Procedural eye glow:** Isolate the eyes via Cryptomatte → convert to a flat RGBA color layer → multiply with a blurred/dilated copy of itself for a soft radial gradient (avoids a flat, artificial-looking glow) → grade to the target color (green, with a touch of red for warmth) → re-merge the *original* alpha (the gradient trick corrupts alpha, so it must be copied back from the source Cryptomatte pass before final compositing) → layer a slow-scrolling `Noise` node in `multiply` to fake obscuration-flicker from the foreground smoke passing in front of the eyes (since the eyes are composited as a flat top layer with no real interaction with the smoke geometry) → `ap_Glow` (free Nukepedia exponential glow gizmo) → a squeezed `Radial` mask convolved (`Convolve` node) with the glow itself for a subtle directional flare.
- **Fake volumetric obscuration via alpha-driven Grade:** To darken the character convincingly under a smoke layer added with a `plus` merge (which otherwise loses all light-obscuration information the original beauty render had baked in), a `Grade` node is fed the smoke render's own **alpha channel** as a black/RGB source and merged multiplicatively under the character — effectively re-deriving "how much smoke is covering this pixel" purely from alpha and using it to darken the character before the smoke color is added on top. The same alpha-Grade is also keyframed (mix 1→0 over the first 50 frames) to fade the character in through the smoke at the start of the shot.
- **Diffusion/fake-GI trick:** A very large (~200px), low-mix `Blur` merged back on top of the sharp result is used repeatedly across nearly every layer in this comp — it blends layers together, lifts/softens pure blacks (avoiding an unnaturally crushed look), and reads as a cheap fake global-illumination bounce. Used on the smoke layers, the full comp, and (with a different blur radius) the dust/snow particle layer.
- **Motion-driven defocus flicker:** A `Defocus` node's amount is driven by a hand-built expression (`random(frame/7)`, offset/clamped to produce occasional spikes from a 0 baseline rather than constant jitter, then scaled) to simulate a handheld camera occasionally racking soft — a reusable pattern for any "make this metric spike occasionally, not constantly" expression need.
- **Finishing stack:** Lens-dirt texture merged in `plus` and masked by a feathered `Roto` so it only affects frame edges; `ap_Vignette` (Nukepedia) for edge darkening (or, in the blizzard variant, edge *brightening* for a different focus-pulling effect); `ap_ChromaticSpin` (Nukepedia) for subtle chromatic aberration; final `Crop` to a 2.35:1 anamorphic aspect for the cinematic finish.
- **Non-destructive full reskin (desert → blizzard):** The single most instructive idea in the whole comp: the *exact same* AOV/Shuffle/Merge node structure, rebuilt with completely different Grade values (desaturate everything first via `Saturation`=0, then re-introduce color — blue/white instead of orange/brown — plus a from-scratch snow-frost UV-projected texture reusing the same STMap+wraparound-fix technique as the scratches, masked to the wind-facing side using the normal AOV's red channel as a directional gradient mask, plus a contrast-pushed shadow-recovery pass using the same normal-derived mask) turns a desert sandstorm shot into a snow blizzard shot using **zero new Houdini renders** — purely a comp-side re-grade of the same split-AOV source data. This is presented explicitly as a demonstration of why AOV-split, non-destructive comping is valuable for fast production iteration/variation work.

### Key Steps
*(Nuke-focused — see Houdini/Solaris summary above for the sourcing side)*
1. Match Nuke's OCIO project color config to Houdini's own exported OCIO config (not default ACES) and ensure EXRs were rendered in ACES CG, so previewed colors match between apps.
2. For each render layer (BG smoke, FG smoke, character, dust): `Shuffle` out each individual split-light/volume AOV, label each Shuffle node's title with its `[value in1]` expression for clarity, grade each independently, then `Merge` them together (`plus`) to reconstruct the beauty.
3. For layers with alpha/edges (the character): unpremult all shuffled AOVs before grading, do the per-AOV color work, recombine, then copy the original render's alpha back in and premult once as the final step to preserve clean anti-aliasing.
4. Build a from-AOV Fresnel mask: `Shuffle` out the ray-origin and smooth-normal AOVs, `Clamp` both, `DotProduct` (vector3) them, refine with `Grade`; use as an edge-attenuation mask for projected textures.
5. Build UV-projected detail textures: `Shuffle` the UV AOV into RGB, fix any values ≥1 with an `Expression` (`R - floor(R)`, same for G), feed into `STMap` with a tileable texture as source, adjust tiling via a `Grade` on the UV channels' white point, mask to specific surfaces via `Cryptomatte`.
6. Build the eye-glow layer: Cryptomatte-isolate the eyes → flatten to RGBA → self-multiply with a blurred copy for gradient → grade to target color → restore original alpha via `Copy` → multiply with a slow-scrolling `Noise` for fake smoke-obscuration flicker → `ap_Glow` → convolved `Radial` for flare.
7. Fake volumetric obscuration: Grade the smoke render's alpha to black/RGB, merge multiplicatively under the character before adding smoke color on top; keyframe the Grade's mix to fade the character in through smoke over the shot's first ~50 frames.
8. Apply the large-radius/low-mix Blur-and-merge "diffusion" trick on volume layers and the final comp for cheap fake-GI blending and black-level lift.
9. Drive a `Defocus` node with a clamped/offset `random(frame/N)` expression for occasional handheld-feeling soft-focus spikes rather than constant jitter.
10. Finish with lens-dirt (roto-masked to frame edges), vignette, chromatic aberration, and an anamorphic `Crop`.
11. To re-skin the entire environment without re-rendering: duplicate the whole Shuffle/Grade/Merge chain, zero out saturation on every AOV layer first, re-introduce a completely different color palette via new Grades, and rebuild any UV-projected surface-detail texture (swap the source texture, reuse the same STMap/wraparound-fix/Cryptomatte-mask pipeline) with a normal-AOV-derived directional mask controlling where the new detail appears.

### Nodes / Tools / Settings
**Nuke:** `Shuffle` (AOV extraction, with `[value in1]` label expressions), `Unpremult`/`Premult` (alias-safe AOV grading), `Merge` (plus/over/in operations for AOV recombination and masking), `Grade` (per-AOV/per-channel color work, alpha-channel-as-mask obscuration trick), `Copy` (restoring original alpha post-AOV-math), `DotProduct` (vector3, Fresnel from ray-origin × normal AOVs), `Clamp`, `STMap` (UV-driven texture projection), `Expression` (`R - floor(R)` UV wraparound fix; `clamp((random(frame/7)-5)*20-10, 0, ...)`-style defocus-flicker driver), `Cryptomatte` (material/object ID isolation via Ctrl-click), `Blur` (diffusion/fake-GI trick, feathered roto masks), `Defocus` (expression-driven flicker), `Noise` (scrolling obscuration-flicker source, snow-texture alternative), `ap_Glow`, `ap_Vignette`, `ap_ChromaticSpin` (free Nukepedia gizmos), `Convolve` (directional flare from a squeezed Radial), `Roto` (edge/region masking), `MotionBlur` (built-in, applied to volume layers), `Crop` (2.35:1 anamorphic finish), OCIO project color management pointed at an exported Houdini config.

**Houdini/Solaris (source side, summarized):** Vellum cloth solver + `Vellum Attach to Geometry` + `Vellum Post Process`, `Extract Centroid` + Attribute VOPs (translation-cancel trick), Ripple Solver + POP Network (cheap wind-cheat shirt effect) + `Clip` (directional collision isolation), Pyro Solver + `Gas Turbulence` (layered) + `Gas Disturb` (rotational force) + `Volume Noise Fog`, POP Network + `POP Advect by Volumes` (dust sourced from smoke velocity), `Copy to Points` (packed instancing), Solaris USD sub-layering (path-matched material preservation), Karma Material Builder + MaterialX (`mtlx_fractal3d`, primvar-mapped noise via `rest` attribute), `Prune` (render-layer scene selection), shading holdout mode (`mat`), render visibility (`invisible to primary rays`), per-light LPE tags, split AOV export (diffuse/glossy per light, indirect volume, Cryptomatte, UV, ray-origin, normal).

### Difficulty
Advanced/Expert — assumes comfort with AOV/light-pass theory, USD/Solaris fundamentals, and Houdini simulation basics; the Nuke section specifically teaches production-grade AOV-reconstruction methodology that goes well beyond typical single-technique tutorials.

### Foundry App & Version
Nuke; exact version not stated on-screen (UI consistent with the modern node-graph/3D-system era seen elsewhere in this batch). Houdini/Solaris version also not stated.

### Tags
compositing, aovs, cryptomatte, channels, digital-matte-painting, projection, st-map, gizmo, camera-tracking, fx-simulation, 3d-system, advanced

---

## Related Tutorials
- Can I Create a Speeder Chase on a TINY Greenscreen? (`can-i-create-a-speeder-chase-on-a-tiny-greenscreen.md`) — shares `projection`, `compositing`; another Nuke map-painting/projection-onto-CG-terrain pipeline.
- This ONE Step Makes CG Look Cinematic (Most Artists Skip It) (`this-one-step-makes-cg-look-cinematic-most-artists-skip-it.md`) — shares `aovs`, `compositing`; both about Light-Group/AOV-driven selective grading for attention direction.
- How to use NUKE to Composite Blender Renders (`how-to-use-nuke-to-composite-blender-renders.md`) — shares `aovs`, `cryptomatte`, `channels`; overlapping AOV-recombination and Cryptomatte-masking fundamentals from a different cross-app pipeline.
- [CROSS-REFERENCE] Full Houdini/Solaris-side sourcing detail (cloth, ripple-solver shirt, pyro smoke/dust, USD assembly) is only summarized above — see `houdini-wand` skill's INDEX.md stub for this same video if deeper FX-simulation extraction is added there later.
