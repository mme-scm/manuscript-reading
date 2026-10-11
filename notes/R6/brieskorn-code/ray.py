"""Chains of 1/m fillings of one fibre exterior.
Exterior X = X(a1,a2;r): Seifert over D^2(a1,a2), P = a1 a2, 0<r<P, gcd(r,P)=1 (r = a_K mod P).
Its integer-homology-sphere fillings, indexed by k in Z (-1/n surgery moves k -> k+n):
    Z_k = +Sigma(a1,a2, r+kP)      k >= 0   (link orientation; Z_0 = S^3 iff r = 1)
    Z_k = -Sigma(a1,a2, |r+kP|)    k <= -1  (Z_{-1} = -S^3 iff r = P-1)
The mirror exterior is X(a1,a2;P-r), with Z'_k = -Z_{-1-k}.
Every family (s*Sigma, K) of scan.py is a window of such a chain: base Z_k, Y_{-1/n} = Z_{k+n}.
Usage: python3 ray.py PMAX KMIN KMAX OUT.json
"""
import sys, json, time
from math import gcd
from fractions import Fraction as F
sys.path.insert(0, '/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/r6/brieskorn-code')
import bk


def chain_member(a1, a2, r, k):
    P = a1 * a2
    x = r + k * P
    return (a1, a2, abs(x)), (1 if x > 0 else -1)


def member_info(A, s):
    d = bk.manifold(A, s)
    if d['ell'] is None:
        return dict(A=list(A), s=s, ell=None, count=0, min=[])
    mins = []
    for eps, l in d['argmin']:
        c_link = d['ell'] if s == 1 else F(3, 8) - d['ell']
        e, CS, gr = bk.fs_check(A, l, c_link)
        if s == -1:
            CS, gr = (-CS) % 1, (-3 - gr) % 8
        mins.append(dict(eps=eps, l=list(l), e=e, CS=str(CS), gr=gr, traceless=(2 * l[2] == A[2])))
    return dict(A=list(A), s=s, ell=str(d['ell']), count=d['count'], min=mins)


if __name__ == "__main__":
    PMAX, KMIN, KMAX, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    t0 = time.time()
    chains = []
    for a1 in range(2, PMAX):
        for a2 in range(a1 + 1, PMAX // a1 + 1):
            if gcd(a1, a2) != 1:
                continue
            P = a1 * a2
            for r in range(1, P):
                if gcd(r, P) != 1:
                    continue
                ch = dict(a1=a1, a2=a2, r=r, P=P, torus=(r in (1, P - 1)), Z={})
                for k in range(KMIN, KMAX + 1):
                    A, s = chain_member(a1, a2, r, k)
                    ch['Z'][k] = member_info(A, s)
                chains.append(ch)
    json.dump(chains, open(out, 'w'))
    print("chains: %d, members %d..%d, %.1fs" % (len(chains), KMIN, KMAX, time.time() - t0))
