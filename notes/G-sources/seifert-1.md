# Seifert-1: the 1/16 tested on Seifert-fibred surgeries

Line of attack: test cases. For every torus knot and for the figure-eight knot, the surgeries Y_{±1}, Y_{±2} (and Y_0 for the twisted bundle) are Seifert fibred. Their flat SU(2) and SO(3) connections, Chern–Simons invariants, absolute gradings and the invariants ℓ, ℓ⁺ can be computed exactly. I did this with code written independently of the sibling notes `ell-1.md` and `pillowcase-1.md`; every number they report and that I recomputed agrees exactly.

Every claim is labelled:
- **VERIFIED**: proved here, computed exactly, or checked against a source.
- **PLAUSIBLE**: supported by evidence and a standard argument, but not proved.
- **SPECULATIVE**: a conjecture or heuristic.

The code is in `gap16/seifert-code/`; §8 lists the scripts.

Notation:
- K ⊂ S³ is a knot, Y_N = S³_N(K), and n = pq for the torus knot T(p,q) (p, q > 0 means the positive knot).
- K̄ is the mirror, so Y_N(K̄) = −Y_{−N}(K).
- a ∈ [0, 1/2] is the reduced meridian parameter, ρ(μ) ~ e^{2πia}; δ = a − 1/4; β is the longitude parameter.
- f(α) = CS~(α) − gr(α)/8 for a generator α, in DLME's conventions.
- ℓ = min f and ℓ⁺ = max f whenever the Floer differential vanishes. In every Seifert example below it does, because all generators of a given (Y, bundle) have the same grading parity.
- The **gap** of K is ℓ(Y_2) − ℓ(Y_{−2}).

---

## 0. Summary

1. **The claimed bound fails, by an exact formula (VERIFIED).** The user's claim, |ℓ(Y_2) − ℓ(Y_{−2})| ≥ 1/16 in DLME's normalisation, is false for torus knots.
   - For every positive torus knot T(p,q) with n = pq, the gap is a function of n alone:
     **ℓ(Y_2) − ℓ(Y_{−2}) = −(n² − 16n + 36) / (8(n² − 4)).**
     The value is 3/32 for the trefoil and 1/32 for T(2,5). It changes sign between n = 13 and n = 14, and tends to −1/8 as n → ∞.
   - It has absolute value below 1/16 exactly when 10 ≤ pq ≤ 29. Those are the eleven knots T(2,5), T(2,7), T(2,9), T(2,11), T(2,13), T(3,4), T(3,5), T(3,7), T(3,8), T(4,5), T(4,7).
   - For negative torus knots, the gap is 1/8 − 4m²/(n² − 4) with m ∈ {0, 1/4, 1/2}, so it lies in [3/32, 1/8].
   - This was checked exactly for all 201 torus knots with pq ≤ 200, in both chiralities.
   - No global orientation convention rescues the claim, since the mirror pair {T(2,7), T(2,−7)} has gaps {−1/192, 23/192}.
2. **Companion formulas (VERIFIED).**
   - ±1 surgery, positive torus knots: ℓ(Y_1) − ℓ(Y_{−1}) = (n² + 6n − 11)/(8(n² − 1)). This decreases to 1/8, so DLME's constant 1/8 is sharp.
   - Nontrivial bundle w on Y_{±2}, positive torus knots: the gap is (3n² − 44)/(8(n² − 4)), which increases to 3/8.
3. **Where the 1/16 lives (VERIFIED for torus knots; PLAUSIBLE in general).** On each arc of the SU(2) character curve C of the knot exterior,
   **f(Y_N, x) = Φ(x) + 3 sgn(N)/16 − N·a(1/2 − a).**
   - Φ does not depend on N. At the points of C with λ ↦ −1 it equals the f-function of the twisted 0-surgery Y_0^w, in the orientation-symmetric normalisation f = (3 + ρ)/16.
   - At the points where arcs leave the reducible line, Φ = (3 − σ_−(ω) − σ_+(ω))/16. Here σ_± are the Levine–Tristram signatures on either side of the root ω = e^{4πia} of Δ_K.
   - For N = ±2 the term 3 sgn(N)/16 − N·a(1/2 − a) lies in ±[1/16, 3/16]. Its inner edge **1/16 = (3 − 2)/16** is attained exactly at traceless representations, where a(1/2 − a) is largest and equals 1/16.
   - The 3/16 is dim SU(2) times the signature term of the trace. The 2/16 is |N| times the surgery solid-torus term at the traceless holonomy a = 1/4.
   - So 1/16 is the f-distance from Y_{±2} to the twisted zero-surgery at the generators that Y_2, Y_0^w and Y_{−2} share: the traceless ones with λ ↦ −1.
   - The same expression with |N| = 1 gives (3 − 1)/16 = 1/8, which is DLME's constant.
4. **Why the 1/16 does not pass to ℓ (VERIFIED for torus knots; PLAUSIBLE as a local mechanism).** ℓ compares minima over different sets of points, so local configurations decide it.
   - **Near a traceless crossing of slope s on a convex branch,** the local gap is 1/8 − 4m²/(s² − 4). Here m ∈ [0, 1/2] is a phase determined by the height of the crossing.
   - **Near a point where an arc leaves the reducible line at a_e on a concave branch,** the local gap is 1/8 − 4(a_e − 1/4)², which tends to −1/8.
     - The cause is a parity effect. For even N the central character χ makes the two ends of each χ-invariant arc equivalent, so Y_{−N}'s nearest generators are trapped at phase {−N a_e} ≈ 1.
     - For odd N, Y_{−1} escapes to the other end at phase 1/2, and the same computation gives 1/4 − 2(a_e − 1/4)² ≥ 1/8. That is the torus-knot shadow of DLME's theorem.
5. **Nontrivial bundle (VERIFIED in the examples).** The twisted gap is at least 0.0854 in all 402 cases (attained at T(3,−5)) and equals 1/8 for 4_1.
   - The reason: the lines L_{±2}^w pass through the twisted reducible ζ = (1/4, 0) rather than through θ.
   - Near the points where arcs leave the reducible line both twisted phases are about 1/2, and the local gap is 1/8 + 2|a_e − 1/4| − 4(a_e − 1/4)² ≥ 1/8.
   - This explains why the twisted form of the claim survives every Seifert test.
