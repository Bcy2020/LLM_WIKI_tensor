---
name: wiki-status
description: 查看当前中文 Wiki 的运行状态：待处理资料、manifest 覆盖情况、核心页面新鲜度、最近操作、领域覆盖与维护信号。
allowed-tools: Read, Glob, Grep, mcp__obsidian-mcp__list_notes, mcp__obsidian-mcp__read_note, mcp__obsidian-mcp__search_vault
---
# Wiki Status

报告当前 wiki 的运行状态。

## 检查项

- `raw/` 中待处理文件
- `raw/.manifest.json`
- `wiki/hot.md`
- `wiki/wiki-index.md`
- `wiki/log.md` 最近条目
- 各主要目录中的 `_index.md`
- 各类页面数量：
  - sources
  - concepts
  - entities
  - questions
  - maintenance
  - learning
  - domain topic pages
- 明显漂移：
  - raw 文件无 manifest 记录
  - manifest 指向的摘要页缺失
  - 核心页面缺失
  - trash 缺失

## 输出格式

1. **队列**
   - 待处理 raw 文件数量
   - 最多列出 20 个待处理文件
2. **核心健康度**
   - hot 缓存新鲜度
   - 总索引是否存在
   - overview 是否存在
3. **覆盖情况**
   - 各类页面数量
   - 各主领域数量（能判断时）
4. **最近活动**
   - 最近 5 条日志
5. **警告**
   - 具体修复建议

## 约束

- 这是只读检查技能。
- 除非用户明确要求 `repair`，否则不要直接修改 vault。
