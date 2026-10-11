"""Figure-eight knot 4_1: SU(2) pillowcase curve, f_Gamma, period, surgeries.

Group (Riley; same as Andersen-Hansen arXiv:math/0506456 (5.57)):
   pi = <x, y | w x = y w>,  w = x^-1 y x y^-1,  mu = x,
   lambda = y x^-1 y^-1 x^2 y^-1 x^-1 y.
Riley normal form: x -> [[s,1],[0,1/s]], y -> [[s,0],[z,1/s]].  sympy gives
   w x - y w = 0  <=>  z^2 + (s^2 + s^-2 - 3)(z - 1) = 0,
i.e. A-H's phi(t,u) = u^2 + (3 - t - 1/t)(u + 1) with u = -z, t = s^2.
SU(2) locus: s = e^{2 pi i theta}, z real (z = 2 sin^2(2 pi theta)(1 - cos phi) where phi is
the angle between the axes of x and y).  a = theta, e^{2 pi i b} = lambda_11.
"""
import sys
import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from pillow import quat, inv, word, ab_from, unwrap, cumtrapz, kk_surgery_cs, dist_mod1, rat
from brieskorn_fs import fs_values

W = "XyxY"
LAM = "yXYxxYXy"


def G(theta, u):
    c = np.cos(4 * np.pi * theta)
    return u * u + (3 - 2 * c) * (u + 1)


def riley(theta, u):
    s = np.exp(2j * np.pi * theta)
    z = -u
    x = np.array([[s, 1], [0, 1 / s]], dtype=complex)
    y = np.array([[s, 0], [z, 1 / s]], dtype=complex)
    return x, y


def su2_rep(theta, u):
    al = 2 * np.pi * theta
    z = -u
    cphi = 1 - z / (2 * np.sin(al) ** 2)
    phi = np.arccos(np.clip(cphi, -1, 1))
    x = quat(np.cos(al), np.sin(al), 0, 0)
    y = quat(np.cos(al), np.sin(al) * np.cos(phi), np.sin(al) * np.sin(phi), 0)
    return x, y


def AH_L(theta, eps):
    c = np.cos(4 * np.pi * theta)
    re = 2 * c * c - c - 2
    im = -eps * 2 * np.sin(4 * np.pi * theta) * np.sqrt(max(c * c - c - 0.75, 0.0))
    return re + 1j * im


# polar parametrisation of the oval G(theta,u)=0 about (1/4, -5/2)
TH0, U0, STH, SU = 0.25, -2.5, 0.1, 2.0


def oval_point(psi):
    f = lambda r: G(TH0 + r * STH * np.cos(psi), U0 + r * SU * np.sin(psi))
    r = brentq(f, 1e-9, 1.0 - 1e-12) if f(1e-9) * f(1.0 - 1e-12) < 0 else None
    return TH0 + r * STH * np.cos(psi), U0 + r * SU * np.sin(psi)


