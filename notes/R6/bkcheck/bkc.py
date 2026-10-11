"""Independent level computation for Brieskorn spheres Sigma(a1,a2,a3).

Written from scratch (no code shared with earlier directories).

Method M1 (exact): orbifold APS / G-signature on the disk orbibundle W -> S^2(a1,a2,a3),
  W negative definite for the link orientation, sign(W) = -1, twisted signature 0.
  rho(ad alpha) = -3 + sum_i (4/a_i) sum_k sin^2(pi l_i k/a_i) cot(pi k/a_i) cot(pi nu_i k/a_i),
  nu_i = S * b_i (mod a_i), S = +-1 fixed by calibration.
  Each cone sum is evaluated exactly by the identity
  sum_{k mod a} cot(pi k/a) cot(pi nu k/a) e^{2 pi i l k/a} = 4a sum_m ((m/a)) (((nu m + l)/a)).
  c = (3+rho)/16 = sum_i F_i(l_i) / (8 a_i^2),  F_i(l) = sum_x X(x)[X(nu x) - X(nu x + l)],
  X(x) = 2a((x/a)) in Z.

Method M2 (float, different parametrisation): Fintushel-Stern style cot sum
  c = S/4 * sum_i (1/a_i) sum_k cot(pi a k/a_i^2) cot(pi k/a_i) sin^2(pi e k/a_i),
  e from CRT, e = l_i (a/a_i) mod a_i, direct float cot products.
"""
import numpy as np
from fractions import Fraction
from math import gcd, prod

SIGN = -1  # calibrated: Sigma(2,3,5) -> -7/60,-13/60; Sigma(2,3,7) -> 23/84, 29/84


