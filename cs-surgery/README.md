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
* §4 Filtered mapping cone: CI(Y_{1/n}) ≃ Cone(CI(Y_{1/(n−1)}) → CI(Y_0,w)) with filtration offset (n−1)/4 mod Z
  (action of the corner morphism), iterated twisted-complex form for Y = S^3, remarks on −1/n and ±2.
* §5 Tests: trefoil (Σ(2,3,5), Σ(2,3,7), Σ(2,3,11)) and figure-eight (Σ(2,3,7)) numerics.
* §6 Workflow: agent tasks with models, effort levels and acceptance criteria.

Build: `pdflatex main.tex && pdflatex main.tex`.