6. **Figure-eight knot, the only Seifert case where no arc meets the reducible line (VERIFIED).**
   - S³_2(4_1) = M((2,−1),(4,−1),(5,4)); the orientation is fixed by the Casson–Walker invariant −1/2.
   - Untwisted: ℓ(Y_2) = 19/80 and ℓ(Y_{−2}) = 11/80, so the gap is 1/10.
   - Twisted: 3/40 and −1/20, so the gap is 1/8.
7. **Double covers (VERIFIED; the heuristic fails).** For p, q odd, the double cover of Y_{±2}(T(p,q)) is ∓Σ(p, q, pq ∓ 2) = Σ_{±1}(K̃).
   - Upstairs the gap lies between 0.19 and 0.375, so it exceeds 1/8 in every example.
   - For pulled-back generators f̃ = 2f + k/8, with an integer k that varies from generator to generator.
   - So "downstairs ℓ is upstairs ℓ halved" is false, in line with the user's experience.
8. **Proposed explanation and conjectures.**
   - The 1/16 is the inner edge of the ±2 band, (3 − |N|)/16 at |N| = 2.
   - It controls ℓ when the minimising generators lie near traceless crossings, which is the case for negative torus knots and 4_1. It fails when they lie near reducible points where arcs leave the reducible line.
   - Knots with Δ_K = 1 have no such points, so the failure mechanism is absent for every cosmetic candidate.
   - Conjecture (Δ_K = 1 ⇒ gap ≥ 1/16) and its twisted analogue are SPECULATIVE, about 25% and 35%. Details in §7.

---

## 1. Conventions and normalisations

### 1.1 Seifert invariants and orientations (VERIFIED)
- **Presentation.** M((a_1,b_1), …, (a_k,b_k)) has
  π_1 = ⟨x_i, h | h central, x_i^{a_i} h^{b_i} = 1, x_1⋯x_k = 1⟩, with e = −Σ b_i/a_i.
  Links of singularities have e < 0; Σ(a_1,a_2,a_3) has e = −1/(a_1a_2a_3).
  The plumbing parameter of the arm at (a_i, b_i) is β_i ≡ −b_i (mod a_i). Check: Σ(2,3,5) = M((2,1),(3,1),(5,−4)) bounds −E_8 with arms 2/1, 3/2, 5/4.
- **Torus knot surgeries.** Y_N(T(p,q)) = M((p, b_1), (q, b_2), (pq − N, −1)) with b_1 q + b_2 p = 1, and e = N/(pq(pq − N)).
  - Derivation: T(p,q) is a regular fibre of the Seifert fibration of S³ with e = −1/(pq). The fibre slope on ∂νK is pq·μ + λ, and the filling slope Nμ + λ gives the third fibre (pq − N, −1).
  - The sign is forced by |H_1(Y_{−1})| = 1.
  - Checks: S³_{−1}(RHT) = +Σ(2,3,7), S³_{+1}(RHT) = −Σ(2,3,5), and S³_{+2}(RHT) = −S³/O*.
- **Orientation checks by Casson–Walker.** The invariant, in Casson normalisation, was computed from the Seifert invariants by Lescop's formula, checked on Σ(2,3,5), Σ(2,3,7) and Y_{±2}(RHT).
  - λ(Y_{±2}(K)) = ±a_2(K)/2 by the surgery formula. This agrees for all torus knots, and for 4_1 it fixes S³_{+2}(4_1) = M((2,−1),(4,−1),(5,4)) with e = −1/20.
- **Regina and SnapPy.** Recognition of the SnapPy fillings confirms the unoriented Seifert types: (2,3,8), (2,5,8), (2,5,12), and (2,4,5) for 4_1. Regina's names do not track orientation (it gives the same name to S³_{±2}(4_1)), so orientation was fixed by Casson–Walker.

### 1.2 Flat connections (VERIFIED)
- **Untwisted irreducibles.** ρ(h) = (−1)^m and ρ(x_i) ~ e^{πi l_i/a_i}, with 0 < l_i < a_i, l_i ≡ m b_i (mod 2), and the strict spherical triangle inequalities for the angles π l_i/a_i.
- **Twisted connections (w ≠ 0 on Y_{±2}).** These are SO(3) representations of the triangle group, counted as orbits of SU(2) triangle solutions under even sign changes, that do not lift to π_1(Y).
- **Independent enumeration.** For torus knots the same sets were enumerated on the pillowcase:
  - arcs (k, l) with 0 < k < p, 0 < l < q, k ≡ l (mod 2);
  - each arc a straight segment β ≡ k/2 − pq·a between two roots of Δ_K(e^{4πia}) = 0;
  - generators on L_N = {Na + β ∈ ℤ} (untwisted) or L_N^w = {Na + β ∈ 1/2 + ℤ} (twisted).
  The counts agree with the Seifert enumeration in all cases checked: 54 (knot, slope) cases in `test_torus.py`, and every torus knot with pq ≤ 200 in `scan.py`.
- **Dictionary between the two descriptions.** On the generator of the arc (k,l) at parameter a, the Seifert rotation numbers are (k·b_1 mod p, l·b_2 mod q, 2a(pq − N)), because x_1 = x^{−b_1}, x_2 = y^{−b_2} and x_3 = μ.
- **The involution ι = ⊗χ.** It maps (a, β) to (1/2 − a, −β). For even N it preserves L_N; for odd N it maps L_N to L_N^w.
  - Untwisted generators of Y_{±2} always come in ι-pairs.
  - Twisted generators fixed by ι do occur: they sit at a = 1/4 with λ ↦ +1 and are binary dihedral. Examples are T(2,3), T(2,5) and 4_1; there are none when det K = 1.

### 1.3 Chern–Simons, grading, f, ℓ (VERIFIED)
- **Chern–Simons.** CS is DLME's: an instanton from α to α′ has energy CS~(α) − CS~(α′), and CS~(θ) = 0.
  - For torus knots, CS mod 1 is given by the Kirk–Klassen path integral along the arc starting at its first endpoint a_+:
    CS(Y_N, x) ≡ −pq(a² − a_+²) + N a² (mod 1).
  - Independently, the lens-space decomposition of §1.4 gives CS mod 1/4 = Σ_i −l_i² ν_i*/(4a_i), with ν_i ν_i* ≡ 1 (mod a_i).
  - The two agree on every generator.
