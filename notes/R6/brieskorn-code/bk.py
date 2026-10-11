"""
Core library: DLME levels c = (3+rho)/16 of the irreducible flat SU(2) connections on
+-Sigma(a1,a2,a3), ell = min c, and the 1/m surgeries on an exceptional fibre.

TOPOLOGY (derived in brieskorn.md, section 1; verified by Casson in validate.py)
  Sigma = Sigma(a1,a2,a3), link orientation.  K_i = exceptional fibre of order a_i,
  P_i = a/a_i (a = a1 a2 a3).  With respect to the Seifert framing of K_i,
      Sigma_{1/m}(K_i) = sgn(a_i - m P_i) * Sigma(.., |a_i - m P_i|, ..)    (i-th slot replaced)
  and for the reversed orientation (-Sigma)_{1/m}(K_i) = -( Sigma_{-1/m}(K_i) ).
  Unified, for base  s*Sigma  (s = +-1):
      (s Sigma)_{1/m}(K_i) = s*sgn(a_i - s m P_i) * Sigma(.., |a_i - s m P_i|, ..).
  Calibration: Sigma(2,3,1) = S^3, K_3 = regular fibre = right-handed trefoil:
      S^3_{-1/n}(RHT) = Sigma(2,3,6n+1),  S^3_{1/n}(RHT) = -Sigma(2,3,6n-1).

LEVELS.  Fintushel-Stern presentation <x_i,h | h central, x_i^{a_i} h^{b_i}, x1x2x3>,
  sum b_i a/a_i = 1.  Irreducibles (eps,l1,l2,l3): 0<l_i<a_i, (-1)^{l_i} = eps^{b_i},
  strict spherical triangle inequality on t_i = l_i/a_i.
  c = (1/4) sum_i T(a_i, -b_i, l_i),  T(m,b,l) = (1/m) sum_k cot(pi k/m)cot(pi k b/m) sin^2(pi k l/m)
    = N(m,b,l)/(2 m^2),  N(m,b,l) = sum_j s(j) [s(bj) - s(bj+l)],  s(x) = 2(x mod m) - m (0 if m|x).
  This is check-code/fs.py's c_APS (APS rho on the orbifold mapping cylinder), in integer form.
  On -Sigma: c -> 3/8 - c, CS -> -CS, gr -> -3-gr.
  c * 8a is an integer (c = CS - gr/8 mod 1, CS = e^2/(4a)), used to make float search exact.

INDEPENDENT CHECK (per minimiser): Fintushel-Stern integer e (e b_i = +-l_i mod 2a_i),
  CS = e^2/(4a), c_FS = -SigmaFS(e)/8 with SigmaFS(e) = sum_i 2 T(a_i, a/a_i, e)
  [a different Dedekind-type sum: different b and different l], and 8(CS - c) in Z.
"""
from fractions import Fraction as F
from math import gcd
from functools import lru_cache
from itertools import product
import numpy as np


