---
title: A new way to design VFX | Virtual Reality | Gravity Sketch + Nuke Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=wEHiUNE66fk
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke (cross-platform: Gravity Sketch is a third-party VR modeling app, not a Foundry product; Nuke both generates the source textures and would composite the final result)"
version: "Nuke 13.x (13.1/13.2 — exact 2022 point-release not stated)"
tags: [compositing, procedural-texture, gizmo, motion-graphics, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/a-new-way-to-design-vfx-virtual-reality-gravity-sketch-nuke-tutorial/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# A new way to design VFX | Virtual Reality | Gravity Sketch + Nuke Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=wEHiUNE66fk)
**Author:** Compositing Academy
**Duration:** 15m48s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to this tutorial. This is going to be a video about how to design effects
[0:11] in a new way. And I think that I don't think this workflow has been explored that deeply.
[0:17] I think it's a kind of a new workflow with some virtual reality software called Gravity
[0:22] Sketch. And so Gravity Sketch is primarily a tool for 3D modeling. It's actually more
[0:27] of a concept design and modeling tool. And I've been exploring Gravity Sketch for some
[0:33] other uses, for some independent filmmaking that I'm working with a friend and some other
[0:37] people on to kind of develop some independent filmmaking workflows around Unreal and Blender
[0:42] and kind of VR workflows as well. But this is a different way to use Gravity Sketch and
[0:48] kind of using some of these 2D effects that I've been talking about on some of the last
[0:53] videos. And basically how we can kind of design these in a new way with combining Nuke and
[0:59] Gravity Sketch. So essentially, this is just a kind of a slap kind of comp of like a wormhole
[1:06] type of thing. Definitely not a final quality type of effect. This is, I spent maybe an
[1:11] hour and a half on it. So just a quick kind of sandbox type of thing playing around. This
[1:17] is just in Nuke, but fundamentally this concept of taking these textures and ignore the script
[1:22] if you would, because it's just, this is really a sandbox. It's not like a real shot, just
[1:27] playing around. But fundamentally taking these two dimensional textures and wrapping them
[1:31] into 3D geometries in different ways was where the idea came from. But essentially, we can
[1:38] do a more advanced version of this, like kind of modifying these textures and placing them.
[1:44] You know, for example, I created this texture from some of the elements and kind of basically
[1:50] just wrap this onto a cylinder in 3D space. But rather than just using cylinders, we can use
[1:55] Gravity Sketch's NURBS modeling workflow to like create really crazy geometries that wouldn't be
[2:02] really possible or easy to do in Nuke. And it would be kind of difficult to do even in Houdini
[2:08] or Maya or whatever software you're using, because it's just not, you know, you'd have to use
[2:13] curves and like extruding along curves and NURBS and stuff like that. So yeah, I'll kind of
[2:18] present that workflow and how we can actually use it. I'll just show a couple examples of some of
[2:24] the 2D textures I created going into Gravity Sketch. So I'll start with some materials like
[2:29] some of these. And these are all from that library. And I kind of used Chris Friar's node. I'll
[2:36] release his video or his tutorial in the description there. He had a really awesome tutorial about
[2:42] how to use this sort of bi-directional God right now that he created, which creates a God right in
[2:47] two directions instead of one from a point. And in that tutorial, he actually mentioned a way to
[2:54] kind of kind of spectrum map through it, which I had never actually seen before. It was really,
[2:59] really unique workflow. I thought it was really clever. And so I thought to kind of take that
[3:04] method and apply it to some of these elements. And it turns out you can create some really crazy
[3:08] stuff by just doing this. So you start to get these like really great kind of crazy, you know,
[3:15] rainbow type of effects that you can create. And there's all kinds of stuff you can do with it.
[3:20] But fundamentally, what's doing, and you can watch his original tutorial. It's just it's like an
[3:26] advanced tile almost, you can tile, and then you can map the colors differently on each tile that
[3:31] you're creating. So you can either tie with tile through scale or rotation and lower the samples
[3:36] to a low amount. You can actually do this with a normal God right node as well. But I like his
[3:41] because he has that center point thing and it kind of goes in both directions. So yeah, go check
[3:46] that out for sure. But here's like some of the patterns I created using that technique. At first,
[3:52] I created the kind of, I don't know, rotated design here. And then I just did a polar distort to
[3:58] create them in a flat kind of space. And of course, these are animated. So if I step through,
[4:03] you'll see that there is animation, you know, on this. So same with all these, like I just did
[4:10] the same sort of technique in different ways, and created some different designs, stuff like this,
[4:16] and then I would kind of polar distort it to create like a flat version. And these were going to
[4:21] use to stretch across these kind of crazy geometries and gravity sketch. So here's just a couple more
[4:28] examples of the type of things you can do. If you're just playing around. And like I said,
[4:31] this is a really messy script, none of the nodes following concatenation or any of those rules
[4:36] that we have, it's just it's purely just playing around, you know, with different stuff here.
[4:41] So here's a few more textures that were created. So I had something that was kind of interesting
[4:48] like this looks kind of like a galaxy type of thing, you could you could definitely create a
[4:52] galaxy from this effect if you wanted. But yeah, basically just kind of doing some rainbow stuff
[4:58] to get some color variation in there first. And then we can kind of, yeah, polar distort this. So
[5:04] we get this nice texture that is animated. So gravity sketch doesn't take animated geometry
[5:09] animated texture rather. But we can export one frame of this, we can design our geometry in
[5:15] gravity sketch using the material on it. And then we can bring that geometry back into nuke,
[5:20] and we can actually take the animated version and kind of make it, you know, go crazy on the on
[5:26] the surface. So essentially, that's what we're doing. And here's here's another example. So we
[5:32] have like a here's a shape like this kind of animated like this. And we can take and do this
[5:37] type of effect where we kind of god ray it with a few samples and make the make a rainbow design.
[5:42] And then we can polar distort it so we get a flat pattern again. And if you scrub through,
[5:48] you're going to see that this is actually moving and still has an interesting look. But I'll export
[5:52] one frame of this into gravity sketch. So those are just a few examples. There's a bunch more
[5:58] here that I did of just random, random designs and stuff like that, just playing around. But
[6:06] yeah, we'll hop into gravity now and start showing how we can actually kind of create new designs
[6:12] with these. Alright, so we're in gravity sketch. So I'm going to start a new sketch here. And


### Gravity Sketch [6:13]
**Transcript (timestamped):**
[6:19] probably some of you guys have never seen the software. So I'll just briefly explain what it
[6:23] is and what it is that normally people are using it for. So people are normally using this for
[6:28] 3d modeling software. So you have like basic stuff like strokes, you can create these like kind of
[6:34] stuff like this. And you can increase the brush size and we can create these like paths. You can
[6:40] also do like ink and stuff like this. So you may have seen tilt brush before, but maybe we've never
[6:45] heard of gravity sketch. So gravity sketch is more 3d modeling. So what's great about this is you
[6:49] can actually take the vertices. This is a nerve. So maybe it would be the surface points. But yeah,
[6:54] we can basically take these points and you know, model different stuff here. So that's how it kind
[6:59] of works. But you also have really great tools like revolve. So you can kind of take a point and


### Revolve [7:00]
**Transcript (timestamped):**
[7:04] rotate around an axis and kind of create geometries like this. But you can start to see where we're
[7:09] starting to go with this is like if we can create these geometries, what else could we do with this?
[7:14] It's like, yeah, you could create models and cars and whatever it is that you're doing,
[7:18] which is mostly what it's intended for. But what gravity sketch allows you to do is actually bring
[7:23] in materials. So we can bring in some of those materials have exported there's a few of them here.
[7:29] And normally they're just used to be used as like materials on a model or just reference pictures.


### Materials [7:30]
**Transcript (timestamped):**
[7:34] But if you load in reference pictures, so something like this, if I start pulling these off with my
[7:39] hand, I can actually grab them. I can put them off to the side. And as I start to do this,
[7:45] it actually loads these textures in as ones we can wrap on the 3d models.
[7:51] So I'm going to grab a few that I find interesting here. These are some of the ones I kind of put
[7:55] together a nuke if I just scale it up and we look at it. It's just one of the effects with a basic
[8:00] color grade on it. And then these are the ones where I did some polar distorts and some other stuff.
[8:05] So we have those. And then we can take, we give this second a load here, we'll let some of the
[8:11] other ones load here. So they load on a cloud and it's kind of connected. And so like even some
[8:16] of these, like this is just a basic color grade on some of these here, like this one.
[8:22] And yeah, so what are we going to do? We can basically set a material now. So in our, we can
[8:27] actually right click and press in the toggle and kind of select materials. So basically you can
[8:34] create these axes and then I can start to revolve and you see my texture will be wrapped
[8:39] onto that material. So you can really start to see where we're going to go with it. It's like,
[8:42] well, we can start to do really creative stuff and move our hand a lot and we can create these
[8:47] multi-layered effects really, really easily. So creating stuff like this, if you're creating like a
[8:52] jet engine or some kind of portal or whatever it is that you're doing, you can really design
[8:59] stuff in here and kind of stretch up and down in a way that you're not going to loft and make curves
[9:05] in Maya or Houdini or something like this and design that. It's just not going to make sense
[9:09] because it's not as intuitive and you're not going to see how the texture is actually stretching.
[9:13] But here you do. So keep in mind, even though this is a still image, we can animate this in
[9:20] Nuke. So if we export that back to Nuke, we can animate the textures flowing on that path because
[9:26] it's the UV already in the correct way. So let's just continue with this. We can create some different
[9:31] designs here. We can try switching the pattern so we could go here and we could pull it along. And
[9:39] if you look at the design, we can really see. And this is all in stereo for me. So I'm seeing this
[9:44] all in true 3D. So it's really giving you a sense of depth and how you can design these things. And
[9:51] even if we weren't to use this as the final composite, this shape alone is very interesting.
[9:55] You see how we have all those layers of parallax in there. We could use that as an engine on something.
[10:03] So we can create new designs. And if we switch to another material, we can switch to the surface.
[10:11] Surface is cool because it allows you to take two of your hands like this and you can drag out like
[10:15] this. And we can actually create these geometries that are more like surface. So we could try something
[10:23] different here. Let's try this one. Maybe this one's better. So you could really see, you know,
[10:27] you could create like a shockwave type of thing. You maybe you could switch to a revolve. And if
[10:34] you had like, you know, a character landing, you could go here and, you know, create that impact.
[10:40] And then you could create multiple levels of geometry to get
[10:44] detailed layers basically in there. So we'll have those, those, those kind of, you see, we have
[10:49] depth in between those cards. If we're kind of rotating between. So we can delete that. We can
[10:56] try some different stuff. Stroke is kind of cool because you can create polar symmetry. So you can
[11:03] create these basically circles around a point. So we can kind of zoom out and we can design around
[11:09] this point. So if we wanted to create a wormhole, you know, maybe we could start with, you know,
[11:16] more of a revolve thing, we could just use one of these textures to preview what it's going to be
[11:20] like, something like this. The the transparency and gravity sketch isn't perfect, by the way. So
[11:28] it's a little bit glitchy, but it still could do a good idea. And then we could just go here with
[11:33] another material. You know, I could do something like this, or let's try this one.
[11:40] And this is the one that has, yeah, this one's kind of different, has more of the kind of triangle
[11:44] stuff. So you can really start to see how we can really come up with different designs here. And
[11:51] these are not final effects, we can we can animate these in nuke. So let's try something else here.
[11:59] We could try surface, we could add on to this. So maybe we would go here with another material.
[12:04] And maybe if it's bending space around it, it would kind of bend the light. So we could use
[12:09] this material here. And sort of layered in so you see them, the transparency is not working 100%
[12:16] there. But we can we can kind of see it here. So let me just grab this piece so I can kind of
[12:24] duplicate that around. And that I could use in nuke as a kind of refractive edge of a wormhole.
[12:32] And I could kind of design this. And here you see we're not seeing it properly, but it is there.
[12:39] So you know, in this case, it's a little bit annoying because we know we can move it back and
[12:43] or do whatever. But you can create different designs like this. So it's just a really, really
[12:50] interesting way to work. And there's different things you can do with it. Play around with it.
[12:55] It's definitely a new way to work this this kind of working that way of working never existed before.
[12:59] But you know, doing these revolves and doing these different layers here, we could try another
[13:06] material. So let's bring another material in. Go to the materials. Give a second to download.
[13:21] We can grab. So I have some particle ones here, some lasers, I have this one as well, kind of cool.
[13:27] This one's pretty cool as well. So I could try this. And then, you know, let's make sure we switch it.
[13:34] So something like this. And then when you're flying through, if this was transparent in the
[13:39] right way, we would be able to see some of that stuff that's on the outside. So maybe this material
[13:44] is not so correct with transparency, but let's see. So we have looking through there, and then we can
[13:51] add the stuff around. So what I'm trying to say is the key about this is you can get those levels
[13:57] of parallax that would be kind of difficult to do directly in other ways. So if we're flying through,
[14:04] we can see those things around, we can see them above, and we have that sense of 3D. So if we're
[14:09] moving a camera through this, these objects will move at a lesser speed. So we can spend a lot of
[14:15] time designing it. Or if you go in here, we could animate around the inner edges. So we could actually
[14:20] zoom ourselves out and kind of take them, take the material and animate around these inner rings.
[14:28] So that when we're flying through, you know, we can create different effects that we're going to
[14:34] see as we're going through this, this sort of wormhole. So I'm just using my hands and grabbing
[14:40] and scaling basically right now, which gives me a pretty good sense of the depth there.
[14:50] Yeah, so that's pretty much it in terms of what you can do. There's all kinds of stuff. You can
[14:55] spend a lot of time making like really good designs. And this is me just like playing around and
[14:59] everything. You could even make some galaxies and stuff like that if you were just duplicate these
[15:03] like crazy, you know, you can just duplicate a whole bunch of stuff. And then, you know,
[15:08] that's something you could export right back into Nuke and work it into a higher quality level. But
[15:18] you know, let's just see. You could do something like this and you could mix in different layers.
[15:25] So, you know, there's all kinds of stuff you could do. And if you flew a camera camera through
[15:28] this in Nuke, it's already more interesting than flat cards, because you have all these layers
[15:33] of depth. So really awesome way to just sketch out effects and design different things. So
[15:40] hopefully you guys found the video interesting or useful and hit the like button if you did. And
[15:47] that's about it.



---

## Captured Frames

- [1:00] tutorials/frames/a-new-way-to-design-vfx-virtual-reality-gravity-sketch-nuke-tutorial/frame_000.jpg
- [3:52] tutorials/frames/a-new-way-to-design-vfx-virtual-reality-gravity-sketch-nuke-tutorial/frame_001.jpg
- [6:34] tutorials/frames/a-new-way-to-design-vfx-virtual-reality-gravity-sketch-nuke-tutorial/frame_002.jpg
- [8:39] tutorials/frames/a-new-way-to-design-vfx-virtual-reality-gravity-sketch-nuke-tutorial/frame_003.jpg
- [10:15] tutorials/frames/a-new-way-to-design-vfx-virtual-reality-gravity-sketch-nuke-tutorial/frame_004.jpg
- [13:27] tutorials/frames/a-new-way-to-design-vfx-virtual-reality-gravity-sketch-nuke-tutorial/frame_005.jpg

---

## Structured Notes

### Core Technique
Generate 2D procedural "energy"/wormhole-style textures in Nuke (via a bidirectional GodRay-based spectrum-mapping trick), flatten them with `PolarDistort`, then use them as reference/wrap materials inside the VR modeling app **Gravity Sketch** to hand-sculpt NURBS-based 3D geometry that would be impractical to build with curves/lofts in Nuke, Houdini, or Maya — then bring that geometry back into Nuke so the *original animated* (not the single exported still) texture can be re-applied to its surface.

### Summary
An exploratory/"sandbox" video (author explicitly disclaims the demo Nuke script as messy, non-production) demonstrating a workflow bridging 2D procedural texture design in Nuke and VR-native 3D modeling in Gravity Sketch. The Nuke side (frame_000, a wormhole slap-comp; frame_001, the messy sandbox script) starts from a technique credited to a fellow artist named Chris Friar: a custom bidirectional `GodRay`-style gizmo that rays out from a center point in two directions at once, combined with tiling (via scale/rotation, low sample count) and per-tile color/spectrum mapping to create rainbow/energy patterns — the author reproduces and extends this "spectrum map through tiling" trick to build a library of animated abstract textures. Each pattern is optionally rotated then flattened with `PolarDistort` into a tileable flat texture (frame_002 shows Gravity Sketch's basic stroke/point-editing UI as context for the modeling side). These flat textures are exported as reference/material images into Gravity Sketch, a VR 3D modeling app (not a Foundry product) primarily used for concept/product design — inside VR, the artist can grab a texture, assign it as a material via a right-click toggle, and use tools like **Revolve** (rotate a profile around an axis — frame_003 shows a revolved ring geometry lit up with the imported texture), **Surface** (drag geometry out with both hands, good for shockwave-like forms), and **Stroke with polar symmetry** (repeat a stroke radially around a point — natural fit for wormhole/portal designs) to sculpt 3D forms directly around the texture in true stereo 3D, seeing exactly how the texture stretches across the surface as they design — something the author argues is far more intuitive than lofting curves in a DCC without that direct visual/spatial feedback. Multiple material layers can be stacked in VR for cheap, convincing parallax (frames 004-005 show layered glowing ring/particle materials forming a wormhole-like composition) that would be tedious to achieve with flat 2D cards alone. Because Gravity Sketch only supports static (non-animated) reference textures, only a single frame is exported for use during VR modeling — the payoff comes after: the sculpted geometry is brought back into Nuke, where the *original animated* texture (not the static VR reference) is reapplied to its UVs, so the final render/comp gets both the hand-designed, VR-native 3D form *and* full texture animation. The video ends before showing that re-import/re-texture step in detail — it demonstrates the texture-generation and VR-sculpting halves of the pipeline only.

### Key Steps
1. Build a base animated "energy" texture in Nuke using a bidirectional `GodRay`-type gizmo (credited to Chris Friar) that emits rays in two directions from a center point.
2. Tile the ray pattern (via scale and/or rotation repetition, kept at a low sample count) and map different colors per tile to produce spectrum/rainbow-style variation instead of a single-hue glow.
3. Optionally rotate the design, then flatten it with `PolarDistort` into a tileable, non-radial flat 2D texture — repeat this generation process to build a small library of distinct animated patterns.
4. Export a still frame of each pattern (Gravity Sketch only accepts static reference/material images, not animated textures) for use inside the VR app.
5. In Gravity Sketch: load the exported textures as materials, assign one to a geometry via right-click → material toggle, then sculpt using **Revolve** (axis-rotated profile), **Surface** (two-handed drag/extrude), or **Stroke with polar symmetry** (radial repeat around a point) — watching in real stereo 3D how the actual texture stretches across the surface as the geometry is shaped, rather than guessing at UV stretch the way a flat-screen loft/curve workflow would require.
6. Layer multiple separately-modeled/textured pieces in VR (e.g. an inner glowing ring plus an outer particle/laser layer) to build up parallax depth cheaply — noted as one of Gravity Sketch's biggest advantages over flat 2D compositing cards for this kind of design work.
7. Bring the finished geometry back into Nuke with its UVs intact; reapply the *original animated* (not the static exported-reference) version of the source texture, so the final asset combines VR-sculpted 3D form with full texture animation. (This re-import/re-texture step is described but not shown step-by-step in this video.)

### Nodes / Tools / Settings
- **Core Nuke:** `PolarDistort` (Nukepedia gizmo — same one used in "360 Spherical LatLong Textures" and "Mixed Medium VFX P1", here for flattening radial patterns into tileable textures rather than sphere-wrapping or artistic abstraction), Transform (tile via scale/rotation), Grade/color mapping per tile for the spectrum effect
- **Bidirectional GodRay gizmo:** credited to fellow artist Chris Friar (his own tutorial referenced in the video description) — emits rays in two directions from a single center point, unlike a standard one-directional `GodRays` node; combined with low-sample tiling to fake a spectrum-mapped rainbow look
- **Gravity Sketch (third-party VR app, not Foundry):** Revolve, Surface, Stroke-with-polar-symmetry tools; material/reference-image import (right-click → material toggle); geometry export back to a DCC with UVs preserved
- **Workflow constraint to remember:** Gravity Sketch materials are static images only — always export a single representative frame for VR modeling, then swap back to the animated source texture once geometry returns to Nuke

### Difficulty
Intermediate — the individual Nuke nodes are simple (GodRay gizmo, tiling, PolarDistort), but the workflow requires comfort in a completely different (VR) tool and the conceptual leap of designing 3D form around a 2D texture's visual stretch rather than through curves/lofts.

### Foundry App & Version
Nuke for texture generation (and, per the author, for the eventual re-composite once geometry returns from VR) — cross-platform with Gravity Sketch, a third-party VR modeling app with no Foundry relationship. Nuke version not stated on screen; per this skill's version-tracker, a 2022 upload falls in the 13.1 (Nov 2021) → 13.2 (Apr 2022) window. Nothing in this video uses Nuke's actual 3D system (Sphere/Camera/ScanlineRender) — all "3D" work happens in Gravity Sketch, not Nuke.

### Tags
compositing, procedural-texture, gizmo, motion-graphics, intermediate

---

## Related Tutorials
- 360 Spherical LatLong Textures | Nuke Tutorial (`360-spherical-latlong-textures-nuke-tutorial.md`) and Mixed Medium VFX P1 (`mixed-medium-vfx-p1-blender-nuke-ai-embergen-vr-tutorial.md`) — both share the `PolarDistort` gizmo, each using it for a different purpose (sphere-wrapping, artistic radial abstraction, and here flattening a radial pattern into a tileable texture); useful to read together to see the same node applied three different ways.
- Mixed Medium VFX P1 also shares the broader "design 2D textures in Nuke, hand-build custom 3D geometry in another tool, bring it back into Nuke" pipeline shape (there: Blender; here: Gravity Sketch VR).
- [3/3] Nuke Tutorial Series (Flow Paths, FX Integration, Design) (`33-nuke-tutorial-series-flow-paths-fx-integration-design.md`) — shares the same "author 2D textures in Nuke, hand-sculpt supporting geometry in a VR app, bring it back into Nuke" pipeline shape (there: Tilt Brush flow-path curves; here: Gravity Sketch NURBS models).
