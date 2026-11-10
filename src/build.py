#!/usr/bin/env python3
# Gerador descartável: copy.json + fatos -> /Users/jester/destrava-landing/index.html (standalone)
# e <scratchpad>/artifact.html (fragmento para o Artifact). Não faz parte da entrega.
import json, html, re, pathlib
HERE = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path('/Users/jester/destrava-landing')
src = HERE / 'copy.json'
C = json.loads((src if src.exists() else HERE / 'copy_fallback.json').read_text(encoding='utf-8'))
E = lambda s: html.escape(str(s), quote=True)

WA = '5591985394274'
MODULES = [
 ('Fundamentos do mercado digital', ['Funcionamento do mercado digital', 'Modelos de negócios', 'Comportamento do consumidor', 'Identificação de oportunidades']),
 ('Infoprodutos', ['O que são infoprodutos', 'Tipos de produtos digitais', 'Criação e validação de ideias', 'Estruturação de ofertas', 'Comercialização']),
 ('Estrutura digital', ['Plataformas de venda', 'Landing pages', 'Checkout', 'Ferramentas digitais', 'Organização de um negócio']),
 ('Tráfego pago', ['Introdução ao tráfego pago', 'Meta Ads', 'Públicos e segmentação', 'Criativos e campanhas', 'Orçamento e métricas']),
 ('Crescimento e oportunidades', ['Análise de resultados', 'Otimização', 'Identificação de oportunidades', 'Desenvolvimento de projetos', 'Próximos passos']),
]
COMPARE = [
 ('Formação e conteúdo',), ('Total de aulas', '15', '20'), ('15 aulas principais gravadas', 1, 1), ('Formação em infoprodutos', 1, 1),
 ('Conteúdo sobre tráfego pago', 1, 1), ('Estudos de oportunidades de mercado', 1, 1), ('Certificado digital de conclusão', 1, 1),
 ('Acompanhamento',), ('Grupo exclusivo no WhatsApp', 1, 1), ('Suporte durante a mentoria', 1, 1), ('30 dias de atendimento após a conclusão', 'Gratuito', 'Prioritário'),
 ('Direcionamento individual e conexão',), ('5 aulas bônus exclusivas', 0, 1), ('Networking VIP exclusivo', 0, 1), ('4 encontros coletivos ao vivo', 0, 1),
 ('Sessão individual de 30 minutos', 0, 1), ('Análise personalizada', 0, 1), ('Plano de ação de 30 dias', 0, 1), ('Feedback estratégico', 0, 1), ('Biblioteca exclusiva', 0, 1),
 ('Implementação',), ('Landing page personalizada', 0, 1),
]
ANCHOR = ['Sessão individual de 30 min', 'Análise personalizada', 'Plano de ação de 30 dias', 'Feedback estratégico', 'Landing page personalizada', '4 encontros ao vivo', '20 aulas (5 bônus)', 'Networking VIP', 'Biblioteca exclusiva']
TICKER = [m[0] for m in MODULES] + ['15 aulas gravadas', 'Grupo no WhatsApp', 'Certificado digital', '4 encontros ao vivo no Pro', 'Landing page personalizada no Pro', '7 dias de garantia']

ICO = {
 'check': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 4.5 4.5L19 7"/></svg>',
 'x': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>',
 'arrow': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>',
 'shield': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 4 6v6c0 5 3.5 8.5 8 9 4.5-.5 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/></svg>',
 'users': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17" cy="9" r="3"/><path d="M15.5 14.5A5.5 5.5 0 0 1 21.5 20"/></svg>',
 'book': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M4 5h7a3 3 0 0 1 3 3v12a2 2 0 0 0-2-2H4z"/><path d="M20 5h-7a3 3 0 0 0-3 3v12a2 2 0 0 1 2-2h8z"/></svg>',
 'compass': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="m15 9-2 6-4 2 2-6z"/></svg>',
 'bolt': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M13 2 4 14h6l-1 8 9-12h-6z"/></svg>',
 'wa': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.3.8 3.2.7a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>',
}

def li(items, ico):
    return ''.join(f'<li>{ICO[ico]}<span>{E(t)}</span></li>' for t in items)

def stats():
    out = []
    for s in C['hero']['stats']:
        v = str(s['value']).strip()
        num = re.fullmatch(r'\d+', v)
        b = f'<b data-count="{v}">{v}</b>' if num else f'<b>{E(v)}</b>'
        out.append(f'<div class="stat">{b}<span>{E(s["label"])}</span></div>')
    return ''.join(out)

def pillars():
    icos = ['book', 'compass', 'bolt']
    return ''.join(f'<article class="pillar"><span class="ico">{ICO[icos[i]]}</span><h3>{E(p["title"])}</h3><p>{E(p["text"])}</p></article>' for i, p in enumerate(C['method']['pillars'][:3]))

def modules():
    out = []
    for i, (fact, bullets) in enumerate(MODULES):
        cp = C['modules']['items'][i] if i < len(C['modules']['items']) else {'title': fact, 'text': ''}
        title = re.sub(r'^\s*M[óo]dulo\s*0?\d+\s*[—–:\-]\s*', '', cp.get('title') or fact) or fact
        sub = '' if title.strip().lower() == fact.lower() else f'<span class="fact">{E(fact)}</span>'
        out.append(f'<article class="mod"><span class="n">Módulo 0{i+1}</span><h3>{E(title)}</h3>{sub}<p>{E(cp.get("text",""))}</p><ul>' + ''.join(f'<li>{E(b)}</li>' for b in bullets) + '</ul></article>')
    return ''.join(out)

def steps():
    out = []
    for i, st in enumerate(C['journey']['steps'][:6]):
        t = re.sub(r'^\s*Etapa\s*\d+\s*[—–:\-]\s*', '', st['title']) or st['title']
        out.append(f'<article class="step"><span class="n">{i+1}</span><h3>{E(t)}</h3><p>{E(st["text"])}</p></article>')
    return ''.join(out)

def compare():
    def cell(v):
        if v == 1: return f'<td class="c"><span class="y" aria-label="Incluído">{ICO["check"]}</span></td>'
        if v == 0: return '<td class="c"><span class="n" aria-label="Não incluído">—</span></td>'
        return f'<td class="c">{E(v)}</td>'
    out = []
    for r in COMPARE:
        if len(r) == 1: out.append(f'<tr class="g"><td colspan="3">{E(r[0])}</td></tr>')
        else: out.append(f'<tr><td>{E(r[0])}</td>{cell(r[1])}{cell(r[2]).replace("<td ", "<td data-pr ", 1)}</tr>')
    return ''.join(out)

