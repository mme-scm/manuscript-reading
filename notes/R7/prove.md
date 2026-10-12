# prove.md: mixed maps of level exactly −1/16 that carry flat connections

Labels: PROVED (complete from the stated inputs, bookkeeping included), PLAUSIBLE (one named gap), SPECULATIVE.
Notation as in BRIEF: A_i = C(Y_2,P_i), B_i = C(Y_{-2},P_i), T traceless, W′, S, X′ = W′∖νS, Q = mixed point (1/8,1/4) or (3/8,3/4), bd = (1/4,0).
The scope was narrowed by the coordinator to the enumeration (§1–§2). §3–§4 keep the earlier items short.

---

## 0. Verdict

1. **Every mixed map of level −1/16 that I can build near S is the exterior map E_{γ1}, and it is null-homotopic.** This covers X′ and its recappings, the orbifold cone C²/Z₄, the rational ball, singular holonomy along S, and the τ-quotient of DLME's ±1 cobordism. (PLAUSIBLE: gluing at γ1.)
2. **Same-point rigidity (PROVED, bookkeeping).** Each of these cobordisms has π₁ (or orbifold π₁) of its flat part equal to π₁(X′). So a flat connection restricts to the *same* knot representation x on both ends. Its level shift is then fixed by the ends: −g(x), where g(x) = c(Y_2,x) − c(Y_{−2},x) is 1/8 at same-bundle points and 3/16 at mixed points (all 1732 torus-knot common points). That is never −1/16.
   - A rigid −1/16 map can therefore carry a flat connection only at a mixed point where the X′-index is 0 instead of −1.
   - I argue (SPECULATIVE) that this index is a Maslov triple index of the slopes (2, −2, s_Γ(x)). It is −1 when |s_Γ| > 2, which covers every torus knot.
3. **The equality cases are not carried by any such flat connection (PROVED from the data).** In both T(2,−3) and 4₁ the pair realising m₂ = 1/16 joins *different* points of Γ_K: bd on Y_2^w, and Q (T(2,−3)) or a non-common point z (4₁) on Y_{−2}^0. Also, bd does not lie on L_{−2}^0, so the flat connection at bd is P₁→P₁, with gap exactly 1/8.
   - What does realise equality is the composite b′∘a′ = ∂g′_A: a′ is flat (energy 0) at bd, and b′ has energy exactly 1/16.
   - For T(2,−3) that energy is the area of the pillowcase triangle (bd, (1/4,1/2), Q), which is 1/16 = E_cap.
   - So equality sits on the J-face of the family, not on a −1/16 cobordism.
4. **A new family of triangles (SPECULATIVE; §2.5).** Make W′ singular along S with holonomy α₀, and replace T by C^{α₀}(K). The middle term vanishes for Δ_K = 1 once α₀ < min α(Γ_K), so g^ns + g^{α₀} would be a chain map that is injective, with no third term. The obstruction is that the level is topological only at α₀ = 1/4 (monotonicity); otherwise it is not bounded by −1/8.
   - A naive version contradicts the data: it would give m ≥ 1/8, but T̄(3,5) has m₁ = 0.085. So non-monotonicity is essential, not technical.
   - This is the precise form of "the middle term can vanish, but only where levels are not topological".
5. **(D) and Conjecture R.**
   - (D) is equivalent to the conclusion witnessed by g_A on the first kernel class. It is an energy lower bound whenever δ > 1/16 (§3).
   - Conjecture R is refuted by the vertex relation itself (§3). This agrees with the withdrawal note now in strategy16.tex.

---

## 1. Same-point rigidity (the arithmetic behind §0.2)

**Lemma 1 (PROVED, bookkeeping).** Let Z: Y_2 → Y_{−2} be W′ modified inside a neighbourhood of S. That is, Z = X′ ∪_{L(4,1)} N for a cap N: a smooth cap, a singular cap, an orbifold cap, or a rational ball. Suppose π₁(N∖sing) ← π₁(L(4,1)) is onto. Then:
- every flat connection on Z restricts on Y_2 and Y_{−2} to the same representation x of π₁(E_K) with ρ(μ)⁴ = ±1 and ρ(λ) = ρ(μ)^{±2};
- its level shift is c(out) − c(in) = −g(x), whatever N is.

*Proof.* Van Kampen gives π₁^{(orb)}(Z∖sing) = π₁(X′) = π₁(E_K)/⟨⟨μ²λ, μ^{−2}λ⟩⟩. The shift equals (ρ(Y_{−2},x) − ρ(Y_2,x))/16, which depends only on the ends. ∎

