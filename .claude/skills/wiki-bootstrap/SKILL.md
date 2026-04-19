---
name: wiki-bootstrap
description: 修复或补齐中文 Wiki 脚手架。用于首次安装后初始化，或在目录/索引损坏时重建缺失部分。
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Glob, Grep, mcp__obsidian-mcp__manage_folder, mcp__obsidian-mcp__create_note, mcp__obsidian-mcp__read_note, mcp__obsidian-mcp__search_vault
---
# Wiki Bootstrap

用于确认并修复 vault 的核心结构。

## 目标

确保以下内容存在：

- `raw/`
- `raw/.manifest.json`
- `wiki/wiki-index.md`
- `wiki/log.md`
- `wiki/hot.md`
- `wiki/overview.md`
- `wiki/sources/_index.md`
- `wiki/concepts/_index.md`
- `wiki/entities/_index.md`
- `wiki/questions/_index.md`
- `wiki/maintenance/_index.md`
- `wiki/maintenance/trash/_index.md`
- `wiki/learning/_index.md`
- `wiki/domains/physics/_index.md`
- `wiki/domains/mathematics/_index.md`
- `wiki/domains/computer-agents/_index.md`

## 规则

- 除非用户明确要求 `rebuild` 或 `reset`，否则不要覆盖已有且内容充实的页面。
- Wiki 笔记优先用 Obsidian MCP 创建。
- `raw/.manifest.json` 与非笔记脚手架优先用内置文件工具处理。
- 如果只缺少少数部件，就只修缺少部分。
- 默认产出中文页面。
- 系统导航页统一使用 `wiki/wiki-index.md`，不要再创建 `wiki/wiki-index.md`。

## 步骤

1. 检查必须存在的目录和文件。
2. 先补齐缺失目录。
3. 再补齐缺失的索引页与 meta 页。
4. 确保 `wiki/maintenance/trash/` 存在。
5. 确保 `raw/.manifest.json` 存在且至少为：

```json
{
  "sources": {}
}
```

6. 汇报修复结果。
7. 若损坏较重，建议继续运行：
   - `/wiki-reindex`
   - `/wiki-refresh-hot`
   - `/wiki-lint`
