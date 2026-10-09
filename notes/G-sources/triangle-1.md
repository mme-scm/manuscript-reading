# Singular instantons, the distance-four triangle, and the 1/16

Line of attack: exact triangles and filtered relations among I(Y_2), I(Y_{-2}) and the singular instanton homology of (S^3, K) with holonomy parameter 1/4. Here K ⊂ S^3 is a knot, Y_r = S^3_r(K), and K̄ is the mirror of K.

Every claim carries one of three labels:
- **VERIFIED**: proved here, computed exactly, or checked against a source.
- **PLAUSIBLE**: supported by an argument with a gap that is named.
- **SPECULATIVE**: heuristic.

The scripts are in `gap16/triangle-code/`. The torus-knot machinery in `tk.py` re-implements the formulas of the sibling notes `ell-1.md` and `pillowcase-1.md`, which calibrated them against DLME's Example 3.7 and against Fintushel–Stern. I use those notes' results where stated, and I re-derive the facts I need.

---

## 0. Summary

1. **The distance-four relation is a double twist about the traceless circle (VERIFIED, pillowcase topology).**
   - In the pillowcase, the Lagrangian of the ±2 fillings satisfies L_{-2} = τ_V^2(L_2), where V = {α = 1/4} is the traceless circle. The ±1 fillings satisfy L_{-1} = τ_V(L_1).
   - L_2, L_{-2} and V meet in a single triple point, the traceless representation with λ ↦ −1.
   - For a holonomy parameter α_0, the triangle bounded by L_2, V_{α_0} and L_{-2} has area (1 − 4α_0)^2/4. This equals the energy of the reducible on νS with ⟨c_1(L), S⟩ = −1, singular along S with holonomy α_0. The value is 1/4 at α_0 = 0, 1/16 at α_0 = 1/8, and 0 at α_0 = 1/4.

2. **The same-bundle singular configuration does not close up into a triangle (VERIFIED for torus knots).**
   - On (W′, S), singular along S with holonomy 1/4 and the trivial bundle on both ends, the one-parameter family has the following faces:
     - its L(4,1) face has a flat cap of index −1;
     - its J = S^3 face is the composite Y_2 → I^tl(K) → Y_{-2} through the traceless theory. This is the obstruction the user found.
   - No exact triangle I(Y_2) → I^tl(K) → I(Y_{-2}) with these maps can exist for torus knots. The ranks and gradings forbid it. For T(2,5), the levels contradict it as well.

3. **The correct triangles exchange the bundle (PLAUSIBLE construction; strong numerical evidence).** I propose the two exact triangles
   - (I) I(Y_2) → I^tl(K) → I^w(Y_{-2}) → I(Y_2), and
   - (II) I^w(Y_2) → I^tl(K) → I(Y_{-2}) → I^w(Y_2).

   Their maps are:
   - two singular 2-handle maps of level 0;
   - a third map on the lens-ended exterior of νS, with the odd bundle, of level 3/16.

   The homotopy g on W′ is the difference of two families:
   - the nonsingular family with bundle odd on S;
   - the singular family along S.

   **Each fails on its own, which is what was observed. Together they work:** their L(4,1) faces cancel, because both glue to a cap of energy 1/16. The only face that remains runs through the traceless theory, and that face is exactly the third vertex of the triangle.

   For det K = 1 these triangles should be the τ-quotient of DLME's distance-two triangle for (Σ_2(K), K̃) (PLAUSIBLE; §4.5).

   Evidence (VERIFIED computations), for the 29 torus knots T(p,q) with p < q ≤ 15 and pq ≤ 60, both chiralities:
   - rank identities hold exactly;
   - parities are consistent;
   - the filtered maps are compatible with the predicted levels;
   - the predicted levels are sharp: the level 3/16 of the third map and the level 0 of the singular maps are attained;
   - the controls behave as they should: DLME's ±1 window is reproduced in 25 of 25 cases, and the two triangles that should fail do fail.

4. **Where 1/16 comes from (VERIFIED as bookkeeping).**
   - Let E_cap be the energy of the minimal index −1 reducible bounding the middle-end flat connection of the third cobordism. In a DLME/CDX triangle whose third cobordism has b⁺ = 1:
     - the third map has level 1/8 + E_cap;
     - the two vertex homotopies have level E_cap;
     - with no interference from the middle term, the difference of ℓ between the two ends lies in the window [1/8, 1/8 + E_cap].
   - The values of E_cap are:

     | case | E_cap | window |
     |---|---|---|
     | DLME ±1 (RP^3) | 1/8 | [1/8, 1/4] |
     | mixed ±2 (L(4,1), odd flat connection γ_1) | **1/16** | [1/8, 3/16] |
     | same-bundle singular ±2 | 0 | — |

   - In general E_cap = 1/(4|S·S|) for the odd class on the disk bundle of the sphere S, with S·S = −2p for ±p surgery.
   - Under the double cover branched along S, E_cap halves (1/8 ↦ 1/16), but the family term 1/8 does not.
   - **This is the precise sense in which the 1/16 is the reducible of observation (i).**

5. **Consequences (conditional on (I), (II)).**
   - The kernel criterion: the mixed differences m_1 = ℓ(Y_2) − ℓ^w(Y_{-2}) and m_2 = ℓ^w(Y_2) − ℓ(Y_{-2}) exceed 1/8 whenever the traceless theory does not absorb the ℓ-minimiser.
   - For positive torus knots parity forbids absorption. Then m_1, m_2 ∈ (1/8, 3/16], as observed (0.131 to 0.1875).
   - For mirrors, absorption happens and m drops. The two examples with m = 1/16 exactly (T̄(2,3) and 4_1) are absorptions of zero energy at binary dihedral representations. For T̄(2,3), m = 3/16 − 1/8 exactly.
   - The same-bundle difference is D = m_1 − ε_{-2} = m_2 + ε_2, where ε_{±2} = ℓ(Y_{±2}) − ℓ^w(Y_{±2}). The triangles do not control ε_{±2}. This is why D has no forced gap (T(2,7): −1/192).

6. **Cosmetic pairs (conditional theorem).**
   - Assume (I), (II), and suppose S^3_2(K) ≅ S^3_{-2}(K) = Y. Suppose also that no irreducible traceless representation sends λ to ±1, as for det-1 torus knots.
   - Then both ℓ-minimisers, of I(Y) and of I^w(Y), must be absorbed by I^tl(K). Moreover
     ℓ(I^tl) < min(ℓ(Y), ℓ^w(Y)) ≤ max(ℓ(Y), ℓ^w(Y)) < ℓ(I^tl) + 1/16,
     and dually for ℓ⁺.
   - Consequently, if either singular 2-handle map I(Y_2) → I^tl(K) or I^w(Y_2) → I^tl(K) costs energy > 1/16 on the ℓ-minimiser, there is no cosmetic pair.
   - **The missing input is exactly an energy bound of size E_cap = 1/16 for absorption by the traceless theory.**

**Confidence.**
- Bookkeeping and pillowcase facts: 90–95%.
- The mixed triangles: 65%.
- The conditional theorems, given the triangles: 85%.
- That the 1/16 the user sees "is" E_cap: 70%.

---
## 1. Conventions and normalisations

### 1.1 Manifolds (VERIFIED, standard)

**Surgeries and traces.**
- Y_N = S^3_N(K) = ∂X_N, where X_N is the trace. X_N° is the trace with a ball removed, viewed as a cobordism S^3 → Y_N.
- Mirroring: Y_{-N}(K) = −Y_N(K̄).

**The cobordism W′.**
- W′ = (−X_2°) ∪_J X_{-2}° : Y_2 → Y_{-2}, with J ≅ S^3.
- Its cores are disks D_l ⊂ −X_2° and D_r ⊂ X_{-2}°, both with boundary K ⊂ J.
- Relative to the Seifert framing, D_l·D_l = D_r·D_r = −2.
- S = D_l ∪ D_r is a sphere with S·S = −4, and ∂νS = L(4,1).

**The complement of S.**
- X_N° minus a neighbourhood of its core deformation retracts onto Y_N.
- Hence W′∖νS ≃ Y_2 ∪_{E(K)} Y_{-2}, and
  π_1(W′∖νS) = π_1(E(K)) / ⟨⟨μ^2λ, μ^{-2}λ⟩⟩.
