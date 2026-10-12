# Ren-type PURELY cosmetic pair on o10_150704 (4 cusps): phi orientation-preserving, (0 2)(1 3), phi^2|T0 of order 3.
import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/r8/code8')
from cone import *; from spin import *
import numpy as np
N=snappy.OrientableCuspedCensus(num_cusps=4)['o10_150704'] if False else snappy.Manifold('o10_150704')
print('N',N.num_cusps(),N.volume(),'cs',N.chern_simons(),'H1',N.homology(),'sym',N.symmetry_group())
isos=N.is_isometric_to(N,return_isometries=True)
def mat(m): return np.array([[int(m[0,0]),int(m[0,1])],[int(m[1,0]),int(m[1,1])]])
phi=None
for iso in isos:
    ci=iso.cusp_images(); cm=[mat(m) for m in iso.cusp_maps()]
    if round(np.linalg.det(cm[0]))==1 and list(ci)==[2,3,0,1]:
        sq=cm[2]@cm[0]
        if int(np.trace(sq)) in (-1,0,1): phi=(ci,cm); break
ci,cm=phi
print('phi cusp images',ci,'maps',[c.tolist() for c in cm],'phi^2|T0=',(cm[2]@cm[0]).tolist())
P,res=cusp_types_all(N); types=sorted(realizable(P,res))
print('N realizable cusp types (4-tuples):',len(types)); [print('  ',t) for t in types]
json.dump if False else None
from fractions import Fraction as Fr
from math import gcd
A=cm[0]; A2=cm[2]@cm[0]
def ext(P,sl): return ((sl[0]*P[0]+sl[1]*P[1])-0.5)%1==0
cands=[]
for p in range(-5,6):
    for q in range(0,6):
        if gcd(p,q)!=1 or (q==0 and p!=1): continue
        s=(p,q); As=tuple(int(x) for x in A@np.array(s)); A2s=tuple(int(x) for x in A2@np.array(s))
        okT=[t for t in types if ext(t[0],s) and ext(t[2],As)]
        if not okT: continue
        M=N.copy(); M.dehn_fill([(0,0),(0,0),As,(0,0)])
        X1=M.copy(); X1.dehn_fill([s,(0,0),As,(0,0)]); X2=M.copy(); X2.dehn_fill([A2s,(0,0),As,(0,0)])
        st=[Z.solution_type()[:12] for Z in (M,X1,X2)]
        if all(x.startswith('all tetrahed') for x in st):
            cands.append((s,As,A2s,float(X1.volume()),float(X2.volume()),len(okT)))
for c in cands: print(c)
