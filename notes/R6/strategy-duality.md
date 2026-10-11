# Combining the triangles of K and of its mirror: what duality, the cosmetic identification, gradings, χ and Euler characteristics give for the ±2 drop

Labels: **PROVED** (a complete argument from the stated inputs, or exact finite verification), **COMPUTED** (exact computation on the torus-knot and figure-eight data), **PLAUSIBLE** (an argument with a named gap), **SPECULATIVE**.

Code: `scratchpad/r6/duality-code/`. The scripts are `tests_data.py`, `counting.py`, `model.py` and `fig8_ctl.py`, and their outputs are in the matching `*.out` files. They reuse read-only the calibrated torus-knot machinery of `gap16/triangle-code/tk.py`.

---

## 0. Verdict

1. **The angle cannot produce a contradiction or a drop by itself.**
   - The triangles for the mirror K̄ are exactly the duals of the triangles for K (§4.1). So "using K̄" is the same as running the same triangles at the top of the spectrum.
   - Gradings mod 8, the χ-involution, balanced gradings, Euler characteristics and the Casson–Lin count give identities. For Δ_K = 1 all of these identities are satisfied automatically (§4.2).
   - I give explicit filtered complexes (§4.6, `model.py`) that satisfy every input of the strategy together with a cosmetic identification. Each model has m₁ = m₂ = 0 and both-bundle drops 0 at both ends. Every model has nonzero traceless homology, and two of the four have a nonzero differential. **No argument that uses only these inputs and positivity of energy can prove "drop > 0".** (PROVED: exact verification over F₂.)
2. **What the angle does give is a sharp set of necessary conditions** for a vanishing both-bundle drop, valid for any knot (§4.4–4.5). In the perfect case they are:
   - (i) the bottom class is absorbed by the traceless theory;
   - (ii) every traceless class below the bottom lies in the image of the singular maps;
   - (iii) a counting condition: the classes of I(Y₂) (resp. I^w(Y₂)) within 1/8 of the bottom inject into T(K) through a (resp. a′), so their number is at most rank a (resp. rank a′). Under a cosmetic pair, rank a = rank a′ = ½ dim T(K);
   - (iv) a matching condition: the k-th such class lies within (η, 1/16] above the k-th class of im a;
   - the dual conditions at the top.

   **These conditions fail for every knot in the data**, at both ends: 58 torus-knot cases with or without using parity, and 4₁ (COMPUTED, `counting.py`). So the soft structure explains every positive drop in the data. It cannot exclude them in general.
3. **Closing the argument needs exactly what RULES (a) forbids.** It needs one of:
   - a lower bound on the energy of absorption by a, a′;
   - a bound on the boundary depth of C^tl(K), which is again an energy statement;
   - a non-energy statement about where the spectrum of T(K) lies relative to that of I(Y₂). No such statement is available.

   By RULES (e), I stop there.

---

## 1. Setting and notation

**Manifolds and bundles.**
- K ⊂ S³ is a knot, Y_r = S³_r(K), and K̄ is the mirror of K, so Y_r(K̄) = −Y_{−r}(K).
- On Y_{±2} the bundles are P₀ (w₂ = 0) and P₁ (w₂ ≠ 0).

**Complexes (F₂ coefficients).**
- A_± = C(Y_{±2}, P₀), Z/8-graded.
- B_± = C(Y_{±2}, P₁), Z/8-graded (ζ-normalised).
- T = C^tl(K), the irreducible traceless complex of (S³, K), Z/4-graded.
- Their dimensions in homology are α_±, β_±, τ.

**Levels.**
- Every generator carries its level c = (3 + ρ)/16, for both bundles (BRIEF). For T the level is the Seifert-framed c^tl of triangle-1 §1.3.
- Differentials strictly lower the level, since instantons on ℝ × Y have positive energy.

**Filtered homology.** For a filtered complex C:
- F_t H is the image of H(C_{≤t}) in H = H(C).
- ℓ(ξ) = min{t : ξ ∈ F_t H}.
- For a subspace V ⊂ H, the spectrum is σ_k(V) = min{t : dim(V ∩ F_t H) ≥ k}.
- For a quotient H/W, σ_k(H/W) = min{t : dim((F_t H + W)/W) ≥ k}.
- ℓ(C) = σ₁(H), the lowest infinite bar, and ℓ⁺(C) is the highest infinite bar.
- The boundary depth β(C) is the length of the longest finite bar: every boundary w has a primitive of level ≤ lev(w) + β(C).

**Basic fact (PROVED).**
- ℓ(H) = min(σ₁(W), σ₁(H/W)) for every subspace W.
- Both the spectrum of a subspace and the spectrum of a quotient lie termwise at or above the spectrum of H.

**Both-bundle invariants.**
- λ_i = ℓ of the P_i theory.
- N_± = A_± ⊕ B_±.
- D_min(K) = ℓ(N₊) − ℓ(N₋) = min(λ₀, λ₁)(Y₂) − min(λ₀, λ₁)(Y₋₂).
- D_max(K) = ℓ⁺(N₊) − ℓ⁺(N₋).
- Mixed differences: m₁ = λ₀(Y₂) − λ₁(Y₋₂) and m₂ = λ₁(Y₂) − λ₀(Y₋₂).
- A cosmetic pair is an orientation-preserving diffeomorphism φ: Y₋₂ → Y₂.

**Level formula (BRIEF).**

  c(β) − c(α) = (i₀ + 3b⁺)/8 − E − Σ_j (3 − h(γ_j) + ρ(γ_j))/16,

