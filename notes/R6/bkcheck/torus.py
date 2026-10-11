# Claim 5: ell(S^3_{-1/n}(T(p,q))) = ell(Sigma(p,q,pqn+1)) = 3/8 - 5/(16pq) - n/16 + beta_n^2/(16pq(pqn+1))
import bkc
from fractions import Fraction as Fr
from math import gcd
pq_list=[(6,7),(7,8),(5,9),(7,9),(8,9),(5,11),(9,10),(3,16),(11,12),(2,3),(2,5),(2,7),(3,4),(3,5),(2,9),(3,7),(4,5),(2,11),(3,8),(5,6),(4,7),(5,7),(2,15),(3,10)]
bad=0; tot=0
for p,q in pq_list:
    for n in range(1,7):
        m=p*q*n+1
        v=bkc.ell((p,q,m))
        b=3 if n%2==0 else p*q-3
        f=Fr(3,8)-Fr(5,16*p*q)-Fr(n,16)+Fr(b*b,16*p*q*m)
        tot+=1
        if v!=f:
            bad+=1; print("MISMATCH",p,q,n,v,f)
print("torus-knot formula: tested",tot,"mismatches",bad)
# examples
print(bkc.ell((2,3,7)),bkc.ell((2,3,13)))
