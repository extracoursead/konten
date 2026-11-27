import os, sys
sys.path.insert(0, '/home/claude/work/libur28')
import build as B  # reuse fonts, frame css, defs, base css
D = os.path.dirname(os.path.abspath(__file__))
A = '/home/claude/work/libur28/assets/compass.png'

CSS = r"""
/* closed agenda book */
.ag{position:absolute;filter:drop-shadow(0 34px 36px rgba(19,41,75,.38))}
.ag .cv{position:absolute;inset:0;border-radius:10px 22px 22px 10px;background:linear-gradient(100deg,#0E2140 0%,#13294B 8%,#1C3A66 60%,#17325A 100%)}
.ag .cv::after{content:"";position:absolute;inset:0;border-radius:inherit;opacity:.55;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.1' numOctaves='2'/%3E%3CfeColorMatrix values='0 0 0 0 .1 0 0 0 0 .1 0 0 0 0 .15 0 0 0 .5 0'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)'/%3E%3C/svg%3E")}
.ag .pages{position:absolute;right:-14px;top:12px;bottom:12px;width:18px;border-radius:0 8px 8px 0;
  background:repeating-linear-gradient(180deg,#FFFCF4 0,#FFFCF4 3px,#E7DFCD 3px,#E7DFCD 4px)}
.ag .spine{position:absolute;left:0;top:0;bottom:0;width:40px;border-radius:10px 0 0 10px;background:linear-gradient(90deg,rgba(0,0,0,.35),rgba(0,0,0,0))}
.ag .band{position:absolute;top:-6px;bottom:-6px;width:26px;background:linear-gradient(90deg,#B85A1A,#E8792B 40%,#C9641F);box-shadow:0 0 6px rgba(0,0,0,.3)}
.ag .emb{position:absolute;left:90px;top:90px;color:rgba(220,229,243,.85);font-family:'DM Serif Display';font-size:54px;line-height:1.05}
.ag .emb small{display:block;font-family:'Plus Jakarta Sans';font-weight:800;font-size:18px;letter-spacing:4px;color:rgba(143,163,196,.9);margin-top:16px}
.ag .rib{position:absolute;bottom:-90px;width:30px;height:120px;background:#DCE5F3;clip-path:polygon(0 0,100% 0,100% 100%,50% 82%,0 100%);box-shadow:0 4px 6px rgba(0,0,0,.2)}
/* hanging tag */
.htag{position:absolute;background:#FFFDF6;border-radius:10px;box-shadow:0 24px 34px -14px rgba(19,41,75,.5);padding:44px 40px 34px 40px}
.htag::before{content:"";position:absolute;left:50%;top:18px;width:26px;height:26px;margin-left:-13px;border-radius:50%;background:#DCE5F3;box-shadow:inset 0 2px 3px rgba(0,0,0,.3)}
.htag .t1{white-space:nowrap;font-family:'Caveat';font-weight:700;font-size:44px;color:#C45F17;line-height:1;margin-top:14px}
.htag .t2{font-family:'DM Serif Display';font-size:64px;color:#13294B;line-height:1.02;margin-top:8px}
.cord{position:absolute;height:3px;background:#B89A6A;transform-origin:left center}
/* list card */
.lc{position:absolute;background:#FFFDF6;border-radius:14px;box-shadow:0 30px 44px -20px rgba(19,41,75,.45);padding:40px 48px}
.row{display:flex;gap:28px;align-items:flex-start;padding:30px 0;border-bottom:2px dashed #D7DFEC}
.row:last-child{border-bottom:none}
.row .num{flex:none;width:76px;height:76px;border-radius:50%;background:#13294B;color:#fff;font-family:'DM Serif Display';font-size:44px;display:flex;align-items:center;justify-content:center}
.row .tx{font-size:34px;line-height:1.3;color:#4A5A73;font-weight:500}
.row .tx b{display:block;color:#13294B;font-weight:800;font-size:38px;margin-bottom:4px}
.slide.tall{width:1080px;height:1920px}
"""

def frame(bg, n, total, body):
    return f'''<section class="slide {bg}">
<div class="corner l"><b>Info Libur</b><br>ExtraCourse</div>
<div class="tab"><img src="{A}" alt=""><div><div class="word">ExtraCourse</div><div class="sub">LES PRIVAT SD · SMP · SMA · UMUM</div></div></div>
<div class="corner r"><b>{n}</b> / {total}</div>
{body}
<div class="bar"><span><i><svg><use href="#i-wa"/></svg></i>0812-2069-3313</span><span><i><svg><use href="#i-ig"/></svg></i>@extracourse_</span><span><i><svg><use href="#i-pin"/></svg></i>Jogja</span></div>
</section>'''

