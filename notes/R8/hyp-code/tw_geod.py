import snappy, warnings, math, cmath, sys
warnings.filterwarnings('ignore')
from tw_profile import getM, profile
from tw_frame import fix_frame
def red(z):  # reduce imaginary part to (-pi,pi]
    return complex(abs(z.real), (z.imag+math.pi)%(2*math.pi)-math.pi) if z.real>=0 else complex(-z.real, (-z.imag+math.pi)%(2*math.pi)-math.pi)
for nm in sys.argv[1].split(','):
    M=getM(nm)
    if '_' in nm: fix_frame(M)
    cores={}
    for N in (2,-2):
        us,_=profile(M,N,200); cores[N]=us[-1]
    out=[nm]
    for N in (2,-2):
        X=M.copy(); X.dehn_fill((N,1))
        try: spec=X.length_spectrum(2.5)
        except Exception: X.randomize(); spec=X.length_spectrum(2.5)
        Ls=[complex(g['length']) for g in spec]
        core=red(cores[N]); other=red(cores[-N])
        dcore=min(abs(red(L)-core) for L in Ls) if Ls else None
        # does Y_N contain a geodesic with the complex length of the other core (either orientation)?
        doth=min(min(abs(red(L)-other),abs(red(L)-complex(other.real,-other.imag))) for L in Ls)
        rank=sorted(set(round(L.real,6) for L in Ls)).index(round(min(Ls,key=lambda L:abs(red(L)-core)).real,6))
        out.append('Y_%+d: core L=%.4f%+.4fi (match %.1e), rank of core among lengths=%d, shortest 4: %s; nearest to other core %.3f'%(
            N,core.real,core.imag,dcore,rank,[ '%.3f%+.3fi'%(red(L).real,red(L).imag) for L in Ls[:4]],doth))
    print(*out,sep='\n  ')
