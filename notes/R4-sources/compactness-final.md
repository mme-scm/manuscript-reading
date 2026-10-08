# Compactness, energy, interior strata and long necks for the cut-down family space $\mathcal Z_e$

*Round 4, referee's final version. It replaces `round4/compactness-1.md` (cited as [C1]) as the record. Subject: the closure over $\bar Q$ of $\mathcal Z_e=\mathcal V(z)\cap\mathcal W^{n_a-1}\cap\mathcal M^{*,0}_{\mathfrak t_e}(Q)/S^1$ of `statements.tex` §4 for $X=X(\Pi_M)$ and the family $g^R_t$, away from the faces $t_i=\pm1$ (treated in `faces-1.md`) and from the mixed limits with abelian instanton components at those faces (treated separately). The report of my checks is §10.*

**Labels.** **VERIFIED**: proved here; or read in the source named, with the statement or equation number recomputed from its LaTeX counters; or confirmed by an exact or convergent computation listed in §10. **PLAUSIBLE**: standard in kind, or supported by an argument whose structure I checked but whose analysis I did not redo. **SPECULATIVE**: unproved, or a guess.

**Sources.** [S] `statements.tex` (Round 3), §4 and (H1)–(H5). [St] `strategy.tex`, Theorem 2.1. [R] `notes/R3-sources/relation-final.md`. [G] `notes/R3-sources/gluing-final.md`. [C1] the analysis under review, with its computations `round4/compactness-checks/c1_csd_identity.py`, `c2_counts.py`. [MS] the manuscript `src/06-geometry.tex`, `07-estimates.tex`, `09-analysis.tex`, `10-gluing.tex`, cited by section and by a paraphrase of the statement. FL1 = dg-ga/9710032; FL2a = math/0007190; FL2b = dg-ga/9712005 (all in `lit/`). [KM-D] = Kronheimer–Mrowka, *Dehn surgery, the fundamental group and SU(2)*, math/0312322; [OS-Q] = Ozsváth–Szabó, *Knot Floer homology and rational surgeries*, math/0504404 (both in `round4/src-*`). My computations are in `round4/compactness-final-checks/`.

**Notation.** As in [S] §4 and FL2b §3: spin$^u$ structures $\mathfrak t_e$ with $w_2(\mathfrak t_e)\equiv w_e=w_0+\sum_ie_i\,\mathrm{PD}[S_i]$, $\Lambda_e=c_1(\mathfrak t_e)$, $p_1(\mathfrak t_e)=-4\kappa$, $d_a=8\kappa-3(1+b^+)$, $n_a=\Theta-\kappa$, $\Theta=\frac14(\Lambda^2-\sigma)$; $\mu_p(z)$ is represented by $\mathcal V(z)$, the intersection of the jumping-line divisors $V_{S_i}$ and the cap representatives, with $\deg z=d_a+n$; $\mu_c$ by $n_a-1$ sections of $\mathbb L_{\mathfrak t}$ that sample the spinor on every piece ([R] §1.3); the link of the instanton stratum is $\{\|\Phi\|^2_{L^2}=\varepsilon\}$; levels are $\ell$, and the Seiberg–Witten strata are $\iota(M_{\mathfrak s})\times\mathrm{Sym}^\ell$ with $\ell=\kappa+\frac14v^2$, $v=c_1(\mathfrak s)-\Lambda$ (FL2b Lemma 3.32, (3.64)). The *long necks* are the copies of $[-R,R]\times Y_{\pm2}$ joining consecutive copies of $W_B$ through $\phi$ and the two joining the caps, with metric $dt^2+h_Y$, $h_Y$ fixed; the two copies of $Y_{\pm2}$ inside each copy of $W_B\cup W_H\cup W_B$ keep a fixed length. A *block* is a component of $X$ with the middles of the long necks removed: a cap, a copy of $W_B$ (written $W$), or a copy of $W_B\cup W_H\cup W_B$ (written $B_P$; it contains a positive piece $P\cong\mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2$). A component of an ideal limit is *irreducible with nonzero spinor*, *anti-self-dual* (irreducible, zero spinor), a *Seiberg–Witten component* (reducible, nonzero spinor) or an *abelian instanton* (reducible, zero spinor), as in FL2a Prop. 3.1. For a chain $\Gamma$ of components between broken necks, $\varepsilon_I(\Gamma)=\sum_{j\in\Gamma}(q_j+4)$ is the sum of the cut-down instanton indices plus four per component, as in [R] §3.1.

---

## 0. Findings

1. **$C^0$ bound.** $|\Phi|^2\le K_3$ with $K_3$ independent of $t\in\bar Q$ and of $R$, once the tube scale, the regularizer and the isolation lengths of [MS §6] are fixed. This is FL1 Lemma 4.4 with an additive gradient holonomy term. **VERIFIED** as a deduction; its geometric input (scalar curvature bounded below on the family) is read in [MS §6].
2. **Negative-part bound.** [C1] Prop. 2.2 is correct, constants included (re-derived), and is uniform in the lengths of the necks along $J_i$ and $\partial\nu S_i$. Two corrections: on the $S^2\times S^1$ tubes of [MS §6] only $\int h^2=o(\epsilon^{-1})$ holds, not $h=0$; and in [C1] Prop. 2.7(a) the bound must read $|F^{0,+}_A|\le C|\Phi|^2+|P_+|$, since a constant term integrates to the volume of the long necks. **VERIFIED.**
3. **Why it cannot be uniform in $R$.** $\int h^2\ge cR$ on each $Y_{\pm2}$-neck, because $Y_{\pm2}$ carries no metric of nonnegative scalar curvature, and $\int|\Phi|^4$ grows linearly wherever a solution stays near a three-dimensional critical point with nonzero spinor. **VERIFIED.** I closed the gap [C1] left open. The fetched theorem of [OS-Q] gives, at slope $2$, only $g\le2$, so it does not exclude genus two, which is the case that matters. The integer-surgery mapping cone gives $\operatorname{rk}\widehat{HF}(S^3_2(K))=2+2(2g-3)>2$ for every Alexander polynomial of $L$-space form with $2\le g\le5$ (f5).
4. **The Chern–Simons–Dirac identity** of [C1] Lemma 2.5 is correct. I re-derived it with non-gradient errors, checked it as an exact pointwise identity and in integrated form (f1), and read it in [MS §7] (the lemma on the charge of a finite $Y$-middle). Each neck middle has charge $\ge-C_Y(1+\nu)$, and every block has curvature energy $\le C(1+\kappa+M)$, uniformly in $R$ and $t$. **VERIFIED.**
5. **What must be independent of $R$.** Exactly three things: the cap constants $C_W$, the absence of abelian instantons containing a cap, and the vertex alternative on $P$ ([R] Prop. 4.2, Lemma 4.6). The order of choices in [MS §7] makes them so. **VERIFIED** as logic. Their analytic proofs, by contradiction along sequences with $R\to\infty$, are **PLAUSIBLE** (70%).
6. **Lower levels with nonzero spinor.** They have dimension $\le1-2\ell$, with the parameters cancelling (**VERIFIED**). [C1]'s correction is right in substance but overstated. What is needed is *persistence*: $V_{S_i}$ must be closed under Uhlenbeck convergence whose points of concentration avoid $S_i$. Support exactly on $S_i$ is not required. In FL2a's framework the lower strata are products (FL2a Thm. 2.12), and the four-dimensional supports of FL2b Lemma 3.15 are harmless. Lower strata depend on the positions only with FL1's energy cut-offs (FL1 §1.1.2) or with [MS §9]'s sampling terms. [G] (D4) ("perturbations depending only on $A|_{\nu S_i}$") must therefore be sharpened to "continuous for Uhlenbeck convergence off $S_i$". [St] Thm. 2.1 already used sections over the space of connections on $S_i$, which satisfy this.
7. **Zero-spinor lower levels** ($\le-4\ell$), **Seiberg–Witten strata** (incidence and (B3)) and **abelian instantons on $X$** (caps, (B2)): as in [C1]. **VERIFIED** given (B2), (B3).
8. **The link with parameters.** FL2b Lemma 3.22 adapts to $M^w_\kappa(Q)$ (statement and proof read). The local count is $2^{n_a-1}$ per cut-down instanton, with the orientation $O^{\rm asd}(\Omega,w_e)$ for each $e$, so all dependence on $e$ sits in the lens-face comparison. **PLAUSIBLE** (85%); the count is **VERIFIED**.
9. **Long necks.** At finite $R$ no long neck breaks, so the closure of $\mathcal Z_e$ meets no limit broken along $Y_{\pm2}$ (**VERIFIED**). As $R\to\infty$, the breakings at the central flats $\theta,\chi\theta$ have codimension $3$ and all others codimension $0$ (**VERIFIED**). The three-dimensional Seiberg–Witten critical points exist (item 3). For the irreducible flats, [KM-D] Thm. 1 supplies representations, not perturbed critical points; existence after perturbation follows from $I(Y_{\pm2})\ne0$, which holds whenever $\Omega$ can be nonzero. **PLAUSIBLE.**
10. **Central $Y$-necks next to abelian chains (only at $R=\infty$).** [C1] gives the projected index of the minimal chain as $I=2-2\Theta(B_P)\in\{0,1,2\}$. In fact $\Theta(B_P)=1$ for every $e$, since $\Theta=0$ on each copy of $W_B$ and $\Theta(W_H)=1$ (f3). So the count that keeps the deleted parameters gives exactly $I=0$, and the parameter-local count ([R] (A7′)) gives $I'=-2$. Both are computed before Atiyah–Patodi–Singer corrections, which cancel when the two bounding central limits and spin$^c$ restrictions agree. The maximum $8$ printed by check c2(C) is an artefact of treating $\Theta(B_P)$ as free. None of this enters the proof at finite $R$.
11. **Shortening the internal necks.** [C1] Thm. 6.1 is correct as a conditional statement; its arithmetic is **VERIFIED** ($\varepsilon_I\ge-2$ suffices, $-3$ does not; f4(E)). It needs the vertex alternative and the exclusion part of (E0) at *short* internal necks, which [MS] does not state. It buys nothing. **PLAUSIBLE** (55–60%).
12. **Route.** Prove the vanishing at the long necks the composition law needs, at $R\ge\max(R_0(M),T_0(M))$ (route A). It costs Lemma D and Corollary E (proved here), the contradiction arguments of [MS §7] (plausible), and the persistence clause (D4′). Shortening first (route B) costs Theorem H (= [C1] Thm. 6.1), still needs long cap necks and Lemma D, and gains nothing. A block-by-block analysis at $R=\infty$ would need gluing at three-dimensional Seiberg–Witten critical points, which is not available for $\mathrm{SO}(3)$-monopoles.
13. **Verdict.** With (H5′) and (D4′) of §7, the compactness, energy and interior-strata part of (H5) holds as [S] Theorem 4.3 needs it, at every $R\ge\max(R_0(M),T_0(M))$. Confidence about **72%**: the identity 97%, uniform energy 90%, the $R$-independent inputs 70%, persistence 85%, the link 85%.