- A representation of this group has ρ(μ)^4 = 1 and ρ(λ) = ρ(μ)^2.
- So the flat connections on W′∖νS with irreducible ends are exactly the traceless representations with λ ↦ −1, i.e. the common generators of Y_2 and Y_{-2}.

**Classes.**
- H^2(W′; Z/2) = ⟨F_l^*, F_r^*⟩ restricts isomorphically to H^2(Y_2) ⊕ H^2(Y_{-2}).
- Both F_l^* and F_r^* are odd on S.
- The restriction map H^2(νS; Z/2) → H^2(L(4,1); Z/2) is an isomorphism. So a bundle that is odd on S is nontrivial on ∂νS: it is twisted on exactly one end of W′.

### 1.2 The level c and the uniform normalisation (VERIFIED: ell-1 Theorem A, pillowcase-1 Theorem 3.1)

**Definition.** For an irreducible nondegenerate flat connection α on a rational homology sphere,
  c(α) := CS~(α) − gr(α)/8.

**Lift independence.** This does not depend on the lift, because (CS~, gr) ↦ (CS~ + 1, gr + 8). In DLME's normalisation (CS~(θ) = 0, gr = index to θ),
  c(α) = (3 + ρ(α))/16,
where ρ is the APS ρ-invariant of ad α.

**Relation to ℓ.** DLME's ℓ(A) = inf_d (κ_A(d) − d/8) is the least c-level at which an infinite bar is born.

**Uniform normalisation.** I use c := (3 + ρ)/16 for **both** bundles on Y_{±2}. This is ell-1's absolute level plus 3/16.
- It agrees with DLME on the trivial bundle.
- The twisted theory's own normalisation, through its abelian reducible ζ, differs by (1 − σ(K))/8. This is an odd multiple of 1/8, so it is not a source of sixteenths.
- In the uniform normalisation, a map of degree D and level L shifts c by L − D/8. The rule of §1.4 is then the same for every pair of bundles (ell-1, Proposition B).
- An orientation-preserving diffeomorphism Y_{-2} → Y_2 preserves the uniform normalisation of both bundles, because ρ is a diffeomorphism invariant.

**Orientation reversal.** c(−Y, α) = 3/8 − c(Y, α).

**Normalisation checklist (VERIFIED against DLME and ell-1).**
1. **Chern–Simons.** CS is in SU(2) units: degree-one gauge transformations shift it by 1. DLME's sign is CS_DLME = −cs, so that E = CS~(in) − CS~(out) − c^2/4 ≥ 0. For SO(3) bundles, energies are −p_1/4, which equals c_2 on liftable bundles. The odd caps of §3.1 have −p_1/4 = −ξ^2/4 = 1/16 in these units; there is no factor of 2 between SU(2) and SO(3) here.
2. **Grading.** The absolute grading d is the Z-valued index from the chosen lift of α to θ. The "d/8" in ℓ pairs this Z-lift with the real lift of CS. The period (CS~, d) ↦ (CS~ + 1, d + 8) is what makes c lift-independent.
3. **Singular theory.** For the singular theory of (S^3, K) the period is (1/2, 4): the monopole number changes κ by 1/2 and the index by 4. So c^tl is again lift-independent.
4. **Orientation.** Y_{-N}(K) = −Y_N(K̄), and every orientation statement goes through c ↦ 3/8 − c.

### 1.3 The traceless singular theory and its level (VERIFIED, from KM's formulas)

**KM's formulas.** For SU(2) singular connections with holonomy parameter λ along a closed surface Σ, Kronheimer–Mrowka give (0806.1053, `yaft_paper.tex` lines 1410–1420, checked in the source):
- index 8k + 4l + χ(Σ) − 3(b⁺ − b^1 + 1);
- action k + 2λl − λ^2 Σ·Σ.

At λ = 1/4, on a closed pair with b^1 = 0,
  ind − 8κ + 3(1 + b⁺) = s(Σ),  where s(Σ) := χ(Σ) + Σ·Σ/2.

**The traceless theory.** C^tl(K) is the complex of (S^3, K) with holonomy 1/4. It is generated by the irreducible traceless SU(2) representations, R*(K; i), and is Daemi–Scaduto's irreducible complex. The reducible θ_K is the abelian representation with μ ↦ i and h^0 = 1. CS is defined modulo 1/2 and the grading modulo 4.

**Its level.** I define
  c^tl(x) := 3(1 + b⁺(W))/8 + (ind A − 8κ(A) − s(F))/8,
for any cap (W, F) of (S^3, K) with b_1(W) = 0 and any singular connection A asymptotic to x. Here F·F is taken relative to the Seifert framing of K.
- Well defined: index and action are additive, s is additive for a common framing, and the closed formula vanishes.
- Under orientation reversal, c^tl(K̄, x̄) = 3/8 − c^tl(K, x), by the same argument as for Y.

**Singular disks and spheres in W′.**
- For D_l ⊂ −X_2° and D_r ⊂ X_{-2}°: s = 1 − 2/2 = 0.
- For S: s(S) = 2 − 4/2 = 0.
- For the cores of −X_1° and X_{-1}° (square −1): s = 1 − 1/2 = 1/2. These give the only half-integral s in sight; see §2.4.

### 1.4 Level bookkeeping (VERIFIED as bookkeeping)

Let (W, F) be a cobordism between rational homology spheres or knot pairs, with b_1(W) = 0. Let G be a family of metrics and z an insertion. A counted instanton A has:
- energy E;
- index i_0 = codim(z) − dim G;
- limits γ_j, with h(γ_j) = h^0 + h^1, on middle ends M_j oriented as part of ∂W.

Then
  c(out) − c(in) = 3b⁺(W)/8 + (i_0 − s(F))/8 − E − Σ_j (3 − h(γ_j) + ρ(M_j; γ_j))/16.  (1.1)

This is ell-1's Proposition B with KM's s-term added. For a cap (W, F) of index i bounding a reducible γ with h^0(γ) = 1 and h^1(γ) = 0, the same additivity gives
  c_γ := (3 − h(γ) + ρ(γ))/16 = 3(1 + b⁺)/8 + (i − 8E − s)/8.  (1.2)

**Lens space values.** On L(4,1) = ∂(disk bundle of Euler number −4), consider the flat SO(3) connection whose generator acts by rotation through 2πk/4. Its ρ-invariant is 0, 1, 2, 1 for k = 0, 1, 2, 3 (ell-1 `spaceform.py`; my `pillow.py` re-checks (1.2)). Following ell-1, I write:
- **γ_0** for k = 2: rotation by π, SU(2)-liftable (holonomy i), ρ = 2. It is the restriction to ∂νS of every traceless representation.
- **γ_1** for k = 1: rotation by π/2, odd (w_2 ≠ 0 on L(4,1)), ρ = 1.

On RP^3, ρ = 0 for the abelian flat connection.

---
## 2. The pillowcase: twists, a triple point, and areas

### 2.1 Setting
- **Coordinates.** ρ(μ) ~ e^{2πiα}, ρ(λ) ~ e^{2πiβ}. The pillowcase is the quotient of the torus (α, β) ∈ (R/Z)^2 by (α, β) ↦ (−α, −β), with four corners.
- **Area form.** ω = 2 dα∧dβ, so the total area is 1 and Chern–Simons values are actions (pillowcase-1, Theorem 2.1).
- **Lagrangians.**
  - L_N = {Nα + β ∈ Z} and L_N^w = {Nα + β ∈ 1/2 + Z} are the ±N fillings, untwisted and twisted.
  - V_{α_0} = {α = α_0} is the filling of the meridional slope by a solid torus whose core is singular with holonomy α_0.
  - V := V_{1/4} is the traceless circle.
- **Character curve.** C* is the image of the irreducible representations of the knot group.
- **The Atiyah–Floer dictionary is heuristic.** Generators of I(Y_N) are the points of C* ∩ L_N, those of I^tl(K) are the points of C* ∩ V, and CS is the action.

### 2.2 Twists (VERIFIED, `pillow.py`)

**The Dehn twist about V_{α_0}.** For α_0 ∈ (0, 1/2), the curve V_{α_0} lifts to the two circles {α = α_0} and {α = 1 − α_0}. The twist lifts to the shear
  (α, β) ↦ (α, β + Φ(α)),  Φ = 0, 1, 2 on [0, α_0), (α_0, 1 − α_0), (1 − α_0, 1].