def main():
    # sanity: G(1/4 +- ..) and radial monotonicity
    N = 200000
    # start at the point theta = 1/6, u = -2 (where both A-H branches meet, L = -1)
    psi0 = np.arctan2((-2 - U0) / SU, (1 / 6 - TH0) / STH)
    PSI = np.linspace(psi0, psi0 + 2 * np.pi, N + 1)
    TH = np.empty(N + 1); U = np.empty(N + 1); Bm = np.empty(N + 1)
    rel = lc = un = su2err = ahErr = 0.0
    for i, ps in enumerate(PSI):
        th, u = oval_point(ps)
        TH[i], U[i] = th, u
        x, y = riley(th, u)
        gens = {'x': x, 'y': y}
        w = word(gens, W)
        rel = max(rel, np.linalg.norm(w @ x - y @ w))
        L = word(gens, LAM)
        lc = max(lc, abs(L[1, 0]), np.linalg.norm(L @ x - x @ L))
        un = max(un, abs(abs(L[0, 0]) - 1))
        Bm[i] = np.angle(L[0, 0]) / (2 * np.pi)
        if i % 997 == 0:
            xs, ys = su2_rep(th, u)
            g2 = {'x': xs, 'y': ys}
            ws = word(g2, W)
            a2, b2, res = ab_from(xs, word(g2, LAM))
            su2err = max(su2err, np.linalg.norm(ws @ xs - ys @ ws), dist_mod1(a2, th), dist_mod1(b2, Bm[i]), res)
            eps = +1 if np.sin(ps) > 0 else -1  # which A-H branch? decide by comparison below
            Lp, Lm = AH_L(th, 1), AH_L(th, -1)
            ahErr = max(ahErr, min(abs(Lp - L[0, 0]), abs(Lm - L[0, 0])))
    print(f"[checks] max |wx - yw| = {rel:.1e}; max |lambda_21|,|[lambda,x]| = {lc:.1e}; max ||lambda_11|-1| = {un:.1e}")
    print(f"[checks] explicit SU(2) quaternion rep: max(relation residual, |a-theta|, |b-b_Riley|) = {su2err:.1e}")
    print(f"[checks] lambda_11 vs A-H closed form L_+-(theta): max deviation = {ahErr:.1e}")
    print("         abelianisation: x,y -> t; lambda word exponent sums: x: -1+2-1=0, y: 1-1-1+1=0")

    A = TH
    B = unwrap(Bm)
    print(f"[curve] start point theta={A[0]:.12f} (1/6), b mod 1 = {B[0] % 1:.12f} (expect 1/2)")
    B += np.round(0.5 - B[0])  # integer shift only: A-H lift b = 1/2 at theta = 1/6
    # which branch first? (A-H: beta_+ runs 1/2 -> 3/2, beta_- runs 1/2 -> -1/2)
    imid = N // 4
    print(f"[curve] start (a,b)=({A[0]:.6f},{B[0]:.6f});  at psi=pi+pi/2: (a,b)=({A[imid]:.6f},{B[imid]:.6f})")
    j13 = np.argmax(A)
    print(f"[curve] a_max = {A[j13]:.8f} (1/3) with lifted b = {B[j13]:.6f};  end of loop (a,b)=({A[-1]:.6f},{B[-1]:.6f})")
    print(f"[curve] lift translation after one circuit: Delta b = {B[-1]-B[0]:.6f}  (Delta a = {A[-1]-A[0]:.1e})")

    # immersion / branch points
    dA = np.gradient(A, PSI); dB = np.gradient(B, PSI)
    speed = np.hypot(dA, dB)
    k = np.argmin(speed)
    print(f"[immersion] min |(a',b')| over the circle = {speed.min():.4e} at (a,b)=({A[k]:.5f},{B[k]%1:.5f}); "
          f"max = {speed.max():.4e}")
    za = np.where(np.sign(dA[:-1]) * np.sign(dA[1:]) < 0)[0]
    for i in za:
        print(f"   a' = 0 at (a,b mod 1) = ({A[i]:.6f}, {B[i] % 1:.6f}); there |b'| = {abs(dB[i]):.4f}  (fold of a, not a branch point)")
    zb = np.where(np.sign(dB[:-1]) * np.sign(dB[1:]) < 0)[0]
    for i in zb:
        print(f"   b' = 0 at (a,b mod 1) = ({A[i]:.6f}, {B[i] % 1:.6f}); there |a'| = {abs(dA[i]):.4f}")

    # f_Gamma and period
    F = -2 * cumtrapz(B, A)  # relative to base point (1/6, 1/2)
    per = -F[-1]  # oint 2 b da
    print(f"\n[period] oint 2 b da around the circle (lift as above) = {per:.12f}  ~ {rat(per)[0]} (exact value; not reduced mod 1)")
    print(f"         the lift is not closed: end = start + (0, {B[-1]-B[0]:.0f}).  KK transition for (a,b)->(a,b+n): c -> c - 2 n a")
    print(f"         consistency: oint(-2b da) + 2*Delta_b*a0 = {-per + 2*round(B[-1]-B[0])*A[0]:.12f}  (must be in Z)")
    # area check: symmetric form a db - b da
    sym = cumtrapz(A, B)[-1] - cumtrapz(B, A)[-1]
    print(f"         oint (a db - b da) = {sym:.12f}")

    # absolute normalisation of f via A-H: CS-path value at (1/6,1/2) is -2*(1/12) = -1/6 (SL(2,C) path)
    C0 = -1.0 / 6.0
    Fabs = C0 + F

    def find(gfun, label):
        g = gfun(A, B)
        out = []
        for kk in range(int(np.floor(g.min())) - 1, int(np.ceil(g.max())) + 2):
            idx = np.where(np.sign(g[:-1] - kk) * np.sign(g[1:] - kk) < 0)[0]
            for i in idx:
                t = (kk - g[i]) / (g[i + 1] - g[i])
                # refine on the dense grid by local cubic interpolation
                sl = slice(max(i - 3, 0), min(i + 5, N + 1))
                ps = brentq(lambda P: np.interp(P, PSI[sl], g[sl]) - kk, PSI[i], PSI[i + 1])
                a = np.interp(ps, PSI[sl], A[sl]); b = np.interp(ps, PSI[sl], B[sl]); f = np.interp(ps, PSI[sl], Fabs[sl])
                out.append((ps, a, b, kk, f))
        return out

    print("\n=== 4_1 surgeries S^3_{1/n}: CS via A-H (5.67)/Prop 4 (absolute constant -1/6 from the SL(2,C) path) ===")
    res = {}
    for n in [1, -1, 2, -2]:
        pts = find(lambda a, b: a + n * b, f"1/{n}")
        rows = []
        for ps, a, b, kk, f in pts:
            cs = kk_surgery_cs(f, a, b, 1, n) % 1
            rel_ = kk_surgery_cs(f - C0, a, b, 1, n) % 1
            rows.append((a, b, kk, f, cs, rel_))
        res[n] = rows
        print(f"\n-- 1/{n}: {len(rows)} points")
        print(f"   {'a':>10} {'b~':>10} {'k':>3} {'f (abs)':>10} {'CS abs':>10} {'~ rational':>12} {'CS rel(no const)':>16}")
        for a, b, kk, f, cs, rel_ in rows:
            fr, err = rat(cs, 2000)
            print(f"   {a:10.6f} {b:10.6f} {kk:3d} {f:10.6f} {cs:10.6f} {str(fr):>12} {rel_:16.6f}   (rat err {err:.1e})")
        if len(rows) == 2:
            d = (rows[1][4] - rows[0][4]) % 1
            print(f"   relative difference CS(2nd)-CS(1st) = {d:.10f} ~ {rat(d, 2000)[0]};  4/7 = {4/7:.10f}, 3/7 = {3/7:.10f}")
    fs = fs_values((2, 3, 7))
    print(f"\n   FS  Sigma(2,3,7) = {[str(v) for v in fs]} ;  FS -Sigma(2,3,7) = {[str((-v) % 1) for v in fs]}")

    # b = 1/2 line (0-surgery, SO(3))
    print("\n=== 4_1: Gamma ∩ {b = 1/2} ===")
    g = B - 0.5
    for kk in range(int(np.floor(g.min())) - 1, int(np.ceil(g.max())) + 2):
        idx = list(np.where(np.sign(g[:-1] - kk) * np.sign(g[1:] - kk) < 0)[0]) + list(np.where(np.abs(g - kk) < 1e-12)[0])
        for i in sorted(set(idx)):
            a, b, f = A[i], B[i], Fabs[i]
            print(f"   (a,b~)=({a:.6f},{b:.6f}): f_abs={f:.6f}; A_lit=f+a={(f + a) % 1:.6f}; A_KK=f+2ab={(f + 2*a*b) % 1:.6f} ~ {rat(f + 2*a*b, 500)[0]} (mod 1/4)")
    return A, B, res


