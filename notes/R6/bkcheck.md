# Independent check of brieskorn.md (code: `r6/bkcheck/`, written from scratch)

## Method
**M1 (exact).** I derived the formula myself from the orbifold APS/G-signature theorem on the disk orbibundle W → S²(a₁,a₂,a₃):
- W is negative definite, so sign W = −1.
- The twisted signature vanishes.
- The cone point i has local action (ζ, ζ^{ν_i}), with ν_i = −b_i and Σ b_i a/a_i = +1.

This gives

  c = Σ_i (1/4a_i) Σ_k sin²(π l_i k/a_i) cot(πk/a_i) cot(πν_i k/a_i).

Each sum is evaluated exactly via the identity Σ_k cot·cot·e^{2πilk/a} = 4a Σ_m ((m/a))(((νm+l)/a)). The irreducibles are (ε, l₁, l₂, l₃), with the parities (−1)^{l_i} = ε^{b_i} and the strict spherical triangle inequality.

**M2.** This is Fintushel–Stern's own parametrisation: e by CRT from e ≡ l_i·a/a_i (mod a_i), local weight cot(πak/a_i²), direct float cot products. In those terms c = −S_FS(e)/8.

**Validation.**
- **Calibration.** The derived sign (ν = −b) reproduces all four values exactly: Σ(2,3,5) gives (CS, gr, c) = (1/120, 1, −7/60) and (49/120, 5, −13/60); Σ(2,3,7) gives 23/84 (CS 25/168, gr 7) and 29/84 (CS 121/168, gr 3). The opposite sign gives −c, which is not 3/8 − c, so this is a genuine test.
- **Reps checked.** 89,532 reps over 806 triples:
  - |M1 − M2| ≤ 8·10⁻¹⁵;
  - 8a·c ∈ ℤ for every rep;
  - a CS = e²/(4a) exists with 8(CS − c) an odd integer, and it was unique in the cases inspected;
  - the c-multiset does not change when the fibres are permuted;
  - the rep count N matches Brieskorn's signature count, N = −σ/4.
- **Convention flag.** In DLME's normalisation, CS = +e²/(4a) on link-oriented Σ, not FS's −e²/(4a). This has no effect on c.
- **Limitation.** M2 is an independent evaluation, not an independent theory. I did not implement a KKR splitting.

## Topology: CONFIRMED
- **Seifert algebra.** The filling μ + kλ₀ has |H₁| = 1 and Σb/a = 1/(P(a_K + kP)).
- **Slope sign.** The order-1 fibre of Σ(2,3,1) is the complex link of x² + y³, which is the RHT. So k = n ↔ slope −1/n.
- **Casson check.** I tested λ(sgn·Σ(…, a_K + nP, …)) = λ(Σ) − n(a_j² − 1)(a_k² − 1)/24, with λ = −N/2 on link-oriented Σ:
  - 6912 cases (n = ±1…±4, all fibres, including S³ = Σ(p,q,1));
  - 0 failures;
  - with the opposite slope sign the check passes only where Δ'' = 0.
- **Mirror rule.** (−Σ)_r = −Σ_{−r} is consistent.

## Verdicts
| # | Verdict | Evidence |
|---|---|---|
| 1 | **CONFIRMED** | All 9 values match exactly. ℓ(Y_{+1/n}) for K = 7 also matches: 59/120, 209/520, 389/920. |
| 2 | **CONFIRMED** | 821 L+ families (383 with base a > 2000; base a up to 59,878; Y up to a ≈ 5.7·10⁶). (a) never fails; ℓ is strictly decreasing for n = 0…5 (n = 0…4 in the large-a sample); min T₁ = 1/8 exactly, at K = 17 ⊂ Σ(3,5,17), K = 23 ⊂ Σ(3,7,23), K = 47 ⊂ Σ(3,11,47), K = 71 ⊂ Σ(3,23,71) and K = 119 ⊂ Σ(3,13,119). Also, in 574 L− families, (a) holds and T₁ ≥ 1/8. |
| 3 | **MOSTLY; overstated** | 686 R− families. "(a) fails for 2P < a_K < 4P" is **not universal**: it fails in 314/320 (see below). T₁ ≥ 1/8 ⇔ a_K < 3P holds in all 686. For a_K > 4P, 0 < T₁ < 1/8 in all 179. Both examples reproduce: 209/520, 59/120, 11/70, and T₁ = −9/8. The value −9/8 is **not** the global minimum (see below). |
| 4 | **CONFIRMED with the stated exception** | 1141 chains, details below. |
| 5 | **CONFIRMED** | 24 (p,q) pairs (pq up to 132) × n = 1…6: 144 exact matches. |
| 6 | **CONFIRMED for n ≥ 1; false if the base step counts** | Details below. |

