# R8/twist.md — a priori twist control for the spin–Schläfli criterion

Labels: PROVED / PLAUSIBLE / SPECULATIVE. Code in R8/code/tw_*.py.
Conventions: cusp shape tau = x+iy (mu = 1, lambda = tau). Slope N: N mu + lambda, complex length N+tau.
Normalised length L_N^2 = |N+tau|^2 / y. u_N(alpha) = log hol(mu) along slope-N cone path
(N u + v(u) = i alpha, v = log hol(lambda) = tau u + O(u^3)); tau_N = Im u_N, ell_N = Re u_N.
Z := (1/4pi^2) int_0^{2pi} (u_2 - u_{-2}) d alpha (complex); Delta = Im-part convention as in tex (twist part).
Cosmetic => Re Z = 0 (Vol) and Delta == 1/2 mod 1.

## Step 0: read spinschlafli.tex, hyp.md, schlafli.py, survey.py. Plan:
 (a) exact algebra of Z in terms of v(u); leading order; window lemma.
 (b) cusp-shape constraints for genus 2 / Delta=1 (Agol–Lackenby longitude bound, 6-thm, HK).
 (c) numerics: window, remainder Z - Z_lead, shortest geodesics of Y_{+-2}.
 (d) necessary configuration (two cores in Y_2).

## Step 1: exact reformulations (algebra; all PROVED given the cone paths)
SnapPy sign: hol(mu) log = u with Re u < 0 along paths (ell = |Re u|); Im u agrees with i alpha/(N+tau) to leading order.
(1a) Longitude form. On slope N path: N u + v = i alpha (v = log hol lambda). For N=+-2:
     u_2 - u_{-2} = i alpha - (v_2 + v_{-2})/2. Hence, with W := (1/8pi^2) int_0^{2pi} (v_2 + v_{-2}) d alpha,
        Z = i/2 - W,     Delta = 1/2 - Theta,   Theta := Im W = (1/8pi^2) int (theta_2 + theta_{-2}) d alpha,
     theta_N = Im log hol(lambda) (continuous, 0 at alpha=0).  Re W = -Re Z = (Vol(Y_2)-Vol(Y_-2))/(2pi^2) (sign conv.).
     COSMETIC  <=>(necessary)  W in iZ.     [Vol equal: Re W = 0; spin bit: Theta in Z.]
     Sanity: UNKNOT: lambda trivial, v == 0, W = 0, Delta = 1/2 exactly — and indeed S^3_{+2}(U)=RP^3=S^3_{-2}(U), Arf=0.
     So Delta - 1/2 measures how much the Seifert longitude twists; the cosmetic value is the "unknot value".
(1b) Leading order (v = tau u): W_lead = (i/2) tau^2/(tau^2-4),  Z_lead = 2i/(4-tau^2).
     W_lead in iZ  <=> tau^2/(tau^2-4) in 2Z (real) <=> tau^2 real => tau in iR (y>0) => y^2/(y^2+4) in (0,1): never.
     => LEADING ORDER HAS NO COSMETIC SOLUTION for any nondegenerate cusp (PROVED, elementary).
     Danger set {tau: W_lead in iZ} = {0, +-2sqrt2, +-sqrt(8/3), +-sqrt(16/3), ... -> +-2}: all on the REAL axis (y=0).
     Volume equality at leading order forces x = 0, and then Delta_lead = 2/(4+y^2) < 1/2.
