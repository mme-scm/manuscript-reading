# r7 test: the mixed triangles at ±2 at chain level in the pillowcase model

This is a test, not a proof. The question is Conjecture R of `strategy16.tex`. The test computes the chain-level maps a, b, c, g_A, g_M, g_B of the mixed triangles in the pillowcase model:

- (I): A_0 → T → B_1 → A_0;
- (II): A_1 → T → B_0 → A_1.

It then reads off three things:

- absorption of the bottom class;
- the depth δ;
- whether the vertex relation id ≃ c g_A + g_M a returns the bottom class through g_M a.

Labels used below:

- **COMPUTED**: exact rational computation, or a numerical one where stated. Either it is in the model with the rules stated, or it is forced by exact level data plus the triangle relations.
- **MODEL-DEPENDENT**: true in the model, but resting on a rule that is not derived from gauge theory.
- **UNCERTAIN**: neither of the above.

Code is in `r7/test-code/`. Levels are always the exact ones from `gap16/triangle-code/tk.py` and the 4_1 Seifert data; the model never computes a level. The model computes polygons and their ω-areas, and these are compared with the levels.

---

## 0. Verdict

1. **The model works (COMPUTED / MODEL-DEPENDENT).** With the rules of §1, the polygon counts satisfy every relation of both triangles exactly, at chain level:
   - ba = cb = ac = 0;
   - c g_A + g_M a = id_A, a g_M + g_B b = id_T, b g_B + g_A c = id_B.

   They also reproduce the known ranks, the parity vanishing (b = 0 for mirrors, a = 0 for positive knots), m1 and m2, and the gaps 3/16 and 1/8 at common points.

   Coverage: **104 scan lines (55 distinct instances), with 0 relation failures.**
   - Complete, meaning both chiralities, both triangles, and both perturbation signs where the instance is degenerate: T(2,3), T(2,5), …, T(2,17), T(3,4), T(3,5), T(4,5), T(3,8), T(5,6).
   - Partial: the mirror of T(4,7).
   - Separate summary runs, all relations holding: the mirrors of T(3,7), T(5,7), T(3,11), both triangles.

   Of the 90 rule variants tried on T(3,−5) (§1.3), the only ones in which all relations hold are the variants of one choice. They differ only in the corner rule, which makes no difference. The full grid was run for (I); for (II), 86 of the 90 variants were run with the same result.
2. **Absorption.** For T(3,−5), the bottom class is absorbed in both triangles:
   - δ_I = 27/340, which settles strategy-exact's open interval [1/20, 27/340];
   - δ_II = 1/34.

   For T(2,−3) and 4_1, (I) is not absorbed (δ = 0) and (II) is absorbed: δ = 1/8 for T(2,−3), δ = 1/10 for 4_1.
3. **Return (the main finding).** In every absorbed instance (21 distinct instances) the bottom class returns through g_M a, never through c g_A. The returning pair has η_a + E_M = 1/16 exactly. In the pillowcase, the a-triangle and the g_M-quadrilateral are the two pieces of a **mixed triangle** (p_A, p_B, q) of area 1/16, cut by a chord of Γ (§5.2):
   - T(3,−5): η_a = 1/272 and E_M = 1/17;
   - binary dihedral cases: η_a = 0 and E_M = 1/16.
4. **Return is forced by levels alone.** For perfect complexes, the vertex relation forces a return at the bottom whenever no generator of B lies in the window [λ − 3/16, λ − 1/8]. In particular it forces one whenever m < 1/8. So, for perfect complexes, **Conjecture R (no return) implies m ≥ 1/8 + η_g** (§5.3):
   - this is stronger than the 1/16 target;
   - it is false for every det-1 mirror torus knot tested, in both triangles: m ≈ 0.085–0.1248, all below 1/8;
   - it is false for T(2,−3) (II) and 4_1 (II).

   As stated, Conjecture R cannot be the route. strategy16's claim that "zero-energy returns at binary dihedral points are the only mechanism the data show" is wrong: det-1 knots return with η_a = 1/(16(pq+2)) > 0.
5. **Inequality (D) of strategy16.** δ ≤ 1/16 + η_g holds in every instance computed. Equality holds only for T(2,−3) (II). The lower end of Theorem 5.1, m ≥ 1/8 − δ + η_g, is attained exactly in most instances.
6. **The coordinator's question (§8).** At common or χ-related pillowcase points, the exact level differences are only:
   - 0 or 1/8 for Y/traceless pairs (flat singular connection of index 0 or −1);
   - 1/8 for same-bundle pairs;
   - 3/16 for mixed pairs.

   The pairs that differ by exactly 1/16 do exist, and they realise m2 = 1/16 for T(2,−3) and 4_1. But they never sit at common points, so **no flat connection on any cobordism containing the knot exterior carries them**. The 1/16 they realise is the area of the mixed triangle (the minimal odd cap), reached through a zero-energy flat singular absorption.

   The level formula does predict a genuinely flat 1/16: at a mixed common point where Γ has shallow negative slope (−2 < s < 0), the rigid exterior E_{γ_1} of level −1/16 would carry it at zero energy. This never occurs in the data. For Δ = 1 it is non-generic by the Thom principle.

