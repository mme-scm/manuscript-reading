# The 1/16 and the pillowcase: referee's final account

This is a hostile referee report on `gap16/pillowcase-1.md`, which studies Chern–Simons values on the pillowcase. It gives the corrected account and the corrected statements, and ends with a verdict.

Every claim carries one of three labels:
- **VERIFIED**: proved here, computed exactly, or checked against a source.
- **PLAUSIBLE**: supported by an argument with a named gap.
- **SPECULATIVE**: heuristic.

New code is in `gap16/pillowcase-final-code/`. I wrote it from scratch and did not reuse pillowcase-1's scripts. I reran those scripts only for comparison.

Notation:
- K ⊂ S³ is a knot, K̄ its mirror, Y_N = S³_N(K), and X_N is the trace.
- X_K is the knot exterior, and C is the image of its irreducible SU(2) representations in the pillowcase.
- ρ(μ) = e^{2πiα} and ρ(λ) = e^{2πiβ}, with δ = α − 1/4.
- L_N = {Nα + β ∈ ℤ} and L_N^w = {Nα + β ∈ 1/2 + ℤ}.
- W_B = (−X_2°) ∪_J X_{−2}°, with J ≅ S³. It contains the sphere S of square −4, and ∂νS ≅ L(4,1).

---

## 0. Verdict in brief

1. **The bound is false as a statement about all knots (VERIFIED, 97%).** Under DLME's normalisation, |ℓ(Y_2) − ℓ(Y_{−2})| ≥ 1/16 fails for exactly the eleven positive torus knots with 10 ≤ pq ≤ 29, among all torus knots with pq ≤ 120.
   - The evidence is now three independent computer checks, plus a new and independent validation of the formula for c by finite-group ρ-invariants (§2.1).
   - Pillowcase-1 stated the list of failing knots wrongly (§3.D).
2. **What the pillowcase line does explain (VERIFIED for torus knots and 4_1, PLAUSIBLE in general).** A generator x of Y_N satisfies
   c(Y_N, x) = Φ(x) + (3/16)·sgn N − N·α(1/2 − α) − ι_N(x)/8.
   - At |N| = 2 and the traceless holonomy α = 1/4 the slope term is ±(3 − 2)/16 = ±1/16.
   - Pillowcase-1's split of this term was wrong. The correct split is 3/16 from the signature of the trace, +2/16 from the solid-torus Chern–Simons term, and −4/16 from the solid-torus spectral flow.
   - The "a² = 1/16" of the brief is the maximum of α(1/2 − α), not the Chern–Simons term alone.
3. **The part that does not depend on conventions** is the gap 1/8 = 2·(1/16) between Y_2 and Y_{−2} at the flat connections they share: traceless meridian with λ ↦ −1.
   - **New (VERIFIED as an identity):** this gap is equivalent to a 4-dimensional statement. On W_B, the configuration that is x off νS and the energy-1/4 reducible on νS has index exactly 1, which is the index of the instantons counted by the map B.
4. **The line does not explain any gap in ℓ, and cannot.**
   - ℓ compares minima over disjoint sets of generators, and Φ varies along C by more than 1/16.
   - Example T(2,5): both pointwise offsets exceed 1/16, but Φ differs by 0.195 between the two minimising generators, and the gap is 1/32 (§3.F.4).
5. **The double cover gives no halving at the level of generators (VERIFIED).** By the covering formula for η-invariants, c(x̃) = c(x) + [ρ(Y, ad x ⊗ χ) − 3ρ(Y, χ)]/16, which is not 2c(x) + const. This is why "naive" branched-cover relations fail.
6. **Overall:**
   - The line accounts for the number 1/16 as a pointwise offset, and that account is correct after the corrections below.
   - It refutes the universal gap.
   - It gives a conditional local mechanism, but no theorem.
   - Remaining open question: a gap under cosmetic-type hypotheses (Δ_K = 1, balanced gradings). No computable example exists.

---

## 1. Conventions, re-derived and pinned

**1.1 Chern–Simons and grading (VERIFIED against DLME `instanton.tex` and BHKK `2001-6.tex`).**
- **Chern–Simons.**
  - DLME: an instanton from α to α′ has energy CS~(α) − CS~(α′), and CS~(θ) = 0.
  - Kirk–Klassen and BHKK use cs = (1/8π²)∫tr(A dA + ⅔A³). Then CS_DLME(Y) = −cs(Y) = cs(−Y).
  - Check: DLME's Example gives 1/120 and 49/120 on Σ(2,3,5), oriented as the boundary of the negative E8 plumbing. BHKK's Table 1 gives cs = 1/120 and −71/120 on X_{+1} = S³_{+1}(RHT) = −Σ(2,3,5).
