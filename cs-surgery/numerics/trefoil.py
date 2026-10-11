"""Right-handed trefoil: pillowcase curve, f_Gamma, CS of 1/n surgeries, SO(3) line b=1/2.

pi_1 = <x, y | x^2 = y^3>,  mu = y^-1 x,  lambda = x^2 mu^-6.
Irreducible SU(2) reps: x = pure unit quaternion u (tr 0), y = 1/2 + (sqrt3/2) v (tr 1),
angle(u, v) = phi in (0, pi).  phi -> 0 is the reducible endpoint.
"""
import sys
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from pillow import quat, inv, ab_from, unwrap, cumtrapz, kk_surgery_cs, dist_mod1, rat
from brieskorn_fs import fs_values

s3 = np.sqrt(3) / 2


def rep(phi):
    x = quat(0, np.cos(phi), np.sin(phi), 0)
    y = quat(0.5, s3, 0, 0)
    mu = inv(y) @ x
    lam = x @ x @ np.linalg.matrix_power(inv(mu), 6)
    return x, y, mu, lam


def checks():
    worst = 0
    for phi in np.linspace(0.01, np.pi - 0.01, 37):
        x, y, mu, lam = rep(phi)
        worst = max(worst,
                    np.linalg.norm(x @ x + np.eye(2)),
                    np.linalg.norm(np.linalg.matrix_power(y, 3) + np.eye(2)),
                    np.linalg.norm(mu @ lam - lam @ mu))
    # abelianisation: x -> t^3, y -> t^2  (x^2 = y^3)  =>  mu -> t^{-2+3} = t, lambda -> t^{6-6} = 1
    print(f"[checks] max |x^2+1|, |y^3+1|, |[mu,lambda]| over sample = {worst:.2e}")
    print("[checks] H_1: x->3, y->2 (generator t=mu): mu = y^-1 x -> 1, lambda = x^2 mu^-6 -> 6-6 = 0")


# ---------- the curve -------------------------------------------------------
N = 400001
PHI = np.linspace(0.0, np.pi, N)


def curve():
    A = np.empty(N)
    B = np.empty(N)
    R = 0.0
    for i, ph in enumerate(PHI):
        a, b, res = ab_from(*rep(ph)[2:])
        A[i], B[i] = a, b
        R = max(R, res)
    B = unwrap(B)
    B -= np.round(B[0])  # lift with b = 0 at the reducible endpoint
    return A, B, R


def F_closed(a):
    """-int 2 b da along Gamma from (1/12,0), with lift b = 1/2 - 6a"""
    return -(a - 6 * a * a) + Fr(1, 24) if isinstance(a, Fr) else -(a - 6 * a * a) + 1 / 24


