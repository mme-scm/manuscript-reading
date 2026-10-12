import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/r8/code8')
from cone import *; from spin import *
E=snappy.Manifold('o9_39009'); cE=float(E.chern_simons())
P,tr,res,G,chis=cusp_types(E)
print('SnapPy lift cusp type',P,'traces',tr,'restrictions of H^1(Z/2):',res, 'nchis',len(chis))
types={ ((P[0]+cm/2)%1,(P[1]+cl/2)%1) for cm,cl in res}
print('available cusp types',types)
n=int(sys.argv[1]) if len(sys.argv)>1 else 300
out={}
for sl in [(-1,3),(-3,2)]:
    d=path(E,0,sl,n=n); r,s=d['dual']; p,q=sl
    ext=[t for t in types if abs(((p*t[0]+q*t[1])-0.5)%1)<1e-9 or abs(((p*t[0]+q*t[1])-0.5)%1-1)<1e-9]
    print(sl,'dual',(r,s),'eps',d['eps'],'J=%.9f'%d['J'],'bad',d['bad'],'jump %.4f'%d['jump'],'maxtor %.3f'%d['maxtor'],'cs_fill %.9f'%d['cs_fill'],'chk mod1/2 %.1e'%mod(d['cs_fill']-cE-d['J'],0.5),'extendable types',ext)
    out[sl]=(d,ext)
d1,e1=out[(-1,3)]; d2,e2=out[(-3,2)]
common=set(e1)&set(e2)
print('common extendable cusp types:',common)
for t in common:
    B1=d1['dual'][0]*t[0]+d1['dual'][1]*t[1]; B2=d2['dual'][0]*t[0]+d2['dual'][1]*t[1]
    T=2*cE+B1+B2+d1['J']+d2['J']
    print('type',t,'B0s',B1,B2,'T = 2cs(E)+B1+B2+J1+J2 = %.9f  -> mod 1: %.9f'%(T,mod(T,1)))
print('J1+J2 = %.9f ; 2cs(E) = %.9f'%(d1['J']+d2['J'],2*cE))
