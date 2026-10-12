import numpy as np, snappy, warnings
warnings.filterwarnings('ignore')
from kkpath import *
p,q=11,3; C=Curve(p,q)
E=snappy.RationalTangle(q,p).denominator_closure().exterior()
ugeo=C.roots(-1+0j)[0]; print('ugeo',ugeo)
N=2; n=40
H=cone_path_H(E,N,n)
X=[]
for k in range(n+1):
    s=k/n
    if k==0: X.append((0j,0j)); continue
    Y=E.copy(); Y.dehn_fill((N/s,1/s)); ci=Y.cusp_info()[0]; X.append((complex(ci['holonomies'][0]),complex(ci['holonomies'][1])))
for sg in (1,-1):
    u=ugeo; Mprev=-1+0j
    for k in range(1,n+1):
        Mk=-np.exp(sg*X[k][0]/2)
        seg=lambda t: Mprev+(Mk-Mprev)*t
        m,uu,ll=track(C,seg,u,hmax=0.05); u=uu[-1]; Mprev=Mk
        if k in (1,2,10,20,40):
            L=C.L(Mk,u)
            print(sg,k,'L_S',np.round(L,6),' -exp(sg Hl/2)',np.round(-np.exp(sg*X[k][1]/2),6), ' 1/that', np.round(-np.exp(-sg*X[k][1]/2),6))
