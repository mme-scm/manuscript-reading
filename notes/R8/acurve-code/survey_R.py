from series import *
from pot import potential, FN
import sys
def run(name, r=None):
    M = snappy.HTLinkExteriors[name] if name[0]=='K' and 'n' in name else snappy.Manifold(name)
    S = Sheet(M)
    us = {}
    for N in (2,-2):
        X = M.copy(); X.dehn_fill((N,1)); us[N] = complex(X.cusp_info()[0]['holonomies'][0])/2
    umax = max(abs(us[2]),abs(us[-2]))
    r = r or 0.85*umax
    c, mono = coeffs(S, r, m=512)
    if c is None: return name, 'circle failed'
    ks = [k for k in range(31,61,2)]
    Rest = np.median([abs(c[k]/c[k+2])**0.5 for k in ks])
    # series value of Delta
    def Gser(u): return sum(c[k]*u**(k+1)/(k+1) for k in range(1,len(c)))
    D_ser = -((FN(2,us[2],Gser(us[2])) - FN(-2,us[-2],Gser(us[-2]))).real)/math.pi**2
    D_int = []
    for N in (2,-2):
        G,vN,minsv,maxres,w = potential(S, us[N], n=300); D_int.append(FN(N,us[N],G))
    D_path = -((D_int[0]-D_int[1]).real)/math.pi**2
    return name, 'tau=%s'%np.round(S.tau,3), '|u_2|=%.3f |u_-2|=%.3f'%(abs(us[2]),abs(us[-2])), 'R~%.3f'%Rest, 'ratio=%.2f'%(umax/Rest), 'Delta(series)=%.5f Delta(segment)=%.5f'%(D_ser, D_path)
if __name__=='__main__':
    for nm in sys.argv[1:]:
        try: print(*run(nm))
        except Exception as e: print(nm, 'ERR', e)
