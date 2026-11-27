import os
D = os.path.dirname(os.path.abspath(__file__))
TPL = '/home/claude/konten-src/konten/_template/carousel-pr-buku-tulis'
FR = open(f'{TPL}/frame_style.css').read()
DEFS = open(f'{TPL}/defs.html').read()
F = f'{D}/fontpkg/node_modules'
FONTS = f"""
@font-face{{font-family:'Plus Jakarta Sans';src:url('{F}/@fontsource-variable/plus-jakarta-sans/files/plus-jakarta-sans-latin-wght-normal.woff2');font-weight:200 800}}
@font-face{{font-family:'DM Serif Display';src:url('{F}/@fontsource/dm-serif-display/files/dm-serif-display-latin-400-normal.woff2')}}
@font-face{{font-family:'DM Serif Display';font-style:italic;src:url('{F}/@fontsource/dm-serif-display/files/dm-serif-display-latin-400-italic.woff2')}}
@font-face{{font-family:'Caveat';src:url('{F}/@fontsource-variable/caveat/files/caveat-latin-wght-normal.woff2');font-weight:400 700}}
@font-face{{font-family:'Kalam';src:url('{F}/@fontsource/kalam/files/kalam-latin-400-normal.woff2')}}
@font-face{{font-family:'Kalam';font-weight:700;src:url('{F}/@fontsource/kalam/files/kalam-latin-700-normal.woff2')}}
"""

