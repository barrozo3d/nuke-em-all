---
title: Stormy Crystal Skull | Nuke, Blender, Ai, Embergen, Mixed VFX Medium Part 2
source: YouTube
url: https://www.youtube.com/watch?v=prhQhQ5AnNM
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke (cross-platform: EmberGen storm sim + Blender/Adobe Medium sculpting for the CG asset, but the compositing techniques — the video's back half and this skill's focus — are pure Nuke)"
version: "Nuke 13.x (13.1/13.2 — exact 2022 point-release not stated; Classic 3D system / no USD-specific nodes used)"
tags: [compositing, merge, channels, st-map, gizmo, grading, fx-simulation, lighting, advanced]
extraction_status: complete
frames_dir: tutorials/frames/stormy-crystal-skull-nuke-blender-ai-embergen-mixed-vfx-medium-part-2/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Stormy Crystal Skull | Nuke, Blender, Ai, Embergen, Mixed VFX Medium Part 2

**Source:** [YouTube](https://www.youtube.com/watch?v=prhQhQ5AnNM)
**Author:** Compositing Academy
**Duration:** 27m3s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Hello guys, welcome to part 2 of this tutorial. This time we will be talking about how the
[0:13] skull aspect was made and kind of everything involved in that. So we'll cover VR, Blender,
[0:20] Nuke and EmberGen. So it's a couple different workflows and so if you just want the compositing
[0:25] aspect there are some techniques that will be covered in that portion which will be sort
[0:30] of the last part of the video but if you're looking for CG stuff that will be sort of
[0:35] on the front end of this video. So yeah I know some people are just looking for compositing
[0:39] or some are looking for 3D as well so keeping that context in mind you can just look at
[0:44] the timeline of the video. So yeah we're not talking about the frame in this one we're
[0:47] just going to talk about the skull itself. So basically I guess we'll talk about the
[0:53] EmberGen portion first which is basically this sort of storm simulation. So I'll hop
[0:59] into EmberGen in just a second here. I'm not going to cover every button and every sort
[1:03] of parameter I suppose this is just a general workflow like the last video and if you're
[1:09] looking for very specific you know like turbulence settings and all these kind of things if you're
[1:13] simulating fluids you know you basically just need to play around with it to truly understand
[1:19] because there's a lot of settings in EmberGen so just keep that in mind something you really
[1:23] just need to dive into. So we're in EmberGen here and I'll just explain really simply how


### Embergen [1:28]
**Transcript (timestamped):**
[1:29] this is done. I'll switch to a mouse because the whack and glitch is a little bit here.
[1:34] Switch to mouse. So it's a very simple node setup. It's almost like the default node setup
[1:39] and you just add a couple of force noise and stuff like that so if we let this play and
[1:45] see what the EmberGen simulation looks like so this is in real time which is what's really
[1:49] great about this so we can get iteration speed much quicker in EmberGen than using something
[1:54] that's going to take a little bit longer. So for me this works great. The level of detail
[1:59] here is definitely good enough for what it's being used for and so basically all we have
[2:05] is a sphere emitting some smoke here and you're going to have to play with the settings a bit
[2:13] to get the smoke density right so you can control all these kind of things if you're
[2:16] familiar with EmberGen already you can control the amount of dissipation, the amount of generated
[2:23] smoke if you're using flames so we're not using any flames here basically just using pure smoke
[2:27] and we're also applying a force to it so I've applied a force line in the center with a little
[2:33] bit of a twist and a slight repel strength so it kind of pushes it outward against this skull.
[2:41] So we're simulating it inside of a skull which is imported as an FBX as a collider so basically
[2:48] it's just colliding against this and this is the kind of simulation that we're getting here.
[2:52] So the light is just temporary so I didn't render directly out of EmberGen and I'll explain why
[2:59] that's necessary for what I wanted so I'm sure you could modulate this light in here and you
[3:05] could animate it but I really wanted to get that ray tracing I wanted it to have sort of since the
[3:13] skull is made of crystal or a quartz material we really want this effect to have that refraction
[3:20] and that ray trace quality so although you could import an Olympic camera into EmberGen and render
[3:27] this directly which you certainly could work with this you could bring this in and fake that
[3:33] distortion rather than you know ray tracing that refraction that is a potential workflow but I just
[3:40] prefer to have a ray trace since you know why not it's a it's better quality so I did one simulation
[3:45] here and that's kind of nice but the back of the skull was a little bit empty so I also did a second
[3:50] simulation so just open this up and go to the second one and this is just the same basic
[3:58] simulation but I shifted the spawn spawn point I guess the emitter to the back of the skull so
[4:04] that basically just kind of fills it up on the backside and so we have two simulations that you
[4:10] can export as VDB so you can export VDBs and use open VDB in Blender to bring these in so to


### Blender [4:17]
**Transcript (timestamped):**
[4:17] hop into Blender here this is the kind of scene setup and to show those EmberGen simulations if
[4:22] I just disable the sort of skull layer here and look at the inside of what this is we basically
[4:29] have the two VDBs loaded in so you can load these in if you just hit shift A shift A and then you
[4:35] can go to volume and you can do import open VDB so your VDB file will come in here and you have
[4:41] those simulations and you can set them up here in your little sort of cloud settings here and you
[4:47] can load the frames so you say sequence and frames and it's going to come in as an animated
[4:51] limbic so if I move this off the side we can see those are two different simulations by
[4:56] themselves so we can we can separate that all out and see what this kind of consists of so I'll
[5:02] bring those back together and maybe I'll just disable them for just a second here and show some
[5:08] of the other layers of what this sort of consists of so I have a couple different things here I have
[5:12] a low resolution skull which is the kind of remeshed high-res skull so originally this was
[5:18] sculpted with sort of VR and adding details and stuff like that but I also have a low res one
[5:24] that I remeshed so you can remesh stuff using a remesh modifier same with Maya same with Houdini
[5:30] whatever workflow you're using it's nice to have a sort of low resolution version because well
[5:35] especially for rendering and iterating quicker you don't want to you know have to sort of calculate
[5:40] all of those extra triangles and all the detail that's going to be captured so this is what I do
[5:45] when I'm iterating I have a low res and I'll work that way so if I disable that for a second we
[5:49] even have another layer inside which is also sculpted so this was sculpted in Adobe medium so we
[5:56] can see this here and yeah you can check it out Adobe medium if you have a Windows Beards free
[6:02] and it's pretty awesome I mean it's pretty self-explanatory it's a sculpting software but it
[6:08] doesn't have the sort of learning curve or the upfront cost of time of like learning Z brush so
[6:13] you can really just hop in there and do quite a lot of stuff and it's kind of more intuitive so I
[6:18] think that these sort of workflows in the future are going to completely replace softwares like
[6:24] Z brush in my opinion so unless they sort of adapt and create something that's compelling but if
[6:30] you actually go in here and you sculpt with your hands it's a much more intuitive experience it
[6:34] makes a lot more sense to be working in three dimensions in a virtual space than working
[6:39] on a flat screen especially with when you're dealing with 3d forms in my opinion so that's kind
[6:44] of how these were done so these were kind of sculpted on the inside and the reason for doing
[6:50] this is because if you look at quartz there are multiple cracks and stuff like that that kind of
[6:56] makes something look more quartz like so if I go down to like this picture here this is this is
[7:01] just the pure glass render so I kind of rendered this in different layers here and so if we just
[7:07] look at that that's kind of what the that gives you so yeah we get we get sort of parallax we
[7:13] get sort of these different layers of cracks and detail on the inside which is going to give it a
[7:20] little bit of a nicer look than just like chucking on a glass shader so you really want to add that
[7:26] inside details you can see the bubbles inside and stuff like that and it's very simple you don't
[7:29] have to do any kind of procedural noise or anything like that to try to get in there you can just
[7:35] kind of sculpt it if you go into Adobe medium so that's how that was done and we'll go back to
[7:42] Blender and let's just enable our preview layer again we can also check out some of the lighting


### Lighting [7:51]
**Transcript (timestamped):**
[7:51] and how this was done so I'll just switch on ray trace real quick and I'll show you guys basically
[7:57] the way I approached this scene for lighting so first I'll show the camera because that relates to
[8:03] the lighting I basically parented a camera to an axis in the center of the world so we have an axis
[8:09] that is rotating 360 degrees and the camera is kind of parented to that and that gives us yeah
[8:17] basically just a rotation and the reason I did it that way I just found it easier to light to kind
[8:22] of you know place my lights that work from every angle so these these squares back here are different
[8:26] area lights and I lit this based on you know what looks good from different angles and trying to
[8:32] consider the where the highlights roll off so if you look at the original render if you pay
[8:40] attention to the sort of rim light on the edge we always want to read the silhouette on the shape
[8:45] so you don't want to lose sort of the like this what you don't want this to be black here because
[8:49] you can't really read that does a shape so the lights are placed intentionally to sort of catch
[8:53] the glancing angles but also not be too front lit as well so it's it's tricky to light something as
[8:59] pure glass but it is something that's kind of interesting to think about and the other thing is
[9:04] I placed a light directly behind this the glass here and that kind of gives it that sort of a
[9:10] sub dermal refraction I suppose like coming through on that angle so if you look at it on the on a
[9:16] sort of more final result you know we get that sort of a kind of ghostly kind of light that's just
[9:23] sitting right behind it only appears just at the start but it kind of gives us some interest but if
[9:28] you pay attention again to the sort of highlights as we rotate around you see we're always getting a
[9:33] rolling highlight on the edge to try to read the silhouette and that was kind of an intentional
[9:37] decision I just thought that looks kind of interesting to continue to read the silhouette
[9:41] versus it getting too dark so those are the kinds of things that I'm thinking about when I'm lighting
[9:47] something like this so some other things this was split into multiple different renders so if I show
[9:56] you some different renders here we have just the glass without the simulations inside and this was
[10:03] just done as a base render to iterate off of you can apply different effects to this and stuff like
[10:08] that so yeah I have like a base render here and I also did a base render of the basically the same
[10:17] glass without the high resolution model so like I showed you there's a low res and a high res model
[10:24] I did a low res render which gives a little bit smoother surfaces which I kind of like on some
[10:29] spots and maybe not on others because sometimes there's a little bit too much detail in some of
[10:35] these areas like here it gets a little bit noisy on the chin I kind of like the noise because it
[10:40] gives it some nice detail in terms of the like little divots in the in the surface but sometimes
[10:46] you just want to smooth it out so you can have those two renders and kind of just mix them together
[10:49] in nuke so this is what is beneficial of kind of rendering out different passes and layers you can
[10:56] just mix and match wherever you want using P mats so we'll talk about that a little bit later on
[11:02] but yeah so we have like the storm inside of the lower as one here and the high res without
[11:08] anything so we have all these renders to play with and that's kind of how we go about it now for
[11:13] the lighting of the basically let's go back and turn off the skull layer again so for the lighting
[11:25] of the storm it's basically just some lights on the inside here and some blue lights and I placed
[11:33] two different lights inside there and basically what that gives you is two renders like this so I
[11:41] render those out again as separate renders so we have one light in the center of the storm like
[11:48] this and we have another light that's kind of on the back and the reason I did that different let
[11:54] me show it here so here's render one here's render two so we have these two renders that we can
[11:59] combine by simply plusing them together and now the reason for doing this is because we don't want
[12:07] to animate the lights in 3d it's really inconvenience to animate lights in 3d because you can't change
[12:13] the timing after you've done it so you're you know you don't have as much control to preview what
[12:20] you're doing in 3d unless you're working in a real-time renderer and in this case there's no way
[12:24] you're gonna do this in real time because this is being rendered through glass and stuff like that so
[12:28] it's faster to do this in compositing still so you render the lights without any flickering at all
[12:33] and just let it play through and now that we have that we can basically just control those lights
[12:39] independently so if I were to go here and put a grade here on this light to render I can gain
[12:47] this up oops gain it up like this and you see I can flicker just the backside independently from
[12:53] this one so if I want to make it look like there's lighting in there we have really a lot of control
[12:57] here to just kind of play with this and what you can do is you can use an expression to create
[13:04] that flickering so rather than we don't want to go here and manually grade this and then go to a
[13:08] different frame and grade it down it's not a very efficient workflow so what you want to do is put a
[13:12] grade node and we can put an expression in here so this is add expression and you can either type
[13:17] an expression or you can use something like this which is an expression generator so you can find
[13:22] this on Nucopedia expression generator and essentially what you can do is we have our grade
[13:29] node here and we have our expression generator and you see this little box that's blue it says
[13:34] result we can basically just control drag that down into one of the either the gain or the multiply
[13:40] and that's gonna like animate our thing kind of flickering so if we just look at that I'm kind
[13:46] of a raw result here without the composite let's just plug it in and brighten it up a little bit so
[13:52] here's the backlight put another one here for the sort of one we're gonna use for expression double
[13:58] click the expression generator and we'll drag the result into the the gain so it's control drag
[14:03] and now basically you're gonna see that it's automatically flickering and maybe it's not
[14:09] flickering enough so what you can do is we can shorten the wavelength so it goes faster so that's
[14:15] gonna make it go a little bit faster and then we can change the min and max value if you want to
[14:19] make that amplitude a little bit more or less so you want the flicker be more tense so we can make
[14:25] the wavelength very short and we're gonna get a constant flicker which is gonna be similar to our
[14:29] lightning effect so it's not perfect to every single lightning bolt but I actually didn't want
[14:34] that I didn't want every single lightning bolt because I wanted to maintain sort of a consistent
[14:39] level of blue light inside because I like I didn't want to go pure black basically or go dark in
[14:45] any frame so this approach was what I wanted to use for the flickering of the lightning and yeah
[14:52] that's basically it for that part so we can talk about the specific lightning bolts in this now
[14:57] so these are just some grades and stuff and expression like I just showed to get it to flicker
[15:02] you just combine them together now we have two flickering lights on the inside for for that
[15:06] effect next thing we can do is basically just do some glows and you know kind of the standard
[15:12] nuke stuff you know just do a key pull out the luminance and pre multiply that and then you
[15:18] could put an exponential glow and kind of glowed out and plus it back over so we can start to add
[15:21] a little bit glows on there and we can grade this up with tiny bit more and so we can see it and so
[15:27] that's kind of what's going on here there were some artifacts in this render I think it was like
[15:31] sort of inter-painting on the model so I actually ended up just painting those out but anyways we
[15:36] get this kind of result and we'll step down to the lightning portion so this is the lightning


### Lightning Bolts [15:45]
**Transcript (timestamped):**
[15:45] portion so basically what it consists of is we're taking our render and we're doing a we're
[15:51] shuffling out our UV map here and basically it just helps us see what we're doing and then we can
[15:58] use an ST map and what I'm ST mapping is a bunch of these sort of lightning patterns from the
[16:03] Compositing Academy look dev library so this makes it faster to basically create lightning patterns
[16:10] there's another way to create lighting lighting patterns that I kind of was playing around with
[16:14] to see if this would be interesting workflow and comp to do it but there's so many lightning bolts
[16:19] that happen that it would be a little bit time consuming and to do it this way so you can also
[16:24] use the node called X Tesla which is custom node again newopedia and you can get these really nice
[16:31] lightning bolts and most of the time this is a really great node and you can get some really
[16:34] specific great looking lightning and there's all kinds of settings that that were built into here
[16:39] so yeah Xavier Martin created that and it's probably still the best way to like make an individual
[16:46] lightning ball I think but if you're trying to do like a ton of lightning this pattern really
[16:51] helps and I kind of like using this workflow so if you guys are taking Duke 606 the class I put
[16:57] out there on CG composing we did use this lightning in that class a little bit and so it's a very
[17:02] similar technique but we do go a little bit more in detail on that class but this this workflow is
[17:07] kind of similar so essentially what we're doing here is we're taking these lightning patterns
[17:11] and we're ST mapping it to the surface of the skull so basically we get something like this we
[17:17] get this like lightning jumping around so if I just switch it we get something kind of crazy
[17:22] like this now this isn't going to work off the bat because it's on the surface and we want it to
[17:27] look like it's actually inside so really we just need to do some kind of comp trickery here to make
[17:32] it look like it's actually in the depth of these sort of clouds so because we don't have we don't
[17:38] want it to look like there's lightning on the surface rather they're kind of on the inside so
[17:42] it's a very simple trick basically what you do is you just key this image and you you mask the
[17:49] lightning to the inside of that kind of shape so essentially what I'm saying is we have our
[17:56] lightning and we just want the lightning to be only in the bright parts so we want the dark
[18:00] parts of the cloud to cut out the lightning and you could add some lightning bolts in the dark
[18:05] areas if you want but you'd have to kind of add detail back if there's no detail because if a
[18:10] lightning bolt lights up lightens a cloud you're going to start to see more detail in the cloud so
[18:15] if we're comping the lightning in and you want to have a lightning bolt that's in an area that has
[18:19] no detail for those frames you'd have to add like a noise texture in front or something like that
[18:25] because you wouldn't have any detail to key out so it's easier to just yeah stencil the darkest
[18:32] parts out and hide the lightning into the into the brighter areas and what that does is something
[18:37] like this so let's just look at it so it's going to look like the lightning is happening inside
[18:42] rather than on the surface because we never see it kind of going across all all the glass up top
[18:48] so it's being masked by again just to reiterate that we have like the the brighter parts and we're
[18:55] just masking the lightning that was ST mapped to the skull and then we kind of have something that
[19:03] looks like this if I just look at that layer by itself one other thing I did to make it a little
[19:08] bit more random as well was rather than just a pure mask on on the entire thing like what I'm showing
[19:15] I did do a separate mask of roto paints so I did kind of manually go in there and paint some of the
[19:22] lightning bolts to be masked so what I'm saying is I would go here and I would take a roto paint
[19:28] and just like you know paint one in like this if I want a lightning bolt to appear in a certain
[19:33] spot and that would go to the next frame and then paint another one if I want it and it just adds
[19:37] a little bit more randomness because if I just leave all the lightning on and then I mask that
[19:41] it's maybe it's just a little bit too much because then you have like constant crazy stuff so I just
[19:46] wanted to have it a little bit more controlled so that's what the roto paints are for so it's
[19:52] really just yeah masking it and yeah it really helps to get sort of a crazy lightning effect with
[19:58] with these different patterns here so if you guys are interested in that you can find it on the
[20:02] website so there's a pack with 200 simulations and you can use them for different stuff so I've
[20:08] been using them for a variety of use cases so once we have that we have the basically the main
[20:15] portion of our skull done now we have like the storm in there and we have like the lightning
[20:19] bolts one other thing with the lightning bolts I forgot to mention is you know we want to have
[20:24] a bounce light coming off of those lightning bolts so if there's a lightning bolt here we
[20:28] wanted to bounce into the region around it so that's just a blur basically so if we look at this
[20:33] and then disable these two nodes just above yeah if we were just plus the lightning on it looks


### More Details [20:36]
**Transcript (timestamped):**
[20:40] kind of like that but actually what we want to do is kind of make it more isolated around so it
[20:46] feels like the light is casting on the areas around so it's a cheat because we don't have that in
[20:51] our CG so yeah it's pretty much just you know just key or lightning blur it out a little bit and
[20:58] same thing mask it behind the darker areas and then we can use that alpha as being created either to
[21:06] kind of gain up or gain down those different areas so I'm using a multiply here to kind of yeah
[21:13] brighten this area here and this technique with a constant and sort of you know taking bright
[21:19] things and putting them over a white and then sort of multiplying that's in nuke 606 as well so
[21:25] some of these techniques are yeah you may have seen them before if you've taken some of the advanced
[21:29] classes so that's kind of the idea and let's continue down some roto paints here that kind of
[21:37] fix some of the little edge stuff we have these weird little triangles so basically I just kind
[21:41] of like painted those out and fix that up this thing here we have some frame range and time clips
[21:48] so if you looked at the render you'll notice that it actually loops so we have this render and by
[21:55] the end of it it starts on the first frame again so our simulation our smoke simulation you can't
[22:01] really loop a fluid that easily I think Ember Jen does have some settings for it but just for ease
[22:06] what I did was essentially rendered like 20 extra frames beyond the last frame so I rendered if
[22:13] you see my mouse here on the last frame I kind of rendered it like an extra portion here and that
[22:18] allows me to dissolve between the last frame and getting back to the first frame seamlessly so
[22:23] really want to dissolve between those two videos to get a perfect loop and if somebody wants me to
[22:29] do like a longer tutorial maybe on like how to make something loop I can do that but I want to make
[22:34] this video specifically too long but really it's just rendered the extra frames you can do you can
[22:39] kind of time offset and then use it dissolve to blend between two videos so stepping down further
[22:47] we have this glass sorry this storm here that was rendered through the low resolution skull so
[22:55] doesn't have that much distortion on the surface so I wanted to add a little bit more so what I did
[22:59] is a glass node to just kind of roughen up those edges a little bit to make it feel like it's even
[23:03] more inside and that will kind of distort our lightning bolts as well so as this rotates around
[23:09] it'll just feel like everything's really inside the glass and I'm using the the glass render I did
[23:14] to use as a distortion map so it's basically just the alpha of this through a glass node and that
[23:21] kind of will mess up the edges which is what we want so continue down a little bit of fake bounce
[23:30] lighting on the inside as well this just kind of helps it not be completely dark and helps the
[23:35] edges a little bit so all that is is really just taking let's see what is it we have basically I
[23:42] guess it looks like we just kind of darkened the main effect and then kind of blurred it out and
[23:48] masked it sort of by the alpha itself so yeah so it's kind of just blurring the highlights a
[23:56] little bit and kind of mixing it in and that just kind of helps us read our silhouette a tiny bit
[24:01] more which is pretty nice and then we can kind of plus on the glass effect which gives us something
[24:07] like this getting our main highlights in there so we have our our pure glass render that's been
[24:14] darkened like this glass render darkened we plus it on and now we kind of get that pieces on top
[24:23] then we can continue on to refine the CG after that so we can go to like the front for example I
[24:30] thought the eyes were a little bit dark so what I did was I kind of boosted those eyes up a little
[24:34] bit and that's just using P mats so I can use a P mat node from Nucpedia and we have our position
[24:40] pass that's with our render so we can just like create basically yeah the two I areas and we can
[24:47] use those as masks to brighten up the centers and we have some glows and all that kind of comp
[24:55] stuff at the end so a little bit of a sharpen in log space so you usually want to do your
[25:00] sharpens in log space so what you do is you take a log to Lin node say the operation Linda log so
[25:08] it's very flat and gray like this you do your sharpen and then you convert it back so the last
[25:13] one says log to Lin and that will give you better results than if you just put a sharpen
[25:17] directly on your image like that so usually want to do those kind of sharpening in log space
[25:22] and a little bit of volume raise at the end as well so one thing to note with a volume raise that
[25:30] might help some people out this image was eventually scaled down later on so I needed to have some
[25:36] overscan so there's a bunch of overscan here so I think I scaled it down quite a bit but one thing
[25:41] to note with volume raise node is if you just do it straight out of the box it's gonna crop your
[25:46] image which is not ideal so what you can do is actually double click the volume raise node and
[25:52] you can go up to the little node button here and you can say copy to group and that will make a
[25:57] copy of it but it's a group node instead of a kind of a locked off node so it says group it's doing
[26:02] the same exact thing but if you hit control enter you can actually go inside that node and see
[26:06] everything that's happening here and really what you just want to do is go in here and disable the
[26:10] crop node and that will just give you a little bit of your overscan which is what we're gonna need
[26:16] here in terms of yeah just kind of making that work because we don't want to lose the pixels
[26:22] outside so this is a huge bounding box here so we can probably you know it's you know not ideal
[26:28] you want to put a crop after that so you don't have that many pixels because that's not gonna be
[26:32] good so I put a crop after but you'll notice the crop after maintains a little bit of that overscan
[26:39] so that's basically one thing you keep in mind and yeah so this is the sort of final result with
[26:48] all of those changes techniques of different renders and I think that's basically it so if you guys
[26:55] have any questions feel free to leave it in the comments below make sure to hit the like button
[26:59] if you liked the video if it helped you out and appreciate it



---

## Captured Frames

- [0:59] tutorials/frames/stormy-crystal-skull-nuke-blender-ai-embergen-mixed-vfx-medium-part-2/frame_000.jpg
- [4:22] tutorials/frames/stormy-crystal-skull-nuke-blender-ai-embergen-mixed-vfx-medium-part-2/frame_001.jpg
- [9:56] tutorials/frames/stormy-crystal-skull-nuke-blender-ai-embergen-mixed-vfx-medium-part-2/frame_002.jpg
- [13:52] tutorials/frames/stormy-crystal-skull-nuke-blender-ai-embergen-mixed-vfx-medium-part-2/frame_003.jpg
- [16:03] tutorials/frames/stormy-crystal-skull-nuke-blender-ai-embergen-mixed-vfx-medium-part-2/frame_004.jpg
- [18:42] tutorials/frames/stormy-crystal-skull-nuke-blender-ai-embergen-mixed-vfx-medium-part-2/frame_005.jpg
- [23:03] tutorials/frames/stormy-crystal-skull-nuke-blender-ai-embergen-mixed-vfx-medium-part-2/frame_006.jpg
- [25:52] tutorials/frames/stormy-crystal-skull-nuke-blender-ai-embergen-mixed-vfx-medium-part-2/frame_007.jpg

---

## Structured Notes

### Core Technique
Building a "crystal skull with an internal lightning storm" CG element by rendering many separate, deliberately simple CG passes (glass, storm, two independent point-light passes) and doing all of the actual "art direction" — light flicker, lightning placement, internal-vs-surface depth cheating, edge distortion — in Nuke compositing rather than in the 3D renderer.

### Summary
Part 2 of the "Stormy Crystal Skull" project (continuing Part 1's "frame" build). The CG side is fast: EmberGen simulates smoke/storm inside an imported FBX skull collider (two sims, one emitting from center, one from the back, to fill the skull evenly) exported as VDBs (frame_000); Blender loads the VDBs (Shift-A → Volume → Import OpenVDB) alongside a high-res and a remeshed low-res skull, both containing extra crack/bubble detail hand-sculpted in Adobe Medium VR (frame_001) rather than procedurally, because sculpted interior cracks read as more convincingly "quartz-like" than a glass shader alone. Lighting uses a camera parented to a rotating axis so the same fixed area lights read correctly from every angle, with a rim/silhouette-read priority (never let the glancing edge go fully black) and one light placed directly behind the skull for a sub-dermal glow. Everything is deliberately split into many separate un-animated renders (base glass high-res, base glass low-res, storm-lit-from-center, storm-lit-from-back) so that all animation — light flicker, mixing high/low-res detail, blending render layers — happens in Nuke instead of 3D, because iterating on lighting timing inside a ray-traced glass render is too slow. The two storm-light renders (frame_003 shows one, a raw blue glow) are combined with Merge (plus) and independently flickered using Grade nodes driven by the Nukepedia "Expression Generator" gizmo (control-drag its `result` output into a Grade's gain knob), with wavelength/min/max tuned for a fast, high-frequency flicker rather than a naturalistic single-strike look, because the author wanted the interior to never read fully dark. Lightning bolts (frame_004) come from ST-mapping pre-rendered lightning-pattern footage (from Compositing Academy's own look-dev library) onto the skull's UV pass, then masking the ST-mapped lightning so it only shows through the bright parts of the storm render — making surface-projected lightning read as if it's happening deep inside the volume (frame_005). RotoPaint is layered on top of the mask to hand-place individual bolts for a less uniform, more random-feeling strike pattern. A blurred, keyed-out version of the lightning creates a cheap bounce-light glow around each strike. Later passes: a Glass-node edge distortion (using the glass render's own alpha as a displacement map) to make the lightning/storm feel like it's refracting through uneven glass rather than sitting on a flat surface (frame_006); fake interior bounce light (darken + blur + alpha-mask the main effect, Plus it back); PMatte-driven eye brightening from the position pass; log-space sharpening (Log2Lin → Sharpen → Lin2Log) for better results than sharpening directly in display space; and a VolumeRays node worked around via "Copy to Group" + disabling its internal Crop node, to preserve overscan pixels needed because the final image was later scaled down (frame_007 shows the finished glowing-comet-like lightning result).

### Key Steps
1. **EmberGen:** near-default force+noise smoke setup, sphere emitter, FBX skull imported as a collider; run two separate sims (front-emitting, back-emitting) so the whole skull fills with smoke; export both as VDB sequences — temporary EmberGen lighting is discarded because true glass refraction/ray-tracing needs to happen in a renderer that actually ray-traces (Blender), not EmberGen's real-time preview.
2. **Blender:** import VDBs (Shift-A → Volume → Import OpenVDB); keep both a high-res sculpted skull and a remeshed low-res version for faster iteration; hand-sculpt interior crack/bubble detail in Adobe Medium (VR sculpting) rather than procedural noise, since real quartz reads convincingly mainly from internal fracture detail; light with a camera parented to a rotating axis + fixed area lights placed to keep a rim highlight readable at every rotation angle, plus one light directly behind the object for sub-dermal glow; render many separate un-animated passes (base glass hi-res, base glass lo-res, storm-lit-front, storm-lit-back) instead of one animated composite, specifically to push all timing/animation decisions into Nuke.
3. **Nuke — combine and animate the two light passes:** `Merge` (plus) the two storm-light renders; add an independent `Grade` per light with an expression-driven `gain`, generated via the Nukepedia **Expression Generator** gizmo — control-drag its `result` knob into Grade's gain, then tune wavelength (shorter = faster flicker) and min/max (amplitude) so the interior stays lit rather than going to black between strikes.
4. **Nuke — glows:** key/pull luminance from the flickering light layers, premultiply, run an exponential `Glow`, `Plus` back over the main chain, `Grade` up slightly to taste.
5. **Nuke — lightning bolts:** `Shuffle` out the render's UV pass; `STMap` pre-made lightning-pattern footage (Compositing Academy look-dev library asset pack) onto the skull surface using that UV pass. Alternative/complementary tool named: **X-Tesla** (Nukepedia, by Xavier Martin) for generating individual bespoke lightning bolts — preferred for single bolts, but too slow for "lots of simultaneous lightning," which is why the ST-map-library approach was used here instead.
6. **Nuke — fake internal depth for the lightning:** the ST-mapped lightning initially reads as sitting on the surface; fix by keying/masking it so it's only visible through the bright regions of the storm's own render (dark cloud areas cut the lightning out) — this alone sells "lightning happening inside the volume" instead of on the glass surface. Layer hand-painted `RotoPaint` masks on top to selectively re-enable/disable specific bolts frame-by-frame for a less uniform strike pattern than the raw ST-mapped layer gives.
7. **Nuke — bounce light from the bolts:** blur a keyed/masked copy of the lightning layer, mask it to the dark cloud regions, use it to `Multiply` (brighten) the surrounding area — cheap, comp-only fill light that has no equivalent in the CG render.
8. **Nuke — seamless loop:** render ~20 extra frames past the simulation's natural end, then `Dissolve` between the tail and the head of the render to hide the loop point (fluid sims can't trivially self-loop).
9. **Nuke — edge distortion:** feed the alpha of the low-res glass render into a `Glass` node as a displacement source, applied over the storm/lightning composite, so refraction-like surface noise reads on the lightning as the skull rotates — reinforces "this is inside solid glass," not a flat overlay.
10. **Nuke — final polish:** fake interior bounce (darken + blur + alpha-mask the main effect, `Plus` back over); `PMatte` (Nukepedia) driven by the position pass to isolate/brighten just the eye sockets; log-space sharpen (`Log2Lin` → `Sharpen` → `Lin2Log`, better result than sharpening directly in display-referred space); `VolumeRays` handled via right-click → **Copy to Group** (converts the locked node into an editable group) so its internal auto-`Crop` can be disabled, preserving the overscan the shot needed since the final image was later scaled down — re-`Crop` afterward to a sane bounding box rather than leaving the huge overscan canvas in place.

