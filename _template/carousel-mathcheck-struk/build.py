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

CSS = r"""
.slide.navy{background:radial-gradient(ellipse 900px 800px at 50% 40%,#1C3A66 0%,#13294B 70%)}
.slide.navy::before{content:"";position:absolute;inset:0;opacity:.45;mix-blend-mode:soft-light;pointer-events:none;
 background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)' opacity='.5'/%3E%3C/svg%3E")}
.kick{position:absolute;font-family:'Caveat';font-weight:700;color:#F3A15F;transform:rotate(-3deg);transform-origin:left}
.h{position:absolute;font-family:'DM Serif Display';color:#fff;line-height:1.02}
.h i{color:#F3A15F}
.p{position:absolute;color:#DCE5F3;font-weight:500;line-height:1.45}
.p b{color:#fff;font-weight:800}
/* thermal receipt */
.rc{position:absolute;background:#FBFAF6;color:#2A2A2A;font-family:'Courier Prime',monospace;
  filter:drop-shadow(0 26px 30px rgba(0,0,0,.45));
  clip-path:polygon(0 1.4%,3% 0,6% 1.4%,9% 0,12% 1.4%,15% 0,18% 1.4%,21% 0,24% 1.4%,27% 0,30% 1.4%,33% 0,36% 1.4%,39% 0,42% 1.4%,45% 0,48% 1.4%,51% 0,54% 1.4%,57% 0,60% 1.4%,63% 0,66% 1.4%,69% 0,72% 1.4%,75% 0,78% 1.4%,81% 0,84% 1.4%,87% 0,90% 1.4%,93% 0,96% 1.4%,100% 0,100% 98.6%,97% 100%,94% 98.6%,91% 100%,88% 98.6%,85% 100%,82% 98.6%,79% 100%,76% 98.6%,73% 100%,70% 98.6%,67% 100%,64% 98.6%,61% 100%,58% 98.6%,55% 100%,52% 98.6%,49% 100%,46% 98.6%,43% 100%,40% 98.6%,37% 100%,34% 98.6%,31% 100%,28% 98.6%,25% 100%,22% 98.6%,19% 100%,16% 98.6%,13% 100%,10% 98.6%,7% 100%,4% 98.6%,1% 100%,0 98.6%)}
.rcw{position:absolute;filter:drop-shadow(0 24px 26px rgba(0,0,0,.5))}
.rc::after{content:"";position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(90deg,rgba(0,0,0,.06),rgba(0,0,0,0) 12%,rgba(0,0,0,0) 88%,rgba(0,0,0,.07)),
  repeating-linear-gradient(180deg,rgba(0,0,0,0) 0 260px,rgba(0,0,0,.035) 260px 262px,rgba(0,0,0,0) 262px 520px);}
.rc .in{position:absolute;inset:0;padding:54px 46px;opacity:.86}
.rc .c{text-align:center}
.rc .row{display:flex;justify-content:space-between;font-size:27px;line-height:1.55}
.rc .dash{border-top:3px dashed #555;margin:14px 0;opacity:.7}
.rc .big{font-weight:700;font-size:34px}
.ink{font-family:'Caveat';font-weight:700;position:absolute;white-space:nowrap}
.ink.blue{color:#24408E}.ink.red{color:#C8302A}
.pen{position:absolute;overflow:visible;pointer-events:none}
.card{position:absolute;background:#FFFDF6;box-shadow:0 26px 40px -18px rgba(0,0,0,.6);color:#13294B}
.src{position:absolute;font-size:20px;color:#8FA3C4;font-weight:500;line-height:1.35}
.tag{position:absolute;background:#FBF4E4;border-radius:12px 12px 12px 12px;box-shadow:0 22px 30px -14px rgba(0,0,0,.6);color:#13294B;
  clip-path:polygon(16% 0,100% 0,100% 100%,16% 100%,0 50%)}
.tag .hole{position:absolute;left:7%;top:50%;width:26px;height:26px;margin-top:-13px;border-radius:50%;background:#13294B;box-shadow:inset 0 3px 4px rgba(0,0,0,.5)}
.string{position:absolute;height:3px;background:#C9B48A;transform-origin:left}
.ticket{position:absolute;left:80px;right:80px;height:150px;background:#E8792B;color:#fff;display:flex;align-items:center;padding:0 56px;gap:30px;border-radius:18px;
  -webkit-mask:radial-gradient(circle 26px at 0 50%,transparent 25px,#000 26px) left/51% 100% no-repeat,radial-gradient(circle 26px at 100% 50%,transparent 25px,#000 26px) right/51% 100% no-repeat}
.ticket .l{font-size:28px;font-weight:600}.ticket .big{font-size:58px;font-weight:800;letter-spacing:-1px;line-height:1.05}
.ticket .cut{margin-left:auto;align-self:stretch;border-left:4px dashed rgba(255,255,255,.55);padding-left:38px;display:flex;align-items:center}
.ticket svg{width:80px;height:80px}
.num{display:inline-flex;align-items:center;justify-content:center;width:62px;height:62px;border-radius:50%;background:#E8792B;color:#fff;font-weight:800;font-size:32px;flex:none}
"""

