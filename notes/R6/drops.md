# Drops of ℓ between ±1/n surgeries on torus knots

Setting and normalisation are those of BRIEF.md. K is T(p,q) (p,q > 0) or its mirror mT(p,q), Y_r = S³_r(K), c(α) = CS~ − gr~/8 = (3 + ρ(α))/16, and ℓ(Y) is DLME's invariant.

Labels: **PROVED**, **COMPUTED** (exact rational arithmetic, code saved), **PLAUSIBLE**, **SPECULATIVE**.

Code and outputs are in `r6/drops-code/`:
- `brieskorn.py`: flat connections, levels c, CS and gradings on ±Σ(a₁,a₂,a₃);
- `validate.py` with `validate.out`;
- `compute.py` with `tables.txt` (the full tables, including T(2,11) and T(4,5)) and `data.json` (every generator);
- `summary.py` with `summary.out`, and `closedform.out`;
- `fs_e_test.py`, the calibration of the Chern–Simons convention.

## 1. Method and validation (COMPUTED)

**Identification of the manifolds.** Brieskorn spheres carry their link orientation.
- S³_{−1/n}(T(p,q)) = Σ(p,q,pqn+1).
- S³_{+1/n}(T(p,q)) = −Σ(p,q,pqn−1).
- S³_r(mT) = −S³_{−r}(T).

**Flat connections.** I use the Fintushel–Stern presentation ⟨x_i, h | x_i^{a_i} h^{b_i}, x₁x₂x₃⟩ with Σ b_i a/a_i = 1.
- SU(2) irreducibles correspond to data (ε, l₁, l₂, l₃) with (−1)^{l_i} = ε^{b_i} that satisfy the triangle condition.
- The level is c = S/4 on Σ and c = 3/8 − S/4 on −Σ, where S = Σ_i (1/a_i) Σ_k cot(πk/a_i) cot(πβ_i k/a_i) sin²(πl_i k/a_i) and the β_i are the Seifert invariants with e = −1/a.
- The Chern–Simons value is CS = e²/(4a), with e b_i ≡ ±l_i (mod 2a_i), and gr = 8(CS − c).

**Checks.** All of the following pass (`validate.out`):
1. **DLME Example 3.7.** Σ(2,3,5) has (CS, gr) = (1/120, 1) and (49/120, 5), with c = −7/60 and −13/60 (ρ = −73/15 and −97/15).
2. **Σ(2,3,7) = S³_{−1}(RHT) = S³_{+1}(4₁).** The Casson invariants agree (λ = −1). We get (CS, gr, c) = (25/168, 7, 23/84) and (121/168, 3, 29/84), which matches Fintushel–Stern's CS values.
3. **Independent cross-check.** For Y_{±1} of all nine positive torus knots, both chiralities, the full multisets (c, gr mod 8) agree exactly with the independent pillowcase code `gap16/ell-code` (18 manifolds, 0 mismatches).
4. **Casson count.** #R*(Y_{±1/n}) = n(p²−1)(q²−1)/12.
5. **DLME's Lemma (n-surgery-calc) holds as ℤ/8-graded spaces.** I(Y_{−1/n}) = ⊕_{i<n} I_{*−2i}(Y_{−1}) and I(Y_{1/n}) = ⊕_{i<n} I_{*+2i}(Y_1), for n ≤ 5.
6. **Gradings.** Every Y has all its gradings of one parity, so the differential vanishes and ℓ(Y) = min_α c(α).

## 2. The values ℓ(Y_r) (COMPUTED, exact)

