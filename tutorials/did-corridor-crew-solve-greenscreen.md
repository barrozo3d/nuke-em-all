---
title: Did Corridor Crew SOLVE Greenscreen?
source: YouTube
url: https://www.youtube.com/watch?v=abNygtFqYR8
author: Compositing Academy
ingested: 2026-08-14
app: "Nuke"
version: "not specified — comparison includes native Nuke keyers (Keylight, IBK) vs. 'Corridor Key', a free neural-network keyer gizmo released by Corridor Digital (3rd party, distributed as a Nuke node/group, not a Foundry feature)"
tags: [keying, compositing, ai-tools, gizmo, edge-extending, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/did-corridor-crew-solve-greenscreen/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Did Corridor Crew SOLVE Greenscreen?

**Source:** [YouTube](https://www.youtube.com/watch?v=abNygtFqYR8)
**Author:** Compositing Academy
**Duration:** 19m17s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below. Condensed transcript summary (full timestamped version retained in git history at commit eae0e47):

[0:00] Corridor Digital released a neural-network keyer ("Corridor Key") claiming to fix the classic edge-color-contamination problem by predicting/extending correct edge color.
[1:13] Four adversarial test plates set up "the way a supervisor would look at edges": (1) transparency + motion blur on an imperfect screen, (2) a shaken dress with fine detail + green-screen gradient, (3) flat green vs. a bright orange pumpkin (complementary color, noisy plate), (4) a defocused edge over a messy/detailed background ("nightmare" case).
[2:37] Plate 1: Keylight default has dark/discolored edges; Screen Balance and Edge Extend help but Edge Extend fails on motion-blurred regions (traditionally requires frame-by-frame hand-painting). IBK + clean plate gives a solid despill but loses some motion blur/dark glass detail. Corridor Key's predicted color + alpha (despilled afterward manually, since it wasn't trained on despilled footage) beats IBK, retaining motion blur slightly better, though shows temporal flicker traced to instability in its input alpha hint. Winner: Corridor Key.
[9:00] Plate 2: Keylight struggles with the green-screen gradient; IBK + clean plate improves but still shows dark edges; Corridor Key handles the gradient better and wins again, though presenter would still blend it with IBK rather than use alone — one bright peach prop defeats all three keyers equally.
[12:34] Plate 3: tests despill specifically. Keylight's screen-balance despill shifts skin/shirt toward pink; IBK's screen subtraction despills well with the same pink-shift side effect; Corridor Key does NOT despill well and has no despill controls of its own — ties/loses to Keylight, IBK judged overall winner for this plate. Also noted: Corridor Key failed on a wider/less-tightly-cropped version of the same shot, suggesting training data expects tight greenscreen framing.
[16:00] Plate 4 (defocus "nightmare"): all three keyers show visible creasing/patterning in the alpha where a smooth defocus edge is expected. Corridor Key judged the best starting point but still needs manual fixup — roto-paint solid extended color into RGB, and either hand-draw a replacement roto shape for the alpha edge or roto-paint a blurred patch to fake believable defocus falloff.
[18:56] Overall verdict: keying "is not dead" — Corridor Key wins on edge-contamination-heavy plates but loses/ties on despill-heavy and defocus-heavy cases, and is never a one-shot final key on any plate; always meant to blend with a traditional keyer's result.

---

## Captured Frames

- [0:44] tutorials/frames/did-corridor-crew-solve-greenscreen/frame_000.jpg
- [3:00] tutorials/frames/did-corridor-crew-solve-greenscreen/frame_001.jpg
- [5:11] tutorials/frames/did-corridor-crew-solve-greenscreen/frame_002.jpg
- [6:14] tutorials/frames/did-corridor-crew-solve-greenscreen/frame_003.jpg
- [10:57] tutorials/frames/did-corridor-crew-solve-greenscreen/frame_004.jpg
- [13:11] tutorials/frames/did-corridor-crew-solve-greenscreen/frame_005.jpg
- [16:05] tutorials/frames/did-corridor-crew-solve-greenscreen/frame_006.jpg

---

## Structured Notes

### Core Technique
Head-to-head keying comparison across 4 deliberately hard greenscreen test plates (motion blur + transparency, heavily shaken small detail, flat green vs. a bright complementary color, defocused edge over a messy background) evaluating Nuke's stock Keylight, the IBK (Image Based Keyer) gizmo with a clean plate, and "Corridor Key" — a free neural-network keyer released by Corridor Digital that claims to fix edge color contamination by predicting/extending the correct edge color via a trained model.

### Summary
Corridor Digital released a neural-network keyer claiming to solve the classic green-fringe/edge-contamination problem — where semi-transparent edge pixels pick up spill color that traditional keyers can't cleanly remove without hand-painting. The video tests it against Keylight and IBK on 4 plates supervisor-style. Plate 1 (motion blur + transparency, imperfect screen): Keylight's default result has dark/discolored edges that edge-extending only partially fixes (edge-extend fails on motion-blurred regions, which normally require frame-by-frame hand-painting); IBK with a clean plate gives a solid despill but loses some motion blur and dark glass detail; Corridor Key's raw output (a "contaminated color" prediction plus alpha, combined with a manually-added Despill afterward since it wasn't trained on despilled footage) beats IBK here, retaining motion blur slightly better, though it shows some temporal flicker traced back to instability in the alpha hint it was fed. Plate 2 (shaking dress, green screen gradient): Keylight struggles with the gradient out of the box; IBK with a clean plate improves on it but still shows dark edges; Corridor Key handles the gradient better and is judged the winner again, though the presenter would still blend it with IBK's result rather than use it alone, and one bright peach-colored prop defeats all three keyers equally. Plate 3 (pumpkin vs. bright orange complementary color, plus noise): tests despill quality specifically — Keylight's screen-balance despill works but shifts skin/shirt color toward pink; IBK's screen subtraction does a good despill with the same pink-shift side effect; Corridor Key does NOT despill well here and has no despill controls of its own, so it ends up tied-or-behind Keylight and loses to IBK overall for this plate — also noted: Corridor Key failed when tested on a wider/less-tightly-cropped version of the same shot, suggesting its training data expects tight greenscreen framing. Plate 4 (defocused edge over a detailed, messy background — the "nightmare" case): all three keyers produce visible creasing/patterning in the alpha where a smooth defocused edge is expected; Corridor Key is judged the best starting point but still requires manual fixup — roto-painting a solid extended color into the RGB and either replacing the alpha edge with a hand-drawn roto shape or roto-painting a blurred patch to restore a believable defocus falloff. Overall verdict: Corridor Key wins 2 plates outright, ties/loses on despill-heavy and defocus-heavy cases, and is never presented as a one-shot final key on any plate — always meant to be blended with a traditional keyer's result. Conclusion: keying is "not dead," and AI tools are additive to the traditional keyer toolkit rather than a replacement.

