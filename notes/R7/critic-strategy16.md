# Referee report on strategy16.tex (round 7)

Sources checked: strategy16.tex; notes/R6/strategy-exact.md §§2-5, 6, 7.4, 9; notes/G-sources/triangle-1.md §5.
Notation as in the paper. "Perfect" = all differentials zero (Seifert data).

## 0. Two facts used throughout

(F1) Vertex relation at A_0 (OS/DLME triangle detection, pentagon h, q = id + dk + kd):
  c g_A + g_M a = q + dh + hd = id + d(h+k) + (h+k)d   (F_2).
For ANY cycle x, w := (c g_A + g_M a) x = x + d((h+k)x). Hence [w] = [x] = xi, always.

(F2) Model 3 of strategy-exact Thm 6.2 (T = <w(3/32), t(-1/32)>, dw = t; A_0 = <x(0)>, B_1 = <z(1/16)>;
a x = t, b w = z, c z = x, g_A = 0, g_M t = x, g_B z = w). I re-checked by hand: all three homotopy relations,
all three vertex relations (q = id, h = 0), exactness, all level bounds, eta_a = eta_b = 1/32 > 0.
Here [x] in ker a_* (T is acyclic) so delta_0 = 0, yet m_1 = 0 - 1/16 = -1/16. x is not in the chain-level ker a.

## 1. Psi = g_A|ker a.  Verdict: chain map CORRECT; level CORRECT; injectivity statement CORRECT as phrased but does not do the job claimed.

- ker a is a subcomplex (a chain map); d g_A x + g_A d x = b a x = 0 on ker a. Chain map, degree shifted by that of g_A. OK.
- iota: ker a -> Cone(a), x -> (x,0), is a chain map (d_cone(x,0) = (dx, ax) = (dx,0)). (g_A,b) iota = Psi.
  ker(iota_*) = {[x] : x = dy in A_0 with a y = d t in T}. This is exactly the paper's sentence. Correct.
  Consequence: a class of H(A_0) with a chain-level representative in ker a gives a nonzero Psi class. Correct.
- level -1/8 - eta_g: i_0 = -1, b+ = 0 (ledger). eta_g > 0: odd-bundle piece has no flat connection; singular piece has none because a flat singular
  connection with both limits would need mu^2 lambda -> eps, mu^-2 lambda -> eps' with eps != eps' (mixed bundles) while mu^4 = 1 for traceless mu.
  So the reason is the mixed-bundle sign, not "W' simply connected" (the singular piece lives on W' minus S, not simply connected). Cosmetic misattribution.
- Real defects: (a) chain-level ker a is not invariant under filtered homotopy equivalence and is typically tiny (Model 3: ker a = 0 although a_* = 0);
  H(ker a) -> H(A_0) does not hit ker a_*. Psi therefore sees only classes with a representative in ker a. The invariant object is Cone(a),
  and passing from ker a_* to Cone(a) costs the primitive y of a x, i.e. beta(T) (Lemma 3.2). (b) "has a cycle representative in ker a" must read
  "has a MINIMAL-level cycle representative in ker a" (triangle-1 Thm 5.2); otherwise the bound loses c(x) - lambda.
- "Covers positive torus knots (parity forbids absorption)": true only because Seifert complexes are perfect and a = 0 at chain level by parity.
  For general K parity gives a_* = 0, not a = 0.

## 2. m_1 >= 1/8 - delta + eta_g.  Verdict: WRONG as stated (misquotes Thm 5.1).

Thm 5.1(i) of strategy-exact: m_1 >= 1/8 - delta_0 + min(eta_g, eta_a + eta_b - beta(T)). Proof: Lemma 3.2 on (a, g_A) at a class of ker a_* with c = kappa;
w = g_A x + b y with a x = d y, and c(b y) <= c(x) - eta_a - eta_b + beta(T) - 1/8. The paper's "Psi applied at kappa" silently assumes the kappa-class has a chain
representative in ker a. In general it does not, and the y-term is needed. Model 3 (F2) is a counterexample to the paper's inequality: delta_0 = 0, g_A = 0 (no energy
constraint), claimed m_1 >= 1/8, true m_1 = -1/16. Even the surviving form needs beta(T) < 1/8 + eta_a + eta_b - eta_g... i.e. an upper bound on energies of the
traceless differential (rule 1). For Delta_K = 1 the complexes are not expected to be perfect (triangle-1 §5.6, last para), so this term cannot be dropped.
Consequence: "(D) => m_1 >= 1/16" is also false as stated; the sufficient condition is 1/8 - delta + min(eta_g, eta_a + eta_b - beta(T)) >= 1/16.

## 3. "Tightness in both equality cases".  Verdict: 4_1 CIRCULAR; T(2,-3) not circular but a numerical coincidence; "structural reason" UNSUPPORTED and contradicts both sources.

