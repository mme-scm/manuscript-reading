"""triangle-1: torus-knot machinery (re-implemented from the formulas of gap16/ell-code/torus.py,
tables.py, twistedw.py, which were calibrated there against DLME Example 3.7 and Fintushel-Stern),
plus the traceless singular theory of (S^3, T_{p,q}).

Conventions (all as in ell-1.md / pillowcase-1.md):
  K = T_{p,q}, p,q > 0 coprime (right-handed, positive).  Pillowcase: rho(mu) ~ e^{2 pi i a}, rho(lambda) ~ e^{2 pi i b}.
  Irreducible arcs (k,l): 0<k<p, 0<l<q, k=l mod 2, on b = k/2 - pq a, a in (amin, amax).
  Y_N untwisted generators: N a + b in Z; twisted (w2 != 0, N even): N a + b in 1/2 + Z.
  CS_D (DLME sign) = -(pq (a^2 - a0^2) - N a^2) mod 1.
  rho^m = -rho (DLME rho);  c = CS~ - gr/8 = (3 - rho^m)/16 = (3 + rho)/16.
  absolute level f^abs = rho/16 = -rho^m/16 for every bundle.
Traceless singular theory, Seifert-framed cap normalisation (see triangle-1.md, Sec. 1):
  c^tl(x) := 3(1+b^+(W))/8 + (ind A - 8 kappa(A) - s(F))/8 for any cap (W,F) of (S^3,K),
  s(F) = chi(F) + F.F/2 (KM index - 8 kappa formula), F.F relative to the Seifert framing.
  Computed through the flat singular connection A_N on (-X_N^o, D) at a traceless point x common with Y_N:
     c^tl(x) = c(Y_N,x) + (3 b^+(-X_N^o) + ind(A_N) - s(D))/8,  b^+ = [N<0], s(D) = 1 - N/2,
     ind(A_N) = -[Q_N > 0],  Q_N = pq - N  (twisted self-intersection; twisted framing of K = pq).
  CS^tl(x) = CS_D(Y_N,x) + N/16  (mod 1/2);  gr^tl = 8 (CS^tl - c^tl) mod 4.
"""
from fractions import Fraction as Fr
from math import cos, sin, pi


def cot(x):
    return cos(x) / sin(x)


def s_fun(l, a, B):
    if a == 1:
        return 0.0
    return 2.0 / a * sum(cot(pi * j / a) * cot(pi * B * j / a) * sin(pi * l * j / a) ** 2 for j in range(1, a))


def rat(x, den=10 ** 7, tol=1e-7):
    f = Fr(x).limit_denominator(den)
    assert abs(float(f) - x) < tol, (x, f)
    return f


def fold(t):
    t = Fr(t) % 1
    return 1 - t if t > Fr(1, 2) else t


def arcs(p, q):
    for d in range(-p * q, p * q + 1):
        if (1 - q * d) % p == 0:
            c = (1 - q * d) // p
            break
    out = []
    for k in range(1, p):
        for l in range(1, q):
            if (k - l) % 2:
                continue
            e1 = fold(Fr(d * k, 2 * p) + Fr(c * l, 2 * q))
            e2 = fold(Fr(d * k, 2 * p) - Fr(c * l, 2 * q))
            out.append((k, l, min(e1, e2), max(e1, e2)))
    return out


B_of = lambda p, q: (q % p, p % q, -1)


def rho_m(p, q, N, k, l, a):
    m = p * q - N
    e = Fr(N, p * q * m)
    sg = 1 if e > 0 else -1
    B1, B2, B3 = B_of(p, q)
    return rat(-3 * sg + 2 * (s_fun(k, p, B1) + s_fun(l, q, B2) + s_fun(float(2 * a * m), m, B3)))


def gens(p, q, N, twisted=False):
    """generators of Y_N(T_{p,q}) (SU(2) count: chi-pairs both listed), N < pq."""
    m = p * q - N
    assert m > 0
    shift = Fr(1, 2) if twisted else Fr(0)
    res = []
    for (k, l, amin, amax) in arcs(p, q):
        a0 = amin
        for j in range(-4 * m, 4 * m):
            a = (Fr(k, 2) - shift + j) / m
            if amin < a < amax:
                cs = p * q * (a * a - a0 * a0) - N * a * a
                CSD = (-cs) % 1
                r = rho_m(p, q, N, k, l, a)
                c = (3 - r) / 16
                gr = 8 * CSD - (3 - r) / 2   # untwisted: integer; twisted: see below
                res.append(dict(k=k, l=l, a=a, b=(Fr(k, 2) - p * q * a) % 1, CSD=CSD, rho=-r, c=c, fabs=-r / 16, gr=gr))
    return res


def sigma_torus(p, q):
    neg = pos = 0
    for i in range(1, p):
        for j in range(1, q):
            x = Fr(i, p) + Fr(j, q)
            if Fr(1, 2) < x < Fr(3, 2):
                neg += 1
            else:
                pos += 1
    return pos - neg


def traceless(p, q):
    """irreducible traceless SU(2) reps of T_{p,q} (a = 1/4 on an arc), as pillowcase points."""
    out = []
    for (k, l, amin, amax) in arcs(p, q):
        if amin < Fr(1, 4) < amax:
            b = (Fr(k, 2) - Fr(p * q, 4)) % 1
            out.append(dict(k=k, l=l, a=Fr(1, 4), b=b))
    return out


def common_N(p, q, x, Ns=range(-7, 8)):
    """odd/even N with x a generator of Y_N (untwisted): N/4 + b in Z."""
    return [N for N in Ns if N != 0 and N < p * q and (Fr(N, 4) + x['b']) % 1 == 0]


def ctl_via(p, q, x, N):
    """c^tl, CS^tl, gr^tl of the traceless generator x computed through Y_N (positive torus knot)."""
    G = [g for g in gens(p, q, N) if g['a'] == Fr(1, 4) and (g['k'], g['l']) == (x['k'], x['l'])]
    assert len(G) == 1, (p, q, N, x, G)
    g = G[0]
    bplus = 1 if N < 0 else 0
    s = 1 - Fr(N, 2)
    Q = p * q - N
    ind = -1 if Q > 0 else 0
    ctl = g['c'] + (3 * bplus + ind - s) / 8
    cstl = (g['CSD'] + Fr(N, 16)) % Fr(1, 2)
    grtl = (8 * (cstl - ctl)) % 4
    return dict(c=ctl, CS=cstl, gr=grtl, cYN=g['c'], N=N, ind=ind)


if __name__ == '__main__':
    # consistency of c^tl computed through different N
    for (p, q) in [(2, 3), (2, 5), (3, 4), (3, 5), (2, 7), (3, 7), (4, 5), (5, 7), (3, 8)]:
        T = traceless(p, q)
        print('T(%d,%d): sigma=%d, #traceless SU(2) irreducibles=%d' % (p, q, sigma_torus(p, q), len(T)))
        for x in T:
            Ns = common_N(p, q, x)
            vals = [ctl_via(p, q, x, N) for N in Ns]
            cs = sorted({v['c'] for v in vals}); grs = sorted({v['gr'] for v in vals}); css = sorted({v['CS'] for v in vals})
            print('   (k,l)=(%d,%d) b=%s  via N=%s  c^tl=%s  CS^tl=%s  gr^tl mod4=%s' % (
                x['k'], x['l'], x['b'], Ns, [str(c) for c in cs], [str(c) for c in css], [str(g) for g in grs]))
