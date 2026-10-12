"""(c) exact SU(2)/SL(2,R) analogue of (P) on Y_{+-2}(T(p,q)).
Exact CS (SU(2) units) of a flat connection on Y_N on arc (k,l) at pillowcase point a:
   CS(Y_N,a) = -( pq (a^2 - a0^2) - N a^2 )  mod 1     [gap16/tk.py, FS/DLME-calibrated; re-checked below on Sigma(2,3,5), Sigma(2,3,7)]
Analogue of the hyperbolic set-up: base point a=1/2 on the line b = k/2 - pq a with k - pq odd (tr mu = tr lambda = -2, 'S^3-lift'),
H_mu = 4 pi i (a-1/2), H_lambda = 4 pi i (b - b(1/2)); cone angle alpha defined by N H_mu + H_lambda = i alpha.
Endpoint alpha = 2 pi:  a_N = 1/2 - 1/(2(pq-N));  tau_N(alpha) = Im H_mu = alpha/(N-pq);  int_0^{2pi} tau_N = 2 pi^2/(N-pq).
Compare exact D = CS(Y_2,a_2) - CS(Y_-2,a_-2) with
   manuscript (P), SU(2) units:  D = c_2 - c_-2 + (1/4pi^2) int (tau_2 - tau_-2) = Delta          (c_2 == c_-2 mod 1)
   corrected:                    D = (1/8pi^2) int (tau_2 - tau_-2) = Delta/2
"""
from fractions import Fraction as Fr
import sys
sys.path.insert(0,'/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/gap16/triangle-code')
import tk

def CS(p,q,N,a,a0): return (-(p*q*(a*a-a0*a0) - N*a*a)) % 1

# sanity: Brieskorn spheres (FS values -e^2/(4 a1 a2 a3))
def FS(a1,a2,a3,N,p,q):
    vals=[]
    for (k,l,amin,amax) in tk.arcs(p,q):
        for g in tk.gens(p,q,N):
            pass
    return sorted({ (g['CSD']) for g in tk.gens(p,q,N)})
print('Sigma(2,3,7)=S^3_{-1}(T23): CS =', [str(c) for c in FS(2,3,7,-1,2,3)], ' FS: -25/168,-121/168 ->', str(Fr(-25,168)%1), str(Fr(-121,168)%1))
print('Sigma(2,3,5)=S^3_{+1}(T23): CS =', [str(c) for c in FS(2,3,5,1,2,3)], ' FS: -1/120,-49/120 ->', str(Fr(-1,120)%1), str(Fr(-49,120)%1))

print()
print('%-8s %-6s %-10s %-10s %-9s %-9s %-9s %s'%('T(p,q)','arc','a_2','a_-2','D_exact','Delta/2','Delta','SU(2) both?'))
for (p,q) in [(2,3),(2,5),(3,4),(2,7),(3,5),(4,5),(2,9),(3,7),(5,6),(4,7),(3,8),(5,7)]:
    pq=p*q
    for (k,l,amin,amax) in tk.arcs(p,q):
        if (k-pq)%2==0: continue
        # reducible endpoint a0 with b(a0) integer: choose amin (b = k/2 - pq a0 integer?)
        a0=amin
        assert (Fr(k,2)-pq*a0).denominator==1
        a2=Fr(1,2)-Fr(1,2*(pq-2)); am2=Fr(1,2)-Fr(1,2*(pq+2))
        D=(CS(p,q,2,a2,a0)-CS(p,q,-2,am2,a0))%1
        Delta=(Fr(1,2)*(Fr(1,2-pq)-Fr(1,-2-pq)))   # (1/4pi^2) int(tau_2 - tau_-2)
        both = (amin<am2<amax) and (amin<a2<amax)
        ok_corr = (D-Delta/2)%1==0; ok_ms=(D-Delta)%1==0
        print('%-8s %-6s %-10s %-10s %-9s %-9s %-9s %s  corrected:%s manuscript:%s'%('T(%d,%d)'%(p,q),(k,l),a2,am2,D,Delta/2%1,Delta%1,both,ok_corr,ok_ms))
