# find hyperbolic amphichiral fillings of given cusped manifolds (small slopes)
import snappy, warnings, json, sys, math
from multiprocessing import Pool
warnings.filterwarnings('ignore')
def gcd(a,b):
    while b: a,b=b,a%b
    return abs(a)
def job(args):
    name,B=args
    E=snappy.Manifold(name); E.chern_simons()
    out=[]
    for p in range(-B,B+1):
        for q in range(0,B+1):
            if gcd(p,q)!=1 or (q==0 and p!=1): continue
            X=E.copy(); X.dehn_fill((p,q))
            if not X.solution_type().startswith('all tetrahedra positively'): continue
            try: cs=float(X.chern_simons())
            except: continue
            y=cs%0.5; d=min(y,0.5-y)
            if d>1e-7: continue
            if float(X.volume())<0.9: continue
            try:
                if X.symmetry_group().is_amphicheiral(): out.append(((p,q),str(X.homology()),float(X.volume())))
            except Exception as e: pass
    return (name,out)
if __name__=='__main__':
    names=sys.argv[1].split(','); B=int(sys.argv[2])
    with Pool(8) as P: res=P.map(job,[(n,B) for n in names])
    json.dump(res,open('amphi_fill_%s.json'%sys.argv[3],'w'))
    for n,o in res: print(n,o)
