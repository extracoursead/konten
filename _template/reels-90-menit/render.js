const {chromium}=require('playwright');const {spawn}=require('child_process');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/sesi.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
const N=435;const ff=spawn('ffmpeg',['-y','-v','error','-f','image2pipe','-framerate','30','-i','-','-i','music.mp3','-filter_complex','[1:a]atrim=0:14.5,afade=t=in:d=0.3,afade=t=out:st=13.1:d=1.4,volume=0.9[a]','-map','0:v','-map','[a]','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart','out.mp4'],{stdio:['pipe','inherit','inherit']});
for(let f=0;f<N;f++){await p.evaluate(f=>render(f),f);const buf=await p.screenshot({type:'jpeg',quality:95});ff.stdin.write(buf);}
ff.stdin.end();ff.on('close',()=>b.close());})();
