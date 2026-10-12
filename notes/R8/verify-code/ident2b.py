import snappy, warnings
from math import gcd
warnings.filterwarnings('ignore')
for p in range(7,30,2):
    for q in range(1,p//2+1):
        if gcd(p,q)!=1: continue
        try:
            L=snappy.RationalTangle(q,p).denominator_closure()
            if len(L.link_components)!=1: continue
            E=L.exterior()
            ids=[str(m) for m in E.identify()]
            out=[]
            for N in (2,-2):
                X=E.copy(); X.dehn_fill((N,1)); out.append(X.solution_type()[:16])
            print(p,q,ids,out, 'shape',complex(E.cusp_info()[0]['shape']))
        except Exception as e:
            print(p,q,'err',str(e)[:60])
