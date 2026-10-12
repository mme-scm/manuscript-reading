import snappy, warnings, json
warnings.filterwarnings('ignore')
R=json.load(open('survey10.json'))
rows=[]
for r in R:
    if 'err' in r: continue
    M=snappy.Manifold(r['name']); t=complex(M.cusp_info()[0]['shape'])
    x,y=t.real,t.imag
    lo=0.5*((2+x)/abs(2+t)**2-(x-2)/abs(t-2)**2)
    rows.append((r['name'],y,r['Delta'],lo))
rows.sort(key=lambda z:z[1])
print('min Im tau:',[(n,round(y,3)) for n,y,_,_ in rows[:5]])
import math
err=[abs(abs(D)-abs(l)) for _,_,D,l in rows]
print('max | |Delta| - |NZ leading| |:',max(err),' median:',sorted(err)[len(err)//2])
print('worst NZ fits:',sorted([(round(abs(abs(D)-abs(l)),3),n,round(D,3),round(l,3)) for n,_,D,l in rows],reverse=True)[:5])