def bvec(A):
    a = prod(A)
    b = [pow(a // ai, -1, ai) for ai in A]
    s = sum(bi * (a // ai) for bi, ai in zip(b, A))
    t = (s - 1) // a
    assert (s - 1) % a == 0
    b[0] -= t * A[0]
    assert sum(bi * (a // ai) for bi, ai in zip(b, A)) == 1
    return b


def saw2(x, a):
    """X(x) = 2a((x/a)) as int64 array."""
    r = np.mod(x, a)
    return np.where(r == 0, 0, 2 * r - a).astype(np.int64)


_Fcache = {}


def Farr(a, nu):
    """F(l) for l = 0..a-1, exact int64. F(l) = sum_x X(x)[X(nu x) - X(nu x + l)]."""
    key = (a, nu % a)
    if key in _Fcache:
        return _Fcache[key]
    x = np.arange(a, dtype=np.int64)
    X = saw2(x, a)
    # A(y) := X(nu^{-1} y), so sum_x X(x) X(nu x + l) = sum_y A(y) X(y + l)
    if a == 1:
        F = np.zeros(1, dtype=np.int64)
        _Fcache[key] = F
        return F
    nuinv = pow(nu % a, -1, a)
    Ay = X[(nuinv * x) % a]
    corr = np.empty(a, dtype=np.int64)
    # chunked direct correlation (exact integers)
    CH = max(1, 4_000_000 // a)
    for l0 in range(0, a, CH):
        ls = np.arange(l0, min(a, l0 + CH), dtype=np.int64)
        idx = (x[None, :] + ls[:, None]) % a
        corr[l0:l0 + len(ls)] = (X[idx] * Ay[None, :]).sum(axis=1)
    F = corr[0] - corr
    _Fcache[key] = F
    return F


def cone_terms(A, sign=None):
    sign = SIGN if sign is None else sign
    b = bvec(A)
    return [Farr(ai, sign * bi) for ai, bi in zip(A, b)], b


def enumerate_reps(A, sign=None, want_all=False):
    """Return dict with N (# irreducibles), min/max exact c with argmin/argmax label lists.
    Labels are (eps, l1, l2, l3)."""
    A = tuple(A)
    assert all(gcd(A[i], A[j]) == 1 for i in range(3) for j in range(i + 1, 3))
    if min(A) == 1:
        return dict(N=0, cmin=None, cmax=None, argmin=[], argmax=[], reps=[])
    a = prod(A)
    F, b = cone_terms(A, sign)
    fl = [F[i].astype(np.float64) / (8.0 * A[i] ** 2) for i in range(3)]
    ls = [np.arange(1, A[i], dtype=np.int64) for i in range(3)]
    Xs = [ls[i] * (a // A[i]) for i in range(3)]
    best = None
    worst = None
    N = 0
    allreps = []
    # chunk over l1
    for eps in (1, -1):
        par = []
        for i in range(3):
            if eps == 1:
                par.append(ls[i] % 2 == 0)
            else:
                par.append(ls[i] % 2 == (b[i] % 2))
        i1 = np.nonzero(par[0])[0]
        i2 = np.nonzero(par[1])[0]
        i3 = np.nonzero(par[2])[0]
        if len(i1) == 0 or len(i2) == 0 or len(i3) == 0:
            continue
        X2 = Xs[1][i2]
        X3 = Xs[2][i3]
        f2 = fl[1][ls[1][i2]]
        f3 = fl[2][ls[2][i3]]
        CH = max(1, 6_000_000 // (len(i2) * len(i3)))
        for c0 in range(0, len(i1), CH):
            j1 = i1[c0:c0 + CH]
            X1 = Xs[0][j1][:, None, None]
            S = X1 + X2[None, :, None]
            D = np.abs(X1 - X2[None, :, None])
            X3b = X3[None, None, :]
            ok = (X3b > D) & (X3b < np.minimum(S, 2 * a - S))
            n = int(ok.sum())
            if n == 0:
                continue
            N += n
            val = fl[0][ls[0][j1]][:, None, None] + f2[None, :, None] + f3[None, None, :]
            vmin = np.where(ok, val, np.inf)
            vmax = np.where(ok, val, -np.inf)
            mn = vmin.min()
            mx = vmax.max()
            tol = 1e-9
            if best is None or mn < best[0] - tol:
                best = [mn, []]
            if mn <= best[0] + tol:
                w = np.argwhere(vmin <= best[0] + tol)
                best[1] += [(eps, int(ls[0][j1[p]]), int(ls[1][i2[q]]), int(ls[2][i3[r]])) for p, q, r in w]
            if worst is None or mx > worst[0] + tol:
                worst = [mx, []]
            if mx >= worst[0] - tol:
                w = np.argwhere(vmax >= worst[0] - tol)
                worst[1] += [(eps, int(ls[0][j1[p]]), int(ls[1][i2[q]]), int(ls[2][i3[r]])) for p, q, r in w]
            if want_all:
                w = np.argwhere(ok)
                allreps += [(eps, int(ls[0][j1[p]]), int(ls[1][i2[q]]), int(ls[2][i3[r]])) for p, q, r in w]

    def exact(lab):
        return sum(Fraction(int(F[i][lab[i + 1]]), 8 * A[i] ** 2) for i in range(3))

    out = dict(N=N, A=A, b=b)
    if N == 0:
        out.update(cmin=None, cmax=None, argmin=[], argmax=[], reps=[])
        return out
    ex = [(exact(l), l) for l in best[1]]
    cmin = min(e for e, _ in ex)
    out['cmin'] = cmin
    out['argmin'] = [l for e, l in ex if e == cmin]
    ex = [(exact(l), l) for l in worst[1]]
    cmax = max(e for e, _ in ex)
    out['cmax'] = cmax
    out['argmax'] = [l for e, l in ex if e == cmax]
    if want_all:
        out['reps'] = [(exact(l), l) for l in allreps]
    return out


def c_exact(A, lab, sign=None):
    F, b = cone_terms(A, sign)
    return sum(Fraction(int(F[i][lab[i + 1]]), 8 * A[i] ** 2) for i in range(3))


def c_fs_float(A, lab, sign=None):
    """M2: FS-parametrised float cot sum with e from CRT (e = l_i a/a_i mod a_i)."""
    sign = SIGN if sign is None else sign
    a = prod(A)
    e = crt([(lab[i + 1] * (a // A[i])) % A[i] for i in range(3)], A)
    tot = 0.0
    for ai in A:
        k = np.arange(1, ai, dtype=np.float64)
        tot += (1.0 / ai) * np.sum(1.0 / np.tan(np.pi * ((a * np.arange(1, ai)) % (ai * ai)) / ai ** 2)
                                    / np.tan(np.pi * k / ai) * np.sin(np.pi * ((e * np.arange(1, ai)) % ai) / ai) ** 2)
    return sign * tot / 4.0


def crt(rs, ms):
    x, M = 0, 1
    for r, m in zip(rs, ms):
        # x = x mod M, need x' = r mod m
        t = ((r - x) * pow(M, -1, m)) % m
        x = x + M * t
        M *= m
    return x % M


def ell(A, orient=1):
    """ell of orient*Sigma(A); returns Fraction or None for +infinity (S^3)."""
    A = tuple(sorted(A))
    if A[0] == 1:
        return None
    R = enumerate_reps(A)
    if R['N'] == 0:
        return None
    if orient == 1:
        return R['cmin']
    return Fraction(3, 8) - R['cmax']


def ell_full(A, orient=1):
    A = tuple(A)
    if min(A) == 1:
        return None, None
    R = enumerate_reps(A)
    if orient == 1:
        return R['cmin'], R
    return Fraction(3, 8) - R['cmax'], R


def brieskorn_sigma(A):
    """Brieskorn's signature of the Milnor fibre of x^p+y^q+z^r (sign: E8 -> -8)."""
    p, q, r = A
    a = p * q * r
    i = np.arange(1, p)[:, None, None] * (q * r)
    j = np.arange(1, q)[None, :, None] * (p * r)
    k = np.arange(1, r)[None, None, :] * (p * q)
    s = i + j + k  # s/a in (0,3)
    neg = ((s > a) & (s < 2 * a)).sum()
    pos = ((s < a) | (s > 2 * a)).sum()
    return int(pos - neg)


def lam(A, orient=1):
    """Casson invariant via rep count, lambda(Sigma) = -N/2 (link orientation)."""
    if min(A) == 1:
        return Fraction(0)
    R = enumerate_reps(tuple(A))
    return Fraction(-orient * R['N'], 2)


def surg(A, K, n):
    """(orient, A') with Sigma_{-1/n}(K) = orient*Sigma(A'), per the CLAIMED rule (link-oriented Sigma).
    K = index of the fibre. n any integer (n<0 means +1/|n| surgery)."""
    A = list(A)
    P = prod(A) // A[K]
    m = A[K] + n * P
    o = 1 if m > 0 else -1
    A[K] = abs(m)
    return o, tuple(A)
