# Rotation-form criterion with SnapPy real generalized Dehn filling (t,1), t in [-2,2].
import snappy, warnings, math, json, sys
from multiprocessing import Pool
warnings.filterwarnings('ignore')
def job(r):
    name=r['name']
    try:
        M=snappy.Manifold(name); n=80
        ts=[-2+4*j/n for j in range(n+1)]; us=[]; bad=0; prev=None; jump=0
        for t in ts:
            X=M.copy(); X.dehn_fill((t,1))
            if not X.solution_type().startswith('all tetrahedra positively'): bad+=1
            u=complex(X.cusp_info()[0]['holonomies'][0])/2; us.append(u)
            if prev is not None: jump=max(jump,abs(u-prev))
            prev=u
        f=[u*u for u in us]; h=4/n
        I=h/3*(f[0]+f[-1]+4*sum(f[1:-1:2])+2*sum(f[2:-1:2]))
        D=I.real/(2*math.pi**2)
        return dict(name=name, Drot=D, Dcone=r.get('Delta'), maxu=max(abs(u) for u in us), bad=bad, jump=jump)
    except Exception as e: return dict(name=name, err=str(e))
if __name__=='__main__':
    R=[r for r in json.load(open('../survey10.json')) if 'err' not in r]
    with Pool(8) as p: out=p.map(job,R,chunksize=4)
    json.dump(out,open('rot_survey.json','w'))
    ok=[o for o in out if 'err' not in o]
    clean=[o for o in ok if o['bad']==0 and o['jump']<0.2]
    print('knots',len(ok),'clean pencils',len(clean))
    agree=[abs(o['Drot']-o['Dcone']) for o in clean]
    print('max |Drot-Dcone| on clean:',max(agree), ' #>1e-3:',sum(a>1e-3 for a in agree))
    print('max over clean of max|u_t|:',max(o['maxu'] for o in clean),' (pi/2=1.5708)')
    print('max |Drot| clean:',max(abs(o['Drot']) for o in clean))
    dirty=[o for o in ok if o not in clean]
    print('dirty:',[(o['name'],o['bad'],round(o['maxu'],3),round(o['Drot'],4),round(o['Dcone'],4)) for o in dirty][:30])
