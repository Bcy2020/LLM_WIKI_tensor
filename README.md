# Claude Code + Obsidian MCP 中文科研 Wiki Starter

这是一套面向 **物理 / 数学 / 计算机 agent** 的项目级 Claude Code + Obsidian Wiki 启动目录。里面已经有了张量分析相关内容作为示例

## 这套脚手架要解决什么

它不是“每次现问现答”的临时工作流，而是：

- 把原始资料放进 `raw/`
- 由 Claude 把资料编译进 `wiki/`
- 在 Obsidian 里持续维护、交叉链接、查询与修复

## 目录说明

- `.claude/`：skills、hooks、agents、项目设置
- `.mcp.json`：Obsidian MCP 项目配置
- `raw/`：原始资料层
- `wiki/`：编译后的知识层
- `_templates/`：模板

## 正确打开方式

**请用 Obsidian 打开整个项目根目录，而不是只打开 `wiki/` 子目录。**

## 一次性配置

1. 安装 Obsidian 桌面版
2. 安装 Obsidian 的 Local REST API 插件并生成 token
3. 复制：

```bash
cp .claude/settings.local.example.json .claude/settings.local.json
```

4. 填入：
   - `OBSIDIAN_VAULT_PATH`
   - `OBSIDIAN_API_TOKEN`
   - `OBSIDIAN_API_PORT`

## 日常使用

### 查看状态
```text
/wiki-status
```

### 单个入库
```text
/wiki-ingest raw/你的文件.pdf
```

### 批量入库
```text
/wiki-batch-ingest
```

### 查询
```text
/wiki-query 解释李雅普诺夫稳定性和能量方法的关系
```

### 维护
```text
/wiki-lint
/wiki-reindex
/wiki-refresh-hot
```

### 改名与删除
```text
/wiki-rename wiki/concepts/old-name.md wiki/concepts/new-name.md
/wiki-delete wiki/concepts/obsolete-note.md
/wiki-delete wiki/concepts/obsolete-note.md hard
```

## 重要约束

- Wiki 页面默认使用中文
- 公式、符号、定理记号保持原样
- `index` 在数学/物理语境中默认视为术语，不得自动链接到系统导航页
- 系统导航页统一为 `wiki/wiki-index.md`
- Windows 下 hooks 已改为 `py -3 -X utf8 ...`，避免 `python3` 启动问题

## 推荐启动测试

```text
/wiki-status
/wiki-batch-ingest
/wiki-query 当前这个 wiki 最近新增了什么
```

## 教学功能

现在新增两个命令：

```text
/wiki-assess-mastery wiki/concepts/某个节点.md
/wiki-teach wiki/concepts/某个节点.md
```

- `/wiki-assess-mastery`：先让用户自述，再进行 5~10 个问题的评估，最后更新节点掌握度。
- `/wiki-teach`：按“讲解 → 提问澄清 → 用户复述 → 纠正 → 更新掌握度”的流程教学。

## 掌握度更新三种方式

```text
/wiki-assess-mastery <节点>
/wiki-assess-mastery <节点> quick
/wiki-set-mastery <节点> 我已经能……但……
```

- 完整评估：适合重要节点
- quick：适合基础节点
- set-mastery：适合用户明确知道自己想怎么登记的情况
