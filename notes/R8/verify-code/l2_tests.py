"""(b) L2 tests. (i) lens spaces L(p,1): SU(2) reps k -> e^{2 pi i k/p}; cs via the disk bundle D_p (reducible U(1) extension):
cs(k) = -c_1(L)^2 = -k^2/p  (rational self-intersection), independent of KK.  Twist by eps (p even): k -> k + p/2.
(ii) torus knots: chi-pairs (x, chi x) on Y_{+-2}(T(p,q)) from tk.gens (twisting by eps: a -> 1/2 - a, b -> -b)."""
from fractions import Fraction as Fr
import sys
sys.path.insert(0,'/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/gap16/triangle-code')
import tk
print('(i) lens spaces')
for p in (2,4,6,8,10):
    diffs=sorted({ (Fr(-(k+p//2)**2,p)-Fr(-k*k,p))%1 for k in range(p)})
    lk=Fr((p//2)**2,p)%1
    eps3 = (p%4==2)
    print('  L(%d,1): central rep cs=%s ; cs(rho*eps)-cs(rho) = %s ; self-linking of order-2 class = %s ; eps^3!=0: %s'%(
        p, Fr(-(p//2)**2,p)%1, [str(d) for d in diffs], lk, eps3))
print('(ii) torus knots, Y_N, N=+-2: chi-pairs')
for (p,q) in [(2,3),(2,5),(3,4),(2,7),(3,5),(4,5),(3,7),(5,6)]:
    for N in (2,-2):
        G=tk.gens(p,q,N)
        diffs=[]; unmatched=0
        for g in G:
            a2=Fr(1,2)-g['a']; b2=(-g['b'])%1
            k2=(p-g['k']) if q%2 else g['k']; l2=(q-g['l']) if p%2 else g['l']
            m=[h for h in G if h['a']==a2 and h['b']%1==b2 and (h['k'],h['l'])==(k2,l2)]
            if not m: unmatched+=1; continue
            diffs.append((m[0]['CSD']-g['CSD'])%1)
        print('  T(%d,%d) N=%+d: #gens=%d, chi-pair CS differences: %s, unmatched=%d'%(p,q,N,len(G),sorted({str(d) for d in diffs}),unmatched))
