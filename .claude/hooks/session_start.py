#!/usr/bin/env python3
from __future__ import annotations

import json
from util import HOT_PATH, list_pending_raw_files, latest_log_headings, read_stdin_json, read_text

event = read_stdin_json()
pending = list_pending_raw_files(limit=20)
hot = read_text(HOT_PATH).strip()
recent = latest_log_headings(limit=6)

parts = [
    "项目 Wiki 启动上下文。",
    "先读 wiki/hot.md，再读 wiki/wiki-index.md，随后读取最相关的分区 _index.md。",
    "默认将 raw/ 视为原始资料层，不随意改写。",
    "对 wiki/**/*.md 的检索与读写优先使用 Obsidian MCP；对 raw 资料优先使用内置 Read/WebFetch。",
    "数学/物理中的 index、indices、tensor index 等术语默认不得链接到系统总索引页。",
]

if pending:
    parts.append("待处理原始资料：\n- " + "\n- ".join(pending))
else:
    parts.append("待处理原始资料：无。")

if recent:
    parts.append("最近日志条目：\n- " + "\n- ".join(recent))

if hot:
    parts.append("当前 hot 缓存：\n" + hot[:4000])

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": "\n\n".join(parts),
    }
}, ensure_ascii=False))
