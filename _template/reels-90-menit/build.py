from parts import HEAD, DEFS, DESK, FRAME

CSS = r"""
.sheet::before{content:"";position:absolute;right:-2px;bottom:-2px;width:160px;height:160px;background:linear-gradient(135deg,rgba(0,0,0,0) 50%,rgba(30,35,50,.10) 75%,rgba(30,35,50,.0) 100%);z-index:2}
#grain{position:absolute;inset:0;z-index:60;pointer-events:none;opacity:.35;mix-blend-mode:multiply;
 background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='256' height='256'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.95' numOctaves='2'/%3E%3CfeColorMatrix values='0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 .12 0'/%3E%3C/filter%3E%3Crect width='256' height='256' filter='url(%23n)'/%3E%3C/svg%3E")}
#win{position:absolute;inset:-200px;z-index:1;pointer-events:none;opacity:.55;
 background:repeating-linear-gradient(118deg,rgba(255,255,255,0) 0 230px,rgba(255,252,240,.55) 230px 420px,rgba(255,255,255,0) 420px 470px);filter:blur(28px)}
.ul{position:absolute;left:4px;top:138px;width:420px;height:26px;overflow:visible}

.clip{position:absolute;left:60px;top:570px;width:850px;height:1070px;border-radius:26px;background:#9A6B3F;
  box-shadow:0 34px 50px -20px rgba(30,35,50,.55),inset 0 2px 0 rgba(255,255,255,.25),inset 0 -6px 12px rgba(0,0,0,.25);transform:rotate(-1.4deg);z-index:20}
.clip::before{content:"";position:absolute;inset:0;border-radius:inherit;opacity:.6;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='400'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.004 .09' numOctaves='3' seed='4'/%3E%3CfeColorMatrix values='0 0 0 0 .35 0 0 0 0 .2 0 0 0 0 .08 0 0 0 .6 0'/%3E%3C/filter%3E%3Crect width='400' height='400' filter='url(%23n)'/%3E%3C/svg%3E")}
.sheet{position:absolute;left:34px;right:34px;top:70px;bottom:34px;background:#FFFDF6;box-shadow:0 3px 6px rgba(0,0,0,.18)}
.sheet::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:.5;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/%3E%3CfeColorMatrix values='0 0 0 0 .45 0 0 0 0 .4 0 0 0 0 .3 0 0 0 .07 0'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E")}
.metal{position:absolute;left:50%;top:-26px;width:330px;height:110px;margin-left:-165px;border-radius:18px 18px 26px 26px;z-index:3;
  background:linear-gradient(180deg,#F4F6F8 0%,#C3CAD3 45%,#8C96A3 100%);box-shadow:0 10px 14px -6px rgba(0,0,0,.45),inset 0 2px 0 #fff}
.metal::after{content:"";position:absolute;left:50%;top:22px;width:70px;height:26px;margin-left:-35px;border-radius:13px;background:#6E7784;box-shadow:inset 0 3px 4px rgba(0,0,0,.5)}
.form{position:absolute;left:44px;right:44px;font-family:'PJ';font-size:22px;font-weight:700;letter-spacing:2px;color:#7A8597}
.form b{font-family:'Kalam';font-weight:400;letter-spacing:0;font-size:34px;color:var(--ball);margin-left:10px}
.axis{position:absolute;left:44px;right:44px;top:210px;height:70px}
.axis .base{position:absolute;left:0;right:0;top:46px;height:0;border-top:3px solid #2B3A55;filter:url(#ink)}
.axis .base::before,.axis .base::after{content:'';position:absolute;top:-12px;width:3px;height:21px;background:#2B3A55}.axis .base::before{left:0}.axis .base::after{right:0}
.seg{position:absolute;top:14px;height:30px;transform-origin:left;opacity:.8;border-radius:4px 9px 5px 10px;filter:url(#ink);mix-blend-mode:multiply}
.axis .tk{position:absolute;top:56px;font-family:'Kalam';font-size:26px;color:#2B3A55;transform:translateX(-50%)}
.row{position:absolute;left:44px;right:44px;height:140px;display:flex;align-items:center;gap:26px;border-bottom:2px solid #D9E2F0}
.row .min{width:118px;font-family:'Caveat';font-weight:700;font-size:72px;color:var(--redpen);text-align:right;line-height:1}
.row .txt{flex:1;display:block;font-family:'Kalam';font-size:46px;line-height:1.1;color:var(--ball)}
.row .box{width:54px;height:54px;border:3px solid #2B3A55;border-radius:6px;position:relative;flex:none}
.row .box svg{position:absolute;left:-6px;top:-16px;width:76px;height:76px;overflow:visible}
.hl1{background:rgba(255,196,80,.65)}.hl2{background:rgba(232,121,43,.7)}.hl3{background:rgba(120,180,240,.75)}.hl4{background:rgba(130,205,140,.75)}
"""

