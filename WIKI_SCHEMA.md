# Wiki 结构约定

## 目标

这个 vault 是一套面向以下领域的 **持续累积型中文科研 Wiki**：

- physics
- mathematics
- computer-agents

除了做知识沉淀，它还承担 **教学与掌握度跟踪** 的功能。

## 三层结构

- `raw/` = 原始资料层，默认不可变
- `wiki/` = 由 LLM 维护的派生知识层
- `_templates/` = 模板层，供技能与人工共同使用

## 顶层核心页面

- `wiki/wiki-index.md` — 总索引页
- `wiki/log.md` — 追加式操作日志
- `wiki/hot.md` — 最近上下文缓存
- `wiki/overview.md` — 总体说明与当前理解

## 主要页面家族

- `wiki/sources/` — 资料摘要页
- `wiki/concepts/` — 概念页
- `wiki/entities/` — 实体页
- `wiki/domains/physics/` — 物理主题页与分索引
- `wiki/domains/mathematics/` — 数学主题页与分索引
- `wiki/domains/computer-agents/` — agent 系统主题页与分索引
- `wiki/questions/` — 值得沉淀的问题页/分析页
- `wiki/learning/` — 评估与教学记录页
- `wiki/maintenance/` — lint 报告、修复记录、trash、运维页

## frontmatter 规则

统一使用扁平 YAML，不使用嵌套对象。

最小推荐字段：

```yaml
type: concept
title: "示例标题"
status: active
domains:
  - mathematics
tags:
  - topology
sources:
  - wiki/sources/example-source.md
mastery: "对核心定义有了解，但应用尚不熟练"
mastery_updated: 2026-04-18
mastery_basis: "自述 + 7 题诊断"
mastery_neighbors: "相邻概念中，线性映射较稳，张量积较弱"
created: 2026-04-18
updated: 2026-04-18
```

## `type` 允许值

- `meta`
- `source`
- `concept`
- `entity`
- `domain`
- `question`
- `maintenance`
- `learning`

## `status` 允许值

- `active`
- `stub`
- `archived`
- `conflict`
- `deprecated`

## 掌握程度字段（重要）

每个节点都可以维护以下字段：

- `mastery`：**简短、描述性** 的掌握表述，不使用“已掌握/未掌握”这种过粗标签
- `mastery_updated`：最近评估或教学更新日期
- `mastery_basis`：本次判断依据，例如“自述 + 6 题问答 + 复述纠偏”
- `mastery_neighbors`：对周边节点的系统性观察，保持简短

### `mastery` 写作要求

- 尽量控制在一两句话内
- 要描述“知道到什么程度、不会到什么程度”
- 例子：
  - `对核心定义有初步了解，但自由指标与哑指标的区分仍不稳定`
  - `能解释 ReAct 的主流程，但对 tool-use 与 planning 的边界还不够清楚`
  - `能完成基础推导，并能与邻近概念建立联系，复杂应用仍需练习`

## 教学与评估闭环

针对节点可执行两类操作：

1. **掌握度登记 / 评估（完整模式）**
   - 用户先自述
   - LLM 提出 5~10 个问题
   - 问题应以目标节点为主，并略微覆盖周边节点
   - 根据回答更新 `mastery` 等字段
   - 若证据强，也可谨慎更新相邻节点的掌握描述

2. **掌握度登记 / 快速模式**
   - 用户先自述
   - LLM 只问 2~3 个关键问题
   - 适用于十分基础的节点或补录
   - 更新 `mastery` 等字段，但不做冗长盘问

3. **强制掌握度登记**
   - 用户直接给出掌握描述
   - LLM 只做最小规范化
   - `mastery_basis` 应标记为 `用户直接登记（未做问答）`
   - 默认不更新周边节点

4. **节点教学**
   - 根据目标节点及周边节点掌握度，生成针对性讲解
   - 允许多轮用户提问与澄清
   - 最后要求用户复述
   - LLM 负责纠正并更新掌握度

## 命名规则

- 文件名优先使用稳定的 slug（小写、kebab-case）
- 标题与正文优先中文
- 英文术语首次出现可双语并列
- manifest 和 log 中优先记录 vault 相对路径

## 链接规则

正常使用 Obsidian wikilink：
- `[[note-name]]`
- `[[path/to/file|显示名]]`

### index 歧义规则（重要）

为避免与数学/物理中的“指标 index”冲突：

- 系统导航页一律使用 `wiki/wiki-index.md`
- 导航页的推荐显示名一律是 `总索引`
- **不得**把普通词 `index`、`indices` 自动链接到系统页
- 张量指标、自由指标、哑指标等专业术语，应链接到其真实概念页，而不是导航页
- 出现形如 `[index`、`[[[[index]]]]`、`[[index]]]]` 的畸形链接时，应视为脏链接并在 lint / reindex 中修复

## 中文写作规范

- Wiki 正文默认中文
- 保留公式与记号的精确性
- 重要英文术语首次出现可加括注
- 不写营销化语言，不写空泛套话
- 摘要要可追溯，必要时指出来源页与矛盾点

## raw manifest

`raw/.manifest.json` 用于记录资料入库状态。

## 删除策略

默认采用 **软删除**：
- 移动到 `wiki/maintenance/trash/`
- 修复 backlinks
- 更新索引与日志

只有在用户明确要求时，才执行硬删除。
