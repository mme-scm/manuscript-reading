"""Closed form far along chains: fit A, beta_0, beta_1 from j = 0..3 and test up to j = JMAX."""
import sys, random
from fractions import Fraction as F
from math import gcd, isqrt
sys.path.insert(0, '.')
import bk
JMAX = 40
random.seed(3)
pairs = [(2,3),(2,5),(3,4),(3,5),(2,7),(3,7),(4,5),(5,7),(3,8),(2,9),(5,6),(3,11),(4,9),(7,8),(5,9),(2,15),(3,13),(7,9)]
nchains = nok = 0
for a1, a2 in pairs:
    P = a1*a2
    rs = [r for r in range(1, P) if gcd(r, P) == 1]
    for r in random.sample(rs, min(4, len(rs))) + ([2] if P % 2 and 2 in rs else []):
        ell = {}
        for j in range(0, JMAX+1):
            m = r + j*P
            if m == 1: continue
            ell[j] = bk.manifold((a1, a2, m), 1)['ell']
        ok = True; info = []
        for eps in (0, 1):
            js = [j for j in sorted(ell) if j % 2 == eps]
            j1, j2 = js[0], js[1]
            m1, m2 = r + j1*P, r + j2*P
            g1, g2 = ell[j1] + F(j1,16), ell[j2] + F(j2,16)
            B = (g1 - g2) / (F(1,m1) - F(1,m2)); A = g1 - B/m1
            ok &= all(ell[j] == A - F(j,16) + B/(r + j*P) for j in js)
            info.append((A, isqrt((B*16*P).numerator) if (B*16*P).denominator == 1 else B*16*P))
        nchains += 1; nok += ok
        if not ok or (a1,a2) in [(3,5),(2,3)]:
            print((a1,a2,r), "holds for j=0..%d:" % JMAX, ok, info)
print("chains tested:", nchains, " closed form exact up to j=%d in:" % JMAX, nok)
