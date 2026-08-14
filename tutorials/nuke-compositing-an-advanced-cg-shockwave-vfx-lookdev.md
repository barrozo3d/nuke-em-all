---
title: Nuke Compositing an Advanced CG Shockwave | VFX (LookDev)
source: YouTube
url: https://www.youtube.com/watch?v=ErwClH-dQA0
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke / NukeX (deep compositing requires NukeX)"
version: "Nuke 13.x (13.1/13.2 — exact 2022 point-release not stated)"
tags: [compositing, 3d-system, deep-compositing, st-map, projection, gizmo, fx-simulation, grading, expert]
extraction_status: complete
frames_dir: tutorials/frames/nuke-compositing-an-advanced-cg-shockwave-vfx-lookdev/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Nuke Compositing an Advanced CG Shockwave | VFX (LookDev)

**Source:** [YouTube](https://www.youtube.com/watch?v=ErwClH-dQA0)
**Author:** Compositing Academy
**Duration:** 30m29s | 9 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey everyone, welcome to this tutorial. This time we're going to talk about how to create
[0:13] this advanced shockwave that you guys might have seen me post in the last couple posts
[0:18] on the channel. So we're going to kind of talk about this and how I use some of the
[0:22] elements that I just released as a library to kind of kitbash this sort of thing together.
[0:28] So this is the effect. I'll just let it play in case you guys haven't seen. We have this
[0:33] ball kind of dropping down and in, and then we have like this huge kind of shockwave explosion
[0:39] and sort of this refractive thing happening. And there's sort of a couple levels of complexity
[0:46] to this explosion. It's not simply like a 2D element. That's not going to work. So just
[0:52] to point out some of the levels of complexity in this, if I pause on maybe one of the explosion
[0:57] frames here, we can see that first of all, we have obviously this very bright over exposed
[1:03] center here where we're losing detail. And this is an important part of I guess composing
[1:10] is like losing details really important. And knowing where to maintain or lose it as part
[1:16] of the photographic quality of something is something you want to consider. So that's
[1:21] kind of something we have happening in center, but we also have a couple of different variations
[1:25] of color happening. And then we also have this like huge explosion with sort of these
[1:31] like manifolds of, I guess, like additive sort of overlapping ripples that give it this
[1:37] sort of quality. So it's not as straightforward as just, you know, using an eye distort and
[1:43] kind of, you know, putting it over the scene. So I'm going to talk about how I did this
[1:48] and how I use the elements. And also why I call it kit bashing. So it really is a lot
[1:55] of the elements combined, but you'll see how I'm working with them. And I think that this
[1:59] is probably something that's maybe not understood directly when you're looking at the energy
[2:05] effects library that releases, it's not meant to just be something you take and you just
[2:10] slap it over your footage and you're done. Really, there's a certain way you can actually
[2:14] work with these. And I think it's actually sort of a new way of working. I also think
[2:19] it's sort of combining an old way of working, like kind of the lost art of some of the people
[2:25] you know, like an after effects, the way they composite and they use patterns is something
[2:29] that I think is almost kind of a lost art. You see some people doing it, but not that
[2:34] many people are doing it. So yeah, I think that having this library is really useful.


### Energy FX Library [2:35]
**Transcript (timestamped):**
[2:39] And if you want that, by the way, you can get it here. So it's on the website, composite
[2:44] Academy slash energy effects, FX in the domain. And then you can see basically 200 simulated
[2:52] effects for look development. So put this back. And we'll look at this next is a video
[2:59] I'll show you guys next of how I actually use some of these elements to generate some
[3:03] of the lens flares and the lens artifacts. So these are these elements, even though it's
[3:08] called the energy kind of effects library, really, it's just a bunch of patterns, and
[3:12] you can do anything that you can do with a pattern. So that's like part of a big part
[3:18] of all of these lens flares. And that sort of refractive quality is also coming from
[3:24] those elements. So I'm going to talk about the main part here first, which is this. Let
[3:31] me just zoom here to my shockwave. So this is the main shockwave event. So we have this
[3:39] pass that I created. We have all that kind of glassy refraction happening in there. And
[3:45] it's kind of scaling scaling up and going across our scene. And then we also have the
[3:51] second part. So there's kind of a two parts to the main shockwave. There's like this bubble
[3:56] that kind of comes. But we also have where the bubble is contacting the geometry. So I
[4:02] created kind of like an electrical pass that is utilizing another element. But we're revealing
[4:10] it across the geometry where the shockwave is touching. And if you look at the final comp,
[4:15] go back to the final comp, you can see it gives it that quality of it feels like something is
[4:21] truly kind of traveling along the surface. So even though it's split into two elements,
[4:26] it looks like one whole event that's happening together. And so let me just go back to that.
[4:33] So I guess I'll explain the contact point first just because I'm already at this part of the
[4:37] script. So essentially what this is is we have this element from the pack from the library. And
[4:44] you can notice that it's actually a circle. And that's not going to work for our situation. But
[4:49] one thing with this library is that they're 4k. So you can basically bend them, you can warp them,
[4:56] and you're going to maintain a certain level sharpness. And you can kind of rewrap the
[5:01] amount of geometries in different ways. So in this case, we have a circular kind of portal,
[5:07] which could be used for a multitude of things. But in this case, I unwrapped it into a straight,
[5:14] kind of linear pattern. So we have a node here called polar distort. This is from
[5:18] Nucopedia. You can do the same thing with a spherical transform node. I just don't like
[5:23] messing around with all the settings here. There's a bunch of stuff you have to memorize. And
[5:26] I'm a little bit lazy with that. So I just keep the polar distort, chuck it on whenever I need to
[5:30] unwrap or rewrap. So what that does is you can wrap circles into basically straight lines. And
[5:37] that allows us to take the circular pattern, put it into a linear pattern. And what we can do with
[5:43] that is ST map it to our scene. So again, the ST map covered as many times in some other videos,
[5:50] you can go check them out with UV passes. But basically, we have a UV pass for this environment.
[5:56] And we're wrapping this new effect. And as it kind of spreads, if I just like kind of play upward,
[6:02] this thing will kind of expand across our scene. So we have the pattern ST map to it,
[6:11] which is going to give us something kind of everywhere on the geometry. So if I just look at
[6:18] that, and give it a second to load here, we can see that that's kind of wrapped on the whole
[6:29] scene. But we only want this texture to appear where the shockwave is touching. So the way I did
[6:35] that was I essentially just used P mats. So I use the P mask node again from Nucopedia,
[6:42] you can grab it, I'll just type it in. There's other ones as well, I just use this one. They all do
[6:47] the same thing basically. But yeah, so basically, I expand this mat at the same time as the shockwave.
[6:53] So we have this black and white alpha that is going to reveal our quote unquote kind of contacting
[7:00] energy effect. So this effect is only going to appear on the edges. And that will just give us
[7:06] that like kind of leading edge of the effect that's spreading. So that's basically how that was done.
[7:11] I know that's a quick overview. And I'm not covering every single node, but this is a more advanced,
[7:17] I guess, tutorial. So I'm not going to cover every single node, because the videos will just end
[7:21] up being way too long. I'd rather cover the concepts. And if people have a specific question,
[7:26] I can maybe try to answer it. But I think covering the concepts and the way to think about approaching
[7:33] a visual effect is actually maybe more useful than just like a specific node. And one other thing
[7:40] I can I guess mention here just to point it out is I did use some crypto mats to isolate certain
[7:47] areas and kind of mix in texture a little bit differently. And that's because if you just slap
[7:54] on this whole effect with an ST map, the way the UVs are mapped on different pieces of the scene,
[8:00] you know, you might have a little bit of texture that's stretched too far or too big. So what you
[8:05] can do is sort of ST map it differently. So you kind of scale this thing up and down. And then
[8:11] just kind of key mix that between different pieces of the geometry of the scene, if that makes sense.
[8:17] So essentially, we're just taking mats of different pieces, and scaling that effect for each piece
[8:22] so that it doesn't look stretched and stuff like that. So that's kind of a very quick and simplified
[8:29] version of I guess the explanation of that, but hopefully that makes sense. So you can see how


### Compositing the Shockwave [8:35]
**Transcript (timestamped):**
[8:35] that circular element became something totally different. And that's something I'm really trying
[8:39] to demonstrate with this video. And you'll see again, with this main shockwave, basically the same
[8:45] thing. So it's like an effect, but it looks totally different than the original fact. So I'll show
[8:50] you guys that now. So I'll go up here. One way I like to work with these elements that I discovered
[8:56] after creating them is I just like to load them all in Nuke at the same time. So I chucked them all
[9:01] on like an external drive. So I don't feel my computer with some memory, so throw them on an
[9:06] external drive, and I can just step through. And I just load them all into Nuke at the same time.
[9:11] And I can just find a pattern that suits what I'm doing. So I wanted to make a shockwave. So I
[9:19] found this pattern. And I thought this one was pretty cool. But this isn't going to work to just
[9:25] scale up in 2D towards the camera. It's not going to really give us that that look. And that's
[9:30] actually what I tried originally. I'm like, oh, maybe I could just stick it out in there and kind
[9:33] of scale it. So usually I try to go for the very, very quick solution first. But that's just not
[9:37] going to work because we need that three dimensional quality. So the way I use this element was to
[9:46] so I did some grading here. Let's just see. Go back in time here. So at the right frame. So like
[9:52] this, I used this another element here, this kind of liquid one you saw me use probably in the last
[9:58] tutorial I did. I really like this one just has a lot of depth and layer and you can do all kinds of
[10:03] stuff with it. So I use that as a basically I distort to the other effect. So we have this main
[10:11] effect being distorted by this other liquid effect. I'm using a node called glass, again, another
[10:18] one from New Wikipedia, you can just type it in. It's the same thing as an I distort. But the nice
[10:22] thing about this node is you can I distort the color channels slightly differently. And what that
[10:28] does is it gives us this nice aberration in some of the highlights and gives us that really refractive
[10:32] quality. So we get something that looks like this. But again, we're still working with a 2d sphere here.
[10:39] So now we need to solve how can we make something 2d have multiple layers of depth and have a nicer
[10:46] quality. So essentially what I did was I took a sphere. And we have a sphere here. And I did a
[10:55] apply material. And the reason I use the apply material because we don't want to apply the texture
[11:00] right away because we actually need to change the UVs of the effect that we're trying to apply. So
[11:08] what I mean by that is if I disable this, I guess I could have maybe applied it as a as a texture
[11:14] directly, it's just see. So yeah, let's see that versus. Yeah, I probably could have applied it directly
[11:22] as an image. Let's just see UV project. Yeah, it looks like it does the same thing. So maybe the
[11:27] apply material is not necessary here. But in any case, essentially, what I did was I took the sphere,
[11:33] I used a UV project. And what is this doing? We have the normal UVs of a sphere. So if you look at
[11:40] the way the sphere normally maps the UVs, if we apply like a checkerboard and we look at that, we see
[11:47] it's just kind of wrapping around. But actually what I wanted to do is kind of project. Let's just
[11:54] switch back to the effect quick. It'll be easier to demonstrate what I wanted to do was kind of project
[12:01] this effect on both sides. So instead of having it just on one side wrapping around the whole thing,
[12:08] which you kind of lose the texture almost like I wanted to make it look like a multi layered effect
[12:15] sort of. So by using a UV project, you're basically doing you're changing the way the UVs are mapped.
[12:22] And you can check out the video on UVs I have, I think I have a pretty good description of like what
[12:28] are UVs and everything like that. But I used a planar projection on the YZ plane from an axis. So
[12:37] what is that doing when I move this axis around? Essentially, let's just move it up and down so
[12:43] you can see. So essentially it's doing this is kind of projecting that texture on this plane onto
[12:50] this surface. So we get this double sort of effect here. And after that, I just took a transform
[12:57] geo and merge it over itself. So I rotated it 90 degrees and merge this thing over itself. So we
[13:04] get this effect of like four different, I guess, patterns here and we could time offset them if
[13:11] you want to make them slightly asymmetrical or something like that. In this case, there's so
[13:15] much motion blur and everything that I didn't really bother. But this is like the base of the
[13:20] effect. And then what I did was a displaced geo. So I did a displaced geo with a radial, and I put
[13:27] the radial at the center of this sort of format. And then I use the displaced geo. And what is this
[13:34] doing? Basically, I animated this displaced geo to have a smaller scale towards the start of the
[13:40] scene. So if I go a little bit backwards in time, you'll see that our sphere starts to bend inward
[13:46] towards the center. And I wanted it to feel like an explosion coming from a center point. So rather
[13:51] than just having a sphere scaling up, I did a sphere that displaces from the center outward.
[14:00] So basically, everything is like curving in at the start,
[14:04] like this. And it's just displacing from a radial. And then I just animate that scale off
[14:09] of the displacement. So we can see it like kind of goes more circular as it travels further away.
[14:15] So you see the bend is becoming less as it gets bigger. So if I just skip forward again in time,
[14:21] that displacement reduces over time. So we have like a perfect sphere.
[14:26] And what does that give you? It gives you something that basically looks like this. So we have that
[14:31] kind of weird shape at the start that kind of have these nice like triangle, like almost
[14:36] explosive look. And then it's kind of moving outward, and then becoming more spherical as it
[14:42] expands. And we also have that nice kind of glass effect. I did use some deep compositing here. I'm
[14:51] not going to cover a full tutorial decomposing yet, because I haven't completely dived into those
[14:55] concepts. And that is a pretty deep concept in itself. So that's not what this video is about.
[15:01] But essentially, what it is is just taking a scanline render, taking the geometry of the scene,
[15:08] and doing a deep merge. And that basically allows you to cut out the shockwave from the
[15:14] geometry that it's passing across. So it's basically just a deep merge. I think I used a deep
[15:20] reformat as well to make it faster. I think it was pretty slow. But again, I don't want to get too
[15:25] much in deep on this tutorial, because that's a really, really long topic. I just want to kind of
[15:29] cover the look depth of this shockwave. So yeah, now we have this nice base of this exploding thing.


### Distortion [15:33]
**Transcript (timestamped):**
[15:37] And let's go back to the script and see. So shockwave. And then I did some color grading on it
[15:46] to make it a little bit more blue. Because that goes with the color scheme of our scene. I'm going
[15:52] to talk about a little bit more of the color scheme in a few minutes once I get to that. But
[15:57] yeah, and then just merging this over. Also, I used it as a map for distortion as well. So
[16:04] like we have the scene without it, we have the scene with it. But also I'm using the same
[16:09] effect as another distortion map. So that kind of distorts the background below it like this.
[16:16] And then merging the effect over the top. So now we have all those like layered
[16:19] highlights and that kind of complexity I was talking about, as well as, you know, as it's
[16:24] crossing, we have that all this stuff happening. So let's keep going. Down the script, I'll start


### Lens Layers [16:33]
**Transcript (timestamped):**
[16:33] talking about, I guess, the lens flares now. I'm not going to cover every lens flare. I'll just cover
[16:40] kind of the ones I use the elements in here. So let's just go down. One other part was,
[16:47] I just forgot to mention this. So part of that shockwave, I created another render pass, not a
[16:52] render, but I did this in Nuke. I just took an element and I wrapped it on that same sphere that
[16:58] I created with all that distortion, everything happening, but I put a refractive element on it.
[17:06] So let me go up and just explain that real quick before I move on to the lens flare portion.
[17:13] If I can find it, don't have it properly labeled here and spend a couple of days. Here we go.
[17:19] So here it is. So this is the element I used on there instead. So this is the same sphere setup
[17:26] I just showed you guys, but instead of putting that other material on, I took this element from
[17:32] the library because I thought that it had kind of a glass-like quality to it in a way that


### Color Space [17:33]
**Transcript (timestamped):**
[17:37] things overlap with each other. And I'm going to show you guys a video of a real flare and kind of
[17:42] refractive element in a second here, some footage I took with a drone, just to explain that further,
[17:48] but I want to go over this real quickly anyway. So we have the color space into HSV and I'm doing
[17:55] this sort of trick to make it a rainbow. I have a tutorial on my channel about how to make a rainbow
[18:01] in Nuke so you can find that. So I'm not going to explain this whole concept because that's a video
[18:05] in itself, but essentially we can take a black and white image and we can basically make it a rainbow.
[18:11] And then what I did was I took some of the greens out because I don't want those colors,
[18:17] that very hunter, like, woods green. I didn't want that in my scene. So I'm going to show you guys
[18:22] the color scheme I was working for, but so I just took a little bit of that out. So we have this crazy
[18:26] looking element that we can essentially distort. So I use the same trick there and then I just
[18:33] applied that to my sphere. And then we basically get an element that looks like this. And this is
[18:39] something we can just mix in a little bit to give more of a glassy kind of quality. And you see it
[18:43] gets a little bit low res when it's really, really close to the camera, but it really doesn't matter
[18:47] because the amount of motion blur that's happening here, we can also blur it a little bit more as
[18:52] it comes and fade it off. So this is going to be a really great pass to have as a composer.
[18:59] So yeah, I'm kind of like creating each layer, each pass, but just in nuke, you know, we don't


### Color Scheme [19:03]
**Transcript (timestamped):**
[19:04] need to create everything in CG. So I'll just go down here and start talking about some of these
[19:11] other parts. Let's go to a good frame to demonstrate it. So let's see. So I think this is a good frame.
[19:21] So one of the things I want to mention before I talk about the flare aspect is the color scheme,
[19:26] because this is important. It's always seems to be overlooked in tutorials and stuff like that. You
[19:31] never you never hear composters talking about the art side of compositing, you always hear about,
[19:36] you know, just CG passes and stuff like that. But that's actually not the most important part.
[19:41] So one of the things when you're working on this is not to just start chucking random colors
[19:47] in a scene, you want to come up with a color scheme and try to work within those mental barriers,
[19:52] those artistic barriers. So one of the kind of color schemes I worked in here is I mean,
[19:59] you can see it pretty much at the start of the shot. So we go here, and we have this pretty
[20:03] monochromatic sort of scene, like just basically blue and kind of teals and then the highlights go
[20:09] a bit desaturated. So if we were to like draw that out as a color scheme, just to visualize it,
[20:16] and it does help to do this, let's just draw it out. So we have something like that.
[20:22] We have something a little bit more in the teals kind of teal greens,
[20:27] like that. And then we have some desaturated highlights, maybe make it a little bit brighter
[20:33] for demonstration, desaturated highlights. So this is our main color scheme sort of. But what I
[20:38] wanted to do was rather than have it completely monochromatic was to chuck in some, just some
[20:45] cooler tones, but not completely breaking the image. If I go in the really reds and orange and
[20:49] green, everything is going to look rainbow and it starts to look a bit cheap. Like you have to do
[20:54] that very carefully if you're going to use a lot of colors. And if you look at Marvel films,
[20:59] you know, like you look at Doctor Strange and some of these films, they do this quite
[21:02] brilliantly in terms of the way that they're managing these colors. And some of their frames
[21:07] look very stylized because the amount of saturation they're using. But it still is very static in the
[21:14] way that they're doing it because they're very cautious in the way that they're choosing their
[21:18] colors. So for this, what I wanted to do was chuck some of these cooler tones in. So I took a little
[21:24] bit of this kind of purplish color and a little bit of this kind of slightly more green sort of
[21:31] color in the in the flare. So we're going to see this pretty much in the picture. I did use a tiny
[21:38] bit of yellow, yellow green on some of the flares at one point. But yeah, it's really not as prominent
[21:47] as everything else. It's very, very subtle addition. But that just gives it a little bit of color
[21:52] variation. So you start to see that in our highlights, in our explosion flare, and all of these little
[21:59] elements here. So it just adds pops of color to your scene. So let me talk about how these flares
[22:08] were actually made, not just the color. I'll go back up to it. So let me just go back earlier in
[22:15] my comp and give it a second to load. Let's go to frame 50. Yeah, frame 51. Actually, I think it's fine.
[22:27] Just let it load for a second. I'll have the whole thing completely precomped out.
[22:31] Well, I do have a lot of precompensants comp. This is a pretty big script, as you can see.
[22:40] Let's go here, go a bit further down in our comp. There we go. So let's look at just one of these
[22:47] elements here. Yeah, I have some of these elements, these explosion stuff coming towards the camera
[22:52] as well. I'm not going to talk about every single element I use, but I did use a lot of those
[22:57] energy effects layered together. And that's the nice thing about having them already rendered.
[23:01] It's like you wouldn't necessarily think if you're doing the simulations yourself,
[23:07] you'd have to make every single effect from scratch. But having all that huge library at your
[23:11] disposal, it speeds up this process. So these are some of the elements I created for lens flares.


### Lens flares [23:13]
**Transcript (timestamped):**
[23:17] So this is an element from my energy pack that it's supposed to be probably, I don't know,
[23:23] maybe some kind of wormhole or like EMP or some kind of crazy explosion. So you can use it for
[23:28] all kinds of stuff. But when I was looking at this, you know, I just dropped them all on Nuke,
[23:32] and I was like, well, this kind of looks like a refractive type of quality. And what I mean by
[23:37] that is, let me show you a video. So this is a video that took, and I have some really nice lens
[23:43] flares in this video. So there's like basically no post production in here except some very slight
[23:48] grading on DaVinci Resolve. But I like to keep these videos and I have like basically a library
[23:54] pictures and videos that I mentally store, because there's all kinds of details that you want to
[24:00] remember. So something like this, you see this flare forming down on this car with all these tiny
[24:05] little rainbow streaks. And this is like a crazy flare. It doesn't happen that often. But, you
[24:12] know, it's something that you're not going to maybe intuitively think of. So it's nice to have
[24:18] those things. So you can see that little flare forming there. But that's not the one I wanted
[24:22] to point out. There's a couple flares in this video that are very interesting. And kind of
[24:27] demonstrate this sort of idea. So you can see here on the bottom of the frame, we have this
[24:34] flare coming in. And it looks like some shapes that are kind of almost overlapping in the way they
[24:39] move. And this is something you see a lot in sort of lens flares. You see these like little
[24:45] overlapping highlights. So we'll go here. Again, another one forms here. So we can see these
[24:51] little almost, I don't know, slight brighter pieces in a larger glass like flare.
[25:00] And as it keeps going, there's a couple more that show this that well as here. So we can see it
[25:08] again here. So we see that little pieces that are changing highlights at different rates
[25:14] from each other and kind of overlapping, which makes this really nice, organic looking motion.
[25:21] Again, with this one, so we see this kind of weird shape that appears at the end. And if we look at
[25:26] my comp, I always try to take those things into consideration to try to mimic those effects.
[25:32] You can see this kind of flare thing happening. We have something similar happening here.
[25:38] And those kind of refractive elements are happening in the edge flare. So let's go back to it.
[25:45] So yeah, this library can be used for a lot of things. And I used it in this case for an edge
[25:51] flare. So I took this element, I scaled it up to the edge of the frame. And then I kind of like
[25:58] frame hold it on different frames and dissolved between. So like as I switch frames, as I tap
[26:03] through here, you see that these highlights are kind of changing in within the shape of another
[26:10] shape. So it gives that sort of look that I just described. And what we can do with that is kind
[26:16] of push it into our color scheme that I mentioned. So if I go into that color scheme, we have those
[26:22] blues and those nice highlights there as well. So we can kind of plus that on as the explosion is
[26:29] happening. So let's just load it here. Go back to frame 51. I think it's already cached. So
[26:39] obviously it looks kind of weird. Everything looks weird on this frame because there's not enough
[26:42] elements here. So everything looks just like a very ugly glow in the center. But if we again,
[26:47] if we step down the comp, once we have all the other stuff, that's where it comes together. So
[26:52] it's a lot of layers. But you can see that just even that base layer, that little refractive element,
[26:59] it adds that that edge here. I also used another one of my effects from that library. So if I


### Optical flares [27:03]
**Transcript (timestamped):**
[27:08] time pin it, look at it. So this is another element that's that comes with that library.
[27:14] It does something like this, where there's like these like two spheres that like protrude outward.
[27:19] And that can be used for like a bunch of different stuff. But in this case, I actually looked at the
[27:24] start frame and I said, Well, that actually looks kind of interesting. It doesn't, you know, even
[27:28] though this is like some kind of energy ball explosion, the start frame looks like an optical
[27:33] element. So actually, I just frame hold it on that frame and scale it up like crazy. And then
[27:40] what I did was add some color to it. So I basically went in the blues, the same kind of tones were
[27:45] in here. And then I added a slight bit of purple into the highlights. So I kind of blurred it.
[27:52] So it's like all blurred together. And then I add a slight bit of color into that image.
[27:58] And that's again, just giving a slight pop of color is going to add interest to your image,
[28:02] rather than just, you know, going completely monochromatic. So you see, even though we have
[28:07] a blue explosion, I'm adding pink highlights. And as I step down, all these same concepts are being
[28:15] applied. So as I step down, we have more different color highlights. So again, I use this element
[28:20] as a lens flare as well. So if you remember, this is the same element I wrapped onto the,
[28:27] I guess the shock wave as a refractive thing, but I also use it as a lens flare. So you can see
[28:31] it's used in different ways. And yeah, basically just did the rainbow technique,
[28:38] which is explained in the video, how to make a rainbow nuke. And then I'm just kind of scaling
[28:42] that up and adjusting the point of time of that video to make it kind of flicker.
[28:50] So same thing here. So we have that same element, just at a different point of time. And I'm mixing
[28:54] them on and off at different points. And let's see. And then this one, I think this is just
[29:01] an optical flare. So this is from the optical flares plugin. So that's how we can get a more
[29:08] complex looking flare using a kit bashing. And let's just keep going down. I think, yeah,
[29:17] this is an interesting one as well. Let me go to frame 51. This is cash. This is another
[29:22] interesting one. So again, like we've constructed it to here at this point, and we can add layers of
[29:27] color just to make it more interesting. So I took this shock wave element and motion blur to outward
[29:33] just a 2D motion blur, very simple. And then just add a bit of that greenish tone in there.
[29:39] And we can just add those little stacking those pops of color as we build this image up.
[29:45] Let's just see. And yeah, there's a bunch of other stuff. But I think that's basically it for the shock
[29:53] wave. I know a lot of people had a question how to do that. And I think this tutorial will be very
[29:57] useful in seeing that. Obviously, if you guys don't want to get the, you know, the library for
[30:02] whatever reason, a lot of these techniques still apply. And you can see like the sort of logic,
[30:08] the sort of logic, the way of combining patterns and stacking things and combining colors to get a
[30:16] result. And that's, I think, pretty useful. So hopefully you guys have enjoyed it. Hit like if
[30:23] you liked the video, really helps the algorithm. And yeah, thanks so much.



---

## Captured Frames

- [0:33] tutorials/frames/nuke-compositing-an-advanced-cg-shockwave-vfx-lookdev/frame_000.jpg
- [5:14] tutorials/frames/nuke-compositing-an-advanced-cg-shockwave-vfx-lookdev/frame_001.jpg
- [10:28] tutorials/frames/nuke-compositing-an-advanced-cg-shockwave-vfx-lookdev/frame_002.jpg
- [12:50] tutorials/frames/nuke-compositing-an-advanced-cg-shockwave-vfx-lookdev/frame_003.jpg
- [14:26] tutorials/frames/nuke-compositing-an-advanced-cg-shockwave-vfx-lookdev/frame_004.jpg
- [18:39] tutorials/frames/nuke-compositing-an-advanced-cg-shockwave-vfx-lookdev/frame_005.jpg
- [20:16] tutorials/frames/nuke-compositing-an-advanced-cg-shockwave-vfx-lookdev/frame_006.jpg
- [26:03] tutorials/frames/nuke-compositing-an-advanced-cg-shockwave-vfx-lookdev/frame_007.jpg

---

## Structured Notes

### Core Technique
"Kitbashing" a complex, multi-layered CG shockwave/explosion entirely in 2D compositing by combining pre-rendered stock energy-effect elements (from the author's own 200-effect library) through re-projection, distortion, deep occlusion, and color-scheme-driven grading — rather than treating any single element as a literal, un-transformed overlay.

### Summary
An advanced, concept-first (not node-by-node) breakdown of a "ball drops in, huge glassy shockwave explosion" shot (frame_000), built almost entirely from generic pre-simulated "energy effects" stock elements — the author's own paid library (composingacademy.com/energy-fx) — reworked so aggressively that their circular/spherical stock origin is unrecognizable in the final comp. Two techniques recur throughout: **re-mapping a stock element's shape** (a circular pattern polar-distorted into a straight line, then ST-mapped onto scene UVs, or a flat 2D texture UV-projected onto both sides of a 3D sphere for multi-layered depth) and **using the same element for multiple unrelated purposes** (one "wormhole/EMP" element is used simultaneously as the shockwave's refractive glass texture, a lens flare, and — frame-held on a single interesting frame — an "optical flare"). The core shockwave has two coupled parts: (1) a 3D sphere (frame_003) whose surface is doubled via `UVProject` (planar YZ projection from a movable axis, giving two overlapping copies of the same texture — frame_004) then transform+merged 90°-rotated over itself for a 4-layer pattern, and whose shape is animated via `DisplaceGeo` fed a radial gradient so the sphere pinches inward at the start of the explosion and relaxes into a perfect sphere as it expands (an explosive "coming from a point" read, not just a scaling ball); and (2) a separate "contact" pass — a circular library element `PolarDistort`-unwrapped into a straight line, `STMap`-projected across the scene's UVs, then masked with an expanding `PMatte` (Nukepedia) driven at the same rate as the shockwave's growth so the energy texture is only revealed right at the shockwave's leading edge (frame_001/002) — making two separately-authored elements read as one continuous physical event traveling across the geometry. `Glass` (Nukepedia, an IDistort variant that can distort R/G/B slightly differently) applied with another liquid-look stock element as the displacement source gives the shockwave sphere its chromatic-aberration/glass-refraction look. Where the shockwave crosses in front of scene geometry it needs to occlude correctly, so a `Deep` merge (ScanlineRender's deep output merged against the live-action/CG geometry's deep data, sped up with `DeepReformat`) cuts the shockwave where it passes behind objects — described only at a conceptual level, not step-by-step, since deep compositing is a large topic on its own. `Cryptomatte` IDs are used to re-scale the same ST-mapped texture per-piece-of-geometry so UV stretching doesn't read as obviously wrong across differently-scaled surfaces. A recurring "make anything a rainbow" trick (Linear→HSV round-trip, cross-referenced to the channel's dedicated rainbow tutorial, frame_006 shows the resulting rainbow-mapped color wheel/element) recolors black-and-white stock elements to match a deliberately chosen **color scheme** — the video spends real time on this: a mostly monochromatic blue/teal base with desaturated highlights (sketched live as a literal color-swatch diagram) plus small, careful "pops" of a second/third accent hue (purple, a little yellow-green) so the shot doesn't read as an untethered rainbow — explicitly citing Doctor Strange/Marvel-style disciplined stylization as the reference point, and warning that "compositors rarely talk about the art side" despite it mattering more than the pass list. Lens flares are built the same kitbashing way: an edge-flare element scaled to frame edge, frame-held on different frames and `Dissolve`d between them so overlapping highlights shift organically within the shape (frame_007, mimicking a real drone-footage reference clip of natural lens flare behavior the author studied directly) — plus one shot's actual first frame repurposed as a static "optical" flare because it coincidentally looked like a lens artifact rather than an explosion start frame, and a genuine third-party Optical Flares plugin pass mixed in for additional complexity.

### Key Steps
1. Source stock/library energy elements (author's own 200-effect pack, but the technique generalizes to any similar stock library) — load many candidates into Nuke simultaneously to browse for a pattern that suits the target look, since elements are high-res (4K) enough to survive heavy re-warping.
2. **Contact-point pass:** `PolarDistort` (Nukepedia) a circular stock element into a straight linear pattern; `STMap` it onto the scene's UV pass so it wraps correctly across the actual geometry; mask its visibility with an expanding `PMatte` (Nukepedia, position-pass-driven) timed to grow at the same rate as the shockwave itself, so the texture only shows right at the shockwave's leading edge — this is what sells "energy traveling across the surface" instead of a static decal.
3. **Main shockwave shape:** build a 3D `Sphere`; use `UVProject` with a planar projection (YZ plane, from a movable `Axis`) to re-map the sphere's UVs so a flat texture wraps identically on both front and back instead of once around the whole sphere — doubles the perceived layering; `Transform`+`MergeGeo` a 90°-rotated copy over itself for a 4-layer composite pattern (time-offset the copies for asymmetry if desired).
4. Animate the explosion's shape (not just its scale) with `DisplaceGeo` fed a radial gradient centered on the sphere: keyframe the displacement scale from strong (pinched/triangular, near the origin point) at the shot's start down to zero (perfect sphere) as the shockwave expands — reads as energy radiating from a point rather than a ball simply growing.
5. Distort the sphere's surface texture with `Glass` (Nukepedia — an `IDistort` variant with independent per-channel R/G/B displacement) using a separate stock "liquid" element as the displacement source, for a chromatic-aberration/glass-refraction highlight quality.
6. Occlude the shockwave correctly against scene geometry it passes behind using `Deep` compositing: render/derive deep data for both the shockwave pass and the scene geometry, `DeepMerge` them (speed up with `DeepReformat` beforehand), so the shockwave is cut where it's behind objects instead of always drawing on top.
7. Fix UV-stretch artifacts from the single global ST-map by isolating individual geometry pieces with `Cryptomatte` and key-mixing in a differently-scaled copy of the same ST-mapped texture per piece.
8. Color-grade the shockwave/scene toward a deliberately chosen, mostly-monochromatic color scheme (sketch it as literal color swatches if it helps) — one dominant hue family (here blue/teal) with desaturated highlights, then add small, careful "pops" of one or two accent hues rather than using many saturated colors freely (which reads cheap) — cite strong stylized-but-disciplined references (e.g. Doctor Strange) as a target.
9. Recolor black-and-white stock elements to fit that scheme using the Linear→HSV "rainbow" trick (own dedicated tutorial), then subtract unwanted hue ranges (e.g. remove greens) via a `HueCorrect`-style shuffle/keyer before merging.
10. Build lens flares from the same stock-element philosophy: scale an element to a frame edge, `FrameHold` several different frames of it, `Dissolve` between the frame-holds so internal highlight shapes shift organically (study real reference footage — the author reviews his own drone footage's natural flares directly on camera to justify the look) — reuse a single element in multiple roles (refractive sphere texture, edge flare, frame-held "optical" flare) rather than sourcing a new element per need.
11. Layer in a genuine third-party plugin pass (Optical Flares) alongside the from-scratch kitbashed flares for additional complexity where useful.

### Nodes / Tools / Settings
- **Core Nuke/NukeX:** `Sphere`, `Axis`, `UVProject` (planar, YZ plane), `MergeGeo`/Transform-and-merge-over-itself, `DisplaceGeo` (radial-gradient-driven), `ScanlineRender`, `Deep`/`DeepMerge`/`DeepReformat` (NukeX-only feature), `Cryptomatte`, `STMap`, `FrameHold`, `Dissolve`, HSV colorspace round-trip (Linear→HSV→remap→back) for the "rainbow" recolor trick
- **Nukepedia gizmos:** `PolarDistort` (circle↔line unwrap — author prefers it over `SphericalTransform` to avoid memorizing more settings), `PMatte` (position-pass-driven expanding reveal mask), `Glass` (per-channel `IDistort` variant for chromatic-aberration-style refraction)
- **Third-party:** the author's own "Energy FX" stock library (200 pre-simulated elements, compositingacademy.com/energy-fx) as raw material; **Video Copilot Optical Flares** (or similar) plugin for one flare layer
- **Reference-gathering habit worth noting:** the author keeps and directly reviews his own reference footage (a drone clip with natural lens flares) on camera while explaining the flare-kitbashing technique, to justify why the frame-hold+dissolve overlapping-highlight approach reads as organic

### Difficulty
Expert — this is explicitly a concept-level walkthrough, not a followable node-by-node recipe (the author states this directly); requires prior comfort with Nuke's 3D system, ST-maps, Cryptomatte, and deep compositing to reconstruct any of it, plus color-theory judgment for the grading pass.

### Foundry App & Version
Nuke / NukeX (deep compositing — `Deep`/`DeepMerge`/`DeepReformat` — requires NukeX, not base Nuke). Version not stated on screen; per this skill's version-tracker, a 2022 upload falls in the Nuke 13.1 (Nov 2021) → 13.2 (Apr 2022) window. Uses only the Classic 3D system (Sphere/Axis/UVProject/DisplaceGeo/ScanlineRender) — predates the 14.0-beta USD 3D overhaul.

### Tags
compositing, 3d-system, deep-compositing, st-map, projection, gizmo, fx-simulation, grading, expert

---

## Related Tutorials
- Nuke Tutorial | Compositing a Rainbow [Intermediate] (`nuke-tutorial-compositing-a-rainbow-intermediate.md`) — this tutorial directly reuses that video's Linear→HSV rainbow recolor trick to colorize black-and-white stock elements.
- 360 Spherical LatLong Textures | Nuke Tutorial (`360-spherical-latlong-textures-nuke-tutorial.md`) and Mixed Medium VFX P1 (`mixed-medium-vfx-p1-blender-nuke-ai-embergen-vr-tutorial.md`) — both also use `PolarDistort` for a different purpose than this tutorial's circle-to-line stock-element unwrap.
- Build Entire FX with ONE Pass - Nuke Tutorial (`build-entire-fx-with-one-pass---nuke-tutorial.md`) — shares the underlying philosophy of driving comp-side FX from position/UV passes and Cryptomatte-isolated regions rather than re-rendering.
