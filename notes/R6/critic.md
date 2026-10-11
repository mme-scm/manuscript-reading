# A critical re-reading of rho.tex and triangle-1.md, Sections 4–5

This note re-examines every deduction in `rho.tex` and in `notes/G-sources/triangle-1.md` §§4–5 under the rules in `r6/RULES.md`:
- differentials need not vanish;
- the only admissible energy facts are E ≥ 0, and E > 0 when no flat connection contributes;
- the exact triangles are assumed.

Each claim carries one of four labels:
- **PROVED**: a complete argument from named standard facts. Where a claim depends on the assumed triangles, it says so.
- **COMPUTED**: an exact machine check. The script is `r6/critic_toys.py` (exact rationals, F_2 linear algebra), and its output is reproduced in the Appendix.
- **PLAUSIBLE**: supported by an argument with a named gap.
- **SPECULATIVE**: heuristic.

---

## 0. Conclusions

1. **The c-level is not a filtration, and this matters for boundary depth (PROVED).** The differential raises c = CS~ − gr/8 by 1/8 − E, where E is the energy of the trajectory. ell-1 §2.2 claims the opposite. Neither rho.tex nor triangle-1 says in which units boundary depth is measured, and triangle-1's boundary-depth clause reads as if c were a filtration.
   - ℓ, ℓ⁺ and DLME's injectivity lemma are unaffected, because they only involve homogeneous classes.
   - Boundary depth must be measured in the Chern–Simons filtration within one degree. A boundary z then has a primitive of c-level at most c(z) + β − 1/8.

2. **The vertex lemma (PROVED; sharpness COMPUTED).**
   - The dichotomy in triangle-1's Lemma 5.1 is correct for arbitrary differentials.
   - Its boundary-depth clause is off by 1/8, in the unfavourable direction.
   - The claim that "1/16 becomes 1/16 + O(β)" is wrong as a general statement. A minimiser can be carried by a long *finite* bar of the middle complex, and then every window conclusion disappears. This happens even when the middle complex is acyclic (Example 2).
   - DLME's ±1 argument uses that C(S³) is **zero at chain level**, not merely acyclic.

3. **What positivity gives in the user's both-bundle version (PROVED, given the triangles).** Put
   - p = min(λ_0, λ_1)(Y_2),
   - q = min(λ_0, λ_1)(Y_{−2}),
   - μ = ℓ(I^tl(K)).

   Then q < p (the drop is positive) in every case except one configuration of the middle term:
   - (a) the traceless image of every cycle realising p is not the boundary of any chain of level < p; and
   - (b) b_* and b′_* both vanish on every class of I^tl(K) of level ≤ p. By exactness, these classes therefore lie in im a_* ∩ im a′_*.

   When the complexes are perfect, (a) says the minimiser of Y_2 has nonzero image in I^tl(K). In that case both bundles of Y_2 lie in the window μ < p ≤ max(λ_0, λ_1)(Y_2) ≤ μ + 1/16. The S³ summand of the middle term is zero and plays no part.

4. **Cosmetic pairs (PROVED; the sharpness is COMPUTED).**
   - A cosmetic pair forces this configuration at the bottom of the spectrum, and its mirror image at the top. For perfect complexes this gives
     μ < min(λ_0, λ_1)(Y) ≤ max(λ_0, λ_1)(Y) ≤ μ + 1/16,
     μ⁺ − 1/16 ≤ min(λ_0⁺, λ_1⁺)(Y) ≤ max(λ_0⁺, λ_1⁺)(Y) < μ⁺.
   - Nothing stronger follows. Example 1 satisfies every triangle identity and every level bound, with strictly positive energies, and has identical complexes on Y_2 and Y_{−2}.

5. **Step 4 of rho.tex.** An energy cost ≥ 0, or > 0, is not enough. The reasons are given in §6. Example 1 realises every absorption cost in (0, 1/16]. Any estimate that closes this window is equivalent to the drop itself.

6. **The gap.** What is missing is a *structural* lemma excluding the configuration (a)+(b) either at the bottom or at the top, for knots with Δ_K = 1.
   - Neither version can hold for all knots. The bottom version fails for the det-1 negative torus knots computed in triangle-1 §5.4, where b = b′ = 0 by parity and absorption is forced. The top version fails for their mirrors.
   - For torus knots, parity always supplies one of the two. That is why the triangles do decide torus knots and do not, by themselves, decide anything else.

---

## 1. Conventions

### 1.1 Complexes and c-levels
For each (Y_{±2}, P_i), C(Y, P_i) is the ℤ-graded lift of the Floer complex over F_2: its generators are lifts α̃ with CS~ and gr~, and it is 8-periodic. For a chain x put ν(x) = max CS~ over the generators in x (ν(0) = −∞). For homogeneous x of degree k put

  lev(x) = ν(x) − k/8.

On a generator, lev(α̃) = c(α) = (3 + ρ(α))/16, in the uniform normalisation of the brief (both bundles). The same conventions apply to C^tl(K), whose period is (1/2, 4).