- **Grading.** gr(α) is the index on ℝ × Y from α to θ, and "d" in ℓ = inf_d(κ(d) − d/8) is this ℤ-lift.
- **f.** f = CS~ − gr/8 does not depend on the lift. ℓ is the least birth level of an infinite bar in the f-filtered homology, so ℓ = min f when the differential vanishes. ℓ⁺ is the largest birth level.
- **The APS formula.** With trivial bundle and reference θ (h⁰ = 3), DLME's index formula gives
  **f(α) = (3 + ρ_ad(α))/16,**
  where ρ_ad is the APS ρ-invariant of the adjoint flat bundle. This reproduces DLME's Example 3.7.
  - With reference χθ the result is the same.
  - Orientation reversal: f_{−Y} = 3/8 − f_Y, hence ℓ(−Y) = 3/8 − ℓ⁺(Y) and the gap of K̄ equals ℓ⁺(Y_2(K)) − ℓ⁺(Y_{−2}(K)).
- **SU(2) versus SO(3).** Passing to the full SO(3) gauge group identifies α with α ⊗ χ. That shifts (CS, gr) by (1/2, 4) and leaves f unchanged. So ℓ is the same in the SU(2) and SO(3) normalisations, and nothing in it involves a factor 4.

### 1.4 The ρ-formula for Seifert-fibred rational homology spheres (VERIFIED: derivation plus independent checks)
**Formula.**

  ρ_ad(M, α) = 3 sgn(e) + Σ_i ρ_L(a_i; ν_i; l_i),  with ν_i ≡ −b_i (mod a_i),

  ρ_L(a; ν; l) = (1/a) Σ_{k=1}^{a−1} 4 sin²(πlk/a) cot(πk/a) cot(πνk/a).

**Derivation.**
1. Let W be the orbifold disc bundle over S²(a_1, a_2, a_3) with ∂W = M. The flat SO(3) connection ad α (on which h acts trivially) extends flatly over W.
2. Remove cone neighbourhoods of the singular points. These are C²/Z_{a_i} with weights (1, ν_i): 1 along the zero-section, ν_i along the fibre.
3. Apply APS to the resulting manifold W°. The signature of W° is sgn(e), and the twisted signature vanishes because H*_orb(B; ad α) = 0 for a rigid irreducible triangle representation.
4. The local weights come from toric geometry. In the fan of C²/Z_a with weights (1, ν), the Hirzebruch–Jung chain a/ν = [c_1, …, c_k] starts next to the divisor {w = 0}, which is the zero-section. So ν_i = β_i = −b_i.
   - This was derived, not calibrated. The sibling `ell-1.md` instead chose its cone data "by integrality among 16 candidates".
5. ρ_L is the APS ρ of the flat SO(3) bundle (rotation by 2πl/a) on S³/Z_a with the link orientation. It uses the finite-group formula ρ_E(S³/G) = (1/|G|) Σ_{g≠1}(dim E − tr E(g)) cot(θ_1/2) cot(θ_2/2).

**Lens identity used repeatedly (VERIFIED, proof).** ρ_L(m; 1; l) = 4l(m − l)/m − 2 for 0 < l < m.
- The second difference in l of the sum equals −8/m + 2([l = 1] + [l = m−1]).
- Together with symmetry under l ↦ m − l this forces the stated quadratic.
- It was also checked exactly for all m < 30.

### 1.5 The twisted normalisation (VERIFIED for pq even; PLAUSIBLE for pq odd)
- On (Y_{±2}, w) the only reducible flat connection is ζ: μ ↦ rotation by π, with ad ζ = ℝ ⊕ χ ⊕ χ, h⁰ = 1 and h¹ = 0.
- With CS~(ζ) = 0 and gr_ζ(α) = ind(α → ζ), the same index argument as in §1.3 gives
  f^w(α) = (1 − ρ(ζ) + ρ_ad(α))/16, with ρ(ζ) = 2ρ_χ(Y).
- **ρ_χ = −σ(K).** The Seifert formula for the real line bundle χ applies when χ(h) = 1, that is when pq is even. It gives ρ_χ(Y_{±2}(T(p,q))) = −σ(T(p,q)) on both Y_2 and Y_{−2} for twelve torus knots (T(2,q) with q ≤ 13, T(3,4), T(3,8), T(4,5), T(4,7), T(5,6), T(6,7)), and 0 for 4_1. For pq odd I use the Casson–Gordon form ρ_χ = −σ(K), which is the same for Y_2 and Y_{−2}.
- Consequences:
  - The twisted gap does not depend on this normalisation.
  - f^w differs from the formal (3 + ρ)/16 by the constant (1 − σ)/8, the same on both sides.
  - Orientation reversal acts by f^w_{−Y} = 1/8 − f^w_Y.

---

## 2. Independent checks of the machinery (all VERIFIED)