(1c) Twist-window lemma (PROVED). If |tau_N(alpha)| <= alpha/2 for all alpha, N=+-2, then |Delta| < 1/2.
     Proof: |tau_2 - tau_-2| <= alpha, int_0^{2pi} alpha d alpha/(4pi^2) = 1/2; equality forces tau_2 = -tau_-2 = +-alpha/2
     a.e., impossible near alpha=0 where tau_N/alpha -> t_N := (N+x)/|N+tau|^2 and |t_2 - t_-2| < 1 for y>0.
     Geometric meaning: on the tube torus the dual curves are mu + k m_N with vectors (ell cosh R, (tau+k alpha) sinh R);
     |tau| <= alpha/2 <=> mu is a SHORTEST dual curve (independent of R). Equivalently (N=+-2):
     0 <= theta_N(alpha) <= 2 alpha, i.e. Theta in [0,1]: the window boundary is exactly "lambda untwisted"
     (2mu - m_2 = -lambda, 2mu + m_-2 = lambda). At alpha -> 0 window holds iff |t_N| <= 1/2, automatic if y >= 1.
     Numerics (code/tw_lam.py): Z = i/2 - W verified to 1e-14 (N u + v = i alpha holds exactly in SnapPy);
     theta_N/alpha in [0, ~1] on all genus-2 Delta=1 examples (window: [0,2]).

## Step 2: numerics — Rolfsen <= 10 (tw_survey.py, tw_rolf.json) and CensusKnots (tw_shapes.py, tw_census*.json)
 !! CensusKnots in SnapPy do NOT always carry the homological longitude: e.g. K10_349 has H1(M(0,1)) = Z/366.
    Fixed in code/tw_frame.py (find a with H1(M(a,1)) infinite, set_peripheral_curves([(1,0),(a,1)])).
 Rolfsen <=10, clean paths (217): max window 0.574, max|Delta| 0.135, median |Z - Z_lead| 1.6e-3, max 0.023.
   Window > 1 only on paths that END at an exceptional (degenerate, vol 0) filling: 9_46 (+2), 10_132 (-2); path breaks (jump ~20-30).
 CensusKnots (3116, framing fixed): y<1 occurs (211 knots) but ONLY with |x| huge (>= ~100: lens-space/Berge-type
   knots, some integer slope near -x is short) -> both +-2 slopes have L ~ 300-500 (deep HK regime), Delta ~ -2/x^2.
   With |x| <= 4: min y = 1.11, min |tau| = 1.23 (K10_1033: tau = -0.353+1.175i), min dist(W_lead, iZ) = 0.141.
 ACTUAL Delta on the 40 census knots with smallest leading margin (tw_census_delta.py): Delta up to 0.385 (K10_644,
   K10_926), i.e. margin to 1/2 only 0.115 — much less comfortable than the "<= 0.135" Rolfsen evidence.
   |Z - Z_lead| <= 0.015 whenever both ends hyperbolic; ~0.1 when one end is exceptional (K9_72, K10_81, K8_47, K9_63, K10_104).
   Twist window on hyperbolic-ending paths: max 0.924 (K10_644, N=-2: tau_{-2}(2pi) = -2.904 ~ -0.92 pi).
   => the tex's crude condition sup|tau_2|+sup|tau_-2| < pi FAILS there (2.09+2.90 = 5.0) while the window lemma still applies.
 FULL CENSUS (code/tw_census_all.py -> tw_census_all.json; 3116 knots; 2194 have |x|>12 = sheared, skipped since
   |Delta_lead| <= 2/(x^2-4) < 0.015 and both L >> 7.6; 922 analysed, 819 with both ends hyperbolic & continuous):
   max |Delta| = 0.3847 (K10_644); NO knot with |Delta| >= 1/2. median |Z - Z_lead| = 0.004 (hyperbolic ends).
   remainder/margin := |Z - Z_lead| / dist(W_lead, iZ): max 0.243 (hyperbolic ends, K10_1307), 0.705 (K10_104, one end exceptional).
   *** TWIST WINDOW FAILS on genuine-looking paths with hyperbolic ends: K10_1307 (N=+2, L=1.36, window 1.172:
       tau_2(2pi) = 3.683 > pi, strongly superlinear: Im u = 0.758 at alpha=pi, 3.683 at 2pi; endpoint vol 2.6528, continuous
       at 480 steps, negatively oriented tets) and K10_1191 (N=-2, L=1.30, window 1.079). Both still have Delta ~ 0.29 < 1/2
       because the other slope is long (L ~ 3) and barely twists. => "mu stays a shortest dual" is NOT a universal law.
   Elementary: max(L_+, L_-) >= 2 always ((4+y^2)/y >= 4 at x=0 is the min of the max), so both slopes cannot be ultra-short.

