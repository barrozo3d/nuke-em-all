# Mari 7.1 — Release Notes

**Released:** 2024-12-09 (beta posted 2024-10-11)
**Type:** Stable
**VFX Reference Platform:** CY2023 (unchanged from 7.0 — two specs behind current at time of release)

## Added
- **2D Paint Mode** — create/edit 2D images natively without needing an external app like Photoshop; supports Paint Buffer, Node Graph, and Layer Stack. New **`.mrimg`** file format for exporting 2D work.
- **Image Write node** — new node type for 2D workflows; auto-updates baked images in the Image Manager.
- **Switch node** — toggle between different Node Graph sections to create texture variants (e.g., clean vs. dirty states) without duplicating the whole graph.
- Node Graph: Backdrop nodes are now selectable by clicking anywhere inside them; node-graph sections can be saved as reusable **Node Packages**.
- Color Presets/swatches available when creating Paint nodes, with custom swatch support.
- **Grunge Shelf** — pre-built Smart Masks contributed by Digital Domain's Stuart Ansley.

## Changed
- **"Custom Procedurals" renamed to "Smart Masks"** — aligning Mari's terminology with Adobe Substance 3D Painter's naming convention. Any tutorial referencing "Custom Procedurals" is describing what's now called Smart Masks.
- Pricing: $86/month or $689/year individual; $1,169/year teams.

## Breaking Changes & Migration Notes
- **What breaks:** Tutorials/UI references to "Custom Procedurals" (menus, panel names) predate this rename — the feature still exists functionally, just under a new name and (likely) reorganized menu location.
  **Workaround:** Mentally substitute "Smart Masks" wherever an older tutorial says "Custom Procedurals"; underlying node behavior is the same feature carried forward.

## Sources
- https://www.cgchannel.com/2024/12/foundry-releases-mari-7-1/