### 1.2 The differential raises c (PROVED)
- In DLME's convention the differential has degree −1. Index additivity gives i(α, β) = i(α) − i(β), and d counts index-one trajectories.
- d lowers CS~ by the energy E > 0.
- Hence c(β) = c(α) + 1/8 − E. Equivalently: in the level formula take i_0 = 1 and b⁺ = 0.

So c is a filtration of the ℤ/8-graded complex only if every index-one trajectory has E ≥ 1/8. ell-1 §2.2 asserts "the differential does not increase f"; this is false in general. The correct filtered object is CS~ on the ℤ-graded lift, and c-levels may be used only for homogeneous elements.

### 1.3 Maps
Let f be a homogeneous map of degree D whose counted instantons each shift CS~ by at most L. Its **c-shift** is λ_f = L − D/8. This is the "level" of rho.tex Prop. 3.1 and of triangle-1 (1.1), and it satisfies lev(fx) ≤ lev(x) + λ_f.

### 1.4 Boundary depth and death level
- **Boundary depth.** β(C) is the least β such that every boundary z has a primitive y with ν(y) ≤ ν(z) + β. This is in CS units, and it equals the length of the longest finite bar (Usher).
- **Death level.** For a chain z,
  R(z) = inf{lev(y) : dy = z},
  with R(0) = −∞, and R(z) = +∞ if z is not a boundary.
- **Relation (PROVED).** R(z) ≤ lev(z) + β(C) − 1/8 for every boundary z, because a primitive has degree one more than z.
- **Consequence.** A finite bar of CS-length L has c-length L − 1/8, which can be negative.

### 1.5 Invariants
- ℓ(C) is the least c-level of a nonzero homogeneous class, minimised over representatives. This is DLME's inf_d(κ(d) − d/8).
- ℓ⁺(C) is the largest birth level of an infinite bar.
- ℓ of a direct sum is the minimum of the ℓ's.
- ℓ(−Y) = 3/8 − ℓ⁺(Y), by duality of barcodes under c ↦ 3/8 − c.
- λ_i = ℓ(C(Y, P_i)) and λ_i⁺ = ℓ⁺(C(Y, P_i)). Also μ = ℓ(C^tl(K)) and μ⁺ = ℓ⁺(C^tl(K)).

---

## 2. Filtered-algebra lemmas (arbitrary differentials)

**Lemma 2.1 (DLME Lemma 2.6; PROVED).** Let f : C → C′ be a chain map of c-shift λ that is injective on homology. Then every class ξ satisfies lev(f_*ξ) ≤ lev(ξ) + λ, and ℓ(C′) ≤ ℓ(C) + λ. No hypothesis on the differentials is needed.

**Lemma 2.2 (left inverse from triangle detection; PROVED).** Take the data of DLME Prop. 5.1, with q_i ≃ id. Put
- φ_i = (f_i, g_i) : C_i → Cone(f_{i−1}),
- ψ_i(a, b) = g_{i−1}a + f_{i−2}b : Cone(f_{i−1}) → C_{i−3} = C_i.

Then:
- ψ_i is a chain map, by the identity d g_{i−1} + g_{i−1} d = f_{i−2} f_{i−1};
- ψ_i φ_i = f_{i−2}g_i + g_{i−1}f_i = q_i + dh_i + h_i d.

Hence H(φ_i) is injective. This injectivity is all that is used below. Triangle-1 §4.1 calls φ_i a "filtered quasi-isomorphism"; that is neither proved nor needed.

**Lemma 2.3 (vertex lemma; PROVED).** Suppose we have C →f C′ →f′ C″ and g : C → C″ with dg + gd = f′f, and (f, g) : C → Cone(f′) is injective on homology. Let x be a homogeneous cycle with [x] ≠ 0. Exactly one of the following holds.
- (i) [fx] ≠ 0 in H(C′). Then [fx] is a nonzero class of level ≤ lev(x) + λ_f.
- (ii) [fx] = 0. Then for every y with dy = fx, the cycle gx + f′y is not a boundary in C″. Hence
  ℓ(C″) ≤ max( lev(x) + λ_g , R(fx) + λ_{f′} ),
  where R(fx) ≤ lev(x) + λ_f + β(C′) − 1/8. If fx = 0 at chain level, then ℓ(C″) ≤ lev(x) + λ_g.

*Proof.* The class of (fx, gx) in H(Cone f′) is nonzero. In case (ii), subtract d_cone(y, 0) = (dy, f′y) to get (0, gx + f′y). If gx + f′y = dv, then (0, gx + f′y) = d_cone(0, v), which is impossible. ∎

**Remark (where the 1/8 lives).** Write each c-shift as a topological part minus an energy: λ_f = τ_f − E_f, and so on. In the triangles deg g = deg f + deg f′ + 1, so τ_g = τ_f + τ_{f′} − 1/8; the −1/8 is the family term i_0 = −1. Let L be the CS-length of the bar of C′ through fx, computed with the best primitive. Case (ii) then reads:

  ℓ(C″) ≤ lev(x) + τ_f + τ_{f′} − 1/8 + max(−E_g, L − E_f − E_{f′}).

