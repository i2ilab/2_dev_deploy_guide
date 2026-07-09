# 教程 · 从 harness 到上线(一条故事线走完 Build + Ship)

> 这篇把 `2_dev_deploy_guide` 的两根支柱串成一个故事:拿「考前 3 分钟」这个心理陪伴 agent,从你**已经造好的 mini CC harness**,一路走到**同学用手机就能打开的公网网址**。
> 全程一句话:**你是导演,不是码农。** 代码交给 Claude Code 写,你负责三件事——看懂架构、守住 key 安全、把危机红线钉死。
> 每一节都指向对应的 `BUILD/B*`、`SHIP/S*` 阶段文件、模板,以及真能跑的样板 `example_project/端到端示例_考前3分钟/`。

---

## 第 0 幕:你手里已经有什么

四天下来,你其实已经攒齐了做一个真产品的所有零件,只是还没拼起来:

- **对话内核**:`1_claude_code_basic` 里你亲手造的 mini CC harness(`c0`→`c5`)——JSON 协议、工具箱、TodoWrite、子 agent、上下文压缩、权限门。**这就是后端的大脑。**
- **产品定义**:`1_DEFINE_guide` 里你产出的 PRD(T4)、人设、危机红线、E4 自检环。**这就是要装进大脑的灵魂。**
- **一个 key**:`0_agent_basic/.env` 里的 `OPENROUTER_API_KEY`。**这就是发动机的油——但它只能待在后端。**

这个模块不教你造新零件,只教你**把零件拼成一个能上线的东西**。拼装分两半:**Build(做出来)** 和 **Ship(送上线)**。

> 📖 详见 `BUILD/B0_总览_你是导演不是码农.md`——那里有一张关键的表:harness 的五根支柱,分别对应上线后要用到的五个真实能力。

---

## 第一幕 · Build:把 harness 变成一个能被网页调用的后端

### 1.1 先把灵魂装进大脑(B1)

打开 Claude Code,在你的项目目录里,让它帮你把 PRD 翻译成三样东西(**别自己写,让它写,你来审**):

- `agent.md`——你的 agent 是谁、语气怎样、**绝不做什么**(硬边界)。参照样板 `backend/agent.md` 的三段式(身份/语气/边界)。
- 一批 `skill_*.md`——每个工作流环节一个。比如「考前 3 分钟」就有 `skill_正念.md`。
- **`skill_危机转介.md`——必备,而且拼接时永远排最前。** 这是你的一票否决红线。

然后,以 `1_claude_code_basic/c5_guard.py` 为底座,把这些 skill 装上去:要能查资料/记笔记就用 `c1` 工具箱;要独立审一遍"这条回复安不安全"就开 `c3` 子 agent(**这正是 1_DEFINE 的 E4 自检环,现在变成后端的一层护栏**);对话长了要不爆 token 就用 `c4` 压缩。

> 📖 `BUILD/B1_装配后端agent.md` + skill `/build-backend`。

### 1.2 把交互循环搬成一个接口(B2)

你的 harness 现在还是 `while True: input()`——只能在你自己的终端里跑。上线要的是一个**网页能调用的接口**。让 Claude Code 做这个改造:

> "把这个 harness 包成一个 FastAPI 服务,开一个 `POST /api/chat`:前端会传 `{messages:[...]}`,你跑一轮 harness,把最终回复作为 `{reply, meta}` 返回。key 从 `os.environ` 读。加 `/api/health`、CORS、以及调不通模型时的兜底(别返回 500)。"

三个**你必须亲自把关**的点:

1. **key 走环境变量**,绝不写死在代码里(样板:`os.getenv("OPENROUTER_API_KEY")`)。
2. **去掉 bash,只留白名单工具**。终端里给 agent `bash` 没问题(是你自己);但公网上给所有用户 `bash` = 灾难。这就是 `c5` 权限门在服务端的正确形态:一张安全工具的白名单,`save_journal` 这种可以,`rm` 这种永远不行。
3. **危机拦截用确定性代码兜底**。看样板 `main.py` 的 `is_crisis()`:它在**入口和出口各拦一次**,一命中危机关键词,直接返回转介话术,**根本不问模型**。为什么?因为模型可能失手,但代码不能失守——这就是「安全一票否决」在工程上的样子。

跑一下验证(不填 key 也能验危机拦截):
```bash
cd backend && pip install -r requirements.txt && uvicorn main:app --reload --port 8000
curl -X POST localhost:8000/api/chat -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"我撑不下去了"}]}'   # → 必须返回危机转介
```

> 📖 `BUILD/B2_后端服务化.md`。样板就是 `backend/main.py`,读它比读十页文档管用。产出:填 `templates/技术架构卡.md` + `templates/API契约卡.md`。

### 1.3 给它一张脸(B3)

后端有了,但它还没法给人用——没人会用 curl。让 Claude Code 生成一个聊天前端,记住**三句话**:

1. 做什么页:一个单页聊天界面,调后端 `POST /api/chat`,回复显示成气泡。
2. 什么风格:贴你的项目——心理陪伴就温暖圆角,评估工具就专业极简。
3. 连哪个后端:后端地址放一个变量 `BACKEND`,本地 `localhost:8000`,上线改成部署域名。

