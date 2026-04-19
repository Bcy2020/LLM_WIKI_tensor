---
name: wiki-rename
description: 安全重命名或移动 Wiki 页面，同时保留反链、索引、manifest 引用与 hot 缓存。用于规范命名、去重和分类整理。
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Glob, Grep, mcp__obsidian-mcp__search_vault, mcp__obsidian-mcp__read_note, mcp__obsidian-mcp__read_multiple_notes, mcp__obsidian-mcp__move_note, mcp__obsidian-mcp__update_note
---
# Wiki Rename

安全地重命名或移动一个页面。

参数在 `$ARGUMENTS` 中，应能识别出：
- 原路径 / 原页面
- 新路径 / 新文件名

## 规则

1. 先解析出精确旧页面。
2. 确认新路径不会意外撞名。
3. 使用 `move_note` 执行移动 / 重命名。
4. 修复全 vault 的反链：
   - 旧 wikilink
   - 索引中的旧显式路径
   - `raw/.manifest.json` 中相关旧路径
5. 更新 `wiki/wiki-index.md`、相关 `_index.md`、`wiki/log.md`、`wiki/hot.md`。
6. 默认中文汇报。
