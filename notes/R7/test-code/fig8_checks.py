"""4_1 numerics on the Riley curve (gap16/pillowcase-code/fig8_curve.npy; branch 1 = b from -1/2 to 1/2,
branch 2 = (a, 1-b) reversed).  (i) levels from the pillowcase formula with one constant fitted on A0;
(ii) the a-triangle of triangle (I) (x in A0 -> p_A=(1/4,-1/2) -> y+ in T) and its area vs the level drop;
(iii) the lobe bigon between the two traceless generators y-, y+ at the double point (1/4,0)."""
import os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
A, B = np.load(os.path.join(HERE, '..', '..', 'gap16', 'pillowcase-code', 'fig8_curve.npy'))
A = np.concatenate([[1/6], A, [1/3]]); B = np.concatenate([[-0.5], B, [0.5]])
n = len(A)
alpha = np.concatenate([A, A[::-1][1:]]); beta = np.concatenate([B, (1 - B)[::-1][1:]])
Phi = np.concatenate([[0], np.cumsum(2 * (0.5 * (alpha[1:] + alpha[:-1]) - 0.25) * (beta[1:] - beta[:-1]))])
f = 2 * A + B
i0 = [i for i in range(n - 1) if f[i] * f[i + 1] < 0][0]
s = -f[i0] / (f[i0 + 1] - f[i0]); x = (A[i0] + s * (A[i0 + 1] - A[i0]), B[i0] + s * (B[i0 + 1] - B[i0]))
iy = int(np.argmin(abs(A - .25)))
off = 19 / 80 - 2 * (x[0] - .25) ** 2 - 1 / 16 - Phi[i0]
print('(i) A0 point x=(%.5f,%.5f), c=19/80 fixes Phi(x)=%.6f' % (x[0], x[1], Phi[i0] + off))
for nm, i in (('branch+ (slope +2sqrt5)', iy), ('branch- (slope -2sqrt5)', 2 * n - 2 - iy)):
    P = Phi[i] + off
    print('    %s at (1/4,0): Phi*80=%.4f  c(A1)*80=%.4f  c(B1)*80=%.4f  c^tl*80=%.4f' % (nm, P * 80, (P + 1/16) * 80, (P - 1/16) * 80,
          (P + (1/16 if 'slope +' in nm else -1/16)) * 80))
def oarea(pts):
    P = np.array(pts); xs, ys = P[:, 0], P[:, 1]
    return np.sum(xs * np.roll(ys, -1) - np.roll(xs, -1) * ys)   # = omega-area (2 x Euclidean)
pts = [x, (0.25, -0.5), (0.25, 0.0)] + [(A[i], B[i]) for i in range(iy - 1, i0, -1)]
print('(ii) a-triangle x -> p_A -> y+ : omega-area %.10f (ccw>0); level drop 19/80 - 1/5 = %.10f' % (oarea(pts), 19/80 - 1/5))
lobe = [(0.25, 0.0), (0.25, 1.0)] + [(A[i], 1 - B[i]) for i in range(iy + 1, n)] + [(A[i], B[i]) for i in range(n - 2, iy, -1)]
print('(iii) right lobe (V up from y+ to y-, back along Gamma): signed omega-area %.6f' % oarea(lobe))
print('     => ccw bigon y- -(V)-> y+ -(Gamma)-> y- of area %.6f ; a differential d(y-)=y+ needs area 1/8 + c(y-) - c(y+) = %.6f' % (-oarea(lobe), 1/8 + 7/40 - 1/5))
