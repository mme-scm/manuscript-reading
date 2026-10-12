"""Run scan.run on a selected list of knots: python3 scan_sel.py p,q p,q ..."""
import sys
from scan import run
out = []
for s in sys.argv[1:]:
    p, q = map(int, s.split(','))
    for mirror in (True, False):
        for which in ('I', 'II'):
            run(p, q, mirror, which, out)
