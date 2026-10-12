import snappy, warnings, json
from multiprocessing import Pool
warnings.filterwarnings('ignore')
def job(nm):
    try:
        M=snappy.Manifold(nm)
        if M.solution_type()!='all tetrahedra positively oriented': M=M.copy(); M.randomize()
        G=M.symmetry_group()
        if G.is_amphicheiral():
            return (nm, float(M.chern_simons()), str(M.homology()), str(G))
    except Exception as e:
        return ('ERR '+nm, str(e)[:60])
    return None
if __name__=='__main__':
    cnt={3:1,4:1,5:2,6:3,7:7,8:21,9:49,10:165}
    knots=['%d_%d'%(c,k) for c in cnt for k in range(1,cnt[c]+1)]
    knots+=['K11a%d'%k for k in range(1,368)]+['K11n%d'%k for k in range(1,186)]
    knots+=['K12a%d'%k for k in range(1,1289)]+['K12n%d'%k for k in range(1,889)]
    cens=[snappy.OrientableCuspedCensus(num_cusps=1)[i].name() for i in range(0,len(snappy.OrientableCuspedCensus(num_cusps=1)),1) ][:8000]
    with Pool(8) as p:
        rk=[r for r in p.map(job,knots,chunksize=20) if r]
        rc=[r for r in p.map(job,cens,chunksize=50) if r]
    json.dump([rk,rc],open('amphi_cusped.json','w'))
    def d(x):
        y=(x%0.5); return min(y,0.5-y)
    for lab,res in (('knots',rk),('census1cusp',rc)):
        ok=[r for r in res if not r[0].startswith('ERR')]
        print(lab,'amphichiral:',len(ok),'errors',len(res)-len(ok))
        print('  cs=0 mod 1/2:',sum(1 for r in ok if d(r[1])<1e-6),' cs=1/4 mod 1/2:',sum(1 for r in ok if abs(d(r[1])-0.25)<1e-6),' other:',[r for r in ok if 1e-6<d(r[1])<0.25-1e-6][:5])
        print('  examples 1/4:',[r for r in ok if abs(d(r[1])-0.25)<1e-6][:12])
