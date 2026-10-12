# r8/hyp.md — hyperbolic / complex-CS route to S^3_2(K) != S^3_{-2}(K)

Status log (update after each step).

## Step 0 (initial checks of established facts)

F1 spin swap (Kirby–Melvin). C = char. sublink. C=empty: mu = sigma(X_n) = sign n.
C = K: mu = sigma - n + 8Arf. So (Y_2: s0->1, s1->-1+8Arf), (Y_-2: s0->-1, s1->1+8Arf). Arf=0 => phi:Y_-2->Y_2 sends s1->s0, s0->s1. CONFIRMED.

Peripheral lift traces. Principle: for a peripheral parabolic gamma, lifted trace is -2 iff the
induced spin structure on gamma (framed by the cusp torus) is the BOUNDING one; +2 iff Lie.
S^3-spin restricted to E_K: mu bounds disk (0-framing = torus framing) -> bounding; lambda bounds
Seifert surface (Seifert framing = torus framing) -> bounding. Hence tr mu = tr lambda = -2 for the
S^3 lift. CONFIRMED (consistent with Calegari tr lambda = -2 for all lifts, since lambda = 0 in H_1(E;Z/2)).
Other lift: tr mu = +2.
Both spin structures of E_K extend over the slope n mu + lambda filling for n even (q(n mu+lambda)=q(lambda)=0). OK.

CAVEAT on "tr rho_{s0}(c2) = -2cosh(L2/2)": the sign is only meaningful once L2 is fixed mod 4 pi i.
L(core) is only defined mod 2 pi i; replacing the dual curve mu by mu + m (m = filling slope) shifts
the continuous log by 2 pi i and flips the sign. The statement is correct as: lifted complex length
of c2 in (Y2,s0) = L_def(mu) + 2 pi i (mod 4 pi i), where L_def is the continuous log along the
deformation and mu is the dual curve; for c_{-2} in (Y_-2,s1) it is L'_def(mu) (no shift).
Also: the cone deformation 0 -> 2pi is NOT known to exist in general (Hodgson–Kerckhoff need
normalized length >~ 7.5); without it, use any path on the canonical component, but then the
normalization of Im L may wind. Becomes intrinsic only if |Im L| < pi with no winding (long slopes).

Spin-refined CS (new, checked): for SL(2,C) lifts rho, rho*eps of a closed M,
cs(rho*eps) - cs(rho) = <eps^3,[M]>/2 mod 1 (SU(2) units; WZW of non-liftable gauge g:M->SO(3)).
Check: RP^3 central rep CS=1/2 (OK), L(4,1) eps^3=0 (OK). For Y_{+-2}: H_1=Z/2, eps^3 != 0, so
cs(Y,s1) = cs(Y,s0) + 1/2. PSL CS determines cs mod 1/2; the spin refinement is exactly ONE bit:
which spin structure carries which of {a, a+1/2}.

Coordinator refocus (received): centre = can Vol / complex CS be specialisations of a gauge-theoretic
concept (holomorphic CS, Kirk–Klassen, Kapustin–Witten/Haydys–Witten, Abouzaid–Manolescu,
Lefschetz thimbles). Verdict needed.

## Step 1 (refocus: complex CS as specialisation) — analysis

(i) CS_C(A), A = omega + i e flat hyperbolic: cs_C = (CS + i Vol)/(2 pi^2) in SU(2) units (sign conv.).
Yoshida '85, Kirk–Klassen '93. PROVED/classical. Rep volume = 2pi^2 Im cs_C (Dupont/Cheeger–Simons).
Spin: cs_C(Y,s1) = cs_C(Y,s0) + 1/2 for Y_{+-2} (eps^3 != 0). So under cosmetic phi:
   cs_C(Y_2,s0) - cs_C(Y_-2,s0) = 1/2 mod Z   (PSL alone only gives in {0,1/2}).
   => THE FORCED LIFT PAIRING = exactly one bit; a knot-specific test, not a contradiction.

