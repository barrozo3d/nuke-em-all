---
title: How I Made a FULL Star Wars Cinematic from JUST One Screenshot
source: YouTube
url: https://www.youtube.com/watch?v=6hArU1CgJUA
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/how-i-made-a-full-star-wars-cinematic-from-just-one-screenshot/
frame_count: 0
frame_status: pending-selection
---

# How I Made a FULL Star Wars Cinematic from JUST One Screenshot

**Source:** [YouTube](https://www.youtube.com/watch?v=6hArU1CgJUA)
**Author:** Compositing Academy
**Duration:** 7m41s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py how-i-made-a-full-star-wars-cinematic-from-just-one-screenshot <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In just one week, can I take this static image from Battlefront 2 and transform it into a cinematic teaser that can be used for Battlefront 3?
[0:07] Star Wars Battlefront 2 has been having a massive resurgence online, tens of thousands of players jumping back into Battlefront 2.
[0:15] And for good reason. After May 4th, people started realizing that this game has been totally overlooked, and that it's actually an incredible game even today.
[0:23] Players online have been hoping for a Battlefront 3, a continuation of the game series.
[0:27] So everyone has been hopping back on in an act of rebellion in hopes to get a third game made.
[0:31] Attention all flight personnel, please report to your commanders immediately.
[0:35] I was one of those players hopping back in, I used to play it constantly, and so when I booted it back up, something hit me.
[0:40] I saw this loading screen with the Sith Trooper, the red design of the helmet, fading into a hologram.
[0:46] And I thought to myself, what if this wasn't just a loading screen, what if it was the opening shot to a cinematic?
[0:51] So that became the challenge for this video. The game is having a second life right now, and I don't know how long that's gonna last.
[0:56] And so if I fail, it's just another forgotten fan project.
[0:59] But if I pull it off, maybe it reminds people of the game and keeps the series going.
[1:02] But guys, I have a problem. I need a Sith Trooper and I need a really good one.
[1:07] And I don't have time to model this in a week, and I'm certainly not working with a full team.
[1:11] So with no resources, are we just dead on arrival?
[1:16] Nah, there's always a way.
[1:18] So I searched around a little bit to find the model and found a high quality rigged Sith Trooper, which was perfect for this video.
[1:24] I can literally just import this directly into Blender and start working.
[1:27] Now, it's great to have a model in Blender, but how are we supposed to make this into a cinematic?
[1:31] The first step is I need to add a little bit of motion.
[1:33] Again, I don't have days to hand animate a character in some kind of crazy fight scene.
[1:37] So I'm going to go to Mixamo, which lets you apply motion capture data to any rig instantly.
[1:42] In this case, I just grabbed the kneeling pose that fits perfectly, like the Trooper was waiting for activation.
[1:47] Minimal animation, but it still tells a story.
[1:50] I can add a little bit of extra detail by hand animating a few elements, such as rotating the head just to get a little bit of custom animation in there.
[1:56] So now I have a model in pose, but it's doing nothing.
[1:58] It's pretty boring.
[1:59] We need to figure out how do we make this cool?
[2:01] I'm going to lean into my strengths, which is my understanding of cameras, light and compositing.
[2:05] So here I'm going to frame up with long lenses and shallow depth of field.
[2:09] The way you'd shoot a teaser similar to a TV opening series.
[2:12] It keeps the background abstract and lets the viewer focus entirely on the Trooper and the transformation that's going to occur.
[2:18] In addition, I'm keeping the camera motion super simple, slow, steady push-ins, nothing too fancy.
[2:23] But even then, something was still missing.
[2:25] So the character still looks great, but without any more motion in the scene, it can still feel a little bit dead.
[2:29] Here's the trick, because the armor is actually reflective, by animating area lights in the background, I can create sweeping highlights on the object.
[2:37] This gives the illusion of extra movement, even when the camera is barely moving.
[2:40] It's subtle, but can help keep a shot alive.
[2:42] But we're still not there yet, and with the week running out, I had to render all these shots and still need to create this holographic effect.
[2:48] In the original artwork, the Sith Trooper helmet fades from this blue glitch to red, as if it were loading in.
[2:53] I wanted to build on that idea and have the armor activate from black to red as he grabs the gun.
[2:58] The best way to do this is directly within nuke.
[3:00] We can work really fast and we can get really high quality without having to do any kind of complex simulations.
[3:06] So the first effect I need to do is the gun appearing out of thin air as a hologram.
[3:10] So here I went into blender and clicked the gun and exported as an limbic, so I can bring it directly into nuke.
[3:14] I also export the 3D camera from every shot.
[3:17] Now we can see the gun and the camera in nuke working together.
[3:20] But now we need to get interesting patterns to layer together to create this animated hologram effect.
[3:25] For this, I'm using the ScreenFX plugin from the Compositing Academy Asset Store.
[3:29] This plugin allows you to create thousands of patterns, whether you're creating holograms or glitches or motion graphics.
[3:35] It's a really great tool, nuke, if you're doing those type of effects.
[3:38] So as an example, this is a starting base effect we have here, which is just some of the grid drips that we can control.
[3:43] We can control the speed, the width, how many of them there are, all of these different things to change the pattern.
[3:48] But if we run this through and we put it into the image and put on the model, we can get a nice effects pass directly on the 3D.
[3:54] Now the other thing I wanted to do is to have the gun growing and start to appear.
[3:58] So what I did was I took a Boolean of a sphere, chopping the gun just within that sphere in blender, and I exported that as a new piece of geometry.
[4:06] So if I hit play, this gun actually grows on the edges.
[4:09] Now, if I just put another ScreenFX pattern on it, I can get all these really cool patterns.
[4:13] And now we have another effects pass that we can line up with the one we just created before.
[4:18] But two effects isn't enough. We need more layers to make this convincing.
[4:21] Using similar techniques, I created these other passes that I can combine together to create a complex looking hologram.
[4:27] Add a little bit of Compositing Academy Lens Dirt Magic and some camera defocus and the shot starts to come together.
[4:33] But we still haven't slayed the beast.
[4:34] We still have to create this seamless holographic transition across the helmet to match the concept art.
[4:40] First, we start with a really ugly roto just blending the red and black helmet.
[4:43] The tricky part is we need to blend this seam perfectly across the 3D model and make it not feel like a 2D effect.
[4:49] So it flows on the actual 3D shape.
[4:51] Here I'm starting with a ScreenFX node called Polyflow, which allows us to create geometric shapes that evolve down a path.
[4:57] So I have something like this and I can also create a wider version of that that has a little bit of a fall off.
[5:01] After that, we can use a UV project node with an axis so we can do a planar projection directly onto the face on the model.
[5:08] Off to the side, I created another effects pattern that looks like this.
[5:11] And if you multiply those two together, we have the original and then we have the one with the new pattern multiplied in.
[5:16] This gives us a pretty good starting point for our effect.
[5:18] Now, the next problem is that it doesn't look very blended. It looks very graphic still.
[5:22] We don't have any glows or interactive light.
[5:24] But what we can do is take the original effect, blur it and glow it outwards and we can multiply that against a normal's render of the face.
[5:30] And this gives us a bit of interactive light underneath the blend.
[5:34] So if you put that back on top, we can start to see that it's looking a little bit better now.
[5:37] But there's a lot more we can do.
[5:39] So I went back here and added another interactive pass, but I boosted the edges just around some various areas using the normal's once again.
[5:45] So we get an effect that looks like this.
[5:47] We have the normals and we have these little edge highlights appearing everywhere just to make it look a little bit more graphic.
[5:52] And we want to add even more trailing effects.
[5:54] So I used another ScreenFX pattern that is like a grid.
[5:57] So it looks like it's being constructed as it flows along.
[5:59] But there's even more we can still do.
[6:01] Once we added the focus, it starts to come together.
[6:03] But I want to have a little bit of the effect coming off of the edges rather than just sitting perfectly on the model.
[6:08] So the next step I did here was doing edge attack on the normals of the model, which allows us to get edges all the way around in different places.
[6:14] And then I masked that by the effect we just created earlier.
[6:17] So it only goes around the edge.
[6:18] If we multiply that effect by some dots, we can get something that looks pretty similar to the concept art with these little dots breaking up the edge.
[6:25] And it will travel along with our main effect.
[6:27] So this is kind of what it looks like when you put it together.
[6:30] And I did a similar effect to this where I did another edge detect, but I do this little glitchy break up blocky transform,
[6:36] which will create some of these edges that kind of scatter off as well as the pattern travels down the edge.
[6:41] And for the final effect, I created another edge detected I animated outwards.
[6:45] So it looks like it's coming off the edge and creating a hologram.
[6:48] And if you take this and mask this by another dot pattern, once again, we get a very similar effect to the concept art.
[6:53] So let's see the final result.



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
