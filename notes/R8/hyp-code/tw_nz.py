import snappy, warnings, math, sys
warnings.filterwarnings('ignore')
from tw_profile import getM
from tw_frame import fix_frame
for nm in sys.argv[1].split(','):
    M=getM(nm)
    if '_' in nm and nm.startswith('K'): fix_frame(M)
    t=complex(M.cusp_info()[0]['shape']); out=[nm,'tau=%.3f%+.3fi'%(t.real,t.imag)]
    for N in (2,-2):
        X=M.copy(); rs=[]
        for a_frac in (0.05,0.1,0.25,0.5,0.75,1.0):
            X2=M.copy(); X2.dehn_fill((N/a_frac,1/a_frac)); h=X2.cusp_info()[0]['holonomies']; u,v=complex(h[0]),complex(h[1])
            rs.append((a_frac,abs(u),(v/u-t.conjugate())/u**2))
        out.append('N=%+d: '%N+' '.join('[a=%.2f|u|=%.2f c_eff=%.3f%+.3fi]'%(a,au,r.real,r.imag) for a,au,r in rs))
    print(*out,sep='\n  ')
