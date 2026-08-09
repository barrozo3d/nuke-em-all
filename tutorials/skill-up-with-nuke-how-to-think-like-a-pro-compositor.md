---
title: Skill Up with Nuke | How To Think Like A Pro Compositor
source: YouTube
url: https://www.youtube.com/watch?v=tLQfGjHpsd8
author: Foundry
ingested: 2026-08-09
app: "Nuke + Nuke Studio"
version: "not specified on screen (ACES 1.1 OCIO config consistent with recent Nuke 15.x-17.x)"
tags: [compositing, nuke-studio, color-management, ocio, tracking, keying, roto, grading, defocus, edge-extend, chromatic-aberration, editorial, conform, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/skill-up-with-nuke-how-to-think-like-a-pro-compositor/
frame_count: 13
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Skill Up with Nuke | How To Think Like A Pro Compositor

**Source:** [YouTube](https://www.youtube.com/watch?v=tLQfGjHpsd8)
**Author:** Foundry
**Duration:** 34m57s | 19 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey, this is Peter Timberlake, I'm a compositor and director working out of Southern California.
[0:11] So I've recently put online a bunch of practice material that compositors can download and
[0:15] get started with, and these are intended for compositors who want to improve their reel
[0:20] using kind of high quality practice material, or people who are just wanting to do tutorials
[0:24] online and have something to do the tutorials with.
[0:27] And you can access these by going to petertimberlake.com.
[0:31] Within each of these shots will be all of the plates required to do this shot.
[0:36] We'll see up here on the top, there's a video of this kid running by, this lady really
[0:40] fast, so the boy goes in fast motion, and then everything behind him, the lady, the
[0:45] flags, the tablecloth, etc, blows in slow motion.
[0:48] To achieve that, you're going to need a handful of plates, including the boy, the lady, the
[0:52] tablecloth, and then some auxiliary things such as map painting elements, CG flags, and
[0:58] then the roto for the boy.
[0:59] And this is all contained and downloadable here, you just click download here, and it's
[1:02] designed so that you can just simply download it and then chuck it into Nuke and get started.
[1:08] If that's what you do want to do, make sure to convert your project color space from Nuke
[1:11] default to ACEs 1.1, we'll go over that in just a second.
[1:14] So the reason I've done this is just because it's really hard to find accessible, good
[1:18] quality practice material that's not prohibited by either the movie studios or agencies or
[1:24] brands or what have you.
[1:26] So these are completely free to use, no license, use them abuse them, do whatever you want
[1:30] with them.
[1:31] So the founder have asked me to kind of put together a demo video on how to get started
[1:34] with these practice plates.
[1:36] So we're not going to actually go over all of the individual techniques needed to complete
[1:40] these shots, we will be going over kind of the problem solving that you're going to need
[1:44] to use over and over throughout your career.
[1:46] And that can enable you to solve problems not only on these shots, but on every shot
[1:50] you ever do in your whole composing career.
[1:53] If you are curious about where to find the more technical specific knowledge, you can
[1:57] do that just on either foundry's YouTube page, so foundry nuke, and you can find the foundries
[2:03] page here, or you could just search a particular technique that you might be interested in
[2:07] learning such as say about a grade node, you can just say grade node nuke.
[2:12] There's going to be a lot of people very eager to share what they know.
[2:15] Anytime you encounter a problem, go to Google first.
[2:17] Without further ado, here's the skills that we're going to be going over in this video
[2:21] as we kind of build this shot.


### Survival Skill 1 - Use What You Know to Solve Problems [2:23]
**Transcript (timestamped):**
[2:23] One, use what you have in your brain to solve problems.
[2:26] I mean what that means is you already know all kinds of stuff, and you probably even
[2:29] know a lot of stuff about graphics and compositing.
[2:32] So our goal is going to be to use the things that we already know to kind of triangulate
[2:36] the things that we don't know and ask the questions that we need to be asking.


### Survival Skill 1B - Google Relentlessly [2:40]
**Transcript (timestamped):**
[2:40] One, be Google stuff relentlessly.
[2:43] Once you kind of figure out the problem that you're trying to solve, just Google it exhaustively
[2:46] and read as much as you can.
[2:48] Probably a lot of the answers you're going to be getting are from people who are experienced
[2:51] in the compositing world who are eager to share their knowledge with you.


### Survival Skill 1C - Reach Out to People in Forums and Discord [2:54]
**Transcript (timestamped):**
[2:54] And one, see when Google fails, ask people on forums and Discord.
[2:58] If you've spent a lot of time Googling your problem, you can't figure out the answer.
[3:01] Just ask people on the foundry forums, forums, nuke users, or ask on Discord.
[3:06] And there's a handful of Discord servers.
[3:08] One of them I created and run, it's called Nuke Coven here.
[3:11] And as you can see, there's people asking questions about various things here.


### Survival Skill 2 - Use Reference Material [3:15]
**Transcript (timestamped):**
[3:15] Skill set number two, use references as often as possible.
[3:18] In every comp, we're going for a ground truth perfect comp.
[3:21] In order to get there, we're going to need to use real world references.
[3:25] Say for example, we want to replace the sky and our sky is not looking perfect.
[3:28] We're going to go online and look at some images and videos of the thing that we're
[3:31] trying to create.
[3:32] And then we're going to use the information that we learn from that reference video to
[3:36] solve problems within our comp.


### Survival Skill 3 - Observe Information Within the Plate [3:38]
**Transcript (timestamped):**
[3:38] Number three, there's tons of information in the plate.
[3:40] Use it when we composite an element into a plate.
[3:43] All of the information that we need to know about how that element should look is contained
[3:48] within the original footage itself.
[3:49] Say for example, we want to match the color of something white in our CG element to something
[3:55] white in the comp.
[3:56] We need to be able to access that information in the plate itself, the footage that we shot
[4:00] and then apply that to our new composited element.
[4:03] And we'll go over that more in a second.


### Survival Skill 4 - Critique Your Work Relentlessly [4:04]
**Transcript (timestamped):**
[4:05] Number four, always assume there's a way to improve your comp until time runs out.
[4:09] In other words, we need to learn how to critique our own work and be really relentless against
[4:12] our comps while always being confident in our ability to improve that comp and also improve
[4:18] our own work.
[4:19] And that skill is at the core of compositing and it's going to be the process by which you
[4:23] improve your eye and improve yourself as a compositor.


### Survival Skill 5 - Seek Out Mentors [4:25]
**Transcript (timestamped):**
[4:26] And number five, find mentorship where you can, even if it's not called formally a mentor-mentee
[4:31] relationship.
[4:32] There are folks that can provide wisdom to you and then just try and absorb as much as
[4:35] you can from them.
[4:36] Okay.
[4:37] And the last thing we do before getting into these comps is let's please download the Tony
[4:42] Lyons survival toolkit.
[4:43] And you can find this on GitHub under creative Lyons, Nuke survival toolkit.
[4:47] And this is going to contain a lot of tools that aren't installed with Nuke, but that have
[4:51] been developed by Nuke users over the last 10 to 20 years and they're used in studios
[4:56] all around the world.
[4:57] In order to install this, please just watch this demo video or the instruction manual here
[5:02] and we'll be using these throughout this demo video.
[5:04] Okay.
[5:04] If all you'd like to do is just throw these into Nuke and start compositing, all you'll
[5:08] have to do is just download these, check them in like so, and then change your color space
[5:12] settings and then get started.
[5:13] Change your color space settings here by going color management, OCIO, OCIO config,
[5:19] ACEs 1.1.
[5:20] And that will give you the correct color space for your read node, which is ACEs CG.
[5:24] I've seen linear and ACEs CG are the same color space while in the ACEs OCIO config.
[5:31] And this will be everything you need to get started.


### Preparing the Sequence, Folder Structure and Export Settings in Nuke Studio [5:33]
**Transcript (timestamped):**
[5:33] Okay.
[5:33] So Foundry have also asked me to put together a quick demo on Nuke Studio and how you can
[5:37] use Nuke Studio to manage your entire project.
[5:41] So the last thing you'd want to do, if you're working on a personal project or a client
[5:44] project is complete your edit and premiere, then export plates out of premiere and then
[5:49] kind of just hope that everything goes right.
[5:51] And I've seen a lot of studios do this and it always ends up in a lot of heartbreak and
[5:56] a lot of stress for everyone involved and a lot of late nights.
[5:59] To solve this problem.
[6:00] Foundry have created Nuke Studio, which is kind of the starting place and ending place
[6:05] for every VFX project.
[6:07] So the way that we would start this process, we would export an XML from our editorial
[6:11] software like Premiere or Resolve or Avid or whatever and import it into Nuke.
[6:16] And what we would get is something that looks like this, a timeline.
[6:19] And this timeline is composed of firstly all of our plates that compose this edit in a
[6:23] timeline and then also all of the ingredients needed to put together these composites.
[6:28] After a shot like this where our boy is running across the frame in fast motion and everything
[6:32] in the background is going in slow motion, we're going to need a handful of plates.
[6:36] We're going to need the boy running obviously in fast motion.
[6:38] We're going to need some slow motion tablecloth here and slow motion a lady's hair getting
[6:43] blown up like so.
[6:45] And so our goal for this is going to be to create a project folder structure that our
[6:49] compositors in our case probably ourselves can work within and export within in a really
[6:54] organized way so that everything is being named correctly and everything is being put
[6:58] in the correct folders so that we can then later take all of this stuff back up in Nuke
[7:02] Studio with just the single push of a button.
[7:04] So in order to achieve that goal, we're going to need to name stuff in a specific way.
[7:08] We will just go through our project and name things sequentially SC10, 20, 30, 40 and make
[7:14] sure that our tracks are named in a meaningful way.
[7:17] In our case BGO1, BGO2, BGO3, which is short for background 1, 2, and 3 and then make sure
[7:23] that all of our vertical ingredients here, our elements are named the same way.
[7:28] We can do that naming pretty easily by just sequentially naming everything.
[7:32] We're going to editorial, rename shots, sequential rename, start at shot 10 and then here's our
[7:36] pattern and we can increment by 10.
[7:38] So our first shot will be called SH0010.
[7:42] The following shot will be incremented by 10 meaning SH0020 and so on.
[7:48] So what that will create is shot SH0010 all the way to SH0530 for 53 total shots.
[7:56] Imagine that we have named everything correctly.
[7:57] We've named our sequence correctly, SCQ010.
[8:00] I would recommend something kind of short so that your file paths aren't too long and
[8:03] then we'll hit export.
[8:04] Okay, and then what we'll see is as an export structure here, this is one that I've created.
[8:08] Foundry have also preloaded Nuke Studio with some other export templates that you can use.
[8:13] But at the end of the day, you'll probably want to change this file structure that works
[8:16] for you.
[8:17] So this is going to export a handful of things.
[8:20] Firstly it will export your plates as EXRs, which is a key that you're working on EXRs
[8:24] and not an MOV you're in before.
[8:26] And I will name these files according to the tokens that you've provided Nuke Studio.
[8:31] Firstly we will get a bunch of folders here.
[8:34] You can create as many in closing folders as you wish.
[8:36] And then we'll have this bracket here, which will denote a sequence.
[8:41] So instead of writing sequence within our file path, you'll see that in our example
[8:45] preview here.
[8:46] So if we don't get the word sequence, we get the phrase Seq 010, which is our sequence
[8:50] name here.
[8:51] Basically Nuke Studio is replacing this sequence token with whatever our sequence is named.
[8:56] Next is our shot.
[8:57] Our shot is named SH0070.
[9:00] So we'll see here SH0070.
[9:01] Our track, BG01.
[9:03] Our version is pulling from right here, 0001.
[9:06] And our extension, which is the file type.
[9:08] So when we look at what EXR sequence Nuke Studio is going to be writing, we can see our sample
[9:12] path here.
[9:13] And then we have all of our settings here.
[9:14] One of the other things Nuke Studio is going to be creating is a Nuke project file, which
[9:19] contains your read node.
[9:21] The read node is going to look something like this, where it's pulling directly from the
[9:24] file path from Nuke Studio, this read node.
[9:27] And a write node, which has a pre-filled write path within whatever folder structure you
[9:32] like.
[9:33] Nuke Studio will also be looking to repopulate the edit with completed VFX work from that
[9:37] write path.
[9:38] So according to these tokens, here is where our Nuke project file is going to be created.
[9:43] And then finally, you will denote the output path of your write node within Nuke, according
[9:49] to this Nuke write node output structure.
[9:52] All this means is when you do create that Nuke file, the write node that is created within
[9:56] that Nuke script will be auto populated to write to this path.
[10:01] And in turn, when our VFX work is completed, Nuke Studio will be looking for that write
[10:05] path to repopulate its edit with completed VFX work.
[10:09] Okay, so let's hit export here.
[10:11] And after that export completes, what we'll see is 53 discrete shot folders here for our
[10:16] 53 shots, as well as all of the requisite plates for those shots that we selected during our
[10:22] export.
[10:23] So for a shot like this, shot 70, we'll see BG01, BG02, BG03, which correlate to BG01,
[10:29] BG02, BG03.
[10:31] So now that we've exported our plates and had our Nuke scripts pre-generated, let's
[10:35] get started with compositing.
[10:37] So in the case of someone who is just downloading stuff off my website, you can just check these


### Starting the Comp [10:38]
**Transcript (timestamped):**
[10:41] into Nuke and pretty much get started.
[10:44] Likely when you first pull in plates, this is how our comp is going to look.
[10:47] Not great.
[10:48] The colors look a little bit flat and a little bit greenish.
[10:50] And that's just because Nuke is interpreting these in the incorrect color space.
[10:53] And in order to fix that, we'll just hit ask on your keyboard, go to project settings.
[10:57] We'll ensure color management is set to OCIO and OCIO config is set to ACES 1.1.
[11:03] And that will ensure that our read nodes are automatically set to ACES CG.
[11:07] ACES CG and scene linear in the ACES OCIO config are the same.
[11:12] So we can switch between scene linear and ACES CG and we'll see that they look the same.
[11:16] That will put us in a good place to start our compositing work.
[11:19] Okay, so I just opened shot 60 here.
[11:22] We'll be working with both shot 60 and 70, but we'll start with shot 60.
[11:26] We'll see that we want to composite both this running boy here and this lady airing out the
[11:31] laundry here.
[11:32] What we'll notice first is that the shot is not stable.
[11:34] It's not on a tripod.
[11:35] And not only that, but the motion isn't the same for each shot.
[11:38] If we were just to do kind of a cheap over here, we would notice that the backgrounds
[11:42] are moving a ton against each other.
[11:44] Okay, so let's use our first concept of compositing.


### Applying Survival Skill 1 [11:45]
**Transcript (timestamped):**
[11:47] We'll use what's in our head to solve problems.
[11:50] So we know that if something is moving and it has a different motion than the element
[11:55] that we're compositing on top of, we're going to get a lot of swimming where one of the
[11:59] elements is swimming against the other element.
[12:01] So let's kind of use what's in our brain and diagnose.
[12:04] So what if we stabilized each of the plates before doing our compositing work?
[12:10] That way we would have one plate that's stable, another plate that's stable, and then we could
[12:13] just smack them on top of each other.
[12:15] We have kind of problem solved using our own brain, but what if we don't know how to stabilize
[12:20] an image?
[12:21] Well, we'll use our second concept, 1b Google stuff, and we will say how to stabilize in


### Applying Survival Skill 1B [12:23]
**Transcript (timestamped):**
[12:28] Nuke.
[12:29] What we'll see is a bunch of different walkthroughs on how to stabilize.
[12:32] I'll give you a shortcut right now.
[12:34] We could just use a simple tracking node, Tracker.
[12:36] We could create a bunch of tracking points using Ctrl Alt Click, something like this
[12:42] general plane, highlight them all, and track.
[12:48] Grab all of these, just indicating to Nuke that we want to use the transform, motion
[12:52] in X and Y, and the rotation information that's rotating like so, and we will stabilize
[12:58] it.
[12:59] We'll notice that it's kind of working, but we still have a lot of swimming over here
[13:02] in the extremities right here, and up here on the left, right here, we're getting a lot
[13:06] of swimming.
[13:07] Say we've Googled a lot of solutions to this problem, and we haven't been able to find
[13:12] anything.
[13:13] One of the next steps we can take is strategy 1c, when Google fails, ask people on the forums


### Applying Survival Skill 1C [13:15]
**Transcript (timestamped):**
[13:18] and Discord.
[13:19] We could go to the Foundry forums here, Nuke users, or we could go to the Discord here.
[13:25] This Discord is a Discord that I created and is run by some really cool people, and people
[13:30] are very charitable with their information, with their time here.
[13:33] If we're a new user, we can use this new user's thread, and we can just ask our question.
[13:37] We'll probably want to include a screenshot of our problem, and maybe even a video of
[13:41] what's not working, and maybe explain things that we've tried, and ask for some potential
[13:44] solutions to our problem.


### Prepping the Shot Elements That Need Fixing [13:45]
**Transcript (timestamped):**
[13:46] Okay, so let's leave this shot behind now, and move on to a new shot.
[13:49] This is going to be shot 70.
[13:51] So when getting started with this, the first step we'll probably take is we'll take a look
[13:55] at all of our elements, we'll play them through, just to kind of see what's going on with them,
[13:58] and then we'll build a list in our mind of how these elements need to be built up from
[14:03] back to front.
[14:04] So one kind of best practice is to build your comp from the furthest element back, and then
[14:08] build it sequentially of each element in space forward.
[14:11] If we take a look at all of our elements here, we will conclude that probably the furthest
[14:15] back in every single comp we ever do in our whole life will be the sky.
[14:19] So sometimes what I'll do when starting a comp is I will just create an empty reformat
[14:24] node at the correct format that we're compositing within, and that will just set us on the right
[14:28] path moving forward, create an empty reformat node, set it to the same format as our plate,
[14:33] and then we'll get going.
[14:34] So our furthest element back here is the sky.
[14:36] Let's just merge that over our empty reformat, and here's what we'll get.
[14:40] So this doesn't really look super usable.
[14:42] So we'll just position this something like that, just as a starting place before we merge
[14:46] our other elements over.
[14:48] And then as you can see our bounding box here is really large, and this just means that
[14:52] we're only seeing this in our viewport, but Nuke is actually calculating all of this data
[14:57] here, meaning it's calculating four times more data than what we actually need it to
[15:01] be calculating.
[15:02] So let's just crop that here, and that will ensure that Nuke only calculates what's in
[15:06] the viewport.
[15:07] Okay, our next furthest element back would be this drone plate, but for now let's just
[15:12] skip that one and go straight to our next furthest in space and just for time.
[15:16] Okay, so we have first our boy.
[15:18] That's not further back than the lady, is it?
[15:21] And then we have this tablecloth here, which is going in front of the lady's knee.
[15:25] So we will conclude that our next furthest back element would be the lady getting her
[15:29] hair blown like so.
[15:31] One thing I'll actually do before compositing this over is I want to white balance this
[15:36] plate.
[15:37] And that's just because this doesn't look super white balanced to me.
[15:39] It looks very orange.
[15:40] And this is something that we probably wouldn't do at a studio, but in this case we can.
[15:44] And we'll just treat this white balance as a so-called neutral grade that we're going
[15:48] to do some of our compositing work within, knowing that if we want to we can reverse
[15:52] that neutral grade later to get back to our original color.
[15:55] So I'll go tab and type in white balance TL.
[15:58] And if this doesn't appear for you right away, this is because this is part of the Tony
[16:02] Lions survival toolkit.
[16:04] If it doesn't appear for you, that means it's not installed or it's not installed correctly.
[16:08] And you can confirm that it's installed correctly.
[16:10] If you can see this little red Swiss army knife here, that means it's installed correctly.
[16:14] And if you can't, it means it's not installed correctly.
[16:16] Just to confirm who got to GitHub, creative lions, new survival toolkit, and you'll follow
[16:21] the download and install instructions there.
[16:24] So to get started with this white balance tool, let's just disable it and let's pick
[16:28] a kind of neutral area of the frame that we think should be true white.
[16:32] Let's say right here, and then we'll re enable.
[16:34] And that looks a lot more like true white to me.
[16:36] If we go back and forth, this looks very orange where this looks very much more white.
[16:40] And that's what we're after.
[16:41] The reason that you disable this while I'm working with the color picker, if we think
[16:44] about it, we're using this color picker to choose a value which then changes the overall
[16:49] look of the comp.
[16:50] If we keep this enabled and then we try and color pick like so, we're going to be getting
[16:54] lots of changes because it's adapting to the new look.
[16:57] So we'll just disable this while we pick our color and then re enable it after the color
[17:01] is picked.
[17:02] So like we said earlier, we can treat this white balance as a so-called neutral grade,
[17:07] meaning that we can grade it to be more neutral, having confidence that whenever we want, we
[17:11] can invert that neutral grade later.
[17:13] So imagine we have our neutral grade here, and then we do a bunch of compositing work.
[17:18] We know that we can always grab this, put it at the bottom later, and then reverse it.
[17:23] And then if we check between this reversed neutral grade and our original plate, we can
[17:28] have confidence that these two look the same.
[17:31] So you can kind of set this neutral grade to kind of whatever.
[17:34] I mean, it should look kind of neutral and normal, knowing that we can reverse it later.
[17:39] I might actually dial this back to around like something like this just to give it a
[17:42] little bit more of that kind of warmth, but not too far.
[17:46] So here's the difference between our original plate and our neutral grade.
[17:49] And then while we're at it, we might as well copy this neutral grade to our other two plates
[17:53] here.
[17:54] So let's make our next step merging over this plate over our sky.
[17:57] So we want to effectively remove this sky, and we can oftentimes do that with a simple
[18:01] Luma key here.
[18:03] And then we'll hit A to view our plate here.
[18:06] The white areas are areas that get past an alpha.
[18:09] So let's invert this so that our buildings are now white.
[18:12] And then we'll just dial in our key here.
[18:13] And we'll want to go for something where the edges are not too, too sharp because sharp
[18:17] edges in general kind of look ugly, knowing that we'll probably need to fill this out
[18:21] with a bit of supplementary Roto O for Roto node.
[18:24] And then I'll just fill in the areas that kind of got missed by the key.
[18:28] And when I use Roto, I almost always use this B-spline option just because it's much more
[18:32] flexible than using the Bezier.
[18:34] And to ensure we don't have any kind of sharp Roto edges, a lot of times I'll also just
[18:39] take this and hit E to feather out these edges, ensuring that we don't have any kind of stray
[18:44] edges like so.
[18:46] And our alpha is looking a lot fuller now, which is what we want.
[18:49] So you'll notice that nothing changed perceptually here for the RGB, and that's because we need
[18:53] to pre-multiply here.
[18:55] For multiplication, you can find tutorials on this.
[18:57] All it means is we multiply the values in our alpha by the values in our RGB.
[19:02] We have zero alpha up here, meaning the RGB here will be zero.
[19:05] We have one values right here, meaning the RGB will be the same value that it used to
[19:10] be before.
[19:11] And what that gives us is this transparent image.
[19:13] If we wanted to truly do our due diligence on this shot, we would use an additional key
[19:17] for this area here, or just it wouldn't take long to just Roto out these buildings here.
[19:22] For the sake of time, we'll just leave these as is.
[19:25] So let's merge over our building here.
[19:27] Here's what we'll get.
[19:28] So we might think to ourselves, okay, that kind of accomplished our goal.
[19:31] We're getting a lot more detail and saturation in the sky, but our eye might kind of tell
[19:36] us this looks kind of weird.
[19:38] I don't really know why it looks weird, but if I was watching this in a movie, I would
[19:42] definitely be able to tell that this sky was not real.
[19:45] So let's do ourselves a favor and check out some reference images to see if we can kind


### Applying Survival Skill 2 [19:46]
**Transcript (timestamped):**
[19:49] of diagnose why this might be looking kind of strange.
[19:51] So let's just go off to Google images and I'll just search.
[19:54] We shot this in scope a Macedonia.
[19:56] So I'll just search scope a Macedonia.
[19:58] Then I'll just look for some images of scope.
[20:00] When searching for references, there's always going to be some that are really heavily color
[20:04] corrected.
[20:05] And those are going to be images that we want to avoid images like this, something like
[20:08] this is extremely color corrected.
[20:10] So we'll want to find something a little bit more natural, something like this.
[20:13] Let's just try and kind of describe what we see in the sky to help us help our comp a
[20:17] little bit.
[20:18] So we're just describing the sky.
[20:19] I'll say it looks super blue near the top of the frame.
[20:22] And then as we go further toward the horizon, we get a little bit more brightness and a
[20:27] little bit less saturation, a little bit more white and a little bit less fully blue.
[20:32] Okay, so if we kind of go through some of these images, we'll probably start to form
[20:36] a pattern here where the same rules hold true.
[20:40] See something like this where we have blue saturation near the top of the frame.
[20:43] And as we go further toward the horizon line, we get less saturation and more brightness.
[20:48] And then probably each and every other image will probably see something similar.
[20:53] Here's a cool example where we have blue near the top of the frame.
[20:56] Then as we go toward the horizon line, we almost get this kind of pinkish magenta-ish
[21:00] hue, but also a little bit more brightness.
[21:02] Okay, so let's take what we learned here and apply it to our comp.
[21:06] Compared to our comp, a lot of those images were one, a lot less saturated than the sky.
[21:11] This guy is extremely saturated.
[21:12] And two, near the horizon line, we would expect a lot more brightness.
[21:16] This is looking pretty dark.
[21:17] The first step we'll probably take is to just adjust the positioning of this HDRI so that
[21:22] we're getting a little bit more of a natural positioning of our sky.
[21:26] Maybe scale up a touch.
[21:28] One step we could also take is increase the brightness of the horizon line, even a touch
[21:32] more.
[21:33] We may be able to bring the luminance of this top of the sky down a touch relative to the
[21:38] sky.
[21:39] We might grab this area near the horizon line and feather this out a bit.
[21:44] Probably gamma this up a touch.
[21:46] Maybe gain up a touch.
[21:47] And then we'll do pretty much the opposite to the top of the sky.
[21:50] Let's grab a cost rectangle here, feather it out down.
[21:53] We might be able to gamma down a touch.
[21:55] Maybe even bring up the blue and green a touch.
[21:58] I might also just overall multiply up a bit and we are looking pretty cool.
[22:03] Okay, so let's compare our sky now to the sky we had before.
[22:07] We've achieved our goal of providing more detail to this sky while also staying true
[22:10] to the references that we found online.
[22:13] Okay, so if we're using our rule of compositing an order of z depth, the next element we'll
[22:18] probably want to composite will be this tablecloth here.
[22:22] As you can see it goes over her leg, meaning it's going to be in front of the lady.
[22:25] And then finally our boy plate here.
[22:28] For the time being we'll leave these to you to composite completely and we'll move on
[22:31] to our flag element.
[22:33] Let's just do our quick A over B here and see how it's coming in.
[22:36] As you can see it comes in transparent and this is due to a kind of embarrassing problem
[22:42] caused by myself.
[22:43] I basically rendered this in my spare time and I didn't render it with an alpha and I
[22:46] didn't really have time to fix it.
[22:48] So we can use this opportunity to lean into some real world experiences.
[22:52] If you had a better lighter at a studio, this would definitely come in with an alpha.
[22:56] But considering our lighter is a total novice, it's coming in without an alpha.
[23:01] We can see here that we'll be able to probably pretty quickly key this and we will pre-mult
[23:05] to multiply our alpha by our RGB.
[23:08] And as you can see now we have our complete transparency along with our RGBA.
[23:13] The first thing you'll notice is that this is looking kind of insane.
[23:17] We'll use our next strategy to figure out why it might look so insane.
[23:21] So that's strategy three.


### Applying Survival Skill 3 (and a little 1B) [23:22]
**Transcript (timestamped):**
[23:22] There's tons of information in the plate, use it.
[23:25] So let's take a look at our plate here and compare it against our CG element.
[23:28] So the first thing we might notice is that this red here is looking extremely bright
[23:34] and extremely saturated.
[23:35] And the reason we're keying into that so fast is because we have a direct comparison of
[23:40] what this color of red should look like because of this red umbrella right here.
[23:44] So we know that this red umbrella is really what we should be aiming for and this red
[23:48] looks totally different from it.
[23:50] So that's an example of how we use the information in the plate to determine what our composited
[23:54] elements should look like.
[23:55] The next thing you're probably noticing is that this white looks very neutral whereas
[23:59] this one has a touch of kind of orange in there.
[24:01] You'll also notice that this beam of light here is causing this area to be super bright
[24:06] and then it casts a shadow right here which is pretty dark, which isn't being reflected
[24:10] in our CG element.
[24:12] We would expect that these flags should be pretty dark by comparison to the flag on the
[24:16] left here.
[24:17] We also might notice that the focus here is mismatched where we have a pretty soft out
[24:22] of focus element here whereas these flags are very sharp.
[24:26] We also might notice that our chromatic aberration and our lensing is very different where we
[24:31] have this orange edge here and this turquoise cyan edge here which is also not being reflected
[24:36] in the CG.
[24:37] Lastly we have this pretty extreme technical flaw where we have these extremely dark edges
[24:43] around our CG which we're also going to need to solve.
[24:46] We'll also probably key in on the fact that these are very noisy coming out of redshift.
[24:50] Okay so we've kind of keyed into the information that is in our plate that we're going to need
[24:55] to apply to our CG element so let's go ahead and get started with doing that.
[24:59] So maybe one of the first things I'll do is I'll address the luminance difference between
[25:03] our shadow to area and the plate and the same area in our CG.
[25:07] So I'll just grab a gray node here and a matte.
[25:10] I'll just gray down the side of the CG.
[25:13] One thing you'll notice as we gray this down is that we are getting a lot less brightness
[25:18] luminance off these but it still looks kind of wrong and that's because we still have a
[25:21] lot of contrast in these in an area like so where she's getting hit by a direct ray of
[25:26] light from the sun which is tucked behind this building here and then she falls off
[25:30] into shadow relatively quickly creating this high contrast area.
[25:34] When things aren't getting hit by direct light they're only getting hit by reflected light.
[25:38] We don't get those areas of high contrast because they're not getting hit by a direct
[25:41] light source.
[25:42] So that's something that we're going to need to address here.
[25:44] Again this probably should have been addressed in lighting by our terrible lighter myself
[25:48] but we have to deal with the situations presented to us.
[25:51] So the quickest way to kind of get rid of some of this contrast is just to bump up the
[25:54] gamma and then bump up the black point a bit and then we'll put our pre-mult under our
[25:58] gray here.
[25:59] We'll just need to continue to dial these in as we build our comp.
[26:03] Okay the next thing we'll probably notice that is kind of a glaring error is that we
[26:07] should probably desaturate these a touch.
[26:09] I might even desaturate these before my gray node so we'll just bump the saturation down.
[26:14] So the reason that desaturating before using your gray node helps a lot is because when
[26:19] we desaturate something that's super saturated we basically take values from the red channel
[26:24] and shuffle them into the other channels.
[26:27] That gives us more information to play with when we're trying to say make it more green
[26:31] or make it more blue.
[26:32] If there's no information in the green or blue channels if we try and adjust the blue
[26:36] channel we'll get kind of nothing because we're trying to adjust nothing.
[26:39] So desaturating before doing your color correction node can be a neat trick.
[26:44] We'll be continuing to try and get those closer and closer throughout the comp.
[26:47] So let's leave it there for now and move on to probably the next most glaring issue which
[26:51] is that these flags here are very sharp compared to our background here.
[26:55] So we'll use the focus in our background here to inform how focus these flags should be.
[27:01] So let's take a look at our plate to see where our flag should be sharpest.
[27:05] Probably the sharpest point in our plate is somewhere around her dress here in Z space.
[27:10] Then we'll follow that focus plane upward to our CG element to determine where it should
[27:14] be sharpest.
[27:15] And we'll say it's right here and we'll use an icon vol tool.
[27:18] This was created by a guy named Adrian.
[27:20] He's made a lot of other cool stuff too.
[27:21] So let's use this control mask to determine where we want our flags to be sharpest.
[27:26] Sharpest right here and as we go out we'll get progressively softer.
[27:30] So you're probably already noticing that this control mat is doing the opposite of what
[27:34] we want it to be doing.
[27:35] The areas closest to the center are the most defocused whereas we want the areas closest
[27:41] to the center to be the sharpest or the least defocused.
[27:44] So we just need to invert our control mask here.
[27:47] We'll do that using an invert node.
[27:49] If we take a look at our control mask before and after we'll hit A here in order to see
[27:53] the alpha and then we can A, B using one, two.
[27:56] And as you can see these are inverted.
[27:57] So now let's take a look at this area that we were keyed in on earlier.
[28:00] The focus of this background is relatively defocused whereas the defocus of our CG element
[28:05] here is massively, massively defocused.
[28:07] So we'll want to address that just by adjusting the max size here to kind of match it to this
[28:12] background here.
[28:13] We'll also probably use our intuition to know that these should be actually less defocused
[28:18] than this background element here because they're closer to the focus plane.
[28:22] So the more OCD among you will probably also be screaming to yourself about this black
[28:28] edge here which is very, very ugly and we need to fix.
[28:31] So we'll do that using an edge extend tool and let's go back to one of our prior principles.
[28:35] We'll use 1B, Google stuff and say how to extend edges in Nuke.
[28:39] If you're not familiar with Nukepedia, Nukepedia is basically a database of user created tools
[28:44] that was often used on a day to day basis by compositors in the industry.
[28:48] So we can just go to really any of these tools.
[28:50] Edge extend, there's probably 15 or 20 of these on Nukepedia, maybe even more.
[28:55] But the one we'll use today is called lens edge extend.
[28:58] Connect our RGB to our source.
[29:00] Edges is what this gizmo calls alpha.
[29:02] We also will probably need to recopy our alpha here to our original stream and then see what
[29:07] we get.
[29:08] And right off the bat we're getting an improvement to our result.
[29:11] So here's before and after.
[29:12] So what this is doing is just taking our RGB pixels and pushing them outward according
[29:17] to the alpha.
[29:18] Okay, one thing we also might try is to bump up the black point so that we're not getting
[29:22] such crazy black on the string edges.
[29:24] And then we might even be able to cheat our edges a bit more so that the black isn't so
[29:29] noticeable and we'll call that fine.
[29:32] And last thing we might notice on these is that our chromatic aberration on our plate
[29:37] is not matching the chromatic aberration in our CG element and we want to fix that.
[29:41] We want to match the lensing of our CG element to the lensing of our plate.
[29:44] There is a handful of chromatic aberration tools in the survival tool kit.
[29:47] So we'll go chromatic aberration.
[29:50] There's a few here.
[29:51] If these don't work for you, you can also go onto Google and go chromatic aberration
[29:55] Nukepedia and then there's probably going to be another 15 or 20 of these.
[29:59] So the one that I ended up grabbing was called K Chromatic I think.
[30:03] And we can just hop in and start kind of messing around with this.
[30:06] So we'll notice here that this is producing a result that kind of resembles our plate.
[30:11] But you'll also notice that this turquoise color, while it is close-ish to this color,
[30:16] it's on the wrong side.
[30:17] We have this blue element on the right side, this orange element on the left side.
[30:20] So maybe we will just kind of mess around with our controls here.
[30:24] It's possible that we might also just want to mix this in a little bit.
[30:27] Okay, this comp is obviously incomplete, but you'll be using these techniques for every
[30:31] step of the process.
[30:32] And that brings us to another skill set that we're also going to be using pretty relentlessly
[30:36] throughout the process.


### Applying Survival Skill 4 [30:37]
**Transcript (timestamped):**
[30:38] Always assume we can improve our comp until time runs out.
[30:42] And so here's the comp that I came up with and time ran out pretty quick for me.
[30:45] So there's definitely a lot to critique in here.
[30:47] And that's going to be what we're going to do now.
[30:49] Learn how to really be critical of our own work so that we can take steps to improve
[30:53] our own work.
[30:54] First thing we'll notice here is that these could definitely be darker, right?
[30:59] We talked about this earlier.
[31:00] These should be in shadow.
[31:01] Another thing we'll notice is that our white balance on these looks a little bit off.
[31:04] These are looking kind of pink to me, whereas this area is looking turquoise-ish by contrast.
[31:09] Another thing I'll notice is that we have some kind of gnarly lines right here that are coming
[31:14] off of the key.
[31:16] So we could probably use either an edge extension tool or paint these in a little bit more or
[31:20] just get our alpha a little bit tighter.
[31:22] We'll also notice some retime artifacts here.
[31:24] This lamp gets kind of pushed in by the boy.
[31:27] And then we'll also notice some kind of gnarly keying issues here.
[31:30] There's actually more in here that we could probably dig into, but I just wanted to demonstrate
[31:34] the principle of this is my comp.
[31:36] It's not perfect by any stretch.
[31:38] And I need to be able to acknowledge that so that I can make my work better and better
[31:42] and better.
[31:43] And it's not that we should always be depressed that our work is always wrong.
[31:46] We should always have confidence in our ability to critique our own work.
[31:49] And that's the only way that we can improve our work and make our work better is if we're
[31:54] able to be really harsh on ourselves.
[31:55] Our final principle of compositing is find mentorship where you can.


### Applying Survival Skill 5 [31:57]
**Transcript (timestamped):**
[31:59] And that can be in many different forms.
[32:02] Probably one of the better forms is to find someone at work who you can just ask a lot
[32:05] of questions to, even if it's not a formal mentor-mentee relationship, just try and absorb
[32:10] as much information from them as you can.
[32:12] If you're not working at a studio, there are other ways to find mentorship.
[32:15] And that can be online.
[32:17] You can find people on the Foundry forums who know a lot.
[32:19] You can also find people on the Discord who are very willing to share their information
[32:23] with you.
[32:24] And that includes me.
[32:25] I started this and there are lots of people who are very active on here who know a lot,
[32:29] who can help you work through your comms.
[32:31] And then you can also find a more formal relationship with a mentor by going to AccessVFX, accessvfx.org.
[32:38] And on AccessVFX, you can be paired with a mentor who knows a lot about compositing or
[32:43] VFX in general.
[32:44] I'm a mentor on here.
[32:45] And there are lots of other mentors who are very forthcoming with their wisdom on, for
[32:49] example, industry stuff, how to get a job at a studio, but also the technical stuff
[32:53] of how to improve your compositing work.
[32:55] Okay, so we'll say that we've done our compositing work on some of our shots and it's time to
[33:00] implement those shots back into our edit.


### How Nuke Studio Saves Hours of Shot Matching [33:01]
**Transcript (timestamped):**
[33:02] So we'll hop over back to Nuke Studio here and we will try and import our VFX work back
[33:07] into our Nuke Studio project so that we can view it as an edit and so that we can critique
[33:12] our own work.
[33:13] This would work also if you had, say, five other compositors working with you and they
[33:16] were working within the correct Nuke scripts and output structure, you could import their
[33:20] work into Nuke Studio too.
[33:22] We'll just highlight our entire edit here and we will choose build track from export
[33:27] structure and then we will find the Nuke write node that we've specified prior and that's
[33:32] the output path that all of our Nuke scripts are going to be writing to and then we'll
[33:35] select that and build and let's call this Foundry 2.
[33:39] In real time up here is this new track Foundry 2 getting populated with all of our VFX work
[33:44] that we've completed on these shots.
[33:46] As long as it was rendered using that specified write node.
[33:49] If you are working at a studio that did not have access to Nuke Studio, it can take literally
[33:54] hours to find all the correct paths, put them into your timeline, trim them to the correct
[34:00] handles, make sure they're lining up with the offline, etc.
[34:03] And that's something that has just been completed for us by Nuke Studio just in the time that
[34:07] I've been talking.
[34:08] And so this will enable us to export all of our shots either as a full edit or it can
[34:12] even be exported as individual shots say for a colorist to do their color work on.
[34:18] And in order to do that we would just highlight our entire edit here.
[34:21] We would click export and then we would process as shots and we can export individual MOVs
[34:26] for each and every shot or process as a sequence.
[34:29] We could export as literally any type of file format or even as an XML as well.
[34:33] Okay, so that wraps up our quick demo on how to get started with this practice material.
[34:38] If you have any questions about this, I created this Discord server specifically for questions
[34:42] and it has since grown into a general Nuke knowledge forum.
[34:47] And I look forward to seeing all these shots on your reels and good luck and having a good
[34:51] day.



---

## Captured Frames

- [5:19] tutorials/frames/skill-up-with-nuke-how-to-think-like-a-pro-compositor/frame_000.jpg
- [9:08] tutorials/frames/skill-up-with-nuke-how-to-think-like-a-pro-compositor/frame_001.jpg
- [10:44] tutorials/frames/skill-up-with-nuke-how-to-think-like-a-pro-compositor/frame_002.jpg
- [12:48] tutorials/frames/skill-up-with-nuke-how-to-think-like-a-pro-compositor/frame_003.jpg
- [15:58] tutorials/frames/skill-up-with-nuke-how-to-think-like-a-pro-compositor/frame_004.jpg
- [18:09] tutorials/frames/skill-up-with-nuke-how-to-think-like-a-pro-compositor/frame_005.jpg
- [20:00] tutorials/frames/skill-up-with-nuke-how-to-think-like-a-pro-compositor/frame_006.jpg
- [21:50] tutorials/frames/skill-up-with-nuke-how-to-think-like-a-pro-compositor/frame_007.jpg
- [25:10] tutorials/frames/skill-up-with-nuke-how-to-think-like-a-pro-compositor/frame_008.jpg
- [27:26] tutorials/frames/skill-up-with-nuke-how-to-think-like-a-pro-compositor/frame_009.jpg
- [28:57] tutorials/frames/skill-up-with-nuke-how-to-think-like-a-pro-compositor/frame_010.jpg
- [29:50] tutorials/frames/skill-up-with-nuke-how-to-think-like-a-pro-compositor/frame_011.jpg
- [33:27] tutorials/frames/skill-up-with-nuke-how-to-think-like-a-pro-compositor/frame_012.jpg

---

## Structured Notes

### Core Technique
An official Foundry-commissioned video (by compositor/director Peter Timberlake) teaching a **problem-solving framework** for compositing rather than a single technique — five "survival skills" (use what you know → Google relentlessly → ask forums/Discord when Google fails → use real-world reference → read the information already present in the plate → critique your own work relentlessly → seek mentorship) — applied live across a real multi-element shot build (sky replacement, CG flag integration, stabilization, shadow/focus/lensing matching) using Peter Timberlake's own free downloadable practice plates and the community-made "Nuke Survival Toolkit" gizmo pack.

### Summary
Introduces free practice plates (petertimberlake.com) designed for compositors to build a reel, plus the "Nuke Survival Toolkit" (GitHub: creativelyons/nuke-survival-toolkit) — a community gizmo pack used throughout. States the five survival skills up front, then covers **Nuke Studio** project setup: exporting an XML from editorial (Premiere/Resolve/Avid) into Nuke Studio's timeline, a token-based project/export naming convention (Sequence/Shot/Track/Version tokens like `SEQ010`/`SH0070`/`BG01`/`0001` driving both the EXR export path and an auto-generated Nuke script with pre-wired Read/Write nodes), and the payoff — **Build Track from Export Structure** later re-imports completed VFX renders straight back into the Nuke Studio timeline for review, a task the video says can otherwise take hours of manual path-matching per shot. Sets project color management to **OCIO / ACES 1.1** (confirms ACEScg and Scene-Linear are the same colorspace within the ACES OCIO config) before any comp work, since footage reads flat/greenish under the wrong colorspace. Applies the five skills live on two shots: **Shot 60** — diagnoses handheld-camera mismatched motion between plates ("swimming" on a naive over) by reasoning from first principles (Skill 1) that stabilizing each plate first would fix it, then Googles "how to stabilize in Nuke" (Skill 1B) and uses a `Tracker` node (multiple tracking points via Ctrl+Alt+Click, Transform export set to Translate/Rotate) to stabilize — noting the forums/Discord fallback (Skill 1C, e.g. the Foundry forums or the presenter's own "Nuke Coven" Discord) for when tracking alone doesn't fully solve residual swimming at the frame edges. **Shot 70** (the main build) — establishes a back-to-front compositing order (sky → distant plates → tablecloth → boy, furthest-to-nearest in Z), starting from an empty `Reformat` node matched to the plate format, then **Crop**ped to the viewport to avoid Nuke calculating far more data than needed. White-balances the lady plate using the toolkit's `WhiteBalanceTL` gizmo as a reversible "neutral grade" (disable the gizmo while color-picking a should-be-white area, re-enable — picking with it live re-adapts and gives wrong results), explicitly treated as invertible later to recover the true original grade; copies the same neutral grade to the other plates. Removes the sky via a **Luma key** (inverted so buildings read white/opaque), supplemented with a `Roto` node (B-spline shapes preferred over Bezier for flexibility, edges feathered with `E`) to patch key gaps, followed by a **Premult** to make the alpha edit visible in RGB. After merging a replacement sky, applies **Skill 2 (reference)** — Google-Images research on the real shoot location (Skopje, Macedonia), explicitly avoiding over-color-corrected reference images, extracting a pattern (more saturated/blue near the top, brighter/less saturated toward the horizon) and re-grading the sky to match (repositioning/scaling the HDRI, feathered horizon/top-of-frame color corrections, gamma/gain adjustments) rather than trusting the eye alone. For a CG flag element rendered without alpha (a deliberate "real-world experience" callout — bad lighter output happens on real jobs) keys and premultiplies it in, then applies **Skill 3 (read the plate)** — a side-by-side comparison against a real red umbrella already in the plate to correct the CG's oversaturated red, matches white balance, and identifies four more plate-vs-CG mismatches to fix: (1) shadow/contrast (a `Grade` + garbage matte darkens/desaturates the shadowed side, desaturating *before* the Grade specifically because desaturating redistributes red-channel information into green/blue so those channels have something to actually grade), (2) focus mismatch — samples the real focus falloff from the background plate, builds an `IconVOL`-based defocus control mask (inverted, since the tool's default treats center as most-defocused when the opposite was needed) to drive a Defocus/blur matched to the plate's focus falloff, (3) a harsh black edge from the flag's key — fixed with the Nukepedia `Lens Edge Extend` gizmo (RGB into Source, alpha into its "Edges" input, alpha recopied back afterward) plus a black-point lift, (4) mismatched chromatic aberration — matched using a toolkit chromatic-aberration gizmo (`K Chromatic`), correcting for the tool's default color-fringe orientation being backwards relative to the plate's real orange-left/turquoise-right fringing. Closes with **Skill 4 (self-critique)**: the presenter reviews his own intentionally time-boxed, imperfect comp on camera, listing concrete flaws (shadows should be darker, white balance drifting pink/turquoise, ragged key edges, a retiming artifact where a lamp gets visually "pushed" by the running boy, residual keying issues) as a demonstration of the critique habit itself rather than a finished result — and **Skill 5 (mentorship)**, pointing to Foundry forums, the presenter's Discord, and AccessVFX (accessvfx.org) for formal mentor pairing.