def frame(corner_l, n, body):
    return f'''<section class="slide navy">
<div class="corner l"><b>MathCheck</b><br>{corner_l}</div>
<div class="tab"><img src="assets/compass.png" alt=""><div><div class="word">ExtraCourse</div><div class="sub">LES PRIVAT SD · SMP · SMA · UMUM</div></div></div>
<div class="corner r"><b>{n}</b> / 6</div>
{body}
<div class="bar"><span><i><svg><use href="#i-wa"/></svg></i>0812-2069-3313</span><span><i><svg><use href="#i-ig"/></svg></i>@extracourse_</span><span><i><svg><use href="#i-pin"/></svg></i>Jogja</span></div>
</section>'''

def circle(x, y, w, h, color="#C8302A", sw=5, rot=-4):
    return f'<svg class="pen" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)" viewBox="0 0 {w} {h}"><path d="M{w*0.08} {h*0.55} C{w*0.05} {h*0.1},{w*0.9} {h*0.02},{w*0.96} {h*0.45} C{w*1.0} {h*0.9},{w*0.2} {h*1.02},{w*0.06} {h*0.62} C{w*0.02} {h*0.45},{w*0.2} {h*0.18},{w*0.4} {h*0.12}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" filter="url(#ink)"/></svg>'

def strike(x, y, w, color="#C8302A"):
    return f'<svg class="pen" style="left:{x}px;top:{y}px;width:{w}px;height:30px" viewBox="0 0 {w} 30"><path d="M4 18 C{w*0.3} 10,{w*0.6} 20,{w-4} 12" fill="none" stroke="{color}" stroke-width="5" stroke-linecap="round" filter="url(#ink)"/></svg>'

def arrow(x, y, w, h, color="#C8302A", rot=0):
    return f'<svg class="pen" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)" viewBox="0 0 {w} {h}"><path d="M4 {h-6} C{w*0.3} {h*0.2},{w*0.7} {h*0.1},{w-10} 10" fill="none" stroke="{color}" stroke-width="5" stroke-linecap="round" filter="url(#ink)"/><path d="M{w-34} 8 L{w-8} 10 L{w-18} 34" fill="none" stroke="{color}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" filter="url(#ink)"/></svg>'

def receipt(x, y, w, h, rot, rows_html):
    return f'<div class="rcw" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)"><div class="rc" style="inset:0"><div class="in">{rows_html}</div></div></div>'

HEAD_RC = '''<div class="c big">TOKO MAKMUR</div><div class="c" style="font-size:22px">Jl. Kaliurang Km 5 · Yogyakarta</div>
<div class="c" style="font-size:22px">04/12/2026 10:12 · KASIR 02</div><div class="dash"></div>'''

def row(a, b, style=""):
    return f'<div class="row" style="{style}"><span>{a}</span><span>{b}</span></div>'

# ---------- slide 1 : cover ----------
s1_rc = HEAD_RC + row("SEPATU SEKOLAH", "100.000") + row("DISKON 20%", "-20.000") + row("DISKON 10%", "-8.000") + '<div class="dash"></div>' + row('<b class="big">TOTAL</b>', '<b class="big">72.000</b>') + '<div class="dash"></div><div class="c" style="font-size:22px">TERIMA KASIH</div>'
s1 = f'''
<div class="kick" style="left:80px;top:178px;font-size:62px">cek struk belanja:</div>
<div class="h" style="left:76px;top:248px;font-size:136px;letter-spacing:-1px">20% + 10%<br><i>≠ 30%</i></div>
<div class="p" style="left:80px;top:560px;width:440px;font-size:50px;line-height:1.2;color:#fff;font-weight:800">Anak Anda<br>tahu kenapa?</div>
<div class="p" style="left:80px;top:720px;width:440px;font-size:30px">Promo akhir tahun sering memakai diskon bertingkat. Di soal ujian, jebakannya sama.</div>
{receipt(560, 470, 450, 690, 4, s1_rc)}
{circle(820, 820, 200, 80)}
<div class="ink red" style="left:650px;top:930px;font-size:60px;transform:rotate(-2deg)">bukan 70.000!</div>
<div class="ink" style="left:84px;top:1010px;font-size:54px;color:#F3A15F;transform:rotate(-4deg)">hitung dulu, baru geser</div>
{arrow(390, 1060, 150, 80, "#F3A15F", 0)}
'''

