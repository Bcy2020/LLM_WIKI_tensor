---
name: wiki-reindex
description: 依据当前实际页面，重建 `wiki/wiki-index.md` 与各类 `_index.md`。适用于大改、重命名、删除或结构漂移后。
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, mcp__obsidian-mcp__list_notes, mcp__obsidian-mcp__search_vault, mcp__obsidian-mcp__read_note, mcp__obsidian-mcp__read_multiple_notes, mcp__obsidian-mcp__update_note
---
# Wiki Reindex

根据当前实际页面重建索引。

## 要重建的内容

- `wiki/wiki-index.md`
- `wiki/sources/_index.md`
- `wiki/concepts/_index.md`
- `wiki/entities/_index.md`
- `wiki/questions/_index.md`
- `wiki/maintenance/_index.md`
- `wiki/learning/_index.md`
- `wiki/maintenance/trash/_index.md`
- `wiki/domains/physics/_index.md`
- `wiki/domains/mathematics/_index.md`
- `wiki/domains/computer-agents/_index.md`

## 规则

- 以现有页面为准，不凭空编造
- 能保留有用页首说明时尽量保留
- 目录项重新计算
- 尽量稳定排序：
  - 家族索引按字母 / 规范顺序
  - 领域索引按子领域分组（可见时）
  - maintenance 需要时可按时间倒序
- 系统总索引一律写入 `wiki/wiki-index.md`
- 避免将数学/物理中的 `index` 术语链接到系统总索引页
- 默认中文写索引说明

## 完成后

更新：
- `wiki/log.md`
- `wiki/hot.md`
