# D. The PU(2) step as a families/relative Witten-type vanishing theorem

Thread D of BRIEF.md. Manuscript labels refer to `src/*.tex`.
Tags: **[V]** means I checked the computation, or checked the logic against the text. **[P]** means plausible. **[S]** means speculative.
Literature is cited from memory, and bibliographic details (titles, venues, theorem numbers) are unverified.

## 0. Conclusions

1. **[V]** Sections 8–10 prove an $S^1$-localization statement with a single fixed component. The only $S^1$-fixed points of the cut-down PU(2) moduli over the parameter cube are the $\Omega$ instantons. The remaining ends are lens-face ends, which cancel in bit pairs. Hence $2^{n_D-1}\Omega=0$. The most old-fashioned name for this is Pidstrigach–Tyurin localization in the empty-window case, parametrized over a cube whose faces are psc neck-stretchings (§1).
2. **[V]** Dictionary. Type S is an irreducible SW solution for $K=\Lambda+v$, with fixed self-dual perturbation $\beta^+$, $[\beta/2\pi]=\Lambda$. Type R is the reducible SW solution, which is the same thing as an Abelian ASD reducible with line difference $v$, i.e. a Donaldson (Kotschick–Morgan) wall. R never meets a cap, so R occurs only on interior pieces at $J$-faces.
3. **[V]** Sections 7–8 do **not** prove that any families SW moduli space is empty. They prove two things:
   - **(L)** SW *localization*: the clamp band, $u=0$ on long tubes, and the cap bounds $K_W^2,v_W^2\le C_W$.
   - **(B)** A lattice/charge *budget*: after paying for the $n$ sphere tests, the charge any (L)-admissible reducible needs exceeds $\kappa$. In the closed stratum this means $\ell=\kappa+v^2/4<0$. Broken tuples violate $\sum(q_i+4)=4$.

   So the slogan "families Witten + families SW vanishing ⇒ families Donaldson $=0$" is the wrong shape. The right shape is "gluing-free PU(2) cobordism + families SW localization + window budget ⇒ $2^\eta\Omega=0$".

   Vanishing of a families SW *invariant* would not suffice: using it would need Feehan–Leness gluing at the reducible strata. It is also not defined here: $b^+(X)=m+b_0\approx n/4<\dim Q=n$, so walls are crossed (§2).
4. **[V]** Per block of $k$ intervals carrying one positive bridge:
   - $\Delta n_D=(5-k)/8$;
   - the fixed-type (R/S) score is $\ge 3k-7$;
   - the mixed R-run score is $\ge k-4$.

   Hence $n_D>0$ iff the average $k<5$. The fixed exclusion needs only $k\ge3$; the mixed P/R exclusion needs $k\ge4$. Spacing four is used **only** in Lemma `indices:mixed-run`. The upper bound $m/n\le 1/4$ is forced by Abelian zero-spinor (R) runs in mixed limits, not by the SW (S) exclusion. This refines the brief's heuristic (§4).
5. **[P]** Most of Sections 9–10 adapts existing tools: FL-I/II, Donaldson/MMR neck analysis, Kotschick–Morgan reducibles in families, and branched-manifold Stokes. The genuinely new analytic lemma is the "necessary projection" for mixed P/R tuples (Lemma `analysis:projection`). The minimal new statement is Theorem R in §3.

## 1. What the PU(2) cobordism proves

**1.1 Data.**
- $X$ is closed with $H_1(X;\mathbb Z)=0$ and $b^+=m+b_0$.
- $Q=\prod_{i=1}^n[-3,3]$. The face $t_i=-3$ stretches the neck $J_i\cong S^3$; the face $t_i=+3$ stretches $\partial N_i\cong L(4,1)$, where $N_i=\nu S_i$ and $S_i^2=-4$. Both links carry psc (Thm `geometry:family`).
- For $e\in\{0,1\}^n$: $c_e=c_0+\sum e_i\,\mathrm{PD}(S_i)$, and $\kappa=c_2-c_e^2/4$ is fixed. The spin$^c$ class $l$ is fixed and $\Lambda_e=l+c_e$.
- Cuts: $n$ holonomy sphere tests $x(S_i)$ of degree 2, cap probes of degree $z$, and $D_I=8\kappa-3(1+b^+)=n+z$.
- $\Omega=\sum_e\varepsilon(e)\,\#\{(t,[A]) : t\in\mathrm{int}\,Q,\ A\in M^{\rm ASD}_{g_t}(E_e)\cap V_{x(S_\bullet)}\cap V_z\}\in\mathbb Z$.

