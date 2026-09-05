---
title: Writing EXR Metadata from Katana
source: Article
url: https://learn.foundry.com/katana/Content/ug/rendering_scene/openexr_header_metadata.html
author: learn.foundry.com
ingested: 2026-09-04
app: "Katana"
version: "9.0 (learn.foundry.com/katana current docs at ingest; release notes whats_new_9.0)"
tags: [katana, python-scripting, katana-9, advanced]
extraction_status: complete
frames_dir: tutorials/frames/writing-exr-metadata-from-katana/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Writing EXR Metadata from Katana

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/rendering_scene/openexr_header_metadata.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Writing EXR Metadata from Katana It is possible to create custom EXR metadata fields in Katana disk renders in both Arnold and RenderMan. This can be created using AttributeSet nodes. In the AttributeSet node, set the attributeName at /root to renderSettings.metadata. attrib .[key|value|prefix] where attrib is an arbitrary attribute identifier. You will need to include key or value to output metadata to the EXR. Note: If there is no prefix, the property will be exr/katana: key = value . If a prefix is specified, the property will be exr/ prefix :katana: key = value . For example, setting a value (with ‘dummy’ as the attribute identifier): OpenEXR Header Metadata Warning: This is only currently supported by RenderMan. An alternative method for adding arbitrary metadata to OpenEXR headers for RenderMan is to use the OpScript node. To do this, you can create attributes under exrheaders and use the OpScript node targeting the /root location to set the following: local EXR_String = "renderSettings.outputs.primary.rendererSettings.exrheaders.test_string" local EXR_String_Value = StringAttribute("A String") Interface.SetAttr(EXR_String, EXR_String_Value) local EXR_Integer = "renderSettings.outputs.primary.rendererSettings.exrheaders.test_int" local EXR_Integer_Value = IntAttribute(1) Interface.SetAttr(EXR_Integer, EXR_Integer_Value) local EXR_IntegerArray = "renderSettings.outputs.primary.rendererSettings.exrheaders.test_intArray" local EXR_IntegerArray_Value = IntAttribute({1,2,3,4}) Interface.SetAttr(EXR_IntegerArray, EXR_IntegerArray_Value) local EXR_Float = "renderSettings.outputs.primary.rendererSettings.exrheaders.test_float" local EXR_Float_Value = FloatAttribute(1.5) Interface.SetAttr(EXR_Float, EXR_Float_Value) local EXR_FloatArray = "renderSettings.outputs.primary.rendererSettings.exrheaders.test_floatArray" local EXR_FloatArray_Value = FloatAttribute({2.6,3.8}) Interface.SetAttr(EXR_FloatArray, EXR_FloatArray_Value) Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
Write custom OpenEXR metadata from a Katana disk render either declaratively with an **AttributeSet** node under `renderSettings.metadata`, or — RenderMan only — by setting `exrheaders` attributes from an **OpScript**.

### Summary
A small page with exact syntax, which is the kind that saves an afternoon. The portable route works in **both Arnold and RenderMan**: an **AttributeSet** node at `/root` sets `renderSettings.metadata.<attrib>.[key|value|prefix]`, where `<attrib>` is an arbitrary identifier and **`key` or `value` must be included for anything to be written**. The `prefix` component decides the property's namespace in the file — with no prefix the property is `exr/katana:key = value`, and with one it becomes `exr/<prefix>:katana:key = value`. The second route is **RenderMan-only** and goes through **OpScript** targeting `/root`, building attributes under `renderSettings.outputs.primary.rendererSettings.exrheaders.*` with `Interface.SetAttr` and typed Lua attribute constructors — `StringAttribute`, `IntAttribute` (scalar and array), `FloatAttribute` (scalar and array) — which is also a compact demonstration of Katana's OpScript typing model.

### Key Steps
1. **Portable route:** add an **AttributeSet** node and target **`/root`**.
2. Set `attributeName` to **`renderSettings.metadata.<attrib>.key`** and/or **`.value`** — an arbitrary `<attrib>` identifier groups them; **omitting both key and value writes nothing**.
3. Add **`.prefix`** to namespace the property: no prefix yields `exr/katana:key = value`, a prefix yields `exr/<prefix>:katana:key = value`.
4. ⚠️ **RenderMan-only route:** use an **OpScript** node targeting `/root` and set attributes under `renderSettings.outputs.primary.rendererSettings.exrheaders.<name>`.
5. Build values with the typed constructors and `Interface.SetAttr` — `StringAttribute("A String")`, `IntAttribute(1)`, `IntAttribute({1,2,3,4})`, `FloatAttribute(1.5)`, `FloatAttribute({2.6,3.8})`.
6. Note this is a **disk render** feature — the metadata is written into the rendered EXR.

### Nodes / Tools / Settings
- **AttributeSet** node at `/root`; `attributeName` = `renderSettings.metadata.<attrib>.[key|value|prefix]`. Supported by **Arnold and RenderMan**.
- Resulting property form: `exr/katana:key = value`, or `exr/<prefix>:katana:key = value`.
- **OpScript** node at `/root` (⚠️ **RenderMan only**): `renderSettings.outputs.primary.rendererSettings.exrheaders.<name>`.
- Lua API: `Interface.SetAttr(path, value)`; `StringAttribute`, `IntAttribute` (scalar / array), `FloatAttribute` (scalar / array).

### Difficulty
Advanced

### Foundry App & Version
Katana 9.0. The AttributeSet route covers Arnold and RenderMan; the `exrheaders` OpScript route is RenderMan-only, and the page says so explicitly.

### Tags
`katana`, `python-scripting`, `katana-9`, `advanced`

---

## Related Tutorials
- [OpScript Tutorials](opscript-tutorials.md) — the `Interface` API and Lua attribute types used here.
- [RenderOutputDefine](renderoutputdefine.md) — the render outputs whose `rendererSettings` these attributes hang off.
- [Performing a Render](performing-a-render.md) — the disk render this metadata is written by.

---

> **Provenance.** `learn.foundry.com/katana` (MadCap Flare). Paths in this doc set
> are not guessable and `Data/Tocs/*` 404s, so this page was reached by crawling
> from `Content/learn_katana.html` → `user_guide.html`, or from a sibling page's
> own links. Reference-guide and user-guide pages carry clean `<title>`s and need
> no `--title` override, unlike `learn.foundry.com/nuke/developers/**`.