with the additional term −s(F)/8 for maps singular along a surface F, where s(F) = χ(F) + F·F/2 (triangle-1 (1.1)).

---

## 2. Inputs and their status

### 2.1 Triangles used (RULES (c))

**(I)** A₊ →a T →b B₋ →c A₊. **(II)** B₊ →a′ T →b′ A₋ →c′ B₊.

These are triangle-1's Conjecture T. The RULES allow them to be assumed; their status is PLAUSIBLE.

**The cobordisms.**
- a and a′ are the trace (−X₂°, D_l) of +2 surgery with a ball removed, singular along the core disc with traceless holonomy. For a the bundle restricts to P₀ on Y₂; for a′ it restricts to P₁.
- b and b′ are (X₋₂°, D_r), with P₁ (for b) and P₀ (for b′) on Y₋₂.
- c and c′ are X₋₂,₂ = −(W′∖νS) with the class odd on ∂νS = L(4,1), whose limit there is γ₁ (rotation by π/2, h = 1, ρ = 1).

**Bundles summed and middle terms.**
- On the double cover branched along S, the outer terms of the invariant triangle are the sums over both bundles.
- The middle term is (I(S³) ⊕ T)^{⊕2} = T ⊕ T, because the irreducible theory of S³ vanishes.
- So the summed triangle is

  **(Σ)** N₊ →α T⊕T →β N₋ →γ N₊, with α = a ⊕ a′, β = b ⊕ b′ and γ = c ⊕ c′.

  Here γ exchanges the bundles: c maps B₋ to A₊, and c′ maps A₋ to B₊.

**Levels from the level formula.** Here η denotes the least energy of a counted solution.

| map | cobordism / family | b⁺ | i₀ | s | middle end | level |
|---|---|---|---|---|---|---|
| a, a′ | (−X₂°, D_l) | 0 | 0 | 1 − 2/2 = 0 | — | −η |
| b, b′ | (X₋₂°, D_r) | 0 | 0 | 0 | — | −η |
| c, c′ | X₋₂,₂, odd | 1 | 0 | — | L(4,1), γ₁: (3−1+1)/16 | 3/8 − 3/16 − η = **3/16** − η |
| g_A (I), g′_A (II) | W′, interval, nonsingular odd family + singular family | 0 | −1 | 0 | — | **−1/8** − η, with η > 0 |
| g_M, g_B and their (II) analogues | (X₋₂°, D_r) ∪ X₋₂,₂ and X₋₂,₂ ∪ (−X₂°, D_l), interval | 1 | −1 | 0 | γ₁ | (−1+3)/8 − 3/16 − η = **1/16** − η |
| pentagons | — | 1 | −2 | 0 | γ₁ | **−1/16** − η |
| g_S, g_S^w (same-bundle singular families on (W′, S), with P₀ resp. P₁ on both ends) | W′ | 0 | −1 | 0 | (face γ₀, null-homotopic) | −1/8 − η |
| H (four meridional handles) | W_H | 1 | 0 | — | L(4,3), γ₀: 1/4 | 1/8 − η |
| B (distance-four map) | W′, interval, μ(S) | 0 | +1 | — | — | 1/8 − η, with η > 0 |

**Homotopy relations (triangle detection).**
- d g + g d = (next map) ∘ (map), and f g + g f ≃ id at every vertex.
- In (I): g_A: A₊ → B₋ satisfies dg + gd = b a; g_M: T → A₊ satisfies dg + gd = c b; g_B: B₋ → T satisfies dg + gd = a c. The same pattern holds in (II).
- At every vertex the self-composite f g + g f has level **1/16** − η. For example, at A₊ it is c g_A + g_M a, of level max(3/16 − 1/8, 1/16 + 0).

### 2.2 Further inputs

