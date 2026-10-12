# Independent count of irreducible SU(2) (projective) reps of S^3_N(T(p,q)), N=+-2, both bundles,
# from the arcs of R*(T(p,q)) in the pillowcase: x^p=y^q, mu = x^r y^s (rq+sp=1), lambda = x^p mu^{-pq}.
import numpy as np, sys
from fractions import Fraction as F
def su2(axis, ang):  # exp(ang * axis . (i,j,k)), quaternion as 2x2
    n=np.array(axis)/np.linalg.norm(axis)
    I=np.array([[1j,0],[0,-1j]]); J=np.array([[0,1],[-1,0]]); K=np.array([[0,1j],[1j,0]])
    return np.cos(ang)*np.eye(2)+np.sin(ang)*(n[0]*I+n[1]*J+n[2]*K)
def mpow(M,e):
    return np.linalg.matrix_power(M,e) if e>=0 else np.linalg.matrix_power(np.linalg.inv(M),-e)
def count(p,q,N,eps,M=4000):
    # find r,s with r q + s p = 1
    r=next(r for r in range(-p*q,p*q) if (1-r*q)%p==0); s=(1-r*q)//p
    tot=0; pts=[]
    for k in range(1,p):
        for l in range(1,q):
            if (k-l)%2: continue
            X=su2([1,0,0],np.pi*k/p)
            th=np.linspace(1e-6,np.pi-1e-6,M)
            vals=[]
            for t in th:
                Y=su2([np.cos(t),np.sin(t),0],np.pi*l/q)
                mu=mpow(X,r)@mpow(Y,s)
                ca=np.clip(np.real(np.trace(mu))/2,-1,1); a=np.arccos(ca)/(2*np.pi)  # a in [0,1/2]
                # lambda = (-1)^k mu^{-pq}; b = -pq*a + k/2 in the eigenline of mu; condition mu^N lambda = (-1)^eps
                # => N a - pq a + k/2 - eps/2 in Z  (using the e^{2 pi i a} eigenline; same for the other)
                vals.append(N*a-p*q*a+(k-eps)/2)
            vals=np.array(vals)
            # count crossings of integers by vals as theta runs over (0,pi)
            fl=np.floor(vals)
            c=int(np.sum(np.abs(np.diff(fl))))
            tot+=c
    return tot
for (p,q) in [(2,3),(2,5),(3,4),(3,5),(3,7),(4,5)]:
    print((p,q),'det', 1 if (p%2 and q%2) else (p if q%2==0 else q),
          {f'N={N},w={e}':count(p,q,N,e) for N in (2,-2) for e in (0,1)})
