# WordCheck PR anak (14 Des 2026): buku tulis sekolah bergaris, tulisan pensil anak, koreksi pena hijau guru.
# Bingkai sama dengan carousel-mathcheck-struk (frame_style.css + defs.html). Latar navy.
# Render: python3 build.py  (butuh Playwright + font di ../gf/)
import os
from playwright.sync_api import sync_playwright

NAME = '2026-12-14-wordcheck-pr-anak'
TOTAL = 7
CSS_FRAME = open('frame_style.css').read()
DEFS = open('defs.html').read()
FONTS = """
@font-face{font-family:'Plus Jakarta Sans';src:url('../gf/PlusJakartaSans.ttf');font-weight:200 800}
@font-face{font-family:'DM Serif Display';src:url('../gf/DMSerifDisplay-Regular.ttf')}
@font-face{font-family:'DM Serif Display';font-style:italic;src:url('../gf/DMSerifDisplay-Italic.ttf')}
@font-face{font-family:'Caveat';src:url('../gf/Caveat.ttf');font-weight:400 700}
@font-face{font-family:'Kalam';src:url('../gf/Kalam-Regular.ttf')}
@font-face{font-family:'Kalam';font-weight:700;src:url('../gf/Kalam-Bold.ttf')}
"""
CSS = r"""
.slide.navy{background:radial-gradient(ellipse 900px 800px at 50% 40%,#1C3A66 0%,#13294B 70%)}
.slide.navy::before{content:"";position:absolute;inset:0;opacity:.45;mix-blend-mode:soft-light;pointer-events:none;
 background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)' opacity='.5'/%3E%3C/svg%3E")}
.kick{position:absolute;font-family:'Caveat';font-weight:700;color:#F3A15F;transform:rotate(-3deg);transform-origin:left;white-space:nowrap}
.h{position:absolute;font-family:'DM Serif Display';color:#fff;line-height:1.02}
.h i{color:#F3A15F}
.p{position:absolute;color:#DCE5F3;font-weight:500;line-height:1.42}
.p b{color:#fff;font-weight:800}
.src{position:absolute;font-size:21px;color:#8FA3C4;font-weight:500;line-height:1.35}
/* buku tulis sekolah: sampul + halaman bergaris + margin merah */
.book{position:absolute;filter:drop-shadow(0 30px 34px rgba(0,0,0,.5))}
.book .cov{position:absolute;inset:-14px -14px -14px -14px;background:#2B55A8;border-radius:6px 14px 14px 6px}
.book .pg{position:absolute;inset:0;background:#FFFDF8;border-radius:2px 8px 8px 2px;overflow:hidden;
  background-image:linear-gradient(90deg,transparent 0 118px,#E59A9A 118px 121px,transparent 121px),
  repeating-linear-gradient(180deg,transparent 0 69px,#B9CBEA 69px 71px);background-position:0 0,0 46px}
.book .pg::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:.55;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/%3E%3CfeColorMatrix values='0 0 0 0 .45 0 0 0 0 .4 0 0 0 0 .32 0 0 0 .08 0'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E")}
.label{position:absolute;background:#fff;border:3px solid #2B55A8;border-radius:10px;color:#2B55A8;font-weight:700;font-size:24px;padding:10px 20px;line-height:1.35}
.label span{font-family:'Kalam';color:#4A4A52;font-weight:400;font-size:28px}
.pencil{position:absolute;font-family:'Kalam';color:#55555E;white-space:nowrap;line-height:71px}
.green{position:absolute;font-family:'Caveat';font-weight:700;color:#1E7A46;white-space:nowrap;line-height:1}
.pen{position:absolute;overflow:visible;pointer-events:none}
.x,.o,.ins{position:relative;display:inline-block}
.x::after{content:"";position:absolute;left:-6px;right:-6px;top:46%;height:22px;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 20' preserveAspectRatio='none'%3E%3Cpath d='M2 13 C30 6 60 15 98 7' fill='none' stroke='%231E7A46' stroke-width='4.5' stroke-linecap='round' vector-effect='non-scaling-stroke'/%3E%3C/svg%3E") center/100% 100% no-repeat;transform:translateY(-50%)}
.o::after{content:"";position:absolute;left:-18px;right:-18px;top:2px;bottom:-4px;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 80' preserveAspectRatio='none'%3E%3Cpath d='M30 12 C80 0 170 2 192 30 C206 56 150 78 90 76 C30 74 2 58 8 36 C12 20 40 8 110 6' fill='none' stroke='%231E7A46' stroke-width='4.5' stroke-linecap='round' vector-effect='non-scaling-stroke'/%3E%3C/svg%3E") center/100% 100% no-repeat}
.ins{width:0}
.ins::after{content:"";position:absolute;left:-16px;top:52px;width:32px;height:30px;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'%3E%3Cpath d='M6 34 L20 8 L34 34' fill='none' stroke='%231E7A46' stroke-width='5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/contain no-repeat}
.ins b{position:absolute;left:-14px;top:-34px;font-family:'Caveat';font-weight:700;color:#1E7A46;font-size:46px}
.idx{position:absolute;font-family:'DM Serif Display';color:#F3A15F;font-size:44px}
.why{position:absolute;left:80px;width:920px}
.why .t{font-size:24px;font-weight:800;letter-spacing:3px;color:#8FA3C4;text-transform:uppercase}
.why .d{font-size:36px;color:#fff;font-weight:600;line-height:1.38;margin-top:12px}
.why .d i{font-style:normal;color:#F3A15F}
.ticket{position:absolute;left:80px;right:80px;height:150px;background:#E8792B;color:#fff;display:flex;align-items:center;padding:0 56px;gap:30px;border-radius:18px;
  -webkit-mask:radial-gradient(circle 26px at 0 50%,transparent 25px,#000 26px) left/51% 100% no-repeat,radial-gradient(circle 26px at 100% 50%,transparent 25px,#000 26px) right/51% 100% no-repeat}
.ticket .l{font-size:28px;font-weight:600}.ticket .big{font-size:58px;font-weight:800;letter-spacing:-1px;line-height:1.05}
.ticket .cut{margin-left:auto;align-self:stretch;border-left:4px dashed rgba(255,255,255,.55);padding-left:38px;display:flex;align-items:center}
.ticket svg{width:80px;height:80px}
"""