| input | statement | status |
|---|---|---|
| same-bundle singular null-homotopies | b′ ∘ a ≃ 0 and b ∘ a′ ≃ 0. These are the J-faces of the singular families g_S and g_S^w on (W′, S). The other face of each is an exterior map with limit γ₀ on L(4,1), and that map is null-homotopic (B-final Thm A(e); for P₁ on both ends the class is even on S, so the same argument applies). | PLAUSIBLE (triangle-1 §3.2; analytic gaps as there) |
| orientation reversal | C(−Y) = C(Y)* with c ↦ 3/8 − c for both bundles, since ρ changes sign. Infinite bars [b, ∞) go to [3/8 − b, ∞), and finite bars [b, d) go to [3/8 − d, 3/8 − b). Gradings: g ↦ −3 − g (reference θ, h⁰ = 3, also used for the traceless normalisation) and g ↦ −1 − g (reference ζ, h⁰ = 1). | PROVED (APS: ρ_{−Y} = −ρ_Y; ell-1 §2.4) |
| gradings and degrees | Degrees mod 4: (a, b, c, a′, b′, c′) = (1, 1, 1, 3, 1, 3), with twisted gradings normalised as gr^w − σ (for Δ_K = 1, σ = 0). A homotopy has degree (deg f + deg f′ + 1). Hence deg(b′a) = 2 and deg(ba′) = 0. | deg a = 1: PROVED as index bookkeeping (triangle-1 §3.3); the full table: COMPUTED (§5, test 3) |
| χ-involution | Tensoring with the flat real line bundle of holonomy −1 on μ. It preserves levels and has degree 4 on P₀ (mod 8), 0 on P₁ (mod 8) and 0 on T (mod 4). It is free on P₀ always. It is free on P₁ and on T when det K = 1; the fixed points on T are the (det K − 1)/2 binary dihedral representations. It commutes with all the maps: a, b, c and their primed versions extend over cobordisms with H¹(·; Z/2) ≠ 0, and the maps between different bundles are sums over U(2) lifts c and c + 2a, which differ in degree by 4. Consequently maps between P₀ and P₁ are homogeneous only mod 4. | levels and degrees: COMPUTED (§5, test 2); commutation: PLAUSIBLE |
| balanced gradings | If φ exists, dim I_j(Y₂, P₀) is independent of j ∈ Z/8. The reason is that H∘φ_* is an automorphism of odd degree −3. | PROVED given (H1) (statements.tex, Cor. 1.4) |
| Euler characteristics | Unrolling the triangles with odd maps gives χ(A₊) + χ(T) + χ(B₋) = 0 and χ(B₊) + χ(T) + χ(A₋) = 0. | PROVED given (I), (II) and odd degrees |
| Casson–Lin | The signed count of traceless irreducibles is σ(K)/2 (Lin; Herald). In this normalisation χ(T) = −σ/2, which is 0 if Δ_K = 1. | standard; sign COMPUTED |
| Casson-type formulas | χ(A_±) = ±Δ″_K(1) and χ(B_±) = ±Δ″_K(1) + σ/2. All of these vanish if Δ_K = 1. | COMPUTED for torus knots; PLAUSIBLE in general (Boyer–Lines / Curtis type) |
| nonvanishing | H(T) ≠ 0 for K nontrivial. If H(T) = 0, Daemi–Scaduto's complex C ⊕ C ⊕ F for I^♮ has homology F, and then K is the unknot (Kronheimer–Mrowka). | PLAUSIBLE (standard inputs) |
| energy (RULES (a)) | E ≥ 0. E > 0 when no flat (zero-energy) contribution exists. | — |

**Which maps can have flat (zero-energy) contributions when Δ_K = 1.**
- **g_A and g′_A: never.** W′ is simply connected, and a flat singular contribution would need a traceless representation with λ ↦ −1 and λ ↦ +1 at once. (PROVED)
- **a′ and b (twisted ends): never.** A flat singular connection would be a traceless representation with λ ↦ +1, which is binary dihedral, and there are none when det K = 1. (PROVED)
- **a and b′ (untwisted ends): possibly.** A flat singular connection here is a traceless representation with λ ↦ −1. Such a representation corresponds to an irreducible τ-equivariant SU(2) representation of π₁Σ₂(K), and det K = 1 does not exclude these. (PROVED as topology)
- c, c′, g_M, g_B: possibly (mixed common points; the cobordisms are not simply connected).

### 2.3 Filtered algebra (all PROVED; general complexes, nonzero differentials allowed)

**Lemma 2.1.** A chain map f of level ≤ λ satisfies f_*(F_t H) ⊂ F_{t+λ} H′. Hence:
- σ_k(f_*V) ≤ σ_k(V) + λ when f_* is injective on V;
- the same holds for an injective map induced on a quotient.

**Lemma 2.2 (vertex lemma).** Suppose that:
- (f, g): X → Cone(f′: Y → Z) is a quasi-isomorphism, where dg + gd = f′f;
- the levels of f, g, f′ are λ_f, λ_g, λ_{f′};
- x is a cycle with [x] ≠ 0.

Then either [fx] ≠ 0, or fx = dy and [gx + f′y] ≠ 0 in H(Z). In the second case y can be chosen with lev(y) ≤ lev(fx) + β(Y). So H(Z) has a nonzero class of level at most

  max(lev x + λ_g, lev x + λ_f + β(Y) + λ_{f′}).

*Proof.* (fx, gx) is a cycle of the cone with nonzero class. Adding the boundary of (y, 0) gives (0, gx + f′y). Z is a subcomplex of the cone, so this class is nonzero in H(Z). ∎

**Lemma 2.3 (connecting isomorphisms).** Let X →f Y →f′ Z →f″ X come from triangle detection, with homotopies g: X → Z and g_Y: Y → X. Then g induces an isomorphism G: ker f_* → coker f′_*, namely [x] ↦ [gx + f′y] where fx = dy. The inverse of G is the isomorphism coker f′_* → ker f_* induced by f″.

Levels: G has level ≤ λ_g in the perfect case, and ≤ max(λ_g, β(Y) + λ_{f′}) in general.

*Proof.* We have

  f″(gx + f′y) = (q_X − g_Y f)x + f″f′y = q_X x − g_Y dy + (d g_Y + g_Y d)y = q_X x + d(g_Y y),

where q_X = f″g + g_Y f ≃ id. So f″ ∘ G = id on ker f_*. Both sides have the same dimension. ∎

---

## 3. The theorem the strategy aims at

**Target.** For every nontrivial knot K,

  D_min(K) > 0  or  D_max(K) > 0.

**Why this suffices.** By §4.1, D_max(K) = D_min(K̄). So the target says that K or K̄ has a positive both-bundle drop at the bottom.
- A cosmetic pair for K is also one for K̄: Y₂(K̄) = −Y₋₂(K) ≅ −Y₂(K) = Y₋₂(K̄).
- A cosmetic pair forces D_min(K) = D_max(K) = 0, and also m₁ = −m₂.
- So the target excludes ±2 cosmetic surgery.

It is the weakest drop statement of the required kind, with a consistent sign, that suffices: "> 0" is enough. The data have D_min, D_max ≥ 1/8 − 1/884 in all cases.