So a drop below lev(x) + τ_f + τ_{f′} survives as long as L < 1/8 + E_f + E_{f′}, and the full 1/8 survives when fx = 0.

Triangle-1's Lemma 5.1 writes lev(y) ≤ ℓ(V) + λ_f + β(V′), with β in CS units. That bound is true but 1/8 weaker. Used as written at the first vertex, it would give ℓ(V″) ≤ ℓ(V) + β, which is no drop at all.

**Lemma 2.4 (the death-level term cannot be removed; COMPUTED).** Example 2 in the Appendix is a triangle with:
- H(C′) = 0, and C′ a single finite bar of CS-length 37/200 > 1/8;
- every identity and every level bound satisfied, with strictly positive energies;
- ℓ(C″) − ℓ(C) = +1/50.

So "the middle term has zero homology" does not give DLME's conclusion. Neither the term R(fx) nor a boundary-depth hypothesis can be dropped.

**Lemma 2.5 (duality; PROVED, given triangles for K̄).** A cosmetic pair for K is one for K̄, because Y_{±2}(K̄) = −Y_{∓2}(K). Moreover ℓ(−Y) = 3/8 − ℓ⁺(Y) and c^tl(K̄) = 3/8 − c^tl(K) (triangle-1 §1.3). So any statement about bottoms for K̄ is a statement about tops for K.

Translating a statement about the *maps* of K̄ into one about the maps a, b of K also needs K̄'s triangle to be the dual of K's. That is PLAUSIBLE, since the cobordisms are the reversed ones, but it is not needed for the level inequalities.

---

## 3. The triangles, the bundles summed, and the level of every map (rule (c))

### 3.1 The triangles
The triangles used are triangle-1's Conjecture T, assumed per rule (c):
- (I) C(Y_2, P_0) →a C^tl(K) →b C(Y_{−2}, P_1) →c C(Y_2, P_0);
- (II) C(Y_2, P_1) →a′ C^tl(K) →b′ C(Y_{−2}, P_0) →c′ C(Y_2, P_1).

Their direct sum is the user's both-bundle triangle:
- outer terms O_+ = ⊕_i C(Y_2, P_i) and O_− = ⊕_i C(Y_{−2}, P_i);
- maps A = a ⊕ a′, B = b ⊕ b′, Γ = c ⊕ c′ (bundle-exchanging), and G_+ = g_A ⊕ g_A′.

### 3.2 The middle term
- On the branched double cover, the triangle is the τ-invariant part of DLME's triangle for (Σ_2(K), K̃) (PLAUSIBLE; triangle-1 §4.5).
- The invariant middle term splits by isotropy type along K̃.
  - **Trivial isotropy (the S³ summand).** Only the trivial connection. It is zero in the irreducible theory (DLME Prop. 3.1(c)). It enters only through index counts that exclude breaking at θ (DLME Lemma 5.9; the J-face of g^ns in triangle-1 §4.2).
  - **Order-two isotropy (the traceless summand).** The traceless representations.
- **Size of the middle term.** Triangle-1's rank identities (§4.6(a)) force the middle term of (I) ⊕ (II) to have rank 2·#R*(K; i) in the SU(2) count. So it is C^tl ⊕ C^tl, one copy for each triangle.
- Everything below holds for an arbitrary middle term M. For M = C^tl ⊕ C^tl, "B_* kills m" means that both b_* and b′_* kill m.

### 3.3 Levels
Levels come from the level formula; E is the energy of the counted instanton, "c-shift" is as in §1.3, and the last column says what is assumed about E.

| map | cobordism, family | b⁺ | i_0 | middle-end term | c-shift | energy input |
|---|---|---|---|---|---|---|
| a, a′, b, b′ | (−X_2°, D_l), (X_{−2}°, D_r), singular, s = 0 | 0 | 0 | none | −E | E ≥ 0. E > 0 unless a flat singular connection contributes, i.e. a traceless representation with λ ↦ −1 (P_0 ends: a, b′) or λ ↦ +1 (P_1 ends: a′, b) |
| c, c′ | −(W′∖νS), odd on ∂νS | 1 | 0 | γ_1 on L(4,1): (3 − 1 + 1)/16 = 3/16 | 3/16 − E | E ≥ 0 |
| g_A, g_A′ | W′, interval of metrics | 0 | −1 | none | −1/8 − E | E > 0. Allowed: the nonsingular part lives on the simply connected W′; a flat singular connection would need λ ↦ −1 and λ ↦ +1 at once |
| g_M, g_B (both triangles) | composites through X_{−2,2}, interval | 1 | −1 | 3/16 | 1/16 − E | E ≥ 0 |
| h | pentagon | 1 | −2 | 3/16 | −1/16 − E | not used |

### 3.4 The hypothesis on λ
rho.tex Step 3 assumes that **no irreducible traceless representation of K sends λ to ±1**. Under this hypothesis the c-shifts of a, a′, b, b′ are strictly negative, which rule (a) allows.

