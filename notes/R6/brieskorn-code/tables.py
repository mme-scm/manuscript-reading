"""Per-example tables from scan JSON files.
Usage: python3 tables.py OUT.md FILE.json [FILE.json ...]
For each base s*Sigma(A) in EXAMPLES and each fibre K: ell(s Sigma), ell(Y_{-1/n}) n=1..4,
ell(Y_{+1/n}) n=1..3, D1, D2, T1, beta of the classes, traceless flags of the minimisers."""
import sys, json
from fractions import Fraction as F
from math import isqrt

EX_NT = [(2, 5, 7), (3, 4, 5), (2, 5, 13), (3, 5, 7), (2, 7, 9), (3, 4, 7), (2, 5, 17), (4, 5, 7)]
EX_T = [(2, 3, 5), (2, 3, 7), (2, 3, 11), (2, 3, 13), (2, 5, 9), (2, 5, 11), (3, 4, 11), (3, 4, 13),
        (2, 3, 1), (3, 5, 1), (2, 5, 1)]
out = open(sys.argv[1], 'w')
fams = {}
for fn in sys.argv[2:]:
    for f in json.load(open(fn)):
        fams[(tuple(f['A']), f['s'], f['i'])] = f


def fmt(x):
    return "∞" if x is None else str(x)


def E(y):
    return None if y['ell'] is None else F(y['ell'])


def orient(y):
    return ('+' if y['s'] == 1 else '−') + "Σ(%s)" % ",".join(map(str, y['A']))


def tlf(y):
    return "".join('T' if m.get('traceless') else '·' for m in y['min'])


def beta(f, n):
    """beta from the closed form, using Y_{-1/n} and Y_{-1/(n+2)} (same parity class), when link-oriented."""
    y1, y3 = f['neg'][str(n)], f['neg'][str(n + 2)]
    if y1['s'] != 1 or y3['s'] != 1 or y1['ell'] is None or y3['ell'] is None:
        return None
    m1, m3 = y1['A'][f['i']], y3['A'][f['i']]
    x = (E(y1) - E(y3) - F(1, 8)) * 8 * m1 * m3
    if x.denominator == 1 and x >= 0 and isqrt(x.numerator) ** 2 == x.numerator:
        return isqrt(x.numerator)
    return "?"


for title, EX in (("Non-torus-knot bases", EX_NT), ("Torus-knot bases (and S^3 = Σ(p,q,1) with K = regular fibre = T(p,q))", EX_T)):
    out.write("\n## %s\n\n" % title)
    out.write("| base, K (order) | P | ℓ(base) | ℓ(Y−1) | ℓ(Y−1/2) | ℓ(Y−1/3) | ℓ(Y−1/4) | ℓ(Y+1) | ℓ(Y+1/2) | ℓ(Y+1/3) | D1 | D2 | T1 | β(n=1), β(n=2) | TL n=1,2,3 | orient. Y−1..Y−1/3 |\n")
    out.write("|" + "---|" * 16 + "\n")
    for A in EX:
        for s in (1, -1):
            for i in range(3):
                key = (A, s, i)
                if key not in fams:
                    continue
                f = fams[key]
                P = A[0] * A[1] * A[2] // A[i]
                ng = {int(k): E(v) for k, v in f['neg'].items()}
                ps = {int(k): E(v) for k, v in f['pos'].items()}
                ok = all(ng[n] is not None for n in (1, 2, 3))
                D1 = ng[1] - ng[2] if ok else None
                D2 = ng[2] - ng[3] if ok else None
                T1 = ng[1] - ng[3] if ok else None
                b = (beta(f, 1), beta(f, 2))
                out.write("| %sΣ(%s), K=%d | %d | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n" % (
                    '+' if s == 1 else '−', ",".join(map(str, A)), A[i], P, fmt(E(f['base'])),
                    fmt(ng[1]), fmt(ng[2]), fmt(ng[3]), fmt(ng[4]), fmt(ps[1]), fmt(ps[2]), fmt(ps[3]),
                    fmt(D1) if D1 is None else "%s ≈ %.4f" % (D1, float(D1)),
                    fmt(D2) if D2 is None else "%s ≈ %.4f" % (D2, float(D2)),
                    fmt(T1) if T1 is None else ("**1/8**" if T1 == F(1, 8) else "%s ≈ %.4f" % (T1, float(T1))),
                    "%s, %s" % b, "%s %s %s" % (tlf(f['neg']['1']), tlf(f['neg']['2']), tlf(f['neg']['3'])),
                    " ".join(orient(f['neg'][str(n)]) for n in (1, 2, 3))))
out.close()
print("written", sys.argv[1])
