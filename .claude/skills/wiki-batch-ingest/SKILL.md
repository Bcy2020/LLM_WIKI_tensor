---
name: wiki-batch-ingest
description: 批量将 raw/ 或指定目录中的资料编译进中文 Wiki。适用于一次处理一批待入库文件。
allowed-tools: Read, Write, Edit, Glob, Grep, WebFetch, Agent, mcp__obsidian-mcp__search_vault, mcp__obsidian-mcp__read_note, mcp__obsidian-mcp__read_multiple_notes, mcp__obsidian-mcp__create_note, mcp__obsidian-mcp__update_note, mcp__obsidian-mcp__manage_folder, mcp__obsidian-mcp__auto_backlink_vault
---
# Wiki Batch Ingest

你现在要处理一批资料。

参数在 `$ARGUMENTS` 中。

## 默认行为

- 参数为空 → 处理 `raw/` 中所有待处理文件
- 参数是目录 → 递归处理该目录下支持的文件
- 参数包含 `force` → 即使 hash 相同也重新处理
- 若待处理数为 0，则直接说明并停止

## 队列顺序

默认：
1. 优先按最早未处理文件先处理，保证公平
2. 若用户指定某个目录，则尽量保持自然文件夹分组顺序

## 处理模型

对每个文件：
1. 完整阅读资料
2. 检查 manifest 去重
3. 搜索相关 wiki 页面
4. 按需更新 / 创建 source、concept、entity、domain 页面

整批完成后：
1. 修复总索引
2. 修复各类 `_index.md` 页面
3. 追加一条批处理日志
4. 刷新 `wiki/hot.md`
5. 需要时再统一运行一次 `auto_backlink_vault`

## 合理使用子 agent

需要时可使用：
- `@agent-source-distiller`：先把复杂资料抽成结构化提纲
- `@agent-domain-taxonomist`：分类有歧义时做归档判断
- `@agent-consistency-auditor`：整批结束后检查冲突与重复

## 约束

- 不要每处理一个文件都追问用户
- 只有在“放置位置或删除会受影响”的真实歧义下才提问
- 聊天里保持简洁，细节沉淀到 wiki 页面
- 默认使用中文写入页面
- 数学/物理中的 index 术语不得误链到系统总索引页

## 最终回复

返回：
- 处理数量
- 跳过数量
- 新建页面
- 更新页面
- 失败或需要人工处理的文件
- 本轮最有价值的新交叉联系