---

## 1. The model

### 1.1 Lines, corners, maps

The torus is T² = R²/Z², the pillowcase is P = R²/G with G = Z² ⋊ {±1}, and ω = 2 da∧db (P has area 1).

**Lines.**

| object | line |
|---|---|
| A_0 | L_2^0 = {2a + b ∈ Z} |
| A_1 | L_2^w = {2a + b ∈ ½ + Z} |
| B_0 | L_{−2}^0 = {−2a + b ∈ Z} |
| B_1 | L_{−2}^w = {−2a + b ∈ ½ + Z} |
| T | V = {a ∈ ¼ + ½Z} |
| (S³ route) | L_∞ = {a ∈ Z}, and its χ-image {a ∈ ½ + Z} |

**Corners of the triangles, in P.**

| | (I) | (II) |
|---|---|---|
| p_A = L_2 ∩ V | (1/4, 1/2) | (1/4, 0) |
| p_B = V ∩ L_{−2} | (1/4, 0) (the reducible θ_K) | (1/4, 1/2) |
| q_1, q_2 = L_{−2} ∩ L_2 | (1/8, 3/4), (3/8, 1/4) | (1/8, 1/4), (3/8, 3/4) |
| g^ns corners (pillowcase corners) | (0,0), (0,1/2) and χ-images (1/2,0), (1/2,1/2) | (0,1/2), (0,0) and χ-images |

The mixed triangles (p_A, p_B, q_i) have area exactly 1/16 (triangle-1 §2.3). Their χ-images are the triangles with the other q_i.

**The maps.** Each is μ^d with the listed corners:

| map | polygon | top. level |
|---|---|---|
| a | μ²(x, p_A) | 0 |
| b | μ²(y, p_B) | 0 |
| c | μ²(z, q_1 + q_2) | 3/16 |
| g_A = g^sing + g^ns | μ³(x, p_A, p_B) + μ³(x, c_0, c_∞) | −1/8 |
| g_M | μ³(y, p_B, q_1 + q_2) | 1/16 |
| g_B | μ³(z, q_1 + q_2, p_A) | 1/16 |

### 1.2 Rules (status: MODEL-DEPENDENT unless stated)

- **M1 (generators).** Generators are Γ ∩ L in P. The counts are SU(2) counts: χ-pairs are listed separately, χ-fixed generators once.
- **M2 (polygons).** μ^d(x, p_1, …, p_{d−1}) → z counts convex Euclidean polygons in R², counted modulo G by fixing the base lift of x. The vertices are x, p_1, …, z in **counter-clockwise** order, with:
  - edge x → p_1 on the M_0-line through x;
  - p_i → p_{i+1} on an M_i-line;
  - p_{d−1} → z on the M_{d−1}-line through z;
  - z → x along the same lifted component of Γ.

  For the torus knots Γ is a union of straight segments, so immersed polygons with convex corners are exactly convex Euclidean polygons. For the same reason the model differentials vanish (straight segments bound no bigons), consistent with perfection. The orientation was fixed on the first example, where the area of the a-triangle equals c(x) − c^tl(y) (T(2,−3): 1/32 = 1/32).
- **M3 (corners).** Each corner must project to the listed point of P.
  - **c uses both mixed points q_1 + q_2**, i.e. both odd flat limits γ_1 and γ_1′ = γ_1 ⊗ χ on L(4,1). With only one of them, ac ≠ 0 (12 failing entries for T(3,−5)).
  - **g_A contains the nonsingular family g^ns.** It is a quadrilateral with two vertices at pillowcase corners: L_2 ∩ edge and edge ∩ L_{−2}. This is the route through J = S³ (the edge L_∞), and it is the only place where pillowcase corners are polygon vertices.
  - **Both edges {a = 0} and {a = 1/2} must be used** (χ-symmetrised). With only a = 0, the vertex relations fail in 6 entries; with both, they hold exactly.

  The resulting a, b, c, g_A, g_M, g_B are all χ-equivariant.
- **M4 (corner avoidance).** Variants:
  - 'free': orbifold count;
  - 'int': no corner of P strictly inside;
  - 'closed': no corner on the boundary either.

  After M5 the three give identical maps for T(3,−5) (§1.3). The runs use 'int'.
- **M5 (index rule).** A polygon counts only if its ω-area equals the level drop prescribed by the topological level of the map: c(out) = c(in) + ℓ_top − area. Rejected polygons have residual in ½Z ∖ {0}: these are larger lifts of index ±4k. This is the instanton Z/8 grading, gr ≡ 4(Na + b) + …, imposed on the Fukaya count. Without M5 every variant fails (§1.3).
- **M6 (endpoints of torus-knot arcs, the (H1) violation).** Γ consists of segments ending on b ∈ Z, where they meet the reducible arc. The endpoints are treated as **stops**: a Γ-edge stays inside one arc and never continues onto the reducible line.
  - Arcs with different (k, l) are different components even where they are collinear and overlap in P. For T(3,5), (1,1) and (1,3) both lie on b = 15a − 1/2. Generators at the same point of P on different arcs are different generators, with different levels.
  - A Γ-edge joins two generators of the same arc, so it lies inside that arc automatically.
  - The alternative, letting Γ continue through an endpoint (along the reducible line, or into a collinear arc with different (k, l)), was **not tested** (MODEL-DEPENDENT).
  - The rule is supported only indirectly: with it, all triangle relations hold.
