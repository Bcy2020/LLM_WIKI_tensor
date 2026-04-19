---
name: wiki-delete
description: 安全删除或软删除 Wiki 页面，同时修复反链、索引、manifest 记录和 hot 缓存。
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Glob, Grep, mcp__obsidian-mcp__search_vault, mcp__obsidian-mcp__read_note, mcp__obsidian-mcp__read_multiple_notes, mcp__obsidian-mcp__move_note, mcp__obsidian-mcp__delete_note, mcp__obsidian-mcp__update_note, mcp__obsidian-mcp__manage_folder
---
# Wiki Delete

安全删除页面。

参数位于 `$ARGUMENTS`。

## 模式

### 默认：软删除
如果用户没有明确说 `hard`，就把目标页面移动到：
- `wiki/maintenance/trash/`

必要时加时间戳后缀避免重名。

### 硬删除
只有当用户明确说 `hard`、`permanent`、`remove completely` 时才执行。

### source 删除细则
如果删除的是资料摘要页：
- 删除或归档摘要页
- 更新索引与反链
- 更新 `raw/.manifest.json`
- 默认保留 raw 原文件
- 只有用户明确说 `delete raw` 且指定目标时，才删除 raw 文件

## 安全规则

- 不要直接按通配符删，先枚举精确目标
- 先解析出精确页面路径
- 有多个候选时先消歧
- 修复受影响页面中的反链
- 删除或更新陈旧索引项
- 更新 `wiki/log.md` 与 `wiki/hot.md`
- 默认中文汇报