This hypothesis is genuinely extra.
- det K = 1 excludes binary dihedral representations: there are (det K − 1)/2 of them (Klassen).
- It does not exclude other traceless representations with ρ(λ) = ±1 (PROVED for the example below, given the traceless count |σ|/2 computed in triangle-1 §4.6). For a torus knot, λ = x^p μ^{−pq} with x^p central, so a traceless ρ has ρ(λ) = ±ρ(μ)^{−pq}. This is ±1 whenever pq is even.
  - For example, T(3,4) has three traceless irreducibles in the SU(2) count (|σ|/2 = 3) but only one binary dihedral one (det = 3). The others are not binary dihedral and send λ to ±1.
  - For det-1 torus knots pq is odd, so there are none.

The statement in triangle-1 §6.2(b), "for Δ_K = 1 every absorption costs positive energy", is therefore **not established**.

---

## 4. What positivity gives: the both-bundle dichotomy

**Theorem 4.1 (PROVED, given (I), (II) with the levels of §3.3 and the hypothesis on λ).** Let p = min(λ_0, λ_1)(Y_2), q = min(λ_0, λ_1)(Y_{−2}) and μ = ℓ(I^tl(K)). Let x be a cycle realising p. Without loss of generality x lies in C(Y_2, P_0); otherwise exchange (I) and (II). Put x′ = a x ∈ C^tl(K).

1. If R(x′) < p, then q ≤ max(p − 1/8 − E_{g_A}, R(x′) − E_b) < p. In particular, if x′ = 0 then q ≤ p − 1/8 − E_{g_A}.
2. If some class m of I^tl(K) with lev(m) ≤ p has b_* m ≠ 0, or b′_* m ≠ 0, then q ≤ lev(m) − E < p.
3. Hence, if q ≥ p, both of the following hold:
   - (a) for every cycle x realising p, R(x′) ≥ p; that is, x′ bounds no chain of level < p;
   - (b) b_* and b′_* vanish on every class of I^tl(K) of level ≤ p. Equivalently, by exactness of (I) and (II), all these classes lie in im a_* ∩ im a′_*.
4. Suppose q ≥ p and [x′] ≠ 0 for some such x. This is automatic for perfect C^tl, by (a). Then μ < p, and
   - λ_0(Y_2) ≤ μ + 1/16 + β(C(Y_{−2}, P_1)),
   - λ_1(Y_2) ≤ μ + 1/16 + β(C(Y_{−2}, P_0)).

   The β-terms are absent when the differentials of Y_{−2} vanish. In the perfect case this is the window μ < p ≤ max(λ_0, λ_1)(Y_2) ≤ μ + 1/16.

*Proof.*
- (1) Apply Lemma 2.3(ii) at the vertex C(Y_2, P_0) of (I), with C″ = C(Y_{−2}, P_1), λ_{g_A} = −1/8 − E and λ_b = −E_b < 0. Then use q ≤ ℓ(C″).
- (2) The nonzero class b_* m has level ≤ lev(m) + λ_b < lev(m). Similarly for b′_*.
- (3) This is the contrapositive of (1) and (2).
- (4) By (a), μ ≤ lev[x′] ≤ p + λ_a < p. Let z be a cycle realising μ. By (b), b_*[z] = 0 = b′_*[z]. Apply Lemma 2.3(ii) at the vertex C^tl of (I), with f = b, f′ = c, g = g_M and C″ = C(Y_2, P_0). This gives
  λ_0(Y_2) ≤ max(μ + 1/16, R(bz) + 3/16),
  and R(bz) ≤ μ + β(C(Y_{−2}, P_1)) − 1/8. Triangle (II) gives the bound on λ_1(Y_2) in the same way. ∎

**Answer to the user's question about the configuration.** Positivity alone gives drop > 0 except in the configuration (a)+(b). That configuration is a statement about the middle term and the maps a, a′, b, b′ on filtered homology; it is not an energy statement.

In words:
- the traceless complex carries the bottom of Y_2;
- nothing in the traceless homology at or below that level reaches either bundle of Y_{−2};
- everything there comes from Y_2 in both bundles.

For perfect complexes the configuration is:
- F_p H(I^tl(K)) ≠ 0;
- F_p H(I^tl(K)) ⊂ im a_* ∩ im a′_* = ker b_* ∩ ker b′_*;
- the minimiser of Y_2 has nonzero image in F_p H(I^tl(K)).

When the differentials are nonzero, the configuration has a second form: x′ is a boundary, but only of chains of level ≥ p. The bar of C^tl through x′ then has CS-length at least 1/8. In this form there is no window (Example 2).

**Remarks.**
- **The S³ summand.** It is zero at chain level, so it cannot carry x′. When x′ = 0, which is how a zero middle term behaves, part (1) gives DLME's drop q ≤ p − 1/8 − E. In this sense the S³ summand produces the 1/8, and the traceless summand is the only possible obstruction.
- **Without the hypothesis on λ** (zero-energy flat contributions allowed):
  - the conclusion of (2) weakens to q ≤ lev(m), and in (b) "level ≤ p" becomes "level < p";
  - μ < p weakens to μ ≤ p;
  - one more degenerate case appears, q = μ = p, realised only through zero-energy singular instantons at traceless representations with λ ↦ ±1.
