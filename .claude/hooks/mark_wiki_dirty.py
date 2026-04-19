#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone
from util import clear_dirty, load_dirty, read_stdin_json, save_dirty

event = read_stdin_json()
tool_name = event.get("tool_name", "")
tool_input = event.get("tool_input", {}) or {}
raw = json.dumps(tool_input, ensure_ascii=False)

# If the operation clearly touched hot.md, treat it as a freshness update and clear the dirty flag.
if "wiki/hot.md" in raw or "/wiki/hot.md" in raw:
    clear_dirty()
    raise SystemExit(0)

dirty = load_dirty()
dirty["last_change_utc"] = datetime.now(timezone.utc).isoformat()
dirty["tool_name"] = tool_name
dirty["tool_input"] = tool_input
save_dirty(dirty)