- **Grading.** i(α) is the index on ℝ×Y from α to θ. Then i_DLME(α; Y) = SF_{su(2)}(Θ → α; −Y) in BHKK's (−ε,−ε) convention.
  - Check: BHKK's equation (rhoadAPS) gives SF = 8cs + ρ_ad/2 − 3/2. With ρ = 73/15 for cs = 1/120 this gives 1. For cs = −71/120 it gives −3 ≡ 5, taking ρ = 97/15 from the group sum of §2.1.
  - These are DLME's gradings 1 and 5.
- **c and ℓ.** Set c(α) := CS~(α) − i(α)/8. It is independent of the lift, since (CS~, i) ↦ (CS~ + 1, i + 8) fixes it.
  - Every bar of the barcode starts at the critical level of a generator in the same degree.
  - So if all generators have the same grading parity, the differential vanishes and ℓ = min_α c(α). Also ℓ(−Y) = 3/8 − max_α c(Y, α).

**1.2 Parity (VERIFIED).** For a Seifert-fibred rational homology sphere with three exceptional fibres, every irreducible has i odd if e < 0 and even if e > 0. This is the orbifold complex-structure argument of Fintushel–Stern, which is unchanged when H_1 ≠ 0.
- The pillowcase Chern–Simons values reproduce this parity on every generator tested.
- So all Seifert-fibred complexes below are perfect, and ℓ = min c.

**1.3 Sign conventions are pinned (VERIFIED).** DLME prove ℓ(Y_{−1}) < ℓ(Y_{−2}), ℓ(Y_2) < ℓ(Y_1) and ℓ(Y_{−1}) < ℓ(Y_1) − 1/8.
- With these conventions all three hold for T(2,3), T(2,5), T(2,7), T(3,4), T(3,5), T(2,9), T(4,5), T(3,7), T(2,11), T(5,6), in **both** chiralities.
- Suppose instead that Y_N were oriented oppositely, so that the invariant used were ℓ(−Y_N(K)) = ℓ(Y_{−N}(K̄)). Then the first two inequalities would be reversed for every knot. So this check has teeth.

**1.4 χ and the pillowcase (VERIFIED).** On Y_{±2}, H_1 = ℤ/2 and the reducibles θ, χθ are central.
- Tensoring with χ sends (α, β) to (α + 1/2, β) on the knot group. It shifts CS by N/4 ≡ 1/2 and fixes c, because ad(χx) = ad x.
- Traceless x with x(λ) = −1 satisfy χx ≇ x. A conjugacy χx ≅ x would make x binary dihedral, and binary dihedral representations have x(λ) = 1.
- On the pillowcase, x and χx lie over the same point (1/4, 1/2).

---

## 2. Independent checks carried out for this report

**2.1 The c-formula for Seifert rational homology spheres, checked by finite-group ρ-invariants (VERIFIED; new).**
- **Setup.** Let G be one of I*, O*, T* ⊂ SU(2), and let π = G × ℤ_k with gcd(k, |G|) = 1. Let π act on S³ by q ↦ g·q·e^{−2πij/k}. In the complex structure given by right multiplication by i, this is the subgroup {e^{−2πij/k}g} of U(2), and S³/π with the complex orientation is a link of a singularity.
- **The group sum.** A group element with eigenvalues e^{i(±φ−ψ)} contributes the defect cot((φ−ψ)/2)·cot((φ+ψ)/2). The ρ-invariant is
  ρ_ad(S³/π) = (1/|π|) Σ_{γ≠1} (χ_ad(γ) − 3)·cot((φ−ψ)/2)·cot((φ+ψ)/2).
- **Calibration.** One overall sign is calibrated on S³/I*, by requiring c = (3+ρ)/16 to reproduce DLME's −7/60. The second I* value, −13/60, then comes out right, and so does BHKK's ρ = 73/15 on −Σ(2,3,5).
- **Comparison.** Everything else is a prediction. It is compared with the generalised Fintushel–Stern formula
  c = (3 + 3 sgn e − 2Σ s(l_i; a_i, b_i))/16, with Y_N(T(p,q)) = M((p,b_1),(q,b_2),(pq−N,−1)) and b_1q + b_2p = 1.

