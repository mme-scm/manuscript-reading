# The 1/16 seen from the pillowcase

Line of attack: Chern–Simons values, gradings and the quantity c = CS − gr/8 of flat connections on Y_N = S^3_N(K), computed from the image of the representation variety of the knot complement in the pillowcase. Every claim carries a label: VERIFIED (proved here, computed exactly, or checked against a source), PLAUSIBLE, or SPECULATIVE. The scripts are in `gap16/pillowcase-code/`. The source used is Boden–Herald–Kirk–Klassen, *Gauge theoretic invariants of Dehn surgeries on knots* (arXiv math/9908020, in `gap16/src-bhkk/`), together with the DLME LaTeX.

## 0. Summary

1. **CS formula (VERIFIED).** In DLME's sign convention,
   CS(Y_N, ρ) ≡ 2∫_γ α dβ + Nα² (mod 1),
   and for p/q surgery it is −2∫ B′dA′. Here (α, β) is a continuous lift of the pillowcase path of ρ. At the traceless points with λ ↦ −1, the only irreducible flat connections that Y_2 and Y_{−2} share, the two CS values differ by exactly 4α² = 1/4. Each differs from the slope-0 value by N·(1/4)² = ±1/8. This is the "a² = 1/16" of the brief. For the nontrivial bundle on one end, the common points sit at a = 1/8 and 3/8. There ΔCS ≡ 1/16 (mod 1/8), which is the SO(3) reducible of energy 1/16 on νS.
2. **c is a ρ-invariant (VERIFIED).** For every nondegenerate irreducible flat α on a rational homology sphere whose reducibles are central,
   c(α) := CS~(α) − i(α)/8 = (3 + ρ_ad(α))/16.
   Here ρ_ad is the APS ρ-invariant of the adjoint flat bundle. Hence ℓ(Y) = (3 + ρ_*)/16, where ρ_* belongs to the generator that realises ℓ, and c(−Y, α) = 3/8 − c(Y, α). This is where the factor 1/16 lives: the APS formula carries ρ with coefficient 1/2, and ℓ divides by 8. Cobordism and family maps only ever shift c by (1/8)ℤ − η.
3. **Seifert fibred surgeries (VERIFIED).** The Fintushel–Stern formula extends to Seifert fibred rational homology spheres with three exceptional fibres: c = (3 + 3 sgn e − 2Σ s(l_i; a_i, b_i))/16. It is checked against FS for Brieskorn spheres, against finite-group ρ-invariants for S³/I*, S³/O* and S³/T*, and against DLME's Example. For torus knots it gives the closed form
   c(Y_N(T_{p,q}), x) = κ_arc + (pq − N + 3 sgn N)/16 − (pq − N)(α − 1/4)²,
   valid for 0 < N < pq or N < 0, in either bundle.
4. **The claimed bound fails for torus knots (VERIFIED, given 3).** With DLME's normalisation, ℓ(Y_2) − ℓ(Y_{−2}) takes the following values for positive torus knots:
   - T(2,3): 3/32
   - T(2,5): 1/32
   - T(2,7): −1/192
   - T(3,4): 3/280
   - T(4,7): −31/520

   So **no mechanism can force |ℓ(Y_2) − ℓ(Y_{−2})| ≥ 1/16 for all knots.** The sign is not uniform either. For the mirrors (negative torus knots) the difference always lies in [3/32, 1/8], and for the figure-eight knot it is exactly 1/10. Reversing orientation conventions only swaps which chirality fails.
5. **Pillowcase formula for c (VERIFIED for torus knots and the figure-eight; PLAUSIBLE in general).** There is a function Φ on the irreducible character curve, independent of the slope, with dΦ = 2(α − 1/4) dβ, such that
   c(Y_N, x) = Φ(x) + (3 sgn N − N)/16 + N(α − 1/4)² − ι_N(x)/8.
   Here ι_N ∈ {0, 1} is a Maslov indicator, which vanishes when the curve is steeper than L_N. Equivalently, the Floer grading is 4(Nα + β) − (3/2) sgn N + const. For the figure-eight knot, Φ − 2∫(α − 1/4)dβ ≡ 3/16 on all 12 generators of S³_N(4_1), N = ±1, ±2, ±3.
