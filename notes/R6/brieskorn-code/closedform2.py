"""Further closed-form checks.  Usage: python3 closedform2.py rays.json
 1. A_0 == A_1 ?
 2. beta (16 P B = beta^2) vs FS invariant e of the minimiser: is beta = min |2e' - m| over e' = +-e mod 2a?
 3. Reversed side k <= -2 (m = |r+kP|): fit ell = A' + B'/m on parity classes; is B' = -g^2/(4P)?
 4. Value of ell at the special member Z_{-1} vs the reversed-side fit (the "jump").
"""
import sys, json
from fractions import Fraction as F
from math import isqrt
from collections import Counter

chains = json.load(open(sys.argv[1]))
cl = {tuple(x['key']): x for x in json.load(open(sys.argv[1].replace('.json', '_closed.json')))}
c1 = Counter(); c2 = Counter(); c3 = Counter(); c4 = Counter()
betas = {}
for ch in chains:
    key = (ch['a1'], ch['a2'], ch['r'])
    P, r = ch['P'], ch['r']
    x = cl[key]
    A0, A1 = F(x['A0']), F(x['A1'])
    c1[A0 == A1] += 1
    Z = {int(k): v for k, v in ch['Z'].items()}
    bs = []
    for eps in (0, 1):
        B = F(x['B%d' % eps])
        b2 = B * 16 * P
        beta = isqrt(b2.numerator)
        bs.append(beta)
        for j in range(max(x['j0_%d' % eps], 0), max(Z) + 1):
            if j % 2 != eps or Z[j]['ell'] is None:
                continue
            m = r + j * P
            a = P * m
            ok = False
            for mm in Z[j]['min']:
                e = mm['e'] % (2 * a)
                cands = {e, (-e) % (2 * a)}
                best = min(abs(2 * ep - m) for ep in cands)
                best2 = min(abs(2 * ep - m) % (2 * P * 0 + 10 ** 9) for ep in cands)
                # e only matters via e^2 mod 4a: compare CS directly
                cs = F(mm['CS'])
                ok |= (cs == F((m + beta) ** 2, 16 * P * m) % 1) or (cs == F((m - beta) ** 2, 16 * P * m) % 1)
            c2[ok] += 1
    betas[key] = bs
    # reversed side
    ks = [k for k in sorted(Z) if k <= -2 and Z[k]['ell'] is not None]
    for eps in (0, 1):
        kk = [k for k in ks if k % 2 == eps]
        if len(kk) < 3:
            continue
        m1, m2 = -(r + kk[0] * P), -(r + kk[1] * P)
        g1, g2 = F(Z[kk[0]]['ell']), F(Z[kk[1]]['ell'])
        Bp = (g1 - g2) / (F(1, m1) - F(1, m2))
        Ap = g1 - Bp / m1
        holds = all(F(Z[k]['ell']) == Ap + Bp / (-(r + k * P)) for k in kk)
        g2v = -Bp * 4 * P
        sq = g2v >= 0 and g2v.denominator == 1 and isqrt(g2v.numerator) ** 2 == g2v.numerator
        c3[(holds, sq)] += 1
        # same A' for both parities?
    # Z_{-1}
print("1. A_0 == A_1 :", dict(c1))
print("2. minimiser CS == (m +- beta)^2/(16 P m) mod 1  (i.e. FS e = (m +- beta)/2 up to e^2 mod 4a):", dict(c2))
print("3. reversed side k<=-2: (ell = A' + B'/m exactly on parity class, -4PB' a square):", dict(c3))
bc = Counter()
for key, (b0, b1) in betas.items():
    P = key[0] * key[1]
    bc[(min(b0, b1) == 0, max(b0, b1) == P)] += 1
print("   (min beta == 0, max beta == P):", dict(bc))
import itertools
print("   sample betas (a1,a2,r): beta_even, beta_odd")
for key in list(betas)[:60]:
    print("     ", key, betas[key], "  r parity", key[2] % 2)
