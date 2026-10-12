# r8/pu2route.md — PU(2)-monopole (HPU) route to S^3_2(K) != S^3_{-2}(K)

Status log (updated after each step). Labels: PROVED / PLAUSIBLE (posits stated) / SPECULATIVE.

## Step 0 — read inputs (done)
pu2.tex (ZHS sketch), spinschlafli.tex, hyp.md, mono.md, statements.tex, R4 faces-final (lens faces at L(4,1)).
REFOCUS (coordinator, from user): NOT a level/window mechanism. Goal: a 1 != 0 (nonvanishing vs vanishing)
contradiction, Property-P style. Keep: HPU set-up on Y_{+-2}, reducibles, HPU(lens)=0, spin structures, chi.
Evaluate (i) spin-structure mismatch, (ii) closed Z_+- = X_{+-2} cup_phi (-+X_{-+2}), (iii) cobordism endomorphism
forced iso vs forced zero, (iv) Floer FL relation in HPU. Calibration: KT slice, Delta=1 kills abelian invariants.

## Step 1 — (a) HPU set-up on Y with H_1 = Z/2 (Y = Y_{+-2}); corrections to the sketch
A1 [PROVED, bundle theory] Spin^u structures on Y: V = W_t (x) E up to (W(x)L, E(x)L^*). Since U(2)-bundles on a
   3-manifold are classified by c_1 and c_1(L_eps (x) C^2) = 2 beta(eps) = 0, (W_{s0}, C^2) ~ (W_{s1}, C^2).
   So there are exactly TWO PU(2) theories on Y, indexed by w in {0, eps^2} (eps^2 != 0 since eps^3 != 0), and
   NEITHER depends on the spin structure. Xi := (A,Phi) -> (u_*(A(x)eps), u Phi) is an isomorphism
   theory(W_{s1}) -> theory(W_{s0}), shifting CS by 1/2 (half-period lemma).
A2 [PROVED] Spin structures become LABELS on reducibles. In theory(W_{s0}), w=0: theta has Dirac D_{s0}(x)C^2,
   eps.theta has Dirac D_{s1}(x)C^2. Canonical label: a central flat E_a = L(+)L gives W(x)L = spinors of s(x)hol.
   Write theta_{s0}, theta_{s1}. w = eps^2: one reducible zeta = C (+) L_eps (U(2), det L_eps; SO(3) holonomy
   diag(-1,-1,1), stabiliser U(1)), Dirac D_{s0} (+) D_{s1}: it carries BOTH labels. For Delta_K = 1 there are no
   other abelian flat connections (abelian reps factor through H_1 = Z/2).
A3 [PROVED] The instanton involution chi: alpha -> eps.alpha is NOT a symmetry of the PU(2) theory: it carries
   D_A on W(x)E to D_A on W(x)L_eps(x)E (another operator; at theta: D_{s0} vs D_{s1}, different spectra).
   Consistency check: if chi were a symmetry, deg chi in {0,3} mod 6 (chi^2 = odd-degree SU(2) gauge map, 6Z);
   but deg chi = 4 (ASD) + 2 ind_C = 4 + 2(-1/2 - 2 rho_D) = 3 - 4 rho_D with rho_D := xi(s1) - xi(s0) and
   4 rho_D in Z odd, and rho_D moves by integers with the metric -> not invariant. So PU(2) BREAKS the chi-pairing
   of I(Y_{+-2}): on the E_1 page alpha and eps.alpha get Dirac regradings differing by 2 ind_C(alpha -> eps.alpha).
