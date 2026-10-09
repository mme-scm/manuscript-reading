import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/gap16/ell-code')
from math import gcd
from fractions import Fraction as Fr
from mixedwide import spec
from twistedw import sigma_torus

def ells(p, q, mirror):
    S = {(N, tw): spec(p, q, N, tw) for N in (2, -2) for tw in (False, True)}
    if not mirror:
        E = {k: min(v) for k, v in S.items()}
    else:
        E = {(N, tw): -max(S[(-N, tw)]) for (N, tw) in S}
    return E  # absolute normalisation

rows = []
for p in range(2, 12):
    for q in range(p + 1, 61):
        if gcd(p, q) != 1 or p*q > 120: continue
        for mir in (False, True):
            E = ells(p, q, mir)
            Lp = min(E[(2, False)], E[(2, True)]); Lm = min(E[(-2, False)], E[(-2, True)])
            Mp = max(E[(2, False)], E[(2, True)]); Mm = max(E[(-2, False)], E[(-2, True)])
            which_p = 'u' if E[(2, False)] <= E[(2, True)] else 'w'
            which_m = 'u' if E[(-2, False)] <= E[(-2, True)] else 'w'
            rows.append((('m' if mir else '') + 'T%d,%d' % (p, q), sigma_torus(p, q)*(-1 if mir else 1), Lp - Lm, Mp - Mm, which_p, which_m))
# figure-eight from notes/G-fig8.md (absolute normalisation): a=1/20, b=-1/20, c=1/80, d=-9/80
a, b, c, d = Fr(1,20), Fr(-1,20), Fr(1,80), Fr(-9,80)
rows.append(('4_1', 0, min(a,c)-min(b,d), max(a,c)-max(b,d), 'w', 'w'))
for r in rows[:12] + rows[-1:]:
    print('%-8s %4d  mingap=%-12s (%.5f)  maxgap=%-12s (%.5f)  argmin Y2:%s Y-2:%s' % (r[0], r[1], r[2], float(r[2]), r[3], float(r[3]), r[4], r[5]))
mg = [r[2] for r in rows]; Mg = [r[3] for r in rows]
print('cases', len(rows))
print('min-gap range: [%s, %s] = [%.5f, %.5f]' % (min(mg), max(mg), float(min(mg)), float(max(mg))))
print('max-gap range: [%s, %s] = [%.5f, %.5f]' % (min(Mg), max(Mg), float(min(Mg)), float(max(Mg))))
print('cases with min-gap < 1/16:', [(r[0], r[2]) for r in rows if r[2] < Fr(1,16)][:20])
print('cases with min-gap == 1/16:', [r[0] for r in rows if r[2] == Fr(1,16)][:20])
print('cases with min-gap == 1/8:', len([r for r in rows if r[2] == Fr(1,8)]))
pos = [r for r in rows if not r[0].startswith('m') and r[0] != '4_1']; neg = [r for r in rows if r[0].startswith('m')]
print('positive: min-gap in [%.5f, %.5f]; negative: [%.5f, %.5f]' % (float(min(r[2] for r in pos)), float(max(r[2] for r in pos)), float(min(r[2] for r in neg)), float(max(r[2] for r in neg))))
print('below 1/8:', [(r[0], r[1], str(r[2]), round(float(r[2]),5), r[4], r[5]) for r in rows if r[2] < Fr(1,8)])
