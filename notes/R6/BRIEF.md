# Brief for this round (read first)

## Setting
K ⊂ S^3 a knot, Y_r = S^3_r(K). P_0 and P_1 are the two SO(3)-bundles on Y_{±2} (w_2 = 0 and w_2 ≠ 0).
DLME is Daemi–Lidman–Miller Eismeier, arXiv:2410.21248; its LaTeX is in scratchpad/dlme/src.

For an irreducible flat connection alpha, c(alpha) = CS~ - gr~/8 = (3 + rho(alpha))/16. Here rho is the APS rho-invariant of the odd signature operator twisted by ad(alpha). Signs are fixed by DLME's Poincaré-sphere example (rho = -73/15, -97/15).

DLME's ell(Y) is the least c-value of a nonzero homology class, in the min-max sense over cycles. We use the same normalisation c = (3+rho)/16 for both bundles: lambda_0(Y) = ell(Y) and lambda_1(Y) = the twisted analogue.

Level of a cobordism map (index bookkeeping, from APS). If an instanton of energy E on W runs from alpha to beta, with i_0 = (degree of insertions) - (dimension of the family), then

  c(beta) - c(alpha) = (i_0 + 3 b^+(W))/8 - E - sum over middle ends M_j of (3 - h(gamma_j) + rho(gamma_j))/16.

On lens-space ends the terms (3 - h + rho)/16 are:
- central flat connection: 0;
- RP^3, rotation by pi: 1/8;
- L(4,1), rotation by pi: 1/4 or 0;
- L(4,1), rotation by pi/2 (w_2 ≠ 0): 3/16 or 1/16, according to orientation.

The maps that carry 1/16 exchange P_0 and P_1.

The notes are rho.tex/rho.pdf in the repo, and notes/G-sources/*.md (ell-1, pillowcase-1, pillowcase-final, cover-1, seifert-1, triangle-1).

## The user's corrections (binding)
1. **No magical energy estimates.** A strategy may not rest on a conjecture that some map loses at least a certain amount of energy, if that estimate is equivalent to the drop being proved. The only energy facts allowed are:
   - energy ≥ 0;
   - energy > 0 for instantons between irreducibles on simply connected cobordisms (no flat connections).

   Exact drops can only come from non-energy terms: the topological terms in the level formula (b^+, i_0, rho of flat connections on middle ends). Where a drop is exact, the relevant cobordism is not simply connected, and a flat (zero-energy) contribution supplies the non-energy term.
2. **Differentials are almost never zero.** Arguments must work for filtered complexes with nonzero differentials, using barcodes and boundary depth. The Seifert examples are the exception: exceptional surgeries, no differentials.
3. **The exact triangles exist and are not the hard part.** Working invariantly on the double cover branched along S, the triangle's outer terms are the SUM over both bundles, and the middle term is the sum of the theories of S^3 and of (S^3, K) with traceless holonomy. So the natural statements are:
   - mixed: compare P_0 on one side with P_1 on the other;
   - both bundles: compare min(lambda_0, lambda_1)(Y_2) with min(lambda_0, lambda_1)(Y_{-2}).

   The drop must have a consistent sign; it is not an absolute value. "Drop > 0" would suffice. The 1/16 should give something to work with.
4. **The previous rho.pdf Step 4 is rejected.** It assumed that absorption into the traceless theory costs energy > 1/16, which is magical. Step 2 assumed zero differentials.

## Data (computed in the absolute normalisation; Seifert examples have zero differential)
- Positive torus knots, n = pq:
  - ell(Y_2) - ell(Y_{-2}) = -1/8 + (2n-5)/(n^2-4), which changes sign;
  - the twisted analogue is 3/8 - 4/(n^2-4);
  - the mixed differences m_1 = lambda_0(Y_2) - lambda_1(Y_{-2}) and m_2 = lambda_1(Y_2) - lambda_0(Y_{-2}) lie in (1/8, 3/16].
- Negative torus knots:
  - the untwisted gap lies in [3/32, 1/8];
  - the twisted gap lies in [0.085, 1/8];
  - m_1 lies in [0.085, 5/32] and m_2 in [1/16, 0.137].
- Figure-eight knot: untwisted 1/10, twisted 1/8, m_1 = 13/80, m_2 = 1/16.
- The both-bundle drop min(lambda_0, lambda_1)(Y_2) - min(lambda_0, lambda_1)(Y_{-2}) is at least 1/8 - 1/884 in all 211 cases.
- 1/16 is attained by m_2 for the figure-eight knot and the mirror trefoil. In both, the minimiser maps at zero energy to the traceless theory through a binary dihedral representation; such representations do not exist when det K = 1.
- Code: scratchpad/gap16/ell-code (torus.py, mixedwide.py, twistedw.py, datatable.py, data_table.txt), scratchpad/fig8-A, scratchpad/fig8-B (sfs.py, Seifert library), scratchpad/mincheck/minvar.py.
