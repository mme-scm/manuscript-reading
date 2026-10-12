# spin / lift utilities for one-cusped SnapPy manifolds
import snappy, warnings, itertools
warnings.filterwarnings('ignore')
def word_vec(w, gens):
    v={g:0 for g in gens}
    for ch in w:
        if ch.islower(): v[ch]+=1
        else: v[ch.lower()]-=1
    return v
def H1Z2(G):
    """basis of H^1(pi;Z/2) as dicts gen->0/1 (brute force)"""
    gens=G.generators(); rels=G.relators()
    out=[]
    for bits in itertools.product([0,1],repeat=len(gens)):
        chi=dict(zip(gens,bits))
        if all(sum(word_vec(r,gens)[g]*chi[g] for g in gens)%2==0 for r in rels): out.append(chi)
    return out
def chi_eval(chi,w,gens):
    v=word_vec(w,gens); return sum(v[g]*chi[g] for g in gens)%2
def cusp_types(M, cusp=0):
    """return SnapPy's lift cusp type (a0,b0) and list of restrictions (chi_mu,chi_lambda) of all chi in H^1(Z/2)"""
    G=M.fundamental_group()
    m,l=G.peripheral_curves()[cusp][:2]
    tm=complex(G.SL2C(m).trace()); tl=complex(G.SL2C(l).trace())
    a0=0.5 if tm.real<0 else 0.0; b0=0.5 if tl.real<0 else 0.0
    gens=G.generators(); chis=H1Z2(G)
    res=[(chi_eval(c,m,gens),chi_eval(c,l,gens)) for c in chis]
    return (a0,b0),(tm,tl),res,G,chis

def genuine_lift_signs(G):
    """Find sign corrections s_g in {0,1} (1 = multiply generator by -1) making SnapPy's SL2C lift a homomorphism."""
    gens=G.generators(); rels=G.relators()
    rhs=[]
    for r in rels:
        t=complex(G.SL2C(r).trace()).real
        assert abs(abs(t)-2)<1e-6, t
        rhs.append(0 if t>0 else 1)
    A=[[word_vec(r,gens)[g]%2 for g in gens] for r in rels]
    for bits in itertools.product([0,1],repeat=len(gens)):
        if all(sum(a*b for a,b in zip(row,bits))%2==rr for row,rr in zip(A,rhs)):
            return dict(zip(gens,bits))
    raise ValueError('no lift')
def signed_trace(G,w,corr):
    gens=G.generators(); v=word_vec(w,gens)
    t=complex(G.SL2C(w).trace())
    flip=sum(v[g]*corr[g] for g in gens)%2
    return -t if flip else t
def cusp_types_all(M):
    """genuine lift cusp types for all cusps + restrictions of H^1(M;Z/2) to (mu_i,l_i) for all cusps"""
    G=M.fundamental_group(); corr=genuine_lift_signs(G)
    pc=G.peripheral_curves(); gens=G.generators()
    P=[]
    for c in range(len(pc)):
        m,l=pc[c][:2]
        tm=signed_trace(G,m,corr).real; tl=signed_trace(G,l,corr).real
        P.append((0.5 if tm<0 else 0.0, 0.5 if tl<0 else 0.0))
    chis=H1Z2(G)
    res=sorted(set(tuple(chi_eval(ch,w,gens) for c in range(len(pc)) for w in pc[c][:2]) for ch in chis))
    return P,res
def realizable(P,res):
    out=set()
    for r in res:
        out.add(tuple(((P[c][0]+r[2*c]/2)%1,(P[c][1]+r[2*c+1]/2)%1) for c in range(len(P))))
    return out
