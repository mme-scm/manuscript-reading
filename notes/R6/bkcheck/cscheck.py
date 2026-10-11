import bkc, itertools
from fractions import Fraction as Fr
from math import prod
for A in [(2,3,5),(2,3,7),(2,3,11),(2,3,13)]:
    a=prod(A); R=bkc.enumerate_reps(A,want_all=True)
    for c,lab in sorted(R['reps']):
        s=set()
        for sg in itertools.product((1,-1),repeat=3):
            e0=bkc.crt([(sg[i]*lab[i+1]*(a//A[i]))%A[i] for i in range(3)],A)
            for e in (e0,e0+a):
                cs=Fr(e*e,4*a)%1; g=8*(cs-c)
                if g.denominator==1: s.add((str(cs),int(g)%8))
        print(A,lab,c,s)