ROWS = [("10'", "Cek materi dan kisi-kisi ujian terdekat", "hl1"),
        ("50'", "Latihan soal yang mirip soal ujian", "hl2"),
        ("20'", "Bahas kesalahan yang muncul", "hl3"),
        ("10'", "Catatan tutor untuk orang tua", "hl4")]
MINS = [10, 50, 20, 10]

rows_html = ""
for i, (m, t, c) in enumerate(ROWS):
    rows_html += f'''<div class="row" id="r{i}" style="top:{352+i*148}px"><div class="min">{m}</div><div class="txt"><div class="w">{t}</div></div>
<div class="box"><svg viewBox="0 0 76 76"><path id="ck{i}" d="M12 40 L30 58 L68 8" fill="none" stroke="#C8302A" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg></div></div>'''

segs = ""
acc = 0
for i, m in enumerate(MINS):
    segs += f'<div class="seg {ROWS[i][2]}" id="sg{i}" style="left:calc({acc/90*100}% + 3px);width:calc({m/90*100}% - 6px)"></div>'
    acc += m
ticks = "".join(f'<div class="tk" style="left:{v/90*100}%">{v}\'</div>' for v in (0, 10, 60, 80, 90))

BODY = f"""<div id="s">{DEFS}
<div id="cam" class="abs" style="inset:0;transform-origin:420px 1100px">
{DESK}

<div id="win"></div>
<div class="clip" id="clip"><div class="metal"></div><div class="sheet">
  <div class="form" style="top:44px">RENCANA SESI <b style="font-family:Caveat;font-weight:700;font-size:48px;color:var(--odeep)">pekan ujian</b></div>
  <div class="form" style="top:112px">DURASI<b>90 menit</b></div>
  <div class="axis"><div class="base"></div>{segs}{ticks}</div>
  {rows_html}
</div></div>


<div id="stk" class="sticky abs" style="left:590px;top:600px;width:320px;height:200px;background:#FFE07A;padding:22px 26px;z-index:30;transform:rotate(5deg)">
  <div class="hand" style="font-size:44px;line-height:1.05;color:var(--ball)">masuk laporan bulanan<br>+ Portal Orang Tua</div></div>
</div>

<div id="hook" class="abs" style="left:70px;right:70px;top:196px;z-index:30">
  <div id="h1" style="font-family:'DMS';font-size:150px;line-height:.95;letter-spacing:-2px;color:var(--navy);position:relative">90 menit les<svg class="ul" viewBox="0 0 420 26"><path id="ulp" d="M6 16 C100 8 240 6 412 12" fill="none" stroke="#E8792B" stroke-width="12" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="0" filter="url(#ink)"/></svg></div>
  <div id="h2" class="hand" style="font-size:96px;line-height:1;color:var(--redpen);margin-top:10px;transform:rotate(-2deg);transform-origin:left">di pekan ujian, isinya apa?</div>
</div>
<div id="end" class="abs" style="inset:0;z-index:45;opacity:0">
  <div class="abs" style="inset:0;background:rgba(19,41,75,.88);backdrop-filter:blur(14px)"></div>
  <div class="abs" style="left:80px;right:80px;top:330px;color:#fff">
    <div class="el" style="font-family:'Caveat';font-weight:700;font-size:70px;color:#F3A15F;transform:rotate(-2deg)">setiap sesi punya rencana</div>
    <div class="el" style="font-family:'DMS';font-size:116px;line-height:1.02;margin-top:20px">Konsultasi dulu<br><i style="color:#F3A15F">lewat WhatsApp</i></div>
    <div class="el" style="font-size:44px;font-weight:600;line-height:1.4;margin-top:44px;color:#DCE5F3">Les privat SD · SMP · SMA di Jogja.<br>Tutor datang ke rumah atau online.</div>
    <div class="el" style="margin-top:70px;display:flex;flex-direction:column;gap:22px">
      <div style="display:inline-flex;align-items:center;gap:22px;background:var(--orange);color:#fff;border-radius:22px;padding:26px 40px;font-weight:800;font-size:58px;width:max-content"><svg style="width:64px;height:64px"><use href="#i-wa"/></svg>0812-2069-3313</div>
      <div style="font-weight:700;font-size:48px;color:#fff;margin-left:8px">extracourse.id</div>
    </div>
  </div>
</div>
{FRAME}
<div id="grain"></div>
</div>""".replace('<div class="bar">','<div class="bar" style="padding:0 150px 0 60px;display:none">')

