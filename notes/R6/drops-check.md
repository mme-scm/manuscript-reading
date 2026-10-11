# Independent check of r6/drops.md

Checker's own code is in `r6/check-code/`. None of `drops-code/` was used. Only its outputs (`data.json` and the tables in drops.md) were read, for comparison.

Normalisation: BRIEF.md, c = CS~ − gr~/8 = (3+ρ)/16, and ℓ = least c of a nonzero class.

**Verdict.**
- Every number in drops.md that I recomputed is correct.
- Claims 1, 2 and 4 are confirmed. Claim 2 is confirmed only as evidence, and it extends: equality is generic for mirrors of odd–odd torus knots.
- Claim 3 is correct only on the 18-knot sample. Its upper end, 0.107, is not a bound.
- One interpretive remark in §2 is wrong (see 4.1); it does not affect any number.

## 1. Method (own implementation)

`fs.py` does the following.

**Representations.**
- The presentation is ⟨x_i, h | x_i^{a_i} h^{b_i}, x₁x₂x₃⟩ with Σ b_i a/a_i = 1.
- The irreducibles are the tuples (ε, l₁, l₂, l₃) with 0 < l_i < a_i and (−1)^{l_i} = ε^{b_i}, and with a strict spherical triangle inequality on the angles πl_i/a_i.
- For each irreducible, the Fintushel–Stern integer e is found by CRT from e·b_i ≡ ±l_i (mod 2a_i). Then e² mod 4a is well defined.

**Fintushel–Stern data.**
- CS = e²/(4a) mod 1.
- Σ_FS(e) = Σ_i (2/a_i) Σ_k cot(πak/a_i²) cot(πk/a_i) sin²(πek/a_i).
- gr = 2e²/a + Σ_FS(e) mod 8.

**The real level is c = −Σ_FS(e)/8.** I derived this independently of FS as an APS ρ-invariant on the orbifold mapping cylinder W of Σ → S²(a₁,a₂,a₃):
- sign W = −1;
- ad α factors through the triangle group, so it extends flatly over W;
- H*(W; ad α) = 0, so sign_{ad α}(W) = 0.

Hence ρ = −3 + Σ_i (4/a_i) Σ_k sin²(πkl_i/a_i) cot(πk/a_i) cot(−πkb_i/a_i). The substitution k → b_i k turns this into −3 − 2Σ_FS.

**Exact evaluation and internal checks.**
- Both expressions are evaluated exactly, using the identity Σ_k cot(πk/m) cot(πkb/m) cos(2πkl/m) = 4m Σ_j ((j/m))(((bj+l)/m)).
- For every representation the two expressions agree identically.
- For every representation, 2e²/a + Σ_FS is an exact integer. This is the check that ties CS to c.
- The c-multiset is invariant under permuting the fibres and under changing b_i.
- The exact sums agree with floating-point sums to 2e−13.

**Manifolds.**
- S³_{−1/n}(T(p,q)) = Σ(p,q,pqn+1).
- S³_{+1/n}(T(p,q)) = −Σ(p,q,pqn−1).
- S³_r(mT) = −S³_{−r}(T).
- On −Σ: c → 3/8 − c, CS → −CS, gr → −3 − gr.

**Orientation check.** For every Y computed (18 knots, n ≤ 7, both signs):
- λ := ½ Σ_α (−1)^{gr(α)} equals ±n·a₂(K), with a₂ = (p²−1)(q²−1)/24. This is the Casson surgery formula.
- #R* = n(p²−1)(q²−1)/12.
- All gradings have one parity, so the differential is 0 and ℓ = min c.

## 2. Validation

- **Σ(2,3,5), link orientation.** (CS, gr, c) = (1/120, 1, −7/60) and (49/120, 5, −13/60), with ρ = −73/15 and −97/15. This is exactly DLME's example.
- **Σ(2,3,7) = S³_{−1}(RHT) = S³_{+1}(4₁).** (CS, gr, c) = (25/168, 7, 23/84) and (121/168, 3, 29/84). The real lift is reproduced, not only c mod 1: 23/84 = CS − gr/8 + 1.

## 3. Recomputed values ℓ(Y_r)

| K | Y_1 | Y_{1/2} | Y_{1/3} | Y_{−1} | Y_{−1/2} | Y_{−1/3} |
|---|---|---|---|---|---|---|
| T(2,3) | 59/120 | 131/264 | 203/408 | 23/84 | 8/39 | 8/57 |
| mT(2,3) | 5/168 | 17/312 | 29/456 | −13/60 | −17/66 | −35/102 |
| T(2,5) | 179/360 | 379/760 | 579/1160 | 17/55 | 31/140 | 103/620 |
| mT(2,5) | −91/440 | −151/840 | −211/1240 | −41/90 | −187/380 | −337/580 |
| T(3,4) | 263/528 | 551/1104 | 839/1680 | 199/624 | 271/1200 | 307/1776 |
| mT(3,4) | −61/156 | −109/300 | −157/444 | −169/264 | −373/552 | −643/840 |
| T(3,5) | 419/840 | 869/1740 | 1319/2640 | 79/240 | 857/3720 | 62/345 |
| mT(3,5) | −17/30 | −497/930 | −361/690 | −49/60 | −2947/3480 | −113/120 |

