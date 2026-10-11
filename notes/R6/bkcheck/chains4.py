import json, sys
from math import gcd, prod
from multiprocessing import Pool
from chains import job, beta_of
if __name__=="__main__":
    pairs=[(3,77),(3,64),(2,101),(5,41),(4,49),(7,29)]
    JMAX=3
    chains=[(aj,ak,r) for aj,ak in pairs for r in range(2,aj*ak) if gcd(r,aj*ak)==1]
    tasks=sorted({(aj,ak,r+j*aj*ak) for aj,ak,r in chains for j in range(JMAX+1)},key=prod)
    print(len(chains),len(tasks)); sys.stdout.flush()
    with Pool(4) as p: res=dict(p.imap_unordered(job,tasks,chunksize=8))
    outl=[]
    for aj,ak,r in chains:
        P=aj*ak; rows=[]
        for j in range(JMAX+1):
            m=r+j*P; c,args=res[(aj,ak,m)]
            rows.append(dict(j=j,m=m,ell=str(c),betas=sorted({beta_of(l,P,m) for l in args}),args=args))
        outl.append(dict(aj=aj,ak=ak,r=r,P=P,rows=rows))
    json.dump(outl,open("chains4.json","w"))
