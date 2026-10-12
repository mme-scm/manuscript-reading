"""Corrected twisted complexes of Y_{+-2}(T_{p,q}) and mirrors (user's rule), and the five drops.
zeta-normalisation (ell-1): f^w = CS^w - gr^w/8, CS^w(zeta)=0, gr^w = ind(. -> zeta).
Uniform level c = f^w + (1 - sigma)/8  (= (3+rho)/16 on irreducibles).
Correction for (Y_{+-2}(L), w): |sigma_L|/2 generators, CS^w = 0,
   sigma_L < 0: gr^w = -1,-3,...   sigma_L > 0: gr^w = 0,2,4,...
(For Y_{-2} this is the same rule, obtained from Y_{-2}(L) = -Y_2(mirror L).)"""
import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/gap16/triangle-code')
import tk
from fractions import Fraction as F
from math import gcd

def old_twisted(p, q, N):
    """positive T(p,q): list of (f^w, gr^w mod 8) for twisted irreducibles of Y_N."""
    sig = tk.sigma_torus(p, q)
    rz = 2 * sig
    out = []
    for g in tk.gens(p, q, N, twisted=True):
        r = -g['rho']                       # rho^m (float-derived rational; only used to round)
        csw = (g['CSD'] - F(N, 16)) % 1     # exact
        grf = float(8 * csw + (r - rz - 1) / 2)
        grw = round(grf)
        assert abs(grf - grw) < 1e-4, (p, q, N, grf)
        fw = csw - F(grw, 8)                # exact, from exact CS and integral grading
        out.append((fw, grw % 8))
    return out

def untwisted_c(p, q, N):
    out = []
    for g in tk.gens(p, q, N, twisted=False):
        grf = float(g['gr']); gr = round(grf)
        assert abs(grf - gr) < 1e-4, (p, q, N, grf)
        out.append(g['CSD'] - F(gr, 8))     # c = CS - gr/8, exact
    return out

def data(p, q, mirror):
    """returns sigma_L and, for N=+-2: untwisted levels (uniform c), old twisted (f, gr mod 8)."""
    sig = tk.sigma_torus(p, q)
    if not mirror:
        return sig, {N: (untwisted_c(p, q, N), old_twisted(p, q, N)) for N in (2, -2)}
    # Y_N(mK) = -Y_{-N}(K): c -> 3/8 - c ; f^w -> 1/8 - f^w ; gr^w -> -1 - gr^w
    d = {}
    for N in (2, -2):
        u = [F(3, 8) - c for c in untwisted_c(p, q, -N)]
        t = [(F(1, 8) - f, (-1 - g) % 8) for (f, g) in old_twisted(p, q, -N)]
        d[N] = (u, t)
    return -sig, d

CONV = 'b'   # 'a': user degree = gr^w = ind(. -> zeta);  'b': user degree = ind(zeta -> .) = -1 - gr^w
def new_gens(sig):
    n = abs(sig) // 2
    degs = [-(2 * j + 1) for j in range(n)] if sig < 0 else [2 * j for j in range(n)]
    out = []
    for d in degs:
        gr = d if CONV == 'a' else -1 - d
        out.append((F(-gr, 8), gr % 8))     # CS^w = 0  =>  f^w = -gr/8
    return out

def can_pair(old, new):
    (fo, go), (fn, gn) = old, new
    ok = False
    if (go - gn) % 8 == 1 and fn < fo + F(1, 8):  ok = True   # d(old) = new
    if (gn - go) % 8 == 1 and fo < fn + F(1, 8):  ok = True   # d(new) = old
    return ok

def max_matching(left, right, adj, forced_right=None, banned_right=None):
    """left = new gens (indices), right = old gens; returns size of max matching
    (optionally only using allowed rights)."""
    banned_right = banned_right or set()
    match_r = {}
    def try_(u, seen):
        for v in adj[u]:
            if v in banned_right or v in seen: continue
            seen.add(v)
            if v not in match_r or try_(match_r[v], seen):
                match_r[v] = u
                return True
        return False
    size = sum(1 for u in left if try_(u, set()))
    return size

def lam1_range(old, new, n_untw):
    """corrected twisted lambda (in f^w units) range over admissible cancellations."""
    tot = len(old) + len(new)
    ex = tot - n_untw
    if ex == 0:                      # deficit case: everything survives
        v = min(f for f, _ in old + new)
        return v, v, 'survive'
    assert ex == 2 * len(new), (len(old), len(new), n_untw)
    olds = sorted(range(len(old)), key=lambda i: old[i][0])
    adj = {j: [i for i in range(len(old)) if can_pair(old[i], new[j])] for j in range(len(new))}
    L = list(range(len(new)))
    if max_matching(L, olds, adj) < len(new):
        return None, None, 'NO perfect matching (parity/filtration inconsistent)'
    # min lambda: lowest old that can be left unmatched
    lo = None
    for i in olds:
        if max_matching(L, olds, adj, banned_right={i}) == len(new):
            lo = old[i][0]; break
    # max lambda: largest k such that the k lowest olds can all be matched (and new saturated)
    k_best = 0
    for k in range(1, len(new) + 1):
        S = olds[:k]
        adjS = {i: [j for j in L if i in adj[j]] for i in S}
        # matching saturating S (S on the left)
        match = {}
        def tr(u, seen):
            for v in adjS[u]:
                if v in seen: continue
                seen.add(v)
                if v not in match or tr(match[v], seen):
                    match[v] = u; return True
            return False
        if all(tr(u, set()) for u in S): k_best = k
        else: break
    hi = old[olds[k_best]][0]
    return lo, hi, f'cancel {len(new)}'

def drops(p, q, mirror):
    sig, d = data(p, q, mirror)
    shift = (1 - sig) / F(8)
    res = {}
    for N in (2, -2):
        u, t = d[N]
        lam0 = min(u)
        lam1_old = min(f for f, _ in t) + shift
        lo, hi, how = lam1_range(t, new_gens(sig), len(u))
        res[N] = dict(lam0=lam0, lam1_old=lam1_old,
                      lam1_lo=None if lo is None else lo + shift,
                      lam1_hi=None if hi is None else hi + shift, how=how,
                      par_old=sorted({g % 2 for _, g in t}), n=(len(u), len(t)))
    return sig, res

if __name__ == '__main__':
    PQ = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    for (p, q) in [(2, 3), (2, 5), (3, 4), (3, 5)]:
        for mir in (False, True):
            sig, r = drops(p, q, mir)
            print(f"T({p},{'-' if mir else ''}{q}) sigma={sig}")
            for N in (2, -2):
                x = r[N]
                print(f"   Y_{N:+d}: n(untw,tw)={x['n']} old-tw parity={x['par_old']} lam0={x['lam0']} lam1 old={x['lam1_old']} "
                      f"corrected=[{x['lam1_lo']}, {x['lam1_hi']}] ({x['how']})")
