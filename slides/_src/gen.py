# -*- coding: utf-8 -*-
"""2_dev_deploy_guide 模块导览 deck —— Fathom 数据叙事风 (Path A, html2pptx 原生可编辑).
画布 960x540px. 与 1_DEFINE_guide / lecture v2.0 数据叙事风同源。"""
import os
BG="#FFFFFF"; INK="#2B2B2B"; NAVY="#1A365D"; ACC="#C2410C"
GREEN="#2D7D46"; RED="#B03A2E"; GREY="#8A8A8A"; LINE="#E3E1DC"
PANEL="#F6F4EF"; NAVYT="#EAF0F6"
FCJK="'PingFang SC','Helvetica Neue',sans-serif"; FNUM="'Helvetica Neue','PingFang SC',Arial,sans-serif"
W,H=960,540; MX=56; CW=W-2*MX

def rect(x,y,w,h,fill=None,border=None,bw=1.5,radius=0):
    s=f"position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;box-sizing:border-box;"
    if fill:s+=f"background:{fill};"
    if border:s+=f"border:{bw}px solid {border};"
    if radius:s+=f"border-radius:{radius}px;"
    return f'<div style="{s}"></div>'
def hline(x,y,w,color=NAVY,h=2): return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{color};"></div>'
def vline(x,y,h,color=NAVY,w=2): return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{color};"></div>'
def txt(x,y,w,s,size=17,color=INK,weight=400,align="left",lh=1.35,tag="p",font=FCJK,ls="0px"):
    st=(f"position:absolute;left:{x}px;top:{y}px;width:{w}px;margin:0;padding:0;font-family:{font};"
        f"font-size:{size}px;color:{color};font-weight:{weight};text-align:{align};line-height:{lh};letter-spacing:{ls};")
    return f'<{tag} style="{st}">{s}</{tag}>'
def bullets(x,y,w,items,size=15,color=INK,lh=1.6,gap=4):
    lis="".join(f'<li style="margin:0 0 {gap}px 0;padding:0;">{it}</li>' for it in items)
    st=(f"position:absolute;left:{x}px;top:{y}px;width:{w}px;margin:0;padding:0 0 0 18px;font-family:{FCJK};"
        f"font-size:{size}px;color:{color};line-height:{lh};list-style:disc;")
    return f'<ul style="{st}">{lis}</ul>'
def kicker(k): return txt(MX,38,CW,k.upper(),12,NAVY,700,ls="1.5px")
def title(t,y=60,size=32,color=INK): return txt(MX,y,CW,t,size,color,700,lh=1.18)
def rule(y,x=MX,w=54): return hline(x,y,w,ACC,3)
def foot(page): return [txt(MX,512,460,"2_dev_deploy_guide · Build 与 Ship",11,GREY,500),
                        txt(W-140,512,84,f"{page:02d}",11,GREY,600,align="right",font=FNUM)]
def src(s,y=508,x=MX): return txt(x,y,CW,s,11,GREY,400,lh=1.3)
def page(bl):
    body=("<body style='margin:0;padding:0;width:960px;height:540px;position:relative;"
          f"background:{BG};overflow:hidden;'>"+"".join(bl)+"</body>")
    return ("<!doctype html><html><head><meta charset='utf-8'>"
            "<style>*{box-sizing:border-box;}p,h1,h2,h3,h4,ul,li{margin:0;}</style></head>"+body+"</html>")
def cards(items,y,h,accents=None,gap=18,top=18,bodysize=13):
    n=len(items); cw=(CW-gap*(n-1))//n; b=[]
    for i,(lab,tt,bd) in enumerate(items):
        x=MX+i*(cw+gap); acc=accents[i] if accents else NAVY
        b.append(rect(x,y,cw,h,fill="#FFFFFF",border=LINE,bw=1.4)); b.append(vline(x,y,h,acc,4))
        if lab: b.append(txt(x+16,y+top,cw-26,lab.upper(),11,acc,700,ls="1px"))
        b.append(txt(x+16,y+top+(20 if lab else 0),cw-26,tt,16,INK,700,lh=1.22))
        b.append(txt(x+16,y+top+(48 if lab else 26),cw-26,bd,bodysize,INK,400,lh=1.5))
    return b
