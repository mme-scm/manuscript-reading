# The invariant ℓ for S³_{±2}(K): normalisations, levels, and where 1/16 comes from

Line of attack: the invariant ℓ itself. Labels: **VERIFIED** (proved here, computed exactly, or checked against a source), **PLAUSIBLE**, **SPECULATIVE**. The scripts are in `gap16/ell-code/`. They were written independently of the sibling write-up `gap16/pillowcase-1.md` (Pillowcase-1). Where the two overlap, the numbers agree exactly, and this is recorded below.

Notation:
- K ⊂ S³ is a knot, Y_r = S³_r(K), X_N is the trace of N-surgery, and K̄ is the mirror of K.
- W′ = (−X_2°) ∪_J X_{−2}° : Y_2 → Y_{−2}, with J ≅ S³.
- S ⊂ W′ is the sphere of square −4, νS its disc bundle, and ∂νS = L(4,1).
- W_H : Y_{−2} → Y_2 is the composite of the four meridional handle cobordisms through Y_{−1}, Y_0, Y_1.

---

## 0. Summary

1. **The 16 is the APS coefficient (Theorem A; VERIFIED).** Let Y be a rational homology sphere and α a nondegenerate irreducible flat connection. Measure α against a nondegenerate reducible reference γ: either θ, or the abelian flat ζ of the nontrivial bundle on Y_{±2}. Then
   f_γ(α) := CS~(α) − gr_γ(α)/8 = (h⁰(γ) − ρ(γ) + ρ(α))/16.
   Here ρ is the APS ρ-invariant of the adjoint flat bundle, in DLME's convention.
   - For the trivial bundle f(α) = (3 + ρ(α))/16, so ℓ(Y) = (3 + ρ_♯)/16, where ρ_♯ is the adjoint ρ-invariant of a realising generator.
   - This is checked exactly on DLME's Example 3.7: ρ = −73/15 and −97/15 give −7/60 and −13/60.
   - Consequently every value of ℓ, and every difference ℓ(Y_2) − ℓ(Y_{−2}), is a difference of adjoint ρ-invariants divided by 16.
2. **Explicit ℓ for Y_{±2} (§2; VERIFIED except where marked).**
   - The two central reducibles θ and χθ give the same f. So ℓ does not depend on which of them normalises CS and the grading.
   - The twist ι = ⊗χ has degree 4 and CS-shift 1/2, and it fixes f.
   - Orientation reversal: f_{−Y} = 3/8 − f_Y, hence ℓ(−Y) = 3/8 − ℓ⁺(Y). Here ℓ⁺ is the largest birth of an infinite bar.
   - The nontrivial bundle w is referenced to the abelian flat ζ, which has h⁰ = 1 and ρ(ζ) = −2σ(K) (VERIFIED for torus knots). This gives f^w = (1 + 2σ(K) + ρ(α))/16.
   - The absolute normalisation f^abs := ρ/16 makes every cobordism map, between either bundle, shift levels by the same rule.
3. **Level bookkeeping (Proposition B; VERIFIED as bookkeeping).** A count on (W, c, G) with b₁(W) = 0, fixed-limit index i₀ = codim − dim G, and middle ends M_j carrying limits γ_j shifts f^abs by
   −E + (i₀ + 3b⁺)/8 − (1/16) Σ_j (3 − h(γ_j) + ρ(M_j; γ_j)).
   Consequences:
   - Without middle ends, every shift lies in (1/8)ℤ − E, for either bundle.
   - An odd number of sixteenths enters only through a lens end L(4,·) on which the bundle is odd. There the order-four flat connection has ρ = ±1. This is the same fact as the energy 1/16 of the odd reducible on νS (observation (i)), and the same as the "half-integral relative grading" (D/8 with D ∈ 1/2 + ℤ) of the exterior W′∖νS.
4. **DLME's inequalities and their partners (§4).**
   - ℓ(Y_{−1}) < ℓ(Y_{−2}) and ℓ(Y_2) < ℓ(Y_1) come from handle cobordisms of degree 0 and level −η. The gap is η, the least energy of a counted instanton. It is not quantised: in examples it ranges from 1/1520 to about 0.2. No reducible energy and no D/8 enters.
   - **New upper bounds (PLAUSIBLE, given (H1) and standard neck-stretching):**
     - ℓ(Y_1) − ℓ(Y_{−1}) ≤ 1/4: DLME's third map, whose ℝP³ end contributes 1/8.
     - ℓ(Y_2) − ℓ(Y_{−2}) ≤ 1/8 and ℓ⁺(Y_2) − ℓ⁺(Y_{−2}) ≤ 1/8: the map H has b⁺ = 1, and every admissible lift is odd on the A_3 plumbing inside W_H, whose caps cost energy at least 1/4.
     - All three bounds are attained in examples.
   - Together with B, of level +1/8, the ±2 window is (−1/8, 1/8]. It is symmetric about 0. The ±1 window (1/8, 1/4] is not.
   - **This is the precise reason the ±2 comparison is hard.** The only known chain map Y_2 → Y_{−2} that is expected to be an isomorphism (B, or g_−g_+) has level +1/8 rather than −1/8, and the extra 1/4 is the forced μ(S) insertion.
5. **The claimed universal gap is false (VERIFIED by exact computation).** Here is ℓ(Y_2) − ℓ(Y_{−2}) for positive torus knots:

   | knot | T(2,3) | T(2,5) | T(2,7) | T(3,4) | T(3,5) | T(4,5) | T(5,24) |
   |---|---|---|---|---|---|---|---|
   | ℓ(Y_2) − ℓ(Y_{−2}) | 3/32 | 1/32 | −1/192 | 3/280 | −21/1768 | −29/792 | ≈ −0.109 |

   - For every negative torus knot with pq ≤ 120 (105 knots), the difference lies in [3/32, 1/8]. For 4_1 it is 1/10 (from Pillowcase-1).
   - The sibling Pillowcase-1 obtained the same values with independent code.
   - So no mechanism forces |ℓ(Y_2) − ℓ(Y_{−2})| ≥ 1/16 for all knots, and no one-sided version holds for all knots either.
6. **What the data do support (§6).**
   - Generators of Y_2 and Y_{−2} at a common representation of the knot group differ in f by exactly 1/8, for either bundle, and by 3/16 in the mixed case, in absolute normalisation.
   - In all 210 torus-knot cases (both chiralities, pq ≤ 120) the following hold:
     - (a) the twisted gap ℓ^w(Y_2) − ℓ^w(Y_{−2}) is at least 0.085;
     - (b) both mixed differences ℓ^abs(Y_2) − ℓ^{w,abs}(Y_{−2}) and ℓ^{w,abs}(Y_2) − ℓ^abs(Y_{−2}) lie in [1/16, 3/16], with both ends attained;
     - (c) the untwisted gap is at least 3/32 whenever σ(K) ≥ 0.
   - The mixed window [1/16, 3/16] is exactly the pair of levels (−1/16, +3/16) of the two odd lens-ended cobordisms W′∖νS and W_H∖A_3.
