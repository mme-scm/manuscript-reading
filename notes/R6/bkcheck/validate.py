import bkc, itertools, numpy as np
from fractions import Fraction as Fr
from math import gcd, prod
# 1) calibration
for A,exp in [((2,3,5),{Fr(-7,60),Fr(-13,60)}),((2,3,7),{Fr(23,84),Fr(29,84)})]:
    R=bkc.enumerate_reps(A,want_all=True); got={c for c,_ in R['reps']}
    print("calib",A,got==exp)
# 2) CS/grading: find e (CRT with signs, lift mod 2a) s.t. gr = 8(CS - c) integer, CS = e^2/(4a)
def cs_check(A,c,lab):
    a=prod(A); found=set()
    for sg in itertools.product((1,-1),repeat=3):
        e0=bkc.crt([(sg[i]*lab[i+1]*(a//A[i]))%A[i] for i in range(3)],A)
        for e in (e0,e0+a):
            g=8*(Fr(e*e,4*a)-c)
            if g.denominator==1: found.add((e%(2*a), int(g)%8))
    return found
triples=[t for t in itertools.combinations(range(2,40),3) if all(gcd(x,y)==1 for x,y in itertools.combinations(t,2)) and prod(t)<=3000]
print("triples",len(triples))
bad_m2=0; bad_cs=0; bad_par=0; bad_perm=0; bad_sig=0; bad_8a=0; nrep=0; worst=0
grset=set()
for A in triples:
    R=bkc.enumerate_reps(A,want_all=True)
    a=prod(A)
    # Brieskorn signature
    if bkc.brieskorn_sigma(A)!=-4*R['N']//1 or 4*R['N']!=-bkc.brieskorn_sigma(A): bad_sig+=1
    ms=sorted(c for c,_ in R['reps'])
    # permutation invariance
    for perm in [(1,2,0),(2,0,1),(1,0,2)]:
        B=tuple(A[p] for p in perm)
        R2=bkc.enumerate_reps(B,want_all=True)
        if sorted(c for c,_ in R2['reps'])!=ms: bad_perm+=1
    for c,lab in R['reps']:
        nrep+=1
        if (8*a*c).denominator!=1: bad_8a+=1
        f=bkc.c_fs_float(A,lab)
        worst=max(worst,abs(f-float(c)))
        if abs(f-float(c))>1e-8: bad_m2+=1
        fd=cs_check(A,c,lab)
        if not fd: bad_cs+=1
        else:
            pars={g%2 for _,g in fd}
            grset|={g for _,g in fd}
            if pars!={1}: bad_par+=1
print("reps",nrep,"M2 mismatches",bad_m2,"max|M1-M2|",worst)
print("8ac nonint",bad_8a,"no integral CS-lift",bad_cs,"non-odd grading",bad_par,"perm mismatch",bad_perm,"Brieskorn sigma mismatch",bad_sig)
print("grading residues mod 8 seen",sorted(grset))
# 3) min/max search vs full multiset
bad=0
for A in triples:
    R=bkc.enumerate_reps(A,want_all=True)
    cs=[c for c,_ in R['reps']]
    if R['cmin']!=min(cs) or R['cmax']!=max(cs): bad+=1
    if set(R['argmin'])!={l for c,l in R['reps'] if c==min(cs)}: bad+=1
print("min/max search mismatches",bad)
