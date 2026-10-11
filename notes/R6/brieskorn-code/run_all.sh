#!/bin/sh
# Reproduce everything in r6/brieskorn-code (outputs *.out, *.json, *.txt, examples.md).
set -e
cd "$(dirname "$0")"
python3 validate.py                                  > validate.out
python3 scan.py 1000 nt1000.json                     > scan_nt1000.out 2>/dev/null
python3 scan.py 1000 tk1000.json torus               > scan_tk1000.out 2>/dev/null
python3 scan.py 3000 tk3000.json torus               > scan_tk3000.out 2>/dev/null
python3 scan.py 5000 nt5000.json                     > scan_nt5000.out 2>/dev/null   # ~30 min
python3 ray.py 120 -6 10 rays120.json                > rays120.out
python3 rayan.py rays120.json                        > rayan.out
python3 closedform.py rays120.json                   > closedform.out
python3 closedform2.py rays120.json                  > closedform2.out
python3 betacheck.py                                 > betacheck.out
python3 checks2.py                                   > checks2.out
python3 betalist.py                                  > betalist.out
python3 mixedwin.py                                  > mixedwin.out
python3 longchain.py                                 > longchain.out
python3 matching.py                                  > matching.out
python3 onestep.py nt5000.json tk3000.json           > onestep.out
python3 detail.py nt5000.json tk3000.json            > detail.out
python3 famcheck.py nt5000.json                      > famcheck_nt5000.out
python3 famcheck.py tk3000.json                      > famcheck_tk3000.out
python3 tables.py examples.md nt1000.json tk1000.json
python3 dump.py all_nontorus_a5000.txt nt5000.json
python3 dump.py all_torus_a3000.txt tk3000.json
python3 verify_claims.py nt5000.json tk3000.json     > verify_claims.out
python3 classify.py nt5000.json                     > classify_nt5000.out
python3 classify.py tk3000.json                     > classify_tk3000.out
python3 matching_big.py 3 77 211 1                  > matching_big.out
python3 matching_big.py 3 7 2 3                     >> matching_big.out