**Corollary.** A map of Z counted at index i has topological level L_Z(i). A flat connection at x is counted there only if L_Z(i) = −g(x).
- Torus knots give g = 1/8 (γ0 end) and g = 3/16 (γ1 end) at every common point (strategy-exact §7.1; 1036 + 696 points).
- So a level −1/16 count never contains a flat connection. Flat mixed connections live in the index-(i − 1) count, which is the one-parameter family at level −3/16.

**When g(x) = 1/16 is possible (SPECULATIVE).**
- On X′, g(x) = 1/16 − i_{X′}(x)/8.
- By Mayer–Vietoris, the twisted H² of X′ at x is 1-dimensional (H¹(E_K; ad) = 1, and H*(Y_{±2}; ad) = 0). So i_{X′}(x) ∈ {−1, 0}, according to the sign of its square.
- By the analogue of triangle-1 §3.2, that sign is the Maslov triple index of (L_2, L_{−2}^w, T_xΓ_K). It is −1 when |s_Γ(x)| > 2 (torus knots: s = −pq).
- At a transverse mixed point with |s_Γ| < 2, i_{X′} would be 0 and g = 1/16. Then E_{γ1} would carry that flat connection at zero energy. The Thom principle does not exclude this.
- It changes nothing, because E_{γ1} ≃ 0 (§2.1).

---

## 2. The enumeration (target: mixed, level exactly −1/16, flat connection)

Arithmetic options (BRIEF): (i₀, b⁺, Σt) = (0, 0, 1/16), (+1, 0, 3/16), (−2, 1, 3/16), (−1, 1, 5/16).

