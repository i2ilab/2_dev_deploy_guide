# web_basics 教程 slides · Fathom 数据叙事风(30 页)

> `2_dev_deploy_guide` 的第二套 deck:**AI 时代 web 技术栈基础**(HTML/CSS/JS、React/Next.js、Node/Python/FastAPI、API、工具链)。与既有 `2_dev_deploy_guide_数据叙事风.pptx` 同源、**共存**(不同文件)。定位=看懂+会指挥。

## 产物
| 文件 | 说明 |
|---|---|
| `web_basics_数据叙事风.pptx` | 30 页,16:9,文字可编辑 |
| `_src/gen_web_basics.py` + `_src/build_web_basics.js` | 生成产线(输出到 `html_web_basics/`,不与既有 deck 冲突) |
| `../web_basics/逐页讲义_web技术栈.md` | 30 页逐页讲义(一一对应) |

## 页面结构(9 章 30 页)
封面 / 02 为什么零基础也要懂web / **W1** 03分节 04请求旅程6步 05客户端vs服务器 06HTTP·静态vs动态 / **W2-W4 前端三件套** 07分节 08盖房子比喻 09HTML 10CSS 11JS 12fetch / **W5** 13分节 14JSON 15API·REST 16状态码 / **W6框架** 17分节 18为什么要框架 19React 20Next.js+三项目选型 / **W7后端** 21分节 22Node vs Python 23FastAPI拆解 24数据与存储 / **W8工具链** 25分节 26终端/npm/git 27DevTools 28看懂报错 29结课清单 / 30金句

**核心装置**:多页用「🤖 Claude Code 帮你做了 / 👁 你要认得」双栏 + 深色代码块(锚运行示例真实代码)。

## 复现 / 修改
```bash
cd _src
python3 gen_web_basics.py            # 生成 html_web_basics/ 30 页
node build_web_basics.js --validate  # 校验 0 溢出
node build_web_basics.js             # 输出 web_basics_数据叙事风.pptx(与既有 deck 共存)
```
设计系统:白底 #FFFFFF · 墨黑 #2B2B2B · 海军蓝 #1A365D · 橙红 #C2410C · 绿/红语义 · 深色代码块 #1E2A38 · 断言式标题。

---
*郑先隽,北师大心理学部｜huashu-slides Path A｜2026-07*