**Agreement with drops.md.**
- All 140 entries of the drops.md §2 table (14 knots × slopes ±1, …, ±1/5) agree with mine.
- Against `drops-code/data.json`, all 180 manifolds agree: the Brieskorn triple, the orientation, and the full generator lists (9480 generators), compared as multisets of (c, CS mod 1, gr mod 8). There are 0 mismatches.
- **§3 drop table.** Every entry agrees: D₁⁻ through D₄⁻, T₁, ℓ(Y₁)−ℓ(Y₋₁), ℓ(Y_{1/2})−ℓ(Y_{−1/2}) and D₁⁺. There is one rounding slip: for mT(2,5), D₁⁻ = 25/684 ≈ 0.03655, printed as .0366.
- **§1 checks 4–6 hold.** These are the Casson count, the graded DLME lemma (both signs, n ≤ 5, 18 knots, 0 mismatches) and the parity check.
- **DLME's results hold for n ≤ 7.** These are the chain ℓ(Y_{−1/7}) < … < ℓ(Y_{1/7}) and the inequality ℓ(Y_{−1/n}) < ℓ(Y_{1/n}) − 1/8.

## 4. The four claims

**4.1 Closed form ℓ(Y_{1/n}(T(p,q))) = 1/2 − 1/(4pq(pqn−1)). CONFIRMED.**
- It holds exactly for the 9 knots with n ≤ 10, and for all 141 positive torus knots with pq ≤ 160 at n = 1, 2.
- The minimiser is the e = 1 representation, with gr = 4 on −Σ, for every n. So "fixed e and fixed grading" is right for this family.
- The mirror closed form A_K − c_K²/(4pq(pqn+1)) also fits for n ≤ 7, with the same A_K and c_K² as drops.md.
- **Error.** The sentence "In both families the minimiser keeps a fixed Fintushel–Stern invariant e and a fixed grading" is false for the mirror family:
  - for mT(2,3), the minimiser has e = 12n − 1, and its CS is not ≡ −9/(4a) mod 1;
  - for mT(4,5), the minimiser's grading alternates between {2,6} (n odd) and {0,4} (n even);
  - there are two tied minimisers for mT(3,5) and mT(3,7) when n ≥ 2, and for mT(4,5) at every n.

  This is a remark only; no value changes.

**4.2 Two-step bound T_n = ℓ(Y_{−1/n}) − ℓ(Y_{−1/(n+2)}) ≥ 1/8. CONFIRMED as evidence, and it holds more widely.**
- It holds in drops.md's 54 cases, in 18 knots × n ≤ 8, and in 282 knots (all torus knots with pq ≤ 160, both chiralities) × n ≤ 3. There are no violations.
- Equality holds for mT(3,5) and mT(3,7) at n = 1 and 3. It also holds at n = 5 and 7.
- **Equality is not special to these two knots.** It holds for every mirror torus knot with p and q both odd in the scan (38 knots, for example mT(3,11), mT(5,7), mT(7,9), mT(9,11) and mT(11,13)), at every odd n tested.
- In each equality case:
  - the minimiser on Y_{−1/n}, n odd, has l₃ = a₃/2 (checked);
  - ℓ(Y_{−1/n}) = ℓ(Y_{−1}) − (n−1)/16 for odd n.
- The inequality is strict whenever p or q is even.
- The claim min T₂ = 223/1780 (T(2,11)) is correct for the sample. Over the wide scan, T₂ decreases towards 1/8 without reaching it (T(5,32): 34295/274348 ≈ 0.12501).

**4.3 Range [7/232, 0.107] for D₁⁻ = ℓ(Y_{−1}) − ℓ(Y_{−1/2}). CORRECT ONLY ON THE SAMPLE.**
- Over the 18 knots, the minimum is 7/232 ≈ 0.03017 (mT(3,5)) and the maximum is 49/460 ≈ 0.1065 (T(2,11)).
- The lower end persists over all 282 knots.
- The upper end does not. D₁⁻ grows with pq for positive knots: T(3,8) 0.1080, T(5,12) 0.1179, T(5,32) 0.1223. So 0.107 is a sample maximum, not a bound.

**4.4 Range (1/8, 1/4] for ℓ(Y₁) − ℓ(Y₋₁). CONFIRMED.**
- On the sample the actual range is [605/3864 ≈ 0.1566, 1/4].
- Over the 282 knots:
  - the minimum is 0.1296 (T(5,32)), and the values decrease towards 1/8 for large positive knots;
  - the maximum is exactly 1/4, attained by every odd–odd mirror torus knot and never exceeded.
- Two related ranges:
  - for ℓ(Y_{1/2}) − ℓ(Y_{−1/2}), the bound < 5/16 holds on the wide scan, but the lower end 0.2634 is a sample value (0.2519 for T(5,32));
  - for the mirror knots, D₁⁻ ∈ [0.030, 0.041] is confirmed.

## 5. Suggested corrections to drops.md

1. The equality statement in §4(c) should read: equality for mirrors of odd–odd torus knots, at all odd n tested. Correspondingly, ℓ(Y₁) − ℓ(Y₋₁) = 1/4 holds for the same knots.
2. Delete or restrict the "fixed e and fixed grading" sentence in §2 to positive knots.
3. Present [7/232, 0.107] and [0.2634, 5/16) as sample ranges. Only the lower end of the first range and the upper end of the second survive the wide scan.
4. Change .0366 to .0365 for mT(2,5) D₁⁻.

The non-numerical parts of drops.md (the level-formula explanation, the gap, and the van Kampen argument) were not re-derived here.

**Files** (all in `r6/check-code/`):

| File | Contents |
|---|---|
| `fs.py`, `fastT.py` | formulas |
| `validate.out` | validation |
| `compute.out`, `ell_table.json` | tables and Casson checks |
| `claims.out`, `claims2.out` | claims |
| `cmp_data.out` | generator-level comparison |
| `wide160.out` | wide scan |
| `oddodd.out` | odd–odd equality pattern |
| `minimisers.out` | e and gr of the minimisers |
| `extra2.out` | n ≤ 10 checks |
