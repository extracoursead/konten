# Rapor (18 Des 2026): lembar rapor sungguhan (nama ditutup), stabilo oranye di deskripsi, catatan tempel tulisan tangan.
# Bingkai sama dengan carousel-pr-buku-tulis (frame_style.css + defs.html). Latar navy.
# Render: python3 build.py  (butuh Playwright + font di ../gf/)
import os
from playwright.sync_api import sync_playwright

NAME = '2026-12-18-rapor-bicara-dengan-anak'
TOTAL = 6
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
NOISE = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/%3E%3CfeColorMatrix values='0 0 0 0 .45 0 0 0 0 .4 0 0 0 0 .32 0 0 0 .08 0'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E\")"
CSS = r"""
.slide.navy{background:radial-gradient(ellipse 900px 800px at 50% 40%,#1C3A66 0%,#13294B 70%)}
.slide.navy::before{content:"";position:absolute;inset:0;opacity:.45;mix-blend-mode:soft-light;pointer-events:none;
 background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)' opacity='.5'/%3E%3C/svg%3E")}
.kick{position:absolute;font-family:'Caveat';font-weight:700;color:#F3A15F;transform:rotate(-3deg);transform-origin:left;white-space:nowrap}
.h{position:absolute;font-family:'DM Serif Display';color:#fff;line-height:1.04}
.h i{color:#F3A15F}
.p{position:absolute;color:#DCE5F3;font-weight:500;line-height:1.42}
.p b{color:#fff;font-weight:800}
.p i{font-style:normal;color:#F3A15F}
.src{position:absolute;font-size:21px;color:#8FA3C4;font-weight:500;line-height:1.35}
.idx{position:absolute;font-family:'DM Serif Display';color:#F3A15F;font-size:44px}
/* lembar rapor */
.sheet{position:absolute;background:#FFFDF8;color:#1E2633;border-radius:3px;filter:drop-shadow(0 30px 34px rgba(0,0,0,.5));overflow:hidden;padding:34px 40px}
.sheet::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:.6;mix-blend-mode:multiply;background-image:NOISE}
.sheet .kop{text-align:center;font-weight:800;font-size:22px;letter-spacing:2px;color:#1E2633;border-bottom:3px double #1E2633;padding-bottom:12px}
.sheet .kop small{display:block;font-weight:600;font-size:16px;letter-spacing:1px;margin-top:4px;color:#4A5568}
.meta{display:grid;grid-template-columns:130px 1fr 90px 160px;align-items:center;gap:8px 10px;font-size:18px;margin:16px 0 14px;color:#2D3748}
.meta .blk{background:#1E2633;height:20px;border-radius:2px;width:80%}
table.r{width:100%;border-collapse:collapse;font-size:18px}
table.r th{background:#E9EEF6;font-weight:800;font-size:16px;letter-spacing:1px;text-transform:uppercase;color:#2D3748;padding:9px 10px;border:1.5px solid #9AA6B8;text-align:left}
table.r td{border:1.5px solid #9AA6B8;padding:10px 10px;vertical-align:top;line-height:1.38;color:#2D3748}
table.r td.n{text-align:center;font-weight:800;font-size:22px;width:76px;color:#1E2633}
table.r td.m{width:170px;font-weight:700}
.hl{background:linear-gradient(100deg,rgba(255,160,70,0) 0%,rgba(255,160,70,.62) 3%,rgba(255,150,60,.55) 96%,rgba(255,160,70,0) 100%);padding:1px 2px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.hlb{background:linear-gradient(100deg,rgba(120,170,255,0) 0%,rgba(120,170,255,.55) 3%,rgba(110,160,255,.5) 96%,rgba(120,170,255,0) 100%);padding:1px 2px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.contoh{position:absolute;font-size:18px;font-weight:800;letter-spacing:2px;color:#8FA3C4;text-transform:uppercase}
/* catatan tempel */
.note{position:absolute;background:#FFE07A;color:#3A3320;font-family:'Kalam';line-height:1.3;padding:30px 34px;
  box-shadow:0 2px 0 rgba(0,0,0,.05),0 22px 40px -14px rgba(10,20,40,.55),inset 0 -30px 40px -30px rgba(0,0,0,.12)}
.note.b{background:#CFE0FA;color:#1E2B45}
.note.o{background:#FFD2AE;color:#3D2414}
.note::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:.5;mix-blend-mode:multiply;background-image:NOISE}
.note .who{font-family:'Plus Jakarta Sans';font-weight:800;font-size:18px;letter-spacing:2px;text-transform:uppercase;opacity:.6;margin-bottom:8px}
.step{position:absolute;left:80px;width:920px}
.step .t{font-size:24px;font-weight:800;letter-spacing:3px;color:#8FA3C4;text-transform:uppercase}
.step .d{font-size:35px;color:#fff;font-weight:600;line-height:1.38;margin-top:12px}
.step .d i{font-style:normal;color:#F3A15F}
.avoid{position:absolute;left:80px;right:80px;border:3px solid rgba(243,161,95,.7);border-radius:18px;padding:26px 34px;color:#DCE5F3;font-size:30px;line-height:1.4;font-weight:500}
.avoid b{color:#F3A15F;font-weight:800;letter-spacing:2px;font-size:22px;display:block;margin-bottom:6px}
.ticket{position:absolute;left:80px;right:80px;height:150px;background:#E8792B;color:#fff;display:flex;align-items:center;padding:0 56px;gap:30px;border-radius:18px;
  -webkit-mask:radial-gradient(circle 26px at 0 50%,transparent 25px,#000 26px) left/51% 100% no-repeat,radial-gradient(circle 26px at 100% 50%,transparent 25px,#000 26px) right/51% 100% no-repeat}
.ticket .l{font-size:28px;font-weight:600}.ticket .big{font-size:58px;font-weight:800;letter-spacing:-1px;line-height:1.05}
.ticket .cut{margin-left:auto;align-self:stretch;border-left:4px dashed rgba(255,255,255,.55);padding-left:38px;display:flex;align-items:center}
.ticket svg{width:80px;height:80px}
.arrow{position:absolute;overflow:visible}
""".replace('NOISE', NOISE)

