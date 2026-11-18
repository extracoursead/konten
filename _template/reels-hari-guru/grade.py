import json
M={'v1':[156.7,150.3,138.3],'v2':[145.9,127.4,107.9],'v4':[138.2,130.2,116.0],'v5':[133.6,128.0,116.7],
   'v7':[88.6,80.3,75.8],'v8':[134.3,127.4,129.5],'v9':[119.0,116.7,106.3]}
T=[1.04,1.0,0.93]; K=0.6; out={}
for c,(r,g,b) in M.items():
    gains=[ (T[i]*g/[r,g,b][i])**K for i in range(3)]
    luma=(r+g+b)/3; gamma=min(1.45,max(0.95,(128/luma)**0.55))
    out[c]=dict(rr=round(gains[0],3),gg=round(gains[1],3),bb=round(gains[2],3),gamma=round(gamma,3))
json.dump(out,open('grade.json','w'),indent=1); print(out)