**[V]** $\Lambda_e^2=\Lambda_0^2$ because $\Lambda_0S_i=2$, $S_i^2=-4$ and $S_iS_j=0$. Likewise $c_e^2=c_0^2-4|e|$. So $\Theta=(\Lambda^2-\sigma)/4$ and $n_D=\Theta-\kappa$ are independent of $e$.

**1.2 Theorem V (abstracted from Thm `gluing:contradiction`).** Assume the following.
- **(H0)** $n_D\ge1$.
- **(H1)** Every $S^1$-fixed point of the compactified cut-down PU(2) moduli over $\bar Q$ is an unbroken, loss-free irreducible instanton. Compactified means all $e$, all faces and all Uhlenbeck levels.
- **(H2)** Every limit of free (P) points is either unbroken, or a single lens-face limit with minimal trace cap ($\kappa_N=1/4$) and no particles.
- **(H3)** At such an end, the bit-flip partner $e_i\mapsto 1-e_i$ has the opposite $\varepsilon$-weighted orientation.

Then $2^{\,n_D-1}\Omega=0$.

Sources in the manuscript:

| Hypothesis | Manuscript source |
|---|---|
| (H1) | Prop `indices:fixed-exclusion`, Thm `estimates:clamp`, Prop `analysis:first-stage` |
| (H2) | Prop `indices:mixed-exclusion`, Lemma `analysis:projection`, Prop `analysis:finite-induction` |
| (H3) | Prop `gluing:signs` |
| The count itself | Prop `analysis:instanton-link` and Lemma `analysis:stokes` |

**1.3 Old-fashioned formulation (Pidstrigach–Tyurin localization) [V as logic].** Let $\mathcal M$ be the free stratum cut down by the tests, the probes and $\eta=n_D-1$ sections of the phase-weight-2 line, divided by $S^1$. Then $\bar{\mathcal M}$ is a compact weighted 1-manifold with
$$\partial\bar{\mathcal M}=\bigsqcup_{A}\operatorname{sign}(A)\cdot\big(\mathbb P(\ker D_A)\cap\{\eta\ \mathcal O(2)\text{-divisors}\}\big)\ \sqcup\ \bigsqcup_{\rm lens}(\text{main}\times\text{cap}).$$

This is the $S^1$-localization identity "sum of fixed-point contributions + face terms $=0$" in the case where the instanton component is the only fixed component. PT, Okonek–Teleman and FL built the cobordism to compute the other fixed components (SW strata at all levels $\ell$). Here those components are absent, so no reducible gluing is needed.

Caveat **[V]**: psc alone would not empty the S-strata. The effective SW perturbation is $2\pi\Lambda^+$, and §2.1 shows that a solution needs $vH$ strictly between $0$ and $-\Lambda H$. The band is empty only if $\Lambda H=0$.
- [P] FL obtain $n_D\ge1$ by enlarging $\Lambda$, which widens the band.
- The manuscript instead obtains $n_D$ from topology (many $b^+=1$ cells) and keeps $|\Lambda H_I|\le 3/2$ on each cell, so each band is narrow.
- This is the conceptual reason the manuscript needs a clamp and not just scalar curvature.

**1.4 Comparison with Feehan–Leness [P for the FL side].** FL (*An SO(3)-monopole cobordism formula…*, Mem. AMS, 2018) give, for closed standard $X$:
$$D^w_X(h^{\delta-2m}x^m)=\sum_{s}(-1)^{\cdots}\,SW_X(s)\,f_{\delta,m}(\chi_h,c_1^2,c_1(s),\Lambda;h),$$
with universal polynomial coefficients. I believe the general case rests on a gluing theorem at reducible strata of all levels, whose full proof was not published. That is unverified. The analogues here:

