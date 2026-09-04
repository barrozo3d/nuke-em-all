---
title: Customizing the UI
source: Article
url: https://learn.foundry.com/nuke/developers/latest/pythondevguide/custom_ui.html
author: learn.foundry.com
ingested: 2026-09-04
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
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
