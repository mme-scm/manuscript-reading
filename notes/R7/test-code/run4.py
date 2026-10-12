from knots import torus
from triangle import *
D = torus(3, 5)
for which in ('I','II'):
  for rule in ('int','closed'):
    for parts in (('gAs','gAn'),('gAn',)):
      I = analyse(D, which, ('q1','q2'), rule, gA_parts=parts, edges=2)
      for key in ('vA','vB'):
        for (x,y) in sorted(I['rel'][key], key=lambda e:(e[0].level,e[1].level)):
            print('   fail',key, x.level, x.label, '->', y.level, y.label)
