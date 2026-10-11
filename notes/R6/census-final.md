# Knots with both ±2 surgeries Seifert fibred: final census

Labels: **VERIFIED** means established by exact or interval computation and cross-checked by a second method or an independent earlier computation; **COMPUTED** means obtained by one method (floating point, or exact but not cross-checked); **PLAUSIBLE** means supported by evidence but not proved.

Notation: Y_r = S^3_r(K), mK is the mirror of K, and S^3_r(mK) = -S^3_{-r}(K). So "Y_{+2} and Y_{-2} are both Seifert fibred" is a property of K up to mirror image, and each table entry is one test.

## 1. Answer

Search range: all 313,230 prime knots with at most 15 crossings (SnapPy HTLinkExteriors, one entry per knot up to mirror image), and all 3,116 knots of SnapPy's census of knot exteriors with at most 10 ideal tetrahedra.

Within this range, K has both S^3_{+2}(K) and S^3_{-2}(K) Seifert fibred exactly when K is one of the following.

1. **A torus knot with crossing number at most 15**, in either chirality (11 knots, 22 oriented knots): T(2,3), T(2,5), T(2,7), T(2,9), T(2,11), T(2,13), T(2,15), T(3,4), T(3,5), T(3,7), T(4,5). Each was identified by its fibres: Y_{±2}(T(p,q)) has exceptional fibres p, q, |pq ∓ 2|. The invariants are in §5.
2. **The figure-eight knot**, which occurs twice in the range (K4a1, and the census knot K2_1). The invariants are in §6.

**There are no others.** No hyperbolic knot other than 4_1 and no satellite knot in the range has both ±2 surgeries Seifert fibred. So nothing new needed its flat connections computed. The level code was still validated on 4_1 and on the Poincaré sphere (§6).

**Status.**
- VERIFIED for every knot with at most 14 crossings and for every census knot.
- For the 15-crossing knots, every survivor of the filter was settled rigorously. The exclusion of the other hyperbolic 15-crossing knots is VERIFIED (interval arithmetic) for all 5,032 knots whose larger slope length is at most 12 and for a 1-in-50 sample of the rest, 9,997 knots in all. For the remaining 243,282 knots, whose floating-point slope length exceeds 12, it is COMPUTED (§3).
- No knot in the range is unresolved.

## 2. Normalisation

- c(alpha) = (3 + rho(alpha))/16 for an irreducible flat SO(3) connection alpha. Here rho is the APS rho-invariant of the odd signature operator twisted by ad(alpha).
- This is checked against DLME's example: on Σ(2,3,5), oriented as the boundary of the negative definite E8 plumbing, the code gives rho = -73/15 and -97/15, so c = -7/60 and -13/60. These are DLME's 1/120 - 1/8 and 49/120 - 5/8 (VERIFIED).
- For a Seifert fibred Y_{±2} there are no differentials, so lambda_0 is the least c over the flat connections of the trivial bundle P_0 (w_2 = 0), and lambda_1 the least over P_1 (w_2 ≠ 0).
- untwisted gap u = lambda_0(Y_2) - lambda_0(Y_{-2});
- twisted gap w = lambda_1(Y_2) - lambda_1(Y_{-2});
- m_1 = lambda_0(Y_2) - lambda_1(Y_{-2});
- m_2 = lambda_1(Y_2) - lambda_0(Y_{-2});
- both-bundle drop = min(lambda_0, lambda_1)(Y_2) - min(lambda_0, lambda_1)(Y_{-2}).

**Seifert notation.** M(e_0; (a_1,b_1), (a_2,b_2), (a_3,b_3)), with 0 < b_i < a_i, is the boundary of the star-shaped plumbing with central weight e_0 and arms a_i/b_i = [k_1, k_2, ...] with weights -k_j. Its Euler number is e = e_0 + Σ b_i/a_i, and the plumbing is negative definite exactly when e < 0. Reversing orientation gives -M = M(-e_0 - 3; (a_i, a_i - b_i)).

## 3. Search and filter