### Key Steps
1. Build a deliberately adversarial test set: (a) motion blur + transparency on an imperfect screen, (b) small shaken detail with a green-screen gradient, (c) flat green vs. a bright complementary-color prop plus sensor noise, (d) a defocused edge passing over a detailed/messy background.
2. For each plate, key with Keylight first using default settings (no fine-tuning) to establish a baseline; note edge darkening/discoloration.
3. Diagnose edge contamination by pushing Screen Balance (can shift plate color — use carefully) and applying an Edge Extend as a first fix; recognize edge-extend's core limitation — it does not work on motion-blurred regions, which traditionally require frame-by-frame hand-painting of solid edge color.
4. Re-key with IBK, generating and plugging in a clean plate (paint out the subject from a reference frame) to drive Screen Subtraction for despill; compare against the default/no-clean-plate result.
5. Run the same plate through the Corridor Key gizmo: feed it the plate, receive back a predicted/"contaminated" edge-color result plus an alpha ("alpha hint"-driven); since it wasn't trained on despilled footage, apply a separate despill (e.g. Despill Madness) afterward for a fair comparison against IBK/Keylight's built-in despill.
6. Compare all three results directly (toggle/wipe) per plate on identical backgrounds, judging edge cleanliness, motion-blur retention, temporal stability, and despill accuracy; call a per-plate winner rather than assuming one keyer wins everywhere.
7. Where Corridor Key's alpha hint carries an artifact (e.g. flicker on glass), trace it back to the input alpha and consider re-feeding it a more stable hand-tuned Keylight alpha instead of Corridor Key's own default hint.
8. For unfixable residual problems (defocus-edge creasing in the alpha, single stubborn colored props that defeat every keyer), fall back to manual roto/paint: extend RGB color with roto-paint or clone-stamp, and either hand-draw a replacement roto shape for the alpha edge or roto-paint a blurred patch to fake a believable defocus falloff.
9. Treat the AI keyer's output as one input among several to mix/key-mix together, not a standalone final key.

### Nodes / Tools / Settings
- Keylight — Nuke's default/most common keyer; Screen Balance control (careful: can shift plate color); paired with EdgeExtend for edge-color restoration (does not fix motion-blurred edges)
- IBK (Image Based Keyer) gizmo — driven by a clean plate; Screen Subtraction toggle for despill
- Corridor Key — free neural-network keyer gizmo/group node released by Corridor Digital (3rd party); outputs a predicted edge-corrected color plus an alpha derived from an "alpha hint" input; has no built-in despill controls (must pair with a separate despill node/technique such as Despill Madness)
- RotoPaint — for manual solid-color edge extension and hand-drawn alpha-edge replacement/blurred-patch fixes on unsolvable defocus/motion-blur cases
- KeyMix (referenced conceptually) — for blending multiple keyers' results together rather than trusting one in isolation

### Difficulty
Advanced — requires supervisor-level judgment comparing keyer outputs across edge cases (motion blur, gradients, despill, defocus), not a beginner keying tutorial.

### Foundry App & Version
Nuke; exact version not stated on-screen. Keylight and IBK are native Nuke tools; Corridor Key is a free third-party gizmo/group node released by Corridor Digital, not a Foundry product — this comparison is about a competing free AI keyer, not a native Nuke feature.

### Tags
keying, compositing, ai-tools, gizmo, edge-extending, intermediate

---

## Related Tutorials
- Rotoscoping in Nuke Tutorial | 5 Beginner Tips (tutorials/rotoscoping-in-nuke-tutorial-5-beginner-tips.md) — shares compositing; roto fundamentals used in this video's manual edge-fixup fallback.
- How SMART is State of the Art A.I Rotoscoping? (tutorials/how-smart-is-state-of-the-art-ai-rotoscoping.md) — shares ai-tools, compositing; same channel's pattern of rigorously benchmarking a new AI tool against hard test cases before recommending it.
