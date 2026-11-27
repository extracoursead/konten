const { chromium } = require('/home/claude/work/libur28/fontpkg/node_modules/playwright');
const path = require('path'); const fs = require('fs');
(async () => {
  const dir = __dirname; const out = path.join(dir,'out'); fs.mkdirSync(out,{recursive:true});
  const b = await chromium.launch({executablePath:'/usr/bin/google-chrome'});
  const p = await b.newPage({viewport:{width:1200,height:1400}});
  await p.goto('file://'+path.join(dir,'slides.html'),{waitUntil:'networkidle'});
  await p.evaluate(()=>document.fonts.ready);
  const s = await p.$$('section.slide');
  for (let i=0;i<s.length;i++){ const f=path.join(out,`2026-12-16-info-libur-${String(i+1).padStart(2,'0')}.png`); await s[i].screenshot({path:f}); console.log(f);}
  await b.close();
})();
