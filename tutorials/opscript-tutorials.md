---
title: OpScript Tutorials
source: Article
url: https://learn.foundry.com/katana/Content/ug/working_with_attributes/opscript_tutorials.html
author: learn.foundry.com
ingested: 2026-08-24
app: "Katana"
version: "9.0v3"
tags: [katana, scenegraph, nodegraph, cel, katana-9, advanced]
extraction_status: complete
frames_dir: tutorials/frames/opscript-tutorials/
frame_count: 0
frame_status: skipped
---

# OpScript Tutorials

**Source:** [Article](https://learn.foundry.com/katana/Content/ug/working_with_attributes/opscript_tutorials.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** OpScript Tutorials OpScript Tutorials Creating Scene Graph Locations Deleting Scene Graph Locations Copying Scene Graph Locations and Attributes Please note that the following examples are located in the Help Example Projects menu in Katana , or within the katana install directory at $KATANA_HOME/demos/katana_files/opscript_tutorial.katana . Creating Scene Graph Locations Using CreateChild() This example shows you how to create child locations using the OpScript node. By default, if you specify Interface.CreateChild( ‘childName’ ) inside your OpScript without specifying the opType parameter, your child location inherits the opType used by the parent. So, in this case, it recursively uses this opType, OpScriptLua, and creates an infinite number of child locations. Note: Please refer to OpScript for more information on any of the following functions, or for information on exposed functions for the OpScript. There are a few solutions to this: check if we match the CEL, create a hierarchy based on an if-else statement, or use a StaticSceneCreate op to create a hierarchy. Check If We Match the CEL A simple way to get around this is to use the following command: if Interface.AtRoot() then Interface.CreateChild("child_a") end In the OpScript node, set the CEL statement to /root/world by previously creating a /root/world location using LocationCreate. Also make sure that the applyWhere parameter is set to at locations matching CEL . Create a Hierarchy Based on if-else Statement We create a hierarchy by checking which location we are currently at and executing the commands associated to that if statement. When this script is run for the first time, it creates a child location at /root , which is /root/world . Then, when the OpScript is executed at the child location, it creates /root/world/geo . This continues until the last condition is met. In this way, we avoid infinite recursion. We’ve set the applyWhere parameter to at all locations too, so that we don’t need to worry about specifying /root . Use a StaticSceneCreate Op to Create a Hierarchy We can use the StaticSceneCreate op to create a hierarchy without the use of if-else statements using the OpArgsBuilder.StaticSceneCreate() function. You can input the following directly into an OpScript node, or refer to the example OpScript Tutorial file. Again, we’ve set the applyWhere parameter to be run at all locations . Deleting Scene Graph Locations There are three methods available to remove scene graph locations: deleteChild() , deleteChildren() and deleteSelf() . By allowing you to remove your own scene graph locations, you can re-implement your own Prune node, for instance. This tutorial looks at each of these methods, but please refer to the OpScript Tutorial Example Projects for context. You can comment or uncomment the relevant commands. Delete the Child by Name The OpScript node allows you to delete newly-created children and incoming child locations, like so: Interface.DeleteChild("child_a") Note that child_a is the immediate child of the matching CEL. For example, if your CEL statement looked like this: /root/world/geo/parent and the children that exist here are /root/world/geo/parent/child_a and /root/world/geo/parent/child_a/grandchild_a the DeleteChild() function cannot delete grandchild_a. Delete All Children Deleting all children under which the OpScript is being cooked at is straightforward. This also deletes all newly-created children and incoming ones: Interface.DeleteChildren() Delete Self You are also able to delete the current output location using Interface.DeleteSelf() , however, all calls to DeleteSelf() keep the location in its parent’s potential children list. So, it’s advisable to use DeleteChild() instead, if possible. Copying Scene Graph Locations and Attributes Since the attributes are being copied over along with the scene graph locations, we can use this to our advantage. As the OpScript node supports multiple inputs, you can effectively recreate a custom Merge or Switch node, again, increasing the potential of the OpScript node. Using the same function as above, look at how you can copy from one input to another. Please refer to the OpScript Tutorials example file for context. We have two LocationCreate nodes and an AttributeSet node corresponding to each LocationCreate node. The two node graph branches are then connected to separate input ports of the OpScript node. The CopyLocationToChild() function that we used in the previous example has two extra arguments that we haven’t explicitly specified; they are: the input index and the order of where you want to place your new hierarchy. if Interface.AtRoot() then Interface.CopyLocationToChild("target_child_a","/root/world/another_parent/another_child_a", 1, "child_a") -- Interface.CopyLocationToChild("target_child_a","/root/world/parent/child_a", 0, "child_a") end This script copies over the name attribute from the second input of the OpScript to the target_child_a location. The name changes depending on which line you comment/uncomment. Creating Scene Graph Locations Using CreateChild() This example shows you how to create child locations using the OpScript node. By default, if you specify Interface.CreateChild( ‘childName’ ) inside your OpScript without specifying the opType parameter, your child location inherits the opType used by the parent. So, in this case, it recursively uses this opType, OpScriptLua, and creates an infinite number of child locations. Note: Please refer to OpScript for more information on any of the following functions, or for information on exposed functions for the OpScript. There are a few solutions to this: check if we match the CEL, create a hierarchy based on an if-else statement, or use a StaticSceneCreate op to create a hierarchy. Check If We Match the CEL A simple way to get around this is to use the following command: if Interface.AtRoot() then Interface.CreateChild("child_a") end In the OpScript node, set the CEL statement to /root/world by previously creating a /root/world location using LocationCreate. Also make sure that the applyWhere parameter is set to at locations matching CEL . Create a Hierarchy Based on if-else Statement We create a hierarchy by checking which location we are currently at and executing the commands associated to that if statement. When this script is run for the first time, it creates a child location at /root , which is /root/world . Then, when the OpScript is executed at the child location, it creates /root/world/geo . This continues until the last condition is met. In this way, we avoid infinite recursion. We’ve set the applyWhere parameter to at all locations too, so that we don’t need to worry about specifying /root . path = Interface.getOutputLocationPath() if path == "/root" then Interface.CreateChild("world") elseif path == "/root/world" then Interface.CreateChild("parent") elseif path == "/root/world/parent" then Interface.CreateChild("child_a") elseif path == "/root/world/parent/child_a" then Interface.SetAttr("test", IntAttribute(123)) end Use a StaticSceneCreate Op to Create a Hierarchy We can use the StaticSceneCreate op to create a hierarchy without the use of if-else statements using the OpArgsBuilder.StaticSceneCreate() function. You can input the following directly into an OpScript node, or refer to the example OpScript Tutorial file. Again, we’ve set the applyWhere parameter to be run at all locations . sscb = OpArgsBuilders.StaticSceneCreate(true) sscb:createEmptyLocation("/root/world/parent/child_a", "group") --create a scenegraph location with a type sscb:setAttrAtLocation("/root/world/parent/child_a", "test_id", IntAttribute(123)) --set the attribute Interface.ExecOp("StaticSceneCreate", sscb:build()) --execute the Op Deleting Scene Graph Locations There are three methods available to remove scene graph locations: deleteChild() , deleteChildren() and deleteSelf() . By allowing you to remove your own scene graph locations, you can re-implement your own Prune node, for instance. This tutorial looks at each of these methods, but please refer to the OpScript Tutorial Example Projects for context. You can comment or uncomment the relevant commands. Delete the Child by Name The OpScript node allows you to delete newly-created children and incoming child locations, like so: Interface.DeleteChild("child_a") Note that child_a is the immediate child of the matching CEL. For example, if your CEL statement looked like this: /root/world/geo/parent and the children that exist here are /root/world/geo/parent/child_a and /root/world/geo/parent/child_a/grandchild_a the DeleteChild() function cannot delete grandchild_a. Delete All Children Deleting all children under which the OpScript is being cooked at is straightforward. This also deletes all newly-created children and incoming ones: Interface.DeleteChildren() Delete Self You are also able to delete the current output location using Interface.DeleteSelf() , however, all calls to DeleteSelf() keep the location in its parent’s potential children list. So, it’s advisable to use DeleteChild() instead, if possible. Copying Scene Graph Locations and Attributes Another useful feature of the OpScript node is the ability to copy scene graph locations. For instance, allowing you to re-implement the HierarchyCopy node, if you wish. You can achieve this using Interface.CopyLocationToChild() function. Please refer to the OpScript Tutorial Example Projects and use the following code in conjunction for understanding the process. Copying Scene Graph Hierarchies These tutorials have shown how you can copy hierarchies very easily using the CopyLocationToChild() function. Using the following piece of Lua code, we can copy the /root/world/geo/parent_a hierarchy to the locations matching the CEL statement provided, in this case, /root/world/geo . The result is another hierarchy at /geo with /root/world/geo/parent_b/child_a . The resultant hierarchy has all the attributes copied over too. if Interface.AtRoot() then Interface.CopyLocationToChild("parent_b", "/root/world/geo/parent_a") end Copying Attributes Across Different Inputs Since the attributes are being copied over along with the scene graph locations, we can use this to our advantage. As the OpScript node supports multiple inputs, you can effectively recreate a custom Merge or Switch node, again, increasing the potential of the OpScript node. Using the same function as above, look at how you can copy from one input to another. Please refer to the OpScript Tutorials example file for context. We have two LocationCreate nodes and an AttributeSet node corresponding to each LocationCreate node. The two node graph branches are then connected to separate input ports of the OpScript node. The CopyLocationToChild() function that we used in the previous example has two extra arguments that we haven’t explicitly specified; they are: the input index and the order of where you want to place your new hierarchy. if Interface.AtRoot() then Interface.CopyLocationToChild("target_child_a","/root/world/another_parent/another_child_a", 1, "child_a") -- Interface.CopyLocationToChild("target_child_a","/root/world/parent/child_a", 0, "child_a") end This script copies over the name attribute from the second input of the OpScript to the target_child_a location. The name changes depending on which line you comment/uncomment. Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
Creating, deleting and copying scene graph locations from an **OpScript** node using the Lua `Interface` API — and the recursion trap that makes `Interface.CreateChild()` generate infinite children unless the script is guarded by CEL matching, an `if`-`else` on the current location path, or a `StaticSceneCreate` Op.

### Summary
Katana's OpScript node runs Lua against each scene graph location it is cooked at, which makes it a general-purpose way to re-implement nodes like Prune, HierarchyCopy, Merge or Switch. The page works through three groups of operations — creating locations with `CreateChild()`, removing them with `DeleteChild()` / `DeleteChildren()` / `DeleteSelf()`, and copying locations *with their attributes* via `CopyLocationToChild()` — and is explicit about the failure mode that bites first: a bare `CreateChild()` inherits the parent's `opType` (`OpScriptLua`) and recurses forever. The matching example project ships with Katana at `$KATANA_HOME/demos/katana_files/opscript_tutorial.katana`.

### Key Steps
1. Open the example scene — **Help → Example Projects** in Katana, or `$KATANA_HOME/demos/katana_files/opscript_tutorial.katana` — and work through it alongside the node's `applyWhere` setting.
2. Understand the recursion trap first: `Interface.CreateChild('childName')` with no `opType` inherits the parent's `opType` (`OpScriptLua`), so the new child runs the same script and creates an infinite number of child locations.
3. **Guard by CEL** — wrap creation in `if Interface.AtRoot() then ... end`, create `/root/world` upstream with a **LocationCreate** node, point the OpScript's CEL statement at `/root/world`, and set `applyWhere` to *at locations matching CEL*.
4. **Or branch on the location path** — read `Interface.getOutputLocationPath()` and use `if`/`elseif` to build one level per cook, which terminates when the last condition stops matching; `applyWhere` can then be *at all locations*.
5. **Or build the hierarchy in one Op** — assemble it with `OpArgsBuilders.StaticSceneCreate(true)`, calling `createEmptyLocation()` and `setAttrAtLocation()`, then `Interface.ExecOp("StaticSceneCreate", sscb:build())`.
6. **Delete a named child** with `Interface.DeleteChild("child_a")` — it only reaches the *immediate* child of the matching CEL, so with a CEL of `/root/world/geo/parent` it cannot delete `.../child_a/grandchild_a`.
7. **Delete everything below** the cooked location with `Interface.DeleteChildren()`, which removes both newly-created and incoming children.
8. Avoid `Interface.DeleteSelf()` where possible — it deletes the current output location, but every call leaves the location in its parent's potential-children list; the page advises `DeleteChild()` instead.
9. **Copy a hierarchy with its attributes** using `Interface.CopyLocationToChild("parent_b", "/root/world/geo/parent_a")` inside an `AtRoot()` guard — this re-implements HierarchyCopy, and the copied hierarchy keeps all attributes.
10. **Copy across inputs** to build a custom Merge or Switch: OpScript accepts multiple inputs, and `CopyLocationToChild()` takes two further arguments — the input index and the ordering name — as in `Interface.CopyLocationToChild("target_child_a", "/root/world/another_parent/another_child_a", 1, "child_a")`, where index `1` reads the second input.

### Nodes / Tools / Settings
**Nodes:** OpScript (Lua, `opType` `OpScriptLua`), LocationCreate, AttributeSet, StaticSceneCreate (as an Op), plus the nodes these examples re-implement — Prune, HierarchyCopy, Merge, Switch.

**OpScript parameters:** `CEL` (the locations to match) and `applyWhere` — *at locations matching CEL* vs *at all locations*. The choice between them is what makes each example terminate or recurse.

**`Interface` functions used:** `Interface.CreateChild(name [, opType])` · `Interface.AtRoot()` · `Interface.getOutputLocationPath()` · `Interface.SetAttr(name, attr)` · `Interface.DeleteChild(name)` · `Interface.DeleteChildren()` · `Interface.DeleteSelf()` · `Interface.CopyLocationToChild(childName, sourcePath [, inputIndex, orderName])` · `Interface.ExecOp(opType, args)`.

**Builder:** `OpArgsBuilders.StaticSceneCreate(true)` with `:createEmptyLocation(path, "group")`, `:setAttrAtLocation(path, name, attr)` and `:build()`.

**Attribute types:** `IntAttribute(123)` in both the `SetAttr` and `setAttrAtLocation` examples.

**Verbatim examples from the page:**

```lua
-- guard against infinite recursion by matching the CEL
if Interface.AtRoot() then
    Interface.CreateChild("child_a")
end
```

```lua
-- build one level per cook, keyed off the current location
path = Interface.getOutputLocationPath()
if path == "/root" then
    Interface.CreateChild("world")
elseif path == "/root/world" then
    Interface.CreateChild("parent")
elseif path == "/root/world/parent" then
    Interface.CreateChild("child_a")
elseif path == "/root/world/parent/child_a" then
    Interface.SetAttr("test", IntAttribute(123))
end
```

```lua
-- build a hierarchy in a single Op instead of if/else
sscb = OpArgsBuilders.StaticSceneCreate(true)
sscb:createEmptyLocation("/root/world/parent/child_a", "group")   -- location with a type
sscb:setAttrAtLocation("/root/world/parent/child_a", "test_id", IntAttribute(123))
Interface.ExecOp("StaticSceneCreate", sscb:build())
```

```lua
-- copy a hierarchy, attributes included (re-implements HierarchyCopy)
if Interface.AtRoot() then
    Interface.CopyLocationToChild("parent_b", "/root/world/geo/parent_a")
end
```

```lua
-- copy from a chosen input: index 1 is the second input
if Interface.AtRoot() then
    Interface.CopyLocationToChild("target_child_a", "/root/world/another_parent/another_child_a", 1, "child_a")
    -- Interface.CopyLocationToChild("target_child_a", "/root/world/parent/child_a", 0, "child_a")
end
```

**Example project:** `$KATANA_HOME/demos/katana_files/opscript_tutorial.katana` (also under Help → Example Projects).

### Difficulty
Advanced

### Foundry App & Version
Katana 9.0v3 (current Katana documentation set; the OpScript `Interface` API shown is long-standing and not flagged as version-specific on the page)

### Tags
katana, scenegraph, nodegraph, cel, katana-9, advanced

---

## Related Tutorials
- [GafferThree](gafferthree.md) — shares `katana`, `scenegraph`-adjacent and `cel` ground, since GafferThree's light and shadow linking is expressed with the same CEL statements used here to scope an OpScript.
- [Setting up UsdPreviewSurface Materials](setting-up-usdpreviewsurface-materials.md) — shares `katana` + `nodegraph`; its `UsdPrimvarReader_float2` reads the `st` primvar off the geometry, the attribute-to-shader transfer an OpScript can author at the scene graph level.
- [LiveGroups and LiveShadingGroups](livegroups-and-liveshadinggroups.md) — shares `katana` + `nodegraph`; both are routes to reuse rather than rebuild — OpScript authors scene graph locations procedurally, while a LiveGroup packages a Group node's children for reuse across projects.
- [Creating Shading Networks](creating-shading-networks.md) — shares `katana` + `nodegraph`; NetworkMaterialCreate wires materials by hand in the node graph, where OpScript's `Interface` API creates and edits the same scene graph locations procedurally.
- [Using Native USD Workflows](using-native-usd-workflows.md) — shares `katana` + `scenegraph` + `nodegraph`; it positions USD's Pattern-Based Collections as *"similar to Katana's CEL"* — the same selection problem solved once per scene representation.
- [UsdPrimCreate](usdprimcreate.md) — shares `katana` + `scenegraph` + `nodegraph`; OpScript's `Interface` API creates and deletes scene graph locations procedurally on the Katana side, the same authoring job this node does declaratively on the USD side.

*Note: the library held zero Katana sources before 2026-08-24 (see `KNOWLEDGE_GAPS_TODO.md`) and now holds twelve, so the Katana cross-link set is still narrow.*