---

## 1. The setting at a fixed $R$, and what depends on $R$

Fix $M$, the data of [S] §3 and $R$. For each $e$,
$$\dim\mathcal Z_e=(d_a+2n_a+n-1)-(d_a+n)-2(n_a-1)=1$$
(**VERIFIED**, f4(A0); FL2b (3.20), (3.26) with $\deg z-\dim Q$ in place of $\deg z$). At an interior parameter nothing is broken, and a limit of points of $\mathcal Z_e$ is a single ideal monopole $[A,\Phi,\mathbf x]\in\mathcal M_{\mathfrak t_e(\ell)}(g^R_t)\times\mathrm{Sym}^\ell(X)$ (FL1 Def. 4.19, Thm. 4.20; FL2a Thm. 2.12; read). For a compact set of parameters in $\operatorname{int}Q$ the metrics form a smooth compact family, and FL1's proof gives compactness with uniform constants. **PLAUSIBLE**, routine.

Two facts organize what follows.

- At a fixed $R$ the long necks are compact parts of $X$. Every exclusion in [R] Theorems A–C is an index identity or a lattice inequality for charges, and $R$ does not enter, except through the inputs named in item 5 of §0: the cap constants of [R] Lemma 4.6, (B2), and the vertex alternative of [R] Prop. 4.2 at the chosen $R$. **VERIFIED** by reading [R] §§2–4.
- The composition law ([G] Thm. A′) holds for $R\ge R_0$, and $R_0$ depends on all the data on the blocks: the two-parameter families on the copies of $B_P$, their isolation lengths, and the perturbations. Suppose the isolation lengths needed for the vertex alternative had to grow with $R$, because the energy bound did. Then the requirement $R\ge R_0(\text{isolation}(R))$ might have no solution. Uniformity in $R$ is needed to rule out this circularity, and for no other reason. **VERIFIED** as logic, against [MS §7] (the corollary on the order of the finite choices, read) and [MS §5] (its table of choices: caps, then the exceptional evaluations, then $M$, then the tube scale $\epsilon$, then the regularizer, the rational isolations and the gradient tolerance, then the finite $Y$-lengths, then the non-gradient errors).

---

## 2. A priori bounds

### 2.1 The $C^0$ bound

FL1 Lemma 4.4 (label `lem:C0EstFAPhi`, read) proves $\|\Phi\|^2_{C^0}\le K_3$, and FL1 Remark 4.6 gives
$$K_3=\max\Big\{0,\,-\tfrac12\inf_XR+8\|\vartheta_A\|_{L^\infty_{1,A}}+\|F^+_{A_L}\|_{C^0}+\|F^+_{A_e}\|_{C^0}\Big\},$$
from the maximum principle applied to FL1 Lemma 4.1(1b). FL1's perturbations are multiplicative on the quadratic term ($\tau$) and additive on the Dirac operator ($\vartheta$). The instanton problem's Floer perturbation on the $Y$-necks is instead an *additive* term $\nabla\mathcal W_{\rm hol}$ in the curvature equation. At a maximum of $|\Phi|$ it contributes $-|\nabla\mathcal W_{\rm hol}||\Phi|^2$ to the right-hand side of the Weitzenböck inequality, so it enters $K_3$ through its sup-norm only. **VERIFIED** (adaptation).

**Proposition A.** Fix $M$ and the choices of [MS §§6–7] made before the $Y$-lengths (tube scale $\epsilon$, regularizer, rational isolation lengths, gradient tolerance). Then every solution on $(X,g^R_t,\mathfrak t_e)$ satisfies $|\Phi|^2\le K_3$ and $|F^{0,+}_A|\le C(K_3+1)$, with $K_3,C$ independent of $t\in\bar Q$ and of $R$.

*Proof.* The scalar curvature is bounded below uniformly on the family. The $J_i$-necks are round, the lens necks and the lens caps have positive scalar curvature ([MS §6], the theorem on the metric family, (i)), and the toric and rescaled satellite metrics on $P$ have nonnegative scalar curvature, also after their conformal changes ([MS §6], the lemma on uniform collar and satellite models; read). On the $Y$-necks the metric is the fixed product $dt^2+h_Y$. The background connections are harmonic ([MS §7], the lemma on harmonic backgrounds). On the toric pieces their self-dual parts are $2\pi(\Lambda\cdot H/H^2)$ times the Kähler form, whose pointwise norm only decreases under the conformal changes. Since $H^2=2(a+b_0)-4(a^2+b_0^2)\ge c\epsilon$ on the retained toric region, and the region of small width is replaced by the tube model with bounded background, their $C^0$ norms are bounded for fixed $\epsilon$. They are flat on the $Y$-middles and zero on the separated lens caps. ∎ **VERIFIED** as a deduction from FL1 Lemma 4.4 and the cited geometric facts, which are **PLAUSIBLE** (the [MS §6] construction).

### 2.2 The integrated bound with the negative part of the Weitzenböck potential

Write the equations as $D_A\Phi=P_D$ and $\rho(F^{0,+}_A)=(\Phi\Phi^*)_{00}+P_+$. Put $V=\frac14\mathrm{Scal}+\frac12\rho(F^+_{A_\Lambda})$ and $h=\max\{0,-\lambda_{\min}(V)\}$. Then
$$\langle(\Phi\Phi^*)_{00}\Phi,\Phi\rangle=\tfrac14(s^4+t^4)+\tfrac52s^2t^2\ge\tfrac14|\Phi|^4,$$
where $s,t$ are the singular values of $\Phi$ viewed as a $2\times2$ matrix, with equality in the inequality exactly when $\Phi$ has rank $\le1$. In particular $(\Phi\Phi^*)_{00}=0$ only for $\Phi=0$. **VERIFIED** (f2: closed form to $10^{-15}$; minimum ratio $\frac14$).

**Proposition B** ([C1] Prop. 2.2; [MS §7], the local integrated estimate). For $\zeta=f^2$, $0\le f\le1$, compactly supported,
$$\tfrac12\!\int\!\zeta^2|\nabla_A\Phi|^2+\tfrac1{16}\!\int\!\zeta^2|\Phi|^4\le2\!\int\!\zeta^2|P_D|^2+4\!\int\!\zeta^2(h^2+|P_+|^2)+36\!\int\!\frac{|d\zeta|^4}{\zeta^2}.$$
*Proof.* Pair $D_A^*D_A\Phi=D_A^*P_D$ with $\zeta^2\Phi$ and use FL1 Lemma 4.1(1b). The cross terms are bounded by $\frac12\zeta^2|\nabla\Phi|^2+2|d\zeta|^2|\Phi|^2$ and $\zeta^2|P_D|^2+|d\zeta|^2|\Phi|^2$. Young's inequality gives $\zeta^2(h+|P_+|)|\Phi|^2\le\frac18\zeta^2|\Phi|^4+4\zeta^2(h^2+|P_+|^2)$ and $3|d\zeta|^2|\Phi|^2\le\frac1{16}\zeta^2|\Phi|^4+36|d\zeta|^4/\zeta^2$, which leaves $\frac1{16}$ of the quartic coefficient $\frac14$. ∎ **VERIFIED** (re-derived).

