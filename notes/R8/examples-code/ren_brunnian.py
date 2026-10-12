import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-manuscript-reading/2864ca38-4e2e-507e-a435-401b17fbea03/scratchpad/r8/code8')
from cone import *; from spin import *
import numpy as np, json
PD=[(94,60,95,59),(21,48,22,49),(80,58,81,57),(95,64,96,33),(86,18,87,17),(74,28,75,27),(28,76,29,75),(83,12,84,13),(85,26,86,27),(90,40,91,39),(88,8,89,7),(76,14,77,13),(63,32,64,1),(43,18,44,19),(73,14,74,15),(4,42,5,41),(8,88,9,87),(36,70,37,69),(15,72,16,73),(22,62,23,61),(33,96,34,65),(71,16,72,17),(42,4,43,3),(9,70,10,71),(11,82,12,83),(40,6,41,5),(67,54,68,55),(62,24,63,23),(2,52,3,51),(92,38,93,37),(10,78,11,77),(58,66,59,65),(81,34,82,35),(55,66,56,67),(56,80,57,79),(31,46,32,47),(93,52,94,53),(38,92,39,91),(29,84,30,85),(53,68,54,69),(19,50,20,51),(35,78,36,79),(45,30,46,31),(24,48,25,47),(44,26,45,25),(49,20,50,21),(1,60,2,61),(6,90,7,89)]
L=snappy.Link(PD); N=L.exterior()
print('N cusps',N.num_cusps(),'tets',N.num_tetrahedra(),'vol',N.volume(),'sol',N.solution_type(),'cs',N.chern_simons(),'H1',N.homology())
isos=N.is_isometric_to(N,return_isometries=True)
def mat(m): return np.array([[int(m[0,0]),int(m[0,1])],[int(m[1,0]),int(m[1,1])]])
for iso in isos:
    print(iso.cusp_images(),[mat(m).tolist() for m in iso.cusp_maps()])
from fractions import Fraction as Fr
q=int(sys.argv[1]) if len(sys.argv)>1 else 3
n=int(sys.argv[2]) if len(sys.argv)>2 else 80
N.chern_simons(); cN=float(N.chern_simons())
fills=[None,(1,-q),(1,q)]
M=N.copy(); M.dehn_fill([(0,0),(1,-q),(1,q)])
print('M sol',M.solution_type(),'vol',M.volume(),'H1',M.homology())
cM=float(M.chern_simons()); print('cs(M)',cM)
# N -> M twist (two cusps): fill T1 then T2
d1=path(N,1,(1,-q),n=n,fills=[None,None,None]); d2=path(N,2,(1,q),n=n,fills=[None,(1,-q),None])
print('N->M: J1=%.9f J2=%.9f, chk cs(M)-cs(N)-J1-J2 mod 1/2 = %.2e'%(d1['J'],d2['J'],mod(cM-cN-d1['J']-d2['J'],0.5)))
dp=path(N,0,(1,q),n=n,fills=fills); dm=path(N,0,(1,-q),n=n,fills=fills)
print('M->Y+: J=%.9f bad %d ; M->Y-: J=%.9f bad %d ; cs(Y+)=%.9f cs(Y-)=%.9f'%(dp['J'],dp['bad'],dm['J'],dm['bad'],dp['cs_fill'],dm['cs_fill']))
P,res=cusp_types_all(M); types=sorted(t[0] for t in realizable(P,res))
print('M cusp types',types)
def ext(P,sl): return abs(((sl[0]*P[0]+sl[1]*P[1])-0.5)%1)<1e-9
for sl,d in (((1,q),dp),((1,-q),dm)):
    print(sl,'ext types',[t for t in types if ext(t,sl)],'dual',d['dual'])
json.dump(dict(q=q,cN=cN,cM=cM,J1=d1['J'],J2=d2['J'],Jp=dp['J'],Jm=dm['J'],dualp=dp['dual'],dualm=dm['dual'],types=types,
               csp=dp['cs_fill'],csm=dm['cs_fill']),open('ren_brunnian_q%d.json'%q,'w'))