| K | Y_{+1} | Y_{+1/2} | Y_{+1/3} | Y_{+1/4} | Y_{+1/5} | Y_{−1} | Y_{−1/2} | Y_{−1/3} | Y_{−1/4} | Y_{−1/5} |
|---|---|---|---|---|---|---|---|---|---|---|
| T(2,3) | 59/120 | 131/264 | 203/408 | 275/552 | 347/696 | 23/84 | 8/39 | 8/57 | 23/300 | 5/372 |
| mT(2,3) | 5/168 | 17/312 | 29/456 | 41/600 | 53/744 | −13/60 | −17/66 | −35/102 | −109/276 | −163/348 |
| T(2,5) | 179/360 | 379/760 | 579/1160 | 779/1560 | 979/1960 | 17/55 | 31/140 | 103/620 | 39/410 | 19/510 |
| mT(2,5) | −91/440 | −151/840 | −211/1240 | −271/1640 | −331/2040 | −41/90 | −187/380 | −337/580 | −41/65 | −173/245 |
| T(2,7) | 363/728 | 755/1512 | 1147/2296 | 1539/3080 | 1931/3864 | 137/420 | 93/406 | 107/602 | 55/532 | 95/1988 |
| mT(2,7) | −379/840 | −687/1624 | −995/2408 | −1303/3192 | −1611/3976 | −255/364 | −139/189 | −237/287 | −1347/1540 | −1837/1932 |
| T(2,9) | 611/1224 | 1259/2520 | 1907/3816 | 2555/5112 | 3203/6408 | 115/342 | 311/1332 | 73/396 | 71/657 | 44/819 |
| mT(2,9) | −955/1368 | −1783/2664 | −2611/3960 | −3439/5256 | −4267/6552 | −145/153 | −1237/1260 | −2047/1908 | −1433/1278 | −1919/1602 |
| T(3,4) | 263/528 | 551/1104 | 839/1680 | 1127/2256 | 1415/2832 | 199/624 | 271/1200 | 307/1776 | 235/2352 | 127/2928 |
| mT(3,4) | −61/156 | −109/300 | −157/444 | −205/588 | −253/732 | −169/264 | −373/552 | −643/840 | −919/1128 | −1261/1416 |
| T(3,5) | 419/840 | 869/1740 | 1319/2640 | 1769/3540 | 2219/4440 | 79/240 | 857/3720 | 62/345 | 767/7320 | 113/2280 |
| mT(3,5) | −17/30 | −497/930 | −361/690 | −947/1830 | −293/570 | −49/60 | −2947/3480 | −113/120 | −6997/7080 | −16/15 |
| T(3,7) | 839/1680 | 1721/3444 | 2603/5208 | 3485/6972 | 4367/8736 | 631/1848 | 1703/7224 | 1009/5376 | 1577/14280 | 505/8904 |
| mT(3,7) | −155/168 | −3217/3612 | −4729/5376 | −6241/7140 | −7753/8904 | −197/168 | −8287/6888 | −109/84 | −18745/13944 | −239/168 |

**Order (COMPUTED, in all 18 cases).** ℓ(Y_{−1/5}) < ℓ(Y_{−1/4}) < ℓ(Y_{−1/3}) < ℓ(Y_{−1/2}) < ℓ(Y_{−1}) < ℓ(Y_1) < ℓ(Y_{1/2}) < … < ℓ(Y_{1/5}). This is DLME's chain. ℓ(Y_1) − ℓ(Y_{−1}) > 1/8 in every case.

**Closed forms on the positive side** (COMPUTED for n = 1, …, 5 and all knots listed):
- ℓ(S³_{1/n}(T(p,q))) = 1/2 − 1/(4pq(pqn−1)).
- ℓ(S³_{1/n}(mT(p,q))) = A_K − c_K²/(4pq(pqn+1)).
  - c_K² = 9, 25, 49, 81, 121 for mT(2,q) with q = 3, 5, 7, 9, 11, so c_K = q.
  - c_K² = 36, 64, 121, 100 for mT(3,4), mT(3,5), mT(3,7), mT(4,5).
  - A_K = 1/12, −3/20, −11/28, −23/36, −39/44, −1/3, −1/2, −6/7, −69/80 for mT(2,3), mT(2,5), mT(2,7), mT(2,9), mT(2,11), mT(3,4), mT(3,5), mT(3,7), mT(4,5) (from `closedform.out`).
