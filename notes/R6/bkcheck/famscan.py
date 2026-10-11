# Family scan: base +-Sigma(A), fibre K, Y_{-1/n}(K) for n = 0..NMAX (n=0: base).
import bkc, itertools, random, json, sys, time
from fractions import Fraction as Fr
from math import gcd, prod
from multiprocessing import Pool

def nontorus(t):
    a=prod(t)
    for i in range(3):
        P=a//t[i]
        if t[i]%P in (1,P-1) or P<=2 and False: return False
    return True

def Ymember(A,K,n,orient):
    """Y_{-1/n}(K) of orient*Sigma(A): returns (o, B) with B ordered (other, other, surgered)."""
    A=list(A); P=prod(A)//A[K]; j,l=[i for i in range(3) if i!=K]
    if orient==1: m=A[K]+n*P; o=1 if m>0 else -1
    else:          # (-Sigma)_{-1/n} = -(Sigma_{+1/n}) = -sgn(aK-nP) Sigma(|aK-nP|)
        m=A[K]-n*P; o=-1 if m>0 else 1
    return o,(A[j],A[l],abs(m))

def job(arg):
    o,B=arg
    if min(B)==1: return arg,(None,[],0)
    R=bkc.enumerate_reps(B)
    if o==1: return arg,(R['cmin'],R['argmin'],R['N'])
    return arg,(Fr(3,8)-R['cmax'],R['argmax'],R['N'])

if __name__=="__main__":
    random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 1)
    NMAX=int(sys.argv[2]) if len(sys.argv)>2 else 5
    out=sys.argv[3] if len(sys.argv)>3 else "fam.json"
    allt=[t for t in itertools.combinations(range(2,200),3) if prod(t)<=8000 and all(gcd(x,y)==1 for x,y in itertools.combinations(t,2)) and nontorus(t)]
    small=[t for t in allt if prod(t)<=2000]; big=[t for t in allt if prod(t)>2000]
    print(len(small),len(big))
    S=random.sample(small,min(140,len(small)))+random.sample(big,30)
    for t in [(3,5,17),(2,5,7),(2,17,147),(3,7,23),(3,23,71),(2,5,23),(3,13,119),(3,20,77),(3,7,19),(3,5,13)]:
        if t not in S: S.append(t)
    fams=[(t,K,o) for t in S for K in range(3) for o in (1,-1)]
    tasks=set()
    for t,K,o in fams:
        for n in range(0,NMAX+1): tasks.add(Ymember(t,K,n,o))
    tasks=sorted(tasks,key=lambda x:prod(x[1]))
    print("families",len(fams),"manifolds",len(tasks)); sys.stdout.flush()
    t0=time.time(); res={}
    with Pool(4) as p:
        for k,(arg,v) in enumerate(p.imap_unordered(job,tasks,chunksize=4)):
            res[arg]=v
    print("time",time.time()-t0)
    data=[]
    for t,K,o in fams:
        row=[]
        for n in range(NMAX+1):
            arg=Ymember(t,K,n,o); v=res[arg]
            row.append(dict(o=arg[0],B=arg[1],ell=None if v[0] is None else str(v[0]),arg=v[1],N=v[2]))
        data.append(dict(A=t,K=K,o=o,rows=row))
    json.dump(data,open(out,"w"))
