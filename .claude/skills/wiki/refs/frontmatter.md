# Frontmatter 说明

统一使用扁平 YAML。

## 资料页示例

```yaml
type: source
title: "资料标题"
status: active
domains:
  - computer-agents
tags:
  - source
  - llm-wiki
source_kind: paper
source_path: raw/some-file.pdf
source_url:
created: 2026-04-18
updated: 2026-04-18
```

## 概念页示例

```yaml
type: concept
title: "ReAct"
status: active
domains:
  - computer-agents
tags:
  - concept
  - prompting
  - tool-use
sources:
  - wiki/sources/react-paper.md
created: 2026-04-18
updated: 2026-04-18
```

## 实体页示例

```yaml
type: entity
title: "Andrej Karpathy"
status: active
domains:
  - computer-agents
tags:
  - entity
  - person
sources:
  - wiki/sources/llm-wiki-gist.md
created: 2026-04-18
updated: 2026-04-18
```

## 领域页示例

```yaml
type: domain
title: "物理"
status: active
domains:
  - physics
tags:
  - domain
created: 2026-04-18
updated: 2026-04-18
```

## 问题/分析页示例

```yaml
type: question
title: "问题标题"
status: active
domains:
  - mathematics
tags:
  - question
  - analysis
sources:
  - wiki/concepts/example.md
created: 2026-04-18
updated: 2026-04-18
```


## 掌握度字段示例

```yaml
mastery: "对核心定义有初步了解，但应用尚不熟练"
mastery_updated: 2026-04-18
mastery_basis: "自述 + 6 题问答 + 复述纠偏"
mastery_neighbors: "与线性映射的关系较稳，对张量积仍较弱"
```