**6-theorem filter.**
- If both S^3_{±2}(K) are exceptional, then both slopes ±2 have length at most 6 on the maximal cusp (Agol, Lackenby, with geometrisation).
- Floating-point pass: every one of the 316,346 exteriors was scanned (SnapPy 3.3.2, snappy_15_knots 1.2.1, SnapPea-kernel maximal cusp).
  - The previous run had stopped short in two blocks of 15-crossing knots, indices 197,514–199,999 and 247,657–249,999 (4,829 knots). These were scanned now. They contain no survivor, and the 15-crossing table is complete (253,293 entries, no errors).
  - 122 entries survive: either both lengths are at most 6.2, or the exterior has no positively oriented solution (21 non-hyperbolic knots).
- Interval pass (vscan.py, SnapPy verified cusp translations on a verified embedded cusp):
  - All 63,053 exteriors with at most 14 crossings, plus all census knots: 62,964 excluded rigorously, 76 candidates and 13 non-hyperbolic, with no failures. Every interval survivor is also a floating-point survivor. VERIFIED.
  - 15 crossings (new in this run). The 253,285 hyperbolic 15-crossing knots fall into three groups:
    - 6 survive the floating-point filter: K15a78880, K15a84969, K15a85234, K15n51748, K15n112479 and K15n115375. Both fillings of each are verified hyperbolic (§4).
    - 5,032 have floating-point max(|λ+2μ|, |λ−2μ|) in (6.2, 12]. All of them were interval-verified, and all are rigorously excluded. VERIFIED.
    - 248,247 have max length greater than 12. A systematic sample of 4,965 of them (every 50th by name) was interval-verified, and all are excluded.
  - In total 9,997 of the 15-crossing knots carry a verified exclusion. The other 243,282 rest on floating-point lengths of at least 12 = 2 × 6. COMPUTED.
  - On the 9,997 verified knots, the verified lower bound (on an embedded, not necessarily maximal, cusp) is always at least 0.699 times the floating-point maximal-cusp length. So a floating-point length of 12 or more corresponds in practice to a verified bound above 8.
  - A full interval pass over the 15-crossing table (about 253,000 knots at 5 to 15 knots per second per process on the shared CPUs) was not run. It is the one remaining step for a fully verified census.
- The floating-point and interval lengths agree to the printed precision (5·10^{-7}) wherever both were computed on the maximal cusp.

## 4. The 122 survivors and how each was settled

Each filling was examined with census-code/analyse_knot.py:
- SnapPy verify_hyperbolicity, with interval Newton, falling back to a drill-and-refill triangulation when needed;
- Regina 7.4 StandardTriangulation recognition, which is exact but only up to orientation;
- for Seifert fillings, orientation by the Casson–Walker invariant, lambda_W(S^3_{±2}(K)) = ±Delta_K''(1)/2. Exactly one orientation of the model matched in every case.

Non-hyperbolic exteriors were then certified by new scripts in census-code2/ (sat_check.py, graph_cert.py).

| outcome | entries |
|---|---|
| both fillings Seifert fibred | 13 (the 11 torus knots, K4a1, K2_1) |
| both fillings verified hyperbolic | 76 |
| one filling verified hyperbolic | 23 |
| graph-manifold filling, not Seifert | 4 (K13n4587, K13n4639, K15n40211, K15n124802; 2-cables of the trefoil) |
| filling with an incompressible torus and a verified hyperbolic piece | 6 (K14n22180, K14n26039, K15n59184, K15n115646, K15n142188, K15n156076) |

The per-knot table is in families/census.md §4 and in families/census-code2/survivor_table.md.

**Graph manifolds (VERIFIED).**
- Regina recognises S^3_{±2} of K13n4587, K13n4639 and K15n40211 as unions SFS[D: (2,1)(3,1)] ∪_m SFS[D: (2,1)(n,1)]. Here n = 12 and 16 for K13n4587, 8 and 12 for K13n4639, and 16 and 20 for K15n40211, for +2 and -2 respectively.
- Regina's convention is (f_1, o_1)^T = m (f_0, o_0)^T. The matrices are [-3,5 | -1,2], [-5,7 | -2,3] and [-1,3 | 0,1]. So the fibre f_1 of one piece meets the fibre f_0 of the other 5, 7 and 3 times respectively; it is never ±f_0.
- Both pieces have unique Seifert fibrations: they lie over the disc with two exceptional fibres, not of type (2,2).
- H_1 = Z/2 rules out horizontal tori. So these fillings are not Seifert fibred.
- An independent check that does not use the gluing matrix: a Seifert fibration would put the exceptional fibres 2, 3, 2, n over S^2, and n is even, so there would be three even fibres. That contradicts H_1 = Z/2, as for K15n124802 below.