- **M7 (triple points: binary dihedral generators at (1/4,0), generators at mixed points q).** These are degenerate: a generator coincides with a corner. Every arc is translated by db = ±10⁻⁶ (a Thom perturbation, which breaks χ).
  - Results are identical for both signs: relations, absorption, δ, η_g, return. Only which member of a χ-pair carries which term changes.
  - The perturbation **must** break χ. For T(2,−3) (I), the triangle relations cannot hold with χ-equivariant g_M while B_1's only generator is χ-fixed (simple algebra, §4.1).
  - At a transverse triple point Γ ∩ L ∩ L′, the tiny polygon left after a translation has an orientation independent of the direction of the translation. For a′ at (1/4, 0) (lines L_2^w and V) it counts iff Γ's slope s > −2. This agrees with the levels: the flat singular connection has index 0 for s > −2 and −1 otherwise (4_1: branch + equal levels, branch − differs by 1/8).
- **M8 (4_1 double point).** Polygon edges follow one branch through the double point (no corner there). The bounding cochain of Conjecture 3.2 is ignored. **This is known to be insufficient** (§7.3): the naive count gives a bigon d_T(y₋) = y₊ that cannot be there (UNCERTAIN how the bounding cochain removes it).

### 1.3 Sensitivity (`rulecheck.py`, T(3,−5); COMPUTED)

The grid is 3 corner rules × 3 choices of c-corners × 3 g_A-parts × 2 edge choices × M5 on/off, giving 90 variants. For (I) the full grid was run; for (II), 86 of the 90 variants were run, with the same outcome. Exactly 3 have zero failing relation entries: corner rule free, int or closed, each with c = q_1 + q_2, g_A = g^sing + g^ns, both edges, and M5 on. Nearest misses:

| variant | failing entries |
|---|---|
| g^ns on one edge only | 6 |
| g_A = g^sing alone | 12 |
| c with q_1 or q_2 alone | 42 to 54 |
| the full rule set with M5 off | 32 ('closed') or 70 ('int') |

So the rules are not tuned per knot: one rule set works everywhere tested.

---

## 2. Consistency checks (question 4)

| check | result | label |
|---|---|---|
| m1, m2 from the model's bottoms | T(2,−3): 5/32, 1/16. T(3,−5): 151/1768, 219/1768. 4_1: 13/80, 1/16. All as known. | COMPUTED (levels are input) |
| triangle relations | all hold exactly (§0.1) | COMPUTED / MODEL-DEPENDENT |
| parity | b = 0 for mirrors and a = 0 for positive knots, in every model run | COMPUTED |
| ranks | rk a = \|T\| for mirrors, c injective, rk g_A = \|B\|. For example T(3,−5) (I): rk(a, b, c, g_A, g_M) = (4, 0, 12, 12, 4) | COMPUTED |
| mixed-point gap 3/16 | T(2,−3) (II): c′ maps the B_0 generator at q′ to the A_1 generator at the same point, with **area 0** and level drop exactly 3/16 | COMPUTED |
| same-bundle gap 1/8 | at (1/4,0) for P1/P1 (T(2,−3) and 4_1): A_1 − B_1 = 1/8 | COMPUTED (level data) |
| Kirk–Klassen action vs level formula | every counted polygon's area equals the level drop (M5). The rejected ones miss by multiples of 1/2 only, a nontrivial check that action ≡ level mod ½ | COMPUTED |
| 4_1 a-triangle | x ∈ A_0 → p_A → y₊: numerical ω-area 0.0374999993 against level drop 19/80 − 1/5 = 3/80 | COMPUTED (numerics, 10⁻⁹) |
| 4_1 traceless levels | the pillowcase rule c^tl = Φ + sgn(slope)/16 with one constant fitted on A_0 gives A_1 = 1/5, 3/10, B_1 = 3/40, 7/40 and B_0 = 11/80 to 10⁻³. It selects triangle-1's option {1/5, 7/40}: y₊ at 1/5, y₋ at 7/40 | COMPUTED (numerics) |

---

## 3. Generators and levels (question 1)

Positions are in P, with a ∈ [0, 1/2] and b mod 1. Levels are c = (3+ρ)/16; c^tl is Seifert-framed. The model differential is zero for all torus-knot complexes (no bigons). For 4_1 see §7.3.

### 3.1 T(2,−3)

Γ is the segment b = 6a − 1/2, a ∈ (1/12, 5/12). Both ends are on b ∈ Z, at the roots of Δ.

