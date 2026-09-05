---
title: Building Materials Using NetworkMaterialCreate
source: Article
url: https://learn.foundry.com/katana/Content/ug/adding_assigning_materials/using_networkmaterialcreate.html
author: learn.foundry.com
ingested: 2026-09-04
app: "Katana"
version: "9.0 (learn.foundry.com/katana current docs at ingest; release notes whats_new_9.0)"
tags: [katana, lookdev, nodegraph, katana-9, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/building-materials-using-networkmaterialcreate/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Building Materials Using NetworkMaterialCreate

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/adding_assigning_materials/using_networkmaterialcreate.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Building Materials Using NetworkMaterialCreate The NetworkMaterialCreate node is specifically designed for building materials. It is similar to a Group node as it acts like a container for a selection of your node graph, however it exclusively stores your material network. Note: To learn about the NetworkMaterialCreate node parameters, see NetworkMaterialCreate . One aim of the NetworkMaterialCreate node is to minimize the amount of separate nodes the user needs to create when working with materials. Because of this, it incorporates a NetworkMaterial and other nodes, all conveniently within the NetworkMaterialCreate node. The node features a left-to-right workflow and a new shading node design, which enables you to work more efficiently, making building and editing materials as quick and simple as possible. NetworkMaterialCreate nodes support multiple NetworkMaterial locations to further streamline your workflow. This new network material workflow also introduces the ShadingGroup node which allows you to section off pieces of your shading network within a NetworkMaterialCreate node. This layout results in multiple levels of networks which allows full control over the accessibility of certain shading nodes and parameters. Example node graph showing the NetworkMaterialCreate workflow layout Creating Shading Networks Learn how to use the NetworkMaterialCreate node to build shading node networks. Adding Multiple NetworkMaterials Use the NetworkMaterialCreate node to create and organise multiple NetworkMaterials. Using the ShadingGroup Node Learn to use the ShadingGroup node to keep your shading node networks organized. The Node Parameters and Interface Controls Use the Node Parameters and Interface controls to customize shading node parameters from outside the NetworkMaterialCreate node. The NetworkMaterialEdit Node Edit NetworkMaterials that have been created using NetworkMaterialEdit nodes. NetworkMaterialCreate Compatibility The new workflow of using a NetworkMaterialCreate node to build a material is both forward and backward compatible. This means that your shading node networks from previous Katana versions can be copy-and-pasted into a NetworkMaterialCreate node and the shading nodes will appear in the updated node design. The network will be connected up correctly and will give you the same result as before. In the same way, the shading nodes from your new network within the NetworkMaterialCreate can be copy-and-pasted to previous versions of Katana as well as copied to the root of your node graph. Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
**NetworkMaterialCreate** is a container node — Group-like, but exclusively for a material network — that folds NetworkMaterial and its supporting nodes into one node with a left-to-right shading-node layout.

### Summary
This is the hub page for the modern material workflow, and its value is as a map: it states what NetworkMaterialCreate *is* (a container that minimises how many separate nodes you must create, holding a NetworkMaterial and other nodes inside itself), introduces the **ShadingGroup** node for sectioning a network into sub-levels, notes that a single NetworkMaterialCreate **supports multiple NetworkMaterial locations**, and then names the five child topics that make up the rest of the workflow — creating shading networks, adding multiple NetworkMaterials, using ShadingGroup, the **Node Parameters and Interface Controls**, and NetworkMaterialEdit. The compatibility statement is the practically important one: the workflow is **forward and backward compatible**. Shading networks from previous Katana versions can be copy-pasted into a NetworkMaterialCreate and will appear in the updated node design, correctly connected and giving the same result; and nodes from a new network can be copy-pasted back out to previous versions or to the root of the node graph.

### Key Steps
1. Treat **NetworkMaterialCreate** as the material's container — similar to a Group node, but storing only the material network.
2. Work **left to right** in the new shading-node design, with exposed ports on the nodes.
3. Use **ShadingGroup** nodes inside it to section off parts of the network, producing multiple levels and letting you control which shading nodes and parameters remain accessible.
4. Create **multiple NetworkMaterial locations** in a single NetworkMaterialCreate rather than one node per material.
5. Promote the parameters artists actually need to the outside via **Node Parameters and Interface Controls**.
6. Edit an existing network material downstream with **NetworkMaterialEdit**.
7. **Migrate freely:** paste an old-workflow shading network into a NetworkMaterialCreate — it redraws in the new design, connects correctly and renders the same; paste new-network shading nodes back out to older versions or to the node graph root.

### Nodes / Tools / Settings
- **NetworkMaterialCreate** — container for a material network; incorporates **NetworkMaterial** and supporting nodes.
- **ShadingGroup** — sections a network into sub-levels (only creatable inside NetworkMaterialCreate).
- **NetworkMaterialEdit** — downstream editing of an existing network material.
- **Material Interface** — where promoted parameters surface.
- Child topics: Creating Shading Networks; Adding Multiple NetworkMaterials; Using the ShadingGroup Node; The Node Parameters and Interface Controls; The NetworkMaterialEdit Node.
- Compatibility: forward **and** backward, by copy-and-paste, in both directions.

### Difficulty
Intermediate

### Foundry App & Version
Katana 9.0; the NetworkMaterialCreate workflow dates from Katana 3.2.

### Tags
`katana`, `lookdev`, `nodegraph`, `katana-9`, `intermediate`

---

## Related Tutorials
- [Creating Shading Networks](creating-shading-networks.md) — the node-building detail this page points to.
- [Node Parameters and Interface Controls](node-parameters-and-interface-controls.md) — promoting parameters out of the container.
- [Organizing Shading Networks with ShadingGroup Nodes](organizing-shading-networks-with-shadinggroup-nodes.md)
- [Editing Materials With The NetworkMaterialEdit Node](editing-materials-with-the-networkmaterialedit-node.md)
- [Material Basics](material-basics.md) — the legacy workflow this supersedes.

---

> **Provenance.** `learn.foundry.com/katana` (MadCap Flare). Paths in this doc set
> are not guessable and `Data/Tocs/*` 404s, so this page was reached by crawling
> from `Content/learn_katana.html` → `user_guide.html`, or from a sibling page's
> own links. Reference-guide and user-guide pages carry clean `<title>`s and need
> no `--title` override, unlike `learn.foundry.com/nuke/developers/**`.
