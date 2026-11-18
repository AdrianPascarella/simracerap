#!/usr/bin/env python3
"""Two checks of what the context files cost and whether they still tell the truth, for close_check.py.

  * startup read: what every session reads before doing anything (STATE.md, USER_ACTIONS.md, the
    last LOG entry, the active PLAN phase), measured in UTF-8 bytes. A line cap alone lets a handoff
    of 120 very long lines weigh four times another; bytes are what the session pays for. Over a
    budget it warns; only STATE.md over twice its budget fails, like the line cap.
  * cited paths: the repository paths ARCHITECTURE.md (whole) and DECISIONS.md (the "Touches:" line
    of the decisions still in force) cite in backticks, checked against one `git ls-files` listing.
    A map that names files which were renamed or removed misleads every session that trusts it.

Lives next to close_check.py and is copied to projects with it (like open_work.py); close_check.py
warns that these checks did not run when this file is missing. Stdlib only. Python 3.8+.
"""

from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path
from typing import Callable, Iterable

# Byte budgets (UTF-8) of what a session reads at start; close_check.py exposes them as flags.
STATE_BYTES = 12_000
LOG_BYTES = 6_000
PLAN_BYTES = 12_000
ACTIONS_BYTES = 8_000
HARD_FACTOR = 2  # STATE.md over HARD_FACTOR x its budget fails, like the line cap

SIZE_CHECK = "startup read"
PATHS_CHECK = "cited paths exist"
MAX_SHOWN = 10

# The same markers ctx_log_last.py and ctx_plan_active.py use, so the size is what they print.
LOG_HEADING = re.compile(r"^##\s+S(\d+)\b")
PHASE_HEADING = re.compile(r"^##\s+\S*\d+\b.*$")
ANY_HEADING = re.compile(r"^##\s+\S")
ACTIVE_MARKER = "⏳"

DECISION_HEADING = re.compile(r"^###\s+D\d+\b")
IN_FORCE = re.compile(r"VIGENTE|IN FORCE")
TOUCHES = re.compile(r"^\s*-\s*\*\*(?:Toca|Touches)\s*:\*\*\s*(.*)$")
BACKTICKED = re.compile(r"`([^`\n]+)`")
CODE = (".py", ".js", ".ts", ".dart", ".ps1", ".cs", ".vb")
EXTENSIONS = CODE + (".md", ".json", ".yml", ".yaml")  # a bare `x.json` is usually a data file's name, so
# a bare name counts only with a CODE extension; with a folder in front, any of these counts.
LINE_SUFFIX = re.compile(r"(?::\d+)+$|::[\w.]+$")

Report = Callable[..., None]


def read_lines(path: Path) -> "list[str]":
    return path.read_text(encoding="utf-8", errors="replace").splitlines()


def last_log_entry(path: Path) -> str:
    """The first '## S<n>' block, as ctx_log_last.py prints it; the whole file without one."""
    lines = read_lines(path)
    starts = [i for i, ln in enumerate(lines) if LOG_HEADING.match(ln)]
    if not starts:
        return "\n".join(lines)
    end = starts[1] if len(starts) > 1 else len(lines)
    return "\n".join(lines[starts[0]:end]).rstrip()


def active_plan_phase(path: Path) -> str:
    """Every phase marked active, as ctx_plan_active.py prints them; the whole file without one."""
    lines = read_lines(path)
    phases = [i for i, ln in enumerate(lines) if PHASE_HEADING.match(ln)]
    active = [i for i in phases if ACTIVE_MARKER in lines[i]]
    if not active:
        return "\n".join(lines)
    headings = sorted(set(phases) | {i for i, ln in enumerate(lines) if ANY_HEADING.match(ln)})
    blocks = []
    for start in active:
        later = [i for i in headings if i > start]
        blocks.append("\n".join(lines[start:later[0] if later else len(lines)]).rstrip())
    return "\n\n".join(blocks)


def kb(n: int) -> str:
    return f"{n / 1000:.1f}"


