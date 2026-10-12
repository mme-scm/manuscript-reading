# tri-topology-g: the topology-first angle

**Verdict.** This angle gives one genuinely new triangle relating Y_2 and Y_{−2}, together with a new exact source of −1/16. It does **not** give a triangle that meets (1)+(2)+(3), and the failure is sharp. Three obstructions follow, O1–O3 (§g).

Labels: PROVED, PLAUSIBLE, SPECULATIVE. Notation as in BRIEF.

## (a) The triangle Δ_λ (new)

- **Topology (PROVED: Kirby calculus, cross-checked by the mapping-class computation).** Let λ′ ⊂ E_K ⊂ Y_2 be the Seifert-framed push-off of K. Then
  $$Y_{-2}=(Y_2)_{\lambda'}(-1)\quad(\text{framing relative to the Seifert framing of }\lambda').$$
  - Check by twists: one twist T_λ^{−1} of ∂E_K sends (2,1) ↦ (2,1) − 2(0,1) = (2,−1).
  - Check by Kirby calculus: slide K over λ′, then slam-dunk: −1 − 1/(2 − 1) = −2.
  - λ′ is the (2,·)-cable of the dual knot K′_2, and it is null-homologous in Y_2, with genus g(K).
- **The Floer triad of λ′ ⊂ Y_2** (slopes ∞, −1, 0) gives
  $$C(Y_2,P_i)\xrightarrow{\ W_*\ }C(Y_{-2},P_i)\xrightarrow{}C^{w}(Y_0\#\mathbb{RP}^3)\xrightarrow{}C(Y_2,P_i).$$
  - W = W_{λ′} is a **single 2-handle**, with b_2 = 1, form (−1), b⁺ = 0 and π₁ = π₁(Y_2)/⟨⟨λ′⟩⟩.
  - The class dual to the closed surface Σ = core ∪ F′ restricts to 0 on both ends (μ_{λ′} = 0 in H_1(Y_{−2})). So H²(W;Z/2) gives **same-bundle maps only**.
- **Singular variant (new −1/16).** The core D and the cocore C of the λ′-handle have square −1, so s = χ + F·F/2 = 1/2 for each. This gives two maps:
  - σ_λ = (W,D): (Y_2, λ′)^{tl} → Y_{−2};
  - σ′_λ = (W,C): Y_2 → (Y_{−2}, λ′*)^{tl}.

  Each has **topological level exactly (0 − 1/2)/8 = −1/16**, with b⁺ = 0 and i₀ = 0 (PROVED bookkeeping, KM's s-term).
  - These are the ±2 analogues of σ_{±1}: λ′ is a ±1-surgery knot for the pair (Y_2, Y_{−2}).
  - This −1/16 source is missing from BRIEF's arithmetic table, which has only γ1-ends.
  - The one-copy triangle they suggest is Y_{2/3} → (Y_2,λ′)^{tl} → Y_{−2}, since (Y_2)_{λ′}(+1) = Y_{2/3}. The CDX version for λ′ is Y_{2/3} → C(Y_2)^{⊕2} → Y_{−2}.

## (b) Exactness

- Δ_λ is Floer's triangle for a null-homologous knot in a QHS (PROVED, standard; DLME Prop. 3.8 form).
- The CDX version holds by DLME Prop. 3.9 with base Y_2. That is PLAUSIBLE, because the base is a QHS, so the central reducibles θ, θ′ must be handled as in B-final §1.2.
- The one-copy singular triangle is SPECULATIVE. It is degenerate exactly as triangle-1 Prop. 3.1 is (see (e)), so I expect it to fail.

## (c) Injectivity: fails

- The third vertex Y_0 # RP³ has I ≠ 0 for every nontrivial K (KM nonvanishing for (Y_0, w), tensored with the RP³ factor; PLAUSIBLE).
- **Consistency check (PROVED from data).** W_* would give D ≥ 0 if it were injective. But D(T(2,7)) = −1/192 and D(T(3,5)) = −21/1768. So W_* cannot be injective, and this agrees with a nonvanishing third vertex.
- The CDX version has outer vertex Y_{2/3} ≠ 0.

## (d) Levels (PROVED bookkeeping)

| map | b⁺ | i₀ | s or middle end | level | bundles |
|---|---|---|---|---|---|
| W_* = (W_{λ′})_* | 0 | 0 | – | 0 | same |
| family of Δ_λ (inverse direction) | 1 | −1 | S³-type face | ≥ +1/8 | same |
| σ_λ, σ′_λ | 0 | 0 | s = 1/2 | **−1/16** | singular ↔ either P_j |
| Σ-singular (closed surface Σ, genus g) | 0 | 0 | s = 3/2 − 2g | (4g − 3)/16 | same |

**Flat connections.**
- σ′_λ is flat at x iff x(λ) is traceless: π₁(W∖C) = π₁(Y_2), and the meridian of C is λ′.
- σ_λ is flat at z ∈ L_{−2} with z(λ) traceless.
- Both are same-point (Lemma 1 of prove.md applies: W ⊃ E_K × I).

## (e) Pillowcase

- T_λ^{−1} is the half-twist along the arc L_0 = {b = 0}, so the Seidel vertex of Δ_λ is L_0, i.e. Y_0.
- (Y_2, λ′)^{tl} ≃ H := {b = ±1/4} (λ traceless; PLAUSIBLE, via τ_H ≅ T_λ²).
- **H contains all four mixed common points** Q = L_2^ε ∩ L_{−2}^{1−ε} (PROVED: common points have 2b ∈ (ε+ε′)/2 + Z). V = {a = 1/4} contains the same-bundle ones. **H is the mixed analogue of V.**
- But (L_2^0, H, L_{−2}^w) meet in a single triple point with zero area. This is the degenerate configuration that triangle-1 §3.4 showed is *not* a triangle for V. So the H-version inherits the same failure (SPECULATIVE by analogy).

## (f) Checks

- **Sharpness test: fails.**
  - Δ_λ is same-bundle, so it is silent on m₂.
  - In the H-route, bd = (1/4, 0) ∉ H (b = 0), so neither σ-map is flat at bd. The pair bd → Q (T(2,−3)) or bd → z (4₁) needs positive energy there as well.
- **Other data: consistent.** Same-bundle level 0 matches the existence of D < 0. σ-levels −1/16 match c(Q) − c(bd) = −1/16 numerically. That match is not realised by a flat connection.
- **prove.md failure modes.** W_{λ′} is *not* W′ modified near S: it has b_2 = 1 and contains no (−4)-sphere. But it still contains E_K × I, so prove.md's Lemma 1 (same-point rigidity) applies verbatim.

## (g) The obstruction (the sharp negative), hardest step, plausibility

**O1 (slopes; PROVED arithmetic, PLAUSIBLE as a classification).**
- The g ∈ SL(2,Z) with g(2,1) = ±(2,−1) are T_λ^{−1}·Stab(2,1) and T_μ^{4}·Stab(2,1). Here Stab(2,1) is generated by T_{(2,1)}, which fixes Y_2 and has vertex Y_2 # (S¹×S², w) = 0.
- Every knot J ⊂ Y_2 with J ⊂ (collar ∪ filling torus) and a surgery equal to Y_{−2} is the core or a 2-cable (cabling formula; Berge–Gabai in T²×I).
- Hence every triad, CDX or iterated-cone vertex between (Y_2, Y_{−2}) is one of: Y_0#RP³, Y_{±2/3} (λ-route), Y_{±1}, Y_0 (μ-route), S³, or T. The first two families are nonzero for every nontrivial K.

**O2 (bundles; PROVED).**
- The μ-route has four S³ vertices. In the pillowcase it is h_{a=0}^3·h_{a=1/2} for mixed bundles and h_{a=0}^4 for the same bundle.
- Collapsing it to **one** cone with vanishing middle needs several bundle classes on W′ with the same end restrictions, whose L(4,1)-faces cancel: two at distance two in DLME's ĉ, č.
- But H²(W′;Z/2) → H²(Y_2) ⊕ H²(Y_{−2}) is an isomorphism. So E_{γ1} is uncancelled, and the only partner cap is the singular one, which brings back T.
- A Z/4 structure (CDX's SU(4) distance-four triangle) would collapse the four copies (SPECULATIVE). It is not the SO(3) theory, so it says nothing about λ_i.

**O3 (representation change; PROVED group theory).**
- A cobordism containing E_K × I fixes the E_K-representation (prove.md Lemma 1).
- Otherwise Z = Z_1 ∪_M Z_2 with M carrying only reducibles (S³, lens spaces, S¹×S²_w).
- If Z_1 is Y_2 × I plus 2- and 3-handles (π₁-onto), the holonomy on M lies in the image of x. For bd, the SO(3) image is dihedral: D_3 for T(2,−3) and D_5 for 4₁. These contain no element of order 4, so **γ1 can never be the restriction.**
- Holonomies of order ≤ 2 give middle-end terms in (1/8)Z.
- So no flat connection through a reducible-only vertex carries either sharp pair at level −1/16. The only loophole is 1-handles in Z_1, which add b₁ and are not natural from E_K.

**Conclusion.** No exact triangle built from the E_K-topology at slopes ±2 meets (1)+(2)+(3). The 1/16 equality is carried by positive energy on a triangle face (prove.md §2.3), not by a flat connection on any natural cobordism.

**Hardest step.** Making O1 a theorem: the classification of knots in Y_2 with a Y_{−2} surgery that respect the E_K-structure. Beyond that it would have to exclude non-surgery triangles, which this angle cannot do.

**Plausibility.**

| claim | estimate |
|---|---|
| Δ_λ and the −1/16 σ-maps are correct as stated | 85% |
| that they lead to (1)+(2)+(3) | < 5% |
| that the negative O1–O3 is right in the stated scope | 75% |
