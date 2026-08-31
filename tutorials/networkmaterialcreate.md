---
title: NetworkMaterialCreate
source: Article
url: https://learn.foundry.com/katana/Content/rg/3d_nodes/networkmaterialcreate.html
author: learn.foundry.com
ingested: 2026-08-31
app: Katana
version: 9.0v3
tags: [katana, lookdev, nodegraph, katana-9, advanced]
extraction_status: complete
frames_dir: tutorials/frames/networkmaterialcreate/
frame_count: 0
frame_status: skipped
---

# NetworkMaterialCreate

**Source:** [Article](https://learn.foundry.com/katana/Content/rg/3d_nodes/networkmaterialcreate.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** NetworkMaterialCreate The NetworkMaterialCreate node has been designed to contain your material network. The node features a left-to-right workflow and a new shading node design, which enables you to work more efficiently, making building and editing materials as quick and simple as possible. It holds the function of one or more NetworkMaterial nodes as well as the NetworkMaterialInterfaceControls node. Control (UI) Default Value Function rootLocation /root/materials Defines the scene graph location where the material locations are created. The parameter options are available in either the scene graph widget or drop-down menu to the right of the parameter. For more information, refer to the Scene Graph Location Widget Type . Add NetworkMaterial / Add Namespace N/A Click to add a new NetworkMaterial location or Namespace . Add NetworkMaterial - Add a new NetworkMaterial location, accessible from within this NetworkMaterialCreate node. Added a new NetworkMaterial called NetworkMaterial1 Add Namespace - Add a new namespace to the Scene Graph under which NetworkMaterial locations can be grouped. Added a new Namespace called namespace Note: To learn more about multi- NetworkMaterial workflows in a NetworkMaterialCreate node, see Multiple NetworkMaterials with NetworkMaterialCreate . Material Scenegraph N/A Add, remove and organize NetworkMaterials and Namespaces . Name - To change the name of a NetworkMaterial or Namespace , you can double-click, or select the NetworkMaterial or Namespace and press Enter on the keyboard. You can then type a new name. Renderers - View the number of renderers connected to each NetworkMaterial . Terminals - View the number of terminals connected to each NetworkMaterial . Interactive - When checked, you can drag objects in the Viewer and Katana retains the information from the Viewer . Color - Set the color of a NetworkMaterial which is then applied to the terminal sidebar within the NetworkMaterialCreate node. Use the middle-mouse button to click and drag NetworkMaterials and Namespaces to organize them. Middle-mouse drag NetworkMaterial1 to place it under the namespace Note: You can place NetworkMaterials and Namespaces underneath other Namespaces but not underneath other NetworkMaterials . Node Parameters Control (UI) Default Value Function parameters N/A Promoted parameters within the NetworkMaterialCreate node appear here. This section remains empty if no parameters have been promoted. Note: For more information on how to promote parameters, see Node Parameters and Interface Controls documentation. Interface Controls Control (UI) Default Value Function Add Node button N/A Click to add a new Interface Control and open its parameters. Filter N/A Filter the list of Interface Controls by name or type. Type in the text field to start filtering. A list of matching controls are displayed. Click the Select All Matching button to display the parameters for all matching Interface Controls. Disable Parameter Display Disabled Toggles the display of the parameters. Fit to Width Disabled Adjusts the width of the Interface Control list so the full length of the control names are visible. Fit to Height Disabled Adjusts the height of the Interface Control list so all controls are visible. Note: The following parameters are only visible once an Interface Control has been created and is selected. state visibility The state of the parameter or page for the control to affect. visibility - Depending on the condition, displays or hides the parameter or page specified in the targetName parameter. lock - Depending on the condition, locks or unlocks the parameter or page specified in the targetName parameter, making any edits impossible if locked. targetType parameter Select whether to apply the condition on either: parameter - The operation affects a single parameter. page - The operation affects a page containing one or more parameters. targetName N/A Specifies the name of the chosen parameter or page. Note: The name must be identical to the one displayed in the NetworkMaterial node's Material Interface. definitionStyle operator tree Selects how to set up the condition: operator tree - Allows you to set up conditions using an operator tree. conditional state expression - Allows you to set up conditions using one or several expressions. When definitionStyle: operator tree operators op and Select which expression operator to use in the operator tree: and - The resulting expression is satisfied only if all of the child expressions are satisfied. or - The resulting expression is satisfied if at least one of the child expressions is satisfied. ops Add N/A Select an op: contains - Evaluates if the condition is true by testing if the parameter or page values contain the values set in the expression. doesNotContain - Evaluates if the condition is true by testing if the parameter or page values do not contain the values set in the expression. endsWith - Evaluates if the condition is true by testing if the parameter or page values end with the values set in the expression. equalTo - Evaluates if the condition is true by testing if the parameter or page values are equal to the values set in the expression. greaterThan - Evaluates if the condition is true by testing if the parameter or page values are greater than the values set in the expression. greaterThanOrEqualTo - Evaluates if the condition is true by testing if the parameter or page values are greater than or equal to the values set in the expression. in - Evaluates if the condition is true by testing if the parameter or page values are in the values (separated by a pipe with no spaces) set in the expression. lessThan - Evaluates if the condition is true by testing if the parameter or page values are less than the values set in the expression. lessThanOrEqualTo - Evaluates if the condition is true by testing if the parameter or page values are less than or equal to the values set in the expression. notEqualTo - Evaluates if the condition is true by testing if the parameter or page values are not equal to the values set in the expression. notIn - Evaluates if the condition is true by testing if the parameter or page values are not in the values (separated by a pipe with no spaces) set in the expression. numChildrenEqualTo - Evaluates if the condition is true by testing if the number of children in the target group parameter is equal to the number of children specified in the parameter or page. numChildrenGreaterThanOrEqualTo - Evaluates if the condition is true by testing if the number of children in the target group parameter is greater than or equal to the number of children specified in the parameter or page. regex - Evaluates if the condition is true by testing if the parameter or page values match the values set in the regular expression. and - Specifies if you want to compare the parameter or page values to another set of values. It uses all the expressions to evaluate the condition. or - Specifies if you want to compare the parameter or page values to another set of values. It uses only one of the expressions to evaluate the condition. Note: The following parameters are only visible once an operator has been selected from the Add menu. op N/A The chosen op from the Add menu. path N/A Specifies the path of the parameter or page to evaluate. value N/A Specifies the values to compare the parameter or page values with, in order to evaluate if the condition is true. Material Interface Control (UI) Default Value Function Name N/A A list displaying all promoted parameters, organized in the same way as they were grouped when promoted. Source N/A The path to each different parameter. Note: For more information on the uses of the Material Interface, see Node Parameters and Interface Controls documentation. Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
The parameter reference for **NetworkMaterialCreate** — where the NetworkMaterial locations land in the scene graph, how several of them are organised under Namespaces, and how promoted parameters are exposed and conditionally shown or locked through **Interface Controls**.

### Summary
NetworkMaterialCreate contains a material network and absorbs the function of one or more **NetworkMaterial** nodes plus the **NetworkMaterialInterfaceControls** node. Its parameters divide into four areas: `rootLocation` and the Material Scenegraph, which decide where materials are created and how multiple NetworkMaterials are grouped under Namespaces; Node Parameters, listing whatever has been promoted; **Interface Controls**, a rule system that shows/hides or locks a promoted parameter or page based on a condition; and the Material Interface, which lists every promoted parameter against its source path. The Interface Controls half is the substantial part — conditions are built either as an operator tree or as conditional state expressions, with sixteen comparison ops.

### Key Steps
1. Set **`rootLocation`** (default `/root/materials`) — the scene graph location where the material locations are created. Pick it from the scene graph widget or the drop-down beside the parameter.
2. Use **Add NetworkMaterial** to add a new NetworkMaterial location accessible inside this node, or **Add Namespace** to create a Scene Graph group that NetworkMaterial locations can sit under.
3. Organise them in the **Material Scenegraph**: rename by double-clicking (or select and press `Enter`), and **middle-mouse drag** to move items. NetworkMaterials and Namespaces can go under other Namespaces, **but never under another NetworkMaterial**.
4. Read the Material Scenegraph columns — **Renderers** and **Terminals** show how many of each are connected per NetworkMaterial, **Interactive** keeps Viewer-drag information, and **Color** sets the colour that NetworkMaterial takes in the terminal sidebar inside the node.
5. Promote the parameters you want exposed; they appear under **Node Parameters → `parameters`**, which stays empty until something is promoted.
6. Add an **Interface Control** with the *Add Node* button, then set `state` (`visibility` or `lock`), `targetType` (`parameter` or `page`) and **`targetName` — which must match the name shown in the NetworkMaterial node's Material Interface exactly**.
7. Build the condition: choose `definitionStyle` — `operator tree` or `conditional state expression`. For an operator tree, set the `operators op` (`and` = all children must be satisfied, `or` = at least one) and add ops.
8. Add comparison ops from the **Add** menu, then fill in `path` (the parameter or page to evaluate) and `value` (what to compare against).
9. Manage a long control list with **Filter** (by name or type, with *Select All Matching*), **Disable Parameter Display**, **Fit to Width** and **Fit to Height**.
10. Verify against the **Material Interface** tab, which lists every promoted parameter by **Name** in its promoted grouping alongside the **Source** path it came from.

### Nodes / Tools / Settings
**Node:** `NetworkMaterialCreate` — designed to contain a material network, with a left-to-right workflow and the newer shading-node design. **It holds the function of one or more `NetworkMaterial` nodes as well as the `NetworkMaterialInterfaceControls` node.**

**Top level:**

| Control | Default | Function |
|---|---|---|
| `rootLocation` | `/root/materials` | Scene graph location where the material locations are created (Scene Graph Location Widget Type). |
| `Add NetworkMaterial` / `Add Namespace` | N/A | Add a NetworkMaterial location accessible from inside this node, or a Namespace to group them under in the Scene Graph. |
| `Material Scenegraph` | N/A | Add, remove and organise NetworkMaterials and Namespaces. |

**Material Scenegraph columns:** `Name` (double-click, or select + `Enter`, to rename) · `Renderers` (count connected to each NetworkMaterial) · `Terminals` (count connected) · `Interactive` (when checked, objects can be dragged in the Viewer and Katana retains the Viewer's information) · `Color` (sets the NetworkMaterial's colour in the terminal sidebar inside the node).
⚠️ **Middle-mouse drag** reorganises them, and **NetworkMaterials and Namespaces may be placed under other Namespaces but never under another NetworkMaterial.**

**Node Parameters:** `parameters` — promoted parameters appear here; the section stays **empty if nothing has been promoted**.

**Interface Controls** — the rule system that drives a parameter's visibility or lock state:
- `Add Node` button — add a new Interface Control and open its parameters.
- `Filter` — filter the control list by name or type; **Select All Matching** displays the parameters for every match.
- `Disable Parameter Display` (Disabled) · `Fit to Width` (Disabled) · `Fit to Height` (Disabled).
- The following appear **only once a control exists and is selected**:
  - `state` = **`visibility`** (show/hide the target) or **`lock`** (lock/unlock it, making edits impossible while locked).
  - `targetType` = `parameter` (a single parameter) or `page` (a page containing one or more).
  - `targetName` — ⚠️ **must be identical to the name shown in the NetworkMaterial node's Material Interface.**
  - `definitionStyle` = `operator tree` or `conditional state expression`.
- With `definitionStyle: operator tree`: `operators op` = `and` (satisfied only if **all** child expressions are) or `or` (satisfied if **at least one** is); then `ops Add` to choose a comparison.

**The sixteen comparison ops:** `contains` · `doesNotContain` · `endsWith` · `equalTo` · `notEqualTo` · `greaterThan` · `greaterThanOrEqualTo` · `lessThan` · `lessThanOrEqualTo` · `in` and `notIn` (**values separated by a pipe with no spaces**) · `numChildrenEqualTo` and `numChildrenGreaterThanOrEqualTo` (test the child count of the target group parameter) · `regex` · plus `and` / `or` to compare against a further set of values, using all expressions or just one.
Once an op is picked, three more parameters appear: `op` (the chosen op), `path` (the parameter or page to evaluate) and `value` (what to compare against).

**Material Interface:** `Name` — every promoted parameter, organised as it was grouped when promoted; `Source` — the path to each parameter.

**Referenced docs (not ingested):** *Node Parameters and Interface Controls* (how promotion works, and the wider uses of the Material Interface), *Multiple NetworkMaterials with NetworkMaterialCreate*, and the *Scene Graph Location Widget Type* in *Common Parameter Widgets*.

### Difficulty
Advanced

### Foundry App & Version
Katana 9.0v3 (page served from the current Katana 9.0v3 documentation set)

### Tags
katana, lookdev, nodegraph, katana-9, advanced

---

## Scope note — the forward reference this closes

`creating-shading-networks.md` defers to this page **twice** — once for the node's
parameters in general and once specifically for changing the NetworkMaterial's
scene graph location. That location is **`rootLocation`, default `/root/materials`**,
documented here. Before this ingest, both of those pointers led out of the library.

Still not ingested and recorded in `KNOWLEDGE_GAPS_TODO.md`: *Node Parameters and
Interface Controls* — this page defers to it for **how** a parameter is promoted in
the first place, which is the step before every Interface Control described here —
and *Multiple NetworkMaterials with NetworkMaterialCreate*.

---

## Related Tutorials
- [Creating Shading Networks](creating-shading-networks.md) — shares `katana` + `lookdev` + `nodegraph`; **the workflow half of the same node.** That page builds the network inside NetworkMaterialCreate and defers to this one twice for the parameters; read it first, then this for `rootLocation`, Namespaces and Interface Controls.
- [Setting up UsdPreviewSurface Materials](setting-up-usdpreviewsurface-materials.md) — shares `katana` + `lookdev` + `nodegraph`; the UsdPreviewSurface network built there lives inside a NetworkMaterialCreate, so `rootLocation` is what decides where its `usdSurface`-terminated material lands in the scene graph.
- [GafferThree](gafferthree.md) — shares `katana` + `lookdev` + `katana-9`; GafferThree's Template Materials expose a controlled set of light-material parameters from one interface, the same problem the Material Interface and Interface Controls solve for geometry materials.
- [RenderOutputDefine](renderoutputdefine.md) — shares `katana` + `katana-9`; the `Ci` (final shader colour) pass it writes is the rendered output of the material this node defines.
- [Using Native USD Workflows](using-native-usd-workflows.md) — shares `katana` + `nodegraph` + `katana-9`; materials on the native USD path go through `UsdMaterial` rather than this node — the two parallel material-authoring routes.