# ---------- slide 2 : real calculation ----------
s2_rc = HEAD_RC + row("SEPATU SEKOLAH", "100.000") + row("DISKON 20%", "-20.000") + row("SUBTOTAL", "80.000", "font-weight:700") + row("DISKON 10%", "-8.000") + '<div class="dash"></div>' + row('<b class="big">TOTAL</b>', '<b class="big">72.000</b>')
s2 = f'''
<div class="kick" style="left:80px;top:178px;font-size:56px">hitungan sebenarnya</div>
<div class="h" style="left:76px;top:240px;font-size:84px">Diskon kedua dihitung<br>dari <i>harga baru</i></div>
{receipt(70, 470, 450, 560, -3, s2_rc)}
<div class="card" style="left:550px;top:470px;width:470px;height:420px;transform:rotate(2deg);
  background-image:repeating-linear-gradient(180deg,transparent 0,transparent 77px,#BBD0EE 77px,#BBD0EE 79px);background-position:0 28px">
  <div style="position:absolute;left:30px;top:34px;font-family:'Kalam';font-size:35px;line-height:79px;color:#24408E;white-space:nowrap">
  100.000 − 20% = 80.000<br>10% dari <span style="border-bottom:4px solid #C8302A">80.000</span> = 8.000<br>80.000 − 8.000 = 72.000<br>
  <span style="color:#C8302A;font-family:'Caveat';font-weight:700;font-size:50px">potong 28%, bukan 30%</span></div></div>
<div class="p" style="left:80px;top:1090px;width:920px;font-size:30px">Rp28.000 dari Rp100.000. Selisihnya kecil, tapi di soal ujian <b>jawaban 70.000 tetap salah.</b></div>
'''

# ---------- slide 3 : why ----------
s3 = f'''
<div class="kick" style="left:80px;top:178px;font-size:56px">kenapa sering salah?</div>
<div class="h" style="left:76px;top:240px;font-size:82px">Persen selalu punya<br><i>"dari berapa"</i></div>
<div class="p" style="left:80px;top:460px;width:900px;font-size:34px">20% dihitung dari <b>Rp100.000</b>, sedangkan 10% dihitung dari <b>Rp80.000</b>. Dasarnya beda, jadi persennya tidak bisa langsung dijumlah.</div>
<div class="card" style="left:80px;top:690px;width:920px;height:410px;padding:44px 50px;transform:rotate(-1deg);
  background-image:repeating-linear-gradient(180deg,transparent 0,transparent 63px,#BBD0EE 63px,#BBD0EE 65px);background-position:0 30px">
  <div style="font-family:'Caveat';font-weight:700;font-size:44px;color:#C45F17">bukan hanya anak-anak</div>
  <div style="display:flex;align-items:baseline;gap:26px;margin-top:6px">
    <div style="font-family:'DM Serif Display';font-size:150px;line-height:.9;color:#13294B">59%</div>
    <div style="font-family:'Kalam';font-size:38px;line-height:1.25;color:#24408E">mahasiswa dalam satu studi<br>langsung menjumlahkan<br>dua diskon bertingkat.</div>
  </div>
  <div style="font-size:21px;color:#4A5A73;margin-top:22px;font-weight:600">Studi Chen &amp; Rao, Journal of Consumer Research (2007), mahasiswa di Amerika Serikat.</div>
</div>
<div class="ink" style="left:610px;top:1130px;font-size:44px;color:#F3A15F;transform:rotate(-3deg)">jebakan yang wajar</div>
'''

