# Judge's report: the ±2 drop after the no-go

Setting, normalisations and rules are those of `r6/BRIEF.md` and `r6/RULES.md`. Notation:
- Y_N = S³_N(K), with bundles P₀ (w₂ = 0) and P₁ (w₂ ≠ 0);
- c = (3 + ρ)/16 for every irreducible flat SO(3) connection;
- λ_i = ℓ of the P_i theory, and Λ(Y) = min(λ₀, λ₁)(Y);
- T = C^tl(K), the irreducible traceless complex, and r = rank of its χ-reduced homology;
- C is the image of R*(E_K) in the pillowcase, with coordinates ρ(μ) ~ e^{2πiα}, ρ(λ) ~ e^{2πiβ}, and δ = α − 1/4.

Labels:
- **PROVED**: a complete argument from stated inputs. The exact triangles (I) and (II) are assumed, as rule (c) allows.
- **COMPUTED**: an exact or high-precision machine check. New scripts are in `r6/judge-code/`.
- **PLAUSIBLE**: an argument with a named gap.
- **SPECULATIVE**: a heuristic.

---

## 0. Verdict

1. **The no-go result is correct (PROVED; checked by five independent implementations, one of them mine).** Here is what it shows is not enough. Take:
   - the triangles with every level of the ledger;
   - positivity of energy, even strict positivity on every singular map;
   - nonzero or zero differentials;
   - the degree table, the χ-involution with its correct degrees, and balanced gradings;
   - the same-bundle relations b′a = 0 = ba′;
   - Euler characteristics, Casson–Lin, and H(T) ≠ 0;
   - the mirror (dual) triangles, the odd automorphisms of a cosmetic pair, and the lift to the branched double cover.

   All of these together admit a cosmetic model with every drop equal to 0. A proof must use where the generators actually sit, that is, the ρ-invariants of flat connections, or some other structure not on that list.

2. **χ acts with degree 4 on P₀ and degree 0 on P₁ (mod 8)** (PROVED from the pillowcase Chern–Simons formula; COMPUTED in 48 cases). χ-twins therefore produce no clustering in χ-reduced counts, and the spacing condition is unchanged by doubling.
   - The real sources of clustering are two: the cosmetic window |λ₀ − λ₁| < 1/16, and, under (H2), the odd automorphism φ⁻¹B of level < 1/8.
   - Together they exclude r = 2, and r is always even and at least 2. So a cosmetic pair with perfect complexes needs r ≥ 4.
   - This yields no contradiction, because nothing bounds r above for Δ_K = 1.

3. **The most promising additional input is (c), the pillowcase structure.** It enters through a precise calculus lemma, the steep-minimum lemma of §2.3.
   - **The key fact.** dΦ = 2δ dβ along C, so the critical points of Φ on C are exactly the traceless points and the horizontal tangencies. Positive-slope traceless points are local minima and negative-slope ones local maxima. When Δ_K = 1 the curve C is closed, so min_C Φ is attained at one of these critical points.
   - **The conclusion.** If the minimum lies on a steep branch, every generator of Y₂ (both bundles) sits at least Φ₀ + 1/16 high, and some generator of Y₋₂ sits at most Φ₀ − 1/16 + 1/(16(s* − 2)). Here Φ₀ is the minimum value and s* the least slope near the minimiser. So the generator-level both-bundle drop is at least 1/8 − 1/(16(s* − 2)), which is at least 1/16 once s* ≥ 3.
   - **Tests.** The lemma holds on all 16 mirror torus knots tested and on 4₁ (COMPUTED). It is sharp: it attains m₂ = 1/16 for T̄(2,3) exactly.
   - **How it reaches the cosmetic problem.** The multiset of ρ-values of flat connections is a diffeomorphism invariant. This turns the lemma into a cosmetic obstruction that uses no energy and no differentials.
   - **What it does not give.** It is not a statement about λ_i. On the Floer side it gives only the lower bound Λ(Y₂) ≥ Φ₀ + 1/16, which holds for any differential.
   - **What remains open.** The general pillowcase formula (PLAUSIBLE, about 70%), and a steepness-type hypothesis on C for Δ_K = 1 knots (SPECULATIVE).

4. **Ranking:** (c) > (a) > (d) > (b).
   - (a), the counting lemma, is correct (I re-derived it) and is the right Floer-theoretic consumer of spectral information. But its Input X fails in plain form for 4₁ and is provably vacuous in the ±1/n analogue.
   - (d) gives drops only when the bottom of the traceless spectrum is a common point. That is non-generic when det K = 1.
   - (b) cannot produce a contradiction.

5. **±1/n.**
   - **The triangle does not prove it.** The two-step pair (−1/n, −1/(n+2)) is a distance-two problem with closed middle term I(Y_{−1/(n+1)})^{⊕2}. Its triangle is short exact, with an injective first map (DLME). So every class is absorbed and the counting form is vacuous (PROVED; COMPUTED). The two-step 1/8 therefore cannot be proved by the same argument; it meets the middle-term obstruction in its strongest form.
   - **Correction to drops.md §4(c).** The equality cases are realised exactly by a flat SO(3) connection on X_n∖νS, with RP³ end the rotation by π. These connections exist at representations whose meridian and longitude are both traceless. drops.md's van Kampen argument considered SU(2) representations only. The exact −1/8 shift holds at every such shared representation (COMPUTED).
   - **The lesson for ±2.** The exact values (1/8 for the two-step; 1/8 and 3/16 for ±2) are levels of flat connections at shared points. For ±2, the generic (unshared) case falls just below 1/8 by an amount that the pillowcase geometry controls.