- In both families the minimiser keeps a fixed Fintushel–Stern invariant e and a fixed grading as n varies, so the level varies only through CS = e²/(4a).

## 3. Drops (COMPUTED)

Notation:
- D_n⁻ = ℓ(Y_{−1/n}) − ℓ(Y_{−1/(n+1)}) is the one-step drop on the negative side.
- T_n = ℓ(Y_{−1/n}) − ℓ(Y_{−1/(n+2)}) is the two-step drop.
- D_1⁺ = ℓ(Y_{1/2}) − ℓ(Y_1) is the first drop on the positive side.

| K | D_1⁻ | D_2⁻ | D_3⁻ | D_4⁻ | T_1 | ℓ(Y_1)−ℓ(Y_{−1}) | ℓ(Y_{1/2})−ℓ(Y_{−1/2}) | D_1⁺ |
|---|---|---|---|---|---|---|---|---|
| T(2,3) | 25/364 ≈ .0687 | 16/247 ≈ .0648 | .0637 | .0632 | .1335 | 61/280 ≈ .2179 | .2911 | 1/220 |
| mT(2,3) | 9/220 ≈ .0409 | 16/187 ≈ .0856 | .0518 | .0735 | .1265 | 69/280 ≈ .2464 | .3121 | 9/364 |
| T(2,5) | 27/308 ≈ .0877 | 12/217 ≈ .0553 | .0710 | .0579 | .1430 | 149/792 ≈ .1881 | .2773 | 1/684 |
| mT(2,5) | 25/684 ≈ .0366 | 49/551 ≈ .0889 | .0497 | .0754 | .1255 | 197/792 ≈ .2487 | .3123 | 25/924 |
| T(2,7) | 169/1740 ≈ .0971 | 64/1247 ≈ .0513 | .0744 | .0556 | .1484 | 269/1560 ≈ .1724 | .2703 | 1/1404 |
| mT(2,7) | 49/1404 ≈ .0349 | 100/1107 ≈ .0903 | .0489 | .0762 | .1252 | 389/1560 ≈ .2494 | .3124 | 49/1740 |
| T(2,9) | 289/2812 ≈ .1028 | 20/407 ≈ .0491 | .0763 | .0543 | .1519 | 421/2584 ≈ .1629 | .2661 | 1/2380 |
| mT(2,9) | 81/2380 ≈ .0340 | 169/1855 ≈ .0911 | .0484 | .0766 | .1251 | 645/2584 ≈ .2496 | .3125⁻ | 81/2812 |
| T(3,4) | 121/1300 ≈ .0931 | 49/925 ≈ .0530 | .0729 | .0565 | .1460 | 205/1144 ≈ .1792 | .2733 | 1/1012 |
| mT(3,4) | 9/253 ≈ .0356 | 289/3220 ≈ .0898 | .0492 | .0758 | .1253 | 285/1144 ≈ .2491 | .3124 | 9/325 |
| T(3,5) | 49/496 ≈ .0988 | 289/5704 ≈ .0507 | .0749 | .0552 | .1495 | 19/112 ≈ .1696 | .2690 | 1/1624 |
| mT(3,5) | 7/232 ≈ .0302 | 11/116 ≈ .0948 | .0466 | .0784 | **1/8** | **1/4** | .3124 | 1/31 |
| T(3,7) | 50/473 ≈ .1057 | 529/11008 ≈ .0481 | .0773 | .0537 | .1538 | 139/880 ≈ .1580 | .2640 | 1/3280 |
| mT(3,7) | 5/164 ≈ .0305 | 31/328 ≈ .0945 | .0467 | .0783 | **1/8** | **1/4** | .3125⁻ | 11/344 |

