# Correctness report on `round3a/strategy-draft.tex` (Strategy section and closed prototype)

**Read:** `strategy-draft.tex` (and its build, 4 pages), `prototype1.md`, `prototype2.md`.

**Checked against:** the LaTeX sources in `scratchpad/lit/` (FL1 dg-ga/9710032, FL2a math/0007190, FL2b dg-ga/9712005, FL6 math/0609530), and `round3a/src/` (FS blow-up alg-geom/9405002, FKLM math/9812125). Also `notes/R1-literature.md`, T1, T2, T3, `exposition.tex` and `numerology.tex`.

**Theorem numbering.** Theorem and equation numbers were recomputed from the LaTeX counters (`round3a/scripts/numbering.py`). For FL2b the cited statements were read in full.

**My scripts** are in `round3a/referee_scripts/` and use exact arithmetic:
- `r1_identities.py`: identities, the density window, the positive piece, the pinned halves, Lemma D.
- `r2_elliptic_test.py`: a new test of the prototype against Witten's formula on E(N)#rCP̄².
- `r3_incidence_needed.py`: whether the incidence term is ever needed.
- `r4_pinned_cor22.py`: whether Corollary 2.2 is compatible with n_D ≥ 1.

---

## 0. Verdict

1. **The arithmetic of the Strategy is correct.** I re-derived all of the following independently:
   - the pair identities;
   - the per-piece changes (−⅛, −⅜) for a copy of B and (+⅝, +⅞) for a positive piece;
   - n_D = (5m−n)/8 + O(1) and ℓ−T ≤ (7m−3n)/8 + O(1);
   - the windows (1/5, 3/7) for the family and (2/5, 2/7), which is empty, for the closed case;
   - the threshold s < 5/24;
   - Θ(P) = 1;
   - the cost ½ of a pinned sphere's halves;
   - the bound ½ for a chain (Lemma D).
2. **Some statements in the Strategy are false or overstated.** Three are mathematical errors:
   - "the same selection" in (3);
   - the reason given for spacing four in (6);
   - the attribution of the cut-down vanishing to FL2b Thm. 3.33(a) in (1).

   Several others need qualification.
3. **Theorem 2.1 is true as stated.** Its proof is correct, granted the standard transversality that the draft flags. Three qualifications:
   - One hypothesis, S_i·S_i = −4, is never used.
   - The reduction to FL2b has two unstated steps. The first is intersection-suitability for the new supports. The second is the smoothness of the representative at the instanton points, needed for FL2b Lemma 3.22.
   - One construction is misstated: the determinant line must be that of an index-zero operator.
4. **The FL2b citations are all correct**, except for the following:
   - FL1 Thm. 1.1 is cited for a convergence property that lives in FL1 Def. 4.19 and Thm. 4.20.
   - The jumping-line citation [KM, pp. 588–595] could not be confirmed from the available sources, and is probably not where the jumping-line statement appears.
5. **Corollary 2.2 and Remark 2.3 are correct.**
6. **The identities in Remark 2.4 are correct**, but two of its sentences are wrong:
   - "Reducible limits are excluded as in (v)" fails in the family.
   - The heading "would gain nothing" contradicts its own second bullet.
7. **No counterexample to Theorem 2.1 or Corollary 2.2 was found.** A new test on 15 configurations in E(2), E(3) and E(4) blown up shows no contradiction with Witten's formula. In several cases the insertions are genuinely needed: Theorem 2.1 excludes where FL2b Thm. 3.33(a) does not.
8. **Explicit counterexamples to the overstatements:**
   - (3): a class with ⟨K,S⟩ = 2 and Λ·S = 2 is kept by Witten's selection and missed by the incidence.
   - (6): at spacing three the segment inequality holds, with fixed-limit excess (3k−7)m−3k+5 ≥ −2.
   - Remark 2.4(b): K3#4nCP̄² with Λ orthogonal to the halves is a closed manifold that does gain.

---

## 1. The Strategy section, point by point

### (1) A Witten-type relation, used in reverse

**Verified.**
- n_D = ¼(Λ²−σ)−κ, with FLM (2.1.12) via R1.
- The weight-two class restricts to 2h on the instanton link (FL2b Lemma 3.28).
- The count 2^{n_D−1}D^w_X(z) at the instanton link: FL2b Prop. 3.29, eq. (3.60). Its hypotheses are w good, d_a ≥ 0, n_a > 0, deg z + 2δ_c = d_a+2n_a−2, deg z ≥ d_a and z intersection-suitable.
- The strata M_𝔰 × Sym^ℓ with ℓ = κ+¼v² (FL2b Lemma 3.32, (3.64)). ℓ is an integer, because v ≡ w mod 2 gives v² ≡ w² ≡ p₁ mod 4.
- "No gluing at reducibles" is correct for Thm. 3.33(a).

