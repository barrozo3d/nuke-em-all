---
title: Introduction to Mari for Complete Beginners - 1 Hour Quick Start Guide
source: YouTube
url: https://www.youtube.com/watch?v=AcpwyNun0oo
author: FlippedNormals
ingested: 2026-08-17
app: Mari
version: Mari 7 (referenced Bakery feature)
tags: [interface, hotkeys, paint-buffer, nodegraph, merge-node, teleport-nodes, symmetry, triplanar, tile-nodes, paint-through, hand-painting, export-manager, bakery, geo-channels, beginner]
extraction_status: complete
frames_dir: tutorials/frames/introduction-to-mari-for-complete-beginners---1-hour-quick-start-guide/
frame_count: 14
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Introduction to Mari for Complete Beginners - 1 Hour Quick Start Guide

**Source:** [YouTube](https://www.youtube.com/watch?v=AcpwyNun0oo)
**Author:** FlippedNormals
**Duration:** 59m13s | 30 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Hi, this is Henning from FlipNomuls.com and in this tutorial you are going to learn how to use Mari.
[0:08] Mari is an incredibly powerful texturing software and by the end of this video you are hopefully going to have a good grasp of how to use it.
[0:16] Before we get into that though, make sure to check out our full introduction to Mari over at FlipNomuls.com.
[0:23] This is an incredibly elaborate course that covers really everything you need to know about Mari.
[0:27] Where we cover all the tools in depth, way more in depth of course in this video here and we cover how to texture a character at the very end,
[0:35] including how to do realistic skin shading at the very end.
[0:40] So check that out over at FlipNomuls.com, link in the description.


### Project Setup [0:41]
**Transcript (timestamped):**
[0:44] The first thing we are going to be covering is how to create a new project.
[0:48] You can very easily do that by right clicking or going down here and clicking New.
[0:53] So right click New and we are going to get up this new project interface.
[0:57] We are going to rename this intro to Mari and then we are going to be picking a model.
[1:03] We are going to be picking a high poly model and then we are moving on to the Channels tab.
[1:09] This is where we have various shaders that ships with Mari.
[1:13] So if you click on the category you can see that we have some that are highly specific like the V-Rare Material for VFX or V-Rare Six Material for VFX,
[1:20] Unreal, Metallic, Non-Metallic. Pick whatever you prefer.
[1:23] This can be a generic one which is going to work with all engines or it can be something specific like the Arnold Standard Surface for VFX.
[1:31] By clicking on Create next to any one of these is going to be creating this channel.
[1:37] So in this case it is going to be creating a channel for Diffuse Color, Specular Color and Specular Roughness.
[1:42] In this case we just want Specular Color and Specular Roughness and you can also change the size,
[1:48] the color space and the bit depth as well for this.
[1:51] So if you want to change this to something else you can very easily do that.
[1:55] I recommend that you don't mess around with this too much unless you know what you are doing.
[1:59] Then we are going to create new project.


### Interface Overview [2:02]
**Transcript (timestamped):**
[2:02] The very first thing I'm going to be doing is going to view and default layout.
[2:06] This ensures that I have the exact same layout as you do.
[2:09] Then I'm going to enable full screen just so we get rid of this menu at the top.
[2:15] The interface in Mari is really flexible and easy to customize.
[2:19] So for instance if you want to move the layers to the left side you can very easily do that
[2:23] simply by dragging this over.
[2:25] If you want to take the channels, move them on top you can do that.
[2:28] If you want to move it next to the layer so it's not going to be on tab you can very easily do that as well.
[2:33] You can change the interface to whatever you prefer.
[2:36] It's a very flexible and very powerful system.
[2:39] What we are going to be doing though we are going to be removing all of these ones
[2:42] because we aren't really going to be using all these ones at the moment.
[2:45] So we are just going to start with clean slate.
[2:48] We are going to customize an interface ever so slightly though.
[2:51] We are going to be moving the node graph over to the right side.
[2:55] This is going to make sense a bit later on and then we're going to take the node properties,
[2:58] put them on the top right here.
[3:00] Then we are just going to scale this up like so so we can see the node graph and we can see the node properties.
[3:07] We are also going to take the color space controls all the way down on the bottom right here.
[3:12] If you want to hide or remove certain elements as well you can also right click on the interface
[3:16] and you can just for instance enable view transform.
[3:18] So if you don't want these at all you can just enable and disable them.
[3:21] So if there are certain things you don't want for instance the controls down here
[3:24] you can just right click navigation and just hide these ones.
[3:27] Speaking of navigation this is going to be the first thing that we are covering.


### Navigation [3:31]
**Transcript (timestamped):**
[3:31] You rotate by alt left mouse button.
[3:34] You pan by alt shift left mouse button.
[3:38] And you zoom by alt right mouse button so dragging left to right.
[3:44] You will also have to change something slight in the preferences but go into edit preferences navigation
[3:51] and just make sure that lock to world up is enabled.
[3:53] If this is not enabled you are going to get off center right away so always make sure this is enabled.
[3:59] And if you do get off axis you can also hit the control R key just to roll the camera
[4:05] which is really quite handy.
[4:06] This can be really useful if you need to go into a certain spot and just somehow just go in and do that.
[4:11] But very easy to go in and roll the camera like this control R.
[4:16] Continuing with the interface at the very left this is where we have all the main tools.
[4:22] Right below it we have the color so you can very easily swap the foreground and the background color.
[4:26] If you click on the color itself you can change the color and you can now just swap it like so
[4:31] and you can reset it with the button right below it.
[4:34] At the very top we have some handy options for instance we can export out textures right here.
[4:39] We can bake right here and we have selection tools right here as well.
[4:44] To the very right this is where we have a lot of interface items like channels, colors, the
[4:49] basically undue list right here, image managers, lights and so on.
[4:53] So you're going to be using some of these quite a lot and some of these not at all.
[4:59] But if you do want to use them for instance if you want to get the image manager up you can
[5:03] simply just click on the image manager and now you can see it fades open and then if you want
[5:06] to move this somewhere you can just drag this on top like so or if you just want to have this
[5:10] temporarily somewhere you can just do this again image manager and you can just see there is a
[5:14] pin icon here just hit the pin key and now this is just going to be pinned here.
[5:18] So if you need to use this just temporarily you can very easily just pin this around and then
[5:23] close this once you no longer need this. We also have various tabs the first one is the project.
[5:29] So here you can see all your projects then you can see the UVs of the object you currently have
[5:34] selected. Next up we have the ortho and UVs which allows us to see the model in ortho and allows
[5:40] us to see the UVs you can just drag this to the left and this to the right so you can see the UVs
[5:44] a bit better. Then we have perspective and then finally we have ortho as well. I always prefer
[5:49] to work in ortho in Mari. The reason is that if I want to go into an ortho view it's a lot easier


### Orthographic Views [5:51]
**Transcript (timestamped):**
[5:55] to paint from one of the sides so you can do this very easily with the one, two, six keys. So one,
[6:00] two, three, four, five and six so then you can see the various views. This is not a locked view at all
[6:07] so you can just very easily just go in here like this it's simply just a snapped view. This is why
[6:12] I prefer the ortho versus perspectives because now I know if I were to paint here this would just


### Using Selections [6:16]
**Transcript (timestamped):**
[6:17] project in an orthographic manner. One of the tools you are going to be using the most by far
[6:22] is going to be the selection tool. You can find this by going all the way up here to the top left
[6:27] or you can simply hit the S key. So S is probably what you're going to be using most of the time
[6:32] but you can also just find it right here. The select tool has a few options and you can find
[6:36] this up here or by right clicking. The right click menu is something you are going to be using a lot.
[6:40] We have a few main modes so we have object, patch and face mode. Object means you are selecting
[6:46] the whole object. Honestly I always work with whole objects anyway. A very rarely important
[6:51] additional object so I don't really use this a whole lot. What I do use a lot though is patch
[6:55] mode. Patch basically means you them. So if you are in the UV view here you can see that if you
[7:01] select this one they selects a whole you them. So a lot of the selection in Mari is based entirely
[7:06] around you thems. You can also select individual faces as well. So you can for instance go in here
[7:10] and you can just select the faces just by dragging on top of this and if you want to select through
[7:17] you can go up here and they're facing and just select through and now this is going to select
[7:20] through the whole thing. Currently this is using a rectangular selection which is of course is handy
[7:25] but you can also set this to be lasso, polygonal or smart. Smart is really handy because smart is
[7:37] going to be selecting the whole thing that's connected. So if we can now click on tooth here
[7:43] for instance or the gums this is going to be selecting the connected polygon islands. So this
[7:49] is super handy. We can also change the type in the smart mode from connected mesh to connected UVs.
[7:55] So this is going to be selecting everything that's connected in pure UVs now which is going to be the
[7:59] UV island. So really really really handy stuff. Most of the time though you are probably going
[8:04] to be dealing with the patch mode and you are going to be dealing with probably the square
[8:10] rectangular selection. Now you can just select something here and very easily hide something
[8:14] or unhide something. You can hide something with the H key. So now you can just very easily hide


### Hiding and unhiding [8:15]
**Transcript (timestamped):**
[8:18] this. You can hide additional things. If you want to show everything you hit control shift and H and
[8:23] this is going to hide everything. If you want to hide unselected that's shift and H. So if you only
[8:27] want to have the face enabled you can very easily do that. Then control shift and H to make everything
[8:31] visible again. So the selection tool is something you are going to be using a lot. Next up let's talk


### Objects and versions [8:35]
**Transcript (timestamped):**
[8:36] about objects. The object palette is going to be here in the middle to the right and we are just
[8:41] going to be docking this over right here. Like I said I don't tend to add new objects a whole lot
[8:46] but what I tend to do a lot is I tend to change the versions. So using objects can be just a
[8:52] little bit confusing and I tend to set up my project so that all the UVs are non-overlapping.
[8:57] So for instance here the teeth are going to be in one utim. The head is going to be in one but this
[9:02] is also personal preference. I just prefer to set up this way because it means that export and texture
[9:08] setting up channels and such is just much much easier. But if you want to add a new object you
[9:13] can very easily do that by right clicking add object and here we can add a new one which is
[9:17] going to be a low poly version of this. And now we have the same options as we had in the initial
[9:22] palette as well. Just hit okay and now you can see we have another one. Now we have the head right
[9:27] here and this is a low poly head. You can see this if we were to enable the wireframe and a very top
[9:32] right. So now we have the new head. What we can do though which is quite handy we can remove it
[9:38] right here just by selecting the minus key. We can add it as a version instead. What I do a lot is
[9:44] instead of adding new objects I'm just adding versions and this allows me to very quickly go
[9:49] between a high poly version or low poly version or simply if I'm iterating on a model and I keep
[9:54] changing the model then it can very easily just add a whole new version. So we can do that by right
[9:59] clicking add version and here we can add the head and now you can see nothing changed but if you go
[10:04] under the geometry you can see that we now have two versions and this is super useful because this
[10:09] is not an intelligent feature in any way. It doesn't try to convert anything or anything like that.
[10:14] What this is doing is simply just replacing the model itself. So if you have tons of painted data
[10:19] this painted data is going to be stored in the textures. It's not stored in the polygons themselves
[10:26] in any way like it is in painter where the curves are stored on the model or in seabush where it's
[10:31] stored in the verts with polypainting. This is just stored in the baked textures. So if you update
[10:37] the model but the UVs remain the same you simply just add a new version and you change to that
[10:42] and you can very easily just go back and forth. Next up let's talk about the lights. The lighting


### Lights [10:44]
**Transcript (timestamped):**
[10:47] in Mari by default is not fantastic. What you can see here is that some parts are dark some parts are
[10:53] bright and we can't have that. So we can change this by going to the lights palette and we can just
[11:00] pin this over right here and we are going to be disabling all of them apart from the one that says
[11:05] one. We are going to go down to the general and change the fix to and change this to camera
[11:11] which means that if you rotate around now you can see that this indeed changes with the camera.
[11:14] This means that we're never going to have just dark spots on our model. If this is set to scene you
[11:19] might have areas now that are always dark and that's really bad because we can't see what we're
[11:24] working with. So it's changed as a camera then we can go down here we can change the position as
[11:28] well. So I always prefer to have this pretty frontal but a little bit from the top like so. So we
[11:34] can see some shadows and that's pretty nice. Now you can also change the intensity as well to fit
[11:41] what you have. So if you hit f1 you can see that this turns flat f2 turns shaded without spec and f3
[11:48] shows you with spec as well. So you just want to be sure that these are matching. You can see here
[11:53] this is white and this is gray so we just have to increase this so this matches. I prefer something
[11:57] like 1.5 is close at least but you have to try to match this. You can also enable an HDRi as well
[12:04] in the environment up here which is super handy if you have a lot of reflections. So now you can see
[12:10] that this indeed reacts to reflections. If you have an object that's very metallic or just very
[12:16] speccy this is really really really useful particularly when you are developing your
[12:20] specular reference map because otherwise you really are working in the blind. You can also
[12:24] enable your own HDRi or load in your own HDRi with this nice friendly button which says load an
[12:30] image file. We are just going to be disabling this one because we don't really need this at the moment
[12:34] but you really just want to be sure the light is locked to the camera and not locked to the scene.
[12:40] Next up let's talk about the channels. The channels is what's going to be exported out from
[12:47] Mari at the very end. This can be something like a base color which is going to be directly plugged
[12:52] into the material in your rendering software. It can be something like a specular roughness or it can
[12:57] be a mask which you are going to be using in your looked at software to develop the look further
[13:03] but regardless it's something that's going to be exported from Mari and you can find the channels
[13:08] all over here. We can just dock this over as well. We can just pin this here and you can see we have
[13:12] only three channels at the moment. We have bump, diffuse color and specular roughness and what you
[13:17] can see as well we haven't gone to nodes yet but you can see that these also exist right here. So
[13:22] these are the different channels. So if we for instance rename this to coal you can see this
[13:27] changes right here as well which means you can also rename this right here. So you can double
[13:32] click on a node see this in the node properties. So if you change it here this will also change here.
[13:37] You can see that we have two bits of information next to this as well. We have 16 which says that
[13:41] this is a 16-bit half float channel and you can see that this is gray which means this is scalar.
[13:49] The next one is 16 and this has color which means that this is a non-scalar. Scalar simply
[13:54] means that the data here is going to be computed while the data and the color is here to be seen.
[14:00] This means that if you're working with color this should not be set to scalar while a bump map and
[14:05] a specular roughness should be set to scalar data. A normal map as well should also be set to scalar
[14:12] because while it has colors it's there to be computed. So that's a very easy way to think about
[14:17] it. If the colors are here to be seen non-scalar if it's here to be computed in the shader then
[14:23] it's scalar. You can also change the bit depth and the size of this by right clicking. Then we can go
[14:29] to resize and here you can change the resolution. This is destructive so if you change this from
[14:34] like 4k down to like 1k and then up again you've lost data. That's important to note and you can
[14:40] also convert it to a 8-bit or 32-bit or 16-bit by going to right click and then convert channel and
[14:48] here you have additional settings here. So currently this is 16-bit so we can't convert to 16-bit but
[14:52] we can convert to 8 or 32. Now the last thing is we can create a new channel which we can very easily
[14:57] do by just clicking this plus icon here and we can set the name. This can be for instance mask01.
[15:03] So now we have a mask and we can set this to be 1k. We can set this to be scalar data and we can set
[15:09] this to either be transparent which it currently is because you can see the alpha is enabled or we
[15:14] can set this to be black so now this is going to be filled with black. So we can create this one and
[15:18] I can see down in the node graph we are going to be having this one right here. So we are going to


### Paintbuffer [15:24]
**Transcript (timestamped):**
[15:27] be closing this one then we are going to be deleting this because we don't really need this at the
[15:30] moment. Next up we are going to be talking about the paint buffer. The paint buffer is a unique
[15:34] concept found in Mari that you don't have in other texturing solutions and this can cause a lot of
[15:40] confusion. We are going to be painting right now just a little bit nothing too fancy. We are just
[15:45] going to be painting in the paint node right here. We can actually just preview this through the base.
[15:50] Actually this is preview this through the whole material. We'll get to this how we do this in
[15:53] a second but what we can see now is if we were to zoom out actually let's zoom really far in now
[15:59] what you can see is that we have a square around the model and on the bottom here it says 2k,
[16:06] 60-bit, half paintable and this is the paint buffer. If you are painting outside of this one
[16:13] meaning if you were to paint like here it doesn't matter there's nothing paintable there so if you
[16:18] try to paint now here you can see that this is not possible and the way you can think about the
[16:22] paint buffer is as if you're painting on a glass pane so you're not actually painting on a model
[16:28] right now you're painting on glass then once you're happy with this then you can commit to it and
[16:33] project whatever you have in the glass pane onto the model so this means if you're now able to rotate
[16:38] you can see that this doesn't actually go onto the model at all this is just on a glass pane on top.
[16:43] So what's happening here is that this is on a glass pane and this is 2k, it's 60-bit and it's
[16:48] paintable which means that if you were to have an image that's 8k and you're projecting this onto
[16:54] our model well you're only going to get 2k or it means if you are having an image that's like
[16:59] 512 and you're projecting it well you're still projecting in 2k of course it's going to be way
[17:04] too low-res but this is the date that is being projected. If you don't see the paint buffer
[17:09] that means that either it's way too close like this or it's like stupidly small the way you can
[17:15] check this is by hitting the Z key and then you can drag left to right and now you can see on the
[17:19] bottom here you can see the and I can see you're on the top here that you have the zoom level you
[17:24] can also reset this if you are completely screwing this up and you can zoom in or zoom out like this.
[17:31] So this is why I have the node graph right here to the right and why I have the paint buffer so
[17:36] large so I can really just paint on most of the screen. You can clear the paint buffer by hitting
[17:40] Ctrl, Shift and C or you can click on this button right here this is probably the second time in my
[17:45] life I use this one because I only use Ctrl, Shift and C. You can get settings for the paint
[17:50] buffer we're going to painting let's just dock this over right here actually so we have a bit of
[17:55] space and then under painting you see you have paint buffer. This is where you can change the
[18:00] color depth from 8 to 16 to 32 and the size itself and if you want to clamp it meaning that the
[18:06] value is going to be only between 0 and 1 you can also change the scale of it as well this is
[18:11] essentially what we're doing here you can see here if you zoom in or out with a Z key you can see
[18:15] this change in the scale and this setting here is something I highly recommend that you disable.
[18:21] This is an incredibly annoying one so this means if you were to bake this down by hitting the B key
[18:26] which is how you bake you can see this is not resetting this but if this is enabled and you just
[18:32] paint something now you can see this is going to reset and now this is massive so that means you're
[18:36] going to have to keep redoing this over and over and over again it's very very very annoying if
[18:41] this is set to enable so go in here set this to disable and then you can just find the size of
[18:47] your paint buffer. Another setting you might want to change this is up to you is the bake behavior
[18:53] my preferred method is setting this to manual what this means is that I can paint whatever I want to
[18:59] and I can rotate around as much as I want and only when I hit the B key for bake will this be bake
[19:06] down and as you can see if I hit the B key for bake yeah it is bake down but it's not cleared
[19:10] which is quite handy for instance if you are doing a highly specific pattern I don't know like a tattoo
[19:15] or whatever it is or if you have an image in the paint buffer then you can keep reusing this image
[19:21] over and over again but if this is set to clear only or auto-baking clear that means this is going
[19:27] to be removed so I personally really recommend setting this to manual this is again under
[19:33] painting projection settings and then projection and here we have the options and
[19:40] this means you can paint control shift C and you can go in here if you want to hide the paint
[19:45] buffer you can hit the period key and you can see this now hides the paint buffer this is really
[19:51] useful you can see this changes down here as well so now it's set to invisible this is incredibly
[19:55] handy if you need to just check what you've been projecting is looks good or not instead of having
[20:00] to control shift C and undo and such so period key super handy another setting that's incredibly
[20:07] useful is the ability to paint through so if we go to a ortho view like by hitting the two key we
[20:12] can go to the side view and we try to paint on the nose what's going to happen now is that we are
[20:17] going to get this nasty edge because this is just painting what we're seeing sure we could use some
[20:22] masking techniques to make the softer but it's still really annoying so what I want to do instead I
[20:26] want to just paint through the whole thing give it very easy to do that if we just remove this so
[20:32] here we go and then by going to the bottom right you can see that we have a little setting in the
[20:37] middle this says projection on front of object so if we click this one this is going to be through
[20:43] so now if we were to paint here now we can even paint a bit on this chin and such paint here
[20:47] this is going to paint through so now you get this really nice and soft gradient just remember
[20:54] to disable it because if you keep painting now here whatever you do paint hit the B key for bake
[21:00] this is going to well paint through so this is going to go on the other side as well so just
[21:04] be sure to disable this one otherwise you are going to be in a world of pain one quick note
[21:09] before we leave the paint buffer and the settings which is the project on and this needs to be set
[21:14] to all because if this is set to select only you are not going to be able to paint sure it's really
[21:18] handy because it means you can select something and it's going to be allowed to only paint on that
[21:22] the problem is you are going to forget that this is set to select it only and you're going to forget
[21:27] that you have a selection so probably this is going to mean that you are going to do an
[21:31] anger google search saying why can't i paint in marie so just be sure this is set to all next


### Node Graph [21:37]
**Transcript (timestamped):**
[21:37] step let's look at the node graph so we are going to be killing this one just be sure we only have
[21:44] the node graph enabled so here we have the node graph we have the node graph which has the default
[21:49] nodes set up these are just the ones that were created when we set up the project and on top
[21:54] we have the node properties so every single node will have properties you can double click this
[21:59] and you can see the properties next to the node properties you can see that you have a number i
[22:03] prefer to set this to one this is how many node properties you have active at the same time so
[22:08] you can enable this one here set to 10 and if you were to have this now you can see we have a really
[22:13] long scroll bar this gets very confusing so i always recommend setting this to one the navigation
[22:19] in the node graph is very simple right mouse button to pan and alt and right mouse button to
[22:25] zoom in and out you can create nodes by hitting the tab key and you can search for a node for
[22:30] instance you can type color and hit enter and now we're going to have a color it's going to be down
[22:35] here now or you can right click nodes and you can create nodes from this list i pretty much never
[22:41] use that menu i only hit the tab key and i type what i want then i hit enter and there we go
[22:49] the way nodes works in marie is honestly quite simple ones to understand it but it can be a
[22:55] little bit intimidating if you don't so let's work from the right to the left just to keep this simple
[23:01] at the very right we have the arnold standard surface this is the shader if you double click
[23:05] this one you can see that we have all the settings for the shader so we can change the
[23:11] amount of specularity here we change the color and such but of course these are things that's going
[23:16] to be changed with texture maps themselves but you still have some handy options like you can go
[23:21] down to the bump and you can change the amount of bump the bump method and such so this is is really
[23:26] useful this is going to be quite similar to what you have in arnold but don't trust it fully because
[23:32] you know it doesn't do proper displacement of subsurface and that kind of stuff but it's still
[23:36] a decent approximation then we have the color this is a channel this is what you are exporting out
[23:42] so if you were to go to the export manager right now you can see that this is color this is specular
[23:47] roughness and this is bump and if we were to hit export this is what's going to be exported out it's
[23:52] going to be everything plugging into this the merge node is probably the most used node in


### Merge Node [23:55]
**Transcript (timestamped):**
[23:58] marie and this is because you need this constantly this is not a cool node or anything like that
[24:03] it simply merges things together then we have a paint node and we have a bottom transparency
[24:08] this simply allows us to paint right now but we can really delete everything here so all of
[24:15] these ones we can just straight up just delete and then we can create our own nodes the only thing
[24:20] you need here is you need an input going into the channel itself so we can for instance create
[24:26] something ourselves so we can hit the tab key we can type color and now we can create a color
[24:31] node and this allows you to have a simple color so we can just set this to be red and we can just
[24:37] plug this into color in order to see these nodes in the viewport we can select them and then we


### Displaying nodes in the viewport [24:39]
**Transcript (timestamped):**
[24:42] hit the one key so if we do this now you can see we are seeing this node if we go to the color you
[24:47] can see we're seeing this one which is of course it's the same input and if you go to the arnold
[24:51] stand on the surface we are seeing that if we were to go to the specular roughness of course there
[24:56] was no data here you will be able to see that one and we can just go back here and what you're seeing
[25:02] is that this goes into a viewer which is really handy if you are familiar with nuke or fusion this
[25:07] is going to be quite familiar if not you won't be wondering what's going on if you hit shift an s
[25:13] on the viewer this is a way to expand the node if for some reason the nodes are contracted like so
[25:19] then you can hit shift an s on them to expand them this is really useful and you can see that these
[25:23] are in the first port this is quite useful because this allows you to have up to nine
[25:29] ports enabled so you can see for instance this is connecting to one but if you set the arnold
[25:34] surface and we set this to two now that means that we can now connect these two together so if we hit
[25:39] one we can go to the first port and we hit the two key we can go to the arnold standard surface this
[25:46] is incredibly useful if you have a complicated network because now you can go between this very


### Flat, shades and fully rendered shaders [25:51]
**Transcript (timestamped):**
[25:51] easily we can also go to the left and here we have the flat view the basic view and we have the full
[25:57] which is going to be the full specularity the full material so this is quite useful so this is how
[26:03] we see the nodes in the actual viewport now just a note notice the paint buffer is now gone this is
[26:11] really annoying so you just have to be on top of that whenever you can't see the paint buffer
[26:16] you just have to be on top of that use the z key for that you can very easily copy paste nodes by
[26:21] hitting the node selecting node ctrl c and then ctrl v and this is going to be simply pasting the
[26:28] node now we can use this somewhere else so we can now go into this one and we can plug this into
[26:32] the specularity we can just make this really dull or really rather really rough or really smooth
[26:38] like so going back to the merge node this is the node that you are going to be using all the time
[26:43] you can make a merge nobody n key simply hit n and now you can plug things into the merge so we
[26:50] have three ports in the merge i think this is pretty important to talk about we have the base
[26:54] which is going to be the bottom then we have the over that's going to be well over the base and
[26:58] then we have a mask and this is something we can use to mask out the over so let me show you an
[27:04] example of this let us plug the color into the base so now this is going to be the same color so
[27:13] we haven't really done anything we just plug this in then we plug the output into the channel itself
[27:17] so if we were to now make sure this was previous like this and then we can now make another color
[27:23] ctrl c ctrl v and we can make this really dark like so and we can put this in the over now this
[27:31] is going to change color to this one now what we want to do is we want to mask out the over with
[27:37] something this can be something we're painting or it can be something procedural we can hit the tab
[27:41] key we can type clouds and here we have a cloud and then we can plug this into the mask and I can
[27:46] see that this is masking this out right away and this is one of the advantages of nodes this of
[27:52] course is something you can do very easily with layers and if the only thing you're doing is this
[27:56] kind of stuff you you can just stick the layers but this becomes incredibly handy because now you
[28:01] can use the same masks the same nodes and tons of other merge nodes and tons of other systems
[28:08] now for instance you can go in here you can change the color of this and you can very easily just
[28:13] build a procedural network we can also delete a node by selecting a node and hitting the delete
[28:18] key this is going to well delete the node we can also hit ctrl and x which technically doesn't
[28:23] really delete it instead it cuts it out but just ergonomically the ctrl x is a lot easier to do
[28:29] than going all the way over to the delete key so ctrl x is how I delete stuff a little bit dirty
[28:34] but it works now if we want to insert a merge node we don't we can of course just hit the m key and
[28:41] we can just insert it in here but a quicker way is to select first the base then the over then
[28:46] hitting the m key and I can see this connects this up right away then we just have to go here and
[28:51] this is just really handy another way to do this is if we already have a merge we can just hover
[28:58] over the connection and I can see this just inserts itself right away then we can just plug
[29:03] this in here and plug this in here and if we want to extract this meaning that we just want to remove
[29:09] this from the node graph and we want to use it somewhere else we have two main ways of doing
[29:13] this we have ctrl shift and x which is going to simply extract it like so so it doesn't delete it
[29:17] but just removes connections or we can do a fun one that introduced recently which is shake it
[29:22] this is going to simply remove the node from the connections let's just undo so we can go back to


### Swap node inputs [29:27]
**Transcript (timestamped):**
[29:28] and if you want to change the inputs for instance we want to make the base the over and
[29:33] the over the base we can do this very easily with shift and x so now you can see you can just change
[29:37] the inputs real fast instead of having to go in here and then having to like move this around
[29:41] which is really annoying shift and x you're going to be using this a lot so what if you want to paint


### Paint Nodes [29:44]
**Transcript (timestamped):**
[29:46] something well you can easily do that as well with a paint node so delete the clouds then we
[29:51] make a paint node and we can do this by hitting the p key or right click and create paint node this
[29:57] is so useful that is right here because you're going to be creating this all the time so create
[30:01] paint node this is where we are having a similar menu to the channels when we created this we can
[30:07] change the size to 2k to whatever you want to bit depth you can't see it here but we actually have
[30:12] two inputs we have the color itself then we have the alpha so currently this is going to be filled
[30:18] in entirely with black but if you want this to be transparent we can go in here we can just change
[30:22] the alpha so now this is going to be a transparent object and this is going to be scalar that we may
[30:28] or may not want in this case we actually want this to be scalar because this is going to be a simple
[30:31] mask between these two then we can hit okay and now we simply just plug this into the mask and now
[30:37] if we were to just paint now you can see that this paints in exactly where we want this to be
[30:43] but an issue with this is that this since this has transparency our painting now is so sharp so what
[30:49] we can do we can fill this in with black instead of course we could have just done this when we
[30:53] created the node but what we can do instead as a little tip is we can hit the s key hold down the s
[30:57] key select the whole model right click fill and black and now the whole thing is going to be filled
[31:05] in with black and then we can just continue painting with this and I can see we get this really
[31:08] beautiful fall off so now you can paint wherever you want on the model and hit the b key to bake
[31:15] and there we go now you can of course just see this specific input by clicking the one key
[31:21] and then you can see this changes the view so now this is what it looks like in this case it actually
[31:24] read we can just make this white as well wouldn't matter too much but now we can just see this is
[31:29] white because this is just a value the only thing it cares about is the value itself so now we can
[31:33] go in here we can just preview this through the Arnold standard surface you can see what's going on
[31:37] now so you can very easily paint like so now what if we want to paint with symmetry this is very


### Working with Symmetry [31:41]
**Transcript (timestamped):**
[31:44] easy to do we can go under the mirror projection which is right here the fourth item from the bottom
[31:50] and we can enable this to mirror x and now you can see we get this plane in the center so now we can
[31:55] very easily just paint on one side and where we paint here it's going to be mirror just bake it
[31:59] and it's going to be mirror right away what we can do we can just select the whole thing again
[32:03] right click fill black and now we have removed all this and now we can just continue painting
[32:09] like this anything that's white is going to be revealed anything that's black is going to be
[32:13] removed so now you can just paint this out and you can see how this transforms right over to the
[32:19] other side another way to deal with symmetry is to this depends on your UVs but in this case we
[32:25] have kind of symmetrical UVs this is not perfect in any way but it's kind of there if we were to
[32:29] paint something on one side in the UV editor we can bake this down now what we can do we can select
[32:35] this item right click patches mirror bit of mouth full as one and then we can do right to left and
[32:41] I can see this mirrors the whole thing from right to left just be sure that the paint note is selected
[32:46] if it's not selected and you right click and you do mirror and right left it's going to be like hey
[32:52] whoa you don't have anything anything selected you want to mirror everything and you're like nope
[32:57] because that would cause absolute mayhem so this is a very quick quick and easy way to mirror
[33:01] something over just be aware of the fact that you do need symmetrical UVs for this there's nothing
[33:06] magical going on it's simply mirroring everything from right side to the left side in the tile itself
[33:14] also when it comes to from right to left just to explain this real quick when it says left to right
[33:19] right to left this is within the tile itself so from right to left means from this side to this
[33:24] side and left to right is from this side to this side there's nothing to do with the character side
[33:28] it's purely within the tile itself let's go back to ortho and let's talk a bit more about nodes a
[33:35] quick way to organize nodes is to add dots so you can very easily do this by holding on a control
[33:40] key and I can see you get this diamond shape you click on this one and now you can see you get this
[33:46] little dot that makes it a lot easier to organize your nodes where you can hit the period key as
[33:51] well within the node graph so now you select this input and you can put this somewhere else if you
[33:56] want to for instance you can create additional dots and you can just keep using this one this is
[34:02] really really handy this becomes a little bit spaghetti though so another way to deal with
[34:07] this instead of working with all these crazy connections is to use teleport nodes teleport


### Teleport Nodes [34:12]
**Transcript (timestamped):**
[34:12] nodes are incredibly useful when it comes to organizing your node graph so how they work
[34:16] is that you can create a teleport broadcast here and you can make a teleport receiver over here
[34:21] and instead of it there being a node connection between them it's just done without well a node
[34:26] connection it's just teleporting from one to the other so let's say we want to have this output here
[34:32] be used somewhere else so let's say we want to have this be used as a specular map we can just
[34:36] delete this as well just remove all this remove this input instead of having this be connected in
[34:41] like so in this case of course this is an issue but what if this has 200 nodes then it's very much
[34:46] an issue so what we can do we can just move all of this select them just move them over then we
[34:51] can create a teleport just type teleport I hit in the tab key and we want to do a broadcast because
[34:58] this is broadcasting data then we connect the output to this one this shouldn't go in between
[35:03] this this should just be a separate little node going out on the broadcast we can type for instance
[35:08] base call and now we have to make a teleport receiver so hit the tab key teleport teleport
[35:15] receiver and then we have to duplicate and then we'll go on our channel and right here we can
[35:21] set this to base call and now if we were to just plug this in you can see that we have the exact
[35:26] same data in these two now of course the difference is going to be that just have to connect this up
[35:32] the difference is going to be that one is a scalar map the other one is not so this is just going to
[35:39] look a little bit different than what we have here but that's the main difference the data itself is
[35:44] exactly the same so this means you don't really need to have this insane spaghetti you can just
[35:49] use teleport nodes to transfer data for one point to another the clever workflow here is that you
[35:55] can create tons of masks in the beginning of your project mask you know you're going to be using this
[36:00] could be for instance for the ears the teeth the nose the eyes and such and then instead of having
[36:05] them connect through nodes anywhere you can just create a teleport broadcast call this like mask
[36:11] teeth then you can make tons of teleport receivers and now you're going to have a much easier time
[36:16] actually doing your texturing you can disable nodes very easily with the d-key so if you want to


### Disable Nodes [36:18]
**Transcript (timestamped):**
[36:22] we can just preview this one if you want to for instance disable the color you can very easily
[36:25] do that d or if you want to disable the whole thing you can just hit the d-key and this disables
[36:29] this one very useful if you just want to see what something looks like before and after


### Rename Nodes [36:34]
**Transcript (timestamped):**
[36:34] you can rename nodes by hitting the n key and now you can just type here color test and now you can
[36:42] see it here or you can go all the way to the top and you can just rename this right here
[36:46] you can search for nodes by hitting the j key so now for instance you can type the
[36:50] yes and you can see it here and now you can see this is going to be selecting the nodes that you
[36:54] are searching for very very useful this means that there is an argument for really keeping your
[36:59] nodes clean as well because this can get very messy you can create backdrops very easily for


### Backdrops [37:02]
**Transcript (timestamped):**
[37:04] organizing nodes you can select all the nodes you want in a backdrop tab backdrop and now you see
[37:09] you get a backdrop for this then you can double click it you can name the backdrop up here and
[37:13] call this color and now you can see the refreshes and then we have the color you can also change the
[37:19] background color as well and then we can go down here we can set do the same thing for this one
[37:24] backdrop and we can call this like spec r for specular roughness and you can change the color
[37:30] of this as well so this is a very very very handy way of organizing your projects another way to
[37:36] clean up the scene to make this easier to use is instead of working in a geographical proximity
[37:42] of the channel itself we can just work somewhere completely different and then use teleport nodes
[37:48] to get the data into the channel so what we can do we can just move all this all the way
[37:53] somewhere else then we can in this case we can actually reuse this one here the base color
[37:57] and then we can go down here we can make a teleport receiver and then we can just plug this in here
[38:03] this is just going to go in here and then the receiver is going to be using the base color
[38:08] and this means that you don't have to have really any connection between them you can
[38:12] also just see here in the little map you can just see where it lives so this is a really handy way
[38:17] of just keeping everything nice and simple because it means this just gets messy after a while so and
[38:23] this is my preferred way of working keeping everything nice and organized speaking of organized
[38:28] sometimes stuff gets messy so you can select the nodes you can hit the l key or you can right click
[38:33] and auto place and this is just going to make this a little bit cleaner it's not too much to
[38:38] clean up at the moment but this can very easily get very messy so if this happens l auto place
[38:45] this saves your day next up let's talk about some of the grading nodes the first one is going to be


### Grading Nodes [38:47]
**Transcript (timestamped):**
[38:50] great and this you can access by just typing great and this now just plugs in this is a very simple
[38:57] grade node that allows you to change the black point the white point you can lift the whole thing you
[39:01] can offset the whole thing you change the gamma you can change the gain and multiply as well so
[39:06] this is a way to change the values of the textures you're going to be using this a lot if you want
[39:12] to mask a great node you can see there isn't really a mask port to it so we are going to be
[39:16] extracting this one control shift and x and then we're going to make a merge so just select this
[39:22] and this and then hit the m key just the base and the over and then we need to plug the output
[39:27] under the input of the grade and then we mask this under the mask here so if we now want to have a
[39:34] cloud to mask this off we can very easily do that this was a little bit confusing to me when I first
[39:39] started with nodes I didn't really understand exactly how to grade procedures but this is how
[39:42] you do it another useful node is the HSV node which is hue saturation and value this is super useful
[39:50] and allows it to change well you guessed it the hue saturation and value so you can very easily just
[39:54] go in here change the hue saturation and the value basically what is the color how strong is the color
[40:02] and how bright or how dark is it so this is something you this is a node you're going to be using a lot
[40:07] let's just disable the mirror projection and next up we are going to be talking about the
[40:11] invert node invert node and that's exactly what you expect it simply inverts things this is not
[40:16] particularly useful when it comes to color but it's essential when you are creating masks because
[40:21] you need to invert that stuff all the time next up let's talk about the image manager the image


### Image Manager [40:23]
**Transcript (timestamped):**
[40:25] manager can be found up here to the right and we are going to be actually docking this over we can
[40:31] very easily add images to the image manager simple by dragging and dropping these from the windows
[40:36] explorer or linux equivalent if you are on linux and then you have them in here you can see the
[40:42] resolution and you can see the path of it as well and you can change this from a scalar to a non-scaler
[40:49] so this is a scalar image make sure to tick this one so that's really really really handy you can
[40:54] have bunch of images here so we can just take all of them at the same time just drag them in like so
[40:59] and I can see that all of these are going to be added right here and now if you want to remove a
[41:04] duplicate or delete something you simply select the image and hit the delete key right here or right
[41:08] click and then close and there you go this now removes it next up let's talk about triplaners


### Triplanars and Tile Nodes [41:13]
**Transcript (timestamped):**
[41:15] and tiles none of these are really tiled but they work really well as triplaners a triplaner is a
[41:23] kind of node that allows you to very quickly add variety to your textures by having three planes
[41:31] and projecting images from them and blending between these three projections this is incredibly
[41:36] useful as this does not really produce seams in the UVs and if you do change the UVs later on
[41:43] this is based on world scale this is not based on your 2D space so we can very easily create a
[41:50] triplaner a few ways we can do that we can either in the node graph type triplaner the advantage of
[41:56] this is that well it's fast enough to do but the disadvantage of course is that you will have to
[42:00] add the images to all the different planes which is annoying you know three planes as you can see
[42:05] a faster way to do this is to go up here in the image manager hold down a shift key and then drag
[42:12] this in here and I can see triplaner and now this has already been set up for you this is incredibly
[42:17] handy then we can just add this into our graph so we can just set this to be this should be on top
[42:24] so we do merge triplaner just make sure these are both selected and then we hit m key and then this
[42:31] triplaner is fantastic now we can change the scale of this as well so you can for instance go in here
[42:35] change the world scale to 0.1 something like that or 10 and then you can see that this indeed
[42:43] you can also go into each individual plane as well you can change this you can for instance go here
[42:47] change the repeat of this one just a bit faster here just holding it down like so and I can see
[42:52] that this one scales up and down you can change the angle of it as well so you have a lot of control
[42:56] with this and of course if something messes up you can hit the r for reset down here you can also
[43:01] change the fall off as well so if you want this to be sharper or softer you can change this so
[43:06] really really really handy you can also use different images for different planes as well so
[43:10] you can just drag them in here so you can have different ones for each one super handy so triplaners
[43:17] really really useful another node we can use is a tile node and you can get this up in the exact
[43:22] same way by hitting the tab key and doing tile and here you can see with tiled one comes and then
[43:28] we can double click this one and you can just drag this in here and then of course we can just
[43:32] replace this one here just make this go over and now you can see this just tiles this this of course
[43:37] is tiling it across meaning that we are going to get seams here this is often not really a huge
[43:44] issue because oftentimes the stuff from tiling doesn't really isn't really large-scale stuff like
[43:50] this is often really tight skin stuff so often you can't really see this but in this case you
[43:55] clearly can see this which is an issue another way to bring in a tiled is by holding down a control
[44:01] key when you're dragging so just dragging this in and I can see we get a tiled with this image
[44:05] is set up so very nice and easy you just hold the control key drag it down a little bit fiddly
[44:10] sometimes and there we go and now you can see we have a tiled in here so nice and handy so if we go
[44:16] into the tiled we can of course change the rotation of this as well so you can now you can just
[44:20] rotate this you can change the scale of this as well really handy of course in this case
[44:25] something that is annoying is that you do have to copy paste the scale so that because it doesn't lock
[44:32] so that is just a little heads up that you do have to just copy paste this in like so but you can
[44:37] also offset them as well like this so tiled super super useful you're going to be using this a lot
[44:43] the more you tiled though you can see the less of an issue this is but yeah still this is a bit of
[44:48] an issue a way to kind of fix this though is by using a tool called a paint through tool the


### Paint Through Tool (project images) [44:49]
**Transcript (timestamped):**
[44:55] paint through tool is one of the most useful tools in marie and allows you to project images on top
[45:02] of your textures so we can make a new paint node at the peaky make sure this is this should not be
[45:09] scalar data and this should be transparent then we plug it in here and then we are going to plug
[45:14] this into the merge like so and we just need to flip this around shift an x and here we can now very
[45:20] easily project an image so let's find the same image we had before which is this one right here
[45:27] then we can simply drag this into the interface and now you see that this automatically changes to
[45:32] the paint through tool if you don't have the paint through enable you can just hit the u key for
[45:37] instance if you are in a paint tool with the peak key you can hit the u key to go in here and now we
[45:41] can start to just paint over this the navigation for the paint through tool is control shift for scale
[45:50] and shift the left mouse button to pan and control and left mouse button to rotate around this
[45:56] becomes intuitive after just trying this a little for a little bit so now we can just very quickly
[46:01] just paint through this hit the r key to change the radius and now we can very quickly just paint
[46:06] over this this is a really legit workflow so this is how you often want to do it start off with
[46:12] a tile or triplanar and then you can go in and fix specific things or not even fixing things
[46:17] but if you want specific paint in specific spots you can't really do that with a triplanar let's say
[46:22] want this like and right here you can just do that then you can hit the peak key for paint tool just
[46:28] to hit just to hide the paint through tool and then you can hit the beaky and this is going to bake
[46:33] this down there we go so you can keep doing this you can go over the eyes here let's say you want
[46:38] some specific stuff in this area you very easily do this just go through here you can just paint
[46:42] this through just hit the beaky for a bake an incredibly handy tool which allows you to get
[46:48] highly specific images in in specific spots now what if you want to warp the images that you're
[46:55] projecting on top we can very easily do that as well so let's say we have a specific shape they
[47:01] want to get across we can use the paint through tool hit the u key let's say we have this you see
[47:06] this vertical part of the like in here we can just get this in what if we want to warp this we can
[47:11] very easily do this with a warp tool so to the left you have the warp tool so while this data is in
[47:17] the paint buffer just drag over the area and now you can simply just warp this select the part you
[47:24] want to move and you can just warp this around you can just do this and you can warp this now it's
[47:29] a little bit annoying having to actually select the dots themselves so what you can do you can be
[47:33] a little bit dirty with this you can just do a quick selection over them then you can hold on a
[47:37] control key and this is going to allow you to just move this around so control and left mouse button
[47:41] like so if you want more control you just go up here and you can just add additional vertices
[47:47] so we can just have a lot more fine control with this as well so the warp tool along with the
[47:53] paint through tool is incredibly useful now if you want even more control with this you can
[47:57] use a slurp tool as well and this is basically liquefy so this allows you to just go in here and
[48:02] just like really subtly move things like so so slurp along with the warp tool along with the
[48:09] paint through tool along with nodes is very powerful particularly if you combine this with tile to
[48:14] try planners as well hit the b-key to bake this down everything in marie revolves around the
[48:19] paint buffer there's no way to do this without the paint buffer so if you're painting now with the
[48:25] paint tool or you're painting with the painter tool it's all the paint buffer so now you can see
[48:30] we can get very specific textures in highly specific spots using this technique next up let's


### Hand Painting Textures [48:35]
**Transcript (timestamped):**
[48:36] talk a little bit about hand painting so we are going to be removing all of this stuff here just
[48:41] so we have a simple setup so we are going to be creating a color just so we have a base and then
[48:48] we are going to make a merge and we're just going to plug this in here and then we're going to make
[48:52] plug this in here and then we are going to simply make a paint on top of this then we just hit okay
[49:00] and then we can just paint in here so whatever we paint in here now it's just going to be well
[49:04] painted data we of course use the paint tool here for this and now you can see we can just paint
[49:09] whatever we want on top of this you can of course change the color of the background as well so if
[49:13] this is uh if this is some kind of crazy auger character you can just set this to be a bit of a
[49:18] base color and then you can start to just paint on top of this you can very easily change your
[49:23] radius just by holding down the r key or we can go up here i've never ever ever used this one here
[49:28] so i'd always use the r key and then we can just go in here we can just paint highly specific
[49:33] paint data where you want this to be if you want to change the color you can go up here and you can
[49:39] change the color here or you can hit the j key for color this is a really handy way of doing it
[49:45] now by default it's a little bit difficult to paint in marie and the reason for this is whenever
[49:51] you're painting you are going to be using the color picker a lot and in order for the color
[49:55] picker to really work we're going to have to do one change in the preferences edit preferences
[50:01] misc and then we go all the way to the bottom and then under toggle hold we have to enable tool on
[50:07] key held and make sure this is enabled if this is not enabled that means that the keys are not
[50:12] going to be sticky so for instance if you have a not a color here let's say you have blue and you
[50:17] want to blend between these two which is something you do all the time on hand painting you're going
[50:21] to have to switch to the color picker which has the hotkey c and then you switch to it and then
[50:27] you're going to have to hit the p key again and it's such an annoying workflow so by enabling the
[50:34] setting it allows you to just quickly hold down the c key and this becomes sticky so it's very
[50:41] easy to just go in and paint like so if you hit the k key you can see a ton of different brushes


### Using the custom shelf [50:43]
**Transcript (timestamped):**
[50:47] i've already put a lot of different things under custom brushes if you want to you can just take
[50:50] a screenshot of this and you can just find these ones these are all found within marie so you can
[50:54] go on a marie you can go under organic brushes and brad's new brushes and basic brushes and
[51:00] you can just use these ones yourself so some of these ones that are really handy is for instance
[51:04] dinoskin this one here is super handy this one is found under organic brushes right here and it's
[51:10] going to be right here so dinoskin super handy so now we can just very easily go in and just blend
[51:16] this stuff together and this is really only possible because we have the sticky key enabled
[51:21] if not this is such an annoying workflow so this is a really powerful way of working if you want to
[51:28] make your own custom shelf like this this is very simple we have the shelf icon right here we just
[51:34] can just dock this over or just pin this like this then you can find the brush you want not like this
[51:40] no sorry marie marie can be a little bit weird sometimes with the interface so you can just change
[51:45] this like so just move this down and if you want to have a specific brush in a specific spot you
[51:50] can for instance go under custom this is where you want everything to go you can go under organic
[51:54] and you can just move this in here so there we go you can now see that we have this right here so
[51:58] nice and simple so now you can just hit the k key to go in under custom and now you see we have the
[52:04] new hippo skin here so really nice and useful stuff so c key for color picker j key for color you can
[52:11] go in here you can change this to whatever you want to k for the shelves you can very easily
[52:17] let's go in and just add tons of variety to this now let's bake this beautiful painting down
[52:23] then now we have all our textures so what we have now is we have a very very a very ugly set of
[52:30] channels we have the color map and we have the specular roughness in this case we can just go
[52:34] in and we can just grade the spec r ever so slightly we can just make an hsv like this is not
[52:39] going to be anything beautiful we can just make an hsv and we can just change this to
[52:44] just make sure this goes in the center and we can just make sure this is just black and white
[52:47] we can just do whatever it doesn't really matter the point is that now we have two channels that
[52:53] actually have something in here we do have a third one we can just delete this one because we don't
[52:56] really need this one so we have two channels we have the color we have the specular roughness


### Exporting maps using Export Manager [52:59]
**Transcript (timestamped):**
[52:59] let's export these maps out we can do this by going up here in the export manager or right click
[53:06] file and export manager what we're seeing is that we have the color and the specular roughness if you
[53:11] want to change the name of these ones just change them in the channel itself and we can change the
[53:17] resolution of it so we can double click on it and now you can just overwrite this one if you
[53:21] change this to something else you can see it turns yellow which means that this is not the same as
[53:25] source and you can change the color space bit depth and the name itself you can also change the
[53:32] export path as well of course we'll have to change this to something else and this is where we have
[53:37] the object name as well we only have one object so we don't have to deal with this one at all
[53:42] on the bottom we can change the size for all of them so for instance if we want to let's say we're
[53:47] painting in 4k but we just want to do a quick look at the export for like 1k we can easily do that if
[53:53] you want to force linear we can do that if you want to force 8 bit we can do that we can also just
[53:59] go under here and just remove the overrides so this is nice and simple if you want to change the
[54:04] file format itself the logical part might be under file options but if you do that you see that you
[54:09] just have file options here just the compression options for the xr if you want to actually change
[54:14] the file format go under file name and just change this to something else it's going to change this
[54:20] to dot tga and now we have tga options you can also notice that we have dollar sign channel and
[54:25] dollar sign udem in this case it's going to get the name of the channel and it's going to get the
[54:31] udem number as well once you're done with your setup honestly most likely you aren't going to
[54:35] have to change a whole lot here then you simply hit export current export current is going to
[54:40] export from the current object if you have multiple objects this is going to export all it's going to
[54:46] export from all objects so it doesn't matter which one we use so if you hit one of these ones now
[54:51] this is going to export out our channels the last thing we are going to be covering in this tutorial


### Baking Maps using the Bakery [54:54]
**Transcript (timestamped):**
[54:56] is going to be the bakery you can find this by going to the top left right next to the export
[55:02] manager we have the bakery click on this nice little pizza oven and we have the bakery the first
[55:07] thing we want to do is we want to add a bake item we can do this by going under well add a bake item
[55:12] then we can add for instance an ambient pollution and we can click on that and we can add a curvature
[55:17] map and we can get both of these ones out we can change the name of the bake items we can change
[55:22] the size and bit depth and just by scrolling here we can also see the edge bleed as well then on the
[55:27] bottom we have bake to and bake from we can just make sure it bakes to the high poly from the high
[55:33] poly and then we can preview this so now it's going to be previewing the curvature and you can see
[55:38] the curvature here and you see the ambient occlusion here so you can for instance have multiple
[55:43] ambient occlusion so you can have one that's really sharp and go here so it's really sharp a o and
[55:48] then we can add another one which is really broad a o so we can just set this up like this so now
[55:52] this is just going to be nice and and broad so this is pretty cool you can go on a curvature and we
[55:59] can see that each one of these have different options as well so we can change this to convexity
[56:04] or curvature or concavity and we can change the multiplier which is basically how strong this is
[56:09] going to be and tons more options for that so this is a very powerful way of baking and on
[56:16] the bottom right we have three ways to bake this down so we can actually use the data we have a
[56:21] paint node geo channel and a channel paint node means that this is going to be baked down simply
[56:26] as a paint node right here this is pretty cool because this means that we have a straight up
[56:32] paint node that we can use another way to do it is as a geo channel which is similar to the mesh
[56:37] maps found in painter which means that they are going to be attached to the object itself and
[56:43] we have a channel which means it's going to just go straight here as a channel which means that you
[56:47] can also export this out we are going to be using geo channel at the moment so we can just bake these
[56:52] down and this is honestly pretty fast and there we go this only took a few seconds now we can
[56:57] close the bakery you can also take this message a geo channel is data that's attached to the object


### Geo Channels [57:00]
**Transcript (timestamped):**
[57:03] if you go to the object palette right here just bring this over right like this we can just dock
[57:09] this on the other side actually like so you can see here on the bottom we have geo channels so we
[57:14] have three now we have geo channel one and the inclusion and curvature there's not going to
[57:17] be anything in the first one but we do have something in these ones you can also bring in maps into
[57:22] the geo challenge if you bake them in other software like for instance displays maps from
[57:26] seabush or additional maps from painter but here is where you can find them under the objects geo
[57:32] channel properties and right here you can also import new ones by going under the eye now it's
[57:38] very simple to bring geo challenge into the node graph we simply hit the tab key type geo channels
[57:44] and here we go we can now make a merge just select merge first then geo channel hit the m key
[57:50] and preview this one i should preview the geo channel itself and under the geo channel we just
[57:57] select the ambient occlusion or we can select the curvature so in this case we can for instance set
[58:03] this to be a overlay so we can go to the blending mode normal contrast and we can set this to overlay
[58:10] and there we go or you can use this as a mask for instance to get a different effect you can also
[58:15] change this directly here to ambient occlusion and you can keep rebaking these ones so geo challenge
[58:20] really really powerful ways to get bake data into the node graph the advantage of geo challenge
[58:26] versus just paint nodes is that if you keep rebaking they're going to go into the same geo
[58:32] challenge as well so with geo challenge out of the way that is it for this introduction to marie if
[58:38] you want to learn more about marie i highly recommend our full introduction to marie that you can find
[58:43] on flipmomo.com with a link in the description if there's anything else you want to see in marie
[58:49] let us know in the comments we would love to hear your perspective on that and we would also love to
[58:54] hear if you've used the new bakery in marie seven is it as good as the one found in painter or
[59:00] does it need improvements we'd love to hear your opinion and yeah thank you so much for watching
[59:05] i really hope you enjoy marie it's a fantastic software that i enjoy a lot



---

## Captured Frames

- [2:02] tutorials/frames/introduction-to-mari-for-complete-beginners---1-hour-quick-start-guide/frame_000.jpg
- [10:55] tutorials/frames/introduction-to-mari-for-complete-beginners---1-hour-quick-start-guide/frame_001.jpg
- [11:40] tutorials/frames/introduction-to-mari-for-complete-beginners---1-hour-quick-start-guide/frame_002.jpg
- [16:16] tutorials/frames/introduction-to-mari-for-complete-beginners---1-hour-quick-start-guide/frame_003.jpg
- [16:55] tutorials/frames/introduction-to-mari-for-complete-beginners---1-hour-quick-start-guide/frame_004.jpg
- [20:50] tutorials/frames/introduction-to-mari-for-complete-beginners---1-hour-quick-start-guide/frame_005.jpg
- [26:50] tutorials/frames/introduction-to-mari-for-complete-beginners---1-hour-quick-start-guide/frame_006.jpg
- [29:30] tutorials/frames/introduction-to-mari-for-complete-beginners---1-hour-quick-start-guide/frame_007.jpg
- [30:30] tutorials/frames/introduction-to-mari-for-complete-beginners---1-hour-quick-start-guide/frame_008.jpg
- [41:12] tutorials/frames/introduction-to-mari-for-complete-beginners---1-hour-quick-start-guide/frame_009.jpg
- [44:20] tutorials/frames/introduction-to-mari-for-complete-beginners---1-hour-quick-start-guide/frame_010.jpg
- [47:50] tutorials/frames/introduction-to-mari-for-complete-beginners---1-hour-quick-start-guide/frame_011.jpg
- [51:10] tutorials/frames/introduction-to-mari-for-complete-beginners---1-hour-quick-start-guide/frame_012.jpg
- [57:30] tutorials/frames/introduction-to-mari-for-complete-beginners---1-hour-quick-start-guide/frame_013.jpg

---

## Structured Notes

### Core Technique
A ground-up "zero to functional" Mari onboarding (FlippedNormals, Henning) covering every mechanical fundamental needed before attempting real character texturing: project creation, interface/navigation, the paint-buffer concept unique to Mari, the node graph and its core nodes, symmetry/mirroring, organization tools, and the export/baking pipeline. Explicitly positioned as a fast on-ramp to the same node-based, reusable-mask philosophy taught in the companion advanced FlippedNormals video in this collection.

### Summary
**Project Setup [0:41]:** New Project dialog — pick a model, then a Channels tab where built-in shader presets (V-Ray, V-Ray 6, Unreal Metallic/Non-Metallic, Arnold Standard Surface, or a generic engine-agnostic one) auto-create the matching channel set (e.g. Diffuse Color + Specular Color + Specular Roughness) at a chosen resolution/color-space/bit-depth.

**Interface & Navigation [2:02-6:16, frame 003]:** fully dockable/rearrangeable panel layout (View → Default Layout to reset); orbit = Alt+LMB, pan = Alt+Shift+LMB, zoom = Alt+RMB-drag; **Preferences → Navigation → "Lock to World Up" must be enabled** or the camera drifts off-axis (Ctrl+R re-rolls the camera if it happens anyway); number keys 1-6 snap to orthographic side views, preferred over perspective because ortho projection is predictable/undistorted. Selection tool (S) has Object/Patch(UDIM)/Face modes plus a "Smart" mode that selects whole connected mesh- or UV-islands; H hides selection, Shift+H hides everything unselected, Ctrl+Shift+H reveals all.

**Objects & Versions [8:35]:** rather than adding new Objects for model iterations, add **Versions** of the same object (right-click → Add Version) — since Mari stores all painted data in textures (not on verts/curves like ZBrush/Painter), a version swap just re-points to a different mesh with the same UVs, letting you flip between high/low-poly or updated sculpts without losing any painting.

**Lights [10:44, frame 003]:** default lighting is uneven and must be fixed before painting — disable all lights except one, set its Fix-To to **Camera** (not Scene) so it always follows the view and never leaves permanently dark areas, position it frontal-and-slightly-above for soft shadow read, and match its intensity across F1 (flat)/F2 (shaded, no spec)/F3 (full spec) preview modes. An HDRI environment can be enabled for realistic reflections, important when developing a specular/roughness map "in the blind" otherwise.

**Paint Buffer [15:24-21:37, frame 004]:** Mari's defining, non-obvious concept — you never paint directly on the model; you paint onto a rectangular 2D "glass pane" (the paint buffer, shown with a resolution/bit-depth/paintable-state label) hovering in view space, which only gets projected onto the surface on **Bake (B)**. Key settings (Painting → Paint Buffer): disable "auto-reset on bake" (default is on and extremely disruptive — it silently resets buffer scale after every bake); set Bake Behavior to **Manual** so the buffer persists after baking (lets you reuse one projected image/pattern across multiple bakes) instead of auto-clearing; the period key toggles paint-buffer visibility without a full Ctrl+Shift+C clear; **Project → "Project On" must be set to All**, not "Selection Only," or painting silently stops working whenever an old selection lingers (a classic beginner "why can't I paint" trap). "Projection on front of object" (paint-through) lets a brush stroke pass through to the back/far side of geometry instead of just the visible front, essential for soft gradients on rounded forms like a nose — must be manually disabled afterward or normal painting starts leaking through unintended geometry.

**Node Graph fundamentals [21:37-29:44, frames 005-006]:** Tab to search/place nodes (same pattern as Nuke); node-properties panel count should be set to 1 to avoid a confusing long scroll of stacked properties; RMB pans, Alt+RMB zooms in the graph. Reading right-to-left: the shader node (e.g. Arnold Standard Surface) sits at the end and previews texture channels directly in its own settings; each exported **Channel** (color, specular roughness, bump, etc.) is what feeds the shader and what Export Manager pulls from. **Merge** (N) is the single most-used node — Base (bottom)/Over (top)/Mask three-port model, procedural masks (e.g. a Clouds generator node) or painted masks both work identically. View a node in the viewport by selecting it and pressing a number key (1-9, mirroring Nuke's input-preview system); Shift+S expands a collapsed node's ports for connecting alternate inputs. Flat/Shaded/Full preview modes (also usable on the graph output, not just the light rig) show a node's raw value vs. lit vs. fully shaded result. Ctrl+X is the preferred "delete" (cuts, doesn't just delete) since it's more ergonomic than reaching for Delete; Ctrl+Shift+X extracts a node from its connections without deleting it; hovering a wire while placing a new node auto-inserts it inline.

**Paint Nodes & Symmetry [29:44-34:12, frame 006]:** a Paint node has both a color input and a separate alpha/transparency input — for masking work, fill the whole model black first (Select-all → right-click Fill → Black) before painting so strokes read as a clean falloff instead of harsh alpha edges. Mirror painting: enable **Mirror Projection → Mirror X** in the paint-buffer settings for live symmetrical painting (only works well with truly symmetrical UVs), or paint one side and use right-click **Patches → Mirror → Left-to-Right/Right-to-Left** on a selected paint node to mirror after the fact purely within the UDIM tile (unrelated to character left/right — it mirrors within the tile's own space).

**Node organization [34:12-38:47, frames 007-008]:** **Teleport Broadcaster/Receiver** node pairs move data across the graph without a literal wire — name a broadcaster (e.g. "mask_teeth"), then any number of receivers elsewhere in the graph can pull that exact data, avoiding "spaghetti" in complex graphs; the recommended production pattern is painting a full mask library up front (ears/teeth/nose/eyes) via broadcasts, then working with receivers wherever needed. D disables a node for quick before/after comparison; N renames a node; J searches/selects nodes by name; Backdrops (Tab → "backdrop") group and color-code regions of the graph; L (or right-click Auto Place) auto-arranges a messy selection of nodes.

**Grading nodes [38:47-40:23]:** Grade (black/white point, lift/offset, gamma, gain/multiply) has no built-in mask port — to mask a Grade, extract it (Ctrl+Shift+X), rebuild the chain through an explicit Merge node instead, and mask that Merge. HSV adjusts hue/saturation/value directly; Invert is described as essential specifically for mask work (rarely useful on color directly).

**Image Manager, Triplanar & Tile nodes [40:23-44:49, frames 009-010]:** drag-and-drop images into the Image Manager (tick "scalar" for grayscale/mask-type images); **Triplanar** projects and blends a texture from three perpendicular world-space planes — seam-free regardless of UVs since it's driven by world scale, not UV space, adjustable per-plane (repeat, angle, blend falloff) with a shortcut of Shift-dragging an image from the Image Manager straight into the graph to auto-build a full Triplanar setup (vs. manually assigning all three plane images). **Tile** nodes repeat a single texture across UV space (Ctrl-drag from Image Manager for a quick setup) — faster to reason about than Triplanar but produces visible UV seams, generally acceptable for tight, high-frequency detail (skin pores) rather than large-scale patterns.

**Paint Through tool [44:49-48:35, frame 011]:** projects a reference image directly onto the paint buffer for spot-fixing/detailing after a Triplanar/Tile base pass — hotkey U (from the Paint tool P), navigation is Ctrl+Shift-drag to scale, Shift+LMB to pan, Ctrl+LMB to rotate the projected image; combined with the **Warp** tool (drag control points, Ctrl+LMB for quick free-move, add vertices for finer control) to distort the projected image to fit specific geometry, and the **Slurp** tool (a liquify/smudge) for subtler pushes — described as the standard production loop: broad Triplanar/Tile base, then Paint-Through + Warp + Slurp for hand-targeted fixes, all still ultimately committed via Bake (B) since everything in Mari routes through the paint buffer.

**Hand painting [48:35-50:43, frame 012]:** R-hold for brush radius, J for the color picker window, C for the eyedropper/color-picker tool — critically, **Preferences → Misc → Toggle Hold → "Tool on Key Held" must be enabled** or the color-picker hotkey (C) doesn't behave as a sticky momentary tool, making fluid color-blending painting (constantly re-sampling nearby colors) painfully slow. K opens the brush shelf; Mari ships many production-ready organic/character brushes (e.g. "Dino Skin" under Organic Brushes) that can be pinned into a **custom shelf** for one-click access.

**Export Manager & Bakery [52:59-57:00, frame 013]:** Export Manager (or File → Export Manager) lists every channel with resolution/color-space/bit-depth override controls (edited fields turn yellow to flag a deviation from source) and per-object export paths using `$channel`/`$udim` tokens; **Export Current** exports just the active object, the other option exports all objects. The **Bakery** (separate from Export Manager) bakes procedural mesh-based maps — Ambient Occlusion and Curvature are the two demoed, each independently configurable (e.g. a tight AO plus a separate broad AO, or Curvature switched between Convexity/Concavity modes with a strength multiplier), baking from/to a chosen mesh version, with edge-bleed control. Bake target options: **Paint node** (a standalone paintable node), **Geo Channel** (data attached to the object itself, survives re-baking into the same slot, analogous to Painter/ZBrush mesh maps), or **Channel** (a directly exportable channel) — Geo Channel is the recommended default since repeated re-bakes update in place rather than creating new nodes. Geo Channels are browsable per-object (Object palette → Geo Channels) and pulled into the graph via a `geo channels` node, typically Merged in Overlay blend mode or used as a mask.

### Key Steps
1. Create a project by picking a model and a shader-appropriate channel preset (Arnold/V-Ray/Unreal/generic) rather than building channels manually from scratch.
2. Fix the default lighting immediately (single light, Fix-To Camera, matched intensity across Flat/Shaded/Full preview) before doing any color/value judgment.
3. Internalize the paint-buffer model — painting always happens on a floating 2D buffer, committed to the mesh only on Bake — and disable the "auto-reset on bake" trap while setting Bake Behavior to Manual and Project-On to All.
4. Build every paint-driven mask through the same Color → Paint(mask) → Merge node pattern, keeping node-properties display count at 1 and organizing early with Backdrops/Teleport nodes rather than letting the graph sprawl.
5. Use Teleport Broadcaster/Receiver pairs for any mask or map reused in more than one place, instead of long literal wires across the graph.
6. Establish base texture variety fast with Triplanar (seamless, world-scale-driven) or Tile (UV-seam-prone but fine for tight detail) nodes sourced straight from the Image Manager, then refine specific areas with Paint-Through + Warp + Slurp.
7. Enable "Tool on Key Held" in Preferences before attempting real hand-painting, or the color-picker hotkey workflow is unworkably slow.
8. Use Versions (not new Objects) to swap in updated/higher-poly meshes without losing painted texture data, as long as UVs stay consistent.
9. Export finished channels via Export Manager (per-channel resolution/format overrides) and bake mesh-derived data (AO, Curvature) via the Bakery into Geo Channels for reusable, re-bakeable procedural masks inside the node graph.

### Nodes / Tools / Settings
Color, Paint (color+alpha inputs, "raw data"/transparent mode), Merge (Base/Over/Mask), Clouds (procedural mask generator), Grade (black/white point, lift, gamma, gain — no native mask port), HSV, Invert, Triplanar, Tile, Teleport Broadcaster / Teleport Receiver, Backdrop, Geo Channels node, Arnold Standard Surface (shader/material node with bump weight/mode), Selection tool (Object/Patch/Face/Smart modes), Warp tool, Slurp tool, Paint-Through tool, Image Manager, Export Manager, Bakery (Ambient Occlusion, Curvature/Convexity/Concavity bake items), Mirror Projection (Mirror X) and Patches → Mirror (Left-to-Right/Right-to-Left).

### Difficulty
Beginner (explicit "complete beginners" onboarding) — assumes zero prior Mari knowledge, covers only mechanical/interface fundamentals, and repeatedly defers deeper technique (character texturing, skin shading) to the creator's paid full course. Pairs directly with the companion Advanced Character Texturing in Mari video in this collection for the follow-on production workflow.

### Foundry App & Version
Mari (Bakery feature referenced as part of "Mari 7" in closing remarks). Non-commercial/learning use implied throughout.

### Tags
interface, hotkeys, paint-buffer, node-graph, merge-node, teleport-nodes, symmetry, triplanar, tile-nodes, paint-through, hand-painting, export-manager, bakery, geo-channels, beginner

---

## Related Tutorials
Shares the node-based Color+Paint+Merge mask pattern, Teleport Broadcaster/Receiver workflow, and Triplanar/Tile texture-variety techniques with Advanced Character Texturing in Mari: Studio Techniques (`advanced-character-texturing-in-mari-studio-techniques.md`) — that video applies these exact fundamentals (taught here from scratch) to a full production character, adding roughness-map theory, ZBrush integration, and high-frequency bump-channel projection on top.