def frame(corner_l, n, body):
    return f'''<section class="slide navy">
<div class="corner l"><b>Rapor</b><br>{corner_l}</div>
<div class="tab"><img src="assets/compass.png" alt=""><div><div class="word">ExtraCourse</div><div class="sub">LES PRIVAT SD · SMP · SMA · UMUM</div></div></div>
<div class="corner r"><b>{n}</b> / {TOTAL}</div>
{body}
<div class="bar"><span><i><svg><use href="#i-wa"/></svg></i>0812-2069-3313</span><span><i><svg><use href="#i-ig"/></svg></i>@extracourse_</span><span><i><svg><use href="#i-pin"/></svg></i>Jogja</span></div>
</section>'''

def arrow(x, y, w, h, d, color='#F3A15F'):
    return f'<svg class="arrow" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px" viewBox="0 0 {w} {h}"><path d="{d}" fill="none" stroke="{color}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" filter="url(#ink)"/></svg>'

META = '''<div class="meta"><span>Nama</span><span class="blk"></span><span>Kelas</span><span>VIII</span>
<span>Semester</span><span>Ganjil</span><span>Tahun</span><span>2026/2027</span></div>'''
ROWS = [
  ('Bahasa Indonesia', '84', 'Menunjukkan penguasaan dalam menemukan gagasan utama teks. Perlu bimbingan dalam menyusun paragraf argumentasi.'),
  ('Matematika', '72', '<span class="hlb">Menunjukkan penguasaan dalam operasi bilangan bulat.</span> <span class="hl">Perlu bimbingan dalam menyelesaikan soal cerita perbandingan.</span>'),
  ('Bahasa Inggris', '78', '<span class="hlb">Mampu memahami teks pendek tentang kegiatan sehari-hari.</span> <span class="hl">Perlu bimbingan dalam menulis kalimat lampau.</span>'),
  ('IPA', '81', 'Menunjukkan penguasaan dalam mengidentifikasi ciri makhluk hidup. Perlu bimbingan dalam membaca grafik hasil percobaan.'),
]
def rapor(rows, kop=True):
    t = ''.join(f'<tr><td class="m">{m}</td><td class="n">{n}</td><td>{d}</td></tr>' for m, n, d in rows)
    k = '<div class="kop">LAPORAN HASIL BELAJAR<small>Contoh, bukan rapor siswa sungguhan</small></div>' + META if kop else ''
    return k + f'<table class="r"><tr><th>Mata pelajaran</th><th>Nilai</th><th>Capaian kompetensi</th></tr>{t}</table>'

