# R8/examples.md — stress tests of the spin–Schläfli mechanism on genuinely homeomorphic fillings

Status log (updated after each step). Code: R8/code8/.

## Step 0 — read spinschlafli.tex, hyp.md, code/. Plan
Tests: (1) Ren 2604.02672 multi-cusped purely cosmetic; (2) chirally cosmetic (amphichiral ±r; IIS; Ren chiral);
(3) other homeomorphic fillings (BHW, symmetric pairs); (4) any pair with twist integral at a half period.
First concern found while reading (to be checked): UNITS. Manuscript identifies SnapPy chern_simons() with
SU(2)-unit cs mod 1/2 and takes Lemma 2's 1/2 in those units.

## Step 1 — UNITS: the manuscript's mod-1 bookkeeping is off by a factor 2 (PROVED modulo standard normalisations)
Three independent checks, all giving cs_SU2 = cs_SnapPy / 2 (up to sign), NOT cs_SU2 = cs_SnapPy:
 (a) Goette–Zickert (arXiv 0705.0500, intro): c^_2 : H_3(SL(2,C)) -> C/Z(2) = C/4pi^2 Z ; PSL version (Neumann) -> C/pi^2 Z;
     Dupont–Zickert -> C/2pi^2 Z. In the normalisation i(Vol + i CS) used by SnapPy (CS = 2pi^2 * chern_simons()),
     the SL(2,C) period is 4pi^2  <=>  chern_simons() mod 2. Period 1 in SU(2) units <=> period 2 in SnapPy units.
 (b) First-principles Kirk–Klassen: delta cs = -(1/8pi^2) int tr(A ^ dA) on the boundary gives d cs = -(a db - b da)
     (eigenvalues e^{2 pi i a}, e^{2 pi i b}); this normalisation reproduces cs(L(p,1), k) = -k^2/p and cs(RP^3, central) = 1/2.
     Along a cone path a = a0 + H/(4 pi i) (H = SnapPy holonomy = log multiplier = 2 log eigenvalue), so
     Re-part changes by (1/8pi^2) int Im H d alpha, i.e. HALF of SnapPy's validated (1/4pi^2) int tau.
     Im-part: (1/8pi^2) int Re H = -dVol/(4pi^2); independently, Im CS(omega + i e) = (1/8pi^2)(4/3) int tr e^3 = -Vol/(4pi^2).
 (c) Volume conjecture: J_N(e^{2pi i/N}) ~ exp(N (Vol + i CS)/2pi) with level k+2 = N weight e^{2 pi i N cs}
     => cs_C = (CS - i Vol)/(4 pi^2), CS = SnapPy's 2pi^2 chern_simons().
 Riemannian CS (Chern–Simons, R/Z) = SnapPy chern_simons() mod 1 = -2 cs_SU2 mod 1: a PSL / isometry invariant.
