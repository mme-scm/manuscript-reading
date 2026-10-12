# R8 acurve.md — path-independent reasons for Delta_K notin 1/2+Z ? (A-curve / complexified pillowcase)

Status log; labels PROVED / PLAUSIBLE / SPECULATIVE.

## Step 0: read spinschlafli.tex, hyp.md, slope2.tex, mono.md. Conventions used here
- (m,l) SL eigenvalues of (mu,lambda) on E_K. S^3-lift complete point Q0=(-1,-1); other lift chi(Q0)=(1,-1).
- L_N^+ = {m^N l = 1} (SL reps of Y_N), chi(m,l)=(-m,l) = lift swap = eps-twist (eps(mu)=-1, eps(lambda)=1).
- Half-period lemma, all SL reps of Y_{+-2}: cs(rho*eps) = cs(rho) + N/4 = cs(rho)+1/2 (N=+-2).
- Delta_K = cs(Y_2,s0) - cs(Y_-2,s0); cosmetic + Arf=0 => Delta_K == 1/2 (mod 1).

## Step 1 (quick consistency facts found while setting up)
- (PROVED) No SL rep rho of Y_{+-2} has rho*eps ~ rho (else cs(rho)=cs(rho)+1/2). Consistent: such rho would be
  induced (binary-dihedral type); those send lambda -> I (lambda in pi''), so l=+1, never on L_{+-2}^+ at m=+-i.
- (PROVED) For ANY one-cusped M, an orientation-preserving symmetry h fixes the rational longitude up to sign
  and has finite order in SL(2,Z) => h_* = +-I on H_1(cusp) => h fixes every slope. So "symmetric models" of a
  purely cosmetic pair (where Delta=1/2 would be explained by a holomorphic involution of C_0 mapping P_-2 -> P_2)
  do NOT exist for one-cusped manifolds. Idea 4 can only produce orientation-REVERSING (mirror) symmetries,
  which map L_N -> L_-N but conjugate cs; they relate Delta to 2cs(Y_2,s0), not to 1/2.

## Step 2: path-independent form (idea 1) — what contour deformation can and cannot give
Coordinates on the Q0-sheet: u = log(-m), v = log(-l) (u=v=0 at Q0), v = g(u) = tau u + c3 u^3 + c5 u^5 + ...
(odd: (m,l)->(1/m,1/l) fixes Q0). PSL core length H = 2u. Cone/generalized filling for slope N:
   N u + g(u) = w,  w = i alpha/2 in [0, i pi]   (w = i pi is the closed filling P_N).
Complex Schlafli d(Vol + i CS) = -(1/2) H d alpha  =>  d(Vol+iCS) = 2i u dw, hence EXACTLY
   (Vol+iCS)(P_N) - (Vol+iCS)(Q0) = 2i * F_N(u_N),   F_N(u) := i pi u - N u^2/2 - G(u),  G' = g, G(0)=0,
