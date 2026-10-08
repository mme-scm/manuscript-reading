# The faces of the cube: limits of $\mathrm{SO}(3)$-monopoles over $\partial Q$ for $X(\Pi_M)$ — referee's final report

*Round 4. This report replaces `round4/faces-1.md` (cited as [F]) as the record for the faces of the cube. I re-derived every index, energy and orientation statement of [F], checked its citations against the LaTeX sources, and looked for limits it missed. The substance of [F] stands. The corrections concern the form of the coupled transversality hypothesis, the thresholds at which it is needed, the treatment of corners with abelian components, the role of the spinor in the orientation comparison, and several smaller points (§7). My computations are in `round4/faces-final-checks/`; the report of the checks is §10.*

**Labels.** **VERIFIED**: proved here; or read in the source named, with the statement or equation number recomputed from its LaTeX counters; or confirmed by an exact computation listed in §10. **PLAUSIBLE**: standard in kind, or supported by an argument whose structure I checked but whose analysis I did not carry out. **SPECULATIVE**: unproved, or a guess.

**Sources.** [S] `statements.tex` (Theorem 1.1, Lemma 3.2, Theorems 4.1, 4.3, Proposition 4.2, (H1)–(H5), "The hardest open point"). [St] `strategy.tex`, Theorem 2.1. [R] `notes/R3-sources/relation-final.md` ((A1)–(A7), (B1)–(B5), Lemmas 1.2, 1.3, 4.3–4.6, Proposition 4.2, §3.4). [G] `gluing-final.md` (Lemmas 1.1, 4.1–4.5, data (D1)–(D8)). [B] `B-final.md` (Lemmas 1.2, 2.2–2.5). T2 = `notes/T2-mu-classes.md` (Propositions 2.3, 3.2, Example 3.5, Lemma 5.1). [C] `round4/compactness-final.md` (Proposition C, (D4′), (H5′), Lemma G). [Mx] `round4/mixed-2.md` (Propositions 2.1–2.6, 3.1, 3.2, Theorem 3.3, (A3′)). [MS] the manuscript, `src/08-indices.tex`, `09-analysis.tex`, `10-gluing.tex`, cited by the titles of its statements. FL1 = dg-ga/9710032; FL2a = math/0007190; FL2b = dg-ga/9712005; Memoir = math/0203047 (all in `lit/`).

**Notation (Feehan–Leness).** $X=X(\Pi_M)$, closed, $H_1(X;\mathbb Z)=0$, with three-spheres $J_1,\dots,J_n$ and spheres $S_i$, $S_i\cdot S_i=-4$, $[S_i]=F_{l,i}-F_{r,i}$, $\nu_i=\nu S_i$, $\partial\nu_i\cong L(4,1)$. For $e\in\{0,1\}^n$ the spin$^u$ structure $\mathfrak t_e$ has $w_e=w_0+\sum_ie_i\,\mathrm{PD}[S_i]$, $\Lambda_e=c_1(\mathfrak t_e)$, $\langle\Lambda_e,S_i\rangle=2-4e_i$, $p_1(\mathfrak t_e)=-4\kappa$, $d_a=8\kappa-3(1+b^+)$, $n_a=\Theta-\kappa$, $\Theta=\frac14(\Lambda^2-\sigma)$. The class $z=\mu(S_1)\cdots\mu(S_n)z_C$ has $\deg z=d_a+n$ and is represented by $\mathcal V(z)$ (jumping-line divisors $V_{S_i}$ and cap representatives); $\mu_c$ is represented by $n_a-1$ sections of $\mathbb L_{\mathfrak t}$ that sample the spinor on every piece ([R] §1.3), called the $\mu_c$-sections. Then
$$\mathcal Z_e=\mathcal V(z)\cap\mathcal W^{n_a-1}\cap\mathcal M^{*,0}_{\mathfrak t_e}(Q)/S^1,\qquad\dim\mathcal Z_e=1,\qquad \Omega=\sum_e\epsilon(e)\,\#\big(\bar{\mathcal V}(z)\cap\bar M^{w_e}_\kappa(Q)\big),\quad \epsilon(e)=\textstyle\prod_i(-\epsilon)^{e_i}.$$
The link of the instanton stratum is $\{\|\Phi\|^2_{L^2}=\varepsilon_0\}$. The faces $\{t_i=-1\}$ stretch $J_i$ (round), the faces $\{t_i=+1\}$ stretch $\partial\nu_i$ (positive scalar curvature). The necks along $Y_{\pm2}$ have the fixed length $R$ required by the composition law; they are not faces.

A face $F(\mathcal J,\mathcal N)$ breaks $k=|\mathcal J|$ three-spheres and $l=|\mathcal N|$ lens spaces. Its main pieces $\hat\Gamma_0,\dots,\hat\Gamma_k$ are closed up by balls at the $J$-ends; $\hat\Gamma_0\supset C_-$ and $\hat\Gamma_k\supset C_+$. By the proof of FL2a Proposition 3.1, which is local to a component, the main component on a piece is an **$\mathcal M^{*,0}$-component** ($A$ irreducible, $\Phi\not\equiv0$), an **anti-self-dual component** ($A$ irreducible and anti-self-dual, $\Phi\equiv0$), a **Seiberg–Witten component** (a point of $\iota(M_{\mathfrak s})\times\mathrm{Sym}^\ell$ of the piece) or an **abelian component** (reducible, $\Phi\equiv0$). For a main component, $q_j=d_a(\hat\Gamma_j)+p_j-2s_j-z_j$ is its cut-down anti-self-dual index and $i_j=q_j+2n_a(\hat\Gamma_j)$ its monopole index, with lens ends filled ([R] Lemma 1.3). A *chain of reducible components* is a maximal set of consecutive main components that are all reducible; for such a chain $\Gamma$ put $\delta(\Gamma)=\sum_{j\in\Gamma}(i_j+4)$ (the quantity [R] §3.1 calls $\epsilon_S$).

---

## 0. Findings

1. **Bookkeeping** (VERIFIED). The identities (I) $\sum_j(q_j+4)=4-\sum_\tau(8c_\tau-2\delta_\tau)-\sum_\nu(\delta_I(\nu)-1)-\sum_\beta(8a_\beta-d_\beta)$ and (M) $\sum_ji_j-2(n_a-1)=2-4k-\sum_\tau(6c_\tau-2\delta_\tau)-\sum_\nu(\delta_{\rm sp}(\nu)-1)-\sum_\beta(6a_\beta-d_\beta)$ of [F] Lemma 1.1 are correct; I re-derived them from index additivity piece by piece and checked them on 20,000 random configurations (ff1). A broken three-sphere costs $3+1$, a lens end $\delta-1$, a trajectory $8c-2\delta$ resp. $6c-2\delta$, a point of concentration $8a-d$ resp. $6a-d$.
2. **The valid count is the dimension of the $\mathcal M^{*,0}$-factor** (VERIFIED as logic). The $\mu_c$-sections vanish at anti-self-dual, Seiberg–Witten and abelian components ([F] Lemma 1.2), so with perturbations local to components a limit lies in (the $\mathcal M^{*,0}$-components cut down by everything, modulo the diagonal circle) $\times$ (the other components), and the first factor has dimension
$$D_F=1-4k-\textstyle\sum_\tau(6c_\tau-2\delta_\tau)-\sum_\nu(\delta_{\rm sp}(\nu)-1)-\sum_\beta(6a_\beta-d_\beta)+\sum_{\beta\text{ on }F}\pi_\beta-\sum_{j\notin F}i_j$$
   (actual indices $i_j$ of the components, lens ends unframed; [F] Corollary 1.3(a)).
   [F]'s second count $D_C=1-4k-4t-\dots$ ("all components regular together") is **not attainable**: a trajectory of charge $c$ on a $J$-neck has Dirac index $-c$ and zero kernel, on a neck where every perturbation vanishes, and a central cap of energy $E\ge1$ has a Dirac cokernel of dimension $E$. $D_C$ must be replaced by $D_F$ together with a condition imposed on anti-self-dual components only (item 5). This changes the hypothesis, not the conclusions.