if __name__ == "__main__":
    A, B, res = main()
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    ax.plot(A, B % 1, '.', ms=0.6, color='C0', label=r'$\Gamma_{4_1}$')
    for n, col in [(1, 'C1'), (-1, 'C3'), (2, 'C2'), (-2, 'C5')]:
        sl = np.linspace(0, 0.5, 400)
        for kk in range(-4, 5):
            bb = (kk - sl) / n
            m = (bb >= 0) & (bb <= 1)
            ax.plot(sl[m], bb[m], '-', lw=0.6, color=col, label=f'$L_{{1/{n}}}$' if kk == 0 else None)
        for a, b, kk, f, cs, rel_ in res[n]:
            ax.plot(a, b % 1, 'o', mfc='none', color=col, ms=5)
    ax.axhline(0.5, ls='--', lw=0.6, color='C4', label='b=1/2')
    ax.set_xlim(0, 0.5); ax.set_ylim(0, 1)
    ax.set_xlabel('a (meridian)'); ax.set_ylabel('b (longitude)')
    ax.set_title('Figure-eight knot: SU(2) pillowcase image')
    ax.legend(fontsize=7, loc='upper right')
    fig.tight_layout()
    fig.savefig(__file__.rsplit('/', 1)[0] + '/fig8_pillowcase.png', dpi=150)
    print("\nwrote fig8_pillowcase.png")