where u_N solves N u + g(u) = i pi.  [integrate u (N + g') du by parts]. F_N = NZ potential + Dehn-filling term
(the "single multivalued holomorphic function" of the brief).  Delta_K = Re of the difference / (2 pi^2), up to sign.
(PROVED, given the complex Schlafli formula; numerically checked below.)
Facts:
 (a) PROVED (S^3 input = cyclic surgery theorem, CGLS): mu is not a strict boundary slope, so every ideal point of
     C_0 lies over m in {0, infinity}. Hence in the finite u-plane the only singularities of g (and of G, F_N) are
     BRANCH POINTS of m|C_0 (algebraic, from disc_l A_K), where G has Puiseux (u-b)^{3/2}-type terms: finite,
     no residues. Ideal points sit at Re u = +-infinity.
 (b) PROVED (Kirk–Klassen flat section): continuation of F_N along two paths in X (normalisation of C_0 minus
     ideal points) with the same endpoints differs by an element of Z (SU(2) units) after the KK transition
     functions for the log branches. Hence Delta_K mod 1 is a RELATIVE PERIOD: path-independent, but every global
     contribution (loops around branch points, around m=0/infinity, Culler–Shalen norm, tame symbols) is an
     INTEGER. Contour deformation cannot produce a 1/2: residues/periods are integral.
 (c) Consequence: Delta_K mod 1 is determined by the transcendental moduli of the germ (tau, c3, c5, ...) and the
     endpoint u_N; discrete global data of C_0 enter only through which sheet P_N is on. No mod-1 formula in terms
     of global discrete data exists (PLAUSIBLE as a meta-statement; each ingredient PROVED).
 (d) Fibre-trace identity (PROVED modulo standard NZ): for fixed N, sum over the whole fibre f_N^{-1}(z),
     f_N = m^N l, of the generalized-filling potentials is a QUADRATIC POLYNOMIAL in log z, because
     d/dlog z (sum) = const * sum of core lengths = const * log Norm_{f_N}(m)(z), and Norm(m) is a rational
     function with zeros/poles only over images of ideal points = {0,infinity} when N is not a boundary slope,
     hence a monomial c z^k. So whole-fibre sums are elementary/rational. BUT fibres are chi-invariant: pairs
     (x, chi x) contribute 2cs(x)+1/2 -> spin-blind. They give a CS-weighted SL(2,C)-Casson-type quantity, not the bit.

## Step 3: where can the bit live at all? (ideas 2,3,4)
Key logical point (PROVED as logic): the cosmetic hypothesis yields the half-period only through a point
whose two SL lifts are CANONICALLY labelled by spin structures of Y in a homeomorphism-natural way.
 - Geometric rep rho_Y: lifts <-> spin structures (frame bundle). Mostow => phi pairs geometric points.
 - Galois conjugates rho_{Y,s}^sigma (sigma: k -> C, k = trace field): phi^* commutes with sigma, so
   phi^* rho_{2,s0}^sigma = rho_{-2,s0}^sigma * eps.  => (PROVED) cosmetic implies, for EVERY embedding sigma,
      cs(rho_{2,s0}^sigma) - cs(rho_{-2,s0}^sigma) == 1/2  (complex, mod 1),  Vol's equal.
   At a real place where the quaternion algebra ramifies, rho^sigma is an SU(2) rep: the bit is transported to
   two CANONICAL SU(2) points x_{+-2}^sigma in the pillowcase (on sigma(C_0)'s unitary slice) whose SU(2) cs must
   differ by exactly 1/2 (pairing x_2^sigma <-> chi x_-2^sigma). New testable conditions, [k:Q] of them.
 - Every other character x of Y_{+-2}: no natural label {x, x eps} <-> {s0,s1}. Labels via "the S^3-lift branch
   of C_0" depend on the surgery description, and phi does not preserve components of X(E_K). Hence:
   SU(2)/instanton data, total CS over X_SL(Y), Casson counts (incl. Culler–Shalen norm difference
   ||2|| - ||-2||), fibre sums: all eps-symmetric => spin-blind (they can only give "unfiltered" obstructions,
   which are knot-specific and orthogonal to the bit).
 - Galois totals: S(Y,s) := sum_sigma cs(rho_s^sigma). Res_{k/Q} rho_s is (if traces integral) an SL(2d,Z) rep, so
   S(Y,s) lies in the image of H_3(SL(Z)) ~ Z/24 -> Q/Z (PLAUSIBLE, Suslin/Quillen: K_3^ind(Q)=Z/24, regulator
   injective on torsion). [k:kGamma] in {1,2} for H_1=Z/2: if 2, sigma_0 swaps the lifts (S(s0)=S(s1), no info);
   if k = kGamma and d=[k:Q] odd, S(Y,s1) = S(Y,s0)+1/2 and cosmetic => S(Y_2,s0)-S(Y_-2,s0) == 1/2: a RATIONAL
   (denominator | 24), path-free form of the bit. But S is an invariant of (Y,s); any invariant of (Y,s) is
   automatically consistent with a hypothetical isometry. Obstruction only arises if S(Y_N,s0) is computed from
   K-side data (A-curve), and Galois orbits are NOT whole fibres in general (fibre sums are spin-blind), so this
   needs the factorisation of C_0 cap L_N over Q: knot-specific. (SPECULATIVE as a route.)
 - Symmetry (idea 4): PROVED no orientation-preserving symmetry of a one-cusped M moves slopes (fixes rational
   longitude up to sign + finite order in SL(2,Z) => +-I). So phi is never induced by an automorphism of C_0.
   Mirror (m,l)->(m,1/l) exists only for amphichiral K, swaps L_2,L_-2, conjugates cs: gives Delta = 2cs(Y_2,s0),
   no constraint (and no test of the mod-1 bookkeeping: symmetric in N).
 - Spin sign of geodesics (reformulation, PROVED given |tau_N(2pi)|<pi, true in all numerics): in (Y_2,s0) the core
   c_2 has lifted trace -2cosh(L/2) (bounding), while a cosmetic phi would produce a second geodesic c'=phi(c_-2)
   with complement E_K and lifted trace +2cosh(L/2) (Lie). Equivalent to the bit; no contradiction by itself.
 - Arithmetic (idea 3): the would-be relation [Y_2,s0]-[Y_-2,s0] = t_2 (order-2 element of K_3^ind, defined over Q)
   is realised by any actual isometry, so it cannot contradict trace-field / Bloch-group structure; arithmetic
   only gives MORE equations (one per place), not a contradiction. SHARP NEGATIVE.

## Step 4: numerics for the path-free form (code/acurve/{glue,pot,series,survey_R}.py)
Own Newton solver on SnapPy gluing equations, u = H(mu)/2 complex, straight SEGMENT 0 -> u_N in the u-plane
(no cone path). Exact identity (SnapPy orientation convention): (Vol+iCS)(Y_N)-(Vol+iCS)(E) = -2i F_N(u_N).
 KT N=+2: -2ImF = 1.270099 = -dVol ; ReF/pi^2 = -0.057565 = -dCS (EXACT, not just mod 1/2). N=-2 likewise.
 Delta(segment) for the 7 genus-2 Delta=1 knots: 0.06173 0.05791 0.06635 0.02826 0.07618 0.05582 0.04783 = hyp.md values.
NZ series v = g(u) via Cauchy/FFT on a circle; truncated series (k<=21) reproduces Delta to 6 digits (KT, 12n313, 13n1019).
Radius of convergence R (nearest branch point of m|C_0 on the geometric sheet), max|u_{+-2}|/R:
 KT 0.98 (0.72); 12n313 1.00 (0.72); 12n430 0.97 (0.73); 13n71 0.35 (1.20!); 13n1019 0.89 (0.68); 13n1757 1.04 (0.71);
 13n4591 0.52 (1.05!). KT: nearest singularities at u ~ +-0.97 (real u, m ~ -2.6). For 13n71, 13n4591 the filling
 points lie OUTSIDE the disk of convergence, yet straight segments avoid the branch points and agree with cone paths.
 => the right domain is the Riemann surface, not a disk; a "branch-radius" certificate is not uniform either.

## Step 5: complexified rotation identity = path-free form of the criterion (main positive output)
F_N(u) = Phi_N(u) := i pi u - N u^2/2 - G(u) has Phi_N'(u) = i pi - N u - g(u): the filling point u_N is a
CRITICAL POINT of Phi_N on the geometric sheet, and (Vol+iCS)(Y_N) - (Vol+iCS)(E) = -2i * (critical value).
Envelope theorem for the pencil t in [-2,2] of lines t u + v = i pi through the pivot (m,l) = (-1,1):
   d/dt crit(Phi_t) = -u_t^2/2   ==>   Delta_K = (1/(2 pi^2)) Re  int_{-2}^{2} u_t^2 dt,
   u_t = half the complex length of the core of the generalized Dehn filling (t,1) on the geometric sheet
   (= rational t=p/q: cone manifold on slope (p,q) with angle 2pi/q). Valid along ANY t-path in C homotopic
   rel ends in C minus the caustic set {t + g'(u_t) = 0}. (PROVED modulo complex Schlafli; NUMERICALLY EXACT:)
   all 8 genus-2 Delta=1 knots: Delta_rot = 0.06173 0.05791 0.06635 0.02826 0.07618 0.07090 0.05582 0.04783
   (= cone-path values), endpoint of the t-family = SnapPy's P_{-2} to 1e-15.
 CRITERION (rotation form). K hyperbolic, Arf=0. If the generalized fillings (t,1), -2<=t<=2, form a continuous
   family on the geometric sheet with |H_t| < pi (H_t = 2u_t core complex length), then |Delta_K| <= 2 max|u_t|^2/pi^2
   < 1/2, so S^3_2(K) != S^3_-2(K). Equivalently: cosmetic => mean_{t in[-2,2]} Re(H_t^2) = pi^2 (1+2n), so the cores
   of the pencil must have |H_t| >= pi on average. Data: max|u_t| = 0.709 0.716 0.711 0.423 0.708 0.720 0.735 0.548
   (threshold pi/2 = 1.571); bound 2max^2/pi^2 <= 0.11. Leading order u_t ~ i pi/(t+tau): criterion <=> Im tau > 2.
 UNIFICATION with slope2.tex: on the unitary slice u = 2 pi i (a - 1/2) and t is real, so the same identity reads
   drop = -2 int (a_t - 1/2)^2 dt: sign-definite (the SU(2) windows). Pivots at (m,l) = (+-i,-1) give the a_P=1/4
   version [(u_t + i pi/2)^2]; on the geometric sheet that pencil passes through Q0 at t=0.
   SU(2) windows = positivity of a real square on the unitary slice; on the geometric sheet the same integrand is
   complex, so only a SIZE bound survives. This is exactly why no window/positivity argument transfers.
 Caveat on Step 2(a): "no ideal point at finite m" <=> canonical factor of A_K has no horizontal Newton edge
   (slope mu associated to an ideal point). Meridional essential surfaces DO exist (Conway spheres, e.g. KT), so this
   is not "mu is not a boundary slope"; I believe Culler–Shalen theory excludes mu being associated to an ideal
   point when M(mu)=S^3, but did not pin down the reference -> PLAUSIBLE. Irrelevant for (b): cs(Y_N,P) is
   intrinsic, so any residue is absorbed (path changes never change the evaluated value).

## Step 6: rotation-form criterion over knots <= 10 crossings (code/acurve/rot_survey.py, rot_survey.json)
Plain SnapPy real generalized filling dehn_fill((t,1)), 81 values of t in [-2,2], u_t = H(mu)/2.
 241 knots; 216 "clean" pencils (all positively oriented, continuous): Delta_rot = cone-path Delta to <= 9e-6 (all 216);
 max over them of max_t|u_t| = 1.13 < pi/2 = 1.571; max |Delta| = 0.082. So the criterion holds for all clean ones.
 Dirty pencils (25): flat-tetrahedra artefacts with agreeing values (4_1, 6_3, 8_8, 8_9, 9_28, ...), or genuine failures
 for twist-type knots with small Im tau (5_2, 6_1, 7_2, 7_4, 8_20, 10_140...: the pencil crosses exceptional slopes in
 (-2,2), SnapPy jumps sheet, max|u| ~ 6-13). Those are genus 1 / not in the target class; cone paths still work there.
 => rotation form is a ONE-family, SnapPy-testable, certifiable (interval Newton along t) version of spin–Schlafli.
Suggested independent test of the mod-1 bookkeeping (still unverified): two distinct Arf-0 hyperbolic knots with
 S^3_2(K) = S^3_2(K') (orientation-preserving); Rokhlin forces s0 <-> s0, so their mod-1 Schlafli values must agree.

## VERDICT
 Path-independent formulation: YES (PROVED/numerically exact). Delta_K = (1/2pi^2) Re int_{-2}^{2} u_t^2 dt over the
 pencil of generalized fillings (t,1) through the pivot (m,l)=(-1,1) = complexification of slope2.tex's rotation
 identity; equivalently difference of critical values of Phi_t = i pi u - t u^2/2 - G(u) (G = NZ potential).
 Conceptual reason for Delta_K notin 1/2+Z from this structure: NO, and here is why (sharp negatives):
  N1 (PROVED) periods/residues/monodromy of the KK form are integers: contour deformation never yields the bit.
  N2 (PROVED, logic) only Galois conjugates of the geometric point carry a homeomorphism-natural lift<->spin label;
     all counts / fibre sums / SU(2)-instanton data / Culler–Shalen norms are eps-symmetric (spin-blind).
  N3 (PROVED) no symmetry of C_0 can realise phi (one-cusped symmetries fix all slopes); mirror only for amphichiral.
  N4 (PROVED) arithmetic: the required relation [Y_2,s0]-[Y_-2,s0] = 2-torsion of K_3^ind is realised by any isometry,
     so it cannot contradict trace-field/Bloch data; Galois only multiplies the conditions (one per place;
     at real ramified places the bit is transported to canonical SU(2) points).
  N5 (PROVED + numerics) the SU(2) windows are positivity of -(a-1/2)^2 on the unitary slice; on the geometric sheet the
     same integrand u_t^2 is complex: only the size bound |Delta| <= 2 max|u_t|^2/pi^2 survives.
 => Any proof must be an a priori bound: |H_t| < pi (core complex lengths of the pencil (t,1), |t|<=2), i.e. a
    short-slope effective Hodgson–Kerckhoff theorem (none known; HK needs Im tau >~ 56 for the whole pencil).
