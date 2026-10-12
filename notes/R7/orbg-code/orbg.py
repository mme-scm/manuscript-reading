"""tri-orbifold-g: Kawasaki/APS bookkeeping and pillowcase smoothings (tests, not proofs)."""
from fractions import Fraction as Fr
from math import cos, sin, pi, tan
import itertools

def cot(x): return cos(x)/sin(x)
def fr(x, d=10000): return Fr(x).limit_denominator(d)

# --- 1. APS rho of the adjoint flat connection gamma_k on L(p,q) (ledger.py convention) ---
def rho_lens(p, q, k):
    s = sum(cot(pi*j/p)*cot(pi*q*j/p)*sin(pi*k*j/p)**2 for j in range(1, p))
    return fr(-4*s/p)
print("rho(dnuS=L(4,-1)) k=0..3:", [str(rho_lens(4,-1,k)) for k in range(4)], " rho(RP3) k=0,1:", [str(rho_lens(2,-1,k)) for k in range(2)])

# middle-end term t = (3 - h + sign*rho)/16 ; sign=-1 for the end -dnuS (as in E), +1 for +dnuS (as in -E)
def t_end(p, k, sign):
    h = 3 if (2*k) % p == 0 and k % p == 0 else 1
    return Fr(3 - h, 16) + sign*rho_lens(p, -1, k)/16

# --- 2. Kawasaki defect of an isolated cone point C^2/Z_n (scalar weights (1,1)), isotropy = rotation 2 pi k/n on ad ---
# local index of d*+d^+ at g with angles (th,th):  -(1/2)(1 - cot(th/2)^2) ; twisted by chi_ad(g) = 1 + 2 cos(2 pi k j/n)
def kawasaki_delta(n, k):
    tot = 0.0
    for j in range(1, n):
        th = 2*pi*j/n
        chi = 1 + 2*cos(2*pi*k*j/n)
        tot += chi * (-0.5)*(1 - cot(th/2)**2)
    return fr(tot/n)
def dim_inv_ad(n, k):  # dim of Z_n-invariant part of ad under rotation 2 pi k/n
    return 3 if (k % n == 0) else (1)
print("\nCone points (orbifold blow-down of the sphere with boundary L(n,1)):")
for n in (2, 4):
    d_theta = kawasaki_delta(n, 0)
    for k in range(0, n//2 + 1):
        d = kawasaki_delta(n, k)
        s_orb = d - d_theta
        i_cone = -dim_inv_ad(n, k); h = 3 if k == 0 else 1
        # APS route: s_orb/8 = (i_cone + h)/8 + t(gamma, -end)
        aps = 8*((Fr(i_cone + h, 8)) + t_end(n, k, -1))
        print(f"  C^2/Z_{n}, isotropy k={k}: Kawasaki delta={d}, s_orb=delta-delta_theta={s_orb}, APS check s_orb={aps}, "
              f"rigid level of the exterior map = {-s_orb/8}")

# --- 3. KM singular term along a surface with holonomy alpha (cone angle 4 pi alpha... alpha=1/4 <-> pi, 1/8 <-> pi/2) ---
def s_KM(alpha, l, chi, self_int):
    return 4*l*(1 - 4*alpha) + chi + 8*alpha**2*self_int
print("\nSingular term s(l) = 4l(1-4a) + chi + 8a^2 F.F:")
for (name, chi, ff) in (("core disk D (in -X_2^o)", 1, -2), ("sphere S in W'", 2, -4)):
    for alpha in (Fr(1,4), Fr(1,8)):
        vals = {l: s_KM(alpha, l, chi, ff) for l in (-2, -1, 0, 1)}
        print(f"  {name}, alpha={alpha}: " + ", ".join(f"l={l}: s={v}" for l, v in vals.items()))
print("  => family on (W',S,alpha=1/8), i0=-1: level (i0 - s)/8 by sector:",
      {l: str(Fr(-1,8) - s_KM(Fr(1,8), l, 2, -4)/8) for l in (-3,-2,-1,0,1)})

# --- 4. ledger values of the side maps of the four single-cone triangles ---
def lvl(bplus, i0, s, ends):
    return Fr(3*bplus, 8) + Fr(i0, 8) - Fr(s)/8 - sum(ends)
print("\nSide maps between Y_2 and Y_-2:")
print("  E_{g1}  (A->B, b+=0, gamma1 on -dnuS):", lvl(0, 0, 0, [t_end(4,1,-1)]))
print("  -E_{g1} (B->A, b+=1, gamma1 on +dnuS):", lvl(1, 0, 0, [t_end(4,1,+1)]))
print("  E_{g0}, E_theta (A->B):", lvl(0,0,0,[t_end(4,2,-1)]), lvl(0,0,0,[t_end(4,0,-1)]))
print("  -E_{g0}, -E_theta (B->A):", lvl(1,0,0,[t_end(4,2,+1)]), lvl(1,0,0,[t_end(4,0,+1)]))
print("  pm1 analogue: rigid RP3 exterior (b+=0, odd on -RP3):", lvl(0,0,0,[t_end(2,1,-1)]))

# --- 5. pillowcase Lagrangian surgery: crossings of L_2^e and L_-2^e' in T^2, centres of the smoothings ---
print("\nSmoothings of L_2^e # L_-2^e' (crossings in T^2; vertical zigzag centres in a, horizontal in b):")
for e, ep in ((0, 1), (1, 0), (0, 0), (1, 1)):
    pts = []
    for a8 in range(8):
        a = Fr(a8, 8)
        for b8 in range(8):
            b = Fr(b8, 8)
            if (2*a + b - Fr(e, 2)) % 1 == 0 and (-2*a + b - Fr(ep, 2)) % 1 == 0:
                pts.append((a, b))
    As = sorted(set(p[0] for p in pts)); Bs = sorted(set(p[1] for p in pts))
    vc = sorted(set(((As[i] + (As[(i+1) % len(As)] + (1 if i == len(As)-1 else 0)))/2) % 1 for i in range(len(As))))
    hc = sorted(set(((Bs[i] + (Bs[(i+1) % len(Bs)] + (1 if i == len(Bs)-1 else 0)))/2) % 1 for i in range(len(Bs))))
    print(f"  (eps,eps')=({e},{ep}) {'mixed' if e!=ep else 'same '}: crossings {[(str(a),str(b)) for a,b in pts]}")
    print(f"      vertical smoothing -> V_a, a in {[str(x) for x in vc]} ; horizontal -> H_b, b in {[str(x) for x in hc]}")

# --- 6. 4_1 sharp pair (census-final Sec. 6) ---
rho_bd, rho_x0 = Fr(1,5), Fr(4,5)
print("\n4_1: m2 = c(Y_2^w,(1,2,1)) - c(Y_-2^0,(1,1,2)) = (rho(1,2,1)+rho(1,1,2))/16 =", (rho_bd + rho_x0)/16,
      "; bd at (1/4,0) on L_-2^0?", ((-2*Fr(1,4)+0) % 1 == 0))
