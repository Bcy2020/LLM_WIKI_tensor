#!/usr/bin/env python3
from __future__ import annotations

import json
from util import load_dirty, read_stdin_json

event = read_stdin_json()
dirty = load_dirty()
if not dirty:
    raise SystemExit(0)

if event.get("stop_hook_active"):
    raise SystemExit(0)

reason = (
    "本次会话中 Wiki 已发生变更。停止前请先刷新 `wiki/hot.md`，"
    "以便下一次会话能快速恢复上下文。请运行 `/wiki-refresh-hot`，"
    "或直接更新 `wiki/hot.md` 后再停止。"
)

print(json.dumps({
    "decision": "block",
    "reason": reason
}, ensure_ascii=False))
