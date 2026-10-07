# Audit of the two round-2 derivations against the manuscript

**Scope.** Every number in `round2/derivation1.md` (D1) and `round2/derivation2.md` (D2) was recomputed by hand from the manuscript TeX (`src/02`, `03`, `04`, `05`, `06`, `07`, `08`) and, where a minimisation is involved, by an independent computer check written for this audit (files in `round2/audit_checks/`, described in §14). Labels in code font are the manuscript's LaTeX labels.

**Verdicts.** *correct*; *wrong* (with the corrected value); *unverifiable* (the manuscript does not decide it). "same" in the D2 column means D2 states the same value as D1.

**Outcome in one paragraph.** No number in the manuscript is wrong. D1 and D2 agree on every block value, both global inequalities, all per-period values and all exact segment minima, and the audit confirms each of them independently (segment minima for spacings 2–5 and up to four positive pieces). There is one substantive disagreement, at spacing 1. D1 says the sharp per-period level balance is 0; this is wrong. D2 says the energy cost is unbounded below, so the level bound is unbounded above; this is right (§9). The other discrepancies concern our notes and small imprecisions (§11, §13).

---

## 1. A copy of B: W' = (−X₂) ∪_{S³} X₋₂ : Y₂ → Y₋₂

| # | Number or claim | D1 | D2 | Verdict | Reference |
|---|---|---|---|---|---|
| 1.1 | H₂(W') = ⟨F_l, F_r⟩ with form diag(−2,−2): b⁺ = 0, σ = −2 | 0, −2 | same | correct | `negative:sphere` |
| 1.2 | S = F_l − F_r, S² = −4, SᵢSⱼ = 0 | yes | same | correct | `negative:sphere`, `stack:sphere-pairings` |
| 1.3 | (Λ₀F_l, Λ₀F_r) = (0, −2), Λ₀S = 2, c₀S = 0 | yes | same | correct | proof of `stack:lifts` ((Λ₀F_r, Λ₀F'_l) = (−2,0) on every cell); `stack:sphere-pairings` |
| 1.4 | PD(S) evaluates (−2, 2) on (F_l, F_r); (Λ_eF_l, Λ_eF_r) = (−2e, −2+2e); Λ_eS = 2 − 4e = ±2 | yes | same | correct | `negative:lifts`, `stack:bit-lifts` |
| 1.5 | relative Λ_e² on W' equals −2 = σ for e = 0, 1, so Θ(W') = 0 for both lifts | 0 | 0 | correct (hand and `audit_lemma.py`) | global form `stack:global-bit-squares`; cell form `stack:cell-theta` |
| 1.6 | in cell bookkeeping the zero is (−1/4 + e/2) + (1/4 − e/2) | yes | — | correct | `stack:cell-theta` |
| 1.7 | Θ is independent of the bit iff Λ₀S = 2, since Λ₁² − Λ₀² = 2Λ₀S − 4 | — | yes | correct | `stack:global-bit-squares` |
| 1.8 | energy supplied 1/8 (8κ rises by 1): one interval parameter and one test of real degree 2 | 1/8 | same | correct | `negative:dimension` (i + 1 + 1 − 3 = 0); text before `stack:ordinary-dimension` |
| 1.9 | coupled Dirac index −1/8 | −1/8 | same | correct | `stack:dirac-growth` |
| 1.10 | halves even; v² on W' = −(h_l² + h_r²)/2; μ(S) met iff vS = h_l − h_r ≠ 0 (winding vS/2) | yes | same | correct | `stack:negative-dual-square`, Lemma `stack:tests` |
| 1.11 | least energy cost 1/2 when met, attained at (±2,0), (0,±2); if missed the Feehan–Leness level is ≥ 1, distinct spheres needing distinct points | 1/2; ≥ 1 | same | correct | `stack:negative-test-cost` (8κ ≥ 4s); Def. `indices:analytic-hypotheses`(ii) |

## 2. The positive cobordism W_H (path −2 → −1 → 0 → 1 → 2) and the positive piece P = X₋₂ ∪ W_H ∪ (−X₂)

| # | Number or claim | D1 | D2 | Verdict | Reference |
|---|---|---|---|---|---|
| 2.1 | b⁺(P) = 1, σ(P) = −4 | yes | same | correct | Prop. `stack:lattice` |
| 2.2 | b⁺(W_H) = 1, σ(W_H) = −4 + 1 + 1 = −2 (each trace half has σ = −1) | yes | same | correct | Novikov additivity across Y₋₂, Y₂; cf. proof of Cor. `ordinary:bridge` |
| 2.3 | Q_P = [[2,1],[1,0]] ⊕ (−I₄) ≅ ⟨1⟩ ⊕ 5⟨−1⟩; F_r = G − ΣT_b, F'_l = G − 2U, F_r² = F'_l² = −2, F_r·F'_l = 0, UF_r = UF'_l = 1 | yes | same | correct (`audit_lemma.py`) | `stack:positive-lattice` |
| 2.4 | v² = 2xu − 2u² − Σt_b² | yes | same | correct | `stack:positive-dual-square` |
| 2.5 | Λ₀ = (−2,−1;0,1,0,−1), c₀ = (2,1;1,0,1,0), Λ₀² = c₀² = 0 | yes | same | correct | `stack:base-lifts` |
| 2.6 | l = Λ₀ − c₀ = (−4,−2;−1,1,−1,−1) characteristic, l² = 4 = 2χ + 3σ | yes | — | correct | proof of `stack:lifts` (l²: audit) |
| 2.7 | Θ(P) = 1; relative Λ₀² on W_H = 0 − (−2) − 0 = 2, Θ(W_H) = 1 for all bits | 1 | 1 | correct | `stack:cell-theta` (m_cell = 1) |
| 2.8 | energy supplied 3/8 (b⁺ rises by 1); coupled Dirac index +5/8 | yes | same | correct | `stack:ordinary-dimension`, `stack:dirac-growth` |
| 2.9 | x even; t_b ≡ (1+e, e, 1+e, e) mod 2 (two odd); u ≡ λ = −1 − e + f, so u odd iff the adjacent bits agree | yes | same | correct | proof of `stack:charge-costs`; `estimates:vertex-values` |
| 2.10 | λ₁ = −3/2 + f, λ₂ = −1/2 − e, λ₁₂ = −1; \|λ_I\| ∈ {1/2, 1, 3/2} | yes | same | correct | `estimates:vertex-values`, `indices:lambda-values` |
| 2.11 | c₀F₀ = 1 for F₀ = G − T₃ − T₄; determinant odd on T₂ − T₁ | yes | — | correct | `stack:middle-class`, proof of `stack:charge-costs` |
| 2.12 | u = 0 ⇒ Q₀ = −Σt_b² ≤ −2 | yes | same | correct | Lemma `indices:positive-square`; u = 0 on the long tube by Cor. `estimates:tube` |
| 2.13 | Q ≤ −2 except nonzero spinor, \|I\| = 1, u = z_I = ±1, where Q ≤ 2 and d_i = 0 | yes | same | correct; the three identities `indices:square-one`, `-two`, `-both` re-expanded by hand | Lemma `indices:positive-square` |
| 2.14 | maxima of Q: u = 0: −2; zero spinor: −6 (\|I\| = 1), −4 (\|I\| = 2); nonzero spinor: −2 (\|I\| = 2, and \|I\| = 1 outside the exception), 2 (exception) | yes | same | correct (`audit_lemma.py`: \|x\| ≤ 16, \|u\| ≤ 6, \|t_b\| ≤ 5, \|h_i\| ≤ 18, all bits, both types; no violation) | Lemma `indices:positive-square` |
| 2.15 | positive cobordism with its two adjacent copies of B costs ≥ 1/2 (8κ ≥ 4), attained at u = 0, x = 2, t = (1,0,−1,0); exceptional case −1/2 + level 1 = 1/2; marginal cost −1/2 against two free copies of B | yes | same | correct | `indices:incidence-charge`, `stack:positive-charge` |
| 2.16 | this accounting needs each copy of B adjacent to at most one positive piece (k ≥ 2) | — | yes | correct | reservation paragraph before Lemma `indices:component-score` |
| 2.17 | Θ(P) = 1 is the largest value with (ΛF_r, ΛF'_l, ΛU) = (−2, 0, −1): then x = −2, Σt = 0, Λ² = 2 − Σt² ≤ 0 | — | yes | correct | not stated in the manuscript; follows from `stack:positive-dual-square` |
| 2.18 | with the same trace evaluations and ΛU = −3: Λ = (−6,−3;−2,−1,0,−1), Λ² = 12, Θ(P) = 4, λ₁ = −7/2 | yes | — | correct (audit: the largest Θ(P) for ΛU = −1, −3, −5 is 1, 4, 9) | not in the manuscript; the narrow chamber \|λ_I\| ≤ 3/2 is used in the proof of `indices:positive-square` |

D1 (Θ(P) = 4 is possible) and D2 (Θ(P) = 1 is maximal) do not conflict: D2 fixes ΛU = −1, D1 does not.

## 3. A definite cobordism V : Y₋₂ → Y₂ with b₁ = b⁺ = 0 (or φ)

| # | Number or claim | D1 | D2 | Verdict | Reference |
|---|---|---|---|---|---|
| 3.1 | b⁺ = 0, no parameter, no test: energy 0 | 0 | 0 | correct | notes T4 §3; the manuscript treats only φ |
| 3.2 | Θ_V ≤ 0, with 0 for a lift whose diagonal coordinates are ±1 and (ΛF_r, ΛF'_l) = (−2, 0); uses Donaldson's theorem on N_V = X₋₂ ∪ V ∪ (−X₂) | yes | yes | correct | notes T4 Lemma 3.1; for φ, H₂ = 0 and the cell is ⟨−1⟩² with Λ₀² = −2 = σ (`stack:negative-lattice`, proof of `stack:telescope`) |
| 3.3 | coupled Dirac index Θ_V, best 0 | "0" | "Θ_V, best 0" | correct (D1's "0" means the best lift) | — |
| 3.4 | least cost 0; −v² ≥ ½((vF_r)² + (vF'_l)²) on N_V by orthogonal projection, the only form used | yes | same | correct | `stack:negative-dual-square` enters only as an upper bound for v² (proof of `indices:component-score`) |
| 3.5 | reducible flat connections on V have index −3(1 − b₁ + b⁺) = −3; central contacts cost 3 | yes | yes | correct as a statement of notes T4 Prop. 3.4 | not in the manuscript (analogue: Lemma `ordinary:central-cost`) |
| 3.6 | "definite" alone is not enough: −E₈ has characteristic Λ = 0 with Λ² − σ = 8 | yes | — | correct (a lattice remark; Donaldson excludes it on a closed smooth N_V) | — |

## 4. Caps

| # | Number or claim | D1 | D2 | Verdict | Reference |
|---|---|---|---|---|---|
| 4.1 | b⁺(C_±) ≥ 1; together b₀ | yes | same | correct | Thm. `caps:pairing`(i); proof of Prop. `estimates:cap` (A² = 0, cA odd) |
| 4.2 | energy supplied (z + 3 + 3b₀)/8, i.e. z_± + 3b⁺(C_±) per cap plus a global 3 | yes | same | correct | proof of Prop. `caps:periods` (8κ_closed = z + 3(1 + b⁺)); `stack:ordinary-dimension` |
| 4.3 | Θ₀ contains (1 − Λ(E)²)/4 for each extra exceptional class (E² = −1, cE = 0, ΛE odd) | yes | same | correct | Thm. `caps:pairing`(ii); text before Lemma `stack:lifts` |
| 4.4 | coupled Dirac index of the caps c₁ = Θ₀ − (z + 3 + 3b₀)/8, fixed before the repetitions | yes | same | correct | Table `stack:choices`, rows 2–3 |
| 4.5 | no zero-spinor abelian component contains a cap | yes | same | correct | Thm. `estimates:clamp`(ii) |
| 4.6 | v_W² ≤ C_W and (Λ_W + v_W)² ≤ C_W, so each cap lowers the least cost by at most C_W/4, independently of n, m, Λ(E) | yes | same | correct | `estimates:cap-squares`, `estimates:CW` |
| 4.7 | vE even with cost (vE)²/4; on short outside components \|KE\| ≤ B, so \|vE\| ≥ \|ΛE\| − B; outside Seiberg–Witten components have q + 4 ≥ 8 | yes | same | correct | Lemma `indices:end-exclusion`, `indices:end-score` |

## 5. Totals and the two global inequalities

| # | Number or claim | D1 | D2 | Verdict | Reference |
|---|---|---|---|---|---|
| 5.0 | ℓ = κ + v²/4 is Feehan–Leness's ((Λ − K)² − p₁)/4 with p₁ = −4κ; a class occurs only if ℓ ≥ 0 | yes | yes | correct | `indices:ell`; notes R1 §0 (Memoir (2.3.14)) |
| 5.1 | b⁺ = m + b₀, Θ = m + Θ₀ | yes | same | correct | `stack:total-topology` |
| 5.2 | 8κ = n + 3m + z + 3 + 3b₀ | yes | same | correct | `stack:ordinary-dimension`; proof of Thm. `stack:nonzero` (8κ changes by n + 3m) |
| 5.3 | n_D = (5m − n)/8 + Θ₀ − (z + 3 + 3b₀)/8 | yes | same | correct | `stack:dirac-growth` |
| 5.4 | (I): n_D → ∞ iff 5m − n → ∞, asymptotically m/n > 1/5 | 1/5 | 1/5 | correct | — |
| 5.5 | −v²/4 + T(v) ≥ (n − m)/2 − C, C = (C_{W−} + C_{W+})/4, valid for k ≥ 2 | yes | same | correct | `indices:incidence-charge` summed with s_N = n − 2m; `estimates:cap-squares` |
| 5.6 | ℓ − T(v) ≤ (7m − 3n + c_κ)/8 + C, c_κ = z + 3 + 3b₀; (II) iff asymptotically m/n < 3/7 | 3/7 | 3/7 | correct | — |
| 5.7 | manuscript form q ≥ 3L − 7m + 2Σv(E)² − C; the unbroken component has q = 0, forcing 3n − 7m ≤ C | yes | yes | correct | `indices:end-lower`, `indices:end-square`, `indices:phase-count` |
| 5.8 | m ≤ (L + 3)/4 gives 3L − 7m ≥ (5L − 21)/4 | yes | yes | correct | proof of `indices:end-exclusion` |
| 5.9 | per piece (Δn_D, Δ(8ℓ) bound): copy of B (−1/8, 1 − 4 = −3), positive piece (+5/8, 3 + 4 = +7); in ℓ: −3/8 and +7/8 | yes | yes | correct | — |
| 5.10 | the window is nonempty because (5/8)/7 > (1/8)/3, equivalently 1/5 < 3/7 | — | yes | correct | — |
| 5.11 | spacing 4: n = 4m + p, n_D = (m − p)/8 + c₁, 3n − 7m = 5m + 3p | yes | yes | correct | Thm. `stack:nonzero` (n = p₋ + 4q₀ + p₊, n_D = q₀/8 + Θ₀ − (p₋ + p₊ + z + 3 + 3b₀)/8); text after `stack:dirac-growth` |

## 6. One period of spacing k (k copies of B, one positive cobordism, k − 1 copies of V); all values times 8 unless stated

| # | Number or claim | D1 | D2 | Verdict | Reference |
|---|---|---|---|---|---|
| 6.1 | energy supplied k + 3 | yes | same | correct | 5.2 |
| 6.2 | 8ΔΘ = 8 | yes | — | correct | 5.1 |
| 6.3 | least energy cost 4(k − 2) + 4 = 4k − 4 for k ≥ 2, attained | yes | same | correct (`audit_periods.py`: increments 4, 8, 12, 16 for k = 2, …, 5, both types) | `indices:incidence-charge` |
| 6.4 | Δn_D = (5 − k)/8: +3/8, +1/4, +1/8, 0 for k = 2, …, 5; +1/2 at k = 1; (I) iff k ≤ 4 | yes | same | correct | — |
| 6.5 | Δ(8ℓ) bound = 7 − 3k: +1, −2, −5, −8; (II) iff k > 7/3 | yes | same | correct (audit: 1, −2, −5, −8) | — |
| 6.6 | fixed excess per period 3k − 7 = −(7 − 3k): −1, 2, 5, 8; weights: κ has weight 8, each piece +1, each positive piece −3, each sphere −2; free copy +3, positive cobordism with its two copies 4 + 2 − 4 − 3 = −1 | yes | same | correct | proof of `indices:component-score` (q_i + 4 = 8κ_i + L_i − 3m_i − 2s_i) |
| 6.7 | mixed excess per period k − 4: −2, −1, 0, 1; κ has weight 6 = 8 − 2, positive piece −3 + 2Θ = −1, sphere −2, parameters 0; free copy 3 − 2 = +1, positive cobordism with its two copies 3 − 1 − 4 = −2 | yes | same | correct | proof of `indices:mixed-run` (i_i − p_i = 6κ_i − 3 − m_i + Δ_i − 2s_i) |
| 6.8 | D2's table, rows k = 2, …, 5 and the row k ≥ 2 | — | yes | correct | — |
| 6.9 | row k = 1 | (II) "4 − 4 = 0 at best" | least cost unbounded below; Δ(8ℓ) bound unbounded above | **D1 wrong, D2 correct** (§9.3) | — |

## 7. Local excesses and the exact minima over segments of consecutive pieces

| # | Number or claim | D1 | D2 | Verdict | Reference |
|---|---|---|---|---|---|
| 7.1 | fixed excess Σ(q + 4) = 8κ − 3m + L − 2s, independent of internal cuts | yes | same | correct | proof of `indices:component-score`; `indices:virtual-sums` |
| 7.2 | mixed excess Σ(4 + i − p) = r + 6κ − m + Δ − 2s | yes | same | correct | proof of `indices:mixed-run` |
| 7.3 | spheres not adjacent to a positive piece: s − 2m + f (k ≥ 2), with L = k(m − 1) + 1 + a + b + g, s = L − 1 + ε_a + ε_b | yes | — | correct | — |
| 7.4 | fixed lower bound (3k − 7)m − 3k + 1 + [3a + 2ε_a + 4f_a] + [3b + 2ε_b + 4f_b] + 3g ≥ (3k − 7)m − 3k + 5 (each bracket ≥ 2) | yes | yes | correct | — |
| 7.5 | mixed lower bound (k − 4)m − k + r + Δ + g + [a + ε_a + 3f_a] + [b + ε_b + 3f_b] ≥ (k − 4)m − k + 2 = (k − 4)(m − 1) − 2 | yes | yes | correct; the end inequality is the manuscript's | proof of `indices:mixed-run` |
| 7.6 | m = 0: ≥ 1 (fixed) and ≥ 0 (mixed) | yes | — | correct | proofs of `indices:fixed-run` ("at least L > 0") and `indices:mixed-run` ("s + r + Δ ≥ 0") |
| 7.7 | m = 1: both minima −2, attained by one positive piece with both adjacent tests assigned to it, κ = 1/2 | yes | yes | correct (audit) | — |
| 7.8 | exact fixed minima: k = 2: −m − 1; k = 3: 2m − 4; k = 4: 5m − 7; k = 5: 8m − 10; attained | yes | yes | correct for m ≤ 4 (audit: −2,−3,−4,−5; −2,0,2,4; −2,3,8,13; −2,6,14,22) | — |
| 7.9 | exact mixed minima: k = 2: −2, −3, −6, −7 (m = 1, …, 4); k = 3: −m − 1; k = 4: −2 (m odd), −1 (m even); k = 5: m − 3 | yes | yes | correct for m ≤ 4 (audit: k = 3: −2,−3,−4,−5; k = 4: −2,−1,−2,−1; k = 5: −2,−1,0,1) | — |
| 7.10 | the mixed bound needs Δ = −1, i.e. an odd number of bit changes, ≡ m + (m − 1)k mod 2; for even k and even m the minimum is one higher | yes | "attained for odd m at k = 4" | correct; internal true cuts do not lower any minimum (`cuts_check.py`) | — |
| 7.11 | the manuscript's coarse bound max(2s + L − 7m, m + L − 2s) still has minimum −2 under L ≥ 3m − 2 (minimum L − 3m at m ≤ 3, and 2m − 8 ≥ 0 for m ≥ 4) | yes | yes | correct (audit: minima −2, −2, −2, 0, 2, … at spacing 3) | Lemma `indices:fixed-run` |

## 8. Thresholds of the two exclusions

| # | Number or claim | D1 | D2 | Verdict | Reference |
|---|---|---|---|---|---|
| 8.1 | fixed limits tolerate −3 per segment: 4α + 8β − 3(α + β − 1) = α + 5β + 3 ≥ 5 > 4; −4 does not suffice (4 − 4 + 4 = 4) | yes | yes | correct | `indices:virtual-sums`, `indices:end-score` |
| 8.2 | the manuscript proves −2 and obtains 2a + 6b + 2 ≥ 6 | yes | yes | correct | Lemma `indices:fixed-run`, Prop. `indices:fixed-exclusion` |
| 8.3 | mixed limits: −2 suffices (3 − 2N ≤ −1) and is exact (a segment at −3 with N = 2 gives 5 − 8 + 3 = 0) | yes | yes | correct | `indices:projected-dimension`, Prop. `indices:mixed-exclusion` |
| 8.4 | fixed limits need k ≥ 3 (at k = 2 the first failure is m = 3, value −4); mixed limits need k ≥ 4 (at k = 3 the first failure is m = 2, value −3) | yes | yes | correct | — |
| 8.5 | only k = 4 meets (I), (II) and both local conditions; the manuscript uses exactly 4 | yes | yes | correct | §5.1 ("at least four intervals apart"); Thm. `stack:nonzero` |

## 9. Spacing by spacing

| # | Number or claim | D1 | D2 | Verdict | Reference |
|---|---|---|---|---|---|
| 9.1 | k = 1: n_D grows by 1/2 per period | yes | yes | correct | — |
| 9.2 | k = 1: 3n − 7m ≈ −4m | yes | — | correct (crude form of (II)) | — |
| 9.3 | k = 1, the per-period level balance | "sharply, supply equals demand (1/2 per period)"; table "4 − 4 = 0 at best" | least energy cost unbounded below, level bound unbounded above | **D1 wrong; D2 correct.** The value 0 presupposes Lemma `indices:positive-square` with its reserved neighbouring halves, unavailable when adjacent positive pieces share a (−4)-sphere. Audit: the least 8κ on two adjacent positive pieces is −4, −24, −56 (zero spinor) and −24, −56, −100 (nonzero spinor) as the range of evaluations grows (`k1_box.py`). D1's own chain (9.5) contradicts "sharply". | — |
| 9.4 | k = 1, D1's u = 0 class: x = 0, t = (1,0,1,0) and (0,1,0,1) alternately, bits alternating; −v² = 2 per piece, interior spheres met with vS = 2, level independent of m | yes | — | correct (with both boundary tests assigned inward, the last one is missed: a boundary effect) | — |
| 9.5 | k = 1, D1's divergent chain: u = 1, x_j = 4 + 2j, t = (1,0,−1,0), z₂ = 0 | "bits 0, last piece u = 0" | — | correct, with one precision: the final bit must be 1, since u ≡ 1 + e + f (D1's check file uses final bit 1). Audit: 8κ = −20, −76, −220, −524 for 3, 5, 8, 12 pieces | — |
| 9.6 | k = 1, D2's family v = (−2N, −1; 1, 0, 1, 2), bits 0: vS = 6, v² = 4N − 8, K² = 8N − 4, Seiberg–Witten dimension 2N − 2, sign(u)z₂ = −1/2 < \|λ₂\| = 1/2, vH = −1 − 6a + 6b, ΛH = −1 − 2a + 2b, band (vH)(KH) < 0 at (1/64, 3/16) (vH = 1/32, KH = −5/8), ℓ = (N − 3/2)m | — | yes | correct (`audit_explicit.py`); the band holds exactly when 1/6 < b − a < 1/4. Compatibility of (a, b) along shared intervals: unverifiable (D2 says so), and moot | — |
| 9.7 | k = 1: the construction and the chamber condition are unavailable (the positive cobordisms with their adjacent copies of B must be disjoint and separated by single intervals) | yes | yes | correct | §5.1; Prop. `stack:composition` |
| 9.8 | k = 2: (II) fails, supply 5 against cost 4, level grows like m/8 (density 1/2 > 3/7) | yes | yes | correct (audit: periodic cost 4 per period) | — |
| 9.9 | k = 2 periodic class: u = 0, x = 2, Σt = 0 on positive pieces, halves (0,0) on negative pieces, bits …0,1,1,0,0,1,1,0… | yes | yes | correct | — |
| 9.10 | k = 2: PNPNP, bits 0,1,1,0,0,1, both boundary tests inward: −v² = 6, κ = 3/2, L = 5, s = 6, m = 3, Σ(q + 4) = 12 − 9 + 5 − 12 = −4; ASD \| PNPNP \| ASD sums to 4 | yes | yes | correct (audit) | `indices:virtual-sums` |
| 9.11 | k = 2: PNP gives −3 and is still excluded | yes | yes | correct | — |
| 9.12 | k = 2: mixed limits fail, −2 per period | yes | yes | correct | — |
| 9.13 | k = 2: two positive cobordisms with their adjacent copies of B meet at one seam; A ≤ S fails; (−2) + (−2) + 3 = −1 | yes | yes | correct | Prop. `stack:composition`, `stack:macro-excess` |
| 9.14 | k = 3: (I) +1/4, (II) −2 in 8ℓ, fixed minimum 2m − 4 ≥ −2 | yes | yes | correct | — |
| 9.15 | k = 3: PNNP with (P_*, (1,−1), (0,0), P_*), bits 0,1,0,0,1, zero spinor: −v² = 6, κ = 3/2, s = 5, Δ = −1, Σ(4 + i − p) = 1 + 9 − 2 − 1 − 10 = −3; projected dimension ≤ 5 − 8 + 3 = 0 | yes | yes | correct (audit) | `indices:projected-dimension` |
| 9.16 | k = 3: (P N₁ N₀)³P gives −5 = (k − 4)m − k + 2 at m = 4 | yes | yes | correct (audit) | — |
| 9.17 | zero spinor on a positive-width toric piece forces vH = u + a d₁ + b₀ d₂ = 0; the extremal classes have u = 0, d₁ = d₂ = 2 at internal sides | yes | yes | correct | Lemma `estimates:projection`, `geometry:period` |
| 9.18 | counting one wall per positive piece gives k − 3 per period and −1 for PNNP | yes | yes | arithmetic correct; the transversality it needs is not in the manuscript: unverifiable. "Artifact of the method" is a shared judgement, not a manuscript statement | — |
| 9.19 | k = 4: n_D +1/8 and level bound −5/8 per period; mixed excess 0 per period, minimum −2 (m odd), −1 (m even) | yes | yes | correct | — |
| 9.20 | k = 5: Δn_D = 0; n_D = Θ₀ − (p + z + 3 + 3b₀)/8 is constant and is made < 1 by large \|Λ(E)\| (each lowers Θ₀ by (Λ(E)² − 1)/4) and pads p ≥ 2L_*; the abelian side holds with +8 and +1 per period | yes | yes | correct | Thm. `stack:nonzero`; Lemma `indices:end-exclusion` |
| 9.21 | k ≥ 6: n_D falls by (k − 5)/8 per period; mixed gaps: each ≥ 4, average < 5 | yes | yes | correct | — |

## 10. Positive pieces, the cosmetic map, and HB ≡ 1 mod 2

| # | Number or claim | D1 | D2 | Verdict | Reference |
|---|---|---|---|---|---|
| 10.1 | 1/5: a positive piece (+5/8) offsets five copies of B (−1/8 each) | yes | yes | correct | — |
| 10.2 | Θ > 0 needs b⁺ > 0; a piece helps only if Θ > 3b⁺/8 | — | yes | correct | `indices:closed-indices` |
| 10.3 | without φ the returns are H (b⁺ = 1) and the reversed interval −W' (form diag(2,2), b⁺ = 2), forcing k = 1 | yes | yes | b⁺ values correct; "these are the only returns" is a claim of notes T4 §2.2 ([P]): unverifiable from the manuscript | — |
| 10.4 | HB ≡ 1 mod 2: B ≡ g₋g₊ (the Z₂ face of the four-step family), f₊g₊ ≃ J₂, and the mirror gives g₋f₋ ≃ J; hence B ≡ f₋⁻¹f₊⁻¹ = H⁻¹ | yes | yes (writes f₊g₊ ≃ 1; the manuscript has the continuation J₂, which is immaterial) | correct up to the Floer automorphisms introduced by the fixed tensor and end identifications (last sentence of the proof of Lemma `negative:four-topology`); **not stated in the manuscript**, whose only occurrences are 𝒟 = HB (Thm. `stack:nonzero`) and BHB (Prop. `stack:macro`) | `ordinary:two-step-identity`, proof of Thm. `ordinary:units`, Lemma `negative:four-topology`, proof of Thm. `negative:unit` |
| 10.5 | (HB)^M with M a multiple of the exponent of GL_r(Z/2^N): Ω ≡ ±q mod 2^N, while n_D ≈ M/2 | yes | yes | correct | Lemma `stack:finite-lattice` |
| 10.6 | caveat: the manuscript's caps contain φ⁻¹ through T = f₋φ⁻¹f₊ | yes | yes | correct | Cor. `ordinary:bridge`, §4 |
| 10.7 | "the exclusions must fail at spacing 1, and they do" | yes, restricted to caps without φ⁻¹ | yes (summary unrestricted; restricted in its §5) | the failure at spacing 1 is correct (§9); the necessity argument holds only for caps without φ⁻¹ whose pairing is nonzero, which the manuscript does not supply (condition (N) of notes T4 §2.2): unverifiable | — |

## 11. Statements about our notes

| # | Claim | D1 | D2 | Verdict |
|---|---|---|---|---|
| 11.1 | T1 §3.4 Observation 5 ("level bound grows like +4 per period" at k = 1) is wrong | yes, replaced by "sharp balance 0, or worse" | yes, replaced by "unbounded" | the note is wrong (it extrapolates 7 − 3k, i.e. the cost 4k − 4 = 0, to k = 1); the right replacement is D2's; D1's "0" is also wrong (9.3) |
| 11.2 | the exposition also says "+4 per period" (D1: "exposition §7") | yes | — | **wrong attribution.** The exposition contains no "+4". Its spacing-one statements are in §8, "then Seiberg–Witten classes do contribute" (line 142), and §9, "the exclusions provably fail" (line 163). D1's correction of the first to "cannot be excluded" is right |
| 11.3 | D §4.4 "three negative-rule tests" per positive piece at k = 4 should be two (k − 2 = 2 spheres, in three negative pieces) | yes | — | correct |
| 11.4 | B4 §4 gives the mixed bound as "2" at spacing 4 and "4 − m" at spacing 3; the minima are −2 and −m − 1 | yes | — | correct. B4's values are the bound at a = b = 0 with both boundary tests outside (3 + Δ at Δ = −1, and 4 − m + Δ at Δ = 0), not minima |
| 11.5 | (m, L, s) = (2, 3, 4) gives −3, which breaks Lemma `indices:fixed-run` but not the exclusion; the first failure is PNPNP at −4 | yes (cites D §4.3) | yes (cites B4 §4) | correct; both notes contain the example |
| 11.6 | closed forms (3k − 7)m − 3k + 5 and (k − 4)m − k + 2 (T1 Prop. 3.4, exposition §7) are lower bounds; the second is not attained for even k and even m | yes | yes | correct |
| 11.7 | maxima of Lemma `indices:positive-square` in T1 §3.2: −6, −4; 2, −2 | yes | yes | correct |

## 12. Statements about the manuscript

Both derivations: "no numerical discrepancy in the manuscript". **Correct.** The audit rechecked, besides the items above: the lift evaluations (−1, −1) on a, b and l on P (proof of `stack:lifts`); c_e² = c₀² − 4Σe_i and Λ_e² = Λ₀² (`stack:global-bit-squares`); the telescope Λ_e² − Λ₀² = 4e_j − 2e_j² − 2e_{j+1}² = 2(e_j − e_{j+1}) and the outside contributions −e₁/2, +e_n/2 (proof of `stack:telescope`); the tables 1, −1, 0, −4 and 2, −1, −4 in the proof of Lemma `stack:local-excess`; the bounds 5 + k − t, 5 − t, 6 in the proof of Prop. `stack:macro`; the table (1,1): 2, 0, −2 and (1,2): 1, −1, 1 and the bound 5m − 11 in the proof of Lemma `indices:fixed-run`; Σ(q_i + 4) = 4 and Σi_i − 2η = 2 − 4k (`indices:virtual-sums`); the free dimension 1 after `indices:phase-count`; 2χ + 3σ = 4(1 − b₁ + b⁺) + σ (proof of Lemma `indices:closed`); and the identity 5 − 4N − Σ_R(4 + i − p) in `indices:projected-dimension`.

Slack, as both derivations say (correct): the conclusion of Lemma `indices:fixed-run` and the arguments of Lemma `indices:end-exclusion` and Prop. `stack:composition` work at spacing 3; spacing 4 is needed only in Lemma `indices:mixed-run`, whose threshold −2 is attained.

## 13. Where the derivations disagree, and the decision

1. **Spacing 1 (9.3, 6.9, 11.1).** D1 calls 0 the sharp per-period balance; D2 says the cost is unbounded below. D2 is right. The balance 0 uses Lemma `indices:positive-square` with reserved neighbouring halves, which does not apply when consecutive positive pieces share a (−4)-sphere. D1's own chain in its §4 has −v² → −∞, and the audit's minimisation decreases without bound as the range of evaluations grows. Both derivations agree that (II) fails at k = 1.
2. **Notes.** D1 alone corrects D §4.4 and B4 §4 (mixed values); both corrections are right. D1 alone attributes "+4 per period" to the exposition, which is wrong (11.2).
3. **Wording.** D1's chain at k = 1 needs final bit 1, not "bits 0" throughout (9.5). D2's f₊g₊ ≃ 1 should be ≃ J₂ (10.4). D1's "n_D = 0" for V means the best lift (3.3). D2's summary states the spacing-1 consistency test without the restriction to caps free of φ⁻¹ that its own §5 and D1 impose (10.7).

Every other number is the same in D1 and D2 and is correct.

## 14. Checks performed for this audit (`round2/audit_checks/`)

- `audit_lemma.py` (output `lemma_out.txt`): lattice and lift data of P and of a copy of B; Θ(P), Θ(W_H), Θ(W'); the largest Θ(P) for fixed trace data; maxima and exceptions in Lemma `indices:positive-square`.
- `audit_explicit.py` (output `explicit_out.txt`): every explicit configuration quoted by D1 and D2 (PNP, PNPNP, PNNP, (PNN)³P, the k = 2 periodic class, both k = 1 classes and D1's chain).
- `audit_dp.py`: exact minimisation of κ over a segment, cell by cell, with parities, bits, incidence and the chamber condition on whole sides only (halves of absolute value ≤ 8, \|u\| ≤ 4). Coverage: `segments_out.txt` searches all segments with gaps k or k + 1, up to two extra negative pieces at each end and all boundary assignments, for k = 2, 3 (m ≤ 4) and k = 4 (m ≤ 2); `core45_out.txt` covers k = 4, 5, m ≤ 4, with up to one extra negative piece at an end; `cuts_out.txt` adds internal true cuts; `periods_out.txt` gives the cost per period; `k1_box_out.txt` gives spacing 1 on growing ranges. The fixed minima are moreover forced by the proven lower bound (7.4) and explicit attainment.
