---
title: Create 3D Noise | Nuke Compositing
source: YouTube
url: https://www.youtube.com/watch?v=4uHLGGcQzzM
author: Compositing Academy
ingested: 2026-08-14
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/create-3d-noise-nuke-compositing/
frame_count: 0
frame_status: pending-selection
---

# Create 3D Noise | Nuke Compositing

**Source:** [YouTube](https://www.youtube.com/watch?v=4uHLGGcQzzM)
**Author:** Compositing Academy
**Duration:** 8m10s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py create-3d-noise-nuke-compositing <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to this quick tutorial about how to create a 3D noise patterns on a CG position pass in Nuke.
[0:08] So this shot here is just a quick example of where I actually used this kind of idea.
[0:13] If I just let it play, this is just a CG car kind of sitting in this parking lot and there's some rain drips kind of falling.
[0:21] And there were some rain drips already rendered on this car, but I wanted to add some extra ones.
[0:25] So this is a really good technique for adding texture detail, dirt, drips, all kinds of things, whatever you can do with the noise pattern you can do with this technique, but in 3D on a CG position pass.
[0:39] So if you guys want the full project file for this shot with the CG car and everything like that, that's available in my Nuke 303 class.
[0:48] And you'll get the script along with an entire class on how to accomplish this shot, along with a variety of techniques.


### Position Pass Setup [0:55]
**Transcript (timestamped):**
[0:56] But I'm just going to teach you a very short, quick trick from that class, which is this 3D noise.
[1:03] So if I go over here to a kind of just a little example I created, it's just a cube and a scanline render, nothing special.
[1:11] But if we go in the scanline render and we go to the shader tab, if you switch the output vectors, you can turn on the surface point and set the channel to P.
[1:21] So that's going to export our position pass out of the scanline render.
[1:26] So if I copy this, actually I'll just create a new one, create a shuffle node, plug it into that scanline render and switch that to P.
[1:35] And you will see that we have our position pass stored there.
[1:38] If we switch to R, G and B, we can see that's storing the three axis in that information pass there.
[1:46] So what we can do with this position pass, if we create an expression, so I'm going to create an expression node, it's a really simple expression.
[1:54] And all we have to do is go to this last box here.
[1:58] So if you guys aren't familiar with the expression node, each one of these boxes basically represent one of the color channels that we have.
[2:07] And you can put like a math expression here to adjust those channels.
[2:11] So you see this box is checked red, this box is checked green and this box is checked blue.
[2:16] So these represent the channels.
[2:17] So just to quickly explain it, if I would just put the number one in the red channel, it's going to make our red channel a solid value of one.
[2:26] So that's kind of how this setup is working.


### Noise Expression Setup [2:30]
**Transcript (timestamped):**
[2:30] But we want to basically go to the last channel here, which is the alpha.
[2:35] So I'm going to erase that one.
[2:36] And we're going to type in a little expression here.
[2:39] So we're going to type in noise, parentheses, R, comma, G, comma B.
[2:44] So that's going to take the information from the red, green and blue channel and put it into a noise expression.
[2:49] So hit enter.
[2:50] And I look at the alpha channel, we get this kind of strange result.
[2:54] So something's happening.
[2:55] If I disable it, you see there's nothing.
[2:57] So we're creating this sort of effect, but it's not very useful at the moment.
[3:01] So a way we can make this more useful is if we go up to the node tab and right click and say manage user knobs, we're going to create a new knob.
[3:11] So choose the floating point slider.
[3:14] And in the name, we're just going to type scale and the label type scale and we'll set the maximum to 30.
[3:21] And what that's going to do is create this little slider, which is going to allow us to control this pattern.
[3:28] However, right now it's not doing anything because we haven't attached it.
[3:31] So if we go back to the expression and we go to each box here and we type asterisks or the multiply symbol and types multiplied by scale and put that after each letter on our little expression here.
[3:49] So now you see that that pattern is being driven by the slider.
[3:54] So when I increase or decrease, we're actually changing the size of our noise pattern, which is really perfect for creating all kinds of different patterns that we can use.
[4:03] So another thing we can do to have more control over this, if this isn't enough already, you know, you can be creative with this.
[4:10] This could be dirt patterns.
[4:11] We can mask it off.
[4:12] You know, for example, if we wanted dirt around the bottom of that cube, we could easily just go here with a roto shape or something else and just kind of mask it.
[4:22] But another way to control this basically noise pattern is to put a grade node before the expression.
[4:29] An important thing to do is uncheck the black clamp.
[4:33] You see it creates this weird streaking and the way these information passes work, if we go back to the RGB, we see that it looks like half black and half white.
[4:44] If I look at the red channel, but if I'm sampling, if I take the sample and I sample, we see that some of these values are negative.
[4:51] So if in the grade node, we have this black clamp, which is on by default, we're actually losing all the values of that position pass.
[4:59] So it's breaking this whole effect.
[5:01] So what you need to do is just uncheck the black clamp.
[5:04] And now you'll be able to, you know, have our image back.


### Color Channels [5:05]
**Transcript (timestamped):**
[5:07] But what we can do is go to the gain and split it into the four color channels.
[5:13] And now we can adjust the red, green, and blue separately, which is going to allow us to scale this however we want.
[5:19] So if I increase or decrease the green, we'll see that we're actually scaling that noise pattern in the y axis.
[5:26] If we do the red, we see the x and then in the blue, we have the z.
[5:31] So that's how you have a lot of control over this pattern.
[5:34] And, you know, you can mix it in different ways.
[5:36] You can even do, I don't know what a gamma, I guess you can use the gamma a little bit, kind of breaks it, but it's mainly these three color channels to scale it.
[5:45] And that's kind of the main idea to get these patterns.
[5:49] So how can we use this like practically other than what I just explained?
[5:53] So in this project, which is available in the description below if you guys are interested, I created some extra drips on the wheels of this car.
[6:03] So if I gain up here, we can see there's some little drips and details on this car.
[6:09] So I'm just going to go to my example and show you guys exactly what that is.
[6:14] So if I gain up a little bit, we can see that's what's happening.
[6:18] So I'm going to go before.
[6:19] We see there's kind of a wheel, but there's no high frequency, little details on there.
[6:24] So what I did was I created an expression with that pattern, just using the position pass of the car that comes with the CG render.
[6:32] And I'm just gaining up a little bit using that pattern.
[6:37] So we get the kind of base highlight of the water drips.
[6:41] And then what I did was I shuffled out the alpha channel into the color channels.
[6:47] So what is that doing?
[6:48] Not much is putting it just in all the channels, but what it allows us to do is easily key and make these dots smaller.
[6:55] So I keyed the already result that's here to get tiny drips basically in the same position as the other ones.
[7:05] And then I just put those on top as well.
[7:07] So now we start to get small highlights, small specular highlights on the drips of the tire.
[7:14] And the last thing I did was I took that same expression, this pattern, and I transformed it in its own stream here by one pixel.
[7:26] So I'm moving it over by one pixel and then I'm using that to darken.
[7:30] So it's actually creating a simple drop shadow effect on our drips.
[7:34] So we get more of a 3D looking drip on the surface where we want it.
[7:38] And that's a way that we can add a little bit of surface drips.
[7:41] And if I go back to the normal exposure, it just adds a little bit of detail that catches your eye if you're looking in that area.
[7:49] And that's kind of the level of detail that we can get into on shots if you want.
[7:55] So that's kind of the theory and the principle.
[7:58] Hopefully you guys got something out of it.
[8:00] If you liked the video, hit the like button.
[8:02] It really helps the YouTube algorithm in helping the channel grow and I can produce more content like this.
[8:07] So thanks so much.



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