def faq():
    out = []
    for i, f in enumerate(C['faq']):
        out.append(f'<div class="fq"><button type="button" aria-expanded="false" aria-controls="fa{i}" id="fq{i}"><span>{E(f["q"])}</span><i aria-hidden="true"></i></button><div class="a" id="fa{i}" role="region" aria-labelledby="fq{i}"><div><p>{E(f["a"])}</p></div></div></div>')
    return ''.join(out)

ticker_items = ''.join(f'<span>{E(t)}</span>' for t in TICKER)
FR = {
 '#stats': stats(), '#pillars': pillars(), '#modules': modules(), '#steps': steps(), '#compare': compare(), '#faq': faq(),
 '#pain_ps': ''.join(f'<p>{E(p)}</p>' for p in C['pain']['paragraphs']),
 '#outcomes': li(C['outcomes']['items'], 'check'),
 '#fit_yes': li(C['fit']['yes'], 'check'), '#fit_no': li(C['fit']['no'], 'x'),
 '#ess_feats': li(C['plans']['essencial']['features'], 'check'), '#pro_feats': li(C['plans']['pro']['features'], 'check'),
 '#anchor': ''.join(f'<li>{E(a)}</li>' for a in ANCHOR),
 '#ticker': ticker_items + ticker_items,
 '#weeks': ''.join(f'<i style="--i:{i}"></i>' for i in range(8)),
 '#ico_arrow': ICO['arrow'], '#ico_shield': ICO['shield'], '#ico_users': ICO['users'], '#ico_wa': ICO['wa'],
}

_c2 = C['hero']['cta_secondary']
FR['#hero_cta2'] = (f'<a class="btn" data-wa href="#planos">{ICO["wa"]} {E(_c2)}</a>' if 'whatsapp' in _c2.lower() else f'<a class="btn" href="#metodo">{E(_c2)}</a>')
_st = [x.strip() for x in C['sticky']['text'].split('·') if x.strip()]
if len(_st) > 1:
    _main = next((x for x in _st if ('R' + chr(36)) in x), _st[0]); _rest = [x for x in _st if x != _main]
    FR['#sticky'] = f'<div class="t">{E(_main[:1].upper() + _main[1:])}<small>{E(" · ".join(_rest))}</small></div>'
else:
    FR['#sticky'] = f'<div class="t">{E(C["sticky"]["text"])}<small>7 dias de garantia incondicional</small></div>'