| surgery | group | e | Seifert c-values | matches the group sum for |
|---|---|---|---|---|
| S³_1(T(2,3)) | I* | 1/30 | 59/120, 71/120 | −link |
| S³_2(T(2,3)) | O* | 1/12 | 23/48 | −link |
| S³_3(T(2,3)) | T* | 1/6 | 11/24 | −link |
| S³_10(T(2,3)) | O*×ℤ_5 | −5/12 | −1/48 | link |
| S³_11(T(2,3)) | I*×ℤ_11 | −11/30 | −2/15, −1/30 | link |
| S³_7(T(2,5)) | I*×ℤ_7 | 7/30 | 47/120, 53/120 | −link |
| S³_13(T(2,5)) | I*×ℤ_13 | −13/30 | −1/15, −1/60 | link |
| S³_10(T(3,4)) | O*×ℤ_5 | 5/12 | 19/48 | −link |
| S³_14(T(3,4)) | O*×ℤ_7 | −7/12 | 1/48 | link |
| S³_13(T(3,5)) | I*×ℤ_13 | 13/30 | 47/120, 53/120 | −link |
| S³_17(T(3,5)) | I*×ℤ_17 | −17/30 | 1/60, 1/15 | link |

- All eleven agree exactly, in the orientation predicted by sgn e. These cover |H_1| ∈ {1,2,3,7,10,11,13,14,17}, both signs of e, and both regimes N < pq and N > pq, so they include the −1/8 jump of §3.E.
- Scope: in every spherical case ρ(h) = −1. The case ρ(h) = +1 on rational homology spheres (for example T(3,4) at N = ±2) rests on:
  - the orbifold argument, which only uses ad ρ;
  - Fintushel–Stern on Brieskorn spheres, which has both signs;
  - the consistency c ≡ CS (mod 1/8) against the independently computed pillowcase CS.
- (`spherical.py`, `seif.py`)

**2.2 ℓ tables recomputed (VERIFIED).**
- **Method.** My own triangle-group enumeration and s-sums.
- **Untwisted bundle.** They reproduce Table 4.3 of pillowcase-1 entry by entry. They also reproduce the sibling closed form ℓ(Y_2) − ℓ(Y_{−2}) = −(n² − 16n + 36)/(8(n² − 4)), with n = pq, for every positive torus knot with pq ≤ 120.
- **Mirrors.** Their gaps lie in [3/32, 1/8].
- **Twisted bundle,** in the normalisation c^w = (3+ρ)/16: the gap is at least 151/1768 ≈ 0.0854 over pq ≤ 120 in both chiralities, with the minimum at T(3,−5).
- (`elltab.py`)

**2.3 The figure-eight knot recomputed (VERIFIED).** I computed a new parametrisation of the SU(2) curve of 4_1, solving for the conjugating angle.
- The curve is closed, with |dβ/dα| ≥ 4.47 everywhere and a double point at (1/4, 0). Over the loop, Δβ = 2, ∮2α dβ = 1 and ∮2δ dβ = 0.
- Seifert data: S³_{±2}(4_1) = M((2,∓1),(4,∓1),(5,±4)), with e = ∓1/20.
  - The orientation is fixed by the Casson–Walker sign λ(S³_{+2}(4_1)) = a_2/2 = −1/2, through the grading parity of §1.2.
  - It is fixed independently by the single pillowcase CS constant.
- The resulting values are ℓ(Y_2) = 19/80, ℓ(Y_{−2}) = 11/80, and gap 1/10.
- Let J := c − [(3 sgn N − N)/16 + Nδ²] − 2∫δ dβ, integrating from the turning point (1/6, −1/2). Then J = 3/16 at all 12 generators of S³_N(4_1), N = ±1, ±2, ±3, up to 10⁻⁴.
  - For N = ±2 no matching between pillowcase points and Seifert generators is involved.
  - For N = ±1 and ±3 there is exactly one bijection that works.
  - The two generators at the turning point (1/6, ±1/2) for N = ±3 were checked by hand: 5/24 − 3/144 = 3/16 and 1/6 + 1/48 = 3/16.
- (`fig8_check.py`)

**2.4 Negative controls and citations (VERIFIED).**
- Pillowcase-1's test "c ≡ CS (mod 1/8)" rejects wrong local Seifert data wherever the variants actually differ (`teeth.py`).
- Citations checked against the LaTeX:
  - BHKK: Theorem `csthm` (cs = −c + 2∫n dm, with (m, n) the coordinates of the filling solid torus), equation (rhoadAPS), Tables 1 and 2, Theorem `nicerformula` (SF = SF_Z(P⁻) + 2(a − b) − 2 with a = m_1), and the Remark that X_k ≅ −Σ(2, q, 2qk − 1).
  - DLME: the definitions of κ and ℓ, Lemma `kappa-ineq`, Proposition `IP-morphism` (degree −2c², level −c²/4 − η), Example `ell` (ℓ(Σ(2,3,5)) = −13/60), Proposition `pm-one-map` (g_1 of degree 3 and level 1/4 − η), and the ±2 Remark in `intro.tex`.
  - `statements.tex`, Theorem B: B has L − D/8 = 1/8 − η.

---

## 3. The statements of pillowcase-1, one by one

