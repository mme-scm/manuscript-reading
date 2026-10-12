import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/r8/code8')
from cone import *; from spin import *
import numpy as np
N=snappy.Manifold('o10_150704')
def mat(m): return np.array([[int(m[0,0]),int(m[0,1])],[int(m[1,0]),int(m[1,1])]])
def norm(v):
    p,q=int(v[0]),int(v[1])
    return (p,q) if (q>0 or (q==0 and p>0)) else (-p,-q)
for s,As,A2s in [((3,4),(-7,3),(4,-7)),((2,1),(-3,2),(1,-3)),((3,5),(-8,3),(5,-8))]:
    M=N.copy(); M.dehn_fill([(0,0),(0,0),As,(0,0)])
    Mf=M.filled_triangulation() if False else None
    # symmetries of M (3 unfilled cusps): use the filled manifold's isometries
    try:
        isos=M.is_isometric_to(M,return_isometries=True)
        found=[]
        for iso in isos:
            ci=iso.cusp_images(); cm=[mat(m) for m in iso.cusp_maps()]
            if ci[0]==0 and norm(cm[0]@np.array(s))==norm(np.array(A2s)): found.append((list(ci),round(np.linalg.det(cm[0]))))
        print(s,'M sym group order',len(isos),'symmetries of M sending s->phi^2 s on T0:',found)
    except Exception as e:
        print(s,'iso err',e)
