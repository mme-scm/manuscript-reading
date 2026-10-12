# General cone-path Schlafli integrator for one cusp of a (possibly multi-cusped) SnapPy manifold.
import snappy, warnings, math, cmath
warnings.filterwarnings('ignore')
PI=math.pi
def egcd(a,b):
    if b==0: return (a,1,0)
    g,x,y=egcd(b,a%b); return (g,y,x-(a//b)*y)
def dual(p,q):
    """positive dual (r,s) with p*s-q*r=1"""
    g,x,y=egcd(p,q)   # p*x+q*y=g=+-1
    # want p*s - q*r = 1 : s = x*g, r = -y*g  (since g=+-1, g*g=1)
    s=x*g; r=-y*g
    assert p*s-q*r==1,(p,q,r,s)
    return (r,s)
def path(M, cusp, slope, n=200, fills=None, dual_rs=None, check=True):
    """Cone path on `cusp` towards slope=(p,q), other cusps filled as in `fills` (list of slopes or None=complete).
    Returns dict with J (SnapPy-normalised twist along positive dual), eps, B-data, final cs."""
    p,q=slope; r,s = dual_rs if dual_rs else dual(p,q)
    nc=M.num_cusps()
    base=[(0,0)]*nc if fills is None else [f if f is not None else (0,0) for f in fills]
    Hl=[]; Hm=[]; bad=0; alphas=[]
    for k in range(1,n+1):
        t=k/n
        X=M.copy(); fl=list(base); fl[cusp]=(p/t,q/t)
        for i,f in enumerate(fl): X.dehn_fill(f,i)
        st=X.solution_type()
        if not st.startswith('all tetrahedra positively'): bad+=1
        hm,hl=X.cusp_info()[cusp]['holonomies']
        hm=complex(hm); hl=complex(hl)
        Hm.append(p*hm+q*hl); Hl.append(r*hm+s*hl); alphas.append(2*PI*t)
    eps = round((Hm[-1].imag)/(2*PI))
    assert abs(Hm[-1]-eps*2j*PI)<1e-6, Hm[-1]
    # continuity of Im H_l
    tor=[h.imag for h in Hl]
    jump=max(abs(tor[i+1]-tor[i]) for i in range(len(tor)-1)) if n>1 else 0
    da=2*PI/n
    I=da*(sum(tor)-0.5*tor[-1])   # trapezoid, tor(0)=0
    IL=da*(sum(h.real for h in Hl)-0.5*Hl[-1].real)
    J=-eps*I/(4*PI**2)            # SnapPy-normalised twist (sign fixed by validation)
    X=M.copy(); fl=list(base); fl[cusp]=(p,q)
    for i,f in enumerate(fl): X.dehn_fill(f,i)
    return dict(slope=(p,q),dual=(r,s),eps=eps,J=J,Ivol=-0.5*eps*IL,jump=jump,bad=bad,
                cs_fill=float(X.chern_simons()), vol_fill=float(X.volume()), st=X.solution_type(),
                maxtor=max(abs(t) for t in tor), Hend=Hl[-1])
def mod(x,m):
    y=x % m
    return y if y<=m/2 else y-m
