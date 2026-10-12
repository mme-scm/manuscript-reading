"""r7 test: chain-level pillowcase model of the mixed triangles (I), (II) at +-2.

Exact (rational) geometry in the universal cover R^2 of the pillowcase P = R^2 / G,
G = Z^2 x| {+-1}.  omega = 2 da^db.  Gamma = G-orbit of straight base arcs (torus knots).

Lines (families of parallel lines in R^2, all G-invariant):
  L_N^eps = {N a + b in eps/2 + Z},   V = {2a in 1/2 + Z} (a = 1/4 mod 1/2),   Linf = {a in Z}.

Model rules (stated in test.md):
  M1  generators = (Gamma cap L)/G, represented on the base arcs.
  M2  mu^d(x, p_1..p_{d-1}) -> z counts convex Euclidean polygons in R^2 with vertices
      x, p_1, .., p_{d-1}, z in COUNTER-CLOCKWISE order, edge x->p_1 on the M_0 line through x,
      p_i -> p_{i+1} on an M_i line, p_{d-1} -> z on the M_{d-1} line through z, and z -> x along
      the SAME lifted arc of Gamma (one component; the arc's endpoints on b in Z are stops).
      Polygons are counted modulo G by fixing the base lift of x.
  M3  corners p_i must project to the prescribed points of P.
  M4  corner rule (variants): 'free' (orbifold / equivariant count), 'int' (no corner of P in
      the open polygon), 'closed' (no corner of P anywhere except at prescribed corner vertices).
"""
from fractions import Fraction as F
import itertools, math

HALF = F(1, 2)

class Fam:
    def __init__(self, name, n, c):
        self.name, self.n, self.c = name, (F(n[0]), F(n[1])), F(c) % 1
    def val(self, u):
        return self.n[0] * u[0] + self.n[1] * u[1]
    def contains(self, u):
        return (self.val(u) - self.c) % 1 == 0
    def dirv(self):
        return (self.n[1], -self.n[0])

def L(N, eps):
    return Fam('L%d^%s' % (N, 'w' if eps else '0'), (N, 1), F(eps, 2))

V = Fam('V', (2, 0), HALF)
LINF = Fam('Linf', (1, 0), 0)

def meet(f1, k1, f2, k2):
    (a1, b1), (a2, b2) = f1.n, f2.n
    det = a1 * b2 - a2 * b1
    if det == 0:
        return None
    return ((k1 * b2 - k2 * b1) / det, (a1 * k2 - a2 * k1) / det)

def canon(u):
    """canonical representative of the G-orbit of u: a in [0,1/2], b in [0,1) (edges folded)."""
    a, b = u[0] % 1, u[1] % 1
    if a > HALF:
        a, b = 1 - a, (-b) % 1
    if a == 0 or a == HALF:
        b = min(b, (-b) % 1)
    return (a, b)

def cross(o, p, q):
    return (p[0] - o[0]) * (q[1] - o[1]) - (p[1] - o[1]) * (q[0] - o[0])

def area(poly):
    s = F(0)
    for i in range(len(poly)):
        x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % len(poly)]
        s += x1 * y2 - x2 * y1
    return s  # = 2 * Euclidean signed area = omega-area (omega = 2 da db)

def convex_ccw(poly):
    n = len(poly)
    for i in range(n):
        if cross(poly[i - 1], poly[i], poly[(i + 1) % n]) <= 0:
            return False
    return True

def corner_points_in(poly):
    """half-lattice points (corners of P) strictly inside, and on the boundary (not vertices)."""
    xs = [p[0] for p in poly]; ys = [p[1] for p in poly]
    inside, onb = [], []
    for i2 in range(math.floor(2 * min(xs)) - 1, math.ceil(2 * max(xs)) + 2):
        for j2 in range(math.floor(2 * min(ys)) - 1, math.ceil(2 * max(ys)) + 2):
            u = (F(i2, 2), F(j2, 2))
            if u in poly:
                continue
            cs = [cross(poly[k], poly[(k + 1) % len(poly)], u) for k in range(len(poly))]
            if all(c > 0 for c in cs):
                inside.append(u)
            elif all(c >= 0 for c in cs):
                onb.append(u)
    return inside, onb

