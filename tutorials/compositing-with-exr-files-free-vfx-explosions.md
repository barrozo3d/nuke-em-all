---
title: Compositing with EXR Files | FREE VFX Explosions
source: YouTube
url: https://www.youtube.com/watch?v=Ps7LQcKNPWc
author: Compositing Academy
ingested: 2026-08-17
app: "Nuke"
version: "Not specified numerically; UI consistent with the modern node-graph era seen elsewhere in this batch"
tags: [compositing, channels, grading, aovs, gizmo, fx-simulation, color-management, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/compositing-with-exr-files-free-vfx-explosions/
frame_count: 9
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Compositing with EXR Files | FREE VFX Explosions

**Source:** [YouTube](https://www.youtube.com/watch?v=Ps7LQcKNPWc)
**Author:** Compositing Academy
**Duration:** 21m52s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to this tutorial. We're going to be composing explosions.
[0:03] So if you like explosions, you're probably downloading this explosion because you want to learn how to composite it.
[0:07] So this is actually a pretty cool render that you're getting. It's a multi-layered EXR.
[0:12] So if you haven't worked with those before, essentially what you can do is you can take this multi-layered EXR and adjust each layer independently.
[0:18] So for example, you can adjust the lighting on one side of the explosion or you can extract the glow as its own pass, its own layer.
[0:26] So Nuke is really good for this. We're going to be using Nuke to composite it and you'll actually see how it works.
[0:30] And so we're going to talk on a very beginner level with Nuke.
[0:33] So if you never use Nuke, there's an After Effects to Nuke free masterclass that's included.
[0:38] So you can click in the link below if you want to take that masterclass.
[0:41] My background has been working in feature films.
[0:43] So I've been using Nuke on films like Star Wars, Avengers, Across the Spider-Verse and a bunch of other projects.
[0:49] But I started out also in After Effects.
[0:51] So basically, if you want to transfer your skills really quickly, that's software to do it.
[0:55] If you're more of a CG guy, if you're doing like Blender and Unreal or Houdini,
[1:00] basically all senior generalists in the industry are also composing with Nuke.
[1:04] So, you know, for example, Unreal has an Unreal Engine bridge that connects to Nuke and you can polish your CG renders really effectively.
[1:11] So that's all information to know. Check out the free masterclass below and we'll go into the explosion tutorial and explain how we can actually use this render in your own CG shots.


### Project Explanation [1:15]
**Transcript (timestamped):**
[1:20] Alright guys, so this is going to be the render that we're working with.
[1:23] So this is after the composite. We're going to do some glows.
[1:26] We're going to break out the layers and show how a multi-layer EXR works.
[1:30] So this tutorial is really geared for people who haven't done a multi-layer EXR composing.
[1:35] So if you're a beginner, this will help you out.
[1:37] If you're more intermediate, you might see some interesting things in here related to just how to grade stuff.
[1:41] So you can probably skip to the middle of the tutorial, but essentially that's the level that we're speaking at here.
[1:46] So there are four free explosion downloads.
[1:48] You can use them in any project or film that you want as long as it's in a final project form.
[1:52] So that's essentially what's in the link below as well as the After Effects to Nuke course.
[1:57] So essentially, the first thing we want to do though is switch this project into Aces.
[2:00] So if you opened up your Nuke script automatically when you open the software, it's not going to be set to Aces.
[2:05] And you've probably heard Aces, but I'm not going to do a full technical Aces tutorial right now,
[2:10] but I will show you a quick understanding that you can understand how it immediately will help you to switch into Aces.
[2:16] So essentially to do it, you hit S while pointing here and we want to go into the color settings.
[2:22] Switch to O C I O and switch to Aces 1.2 or Aces 1.3.
[2:27] And you can just basically close that and you'll see up here it says SRGB Aces if you've done it correctly.
[2:32] So what that actually does is the highlights are going to roll off a little bit differently when we grade this explosion.
[2:38] It makes it a little bit easier to get a better result much quicker.
[2:41] So that's one of the benefits of Aces and we can compare to a Aces and not Aces footage.


### ACES Explanation [2:46]
**Transcript (timestamped):**
[2:47] So this is the same footage. This is 8-bit footage. There's no high dynamic range.
[2:51] This wasn't shot in log or anything like that. It's just really normal footage out of a phone.
[2:56] And essentially on the right here, it's not Aces and on the left it is Aces.
[3:01] Now right now they're exactly the same. They've been loaded in.
[3:04] And when you bring them in, by the way, you just double click it and you load is SRGB.
[3:09] You know, because that's a standard color space for an image.
[3:11] Again, going to technical, but essentially if we gain this down, we can bring this line down here
[3:18] and you'll see that it looks kind of flat when we darken it.
[3:20] We don't see any more detail and that's to be expected.
[3:24] You don't necessarily have more detail in the highlights,
[3:26] but this is kind of what happens when you're in a normal sort of color management workflow here.
[3:31] Now if you switch to Aces, it's just the math and the way that the highlights are being handled.
[3:36] If you actually pull this game down a little bit, you'll actually see that everything looks like it has more detail in there.
[3:41] So there actually is more detail.
[3:43] It's just that when you're not in an Aces workflow, the way the highlights are managed,
[3:47] as you're pulling or pushing them, this is doing basically some special tone mapping around the highlight regions,
[3:53] which gives it just a better result immediately.
[3:56] So you can see the difference.
[3:57] Look how flat this looks and look at how much more there was actually in the image, even just the 8-bit.
[4:02] So that's good to know and especially if we're going to start doing an explosion where the highlights really matter.
[4:07] So that is essentially why I wanted to just really quickly touch on that, even though we're in a beginner tutorial.
[4:12] So we're in Aces and this is the image that we can start with.


### Layered EXR [4:15]
**Transcript (timestamped):**
[4:16] So this is my little node tree here.
[4:18] If you've never worked with nodes, again, go check out that free tutorial,
[4:22] but I'll talk to you on a still beginner level here just to not lose anybody.
[4:26] So we have the explosion.
[4:28] We're going to pull it into Nuke.
[4:29] So you just drag in the image sequence or you do a read node by typing read,
[4:33] and then you can load in the image by just finding the path.
[4:36] So I'll just paste it over here to the side, copy and paste, and we're going to do this from scratch.
[4:41] So these are the shuffle nodes here that will break out the different layers that are stored in here.
[4:46] So this is not like a normal movie file.
[4:48] It's not a quick time.
[4:49] This is an EXR that has multiple passes in it.
[4:52] So this is a multi-pass CG compositing.
[4:54] So if we click here and we go to this little tab,
[4:56] we can actually see the layers that are stored within this image.
[4:59] And that's why if you go download this, you'll see that the file size is kind of big
[5:03] because there's a lot of data in there and it's all high dynamic range.
[5:06] So there's a lot of data being stored in one single frame, for example.
[5:10] So if we want to see one of the layers, we can see we're looking at RGBA,
[5:13] which is kind of like the main area that we normally composite in.
[5:16] But if we go to any of these layers, we can actually see the aspects of this explosion.
[5:22] So we can look at different lights, for example, and we can see like just the light on one side of the explosion.
[5:29] So our ability to look at those layers, I can brighten it up to see it better.
[5:34] We can actually break these layers out and recombine the image in a different way.
[5:38] So this is our main image that's combined, but we can break those layers out and recombine them.
[5:43] So that's essentially what we're going to do.
[5:44] So I'll hit Tab here and type shuffle.
[5:47] And shuffle is the node that you're going to use to essentially pull these layers out into our main RGBA layer
[5:52] where we're doing the composite.
[5:53] So these layers are stored in different layers, but we want to be working all in here.
[5:57] So it's basically taking the data from any of one of these, we're putting it into here,
[6:01] and that's where we're doing essentially the composite.
[6:04] So I'll bring this down, I'll hold Ctrl to create a little dot,
[6:07] and then I'll just bring it off to the side here.
[6:09] And I'm going to grab a few of the light layers that are in here.
[6:14] So essentially, first we'll grab the spotlight side all.
[6:18] So we have a spotlight from the left side.
[6:20] I'll just copy and paste this.
[6:22] So Ctrl C, Ctrl V, and we'll keep it connected.
[6:25] So they're always pointing into the same image here.
[6:28] And we'll grab another one, spotlight all, which is just from the other side,
[6:32] copy and paste, double click it.
[6:34] And the one we're double clicking on, you see the shuffle eight.
[6:37] This is the one that we're opening in our properties panel over here.
[6:40] So we close this one, and then we'll grab another one.
[6:43] Let's say the second fire, one of these channels I think are empty.
[6:49] So some of them don't have anything, I believe.
[6:51] I think it's this one, the NoMap all.
[6:54] So that's like kind of an ambient light overall.
[6:58] I can just double check here to make sure.
[7:00] So we have spotlight, spotlight all, and end NoMap all.
[7:04] So that's like our three main ones.
[7:07] If you forget the names, you can see them here, spotlight, spotlight, and end light.
[7:13] And then there's one more layer we want to pull out.
[7:15] So I'll copy and paste, and we'll just click here and we'll click on all emission.
[7:19] So this is going to be the essentially the light, the emissive light that's coming out of this
[7:24] explosion.
[7:24] So essentially what we want to do here is we want to recombine these back together.
[7:29] So we actually don't need to see this original image anymore.
[7:32] What we're going to do is take these layers that have been pulled out and recombine them back
[7:37] together.
[7:37] We're not going to do anything to the layers yet.
[7:38] We just want to recombine them so that they match the original image.
[7:42] So what we can do is we put a merge node and we see this node, which has the light,
[7:47] and this node, which has another light.
[7:49] I'm hitting one to switch where I'm looking at the different nodes here.
[7:52] And we'll say A and B, and then we'll merge them together.
[7:56] So that will combine the two.
[7:58] So if I hit disable and enable, you see they're being merged together.
[8:00] We want to switch this to a plus.
[8:02] Whenever we're adding light of passes together, it's always a plus.
[8:06] So copy and paste this.
[8:08] And I'll switch the input here by hitting shift X.
[8:11] So I want the A to always go over the B.
[8:13] That's the good way of doing compositing.
[8:15] So if you get more interested in Nuke or if you're already intermediate, you already know this.
[8:19] So A over B and then A over B.
[8:22] So I'll hit shift X and then A over B.
[8:24] So essentially we're just merging these all together.
[8:26] If you imagine Photoshop, like layers, each one of these is like a layer.
[8:30] So if I put little corners here by hitting control, it'll be a little bit more visually
[8:35] understandable.
[8:37] So you can imagine that each one of these is like a layer.
[8:41] So we have like the base image.
[8:42] We have another image being merged over that one,
[8:45] another one going over that one, etc.
[8:48] Now what is interesting about this is if we look at the end result and we compare to the original,
[8:52] we should basically have the same result.
[8:54] It looks like we might have one slight pass missing here.
[8:57] So we could probably go in there and find whatever that one is.
[9:00] So it looks like we just have one more pass called pyro volume light all.
[9:03] So we just need that extra one.
[9:04] It just gives the luminance a little bit more in there.
[9:08] So we'll just connect that.
[9:10] I don't think we'll grade that one for anything, but we want the beauty to match the
[9:14] recombined version that we recreated here just to make sure that we're doing it right.
[9:18] So if you look at the end and then we hit two on our keyboard,
[9:21] so we can have multiple inputs.
[9:23] So if you're new, we can hit two and we can hit one on your keyboard and you can switch between the two.
[9:28] So that's essentially what I'm doing.
[9:29] I'm hitting one and two and we can see there's no difference between those two different images.
[9:33] So we've recombined it and we're all good.
[9:35] So that's cool, but it's not really doing anything.
[9:38] But now what we can do is go in between any of these layers and we can add a grade node
[9:43] to adjust the look.
[9:44] So for example, if we go up to, let's say,
[9:48] shuffle seven that has this light from the right side,
[9:51] if we put a grade node by hitting G and we disable this,
[9:55] we can grade this up.
[9:56] And if I look at the grade by hitting one, so if I hit one here and one here,
[10:00] we see that it gets brighter.
[10:01] So we're making that light brighter and we're recombining the image together.
[10:05] So let's go to the very bottom and let's go a little bit further in the image so we can see
[10:08] more clearly exactly what we're doing.
[10:12] We can see we've made this light that's on the back much brighter.
[10:17] So if I disable it and enable it, we can see how we're actually modifying the image in its different
[10:22] elements to create a result that's different.
[10:25] So I'll disable it.
[10:26] Let's put a grade node on a different one just to show it and we can grade it up.
[10:30] I'm looking at the end of the composite here.
[10:32] So my viewer node is attached to the very end after we've combined them all.
[10:36] So I can put a grade on any of these layers and we can see the modifications as we do them.
[10:40] So we can go here, we can grade up just the emission.
[10:44] So this is going to be how we can create a brighter or darker emission.
[10:48] So that's going to control the glow or the color of the fire and the burning fuel,
[10:54] essentially that's in this explosion.
[10:57] So if I bring it down all the way, we see that just the remaining layer, which is this
[11:02] volume light all.
[11:04] Now in my original comp, I didn't even use that layer for whatever reason.
[11:08] So I'm just going to disable it for now.
[11:09] We're just going to leave it off this comp because I don't actually need it.
[11:12] But it is there if you want the extra control.
[11:16] So let's look at the end result.
[11:18] Right now we have no fire.
[11:19] Right now we have fire free enabled.
[11:20] So that's what this grade is doing.
[11:22] So that's the basic idea of multi-pass CG compositing.
[11:26] You can break out all your CG layers, modify them in a really, really detailed way,
[11:30] and then reassemble them together.
[11:32] Now what we want to do is actually start to create a nice looking glow on this explosion.
[11:37] We're going to comp it as if it's nighttime.
[11:40] We're not going to put it on a background or anything, but explosions can look different
[11:44] based on how exposed your camera is.
[11:47] So if your exposure is higher or lower, it's going to actually affect how much glow
[11:52] or how much detail you're actually seeing.
[11:54] For example, if you're at nighttime and there's a person standing in the night
[11:58] and you're exposed to them, meaning you see all the detail on the person,
[12:03] something as bright as an explosion would probably appear almost pure white.
[12:08] You would see almost no detail at all.
[12:10] All the detail gets lost because the camera is not exposed to that detail.
[12:14] So this is where an understanding of photography comes in and exposure.
[12:17] So we're going to kind of composite where it still looks cool and we still see some of that
[12:22] detail.
[12:22] So we're exposed a little bit into it.
[12:24] And that's something to keep in mind as we move into this.
[12:28] So explosion, a little bit too red for me right now.
[12:31] So first thing we're going to do is just start to take out a bit of the red.
[12:33] So we go to the grade node, we'll click on one of these little color wheels,
[12:36] and we'll just start to pull down the red in here.
[12:39] And you see we're only doing this in this little layer,
[12:42] this little stream that we've created in only the emission pass.
[12:46] So if I double click the shuffle, it's the all emission.
[12:49] So I could take a little bit of that red out and make it a little bit more of a
[12:52] natural color for an explosion, which is this kind of orangish result that we have here.
[12:59] Now, what we can also do is let's start to just add a glow to it and see what happens.
[13:04] So essentially the glow is something you have to kind of modify quite a lot sometimes when
[13:08] you're doing explosions, meaning it might be too much glow at one frame and then not enough
[13:14] glow in another frame. So a lot of times you have to manually adjust your brightness to get it to
[13:18] look good. But essentially what we want to do is we'll start by just getting a glow in there just


### Explosion Glow [13:21]
**Transcript (timestamped):**
[13:22] to see what the base will look like. So I'm going to put a keyer node by hitting tab, type in keyer.
[13:28] And this node essentially lets you target the highlights. So I'll hit A and we can see that
[13:32] it's creating an alpha targeting the highlights. This is basically looking at the brightness of the
[13:36] image. And I'm going to increase the value of this little slider here. Usually the vast majority
[13:41] of the time you're only using A and B, which basically selects the range of the highlights
[13:46] that you're trying to target. Now, because this is essentially working aces and we have a high
[13:50] dynamic range explosion, if we sample here by hitting control, we see the values are really high,
[13:55] like eight in some of the values or two or three. So right now it's only selecting between zero and
[14:00] one, but we want to really target into the highlights. So what I'm going to do is go to the
[14:03] B and hit the arrow key and hit up. And that's just going to allow us to target even further
[14:08] into those highlights. So we can really target just the very, very bright areas. So now that we've
[14:14] targeted, we need to do something with it. So I'm going to hit pre-mult node by typing hit tab and
[14:19] type pre-mult. And this will essentially multiply the alpha that we've created against the colors of
[14:25] the image, essentially cutting out the bright areas that we've just targeted. So we have just
[14:29] the bright areas and the color combined. So essentially like this, and then we can put an
[14:34] exponential glow node. So this node will come in the script that I provided you guys. It's a custom
[14:39] node that creates a nice looking glow. And yeah, we have a nice looking glow on here. Now what we
[14:44] can do is we can take a merge node and plus it onto the original. So we switch this to a plus,
[14:50] and we have a glow on our explosion. So this is a pretty basic glow, but we start to see the idea
[14:56] coming into play here. Now you see at the start, it's pretty bad. It's like if we go a few frames
[15:03] back, it just gets like a very like a circle almost. And this is where you had to start doing a lot
[15:08] of manual key framing on your explosions to get them to look good, to get a little bit more of a
[15:14] natural camera glow. If we look at the one that I did, this is essentially what I did. I stacked
[15:20] a few glows together to essentially create a more natural, essentially glow around this. We don't
[15:26] want it to be too much of a ball around it. And usually there's a broader glow that's softer. So
[15:31] usually at least two or three glows is what you're going to need, even when you're using exponential
[15:35] glow. Now there might be an exponential glow out there. People make their own nodes that glow
[15:41] differently, essentially. That might do a better job, but that's just what I had to do in this
[15:46] specific case. So when the values are very different explosions, it's pretty common. So like for example,
[15:52] on this frame completely blows out. So what you would have to do to fix this is put a grade
[15:56] node just before the glow and just we'll just bring it down. So we can bring it down to somewhere
[16:00] like here and set a key frame by hitting right click and hit set key. And then we can just go
[16:05] forward in time and then okay, there's no more glow. So we just bring it back up. And essentially,
[16:10] we just do that and try not to make it look, you know, there's no frame that's basically
[16:16] like a broken glow almost, which can definitely happen. So I'll bring this down even more.
[16:21] We could expect definitely more glow on this frame, for example, where it's like really just
[16:25] exploding. If it was a real life camera, and we want to be really picky, we could look at some
[16:30] real reference and things like that. I would go check out the reference of, I believe it is
[16:36] Oppenheimer and but not the actual film itself, look at the behind the scene footage of how they
[16:42] filmed the explosions. You can see some pretty cool gasoline explosions in those examples.
[16:47] So I'll close all this. And we'll do another glow and then we'll just make this one have a higher
[16:52] spread, maybe we'll blur it, and then we'll bring the brightness like way down. So we have like a
[16:56] broad glow and we have a little bit of tighter glow and we can add that on top. Maybe that's a
[17:01] little bit too much. So we'll just again, key frame it manually. And then we'll just kind of play
[17:07] through. So like I said, if this was, if we were doing this for a specific light condition, I would
[17:14] go straight to reference even for the glows. I still go to reference all time to think that
[17:20] you can memorize exactly how things look in real life. I don't think it's a good idea. I think
[17:23] you should always look at reference, at least the first time you're doing it. And then once you get
[17:27] the look locked in, you can pretty much just match what you did. That's typically how I like to do
[17:32] it. So we can go back a few frames like here is getting a little bit too much again on the broad
[17:36] glow. So we can bring that down. And the original glow, it could be good. I think it's, I think it's
[17:43] not too far off. So that's kind of the base glow that we got here. One other thing that we can do
[17:49] is if you need to, you can play with the exposure right away. So right here, it starts to get dark
[17:56] pretty quickly. So basically what I did in this comp, I won't redo it completely just to make the


### Extra Details [18:00]
**Transcript (timestamped):**
[18:01] video not too long. If you want to go in this comp and look at it, you can check it out. But
[18:05] essentially what I did was I targeted the highlights and just made them a tiny bit brighter.
[18:11] First of all, so we take the same technique we just did, we do a key or node, and then we just use
[18:16] a grade node plugged into the mask. And then you can just bring it up and down. So it's only hitting
[18:20] the highlights. And a few other adjustments make it less red. But the real adjustment here that's
[18:26] interesting is that if you want to keep it hotter at the beginning, we're only in the emission layer
[18:31] here. But if we target essentially the shadow areas, even though the whole thing is pretty bright,
[18:37] we take the key or node and target shadow areas by hitting invert. And we can play with the range
[18:42] there to really target those shadow regions. Essentially what I did was brighten them up a
[18:48] tiny bit. Because usually when an explosion is happening, it's almost white, you're losing
[18:53] all the detail, we're not seeing all the cloud detail right away. And a lot of times you want to
[18:57] actually just lift those blacks a little bit. So that's one thing you can do is just target those
[19:02] regions. And we can get something like this. And now this is something that you can keyframe off.
[19:08] So again, here's our high, our shadows are targeted, I blurred it a tiny bit, just so you get the whole
[19:13] region. And then I have this keyframed grade with RGBA. And as it goes on, we basically fade it off.
[19:21] So the grade is going to turn off over time. So that's a little bit more intermediate. If you're
[19:26] a beginner, that might be a little bit too far for you. But I just wanted to show you guys,
[19:29] and you can sit there and kind of check it out if you want. So you see the effect that it has,
[19:33] we start in a more kind of yellowish brighter thing. And then it's kind of fading off into the
[19:38] darker tones where we see a little bit more detail. And why we're doing that is because we're removing
[19:43] the detail towards the beginning. So if we go towards the end, we're keeping the detail lost
[19:48] for just a tiny bit longer. And you see that that's the effect here. So that is kind of what we got
[19:54] going on. We can compare to this one, you see how you see how right away we start seeing detail,
[20:00] like we have like very bright and then immediately we're starting to see like almost shadows already,
[20:06] it almost feels like electricity versus like this one feels like everything is still burning.
[20:10] And then like the fuel starts to go, we could adjust the timing of that as well. But doing
[20:15] explosions and glows like this, you can see it's a lot about timing and grading. It's not just about
[20:21] one frame making it look good, but you got to adjust across time. So that is essentially the
[20:26] two different ones we have here. So let's compare this one that I just did and the one I did earlier,
[20:30] which has a little bit more detail. And you can see just by grading the highlights as well,
[20:35] we get a little bit more detail in there. Now one thing I like to do with explosions as well,
[20:40] this is a little bit of a cheat, but we can do it. But I'm going to sharpen it basically. So we put
[20:45] a sharpen note. And what we can also do is a log to Lynn. So we put a log to Lynn node,
[20:50] we switch it to log space. And then we copy, and we put it back, basically right after,
[20:58] and we switch it to back to linear, and we have the sharpen in between. So that's usually sharpen
[21:03] needs to go in between these two nodes. I won't go into the details of it right now, but just
[21:07] basically always do that, you'll be fine. It'll just sharpen it in a better way. So if I zoom in,
[21:14] sharpening explosions, pretty awesome technique just always works. Even when you have like pretty
[21:18] detailed explosions, you just get awesome looking stuff in there. So if you want to make your stuff
[21:23] look good, sharpening your explosions, I would recommend it. I think it's pretty cool. So that's
[21:29] about it for this tutorial. If you guys like it, make sure to hit the like button. I know this is
[21:34] more beginner slash intermediate, different levels there for different people. But I think it'll be
[21:39] useful for everybody and you get the free asset that you can use in your project. So hopefully
[21:43] that'll be good for you guys. And if you want, check out the After Effects to new course if you're


### After Effects to Nuke Masterclass [21:46]
**Transcript (timestamped):**
[21:48] new and downloading these for the first time. That's about it. Thanks guys.



---

## Captured Frames

- [2:16] tutorials/frames/compositing-with-exr-files-free-vfx-explosions/frame_000.jpg
- [3:01] tutorials/frames/compositing-with-exr-files-free-vfx-explosions/frame_001.jpg
- [4:56] tutorials/frames/compositing-with-exr-files-free-vfx-explosions/frame_002.jpg
- [6:04] tutorials/frames/compositing-with-exr-files-free-vfx-explosions/frame_003.jpg
- [9:00] tutorials/frames/compositing-with-exr-files-free-vfx-explosions/frame_004.jpg
- [10:00] tutorials/frames/compositing-with-exr-files-free-vfx-explosions/frame_005.jpg
- [13:22] tutorials/frames/compositing-with-exr-files-free-vfx-explosions/frame_006.jpg
- [16:00] tutorials/frames/compositing-with-exr-files-free-vfx-explosions/frame_007.jpg
- [20:45] tutorials/frames/compositing-with-exr-files-free-vfx-explosions/frame_008.jpg

---

## Structured Notes

### Core Technique
Beginner/intermediate multi-pass EXR compositing: an ACES color workflow, `Shuffle`-splitting a multi-layer CG explosion render into its individual light passes (spotlights, ambient/no-map, emission, pyro volume light), regrading each pass independently, recombining with `plus` merges, then building a hand-tuned, keyframed glow (via `Keyer` → `Premult` → an exponential glow gizmo) plus exposure-driven shadow/highlight grading to sell the explosion's timing and camera-exposure feel.

### Summary
A free downloadable multi-layer EXR explosion render (four such explosions are provided as a lead magnet, alongside a linked "After Effects to Nuke" beginner masterclass) is used to teach multi-pass CG compositing from scratch. **ACES setup:** before anything else, the project's color management is switched from Nuke's default OCIO config to ACES (S key over the node graph → color settings → OCIO → ACES 1.2 or 1.3; the top-left readout should then show "sRGB (ACES)"). A live comparison of the same 8-bit, non-HDR phone footage loaded as both ACES and non-ACES demonstrates the practical payoff: pulling the gain down on non-ACES footage looks flat with no recoverable highlight detail, while the same operation under ACES reveals real detail in the highlights — attributed to ACES's built-in highlight tone-mapping math, which matters especially for something as highlight-heavy as an explosion. **Reading the multi-layer EXR:** a `Read` node loads the EXR sequence; its Channels tab reveals the render is not a simple RGBA image but a multi-pass CG output containing many separately-stored light layers (visible file size is large because of all this extra high-dynamic-range data packed into single frames) — named layers observed include Spotlight (Side A / Side B), a "NoMap"-style ambient/overall light layer, an Emission layer (the fire/burning-fuel light itself), and a Pyro Volume Light layer. **Breaking out and recombining layers:** a `Shuffle` node is used per layer to pull that layer's data into the main RGBA stream Nuke actually composites in (layers themselves aren't directly editable in place — Shuffle routes a chosen layer's channels into RGBA where grading tools operate); one Shuffle is set up per light layer needed (Spotlight A, Spotlight B, ambient/ombient NoMap, Emission, and later Pyro Volume Light once it's noticed the recombined result doesn't exactly match the original beauty without it). These shuffled streams are recombined with `Merge` nodes set to **plus** (light passes are additive, never any other merge operation) with each Merge's inputs swapped (Shift+X) so the convention is consistently "A over B," visually organized with corner-pinned/staggered node placement so the stack reads like layered Photoshop layers. The recombined result is checked against the original beauty render by wiring both into a Viewer and toggling input 1 vs. input 2 — confirming a pixel-accurate match validates that the layer breakdown is complete and correct before any creative grading begins. **Per-layer grading:** with the recombination validated, a `Grade` node inserted into any individual Shuffle stream (e.g. brightening just the right-side spotlight, or the Emission layer specifically) lets that one light/element be pushed independently of the rest — demonstrated by toggling a Grade on/off while viewing the final composited output, and by pushing the Emission grade to zero to isolate what the (here, unused/disabled) Pyro Volume Light layer alone contributes. This same per-layer isolation is used for basic hue correction — pulling red out of just the Emission layer's color wheel to shift an overly-red explosion toward a more natural orange. **Exposure/realism framing:** the video explicitly ties glow/detail-visibility decisions to photographic exposure theory — an explosion this bright, shot at an exposure where a nearby person's skin detail is still visible, would in reality read as near-pure white with almost no internal detail; the comp is deliberately built "slightly exposed into" the explosion so some internal cloud/fire detail remains visible while still reading as extremely bright, rather than either full white-out or an unrealistically detailed/dim result. **Building the glow:** a `Keyer` node isolates the brightest highlight regions (its A/B range sliders define the selected brightness band); because the ACES/HDR data goes well above the normal 0-1 range (sampled highlight values around 2-8), the B threshold has to be raised well past 1 using the up-arrow key to actually target only the true highlights rather than the whole normalized 0-1 range. The keyed alpha is applied to the color via `Premult`, then fed into a custom **exponential glow** gizmo (bundled with the provided project file) for the actual bloom, merged back onto the base image with `plus`. A single glow pass looks unnatural on its own (described as collapsing into a flat "circle" on some frames) — the recommended fix is stacking at least two or three glow passes with different characteristics (e.g. one broader/softer + blurred + dimmer, one tighter/hotter), each independently `plus`-merged in, rather than relying on one generic glow setup. Because explosion brightness varies wildly frame to frame, glow strength is manually keyframed throughout the shot: a `Grade` node placed just before a glow pass, with its gain animated down on over-bright frames (right-click → Set Key) and back up elsewhere, prevents any single frame from "blowing out" into a broken-looking glow — with an explicit recommendation to study real reference footage (e.g. behind-the-scenes footage of the practical gasoline explosions used in Oppenheimer) when trying to match a specific real-world light condition, then lock in the look from that reference rather than relying on memory. **Shadow-region highlight fading:** a more intermediate technique layers a second `Keyer`, this time **inverted** to target shadow/darker regions instead of highlights, slightly brightening (lifting blacks in) those areas early in the explosion's life so cloud/smoke detail isn't fully lost in the initial near-white flash — this shadow-lift Grade is blurred slightly (to avoid a hard-edged mask) and animated to fade out over time via keyframed RGBA values, so the shot reads brighter/more detailed at the very start and gradually settles into the deeper, more contrasted "burning" look as the explosion progresses — explicitly framed as being as much about grading-over-time/timing as any single-frame look. **Finishing polish — the "always sharpen explosions" trick:** a `Sharpen` node is wrapped between a `LogToLin` (switched to log space) going in and a second `LogToLin` switched back to linear coming out — sharpening explicitly needs to happen in log space between these two conversion nodes for a better-quality result — described as a small, near-universally-applicable trick that reliably improves the look of CG explosion renders.

### Key Steps
1. Switch the Nuke project's color management to ACES: press S over empty node-graph space (or open project Color Settings), set OCIO config to ACES 1.2 or 1.3; confirm the viewer readout shows "sRGB (ACES)."
2. Load the multi-layer EXR sequence with a `Read` node; open its Channels/layers tab to inventory every stored pass (e.g. Spotlight Side A/B, ambient "NoMap" light, Emission, Pyro Volume Light) beyond the default RGBA.
3. For each light layer needed in the comp, add a `Shuffle` node routing that layer's data into RGBA so it can be graded with normal 2D tools.
4. Recombine all shuffled layers with `Merge` nodes set to **plus** (additive — the correct operation for light passes), consistently swapping inputs (Shift+X) so the convention is A-over-B throughout; organize nodes visually (e.g. corner-pin staggering) to read as a clear layer stack.
5. Validate the recombination by wiring both the original beauty Read and the recombined Merge stack into a Viewer, toggling between input 1/2 (keyboard 1 and 2) to confirm a pixel-accurate match before any grading — if a mismatch is found, identify and add the missing layer (e.g. Pyro Volume Light) via another Shuffle.
6. Insert a `Grade` node into any individual shuffled layer's stream to adjust that light/element independently (brightness, color) without affecting the others — toggle the Grade on/off while viewing the final merged output to judge the isolated contribution.
7. Correct base color (e.g. de-red an overly-warm explosion toward natural orange) by grading directly on the Emission layer's stream rather than the combined image.
8. Decide the comp's exposure philosophy up front: aim for the explosion to read "slightly exposed into" — extremely bright but retaining some internal detail — rather than either a flat white blowout or an unrealistically fully-detailed result, informed by how real cameras handle exposure against very bright light sources.
9. Build a glow pass: `Keyer` to isolate highlights (raise the B threshold well above 1 for ACES/HDR data, since true highlight values can reach 2-8+), `Premult` to combine the keyed alpha with color, feed into an exponential-glow gizmo, `plus`-merge back onto the base image.
10. Stack at least 2-3 differently-tuned glow passes (varying spread/blur/brightness) rather than relying on a single glow setup, since one flat glow pass tends to look unnatural (a plain "circle") on many frames.
11. Tame frame-to-frame glow blowouts by placing a `Grade` before each glow pass and keyframing its gain down on overly bright frames (right-click → Set Key) and back up elsewhere, checking against real reference footage of similar practical explosions when trying to match a specific look.
12. For intermediate shadow-detail control: add a second, inverted `Keyer` targeting shadow regions, lightly brighten/lift them with a blurred, keyframed `Grade` (RGBA animated to fade out over time) so early frames show more retained detail that gradually gives way to a deeper, more contrasted look as the explosion progresses.
13. Finish with the log-space sharpen trick: `LogToLin` (to log) → `Sharpen` → `LogToLin` (back to linear) — apply this to CG explosion renders as a near-default final polish step.

### Nodes / Tools / Settings
- **Color management:** OCIO project Color Settings → ACES 1.2/1.3 config
- **Core Nuke:** `Read` (multi-layer EXR, Channels tab to inspect stored passes), `Shuffle` (layer-to-RGBA routing, one per light pass), `Merge` (plus/additive for light-pass recombination, A-over-B input convention via Shift+X), `Grade` (per-layer independent color/brightness correction, glow-gain keyframing, shadow-region lift), `Keyer` (highlight isolation via A/B range, inverted for shadow-region isolation; B threshold pushed above 1 for HDR/ACES data), `Premult` (combining a keyed alpha with color before glow), `Sharpen` (wrapped between `LogToLin` in/out nodes for log-space sharpening)
- **Gizmo:** a custom exponential glow node (bundled with the provided project file, not a stock Nuke node)
- **Render passes leveraged:** Spotlight Side A / Side B, ambient/"NoMap" overall light, Emission (fire/fuel light), Pyro Volume Light
- **Cross-referenced resource:** the channel's free "After Effects to Nuke" beginner masterclass (companion course for viewers new to Nuke)

### Difficulty
Beginner to Intermediate — the core multi-pass Shuffle/Merge/Grade workflow and ACES setup are pitched at true beginners; the inverted-shadow-Keyer fade-over-time technique is explicitly flagged mid-video as "a little bit more intermediate" and optional for newer viewers.

### Foundry App & Version
Nuke. Version not stated numerically on screen; UI is consistent with the modern node-graph/3D-system era seen elsewhere in this batch.

### Tags
compositing, channels, grading, aovs, gizmo, fx-simulation, color-management, beginner, intermediate

---

## Related Tutorials
- Shuffle and Channel Management | Nuke Compositing [Beginner/Intermediate] (`shuffle-and-channel-management-nuke-compositing-beginner-intermediate.md`) — directly relevant: covers the Shuffle/layer/AOV fundamentals this tutorial builds on for splitting and recombining a multi-pass render.
- The BLUEPRINT for Cinematic Light (VFX) (`the-blueprint-for-cinematic-light-vfx.md`) — shares the position-pass-driven procedural noise and Cryptomatte-based light-pass isolation/boosting techniques, applied to selling directional light rather than assembling a full multi-pass beauty.
- How to use NUKE to Composite Blender Renders (`how-to-use-nuke-to-composite-blender-renders.md`) — shares multi-pass AOV recombination and Cryptomatte-masking fundamentals from a different cross-app CG-compositing pipeline.