CSS = r"""
.slide.paper{background:radial-gradient(ellipse 900px 800px at 50% 40%,#FFFEFA 0%,#FFFDF8 55%,#F6F1E6 100%)}
.slide.sky2{background:radial-gradient(ellipse 900px 900px at 45% 35%,#E8EEF8 0%,#DCE5F3 60%,#CFDAEC 100%)}
.paper .corner,.sky2 .corner{color:var(--slate)} .paper .corner b,.sky2 .corner b{color:var(--navy)}
.paper .bar i,.sky2 .bar i{background:var(--navy);color:#fff}
.paper .bar,.sky2 .bar{color:var(--navy)}
.kick{position:absolute;font-family:'Caveat';font-weight:700;color:#C45F17;transform:rotate(-2deg);transform-origin:left}
.h{position:absolute;font-family:'DM Serif Display';color:#13294B;line-height:1.02}
.h i{color:#C45F17}
.p{position:absolute;color:#4A5A73;font-weight:500;line-height:1.45}
.p b{color:#13294B;font-weight:800}
/* desk calendar */
.cal{position:absolute;background:#FFFDF6;border-radius:10px;box-shadow:0 30px 46px -20px rgba(19,41,75,.45),0 2px 0 rgba(0,0,0,.04)}
.cal .rings{position:absolute;top:-26px;left:0;right:0;display:flex;justify-content:space-around;padding:0 60px}
.cal .rings span{width:16px;height:52px;border-radius:9px;background:linear-gradient(90deg,#6B7482,#E6E9EE 45%,#8A93A0);box-shadow:0 3px 4px rgba(0,0,0,.25)}
.cal .head{height:110px;background:#13294B;border-radius:10px 10px 0 0;display:flex;align-items:center;justify-content:space-between;padding:0 50px;color:#fff}
.cal .head b{font-family:'DM Serif Display';font-weight:400;font-size:58px}
.cal .head span{font-weight:800;letter-spacing:4px;font-size:22px;color:#DCE5F3}
.cal .dow,.cal .wk{display:grid;grid-template-columns:repeat(7,1fr);padding:0 34px}
.cal .dow div{text-align:center;font-weight:800;font-size:19px;letter-spacing:2px;color:#8FA3C4;padding:20px 0 6px}
.cal .wk div{position:relative;height:84px;display:flex;align-items:center;justify-content:center;font-family:'DM Serif Display';font-size:46px;color:#13294B}
.cal .wk div.o{color:#C9D3E3}
.cal .wk div.sun{color:#C8302A}
.cal .wk div.sun.o{color:#EBC1BD}
.hl{position:absolute;height:62px;background:rgba(232,121,43,.32);border-radius:6px;transform:rotate(-.6deg);mix-blend-mode:multiply}
.hw{position:absolute;font-family:'Kalam';color:#24408E;white-space:nowrap}
.hwc{position:absolute;font-family:'Caveat';font-weight:700;white-space:nowrap}
.circ{position:absolute;border:5px solid #C8302A;border-radius:50%;filter:url(#ink)}
/* index cards */
.ic{position:absolute;width:400px;height:230px;background:#FFFEF9;border-radius:6px;box-shadow:0 22px 34px -16px rgba(19,41,75,.45);
  background-image:linear-gradient(180deg,transparent 64px,#E8A3A0 64px,#E8A3A0 67px,transparent 67px),repeating-linear-gradient(180deg,transparent 0,transparent 46px,#D2DCEC 46px,#D2DCEC 48px);
  background-position:0 0,0 70px;background-size:100% 100%,100% 100%;background-repeat:no-repeat,no-repeat}
.ic .w{position:absolute;left:34px;top:84px;font-family:'Kalam';font-weight:700;font-size:64px;color:#24408E}
.ic .m{position:absolute;left:36px;top:168px;font-family:'Kalam';font-size:34px;color:#C8302A}
/* notebook checklist */
.nb{position:absolute;background:#FFFDF6;border-radius:8px;box-shadow:0 30px 44px -20px rgba(19,41,75,.45);overflow:hidden}
.nb::before{content:"";position:absolute;left:0;top:0;bottom:0;width:70px;background:#F2EDE1;border-right:2px solid #E6B5B0}
.nb .lines{position:absolute;left:70px;right:0;top:40px;bottom:0;background-image:repeating-linear-gradient(180deg,transparent 0,transparent 88px,#D7DFEC 88px,#D7DFEC 90px)}
.nb .holes{position:absolute;left:22px;top:60px;bottom:40px;display:flex;flex-direction:column;justify-content:space-around}
.nb .holes span{width:26px;height:26px;border-radius:50%;background:#DCE5F3;box-shadow:inset 0 3px 4px rgba(0,0,0,.25)}
.item{position:absolute;left:110px;right:40px;display:flex;align-items:flex-start;gap:20px;font-family:'Kalam';font-size:40px;line-height:1.12;color:#24408E}
.item svg{flex:none;width:48px;height:44px;margin-top:2px}
/* price tags */
.tag{position:absolute;width:300px;height:140px;background:#FFFDF6;box-shadow:0 22px 30px -16px rgba(19,41,75,.5);
  clip-path:polygon(40px 0,100% 0,100% 100%,40px 100%,0 50%);padding:22px 20px 0 70px}
.tag::before{content:"";position:absolute;left:28px;top:63px;width:24px;height:24px;border-radius:50%;background:#DCE5F3;box-shadow:inset 0 2px 3px rgba(0,0,0,.3)}
.tag .n{font-weight:800;font-size:28px;color:#13294B;line-height:1.1;white-space:nowrap}
.tag .c{font-family:'DM Serif Display';font-size:50px;color:#C45F17;margin-top:6px;line-height:1}
.tag .c small{font-family:'Plus Jakarta Sans';font-weight:700;font-size:22px;color:#4A5A73;margin-left:6px}
.string{position:absolute;height:3px;background:#B89A6A;transform-origin:left center}
.gold{background:linear-gradient(135deg,#F7E3A8,#E2BF63 55%,#C99E3E)}
.gold .c{color:#13294B}
/* sticky */
.st{position:absolute;width:300px;height:300px;padding:34px 30px;font-family:'Kalam';font-size:36px;line-height:1.18;color:#13294B;
  box-shadow:0 2px 0 rgba(0,0,0,.05),0 22px 36px -14px rgba(10,20,40,.4),inset 0 -30px 40px -30px rgba(0,0,0,.10)}
.st b{display:block;font-family:'DM Serif Display';font-weight:400;font-size:64px;color:#C45F17;line-height:1;margin-bottom:10px}
.ticket{position:absolute;left:80px;right:80px;height:150px;background:#13294B;color:#fff;display:flex;align-items:center;padding:0 56px;gap:30px;border-radius:18px;
  -webkit-mask:radial-gradient(circle 26px at 0 50%,transparent 25px,#000 26px) left/51% 100% no-repeat,radial-gradient(circle 26px at 100% 50%,transparent 25px,#000 26px) right/51% 100% no-repeat}
.ticket .l{font-size:28px;font-weight:600;color:#DCE5F3}.ticket .big{font-size:58px;font-weight:800;letter-spacing:-1px;line-height:1.05}
.ticket .cut{margin-left:auto;align-self:stretch;border-left:4px dashed rgba(255,255,255,.45);padding-left:38px;display:flex;align-items:center}
.ticket svg{width:80px;height:80px;color:#F3A15F}
"""

TICK = '<svg viewBox="0 0 44 40"><path d="M4 22 L16 34 L40 6" fill="none" stroke="#C8302A" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" filter="url(#ink)"/></svg>'
TOTAL = 6

