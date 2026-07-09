# 前端 · 考前 3 分钟(纯静态单页)

一个 `index.html` 就是全部——没有构建、没有框架、**没有任何 key**。它只做一件事:把用户的话 POST 给后端 `/api/chat`,把回复显示成气泡。

## 本地看
直接双击 `index.html`,或:
```bash
cd frontend && python3 -m http.server 5500   # 打开 http://localhost:5500
```
本地时它会自动连 `http://localhost:8000`(先把后端跑起来)。

## 部署到 GitHub Pages(免费)
1. 把前端 push 到 GitHub 仓库(可以和后端同仓不同目录)。
2. 仓库 Settings → Pages → Source 选分支 + `/frontend`(或把 index.html 放根目录)。
3. 拿到 `https://你的用户名.github.io/仓库名/` 网址。
4. **改一行**:把 `index.html` 里的 `BACKEND` 线上分支改成你的 Railway 域名:
   ```js
   : "https://你的后端.up.railway.app";
   ```
5. 记得在后端 Railway 的 `CORS_ORIGINS` 填上这个 Pages 域名(否则浏览器会拦跨域请求)。

## 安全铁律(上线前 `grep` 一遍)
```bash
grep -rniE "sk-[a-z0-9]{16}|openrouter.*key" .   # 前端目录必须为零
```
前端是公开的,任何人都能看源码。**key 只能待在后端。** 前端只认识后端的 `/api/chat`。

## 优雅降级
后端连不上时,前端不会白屏——它给一句兜底 + 危机热线(见 `index.html` 的 `catch`)。这是小智 `CompositeProvider` 的思想:AI 不可用时,产品要稳住,不能崩在用户脸上。