**K15n124802 (new, VERIFIED).**
- Its exterior has volume 0 and Alexander polynomial Δ_{T(2,3)}(t^2)·Δ_{T(2,3)}(t). This points to the 2-cable C_{2,±3} of the trefoil (PLAUSIBLE as an identification), but the certificate below does not use that identification.
- In a triangulation of each filling, a normal torus cuts N into two pieces recognised by Regina:
  - Y_{+2}: SFS[D: (2,1)(3,-2)] and SFS[D: (2,1)(4,-3)];
  - Y_{-2}: SFS[D: (2,1)(3,-2)] and SFS[D: (2,1)(8,-7)].
- Suppose N were Seifert fibred. The torus would be vertical, since H_1 is finite and so there are no horizontal tori, and the fibrations of the pieces are unique. So N would be Seifert fibred over S^2 with exceptional fibres 2, 3, 2, 4 (resp. 2, 3, 2, 8).
- A Seifert space over S^2 with k ≥ 1 fibres of even multiplicity has H_1(N; Z/2) = (Z/2)^{k-1}. Here k = 3, which contradicts H_1(N) = Z/2.

**Satellites with hyperbolic patterns (VERIFIED, at least one side each).**
- These are four knots whose exteriors have volume 3.6639 (the Whitehead-link volume; their Alexander polynomials are those of twisted Whitehead doubles) and two with volume 5.3336.
- In each certified filling, a normal torus cuts it into the trefoil exterior SFS[D: (2,1)(3,-2)] and a piece that SnapPy verifies hyperbolic, of volume 2.6667 or 5.03–5.22. So the torus is incompressible and the filling has a hyperbolic JSJ piece; it is not Seifert fibred.
- Certified slopes: K14n22180 at -2; K14n26039 at +2; K15n59184 at +2; K15n115646 at -2; K15n142188 at both ±2; K15n156076 at both ±2.

## 5. Torus knots (VERIFIED)

**Identification and orientation.**
- In each row, Y_{+2} has exceptional fibres p, q, |pq - 2| and Y_{-2} has p, q, |pq + 2|, where pq < 0 for the negative knots. This identifies the knot.
- Orientations come from Casson–Walker. They agree with the independent pillowcase table (gap16/ell-code/data_table.txt) in every row, both chiralities.
- K3a1 is the left-handed trefoil T(2,-3). K5a2, K7a7, K8n3, K9a41, K10n21, K11a367, K13a4878, K14n21881, K15a85263 and K15n41185 are the positive torus knots.

All levels are in the normalisation of §2.

