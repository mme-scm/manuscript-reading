"""Generator-level test.  For link-oriented chain members Z_j = Sigma(a1,a2,m_j), m_j = r+jP:
is there an injection phi: gens(Z_j) -> gens(Z_{j+2}) with
     c(alpha) - c(phi alpha) = 1/8 + beta^2/(8 m_j m_{j+2}),  beta in Z_{>=0}  ?
(This would give T(j) >= 1/8 generator by generator, with equality iff beta(minimiser) = 0.)
Also records whether phi can be chosen to preserve (l1,l2) and to shift gr by +2 mod 8.
Usage: python3 matching.py"""
import sys
from fractions import Fraction as F
from math import isqrt, gcd
sys.path.insert(0, '/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/r6/brieskorn-code')
import bk


def gens(A):
    d = bk.analyse(A, want_all=True)
    out = []
    for eps, l, c in d['all']:
        e, CS, gr = bk.fs_check(A, l, c)
        out.append(dict(l=l, c=c, gr=gr, tl=(2 * l[2] == A[2])))
    return out


def max_matching(adj, nL, nR):
    match_r = [-1] * nR

    def try_(u, seen):
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                if match_r[v] == -1 or try_(match_r[v], seen):
                    match_r[v] = u
                    return True
        return False
    sys.setrecursionlimit(100000)
    return sum(try_(u, set()) for u in range(nL))


def test(a1, a2, r, j):
    P = a1 * a2
    m0, m2 = r + j * P, r + (j + 2) * P
    G0, G2 = gens((a1, a2, m0)), gens((a1, a2, m2))
    adj, adj_l, adj_gr = [], [], []
    betas = []
    for g in G0:
        row, rowl, rowg = [], [], []
        for k, h in enumerate(G2):
            x = (g['c'] - h['c'] - F(1, 8)) * 8 * m0 * m2
            if x >= 0 and x.denominator == 1 and isqrt(x.numerator) ** 2 == x.numerator:
                row.append(k)
                if h['l'][:2] == g['l'][:2]:
                    rowl.append(k)
                if (h['gr'] - g['gr']) % 8 == 2:
                    rowg.append(k)
        adj.append(row); adj_l.append(rowl); adj_gr.append(rowg)
    full = max_matching(adj, len(G0), len(G2))
    full_l = max_matching(adj_l, len(G0), len(G2))
    full_g = max_matching(adj_gr, len(G0), len(G2))
    return len(G0), len(G2), full, full_l, full_g


if __name__ == "__main__":
    cases = [(2, 3, 1), (2, 3, 5), (2, 5, 3), (2, 5, 7), (3, 4, 5), (3, 4, 7), (3, 5, 2), (3, 5, 7), (3, 5, 4),
             (3, 5, 8), (2, 7, 9), (3, 7, 2), (3, 7, 8), (4, 5, 3), (5, 7, 2), (5, 7, 9), (3, 8, 5), (2, 9, 11),
             (5, 6, 7), (3, 10, 7)]
    allok = True
    for (a1, a2, r) in cases:
        for j in (0, 1, 2):
            if r + j * a1 * a2 == 1:
                continue
            n0, n2, f, fl, fg = test(a1, a2, r, j)
            ok = (f == n0)
            allok &= ok
            print("chain (%d,%d,%d) j=%d: #Z_j=%d #Z_j+2=%d  matched %d (with same (l1,l2): %d; with gr+2: %d) %s"
                  % (a1, a2, r, j, n0, n2, f, fl, fg, "OK" if ok else "NO INJECTION"))
    print("all injective:", allok)
