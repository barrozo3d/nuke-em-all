# Nuke Python Scripting Reference

Grounded against Foundry Learn's Python Developer's Guide and Python API Reference (`learn.foundry.com/nuke/developers/`). Covers the `nuke` module basics needed for gizmos, callbacks, and pipeline tools; not exhaustive of the full API.

## Core object model
- `nuke.Node` — every node instance (native or Group/Gizmo). Key methods: `.knob(name)`, `.knobs()` (dict of all knobs), `.getNumKnobs()` / `.knob(i)` for positional access, `.setInput(index, node)` / `.input(index)`, `.name()` / `.setName()`, `.screenWidth()`/`.screenHeight()` for layout, `.forceValidate()` / `.forceEvaluate()`.
- Creating nodes: `nuke.createNode("Blur")` (adds to the graph interactively, connects to selection) vs. `nuke.nodes.Blur()` (creates without graph side-effects — preferred inside scripts/tools). Both return the `Node`.
- Selection: `nuke.selectedNode()`, `nuke.selectedNodes()`, `nuke.allNodes()` (optionally filtered by class or recursed into Groups).
- Knobs: `node.knob("size").setValue(20)`, `node["size"].value()` (bracket access is shorthand for `.knob()`), animation via `node["size"].setAnimated()` then `.setValueAt(value, frame)`.

## Callbacks
Registered in `menu.py` / `init.py` (see Setup below) via `nuke.addOnCreate`, `nuke.addOnScriptLoad`, `nuke.addKnobChanged`, `nuke.addOnDestroy`, etc. Common patterns:
- `knobChanged` callback on a Gizmo/Group — reacts live to a user changing a control, e.g. showing/hiding other knobs based on a dropdown (`nuke.thisKnob()`, `nuke.thisNode()` inside the callback).
- `onCreate` — runs when a node is created (interactively or via script) — used to set defaults, tag metadata, or auto-wire internal Group contents.
- `onScriptLoad` / `onScriptSave` — project-wide hooks, e.g. validating a script against a naming convention before save.

## `init.py` vs `menu.py`
- `init.py` — runs at Nuke startup *before* the GUI exists; used for non-UI setup: registering custom node classes/plugin paths (`nuke.pluginAddPath(...)`), Python path setup, defining callback functions (but not necessarily binding them to menus).
- `menu.py` — runs after the GUI initializes; used to add toolbar/menu entries (`nuke.menu("Nodes").addMenu(...)`, `nuke.menu("Nuke").addCommand(...)`), and to bind the callbacks defined in `init.py` (or here) via `nuke.addOnCreate(...)` etc.
- Both are auto-loaded from `~/.nuke/` (or any path added via `NUKE_PATH`) — the standard place to drop studio pipeline tools so they load in every session.

## Panels / UI
- `nuke.Panel` — simple modal dialogs (`addSingleLineInput`, `addButton`, `.show()`).
- PySide2/PySide6 (Nuke embeds Qt) for anything beyond a simple modal — custom docked panels are registered via `nuke.menu('Pane').addCommand(...)` returning a widget, then typically wrapped with `nukescripts.panels.registerWidgetAsPanel`.

## Gizmos vs. Groups vs. Python-created tools
- A **Group** is a live sub-graph, editable by double-clicking in the node graph.
- A **Gizmo** is a Group saved to a `.gizmo` file (essentially a serialized gizmo script) and distributed via the plugin path — the standard "shareable custom node" format; can optionally hide its internals from casual editing.
- Purely Python-driven tools (no saved node) are common for one-off pipeline actions (e.g. a "publish comp" menu command that walks `nuke.allNodes()`, validates Write node paths, and triggers a render) — these don't need a Group/Gizmo at all.

## Command-line / batch rendering
- `nuke -x script.nk` — execute (render) a script's Write nodes non-interactively.
- `nuke -t script.py` — run a Python script inside a full Nuke Python environment without the GUI (useful for pipeline automation, since Nuke-as-a-Python-module gives access to the same `nuke` API in headless batch jobs).

## Stereo / multi-view
Nuke's Python API and node graph are view-aware (`nuke.views()`, per-view knob expressions like `{L}`/`{R}`) — relevant for any stereo or multi-view pipeline automation, distinct from single-view compositing scripting.