This is isotopic to T^2, where T(α, β) = (α, β + α) and T(L_N) = L_{N−1}.

**The image of L_N.** The image of L_N has ∫β dα = −(N − 2)/2. That is the flux of the straight L_{N−2}, so
  τ_{V_{α_0}}(L_N) ≅ L_{N−2}  (Hamiltonian isotopic), for every α_0.

Hence L_{-1} = τ_V(L_1) and **L_{-2} = τ_V^2(L_2)**. The distance-four relation is a double twist about the traceless circle. The single twist sends L_2 to L_0, the untwisted 0-filling.

**DLME's case.** For DLME's ±1 case, the twist τ_{V_ε} about a thin circle around the meridional arc L_∞ is the square of the half-twist about L_∞. Since V_ε is "two copies of L_∞", this is the pillowcase form of DLME's middle term C(S^3)^{⊕2}.

**Interpolation.** As α_0 runs from 0 to 1/4, V_{α_0} interpolates from that degenerate middle term to the traceless circle. The curves are isotopic but enclose different areas, so they are not Hamiltonian isotopic.

### 2.3 The triple point and the areas (VERIFIED)

**The triple point.**
- L_2 ∩ V = L_{-2} ∩ V = {C_0}, where C_0 = (1/4, 1/2), the traceless representation with λ ↦ −1.
- Among the circles V_{α_0}, only the traceless one passes through L_2 ∩ L_{-2}.

**Areas.** For general α_0, the three curves bound a triangle with vertices (α_0, 1 − 2α_0), (α_0, 2α_0) and C_0. Its area is
  A(α_0) = (1 − 4α_0)^2/4 = 4(α_0 − 1/4)^2.

**Reducibles on νS.** Let ξ ∈ H^2(νS) with ⟨ξ, S⟩ = 1, so ξ^2 = −1/4 and PD(S) = −4ξ. An SU(2) reducible L ⊕ L^{-1} on νS, singular along S with holonomy α_0 and with c_1(L) = mξ, has effective class (m + 4α_0)ξ and energy (m + 4α_0)^2/4. For m = −1 this is exactly A(α_0):

| α_0 | area A(α_0) | reducible with m = −1 | its role |
|---|---|---|---|
| 0 | 1/4 | the nonsingular even reducible (E = 1/4, index 1, boundary γ_0) | the obstruction that forces the divisor μ(S) in B |
| 1/8 | **1/16** | energy 1/16 | the value of the odd SO(3) cap of observation (i) (§3.1) |
| 1/4 | 0 | the flat singular cap (index −1, boundary γ_0) | the face of the same-bundle singular family (§3) |

**The ±1 analogue.** The triangle (L_1, V_{α_0}, L_{-1}), with third vertex the corner θ, has area 2α_0^2. This equals the energy (m + 2α_0)^2/2 at m = 0 of the corresponding reducible on the (−2)-sphere. At α_0 = 1/4 the area is 1/8, DLME's cap energy.

**The mixed triangle.** L_2, V and L_{-2}^w bound a triangle with vertices:
- (1/4, 1/2), traceless with λ ↦ −1;
- (1/4, 0), traceless with λ ↦ +1;
- (3/8, 1/4), in L_2 ∩ L_{-2}^w.

Its area is **exactly 1/16**, the energy of the odd caps of §3.1. This is the pillowcase picture of the triangles of §4. Observation (iv)'s "a^2 = 1/16" is the solid-torus term Nα^2 at the traceless point. The relevant 1/16 here is instead 4δ^2 at the mixed points δ = α − 1/4 = ±1/8.

### 2.4 What the pillowcase does and does not predict (SPECULATIVE / VERIFIED negative)

**Prediction.** Seidel's exact sequence for τ_V and τ_V^2 would give triangles with one traceless copy at ±1 (L_1 → V → L_{-1}). It would give a two-step filtration with two traceless copies at ±2.

**Failure at ±1 with one copy.** The instanton version of the first fails: no triangle I(Y_1) → I^tl(K) → I(Y_{-1}) exists for torus knots.
- The singular 2-handle maps have odd degree, so parity forces rank I(Y_{-1}) = rank I(Y_1) + rank I^tl.
- But rank I(Y_1) = rank I(Y_{-1}) (DLME, Lemma 4.3).
- The rank test fails for all 25 torus knots tested, those with p ≤ 6, q ≤ 13 and pq ≤ 60 (`control.py`; VERIFIED).

The reason is that C contains the reducible arc and the corners, which the irreducible theories discard. So the pillowcase is a guide to *which* Lagrangian enters, not to the exact form of the instanton triangles.

**A remark on ±1.** For the ±1 cores (square −1), s = 1/2, so the singular maps Y_{±1} ↔ (S^3, K) have level −1/16 each. If the traceless theory were transparent, DLME's 1/8 would factor as two half-steps of 1/16. It is not transparent, as just shown.

---

## 3. The same-bundle singular configuration on W′, and why it is not a triangle

### 3.1 Caps on νS (VERIFIED by (1.2) and the formulas of §2.3)

| cap on νS | bundle | energy | boundary | index |
|---|---|---|---|---|
| flat, singular along S (holonomy 1/4, m = −1) | SU(2)-type | 0 | γ_0 | −1 |
| nonsingular reducible, c_1(L) = ξ | SU(2), even on S | 1/4 | γ_0 | +1 |
| nonsingular SO(3) reducible, adjoint line c_1 = ξ | odd on S | **1/16** | γ_1 | −1 |
| SO(3)-type singular reducible, adjoint holonomy π around S, n = −1 or −3 | odd on S | **1/16** | γ_1 | −1 |

**The two odd caps.**
- The SO(3)-singular reducibles have effective class (n + 2)ξ, so their energy is (n + 2)^2/16.
- Their boundary must be γ_1. By (1.2), an energy-1/16 cap on γ_0 would have index 8(1/4 − 3/8) + 1/2, which is not an integer. On γ_1 the index is −1.
- The two odd caps are the two equivariant descents of DLME's cap Â_N (energy 1/8 on the (−2)-disk bundle). This agrees with cover-1, §3.4.

### 3.2 The family and its faces

**The family.** Let g_S count index −1 instantons on (W′, S), singular along S with holonomy 1/4, trivial on Y_2 and Y_{-2}. The interval of metrics G runs from the metric broken along J to the metric broken along ∂νS. By (1.1) with b⁺ = 0 and s(S) = 0, g_S has level −1/8 − η. Its faces are as follows.

**The L(4,1) face (PLAUSIBLE).**
- It is the exterior W′∖νS with limit γ_0 (index 0), glued to the flat cap (index −1); the total index 0 + h^0(γ_0) − 1 = 0 is correct.
- B-final, Theorem A(e) shows that this exterior map (X_{2,−2}, γ_0) is null-homotopic.
- So the face can be absorbed into g_S.

**The J face.** It consists of pairs of index-0 singular instantons on (−X_2°, D_l) and (X_{-2}°, D_r), glued at an irreducible traceless x. That is, it is b∘a, where
- a : C(Y_2) → C^tl(K), the singular 2-handle map;
- b : C^tl(K) → C(Y_{-2}), the singular 2-handle map.

**Breaking at θ_K (PLAUSIBLE).** This would need an irreducible index −1 instanton asymptotic to θ_K. Its framed moduli space is 0-dimensional and carries a free U(1)-action, so it is generically empty.

**Flat connections.** At common points (λ ↦ −1) there is a flat singular connection on (W′, S).
- Its index is −1. This is VERIFIED for torus knots, by consistency with ell-1 and pillowcase-1.
- The mechanism is PLAUSIBLE: by Mayer–Vietoris, each half has a 1-dimensional twisted H^2. Its self-intersection is −2 ± t, where t is the twisted framing of K at the point, i.e. minus the slope of C*. The index of a half is −1 exactly when this is positive.
- So η(g_S) = 0 when such points exist.
- This matches the gap c(Y_2, x) − c(Y_{-2}, x) = 1/8 at common points (ell-1, §6.3).

**Conclusion.** d g_S + g_S d ≃ b∘a. **This is precisely the obstruction the user met.**

### 3.3 Levels and degrees of the singular 2-handle maps (VERIFIED as bookkeeping)

**Formulas.** By (1.1) with b⁺ = 0, s = 0 and i_0 = 0:
- a and b have level −η.
- Their degree is D = 8κ_top + s(D) = 1 (mod 4), where κ_top = −D·D/16 = 1/8 (mod 1/2).

