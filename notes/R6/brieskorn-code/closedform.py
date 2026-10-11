"""Closed form along chains (link-oriented members j >= 0):
    ell(Z_j) = A_eps - j/16 + B_eps/m_j,   m_j = r + jP,   eps = j mod 2.
Fit (A,B) on each parity class from the two largest-j points; record the least j0 from which
the form holds exactly.  Then T(j) = ell(Z_j)-ell(Z_{j+2}) = 1/8 + 2P B_eps/(m_j m_{j+2}).
Also tests B = beta^2/(16P) with beta rational of small denominator, and relates B=0 to traceless.
Usage: python3 closedform.py rays.json"""
import sys, json
from fractions import Fraction as F
from math import isqrt
from collections import Counter

chains = json.load(open(sys.argv[1]))
res = []
for ch in chains:
    P, r = ch['P'], ch['r']
    Z = {int(k): v for k, v in ch['Z'].items()}
    J = max(Z)
    rec = dict(key=(ch['a1'], ch['a2'], r), torus=ch['torus'])
    for eps in (0, 1):
        js = [j for j in range(0, J + 1) if j % 2 == eps and Z[j]['ell'] is not None]
        j1, j2 = js[-2], js[-1]
        m1, m2 = r + j1 * P, r + j2 * P
        g1, g2 = F(Z[j1]['ell']) + F(j1, 16), F(Z[j2]['ell']) + F(j2, 16)
        # g = A + B/m
        B = (g1 - g2) / (F(1, m1) - F(1, m2))
        A = g1 - B / m1
        j0 = j2
        for j in reversed(js):
            if F(Z[j]['ell']) == A - F(j, 16) + B / (r + j * P):
                j0 = j
            else:
                break
        tl = all(any(mm['traceless'] for mm in Z[j]['min']) for j in js if j >= j0)
        rec[eps] = dict(A=A, B=B, j0=j0, nj=len([j for j in js if j >= j0]), tl=tl)
    res.append(rec)

cnt = Counter()
for x in res:
    for eps in (0, 1):
        d = x[eps]
        cnt[('holds from j0=%d' % d['j0'], 'torus' if x['torus'] else 'nontorus')] += 1
print("closed form ell(Z_j) = A - j/16 + B/m_j on parity classes; first j from which it holds exactly:")
for k, v in sorted(cnt.items()):
    print("   ", k, v)
negB = [(x['key'], eps, x[eps]['B']) for x in res for eps in (0, 1) if x[eps]['B'] < 0]
print("classes with B < 0:", len(negB), negB[:10])
zeroB = [(x['key'], eps) for x in res for eps in (0, 1) if x[eps]['B'] == 0]
print("classes with B = 0:", len(zeroB))
print("   B = 0  <=>  traceless minimisers on that class:",
      all((x[eps]['B'] == 0) == x[eps]['tl'] for x in res for eps in (0, 1)))
# B * 16 P a perfect square?
sq = Counter()
for x in res:
    P = x['key'][0] * x['key'][1]
    for eps in (0, 1):
        v = x[eps]['B'] * 16 * P
        ok = v.denominator == 1 and isqrt(v.numerator) ** 2 == v.numerator
        v4 = x[eps]['B'] * 64 * P
        ok4 = v4.denominator == 1 and isqrt(v4.numerator) ** 2 == v4.numerator
        sq[(ok, ok4)] += 1
print("(16PB is a square integer, 64PB is a square integer) ->", dict(sq))
json.dump([dict(key=x['key'], torus=x['torus'],
                **{('A%d' % e): str(x[e]['A']) for e in (0, 1)}, **{('B%d' % e): str(x[e]['B']) for e in (0, 1)},
                **{('j0_%d' % e): x[e]['j0'] for e in (0, 1)}) for x in res],
          open(sys.argv[1].replace('.json', '_closed.json'), 'w'), indent=0)
for key in [(2, 3, 1), (2, 3, 5), (3, 5, 2), (3, 5, 14), (3, 5, 7), (2, 5, 7), (3, 4, 5), (7, 17, 2), (3, 7, 2)]:
    for x in res:
        if x['key'] == key:
            P = key[0] * key[1]
            print("  chain %-12s A0=%-12s B0=%-10s (16PB0=%s, j0=%d)  A1=%-12s B1=%-10s (16PB1=%s, j0=%d)" % (
                key, x[0]['A'], x[0]['B'], x[0]['B'] * 16 * P, x[0]['j0'], x[1]['A'], x[1]['B'], x[1]['B'] * 16 * P, x[1]['j0']))
