"""Spin^c Dirac eta invariants of S^3/Z_p (Z_p in SU(2)_L, round metric) by zeta regularisation.
Dirac on S^3: eigenvalue +(n+3/2) on V_{n+1}(x)V_n, -(n+3/2) on V_n(x)V_{n+1}; Gamma acts on the left factor,
twisted by a character omega^k (the choice of lift = spin^c structure).  f(n) = signed multiplicity is a
quasi-polynomial of degree 2 in n with period 2p; on each residue class fit a quadratic in x = n+3/2 and use
Hurwitz zeta: sum_{m>=0} (P m + a P)^{j-s} = P^{j-s} zeta(s-j, a)."""
from mpmath import mp, zeta, mpf, exp, pi, nint, matrix, lu_solve
mp.dps = 30
def inv_dim(a, p, k):
    z = exp(2j*pi/p); om = exp(2j*pi*k/p)
    return sum(1 for j in range(a+1) if abs(z**(a-2*j)*om-1) < 1e-12)
def f(n, p, k):
    return inv_dim(n+1, p, k)*(n+1) - inv_dim(n, p, k)*(n+2)
def eta(p, k):
    P = 2*p; tot = mpf(0)
    for r in range(P):
        xs = [mpf(r + P*m) + mpf(3)/2 for m in range(3)]
        ys = [f(r + P*m, p, k) for m in range(3)]
        A = matrix([[1, x, x*x] for x in xs]); c = lu_solve(A, matrix(ys))
        a = (mpf(r) + mpf(3)/2)/P
        tot += c[0]*zeta(0, a) + c[1]*P*zeta(-1, a) + c[2]*P**2*zeta(-2, a)
    return tot
if __name__ == '__main__':
    for p in [1, 2, 3, 4]:
        print('p=%d' % p, ['%s' % (nint(eta(p, k)*96)/96) for k in range(p)])
