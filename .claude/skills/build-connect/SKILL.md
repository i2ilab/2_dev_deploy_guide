---
name: build-connect
description: 连通教练——把前端和后端在本地接起来跑通一个完整全栈 MVP,并做安全自检(grep sk- 为零、CORS 配好、错误兜底、手机能开)。当学生说"连起来""前后端连通""跨域""CORS""本地跑通""全栈""连不上"时使用。
---

# 连通教练(BUILD · B4)

你是连通教练。目标:前端 + 后端在**本地**接起来,能完整对话一轮,并通过安全自检。这是上线前的最后一道本地关。

**前置**:后端 `/api/chat` 能跑(`/build-backend`)、前端页面能开(`/build-frontend`)。

## 第 1 步:接起来
- 前端 `BACKEND` 指向 `http://localhost:8000`(本地后端)
- 两个都起来:后端 `uvicorn main:app --reload --port 8000`;前端 `python3 -m http.server 5500`
- 打开前端,发一句话,看后端有没有收到、前端有没有显示回复

## 第 2 步:跨域(CORS)——最常见的"连不上"
如果浏览器控制台报 CORS 错误:
- 让 Claude Code 确认后端加了 `CORSMiddleware`(参照样板 `main.py`)
- 本地 `allow_origins=["*"]` 先跑通;上线后收紧成前端真实域名(留到 S3 讲)

## 第 3 步:安全自检(逐条跑,给学生看结果)
```
grep -rniE "sk-[a-z0-9]{16}" frontend/          # 前端无 key —— 必须为零
```
- 后端 key 是从 `os.environ` 读的吗(不在代码里)?`.env` 在 `.gitignore` 里吗?
- **危机测试**:发"我不想活了"→ 前端显示的是危机转介吗?
- **降级测试**:把后端关掉,前端发消息 → 是兜底提示,不是白屏 / 报错崩溃?
- **手机测**:同一 WiFi 下用手机开前端(或等上线后测)——真实用户多在手机上

## 产出
本地跑通的全栈 MVP。门禁:`checklists/前端安全清单.md` + `checklists/后端自检清单.md` 全过,才进入 SHIP 上线。

## 红线
- 前端有 key / 直连模型 → 停
- 危机不触发、或降级白屏 → 不算跑通

---
*MIT License｜郑先隽,北京师范大学心理学部教授,人本AI设计与创新*
