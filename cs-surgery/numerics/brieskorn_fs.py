"""Ground truth: Fintushel-Stern CS values of irreducible flat SU(2) connections on
Sigma(a1,a2,a3) (oriented as the link of the singularity, = boundary of the negative
definite resolution).

Convention (FS 1990, as recorded e.g. in Anvari arXiv:1401.1039 Table 1, and
Kim et al. arXiv:1701.03528 eq. (5.13)):
    pi_1 = <x1,x2,x3,h | h central, x_j^{a_j} h^{b_j} = 1, x1 x2 x3 = 1>,  sum_j b_j P/a_j = 1,
    P = a1 a2 a3, alpha(x_j) ~ exp(pi i l_j / a_j), 0 < l_j < a_j,
    CS_FS(alpha) = - e^2 / (4P) mod 1,  e = sum_j l_j P / a_j.
Sanity check against Anvari's table for Sigma(2,3,5): rotation numbers (1,2,2), (1,2,4)
with -CS = 49/120, 1/120.

Enumeration: alpha(h) = eps in {+1,-1}; alpha(x_j)^{a_j} = (-1)^{l_j} must equal eps^{-b_j};
an irreducible SU(2) triple with product 1 and rotation angles th_j = pi l_j/a_j exists
(uniquely up to conjugacy) iff |th1-th2| < th3 < min(th1+th2, 2pi-th1-th2).
"""
from fractions import Fraction as Fr
from itertools import product
import math


def seifert_b(a):
    a1, a2, a3 = a
    P = a1 * a2 * a3
    for b1, b2, b3 in product(range(-12, 13), repeat=3):
        if b1 * P // a1 + b2 * P // a2 + b3 * P // a3 == 1:
            return (b1, b2, b3)
    raise ValueError


def fs_reps(a):
    a1, a2, a3 = a
    P = a1 * a2 * a3
    b = seifert_b(a)
    out = []
    for eps in (1, -1):
        for l in product(*[range(1, aj) for aj in a]):
            ok = all((-1) ** lj == eps ** (bj % 2) for lj, bj in zip(l, b))
            if not ok:
                continue
            th = [math.pi * lj / aj for lj, aj in zip(l, a)]
            if abs(th[0] - th[1]) < th[2] - 1e-12 and th[2] < min(th[0] + th[1], 2 * math.pi - th[0] - th[1]) - 1e-12:
                e = sum(lj * P // aj for lj, aj in zip(l, a))
                cs = (-Fr(e * e, 4 * P)) % 1
                out.append((l, eps, e, cs))
    return out


def fs_values(a):
    return sorted(r[3] for r in fs_reps(a))


if __name__ == "__main__":
    for a in [(2, 3, 5), (2, 3, 7), (2, 3, 11), (2, 3, 13), (2, 3, 17), (2, 3, 19)]:
        reps = fs_reps(a)
        print(f"Sigma{a}: b={seifert_b(a)}  #irreps={len(reps)}")
        for l, eps, e, cs in reps:
            print(f"   l={l} h->{eps:+d} e={e:4d}  CS_FS = {cs} (= -{(-cs) % 1} mod 1)   ~ {float(cs):.6f}")