### A. Chern–Simons on the pillowcase (Theorem 2.1, Corollary 2.2): kept, VERIFIED
- **Theorem 2.1.** CS_DLME(Y_{p/q}, x) ≡ −2∫_γ B′dA′ (mod 1), for a path γ from θ lifted continuously. In particular CS_DLME(Y_N, x) ≡ 2∫_γ α dβ + N·α(1)².
  - This is BHKK's Theorem `csthm` reduced mod 1, with the sign change CS_DLME = −cs.
- **Corollary 2.2(a).** At the traceless points with λ ↦ −1, CS(Y_2) − CS(Y_{−2}) ≡ 4·(1/4)² = 1/4.
  - Wording fix: 1/4 is the area of the triangle with vertices θ, (1/4, ±1/2), measured with 2dα∧dβ. It is not "twice" that area.
- **Corollary 2.2(b).** At L_2 ∩ L_{−2}^w (a = 1/8, 3/8), ΔCS ≡ 1/16 holds modulo 1/2, which is stronger than modulo 1/8. This is the energy of the SO(3) reducible on νS with v = ξ, observation (i) of the brief.
- **Corollary 2.2(c).** L_2^w ∩ L_{−2}^w = {(0,1/2), (1/4,0), (1/2,1/2)}. Only (1/4,0) can carry flat connections of X_K.

### B. c as a ρ-invariant (Theorem 3.1, Corollary 3.2): kept, VERIFIED; Remark 3.3 narrowed
- **Theorem 3.1.** c(α) = (3 + ρ_ad(α))/16 for a nondegenerate irreducible flat α on a rational homology sphere, with ρ_ad = η_{ad α} − 3η.
  - The hypothesis that all reducibles are central is not needed for this identity. It is needed only to define the Floer complex simply.
- **Corollary 3.2.** Both parts hold:
  - c(−Y) = 3/8 − c(Y);
  - c(α) = 3(1 + b⁺(W))/8 + (ind A − 8E(A))/8, for any W with ∂W = Y and b_1(W) = 0. I re-derived this from DLME's index additivity and energy formula.
  - Equivalently, for a cobordism W: Y → Y′ with b_1 = b⁺ = 0, c(α′) − c(α) = ind(A)/8 − E(A), for any connection A on any bundle.
- **Remark 3.3, corrected.**
  - "Nonsingular cobordism and family maps between Floer groups with θ-normalised gradings have L − D/8 ∈ (1/8)ℤ − η": VERIFIED, because the c² terms cancel.
  - So a 1/16 cannot enter through L − D/8. It can enter through η, the least energy of a counted instanton.
  - Mixed-bundle maps across W_B meet configurations of energy exactly 1/16: the odd reducible on νS, at L_2 ∩ L_{−2}^w.
  - Singular maps with holonomy along a surface have energies containing α_0²·Σ·Σ. At α_0 = 1/4 this produces sixteenths.
- **Units statement.** "1/16 lives in the c-values because ℓ = (3+ρ)/16" is only a statement about units: a gap of 1/16 in ℓ is a gap of 1 in ρ_ad between the minimising generators.
  - Since ρ_ad is not quantised, this alone does not single out 1/16.
  - Quantisation holds only at shared generators, where Δρ_ad ∈ 2ℤ (§3.F.3).

### C. The Seifert formula (Theorem 4.1): upgraded to VERIFIED
- The proof is Fintushel–Stern's orbifold argument, verbatim:
  - sign(W) = sgn e for the orbifold disc bundle;
  - the twisted signature vanishes, because rigid irreducible triangle representations have H*(B; ad) = 0;
  - the cone-point terms are −2s(l_i; a_i, b_i).
- Nothing in the argument uses H_1 = 0. The remaining doubt in pillowcase-1 ("proof sketch PLAUSIBLE") is removed by the eleven group-sum checks of §2.1.
- **Theorem 4.2,** the torus-knot closed form, is an exact consequence. I checked the algebra by hand: s(l; m, −1) = 1 − 2l(m − l)/m.

### D. Torus knots and the failure of the bound: VERIFIED, with Conclusion 4.4 corrected
- **Correction.** Pillowcase-1 says the bound fails "for T(2,q) with q ≥ 5 and for T(3,4), T(3,5), T(3,7), T(4,5), T(4,7)". That is wrong in two ways.
  - For q ≥ 15 the absolute bound holds, with a negative gap. For example T(2,15) has gap −57/896 ≈ −0.0636.
  - T(3,8) is missing from the list.
