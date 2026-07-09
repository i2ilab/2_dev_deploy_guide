# 后端 · 考前 3 分钟(FastAPI 包 mini CC harness)

这是把你在 `1_claude_code_basic` 造的 mini Claude Code harness **搬上线**的最小样板。核心逻辑就三步:
1. `while True: input()` 交互循环 → 无状态 `POST /api/chat`(前端传 `messages`,后端跑一轮 harness)
2. key 从 `os.environ` 读(**绝不进前端、绝不进 git**)
3. 去掉危险的 `bash` 工具,只留白名单安全工具(`save_journal`)——这就是 c5 权限门在服务端该有的样子

harness 五支柱 → 上线能力的对应,见模块根 `README.md`。安全一票否决(危机拦截)由 **确定性代码** `is_crisis()` 在入口/出口各兜一次,不只靠模型自觉。

## 本地跑

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate     # 可选,建议
pip install -r requirements.txt
cp .env.example .env        # 然后把 .env 里的 OPENROUTER_API_KEY 换成你自己的
uvicorn main:app --reload --port 8000
```

自测(不填 key 也能验证危机拦截):
```bash
curl localhost:8000/api/health
curl -X POST localhost:8000/api/chat -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"我撑不下去了"}]}'   # → 返回危机转介
```

## 部署到 Railway(默认路径,Python 友好)

1. 把这个仓库 push 到 GitHub。
2. Railway → New Project → Deploy from GitHub repo,选你的仓库。
3. Root Directory 设为 `backend`(若后端在子目录)。Railway 用 Nixpacks **自动识别 Python**,`requirements.txt` 自动装。
4. Settings → **Variables** 填 `OPENROUTER_API_KEY`(和 `CORS_ORIGINS=https://你的用户名.github.io`)。**key 只在这里,不进代码。**
5. 起动命令(若没自动识别):`uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Railway 给你一个 `https://xxx.up.railway.app` 域名 → 填进前端的 `BACKEND`。
7. 健康检查:访问 `/api/health` 应返回 `{"status":"ok"}`。

> 成本:Railway 非永久免费(~$5 试用/hobby)。想零成本 → 用 Vercel Node serverless(见模块 `SHIP/S2`),或后端也放 Vercel Python function。

## 免费替代:Vercel
Vercel 原生是 Node serverless;跑 Python 需要 `api/` 函数或 `vercel.json` 配置,比 Railway 麻烦。零成本演示可用;要 Python 顺手,优先 Railway。
