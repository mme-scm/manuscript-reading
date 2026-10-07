# B3. An $S^1$-equivariant PU(2)-monopole Floer theory for the spin-filtered route

Thread B3 of BRIEF.md (round 2). Labels: **[V]** I checked the computation or the logic; **[P]** plausible; **[S]** speculative.
**†** marks literature cited from memory; details such as titles, theorem numbers and dates are unverified.
Manuscript labels refer to `src/*.tex`; "DLME" means arXiv:2410.21248.
Notation: $Y_r=S^3_r(K)$, $g(K)=2$, $\phi:Y_{-2}\to Y_2$ orientation preserving. All Floer groups are taken with $\mathbb Q$ coefficients unless stated otherwise (§1.4 explains why).

## 0. Conclusions

1. **Design [P].** The natural theory is Kronheimer–Mrowka's monopole Floer construction (blow up along $\{\Psi=0\}$, then form the three flavours $\check I,\hat I,\bar I$), with two substitutions:
   - KM's reducible locus is replaced by the entire instanton configuration space;
   - KM's constant-gauge circle is replaced by the phase circle $S^1/\{\pm1\}$.

   The boundary flavour $\bar I^{\rm PU}$ is then instanton Floer homology coupled to the family of 3-dimensional Dirac operators. This is KM's "coupled Morse theory", with the torus of flat $U(1)$-connections replaced by the Chern–Simons flow on $\mathcal B^{\rm inst}(Y)$.