| | FL, closed | Here |
|---|---|---|
| Fixed loci | instantons; SW strata $M_{s'}\times\mathrm{Sym}^\ell X$ with $c_1(s')=K$ | instantons (type A); type S on pieces; plus type R |
| Level condition | $\ell=\kappa+(K-\Lambda)^2/4\ge0$ | identical: $\kappa_i=-v_i^2/4+\ell_i$ (Lemma `indices:virtual-sums`) **[V]** |
| "Basic classes" | $K$ with $SW(K)\ne0$ | classes $K=\Lambda+v$ admitted by (L), i.e. bounded on caps, in the clamp band on positive cells, $vU=0$ on long tubes, and test-compatible ($vS_j\ne0$ or a paid unit of $\ell$) |
| Role of $\mu$-insertions at reducibles | coefficient polynomials in $\langle K-\Lambda,\cdot\rangle$ | the holonomy test at a reducible has winding $vS/2$ (Lemma `stack:tests`), so it is "all-or-nothing" in $vS$. **[P]** It is the analogue of the leading factor $\langle v,S\rangle$ of $\mu(S)$ on reducible links. |
| Auxiliary $\Lambda$ | free; chosen to make $n_D$ large | constrained by $\Lambda S_i=2$ and $\Lambda^2_{\rm cell}\in\{-2,0\}$. A large odd $\Lambda(E_{\rm exc})$ on the caps pushes cap basic classes out of the window, at a cost of $\approx\Lambda(E)^2/4$ in $\Theta_0$, repaid by $q_0$. **[V]** This matches the order of choices in Table `stack:choices`. |
| R-type (Abelian, $\Phi=0$) | absent for generic metrics on closed $X$ with $b^+\ge1$ | present as a families phenomenon at $J$-faces, since $\dim Q>b^+$; analogue of Kotschick–Morgan wall terms or u-plane terms |
| Faces | none | $J$: excluded by index. Lens: cancel in lift pairs. |
| Gluing at reducibles | required | none |

**1.5 The exponent [V].**
- **Why $\eta=n_D-1$.** The free dimension is $(D_I+n-2n-z)+2n_D-1-2\eta=2n_D-1-2\eta$, so dimension 1 forces $\eta=n_D-1$.
- **Why the link is $\mathbb{CP}^{n_D-1}$.** With $\operatorname{coker}D_A=0$, the normal link of an instanton is $S(\ker D_A)/\{\pm1\}$, and its phase quotient is $\mathbb P(\ker D_A)$.
- **Why the cuts are $\mathcal O(2)$.** $-1\in S^1$ acts as the central gauge, so only even phase characters descend. A weight-2 function $q(\lambda z)=\lambda^2q(z)$ is a section of $\mathcal O(2)$. Equivalently, $S(K)/\pm1\to\mathbb P(K)$ is the Hopf bundle squared.
- **The count.** $\langle(2h)^{n_D-1},[\mathbb{CP}^{n_D-1}]\rangle=2^{n_D-1}$. The explicit sections $z_j^2-a_jz_0^2$ have $2^{n_D-1}$ transverse zeros.
- Only nonvanishing matters, so FL's normalization of the corresponding class is irrelevant.

## 2. Is type-S absence a families SW vanishing statement?

**2.1 Dictionary [V].** In the proof of Lemma `estimates:projection` the reduced equations are $\rho(iD^+)=(\psi\psi^*)_0$, with Dirac curvature $i(\beta+D)$.
- Put $F_B=i(\beta+D)$, the connection on $\det$ of the spin$^c$ structure with $c_1=K=\Lambda+v=l+2c_1(L_1)$. The equations become $\rho(F_B^+-i\beta^+)=(\psi\psi^*)_0$ and $D_B\psi=0$. These are the SW equations for $K$ perturbed by $i\beta^+$.
- Reducible SW solutions satisfy $\psi=0$, which gives $D^+=0$: $v$ is anti-self-dual, which is type R.

So R is simultaneously the SW wall for $(K,\beta^+)$ and the Donaldson wall for $v$.

- The R-type cap exclusion is the classical generic-period argument, using $b^+(W)>0$ (Prop `estimates:cap`). Hence R occurs only on interior pieces, i.e. at $J$-faces.
- The integrated Weitzenböck identity gives $\psi\ne0\Rightarrow (vH)(KH)<0$, i.e. $vH$ lies strictly between $0$ and $-\Lambda H$. This is the standard $b^+=1$ chamber band. With $\Lambda H=0$ it is psc vanishing.
- The vertex test reduces the band condition over the period square $H=U+aX_1+bX_2$, $(a,b)\in[0,\tfrac14]^2$, to the four vertices $H_I$. Walls $\{vH(a,b)=0\}$ are lines in $(a,b)$.
- **[V]** The positive cell has lattice $H\oplus4\langle-1\rangle\cong\langle1\rangle\oplus5\langle-1\rangle$ (odd, indefinite, rank 6, $\sigma=-4$).
  - $l|_{\rm cell}=(-4,-2;-1,1,-1,-1)$ has $l^2=4=2\chi+3\sigma$.
  - So the cell has the homological SW profile of a rational surface, and the clamp is the families form of "rational surfaces have no SW solutions on the psc side of the wall".

