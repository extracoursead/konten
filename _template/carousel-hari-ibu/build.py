# Hari Ibu (22 Des 2026): sudut Kongres Perempuan Indonesia I, 22-25 Des 1928, Dalem Jayadipuran Yogyakarta.
# Kartu arsip manila diketik (Courier Prime) + selotip, lalu surat tulisan tangan. Latar kertas terang.
# Render: python3 build.py  (butuh Playwright + font di ../gf/)
import os
from playwright.sync_api import sync_playwright

NAME = '2026-12-22-hari-ibu-kongres-perempuan'
TOTAL = 3
CSS_FRAME = open('frame_style.css').read()
DEFS = open('defs.html').read()
FONTS = """
@font-face{font-family:'Plus Jakarta Sans';src:url('../gf/PlusJakartaSans.ttf');font-weight:200 800}
@font-face{font-family:'DM Serif Display';src:url('../gf/DMSerifDisplay-Regular.ttf')}
@font-face{font-family:'DM Serif Display';font-style:italic;src:url('../gf/DMSerifDisplay-Italic.ttf')}
@font-face{font-family:'Caveat';src:url('../gf/Caveat.ttf');font-weight:400 700}
@font-face{font-family:'Kalam';src:url('../gf/Kalam-Regular.ttf')}
@font-face{font-family:'Kalam';font-weight:700;src:url('../gf/Kalam-Bold.ttf')}
@font-face{font-family:'Courier Prime';src:url('../gf/CourierPrime-Regular.ttf')}
@font-face{font-family:'Courier Prime';font-weight:700;src:url('../gf/CourierPrime-Bold.ttf')}
"""
NOISE = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/%3E%3CfeColorMatrix values='0 0 0 0 .45 0 0 0 0 .4 0 0 0 0 .32 0 0 0 .08 0'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E\")"
CSS = r"""
.slide.paper{background:#FFFDF8}
.slide.paper::before{content:"";position:absolute;inset:0;pointer-events:none;opacity:.7;mix-blend-mode:multiply;background-image:NOISE}
.paper .corner{color:#4A5A73}.paper .corner b{color:#13294B}
.paper .bar i{background:#13294B;color:#fff}.paper .bar{color:#13294B}
.kick{position:absolute;font-family:'Caveat';font-weight:700;color:#C45F17;transform:rotate(-3deg);transform-origin:left;white-space:nowrap}
.h{position:absolute;font-family:'DM Serif Display';color:#13294B;line-height:1.04}
.h i{color:#C45F17}
.p{position:absolute;color:#4A5A73;font-weight:500;line-height:1.42}
.p b{color:#13294B;font-weight:800}
.src{position:absolute;font-size:21px;color:#6B7A92;font-weight:500;line-height:1.35}
/* kartu arsip manila */
.card{position:absolute;background:#F2E2B6;color:#2E2A22;font-family:'Courier Prime';padding:46px 54px 40px;border-radius:4px;
  box-shadow:0 2px 0 rgba(0,0,0,.05),0 34px 44px -22px rgba(19,41,75,.55)}
.card::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:.8;mix-blend-mode:multiply;background-image:NOISE;border-radius:inherit}
.card .rule{border-top:2px solid rgba(190,60,50,.55);margin:14px 0 18px}
.card .ln{background-image:repeating-linear-gradient(180deg,transparent 0 51px,rgba(70,110,170,.28) 51px 53px);line-height:53px}
.card .no{position:absolute;right:40px;top:34px;font-size:22px;opacity:.65}
.tape{position:absolute;width:200px;height:54px;background:rgba(236,226,200,.82);box-shadow:0 2px 4px rgba(0,0,0,.08);z-index:3;
  clip-path:polygon(2% 8%,10% 0,22% 7%,35% 1%,50% 6%,64% 0,78% 6%,90% 1%,100% 9%,98% 92%,88% 100%,75% 94%,60% 100%,46% 94%,32% 100%,18% 95%,6% 100%,0 90%)}
.circ{position:absolute;overflow:visible}
/* surat tulisan tangan */
.letter{position:absolute;background:#fff;border-radius:3px;padding:60px 64px;font-family:'Kalam';color:#24408E;line-height:1.55;
  box-shadow:0 34px 44px -22px rgba(19,41,75,.5);
  background-image:repeating-linear-gradient(180deg,transparent 0 63px,#D6E0F0 63px 65px);background-position:0 48px}
.letter::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:.5;mix-blend-mode:multiply;background-image:NOISE}
.letter .sig{text-align:right;margin-top:14px;font-size:38px}
"""
CSS = CSS.replace('NOISE', NOISE)

def frame(corner_l, n, body):
    return f'''<section class="slide paper">
<div class="corner l"><b>Hari Ibu</b><br>{corner_l}</div>
<div class="tab"><img src="assets/compass.png" alt=""><div><div class="word">ExtraCourse</div><div class="sub">LES PRIVAT SD · SMP · SMA · UMUM</div></div></div>
<div class="corner r"><b>{n}</b> / {TOTAL}</div>
{body}
<div class="bar"><span><i><svg><use href="#i-wa"/></svg></i>0812-2069-3313</span><span><i><svg><use href="#i-ig"/></svg></i>@extracourse_</span><span><i><svg><use href="#i-pin"/></svg></i>Jogja</span></div>
</section>'''

