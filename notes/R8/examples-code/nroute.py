import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/r8/code8')
from cone import *; from spin import *
E=snappy.Manifold('o9_39009'); E.chern_simons()
Y2=E.copy(); Y2.dehn_fill((-3,2))
N=Y2.drill(0)   # cusp0 = o9 cusp filled (-3,2), cusp1 = gamma
print('N cusps',N.num_cusps(), N.cusp_info('filling'))
N.dehn_fill([(0,0),(0,0)])
print('N complete: vol',N.volume(), 'sol',N.solution_type(), 'H1',N.homology())
try: cN=float(N.chern_simons()); print('cs(N)',cN)
except Exception as e: print('csN err',e); cN=None
# identify: N(inf,(1,0)) should be E ; N((-3,2),inf) should be -E
A=N.copy(); A.dehn_fill([(0,0),(1,0)]); B=N.copy(); B.dehn_fill([(-3,2),(0,0)])
print('N(inf,(1,0)) iso E?',A.is_isometric_to(E), A.volume(), 'N((-3,2),inf) iso E?', B.is_isometric_to(E), B.volume())
for X in (A,B):
    try: print(' cs',X.chern_simons())
    except Exception as e: print(' cs err',e)
G=N.symmetry_group()
print('N symmetry group',G, 'amphichiral',G.is_amphicheiral())
for iso in G.isometries():
    print(iso.cusp_images(), [m.tolist() if hasattr(m,'tolist') else m for m in iso.cusp_maps()], 'orientation?')