| knot | table entry | Y_{+2} | Y_{-2} | λ0(Y_2) | λ1(Y_2) | λ0(Y_{-2}) | λ1(Y_{-2}) | untwisted | twisted | m_1 | m_2 | both-bundle drop |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T(2,3) | mirror of K3a1 | M(-1; (2,1), (3,1), (4,1)) | M(-1; (2,1), (3,1), (8,1)) | 23/48 | 13/24 | 37/96 | 7/24 | 3/32 | 1/4 | 3/16 | 5/32 | 3/16 |
| T(2,5) | K5a2 | M(-1; (2,1), (5,2), (8,1)) | M(-1; (2,1), (5,2), (12,1)) | 79/160 | 13/20 | 37/80 | 19/60 | 1/32 | 1/3 | 17/96 | 3/16 | 17/96 |
| T(3,4) | K8n3 | M(-1; (3,2), (4,1), (10,1)) | M(-1; (3,2), (4,1), (14,1)) | 119/240 | 161/240 | 163/336 | 109/336 | 3/280 | 97/280 | 6/35 | 13/70 | 6/35 |
| T(2,7) | K7a7 | M(-1; (2,1), (7,3), (12,1)) | M(-1; (2,1), (7,3), (16,1)) | 167/336 | 115/168 | 225/448 | 37/112 | -1/192 | 17/48 | 1/6 | 35/192 | 1/6 |
| T(3,5) | K10n21 | M(-1; (3,1), (5,3), (13,1)) | M(-1; (3,1), (5,3), (17,1)) | 97/195 | 269/390 | 1039/2040 | 679/2040 | -21/1768 | 631/1768 | 291/1768 | 319/1768 | 291/1768 |
| T(2,9) | K9a41 | M(-1; (2,1), (9,4), (16,1)) | M(-1; (2,1), (9,4), (20,1)) | 287/576 | 101/144 | 379/720 | 61/180 | -9/320 | 29/80 | 51/320 | 7/40 | 51/320 |
| T(4,5) | K15n41185 | M(-1; (4,3), (5,1), (18,1)) | M(-1; (4,3), (5,1), (22,1)) | 359/720 | 509/720 | 471/880 | 301/880 | -29/792 | 289/792 | 31/198 | 17/99 | 31/198 |
| T(3,7) | K14n21881 | M(-1; (3,2), (7,2), (19,1)) | M(-1; (3,2), (7,2), (23,1)) | 199/399 | 283/399 | 2083/3864 | 1327/3864 | -141/3496 | 1279/3496 | 543/3496 | 595/3496 | 543/3496 |
| T(2,11) | K11a367 | M(-1; (2,1), (11,5), (20,1)) | M(-1; (2,1), (11,5), (24,1)) | 439/880 | 313/440 | 191/352 | 91/264 | -7/160 | 11/30 | 37/240 | 27/160 | 37/240 |
| T(2,13) | K13a4878 | M(-1; (2,1), (13,6), (24,1)) | M(-1; (2,1), (13,6), (28,1)) | 623/1248 | 28/39 | 807/1456 | 127/364 | -37/672 | 31/84 | 101/672 | 55/336 | 101/672 |
| T(2,15) | K15a85263 | M(-1; (2,1), (15,7), (28,1)) | M(-1; (2,1), (15,7), (32,1)) | 839/1680 | 607/840 | 1081/1920 | 169/480 | -57/896 | 83/224 | 33/224 | 143/896 | 33/224 |
| T(2,-3) | K3a1 | M(-2; (2,1), (3,2), (8,7)) | M(-2; (2,1), (3,2), (4,3)) | -1/96 | -1/24 | -5/48 | -1/6 | 3/32 | 1/8 | 5/32 | 1/16 | 1/8 |
| T(2,-5) | mirror of K5a2 | M(-2; (2,1), (5,3), (12,11)) | M(-2; (2,1), (5,3), (8,7)) | -61/240 | -11/40 | -59/160 | -2/5 | 11/96 | 1/8 | 7/48 | 3/32 | 1/8 |
| T(3,-4) | mirror of K8n3 | M(-2; (3,1), (4,3), (14,13)) | M(-2; (3,1), (4,3), (10,9)) | -37/84 | -11/24 | -67/120 | -7/12 | 33/280 | 1/8 | 1/7 | 1/10 | 1/8 |
| T(2,-7) | mirror of K7a7 | M(-2; (2,1), (7,4), (16,15)) | M(-2; (2,1), (7,4), (12,11)) | -225/448 | -29/56 | -209/336 | -9/14 | 23/192 | 1/8 | 9/64 | 5/48 | 1/8 |
| T(3,-5) | mirror of K10n21 | M(-2; (3,2), (5,2), (17,16)) | M(-2; (3,2), (5,2), (13,12)) | -319/510 | -319/510 | -1169/1560 | -1109/1560 | 219/1768 | 151/1768 | 151/1768 | 219/1768 | 219/1768 |
| T(2,-9) | mirror of K9a41 | M(-2; (2,1), (9,5), (20,19)) | M(-2; (2,1), (9,5), (16,15)) | -541/720 | -55/72 | -503/576 | -8/9 | 39/320 | 1/8 | 11/80 | 7/64 | 1/8 |
| T(4,-5) | mirror of K15n41185 | M(-2; (4,1), (5,4), (22,21)) | M(-2; (4,1), (5,4), (18,17)) | -79/80 | -859/880 | -89/80 | -791/720 | 1/8 | 97/792 | 1/9 | 3/22 | 1/8 |
| T(3,-7) | mirror of K14n21881 | M(-2; (3,1), (7,5), (23,22)) | M(-2; (3,1), (7,5), (19,18)) | -949/966 | -949/966 | -3533/3192 | -3533/3192 | 435/3496 | 435/3496 | 435/3496 | 435/3496 | 435/3496 |
| T(2,-11) | mirror of K11a367 | M(-2; (2,1), (11,6), (24,23)) | M(-2; (2,1), (11,6), (20,19)) | -1057/1056 | -89/88 | -989/880 | -25/22 | 59/480 | 1/8 | 13/96 | 9/80 | 1/8 |
| T(2,-13) | mirror of K13a4878 | M(-2; (2,1), (13,7), (28,27)) | M(-2; (2,1), (13,7), (24,23)) | -1821/1456 | -131/104 | -1715/1248 | -18/13 | 83/672 | 1/8 | 15/112 | 11/96 | 1/8 |
| T(2,-15) | mirror of K15a85263 | M(-2; (2,1), (15,8), (32,31)) | M(-2; (2,1), (15,8), (28,27)) | -2881/1920 | -181/120 | -2729/1680 | -49/30 | 111/896 | 1/8 | 17/128 | 13/112 | 1/8 |