**Error 1.1 (attribution).** The draft says "If none of these is reached, Stokes' theorem gives D^w_X(z) = 0 [FL2b, Thm. 3.33(a)]". That theorem does not say this.
- Its hypothesis (3.68) is that (c₁(𝔱)−c₁(𝔰))² < p₁(𝔱) for **every** 𝔰 with M_𝔰 ≠ ∅. That is, no reducible stratum exists in \bar M_𝔱 at any level.
- Its standing hypothesis is that all reducibles lie in the top level.
- The weaker hypothesis "not reached by the cut-down one-manifold" is the cut-down refinement, i.e. Theorem 2.1 of this draft with n insertions, or R1's Theorem E with no parameters.

*Fix:* "If none of these strata lies in the closure of the cut-down one-manifold, Stokes' theorem gives D^w_X(z) = 0. When none exists at all this is [FL2b, Thm. 3.33(a)], and no gluing at reducibles is needed."

**Imprecision 1.2.** "A nonzero instanton count therefore needs a Seiberg–Witten class to support it" is not what the mechanism gives. The vanishing theorem concerns **non-empty Seiberg–Witten moduli spaces at non-negative level**, whatever their invariant. Section 2 is careful about this, but point (1) is not.

*Fix:* "needs a non-empty Seiberg–Witten moduli space at non-negative level, whether or not its invariant vanishes."

### (2) Non-vanishing from the cosmetic hypothesis

**Verified.**
- The algebra.
- u = (φ_*B)³HB is a well-typed endomorphism of I(Y₂).
- u is invertible on L⊗ℤ₍₂₎ with L = I(Y₂;ℤ)/Tor, because an integral map that is an isomorphism mod 2 has a cone with odd torsion homology.
- u^M ≡ 1 mod 2^N for M divisible by the exponent of GL_r(ℤ/2^N).
- ⟨Ψ₊, u^MΨ₋⟩ ≡ q mod 2^N, since Ψ₊ is an integral functional.
- The remark on integrality.

**Comment.** The mod-2 identification B ≃ g₋g₊ is labelled P (80%) in `exposition.tex`. A strategy section may state it, but not as established fact. Suggest "Surgery exact triangles give, or are expected to give, …" or a footnote.

### (3) A (−4)-sphere costs more energy than it supplies

**Verified.**
- S = F_l − F_r, S² = −4, ∂νS = L(4,1).
- The displayed formula is Witten's formula, FL6 (1.2): the exponent 2^{2−χ_h+c₁²}, the sign (−1)^{½(w²+c₁(𝔰)·w)}, and **D**(z) = D((1+x/2)z).
- The multilinear coefficient. It needs only S_i·S_j = 0 for i ≠ j and h ⊥ S_i, not S_i² = −4.
- The link restriction ½⟨v,S⟩·hyperplane class: FL2b Cor. 4.7 with Def. 4.3 and Lemma 4.8, where ν = c₁(𝒪(1)) on fibres.
- The jumping-line dichotomy.
- The cost of meeting a sphere is ≥ ½ from the halves: −¼v_R² = ⅛(a²+b²) with a, b even and not equal, hence ≥ ½.
- Supply ⅛ with the parameter and ¼ without.
- "Each sphere lowers ℓ−T(v) by at least ⅜ for every class". A met sphere gives ½−⅛. A missed sphere gives 1−⅛ (with a = b the extra cost is even ≥ 1), so ≥ ⅞.

**Error 1.3 (false as stated).** "The SO(3)-monopole cobordism performs the same selection geometrically." It does not.
- The incidence selects the classes with ⟨c₁(𝔰)−Λ, S⟩ ≠ 0. At level zero the link pairing carries ∏⟨c₁(𝔰)−Λ, S_i⟩ (FL2b Thm. 4.13 and Cor. 4.7).
- Witten's formula selects ⟨c₁(𝔰), S⟩ ≠ 0.
- In the application Λ·S = 2, so the two rules differ. A class with ⟨K,S⟩ = 2 has ⟨K−Λ,S⟩ = 0. Witten's rule keeps it, while the incidence misses it and forces a bubble on S.
- Concretely, in K3#2CP̄² with S = σ+e₁+e₂ (σ a (−2)-section) and Λ·S = 2, the basic classes with K·S = 2 are of this kind.
- The two rules are reconciled only after the contributions of all levels are summed (cf. FLL1 Lemma 4.10, bubble term). Prototype 1 §4.2 says this.

