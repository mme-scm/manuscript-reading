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

## Round 7b: a NEW triangle is required (user, binding)

**User:** "Something clever needs to happen... I have been aware of both the triangles using Donaldson divisors and the triangle using the singular complex and neither seems to do the trick. A new triangle needs to be suggested."

**Known triangles. Do NOT re-propose these, except as an ingredient of something genuinely new.**
1. **Farey/Floer triads (distance one)** through S³ (C(S³) = 0), and the cones of the uploaded paper's §6.
   - All routes Y_2 → Y_{-2} through Y_{±1} or Y_0 have level ≥ +1/8.
   - Y_0 has b1 = 1, which costs +3/16 per step.
2. **The CDX/DLME distance-two triangle** Y_{n+1} → S³⊕S³ → Y_{n-1}.
   - It works at ±1 (g1 has level −1/8 and is injective because the middle term is 0).
   - At ±2 it must pass through Y_0.
3. **Donaldson-divisor (μ(S)) triangles.** They give the map B: Y_2 → Y_{-2}.
   - B is the quasi-isomorphism, the distance-four "g1".
   - Its level is +1/8, because the μ(S) insertion costs 1/4.
4. **The singular (traceless) triangle** A_i → T(K) → B_{1−i}, which exchanges bundles.
   - Its connecting family g_A has level −1/8, but it is not injective, because T ≠ 0 absorbs.
   - Equivariantly it is the descent of CDX for (Σ_2(K), K̃), with middle term C(S³) ⊕ T(K).

**User's structural guidance.**
- Look for maps of energy 1/16.
- A triangle including BOTH bundles should give a STRICT lower bound. Data: both-bundle drop ≥ 1/8 − 1/884.
- A triangle pairing OPPOSITE bundles should give a NON-STRICT lower bound. Data: m2 = 1/16 exactly for T(2,−3) and 4_1.
- So the relevant cobordism (or family) should:
  - have topological level exactly −1/16;
  - SUPPORT A FLAT CONNECTION (not simply connected);
  - have injectivity coming from a vanishing third term, as at ±1.

**Facts from the ledger, for checking proposals.**
- Level formula: c(β) − c(α) = (i0 + 3b⁺)/8 − E − Σ_j (3 − h(γ_j) + ρ(γ_j))/16 over middle ends.
  - For ends with b1 > 0 (e.g. Y_0), 3b⁺ is replaced by (3/2)(χ + σ).
- Lens terms (3 − h + ρ)/16:
  - central: 0;
  - RP³, rotation by π: 1/8;
  - L(4,1), rotation by π (γ0, h = 1, ρ = ±2): 1/4 or 0;
  - L(4,1), rotation by π/2 (γ1, γ1′ = γ1⊗χ, h = 1, ρ = ±1, w2 ≠ 0): 3/16 or 1/16.
- W′ = (−X_2) ∪_{S³} X_{−2} is simply connected, b⁺ = 0, intersection form diag(−2,−2).
  - It contains the (−4)-sphere S (cocore ∪ core glued along K), with ∂νS = L(4,1).
- X′ = W′∖νS has boundary Y_2 ⊔ −Y_{−2} ⊔ L(4,1) and π1(X′) = π1(E_K)/⟨⟨μ²λ, μ^{−2}λ⟩⟩.
  - Flat connections on X′ correspond to common points of the lines L_2^ε and L_{−2}^{ε′}:
    - same bundle: a = 1/4, b ∈ {0, 1/2}, end γ0, exact gap 1/8;
    - mixed: a ∈ {1/8, 3/8}, end γ1, exact gap 3/16.
  - At mixed points the flat connection has index −1 on X′ and 0 on −X′.
- The exterior map E_{γ1} has level −1/16 and is mixed, but it is null-homotopic: E_{γ1} = d g^ns + g^ns d, because the S³-face of g^ns is empty.
- Minimal odd cap on νS: energy 1/16, index −1.
- Rational ball B_2 with ∂ = L(4,1): the blown-down W″ carries no mixed bundle, and W″_* ≃ 0.
- Branched double cover: Σ_2(K) is a ZHS when det K = 1.
  - Double covers of Y_{±2} are Σ_{±1}(K̃).
  - Over S, (−4, L(4,1)) is covered by (−2, RP³).
  - CS doubles under pullback, and minimal cap energies halve (1/8 ↦ 1/16).
- Pillowcase: Γ_K ⊂ U = pillowcase minus the edges a ∈ {0, 1/2}. The edges are the S³ line and its χ-translate.
  - L_{−2} = (twist along both edges)² applied to L_2.
  - V = {a = 1/4} is the traceless line T(K).
  - Common points: P_w = (1/4, 0), P_0 = (1/4, 1/2), and the mixed points Q = (1/8, 3/4) and (3/8, 1/4) (mod the identifications).
