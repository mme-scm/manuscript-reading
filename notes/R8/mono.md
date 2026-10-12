# R8 mono.md — monopole mechanism for S^3_{2}(K) vs S^3_{-2}(K)

Status: started. Step 0: reading notes.

## Step 0 (done): what OAI used monopoles for
- OAI: closed X(Pi_M) built from composites of phi_*B (B = mu(S)-cut map on W'=(-X_2)∪X_{-2}), caps from KM symplectic manifold.
  Omega(X) != 0 via Witten's formula (KM04 Cor 7, i.e. monopole nonvanishing transported by Feehan–Leness), and
  Omega = 0 via SO(3)-monopole cobordism over a cube: the "bashy" part = excluding SW (reducible) strata on chains of
  positive pieces P = CP^2#5CP^2bar (lattice lemmas, toric PSC metrics, cap constants, coupled regularity).
- So monopoles enter OAI as (i) nonvanishing of a closed invariant (symplectic), (ii) the SO(3)-monopole bridge.

## Step 1: basic topology / spin bookkeeping (checked)
- Rokhlin mod 16: mu(Y2,s0)=1, mu(Y2,s1)=-1+8Arf, mu(Y-2,s0)=-1, mu(Y-2,s1)=1+8Arf. Cosmetic => Arf=0 and
  phi: s1(Y-2)->s0(Y2), s0(Y-2)->s1(Y2).
- d(Y2,s0)=-1/4, d(Y2,s1)=1/4, d(Y-2,s0)=1/4, d(Y-2,s1)=-1/4 when V0=0 (forced by cosmetic, Ni–Wu).
- W := W_{lambda'}: H_2=Z gen Sigma (Seifert surf ∪ core, genus g), Sigma^2=-1 => W NOT spin. X_2 ∪ W ≅ X_{-2} # CP^2
  (the class F_2+Sigma is a sphere of square +1: core(K) ∪ annulus ∪ core(K')).
- W' = (-X_2°)∪X_{-2}°: spin^c (c_l,c_r)∈(2Z)^2, all four minimal ones are d-sharp for unknot-type d's.
  (0,2): (Y2,s0)->(Y-2,s1) degree 0 — the cosmetic pairing, same as W with c1=±e.
- Monopole "level": L(out)-L(in) = -(E^an + pi^2 c1^2)/2 with E^an >= -∫ s^2/16-type metric term (NOT >=0).
  For W (c1^2=-1) monopole level is POSITIVE (reducibles at energy 1/4); for the reversed b+=1 handle W^+ : Y-2 -> Y2
  (c1^2=+1) it is formally -1/4, but only up to a metric-dependent scalar-curvature term. => a pure monopole
  CSD-filtration nilpotency argument violates the "energy >= 0" rule (monopole energy is not >= 0 without PSC).

## Step 2 (coordinator update): ignore 1/16 entirely. Goal = any strict separation on a large testable class.

## Step 3: HF has an EXACT "level": the absolute Q-grading
- In HF/HM, degree of (W,t) is (c1^2-2chi-3sigma)/4: topological, exact. A self-map of a finite-dim Q-graded space all of
  whose homogeneous components have degree <0 is nilpotent; an injective map V->W strictly lowering degree with
  dim V_k = dim W_k for all k forces W=0 (dim W_{<k} >= dim W_{<=k}).
- HF analogue of the instanton distance-4 triangle (triad slopes -2, 2, infinity; distances 4,1,1):
  HF+(Y_-2) --G--> HF+(Y_2) --> HF+(S^3) (x) F^4 --> HF+(Y_-2).
  G = map of M = (-X') ∪_{L(4,1)} A_3  (A_3 = (-2,-2,-2) plumbing, sharp cap; equivalently the triangle map with the
  4 top generators of HF(L(4,1))). M: Y_-2 -> Y_2, b+=1, b-=3, sigma=-2, chi=4, deg = (c^2-2)/4.
  Third vertex = towers only, so ker G ⊂ image of towers (G "injective mod towers") — the HF analogue of C(S^3)=0.
- Spin^c of M <-> (c_l,c_r) in (2Z)^2 on W' (classes on F_l,F_r), S=F_l-F_r, Sigma=F_l+F_r (Sigma^2=+4 in -X').
  c^2(M) = (c_l+c_r)^2/4 + c^2_{A3,sharp}(c_l-c_r mod 8), c^2_{A3} = 0 (≡4 mod 8), -3 (≡±2), -4 (≡0).
  Components and degrees (source spin -> target spin):
    s1(Y-2)->s0(Y2) [cosmetic pairing]: c_l+c_r=±2: deg -1 ; ±6: +1 ; ±10: +5
    s0(Y-2)->s1(Y2) [cosmetic pairing]: ±2: -1 ; ±6: +1 ...
    s1->s1: c_l+c_r ∈{0,±4}: -1/2 ; ±8: 7/2
    s0->s0: c_l+c_r=0: -3/2 ; ±4 (c_l-c_r=4): +1/2 ; ±8: 5/2
  Adjunction (OS, Sigma^2=4>=0, genus h): |c_l+c_r| <= 2h-6. A genus-(2g+1) representative of Sigma in X'
  (2F ∪ oriented resolution of alpha_+ ∪ alpha_- in T^2xI ∪ two cores) gives |c_l+c_r|<=4 at g=2: kills deg +1 pieces of
  the cosmetic pairings but NOT the s0->s0 deg +1/2 piece.
- KEY META-POINT (sharp negative, PROVED as logic): this whole argument only uses "dim HF_red(Y2)_k = dim HF_red(Y-2)_k".
  Any argument "natural map with property P + equal invariants => contradiction" is an object-level comparison in
  disguise. Since Hanselman shows graded HF groups CAN agree at ±2 for genus 2 (that is why g=2 is open), no HF/HM
  argument using only graded groups + cobordism maps can work on all g=2 knots. Same for instantons: the
  "negative-level injective map" programme is exactly "filtered complexes of Y_2, Y_-2 differ" (user expects not).
  => a successful mechanism must use an invariant that is NOT a function of (graded HF, filtered I) separately.

## Step 4: routes checked against calibration
- Z-route DEAD on the class (PLAUSIBLE->near PROVED): if K smoothly slice (KT), X_2(K) = D_2 ∪_{RP^3} C with C a
  Q-homology cobordism RP^3 -> Y_2, likewise -X_{-2}; so Z = D_2 ∪ R ∪ D_2 with R: RP^3 -> RP^3 a Q-homology cobordism.
  Every invariant computed by gluing along Y_{±2} (Donaldson, SW, mixed HF, Bauer–Furuta: S^1-maps of spheres of
  fixed-point degree 1 have degree 1) equals that of CP^2#CP^2. Also with V_0=0 all trace relative invariants in HF
  are tower-type, so mixed invariants of Z vanish for every K in the class.
- Double cover: unbranched double covers of Y_{±2} are Σ_{±1}(K~), Σ=Σ_2(K) a ZHS (Δ=1), K~ the lift (Δ_{K~}=1 by Fox).
  Cosmetic at ±2 => τ-equivariant cosmetic at ±1 in Σ. DLME fails upstairs (I(Σ)≠0); HF upstairs has same limits.
- Lefschetz idea: negative-level self-map => nilpotent => supertrace 0 at chain level. Closed M_f=(cob f)/φ, b1=1.
  Joint mechanism would need Witten/Furuta–Ohta=SW-type theorem for b1=1 manifolds AND a φ-independent way to
  compute one side. Corrections are functions of end invariants, which φ preserves; a genuine self-cobordism with the
  same data (e.g. (Y2×I)#CP2bar) satisfies the same formula => no fractional obstruction. Route gives only a
  constraint on an unknown integer. SPECULATIVE/negative.
- OAI Cor (instanton only, given H1): cosmetic => dim I_j(Y_2;F) independent of j∈Z/8 (odd-degree iso H∘φ^{-1}).
  Joint version (SPECULATIVE): + a Z/4-graded I^# ≅ HF^ (KM conjecture) => HF^ mod-4 equidistribution (after removing
  the two tower generators), which fails for e.g. A^red_1 = F_(k)⊕F_(k+1). Relies on an open conjecture.
- Checked & discarded: eigenvalue/genus-detection through the W_{λ'} triad (F^ is the square-0 core class of the
  2-handle in V: Y_0#RP^3 -> Y_2, not homologous into Y_2 — no constraint).

## Step 5: the precise residual of the HF (exact-grading) route, and the Witten transfer
- Per-spin^c regrading is allowed (φ preserves s^±, labelled by Rokhlin / quadratic refinement q(μ)=1/4 for s^+).
  With adjunction |c_l+c_r|<=4 (g=2), G's components (source Y_-2 -> target Y_2), s^+=s1(Y-2)->s0(Y2) etc.:
    diag s^+->s^+, s^-->s^- : deg -1 only
    swap s^+->s^- : -1/2 (c_l+c_r ∈{0,±4})        swap s^-->s^+ : -3/2 (0), +1/2 (±4)
  Shift s^- grading by δ: swap degrees -1/2+δ and +1/2-δ. Optimal δ=1/2 gives all degrees <=0, with the
  degree-0 part G_0 = the two spin-SWAP blocks (P: s^+->s^-, Q: s^-->s^+). Filtration argument: if φ∘G_0 is
  nilpotent (⇔ QP composite with φ nilpotent) and G is injective on HF_red, then HF_red=0 => contradiction.
  So HF alone closes EXCEPT for one φ-dependent degree-0 block: the spin-swap composite. (If P or Q vanished the
  argument would be object-level, hence subsumed by graded groups — object-level principle.)
- Rational blow-down remark (PLAUSIBLE): W_{λ'} = W' with νS replaced by the rational ball B (∂=L(4,1)); π1 agree
  (π1(E_K)/<<μ^2,λ>>); the spin^c on L(4,1) extending over B are exactly c·S ≡ ±2 (8) (d=0), i.e. EXACTLY the
  cosmetic pairings. So "the forced spin pairing" = "spin^c that survive rational blow-down of S".
- Witten transfer (conditional on FL's Witten formula for C_-∪(cob)∪C_+, simple type): D-maps are the
  Fourier transform over w∈H^2(;Z/2) of SW-maps; inversion separates t from t' iff (c_t-c_t')/2 is odd on some class.
  On W_{λ'}: e and -e separated (via w·Σ), e and -3e not, but different degrees => each SW(N,t)=0 separately.
  CONSEQUENCE (testable prediction, no cosmetic assumption): instanton W_*=0 for all bundles forces
  F^HF_{W_{λ'},±e} = 0 on cap-detected HF_red for every K. Hence W_{λ'} can NEVER supply the HF injectivity.
  Consistent check: HF^ rank count in the λ' triad: closed (figure-eight type) curve components add the same
  amount to every slope => 2 dim HF^(Y0) = dim HF^(Y2)+dim HF^(Y-2) => summed hat map is 0, as in instantons.
- General principle: Witten-transfer turns instanton negative-level nilpotency into HF nilpotency of the
  corresponding spin^c composites. Joint argument closes iff some instanton map of negative level has, after
  Fourier inversion, the degree-0 swap block of G in its spin^c support. The instanton map Fourier-dual to G is
  the triangle map c (-X' with γ1 end), level +3/16 > 0: wrong sign. => this is the precise gap.

## Step 6: the HF theorem (main positive output) — checked
Inputs: (T) OS n-surgery triangle HF+(Y_m)->HF+(Y_{m+n})->HF+(S^3)^{⊕n} with m=-2,n=4, first map = Σ_s F_{-X'}(·⊗Θ_s)
= Σ over A_3-sharp t^ of F_{M,t^}, M=(-X')∪A_3 [PLAUSIBLE: standard identification];
(A) OS adjunction for HF+ cobordism maps, Σ^2>=0, g>=1 [HT&4M Thm 1.5]; (NW) cosmetic => V_0(K)=V_0(Kbar)=0.
- X' = W' minus νS ⊃ E_K×I; ∂νS = V_{μ^2λ} ∪ T^2×I ∪ V_{μ^-2λ} = L(4,1). Σ = F×{t1} ∪ F×{t2} ∪ (genus-1, 4-holed
  smoothing surface of α_+∪α_- in T^2×I, 4 crossings all same sign, no trivial circles) ∪ 2 meridian disks:
  χ = 2χ(F) - 4 + 2 = -4g, genus 2g+1, Σ^2=+4 in M. Adjunction: |c_l+c_r| <= 4g-4.
- Lemma G (PROVED from T, NW): ker G ⊂ towers (third vertex = towers), G kills towers (b+(M)=1), F_2 injective on
  towers of Y_2 when V_0=0 (trace maps sharp) => Gbar: HF_red(Y_-2) -> HF_red(Y_2) injective; iso if also V_0(Kbar)=0.
  Sanity: RHT (V_0=1) violates injectivity hypothesis correctly; 4_1: Gbar = P_0 : F_(-1/4) -> F_(-3/4), iso, deg -1/2. ✓
- Filtration lemma: φ^{-1}∘Gbar filtration-preserving (δ-degrees <=0) + iso + finite-dim => associated graded iso.
- THEOREM H.
  (a) g(K)=1: only c_l+c_r=0 survives: P_0 (s+->s-, deg -1/2), Q_0 (s- -> s+, deg -3/2). δ=1/2: degrees 0,-2; G_0=P_0
      squares to 0 => φ^{-1}Gbar nilpotent, contradiction with iso unless HF_red=0 (impossible: V_0=0, K≠trefoil).
      => no ±2 cosmetic for genus one (known: Wang; here a 5-line proof).
  (b) g(K)=2: survivors D_{±2} (diag, deg -1), P_0 (-1/2), P_{±4} (-1/2), Q_0 (-3/2), Q_{±4} (+1/2!).
      δ=1/2 is forced; degree-0 part G_0 = P_0+P_{±4} (s+->s-) and Q_{±4} (s- -> s+). Q_{±4} is the EXTREMAL
      adjunction case (|<c,Σ>|+Σ^2 = 8 = 2·5-2). Cosmetic => P and Q_{±4} are graded F[U]-isomorphisms.
      Corollary (testable, K only): A^red_0(K) ≅ (A^red_1(K) ⊕ A^red_{-1}(K))[shift: A_0 sits one degree lower,
      tower-normalised], i.e. HF_red(S^3_2(K),s-) ≅ HF_red(S^3_2(K),s+)[-1/2].
      Genus 2 is the last case for THIS mechanism precisely because of the one extremal block Q_{±4}.
  Caveat (object-level): (b)'s corollary follows from HF+ graded-module equality; it is finer than HF^ (Hanselman
  uses hat) but is still a graded-group statement. It cannot by itself exclude a hypothetical matching curve.
- Sector bookkeeping: <c,S> ≡ ±2 (8): D_{±2};  ≡ 4: P_0, Q_{±4};  ≡ 0: Q_0, P_{±4}.
  Fourier heuristic for B = m_c - ε m_{c+PD S} (μ(S)-cut): support factor <c,S>(1-ε(-1)^{<c,S>/2}).
  With ε=-1: support = sector 4 = {P_0, Q_{±4}} = (almost exactly) HF's degree-0 obstruction. Consistent with
  Conj B at g=1 (Gbar = P_0 iso for 4_1). So instantons (B: level +1/8) and HF (G_0: δ-degree 0) obstruct in the
  SAME sector. SPECULATIVE dictionary but two consistency checks pass (4_1; sector of the -4-sphere relation).

## Step 7: direction check and remaining mixing attempts
- Triangle direction: slopes increase cyclically ∞ -> -2 -> 2 -> ∞, so HF(S^3)^4 -> HF(Y_-2) -> HF(Y_2) -> HF(S^3)^4;
  F_3 = traces X_{-2}° (neg. def.), F_2 = flipped -X_2° (neg. def.), G = distance-4 map. Only this cyclic order exists
  (the other is the orientation reversal), so there is no φ-free reverse map Y_2 -> Y_-2 with L-space third vertex.
- Instanton counterpart of the residual block: the distance-4 instanton maps are c (-X' with γ1 end, level +3/16)
  and B (μ(S)-cut, level +1/8), whose Fourier support (ε=-1) is the <c,S>≡4 sector. Positive level => the CS
  filtration cannot make the residual nilpotent. Sharp negative for "kill Q_{±4} by instanton levels".
- Extremal adjunction does NOT bound rank(Q_{±4}): the factorisation goes through HF+(Y_-2 # Σ×S^1, top)
  ≅ HF+(Y_-2)⊗(rank 1), not through a rank-1 group.
- Involutive remark: over F_2, conjugate blocks pair as X + ιXι; for s^+ on Y_2, ι swaps A_1 and A_-1, so the
  residual is the ι-anticommuting part of Q_{+4}; this is the reported involutive dead end in another guise.

## VERDICT (R8)
1. PROVED (mod. standard HF inputs T, A, NW): Theorem H. HF's absolute grading, shifted by δ=1/2 on s^-, is an
   exact topological "level". The distance-4 triangle (third vertex = towers) gives an iso Gbar on HF_red.
   g=1: all blocks have δ-degree <=0 and the degree-0 part is nilpotent => no ±2 cosmetic (known; short proof).
   g=2: exactly one positive block survives adjunction: the extremal spin-swap block Q_{±4}
   (<c,Σ>=±4, <c,S>≡4 mod 8, degree +1/2). Cosmetic => P, Q_{±4} graded isos => A^red_0 ≅ (A^red_1⊕A^red_-1)[-1].
2. The obstruction is theory-independent: the same <c,S>≡4 (mod 8) sector carries B (level +1/8) in instantons.
   No CS-level argument can kill it; no HF-degree argument can either.
3. Sharp negatives: Z-route dead (slice KT ∈ class); Pin(2)/spin pairing = cobordism-level; W_{λ'} cannot feed
   non-nilpotence (Witten transfer forces its HF maps to be cap-null); Lefschetz route constrains only unknown
   integers; object-level principle: any map-based HF argument = graded-group comparison.
4. What a successful mixed argument must do: produce a φ-sensitive input that makes the degree-0 swap composite
   (φ^{-1}Q_{±4})(φ^{-1}P) nilpotent. Neither CS levels nor Q-gradings do; a joint invariant (e.g. a Q-graded lift of
   the instanton Z/8 grading compatible with B, or Z/8-equidistribution (OAI Cor) + a graded I^#≅HF^) is needed.

## Step 8: sanity check of Theorem H(b) on box models (CFK = x_0 ⊕ boxes), F_2 coefficients
- n-box B_n (a at (0,0) M=0, b at (-n,0), c at (0,-n), d at (-n,-n)) gives A^red_s = F[U]/U^{n-|s|} for |s|<n, bottom
  degree 2|s|-1; reproduces 4_1 (A^red_0 = F_(-1), HFK gradings (1,0,0,0,-1) ✓).
- Genus-2 pieces: B_1^(0) (A_0+=F), pair B_1^(±1) (A_{±1}+=F each), B_2^(0) (A_0+=F[U]/U^2, A_{±1}+=F each).
  Signed counts n_0,n_1,n_2: Δ=1 ⇔ n_2=-n_1, n_0=2n_1. H(b) (U-module iso A_0 ≅ (A_1⊕A_-1)[-1]) ⇔ N_2=0, N_0=2N_1
  (+ grading conditions). So for box models: a cosmetic Δ=1 genus-2 knot has NO 2-box and only parity-cancelling
  pieces. (Here H(b) also follows from the hat-level comparison; it is a reformulation, not a new obstruction.)
  Note: the Hanselman-type configuration x_0 + 2B_1^(0) + B_1^(±1) has Δ = 1 ± (t^{1/2}-t^{-1/2})^4 ≠ 1.
