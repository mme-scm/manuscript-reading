from glue import *
import sys
def potential(S, uend, n=400):
    us = [uend*k/n for k in range(n+1)]
    out = S.path(us[1:])
    vs = [0j] + [o[1] for o in out]
    # Simpson for G = int_0^uend v du along straight segment
    h = uend/n
    G = h/3*(vs[0] + vs[-1] + 4*sum(vs[1:-1:2]) + 2*sum(vs[2:-1:2]))
    minsv = min(o[3] for o in out); maxres = max(o[2] for o in out)
    return G, vs[-1], minsv, maxres, out[-1][4]
def FN(N, u, G): return 1j*math.pi*u - N*u*u/2 - G
if __name__ == '__main__':
    name = sys.argv[1] if len(sys.argv)>1 else 'K11n42'
    S = Sheet(name); M = S.M
    V0, c0 = float(M.volume()), float(M.chern_simons())
    res = {}
    for N in (2,-2):
        X = M.copy(); X.dehn_fill((N,1))
        uN = complex(X.cusp_info()[0]['holonomies'][0])/2
        G, vN, minsv, maxres, w = potential(S, uN)
        F = FN(N, uN, G)
        dV, dC = float(X.volume())-V0, float(X.chern_simons())-c0
        res[N] = F
        print(N, 'u_N=%s'%uN, 'check N u+v-i pi =', abs(N*uN+vN-1j*math.pi), 'minsv=%.2e'%minsv,
              '\n   -2ImF=%.6f dVol=%.6f | ReF/pi^2=%.6f dCS_snappy=%.6f  (diff mod 1/2: %.2e)'%(-2*F.imag, dV, F.real/math.pi**2, dC,
              ((F.real/math.pi**2 - dC + 0.25) % 0.5) - 0.25))
    print('Delta_K (path-free, straight segments) = Re(F_2 - F_-2)/pi^2 =', (res[2]-res[-2]).real/math.pi**2)
    print('Z_K complex =', (res[2]-res[-2])/math.pi**2)
