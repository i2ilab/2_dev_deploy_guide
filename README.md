# 2_dev_deploy_guide — Build 与 Ship 双支柱(开发 + 部署指南)

> 你已经用 `1_DEFINE_guide` 把 agent **想清楚(PRD)、评明白(Eval)**。
> 这个模块教你把它 **做出来(Build)** 并 **送上线(Ship)**——变成一个**任何人手机能打开、能对话的公网应用**。
> **你不需要会写代码、不需要懂前端后端。** 你的活是:指挥 Claude Code 来写,你负责**看懂架构 · 守住 key 安全 · 把关体验**。

---

## 这是 i2i 的后半段

```
 Idea ─────► Build ─────► Ship ─────► Impact
 (定义)      (做出来)     (送上线)     (影响)
  └── 1_DEFINE_guide ──┘  └──── 2_dev_deploy_guide(本模块）────┘
      定义 + 评估              前端 + 后端 + 部署
```

模块序列:`0_agent_basic`(造 agent 行为)→ `1_claude_code_basic`(造 mini CC harness)→ `1_DEFINE_guide`(定义+评估)→ **`2_dev_deploy_guide`(做出来+送上线,本模块)**。

## ★ 后端不用从零:就是你造过的 mini CC harness

`1_claude_code_basic` 里你亲手做的 `c5_guard.py`,已经是一个完整的 mini Claude Code。它的**五根支柱,正好对应上线要的五个能力**——本模块只教你把它**包成一个 Web 服务并送上线**:

| harness 支柱(模块 1) | 上线后的真实用途 |
|---|---|
| c0 JSON 协议 | 结构化输出,前端稳定解析 |
| c1 工具箱 | 读写文件 + 领域工具(查量表 / 存情绪日记 / 记录进度) |
| c2 TodoWrite | 多步任务拆步(如陪做一次完整 CBT 思维记录) |
| **c3 子 agent** | **安全复核层 —— 就是 `1_DEFINE_guide` E4 自检环的后端落地** |
| c4 上下文压缩 | 长程陪伴多轮对话不爆 token |
| c5 权限门 | 服务端只留白名单工具(去掉危险的 bash) |

**改造只做三件事**:`while input()` 交互循环 → 无状态 `/api/chat`;key 从 `os.environ` 读(绝不进前端);去掉 bash,只留安全工具。全 Python → FastAPI → Railway,一条链。

## 两个支柱,10 个阶段(每步一个产出物)

### 支柱一 · BUILD(做出来) → `BUILD/`

| 阶段 | 核心想法 | 产出物 | 配套 skill |
|---|---|---|---|
| B0 | 你是导演不是码农;三层架构 + harness 五支柱 | —(读) | — |
| B1 | 以 harness 为底装领域 skills + 危机转介(置顶)+ c3 安全复核 | 技术架构卡 | `/build-backend` |
| B2 | 把 harness 变成 FastAPI `/api/chat`(key 走 env、去 bash、优雅降级) | API 契约卡 | `/build-backend` |
| B3 | 三句话让 Claude Code 生成聊天前端 + 危机按钮 + 优雅降级 | 前端提示词卡 | `/build-frontend` |
| B4 | 前端只调后端、**绝不放 key**(`grep sk-` 为零)、CORS | 本地跑通的全栈 MVP | `/build-connect` |

### 支柱二 · SHIP(送上线) → `SHIP/`

| 阶段 | 核心想法 | 产出物 | 配套 skill |
|---|---|---|---|
| S0 | 不上线=没 impact;静态 vs 动态判断;三平台 + 成本 | —(读) | — |
| S1 | GitHub Pages 静态上线 | 公网展示 URL | `/ship-static` |
| S2 | FastAPI → Railway(Python 友好,= HEAI 同款);Vercel 免费替代 | 后端公网 URL | `/ship-backend` |
| S3 | 前端接后端 + CORS + 手机跨设备测 | 手机能打开的可对话应用 | `/ship-golive` |
| S4 | 上线检查清单 + 结项技术文档 | 上线检查全过 + 结项文档 | `/ship-golive` |