### Key Steps
1. Set project color management: `S` (project settings) → Color Management → OCIO → OCIO Config → **ACES 1.1** (fixes flat/greenish-looking Read nodes; confirms ACEScg = Scene-Linear within this config).
2. Install the community **Nuke Survival Toolkit** (GitHub: creativelyons/nuke-survival-toolkit) — verify install via a red Swiss-army-knife icon on its gizmos.
3. **Nuke Studio project setup:** import an XML export from editorial → set up a token-based naming/export structure (Sequence/Shot/Track/Version) → Export to generate per-shot EXR plates + pre-wired Nuke scripts (Read node pointed at the exported plates, Write node pre-pathed per the export structure).
4. **Stabilize mismatched-motion plates:** `Tracker` node → place multiple tracking points (Ctrl+Alt+Click) → select all → export Transform (Translate + Rotate) → apply to stabilize each plate independently before compositing them together.
5. **Compositing order:** build back-to-front in Z-depth (sky first, then progressively closer elements) starting from an empty `Reformat` node matched to plate format, `Crop`ped to the working viewport/format to limit unnecessary calculation.
6. **Reversible neutral grade:** `WhiteBalanceTL` (survival toolkit) → disable the gizmo → color-pick a should-be-neutral-white area of the plate → re-enable → copy the same grade to other plates sharing the same lighting; keep it invertible for later.
7. **Sky replacement:** `Luma` key on the original sky plate (invert so the subject/buildings read opaque) → patch key gaps with a `Roto` node (B-spline shapes, feathered edges via `E`) → `Premult` → merge the replacement sky over.
8. **Reference-driven sky grading:** research real photos of the shoot location, avoid heavily-graded reference images, extract a color pattern (saturation/brightness gradient top-to-horizon) → reposition/scale the sky HDRI and grade top vs. horizon regions separately (feathered garbage mattes + gamma/gain) to match.
9. **CG element cleanup:** key + `Premult` a no-alpha CG render → compare directly against a matching real object already in the plate (e.g. a red umbrella) to correct color/saturation.
10. **Shadow/contrast matching:** desaturate the CG element *before* a `Grade` (redistributes channel information for more effective grading), grade with a garbage matte to darken/reduce contrast on the shadowed side to match the plate's directional lighting.
11. **Focus matching:** sample the plate's real focus falloff → build an inverted `IconVOL`-driven defocus control mask (sharpest at the correct depth, softer outward) → apply Defocus to the CG element accordingly.
12. **Edge cleanup:** Nukepedia's `Lens Edge Extend` gizmo (RGB → Source input, alpha → its Edges input, recopy alpha afterward) to push RGB outward along the alpha edge and remove harsh black fringing; lift the black point further if needed.
13. **Chromatic aberration matching:** apply a toolkit CA gizmo (`K Chromatic`), correct its default fringe-color orientation to match the plate's actual left/right color-fringe direction, mix to taste.
14. **Self-critique pass:** review the finished (intentionally time-boxed) comp against the original diagnostic list — shadow darkness, white balance, key edge quality, retiming artifacts — as an explicit, repeatable habit rather than a one-time step.
15. **Shot re-integration:** back in Nuke Studio, select the edit → **Build Track from Export Structure** → point at the Write node's output path → auto-populates a new timeline track with completed VFX renders for review; export the reviewed edit as full-sequence or per-shot MOVs (or any supported format/XML) via Export → Process as Shots/Sequence.