def check_sizes(
    report: Report,
    ctx: Path,
    names: "dict[str, str]",
    budgets: "dict[str, int]",
) -> "dict[str, int]":
    """Measure the startup read. `names` and `budgets` are keyed STATE, LOG, PLAN, ACTIONS."""
    extract = {
        "STATE": lambda p: p.read_bytes(),
        "LOG": lambda p: last_log_entry(p).encode("utf-8"),
        "PLAN": lambda p: active_plan_phase(p).encode("utf-8"),
        "ACTIONS": lambda p: p.read_bytes(),
    }
    sizes = {}
    for key, get in extract.items():
        path = ctx / names[key]
        sizes[key] = len(get(path)) if path.is_file() else 0
    detail = f"{kb(sum(sizes.values()))} KB (" + ", ".join(f"{k} {kb(v)}" for k, v in sizes.items()) + ")"
    over = [f"{k} {kb(v)} > {kb(budgets[k])} KB" for k, v in sizes.items() if v > budgets[k]]
    if sizes["STATE"] > HARD_FACTOR * budgets["STATE"]:
        report(
            "FAIL",
            SIZE_CHECK,
            f"{detail} - {names['STATE']} is {kb(sizes['STATE'])} KB, over twice its "
            f"{kb(budgets['STATE'])} KB budget: move the oldest material to the log",
        )
    elif over:
        report("WARN", SIZE_CHECK, f"{detail} - over budget: {', '.join(over)}; every session pays it")
    else:
        report("PASS", SIZE_CHECK, detail)
    return sizes


# --- cited paths ------------------------------------------------------------------------------