(ii) Complexify pillowcase: u = 2 pi i a, v = 2 pi i b. 2(a-1/4)db = -(1/2pi^2)(u - i pi/2)dv.
On complex surgery line N u + v = i pi eps: -(1/2pi^2)(u-i pi/2)dv = d[(N/4pi^2)(u-i pi/2)^2]
and (N/4pi^2)(u - i pi/2)^2 = -N(a-1/4)^2.  CHECKS with slope2.tex.
On N u + v = 2 pi i k the quadratic (N u^2 + u v)/2 = pi i k u is LINEAR in u = log of core
eigenvalue (dual curve mu): this is the Yoshida/Neumann core-length term. So the SU(2) slope term
and the hyperbolic Dehn-filling correction are literally the same holomorphic expression. CONFIRMED.
Potential F is a section of the (complex) CS bundle over (C*)^2/+-; well-defined mod Z on each
component of the eigenvalue variety (Kirk–Klassen: loops of reps of E_K have integral period).
SU(2) arcs on X_0? Unknown in general. For Delta=1, X_0 misses the reducible line entirely
(no roots of Delta(M^2)), so no reducible anchor; SU(2) curves Gamma may lie on other components.

(iii) Theta-flows of Re(e^{i theta} cs_C): Hamiltonian => Im(e^{i theta} cs_C) conserved; 
topological level on cobordisms (c_2, or 1/4 Z for PSL) is REAL. theta=0 flows between ends need
equal Vol: automatically true under cosmetic hypothesis. No obstruction from filtration.
Volume rigidity (Gromov–Thurston, Dunfield '99, Francaviglia–Klaff, BCG): |Vol rho| <= Vol(Y),
equality iff rho in {rho_hyp, conj}. So chi_hyp is the sharp TOP of the Im-filtration (isolated,
nondegenerate since H^1(Y;Ad)=0) -> rank-1 top piece of any vanishing-cycle theory (AM's HP).
BUT the a priori bound is on Im; SU(2) levels are Re (Im=0 on SU(2)); the filtrations are transverse.
Orientation: Y -> -Y sends hyperbolic cs_C = CS + iV to -CS + iV. Vol is orientation-blind.
Amphichiral K: Y_-2 = -Y_2, so every Im-only argument is satisfied by the chirally-cosmetic map;
=> any theta=pi/2 (volume) mechanism must fail. Orientation lives only in Re = CS, which has no
rigidity/extremality.
Complexified rotation identity (slope2.tex Prop) is algebraic, so holds holomorphically on X_0:
 cs_C(Y_2,x2)-cs_C(Y_-2,x_-2) = g_P - int_gamma (a(x_t)-a_P)^2 dt (+ discrete terms)
with a complex: integrand has no sign. Cosmetic => one complex equation (Re: CS; Im: Vol);
codim-2 condition on X_0, not a contradiction.
Cobordisms W_{lambda'}, X': flat conns have mu^2=1 (resp mu^4=1), lambda-relations -> only orbifold
points of X_0 (M = +-i, M^4=1), never hyperbolic Dehn-filling points. Exact cobordism relations
only among non-hyperbolic characters = back to the SU(2)/orbifold problem.

## Step 2 (coordinator: complexified pillowcase design; questions (1),(3) only; 1/16 dropped)

(1) Correctness of the design.
- Omega = du^dv on (C*)^2/+- OK; any holomorphic curve is Lagrangian for every Re(e^{-i th}Omega).
- Shear T(m,l)=(m,ml): preserves Omega, fixes {m=1} ptwise, T^4(L_2)=L_-2 (check: m^-2 m^4 l = m^2 l). OK.
  T does NOT commute with lift-swap m->-m; T^2 does. Hamiltonian H=u^2/2; action shift for T^4 is 4u^2
  (times normalisation) = complexification of the real slope term. OK.
- Lift/spin: A_K has only even powers of m; lift swap chi: m -> -m. In SU(2) coords chi(a,b)=(1/2-a,-b),
  i.e. the project's involution chi IS the spin/lift swap. Edges m=1 and m=-1 swapped by chi.
- "Exactness"/K2: periods of the CS form on C_K are trivial in the CS line bundle sense (Kirk–Klassen:
  E_K gives a flat section over its rep curve) => C_K is Bohr–Sommerfeld for the complex CS bundle;
  value at x in C_K ∩ L_N = ratio of the E_K-section and solid-torus section = cs_C(Y_N,x) in C/Z.
  The ADDITIVE CONSTANT on each component of C_K is the cusped complex volume (or cs of some rep),
  a transcendental knot invariant: for Delta=1, X_0 never meets the reducible line, so no topological anchor.
- Ideal points: ends of C_K asymptotic to cylinders {m^p l^q = root of unity} (CCGLS tame symbols);
  #(C_K ∩ L_N) = Culler–Shalen norm ||N mu + lambda|| = sum_P w_P |Delta(N,beta_P)|. The complex theory
  is NOT Hamiltonian-invariant under T^4: points escape through ideal points with beta in between.
  Count difference ||2||-||-2|| = -sum w_P q_P g(beta_P), g odd (2beta if |beta|<=2, 4sgn beta else):
  an "unfiltered" obstruction absent in SU(2) (= SL(2,C) Casson, Boden–Curtis/Ichihara–Saito). Knot-specific.
- Pivots: L_2 ∩ L_-2 = {m^4=1, l=m^-2} = {(+-1,1),(+-i,-1)}: exactly where flat conns on X' live (fact 4).
- Reducibles of Y_{+-2} (SL): (m,l)=(+-1,1) central. (+-i,1) are PSL w2!=0 points on L^-.
- GENUINE INVARIANTS: (a) finite char scheme X_SL(Y_N) with cs_C: X -> C/Z and H^1(Y;Z/2)-action;
  (b) Abouzaid–Manolescu HP(Y) (unfiltered, no cobordism maps); (c) lambda_SL (Curtis).
  NOT known invariant: HF(C_K,L_N) in (C*)^2/+- (splitting-dependent: misses components on which
  restriction is constant, orbifold points, ends); Stokes numbers (need KW on Y x R; adiabatic
  limit unproven).

(3) KEY NEW OBSERVATION — spin-refined Schlafli obstruction (candidate theorem).
 Under cosmetic phi: cs(Y_2,s0) - cs(Y_-2,s0) = 1/2 mod 1 (SU(2) units) [= pi^2 mod 2pi^2 standard].
 Both (Y_{+-2},s0) are reached from the SAME complete S^3-lift by cone deformations along slopes +-2
 (lift continues; tr rho(m_fill) = -2cos(alpha/2) -> +2 at 2pi, so it descends: it is s0).
 Complex Schlafli: d(Vol + i CS) = -(1/2)(l + i tau) d alpha along cone deformations.
 => cs(Y_2,s0)-cs(Y_-2,s0) = (1/2pi^2)(1/2) int_0^{2pi} (tau_{-2}(a) - tau_2(a)) da   EXACTLY (real number).
 So cosmetic needs int |tau_2 - tau_-2| >= 2 pi^2, i.e. average |tau_2-tau_-2| >= pi.
 THEOREM (PLAUSIBLE): if both cone deformations 0->2pi exist and int_0^{2pi}|tau_2 - tau_-2| da < 2pi^2
 (e.g. |tau_{+-2}(a)| < pi/2 throughout), then S^3_2(K) != S^3_-2(K).
 NZ leading order: tau_N(a) ~ -a(N+x)/|N+tau|^2 (tau = x+iy cusp shape) => |Delta_CS| <= pi^2/y:
 leading-order condition is Im(cusp shape) > 1.  TODO: numerics (SnapPy real Dehn filling).

## Step 3 (numerics + rigor of the spin–Schlafli criterion)

NUMERICS (SnapPy 3.3.2, code in r8/code/schlafli.py): along cone paths dehn_fill((N/s,1/s)), s in (0,1]
(alpha = 2 pi s), with H = holonomy log of knot meridian mu (dual curve), ell=|Re H|, tor = Im H:
  K11n42 (KT), N=+2: dVol = -1.270099 = -(1/2) int ell dalpha (6 digits); dCS_snappy = 0.057565 = (1/4pi^2) int tor dalpha.
                N=-2: dVol = -2.254142 (match), dCS = -0.004165 (match).  max|tor| = 0.729 (N=2), 0.055 (N=-2).
  SnapPy chern_simons() = CS/(2pi^2) = SU(2)-units cs (mod 1/2). Schlafli verified EXACTLY (no mod-1/2 slip).
  => KT: Delta = cs(Y2,s0)-cs(Y-2,s0) = 0.0617, far from 1/2. (Volume already separates, as expected.)

RIGOR of "same constant for N=+2 and N=-2" (the only place a hidden 1/2 could live):
  KK solid-torus term for slope (N,1): reps core->exp(2 pi i w), boundary (a,b)=(-w, Nw)+(0,k);
  cs_rel(V_N) = N a^2 -+ 2 k a. At the s0 (S^3-lift) Dehn-filling point (a,b) ~ (1/2,1/2), k = N/2+1.
  Constant part = N/4 -+ (N/2+1) == N/4 (mod 1). N=+2 and N=-2 both give 1/2 mod 1 => EQUAL.
  Cross-check with unknot/lens spaces: central rep mu -> -I on L(N,1) has cs = -(N/2)^2/N = -N/4 mod 1:
  the N/4 (mod 1) alternation is real; and N=+-2 agree. Along the path, the -a dalpha/2pi piece of the
  KK form contributes -1/2 for BOTH N (a_P = 1/2), cancels in Delta.
  Also: Schlafli must use the SAME dual curve mu for both N (mu . (+-2mu+lambda) = 1); using mu+m_fill
  would shift by int alpha dalpha/4pi^2 = 1/2 — exactly the spin bit, consistent.

THEOREM (Spin–Schlafli criterion). K hyperbolic, Arf(K)=0. Suppose continuous paths of (cone) hyperbolic
structures / SL(2,C) reps on the canonical component join the complete structure to the +-2 fillings,
and tau_{+-2}(alpha) = Im log hol(mu) along them (continuous, 0 at alpha=0). If
   (1/4pi^2) | int_0^{2pi} (tau_2 - tau_{-2}) dalpha |  < 1/2     (e.g. sup|tau_2|+sup|tau_-2| < pi),
then S^3_2(K) != S^3_{-2}(K).  Proof: cosmetic => (Mostow) isometry pairing hyperbolic chars, spin swap
=> cs(Y2,s0) = cs(Y-2,s1) = cs(Y-2,s0)+1/2 (eps^3!=0); KK/Schlafli => cs(Y2,s0)-cs(Y-2,s0) = Delta exactly mod 1.
Status: PROVED modulo KK sign conventions (all conventions give the same constants) — call it PROVED(sketch).

## Step 4 (literature, short)
- Ravelomanana arXiv:1505.00238 Thm 1.4: exceptional purely cosmetic slopes on hyperbolic K must be {+1,-1}
  => for +-2 both fillings hyperbolic (K hyperbolic). Ren arXiv:2411.13828: if some knot in S^3 has purely
  cosmetic surgeries then a hyperbolic one does (so K hyperbolic WLOG).
- Futer–Purcell–Schleimer, "Excluding cosmetic surgeries on hyperbolic 3-manifolds" (arXiv:2403.10448, JoCG 2025):
  effective drilling/filling; long slopes => core = shortest geodesic; computationally: no purely cosmetic
  surgeries for knots <= 19 crossings and all 1-cusped census manifolds.
- Ren arXiv:2604.02672 (Apr 2026): infinite families of chirally cosmetic surgeries on CHIRAL hyperbolic knots,
  and PURELY cosmetic surgeries on multi-cusped hyperbolic manifolds. => any purely hyperbolic-geometric
  mechanism must use S^3-specific input. Our criterion uses the S^3 spin swap (Arf=0), consistent.
- SL(2,C) Casson: Ichihara–Saito (2-bridge), Boden–Curtis surgery formula via Culler–Shalen norm; Detcherry
  (quantum, 5th root), Ito (LMO), Ichihara–Wu (V'''(1)=0). All knot-specific/finite-type; not used.

## Step 5 (design-language reading of the criterion)
- Cone path for slope N at angle alpha: N u' + v' = i alpha/2 (u'=log(-m), v'=log(-l), SL logs).
  For fixed alpha all these lines pass through (m,l) = (-1, -e^{i alpha/2}); at alpha=2pi this is the pivot
  P=(-1,1). So the +-2 hyperbolic points sit at the ends of two "spokes" of C_K leaving the S^3-cusp point
  (-1,-1) on the edge {m=-1}. Delta = difference of the CS action along the two spokes = twist integral.
- Roles of the phases: theta=pi/2 (Vol) + Mostow/Gromov–Thurston rigidity => the carrier is canonical
  (phi must pair the two hyperbolic characters; no "where does the carrier sit" problem).
  theta=0 (CS) + forced lift pairing => exact identity Delta == 1/2 (mod 1): a GAP of half a period.
  Schlafli on the spokes => |Delta| <= (1/4pi^2) int |tau_2 - tau_-2| : violated whenever twists are moderate.
- Complex form: Z_K := (1/4pi^2) int_0^{2pi} (H_2 - H_-2)(alpha) dalpha (H = log hol mu, complex);
  cosmetic => Z_K in 1/2 + Z (Im part = volume equality, Re part = spin-shifted CS).
- Special to +-2: for +-1/q, H_1 = 0, one spin structure, no half-period gap.

## Step 6 (survey, Rolfsen <= 10 crossings, 241 hyperbolic knots, 40-step cone paths; code/survey.py, survey10.json)
- Schlafli twist integral == SnapPy CS(Y_{+-2}) - CS(E) mod 1/2 for ALL 241 knots (482 paths): formula validated.
- 217 knots with both paths through positively oriented solutions: max |Delta| = 0.135, median 0.014;
  max (sup|tau_2| + sup|tau_-2|) = 2.72 < pi  => the crude sufficient condition holds for every one.
- 24 "dirty" paths (flat/negatively oriented; mostly exceptional +-2 slopes, e.g. 8_20, 10_1): |Delta| <= 0.27.
- So Delta == 1/2 (needed for cosmetic) is missed by a factor >= 3.7 everywhere tested. Running: Delta=1 knots <= 13 xings.

## Step 7 (genus-2, Delta_K=1 knots <= 13 crossings; code/findD1.py, d1crit.py; 120-step paths)
Alexander-trivial knots found (HFK): K11n34(g3) K11n42(g2) K12n313(g2) K12n430(g2) K13n65(g3) K13n71(g2)
K13n866(g3) K13n1019(g2) K13n1496(g2,tau=1) K13n1756(g2) K13n1757(g2) K13n3871/3872/3897(g4) K13n3934/3936/3938/4582(g3) K13n4591(g2).
Criterion on all genus-2 ones: Delta = 0.0617, 0.0579, 0.0664, 0.0283, 0.0762, 0.0562, 0.0709, 0.0558, 0.0478;
sup|tau| <= 0.784; Schlafli vs SnapPy CS agree mod 1/2 to <1e-6; Im(cusp shape) in [4.0, 7.3].
=> every genus-2 Delta=1 knot <= 13 crossings satisfies the criterion with margin >= 6.5x (numerical, uncertified).
Slopes +-2 are SHORT here (normalized length ~2.8 for KT), far outside Hodgson–Kerckhoff/FPS proven ranges.
NZ leading order: Delta ~ (1/2)[(2+x)/|tau+2|^2 - (x-2)/|tau-2|^2], |Delta| <= 1/(2 Im tau); matches survey
with median error 1e-3. min Im tau over knots <= 10 xings = 1.80.

## VERDICT
(1) Complexified pillowcase: RIGHT as a 3-dimensional framework (KK complexified + NZ/Yoshida), with fixes:
  chi = lift/spin swap; constants are N/4 mod 1 in the s0 (m=-1) gauge (lens-space check); K2/periods automatic
  (Bohr–Sommerfeld for the CS bundle); additive constant per component is transcendental for Delta=1;
  ideal points = boundary slopes, break Hamiltonian invariance of T^4 (that is the SL(2,C) Casson count);
  genuine invariants: (X_SL(Y_N), cs_C, H^1(Z/2)-action), lambda_SL, AM's HP. HF(C_K,L_N) and Stokes data: not invariants (yet).
(3) YES for a testable class, but not via 4D theory: theta=pi/2 + rigidity fixes the carrier; theta=0 + forced lift
  pairing gives the half-period gap Delta == 1/2; Schlafli on the two spokes bounds Delta by the twist.
  Spin–Schlafli criterion (PROVED modulo KK-convention bookkeeping + path hypothesis). Not a uniform proof:
  needs the cone paths and a twist bound for short slopes; no a priori control known.
  Sharp negatives: Vol alone orientation-blind (amphichiral); 4D theta-flows conserve Im and have real levels =>
  no gap; faithful reps don't cross 2-handles; Ren 2026 purely cosmetic multi-cusped examples => S^3 input
  (the spin swap) is indispensable.
