# Katana 7.0 — Release Notes

**Released:** 2023-11-01
**Type:** Stable
**VFX Reference Platform:** CY2023 (Python 3.10.10, Qt 5.15.2, OpenEXR 3.1.4, USD 23.05)

## Added
- **Native USD framework** — same architectural family as Nuke's new USD-based 3D system. Direct USD manipulation without conversion round-trips; the same node set introduced in 6.5 (UsdActiveSet, UsdAttributeSet, UsdMetadataSet, etc.) ships as stable here.
- **Live Rendering up to 2x faster.**
- **Scene Explorer tab**, **Attributes tab** USD support, and **OpenVDB volume support** (see Katana 6.5 notes — identical feature set, newer platform).

## Changed
- Native USD nodes are visually distinguished with a **light-blue background and blue stripe** in the Node Graph.
- Cache pre-population is disabled by default under the new (6.5-introduced) cache-eviction modes.
- **Experimental Geolib3-MT runtime removed** (carried over from 6.5).

## Breaking Changes & Migration Notes
- **What breaks:** Same as Katana 6.5 — Geolib3-MT is gone; tooling should use the cache-eviction-mode system.
  **Workaround:** See Katana 6.5 notes.
- **What to watch for:** This is the first *non-parallel* release where the native USD framework is the mainline recommended approach going forward — tutorials from 6.0 and earlier describing Katana's older (non-native, conversion-based) USD interop are increasingly outdated as native USD nodes (UsdIn, UsdActiveSet family, etc.) become the standard path in 7.0+.
  **Workaround:** Prefer native Usd* nodes over older USD-conversion-node chains when following pre-6.5 tutorials.

## Sources
- https://www.foundry.com/news-and-awards/foundry-releases-katana-70
- https://www.cgchannel.com/2023/11/foundry-releases-katana-7-0/
- https://learn.foundry.com/katana/content/release_notes/whats_new_7.0.html
