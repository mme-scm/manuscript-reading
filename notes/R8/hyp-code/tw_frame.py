import snappy
def fix_frame(M):
    """Make (1,0) the given meridian and (a,1) the homological longitude. Assumes M(1,0)=S^3-like (H1=0)."""
    B=M.copy(); B.dehn_fill((0,1)); h=B.homology()
    if h.betti_number()==1: return 0
    n=int(h.order())
    for a in (n,-n):
        C=M.copy(); C.dehn_fill((a,1))
        if C.homology().betti_number()==1:
            M.set_peripheral_curves([(1,0),(a,1)],0); return a
    raise ValueError('no longitude found')
