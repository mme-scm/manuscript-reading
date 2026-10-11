# Larger L+/L- sample: random non-torus triples a<=AMAX, families with P<=PMAX, n=0..NMAX
import random, json, sys, itertools
from math import gcd, prod
from multiprocessing import Pool
from famscan import Ymember, job, nontorus
if __name__=="__main__":
    seed,AMAX,PMAX,NF,NMAX,out=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),sys.argv[6]
    random.seed(seed)
    fams=set()
    while len(fams)<NF:
        a1=random.randint(2,40); a2=random.randint(a1+1,200); 
        if a1*a2>AMAX: continue
        a3=random.randint(a2+1,max(a2+2,AMAX//(a1*a2)))
        t=(a1,a2,a3)
        if prod(t)>AMAX or not all(gcd(x,y)==1 for x,y in itertools.combinations(t,2)) or not nontorus(t): continue
        K=random.randrange(3); P=prod(t)//t[K]
        if P>PMAX: continue
        o=random.choice((1,1,-1))
        if o==-1 and t[K]>P: continue
        fams.add((t,K,o))
    fams=sorted(fams)
    tasks=sorted({Ymember(t,K,n,o) for t,K,o in fams for n in range(NMAX+1)},key=lambda x:prod(x[1]))
    print(len(fams),len(tasks),sum(prod(t)>2000 for t,_,_ in fams)); sys.stdout.flush()
    with Pool(4) as p: res=dict(p.imap_unordered(job,tasks,chunksize=2))
    data=[]
    for t,K,o in fams:
        rows=[]
        for n in range(NMAX+1):
            arg=Ymember(t,K,n,o); v=res[arg]
            rows.append(dict(o=arg[0],B=arg[1],ell=None if v[0] is None else str(v[0]),arg=v[1],N=v[2]))
        data.append(dict(A=t,K=K,o=o,rows=rows))
    json.dump(data,open(out,"w"))
