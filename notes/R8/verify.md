# R8/verify.md — independent referee check of L1, L2, L3, P (spin–Schläfli criterion)

Status log; updated after each step. Code in R8/vcode/.

## Step 0 — plan
(a) L1 via Freedman–Kirby characteristic surfaces; (b) L2 via Cheeger–Simons and via WZ of non-liftable gauge,
lens spaces exact; (c) exact SU(2) torus-knot analogue of (P); (d) mod-1 SL(2,C) CS via an independent
Kirk–Klassen path from an abelian (cs = 0) base point on the Riley curve of 2-bridge knots; (e) amphichiral check.

First theoretical red flag (to be tested): UNITS. Direct computation (below) gives, in SU(2) units,
|Im cs_C(hyperbolic)| = Vol/(4 pi^2), not Vol/(2 pi^2). Since Vol + i*2pi^2*x_snappy is holomorphic
(dVol = -(1/2) l dα, d x_snappy = (1/4pi^2) τ dα, both checked in hyp.md Step 3), this would force
x_snappy = 2 * cs_SU(2): SnapPy gives cs_SU(2) only mod 1/4, and the spin bit (1/2 in SU(2) units) is 1 in SnapPy units.

## Step 1 — normalisation facts (decisive for everything below)
- SnapPy: chern_simons() = CS_conv/(2 pi^2), complex_volume() = Vol + i CS_conv (checked: m003 -> 0.25, 5_2 -> -0.15320).
- Direct form computation (SU(2) units, A = (omega + i e)(-i/2)sigma, CS-form of a flat A = (1/96 pi^2) eps_ijk Ω^iΩ^jΩ^k):
  Re cs_C = cs(omega_spin) exactly (torsion-free), Im integrand = (1/2)d(omega.e) - 2 dvol  =>  Im cs_C = -Vol/(4 pi^2).
  Calibration of the same algebra on round S^3 (A_± = omega ± e): CS(A_+) - CS(A_-) = Vol(S^3)/(2 pi^2) = 1. OK.
  Volume-conjecture normalisation (|J_N| ~ e^{N Vol/2pi}, exp(ik W), W = 2 pi cs) gives the same |Im cs| = Vol/4pi^2.
- Holomorphy + Schläfli (dVol = -(1/2) l dα, d x_snappy = (1/4pi^2) τ dα) => d Re cs_C = (1/8 pi^2) τ dα and
  **x_snappy = 2 cs_SU(2)**.  SnapPy's "mod 1/2" is mod 1/4 in SU(2) units; the spin bit (1/2 in SU(2) units) is 1 in x-units.
- Closed census sanity: all 37 amphichiral closed census manifolds have x_snappy = 0 mod 1/2 (vcode/amph_closed.py),
  as forced by x = 2cs (cs = -cs mod 1/2 => x in {0,1/2} mod 1); under x = cs the value 1/4 would be allowed. (consistent, not decisive)

## Step 2 — (c) exact torus-knot analogue (vcode/torus_test.py), exact rational arithmetic
Base a = 1/2 on the line b = k/2 - pq a (k - pq odd: tr mu = tr lambda = -2, the "S^3-lift"), H_mu = 4 pi i (a - 1/2),
cone angle by N H_mu + H_lambda = i α, endpoint a_N = 1/2 - 1/(2(pq-N)), τ_N = α/(N-pq), ∫τ_N = 2pi^2/(N-pq).
Exact CS (tk.py formula; re-checked = FS on Σ(2,3,7), Σ(2,3,5) up to global sign) gives, for ALL 44 arcs of 12 torus knots:
   D_exact = CS(Y_2,a_2) - CS(Y_-2,a_-2) = (1/8pi^2)∫(τ_2 - τ_-2) = Delta/2 (mod 1)  [e.g. T(2,3): D = 31/32 = -1/32]
   and NEVER = Delta (manuscript (P) in SU(2) units: -1/16).   c_2 == c_-2 (mod 1) confirmed.
   (Endpoints are SL(2,R)-type real reps beyond the SU(2) arc; the CS formula there is the KK continuation.)

