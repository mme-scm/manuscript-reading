# tri-pillowcase-g: what the pillowcase can and cannot give at ±2

Labels: PROVED / PLAUSIBLE / SPECULATIVE. Notation follows BRIEF. P is the pillowcase, ω = 2da∧db, and Λ is the Novikov field.
- E_0 and E_{1/2} are the edges a = 0 and a = 1/2. Both are S³, and HF(Γ, E) = 0.
- V_α = {a = α}, and V = V_{1/4}.
- q1 = (1/8, 3/4) and q2 = (3/8, 1/4) are the mixed points of L_2^0 ∩ L_{-2}^w. For (II) they are q1′, q2′.

**Verdict.** The angle produces no viable new triangle. What it does give:
- a complete list of the triangles it can produce (C);
- one new triangle, F, whose rigid vertex map Y_2 → Y_{-2} has topological level exactly −1/16, and which is useless because that map is null;
- a general obstruction to the sharpness test (N2), which applies to every construction built on E_K × [0,1], not only to the pillowcase.

Rank obstructions are not used anywhere (BRIEF correction). The pillowcase agrees with that correction:
- For a closed Γ, the edge twists give HF(Γ, L_N^ε) ≅ HF(Γ, L_{N'}^{ε'}).
- For torus knots, the w-lines meet the reducible arc at ζ = (1/4, 0). Edge twists move this point past the ends of Γ at the roots of Δ with a ∈ (0, 1/4); there are about σ/2 of them (PLAUSIBLE).

## (a) The triangles: classification C (PROVED in the Fukaya model of P, given Conj. 3.2)

**Why the list is complete.** Mixed lines share no corner, and L_2^ε ∩ L_{-2}^{1-ε} = {q1, q2} in minimal position. So
Hom(L_2^ε, L_{-2}^{1-ε}) = Hom(L_{-2}^{1-ε}, L_2^ε[1]) = Λ⟨q1, q2⟩.
An exact triangle with two prescribed vertices is the cone of a morphism between them. So every triangle with vertices L_2^ε and L_{-2}^{1-ε} is one of the following. Each cone was computed by resolving the four lifted crossings in T² and taking fluxes.

1. **Backward family B_α.** Cone(λ1 q1 + λ2 q2 : L_{-2}^{1-ε} → L_2^ε[1]) ≅ V_α ⊕ E_0 ⊕ E_{1/2}.
   - The turn-back resolution gives four vertical zigzags.
   - The two zigzags centred on the edges pass through corners, so they are rigid. They are E_0 and E_{1/2}.
   - The zigzag centred on a = 1/4 has one turning point at q1 and one at q2. Its flux is A(s1) − A(s2), where s_i is the neck size at q_i, so α is free.
   - α = 1/4 exactly when λ1 = λ2, i.e. when the cone is χ-symmetric.
   - Instanton reading: the middle term is C^α(K) ⊕ C(S³)².
     - α = 1/4 gives the known triangles (I) and (II).
     - α ≠ 1/4 gives prove.md's Triangle(α₀).
     - α → 0 gives the all-edge triangle L_{-2}^{1-ε} = σ_0 σ_{1/2}³ L_2^ε: four half-twists along S³, middle term 0 for every K. This is the Farey route, whose level is ≥ +1/8.