P=[]

# 1 cover
P.append(page([rect(0,0,W,6,fill=NAVY),
    txt(MX,116,CW,"2_dev_deploy_guide",44,NAVY,800,font=FNUM,lh=1.0),
    rule(188,MX,72),
    txt(MX,208,CW,"Build 与 Ship 双支柱",34,INK,800,lh=1.2),
    txt(MX,270,CW,"把你的 PRD,变成一个手机能打开、能对话的公网应用",18,GREY,500),
    txt(MX,332,CW,"BUILD IT · SHIP IT",12,NAVY,700,ls="2px"),
    txt(MX,470,CW,"面向零编程/前端/后端/部署经验的心理与教育本科生",13,GREY,400)]))
# 2 positioning i2i
b=[kicker("定位 · i2i 全程"),title("你已经想清楚、评明白;现在把它做出来、送上线"),rule(112)]
steps=[("Idea","定义",NAVY),("Build","做出来",ACC),("Ship","送上线",ACC),("Impact","影响",NAVY)]
cw=(CW-3*12)//4
for i,(L,t,acc) in enumerate(steps):
    x=MX+i*(cw+12); y=176
    strong=acc==ACC
    b.append(rect(x,y,cw,96,fill=("#FBF1EC" if strong else "#FFFFFF"),border=(acc if strong else LINE),bw=(1.8 if strong else 1.3)))
    b.append(txt(x,y+16,cw,L,22,acc,800,align="center",font=FNUM))
    b.append(txt(x,y+54,cw,t,13,INK,600,align="center"))
    if i<3: b.append(txt(x+cw-2,y+34,16,"→",18,ACC,800))