The full pairwise table, including all ℓ(Y_a) − ℓ(Y_b) for a, b ∈ {±1, …, ±1/5}, can be read off §2. All values are in `tables.txt`.

## 4. Lower bounds: what the data say

### (a) One-step drops on the positive side: no bound other than 0 (COMPUTED + PROVED from the closed form)
- For positive torus knots, ℓ(Y_{1/(n+1)}) − ℓ(Y_{1/n}) = 1/(4(pqn−1)(pq(n+1)−1)) exactly. This tends to 0 as pq → ∞, for example 1/3612 for T(2,11) at n = 1.
- So no knot-independent positive bound exists.
- The drop is a pure difference of Chern–Simons values, e²/(4pq)·(1/a₃ − 1/a₃′), at fixed grading. That is an energy, with no topological term.
- This matches correction 1: the cobordisms Y_{1/(n+1)} → Y_{1/n} in DLME's map W ⊕ (W,c) are simply connected and negative definite, so only η > 0 is available.

### (b) One-step drops on the negative side, D_n⁻: no bound other than 0 is suggested
- The minimum of D_1⁻ = ℓ(Y_{−1}) − ℓ(Y_{−1/2}) is 7/232 ≈ 0.0302, at mT(3,5).
- The candidates fail:
  - 1/(8n(n+1)) = 1/16 at n = 1 fails for every mirror knot (all values lie in [0.030, 0.041]);
  - 1/32 fails (7/232 and 5/164 are smaller).
- For mirror torus knots the one-step drops alternate small/large and look like they converge as pq grows (PLAUSIBLE, from the trends in mT(2,q)): roughly 1/32, 3/32, 3/64, 5/64 for n = 1, 2, 3, 4. Each consecutive pair sums to about 1/8.
- The single-handle cobordism W_n: Y_{−1/n} → Y_{−1/(n+1)} is simply connected with b⁺ = 0, so its level is exactly −η. No topological term is available.
- Its least reducible energies are 0 (c even) and 1/4 (c odd). The data lie strictly between them, so that energy does not explain the drop either.

### (c) The suggested bound is on the two-step drop: T_n = ℓ(Y_{−1/n}) − ℓ(Y_{−1/(n+2)}) ≥ 1/8 (COMPUTED evidence; SPECULATIVE as a theorem)
- It holds in all 54 cases (18 knots, n = 1, 2, 3).
- **Equality holds exactly** for mT(3,5) and mT(3,7) at n = 1 and n = 3:
  - mT(3,5): ℓ(Y_{−1}) = −49/60, ℓ(Y_{−1/3}) = −113/120, ℓ(Y_{−1/5}) = −16/15;
  - mT(3,7): ℓ(Y_{−1}) = −197/168, ℓ(Y_{−1/3}) = −109/84, ℓ(Y_{−1/5}) = −239/168.
- Equality never occurs at n = 2. The minimum there is T_2 = 223/1780, at T(2,11).
- For mirror knots T_1 → 1/8 from above (0.1265, 0.1255, 0.1252, 0.1251, 0.12509 for mT(2,q)).
- By orientation reversal (ℓ⁺(Y) = 3/8 − ℓ(−Y)), the statement is equivalent to ℓ⁺(Y_{1/(n+2)}) − ℓ⁺(Y_{1/n}) ≥ 1/8 for the mirror knot. This dual form also holds in the data. The ℓ version fails on the positive side, by (a).
- **This is DLME's 1/8 one step further along.** The slopes −1/n and −1/(n+2) are at distance 2, and their middle slopes are −1/(n+1) and 0. DLME's theorem ℓ(Y_{−1}) < ℓ(Y_1) − 1/8 is the case of the pair (1/m, 1/(m+2)) with m = −1, whose middle slope is ∞.