| complex | generators: level @ position |
|---|---|
| A_0 (Y_2, P0) | −1/96 @ (3/16, 5/8); −1/96 @ (5/16, 3/8) (χ-pair) |
| A_1 (Y_2, P1) | **−1/24 @ (1/4, 0)** (binary dihedral); 1/12 @ (1/8, 1/4) = q′_1; 1/12 @ (3/8, 3/4) = q′_2 |
| T | −1/24 @ (1/4, 0) (binary dihedral) |
| B_0 (Y_{−2}, P0) | −5/48 @ (1/8, 1/4) = q′_1; −5/48 @ (3/8, 3/4) = q′_2 |
| B_1 (Y_{−2}, P1) | −1/6 @ (1/4, 0) (binary dihedral) |

Degeneracies:
- (I): Γ passes through p_B, the triple point Γ ∩ V ∩ L_{−2}^w at (1/4, 0).
- (II): Γ passes through p′_A, and the mixed points q′_1, q′_2 lie on Γ.

### 3.2 T(3,−5) (det 1, no binary dihedral representations)

There are four arcs (1,1), (1,3), (2,2), (2,4) on b = 15a − k/2, with (1,1) and (1,3) overlapping, and (2,2) and (2,4) overlapping. There are no degeneracies. Full list in `test-code/detail_mT35.out`. Bottoms, and the generators that matter:

| complex | size | lowest levels @ position (arc) |
|---|---|---|
| A_0 | 16 | **−319/510** @ (9/34, 8/17)(1,3) and (4/17, 9/17)(2,2); −587/1020 @ same two points, arcs (1,1), (2,4); −557/1020 @ (7/34, 10/17), (5/17, 7/17); … |
| T | 4 | **−151/240** @ (1/4, 1/4)(1,3), (1/4, 3/4)(2,2); −139/240 @ (1/4, 1/4)(1,1), (1/4, 3/4)(2,4) |
| B_1 | 12 | **−1109/1560** @ (4/13, 3/26)(1,3), (5/26, 23/26)(2,2); −1091/1560; −1031/1560; … |
| A_1 | 20 | **−319/510** @ (4/17, 1/34)(1,3), (9/34, 33/34)(2,2); −152/255; … |
| B_0 | 16 | **−1169/1560** @ (7/26, 7/13)(1,3), (3/13, 6/13)(2,2); −1091/1560; … |

### 3.3 4_1 (numerics on the Riley curve)

Γ is a closed figure-eight. Its double point is at (1/4, 0), with branch slopes ±2√5. The A_0 points lie on branch +, the B_0 points on branch −.

| complex | generators |
|---|---|
| A_0 | 19/80 @ (0.17802, −0.35604) and its χ-partner (0.32198, 0.35604); slope +6.94 |
| B_0 | 11/80 @ (0.32200, 0.64385) and (0.17804, 0.35586); slope −6.94 |
| A_1 | 1/5 @ (1/4, 0) on branch +; 3/10 @ (1/4, 0) on branch − |
| B_1 | 3/40 (branch +); 7/40 (branch −), both @ (1/4, 0) |
| T | 1/5 (branch +, y₊); 7/40 (branch −, y₋), both @ (1/4, 0) |

Every generator of A_1, B_1 and T sits at the double point (1/4, 0) = p_B (I) = p′_A (II). All of these are binary dihedral.

---

## 4. The maps (question 2)

### 4.1 T(2,−3), complete

Model after the perturbation db = +10⁻⁶; areas are given to 10⁻⁶. Write x_1 = A_0 @ (3/16, ·), x_2 = A_0 @ (5/16, ·), y_0, z_0 the binary dihedral generators, x_bd = A_1 @ (1/4, 0), and x_q, z_q for the A_1 and B_0 generators at q′.

**Triangle (I).**

| map | value | area | corner |
|---|---|---|---|
| a | x_1, x_2 ↦ y_0 | 1/32 each | — |
| b | 0 | — | — |
| c | z_0 ↦ x_1 + x_2 | 1/32 each | q_1 and q_2 respectively |
| g_A^sing | x_1 ↦ z_0 | 1/32 | — |
| g_A^ns | 0 | — | — |
| g_M | y_0 ↦ x_2 | 1/32 | corners p_B, q_2 |
| g_B | 0 | — | — |

- Kernel: x_1 + x_2 (level −1/96, so **δ = 0, not absorbed**).
- Vertex relation on the bottom generators: x_1 = c g_A x_1, while x_2 = g_M a x_2, with η_a = E_M = 1/32 (sum 1/16).
- The opposite perturbation swaps x_1 and x_2.
- Without any perturbation the relations are impossible. a(x_1) = a(x_2) and c z_0 = x_1 + x_2 are forced, which forces g_A to break χ and then g_M(y_0) ∈ {x_1, x_2}, which is not χ-invariant.

**Triangle (II).**

| map | value | area | corner(s) |
|---|---|---|---|
| a′ | x_bd ↦ y_0 | ≈ 0: the flat singular connection, tiny-triangle rule with s = 6 > −2 | — |
| a′ | x_q ↦ y_0 | 1/8 | — |
| c′ | z_q ↦ x_q | 0: the flat exterior at the mixed point, level drop exactly 3/16 | — |
| c′ | z_q ↦ x_bd | 1/8 | — |
| g′_A | x_{q′2} ↦ z_{q′2} | 1/16 | g^sing |
| g′_A | x_{q′1} ↦ z_{q′1} | 1/16 | g^ns, pillowcase corners (0,1/2), (0,0) |
| g′_M | y_0 ↦ x_bd | **1/16** | p′_B, q′_1 |