**2.2 What Sections 7–8 actually prove.**

(L) Families SW localization:
- (L1) the clamp band and vertex test on positive-width cells;
- (L2) $u=vU=0$ on long $S^2\times S^1$ tubes;
- (L3) caps: no R; for S, $v_W^2,K_W^2\le C_W$ by the standard a priori bound on $F^+$, i.e. finiteness of basic classes;
- (L4) $d_s+p_i+4\ell_i\ge0$, the expected dimension of families SW.

(B) Budget:
- each assigned test contributes $\le-2$ to $v^2$ or one unit of $\ell$;
- each positive cell contributes $Q\le-2$ (or an exception paid by $\ell$);
- hence $8\kappa_i\ge 4s_N+4m_i$;
- and $8\kappa$ is fixed by $D_I=n+z$.

**[V]** Closed stratum ($k=0$, $L=n$):
- Any reducible meeting the tests needs $8\kappa_{\rm red}=-2v^2+8\ell\ge4(n-2m)+4m-O(1)$, with tests paid by nonzero halves or by units of $\ell$, and the caps contributing $O(1)$ through $v_W^2\le C_W$.
- But $8\kappa=n+3m+O(1)$.
- So once $3n>7m+O(1)$ no $K$ qualifies: a test-compatible $K$ has $\ell(K)<0$, and a test-incompatible $K$ needs even more $\ell$.

The SW analysis enters only through (L1) and (L3), with (L4) used for short end components. No SW moduli space is asserted to be empty. The content is: every SW-admissible class lies outside the window $W_\kappa=\{(K-\Lambda)^2\ge-4\kappa\}$ after the tests are paid for. For $k\ge1$ the exclusion is of tuples, via $\sum(q_i+4)=4$; individual pieces may well carry SW solutions.

**2.3 Not equivalent to vanishing of a families invariant [V].**
- (a) Vanishing of a count would not exclude the strata. Converting it into vanishing contributions needs FL-type gluing at S-strata, which is exactly what is avoided.
- (b) The invariant is not defined. Li–Liu-type families SW over $B$ needs $b^+>\dim B+1$, but here $b^+=m+b_0\approx n/4<n$. Walls (type R) are crossed generically, and the cube has faces.
- (c) The statement is metric-specific: the toric periods and the generic cap periods. It is not deformation-invariant.
- (d) The converse direction is trivial: absence implies vanishing of anything computed from those moduli.

**2.4 Standard-language replacement [P].**

*Proposition L (families SW localization).* For each face $F\subseteq\bar Q$, each piece $Y$ of the $F$-decomposition (psc ends $S^3$, $L(4,1)$) and each $K\equiv l\pmod 2$: if $\mathfrak M^{SW}(Y/F;K,\beta^+)\ne\emptyset$, then (L1)–(L4) hold. If $\psi\equiv0$, it lies on the wall $v^+=0$, and on a cap this never happens.

*Lemma D (window disjointness, pure lattice).* No tuple $(K_i)$ satisfies (L1)–(L4), test-compatibility, $\ell_i\ge0$ and $\sum(q_i+4)=4$.