6. **Why 1/16 (proposed structural explanation).** At N = ±2 the slope term is ±(1/16 + 2(α − 1/4)²). So every flat connection of Y_2 lies 1/16 or more above the slope-independent level Φ, and every flat connection of Y_{−2} lies 1/16 or more below it, with equality exactly at traceless points. The decomposition is
   1/16 = (3 − |N|)/16 = 3/16 − 2·(1/4)².
   - The 3/16 is the b⁺-term of the trace, 3(1 + b⁺)/8, with 3 = dim SU(2) = h⁰(θ).
   - The 2/16 is |N| times the square of the traceless holonomy.

   At |N| = 1 the same expression gives 1/8, DLME's ±1 constant. This is a numerical coincidence that I have not explained (SPECULATIVE).
7. **Traceless representations.** R(K, i) = C ∩ {α = 1/4} is the common critical set of all the functions c_N, since dc_N = 2(α − 1/4) d(Nα + β). These points are the only places where Y_2 and Y_{−2} share flat connections, and there c(Y_2) − c(Y_{−2}) = 1/8 = 2·(1/16), split ±1/16 about Φ. An instanton from Y_2 to Y_{−2} that breaks along S³ at a traceless flat connection crosses two half-steps of 1/16. This is consistent with the traceless representations obstructing the odd-bundle family map (SPECULATIVE).

## 1. Conventions

### 1.1 Manifolds and orientations
- Y_N = S³_N(K) is the boundary of the trace X_N(K). Its meridian of the filling is Nμ + λ.
- Y_{−N}(K) = −Y_N(K̄), where K̄ is the mirror of K.
- We have S³_{+1}(RHT) = −Σ(2,3,5) and S³_{−1}(RHT) = Σ(2,3,7), where Brieskorn spheres carry their link orientation. Also S³_{+1}(4_1) = Σ(2,3,7), by the Casson invariant, since λ(S³_{+1}(4_1)) = a_2(4_1) = −1 = λ(Σ(2,3,7)). All of these are VERIFIED.
- On Y_{±2}, H_1 = ℤ/2. The reducibles are exactly θ and χθ, both central. The central character χ acts on representations of the knot group by ρ ↦ χρ, that is (α, β) ↦ (α + 1/2, β). It shifts CS by 1/2 and the grading by 4, and fixes c (VERIFIED).
- A traceless ρ with ρ(λ) = −1 satisfies χρ ≇ ρ. A conjugacy χρ = gρg⁻¹ forces ρ to be binary dihedral, and binary dihedral representations have ρ(λ) = 1 because λ ∈ π″ (VERIFIED). So the traceless generators of Y_{±2} come in χ-pairs.

### 1.2 Pillowcase
Write ρ(μ) = e^{2πiα} and ρ(λ) = e^{2πiβ} in a common maximal torus. The pair (α, β) is defined modulo ℤ² ⋊ {±1}, and a ∈ [0, 1/2] is the reduced α. We use:
- L_N = {Nα + β ∈ ℤ}, whose points on C are the generators of Y_N.
- L_N^w = {Nα + β ∈ 1/2 + ℤ}, for the nontrivial SO(3) bundle w on Y_N with N even.
- C, the image of R*(K).
- The traceless line {α = 1/4}.

The intersection L_2 ∩ L_{−2} in the pillowcase is {(0,0), (1/4,1/2), (1/2,0)}, and (1/4, 1/2) also lies on L_0^w. The mixed intersection L_2 ∩ L_{−2}^w is {(1/8, 3/4), (3/8, 1/4)}, and L_2^w ∩ L_{−2}^w ∋ (1/4, 0). All VERIFIED.

