import bkc, random, json, sys
from math import gcd, prod
from multiprocessing import Pool
from chains import job, beta_of
if __name__=="__main__":
    seed=int(sys.argv[1]); PLO,PHI=int(sys.argv[2]),int(sys.argv[3]); NCH=int(sys.argv[4]); JMAX=int(sys.argv[5]); out=sys.argv[6]
    random.seed(seed)
    pairs=[(x,y) for x in range(2,PHI) for y in range(x+1,PHI//2+1) if gcd(x,y)==1 and PLO<=x*y<=PHI]
    chains=set()
    while len(chains)<NCH:
        aj,ak=random.choice(pairs); P=aj*ak
        r=random.choice([r for r in range(2,P) if gcd(r,P)==1])
        chains.add((aj,ak,r))
    chains=sorted(chains)
    tasks=sorted({(aj,ak,r+j*aj*ak) for aj,ak,r in chains for j in range(JMAX+1)},key=prod)
    print(len(chains),len(tasks)); sys.stdout.flush()
    with Pool(4) as p: res=dict(p.imap_unordered(job,tasks,chunksize=4))
    outl=[]
    for aj,ak,r in chains:
        P=aj*ak; rows=[]
        for j in range(JMAX+1):
            m=r+j*P; c,args=res[(aj,ak,m)]
            rows.append(dict(j=j,m=m,ell=str(c),betas=sorted({beta_of(l,P,m) for l in args}),args=args))
        outl.append(dict(aj=aj,ak=ak,r=r,P=P,rows=rows))
    json.dump(outl,open(out,"w"))