**What is actually proved.**
- The necessary conditions of Theorem 4.4 and Corollary 4.5.
- The realisability Theorem 4.6, which shows that the target does not follow from the inputs of §2.

---

## 4. The argument

### 4.1 The mirror triangles are the duals (PROVED, given that (I) and (II) are defined by the cobordism counts of §2.1)

**Proposition 4.1.** Triangle (I) for K̄ is the dual of triangle (II) for K, and (II) for K̄ is the dual of (I) for K. In detail:

- a_{K̄} = (b′)*, b_{K̄} = (a′)*, c_{K̄} = (c′)*.
- g_{A,K̄} = (g′_A)*, g_{M,K̄} = (g′_B)*, g_{B,K̄} = (g′_M)*.
- Levels are unchanged.
- The degree table (1, 1, 1, 3, 1, 3) is carried to itself.

*Proof.*
- The dual of the map of a cobordism W: Y → Y′ is the map of the same oriented 4-manifold, read as a cobordism −Y′ → −Y.
- −X₂°(K) = X₋₂°(K̄), read upside down, is the cobordism of b for K̄, and similarly for the others.
- A level shift L for C(Y) → C(Y′) becomes a level shift L for C(−Y′) → C(−Y), because c ↦ 3/8 − c on both ends.
- Degrees: a map X → Y of degree e has a dual of degree e + (const_X − const_Y), where const = −3 for θ and the traceless normalisation and −1 for ζ. Applied to the table, this gives back (1, 1, 1, 3, 1, 3). This is also checked on the data (§5, test 3). ∎

**Consequence.**
- Combining the triangles for K and K̄ adds nothing beyond running (I) and (II) at the **top** of the spectrum: ℓ ↔ 3/8 − ℓ⁺.
- The cosmetic map φ for K̄ is the same diffeomorphism with reversed orientation, so it adds nothing new either.
- In particular, D_max(K) = max(λ₀⁺, λ₁⁺)(Y₂) − max(λ₀⁺, λ₁⁺)(Y₋₂) = D_min(K̄).

### 4.2 Euler characteristics, ranks, gradings (PROVED from §2.2)

**Proposition 4.2.**

(a) χ(A₊) + χ(T) + χ(B₋) = 0 and χ(B₊) + χ(T) + χ(A₋) = 0.

(b) If Δ_K = 1, all six Euler characteristics vanish. Under φ this already follows from balance and Casson–Lin alone: χ(A) = 0 and χ(T) = 0 give χ(B) = 0.

(c) If det K = 1, then dim H(A_±), dim H(B_±) and τ are even. The reason is that a free F₂[Z/2]-complex C has dim H(C) = 2 dim H(D) − 2 rank δ, where D = C/(1+χ)C and δ is the connecting map of 0 → (1+χ)C → C → D → 0.

**Proposition 4.3 (image lemma).** Assuming the same-bundle null-homotopies,

  im a = im a′ = ker b = ker b′ =: I ⊂ H(T).

Hence α₊ + α₋ = β₊ + β₋.

Under a cosmetic pair, moreover:
- dim H(A) = dim H(B);
- rank a = rank a′ = rank b = rank b′ = τ/2;
- rank c = rank c′ = dim H(A) − τ/2.

*Proof.*
- b a = 0 and b′ a = 0 (the first by (I), the second by the null-homotopy), so im a ⊂ ker b ∩ ker b′ = im a ∩ im a′, using exactness of (I) and (II). Symmetrically, im a′ ⊂ ker b ∩ ker b′.
- So im a = im a′ = ker b = ker b′.
- The rank identities follow from exactness. For example, α₊ − β₋ = rank a − rank b = β₊ − α₋.
- Under φ, α₊ = α₋ and β₊ = β₋. ∎

**Remarks on gradings.**
- Balanced gradings, χ, Euler characteristics and Casson–Lin together give only these identities.
- For Δ_K = 1 they impose no inequality among levels.
- Parity, which kills a (positive torus knots) or b (mirrors) in all the data, is unavailable when the gradings are balanced.

### 4.3 The three filtered isomorphisms of the summed triangle (PROVED; perfect case, general case with boundary depth)

Apply Lemma 2.3 at the three vertices of (Σ).

**Proposition 4.4.**

(a) α induces N₊/ker α ≅ im α, of level −η_α. The inverse comes from the vertex homotopy at T⊕T, of level **1/16** in the perfect case and max(1/16, β(N₋) + 3/16) in general.

(b) β induces (T⊕T)/im α ≅ im β, of level −η_β. The inverse comes from the vertex homotopy at N₋, of level **1/16** in the perfect case and max(1/16, β(N₊) − η_α) in general.

(c) γ induces N₋/im β ≅ ker α, of level **3/16**. The inverse is induced by g_N = g_A ⊕ g′_A, of level **−1/8 − η_g** with η_g > 0. In general the inverse has level max(−1/8 − η_g, β(T) − η_β).

So, for every k:
- σ_k(im α) + η_α ≤ σ_k(N₊/ker α) ≤ σ_k(im α) + 1/16;
- σ_k((T⊕T)/im α) − 1/16 ≤ σ_k(im β) ≤ σ_k((T⊕T)/im α) − η_β;
- σ_k(ker α) − 3/16 ≤ σ_k(N₋/im β) ≤ σ_k(ker α) − 1/8 − η_g.

### 4.4 The bottom formula and the conditions for a vanishing drop

