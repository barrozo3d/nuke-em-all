---
title: Nuke Keying Tutorial | Greenscreen Beginner Concepts
source: YouTube
url: https://www.youtube.com/watch?v=aeJTBwIudSs
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/nuke-keying-tutorial-greenscreen-beginner-concepts/
frame_count: 0
frame_status: pending-selection
---

# Nuke Keying Tutorial | Greenscreen Beginner Concepts

**Source:** [YouTube](https://www.youtube.com/watch?v=aeJTBwIudSs)
**Author:** Compositing Academy
**Duration:** 13m15s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py nuke-keying-tutorial-greenscreen-beginner-concepts <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### <Untitled Chapter 1> [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, this is just a free preview from Nuke 505 of my Keying and Color Integration
[0:06] course, how to take footage and integrate it with the background, but also do difficult
[0:10] extractions, how to get those alphas as well.
[0:14] And all the steps that come with it, so grain workflows, semi-transparent edges, difficult
[0:21] keys is really what it's about.
[0:22] So not to TV level, but more feature film level work is kind of what the course is.
[0:28] Okay in this video, it's just a few lectures from that class going over the high level
[0:32] concepts, sort of the underlying fundamentals you actually need to understand before you
[0:36] even go into Nuke of just how to approach and problem solve a basic key, but it does
[0:43] go more advanced and more intermediate than that, so a few other clips from this course,
[0:47] you can see the kind of level detail we get into combining multiple keys together, combining
[0:53] lots of roto shapes and motion blur and all of those things.
[0:56] The things that as a beginner, it's easy to struggle on because you don't see how the
[1:02] pieces connect together and oftentimes it can seem complex, but actually it's just a
[1:08] few simple concepts that need to be laid out first that if you understand them, you'll
[1:13] see the full picture and it's actually not as hard as it seems.
[1:17] So this is some other just quick time lapses from that course showing some of the integration
[1:22] and the color work that we can get into, various workflows with that and yeah, the artistic
[1:29] side as well, so just those really, really small details that can make an image feel
[1:33] more integrated and also I think is the most fun side of compositing, so that's also a
[1:38] big part of the class.
[1:39] So yeah, in the next few minutes, it'll just be some of the high level concepts, not node-focused
[1:45] about keying in general, so if you're really starting out, really for beginners is who
[1:49] is aimed at here, you might find it useful.
[1:54] Example of a perfect ideal key.
[1:56] So this is kind of, so when you're kind of starting out and you're learning keying, some
[2:01] of the information out there is just like using one of the nodes and then you're getting a
[2:04] key and that's just usually not how it works.
[2:08] Usually it's kind of combining multiple keyers and it's more of an advanced process.
[2:13] So if we look at this video and I hit play here, we have like a guy on a green screen,
[2:17] we take our little color picker and we just basically select color and voila, we have
[2:22] like a perfect character cutout put over the background and your job's done, you get home,
[2:27] you get paid, which is generally never how it works.
[2:30] Basically most of the time we have green screens that are not lit perfectly like this and
[2:37] you don't have this perfect scenario and usually it takes a lot more work, so we need to understand
[2:41] a little bit deeper.


### A more realistic shot... [2:43]
**Transcript (timestamped):**
[2:43] So this is a more realistic green screen.
[2:45] We have a unevenly lit screen here, so we see it's been lit.
[2:50] This is basically just a fake drawing, but it's lit more on the right side here and it's
[2:55] darker here.
[2:57] We also have some problems.
[2:58] We have a microphone standing in the way on the left side and we also have some wrinkles
[3:02] on the bottom of the green screen.
[3:03] So this is something that's very standard.
[3:05] You have all these problems, so unwanted objects, bad overlap and then also our character has
[3:12] some spill.
[3:13] So because of the, this is all simulated, but we'll look at real examples after this,
[3:19] but we see that that green outline is around the character because the bounce light or
[3:26] the light is bright enough to basically bounce off the surface and go on to the character,
[3:31] which is going to cause us problems when we're trying to key it.
[3:33] We could get semi-transparent edges.
[3:36] We could also, you might be able to pull a nice key still, but you're still going to
[3:41] have that contaminated color.
[3:43] So we have to learn how to deal with all these problems.
[3:46] And lastly, we also have just, by bad luck, we have this character wearing a tie that
[3:52] has some green dots on it.
[3:54] So those would be a problem as well, that we would use a holdout.
[3:58] We would have to road of this so that it doesn't get keyed.
[4:02] So that's kind of just the realistic scenario.
[4:04] Those are all the problems we see before we even start this shot.
[4:08] We see the problems.
[4:10] We also see that these legs are going over the wrinkles, and some of these wrinkles might
[4:13] be black, so we can't actually key them.
[4:17] So this is something that we'd have to deal with a different way.
[4:21] We'd actually use some rotoscoping to combine it.
[4:24] And of course, we have the spill.
[4:25] So that's the area I was talking about earlier.
[4:29] And that's something to think about before we start a shot.


### It requires a more Complex approach [4:33]
**Transcript (timestamped):**
[4:34] So requires a more complex approach.
[4:37] If we were to just try one keyer, this is what would happen.
[4:40] We would go in here, we would select the color.
[4:43] But then you see all of this problem area is actually basically being added over the
[4:48] background.
[4:49] You see it's darker here, and it's brighter here.
[4:51] So that darkness isn't being keyed the same way as the area we selected.
[4:55] So the area we select is good.
[4:57] So maybe we select this lighter green color, and it's getting removed properly.
[5:02] But the darker green is kind of still there a little bit.
[5:05] And we're also having the wrinkles coming through, and we still have the microphone.
[5:09] So if we look at it, also we have this green spill on the character, which is not being
[5:14] handled very well either.
[5:16] So if we go further and we just look at what the alpha of that thing looks like, we see
[5:21] where all our problems are coming in.
[5:23] The black is good because we've removed this area.
[5:26] But all this area that's not supposed to be here, that's not our main character, that's
[5:30] a problem.
[5:31] So obviously we have the tie.
[5:33] So there's holes in the middle of our character.
[5:35] We also have this left side here that needs to be transparent, but it's not.
[5:41] And then obviously the wrinkles and the object there.
[5:46] So this is what we're looking for.
[5:47] We're actually looking for an alpha that looks like this, and that's not what we have.
[5:53] So before you start your shot, you want to identify all those problem areas.


### o Identify the problem areas • Think about how you will go about solving them [5:54]
**Transcript (timestamped):**
[5:57] You want to think about how you're going to go about solving them.
[6:01] And we've already done that.
[6:02] We've kind of identified them.
[6:04] But we want to just think about it mentally, how this puzzle is going to be solved.
[6:09] So this is the way I would solve this shot, and probably would have to be solved this
[6:14] way.
[6:15] So we could separate it into two keys here.
[6:18] So we could put basically one key here selecting this color and another one selecting this
[6:23] color.
[6:24] And we can actually blend them across each other with a key mix.
[6:27] So that's what a key mixing is.
[6:28] It's taking two different results and blending them together with a roto shape.
[6:34] We could also use a garbage mat.
[6:38] So garbage mat, again, we went over quickly in the vocabulary, I think, but basically
[6:43] you just wrote out objects that aren't supposed to be there that aren't keyable.
[6:47] So we can't remove that microphone with a key because it's not green.
[6:52] So we just need to rotoscope around it and basically remove it from our alpha.
[6:56] So we do something like that.
[6:57] Just cut it off and say, okay, that's just garbage.
[6:59] So that's what that is.
[7:02] Next thing we want to do is we actually have to garbage mat off the feet.
[7:07] So if we have a scenario where there is ground and the character's feet are not over the
[7:11] green screen or there's really bad wrinkling, this picture might not demonstrate it completely.
[7:17] But if let's just say these wrinkles, you can't key them out because there's too much
[7:20] black.
[7:21] We don't want those wrinkles in our final image.
[7:24] So what we do is we actually rotoscope the feet off of the character.
[7:28] And then we use another rotoscope to bring back just the bottom of the feet like this.
[7:34] And this is called a holdout.
[7:36] So the red line is part of our garbage mat where we tell Nuke or whatever software we're
[7:41] using to cut off that piece of the alpha.
[7:44] And then after that, we can do another roto and just put it back in the pieces that we
[7:49] need.
[7:51] Also, we'd want to do a holdout, another one of these holdouts, just protecting and
[7:58] solidifying that alpha over the tie.
[8:01] So we would say, don't punch a hole in the green of these areas over the tie.
[8:07] And that's basically how we would attack this.
[8:10] So that's kind of combining multiple keyers and thinking about how we're going to do this.
[8:15] And yeah.
[8:19] So yeah, that's pretty much a lot of times, keying and rotoscoping, they go together.
[8:24] It's not just one or the other.
[8:25] We're both trying to achieve the same result, which is just getting a clean alpha channel
[8:30] to define what part of the image we're going to keep or remove.
[8:34] Yeah.
[8:38] So if we want to break down that idea a little bit further, just to see it more visually
[8:44] even than we saw, I'm just going to show you guys an example here of the idea we talked
[8:52] about with key mixing.
[8:54] So if we want to look at uneven green screen, and here we are using two keyers, but sometimes
[9:00] we have multiple keyers.
[9:01] You could have eight, nine, even 10 keyers that solve different areas of your key.
[9:07] This is an easier example we have two.
[9:10] But we see key one on the right side here.
[9:13] If we select that color with one of our keyers, we see that it goes black and it's solving
[9:18] it pretty well.
[9:19] But it's not solving the rest of the image.
[9:21] We have key two over here where we use another key or node.
[9:25] We're going to get to the new nodes later, so don't worry.
[9:28] This is just a theory.
[9:30] But we see key or two is selecting that color and it's punching a hole.
[9:34] So we have the black, which is good.
[9:36] But neither one of them are solving the entire image.
[9:39] So we need to use key mixing, which means combining two or more alphas together.
[9:43] And remembering that black is transparent and white is solid.
[9:48] So if we were to combine these two, use a roto shape, we can actually do this in a node
[9:53] in Nuke.
[9:54] So we would say we want to keep this area from key one and keep this area from key two
[9:58] and just combine those.
[9:59] And now we have a key mix alpha and that's solving this uneven green screen.
[10:04] So we see that we still have the microphone and the wrinkles and the holes in the guy,
[10:08] but we've at least solved the first part, which is just getting that uneven green screen
[10:12] keyed out.
[10:13] And we have a clean result behind our person.
[10:17] So we want to solve the areas that the key is not going to solve for us.
[10:21] So we're going to use the garbage mats to remove areas that can't be removed by King
[10:25] and hold out mats to hold out or maintain the areas of the key that we need to keep.
[10:32] So let me go back here.
[10:36] And so here's our garbage mats.
[10:39] We're going to garbage mat out the microphones, which is your roto shape will stencil it out
[10:44] and stenciled out from the ground here.
[10:48] And then we'll have an alpha like this.
[10:50] But now we've lost the feet of the character and we still have the holes in the center.
[10:54] So we go back and we would actually rotoscope around the feet and we would need to animate
[10:58] the rotoscoping for as long as the shot is.
[11:00] So that obviously is a bit of manual work that we have to do, but we restore it like
[11:05] this.
[11:06] So that's our rotoscoping.
[11:07] And then our final mat looks like this.
[11:09] So we have it, the character repaired and our final alpha.
[11:15] And finally, we would combine it into the image.
[11:17] So it's copying into the image.
[11:20] Yeah, so we'll learn about that.
[11:24] So if you guys don't know, well, how do I copy an alpha into a picture?
[11:27] What does that even mean?
[11:29] We'll go into that in Nuke and, you know, it's going to go from the beginner to the
[11:33] complete advance of King.
[11:35] So we'll go over that.
[11:38] One thing we'll do, and the last thing we need to solve on this is we need to remove
[11:42] the green from the edge of our character before we pre-multiply it.
[11:47] So before we apply our cutout and merge it over the background, we just want to do a
[11:51] color correction on just the edge of this character.
[11:56] So because we've actually created this alpha, we can actually do an erode.
[12:01] So we can shrink it inward and we can actually create another alpha that we're going to use
[12:05] just for color correction, which is called an edge mat.
[12:09] So if we go here, we use that alpha, but we shrink it in just a little bit.
[12:13] We can create basically an alpha that's just this white edge that we see here.
[12:19] And we can actually blur it just a little bit.
[12:21] And you'll have an alpha that's, if we're just looking at the white on this example,
[12:25] we're going to use that to remove the green from the edges.
[12:29] So we see here, the green is just on that edge.
[12:32] So we've lined up our new alpha that we've created, this edge mat, and we're going to
[12:36] use it to counteract the green.
[12:39] So here's our image.
[12:40] We'll use that alpha that we've just created and just remove the green from our picture.
[12:45] And you see that we get a nicer result.
[12:47] We darken it.
[12:49] Maybe we add the opposite color of green, whatever works, and we'll look at different
[12:54] ways to do that, which is called de-spilling.
[12:57] So now we have a clean result.
[12:59] We also have that alpha stored in this picture.
[13:01] If we go back, this alpha is still in there.
[13:04] So we have a clean result of the guy, and then we can pre-multiply.
[13:07] So that would apply our cutout or apply the alpha that we created, and we'll cut out our
[13:12] character and put him over the background like this.



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
