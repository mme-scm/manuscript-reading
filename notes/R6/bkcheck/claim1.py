import bkc
from fractions import Fraction as Fr
def L(A,o=1):
    v=bkc.ell(A,o); return "inf" if v is None else v
tests=[((2,5,7),1,Fr(11,70)),((2,3,13),1,Fr(8,39)),((3,5,32),1,Fr(-41,120)),((2,5,13),-1,Fr(209,520)),((2,3,5),-1,Fr(59,120))]
for A,o,exp in tests:
    v=L(A,o); print(("+" if o==1 else "-")+str(A),v,"claim",exp,"OK" if v==exp else "MISMATCH")
# K=7 in Sigma(2,5,7): Y_{-1/n} = Sigma(2,5,7+10n)
exp=[Fr(19,170),Fr(17,540),Fr(-17,740),Fr(-22,235)]
for n in range(1,5):
    o,B=bkc.surg((2,5,7),2,n); v=L(B,o); print("n",n,B,v,"claim",exp[n-1],"OK" if v==exp[n-1] else "MISMATCH")
# +1/n for K=7 (reported in brieskorn.md)
for n in range(1,4):
    o,B=bkc.surg((2,5,7),2,-n); print("+1/%d"%n,o,B,L(B,o))
