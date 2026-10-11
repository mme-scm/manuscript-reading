# A pillowcase action complex C(K) for Chern–Simons filtered instanton homology of 1/n surgeries

LaTeX notes (`main.tex`, compiled to `main.pdf`). Goal: for a knot K in an integer homology sphere whose Alexander
polynomial has no unit-circle roots and whose irreducible SU(2) representation variety is a smooth compact
1-manifold, define a complex C(K) from which the Chern–Simons filtered *irreducible* instanton complex of
Y_{1/n}(K) is extracted by a mapping cone formula with concrete correction terms.

Contents:

* §1 Hypotheses and consequences: generators of CI(Y_{1/n}) are the intersections of the pillowcase curve Γ_K with
  the surgery line; nondegeneracy is transversality (Mayer–Vietoris).
* §2 Chern–Simons = symplectic action in the pillowcase (Kirk–Klassen + an SL(2,Z) change-of-basis lemma); period
  lemma; the per-component absolute constants c_i as the first correction terms.
* §3 The complex C(K): an A_∞-module over the two-line algebra of the pillowcase with underlying complexes CI(Y) and
  CI(Y_0(K), w); rigorous part (exact-triangle maps and homotopies) separated from the conjectural pillowcase model.
* §4 The bound-type cone (levels as in Daemi–Lidman–Miller Eismeier); shown non-exact by the figure-eight.
* §5 The exact statement: Lagrangian surgery (zigzag) + collar perturbation; generators and CS values exact
  (A_cone + area correction δ), the chain-level cone conditional on (N1)–(N3) of Appendix B.
* §6 All slopes: Farey triads, bundle parity rule ε_γ = ε_α + ε_β + 1, Stern–Brocot recursion.
* §7 Tests: trefoil (Σ(2,3,5), Σ(2,3,7), Σ(2,3,11), …), figure-eight (±1, ±1/2, exact cone for n = 1,2,3,
  twelve Farey-triad bundle combinations); scripts and outputs in `numerics/`.
* §8 Workflow. Appendix A: collar perturbations and the perturbed action. Appendix B: Floer's perturbation at
  chain level, conditions (N1)–(N3), gaps.

Build: `pdflatex main.tex && pdflatex main.tex`.