A4 [PROVED, one line] CORRECTION to pu2.tex Thm B(i): Seiberg–Witten points (A = B (+) B^{-1}, Phi in W(x)L only)
   are S^1-FIXED, not free: lambda.Phi = diag(lambda^{-1},lambda).Phi. (This is FL's fixed-point set: ASD + SW.)
   So SW points sit with theta_s, zeta in the localised part U^{-1}H^-; HPU = U-torsion contains only the
   instanton faces over irreducible alpha and genuinely irreducible PU(2) monopoles. SW points split by spin^c
   label t0/t1 (SW monopoles on W(x)L, L in {C, L_eps}): the SW sector is HM(Y,t0) (+) HM(Y,t1), labelled.
A5 [PROVED] Dirac rho mod Z is Rokhlin: xi(Y,s) = -sigma(X)/8 - eta_sign/24 mod Z for spin (X,s), so
   rho_D(Y) := xi(s1)-xi(s0) = -(mu(s1)-mu(s0))/8 = +1/4 (Y_2), -1/4 (Y_{-2}) mod Z (Arf=0). Its REAL value is
   NOT metric-independent (Dirac kernels jump on a hyperbolic Y); the user's 'metric-independent abelian
   invariant' holds only mod Z, where it is exactly the Rokhlin swap.  Numerics (pu2code/eta_lens.py, zeta-
   regularised, checked S^3 -> 0 and L(4,1) -> {-5/8,1/8,3/8,1/8} = faces-final): RP^3 round: eta(s0) = -1/4,
   eta(s1) = +1/4 (s0 extends over D_2: ind = -1/8 - xi(s0) in Z). So rho_D(RP^3 = Y_2(U)) = 1/4, consistent.