再加两条心理/教育项目的必备:**一个醒目的「危机求助」按钮**;**优雅降级**——后端连不上时,`catch` 里给一句兜底 + 热线,**绝不白屏**(这是小智 `CompositeProvider` 的思想:AI 不可用,产品也要稳住)。

> ⚠️ 全程最重要的一条:**前端是公开的**。任何人右键"查看源代码"就能看到里面所有东西。所以 **key 绝对不能进前端**,前端只认识后端的 `/api/chat`。
>
> 📖 `BUILD/B3_前端界面.md` + `/build-frontend`。样板:`frontend/index.html`。

### 1.4 在本地接起来,过安全关(B4)

两个都起来(后端 `uvicorn`,前端 `python3 -m http.server 5500`),让前端 `BACKEND` 指向 `localhost:8000`,发一句话,通了。

如果控制台报 **CORS** 错误(最常见的"连不上")——那是浏览器的跨域保护,让 Claude Code 确认后端加了 `CORSMiddleware`,本地先 `*` 跑通。

然后跑本地安全自检(这一关不过,不许上线):
```bash
grep -rniE "sk-[a-z0-9]{16}" frontend/     # 前端无 key —— 必须为零
```
危机测试(发"我不想活了"→ 显示转介?)、降级测试(关掉后端 → 兜底还是白屏?)、手机测。

> 📖 `BUILD/B4_连通与安全自检.md` + `/build-connect`。门禁:`checklists/前端安全清单.md` + `后端自检清单.md`。

---

## 第二幕 · Ship:让世界用到它

一句话:**不上线 = 没有 impact。** 你的 agent 再好,躺在你电脑里,影响力是零。

### 2.1 静态还是动态?(S0)

- 只有展示页/作品集(不真调模型)→ **静态**:GitHub Pages(免费最简单)。
- 要真对话(调模型)→ **动态**:前端 + 一个后端。前端可以照样放 GitHub Pages,**后端放 Railway**。

三平台定位:**GitHub Pages = 静态前端(免费)**;**Railway = Python 后端(默认,对 FastAPI 友好,三个真实项目同款)**;**Vercel = 免费替代**(Node serverless)。成本要透明:Pages/Vercel 免费,Railway ~$5 试用/hobby(非永久免费)。

> 📖 `SHIP/S0_总览_不上线就没有impact.md` + `templates/部署选型决策卡.md` + `checklists/部署平台对照表.md`。

### 2.2 前端上线:GitHub Pages(S1)

把前端 push 到 GitHub → 仓库 Settings → Pages → 选分支 → 拿到 `https://用户名.github.io/仓库名/`。上线前必须 `grep sk-` 为零、`.env` 在 `.gitignore`。

> 📖 `SHIP/S1_静态展示上线_GitHubPages.md` + `/ship-static`。

### 2.3 后端上线:Railway(S2)

push 到 GitHub → Railway New Project → Deploy from GitHub repo → 若后端在子目录设 Root Directory → **Variables 里填 `OPENROUTER_API_KEY`(key 只在这里!)** → 启动命令 `uvicorn main:app --host 0.0.0.0 --port $PORT` → 打开 `/api/health` 应返回 ok。

不想付费?用 Vercel serverless(`api/chat`)代替,环境变量里放 key。Python 顺手优先 Railway,零成本优先 Vercel。

> 📖 `SHIP/S2_后端上线_Railway.md` + `/ship-backend` + `templates/密钥环境变量清单.md`。

### 2.4 接起来 + 上线检查 + 结项(S3–S4)

前端 `BACKEND` 改成 Railway 域名;后端 `CORS_ORIGINS` 填 Pages 域名(否则跨域被拦)。**用手机打开线上网址**——这才是真实用户的入口。

跑完整上线检查清单(`templates/上线检查清单.md`):前端无 key、git 历史无泄漏、网址手机能开、AI 身份披露 + 隐私说明、**危机热线号码对(12356 / 010-82951332)**、优雅降级、README 三要素。

最后,填 `templates/结项技术文档.md`(架构图 + 部署说明 + 复现步骤),对齐 `2_hcai_guide` 的 T8 第 4 节。

> 📖 `SHIP/S3_前端接后端_整体上线.md` + `S4_上线检查与结项.md` + `/ship-golive`。

---

## 收尾:你到底学会了什么

你没有变成一个前端工程师,也没变成运维——你学会的是**把一个想法,变成一个别人真能用、且不会伤害人的东西**:

- **架构感**:前端 / 后端 / 模型三层,数据怎么流,key 藏哪。
- **安全底线**:key 绝不进前端;危机由确定性代码兜底;调不通要优雅降级。
- **上线能力**:静态上 Pages,后端上 Railway,手机能打开。

把网址发到群里的那一刻——**这就是你的 impact 的起点。**

对照三档真实架构继续深挖:`example_project/小智_架构与部署.md`(静态+离线兜底)/ `HEAI_架构与部署.md`(FastAPI,和你走的默认路径几乎一样)/ `AgentLeo_架构与部署.md`(全栈+多 agent)。

---
*MIT License｜郑先隽,北京师范大学心理学部教授,人本AI设计与创新*
