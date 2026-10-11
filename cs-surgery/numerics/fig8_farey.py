"""Figure-eight knot: Farey-triad version of the exact cone with area corrections.

Conventions (as in fig8.py / fig8_cone.py):
  Gamma~: lift of the irreducible SU(2) circle, base (1/6,1/2), b continuous, circuit translation (0,-2).
  f = -int 2 b da along Gamma~ from the base (relative; absolute KK = f - 1/6, cancels in every delta).
  omega = 2 da^db, counter-clockwise positive; for closed loops  oint(-2b da) = int omega.
  Slope delta = p/q, class eps in {0,1}:  L_delta^eps = {p a + q b in eps/2 + Z},  v_delta = (q, -p).
  Q_delta(a,b) = c p a^2 + 2 c q a b + d q b^2  with p d - q c = 1   (A-H (5.67) / KK; used for BOTH eps;
     along any line {pa+qb = const} it is a primitive of -2b da; for eps=1 it is defined mod 1/4 by the
     choice of (c,d), but every delta below is independent of that choice).
  Action of x' in Gamma ∩ L_gamma: A(x') = f(x~') - Q_gamma(x~').
  Zigzag Z: half-lattice point P = L_alpha^ea ∩ L_beta^eb, vertices P -> P+v_a -> P+v_a+v_b, period v_g = v_a+v_b.
     midpoints m1 = P + v_a/2 (alpha leg), m2 = P + v_a + v_b/2 (beta leg).
  Cone actions: alpha-leg  A_cone = f - Q_a(x~) + kappa_a,  kappa_a = Q_a(m) - Q_g(m);  beta-leg likewise,
     with m = the (lifted) midpoint of the leg containing x~; we also report kappa evaluated at the base
     midpoints m1, m2 (the translate-independence question).
  Isotopy: P1(t) = (1-t) P1 + t (m1+m2)/2, P0(t) = 2 m1 - P1(t), P2(t) = 2 m2 - P1(t)  (midpoints fixed,
     point-symmetric about every midpoint => iota-equivariant, zero flux).
  Region R(x): x~ --Gamma~--> x~' --L_gamma--> m --Z--> x~.
"""
import sys
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from fig8 import oval_point, riley, LAM, U0, SU, STH, TH0
from pillow import word, cumtrapz, dist_mod1, rat, cd_for

# ---------------------------------------------------------------- Gamma~
N = 40000
psi0 = np.arctan2((-2 - U0) / SU, (1 / 6 - TH0) / STH)
P1c = np.linspace(psi0, psi0 + 2 * np.pi, N + 1)
A1 = np.empty(N + 1); B1 = np.empty(N + 1)
for i, ps in enumerate(P1c):
    th, uu = oval_point(ps)
    x, y = riley(th, uu)
    L = word({'x': x, 'y': y}, LAM)
    A1[i] = th; B1[i] = np.angle(L[0, 0]) / (2 * np.pi)
B1 = np.unwrap(2 * np.pi * B1) / (2 * np.pi)
B1 += np.round(0.5 - B1[0])
DB = round(B1[-1] - B1[0])
REP = 3
PSI = np.concatenate([P1c[:-1] + 2 * np.pi * j for j in range(-REP, REP)] + [P1c + 2 * np.pi * REP])
AA = np.concatenate([A1[:-1] for j in range(-REP, REP)] + [A1])
BB = np.concatenate([B1[:-1] + DB * j for j in range(-REP, REP)] + [B1 + DB * REP])
FF = -2 * cumtrapz(BB, AA)
FF -= np.interp(psi0, PSI, FF)
I0 = REP * N  # index of base point
WIN = slice(I0 - 37, I0 + N - 37)  # one circuit, base point interior


def gam(ps):
    return np.interp(ps, PSI, AA), np.interp(ps, PSI, BB), np.interp(ps, PSI, FF)


def Q(sl, X):
    p, q = sl
    c, d = cd_for(p, q)
    a, b = X[..., 0], X[..., 1]
    return c * p * a * a + 2 * c * q * a * b + d * q * b * b


def form(sl, X):
    return sl[0] * X[..., 0] + sl[1] * X[..., 1]


def v(sl):
    return np.array([sl[1], -sl[0]], dtype=float)


