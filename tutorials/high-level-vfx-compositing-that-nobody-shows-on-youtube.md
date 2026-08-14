---
title: High Level VFX Compositing that Nobody Shows on Youtube
source: YouTube
url: https://www.youtube.com/watch?v=GTfxuJftv_I
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "not specified"
tags: [compositing, grading, relighting, aovs, digital-matte-painting, fx-simulation, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/high-level-vfx-compositing-that-nobody-shows-on-youtube/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# High Level VFX Compositing that Nobody Shows on Youtube

**Source:** [YouTube](https://www.youtube.com/watch?v=GTfxuJftv_I)
**Author:** Compositing Academy
**Duration:** 15m6s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey guys, welcome to this video. We're going to be talking about how to take a version zero comp.
[0:04] Sometimes the studios are called slap comps or bash comps up to a final shot.
[0:08] So a lot of times in tutorials, you're kind of focused on like one specific technique or method on a specific shot.
[0:14] But this video is really focused more on the iteration between versions on a comp.
[0:18] So you can actually see the hundreds of micro decisions that compositors have to make to develop images.
[0:24] Usually, after you've composited hundreds or thousands of shots, this sort of becomes an intuition.
[0:28] But my goal is to break down that intuition into principles or methods that you can actually figure out and break down shots on your own.
[0:35] So this is going to be kind of like a 20 minute deep dive into those versions.
[0:38] But if you want to get the full course, there's actually six hours of content available and you can get all the assets and the additional training
[0:44] and we dive into a bunch of other concepts as well.
[0:46] You'll also get a pretty cool shot on your demo reel at the end of it.
[0:49] So let's jump into the comp.
[0:50] If we just slap in the footage, there's going to be a few discrepancies that you know, you're going to start to see initially.
[0:56] This doesn't even have the background yet.
[0:57] So literally just one smoke layer and a graded a little bit orange and kind of get a gradient.
[1:03] But the first things I start thinking about when I'm starting comp is just a rough block in how how is the contrast going to look?
[1:09] And then how can we start to improve it?
[1:11] Like it's impossible to improve unless we have the starting point sort of like if you're sculpting a sculpture, you start with a few blocks of clay.
[1:17] And then you eventually will start with big, big chunks and then we'll start to refine.
[1:22] So this at least gives me an idea of the gradient across the shot.
[1:25] I'm always trying to create gradients on shots.
[1:28] It makes it more interesting wherever you can find a reason and you need to think about the reasons, but you need to find reasons to get gradients,
[1:35] whether that's a flare from offscreen and it kind of just slightly lifts one side of the screen or if it's like light hitting one side and fading off into darkness.
[1:44] Those are the kind of things I start looking for to start creating interest.
[1:48] Now we can already see a lot of discrepancies on the base comp.
[1:52] So having this is super useful because we can start to see things like the intensity of these highlights versus the highlights on the CG or the highlight here.
[1:59] Maybe this doesn't make entire sense if there's a big cloud in front of it.
[2:03] So that means we're going to have to break up that reflection.
[2:07] The tones are a little bit off.
[2:08] This is a little bit more pinkish than this is orange.
[2:10] So we need to balance those things out.
[2:12] Now one of the big things is just this whole area.
[2:15] Why it feels very cut out is the contrast ratio.
[2:19] So contrast ratio or the ratio between light and dark.
[2:24] Sometimes it's just a contrast thing where you need to gamma down.
[2:26] Like this might just need to gamma down, but sometimes it's actually the relationship between how much fill light there is and how much like spec light there is.
[2:35] Or like, let's say the highlights, how much fill versus like the brightest things.
[2:40] So for example, what I mean by that is we can see some highlights here.
[2:43] It's a little bit similar.
[2:44] This could be a little bit hotter.
[2:45] But the real big discrepancy here is how bright this shirt is compared to the chair.
[2:51] Right?
[2:51] So we have like, this is getting lit up quite a lot.
[2:54] This is getting lit quite odd.
[2:56] So is this.
[2:57] But then the chair looks very dark.
[2:58] So one of two things needs to happen.
[3:00] Either this needs to come down to get this closer.
[3:02] We need to get this element and this element closer.
[3:05] A lot of composing is just getting things to sit together.
[3:08] And right now they're not sitting together.
[3:10] And the other thing that's not working so well here is there's just a little bit of this like reflective highlight on the edge of the footage.
[3:17] So that's going to be the one one of the things when you take care of like, there's there's no light source coming from back here.
[3:22] The way that we're composing it, right?
[3:24] There's a chair that's blocking this person.
[3:27] So we shouldn't have any light really hitting this.
[3:30] So we need to suppress the edge, suppress the highlight.
[3:32] And there's it's not an uncommon thing to have to do that.
[3:35] The way that I actually saw this later in the comp is we're going to boost up that that fill light.
[3:39] Like to get it to similar level here.
[3:41] So the ratio is the same.
[3:42] So we have equal fill, like I said, the highlight and we'll do some edge blurring.
[3:46] And also I did a little bit of a gradient as well here.
[3:49] So the original plate actually gets lit all the way down, but maybe we want to cast a little bit of shadow from this edge.
[3:54] Just so we don't draw attention to like something super bright down in here where we would expect it that falls into shadow.
[3:59] So those are a few balancing things that we're going to start thinking about.
[4:03] Now we can also.
[4:05] Okay, let's just actually take a look at the next comp.
[4:08] So you just see the progression here.
[4:10] So this is the second step here.
[4:13] And we see some of the tones are getting a little closer together.
[4:16] Let's pay attention to the some of the color grading.
[4:19] See, this is a little bit.
[4:19] This was a little bit pinkish.
[4:21] See how orange that is.
[4:22] And this is slightly pinkish not by far, but just look here and look here.
[4:27] It's always these small color differences.
[4:29] But if you just get this a little bit warmer, a little bit less red in it, it starts to come closer.
[4:33] These are the small 5-10% differences in colors that it's good to get the those base tones sitting together as we as we progress.
[4:43] I also took a bit of this purplish tone out of the shirt.
[4:47] De-saturate slightly just so we have like a slightly more neutral tone to start.
[4:52] And we'll see how that progresses, but that's essentially the next step here.
[4:55] Now we have a background with the defocus applied.
[4:58] So this starts to give me an idea of, okay, where the fires placed.
[5:02] How are we going to sell the reflection on this light as well?
[5:05] So we have a light hitting here and here and here.
[5:10] So we know there's some kind of a light source up in this direction that's pretty much causing this.
[5:16] So we need to like sell like some kind of a light source up in this area that's enough to cast this.
[5:22] And right now it doesn't feel like that because even this cloud element doesn't quite feel lit.
[5:28] So that's a little bit odd.
[5:29] It's just like we have these bright highlights, but we don't have anything necessarily telling our brain that that's happening.
[5:33] Now there could be something technically like offscreen causing that, but right now it doesn't feel connected.
[5:39] So it's mostly just how do we make it feel connected?
[5:42] Now the other things that stand out to me in this image, again, this still feels very cut out.
[5:45] This is something I solved later.
[5:47] I just was focused on different things is sort of harsh contrast between here and here.
[5:54] It's just like this feels very black and we see like a very cut out element like looking like this.
[6:00] And sometimes that can happen, but a lot of times what I like to do is mix it with a thinner element.
[6:05] So I take a thicker element like this and I'll mix it with a thinner one.
[6:08] You see how over here it's like a little bit more blended where I have like we still see some detail,
[6:12] but there's something very thin behind it.
[6:15] So that's those kind of things catch my eye.
[6:16] It was very cut out looking things.
[6:18] I'm trying to avoid now other things that are introduced here with the background is this really.
[6:24] Extremely blown out highlight.
[6:26] There's a reflection probably in CG that needs to be suppressed.
[6:29] And so this immediately is literally the brightest thing in a comp.
[6:33] And so your eyes going to go there and then that's really distracting from where we supposed to be looking.
[6:37] Is this person the actions happening here and right now it's still the last place we're looking.
[6:42] This is the darkest thing, you know, all those things.
[6:44] So we need to take away the attention from the background and take away attention from the things we don't want to see and bring the attention to here.
[6:52] That is the that is what we're doing.
[6:54] We're compositing it.
[6:55] We're shaping the image.
[6:56] So if we go forward in time, this one, I just added a little bit of lens diffusion just to see how that's going to sit the blocks together a little bit better.
[7:05] This is always a I don't do this right off the bat because you can if you rely too much on it, your comps won't go as far,
[7:11] but it is a cheat a little bit in helping things sit together.
[7:14] So essentially it's very, very soft blurs on the on the image like blurring the image by like two or 300 pixels and then mixing that back to a very low number.
[7:22] What that does is it helps all the black levels sit together.
[7:25] So that's a good way to match the blacks kind of, but you still should match your blacks first before you do this.
[7:31] Don't over rely on it.
[7:33] But I just want to see what it looked like with some grain and setting the blocks together.
[7:37] That already helps quite a lot.
[7:40] We can go to the next version.
[7:42] So let's see the difference here.
[7:45] This is just adding the element, the embers in France, a particle system.
[7:49] We're also projecting embers on the surface of the geometry.
[7:52] We'll talk about all that stuff later on.
[7:57] And this is this is the really important step here.
[7:59] So here's where it's cut out.
[8:01] This is the kind of thing that a lot of junior composers will miss.
[8:03] They don't know what it is that's missing.
[8:05] But if you always go back to the fundamentals, what are we trying to do?
[8:08] We have to think about light, light and light direction.
[8:11] If you can remember those two things, you're going to do light, light direction and and ratio of light and and the amount of fill with amount of highlight,
[8:18] hitting things.
[8:19] If you can remember those few things, you're going to be able to do a lot of complex composites.
[8:25] Like that is the base of the knowledge.
[8:26] So here we just swap back and forth.
[8:29] You can really see the difference of when we start to shift those things.
[8:32] So see how bright, see how dark we brighten this up.
[8:35] Maybe we darken the edge a little bit and boom, like now this sits together a lot better.
[8:40] And those are the very small adjustments that's going to help a lot and also just help sell like how much spec.
[8:46] Like we have a very rough bright spec and we can kind of, you know, fake that in some of the diffuse.
[8:52] We just bring that up and bring it to a similar level there.
[8:57] This also involves breaking up some of the highlight now.
[9:00] So again, we have a very smooth highlight, but we have things that are including it.
[9:03] So in theory, we need to break that up.
[9:06] And so, you know, we're, I'll show you some techniques for, for getting that and also animating it through.
[9:10] So because we have a multi light setup here in this composite, the lights are rendered separately.
[9:15] We can actually occlude basically different pieces of it with animated textures.
[9:21] So it actually matches the elements that we're adding.
[9:24] That's what's really good about having the lights rendered separately.
[9:27] And in studio, sometimes they will give you these multi light setups for this reason.
[9:33] And okay, so let's keep going here.
[9:37] Now let's just see what we do in the background.
[9:39] So here I'm just exposing the background a bit more.
[9:41] So we're actually adding fire elements before it was just a few interactive basic reflections on the background CG.
[9:49] But we need to actually, you know, again, sell this idea.
[9:52] What is it exactly that's causing this?
[9:54] So if we can get something in there, that's a little bit hotter and it feels like that's justified.
[9:58] Now it starts to feel like things are a little bit more connected.
[10:02] And I did add some breakup on this nasty kind of yellow square that formed.
[10:08] I just didn't like it.
[10:09] So I kind of covered that up with darker elements and then broken up with brighter elements on top.
[10:14] And so we'll look at that too in detail.
[10:17] And also, so what happens here just by having a brighter element is going back to that one concept I was talking about where we're just creating a little bit of a harsh contrast on that cloud,
[10:26] which I wasn't that huge a fan of just seeing like very cut out things in the background.
[10:30] So there's a few ways you could do that.
[10:31] You could add a thin element around it.
[10:33] That's one technique I like to do.
[10:35] But the other thing is if there's something very bright,
[10:37] actually that will naturally reduce the contrast there as well.
[10:40] Because what happens is the glow itself, if we go to, let's see, like green, the glow from this is actually lifting the black level.
[10:51] So it's basically taking the darkest things and lifting it slightly.
[10:55] And that reduces the contrast between this cloud element and what's behind it.
[10:59] So a glow can also have that effect, especially like very diffusion.
[11:03] That's why diffusion and glows can help blend things together if they feel a little bit cut out, but it can also be overdone.
[11:09] So it's just like trying to find a sweet spot of not making everything just super glowy and overly, yeah, in that way.
[11:18] So another thing that I did here is the elements are actually scattering through the smoke as well now.
[11:25] So we have like smoke elements behind, but this is not only are we adding glow,
[11:29] but we're also adding scattering in the actual smoke itself because this should be receiving light passing through the atmosphere.
[11:37] So we need to make sure that we have those interactions happening to sell the effect.
[11:41] I think this version might have been clamped, version G to version H, because in this one we see a little bit more range.
[11:49] You got to be careful not to clamp your highlights.
[11:50] So if we look at this version, I think I had a clamped note on accident here and I realized it.
[11:55] I was like, that's not good.
[11:56] So we want to make sure we don't do that because it'll make your highlights nasty like this.
[12:01] You don't want to do that.
[12:03] So we'll look at QC at the end of all the stuff as we get there.
[12:08] And then the final result, I think.
[12:12] Let's see.
[12:13] We can also look at some of the other frames here as well because this explosion, I was probably the last thing I did just because it's almost like its own composite.
[12:23] So I'm just going to go back in time on some of these older ones.
[12:27] So we can look at the original.
[12:28] So here's like an explosion, but I actually really like this look because the glass becomes more apparent, how it passes through the glass.
[12:37] We're going to talk about that as well.
[12:39] But it doesn't make entire sense because there's a ton of smoke back there and that should cast through the smoke.
[12:45] So even though I really do like this look, I think this makes a lot more logical sense that all of that atmosphere that's between us,
[12:52] that very thick cloud, that really needs to receive the light.
[12:55] So we are going to be bold with how overexposed we go with the shot because that's what would actually happen.
[13:02] So that's the hard part sometimes.
[13:05] The hard part is losing the detail and being comfortable with doing that because the tendency is just to want to see everything.
[13:14] If we didn't have atmosphere in between, this would actually make a lot of sense.
[13:17] But this will work.
[13:20] And that's essentially, let's just see if we have any other notes between here.
[13:26] Because I did mess with the lens flares a little bit and different things like that.
[13:29] So I'm just trying to see if there's any other little pieces we can mention here.
[13:33] Yeah, so actually H is the last version.
[13:35] I think I got these numbers mixed up here.
[13:37] So there was just some artifacting here and just the QC stuff.
[13:42] We're going to go through and clean it up and any little details,
[13:45] any little little black edges and stuff like that.
[13:47] This is, you know, YouTube all that people aren't going to notice, but feature film, little black edge, little holdout issues,
[13:53] things where we've layered things.
[13:55] That's the kind of stuff that we just want to clean it up.
[13:57] So you see those little black edge and we can just fix that.
[14:01] So those are the tiny little details that we can do a pass on at the very end just to make sure we're hitting that level standard that this could be put on to a movie screen.
[14:11] That's subjective with all these classes really.
[14:13] It's just like how do we hit movie quality and give you the real experience of studio, not just putting the image together.
[14:19] So that's about it for just the overview.
[14:22] There's all obviously a lot of things we haven't talked about here in terms of like the parallax and movement and like all these elements and how they merge over each other.
[14:30] So we'll take a look at all that stuff next, but that gives you a good idea of the progression of sort of concepts you can think about.
[14:36] So if you if you need to rewatch this video to even just rewatch it and those are such important concepts I just covered.
[14:43] And if you can sort of absorb those ideas when you're looking at when it's not done, that's where it could be very useful because if you don't see the relationship, it's hard to know what to do.
[14:55] The nodes are easy.
[14:57] The nodes are easy.
[14:58] Developing the image is not easy.
[14:59] So, you know, those are the main the main ideas.



---

## Captured Frames

- [0:50] tutorials/frames/high-level-vfx-compositing-that-nobody-shows-on-youtube/frame_000.jpg
- [4:08] tutorials/frames/high-level-vfx-compositing-that-nobody-shows-on-youtube/frame_001.jpg
- [4:55] tutorials/frames/high-level-vfx-compositing-that-nobody-shows-on-youtube/frame_002.jpg
- [6:24] tutorials/frames/high-level-vfx-compositing-that-nobody-shows-on-youtube/frame_003.jpg
- [7:59] tutorials/frames/high-level-vfx-compositing-that-nobody-shows-on-youtube/frame_004.jpg
- [11:50] tutorials/frames/high-level-vfx-compositing-that-nobody-shows-on-youtube/frame_005.jpg
- [13:20] tutorials/frames/high-level-vfx-compositing-that-nobody-shows-on-youtube/frame_006.jpg

---

## Structured Notes

### Core Technique
Walks through the real version-by-version iteration (A through H) of a car-crash/explosion VFX shot from a rough "slap comp"/"bash comp" (studio terms for version zero) to final delivery, using each version diff to teach the underlying decision-making principles compositors use — not just the node techniques — condensed from a 6-hour full course.

### Summary
Starting from version zero — a single ungraded smoke layer with a rough orange gradient and no background — the video tracks the recurring judgment calls a compositor makes across versions: (1) establish a rough contrast block-in first ("you can't refine what you haven't blocked in," compared to sculpting clay), and deliberately look for reasons to add gradients across a shot (an offscreen flare lifting one side, light fading into shadow) because flat, ungradated images read as less interesting; (2) diagnose "elements not sitting together" as a contrast-ratio problem — specifically the ratio between fill light and highlight/spec light on different elements (e.g. a shirt lit brightly while a chair stays dark) — fixed by bringing the mismatched element's fill up or down to match, not just eyeballing brightness; (3) hunt down and suppress "impossible" light — e.g. a reflective highlight on an edge that shouldn't be lit given the established light logic (an occluding chair blocking that light path) — via edge suppression plus a touch of manual shadow gradient; (4) fix small (5-10%) color-temperature mismatches between elements (pinkish vs. orange tones) early, since these compound visually; (5) avoid "cut out" looking elements (hard-edged smoke/cloud silhouettes) by mixing a thick element with a thinner, softer one behind/around it so some edge detail survives, and note that both added glow/diffusion AND a bright adjacent highlight can reduce perceived edge contrast (a highlight's glow lifts the local black level, which is why diffusion/glow "blend" cut-out edges but can be overdone); (6) always ask "does this light make sense" for background elements too — an extremely blown-out background CG reflection with no justified light source is not just wrong, it actively steals viewer attention from the intended focal point (the actor), so attention has to be actively directed away from unintended hotspots and toward the subject; (7) use a very soft, huge-radius blur (200-300px) mixed back in at a low percentage as a "cheat" to help black levels visually sit together across composited layers — but only after doing proper black-level matching first, not as a substitute for it; (8) once particle/ember elements are added, revisit the same light/light-direction/ratio principles shot-wide — the author frames this as the single most important recurring lesson: "light, light direction, and the ratio of fill vs. highlight — if you can remember those, you can do a lot of complex composites"; (9) exploit a multi-light-pass render setup (lights rendered as separate elements) to occlude individual light contributions with animated textures so newly-added FX elements (embers, fire) interact correctly with the existing lighting, without re-rendering; (10) add scattering/glow interaction between new light sources and existing atmosphere/smoke elements so additions feel physically connected to the scene rather than pasted on top; (11) watch for accidental clamping between versions (an accidentally clamped node crushed the highlight range in one version) — always cross-check highlight range across versions during QC; (12) accept "losing detail" in favor of physical plausibility — a very thick foreground smoke/atmosphere layer should overexpose/wash out background detail when raytraced light passes through it, and a compositor has to be willing to blow out an area even if a lower-exposure version "looked cooler," because the overexposed version is what would actually happen physically; (13) final pass is dedicated purely to invisible-on-YouTube-but-critical QC — small black edges/holdout errors from element layering that would read on a cinema screen even if unnoticed on a compressed web video. Conclusion: "the nodes are easy — developing the image is not easy," i.e. the technical toolset is not the bottleneck, the perceptual/decision-making skill is.

### Key Steps
1. Block in a rough version-zero comp (single main element, rough grade, basic gradient) before attempting any refinement — establishes the baseline discrepancies to solve.
2. Deliberately look for a justified reason to add a gradient across the frame (offscreen flare, falloff into shadow) rather than leaving flat, undifferentiated light.
3. Diagnose "not sitting together" elements as fill-vs-highlight ratio mismatches between them, and bring the outlier element's fill level up or down to match its neighbor rather than adjusting contrast globally.
4. Identify and suppress any highlight/reflection that doesn't match the established light-logic of the scene (e.g. light hitting an area that should be occluded) via edge suppression, edge blur, and a manual shadow-gradient touch.
5. Match small (5-10%) color-temperature discrepancies between elements early (e.g. pinkish vs. orange) — desaturate/rebalance toward a shared neutral base tone.
6. For hard "cut out" looking silhouetted elements, mix in a thinner, softer secondary element behind/around the thick one to retain some edge detail instead of a flat silhouette.
7. Track down any "impossible" or unjustified extreme highlight (e.g. a blown-out background CG reflection) and suppress it — an unmotivated hotspot competes with and steals attention from the actual subject.
8. Apply a very soft (200-300px), low-opacity global blur as a late "cheat" to help black levels visually cohere across layers — only after proper black-level matching, never as a replacement for it.
9. When adding particle/ember/fire elements, re-apply the light/light-direction/fill-vs-highlight-ratio check across the whole shot again — new elements reset the balance.
10. Where lights were rendered as separate passes/elements (a multi-light setup), use that separation to occlude individual light contributions with animated textures so new FX elements interact correctly with existing lighting without a re-render.
11. Add scattering/glow interaction between new bright elements and existing atmosphere/smoke so additions read as physically connected to the environment, not composited on top.
12. QC for accidental clamping between comp versions by comparing highlight range across versions — a clamped node can silently crush highlight detail.
13. Be willing to intentionally overexpose/blow out a foreground atmosphere element when it's physically correct (thick smoke really would wash out background light), even if a lower-exposure alternative "looks cooler" — physical plausibility over personal preference.
14. Do a dedicated final QC pass hunting for small black edges/holdout errors from element layering — invisible on compressed web video but visible at cinema scale.

### Nodes / Tools / Settings
- Version-comparison workflow: a row of `Read` nodes (one per comp version, A through H) feeding into a switch/selector so versions can be directly A/B compared in the Viewer — shown as a thumbnail strip and as a row of colored Read nodes in the node graph.
- Multi-light-pass setup — lights rendered as separate elements/AOVs so individual light contributions can be independently occluded/adjusted per new FX element without re-rendering the base CG.
- Large-radius, low-opacity blur — used as a black-level-blending "cheat" late in the comp (200-300px blur, mixed back at a low percentage).
- Particle system + surface-projected embers — embers added both as a 2D particle system and projected onto CG geometry surfaces for grounded interaction.
- Glow/diffusion — used deliberately to reduce perceived edge contrast on cut-out-looking silhouettes (works by lifting local black levels), balanced against overuse.

### Difficulty
Intermediate/Advanced — the techniques themselves (grading, blurs, glow, roto/masking) are straightforward, but the judgment about *when and why* to apply them across dozens of iterative versions is the actual subject, aimed at compositors past the beginner stage who already know the node toolset.

### Foundry App & Version
Nuke; exact version not stated on-screen.

### Tags
compositing, grading, relighting, aovs, digital-matte-painting, fx-simulation, intermediate

---

## Related Tutorials
- 2 Expert VFX Tips to PERFECTLY Blend CG (`2-expert-vfx-tips-to-perfectly-blend-cg.md`) — shares `relighting`, `compositing`; overlapping "getting elements to sit together" methodology.
- This ONE Step Makes CG Look Cinematic (Most Artists Skip It) (`this-one-step-makes-cg-look-cinematic-most-artists-skip-it.md`) — shares `grading`, `aovs`, `compositing`; both about first-read/attention-direction and light-group-driven selective grading.
- How I Use Compositing to Skip THOUSANDS of Hours Rendering (`how-i-use-compositing-to-skip-thousands-of-hours-rendering.md`) — shares `compositing`; same channel's methodology-over-technique teaching style.