def main():
    checks()
    A, B, R = curve()
    print(f"[curve] max eigvec residual {R:.1e}; a range [{A[0]:.6f}, {A[-1]:.6f}] (expect 1/12={1/12:.6f}, 5/12={5/12:.6f})")
    print(f"[curve] b(0)={B[0]:.2e}, b(pi)={B[-1]:.6f}; max |b - (1/2 - 6a)| = {np.max(np.abs(B - (0.5 - 6 * A))):.2e}")
    F = -2 * cumtrapz(B, A)
    print(f"[curve] max |F_numeric - F_closed| = {np.max(np.abs(F - F_closed(A))):.2e}")
    print("        closed form: Gamma lift b = 1/2 - 6a, a in [1/12, 5/12];  f_Gamma(a) = -(a - 6a^2) + 1/24")

    # ---------- 1/n surgeries ------------------------------------------------
    results = {}
    print("\n=== Surgeries S^3_{p/q}(RHT): points of Gamma ∩ {pa+qb in Z} and their CS ===")
    print("CS_KK = Kirk-Klassen/A-H (5.67) (path: trivial -> reducible endpoint along b=0 -> Gamma).")
    print("claim(I1): f_G(y) - f_L(y) with f_L := -a*b at the lifted point (= pq s^2 on L_0, extended)")
    print("claim(I2): f_L = pq s^2 with s from translating the lifted point to L_0 by an a-shift (p | k)")
    print("claim(I3): f_L = pq s^2 with s from translating by a b-shift (q | k)")
    for (p, q) in [(1, 1), (1, 2), (1, 3), (-1, 1), (-1, 2), (-1, 3)]:
        g = p * A + q * B
        ks = range(int(np.floor(g.min())) - 1, int(np.ceil(g.max())) + 2)
        pts = []
        for k in ks:
            idx = np.where(np.sign(g[:-1] - k) * np.sign(g[1:] - k) < 0)[0]
            for i in idx:
                # refine using the closed-form lift (verified above to 1e-12)
                fa = lambda ph: p * ab_from(*rep(ph)[2:])[0] + q * (B[i] + (((ab_from(*rep(ph)[2:])[1] - B[i]) + 0.5) % 1 - 0.5)) - k
                ph = brentq(fa, PHI[i], PHI[i + 1], xtol=1e-15)
                a, bb, _ = ab_from(*rep(ph)[2:])
                b = B[i] + (((bb - B[i]) + 0.5) % 1 - 0.5)
                aF = Fr(2 * k - q, 2 * (p - 6 * q))  # exact: p a + q (1/2 - 6a) = k
                Fnum = np.interp(a, A, F)
                pts.append((a, b, k, Fnum, aF))
        pts.sort()
        rows = []
        for a, b, k, Fnum, aF in pts:
            bF = Fr(1, 2) - 6 * aF
            Fex = F_closed(aF)
            c, d = __import__('pillow').cd_for(p, q)
            cs_ex = (Fex - c * p * aF ** 2 - d * q * bF ** 2 - 2 * c * q * aF * bF) % 1
            cs_num = kk_surgery_cs(Fnum, a, b, p, q) % 1
            I1 = (Fex + aF * bF) % 1
            I2 = (Fex - p * q * ((aF - Fr(k, p)) / q) ** 2) % 1 if k % p == 0 else None
            I3 = (Fex - p * q * (aF / q) ** 2) % 1 if k % q == 0 else None
            rows.append(dict(a=aF, b=bF, k=k, F=Fex, cs=cs_ex, cs_num=cs_num, I1=I1, I2=I2, I3=I3))
        results[(p, q)] = rows
        r = 6 * q - p if 6 * q - p > 0 else p - 6 * q
        fsS = fs_values((2, 3, abs(6 * q - p)))
        print(f"\n-- p/q = {p}/{q}:  {len(rows)} irreducible points; Seifert: Sigma(2,3,{abs(6*q-p)})")
        print(f"   {'a':>8} {'b~(lift)':>9} {'k':>3} {'f_Gamma':>10} {'CS_KK exact':>12} {'|num-exact|':>11} {'claim I1':>9} {'claim I2':>9} {'claim I3':>9}")
        for rr in rows:
            err = dist_mod1(float(rr['cs']), rr['cs_num'])
            f = lambda v: '   n/a' if v is None else str(v)
            print(f"   {str(rr['a']):>8} {str(rr['b']):>9} {rr['k']:>3} {str(rr['F']):>10} {str(rr['cs']):>12} {err:11.1e} {f(rr['I1']):>9} {f(rr['I2']):>9} {f(rr['I3']):>9}")
        kk = sorted(rr['cs'] for rr in rows)
        print(f"   CS_KK set           = {[str(v) for v in kk]}")
        print(f"   FS  Sigma(2,3,{abs(6*q-p)})    = {[str(v) for v in fs_values((2,3,abs(6*q-p)))]}")
        print(f"   FS -Sigma(2,3,{abs(6*q-p)})    = {[str(v) for v in sorted((-v) % 1 for v in fsS)]}")
        print(f"   CS_KK == FS(+Sigma)? {kk == sorted(fsS)}   CS_KK == FS(-Sigma)? {kk == sorted((-v) % 1 for v in fsS)}")
        for key in ('I1', 'I2', 'I3'):
            vals = [rr[key] for rr in rows]
            if None in vals:
                print(f"   claim {key}: not defined for all points")
            else:
                print(f"   claim {key} set == CS_KK set? {sorted(vals) == kk}")

    # ---------- SO(3): line b = 1/2 (0-surgery, w2 != 0) -----------------------
    print("\n=== Gamma ∩ {b = 1/2} (0-surgery, nontrivial SO(3) bundle) ===")
    so3 = []
    for aF in [Fr(1, 6), Fr(1, 3)]:
        bF = Fr(1, 2) - 6 * aF
        Fex = F_closed(aF)
        A_lit = Fex - (-aF)            # literal: f_L = -a on b=1/2 (base point (0,1/2)), evaluated at lifted a
        A_neg = Fex - (+aF)            # if the lifted point sits on b=-1/2 (odd lift) and one uses f_L=-2(-1/2)a=+a
        A_kk = Fex + 2 * aF * bF       # A-H (5.67) with (p,q)=(0,1), c=-1, d=0 (lift-consistent)
        so3.append(dict(a=aF, b=bF, F=Fex, A_lit=A_lit % 1, A_neg=A_neg % 1, A_kk=A_kk % 1))
        print(f"   a={aF}, lifted b={bF}, f_Gamma={Fex}:  A_lit=f_G+a={A_lit % 1}, A_alt=f_G-a={A_neg % 1}, A_KK(lift-corrected)=f_G+2ab={A_kk % 1}")
    print("   note: A_KK is only defined mod 1/4 (changing d by 1 shifts it by -b^2 = -1/4 mod 1 at b in 1/2+Z)")

    # ---------- corner-offset test --------------------------------------------
    print("\n=== Corner-offset test: CS(1/(n+1)) =? CS(1/n) ∪ {A(x) + off} (mod 1) ===")
    for n, off_pred in [(1, Fr(1, 4)), (2, Fr(2, 4))]:
        big = sorted(rr['cs'] for rr in results[(1, n + 1)])
        small = sorted(rr['cs'] for rr in results[(1, n)])
        for Akey in ('A_lit', 'A_neg', 'A_kk'):
            for sgn, lab in [(1, 'KK sign'), (-1, 'FS sign')]:
                bigS = sorted((sgn * v) % 1 for v in big)
                smallS = [(sgn * v) % 1 for v in small]
                for off in [Fr(j, 4) for j in range(4)]:
                    pred = sorted(smallS + [(sgn * d[Akey] + off) % 1 for d in so3])
                    if pred == bigS:
                        print(f"   MATCH n={n}: {Akey}, {lab}, offset {off}")
        print(f"   n={n}: CS_KK(S^3_1/{n+1}) = {[str(v) for v in big]}")
        print(f"          CS_KK(S^3_1/{n})   = {[str(v) for v in small]}")
        for Akey in ('A_lit', 'A_neg', 'A_kk'):
            print(f"          {Akey} + {off_pred} = {[str((d[Akey] + off_pred) % 1) for d in so3]};  {Akey} - {off_pred} = {[str((d[Akey] - off_pred) % 1) for d in so3]}")
        # nearest distances: for each big value, nearest element of the predicted multiset
        pred = [float(v) for v in small] + [float((d['A_lit'] + off_pred) % 1) for d in so3]
        print("          distances (each CS(1/(n+1)) value to nearest predicted value, A_lit + offset):",
              [round(min(dist_mod1(float(v), w) for w in pred), 5) for v in big])
    return results, so3, A, B, F