**Checks against the brief.**
- Positive torus knots, n = pq: the untwisted gap equals -1/8 + (2n-5)/(n^2-4) and the twisted gap equals 3/8 - 4/(n^2-4) in every row, and m_1, m_2 ∈ (1/8, 3/16].
- Negative torus knots: the untwisted gap lies in [3/32, 1/8], the twisted gap and m_1 have least value 151/1768 ≈ 0.0854 (at T(3,-5)), and m_2 has least value 1/16 (at T(2,-3)).
- The smallest both-bundle drop is 219/1768 = 1/8 - 1/884, at T(3,-5).

## 6. The figure-eight knot (VERIFIED)

**Invariants.**
- Y_{+2} = M(-1; (2,1), (4,1), (5,1)), with e = -1/20; it bounds the negative definite plumbing (-1; -2, -4, -5).
- Y_{-2} = -Y_{+2} = M(-2; (2,1), (4,3), (5,4)), with e = +1/20.
- Casson–Walker: lambda_W(Y_{+2}) = -1 = Delta''(1)/2, and the reversed orientation would give +1.
- This agrees with the Chern–Simons orientation of fig8-A. Both table entries (K4a1 and K2_1) give the same result.

**Flat connections.** Each connection is labelled by the SU(2) angle numerators l, giving angles pi·l_i/a_i.

| Y | l | bundle | rho | c = (3+rho)/16 |
|---|---|---|---|---|
| Y_{+2} | (1,1,2) | P_0 | 4/5 | 19/80 |
| Y_{+2} | (1,2,1) | P_1 (binary dihedral) | 1/5 | 1/5 |
| Y_{+2} | (1,2,2) | P_1 (binary dihedral) | 9/5 | 3/10 |
| Y_{-2} | (1,1,2) | P_0 | -4/5 | 11/80 |
| Y_{-2} | (1,2,2) | P_1 | -9/5 | 3/40 |
| Y_{-2} | (1,2,1) | P_1 | -1/5 | 7/40 |

**Levels.**
- lambda_0(Y_2) = 19/80, lambda_1(Y_2) = 1/5, lambda_0(Y_{-2}) = 11/80, lambda_1(Y_{-2}) = 3/40.
- untwisted gap 1/10, twisted gap 1/8, m_1 = 13/80, m_2 = 1/16, both-bundle drop 1/8.

These are the validation values of the brief, reproduced exactly. 4_1 is amphichiral, so the mirror gives the same row.

