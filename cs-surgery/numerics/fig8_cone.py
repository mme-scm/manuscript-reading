"""Figure-eight knot: test of the "exact cone with area corrections" statement.

Conventions (same as fig8.py):
  * Gamma~ : lift of the irreducible SU(2) circle, parameter psi (A-H branches), base point
    (a,b) = (1/6, 1/2) at psi = psi0, b lifted continuously; one circuit translates the lift by (0,-2).
    Gamma~ is extended to psi in [psi0 - 2pi, psi0 + 4pi] by that periodicity.
  * f(psi) = -int 2 b da along Gamma~ from the base point (RELATIVE normalisation, f(base)=0;
    the absolute KK value is f - 1/6; the constant cancels in every delta below).
  * omega = 2 da^db (counter-clockwise positive); -2b da is a primitive of omega
    (d(-2b da) = 2 da^db), so for a closed loop  oint(-2b da) = int omega = 2*(shoelace area).
  * Lines (lifts): L_{1/m} = {a + m b in Z},  L_0^w = {b in 1/2 + Z}.
  * Actions:  x' in Gamma ∩ L_{1/n}:  A(x') = f(x~') - n b~'^2   (A-H (5.67) with p=1,q=n,c=0,d=1;
    = reading I2 = Q-form)
    x in Gamma ∩ L_{1/(n-1)} (n>=2):  A_line(x) = f(x~) - (n-1) b~^2,   A_cone = A_line + (n-1)/4
    x in Gamma ∩ L_0^w:  A_lit(x) = f(x~) + a~ ("f_L = -a, base (0,1/2)", evaluated at the lifted
                          point even if b~ != 1/2),
                          A_KK(x) = f(x~) + 2 a~ b~ (lift-consistent: A-H (5.67) with (p,q)=(0,1), c=-1, d=0).
  * Zigzag Z_n (periodic PL curve in R^2): corner p = (-(n-1)/2, 1/2) = L_{1/(n-1)} ∩ {b=1/2},
    legs v1 = (-(n-1), 1) (along L_{1/(n-1)}) then v2 = (-1, 0) (along b = const), period v1+v2 = (-n,1).
    Leg midpoints m1 = p + v1/2, m2 = p + v1 + v2/2 lie on L_{1/n} (a+nb = 1) and are lifts of
    pillowcase corners (2m in Z^2), i.e. fixed points of iota(a,b) = (-a,-b) mod Z^2.
  * Isotopy Z_t (t in [0,1]): vertex P1(t) = (1-t) P1 + t (m1+m2)/2, P0(t) = 2 m1 - P1(t), P2(t) = 2 m2 - P1(t).
    Midpoints are fixed, the curve stays point-symmetric about every midpoint (=> iota-equivariant
    in the torus and zero flux relative to L_{1/n} for every t); Z_1 = L_{1/n}.
  * Graph description: coordinates u = a + n b, s = b - a. Z_t is the graph u = U_t(s); the full
    lattice preimage of the torus curve is {u = U_t(s + k) + k : k in Z} (translate by (k,0)).
"""
import sys
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from fig8 import oval_point, riley, LAM, U0, SU, STH, TH0
from pillow import word, cumtrapz, dist_mod1, rat

# ------------------------------------------------------------------ Gamma~
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
DB = round(B1[-1] - B1[0])  # -2
PSI = np.concatenate([P1c[:-1] - 2 * np.pi, P1c[:-1], P1c + 2 * np.pi])
AA = np.concatenate([A1[:-1], A1[:-1], A1])
BB = np.concatenate([B1[:-1] - DB, B1[:-1], B1 + DB])
FF = -2 * cumtrapz(BB, AA)
FF -= np.interp(psi0, PSI, FF)  # f(base) = 0
print(f"Gamma~: base ({AA[N]:.6f},{BB[N]:.6f}), circuit translation (0,{DB}), samples/circuit {N}")


def gam(ps):
    return np.interp(ps, PSI, AA), np.interp(ps, PSI, BB), np.interp(ps, PSI, FF)