Proposition L is classical in families form: Weitzenböck chambers (Witten; LeBrun for scal $\ge0$ Kähler), a priori bounds, families transversality (Li–Liu), and $S^2\times S^1$ necks. At psc faces it is compatible with the fibered-product picture for families SW (Baraglia–Konno gluing along $S^3$; Kronheimer–Mrowka's K3#K3 Dehn twist), which is unverified in detail. Lemma D is Section 8.

The correct slogan is: **"gluing-free PU(2) cobordism (Theorem R) + Prop L + Lemma D + lens pairing ⇒ $2^\eta\Omega=0$."**

## 3. Existing technology versus Sections 9–10

| Step | Manuscript | Predecessor | Status |
|---|---|---|---|
| Compactness, closed parts | Lemmas `analysis:compactness`, `analysis:neck` | FL-I (PU(2) Uhlenbeck); parametric version routine | [P] |
| psc necks $S^3$, $L(4,1)$ | spinor dies (Lemma `indices:lens-charge`); $H^1(Y;\mathrm{ad}\rho)=0$ | Donaldson's *Floer homology groups* (gluing with stabilizers); Morgan–Mrowka–Ruberman, $L^2$ moduli and vanishing theorem | [P] |
| Transversality of A, S-tangential, P | Prop `analysis:first-stage` | Donaldson–Kronheimer; families SW (Li–Liu); FL-I/Teleman holonomy perturbations for P | [P] |
| Instanton link and $2^\eta$ | Prop `analysis:instanton-link` | FL PU(2)-II link lemma (the manuscript's citation) | [V], elementary |
| R in families | budget only | Kotschick–Morgan, families Donaldson (Ruberman) | [P] |
| **Mixed P/R tuples** | forget R fields but keep parameters; projected index; multisections | nearest: Donaldson's connected-sum dimension count and MMR. There the reducible piece is retained with its stabilizer; here it is discarded. | **new** |
| Lens ends | minimal cap with invertible Dirac and $U(1)$ stabilizer absorbed | gluing at reducible flats (Donaldson's book, MMR); lens/rational-blowdown instantons (Austin; Fintushel–Stern) | [P] |
| Orientation of lens pairs | local cap tensor; the Dirac factor is complex | Donaldson orientations; the bit-sum resembles sums over $w$ in Kronheimer–Mrowka structure theory | [P]; new in detail |
| Weighted Stokes | Lemma `analysis:stokes` | branched manifolds (McDuff; Cieliebak–Mundet–Salamon) | [P]; probably avoidable, since the free stratum has stabilizer $\pm1$ |

Families monopole Floer (Kronheimer–Mrowka families maps; Lin) and families Bauer–Furuta concern SW, not PU(2). They could at best repackage (L), and since all faces are psc nothing Floer-theoretic is needed. **[P]**

**Theorem R (proposed minimal new statement) [S as stated].** Let $(X,g_t)_{t\in Q}$ be a cube family whose faces stretch disjoint psc rational homology spheres with nondegenerate flats and invertible flat Dirac. Fix spin$^u$ data with $n_D\ge1$, exact-support cut representatives and the dimension condition. Assume:
- (E1) the only fixed ideal tuples are unbroken instantons;
- (E2) every tuple containing P has negative projected index (8.projection-input) $-2\eta-1$, except unbroken points and single minimal lens ends.

Then, for small generic (multivalued) perturbations, $\mathcal M_{\rm cut}/S^1$ is a compact weighted oriented 1-manifold. Its boundary is the instanton links, each of weight $2^{n_D-1}\operatorname{sign}$, together with the regular ends (main) × (cap crossing).

Everything except "(E2) ⇒ emptiness" is a family-with-faces version of FL-I/II + PT plus MMR. The single new analytic lemma is Lemma `analysis:projection`, together with its R-independence input: the projected problem is Fredholm, has finite isotropy and can be made transverse with global phase cuts.

## 4. Bookkeeping

**4.1 [V]** I recomputed each identity below from the stated definitions.

| Identity | Derivation |
|---|---|
| Lattice (positive cell) | $Q_P^{-1}$ on $(x,u)$ is $\begin{pmatrix}0&1\\1&-2\end{pmatrix}$, so $v^2=2xu-2u^2-\sum t_b^2$ |
| Positive cell: $\Lambda_0$ and $c_0$ | $\Lambda_0^2=4-2-2=0$; $c_0^2=0$ |
| Negative cell: $\Lambda_0$ | $\Lambda_0^2=-2=\sigma_{\rm cell}$ |
| Cell contributions to $\Theta$ | $0$ (negative cell), $1$ (positive cell) |
| Charge | $8\kappa=n+z+3+3m+3b_0$ |
| Dirac index | $n_D=m+\Theta_0-\kappa=\tfrac{5m-n}8+\Theta_0-\tfrac{z+3+3b_0}{8}$ |
| Virtual sum | $\sum q_i=D_I-3k+(n-k)-2n-z=-4k$, so $\sum(q_i+4)=4$ |
| Spinor sum | $\sum i_i-2\eta=2-4k$ |
| Fixed exclusion | $2a+6b+2\ge6>4$ |
| Mixed projected dimension | $5-4N-\sum_R(4+i-p)\le3-2N<0$ for $N\ge2$ |
| Lens end | the trace cap of charge $1/4$ costs $\delta_{\rm sp}-1=1$, so the lens end has dimension 0 |

**4.2 Per-block calculus [V].** One block is $k$ consecutive intervals containing one positive bridge.

| Quantity | Formula | $k=3$ | $k=4$ | $k=5$ |
|---|---|---|---|---|
| $\Delta(8\kappa)$ available, from $D_I=n+z$ | $k+3$ | 6 | 7 | 8 |
| $\Delta(8\kappa)$ required by a reducible run ($s_P=2$, $s_N=k-2$, $Q\le-2$) | $\ge 4k-4$ | 8 | 12 | 16 |
| $\Delta n_D$ | $(5-k)/8$ | $+1/4$ | $+1/8$ | $0$ |
| fixed score $\Delta(q+4)=8\kappa-3m+L-2s$ | $\ge3k-7$ | $+2$ | $+5$ | $+8$ |
| mixed R-run score $\Delta(4+i-p)=6\kappa-m-2s$ | $\ge k-4$ | $-1$ | $0$ | $+1$ |

**4.3 Where spacing four is used [V].** I grepped every use of the spacing.
- Lemma `indices:fixed-run` uses $L\ge4m-3$. Redoing its case analysis with $L\ge3m-2$:
  - $m=2$, $L=4$: the minimum over $s\in\{3,4,5\}$ is $-2$;
  - $m=3$, $L=7$: the minimum is $-2$;
  - $m\ge3$ in general: $3L-2-7m\ge2m-8\ge-2$;
  - $m=1$ is unchanged.

  So spacing 3 suffices. Spacing 2 fails ($m=2$, $L=3$, $s=4$ gives $-3$).
- Lemma `indices:end-exclusion` and Prop `stack:composition` (each seam adjacent to at most one macro) also hold at spacing 3. The slot reservations of Lemma `indices:component-score` remain disjoint at spacing 3.
- Lemma `indices:mixed-run` genuinely needs 4. Its bound $s-4m+r+\Delta+3\,\mathrm{miss}$ decreases by about $1$ per block at spacing 3, so it is unbounded below on long runs, and $3-2N<0$ fails.

**4.4 Conceptual reasons.**
- **Lower bound [V].** Each interval carries a degree-2 test, which raises $8\kappa$ by 1 and so lowers $n_D$ by $1/8$. A $b^+=1$ cell raises $8\kappa$ by 3 but raises $\Theta$ by 1, a net gain of $5/8$. Negative-definite cells cannot help: on $r\langle-1\rangle$ a characteristic $\Lambda$ has $\Lambda^2\le-r=\sigma$. The Dirac index the link needs must therefore come from $b^+$, giving density $>1/5$.
- **Upper bound [V for the arithmetic].** Positive cells are where reducibles are cheap: the clamp extracts only $v^2\le-2$ per positive cell, which pays for one of its two adjacent tests.
  - In ASD units (rate $8$ per unit of $\kappa$), one interleaving negative-rule test per positive cell already suffices ($3k-7>0$ iff $k\ge3$).
  - In the mixed projection, a forgotten R-run removes spinor index at rate $6$ per unit of $\kappa$ ($8$ from ASD, $-2$ from Dirac). Each positive cell also has net $-1$ ($-3$ from $b^+$, $+2$ from $\Theta$).
  - So each positive cell needs three negative-rule tests: $k\ge4$.
- So the upper bound protects against Abelian zero-spinor (Donaldson-wall) runs adjacent to a free component, not against SW (S) strata.

**4.5 [S] A possible relaxation.** The projection discards the wall condition for R: on a positive-width cell, $vH(a,b)=0$ is codimension 1 in the macro parameters. Counting it would add $+1$ per positive cell to the R-run score ($k-3$ instead of $k-4$) and widen the window to $(1/5,1/3]$. This requires transversality of the period map to the walls, and I have not checked it.

## 5. Risks within this thread

- (H1) rests on test property (ii): if $vS=0$ at a reducible, a unit of $\ell$ is required. This is implemented by the bespoke zero-winding holonomy modification, whose persistence under Uhlenbeck limits is flagged in the digest. Its classical analogue (that $\mu(S)$ restricted to reducible links has leading factor $\propto\langle v,S\rangle$) is [P], not checked.
- The clamp's sharpness uses $|\lambda_I|\le3/2$. Any change of $\Lambda$ on positive cells widens the SW band and could admit S-strata.
- The binding constraint is the mixed R-run bound, which is the least classical part (projection plus multisections). An independent check should start with Lemma `analysis:projection` and the R-independence lemma.
- I did not check the instanton-link orientation convention ($\sigma_0$ common to all instantons) or the lens-pair sign; see the other threads.
