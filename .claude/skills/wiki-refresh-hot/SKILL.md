---
name: wiki-refresh-hot
description: 根据最新日志、待处理 raw 队列、overview 与近期重要页面，重建 `wiki/hot.md`。在停止前或大改后使用。
allowed-tools: Read, Glob, Grep, mcp__obsidian-mcp__read_note, mcp__obsidian-mcp__search_vault, mcp__obsidian-mcp__update_note, mcp__obsidian-mcp__create_note
---
# Wiki Refresh Hot

刷新 `wiki/hot.md`。

## 目的

这是缓存，不是完整日志。
它应该：
- 事实性强
- 简洁
- 便于下一次会话快速恢复

## 来源

- `wiki/log.md` 最近 10 条相关记录
- `raw/` 当前待处理队列
- `wiki/overview.md`
- 主要未解问题
- 近期新增或改动最大的关键页面

## 长度控制

目标约 250-500 词。

## 建议结构

```markdown
---
type: meta
title: "热缓存"
status: active
domains:
  - physics
  - mathematics
  - computer-agents
tags:
  - hot-cache
created: 2026-04-18
updated: 2026-04-18
---

# 最近上下文

## 最近更新时间

## 关键事实

## 最近变更

## 当前主线

## 待处理原始资料
```

## 规则

- 直接整页重写
- 不要写成巨型总结
- 优先保留最新、最可操作的上下文
- 默认中文