# ------------------------------------------------------------------ zigzag
def zig(n, t):
    p = np.array([-(n - 1) / 2, 0.5]); v1 = np.array([-(n - 1), 1.0]); v2 = np.array([-1.0, 0.0])
    P0, P1, P2 = p, p + v1, p + v1 + v2
    m1, m2 = (P0 + P1) / 2, (P1 + P2) / 2
    P1t = (1 - t) * P1 + t * (m1 + m2) / 2
    P0t, P2t = 2 * m1 - P1t, 2 * m2 - P1t
    return dict(p=p, v1=v1, v2=v2, P0=P0t, P1=P1t, P2=P2t, m1=m1, m2=m2, per=v1 + v2)


def us(n, X):
    X = np.asarray(X)
    return X[..., 0] + n * X[..., 1], X[..., 1] - X[..., 0]


def U_fun(n, t, J=12):
    z = zig(n, t)
    verts = []
    for j in range(-J, J + 1):
        verts += [z['P0'] + j * z['per'], z['P1'] + j * z['per']]
    verts.append(z['P0'] + (J + 1) * z['per'])
    V = np.array(verts)
    uu, ss = us(n, V)
    assert np.all(np.diff(ss) > 0)
    return lambda s: np.interp(s, ss, uu)


def g_k(n, t, k, ps, Uf=None):
    Uf = Uf or U_fun(n, t)
    a, b, _ = gam(ps)
    u, s = a + n * b, b - a
    return u - k - Uf(s + k)


def all_zeros(n, t, kr=range(-10, 11)):
    """zeros (psi,k) with psi in one circuit [psi0, psi0+2pi)"""
    Uf = U_fun(n, t)
    sl = slice(N - 37, 2 * N - 37)  # one circuit, window offset so the base point is interior
    ps = PSI[sl]
    out = []
    for k in kr:
        g = g_k(n, t, k, ps, Uf)
        idx = np.where((g[:-1] < 0) != (g[1:] < 0))[0]
        for i in idx:
            r = brentq(lambda q: g_k(n, t, k, q, Uf), ps[i], ps[i + 1], xtol=1e-14)
            dg = (g_k(n, t, k, r + 1e-6, Uf) - g_k(n, t, k, r - 1e-6, Uf)) / 2e-6
            out.append((r, k, dg))
    return sorted(out)


def leg_info(n, X, k):
    """for X on Z_0 + (k,0): which leg, its midpoint (lifted)"""
    z = zig(n, 0.0)
    Y = X - np.array([k, 0.0])
    _, sY = us(n, Y)
    _, s0 = us(n, z['P0']); _, s1 = us(n, z['P1'])
    per = n + 1
    j = int(np.floor((sY - s0) / per))
    r = sY - s0 - j * per
    if r < s1 - s0:
        return 'L_1/(n-1)', z['m1'] + j * z['per'] + np.array([k, 0.0])
    return 'L_0^w', z['m2'] + j * z['per'] + np.array([k, 0.0])


def zz_path(n, X, k, m, leg):
    return [m, X]  # straight: X and m on the same leg


def omega_area(poly):
    P = np.asarray(poly)
    a, b = P[:, 0], P[:, 1]
    a2, b2 = np.roll(a, -1), np.roll(b, -1)
    return np.sum(a * b2 - a2 * b)  # = 2 * shoelace = int omega, omega = 2 da^db


# ------------------------------------------------------------------ 1. zero area
print("\n=== 1. signed omega-area between one period of Z_n and L_{1/n} (line through leg midpoints) ===")
for n in (1, 2, 3):
    z = zig(n, 0.0)
    # region between zigzag m1 -> P1 -> m2 -> P2 -> m1+per and the line back
    poly = [z['m1'], z['P1'], z['m2'], z['P2'], z['m1'] + z['per']]
    tri1 = omega_area([z['m1'], z['P1'], z['m2']]); tri2 = omega_area([z['m2'], z['P2'], z['m1'] + z['per']])
    print(f"  n={n}: corner p={z['p']}, m1={z['m1']} (a+nb={z['m1'] @ [1, n]:.0f}), m2={z['m2']} (a+nb={z['m2'] @ [1, n]:.0f});"
          f" triangle areas {tri1:+.6f}, {tri2:+.6f}; total over a period = {omega_area(poly):+.2e}")
    print(f"        corner p has a+nb = {z['p'] @ [1, n]:.2f} (the zigzag vertex is NOT on L_1/n; Z and L meet at the midpoints)")
    for t in (0.25, 0.5, 0.75):
        zt = zig(n, t)
        poly = [zt['m1'], zt['P1'], zt['m2'], zt['P2'], zt['m1'] + zt['per']]
        assert abs(omega_area(poly)) < 1e-12
