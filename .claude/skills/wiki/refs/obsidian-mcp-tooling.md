# Obsidian MCP 工具说明

当前配置的服务器名是 `obsidian-mcp`，因此工具名格式为：

`mcp__obsidian-mcp__<tool_name>`

## 常用工具

- `mcp__obsidian-mcp__list_notes`
- `mcp__obsidian-mcp__read_note`
- `mcp__obsidian-mcp__read_multiple_notes`
- `mcp__obsidian-mcp__create_note`
- `mcp__obsidian-mcp__update_note`
- `mcp__obsidian-mcp__delete_note`
- `mcp__obsidian-mcp__search_vault`
- `mcp__obsidian-mcp__move_note`
- `mcp__obsidian-mcp__manage_folder`
- `mcp__obsidian-mcp__auto_backlink_vault`

## 操作建议

- 找页面先用 `search_vault`
- 已知少量页面时优先用 `read_multiple_notes`
- 局部修改优先用 `update_note`
- 重命名 / 移动优先用 `move_note`
- 建目录与 trash 用 `manage_folder`
- `auto_backlink_vault` 只在大批量入库或重建索引后再谨慎使用

## 边界

`wiki/` 中的页面优先用 MCP。
下列内容优先用内置文件工具：
- raw 原始资料
- manifest JSON
- Claude 配置
- 模板