- **Corrected statement (VERIFIED for pq ≤ 120 here, and for pq ≤ 200 by the sibling `seifert-1.md`).** For the positive torus knot T(p,q), with n = pq:
  ℓ(Y_2) − ℓ(Y_{−2}) = −(n² − 16n + 36)/(8(n² − 4)).
  - This is at least 1/16 only for the trefoil (3/32).
  - It changes sign between n = 13 and n = 14, and tends to −1/8.
  - Its absolute value is below 1/16 exactly for 10 ≤ n ≤ 29, that is, for T(2,5), T(2,7), T(2,9), T(2,11), T(2,13), T(3,4), T(3,5), T(3,7), T(3,8), T(4,5) and T(4,7).
  - The one-sided bound ℓ(Y_2) − ℓ(Y_{−2}) ≥ 1/16 fails for every positive torus knot except T(2,3).
- **Mirrors.** For negative torus knots the gap lies in [3/32, 1/8].
- **4_1.** The gap is 1/10.
- **Orientation conventions.** Reversing them sends the gap of K to minus the gap of K̄. The pair T(2,±7), with gaps −1/192 and 23/192, therefore violates the absolute bound under either convention (VERIFIED).
- **Twisted bundle (VERIFIED as a computation; with caveats).**
  - In the normalisation c^w = (3+ρ)/16, all twisted gaps over pq ≤ 120 are at least 0.0854. This is consistent with the user's twisted observation.
  - Caveat 1: (Y_{±2}, w) carries a flat reducible ζ = (1/4, 0) with stabiliser O(2). So the irreducible twisted complex needs care before it is even defined.
  - Caveat 2: the absolute grading is a choice. The grading relative to ζ, i^w(x) = ind(x → ζ), gives c′ = (ρ(x) − ρ(ad ζ) + h(ζ))/16. This differs from (3+ρ)/16 by (2 + 2ρ_χ)/16.
  - That shift is the same on Y_2 and Y_{−2}, since ρ_χ(Y_{±2}) = −σ(K) on both (PLAUSIBLE: the sibling computed this for torus knots). So the twisted gaps are the same in the two normalisations.
- **Consequence for the map B (VERIFIED as a deduction).** If B (degree −1, L − D/8 = 1/8 − η) is injective, DLME's Lemma 2.7(b) forces η(B) ≤ 1/8 + [ℓ(Y_2) − ℓ(Y_{−2})].
  - For T(2,q) this tends to 0 as q → ∞.
  - So for large positive torus knots B, if injective, must count instantons of nearly zero energy. Its level is unfavourable there, consistent with `statements.tex`.

### E. The pillowcase formula for c (Conjecture 5.1)
- **Statement.** Let Γ be a component of C. For a generator x of Y_N on Γ,
  c(Y_N, x) = Φ(x) + (3/16) sgn N − N·α(1/2 − α) − ι_N(x)/8, with dΦ = 2δ dβ along Γ.
  - This is pillowcase-1's form rewritten, using (3 sgn N − N)/16 + Nδ² = (3/16) sgn N − Nα(1/2 − α).
  - ι_N ∈ {0, 1} is a Maslov indicator, equal to [N > pq] for positive torus knots.
  - Equivalently, i(Y_N, x) = 4(Nα + β) − (3/2) sgn N + ι_N(x) + const_Γ, with Nα + β ∈ ℤ the lifted meridian holonomy of the filling.
- **Status.**
  - For torus knots, at all slopes and in both bundles, it is an algebraic identity once C is established: VERIFIED. The jump at N > pq is confirmed by the spherical cases N = 10, 11 (T(2,3)), 13 (T(2,5)), 14 (T(3,4)) and 17 (T(3,5)).
  - For 4_1 at N = ±1, ±2, ±3 it holds with j_Γ = 3/16: VERIFIED, recomputed independently in §2.3.
  - In general it is PLAUSIBLE, at about 70%. It is the su(2) analogue of BHKK's splitting theorem (`nicerformula`), and in ρ-language a gluing formula of Kirk–Lesch type. In that formula the term −(3/2) sgn N + ι_N is the Maslov triple index of TC, the slope line and a reference line.
  - The precise rule for ι_N is about 55%.
- **Normalisation remark (new).** Requiring the slope term to be odd in N fixes the additive constant of Φ; the odd form is forced by mirror symmetry, Φ_{K̄}(x̄) = 3/8 − Φ_K(x).
  - With this normalisation, Φ equals (3+ρ)/16 on the twisted zero-surgery Y_0^w.
  - Calling Φ "the level" of another Floer theory (Y_0^w, or the traceless singular theory of (S³,K)) is a choice of absolute grading for that theory. The Z/4-graded I^w(Y_0) has no canonical one.
  - Only differences of c between θ-normalised theories are free of conventions.

### F. Y_2 against Y_{−2}