Each g′_A polygon is a mixed triangle or the corner triangle with vertex q′. The g′_M polygon is **exactly the mixed triangle (p′_A, p′_B, q′_1)**, because Γ passes through its vertex p′_A.

### 4.2 T(3,−5) (I): the part that matters

All maps are in `detail_mT35.out`. Bottom generator x = −319/510 @ (9/34, 8/17)(1,3), and τ = −151/240 @ (1/4, 1/4)(1,3).

| map | value | area | corner(s) |
|---|---|---|---|
| a | x ↦ τ | **1/272** | — |
| a | other A_0 generators | (2k+1)²/272 | — |
| g_A | x ↦ 0 | — | forced: B_1 has nothing at level ≤ λ − 1/8 |
| g_A | first kernel class ↦ −1091/1560 | 25/884 | g^sing |
| g_M | τ ↦ x | **1/17** | p_B, q_2 = (3/8, 1/4) |
| c | B_1 bottom −1109/1560 @ (4/13, 3/26) ↦ x | 361/3536 | q_1 |
| c | B_1 bottom ↦ −137/255 | 49/3536 | q_2 |

The first kernel class is (−587/1020 (1,1)) + (−557/1020 (1,1)), at level κ = −557/1020.

Of the g^ns polygons, 4 survive M5 in (I) and 6 in (II). They act only near the top of the spectrum, but they are needed for the vertex relations there.

---

## 5. Absorption, δ, η_g and return (question 3)

### 5.1 Table (COMPUTED in the model; the starred entries are forced by levels and the triangle relations alone)

| instance | m | bottom absorbed? | δ | η_g | 1/8 − δ + η_g ≤ m ≤ 3/16 − δ | (D) δ ≤ 1/16 + η_g | bottom returns via | τ, η_a, E_M |
|---|---|---|---|---|---|---|---|---|
| T(2,−3) (I) | 5/32 | no | 0 | 1/32 | [5/32, 3/16] | yes | class x_1 + x_2 ∈ ker a; generatorwise one each | — |
| T(2,−3) (II) | 1/16 | yes* | 1/8* | 1/16* | [1/16, 1/16] | equality | **g_M a*** | bd, 0, 1/16 |
| T(3,−5) (I) | 151/1768 | yes* | 27/340 | 25/884 | [653/8840, 147/1360] | yes | **g_M a*** | 1/272, 1/17 |
| T(3,−5) (II) | 219/1768 | yes* | 1/34 | 25/884 | [219/1768, 43/272] | yes | **g_M a*** | 1/272, 1/17 |
| 4_1 (I) | 13/80 | no* (ranks) | 0* | ≤ 3/80 | — | yes | — | — |
| 4_1 (II) | 1/16 | yes* | 1/10* | 3/80* | [1/16, 7/80] | yes | **g_M a*** | y₊, 0, 1/16 (model) |
| T(2,−5) (II) | 3/32 | yes | 1/12 | 5/96 | [3/32, 5/48] | yes | g_M a* | bd, 0, 1/16 |
| T(2,−7) (II) | 5/48 | yes | 1/16 | 1/24 | [5/48, 1/8] | yes | g_M a* | bd, 0, 1/16 |
| T(3,−4) (II) | 1/10 | yes | 1/14 | 13/280 | [1/10, 13/112] | yes | g_M a* | bd, 0, 1/16 |
| T(4,−5) (I) | 1/9 | yes | 1/22 | 25/792 | [1/9, 25/176] | yes | g_M a* | bd, 0, 1/16 |
| T(3,−7) (I), (II) | 435/3496 | yes | 1/46 | 37/1748 | lower end = m | yes | g_M a* | 1/368, 11/184 |
| T(5,−7) (I), (II) | 1219/9768 | yes | 1/74 | 65/4884 | lower end = m | yes | g_M a* | 1/592, 1/16 − 1/592 |
| T(3,−11) (I), (II) | 1083/8680 | yes | 1/70 | 61/4340 | lower end = m | yes | g_M a* | 1/560, 1/16 − 1/560 |

Notes on the table:

- **Non-absorbed instances.** The (I) triangles of T(2,−q), T(3,−4), and the (II) triangle of T(4,−5), have m ∈ (1/8, 3/16], as the kernel criterion predicts.
- **Positive torus knots (controls).** a = 0, nothing is absorbed, and every bottom generator goes through c g_A.
- **det-1 mirrors.** η_a = 1/(16(pq + 2)) in every case. Except in T(3,−5) (I):
  - δ = 1/(2(pq + 2));
  - the B-bottom is the g_A-image of the first kernel class, so m = 1/8 − δ + η_g exactly; for example 1/8 − 1/884 for T(3,−5) (II).

  In T(3,−5) (I), δ = 27/340 and m exceeds the lower end by 0.0115.
