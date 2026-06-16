# 每周学习操作流程表

## 核心原则

本系统只要求每周正式维护一次。
平时主要学习、刷题、写代码，不频繁维护仓库。

---

## 每周固定流程

| 时间 | 你要做什么 | 操作文件 / 工具 | 是否必须更新仓库 |
| --- | --- | --- | --- |
| 周一 | 查看本周计划，确认本周唯一主目标 | `WEEKLY_CURRENT.md` | 否 |
| 周二 - 周五 | 按计划学习：刷题、学基础、写代码 | LeetCode / 视频课 / Obsidian / 本地代码 | 否 |
| 周六 | 补齐本周产出：算法题、笔记、项目代码 | 本地代码 / Obsidian / 草稿 | 可选 |
| 周日 1 | 填写本周实际完成情况 | `WEEKLY_CURRENT.md` | 是 |
| 周日 2 | 让 Codex 做周维护 | `prompts/weekly-maintenance-prompt.md` | 是 |
| 周日 3 | 检查 Codex 生成的复盘和下周计划 | `review/`、`notes/weekly-notes/`、`WEEKLY_CURRENT.md` | 是 |
| 周日 4 | 提交到 GitHub | `git add`、`git commit`、`git push` | 是 |

---

## 周一操作流程

| 步骤 | 操作 |
| --- | --- |
| 1 | 打开 `WEEKLY_CURRENT.md` |
| 2 | 查看当前周次、日期范围、当前阶段 |
| 3 | 只看“本周唯一主目标” |
| 4 | 查看“必做任务”和“低状态保底任务” |
| 5 | 心里确认：这周只围绕一个主目标推进 |

周一不要重新规划全年，也不要开新方向。

---

## 周二到周五操作流程

| 每天任务类型 | 建议做法 |
| --- | --- |
| 算法 | 每天 1-2 道题 |
| 基础知识 | 学一个小知识点，例如 Java 集合、链表、HTTP、MySQL 索引 |
| 项目 / 代码 | 写一个小 demo，或者推进项目中的一个小功能 |
| 临时记录 | 记在 Obsidian、手机备忘录、草稿纸即可 |

平时不要求每天 commit。
平时不要求每天写正式笔记。
平时不要求每天更新 `WEEKLY_CURRENT.md`。

---

## 周六操作流程

| 情况 | 周六优先做什么 |
| --- | --- |
| 算法没完成 | 补算法题 |
| 笔记没整理 | 整理 1 篇周笔记草稿 |
| 项目没进展 | 写一个小 demo 或项目功能 |
| 本周任务完成较好 | 简单预习下周内容，但不要开大坑 |

周六的定位是：**补齐本周产出**。

---

## 周日正式维护流程

| 步骤 | 你要做什么 | 输出文件 |
| --- | --- | --- |
| 1 | 打开 `WEEKLY_CURRENT.md` | `WEEKLY_CURRENT.md` |
| 2 | 填写“实际完成 / 没完成 / 最大问题” | `WEEKLY_CURRENT.md` |
| 3 | 把 `prompts/weekly-maintenance-prompt.md` 发给 Codex | Codex 执行 |
| 4 | 让 Codex 生成本周复盘 | `review/2026-Wxx-review.md` |
| 5 | 让 Codex 生成本周学习笔记 | `notes/weekly-notes/2026-Wxx.md` |
| 6 | 让 Codex 归档本周计划 | `weekly/2026-Wxx.md` |
| 7 | 让 Codex 生成下周计划 | `WEEKLY_CURRENT.md` |
| 8 | 检查下周计划是否过重 | `WEEKLY_CURRENT.md` |
| 9 | 提交到 GitHub | commit |

---

## 周日需要填写的内容

在 `WEEKLY_CURRENT.md` 中填写：

```markdown
## 本周进度记录

### 实际完成

- 算法：
- 基础知识：
- 项目 / 代码：
- 笔记：

### 没完成

-

### 本周最大问题

1.
2.
3.
```

填写原则：

- 真实记录，不要美化；
- 不需要写长篇；
- 只写本周实际发生的事情；
- Codex 会根据这些内容生成复盘和下周计划。

---

## 每周最低产出

| 状态 | 最低要求 |
| --- | --- |
| 正常周 | 5-8 道算法题 + 1 篇周笔记 + 1 次代码/项目进展 + 1 篇周复盘 |
| 忙碌周 | 3 道算法题 + 1 篇短笔记 + 1 篇周复盘 |
| 崩溃周 | 1-3 道算法题 + 100 字复盘 + 不断线 |

---

## 每周 commit 规则

| 情况 | commit 频率 |
| --- | --- |
| 正常学习周 | 周日 commit 1 次 |
| 项目开发周 | 每完成一个功能 commit 1 次 |
| 忙碌周 | 周日 commit 1 次 |
| 崩溃周 | 可以只更新 `WEEKLY_CURRENT.md` 或 `review/` |

推荐 commit 信息：

```bash
git add .
git commit -m "Wxx: weekly review and next week plan"
git push
```

例如：

```bash
git add .
git commit -m "W01: weekly review and W02 plan"
git push
```

---

## 每周只看哪些文件

| 场景 | 看哪个文件 |
| --- | --- |
| 平时查看计划 | `WEEKLY_CURRENT.md` |
| 周日复盘 | `WEEKLY_CURRENT.md`、`prompts/weekly-maintenance-prompt.md` |
| 查看历史计划 | `weekly/` |
| 查看历史笔记 | `notes/weekly-notes/` |
| 查看历史复盘 | `review/` |
| 写项目代码 | `projects/` |

---

## 一句话流程

```text
周一看计划，周二到周五执行，周六补产出，周日填进度，让 Codex 复盘并生成下周计划，然后 commit。
```