# ---------- 1 sampul ----------
s1 = f'''
<div class="kick" style="left:80px;top:176px;font-size:60px">rapor sudah di tangan,</div>
<div class="h" style="left:76px;top:244px;font-size:96px;letter-spacing:-1px">lalu bicara apa<br><i>dengan anak?</i></div>
<div class="sheet" style="left:110px;top:500px;width:860px;transform:rotate(-2deg)">{rapor(ROWS[1:3])}</div>
<div class="note" style="left:560px;top:968px;width:420px;transform:rotate(3deg);font-size:30px;padding:22px 30px">Baca kolom ini dulu, baru angkanya.</div>
{arrow(470, 900, 90, 90, 'M84 84 C60 70 40 50 26 8 M26 8 L14 30 M26 8 L44 26')}
<div class="p" style="left:80px;top:1150px;width:920px;font-size:32px">Tiga langkah supaya obrolan <b>tidak berakhir tegang.</b></div>
'''

# ---------- 2 baca deskripsi ----------
s2 = f'''
<div class="idx" style="left:80px;top:176px">Sebelum mulai</div>
<div class="h" style="left:76px;top:236px;font-size:72px">Baca deskripsinya,<br><i>bukan angkanya saja</i></div>
<div class="sheet" style="left:90px;top:450px;width:900px;transform:rotate(1deg);padding:26px 30px">{rapor([ROWS[2]], kop=False)}</div>
<div class="p" style="left:80px;top:730px;width:920px;font-size:33px">Di samping nilai, guru menulis <b style="color:#A9C6FF">yang sudah dikuasai</b> (biru) dan <b style="color:#F3A15F">yang masih perlu bimbingan</b> (oranye).</div>
<div class="p" style="left:80px;top:900px;width:920px;font-size:33px">Angka 78 hanya menunjukkan seberapa jauh. Kalimat <b>"perlu bimbingan dalam menulis kalimat lampau"</b> memberi tahu persis apa yang perlu dilatih.</div>
<div class="src" style="left:80px;top:1142px;width:920px">Rapor di atas contoh. Dasar: Panduan Pembelajaran dan Asesmen, BSKAP Kemendikdasmen (edisi revisi 2025).</div>
'''

# ---------- 3 langkah 1 ----------
s3 = f'''
<div class="idx" style="left:80px;top:176px">Langkah 1 dari 3</div>
<div class="h" style="left:76px;top:236px;font-size:80px">Mulai dari<br><i>yang sudah bagus</i></div>
<div class="note" style="left:120px;top:470px;width:840px;transform:rotate(-1.5deg);font-size:42px"><div class="who">Contoh kalimat</div>"Bahasa Inggrismu sudah bisa memahami bacaan sehari-hari. Itu karena kamu rajin baca, ya?"</div>
<div class="step" style="top:820px"><div class="t">Kenapa</div><div class="d">Anak yang langsung ditanya soal nilai terendah biasanya <i>menutup diri</i>. Mulai dari yang naik membuat obrolan berikutnya lebih mudah.</div></div>
'''

# ---------- 4 langkah 2 ----------
s4 = f'''
<div class="idx" style="left:80px;top:176px">Langkah 2 dari 3</div>
<div class="h" style="left:76px;top:236px;font-size:80px">Tanya pendapat<br><i>anak dulu</i></div>
<div class="note b" style="left:120px;top:470px;width:840px;transform:rotate(1.2deg);font-size:42px"><div class="who">Contoh kalimat</div>"Menurutmu, pelajaran apa yang paling susah semester ini? Bagian mana yang bikin bingung?"</div>
<div class="step" style="top:820px"><div class="t">Kenapa</div><div class="d">Anak biasanya sudah tahu bagian yang sulit. Jawabannya sering <i>sama dengan deskripsi guru</i>, dan ia merasa didengar, bukan dihakimi.</div></div>
'''

# ---------- 5 langkah 3 ----------
s5 = f'''
<div class="idx" style="left:80px;top:176px">Langkah 3 dari 3</div>
<div class="h" style="left:76px;top:236px;font-size:80px">Pilih satu target<br><i>untuk semester genap</i></div>
<div class="note o" style="left:120px;top:470px;width:840px;transform:rotate(-1deg);font-size:40px"><div class="who">Dari deskripsi rapor</div>Perlu bimbingan menulis kalimat lampau<br><span style="font-size:36px">jadi: menulis 3 kalimat tentang "kemarin" setiap malam, 10 menit.</span></div>
<div class="step" style="top:850px"><div class="t">Kenapa satu saja</div><div class="d">Target kecil yang jelas lebih mungkin dijalankan daripada <i>"semua nilai harus naik"</i>.</div></div>
<div class="avoid" style="top:1060px"><b>YANG SEBAIKNYA DIHINDARI</b>Membandingkan dengan kakak, adik, atau teman sekelas.</div>
'''