On the round $S^3$-necks and on the lens necks with their metric of positive scalar curvature, the background is flat and $h=0$. These necks therefore contribute nothing to $\int h^2$, whatever their length, and the bound is uniform as $t$ approaches the faces. On the $S^2\times S^1$ tubes of [MS §6], $\frac14\mathrm{Scal}=1\ge\frac12|\lambda_{\mathcal T}|$ holds *in the product model*. In the actual metric [MS §7] proves only $\int h^2=o(\epsilon^{-1})$ (the proposition comparing tubes and retained energy, read). Since the tube lengths are $O(\epsilon^{-1})$ and $\epsilon$ is fixed before the $Y$-lengths, this is a bound, not a vanishing. [C1] §2.2 says "$h=0$" there; the conclusion is unaffected. **VERIFIED** (reading).

### 2.3 Why the negative-part bound cannot be uniform in $R$

**Proposition C.** Let $g(K)\ge2$.
- (a) $Y_{\pm2}$ is not an $L$-space.
- (b) For every metric on $Y_{\pm2}$ and every small perturbation for which the reducible critical points are nondegenerate, the three-dimensional Seiberg–Witten equations have a solution with nonzero spinor, in one of the two spin$^c$ structures.
- (c) $Y_{\pm2}$ carries no metric of nonnegative scalar curvature. Hence $\int_{[-R,R]\times Y}h^2=2R\|\frac14\mathrm{Scal}(h_Y)_-\|^2_{L^2(Y)}\ge cR$ with $c>0$.
- (d) Suppose a solution on a neck stays within $\delta$ in $C^0$ of the translation-invariant solution of a critical point $(B,\Psi)$ with $\Psi\ne0$ along an interval of length $L$. Then $\int|\Phi|^4\ge(1-C\delta)L\|\Psi\|^4_{L^4(Y)}$. So no bound on $\int_X|\Phi|^4$ independent of $R$ exists for any product metric on the necks, provided such solutions occur.

*Proof.* (a) If $S^3_p(K)$, $p>0$, is an $L$-space, then $K$ is an $L$-space knot and $\widehat{HF}$ is computed by the Ozsváth–Szabó integer-surgery mapping cone with $A_s\cong\mathcal T^+$. For every Alexander polynomial of $L$-space form with $2\le g\le5$, the cone gives $\operatorname{rk}\widehat{HF}(S^3_2(K))=2+2(2g-3)>2=|H_1|$, and rank $2g-1$ at slope $2g-1$ (f5). This agrees with the known criterion "$p\ge2g-1$". Note that [OS-Q] Thm. `RatSurgeryLSpace` (read) gives only $t_{g-1}=0$ unless $g-1\le p/2$, that is $g\le2$ at $p=2$; it does not exclude genus two. Finally $S^3_{-2}(K)=-S^3_2(\bar K)$, and $\bar K$ has the same genus.
(b) If all critical points were reducible and nondegenerate, the monopole Floer complex would consist of the towers of the reducibles, and $\widehat{HM}$ would have rank $|H_1|$. This contradicts (a) under the isomorphism between monopole and Heegaard Floer homology.
(c) A non-flat metric with $\mathrm{Scal}\ge0$ has no harmonic spinor at a flat connection, so the reducibles are nondegenerate. The three-dimensional Weitzenböck formula then rules out irreducible solutions, contradicting (b). A flat metric is impossible, since no closed flat orientable three-manifold has $H_1=\mathbb Z/2$.
(d) This is immediate from §2.2, since $(\Phi\Phi^*)_{00}\ne0$ wherever $\Phi\ne0$. ∎ **VERIFIED**, (a) given the integer-surgery formula, which is cited from the literature and not from a fetched source. That the situation in (d) arises for points of $\mathcal Z_e$ at large $R$ is **PLAUSIBLE**.

### 2.4 The Chern–Simons–Dirac identity on a neck

