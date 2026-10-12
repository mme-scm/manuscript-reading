# Round 7 brief: the ±2 drop of 1/16

## Goal
K ⊂ S³ is nontrivial with Δ_K = 1 (so det K = 1, genus 2 is the only open case). Y_N = S³_N(K).
- On Y_{±2} there are two SO(3) bundles: P0 (w2 = 0) and P1 (w2 ≠ 0).
- The level of a flat connection is c = (3+ρ)/16, with ρ the APS adjoint ρ-invariant.
- λ_i(Y) is the least level of a nonzero homogeneous class of I(Y, P_i).
- Wanted, ideally: mixed drops m1 = λ0(Y_2) − λ1(Y_{−2}) ≥ 1/16 and m2 = λ1(Y_2) − λ0(Y_{−2}) ≥ 1/16. Positivity (> 0) also suffices.
- A cosmetic pair Y_2 ≅ Y_{−2} would force m1 + m2 = 0.

## Binding rules from the user (an expert in instanton homology)
1. The only energy facts allowed are energy ≥ 0, and energy > 0 for instantons between irreducibles on simply connected cobordisms. NO energy lower bound beyond positivity is ever acceptable. In the user's words: "No energy estimate with a positive lower bound is known, at all, ever, in Floer theory." Exact drops must come from non-energy (topological) terms: index i0, b⁺, ρ-terms of flat connections on middle ends.
2. Differentials are almost never zero; arguments must handle general filtered complexes.
3. The exact triangles exist and are not the difficulty.
4. Hypotheses about positions of generators, or steepness of curves, are energy hypotheses in disguise.
5. Thom principle: a nondegeneracy hypothesis that is not always false may be assumed (transversality, Γ_K avoiding specified points, distinct levels, and so on).
6. Mathematics, not programming exercises: computations are tests, not proofs.

## Setting and maps
These are in notes/R6/strategy-exact.md §§1–6 (the ledger, Prop. 4.1–4.3, Theorem 5.1) and notes/R6/strategy-cover.md §2.

Notation:
- A_i = C(Y_2, P_i), B_i = C(Y_{−2}, P_i), T = traceless complex of (S³, K).
- Mixed triangle (I): A_0 →a→ T →b→ B_1 →c→ A_0. The homotopies are g_A (dg + gd = ba, on W′ = (−X_2) ∪_{S³} X_{−2}, a 1-parameter family), g_M (∂ = cb) and g_B (∂ = ac). The pentagons h give the vertex relations, e.g. id_{A0} ≃ c g_A + g_M a + ∂(h).
- Triangle (II) is the same with the bundles swapped.
- Topological levels: a, b ≤ 0; c = 3/16 (b⁺ = 1, L(4,1) end γ1 with ρ = −1); g_A = −1/8 (i0 = −1); g_M = g_B = +1/16; pentagon −1/16.
- W′ contains a (−4)-sphere S with ∂νS = L(4,1); the odd minimal cap has energy 1/16 = 1/(4|S·S|).

## What is known
- **Theorem 5.1** (strategy-exact): m1 ≥ 1/8 − δ0 + min(η_g, η_a + η_b − β(T)).
  - δ0 = depth of absorption: the least level of a class of ker a_* minus λ0.
  - So the drop exceeds 1/8 whenever the bottom class is not absorbed (kernel criterion).
- **No-go:** explicit filtered models satisfy every triangle relation and level bound with zero drop (strategy-exact §6; strategy-cover §7). The missing input is where the generators sit and which survive.
- **Section 6 of the user's paper** (notes/R7/pillowcase-cone.pdf; our reading in slope2.tex): exact CS values and cone isomorphisms.
  - Rotation identity: drop = g_P − ∫(a_t − a_P)² dt. This gives upper bounds only.
- **±1 case (pm1.tex):** DLME's 1-parameter family map g1 is injective because its triangle's middle term C(S³) ⊕ C(S³) is 0.
  - At ±2 the middle term is T ≠ 0.
  - The family map at ±2 is either not a chain map (even bundle on S: flat L(4,1) caps) or not injective (odd bundle: absorption into T).
- **strategy16.tex (last round):** the inequality (D) δ ≤ 1/16 + η_g.
  - The claimed "tightness in the equality cases" is CIRCULAR: η_g was computed from the answer.
  - (D) is essentially a restatement of the conclusion.
- **Data** (Seifert only; notes/R6/census-final.md and overview.tex):
  - m1, m2, D ≥ 1/16 in 211 exact cases.
  - Equality m2 = 1/16 only for T(2,−3) and 4_1, both via binary dihedral representations at the pillowcase point (1/4, 0).
  - For Δ = 1, generator-level data exist only.

## Files
- notes/R6/*.md and notes/G-sources/*.md: triangle-1.md, cover-1.md, pillowcase-*.md, ell-1.md
- notes/R3-sources/B-final.md: the map B, Theorem A, Conjecture C
- DLME source: scratchpad/dlme/src/*.tex (triangle-2.tex is §5, families of metrics, faces)
- Code:
  - scratchpad/gap16/ell-code/ (torus.py, tables.py, twistedw.py: generators and levels on Y_{±2}(T(p,q)) for both bundles)
  - scratchpad/fig8-A, scratchpad/fig8-B: 4_1
  - scratchpad/gap16/pillowcase-code/
- Repo: /home/user/manuscript-reading (branch claude/intelligent-turing-57b012). Do not commit; write outputs to scratchpad/r7/.
