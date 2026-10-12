# Rotation identity: Delta_K = (1/2pi^2) Re int_{-2}^{2} u_t^2 dt,  u_t: t u + v = i pi on the geometric sheet
from glue import *
import sys
def solve_line(S, t, s, w):
    # edges = 2 pi i ; t*H_mu + H_lam = s*2 pi i
    rows = list(range(S.ne))
    for it in range(80):
        Fv = S.F(w); Jm = S.J(w)
        E = np.concatenate([Fv[rows]-2j*math.pi, [t*Fv[S.ne]+Fv[S.ne+1]-2j*math.pi*s]])
        JJ = np.vstack([Jm[rows], t*Jm[S.ne]+Jm[S.ne+1]])
        dw = np.linalg.lstsq(JJ, -E, rcond=None)[0]; w = w+dw
        if np.max(np.abs(dw))<1e-14: break
    return w, np.max(np.abs(E))
def run(name, nt=400, ns=200):
    M = snappy.HTLinkExteriors[name] if name.startswith('K') else snappy.Manifold(name)
    S = Sheet(M); w = S.w0.copy()
    for k in range(1,ns+1):            # cone path for t=2 (to get onto P_2)
        w, r = solve_line(S, 2.0, k/ns, w)
    ts = [2-4*j/nt for j in range(nt+1)]; us=[]; worst=0
    for t in ts:
        w, r = solve_line(S, t, 1.0, w); worst=max(worst,r)
        us.append(S.F(w)[S.ne]/2)
    us=np.array(us); h=4/nt
    f = us**2
    I = h/3*(f[0]+f[-1]+4*f[1:-1:2].sum()+2*f[2:-1:2].sum())   # int from t=2 down to -2 with positive h => int_{-2}^{2}
    X=M.copy(); X.dehn_fill((-2,1)); um2=complex(X.cusp_info()[0]['holonomies'][0])/2
    return dict(name=name, Delta=(I.real)/(2*math.pi**2), Zc=I/(2*math.pi**2), maxu=np.max(np.abs(us)), end_err=abs(us[-1]-um2), res=worst,
                u0=us[nt//2])
if __name__=='__main__':
    for nm in sys.argv[1:]:
        try:
            d=run(nm); print(d['name'], 'Delta_rot=%.5f'%d['Delta'], 'max|u_t|=%.3f (crit pi/2=1.571)'%d['maxu'], 'bound 2max^2/pi^2=%.3f'%(2*d['maxu']**2/math.pi**2), 'end_err=%.1e res=%.1e'%(d['end_err'],d['res']), 'u_0=%s'%np.round(d['u0'],3))
        except Exception as e: print(nm,'ERR',e)