7. **Proposed explanation and conjectures (§7–§8).**
   - The number 1/16 is the APS bookkeeping of the order-four flat connection on L(4,1) for the odd bundle (ρ = ±1). It is also the energy of the odd cap on νS.
   - Same-bundle comparisons see only multiples of 1/8 up to energy.
   - Three precise conjectures, each of which excludes ±2 cosmetic pairs:
     - (U_σ) if σ(K) ≥ 0, then ℓ(Y_2) ≥ ℓ(Y_{−2}) + 1/16;
     - (W) ℓ^w(Y_2) ≥ ℓ^w(Y_{−2}) + 1/16;
     - (M) both mixed differences are at least 1/16.
   - All three are SPECULATIVE. Confidence is about 25%, 30% and 25% respectively; the main reason for doubt is that knots with Δ_K = 1 have balanced gradings, which torus knots lack.

---

## 1. Conventions

### 1.1 Manifolds and orientations (VERIFIED)
- Y_N = S³_N(K) = ∂X_N. Its filling slope is Nμ + λ, and H_1(Y_{±2}) = ℤ/2.
- Mirroring: S³_N(K̄) = −S³_{−N}(K).
- Examples, with Brieskorn spheres carrying their link orientation:
  - S³_{+1}(RHT) = −Σ(2,3,5) and S³_{−1}(RHT) = Σ(2,3,7);
  - S³_{+2}(RHT) = −S³/O*, where S³/O* = ∂(negative E_7) = S³_{−2}(LHT);
  - S³_{−2}(RHT) is Seifert fibred over S²(2,3,8).
- The orientation of S³_2(RHT) is checked twice: by a finite-group computation of ρ (§2.3) and by Chern–Simons values (§6).

### 1.2 Chern–Simons
- SU(2) normalisation throughout: cs(A) = (1/8π²)∫ tr(A dA + (2/3)A³).
- DLME use E(A) = CS~(α) − CS~(α′) − c²/4 along W : Y → Y′. Hence CS_DLME = −cs, where cs increases along ASD trajectories in the standard orientation.
- Check: CS_DLME(Σ(2,3,5)) = 1/120 and 49/120 (DLME, Example 3.7). Our formula gives 119/120 and 71/120 on −Σ(2,3,5) = Y_1(RHT), as it should (VERIFIED).
- The real lift is normalised by CS~(θ) = 0. Then CS~(χθ) ∈ 1/2 + ℤ. The reason: the reducible L ⊕ L⁻¹ on X_{−2}° with ⟨c_1(L), F⟩ = 1 has energy −c_1(L)² = 1/2 and runs from θ on S³ to χθ. On X_{+2}° the same Chern–Weil computation gives the same value mod 1 (VERIFIED).
- **Nontrivial bundle.** Use U(2) connections with a fixed determinant connection, modulo determinant-one gauge. This is DLME's convention for (W, c) with c ≠ 0. CS is then real-valued modulo ℤ. The SO(3) gauge group would reduce it only modulo 1/2, because tensoring with χ is not a determinant-one gauge transformation.
- SO(3) normalisation: the energy −p_1/4 equals c_2 on bundles that lift. Nothing in this note uses an SO(3) normalisation that differs from SU(2) by a factor.

### 1.3 Index and ρ conventions
- **Index formula** [DLME, eq. (index) in the proof of Lemma 5.6, for b₁(W) = 0]:
  ind(A) = 8E(A) − 3(1 + b⁺(W)) + (1/2) Σ_{ends N} (3 − h(γ_N) + ρ(N; γ_N)).
  - The sum runs over all ends N, each oriented as part of ∂W, and γ_N is the limit on N.
  - h = h⁰ + h¹.
  - ρ(N; γ) is the APS ρ-invariant of the adjoint flat bundle in DLME's convention, which is that of Pillowcase-1.
  - For a central limit the summand is 0. For an irreducible nondegenerate limit it is (3 + ρ)/2.
- **Explicit values of ρ** (VERIFIED by `spaceform.py`):

  | manifold | flat connection | ρ |
  |---|---|---|
  | L(4,1) = ∂(disc bundle of Euler number −4) | adjoint rotation by 2πk/4, k = 0, 1, 2, 3 | 0, 1, 2, 1 |
  | L(4,3) = ∂(A_3 plumbing) | k = 2 | −2 |
  | ℝP³ | any | 0 |
  | Σ(2,3,5) (link) | α, β | −73/15, −97/15 |
  | S³/O* (link) | natural | −14/3 |
  | S³/T* (link) | natural | −13/3 |

  For S³/G one has ρ_E = (1/|G|) Σ_{g≠1} cot(θ_1/2) cot(θ_2/2)(dim E − tr E(g)), with S³/G oriented as the link of ℂ²/G.
- **Checks of the index formula on caps** (VERIFIED):
  - The odd minimal reducible on νS has E = 1/16 and boundary k = 1, so ρ = 1. Its index is 8E − 3 + (3 − 1 + 1)/2 = −1, so its framed index is 0.
  - The even minimal reducible has E = 1/4, k = 2, ρ = 2, index 1 and framed index 2. This agrees with B-final, Lemma 1.2.
  - The minimal reducible on the A_3 plumbing has E = 1/4 and boundary k = 2 on L(4,3), with ρ = −2. Its index is −1 and its framed index 0.
- **Grading** [DLME §3]: gr(α̃) is the index on ℝ × Y from α̃ to θ, along the path class of the lift α̃.
  - The lift t·α̃ has gr + 8 and CS~ + 1.
  - The "d" in ℓ = inf_d (κ(d) − d/8) is this ℤ-valued grading of lifts.
  - The 1/8 is the ratio of the period of CS (one) to the period of the grading (eight).

---

## 2. ℓ for Y_{±2}, made explicit

### 2.1 The complex (VERIFIED unless marked)
- **Flat connections.** Since H_1(Y_{±2}) = ℤ/2, every abelian SU(2) representation is central. The reducibles are θ and χθ, where χθ sends μ ↦ −1. Both have h⁰ = 3 and h¹ = 0.
- **Generators.** C_*(Y_{±2}; F_2) is spanned by the irreducible flat connections, after holonomy perturbation, modulo SU(2) gauge.
- **Grading.** The ℤ/8 grading is gr mod 8, and the differential counts index-one trajectories.
- **d² = 0.**
  - By DLME's index additivity (Definition 5.4), a broken trajectory α → θ → β has index at least 1 + 3 + 1 = 5. So it is absent from the index-2 moduli spaces that prove d² = 0. PLAUSIBLE, and standard.
  - Invariance under metric and perturbation follows in the same way. This is DLME's remark in §1.2.2 and hypothesis (H1) of `statements.tex`.
- **The twist.** ι(α) = α ⊗ χ is a chain involution for χ-invariant perturbations (PLAUSIBLE: use functions of the adjoint holonomy).
  - On lifts it shifts (CS~, gr) by (1/2, 4).
  - ια ≇ α whenever α(λ) ≠ 1 (Pillowcase-1, §1.1: a fixed point of ι is binary dihedral, and these have λ ↦ 1).
  - On Y_{±2}, an irreducible α has α(λ) = α(μ)^{∓2}. If this were 1, then α(μ) = ±1 would be central and α abelian. So **every irreducible of Y_{±2} lies in an ι-pair** {α, ια}: gradings d and d + 4, CS differing by 1/2, equal f. Hence rank I(Y_{±2}) is even (VERIFIED, general; observed in all examples).