# ---------------------------------------------------------------- arithmetic
def egcd(x, y):
    if y == 0:
        return (x, 1, 0)
    g, u, v = egcd(y, x % y)
    return (g, v, u - (x // y) * v)


def presentation(A):
    a = A[0] * A[1] * A[2]
    q = [a // ai for ai in A]
    g12, u, v = egcd(q[0], q[1])
    g, s, t = egcd(g12, q[2])
    assert g == 1
    b = (s * u, s * v, t)
    assert sum(bi * qi for bi, qi in zip(b, q)) == 1
    return b


@lru_cache(maxsize=None)
def Nvec(m, b):
    """numpy int64 array N[l], l = 0..m-1, with T(m,b,l) = N[l]/(2 m^2) (exact).
    Cyclic correlation by O(m^2) integer sums for m <= 3000, by FFT (rounded, then spot-checked
    exactly at 12 random shifts and required to round cleanly) for larger m."""
    if m == 1:
        return np.zeros(1, dtype=np.int64)
    b %= m
    j = np.arange(m, dtype=np.int64)
    s = np.where(j == 0, 0, 2 * j - m).astype(np.int64)
    w = np.zeros(m, dtype=np.int64)
    w[(b * j) % m] = s                    # w[b j] = s[j]
    # S(t) = sum_k w[k] s[(k+t) mod m]  (cyclic correlation), N[l] = S(0) - S(l)
    if m <= 3000:
        S = np.empty(m, dtype=np.int64)
        ss = np.concatenate([s, s])
        CH = max(1, 4_000_000 // m)
        for t0 in range(0, m, CH):
            t1 = min(m, t0 + CH)
            idx = (np.arange(t0, t1)[:, None] + j[None, :])
            S[t0:t1] = (ss[idx] * w[None, :]).sum(axis=1)
    else:
        assert m <= 60000
        fw = np.fft.rfft(w.astype(np.float64))
        fs_ = np.fft.rfft(s.astype(np.float64))
        Sf = np.fft.irfft(np.conj(fw) * fs_, n=m)
        S = np.rint(Sf).astype(np.int64)
        assert np.max(np.abs(Sf - S)) < 0.2, ("FFT rounding", m, np.max(np.abs(Sf - S)))
        rng = np.random.default_rng(m * 7919 + b)
        for t in list(rng.integers(0, m, 12)) + [0]:
            t = int(t)
            exact = int(np.dot(w, np.roll(s, -t)))
            assert exact == int(S[t]), ("FFT spot check", m, b, t)
    assert abs(int(S[0])) < 2 ** 62 // 4
    return S[0] - S


def T_exact(m, b, l):
    """Exact T(m,b,l) by direct sawtooth sum (pure Python ints; for checks)."""
    def s2(x):
        r = x % m
        return 0 if r == 0 else 2 * r - m
    tot = sum(s2(j) * (s2(b * j) - s2(b * j + l)) for j in range(1, m))
    return F(tot, 2 * m * m)


# ---------------------------------------------------------------- flat connections
def triangle_bounds(A, l1, l2):
    """Integer range [lo, hi] of l3 satisfying the strict triangle inequality."""
    a1, a2, a3 = A
    P = a1 * a2
    x, y = l1 * a2, l2 * a1                    # t1 = x/P, t2 = y/P
    lo = (a3 * abs(x - y)) // P + 1            # l3/a3 > |t1 - t2|
    up = min(x + y, 2 * P - x - y)             # l3/a3 < min(t1+t2, 2-t1-t2)
    hi = (a3 * up - 1) // P
    return lo, hi


def analyse(A0, want_all=False):
    """Brieskorn sphere Sigma(A0), link orientation, A0 pairwise coprime (entries may be 1).
    Returns dict: count, cmin, cmax (Fractions), argmin/argmax lists of (eps, l) in the
    ORIGINAL order of A0, and (if want_all) the full list of (eps, l, c)."""
    A0 = tuple(A0)
    a = A0[0] * A0[1] * A0[2]
    assert gcd(A0[0], A0[1]) == gcd(A0[0], A0[2]) == gcd(A0[1], A0[2]) == 1
    order = sorted(range(3), key=lambda i: A0[i])           # largest fibre last
    A = tuple(A0[i] for i in order)
    if A[0] == 1 or A[1] == 1:                               # lens space / S^3: no irreducibles
        return dict(A=A0, count=0, cmin=None, cmax=None, argmin=[], argmax=[], all=[])
    b = presentation(A)
    D = 8 * a
    # term_i[l] = 8a * T_i(l)/4 = 2a N/(2 a_i^2) = a N / a_i^2 ; exact rational -> keep float + exact check
    terms = []
    for i in range(3):
        m = A[i]
        Nv = Nvec(m, (-b[i]) % m)
        terms.append(Nv.astype(np.float64) * (a / (m * m)))  # = 8a * c-contribution
    out = dict(A=A0, count=0, cmin=None, cmax=None, argmin=[], argmax=[], all=[])
    best = [np.inf, -np.inf]
    cand = {0: [], 1: []}
    allreps = []
    for eps in (1, -1):
        par = [None] * 3
        for i in range(3):
            par[i] = 0 if (eps == 1 or b[i] % 2 == 0) else 1      # required parity of l_i
        L1 = [l for l in range(1, A[0]) if l % 2 == par[0]]
        L2 = [l for l in range(1, A[1]) if l % 2 == par[1]]
        t3 = terms[2]
        p3 = par[2]
        sub = t3[p3::2]                           # sub[k] = t3[p3 + 2k]
        for l1 in L1:
            for l2 in L2:
                lo, hi = triangle_bounds(A, l1, l2)
                # restrict to parity p3
                if lo % 2 != p3:
                    lo += 1
                if hi % 2 != p3:
                    hi -= 1
                if hi < lo:
                    continue
                k0, k1 = (lo - p3) // 2, (hi - p3) // 2
                out['count'] += k1 - k0 + 1
                base = terms[0][l1] + terms[1][l2]
                seg = sub[k0:k1 + 1]
                mn, mx = base + seg.min(), base + seg.max()
                if mn < best[0] + 0.5:
                    if mn < best[0] - 0.5:
                        cand[0] = []
                    best[0] = min(best[0], mn)
                    for k in np.nonzero(base + seg < best[0] + 0.5)[0]:
                        cand[0].append((eps, (l1, l2, p3 + 2 * (k0 + int(k)))))
                if mx > best[1] - 0.5:
                    if mx > best[1] + 0.5:
                        cand[1] = []
                    best[1] = max(best[1], mx)
                    for k in np.nonzero(base + seg > best[1] - 0.5)[0]:
                        cand[1].append((eps, (l1, l2, p3 + 2 * (k0 + int(k)))))
                if want_all:
                    for k in range(k0, k1 + 1):
                        allreps.append((eps, (l1, l2, p3 + 2 * k)))
    inv = [order.index(i) for i in range(3)]               # position of original fibre i in A

    def exact_c(l):
        return sum(F(int(Nvec(A[i], (-b[i]) % A[i])[l[i]]), 8 * A[i] * A[i]) for i in range(3))

    def to_orig(l):
        return tuple(l[inv[i]] for i in range(3))

    for side, key in ((0, 'min'), (1, 'max')):
        cs = [(exact_c(l), eps, l) for eps, l in cand[side]]
        cs = [x for x in cs if (x[0] * D).denominator == 1]
        assert len(cs) == len(cand[side]), "8a*c not integral"
        ext = min(x[0] for x in cs) if side == 0 else max(x[0] for x in cs)
        assert abs(float(ext) * D - (best[side])) < 1e-3
        out['c' + key] = ext
        out['arg' + key] = [(eps, to_orig(l)) for c, eps, l in cs if c == ext]
    if want_all:
        out['all'] = [(eps, to_orig(l), exact_c(l)) for eps, l in allreps]
    out['b_sorted'] = b
    out['A_sorted'] = A
    return out


# ---------------------------------------------------------------- FS cross-check
def crt_pair(r1, m1, r2, m2):
    g = gcd(m1, m2)
    if (r2 - r1) % g:
        return None
    l = m1 // g * m2
    t = ((r2 - r1) // g * pow(m1 // g, -1, m2 // g)) % (m2 // g) if m2 // g > 1 else 0
    return ((r1 + m1 * t) % l, l)


def fs_e(A, l):
    """FS integer e with e*b_i = +-l_i mod 2a_i (b from presentation(A), A in any order)."""
    b = presentation(A)
    for signs in product((1, -1), repeat=3):
        r, m = 0, 1
        ok = True
        for ai, bi, li, s in zip(A, b, l, signs):
            sols = [x for x in range(2 * ai) if (x * bi - s * li) % (2 * ai) == 0]
            if not sols:
                ok = False
                break
            step = (sols[1] - sols[0]) if len(sols) > 1 else 2 * ai
            res = crt_pair(r, m, sols[0], step)
            if res is None:
                ok = False
                break
            r, m = res
        if ok:
            return r
    raise ValueError((A, l))


def fs_check(A, l, c):
    """Independent FS evaluation for the rep with rotation numbers l (original order of A).
    Returns (e, CS, gr) on the link orientation; asserts c == -SigmaFS(e)/8 and integrality."""
    a = A[0] * A[1] * A[2]
    order = sorted(range(3), key=lambda i: A[i])          # labels l refer to presentation(sorted A)
    e = fs_e(tuple(A[i] for i in order), tuple(l[i] for i in order))
    CS = F(e * e, 4 * a) % 1
    SFS = sum(2 * T_exact(ai, (a // ai) % ai, e % ai) for ai in A)
    assert -SFS / 8 == c, ("FS level mismatch", A, l, c, -SFS / 8)
    g = F(2 * e * e, a) + SFS
    assert g.denominator == 1, ("non-integral FS grading", A, l)
    gr = int(g) % 8
    assert (8 * (CS - c)).denominator == 1 and (int(8 * (CS - c)) - gr) % 8 == 0
    return e, CS, gr


# ---------------------------------------------------------------- Casson / signature
def milnor_count(A):
    """#R*(Sigma(A)) from Brieskorn's signature formula: lambda = sigma/8 = -#R*/2,
    #R* = (#{1<s<2} - #{0<s<1} - #{2<s<3})/4, s = sum j_i/a_i, 0<j_i<a_i."""
    a1, a2, a3 = sorted(A)
    if a1 == 1:
        return 0
    cnt = [0, 0, 0]
    for j1 in range(1, a1):
        for j2 in range(1, a2):
            x = F(j1, a1) + F(j2, a2)               # need j3/a3 in (k - x, k+1 - x)
            for k in range(3):
                lo, hi = k - x, k + 1 - x
                # j3 in (lo*a3, hi*a3) intersect [1, a3-1]
                jl = max(1, int((lo * a3).__floor__()) + 1)
                jh = min(a3 - 1, int((hi * a3).__ceil__()) - 1)
                if jh >= jl:
                    cnt[k] += jh - jl + 1
    s = cnt[1] - cnt[0] - cnt[2]
    assert s % 4 == 0 and s >= 0
    return s // 4


# ---------------------------------------------------------------- surgery
def surgered(A, s, i, m):
    """(s*Sigma(A))_{1/m}(K_i) = (A', s') meaning s' * Sigma(A')."""
    a = A[0] * A[1] * A[2]
    P = a // A[i]
    x = A[i] - s * m * P
    assert x != 0
    Ap = list(A)
    Ap[i] = abs(x)
    return tuple(Ap), s * (1 if x > 0 else -1)


def a2_fibre(A, i):
    """Delta''(1)/2 for the fibre K_i: Alexander polynomial of T(a_j, a_k)."""
    aj, ak = [A[j] for j in range(3) if j != i]
    return F((aj * aj - 1) * (ak * ak - 1), 24)


_cache = {}


def manifold(A, s):
    """ell and minimiser data of s*Sigma(A)."""
    key = tuple(sorted(A))
    if key not in _cache:
        _cache[key] = analyse(key)
    d = _cache[key]
    # map sorted-order data back to the order of A
    perm = [key.index(x) for x in A] if len(set(A)) == 3 else None
    if perm is None:                        # repeated entries only possible with 1s
        perm = list(range(3))
        used = set()
        for j, x in enumerate(A):
            for k, y in enumerate(key):
                if y == x and k not in used:
                    perm[j] = k
                    used.add(k)
                    break

    def reorder(lst):
        return [(eps, tuple(l[perm[j]] for j in range(3))) for eps, l in lst]
    if d['count'] == 0:
        return dict(A=A, s=s, count=0, ell=None, argmin=[], lam=F(0))
    if s == 1:
        ell, arg = d['cmin'], reorder(d['argmin'])
    else:
        ell, arg = F(3, 8) - d['cmax'], reorder(d['argmax'])
    return dict(A=tuple(A), s=s, count=d['count'], ell=ell, argmin=arg,
                lam=F(-s * d['count'], 2))
