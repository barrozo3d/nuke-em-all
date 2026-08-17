---
title: A Senior Compositor's Creative CG Workflow REVEALED
source: YouTube
url: https://www.youtube.com/watch?v=X-x_pLqjYxk
author: Compositing Academy
ingested: 2026-08-17
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/a-senior-compositors-creative-cg-workflow-revealed/
frame_count: 0
frame_status: pending-selection
---

# A Senior Compositor's Creative CG Workflow REVEALED

**Source:** [YouTube](https://www.youtube.com/watch?v=X-x_pLqjYxk)
**Author:** Compositing Academy
**Duration:** 18m39s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py a-senior-compositors-creative-cg-workflow-revealed <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello guys, welcome to this video. This is a free clip from Nuke 707, Deep Compositing in Nuke,
[0:04] which is a course that just released for people who want to learn this skill for feature films,
[0:09] or just want to add it to their workflow if you're an effects artist or a lighting artist,
[0:12] trying to see how deep can be stretched creatively.
[0:16] So this is just showing a few of my creative thought process around look developing a shot like this.
[0:21] So it's not actually talking about deep in this specific YouTube video,
[0:24] but the course does cover a lot of deep techniques to use a lot of elements,
[0:28] and also how to utilize the CG elements you already have in a number of ways to actually stretch them further,
[0:33] such as if you have volume metrics, and how to push those things around to control the contrast of shot.
[0:38] So that's the big project that's included in this course, but there's actually a number of other projects
[0:42] that we go through to explain a variety of use cases, like taking the CG environment and doing deep height fog,
[0:48] deep hazing, there's a variety of techniques involved there,
[0:52] as well as some things we can do with live action elements included.
[0:55] So if you want to check it out, that's there for you.
[0:58] If not, that's cool too.
[0:59] Just hit the thumbs up on this video really helps make the free content for YouTube.
[1:03] So thanks so much, and the video is going to start now.
[1:05] So we're going to talk about how to go from the raw renders,
[1:08] which is essentially this, into the final composite, which is like this.
[1:13] And so there's a lot of changes that are involved here.
[1:16] Whenever you do these kind of A and Bs, it always looks like one color grade,
[1:21] even though your script is absolutely enormous, and there's like,
[1:25] you know, hundreds of color corrections and many, many elements.
[1:28] So it's good to start to look into the details and think about what are the things that are useful
[1:34] to think about when you look at a raw render like this and start to dissect this in a way that makes sense.
[1:41] So essentially, one of the problems with this shot is if you just deep merge everything together,
[1:46] this is a very chaotic shot, there's lots going on.
[1:48] And to get the contrast right is the most difficult thing in this composite.
[1:53] So if you go through and actually do this whole project yourself,
[1:57] you're going to see how many layers of grades you're going to have to actually do.
[2:00] But that's part of the challenge.
[2:01] And I think that's also part of the fun of doing really big CG shots,
[2:05] is figuring out those very small contrast adjustments and stacking them together to make things work.
[2:10] So I can show you a few frames of the foreign after,
[2:13] and then I'm going to show you some work in progress frames as well to show you
[2:17] sort of the direction and how to build it up.
[2:20] And we'll get more specific as we actually look into the composite and things like that.
[2:24] So this is the raw, if we just like deep merge the smoke over without the 2D explosion and fires
[2:29] and sparks fire glow, all of those things that we do.
[2:33] And this is kind of what it looks like.
[2:36] You can see it looks kind of very video gamey.
[2:37] There's not the most aesthetic contrast.
[2:40] And this is after.
[2:41] So you can see there's all kinds of things we're doing here.
[2:43] We're adding the explosion into the deep.
[2:46] We're doing these sparks that are falling.
[2:48] We have falling fire.
[2:49] We have different spark elements underneath.
[2:51] We have some launching sparks on the frames before us.
[2:53] We have these tendril sparks being launched out.
[2:56] And then we have even some lens dirt that's being lit up.
[2:59] And the lens dirt is animated as explosion is coming over.
[3:03] We have the reflection in the glass of all of these things happening.
[3:06] So that means we're using a projection or a 3D setup to get that reflection since it's an element.
[3:12] So we're actually bringing that reflection in and matting it out.
[3:15] So there's lots and lots of things going on here.
[3:18] So I'm just going to keep doing a walkthrough.
[3:19] Some people may want this and might not.
[3:21] So just to throw it out there again.
[3:23] Generally I do this just for the people who want to see my thought process.
[3:28] So even here we have like specular highlights like look how bright the sky is in our composite.
[3:32] So that means we need to start pinging out the top of the snake.
[3:34] Start to get a little bit of contrast.
[3:36] If you look at the original snake and we look at the contrast of the building.
[3:40] This is actually a big mismatch of what you'll need to do.
[3:42] You can see that this just feels generally a bit more contrasty and this feels a little bit more flat overall.
[3:49] So a big part of this is just going to be getting some directionality to this
[3:52] and getting those black levels and the shadow region to feel more connected to the building.
[3:57] So you see in my composite I'm starting to ping out the highlights,
[4:00] brightening up the sky and then darkening underneath.
[4:02] And that's what's going to make these things actually sit together.
[4:05] So that is a big part of what you'll have to do with the contrast.
[4:09] So again, we want to read the snake the whole shot.
[4:11] So part of what I'm doing here is we're composing explosion,
[4:15] but I'm also taking the snake element and pinging out the metal render passes in there.
[4:20] So we can see the snake moving inside.
[4:22] So you see if you look close, you can see the details inside.
[4:24] And that's pretty tricky to do because look at our raw render.
[4:27] We're just if you're just putting that smoke over, you're not going to see anything.
[4:30] We can just step frame by frame.
[4:32] You see nothing happening here versus here.
[4:34] We're still getting all those elements plus we're trying to get that snake being seen all the way
[4:39] through. It's really a difficult thing to do.
[4:42] So it's all of those things in combination that start to make the shot come together.
[4:47] And then we're also doing details like if we look here, a lot of these pieces of glass,
[4:53] for example, if we see here, there's almost no light source.
[4:56] So we're actually pinging out these glasses using normal passes or relighting
[5:01] to bring out those shards and make that contrast against the black.
[5:05] So we're actually, that's not a CG element.
[5:07] We're just using the elements that are there in a new layering technique,
[5:12] just a layer on top and make it feel more complex than the render we've been given,
[5:16] which is a big part of CG compositing is to use what's there and then try to make it
[5:20] look as good as you possibly can.
[5:22] So continuing, we can see the same thing going on here, all kinds of things going on,
[5:29] relighting with different reflections in the windows, same techniques being applied here.
[5:35] And overall, just if we look at the original, especially on the center frame,
[5:38] so I'm going to keep passing through the frames because it's almost like two different shots.
[5:42] Like we have the explosion and then we have like the building collapsing at the end.
[5:45] So you almost think of it like two shots.
[5:47] This at the end, you really don't read the silhouette of the snake.
[5:50] So a big part of what you're going to need to do is get fires and use the elements to read the
[5:55] silhouettes. We want to make sure we understand the story that this thing is ripping through.
[5:59] And in this, you can't really see where everything is.
[6:02] So especially up in these areas where we can use deep transforms, we can bring those pieces of glass
[6:07] up to brighten them so they look like they're reflecting the sky.
[6:11] We could also, I mean, the really big part was just like this part is like you need to have fire
[6:18] and then you need to make sure that casts light onto the snake.
[6:21] And you also want to have some fires behind the snake as well.
[6:25] So you can see the edge because if we do orange and if we do orange here,
[6:29] it's going to feel like that's blending into the edge, whereas it shouldn't be because it's kind of
[6:33] sitting on top of the building. So what I did, I chose to put the light behind the snake just so
[6:38] it feels like it's sitting on top. And that's a big part of making that feel like more 3D as well.
[6:44] So here we can play some big fires. We can do all kinds of things.
[6:47] And this is really up to your interpretation as well.
[6:49] You really don't have to copy this shot. This could be a nighttime shot, frankly,
[6:53] like because it was lit without direct sunlight, you could actually composite this like
[6:58] a very nighttime shot as well. It would be a bit more challenging because of some of the
[7:03] deep, you know, edge stuff that with the smoke, but you could do it. It would be more challenging.
[7:08] But we'll just continue explaining here. I did this really hot metal.
[7:12] So the reason I chose to make the snake kind of having a red, like burning face was this whole
[7:19] reason of reading the shot, just because I thought that the shot read better with like melting metal
[7:25] versus just everything metallic. So because I chose this direction, we can put like melted
[7:32] metal edges all the way along the pieces. And some of the pieces falling down will have hot
[7:37] metal edges. And we can use some different techniques like P P noise and things like that
[7:42] in combination with deep bubbles. So I'll show that technique a little bit later,
[7:46] where we can use deep mats in combination with P noise. So this is kind of what we got going on
[7:53] here. And then we're using the elements as creatively to try to convey the story here. So
[7:58] like as the building starts to like snap kind of stacked, I think it's a three or four elements,
[8:03] even just here, just to get the snapping, just to make it feel just to read that, that moment as
[8:09] things start to break apart, you know, there's nothing really happening here. You know, even
[8:14] though it's something really cool, the simulation is fantastic, but it would just be cool to have
[8:18] more things happening. So that's kind of the direction. And again, look at the look at the
[8:24] windows brightness, we're cranking up the contrast on the shot, this is a super high contrast grade,
[8:29] almost like transformer style, where they really punch the contrast. And so that's a big part of
[8:34] this. So again, doing A and B, you can see the flames here still trying to read the silhouette.
[8:40] A lot of these elements, you're going to need a keyframe over time, you notice like here,
[8:44] we don't see the fire on the edge, but over time as the snake goes in a little bit more,
[8:48] we start to see more of those flames. So a lot of this is just you need to have lots of patience
[8:53] and just sit there and figure out good timing on the elements. And also like exploding sparks. So we
[8:59] have like fire, but then I have like big embers that are shooting off, which gives it more motion.
[9:03] So it kind of looks like, yeah, just things shooting off, which is I think a pretty cool effect.
[9:09] So we'll continue forward, just to go towards the end of the shot here.
[9:13] The end of the shot, we have the smoke actually coming back out as it's starting to collapse
[9:19] here. So what I actually did was I keyframed the deep data of the smoke and transformed it
[9:25] slightly forwards, just so we could keep reusing that simulation element over and over. And that's
[9:30] a really good technique, like, you know, we talked about it earlier, but I'm showing you where I use
[9:34] these techniques on this specific shot. So if you feel like it's not dusty enough, you can always
[9:39] pull the element or push it in, etc. And that's a good way to just drive the contrast. So we're
[9:44] very contrast over here, but we lose some contrast here. So your eyes are going to be going towards,
[9:48] you know, the whole building tipping this way. And actually, that's actually what I want, because
[9:52] some of the spark element looks really cool at the end. So as it like breaks apart, we have like
[9:57] these I added a showering spark element. So I added some of these elements with some of them
[10:02] already in the CG sparks that we get. So it's a combination. And then the bigger chunks are just
[10:08] part of the render. So we just have these dark pieces. But if we use pinos on them, we can actually
[10:13] make them look like that's melting. And that gives us like the bigger chunks mixed in with the small.
[10:18] So the size variation is interesting to look at. And that's kind of how I was thinking about all of
[10:24] this. So we'll just continue just to keep checking out different portions of this, you know, as it's
[10:31] going in, we're having an exploding edge because all this metal is being completely destroyed. So
[10:36] again, not just adding the elements, but we got to do the interactive lights, the specular hits,
[10:41] the showering sparks, and then the burnt and crumpled edges. So there's probably, you know,
[10:47] five or six elements, we have heat distortion, we have a little bit of smoke that's coming out,
[10:52] smoke is behind the heat distortion, so subtle, but it's still, it does make a difference to have
[10:57] those things. Probably the tricky, the two trickiest things, like I said, is composite is the
[11:03] overall contrast is pretty tricky. And then just the explosion is fairly challenging, because there
[11:10] are five or six layers that you need to get to get it to start to look kind of cool. So that is the
[11:17] main ideas. I'll just show you guys some other examples, I guess I explained most of it here,
[11:23] but just to show some like earlier renders, and then like later on, so this was like an early comp.
[11:30] And like really, really early, like just like when you're starting to get the elements in there,
[11:33] I'm going to show you like the difference between early comp and then like sort of final comp. So
[11:37] here's something where like, yeah, you have all the elements in there, but like it's just so messy,
[11:41] and it's just hard to read and things like that. And so if we look at the final comp, it just, you
[11:47] start to get like pieces of glass, you start to get layers of contrast, for example. So we have
[11:50] like a black thing and some, and then we just have a bunch of white dots everywhere, which doesn't
[11:54] read separate from the snake itself. So it's cool to add some color, like those are the pieces of
[12:00] the glass reflecting back the spark colors. So that's the kind of thought process that I'm having
[12:04] there is like, if your eye doesn't read something, or you are on your first read, you're not understanding
[12:10] it. This is where you want to start to introduce more colors or more elements, or even if we could
[12:15] put a smoke element behind some of these, we got to do something to make that read better. And so
[12:21] that's my thought process on these two frames here. There's some other frames that I chose.
[12:28] Again, this was, I already explained this word, so a wedding of the edges. This is another one
[12:33] where I had started the explosion, but this is not what I would consider like a final glow.
[12:39] And sometimes things become a little bit blurry when you have things like this. So if I compare
[12:46] to the end result, we can get this like broader and hotter feeling like this is a massive explosion.
[12:51] We should see all kinds of diffusion and more bounce light on the surface of all of this glass
[12:59] coming towards us. So that's essentially, this is like the final matter, which feels very,
[13:03] very hot. Like this is a huge hot explosion of heat distortion and glow towards the camera,
[13:08] should be overexposed and lose crazy amount of detail. And that's, you can see the difference
[13:13] here between like an earlier one and a later one. So here again, earlier one, a little bit later one,
[13:20] you see how it's overexposed, right? But this just feels even more overexposed. Like you just need
[13:27] to push it to make it really feel like a really hot explosion. And that diffusion too really helps
[13:33] the broader glow. So I always think of glows and layers. I never think of glow as an exponential
[13:41] glow. The exponential glow will help your edges sit in for sure. Like you absolutely need it.
[13:45] Otherwise, your explosions are going to look totally cut out. But I think of it, it's good to
[13:51] think of it in layers. I think of, I usually think of glows as maybe two to three layers of glow.
[13:57] You have like a base glow. You have a broad glow. And then sometimes your glows blur the image a
[14:03] little bit too much. So that's where you want to add things on top of the glow, like maybe
[14:07] shards of glass or sort of a smoke that catches highlights, you know, things like that, you want
[14:12] to layer things on top to catch different forms. Otherwise, it glow, it can easily smooth out your
[14:18] image a little bit too much. So here again, this is early render. This is a second pass at it,
[14:25] adding some manual color correction to the glass around it. You see like, look how bright this is,
[14:31] this should should be reflecting onto this glass and all of these little pillars and things like
[14:36] that. So essentially, that's the difference. We start, we go from something like that to something
[14:41] like that. And you see, again, thinking about where the light is traveling and traveling through,
[14:46] you know, you know, for even from this one to this one, you see, this is what I was talking
[14:50] about stacking contrast, where this does feel very blown out, but just adding those those shards
[14:55] over the top is what makes it cool. So we'll talk probably more about that once we, you know, talk
[15:01] about the specifics of the nodes and stuff. I know I'm talking to more experienced people
[15:07] generally here, so I won't go like to walk through on every single node. But I guess if people want
[15:13] it, I can you can always reach out in the email. So this is again, earlier comp, here's another
[15:17] example of contrast, where you see you feel like you have all your elements here. But there's
[15:22] still just some things with the contrast that could be improved. It's just something about it
[15:26] feels a bit cut out, it doesn't feel like a sitting into the building and, and things like that.
[15:31] And sometimes it's really hard to know exactly what to do with an image, especially after you've
[15:35] spent, you know, 50 hours on a composite or whatever, you could easily spend, especially without a
[15:40] render farm on the shot, you can easily spend 100 hours doing the shot. That's just a heads up,
[15:45] like that's the kind of time that these, these things take. And that's very, very normal. I wouldn't
[15:52] expect less than a week of work on a shot like this in a studio, they're going to go through many,
[15:56] many iterations. So practicing that will, and struggling through that will help. So this is
[16:03] the general, this was an earlier pass, I suppose. And then this is starting to pull some of those
[16:09] deep elements back out towards the end. So you can see, just feels more integrated, everything
[16:13] just sits together. It doesn't feel like so much like something is sitting on top. You see how
[16:18] this just feels like there's something darker, and maybe more dark, and maybe more neutral on top
[16:23] of something more blue. And, you know, it just feels there's something missing here in the contrast.
[16:28] Contrast still kind of nice, but, you know, it feels more lifted back here, which is kind of nice,
[16:33] because it's further up, and there should be some more smoke and stuff. But I think generally,
[16:37] this version looks much better. You start to see like more little pockets of smoke, you'd expect
[16:42] tons of dust in the air, think about how many particles would be in the air from this huge
[16:47] thing happening. So making it more lifted towards the end makes a lot of sense. And then this is
[16:53] this is the end comp here. So let's just see. This is one at 185. This should be
[17:00] 1185 as well. I'm not sure why. I think this might be a different frame. So we'll just try to find
[17:06] the frame here. So this is the final comp. And this was the other one. So we'll just try to find it.
[17:15] Yeah, something like that. So and then okay, so here's first version. Probably not the first
[17:22] version, by the way. It's probably just somewhere where I rendered it. But this was like a work in
[17:25] progress. This was another work in progress working on the contrast. But then there's one more thing
[17:30] we could do and we can pop out the contrast that even more. So look at the final version. We want
[17:34] to make it feel we still want to keep that metallic feeling, you know what I'm saying. So
[17:39] it's all such subtle adjustments, like pushing one thing forward and pushing one thing back.
[17:45] For example, watch the building and watch the snake. Right now it feels like it's kind of inside
[17:50] or this isn't what's sticking out even though it's 3D. So flipping the contrast, you see how
[17:55] this building gets slightly darker and this gets much brighter with the specular and then just
[18:00] starts to feel more like a 3D metal shiny thing in there versus where it's very dark.
[18:05] And also everything we get a little bit more dusty, you pulled out the smoke a lot at the end
[18:09] on this side just because I thought the asymmetry and the contrast looked pretty cool as well.
[18:14] So that's all pretty cool stuff. And then we can look at the
[18:18] raw render. So here's the raw render, right? Lots of things we can do,
[18:22] final comp, lots of color grades, lots of things we can do here. So that's generally my thought
[18:27] process on how to develop these CG shots. We're going to go in much more detail on specific
[18:32] techniques and things like that. But hopefully that gives you a general overview of this type of composite.



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