def frame(bg, n, body):
    return f'''<section class="slide {bg}">
<div class="corner l"><b>Libur Sekolah</b><br>Untuk orang tua</div>
<div class="tab"><img src="{D}/assets/compass.png" alt=""><div><div class="word">ExtraCourse</div><div class="sub">LES PRIVAT SD · SMP · SMA · UMUM</div></div></div>
<div class="corner r"><b>{n}</b> / {TOTAL}</div>
{body}
<div class="bar"><span><i><svg><use href="#i-wa"/></svg></i>0812-2069-3313</span><span><i><svg><use href="#i-ig"/></svg></i>@extracourse_</span><span><i><svg><use href="#i-pin"/></svg></i>Jogja</span></div>
</section>'''

# ---------- 1 cover: December desk calendar ----------
weeks = [[(30,1),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0)],
         [(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0)],
         [(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0)],
         [(21,0),(22,0),(23,0),(24,0),(25,0),(26,0),(27,0)],
         [(28,0),(29,0),(30,0),(31,0),(1,1),(2,1),(3,1)]]
rows = ''
for w in weeks:
    rows += '<div class="wk">' + ''.join(
        f'<div class="{"o " if o else ""}{"sun" if i==6 else ""}">{d}</div>' for i,(d,o) in enumerate(w)) + '</div>'
CW, CX, CY = 860, 110, 540
colw = (CW-68)/7
cal = f'''<div class="cal" style="left:{CX}px;top:{CY}px;width:{CW}px;height:{110+52+84*5+24}px;transform:rotate(-1.5deg)">
<div class="rings"><span></span><span></span><span></span><span></span><span></span></div>
<div class="head"><b>Desember</b><span>2026</span></div>
<div class="dow"><div>SEN</div><div>SEL</div><div>RAB</div><div>KAM</div><div>JUM</div><div>SAB</div><div>MIN</div></div>
{rows}
<div class="hl" style="left:34px;top:{110+52+84*3+11}px;width:{CW-68}px"></div>
<div class="hl" style="left:34px;top:{110+52+84*4+11}px;width:{CW-68}px"></div>
<div class="circ" style="left:{34+colw*1+colw/2-46}px;top:{110+52+6}px;width:92px;height:72px"></div>
</div>'''
s1 = f'''
<div class="kick" style="left:80px;top:178px;font-size:58px">libur 21 Des – 3 Jan</div>
<div class="h" style="left:76px;top:246px;font-size:112px">Libur sekolah,<br><i>belajar tetap jalan</i></div>
{cal}
<div class="hwc" style="left:580px;top:1165px;font-size:40px;color:#C8302A;transform:rotate(-2deg)">tgl 1: event game mulai</div>
'''

# ---------- 2 problem: index cards fading ----------
cards = [('holiday','liburan',1.0,-5,110,530),('gift','hadiah',0.8,4,570,510),('snow','salju',0.55,-3,140,790),('firework','kembang api',0.28,5,590,770)]
ic = ''.join(f'<div class="ic" style="left:{x}px;top:{y}px;transform:rotate({r}deg)"><div class="w" style="opacity:{o}">{w}</div><div class="m" style="opacity:{o}">{m}</div></div>' for w,m,o,r,x,y in cards)
s2 = f'''
<div class="kick" style="left:80px;top:178px;font-size:56px">dua minggu tanpa latihan</div>
<div class="h" style="left:76px;top:246px;font-size:96px">Kosakata yang baru<br><i>ikut libur</i></div>
{ic}
<div class="p" style="left:80px;top:1070px;width:920px;font-size:32px">Kata yang baru dipelajari paling cepat terlupa kalau tidak dipakai. Tidak perlu belajar lama, cukup <b>latihan singkat tapi rutin</b>.</div>
'''

# ---------- 3 solution: notebook checklist ----------
its = ['Paket kosakata baru<br>terbit setiap Senin', 'Selama libur: paket<br>bertema liburan', 'Soal sesuai jenjang:<br>SD, SMP, SMA', 'Skor masuk papan<br>peringkat mingguan']
items = ''.join(f'<div class="item" style="top:{60+i*150}px">{TICK}<span>{t}</span></div>' for i,t in enumerate(its))
s3 = f'''
<div class="kick" style="left:80px;top:178px;font-size:56px">game ExtraCourse</div>
<div class="h" style="left:76px;top:246px;font-size:96px">Latihan 15 menit,<br><i>cukup dari HP</i></div>
<div class="nb" style="left:150px;top:510px;width:780px;height:660px;transform:rotate(1.2deg)"><div class="lines"></div><div class="holes"><span></span><span></span><span></span><span></span><span></span></div>{items}</div>
<div class="hwc" style="left:690px;top:395px;font-size:38px;color:#C8302A;transform:rotate(-5deg)">khusus siswa B. Inggris</div>
'''

