import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/r8/code8')
from cone import *; from spin import *
import numpy as np
E=snappy.Manifold('o9_39009'); cE=float(E.chern_simons())
Y2=E.copy(); Y2.dehn_fill((-3,2)); N=Y2.drill(0); N.dehn_fill([(0,0),(0,0)]); cN=float(N.chern_simons())
n=200
# cusp types of N for SnapPy lift + H^1 restrictions
G=N.fundamental_group(); pc=G.peripheral_curves()
gens=G.generators(); chis=H1Z2(G)
P=[]
for c in range(2):
    m,l=pc[c][:2]; tm=complex(G.SL2C(m).trace()); tl=complex(G.SL2C(l).trace())
    P.append((0.5 if tm.real<0 else 0.0, 0.5 if tl.real<0 else 0.0))
res=[tuple(chi_eval(ch,w,gens) for c in range(2) for w in pc[c][:2]) for ch in chis]
print('SnapPy lift cusp types',P,'; restrictions (mu0,l0,mu1,l1) of H^1(N;Z2):',sorted(set(res)))
# Route A: fill cusp1 with (1,0) from complete N -> E ; check SnapPy validation
dA1=path(N,1,(1,0),n=n,fills=[None,None])
print('N->E (cusp1 (1,0)): J=%.9f dual %s  chk mod1/2 = %.2e'%(dA1['J'],dA1['dual'],mod(cE-cN-dA1['J'],0.5)))
dA2=path(N,0,(-3,2),n=n,fills=[None,(1,0)])
dA2b=path(N,0,(-1,3),n=n,fills=[None,(1,0)])
print('E->Y2 via N: J=%.9f ; E->Y1 via N: J=%.9f  (o9 direct: -0.314352500, 0.171634518)'%(dA2['J'],dA2b['J']))
# Route B: fill cusp0 with (-3,2) first -> -E, then cusp1 (1,0)
dB1=path(N,0,(-3,2),n=n,fills=[None,None])
dB2=path(N,1,(1,0),n=n,fills=[(-3,2),None])
print('N->-E: J=%.9f chk %.2e ; -E->Y2: J=%.9f'%(dB1['J'],mod(-cE-cN-dB1['J'],0.5),dB2['J']))
print('route A total J=%.9f route B total J=%.9f diff=%.2e'%(dA1['J']+dA2['J'],dB1['J']+dB2['J'],dA1['J']+dA2['J']-dB1['J']-dB2['J']))
# X1 via route fill cusp1 then cusp0 (-1,3)
print('X1 total J (A-route) = %.9f'%(dA1['J']+dA2b['J']))
print('cs(N)=%.9f cs(E)=%.9f'%(cN,cE))