Put s = ℓ(N₊), κ = σ₁(ker α) (∞ if ker α = 0), p = σ₁(im α) and q = σ₁((T⊕T)/im α).

**Theorem 4.4 (perfect complexes; PROVED from §2).**

(i) **Bottom formula.**

  ℓ(N₊) = min(κ, p + e₁),  ℓ(N₋) = min(κ − 1/8 − e₂, q − e₃),

with e₁ ∈ [η_α, 1/16], e₂ ∈ [η_g, 1/16] and e₃ ∈ [η_β, 1/16]. All three error terms are bounded by E_cap = 1/16.

(ii) **If D_min(K) ≤ 0, then:**
1. **Absorption.** p + e₁ = s < κ − 1/8. So the bottom class of N₊ lies outside ker α, and the bottom of im α lies in [s − 1/16, s − η_α].
2. **The traceless classes below s are in the image.** q ≥ s + η_β, i.e. every class of T⊕T below s + η_β lies in im α. In particular μ := ℓ(T) = p.
3. **Counting.** ker α meets F_t only for t ≥ s + 1/8 + η_g. So a (resp. a′) is injective on the n_A (resp. n_B) classes of H(A₊) (resp. H(B₊)) lying below s + 1/8. Hence

   n_A ≤ rank a = (α₊ + τ − β₋)/2  and  n_B ≤ rank a′ = (β₊ + τ − α₋)/2.

4. **Matching.** For k ≤ n_A, the k-th class of A₊ satisfies a_k ≥ σ_k(im a) + η_a ≥ μ_k + η_a. Likewise b_k ≥ μ_k + η_{a′} for k ≤ n_B. If b = 0 (as for the mirrors of torus knots), im a = H(T) and also a_k ≤ μ_k + 1/16.

(iii) **The top.** If D_max(K) ≤ 0, the duals of 1–4 hold at the top. This is (ii) applied to K̄ by Proposition 4.1: the classes of N₋ within 1/8 of its top are "co-absorbed" through b, b′, within (η, 1/16] below classes of T/I.

*Proof.*
- (i) ℓ(V) = min(σ₁(W), σ₁(V/W)). Use W = ker α ⊂ N₊ and Proposition 4.4(a) for ℓ(N₊). Use W = im β ⊂ N₋ and Proposition 4.4(b), (c) for ℓ(N₋).
- (ii) ℓ(N₋) ≥ s forces κ − 1/8 − e₂ ≥ s and q − e₃ ≥ s. Then ℓ(N₊) = min(κ, p + e₁) cannot equal κ. Since ker α ∩ F_{<s+1/8} = 0, the quotient N₊ → N₊/ker α is injective on F_{<s+1/8}, so σ_k(N₊/ker α) = s_k for those k. Now apply Proposition 4.4(a), using σ_k(im α) ≥ σ_k(T⊕T). The ranks come from exactness. ∎

**General version (nonzero differentials; PROVED from Lemma 2.2).** If D_min(K) ≤ 0, then the traceless complex has a bar [b, d), possibly with d = ∞, such that

  b ≤ s − η_α  and  d ≥ s + η_β.

*Proof.* Take a cycle x realising s. If αx is a boundary dy, then by Lemma 2.2 every primitive has lev y ≥ s + η_β, and αx is born at ≤ s − η_α. Otherwise αx gives an infinite bar. ∎

At the top the dual statement holds: T has an infinite bar born at ≥ ℓ⁺(N₋) + η, or a finite bar straddling ℓ⁺(N₋). With nonzero differentials, the 1/16 margins degrade by the boundary depths (Proposition 4.4).

### 4.5 A cosmetic pair

**Corollary 4.5 (PROVED from §2; perfect case for 2–4).** If φ exists, write N = A ⊕ B, s = ℓ(N) and s⁺ = ℓ⁺(N). Then:

1. **Both ends are absorbed.**
   - The lowest class of T lies in I = im a = im a′, at most 1/16 below s.
   - The highest class of T is not in I (the top of T is attained modulo I), at most 1/16 above s⁺.
   - Hence μ < s ≤ μ + 1/16 and μ⁺ − 1/16 ≤ s⁺ < μ⁺.
   - This recovers triangle-1 Proposition 5.6 in both-bundle form, at both ends.
2. **Counting at both ends.**
   - The classes of A within 1/8 above its bottom, and likewise the classes of B within 1/8 above its bottom, inject into I. So each set has at most τ/2 classes.
   - Dually, the classes of A and of B within 1/8 below their tops are hit from T/I. So each of these sets also has at most τ/2 classes.
3. **Matching at both ends.**
   - The spectrum of I contains a copy of the bottom 1/8-slice of each of A and B, lowered by an amount in (η, 1/16].
   - The spectrum of T/I contains a copy of the top 1/8-slice of each, raised by an amount in (η, 1/16].
4. **With nonzero differentials**, 1 is replaced by the barcode statement above. A single finite bar of T that straddles both s and s⁺ satisfies both ends, even if H(T) restricted to that block is 0.
5. **A conditional consequence of 2 (PLAUSIBLE, needs the B-map to be an isomorphism (H2)).**
   - φ_*⁻¹ ∘ B is an automorphism of H(A) of degree −1 and level < 1/8, because η_B > 0 on the simply connected W′.
   - So the bottom class x₀, χx₀, Bx₀ and χBx₀ are four classes in distinct degrees below s + 1/8.
   - Hence τ ≥ 8.

