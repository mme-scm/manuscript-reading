"""Generator-level injection Z_j -> Z_{j+2} for a large chain via level lookup (no gradings).
Usage: python3 matching_big.py a1 a2 r j"""
import sys
from fractions import Fraction as F
from collections import defaultdict
sys.path.insert(0, '.')
import bk
a1, a2, r, j = map(int, sys.argv[1:5]); P = a1*a2
m0, m2 = r + j*P, r + (j+2)*P
G0 = [c for eps, l, c in bk.analyse((a1, a2, m0), want_all=True)['all']]
G2 = [c for eps, l, c in bk.analyse((a1, a2, m2), want_all=True)['all']]
idx = defaultdict(list)
for k, c in enumerate(G2): idx[c].append(k)
adj = []
for c in G0:
    row = []
    for b in range(0, 4*P + 1):
        t = c - F(1, 8) - F(b*b, 8*m0*m2)
        row += idx.get(t, [])
    adj.append(row)
match_r = [-1]*len(G2)
# simpler: recursive with raised limit
sys.setrecursionlimit(1000000)
import threading
def run():
    def try_(u, seen):
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                if match_r[v] == -1 or try_(match_r[v], seen):
                    match_r[v] = u
                    return True
        return False
    got = 0
    for u in range(len(G0)):
        got += try_(u, set())
    print("chain (%d,%d;%d) j=%d: #Z_j=%d  #Z_j+2=%d  matched %d  -> %s" % (a1, a2, r, j, len(G0), len(G2), got,
          "INJECTION EXISTS" if got == len(G0) else "NO INJECTION"))
    print("  generators of Z_j with no candidate at all:", sum(1 for row in adj if not row))
threading.stack_size(512*1024*1024)
t = threading.Thread(target=run); t.start(); t.join()
