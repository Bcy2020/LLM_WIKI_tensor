---
name: wiki-set-mastery
description: 对某个节点进行用户主导的强制掌握度登记。用户直接给出想写入的掌握描述，LLM 只做最小规范化和安全校验，不做长问答。
allowed-tools: Read, Write, Edit, Glob, Grep, mcp__obsidian-mcp__search_vault, mcp__obsidian-mcp__read_note, mcp__obsidian-mcp__read_multiple_notes, mcp__obsidian-mcp__update_note, mcp__obsidian-mcp__create_note
---
# Wiki Set Mastery

你现在要执行“强制掌握度登记”。

目标节点与用户想写入的掌握描述都在 `$ARGUMENTS` 中。

## 适用场景

用于：
- 基础知识点
- 用户已经明确知道自己想怎么登记
- 用户不希望被问很多问题
- 补录掌握状态，而不是严格诊断

## 总原则

- 这是**用户主导覆盖**，不是 LLM 自主评估。
- 不做长问答。
- 只允许做最小校验与规范化。
- 默认只更新当前目标节点，**不要自动改周边节点**。

## 你的工作

### 第 1 步：定位节点
1. 解析目标节点路径或名称。
2. 读取目标页面。
3. 读取当前的 `mastery` 字段，供回写时参考。

### 第 2 步：获取用户描述
如果 `$ARGUMENTS` 中已经包含明显的掌握描述，就直接使用。
如果没有，就让用户补一句简短描述，例如：
- “我已经能稳定区分自由指标和哑指标，但复杂缩并仍容易出错”
- “我知道 ReAct 的流程，但还不能很好解释它和 planning 的区别”

### 第 3 步：最小校验与规范化
你只做这些检查：
- 是否过长
- 是否过空泛
- 是否明显与节点无关
- 是否需要压缩成更规范的 `mastery` 中文句子

可以做轻微润色，但**不得改写用户原意**。

### 第 4 步：写回 frontmatter
更新：
- `mastery`
- `mastery_updated`
- `mastery_basis`
- `mastery_neighbors`

写法要求：
- `mastery`：简短、具体、描述性强
- `mastery_basis`：固定写成 `用户直接登记（未做问答）`
- `mastery_neighbors`：默认留空，或保留原值；不要凭空填充

### 第 5 步：沉淀记录
将本次强制登记摘要保存到：
- `wiki/learning/set-mastery-YYYY-MM-DD-HHMM-<slug>.md`

并更新：
- `wiki/learning/_index.md`
- `wiki/log.md`
- `wiki/hot.md`

## 输出要求

最终向用户汇报：
- 原掌握度
- 新掌握度
- 你是否做了文字规范化
- 明确说明本次是“用户直接登记”，不是诊断结果
