---
name: wiki
description: 中文科研 Wiki 总览技能。用于回答“这个 wiki 是什么、怎么用、有哪些命令、整体架构如何”。
disable-model-invocation: false
allowed-tools: Read, Glob, Grep
---
# Wiki 总览

本项目是一套以 Obsidian 为存储层、以 Obsidian MCP 为读写接口、以 Claude Code 为操作中枢的 **中文科研 Wiki**。

执行任何 wiki 操作前，请先记住：

1. `raw/` 是原始资料层。
2. `wiki/` 是编译后的知识层。
3. 先读 `wiki/hot.md` 获取最近上下文。
4. 再读 `wiki/wiki-index.md` 做导航。
5. 对 `wiki/**/*.md` 的 CRUD / 检索优先使用 Obsidian MCP。
6. 对 raw 文件和 URL 优先使用内置 `Read` / `WebFetch`。
7. 任何有意义的 wiki 变更，都要同步更新 `wiki/wiki-index.md`、`wiki/log.md`、`wiki/hot.md`。
8. **默认用中文写 wiki 页面**；英文术语首次出现时可括注原文。
9. 数学/物理中的 `index`、`indices`、`tensor index` 等默认不得链接到总索引页。

## 可直接使用的命令

- `/wiki-status`
- `/wiki-bootstrap`
- `/wiki-ingest`
- `/wiki-batch-ingest`
- `/wiki-query`
- `/wiki-lint`
- `/wiki-delete`
- `/wiki-rename`
- `/wiki-reindex`
- `/wiki-refresh-hot`
- `/wiki-assess-mastery`
- `/wiki-teach`
- `/wiki-set-mastery`

## 参考文件

需要时可读取：

- `.claude/skills/wiki/refs/architecture.md`
- `.claude/skills/wiki/refs/frontmatter.md`
- `.claude/skills/wiki/refs/taxonomy.md`
- `.claude/skills/wiki/refs/obsidian-mcp-tooling.md`
- `WIKI_SCHEMA.md`

## 教学补充约定

- 当用户要求“评估掌握程度”时，优先使用 `/wiki-assess-mastery`。
- 当用户要求“教我某个节点”时，优先使用 `/wiki-teach`。
- 掌握度更新应写成简短、描述性的中文句子。

## 掌握度更新三档

- `/wiki-assess-mastery <节点>`：完整评估
- `/wiki-assess-mastery <节点> quick`：快速评估
- `/wiki-set-mastery <节点> + 描述`：用户直接登记
