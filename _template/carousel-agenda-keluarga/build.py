import sys
sys.path.insert(0, '/home/claude/work/math4')
CSS_FRAME = open('/home/claude/work/math4/frame_style.css').read()
DEFS = open('/home/claude/work/math4/defs.html').read()
from build_fonts import FONTS

CSS = r"""
.slide.sky{background:radial-gradient(ellipse 900px 900px at 45% 35%,#E8EEF8 0%,#DCE5F3 60%,#CFDAEC 100%)}
.slide.sky::before{content:"";position:absolute;inset:0;opacity:.5;mix-blend-mode:multiply;pointer-events:none;
 background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/%3E%3CfeColorMatrix values='0 0 0 0 .3 0 0 0 0 .35 0 0 0 0 .45 0 0 0 .06 0'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E")}
.kick{position:absolute;font-family:'Caveat';font-weight:700;color:#C45F17;transform:rotate(-3deg);transform-origin:left}
.h{position:absolute;font-family:'DM Serif Display';color:#13294B;line-height:1.02}
.h i{color:#C45F17}
.p{position:absolute;color:#4A5A73;font-weight:500;line-height:1.45}
.p b{color:#13294B;font-weight:800}
/* agenda book */
.book{position:absolute;filter:drop-shadow(0 30px 34px rgba(19,41,75,.35))}
.cover{position:absolute;inset:-14px -18px -18px -18px;background:#1C3A66;border-radius:14px;
  box-shadow:inset 0 0 0 3px rgba(255,255,255,.06)}
.cover::after{content:"";position:absolute;inset:0;border-radius:inherit;opacity:.5;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.2' numOctaves='2'/%3E%3CfeColorMatrix values='0 0 0 0 .1 0 0 0 0 .1 0 0 0 0 .15 0 0 0 .5 0'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)'/%3E%3C/svg%3E")}
.pg{position:absolute;top:0;bottom:0;width:50%;background:#FFFCF4;overflow:hidden}
.pg.l{left:0;border-radius:6px 0 0 6px;background:linear-gradient(90deg,#FFFCF4 0%,#FFFCF4 82%,#EDE6D6 100%)}
.pg.r{right:0;border-radius:0 6px 6px 0;background:linear-gradient(90deg,#E9E2D1 0%,#FFFCF4 14%,#FFFCF4 100%)}
.pg .lines{position:absolute;left:40px;right:44px;top:120px;bottom:30px;
  background-image:repeating-linear-gradient(180deg,transparent 0,transparent 63px,#D7DFEC 63px,#D7DFEC 65px)}
.pg .date{position:absolute;left:40px;right:34px;top:34px;display:flex;justify-content:space-between;align-items:baseline;
  font-family:'Plus Jakarta Sans';font-weight:800;font-size:16px;letter-spacing:2px;color:#8FA3C4;border-bottom:3px solid #13294B;padding-bottom:12px}
.pg .date b{font-family:'DM Serif Display';font-weight:400;letter-spacing:0;font-size:46px;color:#13294B}
.ribbon{position:absolute;width:34px;clip-path:polygon(0 0,100% 0,100% 100%,50% 88%,0 100%);box-shadow:0 4px 6px rgba(0,0,0,.2)}
.hw{position:absolute;font-family:'Kalam';color:#24408E;white-space:nowrap}
.hwc{position:absolute;font-family:'Caveat';font-weight:700;white-space:nowrap}
.tick{display:inline-block;width:46px;height:40px;vertical-align:-6px;margin-right:12px}
.item{display:flex;align-items:flex-start;gap:14px;font-family:'Kalam';font-size:36px;line-height:1.15;color:#24408E;margin-bottom:26px}
.item svg{flex:none;width:44px;height:40px;margin-top:4px}
.tally{position:absolute}
.card{position:absolute;background:#FFFDF6;box-shadow:0 26px 40px -18px rgba(19,41,75,.45);color:#13294B}
.src{position:absolute;font-size:20px;color:#6A7A93;font-weight:600;line-height:1.35}
.ticket{position:absolute;left:80px;right:80px;height:150px;background:#13294B;color:#fff;display:flex;align-items:center;padding:0 56px;gap:30px;border-radius:18px;
  -webkit-mask:radial-gradient(circle 26px at 0 50%,transparent 25px,#000 26px) left/51% 100% no-repeat,radial-gradient(circle 26px at 100% 50%,transparent 25px,#000 26px) right/51% 100% no-repeat}
.ticket .l{font-size:28px;font-weight:600;color:#DCE5F3}.ticket .big{font-size:58px;font-weight:800;letter-spacing:-1px;line-height:1.05}
.ticket .cut{margin-left:auto;align-self:stretch;border-left:4px dashed rgba(255,255,255,.45);padding-left:38px;display:flex;align-items:center}
.ticket svg{width:80px;height:80px;color:#F3A15F}
"""

