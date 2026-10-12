# search multi-cusped census for Ren-type purely cosmetic data: orientation-preserving phi with a 2-cycle (i j),
# phi^2|T_i of order 3,4,6, and at least one more cusp.
import snappy, warnings, sys, json
import numpy as np
from multiprocessing import Pool
warnings.filterwarnings('ignore')
def mat(m): return np.array([[int(m[0,0]),int(m[0,1])],[int(m[1,0]),int(m[1,1])]])
def job(i):
    try:
        N=snappy.OrientableCuspedCensus(num_cusps=NC)[i]
        isos=N.is_isometric_to(N,return_isometries=True)
        out=[]
        for iso in isos:
            ci=iso.cusp_images(); cm=[mat(m) for m in iso.cusp_maps()]
            if round(np.linalg.det(cm[0]))!=1: continue
            for a in range(len(ci)):
                b=ci[a]
                if b!=a and ci[b]==a:
                    sq=cm[b]@cm[a]
                    tr=int(np.trace(sq))
                    if tr in (-1,0,1):
                        out.append((a,b,tr,cm[a].tolist(),cm[b].tolist()))
        return (N.name(),out) if out else None
    except Exception as e:
        return ('ERR',i,str(e)[:40])
if __name__=='__main__':
    NC=int(sys.argv[1]); a,b=int(sys.argv[2]),int(sys.argv[3])
    with Pool(8) as P: res=[r for r in P.map(job,range(a,b),chunksize=10) if r]
    json.dump(res,open('ren_search_%d.json'%NC,'w'))
    print(len(res)); [print(r) for r in res[:20]]