def frame(corner_l, n, body):
    return f'''<section class="slide navy">
<div class="corner l"><b>WordCheck</b><br>{corner_l}</div>
<div class="tab"><img src="assets/compass.png" alt=""><div><div class="word">ExtraCourse</div><div class="sub">LES PRIVAT SD · SMP · SMA · UMUM</div></div></div>
<div class="corner r"><b>{n}</b> / {TOTAL}</div>
{body}
<div class="bar"><span><i><svg><use href="#i-wa"/></svg></i>0812-2069-3313</span><span><i><svg><use href="#i-ig"/></svg></i>@extracourse_</span><span><i><svg><use href="#i-pin"/></svg></i>Jogja</span></div>
</section>'''

G = '#1E7A46'
def strike(x, y, w):
    return f'<svg class="pen" style="left:{x}px;top:{y}px;width:{w}px;height:30px" viewBox="0 0 {w} 30"><path d="M4 18 C{w*0.3} 10,{w*0.6} 21,{w-4} 12" fill="none" stroke="{G}" stroke-width="5" stroke-linecap="round" filter="url(#ink)"/></svg>'
def caret(x, y):
    return f'<svg class="pen" style="left:{x}px;top:{y}px;width:40px;height:40px" viewBox="0 0 40 40"><path d="M6 34 L20 8 L34 34" fill="none" stroke="{G}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" filter="url(#ink)"/></svg>'
