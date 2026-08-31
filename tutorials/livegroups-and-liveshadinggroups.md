---
title: LiveGroups and LiveShadingGroups
source: Article
url: https://learn.foundry.com/katana/Content/ug/livegroups/livegroups.html
author: learn.foundry.com
ingested: 2026-08-31
app: Katana
version: 9.0v3
tags: [katana, nodegraph, group, katana-9, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/livegroups-and-liveshadinggroups/
frame_count: 0
frame_status: skipped
---

# LiveGroups and LiveShadingGroups

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/livegroups/livegroups.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** LiveGroups and LiveShadingGroups A LiveGroup node provides a way for you to import another Katana project into the current project, and reload it every time the current project is updated, either automatically (for example, on scene load or before batch rendering) or manually (through context menu options). A LiveGroup node’s source is expected to contain a Group or Group-like node in its root level. When loading a LiveGroup source scene, the first loaded Group node in the source scene defines the user parameters and child node contents of the target LiveGroup. LiveGroups provide a number of useful constructs for collaborative work between users, for sharing nodes between show, sequence, and shot levels, and for users working in parallel on the same shot. There are two primary cases for using LiveGroups: collaborative work between departments and collaborative work within a department. As an example of collaborative work between departments, an FX artist would pass a Katana project to a lighting artist that can then use that project as part of a lighting scene by loading it into a LiveGroup node. In this example, the FX artist is only interested in publishing their setup, while the lighting artist is only interested in importing the published project, as shown in the diagram below: As an example of collaborative work within a department, a shot or sequence lighting artist would make changes to a LiveGroup source on a shot, and could then publish the source scene back to the shot or sequence for other lighting artists to pick up, as shown in the diagram below: In addition to the existing .katana file extension, the .livegroup file extension has been introduced. For backwards compatibility, it is still possible to use a Katana project with the .katana file extension as a LiveGroup source. When publishing new LiveGroup sources using the Publish... or Publish and Finish Editing Contents... menu options, the .livegroup file extension is used. Any Katana project file can be used as a source of a LiveGroup node, and LiveGroup sources can be published as assets through Katana ’s Asset API. When a LiveGroup node’s contents are exported to a file, the .livegroup file extension is used to create it. When a LiveGroup is imported, you can choose whether to import either .katana or .livegroup files. Files with the extension .macro are not listed by default but if there are macros present in the file structure, you can select the macros option in the Types field in the Import Livegroup dialog. For more information on Asset Management and the asset publishing process, see Asset Management , or Asset Management System Plug-in API . By default, exported .katana files are binary, gzip-compressed archives in a .tar format, containing an XML scene description file as data. This format is archived and compressed because nodes may contain binary data. In contrast, the .livegroup extension uses uncompressed, unarchived, ASCII files in a format similar to .katana but with a dedicated extension for LiveGroup sources. This means that LiveGroups, by default, are written as plain text, uncompressed XML files. While .katana files contain project settings in addition to the nodes of the node graph document, as they represent Katana projects, .livegroup files only contain the XML representation of the parameters and children of the Group node that controls the LiveGroup interface and contents. Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
Importing another Katana project into the current one through a **LiveGroup** node, so the imported node graph reloads whenever its source changes — the mechanism Katana uses to share node setups between departments and across show, sequence and shot levels.

### Summary
A LiveGroup node references an external Katana project as its contents and reloads it on update, either automatically (on scene load, or before batch rendering) or manually from context-menu options. The source scene's first root-level Group node defines the LiveGroup's user parameters and child nodes, which makes any Katana project usable as a LiveGroup source and lets those sources be published as assets through Katana's Asset API. The page also introduces the dedicated `.livegroup` file extension and explains how it differs from `.katana` on disk: `.katana` is a gzip-compressed `.tar` archive wrapping an XML scene description, while `.livegroup` is plain, uncompressed ASCII XML holding only the parameters and children of the controlling Group node.

### Key Steps
1. Create a **LiveGroup** node in the node graph to stand in for a node setup authored in a separate Katana project.
2. Prepare the source project so it contains a **Group or Group-like node at its root level** — on load, the *first* Group node found there defines the target LiveGroup's user parameters and child node contents.
3. Import the source with the **Import Livegroup** dialog, choosing either a `.katana` or a `.livegroup` file. To pick up a macro instead, select the **macros** option in the dialog's **Types** field — `.macro` files are not listed by default.
4. Let the LiveGroup reload its source **automatically** (on scene load, or before batch rendering) or trigger a reload **manually** through the node's context-menu options.
5. Publish changes back with **Publish…** or **Publish and Finish Editing Contents…**; both write the `.livegroup` extension for new sources.
6. Export a LiveGroup's contents to a file — the export also uses the `.livegroup` extension.
7. For a pipeline, publish LiveGroup sources as assets through **Katana's Asset API** rather than passing files by hand (see *Asset Management* and the *Asset Management System Plug-in API*).
8. Apply the two collaboration patterns the page sets out: **between departments** (an FX artist publishes a project; a lighting artist loads it into a LiveGroup as part of the lighting scene) and **within a department** (a shot or sequence lighting artist edits a LiveGroup source and publishes it back for other lighting artists to pick up).

### Nodes / Tools / Settings
**Node:** `LiveGroup` — imports another Katana project into the current project and reloads it when the current project updates.

**Source requirement:** the source scene must contain a **Group or Group-like node in its root level**. The first loaded Group node in the source defines the target LiveGroup's user parameters and child node contents.

**Reload triggers:** automatic — on scene load, or before batch rendering; manual — through the node's context-menu options.

**Menu options:** `Publish…`, `Publish and Finish Editing Contents…` — both use the `.livegroup` extension when publishing new LiveGroup sources.

**Import Livegroup dialog:** file choice of `.katana` or `.livegroup`; the **Types** field has a **macros** option, needed because `.macro` files are not listed by default.

**File formats — the on-disk difference:**

| | `.katana` | `.livegroup` |
|---|---|---|
| Container | binary, gzip-compressed `.tar` archive | uncompressed, unarchived |
| Encoding | XML scene description as data | ASCII / plain-text XML |
| Why | nodes may contain binary data | dedicated extension for LiveGroup sources |
| Contents | project settings **plus** the node graph document's nodes | **only** the XML representation of the parameters and children of the controlling Group node |

**Backwards compatibility:** a `.katana` project is still valid as a LiveGroup source; any Katana project file can be used as one.

**Pipeline integration:** LiveGroup sources can be published as assets through Katana's **Asset API** — see *Asset Management* and the *Asset Management System Plug-in API*.

### Difficulty
Intermediate

### Foundry App & Version
Katana 9.0v3 (page served from the current Katana 9.0v3 documentation set)

### Tags
katana, nodegraph, group, katana-9, intermediate

---

## Scope note — what this page does and does not cover

The page is titled **"LiveGroups and LiveShadingGroups"**, but its body explains
**LiveGroups only**. `LiveShadingGroup` appears in the title and breadcrumb and is
never defined, described or contrasted with a LiveGroup anywhere in the text. It is
recorded as still-missing in `KNOWLEDGE_GAPS_TODO.md` rather than inferred here.

Also referenced but not ingested: **Asset Management** and the **Asset Management
System Plug-in API**, which this page links to as the route for publishing LiveGroup
sources as assets.

---

## Related Tutorials
- [OpScript Tutorials](opscript-tutorials.md) — shares `katana` + `nodegraph`; a LiveGroup packages a Group node's children for reuse across projects, while OpScript's `Interface` API builds and edits scene graph locations procedurally — the two routes Katana offers for reusing work rather than rebuilding it by hand.
- [Setting up UsdPreviewSurface Materials](setting-up-usdpreviewsurface-materials.md) — shares `katana` + `nodegraph`; the NetworkMaterialCreate setup built there is exactly the kind of self-contained node group a LiveGroup is meant to publish and share between departments.
- [GafferThree](gafferthree.md) — shares `katana` + `katana-9`; GafferThree's **Export Rig** writes a lighting rig to a `.rig` file for reuse, the same share-and-reload problem LiveGroups solve at whole-project scale.