### Nodes / Tools / Settings
- **Core Nuke:** Shuffle, STMap, Merge (`plus`), Grade (`gain` driven by expression), Glow (exponential), Blur, RotoPaint, Dissolve, Glass (distortion via alpha displacement), Log2Lin/Lin2Log (`operation` toggle for log-space sharpening), Sharpen, VolumeRays (+ "Copy to Group" trick to disable its internal Crop), Crop, Multiply merges for bounce-light gain
- **Nukepedia gizmos:** **Expression Generator** (drag-and-drop animated-value driver, used here for light flicker via a Grade's gain), **X-Tesla** (Xavier Martin — dedicated single-bolt lightning generator, mentioned as the better tool for individual bolts vs. this video's ST-map-library approach for mass lightning), **PMatte** (position-pass-driven region isolation, used to brighten the eyes)
- **Cross-app / non-Nuke:** EmberGen (smoke/storm sim, VDB export), Blender (VDB import, remesh modifier, area-light rig on a rotating-axis-parented camera), Adobe Medium (VR sculpting for interior crack detail — author predicts VR sculpting workflows like this will eventually supersede flat-screen sculpting tools)
- **Asset source:** Compositing Academy's own "200 lightning simulations" look-dev library pack (ST-mapped footage), referenced as available on the channel's website
- **Cross-reference:** the flicker-expression and constant-over-white-then-multiply bounce-light techniques are both noted as covered in more depth in the author's paid "Nuke 606" course