*Fix:* "The SO(3)-monopole cobordism performs an analogous selection geometrically, with c₁(𝔰) replaced by c₁(𝔰)−Λ."

**Imprecision 1.4.** Cor. 4.7 is a level-zero statement. Add "(at level zero; at positive level there is a bubble term)". The geometric statement used afterwards, the jumping-line dichotomy, needs no level restriction.

**Minor 1.5.** "Donaldson's jumping-line divisor" is not a standard attribution and I could not verify it. Donaldson's construction is the determinant line bundle and its sections. The fact that for a sphere the canonical section of the index-zero determinant line vanishes exactly on jumping lines is Birkhoff–Grothendieck. Write "the jumping-line divisor".

### (4) Why a family

**Verified.**
- X_M is a connected sum along each J_i, and each J_i separates the two caps (b⁺ ≥ 1 each). So the Donaldson and Seiberg–Witten invariants vanish (Donaldson's connected-sum theorem).
- The description of Ω, the bundles c_e, and the non-invariance of single-bundle counts.
- "B is the difference of the two null-homotopies".
  - The J-end map is zero at chain level, since the gluing parameter at S³ costs 3 > 2 (T2 Thm. 5.2(a)).
  - The bit-summed lens-end map vanishes because ιR₀ι = s′R₀ (T2 Lemma 5.1(d)).
  - So B = Φ₀ − s′ιΦ₀ι is a chain map.
- Supply ¼ → ⅛.

**Imprecision 1.6.** "The operation μ(S)·[W′] is null-homotopic in two ways" holds only for the **signed sum over c and c+PD(S)**. For a single bundle the lens-end term m_cR_c is non-zero, so the lens splitting gives no null-homotopy. Say so: "The signed sum over c and c+PD(S) of μ(S)·[W′] is null-homotopic in two ways".

### (5) Why b⁺

**Verified.**
- Λ_e² = Λ₀² + Σe_i(2Λ₀·S_i − 4), with the spin^c part fixed.
- Λ·F even: F² even and w even on the trace classes.
- Θ_R ≤ 0 for pinned halves: max over a−b = 2, a, b even, of Λ_R²−σ_R is 0.
- Lemma D: a chain contributes ≤ ½; brute force for L ≤ 3 gives exactly ½.
- b⁺ costs ⅜.
- For P = CP²#5CP̄² with the lift Λ₀ = (−2,−1;0,1,0,−1): Λ₀² = 0, σ(P) = −4, Θ(P) = 1, n_D gains ⅝.
- The class u = 0, x = 2, t = (1,0,−1,0) has v² = −2 and v·F_r = v·F′_l = 2. So P with both neighbours costs ½.

**Imprecision 1.7.** "P … has Θ(P) = 1" is a property of the admissible Λ, not of P. With the same trace values ΛU = −3 gives Θ(P) = 4 (`numerology.tex` §6), and the chamber condition is what excludes it.

*Fix:* "and with the Λ allowed by the chamber condition has Θ(P) = 1".

**Minor 1.8.** In the manuscript the base bundle has w₀ ≡ 0 on each negative piece N ≅ ⟨−1⟩². So Λ₀ is characteristic on N and Θ_N ≤ 0 already by parity, for the base bundle (prototype 2, §4). The bundle sum is what forces the same for every choice of w₀. One clause would make the logic complete.

### (6) The balance

**Verified.**
- n_D = (5m−n)/8 + O(1) and ℓ−T ≤ (7m−3n)/8 + O(1).
- The window (1/5, 3/7).
- −W′ has form diag(2,2), so b⁺ = 2.
- At m = n, n_D = n/2 → ∞.
- The consistency argument "it must fail".

**Error 1.9 (wrong reason).** The draft says "the inequality must hold on every segment. This requires the positive pieces to be at least four copies of B apart." The segment inequality does **not** require four.
- For broken limits without a free component, the exact minimum of the excess over segments is (3k−7)m−3k+5 (T1 Prop. 3.4; `numerology.tex` §4). This is ≥ −2 for all m iff k ≥ 3.
- At k = 3 both the global bound (−2 per period) and the segment inequality (+2 per period) hold. `r1_identities.py` reproduces the table.
- Four is needed only for limits **with a free component**. There the reducible segment is weighted by its SO(3)-monopole index (6κ, a positive piece −1), with exact minimum (k−4)m−k+2.
- Even there, four is the requirement **of the projection method** (T1 §3.4: "spacing 4 is forced *for this method*"; `numerology.tex` §5: "Whether spacing three truly fails is open").

*Fix:* "Limits may break along the 3-spheres, so a segment of consecutive pieces can carry an abelian configuration by itself. Without a free component the inequality holds on every segment once the positive pieces are three copies of B apart. Next to a free component, where the segment is weighted by its SO(3)-monopole index, the available argument needs four."

**Overstatement 1.10.** "one of them fails when m/n stays outside [1/5, 3/7]".
- For m/n < 1/5 this is true: n_D → −∞.
- For m/n > 3/7 the global bound is sharp as a lattice statement (T1 §3.6). So the **counting argument** fails. That Seiberg–Witten classes actually reach the cut-down space is shown only for spacing 1 and 2 (`numerology.tex` §5).

*Fix:* "and the counting argument fails when m/n stays outside [1/5, 3/7]".

**Overstatement 1.11.** "Together with m/n > 1/5 it leaves one positive piece for every four copies of B." The constraints are spacing ≥ 4 locally and average spacing < 5 globally. Mixtures of gaps 4 and 5 also satisfy both. The period u is the arrangement with spacing exactly four.

*Fix:* "… it leaves average spacing between four and five, and u realizes four".

**Minor 1.12.** "without φ the only useful return Y₋₂ → Y₂ is the cobordism of H". This is true of the returns **supplied by the surgery triangles**. Theorem 1 of `exposition.tex` allows any negative-definite V. Add "supplied by the triangles".

### Length

The Strategy section runs to about 1.3 pages (pages 1–2 of the build), against the requested one page. This is not a correctness issue.

---

## 2. Theorem 2.1

### 2.1 Is it true?

Yes. The proof is FL2b's (Thm. 3.33(a): Stokes, with Prop. 3.29 and Cor. 3.18). The only new input is the jumping-line representative, and with it the incidence argument at reducible limits of every level is sound:
- Convergence is C^∞ (at least C⁰) on compact sets away from the bubble points, after gauge.
- Non-invertibility of ∂̄ is closed under C⁰ convergence, since ∂̄_A − ∂̄_{A′} has order zero.
- A reducible limit restricts to S_i as λ ⊕ λ⁻¹ with deg λ = ½⟨v,S_i⟩.
- Degree zero on ℙ¹ is trivial.
- Disjoint spheres need distinct bubble points.

I checked every step against the FL2b source:
- Lemma 3.15(1) and its proof via (3.23);
- (3.24)–(3.25) and the dimension count before Cor. 3.18;
- Lemma 3.22 and its proof;
- Prop. 3.29 and its proof;
- (3.31)–(3.32);
- Thm. 3.33.

I found no gap beyond those listed in §2.3.

The dimension count in (iv) is FL's: the **background** has dimension ≤ (d_a+2n_a−1−6ℓ) − (deg z + 2δ_c − 4ℓ) = 1−2ℓ. The positions of the bubbles are not counted, and the draft's wording is consistent with that.

### 2.2 Hypotheses

**Not needed.**
- **S_i·S_i = −4 is never used in the proof** of Theorem 2.1. The theorem holds for any pairwise disjoint embedded 2-spheres with ⟨w,S_i⟩ even.
- By T2 Lemma 4.1 the spheres can even be smooth maps of spheres with disjoint images.
- The value −4 enters only through Corollary 2.2, via the split halves, and through the application.

Either drop it from the statement, or say that the theorem holds for any square and that −4 is kept for the application.

**Needed.**
- w ≢ 0 mod 2 (good): for Prop. 3.29, for the absence of flat reducibles, and for the identification (3.32).
- b⁺ ≥ 1: no abelian ASD connections for generic g.
- n_D ≥ 1: there is no link otherwise.
- ⟨w,S_i⟩ even: a square root of det on S_i, and a divisor. For odd ⟨w,S_i⟩ the jumping locus {E|_S ≇ 𝒪(k)⊕𝒪(k+1)} has real codimension 4, and every class meets S anyway.
- Disjointness of the S_i.
- Simple connectivity (or H₁ = 0): suitable neighbourhoods without loops, no twisted reducibles, goodness ⇔ w ≢ 0.

**Optional.** w ≢ 0 could be removed by passing to X#CP̄² as in FL2b (3.31). One must then check (2.1) on the blow-up.

**Sufficient:** yes.

### 2.3 The proof, step by step

**(i) Error 2.1 (the determinant line).** "V_i is the zero set of the canonical section of the determinant line bundle of ∂̄ on S_i" is not right as written.
- ∂̄ on the rank-two, degree-zero bundle E|_S ⊗ (det)^{−1/2} has index 2, so there is no canonical section.
- The canonical section is that of the **index-zero** operator: the Dirac operator on S² coupled to E|_S ⊗ (det)^{−1/2}, equivalently ∂̄ on its twist by 𝒪(−1) (T2 Prop. 2.3).
- Its kernel is H⁰(𝒪(k−1)⊕𝒪(−k−1)). This is non-zero iff k ≥ 1, which is the jumping-line divisor.

*Fix:* "…the canonical section det ∂̄ of the determinant line of the Dirac operator on S_i coupled to E_A|_{S_i} ⊗ (det E_A|_{S_i})^{−1/2} (equivalently, of ∂̄ on its twist by 𝒪(−1), which has index zero)".

**(i) Citations.** "[D], [DK, Ch. 5], [KM, pp. 588–595]".
- FL2b cites KM pp. 588–595 for the representatives V(β): generic sections of the determinant line over **suitable neighbourhoods**, defined on irreducibles only. That is a different object.
- I could not check whether KM state the jumping-line description.
- DK Ch. 5 (determinant line bundles) is plausible for the class c₁(ℒ_S) = μ(S) but was not available to check.
- The jumping-line statement has a two-line proof: Grothendieck, plus the kernel computation above. Give it, and cite DK only for c₁(ℒ_S) = μ(S).

**(i)** The perturbation argument is correct. Near the compact set of reducible restrictions with ⟨v,S_i⟩ = 0, the canonical section is non-zero (uniform invertibility). So V_i is empty there, and no transversality is required there.

**(ii)/(iv) Gap 2.2 (intersection-suitability for the new supports).** FL2b Lemma 3.17 concerns FL's representatives and their suitable neighbourhoods U_i. Cor. 3.18's count needs (3.25) for **all** supports, including the n_D−1 neighbourhoods ν(x_j) of the weight-two sections (codimension 2 each) and now the spheres S_i (codimension 2 each). (3.25) is the condition Σ_{i: x∈U_i}(4−dim β_i) ≤ 4.
- If the base point of a point class lay on S_i, a bubble there would absorb 4+2 = 6.
- The same holds for a triple overlap of two surface neighbourhoods with S_i.

Both are avoided by general position, but this must be said.

*Fix:* "choose the base points of the point classes and of the weight-two sections off ∪S_i, and the neighbourhoods of the surfaces in z′ so that no point of X lies in supports of total codimension more than four (S_i counting two); then (3.25) holds and z is intersection-suitable in the sense of [FL2b, §3.3]."

**(iii) Gap 2.3 (smoothness at the instanton points).** The proof of FL2b Lemma 3.22 treats V(z) as a **smooth submanifold** of B^{w,*}_κ, transverse to M^w_κ at the finitely many points of V(z) ∩ M^w_κ. Two facts are therefore needed:
- The canonical jumping divisor is smooth only on the stratum k = 1, since it vanishes to first order there. The strata k ≥ 2 have real codimension 6.
- So one needs either that the intersection points avoid k ≥ 2 (true generically), or the perturbed section.

Add one clause.

**(iii) Comment.** FL's representatives may have multiplicity q (Def. 3.4), which enters the proof of Prop. 3.29. The jumping divisor has multiplicity one (T2 Prop. 2.3(d)). This is harmless.

**(iv) Citation.** "Uhlenbeck convergence is C^∞ away from the bubble points [FL1, Thm. 1.1]". FL1 Thm. 1.1 is the compactness statement. The convergence is in the definition, FL1 Def. 4.19, with Thm. 4.20, and FL2b states it in the proof of Lemma 3.15. Cite those.

**(v)** Correct. "There are no zero-section reducibles" is FL2a Prop. 3.1 with Cor. 3.3 (and Lemma 3.2). For generic g this holds at every level, since the walls are countable.

**(vi)** Correct.

**Closing sentence.** "The one point not already in [FL2b] is the transversality in (i)" understates. The following are also new, though elementary:
- that V_i represents μ_p on C^{*,0}_𝔱/S¹ (the analogue of FL2b Lemma 3.12);
- the closure property (the analogue of Lemma 3.15(1), with U_i = S_i);
- the extension of (3.25) (Gap 2.2);
- smoothness at the instanton points (Gap 2.3).

List them.

### 2.4 Citations checked against the LaTeX sources

| Cited | Content in source | Status |
|---|---|---|
| FL2b Prop. 3.29, (3.60) | instanton link count; hypotheses as in §1 | correct |
| FL2b Cor. 3.18 | cut-down 1-manifold misses lower strata | correct |
| FL2b Thm. 3.33(a), (3.68) | no reducible at any level ⇒ #(V̄(z)∩M̄^w_κ) = 0; standing hypothesis "all reducibles at top level" | correct, but see Error 1.1 |
| FL2b Lemma 3.32, (3.64) | splitting criterion; lower-level strata | correct |
| FL2b Lemma 3.15(1) | closure in lower strata ⊂ V_ℓ(β) ∪ {bubble in ν(Y∪D)} | correct |
| FL2b (3.25) | Σ_{i: x∈U_i}(4−dim β_i) ≤ 4 (defines intersection-suitable) | correct, see Gap 2.2 |
| FL2b (3.26), (3.62) | definition of δ_c; the one-manifold | correct |
| FL2b Lemma 3.17 | intersection-suitable if no H₀ or no H₃ classes | correct, for FL's representatives only |
| FL2b Lemma 3.22 | V(z) smooth and transverse to M^w_κ; link points near the instantons | correct, see Gap 2.3 |
| FL2b (3.32) | #(V̄(z)∩M̄^w_κ) = (3.31) = D^w_X(z) for w good | correct |
| FL2b Lemmas 3.12–3.13 | representatives of μ_p and μ_c | correct |
| FL2b Cor. 4.7 | γ*μ_p(h) = ½⟨c₁(𝔰)−Λ,h⟩(2μ_𝔰(x)+ν) − … (level zero) | correct, level zero only |
| FL2b Conj. 3.34, Thm. 4.13 | multiplicity conjecture; the level-zero case | correct (FL2b says Thm. 4.13 proves ℓ = 0) |
| FL2a Prop. 3.1, Cor. 3.3, Lemma 3.13 | stabilizers; no zero-section pairs in M_𝔰; reducibles are SW | correct |
| FL1 Thm. 1.1 | compactness | correct theorem, wrong one for the convergence claim |
| FLM (2.1.12), Thm. 1, Hyp. 7.8.1 | indices; the formula; the gluing hypothesis | correct (via R1) |
| FL6 (1.2) | Witten's formula | correct |
| FS Lemma 2.3(6) | D̂_{c+e}(e z) = D_c(z) (Kotschick) | correct |
| FKLM Thm. 1.3 | D^w(h^{d−2m}x^m) = 0 for d ≤ c(X)−1, assuming Conj. 3.1 | correct, conditional |
| KM pp. 588–595 | FL2b's source for V(β) on suitable neighbourhoods | jumping-line content not confirmed |
| DK Ch. 5, D90 (jumping lines) | — | not available |

Suggested refinement: for "at all levels it follows from the cobordism formula" cite [FLM, Thm. 10.1.2] (conditional on Hyp. 7.8.1). For a stratum that the cut-down space reaches, one also needs its link (Thm. 8.1.9).

---

## 3. Corollary 2.2, Remark 2.3, Remark 2.4

### Corollary 2.2 is correct

The inequality is exact:
- −¼v² = −¼(πv)² + ⅛Σ((a_i⁺)²+(a_i⁻)²);
- met spheres give ≥ ½;
- 8κ = 2n + deg z′ + 3(1+b⁺).

The hypotheses (halves pairwise orthogonal, w even on them) are needed. Remark 2.3 shows this for the halves, and w odd on a half gives a cost of only ¼.

**Missing qualification 3.1.** c_⊥ depends on Λ, and n_D ≥ 1 constrains Λ. If b⁺ ≥ 2 the moduli spaces of ±K are both non-empty for a basic K, so c_⊥ ≥ (πK)² + (πΛ)². Combining this with n_D ≥ 1 (`r4_pinned_cor22.py`), Corollary 2.2 can apply only if

  2b⁻_⊥ − 8b⁺ − 2deg z′ − 2(πK)² − 14 + 4n + 2Λ_R² > 0,

where b⁻_⊥ is the number of negative directions orthogonal to the halves.
- **Pinned** (Λ_R² = −2n): the n-dependence cancels, and the condition is b⁻_⊥ > 4b⁺ + 7 + deg z′ + (πK)².
- **Free** (Λ_R = 0): the margin grows by 4n.

This is the precise form of Remark 2.4(b), and it should be stated after Corollary 2.2. As written, the remark "the spheres must outnumber b⁺ by the factor 3/2, up to the constant c_⊥" hides that c_⊥ grows with the n_D that the spheres consume.

### Remark 2.3 is correct

- FS Lemma 2.3(6), iterated, with μ(2e_i) = 2μ(e_i), gives 2^n D^{w₀}_{X₀}(z).
- w = w₀ + ΣPD(e_i) is good even when w₀ = 0. For K3, D_{K3}(x) = 2 from **D** = e^{Q/2}.
- The per-sphere accounting (cost ¼, supply ¼, Θ +¼) is correct.

### Remark 2.4

The dictionary and the identities are correct:
- ℓ(K)+ℓ(−K) = 4κ + 2n_D + ½(K²+σ);
- 2n_D − ℓ(K) − ℓ(−K) = c(X) − ½d_a − 2d_s(K);
- c(X) = χ_h − c₁² = b⁻ − ½(9b⁺+7);
- the change 4s−1 is 0 in the closed case and −½ in the family;
- the closed window (2/5, 2/7) is empty.

**Error 3.2.** "Reducible limits are excluded as in (v)" is false in the family.
- Step (v) begins "There are no zero-section reducibles". In the family, abelian zero-section configurations **do** occur: at J-faces, on pieces with b⁺ = 0, and on walls ⟨v,H⟩ = 0 of the positive pieces, because dim Q = n > b⁺(X) (R1 (f), item 9).
- Unbroken ones are excluded by the cap class (⟨w₀,A⟩ odd, with a generic cap period).
- Broken ones are excluded by the segment inequality, and next to a free component by the projection.

*Fix:* "Unbroken reducible limits of Seiberg–Witten type are excluded by the incidence argument of (v). Unbroken abelian anti-self-dual limits now occur in the family and are excluded by the cap class. Broken limits need the segment inequality and, next to a free component, the projection."

**Omission 3.3.** The list "It needs compactness over the closed cube, the cancellation of lens ends …, and a treatment of broken limits …" omits two items:
- the Seiberg–Witten localization on the positive pieces, uniform over the cube and its faces (R1 (f) item 7, rated "substantial", second in seriousness);
- the orientation comparison of the lens ends between bundles with different w₂ (item 12).

Add both.

**Inconsistency 3.4.** The heading of (b) is "Even a closed manifold with the same local data would gain nothing". Its own second bullet ("Λ free … Corollary 2.2 applies once n is large") contradicts it. K3#4nCP̄² with halves e_a−e_b, e_c−e_d and Λ orthogonal to them is such a closed manifold: n_D = 5/2 + 3n/4 and c_⊥ is bounded.

*Fix:* "(b) Even a closed manifold with the same local data would gain nothing from the insertions." Then add that what it can gain comes from negative directions, which the bundle sum forbids.

**Imprecision 3.5.** "Take Λ·S_i = 2 and K orthogonal to the halves". K orthogonal to the halves is the **extremal** case. A class with non-zero values on the halves lowers ℓ(K)+ℓ(−K) by (k₊²+k₋²)/4 ≥ 1. Say that these are the classes that decide exclusion, which is all the argument needs.

### Note

In the Λ-free example above (Λ = 0, w odd on every e_j, deg z′ = 0), every basic class already has negative level for n ≥ 3: ℓ = 3/2 − 3n/4. So FL2b Thm. 3.33(a) applies there with no insertions, at least for basic classes. This supports the draft's point that the closed gain comes from negative directions.

---

## 4. Tests on examples and attempted counterexamples

### Test of Theorem 2.1 against Witten's formula (`r2_elliptic_test.py`)

**Setting.**
- Manifolds X = E(N)#rCP̄², N = 2, 3, 4, with basic classes (N−2−2j)f + Σ±e_i and SW = (−1)^j C(N−2, j).
- (−4)-spheres:
  - σ+e in E(3), with σ a (−3)-section;
  - sections in E(4);
  - σ+e±e′ and σ−σ′ in K3;
  - conics;
  - split spheres e−e−e+e;
  - their disjoint combinations.
- Every parity of w on the span with ⟨w,S⟩ even.

**Witten side.** The multilinear coefficient on S^⊥ and its order o.

**FL side.**
- The basic-class form of (2.1).
- Λ is optimized over a box, with n_D = 1 forced by a free real Λ_⊥². This relaxation only makes exclusion easier.
- Exclusion is tested at the most favourable degree, deg z′ = 2o.

**Result.** 15 configurations, 162 parity classes, **no contradiction**: exclusion never holds where Witten's coefficient is non-zero.
- Cross-check: E(4) with one section gives P = 4 sinh 2t, consistent with prototype 1 §2.
- A first run with deg z′ = o instead of 2o produced false "contradictions"; this was a bug in my script, now fixed.

### Is the incidence term ever needed? (`r3_incidence_needed.py`)

Yes. Exclusion with T(v) holds while plain exclusion (max_K ℓ < 0, i.e. FL2b Thm. 3.33(a) for basic classes) fails in:
- E(3)#2 (σ+e with a conic): 4 parity classes out of 4;
- E(4)#1 (section with a conic): 2 of 2;
- K3 with σ−σ′: 4 of 4;
- E(3)#4 (split): 1 of 8.

So Theorem 2.1 is strictly stronger than FL2b Thm. 3.33(a) on examples. In all of them the vanishing is also explained by a symmetry: the cosh factor of a conic with w·e even, or reflection in sphere halves. As prototype 2 says, no closed example is known in which Theorem 2.1 is the only proof.

### Counterexamples

- To Theorem 2.1 or Corollary 2.2: none. The proof is sound.
- To overstatements in the draft:
  - (3), "the same selection": classes with ⟨K,S⟩ = 2 = Λ·S (§1, Error 1.3).
  - (6), "requires four": at k = 3 the segment inequality holds, with excess +2 per period; only the projection method fails, at −1 per period.
  - Remark 2.4(b), heading: K3#4nCP̄² with Λ free.

---

## 5. Required changes

1. **(1)** Attribute "not reached ⇒ D = 0" to the cut-down refinement (Theorem 2.1). FL2b Thm. 3.33(a) assumes that no reducible stratum exists at any level (Error 1.1).
2. **(1)** "needs a Seiberg–Witten class" → "needs a non-empty Seiberg–Witten moduli space at non-negative level, invariant possibly zero" (1.2).
3. **(3)** "the same selection" → "an analogous selection with c₁(𝔰) replaced by c₁(𝔰)−Λ". With Λ·S = 2 the two rules differ. Note that Cor. 4.7 is level zero (1.3, 1.4); drop "Donaldson's" before "jumping-line divisor" (1.5).
4. **(4)** "μ(S)·[W′] is null-homotopic" → "its signed sum over c and c+PD(S) is null-homotopic" (1.6).
5. **(5)** Θ(P) = 1 is a property of the Λ allowed by the chamber condition, not of P (1.7).
6. **(6)** Replace the reason for spacing four. The segment inequality needs three (excess (3k−7)m−3k+5); four is needed by the projection for limits with a free component (excess (k−4)m−k+2), for that method only (1.9). Also:
   - "one of them fails" → "the counting argument fails" (1.10);
   - "one positive piece for every four" → "spacing at least four and average below five; u realizes four" (1.11);
   - "only useful return" → "only return supplied by the triangles" (1.12).
7. **Theorem 2.1:** S_i·S_i = −4 is unused. Drop it or remark on it (2.2).
8. **Proof (i):** the canonical section is that of the index-zero operator (Dirac on S_i, i.e. ∂̄ on the 𝒪(−1)-twist), not of ∂̄ on E|_S⊗det^{−1/2}. Replace the KM page citation for jumping lines by the two-line Grothendieck argument (Error 2.1).
9. **Proof (ii)/(iv):** add the general-position choice that makes (3.25) hold with the spheres (codimension 2) and the weight-two base points among the supports. Lemma 3.17 does not cover them (Gap 2.2).
10. **Proof (iii):** say that V(z) is smooth and transverse to M^w_κ at its finitely many intersection points, as Lemma 3.22's proof requires (Gap 2.3). Cite FL1 Def. 4.19 / Thm. 4.20 for the convergence, not Thm. 1.1. Replace "the one point not already in FL2b" by the short list in §2.3.
11. **After Corollary 2.2:** state that c_⊥ involves Λ. With n_D ≥ 1 and Λ pinned, the corollary needs b⁻_⊥ > 4b⁺ + 7 + deg z′ + (πK)², independently of n; with Λ free, the margin grows by 4n (§3.1).
12. **Remark 2.4 dictionary:** "excluded as in (v)" is false in the family, because abelian zero-section limits occur (3.2). Add the uniform Seiberg–Witten localization on positive pieces and the lens orientation comparison to the list of what FL do not cover (3.3).
13. **Remark 2.4(b):** reword the heading to "would gain nothing from the insertions", and say that K orthogonal to the halves is the extremal case (3.4, 3.5).

## 6. Optional

- Mention that the mod-2 identification B ≃ g₋g₊ is not yet proved (1, (2)).
- Add one clause on parity: w₀ ≡ 0 on N already gives Θ_N ≤ 0 for the base bundle (1.8).
- Theorem 2.1 extends to w ≡ 0 via X#CP̄² as in FL2b (3.31), and to maps of spheres with disjoint images.
- Shorten the Strategy to one page as requested; it is now about 1.3 pages.