On a long neck in temporal gauge, $A=a(t)$, $\Phi=\Phi(t)$. Identify $W^+|_Y$ with the spinor bundle of $\mathfrak s_Y=\mathfrak s|_Y$ and take $A_\Lambda$ flat on the middle, which is possible because $H^2(Y;\mathbb R)=0$. The equations read
$$\dot\Phi+D_a\Phi=e,\qquad\dot a+{*F_a}+\sigma\nabla\mathcal W_{\rm hol}(a)=q(\Phi)+r,\qquad\langle q(\Phi),b\rangle=-c\langle\rho(b)\Phi,\Phi\rangle,$$
with $c>0$ ($c=\frac12$ in [MS]'s convention), $\sigma=\pm1$, $|\mathcal W_{\rm hol}|\le M_{\mathcal W}$, and non-gradient errors $r,e$. With $e=r=0$ these are the downward gradient flow of $\mathrm{CS}+\sigma\mathcal W_{\rm hol}+c\langle D_a\Phi,\Phi\rangle$ for the metric $\|\dot a\|^2+2c\|\dot\Phi\|^2$. That metric is positive only for $c>0$, and $c>0$ is the sign of the positive quartic term (FL2a Lemma 3.12: on the reducible locus these are the Seiberg–Witten equations with $\eta=F^+_{A_\Lambda}$; FL2a Prop. 2.15 gives their compactness).

**Lemma D** ([C1] Lemma 2.5; [MS §7], the lemma on the charge of a finite $Y$-middle). Put $H(t)=\langle D_{a(t)}\Phi(t),\Phi(t)\rangle_{L^2(Y)}$ and normalize $\kappa$ so that $\|F^0\|^2=2\|F^{0,+}\|^2+8\pi^2\kappa$ on every region. Then
$$4\pi^2\kappa_{[u,v]\times Y}=\int_u^v\!\big(\|\dot a\|^2+2c\|\dot\Phi\|^2-\langle r,\dot a\rangle-2c\langle e,\dot\Phi\rangle\big)dt+c\big(H(v)-H(u)\big)+\sigma\big(\mathcal W_{\rm hol}(a(v))-\mathcal W_{\rm hol}(a(u))\big).$$
*Proof.* $4\pi^2\kappa_{[u,v]}=-\int\langle*F_a,\dot a\rangle$ (Chern–Weil in temporal gauge). Substitute the curvature equation and $H'=\langle\rho(\dot a)\Phi,\Phi\rangle-2\|\dot\Phi\|^2+2\langle e,\dot\Phi\rangle$. ∎ **VERIFIED**: by hand; pointwise at 200 random states of a finite-dimensional model with a non-polynomial $\mathrm{CS}$, a bounded $\mathcal W$ and both signs $\sigma$ (relative error $5\cdot10^{-10}$); and in integrated form along trajectories, where the error falls at fourth order ($9\cdot10^{-10}\to6\cdot10^{-11}\to4\cdot10^{-12}$) (f1). With $c<0$ the integrand $\|\dot a\|^2+2c\|\dot\Phi\|^2$ is negative at 130 of 200 random states, so the sign matters.

**Corollary E.** Choose slices $u,v$ in fixed unit strips at the two ends of a neck where $|H|\le B_Y(1+\nu)^{3/4}$; they exist by Fubini and Proposition B on fixed larger strips. Here $\nu$ is the total squared $L^2$-norm of $r,e$ on the neck. Then
$$\kappa_{[u,v]\times Y}\ \ge\ -\frac{2cB_Y(1+\nu)^{3/4}+2M_{\mathcal W}+\frac12\|r\|^2+c\|e\|^2}{4\pi^2}\ \ge\ -C_Y(1+\nu),$$
with $C_Y$ independent of $R$, $t$ and $\nu$. **VERIFIED** (Young's inequality; f1 checks the inequality on trajectories). [C1] Cor. 2.6 omits the factor $(1+\nu)^{3/4}$, which is harmless; [MS §7] has it.

### 2.5 Uniform energy on blocks and neck middles

**Proposition F.** With the choices of Proposition A fixed, there is $C$, independent of $R$, $t$ and the solution, such that, with $K(M)=\kappa+C(1+M)$:
- (a) $\kappa_B\ge-C$ for every block $B$ extended by unit strips, and $\kappa_N\ge-C_Y(1+\nu)$ for every neck middle $N$;
- (b) $\kappa_B\le K(M)$ and $\kappa_N\le K(M)$, by additivity of the charge, since there are $O(M)$ blocks and necks;
- (c) $\|F^0_A\|^2_{L^2(B)}\le2C+8\pi^2K(M)$ and $\int_N(\|\dot a\|^2+2c\|\dot\Phi\|^2)\le C(1+K(M))$;
- (d) on each unit interval $I$ of a neck, $\|F^0_A\|^2_{L^2(I\times Y)}\le C(1+\int_I\|\dot a\|^2)$;
- (e) an Uhlenbeck limit along any sequence $(t_\nu,R_\nu)$ has at most $C(1+K(M))$ points of concentration.

*Proof.* (a) $8\pi^2\kappa_B\ge-2\|F^{0,+}\|^2_B$, and $\|F^{0,+}\|^2_B\le C\int_B|\Phi|^4+C\int_B|P_+|^2$. Both terms are bounded by Proposition B, because $h=0$ on the $J$- and lens necks inside $B$, $\int h^2$ is bounded on the tubes for fixed $\epsilon$, and the perturbations have bounded squared norms. (The form $|F^{0,+}|\le C(|\Phi|^2+1)$ used in [C1] would bring in the volume of the long $J$- and lens necks.) The rest is Corollary E, additivity of $\kappa$ (topological on the closed manifold, with no sign assumption on components), Lemma D, $|F_a|\le|\dot a|+|q(\Phi)|+|\nabla\mathcal W_{\rm hol}|+|r|$, and the fact that a point of concentration carries $8\pi^2$ of $\|F^0\|^2$ while $F^{0,+}$ has no atoms. ∎ **VERIFIED** as a deduction; the constants were not computed. This is [MS §7], the proposition on retained energy, together with the bound on the retained charge given there (read).

Under Proposition F, the quantity that stays bounded along a long $Y_{\pm2}$-neck is the drop of the Chern–Simons–Dirac functional. The integrals $\int|F|^2$ and $\int|\Phi|^4$ do not stay bounded.

### 2.6 The inputs that must be independent of $R$

Reading [R] Theorem C, [S] §4 and [MS §7], the inputs fixed before $M$ (hence before $R$) are the cap constants $C_W$ of [R] Lemma 4.6(b). The inputs that must hold at *every* $R\ge T_0(M)$, with $T_0$ depending only on choices made before $R$, are (B2) and the vertex alternative of [R] Prop. 4.2. Everything else in (H5) (transversality, the link, gluing at the lens faces, Stokes) is used at the chosen $R$, with constants that may depend on it. **VERIFIED** as logic.

- *Caps* ([MS §7], the proposition on cap constants fixed before exterior choices; read). The cap metric avoids the countably many walls of classes $v_W$ with $\langle v_W,A_\pm\rangle$ odd. Then $\|v_W^+\|\le B_W$, with $B_W$ built from the local bound for $\|D^+\|_{L^2}$ on unit sets of the completed cap and from the exponential decay of the cap's self-dual harmonic forms. The topological restriction of $v$ is identified with this projection up to an error $\le C'_We^{-\sigma N}(E+C'_W(N+2))^{1/2}$, where $E$ is bounded by Proposition F with the slice taken beyond a prefix of length $N+2$. So $C_W=1+\max\{B_W^2,(\|\Lambda_W^+\|+B_W)^2\}$ depends only on the cap. **PLAUSIBLE** (80%).
- *Positive pieces* ([MS §7], the lemmas on the period inequality for an isolated positive piece and on the vertex test with persistence at finite sizes; read). Suppose the alternative failed along a sequence in which the regularization tends to $0$, the isolations tend to $\infty$, the perturbations tend to $0$ and $\min R\to\infty$. Then a subsequence converges, by the uniform energy of Proposition F, to an unperturbed reduction on the completed toric piece, and the period inequality is contradicted. The positive piece is isolated by rational (lens) collars *inside* $B_P$, so the $Y$-lengths enter only through the energy bound. **PLAUSIBLE** (70%; it inherits the uncertainty of the toric construction of [MS §6]).

---

## 3. The interior strata at a fixed $R$, one by one

| stratum (interior $t$) | dimension or reason | status |
|---|---|---|
| top: $\mathcal Z_e$ | smooth one-manifold for generic data (parametric transversality, FL2a Thm. 2.13 / FL1 Thm. 1.3 with $Q$ added) | PLAUSIBLE, routine |
| level $\ell\ge1$, irreducible, $\Phi\ne0$ | $\le1-2\ell$, provided persistence (§3.2) | VERIFIED as a count |
| level $0$, zero spinor | the finitely many points of $\mathcal V(z)\cap M^{w_e}_\kappa(Q)$ ((E0), [G] Thm. A′(1)); their link is §4 | VERIFIED given (E0) |
| level $\ell\ge1$, zero spinor | $\le-4\ell$ | VERIFIED |
| $\iota(M_{\mathfrak s})\times\mathrm{Sym}^\ell$ | incidence forces $\ell\ge T(v)$; (B3) says $\ell<T(v)$ | VERIFIED given (B3) |
| abelian instantons on $X$ | contain both caps; excluded by (B2) once the cap necks are long, at every level | PLAUSIBLE (85%) |
| broken along $Y_{\pm2}$ | none at finite $R$ | VERIFIED |

### 3.1 The top stratum

$\mathcal Z_e$ is a smooth one-manifold for generic data in the class of (A2)–(A3) of [R]. **PLAUSIBLE**, standard.

### 3.2 Lower levels with irreducible connection and nonzero spinor

At level $\ell$, $\dim\mathcal M^{*,0}_{\mathfrak t_e(\ell)}(Q)/S^1=d_a+2n_a-1+n-6\ell$ (FL2b (3.20) and the sentence after it, read). The parameters enter this dimension and $\deg z=d_a+n$ equally. A limit satisfies every condition that persists. There are two regimes.

- **Product lower strata.** With FL2a's perturbations $(g,\rho,\tau,\vartheta)$ the closure lies in $\bigsqcup_\ell\mathcal M_{\mathfrak t_\ell}\times\mathrm{Sym}^\ell(X)$ (FL2a Thm. 2.12, read). The same holds with Floer's holonomy perturbations on the $Y$-necks, which are averages over families of loops and converge under Uhlenbeck convergence ([MS §9], the lemma on compactness on bodies, read). The background must satisfy the conditions not released, of total degree $\ge\deg z+2(n_a-1)-4\ell$ by FL2b (3.25). So the stratum has dimension $\le1-2\ell<0$, whatever the dimension of the supports. This is FL2b's count before Cor. 3.18 (read); that count is a count of the background and does not involve positions.
- **Lower strata that depend on positions.** FL1's holonomy perturbations carry energy cut-offs, so the lower levels are not products (FL1 §1.1.2, read: "the spaces $\mathbf M_{W,E_{-\ell}}$ are not products when $\ell>0$"). The same is true of [MS §9]'s sampling terms (its formula for the energy cut-offs, read), which the coupled regularity of [R] (A3), (A7) uses. Then the count is over pairs (background, positions), and the stratum has dimension $\le1-6\ell+\sum_x\big(\dim(\text{allowed positions of }x)+\text{degree released at }x\big)$. This is $<0$ if every point of concentration contributes at most $4$.

**The correction, corrected.** The jumping-line condition $V_{S_i}$ is the zero set of $s(A|_{S_i})+p(A)$, where $s$ is the canonical section of the determinant line of $\bar\partial_A$ on the twist by $\mathcal O(-1)$ and $p$ is a small transversality term. If $p$ is continuous for Uhlenbeck convergence whose points of concentration avoid $S_i$, then a limit with no point of concentration on $S_i$ satisfies the limiting condition $s+p_\infty=0$, possibly modified by cut-offs. That is still a condition of degree two, so nothing is released. A point on $S_i$ has two position parameters and releases degree two, which totals $4$. The other supports of [R] §1.3 are within the bound as well: a cap point contributes $0+4$, a cap surface $2+2$, two cap surfaces meeting $0+4$, a sample point of a $\mu_c$ section $0+2$, a transport path $1+2$, and a point on no support $4+0$. So every lower stratum has dimension $\le1-2\ell$ (**VERIFIED**, f4(A)). If $p$ is merely a smooth function of $A|_{\nu S_i}$ that is not Uhlenbeck-continuous, the condition may be lost at every point of $\nu S_i$. A point there then contributes $4+2=6$, and the level-one stratum has expected dimension $1-6+6=1$ (**VERIFIED** as a count, f4(A3); this is [C1]'s observation). Hence:

> (D4′) The transversality term of $V_{S_i}$ is continuous for Uhlenbeck convergence whose points of concentration avoid $S_i$. For instance, it may be a finite sum of sections over the space of connections on $S_i$, as in the proof of [St] Thm. 2.1, or a function of holonomies averaged over families of loops in $\nu S_i$. It vanishes near the compact set of restrictions of reducible limits with $\langle v,S_i\rangle=0$, where $s\ne0$.

This replaces [C1]'s "the support must be exactly $S_i$". Sufficiency is **VERIFIED** as a count. That (D4′) is compatible with transversality on all strata, with the tensor pairing at the lens faces and with (D5) at the $J$-faces is **PLAUSIBLE** (85%). The perturbation directions span each fibre of the determinant line, so the Sard–Smale argument applies; compatibility at the faces belongs to the faces analysis. [MS §9], in the lemma on exact supports and incidence, states and proves exactly this persistence rule for its own (holonomy) representatives of $\mu(S_i)$ (read).

### 3.3 Zero spinor

At level $0$, a limit of points of $\mathcal Z_e$ with zero spinor lies in $\mathcal V(z)\cap\iota(M^{w_e}_\kappa(Q))$, because $\mathcal V(z)$ is closed and the $\mu_c$-sections impose nothing there (FL2b Lemma 3.15(2d)). By (E0) it is one of finitely many regular interior points. At level $\ell\ge1$, the background lies in $M^{w_e}_{\kappa-\ell}(Q)$, of dimension $d_a-8\ell+n$, under conditions of degree $\ge d_a+n-4\ell$. This leaves $\le-4\ell$; with the weaker rule of §3.2 it leaves $-2\ell$. **VERIFIED.** Limits of $\mathcal Z_e\cap\{\|\Phi\|^2\ge\varepsilon\}$ have $\|\Phi\|^2\ge\varepsilon$, because $|\Phi|$ is bounded in $C^0$ and does not concentrate; so zero-spinor limits occur only at the link. **VERIFIED.** Since $w_e$ is good ([R] Lemma 1.1(c)), there are no flat $\mathrm{SO}(3)$ connections, and the zero-spinor stratum is $\iota(\bar M^{w_e}_\kappa(Q))$ near the cut-down points (FL2b Lemma 3.21). **PLAUSIBLE** in families.

### 3.4 Seiberg–Witten strata

For a limit in $\iota(M_{\mathfrak s})\times\mathrm{Sym}^\ell$ with $v=c_1(\mathfrak s)-\Lambda_e$, (J2) gives splitting type $|\langle v,S_i\rangle|/2$ on $S_i$. A sphere with $\langle v,S_i\rangle=0$ therefore needs a point of concentration on $S_i$, by (J1), (J3) and (D4′), and distinct spheres need distinct points. Hence $\ell\ge T(v)$, contradicting (B3). The level is topological, so the long necks play no part. **VERIFIED** given (B3). (B3) rests on $-\frac14v^2+T(v)\ge\frac12(n-m)-C$ with $C=\frac14(C_{W_-}+C_{W_+})$ ([R] §4.4), which uses the inputs of §2.6.

### 3.5 Abelian instantons on $X$

At an interior parameter the single component contains both caps. Such limits exist in the family over walls of codimension $b^+(X)<n$. $\langle w_e,A_\pm\rangle$ is odd, so $v_W\ne0$. The class $v$ has $-v^2\le4\kappa$ and is anti-self-dual, so only finitely many classes occur for given $M$. The cap metric was chosen so that none of them restricts to an anti-self-dual class on the completed cap. With long cap necks the harmonic forms localize, and no such limit exists ([R] (B2); [MS §7], the proposition on cap constants). **PLAUSIBLE** (85%).

### 3.6 Summary at interior parameters

At a fixed $R\ge\max(R_0(M),T_0(M))$, the only limits of $\mathcal Z_e$ over $\operatorname{int}Q$ outside the top stratum are the finitely many points of the link. **VERIFIED** as a deduction, given (E0), (B2), (B3), (D4′) and the regularity of the lower strata.

---

## 4. The link of the instanton stratum, with parameters

Let $(A,t_0)$, $t_0\in\operatorname{int}Q$, be a point of $\mathcal V(z)\cap M^{w_e}_\kappa(Q)$. It is regular for the family problem, and $\mathcal V(z)\subset\mathcal B^{w,*}_\kappa\times Q$ has codimension $d_a+n=\dim M^{w_e}_\kappa(Q)$ and meets it transversely.

1. *Kuranishi model.* Near $(A,0,t_0)$ the family $\mathcal M_{\mathfrak t_e}(Q)$ is the zero set of an $S^1$-equivariant map $T_{(A,t_0)}M^{w_e}_\kappa(Q)\oplus\ker D_{A,t_0}\to\operatorname{coker}D_{A,t_0}$. Its domain has real dimension $(d_a+n)+2(n_a+c)$ and its target $2c$, consistent with $\dim\mathcal M^{*,0}(Q)=d_a+2n_a+n$ (f4(C)). Only the family operator, the anti-self-duality operator with the $\partial_t$ directions added, needs to be onto; $H^2_A(g_{t_0})$ may be nonzero. This is FL2a Cor. 3.6 with parameters. **PLAUSIBLE**, routine.
2. *Deforming $\mathcal V$.* FL2b Lemma 3.22 (label `lem:DeformingV`; statement and proof read) uses only that $\mathcal V(z)$ is a smooth submanifold of $\mathcal B^{w,*}_\kappa$ transverse to $M^w_\kappa$ at the point. With connections replaced by (connection, parameter), $\mathcal V(z)$ becomes a graph over $\ker D_{A,t_0}$, tangent to it, with $(\alpha,s)=O(|\psi|^2)$. **VERIFIED** as an adaptation.
3. *Count.* FL2b Lemma 3.27 gives the Euler class $h^c$ of $S^{2k-1}\times_{S^1}\mathbb C^c$ over $\mathbb P(\ker D)\cong\mathbb{CP}^{k-1}$, $k=n_a+c$, for *any* transverse equivariant section of weight one. The terms of the obstruction map that involve the parameter or the instanton directions are $O(|\psi|^3)$ on $\mathcal V(z)$ and do not change it. FL2b Lemma 3.28 gives $\mu_c=2h$ for sections sampling every piece ([R] §1.3). The count is $\langle(2h)^{n_a-1}h^c,[\mathbb{CP}^{n_a+c-1}]\rangle=2^{n_a-1}$ (FL2b Prop. 3.29, statement and proof read; its hypotheses, $w$ good, $d_a\ge0$, $n_a>0$, $\deg z\ge d_a$ and $z$ intersection-suitable, hold, the last by §3.2). **VERIFIED** as arithmetic (f4(C)); with parameters **PLAUSIBLE** (85%).
4. *Orientation.* FL2b Lemmas 3.24–3.25 (read) compare, for each $w$, the complex orientation of the link with the orientation $O^{\rm asd}(\Omega,w)$ of $\mathcal M^{*,0}/S^1$ induced by $o(\Omega,w)$. Applied to each $e$ separately, with the factor $Q$ common, they give $\sigma_0\,2^{n_a-1}\#(\mathcal V(z)\cap M^{w_e}_\kappa(Q))$ with $\sigma_0$ fixed by conventions. All dependence on $e$ is therefore in the comparison of $O^{\rm asd}(\Omega,w_e)$ with $O^{\rm asd}(\Omega,w_{e+e_i})$ at the lens faces, which is (A5) and belongs to the faces analysis. **PLAUSIBLE.**

The four ways in which [C1] §4 says the parameter could interfere are correctly dismissed: jumps of $\dim\ker D$; terms involving $\partial_tD$, which are cubic on $\mathcal V(z)$; abelian instantons on walls, excluded by (B2); and cut-down points near a face, excluded by (E0). **VERIFIED** as logic.

---

## 5. The long $Y_{\pm2}$-necks

### 5.1 Three-dimensional critical points

On a long neck $c_1(E_e)|_Y=0$, since $c_0$ vanishes on $Y_{\pm2}$ and $\mathrm{PD}[S_i]$ vanishes off $S_i$. So $E|_Y$ is trivial. The neck equations are the downward gradient flow of $\mathcal L=\mathrm{CS}+\sigma\mathcal W_{\rm hol}+c\langle D_a\Phi,\Phi\rangle$ modulo the determinant-one gauge group, with the circle acting on $\Phi$. Its critical points are of four kinds, and of no others.

| kind | connection, spinor | stabilizer in the determinant-one gauge group | critical set mod gauge | circle | on $Y_{\pm2}$ |
|---|---|---|---|---|---|
| (a) | central flat $\theta$ or $\chi\theta$, $\Phi=0$ | $\mathrm{SU}(2)$ | point | fixed | always |
| (b) | irreducible flat, $\Phi=0$ | $\{\pm1\}$ | point | fixed | if $I(Y_{\pm2})\ne0$, after perturbation |
| (c) | $a=b_1\oplus b_2$ on $L\oplus L^{-1}$, $L\in\{\mathbb C,\chi\}$, $\Phi=(\psi,0)$ with $(b_1,\psi)$ an irreducible Seiberg–Witten solution | trivial | point | fixed, via $\mathrm{diag}(u,u^{-1})$ | yes (Prop. C(b)) |
| (d) | irreducible $a$, $\Phi\ne0$ | trivial | circle | free modulo $\pm1$ | unknown |

*Justifications.* The reducible flat connections factor through $H_1=\mathbb Z/2$ and are central with $H^1=0$ ([G] Lemma 1.1). For (c), a reducible $a$ with both summands of $\Phi$ nonzero has $q(\Phi)$ with nonzero off-diagonal part $(\psi_1\psi_2^*)_0$; so by unique continuation one summand vanishes, and a central $a$ forces $(\Phi\Phi^*)_{00}=0$, hence $\Phi=0$ (§2.2). If $b_1=b_2$, $a$ is central. The stabilizer of $(b_1\oplus b_2,(\psi,0))$ is $\{\mathrm{diag}(u,u^{-1}):u\psi=\psi\}=\{1\}$, and swapping the summands stabilizes only central connections. **VERIFIED.** For (b), [KM-D] Thm. 1 (read) gives a representation $\pi_1(Y_{\pm2})\to\mathrm{SU}(2)$ with non-cyclic image, which is irreducible since $H_1=\mathbb Z/2$. A small holonomy perturbation can, however, remove degenerate critical points. Existence of perturbed critical points follows from $I(Y_{\pm2})\ne0$, which holds whenever the pairing $\langle\Psi_{C_+},\Pi_M\Psi_{C_-}\rangle$, and hence $\Omega$, can be nonzero. **PLAUSIBLE.** Nondegeneracy of (c) and (d) needs perturbations depending on the spinor as well, of the kind used by Kronheimer and Mrowka. It is needed only at $R=\infty$. **PLAUSIBLE.**

### 5.2 At finite $R$

The long necks have finite length, so no limit over $\bar Q$ at a fixed $R$ is broken along $Y_{\pm2}$. **VERIFIED.** A point of $\mathcal Z_e(R)$ may sit near a critical point of kind (b), (c) or (d) along most of a neck. That is a point of the top stratum, and nothing has to be excluded.

### 5.3 As $R\to\infty$

By Proposition F, along $(t_\nu,R_\nu)$ with $R_\nu\to\infty$ a subsequence converges on the completed blocks away from finitely many points of concentration. On each neck only a bounded number of unit intervals carry more than a fixed amount of $\int(\|\dot a\|^2+2c\|\dot\Phi\|^2)$, and elsewhere the slices are near the critical set, which is compact modulo gauge. **PLAUSIBLE**: standard in structure, but not in the literature for $\mathrm{SO}(3)$-monopoles. With $2n_a=\sum_\beta i_\beta+\sum_k(\dim\mathrm{Stab}_k+\dim C_k)$ ([G] (I1)–(I2) with invertible Hessians), the broken configurations, after the $\mu_c$-sections and the diagonal circle, form a space of dimension
$$D(\zeta)=1-3\,\#\{\text{necks at }\theta\text{ or }\chi\theta\},$$
for every assignment of kinds (**VERIFIED**, f4(D)). At (b) and (c) the circle phases of adjacent blocks with nonzero spinor are independent and the relative phase is a coordinate; at (d) the matching fixes it, but the critical set is a circle. So breakings of kinds (b), (c), (d) have codimension $0$ in the face $R=\infty$ of $\bigcup_R\mathcal Z_e(R)\times\{R\}$, and a central neck costs $3$. Kinds (b)–(d) cannot be excluded by index or by energy, since their Chern–Simons–Dirac values form a bounded set. They need not be excluded: they are not limits at any finite $R$. **VERIFIED** as logic.

### 5.4 Central necks next to chains of abelian instantons (only at $R=\infty$)

Delete a maximal chain $\Gamma$ of blocks carrying abelian instantons, bounded by central necks. With $i_\beta$ the real monopole index of a block (anti-self-duality index $8E-3(1+b^+)$ with central limits, plus parameters, minus insertions, plus twice the Dirac index $\Theta_\beta-E_\beta$), the projected problem has index
$$I=-2-\sum_{\beta\in\Gamma}(i_\beta-p_\beta+3)\quad\text{(parameters of }\Gamma\text{ kept)},\qquad I'=I-\sum_{\beta\in\Gamma}p_\beta\quad\text{(parameter-local, [R] (A7′))},$$
with $i_W=6E_W-4$, $i_{B_P}=6E-8+2\Theta(B_P)$, $p_W=1$, $p_{B_P}=2$ (**VERIFIED**, by hand).

**Lemma G.** Take the chamber-compatible lift: $(\Lambda_0\cdot F_l,\Lambda_0\cdot F_r)\in\{(0,-2),(2,0)\}$ on each copy of $W_B$, and $\Lambda_0|_P$ with evaluations $(-2,-1;0,1,0,-1)$ on $G,U;T_1,\dots,T_4$ ([R] §4.1). Then for every $e$: $\Theta=0$ on every copy of $W_B$, $\Theta(P)=1+\frac12(e_a-e_b)$, $\Theta(W_H)=1$, and $\Theta(B_P)=1$.

*Proof.* $\Theta$ is additive over rational homology spheres. On a copy of $W_B$, $\Lambda_e\cdot F_l=\Lambda_0\cdot F_l-2e$ and $\Lambda_e\cdot F_r=\Lambda_0\cdot F_r+2e$ are $0$ and $\pm2$ in some order, so $\Lambda^2=-2=\sigma$. On $P$, compute with the form $\left(\begin{smallmatrix}2&1\\1&0\end{smallmatrix}\right)\oplus\langle-1\rangle^4$, the near halves $G-\sum T_b$ and $G-2U$, and the twist by $e_a,e_b$. Then subtract the near halves. ∎ **VERIFIED** (f3, exact arithmetic, all $e$).

Consequently, with $E_W,E_{B_P}\ge\frac12$ ([R] Lemma 4.4), the minimal chain (a single copy of $B_P$ at $E=\frac12$, $u=v\cdot U=0$) has $I=0$ exactly and $I'=-2$. The maximum of $I$ over chains at spacing four is $0$, and the maximum of $I'$ is $-2$ (f3). [C1] states $I=2-2\Theta(B_P)\in\{0,1,2\}$ and allows $\Theta(B_P)\in[0,2]$; check c2(C) even reports a maximum $I=8$ for chains of four copies of $B_P$ with $\Theta(B_P)=0$. Those values of $\Theta$ do not occur. Two Atiyah–Patodi–Singer terms of the twisted Dirac operators of $(Y_{\pm2},\mathfrak s_Y)$ at the two bounding necks remain. They cancel when the two central limits are of the same kind and the spin$^c$ restrictions agree, and otherwise shift $I$ by a difference of spectral invariants of $D_{\mathfrak s_Y}\otimes\mathbb C^2$ and $D_{\mathfrak s_Y\otimes\chi}\otimes\mathbb C^2$, which depends on $K$. **PLAUSIBLE.** So [C1]'s conclusion stands in weakened form: under the coarse count these limits are not excluded ($I=0$); under the parameter-local count they are, up to those spectral terms. None of this enters route A.

### 5.5 Where $R=\infty$ enters

Only in the proofs by contradiction of §2.6, on the completed blocks (the cap and the isolated toric piece), where the kind of critical point at the $Y$-ends plays no role. A block-by-block analysis of $\mathcal Z_e$ at $R=\infty$ would need gluing at kinds (c) and (d) and the exclusion of §5.4. Neither is available for $\mathrm{SO}(3)$-monopoles. **VERIFIED** as a reading of [MS §7] against Proposition F.

---

## 6. Shortening the necks, and the choice of route

**Theorem H** ([C1] Thm. 6.1, restated). Fix $M$ and the choices made before the $Y$-lengths. Keep the two cap necks at a length $L\ge L_{\rm cap}$ for which (B2) and the cap constants hold. Give the other long necks a common length $R\in[R_1,R_2]$. Assume, for all $R\in[R_1,R_2]$ and $t\in\bar Q$:
- (i) regularity of the cut-down instanton problem in one-parameter families, the face condition (D5) of [G], and gluing at the lens faces;
- (ii) the vertex alternative of [R] Prop. 4.2 for abelian instantons;
- (iii) data local in the parameters, and (J1)–(J4).

Then $\Omega(X;g^{R_1})=\Omega(X;g^{R_2})$.

*Proof.* As in [C1] §6: consider the cut-down instanton space over $Q\times[R_1,R_2]$, of dimension one.
- Points of concentration leave dimension $\le1-4\ell$.
- Abelian instantons at interior $t$ contain the caps.
- At a $J$-face, the identity $\sum_j(q_j+4)=4$ holds at the value of $R$ where the limit lies. At most one anti-self-dual component has $q_j=-1$ for generic local data, and the chains between anti-self-dual components have $\varepsilon_I\ge-2$ at spacing four ([R] Lemma 4.5 and its exact minima). Hence $\sum\ge2a+1\ge5$.
- The lens ends cancel between $e$ and $e+e_i$.
∎ The arithmetic is **VERIFIED**: f4(E) re-derives it, with $-2$ sufficient and $-3$ not ($a=2$, $q=(-1,0)$, one chain with $-3$).

**Status of Theorem H.** It is correct as a conditional statement, but its hypothesis (ii) is used at *short* internal necks. [MS §7] proves the vertex alternative only for $Y$-lengths $\ge T_0$ (its lemma on the vertex test is stated "uniformly over all sufficiently long finite $Y$ seams"). The positive piece is isolated by rational collars inside $B_P$, and at bounded $R$ the energy bound of FL1 is finite, so the same contradiction argument should apply. **PLAUSIBLE** (70%) for (ii), and **PLAUSIBLE** (55–60%) for Theorem H as a whole. The cap necks cannot be shortened this way, since (B2) and $C_W$ use their length (**VERIFIED** as logic). [G] §0(6) says that invariance under shortening "is not available"; Theorem H makes it conditionally available, by the chain inequalities that [G] §8(6) said it would need.

**Route A** (the vanishing at $R\ge\max(R_0(M),T_0(M))$). Beyond (H5) at a fixed $R$, it needs Lemma D, Corollary E and Proposition F (proved), the contradiction arguments of [MS §7] (plausible), and (D4′). Nothing is glued at $R=\infty$. This is the manuscript's design ([MS §5], table of choices; [MS §7], the corollary on the order of choices).

**Route B** (shorten, then vanish). It needs Theorem H, so the vertex alternative at short internal necks, and still long cap necks with Lemma D on them. The vanishing argument at a fixed $R$ does not depend on the internal neck length, so route B gains nothing.

**Not recommended:** a block-by-block analysis at $R=\infty$ (§5.5).

**Recommendation: route A.** Its cost beyond what [S] already assumes: one identity (proved), two contradiction arguments (in [MS §7]), and one clause on the representatives of $\mu(S_i)$.

---

## 7. Corrected statements

**(H5′)** (replaces "uniformly in the neck length" in (H5) of [S]). Choose, in this order: the cap metrics and the constants $C_W$; the exceptional evaluations $\langle\Lambda_0,E_\pm\rangle$; $M$; the tube scale $\epsilon$, the regularizer, the rational isolation lengths and a gradient tolerance; then the length $R$ of the long necks; then the non-gradient perturbations, small in norms that may depend on $R$. Then there is $T_0(M)$ such that, at every $R\ge T_0(M)$, every item of (H5) holds; the items that are genericity statements hold for generic data chosen after $R$. In particular:
- the cap constants depend only on the caps, and (B2) holds;
- the vertex alternative of [R] Prop. 4.2 holds at every $t\in\bar Q$.
In [S] Theorem 4.3 take $R\ge\max(R_0(M),T_0(M))$.

**(D4′)** As in §3.2: the transversality term of each $V_{S_i}$ is continuous for Uhlenbeck convergence off $S_i$ and vanishes near the restrictions of reducible limits with $\langle v,S_i\rangle=0$. This applies to the same representatives used for $\Omega$ and for $\mathcal Z_e$.

**Proposition A** ($C^0$), **Proposition B** (negative part), **Proposition C** (no uniform $L^4$ bound; $Y_{\pm2}$ not an $L$-space, no metric with $\mathrm{Scal}\ge0$), **Lemma D** (identity), **Corollary E** (charge of a neck $\ge-C_Y(1+\nu)$), **Proposition F** (uniform energy on blocks and neck middles): as stated in §2.

**Proposition I** (interior strata). Assume (H5′), (D4′), (E0) and the regularity of the lower strata. At a fixed $R\ge\max(R_0(M),T_0(M))$, the closure of $\mathcal Z_e$ over $\operatorname{int}Q$ consists of $\mathcal Z_e$ and the finitely many points of the link at the points of $\mathcal V(z)\cap M^{w_e}_\kappa(Q)$. Near each of them $\mathcal Z_e$ has $2^{n_a-1}$ ends counted with the sign of the instanton in $o(\Omega,w_e)$, up to a sign $\sigma_0$ fixed by conventions.

**Lemma G** ($\Theta=0$ on copies of $W_B$, $\Theta(B_P)=1$) and the corrected count of §5.4.

**Theorem H** (shortening the internal necks, conditional), as in §6.

---

## 8. Gaps, with confidences

1. **The $R$-independent inputs** (caps, (B2), the vertex alternative on $P$ at every $R\ge T_0$). They rest on the metric family of [MS §6] and the contradiction arguments of [MS §7], whose energy input is Proposition F. **70%.**
2. **Persistence (D4′)** together with transversality on all strata and the requirements at the faces ((D5), the pairing at the lens faces). **85%.**
3. **Compactness over compact subsets of $\operatorname{int}Q$ and regularity of the lower strata in families** (FL1, FL2a with parameters; Feehan's and Teleman's transversality in families). **90%.**
4. **The link with parameters** (Kuranishi model with the family operator; FL2b Lemmas 3.22, 3.27, 3.28 and Prop. 3.29 with $Q$). **85%.**
5. **Proposition C(a)** depends on the integer-surgery formula and on "an $L$-space surgery with positive slope comes from an $L$-space knot", which are cited from the literature, not from a fetched source. **95%.**
6. **Kind (b) after perturbation** needs $I(Y_{\pm2})\ne0$. This is harmless: if it fails, $\Omega=0$ trivially. **90%.**
7. **Compactness as $R\to\infty$** (§5.3), used only inside the contradiction arguments, on completed blocks. **80%.**
8. **Theorem H**: not needed. **55–60%.**
9. **The count at $R=\infty$** (§5.4): not needed. Exclusion under the parameter-local count, up to the spectral terms: **60%.**

---

## 9. Verdict and confidence

The compactification of $\mathcal Z_e$ over the interior of the cube behaves as [S] §4 assumes, at every fixed neck length $R\ge\max(R_0(M),T_0(M))$.
- Lower irreducible levels are excluded by FL2b's count with parameters, provided the jumping-line representatives persist off $S_i$.
- The instanton stratum contributes its link with the factor $2^{n_a-1}$.
- Seiberg–Witten strata and abelian instantons on $X$ are excluded by (B3) and (B2).
- The long $Y_{\pm2}$-necks contribute nothing to the closure at finite $R$, and their only effect is on constants.

FL1's energy bound, and its refinement with the negative part of the scalar curvature, grow linearly in $R$. This happens because $Y_{\pm2}$, for $g(K)\ge2$, is not an $L$-space (now checked in genus two, where the fetched source was silent), carries no metric of nonnegative scalar curvature, and carries three-dimensional Seiberg–Witten solutions. The quantity that is uniformly bounded is the drop of the Chern–Simons–Dirac functional (Lemma D). With it the cap constants and the vertex alternative on $P$ can be fixed before $R$, as the composition law requires.

[C1] is correct in its main lines. My corrections are:
- (i) the support condition becomes persistence;
- (ii) $h$ does not vanish on the tubes, and Proposition F(a) must not use a constant term;
- (iii) $\Theta(B_P)=1$ exactly, so the central-neck count at $R=\infty$ is $I=0$ coarse and $I'=-2$ parameter-local, and check c2(C)'s maximum $8$ is spurious;
- (iv) the existence of perturbed irreducible flats comes from $I(Y_{\pm2})\ne0$, not from [KM-D] alone;
- (v) Theorem H needs the vertex alternative at short necks, which is not in [MS].

None of these changes the recommendation: prove the vanishing at the long necks the composition law needs (route A).

| claim | label | confidence |
|---|---|---|
| Lemma D, Corollary E | VERIFIED | 97% |
| Propositions A, B, F (uniform $C^0$, local, block and neck bounds) | VERIFIED as deductions | 90% |
| Proposition C ($L$-space, no $\mathrm{Scal}\ge0$, no uniform $L^4$ bound) | VERIFIED given the surgery formula | 95% |
| caps and the vertex alternative independent of $R$ | PLAUSIBLE | 70% |
| lower levels $\le1-2\ell$; failure without persistence | VERIFIED | 97% |
| (D4′) available with all other requirements | PLAUSIBLE | 85% |
| link with parameters | PLAUSIBLE | 85% |
| classification (a)–(d), codimensions | VERIFIED / PLAUSIBLE | 90% |
| Lemma G and the count of §5.4 | VERIFIED (arithmetic) / PLAUSIBLE (spectral terms) | 95% / 60% |
| Theorem H | PLAUSIBLE | 55–60% |
| **the compactness, energy and interior-strata part of (H5), as [S] Thm. 4.3 needs it, at $R\ge\max(R_0(M),T_0(M))$** | PLAUSIBLE | **about 72%** |

---

## 10. Report of the checks

### 10.1 Citations, checked against the LaTeX

Numbers were recomputed with `num.py` (theorem-like environments sharing the section counter) and `numeq.py` (equations numbered within sections) in `round4/compactness-final-checks/`.

| cited in [C1] | found | verdict |
|---|---|---|
| FL1 Lemma 4.1(1b) | `lem:BWDirac`, Weitzenböck (1b) for $\mathrm{SO}(3)$ connections | correct |
| FL1 Lemma 4.2 | `lem:L21AaprioriEstAPhi`: $\|\Phi\|_{L^4}$ via $\|R\|_{L^2}$, $\|F^+\|_{L^2}$ | correct |
| FL1 Lemma 4.4 and "the remark after it" | `lem:C0EstFAPhi`; the formula for $K_3$ is Remark 4.6 (after Cor. 4.5) | correct |
| FL1 Thm. 1.1, Thm. 1.3, Def. 4.19, Thm. 4.20 | `thm:Compactness`, `thm:Transversality`, `defn:UhlenbeckTop`, `thm:SeqCompact` | correct |
| FL1 §1.1.2 | "Uhlenbeck compactness": lower levels are not products under holonomy perturbations | correct |
| FL2a Thm. 2.12, Thm. 2.13, Prop. 2.15, Prop. 3.1, Cor. 3.6, Lemma 3.12 | compactness (closure in $\bigsqcup\mathcal M_{\mathfrak t_\ell}\times\mathrm{Sym}^\ell$), transversality, compactness of SW spaces, stabilizers, Kuranishi model at instantons, reducibles solve SW with $\eta=F^+_{A_\Lambda}$ | correct |
| FL2b (3.20), (3.21), (3.24), (3.25), (3.26), (3.62), (3.64) | dimension $d_a+2n_a$; $d_a,n_a$ (with the misprint $\chi+2\sigma$); bounds 5 and 4; $\deg z+2\delta_c$; the one-manifold; lower-level reducibles | correct |
| FL2b Lemma 3.15, Cor. 3.18, Lemma 3.21, Lemma 3.22, Lemmas 3.24, 3.25, 3.27, 3.28, Prop. 3.29, Lemma 3.32, Thm. 3.33 | as cited | correct; Cor. 3.18 counts the background only (product strata) |
| [KM-D] Thm. 1 | `thm:hRP3`: non-cyclic $\mathrm{SU}(2)$ image for $|r|\le2$ | correct (representations only) |
| [OS-Q] `thm:RatSurgeryLSpace` | $t_i(K)=0$ for $|i|>p/2q$ | correct; at $p/q=2$ it gives only $g\le2$ |
| [MS §7]: the local integrated estimate, the charge of a finite $Y$-middle, retained energy, cap constants, period inequality, vertex test, order of choices | read | correct attributions; constants agree ($d_*=\frac14$, $c_*=\frac12$) |
| [MS §9]: compactness on bodies, the energy cut-off formula, exact supports and incidence | read | position dependence confirmed; persistence rule stated there |
| [MS §6]: metric family; uniform collar and satellite models | read | scalar curvature bounded below; tubes of length $O(\epsilon^{-1})$ |
| [R], [G], [S], [St] items | read | correct, with the remarks in §§3.2, 6 |

### 10.2 Computations (all in `round4/compactness-final-checks/`)

- **f1_identity.py.** A finite-dimensional model of the neck equations with a quartic-plus-trigonometric $\mathrm{CS}$, a bounded $\mathcal W$ (sum of cosines), both signs $\sigma$ and non-gradient errors $r,e$.
  - Part 1: the pointwise identity of Lemma D at 200 random states, with derivatives along the flow taken by central differences. Maximal relative discrepancy $4.7\cdot10^{-10}$.
  - Part 2: the integrated identity along trajectories (RK4 with Simpson's rule). Discrepancies $9.1\cdot10^{-10},\,5.7\cdot10^{-11},\,3.5\cdot10^{-12}$ at steps $T/400,T/800,T/1600$, a fourth-order decrease, so the identity is exact. Corollary E's lower bound holds: $5.46\ge-12.20$ and $1.30\ge-7.51$.
  - Part 3: with $c<0$ the integrand $\|\dot a\|^2+2c\|\dot\Phi\|^2$ is negative at 130 of 200 states.
- **f2_quartic.py.** $\langle(\Phi\Phi^*)_{00}\Phi,\Phi\rangle=\|\pi_{00}(\Phi\Phi^*)\|^2_{HS}=\frac14(s^4+t^4)+\frac52s^2t^2$ on 20,000 random $\Phi$, including rank-one ones; error $3\cdot10^{-15}$; minimum ratio to $|\Phi|^4$ equal to $\frac14$.
- **f3_theta_blocks.py.** Exact arithmetic on the lattices of a copy of $W_B$ and of $P$, for all $e$.
  - $\Theta(W_B)=0$ for both chamber-compatible lifts, and $-2$ for the lift $(4,2)$.
  - $\Theta(P)=1+\frac12(e_a-e_b)$, $\Theta(W_H)=1$, $\Theta(B_P)=1$.
  - At $R=\infty$: the maximum projected index is $0$ (keeping parameters) and $-2$ (parameter-local) over all chains at spacing four, attained by a single copy of $B_P$.
- **f4_counts.py.**
  - (A) $\dim\mathcal Z_e=1$; lower levels $\le1-2\ell$ in the product and position-dependent regimes; $1$ at level one when $\mu(S_i)$ is released throughout $\nu S_i$.
  - (B) zero-spinor levels $-4\ell$ ($-2\ell$ with the weaker rule).
  - (C) Kuranishi dimensions and the link count $2^{n_a-1}$.
  - (D) $D(\zeta)=1-3c$ for all assignments of kinds on up to five necks.
  - (E) one-parameter $J$-faces: chain bound $-2$ suffices, $-3$ fails (minimal configuration $a=2$, $q=(-1,0)$, one chain); at fixed $R$, $-3$ suffices and $-4$ fails.
- **f5_lspace.py.** For all Alexander polynomials of $L$-space form with $1\le g\le5$, the hat mapping cone of the integer-surgery formula gives $\operatorname{rk}\widehat{HF}(S^3_2(K))=2,4,8,12,16$ for $g=1,\dots,5$ (an $L$-space only for $g=1$), and rank $2g-1$ at slope $2g-1$. It also records that [OS-Q]'s theorem at slope $2$ gives only $g\le2$.
- **[C1]'s files**, executed again. `c1_csd_identity.py` reproduces its stated discrepancies ($1.34\cdot10^{-3}$, $3.35\cdot10^{-4}$, $8.38\cdot10^{-5}$, ratio $4.0$). `c2_counts.py` reproduces (A), (B) and (C). Its (C) prints a maximum projected index $8$ at $(r_W,r_M)=(6,4)$ with $\Theta(B_P)=0$, a value that does not occur (f3).

### 10.3 Attempted counterexamples

1. **A level-one limit with its point of concentration in $\nu S_i\setminus S_i$.** It defeats the count if the transversality term of $V_{S_i}$ is not Uhlenbeck-continuous (expected dimension $1$). It is excluded by (D4′). This was found by [C1]; I sharpened the remedy.
2. **The negative-part bound along a $Y$-neck.** It is defeated by any solution staying near a critical point of kind (c) (Prop. C(d)). The cure is Lemma D. No counterexample to Lemma D exists: it is an identity.
3. **A circularity of choices.** The isolation lengths on $P$ would depend on $R$, and $R_0$ on the isolation lengths. This is prevented by Proposition F; I found no other $R$-dependent input.
4. **Seiberg–Witten solutions on $X$ glued from blocks matched at kind (c).** They glue to reducible solutions on $X$, since the relative phase is a gauge transformation preserving the splitting, and are excluded by (B3) at finite $R$. No counterexample.
5. **Central $Y$-necks next to a copy of $B_P$ carrying an abelian instanton at energy $\frac12$.** $I=0$ coarse, $I'=-2$ parameter-local, at $R=\infty$ only. Not a counterexample to route A.
6. **Shortening.** With chain bound $-3$, an anti-self-dual component with $q=-1$ at an isolated $R$ beside a chain with $\varepsilon_I=-3$ gives a one-parameter family that ends on a $J$-face (f4(E)). At spacing four the exact minimum is $-2$, so this does not occur. At short necks the vertex alternative itself is unproved, which is the weak point of Theorem H.
7. **Orientation of the link depending on $e$.** Each $e$ uses $O^{\rm asd}(\Omega,w_e)$; the $e$-dependence is moved to the lens comparison. No counterexample here; the comparison itself is the faces' (A5).