def tick(x, y, s=70):
    return f'<svg class="pen" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px" viewBox="0 0 70 70"><path d="M8 38 L28 58 L64 10" fill="none" stroke="{G}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def circle(x, y, w, h):
    return f'<svg class="pen" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate(-3deg)" viewBox="0 0 {w} {h}"><path d="M{w*0.08} {h*0.55} C{w*0.05} {h*0.1},{w*0.9} {h*0.02},{w*0.96} {h*0.45} C{w*1.0} {h*0.9},{w*0.2} {h*1.02},{w*0.06} {h*0.62} C{w*0.02} {h*0.45},{w*0.2} {h*0.18},{w*0.4} {h*0.12}" fill="none" stroke="{G}" stroke-width="5" stroke-linecap="round" filter="url(#ink)"/></svg>'

def book(x, y, w, h, rot, inner):
    return f'<div class="book" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)"><div class="cov"></div><div class="pg">{inner}</div></div>'

# ---------- 1 sampul ----------
cover_lines = ['1. I <span class="x">am</span> agree with you.', "2. He <span class='o'>don't</span> like it.",
    '3. I <span class="o">very like</span> it.', '4. Yesterday I <span class="o">go</span> to school.', '5. My father is<span class="ins"></span> teacher.']
inner1 = '<div class="label" style="left:640px;top:16px;transform:rotate(1.5deg)">PR B. Inggris<br><span>Kelas 7</span></div>'
inner1 += '<div class="pencil" style="left:150px;top:132px;font-size:42px">' + '<br>'.join(cover_lines) + '</div>'
s1 = f'''
<div class="kick" style="left:80px;top:176px;font-size:60px">cek PR anak, yuk:</div>
<div class="h" style="left:76px;top:244px;font-size:102px;letter-spacing:-1px">5 kesalahan di PR<br><i>Bahasa Inggris</i></div>
{book(90, 520, 900, 520, -2, inner1)}
<div class="p" style="left:80px;top:1100px;width:920px;font-size:32px">Terdengar benar dalam bahasa Indonesia, <b>jadi sering lolos.</b></div>
'''

# ---------- 2-6 kesalahan ----------
def err_slide(no, wrong_html, fix, marks, why_title, why, ind):
    inner = f'<div class="pencil" style="left:150px;top:126px;font-size:52px">{wrong_html}</div>'
    inner += f'<div class="green" style="left:150px;top:252px;font-size:72px;transform:rotate(-1.5deg);display:flex;align-items:flex-end;gap:12px">{fix}<span style="position:relative;width:66px;height:66px;flex:none">{tick(0, 0, 66)}</span></div>'
    body = f'''
<div class="idx" style="left:80px;top:176px">Kesalahan {no} dari 5</div>
{book(90, 270, 900, 400, 1.2, inner)}
<div class="why" style="top:740px"><div class="t">Kenapa salah</div><div class="d">{why}</div></div>
<div class="why" style="top:990px"><div class="t">Asalnya dari bahasa Indonesia</div><div class="d" style="font-size:34px;color:#DCE5F3;font-weight:500">{ind}</div></div>
'''
    return body

s2 = err_slide(1, 'I <span class="x">am</span> agree with you.', 'I agree with you.', '',
    'Kenapa salah', '<i>Agree</i> sudah kata kerja. Kata kerja tidak perlu ditemani <i>am, is, are</i>.',
    '"Saya setuju" diterjemahkan kata per kata, lalu <i>am</i> ditambahkan karena terasa ada yang kurang.')
s3 = err_slide(2, 'He <span class="x">don\'t</span> like it.', "He doesn't like it.", '',
    '', 'Untuk <i>he, she, it</i>, dan nama satu orang, pakai <i>does</i> atau <i>doesn\'t</i>.',
    'Bahasa Indonesia memakai "tidak" untuk siapa saja. Bahasa Inggris menyesuaikan dengan subjeknya.')
