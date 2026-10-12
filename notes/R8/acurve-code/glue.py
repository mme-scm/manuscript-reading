# Q0-sheet of the canonical curve near the complete structure, via SnapPy gluing equations.
# u = H(mu)/2, v = H(lambda)/2 (H = SnapPy holonomy log), v = g(u) on the sheet through u=0.
import snappy, warnings, numpy as np, cmath, math
warnings.filterwarnings('ignore')
class Sheet:
    def __init__(self, name):
        M = snappy.Manifold(name) if isinstance(name,str) else name
        self.M = M
        G = M.gluing_equations(); E = np.array([[float(G[i,j]) for j in range(G.shape[1])] for i in range(G.shape[0])])
        n = M.num_tetrahedra(); self.n = n
        self.A, self.B, self.C = E[:, :3*n:3], E[:, 1:3*n:3], E[:, 2:3*n:3]
        self.ne = E.shape[0]-2
        z0 = np.array([complex(s) for s in M.tetrahedra_shapes('rect')])
        self.w0 = np.log(z0)
        self.tau = complex(M.cusp_info()[0]['shape'])
    def logs(self, w):
        z = np.exp(w); L0 = w; L1 = -np.log(1-z); L2 = 1j*math.pi - L0 - L1
        return z, L0, L1, L2
    def F(self, w):
        z, L0, L1, L2 = self.logs(w)
        return self.A@L0 + self.B@L1 + self.C@L2
    def J(self, w):
        z = np.exp(w); dL0 = np.ones_like(z); dL1 = z/(1-z); dL2 = -dL0-dL1
        return self.A*dL0 + self.B*dL1 + self.C*dL2
    def solve(self, u, w):
        target = np.concatenate([2j*math.pi*np.ones(self.ne), [2*u]])
        rows = list(range(self.ne)) + [self.ne]
        for it in range(60):
            Fv = self.F(w)[rows] - target
            Jm = self.J(w)[rows]
            dw = np.linalg.lstsq(Jm, -Fv, rcond=None)[0]
            w = w + dw
            if np.max(np.abs(dw)) < 1e-14: break
        res = np.max(np.abs(self.F(w)[rows]-target))
        return w, res
    def v_of(self, w):
        return self.F(w)[self.ne+1]/2
    def path(self, us, w=None):
        w = self.w0.copy() if w is None else w
        out=[]
        for u in us:
            try:
                with np.errstate(all='ignore'):
                    w2, res = self.solve(u, w)
            except Exception:
                break
            if not np.isfinite(res) or res > 1e-8: break
            z = np.exp(w2)
            if np.max(np.abs(w2 - w)) > 0.5: break
            w = w2
            Jm = self.J(w)[list(range(self.ne))+[self.ne]]
            sv = np.linalg.svd(Jm, compute_uv=False)
            out.append((u, self.v_of(w), res, sv[-1]/sv[0], w.copy()))
        return out