**Computation of c^tl.** I computed c^tl for torus knots through the flat singular connection on (−X_N°, D_N) at points common to V and L_N:
  c^tl(x) = c(Y_N, x) + (3[N < 0] + ind − (1 − N/2))/8.
- Here ind = −[pq − N > 0]: the twisted framing of K at x is pq = −(slope of C* at x).
- The value is the same for every admissible N, positive and negative, including N > pq where the index and the Maslov term of pillowcase-1 jump together (`tk.py`; 9 knots, all traceless points).

**Findings.**
- In pillowcase-1's normalisation, c^tl = Φ − 1/16 for positive torus knots and c^tl = Φ + 1/16 for their mirrors.
- At a common point the traceless generator has the **same** c as the Y_{-2} generator, respectively the Y_2 generator. The singular map that sees the flat connection has index 0 and energy 0.
- So the traceless theory never sits halfway (at Φ). In the Seifert-framed normalisation the singular maps between Y_{±2} and (S^3, K) move c by integers over 8 minus energy, never by 1/16.

**Sign convention for CS^tl (it fixes the grading parities).**
- The relation CS^tl(x) = CS(Y_N, x) + N/16 (mod 1/2) at a flat singular connection uses the reference action −D·D/16. This is KM's −λ^2Σ·Σ at λ = 1/4, entering exactly as DLME's −c^2/4 enters E = −c^2/4 + CS~(in) − CS~(out).
- The opposite sign would shift gr^tl by N, which is odd, and so flip every traceless parity.
- With the sign used here, the traceless theory of a positive torus knot is even, and the rank identities of §4.6 hold. With the opposite sign they would fail for (I) and (II).
- So, given Conjecture T, the data also confirm the convention.

**Third map.** The same-bundle triangle's third map would be X_{-2,2} := −(W′∖νS) : Y_{-2} → Y_2, with b⁺ = 1 and middle end ∂νS carrying γ_0. Its level is 3/8 − (3 − 1 + 2)/16 = 1/8.

### 3.4 Proposition 3.1 (no same-bundle triangle with one traceless copy; VERIFIED for torus knots)

**Statement.** For every torus knot T(p,q) with p < q ≤ 15 and pq ≤ 60, and its mirror, there is no exact triangle I(Y_2) →a I^tl(K) →b I(Y_{-2}) → I(Y_2) in which a and b have odd degree.

**Proof.**
1. **Gradings** (`parity.py`). For positive torus knots:
   - I(Y_2) and I^w(Y_2) are supported in even degrees;
   - I^tl(K) is supported in even degrees (0 and 2 mod 4);
   - I(Y_{-2}) and I^w(Y_{-2}) are supported in odd degrees.

   For mirrors every grading g becomes −3 − g, so I^tl is odd while Y_2 stays even and Y_{-2} odd.
2. **Positive torus knots.** Here a = 0, so b is injective and the third map is surjective. Exactness then forces rank I(Y_{-2}) = rank I(Y_2) + rank I^tl.
3. **Mirrors.** Here b = 0, which forces the same identity with Y_2 and Y_{-2} exchanged.
4. **Contradiction.** rank I(Y_2) = rank I(Y_{-2}) (they are equal in all cases, and equal in general under (H1)), while I^tl ≠ 0. ∎

**Level version for T(2,5).** The numbers are ℓ(Y_2) = 79/160, ℓ(Y_{-2}) = 37/80 and c^tl ∈ {3/5, 13/20}.
- Since a = 0, the quasi-isomorphism (a, g_S) of triangle detection would make g_S(x) a nonzero class of level ≤ 79/160 − 1/8 = 59/160 < 37/80.
- Hence the homotopy relation of triangle detection (the pentagon with its S^2 × S^1 face) must fail for the same-bundle singular configuration. The singular distance-four configuration with trivial bundles is **not** a triangle.

**Pillowcase reading (SPECULATIVE).** The pillowcase suggests that the correct same-bundle object has two traceless pieces, one shifted in degree by an odd amount (§2.4). I have not pursued this.

---
## 4. The bundle-exchanging distance-four triangles

### 4.1 Statement

**Conjecture T (PLAUSIBLE; evidence in §4.6).** For every knot K ⊂ S^3 there are exact triangles of F_2-vector spaces
- (I) I(Y_2) →a I^tl(K) →b I^w(Y_{-2}) →c I(Y_2) → ⋯
- (II) I^w(Y_2) →a′ I^tl(K) →b′ I(Y_{-2}) →c′ I^w(Y_2) → ⋯

Here I^tl(K) is the homology of the irreducible traceless complex of §1.3. The maps enrich to IP-morphisms. In the uniform normalisation their levels are as in the table of §4.3:
- a, a′, b, b′: level ≤ 0;
- c, c′: level ≤ 3/16;
- the triangle-detection homotopies g: −1/8 − η with η > 0, and 1/16, 1/16.

For each vertex, the map (f, g) into the cone of the next map is a filtered quasi-isomorphism.

### 4.2 Construction (PLAUSIBLE; it follows DLME §5 / CDX with the changes listed)

I describe triangle (I). Triangle (II) is the same with the bundles on the ends exchanged. The setup is that of DLME §5.2:
- C_1 = C(Y_2), C_0 = C^tl(K), C_{-1} = C^w(Y_{-2});
- the cobordisms come from [−1,1] × E(K) by filling with the slope-2 solid torus, the meridional solid torus with singular core, and the slope −2 solid torus.

**The maps f.**
- f_1 = a is (−X_2°, D_l), singular along the core disk, with trivial bundle on Y_2.
- f_0 = b is (X_{-2}°, D_r), singular along the core disk. Its SO(3) bundle restricts to w on Y_{-2}. It is unique, because X_{-2}°∖D_r ≃ Y_{-2}.
- f_{-1} = c is X_{-2,2} = −(W′∖νS), with the class that is w on Y_{-2} and 0 on Y_2. This class is odd on ∂νS, so the limit there is γ_1.

**The map g_1 = g_A : C(Y_2) → C^w(Y_{-2}).** It lives on W′ with w_2 = F_r^*, over the interval of metrics G of §3.2. It is the sum (over F_2) of two counts of index −1 instantons:
- g^ns: nonsingular, with the bundle odd on S;
- g^sing: singular along S with holonomy 1/4, of SO(3) type (odd near S).

Its faces:
- **J face of g^ns.** The bundle on J ≅ S^3 is trivial and only θ is flat. Breakings there have index at least 3, as in DLME Lemma 5.9. So this face is empty. This is the half of the construction that the user observed to be harmless.
- **J face of g^sing.** It is b∘a, through the irreducible traceless complex. Breakings at θ_K are excluded as in §3.2.
- **L(4,1) faces of g^ns and g^sing.** Both are the same exterior count on (W′∖νS, F_r^*) with limit γ_1 (index 0). One is glued to the nonsingular odd cap, the other to the singular odd cap. Both caps have energy 1/16 and index −1 (§3.1), and the gluing parameter is Stab(γ_1)/(Stab(ext) × Stab(cap)) = point. So the two faces are the same count, and they cancel in g^ns + g^sing.

Hence d g_A + g_A d = b∘a.

> **The user's two failed attempts are the two halves of g_A.**
> - The odd-bundle nonsingular family fails only at its L(4,1) face. The cap of energy 1/16 there has no nonsingular partner (cover-1, §3.6).
> - The singular family fails only at its J face, through the traceless representations.
>
> The sum cancels the first defect. What is left of the second is exactly the composite through the third vertex of an exact triangle.

**The other homotopies.**
- g_0 : C^tl → C(Y_2) lives on (X_{-2}°, D_r) ∪_{Y_{-2}} X_{-2,2}, and g_{-1} : C^w(Y_{-2}) → C^tl lives on X_{-2,2} ∪_{Y_2} (−X_2°, D_l).
- Their second faces are along spheres of the type of DLME's M^i_{i−2} ≅ S^3, here meeting the singular locus in an unknot. The traceless unknot has only its reducible, so these faces should be empty by DLME-type index counts.

**The pentagons h_i.** These are DLME's pentagons. The S^2 × S^1 faces give q_i ≃ id by the degree-one argument of CDX, Propositions 5.40 and 5.53. At the vertices adjacent to c, the lens faces cancel between the nonsingular and singular parts, as the RP^3 faces cancel between ĉ and č in DLME Lemma 5.15.

