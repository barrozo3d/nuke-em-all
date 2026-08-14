---
title: Did Corridor Crew SOLVE Greenscreen?
source: YouTube
url: https://www.youtube.com/watch?v=abNygtFqYR8
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/did-corridor-crew-solve-greenscreen/
frame_count: 0
frame_status: pending-selection
---

# Did Corridor Crew SOLVE Greenscreen?

**Source:** [YouTube](https://www.youtube.com/watch?v=abNygtFqYR8)
**Author:** Compositing Academy
**Duration:** 19m17s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py did-corridor-crew-solve-greenscreen <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Are the claims true?
[0:01] Corridor Digital, the biggest VFX channel on YouTube, just released a brand new green screen keyer.
[0:06] In the video title, they claim to have fixed green screens.
[0:08] And one of the biggest problems with green screens is actually the edge contamination problem.
[0:13] This is when you have semi-transparent pixels and you get this green fringe or some kind of odd color contamination
[0:19] on different parts of your image when you use traditional keyers.
[0:22] But the Corridor Key is claiming to have trained a neural network that actually replaces the edge color
[0:27] by extending the color that it's supposed to be.
[0:30] Present to you, Sam, the finished version.
[0:33] So this looks crazy and wacky because this is something that's impossible to capture in camera.
[0:36] This is the straight color version of the shot.
[0:39] So in other words, there is no transparent pixel here. Every pixel is 100% opaque.
[0:42] If you're a professional, you take this FG output and you would apply the matte.
[0:48] Let's see how it's... Oh, that looks very professional.
[0:50] So we're going to try it out. We're going to take the Corridor Key versus the traditional keyers.
[0:55] So to do an interesting comparison, we need to look for some of the spots that keyers typically have trouble.
[1:01] I have plenty of scar tissue from Keying. I've done a lot of Keying on feature films.
[1:05] And so the standard for Keying is very high to get those perfect edges,
[1:09] especially if you're doing something for like IMAX or a very large screen.
[1:13] So we're going to look at it the way a supervisor would look at the edges.
[1:16] Here I have four different plates focusing on a few different issues that keyers typically have.
[1:20] The first one is transparency and motion blur at the same time.
[1:23] And we don't have a perfect green screen kind of intentionally on the background
[1:27] just to throw a little bit of trouble into it.
[1:29] So that would be the first plate. We get a few motion blur frames.
[1:32] And the second plate we're going to look at is a dress that's being shaken around.
[1:37] So small details, heavy motion blur.
[1:39] That's a pretty flat green screen this one, so not as tricky on the variation.
[1:43] There is a bit of a gradient in the green screen,
[1:46] so that should give some kind of indication if it's able to be smart about the differences in green screen.
[1:52] And then we have one that's just a flat green, but with a very bright color of the opposite tone.
[1:58] So we have this orange pumpkin that I'm throwing up and down just to get an idea of how that would do.
[2:03] And then the last one is kind of a nightmare scenario.
[2:06] Like Nokia typically is going to do a good job on this, but let's try it anyways.
[2:10] We have a bag that's out of focus over a messed up green screen.
[2:14] So we basically have like wrinkles and sharp detail behind the defocus edges.
[2:20] This is going to be a nightmare for Keying typically,
[2:23] just because you usually have to restore those edges from scratch.
[2:26] So we will start with a key light here and then we'll go to IBK and then we'll go to the corridor key to see how it performs.
[2:33] And then we'll choose a winner for each one of these shots and see where the strengths are and weaknesses.
[2:37] So the key light is what we're going to start with.
[2:40] This is the most common key here, I think.
[2:42] So I'm just going to throw a default key light on there.
[2:44] I'm not going to change a bunch of settings and dial it in and try to get a super precise result.
[2:49] We just want to see how the keyers perform by default and just see where that gets us.
[2:54] So if I take a key light and put it over a gray background, this would be the default result, just color picking.
[3:00] And this is what we get.
[3:01] So we do see the same edge problem by default.
[3:04] We see some of the dark edges and some different colored edges.
[3:09] So some it's kind of green in here, some dark here.
[3:12] So you can't treat all the edges exactly the same.
[3:15] And so normally, you know, there's different settings to to fix some of these things.
[3:19] Like you can adjust the screen balance to see how that does.
[3:21] Sometimes that will affect your actual color of the of the plate.
[3:25] So you got to be careful.
[3:26] But if you have some weird edges like that, you know, pushing around the screen balance can help blend some of the weird contamination that's happening.
[3:33] We see we still have the dark edges.
[3:34] So one of the common techniques would be obviously like edge extending.
[3:38] So we could take the color that's in the footage and pull it outward to replace these broken edges.
[3:44] Just normal normal technique, do an edge extend and we can fix some of the edges.
[3:48] The problem, and this is why this this video could be interesting.
[3:52] Edge extends don't work well on motion blurred areas.
[3:55] Normally, you have to hand paint those areas.
[3:57] There's no good procedural way to actually deal with this.
[4:00] And so if we look at the edge extend here, maybe it works as a good starting point and maybe we need to dial it at different places.
[4:06] Like it's fixing a lot of the edge around the sweater sweater here.
[4:11] But it's not doing so well on like the candy.
[4:14] And so normally you'd have to do something like instead of doing a procedural edge extend where we pull the color out, essentially, we need to paint hand paint.
[4:22] Just solid colors frame by frame in the edges on heavily motion blurred areas.
[4:27] People don't even know that this process exists on feature films.
[4:31] And on long sequences, hand painting, the edge contamination thing.
[4:35] I've spent a week or two on a shot doing this before and it's a nightmare.
[4:39] So this is a big problem.
[4:42] And so this is what you could do.
[4:43] You could paint some of the edges and that's one frame to get that result.
[4:47] So so next we have the IBK gizmo.
[4:50] So I'm going to throw a just a basic IBK on there, put it over a background and we get somewhat of a similar result.
[4:57] We can pull around the weight colors, kind of a similar balancing thing going on here.
[5:02] The screen subtraction tries to get rid of some of the color.
[5:05] If you don't have a clean plate, it doesn't do as well.
[5:07] So if we give it a clean plate, here's the basic plate.
[5:11] We do essentially a clean plate removing the main person.
[5:18] And then we plug that back in.
[5:20] And now we put the same result over with the clean plate.
[5:23] IBK is pretty good.
[5:24] It can actually do a despill.
[5:25] That's pretty decent.
[5:26] So if we turn that screen subtraction on and off, we see that it is trying to do this correction
[5:32] and it's doing it differently in different areas around.
[5:35] So this is actually a pretty solid result.
[5:38] And that's going to be hard to compete with because IBK is pretty solid.
[5:42] So if we compare to the original footage and we compare to, let's see, that's original.
[5:47] That's the other.
[5:48] There are some problems, like some weird harsh edges in here.
[5:52] Some areas were losing a bit of motion blur and things like that.
[5:55] So we are losing some details, but it's a pretty solid result.
[5:59] And this is probably what I would start with if I was doing key.
[6:02] We are losing the dark parts of the glass.
[6:04] So, you know, that's something that we have to mix another key or do something else.
[6:08] We probably want to keep that darkness in there.
[6:12] So let's look at the quarter key.
[6:14] Here we have the contaminated color result.
[6:18] So this is what the neural network is outputting.
[6:21] We're getting an alpha and we're getting a contaminated edges with those smeared colors
[6:26] pulled outwards.
[6:27] And if we merge this over, if I turn the despill madness over, let's look at the default result.
[6:33] This wasn't trained on despilled footage.
[6:36] It was just trained on the edges being fixed over some new background.
[6:39] So you can still control the despill if you throw a despill madness.
[6:42] So I think this would be a fair comparison.
[6:44] I was putting a basic despill on afterwards.
[6:47] So if we compare this to the previous best one, which is IBK,
[6:52] IBK actually has a little bit more cleanup that we have to do in some areas.
[6:56] Like IBK has some, some basically background here.
[6:59] And so we would need to mix another key here or you'd have to strengthen how hard we're
[7:04] hitting that image.
[7:05] Whereas the quarter key is actually pretty good.
[7:08] Like this is working pretty well.
[7:11] And in some cases, even retaining the motion blur slightly better than the IBK.
[7:17] So this is the IBK.
[7:19] This is the quarter key.
[7:20] And I'm like, what I'm seeing here is like, it's doing a pretty good job on the color
[7:24] contamination.
[7:25] Now there are some like colors shifting slightly.
[7:28] Like maybe that's the despill.
[7:30] No, it's not.
[7:31] So we have some slight shifts from the plate color so we could mix in the despill or the
[7:35] original colors.
[7:37] But I do think that's a pretty solid result.
[7:39] So first time I saw this, I was very impressed.
[7:42] Now it's not perfect.
[7:44] One of the things that stands out is the temporal consistency in some of the, the color smearing.
[7:51] So if we look at the glass here, we can see a little bit of flickering from the predicted
[7:54] result.
[7:56] And I actually think this could be improved because the way that the quarter key works
[8:00] is it takes an alpha hint.
[8:01] It takes some kind of an alpha upfront and that drives this result that comes out of
[8:06] it.
[8:07] It basically gives you a more fine key plus this color fix.
[8:10] So this is the alpha hint and the alpha hint actually had the problem in it.
[8:14] So I think that this is actually coming from here.
[8:17] And so if I were to do this again, probably what I would do is just do a key light and
[8:21] give it like an alpha like this.
[8:22] That's basically more stable.
[8:24] And then run that through the, the neural network key and see what kind of result that
[8:28] that's going to give.
[8:29] I think it would probably be a best to give a mix.
[8:32] But I do think as a starting point, if you're just objectively looking at these, this has
[8:37] the least amount of problems and I would just mix maybe one here on the edge.
[8:41] And we still get some of the dark edges around.
[8:43] We get almost a perfect motion blur and most of the dark nasty edges are not there.
[8:50] So this is pretty good.
[8:51] I want to give corridor this one to be honest.
[8:53] I think this is the winner and that is really impressive.
[8:56] So super interesting result on the first video.
[9:00] All right.
[9:01] So shot number two, we have the dress thread thing being shaken everywhere.
[9:05] This is a tricky key to get the motion blur right.
[9:09] So if we look at this and we throw a key light on, let's see what the result looks like by
[9:13] default.
[9:15] And we have, you know, we still see some contamination from the gradient.
[9:19] So that's key lights having a little trouble with basically the amount of transparency
[9:24] coming through from the original image.
[9:26] We can see it gets darker up here rather than going on the perfect gray.
[9:29] So that's not 100% great because we would have to push this up a little bit to start
[9:34] to do that.
[9:35] And then we start to see the color shifting a little bit.
[9:37] We start to see the edges.
[9:40] We're kind of losing some motion blur and things like that.
[9:42] So I'm not that happy with the key light result out of the box.
[9:46] Like I would probably try IBK after this.
[9:49] So let's go to IBK.
[9:50] And we do, we'll do a clean plate.
[9:52] So IBK color, we'll throw in paint on it, and that's going to work a lot better.
[9:56] And let's take a look at that.
[9:59] So we take a look at the composite result.
[10:02] This is better than the key light.
[10:05] Let's compare and let's put the key light back to where it was at one.
[10:09] That's the key light.
[10:10] That is the IBK, not that different of result.
[10:15] We still have the darkness in a lot of areas.
[10:17] Now the thing about keying is you don't always have to push your alpha to pure black.
[10:21] People think you do.
[10:22] It depends on the shot.
[10:23] So if you have a background where you can get away with it being slightly gray or like
[10:27] 20% or something like that, sometimes it's actually the best way to retain motion blur
[10:32] is to have certain areas that are slightly semi-transparent.
[10:35] So I'm not saying you always have to push your alpha to black here, but in terms of
[10:40] the cleanliness of this key and the first output, you know, it's something worth considering.
[10:45] Now we do see some dark edges, even from the IBK, it's not a perfect edge contamination
[10:50] that's going on here.
[10:52] So let's take a look at the quarter key and see how it does with the predicted result.
[10:57] So here's the predicted color and here's the alpha that is giving us body fault.
[11:01] And if we throw this over, this is the result.
[11:05] Let's throw it over the same background, make sure we're doing the same exact gray.
[11:08] I think we are.
[11:09] I think it is.
[11:10] Yeah, it's the same gray.
[11:11] It's just that we don't have the gradient problem.
[11:14] So it's doing a better job with the gradient in the green screen.
[11:18] So it was right down here in dark up there.
[11:20] Let's just look back at the original plate again to make sure.
[11:24] So let's just compare what we're getting.
[11:27] This is doing a decent result.
[11:28] I mean, there's some slight darkness, maybe in the edges, but I would say it's doing a
[11:34] pretty good job.
[11:37] Some parts are getting slightly brighter.
[11:39] So I would say like maybe I would blend these two keys together.
[11:42] The only place it's not doing so well is on this thing.
[11:44] This like this sort of peach colored thing.
[11:47] This I think we just need to redo it completely with another keyer.
[11:51] Even key light had a problem.
[11:53] Looks like IBK had a problem as well.
[11:55] So they're all having problems with this thing.
[11:58] But I do think the dress overall, maybe minus the highlight area seems to be the best.
[12:04] I would probably mix the IBK bottom with the corridor one and sort of do a little mix
[12:11] there.
[12:12] But the overall, I still think corridor is actually winning this one.
[12:15] So I'm going to give it to them again on this one with the caveat of, I have it down here
[12:20] actually because I already looked at these, but I would combine it with other keyers.
[12:24] I wouldn't leave it by itself.
[12:26] I wouldn't leave the final key as that.
[12:28] But if we're just talking about which keyer is handling the best as the first result,
[12:32] I think that's, I do think it's fair.
[12:34] Now we're going to check out the pumpkin one.
[12:36] So I didn't de-noise this one as much as I should have.
[12:40] So we should have a little bit more de-noise on here, but since this is the same plate
[12:43] I gave the corridor one, we're just going to look at the noisy version.
[12:46] So this is what it looks like.
[12:48] And yeah, that's the base key, not a perfect amount there overall because there's some
[12:54] slight gradient in the green screen.
[12:56] So if we were to like kind of push this up a little bit, we start getting some nasty edges.
[13:00] And that's why we'd want to do the de-spill separately from the key itself.
[13:05] And so that's probably what we'd want to do.
[13:07] So one thing if we were to de-spill this separately is, key light's pretty good at de-spilling
[13:11] actually if you use it right.
[13:13] So you could push the screen balance up and we could get a nice perfect orange there.
[13:16] But you do notice that the shirt and my hand start to go a little bit like pink.
[13:22] So things start to shift colors in some weird ways.
[13:25] So you would have to key mix the de-spills together to get the final result.
[13:28] You wouldn't be able to do it in one shot, I don't think.
[13:32] So that's something worth considering.
[13:34] But you definitely could pull this key with key light just to say that.
[13:37] I'm not saying that this is not capable, I'm just saying it would be a multi-step process.
[13:42] So same with the IBK, if we look at IBK and we look at an in-paint comp, this would be
[13:49] the base result and we can turn on the screen subtraction.
[13:53] Screen subtraction does a pretty good job on the de-spill as well minus the fact that
[13:57] all this stuff is going pink.
[13:59] So for the maybe the orange part, we could mix that de-spill.
[14:03] Again, this would be a multi-step process.
[14:05] It would not be a single shot key even though it seems like a simple key.
[14:11] It is, but it's mainly just that.
[14:13] Now the corridor key, I had trouble with this one in terms of the de-spill.
[14:18] It did not de-spill the orange as we would expect.
[14:21] So I don't think the corridor key outperformed the traditional keyers on this one just because
[14:26] I would say it's maybe tied with KeyLite, maybe just because KeyLite would give you
[14:34] the ability to de-spill it whereas corridor key, there's no actually controls afterwards.
[14:39] So you'd have to end up splitting this up and doing a normal keying process anyway.
[14:43] It is slightly cleaner.
[14:45] Maybe we're getting a slight background that's cleaner.
[14:48] We're not getting the weird gradient that the KeyLite is giving.
[14:52] So if we look at the KeyLite without the reduced noise because that's what I gave the other
[14:56] footage, we look at that.
[15:00] I would say the base alpha might actually be closer, but to be honest, I think IBK probably
[15:06] wins this one just because it feels like it has a pretty clean alpha and we can do the
[15:12] de-spill.
[15:13] So I'm just going to give that one to IBK as a whole.
[15:15] So a corridor key slightly better than the KeyLite, but IBK, just the optionality there
[15:20] in the ease seems logical.
[15:24] Now one thing worth noting, I did actually try the pumpkin shot as a wider shot originally
[15:29] and putting this through the corridor key actually gave it some problems in the neural
[15:32] network output if it was cropped outwards.
[15:35] So I'm not sure how the training data was created.
[15:38] If the training data doesn't include green screenshots that are wider, meaning maybe it's
[15:42] just a portion of the screen or something like that, like we need to be fully cropped
[15:46] into the green screen, for example, such as this, and then it actually works.
[15:51] So I don't know if it's training data thing or if I just did something differently there
[15:54] that didn't work, but it's worth noting that it did not work when we had stuff around the
[15:59] scene.
[16:00] Lastly, we have the nightmare shot, which is just throw a KeyLite on here and we'll see
[16:05] the problems immediately.
[16:06] So the key is going to be, you know, we have the edge contamination problems, but we also
[16:10] have problems in the alpha, right?
[16:13] So if we look at the defocus edge, it should be a very smooth edge in the resulting alpha.
[16:18] This was a perfect solution.
[16:20] Problem is we're getting all those creases in the actual alpha.
[16:24] So that's why these type of shots are very annoying to do.
[16:27] Defocus shots, especially when they pass over detailed stuff, very annoying to do.
[16:32] So KeyLite's not doing a great job there.
[16:34] None of them will really.
[16:35] So we do IBK.
[16:36] If you look at IBK, we still see the same pattern revealing in the defocused edge in the alpha,
[16:42] maybe we have the edge contamination, even with the screen subtraction on, it's not doing
[16:46] the best.
[16:47] So we would need to do edge extending, we would need to repaint the edges.
[16:51] That's the kind of work we'd need to do to restore that edge.
[16:55] So not going to work.
[16:57] We could turn on the edge extend and see maybe what that looks like, but we'd have to do
[17:00] a little bit more work than that, to be honest.
[17:03] Now, quarter key, let's just disable all this stuff because I have some example here.
[17:08] Quarter key actually gives us a pretty decent result.
[17:10] We still have the little creases in here, but I actually think it might be capturing the
[17:15] defocused edge slightly better, but we still have those edges.
[17:20] So it's not a perfect result.
[17:21] None of these are one-shotting this thing, which is not surprising, but it might be the
[17:29] best result as a starting point.
[17:31] So if I were to fix this and I would use this key, what I would do is I would go into the
[17:37] color result and I would start to just roto-paint the solid color in here.
[17:41] So let's say the true color is supposed to be red without the wrinkled texture in there.
[17:46] We need to go in the color itself and just paint that extension, frame by frame, or you
[17:50] can just use a roto shape.
[17:51] That's a solid color that would work too, or you could clone stamp it whichever way.
[17:56] And the other thing we'd want to do if we look at the final result here, that fixes some
[18:02] of the color a little bit, but it doesn't fix the pattern in the actual alpha.
[18:06] So if you look at the alpha, we actually have to either replace this edge with a roto shape,
[18:11] which would be the proper way to do it if you want to spend a little bit more time on
[18:13] it, or you could try to do a little bit of a roto paint in the blur.
[18:17] So if you kind of blur and just paint in that blur in the defocused area, that's one way
[18:22] to handle it and maybe a little bit of overall defocus as well.
[18:26] And sometimes you can match that defocus a little better just by doing some of these
[18:29] manual results.
[18:30] And that's what we'd expect, a perfect defocus edge.
[18:34] We could spend a little bit more time on it even just to get the exact, the fall off.
[18:38] But this is why these kind of shots are pretty tricky.
[18:41] So yeah, everywhere we still have that problem.
[18:43] But I do think quarter wins, even on the base result, but I wouldn't call it a one shot.
[18:48] So we could say we could say quarter wins or maybe even call the last one a tie, just
[18:54] because the complexity of the shot.
[18:56] So I will say at the end of this, keying is not dead.
[18:58] It's a very valuable skill for compositors.
[19:00] And it's really great to have additional tools, even if they're neural network tools or traditional
[19:05] tools, any solution to speed up our work is really great.
[19:07] If you want to learn keying, we have a bunch of courses on Nuke compositing, which is not
[19:10] just about the technical parts, but really the creative parts as well of image development.
[19:14] And you can check out the courses in the link below.



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