- Equality data, T(2,−3):
  - I^w(Y_2) = {−1/24 at the binary dihedral point (1/4,0), 1/12, 1/12 at the mixed points}.
  - I(Y_{−2}) = {−5/48, −5/48} at the mixed points.
  - m2 = 1/16 = 3/16 (flat mixed gap) − 1/8 (the spacing on Y_2^w, which depends on pq).

## Arithmetic constraint (main thread, PROVED as bookkeeping)

### Setting
A flat connection (E = 0) on a cobordism counted by a map with index i0 forces
  c(y) − c(x) = (i0 + 3b⁺)/8 − Σ_j t_j,
where t_j = (3 − h + ρ)/16 ≥ 0 are the middle-end terms (L(4,1) values: 0, 1/16, 3/16, 1/4).

### Ways to get exactly −1/16 with b1 = 0 and rational-homology-sphere ends

| (i0, b⁺) | Σ t_j | Realisation |
|---|---|---|
| (0, 0) | 1/16 | one γ1 end in the 1/16 orientation |
| (+1, 0) | 3/16 | one γ1 end in the 3/16 orientation; an index-one count, i.e. a codimension-one cut or a divisor of real codimension one |
| (−2, 1) | 3/16 | γ1 end; this is the pentagon type, a 2-parameter family on a b⁺ = 1 cobordism |
| (−1, 1) | 5/16 | two ends, e.g. γ0 (1/4) and γ1 (1/16) |

Since every t_j ≥ 0, (i0, b⁺) = (−1, 0) is impossible: it would need Σ t_j = −1/16.

### Key observation
Same-point flat connections on X′ give only the exact gaps 1/8 (same bundle) and 3/16 (mixed).

So a level −1/16 map whose flat connection realises the equality m = 1/16 must do one of the following:
- connect generators at DIFFERENT pillowcase points. Its cobordism is then not X′-like; its π1 must relate different representations of the knot group, for example through the traceless theory, a cover, or an orbifold point.
- use one of the rows above, with the flat connection at a mixed point having the indicated index.

### Data
For T(2,−3), the equality m2 = 1/16 pairs the binary dihedral generator (1/4, 0) on Y_2^w with the mixed-point generator on Y_{−2}^0: 1/16 = 3/16 − 1/8.

## Round 7c (user, overrides the Δ_K = 1 framing above): target is ALL knots

- The goal is a claim for every nontrivial K ⊂ S³, both chiralities. Δ_K = 1 is one case, not the focus.
- A mechanism that works only when Δ_K = 1 is at best a partial result. Examples: a middle term that vanishes because Γ_K misses the reducible arc (Triangle(α₀)), or "there are no binary dihedral representations". Score proposals on whether they work for general K.
- General target: m₁, m₂ ≥ 1/16, non-strict and sharp. Both-bundle drop D > 0, strict (data: D ≥ 1/8 − 1/884).
- **Sharpness test (mandatory).** A proposal must reproduce exactly 1/16 at T(2,−3) and 4₁. There the realising pair joins *different* representations of E_K: bd on Y_2^w goes to Q (T(2,−3)) or to a non-common point z (4₁) on Y_{−2}^0. It is carried by b′∘a′ through the traceless theory (prove.md §2.3).
  - Flat connections on any cobordism Y_2 → Y_{−2} whose flat part has π₁ = π₁(X′) fix the E_K-representation. Such cobordisms are W′ modified near S.
  - So the sharp map must change representation: it is a triangle face or composite, or it lives on a cobordism of different topology.
- **Middle-term vanishing in general.** I^♮(K) ≠ 0 for every nontrivial K (Kronheimer–Mrowka). A triangle whose middle term is the traceless theory never has a vanishing middle term.
  - Either the third vertex is a theory that vanishes for *every* K (as C(S³) does at ±1), or injectivity must be argued without vanishing.

## Correction (user, after Round 7c): rank obstruction O1 of tri-cover.md is withdrawn
- Floer's triangles (S³, Y_1, Y_2) with w on either side give I(Y_2,w) ≅ I(Y_1) ≅ I(Y_2) for every K. The same holds for Y_{−2}. So there is no rank obstruction to mixed quasi-isomorphisms in the theory that appears in the triangles.
- Where the "16, 12 / 16, 20" for T(3,5) comes from: these are ranks of the *irreducible* twisted complex, which excludes the reducible ζ on the w-bundle (μ ↦ rotation by π, pillowcase point (1/4,0)). ell-1 §2.5 records rank I^w_irr(Y_{±2}) = rank I(Y_1) ± σ(K)/2.
  - The discrepancy is σ/2, contributed by ζ, and it vanishes when σ = 0, e.g. when Δ_K = 1. It is not a det condition: T(3,5) has det 1 and σ = −8.
- Do not use O1 as an obstruction. The rest of tri-cover.md stands.
