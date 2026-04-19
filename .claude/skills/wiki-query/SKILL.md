---
name: wiki-query
description: 从 wiki 中回答问题，而不是靠记忆猜测。先读 hot，再读索引，再读相关页面；必要时可把答案沉淀到 wiki/questions/。
allowed-tools: Read, Glob, Grep, mcp__obsidian-mcp__search_vault, mcp__obsidian-mcp__read_note, mcp__obsidian-mcp__read_multiple_notes, mcp__obsidian-mcp__create_note, mcp__obsidian-mcp__update_note
---
# Wiki Query

请使用 wiki 作为事实来源来回答用户问题。

问题位于 `$ARGUMENTS`。

## 检索顺序

1. 读取 `wiki/hot.md`
2. 读取 `wiki/wiki-index.md`
3. 读取最相关的家族 / 领域 `_index.md`
4. 搜索 vault
5. 只读取最相关的页面
6. 如问题涉及学习状态，再读取相关节点的 `mastery` 字段与 `wiki/learning/` 记录

如果用户显然是在问 wiki 内容，**不要脱离 wiki 用常识硬答**。

## 输出要求

- 默认用中文回答
- 清楚回答
- 在适当位置引用页面路径或 wikilink
- 区分已知事实与空白点
- 如有矛盾，明确指出
- 保持公式和符号精确
- 不要把数学里的 `index` 误解成系统总索引

## 是否回写

回答后，判断这份答案是否值得沉淀。

以下情况应自动沉淀：
- 用户明确要求保存
- 这是较复杂的综合说明，后续大概率还会用到
- 它解决了反复出现的比较 / 解释类问题

保存到：
- `wiki/questions/<slug>.md`

然后同步更新：
- `wiki/wiki-index.md`
- `wiki/questions/_index.md`
- `wiki/log.md`
- `wiki/hot.md`
