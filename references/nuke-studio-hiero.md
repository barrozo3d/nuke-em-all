# Nuke Studio / Hiero Reference

Nuke Studio is Nuke's editorial/conform/review layer, built on the same underlying engine as **Hiero** (Foundry's standalone editorial-and-review tool) and **HieroPlayer** (the free review-only variant) — the three share a timeline/project model, and Nuke Studio additionally embeds the full Nuke compositing environment so shots can be opened directly from the timeline into a compositing script.

## Core concepts
- **Project / Bin** — Nuke Studio organizes footage, sequences, and comp scripts in a Bin (media-management panel), distinct from the Timeline itself.
- **Timeline / Sequence** — standard NLE-style multi-track timeline (video + audio tracks, transitions, retiming) used for conforming an edit (matching a locked editorial cut) rather than for finishing a comp.
- **Track Item** — a single clip placed on the timeline; can be linked to a Nuke comp script (a "Build Track" or explicit "Export"/"Open in Nuke" workflow generates or attaches a `.nk` script per shot from the timeline item).

## Conform workflow
"Conforming" means matching Nuke Studio's timeline to an editorial cut delivered from an offline edit (e.g. an EDL/AAF/XML from Avid/Premiere), so each shot's in/out points and shot order match what the edit department locked. Typical flow: import the offline edit's EDL/AAF/XML, relink/conform the referenced media (or higher-resolution/VFX-plate versions of it) onto the timeline, then use that conformed timeline as the source of truth for which frame ranges each VFX shot needs.

## Shot export / comp creation
Nuke Studio can batch-generate per-shot Nuke comp scripts directly from timeline selections (each Track Item becoming its own `.nk` script with Read nodes pre-wired to the correct frame range and a Write node templated per the studio's naming convention) — this is the main reason productions use Nuke Studio over plain Hiero when compositing is happening in-house: it removes the manual "find the right frame range and build a fresh script" step per shot.

## Review
- Built-in review/annotation tools (frame-accurate notes, drawing/markup, side-by-side/wipe compare between versions) — the same review engine ships in standalone Hiero and the free HieroPlayer, so a director/supervisor without a Nuke license can still review and annotate using HieroPlayer while the annotations round-trip back to the artist's Nuke Studio/Hiero session.
- Version management: a Track Item can carry multiple **Versions** (e.g. v001, v002 of the same shot's comp render), with quick version-switching/compare directly on the timeline — this is the mechanism that makes Nuke Studio useful as a dailies/review tool across an entire reel, not just a single shot.

## Where this sits relative to plain Nuke compositing
Nuke Studio/Hiero is the editorial/organizational layer *around* compositing, not a compositing tool itself — once a shot is opened from the timeline, all the actual node work happens in the same Nuke environment documented in `nuke-compositing-nodes.md`. Studios without an editorial/conform need (freelance, small-scale work) often never touch Nuke Studio at all and work purely in plain Nuke.