- **(a)+(b) is necessary for q ≥ p, but not sufficient.**
  - Example 1 has q = p and Example 3 has q > p.
  - The det-1 negative torus knots satisfy (a)+(b): b = b′ = 0 by parity, and absorption is forced (triangle-1 §5.4). Yet for them q < p by about 1/8.
  - So inside the configuration the triangles and positivity say nothing about the sign of the drop.
- **Mixed version.** The same proof, applied to (I) alone, gives m_1 > 0 unless:
  - every minimiser x of C(Y_2, P_0) has R(ax) ≥ λ_0(Y_2), and
  - b_* vanishes on classes of level ≤ λ_0(Y_2).

  In that case, for perfect complexes, λ_0(Y_2) ≤ μ + 1/16. The both-bundle exception is strictly narrower: it needs both b_* and b′_* to vanish, and it squeezes both bundles.
- **Size of the drop.** Outside the exception the drop is either > 1/8 (part (1) with x′ = 0) or merely > 0 (part (2), an unquantified energy). So "drop ≥ 1/16" is not obtainable from positivity even outside the exception; "drop > 0" is.

---

## 5. Cosmetic pairs: the strongest energy-free consequence

**Theorem 5.1 (PROVED, given triangles for K and K̄ and the hypothesis on λ).** Suppose Y_2 ≅ Y_{−2} =: Y by an orientation-preserving diffeomorphism. Then:
- (a) Configuration (a)+(b) of Theorem 4.1 holds with p = q = min(λ_0, λ_1)(Y).
- (b) The mirror configuration holds at the top. It is obtained by applying Theorem 4.1 to K̄. In terms of the maps of K this reads (PLAUSIBLE, since it needs the duality of the triangles):
  - every functional detecting the top level of I(Y_{−2}) ⊕ I^w(Y_{−2}) is nonzero on im b_* + im b′_*;
  - im a_* + im a′_* lies strictly below max(λ_0⁺, λ_1⁺)(Y_{−2}).
- (c) For perfect complexes:
  - μ < min(λ_0, λ_1)(Y) ≤ max(λ_0, λ_1)(Y) ≤ μ + 1/16;
  - μ⁺ − 1/16 ≤ min(λ_0⁺, λ_1⁺)(Y) ≤ max(λ_0⁺, λ_1⁺)(Y) < μ⁺;
  - the minimisers of both bundles are absorbed;
  - |λ_0(Y) − λ_1(Y)| < 1/16 and |λ_0⁺(Y) − λ_1⁺(Y)| < 1/16.
- (d) With nonzero differentials, (c) holds with 1/16 replaced by 1/16 + β(Y) whenever the minimiser is absorbed by an infinite bar. Otherwise C^tl(K) has a finite bar of CS-length at least 1/8 that is alive at level min(λ_0, λ_1)(Y).

*Proof.*
- The diffeomorphism carries P_i to P_i and preserves c, so the filtered complexes at the two ends agree and p = q.
- (a) is Theorem 4.1(3).
- (b) is Theorem 4.1 applied to K̄, translated by Lemma 2.5.
- (c), first line, is Theorem 4.1(4). The second line is its mirror, using μ(K̄) = 3/8 − μ⁺(K) and ℓ(−Y) = 3/8 − ℓ⁺(Y).
- (c), both minimisers absorbed: say λ_0 ≤ λ_1 and let x_1 realise λ_1. If x_1 were not absorbed, then by perfectness and Lemma 2.3(ii), λ_0 ≤ λ_1 − 1/8 − E. But λ_1 ≤ μ + 1/16 < λ_0 + 1/16, a contradiction.
- (d) follows from the same argument, using Lemma 2.3 with the boundary-depth terms. ∎

These are exactly triangle-1's Proposition 5.6(b),(c) and Corollary 5.8, now stated with the conditions that hold for arbitrary differentials.

**Proposition 5.2 (nothing more follows; COMPUTED).** Example 1 in the Appendix is a model of (I) and (II) with the following properties:
- the same filtered complexes on Y_2 and Y_{−2} in each bundle (a cosmetic configuration);
- every triangle-detection identity holds exactly (h = 0, q = id);
- every level bound of §3.3 holds, with strict positivity for a, a′, b, b′ and g_A;
- the maps are homogeneous, with a and b of degree 1.

The model can be doubled to respect the ι-pairing on Y_{±2} and the χ-pairing on C^tl.

Consequently, no argument that uses only the triangle identities, the levels of §3.3, positivity of energy and the gradings can exclude a ±2 cosmetic pair. The obstruction has to come from somewhere else.

---

## 6. The previous Step 4: is positivity enough?

**No.** Neither E ≥ 0 nor E > 0 suffices, for the following reasons.

