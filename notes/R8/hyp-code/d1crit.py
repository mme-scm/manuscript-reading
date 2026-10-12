import snappy, warnings, math, json
from multiprocessing import Pool
warnings.filterwarnings('ignore')
from survey import path
def job(nm):
    M=snappy.HTLinkExteriors[nm]
    t=complex(M.cusp_info()[0]['shape']); c0=float(M.chern_simons()); V0=float(M.volume())
    out=[nm, 'Imtau=%.3f'%t.imag, 'VolE=%.4f'%V0]
    I={}
    for N in (2,-2):
        X=M.copy(); X.dehn_fill((N,1))
        Ii,IV,mt,jump,worst=path(M,N,120)
        dcs=float(X.chern_simons())-c0; r=(dcs-Ii)*2; mod=abs(r-round(r))
        I[N]=Ii
        out.append('N=%+d: Vol=%.4f(%s) supTau=%.3f jump=%.3f modchk=%.1e worst=%s'%(N,float(X.volume()),X.solution_type()[:12],mt,jump,mod,worst[:12]))
    out.append('Delta=%.4f'%(I[2]-I[-2]))
    return out
names=['K11n42','K12n313','K12n430','K13n71','K13n1019','K13n1496','K13n1756','K13n1757','K13n4591']
with Pool(4) as p:
    for o in p.map(job,names): print(*o,sep='\n   ')
