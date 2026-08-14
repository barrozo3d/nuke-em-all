---
title: Create a Movie Quality Sci-Fi Laser Effect in Nuke
source: YouTube
url: https://www.youtube.com/watch?v=OJJ9hu6smqk
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "not specified"
tags: [compositing, particles, gizmo, procedural-texture,3d-system, digital-matte-painting, advanced]
extraction_status: complete
frames_dir: tutorials/frames/create-a-movie-quality-sci-fi-laser-effect-in-nuke/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Create a Movie Quality Sci-Fi Laser Effect in Nuke

**Source:** [YouTube](https://www.youtube.com/watch?v=OJJ9hu6smqk)
**Author:** Compositing Academy
**Duration:** 26m48s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to this video. We're going to talk about how to create a complex laser scan effect directly inside of Nuke without any simulations.
[0:07] So I'm going to let this play to show you what we're going to be doing.
[0:15] So I'll talk about the 3D scene first and just show you guys where the CG is coming from.
[0:20] And then I'll also show you how the effect is broken into primarily three different parts.
[0:25] So I just pause this real quick. We can take a look.
[0:28] Essentially, we have this pattern that's inside the sphere itself right here.
[0:32] And there's some animation and different tricks that we can pull off there to make it look like this.
[0:37] And then we have the actual spread animation itself.
[0:40] So the way the edge of the laser is spreading, we can't just use a noise pattern.
[0:44] How do we make an intentional spreading effect that looks designed?
[0:49] And then obviously, we have the pattern itself inside of the actual laser that's kind of being revealed.
[0:56] So you can think of those as two different things, but that's what we'll dive into.
[0:59] So we'll take a look at the CG scene just to see where all this is coming from.
[1:03] So this is what the CG scene looks like.
[1:05] I won't spend too much time talking about this just because this is not the focus of the tutorial,
[1:08] but just to give some context if people are wondering, essentially, it's a pretty simple scene.


### 3d Scene Overview [1:10]
**Transcript (timestamped):**
[1:12] It's just like a few photo scans I took in Iceland.
[1:15] These are some lava terrains that I added some CG moss on top of it.
[1:19] And then this rock is also just like a photo scan.
[1:22] So you can use like polycam on your phone if you want to scan objects like this.
[1:26] And it gets pretty decent results.
[1:28] So that's a fast way to do it without having to do local processing for photogrammetry and things like that.
[1:33] So that's where this comes from.
[1:35] Originally, I was going to do a copper sphere, but I changed my mind in the comp.
[1:38] So we'll jump into that now and start talking about the laser.
[1:41] Okay, guys.
[1:42] So before we jump into the final effect on this, I'm going to show you the sandbox of how I came up with this approach.
[1:48] So typically when you're designing something like an effect, it's it's a process of look development,


### LookDev Experimentation [1:50]
**Transcript (timestamped):**
[1:54] which means you're kind of iterating quickly and sort of experimenting.
[1:58] And so rather than just showing you like the linear process of here's this and here's exactly how it's done,
[2:04] which I will show you after.
[2:05] I think it might be interesting if you're watching this and you're curious,
[2:09] how do you quickly iterate on ideas to see something that might be more interesting?
[2:14] And so I'm going to show you a really dirty new script that's just a complete disaster.
[2:19] And this is sort of when I'm working very quickly and iterating.
[2:22] So I don't even care about my new script.
[2:24] So like this is like the main new script.
[2:25] You see kind of a follow some sort of a structure, you know, going down the B pipe and things going left to right and some basic cleanliness to it.
[2:33] Let's say, but when I'm experimenting and trying to come up with an idea, I basically have a separate new script called like a sandbox.
[2:41] And this is where I'm just going to experiment with different approaches very quick.
[2:43] So this is what it looks like.
[2:45] Complete disaster, just different sections, trying different approaches to figure out exactly what I'm going to do before actually bringing into the master comp and sort of create a template for the design.
[2:56] So before I had the final idea, the fundamental idea of a laser is like it's just a projection.
[3:03] It's light going out from a light source going to a surface.
[3:06] So immediately my brain was going to projections and just bringing in the geometry from the 3D blender scene.
[3:13] So essentially I've loaded in the limbic file from the scene.
[3:17] So I'll just close on this stuff.
[3:20] So we have the rock.
[3:21] We have the sphere and we have an axis that I've parented to the sphere.
[3:27] So basically it matches the same motion.
[3:30] The reason we have an axis is because the UV project note can take an axis here.
[3:34] So we can actually project out textures from the source.
[3:37] If this sort, if this axis follows the same center point as our moving object.
[3:41] So you want the pattern to move with the projection.
[3:45] So that was the original idea.
[3:47] Now I'm going to go through this disaster of a sort of layout just to show you how the idea evolved.
[3:53] So the original idea was like, well, maybe I could just take something simple like a grid and then just project that out onto a onto the rock and then just parented to the moving sphere.
[4:03] And then we have something that looks like a laser is being projected out.
[4:07] And this could be one approach like there is no right answer to what it's supposed to look like.
[4:11] You know, you could do so many different designs you could do.
[4:15] If I were to go further with this effect, you would obviously need to like mask this off properly underneath where it's not supposed to be hit.
[4:22] And I did actually do a render, which I'll show later.
[4:25] That is essentially a light source that creates a mask from where we would expect the light to hit.
[4:31] So in the final actual effect, I do have a render for that.
[4:35] But just to give some context, because sometimes these project nodes, you know, even though it's supposed to be occluded, even the project 3D though,
[4:44] they don't always give like perfect occlusions.
[4:46] And so it's a little bit glitchy sometimes.
[4:48] So UV project, it's supposed to project in the front, but it's not really self-occluding in the way that we would necessarily expect.
[4:55] So that's just something to keep in mind.
[4:59] And then if we were to plus this over scene, you know, that's a pretty basic laser.
[5:02] We can make that a lot more interesting for sure.
[5:05] But that could be one starting point for an effect if you were to think about it.
[5:10] Now, another way I thought about, I was like, not that interested in this approach.
[5:13] Maybe I could come up with something better.
[5:15] So let's just try something else.
[5:16] So another way is we could take position data, something like this is just a basically precomp of my position data of the scene, the P data.
[5:24] And you can use a noise node.
[5:26] So let's say P noise advanced.
[5:27] This is a node from Wikipedia.
[5:29] There's a few out there.
[5:30] I've talked about this in stores before, so I won't repeat it.
[5:32] You can find that node if you Google it.
[5:35] Essentially, I was like, okay, well, maybe another way to do this would be making some edges with P noise.
[5:40] Maybe that would give a more interesting motion.
[5:42] So you could just essentially just edge detect a P noise and then, you know, start masking that by a pattern, let's say.
[5:49] And so this is another approach.
[5:51] You could have something that looks like this, some different patterns flowing along the surface.
[5:55] And, you know, to me, it looked a little bit like burning embers.
[5:58] And maybe that's because it's red.
[6:00] If I switch the color here, maybe it would look something else.
[6:04] That could be an interesting starting point.
[6:06] But the problem with this approach is that it didn't feel like I have a very good controllable way to intentionally spread this.
[6:13] And so once I started to come to the idea of I wanted this laser to hit a point and spread outwards,
[6:18] then I knew I need to do something more complex than this.
[6:21] This is not going to work, at least for what I want.
[6:23] If you want a laser uniformly shooting all over a surface and maybe just everywhere in the scene,
[6:29] maybe this approach could work.
[6:31] And so that's sort of how my brain was thinking about this.
[6:34] It's like, okay, well, that's interesting, but not quite what I want.
[6:39] Another approach I tried just because I was continuing to experiment.
[6:42] And usually I don't spend more than like 10 or 20 minutes on like these little mini experiments to try to figure out which path that I want to take.
[6:49] And so another approach I did was, okay, I have the P data.
[6:53] I can also use this little node called P scatter.
[6:55] This is a plugin I released for free.
[6:57] It's on my website on your assets.
[6:59] You can get this literally for free.
[7:00] It's pretty sweet.
[7:01] And you can literally scatter video textures all over your scene, which there's really no other good way to do this, which is why I made it.
[7:09] And so my idea was like, well, if I could project a bunch of little different shapes,
[7:15] maybe that could be another way to create a more interesting effect and just the standard, you know, grid like I was showing at the beginning.
[7:22] So that was another sort of line of thinking I went down.
[7:25] I was scattering these.
[7:26] This is basically some video patterns you can generate from my plugin, my motion graphics plugin, which is also available on the website.
[7:33] But you can create all different types of shapes.
[7:35] So thinking about maybe different types of geometric patterns or different size of these things.
[7:41] And then you could project them out using P scatter and get this crazy looking geometric effect.
[7:48] So that's one way.
[7:49] But again, it wasn't giving me the exact sort of spreading control that I wanted or the exact intentionality I was looking for.
[7:55] But it's an interesting idea.
[7:57] And maybe that would be interesting for you in the future.
[7:59] So that's why I'm sharing it.
[8:00] It's just like, here's some different ideas in a very scattered brain approach.
[8:06] So this is another same thing, basically just taking the grid idea again.
[8:11] Maybe you mask it by a more interesting pattern.
[8:14] So I was thinking, well, maybe I could use this rain circuit pattern, which is again for the motion graphics thing.
[8:20] You don't have to use this bugging, by the way, if you don't want to just grab some stock footage on Adobe stock footage, whatever thing.
[8:25] The reason I made this is because I just got frustrated having grids and noise patterns in Nuke.
[8:29] Like that's not enough to create interesting effects without having to hop into Houdini, for example.
[8:35] So for me, that's just the limitation.
[8:37] I pretty much made it for myself in that scenario.
[8:40] But yeah, so if you combine these two, you have like a grid and some interesting patterns like this that you can actually manipulate and do some load development.
[8:50] I thought that that could be maybe more interesting and start to get something a little bit more interesting in terms of breakup, but still the same sort of problems.
[8:59] So that is the sort of scatterbrained approach we have here.
[9:03] So what did we do for the actual real method?
[9:05] That's the question.
[9:06] So let's take a look at the real script and I'll show you the approach.
[9:10] So first we'll talk about the spread effect and then I'll talk about the pattern inside of it.
[9:14] So to create the spreading, essentially the idea I came up with was to take the rock that I have and I put the texture on it as well.


### The Spread Effect [9:15]
**Transcript (timestamped):**
[9:24] I have the photo scan texture, which is just from Polycam so you can plug it in just to visualize it a little bit cleaner.
[9:29] And I put it through a scan line render and I put a camera where the sphere is roughly.
[9:36] So just like put it here like this facing towards the rock.
[9:40] And in my scan line render, I'm going to put this out to just render that camera.
[9:43] So I have a camera that doesn't move at all looking at the rock.
[9:47] Now, how do we create a laser scan effect that essentially traces the edges and sort of spreads outwards?
[9:54] That's what I was thinking about.
[9:55] That's what I wanted to come up with.
[9:57] So the idea I came up with was to use rotos, basically roto paint mode that has the stroke effect that you can animate.
[10:04] So if I take a roto and you draw a line, you can go like this and then you can take the stroke and essentially animate
[10:13] the end like this.
[10:16] So this is actually a pretty interesting idea because if you had a bunch of these lines spreading in different directions,
[10:21] then maybe we could create a more interesting alpha to start with that could be the base of our spread.
[10:27] So if I go back in time and look at this crevices roto paint and hit play,
[10:32] essentially when the laser starts to come on, we'll see that it starts to trace over the scene.
[10:36] So if I turn this back, turn this off, this little replace thing.
[10:41] Essentially, I just traced over the image and then I hit replace when I was done to just delete what's upstream.
[10:47] So it's just a quick way to essentially delete all the stuff that's above it, but then I can toggle this on and off and actually see what I'm doing, drawing over the rock.
[10:55] So I looked for interesting crevices as my starting point and then just sort of drew in there and try to figure out a way that I could animate those brush strokes at a slightly different offset that feels like it's being traced.
[11:08] And I did another version that's a broader roto paint that essentially spreads in different directions after the crevices have been drawn.
[11:15] So if I look at this, we'll see these larger surface patterns that start to accumulate after the crevices have been drawn.
[11:21] I did different colors because I thought that maybe I could create different interesting edge detects by having different colors.
[11:28] If you did it all in white and you do an edge attack, it only detects around the edge.
[11:31] But if you do different colors and then you do an edge attack, you'll actually get the in between sort of cracks.
[11:37] And so that was like one approach and actually does work, by the way, if you take a look at that.
[11:42] So if I do, as we go back to our just our alpha, I'll disable all these notes, we keep the color and then I'll re-enable this.
[11:48] So if I do an edge attack on the alpha, you see we get the edges like this.
[11:52] And this is already kind of an interesting looking alpha that we get.
[11:56] But I ended up not wanting this. It didn't look right in the end result.
[12:00] So I did just desaturate it so that we just get the far reaching edge rather than this sort of like split up pie type of thing here.
[12:11] What do we do now? We have this alpha that is spreading and we can project it.
[12:17] So I'm going to turn this off because I don't think that's necessary there.
[12:19] But essentially what I did was now I took the same camera that we were looking through towards the rock.
[12:26] So I have two cameras in the scene. I have the animated camera, which is, you know, way back here, the actual one that we're seeing through in the final scene.
[12:33] And we have this projection camera and we'll do the projection camera on the rock like this.
[12:37] So then we get the alpha spreading on the surface.
[12:39] So you can see it's spreading, which is kind of what we wanted.
[12:42] And if I look at that through the actual animated cameras point of view, so this scanline render is looking at the same rock.
[12:49] But now with a new texture, which is just the projected alpha.
[12:52] Now we're seeing it through the correct point of view.
[12:55] So here's the alpha effect after it's projected.
[12:58] And we can see that the spread is happening more organically in a way that feels much more intentional.
[13:03] Now there are some black hole areas that we need to correct just because essentially the facing angle of the camera is probably not hitting those edges.
[13:10] And maybe that's just like a side facing piece of geometry.
[13:13] So we'll need to clean it up a little bit.
[13:15] But in terms of like the base idea, I think this is a good starting point.
[13:19] So that's kind of where I started.
[13:20] So what we can do here after we have that, we can start to do a little bit of rotos to either just kind of clean up some of these little things back here.
[13:27] Or we could just do a dilate as well to essentially basically if you dilate smaller, we can get rid of some of the smallest things and then we can dilate back outwards the opposite direction just to get the edges.
[13:39] Now you might get a little bit of a box of your edge doing that.
[13:42] I thought it was fine in the final effect.
[13:44] So there's different ways you could handle those problems.
[13:46] But for me, it was fine.
[13:48] And then to get the edge of this, you can use either an edge attack or you can create one manually by either eroding that alpha slightly in a different direction and subtracting it from itself.
[13:59] So I can see here I just shrunk it, shrunk it a tiny bit and then subtract it from itself.
[14:04] So we have like this leading edge.
[14:05] Okay, this could be interesting.
[14:07] So that's a good starting point.
[14:09] So now that we have an edge spreading effect, we need to essentially reveal something underneath to make it look more like a laser.
[14:15] So we're going to go back to a new approach.
[14:18] So we have the CG scene.
[14:19] This is what CG scene looks like by default, by the way.
[14:22] No depth of field, no color grading, kind of ugly a little bit, just the raw render compared to the final result where we do some more cinematic color grading and things like that.
[14:32] So we're going to look at the raw render though, which is a little bit more like this.
[14:36] And essentially what we're going to do is use the P data.
[14:40] And I'm going to use a node called projection buddy.
[14:43] You can Google this.
[14:44] Somebody made a really nice tool that you can project videos directly onto position data.


### The Scan Pattern [14:45]
**Transcript (timestamped):**
[14:50] And so this is pretty cool, but we need a pattern to project onto the rock that we're going to mask with the other edge effect that we did.
[14:58] So here I'm using the pattern that I generated from motion graphics plugin in Nuke, which is available in the description below if you want it.
[15:05] So there's a bunch of different nodes here.
[15:07] Like I said, you've probably seen me use these a few different videos if you watch the channel, but there's a bunch of different.
[15:12] A ton of different effects here that we can start as a base to get something more interesting.
[15:16] If you don't want to use a sproach, you can also do something like this where you do like maybe a noise just to show you some alternatives here.
[15:23] You could use a noise pattern and you could just erode it down and make some spheres.
[15:28] So this is a little bit hard to see here, but if I zoom in, you can do something simpler like that.
[15:32] And maybe that would be another type of pattern you could mask.
[15:36] But I wanted something more interesting.
[15:37] So here I'm using a node called hex flow, which gives you these like rippling dots that we can modify.
[15:43] There's a bunch of different controls.
[15:45] And so what I'm going to do is I'm going to P project this onto the surface of the rock here, which is going to give us this really cool rippling effect on the surface,
[15:55] which just gives it a little bit more life than just, you know, masking another noise pattern.
[16:00] Now there are some problems with projections, right?
[16:02] So if we do the P projection on this side, just to quickly explain how this works, P projection node, basically just click this and you sample the P data and you will just be able to drag your video around.
[16:15] So I guess I can just show that real quick.
[16:17] Just copy this, put this and I'll just click the little icon here.
[16:22] So if we control alt click, if you control click, it doesn't work.
[16:27] Control click will do this easily with this with this specific node projection buddy.
[16:32] You can say I can just drag around and place this wherever I want it.
[16:35] And that's pretty cool.
[16:36] So I wanted it on that side.
[16:38] And that's how I got it sitting there.
[16:40] So it'll actually stick now as the scene moves around.
[16:43] And I did a separate one more on this side so that I can reduce some of the stretching that is naturally going to happen with camera projections.
[16:51] And then we can get a base pattern we can mix together just to get the dots in between.
[16:55] Now they don't line up perfectly in the scene but it doesn't really matter because you're not going to actually see it with the edge that's sort of evolving across the surface.
[17:03] So essentially all this two P projections with interesting flowing patterns.
[17:09] And then I'm masking those two projections together using another P mat.
[17:14] So this is a P mat.
[17:15] So I just use an created an alpha on this side of the position data.
[17:19] So we say we want this projection that's kind of more front facing on that side.
[17:24] We want to keep it here.
[17:26] And then the other one we want it on this side.
[17:29] So we're just mixing those two together.
[17:31] So we have this base pattern that we have.
[17:33] Now what we can do is take this pre-comp it out and multiply it against our edge.
[17:38] So now we can get us an edge spread that is actually giving us those little flowing patterns, which is cool.
[17:44] Now we have something a little bit more interesting to start with.
[17:48] Now this is again just a starting point.
[17:50] There's a lot more we can do here in terms of making this more interesting.
[17:53] We can't just do this and then be done.
[17:55] So how do we make this even better?
[17:57] So what I did was I took our original alpha that is just the rotos being projected everywhere,
[18:03] but I didn't do an edge detect on this one.
[18:05] I just left it looking like this.
[18:07] And I took the edge detect version, which is the one we already talked about.
[18:11] And I did a glow on it so I can get this like sort of a light fall off edge.
[18:16] If I mask those two together or multiply in this case,
[18:19] we can get something that's a little bit more interesting.
[18:21] It feels more like the light is actually falling off.
[18:24] And so this could make it a little bit more interesting.
[18:26] So maybe that's something we could put underneath if we multiply that by the same effect that we created.
[18:32] In other words, we're just trying to create interesting alphas.
[18:35] If you get any takeaway out of this, it's like we're trying to create interesting alphas and mask them by another pattern.
[18:40] That's really all we're doing.
[18:41] So it's not, I know it seems like a lot of steps if you're a beginner,
[18:44] but all we're doing is creating those two things.
[18:47] So if we take this and multiply it against that same pattern, which is this,
[18:53] now we have something that kind of has that leading edge, but sort of falls off towards the center
[18:58] and reveals a little bit more of the interesting pattern that we created everywhere.
[19:04] I also masked out the crevices in this alpha, I believe,
[19:08] so that we wouldn't see this pattern appearing in the actual cracks of the rock.
[19:13] The reason I did that was to create a little bit more depth in the laser effect itself,
[19:17] just to make it look more 3D.
[19:19] So we don't want to start to go into 2D effect territory.
[19:22] And so I just thought it would look cool to not have it in the cracks,
[19:25] but have it more on the surface as it's spread around.
[19:28] So if we start putting that underneath, and we put our brighter effect on the edge over the top,
[19:33] which is this one here.
[19:35] Now once we add our ZD focus, technically you would want to separate this scene out into a few different renders
[19:41] to get a perfect ZD focus without any little edge artifacts.
[19:44] I think some of my little moss gets some edge artifacts here,
[19:46] but I didn't really care because it's for this tutorial.
[19:48] And that would make things take longer, but just as a heads up, as a good habit,
[19:53] if you were doing this for like a feature film,
[19:55] you'd want to do this a little bit slightly differently on the ZD focus by splitting everything out.
[19:59] The next thing you want to do is do some god rays.
[20:01] So what we can do is take the actual edge pattern,
[20:03] and we can essentially god ray that back to the light source.
[20:06] So we can do a god ray and shrink it towards the light source like this.
[20:10] So if you guys have ever watched my volume ray tutorial or god ray tutorial,
[20:14] I think it was like a year or two ago I made it,
[20:16] but you put the center at the source of where you want to pull the god rays towards,
[20:19] and then you shrink it down.
[20:21] And then we can create god rays from the actual edge.
[20:24] And then you can increase the steps, and then you can do something like this.
[20:27] Now, I think I did two different versions where one's more falling off on the edge,
[20:31] and one is more overall.
[20:34] And if you look at this, it looks a bit too bright in the natural comp.
[20:39] I compensated after the color grade because after the color grade,
[20:42] it does sort of dim down some of the, those tones in there.
[20:47] So it does look a little bit too intense if we look at the raw render.
[20:51] But yeah, I wasn't doing this comp top down.
[20:55] I probably had the color grade and I was looking at it while I was adjusting the god ray.
[21:00] So if we look at this, it might just look a bit blobby and thick and confusing.
[21:04] But let's continue down the comp, keeping that in mind.
[21:08] So one extra little challenge we're going to have here is how do we get this


### Extra Details [21:10]
**Transcript (timestamped):**
[21:11] composited effect back into the sphere because this is very reflective.
[21:15] So what I did was I pre-comped out these elements and essentially,
[21:19] you know, with the glows and all that kind of stuff.
[21:21] And I want to re-project that back onto the rock.
[21:24] So here's the rock element with the composited effect isolated and
[21:30] re-projected back onto the sphere.
[21:32] And then what we can do is ray render this with a sphere.
[21:35] So the sphere has a reflection shader on it and we're going to ray trace this
[21:40] cop defect back onto the sphere so that we get essentially reflection in the sphere.
[21:45] We need to make sure that that is actually showing up.
[21:48] So essentially we have this and then we can mask it off by the sphere alpha.
[21:52] So we just get that and we put that back inside of the sphere effect.
[21:55] Otherwise, it's not going to be very realistic if we don't have reflection.
[21:59] Now, there's some other things we need to do here, which can make this look a bit better as well.
[22:03] Essentially, what we can do is you can also re-project composited effects back in blender
[22:09] to get some fake interactive effects.
[22:12] So here I did a camera projection of my edge effect into blender to create some fake interactive effect.
[22:18] I kind of rendered this in a pretty low samples just because it's very subtle.
[22:22] You could just comp this, you could do a blur and fake that and kind of gain up if you wanted to fake it that way.
[22:28] But I wanted to have some actual shadows on the back sides of things, which is a little bit more convincing.
[22:33] So what you can do is from the point of view of the camera, project composited effects back in your CG renders
[22:41] and then use those as a light source to essentially contaminate the scene with the actual light essentially.
[22:48] So once we do that and we combine it with Albedo, we have something like this.
[22:53] So we have the actual light source affecting the scene as we would expect.
[23:00] So this is a very cool way to create more integrated composite effects.
[23:06] If you start bringing your comps back into CG, which is actually less common workflow,
[23:11] like if this was probably studio, most likely this would be done maybe in Houdini.
[23:15] You'd have some kind of effect and then some kind of light contamination effect that we're just given to you as a compositor.
[23:21] But if you work in a compositor workflow where you're doing things back and forth,
[23:25] you can do things in a slightly different way but achieve the same result without having to do any complex simulations
[23:32] and you can iterate much faster.
[23:34] That's the key is you can actually create looks, I think, faster than doing simulations or doing geometry setups, for example.
[23:42] So that is the main idea with the spreading effect.
[23:47] Now we've talked about the actual effect here, the spreading and the pattern itself.


### Sphere Effect [23:50]
**Transcript (timestamped):**
[23:53] Now we're going to talk about the sphere, which is a little bit simpler than everything we've been talking about,
[23:57] but still there's some interesting useful techniques here that can be helpful.
[24:02] Now the base idea for the sphere and creating this effect is, I'll show you the base concept,
[24:07] which was this is my simple idea and then I made it a little bit more expanded.
[24:10] But the real idea is really just like you have a base line pattern that's being revealed on that metallic surface to make you feel kind of sci-fi
[24:17] and you want to reveal some sort of light source behind it.
[24:20] And so what I did was I did some spot flares, which are just these sort of exponential glow balls.
[24:25] And if you shift these around with an animation, basically just sliding left to right, this is our texture.
[24:31] If we multiply that by the edges, we get something that looks kind of cinematic.
[24:37] It feels like a light source that's falling off because it's quadratic, but it's sort of behind these edges, which gives a very metallic looking feeling.
[24:44] If you look at that on a sphere, essentially we can get something like this.
[24:50] So this is like the base idea, but I didn't like the grids.
[24:53] It felt a little bit too geometric for what I wanted.
[24:56] So I wanted to break it up a little bit more in my real one.
[24:58] So I used the rain circuit, essentially no, which is like a grid, but more interesting.
[25:05] And then I did the same exact principle.
[25:07] So that's the principle.
[25:08] But if we reveal it through more interesting shapes and patterns, we can do more juicy effects.
[25:13] Now, what I did at the end as well was taking that radial, I guess, spot flare and then just scaling it vertically, scaling it, making it a very tall ellipse so that it kind of looks more interesting as an animation.
[25:28] So we have like a thin beam that shoots across and then it expands at the end as we want to make this into a light source.
[25:35] And this is just, yeah, it's just a 2D image really that we're just masking.
[25:39] So we have like it's kind of spread and then it sort of vertically expands like that.
[25:45] So here we can see pretty much what's happening.
[25:48] So again, this would be something that would be pretty annoying to do if you're doing it all in the 3D software.
[25:52] That's why I think that composing workflows are very interesting because you can iterate faster and work with videos in a timeline in a much more natural way and sort of iterate with these patterns.
[26:02] So that's why I really like working this way.
[26:05] So this is the sort of final effect. It feels like a little bullet shoots across and then sort of expands.
[26:10] And then we can also create some glow on that and create that final integration.
[26:16] And so yeah, this is the final effect. I can play the full shot again just so we can see it.
[26:21] So a few different steps there that are interesting.
[26:23] So hopefully you got some kind of takeaway in this and figure out how you can use in your own projects or even just keeping those techniques in your subconscious in the future.
[26:31] There's probably something there that can be useful.
[26:34] If you guys are wanting to see more videos like this, make sure to hit thumbs up on the video.
[26:39] If you want to learn new composing, check out the courses in the description below as there's a bunch of tutorials there as well with lots of many hours of techniques like this.



---

## Captured Frames

- [2:14] tutorials/frames/create-a-movie-quality-sci-fi-laser-effect-in-nuke/frame_000.jpg
- [3:53] tutorials/frames/create-a-movie-quality-sci-fi-laser-effect-in-nuke/frame_001.jpg
- [9:57] tutorials/frames/create-a-movie-quality-sci-fi-laser-effect-in-nuke/frame_002.jpg
- [12:39] tutorials/frames/create-a-movie-quality-sci-fi-laser-effect-in-nuke/frame_003.jpg
- [15:37] tutorials/frames/create-a-movie-quality-sci-fi-laser-effect-in-nuke/frame_004.jpg
- [20:06] tutorials/frames/create-a-movie-quality-sci-fi-laser-effect-in-nuke/frame_005.jpg
- [24:56] tutorials/frames/create-a-movie-quality-sci-fi-laser-effect-in-nuke/frame_006.jpg
- [26:16] tutorials/frames/create-a-movie-quality-sci-fi-laser-effect-in-nuke/frame_007.jpg

---

## Structured Notes

### Core Technique
Build a fully art-directable "laser scan" reveal effect entirely in 2D/3D comp (no simulation software) by animating hand-drawn `RotoPaint` stroke alphas, projecting them back onto CG geometry with position-data (P-channel) projection tools, then masking a secondary procedural pattern through the spreading edge to fake an intentional, designed light-scan look.

### Summary
Compositing Academy builds a sci-fi laser-scan reveal (light traces across a rock surface toward a glowing sphere) entirely inside Nuke, deliberately avoiding Houdini/simulation. The video first shows a "sandbox" look-dev process — trying UV-projected grids, P-channel edge-detected Perlin noise, and the author's own free `PScatter` plugin scattering shapes — before settling on the actual method: hand-animate `RotoPaint` stroke end-points over the rock's crevices (drawn in different colors so an `EdgeDetect` picks up interior cracks, not just silhouettes), reproject that spreading alpha onto the rock through a static "projection camera" using `Card3D`/`ScanlineRender`, clean it with erode/dilate and edge-subtract tricks, then mask a second procedural pattern (`HexFlow`, or the free `ProjectionBuddy` gizmo projecting textures via P-channel/position data) through the spread edge so the revealed laser trail has internal detail rather than being a flat glow. God rays are pulled from the edge toward the light source, the composited effect is re-projected back onto the CG rock/sphere in the renderer for accurate reflections, and even re-projected into Blender as a fake interactive light-contamination pass. The sphere itself uses a simpler technique: animated exponential "spot flare" glows multiplied against a grid/`RainCircuit`-style pattern, stretched into a tall ellipse to read as a thin expanding beam.

### Key Steps
1. Look-dev/sandbox phase: try (a) UV-projecting a simple grid onto geometry via an `Axis` parented to the moving object, (b) edge-detecting P-channel noise (`P_Noise_Advanced`, a Nukepedia gizmo) for organic but uncontrollable motion, (c) the free `PScatter` gizmo (author's own plugin) to scatter video-texture shapes across position data — reject all three for lack of controllable, intentional spread.
2. Real method — draw the spread mask by hand: use `RotoPaint`'s animatable stroke end-point to hand-trace crevices on the rock texture over time (paint in "replace" mode to preview cleanly), using different stroke colors per region so a later `EdgeDetect` picks up internal cracks, not just outer silhouette.
3. Desaturate the multi-color roto result before edge-detecting, to avoid a "pie slice" split-color artifact; keep the far-reaching edge only.
4. Reproject that spreading alpha onto the rock geometry using a static, non-animated "projection camera" (separate from the animated hero camera) via `ScanlineRender`/`Card3D`-style projection, so the spread reads as if traced across the real surface from the correct point of view.
5. Clean the projected alpha: erode-then-dilate to remove small stray specks, then create a "leading edge" by shrinking a copy of the alpha and subtracting it from the original (manual edge-detect alternative to `EdgeDetect`).
6. Build a secondary internal pattern to reveal inside the spread: project a procedural texture (`HexFlow` gizmo, or a simpler eroded `Noise`) onto the rock's P-channel/position data using the `ProjectionBuddy` gizmo (Nukepedia) — control-click/alt-click the viewer to drag-place the projection directly on the 3D surface; use two projections placed on different facing sides, blended via a `P`-channel-derived matte, to reduce projection stretching.
7. Multiply the internal pattern by the spreading edge alpha (pre-comped) so the revealed detail only shows inside the laser trail, not everywhere.
8. Build a secondary "light falloff" layer: `Glow` the edge-detected alpha and multiply it against the un-edge-detected spread alpha for a softer light-falloff look; mask out the original hand-drawn crevices from this layer so the pattern reads as being on the surface (not inside cracks), preserving a 3D read instead of looking 2D.
9. Add depth of field (ideally on separate per-element renders to avoid edge bleeding) and god rays: shrink an edge-alpha-derived shape toward the light source and increase ray-march steps to build streaking god rays; expect to re-balance brightness after the final color grade dims things down.
10. Feed the composited effect back into the CG pipeline for accuracy: pre-comp the rock's effect layer, reproject it back onto the reflective sphere via ray-traced render so the sphere's reflection shows the effect; separately reproject the edge effect back into Blender at low sample count as a fake interactive light-contamination/bounce-light source, combined with an Albedo pass.
11. Sphere reveal (simpler pass): animate exponential "spot flare" glow shapes sliding across, multiply against edge/pattern shapes (e.g. `RainCircuit`-style grid) for a metallic falling-off-light look; scale one flare into a tall vertical ellipse so the final beam reads as a thin line that "expands" at the end like a shot being fired.

### Nodes / Tools / Settings
- `RotoPaint` — animatable stroke end-point (hand-drawn, animated "trace" reveal), multi-color strokes for interior edge detection, "replace" blend mode to preview cleanly
- `EdgeDetect` — both on multi-color roto (interior cracks) and as an alternative manual erode-and-subtract technique for a leading edge
- `P_Noise_Advanced` (Nukepedia gizmo) — Perlin-style noise driven by P-channel/position data (rejected approach, shown for context)
- `PScatter` (free gizmo, author's own plugin) — scatters video textures across P-channel/position data
- `ProjectionBuddy` (free Nukepedia gizmo) — projects 2D textures onto 3D position data (P-channel), control/alt-click-drag placement directly in the viewer
- `HexFlow` (motion-graphics plugin node, author's own) — rippling procedural dot pattern used as the internal laser-trail texture
- `Card3D` / `ScanlineRender` / static "projection camera" (separate from the animated hero camera) — re-projects 2D comp elements back onto 3D geometry
- `Glow` — light-falloff layer built from the edge-detected alpha
- God ray technique — shrink an edge-derived alpha toward the light source with increased ray-march steps (referenced from the author's earlier dedicated god-ray/volume-ray tutorial)
- Depth of Field — flagged as ideally requiring per-element render separation to avoid edge artifacts (not done here for time)
- Blender re-projection — composited effect fed back into the 3D renderer as a fake interactive light-contamination pass, combined with Albedo

### Difficulty
Advanced

### Foundry App & Version
Nuke (with a Blender-side re-projection step for interactive lighting). No on-screen version banner or OCIO metadata visible in the captured frames — version not specified.

### Tags
compositing, particles, gizmo, procedural-texture, 3d-system, digital-matte-painting, advanced

---

## Related Tutorials
Shares `procedural-texture` and `gizmo` with Build Entire FX with ONE Pass - Nuke Tutorial (`build-entire-fx-with-one-pass---nuke-tutorial.md`) — both use World Position/P-channel data to drive procedural effects without re-rendering.
