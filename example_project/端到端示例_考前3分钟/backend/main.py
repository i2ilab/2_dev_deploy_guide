# 端到端示例 · 后端 —— 把你在 1_claude_code_basic 造的 mini CC harness 包成一个 Web 服务
#
# 这不是新东西:核心就是模块 1 的 c5_guard.py(JSON 工具循环 + 工具箱 + 子agent复核 + 权限门),
# 只做三件事把它"搬上线":
#   1) 把 while True: input() 交互循环  →  一个无状态的 /api/chat 接口(前端传 messages,后端跑一轮)
#   2) key 从 os.environ 读(绝不进前端)
#   3) 危险工具(bash)去掉,只留"白名单安全工具"——这就是 c5 权限门在服务端该有的样子
#
# 对照真 Claude Code / 三个真实项目(HEAI renben.ai 就是这套:vanilla 前端 + FastAPI 后端 + Railway)。
import os, json, re, pathlib
import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

# ---- 配置(全部从环境变量读,本地用 .env,线上用 Railway/Vercel 的 Variables)----
API_KEY   = os.getenv("OPENROUTER_API_KEY", "")            # ← 绝不写死在代码里
MODEL     = os.getenv("MODEL", "anthropic/claude-haiku-4.5")  # 低延迟,够用(OpenRouter 有效 slug)
BASE_URL  = "https://openrouter.ai/api/v1/chat/completions"
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")   # 线上收紧成你的前端域名
HERE = pathlib.Path(__file__).parent
JOURNAL_DIR = HERE / "journals"; JOURNAL_DIR.mkdir(exist_ok=True)

# ---- 系统提示 = agent.md + 所有 skill_*.md(危机转介置顶,和 h5/1_DEFINE 一致)----
def load_system_prompt() -> str:
    parts = [(HERE / "agent.md").read_text(encoding="utf-8")]
    skills = HERE / "skills"
    crisis = skills / "skill_危机转介.md"
    if crisis.exists():                                     # 危机转介永远排在最前
        parts.append(crisis.read_text(encoding="utf-8"))
    for f in sorted(skills.glob("skill_*.md")):
        if f.name != "skill_危机转介.md":
            parts.append(f.read_text(encoding="utf-8"))
    protocol = (
        "\n\n## 输出协议(务必遵守)\n"
        "每次只回复一个 JSON,不要多余文字、不要 markdown 代码块:\n"
        '  需要用工具时:{\"tool\": \"save_journal\", \"args\": {\"entry\": \"...\"}}\n'
        '  直接回复用户时:{\"reply\": \"你要对用户说的话\"}\n'
    )
    return "".join(parts) + protocol

SYSTEM_PROMPT = load_system_prompt()

# ---- 危机关键词(确定性一票拦截:不依赖模型,离线也能守住底线)----
CRISIS_PATTERNS = [
    "自杀", "想死", "不想活", "活着没意思", "活不下去", "撑不下去", "撑不住了",
    "结束生命", "轻生", "伤害自己", "自残", "自伤", "不想醒", "解脱",
]
CRISIS_REPLY = (
    "我听到你现在非常痛苦,谢谢你愿意说出来。这件事很重要,而我只是一个 AI,"
    "没办法替代真正能帮到你的人。请**现在**联系专业援助:\n"
    "· 全国心理援助热线:**12356**\n"
    "· 北京心理危机研究与干预中心:**010-82951332**(24 小时)\n"
    "如果你有立刻的危险,请拨打 **120** 或就近急诊。你不是一个人,愿意的话,"
    "也请告诉你信任的老师、家人或朋友。我会在这里陪着你,但请一定先联系上面的真人。"
)

def is_crisis(text: str) -> bool:
    return any(p in text for p in CRISIS_PATTERNS)

# ---- 白名单工具(c1 工具箱的"服务端安全版":没有 bash,只有领域安全工具)----
def tool_save_journal(args: dict) -> str:
    alias = re.sub(r"[^\w一-鿿-]", "", str(args.get("alias", "guest")))[:40] or "guest"
    entry = str(args.get("entry", "")).strip()
    if not entry:
        return "（空日记,未写入）"
    (JOURNAL_DIR / f"{alias}.md").open("a", encoding="utf-8").write(f"- {entry}\n")
    return "已记录到情绪日记。"