**F.1 Pointwise (VERIFIED given E).** c(Y_{±2}, x) = Φ(x) ± (1/16 + 2δ²) − ι_{±2}(x)/8.
- Pillowcase-1's Summary point 7 omits the term ι/8.
- The inequality "every generator of Y_2 lies at least 1/16 above Φ" holds only where ι_2(x) = 0. By the indicator rule, that is where the tangent slope of C at x is not in (−2, 0).
- Likewise, Y_{−2} lies at least 1/16 below Φ only where the tangent slope is not in (0, 2).

**F.2 The decomposition of 1/16 (CORRECTED).** At N = 2 and α = 1/4 the slope term splits as
- 3/16 = 3·sign(X_N)/16: dim su(2) times the signature of the filling;
- +2/16: the solid-torus Chern–Simons term Nα²;
- −4/16: the solid-torus spectral flow, −Nα/2, which is the 4Nα of the grading divided by 8.

Their sum is 1/16. At N = −2 every sign reverses, giving −1/16.

Pillowcase-1 attributes the −2/16 to "the squared traceless holonomy". That is the wrong sign and the wrong term. The correct description:
- the net solid-torus term is −N·α(1/2 − α);
- the function α(1/2 − α) attains its maximum 1/16 = (1/4)² exactly at the traceless holonomy.

That is the correct place for observation (iv). The same formula gives an offset of (3 − |N|)/16 at the traceless holonomy: 1/8 at |N| = 1, 1/16 at |N| = 2, and 0 at |N| = 3. The value at |N| = 1 equals DLME's constant 1/8; whether that is more than a coincidence is SPECULATIVE.

**F.3 Shared generators: the part free of conventions.**
- If x(μ) ~ i and x(λ) = −1, then Δc := c(Y_2, x) − c(Y_{−2}, x) ∈ (1/8)ℤ. VERIFIED: ΔCS ≡ 1/4 and i is an integer.
- Δc = 1/8 for torus knots in both chiralities: VERIFIED from Theorem 4.2.
  - On the arc (k,l), where β ≡ k/2 − pqα, such points require pq ≡ 2k − 2 (mod 4).
  - So they never occur for T(2,q). They do occur for T(3,4).
- Δc = 1/8 whenever C is smooth at x with tangent slope s, |s| > 2: PLAUSIBLE.
- Δc ∈ {0, 1/4} if |s| < 2: PLAUSIBLE, by the indicator rule.

**Proposition F.3 (new; VERIFIED as an identity).** Let x be as above, and let A_x on W_B be x on W_B∖νS together with the U(1)-reducible on νS with ⟨c_1(L), S⟩ = ±1.
- A_x restricts on L(4,1) to the flat connection of trace zero, has energy E = 1/4, and lies in the jumping divisor V_S.
- By the cobordism identity of §3.B, ind(A_x) = 2 − 8Δc.
- Hence Δc = 1/8 holds if and only if ind(A_x) = 1, which is exactly the index of the instantons counted by B.
- At η = 1/4, B's level L − D/8 = 1/8 − η equals −1/8 = −Δc.

So the pointwise 2·(1/16) is the favourable level of B, realised at its energy-1/4 reducible.
- Gluing in statements.tex's framed convention, where the reducible on νS has framed index 2, the off-νS part x then has index −1. So x is obstructed, and whether A_x actually contributes to B is not settled.

**F.4 From pointwise offsets to ℓ (VERIFIED as an identity; corrected).** Assume the complexes are perfect and ι = 0 at the minimising generators; pillowcase-1 omits the second hypothesis. Then
ℓ(Y_2) − ℓ(Y_{−2}) = 1/8 + min_{C∩L_2}(Φ + 2δ²) − min_{C∩L_{−2}}(Φ − 2δ²).

Worked example T(2,5) (VERIFIED, `t25_example.py`; the closed form agrees with the Seifert formula on all twelve generators):

| | minimising generator | Φ there | c − Φ |
|---|---|---|---|
| Y_2 | α = 1/16 on arc (1,1), next to the arc end 1/20 | 0.3609 | +0.1328 |
| Y_{−2} | α = 1/8 on arc (1,1) | 0.5563 | −0.0938 |

- Both offsets exceed 1/16 in absolute value.
- Φ = 7/80 + 10/16 − 10δ² is concave on the arc, and the Y_2 generators (spacing 1/8) reach closer to the arc end than the Y_{−2} generators (spacing 1/12).
- The resulting Φ-difference of 0.195 pulls the gap down to 1/32.

**Local mechanism (6.4) (VERIFIED as algebra).** Suppose both minimisers lie on one straight branch of slope s > 2 through a traceless point. Then the gap lies in [1/8 − 1/(4(s−2)), 1/8 + 1/(4(s+2))], which is at least 1/16 once s ≥ 6.
- The traceless point need not be a generator. For the mirror trefoil it has λ ↦ +1, and the true value is 3/32.
- Here the "1/16" is 1/8 − 1/(4·4) at s = 6. That is a different 1/16, coming from the steepness of the trefoil branch.

