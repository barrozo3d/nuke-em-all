---
title: [1/3] Nuke Tutorial Series (Practical SFX, Lighting, Script Overview)
source: YouTube
url: https://www.youtube.com/watch?v=NHeqhKOLFgU
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke (overview video; live compositing shown but not stepped through node-by-node — that's deferred to Parts 2/3)"
version: "Nuke 13.x (13.1/13.2 — exact 2022 point-release not stated)"
tags: [compositing, roto, rotopaint, grading, fx-simulation, digital-matte-painting, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/13-nuke-tutorial-series-practical-sfx-lighting-script-overview/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# [1/3] Nuke Tutorial Series (Practical SFX, Lighting, Script Overview)

**Source:** [YouTube](https://www.youtube.com/watch?v=NHeqhKOLFgU)
**Author:** Compositing Academy
**Duration:** 29m39s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro And Overview [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to part one of the Nuke tutorial series of how to go about creating this shot,
[0:15] my process of going about it and how you can do it as well.
[0:19] So there's going to be a couple of different things that we cover in this tutorial.
[0:23] It won't just be the Nuke stuff, I'm going to talk about a couple of different topics
[0:26] in this first video.
[0:28] So if I go here, this is what we're going to talk about.
[0:30] So starting with the concept, how we did some of the practical effects.
[0:34] So my wife is a fashion design background and kind of a more traditional art background,
[0:39] so she helped.
[0:40] And this was more of a collaboration definitely on this side in terms of concepting and effects.
[0:45] So definitely credit for that.
[0:47] But so these are some of the things I'm going to cover, practical effects, practical lighting,
[0:51] and then we're going to do a general overview of the script.
[0:53] So this is a pretty big script and there's a lot of techniques used here.
[0:58] So I know that there's a range of viewers watching this, probably some really senior
[1:03] people, probably some beginner people.
[1:05] So keeping that spectrum in mind, I'm still going to talk kind of on an intermediate level
[1:10] in the way I'm explaining things, but I'm not going to explain like really basic sliders
[1:15] and stuff because that's really covered in my basic courses if you guys have seen them.
[1:20] So that's kind of how I explain and go about this video.
[1:24] And yeah, so part two will be different stuff, so more in detail.
[1:29] So this will be more of an overview video, this specific one.
[1:32] And part two will be really going into the specific details of every kind of layer, every
[1:38] technique and really how to build it up.
[1:41] So it won't just be kind of looking through the script and stepping through, but really
[1:44] explaining each process.
[1:46] So part two, the next video will be kind of tracking, keen tools, smart vectors in paint,
[1:52] mixing tracks, 2D, 3D face enhancement, 3D light stabilization integration.
[1:57] Part three of the final video is how we can use elements, creating complex alphas, 3D
[2:03] relighting and making elements interact.
[2:05] So there's quite a lot here and this is really a simplified list.
[2:09] There's probably a lot of little techniques in there that will be covered.
[2:12] So yeah, that's pretty much it.
[2:15] So we'll start with starting with the concept.
[2:17] So this shot, we wanted to do something kind of artistic and fun just to try mixing some
[2:24] practical effects with some of the energy effects that I'll be providing.
[2:28] So that was kind of the goal of this and to have some sort of meaning behind it.
[2:31] So that's kind of the concept of the shot and sort of shedding like the past self and
[2:36] moving towards the ideal.
[2:38] So that's kind of like the philosophical meaning of the shot.
[2:41] Just to show you guys some of the process, the iteration process that goes on.
[2:47] So this is kind of the final comp, but these are some notes I gave myself along the way


### Compositing Iterations [2:49]
**Transcript (timestamped):**
[2:51] and this is just a show and this isn't even the earliest comp.
[2:54] The earliest comp is really basic, but usually final composites take lots of iteration and
[3:01] I've talked about this before if you guys have taken my paid courses.
[3:05] Everything is about iteration.
[3:06] I don't know one single compositor who's really good who just nails everything on version
[3:11] one.
[3:12] It takes multiple layers of iteration, stepping back, looking at it from different angles
[3:16] and trying to perceive what could be done here to improve this image.
[3:21] So these are the kind of stuff that I'm looking at along the way.
[3:24] Maybe it's too noisy in this area.
[3:27] We have the pattern up here, maybe it's a little bit too bright or maybe I'll run some
[3:30] things through the cracks.
[3:32] So when I'm working through this design process and really this is a design process, it's
[3:37] thinking about where, you know, this could be technically correct and could totally work,
[3:43] but compositing is not a purely technical thing.
[3:46] It's really, you have to think about motion, you have to think about light, you have to
[3:51] think about design and composition.
[3:54] So these are the things that not that many people are talking about.
[3:57] So that's why I think this project is pretty fun because we get to really get into those
[4:00] type of things versus just like here's CG integration or here's color matching, stuff
[4:05] like that.
[4:07] So these are all little notes I gave myself along the way, you know, depth of field, it's
[4:11] a little bit too sharp here.
[4:12] If we look at the footage, a little bit too sharp, just some blending notes for myself.
[4:17] Maybe there's some warping going on from our smart factors or tracks.
[4:22] Maybe something looks a little bit too flat.
[4:25] So these are all the level of detail we can really dive into when you're building this
[4:28] image up.
[4:29] So you see here, this is another version, but it's just really too noisy.
[4:33] So if you kind of zoom out, it's almost too much to look at.
[4:36] You have like all these white dots and your eye doesn't really focus on something.
[4:41] So this is something I want to convey in this series as well is like, where's your eye looking?
[4:46] How do you train that eye?
[4:48] What are the details you want to look at?
[4:49] And how do you balance that image?
[4:51] So this is something, as an example, really just, you know, the effect is sort of working
[4:55] here in this picture, but you have like all these white dots and it's hard to focus on
[4:59] one specific thing.
[5:02] Also it's a little bit too saturated, maybe it's a little flat here.
[5:05] The shoulder looks very, very flat.
[5:08] So these are the kind of things that I'm thinking about along the process.
[5:11] So you see from this version to this version, I kind of go here, darken the chin a little
[5:16] bit, maybe brighten up the eyes to sort of bring the focus to the eyes.
[5:21] It's a little bit of an artificial brightening, but it gives it a little bit of a softer look
[5:25] and sort of brings it a little bit less creepy and more kind of a soft, softer look.
[5:31] And then going on to another version here, there's a lot of changes in between, but again,
[5:36] you have the same problem.
[5:38] You have this like really kind of too much little bright highlights appearing in certain
[5:42] areas.
[5:43] And yeah, so these are all the little things I'm thinking about.
[5:46] So if you go from this to the final comp, you can see sort of it's the way I did the
[5:51] effect was kind of keeping the leading edge bright and then it's kind of darkening across
[5:56] time.
[5:57] You still have these nice like rolling highlights underneath the cracks.
[6:01] And that's something I really wanted to focus on with this effect as well was I don't want
[6:06] to just mask a crack and create a glow because that's a really simple effect.
[6:11] And really what I wanted to demonstrate is how we can do a more complex effect if you
[6:16] have some good elements to work with.
[6:19] And so that's kind of the concept and iteration process in a very quick and simplified explanation
[6:25] of it.
[6:27] And yeah, so that is that.
[6:30] So on the next part, which is practical effects.
[6:34] So what is this practically?
[6:37] What is happening here practically?
[6:39] So basically this is sort of a clay.
[6:42] It's a white clay.
[6:43] So you can this is a basically video of it.


### Practical Clay [6:45]
**Transcript (timestamped):**
[6:46] You can like buy this in the store.
[6:50] And yeah, my wife bought this.
[6:51] It's like white clay.
[6:52] And we also use some like it was called clown white paint.
[6:55] You can get it like a Halloween store.
[6:57] It's a little bit different than like an acrylic or something like that.
[7:00] It's more for like Halloween makeup.
[7:02] So it's like this mixed with some of this.
[7:04] And this gives us a nice practical base to start with.
[7:08] So if we compare this to the practical footage, this is actually the practical.
[7:13] So we have a lot to start with here and then we can enhance what's already there.
[7:17] So you can see there's some cracks added.
[7:19] We added some 3D cracks, 2D cracks, and then painted in a bunch of different textures here.
[7:24] So it's a good idea to start with practical effects if you can, especially if you're filming
[7:28] this yourself or doing a project on your own and mixing traditional filmmaking techniques
[7:35] with compositing.
[7:36] So I think especially with YouTube and internet now it's like everything is super about 3D
[7:43] and you're not seeing a lot of practical effects being used.
[7:45] So I wanted to sort of mix that in here and you know, it's some future videos as well.
[7:50] We asked my ideas for that.
[7:52] And that will be kind of fun to talk about along the way.
[7:56] Even though this is a compositing channel, composing is about mixing it with the real.
[7:59] So yeah, that's something that I thought people would find interesting.
[8:04] So talking about this more, one thing with the lighting.


### Lighting [8:06]
**Transcript (timestamped):**
[8:12] So practical lighting, you want to light this in a way, you know, I'm not a portrait photographer.
[8:17] I'm not a studio photographer.
[8:19] But I do understand lighting pretty well.
[8:21] One type of lighting that you can do is called Rembrandt lighting.
[8:25] So basically you can take a it's a it's very cheap way to do lighting cost effective way
[8:33] rather.
[8:34] And you can sort of let me just set this up here.
[8:40] So you can sort of basically the way this is lit is it's just two lights.
[8:45] So you have like a main key light coming from the right.
[8:48] We have another light coming from the left.
[8:51] And we have a bounce card.
[8:54] Just use the white sheet, basically, to sort of fill in this area here.
[8:59] And that gives it so we don't get too much contrast in this area, which gives it a softer,
[9:04] less aggressive look.
[9:06] And that's going to give us this type of this type of lighting that we have here.
[9:10] And this is called Rembrandt lighting.
[9:12] So it's spelt like this.
[9:14] We have R E M Rembrandt Rembrandt lighting.
[9:22] And my roto paint is a little bit laggy here.
[9:25] So you guys can forgive the handwriting Rembrandt lighting.
[9:30] So this is what we're doing here.
[9:32] And one of the key features of this type of portrait lighting is to try to create these
[9:38] inverted triangles on the opposite or the shadow side of the face.
[9:43] So that's kind of what I went for here is we have this lighting lighting up most of
[9:47] the side of this sheet completely in light.
[9:49] And then we have this inverted triangle.
[9:52] And one thing to note when you're doing this type of lighting, if you guys ever film
[9:55] something like this yourself is to try not making this too big.
[9:58] Otherwise, it kind of doesn't give this sort of look.
[10:03] And so we have this soft lighting here.
[10:05] And one thing to look at, if I just pull this open, is if we have this.
[10:12] So this is a different lighting test we did.
[10:15] Obviously, this is not what we wanted.
[10:17] So we didn't want this sort of creepy effect.
[10:19] And you see that by backlighting stuff, we get a totally different looking shot.
[10:24] So, you know, there's no, there's not much bounce light going on.
[10:27] And we have this kind of contrast rim light and a little bit brighter on this side.
[10:32] And so this is why lighting is really important and why I'm talking about it.
[10:36] Because lighting determines the mood of a shot.
[10:39] And if you are compositing something, let's say you're filming it yourself,
[10:44] you're doing your own project, you know, you need to be thinking about what the
[10:48] actual shot looks like.
[10:49] If the shot itself starts out badly, no matter what you do in the composite,
[10:53] you're not going to get a good end result.
[10:56] So that's pretty much it for the kind of practical effects and the practical lighting.
[11:04] So now I'm going to talk about the general overview of this script.
[11:08] So this is a pretty big script.
[11:10] And this is like the project file.
[11:12] Like I said, I'm not going to break down every single technique in this video.
[11:15] That will come in part two.
[11:17] So the project files are now available when this video is posted.
[11:21] And you can go and get those if you want to do this project.
[11:26] What comes with the project file?
[11:27] It comes with footage, 11 CG assets.
[11:32] It can be used for demo reels and also like my paid classes,
[11:36] also offer kind of email support, get stuck on something,
[11:40] as well as one round of written critical feedback.
[11:43] So if you send me your video, I'll send you back, you know, a draw over of some notes
[11:48] or improvements you can make.


### Project Assets [11:50]
**Transcript (timestamped):**
[11:50] But there's only one round of that as, you know, if I get a lot of emails,
[11:53] I can only handle so many as one person.
[11:55] And obviously I have to have a limit there.
[11:59] So these are the things that you'll get.
[12:01] One thing that's not included is the script.
[12:03] So I'm not including the script as because people would be using this for their demo
[12:07] reel, you're kind of expected if you're going to be taking this or downloading
[12:11] this project file to already know a little bit what you're doing.
[12:15] And if you want more like classes on building up to this level,
[12:19] I already have a bunch of classes out that will get you to this level.
[12:23] So I'm not going to give the script because that would kind of devalue
[12:26] the demo reel shot because people would just copy portions and then it's not
[12:30] their work, so that would not be good.
[12:33] So yeah, here's the stuff here.
[12:35] We have a couple effects simulations that you'll get.
[12:38] These are from the Compositing Academy LookDev pack, which we'll be releasing soon.
[12:42] So this is something I've spent many months on.
[12:45] I've been working on in my past time, actively and passively, to create a whole
[12:50] bunch of LookDev effects.
[12:52] It'll be around 200 simulated effects that you guys can actually do look development with.
[12:58] So I'll be talking more about that in some upcoming videos, how we can use
[13:03] these and how this fundamentally changes the approach towards certain shots,
[13:08] which is why I created it.
[13:10] So we have a bunch of different ones here, some liquid kind of stuff, some kind of
[13:16] Nebula kind of Galaxy explosions, some sort of Embery kind of fiery looking stuff.
[13:24] We have like actual embers as well, which you can simulate extra embers if you want.
[13:29] 3D.
[13:30] We have some line effects here, which these are kind of what's being used in the cloth.
[13:36] So probably in the demo video, didn't even notice because it kind of goes by quick.
[13:40] But there are some sort of like effects.
[13:43] If I play this here, there are some sort of effects wrapped on the cloth as well.
[13:48] Some sort of like, I don't know, energy kind of drips that are appearing.
[13:53] And that's coming from that effect that I just showed.
[13:55] And then we have some like ripple fires that I'm using in some of the edges.
[14:00] So you'll see some of that around where the effect is coming off the shoulders and coming
[14:05] off certain areas.
[14:07] So you see like little portions of stuff kind of peeling off at certain points.
[14:12] And so there's a really high level of detail in the shot.
[14:14] You know, if you zoom in, you can see quite a lot of stuff going on.
[14:18] We see bigger embers coming out of the chunks and stuff like that.
[14:23] So we have all those little details that we can add.
[14:26] And by having these simulations, it's really going to be useful.
[14:29] So you can use these for other shots as well.
[14:31] So if you're getting this pack or this shot, you can use these for other projects as well.
[14:38] So you'll get early access to some of the stuff that will be released in the next few weeks.
[14:43] We also have some shot specific effects.
[14:46] So this is a cloth simulation with UV pass that we can wrap some of our other simulations on.
[14:54] So we can take some of these sort of like this effect here that I showed you.
[14:59] Let's see this one.
[15:01] So this is the effect that you can wrap onto the here.
[15:04] And then you can get some sort of embery kind of effects.
[15:07] You can see like here it is like this.
[15:10] And we get something like that.
[15:11] And so we can create bigger embers that have more life to them than simply just tiny little nuke particles or something like that.
[15:18] So this gives us really awesome way to mix in.
[15:23] So you can see just these little kind of glowing pieces or chunks that just give some size variation and a little bit more interest rather than just using, you know, basic embers.
[15:34] We also have some shot specific effects.
[15:37] So some smoke that's being emitted from the geometry of the face and simulated.
[15:43] So I'm really not going to cover super in depth the simulation because I'm using multiple different softwares, multiple different particle systems to create all of these.
[15:51] So I might go into the more of those in the future, but this is really a compositing project.
[15:57] So that is so this is kind of simulating what you would get in production.
[16:01] So you would get all of these things handed to you as a compositor and you would be able to build that shot out.
[16:07] So these are some flow paths generated in tilt brush.
[16:11] I'm going to talk about that in the part two or part three.
[16:15] I think it is more about how these are generated, why I use this method and why it is actually useful.
[16:22] I did get a couple of questions saying, hey, why are you going in VR?
[16:25] Is it actually useful?
[16:27] And it is actually useful not because it's VR, but the way that tilt brush generates this type of geometry and stretches the UV space to zero to one
[16:36] space and you have basically you can just draw these geometries and not have to manually extrude them.
[16:44] So if you're doing lots of things with a lot of curvature, there's no super simple way to bend textures along splines or grid warps in nuke.
[16:53] And so this kind of solves that problem.
[16:55] You can get these geometries and simply export them and use them that way.
[17:00] So you'll get these given for you because I know most people probably don't have an Oculus.
[17:04] But if you do have an Oculus, I will cover a little bit of that and how you can create these in that part three.
[17:11] And then we'll get the 3D geo tracked.
[17:14] So this is from Keen Tools.
[17:16] I'll talk about Keen Tools in the next video and we'll talk about how you can create these geometries.
[17:22] They also have a 14 day trial, I think on their website.
[17:25] So we'll talk a little bit more about that in the next video, how you can use the face builder, the face tracker to get this 3D model,
[17:34] which is really, really going to help the tracking.
[17:36] And I'm going to break that down further.
[17:38] And then we also have a subdivided head, which is the same model just with higher resolution that we can basically create more advanced displacement from.
[17:46] So by adding geometry or resolution, we can add details in a way that is a little bit more realistic than maybe just sticking 2D textures on a geometry.
[18:00] So that's it for the project file.
[18:02] There should be a link in the description for that and that should be available now.
[18:08] So one thing I want to mention before I continue on to do the overview of the script is, yeah, please don't email a bunch of questions and email support if you're working ahead.
[18:18] So I'm releasing the project file now so you can download it and you can work ahead if you want to start to approach it yourself and try to figure it out.
[18:27] But please, for all the questions, wait until part two and three are posted, which I'll be posting one a week.
[18:34] So in the next two weeks, both videos will be out.
[18:37] So it's feel free to work ahead and try to figure it out or just like recreate it.
[18:42] But, you know, hold off on the questions because a lot of stuff will be covered in detail in the next two videos.
[18:51] So if we step through now, we can just take a look at this comp here.
[18:56] So I'm going to break it down.
[18:58] So basically I started with the 2D sort of smart vector on the skin.


### Overview of Script [19:00]
**Transcript (timestamped):**
[19:03] So just enhancing and using some textures and kind of cutting them up and saturating them.
[19:09] I'll talk about some frequency separation.
[19:11] Again, we use some different techniques to match the lighting and we go into a more advanced version of that as well.
[19:18] When we start talking about the 3D head, so we can actually stabilize some of the lighting by using the 3D model.
[19:25] So that will be a pretty cool topic in, I believe, the second video.
[19:31] So stepping through pretty much the same technique.
[19:34] So for the body, the majority of the body is just smart factors.
[19:37] So if you were to cut this into different pieces, the shot, we have sort of a smart factor in the chest, shoulder, hand, a little bit on the cloth.
[19:47] And then we have some problem area, which not a lot of detail to track here.
[19:50] So I'll talk more about how we will combine tracks and use different things to solve sort of these hidden problems that appear.
[19:57] But yeah, that's basically the first half here is mostly smart factors painting in some 2D solutions for the stuff there.
[20:09] And then we're doing some desaturating.
[20:12] And let's just step through.
[20:15] So the effects are merged in.
[20:18] Next, we also have some interactive balance.
[20:22] So we can use some blurs.
[20:23] We can use some darkening before.
[20:25] So one thing with this composite is I didn't want this to look like the whole effect was like plus over.
[20:31] So a lot of the times I was doing like a darkening with the effect prior to adding the effect over with a plus.
[20:38] So that just gives the effects like this dark sort of spreading effect as the cracks kind of move forward.
[20:45] And you'll see if you just plus it over, it doesn't look if I were to take this off.
[20:50] You see, it feels really like just additive.
[20:52] So I really wanted to add darkness as it's kind of spreading.
[20:57] So pretty much all the effects are doing that.
[21:00] So you can see here, we're getting darker pieces as the effects spreads.
[21:03] And we can use some time offsets and a couple of different variations of techniques to get that darkness to spread faster so that the light effects will be easier to see and they'll flow over it.
[21:14] So again, that's more about balance and more of a creative decision rather than purely technical.
[21:22] And also when I talk about the effects, a little bit more in detail, I'll show you guys how to combine these in different ways.
[21:29] How I warped some of the perspectives to sort of match the body a little bit closer rather than just we don't want to just stick a 2D video on this picture.
[21:40] What we want to do is kind of use, I use some eye transforms and rotations to sort of bend certain pieces so that the flow of the effects will actually go in different directions.
[21:51] And yeah, I'll talk about that again more in detail as we get to the effects.
[21:58] And then we do some heat distortion.
[22:01] I'm going to go over some more advanced heat distortion.
[22:04] So we'll go over this, this portion here, which is creating sort of a normals map type of thing and sort of using some God rays and some Luma keys to kind of generate a more advanced heat distortion as it's coming out of the cracks.
[22:25] And yeah, so that's kind of how that's that's created there.
[22:27] So we create more advanced heat distortion, which gives us this nice ripple effect as the heat is coming up.
[22:33] And if you're watching the clip and you zoom in on it, you'll see you'll actually see that level of detail does does help a lot.
[22:44] The shoulder, same same idea, same type of thing here.
[22:46] And then we have the embers.
[22:48] So a lot of the embers is a lot of retime, retime effects.
[22:52] So either I retime them or I time offset them to basically we have like small embers coming off and then we have like big chunks.
[23:00] So it's really just using that same that same element that I'm giving you guys over and over.
[23:04] But I'll just kind of like mask a different portion.
[23:07] And if I just gain up here, yeah, we'll just you could just cut a piece from here and use it in one area or cut a piece from the middle.
[23:14] Use it in different area.
[23:15] And it will give you the look that there's a bunch of different ones.
[23:17] But actually, we're just using the same one over and over with offset.
[23:22] And you'll see here, by the way, I'm using Daisy chains in my comp.
[23:26] I haven't made a video about this yet.
[23:27] But I was thinking about it because this is something I kind of do is I'll merge each element over the background one at a time just to see how it looks.
[23:35] And then if they kind of go together, for example, these are all embers, I'll kind of just, you know, put all these on one layer and then merge it over as one.
[23:44] And why this is useful is because we could precomp this out as a layer.
[23:48] It's just a nice way to organize your script by doing that.
[23:52] And yeah, so other stuff here, different, we'll use some God raise, we use some different things to sort of.
[23:59] We don't want to completely flat edges.
[24:02] So I wanted to sort of break up the edge, especially since we're against black here to, you know, not make it feel 2D completely.
[24:09] So we want to have some of these little effects kind of flickering off.
[24:13] So I'll talk about some different stuff with that.
[24:15] And then there's just a bunch more ember stuff here.
[24:18] We have some burning edges effects as well for the skin so we can get some different type of rolling effects there.
[24:27] And this is the cloth thing.
[24:29] So again, we use some of those elements to wrap it onto the cloth.
[24:34] And we can use that on both sides of the cloth.
[24:37] This is the more complex part of the script.
[24:40] So the center area, we start to go into some of the 3D.
[24:44] Cracks and 3D displacement so we can take this face and displace in different ways to create more 3D looking stuff and also add ambient inclusion and details like that.
[24:55] So we have these chunks that we're adding on all over.
[24:59] And you see I use 3D more, more on the face and 2D more down here.
[25:03] And that's really because of the facing angle.
[25:05] So like this has more rotation.
[25:06] So because of that, we're going to add some more of the 3D.
[25:09] Rather than opting for 2D just sticking a texture on here.
[25:13] And I didn't use a lot of, I didn't really use 3D cracks down here because there's not much parallax.
[25:17] So you're not going to, it's kind of a waste of time if there's no parallax to feel that something is actually truly 3D.
[25:25] So yeah, we'll talk about all of that.
[25:29] So we're going to go ahead and do some more of the 3D.
[25:31] So we're going to go ahead and add some more of the 3D.
[25:33] And then we're going to add some more of the 3D.
[25:35] So yeah, we'll talk about all of that.
[25:39] And yeah, and I'll also talk about that effect here.
[25:42] So again, working in UV space, this is why I want to make that prior video.
[25:47] Because we do this a lot in this particular project.
[25:50] We're going to flatten this face.
[25:52] And this is really one of the awesome benefits of having Keen Tools and Face Tracker.
[25:57] Because we can work in UV space, we can stabilize the lighting.
[26:01] So one of the effects we'll talk about is how we can stabilize the lighting and use that to basically integrate textures into the picture by using the lighting that exists.
[26:14] Rather than just kind of sticking something on and manually doing color corrections.
[26:23] And yeah, and I'll also talk about how to generate these crack mats.
[26:27] So this is how we're running the effects through.
[26:29] So we're going to use this to mask some of those UV paths that I showed you.
[26:34] And yeah, we use some frequency separation here, Luma Keys, some manual roto paints and working in UV space again.
[26:42] So that's why that UV space is really, really helpful for creating that.
[26:48] You know, if you're working with just purely smart vectors, we could do some stuff here.
[26:53] But where you're going to have problems is where these things overlap.
[26:56] So I'll talk more about that in the next video.
[27:02] And then yeah, basically just the same concept going all the way down.
[27:06] So you can see like if we just look at this layer, what that layer looks like.
[27:11] So we can see that, you know, that those textures are really running through.
[27:15] And that gives us a pretty cool starting point.
[27:21] So let me just keep stepping down and also the face smoke.
[27:26] So this is we can use some of the preexisting stuff here to actually light up some of the effects that we have.
[27:34] So again, I'll talk about that.
[27:36] But we get this really nice look of like kind of sparkling subtle effect.
[27:42] And we don't want to play it up too much.
[27:43] Otherwise you get a little bit too noisy like I was showing you with some of the earlier iterations.
[27:48] But it is really nice to have that subtle detail and movement just to bring that to life.
[27:56] And then there's like a really tiny piece of detail where I kind of took like one of the embers and reflected it in the eye just to get like, you know, a tiny bit of movement into the eyes as well.
[28:06] But we also have some of the some of the effects running through the eyes as well.
[28:10] So we do some polar coordinate or polar distort to sort of warp these into spheres.
[28:16] And we can sort of get this effect to run through the eyes as well.
[28:20] And yeah, that's pretty much how that's being done.
[28:27] And more embers.
[28:29] And then yeah, so some color corrections and grain and stuff like that.
[28:34] So there's a lot of things going on there, but really how you combine all of them is really the key.
[28:41] And how do you manage a script like that? How do you organize it?
[28:46] Yeah, so that's that's why these shots start to get a little bit more complicated.
[28:51] No specific technique is overly complicated.
[28:55] It's really just how do you take all this bag of tools that you have and manage it and combine it and use problem solving to know what tool to use and where to use it.
[29:07] And that's really one of the core concepts of being a good compositor is knowing all of that.
[29:13] So I think that's pretty much covered it for the first video.
[29:16] Yeah, that's pretty much covered for the first video.
[29:19] And if you like the video hit like it really really helps the algorithm.
[29:22] So make sure to do that. Subscribe if you're not already.
[29:25] Project files are in the description below and you guys can work ahead if you want or wait a week and the first detailed video will be out.
[29:37] Thank you.



---

## Captured Frames

- [2:51] tutorials/frames/13-nuke-tutorial-series-practical-sfx-lighting-script-overview/frame_000.jpg
- [6:46] tutorials/frames/13-nuke-tutorial-series-practical-sfx-lighting-script-overview/frame_001.jpg
- [8:40] tutorials/frames/13-nuke-tutorial-series-practical-sfx-lighting-script-overview/frame_002.jpg
- [10:12] tutorials/frames/13-nuke-tutorial-series-practical-sfx-lighting-script-overview/frame_003.jpg
- [12:38] tutorials/frames/13-nuke-tutorial-series-practical-sfx-lighting-script-overview/frame_004.jpg
- [15:01] tutorials/frames/13-nuke-tutorial-series-practical-sfx-lighting-script-overview/frame_005.jpg
- [19:03] tutorials/frames/13-nuke-tutorial-series-practical-sfx-lighting-script-overview/frame_006.jpg
- [25:52] tutorials/frames/13-nuke-tutorial-series-practical-sfx-lighting-script-overview/frame_007.jpg

---

## Structured Notes

### Core Technique
Part 1 of a 3-part flagship demo-reel-shot series: an overview (not a node walkthrough) of the concept/iteration process, the practical (real-world) effects and lighting used to shoot the base plate, and a guided tour of the finished Nuke script's structure — establishing the shot and vocabulary that Parts 2 and 3 will break down node-by-node.

### Summary
The shot: a clay/plaster bust of a person "cracking" apart with glowing energy effects emerging from the cracks, conceived as a "shedding the past self" concept (co-designed with the author's wife, who has a fashion/traditional-art background). The video opens with a **compositing-iteration** case study (frame_000/002/003) — showing several intermediate versions side by side and narrating the actual notes-to-self along the way ("too noisy," "too saturated," "shoulder looks flat," "brighten the eyes to soften it") to make the point that even senior compositors iterate heavily and that judging an image is about motion/light/design/composition, not just technical correctness; a specific recurring fix was reducing "too many competing bright highlights" so the eye has one clear focal point, and shaping each crack-glow effect so it's bright at the leading edge and darkens as it spreads (rather than a flat uniform glow) for a more physically believable "spreading" read. **Practical effects:** the base bust was sculpted from real white modeling clay plus "clown white" Halloween face paint (frame_001, a real behind-the-scenes clip of the material), then enhanced digitally with added 2D/3D cracks and painted-in texture detail — the video argues combining practical/traditional filmmaking with CG compositing is underused given how "everything is 3D now." **Practical lighting:** the bust was lit with classic two-light **Rembrandt lighting** (key light from one side, a second light from the opposite side, plus a white-sheet bounce card to fill shadow contrast) — frame_004 shows a literal hand-drawn diagram over the reference photo explaining the technique, including its signature "inverted triangle" of light on the shadow side of the face, and a warning not to let that triangle get too large or the look breaks. A rejected lighting test using only backlighting (frame not separately captured) is shown as a "too creepy, no bounce fill" counterexample — reinforcing that a badly-lit plate can't be rescued in comp. The remainder of the video is a **project-asset/script tour**, not a tutorial: the accompanying paid project file includes 11 CG assets pulled from the author's then-unreleased "~200 simulated effects" LookDev library (liquid, nebula/galaxy, ember/fire elements — frame_005/006 show raw grayscale versions of these simulation elements), shot-specific simulations (a cloth sim with its own UV pass for wrapping ember effects onto both sides of the fabric), Tilt-Brush-generated "flow path" geometry (VR sculpting chosen specifically because Tilt Brush auto-stretches UVs to 0–1 space, sidestepping Nuke's lack of an easy way to bend textures along splines/curves), and a KeenTools-tracked 3D geo of the subject's face plus a subdivided higher-res version for displacement detail (frame_007, the 3D head geometry in Nuke's viewer). The final segment is a guided click-through of the actual (very large) finished script, narrating its overall structure at a conceptual level: 2D SmartVector-based skin enhancement with frequency separation, body tracking mostly via SmartVectors (with named "problem areas" lacking trackable detail, to be solved in Part 2), a **"darken-before-plus"** compositing habit applied to nearly every crack-glow effect (grading the background darker under an effect before merging it in with Plus, rather than a flat additive Plus alone, so the effect reads as truly emitting/spreading light rather than looking pasted-on), IDistort/rotation warps to bend 2D energy-effect footage so its flow direction follows the body's actual form instead of reading as a flat video pasted on, a from-scratch "advanced heat distortion" built from a normals-map-like pass plus GodRays and Luma keys, heavy reuse of a small number of stock ember elements via retiming/time-offset/masking different sub-regions of the same clip to fake variety ("Daisy chains" — merging same-type elements together into one precomp layer one at a time before merging that whole precomp onto the main image, for script organization), 3D displacement/cracks concentrated on the more rotated, higher-parallax face area vs. 2D-only treatment on flatter, lower-parallax areas (a deliberate cost/benefit call, not an oversight), UV-space work (flattening the face via the KeenTools track) for both crack-matte generation and **lighting-stabilized texture integration** (matching a texture into the existing lighting of the plate rather than manually color-correcting it in), and a couple of small "life" details — reflecting an ember highlight into the eye, and running one energy effect through `PolarDistort` to wrap it convincingly onto the spherical eyeball.

### Key Steps
This is an overview/context video, not a followable technique recipe — the below is the roadmap it lays out for the two follow-up videos, not steps to execute here:
1. Concept and iterate visually before committing — review multiple comp versions, name specific problems in each (competing highlights, flat-looking areas, over-saturation) and fix them one at a time.
2. Shape any "energy" or crack-glow effect with a bright leading edge that darkens as it spreads (not a flat glow) for a more physically convincing "spreading" read.
3. Where possible, shoot practical/real reference material (clay/paint sculpt, real Rembrandt-lit photography) as the base, then enhance digitally — rather than building everything from scratch in CG.
4. Light practical reference with intentional technique (two-light Rembrandt setup + bounce fill) — a badly-lit source plate can't be fixed in comp.
5. (Roadmap for Part 2) Tracking with KeenTools face tracker/builder, SmartVectors, RotoPaint, mixing multiple track types, 2D/3D face enhancement, 3D-light stabilization for texture integration.
6. (Roadmap for Part 3) Using stock elements to create complex alpha mattes, 3D relighting, making elements interact with the surface they're on, and more detail on the Tilt Brush VR flow-path workflow.
7. Organize a large script with "Daisy chains" — group same-type elements (e.g. all embers) into one precomp layer merged incrementally, then merge that whole precomp onto the main chain as a single step, instead of a flat pile of individual merges.
8. Reuse a small number of stock simulation elements broadly by retiming/time-offsetting and masking different regions of the same clip, rather than sourcing many separate elements.

### Nodes / Tools / Settings
- **Core Nuke concepts named (not demonstrated step-by-step in this video):** SmartVector tracking, frequency separation, RotoPaint, IDistort/Transform-based perspective warps, GodRays + Luma keys for heat-distortion, `PolarDistort` (wrapping an effect onto the spherical eye — same gizmo used in several other tutorials in this KB), UV-space work via a KeenTools face track, Grade/darken-then-Plus compositing pattern, precomp "Daisy chain" script organization
- **Cross-app / non-Nuke tools referenced:** KeenTools (Face Builder/Face Tracker plugin, 14-day trial available) for 3D face geo tracking; Tilt Brush (VR) for flow-path geometry with pre-stretched 0–1 UV space; the author's own ~200-effect LookDev/Energy-FX simulation library (liquid, nebula/galaxy, ember/fire elements) built across "multiple different softwares, multiple different particle systems," not detailed further since this is a compositing-focused project
- **Practical/physical materials:** white modeling clay + "clown white" Halloween face paint for the sculpted bust; two-light Rembrandt setup + white-sheet bounce card for practical lighting

### Difficulty
Intermediate (as context/roadmap) — no specific node technique is taught step-by-step here; the actual difficulty lives in Parts 2 and 3, which this video explicitly defers to.

### Foundry App & Version
Nuke (script shown/narrated, not built live). Version not stated on screen; per this skill's version-tracker, a 2022 upload falls in the Nuke 13.1 (Nov 2021) → 13.2 (Apr 2022) window.

### Tags
compositing, roto, rotopaint, grading, fx-simulation, digital-matte-painting, intermediate

---

## Related Tutorials
- [2/3] Nuke Tutorial Series (CRACKS, Keentools, Smartvectors) and [3/3] Nuke Tutorial Series (Flow Paths, FX Integration, Design) — direct continuations of this same shot/project; Part 2 covers the tracking/SmartVector/KeenTools techniques this video only names, Part 3 covers the element-interaction/relighting/Tilt-Brush-flow-path techniques this video only previews.
- 360 Spherical LatLong Textures | Nuke Tutorial (`360-spherical-latlong-textures-nuke-tutorial.md`), Mixed Medium VFX P1 (`mixed-medium-vfx-p1-blender-nuke-ai-embergen-vr-tutorial.md`), Nuke Compositing an Advanced CG Shockwave (`nuke-compositing-an-advanced-cg-shockwave-vfx-lookdev.md`) — all reference or use `PolarDistort` for spherical/radial wrapping, as this video does for the eye effect.
