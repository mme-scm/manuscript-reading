"""Scan: for every pairwise-coprime Sigma(a1,a2,a3) (2<=a1<a2<a3, a<=AMAX), both orientations
s = +-1, and each exceptional fibre K_i, compute ell of
    s*Sigma,  Y_{-1/n} (n=1..NNEG),  Y_{+1/n} (n=1..NPOS)
with minimiser data, and check on EVERY manifold:
  * Casson surgery formula  lambda(Y_{1/m}) = lambda(s Sigma) + m a2(T(a_j,a_k))
    with lambda(s' Sigma(A')) = -s' #R*(A')/2;
  * #R*(A') from the separable count == Brieskorn signature count (bk.milnor_count);
  * for each minimiser: FS e, CS, gr, c == -SigmaFS(e)/8, 8(CS-c) in Z (bk.fs_check).
Usage: python3 scan.py AMAX OUTFILE [torus]   ("torus" = only the torus-knot-surgery triples,
       plus the S^3 = Sigma(p,q,1) regular-fibre families)
"""
import sys, json, time
from fractions import Fraction as F
from math import gcd
sys.path.insert(0, '/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/r6/brieskorn-code')
import bk

NNEG, NPOS = 6, 3


def is_torus(A):
    a = A[0] * A[1] * A[2]
    for i in range(3):
        P = a // A[i]
        if A[i] % P in (1 % P, (P - 1) % P):
            return True
    return False


def triples(AMAX):
    out = []
    for a1 in range(2, 40):
        for a2 in range(a1 + 1, AMAX // (2 * a1) + 2):
            if gcd(a1, a2) != 1:
                continue
            for a3 in range(a2 + 1, AMAX // (a1 * a2) + 1):
                if gcd(a1, a3) == 1 and gcd(a2, a3) == 1:
                    out.append((a1, a2, a3))
    return out


_mc = {}


def mcount(A):
    k = tuple(sorted(A))
    if k not in _mc:
        _mc[k] = bk.milnor_count(k)
    return _mc[k]


_fsc = {}


def info(A, s, i):
    """Manifold s*Sigma(A) with surgered fibre index i (or None)."""
    d = bk.manifold(A, s)
    if d['count'] > 0 and min(A) > 1:
        assert d['count'] == mcount(A), ("signature count", A)
    mins = []
    for eps, l in d['argmin']:
        key = (tuple(A), l)
        if key not in _fsc:
            # c on the link orientation for this rep
            c_link = d['ell'] if s == 1 else F(3, 8) - d['ell']
            _fsc[key] = bk.fs_check(tuple(A), l, c_link)
        e, CS, gr = _fsc[key]
        if s == -1:
            CS, gr = (-CS) % 1, (-3 - gr) % 8
        rec = dict(eps=eps, l=list(l), e=e, CS=str(CS), gr=gr)
        if i is not None:
            rec['l_K'] = l[i]
            rec['a_K'] = A[i]
            rec['traceless'] = (2 * l[i] == A[i])
        mins.append(rec)
    return dict(A=list(A), s=s, count=d['count'], lam=str(d['lam']),
                ell=None if d['ell'] is None else str(d['ell']), min=mins)


def family(A, s, i):
    a2K = bk.a2_fibre(A, i)
    base = info(A, s, i)
    lam0 = F(base['lam'])
    res = dict(A=list(A), s=s, i=i, aK=A[i], a2K=str(a2K), base=base, neg={}, pos={})
    for sg, NN, key in ((-1, NNEG, 'neg'), (1, NPOS, 'pos')):
        for n in range(1, NN + 1):
            Ap, sp = bk.surgered(A, s, i, sg * n)
            y = info(Ap, sp, i)
            assert F(y['lam']) == lam0 + sg * n * a2K, ("Casson", A, s, i, sg * n, y['lam'], lam0, a2K)
            res[key][n] = y
    return res


if __name__ == "__main__":
    AMAX = int(sys.argv[1])
    outf = sys.argv[2]
    torus_mode = len(sys.argv) > 3 and sys.argv[3] == 'torus'
    t0 = time.time()
    T = [A for A in triples(AMAX) if is_torus(A) == torus_mode]
    if torus_mode:
        # regular fibre of S^3 = Sigma(p,q,1): torus knots, for comparison
        T = [(p, q, 1) for p in range(2, 12) for q in range(p + 1, 40) if gcd(p, q) == 1 and p * q <= 160] + T
    print("triples:", len(T), file=sys.stderr)
    fams = []
    for k, A in enumerate(T):
        for s in (1, -1):
            for i in range(3):
                if A[i] == 1 and False:
                    continue
                if A[i] != 1 and min(A) == 1:
                    continue                    # only the regular fibre of S^3
                fams.append(family(A, s, i))
        if k % 25 == 0:
            print(k, A, "%.1fs" % (time.time() - t0), file=sys.stderr)
    json.dump(fams, open(outf, 'w'))
    print("families: %d, all Casson/signature/FS checks passed, %.1fs" % (len(fams), time.time() - t0))