### 2.2 The IP-module and ℓ
- **The filtered complex.** Let C̃ be the ℤ-graded complex with generators the lifts α̃ = (α, n). Then gr(α̃) = gr_0(α) + 8n and CS~(α̃) = CS~_0(α) + n.
- **The IP-module.** F_r I_d is the degree-d homology of the subcomplex spanned by lifts with CS~ ≤ r, taken right-continuously. The periodicity is φ = multiplication by t.
- **The invariants.** κ(d) = inf{r : F_r I_d → I_d is nonzero} and ℓ = inf_d (κ(d) − d/8), following DLME, §2.
- **Reformulation (VERIFIED as algebra).** Put f(α) := CS~(α̃) − gr(α̃)/8. It does not depend on the lift.
  - f defines a filtration of the ℤ/8-graded complex C_*(Y), and the differential does not increase it.
  - κ(d) − d/8 is the smallest f-level at which a nonzero class of degree d is born.
  - So ℓ(Y) is the smallest birth of an infinite bar in the f-filtered barcode of I_*(Y; F_2), and ℓ(Y) = f(α) for some generator α.
  - If the differential vanishes, ℓ(Y) = min_α f(α). This is the case for all Seifert examples below, whose gradings all have the same parity.
- **The top of the spectrum.** Define ℓ⁺(Y) to be the largest birth of an infinite bar. If the differential vanishes, ℓ⁺(Y) = max_α f(α).

### 2.3 Theorem A (f is a ρ-invariant)
> **Theorem A (VERIFIED).** Let Y be a rational homology sphere and α a nondegenerate irreducible flat connection. Let γ be a nondegenerate reducible flat connection on the same bundle, used to normalise both CS~ (by CS~(γ) = 0) and the grading (by gr_γ(α̃) = ind(α̃ → γ)). Then
>   f_γ(α) = CS~(α̃) − gr_γ(α̃)/8 = (h⁰(γ) − ρ(γ) + ρ(α))/16.
> In particular f(α) = (3 + ρ(α))/16 for γ = θ.

*Proof.*
1. Take any W : S³ → Y with b₁(W) = 0 carrying a bundle that extends the one on Y. For a connection A on W from θ_{S³} to a nondegenerate limit x on Y, the index formula reads
   ind(A) = 8E(A) − 3(1 + b⁺) + (3 − h(x) + ρ(x))/2.  (∗)
