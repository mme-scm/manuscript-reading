"""Sensitivity of the model to its choices (mirror T(3,5) and mirror T(2,5)): corner rule (free/int/closed),
c-corners (q1, q2, both), gA parts (sing, ns, both), ns-edges (a=0 only / both), grading rule M5 on/off."""
from fractions import Fraction as F
from knots import torus
from triangle import analyse
from study import degeneracies
import itertools
for (p, q) in [(3, 5)]:
    D = torus(p, q)
    for which in ('I', 'II'):
        for rule, qset, parts, edges, graded in itertools.product(('free', 'int', 'closed'), (('q1',), ('q2',), ('q1', 'q2')),
                                                               (('gAs', 'gAn'), ('gAs',), ('gAn',)), (1, 2), (True, False)):
            if rule == 'free' and not graded: continue
            I = analyse(D, which, qset, rule, verbose=False, gA_parts=parts, edges=edges, graded=graded)
            bad = sum(len(v) for v in I['rel'].values())
            print('mT(%d,%d) (%s) rule=%-6s c=%-12s gA=%-10s edges=%d M5=%-5s  failing relation entries: %s %s' % (
                p, q, which, rule, '+'.join(qset), '+'.join(parts), edges, graded, bad, {k: len(v) for k, v in I['rel'].items() if v}))