3. **Three-spheres** (VERIFIED). On $S^3$ with positive scalar curvature the only three-dimensional critical point is $(\theta,0)$ (quartic identity $\langle(\Phi\Phi^*)_{00}\Phi,\Phi\rangle=|\Phi|^4(\frac14+\frac12\sin^22t)\ge\frac14|\Phi|^4$, re-checked on $2\cdot10^5$ samples, ff6); trajectories are anti-self-dual with zero spinor, index $8c-3$, Dirac index $-c$. The nodal lemma ([S] Lemma 3.2, [G] Lemma 4.2) holds verbatim on the monopole side; with a trajectory the degenerate curve is a chain of three spheres, and the limiting operator is invertible iff every component's normalized bundle is trivial (checked for chains of up to four components, all splitting types $\le3$, every twist position, 1,252 cases, ff4).
4. **Faces $\{t_i=-1\}$** (VERIFIED counts). Pairs $(\mathcal M^{*,0},\mathcal M^{*,0})$: $D_F=-3$. $(\mathcal M^{*,0}$, anti-self-dual$)$: $D_F=-3-i_r$, excluded by counting iff $i_r\ge-2$. $(\mathcal M^{*,0}$, Seiberg–Witten cap component$)$: $i_r\ge\lambda^2-O(\lambda)$, excluded by counting (given [R] Lemma 4.6); **no coupled perturbation is needed at Seiberg–Witten components**, contrary to [F] rows 3 and 8. Zero-spinor limits: excluded by (I). Abelian components: excluded by the caps.
5. **Where counting fails, and the hypothesis needed** (VERIFIED counts; hypothesis PLAUSIBLE, new). Counting excludes every limit with an $\mathcal M^{*,0}$-component and $k\ge1$ unless it contains an anti-self-dual component **of low index**: $i\le-3$ on a piece without a cap, or $i\le-3$ on a cap piece at $k=1$, or $i\le-1$ on a cap piece at $k\ge2$ (exhaustive, ff8). [F] Proposition 2.5 says two-valued perturbations are needed only at index $\le-3$; a cap component of index $-1$ next to an isolated positive piece carrying a Seiberg–Witten component of charge $\frac12$ has $D_F=0$, so the threshold at cap pieces is $-1$ at corners. Low-index components occur only in two end regions fixed before $M$: within about $8\lambda_\pm^2+5p'+O(1)$ copies of $W_B$ of a cap, or on unions containing five or more consecutive negative pieces (ff2). There one needs the two-valued coupled perturbation (A3′) of [Mx]: it imposes on the low-index component the vanishing of a section of its Dirac cokernel bundle, of rank $-2n_a(\hat\Gamma)>q$, so that component's factor becomes empty. Single-valued perturbations cannot do this ([F] Proposition 2.6, re-checked).
6. **Corners** (VERIFIED as deduction). With an $\mathcal M^{*,0}$-component and no low-index component, $D_F\le-1$ at every $k\ge1$, abelian components included, by counting alone ([Mx] Theorem 3.3, re-derived, ff8). So the necessary projection (A7) and "the problem obtained by forgetting the abelian instantons" of [S] (H5) are **not needed**; [F] Proposition 4.1(c) still used them. Without an $\mathcal M^{*,0}$-component, (I) is contradicted.
7. **Lens space and cap** (VERIFIED). Flats on $L(4,1)$: $\theta,-\theta$ (stabilizer $\mathrm{SU}(2)$), $\gamma=\mathrm{diag}(i,-i)$ (stabilizer $\mathrm U(1)$), all with $H^1=0$ and invertible Dirac operator. The psc cap metric $dr^2+A^2(\sigma_1^2+\sigma_2^2)+B^2\tanh^2(4r/B)\sigma_3^2$, $B<2A$, has scalar curvature $64B^{-2}\mathrm{sech}^2(4r/B)+8A^{-2}-2B^2\tanh^2(4r/B)A^{-4}>0$: recomputed from the Christoffel symbols in Euler coordinates (ff5), not from a warped-product formula.
8. **Reducibles on $\nu S_i$** (VERIFIED). $v=2m\xi$, $E=m^2/4$, $\delta_I=8E$ (two derivations), Dirac index $-E$ at a central limit and $\frac14-E$ at $\gamma$ (two derivations: excision against $\mathbb F_4$ and $\mathbb P(1,1,4)$, and the $\eta$-sum over the four spin$^c$ structures of $L(4,1)$ with integrality fixing $\eta_{\rm sign}=-\frac12$), $\delta_{\rm sp}=6E$ resp. $2+6(E-\frac14)$; read on the common exterior bundle, $\theta$ and $-\theta$ swap between the lifts $e_i=0,1$ (ff3).
9. **Lens faces** (VERIFIED counts). The only limits over $\{t_i=+1\}$ are (rigid $\mathcal M^{*,0}$-solution on $X\setminus\nu_i$ with limit $\gamma$) $\times$ (reducible of energy $\frac14$), dimension $0$. Other caps give $-6h$ or $\le-4$; anti-self-dual exteriors $-1$; Seiberg–Witten exteriors are excluded by energy ((B3)), abelian ones by the caps. No coupling is needed there.
10. **Cancellation with the sign $\epsilon$ of [S] Theorem 1.1** (VERIFIED as a deduction from excision and (H4); gluing PLAUSIBLE). The ends of $\mathcal Z_e$ and $\mathcal Z_{e+e_i}$ over the same exterior solution have signs in the ratio $\epsilon$, so they cancel in $\sum_e\epsilon(e)$. No line bundle on $X$ relates $E_e$ and $E_{e+e_i}$ (tensoring never changes $w_2$ of the adjoint bundle, and $w_{e+e_i}-w_e=\mathrm{PD}[S_i]\not\equiv0$); the transport is the local cap operation, the restriction to $\nu S$ of $\otimes L_y$ on $W_B$ followed by a Weyl conjugation at $\gamma$. **Correction to [F] and to [MS]:** this operation does not act on spinors (it changes the spin$^c$ structures of the two summands, evaluations $(4,0)\mapsto(0,-4)$). The spinor contributes $+1$ for a different reason: both cap Dirac operators are invertible, the exterior Dirac operator is common, and excision preserves complex orientations.
11. **Missed limits.** I found no limit configuration that defeats the argument beyond the low-index anti-self-dual components of item 5. Fifteen attempted configurations are recorded in §6.
12. **Verdict.** Given (H4) and the corrected (H5) of §7, the faces contribute to Stokes' theorem only the lens ends, and these cancel in $\sum_e\epsilon(e)$ with exactly the sign $\epsilon$ of [S] Theorem 1.1; nothing occurs over three-sphere faces or corners. The only new analytic input at the faces is (A3′) in the end regions. Confidence: arithmetic 97%; lens cancellation 75%; three-sphere faces and corners about 55%; the face statement as a whole **about 50%** (40–55%).

---

## 1. Bookkeeping at a face

### 1.1 The two identities

Index additivity across $S^3$ and $L(4,1)$, with fixed-limit unframed indices on the pieces and $h^0$ added at each matching, gives [F]'s identities (I) and (M) (item 1 of §0). The ingredients:
- each broken $J$ adds $h^0(\theta)=3$ and removes one parameter;
- a cap of framed index $\delta_I$ (anti-self-dual) or $\delta_{\rm sp}=\delta_I+2\,\mathrm{ind}_{\mathbb C}D$ (monopole) carries $V_{S_i}$ and removes $t_i$, so it costs $\delta-1$;
- a trajectory has anti-self-dual index $8c-3$ (with translations), Dirac index $-c$, and adds one matching and one length;
- a point of concentration of charge $a$ lowers $d_a$ of the background by $8a$, raises its Dirac index by $a$, releases conditions of degree $d_\beta$ and has $\pi_\beta$ position parameters, with $d_\beta+\pi_\beta\le4$ (FL2b (3.25), extended to the supports of [R] §1.3).

Complex Dirac indices add without correction because the coupled Dirac operators of $S^3$ and $L(4,1)$ with positive scalar curvature and flat twisting are invertible. **VERIFIED** (algebra, ff1); additivity itself is **PLAUSIBLE**, standard (Atiyah–Patodi–Singer).

### 1.2 The $\mathcal M^{*,0}$-factor

**Lemma 1.1** ([F] Lemma 1.2). A gauge-invariant function $f$ on configurations of a piece with $f(\zeta x)=\zeta^2f(x)$ vanishes at anti-self-dual, Seiberg–Witten and abelian components. *Proof.* At $(A,0)$ every scalar fixes the configuration. At $(A_{L_1}\oplus A_{L_2},\Phi)$, $\Phi\in\Gamma(W^+\otimes L_1)$, the determinant-one element $\mathrm{diag}(z,z^{-1})$ fixes $A$ and multiplies $\Phi$ by $z$, so $f=z^2f$ for all $z$. ∎ **VERIFIED.**

**Proposition 1.2** (the valid count). Suppose the perturbations near a limit are local to its components (each term depends on the fields and the parameters of one piece; the metric family is local in the parameters, [MS] Theorem "The metric family" (i)). Let $F$ be the set of $\mathcal M^{*,0}$-components, $f=|F|\ge1$. Then the limit lies in $\mathcal Z_F\times\prod_{j\notin F}M_j$, where $\mathcal Z_F$ is the space of $\mathcal M^{*,0}$-components cut down by their insertions and all $n_a-1$ $\mu_c$-sections, modulo the diagonal circle, and
$$\dim\mathcal Z_F=D_F=5-4f-\textstyle\sum_{j\notin F}(i_j+4)-\lambda_F .$$
Here, as in [R] Lemma 1.3 and [MS] Lemma "virtual-sums", the indices $i_j$ ($j\notin F$) are computed with lens ends filled and with the charges of the caps, points of concentration and trajectories allocated to that component included; $\lambda_F\ge0$ is the loss on the $\mathcal M^{*,0}$-components: $\delta_{\rm sp}-1\ge1$ per lens end, $6c-2\delta\ge4$ per trajectory allocated to them, $6a-d-\pi\ge2a$ per point of concentration on them. If $\mathcal Z_F$ is regular and $D_F<0$, the limit does not exist, whatever the other factors are. **VERIFIED** as a deduction from (M); the regularity of $\mathcal Z_F$ is single-component regularity together with transversality of the $\mu_c$-sections on products, **PLAUSIBLE**, routine (each section is a sum over pieces, and its summands can be varied piece by piece).

The forgotten components enter only through their *expected* indices $i_j$, which are topological numbers bounded below by energy (reducible components) or by $q_j\ge0$ and integrality of $n_a$ (anti-self-dual components). Nothing is required of them analytically.

**Correction to [F] Corollary 1.3(b).** [F] adds to $D_F$ "the trajectories' own cut-down monopole indices" and obtains $D_C=1-4k-4t-\dots$, asserting this is the dimension of the stratum "when all components are made regular together". At a trajectory the Dirac operator on $\mathbb R\times S^3$ (conformally $S^4$ minus two points, $F^+=0$, $s>0$) has index $-c$ and zero kernel, so a cokernel of complex dimension $c$, on a neck where all perturbations vanish; at a cap with negative Dirac index (energy $E\ge1$ at a central limit, $E\ge\frac54$ at $\gamma$) the cokernel has dimension $E$ resp. $E-\frac14$. No perturbation reaches these cokernels, so the joint problem is never regular there. The manuscript avoids this by omitting the connecting fields and counting their charges as losses ([MS] Definition "analytic-hypotheses"(iii)); the resulting bound $1-4k-\sum_\tau(6c_\tau-2\delta_\tau)-\dots$ is stronger than [F]'s $1-4k-4t-\dots$, since $6c-2\delta\ge4$. So [F]'s conclusions survive, but the hypothesis must be stated as in §2.6. **VERIFIED.**

### 1.3 Isotropy

At a limit with an $\mathcal M^{*,0}$-component, modulo $(-1,\dots,-1;-1)$, the isotropy in $\prod_j\mathcal G_j\times S^1$ is $\prod_{\text{a.s.d.}}\{\pm1\}\times\prod_{\text{abelian}}\mathrm U(1)$ (or $\mathrm{SU}(2)$ for $v=0$); $\mathcal M^{*,0}$- and Seiberg–Witten components contribute nothing, the latter because its circle must compensate a phase in $\{\pm1\}$. Without an $\mathcal M^{*,0}$-component the isotropy contains a circle. ([F] Lemma 1.4, [Mx] Proposition 2.1.) **VERIFIED.**

