---
title: Can I Create a Speeder Chase on a TINY Greenscreen?
source: YouTube
url: https://www.youtube.com/watch?v=KLNmQtwj5Pc
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/can-i-create-a-speeder-chase-on-a-tiny-greenscreen/
frame_count: 0
frame_status: pending-selection
---

# Can I Create a Speeder Chase on a TINY Greenscreen?

**Source:** [YouTube](https://www.youtube.com/watch?v=KLNmQtwj5Pc)
**Author:** Compositing Academy
**Duration:** 9m48s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py can-i-create-a-speeder-chase-on-a-tiny-greenscreen <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In this video, we're traveling to one of the most insane volcanoes on Earth to film a sci-fi sequence.
[0:05] Can an independent artist and a small team pull off Hollywood-level visual effects on not just one shot, but an entire sequence?
[0:12] I've always wanted to make a project like this, and I figure no one's gonna give me the chance unless I just do it myself.
[0:17] And maybe if I show that's possible, others can do it too.
[0:20] I'm gonna be using Blender and Nuke together to find out.
[0:24] My name's Alex Hanaman.
[0:25] In the last decade, I've been working on feature films on some of the top studios like Weta Digital, ILM, and Sony Pictures.
[0:31] On films like Avengers, Star Wars, Spider-Verse, and a bunch of other movies.
[0:35] But in the last few years, I've been showing how to use Nuke and Blender together to be able to create projects from end to end.
[0:42] For the first time in history, I think the tools and technology are so readily available at a low enough cost that anyone can tell their own stories.
[0:50] And in this video, we're not just saying it, we're going all in to try to prove it.
[0:55] This will be weeks of work hiring other artists and flying to another country before a single shot even exists.
[1:01] And even worse, if I fail, maybe it proves the studio's right that the work only belongs within the Hollywood studios,
[1:07] and that Blender is just a hobbyist tool.
[1:09] Challenge accepted.
[1:12] So a few months ago, we packed our bags and flew all the way to Iceland to film a variety of projects for this YouTube channel.
[1:18] No sci-fi sequence starts in a boring location.
[1:26] We walked the landscape until we finally reached the volcano.
[1:29] This is in Green Deveak Iceland.
[1:31] Volcano in Icelandic is pronounced...
[1:42] This volcano has miles of black lava rock terrain.
[1:45] This massive volcano is still active, erupting multiple times per year.
[1:49] There are active steam vents coming out of the lava, and the entire volcano smells like rotten eggs.
[1:55] My goal here is to find the most interesting patterns that I can 3D scan with my drone.
[1:59] As I fired up the drone, I had one thing in mind.
[2:01] I'm not just trying to capture a few rocks.
[2:03] To make a full scene, I need to capture entire portions of this terrain.
[2:07] The original idea was based on this very rough sketch of a character sitting on something, some kind of vehicle, and an explosion behind.
[2:14] So there's going to be a chase scene, and that means we're going to travel a long distance, and we can't scan that all at once.
[2:19] So I begin to fly my drone in orbiting patterns, trying to capture every angle of the terrain that I can.
[2:24] We can't miss a single piece here, otherwise we'll have holes.
[2:27] Also, I'm scanning in sections, so that I'll recombine these later in Blender.
[2:30] Now, I did run into one big problem.
[2:32] As soon as I get back to my computer, there are just thousands of images, and you don't know which go together.
[2:37] It's as if someone dropped a thousand pictures on your desk and says,
[2:40] reassemble these in each section where you photographed them.
[2:43] So I knew the drone took pictures on a one-second timer while I was shooting this,
[2:47] so I thought maybe if I can find the gaps in the time that are longer than one second, I can separate the pieces,
[2:52] and once they're separate, each section that I scanned will create a model.
[2:55] And finally, I head back my first results.
[2:58] I didn't just bring back a piece of real volcano, but a perfect digital representation of it.
[3:03] And out came this incredibly detailed model with millions of polygons and extremely high resolution textures.
[3:10] It can even get close to the ground for closer upshots, which is what we need for a photo-reel sequence.
[3:16] With these insane assets, I can build a world that I have full control over placement, lighting, and camera composition.
[3:21] As we continue around Iso, to capture some of the best footage and assets from one of the most cinematic places on Earth,
[3:27] I even scanned entire mountain ranges for map painting, as well as 360 images of cinematic skies, which we can use to light our 3D scene.
[3:34] But this was only the beginning.
[3:36] The thing about scanning an empty environment is all we have is the most epic empty landscape.
[3:41] No characters, no story, nothing to chase or run from.
[3:44] And so this second part of the build was going to become the most difficult part of this entire project.
[3:49] So I found this crazy mask, which is what the writer is going to wear.
[3:52] If Mad Max and The Mandalorian had a baby, this is probably what the project is going to look like.
[3:56] So all I had was a sketch of a vehicle, and we can't build the real vehicle like they would on a real movie, because that would blow our budget.
[4:02] So we got to think outside the box a little bit.
[4:04] So we came up with this.
[4:05] Yes, this is literally just bicycle parts attached to a broomstick.
[4:08] So we might be lacking the industrial part from industrial light and magic here.
[4:12] We might only have just a green screen on a garage and a few bicycle parts, but maybe with a few more helping hand specialists,
[4:19] we can build something greater than the sum of its parts.
[4:21] So I sent the 3D scan of my actor to a hard surface modeler slash concept artist.
[4:25] He's going to model the vehicle to the exact dimensions of the actor.
[4:28] Next I need these handlebars actually removed from the footage.
[4:31] I'm also going to remove the side of the jacket and replace it with a CG one to make it look like there's even stronger wind that we could get.
[4:38] Lastly, there's 10 shots to be tracked, so we're going to send this to a matchmaking team and also track the hands which will stick to the CG vehicle.
[4:44] Now let's see what we get back.
[4:46] First we get back our paintwork.
[4:48] This is invisible visual effects.
[4:50] Now we'll be able to put our CG vehicle and attach them to the hands.
[4:54] While they were painting that, I 3D scanned the real jacket, which looks windier and I can attach it after.
[4:59] We'll check that out in the final composite.
[5:01] Next I received the camera tracks and the tracking of the actor, and last but not least, the rider's vehicle.
[5:06] The whole project hinges on this looking amazing, so I had my fingers crossed.
[5:22] Anton fucking slayed it on this model, perfectly modeled to our 3D scan of our actor,
[5:27] and textured in detail from every angle.
[5:30] Now that we have all these insane pieces, we just need to bring it together.
[5:33] I did a simple rig on the vehicle, which allows the vehicle's handlebars to move with the actor.
[5:38] Grabbing the tracking data, I connect the hands and the footage all together.
[5:42] Next I move into camera animation, pre-visualizing some of the shots.
[5:48] The last big piece of the story is still missing, the antagonist.
[5:51] I wanted to have a monolithic ship like a rival or a doom,
[5:54] so Anton went through a few different designs and we settled on this.
[5:59] Now that all of the assets are ready, we can begin the third and final phase, the detailing phase.
[6:04] A few years ago I watched a documentary and they were talking about how when sulfur burns, it creates blue flames.
[6:10] So I've always been inspired by this idea of blue flames mixed with blue lava,
[6:14] and so I'm going to integrate that into this project.
[6:17] Here I'm using the cavity maps from the models I generated to create lava in the cracks,
[6:21] and I created some lava shaders and blender which I can mix into the terrain.
[6:24] I also did my map painting in nuke, and started to paint and sculpt some models as well.
[6:29] Here I'm using substance painter to create some geysers,
[6:31] and I'm using comfy UI to generate some background assets that I can blend into my terrain.
[6:35] This can give us some interesting silhouettes and different forms that we couldn't have scanned otherwise.
[6:39] I'm projecting my Iceland photography back onto these models to actually get these to blend better into the scans that I captured.
[6:46] Here we can see before and after.
[6:47] I'm doing the same process here to create this crater, but using a multi-camera projection setup to blend.
[6:52] Now the next thing we can do is actually blend this into the terrain.
[6:54] You don't want to have hard edges, so I created a variety of different tools for this project,
[6:58] but one of them was to convert terrains into projections, and now I can blend assets easily.
[7:03] But no interesting scene is completely static.
[7:06] To make this interesting, we need to get elements.
[7:09] So I hired multiple effects artists to get things like geyser smoke,
[7:12] or dust explosions when there are bullet impacts,
[7:15] as well as debris and rocks and different variations of elements that we can add to make it interesting.
[7:20] I'm also using some past elements we created, such as these explosive sparks,
[7:24] which comes with nuke templates to make it look cool.
[7:26] And I created some laser blast tools that's in nuke as well.
[7:29] The last few elements I handle myself, such as sparks and blender,
[7:32] or creating some interactive smoke and ember gin.
[7:34] Here I'm also adding some lava textures that are animated using comfy UI.
[7:38] I'm projecting these onto the 3D terrain in Blender, which I can blend perfectly in nuke.
[7:43] This is how we can make it integrate well.
[7:44] Compositors are masters at layering atmosphere, which is what gives that cinematic look to shots.
[7:49] And I needed to create one more tool.
[7:51] This is the Compositing Academy Relight tool, which has self-shadowing.
[7:54] It's the best relighting tool out there, and we can use it to integrate our character driving past these blue light sources.
[8:00] Here we can see the layering of the composite of all the decisions we made along the entire way.
[8:07] And so it all started with a crazy idea.
[8:09] Now we can look at the result and ask the question,
[8:11] is a Blender Nuke combination just for hobbyists?
[8:37] So guys, that's the Ryder.
[8:38] Make sure to hit thumbs up and comment if you like this, so we can keep making more stuff.
[8:42] So I want to mention that this project is actually an expansion of all the projects we've been doing in the past.
[8:46] It's a concept I've been thinking about for a while.
[8:48] If you look at one of the top films this summer at the back rooms, it was directed by Cain Parsons,
[8:52] who was messing around on Blender, making short films on YouTube,
[8:55] and he was able to direct a film using those skills.
[8:57] But the thing is, to actually get projects from end to end, you need at least five disciplines.
[9:02] Shooting, VFX supervision, 3D lighting, and compositing.
[9:05] So instead of being a siloed off specialist, I see this as a new type of generalist that is forming,
[9:10] and I'm calling it the full stack filmmaker framework.
[9:13] So it doesn't just require these skills to pull it off, it also requires tools and infrastructure.
[9:17] I saw a lot of tools and infrastructure in the studio, so I've been adapting those concepts into a smaller format
[9:22] that independence and small teams can pick up.
[9:25] There's a difference between brute forcing through one VFX shot
[9:28] and doing a scalable system that you can actually grow and direct entire sequences.
[9:33] So this whole framework, the skills, the pipeline, the tools, and the assets that were in this project
[9:38] are going to be included in this new course.
[9:40] It's available for pre-order now if you check the link in the description.
[9:43] If you want to bring projects end to end, this is for you.
[9:46] That's about it guys, and thanks for watching.



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
