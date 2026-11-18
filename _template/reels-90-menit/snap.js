const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/'+process.argv[2]);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
for(const f of process.argv.slice(3)){await p.evaluate(f=>render(+f),f);await p.screenshot({path:`/tmp/f${f}.png`,clip:{x:0,y:0,width:1080,height:1920}});}
await b.close();})();