On gluing data: the central element of an anti-self-dual component's gauge group acts on its gluing parameters by $\rho\mapsto-\rho$. So at a pair of $\mathcal M^{*,0}$-components the gluing parameter lies in $\mathrm{SU}(2)$, and at a pair ($\mathcal M^{*,0}$, anti-self-dual) in $\mathrm{SO}(3)$. [F] Lemma 2.2 says $\mathrm{SO}(3)$ in both cases; the dimension, 3, is unaffected. **VERIFIED.**

---

## 2. The faces $\{t_i=-1\}$

### 2.1 The three-sphere

On $(S^3,\text{round})$ with flat background and no perturbation on the neck, the three-dimensional $\mathrm{SO}(3)$-monopole equations have only $(\theta,0)$ as solution: integrating FL1 Lemma 4.1 (1b) (read: $D_A^*D_A=\nabla_A^*\nabla_A+\frac14R+\rho_+(F_A^+)+\frac12\rho_+(F^+_{A_L}+F^+_{A_e})$, with $F_{A_L}+F_{A_e}$ flat on the neck) gives $0=\|\nabla\Psi\|^2+\int\frac s4|\Psi|^2+\|(\Psi\Psi^*)_{00}\|^2$, so $\Psi=0$, then $F_B=0$ and $\pi_1(S^3)=1$. $\theta$ has stabilizer $\mathrm{SU}(2)$, $H^1=0$, and twisted Dirac spectrum $\pm(\frac32+k)$ of multiplicity $2(k+1)(k+2)$. Finite-energy solutions on $\mathbb R\times S^3$ have $\Phi=0$, are anti-self-dual, have integer charge $c$, unframed index $8c-3$ and Dirac index $-c$ with zero kernel. **VERIFIED** (ff6 for the quartic identity; the rest by hand). This is [F] Lemma 2.1.

### 2.2 The jumping-line divisor at the node

[S] Lemma 3.2 and [G] Lemma 4.2 hold verbatim for monopoles, because $V_{S_i}$ depends only on $A|_{S_i}$: if $[A_\nu,\Phi_\nu]$ with $[A_\nu]\in V_{S_i}$ converge over $\{t_i=-1\}$, then (i) $A_l\in V_{f_l}$, or (ii) $A_r\in V_{f_r}$, or (iii) a point of concentration lies on $S_i$, or (iv) a trajectory on the $J_i$-neck has a jumping line on the middle sphere $\mathbb R\times K$ of the degenerate curve. **VERIFIED** for the algebra (ff4: the kernel of the limiting operator on a chain of two, three or four rational curves vanishes for every gluing element iff every normalized bundle is trivial, and is nonzero for every gluing element otherwise); the linear gluing of Cauchy–Riemann operators across the neck is **PLAUSIBLE**, standard.

Requirements on the representatives (**PLAUSIBLE**, jointly 80–85%):
- **(D4′)** of [C]: the transversality term of $V_{S_i}$ is continuous for Uhlenbeck convergence whose points of concentration avoid $S_i$, and vanishes near reducible restrictions with $\langle v,S_i\rangle=0$. This replaces [F]'s (R1) ("support of dimension two"), which is sufficient but stronger than needed.
- Product form near $t_i=-1$ ([G] (D4); [F] (R2)): $\mathcal L_{S_i}\to\mathcal L_{f_l}\otimes\mathcal L_{f_r}$ and the perturbed section converges to a tensor product.
- Transversality of the face limits $V_{f_l}$, $V_{f_r}$ to the moduli spaces of $\mathcal M^{*,0}$- and anti-self-dual components on the completed halves (the monopole form of [G] (D5)).
- At $t_i=+1$: $\mathrm{Stab}(\gamma)$-equivariant near the minimal cap and identical for the two lifts; functions of $E|_{S_i}\otimes(\det E|_{S_i})^{-1/2}$ are unchanged by tensoring.

### 2.3 Codimension one: the strata and their counts

Take $k=1$, $l=0$; both pieces contain a cap.

| # | components on $(\hat\Gamma_l,\hat\Gamma_r)$ | count | handling | status |
|---|---|---|---|---|
| 1 | $\mathcal M^{*,0}$, $\mathcal M^{*,0}$ | $D_F=-3$ | excluded by dimension | count VERIFIED; regularity PLAUSIBLE |
| 2 | $\mathcal M^{*,0}$, anti-self-dual with $i_r\ge-2$ (or mirror) | $D_F=-3-i_r\le-1$ | excluded by dimension | VERIFIED |
| 3 | $\mathcal M^{*,0}$, anti-self-dual with $i_r\le-3$ | $D_F=-3-i_r\ge0$; with (A3′): $D_F+i_r=-3$ | **needs (A3′)** (§2.6); occurs only in the end regions | counts VERIFIED; (A3′) PLAUSIBLE, new |
| 4 | $\mathcal M^{*,0}$, Seiberg–Witten cap component | $i_r\ge\lambda_\pm^2-3B\lambda_\pm-O(1)$, so $D_F\ll0$ | excluded by dimension | VERIFIED given [R] Lemma 4.6 |
| 5 | anti-self-dual, anti-self-dual | (I): $q_l+q_r=-4$, $q\ge0$ | excluded | VERIFIED given single-component regularity |
| 6 | anti-self-dual and Seiberg–Witten, or two Seiberg–Witten | (I): $\sum(q_j+4)=4$, a Seiberg–Witten cap component has $q+4\ge8$ | excluded | VERIFIED given [R] Lemma 4.6(c) |
| 7 | any abelian component | — | impossible: both pieces contain a cap, $\langle w_e,A_\pm\rangle$ odd, generic periods ((B2)) | PLAUSIBLE (85%) |
| 8 | a trajectory of charge $c$ | $D_F$ lowered by $6c-2\delta\ge4$; (I) by $8c-2\delta\ge6$ | excluded by dimension, except next to a component of row 3 (then (A3′)) | VERIFIED |
| 9 | points of concentration of charge $a$ | $D_F$ lowered by $\ge2a$, (I) by $\ge4a$ | as row 8; needs (D4′) | VERIFIED |
| 10 | insertion lost at the node | requires (iii) or (iv) of §2.2 | rows 8–9 | VERIFIED |

Row 4 uses that a Seiberg–Witten component containing a blown-up cap has $|v\cdot E_\pm|\ge\lambda_\pm-B$ ([R] Lemma 4.6(b)), hence $6\kappa\ge\frac32(\lambda_\pm-B)^2$, while $2\Theta$ drops by only $\frac12(\lambda_\pm^2-1)$; the rest of the piece contributes nonnegatively by the family adjunction inequality ([R] Lemma 4.4). [F] rows 3 and 8 ask for "single-valued coupling at Seiberg–Witten components" when $i_r\le-3$; that case does not occur. **VERIFIED** given those inputs.

Rows 5–10 also give the exclusion part of (E0) over $\{t_i=-1\}$: no zero-spinor limit of the cut-down instanton spaces lies there. **VERIFIED** given single-component regularity.

### 2.4 Where the anti-self-dual index is low

For an anti-self-dual component on a closed-up union $\hat\Gamma$ of pieces put $Q=8\Theta(\hat\Gamma)-3(1+b^+(\hat\Gamma))+p-2s-z$. Then $q=Q-8n_a(\hat\Gamma)\ge0$ and $n_a(\hat\Gamma)\in\mathbb Z$, so
$$i=Q-6n_a(\hat\Gamma)\ \ge\ Q-6\lfloor Q/8\rfloor\ \ge\ Q/4 .$$
$\Theta$ is computed from the trace halves: $\Theta(\text{half})=\frac14-\frac18h^2$ with $h=\langle\Lambda,F\rangle\in\{0,\pm2\}$, $\Theta(W_B)=0$, $\Theta(W_H)=1$ ([C] Lemma G). For an inner union of $L$ pieces with $m$ positive ones, $Q=5m-L-2+8(\theta_a+\theta_b)-2(\epsilon_a+\epsilon_b)$ with $\theta_a,\theta_b=\pm\frac14$. My computation (ff2, independent of [F]'s `near_caps.py`):
- **Inner unions where positive pieces are four apart**, with up to three extra negative pieces at each end: least $i=-2$ (attained by one positive piece followed by two negative pieces, $\kappa=\frac32$); the same at spacing five with up to four extra pieces.
- **Stretches of $L$ negative pieces**: least $i=-1,-2,-1,-2,-3,-4,-3,-4,\dots$ for $L=1,2,\dots$; first $i\le-3$ at $L=5$; about $-L/4$ in general. So low index on a union without a cap requires five consecutive negative pieces.
- **Cap pieces.** For the piece containing a blown-up cap, $Q=5m_r-n_r-2\lambda^2\pm2-2\epsilon+C_0$, $C_0=8\Theta_C-1-3b^+_C-z_C$ (one trace half, so the end term is $\pm2$; [F] writes $4\Delta$, an immaterial difference). The farthest broken three-sphere at which $i\le-3$ can occur lies about $8\lambda^2+5p'-4C_0$ copies of $W_B$ from the cap, up to a bounded correction; for $i\le-1$, 32 copies farther. Sample values at $C_0=0$: $(\lambda,p')=(3,8)$: 87 and 119; $(5,16)$: 255 and 287; $(7,16)$: 447 and 479, against $8\lambda^2+5p'=112$, $280$, $472$.