- 4_1: H^w(Y_2) = {1/5, 3/10}, H(Y_{-2}) = {11/80, 11/80}, kappa = 3/10, delta = 1/10. strategy-exact §7.4 sets eta_g = 13/80 - 1/8 = 3/80, where 13/80 = 3/10 - 11/80
  is the level gap between the kernel class and the bottom of Y_{-2}. I.e. eta_g := kappa - 1/8 - lambda'(target). Then delta - eta_g = 1/8 - (lambda - lambda') = 1/8 - m_2
  IDENTICALLY, so "delta - eta_g = 1/16 and m_2 = 1/16" is a tautology. The level count only gives eta_g <= 3/80 (no class of Y_{-2} below 11/80);
  the equality is a fit. Also only the lower end of the bracket [1/40 + eta_g, 7/80] is touched, the upper end 7/80 is not.
  Both strategy-exact §7.4 ("nothing topological makes m_2 = 1/16 here") and triangle-1 §5.4 ("no structural reason ... may be a coincidence") say so explicitly.
  The paper's sentence "the structural reason ..., which triangle-1 lacked" is false.
- T(2,-3): eta_g = 1/16 is computed independently of m_2 (strategy-exact §4.3, §7.4: kernel classes sit at mixed common representations, g_A' = flat exterior of index -1 +
  minimal cap, exact level -3/16; PLAUSIBLE gluing, instanton identification not proved). delta = 1/8 is spectral data of this knot (gap between the binary dihedral
  generator and the mixed generators). So delta - eta_g = 1/8 - 1/16 is a coincidence of two independently computed numbers; both bracket ends = 1/16 there. Not a mechanism.
- General: (D) is not equivalent to m >= 1/16 (sufficient, not necessary; with the upper bracket m <= 3/16 - delta it is even stronger than m >= 1/16 when eta_g < 1/16).
  And "(D) holds in all 211 cases" cannot be read off the data: eta_g is not an observable except at common points; what the data show is delta <= 1/16 in the det-1 cases and m >= 1/16.

## 4. Vertex relation and the derived bound.  Verdict: relation and levels CORRECT; the derivation is WRONG (vacuous); the dichotomy is CIRCULAR.

- Maps/levels: A_0 -g_A-> B_1 -c-> A_0 and A_0 -a-> T -g_M-> A_0, id ~ c g_A + g_M a. Levels c g_A: 3/16 - 1/8 = 1/16; g_M a: 1/16 + (<= 0); pentagon -1/16, and
  d has c-level 1/8 so dh+hd has level 1/16; id and dk+kd have level 0 <= 1/16. All consistent with ledger.
- a_*[w] = tau does hold: a(c g_A + g_M a) = a + d(g_B g_A + h_0 a) using a c = d g_B + g_B d, the T-vertex relation id_T ~ a g_M + g_B b + dh_0, and b a = d g_A + g_A d.
  But it is not independent: by (F1) [w] = xi, so a_*[w] = a_* xi = tau trivially.
- Therefore xi - [w] = 0 ALWAYS. The branch "if xi - [w] != 0 this is (D) with room to spare" never occurs; the "one escape" (return) is the general case.
  (return) = "xi = [g_M tau + c g_A x]" is a tautology; Conjecture R, as stated, contradicts the vertex relation. The paper's claim that "a cosmetic pair needs (return)" is empty.
  (g_M tau alone is not even a cycle: d g_M tau = c b tau != 0 in general; only the sum is.)
- What the relation really gives (and the paper mis-stated):
  * General (non-perfect): w represents xi, so c(w) >= lambda; with c(w) <= max(lambda + 1/16 - (eta_g + eta_c), c(tau) + 1/16 - E_M) one gets
    "eta_g + eta_c <= 1/16 or eta_a + E_M <= 1/16": an inequality, not "= 1/16 exactly". The "exactly" is unsupported.
  * Perfect case (d = 0, q = id, h irrelevant): x = c g_A x + g_M a x exactly. Every path x -> x in either term has energy exactly 1/16.
    Dichotomy: either g_A x != 0, then a generator y of B_1 (a cycle, nonzero class) gives m_1 >= 1/8 + eta_g; or g_A x = 0 and x = g_M a x with eta_a + E_M = 1/16 exactly.
    This is the true content of "return"; the paper only names the second branch and treats it as an exception to be excluded.
- This exact-1/16 return occurs in the data with POSITIVE energies and no binary dihedral rep: det-1 mirrors T-bar(3,5), (3,7), (5,7): m_1, m_2 < 1/8
  (0.0854, 0.1239, 0.1244, 0.1248), so g_A x = 0 and the bottom is returned through T, with eta_a = 0.0037, 0.0027, 0.0017 and E_M = 1/16 - eta_a > 0.
  (Conditional on the triangle structure; these are det 1, not Delta = 1.)

