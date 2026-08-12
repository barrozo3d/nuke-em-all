# Nuke 15.1 — Release Notes

**Released:** 2024-06-14
**Type:** Stable

## Added
- **New USD 3D system (beta): time-remapping** — new Fractional Time mode; GeoImport and GeoReference nodes gain time-remap options; backend improvements make stage-building in large 3D scenes faster.
- **Nuke Studio Timeline Viewer**: Saturation slider (previously Comp Viewer only); redesigned A/B Compare controls for QC workflows.
- **CopyCat**: context-menu additions to manage multiple training runs (resume, delete, create-inference-from-run); mixed-precision training for up to 2x faster training.
- **NDI streaming**: Display Mode knob controls for independent resolution/frame-rate management.
- **Full OTIO roundtrip support** — timeline data can now round-trip through OpenTimelineIO across pipeline apps without lossy conversion.
- OpenAssetIO integration extended to additional ingest nodes (Frame Range, Original Range, Colorspace properties exposed).
- **BlinkScript**: layer channel mapping unlocked, supporting up to four image layers; documentation/learning resources rebuilt.
- USD version selection flexibility via environment variable; USD bumped to 23.11.
- File format: DNxHD `.mxf` writing, RED R3D SDK 8.4.0, MOV Data Range support, Sony RAW SDK 5.0.0.
- PyTorch library upgrade with improved Mac performance for ML tools.

## Breaking Changes & Migration Notes
- **What breaks:** Tutorials describing OTIO export/import as "lossy" or requiring manual cleanup after round-tripping predate 15.1's full roundtrip support — that friction is reduced from this version on.
  **Workaround:** N/A — this is a strict improvement; older workaround steps for OTIO roundtrip issues can generally be skipped on 15.1+.

## Sources
- https://learn.foundry.com/nuke/content/release_notes/nuke_15.1.html
- https://www.cgchannel.com/2024/06/foundry-releases-nuke-15-1-nukex-15-1-and-nuke-studio-15-1/