# ---------- slide 4 : fractions on price tags ----------
def pricetag(x, y, w, h, rot, title, sub, frac):
    return f'''<div class="tag" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)"><div class="hole"></div>
<div style="position:absolute;left:22%;top:26px;right:30px">
<div style="font-family:'Courier Prime';font-weight:700;font-size:40px;line-height:1.05">{title}</div>
<div style="font-size:24px;font-weight:600;color:#4A5A73;margin-top:8px">{sub}</div></div>
<div class="ink red" style="right:34px;bottom:14px;font-size:76px">{frac}</div></div>'''
s4 = f'''
<div class="kick" style="left:80px;top:178px;font-size:56px">pecahan di label promo</div>
<div class="h" style="left:76px;top:240px;font-size:80px">Promo "gratis" juga<br>bisa <i>dihitung</i></div>
{pricetag(150, 470, 620, 210, -3, "BELI 1 GRATIS 1", "bayar 1, dapat 2", "1/2")}
<div class="p" style="left:800px;top:520px;width:220px;font-size:30px"><b>potongan 50%</b></div>
{pricetag(170, 720, 620, 210, 2, "BELI 2 GRATIS 1", "bayar 2, dapat 3", "1/3")}
<div class="p" style="left:810px;top:770px;width:220px;font-size:30px"><b>potongan sekitar 33%</b></div>
<div class="card" style="left:80px;top:990px;width:920px;padding:28px 40px;transform:rotate(-.5deg)">
  <div style="font-family:'Kalam';font-size:36px;color:#24408E;line-height:1.3">Jadi kalau memang butuh 3 barang, <b style="color:#C8302A">diskon 40%</b> lebih hemat daripada <b>beli 2 gratis 1</b>.</div></div>
'''

# ---------- slide 5 : for parents ----------
steps = [("Tebak dulu", "Sebelum ke kasir, minta anak menebak total yang harus dibayar."),
         ("Hitung satu per satu", "Diskon pertama dulu, lalu diskon kedua dari harga barunya."),
         ("Cocokkan dengan struk", "Kalau beda, cari bersama di langkah mana selisihnya muncul.")]
st_html = "".join(f'''<div style="display:flex;gap:26px;align-items:flex-start;margin-bottom:34px"><div class="num">{i+1}</div>
<div><div style="font-weight:800;font-size:38px;color:#fff">{t}</div><div style="font-size:30px;color:#DCE5F3;margin-top:6px;line-height:1.35">{d}</div></div></div>''' for i, (t, d) in enumerate(steps))
s5_rc = HEAD_RC + row("BUKU TULIS", "16.000") + row("PENSIL 2B", "4.500") + row("DISKON 10%", "-2.050") + '<div class="dash"></div>' + row('<b class="big">TOTAL</b>', '<b class="big">18.450</b>')
s5 = f'''
<div class="kick" style="left:80px;top:178px;font-size:56px">latihan di rumah</div>
<div class="h" style="left:76px;top:240px;font-size:84px">Struk belanja =<br><i>soal latihan gratis</i></div>
<div style="position:absolute;left:80px;top:500px;width:560px">{st_html}</div>
{receipt(660, 520, 380, 560, 5, s5_rc.replace('font-size:27px','font-size:21px'))}
<div class="ink" style="left:690px;top:1120px;font-size:42px;color:#F3A15F;transform:rotate(-4deg)">5 menit, cukup</div>
'''

# ---------- slide 6 : closing ----------
s6 = f'''
<div class="kick" style="left:80px;top:178px;font-size:56px">persen, pecahan, soal cerita</div>
<div class="h" style="left:76px;top:240px;font-size:92px">Anak masih bingung<br><i>menghitung persen?</i></div>
<div class="p" style="left:80px;top:480px;width:900px;font-size:34px">Tutor ExtraCourse mulai dari cara berpikirnya, bukan sekadar rumus. Les privat Matematika SD, SMP, SMA di Jogja, <b>tutor datang ke rumah atau online.</b></div>
<div class="ticket" style="top:720px"><div><div class="l">Konsultasi dulu lewat WhatsApp</div><div class="big">0812-2069-3313</div></div>
<div class="cut"><svg style="color:#fff"><use href="#i-wa"/></svg></div></div>
<div class="p" style="left:80px;top:900px;width:900px;font-size:30px">Info lengkap: <b>extracourse.id</b></div>
<div class="p" style="left:80px;top:970px;width:900px;font-size:30px">Kirim ke sesama orang tua yang anaknya sedang belajar persen.</div>
<div class="src" style="left:80px;top:1080px;width:920px">Konteks: hanya 17% siswa Indonesia usia 15 tahun yang mencapai level dasar (Level 2) matematika di PISA 2025; rata-rata OECD 65%. Sumber: OECD, 2026.</div>
'''

html = f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><style>{FONTS}{CSS_FRAME}{CSS}</style></head><body>
{DEFS}
{frame("Persen dan diskon", 1, s1)}
{frame("Hitungan", 2, s2)}
{frame("Kenapa salah", 3, s3)}
{frame("Pecahan", 4, s4)}
{frame("Untuk orang tua", 5, s5)}
{frame("Penutup", 6, s6)}
</body></html>'''
open('slides.html', 'w').write(html)
print('ok')