2. **Forward cone F.** Cone(λ1 q1 + λ2 q2 : L_2^ε → L_{-2}^{1-ε}) ≅ L_0^0 ⊕ L_0^w, for every choice of weights.
   - The horizontal zigzags have their top and bottom turning points alternately at q1 and q2, so their flux is rigidly 0.
   - Instanton reading (NEW; SPECULATIVE as an instanton statement):
     $$F:\quad (Y_2,P_\varepsilon)\xrightarrow{\ \mathcal E_{\gamma_1}+\mathcal E_{\gamma_1'}\ }(Y_{-2},P_{1-\varepsilon})\longrightarrow I(Y_0)\oplus I(Y_0,w)\longrightarrow .$$
     This is a (4, 2, 2)-distance triad, with middle ends L(4,1), RP³ and RP³.
   - **F is the only triangle in P whose map Y_2 → Y_{-2} is a rigid map of topological level −1/16.** That map is row (0, 0, 1/16) of the BRIEF table.
3. **Byproduct (same bundle, not mixed).** Let σ_h be the half-twist along the horizontal arc L_0^w, or along L_0^0. Its lift is one Dehn twist along {b = 1/2}, and it has zero flux against the shear (a, b) ↦ (a + b, b). So σ_h(L_2^ε) ≃ L_{-2}^ε.
   - This gives a same-bundle triangle Y_2^ε → I(Y_0, w) → Y_{-2}^ε with one middle copy, which is not excluded by triangle-1 Prop. 3.1.
   - It is the χ-quotient image of DLME's ±1 triangle with μ and λ exchanged. SPECULATIVE.
   - Its middle term is nonzero (I^w(Y_0) ≠ 0), and its family passes through Y_0, which has b₁ = 1.

So each candidate's middle term is T-like (B_α, monotone only at α = 1/4), or Y_0-like, or 0 (the Farey route, at level ≥ 1/8).

## (b) Exactness of F
- **Pillowcase.** This is the surgery exact triangle for resolving L_2 ∪ L_{-2} at q1 and q2. PROVED in Fuk(P).
- **Instanton side.** Use CDX-type polygon cobordisms E_K × I ∪ solid tori:
  - Y_2 → Y_{-2}: this is X′ with the limits γ1 and γ1′, matching BRIEF/test M3, where c uses both q's;
  - Y_{-2} → Y_0 and Y_0 → Y_2: RP³ middle ends.
- PLAUSIBLE at best. L_0^0 is the reducible arc, so the trivial bundle on Y_0 needs a framed theory. The analysis of the RP³ faces would follow DLME Lemma 5.15.

## (c) Injectivity: fails for every K (PROVED in the model)
- **Each q_i factors through an edge.** q1 = μ²(c_0, c_∞), via the corner triangle (L_2, E_0, L_{-2}) with vertices (0,0), (0,1/2) and q1, of area 1/16. Likewise q2 factors through E_{1/2}.
- Since HF(Γ, E) = 0, μ²(·, q_i) ≃ 0 on every Γ. So F splits: H(Y_0 ⊕ Y_0^w) ≅ H(Y_{-2}) ⊕ H(Y_2)[1].
- This is the pillowcase proof of E_{γ1} = ∂g^ns (strategy-exact 4.1; prove.md §2.1).
- **Level bookkeeping.** level(q) = level(c_0) + level(c_∞) − area = 0 + 0 − 1/16. The topological −1/16 of the rigid exterior is exactly the area of a triangle through an S³ edge, and that is why it is null for every K.

## (d) Levels
- **F's vertex map.** i₀ = 0, b⁺ = 0, γ1 on −∂νS with t = 1/16, so its level is −1/16 exactly. Its only flat connections are at same-point mixed common points with i_{X′} = 0 (prove.md Lemma 1).
- **B_α's third map.** Its level is 1/8 + E_cap(q_i), where E_cap(q_i) = area of the triangle (L_2, V_α, L_{-2}) at q_i:
  - E_cap(q1) = 4(α − 1/8)²;
  - E_cap(q2) = 4(α − 3/8)².
- **The two γ1-parts have equal topological level only at α = 1/4.** This is prove.md's monotonicity obstruction, now as an area identity (PROVED in the model).
- Special values:
  - α = 1/8: V_{1/8} passes through q1, and the q1 cap is flat.
  - α → 0: the caps are 1/16 and 9/16, which are the γ1 and γ1′ caps of strategy-exact 4.1.
- **Clean witness that non-monotonicity is forced.** Suppose B_α (α ≠ 1/4, or α → 0) had a quasi-isomorphism g of topological level −1/8. Then m ≥ 1/8. But 4₁ has m₂ = 1/16, and since σ(4₁) = 0 its data are unaffected by the correction. This replaces prove.md's T̄(3,5) witness, which has σ ≠ 0.

## N2: the sharpness test cannot be met by any construction on E_K × I (PROVED, given the 4₁ data and the level formula)

**Statement.** Let f : C(Y_2, P_1) → C(Y_{-2}, P_0) be a map defined uniformly in K that counts possibly broken instantons on cobordisms or families each containing E_K × [0,1], with E_K × {0} ⊂ Y_2 and E_K × {1} ⊂ Y_{-2}. This covers the whole toolkit: surgery, singular, orbifold and lens-ended cobordisms, families, composites, Toda brackets, pentagons, and pillowcase polygons. If f is nonzero on the bottom class for K = 4₁, then L_top(f) > −1/16.

*Proof.*
1. The data for 4₁ are A_1 = {1/5 at bd, 3/10} and B_0 = {11/80 at z, z̄}, with d = 0 by rank.
2. f[x_bd] ≠ 0 requires a counted configuration x_bd → z with shift −1/16 = L_top − E.
3. A flat configuration restricts to one representation on E_K × I. Since bd ≠ z, none exists. Compactness then gives E > 0.
4. Hence L_top > −1/16. ∎

The same holds for T(2,−3) (bd → q′), conditional on its twisted data, since σ ≠ 0 there. Pillowcase form: a polygon of zero area is constant.

**Consequence.**
- Single-map arguments give m₂ ≥ −L_top < 1/16.
- If topological levels lie in (1/16)ℤ, then L_top ≥ 0. This holds for every row of BRIEF's arithmetic, i.e. ends S³, RP³, L(4,1) and s ∈ ½ℤ.
- So such arguments yield at most m₂ > 0, from positivity, and never ≥ 1/16.
- The requirement "a flat connection that changes the E_K-representation" is unsatisfiable on any cobordism containing E_K × I.

**Remaining escapes.**
1. Cobordisms not containing E_K × I. I know of none that is natural for general K.
2. Arguments in which a non-topological term cancels. Example: 1/16 = 3/16 − δ, where δ is a spacing along Γ. At T(2,−3), δ = (s+2)/64 = 1/8 with s = 6, which is specific to that knot.
3. Branch changes at a double point of Γ. These are E_K × ℝ instantons with positive energy; at 4₁ this is the lobe, 1/10.

## (e) The picture
- 1/16 appears in P in three forms:
  - the area of the mixed triangle (p_A, p_B, q);
  - the area of the corner triangle (L_2, E, L_{-2});
  - the corner action of q.
- The corner action of q is a topological term only for F, whose map is null.
- For B_{1/4} it is an area, i.e. an energy, consistent with test §5.2: returns tile the mixed triangle.
- In the cover a ↦ 2a (= P/χ), the mixed relation becomes one half-twist along the S³ edge plus one along the T edge. This is the CDX descent (#4) again.
- In a ↦ 4a, all flat connections on L(4,1) become edge points, and L_{±2} ↦ L_{±1/2}. One twist along μ, with middle C(Σ_4(K))², descends to (I). Nothing new.

## (f) Checks
- **Sharpness test.**
  - F fails: its vertex map is 0.
  - B_{1/4} reaches 1/16 only through the return η_a + E_M = 1/16.
  - N2 says no single map reaches it.
- **Both bundles.** Flat connections at same-bundle points have gap 1/8. So a both-bundle map of level −1/16 is strict for free, and carries no content (prove.md §2.3).
- **Failure modes reproduced.**
  - E_{γ1} is null: the corner triangle.
  - Triangle(α) is non-monotone: unequal cap areas.
  - The traceless theory absorbs: the middle term of B_{1/4}.
  - The Farey level is ≥ 1/8: the α → 0 limit.

## (g) Hardest step, plausibility
- **Classification C.** PROVED in the model. That the model reflects instanton theory: about 85% (Conj. 3.2 plus the correction).
- **N2.** PROVED from the 4₁ data and the level formula: about 95%.
- **Hardest open step** for any successor: either a cobordism Y_2 → Y_{-2} not containing E_K × I, or a mixed map of topological level 0 that is non-null and nonzero on the bottom class for all K. The latter would give m₂ > 0 strictly; the known level-0 mixed maps, W′_odd and b∘a, are null.
- **Plausibility.**
  - That a pillowcase-derived triangle proves m ≥ 1/16 for all K: < 3%.
  - That F, or the same-bundle byproduct, is a genuine instanton triangle: 40%.
  - That either is useful for the drop: about 0%.
