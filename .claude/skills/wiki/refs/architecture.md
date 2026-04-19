# 架构说明

## 总体设计

这个 vault 使用三层结构：

1. `raw/`
   - 原始资料
   - markdown、txt、pdf、图片、摘录、草稿等
2. `wiki/`
   - 资料摘要页
   - 概念页
   - 实体页
   - 领域综述页
   - 问题页
   - 维护页
3. `.claude/`
   - Claude Code 的操作中枢
   - skills、agents、hooks、settings

## 核心运维页面

- `wiki/hot.md` = 最近上下文缓存
- `wiki/wiki-index.md` = 总索引页
- `wiki/log.md` = 追加式操作日志
- `raw/.manifest.json` = 入库去重状态

## 为什么这样拆分

- 保持 raw 层尽量不可变
- 让 wiki 页面在 Obsidian 中成为一等笔记
- 让最近上下文可低成本恢复
- 让删除 / 重命名操作可审计
- 避免数学中的 `index` 与系统导航页冲突