TOOLS = {"save_journal": tool_save_journal}   # 想加工具就往这里加(白名单),绝不放 bash/rm

# ---- 调模型:一次 OpenRouter 调用;失败不抛给用户(优雅降级,小智 CompositeProvider 思想)----
def call_model(messages: list) -> str | None:
    if not API_KEY:
        return None
    try:
        r = httpx.post(BASE_URL, timeout=40,
            headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
            json={"model": MODEL, "messages": messages})
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
    except Exception:
        return None

def parse_json(s: str) -> dict:
    s = s.strip().strip("`").removeprefix("json").strip()
    return json.loads(s[s.find("{"): s.rfind("}") + 1])

FALLBACK = "抱歉,我这会儿有点忙不过来(可能是网络或额度问题)。你可以先深呼吸三次,过一会儿再和我说说吗?"

# ---- c3 子 agent:安全复核层(= 1_DEFINE E4 自检环的服务端落地)----
def safety_review(user_text: str, draft: str) -> str:
    if is_crisis(user_text):            # 1) 确定性一票拦截,永远优先
        return CRISIS_REPLY
    if not API_KEY:                     # 2) 没 key 就到此为止(已过确定性关卡)
        return draft
    verdict = call_model([             # 3) 独立的一次调用,让"另一个 agent"审这条回复
        {"role": "system", "content":
         "你是安全审核员。判断下面这条回复是否安全、是否越界(诊断/开药/漏掉危机信号)。"
         "只回一个词:SAFE 或 UNSAFE。"},
        {"role": "user", "content": f"用户说:{user_text}\n回复:{draft}"}])
    if verdict and "UNSAFE" in verdict.upper():
        return "我可能不适合回答这个问题——它超出了我能安全支持的范围。如果你正经历困扰,和信任的老师或专业人员聊聊会更好。"
    return draft

# ---- harness 一轮:工具循环直到 {"reply": ...}(c0 JSON 协议 + c1 工具箱 + c5 白名单权限门)----
def run_harness(messages: list) -> str:
    convo = [{"role": "system", "content": SYSTEM_PROMPT}] + messages
    for _ in range(6):                          # 最多 6 步,防死循环
        raw = call_model(convo)
        if raw is None:
            return FALLBACK                     # 优雅降级:调不通就给兜底话术,绝不 500
        convo.append({"role": "assistant", "content": raw})
        try:
            action = parse_json(raw)
        except Exception:
            convo.append({"role": "user", "content": "上一条不是合法 JSON,请只回一个 JSON。"}); continue
        if "reply" in action:
            return str(action["reply"])
        name = action.get("tool", "")
        if name not in TOOLS:                   # 不在白名单 → 拒绝(权限门)
            convo.append({"role": "user", "content": f"工具 {name} 不可用,只能用:{list(TOOLS)}"}); continue
        result = TOOLS[name](action.get("args", {}))
        convo.append({"role": "user", "content": f"工具结果:{result}"})
    return FALLBACK

# ---- FastAPI 应用 ----
app = FastAPI(title="考前3分钟 · 后端示例")
app.add_middleware(CORSMiddleware, allow_origins=CORS_ORIGINS,
                   allow_methods=["*"], allow_headers=["*"])

class ChatIn(BaseModel):
    messages: list          # [{"role":"user"/"assistant","content":"..."}]

@app.get("/api/health")
def health():
    return {"status": "ok", "model": MODEL, "has_key": bool(API_KEY)}

@app.post("/api/chat")
def chat(body: ChatIn):
    last_user = next((m["content"] for m in reversed(body.messages)
                      if m.get("role") == "user"), "")
    if is_crisis(str(last_user)):               # 入口先过危机确定性关卡(最快、最稳)
        return {"reply": CRISIS_REPLY, "meta": {"crisis": True}}
    draft = run_harness(body.messages)
    final = safety_review(str(last_user), draft) # 出口再过子agent安全复核
    return {"reply": final, "meta": {"crisis": final is CRISIS_REPLY}}
