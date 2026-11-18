import json, subprocess, os
G=json.load(open('grade.json')); S='../src'
B=[0.3,0.98,1.81,2.46,3.11,3.76,4.6,5.25,5.9,6.55,7.2,7.94,8.68,9.33,9.96,10.61,11.47,12.12,12.75,13.4,14.05,14.88,15.53,16.18,16.83,17.58,18.32,18.97,19.62,20.27,21.01,21.76,22.41,23.06,23.68,24.33,25.17,25.82,26.47]
b=lambda i: B[i]-0.3
F=lambda t: round(t*30)
SEG=[('v2',0.3,'P',0,4),('v1',0.0,'P',4,8),('v2',13.5,'P',8,12),('v5',1.0,'P',12,16),
     ('v7',0.5,'L',16,20),('v7',5.6,'L',20,24),('v9',1.0,'L',24,28),('v4',25.0,'P',28,32),('v8',1.0,'L',32,38)]
json.dump({'cuts':[F(b(s[3])) for s in SEG]+[F(b(38))]},open('cuts.json','w'))
lst=[]
for k,(c,st,mode,i0,i1) in enumerate(SEG):
    n=F(b(i1))-F(b(i0)); dur=n/30; g=G[c]
    grade=f"colorchannelmixer=rr={g['rr']}:gg={g['gg']}:bb={g['bb']},eq=gamma={g['gamma']}:contrast=1.06:saturation=1.08"
    src=f'{S}/{c}.mp4'; inp=['-ss',str(st),'-t',f'{dur+0.5}','-i',src]
    pre='fps=30'
    if mode=='P':
        trf=f'trf{k}.trf'
        subprocess.run(['ffmpeg','-v','error','-y',*inp,'-vf',f'{pre},vidstabdetect=shakiness=6:accuracy=12:result={trf}','-f','null','-'],check=True)
        zoom=f"zoompan=z='1.0+0.05*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30"
        vf=f"{pre},vidstabtransform=input={trf}:smoothing=20:optzoom=1:interpol=bicubic,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,{grade},scale=2160:3840:flags=lanczos,{zoom},setsar=1"
        fc=None
    else:
        fc=(f"[0:v]{pre},{grade},split[a][f];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=40:2,eq=brightness=-0.16:saturation=0.75[bg];"
            f"[f]scale=2880:-2:flags=lanczos,zoompan=z='1.0+0.04*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1440x810:fps=30,crop=1080:810,setsar=1[fg];"
            f"[bg][fg]overlay=0:365,setsar=1[v]")
    out=f'b{k}.mp4'
    cmd=['ffmpeg','-v','error','-y',*inp]
    cmd+= (['-vf',vf] if fc is None else ['-filter_complex',fc,'-map','[v]'])
    cmd+=['-frames:v',str(n),'-an','-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p','-r','30',out]
    subprocess.run(cmd,check=True); lst.append(out); print(k,c,n)
open('blist.txt','w').write(''.join(f"file '{x}'\n" for x in lst))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','blist.txt','-c','copy','base.mp4'],check=True)
print(subprocess.run(['ffprobe','-v','error','-count_frames','-show_entries','stream=nb_read_frames','-of','csv=p=0','base.mp4'],capture_output=True,text=True).stdout)
