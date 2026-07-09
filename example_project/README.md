# example_project —— 三档参考架构 + 一个能跑的端到端示例

> **看颗粒度,别照抄。** 这里放的是"真实项目长什么样"的参考,不是让你复制粘贴。
> 老师的三个真实项目,正好是**由易到难的三档架构**——你按自己的项目复杂度,挑一档学。
> 想直接看一个**最小但真能跑**的完整例子:进 `端到端示例_考前3分钟/`(前端 + 后端 + 部署说明都在,已测试可运行)。

## 三档参考架构对照

| 项目 | 前端 | 后端 | 部署 | 最亮的一招 | 复杂度档位 |
|---|---|---|---|---|---|
| **小智 / reading-bot** | Next.js 静态导出(纯 HTML/JS,可离线) | 零依赖 Node 小服务 + companion agent | Railway / 打包成安卓 APK | **优雅降级**:AI 连不上就回退到脚本,孩子无感 | 🟢 入门档 |
| **HEAI / renben.ai** | Vanilla HTML + D3.js(手写网页 + 图表) | **Python FastAPI**(和你学的 Python 一脉相承) | Docker + Railway | **强制引用 grounding**:回答必须带证据出处,反幻觉 | 🟡 中档(= 本模块默认路径样板) |
| **Agent Leo / deepsy.ai** | Next.js 14 全栈 + Tailwind | Claude CLI 子进程代理 + **Supabase**(数据库/登录) | Railway + Cloudflare(国内加速) | **多 agent 编排** + persona-as-code(换 SKILL.md = 换专家) | 🔴 进阶档 |

**三个的共同点(记住这三条,比记框架名重要)**:
1. **key 绝不进前端**——都是"前端 → 自己的后端 → 模型",key 只待在后端环境变量里。
2. **人设是 `SKILL.md` 文件**——就是你在 `0/1_claude_code_basic` 学的 agent.md + skill,换文件就换角色。
3. **都用 Railway 部署**——不是巧合:Railway 对 Python/Node 都自动识别,是这类小项目最省心的落点。

## 怎么选(按你的项目)

- **只想快点上线、给人看得见** → 学 **小智** 的静态思路 + 直接照 `端到端示例_考前3分钟/`。
- **要一个能真对话、带 Python 后端的 agent**(大多数组) → 学 **HEAI**:vanilla 前端 + FastAPI + Railway,和端到端示例**同构**,只是多了证据引用。**这是本模块的默认路径。**
- **要账号系统 / 多个 agent / 存历史对话** → 参考 **Agent Leo**(Supabase + 多 agent)。**进阶,非必学**——先把前两档做扎实。

## 文件导览

```
端到端示例_考前3分钟/     ★最小可运行骨架(后端 FastAPI 包 mini CC harness + 静态前端),从 PRD 到公网 URL
小智_架构与部署.md         入门档:静态导出 + 优雅降级 + 化名记忆
HEAI_架构与部署.md         中档:Vanilla 前端 + FastAPI + 强制引用(= 默认路径完整样板)
AgentLeo_架构与部署.md      进阶档:Next.js 全栈 + Supabase + 多 agent(参考,非必学)
```

---
*MIT License｜郑先隽,北京师范大学心理学部教授,人本AI设计与创新*
