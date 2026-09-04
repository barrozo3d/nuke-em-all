---
title: Installing Plug-ins
source: Article
url: https://learn.foundry.com/nuke/developers/latest/pythondevguide/installing_plugins.html
author: learn.foundry.com
ingested: 2026-09-04
app: "Nuke / NukeX / Nuke Studio"
version: "not specified (dev guide served at /latest/; the page's own plug-in-path examples are Nuke 6.2v4-era)"
tags: [python-scripting, pipeline, gizmo, nuke-startup, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/installing-plug-ins/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# Installing Plug-ins

**Source:** [Article](https://learn.foundry.com/nuke/developers/latest/pythondevguide/installing_plugins.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Installing Plug-ins  There are a few different ways to install plug-ins, gizmos, and Python scripts so NUKE can see them. The easiest way is to use your home directory’s ~/.nuke folder, which is created the first time NUKE launches. However, this is not feasible in a multi-user environment. In this case, a custom plug-in directory is preferable. You can set one up using the NUKE_PATH environment variable. Note It is not a good idea to place custom plug-ins in NUKE’s install directory, as there may be permission and security issues and the plug-ins will not be available across different versions of NUKE. Here are the details: Home Directory  On Nukepedia , you can watch a video tutorial about installing plug-ins in the home directory. As mentioned above, the ~/.nuke directory is created when NUKE launches (if it doesn’t already exist). The path to this directory is added to NUKE’s plug-in path. You can view the plug-in path as follows: nuke . pluginPath () # Result: [ /Users/frank/.nuke , /Library/Application Support/NUKE/6.2/plugins , /Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins/user , /Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins/icons , /Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins ] Everything in the listed directories can be accessed from within NUKE. Without custom UI code in place, you can use the Other All Plugins Update option to force load everything in those directories into the Other All Plugins menu. This approach is fine for quick debugging or testing, but is not an acceptable workflow solution. What you want to do once you have your custom gizmo or plug-in in the ~/.nuke directory, is to create a menu.py file, which is automatically run when NUKE launches in interactive mode. Then, create a custom menu item in that file for the new gizmo or plug-in: nuke . menu ( Nodes ) . addCommand ( Other/MyGizmo , lambda : nuke . createNode ( MyGizmo ) ) Here, the second MyGizmo is the file name of the custom plug-in or gizmo (for example, ~/.nuke/MyGizmo.gizmo ). A similar approach can be taken with Python scripts. Let’s say you have a file called ~/.nuke/myFunctions.py, which contains a function called doCoolStuff() . You can import the module in your menu.py , then assign the callable to a custom menu item: import myFunctions nuke . menu ( Nuke ) . addCommand ( My Cool Functions/do cool stuff , myFunctions . doCoolStuff ) To organize custom files better, you can create sub-directories for each type (for example, “gizmos”, “plugins”, “python”, and so on) and add them to NUKE’s plug-in path at start-up: nuke . pluginAddPath ( .gizmos ) nuke . pluginAddPath ( .python ) nuke . pluginAddPath ( .plugins ) The above code is best placed in a file called init.py , which is automatically read every time NUKE launches (both in interactive and command-line mode). You can use both absolute and relative paths. With the above relative paths saved into a file called ~/.nuke/init.py , after relaunching NUKE, you can run nuke.pluginPath() again to make sure the new directories are now read: nuke . pluginPath () # Result: [ /Users/frank/.nuke/.gizmos , /Users/frank/.nuke/.python , /Users/frank/.nuke/.plugins , /Users/frank/.nuke , /Library/Application Support/NUKE/6.2/plugins , /Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins/user , /Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins/icons , /Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins ] Note that nuke.pluginAddPath prefixes paths to the start of the plug-in path. If you want to append them to the end of the path instead, use nuke.pluginAppendPath . For details, see Evaluation Order . Custom Plug-in Repository  To use a custom plug-in directory that is shared across a network, you can either use the nuke.pluginAddPath function in each user’s ~/.nuke/init.py file or use the environment variable NUKE_PATH. Here is how to do that in a bash shell under Linux or Mac OS X: Then, in NUKE: nuke . pluginPath () # Result: [ /Users/frank/.nuke , /Volumes/Library/NukePlugins , /Library/Application Support/NUKE/6.2/plugins , /Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins/user , /Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins/icons , /Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins ] Note The ~/.nuke directory is always at the start of the plug-in path. This way, any default and facility settings can always be overwritten on a per-user basis. You can now create any sub-directories you may need for organizing your custom tools and use an init.py file to include them in the plug-in path: From the init.py file: nuke . pluginAddPath ( ./gizmos ) nuke . pluginAddPath ( ./python ) nuke . pluginAddPath ( ./plugins ) In NUKE: nuke . pluginPath () # Result: [ /Users/frank/.nuke , /Volumes/Library/NukePlugins/gizmos , /Volumes/Library/NukePlugins/python , /Volumes/Library/NukePlugins/plugins , /Volumes/Library/NukePlugins , /Library/Application Support/NUKE/6.2/plugins , /Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins/user , /Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins/icons , /Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins ] On that level, you can also create user directories where everyone can park their custom code that is only accessible to the author. Let’s say you add a sub-directory called Users for this purpose, which contains sub-directories for each user’s login name: You can now place the following code in your top level init.py file to check for the current user when NUKE starts up and only include the respective user directory if it exists: import os user = os . getenv ( USER ) userPath = os . path . join ( /Library/NukePlugins/Users , user ) if os . path . isdir ( userPath ): nuke . pluginAddPath ( userPath ) You can also source project-specific tools in the same way. In this example, we assume all show directories live in /projects and we have set an environment variable called SHOW, which tells us the current show’s name. We then look for the /nuke directory inside the current show directory and add that to the plug-in path: curShow = os . getenv ( SHOW ) showPath = os . path . join ( /projects , curShow , nuke ) if os . path . isdir ( showPath ): nuke . pluginAddPath ( showPath ) You can now place all the show-specific code in each show’s /nuke directory, and use menu.py and init.py to further define the structure. If you want to load all the tools for all the shows (it can be quite handy to quickly grab custom tools from another show when you’re in a pinch), you can use code like this: baseDir = /projects shows = os . listdir ( baseDir ) for s in shows : showPath = os . path . join ( baseDir , s , nuke ) if os . path . isdir ( showPath ): nuke . pluginAddPath ( showPath )



---

## Structured Notes

### Core Technique
Three escalating ways to make Nuke see a gizmo, plug-in or Python script — the `~/.nuke` home directory, sub-directories added with `nuke.pluginAddPath()` from `init.py`, and a shared network repository pointed at by `NUKE_PATH` — plus the `menu.py` entry that turns an installed file into something artists can actually click.

### Summary
Installing a Nuke plug-in is two separate problems: making the file *discoverable* on the plug-in path, and making it *reachable* from a menu. The page walks the discovery half from the single-user case (`~/.nuke`, created on first launch and always first on the plug-in path) up to a multi-user facility (a network directory exported through `NUKE_PATH`), and warns explicitly against the tempting wrong answer — dropping plug-ins into Nuke's own install directory, which brings permission problems and breaks on every version upgrade. It closes with two genuinely pipeline-shaped patterns: a per-user directory added only `if os.path.isdir()` finds it, and per-show tool directories resolved from a `SHOW` environment variable at start-up.

### Key Steps
1. **Single user:** drop the `.gizmo`, plug-in or `.py` file into **`~/.nuke`** — created automatically on first launch and always at the *start* of the plug-in path, so it overrides facility defaults.
2. Verify with **`nuke.pluginPath()`**; for quick debugging only, force everything into a menu with **Other ▸ All Plugins ▸ Update**. The page calls this "fine for quick debugging or testing, but not an acceptable workflow solution."
3. **Make it reachable:** add a command in `menu.py` — `nuke.menu("Nodes").addCommand("Other/MyGizmo", lambda: nuke.createNode("MyGizmo"))`, where the second `MyGizmo` is the *filename* (`~/.nuke/MyGizmo.gizmo`).
4. For a Python module `~/.nuke/myFunctions.py` holding `doCoolStuff()`: `import myFunctions` then `nuke.menu("Nuke").addCommand("My Cool Functions/do cool stuff", myFunctions.doCoolStuff)` — pass the callable, do not call it.
5. **Organise by type:** create `gizmos`, `python`, `plugins` sub-directories and register them from **`init.py`** with `nuke.pluginAddPath("./gizmos")` etc. Relative and absolute paths both work; `pluginAddPath` *prefixes*, `pluginAppendPath` appends.
6. **Multi-user:** point every artist at a shared network directory, either by calling `nuke.pluginAddPath()` in each user's `~/.nuke/init.py` or — better — by setting **`NUKE_PATH`** in the shell environment. `~/.nuke` stays first regardless, so per-user overrides keep working.
7. **Per-user sandbox inside a shared repo:** in the top-level `init.py`, read `os.getenv("USER")`, join it under a `Users` directory, and `nuke.pluginAddPath(userPath)` **only** `if os.path.isdir(userPath)`.
8. **Per-show tools:** read `os.getenv("SHOW")`, build `/projects/<show>/nuke`, and add it if it exists — or loop `os.listdir("/projects")` and add every show's `nuke` directory when artists need to borrow tools across shows.

### Nodes / Tools / Settings
- **`~/.nuke`** — per-user plug-in directory, created on first launch, always first on the plug-in path.
- **`NUKE_PATH`** — environment variable for a shared/network plug-in repository.
- **`nuke.pluginPath()`** / **`nuke.pluginAddPath()`** (prefix) / **`nuke.pluginAppendPath()`** (append).
- **`nuke.menu("Nodes").addCommand(path, cmd)`** — adds to the Nodes toolbar; **`nuke.menu("Nuke")`** — the application menu bar.
- **`nuke.createNode("<name>")`** — instantiates the gizmo/plug-in by filename.
- **Other ▸ All Plugins ▸ Update** — force-loads everything on the path; debugging aid only.
- `os.getenv("USER")`, `os.getenv("SHOW")`, `os.path.isdir()`, `os.path.join()`, `os.listdir()` — the guards that keep a facility `init.py` from failing on a machine where a directory is absent.
- ⚠️ **Do not install into Nuke's own application directory** — permission/security issues, and the plug-ins do not carry across Nuke versions.

### Difficulty
Intermediate

### Foundry App & Version
Nuke / NukeX / Nuke Studio. Version not specified — served from the `/latest/` dev-guide path while the printed `nuke.pluginPath()` results are Nuke 6.2v3/6.2 era. The API calls and `NUKE_PATH` behaviour are current.

### Tags
`python-scripting`, `pipeline`, `gizmo`, `nuke-startup`, `intermediate`

---

## Related Tutorials
- [Start-up Scripts](start-up-scripts.md) — the evaluation order that decides which of these directories wins.
- [Customizing the UI](customizing-the-ui.md) — the full menu/toolbar/hotkey API this page only samples.
- [Break up your "PERFECT CG" Renders with this FREE Plugin](break-up-your-perfect-cg-renders-with-this-free-plugin.md) — a real third-party plug-in to install by this route.

> **Note on code in the Raw Data.** The article fetcher strips quote characters out of inline code, so the captured page text reads `nuke.menu( Nodes ).addCommand( ... )`. Quotes are restored in the notes above; the identifiers, argument order and values are unchanged from the source page.