## Step 3: Direction 1 (HK/FPS machinery, quantitative) and Direction 2 (paths)
Literature (checked in FPS arXiv:1907.13502, G&T 2022): HK cone path exists if L >= 7.5832; FPS Cor 6.13: if L >= 7.823 then
 2pi/(L^2+16.17) < ell < 2pi/(L^2-28.78); FPS Thm 7.30: no purely cosmetic pair if both L >= max{10.1, sqrt(2pi/sys + 58)};
 FPS Cor 1.10 (with Ni–Wu): a purely cosmetic pair on a knot has one slope with L < that bound. Tube control: visual area
 A = alpha*ell >= h(R) = 3.3957 tanh R / cosh 2R, h_max ~ 1.0197 (so R >= 0.531 is guaranteed only while A <= 1.02);
 boundary-term negativity b(eta_c,eta_c) <= 0 needs tanh R >= 1/sqrt3 (A <= 0.980). No twist bound for the CORE in either paper
 (FPS Sec. 7 controls complex length of OTHER short geodesics). Short slopes (L ~ 2-3): nothing applies; constants 16.17, 28.78 > L^2.

(3a) Twist drift in HK's harmonic decomposition (PROVED modulo HK's boundary formula, re-derived): omega = s w_m + (x+iy) w_l + w_c,
  dL/dt = -2sL + 2(x+iy)Re L for every peripheral complex length (FPS Lemma 5.3/(5.5)), t = alpha^2, s = -1/(4 alpha^2). Hence
     d(ell/alpha)/dt = 2x ell/alpha,     d(tau/alpha)/dt = 2y ell/alpha.
  => the LEADING-ORDER (NZ linear) profile is exactly x = y = 0; the twist ratio t_N = tau/alpha moves only through y.
  b(eta_0,eta_0) = A[a(x^2+y^2) + b x s + c s^2] >= 0 with HK's a = -z^2(3-z^2)/(1-z^2), b = -2(1-z^2), c = (1+z^2)(1-z^2)/z^2
  (z = tanh R; b^2-4ac = 16 exactly). This gives the disk (x + bs/2a)^2 + y^2 <= 4 s^2 (1-z^2)^2/(z^4(3-z^2)^2), so
     |y| <= 2|s|(1-z^2)/(z^2(3-z^2)),   |x| <= |s|(1-z^2)/z^2.
  Check: the x-bound + A >= h(R) reproduces exactly FPS Lemma 6.7's G(z) = (1+z^2)/(6.7914 z^3). So
     |d t_N/d alpha| <= 2 ell (1-z^2) / (alpha^2 z^2 (3-z^2))      while tanh R >= 1/sqrt3.
  In the long-slope regime this integrates to ~ 0.589*2pi^2/L^4 ~ 11.6/L^4 (= 0.0035 at L = 7.58): window and hence |Delta| < 1/2
  are rigorous when both L_+-, L_- >= 7.58 and |t_N(0)| <= 1/2 - 11.6/L^4 (PROVED modulo the above bookkeeping).
(3b) Where HK control stops (code/tw_hk.py): A(alpha) = alpha*ell ~ alpha^2/L^2, so the tube-radius mechanism controls EXACTLY
  alpha <~ L. Numbers: genus-2 Delta=1 knots: controlled alpha <= 2.0-3.1, i.e. 32-49% of the path, 10-24% of the Delta-weight
  (weight of [0,a] is (a/2pi)^2). Drift bound on that segment 0.04-0.10 (actual drift <= 0.002). A(2pi) = 4.2-9.2 >> 1.02.
  K10_1307 (N=+2): controlled only alpha <= 1.35 (5% of weight), A(2pi) = 22.9 — and that is where the window breaks.