def line_hits(sl, eps):
    """points of Gamma (one circuit) on L_sl^eps; returns list of (psi, a, b)"""
    ps = PSI[WIN]
    a, b, _ = gam(ps)
    g = form(sl, np.column_stack([a, b])) - eps / 2
    out = []
    for k in range(-20, 21):
        h = g - k
        for i in np.where((h[:-1] < 0) != (h[1:] < 0))[0]:
            r = brentq(lambda q_: form(sl, np.array(gam(q_)[:2])) - eps / 2 - k, ps[i], ps[i + 1], xtol=1e-14)
            aa, bb, _ = gam(r)
            out.append((r, aa, bb))
    return sorted(out)


def red_count(p, eps):
    """reducible points (a,0) on L^eps with p a in eps/2+Z: torus count (a in [0,1)) and pillowcase (a in [0,1/2])"""
    tor = [Fr(2 * k + eps, 2 * abs(p)) for k in range(0, 2 * abs(p)) if 0 <= Fr(2 * k + eps, 2 * abs(p)) < 1] if p else None
    if p == 0:
        return ('all' if eps == 0 else 0), ('all' if eps == 0 else 0)
    tor = sorted(set(x % 1 for x in tor))
    pil = sorted(set(min(x, 1 - x) for x in tor))
    return len(tor), len(pil)


