import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/r8/code8')
from cone import *
for name in ['5_2','6_1','K11n42','7_4']:
    M=snappy.Manifold(name); c0=float(M.chern_simons()); V0=float(M.volume())
    for sl in [(2,1),(-2,1),(5,2),(-3,2),(6,1),(1,3),(7,-2),(10,3)]:
        try:
            d=path(M,0,sl,n=200)
        except Exception as e:
            print(name,sl,'ERR',e); continue
        chk=mod(d['cs_fill']-c0-d['J'],0.5); chkv=d['vol_fill']-V0-d['Ivol']
        # alternative dual l+m
        r,s=d['dual']; p,q=sl
        d2=path(M,0,sl,n=200,dual_rs=(r+p,s+q))
        print(name,sl,'eps',d['eps'],'J=%.6f'%d['J'],'J(l+m)-J=%.6f'%(d2['J']-d['J']),'csChk(mod1/2)=%.1e'%chk,'volChk=%.1e'%chkv,'bad',d['bad'],'jump %.3f'%d['jump'])
