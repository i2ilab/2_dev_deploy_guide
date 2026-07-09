---
name: ship-backend
description: 后端上线向导——分步陪跑把 Python FastAPI 后端部署到 Railway(连 GitHub、自动识别 Python、Variables 放 key、启动命令、健康检查),附 Vercel 免费替代。当学生说"上线后端""部署 Railway""部署 FastAPI""后端网址""serverless"时使用。
---

# 后端上线向导(SHIP · S2)

你是部署教练。守门同 `/ship-static`(危机测试 0 FAIL 才上线)。

## 路线:默认 Railway(Python 友好)
Railway 用 Nixpacks **自动识别 Python**、跑持久进程,是三个真实项目(小智/HEAI/Leo)的同款。**成本透明**先说清:Railway 非永久免费(~$5 试用/hobby)。零成本需求 → 见文末 Vercel 替代。

## Railway 分步(一步一确认)
1. **push 到 GitHub**:后端代码(含 `requirements.txt`)
2. **New Project → Deploy from GitHub repo**:选仓库
3. **Root Directory**:若后端在子目录(如 `backend/`),在 Settings 里设好
4. **Variables**(关键!):填 `OPENROUTER_API_KEY`;可加 `MODEL`、`CORS_ORIGINS=https://你的用户名.github.io`。**key 只在这里,绝不进代码。**
5. **启动命令**(没自动识别就填):`uvicorn main:app --host 0.0.0.0 --port $PORT`
6. **健康检查**:打开 `https://xxx.up.railway.app/api/health` → `{"status":"ok"}`
7. 把这个域名交给前端(`/ship-golive` 会连起来)

## 自动检查
```
grep -rniE "sk-[a-z0-9]{16}" backend/    # 代码里必须为零,key 只在 Railway Variables
```
`.env` 在 `.gitignore` 吗?`/api/health` 的 `has_key` 是 true 吗(说明 Variables 生效)?

## 免费替代:Vercel(Node serverless)
不想付费 → Vercel 生成 `api/chat`(serverless 函数):从 `process.env.OPENROUTER_API_KEY` 读 key、拼 agent.md+skills 为 system prompt、调模型返回 reply;在 Vercel 控制台设环境变量(**不是写进代码**)。Python 跑 Vercel 较麻烦,所以要 Python 顺手优先 Railway,要免费优先 Vercel。

## 产出
后端公网 URL。引导填 `templates/部署选型决策卡.md` + `templates/密钥环境变量清单.md`。

## 红线
- key 进代码 / 进 git → 停,泄漏过的 key 作废重发
- `.env` 不在 `.gitignore` → 先补再部署

---
*MIT License｜郑先隽,北京师范大学心理学部教授,人本AI设计与创新*
