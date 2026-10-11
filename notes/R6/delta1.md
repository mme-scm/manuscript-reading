# Lemma C on knots with Alexander polynomial 1

Setting and normalisations are those of `r6/BRIEF.md`, `r6/judge.md` §2.3 and `notes/G-sources/pillowcase-final.md` §E–F:
- C is the image of R*(E_K) in the pillowcase, with ρ(μ) ~ e^{2πiα}, α ∈ (0, 1/2), and ρ(λ) ~ e^{2πiβ}. Put δ = α − 1/4 and let s = dβ/dα be the slope of C.
- The generators of Y_N are the points of C with Nα + β ∈ ℤ (bundle P₀) or Nα + β ∈ 1/2 + ℤ (bundle P₁). Both χ-twins are counted (the SU(2) count).
- The level formula is c(Y_N, x) = Φ(x) + (3/16) sgn N − N·α(1/2 − α) − ι_N(x)/8, with dΦ = 2δ dβ along C.
- G_C(Y_N) is the least level of a generator of Y_N on the component C, over both bundles, and d_C = G_C(Y₂) − G_C(Y₋₂).

Labels:
- **COMPUTED**: a machine computation.
- **VERIFIED**: cross-checked independently, or exact.
- **PLAUSIBLE**: an argument with a named gap.

All code and outputs are in `r6/delta1-code/`; §9 lists the files.

---

## 0. Verdict

1. **The notes' ι-rule is wrong in sign for N < 0 (VERIFIED: exact, two independent ways).**
   - The rule ι₋₂ = +[s ∈ (0, 2)] contradicts c(−Y) = 3/8 − c(Y).
   - The exact Seifert data for mirror torus knots at N < −pq demand ι = −1 there (`iota_mirror.out`).
   - The consistent rule (PLAUSIBLE) is **ι_N = sgn(N)·[s strictly between 0 and −N]**. Equivalently, (3/16) sgn N − ι_N/8 = (1/8) sgn N + τ(TC, TL_N, TL₀)/16, where τ is the Maslov triple index.
   - Continuity of c under perturbations then forces **Φ to jump by −1/8 across every horizontal tangency** of C, from the s < 0 side to the s > 0 side. Equivalently, the level function of Y_N along C jumps only where C is tangent to the direction of L_N.
   - I call this corrected version **reading B**, and the literal formula of the notes **reading A**.
   - A COMPUTED check supports reading B. For KT and Conway, reading B gives Euler characteristic 0 on every component and in every bundle. Reading A makes χ(I(Y₂), P₀) equal ±4 or ±20, which contradicts χ = 0 for Δ_K = 1.
2. **The curves (COMPUTED).**
   - **KT and Conway:** C is the same set for both knots (they are mutants), to sampling accuracy. It consists of four smooth closed curves, forming two χ-pairs. Each has β-winding 0, ∮2α dβ = 0 and ∮2δ dβ = 0 to 10⁻⁸. Each has two horizontal tangencies and four traceless crossings. C avoids the reducible line, is nondegenerate, and every generator is transverse to L_{±2}.
   - **D₊(RHT) and D₋(RHT):** four valid closed curves each, with winding ±2 and ∮2α dβ = ±1. Every traceless point lies at (1/4, 0), so λ ↦ 1 there. R* is Morse–Bott degenerate: there is a bending circle over every point of C.
   - **P(−3,5,7):** degenerate. Besides two χ-pairs of closed curves of winding ±2, C contains four **flat loops**: one-parameter families with λ ↦ 1, whose image is a segment of β = 0 traversed back and forth. These meet the other curves at singular points.
3. **The per-component drop is independent of the unknown component constants**, because min_C d_C ≤ G(Y₂) − G(Y₋₂) ≤ max_C d_C. In reading B (and, in brackets, reading A):

