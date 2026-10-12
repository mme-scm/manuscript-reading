from knots import torus
from triangle import *
D = torus(3, 5)
for which in ('I', 'II'):
    for qset in (('q1',), ('q2',), ('q1', 'q2')):
        for rule in ('free', 'int', 'closed'):
            analyse(D, which, qset, rule)
