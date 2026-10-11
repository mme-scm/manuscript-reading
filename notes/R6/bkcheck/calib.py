import bkc
from fractions import Fraction as Fr
for S in (1,-1):
    print("SIGN",S)
    for A in [(2,3,5),(2,3,7),(2,3,11),(2,3,13)]:
        R=bkc.enumerate_reps(A,sign=S,want_all=True)
        print(A, R['N'], sorted([(str(c),l) for c,l in R['reps']]))