---

## 1. Verification of the no-go result

### 1.1 What I ran

| model | script | constraints it satisfies | result |
|---|---|---|---|
| critic Examples 1–3 | `critic_toys.py` | (I), (II), triangle detection with q = id and h = 0, ledger levels with strict positivity for a, b and g_A, homogeneity | OK; Ex. 1 has drop 0; Ex. 2 (acyclic middle term, finite bar of CS-length 37/200) and Ex. 3 have drop −1/50 |
| cover Models 1–2 | `cover-code/nogo.py` | the above, plus degrees mod 4, χ(Euler) = 0, a free χ, and an upstairs lift with DLME's levels | OK; drop = m₁ = m₂ = 0 |
| duality Models 1–4 and their duals | `duality-code/model.py` | (C1)–(C12): Z/8 and Z/4 gradings, the degree table (1,1,1,3,1,3), χ of degree 4/0/0, b′a = 0 = ba′, balanced A, odd automorphisms H and B, Euler 0, H(T) ≠ 0, the dual model; Model 3 has a nonzero differential | 0 errors; all seven negative controls detected |
| exact Models 1–3 | `exact-code/toy.py` | relations, exactness by ranks, windows, Euler; Model 3 is a kernel case with a long bar | OK; Model 3 has m₁ = −1/16 |
| **judge model** (new code) | `judge-code/nogo_judge.py` | everything in the next list | 0 errors; 7 of 7 negative controls detected (`nogo_controls.out`) |

The judge model was written from scratch and shares no code with the four reports. It has two blocks:
- an absorbing block, which is perfect;
- a finite-bar block with d ≠ 0 on T, in which c and c′ are isomorphisms of level 0.

The script checks all of the following:
- d² = 0, d of degree −1, and d raising c by less than 1/8 (positive energy);
- that a, b, c, a′, b′, c′ are chain maps;
- dg + gd = f′f around both triangles;
- fg + gf = id at all six vertices;
- **exactness of both triangles in homology** by rank counting: the ranks of (f₁, f₀, f₋₁) on homology are (8, 8, 8);
- the levels: a, a′, b, b′ < 0 strictly; c, c′ ≤ 3/16; g_A, g′_A < −1/8 strictly; vertex homotopies ≤ 1/16;
- degrees mod 4 equal to (1,1,1,3,1,3), with homotopy degrees deg f + deg f′ + 1;
- a free χ of degree 4 on A (mod 8), 0 on B (mod 8) and 0 on T (mod 4), preserving levels and commuting with d and with all twelve maps;
- b′a = 0 = ba′;
- Euler characteristic 0, dim H_j(A) = 2 for every j ∈ Z/8, and H(T) ≠ 0.

The output (COMPUTED): ℓ(A) = ℓ(B) = 0 on both sides, ℓ(T) = −1/32, ℓ⁺(T) = 1/32, and every drop is 0. The negative controls each raise errors:
- absorption cost 3/32 > 1/16;
- zero-energy absorption;
- a′ of degree 1;
- χ of degree 4 on B;
- a bar with c-rise 1/8;
- a deleted homotopy entry;
- b′a ≠ 0.

### 1.2 The no-go theorem, stated precisely

**Theorem 1 (PROVED, by explicit verified models).** Consider data over F₂ consisting of:
- 8-periodic Z-graded lifts A_± = C(Y_{±2}, P₀) and B_± = C(Y_{±2}, P₁), and a 4-periodic lift T, each filtered by CS̃ within each degree, with c = CS̃ − gr̃/8 on generators;
- chain maps and homotopies forming DLME triangle-detection data, with q = id and h = 0, for
  - (I) A₊ →a T →b B₋ →c A₊ and
  - (II) B₊ →a′ T →b′ A₋ →c′ B₊.

Impose:
- **(L)** every level of the ledger: a, a′, b, b′ ≤ −η with η > 0, so no flat contribution at all; c, c′ ≤ 3/16; g_A, g′_A ≤ −1/8 − η with η > 0; vertex homotopies ≤ 1/16; differentials of positive energy;
- **(G)** the degree table mod 4 and the homotopy degrees;
- **(χ)** free χ-involutions of degree 4/0/0, preserving levels and commuting with everything;
- **(S)** b′a = 0 = ba′;
- **(E)** Euler characteristic 0 on A, B and T; dim H_j(A) constant in j; H(T) ≠ 0;
- **(D)** the dual data for K̄, and odd automorphisms of A of degree −3 (level ≤ 1/8) and degree −1 (level < 1/8);
- **(U)** an upstairs lift satisfying DLME's levels;
- **(φ)** A₊ = A₋ and B₊ = B₋ as filtered graded complexes.

