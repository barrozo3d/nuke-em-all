"""
course_engine_loader — find the shared engine, or the vendored snapshot, and
SAY OUT LOUD WHICH ONE IS RUNNING.

⚠️ This file is the answer to open question 2 ("ship the vendored snapshot, or
fail loudly?"). It does both: shipping keeps a standalone `git clone <one skill>`
working, and the printed provenance line is what stops a stale snapshot from
being a SILENT fallback.

That distinction is the recurring bug in this project, not a hypothetical:
`_detect_hallucination` reading only the last 50 words, an empty Prefetch folder
reading as "no programs ran", a permission-denied Security log reading as "no
events", `frame_status: complete` referring to frames that exist on some other
machine. Every one is the same shape — MISSING EVIDENCE PRESENTED AS A CLEAN
RESULT. A vendored engine silently standing in for a newer shared one is that
shape again, so the run says which it got, every time.

Resolution order:
  1. `<skills-root>/_shared/course_engine`  — the shared repo (decision #2)
  2. `<skill>/vendor/course_engine`         — generated snapshot, never hand-edited
"""

import os, re, sys
from pathlib import Path

_VERSION_RE = re.compile(r'^__version__\s*=\s*["\']([^"\']+)["\']', re.M)


def _version_at(pkg_dir):
    init = pkg_dir / "__init__.py"
    if not init.exists():
        return None
    m = _VERSION_RE.search(init.read_text(encoding="utf-8", errors="replace"))
    return m.group(1) if m else "unknown"


def _parse(v):
    try:
        return tuple(int(x) for x in str(v).split("."))
    except ValueError:
        return ()


def load_course_engine(skill_dir, quiet=None):
    """Import and return the course_engine package, printing its provenance.

    Set INGEST_ENGINE_QUIET=1 to suppress the provenance line in batch runs —
    but note that suppressing it is exactly how a stale vendor copy goes
    unnoticed, so prefer leaving it on.
    """
    if quiet is None:
        quiet = os.getenv("INGEST_ENGINE_QUIET", "0").lower() in ("1", "true", "yes")
    skill_dir = Path(skill_dir)
    shared_pkg = skill_dir.parent / "_shared" / "course_engine"
    vendor_pkg = skill_dir / "vendor" / "course_engine"
    shared_v, vendor_v = _version_at(shared_pkg), _version_at(vendor_pkg)

    if shared_v is not None:
        root, source, version = shared_pkg.parent, "_shared/", shared_v
    elif vendor_v is not None:
        root, source, version = vendor_pkg.parent, "vendor/", vendor_v
    else:
        raise ImportError(
            "course_engine not found. Expected either "
            f"{shared_pkg} (clone https://github.com/barrozo3d/course-engine.git "
            f"into {skill_dir.parent / '_shared'}) or a vendored snapshot at {vendor_pkg}."
        )

    sys.path.insert(0, str(root))
    import course_engine  # noqa: E402

    if not quiet:
        print(f"[engine] course_engine {version} from {source}")
        # ⚠️ Only detectable on a device holding BOTH. A device with only the
        # skill cloned cannot know it is behind -- which is why the provenance
        # line above prints unconditionally rather than only on a mismatch.
        if source == "vendor/" and shared_v is not None:
            print("[engine] WARNING: running the vendored snapshot while _shared/ exists")
        if shared_v is not None and vendor_v is not None and _parse(vendor_v) < _parse(shared_v):
            print(f"[engine] NOTE: vendored snapshot ({vendor_v}) is older than "
                  f"_shared/ ({shared_v}) -- regenerate with _shared/sync_vendor.py")
    return course_engine
