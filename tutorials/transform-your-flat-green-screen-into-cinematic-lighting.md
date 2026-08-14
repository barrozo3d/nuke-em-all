---
title: Transform your FLAT Green Screen into Cinematic Lighting
source: YouTube
url: https://www.youtube.com/watch?v=7cYK2CKjp2k
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "not specified (ACES OCIO config; consistent with Nuke 15.x-17.x)"
tags: [relighting, ai-tools, gizmo, compositing, roto, grading, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/transform-your-flat-green-screen-into-cinematic-lighting/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Transform your FLAT Green Screen into Cinematic Lighting

**Source:** [YouTube](https://www.youtube.com/watch?v=7cYK2CKjp2k)
**Author:** Compositing Academy
**Duration:** 9m28s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Using relighting, I'm going to transform this screen-screen shot into an explosive scene.
[0:09] Here we can see the before and after results, but there's one technique in this that wasn't really possible in the past,
[0:14] relighting real footage.
[0:16] I'm using relighting to add interactive light on the character.
[0:18] Relighting has a lot more flexibility now that Bevel is released, and they've just released a Nuke plugin,
[0:23] so it ties directly into professional workflows.
[0:25] So before we jump into these more interesting techniques, I'm going to quickly explain what normals are


### What are Normals? [0:26]
**Transcript (timestamped):**
[0:29] and why we even do relighting in the first place.
[0:31] You've likely seen these colorful images.
[0:33] These are surface normals that define which way is surface points, so the engine knows how to light it.
[0:37] By bringing this pass into Nuke, we can actually cheat lighting after the render is finished.
[0:42] Here we have the colored render, but we also have the utility pass of normals.
[0:45] Now I can cast light from any direction without going back into 3D.


### Why is Re-Lighting Useful? [0:48]
**Transcript (timestamped):**
[0:48] Now the natural extension of thought might be, why are we relighting?
[0:52] Why aren't we just lighting in the first place?
[0:54] Oftentimes in complex CG scenes, we want to do very targeted light adjustments,
[0:57] and sometimes it's actually faster to do this in compositing without light linking specific lights to different objects
[1:02] or having to adjust shaders for many different objects.
[1:05] Up until now, this was only a luxury we had to do with CG, and it's a very common technique that Nuke composters are often using.
[1:10] But with Bevel, we can actually get normals from footage, which means we can actually do things that we would not be able to do otherwise.
[1:16] This is going to be especially useful for interactive lights, or if we just need to match that green screen footage a little bit closer to the CG.
[1:21] Now just using this tiny setup, I have a few lights around the subject, but not quite enough for a huge CG explosion.
[1:26] Normally on set, you would need some DMX lights that can sync up and flash at the same time,
[1:31] or you might not know exactly where those elements are going to be placed in CG later on.
[1:34] So here I'm running Bevel Studio, which does this AI processing locally, and I can get all my PBR passes.


### Beeble ReLighting [1:35]
**Transcript (timestamped):**
[1:39] There's also a web portal to process it on the cloud if you want, if you don't have the GPU, or you're not worried about uploading files to a web server.
[1:46] Also, if you're a studio or an individual, there's a 10% off your first year in the description of this video.
[1:51] So here's what it looks like if we pull in all of the assets that it gives you.
[1:54] First we have our source footage, we have an Albedo pass, which is super interesting by the way,
[1:58] because it's kind of removing the existing lighting and shadow that's there.
[2:02] So if you pay attention to even areas that have sort of a very rough, reflective specular,
[2:07] it's actually removing that pretty well just off the bat.
[2:11] Now the other byproduct of this that I noticed, which is very interesting as well,
[2:15] is that it's also flattening out the green screen substantially.
[2:19] So I do think potentially this could be used for keying as well to sort of ease things out
[2:23] if you have a tricky, very unevenly lit green screen.
[2:26] Potentially, I haven't tested it fully on that, but if I just take a look at this,
[2:29] we can see there's definitely some interesting things going on in this result.
[2:32] Now we also have things like depth automatically, so we're going to get all these passes we can use in different ways.
[2:37] It's not just for relighting, I think.
[2:39] Any utility pass we can use as compositor is going to be beneficial.
[2:42] So we have other things like metallic pass, we have a normal pass,
[2:46] and this is the 4K version as well that comes with the studio version.
[2:49] So studio version is even more detailed than the 1080p or I guess the 2K version, so if we were to sort of compare.
[2:56] I think I used the 2K and the Cobb, which is actually perfect for what I needed,
[3:00] but if you need that extra detail of like this little bumpiness on the surface,
[3:04] pretty incredible that it can even do this.
[3:06] We also have roughness pass, specular pass, and just basically a rough roto that we can get.
[3:12] The roto is actually pretty decent as well, so this could be good for like a garbage mat or various reasons if you just need an automatic AI roto.
[3:19] Now Beeple also has a new Nuke plugin, so if I load the PBR passes,


### Relighting Nuke Plugin [3:20]
**Transcript (timestamped):**
[3:23] essentially you will get all of the PBR passes packed into this node here,
[3:27] as well as a bit of a controller if you want to adjust the intensities of each of these.
[3:32] Essentially it's a multiplier.
[3:33] And what this gives you is if you plug it into a Beeple light,
[3:37] we have different versions here, so we have directional light, point light, environment light.
[3:41] So here I've just plugged it into an environment light, which is essentially an HDRI,
[3:44] and we can essentially relight this footage.
[3:46] So if we look at the source and we look at the relight version,
[3:49] we're getting a pretty awesome result here right off the bat.
[3:52] So if this was like an underwater shot, we needed to adjust the lighting here.
[3:56] This would actually be a pretty good starting point to start manipulating this from.
[4:00] So we can plug it into different HDRI as well just to see the difference here.
[4:03] And we can see different results and we can bring this spec way down because it's too much.
[4:07] So I was pushing that up, but essentially spec and diffuse are separated.
[4:11] So if you want to work through this tool, you can.
[4:14] And it's a pretty good starting point.
[4:16] I would still pull in some of these other passes and do some more traditional
[4:20] compositing techniques on top of this result, given the fact that we have these passes,
[4:24] you can really dial it in.
[4:25] So this would be a good starting point.
[4:27] Now we also have other lighting options such as just a directional light,
[4:32] which is kind of like the normal rotate normals node.
[4:35] If you've used this on Nucopedia where you can just essentially rotate normals around and hit,
[4:39] you know, if you want to add a light from one direction, we could do something like that,
[4:42] which is more directional and we could composite that on top of the original and do those type of things.
[4:47] And we also have a point light if we wanted to have sort of a basically a fall off and we can adjust the depth.
[4:54] We can adjust the color, the intensity, etc.
[4:56] So these are all the main three lights we can use the Bevel.
[4:59] Now those are the main ways to do it.
[5:02] If you want to work through the Bevel plugin, but in my project, I wanted to do it a slightly different way,


### Creating a Chrome Pass [5:06]
**Transcript (timestamped):**
[5:07] which is actually just a free node on Nucopedia called reflection buddy is essentially the same exact concept,
[5:12] except we just need the normals that that Bevel is generating here.
[5:16] So here I have the Bevel normals and I've basically plugged in this HDI.
[5:22] Here it is.
[5:23] And then we put it into reflection buddy.
[5:25] So this is going to actually make a mirror like reflection rather than more of a diffused result.
[5:30] And the reason we want this is going to become obvious in a second, but I like this reflection buddy node because you can essentially move the reflection around based on a 2D selector here.
[5:41] So I can click this and I can select on the normals.
[5:44] So if I go here and I click and drag, essentially that reflection will be moving around based on the surface of the normals here.
[5:50] So it's similar to the Bevel one, we can move the XYZ position of the HDI.
[5:54] But if you want a very mirror like result, this is also a good option.
[5:58] Now the reason you would want a mirrored result is well, if you want a fake reflection, that could be one reason.


### Reflection Roughness [6:01]
**Transcript (timestamped):**
[6:05] If you just like a very sharp reflection like this, which is pretty cool and interesting that you can do this.
[6:10] But in my result, I actually wanted to reflect an explosion, but I want to reflect the explosion differently on different materials.
[6:18] So when you're composing something, we need to consider what is the material that we're composing onto.
[6:23] So if we look at this person, the eyes are going to be like a perfect reflection.
[6:28] The shirt is going to be very diffused and then the helmet is going to have sort of a rough, essentially soft specular reflection.
[6:35] And so I want to be able to control the glossiness or the roughness of the reflection of the different parts.
[6:41] And so being able to separate this out using this reflection buddy, essentially all we need to do is take the HDI and blur it.
[6:49] And that would essentially mimic a rough reflection.
[6:52] So it gives you a ton of control over the type of reflection you're trying to essentially incorporate here.
[6:57] So this would be a rough reflection.
[6:59] And what's cool about doing this way instead of just doing, let's say, a rotate normal thing where we graded up and, you know, we add a little bit of orange if we were to add explosion.
[7:07] The benefit of this is I'm actually using the video.
[7:09] So it's going to be exact to the real thing.
[7:12] So here's my little explosion at the end of my sequence here.
[7:15] So just blown out because it's going to be completely overexposed anyway.
[7:18] There's like no detail on purpose.
[7:20] And essentially, if we look at this through reflection, buddy, essentially, we have something like this where it's going to explode at the same exact time and we can get that results.
[7:30] Now, again, like I mentioned, what we could do is key makes a few versions of this together based on the material of the object.
[7:36] So what I would do is essentially blur this image.
[7:40] And we'll get a different type of reflection, something like this.
[7:44] And then we could bring the intensity of that down.
[7:46] We could mix that back and essentially do actual composing techniques where we're going to mix all those things together.
[7:52] So that's what I've done here.
[7:53] I have a few versions of this reflection that I've done, such as this more harsh one, a slightly softer one, maybe for the clothes.
[8:00] And then I start to go in and actually target different areas based on the materials.
[8:04] We want to avoid the plastic look.
[8:06] This is something that with the relighting, if people are relighting footage, I've seen this mistake.
[8:11] What we want to do is break up the highlights or boost the highlights based on what the surface is actually doing.
[8:16] So, for example, the shirt, we might want to break it up with some noise or just key some of the darker areas and break it up to make it feel more natural.
[8:24] It's not going to be this perfectly smooth reflection, like maybe that what the normal is giving us.
[8:28] So we need to go back into actual targeted corrections.
[8:31] And we might also have other areas that are interesting, such as maybe this ring on the helmet is going to reflect because it's much more mirror-like than the actual helmet that it's sitting on.
[8:41] So if we look at the real footage here, we see there are these little metal pieces that really have sharp reflections on different areas.
[8:47] And that's where we could either mix that really sharp specular or if it's just a frame or two, we could just blow out that highlight.
[8:54] But we see that that little helmet is reflecting different.
[8:57] So we have that control to just, you know, do some quick rotors on those areas and boost things or dim them down or break them up where necessary.
[9:05] So this was my first time trying out Bebel on this project.


### Conclusion [9:06]
**Transcript (timestamped):**
[9:07] I thought it made a lot of sense given what I was working with.
[9:10] I do think these AI-assisted workflows are going to be adopted quickly by studios, especially the ones that are giving more control to artists to like with Bebel rather than less control.
[9:18] If you want the 10% discount, it's in the link in the description.
[9:21] There's also an additional link below if you want the class for the shot, which will be coming out soon.
[9:24] Make sure to hit thumbs up if you want to see more videos like this and that's about it.



---

## Captured Frames

- [0:42] tutorials/frames/transform-your-flat-green-screen-into-cinematic-lighting/frame_000.jpg
- [1:54] tutorials/frames/transform-your-flat-green-screen-into-cinematic-lighting/frame_001.jpg
- [3:23] tutorials/frames/transform-your-flat-green-screen-into-cinematic-lighting/frame_002.jpg
- [3:44] tutorials/frames/transform-your-flat-green-screen-into-cinematic-lighting/frame_003.jpg
- [5:16] tutorials/frames/transform-your-flat-green-screen-into-cinematic-lighting/frame_004.jpg
- [7:20] tutorials/frames/transform-your-flat-green-screen-into-cinematic-lighting/frame_005.jpg

---

## Structured Notes

### Core Technique
AI-generated PBR/normals passes (via the Beeble/Bevel tool + its Nuke plugin) let you relight already-shot green-screen footage in comp — casting new directional/point/environment light from any angle without returning to set or 3D — and separately build a controllable mirror-style reflection pass with ReflectionBuddy for compositing reflective elements (like an explosion) onto the subject.

### Summary
Compositing Academy shows how Beeble Studio's AI processing derives a full PBR pass set (Albedo, Normal, Roughness, Specular, Metallic, Depth, rough roto matte) from ordinary green-screen footage, in both 1080p/2K and a more detailed 4K "Studio" tier. Bevel's Nuke plugin packages those passes into a single node with per-pass intensity multipliers, feeding directional/point/environment Bevel lights to relight the plate. The second half builds an alternate, free approach using the community ReflectionBuddy gizmo (Nucopedia) fed an HDRI and the Bevel normals to create a steerable mirror reflection (2D XY selector to aim it, blur to control roughness/glossiness per-material — sharp for eyes, soft for a helmet, diffused for cloth) so a CG explosion element can be reflected convincingly and material-matched across different surfaces on the same subject, finishing with manual roto/paint touch-ups to break up overly perfect highlights.

### Key Steps
1. Process green-screen plate through Beeble Studio (local GPU or cloud web portal) to generate Albedo/Normal/Roughness/Specular/Metallic/Depth/roto passes.
2. Load the PBR pass bundle into Nuke via the Bevel Nuke plugin node, which exposes per-pass exposure/intensity multipliers (source blend, roughness, specular, metallic).
3. Feed the PBR node into a Bevel light node (`BevelEnvironmentLight`, or the Directional/Point variants) to relight the plate — Intensity, Diffuse Intensity, Specular Intensity, Horizontal/Vertical Rotation knobs.
4. Alternative/supplemental path: feed the Bevel Normal pass + an HDRI into the free `ReflectionBuddy` gizmo to build a mirror-like reflection instead of a diffuse relight.
5. Use ReflectionBuddy's 2D on-viewer selector (drag over the normals) to steer where the reflection sits on the surface.
6. Blur the HDRI input to ReflectionBuddy to soften the reflection per target material (sharp for eyes/metal, soft for a helmet, heavily diffused for cloth) — build several ReflectionBuddy passes at different blur levels and key-mix them together by material region.
7. Composite a practical element (e.g. an explosion plate) through the reflection passes so it reflects convincingly and in sync with the source footage's real timing.
8. Manual roto/paint pass to break up unnaturally smooth relit highlights (e.g. add noise/grain to a shirt) so the result doesn't read as "plastic."

### Nodes / Tools / Settings
- `BevelEnvironmentLight` (and Directional/Point variants) — Light Control: Intensity, Diffuse Intensity, Specular Intensity, Horizontal Rotation, Vertical Rotation
- `PBRController` node — Source Blend, Roughness Exposure, Specular Exposure, Metallic Exposure (per-pass multipliers on the Bevel PBR bundle)
- `ReflectionBuddy` (free Nucopedia gizmo) — takes Normal pass + HDRI/environment image, on-viewer 2D XY selector to aim the reflection, blur input for roughness control
- Multiple `Read` nodes for the Beeble PBR pass bundle (Albedo, Normal, Roughness, Specular, Metallic, Depth, roto/alpha)
- Roto/keying + manual grade touch-ups to break up overly clean relit highlights

### Difficulty
Intermediate

### Foundry App & Version
Nuke (compositing environment for the Bevel plugin and ReflectionBuddy gizmo). No on-screen Nuke version banner; ACES OCIO config visible in Read node metadata is consistent with a recent Nuke 15.x-17.x setup. Beeble/Bevel is a third-party AI relighting tool (web portal + local GPU processing + Nuke plugin), not a native Foundry feature — no Nuke 17.x native-splat/relight overlap here, this is a separate AI-relighting pipeline.

### Tags
relighting, ai-tools, gizmo, compositing, roto, grading, intermediate

---

## Related Tutorials
None yet in the knowledge base share the `relighting` + `ai-tools` combination — first entry establishing these tags. Future AI-relighting or normals-based relighting tutorials (e.g. "The BEST Way to Use Normals to Relight in Nuke") should cross-link here.