**The gaps in this sketch.**
1. Gluing at the γ_1 face with a *singular* cap (h^0 = 1, stabiliser U(1)), and the equality of the two face counts.
2. Exclusion of breakings at the U(1)-reducible θ_K throughout: index −1 framed moduli spaces with a free U(1)-action are empty, but this must be checked in every stratum. For general knots, Daemi–Scaduto's framed complex may be needed at the middle vertex.
3. The degree-one argument of CDX for the mixed singular/nonsingular S^2 × S^1 face.

### 4.3 Levels (VERIFIED as bookkeeping from (1.1); uniform normalisation, c^tl Seifert-framed)

| map | cobordism, family | b⁺ | i_0 | s | middle end, limit, term | level |
|---|---|---|---|---|---|---|
| a, a′ | (−X_2°, D_l) | 0 | 0 | 0 | — | −η (η = 0 iff a flat singular connection exists, i.e. at a common point) |
| b, b′ | (X_{-2}°, D_r) | 0 | 0 | 0 | — | −η (likewise) |
| c, c′ | X_{-2,2} = −(W′∖νS), odd | 1 | 0 | 0 | ∂νS, γ_1: (3 − 1 + 1)/16 = 3/16 | **3/8 − 3/16 = 3/16** |
| g_A | W′, interval, g^ns + g^sing | 0 | −1 | 0 | — | −1/8 − η, with **η > 0** |
| g_M = g_0 | (X_{-2}°, D_r) ∪ X_{-2,2}, interval | 1 | −1 | 0 | γ_1: 3/16 | **1/16** − η |
| g_B = g_{-1} | X_{-2,2} ∪ (−X_2°, D_l), interval | 1 | −1 | 0 | γ_1: 3/16 | **1/16** − η |
| h | pentagon | 1 | −2 | 0 | γ_1: 3/16 | −1/16 |

**Why η(g_A) > 0 (VERIFIED, topology).**
- The nonsingular part lives on the simply connected W′ with w_2 ≠ 0, so it has no flat connection.
- A flat connection in the singular part would be a traceless representation with λ ↦ −1 (untwisted on Y_2) and λ ↦ +1 (twisted on Y_{-2}) at once.

**Degrees.** a, a′, b, b′ have odd degree (1 mod 4 for untwisted ends, §3.3); g_A has odd degree.

### 4.4 The general rule behind the numbers (VERIFIED as bookkeeping)

**Setting.** In any DLME/CDX-type triangle:
- the third cobordism has b⁺ = 1 and middle end ∂νS;
- ∂νS carries a flat connection γ with h(γ) = 1;
- γ bounds on νS a cap of index −1 and energy E_cap;
- the first two maps have level ≤ 0.

**The rule.** (1.2) gives c_γ = 3/8 − 1/8 − E_cap = 1/4 − E_cap, hence

  level(c) = 3/8 − c_γ = **1/8 + E_cap**,  level(g at the two vertices next to c) = **E_cap**,  level(g_A) = −1/8.

Without interference from the middle term, g_A and c are inverse to each other on homology, and the difference of ℓ between the two ends lies in the window **[1/8, 1/8 + E_cap]**.