if __name__ == "__main__":
    results, so3, A, B, F = main()
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    ax.plot(A, B % 1, ',', color='C0', ms=1)
    ax.plot(A, B % 1, '.', color='C0', ms=0.5, label=r'$\Gamma_{RHT}$: $b=1/2-6a$ (mod 1)')
    ax.plot([1 / 12, 5 / 12], [0, 0], 'ko', ms=5, label='reducible endpoints')
    sl = np.linspace(0, 0.5, 400)
    for (p, q), col in [((1, 1), 'C1'), ((1, 2), 'C2'), ((-1, 1), 'C3')]:
        for k in range(-6, 7):
            bb = (k - p * sl) / q
            m = (bb >= 0) & (bb <= 1)
            ax.plot(sl[m], bb[m], '-', color=col, lw=0.8, label=f'$L_{{{p}/{q}}}$' if k == 0 else None)
        for rr in results[(p, q)]:
            ax.plot(float(rr['a']), float(rr['b']) % 1, 'o', color=col, ms=5, mfc='none')
    ax.axhline(0.5, color='C4', lw=0.8, ls='--', label='$b=1/2$')
    for d in so3:
        ax.plot(float(d['a']), 0.5, 's', color='C4', ms=5, mfc='none')
    ax.set_xlim(0, 0.5); ax.set_ylim(0, 1)
    ax.set_xlabel('a  (meridian)'); ax.set_ylabel('b  (longitude)')
    ax.set_title('RHT pillowcase (a in [0,1/2], b in [0,1))')
    ax.legend(fontsize=7, loc='upper right')
    fig.tight_layout()
    fig.savefig(__file__.rsplit('/', 1)[0] + '/trefoil_pillowcase.png', dpi=150)
    print("\nwrote trefoil_pillowcase.png")
