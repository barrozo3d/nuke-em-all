---
title: Intro to Nuke for 3D Artists - Full VFX Course
source: YouTube
url: https://www.youtube.com/watch?v=id1HCc2xkIU
author: Voxyde VFX
ingested: 2026-08-17
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/intro-to-nuke-for-3d-artists---full-vfx-course/
frame_count: 0
frame_status: pending-selection
---

# Intro to Nuke for 3D Artists - Full VFX Course

**Source:** [YouTube](https://www.youtube.com/watch?v=id1HCc2xkIU)
**Author:** Voxyde VFX
**Duration:** 253m40s | 19 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py intro-to-nuke-for-3d-artists---full-vfx-course <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey, this is Rez, I run Voxsite.com where we teach VFX through online courses, primarily focusing on Houdini and Nuke.
[0:06] I've been using Nuke professionally in my work for several years now, and it's been a crucial component in all of my projects.
[0:14] I truly believe that only through Nuke you can push your renders a step above and really unlock your potential as a 3D artist.
[0:22] Every compositor knows that some things are faster and easier to do in comp rather than in 3D,
[0:28] so with Nuke we not only have the power to dramatically change the renders, but we can also increase the speed of our final output
[0:35] by understanding where we can skip certain steps in 3D and do them directly in comp.
[0:41] And so learning and understanding compositing will really provide you with the best results in the long term.
[0:48] I've designed this course in a follow-along manner, so my recommendation will be to go through this course once,
[0:55] only by watching the lessons and then run the course again one more time and also follow along with the lessons.
[1:02] In the case for Nuke, there's really not so much technical understanding around it as let's say Houdini,
[1:09] so really the best way to learn Nuke will be by actually using it.
[1:13] All the renders and assets needed to follow along will be provided, so simply follow the link in the description of the lesson to download these renders.
[1:21] And with that being said, let's get started with Intro to Nuke for 3D Artists.


### Interface, navigation & Basics [1:30]
**Transcript (timestamped):**
[1:30] Before we get started on the actual project that we're gonna work on, we first have to cover a little bit of some Nuke basics like hotkeys and interface, navigation and so on.
[1:41] Just in case this is your first time using Nuke, I want to go over some of these settings real quick, so we are on the same page,
[1:48] but ideally we would like to jump into the main project as soon as possible and get our hands dirty, because really that's the best way to learn.
[1:55] With that being said, when it comes to the main project, what I will recommend is that you first watch a lesson, then re-watch the lesson while following along,
[2:05] and then finally try to recreate everything yourself to solidify the information and reference the course lessons only where you need.
[2:13] So with that in mind, let's go ahead and first we'll create a new comp over here, just so we start from scratch as I explain some of the basics.
[2:23] Now, first of all, we can see that as I open up Nuke, we are greeted with a different interface than what we had previously,
[2:30] and this is because I'm using a custom workspace that I created, so if we go over to Workspace over here, we can see we have a few options to choose from,
[2:40] and by default we will want to work in the compositing space, so if I select this one, now we're starting to get the interface that we actually need.
[2:49] So there are basically three main windows that we are interested in the most, which will be the node graph, so where we placed our nodes,
[2:58] for example, I can drop down a grid over here, we have our viewer where we preview everything we do,
[3:04] and then we have our properties tab over here on the right.
[3:07] When I select a node, all of the properties for that node will show up over here on the right.
[3:12] Now, you can see right away that what I have is a little bit different, and what I did essentially, it's the same windows, but I just swapped them around a little bit,
[3:23] so it's more comfortable for me. Essentially, I took the node graph and I placed it over here to the side, so I have the viewer in the middle.
[3:31] Also, the curve editor and the dope shit, these two windows are also pretty important.
[3:36] These have to do with keyframes, which we'll take a look into a little bit later.
[3:40] So I also dragged these ones over here as well with the node graph and the sequence we don't really need, so I just closed this one.
[3:48] And now I can just close this entire, I think this is called a pane, so I can close this pane,
[3:54] and I essentially have the workspace that I'm usually using.
[3:57] So I save this as a workspace over here called nodes.
[4:01] This is how I usually start my projects.
[4:03] I open up a new comp and then I select the nodes preset for the workspace and we're good to go.
[4:08] So again, we are in the node graph, we can drop down any node if we press step,
[4:13] so I can drop down a saturation node if I want.
[4:17] We can see the properties on the right.
[4:18] We can also choose nodes from over here from this window.
[4:22] So for example, we have them grouped per what we're trying to achieve.
[4:26] So if we are working with 3D nodes, we have a 3D node group over here.
[4:32] So I can select this, let's go to 3D Classic, I can drop down a light.
[4:36] So we have this over here, but 99% of cases I'm just gonna go Tab, select light,
[4:41] and then just drop this like so through the tab menu.
[4:44] So we have this on the left over here.
[4:47] Sometimes it's useful if you don't really remember the name of the node, you might want to go.
[4:51] For example, in the 3D, let's say that I want to drop down a cube,
[4:55] but in Nuke, it's called a box or whatever you can find the name, you can look for it in these
[5:02] groups. But again, most of the time, you're just gonna hit Tab and then just type the first few
[5:06] letters of the node that you want and you're going to drop it.
[5:10] So let's go ahead, get rid of these and let's drop down again a grid.
[5:14] And to preview a node, all we have to do is select the node and we can either hit any number from
[5:20] one to zero. So one, two, three, four, five, all the way up to zero on the keyboard.
[5:24] So if I select the grid and I press one, we can see the preview for this grid in our viewer.
[5:30] So this is how we can preview our results. And what's really cool about this, if for example,
[5:34] I drop down a ramp, I can preview the ramp with two, and then I can reference the grid again
[5:40] with one, we can see we have our one input connected over here to our viewer pointing to our grid.
[5:47] And our ramp is input two, so I can add another one I can do let's let's do whatever let's do
[5:53] a crop I can set this to three and then I can switch between these three using the number.
[5:58] So this is really cool. This is right away a huge advantage over After Effects. I've been in After
[6:05] Effects for over 10 years and and it was always annoying whenever you wanted to preview a change,
[6:11] you will you would have to go and select the layer toggle the visibility for that layer or toggle
[6:16] the visibility for the effect to preview it and without it was really annoying. I'm not sure
[6:22] the latest versions of After Effects maybe there's some sort of plugin or they finally
[6:27] implemented hotkeys for this but just being able to preview the notes like this is really,
[6:33] really, really helpful. We'll cover more about hotkeys as we go but basically this is how you
[6:39] will navigate through your scene. So for example, in our main project file over here, if I want to
[6:47] preview a certain layer that we're working on for example, this glow bounce layer, I can go ahead
[6:52] and I can go to the pre-mult result and press one to preview this or if I want to just preview
[6:58] the GI bounce or whatever I can just preview my layer and I can do any adjustments on it and I can
[7:05] like say for example, I want to add a grade. So I press the G to add a grade node and I can increase
[7:10] the gain here to adjust the values and now I can go to the end of my comp here to our final node and
[7:17] usually I like to preview this with five and I can always reference the final effect with five.
[7:23] You can obviously choose any number that you want but now I can go back with one and just isolate
[7:30] this layer and with five again, I will go back to my final result and I can adjust the grade and
[7:35] either look through the final result over here so I can lower this grade adjustment or I can just
[7:42] isolate this so I can see exactly what I'm doing and at any time I will press five and I can preview
[7:47] the result also in the final comp as well. Really, really helpful and this workflow is just something
[7:53] that you'll get used to the more you keep doing it so one all the way up to zero, you're going to
[7:58] preview any node that you want. We have our node graph viewer and properties and on the properties
[8:04] tab, the default here, we can see that there's a value of one here, the default here is 10,
[8:10] meaning that with this value set to 10, we can preview the properties for the last 10 selected
[8:16] nodes at the same time. So I have the properties for the crop node and now if I double click the
[8:22] ramp to select it, we can also see the ramp properties stacked on top of the crop node properties
[8:29] and as well if I select the grid now with double click, I can see the grid properties stacked up.
[8:34] So we can stack up all the way to 10 different nodes and we can clear these windows if I just
[8:40] close them but really my preferred way of working and maybe this is a Houdini thing, I usually want
[8:46] to preview the properties of just one node, the current node that I'm working on. So I set this
[8:53] property value here to one, meaning that if I select the crop, I just have the crop properties
[8:58] and then the ramp grid and so on. So I don't have them stacked. Sometimes you will need to see the
[9:03] properties of more than one node at the same time. So I might want to, if I set this to five, for
[9:10] example, I might want to reference some of the values from the grid into the values of the ramp.
[9:17] I might want to link them up with expressions. In this case, it will be useful to have both of
[9:23] them open at the same time but 90% of cases, I just want to work on one single node. So I will
[9:29] set this to one and this is all just to mention that you will probably have this value at 10
[9:33] and it's going to be entirely your call. How many nodes you want to see at the same time. Now,
[9:39] obviously, we have a bunch of buttons over here. We have our channels or rather our layers and to
[9:45] the left we have our channels. We'll look into these as we go. And one final thing before we get
[9:51] started is going to be the project setting steps. So if I go in the node graph window over here and
[9:56] I click on an empty space to deselect any node and I press S, we can go to the properties tab over
[10:02] here. And really important is going to be the name and the project directory. I don't usually
[10:07] use this even though I should. So if you set a name and a project directory over here, you will
[10:12] be able to reference the paths with an expression. I think it's brute dot folder or something like
[10:19] that. But don't really worry about this too much for now. What's going to be really important is
[10:24] going to be setting the frame range. So in our case for the project we're going to work on,
[10:28] our renders go from 1001. And so this will be the start frame and our end frame will be 1240.
[10:37] FPS will be 24. Again, this depends on the render, but usually it's either going to be 24 or 30.
[10:45] And for the size format, this will be really important as well to set this to the correct
[10:49] format right from the start. For example, if I leave this at the format that it currently has,
[10:55] which is this 2k, super 35, whatever format, if I drop down a radial, we can see this is
[11:02] nicely in the center of our comp. And if for example, I deselect the radial, I press S to
[11:08] go back to the project settings and I switch the format over here, let's do, let's do maybe
[11:13] something way different like 8k, we can see now that the radial is no longer in the center of
[11:19] our screen, it's going to maintain the bounds it originally had, we can see if we draw an imaginary
[11:26] rectangle over here that was that original 2k format that we had, it's going to be in the center
[11:33] of this. So it's it got displaced when our format changed. And this will be the same for a lot of
[11:39] different nodes. So it happened to me a few times where I was working in a lower size format, for
[11:46] example, I was working on some proxy renders, which were 960 by 540. And I was using that format.
[11:53] And then when I switched to the high quality renders and I switched to the HD 1080 format,
[12:00] all of my radials and my masks and rotos got displaced, and I had to manually readjust them.
[12:05] So it's really important that you work with the correct format right from the start. And again,
[12:10] now that I have this HD 1080, which is the format that we need for our render, so we can keep this
[12:17] format. Now, we can see that this original radial that I dropped again is not centered,
[12:22] but if I drop down a new radial, it's going to be nicely in the center of our screen. So this
[12:27] will be about the format. And finally, we can talk about the color as well. The default color
[12:33] management here, I believe maybe it's set to nuke. But for our renders, which are rendered in aces,
[12:41] we have to set the color management here to OCI O, and you should have in the OCI O config, you
[12:47] should have an aces option over here. And then here we can select aces 1.2. And then this will
[12:53] set all of our other settings to their correct inputs. And we are pretty much good to go. These
[12:59] will be the project settings that we need. And these are some of the basics. And really, a lot of
[13:04] this stuff will make more sense as we go. And with the next lessons, we can start working on our
[13:10] project. So I'm going to go ahead and delete all of these notes. We have all of the project settings
[13:14] that we need. I will let's go ahead and save this. So I'll press Ctrl S, you can give this any name
[13:19] that you want, hit save. And with the next lesson, we can bring in our renders and start working.
[13:24] The best way to learn Houdini and Nuke is through project based courses. All of our courses on Voxside
[13:30] are based on real world projects created for various clients like Riot Games, Puma and many
[13:36] more. So if you want to see how Houdini and Nuke is used in production, you can check out the courses
[13:41] on Voxside.com. So we are ready to start. Let's go ahead and bring in some renders. So to start any


### Read, Merge & Simple Comp [13:45]
**Transcript (timestamped):**
[13:50] kind of composition, we'll have to read in our files. And while I'm in the Node Graph window,
[13:56] we can press R to... So this is essentially, we can also hit Tab and place down a read node like
[14:04] this. So I will select read from here, press Enter. And then this will prompt a window for us, where
[14:10] we can select our file. So I'll go up and here are essentially the folders with containing all of
[14:16] the renders that you've been provided with in the downloads. And if I click in any of these folders,
[14:22] let's start with the HeroEnvironment01. I'll click this folder here, we can see that we have a sequence.
[14:29] So notice where it says here, so it says intro Nuke 02, HeroEnvironment01. And then a bunch of
[14:36] hashtags. These hashtags will represent the actual frame that we are going to read. So if we were to
[14:42] look at this folder in our file explorer, this looks something like this. So it's a bunch of
[14:48] files here, each corresponding for each individual frame. So you will be more than used to this. If
[14:53] you've ever created a render sequence from a 3D application, you will most likely know that the
[14:58] preferred way of working is by rendering out and exporting each individual frame, rather than exporting
[15:04] an entire sequence with all of the frames packed into like .mov file or something like that. You
[15:11] will definitely work with image sequences. And in this case, it's going to be an EXR sequence. We're
[15:16] going to talk more about EXRs in a second. And also to note here is that if I just want to import
[15:22] one single frame, I don't want to bring this in as a sequence, we have an option over here. So if I
[15:27] disable sequences, then we can bring in just an individual frame. But usually you will want to
[15:32] bring in the entire sequence. So I can double click to read in our sequence. And then we can see
[15:39] our read node over here. It has a nice thumbnail of our render. And if I connect this to our viewer
[15:44] by pressing one, we can now see this in the viewer here. And I can go to the beginning of the timeline.
[15:49] I can press play. Now we can see that this is our current render. You will also notice here,
[15:55] as our animation plays, we are loading up this orange bar here at the bottom. This orange bar
[16:03] essentially means that we are storing the results, we are caching the results on our drive. And now
[16:10] we are playing this back in real time. But for example, if we had later when we have a lot more
[16:15] nodes, this will start to slow down a little bit. So the caching portion essentially. But once this
[16:22] timeline is cached out, so we have this full orange bar, then we are going to be able to preview in
[16:28] real time our results. I can also zoom in on this timeline if I hold right click, and I drag it over
[16:37] a region. Now when I release right click, we are going to zoom in on our selected frames. And now
[16:43] when I plan the animation, it's going to loop only that specific region. So if I just want to work on
[16:49] an isolated part of the render, then I can do this. And to go back to the full range that we set in
[16:54] our project settings, we can just right click on the timeline, and it will select the entire range.
[16:59] On the node for timeline and caching, if I press spacebar, we can zoom in on our render or rather
[17:08] the window. So if I do spacebar again, and I'm hovering over the node graph, we can also zoom
[17:14] in on our node graph as well. And this will work with any window. But specifically, this is useful
[17:20] for the viewer. So if I press spacebar here, we can zoom in on our render, and we can look closer
[17:25] and inspect our results. And now you might have noticed that our cached timeline disappeared. And
[17:32] only, and only this region is now cached out. And this happens when you are zooming either in or
[17:38] out, we can see that as I zoom back out, we get our cached timeline back. But when I zoom in,
[17:45] so maybe if I zoom in even further, we no longer have this. And this is because Nuke will cache by
[17:51] default at the at sort of the level of zoom that we have. So if I press spacebar again, and we can
[17:58] also press F to frame in on our render like so, or we can press H, and it will try to fit with the
[18:04] bounds of the window. But generally, I like to use F. So for example, here, we are a little bit
[18:10] zoomed out of our render, and Nuke will try to cache at this size. And this is why when we zoom in,
[18:16] we lose some of that cache, because essentially, now we are sort of at a higher resolution. But
[18:22] if we want to have consistent caching, we can turn on this option here where it says full frame
[18:27] processing. And by the way, we can see that as I hover over any of these icons, we have a nice
[18:33] tooltip which tells us exactly what the buttons do. So this is very, very helpful. We can pretty
[18:38] much hover over any property in any node, and we can get a quick description of what that property
[18:45] does. So this is really, really handy. But now essentially, if I turn on full frame processing,
[18:50] this means that now Nuke will always render at the highest quality. So now if I do a cache,
[18:57] let's maybe just zoom in on a smaller region over here, I'll press play so I can catch this,
[19:02] we can see that no matter at what level I zoom in, the cache will remain. So this is very helpful.
[19:08] I don't really have this setting turned on by default, maybe at a later stage. In the project,
[19:15] I will turn this on. But still, it's a very important option to note. So we have our environment
[19:20] render. And let's right away start to have a little bit of fun and start actually compositing.
[19:27] Let's say that I want to add a background to this city. So I will just simply drop down a ramp. And
[19:34] this isn't what we're gonna do for the final project, but this is just to demonstrate. Let's
[19:38] preview the ramp again by pressing one, this will hook it up to our viewer. I will grab our handles
[19:44] here. So depending on what kind of node you're using, you might have some handles in the viewer.
[19:49] In this case, for the ramp, we can decide where our ramp will be by adjusting these two points. So
[19:56] let's maybe undo this and I will grab the point at the bottom here, I will hold down shift and I
[20:01] will drag it up at the top. So we have this bottom to top white to black gradient like so. And now
[20:09] I want to place this behind our environment render. So we have our render over here and we have our
[20:16] ramp to the right. So I can set the ramp maybe to two on my keyboard. So I can cycle between these.
[20:22] So the way we now combine these renders is I can drop down a merge with M. I will also, if you do
[20:30] tab, you can also drop a merge from here. But since you will be using this merge all the time,
[20:35] it's really worth memorizing the shortcut for this, which is M. We see this merge expects
[20:41] two inputs. And what we want to do in this case is going to be what's called an A over B operation,
[20:47] where A is our foreground layer and B is our background layer. So this is how I like to
[20:53] remember which input is what we can think of the B layer over here that stands for background. It's
[21:01] not really the technical definition, but this is just how I like to remember the order of layers.
[21:07] So our background in this case is going to be our ramp and our foreground is going to be the
[21:12] environment. And now if I preview the result of this merge with one, we can see our ramp behind
[21:18] our city. So we can also preview this animation now and everything seems to work. Now the reason
[21:23] this works, if we look in our environment render, the reason this operation worked is because this
[21:30] layer has an alpha channel. So if I select this layer, and while previewing this layer, I press A
[21:37] over our viewer, we can see this black and white mask that determines what parts of our render will
[21:44] be seen and what parts will be transparent. So our black part is essentially what's going to be
[21:51] replaced by our B layer. Let's say that the ramp in this case is going to be our sky. So wherever
[21:57] we have black, it's going to be the sky. And then the white is going to be our render. So this is
[22:02] how this merge operation knows how to combine these two layers to obtain the result that we are
[22:07] after. And there are many different operations in merge by default, when you drop down a merge
[22:13] node, it's going to come with this over operation. But here we can see that we really have a lot of
[22:19] different operations. So we're gonna go over some of these a little bit more in depth later. And also
[22:26] if you hover over this property over here, we can also see the math behind how these are calculated.
[22:33] And if you look in this list, you can find over more towards the end here, we can see that it's A
[22:40] plus B and in parentheses one minus small case A. Now, don't worry about this for now. A lot of
[22:47] these operations really are going to be done intuitively. So after you get used to compositing
[22:54] in new, a lot of this will just be second nature and you'll know which operations you'll want without
[23:01] really knowing the math behind them. So really, if I were to tell you without looking at this list,
[23:07] how the out operation works, for example, I wouldn't be able to tell you the math, but I know what to
[23:12] expect from it when I use it. So that's what I mean by instinctively. And this is also why I would
[23:18] encourage you to just get your hands dirty as soon as possible and try some of these operations out
[23:23] yourself. There's also a cool property here in this merge node with the mixed value. So let's get rid
[23:29] of this one and go back to our merge operation here. We can also determine how much strength we want
[23:35] from our A layer in this case. So if I were to set this to a lower value, we can see how we start to
[23:42] get more of our ramp and less of our geometries. And this mix property will be present on a lot of
[23:48] nodes as well. So if I drop down a grade node with G, we also have this mix node. And speaking of grade,
[23:54] let's go ahead and again, the shortcut for the grade node is G. And this is also one of the most
[24:00] common nodes you are going to use. So it's worth knowing this shortcut. If I were to drop now a
[24:05] grade after our ramp and before our merge, I can go ahead and gain this down so I can darken our
[24:12] sky. And I can stack multiple grade nodes, I can do another grade node with G. And let's say that I
[24:18] want to make the sky more blue. I will go again to the gain node, we can also affect the gamma in
[24:24] this case. But for the gain node, let's click on this color wheels. So we have access to the
[24:29] individual channels. And I will just bump up the blue channel and maybe decrease the red channel. So
[24:35] now our sky is blue. And again, maybe if this is too blue, I want to bring back more of my
[24:42] original ramp, I could use this mix value. Sometimes I do this, I will, I will just lower this mix
[24:49] value, which essentially determines the strength of this grade node over here. So I can just lower
[24:54] this, maybe I want 50% of this grade node to affect our render. So I will just set the mix value here
[25:00] to 0.5. So sometimes it's pretty useful. So let's bring in our character as well. I'll press R again,
[25:08] I'll go up, let's bring in our hero character, I will double click on our render, and we can
[25:14] preview this with one. And with this layer selected, I will press M. And this will automatically
[25:20] connect it to our merge node as the foreground layer. So now our background layer in this case,
[25:27] I want it to be both our sky and our city render. So I will point this B layer to our other merge.
[25:35] And now slowly we are starting to build our comp. And now, for example, I can grab this character
[25:44] layer over here, I will press G. I might want to darken this for whatever reason, let's drop down
[25:49] the gain. And for our environment render as well, let's go ahead, do another grade with G. Let's
[25:57] maybe gain this down as well, we can lower the gamma. And this right here, what we've done so far
[26:04] is a very, very basic comp. But this is essentially the workflow from here, it's just a matter of
[26:12] adding more stuff and creating our own layers that we will merge in with the rest of our composition.
[26:20] But this is really the general workflow. And in my case, and what makes sense to me with any kind
[26:25] of comp is to work from the furthest element back to the element that's closest to the camera, so
[26:33] that's in front. So in this case, we have our sky, this is this will be our furthest element
[26:39] away from the camera. Then on top of that, we have our environment. And on top of this, we add our
[26:45] character. And now we have, like I've shown you earlier, we have complete control over each
[26:51] individual layer. Now with the next lesson, we'll go more in depth about how we can get the ultimate
[26:56] control with render passes. But this essentially is a very basic composition. So I would like you
[27:01] to try this out yourself with just these two nodes for now, or rather three nodes, including the read
[27:07] notes. So get familiar with the read node, and especially the merge and the grade node, try out
[27:14] to build this very basic composition. And with the next lesson, we'll take a look into how we can
[27:19] get even more control and start to take a deeper dive into compositing. So earlier, we've mentioned


### Render passes & EXRs [27:25]
**Transcript (timestamped):**
[27:26] that our sequence is an exr sequence, as we can see here dot exr. And there's basically two big
[27:33] distinctions when it comes to exr as opposed to other image formats like JPEG or PNGs. So first
[27:40] of all, with exr, we can store from the render pixel values that are over one. So if we look at our
[27:48] character render, we can see that some of the different parts of the character will have
[27:54] different values. So for example, if I look at the sword, the specularity will have pixel values
[28:00] that go over one, we can check our pixel information over here at the bottom. As I hover over this
[28:06] sword over here, I can even sample a region if I hold down control and shift and draw a rectangle,
[28:13] we can see that the average for this region is going to be this 4.9 value on all of our channels,
[28:21] so RGB channels. And then over here, we have normal values, so under one, 0.39, and so on. But
[28:29] the important thing to note here is storing this value that is over one, because if I drop down a
[28:35] grade node, and I gain this down, we can also check this little, let's maybe get rid of this
[28:41] grade node, and we can also use our gain and gamma sliders over here in the viewer. So the difference
[28:48] here is that when we do this, we can see that we can gain our image down when we do this in the
[28:53] viewer, this isn't really applying it to our render, and we can always just get it back if we click
[29:00] where it says this f divided by 20 property over here to reset it to the defaults. So these sliders
[29:07] here are really just to troubleshoot for different areas without having to add a gain node and
[29:13] actually affecting the comp. We can just inspect our renders here, and then we can reset them by
[29:19] clicking on this f thing here and this white thing for the gamma. So as we gain this down, we can see
[29:25] that we actually preserve some of the detail in the texture, and maybe this is more noticeable here.
[29:30] So if I reset this, this area over here, let's go ahead and sample this. So this is roughly 6.6,
[29:37] and if we were to gain this down, we can see that we will preserve all of this detail that's in the
[29:42] texture. So all of the scratches and all this nice detail. So a JPEG is different in this sense.
[29:50] JPEG has all of the values clamped to one. So for example, I could drop down a clamp and let's
[29:57] connect this to our render. So when we preview this, already we can see something different.
[30:02] All of these pixel values now can't go really above one. And if I were to do a gray node or
[30:08] actually change the f stop here, when I gain this down, we can see we have this flat color. So we
[30:14] no longer have any of our details. So this is how a JPEG would work. And this is why these values
[30:20] that go above one is important. So when we go back to our actual render, we can see that we can see
[30:25] a huge difference between this. So this is one of the reasons why EXRs are powerful. And the other
[30:33] even more powerful reason is the ability to store different render passes. So most of you
[30:39] watching this are probably familiar with Houdini. This is a Houdini channel primarily. So I will
[30:45] just step over in Houdini real quick to show you how I set up the render passes. So if I do a quick
[30:52] test render here in the viewport, we'll go to our camera. This is actually what we've exported in
[30:58] the render. And over here, we have this is the karma render settings now. So this is Solaris.
[31:03] And by the way, if you're unfamiliar with Houdini, definitely check out voxside.com,
[31:07] where we have a lot of free beginner classes for Houdini. So but to keep things short and relevant
[31:14] to what we need here in this tab, we have AOVs. So you will either hear the term AOV or render pass.
[31:22] And this essentially means that we can split up the render in each different contribution.
[31:28] So we can have the specularity different from the reflections different from the diffuse passes
[31:35] and so forth. And for example, here is where we can choose what AOVs we are exporting. So diffuse
[31:42] reflections and refractions. In this case, we don't have any refractions. We can choose lights and
[31:47] emissions if we had volume so we can render different effects separately. SSS stands for
[31:52] sub surface scattering. So if we had a character with skin, usually skin shaders have this SSS
[31:59] property. But in our case, we we don't have this. Again, this is just to demonstrate. And then we
[32:04] have a lot of utility layers we have we can export the position in world space. So this is stored
[32:10] again per pixel, everything is stored per pixel. But if I go to this image planes over here, we can
[32:17] check out the individual render passes that we have or render AOVs. And also when we export the
[32:24] render from Houdini as an EXR and bring it over in yoke, for example, our character render and also
[32:29] our environment render will both have the same AOVs. And we can check them if we go where we
[32:35] says here RGBA, we can actually check our render passes so we can go to the combined diffuse,
[32:41] we can we also have this separated by lights. So we have a distant light and a sky and a sun.
[32:48] So we can separate the contribution from the distant light as we can see here. And again,
[32:54] it's useful to use these sliders here at the top to gain up and some of these passes might come out
[33:01] really dark. So when you want to check if you did there's something there, you can just use these
[33:06] adjust these sliders here. So we'll have our combined diffuse sky sun, we have all of the
[33:14] contributions. So this combined glossy reflection, for example, is going to be all of the contributions
[33:19] for all of the lights put together, but we are going to separate them per light. So we have
[33:24] the distant one, let's maybe reset this. So we have the sky and the sun. So having access to all of
[33:30] these layers, when we separate them and put them back together, we are going to come with what's
[33:36] called the beauty, which is the render that contains all of the information, essentially,
[33:42] the RGBA in this case. And one quick note about this RGBA here, we can see that we can also preview
[33:49] just the RGB. And when we have the selected to RGB, and I press a over my viewport, I can see the
[33:56] alpha channel, only if I set this to RGBA. So when I have this RGBA here, if I press a, we can see
[34:03] the alpha channel. So it happened a few times where I would want to preview the alpha channel for a
[34:08] layer, and it wouldn't show me the alpha layer. And this is because this was set to RGB. So make
[34:13] sure that whenever you want to go back to the beauty or the default, you set this to RGBA, we
[34:18] can also see that we can just preview the alpha. But this isn't really useful because we have the
[34:23] alpha information here by pressing a on the viewport. So when we bring in an EXR, like we have
[34:29] in this case, by default, it will show us the beauty. And in order to be able to individually
[34:36] affect all of the different render AOVs, we have to split them all up, and then put them back together.
[34:44] And this splitting and putting back together of the AOVs is what's called recreating the beauty.
[34:50] So this will be our next step here, we can maybe start with the environment. I'm going to just go
[34:56] ahead and let's control C and I will control V to paste this hero environment render over here
[35:03] and start a new comp maybe on the right. So earlier, when I've shown you how we can preview the
[35:09] individual render passes through our viewer here, this isn't really splitting up our beauty. This is
[35:16] really just allowing us to preview the respective render AOV. So if we want to export this render,
[35:24] we would still export the RGBA, which is this right here. So what we need to do is split up
[35:29] each individual layer. And it would be kind of intuitive if we had a node that says something
[35:35] like split AOV. But in this case, to split up the renders, we need a shuffle node. So let's go ahead
[35:41] and press step and drop down a shuffle. And with the environment render selected, this will
[35:46] automatically append it. And we can see that this is by default placed in the B input. And now here
[35:52] to the right, we have our options. So by default, we can see that our input layer, which is our B
[36:00] layer. And this is just the default configuration, we can also shuffle in layers from a different
[36:06] render. But in this case, what we want is to shuffle one of our existing layers from this
[36:12] environment render into the RGBA layer. So really, all of this is to say that over here,
[36:17] we can just select the AOV that we want to expose. And let's say that we want to start with the combined
[36:24] diffuse layer. So we can either choose the combined diffuse without any underscore. But like I said,
[36:30] we would want to separate this per individual light. So we can start with the combined diffuse
[36:35] distant. And we can see now that all of the individual channels, the RGB of the combined
[36:40] diffuse layer are going to be shuffled inside the RGB channels in the output layer. So from this
[36:47] shuffle now, this becomes our new RGB for this shuffle. And now we can do stuff with it, we can
[36:54] add a gray node, we can gain this up. And we can either press M to do a merge and we can merge this
[37:00] on top of our original render. And if I set this operation to plus, we can go ahead and let's
[37:07] increase the gain here and maybe the gamma, we can see that we are adding another layer of our
[37:13] combined diffuse render pass on top of our beauty. This doesn't really make any sense. But
[37:19] the point is that after we do the shuffle, we can now start using this combined diffuse
[37:24] distant pass that we selected over here. So let's go ahead and get rid of this merge for now. And
[37:29] really what we have to do now, we can also get rid of the grade. So with the shuffle node, what we
[37:35] need to do is shuffle out all of the individual different render passes to recreate the beauty.
[37:42] And for example, if I want to duplicate this node, I can select this node, press Alt C. So Alt C
[37:48] will duplicate and I can point this back to our render and this new shuffle, let's go ahead and
[37:53] let's choose our combined diffuse emission. In this case, if we preview this, we can see that
[37:59] there isn't really anything here. So it happens occasionally, especially if we separate the lights
[38:05] per individual contribution that some of these layers my comma in empty. And let's just go to
[38:11] the next one, which will be our combined diffuse sky. So we can see that we do have some information
[38:16] over here. Let's go ahead and reset. And we can do let's do one more for now. Let's do Alt C to
[38:21] duplicate the node point is back to our render. And let's do our final combined diffuse, which
[38:27] will be the sun contribution. So we can preview this. And now if I go cycle through all of this,
[38:33] we can see each individual contribution for the combined diffuse split up per its respective
[38:38] light. And now we can essentially start merging these. So I will select the first shuffle, I will
[38:44] press M, I can merge this with my second shuffle. And from this merge, I can drop down another merge
[38:50] and I can combine this with our third shop. And I will set this operation here to plus. And I will
[38:56] set also our second merge to plus. And now if we take a look at the result, this will be our
[39:02] combined diffuse. And I can start grading and doing stuff per individual past. So I can add a gray node
[39:09] and let's go to our shuffle. This will be our sky contribution. So if I preview the result from our
[39:16] last merge and go to this gray node, that's affecting the sky, I can set the gain to let's
[39:21] maybe go to zero. So now I don't have any contribution from the skylight. And hopefully you can see
[39:26] where I'm going with this. Now something I like doing with the shuffle nodes, we can go to the
[39:31] node tab, we can see we have a tab for shuffle over here. And most nodes will also have this
[39:37] node tab over here where we can give this a label. So in the shuffle node, we can see that this is
[39:42] the combined diffuse distance. So we can go to the label here and we can specify ourselves what we
[39:48] are shuffling in. So this will be our let's do diffuse distance. And now we will see this over
[39:55] here in our node graph. So we know which shuffle is which. But another thing that you can also do
[40:01] is we can grab the name that we shuffle in. So we can grab this input name here, if we do an
[40:08] expression or rather a syntax, so we can do open brackets, and we can type value. And we want to
[40:15] read this from the in one parameter. So here we'll do in one, and we'll close brackets. So now this
[40:21] will give me the name over here combined diffuse distance. And for example, if we select this
[40:27] one and change this to a different one, facing ratio, we can see now that this says facing ratio.
[40:32] So I will undo this, let's bring back our combined diffuse. And we can go ahead and copy this value
[40:38] in one syntax over here to our other shuffles as well. Let's copy this to our third one. So we
[40:45] can easily differentiate between these between all of these shuffles. Now we can organize these
[40:51] layers a little bit because we still have to bring in a lot of other render passes as well. So we
[40:56] don't really want to have a messy organization here. So what we can do if I hold down control,
[41:03] we can see that this now creates a dot at the center of each individual wire. And I can click
[41:10] while holding control to add a dot and I can rewire all of my nodes like this. So for example,
[41:16] now I can add another dot over here with control and I can maybe rewire my nodes like this. And
[41:22] this is how I like to organize my beauty recreation setup. I think this is the most intuitive way at
[41:28] least for me. So I know all of these merge operations need to be plus I can maybe add another
[41:34] dot over here so we can see how easily we can start to organize things. If I just want to add a dot
[41:40] anywhere in this space, I can press period on the keyboard and we can see that this drops down a
[41:46] dot and we can connect this anywhere. And we'll talk a little bit more about wire management as
[41:52] we start to add more nodes. So let's also get rid of this gray node for now. And let's bring in the
[41:58] rest of our AOVs. So we'll go ahead from here and bring in our remaining passes. And what I like to
[42:05] do is we can just grab a bunch of these nodes together and I can press I'll see to duplicate all
[42:11] of them. Then I will connect these two copies up. And so we are on our fourth shuffle now. Let's go
[42:18] ahead and we can bring in the combined glossy reflection. And again, this is separated for
[42:25] the lights as well. So we are interested in the distant light, the sky and the sun. So we'll grab
[42:31] the distant one and for our next one, let's go ahead and we'll grab our sky. So again, this is the
[42:39] combined glossy reflection. Previously, we had the combined diffuse. So we'll bring in the reflection
[42:45] sky and we'll do one more. I'm going to grab a bunch of nodes and press I'll see to duplicate.
[42:50] Let's hook up our sixth shuffle and we'll shuffle in our reflection sky. So if we look at these as
[42:58] well, they look like this. So when we now add all of these together, I'm previewing the final result
[43:04] of our final merge node over here. If we compare it with our original render, I'll press two on
[43:11] the render. So now we can see I'm switching between this merge over here at the end and our render.
[43:16] So we can compare these two. And we have almost the same result, something's missing over here.
[43:23] We can see if we check this first combined diffuse shuffle over here, we can see that the wires are
[43:29] actually disconnected. So if we want to connect all of these wires up, so the RGB, we can just
[43:35] click drag on the input layer and drag it over the output layer. And now we have our pass back
[43:41] and we can check our other ones as well. All of these are connected. So now if we preview again,
[43:47] the final result from the merge and our original render, we can see we have the exact same result.
[43:53] Now one thing I also like to do here is reverse the order of this merge operation. So currently,
[43:59] the first input is a and the second input is B and we can press Shift X with the node selected to
[44:05] reverse the order. And this works with merge, but also works with other nodes as well. So it's a very
[44:10] useful shortcut to know. And the reason I want this B layer to be the first one and the A layer
[44:17] to be the second one, if I look at this merge result and press D, so D is another very important
[44:24] hotkey which we can use to disable layer. So for example, if on this merge, I disable it,
[44:30] we see only the B layer. And then when I press D again to enable it, we have the contribution
[44:36] of our second shuffle. So I will press Shift X on all of our merge nodes over here. So it's going
[44:42] B to A. And now for example, if I go to the beginning, let's maybe preview the result from our
[44:48] last merge node and I would disable all of our merge nodes with D. Now I can enable them one by
[44:55] one and see exactly how everything adds up, create our final beauty. And this is very useful sometimes
[45:02] to troubleshoot things. Sometimes you don't know the contribution of a certain layer, so you can
[45:07] really troubleshoot easily if you just disable the layer. So now I can see that this reflection
[45:12] distant light over here is contributing to this part of our render. So this is really the setup
[45:18] for the beauty recreation. Now, how do we know that all of these passes have to be added together? So
[45:24] how do we know that this merge should be a plus operation and not something else? This has to do
[45:30] with the specific render engine that you're using. So this is the way it works with karma from Houdini.
[45:37] But this would be pretty similar with other render engines as well. So in the past, I've used Redshift
[45:42] and most of the operations in Redshift are also a plus operation. For Redshift, for example, you
[45:49] can check out the documentation. And if we look, we can see here on the AOV documentation that the
[45:56] beauty, if I zoom in here, beauty equals and here we have all of the different passes and
[46:02] how they should be put together. So we see that we plus the diffuse lighting with the global
[46:07] illumination with the specular, everything is a plus. And then after you plus everything together,
[46:12] you multiply it by a volume thing. So again, all of these are just render AOVs or render passes,
[46:19] you multiply all of these with the volume thing. And then on top of that, you add the volume emission
[46:25] and volume lighting. Now, in our case, we don't actually have volumes in our render, but it would
[46:31] be the same pretty much for karma as well. If you don't want to over complicate things in the beginning,
[46:39] just remember that most of these render passes should be plus together. So then finally, we have
[46:45] our beauty recreation setup here and I can go, for example, to the reflection distant pass over
[46:53] here, drop a grade with G and I can gain this down so I can remove this if I don't want to.
[46:59] We can add another grade here for the sky contribution and we can see how overall we're
[47:05] removing some of this reflection, maybe we have too much reflection from the sun,
[47:10] I can gain this down, maybe I want to bring in more contribution from the sky on the combined
[47:16] diffuse layer here and I can bump this up and we can see already if I look at the final result and
[47:22] I like to preview my final result with five. So I will set this to five and with one, I can inspect
[47:27] the current node that I want to. So if I preview now our initial render with our comm version,
[47:34] we can already see a difference. So this is how we can start working with passes and this is why
[47:39] EXRs are super powerful. Now, we're barely just scratching the surface of what's possible with
[47:46] passes and we'll look into more examples as we go. But this is essentially a very basic beauty
[47:53] recreation setup. I'll grab all of these grade nodes and get rid of them. So you might want to
[47:58] get used to the setup because you'll be doing this a lot in CG compositing. Now, before we actually
[48:04] start adjusting all of these passes and great stuff, there's one more crucial step that we have to
[48:10] take into account and we can look at this with the next lesson. Now, unfortunately, we can't just


### Unpremult & Premult [48:13]
**Transcript (timestamped):**
[48:15] start grading right away. There's still one more step that we have to do first. And this has to do
[48:21] with un-premultiplying the layer. So what do I mean by this? Let's maybe just first go to our
[48:26] original example. So here we have the ramp, that's the background. And on top of this, we bring over
[48:33] our environment. And for example, if I were to add a gray node here, and I want to do, let's maybe
[48:40] gain this up. So we are not really getting that problem yet. But if I were to do some more extreme
[48:47] grading, so if I were to also start reducing the gamma, now we will start to see this very subtle
[48:53] dark edge around our building here. And this is what we want to avoid. So the reason that this is
[48:59] happening is because of anti aliasing. And really, the more extreme our grading becomes, the more
[49:07] noticeable this dark edge becomes. So this is really not what we want. And if we look at our render,
[49:14] we can see that this edge here around our building, this very subtle ramp is what's causing this
[49:21] problem to happen. So by default, all of the render engines will have this sort of anti aliasing in
[49:26] order to allow smooth edges so that everything blends a little bit better together. And if we
[49:32] look at alpha information, essentially, what's happening is we are having the RGB pixel values
[49:38] multiplied by this alpha value. So we can see here this very subtle gradient over a few pixels from
[49:46] a full value of one to a value of zero. And when we switch over, so if I press A again, this translates
[49:52] over to the edges as well. So when we do our grading, and we multiply these values, we can see if I
[49:59] compare the original render with the grade version, we can see essentially, we kind of lose one row of
[50:06] pixels if we compare these two values, we had some color information here on this pixel. And when we
[50:12] do our grading, we lose that information. So what we have to do is somehow get rid of this
[50:18] anti aliased effect. And we want our RGB values to sort of ignore this gradient created by the alpha.
[50:26] And this is what the unpremultiplication will do for us. So for this read node, I will drop down an
[50:32] unpremult node. Let's go ahead and drop this down. We can see now with this unpremult, we sort of
[50:38] flatten out this gradient, it's kind of working like an edge extent. And really what's happening,
[50:44] we can see this over here, it's dividing the RGB values by the alpha values. And as a result,
[50:50] we get rid of our anti aliasing. And now when we do our grading, we can see that between these two
[50:57] results, we no longer lose any row of pixels. Now, the problem here is that when we look at our merge,
[51:04] we obviously get a problem where our building is now extended. So if I were to disable both the
[51:11] unpremult and the grade, we can see that our building is a lot thicker. So obviously, we don't
[51:16] want this, we want to bring back the smoothness of the anti aliasing that our alpha provided. So
[51:23] after the gray node, what we can do is pre malt, right? So this will do the reverse of what the
[51:29] unpremult does. So when we add our pre malt, now we will get our edges back. And as a result,
[51:35] we can see we have that very thin, smooth ramp on our edges. So if I were to grab the unpremult
[51:42] and the pre malt with shift, we can disable both of these layers. And we can see now that
[51:47] this is the original result that we had with that annoying black edge around the around the building.
[51:54] And if I enable this, we get rid of it. And we are sort of safe to do our grading. However, we want
[52:01] without worrying about having that nasty black edge problem occurring. So really what's happening,
[52:07] this unpremult and pre malt is it's just a simple divide and multiply operation. If I were to,
[52:13] let's maybe grab our render and I'm just going to shuffle real quick. Let's grab the alpha,
[52:19] which is essentially what's happening. So if I hold down and drag a wire from the alpha and hold
[52:25] down alt, we can connect the alpha to all of our RGB layers. So now we have this black and white
[52:32] image across all of our RG and B channels as well. So now if I add a merge node and I were to divide
[52:39] this, let's set operation here to divide and let's reverse the order with shift x. So when you are
[52:45] doing divide or a minus operation, the order here matters. But when you are doing a plus or a multiply
[52:52] operation, the nodes can be in any order, but it doesn't matter when you are doing divided minus. So
[52:58] we can see now that with this divide operation, we get the exact same result that our unpremult
[53:04] does. So this is really all it does. And then to get our edges back, we can drop down another merge,
[53:11] and we will want to multiply this with our shuffle with this black and white image with the values
[53:16] that we want. And then we can set this to multiply and we get our edges back. And in between, we can
[53:22] do our grading, we can do our safe grading without worrying about this ruining our edges.
[53:28] So really, this is all the unpremult and premultiplication will do. Every time you have a layer,
[53:34] whether it's a render or footage with transparency, anything that has an alpha, you will need to do
[53:41] this unpremult and premult business. So it's really important that you are aware of this. This can
[53:46] really ruin renders, especially when you are separating a lot of passes over here, you can
[53:51] imagine that adding up all of these pixel values together, you can really mess up the edges of
[53:58] a render. Sometimes you don't have to do this. For example, if this, maybe if this environment
[54:04] render was exported with the sky as well. So now we have the alpha transparency, because we
[54:11] don't have any sky. But if this were exported with sky, and this and this alpha information was a
[54:18] completely one color across the entire image, then you probably wouldn't have to do this. But
[54:24] in this case, since we do have to replace the sky and we have to add this environment render on top
[54:29] of another layer, then we do need this unpremult and premultiplication thing to do the proper
[54:35] grading. Now, when we are splitting up the renders, we will need to unpremultiply all of these
[54:43] different AOVs in order to do the proper grading. But the problem here is, for example, if I were to
[54:49] drop an unpremult over the combined diffuse distance shuffle over here, we can see that this
[54:55] isn't working. I can gain this up a little bit. We can see that this unpremult really does nothing
[55:01] for this layer. And this is because by default here in the combined diffuse channel, we are just
[55:06] bringing in the RGB channels from this combined diffuse distance pass and outputting them only
[55:13] to the RGB channel. So if I press A over this shuffle, we don't have any alpha information. So
[55:19] we also need to bring in for each shuffle our alpha information from the original render. So
[55:27] we can do this directly in this shuffle node, we have another layer over here, we can grab the alpha,
[55:33] so we'll grab the alpha. And this B layer is looking at our read node over here, which has
[55:39] our main render. So if I grab the alpha from this render and plug this in our output of this shuffle,
[55:47] now if I press A, we see we bring in the alpha. And if I go back to the unpremult and let's zoom
[55:54] in here and I enable this, now we can see that our combined diffuse distance pass is unpremulted and
[56:00] we can do our grading. So we can drop down a grade from here, let's reset the gain of your over
[56:07] here. So I can gain this up, I can do whatever adjustment and then I can do a pre-mult to get
[56:13] back our edges. Now, another thing to note here when you are splitting up the AOVs and doing this
[56:19] unpremultiplication thing, you do want the unpremult to affect each individual pass, but you
[56:25] don't want to do the pre-multiplication after each individual pass because what happens is when we add
[56:33] our layers together, the pixel values change. So when we do this plus operation, our edges will
[56:40] change and when we add another pass on top, our edges will change again. So what we want to do is
[56:45] do just one pre-multiplication at the end of all of our added shuffles. So I will get rid of this
[56:53] pre-multiplication now and we want to do the pre-multiplication after our last merge node. So from
[57:00] over here, we want to do a pre-mult. The problem what happens here again is that when we add all
[57:07] of these different shuffles together, our alpha, our final alpha from over here will change. So if
[57:14] I press A, we do have the alpha because we are bringing it over from our first shuffle. So we
[57:21] do have the correct alpha in this case, but if this second shuffle, we also will have to bring
[57:27] in the alpha as well. So we'll connect this here and we'll do a non-premult so we can prepare this
[57:32] for grading. So now, for example, if we look at the result, we have added both of these alphas
[57:38] together. So we essentially multiply the alpha by two. And if we compare this with our original
[57:43] render, we can see that the alphas aren't matching. So what we need to do is after we merge all of these
[57:49] shuffles together, all of our AOVs together, we need to bring in the original alpha from our main
[57:55] render. And we can do this with a copy node. So we can drop down a copy node. And also the hot key
[58:01] for this will be K on your keyboard. So this will bring up a copy node. Let's go ahead and we want
[58:07] to copy from A to B. And we can see that by default, we can copy different channels, but by default,
[58:13] this will copy the alpha to alpha. And we can see this over here. So we can also maybe copy
[58:19] other channels to other channels. But in 90% of cases, this is really used to copy the alpha.
[58:25] We want to copy the alpha from our main render. And I will point this over at this dot over here.
[58:32] And let's maybe add another new dot. So if we follow the chain here for this A layer in the
[58:37] cop, we can see that this will point all the way back to our original render. So we'll grab the
[58:42] alpha from the render. And we want to copy it. This B layer should be our merged result. So from
[58:49] our main render to our final result here from the merge, if we look at this result now, we get the
[58:55] alpha that we need. And now we can do our pre-mult after we get the alpha. And if I press A, now
[59:02] we have our anti aliased edges back, we have that smooth fade over our edges. And we are free to do
[59:10] any grading adjustments that we want, we can gain this up, for example. And also very important,
[59:15] now that we have the proper alpha after this copy node, we can also, for example, let's go ahead and
[59:22] grab this ramp that we created earlier, I will press LC to duplicate all of these nodes. So this is
[59:28] just our placeholder for the sky. But now that we have the proper alpha, we can drop down a merge
[59:35] and we can merge our render on top. Of course, this has to be a over B, we want our background to
[59:41] be the sky. So I just reverse the nodes with shift text, add another dot over here preview the final
[59:48] result. And we can check to see if we get any weird issues on our edges. And in this case, we do
[59:53] because we have to un-premult all of these other shuffles as well. This is why we get this black edge
[60:00] still. Now, we can either shuffle in the alpha individually for all of these other layers as
[60:07] well and then un-premult them. But we can also just run an un-premult over all of them at the same
[60:13] time. So let's go ahead and drop down another un-premult node, we will connect this here before
[60:20] we do our shuffle. And by default, this will work only or on the RGB channels. But we can set this
[60:26] to work on all of the layers. So now if I set this to all, we can check and we can see now that our
[60:33] combined diffuse all of our passes are un-premulted and we got rid of all the anti aliased edges and
[60:40] now essentially from our shuffle notes, we no longer need to bring in our alpha. I'll set this back
[60:47] to the first version that we had. So the default version and let's go ahead and get rid of the
[60:52] alpha connection and we no longer need to do our un-premult for each individual shuffles. Now,
[60:57] sometimes I like to do, usually I like to do un-premult per individual AOV, just because on
[61:04] the rare occasion, I might not want some of the layers to be un-premulted. But to keep things
[61:09] simple, let's just run an un-premult application over all of these. So now finally, if I go at the
[61:15] end, let's set this back to RGBA. Now we can finally do our grading. So we can adjust all of these
[61:23] and we will not have any problems with our edges. We can bump up the sun and we can do some crazy
[61:30] stuff and we can see that we have the correct smoothness over our edges. And this is now the
[61:36] final piece of the puzzle. Let's go ahead and get rid of the grade notes. So we un-premult all of the
[61:42] shuffles, then we add them together. After we add them together, we copy back the original alpha from
[61:48] our render and then we run a pre-mult. And this is pretty much what you will have to do every time
[61:54] with renders. Now another problem that's happening when we run the un-premult operation over all of
[62:00] the channels, we have some utility layers over here. So for example, the position pass and maybe
[62:06] the normal pass as well, these layers, we might not want them to be un-premultiplied. We want to
[62:12] run them over the regular version without this pre-multiplication. So it will be more important
[62:18] down the line when we want to bring in these other layers that we do a shuffle and we point
[62:24] them back to our original render without the pre-multiplication. So it's important that we don't
[62:30] connect the shuffle to our un-premult. So it's just something that you have to be aware of.
[62:34] And this is why sometimes I like to run an un-premult over each individual shuffle,
[62:39] just so I know exactly what's happening and it's easier to keep track of the un-premult and
[62:45] pre-mult stuff this way. But again, to keep things simple, we are just going to use this method where
[62:51] we un-premult all of them at the same time. And now with the next lesson, we can start grading
[62:56] and adjusting this environment a little bit. We could go ahead and let's start grading our


### Simple Comp [63:00]
**Transcript (timestamped):**
[63:03] environment. And we can just simply start and look at each individual layer. So for example,
[63:09] we can go to our diffuse distant light here and I can gain this up. I can either preview the results
[63:16] from all the way over here. Maybe for now, I will just let's disconnect our ramp over here. We are
[63:22] going to replace this with an actual sky in a moment. But let's go ahead and we can grade this
[63:27] up or down. We can affect the contributions for each individual light. So I can start to really
[63:34] experiment. Now, what I'm doing here is not really the proper way of working. You would have to adjust
[63:41] the lighting directly in 3D for the best results because when we are adjusting this light in nuke,
[63:48] we are kind of faking a lot of stuff. So really, when we are lowering the diffuse contribution
[63:54] from the skylight, this would affect the reflection as well. So these would kind of go hand in hand
[64:00] the reflections and the global illumination and all that stuff. And ideally, you would get to as
[64:06] close as possible to the result that you are after directly in render. And I've chosen this render
[64:12] specifically to showcase more of an extreme example of how effective compositing can be. But
[64:19] ideally, you would want to make a lot of these adjustments directly in render. Now, sometimes
[64:25] what I do is I get a very crude estimation of what I believe the final result should be. So when
[64:33] I'm looking at and experimenting, I might just throw a render like this with just some of the
[64:39] lights that I know I need. So an HDRI, a sunlight, a directional light, and so on. And I will just
[64:45] fine tune them like this directly inside of nuke, because really, it's just faster to work like
[64:52] this. So we can see how easy this is. We don't have to really worry about anything 3D. So all of
[64:58] these changes I'm doing here are a lot faster than if we were to do them in 3D. So I can do some R&D
[65:05] and experiment with different with different kind of looks. And then I can go back in 3D and readjust
[65:11] my lights to match what I came up with in nuke. Now, this kind of workflow is really only possible
[65:16] when you are doing both the 3D and the compositing. And 100% it's not something that's usually done
[65:22] in productions. So usually, you kind of want subtle changes only in compositing, you want to
[65:29] nail the result as much as possible directly in 3D. But again, when I work for myself and to
[65:34] showcase the power of compositing, I've chosen this extreme example. So we are going to do some
[65:39] very dramatic changes. Let's move forward now to our combined glossy reflection sky. We can also
[65:46] maybe lower this. I kind of like this reflection sky pass. I'll leave this rather unaltered. And
[65:52] let's add another gray node for our sun. And probably I will want to gain this down. I also
[65:58] want to get rid of a lot of this yellow tint that the most of these sun layers will have. So for our
[66:06] combined glossy reflection sun, I can drop down a saturation and I will just reduce the saturation.
[66:13] Probably I want to get rid of the yellows entirely. And so for the sun, I will set the saturation to
[66:19] zero. If we go to our sky, I might want to keep some of this blue color that we are getting from
[66:26] the sky. And let's go to our distant light as well. This should be okay. This doesn't have any color.
[66:32] This is just a simple black and white layer. And let's move forward to our combined diffuse sun.
[66:37] Now really, we should ideally use all of our passes to recreate the beauty. But in some cases,
[66:45] you might not need some of these layers at all. So it happens often that I bypass some layers
[66:52] entirely. So for example, so for example, maybe I don't really need this distant light, we'll
[66:59] keep all of them for now because we don't really know what we want until we add more layers on top.
[67:05] And really, let's for now just try to normalize the intensity and just try to flatten the colors
[67:12] a little bit. So we'll go to our sky, we might want to bump this up. Let's go to our reflection
[67:19] distant. And here I will drop this down quite a bit. Let's let's also look at our individual passes.
[67:26] So again, with five, I will preview the end result. So number five is hooked up to this
[67:32] and the merge node over here. So we'll go back to our sun shuffle here. Again, we will drop down a
[67:38] saturation and let's set this to zero. And with this grade node, let's preview the final result.
[67:43] And I can maybe lower this overall and for our sky combined diffuse sky, but this should be fine.
[67:51] And finally, I might want to lower this as well. We can also maybe for this layer, let's preview
[67:56] the final result. Let's increase the gamma so we don't have this super sharp contrast for our
[68:02] distant light hitting the buildings here. And now we can lower this. So mainly here I'm looking for
[68:09] luminance values. And this is just more of a personal thing, but I like to treat luminance
[68:15] values different from the color values. So in general, if you nail down the luminance, so
[68:22] sort of the intensity of the colors in your comp, it will look pretty good regardless of what colors
[68:30] you are using. So if the value of the color itself is good, then it will look good with any color,
[68:38] regardless if this is blue or yellow or whatever other color, of course, we are still going to
[68:44] go for something pretty specific. But this is just to explain that what I'm trying to do right now
[68:50] is try to get the luminance values right. Now it's also pretty hard to tell exactly what we need,
[68:57] because we still need to add our character and in between the character and the actual environment,
[69:03] we will bring in more elements and we'll create our own layers. So I won't spend that much time
[69:10] tweaking the values right now and just trying to get in the ballpark. And then we'll add all of our
[69:15] other elements and then we'll come back and readjust all of the values for our gray nodes and our
[69:20] saturation. And in this way, we will work non-destructively. And this is really the power of
[69:26] compositing and working in Nuke that you can still come back to your very first layer and do some
[69:31] changes regardless of how many layers we are going to stack later below our first nodes over here.
[69:39] At this point, we can also bring in our character as well. Now, like I said, between the character
[69:45] and our environment, we have to add a lot of layers. But let's just go ahead and also recreate a simple
[69:52] beauty recreation just so we are used to this idea. And then with the next lesson, we can start working
[69:58] on our layers that are in between. So for now, I will just go ahead and I will copy this node.
[70:03] And again, you can just press R and you can read in the character render from over here. So you
[70:08] can open it up. But in this case, I can just copy this because we already had this imported. So
[70:14] here is our character render. So again, we can just drop down a merge node from here and this
[70:20] can go so this will be the foreground now. And our background will be this merged result here.
[70:25] And we can see our character on top of our environment. And for this character, we can copy
[70:31] this exact same setup. If we look at this render, we will find and here this really should have been
[70:37] set to RGBA. So we can also preview the alpha channel. So remember what I mentioned earlier,
[70:43] sometimes when you inspect these layers, you want to go back to RGBA and you select RGB as a mistake
[70:50] and then you will no longer be able to preview the alpha channel. So that's a common mistake that
[70:55] might happen. And here we can see again that we will have all of our combined diffuse layers
[71:00] split by the same lights. And and usually when you have a couple of objects that you want to
[71:06] render separately in a scene, you will want to render them in the same lighting conditions and
[71:12] export the same AOVs for them. But this is what usually happens now in reality, sometimes you
[71:19] might not have this luxury and you will have different lighting setups and also different AOVs
[71:24] in which case your job as a compositor will be a little bit harder. But just to keep things simple
[71:30] for the sake of this course, I'm using the exact same lighting setup for both of these renders and
[71:35] the same AOVs, meaning that now, for example, I will disconnect our render for now, I can grab
[71:41] this entire setup with our unpremote all of our shuffles and even all of our grading and I will
[71:48] just copy and paste this over here. And now I can link up my render to this unpremote. And
[71:55] essentially this will now do all of our operations that we did for our environment. These will now
[72:01] apply to our character. And let's also over here preview the RGB or again, I selected RGB, but we
[72:08] should have selected RGB so right so we also have the alpha and now we can merge this on top of our
[72:14] environment render. And if we preview the final result, this is what we have, we can check our
[72:19] edges and see that everything matches, we don't have any weird black edges, our unpremotivation was
[72:26] correct. And also we transferred all of our let's call this initial grading. So we've covered
[72:34] really a lot of steps so far with just these techniques that we've covered so far, we can
[72:39] really push the renders pretty far so we can see that if I were to look at my original result over
[72:45] here, let's maybe get rid of our grade nodes and just keep our essentially our just our environment
[72:51] and our character. So if we look at this result and we look at our new result, we can already see
[72:57] a huge difference. And now we can come and for example, for the character, let's say that I want
[73:02] to highlight more of the distant light, I can go here and I can increase the grade here, maybe
[73:09] reduce the gamma so I can push the color on this side of the character if I want. So we can treat
[73:15] them a little bit differently. And now for example, if we want the character to pop out a little bit
[73:20] more, we can increase the contrast of the character with the background and we'll look a little bit
[73:25] more into this later when we start to add more layers. But this right here is the very essence of
[73:32] CG compositing this AOV splitting and then grading them per individual AOV putting everything back
[73:40] together and then going back and readjusting different layers. And like I said, we are working
[73:46] non destructively, meaning that at any point I can come back to our environment and I can
[73:51] bump this up if I want to in isolation of the character. And this is also something that's
[73:56] really hard to do. I mean, it's not really hard to do in CG. But for example, if I were to affect
[74:03] the light in my 3d scene, I would also bump the light for my character as well, unless I specifically
[74:09] tell the light to ignore certain objects in our scene. But obviously, this is a lot more handy.
[74:14] And it's just quicker to do look depth. So I really prefer a lot of time to just do a lot of this
[74:20] lighting directly inside of Nuke. And like I mentioned, after I figure out what my light setup
[74:26] should be, I can come back in 3d and actually do them over there. If there's time, of course.
[74:31] So this is how we can use the AOVs when it comes to recreating the beauty person and affecting
[74:36] each individual layer. But really, I'm just scratching the surface with AOVs. There's a lot
[74:42] of stuff that we can do. We can use some of the utility passes like the position and the
[74:47] normals to isolate certain parts of the renders. So in that sense, we can create our, we can create
[74:53] new layers and new masks from these layers. And that's really when we unlock the power of compositing.
[75:00] So with the next lesson, we can take a look at how we can use some of these utility layers. So I
[75:06] will see you there. So we have all of the AOVs that contribute to recreating the beauty, which are


### Utility Layers [75:07]
**Transcript (timestamped):**
[75:13] these combined diffuse and reflection. So the diffuse reflection, GI, all of these, everything
[75:20] that you use to recreate the beauty are essentially the layers that we need to rebuild the beauty.
[75:25] But then we can export a few extra layers that don't directly contribute to rebuilding the beauty,
[75:32] but are still essential in CG compositing. And I just want to give you an example in this lesson
[75:38] with one of these utility layers. So you don't have to follow along. This won't really be part of
[75:44] the main project, so to say. But let's go ahead and let's just copy one of these shuffle notes.
[75:49] And I'm just going to paste this over here. And the reason that I'm copying the shuffle
[75:52] notes is because we have this value in one expression setup for us. So if I were to connect
[75:57] this back to our render, let's go ahead and one of these utility layers will be the normal
[76:02] pass. So we can grab the normal and I will link all of the X, Y and Z values here to our RG and B
[76:09] channels. And we can simply do this by dragging over the input inside output. And we can see
[76:14] that this will make the connections for us. And right away, this is a weird looking pass. You might
[76:21] imagine that there's no way that we can use this in our comp. So if I were to just simply add this
[76:26] on our comp, it would make no sense. But what this normal pass is, we output the normal vector values
[76:34] as RGB value. So we can see here, if I were to isolate this part here, if I were to draw a sample
[76:41] region, we have negative point zero one on our red channel, roughly one on our green channel. And
[76:48] then again, roughly zero on our blue channels. So we can imagine that the RGB channels in this case
[76:55] are going to be our X, Y and Z values for this specific pixel. So if I step over in Houdini real
[77:03] quick, this is our 3d scene. So we can take a look at our normals. And if we were to look closer,
[77:10] let's say that this vector over here, we can look at our coordinate system over here. And we can see
[77:17] that for the most part, this specific vector is mostly facing the Z direction. So this would mean
[77:23] that it has a value closer to one on the Z axis, and then zero on the X and roughly zero on the Y,
[77:32] meaning that in 3d, it will have a vector value of 00 and one on X, Y and Z. And this means that in
[77:39] New York, this will have if we think of RGB values instead, this will have a 00 and one value on RGB.
[77:47] So it will have zero on the red, zero on the green and one on the blue. So it will be mostly blue.
[77:53] And this is in fact what we see over here, if we were to go to our building, we can see that this
[77:58] is mostly blue. And this is because this region of the geometry is mostly pointing in the Z direction.
[78:05] And for our ground, for example, this is mostly pointing upwards. So this will be mostly green,
[78:11] which is a 01 and zero value in terms of RGB. So red, green, blue, green will have a value of one.
[78:19] And this is why it's mostly green. Now, this is super helpful for us. We can do a lot with this
[78:25] normal AOV, but this is mainly used to real light scenes. And we can create special kind of masks
[78:33] with this layer. Now we can create masks with any of the other layers as well with the world
[78:38] position pass as well and the depth and the depth AOV and we'll take a look into this later. But
[78:43] specifically for our normal channel, if for example, I want to isolate the part of our geometry,
[78:49] this facing upwards, so this is mostly going to be our ground, we can let's first disconnect
[78:55] all of our values. So I just want to grab the Y coordinate, I want to isolate the parts that
[79:00] are pointing upwards, and I will place this Y channel in our alpha channel. So usually when
[79:07] you want to create a mask, you will be working with the alpha as an output. And I'll show you
[79:13] Y in a second. But now if I were to press A, we can see that this is how our alpha channel looks
[79:20] right now. So we have isolated this region of our geometry. So now if I want, we can go to one of our
[79:27] combined, let's look for one of these shuffles here, we can go to our combined diffuse sun. And
[79:35] if I were to drop down a grade node, we can see that all of these color correction nodes and a lot
[79:40] of these nodes will have an arrow to the right. And if I drag this over, we can see that it starts
[79:46] to say that this is used for masks. So we can point this arrow to our shuffle. And now with this
[79:54] gray node pointing the mask to the shuffle, if I turn up the gain, we can see that we are just
[80:00] affecting that part of our mask that we selected from our normal pass. And maybe we can make this
[80:07] even more obvious. So we can see that we are just affecting the part of the geometry, essentially,
[80:11] that's pointing upwards. So by default, the mask will look for our alpha channel. So here we can
[80:17] see we can turn on our mask. So so if I were to not use any masks, we can see that our grade will
[80:24] affect all of our render. And when we turn on the mask and the mask is turned on by default,
[80:28] we will look for the alpha channel of our input over here. And this is why I mentioned earlier
[80:33] that usually when you are creating a mask, you will work with the alpha channel. So now if I
[80:38] wanted to, I could go back to our shuffle here, I will press a, and I can append a gray node,
[80:45] I can further control this region that we selected over here. Now the grade node by default will work
[80:51] on the RGB channels. So in this case, we just want to operate over the alpha. So let's select the
[80:56] channels here to alpha. And if I squeeze in the gamma, if I lower the gamma, we can further isolate
[81:02] this region here, we can play around with the gain as well if we want. But in this case, since this
[81:08] is a mask, really our values shouldn't go over one. So I would be a little bit more careful
[81:14] with the gain value here. But with this extra gray node on our alpha channel, which we get from our
[81:20] normal, if we go back to our grade over here, we have further refine our area, our mask selection.
[81:28] So if I were to disable and enable this, we can see that how easily we can just bump up
[81:33] the surface of our ground, for example. And we can see that this affects some of these surfaces
[81:39] over here as well. Now we can get rid of these surfaces if we want by implementing even more
[81:46] utility layers to isolate certain parts. But this is just to give you an example of how we can use
[81:52] the utility layer. So this is one example when we where we are using it as a mask. And again,
[81:57] this isn't really what we are going to use in our final project. I'm just showing you this to
[82:03] demonstrate the power of utility nodes. So again, a utility node is something that doesn't contribute
[82:08] directly to recreating the beauty, but you can use it to create sort of kind of a mask, and you
[82:14] can use them to map different kinds of textures. And we'll see this in a second. And we can also
[82:19] use it to create new layers, which we will do in the next lesson. So with the next lesson,
[82:25] let's go ahead and get rid of this great node and the shuffle. So with the next lesson,
[82:30] we'll take a look in how we can create a new layer with the utility passes. So I will see you there.


### Fog layer [82:36]
**Transcript (timestamped):**
[82:36] Let's see how we can use the depth layer to create a new fog layer that we can place between our
[82:42] character and the environment. So let's go ahead and we might make some room over here with our
[82:48] character shuffle dovies. So I'm just going to drag this entire setup down below. And we can start
[82:54] by grabbing one of our shuffle layers. And I will just copy one of these nodes and paste them down
[83:00] below. Again, we will want to grab one of these shuffles with our value in one expression here.
[83:06] And we'll need to point this shuffle back to our render. And we want to point this
[83:10] to our original render before our unpremult node. And I'll explain why in a second. But
[83:17] essentially, we want to bring in some layers that aren't affected by our primal now. So the
[83:23] layer that we will need will be this depth no AA, we have two versions of our depth layer.
[83:30] Let's first maybe look at our depth extra. And now here we have something new, we just have one
[83:36] input here. So essentially, this depth layer is exporting just a float value. This depth layer
[83:43] essentially represents each individual pixel stores a value based on how far or close it is
[83:50] to our camera. So we want to we don't want to create a mask. So if we wanted to create a mask
[83:56] using this layer, we will just plug this in our alpha and use the alpha as a mask. But in this
[84:01] case, we want to create a new layer that we can plus on top of our render. So in this case, I will
[84:07] hold down alt while dragging this wire and connect this to all of our output layers. In this case,
[84:12] we just need the RGB, but we might as well keep the alpha here as well, we will replace the alpha
[84:17] in a second. So don't worry about this. But now if I were to preview this result, we have this
[84:23] what sort of looks like an alpha image. But if we hover over our pixels here, we can see how the
[84:31] values change here. So for example, if I were to select a region, if I were to sample a region
[84:36] that's closest, closer to our camera, we have a value that's roughly 11. So because we are using
[84:43] the same value over here on all of our RG and B channels, we will have the same value on all of
[84:50] our channels. And we can see currently that this value is roughly 11. And if I were to sample a
[84:55] region that's farther away from the camera, so one of these buildings in the back, if I were to
[85:00] sample this region, we see now that this value is 422. So this is 422 units between this building
[85:09] as it exists in 3d space and our camera. And I can show you this because I have access to the
[85:15] 3d scene. If I were to step inside Houdini, we can see these are the buildings. And this is the
[85:20] building that's furthest away from our camera, our camera being right over here close to the origin
[85:27] of our world. Here we can see the camera. So if we were to draw a straight line between our camera
[85:35] that's over here, we were to draw a straight line to that sampled region that we have in UQ,
[85:40] which is somewhere around on this building, this straight line, we can see our units represented
[85:46] over here on the X and Z coordinates. So this straight line would be 422 units. And this is
[85:53] what this value here represents. Now currently, this depth layer is it is it's not really helpful
[86:00] for us because we see all of these values that go way beyond one. So to normalize this value and
[86:07] actually see this distance on our buildings, we will have to use a gray node. And this is where
[86:13] our black point and our white point values over here become extremely useful. Because if I said
[86:19] this white point to be essentially like I mentioned earlier, this is like a remapping operation. So I
[86:24] can set the highest value to be this 422 value, I will set the white point to be 422,
[86:33] press enter. And now we can see this nice mood gradient growing across our entire render and the
[86:40] closest objects to our camera will have a lower value and the furthest objects away from our
[86:47] camera will have a value close to one. And now in fact, we can see that our RGB values become
[86:52] this value of one, because I said this over here, we can further control this value. And by the way,
[86:59] if you want to change the values in any of these properties, you can set the selection to either
[87:05] of these values and I'm using the arrow keys left and right to go between these. So if I want to make
[87:11] smaller modifications, I will set the selector here between our second and third number and I can
[87:17] just use my down and up arrow keys to increase the values. And if I want to make bigger changes,
[87:23] I can place the selector one value before and I can make bigger changes like this, we can see how
[87:28] the values changes, you can also use the scroll wheel here. And if I want to make even bigger
[87:33] changes, I can set the selector to our first value and I can use the up and down arrow keys or the
[87:40] scroll wheel and we can see how fast we can adjust these values. So I might want to modify the second
[87:46] value here and I can scroll up and down to further refine the gradient here and this remapping
[87:51] operation. So that's just a quick new tip on how you can adjust the values. So now we have this
[87:57] new layer and really, if we wanted we could just merge it. So I with this gray node selected,
[88:03] I pressed M and this will drop down a merge node and we can merge this on top of what we have. Now,
[88:09] in this case, we want to plus this on top. So we could use a plus operation. And now we can see
[88:16] a little bit of our render below. But sometimes when you want to add layers together, but you
[88:22] don't want really the pixel values to accumulate, you can use a screen operation instead. So this
[88:28] is what we'll do. Screen is like a clamped version of the plus. So again, when you want a more of a
[88:37] it's sort of like a soft plus operation, this screen thing over here. So it's another pretty
[88:43] common operation that you might want to use. Now we're not getting exactly what we want. We
[88:48] do need to modify things a little bit. So this is our depth map, but we want to turn this into our
[88:54] fog layer. We don't really have a background for this, because essentially there were no objects
[89:00] in our 3d scene in order for us to record their distance information from the camera.
[89:05] So we will need to fill in our background, our cells, so we can create a constant. And the constant
[89:13] is like a field color. It's just a it's just a flat solid color. And I will set the RGB values
[89:20] here, I will set this to one. And now I can merge our depth layer on top. Let's set this,
[89:26] let's connect these two layers. And I want our depth layer to be our foreground and our constant
[89:31] to be the background. So I will press Shift X to reverse this. And now we can see this really
[89:36] cool effect. So now it's actually starting to look more like a fog layer. And if we look at our
[89:41] final result as well, we can kind of start to see how things are lining up. Now there's a few
[89:47] problems here to address. But the first thing that I want to address is if we look close enough,
[89:53] we can see this very harsh edge on our buildings. And this is coming from our fog layer that we
[90:00] just created. If I were to go to just the render the composite version over here from our merge,
[90:06] we see we have these nice anti aliased smooth edges on our building. And when we add our fog
[90:14] layer on top, we kind of have this harsh edge, sort of like the result that we get from the
[90:20] unpremult operation that we do for the alpha. And this is because by default, most render engines
[90:26] and specifically in Houdini, we render the depth without anti aliasing, because this is what we
[90:33] need when we are doing bokeh or the focusing effects. So if we wanted to adapt a field to our
[90:40] render, we would need this version of the depth map without any filtering on our edges. And in
[90:47] Houdini, if I were to show this real quick, I will go over to Solaris. And here in our environment
[90:54] render settings, we can see here is where I selected all of the utility layers that we want to export.
[90:59] And we can see that this depth layer by default will use this pixel filter option over here. And
[91:06] we can see how this is set up. Essentially, it's kind of like unremolting all of the edges. And
[91:12] we can see that the rest of these layers are using a different pixel filter. So this is the
[91:18] default filtering that provides the anti aliasing and the smooth edges. So I've exported the depth
[91:24] as it is over here without the filtering. And then below, I created another custom depth map,
[91:32] which is named depth no AA, and it's using the same filtering without anti aliasing as the other
[91:38] ones as well. So if I go back inside of Nuke, here, this depth underscore extra is the default one
[91:44] that Houdini provides. And I have added another one, which is this depth no AA. And if I hook up all
[91:51] of these nodes to our RGB channels, we can see now we have a few issues here. But now we can see
[91:58] that we do have this filtering now on on our edges. The new problem that's happening here is that
[92:05] we have to unremold and then pre mold this around the alpha. So we can see that this problem is
[92:10] really just happening. This black edge is just happening around where we have our alpha. So we
[92:16] will need to bring in on our shuffle over here, we'll need to bring in the alpha that we had
[92:21] from our render. And because this B layer is pointing directly to our render, we can just
[92:27] grab the alpha from this B layer, and we can output this on our output layer. So now if I press A,
[92:33] we have the correct alpha, and we can do an unremold, then we will run our grading. And then we can
[92:40] do a pre mold, and we'll have the correct edges when it comes to the alpha, but also the correct
[92:46] edges when it comes to the separation of objects inside this entire alpha space. So if I were to
[92:53] preview the result now, we no longer have any weird edges anywhere in our render. So while I'm
[92:59] recording this, I realize there's a lot of annoying stuff to do with these edges with all this pixel
[93:06] filtering with with all this NDA aliasing. But really, after a while, this will just become
[93:11] second nature. I'm only realizing how annoying this can be as I'm explaining things. But when I'm
[93:17] actually comping myself, and I'm just going full speed, I don't even realize just how annoying some
[93:22] of these edges can be. But sometimes they can be annoying. If for some reason, you just can get the
[93:28] edges working right, there is also a dilate node, which you can use actually, it's called a road.
[93:34] So if I drop down on a road node, now it sells when you when you place this down, it says dilate,
[93:40] but you have to find it by typing a road. So it's a little bit weird, but this dilate what this will
[93:45] do, it will just push out the pixels one row. So we can increase the size here and I can and we
[93:53] can see what happens, we are just expanding the edges and we can also contract the edges. So if
[93:59] for some reason, at any point, you end up with some weird edge issue that you can fix, you can
[94:05] always just place down on a road node, and you can either dial in maybe a value of one or two,
[94:12] or increase the size to try to fix that problem. But in this case, everything lines up, so I will
[94:17] get rid of this dilate. And we can come back to our final result over here. Now after this merge
[94:24] operation, I will want to drop down a grade node with G. And let's say that with this second grade
[94:29] node here, we can just control the overall strength of this fog layer. So I will just drop this down
[94:35] slightly. And one other thing that happens here, if I preview this from our merge, we can see that
[94:40] this building in the back is a little bit brighter than our background. So our constant, which doesn't
[94:47] really make sense because we want this constant to really be the brightest spot in our fog,
[94:55] because it's essentially the furthest thing away from our camera. So this is way out in z space.
[95:01] So what we can do here after our grade node and before our pre-mult, we can drop down a clamp
[95:08] as well. And this will make sure by default that no values will go above one. So now when we add
[95:14] this together, we can see that this building here in the back completely fades off into the distance.
[95:20] And we can go back to our grade node and we can further control this. So maybe we want to reduce
[95:25] this a little bit. So I will just push the highest value, the white point out a little bit further
[95:31] more. So I can increase the value here to roughly 500. And maybe this provides a better result.
[95:36] Again, we can preview this from our final result over here. And now with this grade node, we can
[95:43] also control the gamma of this transition. So of this gradient in z space, I can drop down the
[95:49] gammas to make this a little bit more obvious. And maybe actually I will want to lower the white
[95:55] point. I might want this building here in the back to be brighter a little bit. And we can already see
[96:01] with just this extra layer that we have instantly a lot of depth to our scene. And this really helps
[96:08] us to quickly see the space that we are in. And it creates this nice separation between our
[96:15] buildings. And we build this with just a few nodes directly inside of New York, which is really great.
[96:20] Let's maybe add another dot over here. And actually, I will reroute this wire here for our shuffle.
[96:26] I'm just using control to add a few dot nodes. And maybe I'll drag all of this setup. I'm holding
[96:33] down shift to select extra nodes. And we can just drop this down below. And finally, one more thing
[96:38] that we can add here. So we have this gradient that's going across our z space, essentially, but we
[96:45] can also introduce a gradient that's going on the y space or vertical gradient. And we can do this
[96:51] very simply in this case, by just using a ramp, I will throw down a ramp. Let's reverse the nodes
[96:58] over here, I'm holding down shift, and I'm just trying to create this vertical ramp. So now we
[97:04] can just drop down a merge and we can multiply this over our result. So when we do this, we can see
[97:10] this is what we get. And we can very quickly bump up the detail even more. Let's maybe go to our
[97:14] gray node over here and just increase the gamma. So we push out our fog into the foreground more.
[97:22] And now we can preview our result. And this is it. So let's maybe this great node I'll place below
[97:30] our ramp, just so we have this sort of like global strength of our ramp, we can still play around
[97:35] with the gamma here as well, maybe lower the gain. Now we'll have to introduce our sky. So we will
[97:41] come back to this fog layer in a second. But this is more or less how you can very quickly,
[97:47] very easily set up a fog layer from here, we can control how further away in space, we want this
[97:54] fog to be by playing around with our black and white points. So there's really a lot of stuff
[97:59] that you can do with this depth map. And like I said, usually it's used to create defocusing effects.
[98:05] But I really like to use it to isolate certain parts. So I like to use it in this case to create
[98:11] new layers like a fog layer, I like to use it to create certain stuff. I usually like to darken
[98:17] stuff that's closer to the camera. And maybe we'll do this in a second as well. And with this vertical
[98:23] ramp, you always want to think of different ways in which you can break up your layers and add more
[98:30] detail and contrast to your layers. One more thing that we could do. And you don't have to follow
[98:36] along with this part, we could also break this up even more. And this is really how you should do
[98:41] fogs, you can add a noise and we'll look more into noise a little bit later. But this is just a noise
[98:48] pattern, essentially, we can also multiply our result with this noise. And now we can start to see,
[98:54] I'll add a gray node here and just gamma this up. And now we can really start to see some nice breakup.
[98:59] And this looks, this works extremely well with fog layers, like we have over here, the problem
[99:05] with this noise is that this is a 3d scene. So the camera is moving. So this noise pattern will
[99:11] not follow. And in this case, we might have to create a 3d layer. So in our courses on voxside.com,
[99:19] in some of the courses, we create this noise as a volume directly in 3d and export this
[99:26] and export it as a render. Or in some courses, we create this directly in nuke with a particle
[99:32] system, just so this noise follows the camera and it's actually spread out in 3d space. So it
[99:37] doesn't work in this case with just this simple 2d noise layer. And I think for a beginner course,
[99:44] it's not really worth going into particle systems and all of that right off the bat. So I don't want
[99:49] to really overload you with information. But just as an example, that's this is some of the stuff
[99:55] that you can do to create this breakup, you always want to think of how you can break up the layers
[100:00] even more and add more details. So this will be our fog for now, we can select all of the notes
[100:06] that we have over here. Maybe we can select them with the dots. And if I do tab and drop down a
[100:12] backdrop, this will now create a backdrop for us. This is strictly for organizational purposes,
[100:18] we can spread this out a little bit, we can double click here inside the label, we can do fog. And I
[100:24] usually like to set these backdrops to be darker and more desaturated. So we have our fog layer here,
[100:32] we'll do a backdrop over our other setups as well for the environment and our character,
[100:38] but we'll have to add a few more stuff first. But for our fog, we are pretty much done. Like I
[100:43] mentioned earlier, we'll have to come back to this after we add our sky and some of the other elements.
[100:48] So with the next lesson, we can take care of our sky. So I will see you there.


### 3D System & Sky layer [100:53]
**Transcript (timestamped):**
[100:53] So we can use the AOVs to adjust our already existing render, we can use the utility passes
[101:01] to create our own layers. And we can also create layers by using Nuke's 3D system. And we're gonna
[101:08] do a brief introduction with Nuke's 3D system. It's if you're coming from a 3D application,
[101:15] this will be very familiar to you. Now Nuke's 3D system isn't really as powerful as an actual 3D
[101:21] application. So you can really model things, you can adjust already existing models, you can do
[101:27] certain types of transform operations and soft transform. But really, it's mostly here to help
[101:34] us place certain elements in our scene. And in this case, what we want to do next with this lesson
[101:39] is place a 3D sky that moves with the camera. So currently, if we were to bring in our sky,
[101:47] so I'm gonna press R, and I'm gonna bring in an HDRI in this case, this would work with a
[101:54] just a regular image of a sky in this case, I'm using an HDRI which we got from Polyhaven. So
[101:59] you will have the link if you want to use the same sky as me in the lesson description. Now with
[102:05] this, we can drop down a gray node and we can gain this down slightly. And we can't just really
[102:11] merge this behind our environment. So over here, we have our environment. If I set the background
[102:18] to be our sky, first of all, we see we run into a problem where our resolutions no longer match.
[102:24] So our overcast sky over here, we can see we are using this resolution. So in this case,
[102:30] we would have to use a reformat node. And because we set our project settings, so when I press S
[102:37] without anything selected, and go to our options over here, because we have set this to 1080p,
[102:44] our reformat by default will resize our footage or whatever we bring in to this 1920 by 1080. So
[102:52] now when we do our merge, this is going to work. Now if we just render a few frames over here, we
[102:59] are automatically going to see this problem that our geometry is moving. So our camera is moving,
[103:04] but our sky is static. So we need the sky to follow the camera. Now we are going to use a 3d system
[103:11] for this. I'm going to let's maybe just disconnect our sky. And I'll remove the reformat and the
[103:16] gray node and just keep the sky over here for now. If I while I'm over the viewport, if I press tab,
[103:23] this will now switch over to this 3d view in which if I hold down alt and left click, I can
[103:29] navigate around, I can hold down alt and right click to zoom in and alt and middle click to
[103:34] pan things around. So it's really exactly like in most 3d applications, I believe somewhere in the
[103:41] project settings, let's go to edit somewhere in the preferences over here, you can change how the
[103:47] navigation controls work if you are used to other hotkey combinations. But I'm just using alt,
[103:52] left click, middle click and right click to zoom in to move around and navigate in this 3d space.
[103:58] We have some options over here, we are not going to look into this right away. What I want to do is
[104:04] just give you a very brief introduction to how the system works. So let's say that we want to
[104:10] place a card in our scene and we will do this in the next lesson, we are going to actually place our
[104:16] small cards. But right now, let's just go ahead and place down a card. So you can see that in
[104:23] between brackets, this says geometry. So this is what we want. And we can see this now in our 3d
[104:27] space. We can use a texture. So over here where it says image, we can append a texture. So we can
[104:34] point this to our sky. And now our sky will be mapped to our 2d card, we can also use any other
[104:41] image, we can also use our footage if we want, we can see now that the render is mapped to our
[104:47] card or we can a lot of times you will have to use a let's drop down a noise draw. So we can use
[104:54] a noise texture for our card. And now with our card selected, we see we have the gizmo here,
[105:00] we can use we and R to move scale and rotate. So WER just like it would work in a 3d application.
[105:08] So we can push this further into this space, we can scale this with R on individual axis and we
[105:15] can rotate things around. And now if we wanted to use this in our comp, if I press tab again,
[105:23] we don't have anything showing. And this is because we have to render this from the 3d engine sort
[105:30] of to our actual comp, our 2d comp. So to do this, if I press tab again to go back to our view,
[105:37] we can drop down a scan line render. And over here, we have two versions and we are going to use
[105:43] the 3d classic, we are not going to use the beta versions for now, let's just use the 3d classic
[105:49] versions of all of these 3d nodes. So let's drop down a scan line render. And here, we have a
[105:55] background, an object or scene and a camera. Now, we don't have a background in this case,
[106:01] we don't need one. But our object in this case will be our card. So I'm going to move this over
[106:06] to the right. And by the way, if I hold down control, while I have a node selected, this will
[106:11] grab all of the nodes above it as well. So this works with any nodes, if I want to select this
[106:18] node over here, we can see all of the connections that we have with this node. So if I hold down
[106:22] control while I'm dragging this around, it will grab the entirety of the nodes above it. So it's
[106:28] sometimes very useful for organization. Now, we have our card. So if we go back to our scan line
[106:33] now, we just the card connected to our OBJ, if I press step now, we actually see our card over here.
[106:40] By default, this will create a camera for us, even though we haven't specifically created the camera,
[106:46] it will create a camera for us that's right at the origin and it's, and it's facing along the Z
[106:53] direction. So if I were to drop down a camera, again, we will use the 3d classic version,
[106:59] we can see that this is the camera that we create. So we can now hook the cam arrow here to our camera.
[107:05] And if I go to our scan line and I press step, we can now grab our camera and inside the camera
[107:11] settings here, we can use our translate rotate and scale to move the camera around. So I can
[107:18] bring the camera back and we can press step and see exactly what kind of transforms you are doing.
[107:23] We can use the gizmo as well. So I press w and we can grab the camera, rotate this around. And if I
[107:28] press step, we can see how our render essentially changes. So we can adjust the camera through
[107:34] our settings here or directly in the 3d viewport. Now obviously, in this case, we are going to read
[107:39] in the camera that we export from our actual 3d scene. So we don't have to set the camera here,
[107:46] we can just select read from file and we are going to bring in this cam 01 usd file. And now if I
[107:54] press step, we can see our camera is all the way over here. And this will be placed exactly where
[108:00] it's placed in our 3d scene in Houdini as well. If I go back over here, we have our camera, we can
[108:09] see it's this camera here. And when I go over back inside of nuke, it's again going to be over here.
[108:14] So now with this card selected, I can press w and I can push this around, I can bring this up.
[108:21] And I'm going to try to place this roughly somewhere where our camera can see it, I can increase the
[108:27] uniform scale here. And when we go back to our render, let's maybe just make this a little bit
[108:32] smaller. Now this will follow our camera. So essentially, this is an element that we can now
[108:38] use in our composition. So from our scanline render, if we want, and this is something similar
[108:43] that we will do with the smoke cards later, we can just do a merge with m and just place this here
[108:50] on top of our render. Now currently, this doesn't look like anything, but we can see that it's
[108:56] following the camera and it's nicely integrated with our 3d system. So let's get rid of this merge.
[109:02] And in the case for our sky, we don't press tab, we don't really want a card, although we could use
[109:09] a card and just push this back into 3d space like so and just make this bigger, sort of how we would
[109:15] do it in a regular 3d scene. But in this case, it's better off if we use a sphere instead, so we
[109:21] will drop down a sphere. And here we can see our sphere is really small. So we want this to be huge
[109:27] in order to compensate our entire geometry. So I'm going to push out the uniform scale by quite a
[109:33] lot. Let's try a value of 100. And now we can see our sphere and we can get rid of our card with
[109:39] a noise. And for the sphere, again, we can just map any texture that we want. And in this case,
[109:45] we will map our sky HDRI so we can point the image to our sky and we can see our sky nicely mapped
[109:53] to our sphere. Now this sky is 4k by 2k. So we don't really need to use this much resolution for
[110:02] the sky. In fact, I want to lower this by half. So if I drop down a reformat node after by default,
[110:09] this will look at our root format, which is 1920 by 1080 again. But in this case, I will just set
[110:15] this to scale. And I want to specify exactly how much I want to scale this. In this case, I will
[110:20] scale this down by 50%. So if I set the scale to 0.5, this will now give me a 2k by 1k value. So when
[110:28] we map this onto our sphere, because this is placed all the way in the back and we are covering a
[110:34] very small part of our screen, and we have a bunch of elements on top, we don't really need
[110:38] that extra resolution for from a 4k map. And this will just improve our performance a little bit.
[110:44] So now we can use this will point the object scene from our scan line render to our sphere.
[110:50] And if I go to the scan line and preview this and hit tab, now we can see our sky will follow
[110:57] our camera. If I just load up a little bit of this animation, let's take a look. All right. So now we
[111:03] can use this layer here, the scan line render layer as our background. And finally, we have a sky in our
[111:11] render as well. And after the scan line, we can do any changes that we want, we can also do them
[111:17] directly on our texture as well. So either we add a gray node after the scan line and drop this down,
[111:24] maybe decrease the gamma a little bit, or I just do a gray node after our reformat. So before we
[111:31] map this texture onto our sphere, we can also affect the grading here. In this case, maybe we can
[111:36] just use the grading after the scan line. So I can drop this down slightly. And this is looking
[111:43] fairly decent. We can rotate the sphere if we want to get a different part of our sky onto our
[111:51] render. So if I go to the sphere here, I can choose the rotate y value here, I can just use the scroll
[111:58] wheel, maybe let's try to find a different part or other area of our sky. So this is exactly how
[112:05] it would work if we were to use a HDRI inside 3D directly. But really, in this case, I would use
[112:13] a 3D projection of the sky. Now, I don't really want to get into 3D projection because it might be
[112:20] a little bit beyond a beginner course. I feel like a lot of these, a lot of these things that I've
[112:26] already covered are maybe slightly beyond an introduction course. So I want to avoid getting
[112:32] too deep into some of these techniques. But with a 3D projection, for example, in our Ultimate Effects
[112:39] Workshop on voxside.com, we use a 3D projection to manually place cloud lining textures between
[112:47] clouds to decide exactly where lining can happen in the sky. So you can get pretty advanced with
[112:55] some of the stuff that you can do with a 3D projection and with the 3D system in general.
[112:59] But to keep things simple, let's just keep this as it is right here. We are just using a texture,
[113:06] mapping it onto a sphere and then bringing in the camera from our 3D scene. We have our sphere
[113:13] linked up to our scanline render. And then this is basically a very simple sky replacement technique.
[113:19] We should probably also preview this from our fog layer as well to better judge how our sky
[113:26] should look. So now I can go back to our grade, maybe I can bring this up or down and I can play
[113:31] around with the rotation y of our sphere. And I will leave this up to you. But one final thing
[113:37] that I would like to touch up on is if we go back to our 3D view and we hit tab, first of all,
[113:43] sometimes you might want to display multiple different settings here. So when I'm dealing
[113:49] with 3D, I will set this value to maybe five, just because if I were to select, if I were to just
[113:56] have one over here, like I usually do, and I would select the sphere and preview just the sphere,
[114:03] we can see that now this no longer shows us our camera. And now if I select the camera and preview
[114:08] the camera, we no longer see the sphere. So to fix this, we can set this maybe we can set this to
[114:16] five. And now if I were to select the sphere and preview the sphere, we also have the camera showing
[114:22] as well, because we have the settings of the camera opened over here to the right. So all of this to
[114:27] say is that sometimes if you have a hard time dealing with the geometry in this 3D system,
[114:35] and you want your 3D geometry to show up at all times in this 3D view, just make sure that you
[114:40] are not using one over here as your display the settings. And one more thing about this sphere
[114:47] technique to replace the sky, we don't really know exactly how big this sphere should be. This sphere
[114:54] should really be all the way in the back of our geometry. So at the very least, it should be
[115:01] way bigger than the building that's furthest away from our camera. But we don't really know where
[115:07] that building would line up in 3D space. And this is where we have a node that's called position
[115:13] to points. So if we hook this up to our main render over here, I'm just going to use this dot
[115:20] from over here that essentially points to our in this case, we can we can look at our unpromoted
[115:26] layer doesn't really matter. Or let's just maybe point this to our render for simplicity's sake.
[115:32] So this position to points node is pointing to our render. And inside here, let's set this back to
[115:38] or actually let's just keep this at five because we are dealing with a 3D system,
[115:42] we can set this surface point, we will set this to look at our world position, which is going to be
[115:48] this P layer. And now when we do this, let's go ahead and just preview this layer. So in this case,
[115:55] I'm going to go ahead and set this only to one, because I just want to focus on this single layer.
[116:01] So in some cases, it's actually better if you just set this to one, because you want to isolate your
[116:06] 3d object that you're working on. Anyway, our position to points. This is a really, really cool
[116:12] representation in 3d space of our render scene. Basically, what this does is it's spreading out
[116:19] all of our pixels from our main beauty render. So from the RGB channels, it's arranging the pixels
[116:28] based on their world position value. So if we were to press tab and just look at our world
[116:34] position, so I'm going to look at our render and set this to our P value, we can see that as I hover
[116:41] over our over the pixels here, if I just sample this region, we can see that this surface of the
[116:47] building has a coordinate of 52 on the x 17 on the y and negative 73 on the Z. So this is how our
[116:56] position to points knows where to place our pixels in the 3d space. So if I go back to the
[117:03] position to points, we get this really, really cool representation here. And it's super useful to
[117:09] troubleshoot your 3d objects and to know where you should place because now if I set this properties
[117:15] here, let's increase this to five so we can also see our sphere. If I also select our sphere,
[117:21] we can see that it's actually not entirely covering up our geometry. So like I mentioned earlier,
[117:27] this sphere should be at least as big as our furthest away point in our geometry. So it should
[117:34] be way beyond this building here in the back. So now that I have this 3d representation, I can
[117:41] simply increase the uniform scale as much as I need to. So I will set this to maybe 1000 just to
[117:48] make sure that this is big enough. So if I preview this now in 3d, we can see that this is more or
[117:54] less where we should place the sky in relation to our building. So now when we go over to our merge
[118:02] result over here, let's set this back to RGBA and and control shift click to get rid of that sample
[118:08] region. Now we will know for sure that the movement of the sky is correctly matching the movement of
[118:15] our 3d scene because for example, if so currently our sphere is set to 1000, if I were to set this
[118:22] back to 100, we can see this changes a little bit and this will mean that our sky is going to move
[118:28] way too much in relation with our geometry and it really won't feel when you preview this animation.
[118:36] Let's maybe just render a few frames. It really won't feel like this sky is way, way beyond our
[118:43] geometry. So pushed in z space. I'm not sure how noticeable this will be, but we can kind of feel
[118:49] it that the sky is a little bit flat. There's really no parallax happening here. And if I set this
[118:55] uniform scale back to 1000, this will now our sky should move a little bit slower than our geometry.
[119:01] Again, I'm not really sure how noticeable this is. It's probably not that noticeable, but this sort
[119:07] of thing is really, really important, especially with the next lesson when we look into setting up
[119:13] our 2d cards for the smoke, this will be extremely crucial that we place them in the 3d world exactly
[119:20] where they should be in order to do the proper compositing. So for now, at least we are pretty
[119:25] much done with the sky. We are going to leave this position to points over here because we'll
[119:31] need this in the next lesson. But for now, let's go ahead and just grab all of these nodes, drop
[119:36] down a backdrop. And let's go ahead, rename this label here to sky and also just darken this a
[119:43] little bit. So this will be our simple, simple sky setup. Again, we might want to preview this from
[119:50] our result with the fog as well. And if we compare the renders again, we are really, really starting
[119:57] to see a big difference. So with the next lesson, let's take a look into how we can add our smoke
[120:03] cards. So I will see you there. Now that we are familiar with the 3d system, we can work on our


### 3D Cards & Smoke [120:04]
**Transcript (timestamped):**
[120:08] smoke cards. Let's go ahead and we have to read in our smoke footage. So I'll press R and let's
[120:14] bring in our hero assets underscore smoke, which looks something like this. So this is just a
[120:20] simple render. I did it's a simple smoke simulation in Houdini and rendered it in sort of a flat
[120:27] lighting so we can use it in multiple different kind of situations. And let's say lighting conditions,
[120:34] when you want to create this sort of layer that you want to use as an element as part of your
[120:41] composition, you want to avoid super strong directional lights or very harsh contrasts in your,
[120:48] in this case, smoke. So we would want to avoid having like a, let's say a directional light
[120:54] that's heavily skewed in one direction. Because if we keep things flat, this would allow us the
[121:01] greatest flexibility in order to blend it in any lighting conditions that we have with the rest of
[121:07] our comp. So from this render here, we have to map this to a card sort of like we did earlier. So
[121:15] let's reset our timeline. We can also see here that our timeline is now going from 1001 to
[121:22] 1450. And this is because this sequence is up until this 1450 frame. And we are using the global
[121:30] here. So if we were to switch this to input, now our timeline is mapped to 1050 and 1450,
[121:38] which is the input of our footage that we are previewing. And when we set this back to global,
[121:43] now we have this up until 1450. Now let's go ahead and press S. And for our frame range here,
[121:50] let's set this to 1240, which is the range of our original render. And our global timeline will
[121:58] now match this 1001 to 1240 frame range. We also see that since this footage starts from 1050,
[122:08] in this case, we have to offset this animation slightly so we can do a time offset. And if I
[122:14] want to push this 50 frames forward, we can set the time offset here to negative 50. So now if we
[122:20] go over at 1001 and play the animation, we should have this playing. And now also with this time
[122:27] offset, because we have 400 frames to play with, so from 1050 to 1450, we have 400 frames. And the
[122:34] total length of our final comp is going to be 240 frames. We have around 150 frames that we can
[122:44] offset. So when we duplicate this later and assign it to different cards, we can also do a time
[122:49] offset for the duplicates. And in that way, we can create very easily variations between our copies.
[122:55] And we'll see how all of this works in a second. But now from our time offset, let's straight away
[123:02] append a card node over here. So this will hook it up to a card geometry, which we see over here.
[123:08] So now we can just push this into space and we will line this up with our geometry. Let's go
[123:14] ahead and also grab our camera, which we already have over here, and we'll grab this camera node
[123:19] and let's copy this and let's paste this over here. And we will also while we are previewing the
[123:25] position of this geometry, we will want to reference our position to points node, which we had set up
[123:32] earlier. So let's go ahead and we can drag this node all the way at the bottom here. And let's
[123:38] actually make some more room. I'll grab all of these nodes and I will just drag them up like so
[123:44] and maybe drag all of my setup here with the card up as well. So we have our camera, our card,
[123:52] and let's go ahead and preview our position to points. So here we have it. If I zoom out,
[123:57] we can see our entire geometry, we can see that our card is pretty small. So now what we can do is
[124:03] just drag this in space and position this, let's go ahead and increase the uniform scale here. And
[124:10] we can see that this position to points is essentially just a point cloud, we can see that
[124:17] it actually intersects with our geometry. So our card geometry actually intersects with all of our
[124:23] points. So for example, if I want to place this behind this rubble over here, I can just roughly
[124:30] estimate where our camera is. Or if I want, I can set our where it says here default, I can go
[124:37] inside if I have the camera selected, I can now select this camera to over here. And now I will
[124:44] view this position pass through our camera. So this is actually not our render, this is previewing
[124:51] this position pass. So our point cloud, we are, we are previewing this from our camera, which looks
[124:58] exactly like our render. I can also go to the position points node over here and I can play
[125:04] around with the settings I can make the point size bigger or smaller if I want. So from this
[125:10] camera view over here, I can select my card and I can see directly where I want to place the smoke
[125:17] layer. I might want to bring this up a little bit. And I can also play the animation now slightly.
[125:23] And we can see that everything is working. Maybe I'll make this even bigger. Let's do something
[125:28] like this, we can always adjust this later. So let's say that I'm happy with how this looks,
[125:32] I will drop down a scan line render, let's point the cam to our camera and our object slash scene
[125:39] will point this to our card. And now from our scan line render, let's press tab. And here we have it
[125:46] from here, I can basically just do a merge. And if we merge this on our, so I pressed M to
[125:53] drop down a merge, this will be a my a layer and my background layer will be our final comp,
[125:58] or rather our comp so far. So our main chain, I can drop down another dot over here. And this is
[126:05] my setup with the card. Now it's not intersecting anymore with our geometry, because we are just
[126:11] plusing this card on a sort of like a 2D image. So this is a 3D card, we are plusing it over a 2D
[126:17] image. And I will show you how we can actually blend this in a second. But first, what I want to see
[126:23] is if this lines up with our camera, I'm just going to select a small region over here over a few
[126:29] frames. And I will hit play and let's see if this is following the camera. All right, and we can see
[126:34] that this works. So this is fine, I can still go in my card settings over here with double click.
[126:40] And maybe I want to position this a little bit more, I might want to scale this up, maybe bring
[126:46] this up slightly. So this is fine. But again, the problem is that we are no longer obscuring
[126:53] our smoke with the geometry. And what we can do here is we can use the depth map that we used
[126:59] earlier to create a mask and isolate this part of the, in this case, this pile of rubble over here,
[127:07] we can push our depth information far enough until it reaches the rubble, and then use that as a mask
[127:14] to cut out a part of our smoke. So this will only make sense probably as we start to create this mask.
[127:22] Let's go ahead and we'll need another shuffle. And in fact, we will need the same shuffle that we
[127:28] used in our fog over here. So this depth with no AA. So we want the version with anti aliasing or
[127:36] rather with the smooth edges. So we can copy this, let's control C and control V to paste this over
[127:42] here. And we will point this back to our original render. Let's point this arrow to this dot, and
[127:49] we can rewire this maybe a little bit, let's do something like this. And I'll just drag this position
[127:57] points node over here to the left. And with our depth pass over here, we only need we want to
[128:04] use this as a mask. And remember what I said earlier, when we want to use it as a mask, we just need
[128:10] to use the alpha layer. So I will disconnect all of this. And I will just connect our our depth over
[128:16] here to our alpha. And for now, let's set this property value here to one. So we are just focusing
[128:22] on the currently selected node. So from here, if I press a, we have our depth information here,
[128:28] so I can drop down a grade with G, I will set the channels to RGB, or rather to alpha, because we
[128:35] only have the alpha channel now. And again, if I increase the white point, if we remember from
[128:41] earlier, roughly a value of 400 will be our furthest point away from the camera, which is this
[128:48] building here. But we don't really want to spread this range specifically, what we want to do is
[128:56] have a rather narrow range, but we want to offset that range or push that range into Z space. So what
[129:05] I mean by this is if I were to set this to a lower range, if I were to just use a value of, let's
[129:11] maybe make this fade over 20 units, so I will set the white point here to 20, we can kind of see a
[129:18] little bit over here, let's maybe make this even smaller. So I will set this maybe let's do five
[129:24] instead. And now we no longer see this. If I want to push this entire gradient along our values,
[129:30] I can use the offset adjustment instead. So if I want to push this further, I can decrease the
[129:36] offset value. And if I decrease this enough, we can start to see as I push these values, we can
[129:42] sort of see how this gradient that's over five units. So if we imagine this white to black value
[129:50] is spanned across five units in 3d space, we are just pushing this value into this Z space so
[129:59] further away from our camera, until we sort of isolate the rubble or rather the pile of rubbles
[130:05] that we are interested in, which is going to be this one over here. So we can see now that we
[130:10] finally reached our rubble and this is exactly the mask that we want to cut out our smoke. So
[130:17] what I can do now is if I go back to the scan line render and let's press a to get out of the alpha
[130:24] view, we can drop down a gray node and we can point the mask to our channel that we created over
[130:30] here. So I will point the mask to our grade over here that points to our shuffle. And if I lower
[130:36] the gain, we can see now we are getting the reverse of what we want. If I were to preview this from
[130:43] our final result, we can see now that we are kind of keeping the smoke that's in front of the rubble
[130:49] and we want the reverse effect of this. So if I go to the gray node, I can set this option here
[130:54] for the mask, I can check invert. So now we are getting the correct result. We can also see that
[130:59] we are left with this dark shadow. And this is because we are affecting only the RGB channels.
[131:04] So if we go to this gray node and press a, we still have the alpha information for the smoke
[131:10] that's in front of the rubble. So we want this grade adjustment to also affect the alpha as well.
[131:16] So we will chip. So in this case, we will set this channels to RGB a. So now if I press a,
[131:21] we also have this alpha. And finally, if we preview the result, we have this now nicely
[131:27] integrated with our render. And it really looks like it's behind our rubble over here,
[131:34] even though it's just a random 3d card placed in the 3d system. So this is with and without our
[131:41] grade adjustment. And now we can still go back to our card, we can make this maybe slightly bigger.
[131:48] And now our mask adjustment will persist through our 3d changes, which is really great. And if
[131:55] we want to further control this transition more, we can increase the spread of our ramp here a
[132:01] little bit. So if I were to increase the white point, we can see how this changes. So maybe I want
[132:07] a little bit more interaction with our rubble, we can change the offset, we can bring this
[132:12] slightly forward. And I think in this case, it's actually working out pretty nicely, we can play
[132:18] around with the gamma as well. So we can see how, so we can see how much control we can get with
[132:24] this technique and really how flexible this is. Now from here, we can still do some grading
[132:30] adjustments. So if I drop down another gray node, maybe I want to lower the gain a little bit,
[132:37] we'll probably revisit all of these settings later, as we add all of our or rather the rest of our
[132:43] elements. And then we'll start from the top and work our way down to the bottom. So we'll start
[132:49] back with our sky and our fog and readjust all of the elements. One final thing that I might want
[132:55] to show you here is if I just preview this channel, or rather the smoke layer in isolation, we have
[133:02] Alpha channel. So when we preview the final result, if I were to drop down another gray node, and this
[133:07] is something that I usually like to do, this gray node, I can set to only affect our Alpha. And if I
[133:13] want this smoke to be less opaque, because we are using this merge operation, which is set to over,
[133:20] the way this is blended with our compositing will depend on the Alpha. So if I have this gray node
[133:26] set to Alpha and I reduce the gamma, we can see how we can sort of start to make the smoke more
[133:34] transparent, but only around the edges. So as I decrease the gamma, we are keeping some of this
[133:39] opaqueness in the center of our smoke, but we are reducing it towards the edges. So this is
[133:44] something that you can play around with, meaning a gray node set to Alpha, feel free to experiment
[133:51] with this. So usually I have a gray node that's just set to Alpha and one other gray node,
[133:57] affecting only the RGB values. So I can make this overall darker. And with our second gray node,
[134:03] I can affect the transparency directly. So really, between all of these techniques, you get a lot of
[134:08] flexibility and a lot of options. Let's maybe make some more room here. So this is the setup.
[134:14] And now we can just copy this setup very easily. So what we have to do from here is I can grab
[134:21] all of these nodes, including the merge, I will press alt C to duplicate all of them. And all we
[134:26] have to do here really is connect or rather reconnect the shuffle to our render, let's maybe
[134:33] make some more room and let's bring all of these layers down below like so bring this up. So now
[134:40] this shuffle over here should point to our main render. So I can just grab this node and just point
[134:46] this to our other dot where we have this connection. So we should have exactly the same setup, I can
[134:52] merge this on top of our result. And now with our second smoke copy over here, let's maybe reset the
[135:00] timeline. Let's also change the time offset here. So I might want to push this maybe 50 frames more
[135:07] than our previous ones or set this to negative 100. Just so we are in a different part of the
[135:12] animation for the duplicate. And this will help us with variation. And very easily, we can add more
[135:18] detail this way. So now I can grab the card and let's preview the card. And let's also preview
[135:25] our position to points pass. So with this card selected, let's make sure that I'm selecting the
[135:31] right one. Alright, and let's make sure that we are previewing more properties since we are dealing
[135:37] with 3d. So I'll set this value here to five. Let's preview the card, double click the position to
[135:43] points. And let's go back to our card. So we can now position this in a new spot. Again, we will try
[135:50] to sort of match where our rubble is essentially. Let's do something like this. And I will disable
[135:57] the grade all of these gray nodes and just focus on the positioning for now. So if I preview the
[136:03] merge result, it's over here, which is looking pretty good. Maybe we can bring this over, we can play
[136:09] around with the scale, make this bigger or smaller. But this is fine. I might want to introduce a little
[136:15] bit of variation on the Y as well. I might want to just rotate this plane, not so much. Let's undo
[136:21] this. Let's try to set the values here directly. Let's use negative five and just maybe rotate the
[136:28] plane, maybe negative 20 on the Y should be good. Introduce a little bit of variation in the rotation
[136:35] as well. And now what we have to do with our grade here for our depth mask is find the right offset.
[136:43] So I will try to push this further until we isolate this rubble over here. So we'll just
[136:49] increase the offset until we get the rubble that we are interested in, which is over here at this
[136:55] value. So around nine units. And now I can re-enable all of our mask adjustments. Let's preview this
[137:02] and let's preview the RGB. And here we have it. Maybe in this case, I will want to brighten this
[137:07] smoke overall. I might want to go back to our mask. Let's set this back to one. So I might want to
[137:13] play around with the offset. Let's maybe just isolate this entirely from the rubble. All right.
[137:19] So here we have it and we can preview some frames here as well and see what we get. So I would say
[137:25] this is looking pretty good. It's fairly believable. I might want to isolate more of our rubble for this
[137:34] first layer of smoke that we have here. So this is the part where you just go back and forth between
[137:40] the settings and your readjustings until you are satisfied with the results. So maybe I will just
[137:46] decrease the offset here and just place this more behind our rubble instead of what we had earlier.
[137:53] And one other thing that we can do here, we can see if we look at just our smoke render,
[137:58] it's really flat on the ground. I might want to fade this off towards the edges,
[138:04] just to help us blend it more with the environment. And we can use a radial for this. So if I drop
[138:10] down a radial, we will try to match it with the resolution of our smoke. So in fact, what I will
[138:17] do is I will select this read here with the smoke and then I will drop down a radial. And now this
[138:23] will place the radial exactly in the centers. So I can now grab this gizmo here for the radial.
[138:29] And while holding down control, I will just scale this up like so, maybe scale this even more. And
[138:35] I will use this gradient to fade off the smoke layer itself. So now I can disconnect it from our
[138:42] render. And from our render, I will drop down a multiply or rather a merge node, which I will
[138:47] set to multiply. And I will point the radial back at our smoke. So we have the same resolution on
[138:54] both of our smoke and the radial. So now if I were to enable and disable this, we can see this is
[139:00] the result that we get. And I can maybe decrease the softness and I can increase the area can maybe
[139:06] mask things out a little bit more. So with this extra layer, we might have a smoother result,
[139:13] where it intersects with the actual ground. So if we take a look at our at our result from over
[139:20] here, I might want to increase the brightness of this smoke. But essentially, if we look at this
[139:25] result with and without our radial adjustment, it's we can see it's more nicely blended with
[139:32] our environment. So in fact, we will want to copy this setup for all of our cards as well. So I
[139:37] will just grab all of these nodes, let's copy them. And let's replace this render from our time set
[139:44] from our time offset over here. Alright, so now our second radial as well, or rather our second
[139:50] smoke element as well, we'll have this smooth fade on the ground intersection. So again, here as well,
[139:57] if I were to enable and disable this, in this case, for our second layer, it doesn't really make much
[140:02] of a difference. But it's still something nice to do with your elements. And let's do one more and
[140:08] place this behind our behind this rubble as well. So again, we just have to copy this entire setup,
[140:15] grab all of these nodes out C, let's connect or rather reconnect our nodes. And whenever you have
[140:21] a connection that's that has to like sort of travel a big distance, if you want to make a forward
[140:28] connection. So if you want to connect this node over here to this node, you can select the first
[140:34] node that you want to connect hold down shift, select the second node. And then if you press shift Y,
[140:39] it's going to draw this forward connection between the two dots. So now we can see this is connected
[140:46] and everything still works. So this is our duplicate. Let's go ahead and disable the all of our gray
[140:52] nodes. And let's grab our card and let's just place this forward. I'll press W to go in my move
[140:59] gizmo. I know it's it should be somewhere around this part. Of course, we can now set this value
[141:05] for properties here to five. And let's also select our position to points pass, select back our card,
[141:12] press W. And let's see where our rubble should be. It should be really somewhere in front over here.
[141:19] I will probably have to scale this as well. Let's grab our uniform scale, drop this down,
[141:24] place this down below. And somewhere around this place should be okay, let's preview this from
[141:31] our render, we will merge this in our chain. Let's go ahead and preview this. And from over here,
[141:37] I can say that this should be offset a little bit on the x direction. And also for this time offset,
[141:45] let's use let's push this out even more maybe to 25 frames more just to maintain that variation. And
[141:53] now we can enable our gray nodes again. And we will need to find the right offset. And let's go
[142:01] ahead and set this back to one. And for our grade node pointing to our depth, we will want to bring
[142:07] in the offset until we isolate this rubble right in front somewhere around this place, I would say.
[142:14] So now if we preview the result, we have our third copy over here, we can go to the grade node,
[142:21] we can make some further adjustments and also on our alpha as well, maybe I'll drop down the gamma.
[142:27] Overall, make this a little bit more transparent. And let's go ahead and preview some frames with our
[142:33] third copy as well. Alright, so I'm pretty happy with this, all of our elements are nicely integrated
[142:39] with our 3d scene. And this is where we have combined our 3d system with the utility layers.
[142:47] And hopefully you can see how everything is coming together. And now you have a small idea on some
[142:53] of the things that are possible and the flexibility that you have in compositing. And really here I'm
[142:59] just scratching the surface, you can really go pretty insane with some of these adjustments,
[143:04] you can really build an entire world and tell any story that you want through compositing. So this
[143:11] will be good for now. Let's go ahead and grab all of these nodes and let's organize things, grab all
[143:17] of these and place them down below. So all of this here will be calm, let's draw a background. And this
[143:25] is now this is going to be our let's just simply keep this as a smoke. And let's maybe choose another
[143:32] color here and the saturated this darken this. So this will be our setup with the smoke and adding
[143:38] just a few of these smoke layers can really help make your scene come alive, especially with environments
[143:46] whenever you add a subtle thing that's changing over time, it's really going to help you break up
[143:52] that static sort of feeling. So if we were to compare this with our original render, if we just
[143:59] look at this, even in isolation of all of the color adjustment that we did, if we look at this and
[144:05] then we compare this with our smoke on top, we can really start to sort of get a feeling that this is
[144:13] an environment that's actually alive. So it's always worth adding a little bit of movement,
[144:18] whether you are breaking up the fog or you are adding certain elements like these smoke layers,
[144:25] it's always worth going this extra step to improve your shots, whether you are working in CG or with
[144:31] real life footage, this is something that you will encounter over and over. And with the next
[144:36] lesson, we can take a look into how we can create our own layers directly in Yook to contribute to this
[144:43] coming alive of the environment feeling. So I will see you there. So for the next layer, we will want


### Ground whispy smoke [144:47]
**Transcript (timestamped):**
[144:49] to create a very thin sort of wispy kind of smoke that goes over the ground specifically over the
[144:56] entire ground. And we can use all of the techniques that we know so far, we will create a plane which
[145:03] will place on top of our ground in a 3D system. And then we are going to mask out parts of our
[145:10] geometry based on their height. So first of all, let's start off with a noise. So I will drop down a
[145:17] noise and make sure that this is the version that has this draw in between brackets. So when we preview
[145:22] this, we've used this before. So all rather I've briefly showed you this when we were breaking up
[145:28] the fog. But this noise layer is essentially just a pattern which we can control and further refine
[145:35] to suit our needs. So we can see we can increase the size here, we can play around with the lecunerity,
[145:40] gain, gamma and so forth. So this noise is really, really helpful. I use it in pretty much every comp
[145:48] that I have ever done. You always want just a little bit of detail or you want to break up
[145:54] certain parts of your geometry or your other layers. So this is extremely useful in this breakup
[146:01] type of situation. But in this case, we want to use this to create our own sort of stock footage.
[146:08] So to say that will become this kind of wispy smoke. Now here previously, we have used an actual
[146:15] rendered file. So we've I've created this in Houdini, you could have also used maybe a live
[146:21] action plate of this kind of smoke animation. Now whenever you have the option, you should always
[146:28] use pre rendered elements or filmed elements because obviously that will give you the most
[146:34] realistic results. But in some cases, you can just simply fake some of these layers directly inside
[146:40] of Nuke if you combine some of these noises with distortions and so on. And this is what I want to
[146:46] show you with this layer how we can leverage the simple noise texture to create this kind of
[146:51] wispy smoke on our ground. So first of all, since I want to use this as more of a texture,
[146:57] I want to make this a square format. So if I do a reformat node over here, and I said this output
[147:04] format, usually I like to use either 2k or 4k for this kind of situation. So in this case,
[147:11] 2k will be just fine. Let's choose here square 2k. And I connected the noise to this reformat.
[147:17] The noise will now be mapped on this 2000 by 2000 grid, which will be kind of like the way a texture
[147:23] is mapped. So now if I use this on a card, we can drop down a card geometry from here. We want to
[147:31] rotate this so it's flat on the ground. So I will grab the rotation gizmo here with E and I will just
[147:37] turn this around. We want to use here a value of negative 90. And we want to animate this noise so
[147:44] it goes across the ground from left to right. And if we go to the noise properties here in the transform
[147:51] tab, we can see which of these parameters we want to animate. So if I were to increase the
[147:57] translate on the x, let's maybe take a look closer. Now it's kind of hard to tell because
[148:03] we keep flickering this texture as we are previewing the changes. So the way that we can animate values
[148:09] inside of Nuke is we can add keyframes. So if I wanted to animate this translate x value, I can go
[148:16] to the beginning of the timeline, I can right click and set a keyframe. This will now show up on
[148:22] our timeline here. If I zoom in real close, let's maybe zoom in here, we can see that there's this
[148:28] blue underscore kind of thing. And this indicates that there is a we have set a keyframe. And now
[148:34] I can go to the end of our timeline at 1240 and I can increase this value. And if you have already
[148:40] a keyframe set, whenever you make changes to that value, it will automatically add a new keyframe. So
[148:46] now I can increase this value here. And we can see that this will add automatically a new keyframe
[148:51] for us. So now our, our noise is animated. So we can either animate values through keyframes. But in
[148:58] this case, since I want just a linear animation, I just want to increase this value over time, we
[149:04] can map it to our frame number. So let's go ahead and I'll get rid of the keyframes here. I will
[149:09] set this to no animation. Let's hit yes. And instead of setting keyframes, we can right click
[149:15] and choose add expression. And now I will simply link this to our frame number by typing here frame.
[149:21] And we can see we already have a result since we are on frame 1130. This will give us now this will
[149:28] output 1130. So if I hit okay, we now have this value here. And as I move forward in time, we can
[149:34] see that our, and by the way, I'm using the left and right arrow keys to move back or forward a few
[149:41] frames. So we can see that as I move forward, this value now increases. So if I were to zoom in here
[149:47] and just simulate or rather play the timeline and cash a few frames, we can see that this is the
[149:53] animation that we now get. So if we want to have this animation move faster, we can go back in our
[149:59] expression here, we can right click, choose edit expression. And if I want to make this twice as
[150:04] fast, I can do multiply two. So now we essentially doubled the speed, I can hit okay, I can preview
[150:10] this now. And we can see that this is now the animation. And also we are animating the noise in
[150:15] the correct way. Because like I said, we want to move from left to right, let's place this now in
[150:20] our 3d scene. So we can better judge what changes we need to make. So let's grab our camera. And
[150:27] also we can grab the scanline render as well. Let's copy this. And let's paste this over here. And I
[150:32] will connect the OBJ to our card. And if we go through our look through our scanline, we can see
[150:38] this because we still need to position this. So let's also preview our position to points node
[150:45] over here. Let's preview this and let's change the properties here to five. So we can preview
[150:51] multiple nodes. And if I go now to our card, we can see now that we have to bring this card way
[150:59] further back. So with w I will move this card, let's increase the uniform scale by quite a lot.
[151:05] And we want to cover at least the closest part of the ground. So the closest to our camera. So
[151:11] let's move this over here. Let's increase the size. We'll do something like this. So now this
[151:17] should probably look a lot closer to what we need. We can also maybe drag this up slightly. I do
[151:24] want it to intersect with our ground a little bit. This will give it this will help us to
[151:29] integrate our smoke more. And if I were to merge this from here on our existing chain so far,
[151:36] so I'll just drop down a merge and just put this over with an over operation. Let's go ahead and
[151:42] preview this. And here we can now see our smoke. So we are almost there. We still need to increase
[151:47] the size of our card. So let's go ahead and let's make this even bigger. Let's make this really big.
[151:53] So we cover some of this part over here towards the that's further away essentially from our camera.
[151:59] I might want to push this further out even but we can kind of start to get a feeling of what
[152:05] this will look like. And if I were to let's preview some let's cash up some frames so we can also
[152:12] have an idea on how fast this smoke is moving since we have this noise animated. All right. So
[152:19] I'm pretty happy with this. I think we will keep this speed as it is. And one more thing that we
[152:25] can do for our noise we can also evolve this noise over time. So if we go in the noise tab,
[152:31] this Z property over here, we also want to animate this over time. We can see how our pattern changes
[152:37] when we increase this Z value. So here we will do right click at expression and we want to map this
[152:44] to our frame value as well. So we will do frame only in this case we if I leave this at the frame
[152:51] value we can see that the animation will be really fast and we want to really lower this value we want
[152:57] to multiply it or rather scale it down by quite a big factor. So let's right click edit expression
[153:03] and let's multiply this. Let's say that we want only 10% of this or maybe even less. Let's do 0.05
[153:11] and let's see how this speed will look and probably this is still even too much. We can also
[153:17] right click and choose edit expression or we can select the value and press equal sign which will
[153:23] bring up this expression window. Let's do 0.01 instead. Probably this is even still moving too
[153:31] fast but actually I think this is this is a lot better. So if I preview this from our merged result
[153:38] over here let's cache a few frames. So now we have this result. It's looking pretty good. We might
[153:45] want to make this evolved speed even faster. Let's go ahead go back to our expression window. Let's
[153:52] do our final value here 0.02. So this should be fine. Now let's see if there's a way in which
[154:00] we can make our noise look a little bit more thin and a little bit more wispy. I'm essentially
[154:06] looking for kind of like sharp lines in between our pattern. So if we go to our noise there's
[154:14] different types of noise that we can use and let's use turbulence instead which we see now that it's
[154:20] a different kind of pattern and this will provide for us these thin wispy lines which we want but
[154:25] we want these lines to be white and the background to be black. So we want to reverse this. So after
[154:32] this noise we can drop down an invert node and let's make sure that this invert is going after
[154:38] the noise. So let's reconnect this. So we have our reformat our noise and then the invert which gives
[154:44] us this result and now from here we can go back to our noise and we will reduce the lecunerity a bit
[154:50] if we reduce the octase this will make our noise overall smoother. So in this case we do want a
[154:56] smoother result. Let's maybe use octase 4. Let's drop down the gain as well. Maybe let's increase
[155:04] the gamma in this case. We can kind of start to see our lines and after this invert we can simply
[155:10] drop down a grade and we can control our smoke this way. So now we are really starting to see
[155:14] the pattern that we are after. We can even reduce the gain here on this gray node and maybe this is
[155:21] still we are getting too much detail. We can go to our noise and we can reduce the octase maybe
[155:27] to a value of 2. So I think this is a lot better. Let's reduce the gain maybe. The gain will overall
[155:34] help us decrease some of the level of detail and probably the gamma is looking all right.
[155:41] Let's see how this looks from our rendered view. All right. So this is a lot better. This is exactly
[155:46] what I'm looking for these thin wispy lines. But now I might want to overall increase the pattern
[155:52] of this noise. So in our noise settings I will go to the size here and just increase this. Let's
[155:57] maybe make this an overall bigger pattern. So something like this and maybe I don't want this
[156:04] gamma to be this slow. I might want to push out the gamma and maybe just overall decrease the gain.
[156:11] Now I'm not going to spend too much time adjusting these values. I'll leave this up to you because
[156:15] I don't really want to waste too much time. Fine tuning settings here. But one final thing that we
[156:20] can do with this noise pattern. So we have this. Let's actually preview this from our gray node. So
[156:25] we have this pattern so far. We can now combine this with other noises. So if I do another noise
[156:31] pattern here let's use draw. Let's also format this to our 2k view. So we have the same noise that we
[156:38] started with. Now here we want to use this to multiply our existing results. So we can combine
[156:44] these two layer of noises now. I can drop down a merge node here and I can multiply our second
[156:50] noise. Let's set the merge operation to multiply and we can see let's maybe reverse the order so we
[156:55] can toggle off the A layer and we can see with this extra noise layer on top we introduce even more
[157:02] details. So for this second layer of noise let's maybe just increase the gamma and also I want this
[157:08] to be smoother so I will decrease the lecunerity. Maybe the size is pretty all right. I might want
[157:14] to try to overall just make this more smooth. Maybe let's increase the size slightly and we also
[157:22] want to animate this but just on the Z I think will be fine. So let's go ahead and press equals here
[157:28] and let's do frame multiply. Let's use the same value 0.02 which should be a smooth enough
[157:35] animation for us and if we preview now our texture from over here with this additional layer of noise
[157:43] we get something like this so that's pretty cool and we can preview this now from our actual comp
[157:49] and this is what we end up with. All right so I think this actually works pretty well. I might
[157:54] want to decrease the speed but again I will leave this up to you to decide what kind of values you
[157:59] want to use. I'm pretty happy with this result and we can see how easy it is to create our own
[158:05] elements even if we don't have access to like I said stock footage or pre-rendered elements.
[158:11] You always want to use pre-rendered elements if you have any but sometimes or maybe as a proof of
[158:17] concept you want to see if something like this could work and then you can you know send it to
[158:22] the simulation department and ask them to create an actual simulation of this kind of wispy smoke
[158:29] type of movement. So obviously something like this would look a lot better if it was simulated
[158:34] in Houdini but depending on how much emphasis a certain element has you might not need all of that
[158:43] detail and realism. We can see that when we combine this with our other elements this works
[158:48] just fine. At least as far as I can tell. Now to make this even more believable we will have to
[158:54] integrate it with our actual environment render and in a similar way to how we merged our smoke
[159:02] footage by using the depth as a mask we can use the world position as a mask in this case because
[159:09] we want our gradient to go from bottom towards top instead of from front to back. So I'll show you
[159:16] what I mean by this. We've covered the position pass a little bit when we were using it to create
[159:22] our position to points layer over here so this is only possible through our world position.
[159:29] Let's go ahead and we'll need a new shuffle that points to our render and actually we can just grab
[159:34] one of these shuffle nodes from over here. Let's copy this and let's paste this down below and again
[159:40] we will want to point this back to our render. We can go we might want to add another dot over here.
[159:46] So this dot points all the way to our environment render so from here I can just grab this node
[159:52] or rather dot and I can hold down shift and select my shuffle and then press shift y to create this
[159:58] forward connection. So now in our shuffle we want to shuffle. So here we will want to use our p pass
[160:06] so this is the world position when we select this we have a similar thing here we can see that we
[160:12] have sort of like the normal pass we have x y and z coordinates so in this case we are interested in
[160:20] the height we want to create a gradient on the height which means that we want to use the y
[160:26] value over here. If we wanted a gradient that goes across from left to right across our geometry
[160:33] we would use the x and on the other axis we can use the z but in this case we want to use the y
[160:38] for the height so we can plug this in our alpha channel and if I press a we can already see a
[160:44] little bit of this gradient so if I drop down a grade node and I use the alpha channel over here
[160:50] I can increase the white point if I wanted to increase this gradient so if I want to increase
[160:55] the spread essentially we can increase this so we can assume that if one of these buildings has
[161:01] in units a height of we can actually check if we were to go to our shuffle version over here if we
[161:08] look at this pixel value here we can sample this we see that it's 65 so this is 65 units and if I
[161:15] were to go to our grade node and set the white point here to 65 we will have we will essentially
[161:20] spread out this gradient across our entire building but we don't want to have a gradient that's really
[161:26] this spread out we want to tighten this up so we want to use maybe from 0 to 1 we want a very sharp
[161:34] gradient like this and we will use the offset like we did earlier to determine exactly which parts of
[161:40] our ground we want to isolate so in fact in this case I can even lower the white point even more
[161:46] just so I can filter out some of these pieces of rubble over here and I can decide exactly how I
[161:52] want to blend in our smoke layer so from our grade node here we can go to our scan line and let's
[161:59] preview the RGB and let's go ahead and do the same thing that we did earlier we can drop down a grade
[162:05] node from here we can point the mask to our other grade node that's linked to our position pass and
[162:11] now I will just set the gain value here to 0 and I want to run this over RGB channels as well and
[162:17] now here we have it we have successfully masked this smoke layer with the height of our geometry so
[162:24] if I were to disable this layer we can see very easily we can create this blend between our element
[162:32] that we created directly in nuke and our actual rendered geometry so this is really really cool
[162:37] and again we can go back to our grade adjustment here for our position and I can I can play around
[162:43] with the gamma if I want to tighten up this gradient we can decrease the white point even more or we
[162:49] can increase this if I want some of this smoke to spill over the rubble so I can just increase the
[162:55] white point as we can see here but in this case I want to pretty much obscure it by our piles so
[163:02] overall this is just another example of some of the stuff you can do and here we took it an extra
[163:08] step further by creating our own layer which we didn't have to import from an already existing
[163:14] footage of this smoke we created it ourselves with the noise and again we are really just
[163:20] scratching the possibilities here and in time as you experiment more yourself and as you watch more
[163:27] courses and tutorials you will have more ideas on how you can combine passes and how you can create
[163:33] your own layer so this will come naturally in time as you use nuke more and more so let's maybe just
[163:40] cache a few frames with this as well and see what we get but overall I can say that I'm pretty happy
[163:46] with it it's pretty believable again for this type of shot our main element is actually our character
[163:54] so we are not the I will not really focus on the specific ground fog layer that we created
[164:01] so it will only register as something that's going on in the background and it will just help us
[164:07] create more depth to our scene so with our elements with our smoke elements we added
[164:14] depth from front to back and in this way we are creating depth from bottom to top but we are more
[164:20] or less done with this extra new layer so we can go ahead and also do a backdrop here let's make this
[164:27] bigger we can name this one ground smoke or something like this let's make this darker and more or
[164:34] less we are pretty much done with the environment and with the next lesson we can start working more
[164:40] on our character so I will see you there now for the character we'll take a closer look at what we


### Foreground smoke & PostageStamp [164:43]
**Transcript (timestamped):**
[164:46] can do with our passes over here so with our shuffle the setup but first I would like to add
[164:52] one more layer of the same smoke element that we used in the environment in front of our character
[164:59] as well so we want to integrate this with a character let's go ahead and I want to show you a new node
[165:06] which is going to be the postage stamp node so essentially what the postage stamp is is just
[165:12] a connection to another to a different node in your chain so for example if I were to place down a
[165:18] poster stamp node and connect this to our smoke layer over here so to our read node we can see this
[165:25] poster stamp will create a thumbnail of what it's pointing to so it's really just a bridge between
[165:30] these two nodes it doesn't really do anything it just holds whatever layer you are pointing towards
[165:37] and this is great because for example if I wanted to change this smoke asset now so if I want to
[165:43] replace this render let's go ahead and let's maybe just replace this with our character render we can
[165:49] see that our poster stamp changes as well and this is particularly useful when you want to
[165:54] duplicate elements or you want to create sort of like a connection and this is also helpful when
[166:00] you want to keep things organized where you don't really want to rewire and bypass an entire kind of
[166:07] chain or rather network so essentially with a poster stamp node now we can let's go ahead and
[166:14] undo this so we can point back to our render with this node over here I can replace all of our read
[166:21] nodes with our other smoke elements which is essentially the same render so I can just rewire
[166:27] all of these other nodes to point to the poster stamp and I can get rid of this read node over here
[166:32] so now we can see that we have the same result if I look at this result over here we have the same
[166:38] smoke asset and again this is great because now again if I wanted to change this render so let's
[166:44] say that maybe for example I want to experiment with different kinds of smoke assets maybe I have
[166:50] different version of this render I would just have to replace this single read node over here and if
[166:56] I just replace this real quick with the character so you can see this we can see that our other
[167:01] duplicate changed as well and if I look at the result now this doesn't make any sense but now
[167:07] they are both pointing to the same render which is what we want so again I will undo this so we
[167:12] go back to the smoke and if I want to hide any wire connection for any node we can go over to the
[167:19] tab over here and there is this option where we can hide input so now when I click off of this node
[167:26] this will this wire will only show if we select the node which is really really helpful to keep
[167:32] things organized and you can do this with any node for example in this shuffle node I can go to the
[167:37] node tab over here hide input so now when I click off of it we hide the wire so again this is strictly
[167:43] an organizational technique we can also use the hotkey alt H so I will use this from now on when
[167:50] I want to hide a wire so this is alt H we can see it turns on and off this option so with our poster
[167:56] stamp node let's replace our third re node as well so it's all pointing to the same render I will
[168:02] press alt C on this poster stamp we'll bring this down below over here and again if I want to create
[168:07] a forward connection I want to connect my render to this new poster stamp I will select the render
[168:13] and I will shift select the poster stamp let's press shift Y and we create this forward connection
[168:19] and now we have this hide input turned on so when I click off of it we no longer see the wire and
[168:24] now I can rewire this render to our poster stamp and if we preview the result we have all of our
[168:31] nodes and we can very easily just change this single read node and it will update throughout the chain
[168:38] as well so now with this being done I want to add another smoke layer in front of the character so
[168:44] again I can drop down a postage stamp let's grab our initial read node over here shift select the
[168:52] poster stamp and then press shift Y to create a connection alt H to hide the wiring and here we
[168:58] have it so we can essentially merge this on top I drop down a merge with M we can place this over
[169:05] here and first of all we would have to format this in this case so in this particular case we no
[169:11] longer need to place this on a 2d card in the 3d system this will work just fine if we just merge
[169:17] this on top because this is super close to the camera and the core and the camera is orbiting
[169:23] render slowly this won't really make much of a difference if we just leave it as a sort of static
[169:28] render on top of our image or place it on a 3d card it's not gonna move that much so in this case
[169:35] we are just going to leave this as it is not use a 3d system at all but from here we see that our
[169:42] resolution doesn't match so we will have to do a reformat first of all and let's do a transform
[169:49] node and we can now position this so from our final result I will grab the transform and while
[169:55] selecting this gizmo we can see that we can move this around I can increase the scale here let's
[170:01] maybe increase this a little bit we can do something like this and I don't think we've used this
[170:06] transform node anywhere so far but this transform node is pretty self-explanatory you can scale
[170:14] things up and down you can move them around you can skew you can do all of the regular
[170:20] transform rotation so I'm sure you are used to working with something like this one thing happens
[170:25] here when we scale this up and we move it around we can see that we do have this bounds extended
[170:31] on our comp so now when we merge this over we are working with this resolution over here and we
[170:38] want to limit our elements only to the format size that we are actually using so our root format
[170:46] which is which is 1920 by 1080 so if you end up with stuff like this when you merge things over so
[170:52] this extended kind of bounds it's always worth adding a crop to your layers which will limit it
[170:59] exactly to the size that you are using so the root project format and this will make sure that these
[171:05] areas over here won't take any more computational power than it needs to because for example if I
[171:13] were to not have this crop node over here and let's disable this and I add a grade node or I do
[171:19] other operations and again let's disable this so when I do this grade node this will kind of take
[171:24] into account this extra space here around our image as well so it if you have a lot of elements
[171:31] that are not cropped this has the potential to slow down your comp so it's always good to limit
[171:37] the size of your layers to the actual format that you are using so we can see that right away we have
[171:43] a pretty decent result but we do want this to interact with our character so we can grab the
[171:50] depth map of our character to make our smoke interact with the character so with that being
[171:56] said we can grab a shuffle node let's copy one of these nodes and we will point this to our
[172:03] render directly so not we don't want the unpromoted version we will point this to our render and we'll
[172:09] bring this down and again we can just hide the connection of this wire if I press alt h on this
[172:15] node and now we will not see it unless we have this selected so from over here we here we have
[172:22] just the depth extra which is kind of like that unpromoted thing that we've talked initially and
[172:28] this is simply because I forgot to set up the depth width and the aliasing in this case for the
[172:32] character but this will be fine so if I want to use this now I mentioned that usually we place this
[172:38] inside the alpha if we want to use it as a mask so if I press a here we can see it but in this case
[172:45] we have to take into account all this black space around our character so I will place our depth in
[172:52] all of our RGB channels and I'll explain a little bit more in a second but now if I drop down a
[172:58] gray node and I keep this at RGB I can lower the white point to queezing the ramp and I can just
[173:05] push the offset in negative space over here until we should hopefully and let's make sure that we are
[173:12] not previewing the alpha so we are in the RGB view over here so if I push this in the offset value
[173:20] over here we can see how we can slowly start to isolate the parts of our character so maybe
[173:25] I want the smoke to ignore everything that's black on our character so we have this nice
[173:30] interaction so the problem when we do this as it is so far if I were to just use this in the alpha
[173:37] channel I will just show you this real quick so let's set the grade to work on our alpha right
[173:42] and if I press a we now have this alpha information if I were to drop down a grade from our crop over
[173:48] here and do the same thing that we did with our smoke earlier let's point the mask to our grade
[173:53] and let's set this to RGB and turn the gain all the way down to zero we can see what happens we
[174:00] let's do invert over here so we have this interaction with our character but it is cropped only to the
[174:07] alpha of our character as well and this is because if we just look at our grade information here and
[174:13] press a this is essentially the map where our smoke will be visible but we want the smoke to be
[174:20] visible in the entire region around our character so we need everything that's behind our character
[174:27] essentially to have a full value of one so we want this alpha channel to be white now the easiest
[174:33] way to do this is if we just use the RGB channels instead so in the shuffle I will again we want to
[174:40] shuffle this in the RGB channels and in the grade let's set this to RGB so if I press a to go into
[174:47] the RGB view we have the same result but now what I can do is I can drop down a constant and I can
[174:53] set the RGB values here to one and I can set this as the background of my character so if I press M
[175:00] let's point the B layer to our grade and then reverse this because we want the constant to be
[175:05] the background so the B layer and if I look at the result now we have exactly what we need so now
[175:11] we can actually point the mask to our layer but now that since we are using the RGB channel so we
[175:17] if I press A we only have the alpha of our depth and we want to use one of our RGB channels so in
[175:26] this case we can just use the red channels we can see that if I were to inspect the pixel values here
[175:33] if you look at the bottom of the screen here so if I were to sample a region we can see that all of
[175:38] the rg and b channels are the same value so really here in our grade we can either use the red green
[175:44] or blue let's just use red and now we see that we finally have the result that we are after and
[175:49] we can still go back to our grade node and we can push the offset and we can see this very nice
[175:55] interaction with our character so again we are doing the same thing and now I'm going to point
[176:00] the merge to this grade node and if I look at the final result we can now go back to our grade for
[176:06] the depth adjustment and we can push this smoke back into our character or have it be more in the
[176:13] back or in the front so we have this option to control exactly how this smoke interacts with
[176:18] our character so now it kind of feels like there's a little bit of smoke that's going in front of the
[176:22] character and and some of the smoke is going behind our character so we have this very nice
[176:27] interaction the reason that we didn't have to do this background trick over here for our initial
[176:33] smoke is because we had enough information from the environment to avoid this kind of thing so if
[176:40] we look at some of these alpha masks that we created here for example on our first layer if I press
[176:46] A we see that most of this background is already filled so our smoke being over here we didn't
[176:53] really need to create this kind of a flat background for these layers in order for this to work pretty
[176:59] nicely but for example over here on our second layer if I look at our second mask we can see if
[177:07] I actually look at the result we can see that this is actually cropped by the building so in this
[177:13] case we would have to do the same trick with the background but it doesn't really make much of a
[177:18] difference in this case but if I were to let's go to the RGB values here we can see that it really
[177:24] doesn't feel like the smoke is cropped around this building over here even though actually it is cropped
[177:31] we can see it this is what we are merging on top so we would technically have to do the same kind of
[177:36] trick for all of these layers so depending on what kind of a depth map you have you might have to do
[177:43] this or you might not for example if we had this character render if we had a depth layer that's
[177:50] that's including both the character and our environment we would probably not have to do this
[177:55] kind of trick over here but since we just have our character then we have to fill in all of the
[178:00] black space around the character as well so this will be all right for our smoke layer of course
[178:06] from here we can still drop down a gray node we can increase or decrease the gain we can also
[178:12] drop another gray node for the alpha specifically so I'll set the channel here to alpha maybe drop
[178:18] down the gamma or the gain make this more transparent so probably this works a little bit
[178:23] better we can still go back to our transform and reposition this smoke and let's maybe just
[178:29] cache a few frames and see if everything is lining up correctly and by the way if at any point you
[178:35] have an annoying gizmo like this on your viewer that you want to hide you can just press q and then
[178:41] you can see this turns the overlay to off and then we can with q we can turn this back on again so
[178:47] sometimes really helpful when you want to preview things quickly let's again just cache a few frames
[178:53] and see what we have all right so I'm pretty happy with this we have this nice interaction of our
[178:58] foreground smoke with the character so let's just do a backdrop here and we can call this let's call
[179:06] this fg for foreground so fg smoke let's do this let's make this another color here and we are pretty
[179:16] much done with our foreground smoke and with the next lesson let's take a look into some of the
[179:22] options that we have to really fine tune the look of our character so I will see you there


### Cryptomatte [179:28]
**Transcript (timestamped):**
[179:28] going back to our character setup we can see that if we were to grab a specific AOV we can
[179:35] do changes for that AOV or for that render pass but let's say that for example in the case for this
[179:42] reflection pass over here I really want to isolate a certain part of my character so if I look at my
[179:49] character as it is I really don't want this the blade of the sword to be as bright so it would be
[179:56] really handy if somehow from this pass I would drop down a gray node and I can gain this down but I
[180:03] only want to affect this part of the sword and this is where the crypto mats come into play so
[180:09] crypto mat is another kind of utility layer that you can use so we could go to one of these shuffle
[180:17] nodes and we can kind of see some of these crypto object passes over here which look something like
[180:23] this now this isn't really how you use crypto mats so let's go ahead and undo this for crypto mats
[180:28] since it's more of a special kind of pass we will need to drop down a crypto mat node and with this
[180:36] crypto mat node we can point this now to our render and we want to do this before the on premode so
[180:41] if we were to preview this it looks something like this it's essentially an id map of our
[180:46] materials so this will depend on how you set up the crypto mats in your render engine but in this
[180:52] case specifically I separated the materials so wherever we have a different material this will
[180:58] correspond to a different color and we can see that the blade has a different material the hilt has a
[181:03] different material our character has a few materials and now what we can do with this is if I want
[181:08] for example in our case we want to isolate the blade of the sword I can hold down control and I
[181:14] will click on this sword now we can see this blade turns yellow which means it is selected and if I
[181:20] press A we can see that this will now translate to our alpha channel so I can now go back to our
[181:27] reflection pass over here let's go into the RGB view and if I want I can drop down a gray node
[181:34] point the mask to this crypto mat and if I lower the gain let's preview the result from over here
[181:39] when I now lower the gain we can see that only the blade is affected we can preview this from our
[181:45] final result maybe and hopefully this will now show you the power of crypto mats it's something that
[181:50] you will most likely use in any kind of CG composite that you do so very very handy and
[181:57] let's go back to our crypto mat and in this case for the crypto mat we have to take into account
[182:02] we have to unremultiply this as well so if I press A we can go to the unremultiply and this
[182:08] will now get rid of the aliasing because all of these layers here which we are working on are
[182:13] unremultiplied so we will have to take it take this into account we can see that for example
[182:18] in this crypto mat if I were to turn off this unremult we kind of get different grading around
[182:24] our edges so again we have to take into account this unremultiplied business for the crypto mat
[182:30] we have to specifically unremultiply this here so let's maybe first try to organize things a
[182:36] little bit let's do something like this so it's a little bit cleaner so let's go back to our crypto
[182:41] mat and inspect some of our other settings here so while holding control I can select even more
[182:48] parts of our character and we can see that all of this will merge into a single alpha layer if I
[182:53] press A we can this is currently our option is set to picker add but we can remove if I set this
[182:59] to picker remove and now with control I can deselect objects and we can also see that as I start to
[183:05] add more objects we also have them here on our list so this is how they are separated this here is
[183:11] essentially our material path so this is really cool as well I can even deselect them if I were to
[183:17] just simply remove them from the list so I can also do this I can hit clear to get rid of all of
[183:22] the selections so it's pretty easy to use not really worth spending too much time here let's go
[183:28] ahead and just keep our blade selected go back to our grade we can just grade this down and this
[183:34] should be fine let's maybe go back to our render and also maybe I want to lower the intensity of
[183:40] this hilt here as well let's take a look at some of our other passes I might want to use a different
[183:47] kind of mask for this one here for example so I can just duplicate the crypto mat node with alt
[183:54] let's go ahead and connect this to our render as well maybe we'll bring this all the way over here
[184:00] and with this crypto mat let's clear and let's control click on the hilt we'll do a grade node
[184:07] for our shuffle let's point the mask to our crypto mat so now I can gain this down we can preview
[184:13] our results now let's enable some of these one by one and I'm pretty happy with this let's take a
[184:20] look at this layer specifically we might want to drop down a grade node here that points to the same
[184:25] sword alpha and we might want to gain this down let's preview this from over here we might want
[184:31] to lower this a little bit we can play around with the gamma as well and our final layer this looks
[184:36] all right and now if I preview the result this is what we have so if I were to disable all of our
[184:42] grading adjustment with the crypto mat we can see we can make very very specific changes probably
[184:49] this is too much I might want to bring back some of this reflection and specularity I might want to
[184:55] play with the gamma instead rather than the gain and we can do something like this we can always
[184:59] come back to this essentially what we are doing here is we are just setting up all of our options
[185:06] that we have so that later when we have all of the elements put together when we have everything
[185:11] set up we can come back and we can just pick each element and do any changes and adjustments that we
[185:18] need so this is just a very brief introduction to the crypto mat super super handy again I use this
[185:24] in all of the comps literally all of the comps because you will most likely always need to isolate
[185:31] certain parts of your render and you always want as much flexibility as possible we have a crypto
[185:37] mat on the environment as well if I drop down a crypto mat node we can see how the elements are
[185:42] separated here so if I wanted to affect just the ground I can select the ground and this will create
[185:47] this alpha mess for us and we can do specific changes just for the ground we could use this
[185:53] also to blend in our wispy smoke that's going across the ground so from here for example if I
[185:59] were to drop down a blur node with B and I just blur this a little bit this would probably be a
[186:05] fairly decent mask for our smoke but it's probably better to just use the position or rather the
[186:11] world position in that case but just to give you an example that you can really use this crypto
[186:17] layer in multiple scenarios now one other thing that's missing here on this blade specifically I
[186:23] this is a very basic material that I set up in Houdini it's really just a metallic surface with no
[186:30] detail on the surface and I specifically set it up this way in order to show you a way in which we
[186:36] can add some of this detail ourselves directly in yoke so let's do that with the next lesson


### STmap & Adding details [186:42]
**Transcript (timestamped):**
[186:42] I want to show you now a way in which we can add additional detail on our characters so really on
[186:49] any part of our character but especially this blade part which has this very smooth material we
[186:56] want to add a little bit of dust and scratches and let's see how we can do that by just using a
[187:01] simple noise so I want to introduce you to a new node which is called sd map and if we look closely
[187:08] this will take in two inputs here which is the sd map and the source now really all this sd map
[187:15] is doing it's going to map a texture to our uv coordinates but really it doesn't have to be
[187:22] uv coordinates it can be any kind of coordinates that go from 0 to 1 across the x and the y value so
[187:30] let me show you what I mean by this with a very simple example if I were to drop down a ramp
[187:36] and let's make this just a straight vertical ramp I will just offset this first point over here so
[187:42] it's at the top let's do something like this and let's duplicate this and with our second ramp we
[187:48] want to make an horizontal ramp so if I were to just make this real quick I'm just going to adjust
[187:54] this ramp so it's nice and horizontal let's do something like this it doesn't really have to be
[187:58] perfect but now essentially we can use these as our coordinates so if I were to plug the sd map
[188:07] if I were to point this to our ramp and as a source for now let's just use a noise texture so we will
[188:14] use the noise from this draw category over here again it's the same noise pattern that we kept
[188:20] using let's point the source to our noise and when we go to the sd map let's now set the uv
[188:27] channels this is the most important option so the uv channels let's set this to rgb and now what
[188:33] happens is it's essentially going to look at the red and green values of this ramp and this is how
[188:40] our noise will be mapped but since our ramp only has values so if we inspect our pixels here we can
[188:47] see really that we just have this 0 to 1 value across our x dimension and we also need it on the
[188:55] y so from our ramp I will do a shuffle and I will disconnect everything except the red channel here
[189:01] so I will disconnect the green and the blue so now we just have if we look at the pixel analyzer here
[189:07] we just have a value that's going across the red channel that's going from 1 to 0 essentially so now
[189:14] I want on the green channel to introduce our vertical ramp so I will point this a layer here
[189:21] from the shuffle to our ramp this is our vertical ramp that we created earlier and in the shuffle
[189:27] node let's set the input here to a so our second row over here and from the a layer I just I will
[189:34] populate this with the rgb channels and I will grab the red channel we can grab any of these
[189:39] channels it doesn't make a difference but I will grab the red channel in this case and I will place
[189:44] it in our green channel in our outputs so we have successfully combined our ramps we have a value that
[189:50] goes from 0 to 1 on the green channel vertically and we have a value that goes 0 to 1 on horizontally
[189:58] on the red channel and now when we go to our ST map we have both the x and y coordinates and we can
[190:04] see that our noise is mapped properly now here for the best results as well it's better if we use a
[190:11] square texture so this noise over here let's drop down a reformat and let's set this to a 2k
[190:18] texture so square 2k will point the noise to our reformat so now we have this nice square texture
[190:24] and it doesn't have to be a noise we can for this example we could use a scratch texture but just to
[190:31] keep things simple we can use the noise and I also want to show you the versatility of this noise
[190:36] layer so now if we go back to our ST map we have this noise map to our coordinates and for example
[190:42] if I want to grab this ramp we can clearly see how this works if I were to adjust this ramp if I were
[190:48] to squeeze in this value a little bit we can see now how this changes our ST map so while I have this
[190:54] ST map previewed let's go to our ramp and I can show you how our texture gets mapped or rather
[191:00] remapped in real time and we can do the same with our other so our vertical ramp now as we do this
[191:07] we can see that the texture is not really tiled so it's a little bit different from a 3d app most
[191:13] 3d applications will tile the texture by default there's ways that we can kind of force this
[191:19] tiling to occur but I don't really want to get too advanced on this topic this is just to demonstrate
[191:25] how this ST map basically works so obviously instead of just creating our ST map ourselves as we did
[191:34] over here we usually bring over the information from our AOVs so in this case let's go ahead and get
[191:41] rid of this ramp thing over here and we'll grab one of our shuffle nodes let's copy and paste this
[191:47] and we will probably want the un-premulted version so we can point this shuffle all the way here and
[191:54] let's rewire this and bring this over down below we'll do something like this I think we went the
[192:01] long way around we probably could have done something like this so maybe this makes more sense
[192:07] again this just points to the un-premulted version of our render so from this shuffle now we can bring
[192:12] in this is going to be called this UV extra so we can see again the same red and green kind of business
[192:20] so if we use this as our ST map again in our ST map we can see now our noise being mapped over here
[192:27] just make sure that the UV channels are pointing to the RGB if in your UV extra if this ST map was
[192:34] pointing directly to our render we now have to set the UV channels to look for our layers specifically
[192:41] so from the other layers here we can choose UV extra to get the same kind of thing but I think
[192:46] it's more intuitive and more in line with the way that we've worked so far if we were to point this
[192:53] to our shuffle and we use the RGB channels instead because essentially this shuffle outputs an RGB
[193:00] value so this is why we have to set this here now we have a little bit of a weird issue we can see
[193:06] that in some places like over here the noise is working fine but in some places it's stretched
[193:12] and this is because really the UVs are messed up if your model has proper UVs you won't run into
[193:19] this problem but in this case the UV on the sword is not very great and this is why we have this
[193:24] stretched thing now we can kind of fix this a little bit if we modify this UV coordinates so if I
[193:33] drop down a gray node I will set this the channels here I just want to work with our red channel so
[193:40] I will deselect the green and blue and now when we make modifications with this gray node we will
[193:45] only affect the red channels and this is easier to see if we preview directly from our ST map
[193:51] so by adjusting the gamma on our red channels we can see we might be able to sort of squeezing the
[193:59] texture a little bit to sort of compensate for this stretchiness and we can do the same thing
[194:05] with another gray node I will set this to only work on our green channel and we can again play
[194:10] around with the gamma so we get so we kind of try to sort of skew the results in our favor we can
[194:19] also play around with our black point and white point when we do this kind of modifications we
[194:24] can see that at some point if we mess things up we end up with this problem where our texture
[194:31] gets stretched so maybe in this case we just want to mess around with the gamma now because we are
[194:36] using a noise texture we can also just go to our noise pattern here and in the transform we can
[194:42] go to the scale and we can split up the values in width and height in this case so we can maybe
[194:49] lower the width and we can see now that we can pretty much also fix it in this way as well now
[194:57] let's go back to our noise and we can play around with the size we can make this a little bit smaller
[195:01] we can increase the gain and maybe decrease the gamma now it's worth just seeing this as our final
[195:08] result let's go ahead and try to merge this with our character now I'm gonna place this
[195:14] scratch detail over here after all of our combined shuffles technically you should place it per each
[195:23] individual shuffle so when you add a roughness texture this would affect the specularity and the
[195:28] diffuse in different ways so you would have to spend a little bit of extra time if you really want
[195:33] to get super specific but if you want to just have something done fairly quickly we can just
[195:39] place this after all of our combined shuffles now if we were to do a merge from here over our entire
[195:45] character this is obviously not what we want and I will set this operation here let's set this to
[195:50] screen so first of all I want to limit this to just our blade and we have our crypto mesh so we
[195:57] have the alpha mask from our crypto mat over here with just our blade and on our merge node we can
[196:04] just specify this blade mask as our mask so I'll grab the mask from over here and let's point this
[196:11] to our crypto mat so this takes care of one part of our problem and the other part is we do want
[196:17] to integrate this texture slightly with our actual render so a very easy way to do this if is if we
[196:24] just multiply our result from over here so our final merged result of the shuffle let's drop down a
[196:31] merge node on our ST map and we'll point the other layer to our merged result and let's go ahead over
[196:38] here instead of operation to multiply so now it's going to pick up the colors and the highlights from
[196:43] our render and it will create for the most part a pretty smooth and seamless result as we can see
[196:49] over here if I were to bypass this multiply this is the result that we get so with just a few simple
[196:56] tricks and with our ST map very very easily we can create a nice layer of dust and scratches
[197:03] with a simple noise pattern obviously this might look better if we were to use an actual
[197:09] dust and scratches texture which you can find plenty online but I think it works fairly well with
[197:16] a noise as well I really like to spam these noise textures throughout all of my comps usually so if
[197:24] we preview the final result as well this is with our dust now probably this is a little bit too much
[197:30] we can always just gain things down let's add a grade node after the multiply here and we can just
[197:38] maybe gain this down make this not as obvious we can still play around with the noise but I think
[197:44] this is looking pretty fine as it is so if I were to enable and disable this very easily we can add
[197:50] this extra detail on our sword especially since this is pretty close to the camera we don't really
[197:56] want this very smooth material kind of looks like a fake CG from the 70s so this is just an example
[198:04] on how you can use the ST map in your workflow now really with this ST map you can push this in
[198:09] multiple different ways you don't really just want to use this to add extra details on your renders
[198:15] you can really do some crazy stuff and we'll take a look at an example later as well but for now
[198:22] let's keep things as they are and let's maybe start to organize our character setup here I might want
[198:30] to actually maybe we can hide this connection from our shuffle here with the extra with the UV extras
[198:37] so I will press Alt H on this dot and now we no longer see this and we also I might want to hide
[198:43] this connection as well or try to make this at least a little bit cleaner so this whole thing
[198:49] over here let's do a backdrop and this can be our scratches let's do scratches sword and over here
[198:58] the rest of our nodes maybe make some room everything else over here can be our let's do
[199:06] backdrop and this will be our beauty recreate or rebuild beauty so we'll do rebuild beauty and let's
[199:14] maybe make this darker and now we can move forward with the next lesson for the following lessons we


### Nuke survival toolkit [199:18]
**Transcript (timestamped):**
[199:20] are going to be using some nodes or rather gizmos that aren't directly available with the new
[199:26] installations so these gizmos are created by the community and we can find them on new copedia so if
[199:34] we go over real quick on new copedia this is it and here we can see it says right here in the title
[199:40] over 1000 free tools for foundries nuke which means that all of these gizmos that we can find here are
[199:47] free so these are made by the community and really this is one of the major strengths that nuke has
[199:55] over maybe a similar compositing tool like fusion because some of these nodes are incredibly powerful
[200:04] some of these artists that contributed to new copedia really created some amazing gizmos and I
[200:11] will encourage you to go on new copedia and check out some of these gizmos you can check them by
[200:16] categories we can see here if we go to downloads we can choose gizmos and then we have a bunch
[200:22] of categories here so most of these are actually really useful because they serve a specific
[200:28] requirement in compositing so every gizmo that's created here is created essentially out of a
[200:35] necessity so these are pretty much all of them are extremely useful which brings us to the next
[200:42] subject here which is that a few people put a bunch of these nodes together all of the most
[200:47] useful gizmos from new copedia they put them together and this is where the new survival
[200:52] toolkit comes into play so this is a free tool that contains all of these free gizmos when you
[200:57] install this it will install all of these gizmos automatically so you don't have to do anything
[201:02] manually and it really contains a lot of powerful stuff so over here where we have the toolkit
[201:08] documentation we can take a look real quick and we can see in the menu over here there is all of our
[201:15] nodes laid out and we also have some examples and a very short description on each of these nodes
[201:21] and we can see that we really have a lot a lot of gizmos and all of these are extremely useful so
[201:27] all you have to do really is go to this link and here we also have an intro in installation video so
[201:33] I will really recommend installing this if you plan to do anything in yoke you will 100% need
[201:39] this toolkit so with that being said we are going to be using some of the nodes that are gizmos that
[201:46] are available in this toolkit going forward with the next lesson so go ahead and install this and
[201:51] I will see you in the next lesson and now with this lesson it's finally time to talk about one of my


### Glow [201:53]
**Transcript (timestamped):**
[201:56] favorite subjects and one of my favorite things to do in compositing which is adding glow now adding
[202:02] glow can be a fairly simple subject and an easy thing to do but it can be pretty tricky to do
[202:09] properly and to get it right so usually we want to add glow on emissive objects and in our courses
[202:17] and in my work in general this happens all the time because I always have a magical particle layer
[202:23] somewhere and that's usually with an emissive material so it's nice and bright and it's usually
[202:28] the element which I want to focus on so it's really a no-brainer to add glow to that layer
[202:34] and in this case on our original render here on our read node we have an emissive material on the
[202:42] eyes of the character specifically and on the edge of our blade over here and this is we can access
[202:50] the emissive AOV for this specifically so from our shuffles over here there is an extra shuffle
[202:57] in the case for our character which we didn't have in our environment render which is that direct
[203:02] emission so we want to bring in this shuffle over here probably after our foreground smoke
[203:09] so let's go ahead and instead of creating a big wiring from our render over here we will use the
[203:18] poster stamp node which we used earlier so let's drop down a poster stamp we'll grab our render
[203:24] and in this case we we are not really interested in the pre-multing or un-premulting in the case for
[203:30] glow so we are just going to grab the render let's go ahead and shift select this poster stamp
[203:36] press shift y to create a forward connection and then press alt h to hide the wiring so from here
[203:42] this is essentially like a new read node and let's drop down another shuffle and we want to bring in
[203:49] let's take a look we want to bring in our direct emission so we can see that this is going to be
[203:55] our emissive materials from our character and technically to actually recreate the beauty
[204:01] pass we would just have to merge this on top again as a plus operation so to recreate what we had
[204:08] we can do a plus over here and now we also have this emissive AOV and this is where we want to
[204:15] focus our glow on now the naive approach will be to just add a glow so this regular glow comes with
[204:25] nuke by default so this would be sort of like the default glow and if we take a look here we have
[204:31] some options but let's maybe just increase the size so we can spread this but we can see that
[204:37] obviously this doesn't really look all that great if I were to enable and disable this it's essentially
[204:44] we are just blurring the layer itself and plossing it on top so this default glow is pretty trash I
[204:52] will not really recommend you to use this under any circumstances if I wanted to just spread out
[205:00] or blur out the image to create kind of like glints or something like that I would just use a blur
[205:05] instead so with that being said let's go ahead and get rid of this and we will use one of our
[205:11] glows from the survival toolkit so make sure that you have installed the toolkit and if I do tab we
[205:17] can do ap glow and if you've taken any of my other courses before you will be more than familiar with
[205:25] this node with this glow this is a glow that I use all the time it's my favorite exponential glow
[205:31] and we can see already just with the default settings we get a really really cool result and
[205:36] if I were to just plus this on top as it is we already have well not exactly but if I were to
[205:43] increase the intensity here we can start to get some really really cool results the reason that
[205:49] this glow is better is because this is an exponential glow and with the toolkit we have an expo
[205:56] expo glow as well so this is another type of exponential glow made by somebody else and this
[206:02] is also pretty good as well let's maybe increase the size over here or let's increase the intensity
[206:08] and increase the size and the difference between these nodes and the regular node is if I were to
[206:14] demonstrate this with a simple ramp when we do our normal glow it has this linear fade but light in
[206:22] real life has an exponential decay to it so really what we are interested in if I add a great node
[206:29] and I increase the gamma this is the kind of decay that we want so we don't want a linear decay we
[206:35] want the objects to be super super bright right around their surface and as the light propagates
[206:41] through the scene it starts to decay very very abruptly so we are kind of looking for an exponential
[206:48] ramp over here so if I were to increase the gain this is more or less what the ap glow will do for
[206:53] us and this is why it looks so good and it looks a lot more natural and and again I will really
[206:59] recommend it you reframe from using the standard new glow which again it's really just a glorified
[207:05] blur that's that's plus on top of the layer now if we wanted we could just leave this as it is and
[207:11] we can see that this looks pretty cool and this would be sort of the more beginner approach we
[207:17] could keep it as it is but I want to show you some ways in which you can just add a little bit more
[207:23] detail a little bit of layering to this and how you can get more control and make this slightly
[207:28] more realistic so let's go ahead and I will disconnect this from now let's maybe and the first
[207:34] thing that I want to do is I want to separate the layers for the eyes and for the sword so let's go
[207:42] ahead and from my shuffle let's drop down a crypto mat and let's point the crypto mat to our render
[207:49] we'll select our sword or actually we can see that we just have to select this sore glow over here
[207:55] so I will get rid of the blade selection so we just want this edge thing over here and now from
[208:02] my shuffle let's go ahead and if I want let's drop down a merge and I want to introduce you to a new
[208:08] operation here which is in so if I set this operation to in and I point the b layer to our
[208:14] crypto mat we can see that our rgb channels this thing over here will look at our alpha from the
[208:20] crypto mat and it will sort of use it as a mask so now when we look at our result we just have
[208:27] the edge of our blade and we can do the same thing for our I'm just going to grab all of these notes
[208:33] press lc to duplicate let's link them up to our render and over here in our crypto mat let's clear
[208:41] selection and let's let's just grab our head in this case so when we look at our merge here we just
[208:47] have our eyes so we have our sword over here and our eyes over here and we can do some custom
[208:53] things for both of these when we add these back together so if I drop down a merge and plus
[208:59] these both together we have from here the same result that we had initially so when we preview
[209:04] this from the glow this is what we had but now essentially I can go over here so where our sword
[209:11] is I can drop down a grade note and if I drop down the gain I can affect the overall glow of our
[209:16] sword without affecting the eyes as well so now I can drop down a grade here for the eyes and I can
[209:23] increase the gain we can see that this direct emission layer is a little bit messed up in how I set
[209:30] it up because it also brought a little bit of the helmet as well this is to do with the material
[209:36] assignment is not really correct so from our shuffle over here where we bring the direct emission I
[209:42] will drop down a grade and I will just bring the gamma down so we are just isolating our eyes and we
[209:48] can see the difference with and without so now our let's go to our AP glow we are ignoring the part of
[209:55] our helmet so we have individual control now both for the eyes and the sword which is great let's maybe
[210:02] go to our sword and increase the gain here slightly but what I want to do is maybe break up the source
[210:09] for the emission for this sword so meaning that before we run our AP glow on our sword over here
[210:18] we might want to break this up with a noise texture I usually want to avoid really large areas where we
[210:26] have this sort of flat color even though in reality it would work something like this I kind of want
[210:34] to break it up I want to add just a little bit of detail and in this case we can we can either use
[210:40] the ST map technique that I've shown you earlier but I think we can just get away by adding a noise
[210:46] layer so let's drop down a noise over here and let's just simply multiply it with our sword so I'll
[210:54] set operation here to multiply and we can see we have this very nice breakup in our this affects
[211:00] also the color but also the intensity so now when we go to our AP glow we have this really nice
[211:06] variation in our glow so you always always want to think about ways in which you can break up your
[211:13] layer so with this noise selected I can reduce the size of the noise and maybe I can increase the gamma
[211:20] we just want a little bit of this breakup so I think this is looking fairly good we can
[211:27] plus this whole thing on top of our comp and another thing that I usually like to do with this kind
[211:33] of glow layer is I want the actual emissive object to be a fairly desaturated close to white color so
[211:42] when we add a glow on top it will really feel like it's this super hot kind of thing and let me show
[211:49] you what I mean by this if from our plus operation over here I were to drop down a saturation node
[211:56] let's go ahead and I will set this all the way maybe to zero or something like this if I were to
[212:02] merge this with our AP glow and set the operation to plus if we preview our final result now this
[212:08] is what we get and we can see that with this extra layer on top we can really get more of a feeling
[212:14] of our emissive elements being super hot and we can see this on the eyes as well and if we now
[212:21] isolate our glow layer it looks something like this so again this is fairly good and one more
[212:28] thing that we can do here is we can break up the glow layer itself so if we think about what would
[212:34] happen in real life is this because we essentially have a really atmospheric and smoky scene some
[212:42] of that smoke would break up our glow so we want to replicate this breakup again with a simple
[212:48] noise pattern we can just copy this noise that we already have let's paste this over here and we
[212:53] want to multiply this over our AP glow result so if we do this let's set this to multiply we see we
[213:00] get this really really cool breakup in our glow and this is again one of those things that will
[213:05] help us solidify our comp and actually add more depth and layering to our effects I will also drop
[213:12] down a gray node here and I will push the gamma out maybe we don't want this to be as harsh we
[213:18] want this fairly subtle thing and for our noise we can also animate this on the translate y over
[213:25] here we'll make this move and here I will press equals to add an expression again what we did
[213:30] earlier let's do frame and let's just leave this at frame and see if the speed is all right okay
[213:37] maybe we can make this faster let's do frame multiplied with two maybe even more let's do
[213:44] multiplies three and we also want to go in the noise tab here and add some value on the z
[213:50] channel here so here we'll do frame multiply maybe 0.02 and let's see how this progresses so
[213:58] something like this I think it's fairly good you could also instead of this noise you could also use
[214:05] one of these smoke elements to break up the glow but in this case it might work better with just
[214:12] a simple noise texture that's animated so if we were to cache a few frames here just on this glow
[214:17] channel we can take a look all right so okay so I think this looks pretty good and again this is one
[214:23] of those subtle things that will help us really bring our shot and make it feel more alive so if
[214:28] I were to preview this from our final result here maybe I want to overall increase the glow here in
[214:36] the and here in the ap glow settings feel free to experiment with some of these values we can make
[214:42] this more contrasty or we can flatten this a little bit let's maybe increase the persistence
[214:47] and this will be completely up to you and also you can see here that the color is blue and in the
[214:52] final render that you've seen the color is orange so we can very very easily change this if we were
[214:57] to go to our shuffle notes over here we can drop down a grade after the shuffle and inside this gain
[215:03] here we can just reduce the blue channel and increase the red slightly maybe reduce the blue
[215:09] channel even more until we get exactly the color that we want we might want to bring the red channel
[215:16] up and we can see how very easily we can go from blue to orange and this speed of iteration is again
[215:23] why nuke is so powerful and we can just pretty much copy and paste this note over here for our eyes
[215:30] as well and for our eyes for example we can maybe push the reds even more we can drop down overall
[215:37] the gain here for the eyes and we can see the amount of control that we have so I'm pretty happy
[215:45] with this we can go ahead and call this glow layer done so we can do a backdrop here as well
[215:52] and we'll name this one let's do glow make this darker desaturated and maybe finally I will just
[216:00] maybe increase the intensity even more we'll do something like this we'll probably have to come
[216:05] back to this layer as well and readjusting so it's not worth spending too much time now now this is
[216:11] really just the first part of setting up our glow layer and in the next lesson we can take a look
[216:17] at the second part so just setting the glow on the emissive objects is only one part of integrating


### Glow bounce & Relight [216:18]
**Transcript (timestamped):**
[216:23] the glow with the scene the second part is we have to take into account what would happen in a
[216:29] real-world scenario so even in 3d if we were to have this very bright super emissive object in our
[216:37] scene a lot of this light from this emissive material will spill over to the other parts of
[216:43] our render in this case we are mostly concerned about the character because our maybe a little bit
[216:50] would spill onto the ground as well but the ground is pretty far from this tip of the blade or rather
[216:55] the edge of the blade so we are mostly concerned about some of this light reflecting and bouncing
[217:01] on our character as well now obviously this would be better than directly in 3d usually with the AOVs
[217:08] you can split up the direct emission you can have the direct emission as a pass that isolates these
[217:14] emissive parts and then you would have the indirect emission so the contributions of that
[217:19] emissive material onto the other parts of the render but in this case let's say that we don't
[217:24] have this and in fact we don't so we want to add this global illumination or glow bounce ourselves
[217:32] and we can do this by using the real light node so this is the next node that I want to show you
[217:37] this is a super powerful node it has the potential to completely alter a render and give you the most
[217:44] amount of flexibility so we will place our glow bounce after our scratches for the sword over
[217:51] here I'll grab these setups and I'll just drag this down below and let's also drag down our viewer
[217:58] and let's place down over here a real light node now over here we are looking this will
[218:05] populate with multiple different wirings in a second but first we will have to specify the
[218:11] color which is really this should point to our render and then we'll have these lights which
[218:16] will look in a second so first of all let's go with this color we might want to just bring our render
[218:23] again over here with a poster stamp so let's drop down a postage stamp let's bring our render
[218:30] before the primald and we will shift select the poster stamp shift y and then
[218:36] alt h to connect or rather hide the wire so now this color can point to our render and in the
[218:43] real light let's set some test settings here the normal vector should look at our normal pass so
[218:48] I will set this to n and our point positions should point to our world position which is this p layer
[218:56] and now in our lights if I were to add a light here let's drop down a light and let's add this
[219:03] to our lights in our real light we currently don't have anything and I have the properties value here
[219:09] set to two let's maybe set this back to one so we currently don't see anything and now we can see
[219:15] that when we add the lights we have a new arrow over here showing if I drag this over we can see
[219:22] that we are also now requiring a camera so let's go to one of our camera nodes let's grab this one
[219:29] it's the same camera that we kept using let's paste this over here and let's point the cam to our
[219:35] camera and now we have one more arrow we this is now looking for a material so if I do tab and type
[219:42] here material we can apply a basic material there's also a specular there are multiple materials
[219:49] that you can use but the basic material will do just fine so let's point the material to our material
[219:55] and now we can kind of see something if I were to grab the light and I use the translate coordinates
[220:00] here to move this around we can kind of see how this affects our character which is super useful
[220:06] so this works exactly how it would work in 3d we can just move a light across our scene and it will
[220:12] affect all of the objects that we have in the scene we have some other settings that we will look to
[220:17] in a second but essentially now what we can do to preview this in 3d we can grab another position
[220:24] to point node let's point this to our render and if I were to preview this let's set the surface
[220:31] point here we'll set this to p and our surface normal let's also set this to n so now we also
[220:38] bring in the normal information as well and let's set let's increase this number of properties that
[220:45] we can preview here to five because we are working with this 3d view and essentially now if I wanted
[220:51] to merge multiple objects multiple 3d objects in the same scene we can use a scene node let's drop
[220:59] this here and I will point this to our position to points and the second one to our lights and we
[221:05] can also bring in our camera as well if we wanted to we can grab this and also bring in our camera
[221:11] and now we can see that everything is merged and this basically means that the light that we placed
[221:16] for our real light over here can interact with the objects in our scene so if I grab the light I can
[221:22] now just simply move this in 3d space and we can see how it affects our character let's grab the
[221:29] light I'll place this down below we will want this to be roughly where our sword is so let's do
[221:35] something like this let's I will set the falloff type here let's use quadratic which is going to be
[221:42] this exponential decay that we talked about so this will give you a more natural or rather
[221:48] more physically accurate result and we can increase the intensity we can see this over here and now if
[221:54] we go to our real light and press tab we can also see this how it affects our character now we have a
[222:00] small problem here with our sword but let's not worry about this for now in our real light we also
[222:06] want to turn on use alpha to get rid of some of this problem here with our edges so it's kind of
[222:12] like the pre-mult version and now with our light let's maybe just reposition this we can also play
[222:20] around with the translate direction over here directly we might want to I kind of want to skew
[222:26] this a little bit even though it's not going to line up perfectly with our sword I kind of don't
[222:32] really want to brighten up the character that much I will want to move the light a little bit
[222:38] more around and we are doing here some very creative choices so you can see now that if I were to
[222:43] look to the 3d scene our light is really all the way over here and our sword should be emitting
[222:48] light from over here but this is again one of those advantages of doing this in compositing
[222:55] that we can do these kind of offsets and sort of try to work reality in our favor so let's
[223:02] select back our light and we can see that from here if I were to use if I were to bring the light
[223:09] where our sword is this is more physically accurate but this looks better and it will still make it
[223:16] and it will still make our scene feel like this glow is integrated we can also see what happens if
[223:22] I play around with the y value so I might bring this up I might bring this let's maybe lower the
[223:30] translate x and maybe we can let's actually bring this further out so it's so our character is not
[223:36] as bright and we can do something like this so we still have to take the sword into account but
[223:42] we'll worry about this later let's for now leave this as it is and we'll bring this over here and
[223:48] we want to merge this on top of what we have and we'll set the operation here to plus and now we
[223:54] can set the properties here to one so this is the result that we have and if we preview this with the
[224:00] glow we still need to color correct our real light notes so from over here we can drop down a grade
[224:07] and we can first of all try to increase the contrast here if I were to decrease the gamma let's leave
[224:13] this as it is because we still have to talk about the material a little bit so in this basic material
[224:20] we have a few options here we can increase the diffuse we can increase the specularity so these
[224:25] are kind of self-explanatory feel free to play around and see if you get something that works for
[224:31] you I will set the specular here roughly to zero and I just want to use mostly the diffuse value
[224:37] here and not so much the specular maybe I can bring down the diffuse we should probably preview
[224:44] this from our final result and let's go back to our basic material here and maybe increase the
[224:50] diffuse a little bit and now with our grade node I can drop down the gamma let's do something like
[224:56] this and we'll add another grade node which we will use to color correct so I will split up our
[225:01] color wheel here let's increase the red channel and decrease the blue channel so we have our
[225:07] orangey kind of look that we have on our blade all right so now this will fit with our blade and we
[225:14] can see that with this bounce layer on top now it it should really feel like our glow is solidified
[225:21] in our comp this is overall maybe too much we can go back to our basic material and drop down the
[225:27] specularity a little bit let's go to our grade and maybe decrease the overall brightness we want
[225:34] something just a little bit more subtle but we can see even with something subtle this all of these
[225:40] small detail and all of these levels add up to our final result so you always want to think how
[225:48] the elements that you are adding or rather the new elements that you are adding to your comp you
[225:53] always want to think how this interact with the environment that you already have so for example
[225:58] if this character was standing on a on water or something we would have some puddles on the ground
[226:06] we would have to think about how these elements interact with those puddles so we will need to
[226:11] fake some reflections and maybe reflections as well and all of these are things that you pick up
[226:17] along the way as you are doing more and more compositing now with our relight we are completely
[226:23] ignoring the sword and to kind of fake a little bit of this bounce on our sword as well we can just
[226:29] bring our character render from over here so after our pre-mult let's go ahead and from this
[226:38] pre-mult let's bring a crypto mat on our render to isolate the sword and we'll control click the
[226:45] sword and now we can do we can do a merge between this crypto mat and our render over here let's do
[226:52] A to B so we can use the in operation and we are just going to mask our sword with this crypto mat
[226:59] let's also drop down a saturation and make this completely black and white and then we can just
[227:05] merge this with our relight over here and set the operation to plus so now let's take a look at our
[227:11] grade node and our other grade so if we look at our final result we also have a little bit of
[227:17] bounce lighting on our sword we can still drop down a grade node after the saturation here and
[227:22] maybe I want to increase this gain here and this will be up to you to decide how much you want some
[227:28] of this bounce on the sword specifically and let's take a look one more time I'm pretty happy with
[227:33] this result and we can leave this as it is for now let's maybe drop down another dot over here
[227:41] and we'll do a backdrop so this will be our bounce well let's call this glow bounce glow bounce
[227:49] lighting but let's just leave this as a glow bounce let's set this to a darker color now this
[227:56] bounce affects our character but really it should affect the smoke as well especially since this is
[228:02] a very thin kind of smoke the light would naturally propagate quite a lot through this thin layer of
[228:09] smoke and let's look for our foreground smoke over here and this will be a little bit more simple
[228:15] we'll just do this with a simple radial so if I were let's maybe just make some room over here I can
[228:21] drop down a radial which I can place over here or across our smoke so this radial is just a simple
[228:29] circular mask with fading let's also drop down a blur node with B and I will increase the size here
[228:35] to kind of blur this out a lot more and we can simply use a gray node and let's point this to our
[228:42] radial here so the mask and with this gray node I can now go to the gain here and just make this
[228:48] more orangey around this masked area of our smoke and now if I were to preview the result we also
[228:55] have this nice lighting direction with our smoke and we should probably make this a little bit
[229:01] brighter as well so you can either adjust the gain or the multiply the gain and the multiply are
[229:07] essentially the exactly the same thing so with this multiply on the same gray node I can just
[229:12] increase the overall brightness of our colors so let's take a look and I'm pretty happy with this
[229:19] result and one final final thing that I want to add with our glow with all of the glow layers and
[229:25] the glow bounds I want to add a slight flicker to this glow just to introduce even more life to our
[229:33] scene and have this very subtle thing that's not really going to be obvious but it's something that
[229:39] we can sort of feel and let's go to our glow over here and what I want to do is drop down a gray
[229:46] node and maybe I'll make some more room I will use this gray node and I will set this gain all the way
[229:53] let's set this to 0.5 and now I can use this mix value essentially as the strength of this gray
[230:02] node we can see that if this was zero this lower gain value will not be taken into account and as I
[230:08] increase this we kind of we essentially increase the strength of this gain setting over here so
[230:14] we can see that as I play around with this mix value we kind of create the flickering that I'm
[230:20] after so instead of setting keyframes on this mix let's go ahead and right click and set a
[230:26] rather add expression here so in our noise layers we use the frame value to help us create an
[230:34] expression and another value that we can use here will be random so if we type here random in between
[230:41] parentheses we will have to specify we can see that if I just leave this as it is it will already
[230:47] output for us a result but we will want this random number to change for each frame so in between
[230:52] parentheses as an argument we will type here frame and now if I hit okay we can take a look we have
[230:59] on the explore the curve editor or the dope sheet yet but if I were to look in the curve editor we
[231:04] can see that it creates this value essentially that goes from let's maybe see if I can zoom in here
[231:12] I will hold alt and middle mouse drag to the right to see exactly what's happening so each frame
[231:18] we will get a random value between zero and one and as a result this will now create the flickering
[231:24] for us if I were to just zoom in on our timeline real quick and let's play the animation we can
[231:30] kind of see this flickering that happens all right so if we want to reduce the frequency of this
[231:36] flicker we will just have to divide our frame number so if I go back over to the expression so
[231:43] again I will just highlight the value and press equals in between parentheses over here I can do
[231:48] frame if I want to lower the frequency by half I can just divide this value by two so when I do
[231:54] this we can see that our curve is a little bit more spread out and this will mean that our flicker
[232:00] is a little bit less intense and maybe this is what we want we might want to reduce this even
[232:07] further let's do divided by let's do divided by three and now we can see we have a kind of like a
[232:14] more smoother curve and let's play the animation all right so I'm pretty happy with this but now
[232:21] since our glow intensity changes this will affect our bounce as well so we want to use the same kind
[232:28] of grading adjustment on our other layers too now we can just clone this gray node if I press alt
[232:36] k this isn't obvious right away but if I press alt e and this might be turned on by default for you
[232:44] we can see with alt e this shows all of the notes that are linked together whether through
[232:49] cloning or expressions but now we are connecting these two gray nodes so if I do any adjustment on
[232:56] either of these gray nodes if I were to set the gamma here to a lower value we can see on this node
[233:02] it changes but on this node it changed as well so it's really really helpful especially in this
[233:07] case let's set this back to one let's go ahead and link this gray node let's link this to our glow
[233:13] bounce over here so let's do our grading adjustment so this is basically the intensity we will place
[233:20] this after our first gray node I can even maybe rename this let's do flicker so we can add a label
[233:27] to any of these nodes in order to stay more organized so now our glow bounce will also have this
[233:33] the same flicker that we have on our main glow layer so we can see this now over here so now
[233:40] that we have this glow layer we pretty much have all of the layers that we need and with the next
[233:46] lesson we can go all the way back to the top to the environment and we can start making some small
[233:52] changes we can readjust our gray nodes and see where in between all of these layers we can maybe add
[233:59] a few extra details and really fine tune the overall look of our comp so I will see you there


### Final touches [234:06]
**Transcript (timestamped):**
[234:06] so now that we have all the layers that we need it's simply just a matter of going back and adjusting
[234:12] everything and now we can take a look into some of these finishing touches that we can add to make
[234:18] everything come together now if we go back to our environment all the way over here after we do our
[234:24] pre-mult one more thing that I want to add on this environment I want to show you one of the nodes
[234:30] from the new survival toolkit installation which is P noise advanced so if we type here let's type
[234:37] noise and this is the one that we want to use P noise advanced again you will have to install the
[234:43] new survival toolkit to access this node let's point the image over here to our we can point this
[234:49] to the unremulted version so we can point this to our render from over here and with this P noise
[234:55] advanced we can specify the world position pass and similarly to how a nasty map will work by using
[235:02] the coordinate system on the x and y direction or the red and green channels this noise Gizmo
[235:08] will use the red green and blue channels to map a noise texture over our world position so if the
[235:15] position data here I will set this to P we can see now that we have this very cool noise texture
[235:20] running across our geometry and of course this will follow the camera so it will stick to the
[235:26] geometry so you can either use the UV AOV to map certain types of effects but you can also use the
[235:33] world position so that's something to keep in mind now over here we might want to make this noise
[235:39] slightly bigger I might want to play around with the increase the gain here and let's go ahead and
[235:44] just multiply this over our result and let's do this after or rather before our pre-mult so we'll
[235:50] drop down a merge and set the operation here to multiply and this is what we get so we can see
[235:55] that we might want to bring up the size of this noise let's increase the gamma we can drop down
[236:02] a grade node and we can increase the gamma in this in this way let's preview with five I will set up
[236:09] the final result here so I will preview this on five and we can see that with our extra layer
[236:15] so we are not really getting the result that we are after so we are not getting the correct result
[236:22] and this is because we are modifying the alpha as well so we don't want to break up the alpha so
[236:27] with that in mind let's actually do our P noise advance before we copy the alpha so we'll drop
[236:33] the merge over here before our copy and our pre-mult let's drag these over maybe to the side and let's
[236:40] do our pre multiplication over here so now we finally get the correct result and we can go back
[236:45] to our grade and let's increase the gamma maybe or we can play around with the gain so with this
[236:52] we just add another extra layer to break up our textures we can see that this really adds a lot of
[236:59] layering and detail to our environment and it was super super simple to set up it's essentially we
[237:05] are just mapping a grunge texture over our entire environment now again this is one of those things
[237:11] that you are better off doing directly inside of render but even if I had this in render I still
[237:17] occasionally like to use this noise to break up the textures even more and I think especially for
[237:22] a scene like this it provides an amazing result let's go ahead maybe I'll just bump up the gamma
[237:28] slightly so it's not as harsh and we can now go back to some of our other grade nodes let's take
[237:36] a look at some of these let's see what are the biggest contributors over here so I might want
[237:42] to lower the reflection of the sky let's look one by one I might want to lower this down even more
[237:50] our sun pass let's take a look at our other one all right maybe I can bump this one up slightly
[237:57] preview the final result maybe this is too much let's bring some of this back so I'm not gonna
[238:02] spend too much time really trying to finesse all of these values I will leave this up to you
[238:09] because this is this process is pretty self-explanatory I'm just trying to find the right values here I
[238:15] might want to lower the amount or rather the thickness of some of these smokeards let's go
[238:20] over here and see which of these needs adjustment I will drop down the alpha for some of these smoke
[238:26] layers to make them more transparent and I can make them less bright as well let's do something
[238:32] like this one really cool thing that we can do especially with foggy scenes like this and let's
[238:39] take a look at our fog setup as well I might want to overall lower this even more I might want to
[238:47] drop down the gain slightly we can still play around with the grade here that controls how far
[238:53] we are spreading our mask we can maybe lower this value or actually I think this this should be fine
[239:00] now one thing that we can do after we add our sky and our fog so from over here we can add a bit
[239:08] of diffusion so if I were to drop down a blur node with B let's maybe just drop down another dot over
[239:14] here with period and let's connect the blur to this dot so what I want to do here is just blur
[239:20] this image out maybe let's do something like 300 and now if I merge this on top of the actual result
[239:27] I can set the mix value to a very very low value and we can see it creates this very nice diffusion
[239:34] and it kind of helps us to blend all of our elements together and it adds sort of an extra
[239:40] fill layer in this case since this is a very atmospheric very smoky kind of environment
[239:46] it kind of helps to bump up that feeling of smoke so if I were to turn this on enough we can see
[239:51] what this extra blur layer will do for us now we don't really want to exaggerate and we can still
[239:56] play around with the size of our blur maybe we don't need this one such with such a high spread I
[240:01] will leave this I will leave this value at 100 and let's go back and inspect our merge so we can see
[240:09] with this extra layer this really helps to blend a little bit of these edges and the buildings with
[240:14] our sky element in the back which is really really cool so really helpful especially if we preview
[240:20] this with our final result this will introduce even more contrast with our foreground which is our
[240:26] character and the background so a super quick and easy but extremely powerful technique and
[240:31] furthermore I will want to introduce maybe even more of this blurriness but I want to isolate it
[240:38] with this area here which is essentially the building that's furthest away from our character
[240:44] so we want to do the same thing I'll add another blur node but we want to only affect this area
[240:50] over here so I will create a radial and let's place this roughly where we want it around this place
[240:56] I will go to the first frame of our animation which is 1001 I'll bring this all the way over here
[241:02] I will right click over here to set a key on all of these values which are the coordinates of this
[241:08] radial and I will go to the ending of my timeline at 1240 and I'll grab the gizmo over here and
[241:14] while holding down shift I will just drag this over until it lines up with our the furthest
[241:21] building away from our comp and now we can see that for the most part this will track our building
[241:27] let's inspect some other frames as well so I think this works fairly well so now from our blur node
[241:34] over here let's increase the size let's do something like this and we'll do a merge and let's set this
[241:40] b layer to be our radial and the operation now if we choose in this will now be masked by our radial
[241:47] but over here we might want to drop down another blur node so we can blur out the edges even more
[241:53] let's preview some other frames we will probably have to expand this radial let's maybe go to our
[241:59] first keyframe here and just make this overall a little bit bigger like this go to the end on
[242:05] 1240 over here and also increase the size here and maybe I can decrease the blurring so we can
[242:12] see clearly what's happening here so now I can merge this other new blur layer on top let's we
[242:19] can see that we are just isolating the blur over here and we can drop the mix value so now the
[242:24] further away we go from our camera the more of this blurriness kind of camera diffusion we will
[242:30] get and again we can just play around with the size of our radial maybe I still want to decrease
[242:37] this even more like so and let's go to the beginning of the timeline and also maybe adjust this over
[242:43] here and if I go in between we can see that this kind of tracks for the most part and this is mostly
[242:49] because we have a very linear camera animation on the orbiting axis so if we preview this from our
[242:55] final result with our character again I can press Q to hide our handles on the screen we can see
[243:03] with this extra layer we introduce even more separation in our background and more separation
[243:10] with the character with the character itself which is really really cool so here we can let's maybe
[243:17] hold down control and place all of our layers up and we'll do a backdrop over here so this can be
[243:25] a little bit of we can call this here diffusion so this blurring will help us separate our character
[243:33] but another thing that we can do to create the separation is also introduce a little bit of
[243:37] color variation so I can drop down a ramp in this case and I will let's hit Q again I will make this
[243:46] fade from the top and I will add a grade node and point this to point the mess to our radial
[243:52] and with this grade node I just want to introduce a little bit of blue over here just so we break
[243:57] up a little bit of this black and whiteness that goes across our entire environment so in our
[244:04] gate node let's just decrease the red channel and increase the blue slightly and if this is too
[244:11] much I will play around with the mix value to maybe lower this and I really just want to affect
[244:17] mostly the back part of our environment and the sky so if I were to preview the final result
[244:22] this is what we get with our adjustment and this is a pretty nice contrast I'm specifically doing
[244:28] this to make our orange color pop a little bit more we really don't have to go to very extreme
[244:36] values over here something fairly subtle again just to help our oranges pop out more and to break
[244:43] up the desaturated nature of our environment so something like this will help us we can take a
[244:48] look more into some of our other layers let's check out our ground smoke I think this is looking
[244:54] pretty good we can go forward with our character I might want for the character I might want to
[245:00] play around with some of our AOVs here we can see that I'm just turning them on and off we can see
[245:06] that this one is a big contributor to our shot and this last layer as well I might want to reduce
[245:13] the brightness overall of our reflection from the sky and I might want to increase the reflection
[245:20] here from the side and I think overall our glow bounce is too strong I might want to lower this
[245:28] to something like this and maybe I want to introduce more red in our overall glow let's
[245:34] look at our we can go to the sword which is over here on the left and with our gray node let's maybe
[245:41] reduce the green channel to get more of this red and let's take a look at some other frames
[245:48] all right so I'm pretty happy with this obviously the more time you spend the better the final result
[245:54] will be but these are essentially the techniques that you can use to make any adjustment that you
[246:00] want now that we have everything set up we can go one by one and affect every pass every light
[246:06] contribution all of the layers that we created and we really have the ultimate control this way
[246:12] and finally to finish up the comp we can add some final post processing effects and some of these
[246:19] layers that I usually add is of course we can add a grain so we will drop down a grain node
[246:26] and here for the presets I like to use the last one which is a bit more subtle and we can see that
[246:32] this will break up that perfect CG look it will kind of help us to replicate what happens in an
[246:38] actual camera now depending on what kind of render you are looking you are working on you might need
[246:43] to adjust the overall strength of this grain so you can play around I can maybe drop the intensity
[246:51] on all of the RGB channels here this is more of an aesthetic choice adding grain but usually with a
[246:58] lot of CG renders you do want to add this grain because it also helps to bump up the blacks a
[247:05] little bit and it will just help us smooth all of our layers together so speaking of smoothing all
[247:12] of our layers together we can add a final diffusion after before our grain rather so I can just add a
[247:19] blur node on our main chain over here we can increase the size and I can just drop the mix
[247:26] value over here and we can see what kind of effect this will have for our final diffusion we do want
[247:32] to have the strength rather low and with this final diffusion this will help us to spread our glow
[247:38] layers especially it will help them be more spread overall and again it just helps to blend
[247:45] everything together let's look at this with our grain now there's really a lot of different
[247:51] effects that you can use you can do something that's called an RGB split there's also halation
[247:56] but we can keep things simple we can just add a little bit of diffusion and our grain and finally
[248:02] from the new survival toolkit there's also a AP vignette node which is really cool which essentially
[248:09] just fades the corners of our comp again we're trying to imitate what happens with a real physical
[248:16] camera but in this case it also helps us focus our eye more around this bright part of our character
[248:23] now probably this is too much I can just lower the amount a little bit and the AP vignette is just
[248:28] something that I usually like to use in my comps and now finally to make this more cinematic we can
[248:34] drop down a crop and we can change the aspect ratio here let's do 235 by 1 so now we have this
[248:41] classic film black borders on our comp and from here really we can call this comp finished and
[248:49] with the next lesson we can do a final overview on everything we've learned so far so hopefully you
[248:55] will join me in our final lesson as our last lesson let's do one final rundown over the entire


### Conclusion [248:57]
**Transcript (timestamped):**
[249:02] comp and we can start all the way over here with our environment in fact we can probably also do a
[249:08] backdrop here and we can rename this to rebuild beauty env for environment let's maybe change the
[249:16] color as well we'll do something like this all right so we bring in our environment render we
[249:23] split this up per individual AOV so we can rebuild the beauty and have access to all of the individual
[249:31] contributions that make up our render and then we add an additional layer of detailing with this
[249:38] P noise advanced gizmo that we've got from the new survival tool kit moving forward to the right
[249:44] we have our sky which is just a texture that we added on a 3d sphere and then with our camera we
[249:51] can render this so it matches the alignment with our render just a simple gray node to darken this
[249:58] slightly so this will be the background for our environment with our depth pass over here we created
[250:06] a fog layer which we can add on top of our environment we have some diffusion by simply using a
[250:13] blurred version of the same image and plusing that on top over here with this ramp we just made
[250:19] everything blue on the top part of our comp then with 3d cards we can add some patches or layers
[250:27] of smoke which we can integrate in our render we can mess them by the same depth map that we use to
[250:33] create our fog and here we have our second one and our third one nicely integrated with our
[250:40] environment with our 3d objects by using the depth map on top of this we add a ground smoke which we
[250:46] created with the noise that comes with nuke which is simply animated and evolved by using expressions
[250:52] and this smoke is as well masked with in this case the world position we grab the y value of this
[251:00] world position we place this in the alpha and we can do some grading adjustments and use this as a
[251:06] mask in our smoke layer and this will be as well nicely integrated with our render moving down below
[251:12] we have the beauty rebuild of our character we've looked into how to use the cryptomats to make
[251:19] specific grade changes to specific objects or materials in our render on top of this we added
[251:25] scratches to our sword by using the st map that uses a noise texture and the uv pass of our render
[251:33] to create this extra layer of dust on top of our sword then we have our glow bounce by using the
[251:40] real light node which is leveraging the normal pass and the position pass of our render with a light
[251:46] camera and a material to create this nice bounce lighting that we get from our glow so if we move
[251:54] forward we have our foreground smoke and then finally our glow where we use the ap glow which is
[252:00] an exponential glow that comes with the nuke survival toolkit and it's probably my favorite
[252:06] node from really all of the nodes that are available with nuke then finally some very small camera
[252:13] diffusion with blur ap vignette and a gray node as our final post processing effects to complete
[252:19] our render and then a crop to just give this that cinematic aspect ratio so this is all I wanted to
[252:26] cover and with this we can conclude intro to nuke well done on making it this far some of these
[252:33] topics may go maybe slightly above a beginner level I would say but I do want you to have a sense of
[252:42] what nuke is used for in production so all of this that was covered is really just scratching the
[252:49] surface of what a nuke is capable of we can see that even though we have quite a big chain over here
[252:54] this might seem big to you if you are new to nuke or if you've never used it before but really on a
[253:01] large scale production something like this would be just maybe 10% of the entire comp some of these
[253:08] scripts are really insanely huge and again we are really just scratching the surface but this is
[253:14] it for now thank you for watching so far and I hope you enjoyed this course if you want to learn
[253:19] more about nuke you can check out some of our other free courses or paid one as well usually the
[253:25] renders are included so you can jump straight into compositing without having to go through the 3d or
[253:32] hudini part so go ahead and check out voxside.com for more courses and hopefully we'll see each other
[253:38] again in a new course



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