print("  (also zero flux at t = 0.25, 0.5, 0.75 of the isotopy)")

# ------------------------------------------------------------------ 2. counts
print("\n=== 2. intersection counts with Gamma (pillowcase, i.e. points of the SU(2) circle) ===")
cnt = {}
for n in (0, 1, 2, 3):
    # straight lines: L_{1/0} = {a=0}: empty since a in [1/6,1/3]
    ps = PSI[N - 37:2 * N - 36]
    a, b, _ = gam(ps)
    g = a + n * b
    c = sum(np.count_nonzero((g[:-1] - k < 0) != (g[1:] - k < 0)) for k in range(-10, 11)) if n > 0 else int(np.any(np.abs(a) < 1e-9))
    cnt[n] = c
g = BB[N - 37:2 * N - 36] - 0.5
cnt['w'] = sum(np.count_nonzero((g[:-1] - k < 0) != (g[1:] - k < 0)) for k in range(-5, 6))
for n in (1, 2, 3):
    print(f"  n={n}: |Γ∩L_1/{n}| = {cnt[n]}   vs  |Γ∩L_1/{n-1}| + |Γ∩L_0^w| = {cnt[n-1]} + {cnt['w']} = {cnt[n-1] + cnt['w']}"
          f"   {'OK' if cnt[n] == cnt[n-1] + cnt['w'] else 'FAIL'}")

