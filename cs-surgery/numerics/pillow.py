"""Common helpers: SU(2) matrices, simultaneous diagonalisation of (mu, lambda),
continuous lifts, and the Kirk-Klassen surgery formula.

Normalisation (Kirk-Klassen, Math. Ann. 287 (1990) Thm 4.2, as quoted verbatim in
Andersen-Hansen arXiv:math/0506456 Thm 6 and eq. (5.67)):
  g rho(mu) g^-1 = diag(e^{2 pi i a}, e^{-2 pi i a}),  g rho(lambda) g^-1 = diag(e^{2 pi i b}, ...)
  For a knot K in closed M with meridian mu, and a path rho_t with rho_0(mu)=rho_1(mu)=1,
      CS(rho_1) - CS(rho_0) = -2 int_0^1 b(t) a'(t) dt  (mod Z).
  Surgery corollary (A-H (5.67)): p/q surgery, c,d with p d - q c = 1, path from the trivial
  rep with continuous lift (a,b), a(0)=b(0)=0:
      CS = -2 int b da - c p a1^2 - d q b1^2 - 2 c q a1 b1   (mod Z)
  [independent of c,d and of the lift, given the continuous lift along the path].
"""
import numpy as np

I2 = np.eye(2, dtype=complex)


def quat(q0, q1, q2, q3):
    """unit quaternion q0+q1 i+q2 j+q3 k -> SU(2) matrix"""
    return np.array([[q0 + 1j * q1, q2 + 1j * q3], [-q2 + 1j * q3, q0 - 1j * q1]], dtype=complex)


def inv(m):
    return np.linalg.inv(m)


def word(gens, w):
    """gens: dict letter->matrix; w: string like 'xYxy' (capital = inverse)"""
    m = I2.copy()
    for ch in w:
        g = gens[ch.lower()]
        m = m @ (g if ch.islower() else inv(g))
    return m


def ab_from(mu, lam):
    """Return (a, b) with a in [0,1/2], b in (-1/2,1/2]: a,b from common eigenvector of mu
    with eigenvalue e^{2 pi i a}, a in [0,1/2]."""
    w, V = np.linalg.eig(mu)
    k = np.argmax(np.angle(w))  # eigenvalue with arg in [0, pi]
    v = V[:, k]
    a = np.angle(w[k]) / (2 * np.pi)
    lv = lam @ v
    beta = np.vdot(v, lv) / np.vdot(v, v)
    b = np.angle(beta) / (2 * np.pi)
    # residual check: v is eigenvector of lam
    res = np.linalg.norm(lv - beta * v)
    return a, b, res


def unwrap(b):
    return np.unwrap(2 * np.pi * np.asarray(b)) / (2 * np.pi)


def cumtrapz(y, x):
    out = np.zeros_like(x)
    out[1:] = np.cumsum(0.5 * (y[1:] + y[:-1]) * np.diff(x))
    return out


def cd_for(p, q):
    """integers c,d with p d - q c = 1"""
    def egcd(x, y):
        if y == 0:
            return (x, 1, 0)
        g, s, t = egcd(y, x % y)
        return (g, t, s - (x // y) * t)
    g, s, t = egcd(p, -q)  # p s - q t = g = +-1
    d, c = s * g, t * g
    assert p * d - q * c == 1
    return c, d


def kk_surgery_cs(F, a1, b1, p, q):
    """A-H (5.67). F = -2 int b da from the trivial rep along a continuous lift ending at (a1,b1)."""
    c, d = cd_for(p, q)
    return F - c * p * a1 ** 2 - d * q * b1 ** 2 - 2 * c * q * a1 * b1


def dist_mod1(x, y):
    d = (x - y) % 1.0
    return min(d, 1 - d)


def rat(x, den_max=5000):
    """best rational approx of x mod 1, and the error"""
    from fractions import Fraction
    fr = Fraction(x % 1.0).limit_denominator(den_max) % 1
    return fr, dist_mod1(float(fr), x)