Then such data exist, both with zero and with nonzero differentials, and in them:
- λ_i(Y₂) = λ_i(Y₋₂) for i = 0, 1;
- m₁ = m₂ = 0;
- the both-bundle drops at the bottom and at the top are 0.

So no argument whose inputs are among the following can prove D_min > 0, D_max > 0, m₁ > 0, m₂ > 0 or m₁ + m₂ > 0:
- the triangles and the ledger;
- E ≥ 0, and E > 0 where no flat connection contributes;
- the gradings, χ, (S), (E), (D) and (U);
- filtered algebra with arbitrary differentials.

**What Theorem 1 does not cover.** These are the escape routes.
1. **The actual locations of the generators,** that is, the ρ-invariants of flat connections. In every model the levels are free parameters. In real Floer theory they are values of one function on one curve (§2.3). The cosmetic model of §1.1 cannot come from a steep character curve, by Lemma C below.
2. **Which generators survive in homology.** This is information about differentials that is not formal.
3. **Structure not listed:** the u-map, h-type invariants, and triangles through other slopes. §2.5 explains why the route through Y₀ is blocked.
4. **Energy estimates,** which rule (a) forbids.

### 1.3 Two technical confirmations

- **The c-level is not a filtration (PROVED).** This is the critic's point, and exact's Lemma 3.1 makes it independently. d raises c by 1/8 − E. Boundary depth must be measured in CS units within one degree, and a primitive of z has c ≤ c(z) + β − 1/8.
- **The counting lemma (cover Lemma 4.3) is correct for arbitrary differentials (PROVED; I re-derived it).**
  - Filter Cone(b) degree-wise by F_r = F_{r − D_b/8}M ⊕ F_rB. This is a filtered complex because L_b ≤ D_b/8.
  - An element m of M then sits in the cone at c-level c(m) − 1/8.
  - So Φ = (a, g_A) has c-level −1/8 − min(η_a, η_g).
  - Take U = ker(H(F_tA) → H(F_{t−μ₀}M)). Its image in H(A) has dimension at least N_A(t) − P_M(t − μ₀).
  - These classes lift to H(F_{t−1/8−μ₀}B), and Φ_* is injective. This gives N_B(t − 1/8 − μ₀) ≥ N_A(t) − P_M(t − μ₀). ∎
  - I reran `cover-code/capacity_all.py`: 80 cases, 0 violations, max (T₁ − Λ(Y₂)) = 1/32 (COMPUTED, identical to the stored output).

---

## 2. The candidate inputs

### 2.1 (a) The counting form of DLME's argument