1. **a and a′ have zero topological level.** Their cobordism has b⁺ = 0, i_0 = 0, s(D) = 0 and no middle end. So their c-shift is −E, and E can a priori be any positive number. Positivity gives a strict but unquantified drop across a.
2. **An absorbed class never reaches Y_{−2}.** It lies in im a_* = ker b_*. Upper bounds on ℓ(Y_{−2}) come from only two sources:
   - classes of ker a_*, through g_A, with c-shift −1/8;
   - classes of I^tl(K) outside ker b_*, through b, with c-shift ≤ 0.

   The exceptional configuration (a)+(b) is precisely the absence of both sources at or below the level of the minimiser.
3. **The 1/16 is a ceiling, not a floor.** It appears only in c, c′, g_M and g_B. These maps go from Y_{−2} or from the middle term up to Y_2, or from Y_{−2} up to the middle term. Through Lemma 2.3 at the middle vertex the 1/16 yields p ≤ μ + 1/16, an upper bound on p, never a lower bound on the drop.
4. **The window is realised.** Example 1 realises every absorption cost p − μ in (0, 1/16] with all constraints satisfied.

So Step 4 needs exactly "the absorption cost on the minimiser exceeds 1/16", that is, p − μ > 1/16. This is the negation of the window and hence equivalent to the conclusion; rule (a) forbids it.

**With E ≥ 0 only.** Things are worse. The strict inequality μ < p and the exclusion of emission at level exactly p are both lost. This adds the degenerate configuration p = μ = q, realised through zero-energy singular instantons at traceless representations with λ ↦ ±1.

**In the user's version.** In that version (outer terms summed over both bundles; middle term the S³ theory plus the traceless theory), positivity gives drop > 0 outside the configuration of Theorem 4.1(3). That configuration is structural:
- the bottom class of O_+ maps into the traceless homology. In general this means it does not bound below level p; for perfect complexes it means its image is nonzero;
- every class of I^tl(K) at level ≤ p lies in ker b_* ∩ ker b′_* = im a_* ∩ im a′_*.

The S³ summand is zero and never takes part.

---

## 7. How 1/16 enters

- **Topologically.** The flat connection γ_1 on L(4,1) (rotation by π/2, w_2 ≠ 0) contributes (3 − h + ρ)/16 = 3/16. This gives c and c′ c-shift 3/8 − 3/16 = 1/8 + 1/16, and gives g_M and g_B c-shift 1/16.
- **In the filtered algebra** the 1/16 appears only as:
  - (a) the ceiling 3/16 for the drop when the middle term is zero at chain level. Then g_A is a chain map inverse to Γ up to homotopy, and Lemma 2.1, applied once in each direction, gives drop ∈ [1/8 + E, 3/16]. This is triangle-1 §4.4; it is PROVED only for a middle term that vanishes at chain level, and it is false for an acyclic one (Example 2). For ±2 the middle term is never zero: every nontrivial knot has an irreducible representation with traceless meridian (Kronheimer–Mrowka);
  - (b) the width of the windows in Theorem 4.1(4) and Theorem 5.1(c).
- **Never as a lower bound.** The maps carrying the 1/16 all move classes upward.
- **The examples with m_2 = 1/16** (4_1 and T̄(2,3)) record where the data sit inside these bounds; for T̄(2,3), m_2 = 3/16 − 1/8 after a zero-energy absorption. They are not consequences of the triangles.
- **For the cosmetic problem** the 1/16 gives two narrow, computable necessary conditions: the two windows of Theorem 5.1(c).

---

## 8. Audit of rho.tex

Each item records: (D) validity for nonzero differentials, (E) energy inputs and whether the rules allow them, and the status.

1. **Prop. 2.1, c = (3 + ρ)/16.** APS index theorem, with signs fixed by the Poincaré-sphere check.
   - (D) not applicable. (E) none. PROVED.
2. **Def. 2.2 and Cor. 2.3, ℓ = λ_0.**
   - (D) Valid, because ρ(x) is used only for homogeneous classes, and within one degree ordering by CS is ordering by ρ. (E) none. PROVED.
   - But the tacit picture of a c-filtered complex (stated in ell-1 §2.2) is wrong (§1.2).
3. **"The differential vanishes for every Seifert fibred Y."** Verified by parity for the torus-knot surgeries (seifert-1). It is not proved for every Seifert fibred Y. COMPUTED for the examples.
4. **Prop. 3.1, the level formula.** APS bookkeeping; energy enters only as −E. PROVED.
5. **Cor. 3.2, an injective map gives an inequality.**
   - (D) Valid (DLME Lemma 2.6). (E) E ≥ 0. PROVED.
6. **"Odd sixteenths enter a level only through ρ(γ_j)."**
   - True for the topological part on nonsingular cobordisms.
   - On singular cobordisms the term s(F)/8 of Kronheimer–Mrowka can be ±1/16 (cores of ±1 surgery: s = 1/2, triangle-1 §2.4).
   - For the ±2 maps s = 0, so the statement holds where it is used.