### 1.3 Chern–Simons normalisations
- Kirk–Klassen, BHKK and Fintushel–Stern use cs(A) = (1/8π²)∫ tr(A dA + (2/3)A³). Along ASD trajectories on R×Y, oriented by dt∧vol_Y, cs increases: the energy is cs(+∞) − cs(−∞) ≥ 0.
- DLME use E(A) = CS~(in) − CS~(out). Hence **CS_DLME = −cs**.
- Check: DLME list 1/120 and 49/120 for Σ(2,3,5) = ∂(negative E8) = S³_{−1}(LHT). BHKK's Table 1 gives cs = 1/120 and −71/120 ≡ 49/120 on S³_{+1}(RHT) = −Σ(2,3,5). Their Table 2 gives 215/168 and 479/168 on Σ(2,3,7). All three agree with the formula below (VERIFIED).
- SU(2) normalisation is used throughout. The SO(3) energy −p_1/4 agrees with c_2 on liftable bundles. For the nontrivial bundle w on Y_{±2}, CS is well defined mod 1/2 under the full SO(3) gauge group, because the χ-gauge transformation shifts it by 1/2.

### 1.4 Gradings, c and ℓ
- i(α) is the index on R×Y from α to θ (DLME).
- Comparison with BHKK: i_DLME(α; Y) = SF_BHKK(θ → α; −Y). For Brieskorn spheres, i_DLME = R_FS(α) − 3. Both are checked on DLME's Example, where i(α) = 1 and i(β) = 5 for Σ(2,3,5) (VERIFIED).
- c(α) := CS~(α) − i(α)/8 is a real number. It does not depend on the lift, because the periodicity is (CS~, i) ↦ (CS~ + 1, i + 8).
- Any class is born at a critical level of a generator in the same degree, so ℓ(Y) = c(α) for some generator α. For a perfect complex, ℓ(Y) = min_α c(α). The quantity d/8 in ℓ is the ℤ-lift of the ℤ/8 grading, paired with the real lift of CS.

## 2. Chern–Simons values on the pillowcase

**Theorem 2.1 (VERIFIED).** Let ρ be a flat connection on X = S³∖νK in normal form near T = ∂X, joined to the trivial connection by a path γ of flat connections in normal form. Let (α, β) be the continuous lift of its boundary holonomy. Let m = pμ + qλ be the meridian of the filling and ℓ′ = rμ + sλ the core, with ps − qr = 1. Write A′ = pα + qβ and B′ = rα + sβ. If A′(1) ∈ ℤ, so that ρ extends over Y_{p/q}, then

  cs(Y_{p/q}, ρ) ≡ 2∫_γ B′ dA′,  that is,  CS_DLME ≡ −2∫_γ B′ dA′ (mod 1).

For integer N, take r = −1 and s = 0. Then CS_DLME(Y_N, ρ) ≡ 2∫_γ α dβ + Nα(1)².

*Proof.*
1. On a collar, A_t = 2πi(α dx + β dy)σ. Since the path is flat on X, tr(F∧F) vanishes on [0,1]×X. Stokes' theorem on [0,1]×X then gives cs_X(A_1) = ∫(α̇β − αβ̇) dt. This expression is SL₂-invariant: it equals ∫(Ȧ′B′ − A′Ḃ′).
2. Write A′(1) = n and B′(1) = B_1. The gauge transformation exp(−2πi n u σ) on T, where u is the coordinate along m, puts the boundary value into the form 2πi B_1 dv σ, which extends flatly over the solid torus. Its boundary term adds +nB_1 on the X side. The Wess–Zumino term is an integer, because the boundary values lie in a circle and H_3(S³, S¹) = ℤ.
3. Hence cs(Y) ≡ ∫(Ȧ′B′ − A′Ḃ′) + A′B′|₁ = 2∫B′dA′.
4. Under a change of lift by (k, l) ∈ ℤ², or by (α, β) ↦ (−α, −β), the value changes by 2n(rk + sl) + (pk + ql)(rk + sl) ∈ ℤ. So it is well defined. ∎

