import snappy, warnings, json, sys
from multiprocessing import Pool
warnings.filterwarnings('ignore')
def job(i):
    try:
        M=snappy.OrientableClosedCensus[i]
        G=M.symmetry_group()
        if G.is_amphicheiral():
            X=snappy.Manifold(M.name()); X.chern_simons(); X.dehn_fill(M.cusp_info("filling")); return (repr(M), float(X.chern_simons()), str(M.homology()), str(G))
    except Exception as e:
        return ('ERR%d'%i, str(e)[:60])
    return None
if __name__=='__main__':
    N=len(snappy.OrientableClosedCensus)
    with Pool(8) as p: res=[r for r in p.map(job,range(N),chunksize=50) if r]
    json.dump(res,open('amphi_closed.json','w'))
    errs=[r for r in res if r[0].startswith('ERR')]
    ok=[r for r in res if not r[0].startswith('ERR')]
    print('census size',N,'amphichiral',len(ok),'errors',len(errs))
    def d(x):
        y=(x%0.5); return min(y,0.5-y)
    print('max dist of cs to 0 mod 1/2:', max(d(r[1]) for r in ok))
    print('dist to 1/4 mod 1/2 min:', min(abs((r[1]%0.5)-0.25) for r in ok))
    print([r for r in ok if d(r[1])>1e-6][:10])
    print('with Z/2 in H1:',sum(1 for r in ok if '2' in r[2]), ok[:5])