| knot | as given | mirror image |
|---|---|---|
| Kinoshita–Terasaka 11n42 | [0.0956, 0.1187] ([0.1187, 0.1249]) | [0.1105, 0.1873] ([0.0937, 0.1751]) |
| Conway 11n34 | identical to KT | identical to KT |
| D₊(RHT) | [0.0847, 0.1250] ([0.125, 0.25]) | [0.1087, 0.1250] (same) |
| D₋(RHT) | [0.1000, 0.1250] (same) | [0.0994, 0.1250] ([0.125, 0.25]) |
| P(−3,5,7) | [0, 0.1641] **undecided** | [0, 0.1228] **undecided** |

   - **Positive and at least 1/16, for every choice of constants, in both readings:** KT, Conway, D₊(RHT), D₋(RHT), and their mirrors (COMPUTED, given the formula).
   - **P(−3,5,7): the per-component argument is inconclusive.**
     - The flat loops carry only twisted generators at (1/4, 0), shared by Y₂ and Y₋₂ with Δc = 0, so d = 0 on them.
     - Linking their constants to the neighbouring curves through the singular points (PLAUSIBLE bookkeeping, two resolutions per point) gives one piece with drop **0 or 0.0567** (mirror: **0 or 0.0725**) and the other piece with at least 0.104 (mirror: at least 0.050). The relative constant of the two pieces is unknown.
     - So a generator-level drop of exactly 0 is not excluded.
     - Even ignoring the flat loops, one χ-pair of curves has d = 0.0567 < 1/16.
4. **Lemma C (judge.md §2.3) on these curves (COMPUTED).**
   - Its first part holds everywhere: min Φ is always attained at a positive-slope traceless point or at a horizontal tangency (in reading B, at the jump of Φ there).
   - In reading B, its hypotheses (H_st) and (H_br) hold together in only 3 of the 48 (component, chirality) cases of `compact.md`: D₊(RHT)-mirror component 5, and D₋(RHT) component 5 in both chiralities. In reading A they also hold on KT/Conway components 1 and 3. Wherever they hold, conclusions (ii), (iv) and (v) hold.
   - Elsewhere the minimum usually sits at a **shallow** traceless point (slope 0.08 to 1.9) or at a horizontal tangency, and the lemma does not apply.
   - When (H_st) fails, the conclusions can fail:
     - (ii) fails for D₊(RHT)-mirror component 4 (G − Φ₀ = 0.046) and for D₋(RHT) component 4 (0.0375);
     - (v) fails for D₋(RHT) component 4 (d = 0.100 below the bound 0.105).

     Yet d_C stays at least 1/16 there.
   - **The judge's "nearest Y₋₂ generator" estimate is 0** on six Whitehead-double components. There the minimum of Φ is a shallow shared twisted point with Δc = 0. The full d_C on those components is still 0.085–0.125.

---

## 1. Method (COMPUTED)

**Representation curves.**
- **Groups.** Wirtinger presentations come from PD codes:
  - snappy's K11n42 and K11n34;
  - P(−3,5,7) as the numerator closure of 1/(−3) + 1/5 + 1/7. This is K15n113775, with Δ = 1, genus 1 and τ = +1.
  - Every Alexander polynomial was checked to be 1 by Fox calculus (`wirt.alexander`).
- **Parametrisation.** A representation sends each generator to cos θ + sin θ·u_i, with u_i a unit vector and θ = 2πα. A crossing imposes u_C = Rot(u_o, 2εθ) u_A. Gauge: u₀ = e_x, and the residual U(1) is quotiented out.
- **Calibration.** The sign of the relation and of the longitude word were fixed on the closure of the positive braid σ₁³. This gives the arc β = 1/2 − 6α of T(2,3), as in tk.py and seifert-1 (`calib.py`).
- **Seeds.**
  - Least-squares multistarts at 20 fixed values of α and at 4 fixed values of β (0, 1/4, 1/2, 3/4).
  - Every component of nonzero winding meets every horizontal line, and the fixed-α seeds catch the rest.
  - Every seed lies on a traced component ("seeds not on traced components: 0" in every run).