This is BHKK's Theorem `csthm`, cs = −c + 2∫n dm, reduced mod 1 (their m and n are my A′ and B′). Further checks:
- Lens spaces: CS_DLME(L(p,1), α_k) = −k²/p, matching the reducible of energy k²/p on the disk bundle of Euler number −p.
- Torus knots: on the trefoil arc β = 6(1/12 − α), the formula reproduces 1/120, 49/120 on −Σ(2,3,5) and 47/168, 143/168 on Σ(2,3,7) (KK sign).
- Seifert surgeries: it matches the Seifert-fibred CS mod 1/4 for 8 torus knots × 6 slopes (`csq.py`).
- Figure-eight: one slope-independent constant fits all six Seifert surgeries N = ±1, ±2, ±3 (`fig8_match.py`), although C does not meet θ.

**Corollary 2.2 (common points; VERIFIED).**
- (a) At a traceless point with ρ(λ) = −1 and lift α = 1/4:
  CS(Y_N) − CS(Y_0^w) = N/16, and CS(Y_2) − CS(Y_{−2}) = 4·(1/4)² = 1/4 (mod 1).
  The value 1/4 is twice the area of the triangle between L_2 and L_{−2} from θ to (1/4, 1/2), with area form 2 dα∧dβ, which gives the pillowcase total area 1. It is also the energy −ξ² of the SU(2) reducible on νS with ⟨c_1(L), S⟩ = 1. For the χ-twin, the Y_2 values are c₀ ± 1/4 and the Y_{−2} values are c₀ and c₀ + 1/2, with c₀ := CS(Y_{−2}, ρ). So the two spectra are offset by 1/4 mod 1/2.
- (b) Mixed bundles: at L_2 ∩ L_{−2}^w, where a = 1/8 or 3/8, ΔCS = 4a² ∈ {1/16, 9/16} ≡ 1/16 (mod 1/8). This is observation (i) of the brief: the SO(3) reducible on νS with v = ξ has energy 4a² = 1/16 at a = 1/8.
- (c) At L_2^w ∩ L_{−2}^w = (1/4, 0), ΔCS = 1/4 again. The binary dihedral representations live here, and there are none when det K = 1.

## 3. c is a ρ-invariant

**Theorem 3.1 (VERIFIED).** Let Y be a rational homology sphere whose reducible flat SU(2) connections are central, so h⁰ = 3 and h¹ = 0, and let α be nondegenerate and irreducible. In DLME's conventions,

  c(α) = CS~(α) − i(α)/8 = (3 + ρ_ad(α))/16,

where ρ_ad = η_{ad α} − 3η is the APS ρ-invariant of the odd signature operator on even forms.

*Proof.*
1. BHKK equation (`rhoadAPS`), with their (−ε, −ε) convention, gives SF_{su(2)}(θ → α; Y) = 8 cs(α) + ρ_ad(α)/2 − 3/2.
2. Section 1.4 gives i_DLME(α; Y) = SF(θ → α; −Y) and CS_DLME(α; Y) = cs(α; −Y). The real lifts correspond along the same path.
3. Substituting, and using ρ(−Y) = −ρ(Y), gives the formula. ∎

Checks:
- Σ(2,3,5): ρ_ad = −73/15 and −97/15 give c = −7/60 and −13/60, which are DLME's values. BHKK independently list ρ = 73/15 on −Σ(2,3,5).
- The finite-group formula ρ_E(S³/G) = (1/|G|) Σ_{g≠1} (tr E(g) − dim E) cot²(θ_g/2), with the link orientation, reproduces −73/15 and −97/15 for I* (`sph.py`).

**Corollary 3.2 (VERIFIED).**
- (a) c(−Y, α) = 3/8 − c(Y, α). The derivation is direct: i_{−Y} = −3 − i_Y and CS_{−Y} = −CS_Y. For a perfect complex, ℓ(−Y) = 3/8 − max_α c(Y, α).
- (b) For any W: ∅ → Y with b_1(W) = 0 and any connection A on any U(2) bundle, asymptotic to α,
  c(α) = 3(1 + b⁺(W))/8 + (ind A − 8E(A))/8.
  This follows from DLME's index additivity, ind(W; ∅ → α) = −2c₁² − 3(1 + b⁺) − i(α), and E = −c₁²/4 − CS~(α).

