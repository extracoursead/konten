# Selamat Natal (25 Des 2026): satu gambar, latar navy, satu lilin menyala di tatakan. Tenang, tanpa hiasan lain.
# Render: python3 build.py  (butuh Playwright + font di ../gf/)
import os
from playwright.sync_api import sync_playwright

NAME = '2026-12-25-selamat-natal'
CSS_FRAME = open('frame_style.css').read()
DEFS = open('defs.html').read()
FONTS = """
@font-face{font-family:'Plus Jakarta Sans';src:url('../gf/PlusJakartaSans.ttf');font-weight:200 800}
@font-face{font-family:'DM Serif Display';src:url('../gf/DMSerifDisplay-Regular.ttf')}
@font-face{font-family:'DM Serif Display';font-style:italic;src:url('../gf/DMSerifDisplay-Italic.ttf')}
@font-face{font-family:'Caveat';src:url('../gf/Caveat.ttf');font-weight:400 700}
"""
CSS = r"""
.slide.navy{background:radial-gradient(ellipse 760px 700px at 72% 60%,#22406E 0%,#13294B 62%,#0F2240 100%)}
.slide.navy::before{content:"";position:absolute;inset:0;opacity:.45;mix-blend-mode:soft-light;pointer-events:none;
 background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)' opacity='.5'/%3E%3C/svg%3E")}
.kick{position:absolute;font-family:'Caveat';font-weight:700;color:#F3A15F;transform:rotate(-3deg);transform-origin:left;white-space:nowrap}
.h{position:absolute;font-family:'DM Serif Display';color:#fff;line-height:1.02}
.h i{color:#F3A15F}
.p{position:absolute;color:#DCE5F3;font-weight:500;line-height:1.45}
.p b{color:#fff;font-weight:800}
.glow{position:absolute;border-radius:50%;background:radial-gradient(circle,rgba(255,196,120,.42) 0%,rgba(255,170,90,.16) 38%,rgba(255,170,90,0) 70%)}
.sig{position:absolute;font-family:'Caveat';font-weight:700;color:#F3A15F}
"""

candle = '''<svg style="position:absolute;left:600px;top:470px;width:380px;height:700px;overflow:visible" viewBox="0 0 380 700">
<defs>
<linearGradient id="wax" x1="0" x2="1"><stop offset="0" stop-color="#D9CBB0"/><stop offset=".35" stop-color="#FFF6E4"/><stop offset=".7" stop-color="#F1E3C6"/><stop offset="1" stop-color="#BBA987"/></linearGradient>
<radialGradient id="flame" cx=".5" cy=".7" r=".6"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".35" stop-color="#FFE7A8"/><stop offset=".75" stop-color="#F6A54A"/><stop offset="1" stop-color="#E8792B" stop-opacity="0"/></radialGradient>
<linearGradient id="core" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF" stop-opacity="0"/><stop offset=".6" stop-color="#7FA6E8" stop-opacity=".55"/><stop offset="1" stop-color="#3A5FA8" stop-opacity=".8"/></linearGradient>
<linearGradient id="dish" x1="0" x2="1"><stop offset="0" stop-color="#8E99AA"/><stop offset=".4" stop-color="#E3E7EE"/><stop offset="1" stop-color="#7C8798"/></linearGradient>
<linearGradient id="lit" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFD08A" stop-opacity=".55"/><stop offset="1" stop-color="#FFD08A" stop-opacity="0"/></linearGradient>
</defs>
<!-- bayangan di meja -->
<ellipse cx="190" cy="642" rx="170" ry="26" fill="rgba(0,0,0,.35)"/>
<!-- tatakan -->
<ellipse cx="190" cy="622" rx="160" ry="34" fill="url(#dish)"/>
<ellipse cx="190" cy="612" rx="140" ry="24" fill="#C9D0DB"/>
<!-- lilin -->
<path d="M120 250 L120 610 Q190 632 260 610 L260 250 Z" fill="url(#wax)"/>
<path d="M120 250 L120 610 Q190 632 260 610 L260 250 Z" fill="url(#lit)" opacity=".7"/>
<ellipse cx="190" cy="250" rx="70" ry="16" fill="#F7EBD2"/>
<ellipse cx="190" cy="252" rx="56" ry="10" fill="#EAD9B6"/>
<!-- lelehan lilin -->
<path d="M128 252 Q126 290 134 300 Q142 292 140 256 Z" fill="#FFF3DD"/>
<path d="M236 256 Q234 330 244 340 Q254 328 250 254 Z" fill="#FBEFD6"/>
<!-- sumbu dan api -->
<path d="M190 252 Q188 236 192 222" stroke="#2B2420" stroke-width="5" fill="none" stroke-linecap="round"/>
<path d="M190 226 C160 196 166 150 190 96 C214 150 222 196 190 226 Z" fill="url(#flame)"/>
<path d="M190 222 C178 206 180 186 190 168 C200 186 202 206 190 222 Z" fill="url(#core)"/>
</svg>'''

body = f'''
<div class="glow" style="left:520px;top:370px;width:540px;height:540px"></div>
<div class="kick" style="left:80px;top:190px;font-size:62px">25 Desember 2026</div>
<div class="h" style="left:76px;top:262px;font-size:124px">Selamat<br><i>Natal</i></div>
{candle}
<div class="p" style="left:80px;top:640px;width:520px;font-size:36px">Bagi Bapak, Ibu, dan siswa yang merayakan: <b>damai dan sukacita</b> untuk keluarga di rumah.</div>
<div class="sig" style="left:80px;top:900px;font-size:50px;transform:rotate(-2deg)">dari kami di ExtraCourse</div>
'''
slide = f'''<section class="slide navy">
<div class="corner l"><b>Natal</b><br>25 Desember</div>
<div class="tab"><img src="assets/compass.png" alt=""><div><div class="word">ExtraCourse</div><div class="sub">LES PRIVAT SD · SMP · SMA · UMUM</div></div></div>
{body}
<div class="bar"><span><i><svg><use href="#i-wa"/></svg></i>0812-2069-3313</span><span><i><svg><use href="#i-ig"/></svg></i>@extracourse_</span><span><i><svg><use href="#i-pin"/></svg></i>Jogja</span></div>
</section>'''
html = f'<!doctype html><html lang="id"><head><meta charset="utf-8"><style>{FONTS}{CSS_FRAME}{CSS}</style></head><body>{DEFS}{slide}</body></html>'
open('slides.html', 'w').write(html)
os.makedirs('out', exist_ok=True)
with sync_playwright() as pw:
    b = pw.chromium.launch(); p = b.new_page(viewport={'width': 1200, 'height': 1400})
    p.goto('file://' + os.path.abspath('slides.html')); p.evaluate('document.fonts.ready'); p.wait_for_timeout(800)
    p.query_selector('section.slide').screenshot(path=f'out/{NAME}.png')
    b.close()
print('ok')