### Difficulty
Advanced — no single node is exotic, but the overall approach (deliberately under-baking the 3D render into many static, un-animated passes so that *all* timing/animation/detail-blending happens in comp) requires production-level judgment about what to solve in 3D vs. 2D.

### Foundry App & Version
Nuke for all compositing (majority of this video's runtime and the reason it's extracted fully here); EmberGen for the storm simulation and Blender/Adobe Medium for the CG asset are cross-platform prerequisites, not covered in depth. Nuke version not stated on screen; per this skill's version-tracker, a 2022 upload falls in the 13.1 (Nov 2021) → 13.2 (Apr 2022) window. Uses only Classic-3D-era passes (P Matte position pass, UV pass) — no USD-specific nodes, so unaffected by the 14.0-beta 3D-system overhaul.

### Tags
compositing, merge, channels, st-map, gizmo, grading, fx-simulation, lighting, advanced

---

## Related Tutorials
- Mixed Medium VFX P1 | Blender, Nuke, Ai, Embergen, VR Tutorial (`mixed-medium-vfx-p1-blender-nuke-ai-embergen-vr-tutorial.md`) — direct prequel (Part 1); covers the AI-concepted "frame" element for the same overall Stormy Crystal Skull piece using a related 2D→3D→2D Nuke/Blender pipeline. Read together — Part 1 explains the frame surrounding this skull, this video explains the skull itself.
- Build Entire FX with ONE Pass - Nuke Tutorial (`build-entire-fx-with-one-pass---nuke-tutorial.md`) — shares the "isolate a region via a position/ID pass, then multiply/mask to fake extra CG detail entirely in comp" philosophy (there via World Position AOV, here via P Matte on the position pass), and both push flicker/animation into expression-driven Grade nodes.