# ---------- 4 event: price tags ----------
tags = [('Syal rajut',90,120,540,-5),('Topi Santa',120,590,530,4),('Tanduk rusa',150,130,725,3),('Latar salju',180,600,715,-4)]
tg = ''
for n,c,x,y,r in tags:
    tg += f'<div class="string" style="left:{x+40}px;top:{y-50}px;width:90px;transform:rotate(62deg)"></div>'
    tg += f'<div class="tag" style="left:{x}px;top:{y}px;transform:rotate({r}deg)"><div class="n">{n}</div><div class="c">{c}<small>koin</small></div></div>'
s4 = f'''
<div class="kick" style="left:80px;top:178px;font-size:56px">event Musim Liburan, 1 Des – 3 Jan</div>
<div class="h" style="left:76px;top:246px;font-size:96px">Hadiah kecil,<br><i>alasan untuk latihan</i></div>
{tg.replace('width:250px','')}
<div class="tag" style="left:120px;top:905px;width:360px;transform:rotate(-2deg)"><div class="n">Latar kembang api</div><div class="c">240<small>koin</small></div></div>
<div class="tag gold" style="left:580px;top:895px;width:380px;height:150px;transform:rotate(3deg)"><div class="n">Juara 1–3 dapat</div><div class="c" style="font-size:38px;margin-top:10px;white-space:nowrap">Topi Santa emas</div></div>
<div class="p" style="left:80px;top:1090px;width:920px;font-size:30px">Koin didapat dari menjawab paket soal. Barang hanya dijual selama event, <b>Topi Santa emas khusus juara</b>.</div>
'''

# ---------- 5 parents: 3 sticky notes ----------
s5 = f'''
<div class="kick" style="left:80px;top:178px;font-size:56px">peran orang tua</div>
<div class="h" style="left:76px;top:246px;font-size:96px">Cukup tiga hal<br><i>di rumah</i></div>
<div class="st" style="left:70px;top:540px;width:290px;background:#FFF1B8;transform:rotate(-4deg)"><b>1</b>Sepakati jam main, misalnya setelah sarapan</div>
<div class="st" style="left:395px;top:590px;width:290px;background:#CFE0FA;transform:rotate(3deg)"><b>2</b>Tanyakan 3 kata baru yang ia temukan hari itu</div>
<div class="st" style="left:720px;top:555px;width:290px;background:#FFE3CC;transform:rotate(-2deg)"><b>3</b>Lihat peringkat bersama di akhir minggu</div>
<div class="p" style="left:80px;top:1010px;width:920px;font-size:32px">Kelas selama libur juga bisa tetap berjalan, <b>sesuai kesediaan guru</b>. Tanyakan ke admin ExtraCourse.</div>
'''

# ---------- 6 closing ----------
s6 = f'''
<div class="kick" style="left:80px;top:178px;font-size:56px">belum les di ExtraCourse?</div>
<div class="h" style="left:76px;top:246px;font-size:92px">Semester genap<br><i>mulai 4 Januari</i></div>
<div class="p" style="left:80px;top:500px;width:900px;font-size:34px">Les privat SD, SMP, SMA di Jogja, guru datang ke rumah atau online. Siswa Bahasa Inggris mendapat <b>akun game ExtraCourse</b>. Pendaftaran tetap dilayani selama libur.</div>
<div class="ticket" style="top:790px"><div><div class="l">Tanya jadwal lewat WhatsApp</div><div class="big">0812-2069-3313</div></div>
<div class="cut"><svg><use href="#i-wa"/></svg></div></div>
<div class="p" style="left:80px;top:990px;width:900px;font-size:30px">Info lengkap: <b>extracourse.id</b></div>
'''

html = f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><style>{FONTS}{FR}{CSS}</style></head><body>
{DEFS}
{frame("paper",1,s1)}
{frame("sky2",2,s2)}
{frame("paper",3,s3)}
{frame("sky2",4,s4)}
{frame("paper",5,s5)}
{frame("sky2",6,s6)}
</body></html>'''
open(f'{D}/slides.html','w').write(html)
print('ok')
