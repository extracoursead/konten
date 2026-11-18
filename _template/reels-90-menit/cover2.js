const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/sesi.html');await p.evaluate(()=>document.fonts.ready);
await p.evaluate(()=>{render(320);document.getElementById('cam').style.transform='translateY(40px)';document.getElementById('hook').style.top='290px';});
await p.screenshot({path:'cover.png'});await b.close()})();