s4 = err_slide(3, 'I <span class="x">very</span> like it.', 'I really like it.', '',
    '', '<i>Very</i> tidak bisa langsung di depan kata kerja. Pakai <i>really</i>, atau <i>I like it very much</i>.',
    '"Saya sangat suka" disalin urutannya: sangat = <i>very</i>, suka = <i>like</i>.')
s5 = err_slide(4, 'Yesterday I <span class="x">go</span> to school.', 'Yesterday I went to school.', '',
    '', 'Kejadian kemarin memakai bentuk lampau: <i>go</i> menjadi <i>went</i>.',
    'Bahasa Indonesia tidak mengubah kata kerja menurut waktu. Cukup "kemarin", kata "pergi" tetap sama.')
s6 = err_slide(5, 'My father is<span class="ins"><b>a</b></span> teacher.', 'My father is a teacher.', '',
    '', 'Pekerjaan satu orang butuh <i>a</i> atau <i>an</i>: <i>a teacher, an engineer</i>.',
    'Bahasa Indonesia tidak punya kata sandang. "Ayah saya guru" sudah lengkap tanpa tambahan.')

# ---------- 7 data + ajakan ----------
s7 = f'''
<div class="kick" style="left:80px;top:176px;font-size:56px">bukan karena anak malas</div>
<div class="h" style="left:76px;top:240px;font-size:84px">Polanya sama:<br><i>ikut bahasa Indonesia</i></div>
<div class="p" style="left:80px;top:470px;width:920px;font-size:32px">Penelitian pada tulisan mahasiswa Indonesia: <b>63% kesalahan berupa kata yang terlewat</b>, seperti <i style="font-style:normal;color:#F3A15F">a</i> di <i style="font-style:normal;color:#F3A15F">a teacher</i>, karena mengikuti susunan bahasa Indonesia.</div>
<div class="src" style="left:80px;top:640px;width:920px">Sumber: Aziz, Fitriani &amp; Amalina (2020), Indonesian Journal of Applied Linguistics (UPI).</div>
<div class="p" style="left:80px;top:720px;width:920px;font-size:32px">Tutor ExtraCourse memeriksa PR bersama anak dan menjelaskan <b>kenapa salah</b>, bukan sekadar membetulkan. Les privat SD, SMP, SMA di Jogja, datang ke rumah atau online.</div>
<div class="ticket" style="top:920px"><div><div class="l">Tanya jadwal dan biaya lewat WhatsApp</div><div class="big">0812-2069-3313</div></div>
<div class="cut"><svg style="color:#fff"><use href="#i-wa"/></svg></div></div>
<div class="p" style="left:80px;top:1100px;width:920px;font-size:30px"><b>extracourse.id</b> · Kirim ke sesama orang tua yang anaknya sedang belajar Bahasa Inggris.</div>
'''

slides = [frame('PR anak', 1, s1), frame('Kata kerja', 2, s2), frame('He, she, it', 3, s3), frame('Very', 4, s4),
          frame('Kemarin', 5, s5), frame('Pekerjaan', 6, s6), frame('Untuk orang tua', 7, s7)]
html = f'<!doctype html><html lang="id"><head><meta charset="utf-8"><style>{FONTS}{CSS_FRAME}{CSS}</style></head><body>{DEFS}{"".join(slides)}</body></html>'
open('slides.html', 'w').write(html)
os.makedirs('out', exist_ok=True)
with sync_playwright() as pw:
    b = pw.chromium.launch(); p = b.new_page(viewport={'width': 1200, 'height': 1400})
    p.goto('file://' + os.path.abspath('slides.html')); p.evaluate('document.fonts.ready'); p.wait_for_timeout(700)
    for i, s in enumerate(p.query_selector_all('section.slide'), 1):
        s.screenshot(path=f'out/{NAME}-{i:02d}.png')
    b.close()
os.system(f'ffmpeg -loglevel error -y -i "out/{NAME}-%02d.png" -vf "scale=360:-1,tile=4x2:color=0x777777" sheet.png')
print('ok')