2. Let A_γ run from θ to γ, and let B be a path on ℝ × Y from γ to the lift α̃.
   - DLME's additivity (Definition 5.4: add h⁰ of each intermediate limit) gives ind(A_γ # B) = ind(A_γ) + h⁰(γ) + ind(B).
   - The energy is E(A_γ # B) = E(A_γ) + CS~(γ) − CS~(α̃).
3. Apply (∗) to A_γ # B and to A_γ, and subtract:
   ind(γ → α̃) = 8(CS~(γ) − CS~(α̃)) + (ρ(α) − ρ(γ) − h⁰(γ))/2.
4. Let B̄ be the reverse path. Then B̄ # B is homotopic rel ends to the constant path at α̃, whose index is 0 because h(α) = 0. Gluing at γ adds h⁰(γ), so
   ind(α̃ → γ) = −h⁰(γ) − ind(γ → α̃).
5. Substituting 3 into 4 gives
   gr_γ(α̃) = 8(CS~(α̃) − CS~(γ)) − (h⁰(γ) + ρ(α) − ρ(γ))/2.
6. With CS~(γ) = 0, divide by 8 and subtract from CS~(α̃) to obtain the formula. ∎

Checks (VERIFIED):
- DLME, Example 3.7: Σ(2,3,5) with ρ = −73/15, −97/15 gives f = −7/60 and −13/60, which equal CS − gr/8 = 1/120 − 1/8 and 49/120 − 5/8.
- The finite-group ρ of S³/O* gives f(−S³/O*) = 23/48. This agrees with the Seifert formula on Y_2(RHT).
- Integrality gr ∈ ℤ holds for all 287,532 generators computed: untwisted and twisted, N = ±1, ±2, every T(p, q) with pq ≤ 120 (`integrality.py`). This tests ρ mod 2 against CS mod 1/8.
- The Fintushel–Stern grading formula agrees on Σ(p, q, pq+1) for five torus knots, up to their global shift of 3 (`fscheck.py`).

**Corollaries (VERIFIED).**
- (a) f(α) ≡ CS(α) (mod 1/8), and ι fixes f, since ad(α ⊗ χ) = ad α.
- (b) Normalising by χθ instead of θ changes nothing, because h⁰ = 3 and ρ(χθ) = ρ(trivial) = 0. So ℓ(Y_{±2}) is canonical.
- (c) ℓ(Y_2) − ℓ(Y_{−2}) = (ρ_♯(Y_2) − ρ_♯(Y_{−2}))/16. A gap of 1/16 is exactly a gap of 1 between adjoint ρ-invariants. **No index formula has to contain 1/16 for it to appear. It is the 1/2 in front of ρ divided by the 8 in d/8.**

### 2.4 Orientation reversal (VERIFIED)
- gr_{−Y}(α) = −3 − gr_Y(α) (from ind(α→θ) + 3 + ind(θ→α) = 0), CS_{−Y} = −CS_Y and ρ_{−Y} = −ρ_Y. Hence f_{−Y}(α) = 3/8 − f_Y(α).
- C_*(−Y) is the dual complex. Persistence duality over a field sends infinite bars [b, ∞) to [3/8 − b, ∞). So
  ℓ(−Y) = 3/8 − ℓ⁺(Y)  and  ℓ(S³_N(K̄)) = 3/8 − ℓ⁺(S³_{−N}(K)).
- **Consequence.** Both ℓ and ℓ⁺ are invariants. For a cosmetic pair both coincide, and they coincide for K̄ too. A statement about ℓ⁺(Y_{±2}(K)) is the same as a statement about ℓ(Y_{∓2}(K̄)).

### 2.5 The nontrivial bundle w (twisted theory)
- **Flat connections.**
  - The unique nonzero w ∈ H²(Y_{±2}; ℤ/2) supports exactly one reducible flat SO(3) connection, ζ. It sends μ to the rotation by π, and ad ζ = ℝ ⊕ ℝ_− ⊕ ℝ_−. It has h⁰ = 1 and h¹ = 0, the latter because the double cover is a rational homology sphere (VERIFIED).
  - In the pillowcase, ζ is the abelian point (a, b) = (1/4, 0). The twisted irreducibles are the points of the irreducible curve on L_N^w = {Na + b ∈ 1/2 + ℤ}.
- **Normalisation.** CS^w := CS − CS(ζ) mod 1, in the U(2) fixed-determinant theory, and gr^w := ind(· → ζ). By Theorem A:
  f^w(α) = (1 − ρ(ζ) + ρ(α))/16,  ρ(ζ) = 2ρ(χ) = −2σ(K).
  - ρ(χ) = −σ(K) is VERIFIED for torus knots with pq even, by the orbifold formula on both Y_2 and Y_{−2}. It is consistent with integrality for pq odd, and is the Casson–Gordon value (PLAUSIBLE in general).
  - So f^w = (1 + 2σ(K) + ρ(α))/16.
  - CS(ζ) = N/16 in DLME's sign, from the pillowcase formula at a = 1/4. Integrality of gr^w then holds for every twisted generator computed (VERIFIED).
- **Orientation.** f^w_{−Y} = 1/8 − f^w_Y, so ℓ^w(−Y) = 1/8 − ℓ^{w,+}(Y).
- **Absolute normalisation.** Put f^abs(α) := ρ(α)/16, that is, f − 3/16 untwisted and f^w − (1 + 2σ)/16 twisted. In this normalisation the rule of Proposition B is the same for every pair of bundles. Mixed comparisons below use it.
- **d² = 0 and invariance (PLAUSIBLE).** A trajectory broken at ζ has index at least 1 + h⁰(ζ) + 1 = 3. A continuation configuration through ζ has index at least 1 + 1 − 1 + 1 + 1 = 3. So neither occurs in the moduli spaces of index at most 2 that define d, d² and the continuation maps.
- **Caveat (VERIFIED for torus knots).**
  - rank I^w(Y_{−2}) − rank I^w(Y_2) = |σ(K)|: for instance 3 against 1 for T(2,3), and 34 against 26 for T(4,5).
  - In these examples rank I^w(Y_2) = rank I(Y_1) + σ(K)/2 and rank I^w(Y_{−2}) = rank I(Y_1) − σ(K)/2. For T(2,3): 2 − 1 = 1 and 2 + 1 = 3. So the twisted theories of ±2 surgery have different ranks unless σ = 0, which is the case when Δ_K = 1.
  - Twisted handle maps are therefore not isomorphisms, and the twisted theory is linked to the untwisted one only through cobordisms that are odd on one end.

---

## 3. Level bookkeeping for cobordism maps

> **Proposition B (VERIFIED; it is the index formula of §1.3 rearranged).** Let (W, c) be a cobordism Y → Y′ between rational homology spheres with b₁(W) = 0, possibly with middle ends M_j. Let G be a family of metrics and z an insertion of codimension codim. Let A be a counted instanton: irreducible limits α on Y and β on Y′, limits γ_j on M_j, and index i₀ = codim − dim G. Then
>   f^abs(β) − f^abs(α) = −E(A) + (i₀ + 3b⁺(W))/8 − (1/16) Σ_j (3 − h(γ_j) + ρ(M_j; γ_j)),
> with f^abs = ρ/16 as in §2.5 and each M_j oriented as part of ∂W. If the map is injective on homology, then ℓ^abs(Y′) ≤ ℓ^abs(Y) + (sup of the right-hand side). If it is surjective, the same bound holds for ℓ⁺.

*Proof.*
- Put the end terms (3 − ρ(α))/2 for −Y and (3 + ρ(β))/2 for Y′ into ind(A) = 8E − 3(1 + b⁺) + Σ(…)/2, and divide by 8.
- The statement about ℓ⁺: a surjection maps the subspace V_r of classes born by level r onto a subspace born by r + L.
- In the θ-normalisation of both ends this is DLME's L − D/8 = −η + (i₀ + 3b⁺)/8 (Proposition 3.4 and Lemma 2.7). For example, g₁ has i₀ = −1, b⁺ = 0 and level −1/8 − η. ∎

**Corollary B1 (where sixteenths can and cannot enter; VERIFIED).**
- **Same-bundle maps.** For maps between the same bundle on Y_2 and Y_{−2}, or between different bundles in absolute normalisation, built on cobordisms without middle ends, the shift lies in (1/8)ℤ − E(A). An odd multiple of 1/16 can enter only through the energy.
- **Lens middle end.** A middle end L(4,·) carrying the odd order-four flat connection γ_1 (h = 1, ρ = ±1) contributes (3 − 1 ± 1)/16, which is 1/16 or 3/16. The even flat γ_0 (ρ = ±2) contributes 0 or 1/4, and ℝP³ contributes 1/8.
- **Half-integral degree.** The same fact, read as a degree: the exterior W′∖νS with odd bundle has "D/8" with D ∈ 1/2 + ℤ. So half-integral relative gradings occur exactly at the odd lens face, and nowhere else between Y_2 and Y_{−2}.
- **Reference corrections.** Between the θ-normalised and ζ-normalised theories the reference offset is (3 − (1 + 2σ))/16 = (1 − σ)/8 ∈ (1/8)ℤ, since σ is even. So no sixteenth comes from normalisation either.

**Table 3.1 (energies of reducibles; VERIFIED).** Here m and n are the values of 2x − c on the two generators, and the parities are those of c.

| piece | lattice | reducible energies −(2x − c)²/4 |
|---|---|---|
| W′ | (−2) ⊕ (−2) on F_l, F_r | (m² + n²)/8: lift even on both ends gives {0, 1/2, 1, …}; odd on one end gives {1/8, 5/8, …}; odd on both gives {1/4, 5/4, …} |
| νS (Euler −4) | (−4) | c(S) even: j²/4, so {0, 1/4, 1, …}; c(S) odd: (2j+1)²/16, so **{1/16, 9/16, 25/16, …}** |
| handle cobordism Y_{−2}→Y_{−1} or Y_1→Y_2 | (−2) | m²/8; the reducible from θ to χθ has energy 1/2 |
| ℝP³ cap (Euler −2) | (−2) | c odd: (2j+1)²/8, minimum 1/8 (DLME, Lemma 5.7) |
| A_3 cap inside W_H | A_3 | (1/16) vᵀ(−4Q⁻¹)v. Every lift that is trivial on Y_{±2} and odd on F_0 is odd on R_1 and R_3, which forces **minimum 1/4** with boundary k = 2, and no flat caps |

The energy 1/16 occurs only on νS with c(S) odd and on its complement. Its index partner is ρ(L(4,1); γ_1) = 1. These are one fact seen from the two sides of ∂νS: the odd cap has framed index 8E − 1/2 = 0 exactly when E = 1/16.

---

## 4. DLME's inequalities for ±2, their partners, and the windows

### 4.1 ℓ(Y_{−1}) < ℓ(Y_{−2}) and ℓ(Y_2) < ℓ(Y_1)
**The cobordisms.**
- W_{−2→−1}: attach a (−1)-framed handle along the meridian of K. By slam-dunk, −2 − 1/(−1) = −1.
- W_{1→2}: framing −1, since 1 − 1/(−1) = 2.
- The linking matrices are [[−2,1],[1,−1]] and [[1,1],[1,−1]]. The orthogonal complement of the trace class is spanned by Σ = (1,2), respectively (1,−1), and Σ² = −2.
- So H_2(W) = ℤΣ with form (−2), b⁺ = 0 and π_1 = 1 (VERIFIED).

**The maps.**
- The exact triangles for the triads (∞, −2, −1) and (∞, 1, 2), which have Δ = 1 pairwise, together with I(S³) = 0, make W_* an isomorphism over F_2. This is hypothesis (H1).
- For c = 0, or any lift trivial on the ends, D = 0 and L = −η(W). So L − D/8 = −η and ℓ(Y_{−1}) ≤ ℓ(Y_{−2}) − η and ℓ(Y_2) ≤ ℓ(Y_1) − η.

**Exact size of the gap (VERIFIED).**
- The gap is η(W), the least energy of a counted instanton on a simply connected negative-definite cobordism. No reducible energy contributes, and neither does D/8, since D = 0. The reducible θ ↔ χθ of energy 1/2 never enters irreducible counts.
- In ρ-language: ρ_♯(Y_{−1}) ≤ ρ_♯(Y_{−2}) − 16η.
- The gap is not quantised. The table below lists ℓ(Y_{−2}) − ℓ(Y_{−1}) and ℓ(Y_1) − ℓ(Y_2) (`gaps.py`).

| K | T(2,3) | T(2,5) | T(2,7) | T(3,5) | T(3,7) | T̄(2,3) | T̄(3,5) |
|---|---|---|---|---|---|---|---|
| ℓ(Y_{−2}) − ℓ(Y_{−1}) | 25/224 | 27/176 | 169/960 | 49/272 | 50/253 | 9/80 | 7/104 |
| ℓ(Y_1) − ℓ(Y_2) | 1/80 | 1/288 | 1/624 | 1/728 | **1/1520** | 9/224 | 1/17 |

### 4.2 Partners (upper bounds)
**Downward maps (PLAUSIBLE).**
- In the triads (S³, Y_1, Y_2) and (S³, Y_{−2}, Y_{−1}), triangle detection with C(S³) = 0 makes the g-map on the composite (−X_2°) ∪_{S³} X_1°, respectively (−X_{−1}°) ∪_{S³} X_{−2}°, a homotopy inverse of the handle map. These composites have b⁺ = 1 and one parameter, so i₀ = −1.
- Level 1/4 − η, hence ℓ(Y_1) < ℓ(Y_2) + 1/4 and ℓ(Y_{−2}) < ℓ(Y_{−1}) + 1/4.
- This holds in all examples: the gaps lie in (0, 0.2).

**The ±1 window (PLAUSIBLE, given DLME §5).**
- DLME's third map f_2 = (X, ĉ)_* : Y_{−1} → Y_1 is a homotopy inverse of g₁ when Y = S³. Here b⁺(X) = 1 and the middle end ℝP³ carries the abelian limit (h = 1, ρ = 0).
- By Proposition B its level is 3/8 − 1/8 − η = 1/4 − η. So
  1/8 + η(g₁) ≤ ℓ(Y_1) − ℓ(Y_{−1}) ≤ 1/4 − η(f_2),
  where η(g₁) > 0 (DLME) but η(f_2) ≥ 0 may vanish, because π_1(X) ≠ 1.
- The upper end is attained: exactly 1/4 for T̄(3,5) and T̄(3,7).
- The extremal configuration is a projectively flat connection on X. These exist although no flat SU(2) connection does: π_1(X) = π_1(S³∖K)/⟨⟨μλ, μ⁻¹λ⟩⟩ forces μ ↦ rotation by π in SO(3). So they come from traceless representations with λ ↦ ±μ, and the Y_{±1} ends are an χ-pair.
- For T(3,5) these are exactly the top generators: (1/4, 3/4) on the arc (1,3) of Y_1, and (1/4, 1/4) on the arc (2,2) of Y_{−1}, the χ-image (VERIFIED).

**The ±2 window (PLAUSIBLE, given (H1) and standard neck-stretching compactness).**
- **Upper end.** H = (W_H, c_H)_* is an F_2-isomorphism with b⁺ = 1, so its level is 3/8 − η_H.
  - W_H contains the A_3 plumbing on R_1, R_2, R_3. Every admissible lift is odd on R_1 and R_3, so by Table 3.1 every cap on A_3 has energy at least 1/4: the reducibles have at least 1/4 with the even boundary flat, at least 1/2 with central boundary, and irreducible caps lie in the same energy cosets.
  - Stretching ∂A_3 = L(4,3) gives η_H ≥ 1/4 − o(1). Since each metric gives an IP-morphism inducing the same isomorphism,
    ℓ(Y_2) ≤ ℓ(Y_{−2}) + 1/8,  and, for the mirror, ℓ⁺(Y_2) ≤ ℓ⁺(Y_{−2}) + 1/8.
  - Equivalently, the "third map" (X_{−2,2}, γ_0) has middle term (3 − 1 + 2)/16 = 1/4 and level 3/8 − 1/4 = 1/8.
  - Equality occurs at the common traceless representations (λ ↦ −1), where the exterior is flat and the gap is exactly 1/8 (§6.3).
- **Lower end.** If B is an F_2-isomorphism (Conjecture C of B-final), then ℓ(Y_{−2}) ≤ ℓ(Y_2) + 1/8 − η_B with η_B > 0, because W′ is simply connected. So
  −1/8 < ℓ(Y_2) − ℓ(Y_{−2}) ≤ 1/8.
- **Data.** dmin := ℓ(Y_2) − ℓ(Y_{−2}) lies in [−0.1087, 3/32] for positive torus knots and in [3/32, 1/8] for negative ones. dmax := ℓ⁺(Y_2) − ℓ⁺(Y_{−2}) lies in [3/32, 1/8], respectively [−0.1087, 3/32]. Both windows hold, and 1/8 is attained.

**Why ±2 is harder than ±1 (the precise statement).**
- Both windows have upper end equal to the level of the "third map": 1/4 at ±1 (ℝP³ term 1/8) and 1/8 at ±2 (L(4,1)/γ_0 term 1/4).
- Their lower ends are the levels of the g-type chain maps: −1/8 at ±1 (g₁) and +1/8 at ±2 (B).
- The ±1 window therefore excludes 0 and the ±2 window does not. The difference of 1/4 between −1/8 and +1/8 is the codimension-two insertion μ(S). It is forced, because of flat L(4,1) caps when c(S) is even (B-final; T5, §3.3).
- A chain map Y_2 → Y_{−2} of level −1/16 would give the window [1/16, 1/8] and exclude cosmetic pairs. **The data show that no such injective map exists for all knots**: for T(2,7), ℓ(Y_2) − ℓ(Y_{−2}) = −1/192.

---

## 5. Every known map between Y_2 and Y_{−2}, and why each falls short

Levels are in the absolute normalisation: the supremum over counted instantons of the shift in Proposition B. For same-bundle maps this coincides with DLME's L − D/8. Degrees are given modulo 8, for the lifts named.

| map | cobordism, family, insertion | b⁺ | i₀ | middle term | level | chain map? | F_2-iso? | resulting inequality | why it falls short |
|---|---|---|---|---|---|---|---|---|---|
| H = handle maps Y_{−2}→Y_{−1}→Y_0→Y_1→Y_2 | W_H, c_H² = 0, degree −3 | 1 | 0 | none (A_3 caps cost ≥ 1/4) | 3/8 − η_H ≤ 1/8 | yes | yes (H1) | ℓ(Y_2) ≤ ℓ(Y_{−2}) + 1/8 | upper bound only; the reverse direction is needed |
| downward Y_2→Y_1, then g₁, then Y_{−1}→Y_{−2} | two g-maps with b⁺ = 1, and DLME's g₁ | — | — | — | 1/4 − 1/8 + 1/4 = 3/8 | yes | yes (P) | ℓ(Y_{−2}) < ℓ(Y_2) + 3/8 | positive level |
| B | W′, interval from J to L(4,1), μ(S), degree −1 | 0 | +1 | none | +1/8 − η_B | P (B-final, Theorem A) | conjectured (B-final, Conj. C) | ℓ(Y_{−2}) < ℓ(Y_2) + 1/8 | level +1/8; it needs η_B > 1/8, which is false for some knots (T(2,7)) |
| g_−ϑg_+ | W′ # S²×S², square of metrics | 1 | −2 | none | +1/8 − η | P | conjectured | the same | the same |
| W′_* (rigid) | W′ | 0 | 0 | none | −η | yes | **zero**: it is ≃ 0 by stretching J | none | it vanishes |
| interval on W′, c(S) even, no insertion | W′ | 0 | −1 | none | −1/8 − η | **no**: flat caps on νS with central boundary give uncancelled L(4,1) faces (T5, §3.3) | — | — | not a chain map |
| (X_{2,−2}, γ_0) | W′∖νS | 0 | 0 | −L(4,1), ρ = −2: 0 | −η | yes | ≃ 0 (B-final, Thm A(e)) | none | null-homotopic |
| interval on W′, c(S) odd (mixed) | W′, pairs c and c + PD(S) | 0 | −1 | none | −1/8 − η | P, if the two lens faces cancel | **no in general**: rank I^w ≠ rank I when σ ≠ 0, and the inequality it would give fails for T̄(2,3) (m₂ = 1/16 < 1/8) | ℓ^{w,abs}(Y_{−2}) ≤ ℓ^abs(Y_2) − 1/8 if injective | not injective |
| (X_{2,−2}, γ_1), odd | W′∖νS | 0 | 0 | −L(4,1), ρ = −1: **1/16** | **−1/16 − η** | yes | ≃ 0: it is the lens face of the odd interval, whose J-face is empty | none | null-homotopic |
| (X_{−2,2}, γ_0), even third map | W_H∖A_3 | 1 | 0 | L(4,1), ρ = 2: 1/4 | 1/8 − η | P | ≃ H (T5, P) | ℓ(Y_2) ≤ ℓ(Y_{−2}) + 1/8 | wrong direction |
| (X_{−2,2}, γ_1), odd third map | W_H∖A_3, odd on one end | 1 | 0 | L(4,1), ρ = 1: 3/16 | 3/16 − η | P | unknown | mixed differences ≤ 3/16 | wrong direction |
| orbifold family, traceless along S | (W′, S) singular | 0 | −1 | — | −1/8 − η downstairs | **no**: the J-face runs through C(S³, K)^♮ ≠ 0, the irreducible traceless representations (user; Pillowcase-1, §7) | — | — | not a chain map |

**Reading of the table (VERIFIED as bookkeeping).**
- Every chain map that is known or expected to be an isomorphism has a priori level +1/8 (B, g_−g_+) or +3/8 (the downward composite) in the direction Y_2 → Y_{−2}, and level at most +1/8 in the direction Y_{−2} → Y_2 (H). These give the symmetric window of §4.2.
- The maps with negative level from Y_2 to Y_{−2} are of two kinds.
  - Not chain maps: the even interval without insertion, and the orbifold family.
  - Null-homotopic: W′_*, and the lens-ended exteriors (X_{2,−2}, γ), which are faces of families whose J-face is empty.
  - The one exception is the mixed odd interval, which is not injective in general.
- **The only place an odd sixteenth appears in any level is the odd lens end: the null-homotopic −1/16 map and the mixed third map at 3/16.**

---

## 6. Examples: torus knots and the figure-eight

### 6.1 Method (VERIFIED)
- **Generators.** The irreducible flat connections of Y_N(T_{p,q}) are the points of the irreducible arcs (k, l) on L_N, or on L_N^w in the twisted case.
- **Chern–Simons.** cs = pq(a² − a₀²) − Na², and CS_DLME = −cs. This reproduces CS for Σ(2,3,5) and Σ(2,3,7).
- **ρ.** ρ = 3 sgn(e) − 2[s(k; p, q) + s(l; q, p) + s(2am; pq − N, −1)], with s(l; a, B) = (2/a) Σ_j cot(πj/a) cot(πBj/a) sin²(πlj/a). This is the orbifold signature formula on the mapping cylinder of the Seifert fibration.
- **Choice of local data.** The cone-point data B_i = (q mod p, p mod q, −1) are singled out among 16 candidates by integrality of all gradings, for N ∈ {±1, ±2, ±3} and eight torus knots (`run_checks.py`).
- **Independent checks of ρ.**
  - Finite-group ρ on S³/I* (DLME Example 3.7) and S³/O* (Y_2(RHT)).
  - Fintushel–Stern gradings for Σ(p, q, pq+1), five knots (`fscheck.py`).
  - DLME's inequalities hold in all cases (`ellcmp.py`).
- **Agreement with Pillowcase-1.** Their independent code gives the same numbers in every overlapping case.
- **Differentials.** All gradings on Y_2 are even and all on Y_{−2} are odd, untwisted and twisted. So the differentials vanish, ℓ = min f and ℓ⁺ = max f.

### 6.2 Untwisted values (VERIFIED)

| K | ℓ(Y_{−2}) | ℓ(Y_{−1}) | ℓ(Y_1) | ℓ(Y_2) | ℓ(Y_2) − ℓ(Y_{−2}) |
|---|---|---|---|---|---|
| T(2,3) | 37/96 | 23/84 | 59/120 | 23/48 | 3/32 |
| T̄(2,3) | −5/48 | −13/60 | 5/168 | −1/96 | 3/32 |
| T(2,5) | 37/80 | 17/55 | 179/360 | 79/160 | **1/32** |
| T̄(2,5) | −59/160 | −41/90 | −91/440 | −61/240 | 11/96 |
| T(2,7) | 225/448 | 137/420 | 363/728 | 167/336 | **−1/192** |
| T̄(2,7) | −209/336 | −255/364 | −379/840 | −225/448 | 23/192 |
| T(3,4) | 163/336 | 199/624 | 263/528 | 119/240 | **3/280** |
| T̄(3,4) | −67/120 | −169/264 | −61/156 | −37/84 | 33/280 |
| T(3,5) | 1039/2040 | 79/240 | 419/840 | 97/195 | **−21/1768** |
| T̄(3,5) | −1169/1560 | −49/60 | −17/30 | −319/510 | 219/1768 |
| T(4,5) | 471/880 | 571/1680 | 759/1520 | 359/720 | **−29/792** |
| T̄(4,5) | −89/80 | −1781/1520 | −1549/1680 | −79/80 | 1/8 |

Over all T(p, q) with pq ≤ 120 (105 knots and their mirrors, `conjB.py` and `data_table.txt`):
- dmin = ℓ(Y_2) − ℓ(Y_{−2}) ∈ [−0.1087, 3/32] for positive torus knots and ∈ [3/32, 1/8] for negative ones.
- For each knot, max(dmin, dmax) ∈ [3/32, 1/8], with the minimum 3/32 at the trefoil.
- 4_1: 1/10. This is taken from Pillowcase-1 and not recomputed here; it is consistent with amphichirality, ℓ(Y_{−2}) = 3/8 − ℓ(Y_2).

### 6.3 Common representations (VERIFIED in all cases)
A representation of the knot group that defines generators on both sides gives a fixed gap in absolute normalisation:

| pair of bundles | common points in the pillowcase | gap f(Y_2) − f(Y_{−2}) | explanation by Proposition B (flat exterior, E = 0) |
|---|---|---|---|
| untwisted / untwisted | (1/4, 1/2): traceless, λ ↦ −1 | **1/8** | X_{−2,2}: 3/8 − (3 − 1 + 2)/16 |
| twisted / twisted | (1/4, 0): traceless, λ ↦ +1 | **1/8** | the same, γ_0 |
| mixed | (1/8, ·), (3/8, ·) | **3/16** | 3/8 − (3 − 1 + 1)/16, with γ_1 |

- In every case i₀ = 0 for the flat connection, as these numbers require. For ±1 the analogous projectively flat connections give exactly the upper end 1/4 of the window (§4.2).
- The difference between the mixed and the same-bundle gaps is **3/16 − 1/8 = 1/16 = ρ(γ_0)/16 − ρ(γ_1)/16**.

### 6.4 Twisted and mixed differences (VERIFIED for these knots; `twistedw.py`, `windows.py`, `mixedwide.py`)
- **Twisted.** ℓ^w(Y_2) − ℓ^w(Y_{−2}) ∈ [0.085, 0.375] in all 210 cases. For positive torus knots it is about 1/4 to 3/8, reflecting rank I^w(Y_{−2}) − rank I^w(Y_2) = |σ|. For negative ones it is about 1/8.
- **Mixed (absolute).**
  - m₁ = ℓ^abs(Y_2) − ℓ^{w,abs}(Y_{−2}) ∈ [0.0854, 3/16].
  - m₂ = ℓ^{w,abs}(Y_2) − ℓ^abs(Y_{−2}) ∈ [1/16, 3/16].
  - The value 1/16 is attained by m₂ for T̄(2,3), and 3/16 by m₁ for T(2,3) and by m₂ for T(2,5).
  - For T̄(2,q), m₂ = (2k − 1)/(16k) with q = 2k + 1, which tends to 1/8.
- **Identity.** m₁ + m₂ = (untwisted gap) + (twisted gap).

---

## 7. Where 1/16 comes from: proposed structural explanation

1. **Sixteenths are intrinsic to ℓ (Theorem A; VERIFIED).**
   - In the index formula, ρ appears with coefficient 1/2 next to 8E. Hence CS − gr/8 = (3 + ρ)/16.
   - Every ℓ-value is (3 + ρ_♯)/16, and every difference of ℓ-values is a difference of adjoint ρ-invariants divided by 16.
   - "No 1/16 in the formulas" is therefore only apparent: the 1/16 is (1/2)·(1/8).
2. **Same-bundle comparisons move only in eighths, up to energy (Corollary B1; VERIFIED).**
   - Cobordism and family maps without middle ends change f by (i₀ + 3b⁺)/8 − E.
   - Lens middle ends contribute (3 − h + ρ)/16, and this is an odd multiple of 1/16 exactly when the bundle restricted to L(4,·) is odd. Then the limit is the order-four flat connection γ_1 with ρ = ±1.
   - Equivalently, the minimal odd reducible on νS has energy 1/16 (observation (i)): its framed index 8E − 1/2 vanishes only at E = 1/16.
   - Equivalently again, the exterior W′∖νS with odd bundle has half-integral D. Nothing else produces an odd sixteenth:
     - central reducibles: CS(χθ) = 1/2, and ι fixes f;
     - degrees D: integers;
     - reference offsets: (1 − σ)/8.
3. **The pillowcase form (Pillowcase-1; here a consequence of 1 and 2).**
   - On the irreducible curve, f(Y_N) = Φ + (3 sgn N − N)/16 + N(α − 1/4)² + Maslov term. At N = ±2 the slope term is ±(1/16 + 2δ²).
   - At a common representation both terms meet, and the difference is exactly the level 1/8 of the flat exterior X_{−2,2} with its L(4,1)/γ_0 end (§6.3).
   - So the "±1/16 about Φ" of Pillowcase-1 and the "1/8 = 3/8 − 1/4" of Proposition B are the same identity.
   - In Pillowcase-1's split, the 1/16 itself is (3 − 2)/16. Numerically it is also half the area of each bigon between L_2 and L_{−2}, which is 1/8 for the area form dα∧dβ. This last remark is numerology (SPECULATIVE).
4. **Why there is no universal gap.**
   - Same-bundle gaps are differences of ρ-invariants of different representations. Only common representations are rigidly separated, by 1/8.
   - The generators realising ℓ can sit far from the common points: near the bifurcation points of R*(K) from the reducible arc, at roots of Δ_K on the unit circle. There the separation is arithmetic and can have either sign. Positive torus knots show this.
   - The window analysis (§4.2) is the cobordism-theoretic shadow of this. The available chain maps confine ℓ(Y_2) − ℓ(Y_{−2}) to (−1/8, 1/8], a window symmetric about 0.
5. **What the user's 1/16 most plausibly is.**
   - It is the level −1/16 of the odd b⁺ = 0 lens-ended exterior (X_{2,−2}, γ_1) (VERIFIED as bookkeeping).
   - Numerically this is half of −1/8, the level of DLME's b⁺ = 0 exterior X̄ with ℝP³ end in the lifted distance-two configuration (observation (iii): 1/8 = 2·1/16). I have not proved that levels halve under the branched cover; ρ of a pulled-back flat bundle is not twice ρ downstairs (SPECULATIVE).
   - As a chain map this exterior is null-homotopic: it is the lens face of the odd family, whose J-face is empty. The family itself has level −1/8 but is not injective in general.
   - The mixed odd third map has level 3/16. In all 210 examples the two mixed differences fill exactly the window [1/16, 3/16] cut out by these two lens-ended exteriors. That window excludes 0, and would exclude cosmetic pairs (§8, M).
   - In the cover, the failure is the middle complex C(Σ_2(K))^{⊕2}, which is traceless representations downstairs (user; Pillowcase-1, §7).

---

## 8. Precise statements, status, confidence

**Theorems (proved or computed here).**
- **A. f via ρ.** f_γ(α) = (h⁰(γ) − ρ(γ) + ρ(α))/16. Hence ℓ(Y) = (3 + ρ_♯)/16, and ℓ(−Y) = 3/8 − ℓ⁺(Y). Twisted: f^w = (1 + 2σ + ρ)/16, and ℓ^w(−Y) = 1/8 − ℓ^{w,+}(Y).
  VERIFIED: proof from DLME's index formula and additivity, plus exact checks. Confidence 97%.
- **B. Level bookkeeping and Corollary B1.**
  VERIFIED: bookkeeping. Confidence 97%.
- **C. Windows.**
  - 1/8 < ℓ(Y_1) − ℓ(Y_{−1}) ≤ 1/4.
  - ℓ(Y_2) − ℓ(Y_{−2}) ≤ 1/8 and ℓ⁺(Y_2) − ℓ⁺(Y_{−2}) ≤ 1/8. These need only (H1) and neck-stretching along ∂A_3.
  - ℓ(Y_2) − ℓ(Y_{−2}) > −1/8, if B is an F_2-isomorphism.
  - All endpoints are attained or approached in examples.
  PLAUSIBLE: standard analysis, consistent with all 210 examples. Confidence 85% for the upper ends and 70% for the lower end at ±2.
- **D. Counterexamples.**
  - |ℓ(Y_2) − ℓ(Y_{−2})| ≥ 1/16 is false for T(2,5) (1/32), T(2,7) (−1/192), T(3,4) (3/280) and T(3,5) (−21/1768), among others.
  - Neither one-sided inequality holds for all knots.
  VERIFIED by exact computation, agreeing with Pillowcase-1. Confidence 92%; the residual risk is a different normalisation of ℓ for Y_{±2} on the user's side.
- **E. Common representations.** Same-bundle gap 1/8; mixed gap 3/16 in absolute normalisation.
  VERIFIED in all examples, and explained by Proposition B for flat exteriors of index 0. Confidence 85% that this holds for all knots, conditional on the index being 0, which is a transversality statement for the flat exterior.

**Conjectures. Each implies that S³_2(K) ≇ S³_{−2}(K) for every nontrivial K. All are SPECULATIVE.**
- **(U_σ)** If σ(K) ≥ 0, in particular if Δ_K = 1, then ℓ(S³_2(K)) ≥ ℓ(S³_{−2}(K)) + 1/16.
  - Evidence: all 105 negative torus knots with pq ≤ 120 (gap in [3/32, 1/8]); 4_1 (1/10); T(2,3) as well.
  - No counterexample is known with σ ≥ 0.
  - For Δ_K = 1 it applies to both K and K̄, giving ℓ(Y_2) − ℓ(Y_{−2}) ≥ 1/16 and ℓ⁺(Y_2) − ℓ⁺(Y_{−2}) ≥ 1/16. Both are 0 for a cosmetic pair.
  - Mechanism: none proved. For negative torus knots, ℓ is realised near the traceless line, where the common-representation gap 1/8 is degraded by at most 1/(4(s − 2)) on a branch of slope s (Pillowcase-1, §6.4).
  - Confidence 25%. The main doubt: a cosmetic candidate has dim I_j(Y_2) independent of j (`statements.tex`, Corollary 1.4), whereas every torus-knot example is concentrated in one parity. So torus knots are weak evidence for Δ_K = 1.
- **(U′)** For every knot K, max(ℓ(Y_2) − ℓ(Y_{−2}), ℓ⁺(Y_2) − ℓ⁺(Y_{−2})) ≥ 1/16. Equivalently: K or K̄ satisfies ℓ(Y_2) ≥ ℓ(Y_{−2}) + 1/16.
  - Evidence: at least 3/32 in all 210 cases, and 1/10 for 4_1.
  - Confidence 30%.
- **(W, twisted)** ℓ^w(S³_2(K)) ≥ ℓ^w(S³_{−2}(K)) + 1/16, in either consistent normalisation of the twisted theory.
  - Evidence: at least 0.085 in all 210 cases.
  - Caveats:
    - invariance of the twisted irreducible theory with its abelian reducible ζ (PLAUSIBLE by the index count of §2.5);
    - for σ ≠ 0 the two sides have different ranks.
  - Confidence 30%.
- **(M, mixed)** ℓ^abs(Y_2) − ℓ^{w,abs}(Y_{−2}) ≥ 1/16 and ℓ^{w,abs}(Y_2) − ℓ^abs(Y_{−2}) ≥ 1/16.
  - For a cosmetic pair the two left-hand sides are negatives of each other, which is a contradiction.
  - Evidence: [1/16, 3/16] in all 210 cases, sharp at T̄(2,3).
  - Mechanism: the lower end is the level of the odd lens-ended exterior (X_{2,−2}, γ_1), but that map is null-homotopic, so a proof needs another map with the same level.
  - Confidence 25%.

**Open questions that would decide the conjectures.**
1. **(Toward M.)** In the fixed-determinant theory, (L(4,1), odd w) has two odd flat connections, γ_1 = L_0 ⊕ L_1 and γ_1′ = γ_1 ⊗ L_2. Both have ρ = ±1.
   - The minimal cap (energy 1/16) bounds γ_1. The cap bounding γ_1′ has energy 9/16 and framed index 4.
   - So only the γ_1-exterior is forced to be null-homotopic.
   - Question: is the γ_1′-exterior on W′∖νS, of level −1/16, a chain map up to the lens-neck corrections, and is it injective I^w(Y_2) → I(Y_{−2})? (SPECULATIVE.)
   - A yes in both directions would prove (M), hence the ±2 cosmetic conjecture.
2. **(Toward U_σ, W.)** Compute ℓ(Y_{±2}) for one knot with Δ_K = 1, for instance a Whitehead double or the (−3,5,7) pretzel knot. This needs a numerical pillowcase together with Pillowcase-1's formula f = Φ ± (1/16 + 2δ²) and its Maslov terms. Torus knots cannot test the balanced-grading regime of cosmetic candidates.
3. **(Toward E.)** Prove that the flat connection on X_{∓2,±2} at a common representation has index 0, that is, h¹ = h⁺ for the twisted cohomology. That would make the common-representation gaps 1/8 and 3/16 theorems for all knots.

**Overall.**
- I have a theorem explaining why ℓ lives in sixteenths and where odd sixteenths can arise: the odd order-four flat connection on ∂νS, equivalently the energy-1/16 cap.
- I have a window theorem showing why the known maps cannot separate ℓ(Y_{±2}): H bounds ℓ(Y_2) − ℓ(Y_{−2}) above by +1/8, and B (if an isomorphism) bounds it below by −1/8. The window is symmetric about 0.
- I have computational proof that the claimed universal gap fails.
- I have no theorem forcing a gap. The sharpest surviving formulations are (U_σ), (W) and (M). Each would suffice for the ±2 cosmetic problem, and each is consistent with every computed example.
- Confidence in the account as a whole: 80%. In any one of the conjectures: 25–30%.

---

## Appendix: scripts (`gap16/ell-code/`)
- `spaceform.py`: finite-group ρ for S³/I*, S³/O*, S³/T*, L(4,1); check of Theorem A against DLME's Example 3.7.
- `torus.py`: pillowcase enumeration, CS, and the Seifert ρ formula with candidate cone data. `run_checks.py` calibrates the cone data by integrality.
- `tables.py`: generators of Y_N(T_{p,q}) with CS, ρ, grading and f.
- `ellcmp.py`: ℓ at N = ±1, ±2 for K and K̄, with DLME's inequalities checked. `gaps.py`: the DLME gaps.
- `fscheck.py`: Fintushel–Stern cross-check.
- `twistedw.py`: twisted generators, ρ(χ) = −σ check, and twisted integrality.
- `mixed.py`: common-representation gaps.
- `windows.py`, `mixedwide.py`, `conjB.py`: windows and conjecture tests over pq ≤ 120.
- `datatable.py` writes `data_table.txt`. Columns: dmin, dmax, twisted gap, m₁, m₂, for all 210 cases; the ranges quoted in §0 and §6 were recomputed from this file.
- `integrality.py`: integrality of all 287,532 gradings.