CSS = r"""
/* Layout: editorial escuro, texto alinhado à esquerda, wrap de 1180px; hero em 2 colunas (copy + pilha 3D de entregáveis); o card Pro é o segundo herói */
:root{color-scheme:dark;
 --bg:#060B16;--bg-2:#0A1222;--card:#0E1829;--card-2:#13203A;
 --line:rgba(140,170,255,.13);--line-2:rgba(140,170,255,.26);
 --fg:#F2F5FB;--mut:#93A0B8;--dim:#5F6C84;--bad:#FF6B6B;
 --brand:#2B7FFF;--brand-2:#6CB6FF;--brand-ink:#0B2A66;
 --hot:#FFB224;--hot-2:#FFC94D;--hot-ink:#1A1200;
 --display:'Sora',system-ui,sans-serif;--body:'Inter',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
 --wrap:1180px;--gut:max(16px,env(safe-area-inset-left,0px));--gutr:max(16px,env(safe-area-inset-right,0px));
 --r:14px;--r-lg:22px;--ease:cubic-bezier(.22,1,.36,1)}
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:84px;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:400 1rem/1.6 var(--body);overflow-x:clip}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:60;background:var(--bg)}
img,svg{max-width:100%;display:block}
h1,h2,h3,h4{font-family:var(--display);margin:0;text-wrap:balance;letter-spacing:-.02em}
p{margin:0}a{color:inherit}ul{margin:0;padding:0;list-style:none}
button{font:inherit;color:inherit;background:none;border:0;padding:0;cursor:pointer}
:focus-visible{outline:2px solid var(--brand-2);outline-offset:3px;border-radius:6px}
.wrap{width:min(var(--wrap),100%);margin-inline:auto;padding-left:var(--gut);padding-right:var(--gutr)}
.sec{padding-block:clamp(72px,9vw,120px)}
.sec.alt{background:var(--bg-2)}
.head{max-width:740px;display:grid;gap:14px;margin-bottom:clamp(36px,5vw,56px)}
.eyebrow{display:inline-flex;align-items:center;gap:10px;color:var(--brand-2);font:600 .875rem/1.3 var(--body)}
.eyebrow::before{content:"";width:22px;height:2px;flex:none;background:var(--brand);border-radius:2px}
h2{font-size:clamp(1.9rem,3.4vw,2.85rem);font-weight:700;line-height:1.08}
.lead{color:var(--mut);font-size:clamp(1.02rem,1.4vw,1.15rem);max-width:60ch}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:52px;padding:14px 26px;border-radius:12px;font:600 1rem/1.2 var(--body);text-align:center;text-decoration:none;border:1px solid var(--line-2);color:var(--fg);background:rgba(255,255,255,.03);transition:transform .25s var(--ease),background .25s,border-color .25s,box-shadow .25s;position:relative;overflow:hidden}
.btn:hover{transform:translateY(-2px);border-color:var(--brand-2);background:rgba(43,127,255,.12)}
.btn svg{width:18px;height:18px;flex:none}
.btn.hot{background:var(--hot);color:var(--hot-ink);border-color:transparent;box-shadow:0 10px 30px -10px rgba(255,178,36,.55)}
.btn.hot:hover{background:var(--hot-2);box-shadow:0 16px 40px -12px rgba(255,178,36,.7)}
.btn.hot::after{content:"";position:absolute;top:0;bottom:0;width:40%;left:-60%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.55),transparent);transform:skewX(-20deg);animation:shine 4.5s var(--ease) infinite;pointer-events:none}
@keyframes shine{0%,60%{left:-60%}100%{left:140%}}
/* nav */
.nav{position:sticky;top:env(safe-area-inset-top,0px);z-index:50;backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);background:rgba(6,11,22,.55);border-bottom:1px solid transparent;transition:background .3s,border-color .3s}
.nav.on{background:rgba(6,11,22,.86);border-color:var(--line)}
.nav .wrap{display:flex;align-items:center;justify-content:space-between;gap:20px;min-height:68px}
.brand{display:inline-flex;align-items:center;gap:10px;font:700 .95rem/1 var(--display);letter-spacing:.08em;text-decoration:none;white-space:nowrap}
.brand i{width:10px;height:10px;border-radius:50%;background:var(--brand-2);box-shadow:0 0 0 4px rgba(108,182,255,.18),0 0 18px var(--brand-2)}
.nav ul{display:flex;gap:28px}
.nav ul a{color:var(--mut);text-decoration:none;font-size:.95rem;transition:color .2s}
.nav ul a:hover{color:var(--fg)}
.nav .btn{min-height:42px;padding:8px 18px;font-size:.9rem;white-space:nowrap}
.prog{position:absolute;left:0;bottom:-1px;height:2px;width:100%;transform-origin:0 50%;transform:scaleX(0);background:linear-gradient(90deg,var(--brand),var(--brand-2),var(--hot))}
/* hero */
.hero{position:relative;overflow:hidden;padding-block:clamp(56px,8vw,110px) clamp(48px,6vw,80px)}
.hero::before{content:"";position:absolute;inset:-20% -10% auto;height:85%;background:radial-gradient(55% 55% at 72% 35%,rgba(43,127,255,.3),transparent 70%),radial-gradient(35% 40% at 12% 75%,rgba(255,178,36,.09),transparent 70%);filter:blur(12px);pointer-events:none;animation:breathe 9s ease-in-out infinite}
.hero::after{content:"";position:absolute;inset:0;background-image:linear-gradient(var(--line) 1px,transparent 1px),linear-gradient(90deg,var(--line) 1px,transparent 1px);background-size:64px 64px;-webkit-mask-image:radial-gradient(70% 60% at 50% 20%,#000 20%,transparent 80%);mask-image:radial-gradient(70% 60% at 50% 20%,#000 20%,transparent 80%);opacity:.35;pointer-events:none}
@keyframes breathe{50%{opacity:.7;transform:scale(1.06)}}
.hero .wrap{position:relative;z-index:1;display:grid;grid-template-columns:1.05fr .95fr;gap:clamp(32px,5vw,72px);align-items:center}
.hero .copy>*{opacity:0;animation:rise .9s var(--ease) forwards}
.hero .copy .eyebrow{animation-delay:.1s}
.hero .copy h1{opacity:1;animation:none}
.hero .copy .lead{animation-delay:.8s;margin-top:22px;max-width:52ch}
.hero .copy .ctas{animation-delay:.95s}
.hero .copy .stats{animation-delay:1.15s}
.hero h1{margin-top:18px;font-size:clamp(2.35rem,5.4vw,4.4rem);font-weight:800;line-height:1.02;letter-spacing:-.035em}
.hero h1 .w{display:inline-block;opacity:0;transform:translateY(.6em) rotate(2deg);animation:rise .9s var(--ease) forwards;animation-delay:calc(.25s + var(--i)*.055s)}
@keyframes rise{to{opacity:1;transform:none}}
.ctas{display:flex;flex-wrap:wrap;gap:12px;margin-top:32px}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:0 18px;margin-top:44px;border-top:1px solid var(--line)}
.stat{padding-top:18px;display:grid;gap:4px;align-content:start}
.stat b{font:700 clamp(1.7rem,2.6vw,2.3rem)/1 var(--display);letter-spacing:-.03em;font-variant-numeric:tabular-nums}
.stat span{color:var(--mut);font-size:.85rem;line-height:1.3}
.viz{position:relative;height:clamp(380px,42vw,520px);perspective:1200px;perspective-origin:50% 40%}
.stack{position:absolute;inset:0;transform-style:preserve-3d;transform:rotateX(var(--rx,12deg)) rotateY(var(--ry,-16deg));transition:transform .6s var(--ease)}
.dcard{position:absolute;left:50%;top:46%;width:min(300px,78%);padding:16px 18px;border-radius:16px;background:linear-gradient(160deg,rgba(19,32,58,.96),rgba(14,24,41,.96));border:1px solid var(--line-2);box-shadow:0 30px 60px -30px rgba(0,0,0,.85),inset 0 1px 0 rgba(255,255,255,.06);display:grid;gap:10px;transform:translate(-50%,-50%) translate3d(var(--x),var(--y),var(--z));opacity:0;animation:drop 1s var(--ease) forwards,float 7s ease-in-out infinite;animation-delay:calc(.5s + var(--k)*.22s),calc(1.5s + var(--k)*.5s)}
@keyframes drop{from{opacity:0;transform:translate(-50%,-50%) translate3d(var(--x),calc(var(--y) + 70px),var(--z))}to{opacity:1;transform:translate(-50%,-50%) translate3d(var(--x),var(--y),var(--z))}}
@keyframes float{50%{translate:0 -8px}}
.dc-h{display:flex;align-items:center;gap:10px;font:600 .9rem/1 var(--body)}
.dc-h .dot{width:8px;height:8px;border-radius:50%;background:var(--brand-2);box-shadow:0 0 12px var(--brand-2)}
.dc-h em{margin-left:auto;font:500 .72rem/1 var(--body);font-style:normal;color:var(--hot);padding:5px 8px;border-radius:999px;background:rgba(255,178,36,.12)}
.bar{height:8px;border-radius:4px;background:rgba(140,170,255,.18);transform-origin:0 50%;animation:grow .9s var(--ease) both;animation-delay:calc(1.1s + var(--k)*.22s + var(--j,0)*.1s)}
.bar.hot{background:var(--hot);height:22px;width:38%;border-radius:7px;margin-top:4px}
@keyframes grow{from{transform:scaleX(0)}}
.cols{display:flex;align-items:flex-end;gap:7px;height:56px;margin-top:4px}
.cols span{flex:1;border-radius:4px 4px 2px 2px;background:linear-gradient(180deg,var(--brand-2),var(--brand));height:var(--h);transform-origin:50% 100%;animation:grow-y 1s var(--ease) both;animation-delay:calc(1.6s + var(--j)*.1s)}
.cols span:last-child{background:linear-gradient(180deg,var(--hot-2),var(--hot))}
@keyframes grow-y{from{transform:scaleY(0)}}
.viz .cap{position:absolute;left:0;right:0;bottom:-10px;text-align:center;color:var(--dim);font-size:.82rem;opacity:0;animation:rise .9s var(--ease) 2s forwards}
/* ticker */
.ticker{border-block:1px solid var(--line);background:var(--bg-2);overflow:hidden;padding-block:14px}
.ticker .track{display:flex;gap:48px;width:max-content;animation:scroll 36s linear infinite}
.ticker:hover .track{animation-play-state:paused}
.ticker span{display:inline-flex;align-items:center;gap:14px;color:var(--mut);font:500 .9rem/1 var(--body);white-space:nowrap}
.ticker span::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--hot)}
@keyframes scroll{to{transform:translateX(-50%)}}
/* reveals */
.js .rv{opacity:0;transform:translateY(26px);transition:opacity .8s var(--ease),transform .8s var(--ease)}
.js .rv.on{opacity:1;transform:none}
.js .rv-g>*{opacity:0;transform:translateY(22px);transition:opacity .7s var(--ease),transform .7s var(--ease),border-color .35s,box-shadow .35s}
.js .rv-g.on>*{opacity:1;transform:none}
/* dor */
.pain .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(32px,5vw,80px);align-items:start}
.pain h2{font-size:clamp(2rem,4vw,3.3rem);margin-top:14px}
.pain .ps{display:grid;gap:18px;color:var(--mut);font-size:1.08rem}
.pain .ps p{padding-left:18px;border-left:2px solid var(--line-2)}
.punch{margin-top:28px;font:700 clamp(1.3rem,2.2vw,1.7rem)/1.25 var(--display);letter-spacing:-.02em;color:var(--fg);padding:22px 26px;border-radius:var(--r-lg);background:linear-gradient(135deg,rgba(255,178,36,.14),rgba(255,178,36,.03));border:1px solid rgba(255,178,36,.3)}
/* método */
.pillars{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.pillar{padding:28px;border-radius:var(--r-lg);background:var(--card);border:1px solid var(--line);display:grid;gap:12px;align-content:start;position:relative;overflow:hidden}
.pillar::before{content:"";position:absolute;right:-20%;bottom:-40%;width:60%;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,rgba(43,127,255,.22),transparent 65%);pointer-events:none}
.pillar .ico{width:44px;height:44px;border-radius:12px;display:grid;place-items:center;background:rgba(43,127,255,.14);color:var(--brand-2)}
.pillar .ico svg{width:22px;height:22px}
.pillar h3{font-size:1.25rem}
.pillar p{color:var(--mut)}
/* módulos */
.mods{display:grid;grid-template-columns:repeat(6,1fr);gap:18px}
.mod{grid-column:span 2;padding:26px;border-radius:var(--r-lg);background:var(--card);border:1px solid var(--line);display:grid;gap:10px;align-content:start}
.mod:nth-child(4),.mod:nth-child(5){grid-column:span 3}
.mod:hover{border-color:var(--line-2);box-shadow:0 24px 50px -30px rgba(43,127,255,.5)}
.mod .n{font:700 .8rem/1 var(--display);color:var(--brand-2);letter-spacing:.06em}
.mod h3{font-size:1.2rem}
.mod .fact{color:var(--dim);font-size:.85rem;margin-top:-6px}
.mod p{color:var(--mut)}
.mod ul{display:grid;gap:8px;margin-top:6px;padding-top:14px;border-top:1px solid var(--line)}
.mod li{font-size:.92rem;color:var(--mut);padding-left:18px;position:relative}
.mod li::before{content:"";position:absolute;left:0;top:.6em;width:8px;height:2px;background:var(--brand)}
/* resultados */
.outs{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.outs li{padding:20px;border-radius:var(--r);background:var(--card);border:1px solid var(--line);font-weight:500;display:grid;grid-template-columns:22px 1fr;gap:12px;align-items:start;line-height:1.45}
.outs li svg{width:22px;height:22px;color:var(--hot)}
.note{margin-top:18px;color:var(--dim);font-size:.85rem}
/* jornada */
.weeks{display:grid;grid-template-columns:repeat(8,1fr);gap:6px}
.weeks i{display:block;height:6px;border-radius:3px;background:var(--line-2);transform:scaleX(0);transform-origin:0 50%;transition:transform .6s var(--ease) calc(var(--i)*.12s),background .6s}
.js .rv:not(.on) .weeks i{transform:scaleX(0)}
.rv.on .weeks i,.no-js .weeks i{transform:scaleX(1);background:linear-gradient(90deg,var(--brand),var(--brand-2))}
.weeks-l{display:flex;justify-content:space-between;gap:12px;color:var(--dim);font-size:.8rem;margin:10px 0 28px}
.steps{display:grid;grid-template-columns:repeat(6,1fr);gap:18px}
.steps>*{grid-column:span 2}.steps>:nth-child(4),.steps>:nth-child(5){grid-column:span 3}.steps>:nth-child(5):last-child{grid-column:span 3}
.step{padding:24px;border-radius:var(--r-lg);border:1px solid var(--line);background:var(--card);display:grid;gap:8px;align-content:start}
.step .n{width:32px;height:32px;border-radius:50%;display:grid;place-items:center;background:rgba(43,127,255,.15);color:var(--brand-2);font:700 .85rem/1 var(--display)}
.step h3{font-size:1.08rem}
.step p{color:var(--mut);font-size:.95rem}
/* para quem */
.fit{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.fit-c{padding:30px;border-radius:var(--r-lg);border:1px solid var(--line);background:var(--card);display:grid;gap:16px;align-content:start}
.fit-c.no{background:transparent}
.fit-c h3{font-size:1.25rem}
.fit-c ul{display:grid;gap:12px}
.fit-c li{display:grid;grid-template-columns:22px 1fr;gap:12px;color:var(--mut);align-items:start}
.fit-c li svg{width:22px;height:22px;margin-top:1px}
.fit-c.yes li svg{color:var(--brand-2)}
.fit-c.no li svg{color:var(--bad)}
/* planos */
.plans .head{max-width:780px}
.pgrid{display:grid;grid-template-columns:.9fr 1.1fr;gap:22px;align-items:start}
.plan{position:relative;padding:34px;border-radius:26px;background:var(--card);border:1px solid var(--line);display:grid;gap:20px}
.plan h3{font-size:1.35rem}
.plan .tag{color:var(--mut);margin-top:-10px}
.price b{font:800 clamp(2.4rem,4vw,3.4rem)/1 var(--display);letter-spacing:-.04em;font-variant-numeric:tabular-nums}
.plan ul{display:grid;gap:12px;padding-top:22px;border-top:1px solid var(--line)}
.plan li{display:grid;grid-template-columns:20px 1fr;gap:12px;align-items:start;font-size:.97rem}
.plan li svg{width:20px;height:20px;color:var(--brand-2);margin-top:3px}
.plan .btn{width:100%}
.incl{color:var(--mut);font-size:.9rem;margin-bottom:-8px}
.plan.pro{background:linear-gradient(170deg,#13203A,#0C1628);border-color:transparent;isolation:isolate}
.plan.pro::before{content:"";position:absolute;inset:-1px;border-radius:27px;padding:1.5px;background:conic-gradient(from var(--a),var(--hot),var(--brand) 30%,transparent 55%,var(--brand-2) 80%,var(--hot));-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;animation:spin 6s linear infinite;z-index:-1}
.plan.pro::after{content:"";position:absolute;inset:0;border-radius:26px;box-shadow:0 40px 90px -40px rgba(43,127,255,.6);z-index:-2}
@property --a{syntax:'<angle>';inherits:false;initial-value:0deg}
@keyframes spin{to{--a:360deg}}
.plan.pro li svg{color:var(--hot)}
.badge{position:absolute;top:-14px;left:34px;background:var(--hot);color:var(--hot-ink);font:700 .78rem/1 var(--body);padding:8px 12px;border-radius:999px}
.anchor{margin-top:22px;padding:30px 34px;border-radius:26px;border:1px solid rgba(255,178,36,.3);background:linear-gradient(135deg,rgba(255,178,36,.12),rgba(43,127,255,.08));display:grid;grid-template-columns:auto 1fr;gap:20px 36px;align-items:center}
.anchor .big{font:800 clamp(2.4rem,4.5vw,3.6rem)/1 var(--display);letter-spacing:-.04em;color:var(--hot)}
.anchor .big small{display:block;font:500 .85rem/1.3 var(--body);color:var(--mut);letter-spacing:0;margin-bottom:8px}
.anchor ul{display:flex;flex-wrap:wrap;gap:8px}
.anchor li{padding:7px 12px;border-radius:999px;border:1px solid var(--line-2);font-size:.85rem}
.anchor p{grid-column:1/-1;color:var(--mut)}
/* comparação */
.tbl{overflow-x:auto;border:1px solid var(--line);border-radius:var(--r-lg);background:var(--card)}
table{width:100%;border-collapse:collapse;min-width:560px;font-size:.95rem}
th,td{padding:14px 18px;text-align:left;border-bottom:1px solid var(--line)}
th{font:600 .85rem/1.3 var(--body);color:var(--mut)}
th.pr,td[data-pr]{background:rgba(43,127,255,.08)}
th.c,td.c{text-align:center;font-weight:600}
td.c svg{width:20px;height:20px;margin:0 auto}
tr.g td{background:var(--bg-2);color:var(--brand-2);font:600 .8rem/1.3 var(--display);letter-spacing:.04em}
.y{color:var(--brand-2);display:inline-block}.n{color:var(--dim)}
tbody tr:last-child td{border-bottom:0}
/* vip */
.vip-box{display:grid;grid-template-columns:auto 1fr;gap:26px;align-items:center;padding:34px;border-radius:26px;border:1px solid var(--line);background:radial-gradient(80% 120% at 0% 50%,rgba(43,127,255,.18),transparent 60%),var(--card)}
.vip-box .ico{width:64px;height:64px;border-radius:18px;background:rgba(108,182,255,.12);display:grid;place-items:center;color:var(--brand-2)}
.vip-box .ico svg{width:30px;height:30px}
.vip-box h2{font-size:clamp(1.5rem,2.6vw,2.1rem);margin:8px 0 10px}
/* quem */
.who{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(32px,5vw,72px);align-items:center}
.who h2{margin:14px 0 18px}
.who .txt{display:grid;gap:18px;color:var(--mut);font-size:1.05rem}
.manifesto{font:700 clamp(1.3rem,2vw,1.6rem)/1.3 var(--display);letter-spacing:-.02em;color:var(--fg)}
.people{display:grid;gap:14px}
.person{display:flex;align-items:center;gap:16px;padding:18px 20px;border-radius:var(--r-lg);border:1px solid var(--line);background:var(--card)}
.av{width:52px;height:52px;flex:none;border-radius:14px;display:grid;place-items:center;background:linear-gradient(135deg,var(--brand),var(--brand-ink));font:700 .95rem/1 var(--display);color:#fff}
.person b{display:block;font-weight:600}.person span{color:var(--mut);font-size:.88rem}
/* garantia */
.gar{display:grid;grid-template-columns:auto 1fr auto;gap:28px;align-items:center;padding:36px;border-radius:26px;border:1px solid rgba(255,178,36,.35);background:linear-gradient(135deg,rgba(255,178,36,.1),transparent 60%),var(--card)}
.gar .ico{width:72px;height:72px;border-radius:20px;display:grid;place-items:center;background:rgba(255,178,36,.14);color:var(--hot)}
.gar .ico svg{width:36px;height:36px}
.gar h3{font-size:clamp(1.4rem,2.4vw,1.9rem)}
.gar p{color:var(--mut);margin-top:8px;max-width:60ch}
/* faq */
.faqs{max-width:820px;display:grid;gap:10px}
.fq{border:1px solid var(--line);border-radius:var(--r);background:var(--card);overflow:hidden;transition:border-color .3s}
.fq.open{border-color:var(--line-2)}
.fq button{width:100%;display:flex;justify-content:space-between;align-items:center;gap:16px;padding:20px 22px;text-align:left;font:600 1.02rem/1.35 var(--body)}
.fq button span{flex:1}
.fq button i{position:relative;width:28px;height:28px;border-radius:50%;border:1px solid var(--line-2);display:grid;place-items:center;flex:none;transition:transform .35s var(--ease),background .3s,border-color .3s}
.fq button i::before,.fq button i::after{content:"";position:absolute;width:12px;height:2px;background:currentColor;border-radius:2px}
.fq button i::after{transform:rotate(90deg)}
.fq.open button i{transform:rotate(45deg);background:rgba(43,127,255,.15);border-color:var(--brand)}
.fq .a{display:grid;grid-template-rows:0fr;transition:grid-template-rows .4s var(--ease)}
.fq .a>div{overflow:hidden}
.fq .a p{padding:0 22px 20px;color:var(--mut)}
.fq.open .a{grid-template-rows:1fr}
/* final */
.final{position:relative;overflow:hidden;text-align:center}
.final::before{content:"";position:absolute;inset:0;background:radial-gradient(50% 60% at 50% 100%,rgba(43,127,255,.32),transparent 70%);pointer-events:none}
.final .wrap{position:relative;display:grid;justify-items:center;gap:20px}
.final h2{font-size:clamp(2.1rem,4.6vw,3.6rem);max-width:18ch}
.final .lead{text-align:center}
.final .ctas{justify-content:center;margin-top:10px}
/* footer */
footer{border-top:1px solid var(--line);padding-block:44px 120px;color:var(--mut);font-size:.9rem}
footer .wrap{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:28px}
footer .tag{margin-top:14px;max-width:34ch}
footer h4{font:600 .85rem/1 var(--body);color:var(--fg);margin-bottom:14px}
footer ul{display:grid;gap:8px}footer a{text-decoration:none;color:var(--mut)}footer a:hover{color:var(--fg)}
footer li a{display:inline-flex;align-items:center;gap:8px}footer li svg{width:16px;height:16px}
.legal{grid-column:1/-1;display:flex;flex-wrap:wrap;justify-content:space-between;gap:10px 24px;padding-top:22px;border-top:1px solid var(--line);font-size:.82rem;color:var(--dim)}
.legal span:last-child{display:flex;gap:18px}
/* barra fixa */
.sticky{position:fixed;left:0;right:0;bottom:0;z-index:40;padding:10px var(--gutr) calc(10px + env(safe-area-inset-bottom,0px)) var(--gut);background:rgba(6,11,22,.84);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-top:1px solid var(--line);transform:translateY(110%);transition:transform .5s var(--ease)}
.sticky.show{transform:none}
.sticky .in{width:min(var(--wrap),100%);margin-inline:auto;display:flex;align-items:center;justify-content:space-between;gap:14px}
.sticky .t{font-weight:600;line-height:1.25;white-space:nowrap}.sticky .t small{display:block;color:var(--mut);font-weight:400;font-size:.82rem}
.sticky .btn{min-height:46px;padding:10px 20px;flex:none}
/* responsivo */
@media (max-width:1000px){
 .hero .wrap{grid-template-columns:1fr}.viz{height:clamp(380px,70vw,420px);width:min(520px,100%);justify-self:center;margin-bottom:48px}.viz .cap{bottom:auto;top:100%;margin-top:8px}
 .pain .wrap,.who{grid-template-columns:1fr}.outs,.steps{grid-template-columns:repeat(2,1fr)}.steps>*,.steps>:nth-child(4),.steps>:nth-child(5){grid-column:auto}.steps>:nth-child(odd):last-child{grid-column:1/-1}
 .pgrid{grid-template-columns:1fr}.plan.pro{order:-1}.gar{grid-template-columns:auto 1fr}.gar .btn{grid-column:1/-1}}
@media (max-width:860px){.nav ul{display:none}}
@media (max-width:720px){
 .stats{grid-template-columns:repeat(2,1fr);gap:8px 18px}.stat{padding-top:14px}
 .pillars,.fit,.mods,.steps{grid-template-columns:1fr}.steps>:nth-child(odd):last-child{grid-column:auto}.mod,.mod:nth-child(4),.mod:nth-child(5){grid-column:auto}
 .anchor,.vip-box,.gar{grid-template-columns:1fr}.gar .ico,.vip-box .ico{width:56px;height:56px}
 footer .wrap{grid-template-columns:1fr 1fr}.plan{padding:26px}.badge{left:26px}.sticky .t small{display:none}
 .anchor{padding:24px}.gar{padding:26px}.vip-box{padding:26px}}
@media (max-width:460px){
 footer .wrap{grid-template-columns:1fr}.outs{grid-template-columns:1fr}.ctas .btn{width:100%}
 .hero h1{font-size:clamp(2.1rem,11vw,2.6rem)}.nav .btn{padding:8px 14px}.dcard{width:min(240px,82%);padding:12px 14px}.cols{height:44px}}
@media (prefers-reduced-motion:reduce){
 html{scroll-behavior:auto}
 *,*::before,*::after{animation:none!important;transition:none!important}
 .js .rv,.js .rv-g>*,.hero .copy>*,.hero h1 .w,.viz .cap{opacity:1;transform:none}
 .dcard,.bar,.cols span{opacity:1}
 .weeks i,.js .rv:not(.on) .weeks i{transform:scaleX(1);background:linear-gradient(90deg,var(--brand),var(--brand-2))}
 .prog{display:none}}
"""