def circle(x, y, w, h, c='#C45F17'):
    return f'<svg class="circ" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate(-2deg)" viewBox="0 0 {w} {h}"><path d="M{w*0.08} {h*0.55} C{w*0.05} {h*0.1},{w*0.9} {h*0.02},{w*0.96} {h*0.45} C{w*1.0} {h*0.9},{w*0.2} {h*1.02},{w*0.06} {h*0.62} C{w*0.02} {h*0.45},{w*0.2} {h*0.18},{w*0.4} {h*0.12}" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round" filter="url(#ink)"/></svg>'

# ---------- 1 sampul ----------
s1 = f'''
<div class="kick" style="left:80px;top:178px;font-size:58px">22 Desember 1928,</div>
<div class="h" style="left:76px;top:246px;font-size:108px;letter-spacing:-1px">Hari Ibu<br><i>lahir di Jogja</i></div>
<div class="tape" style="left:430px;top:566px;transform:rotate(-3deg)"></div>
<div class="card" style="left:110px;top:590px;width:860px;transform:rotate(-1.5deg)">
<div style="font-weight:700;font-size:34px;letter-spacing:1px">KONGRES PEREMPOEAN INDONESIA I</div>
<div class="rule"></div>
<div class="ln" style="font-size:31px"><span style="position:relative;display:inline-block">22 - 25 Desember 1928<svg viewBox="0 0 200 60" preserveAspectRatio="none" style="position:absolute;left:-30px;top:-14px;width:calc(100% + 60px);height:calc(100% + 26px);overflow:visible"><path d="M120 3 C170 3,198 14,198 30 C198 48,160 58,100 58 C40 58,2 48,2 30 C2 13,40 2,104 2 C130 2,150 5,160 8" fill="none" stroke="#C45F17" stroke-width="4" stroke-linecap="round" vector-effect="non-scaling-stroke" filter="url(#ink)"/></svg></span><br>Pendopo Dalem Jayadipuran<br>Jl. Brigjen Katamso, Yogyakarta<br>&#177; 30 organisasi perempuan, 12 kota</div>
</div>
<div class="p" style="left:80px;top:1112px;width:920px;font-size:32px">Bukan sekadar hari kasih sayang. <b>Hari ini berawal dari perempuan yang berkumpul di Jogja.</b></div>
'''

# ---------- 2 isi ----------
s2 = f'''
<div class="kick" style="left:80px;top:178px;font-size:56px">yang mereka suarakan, salah satunya:</div>
<div class="h" style="left:76px;top:244px;font-size:96px">hak perempuan<br><i>untuk bersekolah</i></div>
<div class="p" style="left:80px;top:500px;width:920px;font-size:34px">Sekitar <b>30 organisasi perempuan dari 12 kota</b> di Jawa dan Sumatra datang ke Jogja. Di tengah masa penjajahan, mereka membicarakan pendidikan dan martabat perempuan.</div>
<div class="tape" style="left:150px;top:750px;transform:rotate(4deg)"></div>
<div class="card" style="left:110px;top:776px;width:860px;transform:rotate(1deg);padding:40px 50px">
<div class="ln" style="font-size:30px;display:grid;grid-template-columns:230px 1fr"><span>22 Des 1928</span><span>kongres dibuka di Yogyakarta</span><span>16 Des 1959</span><span>22 Desember jadi Hari Ibu</span><span></span><span>(Keppres No. 316)</span></div>
</div>
<div class="src" style="left:80px;top:1112px;width:920px">Sumber: Dinas Perpustakaan dan Arsip Daerah DIY, "Kongres Perempuan Pertama 1928 di Yogyakarta"; Keputusan Presiden RI No. 316 Tahun 1959.</div>
'''

# ---------- 3 ucapan ----------
s3 = f'''
<div class="kick" style="left:80px;top:178px;font-size:56px">Selamat Hari Ibu, 22 Desember 2026</div>
<div class="h" style="left:76px;top:246px;font-size:108px">Terima kasih,<br><i>Ibu</i></div>
<div class="letter" style="left:120px;top:600px;width:840px;transform:rotate(-1.2deg);font-size:40px">Untuk Ibu yang menyiapkan meja belajar, mengingatkan PR, dan menunggu sampai les selesai.<br>Terima kasih sudah menemani.<div class="sig">dari kami di ExtraCourse</div></div>
'''

slides = [frame('Jogja, 1928', 1, s1), frame('Sejarahnya', 2, s2), frame('Terima kasih', 3, s3)]
html = f'<!doctype html><html lang="id"><head><meta charset="utf-8"><style>{FONTS}{CSS_FRAME}{CSS}</style></head><body>{DEFS}{"".join(slides)}</body></html>'
open('slides.html', 'w').write(html)
os.makedirs('out', exist_ok=True)
with sync_playwright() as pw:
    b = pw.chromium.launch(); p = b.new_page(viewport={'width': 1200, 'height': 1400})
    p.goto('file://' + os.path.abspath('slides.html')); p.evaluate('document.fonts.ready'); p.wait_for_timeout(800)
    for i, s in enumerate(p.query_selector_all('section.slide'), 1):
        s.screenshot(path=f'out/{NAME}-{i:02d}.png')
    b.close()
print('ok')