CONSEQUENCES (in the manuscript's normalisation Delta_K = (1/4pi^2) int (tau_2 - tau_-2) dalpha, SnapPy units):
 * SnapPy data (mod 1/2):           cosmetic => Delta_K in (1/2)Z       [what hyp.md saw]
 * Riemannian CS (PSL, mod 1):      cosmetic => Delta_K in Z            [no spin, no Arf needed]
 * spin (Lemma 1+2, SU(2) mod 1):   cosmetic => Delta_K in 1 + 2Z       [NOT Delta_K = 1/2 mod 1]
 So the "missing bit" supplied by spin is the SECOND missing bit; the first is the Riemannian CS mod 1.
 The stated theorem (|Delta|<1/2 => not cosmetic) remains true; corrected sharp form: |Delta_K| < 1 suffices;
 more precisely cosmetic needs Delta_K odd integer (twist integral at HALF a period in SU(2) units = a FULL period in SnapPy units).

## Step 2 — corrected general bookkeeping (T_inv trivialisation, form -(a db - b da)) — derived, internally checked
 Cusp spin lift Ptilde=(a0,b0) in (1/2 Z)^2 (a0=1/2 <=> tr mu = -2). Slope m=(p,q) extends iff A0 := p a0 + q b0 = 1/2 mod 1.
 Positive dual l=(r,s) (ps-qr=1), B0 := r a0 + s b0, H_m = i eps alpha along the cone path.
 cs_SU2(E(m), lift) = Theta_E(Ptilde) + B0 (A0 + eps) + eps (1/8pi^2 i) int_0^{2pi} H_l dalpha.
 Checks (all pass): (i) independent of dual l -> l + k m (twist +k/4, constant -k/4 mod 1);
 (ii) lens spaces (unknot) cs = -k^2/N; (iii) Lemma 2 for ALL even N on knots (cs(s1)-cs(s0) = N/4) given
 Theta(P1)-Theta(P0) = 1/4, which the twisting computation reproduces exactly; (iv) knot (+-2,1), sigma_0, l = -mu:
 kappa_2 - kappa_-2 = -1 = 0 mod 1 (manuscript's "c_2 = c_-2" is right in SU(2) units).
 Riemannian (SnapPy units, mod 1):  R(E(m)) = R_E(Ptilde) + B0 + J_l,   J_l := SnapPy-normalised twist, R_E = cs_SnapPy(E) mod 1/2.
 The manuscript's worry "replacing mu by mu.m_fill shifts the integral by exactly 1/2 = the bit at stake" dissolves:
 the shift is 1/4 in SU(2) units and is cancelled by the constant.

## Step 3 — independent mod-1 calibration: closed amphichiral census (PROVED given Lemma 2 + Rokhlin parity)
 Fact: if H_1(Y) = Z/2 + (odd), every spin structure has ODD Rokhlin invariant (even lattice of det = 2 mod 4 has odd rank),
 so an orientation-reversing isometry h cannot fix a spin structure (mu = -mu mod 16 impossible): h SWAPS s, s'.
 Then cs(s') = -cs(s) and (Lemma 2) cs(s') = cs(s)+1/2  =>  cs_SU2(Y,s) in {1/4, 3/4}.
 Manuscript normalisation (cs_SnapPy = cs_SU2) would force chern_simons() = 1/4 mod 1/2. Mine forces 0 mod 1/2.
 Data (code8/amphi_closed.py): all 37 amphichiral manifolds of OrientableClosedCensus have chern_simons() = 0 to 1e-15,
 incl. 7 with H_1 = Z/2+odd (m082(1,3) Z/82, m078(5,1) Z/34, m168(2,3) Z/34, s235(-3,4) Z/58, s287(3,4) Z/106,
 v2585(1,2) Z/58, v3283(-3,1) Z/74).  => manuscript normalisation REFUTED; cs_SU2 = chern_simons()/2 CONFIRMED.

## Step 4 — PITFALL found: SnapPy's G.SL2C(word) is NOT a homomorphism (relators often map to -I)
 (4_1, K11n42, o9_39009, ...). Peripheral trace signs read off it are garbage. Fixed by solving for generator signs
 so that all relators -> +I (code8/spin.py: genuine_lift_signs). Correct cusp types: every knot {(0,1/2),(1/2,1/2)}
 (Calegari: tr lambda = -2 always) ; o9_39009 {(0,1/2),(1/2,1/2)} ; m135 {(0,1/2),(1/2,0)} ; t12051 {(1/2,0),(1/2,1/2)}.
 (Before the fix, o9_39009 gave a spurious failure T = 1/2.) hyp.md's numerics did not use SL2C, so unaffected.

## Step 5 — Riemannian-level test (SnapPy units mod 1) on genuinely homeomorphic CHIRALLY cosmetic pairs: ALL PASS
 Prediction: R(Y1)+R(Y2) = 2cs(E) + (B1+J1) + (B2+J2) + dR = 0 mod 1, where B = r a0 + s b0, J = SnapPy-normalised twist
 along the positive dual, dR = chi_mu b0 - chi_lambda a0 if the two slopes need different cusp types. (code8/rtest2.py)
   o9_39009 (-1,3)/(-3,2)  [ASYMMETRIC E, H_1(Y)=Z/126]: J=(0.171635,-0.314353), 2cs=-0.357282, B=(-1/2,-1/2), dR=1/2 -> T=-1.000000
   m135 (1,3)/(3,1): T=1.000000 ; t12051 (1,1)/(2,-1): T=0.000000 ; 4_1 (2,1),(6,1),(2,3),(10,3) vs mirror: T=0 ;
   6_3, 8_3 (+-2), 8_9 (10/3, 6/5 vs mirror): T=0.   All to < 1e-6.
 This is one bit beyond what SnapPy itself checks (SnapPy is mod 1/2).

## Step 6 — SPIN level (SU(2) units mod 1) where an independent determination exists: ALL PASS (exact arithmetic)
 (code8/spinlevel.py) kappa = B0 (A0 + eps), T_inv rules cs(a+1,b)=cs-b, cs(a,b+1)=cs+a.
 (a) amphichiral knots, h:(mu,l)->(mu,-l) preserves sigma_0, sigma_1; symmetry forces 2 Theta = 1/2 at (1/2,1/2), 0 at (0,1/2).
     Identity 2Theta + kappa_r + kappa_{-r} + k/4 = 0 mod 1 (k = dual mismatch) holds for ALL 788 extendable (p,q), |p|<=31, q<=15
     (twists cancel numerically: J_r + J_-r = -k/2 in SnapPy units, e.g. 4_1 (1,2): -0.246607-0.253393 = -0.5).
 (b) o9_39009 is EXACTLY Ren's Construction 2.1 with k=2, l=0: drilling the second-shortest geodesic of Y2 = o9_39009(-3,2)
     gives a 2-cusped N (vol 9.13447, cs 0, symmetry group D6, amphichiral); o9_39009 = N(inf,(1,0)) and an
     orientation-REVERSING cusp-swapping symmetry phi of N sends (cusp0 (-1,3), cusp1 (1,0)) -> (cusp1 (1,0), cusp0 (-3,2)).
     Spin-level identity via N: K1 + K2 + I(X1) + I(X2) + 1/2 = -5/4 + 1/2 + 0.250000000 + 1/2 = 0.000000000  (pass).
     Route twists in N: J(X1) = -0.007006478, J(X2) = -0.492993522 (SnapPy units), route-independent to 1e-10.
 (c) knot (+-2,1), dual -mu: kappa_2 = -5/4, kappa_-2 = -1/4 (sigma0); 0, 0 (sigma1): equal mod 1. Lemma 2 consistent for all even N.
 => The corrected bookkeeping reproduces every known identity exactly. The manuscript's c_2 = c_-2 is right;
    its UNIT for the twist (and hence "Delta = 1/2 mod 1") is wrong: cosmetic => Delta_K odd integer.

## Step 7 — Ren-type PURELY cosmetic pair found in the census (item 1): o10_150704 (4 cusps, H_1=Z^4, cs=0, sym D3xD4)
 phi = orientation-PRESERVING isometry, cusps (0 2)(1 3), maps T0->T2: A=[[-1,-1],[1,0]], T2->T0: A, T1->T3: A, T3->T1: I;
 phi^2|T0 = A^2 has order 3. M := N(inf, inf, A s, inf) (3 cusps, symmetry group of order 2, NO symmetry of M sends s to A^2 s).
 M(s) ~ M(A^2 s) orientation-preservingly via phi: purely cosmetic, cusped (T1,T3 complete) — Ren Thm 1.4 type.
 (code8/ren_pc3.py, 200-step cone paths on T0 of M, all positively oriented)
   s=(3,4):  J(s)=0.141886767, J(A^2 s)=0.141886768  ;  s=(3,5): -0.188779035 both ; s=(1,3): -0.134862189/-0.134862191 ;
   s=(2,1): 0.180046580/0.180046607.   => twist DIFFERENCE = 0 (to 1e-8), constants kappa equal mod 1 for the phi-paired lifts.
   Spin-level (SU(2) mod 1) and Riemannian identities hold.  Twist difference is NOT at a half period: it is exactly 0.
 Naturality check of the SU(2) twisting rule on N (code8/delta_nat.py): Theta(sigma'',P'') - Theta(sigma,P) = 0 provided the
 abelian base term is computed with an INTEGRAL lift chihat of chi (radial path to chihat|_bdry /2, then lattice moves);
 the naive "chihat|_bdry in {0,1}" shortcut is only valid when such a lift exists (true for knots).
 H_1 of these purely cosmetic fillings is Z+Z (torsion-free): no closed Z/2 with eps^3 != 0 here, so Lemma 2 has no
 analogue; the identity holds for the phi-paired lifts with zero twist difference.

## Step 8 — Ren's chiral Brunnian knots (Thm 1.5), q=3 (code8/ren_brunnian.py; PD code from the paper; N: 3 cusps, 62 tets,
 vol 55.8977, cs 0, Z/6 symmetry, phi = (0 1 2) with diag(1,-1)).  M = N(inf,(1,-3),(1,3)) = S^3 - K, H_1 = Z.
 J(N->M) = 0.166075938 - 0.166075943 ; cs(M) = -4.7e-9 (K chiral but CS-asymmetry ~1e-8);
 J(M->Y+) = -0.166072658, J(M->Y-) = +0.166072667, cs(Y+-) = -+0.16607266.  H_1(Y+-) = 0 (one spin structure).
 Riemannian: 2cs(M) + B+ + B- + J+ + J- = -5e-10 + 1 = 0 mod 1  PASS.
 Spin level via N: lift (0,1/2)^3, 2 Theta_N = 0 (phi), 2Theta_M = 2(kappa_T1 + kappa_T2) = 2(-1/4+5/4) = 0,
 kappa+ + kappa- = 5/4 - 1/4 = 1, twist sum ~ -4.5e-9  => total 0 mod 1  PASS.  Twist sum ~ 0, not a half period.
 (The genuine SL2C lift of this 62-tet filled manifold is numerically ill-conditioned: SL2C traces ~1e9; cusp types taken
 from the knot-in-S^3 rule instead.)

## Step 9 — orientation-reversing analogue of the condition (derived, PROVED modulo path existence)
 S^3_r(K) = -S^3_r'(K), forced pairing s<->s' (for +-2: s0<->s0 and s1<->s1 for EITHER Arf, from mu(-Y)=-mu(Y)):
   cs_SU2(Y_r,s) + cs_SU2(Y_r',s') = 2 Theta_K + kappa_r + kappa_r' + I_r + I_r' + dTheta = 0 mod 1.
 Riemannian part (computable from SnapPy):  X_K := J_2 + J_-2 + 2 cs(E_K) in Z  for chirally cosmetic +-2.
 Survey (code8/chiral_pm2.py, knots <= 10 crossings): all 20 amphichiral knots X_K = 0 exactly (incl. 8_17, negative
 amphichiral); chiral knots median dist(X_K,Z) = 0.28, closest 10_65 (7e-4), 10_71 (1.3e-3) — a single real condition,
 so near misses occur; volume is the real discriminator. The spin part needs Theta_K mod 1/2, which no SnapPy quantity gives
 for a chiral knot: the chirally cosmetic analogue is checkable only mod 1/2 (SU(2)) unless an ancestor symmetry fixes Theta.

## Step 10 — what each hypothetical PURELY cosmetic knot pair would need (code8/gaps.py), spin level, SnapPy units
 +-2 (Arf=0, Lemma 1 swap + Lemma 2):  Delta_J = J_2 - J_-2  must be ODD.
 +-1/q, q odd (unique spin structure, sigma_1 type): constants alone give Delta kappa = 1/2  => Delta_J must be ODD as well
   (so long +-1/q slopes with q odd are excluded by the same mechanism, without any spin swap) — PLAUSIBLE (no test case exists;
   +-1/q is already excluded by Daemi–Eismeier–Lidman). q even: Delta kappa = 0, Delta_J even, Delta_J = 0 allowed: no gap.
   (Manuscript's remark "for +-1/q ... no gap" is right only for even q.)

## VERDICT (examples.md)
 1. Units: the manuscript's mod-1 bookkeeping has a factor-2 error. cs_SU2 = chern_simons()/2. Correct statement:
    cosmetic (+-2, Arf 0) => Delta_K = (1/4pi^2) int (tau_2 - tau_-2) is an ODD INTEGER; PSL/Riemannian level alone => Delta_K in Z.
    The theorem as stated (|Delta|<1/2) stays true; sharp threshold is |Delta_K| < 1 (sup|tau_2|+sup|tau_-2| < 2 pi suffices).
    Refuted the manuscript normalisation independently with the closed amphichiral census (Rokhlin parity => h swaps spin).
 2. With correct units + genuine SL(2,C) lifts, the mechanism reproduces EVERY known identity exactly: 788 amphichiral slopes
    (spin level, exact), o9_39009 (asymmetric, Z/126, Riemannian + spin via its Ren ancestor), o10_150704 purely cosmetic
    family (twist difference = 0 to 1e-8), Ren's Brunnian chiral knot, m135, t12051.
 3. Every known homeomorphic pair is induced by a symmetry of an ancestor manifold; that pairs the cone-path lifts "unmixed", so
    the isolating twist combination is fixed by constants (0, or 1/4 in SU(2) units for o9's N-routes), never a half period.
    No known pair realises the configuration (mixed spin pairing => twist difference at a half period) that +-2 would need.
