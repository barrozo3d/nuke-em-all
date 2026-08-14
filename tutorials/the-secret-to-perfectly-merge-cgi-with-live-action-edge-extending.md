---
title: The Secret to Perfectly Merge CGI with Live Action | (Edge Extending)
source: YouTube
url: https://www.youtube.com/watch?v=Ub0MmjYy0b0
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/the-secret-to-perfectly-merge-cgi-with-live-action-edge-extending/
frame_count: 0
frame_status: pending-selection
---

# The Secret to Perfectly Merge CGI with Live Action | (Edge Extending)

**Source:** [YouTube](https://www.youtube.com/watch?v=Ub0MmjYy0b0)
**Author:** Compositing Academy
**Duration:** 11m11s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py the-secret-to-perfectly-merge-cgi-with-live-action-edge-extending <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Overview of Edge Extending [0:00]
**Transcript (timestamped):**
[0:00] Edges are really important for good compositing.
[0:02] If you ever want to merge a CG render behind a defocus or motion blurred edge, you will always have edge problems.
[0:08] In this video, I'm going to break down how to correct this very common compositing problem.
[0:13] Now, you might think the solution is simple, just take a roto mask, defocus it and cut out the CG render.
[0:18] However, this is the incorrect approach and you will always run into bad edges if you do this.
[0:24] Defocused or motion blurred edges will always be semi-transparent.
[0:28] This means we get color contamination in between the objects.
[0:31] When everything is in focus, there is less of a problem because you can just roto the sharp edge.
[0:34] We know logically this tree is tan and white, but if you rotoscope the tree with the defocus, we can see the edge.
[0:39] So if we erode in and edge extend that color out, then we reapply the original alpha.
[0:44] Compared to the original, we see the correct color in the edge.
[0:47] So now we have three images, the background, the CG object and the patch that we are going to put over the top.
[0:52] First, the sphere goes over, then we mask the sphere against the patch,
[0:56] then the patch goes over the top of our CG.
[0:58] So I'm going to cover this process in four parts.
[1:00] Part one, the bad method, part two, the node setup, part three, merging it together,
[1:05] part four, where edge extend fails and how to fix it.
[1:08] And for anyone who's looking for more advanced examples, there's a link in the description to some new projects in the beginner series for Nuke.


### Light Dapple Effect [1:14]
**Transcript (timestamped):**
[1:14] So hopping in Nuke now, I'm going to show a quick setup on how this sphere was made,
[1:17] just for the beginners and showing some different node setups to give people ideas.
[1:22] Just pretty much as a radio, kind of grade it down a little bit and we erode some ambient occlusion with some simple roto shapes into some grades.
[1:31] And for the light dappling effect, I basically just took the background image, cropped it to smooth the edge so we don't get a sharp edge.
[1:37] So there's a softness thing in the crop node.
[1:40] You could do a Luma key to kind of capture some of these little light pools.
[1:44] We can blur it out a tiny bit and then we can use that as a grade mask.
[1:49] So the grade is plugged into a mask.
[1:51] And we just basically push it up a tiny bit in the game and we can multiply a bit of warmth into that.
[1:56] So that's essentially what's happening here.
[1:58] Two different copies of the same image to create this sort of fake render just for this example.
[2:03] So just some different ideas there on some basic node setups for creative use.
[2:09] So let's hop into the part one, which is don't do this for the motion blur,


### Bad Method [2:10]
**Transcript (timestamped):**
[2:13] defocus edge like I explained in the quick demo there.
[2:17] We have our sphere.
[2:18] We roto it out and we stencil it.
[2:21] And we put it over the image.
[2:22] So that's like intuitively as a beginner, what you might think is the simplest way.
[2:26] And logically, it would make sense.
[2:27] But we on defocused edges, of course, we can't do this like I explained in the breakdown.
[2:33] So now that we understand the reason why, don't do this unless it's really in focus.
[2:38] And it's really just, if it's a tiny bit of defocus, you could probably do it and maybe an edge extend.
[2:44] But I would say in general, if it's out of focus or motion blur, this is not going to be the approach.
[2:49] So everything is based on what you're doing.
[2:52] So the second method here is the edge extend.
[2:55] And here's the method of doing it.
[2:57] So there are different ways to actually to arrange these nodes.
[3:01] So I'll basically put the script in the beginner series for this project.
[3:06] If people are looking for extra information, there are different ways to arrange nodes and
[3:10] they do the same result.
[3:11] And there are many nodes that actually do the same thing.
[3:13] So actually many edge extend nodes you can download for free on Nucopedia.
[3:17] So I'm going to show this setup.
[3:19] I think it's the most logical and easy to understand for someone who's starting out.


### Node Setup [3:23]
**Transcript (timestamped):**
[3:23] So essentially what we have is our picture.
[3:26] We have a roto that's actually in focus.
[3:28] So no defocus has been applied yet.
[3:29] See, it's actually branched down in this direction.
[3:32] So what we're doing here is we have a solid alpha in our picture.
[3:35] That's what the shuffle here is doing.
[3:36] So it's just creating a solid alpha.
[3:39] And we're taking the eroded version of this roto.
[3:42] So we're eroding it in just a tiny bit.
[3:44] If we look at the alpha channel and we disable and enable,
[3:47] you see that it's basically shrunk in.
[3:50] We're going to mask out the color of the image.
[3:53] So if we disable and enable, we see we're just chopping off the defocus edge there.
[3:58] And we're using the default Nuc edge extend node.
[4:02] No custom node here.
[4:03] I just wanted to show the basics.
[4:04] There are custom nodes that do sometimes a better job, for example, but I wanted to
[4:08] keep it simple.
[4:09] So edge extend.
[4:10] And what you need to do here is you basically push this little road up and down until you
[4:15] get the color that you want.
[4:16] So it's essentially pushing around the color.
[4:18] We've already done the erode into the color.
[4:20] So you might not have to mess with it too much.
[4:23] Sometimes I like to do it manually in this sort of way where it's very visual and you
[4:27] understand exactly what's going on.
[4:29] Because this process of eroding into the color can all be done directly within the edge extend
[4:35] node, which is essentially this setup over here.
[4:39] But we're just going to explain it in this one step here.
[4:42] So without doing it all inside the node, we just do it manually so we really understand
[4:46] what's going on.
[4:47] So we edge extend it out.
[4:48] And this is essentially just pulling out the color.
[4:51] And we're using the source alpha.
[4:53] So the alpha that's coming from this stream, if you look at the alpha channel, it's looking
[4:56] at this.
[4:57] It works better with sharp edges.
[4:59] So you want to use a sharp edge to do this.
[5:02] We extend out and that's all good to go.
[5:05] Now we don't want to apply the sharp edge as the alpha because we want it to still be out
[5:09] of focus.
[5:10] It's an out of focus edge.
[5:12] So the de-focus is actually into its own stream here.
[5:15] We have the roto, which is like this.
[5:17] We de-focus it.
[5:19] So de-focus is being here.
[5:21] And we copy that back into the color stream.
[5:23] This is why it's always good to always think of color and alpha as two different things.
[5:27] We're doing all these crazy things to the color channel, but then we're going to put
[5:30] the alpha channel back into this image.
[5:32] So if you look at the alpha channel by hitting A, that's what this copy node is doing.
[5:36] It's taking this alpha and copying it back into the stream.
[5:39] But we still see it's not like the final image and that's where the pre-multiply comes in.
[5:43] So if you pre-multiply it, it's taking the alpha and cutting it out against the colors
[5:47] that you've modified.
[5:48] That's why this is more powerful than Photoshop or After Effects where you don't separate
[5:52] your colors in your alpha very often.
[5:55] This is actually very common workflow in Nuke to separate those two things.
[5:58] So this is the same setup.
[6:00] I won't explain it here, but the script is here for those people who are in the beginner


### Merging the Patch [6:02]
**Transcript (timestamped):**
[6:04] series.
[6:05] But this is essentially what we have.
[6:06] So we have something that has the colors in the edge.
[6:09] And we don't want to actually put this patch everywhere over the image.
[6:12] So I'm going to disable this for a second.
[6:14] We don't want to put the patch up here because why would we double up the tree?
[6:18] We kind of like creating a new edge and that's a new problem.
[6:21] Really all we want to do is cover up the CG and just fix the edge that it's getting put
[6:25] behind.
[6:26] So that's where the mask comes in.
[6:28] So we have this layer or this image that we've created and we have the alpha from the sphere.
[6:34] So we take the sphere alpha.
[6:35] You see if branched it down separately.
[6:37] We branched it down separately and we're going to mask that patch so that we only apply the
[6:41] patch over the area that we're trying to cover.
[6:44] So we take the alpha here.
[6:46] I've done a little bit of an erode to soften the edge and I'll show you why in just a second.
[6:50] And then we basically mask the patch.
[6:51] So here's our patch.
[6:53] We're taking the alpha from our sphere and we're masking it.
[6:55] So we just get that patch.
[6:57] Now what this erode is doing, if we look at the final result and we zoom in, occasionally
[7:03] you'll need to erode the edge a tiny bit.
[7:05] If you don't do it, sometimes you get this weird halo effect around the edge.
[7:09] So it's like, you see that you fix the edge here, but it's not fixing just around there.
[7:15] What we need to do is make sure that this patch extends a little bit further than the
[7:19] actual sphere render itself.
[7:21] So what we could do is just erode it out and that would fix it there.
[7:25] There's other ways you could fix that.
[7:26] You could roto stencil that off, for example.
[7:30] Or you could, for example, you could add to the alpha if you wanted by just adding a
[7:33] roto shape.
[7:34] So you could add more of the tree patch if you needed.
[7:36] There's various ways you can fix it.
[7:38] That's what I'm trying to explain here.
[7:39] But this is the principle.
[7:41] So we have enough that covers it, but not putting it everywhere all over the image.
[7:45] So that is how you merge it over.
[7:47] Essentially you have background.
[7:49] You put the CG over and then you're putting your patch over the top.
[7:52] And that workflow of doing that is very, very common for layering live action elements,
[7:58] actually.
[7:59] You will do this quite frequently.
[8:02] So one more example just to show where the edge extend doesn't work.


### Where Edge Extend Fails [8:04]
**Transcript (timestamped):**
[8:07] So the edge extend is good for most scenarios, I guess.
[8:11] You don't want to overuse it.
[8:13] There are ways to despell edges and things like that in more advanced courses.
[8:16] I've talked about that in the Keen course, for example.
[8:19] There's many different approaches.
[8:21] You don't want to overdo the edge extend.
[8:22] A lot of beginners will edge extend everything as soon as they see this technique.
[8:26] But essentially one way or one problem that happens with edge extend is that really, really
[8:32] small details, you can't grab the color because you can't really erode in and grab the right
[8:36] color here.
[8:38] So for example, if you look at these little twigs, we have a slightly out of focus twig.
[8:43] And I just wanted to add this to the example because you're like, well, how do you fix
[8:46] the color if the edge extents can't erode and pull that color out like we just did?
[8:52] So if I disable this node, you can see what the actual problem was.
[8:55] So this is a little bit semi-transparent.
[8:57] We know that the twig is brown, but we're seeing to a green leaf that's just behind
[9:01] it.
[9:02] So again, same problem, even though it's very, you know, it's not that out of focus.
[9:06] We're seeing that green contamination coming through the defocus edge.
[9:10] So what we can do is if we go to our result here, here's the edge extend.
[9:16] And we can see it's not really working because how could it work?
[9:19] It's contaminated right through the brown.
[9:21] So we actually need to replace that color if we want it to be correct.
[9:24] So when you start getting into the small details and more advanced compositing, you might not
[9:28] understand why this is relevant if we're just talking on YouTube.
[9:31] But when you're working on Dune and Avatar and these movies are seen on huge screens,
[9:35] you need to fix these little problems.
[9:37] They won't accept these type of problems.
[9:39] So we see that little edge is contaminated.
[9:42] So what we can do is we can just paint in the color channel only instead of affecting
[9:46] the alpha.
[9:47] So if our alpha looks like this, but our colors look like this, this is where this un-premultiplied
[9:52] workflow comes in really handy is we just take the roto paint and we set it to RGB only.
[9:59] We don't have RGBA.
[10:00] So if I paint in here, the alpha will stay the same.
[10:03] It's not going to affect it.
[10:04] So what I can do is I can just take a little bit of a brown color and just basically paint
[10:08] up that spot.
[10:09] And that's something you'd want to basically frame hold.
[10:12] Sometimes you would have to track that on if you're doing a more advanced shot with
[10:15] movement.
[10:16] We're just doing a still image here.
[10:18] But keeping this on a beginner level, essentially we're just going to paint that color out.
[10:22] And when we repremultiply this, you see the difference.
[10:25] If I disable and enable, we fix the color contamination that's coming through the edge.
[10:29] So we merge over, we have that fixed and all those little tiny details are kind of fixed
[10:35] over the image here.
[10:37] And we can see that we have that defocus and most of the edge extent is working for various
[10:42] parts.
[10:43] If we disable the edge extent, let's just do it to show as well.
[10:46] If I disable the edge extent, look at all the problem areas, even with this tiny amount
[10:50] of defocus that we were creating.
[10:52] I know that this defocus is correct.
[10:54] We're kind of rotting the edge, but a lot of those edges are semi-transparent.
[10:58] So edge extent will really help on little areas like this as well.
[11:02] So that's pretty much it for this tutorial.
[11:05] If you guys liked the video, hit thumbs up on the video.
[11:08] If you want more videos like this, and that's about it.



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