### Claim 3 details
- **Exceptions to (a)** (6 of 320):
  - band 2P–3P: K = 95 ⊂ −Σ(2,17,95) and K = 169 ⊂ −Σ(3,23,169);
  - band 3P–4P: K = 113 ⊂ −Σ(2,15,113), K = 263 ⊂ −Σ(2,35,263), K = 82 ⊂ −Σ(3,7,82) and K = 145 ⊂ −Σ(3,14,145).
- **Smaller T₁.** I found T₁ = −411/176 at K = 233 ⊂ −Σ(7,11,233), and −9/4 at K = 227 ⊂ −Σ(3,25,227). Both bases have a > 5000, outside brieskorn.md's range.

### Claim 4 details
- **Data:**
  - 51 chains with P ≤ 110 and j ≤ 20, including torus exteriors;
  - 150 chains with P ∈ [100, 300] and j ≤ 6;
  - 250 chains with P ∈ [200, 600] and j ≤ 4;
  - every residue r for (3,77), (3,64), (2,101), (5,41), (4,49) and (7,29), with j ≤ 3.
- **β.** β is taken from the minimiser's holonomy along the **core** c = x_K^u h^v, with u ≡ −P (mod m): β = |2(l_K·P mod m) − m|.
- **Result.** ℓ = A* − (m² − β²)/(16Pm) holds from j = 0, with A* the same on both classes and β constant per class. The two-step drop formula holds.
- **Convention matters.** Using the holonomy of x_K instead (β = |2l − m|) fails in 51/51 chains.
- **Only exception: (3,77; 211) at m = 442.**
  - The actual minimisers are a tied pair, l = 210 and 232, both with β = 222. Their own β gives A* = −1025/1848, not −1027/1848.
  - ℓ is 1/68068 below the β₁ = 226 prediction.
  - T = 76761/544544 ≠ 997/7072, but it is still > 1/8.
  - The formula holds again from m = 673 on.

### Claim 6 details
- **Bound.** D ≥ m_n/(16 m_{n+1}) holds with 0 violations: 6589 family windows (382 equalities) and 4975 chain windows.
- **Links between β classes.** β(class of r) ≤ β(other class) in all 1141 chains.
- **D > 1/24 for n ≥ 1.** This holds in every L+ family. The minimum I found is 477/11447 ≈ 0.0416703, at K = 2 ⊂ Σ(2,35,109), n = 2. That is below 625/14998 for Σ(2,17,147), which I reproduce, so the latter is not the extremal case beyond a ≤ 5000; the values tend to 1/24.
- **Base step fails.** The step ℓ(Σ) − ℓ(Y_{−1}) does **not** exceed 1/24. Examples: 1/20008 at K = 2 ⊂ Σ(2,17,147) and 1/30536 at K = 2 ⊂ Σ(2,35,109). Both equal the m₀/(16m₁) bound.

## Files
- `bkc.py`: library.
- `validate.py`, `cscheck.py`, `calib.py`: validation.
- `topo.py`: topology checks.
- `claim1.py`, `torus.py`: claims 1 and 5.
- `famscan*.py`, `rscan.py`, `analyze.py`: families, with output in `fam*.json` and `rfam.json`.
- `chains*.py`, `anchains.py`: chains, with output in `chains*.json`.
