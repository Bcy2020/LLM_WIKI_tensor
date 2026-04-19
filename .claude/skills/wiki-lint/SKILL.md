---
name: wiki-lint
description: 审计中文 Wiki 的坏链、重复页、矛盾、陈旧表达、孤儿页、分类漂移、弱反链以及 manifest/source 不一致，并写入维护报告。
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, Bash, mcp__obsidian-mcp__list_notes, mcp__obsidian-mcp__search_vault, mcp__obsidian-mcp__read_note, mcp__obsidian-mcp__read_multiple_notes, mcp__obsidian-mcp__create_note, mcp__obsidian-mcp__update_note
---
# Wiki Lint

审计整个 wiki，并写出维护报告。

## 检查项

### 错误
- 坏的 wikilink
- 缺失 frontmatter 或关键字段
- 明显重复的 concept / entity 页面
- 路径或 frontmatter 冲突
- manifest 与 source 摘要页不一致
- 形如 `[index`、`[[[[index]]]]`、`[[index]]]]` 的脏链接

### 警告
- 可学习节点缺少 `mastery` 字段
- `mastery` 文本过长、过空或过于模板化
- 无日期却使用“当前 / 最新 / 最近”等表达
- 分类漂移
- source 页缺少 concept / entity / domain backlink
- 重要页面反链过弱
- 数学/物理语境中的 `index` 被误链到系统总索引页

### 信息项
- 值得合并的页面
- 值得拆分的页面
- 应新增资料的空白点
- 应调整领域归属的页面

## 检查输入

- 顶层 meta 页面
- 所有 `_index.md` 页面
- sources / concepts / entities / domains / questions / maintenance 的代表页面
- `raw/.manifest.json`

当问题较杂或 vault 较大时，使用 `@agent-consistency-auditor`。

## 报告输出位置

写入：
- `wiki/maintenance/lint-YYYY-MM-DD-HHMM.md`

然后更新：
- `wiki/maintenance/_index.md`
- `wiki/wiki-index.md`
- `wiki/log.md`
- `wiki/hot.md`

## 报告结构

1. 总结统计
2. 错误
3. 警告
4. 改进建议
5. 精确修复建议

除非用户明确要求把 lint 变成 repair，否则不要直接删除页面。