### Nodes / Tools / Settings
`Tracker` (multi-point stabilization, Translate+Rotate export), `Reformat`, `Crop`, `WhiteBalanceTL` (Nuke Survival Toolkit gizmo), `Luma` key, `Invert`, `Roto` (B-spline shapes, feather), `Premult`, `Grade` (with garbage mattes, pre-desaturation trick), `Saturation`, `IconVOL` (defocus control-mask tool, by "Adrian"), `Defocus`, `Lens Edge Extend` (Nukepedia gizmo), `K Chromatic` (Nuke Survival Toolkit chromatic-aberration gizmo), OCIO / ACES 1.1 color management, Nuke Studio (Timeline, token-based Export structure, Build Track from Export Structure, Export → Process as Shots/Sequence).

### Difficulty
Beginner-to-intermediate technically (individual nodes are standard/well-known), but the actual content — a repeatable problem-diagnosis methodology — is valuable at any experience level; several steps assume comfort installing/using third-party gizmo packs (Nuke Survival Toolkit, Nukepedia tools).

### Foundry App & Version
Nuke + Nuke Studio (version not stated on screen or in narration; ACES 1.1 OCIO config and the described UI are consistent with a recent Nuke 15.x/16.x/17.x release).

### Tags
compositing, nuke-studio, color-management, ocio, tracking, keying, roto, grading, defocus, edge-extend, chromatic-aberration, editorial, conform, beginner, intermediate

---

## Related Tutorials
None yet — first Nuke tutorial in this library. Cross-link future compositing-fundamentals or Nuke Studio workflow tutorials here.