**Lemma A (PROVED; the cover's Lemma 4.3 and Cor. 4.7).** Put T₁ = inf{t : N_A(t) > P̄_M(t)}. Then:
- Λ(Y₋₂) ≤ T₁ − 1/8 − μ₀, so drop ≥ 1/8 + μ₀ − (T₁ − Λ(Y₂));
- in a cosmetic pair, N_Y(t − 1/8 − μ₀) ≥ N_Y(t) − P_M(t − μ₀) for all t;
- for perfect complexes, s_{j+r} − s_j ≥ 1/8 + η_g whenever j + r ≤ rk.

**Missing input X (SPECULATIVE; not an energy estimate).** For Δ_K = 1 there is t < Λ(Y₂) + 1/8 (respectively + 1/16) with N_A(t) > P̄_M(t). This gives drop > 0 (respectively ≥ 1/16) with any differentials.

**Tests.**
- Cover (COMPUTED; rerun by me): T₁ − Λ ≤ 0.0294 on the 54 det-1 cases and ≤ 1/32 on 80 torus knots. The perfect form with k = rk a_* holds for 4₁ (T₁ = 19/80).
- **Two warnings.**
  1. **The plain form fails on 4₁.** There N_A(t) ≤ N_M(t) for every t, although the drop is 1/8 (cover §8). So Input X in plain form is not necessary, even for a knot with a closed character curve.
  2. **It is vacuous in the ±1/n analogue (PROVED; COMPUTED in `twostep.out`).** For the two-step triangle Y_{−1/n} → Y_{−1/(n+1)}^{⊕2} → Y_{−1/(n+2)}, DLME's injective map W_n of level −η gives s_j(Y_{−1/(n+1)}) ≤ s_j(Y_{−1/n}) termwise. Hence N_M ≥ 2N_A, and N_A − min(N_M, rk A) ≤ 0 at every level, so T₁ = ∞. Yet the two-step drop is at least 1/8 in all data. A principle that fails in the closest analogue where the answer is known cannot be the universal mechanism.

**How it might be proved.** It needs a lower bound on N_A(t), which counts homology classes of I(Y₂), not generators. No input on the table supplies one. The pillowcase supplies generator counts, and bounds P_M from above.

**Confidence.** That some form of Input X holds for every Δ_K = 1 knot: 35%. That it is provable with present tools: under 10%. **Role:** it is the correct Floer-level engine; it needs (c) as its spectral input, together with an additional statement about which generators survive in homology.

### 2.2 (b) χ-clustering and the spacing condition

**Proposition B1 (PROVED given the pillowcase CS formula CS(Y_N, x) ≡ 2∫α dβ + Nα²; COMPUTED in `chi_degree.out`).** χ sends (α, β) to (α + 1/2, β). Comparing paths from θ, through χθ, gives

  CS(χx) − CS(x) ≡ (Nα + β) + N/4 (mod 1).

- On P₀ we have Nα + β ∈ Z, so the shift is ±1/2: χ has degree 4 (mod 8).
- On P₁ we have Nα + β ∈ 1/2 + Z, so the shift is 0: χ has degree 0 (mod 8). The two twins on P₁ have the same CS̃ and the same gr̃.
- Computed: degree 4 on P₀ and 0 on P₁ in all 48 cases (12 torus knots, N = ±2, both bundles). This agrees with duality's test 2.

**Consequences.**
- **B2 (PROVED).** χ-twins give equal-level pairs in SU(2) counts, in different degrees for P₀ and in the same degree for P₁. The middle term doubles in the same way: k_{SU(2)} = 2r. So the spacing condition s_{j+r} − s_j > 1/8 is invariant under the doubling, and **χ alone can never contradict it.** With d ≠ 0, χ-freeness does not even force pairs in the spectrum. Example: C = D ⊗ F₂[u]/u², with D = ⟨x, y⟩ and d = u·d₁, d₁x = y, has homology ⟨ux, y⟩ at two unrelated levels.
- **B3 (PROVED).** r is even and r ≥ 2 when Δ_K = 1.
  - Euler characteristic: χ(T) = −σ/2 = 0, and χ has degree 0 mod 4 on T, so the χ-reduced complex D has χ(D) = 0 and rank H(D) is even.
  - Nonvanishing: H(T) ≠ 0 (Kronheimer–Mrowka, Daemi–Scaduto) gives H(D) ≠ 0, through 0 → D → T → D → 0.
- **B4 (PROVED; perfect complexes; under (H2) for the bundle of the lower bottom).** In a cosmetic pair, r ≥ 4.
  - Put F = φ_*⁻¹B. It is an automorphism of odd degree and of level < 1/8, because η_B > 0 on the simply connected W_B.
  - The classes x_{low}, x_{other} and F x_{low} are then three independent classes in [s₁, s₁ + 1/8): the window gives |λ₀ − λ₁| < 1/16.
  - So s₃ − s₁ < 1/8 + η_g, which excludes r = 2.
  - The map H has level 3/8, not 1/8, unless an unproved stretching statement holds. So it does not help.
- **B5 (PROVED; perfect complexes; cosmetic).** Let R be the χ-reduced rank of I(Y) over both bundles. Then R < r·(1 + 8(μ⁺ − μ)), where μ⁺ − μ is the spread of the traceless homology. This follows from iterating s_{1+mr} − s₁ > m/8 together with the two windows μ < s₁ and s_R < μ⁺.

**Tests (COMPUTED, `cluster.out`).** On every det-1 torus knot and mirror, the largest number of spectral values in a window of length 1/8 is at least 3.5r. So no computed Y_{±2} satisfies the spacing condition, as the cover already found. But r, R and the traceless spread are all unknown for Δ_K = 1 knots.

**Confidence that (b) yields a contradiction: under 3%.** It needs r = 2, which B4 already excludes under (H2), or an a-priori bound on R/r. I know no route to such a bound.

### 2.3 (c) The pillowcase: one function on one curve

**Input S2 (PLAUSIBLE, about 70%; VERIFIED for torus knots and 4₁ in pillowcase-final §2–3).** There is a function Φ on C with dΦ = 2δ dβ. Put F_± := Φ ± 2δ², so that dF_± = 2δ d(β ± 2α). A generator x ∈ C ∩ (L_{±2} ∪ L^w_{±2}) has

  c(Y_{±2}, x) = F_±(x) ± 1/16 − ι_{±2}(x)/8,  with ι ∈ {0, 1},

and ι_{±2}(x) = 0 whenever the slope s(x) = dβ/dα lies outside (−2, 0) (respectively (0, 2)). The traceless rule is c^tl(z) = Φ(z) + sgn(s(z))/16.
- **Independent check (COMPUTED, `steepmin.py`).** On every arc of 16 torus knots, the value Φ_k recovered from Y₂ and Y₋₂ generators in both bundles is the same exact rational. This checks the slope-independence of Φ across N = ±2 and across bundles.
- **Proof route.** A Kirk–Lesch splitting of η along ∂E_K, with the Maslov triple index giving ι, as in the su(2) version of BHKK; Kirk–Klassen for the CS part. Degenerate curves need holonomy perturbations and a limiting argument.

**Lemma C (steep-minimum and location lemma; PROVED as calculus, given S2).** Suppose Δ_K = 1 and C is a smooth closed immersed curve; this holds after small perturbation, because C̄ meets the reducible arc only at roots of Δ_K. Put Φ₀ = min_C Φ.

(i) **Critical points (PROVED).**
- The critical points of Φ|_C are exactly the traceless points and the horizontal tangencies (dβ = 0).
- At a traceless point Φ ≈ Φ(z) + sδ². So positive-slope traceless points are local minima and negative-slope ones local maxima.
- Hence Φ₀ is attained either at a positive-slope traceless point z₀ or at a horizontal tangency.

Assume further:
- **(H_st)** s ∉ (−2, 0) at every generator of Y₂;
- **(H_br)** Φ₀ is attained at a traceless point z₀, and the branch of C through z₀ is a graph over v = β − 2α on [v(z₀) − 1/4, v(z₀) + 1/4] (both bundles), or on [v(z₀) − 1/2, v(z₀) + 1/2] (one bundle), with slope ≥ s* > 2 there.

Then:

(ii) **Y₂.** Every generator of Y₂ in either bundle has c ≥ Φ₀ + 1/16. Hence G(Y₂) ≥ Φ₀ + 1/16, and Λ(Y₂) ≥ Φ₀ + 1/16 **for any differential**.

(iii) **Traceless.** Φ₀ − 1/16 ≤ min c^tl ≤ Φ₀ + 1/16. So the traceless bottom always lies at or below the generator bottom of Y₂: absorption is geometrically always available, which is why the triangles cannot decide.

(iv) **Y₋₂.** Some generator of Y₋₂ in the given bundle has c ≤ Φ₀ − 1/16 + Δv²/(s* − 2), with Δv = 1/4 for both bundles and Δv ≤ 1/2 for one bundle.

(v) **The drop.** The generator-level both-bundle drop G(Y₂) − G(Y₋₂) is at least 1/8 − 1/(16(s* − 2)). The single-bundle and mixed gaps are at least 1/8 − 1/(4(s* − 2)). So the drop is positive for s* > 5/2 and at least 1/16 for s* ≥ 3; in one bundle it is positive for s* > 4.

*Proof.*
- (i) dΦ/dt = 2δ β′(t).
- (ii) F₊ ≥ Φ ≥ Φ₀, and ι₂ = 0 by (H_st).
- (iii) Use c^tl = Φ ± 1/16 together with (i).
- (iv) Along the branch, dα = dv/(s − 2), so |δ| ≤ |v − v₀|/(s* − 2) and F₋ − Φ₀ = ∫2δ dv ≤ Δv²/(s* − 2). Points of Y₋₂ are spaced by 1/2 in v for both bundles and by 1 for a single bundle.
- (v) Subtract (iv) from (ii). ∎

**Use for the cosmetic problem (PROVED).** An orientation-preserving diffeomorphism Y₋₂ → Y₂ carries irreducible flat SO(3) connections to irreducible flat SO(3) connections. It preserves w₂, because H²(Y; Z/2) = Z/2, and it preserves ρ_ad. So the multisets of c-values agree bundle by bundle; in particular G(Y₂) = G(Y₋₂).

Hence (PROVED given S2): **if C satisfies (H_st) and (H_br) with s* > 5/2, then S³₂(K) ≇ S³₋₂(K).**
- No energy enters, not even E ≥ 0, and differentials play no role.
- The 1/16 enters as the offset (3 − |N|)/16 of Y_{±2} from Φ at the traceless holonomy, with |N| = 2: 3/16 from the signature, +2/16 from the solid-torus CS term, −4/16 from the spectral flow (pillowcase-final F.2).
- The gap is 2·(1/16), less a spacing error.

**Tests (COMPUTED).**

| data | script | result |
|---|---|---|
| 16 mirror torus knots, pq ≤ 56 | `steepmin.out` | Φ₀ is always attained at a traceless point. (ii) and (iv) hold; the both-bundle drop is at least the bound. For odd–odd knots the bound in (iv) is attained **exactly**, because z₀ sits at v ≡ ±1/4, midway between generators of Y₋₂ |
| the same, single bundle and mixed | `steepmin_bundles.out` | Every case satisfying (H_br) obeys the bound. The single exception, T̄(3,5) in P₁, is the one case where (H_br) fails: the arc through z₀ reaches its reducible endpoint, at distance 1/60 from z₀ in α, before the twisted generator, which needs 1/26. Arc ends are a Δ_K ≠ 1 feature |
| sharpness | same | For T̄(2,3), m₂ = 1/16 = 1/8 − 1/(4(6 − 2)) exactly. Several mixed gaps of T̄(2,q) equal the bound |
| 4₁ (closed curve, slopes at least 2√5) | `fig8_phi.out` | Φ has exactly one minimum, 11/80, at the positive-slope traceless passage (slope +4.472), and one maximum, 19/80, at the negative-slope passage. (ii): G(Y₂) = 1/5 = Φ₀ + 1/16. (iv): G(Y₋₂) = 3/40 ≤ 0.1003. The bound on the drop is 0.0997; the actual drop is 1/8 |
| positive torus knots | — | Lemma C does not apply: Φ is concave on arcs with reducible ends, so Φ₀ is at an end. These knots have drop > 1/8 by parity in any case |

**The Floer-level drop (what (c) does not give).** (ii) bounds Λ(Y₂) from below for any differential. An upper bound on Λ(Y₋₂) needs a nonzero class. The missing statement, (F), is: the lowest generator of Y₋₂ on the branch through z₀ represents a nonzero class at its own level, or some class of I(Y₋₂) lies below Φ₀ + 1/16. This is a statement about which generators survive in homology, not an energy estimate, but it is open.

A partial structural fact (PLAUSIBLE; it uses the grading formula i = 4(Nα + β) − (3/2)sgn N + ι + const_Γ of pillowcase-final E):
- On a component of C along which ι is constant, all generators of Y_N in both bundles have one grading parity.
- So d connects only different components, or generators across an ι-jump.
- Euler characteristic 0 (Δ_K = 1) then forces at least two parity classes of components.

**Where the real gap is (SPECULATIVE).**
- **Steepness for Δ_K = 1 knots.** The slope of C at x is minus the twisted framing of K at x (triangle-1 §3.2), and (H_st) says it has absolute value greater than 2. Nothing forces this for a general knot.
- **Horizontal tangencies.** If Φ₀ is attained at a horizontal tangency, nearby generators of Y₂ have ι₂ = 1 and can sit near Φ₀ − 1/16. The lemma then says nothing.
- **Steepness is self-consistent.** On a steep closed component ι ≡ 0. Consistency of the gradings mod 8 then forces even β-winding w and ∮2δ dβ = 0, so Φ is single-valued, as for 4₁ (w = 2).

**Confidence.**
- Lemma C given S2: 95%.
- S2 in general: 70%; the ι-rule: 55%.
- That the generator-level both-bundle drop is positive for every nontrivial Δ_K = 1 knot: about 55%.
- That steepness-type control can be proved for all Δ_K = 1 knots: about 15%.

### 2.4 (d) A flat contribution at the bottom of the traceless theory

**Lemma D (PROVED for perfect complexes, given (I) and (II)).** Suppose the following:
- the lowest class of I^tl(K) is a generator z with z(μ) traceless and z(λ) = −1;
- the slope at z is negative, so c^tl(z) = Φ(z) − 1/16 = c(Y₋₂, z);
- the flat singular connection on (X₋₂°, D_r) at z is regular of index 0.

Then b′ maps z to the generator z₋₂ with coefficient 1, and b′_*[z] ≠ 0. Hence λ₀(Y₋₂) ≤ μ.
- If the bottom of Y₂ is absorbed, then μ ≤ Λ(Y₂), with strict inequality unless a zero-energy absorption sits at another point at the same level. So the drop is positive.
- If the bottom of Y₂ is not absorbed, the kernel criterion gives drop ≥ 1/8 + η_g.

**With differentials.** Lemma D needs in addition that z₋₂ is not the leading term of a boundary. That is a statement about which generators survive.

**Tests.**
- The twisted analogue (λ ↦ +1, binary dihedral) is the 4₁ mechanism: duality test 9 gives D_min ≥ 1/40.
- For det > 1 mirrors, both bottoms sit at the same common point and the drop is exactly 1/8 (exact `samerep120`: 78 of 78 cases).
- For det-1 torus knots there are no λ ↦ −1 traceless points, because pq is odd. So Lemma D cannot be tested where it matters.

**Pillowcase reading.** Negative-slope traceless points are local maxima of Φ. Lemma D requires the bottom of T to sit at such a point, and in addition at β = 1/2, which is a codimension-one coincidence.

**Confidence that Lemma D applies to every Δ_K = 1 knot: under 5%.** Its value is as the exact endpoint of Lemma C: when z₀ is a common point, the generator-level drop is exactly 1/8, from a flat connection on the non-simply-connected E = W′∖νS, as rule (a) requires.

### 2.5 (e) Other inputs

1. **The ρ-spectrum as a diffeomorphism invariant (PROVED).** This is how (c) is best used (§2.3). It changes the target from λ_i to the generator-level G, which is enough for the cosmetic application. I flag it because rule (d) asks for a drop of λ_i.
2. **The route through Y₀ adds no level information (PLAUSIBLE; the key inequality is COMPUTED).**
   - The distance-two maps g₊: Y₂ → Y₀^w and g₋: Y₀^w → Y₋₂ (DLME Prop. 3.10, statements.tex Conj. B) have middle term C(S³)² = 0.
   - c-levels on I^w(Y₀) are defined only up to an absolute normalisation, which cancels in composites.
   - The data rule out any injective map Y₂ → Y₋₂ of level −1/4, between any pair of bundles: every same-bundle and mixed gap in the census is at most 3/16 for the mirror knots, while such a map would force a gap of at least 1/4. So the composite of the two distance-two maps cannot be a level −1/4 isomorphism. In statements.tex the identification ϑ at Y₀ carries the difference, and the composite is B, of level +1/8.
   - Composites through Y₀ are therefore families on W_B whose levels are already in the ledger (g_A at −1/8, B at +1/8). The single-twist factorisation L₋₂ = τ_V²(L₂) adds nothing.
3. **The ±1/n two-step as a test bed** (§4). Any candidate input should first prove ℓ(Y_{−1/n}) − ℓ(Y_{−1/(n+2)}) ≥ 1/8, where all the data are known. (a) fails this test (vacuous) and (b) is irrelevant. The pillowcase mechanism of (c) reproduces the exact equality cases.
4. **The u-map, h-invariants and the reducibles θ and χθ.** I found no mechanism by which these act on the bottom 1/8 of the spectrum (SPECULATIVE; I agree with the duality report).

### 2.6 Ranking

| rank | candidate | the precise non-energy statement | gives | proof status | confidence |
|---|---|---|---|---|---|
| 1 | (c) pillowcase | Lemma C, given S2 | G-drop ≥ 1/8 − 1/(16(s* − 2)) under (H_st) and (H_br); for λ, only Λ(Y₂) ≥ Φ₀ + 1/16 | lemma PROVED; S2 PLAUSIBLE; steepness open | 55% that the G-drop is positive for all Δ=1; 15% that it is provable |
| 2 | (a) counting | Input X | λ-drop ≥ 1/8 − (T₁ − Λ), any d | Lemma A PROVED; X open, false in plain form for 4₁, vacuous for ±1/n | 35% true; under 10% provable |
| 3 | (d) flat bottom | Lemma D | λ-drop > 0 in the perfect case; exact 1/8 at common points | PROVED conditionally | under 5% applicable |
| 4 | (b) χ-clustering | B1–B5 | r ≥ 4 and R < r(1 + 8(μ⁺ − μ)) | PROVED | under 3% |

---

## 3. The best combined strategy

1. **Floer layer (PROVED, given T).**
   - The vertex lemma and Lemma A, valid for any differentials.
   - In the cosmetic case, the windows μ < Λ ≤ max ≤ μ + 1/16, their mirror at the top, and the spacing and rank–spread conditions B4–B5.
2. **Spectral layer: the new input (c).**
   - Establish S2 in general: the Kirk–Lesch splitting of ρ_ad along ∂E_K, with the Maslov index ι. This is standard analysis; the remaining risks are the ι-rule and degenerate curves.
   - Then Lemma C locates all three spectra relative to one number Φ₀ = min_C Φ:
     - Y₂ lies at or above Φ₀ + 1/16;
     - T lies within ±1/16 of Φ₀;
     - Y₋₂ has a generator at or below Φ₀ − 1/16 + 1/(16(s* − 2)).
3. **Cosmetic conclusion, by invariance of the ρ-spectrum.** For Δ_K = 1 knots whose curve satisfies (H_st) and (H_br) with s* > 5/2, there is no ±2 cosmetic pair. This uses no energy and no differentials.
4. **The remaining gap.** Control the shallow parts of C: horizontal tangencies and slopes in (−2, 2). Either:
   - show that for Δ_K = 1 the minimum of Φ cannot sit at a horizontal tangency with a generator of Y₂ having ι = 1 below Φ₀ + 1/8; or
   - find a substitute for (H_st), for instance using the χ-symmetry of C under (α, β) ↦ (1/2 − α, −β), the Bohr–Sommerfeld condition ∮2α dβ ∈ Z, and the closedness of C.
5. **If the λ-drop itself is wanted.** Add statement (F) of §2.3. Lemma D supplies it at common points; the per-component parity of §2.3 may supply it when the bottom component of Y₋₂ is isolated in parity.
6. **Before investing in step 4.**
   - Compute C, Φ, the slopes, and G(Y_{±2}) numerically for an actual Δ_K = 1 knot: the (−3,5,7) pretzel, or untwisted Whitehead doubles. Genus 1 is enough to test the mechanism, which uses only Δ_K = 1. The 4₁ solver in `gap16/pillowcase-final-code/fig8_check.py` adapts directly to any two-bridge or pretzel presentation.
   - Check whether (H_st) and (H_br) hold, and where Φ₀ sits.

**Where 1/16 enters.**
- As the slope offset (3 − |N|)/16 at the traceless holonomy, which produces the gap 2·(1/16).
- In the threshold s* ≥ 3 for a drop of at least 1/16.
- In the mixed common-point gap 3/16 = 1/8 + 1/16, from γ₁ on L(4,1).
- As the width of the Floer windows (E_cap = 1/16).

It never enters as an energy floor.

---

## 4. What the ±1/n data teach

### 4.1 The two-step triangle meets the middle-term obstruction in its strongest form (PROVED; COMPUTED)

**The triangle.** The slopes −1/n and −1/(n+2) are at distance 2. The slopes at distance 1 from both are −1/(n+1) and 0.
- DLME's distance-two triangle for (Y_{−1/(n+1)}, dual knot) is C(Y_{−1/n}) → C(Y_{−1/(n+1)})^{⊕2} → C(Y_{−1/(n+2)}) → ⋯, with levels a ≤ 0, third map 1/4, and g₁ ≤ −1/8 − η.
- By DLME's n-surgery lemma it collapses to a short exact sequence, and its first map is injective (DLME, proof of Lemma `n-surgery-calc` and its footnote).
- So **every class of Y_{−1/n} is absorbed.** The kernel criterion never fires, and only the third map, which is zero on homology, could carry the 1/8.

**Counting.** W_n is injective of level −η, so s_j(Y_{−1/(n+1)}) ≤ s_j(Y_{−1/n}) termwise. This is COMPUTED for 10 knots in both chiralities with n ≤ 4 (`twostep.out` (C)). Hence N_M ≥ 2N_A, and Lemma A is vacuous.

**The no-go.** The same formal no-go applies (PLAUSIBLE: the models of §1 transcribe directly, and the data's one-step drops, as small as 0.030, show the formal structure allows small two-step drops). So the two-step bound **is not provable by the distance-two triangle with intermediate slope −1/(n+1)**. Its middle term is a closed 3-manifold theory that dominates the source termwise, which is worse than the ±2 case. Positivity of the two-step drop is free here (DLME's W_n), but the 1/8 is not.

### 4.2 The equality cases come from a flat SO(3) connection on X_n∖νS (PLAUSIBLE as bookkeeping; COMPUTED)

Let x be an irreducible SU(2) representation of π₁E_K with x(μ) and x(λ) both traceless; these lie at the pillowcase points (1/4, ±1/4). Let n be odd. Then:

1. **x is a generator.** The core of the −1/n filling is λ, modulo the surgery slope, and −α + nβ ∈ Z. So x is a generator of Y_{−1/n} when n ≡ 1 (mod 4), and χx is one when n ≡ 3 (mod 4). The two are swapped from n to n + 2.
2. **ad x descends.** The SO(3) representation ad x = ad(χx) kills γ_{−1/n} and γ_{−1/(n+2)}, so it descends to π₁(X_n∖νS) = π₁E_K/⟨⟨γ_{−1/n}, γ_{−1/(n+2)}⟩⟩.
3. **The RP³ end.** On ∂νS = RP³ it restricts to the rotation by π, because ad x(λ) is a rotation by π. This end has w₂ ≠ 0, h = 1 and ρ = 0, so its term is (3 − 1 + 0)/16 = 1/8.
4. **The level.** With index 0 and b⁺ = 0, the level formula gives c(Y_{−1/(n+2)}) = c(Y_{−1/n}) − 1/8 exactly.

**This corrects drops.md §4(c).** Its van Kampen argument excluded flat connections joining the minimisers by considering SU(2) representations only. There are no shared SU(2) irreducibles, since 2β ∈ Z forces reducibility. The shared SO(3) representations are the χ-pairs on β = ±1/4.

**Tests (COMPUTED, `twostep.out`).** For all 5 odd–odd torus knots tested, in **both** chiralities, at n = 1 and n = 3:
- the multiset of c-values of these shared representations shifts by exactly −1/8 from n to n + 2, at every shared representation and not only at the minimisers;
- for the mirrors, the minimisers at n and n + 2 are such shared representations, which gives T_n = 1/8 exactly;
- for positive odd–odd knots and for knots with p or q even, the minimisers are not shared and T_n > 1/8.

### 4.3 Lessons for ±2

1. **Exactness at shared points is the same mechanism in both problems.** Exact values arise only at representations shared as SO(3) connections, through a flat connection on a non-simply-connected exterior: X_n∖νS with an RP³ end for the two-step, and E = W′∖νS with an L(4,1) end for ±2 (1/8 for γ₀, 3/16 for γ₁). This is rule (a)'s mechanism, now verified in both settings.
2. **The two problems differ off the shared points.**
   - For ±1/n the drop at unshared minimisers exceeds the shared value: T_n > 1/8.
   - For ±2 it falls below: the det-1 mirrors have drop 1/8 − 1/(4(n² − 4)), because the minimiser z₀ sits midway between generators of Y₋₂. Lemma C (iv) computes this loss exactly as 1/(16(s − 2)) and other spacing terms.
   - So the right ±2 target is "> 0" or "≥ 1/16", not 1/8, and the loss is governed by the geometry of C, not by energy.
3. **The middle-term obstruction is real in both problems, and in the two-step problem the data show it is not fatal.** The bound holds even though the triangle with intermediate slope absorbs everything. So the decisive information lies outside the triangle in both problems: in the positions of the generators, that is, in Φ along C. This supports ranking (c) first.
4. **One-step drops have no positive lower bound** (min D₁⁻ = 7/232, and D₁⁺ → 0). They are pure Chern–Simons differences on simply connected negative-definite cobordisms, consistent with rule (a). Nothing in ±2 should be expected from a single handle.

---

## 5. Files (`r6/judge-code/`)

| file | content |
|---|---|
| `nogo_judge.py` / `.out` | independent zero-drop model with all constraints of Theorem 1; exactness by ranks |
| `nogo_controls.py` / `.out` | 7 negative controls, all detected |
| `chi_degree.py` / `.out` | χ-degrees on P₀ and P₁ for 12 torus knots, N = ±2: 4 and 0 mod 8 |
| `cluster.py` / `.out` | cluster numbers of the χ-reduced both-bundle spectra against r |
| `steepmin.py` / `.out` | Lemma C on 16 mirror torus knots: Φ₀, the bounds, both bundles; consistency of Φ across N and bundles |
| `steepmin_bundles.py` / `.out` | single-bundle and mixed versions, with the branch hypothesis checked |
| `fig8_phi.py` / `.out` | Φ along the closed 4₁ curve: its minimum and maximum, and Lemma C |
| `twostep.py` / `.out` | ±1/n: exact −1/8 shift at the shared SO(3) representations, shared minimisers, termwise domination and vacuous counting |
| `capacity_all.rerun` | rerun of the cover's counting test (identical) |
