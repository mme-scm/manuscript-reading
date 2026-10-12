import snappy,warnings;warnings.filterwarnings('ignore')
import numpy as np
E=snappy.Manifold('o9_39009'); E.chern_simons()
Y2=E.copy(); Y2.dehn_fill((-3,2)); N=Y2.drill(0); N.dehn_fill([(0,0),(0,0)])
isos=N.is_isometric_to(N,return_isometries=True)
print('num isometries',len(isos))
def norm(s):
    p,q=int(round(s[0])),int(round(s[1]))
    if q<0 or (q==0 and p<0): p,q=-p,-q
    return (p,q)
X1={0:(-1,3),1:(1,0)}; X2={0:(-3,2),1:(1,0)}
for k,iso in enumerate(isos):
    ci=iso.cusp_images(); cm=[np.array([[int(m[0,0]),int(m[0,1])],[int(m[1,0]),int(m[1,1])]]) for m in iso.cusp_maps()]
    dets=[round(np.linalg.det(m)) for m in cm]
    img={}
    for c,s in X1.items():
        img[ci[c]]=norm(cm[c]@np.array(s))   # assume matrix acts on column (p,q)
    imgT={}
    for c,s in X1.items():
        imgT[ci[c]]=norm(cm[c].T@np.array(s))
    print(k,'cusp_images',ci,'dets',dets,'X1->',img,' (transpose conv:',imgT,')', 'match X2' if img=={c:norm(s) for c,s in X2.items()} else '', 'matchT' if imgT=={c:norm(s) for c,s in X2.items()} else '')
iso=isos[2]; cm=[np.array([[int(m[0,0]),int(m[0,1])],[int(m[1,0]),int(m[1,1])]]) for m in iso.cusp_maps()]
print('phi cusp maps', cm[0].tolist(), cm[1].tolist(), 'images',iso.cusp_images())
P=np.array([0.5,0.0])
print('pulled-back types: cusp0 <- M0^T P1 =', (cm[0].T@P)%1, ' cusp1 <- M1^T P0 =', (cm[1].T@P)%1)
print('M1@(0,1)=',cm[1]@np.array([0,1]),' M0@(0,-1)=',cm[0]@np.array([0,-1]))