**F.5 Conjecture 6.5 (SPECULATIVE, lowered to about 15%).** The conjecture is that Δ_K = 1 implies a gap of at least 1/16.
- Its only support is 4_1, which has Δ ≠ 1, and the local mechanism.
- With Δ_K = 1 the Euler characteristic of I(Y_{±2}) vanishes. So the generators have both parities, and the complexes need not be perfect.
- I know of no knot with Δ_K = 1, or with a_2 = 0, whose ±2 surgeries are both Seifert-fibred. So the conjecture cannot be tested by the methods used here.

### G. Traceless representations and the S³ face (Section 7)
- **Items 7.1–7.3: VERIFIED.**
  - R(K, i) = C ∩ {α = 1/4}.
  - The points with λ ↦ −1 are the irreducibles shared by Y_2, Y_{−2} and Y_0^w.
  - The binary dihedral representations lie at (1/4, 0), and there are none when det K = 1.
- **Item 7.4: SPECULATIVE, and over-stated in pillowcase-1.**
  - "All of R(K, i) sits at level Φ, halfway between Y_2 and Y_{−2}" makes sense only at the points with λ ↦ −1.
  - Even there it presupposes an absolute normalisation of the singular theory of (S³, K) with holonomy 1/4.
  - The statement that survives is about differences: at those points c(Y_{±2}) = Φ ± 1/16.
  - Whether the singular 2-handle maps realise these two half-steps is an open question about the singular theory. The sibling `triangle-1.md` gives a related construction, which I have not refereed.

### H. The branched double cover (new; VERIFIED)
- **The cover.** Let π: Ỹ → Y_{±2} be the connected double cover, with deck character χ. For a flat x on Y_{±2}:
  - η(Ỹ, π*E) = η(Y, E) + η(Y, E ⊗ χ);
  - CS(x̃) = 2CS(x);
  - c(x̃) = c(x) + [ρ(Y, ad x ⊗ χ) − 3ρ(Y, χ)]/16.
- So c(x̃) ≡ 2c(x) (mod 1/8), since the gradings are integers, but c(x̃) is not 2c(x) + const.
- This is the general reason behind the sibling's observation that f̃ = 2f + k/8 with k varying from generator to generator.
- It explains why "halve DLME's 1/8 through the cover" has no content at the level of generators, in line with the user's experience.
- A further obstacle: DLME's ±1 inequality is proved for knots in S³ and uses I(S³) = 0. Upstairs, the knot K̃ sits in Σ_2(K), whose Floer homology is usually nonzero.

---

## 4. The corrected structural account of the 1/16

1. **The number (VERIFIED for torus knots and 4_1; PLAUSIBLE in general).**
   - c-values of surgeries are ρ-invariants: c = (3 + ρ_ad)/16.
   - ρ_ad splits along the torus into an exterior part Φ, which is independent of the slope, and a solid-torus part. That part is (3/16)·sgn N − N·α(1/2 − α), up to Maslov jumps of 1/8.
   - At the traceless holonomy, α(1/2 − α) is maximal and equals 1/16. So at |N| = 2 the offset from Φ is ±(3 − 2)/16 = ±1/16.
   - This is the precise sense in which observation (iv) (a² = 1/16) and the signature term 3/16 combine to give 1/16.
2. **The part free of conventions (VERIFIED for torus knots; PLAUSIBLE in general).** At the shared generators (traceless, λ ↦ −1), Y_2 lies exactly 1/8 = 2·(1/16) above Y_{−2}.
   - This is the identity 1/8 = E − ind/8 = 1/4 − 1/8 for the energy-1/4 reducible on νS glued to x (Proposition F.3).
   - The CS gap 1/4 is the area of the triangle cut out by L_2 and L_{−2}. The grading gap is 1.
3. **Why there is no 1/16 in index formulas, and where it can enter (VERIFIED).**
   - Nonsingular maps shift c by (1/8)ℤ − η.
   - A 1/16 can enter only through η, for example via the odd reducible of energy 1/16 at L_2 ∩ L_{−2}^w in mixed-bundle maps, or through singular maps.
4. **Why no universal gap follows (VERIFIED).** The pointwise offsets are measured from Φ, and Φ varies along C.
   - For positive torus knots the minimisers of c(Y_{±2}) sit near the ends of concave arcs (dΦ = 2δ dβ with dβ/dα = −pq), and the gap is uncontrolled. It is negative for pq ≥ 14 and tends to −1/8.
   - For negative torus knots the minimisers sit on convex branches of slope pq ≥ 6, near the traceless line, and the gap is in [3/32, 1/8].
   - For 4_1, whose curve has |dβ/dα| ≥ 4.47, the gap is 1/10.