7. **The lens-space table, 1/16 = 1/8 − |ρ|/16, and the cap energy 1/(4e).** COMPUTED, and standard.
8. **"The maps carrying 1/16 exchange P_0 and P_1."** PROVED: γ_1 has w_2 ≠ 0, and H²(νS; ℤ/2) → H²(L(4,1); ℤ/2) is an isomorphism.
9. **§4 data table.** COMPUTED (Seifert complexes, zero differentials).
10. **Conjecture 5.1** (m_1, m_2 ≥ 1/16, strict if det K = 1).
    - Not implied by the triangles plus positivity. Theorem 4.1 gives m > 0 outside the exceptional configuration and nothing inside it.
    - "≥ 1/16" is out of reach even outside the exception (§4, last remark).
    - SPECULATIVE.
11. **Cor. 5.2** (the conjecture excludes cosmetic pairs). Valid.
12. **Step 1, the levels.**
    - Correct bookkeeping (§3.3). (E) E(g_A) > 0 is allowed.
    - The triangles are assumed.
13. **Step 2.**
    - "Assume the differentials vanish" is not allowed.
    - The first alternative, a(x) = 0 at chain level, is valid for all differentials.
    - The dichotomy "a(x) = 0, or a(x) ≠ 0 in T(K)" misses the case where a(x) is a nonzero boundary. There Lemma 2.3 gives only q ≤ max(p − 1/8 − E, R(ax) − E_b). By Example 2, this case can produce a negative drop.
14. **Step 3.**
    - Valid for perfect complexes under the hypothesis on λ. It uses only strict positivity, which is allowed.
    - For arbitrary differentials its correct form is Theorem 5.1(d).
    - Nothing stronger follows (Proposition 5.2).
15. **Step 4.** A forbidden energy estimate, equivalent to excluding the window (§6). Its local slope analysis is an energy computation in a model and is admissible only as heuristic.
16. **"Steps 2 and 3 are formal; (iii) control of how far below the lowest class its boundaries can reach."**
    - Item (iii) is not a technicality (Lemma 2.4).
    - Controlling it by an a priori bound on boundary depth would be an upper bound on energies of trajectories of C^tl, which rule (a) also forbids.
    - The admissible replacement is the structural condition R(ax) < p of Theorem 4.1(1).

---

## 9. Audit of triangle-1.md §§4–5

1. **§4.1, Conjecture T.** Assumed per rule (c). The "filtered quasi-isomorphism" clause is unnecessary and unproved; only Lemma 2.2 is used.
2. **§4.3, the level table.**
   - Correct bookkeeping. The justification of E(g_A) > 0 is admissible.
   - The claim that at a common point only one of a, b sees the flat connection with index 0 is COMPUTED for torus knots and PLAUSIBLE in general.
3. **§4.4, the window [1/8, 1/8 + E_cap] "without interference".**
   - PROVED when the middle term is zero at chain level.
   - False when the middle term is merely acyclic (Example 2).
   - Never applicable to ±2, since C^tl(K) ≠ 0 for every nontrivial K.
4. **§5.1, Lemma 5.1.**
   - The dichotomy holds for arbitrary differentials.
   - The boundary-depth clause should be R(fx) ≤ ℓ(V) + λ_f + β(V′) − 1/8, with β in CS units. As written it is 1/8 too weak and would destroy the kernel criterion (§2, Remark).
   - The table of alternatives is valid for perfect complexes only.
5. **Theorem 5.2, the kernel criterion.**
   - Valid for arbitrary differentials, both the chain-level clause and the clause with the primitive y.
   - (E) E(g_A) > 0, allowed.
6. **Corollary 5.3.** Valid: the complexes are Seifert and perfect, and the argument is parity. The upper bounds are COMPUTED.
7. **§5.4, absorption.**
   - COMPUTED, for perfect complexes.
   - Key observation: the det-1 negative torus knots satisfy the exceptional configuration of Theorem 4.1 at the bottom (b = b′ = 0, absorption forced), yet their both-bundle drop is about 1/8.
   - So the triangles do not explain the drop for negative torus knots. It is visible only in the spectra.
8. **§5.5, the identities.** PROVED (algebra).
9. **Proposition 5.6.**
   - (a) and (b) are valid for perfect complexes under the hypothesis on λ, which uses strict positivity (allowed).
   - With differentials, (a) can fail: the minimiser may be carried by a finite bar.
   - (b) acquires +β(Y).
   - The replacement is Theorem 5.1.
10. **Theorem 5.7.** Forbidden energy estimate (absorption cost > 1/16). It is equivalent to the negation of the window.
11. **Corollary 5.8.** PROVED for perfect complexes, given T. It is Theorem 5.1(c).
12. **"Boundary depth: 1/16 becomes 1/16 + O(β)."** Incorrect as a general statement: there is a finite-bar alternative with no window at all.
13. **§6.2(a), the local slope model.** An energy computation; heuristic only.
14. **§6.2(b), "for Δ_K = 1 every absorption costs positive energy".** Not established (§3.4).

---

## 10. The gap, precisely