- **Tracing.** Pseudo-arclength continuation, with steps of at most 0.002 in the pillowcase and Newton correction to residual 10⁻¹².
- **Mirrors.** The mirror is computed from the same representations, with (α, β) ↦ (α, −β).

**Levels.**
- **Φ.** Φ_cont = ∫2δ dβ is integrated with Hermite–Simpson, using exact tangents.
- **Generators.** Each generator is refined by Newton on the representation variety, with Nα + β fixed.
- **Slopes.** Slopes are computed from the null vector of the Jacobian.
- **Flat stretches.** Where |dβ| < 10⁻⁷|dα|, the slope is set to 0 and read as 0⁻. Both readings then give Δc = 0 at such a point.
- **Lemma C.** Its hypotheses and conclusions are evaluated exactly as stated in judge.md, with Δv = 1/4 for both bundles (`levels.py`).

## 2. Validation of the pipeline (VERIFIED)

1. **Figure-eight knot, absolute values** (`fig8_check.out`). The constant is Φ = 3/16 at the turning point (1/6, 1/2). With it, the twelve generators give the values in the table, with worst error 1.1·10⁻⁷. Readings A and B agree, since |s| ≥ 4.47 everywhere. Also ∮2α dβ = 1 and ∮2δ dβ = 0 to 10⁻¹².

| | P₀ | P₁ |
|---|---|---|
| Y₂ | 19/80, 19/80 | 1/5, 3/10 |
| Y₋₂ | 11/80, 11/80 | 3/40, 7/40 |

2. **Torus knots** T(2,3), T(2,5), T(3,4), T(2,7) and their mirrors (`torus_check.out`).
   - These arcs end on the reducible line.
   - With one constant per arc, all generators of Y_{±2} in both bundles (8, 24, 40 and 48 per knot) match the exact Seifert values of tk.py. The worst error is 8.7·10⁻⁸.
   - For the positive knots, the constants found equal Φ at the arc's starting root: 5/16, 9/16, 13/16, as in seifert-1 Theorem 4.2. For the mirrors they are 3/8 minus these.
3. **Whitehead-double reduction** (`whd_cross_pRHT.out`, `whd_cross_mRHT.out`).
   - The curve of D(K) was computed as the image of {ρ_W on the Whitehead link : (α_A, β_A) on the swapped trefoil arc}, with μ_K = λ_A and λ_K = μ_A.
   - This was compared against the full 19- and 20-crossing diagrams of D₊(RHT) and D₋(RHT), built with spherogram and identified by τ = 1 and τ = 0.
   - The β-values agree exactly at α = 0.2 and 0.247 (D₊) and at α = 0.2 (D₋).
   - The full system has a 2-dimensional null space at fixed α, which is the bending circle.
4. **Consistency.**
   - Every closed component satisfies ∮2α dβ ∈ ℤ to 10⁻⁸ (Bohr–Sommerfeld).
   - In reading B, the level functions jump only at tangencies of slope −N, on every component of every knot (`jumpcheck.py`).

## 3. The ι rule

**(a) The notes' rule fails (VERIFIED).**
- **First failure: Δc at a shared point.** At a shared traceless point (β ∈ {0, 1/2}), Δc = c(Y₂) − c(Y₋₂) is mirror-invariant, because c(Y_N(K̄), x̄) = 3/8 − c(Y₋N(K), x). But the slope changes sign under mirroring.
  - The notes give Δc = 0 for s ∈ (−2, 0) and Δc = 1/4 for s ∈ (0, 2) (pillowcase-final F.3), which is impossible.
  - Any rule ι_N = f(N, s) must satisfy f(N, −s) = −f(−N, s).
- **Second failure: exact torus data.** Positive torus knots at N > pq carry an extra −1/8 (bigN.py). Transported to the mirror, this is an extra **+1/8** at N < −pq on branches of slope pq ∈ (0, −N). So there ι = −1, not +1 (`iota_mirror.out`; exact for T(2,3), T(2,5), T(3,4) at four values of N each).

