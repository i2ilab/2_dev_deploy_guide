# API 契约卡（配合 BUILD/B2）

> **怎么用**:记下你后端接口"长什么样"——前端照这个调,部署时照这个填环境变量。契约稳定,前后端才不会互相扯皮。【】里按你的项目填。

## 接口 1:对话
```
POST /api/chat
请求体:{ "messages": [ {"role":"user","content":"..."}, {"role":"assistant","content":"..."} ] }
返回体:{ "reply": "给用户看的话", "meta": { "crisis": true/false } }
```
说明:**无状态**——历史由前端每次带全。后端跑一轮 harness 返回一句 reply。

## 接口 2:健康检查
```
GET /api/health  →  { "status": "ok", "model": "...", "has_key": true }
```
部署平台用它判断服务活没活。

## 需要的环境变量（放平台 Variables,不进代码）
| 变量 | 作用 | 示例 |
|---|---|---|
| `OPENROUTER_API_KEY` | 模型 key（**只在后端**） | 【你的 key】 |
| `MODEL` | 用哪个模型 | anthropic/claude-haiku-4-5-20251001 |
| `CORS_ORIGINS` | 允许哪个前端域名跨域 | https://【你的用户名】.github.io |

## 优雅降级约定
- 模型调不通 → 返回 `FALLBACK` 兜底话,**HTTP 仍是 200,不 500**。
- 危机输入 → 入口/出口各拦一次,直接返回转介话术。

---
*MIT License｜郑先隽,北京师范大学心理学部教授,人本AI设计与创新*