## 默认技术栈(用户已定)

- **前端**:一张静态聊天页(Claude Code 生成)→ **GitHub Pages**(免费)
- **后端**:**Python FastAPI**(包着你的 mini CC harness)→ **Railway**(默认,Python 友好,= HEAI/renben.ai 同款)
- **模型**:OpenRouter(你在 `0_agent_basic` 已配的那把 key),**只在后端 env**
- **免费替代**:Vercel(Node serverless)——Railway ~$5 试用/hobby 非永久免费,要零成本用 Vercel

## 三条使用路径(可混用)

1. **跟着走**:按 `B0→B4` 再 `S0→S4`,每阶段填模板、过门禁。主教程:`教程_从harness到上线.md`。
2. **让 AI 带着走**:启动 Claude Code,六个 skill(`/build-*` `/ship-*`)**分步陪跑、自动扫 `sk-`、不一次甩全部命令**。它们让 Claude Code 写代码,但由你把关架构与安全。
3. **对照示例**:`example_project/` —— 三档真实参考架构(**小智**静态+离线兜底 / **HEAI** FastAPI+证据引用=默认样板 / **Agent Leo** 全栈+多agent)+ 一个**能跑的端到端最小骨架** `端到端示例_考前3分钟/`(前端静态 + FastAPI 后端,已本地验证)。

## 目录导览

```
web_basics/                 ★零 web 基础先读:HTML/CSS/JS·框架·后端·API·工具链(看懂+会指挥)+ 30 页 slides
BUILD/  B0–B4                做出来:后端(harness→FastAPI)+ 前端 + 连通
SHIP/   S0–S4                送上线:Pages + Railway + 整体上线 + 检查结项
templates/                   技术架构卡 / API契约卡 / 前端提示词卡 / 部署选型决策卡 / 密钥环境变量清单 / 上线检查清单 / 结项技术文档
checklists/                  后端自检 / 前端安全(无 sk-) / 上线检查 / 部署平台对照表
example_project/             三档参考架构 + ★端到端示例_考前3分钟(可运行:backend FastAPI + frontend 静态页)
.claude/skills/              /build-* /ship-* 六个教练 skill(分步陪跑、自动扫 sk-、不代做决定)
resources.md                技术资源按「什么时候查」组织 + 三项目 repo 指路
教程_从harness到上线.md        主教程:考前3分钟一条线,从 harness 到公网 URL
作业指南_开发与部署.md          里程碑 M1–M5 + 三级提示 + Capstone
助教评分要点_开发与部署.md      能否真上线 + key 安全/危机护栏一票否决 + 假完成识别
web/index.html              交互指南(离线单文件):Build/Ship 导航 + 门禁进度 + 🔑密钥泄漏自检模拟器 + 🧭部署选型助手
slides/                     Fathom 数据叙事风 20 页 PPTX(可编辑)
```

## 三条红线

1. **key 只能待在后端**——前端是公开的,任何人能看源码。上线前 `grep -rniE "sk-[a-z0-9]{16}"` 前端必须为零。
2. **危机由确定性代码兜底**——`is_crisis()` 在入口/出口各拦一次,不只靠模型自觉。安全一票否决。
3. **不上线,就没有 impact**——躺在你电脑里的 agent,影响力是零。

## 和其它模块的关系

- **不重复造 harness**:怎么造 agent 内核在 `0_agent_basic` / `1_claude_code_basic`;本模块只"**把已造好的 harness 包成服务并上线**"。
- **不重复方法论**:选题/PRD/评估/危机测试在 `1_DEFINE_guide`;这里直接用你产出的 PRD + 危机红线。
- 一句话:**前几个模块给了你手、眼睛和心;这个模块让你的作品走出你的电脑,被真实的人用上。**

---
*MIT License｜郑先隽,北京师范大学心理学部教授,人本 AI 设计与创新｜助教:元真、诗婕*
