# -*- coding: utf-8 -*-
"""web_basics 教程 deck —— AI 时代 web 技术栈基础 · Fathom 数据叙事风 (Path A).
第二套 deck,与 2_dev_deploy_guide_数据叙事风.pptx 共存。画布 960x540px 全绝对定位。"""
import os
BG="#FFFFFF"; INK="#2B2B2B"; NAVY="#1A365D"; ACC="#C2410C"
GREEN="#2D7D46"; RED="#B03A2E"; GREY="#8A8A8A"; LINE="#E3E1DC"
PANEL="#F6F4EF"; NAVYT="#EAF0F6"; GREENT="#EAF3EC"
FCJK="'PingFang SC','Helvetica Neue',sans-serif"; FNUM="'Helvetica Neue','PingFang SC',Arial,sans-serif"
MONO="'SF Mono','Menlo','Consolas',monospace"
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
def title(t,y=60,size=31,color=INK): return txt(MX,y,CW,t,size,color,700,lh=1.18)
def rule(y,x=MX,w=54): return hline(x,y,w,ACC,3)
def foot(page): return [txt(MX,512,520,"web_basics · AI 时代 web 技术栈基础",11,GREY,500),
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
        b.append(txt(x+16,y+top+(20 if lab else 0),cw-26,tt,15.5,INK,700,lh=1.22))
        b.append(txt(x+16,y+top+(46 if lab else 26),cw-26,bd,bodysize,INK,400,lh=1.5))
    return b
def robot_eye(y, robot, eye, h=118):
    """签名装置:🤖 Claude Code 帮你做了什么 / 👁 你要认得什么"""
    b=[]; w=(CW-16)//2
    b.append(rect(MX,y,w,h,fill=NAVYT,border=NAVY,bw=1.4))
    b.append(txt(MX+16,y+12,w-30,"🤖 Claude Code 帮你做了",12,NAVY,800))
    b.append(txt(MX+16,y+34,w-30,robot,13,INK,400,lh=1.5))
    x2=MX+w+16
    b.append(rect(x2,y,w,h,fill="#FBF1EC",border=ACC,bw=1.6))
    b.append(txt(x2+16,y+12,w-30,"👁 你要认得(会指挥)",12,ACC,800))
    b.append(txt(x2+16,y+34,w-30,eye,13,INK,400,lh=1.5))
    return b
def code(x,y,w,h,lines,fill="#1E2A38"):
    b=[rect(x,y,w,h,fill=fill,radius=6)]
    b.append(txt(x+14,y+10,w-26,lines,12,"#E8EEF4",400,lh=1.7,font=MONO))
    return b
def section(part, big, sub, note):
    return page([rect(0,0,W,H,fill=NAVY),
        txt(MX,150,CW,part,16,"#8FB0CC",800,ls="3px",font=FNUM),rule(196,MX,72),
        txt(MX,214,CW,big,44,"#FFFFFF",800),
        txt(MX,290,CW,sub,19,"#C6D6E6",500),
        txt(MX,470,CW,note,13,"#8FB0CC",400)])
P=[]

# 1 cover
P.append(page([rect(0,0,W,6,fill=NAVY),
    txt(MX,110,CW,"web_basics",50,NAVY,800,font=FNUM,lh=1.0),
    rule(184,MX,72),
    txt(MX,204,CW,"AI 时代 · web 技术栈基础",34,INK,800,lh=1.2),
    txt(MX,266,CW,"你不用手写代码——但要看懂它写了什么、读得懂报错、知道每层是什么",17,GREY,500),
    txt(MX,326,CW,"UNDERSTAND THE STACK · DIRECT THE AI",12,NAVY,700,ls="2px"),
    txt(MX,470,CW,"2_dev_deploy_guide 前置基础包 · 面向零 web 基础的心理与教育学生",13,GREY,400)]))

# 2 why learn
b=[kicker("为什么 · WHY LEARN THIS"),title("AI 替你写代码,但看不懂 = 指挥不动、也救不回"),rule(112)]
b+=cards([("看懂","读得懂 Claude Code 写了什么","它生成一堆文件,你至少知道每个是干嘛的"),
          ("会指挥","把需求说到点子上","知道该说\"改后端\"还是\"改前端\""),
          ("能排错","报错时看得懂、救得回","白屏/404/CORS 时不抓瞎")],
         172,150,accents=[NAVY,ACC,NAVY])
b+=[rect(MX,336,CW,80,fill=PANEL,border=LINE,bw=1.2),
    txt(MX+18,350,CW-36,"AI 编程已是主流:2026 年约 90% 开发者每天用 AI 工具(Claude Code / Cursor / v0 / bolt / Lovable)。",13,INK,600,lh=1.4),
    txt(MX+18,378,CW-36,"工作流变了:AI 生成,你审阅+指挥。所以「看懂」比「会手写」更重要。",13,GREY,500,lh=1.4)]
b+=foot(2); P.append(page(b))

# 3 SECTION W1
P.append(section("PART 01","Web 是怎么运作的","从你输入网址,到页面出现,发生了什么","先建立全局心智模型,后面每一层才有位置"))

# 4 request journey
b=[kicker("W1 · 一次请求的旅程"),title("你输入网址,到页面出现:6 步"),rule(112)]
steps=[("输网址","你在浏览器敲 URL"),("查地址","DNS 把域名翻成 IP"),("发请求","浏览器向服务器要页面"),
       ("服务器","后端处理、返回内容"),("传回来","HTTP 响应回到浏览器"),("渲染","浏览器画成你看到的页面")]
cw=(CW-5*10)//6
for i,(t,d) in enumerate(steps):
    x=MX+i*(cw+10); y=176
    b.append(rect(x,y,cw,150,fill="#FFFFFF",border=LINE,bw=1.3))
    b.append(txt(x+10,y+14,cw-16,f"{i+1}",20,ACC,800,font=FNUM))
    b.append(txt(x+10,y+48,cw-16,t,13,INK,800,lh=1.15))
    b.append(txt(x+10,y+78,cw-16,d,11,GREY,400,lh=1.4))
    if i<5: b.append(txt(x+cw-2,y+62,14,"→",15,ACC,800))
b.append(txt(MX,350,CW,"这趟旅程每天在你每次点开网页时发生无数次——记住它,报错时就知道卡在哪一步。",13,GREY,500))
b+=foot(4); P.append(page(b))

# 5 client vs server
b=[kicker("W1 · 客户端 vs 服务器"),title("前端在你的浏览器里跑,后端在远处的服务器上跑"),rule(112)]
b+=[rect(MX,178,(CW-24)//2,232,fill=NAVYT,border=NAVY,bw=1.5),
    txt(MX+20,196,360,"客户端 CLIENT(前端)",14,NAVY,800),
    bullets(MX+20,228,(CW-24)//2-44,["就是你的<b>浏览器</b>(Chrome/Safari)","跑 HTML/CSS/JS,画出界面","<b>公开的</b>:谁都能看源码 → 绝不放 key"],14.5,lh=1.7)]
x2=MX+(CW-24)//2+24
b+=[rect(x2,178,(CW-24)//2,232,fill="#FFFFFF",border=ACC,bw=1.6),
    txt(x2+20,196,360,"服务器 SERVER(后端)",14,ACC,800),
    bullets(x2+20,228,(CW-24)//2-44,["一台<b>一直开机</b>的远程电脑","跑你的 agent 逻辑、藏 key、连模型","<b>私密的</b>:用户看不到里面"],14.5,lh=1.7)]
b.append(txt(MX,430,CW,"回忆 2_dev_deploy 的三层架构:前端(浏览器)→ 后端(服务器)→ 模型。现在你懂前两层住在哪了。",13,GREY,500))
b+=foot(5); P.append(page(b))

# 6 http static dynamic
b=[kicker("W1 · HTTP · 静态 vs 动态"),title("网页分两种:发好的文件 vs 现场算出来"),rule(112)]
b+=cards([("HTTP(S)","浏览器和服务器的对话规矩","请求-响应;S=加密,现在都用 https"),
          ("静态 STATIC","只发写好的文件","展示页/作品集 → GitHub Pages 免费"),
          ("动态 DYNAMIC","服务器现场生成/调模型","能对话的 agent → 要后端(Railway)")],
         172,150,accents=[NAVY,GREEN,ACC])
b+=[rect(MX,338,CW,78,fill=NAVYT,border=LINE,bw=1.2),
    txt(MX+18,352,CW-36,"域名(domain):yourname.github.io 这种人类好记的地址;DNS 负责把它翻译成机器认的 IP。",13,INK,500,lh=1.4),
    txt(MX+18,382,CW-36,"你的项目:静态展示页 + 动态对话后端,正好一静一动。",13,GREY,500,lh=1.3)]
b+=foot(6); P.append(page(b))

# 7 SECTION W2 frontend trio
P.append(section("PART 02","前端三件套","HTML · CSS · JavaScript —— 网页由什么组成","一句话:HTML 搭骨架,CSS 化妆,JS 让它动起来"))

# 8 trio overview
b=[kicker("前端三件套 · THE TRIO"),title("盖房子的比喻:结构 · 装修 · 电路"),rule(112)]
b+=cards([("HTML","结构/骨架","房子的墙和房间:标题、按钮、输入框在哪"),
          ("CSS","外观/装修","刷漆铺地板:颜色、字号、排版、圆角"),
          ("JavaScript","行为/电路","按开关有反应:点击、发消息、调后端")],
         178,158,accents=[ACC,NAVY,GREEN])
b.append(txt(MX,408,CW,"你的运行示例 frontend/index.html 里,这三样都在一个文件里——一会儿逐个拆给你看。",13,GREY,500))
b+=foot(8); P.append(page(b))

# 9 HTML
b=[kicker("W2 · HTML 骨架"),title("HTML:用「标签」把内容装进「盒子」"),rule(112)]
b+=code(MX,176,(CW-24)//2,150,'&lt;header&gt;<br>&nbsp;&nbsp;&lt;h1&gt;考前3分钟&lt;/h1&gt;<br>&lt;/header&gt;<br>&lt;form&gt;<br>&nbsp;&nbsp;&lt;input placeholder="说说"&gt;<br>&nbsp;&nbsp;&lt;button&gt;发送&lt;/button&gt;<br>&lt;/form&gt;')
x2=MX+(CW-24)//2+24
b+=[txt(x2,176,(CW-24)//2,"三个词看懂 HTML:",14,NAVY,800),
    bullets(x2,206,(CW-24)//2,["<b>标签 tag</b>:&lt;button&gt; 一对,包住内容","<b>元素 element</b>:一个完整的盒子","<b>属性 attr</b>:placeholder / id / class,给盒子加设定"],14,lh=1.7),
    txt(x2,320,(CW-24)//2,"↑ 这就是你运行示例 index.html 里真实的一段。",12,GREY,500,lh=1.4)]
b+=robot_eye(360, "自动写好所有标签、嵌套、属性。", "看得懂 &lt;button&gt;/&lt;input&gt; 大概是什么,能说\"加一个危机求助按钮\"。", h=88)
b+=foot(9); P.append(page(b))

# 10 CSS
b=[kicker("W3 · CSS 外观"),title("CSS:给盒子「化妆」和「排版」"),rule(112)]
b+=[txt(MX,176,(CW-24)//2,"三件事:",14,NAVY,800),
    bullets(MX,206,(CW-24)//2,["<b>选择器</b>:选中哪些盒子(按 class/标签)","<b>盒模型</b>:每个盒子有内边距/边框/外边距","<b>布局</b>:flex(自动排队)vs 绝对定位(指哪放哪)"],14,lh=1.7),
    txt(MX,326,(CW-24)//2,"颜色用 #1A365D 这种十六进制;字号用 px。",12,GREY,500,lh=1.4)]
x2=MX+(CW-24)//2+24
b+=code(x2,176,(CW-24)//2,150,'.btn {<br>&nbsp;&nbsp;background: #C2410C;<br>&nbsp;&nbsp;color: white;<br>&nbsp;&nbsp;border-radius: 10px;<br>&nbsp;&nbsp;padding: 10px 18px;<br>}')
b+=robot_eye(360, "自动写全部样式,还能一句话改配色/圆角。", "认得 color/background/padding,能说\"配色换成温暖治愈风\"。", h=88)
b+=foot(10); P.append(page(b))

# 11 JS 1
b=[kicker("W4 · JavaScript 交互"),title("JavaScript:让网页「动」起来"),rule(112)]
b+=[txt(MX,176,(CW-24)//2,"三个基本功:",14,NAVY,800),
    bullets(MX,206,(CW-24)//2,["<b>变量</b>:存东西(如聊天历史 history)","<b>函数</b>:一段可反复调用的动作","<b>事件</b>:用户点击(onclick)、提交(onsubmit)触发函数"],14,lh=1.7),
    txt(MX,326,(CW-24)//2,"DOM = JS 操作页面的方式(增删改盒子)。",12,GREY,500,lh=1.4)]
x2=MX+(CW-24)//2+24
b+=code(x2,176,(CW-24)//2,150,'form.onsubmit = () =&gt; {<br>&nbsp;&nbsp;const t = inp.value;<br>&nbsp;&nbsp;sendMsg(t); // 调后端<br>};<br><br>// ← index.html 里真有这段')
b.append(txt(MX,360,CW,"下一页看 JS 最关键的一招:fetch —— 网页怎么「向后端打电话」。",13,GREY,500))
b+=foot(11); P.append(page(b))

# 12 JS fetch
b=[kicker("W4 · fetch:前端 → 后端"),title("fetch:网页向后端「打电话」问答案"),rule(112)]
b+=code(MX,176,(CW-24)//2,168,'const r = await fetch(<br>&nbsp;&nbsp;BACKEND + "/api/chat",<br>&nbsp;&nbsp;{ method:"POST",<br>&nbsp;&nbsp;&nbsp;&nbsp;body: JSON.stringify(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ messages: history }) }<br>);<br>const data = await r.json();')
x2=MX+(CW-24)//2+24
b+=[txt(x2,176,(CW-24)//2,"一句话:",14,NAVY,800),
    bullets(x2,206,(CW-24)//2,["前端把用户的话 <b>发给后端</b> /api/chat","后端跑 agent、回一段 reply","前端把 reply 显示成气泡"],14,lh=1.7),
    txt(x2,306,(CW-24)//2,"这就是你运行示例前端 sendMsg() 做的事。",12,GREY,500,lh=1.4)]
b+=robot_eye(360,"写好 fetch、错误处理、降级。","认得 fetch = 调后端;能说\"后端连不上要有兜底,别白屏\"。",h=88)
b+=foot(12); P.append(page(b))

# 13 SECTION W5
P.append(section("PART 03","数据怎么在网上传","JSON · API · 请求响应 —— 前后端如何对话","JSON 是普通话,API 是菜单,状态码是回执"))

# 14 JSON
b=[kicker("W5 · JSON"),title("JSON:前端和后端之间的「普通话」"),rule(112)]
b+=code(MX,176,(CW-24)//2,140,'{<br>&nbsp;&nbsp;"messages": [<br>&nbsp;&nbsp;&nbsp;&nbsp;{"role":"user",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"content":"我好紧张"}<br>&nbsp;&nbsp;]<br>}')
x2=MX+(CW-24)//2+24
b+=[txt(x2,176,(CW-24)//2,"JSON 就是「键: 值」清单:",14,NAVY,800),
    bullets(x2,208,(CW-24)//2,["人和机器都读得懂的通用格式","前端发 JSON、后端回 JSON","你在 1_claude_code_basic 见过它"],14,lh=1.7),
    txt(x2,302,(CW-24)//2,"认得大括号 { } 和引号里的 key,就够了。",12,GREY,500,lh=1.4)]
b.append(txt(MX,352,CW,"你的 agent 输出协议就是 JSON:{\"reply\":\"...\"} 或 {\"tool\":\"...\"}。前后端靠它对齐。",13,GREY,500))
b+=foot(14); P.append(page(b))

# 15 API
b=[kicker("W5 · API 与 REST"),title("API:后端对外的「菜单」,点什么给什么"),rule(112)]
b+=cards([("API = 接口","后端开放的\"点单窗口\"","前端照菜单点,后端照单做"),
          ("端点 endpoint","一道菜的地址","/api/chat 对话 · /api/health 体检"),
          ("方法 method","怎么点","GET 取数据 · POST 提交数据")],
         172,152,accents=[NAVY,ACC,GREEN])
b+=[rect(MX,338,CW,78,fill=NAVYT,border=LINE,bw=1.2),
    txt(MX+18,352,CW-36,"REST = 一套大家都遵守的\"点单规矩\"(用 URL + GET/POST 表达要做什么)。",13,INK,500,lh=1.4),
    txt(MX+18,382,CW-36,"你运行示例的后端就开了两道菜:POST /api/chat(聊天)、GET /api/health(体检)。",13,GREY,500,lh=1.3)]
b+=foot(15); P.append(page(b))

# 16 status codes
b=[kicker("W5 · 状态码"),title("状态码:后端给你的「回执」——看懂报错第一步"),rule(112)]
rows=[("200","成功",GREEN,"一切正常,拿到结果"),
      ("400 / 401","你发的请求有问题",ACC,"参数错 / 没权限(如 key 错)"),
      ("404","找不到",ACC,"地址写错 / 页面或端点不存在"),
      ("500","后端自己崩了",RED,"服务器内部错误,去看后端日志")]
y0=172; rh=58
for i,(cod,t,acc,d) in enumerate(rows):
    y=y0+i*rh
    b.append(rect(MX,y,CW,rh-8,fill="#FFFFFF",border=LINE,bw=1.2)); b.append(vline(MX,y,rh-8,acc,4))
    b.append(txt(MX+18,y+13,120,cod,17,acc,800,font=FNUM))
    b.append(txt(MX+150,y+14,200,t,14,INK,700))
    b.append(txt(MX+360,y+14,CW-380,d,13,GREY,500,lh=1.3))
b.append(txt(MX,y0+4*rh+2,CW,"记住这四类,报错时你就能对 Claude Code 说清\"是 404 还是 500\",它才好帮你修。",13,GREY,500))
b+=foot(16); P.append(page(b))

# 17 SECTION W6
P.append(section("PART 04","前端框架","React · Next.js —— 什么时候纯 HTML 不够用","框架是给复杂界面用的\"工具箱\";简单的用纯静态就好"))

# 18 why framework
b=[kicker("W6 · 为什么要框架"),title("纯 HTML 够用,直到它不够用"),rule(112)]
b+=[rect(MX,178,(CW-24)//2,232,fill=GREENT,border=GREEN,bw=1.5),
    txt(MX+20,196,360,"纯静态 HTML 就够(你的默认)",14,GREEN,800),
    bullets(MX+20,228,(CW-24)//2-44,["一两个页面、一个聊天框","展示页、作品集、简单 demo","→ 一个 index.html + GitHub Pages"],14.5,lh=1.7)]
x2=MX+(CW-24)//2+24
b+=[rect(x2,178,(CW-24)//2,232,fill=NAVYT,border=NAVY,bw=1.5),
    txt(x2+20,196,360,"该上框架了",14,NAVY,800),
    bullets(x2+20,228,(CW-24)//2-44,["很多页面、要登录、要管很多状态","重复的界面块(卡片列表…)","要\"记住\"用户、复杂交互"],14.5,lh=1.7)]
b.append(txt(MX,430,CW,"原则:能静态就静态。别一上来就上重框架——那是给复杂项目的。",13,GREY,500))
b+=foot(18); P.append(page(b))

# 19 React
b=[kicker("W6 · React"),title("React:把界面拆成可复用的「积木」(组件)"),rule(112)]
b+=cards([("组件 component","一块可复用的界面","一个\"消息气泡\"写一次,到处用"),
          ("props","给组件传参数","同一个气泡,传不同文字/颜色"),
          ("state","组件的\"记忆\"","输入框里的字、聊天历史,变了自动重画")],
         178,158,accents=[NAVY,ACC,GREEN])
b.append(txt(MX,408,CW,"React 是目前最主流的前端库(2026 最新 React 19)。你不用手写,但要认得\"组件/状态\"这两个词。",13,GREY,500))
b+=foot(19); P.append(page(b))

# 20 Next.js
b=[kicker("W6 · Next.js"),title("Next.js:React 的「全能版」,前后端一体"),rule(112)]
b+=[txt(MX,176,(CW-24)//2,"它多给你什么:",14,NAVY,800),
    bullets(MX,208,(CW-24)//2,["<b>页面路由</b>:多页面自动管理","<b>前后端一体</b>:一个项目里既有界面又有 API","<b>SSR</b>:服务器先渲染好,首屏更快、更利于 SEO"],14,lh=1.7),
    txt(MX,322,(CW-24)//2,"2026 最新 Next.js 16(默认 Turbopack、React 编译器)。",12,GREY,500,lh=1.4)]
x2=MX+(CW-24)//2+24
b+=[rect(x2,176,(CW-24)//2,168,fill=PANEL,border=LINE,bw=1.3),
    txt(x2+18,192,300,"三个真实项目怎么选",13,NAVY,800),
    bullets(x2+18,222,(CW-24)//2-40,["小智:Next.js(静态导出)","Agent Leo:Next.js 14 全栈 + 账号","HEAI:纯 vanilla HTML(够简单)"],13,lh=1.75)]
b.append(txt(MX,360,CW,"看出规律没?越复杂 → 越可能上 Next.js;够简单 → 纯 HTML 反而更省心。",13,GREY,500))
b+=foot(20); P.append(page(b))

# 21 SECTION W7
P.append(section("PART 05","后端与服务器","Node.js · Python · FastAPI —— 藏 key、跑逻辑、连模型","后端 = 一直在线、替你保管秘密、干重活的那台机器"))

# 22 node vs python
b=[kicker("W7 · 后端用什么写"),title("后端:一个「一直在线接电话」的程序"),rule(112)]
b+=[rect(MX,178,(CW-24)//2,232,fill=NAVYT,border=NAVY,bw=1.5),
    txt(MX+20,196,360,"Node.js(用 JavaScript 写后端)",14,NAVY,800),
    bullets(MX+20,228,(CW-24)//2-44,["前端也是 JS → 一种语言通吃","Next.js/Vercel 的原生路线","生态大、部署方便"],14.5,lh=1.7)]
x2=MX+(CW-24)//2+24
b+=[rect(x2,178,(CW-24)//2,232,fill="#FBF1EC",border=ACC,bw=1.6),
    txt(x2+20,196,360,"Python + FastAPI(你的默认)",14,ACC,800),
    bullets(x2+20,228,(CW-24)//2-44,["你在 0_agent_basic 已经会 Python","FastAPI = 最短路径把 Python 变 API","Railway 自动识别、= HEAI 同款"],14.5,lh=1.7)]
b.append(txt(MX,430,CW,"两条路都行。本课默认 Python+FastAPI,因为你已经会 Python、心智不用切换。",13,GREY,500))
b+=foot(22); P.append(page(b))

# 23 FastAPI anatomy
b=[kicker("W7 · FastAPI 拆解"),title("你运行示例的后端,其实就几行"),rule(112)]
b+=code(MX,176,548,176,'app = FastAPI()<br><br>@app.get("/api/health")<br>def health():<br>&nbsp;&nbsp;return {"status": "ok"}<br><br>@app.post("/api/chat")<br>def chat(body):<br>&nbsp;&nbsp;reply = run_harness(body.messages)<br>&nbsp;&nbsp;return {"reply": reply}')
x2=MX+548+16
b+=[txt(x2,176,CW-548-16,"认得三样:",13,NAVY,800),
    bullets(x2,204,CW-548-16,["@app.get/post = 开一道菜","里面 = 收到请求做什么","return {…} = 回 JSON"],12.5,lh=1.7),
    txt(x2,320,CW-548-16,"key 从 os.environ 读,不写死。",12,ACC,600,lh=1.4)]
b.append(txt(MX,362,CW,"← 这就是 backend/main.py 的骨架。后端职责:藏 key、跑你的 agent(harness)、连模型。",13,GREY,500))
b+=foot(23); P.append(page(b))

# 24 data storage
b=[kicker("W7 · 数据与存储"),title("要不要数据库?多数课堂项目:先不要"),rule(112)]
b+=cards([("先用文件/内存","够简单就别上数据库","端到端示例:日记存文件即可"),
          ("何时要数据库","要长期记住很多用户/历史","账号、跨设备、大量数据"),
          ("Supabase 一瞥","最省事的托管数据库","Agent Leo 用它存账号+对话")],
         178,158,accents=[GREEN,NAVY,ACC])
b.append(txt(MX,408,CW,"原则:先跑起来,别过早上数据库。真需要了(要账号/要长期存),再加 Supabase 这类托管方案。",13,GREY,500))
b+=foot(24); P.append(page(b))

# 25 SECTION W8
P.append(section("PART 06","工具链 · 报错 · 红线","终端 / npm·pip / git / DevTools —— 你要认得的工程环境","最后一块拼图:看懂工具、读懂报错、守住安全"))

# 26 toolchain
b=[kicker("W8 · 工程工具链"),title("这些黑框框和命令,是什么"),rule(112)]
b+=cards([("终端 Terminal","打字给电脑下命令的黑框","uvicorn … / npm run dev 都在这跑"),
          ("包管理","一键装别人写好的轮子","npm(JS)· pip(Python)· requirements.txt"),
          ("git / GitHub","代码的存档与云端仓库","push 上去,Pages/Railway 才能部署")],
         178,158,accents=[NAVY,ACC,GREEN])
b.append(txt(MX,408,CW,"你不用记命令——Claude Code 会给你。但要认得:这是终端、那是在装依赖、那是在提交代码。",13,GREY,500))
b+=foot(26); P.append(page(b))

# 27 devtools
b=[kicker("W8 · 浏览器 DevTools"),title("按 F12:排错的「透视镜」"),rule(112)]
b+=cards([("查看源代码","右键→查看源码","验证前端有没有泄漏 key(能看到=公开)"),
          ("Console 控制台","看 JS 报错的地方","红字报错先截图给 Claude Code"),
          ("Network 网络","看每个请求成没成","看 /api/chat 是 200 还是 404/500")],
         178,158,accents=[ACC,RED,NAVY])
b+=[rect(MX,408,CW,44,fill="#FBECEA",border=RED,bw=1.4),
    txt(MX+18,420,CW-36,"「前端是公开的」不是口号:DevTools 右键就能看到你前端的一切 —— 所以 key 只能在后端。",13,RED,700,lh=1.3)]
b+=foot(27); P.append(page(b))

# 28 read errors
b=[kicker("W8 · 看懂常见报错"),title("四个最常见的坑,一眼认出"),rule(112)]
rows=[("白屏 / 转圈不动","前端崩了或后端没连上",ACC,"看 Console 红字 + Network 有没有失败"),
      ("CORS 报错","后端没允许前端域名跨域",NAVY,"后端 CORS_ORIGINS 加上前端网址"),
      ("404","地址/端点写错",ACC,"检查前端 fetch 的 URL 对不对"),
      ("500","后端内部崩了",RED,"去 Railway 看后端日志找异常")]
y0=170; rh=58
for i,(t,c,acc,fix) in enumerate(rows):
    y=y0+i*rh
    b.append(rect(MX,y,CW,rh-8,fill="#FFFFFF",border=LINE,bw=1.2)); b.append(vline(MX,y,rh-8,acc,4))
    b.append(txt(MX+18,y+13,220,t,14,acc,800))
    b.append(txt(MX+250,y+9,300,c,12.5,INK,500,lh=1.3))
    b.append(txt(MX+250,y+27,CW-270,"→ "+fix,12,GREY,500,lh=1.2))
b.append(txt(MX,y0+4*rh+2,CW,"看懂报错 = 会指挥的一半:你能对 AI 说清\"哪一层、什么错\",它就修得快。",13,GREY,500))
b+=foot(28); P.append(page(b))

# 29 red lines + checklist
b=[kicker("W8 · 结课清单"),title("「看懂 + 会指挥」你现在应该能做到"),rule(112)]
b+=[rect(MX,170,CW,246,fill="#FFFFFF",border=LINE,bw=1.4)]
col=(CW-44)//2
b.append(bullets(MX+24,190,col-10,["说得清前端/后端/模型各是什么、住哪","看懂一个网页的 HTML/CSS/JS 三段","知道 fetch = 前端调后端 /api/chat"],14,GREEN,lh=2.0))
b.append(bullets(MX+24+col,190,col-10,["认得 JSON、API、200/404/500","知道何时纯静态、何时上框架","报错时看 Console/Network,说清哪层错"],14,GREEN,lh=2.0))
b+=[rect(MX,428,CW,26,fill="#FBECEA",border=RED,bw=1.2),
    txt(MX+16,433,CW-30,"🔑 唯一铁律:前端是公开的,key 只能待在后端。",12.5,RED,800)]
b+=foot(29); P.append(page(b))

# 30 closing
P.append(page([rect(0,0,W,6,fill=NAVY),
    txt(MX,116,CW,"带走一句话",13,NAVY,700,ls="2px"),rule(152,MX,72),
    txt(MX,178,CW-40,"「你不用会写代码,",34,INK,800,lh=1.32),
    txt(MX,224,CW-40,"但要看懂 AI 写了什么、",34,INK,800,lh=1.32),
    txt(MX,270,CW-40,"知道每一层是什么、错在哪。」",34,ACC,800,lh=1.32),
    txt(MX,360,CW,"看懂了这一层,你就能真正「指挥」Claude Code,而不是被它牵着走。",16,GREY,500),
    txt(MX,404,CW,"下一步:回到 2_dev_deploy_guide 的 B1–B4,把你的项目真正做出来。",14,NAVY,600),
    txt(MX,470,CW,"郑先隽 · 北京师范大学心理学部 · 人本 AI 设计与创新",13,GREY,400)]))

HERE=os.path.dirname(os.path.abspath(__file__)); d=os.path.join(HERE,"html_web_basics"); os.makedirs(d,exist_ok=True)
for i,html in enumerate(P,1): open(os.path.join(d,f"{i:02d}.html"),"w",encoding="utf-8").write(html)
print(f"{len(P)} pages")