- **Starred entries.** In 4_1 (II), absorption, δ = 1/10, η_g = 3/80 and the return are forced by levels:
  - the window [1/5 − 3/16, 1/5 − 1/8] = [1/80, 3/40] contains no B_0 generator (11/80), so g′_A x_bd = 0;
  - the vertex relation then gives x_bd = g′_M a′ x_bd.
  The model adds that τ = y₊ with η_a = 0, from the local check `fig8_local.py`, which finds the a′-triangle of area 0 and the g′_M polygon of area 1/16 with corners (p′_B, q′).

### 5.2 What the return is, geometrically (COMPUTED; `tiling.py`)

In every return found, the a-triangle (x, p_A, τ) and the g_M-quadrilateral (τ, p_B, q, x) glue along the Γ-chord τ–x into the mixed triangle (p_A, p_B, q):

- x lies on its L_2-edge [q, p_A];
- τ lies on its V-edge [p_A, p_B];
- the total area is 1/16.

Checked exactly for T(3,−5) and T(3,−7), both triangles; for example T(3,−5) (I): 1/272 + 1/17 = 1/16.

In the binary dihedral cases the chord shrinks to the vertex p′_A, and the g_M polygon is the whole mixed triangle. strategy16's "lens-end configuration: flat singular connection plus minimal cap" is exactly this degenerate case. The generic case is the same triangle cut by Γ.

### 5.3 Return is forced whenever the drop is below 1/8 (COMPUTED as algebra; model-independent for perfect complexes)

Suppose all differentials vanish, so the vertex relation is the exact identity c g_A + g_M a = id_A. Let x be a bottom generator, at level λ.

1. ⟨c g_A x, x⟩ = 1 needs some z ∈ B with ⟨g_A x, z⟩ = ⟨c z, x⟩ = 1. By the levels of g_A and c this forces c(z) ∈ [λ − 3/16 + η_c, λ − 1/8 − η_g]. Hence m ≥ 1/8 + η_g.
2. Contrapositive: if m < 1/8 + η_g, then ⟨g_M a x, x⟩ = 1 for every bottom generator. Every bottom generator is then absorbed and returned.
3. Any return has η_a + E_M = 1/16 exactly. This is the identity c(τ) = λ − η_a = λ − 1/16 + E_M, which says nothing about cosmetic pairs.
4. If the bottom is not absorbed, the kernel criterion already gives m > 1/8.

So **Conjecture R implies m ≥ 1/8 + η_g**. It is not a path to 1/16; it is equivalent to a 1/8 statement.

In the data it fails exactly where m < 1/8. That includes every det-1 mirror torus knot tested, in both triangles, where m = 0.0854 to 0.1248. A cosmetic pair has m1 + m2 = 0, so it must contain a return; the converse question, whether returns cost anything, is answered by the tiling: they cost exactly the mixed triangle.

For non-perfect complexes (Δ = 1), these statements acquire boundary-depth corrections (UNCERTAIN).

---

## 6. What the test says about the 1/16

**What the pillowcase shows.**

- The quantity 1/16 appears in the chain-level triangle exactly as the ω-area of the mixed triangles (p_A, p_B, q). Every return of an absorbed bottom class tiles one of them.
- The levels of the maps translate into a geometric statement:
  - level(g_M) − level(a) = 1/16;
  - area(mixed triangle) = 1/16;
  - the cap energy is 1/16.
- The drop itself is not controlled by the return. It is m = 1/8 − δ + η_g (attained in most instances):
  - δ is the Φ-spacing on Γ between the absorbed bottom and the first kernel class;
  - η_g is the area of a g^sing quadrilateral.

  Nothing in the return geometry bounds δ − η_g. The values are:

  | instance | δ − η_g |
  |---|---|
  | T(3,−5) (II) | 1/884 |
  | T(3,−5) (I) | 0.051 |
  | T(2,−3) (II) | 1/16 |
- So the inequality (D) of strategy16 holds in all data, but the pillowcase does not show why. (D) is a statement about the spacing of consecutive A-generators along Γ against a g_A-quadrilateral area. Neither is fixed by the 1/16 triangle.

---

## 7. 4_1 (partial)

### 7.1 Done

- Levels and positions: §3.3, numerical, consistent with the pillowcase level formula to 10⁻³.
- The a-map of (I): a(x) = a(χx) = y₊, with area 3/80 matching the levels (10⁻⁹). There is no a-polygon to y₋: the only candidate encloses the right lobe of Γ with the wrong orientation (signed area −1/10).
- (I) is therefore not absorbed (also forced by rk a = 1), δ = 0.
- (II): the local triple-point check at (1/4, 0) (`fig8_local.py`), and the level-forced statements of §5.1. The return is the mixed triangle with Γ through its vertex p′_A, as for T(2,−q).

### 7.2 Not done

The full g_A, c, g_M and g_B polygon counts with the curved Γ, which pass through or around the double point. Two things are missing:

- polygon enumeration for a curved, immersed Γ;
- a rule for the bounding cochain (§7.3).

### 7.3 A defect of the naive model (COMPUTED; consequence UNCERTAIN)

The naive count (M8) gives a convex-cornered **bigon in T** from y₋ to y₊:

- edges: V from y₋ down to y₊, then Γ around the right lobe;
- ω-area 0.099992, against 1/8 + c(y₋) − c(y₊) = 1/10, so it is level-consistent;
- grading: y₊ and y₋ have opposite parity (the tangent line of Γ passes the vertical once along either lobe).