# ------------------------------------------------------------------ 3./4. isotopy, tracking, actions, areas
results = {}
for n in (1, 2, 3):
    print(f"\n=== 3. isotopy Z_t -> L_1/{n}, n={n} ===")
    Z0 = all_zeros(n, 0.0)
    print(f"  t=0: {len(Z0)} intersection points with Z_0 (expect {cnt[n-1] + cnt['w']})")
    tracks = [[(r, k)] for r, k, _ in Z0]
    ts = np.linspace(0, 1, 401)
    mincount = maxcount = len(Z0); mindg = min(abs(d) for _, _, d in Z0)
    maxjump = 0.0
    for t in ts[1:]:
        Uf = U_fun(n, t)
        for tr in tracks:
            r0, k = tr[-1]
            h = 2e-3
            while True:
                lo, hi = r0 - h, r0 + h
                glo, ghi = g_k(n, t, k, lo, Uf), g_k(n, t, k, hi, Uf)
                if glo * ghi < 0:
                    break
                h *= 2
                if h > 1.0:
                    raise RuntimeError("lost track")
            r = brentq(lambda q: g_k(n, t, k, q, Uf), lo, hi, xtol=1e-14)
            maxjump = max(maxjump, abs(r - r0))
            tr.append((r, k))
        if abs(t - round(t * 20) / 20) < 1e-9:
            zs = all_zeros(n, t)
            mincount = min(mincount, len(zs)); maxcount = max(maxcount, len(zs))
            mindg = min(mindg, min(abs(d) for _, _, d in zs))
    print(f"  #intersections over t in [0,1] (checked every 0.05): min {mincount}, max {maxcount}  -> no births/deaths: {mincount == maxcount}")
    print(f"  min |dg/dpsi| at intersection points = {mindg:.3e} (transversality), max tracked step |Δpsi| = {maxjump:.2e}")
    final = sorted(all_zeros(n, 1.0))
    ends = sorted((tr[-1][0] - 2 * np.pi * np.floor((tr[-1][0] - psi0) / (2 * np.pi))) for tr in tracks)
    print(f"  endpoints of tracks reduce to the {len(final)} points of Γ∩L_1/{n}: "
          f"{np.allclose(ends, [r for r, _, _ in final], atol=1e-9)}")
    rows = []
    for tr in tracks:
        (r0, k), (r1, _) = tr[0], tr[-1]
        a0, b0, f0 = gam(r0); a1, b1, f1 = gam(r1)
        X, Xp = np.array([a0, b0]), np.array([a1, b1])
        leg, m = leg_info(n, X, k)
        if leg == 'L_1/(n-1)':
            A_line = f0 - (n - 1) * b0 ** 2
            Acone = {'coord': A_line + (n - 1) / 4, 'KK': A_line}
        else:
            Acone = {'coord': f0 + a0, 'KK': f0 + 2 * a0 * b0}
        Ap = f1 - n * b1 ** 2
        # region: x~ --Gamma~--> x~' --L--> m --Z--> x~
        sel = (PSI > min(r0, r1)) & (PSI < max(r0, r1))
        arc = np.column_stack([AA[sel], BB[sel]])
        if r1 < r0:
            arc = arc[::-1]
        poly = [X] + list(arc) + [Xp, m]
        area = omega_area(poly)
        rows.append(dict(x=X, xp=Xp, k=k, leg=leg, m=m, Acone=Acone, Ap=Ap, area=area, psi=(r0, r1)))
    results[n] = rows
    print(f"\n  4. table n={n}   (f relative to base (1/6,1/2); actions as real numbers, compare mod 1)")
    print(f"  {'x~=(a,b)':>22} {'leg':>10} {'x~\'=(a,b)':>22} {'m (shared corner)':>16} {'A_cone(coord)':>13} {'A_cone(KK)':>10}"
          f" {'A(x\')':>9} {'area':>9} {'d_coord-area':>12} {'d_KK-area':>10}")
    for R in rows:
        dc = R['Ap'] - R['Acone']['coord']; dk = R['Ap'] - R['Acone']['KK']
        rc = ((dc - R['area'] + 0.5) % 1) - 0.5; rk = ((dk - R['area'] + 0.5) % 1) - 0.5
        R.update(dc=dc, dk=dk, rc=rc, rk=rk)
        print(f"  ({R['x'][0]:9.6f},{R['x'][1]:9.6f}) {R['leg']:>10} ({R['xp'][0]:9.6f},{R['xp'][1]:9.6f}) "
              f"({R['m'][0]:5.1f},{R['m'][1]:5.1f})      {R['Acone']['coord'] % 1:13.6f} {R['Acone']['KK'] % 1:10.6f} {R['Ap'] % 1:9.6f}"
              f" {R['area']:9.6f} {rc:12.6f} {rk:10.6f}")
        # predicted residuals from Stokes: delta - area = F_Z(m) - F_L(m)
        bm, am = R['m'][1], R['m'][0]
        if R['leg'] == 'L_1/(n-1)':
            pc = ((n - 1) * bm ** 2 - (n - 1) / 4) - n * bm ** 2
            pk = (n - 1) * bm ** 2 - n * bm ** 2
        else:
            pc = None  # literal convention is not a primitive along b = b_leg unless b_leg = 1/2
            pk = -2 * am * bm - n * bm ** 2
        R['pred'] = (pc, pk)
        print(f"        Stokes prediction: d_KK - area = F_Z(m) - F_L(m) = {((pk + .5) % 1) - .5:+.6f};"
              f" coord: {('%+.6f' % (((pc + .5) % 1) - .5)) if pc is not None else 'not a primitive (b~=%g)' % R['x'][1]}")

# ------------------------------------------------------------------ constant-shift test n=1
print("\n=== single constant shift test (n=1) ===")
rows = results[1]
for key in ('coord', 'KK'):
    c = [R['Acone'][key] % 1 for R in rows]; tgt = [R['Ap'] % 1 for R in rows]
    shifts = [(tg - cc) % 1 for cc, tg in zip(c, tgt)]
    print(f"  {key}: cone actions {[str(rat(v, 500)[0]) for v in c]}, targets {[str(rat(v, 500)[0]) for v in tgt]} (bijection from isotopy);"
          f" required shifts {[str(rat(s, 2000)[0]) for s in shifts]} -> single shift exists: {dist_mod1(shifts[0], shifts[1]) < 1e-6}")
    d_c = (c[1] - c[0]) % 1; d_t = (tgt[1] - tgt[0]) % 1
    print(f"       differences: cone {rat(d_c, 500)[0]}, target {rat(d_t, 500)[0]}; also no shift for the swapped bijection:"
          f" {dist_mod1(d_c, (-d_t) % 1) > 1e-6}")
