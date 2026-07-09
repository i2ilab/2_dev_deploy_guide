# S2 · 后端上线 —— FastAPI → Railway(默认)

> **目标**:把你的 Python 后端(FastAPI,包着 mini CC harness)部署到 Railway,拿到一个公网 API 地址,key 安全地放在平台 env 里。
> **前置输入**:本地能跑的后端(BUILD/B2,或运行示例 `example_project/端到端示例_考前3分钟/backend/`)。
> **产出物**:一个 `https://xxx.up.railway.app` 后端网址,`/api/health` 返回 ok。
> **配套 skill**:`/ship-backend`

## 先打个气:Railway 会替你搞定"环境"

零基础学生最怕"配环境"。好消息:**Railway 用 Nixpacks 自动识别 Python**——它看到 `requirements.txt` 就自动装依赖、自动跑起来。你几乎不用碰命令行。三个真实项目(小智 / HEAI / Agent Leo)都用 Railway。

## 新想法:后端 = 一台一直开着、藏着 key 的电脑

前端(GitHub Pages)是公开的,谁都能看源码;所以 **key 绝不能放前端**。后端不一样——它是一台**只有你能配置**的服务器,key 放在它的"环境变量(Variables)"里,前端只通过 `/api/chat` 和它说话,永远看不到 key。这就是"后端代理 key",是所有真实 AI 产品的铁律。

## 操作步骤(Railway,分步)

1. **push 到 GitHub**:确保后端代码(含 `main.py`、`requirements.txt`)在一个 GitHub 仓库里。**`.env` 必须在 `.gitignore` 里,绝不提交。**
2. **建项目**:登录 [railway.app](https://railway.app) → **New Project** → **Deploy from GitHub repo** → 选你的仓库。
3. **设根目录**(若后端在子目录):Service → Settings → **Root Directory** 填 `backend`(或你的后端目录)。
4. **等它自动构建**:Railway 识别到 Python + `requirements.txt`,自动 `pip install`。看 Deploy 日志。
5. **填环境变量**:Service → **Variables** → 添加:
   - `OPENROUTER_API_KEY` = 你的 key ← **只在这里,不进代码**
   - `CORS_ORIGINS` = `https://你的用户名.github.io`(前端域名)
   - (可选)`MODEL` = `anthropic/claude-haiku-4-5-20251001`
6. **设启动命令**(若没自动识别):Settings → **Start Command** 填
   `uvicorn main:app --host 0.0.0.0 --port $PORT`
   (`$PORT` 是 Railway 注入的端口,必须用它,别写死 8000。)
7. **拿域名**:Settings → **Networking → Generate Domain**,得到 `https://xxx.up.railway.app`。
8. **验证成功**:浏览器打开 `https://xxx.up.railway.app/api/health`,返回 `{"status":"ok",...}` = 后端活了。

## 💰 成本说明(要如实告诉小组)

Railway **不是永久免费**:有约 $5 的试用额度 / hobby 计划起步价。对课程 demo(用量很小)通常够用。**想零成本 → 看下面的 Vercel 备选。**

## 附:免费替代 —— Vercel(Node serverless)

Vercel 有慷慨的免费额度,但原生是 **Node.js serverless**。两条路:
- **前端 + 一个 Node 后端函数**:让 Claude Code 生成 `api/chat.js`(读 `process.env.OPENROUTER_API_KEY`、拼系统提示、调模型、返回回复),整个仓库一键部署到 Vercel。**这是纯免费、一个仓库到一个网址的最省钱路径。**
- **Python on Vercel**:Vercel 也支持 Python 函数,但要放进 `api/` 并加配置,比 Railway 麻烦。**要 Python 顺手 → 用 Railway;要免费 → 用 Vercel Node。**

## 痛点对比

| 😌 简单·看不出必要 | 「我把 key 写进代码,反正只有我用」——一旦 push 到 GitHub,key 就公开了,几小时内就会被爬走盗刷,账单爆炸 |
| 🔥 复杂·痛点凸显 | 上线=真的公开;key 只能进平台 Variables。运行示例的 `main.py` 用 `os.getenv("OPENROUTER_API_KEY")` 读 env,就是为了让你能安全上线 |

## 门禁检查(过了才进 S3)

- [ ] `/api/health` 公网可访问、返回 ok
- [ ] key 在 Railway Variables 里,**代码/仓库里搜 `sk-` 为零**
- [ ] `.env` 在 `.gitignore`,`git log -p | grep sk-` 无结果
- [ ] `CORS_ORIGINS` 填了你的前端域名

## 思考题

> 你的前端和后端现在各有一个网址,但它们还没连起来。
> 浏览器有个"同源安全"规则会挡住跨域请求——下一步 S3,我们用 CORS 让它俩握上手。

---
*MIT License｜郑先隽,北京师范大学心理学部教授,人本AI设计与创新*