class Zig:
    def __init__(self, al, ea, be, eb):
        self.al, self.be = al, be
        self.ga = (al[0] + be[0], al[1] + be[1])
        M = np.array([al, be], dtype=float)
        self.det = al[0] * be[1] - al[1] * be[0]
        assert abs(self.det) == 1
        self.P = np.linalg.solve(M, [ea / 2, eb / 2])
        self.va, self.vb = v(al), v(be)
        self.vg = self.va + self.vb
        self.m1 = self.P + self.va / 2
        self.m2 = self.P + self.va + self.vb / 2
        w = self.va / np.linalg.norm(self.va) + self.vb / np.linalg.norm(self.vb)
        self.w = w
        assert self.va @ w > 0 and self.vb @ w > 0
        c_, d_ = cd_for(*self.ga)  # lattice vector with u = 1: (a,b) = (c'', d'') s.t. p_g a + q_g b = 1
        # solve p_g x + q_g y = 1
        pg, qg = self.ga
        for xx in range(-20, 21):
            if qg != 0 and (1 - pg * xx) % qg == 0:
                self.lam1 = np.array([xx, (1 - pg * xx) // qg], dtype=float); break
            if qg == 0 and pg * xx == 1:
                self.lam1 = np.array([xx, 0.0]); break

    def u(self, X):
        return form(self.ga, np.asarray(X))

    def s(self, X):
        return np.asarray(X) @ self.w

    def verts(self, t, J=14):
        P1 = self.P + self.va
        P1t = (1 - t) * P1 + t * (self.m1 + self.m2) / 2
        P0t = 2 * self.m1 - P1t
        V = []
        for j in range(-J, J + 1):
            V += [P0t + j * self.vg, P1t + j * self.vg]
        return np.array(V)

    def Ufun(self, t):
        """exactly periodic graph function (u(v_gamma) = 0): reduce s mod the period, then interpolate"""
        V = self.verts(t, J=1)[2:5]  # P0(t), P1(t), P0(t)+v_g
        uu, ss = self.u(V), self.s(V)
        assert np.all(np.diff(ss) > 0) and abs(uu[2] - uu[0]) < 1e-12
        s0, per = ss[0], ss[2] - ss[0]
        return lambda s_: np.interp(s0 + np.mod(np.asarray(s_) - s0, per), ss, uu)

    def g(self, t, k, ps, Uf):
        a, b, _ = gam(ps)
        X = np.stack([a, b], axis=-1)
        lam = k * self.lam1
        return self.u(X) - k - Uf(self.s(X) - lam @ self.w)

    def zeros(self, t, kr=range(-25, 26)):
        Uf = self.Ufun(t)
        ps = PSI[WIN]
        out = []
        for k in kr:
            gg = self.g(t, k, ps, Uf)
            for i in np.where((gg[:-1] < 0) != (gg[1:] < 0))[0]:
                r = brentq(lambda q_: self.g(t, k, q_, Uf), ps[i], ps[i + 1], xtol=1e-14)
                d = (self.g(t, k, r + 1e-6, Uf) - self.g(t, k, r - 1e-6, Uf)) / 2e-6
                out.append((r, k, d))
        return sorted(out)

    def leg(self, X, k):
        Y = X - k * self.lam1
        s0 = self.s(self.P); s1 = self.s(self.P + self.va); per = self.s(self.vg)
        j = int(np.floor((self.s(Y) - s0) / per))
        r = self.s(Y) - s0 - j * per
        sh = j * self.vg + k * self.lam1
        if r < s1 - s0:
            return 'alpha', self.m1 + sh
        return 'beta', self.m2 + sh


def omega_area(poly):
    P = np.asarray(poly)
    a, b = P[:, 0], P[:, 1]
    return np.sum(a * np.roll(b, -1) - np.roll(a, -1) * b)


def fmt(sl, e):
    return f"L_{sl[0]}/{sl[1]}^{'w' if e else '0'}"


def run(al, ea, be, eb, verbose=True):
    Z = Zig(al, ea, be, eb)
    ga = Z.ga
    eg_rule = (ea + eb + 1) % 2
    val = Z.u(Z.m1)
    eg_actual = int(round(2 * (val % 1))) % 2
    val2 = Z.u(Z.m2)
    print(f"\n##### ({fmt(al, ea)}, {fmt(be, eb)}) -> gamma = {ga[0]}/{ga[1]}   (ps-qr = {Z.det:+d})")
    print(f"  corner P = {Z.P}, m1 = {Z.m1}, m2 = {Z.m2}; gamma-form at m1, m2 = {val:.3f}, {val2:.3f}"
          f" -> balanced line is {fmt(ga, eg_actual)}; parity rule eps_g = ea+eb+1 = {eg_rule}: {'OK' if eg_rule == eg_actual else 'FAIL'}")
    eg = eg_actual
    # zero flux
    flux = []
    for t in (0.0, 0.3, 0.7):
        V = Z.verts(t, J=1)
        P0, P1 = V[2], V[3]
        P2 = 2 * Z.m2 - P1
        flux.append(omega_area([Z.m1, P1, Z.m2, P2, Z.m1 + Z.vg]))
    print(f"  flux over one period (t=0, .3, .7): {['%.1e' % f_ for f_ in flux]};  triangle areas at t=0: "
          f"{omega_area([Z.m1, Z.P + Z.va, Z.m2]):+.4f}, {omega_area([Z.m2, Z.P + Z.vg, Z.m1 + Z.vg]):+.4f}")
    # counts
    ha, hb, hg = line_hits(al, ea), line_hits(be, eb), line_hits(ga, eg)
    print(f"  |Γ∩{fmt(al, ea)}| = {len(ha)}, |Γ∩{fmt(be, eb)}| = {len(hb)}, |Γ∩{fmt(ga, eg)}| = {len(hg)}"
          f"  (expect 2|q|: {2*abs(al[1])}, {2*abs(be[1])}, {2*abs(ga[1])});  additivity: {'OK' if len(hg) == len(ha) + len(hb) else 'FAIL'}")
    ra, rb, rg = red_count(al[0], ea), red_count(be[0], eb), red_count(ga[0], eg)
    print(f"  reducibles (a,0) with p a in eps/2+Z  [torus, pillowcase]: alpha {ra}, beta {rb}, gamma {rg};"
          f" torus additivity p_g = p_a + p_b: {rg[0] == ra[0] + rb[0]}")
    # isotopy + tracking
    Z0 = Z.zeros(0.0)
    tracks = [[(r, k)] for r, k, _ in Z0]
    mind = min(abs(d) for *_, d in Z0) if Z0 else np.inf
    cmin = cmax = len(Z0)
    for t in np.linspace(0, 1, 401)[1:]:
        Uf = Z.Ufun(t)
        for tr in tracks:
            r0, k = tr[-1]
            h = 2e-3
            while (Z.g(t, k, r0 - h, Uf) < 0) == (Z.g(t, k, r0 + h, Uf) < 0):
                h *= 2
                if h > 1:
                    raise RuntimeError('lost track')
            tr.append((brentq(lambda q_: Z.g(t, k, q_, Uf), r0 - h, r0 + h, xtol=1e-14), k))
        if abs(t * 20 - round(t * 20)) < 1e-9:
            zs = Z.zeros(t)
            cmin, cmax = min(cmin, len(zs)), max(cmax, len(zs))
            if zs:
                mind = min(mind, min(abs(d) for *_, d in zs))
    hg_ps = sorted(r for r, _, _ in hg)
    ends = sorted(tr[-1][0] - 2 * np.pi * np.floor((tr[-1][0] - PSI[WIN][0]) / (2 * np.pi)) for tr in tracks)
    ok_end = len(ends) == len(hg_ps) and np.allclose(ends, hg_ps, atol=1e-8)
    print(f"  isotopy: #points at t=0: {len(Z0)}; over t: min {cmin}, max {cmax} (no birth/death: {cmin == cmax});"
          f" min transversality {mind:.2f}; endpoints = Γ∩{fmt(ga, eg)}: {ok_end}")
    rows = []
    for tr in tracks:
        (r0, k), (r1, _) = tr[0], tr[-1]
        a0, b0, f0 = gam(r0); a1, b1, f1 = gam(r1)
        X, Xp = np.array([a0, b0]), np.array([a1, b1])
        legn, m = Z.leg(X, k)
        sl, mb = (al, Z.m1) if legn == 'alpha' else (be, Z.m2)
        kap = Q(sl, m) - Q(ga, m)
        kap_base = Q(sl, mb) - Q(ga, mb)
        Acone = f0 - Q(sl, X) + kap
        Acone_b = f0 - Q(sl, X) + kap_base
        Ap = f1 - Q(ga, Xp)
        sel = (PSI > min(r0, r1)) & (PSI < max(r0, r1))
        arc = np.column_stack([AA[sel], BB[sel]])
        if r1 < r0:
            arc = arc[::-1]
        area = omega_area([X] + list(arc) + [Xp, m])
        res = ((Ap - Acone - area + .5) % 1) - .5
        res_b = ((Ap - Acone_b - area + .5) % 1) - .5
        rows.append((X, legn, Xp, m, kap % 1, kap_base % 1, Acone % 1, Ap % 1, area, res, res_b))
    if verbose:
        print(f"   {'x~':>20} {'leg':>5} {'x~\'':>20} {'m':>12} {'kappa(m)':>8} {'kappa(base)':>11} {'A_cone':>8} {'A(x\')':>8} {'area':>9} {'resid':>9} {'resid(base kappa)':>17}")
        for X, legn, Xp, m, kp, kb, Ac, Ap, ar, rs, rb_ in rows:
            print(f"   ({X[0]:8.5f},{X[1]:9.5f}) {legn:>5} ({Xp[0]:8.5f},{Xp[1]:9.5f}) ({m[0]:4.1f},{m[1]:5.1f}) "
                  f"{str(rat(kp, 64)[0]):>8} {str(rat(kb, 64)[0]):>11} {Ac:8.5f} {Ap:8.5f} {ar:9.5f} {rs:9.1e} {rb_:17.1e}")
    maxres = max(abs(r[9]) for r in rows) if rows else 0
    maxres_b = max(abs(r[10]) for r in rows) if rows else 0
    print(f"  max |A(x') - A_cone(x) - area| = {maxres:.1e} (kappa at the leg's own midpoint);  with kappa at base m1/m2: {maxres_b:.1e}")
    return dict(Z=Z, eg=eg, rows=rows, counts=(len(ha), len(hb), len(hg)), maxres=maxres, maxres_b=maxres_b,
                nobd=(cmin == cmax), ok_end=ok_end)


if __name__ == "__main__":
    print("=== Γ ∩ L^0 and Γ ∩ L^w for the slopes involved (points (a, b mod 1)) ===")
    for sl in [(1, 0), (1, 1), (2, 1), (1, 2), (2, 3), (3, 2)]:
        for e in (0, 1):
            h = line_hits(sl, e)
            print(f"  {fmt(sl, e):>10}: {len(h)} pts  " + ", ".join(f"({a:.5f},{b % 1:.5f})" for _, a, b in h))
    triads = [((1, 1), (1, 0), "a/b"), ((1, 2), (1, 1), "c"), ((2, 1), (1, 1), "d")]
    summary = []
    for al, be, lab in triads:
        for ea in (0, 1):
            for eb in (0, 1):
                R = run(al, ea, be, eb)
                summary.append((lab, fmt(al, ea), fmt(be, eb), fmt(R['Z'].ga, R['eg']), R['counts'], R['nobd'], R['ok_end'], R['maxres'], R['maxres_b']))
    print("\n=== SUMMARY ===")
    print(f"  {'triad':>5} {'alpha':>10} {'beta':>10} {'gamma':>10} {'counts a,b,g':>13} {'no b/d':>7} {'ends ok':>7} {'max resid':>9} {'resid w/ base kappa':>19}")
    for s_ in summary:
        print(f"  {s_[0]:>5} {s_[1]:>10} {s_[2]:>10} {s_[3]:>10} {str(s_[4]):>13} {str(s_[5]):>7} {str(s_[6]):>7} {s_[7]:9.1e} {s_[8]:19.1e}")