(3c) Endpoint formula (PROVED; verified to 1e-14 on KT): with F(u) := int_0^u v du (Neumann–Zagier potential, along the curve),
     4 pi^2 Z_N = 2 pi u_N + (i/2) N u_N^2 + i F(u_N),   u_N := u_N(2pi).
  So Z (hence Delta) depends only on the two endpoints P_{+-2} of the A-curve and the potential there (mod periods). Any
  "alternative path" is a different integral representation of the SAME endpoint quantity; the endpoints sit at
  |u| ~ 2pi/(L_N sqrt y) ~ 1-1.5, whereas all known control (HK disk) is |u| <~ 2pi/(7.58 sqrt y) ~ 0.3-0.4. No path avoids the
  uncontrolled region because the endpoints are in it. A priori control of Delta <=> a priori control of F(u_N) - tau u_N^2/2,
  i.e. of cs_C(Y_N) minus its NZ leading term: circular. (Orbifold points at alpha = pi: BLP/Weiss give existence/rigidity for
  angles <= pi but no quantitative holonomy bound; the bad growth happens on (pi, 2pi]: K10_1307 Im u = 0.76 at pi, 3.68 at 2pi.)
  (Convention note: SnapPy's cusp 'shape' is the CONJUGATE of lim v/u in its holonomy convention: u ~ i alpha/(N + conj tau).
   Im parts — hence all Delta statements above — are unaffected; Re Z_lead flips sign, already accounted for in tw_stats.)

## Step 4: Direction 3 (cusp geometry) and the size of the nonlinearity
(4a) Leading-order margin (PROVED for the k=0 branch, numerically for k != 0): for Im tau >= y0,
        dist(W_lead(tau), iZ) >= y0^2 / (2(y0^2+4)),  attained at tau = i y0.   (|W_lead| = |tau|^2/(2|tau^2-4|) >= |tau|^2/(2(|tau|^2+4)).)
     Values: y0 = 1: 0.100;  1.25: 0.140;  1.8: 0.224;  4: 0.400.  Volume equality at leading order: Re W_lead = 4xy/|tau^2-4|^2 = 0 <=> x = 0.