# ---------- 6 penutup ----------
s6 = f'''
<div class="kick" style="left:80px;top:176px;font-size:56px">semester genap mulai 4 Januari</div>
<div class="h" style="left:76px;top:240px;font-size:80px">Bawa target itu<br><i>ke les pertama</i></div>
<div class="p" style="left:80px;top:460px;width:920px;font-size:33px">Ceritakan isi deskripsi rapor anak saat mendaftar. Tutor ExtraCourse menyusun <b>rencana belajar bulan pertama</b> dari situ, dan perkembangannya dilaporkan <b>setiap bulan</b> lewat Portal Orang Tua.</div>
<div class="p" style="left:80px;top:700px;width:920px;font-size:31px">Les privat SD, SMP, SMA di Jogja. Guru datang ke rumah atau online. Pendaftaran tetap dilayani selama libur.</div>
<div class="ticket" style="top:860px"><div><div class="l">Tanya jadwal dan biaya lewat WhatsApp</div><div class="big">0812-2069-3313</div></div>
<div class="cut"><svg style="color:#fff"><use href="#i-wa"/></svg></div></div>
<div class="p" style="left:80px;top:1060px;width:920px;font-size:30px"><b>extracourse.id</b> · Kirim ke sesama orang tua yang minggu ini menerima rapor.</div>
'''

# ---------- status WA 1080x1920 ----------
wa = f'''<section class="slide navy" style="height:1920px">
<div class="tab"><img src="assets/compass.png" alt=""><div><div class="word">ExtraCourse</div><div class="sub">LES PRIVAT SD · SMP · SMA · UMUM</div></div></div>
<div class="kick" style="left:80px;top:250px;font-size:64px">rapor sudah di tangan,</div>
<div class="h" style="left:76px;top:330px;font-size:100px">lalu bicara apa<br><i>dengan anak?</i></div>
<div class="note" style="left:90px;top:640px;width:900px;transform:rotate(-1.5deg);font-size:44px;padding:36px 44px"><div class="who">Sebelum mulai</div>Baca deskripsi guru, bukan angkanya saja.</div>
<div class="note b" style="left:90px;top:900px;width:900px;transform:rotate(1deg);font-size:44px;padding:36px 44px"><div class="who">1.</div>Mulai dari yang sudah bagus.</div>
<div class="note o" style="left:90px;top:1120px;width:900px;transform:rotate(-1deg);font-size:44px;padding:36px 44px"><div class="who">2.</div>Tanya pendapat anak dulu.</div>
<div class="note" style="left:90px;top:1340px;width:900px;transform:rotate(1.2deg);font-size:44px;padding:36px 44px"><div class="who">3.</div>Pilih satu target untuk semester genap.</div>
<div class="p" style="left:80px;top:1600px;width:920px;font-size:34px">Semester genap mulai <b>4 Januari</b>. Tanya les privat:</div>
<div class="p" style="left:80px;top:1670px;width:920px;font-size:56px;color:#fff;font-weight:800">WA 0812-2069-3313</div>
<div class="p" style="left:80px;top:1760px;width:920px;font-size:32px">extracourse.id</div>
</section>'''

slides = [frame('Untuk orang tua', 1, s1), frame('Deskripsi', 2, s2), frame('Yang bagus', 3, s3),
          frame('Pendapat anak', 4, s4), frame('Satu target', 5, s5), frame('Semester genap', 6, s6)]
html = f'<!doctype html><html lang="id"><head><meta charset="utf-8"><style>{FONTS}{CSS_FRAME}{CSS}</style></head><body>{DEFS}{"".join(slides)}{wa}</body></html>'
open('slides.html', 'w').write(html)
os.makedirs('out', exist_ok=True)
with sync_playwright() as pw:
    b = pw.chromium.launch(); p = b.new_page(viewport={'width': 1200, 'height': 2000})
    p.goto('file://' + os.path.abspath('slides.html')); p.evaluate('document.fonts.ready'); p.wait_for_timeout(800)
    ss = p.query_selector_all('section.slide')
    for i, s in enumerate(ss[:TOTAL], 1):
        s.screenshot(path=f'out/{NAME}-{i:02d}.png')
    ss[TOTAL].screenshot(path=f'out/{NAME}-status-wa.png')
    b.close()
os.system(f'ffmpeg -loglevel error -y -i "out/{NAME}-%02d.png" -vf "scale=360:-1,tile=3x2:color=0x777777" sheet.png')
print('ok')