**Remark 3.3 (where 1/16 can and cannot appear; VERIFIED).**
- For every cobordism or family map of the kind used by DLME, with b_1 = 0 and fixed-limit index (codim − dim), L − D/8 = −η + (codim − dim)/8 + 3b⁺/8. This lies in (1/8)ℤ − η whatever the bundle, because the c² terms cancel. Two examples: DLME's g_1 has L − D/8 = 1/4 − 3/8 = −1/8, and the μ(S)-cut map B has +1/8.
- The c-values themselves are (3 + ρ)/16. So ℓ(Y_2) − ℓ(Y_{−2}) = (ρ_*(Y_2) − ρ_*(Y_{−2}))/16. A gap of 1/16 is a gap of 1 in adjoint ρ-invariants, and no index formula needs to "contain" 1/16 for it to appear.

## 4. Seifert fibred surgeries and torus knots

**Theorem 4.1 (FS formula for Seifert rational homology spheres; VERIFIED numerically, proof sketch PLAUSIBLE).** Let Y = M((a_1,b_1), (a_2,b_2), (a_3,b_3)), with π_1 = ⟨x_i, h | x_i^{a_i} h^{b_i} = 1, x_1x_2x_3 = 1⟩ and e = −Σ b_i/a_i ≠ 0. Let α be irreducible with ρ(x_i) ~ e^{πi l_i/a_i}, and set
s(l; a, b) = (2/a) Σ_{k=1}^{a−1} cot(πk/a) cot(πbk/a) sin²(πlk/a).
Then

  c(α) = (3 + 3 sgn e − 2 Σ_i s(l_i; a_i, b_i))/16,  CS_DLME(α) ≡ Σ_i b_i⁻¹ l_i²/(4a_i) (mod 1/4).

*Proof sketch.* ad α extends flatly over the orbifold mapping cylinder W. Kawasaki–APS gives ρ_ad = 3·sign(W) − sign_{ad}(W) + (cone terms). We have sign(W) = sgn e. Also sign_{ad}(W) = 0, because rigid triangle representations have H*(B; ad α) = 0. The cone terms are −2s(l_i; a_i, b_i).

Checks:
- FS Brieskorn formula for Y_{±1}(T_{p,q}) = ±Σ(p, q, pq ± 1), 16 cases (`check1.py`).
- S³/O* = −Y_2(T_{2,3}) and S³/T* = −Y_3(T_{2,3}) by group sums (`sph.py`). These are QHS checks with e > 0.
- c ≡ CS (mod 1/8) in every case, and wrong local data fails this test (`teeth.py`).
- Two independent enumerations agree: pillowcase arcs ∩ L_N, and triangle-group rotation numbers (`check2.py`).

**Theorem 4.2 (torus knots; VERIFIED from 4.1 with exact arithmetic).** For T = T_{p,q} and a generator x on the arc (k, l), with N < pq and N ≠ 0, untwisted or twisted (twisted taken in the (3+ρ)/16 normalisation):

  c(Y_N(T), x) = κ_{k,l} + (pq − N + 3 sgn N)/16 − (pq − N)(α − 1/4)².

Here κ_{k,l} = (1 − 2s(k; p, q) − 2s(l; q, p))/16. The proof uses the closed form s(l_3; m, −1) = 1 − 2l_3(m − l_3)/m with l_3 = 2αm. For N > pq, an extra −1/8 appears (`bigN.py`), which is the Maslov indicator of §5. Example: the trefoil has c = 5/48 + (6 − N + 3 sgn N)/16 − (6 − N)(α − 1/4)².

**Table 4.3 (VERIFIED).** All complexes are perfect: Y_2 is concentrated in even degrees and Y_{−2} in odd degrees. The DLME inequalities ℓ(Y_{−1}) < ℓ(Y_{−2}), ℓ(Y_2) < ℓ(Y_1) and ℓ(Y_{−1}) < ℓ(Y_1) − 1/8 all hold (`dlmecheck.py`).