### 4.6 Trying to close the argument, and why it cannot be closed (PROVED by explicit models)

A contradiction requires that conditions 1–3 of Corollary 4.5 be incompatible with each other, or with gradings, χ, balance, Euler characteristics or duality. They are compatible.

**Theorem 4.6 (realisability).** There are finite filtered complexes over F₂ with the following properties:
- A is Z/8-graded, B is Z/8-graded, and M is Z/4-graded.
- There are maps a, b, c, a′, b′, c′ and homotopies for both triangles, and maps H and B on A.
- All of the following hold:
  - (C1) d² = 0, deg d = −1, and d strictly lowers levels;
  - (C2) the six maps are chain maps with the degree table of §2.2. a, a′, b, b′ have level < 0, strictly: this is the most restrictive case, with no flat singular connections at all. c and c′ have level ≤ 3/16;
  - (C3) the homotopy relations hold in both triangles, with the degrees of §2.1. The g_A's have level < −1/8, strictly. The other homotopies have level ≤ 1/16;
  - (C4)–(C5) f g + g f = id at all six vertices, and all six triangle-detection maps are quasi-isomorphisms, so both triangles are exact;
  - (C6) b′a = 0 = b a′;
  - (C7) free χ-involutions with the degrees of §2.2, preserving levels and commuting with d and with every map and homotopy;
  - (C8) dim H_j(A) is independent of j ∈ Z/8;
  - (C9) automorphisms of A of degree −3 (level ≤ 1/8) and −1 (level < 1/8);
  - (C10) χ(A) = χ(B) = χ(M) = 0;
  - (C11) H(M) ≠ 0;
  - (C12) the dual model, with levels 3/8 − c, gradings reversed, maps transposed and (I) ↔ (II)*, satisfies (C1)–(C11).
- In each model the two ends are literally equal (φ = id), so ℓ and ℓ⁺ of A and B agree on both sides.
- In each model m₁ = m₂ = 0 and the both-bundle drops at the bottom and the top are 0.

*Construction* (`model.py`). The complexes are built from blocks indexed by j ∈ Z/8, and χ shifts j by 4.

- **Absorbing block (perfect).** Generators x_j ∈ A (level 0), y_j ∈ B (level 0), z1_j ∈ M (level −1/32) and z2_j ∈ M (level +1/32).
  - Maps: a x_j = z1_j, a′ y_j = z1_j, b′ z2_j = x_j, b z2_j = y_{j+2}, c = c′ = 0.
  - Homotopies: g_M z1_j = x_j, g_B y_{j+2} = z2_j, g′_M z1_j = y_j, g′_B x_j = z2_j.
  - Both minimisers are absorbed by z1 at cost 1/32 < 1/16, and both maximisers are co-absorbed by z2.
- **Window block (perfect, c, c′ ≠ 0).**
  - Non-absorbed classes x′ ∈ A and y″ ∈ B lie 0.15 ∈ (1/8, 3/16] above their partners y′ ∈ B and x″ ∈ A.
  - The third maps are c y′ = x′ and c′ x″ = y″, with inverses g_A and g′_A of level −0.15.
- **Finite-bar block (nonzero differential).** M ∋ w (level −1/32) and w′ (level +1/32), with d w′ = w.
  - The minimisers are absorbed into a **boundary**: a x = w and a′ y = w.
  - The third maps c and c′ are isomorphisms of level 0, so this block's traceless homology is 0.
  - The vanishing drop is paid for entirely by the boundary depth 1/16 of C^tl.

All four combinations of blocks, and their duals, pass every check (0 errors). Seven negative controls are all detected:
- a traceless bottom 1/15 below the minimisers;
- a traceless top 1/15 above the maximisers;
- zero-energy absorption;
- a window gap 0.1 < 1/8;
- a window gap 0.2 > 3/16;
- a deleted homotopy entry;
- b′a ≠ 0.

So the verifier is not vacuous. ∎

**Consequence (PROVED, as logic).** No argument whose only inputs are those of §2 can prove D_min > 0, D_max > 0, m₁ + m₂ > 0, or either of m₁, m₂ > 0 for a knot with Δ_K = 1. The inputs are:
- the triangles (I), (II) and their mirrors, with the levels of every map and homotopy;
- the same-bundle null-homotopies;
- φ;
- gradings mod 8 with the degree table;
- χ;
- balanced gradings and the odd automorphisms H, B;
- Euler characteristics and Casson–Lin;
- H(T) ≠ 0;
- E ≥ 0, and E > 0 where no flat connection contributes;
- the filtered algebra of Lemmas 2.1–2.3, with nonzero differentials allowed.

This holds even with all singular maps strictly negative (no flat contributions at all).

---

## 5. Tests against the data

Scripts: `tests_data.py`, `counting.py` and `fig8_ctl.py`. The data are the torus knots T(p,q) with pq ≤ 60 (29 knots, both chiralities) and 4₁.

