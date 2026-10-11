# Claim 4: chains Sigma(aj,ak,m), m = r + jP, link-oriented, closed form ell = A* - (m^2-beta^2)/(16 P m)
import bkc, itertools, random, json, sys
from fractions import Fraction as Fr
from math import gcd, prod
from multiprocessing import Pool

def beta_of(lab,P,m):
    l=lab[3]; return abs(2*((l*P)%m)-m)

def job(arg):
    aj,ak,m=arg
    R=bkc.enumerate_reps((aj,ak,m))
    return arg,(R['cmin'],R['argmin'])

if __name__=="__main__":
    random.seed(7)
    JMAX=20
    pairs=[(x,y) for x in range(2,60) for y in range(x+1,60) if gcd(x,y)==1 and x*y<=110]
    chains=[]
    for _ in range(40):
        aj,ak=random.choice(pairs); P=aj*ak
        r=random.choice([r for r in range(2,P) if gcd(r,P)==1])
        chains.append((aj,ak,r))
    chains+= [(3,5,2),(3,5,14),(3,7,4),(5,7,8),(2,3,1),(3,5,1),(2,7,1),(3,5,14),(9,11,50),(7,13,45),(2,47,31),(3,31,61)]
    chains=sorted(set(chains))
    tasks=set()
    for aj,ak,r in chains:
        P=aj*ak
        for j in range(JMAX+1):
            m=r+j*P
            if m>1: tasks.add((aj,ak,m))
    # exceptional chain (3,77; 211)
    for j in range(0,9): tasks.add((3,77,211+231*j))
    tasks=sorted(tasks,key=lambda x:prod(x))
    print("chains",len(chains),"manifolds",len(tasks)); sys.stdout.flush()
    with Pool(4) as p:
        res=dict(p.imap_unordered(job,tasks,chunksize=8))
    out=[]
    for aj,ak,r in chains+[(3,77,211)]:
        P=aj*ak; rows=[]
        J = 8 if (aj,ak,r)==(3,77,211) else JMAX
        for j in range(J+1):
            m=r+j*P
            if m<=1: continue
            c,args=res[(aj,ak,m)]
            bs=sorted({beta_of(l,P,m) for l in args})
            rows.append(dict(j=j,m=m,ell=str(c),betas=bs,args=args))
        out.append(dict(aj=aj,ak=ak,r=r,P=P,rows=rows))
    json.dump(out,open("chains.json","w"))