**(b) The rule used here (PLAUSIBLE).** Take ι_N = sgn(N)·[s strictly between 0 and −N].
- Among linear combinations of triple indices of TC, TL_N, TL₀ and TL_∞, it is the unique rule that fits all torus-knot data in both chiralities. It reads (3/16) sgn N − ι_N/8 = (1/8) sgn N + τ(TC, TL_N, TL₀)/16.
- The reference line is L₀, the longitude direction, consistent with Φ = c(Y₀^w).
- Since τ jumps at s = 0 for both N, continuity of c under perturbations that slide a nondegenerate generator through a horizontal tangency forces Φ_true = Φ_cont + J. Here J drops by 1/8 from the s < 0 side to the s > 0 side.
- The bookkeeping is then self-consistent on every closed component computed: the J-jumps cancel exactly where ∮2δ dβ = 0.

**(c) Evidence from the Euler characteristic (COMPUTED; uses χ(I(Y_{±2}), P_i) = 0 for Δ_K = 1).**
- In reading A, every KT generator has ι = 0, so each component has a single grading parity.
- χ-twins have the same parity on P₀ (χ has degree 4).
- So χ(Y₂, P₀) = ±12 ± 8 ≠ 0. Reading A is inconsistent.
- In reading B, the parity flips across each horizontal tangency, and every component has Euler characteristic 0 in each bundle and for each N.

## 4. The curves

**KT 11n42 and Conway 11n34 (COMPUTED; the curves coincide to 10⁻³, the sampling step).**
- There are four components: two χ-pairs, (1,3) and (2,4).
- α ranges: [0.137, 0.361], [0.131, 0.331], [0.140, 0.363], [0.170, 0.369].
- Each component has winding 0, one cap, one cup, and four traceless crossings. The slopes there are +17.4, +3.07, −2.40, +1.42 on components 1 and 3, and +5.93, −23.9, +1.37, +5.46 on components 2 and 4.
- None of the traceless points is shared (β ∉ {0, 1/2}).
- Generators per component: Y₂ has (6, 6) in (P₀, P₁) and Y₋₂ has (4, 4).
- The smallest distance of a generator slope from ∓2 is 0.97, so all generators are nondegenerate. The smallest relative third singular value is 9·10⁻³, so there are no singular points.
- No perturbation is needed.

**D₊(RHT) and D₋(RHT) (COMPUTED).**
- The gluing system has six closed components. On two of them the companion parameter α_K leaves (1/12, 5/12): for D₊ they occupy [0, 1/23] and [10/23, 11/23]. These are not representations and are discarded.
- The valid components have companion bands [2k/23, (2k+1)/23] for D₊ and [(2k+1)/25, (2k+2)/25] for D₋, with k = 1, …, 4.
- Each valid component has winding ±2 and no horizontal tangency. It has two traceless crossings, both at the shared twisted point (1/4, 0), so ρ(λ) = 1.
- Shallow slopes occur there: 0.08, 0.34, 0.93 for D₊ and 0.28, 0.74, 1.73 for D₋.
- **Degeneracy and its perturbation.** Every point of C carries a circle of representations, from bending along the companion torus (PLAUSIBLE as an explanation; VERIFIED numerically as a 2-dimensional null space). So each generator of Y_{±2} is a Morse–Bott circle.
  - A small holonomy perturbation supported near the companion torus splits each circle into two generators, in adjacent degrees, at levels differing by 1/8.
  - Equivalently, it replaces C by two sheets whose constants differ by 1/8, with the same sign for N = ±2 because the shift comes from the exterior.
  - So every d_C is unchanged, and the Euler characteristic vanishes automatically (PLAUSIBLE).

**P(−3,5,7) (COMPUTED; degenerate).**
- **Curves.** Two χ-pairs of closed curves, (1,4) and (2,7), with winding ±2 and no horizontal tangencies. Their traceless crossings are shallow (slopes 1.4 to 1.9) or steep (−3.1, −6.6).
- **Flat loops.** Four flat loops, χ-invariant, lying on β = 0 over [0.108, 0.392], [0.150, 0.350], [0.141, 0.359] and [0.181, 0.319].
  - Plausible origin: bending in Y₀ along the capped genus-1 Seifert surface, which is free, so ρ(λ) = 1 while α moves.
  - Each loop meets one of the two χ-pairs at its fold points, which are singular points of R*(E) (relative third singular value about 10⁻⁵).
  - Components 9–15 of the run are duplicate tracings of loops 3, 5 and 6 (`dedupe.out`).
