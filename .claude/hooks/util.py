from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path.cwd()
STATE_DIR = ROOT / ".claude" / "state"
STATE_DIR.mkdir(parents=True, exist_ok=True)

RAW_DIR = ROOT / "raw"
WIKI_DIR = ROOT / "wiki"
HOT_PATH = WIKI_DIR / "hot.md"
LOG_PATH = WIKI_DIR / "log.md"
DIRTY_PATH = STATE_DIR / "wiki_dirty.json"

def read_stdin_json() -> Dict[str, Any]:
    import sys
    data = sys.stdin.read().strip()
    if not data:
        return {}
    try:
        return json.loads(data)
    except Exception:
        return {}

def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""

def list_pending_raw_files(limit: int = 50) -> List[str]:
    ignore = {"README.md", ".manifest.json", ".keep"}
    if not RAW_DIR.exists():
        return []
    files = []
    for p in RAW_DIR.rglob("*"):
        if p.is_file() and p.name not in ignore and ".git" not in p.parts:
            files.append(str(p.relative_to(ROOT)))
    files.sort()
    return files[:limit]

def latest_log_headings(limit: int = 8) -> List[str]:
    text = read_text(LOG_PATH)
    out = []
    for line in text.splitlines():
        if line.startswith("## "):
            out.append(line.strip())
        if len(out) >= limit:
            break
    return out

def load_dirty() -> Dict[str, Any]:
    if not DIRTY_PATH.exists():
        return {}
    try:
        return json.loads(DIRTY_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}

def save_dirty(payload: Dict[str, Any]) -> None:
    DIRTY_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

def clear_dirty() -> None:
    try:
        DIRTY_PATH.unlink()
    except FileNotFoundError:
        pass

def emit_additional_context(text: str) -> None:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": os.environ.get("HOOK_EVENT_NAME", ""),
            "additionalContext": text
        }
    }, ensure_ascii=False))
