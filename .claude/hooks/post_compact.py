#!/usr/bin/env python3
from __future__ import annotations

import json
from util import HOT_PATH, read_text

hot = read_text(HOT_PATH).strip()
if not hot:
    raise SystemExit(0)

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "PostCompact",
        "additionalContext": "压缩后重新注入 hot 缓存。\n\n" + hot[:4000],
    }
}, ensure_ascii=False))
