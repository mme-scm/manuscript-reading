# Topology check: Casson surgery formula lambda(Y_{1/m}) = lambda(Y) + m*Delta''(1)/2, Delta = Delta_{T(aj,ak)}.
# Claim: Sigma_{-1/n}(K) = sgn(aK+nP) Sigma(..,|aK+nP|,..) for all integers n (n<0 = +1/|n| surgery).
import bkc, itertools
from fractions import Fraction as Fr
from math import gcd, prod
def lamN(A):  # lambda of link-oriented Sigma(A) via rep count; S^3 -> 0
    if min(A)==1: return Fr(0)
    return Fr(-bkc.enumerate_reps(tuple(A))['N'],2)
def lam_sig(A):  # via Brieskorn signature formula
    if min(A)==1: return Fr(0)
    return Fr(bkc.brieskorn_sigma(tuple(A)),8)
# Seifert-invariant algebra check: filling mu + k*lambda0 of exterior
def seif_fill(A,K,k):
    b=bkc.bvec(A); a=prod(A); P=a//A[K]
    j,l=[i for i in range(3) if i!=K]
    D=b[j]*A[l]+A[j]*b[l]
    x=A[K]+k*P; y=b[K]-k*D
    H=abs(P*y+D*x)
    ebar=Fr(b[j],A[j])+Fr(b[l],A[l])+Fr(y,x)
    return H, ebar, Fr(1,P*x)
triples=[t for t in itertools.combinations(range(2,30),3) if all(gcd(x,y)==1 for x,y in itertools.combinations(t,2)) and prod(t)<=1200]
triples+= [(2,3,1),(2,5,1),(3,4,1),(3,5,1),(2,7,1)]
ok=bad=alt_ok=0; badlist=[]; sf_bad=0
for A in triples:
    for K in range(3):
        if A[K]==1 and min(A[:K]+A[K+1:])==1: continue
        j,l=[i for i in range(3) if i!=K]
        d2=Fr((A[j]**2-1)*(A[l]**2-1),24)
        L0=lamN(A)
        for n in [-4,-3,-2,-1,1,2,3,4]:
            H,eb,pred=seif_fill(A,K,n)
            if H!=1 or eb!=pred: sf_bad+=1
            o,B=bkc.surg(A,K,n)
            lB=o*lamN(B)
            if lB==L0-n*d2: ok+=1
            else: bad+=1; badlist.append((A,K,n,lB,L0-n*d2))
            # wrong-sign alternative would need lB == L0 + n*d2
            if lB==L0+n*d2: alt_ok+=1
print("Casson checks: pass",ok,"fail",bad,badlist[:5])
print("opposite slope sign would pass in",alt_ok,"cases (should be ~0)")
print("Seifert algebra failures",sf_bad)
# rep count vs Brieskorn signature on some surgered manifolds
c=0;m=0
for A in triples[:60]:
    for K in range(3):
        for n in (1,2,3):
            o,B=bkc.surg(A,K,n)
            if min(B)>1:
                c+=1; m+= lamN(B)!=lam_sig(B)
print("rep-count vs Brieskorn-signature lambda on",c,"surgered manifolds: mismatches",m)