**Why the code's list of flat connections is complete.** The code assumes ad(h) = 1 for the regular fibre h, and this is justified as follows.
- Suppose an irreducible SO(3) representation had ad(h) ≠ 1. Its image would lie in the centraliser of ad(h), which is O(2). No generator q_i can then be a reflection: for a_i odd, q_i^{a_i} = q_i is not a power of a rotation, and for a_i even, gcd(a_i, b_i) = 1 forces b_i odd.
- So the image would be abelian. Hence every irreducible SO(3) representation on Y_{±2} factors through the (a_1,a_2,a_3) triangle group, which is what the code enumerates.

## 7. Other knots

None in the search range. In particular:
- the 2-cables of the trefoil fail on both sides;
- the satellites with hyperbolic patterns fail on at least one side;
- every hyperbolic survivor other than 4_1 has at least one ±2 filling that is verified hyperbolic.

**Hyperbolic knots with exactly one Seifert filling.** Six such knots occur. Each appears in both tables: K6a3 = K4_1, K7a4 = K4_2, K8a11 = K5_2, K8n1 = K5_12, K9a27 = K5_3 and K10a75 = K6_1, with isometries checked by SnapPy.
- Their Seifert filling is always of type (2, 4, n), with n = 9, 11, 13, 9, 15, 17.
- They are twist-knot-like, and their other ±2 filling is verified hyperbolic. COMPUTED.

## 8. Unresolved cases

**None of the cases in the search range is unresolved.** In nine entries one filling stayed unidentified, but the other filling settles the question each time.

**Census knots.** For K6_8, K8_22, K9_261, K9_63 and K10_81, SnapPy finds no positively oriented solution for one filling and Regina does not recognise it. The other filling is verified hyperbolic in every case. In particular, S^3_{-2}(K9_261) is verified hyperbolic, so K9_261 is excluded.

**Satellites.** For K14n22180, K14n26039, K15n59184 and K15n115646, the side without a certificate is presumably the slope at which the Whitehead-pattern filling is exceptional (PLAUSIBLE; not checked). The other side carries the hyperbolic-piece certificate.

## 9. Confidence and caveats

**Overall.** High confidence in the final list within the stated range.

**Rigour.** All exclusions of survivors are rigorous:
- interval-verified hyperbolicity, or
- exact Regina recognition together with the JSJ arguments above.

All Seifert identifications are exact, and all levels are exact rational arithmetic.

**15-crossing hyperbolic knots.**
- The only non-rigorous step is the 6-theorem exclusion of hyperbolic 15-crossing knots outside the interval-verified set.
- Those knots have a slope of floating-point length greater than 12 on the maximal cusp, against a threshold of 6.
- On every knot where both passes ran, the floating-point and interval values agree to 5·10^{-7}. COMPUTED, and very likely correct.

**Orientations.**
- They rest on Casson–Walker together with the Lescop-type formula for Seifert spaces.
- They were cross-checked on the Poincaré sphere, on 4_1 (by Chern–Simons, in fig8-A) and on all 22 oriented torus knots (against the pillowcase computation). VERIFIED.

**Scope.**
- Knots with more than 15 crossings are covered only through the census, that is, knots whose exteriors have at most 10 tetrahedra.
- The explanation in families/census.md §8 for why so few knots qualify (both slopes short forces a small cusp) is PLAUSIBLE only beyond the range.

## 10. Files

All paths are under scratchpad/families.

- **New code** (census-code2/):
  - survivors.py: the survivor list;
  - sat_check.py: the hyperbolic-piece certificate;
  - graph_cert.py: the graph-manifold certificate;
  - graph_recognise.py;
  - final_table.py and torus_md.py: levels;
  - survivor_table.py: the per-knot table.
- **New output:**
  - scan-out/HT15_197514.csv and HT15_247657.csv;
  - analysis-out/batch_r6.jsonl;
  - sat-out/sat2.jsonl and graph_cert.jsonl;
  - vscan-out/HT15_near9_*.csv and HT15_vlist_*.csv;
  - census-code2/final_table.txt, torus_table.md and survivor_table.md.
