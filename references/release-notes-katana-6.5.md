# Katana 6.5 — Release Notes

**Released:** 2023-11-01 (announced alongside Katana 7.0; v2 patch released 2023-12-19)
**Type:** Stable — **parallel release track**: same new features as Katana 7.0, pinned to the prior VFX Reference Platform generation for studios not ready to move.
**VFX Reference Platform:** Not explicitly stated in the fetched marketing release notes — unverified, but consistent with the parallel-release pattern seen elsewhere (Nuke x.1/x.2, Katana x.5), presumed to stay on CY2022 vs. Katana 7.0's CY2023. Verify against the official point-release PDF if precision matters.

## Added
- **Native USD workflow nodes**: UsdActiveSet, UsdAttributeSet, UsdMetadataSet, UsdRelationshipSet, and related nodes for setting attributes/metadata on prims via non-destructive overrides.
- **FnUsdAbstraction** — framework for studio-specific custom USD implementations.
- **NodeUSD class** for USD-native processing; new Engine plug-in system for building custom nodes/engines.
- **Scene Explorer tab**: expansion-based loading for USD locations (deferred recursive expansion), USD Viewer Visibility Working Set, Payload Working Set (with load-state icons), Active Prim Working Set.
- **Attributes tab**: now displays USD property values for selected locations, with Kind/Type icons and authored-vs-defaulted state badges; supports both USD Attribute and Relationship values.
- **Performance**: multi-threaded live-rendering updates via Foresight+ (revertible to "classic" mode); three cache-eviction modes — Dependency Protecting (default), Continual, Relaxed.
- **OpenVDB volumes** now visible in the Hydra viewer; UsdVol importing via UsdIn/UsdToKatana.

## Removed / Deprecated
- **Geolib3-MT (Experimental) runtime removed**, superseded by the new cache-eviction-mode system.

## Breaking Changes & Migration Notes
- **What breaks:** Any pipeline/tooling still explicitly toggling the experimental Geolib3-MT runtime will find it gone.
  **Workaround:** Use the new cache-eviction modes (Dependency Protecting / Continual / Relaxed) instead — pick based on the same performance trade-offs Geolib3-MT was targeting.

## Sources
- https://learn.foundry.com/katana/content/release_notes/whats_new_6.5.html