BODY = r"""
<header class="nav" id="top"><div class="wrap">
 <a class="brand" href="#top"><i aria-hidden="true"></i>DESTRAVA DIGITAL</a>
 <ul><li><a href="#metodo">A mentoria</a></li><li><a href="#modulos">Módulos</a></li><li><a href="#planos">Planos</a></li><li><a href="#comparar">Comparação</a></li><li><a href="#faq">Dúvidas</a></li></ul>
 <a class="btn hot nav-cta" href="#planos">Ver os planos</a>
 <span class="prog" aria-hidden="true"></span>
</div></header>
<main>
<section class="hero"><div class="wrap">
 <div class="copy">
  <span class="eyebrow">Mentoria de mercado digital em 8 semanas</span>
  <h1>[[hero.headline]]</h1>
  <p class="lead">[[hero.sub]]</p>
  <div class="ctas"><a class="btn hot" href="#planos">[[hero.cta_primary]] [[#ico_arrow]]</a>[[#hero_cta2]]</div>
  <div class="stats">[[#stats]]</div>
 </div>
 <div class="viz" aria-hidden="true"><div class="stack">
  <div class="dcard" style="--x:-90px;--y:-110px;--z:-80px;--k:0"><div class="dc-h"><span class="dot"></span>Oferta<em>definida</em></div><div class="bar" style="width:78%;--j:0"></div><div class="bar" style="width:52%;--j:1"></div></div>
  <div class="dcard" style="--x:-30px;--y:-30px;--z:-20px;--k:1"><div class="dc-h"><span class="dot"></span>Página<em>no ar</em></div><div class="bar" style="width:60%;--j:0"></div><div class="bar" style="width:92%;--j:1"></div><div class="bar" style="width:84%;--j:2"></div><div class="bar hot" style="--j:3"></div></div>
  <div class="dcard" style="--x:40px;--y:50px;--z:40px;--k:2"><div class="dc-h"><span class="dot"></span>Campanha<em>Meta Ads</em></div><div class="bar" style="width:70%;--j:0"></div><div class="bar" style="width:45%;--j:1"></div></div>
  <div class="dcard" style="--x:100px;--y:130px;--z:100px;--k:3"><div class="dc-h"><span class="dot"></span>Métricas<em>lidas</em></div><div class="cols"><span style="--h:30%;--j:0"></span><span style="--h:45%;--j:1"></span><span style="--h:38%;--j:2"></span><span style="--h:62%;--j:3"></span><span style="--h:55%;--j:4"></span><span style="--h:80%;--j:5"></span><span style="--h:100%;--j:6"></span></div></div>
 </div><p class="cap">Oferta, página, campanha e métricas: o que você aprende a construir.</p></div>
</div></section>
<div class="ticker" aria-hidden="true"><div class="track">[[#ticker]]</div></div>

<section class="sec pain" id="dor"><div class="wrap">
 <div class="rv"><span class="eyebrow">Por que agora</span><h2>[[pain.headline]]</h2></div>
 <div class="rv"><div class="ps">[[#pain_ps]]</div><p class="punch">[[pain.punch]]</p></div>
</div></section>

<section class="sec alt" id="metodo"><div class="wrap">
 <div class="head rv"><span class="eyebrow">O método</span><h2>[[method.headline]]</h2><p class="lead">[[method.sub]]</p></div>
 <div class="pillars rv-g">[[#pillars]]</div>
</div></section>

<section class="sec" id="modulos"><div class="wrap">
 <div class="head rv"><span class="eyebrow">O que você aprende</span><h2>[[modules.headline]]</h2><p class="lead">[[modules.sub]]</p></div>
 <div class="mods rv-g">[[#modules]]</div>
</div></section>

<section class="sec alt" id="resultados"><div class="wrap">
 <div class="head rv"><span class="eyebrow">Resultados de aprendizagem</span><h2>[[outcomes.headline]]</h2></div>
 <ul class="outs rv-g">[[#outcomes]]</ul>
 <p class="note">[[outcomes.disclaimer]]</p>
</div></section>

<section class="sec" id="jornada"><div class="wrap">
 <div class="head rv"><span class="eyebrow">Como funciona</span><h2>[[journey.headline]]</h2><p class="lead">[[journey.sub]]</p></div>
 <div class="rv"><div class="weeks" aria-hidden="true">[[#weeks]]</div><div class="weeks-l"><span>Semana 1: aulas 1 e 2</span><span>2 aulas gravadas por semana</span><span>Semana 8: aula 15 e fechamento</span></div></div>
 <div class="steps rv-g">[[#steps]]</div>
</div></section>

<section class="sec alt" id="para-quem"><div class="wrap">
 <div class="head rv"><span class="eyebrow">Para quem é</span><h2>[[fit.headline]]</h2></div>
 <div class="fit rv-g">
  <div class="fit-c yes"><h3>É para você se…</h3><ul>[[#fit_yes]]</ul></div>
  <div class="fit-c no"><h3>Não é para você se…</h3><ul>[[#fit_no]]</ul></div>
 </div>
</div></section>

<section class="sec plans" id="planos"><div class="wrap">
 <div class="head rv"><span class="eyebrow">Planos</span><h2>[[plans.headline]]</h2><p class="lead">[[plans.sub]]</p></div>
 <div class="pgrid rv-g">
  <article class="plan"><h3>Plano Essencial</h3><p class="tag">[[plans.essencial.tagline]]</p><div class="price"><b>R$ 794</b></div><ul>[[#ess_feats]]</ul><a class="btn" data-plan="Essencial" href="#planos">[[plans.essencial.cta]]</a></article>
  <article class="plan pro"><span class="badge">[[plans.pro.badge]]</span><h3>Plano Pro</h3><p class="tag">[[plans.pro.tagline]]</p><div class="price"><b>R$ 1.497</b></div><p class="incl">Tudo do Essencial, mais:</p><ul>[[#pro_feats]]</ul><a class="btn hot" data-plan="Pro" href="#planos">[[plans.pro.cta]] [[#ico_arrow]]</a></article>
 </div>
 <div class="anchor rv"><div class="big"><small>A diferença entre os planos é</small>R$ 703</div><ul>[[#anchor]]</ul><p>[[plans.anchor_note]]</p></div>
</div></section>

<section class="sec alt" id="comparar"><div class="wrap">
 <div class="head rv"><span class="eyebrow">Comparação</span><h2>O que muda de um plano para o outro, linha por linha.</h2></div>
 <div class="tbl rv"><table><thead><tr><th>O que está incluído</th><th class="c">Essencial</th><th class="c pr">Pro</th></tr></thead><tbody>[[#compare]]</tbody></table></div>
</div></section>

<section class="sec" id="vip"><div class="wrap">
 <div class="vip-box rv"><span class="ico">[[#ico_users]]</span><div><span class="eyebrow">Só no Pro</span><h2>[[vip.headline]]</h2><p class="lead">[[vip.text]]</p></div></div>
</div></section>

<section class="sec alt" id="quem"><div class="wrap"><div class="who">
 <div class="rv"><span class="eyebrow">Quem está por trás</span><h2>[[founders.headline]]</h2><div class="txt"><p>[[founders.text]]</p><p class="manifesto">[[founders.manifesto]]</p></div></div>
 <div class="people rv-g">
  <div class="person"><span class="av">JC</span><div><b>João Victor Crestani Castro</b><span>Responsável pela Destrava Digital</span></div></div>
  <div class="person"><span class="av">DR</span><div><b>Deyvid Rodrigues</b><span>Responsável pela Destrava Digital</span></div></div>
 </div>
</div></div></section>

<section class="sec" id="garantia"><div class="wrap">
 <div class="gar rv"><span class="ico">[[#ico_shield]]</span><div><h3>[[guarantee.headline]]</h3><p>[[guarantee.text]]</p></div><a class="btn hot" href="#planos">[[nav.cta]]</a></div>
</div></section>

<section class="sec alt" id="faq"><div class="wrap">
 <div class="head rv"><span class="eyebrow">Dúvidas</span><h2>Perguntas que você faria antes de decidir.</h2></div>
 <div class="faqs rv-g">[[#faq]]</div>
</div></section>

<section class="sec final"><div class="wrap rv">
 <span class="eyebrow">Decida agora</span><h2>[[final.headline]]</h2><p class="lead">[[final.sub]]</p>
 <div class="ctas"><a class="btn hot" href="#planos">[[final.cta_primary]] [[#ico_arrow]]</a><a class="btn" data-wa href="#planos">[[#ico_wa]] [[final.cta_secondary]]</a></div>
</div></section>
</main>
<footer><div class="wrap">
 <div><a class="brand" href="#top"><i aria-hidden="true"></i>DESTRAVA DIGITAL</a><p class="tag">[[footer.tagline]]</p></div>
 <div><h4>Navegação</h4><ul><li><a href="#metodo">A mentoria</a></li><li><a href="#modulos">Módulos</a></li><li><a href="#planos">Planos</a></li><li><a href="#comparar">Comparação</a></li><li><a href="#faq">Dúvidas</a></li></ul></div>
 <div><h4>Contato</h4><ul><li><a href="https://wa.me/5591985394274" target="_blank" rel="noopener">[[#ico_wa]] Deyvid Rodrigues · (91) 98539-4274</a></li></ul></div>
 <div class="legal"><span>© <span id="yr">2026</span> Destrava Digital. [[footer.disclaimer]]</span><span><a href="#">Termos de uso</a><a href="#">Política de privacidade</a></span></div>
</div></footer>
<div class="sticky" role="region" aria-label="Atalho para os planos"><div class="in">[[#sticky]]<a class="btn hot" href="#planos">Ver os planos</a></div></div>
"""