## Step 3 — (d) first result, KK from an abelian character (cs = 0 exactly) on the Riley curve (vcode/kkpath.py)
6_2 (b(11,3), SnapPy's RationalTangle orientation), N=+2:
   cs(Y_2,s0) = 0.375832 - 0.101213 i ;  Vol/4pi^2 = 0.1012135 ;  Re cs mod 1/4 = 0.125832 vs x_snappy/2 mod 1/4 = 0.125835.
   cs(Y_2,s1) = cs(Y_2,s0) + 0.5000000  (L2 directly, hyperbolic SL(2,C) rep).
   => numerically: Im cs_SU2 = -Vol/4pi^2 and Re cs_SU2 = x_snappy/2 (mod 1/4).  Unit claim CONFIRMED.

## Step 4 — (a) L1 re-derived (Freedman–Kirby characteristic surfaces, not the KM linking-matrix formula)
Y_n = ∂X_n, X_n = B^4 ∪_K 2-handle (framing n even). H^1(X_n;Z/2)=0 and Q_X=(n) even => X_n spin, unique spin str.,
restricting to s0 on Y_n (so s0 = the one extending over the trace; s1 does not extend, since the restriction is onto a single class).
s1 = spin str. on Y_n extending over X_n - F, F = (pushed-in Seifert surface) ∪ core: F characteristic (F.x = x.x mod 2 for the generator),
F.F = n, Arf(X_n,F) = Arf(K) (the Seifert form's quadratic refinement).  Generalised Rokhlin (Freedman–Kirby / Kirby–Melvin):
   mu(Y,s_F) = sigma(X) - F.F + 8 Arf(F) mod 16.
=> mu(Y_2,s0)=1, mu(Y_2,s1)=-1+8Arf, mu(Y_-2,s0)=-1, mu(Y_-2,s1)=1+8Arf.  1 != -1 mod 16, mu is a homeomorphism invariant
(3-manifolds: homeo ~ diffeo).  Arf=0 => any or.-pres. homeo Y_-2 -> Y_2 sends s1 -> s0 and s0 -> s1.  (Arf=1 => {-1,9} vs {1,7}:
no homeo at all, recovering Boyer–Lines' Arf condition.)  Unknot sanity: RP^3 has mu = {1,-1}.  L1 CONFIRMED.

## Step 5 — (b) L2 re-derived two ways + exact tests (vcode/l2_tests.py)
(i) Cheeger–Simons: c(E⊗L) = 1 + (c1E+2c1L) + (c2E + c1E c1L + c1L^2); for SL2, ĉ1(E)=0 (det trivial as a flat character), so
    ĉ2(E⊗L_eps) - ĉ2(E) = ĉ1(L)*ĉ1(L) = <u ∪ βu,[Y]>, u = eps/2 ∈ H^1(Y;R/Z)  = linking form λ(g,g) of the order-2 class g.
    Y_{±2}: λ(μ,μ) = ∓1/2 = 1/2 mod 1.  (Identity holds for differential characters: both sides are natural characters with equal
    curvature forms and integral classes on BU(2)xBU(1), which has no odd cohomology.)
(ii) WZ: the two lifts are related by a gauge transformation g: Y -> PSL2(C) ≃ SO(3) with g^*(x) = eps, x ∈ H^1(SO(3);Z/2).
    WZ(g) = deg(g)/2 (SU(2) units; SU(2)->SO(3) has degree 2), deg(g) mod 2 = <g^*x^3,[Y]> = <eps^3,[Y]>.  Holomorphic WZ form on
    PSL2(C) has the real class, so this holds for SL2(C).
(iii) Lens spaces, cs via the disk bundle D_p (reducible U(1) extension, -c1(L)^2 = -k^2/p): twist k->k+p/2 shifts cs by p/4:
    L(2,1): 1/2 (central rep 1/2), L(4,1): 0, L(6,1): 1/2, L(8,1): 0, L(10,1): 1/2  == self-linking == [eps^3 != 0]. OK.
(iv) Torus knots: every chi-pair (x, x⊗eps) of SU(2) flat connections on Y_{±2}(T(p,q)), 8 torus knots, both signs: ΔCS = 1/2 exactly.
(v) Hyperbolic SL2(C), KK from abelian base (Step 3): cs(Y_2(6_2),s1) - cs(Y_2(6_2),s0) = 0.5000000.
L2 CONFIRMED (in SU(2) units).

## Step 6 — (e) amphichiral, PSL level (vcode/amph_knots.py; 20 amphichiral knots <= 10 crossings)
x_snappy(E_K) = 0, I_{-2} = -I_2 to 1e-16, x(Y_2)+x(Y_-2) = 0 mod 1/2, x(Y_2) = I_2 mod 1/2.  Consistent with the formula under
EITHER normalisation (amphichiral symmetry is a PSL-level identity: corrected formula gives cs(Y2,s0) = C_E+1/2+I_2/2 with
2C_E = 0, manuscript gives cs(E)+1/2+I_2 with 2cs(E)=0; both self-consistent).  Not discriminating at SnapPy resolution;
the mod-1 discrimination for amphichiral 6_3, 8_12 is done by KK in Step 7.

## Step 6b — Ptolemy route (task option d) not usable
snappy.ptolemy complex_volume_numerical: "Complex volume is defined up to i*pi^2/6" -> far coarser than the bit; also needs
Magma/Sage to solve Ptolemy varieties of closed fillings. Replaced by the Kirk–Klassen/Riley route (exact base cs = 0).
Note: for Δ_K = 1 knots (KT etc.) there is NO abelian anchor on X_0 (no roots of Δ), so the anchored mod-1 test is only
possible for knots with nontrivial Δ; the bookkeeping identity tested is knot-independent (c_E cancels).

## Step 7a — independent derivation of (P) by Kirk–Klassen (no Schläfli), SU(2) units
Normal form a = 1/2 + H_mu/(4 pi i), b = 1/2 + H_lambda/(4 pi i) (S^3 lift, eigenvalue -e^{H/2}), N H_mu + H_lambda = i α.
∫_0^{2pi}(a db - b da) = (1/2pi)∫h dα + 1/4 - ((N+2)/2) h(2pi)   (h = H_mu/4 pi i);  endpoint n = N a + b = N/2+1 ∈ Z;
solid torus (dual mu): n·a_end = (N+2)/4 + ((N+2)/2) h(2pi).  The h(2pi) terms cancel:
   cs(Y_N,s0) = c_E + (N+3)/4 + (1/8 pi^2) ∫_0^{2pi} τ_N dα   (mod 1),  c_E = relative cs of the complete S^3-lift at (1/2,1/2).
 - dual-curve choice is IMMATERIAL inside KK: d -> d + m_fill changes the solid-torus term by n^2 ∈ Z;
 - c_2 - c_-2 = 5/4 - 1/4 = 1 == 0 (mod 1): the manuscript's "c_2 = c_-2" is right;
 - the integral coefficient is 1/(8 pi^2), NOT 1/(4 pi^2): in x_snappy units x = 2cs it is 1/(4pi^2) but then mod 2.

## Step 7 — (d) mod-1 SL(2,C) CS by Kirk–Klassen from abelian characters (vcode/kk2.py, riley.py, kkpath.py)
Method: Riley rep of the 2-bridge group (chirality + longitude orientation fixed by matching H(λ)/H(μ) near the cusp to SnapPy);
s0 endpoint = S^3-lift (M=-1) tracked along SnapPy's cone path (M = -e^{H/2}); check M^N L = 1 at α=2π (|err| < 1e-12: L3 numerically);
s1 = (-M, same u). Then KK integral ∫(a db - b da) from an abelian character (Δ(M0^2)=0, b=0, cs=0 EXACT) to the endpoint along
several different paths/base points + solid-torus term (Na+b)a. Paths with |Im cs + Vol/4pi^2| > 2e-5 discarded (sheet jumps).
Results (SU(2) units; D = cs(Y2,s0) - cs(Y-2,s0) mod 1; Δ_K = (1/4pi^2)∫(τ_2 - τ_-2) as in the manuscript):
  knot        D (KK, mod 1)   Δ_K/2 mod 1   Δ_K mod 1    | Im cs = -Vol/4pi^2 | Re cs = x/2 mod 1/4 | cs(s1)-cs(s0)
  6_2 b(11,3) 0.992879        0.992879      0.985757     yes (1e-6)            yes                  0.5000000
  7_3 b(13,3) 0.9909986       0.9909988     0.9819976    yes                   yes                  0.4999998 / 0.4999999
  6_3 b(13,5) 0.0225208       0.0225206     0.0450413    yes                   yes                  0.4999937 / 0.5000005
Amphichiral 6_3 (task e, now at mod 1): cs(Y2,s0) = 0.511260, cs(Y-2,s0) = 0.488739: sum = 0 mod 1 (Y_-2 = -Y_2, s0->s0) OK;
  cs(Y2,s0) = 1/2 + I_2/2 (corrected formula with C_E = 0), whereas the manuscript's (P) needs cs(Y2,s0) = I_2 mod 1/2 = 0.0225: FAILS.

## Step 8 — fully anchored ABSOLUTE test of (P) (no free constant) — answers the coordinator's "hidden knot-dependent 1/2"
c_E computed independently: KK from an abelian character (cs=0) to the complete S^3-lift M=-1 on the Riley curve, shifted to normal
form (1/2,1/2) by the cocycle (vcode/cuspanchor.py; 4 resp. 1 independent paths; Im c_E = -Vol(E)/4pi^2 as a check).
   6_2: c_E = 0.1012450 (4 paths agree to 2e-6).  Predicted c_E + (N+3)/4 + I_N/2:  N=+2 -> 0.375834,  N=-2 -> 0.382955.
        Direct KK-from-abelian (Step 7):                                    N=+2 -> 0.375834,  N=-2 -> 0.382955.  MATCH (1e-6).
   7_3: c_E = 0.1563900.  Predicted 0.427989 / 0.436991;  direct KK 0.427990 / 0.436991.  MATCH (1e-6).
   6_3 (amphichiral): the Step-7 values force c_E = 0.25000 (i.e. C_E = c_E+3/4 = 0, as amphichirality requires).
So cs(Y_N,s0) = c_E + (N+3)/4 + (1/8pi^2)∫τ_N holds ABSOLUTELY mod 1 for each knot, with the intrinsic c_E; a knot- or
N-dependent hidden 1/2 (constants or dual curve) would show up here as an exact 1/2 mismatch.  None does.

### On the suggested annulus-twist pair test (Y_2(K) = Y_2(K'), Arf = 0, s0 -> s0)
Not decisive with the data available, for a structural reason: each side needs the exterior term c_E(K) mod 1, and SnapPy only gives
it mod 1/4 (x(E)/2).  At SnapPy resolution the pair condition reads x(E_K)+I_2(K) = x(E_K')+I_2(K') (mod 1/2), which is automatically
true (both sides equal x(Y_2) mod 1/2 by SnapPy's own filling consistency, already validated on 482 paths) and is the SAME condition
under the old and the corrected normalisation.  A mod-1 version needs an anchored c_E, which I can only produce for knots with
Δ_K != 1 and an explicit character variety (2-bridge/Riley); annulus-twist partners are not 2-bridge.  The absolute anchored test
above is strictly stronger for the question asked (it fixes c_E independently and tests constant + dual curve + coefficient per knot).

## Step 9 — referee check of claims added to the current spinschlafli.tex
- Closed amphichiral census (vcode/amph_closed2.py): 37 amphichiral; EIGHT (not seven) have H_1 = Z/2 + odd:
  m082, m078, m168, s235, s287, v2585, v1695 (Z/5+Z/10), v3283; all have chern_simons = 0.
  Argument checked: discriminant form of an even lattice with 2-part Z/2, q = ±1/2 gives Gauss-sum phase e^{±i pi/4} (odd parts give
  even contributions), so sigma(W) and hence mu(Y,s) are ODD for both spin structures; an orientation-reversing isometry sends mu -> -mu,
  so it must swap s and s'; with L2 (λ(a,a)=1/2): cs(s) = -cs(s') = -cs(s) - 1/2 => cs in {1/4,3/4} => 2cs = 1/2 = 0 mod 1/2.
  x = cs would force x = 1/4 mod 1/2.  Observed 0 on all 8: decisive refutation of x = cs, consistent with x = ±2cs.  CONFIRMED (fix count).
- "sup|τ_2|+sup|τ_-2| < 2pi suffices": |Δ_K| <= (2pi/4pi^2)(sup+sup) < 1. OK.
- "Riemannian invariant alone gives Δ_K ∈ Z": cs mod 1/2 (true PSL invariant, = Chern–Simons Φ mod 1) => Δ_K/2 ∈ (1/2)Z. OK.
- Not checked by me: 10_644 max|Δ| = 0.385, the twist agent's families, examples.md identities, the ±1/q remark.
   6_3 anchor (vcode/cuspanchor_loose.py, Im check -Vol(E)/4pi^2 = -0.144206): c_E = 0.2500024, 0.2500001 (one sheet-jumped path with
   Im = -0.14363 discarded).  Predicted 0.25+5/4+I_2/2 = 0.511260, 0.25+1/4+I_-2/2 = 0.488740; direct KK 0.511260 / 0.488739. MATCH.
   (Strict tracker vcode/kk3.py found no admissible path for 7_5/6_3 at all; the loose tracker + Im filter is what was used.)
   Unfinished (timed out, killed): 7_5, 8_2, 8_4, 7_6, 7_7, 8_12 — not needed for the verdict.

## VERDICT
L1 CONFIRMED (Freedman–Kirby char. surfaces; Rokhlin {1,-1+8Arf} vs {-1,1+8Arf}; s0 = unique spin str. of the trace).
L2 CONFIRMED in genuine SU(2) units (Cheeger–Simons, WZ, lens spaces 2/4/6/8/10, all torus-knot chi-pairs, hyperbolic KK: 0.5000000).
L3 CONFIRMED (eigenvalue -e^{iα/2} of m_fill, not merely the trace, which crosses 0 at α=pi; numerically M^N L = 1 at α=2pi to 1e-12).
P  as originally stated REFUTED: units were mixed (c_N in SU(2) units, integral in SnapPy units; SnapPy x = 2cs).  Correct form:
   cs(Y_N,s0) = c_E + (N+3)/4 + (1/8pi^2)∫τ_N dα (mod 1)  [dual curve μ, c_2 = c_-2 both CONFIRMED; dual-curve choice immaterial].
   Verified absolutely (anchored c_E, no free constant) on 6_2, 7_3, 6_3, and in difference form on 12 torus knots (exact).
Criterion: cosmetic => Δ_K ≡ 1 (mod 2) (Δ_K as in the manuscript, 1/4pi^2 normalisation); PSL alone gives Δ_K ∈ Z.
   The original "Δ_K ≡ 1/2 (mod 1)" is false; "≡ 0 mod 1" is the PSL part; oddness is the spin part.  |Δ_K|<1 suffices.
   The current spinschlafli.tex already states this corrected version; only fix found: "seven" -> "eight" amphichiral census manifolds.