b+=[rect(MX,300,(CW-16)//2,64,fill=NAVYT,border=NAVY,bw=1.3),
    txt(MX+16,314,360,"1_DEFINE_guide",13,NAVY,800),txt(MX+16,336,380,"= Idea 定义 + 评估(已完成)",12,GREY,500)]
x2=MX+(CW-16)//2+16
b+=[rect(x2,300,(CW-16)//2,64,fill="#FBF1EC",border=ACC,bw=1.6),
    txt(x2+16,314,360,"2_dev_deploy_guide(本模块)",13,ACC,800),txt(x2+16,336,380,"= Build 做出来 + Ship 送上线",12,GREY,500)]
b.append(txt(MX,392,CW,"目标产出:一个任何人手机都能打开、能对话的公网心理/教育智能体 + 一份结项技术文档。",13,GREY,500))
b+=foot(2); P.append(page(b))
# 3 three-layer arch
b=[kicker("架构 · THREE LAYERS"),title("三层架构:前端 → 后端 → 模型"),rule(112)]
b+=cards([("前端 FRONTEND","一张聊天页(静态)","用户看到的界面;公开,绝不放 key"),
          ("后端 BACKEND","你的 agent 服务","跑 harness、藏 key、代理模型;是安全的守门人"),
          ("模型 MODEL","OpenRouter","真正生成回复;key 只在后端 env")],
         178,196,accents=[NAVY,ACC,NAVY])
b+=[rect(MX,406,CW,42,fill="#FBECEA",border=RED,bw=1.4),
    txt(MX+18,417,CW-36,"🔑 key 铁律:API key 只能待在后端环境变量,前端是公开的、任何人能看源码。",13,RED,700,lh=1.3)]
b+=foot(3); P.append(page(b))
# 4 harness → capabilities
b=[kicker("后端地基 · YOUR HARNESS"),title("后端不用从零:就是你在模块 1 造的 mini CC harness"),rule(112)]
rows=[("c0 JSON 协议","结构化输出,前端稳定解析"),
      ("c1 工具箱","读写文件 + 领域工具(查量表/存日记)"),
      ("c3 子 agent","★ 安全复核层 = 1_DEFINE E4 自检环落地"),
      ("c4 压缩 / c5 权限门","长对话不爆 · 危险动作要人批准")]
y0=170; rh=58
for i,(l,r) in enumerate(rows):
    y=y0+i*rh; strong="★" in r
    b.append(rect(MX,y,CW,rh-8,fill=("#FBF1EC" if strong else "#FFFFFF"),border=(ACC if strong else LINE),bw=(1.8 if strong else 1.2)))
    b.append(txt(MX+18,y+13,300,l,15,(ACC if strong else NAVY),800))
    b.append(txt(MX+330,y+14,CW-350,r,13.5,INK,500,lh=1.3))
b.append(txt(MX,y0+4*rh+2,CW,"改造只做三件事:input() 循环 → /api/chat;key 走 env;去掉 bash 只留白名单工具。",13,GREY,500))
b+=foot(4); P.append(page(b))
# 5 three reference archs
b=[kicker("参考架构 · THREE TIERS"),title("三个真实项目,三档参考架构(都用 Railway)"),rule(112)]
b+=cards([("入门 · 小智","静态 + 离线兜底","Next 静态导出 + CompositeProvider 优雅降级"),
          ("默认 · HEAI","Vanilla + FastAPI","= 本模块默认样板;+ 证据引用 grounding"),
          ("进阶 · Agent Leo","Next 全栈 + 多agent","Supabase + Claude 代理 + 匿名优先")],
         178,200,accents=[NAVY,ACC,NAVY])
b.append(txt(MX,408,CW,"想快上线→学小智/端到端示例;要 Python 后端→学 HEAI;要多 agent/账号→参考 Leo。",13,GREY,500))
b+=foot(5); P.append(page(b))
# 6 SECTION BUILD
P.append(page([rect(0,0,W,H,fill=NAVY),
    txt(MX,150,CW,"PILLAR 01",16,"#8FB0CC",800,ls="3px",font=FNUM),rule(196,MX,72),
    txt(MX,214,CW,"做出来 · BUILD",44,"#FFFFFF",800),
    txt(MX,290,CW,"你是导演,不是码农 —— 指挥 Claude Code 写,你把关架构与安全",19,"#C6D6E6",500),
    txt(MX,470,CW,"产出:一个本地跑得通、带安全复核的全栈 MVP",13,"#8FB0CC",400)]))
# 7 B0 director
b=[kicker("B0 · 你是导演不是码农"),title("零编程也能做:你负责三件工程师替不了的事"),rule(112)]
b+=cards([("看懂架构","前端/后端/模型怎么连","知道谁调用谁、key 藏哪"),
          ("守住安全","key 不进前端 · 危机必拦","grep sk- 为零 · 危机转介置顶"),
          ("把关体验","语气/边界/降级","像你的产品,而不是通用 bot")],
         178,196,accents=[NAVY,ACC,NAVY])
b.append(txt(MX,404,CW,"写代码交给 Claude Code;定义问题、守安全、做判断——永远是你。",13,GREY,500))
b+=foot(7); P.append(page(b))
# 8 B1 backend agent
b=[kicker("B1 · 装配后端 agent"),title("以 harness 为底,按 PRD 装上你的专业"),rule(112)]
b+=[rect(MX,178,(CW-24)//2,232,fill="#FFFFFF",border=LINE,bw=1.4),vline(MX,178,232,NAVY,5),
    txt(MX+20,196,360,"装什么",14,NAVY,800),
    bullets(MX+20,228,(CW-24)//2-44,["agent.md(人设三段式)","领域 skills(如正念/CBT)","<b>危机转介 skill —— 置顶必备</b>"],14.5,lh=1.7)]
x2=MX+(CW-24)//2+24
b+=[rect(x2,178,(CW-24)//2,232,fill="#FBF1EC",border=ACC,bw=1.6),
    txt(x2+20,196,360,"开哪个支柱",14,ACC,800),
    bullets(x2+20,228,(CW-24)//2-44,["<b>c3 子 agent = 安全自检复核</b>","要工具 → 回 c1 工具箱","长对话 → 回 c4 压缩"],14.5,lh=1.7)]
b.append(src("参照运行示例 backend/agent.md + skills/skill_危机转介.md",470))
b+=foot(8); P.append(page(b))
# 9 B2 服务化
b=[kicker("B2 · 后端服务化"),title("把 harness 从 input() 循环,变成 /api/chat"),rule(112)]
b+=cards([("无状态接口","POST /api/chat","前端传 messages → 后端跑一轮 → 回 reply"),
          ("key 走 env","os.environ","绝不写死;去掉 bash,只留白名单工具"),
          ("永不崩","优雅降级","调不通返回兜底话术,不给用户 500")],
         176,182,accents=[ACC,NAVY,NAVY])
b+=[rect(MX,366,CW,48,fill="#FBECEA",border=RED,bw=1.4),
    txt(MX+18,378,CW-36,"危机一票否决由<b>确定性代码</b> is_crisis() 在入口/出口各兜一次——模型可能失手,代码不能失守。",13,RED,700,lh=1.3)]
b+=foot(9); P.append(page(b))
# 10 B3 frontend
b=[kicker("B3 · 前端界面"),title("三句话,让 Claude Code 生成你的聊天页"),rule(112)]
b+=[rect(MX,178,(CW-24)//2,232,fill=NAVYT,border=NAVY,bw=1.4),
    txt(MX+20,196,360,"提示词三句",14,NAVY,800),
    bullets(MX+20,228,(CW-24)//2-44,["做什么页:一个聊天界面","什么风格:贴你项目(温暖/专业)","连哪个后端:调 /api/chat"],14.5,lh=1.7)]
x2=MX+(CW-24)//2+24
b+=[rect(x2,178,(CW-24)//2,232,fill="#FFFFFF",border=ACC,bw=1.6),
    txt(x2+20,196,360,"两个必加",14,ACC,800),
    bullets(x2+20,228,(CW-24)//2-44,["<b>危机求助按钮</b>(把安全做进界面)","<b>优雅降级</b>:后端连不上不白屏","(小智 CompositeProvider 思想)"],14.5,lh=1.7)]
b.append(src("参照运行示例 frontend/index.html(纯静态,零 key)",470))
b+=foot(10); P.append(page(b))
# 11 B4 connect+safety
b=[kicker("B4 · 连通与安全自检"),title("上线前,先在本地把安全关走一遍"),rule(112)]
b+=[txt(MX,180,560,"grep -rniE \"sk-[a-z0-9]{16}\"",26,ACC,800,font=FNUM,lh=1.1),
    txt(MX,222,560,"前端目录必须为零。前端是公开的,key 只能在后端。",17,INK,600)]
b+=[rect(MX+560,178,232,236,fill=PANEL,border=LINE,bw=1.3),
    txt(MX+582,196,190,"四条自检",12,NAVY,700),
    bullets(MX+582,228,190,["前端只调 /api/chat","无任何 sk-","CORS 配好","错误有兜底"],13.5,lh=1.7)]
b.append(txt(MX,300,540,"产出:一个本地跑通的全栈 MVP——下一支柱,把它送上线。",13,GREY,500))
b+=foot(11); P.append(page(b))
# 12 SECTION SHIP
P.append(page([rect(0,0,W,H,fill=NAVY),
    txt(MX,150,CW,"PILLAR 02",16,"#8FB0CC",800,ls="3px",font=FNUM),rule(196,MX,72),
    txt(MX,214,CW,"送上线 · SHIP",44,"#FFFFFF",800),
    txt(MX,290,CW,"不上线 = 没有 impact:让世界用手机就能打开你的作品",19,"#C6D6E6",500),
    txt(MX,470,CW,"GitHub Pages(前端)+ Railway(后端)+ Vercel(免费替代)",13,"#8FB0CC",400)]))
# 13 S0 static vs dynamic
b=[kicker("S0 · 静态 vs 动态"),title("先分清:你要上线的是哪一种"),rule(112)]
b+=[rect(MX,178,(CW-24)//2,232,fill="#FFFFFF",border=LINE,bw=1.4),vline(MX,178,232,NAVY,5),
    txt(MX+20,196,360,"静态 STATIC",15,NAVY,800),
    bullets(MX+20,228,(CW-24)//2-44,["只有界面/展示,不真调模型","→ GitHub Pages,免费最简单","作品集、说明页、demo 截图"],14.5,lh=1.7)]
x2=MX+(CW-24)//2+24
b+=[rect(x2,178,(CW-24)//2,232,fill="#FBF1EC",border=ACC,bw=1.6),vline(x2,178,232,ACC,5),
    txt(x2+20,196,360,"动态 DYNAMIC",15,ACC,800),
    bullets(x2+20,228,(CW-24)//2-44,["要真对话:调模型/存数据","→ 后端 Railway(默认,Python 友好)","key 藏后端环境变量"],14.5,lh=1.7)]
b.append(src("成本:Pages/Vercel 免费;Railway ~$5 试用/hobby(非永久免费),要零成本用 Vercel",470))
b+=foot(13); P.append(page(b))
# 14 S1 pages
b=[kicker("S1 · GitHub Pages"),title("静态展示上线:推上去就有网址"),rule(112)]
stp=[("建仓库","前端代码 push 到 GitHub"),("开 Pages","Settings → Pages 选分支"),
     ("等构建","拿到 username.github.io URL"),("分享","发链接,谁都能打开")]
cw=(CW-3*14)//4
for i,(t,d) in enumerate(stp):
    x=MX+i*(cw+14); y=178
    b.append(rect(x,y,cw,150,fill="#FFFFFF",border=LINE,bw=1.4))
    b.append(txt(x+12,y+14,cw-20,f"STEP {i+1}",11,ACC,700,ls="1px"))
    b.append(txt(x+12,y+40,cw-20,t,14.5,INK,800,lh=1.2))
    b.append(txt(x+12,y+74,cw-20,d,12.5,GREY,400,lh=1.5))
b.append(txt(MX,352,CW,"免费、你已在用 GitHub、纯静态最省事——路演前先把展示页挂上去。",13,GREY,500))
b+=foot(14); P.append(page(b))
# 15 S2 railway
b=[kicker("S2 · 后端上线 Railway"),title("FastAPI → Railway:Python 自动识别,一键部署"),rule(112)]
stp=[("连 GitHub","Deploy from repo,选后端目录"),("自动识别","Nixpacks 认出 Python,装 requirements"),
     ("放 key","Variables 填 OPENROUTER_API_KEY"),("拿域名","xxx.up.railway.app + /api/health")]
cw=(CW-3*14)//4
for i,(t,d) in enumerate(stp):
    x=MX+i*(cw+14); y=176
    b.append(rect(x,y,cw,168,fill="#FFFFFF",border=LINE,bw=1.4))
    b.append(txt(x+12,y+14,cw-20,f"STEP {i+1}",11,ACC,700,ls="1px"))
    b.append(txt(x+12,y+40,cw-20,t,14,INK,800,lh=1.2))
    b.append(txt(x+12,y+74,cw-20,d,12,GREY,400,lh=1.5))
b.append(txt(MX,362,CW,"= HEAI/renben.ai 同款栈。零成本替代:Vercel(Node serverless)。key 只在 Variables,不进代码。",13,GREY,500))
b+=foot(15); P.append(page(b))
# 16 S3 connect
b=[kicker("S3 · 整体上线"),title("前端接后端:改一行 + 配 CORS + 手机测"),rule(112)]
b+=cards([("改前端","BACKEND = Railway 域名","前端指向你的后端公网地址"),
          ("配 CORS","后端 CORS_ORIGINS = Pages 域名","否则浏览器拦跨域,聊不起来"),
          ("手机测","换设备打开","很多用户在手机;跨设备验证")],
         178,196,accents=[ACC,NAVY,NAVY])
b.append(txt(MX,404,CW,"产出:任何人用手机点开链接,就能和你的 agent 对话——这就是 impact 的起点。",13,GREY,500))
b+=foot(16); P.append(page(b))
# 17 S4 checklist
b=[kicker("S4 · 上线检查与结项"),title("上线前,逐条勾选"),rule(112)]
chk=["密钥:grep sk- 为零 · key 在 Variables · git 历史无 key","可用:URL 能开 · 能对话 · 手机测过",
     "合规:AI 身份披露 · 隐私说明 · 危机热线 12356","降级:后端挂了有兜底,不白屏",
     "文档:README 三要素(是什么/怎么用/谁做的)","结项:技术架构图 + 部署说明 + 复现步骤"]
b+=[rect(MX,170,CW,242,fill="#FFFFFF",border=LINE,bw=1.4)]
col=(CW-44)//2
b.append(bullets(MX+24,190,col-10,chk[:3],14,INK,lh=2.0))
b.append(bullets(MX+24+col,190,col-10,chk[3:],14,INK,lh=2.0))
b.append(txt(MX,424,CW,"国内长期给用户用 → 可迁腾讯云/阿里云(需实名+少量费用)。",13,GREY,500))
b+=foot(17); P.append(page(b))
# 18 end-to-end example
b=[kicker("端到端示例 · 考前3分钟"),title("一个能跑的最小骨架:PRD → 公网 URL"),rule(112)]
b+=[rect(MX,176,516,236,fill="#FFFFFF",border=LINE,bw=1.4),
    txt(MX+20,194,470,"架构(= HEAI 简化版)",13,NAVY,700,ls="1px"),
    bullets(MX+20,224,470,["前端 index.html(静态,无 key)→ GitHub Pages","后端 main.py(FastAPI 包 harness)→ Railway","危机 is_crisis() 确定性拦截 + c3 子agent复核","调不通有 FALLBACK,不白屏"],14,lh=1.75)]
x2=MX+516+16
b+=[rect(x2,176,CW-516-16,236,fill=NAVYT,border=ACC,bw=1.4),
    txt(x2+18,196,180,"已验证",12,ACC,700),
    bullets(x2+18,226,180,["本地 uvicorn 起","危机拦截生效","优雅降级生效"],13,lh=1.7),
    txt(x2+18,352,180,"照它改成你的项目",12,GREY,500,lh=1.3)]
b+=foot(18); P.append(page(b))
# 19 skills + platforms
b=[kicker("怎么用 · SKILLS"),title("六个教练 skill + 三个平台"),rule(112)]
b+=[rect(MX,178,(CW-24)//2,232,fill="#FFFFFF",border=LINE,bw=1.4),vline(MX,178,232,NAVY,5),
    txt(MX+20,196,360,"/build-* · /ship-* 教练",14,NAVY,800),
    bullets(MX+20,226,(CW-24)//2-44,["build: backend · frontend · connect","ship: static · backend · golive","<b>分步陪跑 · 自动扫 sk- · 不甩全部命令</b>"],14,lh=1.7)]
x2=MX+(CW-24)//2+24
b+=[rect(x2,178,(CW-24)//2,232,fill="#FBF1EC",border=ACC,bw=1.4),
    txt(x2+20,196,360,"三个平台",14,ACC,800),
    bullets(x2+20,226,(CW-24)//2-44,["GitHub Pages —— 静态前端(免费)","Railway —— Python 后端(默认)","Vercel —— 免费替代"],14,lh=1.7)]
b.append(txt(MX,428,CW,"红线:key 只在后端;危机由代码兜底;上线才有 impact。",13,RED,600))
b+=foot(19); P.append(page(b))
# 20 closing
P.append(page([rect(0,0,W,6,fill=NAVY),
    txt(MX,120,CW,"带走三句话",13,NAVY,700,ls="2px"),rule(156,MX,72),
    txt(MX,184,CW-40,"「key 只能待在后端,前端是公开的。」",30,INK,800,lh=1.3),
    txt(MX,232,CW-40,"「危机由确定性代码兜底,不只靠模型自觉。」",30,INK,800,lh=1.3),
    txt(MX,280,CW-40,"「不上线,就没有 impact。」",30,ACC,800,lh=1.3),
    txt(MX,360,CW,"你不需要会写代码——你需要看懂架构、守住安全、把它送上线。",16,GREY,500),
    txt(MX,470,CW,"郑先隽 · 北京师范大学心理学部 · 人本 AI 设计与创新 · i2i",13,GREY,400)]))

HERE=os.path.dirname(os.path.abspath(__file__)); d=os.path.join(HERE,"html"); os.makedirs(d,exist_ok=True)
for i,html in enumerate(P,1): open(os.path.join(d,f"{i:02d}.html"),"w",encoding="utf-8").write(html)
print(f"{len(P)} pages")
