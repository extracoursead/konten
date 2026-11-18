# Template Reels ExtraCourse: montase klip + teks per kata (Hari Guru, 18 Nov 2026)

Dipakai untuk Reels 2026-11/2026-11-25-hari-guru.mp4 (30 detik, 1080x1920).

- grade.py: hitung koreksi warna per klip (rata-rata RGB tiap klip ditarik ke nuansa hangat netral).
- base.py: potong klip tepat di ketukan musik (tiap 4 ketukan, beat dari librosa), stabilisasi (vidstab) untuk klip tegak,
  klip mendatar ditaruh di tengah dengan latar buram, gerak mendekat pelan. Hasil: base.mp4.
- ov.html + frames.py: lapisan teks animasi (kata per kata), tag logo, pembuka dan kartu penutup; render(f) per frame, 30 fps.
- cover.html: sampul 1080x1920, judul aman untuk potongan grid 3:4.
- Gabung: base.mp4 (tpad clone untuk kartu penutup) + frame overlay + musik (mulai 0,3 detik agar ketukan pertama di 0).

Aset yang tidak disimpan di repo: klip video (Drive "KONTEN EXTRACOURSE - FOTO & VIDEO"), musik (Drive "MUSIC FOR IG"),
font Plus Jakarta Sans dan DM Serif Display (repo google/fonts), logo compass.png (ada di _template/carousel-borrow-vs-lend/assets).
