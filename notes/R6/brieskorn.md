# ℓ along the 1/n surgeries on an exceptional fibre of a Brieskorn sphere

**Normalisation** (BRIEF.md):
- c(α) = CS~ − gr~/8 = (3 + ρ(α))/16.
- ℓ is the least c of a nonzero homology class.
- On every Brieskorn sphere all generators have one grading parity. I checked this on every manifold with a ≤ 420; on the link orientation the gradings are odd in DLME's convention. So d = 0 and ℓ = min c.
- ℓ(S³) = +∞, since S³ has no irreducibles.

**Labels:**
- **DERIVED**: topology worked out by hand, then checked numerically.
- **COMPUTED**: exact rational arithmetic, cross-checked by an independent formula.
- **CONJECTURE**: holds in all data, not proved.

**Code and tables** are in `r6/brieskorn-code/`; see §9.

---

## 0. Answers in brief

Let Σ = Σ(a₁,a₂,a₃) carry its **link orientation** (the boundary of the negative-definite plumbing). Let K be the exceptional fibre of order a_K, and P = a₁a₂a₃/a_K, the product of the other two orders.

| | **Σ link-oriented** (the user's question) | −Σ, a_K < P | −Σ, a_K > P |
|---|---|---|---|
| Y_{−1/n} | Σ(…, a_K + nP, …) | Σ(…, nP − a_K, …) | −Σ(…, a_K − nP, …) while nP < a_K |
| (a) ℓ(Y_{−1}) > ℓ(Y_{−1/2}) > ℓ(Y_{−1/3}) | **always** (in fact strictly decreasing up to n = 6) | **always** | **fails** in 410 of 424 families with 2P < a_K < 4P; holds otherwise |
| (b) T₁ := ℓ(Y_{−1}) − ℓ(Y_{−1/3}) ≥ 1/8 | **always** | **always** | holds iff a_K < 3P |
| (c) sharp lower bound | **1/8, attained** | **1/8, attained** | none: 0 < T₁ < 1/8 with T₁ → 0 for a_K > 4P, and T₁ down to −9/8 |

The two left-hand columns are the analogues of positive and of mirror torus knots: T(p,q) ⊂ S³ = Σ(p,q,1), and mT(p,q) ⊂ S³ = −Σ(p,q,1).

**Exact two-step formula (CONJECTURE).** Whenever Y_{−1/n} and Y_{−1/(n+2)} are both link-oriented,

  **ℓ(Y_{−1/n}) − ℓ(Y_{−1/(n+2)}) = 1/8 + β_n² / (8 m_n m_{n+2}).**

Here:
- m_n is the order of the surgered fibre in Y_{−1/n};
- β_n ∈ ℤ≥0 depends only on the exterior of K and the parity of n.

This holds exactly in 80,894 of 80,895 link-oriented windows. The single exception is explained in §5.1, and T > 1/8 there too.

So T₁ ≥ 1/8, and **T₁ = 1/8 ⇔ β = 0 ⇔ the ℓ-minimisers of Y_{−1/n} and Y_{−1/(n+2)} have traceless holonomy along the surgered fibre**, as for torus knots. This holds in all 5067 equality windows and none of the 75,828 others.

**Equality needs:**
- both other orders odd;
- m_n even;
- (m_n mod 2P) = r < P with r in a set R(a_j, a_k). The set R always contains 2 and P − 1; the case r = P − 1 is the odd–odd mirror torus knots.

**Non-torus equality examples:**
- K = order-17 fibre of Σ(3,5,17): ℓ(Σ(3,5,32)) − ℓ(Σ(3,5,62)) = −41/120 + 7/15 = 1/8.
- K = order-13 fibre of −Σ(3,5,13): ℓ(Σ(2,3,5)) − ℓ(Σ(3,5,32)) = −13/60 + 41/120 = 1/8.

**One-step drops (CONJECTURE).** In every link-oriented window,

  ℓ(Y_{−1/n}) − ℓ(Y_{−1/(n+1)}) ≥ m_n / (16 m_{n+1}),

with equality iff β_n = 0 (102,071 windows, 5784 equalities). Consequences:
- **for link-oriented Σ every one-step drop exceeds 1/24** (sharp). The observed minimum is 625/14998, for K = 2 ⊂ Σ(2,17,147) at n = 2.
- for −Σ with a_K < P the drop D₁ can be as small as 1/(8(P+2)); the smallest observed is 1/568 at Y_{−1} = Σ(2,3,23). So there is no uniform positive one-step bound.

---

## 1. Topology (DERIVED; checked on every manifold)

### 1.1 Set-up

- Σ = Σ(a₁,a₂,a₃) carries its link orientation.
- K = K_i is the fibre of order a_i.
- P = a/a_i, with a = a₁a₂a₃.
- The exterior X = Σ ∖ νK is Seifert fibred over D²(a_j, a_k), with H₁(X) = ℤ.

On ∂X take the basis q (boundary of a section) and h (fibre). Write the unnormalised Seifert invariants as (a_l, b_l). Fix the sign convention so that Σ_l b_l/a_l = +1/a is the link orientation.

**Meridian and longitude.** The meridian is μ = a_i q + b_i h. In H₁(X; ℚ) we have q = (D/P)h, where D = b_j a_k + a_j b_k. So the Seifert longitude is λ₀ = P q − D h, and μ·λ₀ = −(P b_i + D a_i) = −1.

**The fillings.** Filling along μ + kλ₀ = (a_i + kP) q + (b_i − kD) h gives
- |H₁| = |P(b_i − kD) + D(a_i + kP)| = 1 for every k ∈ ℤ, and these are all the homology-sphere fillings;
- Σ b/a = 1/(P(a_i + kP)), so the result is sgn(a_i + kP)·Σ(…, |a_i + kP|, …).

μ + kλ₀ is the slope 1/(σk), where σ = ±1 is universal.

**Calibration of σ.** In S³ = Σ(2,3,1), the order-1 "fibre" is a regular fibre. It is a generic orbit of (x,y) ↦ (t³x, t²y) on S³ ⊂ ℂ², an algebraic knot and hence the right-handed trefoil. S³_{−1/n}(RHT) = Σ(2,3,6n+1) forces k = n ↔ slope −1/n. This is the user's convention: −1 surgery is the negative-definite 2-handle.

**Result:**

  Σ_{−1/n}(K_i) = Σ(…, a_i + nP, …)  (link orientation)
  Σ_{+1/n}(K_i) = sgn(a_i − nP) · Σ(…, |a_i − nP|, …)
  (−Σ)_r(K_i) = −(Σ_{−r}(K_i))

### 1.2 Checks

- **Alexander polynomial.** Δ_K = Δ_{T(a_j,a_k)}. The fibre degrees in H₁(X) are P, a_k and a_j (Milnor/Eisenbud–Neumann formula). So Casson predicts

  λ(Σ_{1/m}(K)) = λ(Σ) + m (a_j² − 1)(a_k² − 1)/24, with λ(±Σ(A)) = ∓#R*(A)/2.

  This holds exactly for every manifold computed: all 21,768 families, both orientations, m = −6, …, 3, and along all 3300 chains. It is an independent check of the sign of the slope, because the m-term changes sign with it.
- **Signature count.** #R*(A) from the representation count agrees with Brieskorn's signature count (−σ/4) for every manifold.
- **Torus knots.** Taking the regular fibre of ±Σ(p,q,1) reproduces all 140 torus-knot entries of drops.md §2 exactly.

### 1.3 Chains

Fix the exterior X(a_j, a_k; r), with r = a_i mod P. Its homology-sphere fillings form the chain

  Z_k = sgn(r + kP) · Σ(a_j, a_k, |r + kP|),  with Z_{k+n} = (Z_k)_{−1/n}(K).

- Z_k is link-oriented for k ≥ 0 and reversed for k ≤ −1.
- r = 1 gives Z₀ = S³ (the knot is T(a_j,a_k)); r = P − 1 gives Z₋₁ = −S³ (the knot is mT(a_j,a_k)). These are exactly the torus-knot exteriors.
- The mirror exterior is X(a_j, a_k; P − r), with Z′_k = −Z_{−1−k}.

**Kinds of family.** Each family (±Σ, K) is a window of a chain, of one of three kinds:

| kind | base | Y_{−1/n} |
|---|---|---|
| **L+** | +Σ = Z_k with k ≥ 0 | Z_{k+n}, all link-oriented |
| **L−** | −Σ with a_K < P, i.e. the base is Z′₋₁ | Z′_{n−1}, all link-oriented |
| **R−** | −Σ with a_K > P, i.e. the base is Z′_k with k ≤ −2 | the first members are reversed |

## 2. Computation (COMPUTED)

### 2.1 Library `bk.py`

**Representations.** Irreducibles of Σ(A) correspond to tuples (ε, l₁, l₂, l₃) in the Fintushel–Stern presentation, subject to:
- the parity conditions (−1)^{l_i} = ε^{b_i};
- the strict spherical triangle inequality.

**Levels.** The level is computed from the APS rotation-number formula

  c = ¼ Σ_i T(a_i, −b_i, l_i),

which is `check-code/fs.py`'s `c_APS`. Each T is evaluated as an exact integer sawtooth (Dedekind-type) sum. The evaluation is vectorised, using an FFT above m = 3000; the FFT values are rounded, required to round cleanly, and spot-checked exactly. The formula is separable, so the extreme values of c are exact range-minima over the triangle region. The value 8a·c is an integer, and this is asserted.

**Independent check on every minimiser.** For each minimiser:
- the Fintushel–Stern integer e is computed by CRT;
- CS = e²/(4a);
- c is recomputed as −Σ_FS(e)/8, which is a different Dedekind sum (different b, different l);
- the two values of c must agree, and 8(CS − c) must be an integer of the right parity.

**Other orientation.** On −Σ: c ↦ 3/8 − c, CS ↦ −CS, gr ↦ −3 − gr.

### 2.2 Validation (`validate.out`)

- **DLME's example.** Σ(2,3,5): (CS, gr, c) = (1/120, 1, −7/60) and (49/120, 5, −13/60).
- **Σ(2,3,7).** (25/168, 7, 23/84) and (121/168, 3, 29/84).
- **Torus knots.** All 140 torus-knot values of drops.md (independently re-checked in drops-check.md) are reproduced.
- **Full multisets.** The full c-multisets agree:
  - with `check-code/fs.py`, for all 113 pairwise-coprime Σ(A) with a ≤ 420 (2030 generators), also under a permuted fibre order;
  - with `drops-code/brieskorn.py` (mpmath cot sums with Seifert invariants), for 6 of the user's spheres in both orientations.
- **Re-run of existing code.** `r6/drops-code/validate.py` and `r6/check-code/validate.py` were re-run and pass.

## 3. Range covered

**(F) Families.** Base ±Σ(a₁,a₂,a₃), each of the three fibres, both orientations. Each family records ℓ of Σ, of Y_{−1/n} for n = 1, …, 6, and of Y_{+1/n} for n = 1, 2, 3.
- **Non-torus bases:** all 3122 pairwise-coprime triples 2 ≤ a₁ < a₂ < a₃ with a ≤ 5000 and no a_k ≡ ±1 (mod a_i a_j). This includes the 279 triples with a ≤ 1000. That is 18,732 families; the largest P is 2499.
- **Torus-knot bases:** 466 triples with a ≤ 3000, plus K = T(p,q) ⊂ S³ = ±Σ(p,q,1) for pq ≤ 160. That is 3036 families; the 197 in which some Y is S³ are excluded.

**(C) Chains.** All 3300 exteriors X(a_j, a_k; r) with P ≤ 120 (106 of them torus-knot exteriors), with members Z_k for −6 ≤ k ≤ 10. In addition, 77 sampled chains up to k = 40.

## 4. Answers to (a), (b), (c)

T₁ = ℓ(Y_{−1}) − ℓ(Y_{−1/3}). D₁ = ℓ(Y_{−1}) − ℓ(Y_{−1/2}) and D₂ = ℓ(Y_{−1/2}) − ℓ(Y_{−1/3}) are the one-step drops.

### 4.1 Non-torus-knot bases (a ≤ 5000; 18,732 families)

| kind | # | (a) holds | min T₁ | # T₁ = 1/8 | # T₁ < 1/8 | min D₁ | min D₂ |
|---|---|---|---|---|---|---|---|
| L+ (+Σ) | 9366 | **9366** | **1/8** | 77 | 0 | 35/836 ≈ 0.0419 [K=71 ⊂ Σ(3,23,71)] | 625/14998 ≈ 0.04167 [K=2 ⊂ Σ(2,17,147)] |
| L− (−Σ, a_K<P) | 7739 | **7739** | **1/8** | 539 | 0 | 1/568 ≈ 0.0018 [K=67 ⊂ −Σ(3,23,67)] | 10201/151604 ≈ 0.067 [K=49 ⊂ −Σ(4,25,49)] |
| R− (−Σ, a_K>P) | 1627 | 1217 | −9/8 | 0 | 864 | −1.393 | −1.155 |

On the subset a ≤ 1000 (1674 families): min D₁ for L+ is 11/260 (K = 23 ⊂ Σ(3,7,23)), and there are 5 L+ and 51 L− equality cases.

**L+ equality cases (77).** They come in arithmetic progressions a_K ≡ r + P (mod 2P):
- K = 17, 47, 77, … ⊂ Σ(3,5,a_K);
- K = 23, 25, 31, 65, 67, 73, … ⊂ Σ(3,7,a_K);
- and others (list: `detail.out`).

In each case Y_{−1} = Σ(…, a_K + P, …) with a_K + P ≡ r (mod 2P), r ∈ R.

**L− equality cases (539).** For example:
- −Σ(3,5,13) with K = 3, 5 and 13 (Y_{−1} = Σ(62,5,13), Σ(3,34,13) and Σ(3,5,2) = Σ(2,3,5));
- −Σ(3,7,19) with K = 19 (Y_{−1} = Σ(2,3,7)).

**R− in detail** (the bands are exact in the data):

| band | (a) | T₁ |
|---|---|---|
| P < a_K < 2P | holds (504/504) | ≥ 1/8 |
| 2P < a_K < 3P | fails 250/259 | ≥ 1/8 |
| 3P < a_K < 4P | fails 160/165 | < 1/8 (≤ 0 in 157) |
| a_K > 4P | holds (699/699) | 0 < T₁ < 1/8 |

- **First failure of (a).** K = 23 ⊂ −Σ(2,5,23). Then Y_{−1} = −Σ(2,5,13), Y_{−1/2} = −Σ(2,3,5) and Y_{−1/3} = Σ(2,5,7), with ℓ = 209/520 < 59/120 > 11/70.
- **Most negative T₁ = −9/8.** K = 119 ⊂ −Σ(3,13,119). Then Y_{−1}, Y_{−1/2}, Y_{−1/3} = −Σ(3,13,80), −Σ(3,13,41), −Σ(2,3,13).
- **The user's eight examples** never fall in the failing bands, so (a) and (b) hold for all 48 of their families (§8).

### 4.2 Torus-knot bases (a ≤ 3000 plus S³; 2839 usable families)

| kind | # | (a) | min T₁ | # T₁ = 1/8 | min D₁ | min D₂ |
|---|---|---|---|---|---|---|
| L+ | 1518 | all | 1/8 | 11 | 784/17767 ≈ 0.0441 | 749/17972 ≈ 0.04168 |
| L− | 1052 | all | 1/8 | 41 | 4489/150556 ≈ 0.0298 | 737/9180 ≈ 0.0803 |
| R− | 269 | all | 1/470378 (→ 0) | 0 | → 0 | → 0 |

- **Torus-knot R−.** Here the K are duals of torus knots in S³_{1/k}(T); for example −Σ(2,3,161) = S³_{1/27}(T(2,3)). There is no jump, so (a) holds, but T₁ → 0 as on the positive side of torus knots.
- **Equality cases.**
  - 44 of the 52 equality cases are in torus exteriors (11 L+, 33 L−). They are the odd–odd mirror torus knots and their chain-mates, such as K = 29 ⊂ Σ(3,5,29), K = 59 ⊂ Σ(3,5,59) and K = 41 ⊂ Σ(3,7,41).
  - The other 8 are non-torus exteriors (other fibres) inside torus-knot bases.
- **Same answers by exterior.** Classifying by exterior instead of by base gives the same answers (`detail.out`).

### 4.3 Chains (all 3300 exteriors with P ≤ 120)

**Windows inside the link-oriented part.** These are windows (Z_j, Z_{j+1}, Z_{j+2}) with j ≥ 0.
- Non-torus exteriors: 27,810 windows. (a) holds in all, T ≥ 1/8 in all, and T = 1/8 in 945.
- Torus exteriors: 1785 windows. (a) holds in all, T ≥ 1/8 in all, and T = 1/8 in 135.

**Monotonicity.** ℓ(Z_k) > ℓ(Z_{k+1}) at every step except Z₋₂ → Z₋₁. That step goes **up** in 3032 of the 3090 non-torus chains.
- Z₋₁ = −Σ(a_j, a_k, P − r) occupies the slot of S³ (where ℓ = ∞) in a torus chain.
- This single step is the only source of failures of (a). It also explains why ℓ(Y_{+1}) < ℓ(Σ) for L− bases (8642 of 8671).

**Crossing windows** (Z₋₁, Z₁) and (Z₋₂, Z₀): T > 1/8 always, with minimum ≈ 0.131. For torus chains these include DLME's ℓ(S³₁) − ℓ(S³₋₁) > 1/8.

**Purely reversed windows:** 0 < T < 1/8, except at the jump. The most negative T is −29/8, at (−Σ(7,17,240), −Σ(7,17,121), −Σ(7,17,2)).

## 5. Closed forms

### 5.1 Link-oriented members (CONJECTURE, exact in all data except one documented case)

For each chain X(a_j, a_k; r), with m_j = r + jP:

  **ℓ(Z_j) = A − j/16 + β_{j mod 2}² / (16 P m_j)**,  where A ∈ ℚ and β₀, β₁ ∈ ℤ≥0.

Equivalently, ℓ(Σ(a_j, a_k, m)) = A* − (m² − β²)/(16Pm), with A* = A + r/(16P) and β = β₀ or β₁ according to the class of m (mod 2P).

**Evidence:**
- **Chains.** Exact for every j ≥ 0 in all 3300 chains with P ≤ 120 (parameters fitted on two points per class), and exact up to j = 40 in 77 sampled chains (fitted on j ≤ 3).
- **Families** (P up to 2499):
  - (T − 1/8)·8 m m″ is a perfect square in 80,894 of 80,895 link-oriented windows (n = 1, …, 4);
  - the predicted one-step drops agree exactly in all 60,290 testable cases.
- **The one exception.** Chain (3,77; 211), i.e. K = 20 ⊂ −Σ(3,20,77), at Y_{−1/2} = Σ(3,442,77). There a tied pair from another generator family undercuts the β-family at the first member of its class. The form holds from the next member on (β₁ = 226, β₀ = 5, β₀ + β₁ = P), and T = 76761/544544 ≈ 0.141 > 1/8.

**Properties of the parameters:**
- A is the same on both classes (3300/3300 chains).
- 0 ≤ β ≤ P.
- β on the class of r is at most β on the other class (3300/3300).
- β₀ + β₁ = P in 3252/3300 chains, and in 27,855 of 27,930 consecutive pairs of the family data. The exceptions are competing families.
- **β = 0 ⇔ traceless minimisers at the surgered fibre** (every class, every window).
- β = 0 occurs only for P odd, on the class m ≡ r (mod 2P) with r even (216 of 652 such chains with P ≤ 120). It occurs:
  - always for r = 2 (27/27);
  - always for r = P − 1 (27/27, the odd–odd mirror torus knots).
- Other residues in R(a_j, a_k):

| (a_j, a_k) | R |
|---|---|
| (3,5) | {2, 14} |
| (3,7) | {2, 4, 10, 20} |
| (5,7) | {2, 8, 24, 26, 34} |
| (3,11) | {2, 4, 8, 14, 16, 32} |
| (3,13) | {2, 16, 34, 38} |
| (5,9) | {2, 4, 14, 22, 32, 44} |

  I found no arithmetic rule for R beyond "the minimiser of Σ(a_j, a_k, r) is traceless at its order-r fibre" (`betalist.out`).

**Consequences:**
- **Two-step drop:** T(j) = 1/8 + β²/(8 m_j m_{j+2}). In the user's notation, for +Σ:

  **T₁ = 1/8 + β²/(8(a_K + P)(a_K + 3P))**,

  and for −Σ with a_K < P, replace a_K by −a_K.
- **One-step drop:** D(j) = 1/16 + (β_j²/m_j − β_{j+1}²/m_{j+1})/(16P). Since β ≤ P, D(j) ≥ m_j/(16 m_{j+1}), with equality iff β_j = 0 and β_{j+1} = P.
  - For +Σ, j ≥ 1. On the class not containing r, β_j ≥ β_{j+1}, so D > 1/16. On the class of r, j ≥ 2, so D ≥ (r + 2P)/(16(r + 3P)) > 1/24.
  - Hence **D > 1/24 for every +Σ** (all 54,420 L+ one-step windows). The bound is approached by K = 2 ⊂ Σ(2,p,q) at n = 2.
  - For −Σ with a_K < P, r = 2 at j = 0 gives D₁ = 1/(8(P+2)) → 0.

**Traceless families** (drop exactly 1/8 per two steps):
- ℓ(Σ(p, q, 2 + 2jpq)) = ℓ(Σ(2, p, q)) − j/8 for all odd coprime p, q and j ≥ 0;
- ℓ(Σ(p, q, (2j+1)pq − 1)) = ℓ(Σ(p, q, pq − 1)) − j/8 (odd–odd mirror torus knots).

**Positive torus knots (new; exact for all 105 chains with r = 1, P ≤ 120):**

  ℓ(S³_{−1/n}(T(p,q))) = 3/8 − 5/(16pq) − n/16 + β_n²/(16pq(pqn+1)),  with β_n = 3 (n even) and β_n = pq − 3 (n odd).

For example, T(2,3) with n = 1 gives 23/84, and with n = 2 gives 8/39. Hence T_n = 1/8 + β_n²/(8(pqn+1)(pq(n+2)+1)) > 1/8.

**Mirror torus knots.**
- β = 0 (pq odd) or β = 1 (pq even) for n odd.
- β = P (pq odd) or β = P − 1 (pq even) for n even.
- So the bound D_n ≥ m_n/(16 m_{n+1}) is attained in the odd–odd case. For example, mT(3,5) at n = 1 gives 14/(16·29) = 7/232, which is drops.md's minimum.

### 5.2 Reversed members (k ≤ −2)

- ℓ(Z_k) = A′ − γ²/(4P m_k), with m_k = |r + kP|, on 3228 of 3300 classes.
- The torus case is ℓ(S³_{1/n}(T)) = 1/2 − 1/(4pq(pqn−1)).
- So on the reversed side T = γ²/(2 m m″): there is **no 1/8 term**, and T → 0.

## 6. Generators, equality and traceless holonomy

**Which generators realise ℓ.** On each parity class of a chain, the minimiser is one family of generators (occasionally two tied ones). Along the class:
- its grading rises by 2 (mod 8) every two steps, as in DLME's I(Y_{−1/n}) ≅ ⊕ I_{*−2i}(Y_{−1});
- it typically keeps its rotation numbers at the two unchanged fibres. The labels depend on the presentation, so this is not always literally so.

**Generator level (COMPUTED).** In 60/60 small transitions Z_j → Z_{j+2} (`matching.out`), and in two large ones including the exceptional chain (3,77; 211) with 7562 generators (`matching_big.out`), there is an injection φ: gens(Z_j) → gens(Z_{j+2}) with

  c(φα) = c(α) − 1/8 − β(α)²/(8 m_j m_{j+2}),  β(α) ∈ ℤ≥0.

In the small cases φ also satisfies gr(φα) = gr(α) + 2. So **T ≥ 1/8 holds generator by generator**, and it is sharp exactly for generators that are traceless along the surgered fibre.

**Equality ⇔ traceless (COMPUTED).** In every link-oriented window, T = 1/8 iff the minimisers at both ends have l_K = m/2. That is, the holonomy along the surgered fibre (the dual knot) is traceless, i.e. rotation by π in SO(3). This holds in 5067 equality windows and in none of the 75,828 others.
- Traceless holonomy requires m even, hence P odd.
- This is the same mechanism as for odd–odd mirror torus knots, and it matches drops.md's ℝP³ bookkeeping: the −2-sphere in the two-step cobordism and the rotation-by-π flat connection with (3 − h + ρ)/16 = 1/8.

## 7. Patterns and conjectures (stated precisely)

**Conjecture 1 (two-step bound).** Let K be an exceptional fibre of a Seifert fibred homology sphere Σ with three exceptional fibres, and let Y_{−1/(n+2)} = Σ_{−1/(n+2)}(K) be link-oriented. This is automatic for all n ≥ 1 when Σ is link-oriented, or when Σ is reversed with a_K < P. Then

  ℓ(Y_{−1/n}) − ℓ(Y_{−1/(n+2)}) ≥ 1/8,

with equality iff the minimisers are traceless along the surgered fibre. If Y_{−1/n} is link-oriented too, the defect is β²/(8 m_n m_{n+2}) with β ∈ ℤ≥0, eventually constant on the parity class of n. Equality requires all of:
- P odd;
- m_n even;
- m_n mod 2P = r < P with r ∈ R(a_j, a_k), where 2 and P − 1 always lie in R.

Once equality holds it persists for n + 2, n + 4, ….

**Conjecture 2 (one-step bound).** In link-oriented windows, ℓ(Y_{−1/n}) − ℓ(Y_{−1/(n+1)}) ≥ m_n/(16 m_{n+1}), with equality iff β_n = 0. In particular:
- (a) holds on the link-oriented side;
- D > 1/24 when Σ is link-oriented;
- the infimum is 0 in general.

**Conjecture 3 (exact form).** On the link-oriented side, ℓ(Σ(a_j, a_k, m)) = A* − (m² − β²)/(16Pm) on each class of m (mod 2P), eventually in m. For T(p,q): A* = 3/8 − 1/(4pq), and β ∈ {3, pq − 3}. A proof should follow from Dedekind/Rademacher reciprocity in the separable level formula, because the third rotation sum is the only term that varies along a chain.

**Reversed side.** (a) and (b) are not structural there. On the reversed side T has no 1/8 term. Monotonicity fails only at the single step into Z₋₁, the "S³ slot" of a non-torus chain.

## 8. The user's examples (+Σ, link orientation; full rows with all ℓ-values in `brieskorn-code/examples.md`)

| base | K | T₁ | β | D₁ | D₂ |
|---|---|---|---|---|---|
| Σ(2,5,7) | 2 / 5 / 7 | 0.1637 / 0.1419 / 0.1347 | 35 / 11 / 7 | 0.1216 / 0.0908 / 0.0803 | 0.0421 / 0.0511 / 0.0545 |
| Σ(3,4,5) | 3 / 4 / 5 | 0.1561 / 0.1477 / 0.1467 | 19 / 13 / 11 | 0.1115 / 0.0991 / 0.0994 | 0.0447 / 0.0486 / 0.0473 |
| Σ(2,5,13) | 2 / 5 / 13 | 0.1650 / 0.1554 / 0.1251 | 65 / 25 / 1 | 0.1231 / 0.1109 / 0.0474 | 0.0419 / 0.0444 / 0.0777 |
| Σ(3,5,7) | 3 / 5 / 7 | 0.1602 / 0.1533 / 0.1464 | 34 / 20 / 14 | 0.1168 / 0.1082 / 0.0995 | 0.0434 / 0.0451 / 0.0469 |
| Σ(2,7,9) | 2 / 7 / 9 | 0.1650 / 0.1434 / 0.1336 | 63 / 15 / 9 | 0.1231 / 0.0930 / 0.0752 | 0.0419 / 0.0504 / 0.0584 |
| Σ(3,4,7) | 3 / 4 / 7 | 0.1588 / 0.1579 / 0.1325 | 27 / 21 / 7 | 0.1150 / 0.1150 / 0.0717 | 0.0438 / 0.0429 / 0.0608 |
| Σ(2,5,17) | 2 / 5 / 17 | 0.1654 / 0.1538 / 0.1251 | 85 / 31 / 1 | 0.1236 / 0.1076 / 0.0545 | 0.0418 / 0.0462 / 0.0706 |
| Σ(4,5,7) | 4 / 5 / 7 | 0.1570 / 0.1560 / 0.1405 | 33 / 27 / 15 | 0.1123 / 0.1118 / 0.0869 | 0.0448 / 0.0443 / 0.0537 |

**Sample values for Σ(2,5,7):**
- ℓ(Σ(2,5,7)) = 11/70.
- For K = 7: ℓ(Y_{−1}), …, ℓ(Y_{−1/4}) = 19/170, 17/540, −17/740, −22/235.
- For K = 7: ℓ(Y_{+1}), ℓ(Y_{+1/2}), ℓ(Y_{+1/3}) = 59/120, 209/520, 389/920. Here Y_{+1} = −Σ(2,5,3) is the reversed Poincaré sphere.

**Torus-knot bases.** Σ(2,3,5) has T₁ = 128/799 ≈ 0.1602, 85/572 ≈ 0.1486 and 139/1012 ≈ 0.1374 for K = 2, 3 and 5.

**Context: ℓ(Y_{+1/n}) − ℓ(Y_{−1/n})** (DLME's comparison):
- For L±: > 1/8 for n = 1, 2, 3, except = 1/8 for n = 1 in 88 L+ families. These are traceless windows, all three members link-oriented, for example K = 17 ⊂ Σ(3,5,17), where Y_{+1} = Σ(2,3,5).
- For R−: mostly < 1/8, and negative near the jump.

**Context: where ℓ(Σ) sits.**
- ℓ(Σ) > ℓ(Y_{−1}) in every L± family.
- ℓ(Y_{+1}) > ℓ(Σ) in every L+ family, but not for L−, because of the jump.

## 9. Files (`r6/brieskorn-code/`)

**Code:**
- `bk.py`: the library.
- `validate.py`: validation, output in `validate.out`.
- `scan.py`: family scans, output in `nt1000.json`, `nt5000.json` (with `scan_nt5000.log`), `tk1000.json`, `tk3000.json`.
- `ray.py`, `rayan.py`: chains, output in `rays120.json` and `rayan.out`.
- Closed forms: `closedform.py`, `closedform2.py`, `betacheck.py`, `checks2.py`, `betalist.py`, `longchain.py`, `mixedwin.py`, `onestep.py`, each with its `.out`.
- `matching.py`, `matching_big.py`: generator-level injections.
- `detail.py`, `famcheck.py`, `classify.py`, `verify_claims.py`: answers by kind, with outputs `detail.out`, `famcheck_*.out`, `classify_*.out` and `verify_claims.out`.

**Tables:**
- `examples.md`: the user's examples and torus-knot bases, all ℓ-values.
- `all_nontorus_a5000.txt`, `all_torus_a3000.txt`: one line per family.

**Reproduction:** `run_all.sh` regenerates everything (about 45 minutes).

## 10. Confidence

- **Topology (convention, orientation, slope sign): high.** Derivation, S³ calibration, Casson's formula on every manifold computed (21,768 families × 9 surgeries, plus all chain steps), and the 140-entry torus table.
- **Values of ℓ: high.** Two independent formulas on every minimiser, agreement of full multisets with two earlier independent codes, and exact integrality checks.
- **Answers (a)–(c) on the data: high.**
- **Conjectures 1–3 as theorems: moderate to good.**
  - The closed form is exact far beyond the fitting data, and the bound holds generator by generator.
  - No proof is given.
  - The equality set R(a_j, a_k) is only described empirically.
