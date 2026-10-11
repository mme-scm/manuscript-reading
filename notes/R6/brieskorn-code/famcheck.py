"""Checks on family scans (scan.py output), for large P.
 1. Link-oriented windows (Y_{-1/n}, Y_{-1/(n+2)} both +Sigma): T_n - 1/8 = beta^2/(8 m_n m_{n+2}), beta integer >= 0;
    beta = 0 iff traceless minimisers at both ends.  (n = 1..4)
 2. Closed form: with beta_n from step 1, D_n = 1/16 + (beta_n^2/m_n - beta_{n+1}^2/m_{n+1})/(16P) (n = 1..3).
 3. Odd P: beta_n + beta_{n+1} = P ?
 4. Window rule: T_1 >= 1/8 whenever Y_{-1/3} is link-oriented; (a) fails only if the window contains the
    step Z_{-2} -> Z_{-1} (two reversed members followed by... see below).
 5. Context: ell(Y_{1/n}) - ell(Y_{-1/n}) (n=1,2,3) vs 1/8 ; position of ell(Sigma).
Usage: python3 famcheck.py FILE.json [...]"""
import sys, json
from fractions import Fraction as F
from math import isqrt
from collections import Counter

fams = []
for fn in sys.argv[1:]:
    fams += json.load(open(fn))
E = lambda y: None if y['ell'] is None else F(y['ell'])
EI = F(1, 8)
c1 = Counter(); c2 = Counter(); c3 = Counter(); c4 = Counter(); c5 = Counter()
worst5 = {}
minD = {}
Pmax = 0
for f in fams:
    i = f['i']; A = f['A']; P = A[0] * A[1] * A[2] // A[i]
    ng = {int(k): v for k, v in f['neg'].items()}
    ps = {int(k): v for k, v in f['pos'].items()}
    if any(E(v) is None for v in ng.values()):
        continue
    Pmax = max(Pmax, P)
    link = {n: ng[n]['s'] == 1 for n in ng}
    m = {n: ng[n]['A'][i] for n in ng}
    beta = {}
    for n in range(1, 5):
        if link[n] and link[n + 2]:
            x = (E(ng[n]) - E(ng[n + 2]) - EI) * 8 * m[n] * m[n + 2]
            ok = x >= 0 and x.denominator == 1 and isqrt(x.numerator) ** 2 == x.numerator
            c1[('square', ok)] += 1
            if ok:
                beta[n] = isqrt(x.numerator)
                tl = any(mm['traceless'] for mm in ng[n]['min']) and any(mm['traceless'] for mm in ng[n + 2]['min'])
                c1[('beta=0 <=> traceless', (beta[n] == 0) == tl)] += 1
    for n in range(1, 4):
        if n in beta and n + 1 in beta:
            D = E(ng[n]) - E(ng[n + 1])
            pred = F(1, 16) + (F(beta[n] ** 2, m[n]) - F(beta[n + 1] ** 2, m[n + 1])) / (16 * P)
            c2[D == pred] += 1
            if P % 2:
                c3[beta[n] + beta[n + 1] == P] += 1
            # one-step drop minima per kind
            kind = 'L+' if f['s'] == 1 else ('L-' if A[i] < P else 'R-')
            if n == 1 or n == 2:
                key = (kind, n)
                if key not in minD or D < minD[key][0]:
                    minD[key] = (D, f['s'], tuple(A), A[i])
    # window rule
    ori = "".join('+' if link[n] else '-' for n in (1, 2, 3))
    T1 = E(ng[1]) - E(ng[3])
    a_ok = E(ng[1]) > E(ng[2]) > E(ng[3])
    c4[(ori, 'T1>=1/8' if T1 >= EI else 'T1<1/8', 'a ok' if a_ok else 'a FAILS')] += 1
    # context: Y_{+1/n} - Y_{-1/n}
    for n in (1, 2, 3):
        if E(ps[n]) is None:
            continue
        d = E(ps[n]) - E(ng[n])
        kind = 'L+' if f['s'] == 1 else ('L-' if A[i] < P else 'R-')
        c5[(kind, n, '>1/8' if d > EI else ('=1/8' if d == EI else '<1/8'))] += 1
        k = (kind, n)
        if k not in worst5 or d < worst5[k][0]:
            worst5[k] = (d, f['s'], tuple(A), A[i])
print("families:", len(fams), " max P among them:", Pmax)
print("1.", dict(c1))
print("2. D_n == closed-form prediction:", dict(c2))
print("3. odd P: beta_n + beta_{n+1} == P:", dict(c3))
print("4. window (orientations of Y-1,Y-1/2,Y-1/3; T1; (a)) -> count")
for k, v in sorted(c4.items()):
    print("    ", k, v)
print("   one-step drop minima (kind, n): value, base")
for k in sorted(minD):
    D, s, A, aK = minD[k]
    print("    ", k, D, "≈ %.5f" % float(D), "%sS%s K=%d" % ('+' if s == 1 else '-', A, aK))
print("5. ell(Y_{1/n}) - ell(Y_{-1/n}) vs 1/8 (kind, n, cmp) -> count")
for k, v in sorted(c5.items()):
    print("    ", k, v)
for k in sorted(worst5):
    d, s, A, aK = worst5[k]
    print("     min", k, d, "≈ %.5f" % float(d), "%sS%s K=%d" % ('+' if s == 1 else '-', A, aK))
