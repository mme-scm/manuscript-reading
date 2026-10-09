# Knots whose +2 and -2 surgeries are both Seifert fibred: a census search

**Scope.** As the user asked, only the census search was done. The family-by-family theoretical analysis was dropped. That analysis would have covered satellites and cables in general, and the Brittenham–Wu, pretzel, Eudave-Muñoz, Miyazaki–Motegi and twisted torus families. Torus knots and satellite knots that occur in the tables were handled computationally, like every other entry.

**Notation.**
- Y_{±2} = S^3_{±2}(K), and mK is the mirror of K.
- Since S^3_r(mK) = -S^3_{-r}(K), the property "Y_{+2} and Y_{-2} are both Seifert fibred" does not change under mirroring. Each table entry is therefore one test.
- Levels are in the absolute normalisation of the task: f^abs(alpha) = rho_APS(ad alpha)/16 for every irreducible flat SO(3) connection alpha.
- ell^abs (trivial bundle) and ell^{w,abs} (w_2 ≠ 0) are the minima of f^abs over the connections of the relevant bundle. Taking the minimum is valid because Seifert fibred spaces have no differentials.
- u, w, m1, m2 and mingap are as defined in the task.

## 1. Results

[[RESULTS]]

## 2. Search range

- **HT knots.** SnapPy 3.3.2 with snappy_15_knots 1.2.1 gives HTLinkExteriors: all prime knots with at most 15 crossings, one entry per knot up to mirror image. That is 313,230 knots. By crossing number 3, 4, ..., 15 the counts are 1, 1, 2, 3, 7, 21, 49, 165, 552, 2,176, 9,988, 46,972 and 253,293.
- **Census knots.** SnapPy's CensusKnots holds 3,116 knot exteriors with ideal triangulations of at most 10 tetrahedra (K2_1, ..., K10_1849). These include the 1,267 census knots with at most 9 tetrahedra that Dunfield treats in "A census of exceptional Dehn fillings" (arXiv:1812.11940). Many of them have more than 15 crossings, and their exteriors are the simplest, which is where exceptional surgeries concentrate.
- **Dunfield's data.** His census of exceptional fillings could not be obtained. The data sits on dataverse.harvard.edu and on Dunfield's web pages, and the egress proxy refuses both hosts (HTTP 403). Only the paper could be read. Its statement that all 1,143 nontrivial Seifert fibred fillings of the 1,267 census knots are integral, of type S^2(q1,q2,q3) or RP^2(q1,q2), is consistent with what is found here.

**Peripheral curves.** The search needs (first curve, second curve) = (meridian, Seifert longitude) for every exterior.
- **Meridian check.** It was checked that the (1,0) filling is S^3: SnapPy simplifies pi_1 to the trivial group, or Regina's 3-sphere recognition succeeds. This was done for every knot with at most 13 crossings, every 10th knot with 14 crossings, every 50th knot with 15 crossings, and all 3,116 census knots. There were no failures.
- **Longitude check.** It was checked that H_1 of the (0,1) filling is Z. This holds for every HT knot.
- **Census longitudes repaired.** For 1,782 census knots, mostly the 10-tetrahedron ones, the stored second curve is lambda + k mu with k ≠ 0, and |k| goes up to about 500. For these the basis was reset to (mu, lambda), with k read off from H_1 of the (0,1) and (1,1) fillings (census-code/periph.py).
- **Consequence.** Without this repair the census part of the search would have tested the wrong slopes.

## 3. The filter (6-theorem)

**The criterion.**
- Let mu be the meridian translation (a complex number) and lambda the longitude translation on the maximal cusp of a hyperbolic exterior. The slope ±2 = ±2 mu + lambda then has length |lambda ± 2 mu|.
- By the 6-theorem (Agol; Lackenby; with geometrisation), a slope of length greater than 6 on an embedded cusp gives a hyperbolic filling, which in particular is not Seifert fibred.
- So K is excluded as soon as one of |lambda + 2mu| and |lambda - 2mu| is greater than 6.
- The filter uses actual lengths on the cusp. Normalised length ≥ 6 implies actual length > 6 here, so this filter is stronger than the one in the task and still rigorous.