JS = r"""
<script>
const N=435;
const clamp=x=>Math.max(0,Math.min(1,x)), ease=x=>1-Math.pow(1-clamp(x),3);
const back=x=>{x=clamp(x);const c=1.6;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const $=id=>document.getElementById(id);
document.querySelectorAll('.el').forEach(e=>e.dataset.base=e.style.transform||'');
function ws(el,p,dy=30){const e=ease(p);el.style.opacity=e;el.style.transform=(el.dataset.base||'')+` translateY(${(1-e)*dy}px)`;}
const ST=[60,126,192,258]; // step starts
function render(f){
  let ty=0;for(let i=0;i<4;i++){ty+= -26*ease((f-ST[i])/20);} $('cam').style.transform=`translateY(${ty*0.6}px)`;
  for(let i=0;i<4;i++){
    const s=ST[i], p=(f-s)/14;
    $('sg'+i).style.transform=`scaleX(${ease(p)})`;
    const r=$('r'+i), w=r.querySelector('.w');
    w.style.clipPath=`inset(-20px ${100-100*ease((f-s-2)/16)}% -20px -10px)`;
    r.querySelector('.min').style.opacity=clamp((f-s)/5);
    $('ck'+i).style.strokeDashoffset=1-ease((f-s-16)/8);
    // active row highlight
    const act=(f>=s && (i==3? f<330 : f<ST[i+1]));
    r.style.background=act?'rgba(255,224,122,.35)':'transparent';
  }
  slap($('stk'),(f-282)/10,'rotate(4deg)'); if(f<282)$('stk').style.opacity=0;
  const eo=clamp((f-330)/10); $('end').style.opacity=eo;
  [...document.querySelectorAll('.el')].forEach((el,i)=>ws(el,(f-335-i*6)/12));
}
function slap(el,p,base){const e=back(p);el.style.opacity=clamp(p*4);el.style.transform=`${base} scale(${1.25-0.25*e})`;}
render(0);
</script></body></html>"""

html = HEAD.replace("#desk{position:absolute;inset:-60px","#desk{position:absolute;inset:-220px").replace("#light{position:absolute;inset:0;","#light{position:absolute;inset:-220px;") + CSS + "</style></head><body>" + BODY + JS
open('/home/claude/work/sesi/sesi.html', 'w').write(html.replace("url('../gf/", "url('../gf/").replace('src="../compass.png"', 'src="../compass.png"'))
print("ok")