print(f"  Using absolute f (subtract 1/6): KK cone actions = {[str(rat(R['Acone']['KK'] - 1/6, 500)[0]) for R in rows]}")

# ------------------------------------------------------------------ plot n=1
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
n = 1
fig, ax = plt.subplots(figsize=(7, 6))
for di in range(-3, 3):
    for dj in range(-2, 4):
        ax.plot(AA[N:2 * N + 1] + di, BB[N:2 * N + 1] + dj, '-', color='C0', lw=0.7, alpha=0.35)
sel = (PSI >= PSI[0]) & (PSI <= PSI[-1])
ax.plot(AA, BB, '-', color='C0', lw=1.4, label=r'$\tilde\Gamma$ (lift used)')
for k in range(-3, 4):
    z = zig(n, 0.0)
    V = np.array([z['P0'] + j * z['per'] + [k, 0] for j in range(-4, 5)] + [z['P1'] + j * z['per'] + [k, 0] for j in range(-4, 5)])
    V = V[np.argsort(us(n, V)[1])]
    ax.plot(V[:, 0], V[:, 1], '-', color='C3', lw=1.2, label=r'$Z_1$ (zigzag of $\{a=0\}$, $\{b=1/2\}$)' if k == 0 else None)
    s = np.linspace(-6, 6, 10)
    ax.plot(k + 1 - s, s, '--', color='C2', lw=1.0, label=r'$L_1=\{a+b\in\mathbb{Z}\}$' if k == 0 else None)
cols = ['C1', 'C4']
for R, col in zip(results[1], cols):
    r0, r1 = R['psi']
    sel = (PSI > min(r0, r1)) & (PSI < max(r0, r1))
    arc = np.column_stack([AA[sel], BB[sel]])
    if r1 < r0:
        arc = arc[::-1]
    poly = np.array([R['x']] + list(arc) + [R['xp'], R['m']])
    ax.add_patch(Polygon(poly, closed=True, fc=col, alpha=0.35, ec=col))
    ax.plot(*R['x'], 'o', color=col, ms=6); ax.plot(*R['xp'], 's', color=col, ms=6); ax.plot(*R['m'], '*', color='k', ms=9)
    ax.annotate(f"area={R['area']:.4f}", R['xp'], textcoords='offset points', xytext=(6, 6), fontsize=8, color=col)
ax.set_xlim(-1.3, 1.0); ax.set_ylim(-2.2, 1.7); ax.set_aspect('equal')
ax.set_xlabel('a'); ax.set_ylabel('b')
ax.set_title('4_1, n=1: Z_1 vs L_1; shaded: x~ -Γ~-> x~\' -L-> m -Z-> x~  (o = x, s = x\', * = m)', fontsize=9)
ax.legend(fontsize=7, loc='lower left')
fig.tight_layout()
fig.savefig(__file__.rsplit('/', 1)[0] + '/fig8_cone_n1.png', dpi=150)
print("\nwrote fig8_cone_n1.png")

# ------------------------------------------------------------------ precision of the Stokes identity
print("\n=== precision: max |(delta_KK - area) - (F_Z(m) - F_L(m))| (mod 1) and residual vs n/4 on the L_0^w leg ===")
for n, rows in results.items():
    err = max(dist_mod1(R['dk'] - R['area'], R['pred'][1]) for R in rows)
    errn4 = max(dist_mod1(R['dk'] - R['area'], n / 4 if R['leg'] == 'L_0^w' else 0.0) for R in rows)
    print(f"  n={n}: Stokes residual error {err:.2e};  'delta_KK = area + (n/4 on L_0^w, 0 on L_1/(n-1))' error {errn4:.2e}")
