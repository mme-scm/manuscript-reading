import numpy as np, snappy, warnings
warnings.filterwarnings('ignore')
from kkpath import *
p,q=11,3; C=Curve(p,q)
E=snappy.RationalTangle(q,p).denominator_closure().exterior()
tS=complex(E.cusp_info()[0]['shape'])
for u0 in C.roots(-1+0j):
    M1=-np.exp(1e-6*np.exp(0.4j)); r=C.roots(M1); u1=r[np.argmin(abs(r-u0))]
    tau=np.log(C.L(M1,u1)/C.L(-1+0j,u0))/np.log(-M1); print(u0,tau)
N=2
for s in (0.05,0.1,0.5):
    X=E.copy(); X.dehn_fill((N/s,1/s)); ci=X.cusp_info()[0]
    print(s, ci['holonomies'], 'check N Hm + Hl =', N*complex(ci['holonomies'][0])+complex(ci['holonomies'][1]), 2j*np.pi*s)