def agenda(x, y, w, h, rot):
    return f'''<div class="ag" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)">
<div class="pages"></div><div class="cv"></div><div class="spine"></div>
<div class="emb">Agenda Les<small>SEMESTER GASAL 2026</small></div>
<div class="band" style="left:{w-150}px"></div>
<div class="rib" style="left:{w*0.42}px"></div>
</div>'''

def tag(x, y, w, rot, cx, cy, ln, ang):
    return f'''<div class="cord" style="left:{cx}px;top:{cy}px;width:{ln}px;transform:rotate({ang}deg);z-index:3"></div>
<div class="htag" style="left:{x}px;top:{y}px;width:{w}px;transform:rotate({rot}deg)"><div class="t1">sampai jumpa lagi,</div><div class="t2">Senin,<br>4 Januari</div></div>'''

s1 = f'''
<div class="kick" style="left:80px;top:178px;font-size:58px">21 Desember 2026 – 3 Januari 2027</div>
<div class="h" style="left:76px;top:246px;font-size:112px">Libur dulu,<br><i>kembali 4 Januari</i></div>
{agenda(120, 560, 600, 560, -4)}
{tag(590, 720, 400, 6, 583, 625, 250, 31)}
'''

s2 = f'''
<div class="kick" style="left:80px;top:178px;font-size:56px">selama libur</div>
<div class="h" style="left:76px;top:246px;font-size:96px">Yang tetap jalan<br><i>selama libur</i></div>
<div class="lc" style="left:90px;top:520px;width:900px;transform:rotate(-.6deg)">
<div class="row"><div class="num">1</div><div class="tx"><b>Kelas yang sudah disepakati</b>tetap berjalan sesuai jadwal yang dikabarkan admin.</div></div>
<div class="row"><div class="num">2</div><div class="tx"><b>Pendaftaran semester genap</b>tetap dilayani lewat WhatsApp.</div></div>
<div class="row"><div class="num">3</div><div class="tx"><b>Game ExtraCourse</b>event Musim Liburan sampai 3 Januari, untuk siswa Bahasa Inggris.</div></div>
</div>
'''

s3 = f'''
<div class="kick" style="left:80px;top:178px;font-size:56px">semester genap</div>
<div class="h" style="left:76px;top:246px;font-size:92px">Atur jadwal sekarang,<br><i>mulai 4 Januari</i></div>
<div class="p" style="left:80px;top:500px;width:900px;font-size:34px">Les privat SD, SMP, SMA di Jogja, guru datang ke rumah atau online. Ceritakan kebutuhan anak, kami bantu susun jadwal semester genap.</div>
<div class="ticket" style="top:800px"><div><div class="l">Konsultasi lewat WhatsApp</div><div class="big">0812-2069-3313</div></div>
<div class="cut"><svg><use href="#i-wa"/></svg></div></div>
<div class="p" style="left:80px;top:1000px;width:900px;font-size:30px">Info lengkap: <b>extracourse.id</b></div>
'''

# WA status, 1080x1920
st = f'''<section class="slide paper tall">
<div class="tab"><img src="{A}" alt=""><div><div class="word">ExtraCourse</div><div class="sub">LES PRIVAT SD · SMP · SMA · UMUM</div></div></div>
<div class="kick" style="left:80px;top:250px;font-size:58px">info libur ExtraCourse</div>
<div class="h" style="left:76px;top:320px;font-size:104px">Libur dulu,<br><i>kembali 4 Januari</i></div>
<div class="p" style="left:80px;top:600px;width:920px;font-size:40px"><b>21 Desember 2026 – 3 Januari 2027</b></div>
{agenda(130, 760, 560, 520, -4)}
{tag(580, 900, 390, 6, 553, 805, 255, 30)}
<div class="p" style="left:80px;top:1400px;width:920px;font-size:36px">Kelas yang sudah disepakati tetap berjalan. <b>Pendaftaran semester genap tetap dilayani.</b></div>
<div class="ticket" style="top:1580px"><div><div class="l">Tanya jadwal lewat WhatsApp</div><div class="big">0812-2069-3313</div></div>
<div class="cut"><svg><use href="#i-wa"/></svg></div></div>
<div class="p" style="left:80px;top:1770px;width:920px;font-size:30px;text-align:center">extracourse.id</div>
</section>'''

html = f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><style>{B.FONTS}{B.FR}{B.CSS}{CSS}</style></head><body>
{B.DEFS}
{frame("paper",1,3,s1)}
{frame("sky2",2,3,s2)}
{frame("paper",3,3,s3)}
{st}
</body></html>'''
open(f'{D}/slides.html','w').write(html)
print('ok')