| # | step tested | result |
|---|---|---|
| 1 | Euler relations of Proposition 4.2(a); χ(T) = −σ/2; Casson-type formulas | all 58 cases (COMPUTED) |
| 2 | χ-involution, computed from the exact action (k, l, a) ↦ (k′, l′, ½ − a) | levels preserved; degrees 4 (P₀, mod 8), **0** (P₁, mod 8), 0 (T, mod 4); P₀ free; fixed points on P₁ and T only when det > 1; on T exactly (det − 1)/2 (COMPUTED). The degree 0 on P₁ corrected my first model, which had 4: maps between bundles are homogeneous only mod 4. |
| 3 | degree table, from graded exactness (positive knots: a = a′ = 0; mirrors: b = b′ = 0) | One assignment mod 4 fits all 29 knots of each chirality, once the twisted grading is normalised by −σ: (a, b, c, a′, b′, c′) = (1, 1, 1, 3, 1, 3). It is consistent with the independent index value deg a = 1 and with the triangle rule (sum ≡ −1 mod 4). The table predicted for K̄ by duality (Proposition 4.1) equals the one found (COMPUTED). |
| 4 | D_min and D_max | Positive knots: min D_min = 0.1368 > 1/8, as Theorem 4.4(i) forces (α = 0, so ℓ(N₋) ≤ s − 1/8 − η). Mirrors: min D_max = 0.1368 > 1/8, likewise. The other ends: min 219/1768 = 1/8 − 1/884 (T(3,5) top, T̄(3,5) bottom). 4₁: D_min = D_max = 1/8 (COMPUTED). |
| 5 | bottom formula, Theorem 4.4(i) | consistent in all 58 cases (positive: α = 0; mirrors: β = 0, κ ∈ spectrum). For 4₁ it holds with e₁ = 0 (flat absorption at a binary dihedral point) and e₂ = 3/80 (COMPUTED). |
| 6 | the cruder test (absorption window only, conditions 1–2): is D_min ≤ 0 excluded? | It is **not** excluded for the 7 det-1 mirrors T̄(3,5), T̄(3,7), T̄(3,11), T̄(3,13), T̄(5,7), T̄(5,9), T̄(5,11) (bottom), nor for their mirror images (top). These are triangle-1's "half-cosmetic" knots. No knot passes both ends (COMPUTED). |
| 7 | the full conditions 1–4 of Theorem 4.4(ii) (counting and matching), without using that parity kills a or b (only dimensions, levels and positivity) | D_min ≤ 0 and D_max ≤ 0 are excluded in **all 58 cases**; with parity as well. Example: T̄(3,5) has 8 classes of I(Y₂) within 1/8 of the bottom but rank a = 4. T̄(5,9) passes counting (12 ≤ 12) but fails matching: a₃ = −2.593 < μ₃ = −2.543 (COMPUTED, `counting.py`). |
| 8 | 4₁ traceless levels | The character curve is cos 2πβ = cos 8πα − cos 4πα − 1, with a double point at (¼, 0) and branch slopes ±2√5. Φ on the positive-slope passage minus Φ on the negative-slope passage is −1/10. This gives T(4₁) = {7/40, 1/5} (triangle-1's option 1), which is self-dual under c ↦ 3/8 − c (COMPUTED; the rule "traceless level = Φ + sgn(slope)/16" is PLAUSIBLE outside torus knots). |
| 9 | 4₁ against Theorem 4.4(ii) | Counting against dim T alone does not exclude a vanishing drop (2 ≤ 2). Counting against rank a = (2 + 2 − 2)/2 = 1 < n_A = 2 does; by amphichirality the same holds at the top. Independently, the lowest traceless class 7/40 maps by a flat singular connection (E = 0) onto the generator 7/40 of I^w(Y₋₂), so it is not in ker β. This gives D_min ≥ 1/5 − 7/40 = 1/40 from an exact zero-energy contribution: the RULES (a) mechanism (COMPUTED/PLAUSIBLE). |
| 10 | ranks of Proposition 4.3 | α₊ + α₋ = β₊ + β₋ in all cases (trivially, by parity, for torus knots). For 4₁, rank a = rank a′ = 1, and a level-compatible configuration with I = ⟨x₁⟩ exists (COMPUTED). |

**Reading of the tests.**
- No proved step fails on the data.
- The necessary conditions for a vanishing drop fail for every knot in the data, at both ends. So the soft structure explains every observed drop.
- Torus knots explain it either by parity or by counting and matching. 4₁ explains it by counting, or by a flat binary dihedral contribution.
- The models of §4.6 show that the same conditions can be met by abstract data with balanced gradings. What separates the data from the models is the position and number of generators of T(K) relative to those of I(Y₂). The triangles do not control that.

---

## 6. Where the strategy fails, and what it would need

**The failing step.**
- Steps 4.1–4.5 go through. Step 4.6, excluding conditions 1–3 of Corollary 4.5 at both ends, does not.
- No step fails on the data. The failure is abstract (Theorem 4.6): the inputs admit a cosmetic model.

**What would close it.** Any of the following, for Δ_K = 1:

(a) **An absorption cost ≥ 1/16** for a or a′ on the bottom class (and dually for b, b′ at the top). This is an energy lower bound equivalent to the drop: it is the rejected Step 4 of rho.pdf. *Forbidden by RULES (a).*

(b) **A boundary-depth bound for C^tl(K)**, needed already with nonzero differentials (the finite-bar block). Boundary depth is bounded by the energies of differential trajectories, so this is again an energy estimate. *Forbidden.*

(c) **A non-energy statement about the spectrum of T(K) relative to I(Y₂)**, of the form "more than τ/2 classes of I(Y₂) lie within 1/8 above its bottom", or "the k-th of them lies below the k-th traceless class". It holds in all the data (test 7), but nothing structural forces it once parity is gone. It is a statement about the distribution of adjoint ρ-invariants, and I see no non-energy route to it. *SPECULATIVE; I could not supply it.*

(d) **An exact zero-energy contribution** at the bottom of T(K). If the lowest traceless class is a representation with λ ↦ −1, and b′ counts it by a flat singular connection of index 0, then condition 2 of Theorem 4.4(ii) fails and D_min ≥ s − μ > 0. This is exactly the 4₁ mechanism. For det K = 1 the twisted version is unavailable, but the untwisted one is not excluded. *SPECULATIVE as a strategy:* it needs the bottom of T(K) to be such a representation, and nothing forces that.

**Non-energy structure the models do not encode, and might in principle constrain them (SPECULATIVE):**
- the u-map (μ(pt), degree 4, level 1/2) and its compatibility with all the maps;
- the reducibles: θ, χθ on Y_{±2}, θ_K in Daemi–Scaduto's framed complex, and the Frøyshov-type invariants. Under φ these coincide on both sides;
- the triangles through Y_{±1} and Y₀ (Floer, CDX).

I did not find a mechanism by which any of these acts on the bottom 1/16 of the spectrum.

**A remark on deforming the holonomy (PROVED as topology).**
- For Δ_K = 1, the irreducible singular theory with holonomy α vanishes for α near 0, because the character curve is closed and stays away from α = 0.
- It would be tempting to run the triangles with V_α in place of the traceless circle. But flat connections on the neck L(4,1) = ∂νS need fibre holonomy of order dividing 4, so the lens neck of the bundle-exchanging triangle exists only for α ∈ ¼Z.
- The traceless value is forced, so this deformation is unavailable.

---

## 7. What the angle gives (summary)

| statement | status |
|---|---|
| Triangles for K̄ = duals of those for K (Proposition 4.1); D_max(K) = D_min(K̄); the degree table is self-dual | PROVED (given the construction); table COMPUTED |
| Euler relations; for Δ_K = 1 all Euler characteristics vanish; even ranks for det K = 1 (Proposition 4.2) | PROVED from §2 |
| im a = im a′ = ker b = ker b′; under φ, dim I(Y,P₀) = dim I(Y,P₁) and rank a = rank a′ = τ/2 (Proposition 4.3) | PROVED given the same-bundle null-homotopies (PLAUSIBLE) |
| The three filtered isomorphisms of the summed triangle, with levels −η / 1/16, −η / 1/16 and 3/16 / −1/8 − η (Proposition 4.4) | PROVED (perfect); with boundary-depth corrections in general |
| Bottom formula and necessary conditions for D_min ≤ 0 (absorption, image, counting, matching), and their duals at the top (Theorem 4.4) | PROVED (perfect); barcode version in general |
| Cosmetic pair ⇒ two-ended absorption within 1/16, counting ≤ τ/2 at both ends; τ ≥ 8 if B is an isomorphism (Corollary 4.5) | PROVED; last item PLAUSIBLE |
| These inputs cannot prove any drop > 0 (Theorem 4.6) | PROVED (explicit verified models) |
| The necessary conditions fail for all 58 torus-knot cases and for 4₁, at both ends | COMPUTED |
| T(4₁) = {7/40, 1/5}; for 4₁, D_min ≥ 1/40 from a zero-energy flat contribution | COMPUTED / PLAUSIBLE |
| Twisted χ-degree 0 mod 8; maps between bundles homogeneous only mod 4 | COMPUTED / PLAUSIBLE |

---

## 8. How 1/16 enters

The number is E_cap = 1/16, the energy of the odd reducible cap on νS, equivalently (3 − h + ρ(γ₁))/16 with ρ(γ₁) = 1 on L(4,1). In this strategy it appears in five places, and nowhere as an obstruction:

1. The third maps c and c′ have level 1/8 + 1/16 = 3/16.
2. The vertex homotopies next to them have level 1/16.
3. The self-composites f g + g f have level 1/16 at all three vertices: the triangle "returns" with a loss of at most E_cap.
4. The three error terms of the bottom formula lie in [η, 1/16].
5. A cosmetic pair requires the traceless theory to shadow both ends of the spectrum within 1/16. The absorption cost must be < 1/16.

Orientation reversal leaves the levels of maps unchanged, so the same 1/16 governs the top.

**In the data:**
- absorption costs 0.0017–0.0037 for the det-1 mirrors;
- it costs 0 for T̄(2,3) and 4₁, at binary dihedral points.

So 1/16 is a ceiling on the cost of absorption, not a floor. The 1/16 alone cannot force a drop: it limits how far below the bottom the traceless theory can sit, but nothing prevents it sitting just below.

---

## Appendix: code (`scratchpad/r6/duality-code/`)

- **`common.py`**: graded spectra (levels and gradings) of A_±, B_± and T for positive torus knots, the mirror rule, and the 4₁ data.
- **`tests_data.py`** (output `tests_data.out`): tests 1–7 and 10 of §5. These cover Euler/Casson–Lin, the χ action and its degrees, the graded-exactness degree table and its duality, the drops, the bottom formula, the cruder absorption test, and the ranks.
- **`les_detail.py`**: per-knot admissible degrees. It is diagnostic: it shows the σ/2-parity dependence that the −σ renormalisation removes.
- **`counting.py`** (output `counting.out`): the full necessary conditions of Theorem 4.4(ii), with and without parity, at both ends, for all cases and 4₁.
- **`fig8_ctl.py`** (output `fig8_ctl.out`): slopes and Φ at the double point of the 4₁ character curve, giving T(4₁) = {7/40, 1/5}.
- **`model.py`** (output `model.out`): the verifier for constraints (C1)–(C12), the four cosmetic models and their duals (0 errors), and seven negative controls (all detected).