TICK = '<svg viewBox="0 0 44 40"><path d="M4 22 L16 34 L40 6" fill="none" stroke="#C8302A" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" filter="url(#ink)"/></svg>'

def frame(corner_l, n, total, body):
    return f'''<section class="slide sky">
<div class="corner l"><b>Kenapa</b><br>ExtraCourse</div>
<div class="tab"><img src="/home/claude/work/math4/assets/compass.png" alt=""><div><div class="word">ExtraCourse</div><div class="sub">LES PRIVAT SD · SMP · SMA · UMUM</div></div></div>
<div class="corner r"><b>{n}</b> / {total}</div>
{body}
<div class="bar"><span><i><svg><use href="#i-wa"/></svg></i>0812-2069-3313</span><span><i><svg><use href="#i-ig"/></svg></i>@extracourse_</span><span><i><svg><use href="#i-pin"/></svg></i>Jogja</span></div>
</section>'''

def book(x, y, w, h, rot, left_html, right_html, ribbons=True):
    rb = ''
    if ribbons:
        rb = f'''<div class="ribbon" style="left:{w*0.5-13}px;top:-20px;width:26px;height:{h+80}px;background:#E8792B"></div>
<div class="ribbon" style="left:{w-40}px;top:-20px;width:26px;height:{h+50}px;background:#2B55A8"></div>'''
    return f'''<div class="book" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)">
<div class="cover"></div>
<div class="pg l"><div class="lines"></div>{left_html}</div>
<div class="pg r"><div class="lines"></div>{right_html}</div>
<div style="position:absolute;left:50%;top:0;bottom:0;width:2px;margin-left:-1px;background:rgba(0,0,0,.12)"></div>
{rb}</div>'''

def date(day, label):
    return f'<div class="date"><b>{day}</b><span>{label}</span></div>'

TOTAL = 5

# ---------- 1 cover ----------
L1 = date('Rumah', 'GURU DATANG') + '<div class="hw" style="left:46px;top:150px;font-size:38px;line-height:65px">Senin 16.00<br>Kamis 16.00<br>di meja belajar<br>anak</div>'
R1 = date('Online', 'DARI LAYAR') + '<div class="hw" style="left:46px;top:150px;font-size:38px;line-height:65px">Selasa 19.00<br>Jumat 19.00<br>Google Meet<br>dari kamar</div>'
s1 = f'''
<div class="kick" style="left:80px;top:180px;font-size:60px">mana yang cocok untuk anak?</div>
<div class="h" style="left:76px;top:250px;font-size:124px">Guru ke rumah<br><i>atau online?</i></div>
{book(110, 600, 860, 520, -2, L1, R1)}
'''

# ---------- 2 data ----------
tally5 = lambda x, y: f'<svg class="tally" style="left:{x}px;top:{y}px;width:96px;height:70px" viewBox="0 0 96 70"><g stroke="#24408E" stroke-width="5" stroke-linecap="round" filter="url(#ink)"><path d="M10 6 L8 62"/><path d="M28 6 L27 62"/><path d="M46 6 L45 62"/><path d="M64 6 L63 62"/><path d="M2 50 L80 14"/></g></svg>'
tally = lambda x, y, n: f'<svg class="tally" style="left:{x}px;top:{y}px;width:{20*n+10}px;height:70px" viewBox="0 0 {20*n+10} 70"><g stroke="#24408E" stroke-width="5" stroke-linecap="round" filter="url(#ink)">' + ''.join(f'<path d="M{10+i*18} 6 L{9+i*18} 62"/>' for i in range(n)) + '</g></svg>'
L2 = date('Rumah', 'KE RUMAH') + '<div class="hw" style="left:46px;top:150px;font-size:40px;line-height:65px">sebagian besar<br>kelas aktif kami</div>' + '<div class="hwc" style="left:46px;top:300px;font-size:46px;line-height:1.05;color:#C8302A">termasuk semua<br>kelas SD</div>'
R2 = date('Online', 'DARI LAYAR') + '<div class="hw" style="left:46px;top:150px;font-size:40px;line-height:65px">dipilih siswa<br>SMP ke atas</div>'
s2 = f'''
<div class="kick" style="left:80px;top:180px;font-size:56px">data kelas ExtraCourse</div>
<div class="h" style="left:76px;top:244px;font-size:86px">Sebagian besar kelas<br><i>di rumah siswa</i></div>
{book(110, 520, 860, 470, 1.5, L2, R2, ribbons=False)}
<div class="p" style="left:80px;top:1050px;width:920px;font-size:30px">Anak usia SD umumnya lebih terbantu bila didampingi langsung. Kelas online saat ini dipilih <b>siswa SMP ke atas</b>.</div>
<div class="src" style="left:80px;top:1170px;width:920px">Berdasarkan kelas aktif ExtraCourse, November 2026.</div>
'''

