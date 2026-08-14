---
title: [3/3] Nuke Tutorial Series (Flow Paths, FX Integration, Design)
source: YouTube
url: https://www.youtube.com/watch?v=_Fu8yl_p0vM
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke / NukeX (cross-platform: Google Tilt Brush VR geometry authoring, otherwise pure Nuke)"
version: "Nuke 13.x (13.1/13.2 — exact 2022 point-release not stated)"
tags: [compositing, 3d-system, projection, st-map, gizmo, fx-simulation, rotopaint, grading, expert]
extraction_status: complete
frames_dir: tutorials/frames/33-nuke-tutorial-series-flow-paths-fx-integration-design/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# [3/3] Nuke Tutorial Series (Flow Paths, FX Integration, Design)

**Source:** [YouTube](https://www.youtube.com/watch?v=_Fu8yl_p0vM)
**Author:** Compositing Academy
**Duration:** 57m29s | 14 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Introduction (Hit LIKE!) [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to part 3 of this Nuke series.
[0:12] So this is the final video in this kind of 3-part series.
[0:16] So if you haven't seen part 2 or part 1, as well as the trailer that kind of showed the
[0:21] breakdown, go check those out first.
[0:25] But yeah, this is what we're going to cover in this specific video.
[0:28] So we're going to cover the flow paths, which is again that geometry that was generated
[0:33] out of virtual reality tilt brush.
[0:36] So Google has a software called tilt brush, if you guys aren't familiar.
[0:39] So we're going to briefly talk about that and why we use that.
[0:42] We're going to also talk about some of the bigger effects that we're using here versus
[0:48] the smaller ones, kind of the ones going through the cracks versus these kind of broader areas
[0:53] that go through the skin.
[0:56] And some of the effects that kind of come off the edges and big embers, small embers,
[1:01] and cloth energy effects.
[1:03] I mentioned it a little bit in the last video, basically how that was done, but we're going
[1:07] to take a closer look.
[1:09] And yeah, animated roto paint strokes.
[1:12] So we have some kind of masks that reveal our moving patterns, element interaction, which
[1:18] is partly, you know, some of these cracks are lighting up some smoke around it.
[1:23] You're also lighting up the face around it.
[1:26] So it's not like you're just, you know, A over B sticking effect on there.
[1:29] Really you always are concerned with interaction.
[1:32] So this is interaction between multiple elements and also interaction, you know, just light
[1:36] interaction.
[1:38] So those are all things we want to think about and we'll talk about it.
[1:42] And then we just have some volume rays and stuff like that at the end.
[1:46] But yeah, we'll start by talking about the flow paths.
[1:49] So yeah, basically, like I mentioned in the earlier video, I didn't want to just mask
[1:55] some of these cracks and have a glow coming out because that's not that interesting.
[2:00] What we want to do is have a texture flowing through different directions.
[2:07] And you could use a grid warp for, you know, basic, you know, some of the ones that are


### Discussing Flow Paths [2:09]
**Transcript (timestamped):**
[2:12] less curved.
[2:15] So when there's not that much curvature, you can of course use a grid warp or something
[2:19] like that.
[2:20] But where we have like these cracks that are really going in different directions, so there's
[2:24] a lot of curvature.
[2:25] You're not going to want to sit there with a grid warp and try to warp and bend every
[2:29] little curve to try to get that thing, you know, going in the right direction.
[2:33] That would take you a lot of time.
[2:35] So again, thinking about saving time.
[2:38] And that's kind of what this technique does is like we can draw all of these basically
[2:43] geometries out in tilt brush.
[2:46] And that will just tell us where the texture will kind of stretch across.
[2:50] So one way to think of this and really, if I just draw it out real quick.


### Flow Paths Explanation [2:54]
**Transcript (timestamped):**
[2:56] So one way to draw this out, and I'm going to use a third party drawing thing here just
[3:00] so it's a little bit less laggy on the roto paint.
[3:03] So basically what we're trying to do is if we want a texture to be wrapped to something
[3:08] that's really, really curved, so something like this, we have like all this crazy line
[3:13] here.
[3:14] We don't want to sit there and grid warp that.
[3:16] So that's really easy to do in 3D if the UVs are mapped in a certain way to it.
[3:21] So if you were to model something like this in Maya, the problem would be you'd have to
[3:25] come up with a way to basically, you know, kind of project the UVs in the right way.
[3:31] And what I mean by that is if let's say you have a texture you want to flow across this
[3:36] path, which is exactly what we're doing.
[3:39] Basically what we want is the UVs to be kind of normalized.
[3:44] So basically the UVs would be zero and one like this.
[3:49] And basically you can think of it like this as well.
[3:52] So if we wanted to visualize that in UV space, obviously we have all this kind of warped
[3:57] thing, but in our UV space, if we were imagining this in our UV space, our texture space, zero
[4:05] would be here and one would be here.
[4:10] So that's how we want our UVs mapped.
[4:12] So it's basically just something like this.
[4:16] And so when we put our texture on here in this, you know, basically horizontal space, we can
[4:21] design it much easier than, you know, bending a bunch of stuff and trying to design a bent
[4:26] design.
[4:27] It just doesn't make sense to work that way.
[4:29] So yeah, that's what we're trying to do.
[4:31] And there's different ways to do it.
[4:32] You can go into 3D and for example, if you were to go into Maya and do this, you know,
[4:37] you could start with a geometry like this and you could basically extrude, you know,
[4:43] it's basically just a bunch of cards or, you know, a plane that's extruded along this
[4:46] sort of curvature.
[4:48] And that's one way to do it.
[4:50] But when we're working in tilt brush, this is why I use tilt brush because tilt brush
[4:54] does this automatically and it already projects the UVs into something like this because the
[5:01] way tilt brush is kind of putting textures on the geometry that they create, it's just
[5:07] already doing this.
[5:08] So yeah, we can basically set it up, just draw our strokes and export those and it will
[5:14] basically save to your Oculus in a folder.
[5:18] So if you guys want to look into that, you can just go open up tilt brush and, you know,
[5:21] in the settings, there's an export button and it will just come out as like an OBJ or
[5:25] something like that.
[5:26] And, you know, you can work with that file.
[5:30] So one thing to think about as well with that, there's one thing to mention if you're going
[5:35] to do it yourself or if you want to play around with tilt brush, there is different brushes
[5:40] in the software that export the UVs differently.
[5:43] And the only reason I know this is because I actually kind of experimented around with
[5:46] it and I realized this specific thing I was looking for, this whole kind of the way the
[5:53] UVs are kind of laid out here.
[5:54] It only happens with specific brushes.
[5:57] So for example, if you're going to use, there's one called like a tapered duct tape kind of
[6:03] thing where it's kind of mapping the texture like this.
[6:08] So that's how I knew that it was actually doing this.
[6:10] It's kind of creating this tapered effect at the end.
[6:14] It just looks like a flat sort of paint stroke, but it's creating this taper effect.
[6:19] And so that's the one you want to use in tilt brush if you want to get these UVs coming
[6:23] out in the correct way.
[6:25] You know, you want the UVs to kind of stretch one picture across the entire length of the
[6:29] geometry.
[6:32] And some of the ones in tilt brush, I think, you know, again, we said we wanted UVs to
[6:37] look like this.
[6:38] We want it to be zero to one.
[6:41] But some of the other brushes in tilt brush kind of, I think they use multiple tiles.
[6:46] So if you guys are familiar with like a more advanced UV layouts, you can actually go beyond
[6:51] the zero to one space and you can like use multiple kind of UV tiles.
[6:57] And I think some of the other brushes in tilt brush do this.
[7:00] So that's not going to work because, you know, we want to have one texture going across the
[7:03] entire thing.
[7:05] And what tilt brush is doing with the geometry in the in some of the other brush styles is
[7:08] kind of stretching it across multiple UV tiles.
[7:11] So that's not going to work.
[7:13] So basically very simple way to think about it.
[7:16] Just use the one called tapered flat.
[7:21] So if you look for the tapered brushes, it's going to work for you and you're going to
[7:24] get the correct geometry to do this type of thing.
[7:27] Now, somebody in the comments, I think said some other softwares do this.
[7:31] If you guys know any softwares, by the way, feel free to comment, you know, that kind
[7:35] of cheaps its effect.
[7:36] Somebody said Maya paint effects might do this laying out the UVs automatically in this
[7:40] way.
[7:41] I know blender and there's some plugins that kind of do this for pipes because people who
[7:45] are if you're doing like a curved pipes, this is a common problem where you have like these
[7:51] pipes that need to be laid out in a certain way so you can texture them.
[7:55] So yeah, there's different ways to do it, but this is just a quick and easy way.
[8:00] So we'll look a little bit more into the flow paths and how I put the effects on those geometry
[8:05] once we get to the lines part.
[8:06] But now I'm going to talk about the effects bigger part, which is basically these areas
[8:12] of skin that aren't really like cracks, but they're more like open.
[8:17] You see these kind of multi layered sort of fluid energy going across.
[8:23] And yeah, so we'll cover that part and then we'll kind of go into how that combines with
[8:27] sort of the cracks.


### Designing Main Effect [8:28]
**Transcript (timestamped):**
[8:28] So when I was doing the look development for this and designing how this is going to look,
[8:34] I started to think of it basically as two different effects like there's the cracks
[8:38] and there's sort of the effect underneath.
[8:41] So they are basically two different things happening there.
[8:45] And yeah, we just want to blend them together to make it feel kind of as one cohesive effect.
[8:50] But yeah, so that's kind of how I was experimenting.
[8:54] And when you're doing look development as well, it is a development.
[8:58] It is a design.
[8:59] So you are experimenting.
[9:00] You're kind of playing around with you start with a concept at least, but you still might
[9:06] not know exactly what it's going to look like in the end.
[9:08] And so it's kind of an experimentation phase playing around phase and seeing what will actually
[9:13] look good.
[9:15] So I'm going to go down to that now.
[9:17] So basically, yes, in these skin areas is where I wanted that effect flowing and then
[9:21] obviously any any cracks I wanted that to be in the cracks as well.
[9:27] But we'll just look at the skin areas first.
[9:29] So after I desaturated this and this part of the script as well, since we're at the
[9:34] top of the script, we don't have any of the face cracks and stuff we did that all comes
[9:38] later.
[9:39] So really just focus on the torso area right now.
[9:44] So basically what I did was the same kind of crack mat we talked about earlier on the
[9:48] last video.
[9:50] So we have something like that basically same idea, frequency separation.
[9:53] I did some color corrections in RGB channel.
[9:57] And then I just basically, you know, the frequency separation doesn't work completely perfectly.
[10:03] So what I did was kind of just filled in those areas because I want that effect to appear
[10:07] on those skin areas.
[10:08] So I just kind of wrote a painted some manual stuff there.
[10:14] And of course, don't remember, don't forget to frame hold this as well, because this is
[10:19] going to be this alpha is going to be stuck on using an ST map.
[10:23] So we already have our ST map.
[10:24] We already did that work in the last video.
[10:26] So if I let this play, we can see, you know, we have this like warping alpha.
[10:31] And even at the start, it's not completely perfect.
[10:33] You see some of these warps don't follow perfectly, but primarily it's in the crack areas over
[10:37] here and it works pretty well in the end results.
[10:40] So it doesn't really matter that this looks like this.
[10:44] So basically I just kind of slice this up.
[10:47] And yeah, so this is our mask that we're going to use for the effect.
[10:51] So basically how I did the effect.
[10:54] We have this effect here.
[10:57] So we have one of the effects that provided in this project.
[11:00] So we have these different simulations that we can use.
[11:03] And again, the reason I created these, and I'm going to make another video talking much
[11:07] more detail in the next weeks here as I release this pack.
[11:12] But you know, I was kind of just tired of doing all of my look development with the same
[11:16] node, which is like, there's like two or three nodes in nuke, which is for look development
[11:20] or kind of doing creative stuff to have like not that much choices of stuff to use.
[11:26] There's a couple other ones here that you can use, but really not that much to work
[11:30] with.
[11:31] And it's impressive how much you can actually do with with a few nodes and that limitation,
[11:35] that creative limitation, you can do quite a lot.
[11:38] And I've done a lot of stuff with noise and projecting that or wrapping that on objects.
[11:43] But I wanted to make something that kind of gives us a better starting point to just make
[11:49] more interesting effects and just kind of opens that creative door for compositors.
[11:53] So that's what this pack is going to do for people.
[11:57] And basically I created for myself more than anything just because I wanted to create some
[12:01] stuff like that.
[12:04] So this is the effect I started with, which is kind of just like flowing sort of effect
[12:10] here.
[12:11] I use this effect in multiple different ways in this shot.
[12:13] So this is just one way to use it.
[12:15] But basically I kind of did a time offset.
[12:18] You see this is called time pin.
[12:19] It's kind of a custom node, but really all it's doing is just it's the same exact things
[12:23] as the time offset.
[12:24] It's just, you know, you can be lazier with not having to do the math of how many frames
[12:30] need offset.
[12:32] So basically I did a little bit of time offset and I did a really strong grade.
[12:37] So I really just wanted to isolate the kind of bright edges on there.
[12:41] So I did a bit of a gamma and a gain here.
[12:46] So a little bit of a multiply down and a little bit of red into the darker edges.
[12:53] And it looks like a little bit of kind of reddish orange into the highlights as well.
[12:56] So just a grade giving you that kind of intense look.
[13:01] And for this thing, kind of the same idea.
[13:04] So we have this, let me just look at it here.
[13:07] So we have this kind of nebula sort of explosion.
[13:09] So this is kind of going underneath it.
[13:11] So I'm combining these two effects and using them to create kind of a new effect.
[13:17] And that's kind of the intention with the SPAC as well as like, you know, same as a noise
[13:21] pattern, you can combine noise patterns and create a new effect rather than just having
[13:25] one single noise pattern.
[13:27] So if you have 200 effects that basically look better than a noise pattern, you can
[13:33] combine these in different ways and design new stuff.
[13:37] So if you guys are familiar with like kit bashing, that was kind of the idea with this
[13:41] whole project that I've been working on for the last few months is like, if I can make
[13:44] something for composters, that's sort of like kit bashing, but for composters with these
[13:49] energy effects.
[13:50] And if there's enough variety, you can basically design new stuff using those elements.
[13:56] So rather than just using this as here's the effect and you're done, you can combine these
[14:01] in different ways.
[14:02] So yeah, so I did the same kind of thing, graded it down.
[14:07] I think I actually end up using this as a mask and said, so yeah, so this is what the
[14:12] final effect looked like, but I was using it as a mask rather than combining the two.
[14:17] I think originally I had started the project trying this out and the whole thing, the whole
[14:21] shot just looked kind of glittery, which is cool.
[14:25] This is still a cool effect, but it's not exactly what I was going for.
[14:29] So rather than using it just as this effect, I actually just use it as a mask to mask off
[14:34] this sort of Emory lines that we did.
[14:39] So that's going to kind of use that explosion animation from this one and just kind of reveal
[14:45] our other pattern in a more organic way.
[14:48] So you can see like it looks like this other effect is actually spreading upwards.
[14:53] So if I let it play, you can see how it looks like it's starting to kind of spread.
[14:57] And that's going to be a more organic way to kind of reveal this effect rather than
[15:03] using like a roto feather.
[15:04] Like it's not just going to be a feathered edge.
[15:06] You're going to have like all these little, you know, nice, basically cut out edges in
[15:12] the way that it's revealing.
[15:13] So that's one way you can kind of use these effects.
[15:18] And yeah, and then I did a little bit of a warp here.
[15:21] So one of the things I noticed when I had stuck this onto the thing, the picture, everything
[15:28] felt like it was just like a 2D video being masked by the cracks.
[15:32] So really what I wanted to do is like look at the kind of angle of the neck here and
[15:38] have the effect kind of flow backwards across the neck.
[15:42] So these kind of flow up and then some kind of flow backwards.
[15:45] And that's really simple by just doing a rotation to fake the perspective.
[15:51] And then the next part here, we have another part of the effect.
[15:57] So this is a different effect that's provided.
[16:00] And basically this one looks more like kind of liquidy stuff.
[16:04] But again, you know, the goal with these effects is not to just create something that you just
[16:09] stick over.
[16:10] Like it's sort of an element to build with.
[16:13] Like I said, it's kind of like kid bashing for composers is how I was thinking of it.
[16:17] So if we take this and kind of do some sort of corrections, this effect already looks
[16:23] completely different than this thing.
[16:26] But just to demonstrate, you know, you could easily go in so many different directions
[16:30] with this, you could go, you could go into some kind of blue, you could do more of a
[16:35] fluid type of thing.
[16:36] You can mask some other effects through this.
[16:40] And this is going to be a force field.
[16:41] This could be all kinds of different stuff.
[16:42] So really it's a versatile way to work to have just a better base to start with.
[16:50] So that's looking like that.
[16:52] And then basically, again, I was doing the same sort of trick here.
[16:55] I was using that explosion effect really as just a mask to kind of reveal that kind of
[17:01] fluid pattern.
[17:03] And what that does is it's starting to make it feel like some kind of electrical kind
[17:08] of fluid.
[17:11] And there's a million different ways you could design this shot.
[17:14] You know, if you're doing this shot yourself, you don't have to necessarily or maybe even
[17:20] make it a goal not to make it look the same.
[17:22] Like you can do different stuff.
[17:24] You can make it a different color.
[17:25] You can do different ways to approach this.
[17:28] But this is just to show you kind of the way I'm thinking about it as I'm kind of designing
[17:33] the shot.
[17:35] So I combined those two effects.
[17:36] We have that kind of thinner one.
[17:38] And then we have that sort of more streaky electrical.
[17:41] And then we're just merging them over each other.
[17:44] And then that's kind of actually the main effect of the body.
[17:47] So we have this whole thing flowing through.
[17:49] And then I just added some 2D motion blur as well to kind of blend everything together.
[17:54] After that, one thing to note is to use these NAND killers sometimes.
[18:03] So this is not actually a node, but you can do an expression.
[18:06] The expression is right here.
[18:07] Sometimes you'll get nodes that are called NANDs.
[18:10] And basically it's just like, you could just think of it like a broken pixel.
[18:15] And it just means it doesn't understand what the value of that pixel is anymore.
[18:19] Sometimes this will happen when you have like crazy high values or like negative values.
[18:25] So some of these effects are pretty bright inner values if you look at some of them.
[18:29] But this kind of fixes it.
[18:30] So if you just write this expression in expression node.
[18:34] So if you ever sampling around, like if I'm holding control and I sample around, if you
[18:37] ever see a pixel that says NAN, that means you have a NAND.
[18:41] And you want to kind of go up the chain in your script and figure out where that's happening
[18:45] and try to kill that so it doesn't keep going.
[18:48] So there's two ways to fix it.
[18:49] You can either put a clamp with a really high value.
[18:52] Sometimes that works.
[18:53] Otherwise, you can do this expression here.
[18:56] So if you create an expression node and put this in the three boxes, it will get rid of
[19:01] that broken pixel.
[19:02] So if you ever run into a problem and you see really weird stuff happening, check to
[19:06] see if it's a value when you sample it.
[19:09] Is that NAND?
[19:13] So we keep going down here.
[19:16] And what else do we have here?
[19:22] It looks like I just added some kind of sparkles on the edge.
[19:25] So I use that same effect, but I actually did merge a little bit over it over just to
[19:29] soften it because it was getting a little bit contrasty.
[19:33] And that's something you're not going to notice when you're designing it.
[19:36] Like I'm looking at this over black.
[19:38] But you know, when I'm designing, I'm probably looking here in my script.
[19:42] Like I'm looking at kind of over the background.
[19:45] What does it actually look like over the picture?
[19:49] But I'm kind of showing you the script in this area.
[19:54] And yeah, that's pretty much it for that, for the big effect there.
[19:57] So one thing I did as well, I mentioned it briefly in the last video, was sort of using
[20:04] the same effect.
[20:06] Let's just go here.
[20:08] So we have this whole effect.
[20:09] I actually use the alpha here to kind of darken the skin that the effect is going over.
[20:19] So that's kind of just a weird, it's not like, there's no technically correct way to kind
[20:23] of merge something like this over.
[20:25] So it's kind of a cheat to just use an over here, but it gives it this different look
[20:31] where it's making the skin darker versus just using a plus.
[20:34] If I were to just use a plus, you know, it's going to look like that.
[20:40] And then you can't really see anything.
[20:41] So that's not really useful.
[20:45] So basically, I think I just kind of created a bit of an alpha here to kind of make it.
[20:51] So basically, if you have an alpha here, even in the dark areas, that's going to be merged
[20:55] over with the effect.
[20:56] So that's kind of how that's being done.
[20:58] There's many ways to do it.
[20:59] You could just use a grade beforehand as well.
[21:02] You know, and just use like a key of some of this area and maybe darken around.
[21:07] So basically your goal is to just darken below.
[21:12] And my goal of the series as well, I've said it before, don't try to copy everything in
[21:17] the script here.
[21:18] It's just not going to happen.
[21:19] It's not, you shouldn't be focused on the nodes at this point.
[21:22] Like when you start to get into more like creative and building things out, the nodes
[21:28] become less important.
[21:30] Whether it becomes more about the way you're thinking about it.
[21:34] And yeah.
[21:38] So and then we just did some glow.
[21:39] So basically, we just took the effect.
[21:41] I used a dreaded hidden input here.
[21:44] I really, really avoid these.
[21:46] I very rarely use these, but I didn't want to, I had to use a piece from up here.
[21:51] I use some of the crack effects.
[21:52] We'll talk about that in a second, but try to avoid using these.
[21:56] It's very, at least if you're working professionally, if you're working professionally, it's very
[21:59] annoying to pick up people's scripts to use hidden inputs.
[22:03] I do use them occasionally, but like I said, it's not the best teaching thing to show people
[22:09] to use these because it's super annoying to pick up.
[22:13] Yeah.
[22:14] So then we use a little bit of an exponential glow and just plus it over kind of standard
[22:18] stuff here, a little bit of volume raise as well.
[22:21] So we can kind of get these nice little rays coming out.
[22:24] And you can even go a little bit more detailed if you want.
[22:26] You can even put some slight mist or smoke break up in there if you want it.
[22:30] In this case, I didn't.
[22:31] I think I use some stuff like that later on.
[22:34] Let's just go down.
[22:40] Okay.
[22:43] So this is some of the edge effects here actually.
[22:44] So we'll look at that in just a second.
[22:47] We'll go back up now and look at some of the crack effects because the crack effects are
[22:53] a different part of this shot.
[22:55] So if I just disable all this stuff, what we just talked about is actually just this.
[22:59] It doesn't have the cracks going through.
[23:02] So this is just filling the gaps around the edges.
[23:07] So I'm going to go back up here and kind of work backwards now.


### Flow Path Effects [23:08]
**Transcript (timestamped):**
[23:10] So now we're just going to focus on that piece.
[23:13] We have, again, back to our base picture.
[23:17] One of the things I did was do some light interaction from these cracks.
[23:23] How did I create these cracks?
[23:24] So again, this is a totally different effect.
[23:26] So what I'm going to do is go over here and take a look at this.
[23:29] So here's our geometries from Tilbrush.
[23:33] The things I already talked about.
[23:34] So they look like this.
[23:36] You don't necessarily have to do this UV thing.
[23:39] You could plug the texture itself directly into the geometry like this.
[23:46] And that might even be a better way of doing it.
[23:48] I'm not quite sure even why I did it this way.
[23:50] I think I was just thinking about UV and stuff like that.
[23:52] But it's actually not necessary.
[23:53] You could just directly plug in a texture and it's going to wrap those geometries.
[23:58] It's just something to think about.
[24:00] But anyways, I did it this way.
[24:01] It doesn't really matter.
[24:04] And you can see that these textures are stretching onto the cards.
[24:07] So what is this texture?
[24:08] It's literally the same effect we used before, but I'm using it in a different way.
[24:12] So I'm just kind of grading it down, retiming it and kind of getting something that looks
[24:17] like this.
[24:18] So again, remember, our zero is over here.
[24:20] Our one is over here.
[24:21] So this texture is automatically going to map to that geometry.
[24:25] And then one thing I did was kind of stencil some kind of edge breakup around the edges.
[24:29] So I created an alpha that looks like this.
[24:32] So we have like a noise pattern.
[24:34] We have like a ramp alpha that's created with some rotos and stencil it.
[24:39] So we get something that looks like this.
[24:40] And if we stencil that from our original picture, it will just make it so our edges aren't super
[24:45] sharp and you're not going to see like kind of CG looking edges.
[24:50] And then just ST map that.
[24:53] And you'll notice how it's all mapping on there.
[24:55] So if I disable the edge breakup, you can see that it really does help to kind of do
[25:00] that.
[25:01] And yeah, so you can kind of move this into place.
[25:05] And basically what I did was so we're going from this, this 3D sort of thing, we're putting
[25:11] the texture on it, but then we're actually just sticking it back on in 2D.
[25:15] So we're just going to take this as a picture or a video rather.
[25:19] And it's not even moving.
[25:20] It's just, you know, the textures are moving, but nothing else is moving.
[25:24] And we'll just stick it on again, using the stuff we already did, the smart factors.
[25:27] So we can take this whole fact, stick it onto the smart factors.
[25:31] And now this effect is going to move with the person.
[25:34] So if I kind of step through, it's hard to tell here, but you can see that it's actually
[25:37] sticking now.
[25:38] And that's the majority of the work you need to do.
[25:43] So that's how I did basically all of these effects.
[25:47] We have like these little ones and they're being stuck on using the same kind of smart
[25:58] fact that we rendered out.
[26:01] And then the other thing you're going to need to do is just go down further.
[26:05] Let's just go here.
[26:10] So this is the same idea.
[26:12] It just looks like, yeah, so I didn't have every single crack drawn out with this geometry.
[26:17] So what I did was I kind of just, I took some of the ones that were in this scanline render
[26:24] and I just like said, okay, I'm going to take this piece and I'm just going to like grid
[26:29] warp it.
[26:30] So it kind of already has like most of the bend in there that we need, but I could just
[26:33] kind of go there and make some adjustments to it and then add that back over as a new
[26:37] one.
[26:38] So I like basically created a bunch of like more cracks by just like grid warping the
[26:44] same pattern over and over and just kind of sticking it everywhere.
[26:47] And then just kind of ST mapping or texture on the end.
[26:53] And then we can just stick on the track as well.
[26:56] So at the end, you have something like this.
[26:59] So this is your precomp and we have like all of our effects flowing through.
[27:04] And you see, I did some basic roto shapes to kind of animate them in.
[27:09] And that's fine for this specific effect because they spread pretty fast.
[27:12] So I just use some basic roto shapes to kind of feather them in as they appear.
[27:16] But later on in the face, we can do a more advanced reveal with roto strokes.
[27:21] So they kind of have more offset.
[27:23] But since this is the beginning of the shot, it was more of an explosive start.
[27:27] So if you look at the effect, it's kind of going pretty quickly as it's coming in.
[27:34] And actually as it goes to the face, it's a little bit slower the way it spreads.
[27:41] So yeah, I wasn't as concerned with like every single tendril or every single bend appearing
[27:45] differently down here.
[27:48] But it still gives the effect.
[27:49] So we still see that these are kind of appearing a little bit faster than our base effect.
[27:54] So again, this is design like you want to think about when are things appearing in the
[27:58] timing and you're not going to get the timing right perfectly the very first time.
[28:02] Like you need to adjust things relative to each other and make make the timing feel kind
[28:06] of natural.
[28:10] And yeah, so that's pretty much it for that.
[28:12] So let's just see what else we need to cover here.
[28:15] So we covered the bigger effects.
[28:16] We covered the lines in the body.
[28:19] Now I want to talk about the effects in the edges.
[28:22] So like what happens when these effects start to flow up and hit the edges?
[28:28] And we don't want to make like the whole shot look like a 2D effect, even though we're using
[28:31] a lot of 2D mix of 3D and stuff like that.
[28:35] There's giveaways that CG is CG.
[28:38] And usually that's around your edges.
[28:39] So we're going to talk a little bit about that now.


### Edge FX [28:42]
**Transcript (timestamped):**
[28:43] So in terms of the edges, we can look here and this is kind of what I was talking about.
[28:48] We see these kind of effects hitting the edge and there's already a lot of contrast right
[28:53] here on the edge, just from the plate from like the footage because we have like spear
[28:58] black and then it's like very straight edge.
[29:01] And this is the kind of thing that is always catching my eyes a composite.
[29:04] I always know if I'm not trying to draw your attention there, usually I want to do something
[29:08] to soften that out.
[29:10] And so one way to do it rather than just color corrections and stuff is to actually use some
[29:14] effects there.
[29:16] So what I decided to do was like as these effects kind of come up towards the edge, if I just
[29:22] pause.
[29:24] So these these hot parts of the effects, the kind of blown out areas will come up and I
[29:29] wanted some like flames to kind of be left behind for like a couple frames, like two
[29:34] or three frames just kind of linger behind.
[29:37] So what I did was if I just zoom in and see if I think it'll be cash here, just try this.
[29:43] Okay, so what I did is in fact a little bit like this.
[29:47] So if I'm zooming in quite a lot here, give a second to cash.
[29:55] We can see as those highlights roll up, it kind of reveals a little bit of flames like
[30:00] flickering off the edge and that just kind of softens the edge makes your eye.
[30:06] If you happen to glance there, it kind of is okay for your eye.
[30:10] It's not like distracting or feeling fake by just adding a little bit of detail there
[30:15] because it was lacking detail and there's a little bit too much contrast.
[30:17] You see it's reducing the contrast because the we're kind of getting a somewhat of a
[30:22] semi transparent effect fading off in the black versus this harsh edge.
[30:29] And so the way I created this effect was I just took the so we have this effect again,
[30:34] another provided effect here.
[30:36] You could do this with noise pattern no as well if you want it, but this effect kind
[30:39] of looks something like this.
[30:42] So we could let it play.
[30:43] So we have these nice flames kind of coming off.
[30:47] So this will be part of the look dev pack I'm releasing as well, one of the 200.
[30:53] And so basically I took the effect, the kind of a pre comp of the shot and I keyed the
[30:59] highlights.
[31:00] So I just keyed out the very brightest area.
[31:03] And then what I did was I did time echo.
[31:05] So what I wanted to do was wherever a bright piece comes up, it'll create a flame.
[31:10] But I don't want the flame to disappear as soon as the bright kind of piece disappears.
[31:15] I want to linger behind.
[31:17] So what I want to do is with a time echo with some frame, some frames that are kind of fading
[31:22] out.
[31:23] So what that does is kind of creates an alpha that looks like this.
[31:27] So it's like a lagged version of the highlights.
[31:29] And if we take that and then we put a God right through it, you just have to think about what
[31:34] we're doing.
[31:35] It's like wherever there was a hot piece, it will leave a flame behind in that kind
[31:40] of ray and it will fade off over a couple frames rather than just vanishing.
[31:45] So if we take that and we mask our other fact, we get something like this.
[31:49] So this is kind of how I want about creating it.
[31:55] And then we can just take this effect and kind of add it over and then we get some nice
[31:59] like lingering flame effects around the highlights and around the edges.
[32:08] And yeah, so that just helps break up the edge.
[32:09] If you go to the final comp at the end and you let it play, you can see it just as just
[32:14] adding that extra level of detail as something moves up towards the top, you just get that
[32:20] nice subtle effect around the edges.
[32:22] I did it a couple of times, I think on different layers, but basically the exact same technique
[32:27] of just getting tiny little details coming off, kind of with that time echo lag in that
[32:33] area.
[32:36] So what else?
[32:37] Let's see.
[32:40] Yeah, edges.
[32:42] Embers.
[32:43] So embers is quite a lot of stuff.
[32:45] Embers plays a big role in this shot, obviously, because as our body effect is going up, one
[32:52] way to make it feel less 2D and more 3D is to have things coming off the surface.
[32:57] So this is a really good opportunity to do some embers and it totally goes with the style
[33:01] effect that I was trying to achieve.
[33:04] So we have some embers that provided you can simulate embers and nuke as well just by using
[33:09] some nuke particles.
[33:12] But I've already rendered some nice a nice simulation for anyone picking it up and you
[33:17] get something like this.


### Embers Small [33:20]
**Transcript (timestamped):**
[33:20] So let's look at it.
[33:23] So here's our effect here.
[33:25] If I turn the gain down a little bit, we do have some nice value differences in there.
[33:29] So we see some are brighter and some are darker.
[33:32] So this is already a really great starting point.
[33:35] And as a compositor, I'm really used to starting with elements.
[33:39] And that's why I think it's hard to do YouTube channels with compositing because you don't
[33:43] have a lot of stuff to work with, footage and everything like this.
[33:47] So this is going to make it easier, this pack, to kind of make some more tutorials for you
[33:53] guys in a more interesting and realistic way of what a composer actually does in the real
[34:00] job.
[34:01] So yeah, we'll talk about the embers.
[34:04] Let's go down and see.
[34:12] So we have the bigger embers and the smaller embers.
[34:16] I'll talk about the smaller embers first because it's a little bit more straightforward.
[34:22] So if I just let this play, let's just go to a spot.
[34:27] Basically, yeah, let's just find a good frame.
[34:33] So some of these are brighter than others.
[34:35] So I kind of made some, these are like a little bit darker embers.
[34:39] But basically, you just have the embers, I did a time offset, masked like a piece and
[34:44] then probably had some NAND.
[34:46] So I use that same thing here.
[34:48] So if you guys create that NAND killer node, just save it as something and you can use
[34:51] it whenever you need it.
[34:53] Sometimes with this effects pack, you'll have those NANDs.
[34:55] So you just want to check that on there if you happen to get that.
[35:00] Basic glow and then just some really simple stuff.
[35:03] And you see, I did it, if there was trying to make some really hyper detailed embers,
[35:09] what I would try to do in this, if I'm looking at this specific effect is I would try to
[35:12] make some brighter than others and get a little bit more variation than we're seeing here.
[35:16] But in this case, there's a collection of a number of embers.
[35:20] So I do have some other effects later on that have the brighter ones and darker ones.
[35:26] So I'm thinking about the temperature of these embers.
[35:30] I'm not just thinking about, we need some embers.
[35:32] You want to think about where are the hot ones, where are the ones that are not as hot.
[35:36] Maybe they come out hotter.
[35:37] So maybe they would be a bit more yellow and white as they're coming out and then they
[35:41] would fade more into red.
[35:43] So you want to think about the physical properties as you're doing stuff rather than just, you
[35:50] want to put thought into it.
[35:53] And that's basically, yeah, I don't think I need to spend that much time on that.
[35:58] I guess the only other useful thing to know is that we can kind of mask some of these
[36:03] out by just adjusting the brightness.
[36:06] So if I don't want that many, I can simply go here, do kind of a color correction to
[36:11] the black point and the white point and even the gamma and just like crunch it.
[36:16] And we can use that to actually mask out the original.
[36:19] And you see that it kind of just gets rid of a bunch of the embers without having to
[36:22] do much work.
[36:23] So we're kind of like having the amount there.
[36:27] So we have like a few.
[36:29] And yeah, that's pretty much it for the small embers.
[36:33] Let me just go up here.
[36:37] And then we have like some glow on them and everything like that.
[36:39] So all the basic stuff.
[36:45] And I'll talk about a little bit of the light interaction later on because some of them are
[36:48] actually casting light on the smoke around them or casting a little bit of light onto
[36:54] the skin.
[36:55] I don't think the embers are actually casting light, but we do have some light interaction
[36:58] from some of the elements there.
[37:00] So yeah, now we'll talk about the big embers.


### Embers Big [37:05]
**Transcript (timestamped):**
[37:05] Let's just go find it.
[37:09] So big embers.
[37:10] So this is the render and providing you guys another simulation.
[37:15] So this basically has a few different passes.
[37:18] And you can use this for your own projects if you want as well.
[37:21] It's kind of a generic render.
[37:24] But basically we have a UV pass so we can wrap things onto this simulation.
[37:30] So if I hit play, just floating up like this.
[37:35] The beauty pass is basically just a red and blue ID pass.
[37:41] So if we want to color correct the top, we can do so.
[37:45] And if you want to color correct the bottom, we can do so because we have those two channels
[37:48] that we can just use.
[37:51] And we also have a position.
[37:53] We have normals if you really want to do something crazy with this.
[37:57] So you could even do some crazy chrome effect.
[38:01] There's ways to make reflections based off just normals and stuff.
[38:04] So there's all kinds of stuff you can do with this type of little thing.
[38:08] And that comes with the shot as well.
[38:11] But yeah, basically I just took the same effect.
[38:15] I put it on like a...
[38:16] So I took the footage, scaled it up to find a piece of the flat skin and just graded it
[38:24] to make it look a little bit more burned and then just put that effect over.
[38:28] So I have this effect just over the top of it.
[38:31] It's a bit low resolution the other thing, but it doesn't matter because the resolution
[38:34] we're shrinking this down to, it literally doesn't matter.
[38:38] So we're just getting this base color with some slight color variation in there.
[38:44] And then we can just ST map that to that UV pass that's shuffled out.
[38:50] So if you shuffle it out, you get something like that.
[38:52] And now you see we have like the darkness of it and we have the effect and the highlights
[38:58] rolling across the whole cloth.
[39:02] And we get this weird stuff on the edges where the background's changing colors.
[39:05] So what you can do is just copy the alpha from the original back in and then just, you
[39:11] know, you can pre-multiply it.
[39:13] I also use a little bit of the ambient inclusion to multiply in there.
[39:17] It doesn't really matter because the thing is so small anyway, but if you just want extra
[39:21] level detail, you can do that.
[39:23] So that's kind of how I did this whole portion.
[39:25] I also did a bit of an O flow, which is changing the speed of it because I think it was going
[39:31] a little bit too fast.
[39:33] Actually it's going too slow.
[39:34] It looks like I doubled the speed.
[39:36] So yeah, you can like change the speed of it as well.
[39:38] If you need to just make it kind of go with the effect that's coming off the skin.
[39:45] So basically you render this out as an element and let's go down here and see.
[39:54] So here's the element rendered out.
[39:58] And then I just did a bunch of color corrections.
[40:01] It looks like I did some slight O flows and read times as well so that they're not all
[40:04] moving the same speed.
[40:07] And then I just shrunk it down to wherever it's coming off of the skin.
[40:12] So I shrunk it down and then just time it up wherever the effect comes.
[40:18] So as the effect rolls to that piece of the skin, this piece will kind of peel off.
[40:23] And that's why I wanted to look like it's kind of like those cracks or dry skin sort
[40:26] of peeling away or like mud.
[40:30] And you get something like that.
[40:31] That's obviously not integrated.
[40:32] But if you do a little bit of a glow, it kind of matches the blacks for you.
[40:37] So I just took the little ember there, pre-multiply, exponential glow, slight color correction in
[40:44] the glow so you can get some slight red in the glow and then just kind of plus that on
[40:48] top.
[40:51] And I think they're all being done pretty much the same exact way.
[40:54] Let me just check here.
[40:57] This is not actually my final comp.
[40:59] So sometimes what I'll do when I'm comping is I'll do like a mini comp off the side because
[41:03] it's faster.
[41:04] So I'll just like pre-comp everything out from behind and then just do some new effects
[41:10] on top.
[41:11] So that's why I think this isn't even the final effect here.
[41:15] So if I go back to my mainstream, give it a second.
[41:25] So it's a little bit different, but let's just go front embers, cloth, color corrections,
[41:33] slight defocus, and that's pretty much it.
[41:35] So basically just have those chunks coming off.
[41:40] So yeah, a lot of it is just reusing stuff.
[41:41] A lot of it is kind of trying to think outside the box and the way that you can use those
[41:48] elements.
[41:50] So we can see here's some embers again.
[41:54] And these ones are a little bit brighter.
[41:56] So like I said, I did a lot of color variation in all of these embers.
[42:01] So I think that's enough for that.
[42:03] Let's go back to our description here.
[42:10] Cloth energy effects, big embers, small embers.
[42:13] So yeah, that's basically all that.
[42:15] Cloth energy effects is actually this stuff.
[42:17] So I'll just quickly go down to that as well.
[42:19] That's pretty straightforward.


### Cloth Energy Flow [42:20]
**Transcript (timestamped):**
[42:20] So I won't spend too much time on it.
[42:23] All right, so here it is.
[42:27] Basically this effect is very simple.
[42:30] It's just taking this thing.
[42:32] So we have this line effect that is part of that look DevPak.
[42:38] And I've just kind of reformatted it and done a bit of a grade to make it sort of more intense.
[42:44] And again, like I went back and forth.
[42:46] I kind of would just stick it on there, see what looks good or not, and then just sort of adjust it.
[42:52] So just a bit of a spline warp and grid warp to kind of get the shape and then kind of wrap it onto the shoulder.
[43:00] So usually what I'll do is I'll just do like the normal transforms, line it up, and then go back and do the grid warps and spline warps.
[43:08] And you see, I'm not worried that much about concatenation here.
[43:11] I could be more careful about it in terms of like, OK, there's a grade.
[43:17] You know, I'm not always worried about that stuff if you're losing a lot of resolution anyway, you're shrinking it down like.
[43:22] But generally when I'm teaching it, you know, you want to be a little bit more careful about those type of things.
[43:27] But especially when you're losing out with resolution anyway, and I'm going to defocus it, I'm not that actually worried about it.
[43:35] Usually when I'm trying to maintain quality, I'll be I'll be more worried about stuff like that.
[43:39] So yeah, basically it's just a bunch of strips that you take that same effect, shrink it down and just do some color corrections.
[43:47] To get it to look more like a gold type of effect there.
[43:52] And you can see at the end how that's going to look.
[43:57] So this is on the other shoulder, it looks like.
[44:01] So we get these like little drips and and it's sort of moving with.
[44:07] With with everything there.
[44:10] And this is a very subtle fact.
[44:11] I didn't want it to be overly.
[44:13] I actually made it less intense even through some of these other color corrections.
[44:17] I didn't want that to be the point of the shot.
[44:20] I just want it to be if you glance there, there's a little bit of something.
[44:28] So let's just go back.
[44:30] So cloth effects.
[44:33] Yeah, we'll talk about the animated roto paint and the element interaction.
[44:40] For the face, so that is a little bit more complicated stuff.
[44:44] So let's go to that part.
[44:48] So when we're talking about the animated roto paint, what we're talking about is some of the face effects.


### Face Effects and Animation [44:49]
**Transcript (timestamped):**
[44:54] So the face effects, I did the same exact thing as the body one.
[44:58] So I took the same basically stream type of thing that we already created before.
[45:06] And I use the same exact one for like the face.
[45:10] And some of them are coming from those ST map lines that I showed you guys.
[45:15] And some I just grid warped a bunch because there's not as much curvature in the face in the lines.
[45:22] So some of them I actually just use normal grid warps to bend these textures.
[45:26] So I didn't have to use the whole till brush thing because if it's just a slight bend, it's definitely something you could do.
[45:33] So let's just go up here.
[45:35] Just to show.
[45:39] So I'll show you.
[45:41] So we see it's kind of mixed, right?
[45:43] So we have, once we give a second to load, this one is the one from the geometries.
[45:50] So these are actual geometries that line up and we've kind of wrapped them on the head.
[45:58] So let me just make that more clear.
[46:01] Yeah, so here's our stuff.
[46:03] Here's our effect.
[46:04] Here's our lines from till brush.
[46:07] And then we're just doing the ST map thing again.
[46:09] And what we're doing instead of using smart factors to stick it on is we're actually doing this in UV space.
[46:16] So just to show you guys what I mean, this again, we're in a square format.
[46:21] We're in 4k square format.
[46:23] We have the flattened UV face.
[46:26] And what I'm doing is I'm lining up those lines on that UV layout instead of doing it from just like the normal footage.
[46:34] So some of the lines are provided basically line up with the face in that way.
[46:42] And if we keep going down, some of the lines, like I said, we're just grid warp.
[46:48] So I just added a bunch more just so that it would fill all the cracks.
[46:53] So just like, yeah, so that's kind of what it is, something like that.
[46:57] So this is till personal lines, and then we just add more.
[47:01] But when I'm talking about the animated roto paint lines, so now what we want to do is like we have the flowing effects, but we need to reveal this effects pass.
[47:10] So this is all sticking to the face because if we do it in UV space, run it out, it'll stick to the 3d model because we're using the keen tools model.
[47:18] And everything's running through.
[47:21] So let's just keep going here.
[47:24] It looks like I did.
[47:26] Yeah, so here's our crack mat that we created in the last video.
[47:29] So first things first, we take our effects, we put it only in the cracks.
[47:33] And that is solving the biggest challenge of getting into the cracks.
[47:38] The next thing we want to do is animate when they come on.
[47:41] So what I did was I went back into UV space again.
[47:44] So I went here, I kind of pre comp this face out in UV space.
[47:48] So if you go up to your 3d model and you kind of pre comp that out, it's useful to have that pre comp out because you can do all your work on there.
[47:56] So what I did was basically, let's just show here.
[48:02] Skip ahead in time so I can show this a little bit more clearly.
[48:09] Okay, so basically I just took these like roto paints and I would draw them on the face when I wanted the effect to appear.


### Rotopaint Animation [48:13]
**Transcript (timestamped):**
[48:22] So if you just draw a roto paint, something you can do in the settings in the stroke is to, I think is a stroke.
[48:31] Where is it here?
[48:32] Let's see.
[48:34] Yeah, so in the stroke settings, we have this right on end.
[48:39] So you can basically key frame that.
[48:41] So if you just draw a stroke, you can basically make it fade on.
[48:47] So it kind of like follows where you drew it.
[48:49] And basically you just want to draw those on that flat face and basically create like an alpha that will basically represent where all those cracks are spreading.
[49:00] So it's going to take a lot of little roto strokes, but as you do that, I kind of blurred them so they're a little bit bigger than the cracks themselves.
[49:08] So they're kind of like a little bit wider.
[49:12] But those will kind of reveal each individual crack as it appears.
[49:16] So if we go to the end result of what that looks like.
[49:19] So the end is not, it's not, it's more of just a feather, but up here you can see it's a little bit more specific in terms of like the way it's spreading.
[49:28] So you see it's kind of, they're moving at different speeds in different directions rather than just being, you know, a simple roto for the whole thing.
[49:39] You know, you want something to move sideways, you want something to move up and, you know, that will give you that variation.
[49:45] And then that's the fact we have.
[49:50] So after that, you can do some color corrections to make it more interesting.
[49:55] So what I did was kind of grade the edge on the very edge brighter.
[50:00] So you see, it looks to get darker over time.
[50:04] And that will really become apparent when we add glow.
[50:08] So if you do that and then you add the normal glow, you know, we're going to get an exaggerated effect in the highlights and much less in the dark areas.
[50:17] So it's going to look like it's really, really getting hot as it comes up.
[50:22] Also what I did, so that's just pus over glow.
[50:26] The other thing I did was like lumens key on the highlights and a little bit of volume rays coming out of some of the very bright areas.


### Extra Face Details [50:29]
**Transcript (timestamped):**
[50:34] And that will just give us some nice little like pings of highlights that pop out on certain frames for like really, really bright areas.
[50:44] And that just gives us some extra like little type of elements that give us some interest.
[50:50] Something like this.
[50:52] And I masked that through some noise as well.
[50:55] So you see, I kind of broke it up to make it look more like a mist.
[50:59] This is very subtle.
[51:01] You see, I did not make this super bright.
[51:03] I didn't go here and I didn't make these like really crazy bright.
[51:07] You could, but it's just not what I was going for.
[51:10] I made some brighter.
[51:11] So some here that a little bit brighter, but you see, there's still subtle.
[51:15] And that just gives it the extra level of detail without being in your face over the top about everything.
[51:25] So let's continue on.
[51:28] Let's check it out here at the top.
[51:33] So element interaction volume rays will cover that.
[51:36] So one of the things we want to do with an element interaction is to make these cracks interact with the face.


### Interactive Elements [51:38]
**Transcript (timestamped):**
[51:43] So like bounce lighting.
[51:44] So if I disable that, you can see there's actually a huge difference in the way that this doesn't look realistic if you don't have any kind of bounce lighting.
[51:52] So bounce lighting and light interaction really, really helps whenever you're integrating stuff and you always want to be thinking about it.
[51:59] And yeah, so it's very simple.
[52:02] What we did, we have the head model.
[52:04] So we can basically just chuck on, you know, point lights and just kind of animate them along with the cracks.
[52:11] So I just took the light position and you can kind of look at it in 2D and just, you know, sort of move it around and animate it in the same speed as your cracks.
[52:20] And so it kind of goes up and they're not ray traced lighting.
[52:24] Nuke should get a ray tracer.
[52:26] I don't know why it hasn't happened yet in terms of like getting better like shadows and stuff like that.
[52:32] These aren't true shadows and we could try to do a spotlight and try to do some depth map shadows, but it's just, it's more just a pain.
[52:39] Really what they need to do is add ray tracing and global illumination.
[52:44] I think that's what I think.
[52:46] But yeah, but basically the way we did it is just kind of take that and mask it through some basic, basically the plate with the Lumikey just to get some slight variation in the way that it looks.
[53:00] And when you look at that, you start to get, you know, something that's kind of interesting in the way that the highlights are catching.
[53:07] And if we plus that over, we're going to get a, you know, a convincing light interaction.
[53:13] And even though we're not doing completely ray traced physical shadows, not that necessary because the light is not bright enough to be like casting like super crazy shadows.
[53:23] Because we're just mixing that in just a little bit.
[53:26] Another thing about element interaction, we had the, let's see where it is.
[53:36] Just find it.
[53:38] Yeah, we had the head smoke.
[53:40] So this is another effect.
[53:42] But we have this layer which we pre-comped out.
[53:45] So this is like all the work I did before.
[53:47] I just pre-comped it out into a layer and kind of did some luminous key to get just the highlights and kind of glow those out like this.
[53:56] So you get this like pretty cool glowy sparkly effect.
[54:00] And what you can do is just multiply that against that smoke layer.
[54:04] And so from something that's just white and, you know, it's not that useful.
[54:08] If we multiply it through our effect, you know, we get something that's really cool in terms of the interaction of the elements together.
[54:17] And then I just did some like color corrections in different spots, you know, where, you know, for example, I, you know, I was fading off the effect down here.
[54:25] So maybe I just need to do some manual work there.
[54:28] Also, some of the highlights were just blowing out way too much like I was showing you guys in the first video.
[54:33] So I kind of was just killing those with some Luma keys and just sort of eroding out and then darkening those areas because I don't want to over, you know, glow things too much.
[54:45] And yeah, that's basically for the interaction of that.
[54:50] So you see by just taking the elements and making them interact together.
[54:54] That plays a big part.
[55:01] So yeah, here's the interactive smoke element.
[55:04] So this is literally just like a basic noise pattern.
[55:07] I might take one or two noise patterns and just kind of put them together and just slightly animate it upwards and then use the whole image behind as like a, you know, the same exact thing we just did with the other smoke.
[55:19] But with basically 2D noise pattern.
[55:22] So yeah, so if we just jump to that, this is kind of what it is very, very simple, but it is effective, you know, so we can, we just took the whole effect here from the chest area.
[55:38] Just did an exponential glow and then multiply it against this.
[55:41] And this is pretty heavy.
[55:43] So this might take a while unless I switch this.
[55:47] Let's see.
[55:48] So you see I use pre comps in all these different places to speed up my workflow.
[55:52] But yeah, you see, we get something like that and that's just going to help everything sit together by adding some thin layers of stuff like that.
[56:02] And that's basically it.


### Conclusion [56:05]
**Transcript (timestamped):**
[56:05] So I think the only part I didn't cover maybe was the tracking I said in the last video covering that area.
[56:11] I think I'll leave it out of this video for now just because this video is already almost an hour.
[56:16] But if you're doing the project and you have a specific question about that, I can send you, you know, basically explanation how to go about doing that.
[56:24] So yeah, that's basically it for the series.
[56:27] If you guys found it useful, hit the like button, hit subscribe and leave a comment if this is like if you want to see more stuff like this.
[56:35] Or if you want more short form tutorials and stuff like that.
[56:39] My intention is to kind of, I think I've said this before, but switch between, you know, maybe a beginner, you know, short form tutorial or intermediate short form and maybe some of these like project based longer stuff.
[56:54] And yeah, so it'll be kind of a mix between the two because there's some more senior people and some more people starting out.
[57:00] So I don't want to just make videos only for advanced stuff like this.
[57:05] But yeah, more about the energy pack will be coming in the next few weeks and that will be released on YouTube.
[57:11] You can go sign up as well on the website.
[57:14] So composingacademy.com slash follow.
[57:17] If you stick your email in there, you'll get notified as soon as this is available.
[57:21] And that will be a pretty cool thing to show off.
[57:26] So yeah, hope you guys enjoyed.



---

## Captured Frames

- [3:52] tutorials/frames/33-nuke-tutorial-series-flow-paths-fx-integration-design/frame_000.jpg
- [9:50] tutorials/frames/33-nuke-tutorial-series-flow-paths-fx-integration-design/frame_001.jpg
- [14:45] tutorials/frames/33-nuke-tutorial-series-flow-paths-fx-integration-design/frame_002.jpg
- [29:43] tutorials/frames/33-nuke-tutorial-series-flow-paths-fx-integration-design/frame_003.jpg
- [34:23] tutorials/frames/33-nuke-tutorial-series-flow-paths-fx-integration-design/frame_004.jpg
- [38:50] tutorials/frames/33-nuke-tutorial-series-flow-paths-fx-integration-design/frame_005.jpg
- [48:34] tutorials/frames/33-nuke-tutorial-series-flow-paths-fx-integration-design/frame_006.jpg
- [52:04] tutorials/frames/33-nuke-tutorial-series-flow-paths-fx-integration-design/frame_007.jpg

---

## Structured Notes

### Core Technique
Part 3/3, the finale: wrapping stock energy-effect textures onto heavily-curved paths using Tilt Brush VR geometry with pre-normalized 0–1 UVs (instead of hand grid-warping every bend), kitbashing multiple stock elements together by using one as an organic reveal mask for another, edge-detail tricks (lingering time-echoed flame at silhouette edges) to hide the "2D-ness" of CG elements, physically-motivated ember/cloth-energy design, animated RotoPaint-stroke reveals for organic crack-appearance timing, and interactive 2D point-lights + multiply-based element interaction so every effect visibly affects its neighbors instead of just sitting "A over B" on top of the plate.

### Summary
**Flow paths (frame_000, a hand-drawn curve diagram):** the video opens explaining *why* Tilt Brush (Google's free VR sculpting app) is used for the curved "flow path" geometry the energy textures travel along — texturing something with heavy, irregular curvature by hand-`GridWarp`-ing in Nuke is prohibitively slow, and building extruded-card geometry with correct UVs in a DCC (Maya) is extra modeling work. Tilt Brush's **"Tapered Flat" brush specifically** (not just any brush) automatically lays out a stroke's UVs normalized to a clean 0-to-1 space along its whole length — critical detail: other Tilt Brush brushes tile the texture across multiple UV tiles instead, which breaks a single-texture-along-the-whole-path design, so brush choice matters. Strokes are drawn directly in VR, exported (Tilt Brush's own export button, saved to the headset's storage) as OBJ geometry, and imported into Nuke's 3D system — a texture plugged directly onto that geometry (UVProject is optional, not required — the author notes he isn't even sure why he UV-projected in this project) automatically stretches correctly along the whole curve, matching the same "avoid brute-force node-by-node distortion when the right geometry solves it structurally" philosophy from earlier videos in the series.

**Main body "flow" effect:** built from the same crack-matte technique as Part 2 (frequency separation on the flattened UV face/torso, hand-painted fill-ins where the automatic separation misses spots, frame-held since it drives an ST map) used here as a mask rather than a final alpha. The actual visual comes from **combining multiple stock energy elements as masks for each other** rather than stacking them additively: a `TimeOffset`("TimePin")-shifted, heavily `Grade`d (isolate bright edges, push warm tones into highlights) stock flow element is layered under a second stock "nebula explosion" element used *as a mask* to reveal the first organically — frame_002/003 show this kitbashed compositing tree — producing cut-out, non-uniform reveal edges instead of a flat roto feather, which the author explicitly frames as the difference between "kitbashing for compositors" and just slapping one pre-rendered element over footage. A `Rotate`-based fake-perspective warp (not a true 3D reproject) is applied so the flow direction follows the neck's actual angle instead of reading as a flat pasted video. Where two effects are combined, the author flags a recurring gotcha: some stock elements have extreme bright/dark values that produce **NaN ("Not a Number") pixels** downstream — diagnosable by Ctrl-sampling a suspicious pixel and seeing a literal "nan" readout — fixed with either a high-value `Clamp` or a small reusable `Expression` node (three channel boxes) that zeroes out non-numeric values; the author recommends saving this as a personal gizmo since it recurs constantly when combining bright stock elements. **Edge softening via lingering flame (frame_003 context):** a hard black-plate-edge silhouette reads as an obvious compositing giveaway, so rather than fix it with grading alone, the author keys the brightest highlights of the flow effect, runs a `TimeEcho` on that key so bright hits "linger" for a couple of extra frames instead of vanishing instantly, feeds that lagged alpha into a `GodRays`-style stock flame element, and masks/adds the result at the silhouette edge — producing small flickering flame licks that soften contrast right where the eye is most likely to notice a fake edge. **Embers:** small embers (frame_004) come pre-rendered with natural brightness variance; the workflow is mostly standard (NaN-kill, `Glow`, mask-to-taste via a crushed black/white/gamma grade to thin out density) but the video stresses *physical* reasoning over just "add embers" — think about ember temperature (hotter = more yellow/white, cooling = redder) and vary color/brightness per group rather than uniform copies. Big embers (frame_005) come as a small multi-pass render kit (beauty with a red/blue top/bottom ID split for independent grading, UV pass, position, normals — enough to build reflections from normals alone if desired); the technique is find-a-flat-skin-area, grade it to look burned, `STMap` the ember render onto the UV pass, copy the original alpha back in (fixes background-color bleed at the edges), optionally multiply in an ambient-occlusion pass, retime for variety, then shrink/position at each "peeling" spot timed to the main effect's spread and finish with a pre-multiplied exponential glow (slight red push) plussed on top. **Cloth energy effects:** the simplest of the set — reformat + grade a stock "line" element for intensity, `SplineWarp`/`GridWarp` it onto the shoulder/cloth shape, kept deliberately subtle (author says he reduced intensity further than his first pass) since it's a background detail, not a focal point; concatenation/quality care is explicitly relaxed here since the element is being shrunk and defocused anyway (a general "know when precision matters vs. when it doesn't" note). **Face effects and animated reveal (frame_006/007):** face-area cracks reuse the Part-2 crack matte to isolate where effects show, then the *appearance timing* is driven by hand-drawn, **individually keyframed `RotoPaint` strokes** on the flattened UV face — each stroke's Stroke-tab "start/end" (birth/death) parameters keyframed so it fades on progressively, tracing the crack's actual growth path rather than a single uniform mask; strokes are drawn slightly wider than the crack itself and at varied speeds/directions per stroke for natural-feeling variation instead of a uniform spread rate. A brightness-graded edge (bright leading edge, darker trailing) plus `Glow` exaggerates highlights disproportionately as things "heat up," and a Luma-keyed highlight pass + light `VolumeRays` adds occasional bright "pings," masked through noise to break the pattern into something read as mist rather than a hard shape. **Element/light interaction (frame_007):** 2D point lights are manually keyed and animated in sync with each crack's spread (Nuke lacks ray-traced/GI lighting — the author explicitly wishes it had one), masked/varied through a Luma-keyed copy of the plate for subtle highlight catch, then `Plus`ed over for believable bounce lighting — author demonstrates the difference is stark by toggling it off. Smoke/mist elements are lit the same way but via `Multiply` instead of `Plus`: pre-comp a glow layer (Luma-keyed highlights, glowed) and multiply it against a separate 2D-noise-driven smoke layer so the smoke visibly picks up nearby light color/brightness instead of reading as a flat white/gray overlay untouched by its surroundings — the author frames all of this "does element A visibly affect element B" thinking as the single biggest lever separating a believable composite from a pile of separately-designed layers.

### Key Steps
1. For textures that need to flow along a heavily curved path: build the path as geometry in Tilt Brush VR using the **"Tapered Flat" brush specifically** (not other brushes, which tile UVs across multiple tiles instead of one normalized 0–1 span) — export as OBJ, import into Nuke's 3D system, plug a texture directly onto the geometry (no UVProject strictly required).
2. Build the main "flow" mask the same way as Part 2's crack matte: frequency-separate the flattened UV face/torso, hand-paint fill gaps, frame-hold (it drives a static ST map).
3. Combine 2+ stock elements as a *kitbash*, not a stack: grade/isolate one element's bright edges as a base look, then use a second, differently-shaped stock element (e.g. an "explosion" pattern) purely as a **reveal mask** for the first, producing organic non-feathered cutout edges instead of a roto feather.
4. Fake perspective flow direction with a simple `Rotate`/`Transform` warp so a 2D stock element's apparent flow follows the underlying surface's actual angle (e.g. neck curvature) rather than reading as a flat pasted video.
5. Watch for NaN pixels whenever combining very bright/high-contrast stock elements — diagnose by Ctrl-sampling a suspicious pixel (readout literally says "nan"); fix with a high-value `Clamp` or a small reusable NaN-killer `Expression` node (save as a personal gizmo).
6. Soften a hard CG-silhouette edge with a *lingering flame* trick instead of pure grading: key the brightest highlights of the effect passing near the edge, `TimeEcho` that key so hits fade out over a few extra frames rather than vanishing instantly, drive a `GodRays`/flame stock element with that lagged alpha, mask/add at the edge.
7. Design embers with physical logic, not just density: vary brightness/color per group (hotter = more yellow/white, cooling = redder), use a crushed black/white/gamma grade on the source render to thin out density to taste instead of manual per-ember masking.
8. For a multi-pass ember/element render kit (beauty + top/bottom ID split + UV + position + normals): grade a flat area of the plate to look "burned," `STMap` the element render onto the UV pass, copy the original plate's alpha back in to fix edge color bleed, optionally multiply in AO, retime per instance for variety, shrink/position/time to the main effect's spread, finish with pre-multiply + exponential glow (push warm) + Plus.
9. For lower-priority background detail elements (e.g. cloth energy lines): reformat + grade for intensity, `SplineWarp`/`GridWarp` to fit the surface, keep it deliberately subtle, and relax concatenation/precision discipline when the element will be heavily shrunk/defocused anyway.
10. Animate organic crack-reveal timing with individually hand-drawn, keyframed `RotoPaint` strokes on a flattened UV face (Stroke tab's fade-on/birth-death parameters), drawn slightly wider than the crack and at varied per-stroke speed/direction, rather than a single uniform mask.
11. Exaggerate a "heating up" read by grading the leading edge of an effect brighter than its trailing edge before applying `Glow` — the glow will amplify that asymmetry automatically.
12. Add interactive 2D point-lights, keyframed to move with each spreading effect, masked/textured through a Luma-keyed copy of the plate for realistic highlight catch, `Plus`ed over — cheap substitute for ray-traced bounce lighting Nuke doesn't natively have.
13. Make ambient/secondary elements (smoke, mist) visibly react to nearby light by `Multiply`-ing a glow pass against them, instead of `Plus`-ing a flat, unlit-looking element on top.

### Nodes / Tools / Settings
- **Core Nuke/NukeX:** `TimeOffset`/"TimePin" (custom time-offset gizmo), `Grade`, keying/Luma key, `TimeEcho`, `GodRays`, `Glow` (exponential), `Clamp`, `Expression` (NaN-killer), `STMap`, `Shuffle` (UV/ID-pass extraction), `SplineWarp`, `GridWarp`, `Rotate`/`Transform`, `RotoPaint` (Stroke tab keyframed birth/death for animated reveals), point `Light` (2D-animated, faked bounce lighting), `Multiply`/`Plus` merges chosen deliberately for different interaction semantics
- **Third-party / cross-app:** **Google Tilt Brush** (free VR sculpting app) — specifically its "Tapered Flat" brush, chosen because it auto-normalizes stroke UVs to 0–1 space (other brushes tile across multiple UV tiles); geometry exported as OBJ
- **Author's own stock library (referenced repeatedly):** flow/energy elements, "nebula explosion" mask elements, small/big ember render kits (multi-pass: beauty w/ top-bottom ID split, UV, position, normals), cloth "line" energy elements — all part of the ~200-effect LookDev pack referenced across this whole series
- **Workflow habits called out explicitly:** hidden/named inputs are used sparingly and flagged as bad practice for handing off scripts professionally; heavy comps are broken into off-to-the-side mini-precomps for iteration speed; design is judged against the *final* composited image, not each isolated intermediate step

### Difficulty
Expert — capstone of a 3-part advanced series; assumes everything from Parts 1–2 (SmartVector, KeenTools 3D tracking, UV-space compositing, crack mattes) as a prerequisite and adds VR-authored geometry, multi-element kitbashing judgment, and interaction-design thinking on top.

### Foundry App & Version
Nuke / NukeX for all compositing (majority of this video and the reason it's extracted fully here); Google Tilt Brush (free, cross-platform, not Foundry) only for authoring the flow-path curve geometry. Nuke version not stated on screen; per this skill's version-tracker, a 2022 upload falls in the Nuke 13.1 (Nov 2021) → 13.2 (Apr 2022) window. Uses only the Classic 3D system (geometry import, UVProject) — predates the 14.0-beta USD 3D overhaul; nothing here needs a ray tracer, which the author explicitly notes Nuke still lacks as of this recording.

### Tags
compositing, 3d-system, projection, st-map, gizmo, fx-simulation, rotopaint, grading, expert

---

## Related Tutorials
- [1/3] Nuke Tutorial Series (Practical SFX, Lighting, Script Overview) (`13-nuke-tutorial-series-practical-sfx-lighting-script-overview.md`) and [2/3] Nuke Tutorial Series (CRACKS, Keentools, Smartvectors) (`23-nuke-tutorial-series-cracks-keentools-smartvectors.md`) — direct prequels; this video is the payoff that puts Part 2's tracking/UV-space/crack-matte work to use with the actual energy-effect kitbashing.
- Nuke Compositing an Advanced CG Shockwave | VFX (LookDev) (`nuke-compositing-an-advanced-cg-shockwave-vfx-lookdev.md`) — shares the same author's stock-energy-effects-library kitbashing philosophy (multiple elements re-mapped and combined as masks for each other, not stacked additively) and several of the same Nukepedia gizmos.
- A new way to design VFX | Virtual Reality | Gravity Sketch + Nuke Tutorial (`a-new-way-to-design-vfx-virtual-reality-gravity-sketch-nuke-tutorial.md`) — shares the "author 2D textures in Nuke, hand-sculpt supporting geometry in a VR app, bring it back into Nuke" pipeline shape (there: Gravity Sketch NURBS models; here: Tilt Brush flow-path curves).
