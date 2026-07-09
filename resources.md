# 资源库 —— 按「什么时候查」组织

> 不用一次读完。**卡在哪一步,就翻哪一节。** 每条先说"什么时候用得上",再给链接。
> 每个技术名词都配一句白话——你是心理/教育背景,不必懂原理,够用就行。

---

## 一、装配后端时查(B1–B2)

- **`1_claude_code_basic/c0–c5`(你自己的 harness)** — *什么时候*:写后端对话内核时,直接以 `c5_guard.py` 为底。白话:你上周亲手造的 mini Claude Code,就是后端的大脑,不用重造。
- **`0_agent_basic/s5_agent_skill.py`** — *什么时候*:想看最小起点(agent.md + skill 怎么拼系统提示)。白话:31 行的极简版,理解"人设+技能=系统提示"。
- **OpenRouter 文档** https://openrouter.ai/docs — *什么时候*:调模型、查模型名(如 `anthropic/claude-haiku-4-5-20251001`)、看接口格式。白话:一个 key 通很多模型的中转站,你已经有 key 了。
- **FastAPI 快速开始** https://fastapi.tiangolo.com/zh/ — *什么时候*:把 harness 包成 `/api/chat` 时。白话:Python 写 Web 接口最省心的库,官方中文文档很友好。
- **Pydantic**(FastAPI 自带) https://docs.pydantic.dev/ — *什么时候*:定义接口收什么(如 `messages`)。白话:帮你检查"前端发来的数据格式对不对"。
- **端到端示例** `example_project/端到端示例_考前3分钟/backend/main.py` — *什么时候*:任何时候。白话:抄这个结构(run_harness / is_crisis / safety_review / FALLBACK)就对了。

## 二、做前端时查(B3–B4)

- **让 Claude Code 生成聊天界面** — *什么时候*:B3 做前端。白话:用三句话(做什么页/什么风格/连哪个后端)让 Claude Code 写 `index.html`,你不用手写。参考 `templates/前端提示词卡.md`。
- **fetch / 调后端** MDN https://developer.mozilla.org/zh-CN/docs/Web/API/Fetch_API — *什么时候*:前端要把消息发给后端时。白话:浏览器里"给后端打电话"的标准方法(示例 `index.html` 里就一句 `fetch(BACKEND+"/api/chat")`)。
- **CORS 跨域** MDN https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CORS — *什么时候*:前端调后端报"被 CORS 拦了"时。白话:浏览器的安全规则——后端要"允许"你的前端域名(在后端设 `CORS_ORIGINS`)。
- **优雅降级思想** 见 `example_project/小智_架构与部署.md` — *什么时候*:担心 AI 连不上白屏时。白话:`catch` 里给兜底话术 + 热线,别把报错甩给用户。

## 三、部署时查(S1–S3)

- **GitHub Pages** https://docs.github.com/zh/pages — *什么时候*:上线纯静态前端/展示页。白话:免费,把 HTML 推上 GitHub,开个开关就有网址。
- **Railway** https://docs.railway.app/ — *什么时候*:上线 Python FastAPI 后端(默认路径)。白话:连 GitHub 自动识别 Python、自动部署;key 填在 Variables 里。成本:非永久免费(~$5 试用/hobby)。
- **Railway 环境变量** https://docs.railway.app/guides/variables — *什么时候*:放 `OPENROUTER_API_KEY` 等。白话:key 只能待在这里,绝不进代码/前端。
- **Vercel**(免费替代) https://vercel.com/docs — *什么时候*:想零成本、或做 Node serverless。白话:前端一键上线免费;跑 Python 比 Railway 麻烦,能省钱但更折腾。
- **腾讯云静态托管 / 云函数** https://cloud.tencent.com/document/product/1103 — *什么时候*:要长期给**国内用户**用、GitHub/Vercel 访问不稳时。白话:国内访问快,但要实名 + 少量费用。

## 四、排错时查(哪一步都可能用)

- **key 泄漏自查** — *什么时候*:上线前必做。命令:`grep -rniE "sk-[a-z0-9]{16}" 前端目录`,**结果必须为零**。白话:前端是公开的,有 key 就会被盗刷。
- **健康检查** — *什么时候*:后端部署后。访问 `你的后端/api/health`,应返回 `{"status":"ok"}`。白话:确认后端"活着"再连前端。
- **手机跨设备测** — *什么时候*:上线后。白话:很多用户用手机,一定在手机上打开你的公网 URL 试一遍(别只在自己电脑上看)。
- **CORS 报错**(前端控制台红字 "blocked by CORS") — 回第一节 CORS 条:后端 `CORS_ORIGINS` 填上你的前端域名。

---

## 真实项目 repo(想深挖时)

- 小智 / Reading Bot:`/Users/samzheng/Documents/2_AI_Projects/0_AI+UX/AI_Teaching/reading-bot/`(静态导出 + 优雅降级)
- HEAI / renben.ai:`/Users/samzheng/Documents/2_AI_Projects/0_AI+UX/AI_Impact_Index/Impact_index/`(FastAPI + 强制引用,= 默认路径样板)
- Agent Leo / deepsy.ai:`/Users/samzheng/Documents/2_AI_Projects/0_AI+UX/AI_Products/agent_leo/`(Next.js 全栈 + Supabase + 多 agent)
- ★ 能跑的最小样板:`example_project/端到端示例_考前3分钟/`

---
*MIT License｜郑先隽,北京师范大学心理学部教授,人本AI设计与创新*