def repo_root(start: Path) -> Path:
    """The repository the context folder belongs to (not the current directory)."""
    start = start.resolve()
    try:
        out = subprocess.run(
            ["git", "-C", str(start), "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        if out.returncode == 0 and out.stdout.strip():
            return Path(out.stdout.strip())
    except OSError:
        pass
    for parent in (start, *start.parents):
        if (parent / ".git").exists():
            return parent
    return Path.cwd()


def list_files(root: Path) -> "list[str]":
    """Every tracked or untracked-but-not-ignored file, relative and with '/'; one git call."""
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-co", "--exclude-standard"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        if out.returncode == 0:
            return [ln.strip() for ln in out.stdout.splitlines() if ln.strip()]
    except OSError:
        pass
    found = []
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in {".git", "node_modules", ".venv", "__pycache__"}]
        rel = Path(dirpath).relative_to(root).as_posix()
        found.extend(f if rel == "." else f"{rel}/{f}" for f in files)
    return found


class Listing:
    """Answers "does this cited path exist?" from one listing of the repository."""

    def __init__(self, files: Iterable[str], root: "Path | None" = None) -> None:
        self.root = root  # an ignored file that is on disk (a local setting) still exists
        self.files = set(files)
        self.dirs = set()
        self.names = set()
        for f in self.files:
            parts = f.split("/")
            self.names.add(parts[-1])
            for i in range(1, len(parts)):
                self.dirs.add("/".join(parts[:i]))
        self.segments = {d.split("/")[-1] for d in self.dirs}

    def exists(self, token: str) -> bool:
        path = token.rstrip("/")
        if path in self.files or path in self.dirs or (self.root and (self.root / path).exists()):
            return True
        if "/" not in path:
            return path in self.names or path in self.segments
        # A path written relative to the package it belongs to (`scripts/gate.py` for
        # `plugins/factory/scripts/gate.py`): the repository has a file or folder ending with it.
        tail = "/" + path
        return any(f.endswith(tail) for f in self.files) or any(d.endswith(tail) for d in self.dirs)

    def ignored(self, paths: "list[str]") -> "set[str]":
        """The paths git ignores: data the program writes at run time, never a file of the map."""
        if not paths or self.root is None:
            return set()
        try:
            out = subprocess.run(
                ["git", "-C", str(self.root), "check-ignore", "--stdin"],
                input="\n".join(paths).encode("utf-8"), capture_output=True,  # bytes: no "\r\n" on Windows
            )
        except OSError:
            return set()
        text = out.stdout.decode("utf-8", errors="replace")
        return {ln.strip() for ln in text.splitlines() if ln.strip()}

    def looks_like_a_path(self, token: str) -> bool:
        if token.endswith(EXTENSIONS):
            return True
        # Without an extension (`docs/dev/`, `skills/spec`) it is a path only if it starts with a
        # folder the repository has: that keeps out branches (`origin/main`) and `owner/repo`.
        return "/" in token and token.split("/")[0] in self.segments


def candidate(raw: str) -> "str | None":
    """The path a backticked token names, or None when it is not one."""
    token = LINE_SUFFIX.sub("", raw.strip().replace("\\", "/"))
    if not token or any(c in token for c in " *<>{}$|?[]()=,;'\"…") or "://" in token:
        return None
    if token.startswith(("-", "@", "~", "/", "#", "!")) or re.match(r"^[A-Za-z]:", token):
        return None
    while token.startswith("./"):
        token = token[2:]
    if token.startswith("../") or "/" not in token and not token.endswith(CODE):
        return None  # outside the repository, a bare word or a bare data file name
    if token.endswith(EXTENSIONS) and token.rsplit(".", 1)[0].rstrip("/") == "":
        return None  # a bare extension such as `.py`
    return token


def cited_in_architecture(path: Path) -> "list[str]":
    return BACKTICKED.findall(path.read_text(encoding="utf-8", errors="replace"))


def cited_in_decisions(path: Path) -> "list[str]":
    """Backticked tokens of the 'Touches:' line (and its wrapped continuation) of each entry in force."""
    found: "list[str]" = []
    in_force = collecting = False
    for line in read_lines(path):
        if line.startswith("#"):
            in_force = bool(DECISION_HEADING.match(line) and IN_FORCE.search(line))
            collecting = False
            continue
        m = TOUCHES.match(line)
        if m:
            collecting = in_force
            if collecting:
                found.extend(BACKTICKED.findall(m.group(1)))
            continue
        if collecting and line.startswith((" ", "\t")) and not line.lstrip().startswith("- "):
            found.extend(BACKTICKED.findall(line))
        else:
            collecting = False
    return found


def missing_paths(sources: "dict[str, list[str]]", listing: Listing) -> "list[str]":
    """'FILE: path' for each cited path the repository does not have, each once, in order."""
    missing, seen = [], set()
    for name, tokens in sources.items():
        for raw in tokens:
            token = candidate(raw)
            if token is None or (name, token) in seen or not listing.looks_like_a_path(token):
                continue
            seen.add((name, token))
            if not listing.exists(token):
                missing.append((name, token))
    ignored = listing.ignored(sorted({t for _, t in missing}))
    return [f"{name}: {token}" for name, token in missing if token not in ignored]


def check_paths(report: Report, ctx: Path, architecture: str, decisions: str) -> "list[str]":
    sources: "dict[str, list[str]]" = {}
    arch, dec = ctx / architecture, ctx / decisions
    if arch.is_file():
        sources[architecture] = cited_in_architecture(arch)
    if dec.is_file():
        sources[decisions] = cited_in_decisions(dec)
    if not sources:
        report("SKIP", PATHS_CHECK, f"neither {architecture} nor {decisions} found in {ctx}")
        return []
    root = repo_root(ctx)
    listing = Listing(list_files(root), root)
    missing = missing_paths(sources, listing)
    cited = sum(len(t) for t in sources.values())
    if missing:
        shown = "; ".join(missing[:MAX_SHOWN])
        more = f" (+{len(missing) - MAX_SHOWN} more)" if len(missing) > MAX_SHOWN else ""
        report(
            "WARN",
            PATHS_CHECK,
            f"{len(missing)} cited path(s) not in the repository: {shown}{more} "
            "- renamed or removed? fix the map",
        )
    else:
        report("PASS", PATHS_CHECK, f"no cited path missing ({cited} backticked token(s) read in {', '.join(sources)})")
    return missing