(4b) What geometry gives on tau (PROVED / cited):  genus g => |tau| = len(lambda)/len(mu) <= 6(2g-1) (Agol/Lackenby boundary-slope
     bound + meridian length >= 1 on the maximal cusp); for g = 2: |tau| <= 18 — an UPPER bound, the wrong direction.
     Lower bound: S^3 = E_K(mu) is non-hyperbolic, so L(mu) = 1/sqrt(y) < 7.515 (HK) => y > 0.0177 => margin >= ~4e-5. Useless.
     Nothing known for Delta_K(t) = 1 (these knots are never alternating, so alternating-knot cusp bounds don't apply).
     Genus-2 forces short slopes: both L_+, L_- >= 7.58 needs |x| >= 2 + sqrt(57.5 y - y^2) (e.g. |x| >= 9.5 at y=1), impossible
     for g <= 5 unless the cusp is strongly sheared (some integral slope near -x very short). Always max(L_+,L_-) >= 2 (PROVED).
     So: a lower bound on Im tau + leading order does NOT give a rigorous result — one still needs |W - W_lead| < y0^2/(2(y0^2+4)),
     and the remainder is uncontrolled on alpha > ~L (Step 3).
(4c) Size/origin of the remainder (code/tw_nz.py): v/u = conj(tau) + c u^2 + ..., c_eff nearly constant along the paths:
     KT c ~ -0.031; K13n4591 c ~ 0.094; K10_644 c ~ 0.010; K10_1307 c ~ -0.03+0.06i; 4_1 (exceptional +-2) c ~ -1.16i and drifting.
     Remainder ~ |c| |u_N|^2 / |tau| with |u_N| ~ 2pi/(L_N sqrt y). Small c explains the 1e-3 NZ accuracy; but c (the cubic NZ
     invariant) has no a priori bound, and |u_N| ~ 2.7-3.7 x (radius of the HK disk, where v is a priori holomorphic & controlled).
     K10_1307: tiny c but |u_2| = 5.2 (L = 1.36) -> superlinear twist, window broken.

## Step 5: sharp negatives
(5a) DUAL-CURVE NEGATIVE (PROVED asymptotically, numerically exact; code/tw_basis.py). On ANY hyperbolic knot exterior take the
     long dual mu' = mu + k lambda and the distance-4 pair s_+- = +-2 mu' + lambda, i.e. slopes 2/(2k+1), 2/(2k-1) (common dual mu').
     Shape tau' = tau/(1+k tau) -> 0, both slopes LONG (L ~ k|tau|/sqrt y: HK regime, all paths positively oriented), and
         Delta' = 1/2 + x'^2/8 + O(k^-3) > 1/2,   e.g. KT: k=2: 0.52965 (L = 11.8, 7.2), k=5: 0.50486, k=8: 0.50192; 5_2 similar.
     So twist integrals of perfectly controlled long-slope cone deformations approach (and cross) the half period. |Delta| < 1/2
     is NOT a consequence of slope lengths/cone geometry; it hinges on the dual curve being SHORT in the cusp (|t_N(0)| <= 1/2,
     guaranteed by Im tau >= 1). For the +-2 pair the dual is the knot meridian: the needed input is "the meridian is short
     relative to sqrt(cusp area)" — S^3-specific, unproved (only L(mu) < 7.5 is known), true empirically (census |x|<=12: y >= 1.11).
(5b) WINDOW NEGATIVE: the natural geometric replacement "mu stays a shortest dual along the cone path" (twist window, which implies
     |Delta| < 1/2) is FALSE for some knots in S^3 on continuous rep paths ending at hyperbolic fillings: K10_1191 (N=-2, endpoint has a
     positively oriented triangulation, vol 2.5546, window 1.079), K10_1307 (N=+2, window 1.172). Delta stays ~0.29 there only
     because the opposite slope is long. (Path beyond alpha ~ 3.3-4.0 uses negatively oriented tets: genuine reps, cone-manifold
     status uncertified.)
(5c) Rolfsen evidence is unrepresentative: census knots reach Delta = 0.385 (margin 0.115), crude sup-condition fails (5.0 > pi).

## Step 6: Direction 4 (necessary configuration in Y_2)
 PROVED (topology): cosmetic => J = phi(c_-2) is a knot in Y_2 with Y_2 - J = E_K, not isotopic (not even equivalent under Homeo(Y_2))
   to c_2 (else Homeo(E_K) would send slope -2 to +2; impossible as Homeo^+(E_K) acts by +-id on (mu,lambda)). Equivalently J has a
   nontrivial distance-4 surgery returning Y_2 (slope sigma with Y_2(J;sigma) = Y_2), and X = S^3 - (K u J) has two fillings
   (one on each cusp) both = E_K; lk(K,J) odd. If c_2, J are realised by the cone-path geodesics gamma, gamma': disjoint or not,
   lengths ell_2(2pi), ell_-2(2pi); spin-lifted complex lengths (s0): L(gamma) = u_2 + 2 pi i, L(gamma') = u_-2 (mod 4 pi i).
 Necessary analytic condition: W in iZ, i.e. nonlinear remainder >= y^2/(2(y^2+4)) (>= 0.4 for the genus-2 Delta=1 knots seen).
 Shortest-geodesic (FPS) route: works only if BOTH cores are the unique shortest geodesics. Numerics (tw_geod.py): for KT, 12n313,
   12n430, 13n1756, 13n1757 the core of Y_{-2} (L ~ 2.05, ell ~ 1.41) has RANK 4 in the length spectrum (4 shorter geodesics); in
   13n1019 ranks 2,3. So the mechanism is not merely unproved but false for this class. (Only 13n71, 13n4591 have both cores shortest.)
 Not contradictory per se (PLAUSIBLE): the unoriented configuration — two distinct cores with isometric drillings, equal volumes —
   is realised by chirally cosmetic pairs on chiral hyperbolic knots (Ren 2026, cited in hyp.md) and purely cosmetic fillings exist
   on multi-cusped manifolds (Ren). Length/volume/drilling data are orientation-blind; the only obstruction left is the oriented
   CS bit, i.e. the twist integral itself. Direction 4 reduces back to Directions 1-3.
 (5a') Exact asymptotics for the dual-curve negative (PROVED, NZ expansion is honest for long slopes): with (p,q) = (2,2k+1),
     (-2,1-2k) one again has u'_+ - u'_- = i alpha - (v_+ + v_-)/2, and for long slopes Im v ~ alpha/q (lambda nearly parallel to the
     filling slope), so  Delta' = 1/2 + 1/(2(4k^2-1)) + O(k^-3)  — the leading correction is TOPOLOGICAL (independent of tau and of
     the NZ coefficient c, which enters at O(k^-4)). Check KT: k=5 predicted 0.50505, actual 0.50486; k=8: 0.50196 vs 0.50192.
     Both slopes have L >= 11.8 for k >= 3 (HK/FPS regime). Hence "long slopes + controlled cone paths" cannot by itself keep
     a distance-4 twist integral away from 1/2 (mod 1).
 Actual (maximal-cusp) lengths of the +-2 slopes for genus-2 Delta=1 knots: 6.3-12.2 (> 6, so the 6-theorem applies, but the
 short side is ~6.3-6.5 ~ 2pi, so the FKP volume bound (1-(2pi/len)^2)^{3/2} ~ 1e-3 is void). Short in NORMALISED length (2.0-3.1),
 long in actual length: the only theorems valid here (6-theorem, FKP) use non-hyperbolic negatively curved metrics and say nothing
 about CS/twist.
 Genus-2 Delta=1 knots (200-step paths): window <= 0.249, |Z - Z_lead| <= 0.008 vs leading margin >= 0.40 (y >= 4.08).

## VERDICT
 NO a priori uniform control exists with current tools; the failure is located precisely:
 1. Exact reduction (PROVED): Z = i/2 - W, W = (1/8pi^2) int (v_2 + v_-2) d alpha (Seifert-longitude holonomy); cosmetic <=> W in iZ
    (the UNKNOT value W = 0). Endpoint form 4pi^2 Z_N = 2pi u_N + (i/2)N u_N^2 + i F(u_N): path-independent, so "better paths"
    cannot help — the endpoints themselves lie ~3x outside the a priori (HK) holomorphy disk.
 2. Leading order (PROVED): W_lead = (i/2) tau^2/(tau^2-4) never in iZ; volume equality forces x=0; margin >= y^2/(2(y^2+4)).
 3. Remainder control (PROVED structure): d(tau/alpha)/dt = 2y ell/alpha with HK's |y| <= 2|s|(1-z^2)/(z^2(3-z^2)) holds only while the
    tube radius is certified, i.e. visual area alpha*ell <= 1.02, i.e. alpha <~ L. For genus-2 Delta=1 knots this is 32-49% of the
    path / 10-24% of the Delta-weight. Rigorous |Delta| < 1/2 only when both L_+- >= 7.6 (minor extension of FPS for +-2).
 4. Cusp input (Direction 3): genus 2 gives |tau| <= 18 (upper bound; forces short +-2 slopes unless |x| >= 2+sqrt(57.5y-y^2));
    Delta_K = 1 gives nothing; best lower bound y > 0.0177. Even "y >= 1" would only give a 0.1 margin to beat with an
    uncontrolled remainder.
 5. Sharp negatives: (a) dual-curve family: Delta' = 1/2 + 1/(2(4k^2-1)) + O(k^-3) on fully controlled long slopes 2/(2k+-1) —
    the gap is NOT a cone-geometry fact; it needs the dual (meridian) to be short, an unproved S^3 input. (b) twist window
    ("meridian stays a shortest dual") false on K10_1191, K10_1307. (c) census knots reach Delta = 0.385. (d) FPS shortest-geodesic
    route false for the class (core of Y_-2 has rank 4). (e) two-cores configuration is orientation-blind-consistent.
 What a proof would need: an S^3-specific theorem "meridian short" (Im tau >= y0, or |t_N(0)| <= 1/2) PLUS a short-slope
 (L ~ 2-3) nonlinearity bound |W - W_lead| < y0^2/(2(y0^2+4)) along the +-2 cone paths — neither exists; both hold with big
 margins numerically on the class (window <= 0.25, remainder <= 0.008 vs 0.40).
