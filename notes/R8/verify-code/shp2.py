import numpy as np, snappy, warnings, sys
warnings.filterwarnings('ignore')
from kkpath import Curve
def riley_shapes(p,q):
    C=Curve(p,q); out=[]
    for u0 in C.roots(-1+0j):
        M1=-np.exp(1e-6*np.exp(0.4j)); r=C.roots(M1); u1=r[np.argmin(abs(r-u0))]
        out.append(np.round(np.log(C.L(M1,u1)/C.L(-1+0j,u0))/np.log(-M1),4))
    return out
for (p,q) in [(19,4),(21,8),(29,12),(13,3),(17,3)]:
    E=snappy.RationalTangle(q,p).denominator_closure().exterior()
    Xs=E.copy(); Xs.dehn_fill((2/1e-3,1/1e-3)); hh=Xs.cusp_info()[0]['holonomies']
    tS=complex(hh[1])/complex(hh[0])
    print((p,q),'target',np.round(tS,4))
    for qq in sorted({q,p-q,pow(q,-1,p),p-pow(q,-1,p)}):
        print('    Riley b(%d,%d):'%(p,qq), riley_shapes(p,qq))