JS = r"""
(function(){
/* ===== CAMPOS EDITÁVEIS ===== */
var CONFIG={linkEssencial:"",linkPro:"",whatsapp:"__WA__"}; // links de pagamento vazios caem no WhatsApp
/* ============================ */
var d=document,root=d.documentElement;root.classList.add('js');
var rm=matchMedia('(prefers-reduced-motion:reduce)').matches;
var $=function(s,c){return (c||d).querySelector(s)},$$=function(s,c){return [].slice.call((c||d).querySelectorAll(s))};
var wa=function(t){return 'https://wa.me/'+CONFIG.whatsapp+'?text='+encodeURIComponent(t)};
$$('[data-plan]').forEach(function(a){var p=a.getAttribute('data-plan'),l=p==='Pro'?CONFIG.linkPro:CONFIG.linkEssencial;a.href=l||wa('Quero garantir o plano '+p+' da Destrava Digital.');a.target='_blank';a.rel='noopener'});
$$('[data-wa]').forEach(function(a){a.href=wa('Olá! Tenho uma dúvida sobre a Destrava Digital.');a.target='_blank';a.rel='noopener'});
var h1=$('.hero h1');if(h1){h1.innerHTML=h1.textContent.trim().split(/\s+/).map(function(w,i){return '<span class="w" style="--i:'+i+'">'+w+'</span>'}).join(' ')}
function count(b){if(b._done||rm)return;b._done=1;var end=parseInt(b.getAttribute('data-count'),10),t0=null,dur=1200;function step(ts){if(!t0)t0=ts;var p=Math.min(1,(ts-t0)/dur);p=1-Math.pow(1-p,3);b.textContent=Math.round(end*p);if(p<1)requestAnimationFrame(step)}requestAnimationFrame(step)}
setTimeout(function(){$$('.hero [data-count]').forEach(count)},1100);
function show(el){if(el.classList.contains('on'))return;if(el.classList.contains('rv-g'))[].forEach.call(el.children,function(c,i){c.style.transitionDelay=Math.min(i,10)*70+'ms'});el.classList.add('on');$$('[data-count]',el).forEach(count)}
var all=$$('.rv,.rv-g');
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){show(en.target);io.unobserve(en.target)}})},{threshold:.12,rootMargin:'0px 0px -6% 0px'});all.forEach(function(el){io.observe(el)});setTimeout(function(){all.forEach(function(el){if(el.getBoundingClientRect().top<innerHeight*1.25)show(el)})},2500)}else{all.forEach(show)}
addEventListener('beforeprint',function(){all.forEach(show)});
var nav=$('.nav'),prog=$('.prog'),sticky=$('.sticky'),hero=$('.hero'),planos=$('#planos'),foot=$('footer'),tick=false;
function onScroll(){tick=false;var y=scrollY,h=root.scrollHeight-innerHeight;nav.classList.toggle('on',y>12);prog.style.transform='scaleX('+(h?y/h:0)+')';var hb=hero.getBoundingClientRect().bottom,pr=planos.getBoundingClientRect(),fr=foot.getBoundingClientRect();var inPlans=pr.top<innerHeight*.6&&pr.bottom>innerHeight*.4;sticky.classList.toggle('show',hb<0&&!inPlans&&fr.top>innerHeight)}
addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(onScroll)}},{passive:true});onScroll();
$$('.fq button').forEach(function(b){b.addEventListener('click',function(){var it=b.parentNode,o=it.classList.toggle('open');b.setAttribute('aria-expanded',o)})});
if(!rm&&matchMedia('(hover:hover) and (pointer:fine)').matches){var st=$('.stack');hero.addEventListener('pointermove',function(e){var r=hero.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;st.style.setProperty('--ry',(-16+x*12)+'deg');st.style.setProperty('--rx',(12-y*10)+'deg')});hero.addEventListener('pointerleave',function(){st.style.removeProperty('--ry');st.style.removeProperty('--rx')})}
$('#yr').textContent=new Date().getFullYear();
})();
""".replace('__WA__', WA)

def fill(tpl):
    def rep(m):
        k = m.group(1)
        if k in FR: return FR[k]
        cur = C
        for part in k.split('.'): cur = cur[part]
        return E(cur)
    return re.sub(r'\[\[([#a-z0-9_.]+)\]\]', rep, tpl)

body = fill(BODY)
title, desc = E(C['meta']['title']), E(C['meta']['description'])
ICON = '''<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='10' fill='%236CB6FF'/%3E%3C/svg%3E">'''
FONT = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'

standalone = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#060B16">
{ICON}
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
{FONT}
<style>{CSS}</style>
</head>
<body>{body}
<script>{JS}</script>
</body>
</html>
"""
fragment = f"""<title>Destrava Digital</title>
<meta name="description" content="{desc}">
<meta name="claude:viewport-fit-sides" content="cover">
{ICON}
{FONT}
<style>{CSS}</style>
{body}
<script>{JS}</script>
"""
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'index.html').write_text(standalone, encoding='utf-8')
(HERE / 'artifact.html').write_text(fragment, encoding='utf-8')
left = re.findall(r'\[\[[^\]]+\]\]', standalone)
print('ok', len(standalone), 'bytes; tokens restantes:', left)
