from knots import torus
from triangle import *
import sys
D = torus(3, 5)
for which in ('I', 'II'):
    for qset in (('q1',), ('q2',), ('q1', 'q2')):
        for rule in ('int', 'closed'):
            for parts in (('gAs','gAn'), ('gAs',), ('gAn',)):
                analyse(D, which, qset, rule, gA_parts=parts)
