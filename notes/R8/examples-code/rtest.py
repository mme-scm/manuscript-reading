import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/r8/code8')
from cone import *; from spin import *
def rtest(name, s1, s2, n=200, orient=-1):
    """orient=-1: chirally cosmetic (sum), +1: purely cosmetic (difference)"""
    E=snappy.Manifold(name); cE=float(E.chern_simons())
    P,tr,res,G,chis=cusp_types(E)
    types={ ((P[0]+cm/2)%1,(P[1]+cl/2)%1) for cm,cl in res}
    out=[]
    for sl in (s1,s2):
        d=path(E,0,sl,n=n); p,q=sl
        ext=[t for t in types if abs(((p*t[0]+q*t[1])-0.5+1e-12)%1)<1e-9]
        out.append((d,ext))
    (d1,e1),(d2,e2)=out
    common=set(e1)&set(e2)
    rows=[]
    for t in common:
        B1=d1['dual'][0]*t[0]+d1['dual'][1]*t[1]; B2=d2['dual'][0]*t[0]+d2['dual'][1]*t[1]
        if orient==-1: T=2*cE+B1+B2+d1['J']+d2['J']
        else: T=B1-B2+d1['J']-d2['J']
        rows.append((t,B1,B2,T,mod(T,1)))
    return dict(name=name,cs=cE,types=types,ext=(e1,e2),J=(d1['J'],d2['J']),bad=(d1['bad'],d2['bad']),
                maxtor=(d1['maxtor'],d2['maxtor']),cs_fill=(d1['cs_fill'],d2['cs_fill']),rows=rows,
                chk=(mod(d1['cs_fill']-cE-d1['J'],0.5),mod(d2['cs_fill']-cE-d2['J'],0.5)))
if __name__=='__main__':
    for args in [('m135',(1,3),(3,1)),('t12051',(1,1),(2,-1)),('4_1',(2,1),(-2,1)),('4_1',(6,1),(-6,1)),('4_1',(2,3),(-2,3)),('6_3',(2,1),(-2,1)),('8_3',(2,1),(-2,1)),('8_9',(10,3),(-10,3))]:
        r=rtest(*args)
        print(r['name'],args[1:],'cs(E)=%.6f'%r['cs'],'types',r['types'],'ext',r['ext'],'J=(%.6f,%.6f)'%r['J'],'bad',r['bad'],'chk',['%.0e'%c for c in r['chk']])
        for row in r['rows']: print('    type',row[0],'B',row[1],row[2],'T=%.6f mod1=%.6f'%(row[3],row[4]))