A6 [PLAUSIBLE: PSC + parity, standard package posited] HPU(L(p,q)) = 0. PSC + quartic term => Phi = 0; all flats
   abelian; theta: HP^infty towers (step 4), abelian alpha: J = j_W (x) j_E (antilinear, J^2 = +1, commutes with
   D_A for SU(2) A) pairs W(x)L with W(x)L^{-1}, so each eigenvalue gives a Morse–Bott S^2 = S^3/U(1) with
   scalar S^1 rotating it (2 fixed poles): Borel contribution free of rank 2, even degrees. Posit: ASD indices
   between abelian flats on lens spaces are even (true for instanton gradings of lens spaces, I^# even). Then all
   Borel generators have even degree, the odd-degree differential vanishes, H^- is free, HPU = 0.

## Step 2 — (b)/(c) levels: DROPPED per refocus. Kept only what gradings need:
- eta(RP^3,s0) = -1/4, eta(RP^3,s1) = +1/4 (round); K-independence for Delta=1 holds ONLY mod Z (= Rokhlin, A5);
  real values of eta(Y_{+-2}(K), s) are metric-dependent (spectral flow), so there is no K-independent real Omega.
- Unknot sanity (PROVED given A3 formula): rel. grading theta_{s0} -> theta_{s1} = 3 - 4 rho_D = 2 on Y_2(U) = RP^3,
  = 4 on Y_{-2}(U); reversed on Y_{-2} it is -4 = 2 mod 6: the swap phi_U is consistent; all generators even,
  so HPU(+-RP^3) = 0 by the parity argument (A6).
- Instanton chi-pairing check (pu2code/tkcheck.py with gap16 tk.py): Y_{+-2}(T_{2,3}), (T_{2,5}), (T_{3,4}): every
  generator is chi-paired (CS + 1/2, gr + 4 mod 8). PU(2) breaks this pairing (A3) — the only new 3D feature.

## Step 3 — refocus: 1 != 0 settings, evaluated
(i) SPIN MISMATCH — OBSTRUCTED [PROVED as logic from A1–A5].
  Group-level: there is ONE PU(2) theory per w; HPU(Y,s0) and HPU(Y,s1) are the same group (A1). A statement
  'nonzero for (Y_2,s0), zero for (Y_{-2},s1)' about groups is a statement about HPU(Y_2) vs HPU(Y_{-2}), with no
  spin content. Spin content lives only in (1) labels on theta_{s}, zeta and the SW sectors t0/t1 — these give
  Froyshov/connected-type data, invariant under (spin-labelled) Z/2-homology cobordism, hence equal to the RP^3
  values for slice K (KT), where the swap is consistent; (2) absolute gradings, whose spin content mod Z is
  rho_D = Rokhlin (A5), i.e. the swap itself. 's1 does not extend over X_{-2}' only says the reducible theta_{s1}
  does not propagate through X_{-2}: a statement about the trace, not about Y_{-2}; X_{-2} (b^+=0) has torsion-free
  relative invariant, so it gives no HPU class to vanish. VERDICT: spin enters any PU(2) proof only as a
  consistency condition, never as the 1 != 0.
(ii) CLOSED Z = X_2 cup_phi (-X_{-2}) — DEAD [PROVED].
  Simply connected, form I_2 (index-2 overlattice of <2>+<2>, both overlattices odd: forced by the swap), b^+ = 2.
  b^+ even, b_1 = 0 => d_ASD = 8k - 9, d_SW = (c^2-14)/4 = 2m-3 (c^2 = 2 mod 8), d_PU = d_ASD + 2 n_a all ODD:
  every Donaldson/SW/PU(2) invariant with H_0/H_2 insertions vanishes by parity. Independently: adjunction on the
  genus-2 A, B (A^2 = B^2 = 2) forces K.A = K.B = 0, impossible for characteristic K. Both 'sides' are 0: no 1.
  For slice K also Z = D_2 cup_{RP^3} (b^+=1 rest): PSC splitting. One-phi closed manifolds with b^+ odd are
  (-Z)#CP^2 etc. (homotopy rational surfaces, b^+ <= 1): chamber invariants fixed by homotopy type; no 1 != 0.
(iii) COBORDISM ENDOMORPHISMS + TRIANGLES — OBSTRUCTED as a contradiction [PROVED structure, PLAUSIBLE package].
  * HPU := U-torsion is NOT an exact functor: H^-(S^3) = H_*(HP^infty) (x) Q[[U]] is free of INFINITE rank (Thm A),
    and torsion of an exact triangle with a free vertex is exact only up to the image of that vertex. So HPU
    behaves like HF_red (towers at S^3), not like Floer's I (I(S^3)=0). The DLME +-1 mechanism does not transfer.
  * W_{lambda'} sits in the triad (Y_2; Y_{-2}, Y_0#RP^3) [Kirby check: K, K' parallel, lk 0; slide K over K'
    inside the annulus -> unknot; framings (-1,0) give Y_{-2}, Y_0#RP^3]. Third vertex has I^w(Y_0) != 0 (KM), so
    W_{lambda'} is never an isomorphism: phi_* W_{lambda'} has a nonzero cone; no forced iso.
  * Gradings: relative gradings are Z/6 (6 = 8 - 2), so a nonzero-degree iso forces only equidistribution of
    graded ranks mod gcd(d,6) — the analogue of OAI's Cor. 1.5 mod 8 — not a contradiction (Euler char = 0 for
    Delta = 1, as for the unknot).
  * Labels: W_{lambda'} (c = +-1) sends theta_{s0}(Y_2) -> theta_{s1}(Y_{-2}); phi_* W_{lambda'} is label-preserving.
    No spin^c / label mismatch is available.
(iv) FLOER FEEHAN–LENESS IN HPU — cannot create asymmetry [PROVED as logic]; useful as an organising principle.
  With A4, Borel localisation gives C_fixed (theta_s, zeta, SW sectors HM(t0)+HM(t1)) -> C -> C_free, and the
  FL relation is the connecting map / residue identity (instanton-face residues = - fixed-point residues).
  It is a 3D relation natural under phi, so it transfers no asymmetry: HF/HM has none for Hanselman's genus-2
  survivors, and instanton asymmetry, if any, is exactly what is unknown. It cannot 'create' a sign of surgery,
  which only 4D pieces (traces, handles) carry.
(d) W'-FAMILY / POINT 4:
  * S^3 face: vanishes on torsion cycles AT CHAIN LEVEL [PROVED given package]: m_2(z) is a cycle in the free,
    zero-differential C^-(S^3) with U^k m_2(z) = m_2(dw) = 0, so m_2(z) = 0.
  * Lens face does NOT drop out from HPU(L(4,1)) = 0 [PROVED]: the face is ext(- (x) c), c = relative invariant of
    the cap nu S in H^-(L(4,1)), carried by the energy-1/4 reducible gamma (U(1)-stabiliser): a LOCALISED (non-
    torsion) element inserted into a 3-ended exterior; ext(x (x) c) is torsion for torsion x and need not vanish.
    OAI's cancellation over the two lifts c, c+PD(S) is still required (H4-type sign).
  * The resulting B is defined on HPU(Y_2) only modulo m_1(H^-(S^3)) (secondary-map defect). There is no
    distance-4 triangle with zero middle term in HPU; the quasi-isomorphism (OAI's H2) gets no help.

## Step 4 — beyond (i)–(iv), and the structural obstruction
- O(2) symmetry [PROVED, checked on the functional]: for spin W and SU(2) E, J = j_W (x) j_E is antilinear, J^2 = +1,
  commutes with gauge and D_A; with scalars it generates O(2) (not Pin(2)). Natural under phi; Manolescu-type
  invariants from it are homology-cobordism invariants (KT-dead); the full modules carry no surgery sign.
- Double cover (Sigma_{+-1}(K~), tau): the two spin lifts of tau differ by -1 in SU(2) = gauge, so the equivariant
  theories coincide — the cover reproduces A1, nothing new.
- PRINCIPLE (PROVED as logic). Under phi every 3D structure (HPU with U-action, gradings, labels, O(2), FL
  connecting maps, cobordism maps of natural cobordisms composed with phi) is matched. A 1 != 0 therefore needs
  a 4D input carrying the surgery sign that is neither homotopy-theoretic (b^+ <= 2 rational pieces: (ii)) nor
  homology-cobordism-invariant (KT). The only universal such input is Gabai's foliation on Y_0 (KM caps C_+-),
  transported to Y_{+-2} by triangles. HPU transports badly (Step 3 (iii)); I transports exactly (I(S^3)=0).
  Hence the 1 != 0 must be OAI's template: nonvanishing in I via KM + Cayley–Hamilton, vanishing in PU(2).

## Step 5 — (e) outline of CSC via PU(2), with status
L1 PROVED: one PU(2) theory per w on Y_{+-2}; spin structures = labels on theta_{s}, zeta, SW sectors (A1,A2).
L2 PROVED: chi is not a PU(2) symmetry (A3); SW points are S^1-fixed (A4; corrects pu2.tex Thm B(i)).
L3 PROVED: rho_D mod Z = Rokhlin = +-1/4; eta(RP^3, s0/s1) = -+1/4 (A5, numerics); real rho_D not invariant.
L4 PLAUSIBLE (posit KM blow-up + Borel ES^1 package): H^-, H^+, H^infty, HPU are invariants with cobordism maps;
   gauge action on B^sigma free and S^1 free on ES^1 x B^sigma, so equivariant transversality is Thom-type. This
   dissolves OAI's 'hardest open point' (circle-stabiliser cokernels at abelian instantons) — it is where PU(2)
   genuinely helps.
L5 PLAUSIBLE: HPU(S^3) = 0 (sketch Thm A), HPU(L(p,q)) = 0 (A6, posit even ASD indices between abelian flats).
L6 PROVED (given L4): the S^3 face of the W' family vanishes on torsion cycles at chain level; the lens face does
   NOT (cap insertion); OAI's two-lift cancellation is still needed; B is defined mod m_1(H^-(S^3)).
L7 OPEN (= OAI (H2), ~65%): B rational isomorphism. HPU supplies no distance-4 quasi-isomorphism.
L8 PLAUSIBLE: b^+ >= 1 caps C_+- (KM) have relative invariants in HPU; nonvanishing of the Donaldson pairing along
   composites Pi_M (KM04 Cor 7 + Cayley–Hamilton, given L7).
L9 SPECULATIVE (Floer FL): HPU pairing through Pi_M = c 2^{n_a-1} (Donaldson pairing) + (fixed-point residues);
   needs degeneration of the E_1 = I(Y;Q) spectral sequence and the Euler-class (mu_c^{n_a-1}) identification.
L10 SPECULATIVE: fixed-point residues of X(Pi_M) vanish, by HM/HF maps of the pieces (replacing OAI's lattice,
   toric-PSC and cap estimates). Not checked; the HF degree argument alone gives finiteness, not vanishing.
L11 PROVED as logic: L7–L10 give 1 = 0. No step uses levels; no step uses the spin swap except as consistency.
VERDICT: the clean HPU-only 1 != 0 routes (i)–(iv) and point 4 FAIL for the precise reasons above; what survives
is OAI's architecture with L4 replacing the transversality bash and L9–L10 replacing the SW-exclusion bash —
conditional on (H2) exactly as before. Confidence that this route proves CSC: ~10% (dominated by L7, L9, L10).