**Floating-point pass (all knots; census-code/scan.py).**
- The SnapPea kernel computes the maximal cusp (displacement equal to the stopping displacement).
- Every entry with a positively oriented solution is kept in the hyperbolic list. Entries without one after 40 randomisations are listed separately in §5.
- Knots with both lengths ≤ 6.2 go to §4.

**Interval pass (census-code/vscan.py, run under passagemath 10.8 so that SnapPy's verified methods are available).**
- SnapPy verifies the hyperbolic shapes (logarithmic gluing equations and positivity, with interval arithmetic).
- It computes interval translations of an embedded cusp: first the triangulation-dependent cusp, then, if that cusp is too small, the maximal one.
- A knot is excluded when the lower end of one of the two length intervals exceeds 6.
- Coverage: [[VERIFIED-COVERAGE]]

## 4. Survivors and their fillings

For each survivor, each of the two fillings was examined in three ways (census-code/analyse_knot.py):
- **Hyperbolicity.** SnapPy's verify_hyperbolicity was run on the filled manifold, with interval Newton on the gluing and filling equations.
  - If SnapPy's triangulation of the filling has negatively oriented tetrahedra, a short geodesic is drilled, the original filling is made permanent, and the new cusp is refilled along its meridian. This gives another triangulation of the same closed manifold, which is then verified; H_1 was checked to agree.
  - A positive result is VERIFIED.
- **Regina recognition.** Regina 7.4's StandardTriangulation recognition was run on up to 300 randomised and simplified triangulations of the filling. Recognition is exact, but only up to orientation.
- **Closed-census identification.** SnapPy's identify() against the closed census was used only as a label.

**When a knot is excluded.** A knot is excluded when one of its fillings is verified hyperbolic, or when it is recognised as a graph manifold whose JSJ torus does not match the Seifert fibres. Such a manifold is not Seifert fibred:
- Both pieces are Seifert fibred over the disc with two exceptional fibres, not (2,2), so each fibration is unique.
- The gluing matrix does not send fibre to ±fibre.
- H_1 = Z/2 is finite, so there are no horizontal tori.

**Orientation of the two fillings.** When both fillings are recognised as small Seifert spaces, the orientation is fixed by the Casson–Walker invariant:
- On the knot side, Walker's formula gives lambda_W(S^3_{±2}(K)) = ±Delta_K''(1)/2, because lambda_W(L(±2,1)) = -s(±1,2) = 0.
- On the Seifert side, Lescop's formula gives lambda_W(M(e0; (a_i,b_i))) = -(2 - n + sum a_i^{-2})/(12 e) - e/12 + sgn(e)/4 + sum s(b_i,a_i). This formula was fitted in fig8-B and checked here on lens spaces, on the Poincaré sphere and on all the torus knots in §7.
- The code accepts an orientation only when exactly one of ±lambda_W(model) equals the knot value. This happened in every case.

[[SURVIVORS]]

## 5. Non-hyperbolic entries of the tables

[[NONHYP]]

## 6. The figure-eight knot

The census finds 4_1 twice, as K4a1 and as K2_1, and both runs agree.

**Seifert invariants with orientations (VERIFIED).**
- Y_{+2} = M(-1; (2,1), (4,1), (5,1)), which in Regina's name is SFS [S2: (2,1) (4,1) (5,-4)]. Its Euler number is e = -1/20 and H_1 = Z/2.
  - It is the boundary of the negative definite plumbing (-1; -2, -4, -5).
  - Casson–Walker: lambda_W = -1 = Delta''(1)/2, since Delta''(1) = -2. The reversed orientation would give +1.
- Y_{-2} = -Y_{+2} = M(-2; (2,1), (4,3), (5,4)), with e = +1/20 and lambda_W = +1.
- This agrees with the orientation that fig8-A obtained independently by Chern–Simons matching (notes/G-fig8.md).

**Flat SO(3) connections.** Each is labelled by the normalised SU(2) angle numerators l (angles pi l_i/a_i, adjoint rotation 2 pi l_i/a_i). All values are exact.

| Y | l | bundle | rho_APS(ad) | f^abs |
|---|---|---|---|---|
| Y_{+2} | (1,1,2) | w_2 = 0 | 4/5 | 1/20 |
| Y_{+2} | (1,2,1) | w_2 ≠ 0 (dihedral D5 image) | 1/5 | 1/80 |
| Y_{+2} | (1,2,2) | w_2 ≠ 0 (dihedral D5 image) | 9/5 | 9/80 |
| Y_{-2} | (1,1,2) | w_2 = 0 | -4/5 | -1/20 |
| Y_{-2} | (1,2,2) | w_2 ≠ 0 | -9/5 | -9/80 |
| Y_{-2} | (1,2,1) | w_2 ≠ 0 | -1/5 | -1/80 |

**Levels.**
- ell^abs(Y_{+2}) = 1/20 and ell^{w,abs}(Y_{+2}) = 1/80.
- ell^abs(Y_{-2}) = -1/20 and ell^{w,abs}(Y_{-2}) = -9/80.

These give:

| quantity | value |
|---|---|
| u | 1/10 |
| w | 1/8 |
| m1 | 13/80 |
| m2 | 1/16 |
| mingap | 1/8 |

All five agree with notes/G-fig8.md, so this is VERIFIED twice: by two independent earlier agents and by the new exact code. Because 4_1 is amphichiral, the mirror gives the same row.

## 7. Validation of the code

seifert_ell.py is new and exact. The rho term of each fibre, (4/a) sum_k sin^2(pi k l/a) cot(pi k/a) cot(pi k b/a), is evaluated as the rational number 8[s(b,a) - sum_n ((n/a))(((bn - l)/a))]. This identity was checked numerically to 30 digits for every a ≤ 11. The SO(3) classes and w_2 are computed as in fig8-B.

The whole pipeline is: Regina recognition, then Casson–Walker orientation, then levels for K and for mK. Its output was compared with gap16/ell-code/data_table.txt, which was computed independently by the pillowcase method. All of the following match exactly (VERIFIED):

[[VALIDATION]]

## 8. Why there are so few: a geometric reason

**Short longitude and small cusp.** Suppose both ±2 are exceptional, so both have length ≤ 6 on the maximal cusp. The parallelogram identity gives
|lambda + 2mu|^2 + |lambda - 2mu|^2 = 2(|lambda|^2 + 4|mu|^2) ≤ 72,
so |lambda|^2 + 4|mu|^2 ≤ 36. On a maximal cusp |mu| ≥ 1. Hence:
- |lambda| ≤ sqrt(32) ≈ 5.66;
- the cusp area satisfies A ≤ |lambda||mu| ≤ (|lambda|^2 + 4|mu|^2)/4 ≤ 9.

**How rare this is.** Knots in S^3 have long longitudes: the longitude of 4_1 is 2 sqrt 3 ≈ 3.46, and the minimum over each crossing number stays between about 3 and 4. Only a handful of knots at each crossing number satisfy the inequality, while the number of knots grows exponentially:

[[STATS]]

**Alternating knots.** For hyperbolic alternating knots, Lackenby and Purcell ("Cusp volumes of alternating knots", Geom. Topol. 2016) bound the cusp volume below by a linear function of the twist number. So A ≤ 9 bounds the twist number of an alternating survivor. The survivors seen here are of this kind: genus one and twist-type knots, and the knots in §4.

**Survivors behave like twist knots.**
- One of the two slopes is usually much shorter than the other.
- When a ±2 filling is Seifert fibred, it is always of type (2, 4, n).
- For a twist knot with c crossings the Seifert filling has n = 2c - 3 and lies on one side only: 5_2: 7, 6_1: 9, 7_2: 11, 8_1: 13, 9_2: 15, 10_1: 17.
- The figure-eight is the twist knot with n = 5, and it is the amphichiral one. That is why its Seifert ±2 slopes occur on both sides.

**Status of these remarks.** They explain the result but are not a proof beyond the searched range (PLAUSIBLE).

## 9. Files

All code is in census-code/:
- scan.py: floating-point scan.
- vscan.py and vscan_list.py: interval scan.
- periph.py: peripheral curves.
- meridian_check2.py: meridian check.
- classify.py and analyse_knot.py: fillings, Regina, orientation and levels.
- jsj_check.py: certificate for a hyperbolic JSJ piece.
- seifert_ell.py: exact Seifert levels.
- validate.py: torus knot and 4_1 validation.
- aggregate.py, stats.py and report_tables.py: tables.

Raw output:
- scan-out/*.csv: one line per knot.
- vscan-out/*.csv: interval lengths.
- analysis-out/*.jsonl: one record per analysed knot.
- validate.out.
- meridian_check.out.