# ---------- 3 & 4 lists ----------
def listpage(title_day, label, items):
    it = ''.join(f'<div class="item">{TICK}<span>{t}</span></div>' for t in items)
    return date(title_day, label) + f'<div style="position:absolute;left:40px;right:60px;top:150px">{it}</div>'

rumah = ["masih SD", "mudah terdistraksi<br>layar", "butuh didampingi<br>langsung saat<br>menulis"]
online = ["SMP atau SMA<br>yang sudah<br>mandiri", "tinggal di luar<br>jangkauan tutor", "jadwalnya padat"]

s3 = f'''
<div class="kick" style="left:80px;top:180px;font-size:56px">guru datang ke rumah</div>
<div class="h" style="left:76px;top:244px;font-size:88px">Cocok untuk anak<br>yang <i>...</i></div>
{book(150, 500, 780, 640, -1.5, listpage('Rumah', 'COCOK JIKA', rumah), '<div class="hwc" style="left:40px;top:60px;font-size:46px;color:#C45F17;white-space:normal;width:300px;line-height:1.1">tutor datang di Yogyakarta dan sekitarnya, sesuai ketersediaan tutor</div>', ribbons=True)}
'''
s4 = f'''
<div class="kick" style="left:80px;top:180px;font-size:56px">belajar online</div>
<div class="h" style="left:76px;top:244px;font-size:88px">Cocok untuk anak<br>yang <i>...</i></div>
{book(150, 500, 780, 640, 1.5, '<div class="hwc" style="left:40px;top:60px;font-size:46px;color:#C45F17;white-space:normal;width:300px;line-height:1.1">lewat video call, satu siswa dengan satu tutor</div>', listpage('Online', 'COCOK JIKA', online), ribbons=True)}
'''

# ---------- 5 closing ----------
s5 = f'''
<div class="kick" style="left:80px;top:180px;font-size:56px">masih ragu?</div>
<div class="h" style="left:76px;top:244px;font-size:92px">Ceritakan kondisi anak,<br><i>kami bantu pilihkan</i></div>
<div class="p" style="left:80px;top:500px;width:900px;font-size:34px">Jenjang, mata pelajaran, jadwal, dan tempat tinggal anak menentukan cara belajar yang paling pas. <b>Les privat SD, SMP, SMA di Jogja.</b></div>
<div class="ticket" style="top:740px"><div><div class="l">Konsultasi dulu lewat WhatsApp</div><div class="big">0812-2069-3313</div></div>
<div class="cut"><svg><use href="#i-wa"/></svg></div></div>
<div class="p" style="left:80px;top:930px;width:900px;font-size:30px">Info lengkap: <b>extracourse.id</b></div>
<div class="p" style="left:80px;top:1000px;width:900px;font-size:30px">Kirim ke sesama orang tua yang sedang memilih les untuk semester genap.</div>
'''

html = f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><style>{FONTS}{CSS_FRAME}{CSS}</style></head><body>
{DEFS}
{frame("Cara belajar", 1, TOTAL, s1)}
{frame("Data kelas", 2, TOTAL, s2)}
{frame("Ke rumah", 3, TOTAL, s3)}
{frame("Online", 4, TOTAL, s4)}
{frame("Penutup", 5, TOTAL, s5)}
</body></html>'''
open('/home/claude/work/agenda9/slides.html', 'w').write(html)
print('ok')