| check | result |
|---|---|
| DLME Example 3.7: Σ(2,3,5) by the Seifert formula | ρ = −73/15 and −97/15, so f = −7/60 and −13/60; CS mod 1/4 is 1/120 and 49/120 − 1/4. Exact match. |
| Finite-group ρ on S³/I* (both representations), S³/O*, S³/T* | Matches the Seifert formula (−14/3 for S³/O* = −Y_2(RHT)). |
| CS of the Galois-conjugate representation of I* from the degree of an equivariant map | 7² = 49 mod 120. Matches. |
| Seifert versus pillowcase enumeration (54 knot/slope cases; scan to pq ≤ 200) | Counts, ρ multisets and CS mod 1/4 all agree. |
| gr = 8(CS − f) ∈ ℤ for every generator (CS mod 1 from the pillowcase, f from the Seifert ρ) | All integral, untwisted and twisted. |
| **ℤ/8-graded ranks:** I(Y_1) against I(Y_2), and I(Y_{−2}) against I(Y_{−1}). The handle maps have degree 0 and are F_2-isomorphisms (DLME's Remark; (H1)). | Equal as multisets of gradings mod 8, for all 12 knots tested, including T(5,7) with rank 96. |
| Floer's triangle mod 4: I_*(Y_{−1}) ≅ I_{*−3}(Y_1) | Holds in all 12. |
| Rank: rank I(Y_{±2}) = 4·\|λ_CW(Y_{±2})\| = Δ''_K(1) = rank I(Y_{±1}) | All torus knots with pq ≤ 200. |
| DLME's inequalities ℓ(Y_{−1}) < ℓ(Y_{−2}), ℓ(Y_2) < ℓ(Y_1), ℓ(Y_{−1}) < ℓ(Y_1) − 1/8 | Hold in all 402 cases. |
| Vanishing of the Floer differential by parity (`parity_scan.py`) | All gradings of each (Y, bundle) have one parity in all 1206 cases: pq ≤ 200, with Y_{±2} untwisted and twisted and Y_{±1}. So ℓ = min f and ℓ⁺ = max f. |
| Agreement with `ell-1.md` and `pillowcase-1.md` | Exact on every overlapping number, including 4_1 (1/10) and the twisted values. |
| Twisted ranks | rank I^w(Y_{−2}) − rank I^w(Y_2) = −σ(K) for positive torus knots (2, 4, 6, 8 for T(2,3), T(2,5), T(3,4), T(3,5)). |

The grading check deserves comment. It uses only the degree-0 handle isomorphisms and the Brieskorn-sphere gradings. It therefore tests the ρ-values (mod 16) of the ±2 surgeries independently of any calibration.

---

## 3. Data

### 3.1 Two examples in full (VERIFIED)
Positive knot, trivial bundle. Columns: arc, a, CS (mod 1), gr (mod 8), ρ_ad, f.

**T(2,3).**
- Y_2 = −S³/O*:
  - (1,1), a = 1/8: CS 47/48, gr 4, ρ 14/3, f 23/48
  - (1,1), a = 3/8: CS 23/48, gr 0, ρ 14/3, f 23/48
- Y_{−2} = M((2,1),(3,−1),(8,−1)):
  - (1,1), a = 3/16: CS 73/96, gr 3, ρ 19/6, f 37/96
  - (1,1), a = 5/16: CS 25/96, gr 7, ρ 19/6, f 37/96
- Gap: 3/32.
- Twisted:
  - Y_2^w has one generator, ι-fixed, at a = 1/4: f^w = 1/6.
  - Y_{−2}^w has f^w ∈ {−1/12 (twice), 1/24}.
  - Twisted gap: 1/4.

**T(2,5).**
- Y_2:
  - f = 79/160 at a = 1/16 and 7/16; these realise ℓ.
  - f = 111/160 at a = 3/16 and 5/16 on arc (1,3).
  - f = 119/160 at a = 3/16 and 5/16 on arc (1,1).
- Y_{−2}:
  - f = 37/80 at a = 1/8 and 3/8; these realise ℓ.
  - f = 139/240 and 151/240.
- Gap: 79/160 − 74/160 = **1/32**.
- The minimisers are the generators nearest the point a_e = 1/20, the first root of Δ, where arc (1,1) leaves the reducible line.
  - Y_2's generator is at phase θ_2 = (n − 2)(a − a_e) = 1/10.
  - Y_{−2}'s is at phase θ_{−2} = 9/10. This is the trapping of §5.4.

### 3.2 ℓ for torus knots (VERIFIED; all rows exact)

| K | ℓ(Y_{−2}) | ℓ(Y_2) | gap | ℓ⁺-gap (= gap of K̄) | twisted gap |
|---|---|---|---|---|---|
| T(2,3) | 37/96 | 23/48 | 3/32 | 3/32 | 1/4 |
| T(2,−3) | −5/48 | −1/96 | 3/32 | 3/32 | 1/8 |
| T(2,5) | 37/80 | 79/160 | **1/32** | 11/96 | 1/3 |
| T(2,−5) | −59/160 | −61/240 | 11/96 | 1/32 | 1/8 |
| T(2,7) | 225/448 | 167/336 | **−1/192** | 23/192 | 17/48 |
| T(2,−7) | −209/336 | −225/448 | 23/192 | −1/192 | 1/8 |
| T(3,4) | 163/336 | 119/240 | **3/280** | 33/280 | 97/280 |
| T(3,−4) | −67/120 | −37/84 | 33/280 | 3/280 | 1/8 |
| T(3,5) | 1039/2040 | 97/195 | **−21/1768** | 219/1768 | 631/1768 |
| T(3,−5) | −1169/1560 | −319/510 | 219/1768 | −21/1768 | 151/1768 |
| T(4,5) | 471/880 | 359/720 | **−29/792** | 1/8 | 289/792 |
| T(4,−5) | −89/80 | −79/80 | 1/8 | −29/792 | 97/792 |
| T(5,6) | 1081/1920 | 839/1680 | −57/896 | 111/896 | 83/224 |
| T(5,−6) | −1003/560 | −1067/640 | 111/896 | −57/896 | 1/8 |
| T(8,25) | 49701/80800 | 39599/79200 | −9209/79992 | 1/8 | 29989/79992 |

**Scan statistics** (`scan.py`; 201 torus knots with pq ≤ 200, both chiralities; `scan_table.txt`):
- Positive knots: the gap ranges from −0.1151 (T(8,25)) to 3/32 (T(2,3)).
- Negative knots: the gap lies in [3/32, 1/8].
- |gap| < 1/16 for exactly the eleven positive knots with 10 ≤ pq ≤ 29.
- Twisted gaps: at least 0.0854 (T(3,−5)); for positive knots they lie in [1/4, 3/8).
- ±1 gaps: in (1/8, 1/4]. The value 1/4 is attained, for example by T(3,−5).
- Every row satisfies the closed forms of §4 exactly.

**Where ℓ is realised.**
- Positive knots: at the generators adjacent to the point a = 1/(2pq), the first root of Δ_K(e^{4πia}), where an arc leaves the reducible line.
- Negative knots: near a = 1/4, on an arc of maximal κ (κ as in Theorem 4.1).
- The gap equals 1/8 exactly when both minima sit at a common traceless generator (λ ↦ −1), for example T(4,−5).

### 3.3 The figure-eight knot (VERIFIED)
- S³_2(4_1) = M((2,−1),(4,−1),(5,4)) and S³_{−2}(4_1) is its reverse.
- Each has one ι-pair of irreducible SU(2) connections:
  - on Y_2: ρ_ad = 4/5, f = 19/80, all gradings odd;
  - on Y_{−2}: ρ_ad = −4/5, f = 11/80, all gradings even.
- **Gap: 1/10**, which equals ρ_ad/8. For an amphichiral knot the gap is (min ρ + max ρ)/16.
- Twisted:
  - two SO(3) connections on each side, with ρ = 1/5 and 9/5 on Y_2, and the negatives on Y_{−2};
  - ρ_χ = 0;
  - f^w = 3/40 and 7/40 against −1/20 and 1/20;
  - the gradings on each side have one parity;
  - **twisted gap 1/8** (both ℓ and ℓ⁺).
- Both twisted pairs sit at the binary dihedral double point (1/4, 0) and differ by exactly 1/8 there.
- The character curve of 4_1 meets the reducible line nowhere (Δ has no roots of modulus one).
- Its slope at the double point is exactly ±√20, from cos 2πβ = cos 8πa − cos 4πa − 1. So the local bound of §5.3 at that crossing is 1/8 − 1/(20 − 4) = 1/16 on the nose (SPECULATIVE whether this is meaningful).

---

## 4. Exact structure for torus knots

**Theorem 4.1 (arc formula; VERIFIED).** Let K = T(p,q) be positive, n = pq, N ≠ 0 with N < n. Let x be the generator of Y_N on the arc (k,l) with parameter a. Then

  f(Y_N, x) = κ_{kl} + 3 sgn(N)/16 + (n − N)·a(1/2 − a),

where κ_{kl} = (1 + ρ_L(p; −b_1; kb_1) + ρ_L(q; −b_2; lb_2))/16 does not depend on N.

For the mirror:
  f(Y_N(K̄), x) = 3/8 − κ_{kl} + 3 sgn(N)/16 − (n + N)·a(1/2 − a).

*Proof.*
1. By §1.4, f = (3 + 3 sgn e + ρ_1 + ρ_2 + ρ_3)/16, and sgn e = sgn N for N < n.
2. The third fibre (n − N, −1) has ν = 1 and l_3 = 2a(n − N). The lens identity gives ρ_3 = 16(n − N)·a(1/2 − a) − 2.
3. Collect terms. The mirror follows from f_{−Y} = 3/8 − f_Y. ∎

The constancy of κ_{kl} over N ∈ {±1, ±2, ±3} was also checked by machine (`phi_check.py`).

**Theorem 4.2 (Φ where arcs leave the reducible line; VERIFIED on all 4996 such endpoints for pq ≤ 120).** Put Φ_{kl}(a) := κ_{kl} + n·a(1/2 − a), the N-independent part. At each endpoint a_e of an arc,

  Φ_{kl}(a_e) = (3 − σ_−(ω_e) − σ_+(ω_e))/16,  ω_e = e^{4πia_e},

where σ_∓ are the Levine–Tristram signatures of K just before and after ω_e. For positive torus knots the values are 5/16, 9/16, 13/16, … at the 1st, 2nd, 3rd, … root.

Interpretation (PLAUSIBLE): along the reducible arc, Φ = (3 − 2σ_K(e^{4πia}))/16. This is the Casson–Gordon ρ-invariant of the abelian adjoint connection, and Φ is continuous where arcs leave the reducible line.

**Theorem 4.3 (closed forms; VERIFIED exactly for all 201 torus knots with pq ≤ 200, both chiralities; general proof sketched).**
For positive T(p,q) with n = pq:
- ℓ(Y_2) − ℓ(Y_{−2}) = G_2(n) = −(n² − 16n + 36)/(8(n² − 4));
- ℓ(Y_1) − ℓ(Y_{−1}) = G_1(n) = (n² + 6n − 11)/(8(n² − 1));
- ℓ^w(Y_2) − ℓ^w(Y_{−2}) = G_2^w(n) = (3n² − 44)/(8(n² − 4)).

For negative T(p,q):
- ℓ(Y_2) − ℓ(Y_{−2}) = 1/8 − 4m²/(n² − 4), with m = dist(1/2 − k/2 + n/4, ℤ) ∈ {0, 1/4, 1/2} for the arc of maximal κ.
- Concretely, m = 1/4 when n is odd, and m ∈ {0, 1/2} according to the parity of k when n is even.

Equivalent forms: G_2(n) = −1/8 + (2n − 5)/(n² − 4), G_1(n) = 1/8 + (3n − 5)/(4(n² − 1)), G_2^w(n) = 3/8 − 4/(n² − 4).
- G_2 changes sign between n = 13 and n = 14 (the root is 8 + 2√7 ≈ 13.29).
- G_2 ≥ 1/16 only for n ≤ 7, which among torus knots means only the trefoil.
- G_2 ≤ −1/16 for n ≥ 30 (the root is 16 + 6√5 ≈ 29.4).

*Proof sketch* (PLAUSIBLE as a full proof; the identities are exact):
1. By Theorem 4.1, f is concave in a on every arc of a positive knot. So its minimum over the generators of one arc is at a generator next to an endpoint.
2. The generator of Y_N next to the left endpoint a_e has phase θ_N = (n − N)(a − a_e) = {N a_e}. Its value is
   Φ_e + 3 sgn(N)/16 − N a_e(1/2 − a_e) + θ_N(1/2 − 2a_e) − θ_N²/(n − N).
3. By Theorem 4.2 and the monotone, step-by-−2 Levine–Tristram function of a positive torus knot, Φ_e = (1 + 4j)/16 at the j-th root. So Φ_e ≥ 5/16, with equality exactly at a_e = 1/(2n) and its ι-image 1/2 − 1/(2n).
   - At the first root θ_2 = 1/n is tiny while θ_{−2} = 1 − 1/n is near 1.
   - That the first root beats every later endpoint, whose Φ_e is larger by 1/4 or more but whose phase and band terms may be smaller, is an inequality I have checked exactly for all pq ≤ 200 but not proved in general.
4. Substituting a_e = 1/(2n), θ_2 = 1/n and θ_{−2} = 1 − 1/n gives G_2. The same with θ_1 = 1/(2n) at a_e and θ_{−1} = 1/2 − 1/(2n) at 1/2 − a_e gives G_1. The twisted phases 1/2 ± 1/n give G_2^w.
5. Negative knots: f is convex in a. The minimum over generators sits next to a = 1/4 on the arc of maximal κ. With the generator offsets (θ + ℤ)/(n ± 2), θ = 1/2 − β_0, this gives 1/8 − 4m²/(n² − 4). ∎

**Corollary 4.4 (status of the claim on torus knots; VERIFIED).**
- |ℓ(Y_2) − ℓ(Y_{−2})| ≥ 1/16 fails exactly for the positive torus knots with 10 ≤ pq ≤ 29.
- It holds, with the gap positive, for all negative torus knots (gap ≥ 3/32) and for T(2,3).
- It holds, with the gap negative, for positive torus knots with pq ≥ 30.
- The one-sided statement ℓ(Y_2) ≥ ℓ(Y_{−2}) + 1/16 fails for every positive torus knot except T(2,3).
- The reverse one-sided statement fails for every negative torus knot.
- The only clean uniform statements for torus knots are:
  - (a) max(gap(K), gap(K̄)) ≥ 3/32;
  - (b) the twisted gap is at least 0.0854;
  - (c) the gap lies in (−1/8, 1/8], and the ±1 gap lies in (1/8, 1/4].

---

## 5. Where the 1/16 comes from, and why it does not control ℓ in general

### 5.1 The band picture (VERIFIED for torus knots; PLAUSIBLE in general)
Write the arc formula as

  f(Y_N, x) = Φ(x) + 3 sgn(N)/16 − N·a(1/2 − a),  with Φ = κ + n·a(1/2 − a).

This is the pillowcase sibling's formula f = Φ + (3 sgn N − N)/16 + Nδ², since Nδ² − N/16 = −N a(1/2 − a). There it is stated as a conjecture in general, with a Maslov term on branches less steep than L_N.

- **Φ is the f-function of the twisted zero-surgery.** With N = 0 the formula gives f(Y_0^w, x) = Φ(x) on C ∩ L_0^w, in the symmetric normalisation f = (3 + ρ)/16, the one for which f_{−Y} = 3/8 − f_Y. For torus knots e(Y_0) = 0, so 3 sgn e = 0.
- **The ±2 bands.** Since 0 ≤ a(1/2 − a) ≤ 1/16, with the maximum at a = 1/4:
  - f(Y_2, x) − Φ(x) ∈ [1/16, 3/16];
  - Φ(x) − f(Y_{−2}, x) ∈ [1/16, 3/16].
  Inner edge (3 − 2)/16 at traceless points; outer edge 3/16 at the reducible corners a = 0, 1/2.
- **The ±1 bands** are ±[1/8, 3/16].
- **Why it is 1/16.** The N-dependence splits as a Chern–Simons part Na² and a grading part −Na/2.
  - The Chern–Simons part is the solid-torus boundary term of Kirk–Klassen, 2∫α dβ + Na².
  - The grading part is the solid-torus spectral flow, the "4Nα" of the grading.
  - At a = 1/4 they total N/16 − N/8 = −N/16.
  - The term 3 sgn(N)/16 is the APS term 3(1 + b⁺(X_N))/8 split symmetrically; its 3 is h⁰(θ) = dim SU(2).
  - Hence ±(3 − 2)/16 = ±1/16 for N = ±2.
  - The a² = (1/4)² = 1/16 of observation (iv) enters through the Chern–Simons part, as N a² = +2/16. The spectral-flow part contributes −N a/2 = −4/16. The net solid-torus term is −2/16, and adding the signature term 3/16 gives 1/16.
- **Classical invariants cannot be the source.** The linking form of Y_{±2} is 1/2 on ℤ/2 for both signs. The Rokhlin invariants of the two spin structures are {1/8, −1/8} (mod 2) on both Y_2 and Y_{−2}: the trace X_{±2} is spin of signature ±1, and the other spin structure has characteristic vector 2.
- **Common generators.** The generators shared by Y_2, Y_0^w and Y_{−2} are the traceless ones with λ ↦ −1. At them:
  - f(Y_2) − f(Y_0^w) = f(Y_0^w) − f(Y_{−2}) = 1/16 exactly;
  - f(Y_2) − f(Y_{−2}) = 1/8.

### 5.2 Three-level data: Y_2, Y_0^w, Y_{−2} (VERIFIED; `zero_surgery.py`)

| K | ℓ(Y_2) − ℓ(Y_0^w) | ℓ(Y_0^w) − ℓ(Y_{−2}) |
|---|---|---|
| T(2,−3) | 0.0521 | 0.0417 |
| T(2,−7) | 0.0603 | 0.0595 |
| T(3,−5) | 0.0620 | 0.0619 |
| T(4,−5) | **1/16** | **1/16** |
| T(5,−6) | 0.0620 | 0.0619 |
| T(2,7) | −0.0119 | +0.0067 |
| T(4,5) | −0.0264 | −0.0102 |
| T(5,6) | −0.0381 | −0.0255 |

- For negative torus knots the three ℓ's are equally spaced by about 1/16, and exactly 1/16 for T(4,−5).
- For positive knots the order breaks down.
- Only the sum of the two columns is independent of how Y_0^w is normalised. The equal split holds in the symmetric normalisation.

This is the precise sense in which 1/16 is a half-step: Y_{±2} sit 1/16 on either side of the twisted zero-surgery at the traceless representations.

Interpretation (SPECULATIVE): this is the configuration of the distance-two maps g_+: C(Y_2) → C(Y_0, w) and g_−: C(Y_0, w) → C(Y_{−2}) in the conjectural factorisation B ≃ g_− ϑ g_+. If each were an injective IP-morphism of level −1/16, ℓ(Y_{−2}) ≤ ℓ(Y_2) − 1/8 would follow. Positive torus knots show that this cannot hold in general.

### 5.3 Local model at a traceless crossing (exact for torus knots; PLAUSIBLE in general)
Take a branch of C of slope s through (1/4, β_0), with |s| > 2.
- On it, f_N = Φ_0 + (3 sgn N − N)/16 + (s + N)δ².
- Generators of Y_{±2} satisfy (s ± 2)δ ∈ θ + ℤ, with θ = 1/2 − β_0 untwisted and θ = −β_0 twisted; this is the same θ for both signs.
- With m = dist(θ, ℤ) and s > 2 (convex), the minima near the crossing give the

  **local gap 1/8 − 4m²/(s² − 4)**, which lies in [1/8 − 1/(s² − 4), 1/8].

Remarks:
- The local gap is at least 1/16 whenever s² ≥ 20.
- For torus knots s = pq ≥ 6, so it is at least 3/32. This is exactly the negative-torus-knot formula.
- For ι-invariant arcs in the untwisted theory, m = 1/2 always: a generator at a = 1/4 would be ι-fixed, which is impossible.
- If s < −2 (concave), the traceless point is a local maximum of f, and ℓ is decided elsewhere. It then governs ℓ⁺ instead, which is why max(gap(K), gap(K̄)) ≥ 3/32 for torus knots.

### 5.4 Local model where an arc leaves the reducible line: the trapping (exact for torus knots; PLAUSIBLE in general)
Take a concave branch (s < −2) leaving the reducible line at a_e < 1/4, with δ_e = a_e − 1/4.
- f increases inward from the endpoint.
- The generator of Y_N next to a_e has phase θ_N = {N a_e}, and
  f ≈ Φ_e + 3 sgn(N)/16 − N a_e(1/2 − a_e) + 2|δ_e| θ_N.
- For N = ±2, θ_2 = 2a_e and θ_{−2} = 1 − 2a_e, so

  **local gap ≈ 1/8 + 4δ_e² + 2|δ_e|(θ_2 − θ_{−2}) = 1/8 − 4δ_e²**,

  plus terms of order 1/|s|. This is below 1/16 iff |δ_e| > 1/8, that is iff the root ω_e = e^{4πia_e} has positive real part. It tends to −1/8 as ω_e → 1.
- **Why even N is special.** ι maps the arc to an arc with endpoint 1/2 − a_e and the same Φ_e.
  - For even N, ι preserves L_{−N}. So at 1/2 − a_e, Y_{−N} sees the same phase {−N a_e} = 1 − N a_e ≈ 1 as at a_e.
  - Y_{−N} is therefore trapped at phase ≈ 1 at both of its best endpoints.
- **Odd N.** ι maps L_N to L_N^w, and the far end offers Y_{−1} the phase 1/2 − a_e. The same computation gives

  **local gap 1/4 − 2δ_e² ≥ 1/8** (±1 surgery).

  So DLME's 1/8 is the |δ_e| → 1/4 limit, attained asymptotically by torus knots (G_1 ↓ 1/8).
- Confirmation of the parity effect. For positive torus knots, as pq → ∞, the ±N gaps tend to +1/8 for N = 1, 3 and to −1/8 for N = 2, 4. At pq = 143 the values are 0.130, −0.111, 0.130, −0.112 (`closedform2.py`).

### 5.5 The nontrivial bundle (VERIFIED for torus knots and 4_1; PLAUSIBLE as a mechanism)
- The twisted lines L_{±2}^w meet the reducible line at ζ = (1/4, 0), not at θ.
- At an endpoint a_e the twisted phases are {±2a_e + 1/2} = 1/2 ± 2a_e. Hence

  **local gap^w = 1/8 + 2|δ_e| − 4δ_e² ≥ 1/8.**

  This tends to 3/8 as a_e → 0, which is G_2^w.
- At traceless crossings the twisted local gap is 1/8 − 4m_w²/(s² − 4), with m_w = dist(β_0, ℤ). It equals 1/8 exactly at twisted common points (λ ↦ +1). Examples: T(2,−q), 4_1.
- Some twisted values fall below 1/8 − 1/(s² − 4). All of them are knots with pq odd: T(3,−5) at 0.0854, T(5,−9) at 0.1132, T(7,−11) at 0.1183, T(7,−13) at 0.1194.
  - In each case the minimising arcs end within 0.017 of a = 1/4. Examples: [7/30, 13/30] for T(3,−5), [0.2444, 0.3556] for T(5,−9), [0.2468, 0.3896] for T(7,−11).
  - The arc end cuts off the generator that would sit next to the crossing.
  - This is a third local configuration: a point where an arc leaves the reducible line close to the traceless line. It costs at most of order 1/(s − 2).
- So in all Seifert examples the twisted form of the claim holds, with a structural reason: no trapping near reducibles.

### 5.6 A chirality-independent quantity (VERIFIED; remark)
Let mean f denote the average of f over generators. Since f_{Y_N(K̄)} = 3/8 − f_{Y_{−N}(K)}, the mean gap mean f(Y_2) − mean f(Y_{−2}) is the same for K and K̄.
- For T(2,q) it equals q²/(12(q² − 1)), checked exactly for q ≤ 21; this tends to 1/12.
- Over all torus knots with pq ≤ 200 it lies in [0.0753, 0.0938].
- The mean birth level of infinite bars is a diffeomorphism invariant, and it would vanish for a cosmetic pair. A positive lower bound for all knots would therefore suffice. I have no formula for the sum of adjoint ρ-invariants over a character variety (SPECULATIVE).

---

## 6. Double covers (VERIFIED computations; the halving heuristic is refuted for torus knots)

For p, q odd:
- The connected double cover of Y_{±2}(T(p,q)) is the fibrewise double cover M((a_i, −b_i(a_i − 1)/2)) = ∓Σ(p, q, pq ∓ 2). Its Euler number is e/2.
- It is Σ_{±1}(K̃) with K̃ ⊂ Σ(2,p,q).
- Pull-back preserves the adjoint rotation numbers and sends h̃ ↦ 1. In the local weights, ν_i is replaced by ν_i/2 (mod a_i).

Results (`cover.py`, `cover_detail.py`):
- **Upstairs gap** ℓ(Σ_1(K̃)) − ℓ(Σ_{−1}(K̃)), for T(3,5), T(3,7), T(5,7), T(3,11), T(5,9), T(3,13), T(7,9), T(5,11): 0.373, 0.231, 0.346, 0.375, 0.375, 0.298, 0.375, 0.193. All exceed 1/8. Downstairs the gaps are −0.012, −0.040, −0.072, −0.069, −0.083, −0.077, −0.095, −0.090.
- **Restricted to pulled-back generators,** the upstairs gap is 0.373 to 0.375, tending to 3/8.
- **Generators.** The upstairs generators are the union of the pull-backs of the untwisted and the twisted downstairs SO(3) connections. For T(3,5) at N = 2 that is 14 = 8 + 6.
- **f does not halve.** For a pulled-back generator f̃ = 2f + k/8 with k ∈ ℤ. This holds because CS doubles and gradings are integers. But k varies between generators: −16, −6, −14, −12, −10, −8 for T(3,5) at N = 2.
  - The reason: ρ_ad(Ỹ, π*α) = ρ_ad(Y, α) + ρ(Y, ad α ⊗ χ), and the second, χ-twisted term is not controlled by f(α).
  - So there is no relation of the form "ℓ downstairs equals half of ℓ upstairs".
  - The 1/8 = 2 × 1/16 numerology of observation (iii) holds pointwise at traceless generators, as in §5.1, but does not transfer to ℓ.

---

## 7. Proposed structural explanation, precise statements, status

**Explanation.**
1. **Normalisation.** ℓ is measured in units of 1/16 because f = (3 + ρ_ad)/16: the APS coefficient 1/2 on ρ, divided by the 8 of d/8. A gap of 1/16 is a unit change in the adjoint ρ-invariant.
2. **Band.** Relative to the slope-independent function Φ on the character variety, which is the f-function of the twisted zero-surgery, Y_2 lies in Φ + [1/16, 3/16] and Y_{−2} in Φ − [1/16, 3/16].
   - The inner edge **1/16 = (3 − |N|)/16** is attained exactly at the traceless representations, the common generators of Y_2, Y_0^w and Y_{−2}.
   - Here 3/16 is the signature/b⁺ term of the trace times dim SU(2), and |N|/16 is the net solid-torus term at holonomy i.
   - At |N| = 1 the same edge is 1/8, which is DLME's constant.
3. **Transfer to ℓ.** The band separates the two spectra pointwise by 1/8 = 2 × 1/16. ℓ inherits a 1/16-size separation only when both minima sit near traceless crossings:
   - convex branches: local gap 1/8 − 4m²/(s² − 4);
   - this is the case for negative torus knots (gap ≥ 3/32) and for 4_1 (gap 1/10).
4. **Failure.** Near reducible points where arcs leave the reducible line (roots of Δ_K on the unit circle), concave branches carry the minima. For even N the χ-symmetry traps Y_{−N} at phase ≈ 1, and the local gap is 1/8 − 4δ_e² → −1/8.
   - Positive torus knots realise this exactly: G_2(n) = −(n² − 16n + 36)/(8(n² − 4)).
   - For odd N there is no trap, which is why DLME's ±1 theorem holds (G_1 ↓ 1/8).
5. **Nontrivial bundle.** The twisted lines avoid θ, so the trap is absent and the local gap near reducibles is at least 1/8. This is why "similar claims hold in the presence of a nontrivial bundle", and more robustly than in the untwisted case.

**Statements and status.**

| | statement | status | confidence |
|---|---|---|---|
| (S1) | f = (3 + ρ_ad)/16 (trivial bundle); f^w = (1 − ρ(ζ) + ρ_ad)/16 with ρ(ζ) = −2σ(K) | VERIFIED (APS; DLME example; checks of §2). ρ(ζ) = −2σ(K) is VERIFIED for pq even and PLAUSIBLE in general | 95% |
| (S2) | Theorem 4.1 (arc formula) and Theorem 4.2 (Φ at the points where arcs leave the reducible line, via Levine–Tristram) | VERIFIED: proof from the Seifert ρ-formula; 4996 endpoints checked | 95% |
| (S3) | Theorem 4.3: closed forms G_2, G_1, G_2^w and the mirror formula | VERIFIED exactly for pq ≤ 200 in both chiralities; general proof sketched, PLAUSIBLE | 95% for the computed cases, 85% for the general proof |
| (S4) | The universal claim \|ℓ(Y_2) − ℓ(Y_{−2})\| ≥ 1/16 fails (eleven torus knots); no one-sided version holds for all knots | VERIFIED, given (S1); agrees with two independent sibling computations | 92% (residual risk: a different normalisation of ℓ on the user's side) |
| (S5) | Band picture and local models (§5.1, §5.3–5.5) for general knots | PLAUSIBLE: exact for torus knots, consistent with 4_1, and agrees with the pillowcase sibling's Conjecture 5.1 | 70% |
| (S6) | **Conjecture U_Δ:** if Δ_K = 1 (more generally, if no arc of irreducibles meets the reducible line on a concave branch with \|a_e − 1/4\| > 1/8), then ℓ(Y_2) − ℓ(Y_{−2}) ≥ 1/16 | SPECULATIVE. Positive evidence: 4_1 (1/10) and all negative torus knots. Negative evidence: knots with Δ_K = 1 need generators of both parities (statements.tex, Corollary 1.4), so branches with \|s\| < 2 and Maslov jumps must occur; torus knots cannot test this | 25% |
| (S7) | **Conjecture W:** ℓ^w(Y_2) − ℓ^w(Y_{−2}) ≥ 1/16 for every nontrivial K (twisted, ζ-normalised) | SPECULATIVE; true in all 403 Seifert cases (minimum 0.0854); mechanism §5.5 | 35% |
| (S8) | Double-cover halving of ℓ | Refuted for torus knots (§6); f̃ ≡ 2f only mod 1/8 | 90% |

**What would settle (S6) and (S7).**
- An exact computation of ℓ(Y_{±2}) for a single knot with Δ_K = 1, with its character curve and the Maslov terms.
- The relevant regime is closed curves with no points on the reducible line, where only traceless crossings and tangencies with L_{±2} can move the minima.
- The local bound 1/8 − 4m²/(s² − 4) shows what has to be controlled: the slopes of the character curve at the traceless crossings, which are the points studied in the singular theory of (S³, K).
- The 1/16 threshold corresponds to s² = 20.

---

## 8. Code (`gap16/seifert-code/`)

| script | contents |
|---|---|
| `sfs.py` | Seifert machinery: representations, SO(3) orbits, the ρ-formula with ν = −b, lens ρ, CS mod 1/4, Lescop's Casson–Walker formula, Y_N(T(p,q)) |
| `torus.py` | Pillowcase arcs, generators, CS mod 1, Seifert rotation numbers |
| `fg_check.py` | Finite-group ρ (I*, O*, T*) against DLME's Example |
| `test_anchor.py`, `test_torus.py`, `grading_check.py` | §2 checks |
| `twisted.py`, `twisted_cs_check.py`, `tw_detail.py` | Twisted theory and ρ_χ |
| `ell_tables.py`, `ell_twisted.py`, `gen_tables.py` | ℓ tables and generator lists |
| `closedform.py`, `closedform2.py`, `formulas.py`, `scan.py` | Closed forms and the pq ≤ 200 scan (`scan_table.txt`, `scan_summary.txt`) |
| `phi_check.py`, `phi_bif.py` | Arc formula; Φ at the points where arcs leave the reducible line against Levine–Tristram signatures |
| `zero_surgery.py` | Y_0^w and the three-level data |
| `fig8.py`, `fig8_twisted.py` | Figure-eight knot |
| `cover.py`, `cover_detail.py` | Double covers |
| `meangap.py`, `meangap2.py` | Mean gaps |
| `regina_sfs.py`, `regina_try.py` | SnapPy/Regina identification |