- **Generators on the flat loops.** Only the P₁ generators at (1/4, 0), two per loop. They are shared by Y₂ and Y₋₂ and nondegenerate, with slope 0 transverse to L^w_{±2}.
- **Effect of a perturbation.**
  - A generic perturbation resolves each singular crossing in one of two ways: the joining strand turns through negative or through positive slopes.
  - This changes the bookkeeping by δ ∈ {0, 1/8}: k_F − k_Γ = Φ_true^Γ(x) − Φ_true^F(x) + δ.
  - The cycle through Γ, χΓ and the two loops closes to 10⁻⁴ (`p357_cycle.out`), which confirms the χ-symmetric choice.
  - The resulting drops within each connected piece of R*(E) are in `p357_pieces.out`.

## 5. Levels, drops and Lemma C per component (reading B; `compact.md`; full tables in `tables.md`)

Columns:
- the minimum Φ₀ of Φ, with the type and slope of the point where it is attained;
- A = G_C(Y₂) − Φ₀;
- the Y₋₂ generator nearest the minimiser along C (c − Φ₀, with its slope);
- B = G_C(Y₋₂) − Φ₀;
- the judge's per-component estimate A − (nearest);
- d_C in reading B, and d_C in reading A;
- the Lemma C hypotheses, and its conclusions (ii), (iv), (v).

| knot | comp | Φ₀ at (slope) | A | nearest (slope) | B | A − nearest | **d_C (B)** | d_C (A) | H_st | H_br (s*) | (ii)(iv)(v) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| KT | 1, 3 | traceless (+1.42) | .0676 | −.0025 (+4.93) | −.0280 | .0702 | **.0956** | .1249 | yes | n/a | ok − − |
| KT | 2, 4 | traceless (+5.46) | .0689 | −.0498 (+6.94) | −.0498 | .1187 | **.1187** | .1187 | no | yes (5.32) | ok ok ok |
| KT mirror | 1, 3 | traceless (+2.40) | .0724 | −.0172 (−17.0) | −.0380 | .0897 | **.1105** | .0937 | yes | no (2.01) | ok − − |
| KT mirror | 2, 4 | horiz. tangency | .1391 | +.0620 (−0.06) | −.0482 | .0771 | **.1873** | .1751 | yes | n/a | ok − − |
| P(−3,5,7) | 1, 4 | traceless (+1.91) | .0635 | +.0068 (−6.62) | +.0068 | .0567 | **.0567** | .0567 | yes | n/a | ok − − |
| P(−3,5,7) | 2, 7 | traceless (+1.42) | .0723 | +.0332 (+1.50) | −.0918 | .0391 | **.1641** | .2891 | yes | n/a | ok − − |
| P(−3,5,7) | flat loops | constant | −.0625 | −.0625 (0) | −.0625 | 0 | **0** | 0 | yes | n/a | fails − − |
| P mirror | 1, 4 | traceless (+1.67) | .0727 | +.0002 (+63) | +.0002 | .0725 | **.0725** | .0725 | yes | n/a | ok − − |
| P mirror | 2, 7 | traceless (+3.08) | .0638 | −.0590 (+6.55) | −.0590 | .1228 | **.1228** | .1228 | no | yes (2.17) | ok ok ok |
| D₊(RHT) | 2 / 3 / 4 | traceless (+0.08 / +0.34 / +0.93) | .0625 | +.0625 (shared) | −.022 / −.046 / −.059 | **0** | **.0847 / .1081 / .1215** | .25 | yes | n/a | ok − − |
| D₊(RHT) | 5 | traceless (+2.35) | .0625 | −.0625 | −.0625 | .125 | **.125** | .125 | yes | no (2.35) | ok − − |
| D₊ mirror | 2, 3 | traceless (+4.18, +4.58) | .0625 | −.0625 | −.0625 | .125 | **.125** | .125 | no | yes | ok ok ok |
| D₊ mirror | 4 | traceless (+5.47) | **.0462** | −.0625 | −.0625 | .1087 | **.1087** | .1087 | no | yes (5.47) | **fails** ok ok |
| D₊ mirror | 5 | traceless (+7.97) | .0625 | −.0625 | −.0625 | .125 | **.125** | .125 | yes | yes (7.97) | ok ok ok |
| D₋(RHT) | 2, 3 | traceless (+4.15, +4.47) | .0625 | −.0625 | −.0625 | .125 | **.125** | .125 | no | yes | ok ok ok |
| D₋(RHT) | 4 | traceless (+5.14) | **.0375** | −.0625 | −.0625 | .100 | **.100** | .100 | no | yes (5.14) | **fails** ok **fails** |
| D₋(RHT) | 5 | traceless (+6.70) | .0625 | −.0625 | −.0625 | .125 | **.125** | .125 | yes | yes (6.70) | ok ok ok |
| D₋ mirror | 2 / 3 / 4 | traceless (+0.28 / +0.74 / +1.73) | .0625 | +.0625 (shared) | −.037 / −.055 / −.062 | **0** | **.0994 / .1176 / .1248** | .25 | yes | n/a | ok − − |
| D₋ mirror | 5 | traceless (+4.47) | .0625 | −.0625 | −.0625 | .125 | **.125** | .125 | yes | yes (4.47) | ok ok ok |