| triangle | E_cap | third map | window |
|---|---|---|---|
| DLME ±1, middle C(S^3)^2 = 0, RP^3 cap | 1/8 | 1/4 | [1/8, 1/4] (lower end: DLME's theorem; upper end: PLAUSIBLE, ell-1) |
| mixed ±2 (I), (II), odd lens cap | **1/16** | **3/16** | [1/8, 3/16] |
| same-bundle singular ±2, flat cap | 0 | 1/8 | [1/8, 1/8] (but not a triangle, §3.4) |

**The cap energy in general.** For the odd class ξ on the disk bundle of a sphere S with S·S = e < 0, we have ξ^2 = 1/e, so E_cap = 1/(4|e|). With S·S = −2p for the cores of ±p surgery, E_cap = 1/(8p): it is 1/8 for p = 1 and **1/16 for p = 2**.

**Through APS.** E_cap = 1/4 − (2 + ρ(γ))/16. The 1/16 is ρ(L(4,1); γ_1) = 1 entering with the coefficient 1/2 of the APS formula, divided by the 8 of d/8.

### 4.5 Relation to the branched double cover (VERIFIED topology; descent PLAUSIBLE)

Let det K = 1, which holds when Δ_K = 1. Cover-1 (§§2–3) shows the following.
- The double cover of W′ branched along S is DLME's W^1_{-1} for (Σ_2(K), K̃).
- The RP^3 = ∂νS̃ covers ∂νS.
- DLME's bundles ĉ, č are pullbacks of F_l^*, F_r^*, which are odd on S.

So DLME's triangle for (Σ_2(K), K̃) is τ-equivariant, and its fixed part is (I) ⊕ (II):
- The middle term I(Σ_2(K))^{⊕2} descends to two copies of I^tl(K). These are the invariant connections with order-two isotropy along K̃, counted modulo χ, which matches the counts modulo χ at the ends. The SU(2) counts used below double everything uniformly.
- The ends descend to both bundles on Y_{±2}.
- The bundles are exchanged because ĉ, č are odd on S.

**Energies and levels under the cover.**
- CS and energies halve under the cover, so DLME's cap energy 1/8 becomes E_cap = 1/16.
- The family term 1/8 is an index, not an energy, so it does not halve.
- Hence the third map goes from level 1/4 = 1/8 + 1/8 upstairs to 3/16 = 1/8 + 1/16 downstairs.

**This is the precise relation between the 1/16 and the branched double cover.** Cover-1's invariant ℓ̃ = ℓ(Ỹ)/2 halves the family term as well, and gets a 1/16 gap for a different reason.

**Beyond det = 1.** The data of §4.6 suggest that (I) and (II) hold for det K ≠ 1 as well, for example T(2,q) with Σ_2 = L(q,1). So the downstairs construction of §4.2 is the right formulation, and it needs no equivariant transversality.

### 4.6 Evidence (VERIFIED computations; `feas.py`, `sharp2.py`, `parity.py`, `control.py`, `fig8_tri.py`)

All complexes below are perfect (single parity), so the homology is spanned by the generators. Counts are SU(2) counts: χ-pairs are listed twice, χ-fixed (binary dihedral) generators once.

**(a) Ranks.** For all 29 torus knots T(p,q) with p < q ≤ 15 and pq ≤ 60:

  rank I^w(Y_{-2}) = rank I(Y_2) + #R*(K; i)  and  rank I(Y_{-2}) = rank I^w(Y_2) + #R*(K; i),

with the two identities exchanged for mirrors. This is exactly what (I) and (II) require when parity kills a, a′ (positive knots) or b, b′ (mirrors). Examples:

| knot | Y_2 | Y_2^w | traceless | Y_{-2} | Y_{-2}^w |
|---|---|---|---|---|---|
| T(2,3) | 2 | 1 | 1 | 2 | 3 |
| T(3,5) | 16 | 12 | 4 | 16 | 20 |
| T(5,7) | 96 | 88 | 8 | 96 | 104 |
| T(4,13) | 210 | 198 | 12 | 210 | 222 |

The traceless count equals |σ(K)|/2. The same-bundle identities fail in every case.

**(b) Filtered maps with the predicted levels exist.** For each of the 58 cases (29 knots, both chiralities) and each of (I) and (II), there are bases matched compatibly with:
- a, b at level 0;
- c at level 3/16;
- g_A at level −1/8.

This was checked by bipartite matching under the interval constraints.

**(c) Sharpness of the levels.** I computed, over 60 triangle instances (the 15 torus knots with p ≤ 5, q ≤ 11 and pq ≤ 35, both chiralities, both triangles), the least levels that keep (b) true:
- third map: maximum 3/16 exactly, attained for T(2,3), T(2,5), T(2,7), T(2,9), T(2,11), T(3,10) and T(5,6), in one or both chiralities and triangles;
- singular map: maximum 0 exactly, attained at the common points by the flat singular connections;
- family map: at most −0.1328 < −1/8, consistent with η(g_A) > 0.

So the predicted levels 3/16 and 0 are attained, and the level −1/8 is respected with room to spare.

**(d) Controls.**
- DLME's ±1 window [1/8, 1/4] is feasible in 25 of 25 cases (p ≤ 6, q ≤ 13, pq ≤ 60; both chiralities). This checks the method against a theorem.
- The one-copy ±1 triangle (§2.4) and the same-bundle ±2 triangle (§3.4) fail the rank test in 25 of 25 cases.

**(e) Figure-eight.** For 4_1, C* is closed (Δ has no roots on the unit circle) and there is no parity simplification. The data:
- Y_{±2}: one SO(3) class each, at c = 19/80 and 11/80;
- Y_2^w: {1/5, 3/10}; Y_{-2}^w: {3/40, 7/40};
- two binary dihedral traceless generators, with c^tl either {1/5, 7/40} or {3/40, 3/10} depending on slope signs I did not determine.

In both cases (I) and (II) admit level-compatible maps with rank a = rank b = rank c = 1. This was checked by hand:
- For (I): A = {19/80, 19/80} and B = {3/40, 7/40}. One 19/80 lies in ker a and is matched with 3/40, a gap of 13/80 ∈ [1/8, 3/16]. b sends one traceless class to 7/40 at level ≤ 0, and a sends the other 19/80 onto the other traceless class.
- For (II): see §5.4.

---
## 5. Consequences for ℓ

All levels are in the uniform normalisation (c-units). I write
- u_N = ℓ(I(Y_N)), v_N = ℓ(I^w(Y_N)) for N = ±2;
- μ = ℓ(I^tl(K)) for the least birth level of an infinite bar of the traceless theory;
- m_1 = u_2 − v_{-2} and m_2 = v_2 − u_{-2} for the mixed differences;
- D = u_2 − u_{-2} and D^w = v_2 − v_{-2} for the same-bundle differences;
- ε_N = u_N − v_N for the bundle offsets.

### 5.1 The vertex lemma (VERIFIED: formal consequence of a filtered quasi-isomorphism)

**Lemma 5.1.** Let (f, g) : C_V → Cone(f′ : C_{V′} → C_{V″}) be a quasi-isomorphism, where f, g, f′ have levels λ_f, λ_g, λ_{f′}. Let x be a cycle representing an infinite bar of H(V) born at ℓ(V). Then one of the following holds:
- (i) [f x] ≠ 0, and then ℓ(V′) ≤ ℓ(V) + λ_f;
- (ii) f x = d y, and then ℓ(V″) ≤ max(ℓ(V) + λ_g, lev(y) + λ_{f′}).

In case (ii), lev(y) ≤ ℓ(V) + λ_f + β(V′), where β is the boundary depth. For perfect complexes, case (ii) means f x = 0 and ℓ(V″) ≤ ℓ(V) + λ_g.

*Proof.*
1. The class of (f x, g x) in H(Cone f′) is nonzero.
2. If f x = d y, subtract the boundary of (y, 0). This leaves (0, g x + f′ y), which is a cycle of C_{V″} with nonzero class. ∎

Applied to (I) at its three vertices (perfect case, η ≥ 0 the energies):

| vertex (minimiser) | alternative (i) | alternative (ii) |
|---|---|---|
| (I-A): I(Y_2), at u_2 | μ ≤ u_2 − η_a | v_{-2} ≤ u_2 − 1/8 − η_g |
| (I-M): I^tl, at μ | v_{-2} ≤ μ − η_b | u_2 ≤ μ + 1/16 − η |
| (I-B): I^w(Y_{-2}), at v_{-2} | u_2 ≤ v_{-2} + 3/16 | μ ≤ v_{-2} + 1/16 |

The vertex lemmas for (II) are the same with the bundles exchanged. The dual statements, for ℓ⁺, follow by reversing orientation: c ↦ 3/8 − c, the arrows reverse, and the levels are unchanged.

### 5.2 Theorem 5.2 (kernel criterion; VERIFIED as a deduction from Conjecture T)

**Statement.** If the ℓ-minimising cycle x of I(Y_2) satisfies a x = 0 at chain level, then
  ℓ^w(Y_{-2}) ≤ ℓ(Y_2) − 1/8 − η(g_A) < ℓ(Y_2) − 1/8,  that is, m_1 > 1/8.

If instead a x = d y with lev(y) ≤ u_2 − 1/8 + η_b, the same holds with ≤ in place of <.

Likewise for (II): if a′ kills the minimiser of I^w(Y_2), then m_2 > 1/8.

*Proof.* Lemma 5.1(ii) at the vertex A of (I), together with η(g_A) > 0 (§4.3). ∎

**Relation to DLME.** This is DLME's argument with the middle term C(S^3)^{⊕2} = 0 replaced by the traceless complex. Downstairs, it is the τ-quotient of cover-1's Theorem 1.

### 5.3 Corollary 5.3 (positive torus knots; VERIFIED given Conjecture T and the computed gradings)

For positive torus knots, a = a′ = 0 by parity (§3.4). Hence m_1, m_2 > 1/8.

**Upper bounds.** For every positive torus knot with p ≤ 6, q ≤ 13 and pq ≤ 60, μ > v_{-2} + 1/16 (`ubound.py`). So alternative (ii) of (I-B) fails, alternative (i) holds, and m_1 ≤ 3/16. The same argument gives m_2 ≤ 3/16 except for T(2,3), where μ ≤ u_{-2} + 1/16; there m_2 = 5/32 directly. So the mixed differences of positive torus knots lie in the window **(1/8, 3/16]**.

Data check: in ell-1's table of 105 positive torus knots, m_1 ∈ [0.1311, 0.1875] and m_2 ∈ [0.1350, 0.1875] (VERIFIED from `ell-code/data_table.txt`). This is a non-trivial check of the levels of a, b, c and g.

### 5.4 Absorption, and the examples with m = 1/16 (VERIFIED computations, `examples.py`)

For mirrors, b = b′ = 0 by parity and a, a′ are surjective, so the traceless theory can absorb the bottom of I(Y_2) or I^w(Y_2). `examples.py` tests whether a level-compatible configuration exists with the minimiser in ker a. Where none exists, absorption is **forced**:
- for T̄(2,q) and T̄(3,4): forced in (II);
- for T̄(4,5): forced in (I);
- for the det-1 mirrors T̄(3,5), T̄(3,7), T̄(5,7): forced in both.

| knot | u_2 | v_2 | u_{-2} | v_{-2} | μ | m_1 | m_2 | D | D^w |
|---|---|---|---|---|---|---|---|---|---|
| T(2,7) | 0.4970 | 0.6845 | 0.5022 | 0.3304 | 0.7857 | 0.1667 | 0.1823 | **−0.0052** | 0.3542 |
| T(3,5) | 0.4974 | 0.6897 | 0.5093 | 0.3328 | 0.9542 | 0.1646 | 0.1804 | **−0.0119** | 0.3569 |
| T̄(2,3) | −0.0104 | −0.0417 | −0.1042 | −0.1667 | −0.0417 | 0.1562 | **1/16** | 0.0938 | 0.1250 |
| T̄(3,5) | −0.6255 | −0.6255 | −0.7494 | −0.7109 | −0.6292 | 0.0854 | 0.1239 | 0.1239 | 0.0854 |
| T̄(5,7) | −1.9251 | −1.9251 | −2.0499 | −2.0499 | −1.9268 | 0.1248 | 0.1248 | 0.1248 | 0.1248 |
| 4_1 | 19/80 | 1/5 | 11/80 | 3/40 | 7/40 or 3/40 | 13/80 | **1/16** | 1/10 | 1/8 |

**How m = 1/16 arises.** In the two examples with m_2 = 1/16, the twisted minimiser of Y_2 is a binary dihedral generator at the common point (1/4, 0). It is absorbed at energy 0 by a flat singular connection. The window then forces the next class of I^w(Y_2) to be the one matched with ℓ(Y_{-2}).

- **T̄(2,3).** I^w(Y_2) = {−1/24, 1/12, 1/12} and I(Y_{-2}) = {−5/48, −5/48}. The pair (−1/24, −5/48) has gap 1/16, outside the window, so ker a′ = {1/12, 1/12}. These are matched at the top of the window, 3/16. The spacing is exactly 1/8 = (s + 2)·(1/8)^2 with s = 6, so

    m_2 = λ_c − spacing = 3/16 − 1/8 = 1/16 = E_cap.

- **4_1.** I^w(Y_2) = {1/5, 3/10} and I(Y_{-2}) = {11/80, 11/80}. Here ker a′ = {3/10}, matched at 13/80, and

    m_2 = 13/80 − 1/10 = 1/16.

  I see no structural reason why this second difference equals E_cap. It may be a coincidence of the particular values.

In both examples the minimiser is absorbed at zero energy at a binary dihedral representation. Binary dihedral representations do not exist when det K = 1.

For the det-1 mirrors T̄(3,5), T̄(3,7), T̄(5,7), the absorbed minimiser lies only 0.0037, 0.0027 and 0.0017 above the bottom of I^tl. So absorption is very cheap, and m ≥ 0.0854.

### 5.5 The same-bundle difference (VERIFIED identities)

  D = m_2 + ε_2 = m_1 − ε_{-2},  D^w = m_1 − ε_2,  D + D^w = m_1 + m_2.

The triangles control m_1, m_2 but not the bundle offsets ε_{±2}.
- For positive torus knots ε_{-2} ranges from 0.09 to 0.22. This exceeds m_1 − 1/16, so D can be negative. This is the structural reason for the counterexamples to the same-bundle claim (T(2,7), T(3,5), …).
- For det-1 mirrors, ε_{±2} ≈ 0. The untwisted and twisted generators interleave along the branches through the traceless line, so D ≈ m ≈ 1/8.

### 5.6 Cosmetic pairs (VERIFIED as a deduction from Conjecture T, perfect complexes)

**Proposition 5.6.** Assume Conjecture T, and suppose φ : Y_{-2} → Y_2 =: Y is an orientation-preserving diffeomorphism. Put u = ℓ(I(Y)), v = ℓ(I^w(Y)), μ = ℓ(I^tl(K)). Suppose no irreducible traceless representation of K sends λ to ±1 (so every singular 2-handle map has η > 0), and the complexes are perfect. Then:
- (a) the minimisers of I(Y) and of I^w(Y) are both absorbed by I^tl(K);
- (b) μ < min(u, v) ≤ max(u, v) < μ + 1/16, so in particular |ℓ(Y) − ℓ^w(Y)| < 1/16;
- (c) dually, μ⁺ > max(u⁺, v⁺) ≥ min(u⁺, v⁺) > μ⁺ − 1/16.

*Proof.* φ identifies I^w(Y_{-2}) with I^w(Y) and I(Y_{-2}) with I(Y), level-preservingly.

(a) Suppose the minimiser of I(Y) is not absorbed.
1. (I-A) gives v ≤ u − 1/8 − η_g.
2. Then (II-A) cannot take its second alternative u ≤ v − 1/8, so μ ≤ v − η_{a′} < v.
3. (I-M) gives either v ≤ μ − η_b < v, which is impossible, or u ≤ μ + 1/16 < v + 1/16 ≤ u − 1/16, which is a contradiction.

The case of I^w(Y) is symmetric.

(b) Both minimisers are absorbed, so μ < u and μ < v.
1. (I-M): the alternative v ≤ μ − η_b contradicts μ < v. So u < μ + 1/16.
2. (II-M) gives v < μ + 1/16 in the same way.

(c) Reverse orientation. A cosmetic pair for K gives one for K̄, with c ↦ 3/8 − c. ∎

**Without the hypothesis on λ ↦ ±1.** The conclusions hold unless some singular map has energy-zero contributions, that is, unless there are flat singular connections at common points.

**Theorem 5.7 (conditional criterion).** Under the hypotheses of Proposition 5.6, suppose the singular 2-handle map a : I(Y_2) → I^tl(K), **or** a′ : I^w(Y_2) → I^tl(K), costs energy > 1/16 on the ℓ-minimiser. Then S^3_2(K) and S^3_{-2}(K) are not orientation-preservingly diffeomorphic.

*Proof.* By (a), the minimiser is absorbed, so μ ≤ u − η_a < u − 1/16. This contradicts (b). ∎

**Corollary 5.8 (a computable obstruction, given Conjecture T).** A cosmetic pair requires the window condition

  W(Y): μ < min(ℓ(Y), ℓ^w(Y)) and max(ℓ(Y), ℓ^w(Y)) < μ + 1/16,

together with its dual W⁺, for **both** Y = Y_2 and Y = Y_{-2}. Each of these is a condition on Y_{±2} and on the traceless theory of K separately.

`window.py` tabulates these for the 25 torus knots with p ≤ 6, q ≤ 13 and pq ≤ 60, and their mirrors:
- no knot satisfies all four;
- W(Y_2) holds exactly for the det-1 mirrors T̄(3,5), T̄(3,7), T̄(3,11), T̄(3,13), T̄(5,7), T̄(5,9), T̄(5,11);
- W⁺(Y_{-2}) holds exactly for their mirror images, the positive det-1 torus knots.

So det-1 torus knots are "half cosmetic" in this sense, and fail on the other side.

**Boundary depth.** With nonzero boundary depths β, the lemmas acquire error terms of size β, and so do the conclusions: 1/16 becomes 1/16 + O(β). This is PLAUSIBLE. It matters for cosmetic candidates (Δ_K = 1), whose complexes have balanced gradings and are not expected to be perfect.

---
## 6. What is missing, and attempts to supply it

### 6.1 The missing inputs, precisely

**(M1) Conjecture T itself.** The three analytic points are listed at the end of §4.2:
- the γ_1 face with a singular cap;
- the exclusion of θ_K-breakings, or replacing C^tl by Daemi–Scaduto's framed complex at the middle vertex;
- CDX's degree-one argument in the mixed singular/nonsingular setting.

For det K = 1 there is an alternative route: a localisation theorem (Tate or Borel) for the τ-action on DLME's triangle for (Σ_2(K), K̃). This would need equivariant transversality, which generally fails (cover-1, §5.6). I regard the direct downstairs construction as more promising.

**(M2) Control of the bundle offsets ε_{±2} = ℓ(Y_{±2}) − ℓ^w(Y_{±2}), for a same-bundle statement.** No triangle with a traceless middle term controls these offsets: by §5.5, D = m_2 + ε_2.
- The same-bundle claim |ℓ(Y_2) − ℓ(Y_{-2})| ≥ 1/16 is false for positive torus knots: T(2,7), −1/192; T(3,5), −21/1768; T(5,7), −0.0718. This was reproduced here by my re-implementation of the formulas, not by independent code.
- So no mechanism in this line can prove it for all knots.

**(M3) For excluding cosmetic pairs, given Conjecture T.** Either of the following suffices:
- an absorption bound: the singular 2-handle map on the ℓ-minimiser costs energy > 1/16 (Theorem 5.7);
- the failure of one of the four window conditions of Corollary 5.8.

**(M4) Boundary-depth control** when the complexes are not perfect, as expected for Δ_K = 1.

### 6.2 Attempts on (M3)

**(a) Local model on a steep branch (VERIFIED arithmetic; the model is pillowcase-1's formula, PLAUSIBLE in general).** By §3.3, on a branch of slope s through a traceless point z, with |s| > 2:
- the traceless generator sits at Φ(z) + sgn(s)/16;
- the Y_2 generators sit at Φ_0 + 1/16 + (s + 2)δ^2.

Absorbing the Y_2 generator nearest to z costs:
- **s < −2** (the case of positive torus knots): about 1/8 − (|s| − 2)δ_min^2 ≥ 1/8 − 1/(4(|s| − 2)), since |δ_min| ≤ 1/(2(|s| − 2)). This is ≥ 1/16 once |s| ≥ 6, so Theorem 5.7's mechanism is available.
- **s > 2** (the case of mirrors): about (s + 2)δ_min^2 ≤ 1/(4(s + 2)) < 1/16. So absorption is cheap.

This matches the data: absorption costs 0.0037, 0.0027 and 0.0017 for T̄(3,5), T̄(3,7) and T̄(5,7).

So the absorption bound holds on negatively sloped branches and fails on positively sloped ones.
- A cosmetic K forces K̄ cosmetic as well, and reverses all slopes. But the minimisers relevant for K̄ are the maximisers for K, so this does not close the argument.
- For Δ_K = 1 the curve C* is closed and both slope signs occur. **I could not supply (M3).**

**(b) Zero-energy absorption needs common points.** By §5.6, zero-energy absorption requires a traceless representation with λ ↦ ±1. The two examples with m = 1/16 use binary dihedral representations, and these do not exist when det K = 1. So for Δ_K = 1 every absorption costs positive energy (VERIFIED as a statement about flat connections). The examples suggest the following.

> **Conjecture M′ (SPECULATIVE, about 30%).** If det K = 1, then m_1 > 1/16 and m_2 > 1/16 in the uniform normalisation.

- Evidence: the minimum over det-1 torus knots is 0.0854, at T̄(3,5).
- Consequence: for a cosmetic pair, m_1 = −m_2, so Conjecture M′ would exclude ±2 cosmetic surgeries.
- Proposition 5.6 already gives |m_1| = |m_2| < 1/16 for a cosmetic pair, so Conjecture M′ is exactly the statement that cosmetic pairs sit outside the window.

**(c) Half-cosmetic knots.** By Corollary 5.8, det-1 torus knots satisfy the window condition on one side, Y_2 for mirrors and Y_{-2} (dual) for positive knots, but never on both.

> **Prediction (SPECULATIVE).** For a knot with Δ_K = 1, the traceless theory sits within 1/16 below the bottoms of both I(Y_2) and I^w(Y_2) only if it does not do so for Y_{-2}.

This can be tested for a Δ = 1 knot once its traceless spectrum and the spectra of Y_{±2} are computable. They need a numerical pillowcase for a non-Seifert example (Whitehead doubles, (−3,5,7) pretzel).

### 6.3 The "two-step filtration" question

- **Same bundle.** The singular configuration on (W′, S) gives a homotopy g_S with d g_S + g_S d = b∘a, but no exact triangle with one traceless copy exists for torus knots (Proposition 3.1). The pillowcase (τ_V^2) suggests a two-step filtration with two traceless pieces, one shifted in degree by an odd amount (SPECULATIVE).
- **Mixed bundles.** Single triangles, Conjecture T.

So the answer to "is there an exact triangle I(Y_2) → I(Y_{-2}) → (singular group)" is no for the same bundle and yes, conjecturally, with the bundle exchanged.

---

## 7. The structural explanation, precise statements, status, confidence

### 7.1 Proposed explanation of the 1/16

1. **The number.** The 1/16 is E_cap = 1/(4|S·S|), the energy of the minimal odd reducible on the disk bundle of the (−4)-sphere S = core(X_2) ∪ core(X_{-2}) ⊂ W′. This is the reducible of observation (i).
   - Under the double cover branched along S it is half of DLME's cap energy 1/8 on the (−2)-sphere of W^1_{-1}.
   - In the pillowcase, it is the area of the triangle cut out by L_2, the traceless circle and L_{-2}^w.
   - Via APS, it is ρ(L(4,1); γ_1) = 1 times the coefficient 1/2, divided by the 8 of d/8.
2. **Where it enters.** It enters the filtered theory in one place only: the third map of the bundle-exchanging distance-four triangle, whose level is 1/8 + E_cap = 3/16.
   - The vertex homotopies next to that map have level E_cap.
   - Without traceless interference, the mixed differences lie in a window of width E_cap: (1/8, 3/16].
   - No other map between Y_{±2} and (S^3, K)^tl moves the level by an odd multiple of 1/16 (§3.3, §4.3).
3. **Why the traceless representations obstruct.** They are the third vertex of these triangles.
   - The odd-bundle family and the singular family each fail on one face. Their sum fails only through b∘a, which is exactly the triangle-detection relation.
   - **The two failures the user observed are therefore complementary halves of one triangle.**
4. **Why the gap is not universal.**
   - The triangles compare *different* bundles on Y_2 and Y_{-2}.
   - The same-bundle difference adds an offset (§5.5) that no such triangle controls. That offset makes D negative for positive torus knots.
   - What the triangles do force is (Proposition 5.6): a cosmetic pair would have |ℓ(Y) − ℓ^w(Y)| < 1/16, with the traceless theory absorbing both minimisers at total cost below 1/16.

### 7.2 Statements and status

| statement | status | confidence |
|---|---|---|
| **A.** L_{-2} = τ_V^2(L_2), L_{-1} = τ_V(L_1); area of (L_2, V_{α_0}, L_{-2}) = (1 − 4α_0)^2/4, equal to the matching singular reducible energy; mixed triangle area 1/16 (§2) | VERIFIED | 95% |
| **B.** Caps on νS (§3.1), formulas (1.1)–(1.2), the level table of §4.3, and the rule third map = 1/8 + E_cap, vertex homotopies = E_cap, E_cap = 1/(8p) (§4.4) | VERIFIED as bookkeeping | 90% |
| **C.** Proposition 3.1: no same-bundle triangle with one traceless copy; the T(2,5) level contradiction | VERIFIED for torus knots with p < q ≤ 15, pq ≤ 60 | 90%; the residual risk is the grading normalisation of the singular theory |
| **D.** Conjecture T: the bundle-exchanging triangles with levels (0, 0, 3/16; −1/8, 1/16, 1/16) | PLAUSIBLE | 65% |
| **D′.** Evidence for D: rank identities (29 knots), level compatibility (58 instances), sharpness of 3/16 and 0, controls, 4_1 | VERIFIED computations | 90% that the computations are right |
| **E.** Theorem 5.2, Corollary 5.3, Proposition 5.6, Theorem 5.7, Corollary 5.8 | VERIFIED as deductions from D for perfect complexes; PLAUSIBLE with boundary depth | 85% given D |
| **F.** The examples with m = 1/16 (T̄(2,3), 4_1) are zero-energy absorptions at binary dihedral points; for T̄(2,3), m = 3/16 − 1/8 exactly | VERIFIED | 90% |
| **G.** Conjecture M′ (det K = 1 ⇒ m_1, m_2 > 1/16), which would exclude ±2 cosmetic pairs given D | SPECULATIVE | 30% |

### 7.3 The precise statement I propose

> **Theorem (conditional on Conjecture T; perfect complexes).** Let K ⊂ S^3 be a knot with no irreducible traceless representation sending λ to ±1. If S^3_2(K) ≅ S^3_{-2}(K) =: Y (orientation-preserving), then the traceless singular instanton homology of K absorbs the ℓ-minimisers of both I(Y) and I^w(Y), and
>   ℓ(I^tl(K)) < min(ℓ(Y), ℓ^w(Y)) ≤ max(ℓ(Y), ℓ^w(Y)) < ℓ(I^tl(K)) + 1/16.
> In particular, if the singular 2-handle map Y_2 → (S^3, K)^tl costs energy > 1/16 on the ℓ-minimiser of either bundle, then no such Y exists.
>
> The constant 1/16 is E_cap, the energy of the odd reducible on νS, which is the level of the third map minus 1/8.

**Status.** VERIFIED as a deduction from Conjecture T (PLAUSIBLE, 65%).

**What is missing.** For the cosmetic conjecture, the remaining input is the energy bound > 1/16 for absorption, or Conjecture M′. I could not supply it. The local model shows that it holds on negatively sloped branches of the character curve and fails on positively sloped ones.

**Overall confidence in the account: 70%.**

---

## Appendix: scripts (`gap16/triangle-code/`)

- **`tk.py`.** Torus-knot generators for Y_N in both bundles, with c = (3 + ρ)/16, CS and gradings, re-implemented from ell-1's formulas. It also computes the traceless representations and c^tl, CS^tl, gr^tl through the flat singular connections at common points, and checks consistency across all admissible N.
- **`spectra.py`.** Spectra of Y_{±1}, Y_{±2} (both bundles) and of the traceless theory.
- **`feas.py`.** Rank identities and level-compatible matchings for the triangles (I), (II), and for the same-bundle triangle.
- **`sharp.py`, `sharp2.py`.** Least feasible levels. `sharp.py` had a monotonicity error in its g-test and is superseded by `sharp2.py`, whose output is in `sharp2.out`.
- **`parity.py`.** Grading parities: untwisted, twisted (with integrality of the twisted gradings checked) and traceless.
- **`control.py`.** The DLME ±1 window as a control, and the rank tests that fail for the one-copy ±1 triangle and the same-bundle ±2 triangle.
- **`examples.py`, `window.py`, `ubound.py`.** The example table, forced absorption, the cosmetic window conditions of Corollary 5.8, and the vertex-B upper bounds.
- **`pillow.py`.** Dehn-twist flux, triangle areas, cap energies, and the APS check of c_γ = 1/4 − E_cap.
- **`fig8_tri.py`, `sfs_copy.py`.** Figure-eight spectra. `sfs_copy.py` is a copy of Seifert-1's `sfs.py`, read before use.
