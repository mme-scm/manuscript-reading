# Riemannian-level (SnapPy units mod 1) test of the Schlafli bookkeeping on homeomorphic pairs, with GENUINE SL2C lifts
import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/r8/code8')
from cone import *; from spin import *
def ext_types(types,sl):
    p,q=sl
    return [t for t in types if abs(((p*t[0]+q*t[1])-0.5)%1)<1e-9]
def rtest(name, s1, s2, n=200, orient=-1, M=None):
    E=snappy.Manifold(name) if M is None else M
    cE=float(E.chern_simons())
    P,res=cusp_types_all(E)
    types=sorted(t[0] for t in realizable(P,res))
    d1=path(E,0,s1,n=n); d2=path(E,0,s2,n=n)
    e1=ext_types(types,s1); e2=ext_types(types,s2)
    P1=e1[0]; P2=e2[0]
    B1=d1['dual'][0]*P1[0]+d1['dual'][1]*P1[1]; B2=d2['dual'][0]*P2[0]+d2['dual'][1]*P2[1]
    chi=(round(2*((P2[0]-P1[0])%1))%2, round(2*((P2[1]-P1[1])%1))%2)
    dR=(chi[0]*P1[1]-chi[1]*P1[0])          # R_E(P2) - R_E(P1) mod 1 (P2 = P1 + chi/2 up to lattice)
    if orient==-1: T=2*cE+(B1+d1['J'])+(B2+d2['J'])+dR
    else: T=(B1+d1['J'])-(B2+d2['J'])-dR
    return dict(name=name,s=(s1,s2),types=types,P=(P1,P2),B=(B1,B2),dR=dR,J=(d1['J'],d2['J']),cs=cE,T=T,Tmod=mod(T,1),
                bad=(d1['bad'],d2['bad']),maxtor=(d1['maxtor'],d2['maxtor']),chk=(mod(d1['cs_fill']-cE-d1['J'],0.5),mod(d2['cs_fill']-cE-d2['J'],0.5)))
if __name__=='__main__':
    cases=[('o9_39009',(-1,3),(-3,2)),('m135',(1,3),(3,1)),('t12051',(1,1),(2,-1)),
           ('4_1',(2,1),(-2,1)),('4_1',(6,1),(-6,1)),('4_1',(2,3),(-2,3)),('4_1',(10,3),(-10,3)),('6_3',(2,1),(-2,1)),('8_3',(2,1),(-2,1)),('8_9',(10,3),(-10,3)),('8_9',(6,5),(-6,5))]
    for c in cases:
        r=rtest(*c)
        print('%-9s %-18s types %s P %s B %s dR %+.1f J=(%.6f,%.6f) 2cs=%.6f  T=%.6f  T mod 1 = %+.6f  bad %s chk %s'%(r['name'],r['s'],r['types'],r['P'],r['B'],r['dR'],r['J'][0],r['J'][1],2*r['cs'],r['T'],r['Tmod'],r['bad'],['%.0e'%x for x in r['chk']]))