| K | ℓ(Y_2) | ℓ(Y_{−2}) | ℓ(Y_2) − ℓ(Y_{−2}) | the same for K̄ |
|---|---|---|---|---|
| T(2,3) | 23/48 | 37/96 | 3/32 | 3/32 |
| T(2,5) | 79/160 | 37/80 | **1/32** | 11/96 |
| T(2,7) | 167/336 | 225/448 | **−1/192** | 23/192 |
| T(2,9) | 287/576 | 379/720 | **−9/320** | 39/320 |
| T(3,4) | 119/240 | 163/336 | **3/280** | 33/280 |
| T(3,5) | 97/195 | 1039/2040 | **−21/1768** | 219/1768 |
| T(4,5) | 359/720 | 471/880 | **−29/792** | 1/8 |
| T(4,7) | 727/1456 | 313/560 | **−31/520** | 193/1560 |
| T(5,6) | 839/1680 | 1081/1920 | −57/896 | 111/896 |
| 4_1 (amphichiral) | 19/80 | 11/80 | 1/10 | — |

Further observations:
- ℓ(Y_2(T_{2,q})) = 1/2 − 1/(8q(q−1)) for q = 3, …, 39.
- For T_{2,q}, the difference ℓ(Y_2) − ℓ(Y_{−2}) decreases through 0 between q = 5 and q = 7, passes −1/16 at q ≈ 15, and reaches −0.106 at q = 51 (`asym.py`).
- For 4_1, the identifications S³_{+2}(4_1) = M((2,−1),(4,−1),(5,4)) with e = −1/20, and its reverse for −2, are fixed twice: by the grading parity (Casson–Walker sign) and by the single CS constant of §2.

**Conclusion 4.4.**
- The statement "|ℓ(Y_2) − ℓ(Y_{−2})| ≥ 1/16" is false for positive torus knots T(2,q) with q ≥ 5 and for T(3,4), T(3,5), T(3,7), T(4,5), T(4,7). These are VERIFIED, conditional only on Theorem 4.1, which has been tested in all the independent ways listed.
- A global orientation flip exchanges the two chiralities, so one family fails under either convention.
- Any proof of a 1/16 gap must therefore use a hypothesis that positive torus knots violate. For torus knots Y_2 and Y_{−2} have opposite grading parity, so they are never cosmetic candidates. The obvious candidate hypotheses are (i) balanced gradings, or (ii) the absence of arcs of irreducibles ending on the reducible arc, which holds when Δ_K has no roots on the unit circle, in particular when Δ_K = 1.

## 5. The pillowcase formula for c

**Conjecture 5.1.** Status: VERIFIED for torus knots, for all slopes and both bundles, and for 4_1 at N = ±1, ±2, ±3. PLAUSIBLE in general.

Let Γ be a component of the irreducible character variety, γ a path in Γ from a base point, and (α, β) the lift. Write δ = α − 1/4. Then:

  c(Y_N, x) = Φ_Γ(x) + (3 sgn N − N)/16 + N δ(x)² − ι_N(x)/8,  with Φ_Γ(x) = j_Γ + 2∫_γ δ dβ.

Here:
- j_Γ is constant on Γ, apart from slope-independent jumps where SF_X jumps. None were observed.
- ι_N(x) = 1 exactly when the slope −N lies strictly between ∞ and the tangent slope of C at x, on the side away from 0. It vanishes on every branch steeper than L_N. For torus knots, ι_N = [N > pq].

Equivalent forms:
- CS(Y_N, x) ≡ κ_Γ + 2∫α dβ + Nα² (mod 1).
- **i(Y_N, x) ≡ 4(Nα + β) − (3/2) sgn N + ι_N(x) + i_Γ (mod 8)**: four times the integer meridian holonomy of the filling, read off the lifted path. This is the su(2) analogue of BHKK's ℂ² formula SF = 2(a − b) − 2 + SF_Z with a = m_1. The factor doubles because the adjoint has weight 2.
- Differential form: along C, dc_N = 2(α − 1/4) d(Nα + β).

