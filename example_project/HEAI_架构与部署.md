# HEAI / renben.ai —— 架构与部署(🟡 中档,= 本模块默认路径样板)

> **看颗粒度,别照抄。** HEAI(Human Experience of AI)研究"人如何心理体验 AI"。它的技术栈**和本模块教你的默认路径几乎一模一样**:手写静态前端 + Python FastAPI 后端 + Railway。你把端到端示例读懂,再看它,就懂"加一点东西能长成什么样"。**大多数组学这一档。**

## 一句话架构
**Vanilla 前端(手写 HTML + 图表)+ Python FastAPI 后端(带证据引用)+ Docker/Railway。** 和你的端到端示例**同构**,只多了"强制引用"。

## 前端:Vanilla HTML + D3.js(不用框架)
- 就是几个手写的 `.html` 页面(`index / explorer / agent-chat / methodology / about`)+ **D3.js v7** 画数据图(树图/散点/热力图)。
- 数据是一个 Python 预先生成的 `data.json`,前端直接读。
- 白话:**不用 React/Next 也能做出正经网页**。你的项目如果就是"一个聊天页 + 几张图",手写 HTML 反而最省心、最好部署(和端到端示例的 `index.html` 一样)。

## ★ 后端:Python FastAPI(和你学的 Python 一脉相承)
- 核心文件 `server/main.py`(FastAPI 应用)+ `server/agents.py`(agent 逻辑),就百来行。
- 接口很干净:`GET /api/health`(健康检查)、`GET /api/agents`(列 agent)、`POST /api/agents/chat`(对话)。**和你端到端示例的 `/api/chat`、`/api/health` 是同一个套路。**
- 每个 agent = 一个 `SKILL.md`(人设)+ 一个 `evidence.json`(证据包)。请求来了,`agents.py` 里:
  - `retrieve(...)`:从证据里检索相关几条(轻量 RAG);
  - `build_system_prompt(...)`:把证据塞进系统提示;
  - `extract_citations(...)`:把回答里的 `[id]` 映射回真实出处。
- 模型:主用 Claude Sonnet,备用 Gemini(via OpenRouter)——**和你一样,key 走后端 env**(`ANTHROPIC_API_KEY` / `OPENROUTER_API_KEY`),前端永远看不到。

## ★ 最亮的一招:强制引用 grounding(反幻觉)
- agent **被要求每个说法都带 `[id]` 引用**,后端再拿 `[id]` 去校验 `citation_index`——**编造的出处会被拦下**。
- 引用的原文是**改写过的**(不逐字照抄),既保真又不侵权;作者用**稳定化名**(保护隐私)。
- 为什么重要:心理/教育场景最怕"一本正经地胡说"。**让 AI 的每句话都能追到证据**,是把"看起来可信"变成"真的可信"的工程手段。呼应 1_DEFINE 的"证据链"。
- **你能借鉴**:如果你的 agent 会给"建议/事实"(如科普、量表解读),让它**只能从你给的资料里引用**,并在前端显示出处——比放任它自由发挥安全得多。

## 部署:Docker + Railway
- `Dockerfile`:`python3.12-slim` 基础镜像,装依赖,启动 `uvicorn server.main:app --host 0.0.0.0 --port $PORT`。
- Railway:Nixpacks 自动识别 Python;`/api/health` 做健康检查;key 填在 Railway 的 Variables。
- 白话:**这就是你在 `SHIP/S2` 要做的事**——把 FastAPI 推上 Railway,填 key,拿网址。HEAI 只是加了个 Docker(可选,Railway 不用 Docker 也能跑 Python)。

## 给你的三条可迁移经验
1. **不用框架也能上线**:手写 HTML 前端 + FastAPI 后端,是零基础最短路径(= 端到端示例)。
2. **让输出可信**:会给建议/事实的 agent,用"只能引用给定资料 + 显示出处"来防幻觉。
3. **接口保持干净**:`/api/health` + `/api/chat`,前端只认这两个,后端怎么变都不影响前端。

---
*MIT License｜郑先隽,北京师范大学心理学部教授,人本AI设计与创新*