So the naive model has d_T(y₋) = y₊ and makes T acyclic. That is impossible:

- rk I^♮(4_1) = det = 5 = 1 + 2·2 forces d_T = 0;
- with T acyclic, (II) would make g′_A an isomorphism A_1 → B_0 of level −1/8, but x_bd (1/5) has nothing below 3/40 to map to.

Conjecture 3.2's bounding cochain at the double point must cancel this bigon. For 4_1 I take d_T = 0, as the rank argument requires. Polygon counts that pass the double point are not trustworthy without it. The same caution applies to any Δ = 1 knot, whose Γ is a closed immersed curve.

---

## 8. Coordinator's request: level −1/16, flat connections, the pairs at 1/16 (`pairs.py`, `pairs.out`)

### 8.1 Level differences at common and χ-related points (COMPUTED, exact)

| knot | pair type | values found |
|---|---|---|
| T(2,−3) | A_1 − B_0 (mixed P1 → P0) | 3/16 at q′_1, q′_2 (same point); 3/16 χ-related |
| | A_1 − B_1 (same bundle P1) | 1/8 at (1/4, 0) |
| | A_1 − T | 0 at (1/4, 0): flat singular, index 0 |
| | T − B_1 | 1/8 at (1/4, 0): flat singular, index −1 |
| | A_0 with anything | no common points (A_0 sits at non-special points) |
| 4_1 | A_1 − B_1 | 1/8 on each branch at (1/4, 0) |
| | A_1 − T | 0 (branch +), 1/8 (branch −) |
| | T − B_1 | 1/8 (branch +), 0 (branch −) |
| | mixed pairs | no common points at all |
| | other branch at the double point (different representations, no flat connection) | 1/40, 9/40, 1/10 |
| T(3,−5) | any pair | no common or χ-related points at all (det 1; Γ misses (1/4, 0), (1/4, 1/2) and the four mixed points) |

**Answer.** At common points the only differences are 0, 1/8 (Y/traceless, index 0 or −1), 1/8 (same bundle) and 3/16 (mixed). **Never 1/16.**

### 8.2 The pairs with difference exactly 1/16 (COMPUTED)

| knot | Y_2 generator | Y_{−2} generator | which drop |
|---|---|---|---|
| T(2,−3) | A_1 binary dihedral, −1/24 @ (1/4, 0) | B_0, −5/48 @ q′_1 = (1/8, 1/4) and q′_2 = (3/8, 3/4) | m2 |
| 4_1 | A_1 branch +, 1/5 @ (1/4, 0) | B_0, 11/80 @ (0.322, 0.644) and (0.178, 0.356) | m2 |
| 4_1 | A_0, 19/80 @ (0.178, −0.356), (0.322, 0.356) | B_1 branch −, 7/40 @ (1/4, 0) | reverse pairing; not the minimiser, m1 = 13/80 |

None of these pairs is at the same or a χ-related point. A flat connection, singular or not, on any cobordism containing X × I restricts to a single representation of π_1(X), so it links only same-point (or χ-twisted) generators. Hence:

- **no flat connection carries an m = 1/16 pair**, not on X′ = W′∖νS (γ_1 or γ_0 end), not on the singular 2-handles, not on (W′, S);
- these equalities are not zero-energy phenomena of a −1/16 cobordism.

**What does carry them (COMPUTED in the model):**

- **T(2,−3):** m2 = 3/16 − δ with δ = 1/8.
  - The 3/16 is the flat exterior at the mixed point q′: c′ of area 0, exact.
  - The 1/8 is the spacing (s + 2)/64 with s = 6 between the binary dihedral point and q′ along Γ.
  - Equivalently, the minimiser pair spans the mixed triangle (p′_A, q′, p′_B): x_bd sits at the vertex p′_A, z at the vertex q′, and the returning g′_M polygon is that triangle (energy 1/16) after a zero-energy flat singular absorption.
- **4_1:** m2 = 13/80 − 1/10. Here 13/80 = c(A_1 branch −) − c(B_0) is a positive-energy g′_A/c′ pairing at different points (no flat connection), and 1/10 = δ = the lobe area of Γ. The value 1/16 is not structural here (triangle-1 agrees).

### 8.3 Where a genuinely flat level −1/16 map would act (MODEL-DEPENDENT: the ι term of the pillowcase level formula)

At a common point x of L_2^ε and L_{−2}^{ε′}, the level formula gives

c(Y_2, x) − c(Y_{−2}, x) = 4(a − 1/4)² + 1/8 − (ι_2(x) − ι_{−2}(x))/8,

with ι_2 = 1 iff Γ's slope s ∈ (−2, 0) and ι_{−2} = 1 iff s ∈ (0, 2). Hence:

| point | steep Γ | s ∈ (−2, 0) | s ∈ (0, 2) |
|---|---|---|---|
| mixed point (a = 1/8, 3/8) | 3/16 (all data) | **1/16** | 5/16 |
| same-bundle point (a = 1/4) | 1/8 | 0 | 1/4 |