Evidence:
- Torus knots: Φ − (pq/16 − pq δ²) is a single constant per arc for all slopes N ∈ [−7, 7] with N ≠ 0 and N < pq, untwisted and twisted (`twisted.py`).
- Figure-eight: the irreducible SU(2) curve is a closed figure-eight in the pillowcase with α ∈ [1/6, 1/3], a double point at (1/4, 0), and monodromy (0, 2). We have ∮2α dβ = 1, so Φ is single valued. On all 12 generators of S³_N(4_1), N ∈ {±1, ±2, ±3}, matched by CS mod 1/4,
  Φ − 2∫_{(1/6,−1/2)} δ dβ = 3/16
  to 4 decimals (`fig8_match.py`).
- Heuristic proof (PLAUSIBLE): BHKK's splitting writes SF on Y_N as SF_X(γ; P⁻), which is independent of N, plus boundary terms that are homotopy invariants of the boundary path (the integers a, b, c). The su(2) version gives 4m − (3/2) sgn N from these terms. The sign term is 3b⁺(X_N)/8 in Corollary 3.2(b). The Maslov indicator records the passage of Λ_X = TC through Λ_{V_N} = TL_N.

## 6. Y_2 against Y_{−2}

**6.1 Pointwise (from 5.1).** On branches steeper than slope ±2,

  c(Y_{±2}, x) = Φ(x) ± (1/16 + 2δ²).

At the same point the gap is 1/8 + 4δ² ≥ 1/8, with equality exactly on the traceless line. On branches with |slope| < 2 the indicators give a gap of 4δ² or 1/4 + 4δ². The parity analysis confirms that Δc ∈ {0, 1/4} there.

**6.2 Why the number is 1/16.** The slope term at a traceless point is (3 sgn N − N)/16.
- The **3/16** is half the jump 3/8 of 3(1 + b⁺(X_N))/8 between positive and negative surgery. Its 3 is h⁰(θ) = dim SU(2), from −3(1 + b⁺) in the index formula.
- The **N/16 = N·(1/4)²** is the solid-torus Chern–Simons term Nα² at the traceless holonomy. This is the precise role of "a² = 1/16".
- At |N| = 2 these combine to (3 − 2)/16 = 1/16. At |N| = 1 they give 1/8, DLME's ±1 constant (SPECULATIVE that this is more than numerology).

**6.3 Traceless triple points.**
- ΔCS = 1/4 and Δi is an integer, so c(Y_2, x₀) − c(Y_{−2}, x₀) ∈ (1/8)ℤ (VERIFIED).
- It equals 1/8 for torus knots, at the traceless generators of T(3,4), where ΔCS = 1/4 and Δi = 1 (VERIFIED). By 5.1 it equals 1/8 whenever C is steeper than ±2 at x₀ (PLAUSIBLE).
- My first attempt to prove universality by excision fails. The two pieces differ along a whole end, so the excision is not between operators that agree outside a compact set.

**6.4 From pointwise offsets to ℓ.** For perfect complexes,

  ℓ(Y_2) − ℓ(Y_{−2}) = 1/8 + min_{L_2}(Φ + 2δ²) − min_{L_{−2}}(Φ − 2δ²).

The gap therefore depends on how much Φ varies between the two sets of generators.
- **Local mechanism (VERIFIED, given 5.1 on that branch; for mirrors of torus knots 5.1 is Theorem 4.2).** Suppose both minimisers lie on one straight branch of slope s > 2 through a traceless point. Then Φ = Φ₀ + sδ², generators of Y_{±2} are spaced 1/(s ± 2) in α, and
  1/8 − 1/(4(s − 2)) ≤ ℓ(Y_2) − ℓ(Y_{−2}) ≤ 1/8 + 1/(4(s + 2)).
  For s ≥ 6 this gives at least 1/16. The mirror trefoil, with s = 6, is the extremal case: the bound is exactly 1/16 and the true value is 3/32.
- For positive torus knots, s = −pq < −2, so the minimisers sit near the bifurcation points, far from the traceless line, and the gap is uncontrolled. This is what produces the counterexamples.

