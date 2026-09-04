---
title: Customizing the UI
source: Article
url: https://learn.foundry.com/nuke/developers/latest/pythondevguide/custom_ui.html
author: learn.foundry.com
ingested: 2026-09-04
app: "Nuke / NukeX / Nuke Studio (interactive sessions only)"
version: "not specified (dev guide served at /latest/; the page's own plug-in-path examples are Nuke 6.2v4-era)"
tags: [python-scripting, pipeline, hotkeys, nuke-startup, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/customizing-the-ui/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Customizing the UI

**Source:** [Article](https://learn.foundry.com/nuke/developers/latest/pythondevguide/custom_ui.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Customizing the UI  This chapter explains how to create your own hotkeys, menus, and menu items. This kind of code is typically placed in the menu.py file. Please refer to Installing Plug-ins for information on how to install custom files. The menus currently available in NUKE are: Nuke - the application menu on top of the interface. Windows - the Windows menu found in all content menus. Nodes - the toolbar (and the right-click menu in the Node Graph). Properties - right-click menus of properties panels. Animation - the pop-up menu on the Animation button of all properties panels, and the right-click menu of the Curve Editor. Viewer - the right-click menu of the Viewer. Node Graph - the right-click menu of the Node Graph. Axis - the menus on all Axis_Knobs. Creating a Custom Menu  To create a custom menu, use: m = nuke . menu ( Viewer ) myMenu = m . addMenu ( MyStuff ) You can assign an icon to the menu as well: m = nuke . menu ( Viewer ) myMenu = m . addMenu ( MyStuff , icon = ohu_icon.png ) Creating a Custom Toolbar  To create a custom toolbar, use: myToolbar = nuke . toolbar ( My nodes ) You can add custom items to the toolbar in the same way as to a menu (see below for details): myToolbar . addCommand ( My Gizmo , lambda : nuke . createNode ( NoOp ) ) If you don’t specify a toolbar menu for the item, the item is added as a button on the toolbar: Otherwise, the item is added as a menu (like in the default toolbar): myToolbar . addCommand ( My Other Tools/tool A , lambda : nuke . createNode ( NoOp ) ) myToolbar . addCommand ( My Other Tools/tool B , lambda : nuke . createNode ( NoOp ) ) To add an icon for the menu, create it explicitly before assigning menu items to it: myMenu = myToolbar . addMenu ( My Other Tools , icon = ohu_icon.png ) myMenu . addCommand ( tool A , lambda : nuke . createNode ( NoOp ) ) myMenu . addCommand ( tool B , lambda : nuke . createNode ( NoOp ) ) Creating a Custom Menu Item  To add a custom entry to any of the above menus, use menu.addCommand() : nuke . menu ( Nuke ) . addCommand ( MyMenu/my tool 1 , lambda : nuke . message ( yay, it works ) ) Note In the above example, we create a menu called MyMenu menu on the fly. Instead of using lambda to create an anonymous function that isn’t executed until the menu item is evoked, you could also wrap the desired command into a string: nuke . menu ( Nuke ) . addCommand ( MyMenu/my tool 2 , nuke.message( yay, it works too ) ) You can also assign an icon to the menu item from NUKE’s plug-in path: nuke . menu ( Nuke ) . addCommand ( MyMenu/my tool 2 , nuke.message( yay, it works too ) , icon = ohu_icon.png ) To set the position of the item in the menu, use the index argument: nuke . menu ( Nuke ) . addCommand ( MyMenu/my tool 1.5 , nuke.message( yay, it works too ) , index = 1 ) Find the menu by name (we didn’t assign it to a variable at creation time), and add a separator before adding another menu item: m = nuke . menu ( Nuke ) . findItem ( MyMenu ) m . addSeparator () nuke . menu ( Nuke ) . addCommand ( MyMenu/my tool 3 , nuke.message( yay, it works too ) ) To find an existing menu item and run its function call, use: m = nuke . menu ( Nuke ) . findItem ( Edit/Node/Filename/Show ) m . invoke () To deactivate a menu item, use: m = nuke . menu ( Nuke ) . findItem ( Render/Proxy Mode ) m . setEnabled ( False ) Note If you deactivate a menu item, the hotkey assigned to it still continues to work. Assigning a Hotkey  To assign a hotkey to an existing menu item, you effectively replace the whole menu item. Let’s assign a hotkey to the Axis2 node. This node lives in the Nodes menu (that is, the toolbar), inside the 3D sub-menu. Its menu item is called Axis . nuke . menu ( Nodes ) . addCommand ( 3D/Axis , lambda : nuke . createNode ( Axis2 ), a ) Pressing a on the keyboard now creates an Axis node. You can also use modifier keys when assigning a hotkey. To use Ctrl (or cmd on Mac OS X) as the modifier, use: ctrl+ followed by the key, or ^ followed by the key. For example: nuke . menu ( Nodes ) . addCommand ( 3D/Axis , nuke.createNode( Axis2 ) , ctrl+a ) nuke . menu ( Nodes ) . addCommand ( 3D/Axis , nuke.createNode( Axis2 ) , ^a ) To use alt as the modifier, use: alt+ followed by the key, or # followed by the key. For example: nuke . menu ( Nodes ) . addCommand ( 3D/Axis , nuke.createNode( Axis2 ) , alt+a ) nuke . menu ( Nodes ) . addCommand ( 3D/Axis , nuke.createNode( Axis2 ) , #a ) To use shift as the modifier, use: shift+ followed by the key, or + followed by the key. For example: nuke . menu ( Nodes ) . addCommand ( 3D/Axis , nuke.createNode( Axis2 ) , shift+a ) nuke . menu ( Nodes ) . addCommand ( 3D/Axis , nuke.createNode( Axis2 ) , +a ) Defining Knob Defaults  To change the default values for knobs, use nuke.knobDefault() : nuke . knobDefault ( Blur.size , 77 ) The above line sets the size control of any subsequently created Blur nodes to 77 by default. When skipping the node class, the new default value is applied to all controls of the given name: nuke . knobDefault ( channels , rgba ) The above sets all channels controls to rgba on node creation.



---

## Structured Notes

### Core Technique
Building Nuke's interface from `menu.py` — `nuke.menu()` to reach one of the eight named menus, `nuke.toolbar()` for a new toolbar, `addCommand()` to place an item, and a third `addCommand()` argument to bind its hotkey.

### Summary
This page is the menu/toolbar/hotkey API that `menu.py` exists to hold. It names the eight addressable menus (**Nuke**, **Windows**, **Nodes**, **Properties**, **Animation**, **Viewer**, **Node Graph**, **Axis**), then covers creating menus and toolbars, adding items with icons and explicit positions, finding and invoking or disabling existing items, and assigning hotkeys with `ctrl+`/`^`, `alt+`/`#`, `shift+`/`+` modifiers. Two details are easy to miss and expensive to rediscover: assigning a hotkey to an existing command means **replacing the whole menu item**, and disabling an item with `setEnabled(False)` **does not disable its hotkey**, which keeps firing. The page ends with `nuke.knobDefault()`, the one piece here that belongs in `init.py` rather than `menu.py`.

### Key Steps
1. Address a menu with **`nuke.menu("<name>")`** — `Nuke` (app menu bar), `Windows`, `Nodes` (the toolbar *and* the Node Graph right-click), `Properties`, `Animation`, `Viewer`, `Node Graph`, `Axis`.
2. **Create a custom menu:** `m = nuke.menu("Viewer")` then `myMenu = m.addMenu("MyStuff")`, optionally `addMenu("MyStuff", icon="ohu_icon.png")` — the icon is resolved from the plug-in path.
3. **Create a custom toolbar:** `myToolbar = nuke.toolbar("My nodes")`. An item added with no sub-menu in its path becomes a **button**; one added as `"My Other Tools/tool A"` becomes a **menu**.
4. To give a toolbar sub-menu an icon, create it explicitly first — `myMenu = myToolbar.addMenu("My Other Tools", icon="ohu_icon.png")` — then add commands to `myMenu`.
5. **Add an item:** `nuke.menu("Nuke").addCommand("MyMenu/my tool 1", lambda: nuke.message("yay, it works"))`. Intermediate menus named in the path are created on the fly. The command may be a `lambda`/callable or a **string** of Python evaluated at invoke time.
6. Control placement and appearance with **`icon=`** and **`index=`** (`index=1` inserts at position 1), and separate groups with **`m.addSeparator()`** after locating the menu via `findItem`.
7. **Find, run or disable an existing item:** `m = nuke.menu("Nuke").findItem("Edit/Node/Filename/Show")` then `m.invoke()`; or `nuke.menu("Nuke").findItem("Render/Proxy Mode").setEnabled(False)`. ⚠️ The hotkey of a disabled item **still works**.
8. **Assign a hotkey by replacing the item:** `nuke.menu("Nodes").addCommand("3D/Axis", lambda: nuke.createNode("Axis2"), "a")` re-registers the existing *3D ▸ Axis* item with `a` bound. Modifiers: `ctrl+a` or `^a`, `alt+a` or `#a`, `shift+a` or `+a`.
9. **Change knob defaults** with `nuke.knobDefault("Blur.size", "77")` — per class, or `nuke.knobDefault("channels", "rgba")` with the class omitted to hit every knob of that name on creation. Put this in `init.py` so command-line renders get it too.

### Nodes / Tools / Settings
- **The eight menus:** `Nuke`, `Windows`, `Nodes`, `Properties`, `Animation`, `Viewer`, `Node Graph`, `Axis`.
- **`nuke.menu(name)`**, **`nuke.toolbar(name)`**, **`.addMenu(name, icon=)`**, **`.addCommand(path, cmd, hotkey, icon=, index=)`**, **`.addSeparator()`**, **`.findItem(path)`**, **`.invoke()`**, **`.setEnabled(bool)`**.
- **`nuke.knobDefault("<Class>.<knob>", "<value>")`** — e.g. `Blur.size` → `77`; class omitted applies to all knobs of that name (`channels` → `rgba`).
- **Hotkey modifier syntax:** `ctrl+` / `^`, `alt+` / `#`, `shift+` / `+`.
- **`nuke.message()`**, **`nuke.createNode()`** — used as the example payloads.

### Difficulty
Intermediate

### Foundry App & Version
Nuke / NukeX / Nuke Studio, interactive sessions only — none of this loads in a command-line session, which is precisely why it belongs in `menu.py`. Version not specified (dev guide `/latest/` path).

### Tags
`python-scripting`, `pipeline`, `hotkeys`, `nuke-startup`, `intermediate`

---

## Related Tutorials
- [Start-up Scripts](start-up-scripts.md) — why this code goes in `menu.py` and never in `init.py`.
- [Installing Plug-ins](installing-plug-ins.md) — putting the gizmo on the path that these menu items then instantiate.

> **Note on code in the Raw Data.** The article fetcher strips quote characters out of inline code, so the captured page text reads `nuke.menu( Nodes ).addCommand( ... )`. Quotes are restored in the notes above; the identifiers, argument order and values are unchanged from the source page.