So the rigid exterior E_{γ_1} (level −1/16, i_0 = 0) carries a zero-energy flat connection exactly at a mixed common point where Γ is shallow and negatively sloped. That is the equality case of the user's proposed non-strict mixed bound. It never occurs in the data: torus knots are steep everywhere, and 4_1 does not reach a = 1/8, 3/8. For Δ = 1 knots, Γ through a mixed point is non-generic, so the Thom principle removes it.

The same formula gives gap 0 at a shallow negatively sloped same-bundle point. A strict both-bundle bound must therefore come from elsewhere than these flat connections.

### 8.4 T(3,−5): mixed pairs with difference in [1/16, 1/8] (COMPUTED; full list in `pairs.out`)

**A_0 − B_1: 32 pairs**, all differences in {653/8840, 151/1768, 203/1768, 219/1768, 1093/8840, 171/1768, 1057/8840}. The bottom pair:

- A_0 −319/510 @ (9/34, 8/17)(1,3);
- B_1 −1109/1560 @ (4/13, 3/26)(1,3);
- difference **151/1768 = m1**.

In P, the bottom A_0 point lies on the L_2^0-edge, and the bottom B_1 point on the L_{−2}^w-edge, of the same mixed triangle (p_A, p_B, q_2) = ((1/4,1/2), (1/4,0), (3/8,1/4)), on different sheets of the steep arc. The smallest difference, 653/8840 ≈ 0.0739, is between the A_0 bottom and B_1 at −1091/1560 @ (3/13, 25/26)(1,1) and (7/26, 1/26)(2,4).

**A_1 − B_0: 44 pairs**, differences in {573/8840, 123/1768, 653/8840, 737/8840, 151/1768, 777/8840, 171/1768, 913/8840, 203/1768, 219/1768}. The minimum is 573/8840 ≈ 0.0648 (A_1 −152/255 @ (5/17, 31/34)(1,3) to B_0 −1031/1560). m2 = 219/1768 is the bottom pair (A_1 −319/510 @ (4/17, 1/34) to B_0 −1169/1560 @ (7/26, 7/13)).

**No mixed pair lies at a common point.** All these differences carry positive energy.

---

## 9. Reliability

| claim | label |
|---|---|
| Generator positions and levels (torus knots exact; 4_1 levels exact, positions numerical) | COMPUTED |
| Model polygons and areas; all triangle relations hold exactly in the instances run | COMPUTED (given M1–M7) |
| The rules themselves: c with both γ_1 limits, g^ns through both edges, M5, the stops at the arc endpoints, the perturbation at triple points | MODEL-DEPENDENT. Selected by consistency (§1.3), not derived. That c uses both q_i contradicts strategy-exact's "limit γ_1"; in SU(2) counts the pillowcase needs both. |
| Absorption and δ for T(3,−5), T(2,−3), 4_1 (§5.1) | COMPUTED. The starred entries are forced by levels and exactness; the others are model values, including δ_I(T(3,−5)) = 27/340. |
| Return via g_M a in every absorbed instance; η_a + E_M = 1/16; tiling of the mixed triangle | Return: COMPUTED and level-forced for m < 1/8. Tiling: COMPUTED in the model. |
| Conjecture R implies m ≥ 1/8 + η_g (perfect complexes) | COMPUTED (algebra). With differentials: UNCERTAIN. |
| (D) δ ≤ 1/16 + η_g in all instances | COMPUTED (model η_g) |
| No flat connection carries the m = 1/16 pairs | COMPUTED (positions) |
| Flat 1/16 at shallow mixed points | MODEL-DEPENDENT (ι term, about 55% per pillowcase-1) |
| 4_1 chain-level g_A, c, g_M | not computed. The naive double-point rule is inconsistent (§7.3) |
| Scan coverage | As in §0.1: 104 scan lines, 55 instances, 0 failures. Absorbed instances: 15 in the scan plus 6 in the summary runs. All return via g_M a with η_a + E_M = 1/16. The scan was stopped for time before T(2,19), T(3,10), T(3,13), T(4,9), T(5,8). 4_1 is outside the scan. |

## 10. Files (`r7/test-code/`)

- **Engine.**
  - `pmodel.py`: geometry, polygon enumeration, F_2 algebra.
  - `knots.py`: torus-knot data from tk.py, with mirroring.
  - `triangle.py`: the maps and relations.
  - `study.py`: absorption, δ and return.
- **Runs.**
  - `scan.py`, `scan_sel.py`: the scan; outputs `scan40.out`, `scan_selA.out`, `scan_selB.out`, merged in `scan_all.out`.
  - `summary.py`: η_g, the bracket and (D); outputs `summary_small.out`, `summary_more.out`.
  - `detail.py`: chain-level listings; outputs `detail_mT23.out`, `detail_mT35.out`.
  - `tiling.py`: output `tiling.out`.
  - `rulecheck.py`: output `rulecheck.out`.
- **4_1 and the coordinator's request.**
  - `pairs.py`: output `pairs.out` (§8).
  - `fig8_checks.py`: output `fig8_checks.out`.
  - `fig8_local.py`.
- Superseded exploration runs: `run1.py` to `run4.py`.
