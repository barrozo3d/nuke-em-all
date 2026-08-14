---
title: Nobody’s Ever Made VFX This Way (New Tech)
source: YouTube
url: https://www.youtube.com/watch?v=3d9ycMKf65U
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke (mentioned only — final compositing pass not shown on screen)"
version: "not specified"
tags: [virtual-production, compositing, camera-tracking, gaussian-splats, digital-matte-painting, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/nobodys-ever-made-vfx-this-way-new-tech/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Nobody’s Ever Made VFX This Way (New Tech)

**Source:** [YouTube](https://www.youtube.com/watch?v=3d9ycMKf65U)
**Author:** Compositing Academy
**Duration:** 9m50s | 11 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] In this video we've flown all the way to Iceland to film a CG dragon in a cave using a brand new workflow with a app called Lightcraft Jet Set.
[0:07] We'll capture the CG character in real time.
[0:09] So this technology is going to allow directors, cinematographers, and visual effects pre-vis teams to actually get shots that you would never be able to do otherwise.
[0:17] So you can film your CG as you're in the location.
[0:20] And what better place in the world to film this project than in Iceland?
[0:24] By combining real uncontrolled physical locations with mixed reality virtual production technology,
[0:30] I want to prove that you can create an insane result without millions of dollars where a giant VFX studio behind you.
[0:37] I believe if you assemble the right team of artists and filmmakers and use the right technology,
[0:42] that it's possible to create a result that rivals the large studios and we don't have to wait for the permission slip.
[0:48] Our destination is a place called Yoda Cave.
[0:51] And as Yoda would say, do or do not, there is no try.
[0:54] So if this works, this could change how visual effects scenes get made by not just large studios, but also small teams anywhere in the world.


### Virtual Production Misconceptions [1:00]
**Transcript (timestamped):**
[1:01] Now without a production crew and a giant budget, it's not going to be easy.
[1:05] Sometimes when people hear the term virtual production, they think of LED stages because there's been a lot of marketing recently about that type of virtual production.
[1:12] Virtual production is not just on those stages.
[1:14] In a previous video on this channel, I showed Jet Set being used on green screen, which you can see your scene as you're filming.
[1:19] This is not the first time this has actually been done.
[1:21] James Cameron was using Simulcam even back on the original avatar.
[1:25] Big difference between normal visual effects workflows and virtual production is framing up to what you're expecting to see.
[1:31] He was using this to see CG characters mixed with real characters or CG set extensions.
[1:36] The system was large and not a consumer product and relied on external tracking.
[1:40] Jet Set is a portable system, but this also means we can take it off the green screen stage into uncontrolled environments.
[1:47] So all we need now is our CG character.


### Finding the Dragon EyeCandyXYZ [1:50]
**Transcript (timestamped):**
[1:54] I needed to find the key ingredient in this project and I knew it would make or break the shot.
[1:59] That's when I found the dragon.
[2:03] This super high resolution sculpt with textures comes from iCandy XYZ.
[2:08] One of my favorite things about filmmaking is teaming up with other artists of different skill sets.
[2:13] They produce hero level assets with incredible quality.
[2:16] As soon as I saw their portfolio, I knew immediately that this was going to be perfect.
[2:21] On top of this, the dragon comes fully rigged and ready for animation.
[2:25] If you want to see what other VFX assets they're cooking up in the future, click the link in the description below.
[2:29] While starting this project, there's an immediate big hurdle that we're going to run into.
[2:33] In a normal VFX workflow, we would go and scan the scene, we would film the empty scene, and then we would add our virtual characters or objects later.
[2:41] This virtual production workflow actually changes the order a little bit.


### Mixed Reality Virtual Production [2:43]
**Transcript (timestamped):**
[2:44] In this Jet Set workflow, we want to switch the filming and animation around so we have the character animated before we film.
[2:50] That way we can see what we're filming.
[2:52] Problem is, we won't have to scan before we fly to Iceland.
[2:55] I don't want the animation done in an empty scene.
[2:57] I want the dragon to interact with the terrain.
[2:59] So if I don't figure out a way to give him the missing model, this entire project could fail.


### Finding the missing Cave [3:04]
**Transcript (timestamped):**
[3:04] Now one thing I discovered about this specific location is there's been a lot of tourists.
[3:10] And those tourists, they take a lot of videos.
[3:13] So if I get enough pictures from the internet and they cover enough angles, maybe I can create a model.
[3:18] So I exported a ton of pictures and threw them into a photogrammetry software.
[3:29] I was lucky enough that these videos had enough motion.
[3:32] I could not believe this actually worked.
[3:34] Next I found my animator, Martin Lays, who's a killer at animating creatures.
[3:37] So still a little paranoid on the accuracy of the cave I generated.
[3:40] It's enough to get the animator started, but I still want to get somebody out there before I get there to scan the cave, even if it's a rough scan.
[3:46] Luckily one of the co-founders in Lightcraft, our sponsor, had some family out in Iceland and was able to get somebody out there and get the measurements we needed.
[3:53] Now that the animation was complete, I still needed this to run in real time on my phone.


### Testing Jetset [3:56]
**Transcript (timestamped):**
[3:57] Taking our hero asset, which has millions of polygons, I created a proxy mesh.
[4:01] This is lightweight, it runs instantly on a phone.
[4:03] So I got the dragon loaded up on my phone.
[4:05] On the real location, we're not going to be filming with the iPhone.
[4:09] We're going to be filming with the Sony FX3.
[4:11] So this is just for tracking and seeing our CG.
[4:14] So I'm just using the free version of Jet Set right now, which by the way, you can download for free in the description below in this video.
[4:19] And I can play the animation back and frame up to the character.
[4:23] Now this is all good for a tech demo, but can we do it for real in production?


### Traveling to Iceland [4:28]
**Transcript (timestamped):**
[4:31] So with all the film gear set in the car, we're ready to start the journey.
[4:37] We set off across Iceland's otherworldly landscape with one mission in mind.
[4:41] But as we followed the southern coastline, a single question began to take over.
[4:44] Is this even going to work?
[4:46] As we get closer to the cave, the project now turns from an idea to something I need to prove as possible.
[4:51] Now filming in Iceland, we do have one factor that plays into our favor.
[4:55] The Iceland Midnight Sun.
[4:57] In Iceland during the summer, the sun doesn't fully set.
[5:00] It gives you a longer blue hour for better lighting and filming.
[5:03] Now on the other hand, we do have some things that are going to play against us.
[5:06] The weather in Iceland is very unpredictable and you can have strong wind and heavy storms.
[5:11] This can cause delays in filming and we have to protect the gear.
[5:14] But if you time it right, you can get a very cinematic look.
[5:17] But even when you plan extensively, things still go wrong.
[5:20] I had blocked out some time where we would be in this region filming in Yodaké.
[5:24] Turns out that another director was filming in this location and reserved the entire park.
[5:29] Christopher Nolan was filming the Odyssey so we lost a bunch of days on where we were supposed to film.
[5:34] And then our car decided to break down because we were charging some gear and it basically killed the battery.
[5:40] This means we lose another day and a half.
[5:42] So really we have one shot to make this work.
[5:52] Now the only day this week it wasn't raining, we arrived at the cave with one more surprise.
[6:00] Driving all the way there and then seeing this sign felt like the final nail in the coffin.
[6:07] But we decided maybe the people would leave past midnight, it was just for the day.
[6:11] And we can just film super late and make it happen.
[6:13] The people actually did leave.
[6:15] We had an opportunity and still the blue hours there can make it happen.


### Starting Production [6:18]
**Transcript (timestamped):**
[6:19] Alright, we're going to film the dragon.
[6:22] The streets empty.
[6:24] We got a bit of light so hopefully everything goes well.
[6:29] It could do it. It's a bit dark.
[6:41] Also the other factor which is there's rain coming from the ceiling so we got to be a little bit careful.
[6:50] So after looking around the location I had a few camera tests to see the lighting and just to get a sense of the angles.


### XGRIDS Lidar Scanning [6:54]
**Transcript (timestamped):**
[6:56] Now before filming I do some onset data capture such as HDRI and scanning.
[7:01] This time I'm using an X-Grid's LiDAR scanner.
[7:03] This gives us an extremely precise model of the interior of the cave and it's a handheld solution.
[7:09] So I can walk around and get every angle I need as I walk the location a dense point cloud forms around me so I can see where I've scanned.
[7:16] What this gives you is a very dense point cloud which you can generate a mesh from.
[7:19] Or you can get a Gaussian splat so you can take measurements and see exactly where it was.
[7:23] This extremely detailed mesh can be used to refine the tracks that we get automatically on set from the iPhone.
[7:29] This can dramatically speed up the process by using this with a virtual production workflow.
[7:33] You can also use this for detailed lighting which will help when we integrate our CG character to the real footage.
[7:37] If you're interested in learning more about X-Grid's handheld LiDAR and Gaussian Spiting check out the link in the description.


### Using Lightcraft Jetset [7:42]
**Transcript (timestamped):**
[7:43] Now that we have this virtual scene on top of our real world scene we can film the dragon in action.
[7:48] After a quick lens calibration the iPhone is now tracking the FX3 and I can see the dragon overlaid on my FX3 footage.
[7:55] Now it's time to hit record and film the action.
[8:05] From each position I film in Jet Set saves the position of that camera.
[8:09] This means each virtual camera matches the real camera's location.
[8:13] This means when we do post production later the scene will already be set up with the real footage and the character already aligned.
[8:19] The real creative thing here is being able to react to the CG moving in front of you.
[8:23] After filming you'll have previous videos of all the clips of film so you can see which clips you actually want to light and composite.
[8:28] For each shot Jet Set creates a scene I can render out and the secret is to finalize your shots in nuke to bring it to that feature level quality.
[8:35] So let's check out the final result.


### Final Filmed Sequence [8:37]
**Transcript (timestamped):**
[9:14] To make sure to check out Jet Set for free in the description below if you have an iPhone.
[9:19] If you want to do the cine version which is connecting it to your cinema camera that's also available.
[9:23] This wasn't my first time working with this product and it's really an empowering tool to pull off sequences instead of just single shots.
[9:29] And if you want to learn the core skills that I used in this video which is based on nuke compositing I have a bunch of courses around that so if you're interested that's based on my experience working in the film industry for over 10 years at some of the large studios.
[9:40] That's about it guys make sure hit thumbs up if you want to keep seeing more videos and we have a bunch of other stuff we shot in Iceland as well so make sure to stay tuned.



---

## Captured Frames

- [2:03] tutorials/frames/nobodys-ever-made-vfx-this-way-new-tech/frame_000.jpg
- [4:03] tutorials/frames/nobodys-ever-made-vfx-this-way-new-tech/frame_001.jpg
- [7:03] tutorials/frames/nobodys-ever-made-vfx-this-way-new-tech/frame_002.jpg
- [7:48] tutorials/frames/nobodys-ever-made-vfx-this-way-new-tech/frame_003.jpg
- [8:37] tutorials/frames/nobodys-ever-made-vfx-this-way-new-tech/frame_004.jpg
- [9:00] tutorials/frames/nobodys-ever-made-vfx-this-way-new-tech/frame_005.jpg

---

## Structured Notes

### Core Technique
This is a behind-the-scenes pipeline case study, not a node-by-node Nuke tutorial: it documents an on-location virtual-production workflow (Lightcraft Jet Set real-time AR camera tracking + XGrids handheld LiDAR/Gaussian-splat scanning + photogrammetry) used to shoot a CG dragon composited into a real Icelandic cave, with Nuke named only as the final finishing/compositing step (not demonstrated on screen).

### Summary
Compositing Academy documents an end-to-end virtual-production shoot: a hero CG dragon asset (from iCandy XYZ, fully rigged) is paired with a photogrammetry reconstruction of a hard-to-access cave (built from tourist photos/videos found online, since the location couldn't be scanned in advance) so an animator could block the creature's interaction with terrain before ever visiting the site. A lightweight ~24,771-poly proxy mesh of the dragon runs in real time inside Lightcraft Jet Set (a portable, phone-based virtual-production/AR app — the free tier used here, paid "cine" tier available for cinema-camera rigs) so the crew can literally see and frame the CG character live through an iPhone while filming on a Sony FX3, with Jet Set recording each camera position so the virtual scene matches the real camera later in post. On location, an XGrids handheld LiDAR scanner is used to capture a dense point cloud / Gaussian splat of the actual cave interior for camera-track refinement and lighting reference. The video frames virtual production as broader than LED-volume stages (tracing the concept back to James Cameron's Simulcam on the original Avatar) and states, without demonstrating, that Nuke is where the final shots get compositing/finishing to reach feature-level quality.

### Key Steps
1. Source a high-quality rigged hero CG asset (here: a dragon from iCandy XYZ) before committing to a location-dependent shoot.
2. When the shoot location can't be scanned in advance, reconstruct a rough proxy model via photogrammetry from publicly available tourist photos/videos of the site, sufficient to let an animator block character-to-terrain interaction ahead of time.
3. Reverse the normal VFX shoot order for virtual production: animate the CG character first (in the reconstructed environment) so the crew has something concrete to frame and react to on set, rather than filming an empty plate and adding CG later.
4. Build a lightweight real-time proxy mesh (order of ~25K polys) from the high-resolution hero asset so it can run smoothly on a phone-based AR tracking app.
5. On location, use a portable phone-based virtual-production app (Lightcraft Jet Set) with a calibrated lens to track the primary camera (here, a Sony FX3) and overlay the CG character live in the viewfinder/monitor, letting the crew frame and direct against the actual CG performance in real time.
6. Jet Set records each camera position per take, so the corresponding virtual camera matches the real camera's position for post-production alignment.
7. Capture on-set reference data before/during filming: HDRI captures and a handheld LiDAR scan (XGrids scanner) producing a dense point cloud, refinable into either a mesh or a Gaussian splat, used both to refine on-set tracking data and as a detailed lighting reference for later CG integration.
8. Review Jet Set's saved preview clips per camera setup to choose which takes to actually light and composite.
9. Finish each selected shot in Nuke to bring it to feature-level quality (this step is stated but not shown on screen in this video).

### Nodes / Tools / Settings
- No Nuke nodes are shown on screen in this video — it is a pipeline/BTS documentary, not a node-graph tutorial.
- Lightcraft Jet Set — phone-based real-time AR virtual-production app; free tier (iPhone) and paid "cine" tier (connects to a cinema camera); records per-take camera position data for post alignment.
- XGrids handheld LiDAR scanner — captures dense point clouds on set; exportable as a mesh or a Gaussian splat; used for track refinement and lighting reference.
- Photogrammetry software (unnamed) — reconstructs a rough environment model from crowd-sourced tourist photos/video when the location can't be pre-scanned.
- Proxy mesh decimation — hero CG asset reduced to a lightweight (~25K poly) real-time stand-in for on-set AR tracking.

### Difficulty
Not applicable — this is a behind-the-scenes pipeline case study; no node-level Nuke compositing instruction is shown on screen (the video states Nuke is used to finish the shots but does not demonstrate it).

### Foundry App & Version
Nuke is named as the tool used to finalize/composite the shots to feature-level quality, but no Nuke UI, node graph, or version indicator appears on screen anywhere in this video — version not specified, and this entry should not be relied on for any concrete Nuke technique.

### Tags
virtual-production, compositing, camera-tracking, gaussian-splats, digital-matte-painting, intermediate

---

## Related Tutorials
First entry tagged `virtual-production`/`gaussian-splats` in the knowledge base — cross-reference against Nuke 17.0/17.1's native Gaussian Splat toolset (`references/release-notes-nuke-17.0.md`, `release-notes-nuke-17.1.md`) since the XGrids scanner shown here produces splat data that could plausibly feed a native Nuke splat pipeline on current versions, though that connection is not made in this video itself.