**Reading the table.**
- The 1/16 offsets of the formula show up exactly whenever the minimiser of Φ is a steep traceless point: A = 1/16 and nearest = −1/16, so d = 1/8.
- When the minimiser is a shallow shared point (λ ↦ 1, Δc = 0, reading B), the nearest Y₋₂ generator sits at +1/16. The per-component drop then comes from other Y₋₂ generators, 0.022–0.062 below Φ₀.
- KT and Conway have no shared points. Their minima sit on shallow branches or at horizontal tangencies, and d_C ranges over 0.096–0.187.

## 6. Answers to the questions of the task, knot by knot

| knot | C closed, avoids reducibles? | degenerate? | Lemma C hypotheses | generator-level both-bundle drop G(Y₂) − G(Y₋₂) (reading B) | positive? | ≥ 1/16? |
|---|---|---|---|---|---|---|
| KT 11n42 | yes; 4 curves, winding 0 | no | hold on no component in reading B (in reading A on components 1, 3 only) | in [0.0956, 0.1187]; mirror [0.1105, 0.1873] | yes | yes |
| Conway 11n34 | same curve as KT | no | same as KT | same as KT | yes | yes |
| P(−3,5,7) | yes, but with flat λ ↦ 1 loops | yes: flat loops and singular crossings | on no component (mirror 2, 7 satisfy H_br but not H_st) | per component in [0, 0.164]; mirror [0, 0.123]; with flat loops linked: one piece 0 or 0.057 (mirror 0 or 0.072) | **undecided** (0 not excluded) | **undecided** (0.057 < 1/16 on one χ-pair) |
| D₊(RHT) | yes; 4 curves, winding ±2 | yes: Morse–Bott bending circles (d unchanged by perturbation) | only mirror component 5 (and 2, 3 lack H_st) | [0.0847, 0.125]; mirror [0.1087, 0.125] | yes | yes |
| D₋(RHT) | yes; 4 curves, winding ±2 | yes: Morse–Bott bending circles | components 5 (both chiralities) | [0.100, 0.125]; mirror [0.0994, 0.125] | yes | yes |

## 7. Remarks