---

## 5. Verdict

The question is whether the line "Chern–Simons values on the pillowcase" explains the 1/16.

- **The number: yes, correctly after correction.** It explains why 1/16, rather than another constant, is the natural size of the offset between Y_{±2} and the mirror-symmetric middle level Φ. It also identifies the gap at shared generators, 1/8 = 2·(1/16), with a definite 4-dimensional configuration on W_B, of index 1 and energy 1/4.
- **The gap: no.** It does not and cannot explain a gap of 1/16 between ℓ(Y_2) and ℓ(Y_{−2}), because no such gap holds for all knots. The torus-knot counterexamples T(2,5) through T(4,7) are now established beyond reasonable doubt.
- **What would be needed.** Any proof of a gap must use a hypothesis that positive torus knots violate. Candidates are balanced gradings, Δ_K = 1, or the absence of concave arcs ending on the reducible line.
- **What it would take.** The pillowcase picture shows that such a proof needs control of Φ between the minimising generators of Y_2 and Y_{−2}, not just the pointwise offsets. None of the cobordism maps considered so far provides that control.

Confidence:
- the explanation of the number: about 85%;
- the failure of the universal bound in DLME's normalisation: 97%;
- that the pillowcase line alone cannot yield a gap theorem without new input: about 90%.

---

## 6. Status of the claims of pillowcase-1

| item | claim | verdict |
|---|---|---|
| 2.1 | CS ≡ 2∫α dβ + Nα² | VERIFIED, kept |
| 2.2 | ΔCS at shared points | VERIFIED; (b) holds mod 1/2; wording of the area fixed |
| 3.1–3.2 | c = (3+ρ)/16; c(−Y) = 3/8 − c; cobordism identity | VERIFIED; centrality hypothesis unnecessary |
| 3.3 | 1/16 cannot appear in index formulas | VERIFIED for nonsingular θ-normalised maps; 1/16 can enter through η or singular maps |
| 4.1 | Seifert formula for rational homology spheres | upgraded to VERIFIED (eleven group-sum checks) |
| 4.2 | torus-knot closed form, including the −1/8 for N > pq | VERIFIED |
| Table 4.3 | ℓ values | VERIFIED (three independent codes) |
| 4.4 | list of failing knots | CORRECTED: exactly 10 ≤ pq ≤ 29; T(2,q) with q ≥ 15 satisfies the absolute bound; T(3,8) added |
| 5.1 | pillowcase formula for c | VERIFIED for torus knots and 4_1 (recomputed); PLAUSIBLE in general (70%; ι rule 55%); Φ's absolute level is a convention |
| 6.1 | c(Y_{±2}) = Φ ± (1/16 + 2δ²) | VERIFIED given 5.1, only with the −ι/8 term restored |
| 6.2 | decomposition 3/16 − 2·(1/4)² | CORRECTED: 3/16 + 2/16 − 4/16; the correct quantity is α(1/2 − α) |
| 6.3 | Δc ∈ (1/8)ℤ at shared points; = 1/8 when steep | VERIFIED / PLAUSIBLE; new 4-dimensional meaning: ind(A_x) = 1 (Proposition F.3) |
| 6.4 | gap formula; local mechanism | VERIFIED as algebra; needs ι = 0 at the minimisers; T(2,5) worked example added |
| 6.5 | Δ_K = 1 ⇒ gap ≥ 1/16 | SPECULATIVE, about 15%; untestable by Seifert methods at present |
| 7.1–7.3 | traceless representations | VERIFIED |
| 7.4 | R(K,i) at level Φ, halfway | SPECULATIVE; meaningful only at points with λ ↦ −1, and only relative to a chosen normalisation of the singular theory |
| new | double cover: c(x̃) = c(x) + [ρ(ad x⊗χ) − 3ρ(χ)]/16 | VERIFIED (covering formula); no halving |
| new | if B is injective, η(B) ≤ 1/8 + gap → 0 along T(2,q) | VERIFIED as a deduction from DLME Lemma 2.7(b) and the table |

---

## Appendix: files in `gap16/pillowcase-final-code/`
- `spherical.py`: ρ_ad of S³/(G × ℤ_k) by group sums, for G = I*, O*, T*; one sign calibrated on S³/I*.
- `seif.py`: Seifert enumeration and the c-formula, and the comparison of eleven spherical surgeries with the group sums.
- `elltab.py`: ℓ(Y_{±2}) for torus knots with pq ≤ 120, both chiralities, untwisted and twisted, compared with the closed form.
- `fig8_check.py`: an independent figure-eight SU(2) curve, and the slope-independence test (J = 3/16).
- `t25_example.py`: the T(2,5) generators, Φ, and the offsets.