2. **The spin level is a grading [V, formal APS].** On a cylinder, $n_D(A)=\sigma_t(\alpha')-\sigma_t(\alpha)$, where $\sigma_t=\widetilde{\rm CS}-\rho_t$. Hence $\sigma_t$ takes values in a single coset of $\mathbb Z$; up to sign it is the Dirac spectral flow from $\theta$, and it marks where the Dirac tower over $\alpha$ splits. So the "spin filtration" is an **integer second grading**, not a real-valued filtration, and $\ell_t\in{\rm const}+\tfrac18\mathbb Z$. The period's shift of $-\tfrac18$ is exactly one quantum.
3. **$\ell_t$ is tower data [V as algebra, given item 1].** Consider the monotone case: no free critical points, and every instanton trajectory has $n_D\le0$. Then the boundary-stable flavour *is* the spin-filtered instanton complex $F^\sigma_{s_0}C^{\rm inst}$, and $u$ acts as the deck (charge-one) shift $T$. In general, the image $L_t$ of $\check I^{\rm PU}$ in the localized theory defines a "$u$-adic" filtration (Def. 2.1).
   - The localized cobordism map on the instanton block is $u^{L_\sigma}(W,c)_*$, with $L_\sigma=-c^2/4-\Theta_W$.
   - So **monotonicity is equivalent to the reducible-transport condition (RD)** of §2.3. Preservation of the lattice is automatic.
   - The closed template is Atiyah–Bott polynomiality: $2^{n_D-1}\Omega\,u^{-1}\in\mathbb Q[u]$.
4. **Coefficients [V].** The theory needs $\mathbb Q$ or $\mathbb Z_{(2)}$, not $\mathbb F_2$, because $u$ acts on an instanton link as $2h$. Injectivity over $\mathbb Q$ follows from the mod-2 units via the finite-lattice lemma (`stack:finite-lattice`).
5. **Why single maps fail [P].** In this theory $\check I^{\rm PU}(S^3)\ne0$: it is a $\theta$-tower. So the interval map $B$ is *not* a chain map: its $J$-face defect factors through the $S^3$ tower. This is the Floer shadow of the closed fact "type R occurs only at $J$-faces". Blocks must control exactly this defect. Since $HB\simeq{\rm id}$ mod 2 has spin shift $-\tfrac12$, (RD) must fail for $B$ or $H$ for every $K$ with $I(Y_2;\mathbb Q)\ne0$ [V, given the framework].
6. **Would-be proof [S].** Assume block monotonicity for the period $\mathcal P=(\phi_*B)^3HB$. Then DLME's Lemmas `kappa-ineq` and `inhomog-ineq` give $\ell_t(Y_2)\le\ell_t(Y_2)-\tfrac18$, a contradiction. Five constructions are needed (§3).
7. **Literature [†].** To my knowledge, no PU(2)/SO(3)-monopole Floer theory has been constructed. The closest existing pieces are:
   - KM's book (the template);
   - Daemi–Miller Eismeier (the $\Psi=0$ sector including $\theta$);
   - Feehan–Leness (the closed analysis);
   - Austin–Braam (equivariant Morse–Bott Floer theory).

   The gap is large. The required theory is essentially the machine one would want for comparing $I^\sharp$ with $\widetilde{HM}$, which is open.
8. **Cheap alternative [V].** Lemma C (§5) is the exact abstract replacement for `kappa-ineq` + `kappa-basic`(c). Its content: a mod-2-unit endomorphism with a nonzero integral pairing, together with closed vanishing along an arithmetic progression, is contradictory. The manuscript is an instance of it. The Floer theory would imply Lemma C's hypothesis (b) (Lemma C′), but it is strictly more than the proof needs.

   **Recommendation:** organize the proof around Lemma C, and present the Floer theory as the conjectural framework of which the closed argument is the shadow.

## 1. The theory

### 1.1 Data [V]
- $Y$ is a rational homology sphere.
- $E\to Y$ is a $U(2)$-bundle with a fixed determinant connection; this gives $w=c_1(E)\bmod 2$.
- $t$ is a spin$^c$ structure with spinor bundle $\mathbb S_t$. The spin$^u$ data are $\mathbb S_t\otimes E$.

For $Y_{\pm2}$ we have $H^2(Y;\mathbb Z)=\mathbb Z/2$. The manuscript takes $w=0$ there: Floer's determinant-one complexes, with central reducibles $\theta$ and $\theta'$. Then:
- $\mathrm{Spin}^c(Y_{\pm2})$ has two elements, and both are self-conjugate, since $2x=0$.
- So any composite of cobordism maps $(Y_2,t)\to(Y_2,t'')$, transported by $\phi$, returns to $t$ after at most two iterations. If $\phi^*$ swaps the labels, use $\mathcal P^2$.
- The $\alpha$-independent normalizations of $\rho_t$ (the signature-$\eta$ and $\Lambda^2$ terms) depend only on $(Y,t)$. They therefore cancel in any endomorphism of $(Y_2,t)$.
- We never need invariance of $\ell_t$ under change of metric or perturbation. The argument compares one fixed choice of data on $Y_2$ with itself, with the data on $Y_{-2}$ taken to be $\phi^*$ of it. **This removes the need for continuation maps**, which would be the first place the reducible sector interferes (§2.3).

### 1.2 Configurations and fixed points
A configuration is a pair $(B,\Psi)$:
- $B$ is a connection on $E$ with the fixed determinant;
- $\Psi\in\Gamma(\mathbb S_t\otimes E)$;
- we work modulo the determinant-one gauge group $\mathcal G$.

The functional is $\mathcal L=\widetilde{\rm CS}(B)+\tfrac12\langle D_B\Psi,\Psi\rangle$, the PU(2) analogue of CSD (normalization †). Its critical points satisfy $D_B\Psi=0$ and $*F^0_B=\rho^{-1}(\Psi\Psi^*)_{00}$.

The phase circle $S^1$ acts by $\Psi\mapsto e^{i\vartheta}\Psi$. Its element $-1$ acts as the central gauge, so the effective group is $T_\phi=S^1/\{\pm1\}$. The 3D classification is the 4D one of Def. `indices:types`, restricted to $\mathbb R$-invariant solutions [V].

| type | 3D critical point | stabilizer in $(\mathcal G\times S^1)/\pm1$ | contribution |
|---|---|---|---|
| A | $\Psi=0$, $B$ irreducible flat $\alpha$ | $S^1$ | Dirac tower $\{(\alpha,\lambda_j)\}_{j\in\mathbb Z}$ |
| R | $\Psi=0$, $B$ reducible flat (on $Y_{\pm2}$: $\theta,\theta'$, central) | $U(2)$ | $\theta$-tower; the A and S sectors meet here |
| S | $\Psi\neq0$ in one summand of a parallel splitting; 3D SW type for $K=\Lambda+v$ | $S^1$ (compensated by gauge) | off-diagonal tower |
| P | everything else | finite ($\pm1$) | one generator, $u$-torsion |

On a psc rational homology sphere (here $S^3$ and $L(4,1)$), the Weitzenböck formula kills $\Psi$, so only type R occurs. On $L(4,1)$ these are the states $+$, $-$ and trace of Prop. `indices:lens-index`. [V]

### 1.3 Blow-up and flavours [P]
Write $\Psi=r\psi$ with $\|\psi\|_{L^2}=1$ and $r\ge0$, and divide by $T_\phi$.
- This is KM's $\sigma$-blow-up verbatim. In KM, the locus $\{\Psi=0\}$ modulo gauge is a point (for a QHS) or a torus. Here it is $\mathcal B^{\rm inst}(Y)$, which carries its own Chern–Simons flow.
- The boundary critical points over $\alpha$ are the pairs $(\alpha,\lambda_j)$, where $\lambda_j$ runs over the eigenvalues of $D_{\alpha,t}$ (simple after perturbation). Such a point is boundary-stable iff $\lambda_j>0$.
- As in KM:
$$\check C=C^o\oplus C^s,\qquad \hat C=C^o\oplus C^u,\qquad \bar C=C^s\oplus C^u,$$
with KM's matrix formulas for the differentials. Here $C^o$ is generated by the P points. The S points have nontrivial isotropy in the interior, so they need either a second blow-up along the split locus (Feehan–Leness's link picture) or a local Borel model. [S]
- A boundary trajectory over an instanton trajectory of index $2k+1$ carries a projectivized Dirac solution. Hence $\bar\partial=\sum_{k\ge0}\bar\partial_{(2k+1)}$, where:
  - $\bar\partial_{(1)}$ is $\partial^{\rm inst}$ with $u$-weights;
  - the terms $\bar\partial_{(2k+1)}$ with $k\ge1$ evaluate Chern classes of the Dirac index bundle over instanton moduli.

  These are KM's coupled-Morse terms, and also the Floer analogue of the Chern-class corrections $1/e(N)=u^{-n}(1-c_1/u+\dots)$ in closed localization.

**Gradings [V, from $D_{\rm sp}=D_I+2n_D$, Lemma `indices:closed`].**
- $\mathrm{gr}_{\rm PU}(\alpha)=\mathrm{gr}(\alpha)-2\sigma_t(\alpha)$, measured at the split of the tower, and $u$ has degree $-2$.
- A charge-one lift changes $(\mathrm{gr},\sigma_t)$ by $(-8,-1)$, so it changes $\mathrm{gr}_{\rm PU}$ by $-6$. The theory is therefore relatively $\mathbb Z/6$-graded.
- A bubble costs 6 PU dimensions and recovers 4 position dimensions, so the net cost is 2 (Lemma `indices:loss-budget`). That is enough to exclude bubbles from every 1-dimensional moduli space: those used for $\partial^2=0$, for chain maps, and for the identities of 1-parameter family maps such as $B$. It is not enough for 2-dimensional moduli spaces. The instanton theory has net cost 4, so this margin is smaller.

### 1.4 Coefficients [V]
- Over $\mathbb F_2$ the theory is useless for this problem. Near an instanton, the effective-circle bundle $S(K)/\pm1\to\mathbb P(K)$ has Euler class $2h$, so $u$ acts on the link's equivariant cohomology by $2h\equiv0$. The closed output $2^{n_D-1}\Omega=0$ is vacuous mod 2 whenever $n_D\ge2$.
- So use $\mathbb Q$. With $\mathbb Q$ coefficients, $H^*(BS^1)$ and $H^*(BT_\phi)$ agree up to $u'=2u$.
- The ordinary maps $B,H,f_\pm$ are integral and are mod-2 quasi-isomorphisms. By `stack:finite-lattice` they are isomorphisms over $\mathbb Z_{(2)}$, hence over $\mathbb Q$. That gives the injectivity DLME's lemma needs.

### 1.5 The spin level is an integer grading
**Lemma 1 [V, formal; the APS normalization constants † are still TO CHECK].** Let $\rho_t(\alpha)$ be the APS correction $(\eta+h)/2$ of $D_{\alpha,t}$, plus $\alpha$-independent terms. Put $\sigma_t=\widetilde{\rm CS}-\rho_t$. Then for every path $A$ on $\mathbb R\times Y$ from $\alpha$ to $\alpha'$ (with the lift of $\alpha'$ fixed by $A$):
$$n_D(A)=\sigma_t(\alpha')-\sigma_t(\alpha).$$
Consequently:
- (i) $\sigma_t(\alpha)\in\sigma_t(\theta)+\mathbb Z$. This is the APS congruence $\rho_t\equiv\mathrm{CS}+{\rm const}\pmod{\mathbb Z}$.
- (ii) $\sigma_t(\alpha)-\sigma_t(\theta)=\pm\,\mathrm{SF}(D_{\theta,t}\leadsto D_{\alpha,t})$.
- (iii) A charge-one lift changes $\sigma_t$ by $-1$, matching "charge $+1$ lowers the Dirac index by 1" in the proof of Prop. `indices:lens-index`. Hence $\sigma_t-\mathrm{gr}/8$ is lift-invariant and lies in a single coset of $\tfrac18\mathbb Z$.

*Proof.* On a product we have $\Theta=0$ and $c=0$, so the brief's formula reads $n_D=-\widetilde{\rm CS}(\alpha)+\widetilde{\rm CS}(\alpha')+\rho(\alpha)-\rho(\alpha')$. Since $n_D\in\mathbb Z$ for every path, (i) and (ii) follow. ∎

Moreover, the boundary-stable/unstable split of the tower over $\alpha$ sits at the spectral position of $D_{\alpha,t}$ measured from $\theta$, which is $\sigma_t(\alpha)$ up to one global constant [P]. **So the spin level is precisely the height of the Dirac tower.** DLME's real-valued CS filtration is replaced by an integer second grading.

### 1.6 Localization
Fix one normalization $s_0\in\sigma_t(\theta)+\mathbb Z$ per pair $(Y,t)$. Let $\iota_0(\alpha)=(\alpha,\lambda_0)$ be the split point of the tower, and set $\iota(\alpha):=u^{\,s_0-\sigma_t(\alpha)}\iota_0(\alpha)$.

**Lemma 2 [V as index bookkeeping].**
- A $\bar\partial$-trajectory over an index-1 instanton $A$ runs from $(\alpha,\lambda_i)$ to $(\alpha',\lambda'_{i-n_D(A)})$. Hence $\bar\partial_{(1)}\iota_0(\alpha)=\sum_A\#\,u^{-n_D(A)}\iota_0(\alpha')$, and therefore $\bar\partial_{(1)}\iota(\alpha)=\sum_A\#\,\iota(\alpha')$.
- A lift satisfies $\iota_0(\alpha_{k+1})=\iota_0(\alpha_k)$, since a gauge map preserves eigenvalues, while $\sigma$ drops by 1. Hence $\iota(\alpha_{k+1})=u\,\iota(\alpha_k)$: **$u$ acts as the deck shift $T$.**
- So the A-sector of $\bar C[u^{-1}]$, restricted to $\bar\partial_{(1)}$, is the lifted ($\mathbb Z$-graded, 8-periodic) instanton complex $C^{\rm inst}_{\rm lift}$, with $u=T$ and with the grading reduced mod 6.

**Conjecture L (localization) [S].**
- (a) There are finitely many P and S critical points, by the 3D Weitzenböck $C^0$ bound together with Uhlenbeck compactness. Hence $\check I^{\rm PU}[u^{-1}]\cong\bar I^{\rm PU}[u^{-1}]$, and the free part is $u$-torsion.
- (b) $\bar I^{\rm PU}$ is the homology of the coupled complex on the sectors A, R and S. Its A-sector has a spectral sequence starting from $I(Y;\mathbb Q)_{\rm lift}$ with $u=T$, whose higher differentials come from $\bar\partial_{(2k+1)}$, $k\ge1$.
- (c) For a cobordism $(W,c,\mathfrak s)$ with $b_1=0$, possibly with a family $G$ and cuts, the localized map has A→A block
$$\iota(\alpha)\ \mapsto\ u^{\,L_\sigma+s_0-s_0'}\,(W,c)_*\,\iota(\alpha)+(\text{coupled terms}),\qquad L_\sigma=-\tfrac{c^2}4-\Theta_W.$$
It also has entries into and out of the R and S sectors, coming from type R and S fixed points on $W$, and face terms through $\check I^{\rm PU}(Z)$ for each psc neck $Z$.

The exponent in (c) is [V]. The closed link computation gives the normal Euler class $u^{n_D}$, hence the weight $u^{-n_D(A)}$. With $n_D(A)=\Theta+c^2/4+\sigma(\alpha')-\sigma(\alpha)$, the terms telescope in the $\iota$-basis.

**Closed template [V].** For a closed $X$ (a cobordism $\emptyset\to\emptyset$):
- $\check I^{\rm PU}(\emptyset)=\mathbb Q[u]\subset\mathbb Q[u^{\pm1}]=\bar I^{\rm PU}(\emptyset)[u^{-1}]$.
- The localized invariant is $\sum_A{\rm sign}(A)\,u^{-n_D}(2u)^{n_D-1}=2^{n_D-1}\Omega\,u^{-1}$. The $\eta=n_D-1$ phase cuts are sections of the weight-2 line, with Euler class $2u$.
- Polynomiality forces $2^{n_D-1}\Omega=0$. This is the manuscript's Stokes argument (Lemma `analysis:stokes` with Prop. `analysis:instanton-link`), written as an Atiyah–Bott residue identity.

**Monotonicity in the Floer theory is the relative form of this polynomiality.**

## 2. The spin-filtered invariant $\ell_t$ as tower data

### 2.1 Definition
Let $L_t(Y):=\pi_A\big(\mathrm{im}(\check I^{\rm PU}(Y,t)\to\bar I^{\rm PU}(Y,t)[u^{-1}])\big)$. Using $\iota$ and Lemma 2, regard it as a subset of $I(Y;\mathbb Q)_{\rm lift}$. This needs:

**(G)** The coupled terms $\bar\partial_{(2k+1)}$, $k\ge1$, do not disturb the identification of the A-sector with $I_{\rm lift}$; otherwise work on the $E_\infty$ page. [S]

**Definition 2.1.** Set $F^u_sI_d(Y):=\big(T^{\,s_0-s}L_t\big)\cap I_d$.

**Lemma 3 [V, algebra].** Suppose $L_t$ is a $\mathbb Q[u]$-submodule ($u=T$) with
- $L_t\cap I_D=I_D$ for $D\ll0$, and
- $L_t\cap I_D=0$ for $D\gg0$.

(Both are lattice properties. The first is Conj. L(a); the second is that $\check I^{\rm PU}$ is bounded on one side, as $\check{HM}$ is.) Then $F^u_\bullet$ is an IP-module in DLME's sense (Def. `I-module`), with periodicity $T^{-1}:F_sI_d\xrightarrow{\cong}F_{s+1}I_{d+8}$.

*Proof.*
- $TL\subset L$, so $F_s\subset F_{s+1}$.
- We have $F_sI_d\cong L\cap I_{d+8(s_0-s)}$. This vanishes for $s\ll0$ and is all of $I_d$ for $s\gg0$, which gives axiom (b).
- Axiom (a) holds because $T$ commutes with the inclusions. ∎

Define $\kappa_t$ and $\ell_t(Y)$ to be DLME's $\kappa$ and $\ell$ of $F^u_\bullet$. By Lemma 1, $\ell_t$ lies in a single coset of $\tfrac18\mathbb Z$. Also $\ell_t<\infty$ if and only if $I(Y;\mathbb Q)\ne0$.

**Lemma 4 (monotone case) [V, given the KM structure of §1.3].** Assume:
- there are no P or S points;
- the R-sector is decoupled from the A-sector;
- every index-1 instanton trajectory has $n_D(A)\le0$.

Then $\check C_A=C^s=F^\sigma_{s_0}C^{\rm inst}_{\rm lift}$, which is a subcomplex, and $u=T$ acts on it. Hence $F^u_s=F^\sigma_s:=\mathrm{im}\,H(F^\sigma_sC)$, and $\ell_t=\min(\sigma_t-\mathrm{gr}/8)$ over surviving classes, which is the brief's definition.

*Proof.* The stable part of the tower over $\alpha_k$ is $\{u^m\iota(\alpha_k):m\ge\sigma(\alpha_k)-s_0\}=\{\iota(\alpha_{k'}):\sigma(\alpha_{k'})\le s_0\}$, using $u\,\iota(\alpha_k)=\iota(\alpha_{k+1})$ and $\sigma(\alpha_{k+1})=\sigma(\alpha_k)-1$. Monotonicity says $\partial$ does not raise $\sigma$. ∎

**General case [P].** Here $\check\partial=\bar\partial^s_s-\partial^u_s\bar\partial^s_u+(C^o\text{ terms})$.
- $\bar\partial^s_u$ consists of the $\sigma$-raising instanton trajectories, those with $n_D\ge1$.
- $\partial^u_s$ counts free PU(2) trajectories returning from $C^u$ to $C^s$.

So a $\sigma$-raising trajectory is corrected by its free "return". This is the Floer form of the closed statement that an $n_D\ge1$ instanton is the end of a free family, with link $\mathbb{CP}^{n_D-1}$. The $u$-adic filtration $F^u$ is therefore the $\sigma$-filtration corrected by free PU(2) trajectories.

### 2.2 Comparison with existing tower invariants [†]
- **Frøyshov's instanton $h$, and DME's invariants for rational homology spheres.** These come from the $SO(3)$-equivariant tower of $\theta$, with $U$ of degree 4. That tower is the R-sector here, and it is *not* what $\ell_t$ uses.
- **The new feature.** Every irreducible flat carries an $S^1$-tower, and the "reduced" part consists of the P points. So $\ell_t$ is a filtration on all of $I(Y)$ induced by the free PU(2) part, not the bottom of a single tower.
- **Daemi's $\Gamma_Y$ and Nozaki–Sato–Taniguchi's $r_s$.** These record Chern–Simons levels along the $U$-tower of $\theta$. DLME's $\ell$ is the $\theta$-free shadow of $\Gamma$. In $\ell_t$ the real-valued CS filtration is replaced by the integer Dirac height.
- **The monopole/HF $d$-invariant and Frøyshov's monopole $h$.** These are the bottom of the tower of $\bar{HM}$ inside $\check{HM}$. Definition 2.1 is the same construction, applied to the A-sector towers instead of the reducible one.
- **Hendricks–Manolescu $\underline d,\bar d$; Lin and Stoffregen $\alpha,\beta,\gamma$.** There, an extra symmetry splits one tower into several numbers. **[S]** On $Y_{\pm2}$ every $t$ is self-conjugate and $E$ is quaternionic, so $\mathbb S_t\otimes E$ has an antilinear structure commuting with $D$. This would enlarge $S^1$ to an $O(2)$-type symmetry and might allow Pin(2)-style refinements. It is not needed here.

### 2.3 Cobordism maps: monotonicity, and when reducibles drop out
**Proposition 5 [V as algebra; inputs: Conj. L, (G)].**
- *Setting.* Let $(W,c,\mathfrak s)$ be a cobordism $(Y,t)\to(Y',t')$ with $b_1(W)=0$, possibly with a family $G$ and cuts. Let $M$ be its localized map. Let $\pi_A$ and $\pi_R$ project onto the A sector and onto the R and S sectors.
- *Hypothesis (RD).* $M_{A\leftarrow R}\big(\pi_R\,\mathrm{im}\check I^{\rm PU}(Y)\big)\subset L_{t'}(Y')$. Also, the coupled part of $M_{A\leftarrow A}$ and, for families, the face terms map $L_t(Y)$ into $L_{t'}(Y')$.
- *Conclusion.* $(W,c,G)_*$ is an IP-morphism $F^u_\bullet I(Y)\to F^u_\bullet I(Y')$ of degree $D=-2c^2-3b^+(W)+\dim G-\mathrm{codim}$ and level $L_\sigma=-c^2/4-\Theta_W$. If it is injective, then
$$\ell_{t'}(Y')\le\ell_t(Y)+L_\sigma-D/8.$$

*Proof.*
1. Maps on $\check I^{\rm PU}$ commute with localization, so $M$ carries $\mathrm{im}\check I(Y)$ into $\mathrm{im}\check I(Y')$, up to face terms in the family case.
2. For $y$ in the image we get $\pi_AMy=u^{a}W_*\pi_Ay+M_{A\leftarrow R}\pi_Ry+(\text{coupled})\in L'$, with $a=L_\sigma+s_0-s_0'$.
3. By (RD), $u^aW_*(L)\subset L'$.
4. If $T^{s-s_0}x\in L$, then $W_*x\in T^{\,s_0'-s-L_\sigma}L'=F'_{s+L_\sigma}$.
5. Finally apply DLME Lemma `kappa-ineq`(b). ∎

So all of the content is in (RD): **monotonicity = "no reducible-to-instanton transport in the window"**. The lattice part is free, because it is the integrality of the non-localized theory.

**When (RD) holds: sufficient conditions.**
- **(a) No type S on $W$ in the window.** This follows from the Weitzenböck band $(vH)(KH)<0$ with $\Lambda^+$ small: the clamp, as in D-families §2.1 [V closed analogue]. [P]
- **(b) No type R in the interior of $W$.** This follows from $b^+(W)>\dim G$ and a generic period [V, standard]. If $b^+(W)=0$ (as for $B$, $\phi$, and continuation maps), then *every* $v$ has an abelian ASD representative. These fixed points map R to R. They are harmless unless they are composed with A→R and R→A transports.
- **(c) A↔R transports at the ends.** These are instantons from $\theta$ to an irreducible flat, or the reverse: Frøyshov's $D_1$/$D_2$ maps.
  - At leading order (index 0), Floer's codimension-3 count controls them [P].
  - Their $u$-weighted coupled versions are not controlled by this. **This is a genuine gap.**
- **(d) Faces at psc necks.** These are R-mediated by construction, since only type R lives on a psc rational homology sphere.
  - Lens faces cancel in bit pairs: the PU(2) form of Prop. `gluing:signs` [P].
  - $J$ faces do not cancel (§2.4).

### 2.4 Why single maps fail
For $B$ (interval $G$ from $J$ to the lens split, with the cut $x(S)$), Stokes on the 1-dimensional family gives
$$\partial M_B-M_B\partial=\delta_J-\delta_{\rm lens},\qquad \delta_{\rm lens}=0\text{ after the bit sum [P]},$$
where $\delta_J=M_{C_{-2}}\circ M_{-C_2}$ factors through $\check I^{\rm PU}(S^3)$.
- In Floer's irreducible theory $\delta_J=0$, because $C(S^3)=0$.
- In the PU(2) theory, $\check I^{\rm PU}(S^3)$ is a $\theta$-tower. So $\delta_J$ is the composite A→R$_{S^3}$→A. It consists of $\Psi=0$ instantons on $-C_2$ (respectively $C_{-2}$) with limit $\theta_{S^3}$, coupled through the $S^3$ Dirac tower, together with split solutions on the two halves.

**Proposition 6 [V, given Prop. 5 and the mod-2 facts].** For no $K$ with $I(Y_2;\mathbb Q)\ne0$ can (RD) hold both for $B$ (including $\delta_J$) and for $H$.

*Proof.*
1. $HB$ is a $\mathbb Q$-automorphism of $I(Y_2)$: it is a mod-2 unit, and `stack:finite-lattice` applies.
2. The formal values are: for $B$, $(D,L_\sigma)\in\{(-1,0),(7,1)\}$, which are equivalent under periodicity; for $H$, $(-3,-1)$. So the shift of $HB$ is $-\tfrac12$.
3. Prop. 5, applied with the transport by $t$ (squared if necessary), gives $\ell_t(Y_2)\le\ell_t(Y_2)-\tfrac12$. But $\ell_t$ is finite by Lemma 3. ∎

Both maps are suspect:
- $H$ has no faces, but $W_H$ has $b^+=1$ and $\Theta=1$ (the rational-surface profile), so type S may occur.
- $B$ carries $\delta_J$.

The closed budget of D-families §4.2 says (RD) can only hold for blocks: the fixed-type score is $3k-7$ and the mixed R-run score is $k-4$.

### 2.5 Block monotonicity
**Conjecture M$_{\rm block}$ [S].** Let $\mathcal P_k=(\phi_*B)^{k-1}\circ HB$, with $k\ge4$ (the manuscript takes $k=4$). Its localized map is the sum over the $2^k$ bits and the $k$-cube of interval parameters, with the lens faces cancelled. Conjecture: this map satisfies (RD) on $L_t(Y_2)$. That is, every R/S-mediated contribution to the A→A entry, including all $J$-face defects of the $k$ intervals and all passages through the R/S sectors of the intermediate $Y_{\pm2}$ seams, maps $L_t$ into $L_t$. Consequently $\mathcal P_k$ is an IP-endomorphism of shift $(k-5)/8$.

**Arithmetic [V].**
- The shift is negative iff $k\le4$.
- The mixed score is nonnegative iff $k\ge4$.
- So $k=4$ is the unique integral block length. Equivalently, the closed window is $\tfrac15<m/n\le\tfrac14$.
- The relaxation of D-families §4.5 would allow $k=3$ as well.

**Weak point.** The closed budget never meets the R/S sectors of $Y_{\pm2}$, namely $\theta,\theta'$ and the 3D SW points, because the manuscript keeps all $Y$-seams finite. M$_{\rm block}$ must control these Floer-end sectors *for arbitrary incoming lattice elements*. That is stronger than the closed statement, which uses the global identity $\sum(q_i+4)=4$ with fixed caps. I see no mechanism that converts the closed budget into this per-block statement automatically. **[S]**

## 3. The would-be DLME-style proof, and what it needs

**Theorem (conditional) [S].** Assume Conj. L, (G) and M$_{\rm block}$ for $k=4$. Then no $\phi$ exists.

*Proof.*
1. **Data.** Fix a metric, a perturbation and $t$ on $Y_2$, and transport them to $Y_{-2}$ by $\phi$. The period map is $\mathcal P=(\phi_*B)^3\circ H\circ B$ on $I(Y_2;\mathbb Q)$. This is the manuscript's $\mathcal A^3\mathcal D$ (`stack:nonzero`).
2. **$\mathcal P$ is invertible over $\mathbb Q$.** $B$, $H$ and $\phi_*$ are integral mod-2 units (Thms `ordinary:units`, `negative:unit`), so `stack:finite-lattice` applies. [V given the manuscript]
3. **Degree and level.** Use the $B$-bit representatives $(D,L_\sigma)=(-1,0)$ and $H=(-3,-1)$. Then $D_{\mathcal P}=-7$, $L_\sigma=-1$, and the shift is $L_\sigma-D/8=-\tfrac18$ [V, arithmetic]. The two bits of each $B$ have periodicity-equivalent $(D,L)$, so DLME's Lemma `inhomog-ineq` absorbs the sum.
4. **Monotonicity.** M$_{\rm block}$ makes $\mathcal P$ an IP-morphism $F^u_\bullet I(Y_2,t)\to F^u_\bullet I(Y_2,t'')$. Replace $\mathcal P$ by $\mathcal P^2$ if $t''\ne t$ (§1.1).
5. **Contradiction.** DLME Lemma `kappa-ineq`(b) gives $\ell_t(Y_2)\le\ell_t(Y_2)-\tfrac18$ (or $-\tfrac14$ after squaring). Lemma 3 says $\ell_t(Y_2)$ is finite as soon as $I(Y_2;\mathbb Q)\ne0$. ∎

**Nonvanishing without caps [P†].** The Floer form needs only $I(Y_2;\mathbb Q)\ne0$. It needs **no caps (Sec. 4) and no repetition**.
- Kronheimer–Mrowka (*Witten's conjecture and property P*†) give $I^w(Y_0;\mathbb C)\ne0$ for nontrivial $K$.
- $f_+:I^w(Y_0)\to I(Y_2)$ is integral and a mod-2 quasi-isomorphism, so it is an isomorphism over $\mathbb Z_{(2)}$.
- Hence $\mathrm{rank}_{\mathbb Q}I(Y_2)\ne0$.

This matters because Euler-characteristic arguments cannot help here: DLME force $\Delta_K=1$.

**What must be constructed, with gap ratings.** E = exists; R = routine extension; M = moderate new work; H = hard or genuinely new; F = I see a concrete risk of failure.

| # | Item | Existing input (†) | Rating |
|---|---|---|---|
| C1a | 3D PU(2) functional; $S^1$-equivariant holonomy perturbations; nondegeneracy | KM cylinder functions; Teleman and FL PU(2) transversality | R–M |
| C1b | Compactness of PU(2) trajectories on cylinders: Uhlenbeck bubbling, $C^0$ bound on $\Psi$ | FL-I (closed); Floer/Donaldson cylinder analysis; net bubble cost 2 (§1.3) | M |
| C1c | Blow-up along $\{\Psi=0\}=\mathcal B^{\rm inst}$, which carries its own flow; boundary-obstructed gluing; $\check/\hat/\bar$ | KM book, Ch. 19–25 (for SW), where the base is finite-dimensional mod gauge | **H** |
| C1d | The $\theta$-sector (stabilizer $U(2)$, where the A and S sectors meet) and the S points (a second blow-up) | DME framing for $\theta$ in the instanton theory; FL links of SW strata (closed) | **H** |
| C2 | Family maps with psc faces; lens cancellation; the $J$-defect through $\check I^{\rm PU}(S^3)$ | DLME/CDX family maps; manuscript `gluing:signs`; MMR/Donaldson psc necks | R given C1, but gluing at $U(2)$-stabilized R points is M |
| C3a | Conj. L(a): finitely many P and S points, so the free part is $u$-torsion | 3D Weitzenböck + Uhlenbeck | R given C1 |
| C3b | Conj. L(b): $\bar I^{\rm PU}$ = coupled instanton complex; identification $u=T$ | KM coupled Morse theory (Ch. 33–35†); Lemma 2 (bookkeeping, V) | M |
| C3c | Conj. L(c): localized cobordism map $=u^{L_\sigma}W_*$ + coupled terms + R/S entries | closed link: Prop. `analysis:instanton-link` (elementary); FL/PT (closed); with Floer ends it is boundary-obstructed gluing at instanton strata | **H** |
| C4 | (G): coupled terms $\bar\partial_{(2k+1)}$, $k\ge1$, compatible with the lattice | none | **H/F**: may genuinely change $\bar I_A$ |
| C5 | M$_{\rm block}$: (RD) per block, with Floer ends | closed analogue in Secs. 7–8 (itself unverified; D-families) | **H/F** (see below) |
| C6 | Coefficients $\mathbb Q$; injectivity | `stack:finite-lattice` | E |
| C7 | $I(Y_2;\mathbb Q)\ne0$ | KM + $f_+$ (above) | E/R |

**Why C5 is the likeliest failure point.**
- The closed exclusion kills end components using *cap geometry*: Lemma `indices:end-exclusion`, generic cap periods, $C_W$ bounds, and a large odd $\Lambda(E_{\rm exc})$.
- In the Floer form, the corresponding inputs are arbitrary elements of $L_t(Y_2)$, including its R and S sectors ($\theta,\theta'$ and 3D SW points on $Y_{\pm2}$). None of these has any geometric control.
- Adding more $B$'s adds more $J$-defects. These are suppressed only through the sphere tests: an R-mediated term pays roughly $\langle v,S\rangle$ per test it passes (D-families §5; [P]).
- A term that enters R at one seam and leaves at the next passes only $O(1)$ tests. Its $u$-order gain is $O(1)$, and that need not exceed the fixed width of $L_t$.
- One can apply Prop. 5 to $\mathcal P^N$ instead of $\mathcal P$, but that reproduces the closed problem with the caps replaced by uncontrolled lattice inputs.

**Why C1c, C1d and C3c are hard.** In KM the base of the blow-up is a finite-dimensional torus modulo gauge. Here it is a full Floer theory with bubbling. Gluing free PU(2) trajectories to *broken instanton trajectories* inside the boundary is a two-level, boundary-obstructed Morse–Bott gluing. To my knowledge it has no precedent in either the instanton or the monopole literature.

## 4. Literature comparison (from memory; every entry †)

| Work | What it does | Relation to this design |
|---|---|---|
| Pidstrigach–Tyurin, *Localisation of Donaldson invariants along SW classes* (preprint, c. 1995) | Introduce spin$^u$/SO(3)-monopoles and the $S^1$-cobordism between instanton and SW strata | Closed template: instanton links $\mathbb{CP}^{n_D-1}$; SW strata as other fixed components |
| Okonek–Teleman, *Quaternionic monopoles* (CMP, c. 1996), and Kähler-surface computations; Teleman, *Moduli spaces of PU(2)-monopoles* (Asian J. Math., c. 2000) | Equations; algebro-geometric description on Kähler surfaces; transversality, compactification | Perturbations (C1a); a Kähler model for the positive cells (the toric metrics of Sec. 6 point in this direction) |
| Feehan–Leness, *PU(2) monopoles I, II*, *links of top-level SW moduli*, gluing preprints *III, IV*; *SO(3)-monopole cobordism formula* (Mem. AMS, c. 2018); *Witten's conjecture for many 4-manifolds of simple type* (JEMS, c. 2015); later virtual Morse–Bott work | Closed Uhlenbeck compactness and transversality; links of reducible strata at all levels; the cobordism formula $D=\sum SW\cdot f$. As I recall, the general case rests on a gluing theorem whose complete proof was not published | Supplies the closed analysis behind C1b and C3c. Nothing for cylindrical ends or Floer theory. The manuscript avoids FL's hard part (gluing at reducibles) by emptying the reducible window |
| Kronheimer–Mrowka, *Monopoles and Three-Manifolds* (CUP 2007) | Blow-up; $\check/\hat/\bar$; boundary-obstructed gluing; Frøyshov invariant from towers; coupled Morse theory for $b_1>0$ | **The formal template for §1.3.** Our A-sector replaces their reducible torus by the instanton complex |
| KM, *Knot homology groups from instantons* (J. Topol., c. 2011) | $I^\sharp$, $I^\natural$, sutured instanton homology via admissible SO(3) bundles; conjecture $I^\sharp(Y)\cong\widehat{HF}(Y)$ (or $\widetilde{HM}$), still open as far as I know | An $S^1$-equivariant PU(2) Floer theory is the natural machine for that conjecture. This calibrates the gap: our theory is at least as hard as the missing tool for a famous open problem |
| KM, *Embedded surfaces and the structure of Donaldson's polynomial invariants* (JDG 1995); *Witten's conjecture and property P* (G&T 2004) | Structure theorem; nonvanishing of $I^w(Y_0)$ for nontrivial $K$ | C7 (§3); caps (Sec. 4) |
| PU(2)/SO(3)-monopole Floer homology | **I know of none.** It is mentioned as desirable (KM program; Feehan–Leness), but I know of no construction. Kronheimer's PU($N$)-monopoles (*Four-manifold invariants from higher-rank bundles*, JDG c. 2005) are closed only | The gap is the whole theory |
| Daemi–Miller Eismeier, *Instantons and rational homology spheres* (arXiv, c. 2022); Miller Eismeier's thesis (*Equivariant instanton homology*) | SO(3)-equivariant framed instanton complexes for rational homology spheres with reducibles; obstructed irreducible–reducible gluing; Frøyshov-type invariants | **Closest existing construction to the $\Psi=0$ sector, including $\theta$ (C1d).** No spinors, no $S^1$ phase |
| Frøyshov, *Equivariant aspects of Yang–Mills Floer theory* (Topology 2002), and the monopole $h$ for rational homology spheres (Duke 2010); Daemi, $\Gamma_Y$ (Duke 2020); Nozaki–Sato–Taniguchi, $r_s$ | Tower invariants and CS-filtered refinements | §2.2: $\ell_t$ is a tower invariant of the same kind, attached to irreducibles |
| Austin–Braam, *Equivariant Floer theory and gluing Donaldson polynomials* (Topology 1996) | $S^1$/SO(3)-equivariant Morse–Bott instanton Floer chain models over $\mathbb Q[u]$ | A chain-level Borel model for the S points (C1d) and for the coupled terms (C4) |
| Seidel–Smith, *Localization for involutions in Floer cohomology* (GAFA 2010); Hendricks (rank inequalities for branched double covers); Lipshitz–Treumann (JEMS 2016); Hendricks–Lipshitz–Sarkar, *flexible* and *simplicial* equivariant Floer; Large | $\mathbb Z/2$-localization: Borel Floer homology $\otimes\,\mathbb F_2[\theta^{\pm1}]\cong$ Floer homology of the fixed set, under stable normal triviality; Smith-type rank inequalities | The conceptual model for Conj. L. These results are $\mathbb Z/2$ and symplectic. In gauge theory, the $S^1$ analogue *is* KM's $\bar{HM}$. **[S]** Conj. L would give a Smith-type inequality $\dim I(Y)+\dim(\text{R/S sectors})\le\dim I^{\rm PU}_{\rm non\text{-}eq}(Y)$ |
| Hendricks–Manolescu (involutive); Manolescu (Pin(2) SWF, JAMS 2016); Lin (Pin(2)-monopole Floer); Stoffregen | Extra symmetry → several tower numbers | §2.2, last bullet |
| Bauer–Furuta (Invent. 2004); Manolescu's SWF spectrum (G&T 2003) | Finite-dimensional approximation; genuine equivariant localization (tom Dieck/Borel) | **Not available for PU(2):** Uhlenbeck bubbling destroys the global a priori bounds that Conley-index methods need [P]. So no spectrum-level shortcut exists for Conj. L |
| Morgan–Mrowka–Ruberman, $L^2$ moduli and a vanishing theorem (1994); Donaldson, *Floer homology groups in Yang–Mills theory* (CUP 2002) | Gluing along psc / reducible necks | The psc faces in C2 |
| Labastida–Mariño; Moore–Witten (u-plane, 1997) (physics) | Non-abelian monopoles; $u$-plane interpolation | Heuristics only |

**Closest existing construction.** KM's book is the formal template, DME supplies the $\theta$-sector, and FL supplies the closed analysis. No single work comes near the combination.

**Size of the gap.** The required work is monograph-scale: C1c, C1d and C3c are each comparable to major chapters of KM's book. On top of that, C4 and C5 are research-level conjectures with concrete failure modes. By contrast, the manuscript's closed route needs only C2-type family analysis on closed manifolds and finite necks, plus the closed budget (Secs. 6–10). That is still long and partly new, but it is an order of magnitude smaller.

## 5. The cheap alternative: the closed-form $\ell$-argument

**Lemma C (closed-form $\ell$-argument) [V].** Let $V$ be a free abelian group of finite rank $r\ge1$. Let $F\in\mathrm{End}_{\mathbb Z}(V)$, $x\in V$ and $y\in\mathrm{Hom}(V,\mathbb Z)$. Suppose:
- **(a) Unit and pairing.** $F\otimes\mathbb F_2$ is invertible, and $y(x)\ne0$.
- **(b) Closed vanishing along a progression.** There are $E_0\ge1$, rationals $n_0$ and $\delta>0$, and exponents $e(N)\ge0$ with the following property. For every $N\in E_0\mathbb Z_{>0}$ with $n_D(N):=n_0+\delta N\ge1$, we have $2^{e(N)}\,y(F^Nx)=0$.

Then (a) and (b) are incompatible.

*Proof.*
1. Choose $\nu$ with $2^\nu\nmid y(x)$.
2. $\det F$ is odd, so $F\bmod 2^\nu\in GL_r(\mathbb Z/2^\nu)$. Let $\varepsilon$ be the exponent of this finite group.
3. For $N\in\mathrm{lcm}(E_0,\varepsilon)\mathbb Z_{>0}$ we have $F^N\equiv1\pmod{2^\nu}$, so $y(F^Nx)\equiv y(x)\not\equiv0\pmod{2^\nu}$.
4. Hence $2^{e}y(F^Nx)\ne0$ in $\mathbb Z$. But $n_D(N)\ge1$ once $N$ is large, contradicting (b). ∎

**This is the precise abstract replacement for DLME's Lemmas `kappa-ineq`(b) and `kappa-basic`(c).**

| DLME | Lemma C |
|---|---|
| injective IP-endomorphism over a field | mod-2 unit over $\mathbb Z$ (via $GL_r(\mathbb Z/2^\nu)$) |
| $\ell$ finite, because $A\neq0$ | $y(x)\ne0$ |
| filtered of negative shift | closed vanishing once the accumulated shift exceeds the gap ($n_D(N)\ge1$) |
| one application suffices (the module is compared with itself) | $N\to\infty$ along a progression (caps compared through the iterate) |
| works over $\mathbb F_2$ | needs $\mathbb Z$, because the closed output is $2^{n_D-1}\Omega=0$ |

The manuscript is an instance of Lemma C:
- $V=I(Y_2;\mathbb Z)/\mathrm{Tor}$ and $F=\mathcal P=\mathcal A^3\mathcal D$;
- $x,y$ are the cap cycle and cocycle, with the pads absorbed: pad lengths are multiples of $\varepsilon$, so the pads are $\equiv1\pmod{2^\nu}$;
- $E_0=8$, so that $c_2$ is integral;
- $\delta=\tfrac18$ per period;
- (b) is Thm. `gluing:contradiction` together with `stack:composition`, i.e. $\Omega_N=\pm y(F^Nx)$.

**Lemma C′ (Floer monotonicity implies (b)) [V, formal].**
- *Setting.* Let $A_\bullet$ be an IP-module over $\mathbb Q$, and $F$ an IP-endomorphism of degree $D$ and level $L$, with $L-D/8=-\delta<0$. Take $x\in F_aA_d$. Let $y:A_{d'}\to\mathbb Q$, and let $b$ be the infimum of the levels $r$ with $y|_{F_rA_{d'}}\ne0$.
- *Conclusion.* If $d+ND\equiv d'$ (up to periodicity) and $(a-\tfrac d8)-N\delta<(b-\tfrac{d'}8)$, then $y(F^Nx)=0$.
- *Proof.* $F^Nx\in F_{a+NL}A_{d+ND}$. Moving to degree $d'$ by periodicity gives level $a+NL+(d'-d-ND)/8$, which is $<b$. ∎
- *Dictionary.* Take $x=C_-(1)$ and $y=C_+$. Lemma 1 telescopes the $\sigma$'s across seams, and $L_\sigma$ is additive. Then the inequality is exactly $n_D(N)=\sum_{\rm pieces}(\Theta+c^2/4)\ge1$ for the dimension-0 closed count. In particular, "$n_D\ge1$" is "the levels have crossed". This matches §1.6: $\Omega\in\mathrm{Hom}(F_0(\emptyset),F_{-n_D}(\emptyset))=0$.

**Consequence (the key comparison) [V as logic].** Hypothesis (b) of Lemma C is Floer monotonicity *only for the capped closed composites* $C_+\circ F^N\circ C_-$. Equivalently, it is (RD) with the R/S end sectors replaced by the caps.
- The caps carry exactly the geometric control that the Floer-end sectors lack: $b^+>0$, generic periods, the $C_W$ bounds, and $\Lambda(E_{\rm exc})$.
- So the closed route avoids C1, C3 and C4 entirely, and replaces C5 (the likeliest failure point) by a statement for which the needed control exists.
- The price is twofold. First, constants must be uniform in $N$: the manuscript's order of choices, Table `stack:choices`, is designed for this. Second, the caps of Sec. 4 are needed, whereas the Floer form would need only $I(Y_2;\mathbb Q)\ne0$.

## 6. Verdict and confidence

1. **The spin-filtered DLME picture is coherent. Confidence about 80%** (normalization constants unchecked). Six independent consistency checks pass:
   - $\sigma_t$ is an integer grading whose quantum is the period shift $\tfrac18$ (Lemma 1);
   - the localized exponent reproduces $L_\sigma=-c^2/4-\Theta$ exactly (§1.6);
   - the closed template reproduces $2^{n_D-1}\Omega=0$ (§1.6);
   - the per-map failure ($HB\simeq{\rm id}$) is explained by the $J$-defect through $\check I^{\rm PU}(S^3)$, consistent with "R only at $J$-faces" (§2.4);
   - $k=4$ is the unique admissible block length, matching the window $\tfrac15<m/n\le\tfrac14$ (§2.5);
   - closed vanishing is exactly Floer monotonicity for capped composites (Lemma C′).
2. **A Floer-theoretic proof (§3) is implausible as a near-term rigorous route. Confidence about 85%.**
   - The gap is monograph-scale: C1c, C1d and C3c are new two-level boundary-obstructed gluing problems, with no Bauer–Furuta shortcut.
   - The theory is at least as hard as the missing tool for KM's $I^\sharp\cong\widetilde{HM}$ conjecture.
   - The probability that M$_{\rm block}$ holds *as stated* (per block, for arbitrary lattice inputs) is about 25–35%. The obstruction is the uncontrolled R/S sectors of $Y_{\pm2}$ at Floer ends.
3. **A proof in spin-filtered DLME *style* is plausible in closed form.** The architecture is Lemma C, plus Theorem V (closed family PU(2) vanishing, D-families §1.2), plus the window budget. This is the manuscript's architecture.
   - Logical soundness of the architecture, given its lemmas: about 75%.
   - Correctness of the lemmas themselves is not assessed here. Per threads C and D, the risk is concentrated in the mixed projection (`analysis:projection`), the zero-winding test, and the uniformity of the clamp.
4. **Recommended presentation.**
   - (i) IP-modules with $\sigma_t$ as an integer second grading (Lemma 1, Def. 2.1).
   - (ii) The equivariant PU(2) theory, stated as Conjectures L and M$_{\rm block}$, to explain where monotonicity comes from and why it holds only for blocks.
   - (iii) The proof itself via Lemma C, with hypothesis (b) supplied by the closed family vanishing theorem.
   - (iv) The sanity test of classical.tex §6: no $\Theta=0$ negative-definite mod-2-unit $V:Y_{-2}\to Y_2$.

**Weak points of this note.**
- The APS normalization of $\rho_t$ is unchecked; only differences are used.
- The identification of the tower split with $\sigma_t$ is [P].
- The $\check/\hat$ direction conventions are †.
- (G) may fail: the coupled terms could change $\bar I_A$.
- The S points need a second blow-up whose Floer theory I have not designed.