# ---------------------------------------------------------------- knots
class Arc:
    def __init__(self, name, P0, P1):
        self.name, self.P0, self.P1 = name, (F(P0[0]), F(P0[1])), (F(P1[0]), F(P1[1]))
        self.d = (self.P1[0] - self.P0[0], self.P1[1] - self.P0[1])
    def param(self, u):
        d = self.d
        if (u[0] - self.P0[0]) * d[1] - (u[1] - self.P0[1]) * d[0] != 0:
            return None
        return ((u[0] - self.P0[0]) * d[0] + (u[1] - self.P0[1]) * d[1]) / (d[0] ** 2 + d[1] ** 2)
    def meets(self, fam):
        """points of (open) arc on lines of fam (exact)."""
        nd = fam.n[0] * self.d[0] + fam.n[1] * self.d[1]
        v0 = fam.val(self.P0)
        out = []
        if nd == 0:
            return out
        lo, hi = sorted([v0, v0 + nd])
        k = math.floor(lo - fam.c) - 1
        while fam.c + k <= hi + 1:
            t = (fam.c + k - v0) / nd
            if 0 < t < 1:
                out.append((t, (self.P0[0] + t * self.d[0], self.P0[1] + t * self.d[1])))
            k += 1
        return sorted(out)

class Gen:
    def __init__(self, cx, arc, t, u, level, label):
        self.cx, self.arc, self.t, self.u, self.level, self.label = cx, arc, t, u, level, label
    def __repr__(self):
        return '%s[%s]' % (self.cx, self.label)

# ---------------------------------------------------------------- polygon enumeration
def polygons(src, dst, fams, corners, rule='int', krange=8):
    """src: list of Gen on lines of fams[0]; dst: list of Gen on lines of fams[-1].
    fams: [M_0, ..., M_{d-1}]; corners: list of length d-1 of sets of canonical points
    (corner p_i in M_{i-1} cap M_i).  Returns list of dicts."""
    out = []
    d = len(fams)
    for x in src:
        k0 = fams[0].val(x.u)
        for z in dst:
            if z.arc is not x.arc or z.t == x.t:
                continue
            kl = fams[-1].val(z.u)
            # free line choices for intermediate fams M_1..M_{d-2}
            mids = []
            for i in range(1, d - 1):
                f = fams[i]
                # choose k near the values at x and z
                base = math.floor(f.val(x.u))
                mids.append([f.c + j for j in range(base - krange, base + krange + 1)])
            for ks in itertools.product(*mids):
                kk = [k0] + list(ks) + [kl]
                verts = [x.u]
                ok = True
                for i in range(1, d):
                    p = meet(fams[i - 1], kk[i - 1], fams[i], kk[i])
                    if p is None or canon(p) not in corners[i - 1]:
                        ok = False; break
                    verts.append(p)
                if not ok:
                    continue
                verts.append(z.u)
                if len(set(verts)) < len(verts):
                    continue
                if not convex_ccw(verts):
                    continue
                ins, onb = corner_points_in(verts)
                if rule == 'int' and ins:
                    continue
                if rule == 'closed' and (ins or onb):
                    continue
                out.append(dict(src=x, dst=z, verts=verts, area=area(verts), ins=ins, onb=onb,
                                corners=[canon(v) for v in verts[1:-1]]))
    return out

def matrix(polys):
    M = {}
    for p in polys:
        key = (p['src'], p['dst'])
        M[key] = M.get(key, 0) ^ 1
    return {k for k, v in M.items() if v}

# ---------------------------------------------------------------- F2 linear algebra on dict-sets
def compose(M2, M1, A, B, C):
    """M1: A->B, M2: B->C (sets of (src,dst)); returns set for M2 o M1."""
    out = {}
    for (x, y) in M1:
        for (y2, z) in M2:
            if y2 is y:
                out[(x, z)] = out.get((x, z), 0) ^ 1
    return {k for k, v in out.items() if v}

def add(*Ms):
    out = {}
    for M in Ms:
        for k in M:
            out[k] = out.get(k, 0) ^ 1
    return {k for k, v in out.items() if v}

def ident(A):
    return {(x, x) for x in A}

def apply(M, vec):
    """vec: set of gens (F2 vector)."""
    out = {}
    for (x, y) in M:
        if x in vec:
            out[y] = out.get(y, 0) ^ 1
    return {k for k, v in out.items() if v}

def rank(M, A, B):
    rows = []
    idx = {b: i for i, b in enumerate(B)}
    for x in A:
        r = 0
        for (s, t) in M:
            if s is x:
                r ^= 1 << idx[t]
        rows.append(r)
    rk = 0
    rows = [r for r in rows]
    for bit in range(len(B)):
        piv = next((i for i in range(rk, len(rows)) if rows[i] >> bit & 1), None)
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        for i in range(len(rows)):
            if i != rk and rows[i] >> bit & 1:
                rows[i] ^= rows[rk]
        rk += 1
    return rk

def kernel_min_level(M, A, B):
    """least level of a nonzero vector of ker M (A sorted by level, vector level = max)."""
    As = sorted(A, key=lambda g: g.level)
    for k in range(1, len(As) + 1):
        sub = As[:k]
        if rank({(x, y) for (x, y) in M if x in sub}, sub, B) < k:
            return As[k - 1].level
    return None