Define the **end regions** as the pieces within these distances of $C_\pm$, enlarged to contain $B\Pi_0$ and $(\phi_*B)^{p'}$ (the only places with five or more consecutive negative pieces). They depend only on the caps, $\lambda_\pm$, $\deg z_C$, $\Pi_0$ and $p'$, all fixed before $M$. **VERIFIED** (arithmetic).

### 2.5 Thresholds, exhaustively

With the bounds $i\ge-2$ for anti-self-dual components without a cap, $i\ge0$ for those with a cap, $\delta\ge-2$ for chains of reducible components without a cap ([R] Lemmas 4.4–4.5, any spacing $\ge2$; $\delta\ge0$ without positive pieces) and $\delta\ge2$ for chains containing a cap ([R] Lemma 4.6), the maximum of $D_F$ over all arrangements of up to eight components is $-1$ at every $k=1,\dots,7$ (ff8; [Mx] Theorem 3.3). The thresholds are sharp:

| configuration | $D_F$ |
|---|---|
| $k=1$: $(\mathcal M^{*,0}$, cap anti-self-dual, $i=-3,-2,-1,0)$ | $0,\,-1,\,-2,\,-3$ |
| $k=2$: (cap anti-self-dual $i$, reducible chain $\delta=-2$, $\mathcal M^{*,0})$, $i=-3,-2,-1,0$ | $2,\,1,\,0,\,-1$ |
| (inner anti-self-dual $i$ between two $\mathcal M^{*,0}$) , $i=-4,-3,-2$ | $-3,-4,-5$ |
| $(\mathcal M^{*,0}$, chain, inner a.s.d. $i$, chain, $\mathcal M^{*,0})$, $i=-4,-3,-2$ | $1,\,0,\,-1$ |

So an anti-self-dual component is **of low index** if $i\le-3$, or if it contains a cap, $k\ge2$ and $i\le-1$. [F] Proposition 2.5 states the requirement only for $i\le-3$; the corner case with a cap component of index $-1$ or $-2$ next to an isolated positive piece carrying a Seiberg–Witten component of charge $\frac12$ (the extremal chain of [R] §4.5) has $D_F\ge0$ and also needs (A3′). It lies in the end regions as well. **VERIFIED.**

### 2.6 Why two-valued, and the hypothesis (A3′)

**Proposition 2.1** ([F] Proposition 2.6, re-checked). At a limit (anti-self-dual component $A_r$ on $\hat\Gamma_r$, $\mathcal M^{*,0}$-component elsewhere):
- (a) a single-valued $\mathcal G_r$-equivariant term in the Dirac equation of $\hat\Gamma_r$ that depends on $A_r$ and on fields of other pieces vanishes identically: the central element of $\mathcal G_r$ fixes every connection on $\hat\Gamma_r$ and every field of the other pieces, and negates the output;
- (b) a term linear or antilinear in $\Phi_r$ changes $D_{A_r}$ by a compact operator and cannot remove a cokernel forced by negative index;
- (c) a single-valued term that compares frames across the neck depends, in the limit, on the gluing parameter $\rho$; the limiting problem then has $\rho$ as a variable and expected dimension $-3+3=0$, and its solutions glue to ends of $\mathcal Z_e$ whose number nothing controls.

**VERIFIED** as arguments.

**Hypothesis (A3′)** ([Mx] §3.6, with my thresholds). For each of the finitely many unions $\Gamma$ of consecutive pieces in the end regions, each stratum $M_\Gamma$ of low-index anti-self-dual components on $\hat\Gamma$ with its insertions and parameters, and each piece $W\not\subset\Gamma$, there is a two-valued $\mathcal G\times S^1$-equivariant term in the Dirac equation on $\Gamma$,
$$\pm\,\beta(|s_W|)\,s_W^{1/2}\,g_{W,\Gamma}(A|_\Gamma),$$
with $s_W$ a weight-two invariant function of spinor values on $W$ (a section of $\mathbb L_{\mathfrak t}$ determined by restriction to $W$), $\beta$ a cut-off vanishing near $s_W=0$, and $g_{W,\Gamma}$ a section of $W^-\otimes E$ over $\Gamma$ defined on a slice through $M_\Gamma$ and extended by the gauge action (so defined up to the centre). The terms are arbitrarily small, supported near $M_\Gamma\times\{s_W\ne0\}$, vanish near the instanton links, are identical for $e$ and $e^{(i)}$ off $\nu_i$ (so that the exterior problems at the lens faces still coincide), and make $\mathcal Z_e$ a weighted branched one-manifold to which Stokes' theorem applies.

*Effect.* At a limit with an $\mathcal M^{*,0}$-component on $W$ and a component near $A\in M_\Gamma$, the Dirac equation on $\Gamma$ reads $D_A\Phi_\Gamma=\mp\beta s_W^{1/2}g(A)$ with $s_W\ne0$; it is solvable only where $\pi_{\mathrm{coker}D_A}\,g(A)=0$. That is a section of the Dirac cokernel bundle over $M_\Gamma$, of real rank $-2n_a(\hat\Gamma)>q=\dim M_\Gamma$, the same on both branches; for generic $g$ its zero set has dimension $i<0$ and is empty. The trajectories, caps, abelian and Seiberg–Witten components of the limit play no role, so the obstruction of §1.2 does not arise. **VERIFIED** as a count; (A3′) itself **PLAUSIBLE**, new.

*Why the cut-off is harmless.* Along limits of the uncoupled problem of the kind in row 3, $|s_W(\Phi_W)|$ is bounded below by some $\delta_0>0$: a sequence with $\Phi_W\to0$ converges to a pair of anti-self-dual components satisfying all insertions, which (I) excludes, and finitely many $s_W$ have no common zero on the compact set of irreducible $\mathcal M^{*,0}$-components with $\|\Phi\|\ge\delta_0$. Choose $\beta\equiv1$ on $|s_W|\ge\delta<\delta_0$, and then the link radius $\varepsilon_0\ll\delta$. Low-index strata contain no reducibles in their closure ((B2) at a cap; on a stretch of $L\ge5$ negative pieces a reducible limit needs $\kappa\ge\frac12s$, while $i\le-3$ forces $\kappa<\frac12s$, [Mx] §3.6). **VERIFIED** as logic.

---

## 3. The faces $\{t_i=+1\}$

### 3.1 The lens space and the cap

- $\det E|_{L(4,1)}$ is trivial for both lifts: $c_1(E_e)|_{\nu_i}\in\{0,-4\xi\}$ and $H^2(\nu)\to H^2(L(4,1))=\mathbb Z/4$ is reduction modulo four (ff7). The flat $\mathrm{SU}(2)$ connections are $\theta$, $-\theta$ (stabilizer $\mathrm{SU}(2)$) and $\gamma$ (stabilizer $\mathrm U(1)$, $\mathrm{ad}\,\gamma=\underline{\mathbb R}\oplus\mathbb C_{-1}$), all with $H^1=0$; with positive scalar curvature and flat twisting the three-dimensional critical points are $(\pm\theta,0)$, $(\gamma,0)$, the Dirac operators are invertible, and trajectories have zero spinor. **VERIFIED** ([G] Lemma 1.1(3), [B] Lemma 1.2(i)).
- The cap needs positive scalar curvature itself, and an anti-self-dual determinant connection: then FL1 Lemma 4.1 (1b) kills every finite-energy spinor on $\hat\nu_i$, also under small perturbations. The metric of §0 item 7 exists (ff5): scalar curvature recomputed from the Christoffel symbols; $b(r)=B\tanh(4r/B)$ is odd with $b'(0)=4$, and the fibre of $L(4,1)$ has $\sigma_3$-length $2\pi/4$, so the bolt is smooth. **VERIFIED.** The family must restrict to such a metric on $\nu_i$ for both lifts ([MS] Theorem "The metric family" (i)): **PLAUSIBLE** (90%).
- The determinant connections for $e$ and $e^{(i)}$ cannot agree exactly off $\nu_i$ while being anti-self-dual on $\nu_i$: the difference of curvatures would be a closed anti-self-dual form supported in $\nu_i$ representing $\mathrm{PD}[S_i]$, hence harmonic and zero by unique continuation. They can agree off $\nu_i\cup(\text{lens neck})$ with self-dual part $O(e^{-cT})$ on the cap, which positive scalar curvature absorbs; and at the face they agree exactly. That suffices, because the lens ends are determined by limits at the face. **VERIFIED** (refines [F] §3.2).

### 3.2 Reducibles and caps

**Proposition 3.1** (verified two ways each, ff3). The reducible anti-self-dual connections on $\hat\nu_i$ have $v=2m\xi$ ($\xi(S)=1$, $\xi^2=-\frac14$), energy $E=\frac14m^2$, normalized restriction $\mathcal O(m)\oplus\mathcal O(-m)$ to $S$, and lie in $V_{S_i}$ iff $m\ne0$. Read on the common exterior bundle:

| $\lvert m\rvert$ | $E$ | limit, $e_i=0$ | limit, $e_i=1$ | Dirac evaluations ($e_i=0$; $e_i=1$) | $\mathrm{ind}_{\mathbb C}D$ | $\delta_I$ | $\delta_{\rm sp}$ | exterior $\mathcal M^{*,0}$: $2-\delta_{\rm sp}$ | exterior a.s.d.: $1-\delta_I$ |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | $\theta$ | $-\theta$ | $(2,2)$; $(-2,-2)$ | 0 | 0 | 0 | (misses $V_{S_i}$) | (misses) |
| 1 | $\frac14$ | $\gamma$ | $\gamma$ | $(4,0)$; $(0,-4)$ | **0, invertible** | 2 | 2 | **0** | $-1$ |
| 2 | 1 | $-\theta$ | $\theta$ | $(6,-2)$; $(2,-6)$ | $-1$ | 8 | 6 | $-4$ | $-7$ |
| 3 | $\frac94$ | $\gamma$ | $\gamma$ | $(8,-4)$; $(4,-8)$ | $-2$ | 18 | 14 | $-12$ | $-17$ |
| 4 | 4 | $\theta$ | $-\theta$ | $(10,-6)$; $(6,-10)$ | $-4$ | 32 | 24 | $-22$ | $-31$ |

In general $\delta_I=8E$, $\mathrm{ind}_{\mathbb C}D=-E$ (central) or $\frac14-E$ ($\gamma$), $\delta_{\rm sp}=6E$ or $2+6(E-\frac14)$; caps of the same charge and limit have the same framed indices. The limits come from the boundary holonomies $\mathrm{diag}(i^m,i^{-m})$ for $e_i=0$ and $\mathrm{diag}(i^{m-2},i^{-m-2})=-\mathrm{diag}(i^m,i^{-m})$ for $e_i=1$. **VERIFIED.**

*Derivations.*
- $\delta_I$: framed off-diagonal complex index $m^2$ (a) by excision against $\mathbb F_4$ and $\mathbb P(1,1,4)$: $-2+\chi(\mathbb P(1,1,4),\mathcal O(2m))+\chi(\mathbb P(1,1,4),\mathcal O(-2m))$ with $\chi$ from weighted monomials and Serre duality ($K=\mathcal O(-6)$); (b) by closing up in $\overline{\mathbb{CP}}{}^2=\nu\cup(-D(T^*\mathbb{RP}^2))$ ([G] Lemma 4.4): off-diagonal index $m^2-1$ on $\overline{\mathbb{CP}}{}^2$, $-1$ on the rational ball, matching $h^0_{\mathbb C}=[m\text{ even}]$. Both give $m^2$ for $m\le8$; diagonal framed index $0$.
- $I(k)$, the spin$^c$ Dirac index on $\hat\nu$ with determinant evaluation $k$: (a) $I(k)=\chi(\mathbb F_4,\mathcal O(aT))-\chi(\mathbb P(1,1,4),\mathcal O(a))$, $k=2a-2$ (the flat quotient ball with positive scalar curvature has index $0$); (b) Atiyah–Patodi–Singer, $I(k)=\frac{4-k^2}{32}-\frac18\eta_{\rm sign}-\frac12\eta_D(k)$, summed over the four spin$^c$ structures of $L(4,1)$ (whose twisted Dirac operators are the isotypic parts of that of $S^3$, so $\sum\eta_D=0$ for the round metric; the combination $\eta_{\rm sign}(L)+\eta_D(S^3)$ is independent of the metric), with $\eta_{\rm sign}(L(4,1))=-\frac14\sum_{j=1}^3\cot^2\frac{\pi j}4=-\frac12$ (the other sign gives a non-integral sum), $I\le0$ by Lichnerowicz, $I(0)=0$, $I(-k)=I(k)$, $I(k-8)=I(k)+\frac{k-4}2$. Both give $I=0$ for $|k|\le4$, $I(\pm6)=-1$, $I(\pm8)=-2$, $I(\pm10)=-3$, $I(\pm12)=-4$, $I(\pm14)=-6$, and $\eta_D=\frac38,\frac18,-\frac58,\frac18$. The manuscript's table ([MS] Proposition "lens-index") agrees.

At each central state the cheapest cap meeting $V_{S_i}$ has effective charge $1$ for both lifts (the reducible with $|m|=2$, or the flat cap with a point of concentration on $S_i$), so $\delta_{\rm sp}\ge6$; a flat cap misses $V_{S_i}$. The swap of $\pm\theta$ between the lifts changes no count. **VERIFIED.**

### 3.3 Limits over an open lens face

Take $k=0$, $l=1$; the exterior $X^\circ=X\setminus\nu_i$ contains both caps.

| # | exterior component | cap and lens neck | count | handling | status |
|---|---|---|---|---|---|
| 11 | $\mathcal M^{*,0}$, no point of concentration | reducible of energy $\frac14$ at $\gamma$, no trajectory | $2-\delta_{\rm sp}=0$ | **genuine ends**; cancel (§3.5) | count VERIFIED |
| 12 | $\mathcal M^{*,0}$ | effective charge $\frac14+h$ at $\gamma$, $h\ge1$ | $-6h$ | excluded by dimension | VERIFIED |
| 13 | $\mathcal M^{*,0}$ | central, effective charge $\kappa_N\ge1$ | $2-6\kappa_N\le-4$ | excluded by dimension | VERIFIED |
| 14 | $\mathcal M^{*,0}$ with points of total charge $a$ | minimal cap | $\le-2a$ | excluded by dimension | VERIFIED |
| 15 | — | irreducible cap of energy $\frac14$ in $V_{S_i}$ | framed index 2 with a free action of $\mathrm{Stab}(\gamma)/\{\pm1\}$; the cut is a 0-manifold with a free circle action | absent for generic cap data | VERIFIED |
| 16 | anti-self-dual | any | $1-\delta_I\le-1$ | excluded | VERIFIED given single-component regularity |
| 17 | Seiberg–Witten | reference filling | (B3): $\ell-T(v)\le\frac18(7m-3n)+C<0$ | excluded by energy | VERIFIED as deduction; inputs PLAUSIBLE (65%) |
| 18 | abelian | — | contains both caps | excluded ((B2)) | PLAUSIBLE (85%) |

The effective cap charge includes trajectories on the lens neck and points in the cap ([MS] Lemma "lens-charge"); at effective charge $\frac14$ there is neither. The exterior solutions of row 11 are rigid and regular, finitely many over each open face (a sequence escaping to $t_j=\pm1$ converges to a corner limit, §4), and their spinors are bounded below because the exterior anti-self-dual problem is empty; so $\varepsilon_0$ can be chosen below them. Every cap meeting $V_{S_i}$ other than the minimal one makes the exterior factor negative-dimensional by itself, whatever the cap's own Dirac cokernel, so **no coupled perturbation is needed at a lens face**. **VERIFIED.**

### 3.4 Gluing at the minimal cap

Each pair (exterior solution $x$, minimal cap $c_e$) is the limit of exactly one end of $\mathcal Z_e$, and every end over the open face arises so. The gluing parameter is $\mathrm{Stab}(\gamma)/(\mathrm{Stab}\,x\cdot\mathrm{Stab}\,c_e)=\mathrm U(1)/\mathrm U(1)$, a point; the framed cap has tangential index $0$ ($H^1(\nu)=H^+(\nu)=0$), normal complex index $1$ made surjective by a $\mathrm{Stab}(\gamma)$-equivariant perturbation vanishing at the reducible ([MS] Proposition "Regular minimal cap"), invertible Dirac operator, and $V_{S_i}$ cuts the normal line transversely (in the holomorphic model the non-split extension of $\mathcal O(1)$ by $\mathcal O(-1)$ is $\mathcal O\oplus\mathcal O$; local degree $\pm1$, T2 Proposition 3.2). The count is **VERIFIED**; the gluing theorem for $\mathrm{SO}(3)$-monopoles at $\gamma$ is **PLAUSIBLE** (80%): it is (H4)'s gluing plus an invertible complex Dirac block and an exponentially decaying spinor on a free exterior, standard in kind, written in [MS] §10, not in the literature for $\mathrm{SO}(3)$-monopoles.

### 3.5 Orientations and cancellation

**Theorem 3.2.** Fix $i$, $e$ with $e_i=0$, $e'=e+e_i$. The exterior problems for $e$ and $e'$ coincide at the face, and for every exterior solution $x$ the ends of $\mathcal Z_e$ at $(x,c_e)$ and of $\mathcal Z_{e'}$ at $(x,c_{e'})$ have signs with $\sigma_{e'}(x)=\epsilon\,\sigma_e(x)$, $\epsilon$ the sign of [S] Theorem 1.1. Hence $\epsilon(e)\sigma_e(x)+\epsilon(e')\sigma_{e'}(x)=\epsilon(e)\sigma_e(x)(1-\epsilon^2)=0$.

*Proof.*
1. *Orientations.* $O_e$ is FL2b Definition 2.3 (read) with the orientation $o_e$ of $M^{w_e}_\kappa(Q)$ glued along the $Y_{\pm2}$-necks from those of the caps, of the copies of $W_B$ with lifts $c_{e_j}$, and of the copies of $W_H$; via FL2b (2.5) (read), $O_e=o_e\otimes(\text{complex orientation of }\det D_{A,\vartheta})$. The composition law forces these $o_e$ in $\Omega$. FL2b Lemmas 3.24–3.25 (read) compare the link's complex orientation with $O^{\rm asd}$ for any lift by conventions alone, so the link contributes $\sigma_0\,2^{n_a-1}$ times the $o_e$-sign with $\sigma_0$ independent of $e$ (FL2b Proposition 3.29, read: it applies to each $e$ with $w$ good, $d_a\ge0$, $n_a>0$, $z$ intersection-suitable).
2. *Exteriors.* $\mathrm{PD}[S_i]$ restricts to zero on $X^\circ$, so $E_e|_{X^\circ}\cong E_{e'}|_{X^\circ}$; the identification is unique up to homotopy because $[X^\circ,\mathrm{SU}(2)]=H^3(X^\circ)\cong H_1(X^\circ,\partial X^\circ)=0$ ($H_1(X^\circ)=0$ since a class of the adjacent piece meets $S_i$ once; ff7). Excision gives $\lambda_e(y\#_Tc)\cong\lambda^\circ_y\otimes\lambda^{\rm fr}_{e,c}$ with $\lambda^\circ$ common; define $k_e$ by $O^\circ\otimes k_e\mapsto O_e$.
3. *The sign of an end* is (sign of $x$ in the exterior problem) $\times$ (sign of $c_e$ in its normal line cut by $V_{S_i}$, relative to $k_e$) $\times$ (outward normal $\partial_{t_i}$); only the middle factor depends on $e_i$.
4. *Transport.* $\tau_i$ = tensoring framed cap configurations by $L_{-2\xi}$ with its harmonic connection, then a determinant-preserving Weyl conjugation at the boundary returning $\mathrm{diag}(-i,i)$ to $\gamma$ (ambiguity in the connected group $\mathrm{Stab}(\gamma)$, absorbed). It preserves $\mathrm{ad}E$, maps $c_e$ to $c_{e'}$, preserves $\mathrm{Hom}(L_+,L_-)$ with its complex structure and the normalized bundle $E|_S\otimes(\det E|_S)^{-1/2}$, hence $V_{S_i}$ with its complex coorientation. So the canonical section has local degree $+1$ for the intrinsic complex orientation of the normal line at both lifts, and the middle factor changes exactly by $s=[\tau_{i*}k_e:k_{e'}]$.
5. *The spinor contributes $+1$.* Compute $s$ at $y_0=(A_0,0)$ on $X^\circ$. There the operator is (ASD) $\oplus$ (Dirac). The exterior Dirac operator is the same for $e$ and $e'$. The cap Dirac operators for $e$ and $e'$ are *different* operators, on the spin$^c$ structures with evaluations $(4,0)$ and $(0,-4)$ — $\tau_i$ does not map $W\otimes E_e|_\nu$ to $W\otimes E_{e'}|_\nu$, since $W\otimes E_{e'}|_\nu=W\otimes E_e|_\nu\otimes L_{-2\xi}$ — but both are invertible ($I(4)+I(0)=I(0)+I(-4)=0$ with zero kernel by Lichnerowicz), so their determinant lines are canonically trivial. Excision of complex operators preserves complex orientations. So the Dirac factor contributes $+1$ to $s$, and $s$ is the comparison of $o_e$ and $o_{e'}$ alone.
6. *$s=\epsilon$.* $o_e$ and $o_{e'}$ differ only in the factor of the $i$-th copy of $W_B$, $o_c$ against $o_{c+\mathrm{PD}(S)}$; excision at $\nu_i$ commutes with gluing along the $Y$-necks, which are disjoint from $\nu_i$. So $s$ is the local lens-end comparison on $W_B$ of [S] Theorem 1.1, $\epsilon_{c+\mathrm{PD}(S)}/\epsilon_c$, which (H4) makes the constant $\epsilon$ ([G] Lemma 4.5(3), [B] Lemma 2.5). ∎

**Status.** Steps 1–5: **VERIFIED** as linear algebra given the excision isomorphisms of determinant lines with a $\mathrm U(1)$ stabilizer at $\gamma$, which are **PLAUSIBLE**, standard in kind (Donaldson's orientation paper; Donaldson–Kronheimer §7.1). Step 6: (H4)'s locality, **PLAUSIBLE** (85% given the rest). With multisections the comparison holds branch by branch, since the exterior branch lists for $e$ and $e'$ are identical.

**Answers to the questions posed.**
1. *Is the sign the $\epsilon$ of Theorem 1.1?* Yes: the spinor, the $\mu_c$-sections, the circle quotient, the parameters $t_j$ ($j\ne i$) and the outward normal are common to both lifts, and the remaining factor is the instanton comparison on $W_B$.
2. *Transport by a line bundle flat off $\nu S_i$?* On $X$ there is none, nor any line bundle at all relating the two bundles: tensoring by a line bundle changes $c_1$ by an even class and never changes $w_2$ of the adjoint bundle, whereas $w_{e'}-w_e=\mathrm{PD}[S_i]$ pairs to $-1$ with a class of the adjacent negative piece (ff7). On $W_B$, $\mathrm{PD}(S)=2y$ is even ($y$ evaluates $(-1,1)$ on $(F_l,F_r)$, restricts to $\chi$ on $Y_{\pm2}$ and to $-2\xi$ on $\nu S$), so $E_c$ and $E_{c+\mathrm{PD}(S)}$ are two lifts of the *same* $w_2$ there and $E_{c+\mathrm{PD}(S)}=E_c\otimes L_y$ (T2 Lemma 5.1). On $X$ only the local operation $\tau_i$ (the restriction of $\otimes L_y$ to $\nu S$, followed by the Weyl conjugation) is available, and since the comparison is local it gives the same sign as on $W_B$.
3. *Does the spinor change the comparison?* No, for the reason in Step 5. [F] and [MS] (Proposition "The ordinary weights cancel the spinor lens ends") say that the cap tensor operation "acts complex linearly on the spinor bundles"; that is inaccurate, but the conclusion holds by invertibility of both cap Dirac operators.
4. *Does Donaldson's rule for lifts (FL2b Lemma 2.4, read: $o(\Omega,w')=(-1)^{\frac14(w-w')^2}o(\Omega,w)$ for $w\equiv w'\bmod2$) enter?* Not on $X$, where the $w_2$ differ. On $W_B$ the two lifts have the same $w_2$, and a rule of this kind would compare the global identification $\otimes L_y$, which twists the ends by $\chi$; the lens-face sign uses instead the identity on the exterior. The difference between the two identifications is what (H4) packages; it is not needed here.

### 3.6 The cut-down instanton spaces at a lens face

An exterior anti-self-dual connection with limit $\gamma$ and the minimal cap form a stratum of dimension $1-\delta_I=-1$; so no zero-spinor limit lies over $\{t_i=+1\}$ and the link meets $\bar{\mathcal Z}_e$ only over $\mathrm{int}\,Q$. **VERIFIED.**

---

## 4. Corners

**Proposition 4.1.** Over a face with $k+l\ge2$ the closures of $\mathcal Z_e$ and of the cut-down instanton spaces are empty, assuming single-component regularity, (A3′), (B2), and the chain bounds of [R] Lemmas 4.4–4.6 (through [R] Proposition 4.2 with separated caps counted as unbroken).
- (a) *With an $\mathcal M^{*,0}$-component and no low-index anti-self-dual component* (abelian and Seiberg–Witten components allowed): group the other components into intervals between $\mathcal M^{*,0}$-components (inner, at most $f-1$, each contributing $\sum(i_j+4)\ge-2$) and between a cap and the nearest $\mathcal M^{*,0}$-component (outer, each contributing $\ge2$). Then $D_F\le5-4f+2(f-1)-2\#\{\text{outer}\}\le-1$, and lens ends, trajectories and points of concentration only lower it. **VERIFIED** (exhaustive, ff8; [Mx] Theorem 3.3).
- (b) *With an $\mathcal M^{*,0}$-component and a low-index anti-self-dual component:* (A3′) empties that component's factor, and the problem formed by the $\mathcal M^{*,0}$-components and the coupled low-index components has dimension $\le-1$ by the same interval count. **VERIFIED** as a count given (A3′).
- (c) *Without an $\mathcal M^{*,0}$-component.* For $k\ge1$: in (I), anti-self-dual components contribute $\ge4$ (plus $\delta_I-1\ge1$ per lens end), Seiberg–Witten cap components $\ge8$, inner chains of reducible components $\ge-3$ ((B4)). Let $N_0$ be the number of anti-self-dual components and of Seiberg–Witten components containing a cap; the two outer components are among them, so $N_0\ge2$, and the remaining components form at most $N_0-1$ chains. Hence $\sum(q_j+4)\ge4N_0-3(N_0-1)=N_0+3\ge5>4$ ([R] Theorem B, case 2). For $k=0$, $l\ge2$: an anti-self-dual main component has $q_0\le-l$; a Seiberg–Witten one violates (B3); an abelian one contains the caps. **VERIFIED** as a deduction.

So **no necessary projection (A7) is needed at corners**: [F] Proposition 4.1(c) used it with the projected index $\le3-2N-l$; the count of (a) excludes those limits with no hypothesis at the abelian components. **VERIFIED** as logic.

*Consequences.* Lens ends lie over open faces and are finite in number; the cancellation of Theorem 3.2 takes place face by face between $e$ and $e^{(i)}$; no fourfold relation among $e,e^{(i)},e^{(j)},e^{(ij)}$ is needed (two minimal caps already give $1-2=-1$). **VERIFIED** as logic.

---

## 5. The strata, one by one

$k$ = broken three-spheres, $l$ = lens ends. "Dimension" means excluded because a factor that is regular by single-component regularity has negative expected dimension.

| # | stratum | precise count | handling | status |
|---|---|---|---|---|
| 1 | interior, instanton points | link $\mathbb{CP}^{n_a-1}$; $\langle(2h)^{n_a-1},[\mathbb{CP}^{n_a-1}]\rangle=2^{n_a-1}$ | ends of $\mathcal Z_e$ (FL2b Proposition 3.29 with parameters, [C] §4) | count VERIFIED; PLAUSIBLE (85%) |
| 2 | interior, $\mathcal M^{*,0}$ at level $\ell\ge1$ | $\le1-2\ell$ | dimension, given (D4′) | VERIFIED count |
| 3 | interior and lens faces, $\iota(M_{\mathfrak s})\times\mathrm{Sym}^\ell(X)$ | $\ell<T(v)$ by (B3), contradicting incidence $\ell\ge T(v)$ | energy | VERIFIED given (B3) |
| 4 | $k=1$: $(\mathcal M^{*,0},\mathcal M^{*,0})$ | $D_F=-3$ | dimension | VERIFIED |
| 5 | $k=1$: $(\mathcal M^{*,0}$, a.s.d.$)$, $i_r\ge-2$ | $D_F=-3-i_r\le-1$ | dimension | VERIFIED |
| 6 | $k=1$: $(\mathcal M^{*,0}$, a.s.d.$)$, $i_r\le-3$ (end regions) | $D_F\ge0$; under (A3′) the a.s.d. factor has dimension $i_r<0$ | **new analysis: (A3′)** | PLAUSIBLE (60%) |
| 7 | $k=1$: $(\mathcal M^{*,0}$, Seiberg–Witten cap component$)$ | $i_r\ge\lambda^2-O(\lambda)$ | dimension | VERIFIED given [R] Lemma 4.6 |
| 8 | $k\ge1$, no $\mathcal M^{*,0}$-component | (I): $\sum(q_j+4)\ge5>4$ | contradiction | VERIFIED as deduction |
| 9 | $k\ge2$: $\mathcal M^{*,0}$ with abelian and/or Seiberg–Witten chains, no low-index a.s.d. | $D_F\le-1$ | dimension, no hypothesis at the reducible components | VERIFIED given [R] Lemmas 4.4–4.6 |
| 10 | $k\ge2$: $\mathcal M^{*,0}$ and a low-index a.s.d. (inner $i\le-3$, cap $i\le-1$) | without coupling $D_F\ge0$ is possible (up to about $\frac12\lambda_\pm^2$); with (A3′) the kept problem has dimension $\le-1$ | **(A3′)** | PLAUSIBLE (60%) |
| 11 | trajectory of charge $c$ | $D_F$ lowered by $6c-2\delta\ge4$; (I) by $8c-2\delta\ge6$ | dimension (no regularity at the trajectory is needed or possible) | VERIFIED |
| 12 | points of concentration of charge $a$ | $D_F$ by $\ge2a$, (I) by $\ge4a$ | dimension | VERIFIED |
| 13 | $l=1$: $\mathcal M^{*,0}$ on $X\setminus\nu_i$ $\times$ reducible of energy $\frac14$ | $0$ | **genuine ends; cancel** with ratio $\epsilon$ | count VERIFIED; gluing PLAUSIBLE (80%); signs given (H4) |
| 14 | $l=1$: other caps | $-6h$ (trace), $\le-4$ (central) | dimension | VERIFIED |
| 15 | $l=1$: irreducible cap of energy $\frac14$ | free circle on a 0-manifold | generic absence | VERIFIED |
| 16 | $l=1$: a.s.d. exterior | $-1$ | dimension | VERIFIED |
| 17 | $l=1$: Seiberg–Witten exterior | (B3) | energy | VERIFIED given (B3) |
| 18 | abelian component containing a cap | — | (B2) | PLAUSIBLE (85%) |
| 19 | corners, $k+l\ge2$ | rows 8–12 with lens penalties $\ge1$; two minimal caps: $-1$ | dimension or (A3′) | as rows 8–12 |
| 20 | $R=\infty$ | — | not a face at fixed $R$ ([C] §5.2) | VERIFIED |

---

## 6. Attempts to defeat the argument

I tried to construct limits in the closure of $\mathcal Z_e$ that survive every count. In each case I record what stops it.

1. *$(\mathcal M^{*,0}$, anti-self-dual cap component of index $\approx-\frac12\lambda^2)$ at a $J$-face near a cap.* Survives counting ($D_F\approx\frac12\lambda^2-3$) and exists with local perturbations; stopped only by (A3′). This is the genuine gap, as [F] found.
2. *The same with a trajectory on the $J$-neck.* Survives counting if $i_r\le-7$; (A3′) still empties the anti-self-dual factor; the trajectory's own Dirac cokernel, which no perturbation reaches, is irrelevant. It refutes only [F]'s claim that $D_C$ is a dimension.
3. *Corner: cap a.s.d. component of index $-1$, an isolated positive piece carrying a Seiberg–Witten component of charge $\frac12$ ($\delta=-2$), $\mathcal M^{*,0}$ on the other cap piece.* $D_F=0$. Not covered by [F]'s threshold $i\le-3$; in the end regions; needs (A3′). The abelian version needs $v\cdot\omega=0$ at a fixed corner period and is absent for generic data ([Mx] §3.4).
4. *Inner a.s.d. component of index $-3$ between two chains of $\delta=-2$.* $D_F=0$; needs five consecutive negative pieces, so it lies in $\Pi_0$ or $(\phi_*B)^{p'}$; (A3′).
5. *Same with $i=-2$ at spacing four.* $D_F=-1$: excluded with margin one.
6. *$(\mathcal M^{*,0},\mathcal M^{*,0})$ with the relative phase as a modulus.* Already in $D_F=-3$.
7. *An a.s.d. component with nonzero Dirac kernel.* The jump locus has real codimension $2+2c_r$ in a space of dimension $q_r$, empty when $i_r\le1$; for $i_r\ge2$ counting excludes the limit anyway.
8. *A Seiberg–Witten cap component on a long cap piece.* The bulk contributes nonnegatively by [R] Lemma 4.4, the cap $\lambda^2-O(\lambda)$: excluded.
9. *An $\mathcal M^{*,0}$-component on which every chosen weight-two function vanishes.* Excluded by compactness and a finite choice (§2.6).
10. *Lens face: trajectory $\gamma\to\theta$ plus flat cap.* The flat cap misses $V_{S_i}$; a point on $S_i$ makes the effective charge $\ge\frac54$: $-6$.
11. *Lens face: the second minimal cap $m=-1$.* It is the same connection with the summands swapped; one cap per lift.
12. *Lens face: an exterior Seiberg–Witten solution whose splitting differs from the cap's.* Covered by (B3) with the reference filling.
13. *Lens face with a monopole cap.* Excluded by positive scalar curvature on the cap with anti-self-dual determinant curvature; this is why the cap metric is part of the hypotheses.
14. *A point of concentration exactly at the node.* It is neck charge: alternative (iv) or (iii) of §2.2, cost $\ge4$.
15. *An abelian component with stabilizer $\mathrm{SU}(2)$ ($v=0$) between two broken necks.* All its insertions need charge, and the chain bound $\delta\ge-2$ covers it.

---

## 7. Corrected statements

**7.1 To replace in [S] (H5).** Replace "transversality for single components, for the product problem at broken limits (modulo the gauge groups of the pieces and the diagonal circle, by multivalued perturbations) and for the problem obtained by forgetting the components that are abelian instantons" by:
- **(A2)** single-component regularity: the $\mathcal M^{*,0}$-strata of every piece at every level, with their insertions, parameters and the $\mu_c$-sections on products; anti-self-dual components with their insertions, including the face limits $V_{f_l}$, $V_{f_r}$; Seiberg–Witten components for their own families problem;
- **(A3′)** two-valued coupled perturbations at the anti-self-dual components of low index, which lie in the end regions (§2.4–2.6);
- **(D4′)** persistence of the jumping-line representatives, product form at $t_i=-1$, tensor pairing at $t_i=+1$;
- a metric of positive scalar curvature on each cap $\nu_i$ and anti-self-dual determinant connections there, identical for the two lifts.

**7.2 [S] Theorem 4.1, sketch.** "A broken $J_i$ lowers it by four, three for the stabilizer of the trivial connection and one for the parameter, given the transversality of the product problem" should read: "... by four; the limit is then excluded by the dimension of its $\mathcal M^{*,0}$-part, except at anti-self-dual components of low index, where (A3′) is used".

**7.3 [S] "The hardest open point."** The transversality after forgetting abelian instantons is not needed ([Mx]; §4). The hardest point at the faces is (A3′) in the end regions.

**7.4 Theorem (the faces).** Assume (A1) with the uniformity of [C], (A2), (A3′), (D4′), (H4), the cap metrics of §3.1, (B2), (B3) and [R] Lemmas 4.4–4.6 and Proposition 4.2 uniformly over $\bar Q$. Then the closure of $\mathcal Z_e$ over $\partial Q$ consists of finitely many ends over the open faces $\{t_i=+1\}$, each the limit of (rigid $\mathcal M^{*,0}$-solution on $X\setminus\nu_i$ with limit $\gamma$) $\times$ (reducible of energy $\frac14$), one end per exterior solution; and the ends of $\mathcal Z_e$ and $\mathcal Z_{e^{(i)}}$ over the same exterior solution carry signs in the ratio $\epsilon$. Hence $\sum_e\epsilon(e)\,\#(\text{ends of }\mathcal Z_e\text{ over }\partial Q)=0$, and Stokes' theorem gives $\sigma_0\,2^{n_a-1}\Omega=0$ in $\mathbb Q$ once the interior strata are as in [C] and [R]. **VERIFIED** as a deduction from the listed hypotheses.

**7.5 Corrections to [F].**
- (a) Corollary 1.3(b) and Proposition 4.1(a): $D_C$ is not a dimension at limits with trajectories or with caps of negative Dirac index; use $D_F$ and (A3′).
- (b) Proposition 2.4 rows 3, 8 and §6 item 1: no coupling at Seiberg–Witten components.
- (c) Proposition 2.5: the threshold at cap components is $i\le-1$ at corners ($k\ge2$), not only $i\le-3$; the end term for a cap piece is $\pm2$, not $4\Delta$. The end regions stay bounded and fixed before $M$.
- (d) Proposition 4.1(c): no projection (A7); the count of [Mx] suffices.
- (e) Lemma 2.2: the gluing parameter at a pair of $\mathcal M^{*,0}$-components lies in $\mathrm{SU}(2)$.
- (f) Theorem 3.7, Steps 3–4 and answer 3: the local cap operation does not act on spinors; the $+1$ comes from invertibility of both cap Dirac operators.
- (g) (R1): replace by (D4′) of [C].
- (h) Answer 2: the obstruction is $w_2$; on $W_B$ the two lifts have the same $w_2$.

---

## 8. Gaps, with confidences

1. **(A3′)**: two-valued multisections coupling a low-index anti-self-dual component to the phase of an $\mathcal M^{*,0}$-component elsewhere, constructed coherently over the faces and corners of the end regions, compatible with Uhlenbeck compactness (the terms act also over $\mathrm{int}\,Q$ and must be continuous under Uhlenbeck convergence, e.g. through energy cut-offs as in FL1 §1.1.2, so that the lower-level counts of [C] §3.2 persist), the instanton links, the lens collars and the equality of data for $e$ and $e^{(i)}$ off $\nu_i$, with Stokes' theorem for weighted branched one-manifolds. Analogous to multisection techniques in symplectic topology and to [MS] Lemma "Finite samples and available variations"; no precedent for $\mathrm{SO}(3)$-monopoles. **60%** (55–65%).
2. **Single-component regularity (A2)** in families over pieces, including the $\mu_c$-sections on products and the face limits of the jumping-line divisors. **85%.**
3. **The chain and cap bounds** used in $D_F$: [R] Proposition 4.2 uniformly over $\bar Q$ (also at lens corners, with separated caps counted as unbroken), [R] Lemma 4.6, (B2). Shared with the Seiberg–Witten exclusion. **65%.**
4. **The nodal lemma's analysis** and the requirements on the representatives (D4′), product form, face transversality, tensor pairing. **80–85%.**
5. **Gluing at the minimal cap** for $\mathrm{SO}(3)$-monopoles (one end per exterior solution). **80%.**
6. **Orientations**: excision with a $\mathrm U(1)$ stabilizer at $\gamma$ (**90%**) and (H4)'s locality and constancy of $\epsilon$ (**80%**, as in [S]).
7. **Compactness near the faces** (A1): the necks are round or of positive scalar curvature and contribute nothing to the negative part of the Weitzenböck potential ([C] Proposition B). **85%.**
8. **The cap metrics** inside the metric family, identical for the two lifts, with determinant connections anti-self-dual up to $O(e^{-cT})$. **90%.**

---

## 9. Verdict and confidence

**Verdict.**
- *Three-sphere faces.* The limits are pieces matched at $(\theta,0)$ at a cost of $3+1$. Every limit without an $\mathcal M^{*,0}$-component is excluded by (I). Every limit with one is excluded by the dimension of its $\mathcal M^{*,0}$-part, with no hypothesis at abelian or Seiberg–Witten components, unless it contains an anti-self-dual component of low index. Such components occur only in two end regions fixed before $M$, and there a two-valued coupled perturbation (A3′) is needed; single-valued perturbations provably cannot replace it.
- *Lens faces.* The only limits are rigid $\mathcal M^{*,0}$-solutions on $X\setminus\nu_i$ with limit $\gamma$, times the reducible of energy $\frac14$. They glue to one end each and cancel between $e$ and $e+e_i$ with exactly the sign $\epsilon$ of [S] Theorem 1.1. The transport is the local cap operation; no line bundle on $X$ serves, because the $w_2$ differ. The spinor contributes $+1$ because both cap Dirac operators are invertible.
- *Corners.* Nothing occurs; no fourfold relation and no necessary projection are needed.

[F] is correct in substance and in its arithmetic. Its formulation of the coupled hypothesis (regularity of the whole broken configuration) is unattainable at trajectories and must be replaced by (A3′); its thresholds miss cap components of index $-1,-2$ at corners; it keeps an unnecessary projection hypothesis at corners and an unnecessary coupling at Seiberg–Witten components; and its account of the spinor in the orientation comparison is inaccurate though its conclusion is right.

| claim | label | confidence |
|---|---|---|
| identities (I), (M); $D_F$; all index tables ($\delta_I$, $I(k)$, $\delta_{\rm sp}$, swap of $\pm\theta$); the counts of §§2–5; thresholds | VERIFIED | 97% |
| three-sphere critical points, quartic identity, nodal algebra, psc cap metric, topology of the lens face | VERIFIED | 97% |
| nodal lemma with analysis; representatives | PLAUSIBLE | 80–85% |
| no coupling at Seiberg–Witten components; no projection at corners | VERIFIED given [R] Lemmas 4.4–4.6 | 90% given those; 65% unconditionally |
| (A3′) at low-index anti-self-dual components | PLAUSIBLE, new | 60% |
| gluing at the minimal cap | PLAUSIBLE | 80% |
| sign $\epsilon$ with the spinor contributing $+1$ (Theorem 3.2) | VERIFIED as deduction given (H4) | 90% given (H4); 75% overall |
| lens-face cancellation as a whole | PLAUSIBLE | 75% |
| exclusion over three-sphere faces and corners | PLAUSIBLE | about 55% (given the Seiberg–Witten inputs: 60%) |
| **the face statement as a whole (Theorem 7.4)** | PLAUSIBLE | **about 50%** (40–55%) |

The rows are positively correlated: (A3′), the lens gluing and single-component regularity rest on one perturbation framework, and the chain bounds are shared with the Seiberg–Witten exclusion. Compared with [F] (about 45%), the corners no longer need (A7), which raises the figure slightly; the corrected thresholds do not lower it, since they lie in the same end regions.

---

## 10. Report of the checks

All files are in `round4/faces-final-checks/`, written independently of [F]'s files and executed with `python3 -I`; arithmetic is exact (fractions, integers, sympy) unless stated.

**Computations.**
- `ff1_identities.py` → `out_ff1.txt`. Identities (I), (M) and the formula for $D_F$ derived from index additivity piece by piece (exterior indices, framed cap indices $8E$ and Dirac $-E$ or $\frac14-E$, trajectories $8c-3$ with an extra matching, points of concentration), with the closed dimension condition imposed: 20,000 random configurations with $k\le3$, $l\le3$, up to two trajectories and two points; 0 failures.
- `ff2_asd_index.py` → `out_ff2.txt`. Least monopole index of an anti-self-dual component from $Q-6\lfloor Q/8\rfloor$, with $\Theta$ computed from the trace halves: spacing four, $m\le6$, up to three extra negative pieces at each end, all half-evaluations and assignments: least $-2$; spacing five: $-2$; negative stretches $L=1,\dots,24$: $-1,-2,-1,-2,-3,-4,\dots,-7,-8$, first $\le-3$ at $L=5$; cap zones for $\lambda\in\{3,5,7\}$, $p'\in\{8,16\}$, $C_0\in\{-20,0,20\}$ at thresholds $-3$ and $-1$.
- `ff3_lens.py` → `out_ff3.txt`. $I(k)$ by excision against $\mathbb F_4$ and $\mathbb P(1,1,4)$ and, independently, by the $\eta$-sum with integrality ($\eta_{\rm sign}=-\frac12$, unique solution $I(2)=I(4)=0$; the opposite sign gives a non-integer); agreement for $|k|\le14$; $\eta_D=\frac38,\frac18,-\frac58,\frac18$; weighted-monomial counts against the Hilbert series of $1/((1-t)^2(1-t^4))$; framed off-diagonal index $m^2$ by the orbifold and by $\overline{\mathbb{CP}}{}^2$ for $m\le8$; the cap table for both lifts with limits read from boundary holonomies; the three flat $\mathrm{SU}(2)$ connections on $L(4,1)$.
- `ff4_nodal.py` → `out_ff4.txt`. Kernel of the matching problem on chains of 1–4 rational curves with bundles $\mathcal O(a_j)\oplus\mathcal O(-a_j)$, $a_j\le3$, one twist by $\mathcal O(-1)$ in every position, six random $\mathrm{SL}(2,\mathbb C)$ gluing elements and four special ones: kernel $0$ iff all $a_j=0$, nonzero otherwise; 1,252 cases, 0 violations.
- `ff5_psc.py` → `out_ff5.txt`. Scalar curvature from the Christoffel symbols in Euler coordinates: unit $S^3$ gives $6$, the Berger sphere $2(4A^2-\beta^2)/A^4$, the cap metric the formula of §0 item 7 (symbolic identity), limit $2(4A^2-B^2)/A^4$, positivity at 400 random parameter values with $B<2A$, $b'(0)=4$, $b$ odd.
- `ff6_quartic.py` → `out_ff6.txt`. $\langle(\Phi\Phi^*)_{00}\Phi,\Phi\rangle=|(\Phi\Phi^*)_{00}|^2=|\Phi|^4(\frac14+\frac12\sin^22t)$ on 200,000 random $\Phi\in\mathbb C^2\otimes\mathbb C^2$ (relative error $6\cdot10^{-16}$), minimum ratio $\frac14$ at decomposable $\Phi$.
- `ff7_topology.py` → `out_ff7.txt`. $H^2(L(4,1))=\mathbb Z/4$ with reduction modulo four; $\xi^2=-\frac14$; divisibility of $S$ in $H_2(W_B)$ is $2$ and $H_1(W_B\setminus\nu S)=\mathbb Z/2$; $y=(-1,1)$, $y|_{\nu}=-2\xi$, $y$ odd on both ends; $S_i\cdot a=-1$ for a class $a$ of the adjacent negative piece, so $H_1(X\setminus\nu_i)=0=H^3(X\setminus\nu_i)$ and $\mathrm{PD}[S_i]\not\equiv0\pmod2$.
- `ff8_corners.py` → `out_ff8.txt`. Maximum of $D_F$ over all arrangements of 2–8 components ($\mathcal M^{*,0}$, inner and cap anti-self-dual, reducible chains with $\delta=-2$ inner and $\ge2$ at a cap): $-1$ for every $k=1,\dots,7$; the threshold table of §2.5.

**[F]'s files**, read and spot-checked: `out_face_counts2.txt`, `out_near_caps.txt`, `out_lens_dirac.txt`, `out_psc_cap.txt` agree with mine where they overlap; the cap-zone distances differ by $O(1)$ through the convention for the end term and $C_0$.

**Citations checked against the LaTeX** (numbers recomputed with `round4/compactness-final-checks/num.py` and `numeq.py`):

| citation | found | verdict |
|---|---|---|
| FL1 Lemma 4.1 (1b) | `lem:BWDirac`: $D_A^*D_A=\nabla^*\nabla+\frac14R+\rho_+(F_A^+)+\frac12\rho_+(F^+_{A_L}+F^+_{A_e})$ | correct |
| FL1 Lemma 4.4, Definition 4.19, Theorem 4.20 | `lem:C0EstFAPhi`, `defn:UhlenbeckTop`, `thm:SeqCompact` | correct |
| FL2a Proposition 3.1 | `prop:ClassificationOfStabilizers`: fixed points are irreducible ASD with $\Phi=0$, or reducible with $\Phi$ in one summand (generic metric) | correct; its proof is local to a component |
| FL2b Lemma 2.2, (2.5), Definition 2.3, Lemma 2.4 | `lem:OrientableModuliSpace`; `eq:ASDOrientIsom` $\det\mathcal D_{A,\Phi}\cong\det(d^*+d^+)\otimes\det D_{A,\vartheta}$; `defn:ASDOrient`; Donaldson's rule $o(\Omega,w')=(-1)^{\frac14(w-w')^2}o(\Omega,w)$ | correct |
| FL2b (3.10), (3.12), (3.25), (3.62) | `eq:DefineC1LineBundle`, `eq:DefineC1`, `eq:CoDimBound2`, `eq:IntersectionWithBoundary` | correct |
| FL2b Lemma 3.13 | `lem:DefineC1GeomRepr`: a generic section of $\mathbb L_{\mathfrak t}(\nu(x))$, determined by restriction to a ball | correct ([R] §1.3 replaces it by sections sampling every piece) |
| FL2b Corollary 3.18, Lemmas 3.24–3.25, Proposition 3.29, Lemma 3.32, Theorem 3.33 | `cor:IntersectionOfSmoothLowerStrata`, `lem:ComplexASDOrientationComparison`, `lem:OrientationOfV`, `prop:LinkOfASD` (hypotheses: $w$ good, $d_a\ge0$, $n_a>0$, $\deg z\ge d_a$, intersection-suitable), `lem:SplittingSpinu`, `thm:CompactReductionFormula` | correct |
| [MS] Proposition "lens-index", Lemma "lens-charge", Corollary "trace-minimum", Lemma "virtual-sums", Definition "analytic-hypotheses" | `08-indices.tex` l. 127–500: Dirac table and $\delta_I$, $\delta_{\rm sp}$ as in §3.2; reference charge $1$ at the state $-$; omitted connecting fields in (iii) | agree with §§1–3 |
| [MS] Lemma "Finite samples and available variations" | `09-analysis.tex` l. 452: finite isotropy, branch lists $h\cdot s(h^{-1}\cdot)$ with weights $1/|H|$ | the construction (A3′) needs |
| [MS] Propositions "Regular minimal cap", "The ordinary weights cancel the spinor lens ends" | `10-gluing.tex` l. 38, 727 | agree, except the remark on spinors (§3.5, answer 3) |
| [S] Theorem 1.1, Lemma 3.2, Theorems 4.1, 4.3, Proposition 4.2 | `statements.tex` | numbering correct |
| [G] Lemmas 1.1, 4.2, 4.4, 4.5; [B] Lemmas 1.2, 2.4, 2.5; T2 Propositions 2.3, 3.2, Example 3.5, Lemma 5.1 | read | correct as cited |

**By hand.** The isotropy and gluing-parameter groups (§1.3); Proposition 2.1 (a)–(c); the jump-locus codimension $2+2c_r$; the effect of (A3′) (§2.6); the weights of $\mathrm{Stab}(\gamma)$ on the normal line and on the determinant line of $\bar\partial$ at both lifts (T2 Proposition 3.2: local degree $\pm1$ with the intrinsic complex structure of $\mathrm{Hom}(L_+,L_-)$, preserved by tensoring); Steps 1–6 of Theorem 3.2; the unique-continuation remark of §3.1; the attempted configurations of §6.