Assume triangles (I) and (II) for K and K̄, and the hypothesis on λ. A ±2 cosmetic pair for K is then excluded as soon as **one** of the following is proved.

- **(Bottom)** Either
  - some cycle realising min(λ_0, λ_1)(Y_2) has traceless image bounding a chain of level < min(λ_0, λ_1)(Y_2), or
  - some class of I^tl(K) of level ≤ min(λ_0, λ_1)(Y_2) survives under b_* or under b′_*.
- **(Top)** The mirror statement: the same, applied to K̄.

Each is a statement about the maps a, a′, b, b′ on filtered homology. Neither is an energy estimate. Neither follows from the triangle identities and levels (Proposition 5.2).

Neither holds for all knots:
- (Bottom) fails for the det-1 negative torus knots computed in triangle-1 §5.4 (COMPUTED there, perfect complexes): b = b′ = 0 by parity, and absorption is forced in both triangles.
- (Top) fails for their mirrors, the det-1 positive torus knots, because (Top) for K is (Bottom) for K̄.

For torus knots, parity always gives one of them:
- for a positive torus knot, a = a′ = 0, which gives (Bottom), with drop > 1/8;
- for a negative torus knot K, the mirror K̄ is positive, and a(K̄) = a′(K̄) = 0 gives (Top) for K.

For Δ_K = 1 there is no parity. In a cosmetic case, moreover, a_* and b_* are both nonzero as soon as I^tl(K) ≠ 0. Indeed:
- exactness and equal ranks of the ends give rk im A_* = rk im B_*;
- these two ranks add up to rk H(M).

So a proof must use a property specific to the knots in question, or prove (Bottom) or (Top) jointly, as a single disjunction.

Possible sources of such a structural input (SPECULATIVE):
- **A second exact triangle** in which C^tl(K) meets Y_{±2} with a nonpositive topological level and which detects the bottom of I^tl(K). The single twist L_0 = τ_V(L_2) (triangle-1 §2.2) suggests one through Y_0.
- **The framed (Daemi–Scaduto) traceless complex.** There the reducible θ_K gives a tower whose position is a concordance invariant, and one could try to place the bottom of I^tl(K) relative to that tower.
- **A module structure** (for example the point class, of degree 4) that a and b preserve and that moves levels by a topological amount.

None of these is an energy estimate, and none is available yet.

---

## Appendix: the examples (COMPUTED, `r6/critic_toys.py`)

The script checks the following for each example:
- d² = 0;
- the differential has degree −1 and strictly decreasing CS;
- the f's are chain maps;
- dg + gd = ff;
- fg + gf = id;
- homogeneity of every map;
- the level bounds of §3.3, with strict inequality for a, b, g_A.

It then computes ℓ and ℓ⁺ by brute force.

**Example 1 (cosmetic configuration).**
- Complexes: P_0 = ⟨x_0⟩ at u = 3/100 and P_1 = ⟨x_1⟩ at v = 3/100, the same on Y_2 and Y_{−2}. C^tl = ⟨z, z′⟩ at μ = 0 and μ′ = 6/100.
- Triangle (I): a x_0 = z, b z′ = x_1, b z = 0, c = 0, g_A = 0, g_M z = x_0, g_B x_1 = z′.
- Triangle (II): the same with x_0 and x_1 exchanged.
- Degrees: x_0 and x_1 in degree 0, z in degree 1, z′ in degree −1.
- Output: every relation and level bound holds; drop = 0; m_1 + m_2 = 0; both windows hold.
- Any μ < u, v ≤ μ + 1/16 and max(u, v) < μ′ ≤ min(u, v) + 1/16 works.

**Example 2 (finite-bar carrying; acyclic middle term).**
- Complexes: O_+ = ⟨x⟩ at 0; M = ⟨z, y⟩ with dy = z, z at −1/100 and y at 5/100; O_− = ⟨w⟩ at 2/100.
- Maps: a x = z, b y = w, c w = x, g_M z = x, g_B w = y, g_A = 0.
- Output: every relation and level bound holds; H(M) = 0; the CS-length of the bar is 37/200; drop = −1/50.

**Example 3 (infinite-bar absorption, negative drop).**
- Complexes: O_+ = ⟨x, x′⟩ at 0 and 17/100; M = ⟨z⟩ at −3/100; O_− = ⟨w⟩ at 2/100.
- Maps: a x = z, b = 0, c w = x′, g_A x′ = w, g_M z = x.
- Output: every relation and level bound holds; drop = −1/50.

Script output (the script calls the examples "Models"):
```
Model 1, triangle (I): relations and level bounds OK      (ell: Y_2 3/100, tl 0 [top 3/50], Y_-2 3/100)
Model 1, triangle (II): relations and level bounds OK
   min(l0,l1)(Y_2) - min(l0,l1)(Y_-2) = 0 ; m1 + m2 = 0 ; both windows True
Model 2 (finite-bar absorption): relations and level bounds OK ; C0 acyclic ; drop = -1/50 ; bar CS-length 37/200
Model 3 (infinite-bar absorption): relations and level bounds OK ; drop = -1/50
```