## 5. Conjecture R and its bullets.  Verdict: R as stated UNSUPPORTED/ill-posed (false as a tautology, chain-level, an energy hypothesis in disguise); bullet 1 WRONG as phrased; bullet 2 non sequitur; bullet 3 partly CIRCULAR.

- R is a statement about which generator g_M hits at chain level: not invariant under filtered homotopy equivalence; a "position of generators" hypothesis (rule 4).
  In perfect (Seifert) examples (return) holds in every case (F1: w = x). A "test that decides it" on mirror torus knots and 4_1 would return "yes" on all of them, including all 211.
- Bullet 1: zero energy of a (eta_a = 0) needs a flat singular connection = traceless rep with lambda -> -1 (P_0) or +1 (P_1) (strategy-exact §2, triangle-1 §5.6). Binary dihedral reps are metabelian,
  so lambda -> +1: they are zero-energy only for a' (P_1, triangle II, the (1/4,0) point). The (1/4,1/2) point (P_0, triangle I) is never binary dihedral.
  Non-binary-dihedral traceless reps with lambda -> +-1 exist: every irreducible traceless rep of T(p,q) with pq even (lambda = x^p mu^-pq, mu^pq = +-1); strategy-exact §7.2 says
  the det>1 mirror bottoms are "binary dihedral or lambda -> -1 traceless". Absence for Delta_K = 1 is a Thom-genericity assumption (Gamma_K misses (1/4,0), (1/4,1/2)), not a consequence of
  "(det K - 1)/2 = 0 binary dihedral". Other zero-energy configurations: mixed common points alpha in {1/8, 3/8} (flat on +-E, energy 0 for c, E_M = 0 for g_M); also removable by Thom.
  More importantly, ruling out ZERO energy says nothing about returns with positive energies summing to 1/16: positivity cannot exclude eta_a + E_M = 1/16 (item 4: det-1 data realise it).
  "This is the only mechanism the data ever show" is false: the det-1 mirrors are all returns through T at positive energy.
- Bullet 2: g_M has the gamma_1 end as an asymptotic end and NO cap; the minimal cap 1/(4|S.S|) = 1/16 appears at the L(4,1)-face of g_A (family on W'), not in g_M.
  The "1/16 = level(g_M) - level(a)" is rho(gamma_1)/16 bookkeeping. Energy of an instanton with fixed endpoints is fixed by CS values: E = 1/16 is an arithmetic coincidence of CS values,
  it does not force a broken (flat + minimal cap) configuration; that holds only in the neck-stretching limit, and uses an energy lower bound for the cap region. Non sequitur. The author concedes
  "what remains ... is the genuinely open part"; that remainder is the whole statement.
- Bullet 3: see 3; additionally every one of the 211 cases is Delta != 1 (no Seifert nontrivial knot with Delta = 1), so the data say nothing about R in its stated range.
- Energy estimate in disguise: YES. (D) delta <= 1/16 + eta_g: if delta <= 1/16 then eta_g is irrelevant and one needs a bound on the CS-gap between two classes of I(Y_2) (positions of generators, rule 4;
  by Lemma 3.1 gaps are energy minus 1/8). If delta > 1/16 it is eta_g >= delta - 1/16 > 0: a positive lower bound on a specific instanton energy (rule 1). (D) is literally
  "the g_A-image of the kappa class sits at level <= lambda - 1/16", i.e. the conclusion for a named witness. Not equivalent to m >= 1/16 (only sufficient), but no easier.
  Thom cannot give it: avoiding common points gives eta > 0, not eta >= delta - 1/16.

## Corrections needed
1. Replace m_1 >= 1/8 - delta + eta_g by Thm 5.1(i) with min(eta_g, eta_a + eta_b - beta(T)); state the chain-kernel case separately (minimal-level representative in ker a).
2. Delete the claim that Psi covers ker a_*; Model 3 is a counterexample. Say Psi is not homotopy invariant.
3. Remove "structural reason" and "tight in both cases"; 4_1's eta_g is fitted (eta_g <= 3/80 only); T(2,-3) is a coincidence of independently computed numbers.
4. Delete the derivation of (D) from the vertex relation: xi - [w] = 0 identically. Replace by (a) the general inequality "eta_g + eta_c <= 1/16 or eta_a + E_M <= 1/16",
   (b) the perfect-case dichotomy (g_A x != 0 => m_1 > 1/8, else exact return with eta_a + E_M = 1/16).
5. Restate Conjecture R or drop it; as written it is tautological; the "test that decides it" is vacuous.
6. Correct bullet 1 (lambda -> -1 vs +1; non-dihedral traceless reps; genericity not binary dihedral count; positive-energy returns exist in det-1 data).
7. Delete the cap argument in bullet 2 (g_M has no cap).
8. Admit (D) is an energy/position hypothesis (rules 1 and 4); the paper currently proves nothing beyond Thm 5.1.