**6.5 Conjecture (SPECULATIVE, about 20%).** If no arc of irreducibles ends on the reducible arc (for instance if Δ_K has no roots on the unit circle, in particular if Δ_K = 1), then ℓ(Y_2) − ℓ(Y_{−2}) ≥ 1/16. Evidence: 4_1 gives 1/10, and the mechanism of 6.4. Against it: a single example; and Δ = 1 knots need generators of both parities, hence several components or branches with |slope| < 2, where 6.1 allows a pointwise gap of 0.

## 7. Where the traceless representations enter

1. R(K, i) = C ∩ {α = 1/4}. Since dc_N = 2δ dm_N and dΦ = 2δ dβ, these points are critical for every c_N and for Φ (VERIFIED from 5.1). They are the levels about which Y_2 and Y_{−2} are placed symmetrically, at ±1/16.
2. The points of R(K, i) with λ ↦ −1 are exactly the generators that Y_2, Y_{−2} and Y_0^w have in common (VERIFIED). There Δc = 1/8 (6.3).
3. The points with λ ↦ +1 are the generators common to the twisted Y^w_{±2}, together with the twisted reducible at (1/4, 0). The binary dihedral representations lie here, and there are none when det K = 1 (VERIFIED).
4. In the orbifold, or odd-bundle, version of the family on W′, splitting along J = S³ produces singular flat connections on (S³, K) with traceless meridional holonomy, which is all of R(K, i). For nontrivial K it contains irreducibles (Kronheimer–Mrowka). In the pillowcase these points sit at the level Φ, halfway between the c-levels of Y_2 (+1/16) and Y_{−2} (−1/16). So a broken trajectory Y_2 → (S³, K)^♮ → Y_{−2} uses two half-steps of 1/16, and the face does not cancel. This is the pillowcase picture of why that map fails (SPECULATIVE).

## 8. Proposed structural explanation, statements, status, confidence

**Explanation.**
- The factor 1/16 is the APS coefficient (Theorem 3.1).
- In the pillowcase it appears as the slope term (3 sgn N − N)/16 at N = ±2. Every Y_{±2} flat connection lies at Φ ± (1/16 + 2δ²), so at a traceless point the two levels differ by 2·(1/16).
- The 1/16 is 3/16 (b⁺ of the trace) minus 2·(1/4)² (solid torus at the traceless holonomy).

**Statements and status.**
- **(A)** Theorem 2.1 and Corollary 2.2: VERIFIED, about 98%.
- **(B)** Theorem 3.1 and Corollary 3.2: VERIFIED, about 97%.
- **(C)** Theorem 4.1 and Theorem 4.2: VERIFIED numerically by independent methods; proof sketch PLAUSIBLE; about 92%.
- **(D)** Conjecture 5.1: verified for torus knots and 4_1; general case about 70%, with the form of ι_N about 55%.
- **(E)** The user's bound |ℓ(Y_2) − ℓ(Y_{−2})| ≥ 1/16 is **false in general** under DLME's normalisation (T(2,7): −1/192), given (C). Confidence 90%. The residual doubt is whether the user's ℓ for Y_{±2} uses a different normalisation.
- **(F)** The local mechanism of 6.4 is VERIFIED as stated. Conjecture 6.5 (Δ_K = 1 ⇒ gap ≥ 1/16) is SPECULATIVE, about 20%.

**Overall.** I have no theorem forcing the gap. I have a structural account of why 1/16 is the natural size of the offset, and evidence that the gap is not forced without further hypotheses. Confidence in this account: about 75%.

## Appendix: scripts

All scripts are in `pillowcase-code/`.
- `seifert.py`: pillowcase enumeration and the c-formula.
- `sfs.py`: triangle-group enumeration.
- `check1.py`, `check2.py`: FS and enumeration cross-checks.
- `sph.py`: S³/G group sums.
- `csq.py`: CS mod 1/4.
- `teeth.py`: negative controls.
- `pm2.py`, `detail.py`, `tables.py`, `asym.py`, `mirror.py`, `dlmecheck.py`: ℓ tables.
- `twisted.py`, `bigN.py`: slope decomposition.
- `fig8_*.py`: figure-eight curve, generator matching and Φ.
