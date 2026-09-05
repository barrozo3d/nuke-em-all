---
title: Writing EXR Metadata from Katana
source: Article
url: https://learn.foundry.com/katana/Content/ug/rendering_scene/openexr_header_metadata.html
author: learn.foundry.com
ingested: 2026-09-04
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
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