1. **Shared twisted traceless points do occur when Δ_K = 1 (COMPUTED).** In D_{±}(RHT) every traceless representation has λ ↦ 1 and lies at (1/4, 0). It is a generator of both Y₂ and Y₋₂ in P₁, but it is not binary dihedral. P(−3,5,7) has such points on its flat loops. BRIEF's remark that "such representations do not exist when det K = 1" is true of binary dihedral representations only.
2. **On shallow branches the pointwise gap at a shared point is Δc = 0** (reading B, for either sign of the slope), not 1/8. The four exact zeros in the "A − nearest" column come from this. The judge's per-component estimate built on the nearest Y₋₂ generator is therefore too weak whenever the minimiser is shallow and shared. The full d_C is what decides.
3. **A cruder obstruction for these knots (COMPUTED; given nondegeneracy).** The number of irreducible flat connections differs between Y₂ and Y₋₂:
   - KT and Conway: 48 against 32 (SU(2) count over both bundles, nondegenerate);
   - P(−3,5,7): 8 against 12 on P₀;
   - D_{±}: different numbers of Morse–Bott circles on P₁.

   So S³₂(K) ≇ S³₋₂(K) for these knots already by counting. This does not touch the general problem.
4. **Exact-looking values.** d = 1/8 exactly at steep shared minimisers; 0.1087 ≈ 5/46 and 0.100 = 1/10 for the Whitehead doubles. The 23 and 25 match the companion bands. I did not pursue exact forms.

## 8. Confidence and caveats

| claim | label | confidence |
|---|---|---|
| curves, generators, Φ_cont and relative levels (given the formula) | COMPUTED; pipeline VERIFIED on 4₁ and torus knots | 95% |
| the notes' ι is wrong in sign for N < 0 | VERIFIED (exact) | 97% |
| reading B (ι-rule plus the horizontal-tangency jump of Φ) | PLAUSIBLE (supported by mirror symmetry, torus data, continuity, and the Euler characteristic on KT) | 75% |
| the general pillowcase formula itself | PLAUSIBLE (as in pillowcase-final) | 70% |
| drops positive and ≥ 1/16 for KT, Conway, D_{±}(RHT) in both chiralities | COMPUTED given the formula; holds in both readings | 70% overall |
| Morse–Bott perturbation leaves d_C unchanged for D_{±} | PLAUSIBLE | 80% |
| P(−3,5,7) undecided; drop 0 possible at generator level | COMPUTED given the formula, plus PLAUSIBLE resolution bookkeeping at the singular points | 65% |

**What is not covered.**
- These are generator-level drops (G). Nothing here controls which generators survive in homology (statement (F) of judge.md).
- Component constants are never needed, because the bounds hold for all constants. For P(−3,5,7) they would be needed, together with the jumps at singular points, which I can only bracket.

## 9. Files (`r6/delta1-code/`)

| file | content |
|---|---|
| `wirt.py`, `fastsys.py`, `rep.py` | Wirtinger presentations from PD codes (knots and links), the quaternion system with analytic Jacobian, multistart, continuation |
| `seeds.py`, `pillow.py`, `analyze.py`, `levels.py` | component finding; Φ, J, slopes, generators and levels (readings A and B); Lemma C bookkeeping |
| `calib.py`, `fig8_check.py` / `.out`, `torus_check.py` / `.out` | calibration and validation (§2) |
| `iota_mirror.py` / `.out` | exact test of the sign of ι (§3a) |
| `run_knot.py`, `whd.py`, `whd_build.py`, `reanalyze.py` | drivers; `*_final.out` / `*_final.pkl` hold the final results per knot (both chiralities, every generator listed) |
| `whd_cross.py`, `whd_cross_[pm]RHT.out` | Whitehead double: gluing system against the full diagram |
| `summarize.py` → `tables.md`; `compact.py` → `compact.md` | all tables |
| `jumpcheck.py`, `singular.py` / `singular_P.out`, `dedupe.py` / `dedupe.out`, `p357_cycle.py` / `.out`, `p357_pieces.py` / `.out`, `degen.py` | consistency checks; the P(−3,5,7) degeneracy analysis |
| `solver.py` | the first (knot-only) solver, used by `calib.py` |
