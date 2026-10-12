# Index and obstruction of the reducible on the surgery cobordisms

Setting: the triangle S³ → Y_1 → (Y_2, w) → S³, and the twisted reducible ζ on (Y_2, w). ζ sends μ to the rotation by π; ad ζ = ℝ ⊕ ℝ_− ⊕ ℝ_−, h⁰ = 1, h¹ = 0.

## The cobordisms adjacent to (Y_2, w)
- **X : Y_1 → Y_2.** Attach a 2-handle along the meridian with framing −1; a slam-dunk takes (K, 1) to (K, 2).
  - X is simply connected, with b₂ = 1 and generator Σ, Σ·Σ = −2. It is negative definite, χ(X) = 1, σ(X) = −1.
  - Check: the linking matrix [[1,1],[1,−1]] of trace(1) ∪ X has signature 0.
- **W : Y_2 → S³.** Attach a 2-handle along the meridian with framing 0.
  - Same invariants: Σ·Σ = −2, χ = 1, σ = −1.
  - Check: [[2,1],[1,0]] has signature 0.

## The reducibles with ζ as a limit
- H²(X; ℤ) = ℤ e with ⟨e, Σ⟩ = 1. Then PD(e) = −Σ/2, so e² = −1/2, and e|_{Y_2} generates H²(Y_2) = ℤ/2.
- The SO(3) reducibles are ℝ ⊕ L with c₁(L) = (2k+1)e, an odd multiple because w|_{Y_2} ≠ 0. Since b⁺ = 0, the harmonic representative is ASD.
  - c and −c give isomorphic SO(3) bundles, so there is one reducible A_k for each odd |2k+1|.
- Limits: θ on Y_1 and ζ on Y_2. Energy κ = −c²/4 = (2k+1)²/8.
  - The minimal one, A_0, has κ = 1/8. This agrees with CS(ζ) = N/16 = 1/8 (ell-1 §2.5).
- ad = ℝ ⊕ L. Deformations split into an ℝ-part and a complex L-part.

## APS index (weights that force decay at both ends)

ind(D_V) = −2p₁(V)[X] − (r/2)(χ + σ) − Σ_{Y ⊂ ∂X} h_V(Y)/2 + Σ_{Y ⊂ ∂X} ρ_V(Y)/2.

- Here ρ_V = η_V − r·η is the APS ρ-invariant of the odd signature operator, and Y carries its boundary orientation.
- Sign convention: the ASD boundary operator has η = −η_sig. This is forced, because the untwisted index is topological while η_sig depends on the metric.

**ℝ-part.** −(χ+σ)/2 − (1 + 1)/2 = **−1**. This is the S¹ stabiliser.

**L-part (complex index).**
- Boundary terms: h_ℂ = 1 on Y_1, where L is trivial. h_ℂ = 0 on Y_2, where L = ℂ_χ, H⁰ = 0, and H¹ = 0 because the double cover is a ℚHS.
- Result:

  ind_ℂ(A_k) = ((2k+1)² − 1)/2 + ρ_χ(Y_2)/2.

**The ρ-invariant.**
- APS: ρ_χ(∂W) = sign(W) − sign_χ(W) = −(Casson–Gordon defect).
- Casson–Gordon Lemma 3.1: σ_1(S³_n(K), χ) = sign(n) − 2r(m−r)n/m² − σ_K(ω^r).
  - The sign of the σ_K term is checked on S³_6(T(2,3)) = L(2,1) # L(3,2). There ρ_χ = ρ_χ(ℝP³) = 0, while the other sign would give −4.
- For n = ±2, m = 2, r = 1 the defect is −σ(K). Hence **ρ_χ(Y_{±2}) = σ(K)** in the APS convention.
- This is the one convention-sensitive step: that the Casson–Gordon σ_r is the twisted signature minus the untwisted one. Integrality holds for either sign, since σ is even.

## Result
| triangle | edge | ind_ℂ(A_k), L-part | minimal A_0 (κ = 1/8) |
|---|---|---|---|
| +2 | Y_1 → (Y_2, w) | ((2k+1)²−1)/2 + σ/2 | σ/2: **obstructed, coker ℂ^{|σ|/2}, if σ < 0** |
| +2 | (Y_2, w) → S³ | ((2k+1)²−1)/2 − σ/2 | −σ/2: obstructed if σ > 0 |
| −2 | S³ → (Y_{−2}, w) (trace, form (−2)) | ((2k+1)²−1)/2 + σ/2 | obstructed if σ < 0 |
| −2 | (Y_{−2}, w) → Y_{−1} (framing −1, σ(W) = −1) | ((2k+1)²−1)/2 − σ/2 | obstructed if σ > 0 |

- **Generic perturbation.** The L-part operator is ℂ-linear, so it can be made injective or surjective, and the obstruction is ℂ^{|σ|/2} with S¹ weight 1.
  - That gives |σ|/2 suspensions, in degrees spaced by 2.
  - All of them come from A_0. The two edges at (Y_{±2}, w) split according to the sign of σ: for σ < 0 the edge into (Y_{±2}, w) is obstructed, for σ > 0 the edge out of it.
  - **For Δ_K = 1, σ = 0, so A_0 has index 0 and is unobstructed.**
- **Total real index.** ind(A_0) = −1 + σ on the edges where the L-part index is +σ/2, and −1 − σ on the others.
- **Higher reducibles.** A_k has L-index ((2k+1)² − 1)/2 ± σ/2. It is obstructed once |σ| > (2k+1)² − 1, for example k = 1 when |σ| > 8. But it lies (2k+1)² − 1 real dimensions above A_0, so it enters only moduli spaces of that much higher dimension. That is irrelevant for the maps and homotopies of the triangle.
- **Rank check for the +2 triangle with σ < 0.** One new generator per cokernel dimension on (Y_2, w) gives:

  | knot | irreducible count + |σ|/2 | rank I(Y_1) |
  |---|---|---|
  | T(2,3) | 1 + 1 | 2 |
  | T(3,5) | 12 + 4 | 16 |
  | T(4,5) | 26 + 4 | 30 |
  | T(4,13) | 198 + 12 | 210 |

- **Where the correction goes in the other three cases.** With σ > 0 in the +2 triangle, and with either sign in the −2 triangle, the irreducible count *exceeds* the rank by |σ|/2. Rank bookkeeping alone does not decide where the corrections go. They could cancel against existing generators through a differential, or sit at the third vertex.