**Explanation through the level formula (PLAUSIBLE as bookkeeping).**
- Let X_n = W_n ∪ W_{n+1}: Y_{−1/n} → Y_{−1/(n+2)}. Its intersection form is −I₂ and b⁺ = 0.
- It contains the sphere S = (cocore of the first handle) ∪ (core of the second handle), glued along the dual knot. S has square −2 and ∂νS = ℝP³.
- For a bundle that is odd on S, either of the following gives an f-shift of −1/8 − E, with E ≥ 0:
  - a count on X_n∖νS whose ℝP³ middle end carries the rotation-by-π flat connection, which has w₂ ≠ 0, h = 1, ρ = 0 and so contributes (3 − h + ρ)/16 = 1/8;
  - equivalently, DLME's one-parameter family stretched along ℝP³, with i₀ = −1, degree 3 and level 1/4 − η.
- The constant 1/8 is the non-energy term. The odd ℝP³ cap has least energy 1/8.

**Gap.** The argument above is not a proof.
- For (Y, K) = (Y_{−1/(n+1)}, dual knot), the distance-two triangle has middle term I(Y_{−1/(n+1)})², which is nonzero.
- The ranks are nr, 2(n+1)r and (n+2)r. So the triangle is short exact, the top map is 0, and the g-type map G_n: C(Y_{−1/n}) → C(Y_{−1/(n+2)}) is only the null-homotopy of F′∘F, not a chain map.
- An injective map with level −1/8 is therefore not available from DLME as stated.

**Equality cases (SPECULATIVE).**
- Correction 1 says an exact drop needs a zero-energy contribution on a cobordism that is not simply connected.
- Van Kampen gives π₁(X_n∖νS) = π₁(E_K)/⟨⟨γ_{−1/n}, γ_{−1/(n+2)}⟩⟩. A representation killing both slopes has 2b ∈ ℤ and a ≡ nb in the pillowcase coordinates, so it is central on μ and reducible.
- So no flat connection on X_n∖νS joins two irreducibles, and the equality cannot come from there.
- What the four equality cases share: on both ends the minimiser has l₃ = a₃/2. The exceptional fibre of multiplicity a₃, which is the dual knot, is sent to an element of order 4 in SU(2) (rotation by π in SO(3), traceless holonomy). That is exactly the holonomy of the ℝP³ end above.
- So the extremisers sit in the traceless theory of the dual knot. This parallels the brief's finding that 1/16 is attained through traceless (binary dihedral) minimisers.
- The equality occurs only for n odd. I have not identified the zero-energy configuration that realises it.

### (d) The other candidates
- **ρ(L(n,1))/16.** For Y_{−1/n} = Σ(p,q,pqn+1) the third Seifert invariant is β₃ = n. By reciprocity, the third cone-point term is a quadratic expression plus an L(n,1)-type Dedekind sum, and this is how L(n,1) enters the values. But no one-step bound of that form is supported: at n = 1 it would be 0 or 1/16, and the data contradict any positive constant near 1/16.
- **The only lens term the data support is ℝP³ = L(2,1)**, with the value 1/8, and it appears for the two-step pair.
- **Cross drops.**
  - ℓ(Y_1) − ℓ(Y_{−1}) ∈ (1/8, 1/4]. The value 1/4 is attained (mT(3,5), mT(3,7)), matching the ℝP³ upper bound in ell-1.
  - ℓ(Y_{1/2}) − ℓ(Y_{−1/2}) ∈ [0.2634, 5/16). Mirror knots approach 5/16 from below.

## 5. Uncertain or open
- **Is the two-step bound T_n ≥ 1/8 true for all knots?** The evidence is torus knots only, with equality attained. A proof needs an injective (or suitably filtered) map of level −1/8 despite the nonzero middle term. Confidence that the statement is true in general: about 40–50%.
- **The one-step limits** (about 1/32, 3/32, 3/64, 5/64 for mirror knots) are extrapolations from five knots and have no closed form yet.
- **Coverage.** Only torus knots were computed. Correction 2 warns that the differential is nonzero in general; here it vanishes by parity.
