# 端到端示例 · 考前 3 分钟(可运行骨架)

> **看颗粒度,别照抄。** 这是一个**最小但真能跑**的心理陪伴 agent,从 `1_DEFINE_guide` 的 PRD 一路走到"手机能打开的公网应用"。它把三个模块串成一条线:
> - `0/1_claude_code_basic` 的 **harness** → 后端的对话内核
> - `1_DEFINE_guide` 的 **PRD / 危机红线 / E4 自检环** → agent.md + 危机 skill + 子agent复核
> - 本模块的 **Build/Ship** → FastAPI 服务化 + 前端 + 部署

## 架构(= HEAI/renben.ai 的简化版)

```
  用户(手机浏览器)
        │  HTTPS
        ▼
  前端 index.html  ──POST /api/chat──►  后端 FastAPI(main.py)
  纯静态 · 无 key                         │  包着 mini CC harness:
  GitHub Pages                            │   c0 JSON协议 · c1 工具箱(save_journal)
                                          │   c3 子agent安全复核 · c5 白名单权限门
                                          │   + is_crisis() 确定性危机一票拦截
                                          ▼
                                    OpenRouter(key 在后端 env)
                                    部署:Railway
```

## 三个关键设计(都能在代码里指给学生看)

1. **harness 搬上线**(`backend/main.py` 的 `run_harness`):就是 c5 的工具循环,去掉 `input()`、去掉 `bash`,变成一个函数。
2. **安全一票否决**(`is_crisis` + `safety_review`):危机拦截由**确定性代码**兜底(入口 + 出口各一次),不只靠模型自觉——这是 1_DEFINE「安全一票否决」的工程落地。子 agent 复核 = E4 自检环。
3. **优雅降级**(`FALLBACK` + 前端 `catch`):调不通模型不 500、不白屏,给兜底话术 + 热线——小智 CompositeProvider 思想。

## 跑起来

```bash
# 后端
cd backend && pip install -r requirements.txt && cp .env.example .env   # 填你的 OPENROUTER_API_KEY
uvicorn main:app --reload --port 8000
# 前端(另开一个终端)
cd frontend && python3 -m http.server 5500     # 打开 http://localhost:5500
```
不填 key 也能验证**危机拦截**与**优雅降级**(见各自 README)。

## 上线
- 后端 → Railway(`backend/README.md`)
- 前端 → GitHub Pages(`frontend/README.md`),把 `BACKEND` 指向 Railway 域名,后端 `CORS_ORIGINS` 填 Pages 域名。

对照更完整的三档真实架构:`../小智_架构与部署.md` / `../HEAI_架构与部署.md` / `../AgentLeo_架构与部署.md`。

---
*MIT License｜郑先隽,北京师范大学心理学部教授,人本AI设计与创新*
