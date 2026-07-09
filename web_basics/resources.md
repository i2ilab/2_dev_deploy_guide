# web 学习资源(按「什么时候查」组织)

> 不用从头学一遍 web 开发。**遇到卡点,按下面的场景找对应资源查一下就行。** 定位仍是「看懂 + 会指挥」。
> 最好的活教材,是你自己的运行示例:`example_project/端到端示例_考前3分钟/frontend/index.html`(前端三件套全在里面)+ `backend/main.py`(FastAPI 后端全貌)。配套导览 slides:`slides/web_basics_数据叙事风.pptx`。

---

## 🤖 AI 时代:先认识你的"施工队"

开发早已是 **AI-first**:AI 生成代码,你审阅 + 指挥。2026 年约 90% 专业开发者每天用 AI 编程工具。认得这几个就够:

| 工具 | 是什么 | 什么时候用 | 链接 |
|---|---|---|---|
| **Claude Code**(本课主线) | 终端里的智能体,读你的代码库、改文件、跑命令 | 全程主力:让它按你的 PRD 造前端/后端、部署 | https://www.claude.com/product/claude-code |
| **Cursor** | AI 优先的代码编辑器(IDE) | 想要图形界面 + 多文件重构 | https://cursor.com |
| **v0**(Vercel) | 一句话生成前端界面(React/Tailwind) | 快速出一个好看的 UI 原型 | https://v0.app |
| **bolt.new** | 浏览器里全栈生成 + 预览 | 不想装环境,浏览器里试想法 | https://bolt.new |
| **Lovable** | 自然语言全栈建站(React+Supabase) | 想要带账号/数据库的完整应用 | https://lovable.dev |

> 记住:**它们生成,你审阅**。看懂它写了什么、守住 key 安全、判断对不对——这是 AI 替不了你的地方。

## 想搞懂前端(HTML / CSS / JS)时

- **MDN Web Docs** — 全世界最权威的 web 技术字典(HTML/CSS/JS/HTTP 全都有,中文可切换)。遇到任何标签/属性/函数不懂,直接搜。 https://developer.mozilla.org
- **MDN · 学习 web 开发** — 零基础系统入门路径。 https://developer.mozilla.org/zh-CN/docs/Learn_web_development
- **javascript.info** — 讲得最清楚的现代 JavaScript 教程。想真正弄懂 JS(变量/函数/事件/fetch)时看。 https://javascript.info
- **web.dev**(Google) — 现代 web 最佳实践(性能、可访问性)。想让页面更快更好时查。 https://web.dev

## 想搞懂框架(React / Next.js)时

- **react.dev** — React 官方文档 + 交互式教程。想弄懂"组件/props/state"时看官方 Quick Start。 https://react.dev/learn
- **Next.js Learn** — 官方手把手全栈教程(边做边学一个应用)。要用 Next.js 时的最佳起点(2026 最新 Next.js 16 / React 19)。 https://nextjs.org/learn
- **Next.js 文档** — App Router、Server Components 参考。 https://nextjs.org/docs
- 判断"要不要框架":先看你项目——一两个页面用纯 HTML;要账号/很多页面/复杂状态再上 Next.js(参考 `example_project/AgentLeo_架构与部署.md`)。

## 想搞懂后端与 API 时

- **FastAPI 官方教程** — 从零到一个 Python API,示例清晰、自带交互文档。你的 `backend/main.py` 就是这套。 https://fastapi.tiangolo.com
- **MDN · HTTP** — 搞懂请求/响应/状态码(200/404/500)/方法(GET/POST)。 https://developer.mozilla.org/zh-CN/docs/Web/HTTP
- **MDN · Fetch API** — 前端怎么调后端。 https://developer.mozilla.org/zh-CN/docs/Web/API/Fetch_API
- 回看模块内:`BUILD/B2_后端服务化.md`(harness→FastAPI)、`example_project/HEAI_架构与部署.md`(FastAPI 真实项目)。

## 部署与工具时

- **GitHub Pages 官方文档** — 免费托管静态前端。 https://docs.github.com/pages
- **Railway 文档** — Python 后端默认部署(Nixpacks 自动识别 + Variables 放 key)。 https://docs.railway.com
- **Railway 快速上手** — https://docs.railway.com/quick-start
- **Vercel 文档** — 免费替代(前端/Node serverless)。 https://vercel.com/docs
- **Git / GitHub 入门** — 代码存档与协作。 https://docs.github.com/get-started
- 回看模块内:`SHIP/S1_静态展示上线_GitHubPages.md`、`SHIP/S2_后端上线_Railway.md`、`checklists/部署平台对照表.md`。

## 报错排查时(先别慌)

- **先按 F12 开 DevTools**:Console 看红字报错、Network 看哪个请求失败(200/404/500?)。把红字**截图发给 Claude Code**,说清"哪一层、什么错"。
- **CORS 报错** → 后端没放行前端域名。查:MDN · CORS https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CORS ;改后端 `CORS_ORIGINS`。
- **404** → 前端 fetch 的 URL 写错,或后端端点不存在。
- **500** → 后端内部崩了,去 Railway 看后端日志找异常。
- **前端白屏** → 多半是 JS 报错(看 Console)或后端没连上(看 Network)。
- 术语不认得 → 回 `术语速查_web_cheatsheet.md` 扫一眼。

## 想再深入(选学,有余力再看)

- **freeCodeCamp** — 免费系统课(前端/后端/全栈),想动手多练时。 https://www.freecodecamp.org
- **The Odin Project** — 完整全栈自学路线。 https://www.theodinproject.com
- **roadmap.sh** — web 开发学习路线图(看清全貌)。 https://roadmap.sh/frontend

---

*MIT License｜郑先隽,北京师范大学心理学部教授,人本AI设计与创新*
