---
title: Blender + Nuke | A.I Enhanced Digital Matte Painting Workflow
source: YouTube
url: https://www.youtube.com/watch?v=XG-5tchFBQM
author: Compositing Academy
ingested: 2026-08-17
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/blender-nuke-ai-enhanced-digital-matte-painting-workflow/
frame_count: 0
frame_status: pending-selection
---

# Blender + Nuke | A.I Enhanced Digital Matte Painting Workflow

**Source:** [YouTube](https://www.youtube.com/watch?v=XG-5tchFBQM)
**Author:** Compositing Academy
**Duration:** 13m36s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py blender-nuke-ai-enhanced-digital-matte-painting-workflow <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro and Explanation [0:00]
**Transcript (timestamped):**
[0:00] In this video, we're talking about new AI techniques and we're merging traditional VFX workflows
[0:17] with those techniques.
[0:18] We're going to go through a multi-step process to show how the digital map painting was done
[0:22] from rough blockout and rough sculpt all the way to lighting, temporary, and low res texture
[0:28] projection and then how we bring this into AI and use upscale techniques to enhance the
[0:33] look and actually get this detail much faster than doing it manually.
[0:37] Then we'll bake it down and project it on a remeshed geo in Nuke.
[0:40] Now you might be asking, why do we want to do this approach?
[0:43] What is the benefit?
[0:44] The benefit is to not have to make every single asset in a very cost-intensive way, right?
[0:49] So Quixel can solve some of this problem or if you do photo bashing, you know, you could
[0:52] take different models together and put them together, but you might not have full control
[0:56] over the composition.
[0:57] This is actually a middle ground between photo bashing and creating your own assets.


### VR Sculpt Blockout [1:01]
**Transcript (timestamped):**
[1:01] All right, guys, so if you haven't seen how this works, this is Adobe Substance Modeler
[1:06] and it's a VR modeling software.
[1:09] Essentially, how it works is you can move around, you can sculpt things in real time
[1:13] and everything's really fast.
[1:14] I did import this into centimeters, not meters because if you do meters, it does get a little
[1:19] bit slow, so you want to find a good resolution for the mesh.
[1:22] So when you import an OBJ, just play around with the scale there, depending on the size
[1:26] you're seeing, but essentially you can draw stuff around, you can subtract stuff.
[1:31] I won't do a whole breakdown of the software, but essentially this is what we're doing.
[1:35] Now I'm not going to sculpt all of the detail.
[1:37] The idea is that this workflow is supposed to be faster and the reason it is faster is
[1:41] because of this.
[1:42] So in this tool here, we have a clay and stuff like that, but there's one called stamps.
[1:47] And if you go to the stamps, they have some default ones called rocks.
[1:51] So you can grab one of these and basically just have some pretty decent rocks to start
[1:55] with.
[1:56] We're going to use AI to enhance this.
[1:58] So the reason we're doing this is because we want to catch light onto a base mesh.
[2:03] It doesn't have to be perfect mesh.
[2:04] We're not sculpting a rock, super, super detailed, like if we were going to do it to make a full
[2:09] on CG asset.
[2:11] What we're doing is we're just getting enough information so that the image to image AI is
[2:15] going to have light information to work with.
[2:17] So essentially we can take these stamps and just kind of like place them.
[2:20] And that's basically what I did.
[2:22] Some sculptor probably look at this and say like, this is like the wrong way to do it,
[2:26] but the end result I think speaks for itself, which after using the AI to kind of enhance
[2:30] the forms there.
[2:32] So essentially you can go around here, play around.
[2:35] And this is why the base mesh is useful because you can kind of use it as a reference guide.
[2:40] You can play around to scale here.
[2:42] You can go in there and erase the edges and do like a proper sculpt if you want to.
[2:46] So this is just also just really fun to play with if you like doing stuff like this, so
[2:51] you can smooth it out and different things like that.
[2:53] So you want to go around, place all the rocks.
[2:55] So I'll just show you the one that I did in a second here, but that's the base idea.
[2:59] So this is the scene that I did.
[3:01] I spent a few more minutes on it, maybe 10, 20 minutes just slapping it together.
[3:05] Again, we're not trying to create a super detailed sculpture where we go in and we carve every
[3:10] single crack because if you look at a real cliff, there's an immense amount of detail
[3:14] actually there.
[3:15] So we don't want to spend all the time.
[3:17] We're trying to create assets in an efficient way.
[3:19] So this is kind of like if you were in real life slapping a piece of clay together really
[3:23] really quick.
[3:24] Basically what this is, but the reason we're doing this versus having a flat geometry,
[3:28] which in older DMP workflows and if there's not a lot of parallax is still totally a legit
[3:33] workflow.
[3:34] You can do it that way, but the reason we're doing this is because the AI will see these
[3:39] different facing angles and the light we're going to light in blender.
[3:43] So it'll cast nicer shadows.
[3:45] So even if we remesh this later on, which we will do, which will reduce some of this
[3:50] parallax and geometry, we're still going to get a higher quality result by just doing
[3:55] a little bit more effort.
[3:56] And the idea with image image, I think that a lot of people might not get right away unless
[4:00] you play around with AI quite a lot is the closer you can get the result to what you
[4:05] want, meaning the lighting and the textures, the closer it is, the better result you're
[4:10] going to get.
[4:11] If you just give it a flat surface with nothing to cast shadows or no, no texture on the surface,
[4:16] it's not going to give you the result you want.
[4:18] So you still have to do some work here.
[4:19] And that's why I think it's an interesting tool in the workflow.
[4:22] So we'll go from this and then we'll go on to the next step.
[4:24] So this is the mesh after bringing it in from Modeler.


### Lighting + LowRes Texture [4:25]
**Transcript (timestamped):**
[4:27] So you can export it.
[4:28] You can also remesh it on the way out.
[4:31] And you can remesh in Blender as well.
[4:32] There's too many faces and things like that.
[4:35] So those are things to keep in mind.
[4:36] Modifier, for example, modifier, remesh, if you have a problem, you don't want a huge
[4:41] poly count because you want to bring this into Nuke after to project onto.
[4:44] And that's just something to keep in mind.
[4:46] So this is going to give us enough lighting information.
[4:48] I'm using EV right now.
[4:49] That's why you see it flickering as I'm rotating.
[4:51] But if I switch the cycles, we'll get a little bit better bounce lighting and the cracks
[4:54] and things like that as well.
[4:55] So that's the base model enough to get shadows and highlights.
[4:58] The next thing we want to do essentially is give it a base material.
[5:02] So we've already given it a base lighting.
[5:04] I've already done like a light setup.
[5:05] I don't think this was the exact light setup I put.
[5:07] I think I had moved these lights around a bit more, played with the shadows.
[5:10] I also go to cycles.
[5:12] I don't want to do it while I'm recording because it'll probably stutter my microphone
[5:16] as the GPU kind of kicks up there.
[5:18] So essentially you want to find a good lighting, good bounce lighting.
[5:21] But then we want to project rock texture.
[5:23] So that's going to give the AI a bit more to work with.
[5:25] Because if you give it this, maybe they'll think it's snow or something like that because
[5:30] it's just blue.
[5:31] It's flat.
[5:32] There's nothing there to tell it that this is rock under blue hour lighting.
[5:36] So if you project a basic material, and it doesn't have to look good.
[5:39] It just has to be there.
[5:40] So this is literally just a rock texture.
[5:42] I think I got it off blender kit, which is like a plugin that you can get assets.
[5:46] There's a free tier and there's a paid tier, things like 14 bucks a month or something.
[5:51] But you basically get a bunch of textures that you can search through.
[5:53] It's a bit similar to Quixel.
[5:55] So kind of like that.
[5:56] But just projecting it from view.
[5:58] So essentially what you want to do, because this thing doesn't have UVs.
[6:01] You basically just go into edit mode.
[6:03] You can hit A and then you can hit U and then say project from view.
[6:07] That's one way to do it.
[6:08] I think this material, the way that it comes is actually using world coordinates and mapping
[6:13] it, not even using the UVs, the specific one from that asset store.
[6:17] But if you don't have it, just project from view any texture.
[6:19] It's going to work.
[6:20] Now we don't care that there's a bunch of repeating materials here like tiling.
[6:26] If you were doing this the right way, you have to spend a lot of time painting this
[6:30] material to get the scale to look realistic.
[6:34] Following the cracks and all of those things.
[6:35] You probably have to bring it into substance painter or something like that.
[6:39] So we're avoiding all of those steps by doing this.
[6:42] We're just giving enough detail that, hey, this is clearly rock and this is going to
[6:46] work with the AI.
[6:47] So next I'm going to show you how to get this image out and get it into either CREA AI,
[6:52] which is what we're using.
[6:54] Or we're going to use a Magnific AI, which is an alternative.
[6:58] Both work really well.
[6:59] So they do a little bit of different things, different offer there.
[7:02] So we're going to show both.


### Krea.Ai [7:03]
**Transcript (timestamped):**
[7:03] All right.
[7:04] So this is CREA AI.
[7:05] It's essentially stable diffusion image to image, except with their new real time capability.
[7:09] So essentially you could draw something here and I have the prompt like snake and then
[7:14] I could just increase the AI strength and then it's going to start to look more and
[7:17] more like a snake, but sort of conforming to the drawing that we're working with.
[7:22] So that's the idea with image to image.
[7:25] Essentially push it too far.
[7:26] You're going to get something totally random and pretty much might as well be as like
[7:29] majority or just stable fusion thing.
[7:32] But image to image is where I think this is the most useful for visual effects artists.
[7:36] So I'm going to remove this and undo and I'm actually, you can bring in images here.
[7:40] So you can do screen to image.
[7:41] You can actually stream from like blender or nuke or something, but you can actually bring
[7:45] in the image.
[7:46] So I brought in the square render that I told you guys to render out.
[7:49] It's yeah, basically square render in cycles.
[7:51] I'm going to scale it up here.
[7:53] Now again, we push it too far.
[7:55] It's going to go crazy.
[7:56] I have snake as the prompt.
[7:57] So it's going to do some really weird stuff.
[7:58] If I say a rocky cliff side detailed cracks stuff like that.
[8:04] And again, way too far here, but if we bring it down, we really, really bring it all the
[8:08] way down.
[8:09] We start to get some results that could be interesting.
[8:11] So you'll see that it's a little bit blurry initially and that's okay because we're going
[8:14] to use the AI upscaler, which will enhance all the detail and kind of run this process
[8:18] again.
[8:19] But the reason I like to generate first occasionally is to just see if we can get different results.
[8:24] It changes a little bit more than the upscaler.
[8:26] The upscaler just kind of add details, but this, the generate kind of changes the details.
[8:31] So it depends what you want.
[8:33] If you want to use the generate workflow or just go straight to upscaling.
[8:36] But essentially we have the blurry version.
[8:38] We can hit the seed a few times and we'll get different types of things.
[8:41] We can see the result really, really quickly.
[8:43] And as long as the shape isn't changing completely, this is something we could project.
[8:47] So again, once you're done with it, you have when you like, you can say send to enhance
[8:51] an upscale and it will go to this tab here and we can add a lot of detail to this.
[8:57] Alternatively, like I said, you can just take this image directly into the upscaler.
[9:00] So I'm going to show kind of both there.
[9:03] This is the result after bringing it in.
[9:05] So we have this blurry one that was there and then we have the upscale and we start
[9:09] to get a lot more detail in here.
[9:11] For me, this was a little bit too streaky.
[9:13] So there was kind of these streaks that kept appearing in the Kria upscale.
[9:16] So both upscalers have their own sort of strengths and weaknesses.
[9:20] I think Kria is more creative in the sense that you could generate different shapes and
[9:24] things like that.
[9:25] I prefer Magnifics upscaler currently.
[9:28] So both are being developed kind of hardcore right now.
[9:31] So that's the upscale, but let's go into Magnific and see the difference.
[9:35] So we go there.


### Magnific.Ai Upscale [9:37]
**Transcript (timestamped):**
[9:37] This is the before.
[9:38] So I just brought the render straight in.
[9:39] Didn't even generate that middle step process and then just upscale from there.
[9:45] And for me, this was a much more realistic result.
[9:47] So especially around like this region, kind of where the light's going to be hitting and
[9:52] we actually are going to see that detail.
[9:53] And it's really respecting the geometry too.
[9:55] If you look at where the light and shadows are and you look at the result that it's giving
[9:59] us, I mean, this is like an incredible detail.
[10:02] And that's all the crack detail I was explaining earlier.
[10:04] We didn't have to sculpt any of that.
[10:07] So that's pretty cool.
[10:08] We could improve this area a little bit down here if you wanted to be picky about it and
[10:13] kind of blend this further.
[10:14] So you could generate additional ones and then just blend them together.
[10:17] So that's something that I actually did in the comp.
[10:20] I generated maybe two or three that I liked and then just key mix them together.
[10:24] So Magnificent, it's not free, but you just drop your image in and then you have some
[10:29] different sliders.
[10:30] It's really, really simple.
[10:32] Creativity will modify it more.
[10:33] HDR, if you push it really far, it'll almost become too detailed.
[10:37] So generally, I would just kind of give a few random values of these three and generate
[10:44] like 10 images and then just pick the best three and then you can use that in the map
[10:47] painting.
[10:48] That's how I did it.
[10:50] And then we'll jump into how to re-project this and finalize this in Nuke.


### Re-Project in Nuke [10:54]
**Transcript (timestamped):**
[10:54] So this is after bringing it into Nuke.
[10:57] I have the first version.
[10:59] I have another version that I kind of cranked up the HDR level on Magnificent, which gives
[11:04] it a little bit of a wetter look, which kind of I was going for in the shop to look kind
[11:08] of damp and wet.
[11:10] So this looks slightly more reflective.
[11:12] Like there's things I can key out there to give it that look.
[11:15] So I kind of just key mix them together, did a few different grades here.
[11:18] So that's what I did and go to the project 3D.
[11:22] We're projecting from our projection camera.
[11:23] This is brought in from Blender.
[11:24] It's an Olympic export and we're projecting onto an Olympic export from Blender onto geometry
[11:29] that we sculpted.
[11:30] So now we have all the parallax and it's going to feel 3D.
[11:33] It's not going to feel like we stuck a 2D image in there that doesn't fit the scene.
[11:36] So the lighting fits, the textures fit, everything's working and that's how we can do it.
[11:40] So final shot camera is going to the camera.
[11:42] So we have an animated camera and we have a static camera for the projection.
[11:46] And essentially after that, this is the result.
[11:49] I've done some grading and things like that to make it actually fit the scene.
[11:52] So you can see there's definitely some stuff going on here to make the colors work, but
[11:56] we are also stenciling out the extra detail.
[11:58] We don't need the floor and the door and things like that.
[12:00] We want to keep the CG that's in there.
[12:03] So if you look at what's going on before that and we let it cache for a second, this DMP
[12:09] is essentially just being slapped over the top of our CG scene to make it better.
[12:14] So that is like a DMP enhancement.
[12:16] So that's what we can see.
[12:18] We have like the before, it's not working that great and then we have after and that's
[12:21] looking a lot better.
[12:22] And then we can obviously do all our hazing and things like that to get a much better
[12:27] result as well to make everything blend.
[12:29] So there's a lot more steps involved there for the creative stuff, but for the DMP that's
[12:33] about it.
[12:34] Also, if it interests you, we've just released some free VFX smoke acids like the ones you
[12:37] saw in this shot.
[12:39] So one's for free.
[12:40] The other ones are paid if you want a few more of them, but they're there if you want
[12:43] it.
[12:44] And additionally, there's going to be a Blender Nuke workshop for this specific two shots.
[12:49] So if you want more workflows like this or just seeing the entire process of grading
[12:53] and sort of the artistic thinking, a longer process, probably two to three hours of a
[12:58] workshop, that'll be there.
[13:00] And essentially, I think what's cool about this as well is it comes with a lot of assets.
[13:03] So it comes with all of the smoke assets instead of getting it separately.
[13:06] So it's basically almost free compared to the price of the assets.
[13:09] And then you'll also get some lens flare patterns.
[13:11] We're going to talk about the first shot as well, how to comp lasers, how to do different
[13:15] things like that.
[13:16] So there's a lot more there for the people who want it.
[13:18] And it's basically a bit of a lower price course for those who just want to have a few
[13:22] hours of extra content.
[13:23] And maybe you're more interested in doing your own indie films or just seeing more of
[13:27] these experimental workflows as well as seeing just more artistic and look development workflows.
[13:32] So that's there for the people who want it.
[13:34] And that's about it.
[13:35] Thanks, guys.



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