| # | cobordism / family | level | chain map | injective | flat connections |
|---|---|---|---|---|---|
| 1 | E_{γ1}: X′ rigid, γ1 on −∂νS | −1/16 exact | PLAUSIBLE | **no**: E_{γ1} = ∂g^ns, the J-face is empty | mixed points with i_{X′} = 0 only; none for torus knots |
| 1′ | E_{γ1′} = ιE_{γ1}ι (χ-twist) | −1/16 | as 1 | no | as 1 |
| 2a | X′ ∪ νS, odd, nonsingular (= W′ odd, rigid) | 0 | yes | ≃ E_{γ1} ≃ 0 after stretching | none (π₁ = 1, w₂ ≠ 0) |
| 2b | X′ ∪ (νS, S) SO(3)-singular, adjoint holonomy π (cap 1/16, index −1) | 0 | no: ∂ = ba + E | – | flat needs λ ↦ −1 and +1 at once: none |
| 2c | X′ ∪ (νS, S) singular at holonomy 1/4, flat cap, γ0 | 0 | g_S, R_0 | – | **same bundle** only |
| 2d | rational ball B_2 | – | – | – | **no mixed bundle** (Ext(Z/2,Z/2) → Ext(Z/4,Z/2) is 0); W″ ≃ 0 |
| 2e | **orbifold cone** W′_orb = X′ ∪ c(L(4,1)), C²/Z₄, odd | **−1/16 exact** (below) | PLAUSIBLE | **no**: ≃ E_{γ1} ≃ 0 | all X′ flats extend; at mixed points the index is −1, so they sit in the family (level −3/16) |
| 2f | (W′, S) singular, adjoint holonomy π/2 (SU(2) parameter 1/8) | rigid −1/16; family −3/16 in the flat sector | rigid ≃ E_{γ1} | no | all mixed flats extend (π₁(νS∖S) = Z/4); gap 3/16 |
| 3 | τ-quotient of DLME W^1_{−1} (cone angle π on S) | g_A: −1/8; its RP³-face descends to E_{γ1} at −1/16 | g_A is not a chain map (∂ = ba) | – | g_A: none (η_g > 0); face: as 1 |
| 4 | (−2, 1): g_A c g_A and the Toda-type composites (Φ∘a, b g_B g_A, g_A g_M a) | −1/16 | Φ∘a only; the others are not | Φa ≃ b(g_B g_A + a h_A + h_M a) factors through b; zero in Models 1–2 | none (W′ simply connected; the singular parts need λ ↦ ∓1 together) |
| 5 | (+1, 0): exterior of a +4-sphere, γ1 on +∂νS, codimension-one cut | −1/16 | – | – | none found: the examples (W′ # CP², conic) have π₁ of the ends killed |

### 2.1 Why 1, 2a, 2e and 2f all collapse to E_{γ1} ≃ 0 (PLAUSIBLE)
- **Stretch along L(4,1).**
  - An index-0 configuration is (exterior, index i_ext) # (cap, index i_cap) with i_ext + i_cap + 1 = 0.
  - Each cap in 2a, 2e and 2f has a unique index −1 piece with γ1 boundary: energy 1/16 in 2a, flat in 2e and 2f. The next pieces have index ≥ 3 in 2a; for 2e and 2f, PLAUSIBLE.
  - So the chain-level map is E_{γ1} × 1 in every case.
- **E_{γ1} = d g^ns + g^ns d** (strategy-exact Prop. 4.1). The S³-face of g^ns is empty because h⁰(θ) = 3.
- **In DLME's language:** the −1/16 map is the descent of DLME's RP³-face. Upstairs it is homotopic to the composite through C(Σ). Downstairs its trivial-isotropy part runs through C(S³) = 0. The vanishing third term *kills* this map instead of inverting it, the opposite of g_1 at ±1.

### 2.2 Orbifold index (2e), PLAUSIBLE
- The cone c(L(4,1)) = B⁴/Z₄, with the scalar action, so the link is ∂(O(−4)). Its orbifold index is the Z₄-invariant part of the ball's index.
  - On the ball, the trivial connection has index −3 (it is −H⁰).
  - The invariant part of ad under rotation by π/2 is 1-dimensional, so i(cone, γ1) = −1.
  - Under rotation by π it is also 1-dimensional, so i(cone, γ0) = −1.
- From (1.2): c_γ = 3/8 + (i − s_orb)/8.
  - γ1 (3/16) gives s_orb = 1/2, so the odd orbifold map has rigid level −1/16.
  - γ0 (1/4) gives s_orb = 0, so the even orbifold map has level 0.
- So **E_{γ1} is the rigid map of the orbifold blow-down of S**. It is a natural home for the −1/16, but it is the same map.

### 2.3 The equality cases (user's check), PROVED from the data
- **bd = (1/4,0)** lies on L_2^w and L_{−2}^w, but not on L_{−2}^0 (−2·¼ + 0 ∉ Z). So no P₀ generator of Y_{−2} sits at bd.
  - The X′ flat connection at bd is P₁→P₁ with γ0 end and gap 1/8.
  - Checks: T(2,−3): −1/24 → −1/6. 4₁: 1/5 → 3/40 and 3/10 → 7/40.
- **The 1/16 pairs in the data:**
  - T(2,−3): bd on Y_2^w (−1/24) → Q on Y_{−2}^0 (−5/48).
  - 4₁: bd on Y_2^w (1/5) → z on Y_{−2}^0 (11/80). Here z ∉ L_2^w, because Γ ∩ L_2^w is the two bd points (rk = 2 = (det − 1)/2).
  - In both, the pair joins different representations. By Lemma 1, no cobordism of the list carries it at zero energy.
- **What carries it:** b′∘a′. a′ is flat at bd (energy 0, c^tl = c(Y_2^w, bd)), and b′ goes from the traceless bd point to the minimiser of Y_{−2}^0 with energy exactly 1/16.
  - For T(2,−3) this b′ is the straight triangle (Q, (1/4,1/2), (1/4,1)). Its area is ½ · ½ · ⅛ · 2 = 1/16. The Γ-edge (slope 6) and the L_2^w-edge (slope −2) give equal areas, because only the apex α = 1/8 and the base on V matter.
  - b′a′ = ∂g′_A. So equality lives on the J-face of the traceless family, not on a −1/16 cobordism.
  - Equivalent bookkeeping: m₂ = D^w − ε_{−2} = 1/8 (flat at bd) − 1/16. Here ε_{−2} = λ₀(Y_{−2}) − λ₁(Y_{−2}) = 1/16 in both cases (T̄(2,3): −5/48 + 1/6; 4₁: 11/80 − 6/80). For other knots it is not 1/16 (T̄(3,5): −0.039).
- **Both-bundle check.** Same-bundle flat connections give exactly 1/8, attained by the 78 mirrors with det > 1. A level −1/16 both-bundle map with a flat connection would need g = 1/16 at a same-bundle point. Those points have a γ0 end, so g ∈ 1/8 + Z/8, and this is impossible (PROVED). So any both-bundle bound at −1/16 is automatically strict, consistent with the user's expectation, but empty of content.

### 2.4 Summary of the enumeration
- The only mixed rigid −1/16 map carrying the γ1-term is E_{γ1}, in several disguises: X′, the orbifold cone, and singular holonomy π/2 along S.
- It supports exactly the X′ flat connections, which realise the exact gap 3/16, or 1/16 if i_{X′} = 0.
- It is null-homotopic, because the S³-face of g^ns is empty.
- No candidate is injective.

### 2.5 A new family of triangles, and its obstruction (SPECULATIVE)
- **Triangle(α₀)**, for α₀ ∈ (0, 1/2):
  $$A_0 \xrightarrow{a_{α₀}} C^{α₀}(S^3,K) \xrightarrow{b_{α₀}} B_1 \xrightarrow{c} A_0 .$$
  - a and b are singular 2-handle maps with holonomy α₀ on D_l and D_r.
  - c is −X′ with γ1, as before.
  - The family is G_{α₀} = g^ns + g^{α₀} on (W′, S, α₀).
- **Faces.**
  - J-face of g^ns: empty.
  - J-face of g^{α₀}: b_{α₀}a_{α₀}.
  - L(4,1)-faces: E_{γ1} × (the unique index −1 cap) in both, so they cancel. This is the same mechanism as triangle-1 §4.2.
  - Hence ∂G_{α₀} = b_{α₀}a_{α₀}.
- **Vanishing third term.** If Δ_K = 1, the irreducible locus Γ_K is compact and misses the reducible arc. So R*(K; α₀) = ∅ for α₀ < α_min(K): C^{α₀} = 0 at chain level, G_{α₀} is a chain map, and triangle detection makes it a quasi-isomorphism. This is the exact analogue of C(S³)² = 0 at ±1. Pillowcase: V_{α₀} → V_ε, the DLME middle line.
- **Obstruction (PROVED as bookkeeping).** For α₀ ≠ 1/4 the singular term
  $$s(l) = 4l(1 - 4α_0) + χ(S) + 8α_0^2\,S\cdot S$$
  depends on the monopole number l.
  - At fixed ends and index, c-shift = top(l) − E(l), and top(l) increases by (1 − 4α₀)/2 for each decrease of l.
  - Positivity of energy bounds each sector separately, but the sectors are unbounded. So the level of G_{α₀} is not topological. Bounding it by −1/8 requires an energy lower bound in the low sectors, which the rules forbid.
  - Only α₀ = 1/4 is monotone, and there the middle term is T ≠ 0. (H(T) ≠ 0 for nontrivial K: if C̃ were acyclic, I^♮ would have rank 1, contradicting KM; PLAUSIBLE via the Daemi–Scaduto structure.)
- **Sanity check.**
  - A topological level −1/8 for G_{α₀} would give m₁, m₂ ≥ 1/8 for Δ = 1.
  - It would also give rk A_0 = rk B_1 for every Δ = 1 knot.
  - There are no Δ = 1 data to test this. For det-1 *torus* knots C^{α₀} ≠ 0 (Γ meets the reducible arc at roots of Δ), so they do not test it either. The ±2 rank identity is not contradicted.
- **Key lemma that would be needed:** a monotone singular theory along S whose middle term vanishes for Δ_K = 1. I see no candidate. The orbifold Z₄ structure along S (holonomy π/2) is also non-monotone.

---

## 3. (D) and Conjecture R (short)

- **(D) δ ≤ 1/16 + η_g is equivalent to the conclusion at a witness (PROVED).**
  - The vertex lemma gives c(g_A x_κ) = κ − 1/8 − η(x_κ), where x_κ is the lowest cycle of ker a and η(x_κ) is the energy realising the top output level.
  - So (D) ⟺ c(g_A x_κ) ≤ λ₀ − 1/16, which is "m₁ ≥ 1/16, witnessed by g_A x_κ".
  - Its energy-free part, δ ≤ 1/16, fails for T̄(2,3) (1/8) and 4₁ (1/10), and possibly for T̄(3,5) in (I) (δ ∈ [1/20, 27/340] ∋ 0.079). Wherever δ > 1/16, (D) is the energy lower bound η ≥ δ − 1/16.
  - (D) also drops the β(T) term of Theorem 5.1; Model 3 refutes the undecorated form.
- **Conjecture R is false whenever the bottom is absorbed (PROVED).**
  - The pentagon relation id + c g_A + g_M a = ∂h (+∂k) gives [x] = [c g_A x + g_M a x] for every cycle x. So the "return" ξ = [w] holds identically.
  - The chain-level reformulation ("g_M carries τ to ξ") is not invariant: g_M a x alone is not a cycle.

---

## 4. Bottom line
- **What is PROVED.** No cobordism obtained by modifying W′ near S (smooth, singular, orbifold, rational ball, or the τ-quotient) gives a non-null-homotopic mixed −1/16 map.
  - Such a map's flat connections are same-point connections, with shifts −1/8 or −3/16; −1/16 is possible only if i_{X′} = 0.
  - The equality pairs join different points, so these maps cannot carry them.
- **What a successful map would need.** It must change the knot representation between its two ends, as b′∘a′ does through the bd point. That forces it through a middle theory (T, or some C^{α₀}). So the −1/16 cannot come from a cobordism alone; it has to come from a triangle's J-face.
- **The cleanest new candidate** is Triangle(α₀) with C^{α₀} = 0 for Δ = 1. It is blocked exactly by non-monotonicity at α₀ ≠ 1/4.
