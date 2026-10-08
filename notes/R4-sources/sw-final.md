# Seiberg–Witten strata in the closure of $\mathcal Z_e$: the unbroken manifold, the positive pieces and the caps

*Round 4, referee's final version. It replaces `round4/sw-1.md` (cited as [SW1]) as the record. Subject: the Seiberg–Witten strata $\iota(M_{\mathfrak s})\times\mathrm{Sym}^\ell$ (reducible connection, nonzero spinor), with their zero-spinor parts where relevant, that could meet the closure over $\bar Q$ of the cut-down one-manifold $\mathcal Z_e=\mathcal V(z)\cap\mathcal W^{n_a-1}\cap\mathcal M^{*,0}_{\mathfrak t_e}(Q)/S^1$ of `statements.tex` §4, for $X=X(\Pi_M)$ and the family $g^R_t$, on $X$ and on the pieces of broken limits. Mixed limits containing abelian instantons are treated elsewhere; I touch them only where a count used here is shared with them. My computations are in `round4/swfinal-checks/`; the report of the checks is §11.*

**Labels.** **VERIFIED**: proved here; or read in the source with the statement or equation number recomputed from its LaTeX counters; or confirmed by an exact computation listed in §11. **PLAUSIBLE**: standard in kind, or supported by a written argument whose structure I checked but whose analysis I did not redo. **SPECULATIVE**: unproved, supported only by numerical evidence, or a guess.

**Sources.** [S] `statements.tex` (Round 3), §§3–4, (H1)–(H5). [St] `strategy.tex`, Theorem 2.1. [R] `notes/R3-sources/relation-final.md` (hypotheses (A1)–(A7), conditions (B1)–(B5), Lemma 1.3, Prop. 4.2, Lemmas 4.3–4.6). [G] `notes/R3-sources/gluing-final.md` (Theorem A′). [CF] `round4/compactness-final.md` (Lemma D, Corollary E, Proposition F, Proposition C). [M2] `round4/mixed-2.md` (Propositions 2.6, 3.1, 3.2, Theorem 3.3). [SW1] `round4/sw-1.md` and its computations `round4/sw1-checks/`. [MS] the manuscript `src/06-geometry.tex`, `07-estimates.tex`, `08-indices.tex`, cited by section and by the name of the statement. [T3] `notes/T3-wallcrossing.md`. [Num] `numerology.tex`. FL1 = dg-ga/9710032, FL2a = math/0007190, FL2b = dg-ga/9712005, Memoir = math/0203047 (all in `lit/`).

**Notation.** As in FL2b §3 and [S] §4. Spin$^u$ structures $\mathfrak t_e$ with $w_2(\mathfrak t_e)\equiv w_e=w_0+\sum_ie_i\mathrm{PD}[S_i]$, $\Lambda_e=c_1(\mathfrak t_e)$, $p_1(\mathfrak t_e)=-4\kappa$, $d_a=8\kappa-3(1+b^+)$, $\Theta=\frac14(\Lambda^2-\sigma)$, $n_a=\Theta-\kappa$. $\mu_p(z)$ is represented by $\mathcal V(z)$ (jumping-line divisors $V_{S_i}$ and cap representatives), $\deg z=d_a+n$; $\mu_c$ by $n_a-1$ sections of $\mathbb L_{\mathfrak t}$ (FL2b (3.10), (3.12)) sampling the spinor on every piece ([R] §1.3); the link of the instanton stratum is $\{\|\Phi\|^2_{L^2}=\varepsilon\}$. At a reducible pair, $E=L_1\oplus L_2$ with the spinor in $W^+\otimes L_1$, and
$$v=c_1(L_1)-c_1(L_2)\equiv w\pmod 2,\qquad K=c_1(\mathfrak s)=\Lambda+v,\qquad \ell=\kappa+\tfrac14v^2,$$
which is FL2b Lemma 3.32 with (3.64), and Memoir (2.3.14). A component of an ideal limit (FL2a Prop. 3.1, which is local to a component) is called a *component in $\mathcal M^{*,0}$* (irreducible connection, nonzero spinor), an *anti-self-dual component* (irreducible, zero spinor), a *Seiberg–Witten component* (reducible, nonzero spinor) or an *abelian instanton* (reducible, zero spinor). A *chain* is a maximal set of consecutive reducible components between broken three-spheres. For a component $j$, $q_j=d_a(\hat\Gamma_j)+p_j-2s_j-z_j$ is its cut-down anti-self-dual index and $i_j=q_j+2n_a(\hat\Gamma_j)$ its monopole index ([R] Lemma 1.3); for a set $\Gamma$ of components I write $\varepsilon_I(\Gamma)=\sum_{j\in\Gamma}(q_j+4)$ and $\delta(\Gamma)=\sum_{j\in\Gamma}(i_j+4)$, the two *index sums* of $\Gamma$. On the positive piece $P_j\cong\mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2$ between $J_j$ and $J_{j+1}$: basis $G,U,T_1,\dots,T_4$ with form $\left(\begin{smallmatrix}2&1\\1&0\end{smallmatrix}\right)\oplus(-I_4)$; near halves $F_r=G-\sum T_b$ (of $S_j$) and $F'_l=G-2U$ (of $S_{j+1}$); $X_1=-S_j$, $X_2=S_{j+1}$; $H_I=U+\frac14\sum_{i\in I}X_i$; $x=v\cdot G$, $u=v\cdot U$, $t_b=v\cdot T_b$, $d_i=v\cdot X_i$, $z_I=v\cdot H_I$, $\lambda_I=\Lambda\cdot H_I$; far halves $h_1=v\cdot F_{l,j}$, $h_2=v\cdot F_{r,j+1}$ in the neighbouring negative pieces; bits $(e,f)=(e_j,e_{j+1})$. The *block* $B_j=W_B^{(j)}\cup W_H\cup W_B^{(j+1)}$ contains $P_j$ and the plumbing $C_2=\nu(X_1\cup U\cup X_2)$; its two internal $Y_{\pm2}$-necks have fixed length, and it meets the rest of $X$ along necks of length $R$. The manuscript parametrizes each interval by $t_i\in[-3,3]$ (three-sphere face at $-3$, lens face at $+3$, period coefficient $\alpha_i=0$ for $t_i\le0$ and $\frac14$ for $t_i\ge1$); [S] uses $[-1,1]$. Nothing depends on the choice.

---

## 0. Findings

1. **Architecture (corrected).** A Seiberg–Witten stratum can be kept out of the closure of $\mathcal Z_e$ in exactly three ways: on unbroken $X$ by incidence and energy; at broken limits without a component in $\mathcal M^{*,0}$ by the index identity $\sum_j(q_j+4)=4$ and lower bounds for $\varepsilon_I$; at broken limits with a component in $\mathcal M^{*,0}$ by the dimension of the $\mathcal M^{*,0}$-part, obtained by forgetting every other component ([M2] Prop. 3.1, re-derived in §5.2), or, where that count fails, by coupled regularity. **VERIFIED** as logic. [SW1] used coupled regularity ([R] (A3)) for every limit with a component in $\mathcal M^{*,0}$; that is unnecessary for interior Seiberg–Witten chains and short cap chains. [M2] claims it is never needed at Seiberg–Witten components; that is wrong for long Seiberg–Witten components containing a blown-up cap (item 12).
2. **Reducible strata and indices.** A Seiberg–Witten component solves the Seiberg–Witten equations for $K=\Lambda+v$ with $\eta=F^+_{A_\Lambda}$ (FL2a Lemma 3.12, Lemma 3.13, Remark 2.14). Its tangential index is $d_s=\frac14(K^2-2\chi-3\sigma)$ (FL2a (2.63)), the monopole index splits as tangential plus normal, each level adds $6$, and $d_s=n_a+\ell+\frac12\Lambda\cdot v-(1+b^+)$. **VERIFIED** (symbolic; every FL number recomputed from the LaTeX, §11.1).
3. **Phase sections.** A Seiberg–Witten point is fixed by the circle up to the gauge transformation $\mathrm{diag}(\zeta,\zeta^{-1})$ (Memoir (2.3.13)), so every section of $\mathbb L_{\mathfrak t}$ vanishes there; at a broken limit the $\mu_c$-sections restrict to the sum of the contributions of the components in $\mathcal M^{*,0}$. No dimension count on $\mathcal W$ can cut a Seiberg–Witten stratum. **VERIFIED.**
4. **Unbroken $X$.** Incidence gives $\ell\ge T(v)$ (with either convention for the representatives near a three-sphere face, §2.1). The projection form of [S] Prop. 4.2 is true but useless on $P$: $(\pi v)_P^2$ is unbounded on classes allowed by the control on $P$ ($80,360,1520,\dots$). The inequality that works reserves the far halves: $-\frac14v^2+T(v)\ge\frac12(n-m)-C$, and it is sharp (exact minima $\frac12(s^-+m)$ on nine chains, recomputed independently). With $8\kappa=n+3m+c_\kappa$ it gives $\ell-T(v)\le\frac18(-5M-3p+c_\kappa)+C<0$. **VERIFIED** as a deduction from the inputs of §2.3. At spacing one the inequality fails without bound (minima $-7,-\frac{29}2,-\frac{43}2$ on $NPPN$, $NPPPN$, $NPPPPN$ in a bounded range), as it must.
5. **What controls the set of $\mathfrak s$.** Three local inequalities, each uniform in $t\in\bar Q$ and $R\ge T_0(M)$: definiteness on negative pieces; the vertex alternative (or $u=0$) on each positive piece; $v_W^2,K_W^2\le C_W$ on the caps. They hold for every Seiberg–Witten solution in the charge window, whatever $\mathfrak s$, and the lattice inequality then excludes every $\mathfrak s$ at once. No basic class, and no finiteness of the set of $\mathfrak s$, is used, except inside the proofs by contradiction of the local inequalities. **VERIFIED** as logic.
6. **The band and the toric metrics.** The Weitzenböck band $(v\cdot H)(K\cdot H)<0$ (nonzero spinor), $v\cdot H=0$ (zero spinor) is re-derived with signs. The scalar curvature of the manuscript's Hessian metrics was computed from scratch (Christoffel symbols of the four-dimensional metric) and agrees *exactly* with Abreu's formula $\mathrm{Scal}=-\partial_i\partial_j(2M^{-1})_{ij}$ and with the manuscript's closed form at ten rational configurations (Fubini–Study: $12$; product tube: $4$); I also derived the closed form by hand. Positivity follows by Schur's theorem. **VERIFIED** (upgrades [SW1], which compared decimal approximations).
7. **Vertex alternative and lattice lemma.** Convexity (band at a period of $\Pi\setminus\{U\}$ forces the alternative at a supported nonempty vertex) holds in all $1{,}240{,}467$ band and $35{,}972$ wall instances checked exactly; the lattice lemma ($Q_I\le-2$, or $\le2$ in the exception with the insertion missed) follows from three algebraic identities and is confirmed on $8.9$ million instances. **VERIFIED.** *Correction to [SW1] Prop. 3.5(b):* "$z_I>0$ when $u<0$" is false when the limiting spinor vanishes at a period with $\theta_\varnothing=0$ (a saturated lens side; $1680$ instances); there the abelian alternative $z_I\ge0$ holds, which gives $Q_I\le-4$. Harmless.
8. **The period along the family.** The relevant period is that of $C_2$. It lies in $\Pi\setminus\{U\}$ on the positive-width region (including every face and corner involving a lens neck and every face with one stretched three-sphere), and is forced to the cusp $U$ when both neighbouring three-spheres are stretched; there the long $U$-tube forces $u=0$. **VERIFIED** (support computation) / **PLAUSIBLE** (construction, [MS §6]).
9. **New: the exact double three-sphere corner needs no tube.** *Lorentzian lemma:* on the closed $P$ with any metric of nonnegative scalar curvature (positive somewhere), every Seiberg–Witten class with $d_s\ge0$ has $v_P^2\le-2$, because a band class with $v_P^2\ge0$ and $K^2\ge4$ would force $\Lambda_P^2\ge K^2\ge4$, while $\Lambda_P^2\le2$ for all bits. So an isolated $P$ with no parameter, carrying any metric of nonnegative scalar curvature, costs $\ge\frac12$ whatever its period. **VERIFIED** (proof; exact check on $852{,}276$ classes). [SW1] §3.8(iii) ("no open set of corner periods works", SPECULATIVE) omitted the realizability condition $d_s\ge0$: with it, $20{,}000$ of $20{,}000$ random periods work. The tube is needed only for uniformity on the approach to the corner, where components carry parameters and far halves; there [SW1]'s numerics apply a fortiori. **VERIFIED** (numerics) / the necessity there **SPECULATIVE**.
10. **Uniformity in $R$; three-dimensional Seiberg–Witten solutions.** The block metrics do not depend on $R$, block energies are uniform in $R$ by the Chern–Simons–Dirac identity ([CF] Prop. F), and the cap constant uses only local bounds on unit strips and the exponential decay of the cap's harmonic forms. The solutions of the three-dimensional equations on $Y_{\pm2}$ ($Y_{\pm2}$ is not an $L$-space) create no stratum at finite $R$ and affect no count used here. **VERIFIED** as logic; the analytic inputs **PLAUSIBLE**.
11. **Caps.** No abelian instanton contains a cap (generic cap period; $\langle w,A_\pm\rangle$ odd) and $v_W^2,(\Lambda_W+v_W)^2\le C_W$ with $C_W$ independent of $M$, $\langle\Lambda_0,e_\pm\rangle$ and $R$. **PLAUSIBLE** (80%). Large odd $\lambda_\pm=\langle\Lambda_0,e_\pm\rangle$ is needed only for short end Seiberg–Witten components, where $d_s+p\ge0$ bounds $|K\cdot e_\pm|$ (the condition $d_s+p+4\ell\ge0$ of [MS §8] is weaker and also suffices); the count needs only $q\ge0$ there and the blow-up gives $q+4\ge8$. **VERIFIED** (arithmetic).
12. **New: the price of the blow-up.** A Seiberg–Witten component containing a blown-up cap on a *long* end component has monopole index as low as $i\approx-\lambda^2/8$ with no positive piece (at length $\approx\frac9{64}\lambda^2$) and $i\approx L-\frac12\lambda^2$ with positive pieces in the small-width region of bits $(1,0)$, which supply $K_P^2=4-4x$ at cost $\frac12$. Next to a component in $\mathcal M^{*,0}$, the $\mathcal M^{*,0}$-part of such a limit then has expected dimension $D\approx-3-i\gg0$ ($330$, $1280$, $5056$ for $\lambda=51,101,201$). Counting does not exclude these limits; coupled regularity at the Seiberg–Witten component does. This corrects [M2] Prop. 3.2(d), whose bound $|v\cdot e_\pm|\ge\lambda_\pm-B$ is proved only for short end components. **VERIFIED** (count) / existence of such components **SPECULATIVE**.
13. **Broken limits.** Without a component in $\mathcal M^{*,0}$: chains have $\varepsilon_I\ge-2$, threshold $-3$, minimum attained by an isolated $P$. With one: interior Seiberg–Witten chains ($\delta\ge-2$) and short cap chains ($\delta\ge2$) are excluded by the $\mathcal M^{*,0}$-count with single-component regularity only; long cap chains and low-index anti-self-dual components, all in end regions fixed before $M$, need coupled regularity. **VERIFIED** as deductions; inputs as labelled.
14. **Missed strata.** None found. Twisted ($O(2)$) reducibles cannot occur ($H_1=0$ on every piece, including $X\setminus\nu S_i$); lens caps carry no Seiberg–Witten component (positive scalar curvature, anti-self-dual background); auxiliary collars and $Y_{\pm2}$-necks do not break at finite $R$; trivial flat connections on pieces are abelian instantons with $v=0$ and are covered. **VERIFIED** / **PLAUSIBLE** as marked in §7.
15. **Corrections to `statements.tex`.** (a) Replace the projection form Prop. 4.2 by the inequality with reserved far halves (Prop. D below). (b) §3 describes $g^R_t$ as the interval $G$ in $t_i$ on each copy of $W_B$; the control on $P$ needs the coupled two-parameter toric family on each block ([MS §6]), so the composition law must be stated for that family ([G] Theorem A′). (c) "$\langle\Lambda_0,e_\pm\rangle$ large excludes their Seiberg–Witten classes" holds only for short end components and creates the residual of item 12. (d) (H5) should name the residual coupled regularity in the end regions.
16. **Verdict.** The Seiberg–Witten exclusion in scope is a correct deduction from: the control on $P$ uniformly over $\bar Q$ and $R\ge T_0$, the cap estimates, incidence, short-end regularity, single-component regularity of $\mathcal M^{*,0}$-strata, and coupled regularity in the end regions. Confidence that, by this route, the strata in scope are absent from the closure of $\mathcal Z_e$ for $u$ and large $M$: **about 35%** (25–45%); without the end-region residual: **about 55%**. [SW1]'s 60% exceeded its own 55% for an indispensable ingredient and missed item 12.

---

## 1. The reducible strata and what can exclude them

### 1.1 Equations and indices

FL2a Lemma 3.12 (`lem:RestrictionOfPU2MonopoleEquation`): a pair reducible with respect to $V=W\oplus W\otimes L$, with spinor $\Psi\oplus0$, solves the $\mathrm{PU}(2)$ monopole equations iff $(B,\Psi)$ solves FL2a (2.55) with $\eta=F^+_{A_\Lambda}$ (FL2a (2.56)); Remark 2.14 notes that this $\eta$ is not generic; Lemma 3.13 identifies $\iota(M_{\mathfrak s})$ with the reducible locus when $w_2(\mathfrak t)\ne0$; Prop. 2.16 makes $M^0_{\mathfrak s}$ smooth of dimension $d_s$ for fixed $\eta,\vartheta$ and generic $\tau$, and Prop. 2.15 gives compactness for $\|\tau-\mathrm{id}\|_{C^0}<\frac1{64}$. **VERIFIED** (read; numbers recomputed, §11.1). With $F_B=i(\beta+D)$, $[\beta/2\pi]=\Lambda$, $[D/2\pi]=v$, the curvature equation reads $\rho(iD^+)=(\psi\psi^*)_0$, and the active line has $c_1=K=\Lambda+v$. **VERIFIED.**

On a closed-up piece with $b_1=0$ (`c1_index.py`, **VERIFIED** symbolically):

- tangential index $d_s=\frac14(K^2-2\chi-3\sigma)$ (FL2a (2.63));
- normal part: the off-diagonal anti-self-dual complex on $L_1L_2^{-1}$, real index $-2v^2-2(1+b^+)$, and the Dirac operator on $W^+\otimes L_2$, real index $\frac14((\Lambda-v)^2-\sigma)$;
- $d_s+\text{normal}=d_a+2n_a$ at level $0$; each unit of level adds $6$;
- $d_s=n_a+\ell+\frac12\Lambda\cdot v-(1+b^+)$.

| closed-up piece | $2\chi+3\sigma$ | constraint on $K$ | $d_s$ |
|---|---|---|---|
| $P$ | $4$ | none | $\frac14(K^2-4)$, even |
| negative piece $\hat N$ (form $\langle-1\rangle^2$) | $2$ | $K^2\le-2$ | $\le-1$, odd |
| $r$ negative pieces joined along three-spheres | $4-2r$ | $K^2\le-2r$ | $\le-1$ |
| $X$ | $4+4b^++\sigma$ | — | $d(\mathfrak s)$ |

In a family with $p$ parameters the space has dimension $d_s+p$ when regular, and $d(\mathfrak s)+n$ on $X$ over $Q$. **VERIFIED.**

### 1.2 Phase sections vanish on Seiberg–Witten points

The circle acts on $\mathcal C_{\mathfrak t}$ by scalars on the spinor, and $\mathbb L_{\mathfrak t}$ is associated to it with weight two (FL2b (3.10)). At $(A_1\oplus A_2,\Psi\oplus0)$ the gauge transformation $\mathrm{diag}(\zeta,\zeta^{-1})$, which is the image of $\zeta$ under the inclusion of gauge groups of Memoir (2.3.13), fixes the connection and multiplies the spinor by $\zeta$; so the point is a fixed point of the circle on the quotient (FL2a Prop. 3.1(2)), and every equivariant function of weight two vanishes there. At a broken limit the gauge groups of the pieces are independent (the limits on $S^3$ have stabilizer $\mathrm{SU}(2)$), and the $\mu_c$-sections are sums over pieces of such functions; so they restrict to the sum of the contributions of the components in $\mathcal M^{*,0}$. **VERIFIED.**

So $\mathcal W$ contains every Seiberg–Witten stratum and cuts nothing there. This is why Feehan and Leness either exclude these strata by level (FL2b Thm. 3.33(a), hypothesis (3.68)) or compute their links (FL2b Thm. 3.33(b), FL2a §§3.4–3.5). **VERIFIED** as logic.

### 1.3 The three mechanisms

- **Unbroken limits** (interior parameters and lens faces): incidence $\ell\ge T(v)$ against the energy inequality (§2).
- **Broken limits without a component in $\mathcal M^{*,0}$**: the identity $\sum_j(q_j+4)=4$ ([R] Lemma 1.3), $q_j\ge0$ at regular anti-self-dual components, $\varepsilon_I\ge-2$ on chains, $q+4\ge8$ at outer Seiberg–Witten components (§5.1).
- **Broken limits with a component in $\mathcal M^{*,0}$**: the dimension $D$ of the $\mathcal M^{*,0}$-part (§5.2). Where $D\ge0$ because a forgotten component has very negative monopole index, nothing short of coupled regularity (or an obstructed gluing theorem) excludes the limit (§5.3).

**VERIFIED** as logic.

### 1.4 Strata that do not occur at all

- *Twisted reducibles.* A reduction of the $\mathrm{SO}(3)$ bundle to $O(2)$ not coming from a splitting needs a nontrivial real line bundle (FL2a Lemma 3.5, after Kronheimer–Mrowka), i.e. $H^1(\cdot;\mathbb Z/2)\ne0$. The pieces $\hat Z_j$ are simply connected ([R] §1.1). For $X\setminus\nu S_i$: each $S_i$ has odd pairing with a class of $X$ ($U$ if $S_i$ is adjacent to a positive piece, $a=\frac12(F_r+F_l)$ of a neighbouring negative piece otherwise), so $H^2(X)\to H^2(\nu S_i)\cong\mathbb Z$ is onto and $H_1(X\setminus\nu S_i)\cong\mathrm{coker}=0$. **VERIFIED**; the same argument for the pieces at mixed faces **PLAUSIBLE**.
- *Lens caps.* On a separated $\hat\nu S_i$ the metric has positive scalar curvature and the background is harmonic and anti-self-dual ([MS §7], the theorem controlling reduced classes, (iii)); the Weitzenböck formula forces $\Phi=0$. **VERIFIED** as logic.
- *Long necks.* At finite $R$ no $Y_{\pm2}$-neck breaks ([CF] §5.2), and the auxiliary rational collars of [MS §6] have finite length ("no added boundary faces", [MS §6], the theorem on the metric family). **VERIFIED** (reading).

---

## 2. The unbroken manifold

### 2.1 Incidence

**Lemma C.** Let points of $\mathcal Z_e$ converge to a Seiberg–Witten point $(A,\Phi,\mathbf x)$ of class $v$ at level $\ell$, at a parameter off the three-sphere faces. Then every insertion that the reducible does not meet carries a point of $\mathbf x$ (at a lens face: a unit of cap charge beyond the reference filling). Distinct insertions need distinct points, so $\ell\ge T(v)$, the number of insertions not met.

*Proof.* Off $\mathbf x$ the convergence is $C^\infty$ after gauge (FL1 Def. 4.19, Thm. 4.20). If $\mathbf x$ misses $S_i$, the restrictions converge in $C^0$ on $S_i$; the perturbed representative is closed under this convergence ([CF] (D4′)), so the limit lies in it. For a reducible, $E|_{S_i}\otimes(\det)^{-1/2}=\mathcal O(k)\oplus\mathcal O(-k)$ with $2k=|\langle v,S_i\rangle|$, since $\langle w_e,S_i\rangle\in\{0,-4e_i\}$ is even. ∎ **VERIFIED** given (J1), (J2), (D4′).

*Which insertions are met.* With the whole-sphere divisor $V_{S_i}$ at every interior parameter ([S], [R] (J1)–(J4)), $S_i$ is met iff $\langle v,S_i\rangle\ne0$. With the manuscript's convention, which switches a sphere to the two-half rule for $t_i<0$ ([MS §8], the definition of admissibility (ii)), a switched sphere is met iff one half evaluation is nonzero. In both conventions *a met sphere has a nonzero even half evaluation*, which is all §2.3 uses. At a lens face the sphere lies in the cap: with the minimal trace filling ($d=\langle v,S_i\rangle=\pm2$, charge $\frac14$) it is met; at a central state with $d=0$ it is not, and needs cap charge. The two minimal fillings give classes $v^\pm=v^\mp\mp\mathrm{PD}(S_i)$ with $(v^+)^2=(v^-)^2$, so $\ell$ does not depend on the choice. **VERIFIED** (algebra) / reference fillings **PLAUSIBLE** ([MS §8]).

### 2.2 The projection form of [S] Prop. 4.2 is not enough

[S] Prop. 4.2, $-\frac14v^2\ge-\frac14(\pi v)^2+\frac12\#\{i:\langle v,S_i\rangle\ne0\}$, is true: the $2n$ halves are pairwise orthogonal of square $-2$ (also the two near halves in $P$, $F_r\cdot F'_l=0$), and their evaluations are even. **VERIFIED** (`c2_lattice.py`). But on $P$, $(\pi v)_P^2=v_P^2+\frac12((v\cdot F_r)^2+(v\cdot F'_l)^2)$ is unbounded on classes allowed by the control on $P$: bits $(0,0)$, $u=1$, $t=(1,0,1,0)$, $x=10,20,40$ give $80,360,1520$, with $z_{12}=\frac12<|\lambda_{12}|=1$. **VERIFIED** (`c5_periods.py`). The far halves pay for the indefinite square, and must be reserved.

### 2.3 The inequality with reserved far halves

**Proposition D.** Assume, for a Seiberg–Witten point on $X$ at $t$ (lens faces filled by reference connections): on every positive piece, $u=0$ or the vertex alternative (Theorem F(b)) at some set $I$ of whole sides; on each cap, $v_W^2\le C_W$; positive pieces at mutual distance $\ge2$ and at distance $\ge L_*$ from the caps. Then
$$-\tfrac14v^2+T(v)\ \ge\ \tfrac12(n-m)-C,\qquad C=\tfrac14(C_{W_-}+C_{W_+}).$$

*Proof.* $H^2(X;\mathbb Z)$ splits orthogonally along the three-spheres $J_i$, so $-v^2$ is the sum of: $\frac12(h_r^2+h_l^2)$ over negative pieces (their halves span them rationally); $-v_P^2$ over positive pieces; $-v_W^2+(v\cdot e)^2+\frac12h_0^2\ge-C_W$ over the two end pieces (old cap, exceptional summand, trace half). Group the terms:

- each positive piece with the far halves of the sides in $I$ contributes $-Q_I=-v_P^2+\frac12\sum_{i\in I}h_i^2\ge2$ (Lemma 3.3 below), or $\ge-2$ in the exception, where the insertion on the side in $I$ is missed and adds $1$ to $T$; if $u=0$, $-v_P^2\ge2$;
- each of the $n-2m$ spheres not adjacent to a positive piece is met through a nonzero half (contributing $\ge2$) or adds $1$ to $T$;
- far halves belong only to adjacent spheres, halves of non-adjacent spheres are never far halves, and at spacing $\ge2$ no far half is reserved twice.

Hence $-v^2+4T\ge2(n-2m)+2m-C_{W_-}-C_{W_+}$. ∎ **VERIFIED** as a deduction. Sharpness: the exact minimum of $-\frac14v^2+T(v)$ over classes on the chains $NN$, $NNN$, $NPN$, $NNPNN$, $NPNNNPN$, $NNPNNNPNN$, $NPNPN$, $NPNNPN$, $NPNNNPNNNPN$ (every sphere whole, parity on negative pieces, the vertex alternative or $u=0$ on positive pieces, all bits) equals $\frac12(s^-+m)$ in every case, with the strengthened alternative as well (`c6_chains.py`, a recursion along the chain written independently of [SW1] and [R]). **VERIFIED.** At spacing one the minimum is unbounded below ($-7$, $-\frac{29}2$, $-\frac{43}2$ on $NPPN$, $NPPPN$, $NPPPPN$ within the computed range), as [Num] §5 predicts. **VERIFIED.**

### 2.4 The conclusion on unbroken $X$

**Theorem E.** Under the inputs of Prop. D at every $t\in\bar Q$ off the three-sphere faces and every $R\ge T_0(M)$, no Seiberg–Witten stratum of $X$, at any level, meets the closure of $\mathcal Z_e$ for $u=(\phi_*B)^3HB$ and large $M$.

*Proof.* Lemma C and Prop. D give $\kappa=\ell-\frac14v^2\ge T(v)-\frac14v^2\ge\frac12(n-m)-C$. With $8\kappa=n+3m+c_\kappa$, $c_\kappa=\deg z_C+3+3b_0$ ([R] Prop. 4.1), this says $7m-3n+c_\kappa+8C\ge0$, i.e. $-5M-3p+c_\kappa+8C\ge0$ for $n=4M+p$, $m=M$: false for large $M$. ∎ **VERIFIED** as a deduction (`c1_index.py`). Per period $8n_a$ rises by $1$ and the bound on $8(\ell-T)$ falls by $5$; a uniform loss of $\delta$ per positive piece (in $-\frac14v^2$) is absorbed iff $\delta<\frac58$. **VERIFIED.**

Abelian instantons on $X$ contain both caps and are excluded by §4.1. **PLAUSIBLE** (85%).

### 2.5 What controls the set of $\mathfrak s$

- **No basic classes.** $X$ is a connected sum along each $J_i$ with $b^+>0$ on both sides, so its Seiberg–Witten invariants vanish, while moduli spaces of many $\mathfrak s$ are nonempty for some $t$. **VERIFIED** as logic.
- **The window $\ell\ge0$ alone gives nothing**: $-v^2\le4\kappa$ admits infinitely many classes in an indefinite lattice. **VERIFIED.**
- **Finiteness is used only inside proofs.** For fixed $M,\epsilon$, regularization, isolations and $R$, the restrictions of $v$ to each block take finitely many values (compactly supported duals and [CF] Prop. F); this is used only in the proofs by contradiction of Theorem F and Prop. G. **PLAUSIBLE.**
- **The control is local and uniform.** Negative pieces need nothing; positive pieces need Theorem F; caps need $C_W$. Each holds for every Seiberg–Witten solution in the charge window, uniformly in $t$ and $R\ge T_0$. Then Prop. D excludes every $\mathfrak s$ at once. **VERIFIED** as logic, inputs as labelled.

---

## 3. The positive pieces

### 3.1 Lattice data

With the chamber-compatible lift $\Lambda_0=(-2,-1;0,1,0,-1)$ on $(G,U;T_b)$ and the twists $-e\,\mathrm{PD}(F_r)$, $f\,\mathrm{PD}(F'_l)$ (`c2_lattice.py`, **VERIFIED**):

| bits | $\Lambda_P$ | $\Lambda_P^2$ | $\Theta(P)$ | $\lambda_\varnothing$ | $\lambda_{\{1\}}$ | $\lambda_{\{2\}}$ | $\lambda_{\{1,2\}}$ | parities of $(x,u;t)$ |
|---|---|---|---|---|---|---|---|---|
| $(0,0)$ | $(-2,-1;0,1,0,-1)$ | $0$ | $1$ | $-1$ | $-\frac32$ | $-\frac12$ | $-1$ | $(0,1;1,0,1,0)$ |
| $(0,1)$ | $(-2,0;0,1,0,-1)$ | $-2$ | $\frac12$ | $0$ | $-\frac12$ | $-\frac12$ | $-1$ | $(0,0;1,0,1,0)$ |
| $(1,0)$ | $(-4,-2;-1,0,-1,-2)$ | $2$ | $\frac32$ | $-2$ | $-\frac32$ | $-\frac32$ | $-1$ | $(0,0;0,1,0,1)$ |
| $(1,1)$ | $(-4,-1;-1,0,-1,-2)$ | $0$ | $1$ | $-1$ | $-\frac12$ | $-\frac32$ | $-1$ | $(0,1;0,1,0,1)$ |

$w_2(P)$ evaluates to $(0,0;1,1,1,1)$ mod $2$; $v\equiv\Lambda_P+w_2(P)$; exactly two $t_b$ are odd, so $v_P^2=2xu-2u^2-\sum t_b^2$ is even and $v_P^2\le-2$ when $u=0$. **VERIFIED.** Note $\Lambda_P^2\le2$ in all cases (used in §3.7).

### 3.2 The period and the band

The block $B_j$ has rational $H^2$ of signature $(1,7)$; $C_2$ has form $\left(\begin{smallmatrix}-4&1&0\\1&0&1\\0&1&-4\end{smallmatrix}\right)$, determinant $8$, signature $(1,2)$, boundary $L(8,1)$; its complement in the block is negative definite. On the positive-width region the retained piece carries a metric conformal to a toric Kähler metric with period
$$H=U+aX_1+bX_2=\textstyle\sum_I\theta_IH_I,\quad \theta=((1-p)(1-q),p(1-q),(1-p)q,pq),\ p=4a,\ q=4b,$$
$H\cdot X_1=1-4a$, $H\cdot U=a+b$, $H\cdot X_2=1-4b$, $H^2=2(a+b)-4(a^2+b^2)$ ([MS §6], the lemma on the toric model). **VERIFIED** (`c5_periods.py`). $\Lambda\cdot H<0$ on $\Pi\setminus\{U\}$ (corner values in §11.2), approaching $0$ at the cusp only for bits $(0,1)$. **VERIFIED.**

**Theorem F(a) (band).** On a complete piece with $\mathrm{Scal}\ge0$, positive on an open set, cylindrical ends on rational homology spheres of positive scalar curvature, $b^+_{L^2}=1$ with period $H$, and harmonic background $\beta$, a finite-energy solution of $\rho(iD^+)=(\psi\psi^*)_0$, $D_B\psi=0$ satisfies $(v\cdot H)(K\cdot H)<0$ if $\psi\not\equiv0$ and $v\cdot H=0$ if $\psi\equiv0$.

*Proof.* With $\mathrm{tr}(\rho(i\eta^+)\rho(i\xi^+))=4\langle\eta^+,\xi^+\rangle$, $\langle(\psi\psi^*)_0\psi,\psi\rangle=\frac12|\psi|^4=4|D^+|^2$ and $\langle\rho(i\beta^+)\psi,\psi\rangle=4\langle\beta^+,D^+\rangle$. The Weitzenböck formula $D_B^*D_B=\nabla^*\nabla+\frac14\mathrm{Scal}+\frac12\rho(F_B^+)$ integrates to $0=\int(|\nabla\psi|^2+\frac14\mathrm{Scal}|\psi|^2)+2\int\langle\beta^++D^+,D^+\rangle$. Since $\beta^+=2\pi\frac{\Lambda\cdot H}{H^2}h_H$ and the harmonic projection of $D^+$ is $2\pi\frac{v\cdot H}{H^2}h_H$, the second integral is $8\pi^2\frac{(v\cdot H)(K\cdot H)}{H^2}+2\|D^+_\perp\|^2$. The first is positive unless $\psi\equiv0$ (a parallel section vanishing on an open set vanishes). ∎ **VERIFIED** (signs re-derived); integration on the ends **PLAUSIBLE** (exponential decay; [MS §7], the lemma on the period inequality, uses cutoffs on end strips).

As $\Lambda\cdot H<0$, the band is $\Lambda\cdot H<K\cdot H<0$, "$K\cdot H$ between $\Lambda\cdot H$ and $0$": the path $s\mapsto s\eta$ crosses the wall of $K$ ([T3] §1.3). **VERIFIED.** *Strictness is essential:* allowing $\mathrm{Scal}\equiv0$ closes the band, which then admits (bits $(0,0)$, $H_{\{1\}}$) $u=1$, $x=6$, $t=(1,0,1,0)$, $h_1=2$, $z_1=\frac32$, $K\cdot H_1=0$, $v_P^2=8$, $Q_{\{1\}}=6$, $d_1=2$. **VERIFIED** (`c5_periods.py`).

### 3.3 Scalar curvature of the toric metrics

The metrics are $g=\frac12M_{ij}d\mu_id\mu_j+2(M^{-1})_{ij}d\theta_id\theta_j$, $M=C+\sum_\nu n_\nu n_\nu^t/l_\nu$, $C=\mathrm{diag}(c,0)$, $c\ge0$ ([MS §6]). With $B=M^{-1}$, $\partial_kB=\sum_\nu\frac{n_{\nu k}}{l_\nu^2}Bn_\nu n_\nu^tB$; contracting twice,
$$-\partial_i\partial_jB_{ij}=2\sum_\nu\frac{G_{\nu\nu}^2}{l_\nu^3}-\sum_{\nu,\mu}\frac{G_{\nu\nu}G_{\mu\mu}G_{\nu\mu}+G_{\nu\mu}^3}{l_\nu^2l_\mu^2},\qquad G=n^tBn,$$
and with $P_{\nu\mu}=G_{\nu\mu}/\sqrt{l_\nu l_\mu}$, $z_\nu=l_\nu^{-1/2}$, $q_\nu=z_\nu P_{\nu\nu}$ this is $q^t(I-P)q+z^t((I-P)\circ(P\circ P))z$. I derived both steps by hand. $0\le P\le I$ because $AA^t=I-B^{1/2}CB^{1/2}$ for $A$ with columns $B^{1/2}n_\nu/\sqrt{l_\nu}$, so both terms are nonnegative by Schur's product theorem. **VERIFIED** (proof). The normalization $\mathrm{Scal}=-\partial_i\partial_j(2B)_{ij}$ (Abreu, with the manuscript's factor) was checked against the scalar curvature computed from the Christoffel symbols of the four-dimensional metric: exact rational agreement of all three expressions on the Fubini–Study triangle (constant $12$) and on eight configurations of the manuscript's punctured pentagon with $c\in\{0,1\}$; the product tube $S^2(1/\sqrt2)\times S^1\times\mathbb R$ has $\mathrm{Scal}=4$ and fibre area $2\pi$ (`c4_scal.py`). **VERIFIED.** That the conformal cylindrical completions at the cone points keep $\mathrm{Scal}\ge0$ is **PLAUSIBLE** ([MS §6], the lemma on cone links: links with $\mathrm{Scal}\ge6$).

### 3.4 The vertex alternative and the lattice lemma

**Theorem F(b) (vertex alternative).** Let $H\in\Pi\setminus\{U\}$ and $u\ne0$. If $v$ is in the band at $H$, some nonempty $I$ with $\theta_I>0$ has $\mathrm{sign}(u)z_I<|\lambda_I|$; if moreover $u<0$, some such $I$ has $z_I>0$. If $v\cdot H=0$, some nonempty $I$ with $\theta_I>0$ has $\mathrm{sign}(u)z_I\le0$; if $u<0$ and $\theta_\varnothing>0$, some such $I$ has $z_I>0$.

*Proof.* $\lambda_I<0$ for $I\ne\varnothing$ and $\lambda_\varnothing\le0$, so $\Lambda\cdot H<0$; parity $u\equiv\lambda_\varnothing\pmod2$ gives $K\cdot U\ge0$ for $u>0$. Band, $u>0$: $K\cdot H<0\le K\cdot U$ forces $K\cdot H_I<0$ at a supported $I\ne\varnothing$. Band, $u<0$: $v\cdot H>0>v\cdot U$ forces $z_I>0$. Wall: $\theta_\varnothing u+\sum_{I\ne\varnothing}\theta_Iz_I=0$. ∎ **VERIFIED** (proof; exact check on a rational grid of $840$ periods including all edges, $|u|\le6$, $|d_i|\le30$: $1{,}240{,}467$ band and $35{,}972$ wall instances, no failure; `c3_convexity.py`). *The strengthened wall statement fails exactly when $\theta_\varnothing=0$:* $1680$ wall instances with $u<0$ and all supported $z_I=0$, all at a saturated lens side (e.g. bits $(0,0)$, $u=-5$, $d_2=20$, $(p,q)=(0,1)$). [SW1] Prop. 3.5(b) asserts $z_I>0$ for every Seiberg–Witten component with $u<0$; its proof passes to a limit whose spinor may vanish, so the correct conclusion is "$z_I>0$, or $z_I\ge0$ with the abelian alternative". **VERIFIED.** Harmless, since the abelian alternative gives $Q_I\le-4$ below.

**Lemma 3.3 (lattice).** Let the alternative hold at $I$ and put $Q_I=v_P^2-\frac12\sum_{i\in I}h_i^2$. Then $Q_I\le-2$, except for a Seiberg–Witten class with $|I|=1$, $u=z_I=\pm1$, where $Q_I\le2$ and $d_i=0$; for an abelian instanton $Q_I\le-6$ ($|I|=1$), $\le-4$ ($|I|=2$); if $u=0$, $v_P^2\le-2$.

*Proof.* With $d_1=x-\sum t_b-h_1$, $d_2=x-2u-h_2$, one has the identities
$$Q_{\{1\}}=8z_1u-4u^2-\textstyle\sum(t_b-u)^2-\frac12(h_1-2u)^2,\qquad Q_{\{2\}}=8z_2u-4u^2-\sum t_b^2-\frac12(h_2-2u)^2,$$
$$Q_{\{1,2\}}=4z_{12}u-2u^2-\textstyle\sum(t_b-\frac u2)^2-\frac12\big((h_1-u)^2+(h_2-u)^2\big).$$
The parity terms total at least $2$ in each case, so with $a=|u|$, $w=\mathrm{sign}(u)z_I\in\frac12\mathbb Z$: $Q_I\le8aw-4a^2-2$ ($|I|=1$) and $\le4aw-2a^2-2$ ($|I|=2$). The constraints $w<|\lambda_I|\le\frac32$ (Seiberg–Witten) and $w\le0$ (abelian) give the claims, the exception being $a=w=1$, $|\lambda_I|=\frac32$, which forces $d_i=4(z_I-u)=0$. ∎ **VERIFIED** (identities symbolic; $8{,}909{,}186$ instances over $|x|\le16$, $|u|\le6$, $|h_i|\le18$, $t_b$ reduced to its sum and minimal square, all bits, both kinds, every $I$: no violation, maxima $-6,-4,-2,2,-2$; exceptions only for bits $(0,0)$ with $I=\{1\}$ and $(1,1)$ with $I=\{2\}$; `c2_lattice.py`). With Theorem F(b), the exception requires $u=+1$.

### 3.5 The tube

**Theorem F(c) (small width).** Suppose a block contains a product tube $T=S^2(1/\sqrt2)\times S^1\times[0,L]$ (metric $g_{S^2(1/\sqrt2)}+\frac12d\xi^2+2d\theta^2$) with fibre class $U$, and background $\lambda_U\omega_{S^2}$ on it. Then for a reduced field on a component containing the block,
$$4\pi^2u^2L\le\int_T|D|^2\le2\|D^+\|^2_{L^2(B)}+16\pi^2\kappa_B .$$

*Proof.* $\int_{S^2}D=2\pi u$ over a fibre of area $2\pi$; Cauchy–Schwarz gives $\int_{S^2}|D|^2\ge2\pi u^2$, and the base has area $2\pi L$ (`c4_scal.py`). The identity $\|F^0\|^2=2\|F^{0,+}\|^2+8\pi^2\kappa$ on a region with its inherited charge, with $|F^0|^2=\frac12|D|^2$ at a reduction, gives the second inequality ([MS §7], the energy–charge identity). ∎ **VERIFIED.** On the tube $V=\frac14\mathrm{Scal}+\frac12\rho(\beta^+)\ge1-\frac12|\lambda_U|\ge0$, as $|\lambda_U|=|\lambda_\varnothing|\le2$ and Clifford multiplication by the self-dual part of $\lambda\omega_{S^2}$ has operator norm $|\lambda|$ on $W^+$. **VERIFIED.** With $\int_Bh^2=o(\epsilon^{-1})$, $\kappa_B\le K(M)$ and $L\ge c/\epsilon$ ([MS §7], the proposition comparing tubes with the retained energy, and the corollary on the small-width test; [CF] Prop. F), $u=0$ once $\epsilon<\epsilon_0(M)$. **PLAUSIBLE** (the $o(\epsilon^{-1})$ costs rest on [MS §6]). For bits $(0,0)$, $(1,1)$ ($u$ odd) there is then *no* reduced field on a component containing the tube. **VERIFIED.**

### 3.6 The period along the family

| region of $(t_j,t_{j+1})$ | retained piece | period | supported $I\ne\varnothing$ | control |
|---|---|---|---|---|
| positive width, interior | $C_2$ punctured at the $A_7$ point | $U+aX_1+bX_2$ | $\{1\},\{2\},\{1,2\}$ | band + F(b) |
| $J_j$ side ($\alpha_j=0$), $w_0\ge3\epsilon$ | $C_{1,1}=\nu(U\cup X_2)$, $S^3$ end | $U+bX_2$ | $\{2\}$ | band + F(b) |
| lens side $j$ ($\alpha_j=\frac14$) | $C_2\setminus N_1$ (Wahl point) | $U+\frac14X_1+bX_2$ | $\{1\},\{1,2\}$ | band + F(b) |
| corner $(J_j,L_{j+1})$ | $C_{1,1}\setminus N_2$ | $H_{\{2\}}$ | $\{2\}$ | band + F(b) |
| corner $(L_j,L_{j+1})$ | $C_2\setminus(N_1\sqcup N_2)$ | $H_{\{1,2\}}$ | $\{1,2\}$ | band + F(b) |
| $w_0\le3\epsilon$, incl. the corner $(J_j,J_{j+1})$ | tube of length $\asymp\epsilon^{-1}$ and bounded templates | not in $\Pi$ | — | F(c): $u=0$ |

A side with $\alpha_i=0$ is never supported, so a stretched three-sphere is never used in $I$; at a lens side $H\cdot X_i=0$ and the supported pairings are computed on the retained piece without the filling ([MS §6], the lemma on support at period vertices). If $J_j$ and $J_{j+1}$ are both broken, $H$ must be orthogonal to both far halves, $H\cdot F_{l,j}=2a$, $H\cdot F_{r,j+1}=2b$, so $H=U$, $U^2=0$. **VERIFIED** (`c5_periods.py`); the construction **PLAUSIBLE** ([MS §6], the proposition on assembly and the lemma on the tube). Walls are crossed: for $u\ne0$ the wall $\{u+ad_1+bd_2=0\}$ meets $\Pi\setminus\{U\}$ whenever $u,z_1,z_2,z_{12}$ do not all share the sign of $u$ (e.g. $u=1$, $d_1=-8$, $d_2=0$ at $a=\frac18$), and walls accumulate at the cusp. **VERIFIED.** Bounded-energy band classes with $u\ne0$ survive near the cusp (bits $(1,0)$, $(u,d_1,d_2)=(2,-2,-4)$, in the band for all $a=b\in(0,\frac13)$, $-\frac14v_{C_2}^2=\frac98$), so the lattice alone does not empty the cusp. **VERIFIED.**

### 3.7 The exact double three-sphere corner: a Lorentzian lemma

**Lemma F(d).** Let $\hat P$ carry a complete metric of nonnegative scalar curvature, positive somewhere, with cylindrical $S^3$-ends and harmonic background of class $\Lambda_P$ (any bits). Every Seiberg–Witten solution of class $K=\Lambda_P+v$ with $d_s=\frac14(K^2-4)\ge0$ has $v_P^2\le-2$.

*Proof.* By F(a), $(v\cdot H)(K\cdot H)<0$, so $v\ne0$. Suppose $v_P^2\ge0$. Then $v$ is causal and $K$ timelike ($K^2\ge4$) in the Lorentzian lattice of $P$; the sign of $v\cdot H$ (resp. $K\cdot H$) is that of the half-cone containing $v$ (resp. $K$), so they lie in opposite half-cones and $K\cdot v\le0$. Then $\Lambda_P^2=K^2-2K\cdot v+v^2\ge K^2\ge4$, contradicting $\Lambda_P^2\le2$. So $v_P^2<0$, and $v_P^2$ is even. ∎ **VERIFIED** (proof; exact check over $|x|\le30$, $|u|\le10$, $|t_b|\le7$, all bits: $852{,}276$ classes with $K^2\ge4$, $v^2\ge0$, $v\ne0$, none with $K\cdot v\le0$; `c8_lorentz.py`).

*Consequence.* At the exact corner the component on the isolated $P$ has no parameter, so for a generic $\tau$ it exists only if $d_s\ge0$ (FL2a Prop. 2.16, applied on the completed piece: PLAUSIBLE); then $\kappa_P\ge\frac12$ and $\varepsilon_I(\{P\})=8\kappa_P-2-2s\ge-2$, for *any* metric of nonnegative scalar curvature on $P$, whatever its period. An abelian instanton on $P$ needs $v\cdot H_P=0$, avoided by a generic fixed period, and has $v_P^2\le-2$ anyway. **VERIFIED** as a deduction.

*Correction to [SW1] §3.8(iii).* [SW1] tested whether a fixed corner period controls the classes with $v_P^2\ge2$, or $v_P^2=0$ with a nonzero near half, and found none of $20{,}000$ periods free of them. It did not impose $d_s\ge0$. With it, all $20{,}000$ random periods, and $G$, $G+U$, $2G+U-\sum T_b$, $3G+U-T_1-T_3$, $G+2U-T_2$, are free of realizable harmful classes (`c7_corner.py`), as the lemma predicts. **VERIFIED.** What remains true: on the *approach* to the corner the components carry parameters (on unbroken $X$, $n$ of them), the dimension condition is void, and the needed bound is $-v_P^2+\frac12\sum_{i\in I}h_i^2\ge2$; every period has band classes with $v_P^2\ge0$ (by [SW1]'s numerics, a fortiori), so uniformity there needs a mechanism forcing $u=0$, such as the tube. **SPECULATIVE** as a theorem, numerically robust.

### 3.8 Uniformity in $t$ and $R$; three-dimensional solutions on $Y_{\pm2}$

**Theorem F(e) (the control, uniformly).** Fix in order the caps and $C_W$, $L_*$, $\Pi_0$ and $p'$, the odd $\lambda_\pm$, $M$, and $\epsilon$. Then there are a regularization, isolation lengths, a perturbation size $\delta_0$ and $T_0$ such that for every $t\in\bar Q$, every $R\ge T_0$ and every reduced field (Seiberg–Witten component or abelian instanton) containing a positive piece $P_j$ of an ideal limit of points of $\mathcal Z_e$: if $w_0\le3\epsilon$ then $u=0$; otherwise $u=0$ or the alternative of F(b) holds at a nonempty set of whole sides (with "$z_I>0$" for $u<0$ replaced by "$z_I>0$ or $z_I\ge0$ with the abelian alternative"). Hence Lemma 3.3 applies.

*Proof sketch* ([MS §7], the lemma on the vertex test with finite persistence and the corollary on the order of choices). By contradiction along a sequence with regularization $\to0$, isolations $\to\infty$, perturbations $\to0$, $R\to\infty$, $t\to t_*$. Block energies are bounded uniformly in all of these ([CF] Prop. F); evaluations on supported vertices are bounded by compactly supported duals and become constant; the reduced fields converge on the completed retained piece to an unperturbed reduction (abelian Coulomb gauge, the $C^0$ bound, elliptic bootstrapping); the limiting period has $w_0\ge3\epsilon$; F(a)–(b) at the limit contradict the assumed failure, which is a closed condition on the constant class at vertices still supported. ∎ **PLAUSIBLE** (70% given the family; 65% overall).

*Uniformity in $R$.* The metric inside each block is independent of $R$; the energy of a block is bounded independently of $R$ because each neck middle has charge $\ge-C_Y(1+\nu)$ by the Chern–Simons–Dirac identity ([CF] Lemma D, Cor. E); the background restricted to a block converges exponentially, the $Y_{\pm2}$ being rational homology spheres. **VERIFIED** as logic. *Three-dimensional solutions.* $Y_{\pm2}$ is not an $L$-space for $g(K)\ge2$ and carries irreducible three-dimensional Seiberg–Witten solutions ([CF] Prop. C). A Seiberg–Witten point of $X$ at large $R$ may stay near one along a neck, so $\int_X|\psi|^4$ grows linearly in $R$; nothing above uses that integral. The retained toric pieces are isolated inside the blocks by collars of positive scalar curvature, and the cap constant uses only unit-strip bounds and the exponential decay of the cap's harmonic forms (§4.2). At finite $R$ no $Y_{\pm2}$-neck breaks, so no stratum is broken there. **VERIFIED** as logic.

### 3.9 Families on $b^+=1$ pieces cross walls; band classes exist

On the closed $P$, $d(K)\ge0$ means $K^2\ge4$, so $K^\perp$ misses the positive cone, the chamber of $(g,0)$ is fixed, $SW(K;g,0)=0$ by positive scalar curvature, and wall-crossing (Kronheimer–Mrowka; Li–Liu for $b_1=0$, cited, not checked) gives $SW(K;g,2\pi\Lambda^+)=\pm1$ exactly on band classes with $d\ge0$. Such classes exist for generic periods ([SW1] `s9c_dsearch.py`); by Lemma F(d) all of them have $v_P^2\le-2$, so they are cheap and harmless. In the two-parameter families on the blocks, Seiberg–Witten solutions appear and disappear along walls $\{v\cdot H(t)=0\}$, where abelian instantons live. **VERIFIED** as logic given the cited wall-crossing formula.

---

## 4. The caps

### 4.1 No abelian instanton contains a cap

The old cap $W$ contains $A$ with $A^2=0$ and $\langle w,A\rangle$ odd, so every allowed restriction $v_W\equiv w_W\pmod2$ is nonzero, and the form of $W$ (nondegenerate, boundaries rational homology spheres) is indefinite. Choose the cap metric, fixed on its collars, so that no such class is anti-self-dual (local period variation and Baire; [MS §7], the proposition on cap constants). For a fixed finite problem only finitely many restriction classes occur, each with $|v_W^+|\ge c>0$; an abelian instanton on a component containing $W$ would make the pairing of $v_W$ with the cap's harmonic self-dual forms equal to a tail term $\le C'_We^{-\sigma N}(E+C'_W(N+2))^{1/2}$, small once the cap neck is long. **VERIFIED** (topology) / **PLAUSIBLE** (85%).

### 4.2 The cap constant

Unit-strip Weitzenböck bounds give $\|D^+\|_{L^2(V_k)}\le A_W$ uniformly in $k$ on the completed cap, even if the field approaches a three-dimensional solution with nonzero spinor along the $Y$-end; with the exponential decay of the harmonic forms, $|v_W^+|\le B_W$, hence $v_W^2\le B_W^2$ and $(\Lambda_W+v_W)^2\le(|\Lambda_W^+|+B_W)^2$, and $C_W=1+\max\{B_W^2,(|\Lambda_W^+|+B_W)^2\}$ ([MS §7], same proposition). $C_W$ depends only on the cap. **PLAUSIBLE** (80%). Only upper bounds on squares are used. **VERIFIED.**

### 4.3 Short end components

Short end components (fewer than $L_*$ pieces) contain no positive piece. For a Seiberg–Witten component on one, regular in its $p$-parameter family (no reducibles there, by §4.1; FL2a Prop. 2.16 with parameters), $d_s+p\ge0$. With $K^2\le C_W-(K\cdot e)^2-2r$ and $2\chi+3\sigma=c-2r$, the number $r$ of negative pieces cancels and $(K\cdot e)^2\le C_W-c+4p$, so $|K\cdot e|\le B$ independently of $\lambda$; then $|v\cdot e|\ge\lambda-B$, $\kappa\ge\frac14(\lambda-B)^2-\frac14C_W$, and $q+4\ge8$ for $\lambda$ large. **VERIFIED** (arithmetic, `c1_index.py`: e.g. $C_W=10$, $c=5$, $p=4$: $|K\cdot e|\le3$, $\lambda=101$: $8\kappa\ge19{,}188$). [MS §8] and [SW1] use the weaker $d_s+p+4\ell\ge0$; it suffices but is not the regularity statement. The count needs only $q\ge0$ ([R] (B2)). Regularity in families **PLAUSIBLE** (85%).

### 4.4 Long end components

The family adjunction inequality gives $q\ge3L-7m+2\sum(v\cdot e)^2-C\ge4$ once $L\ge L_*$ ([MS §8], the lemma on end exclusion; [R] Lemma 4.6). **VERIFIED** as arithmetic, given Theorem F and $C_W$. On unbroken $X$ the blow-up is not needed at all: Prop. D uses only $(v\cdot e)^2\ge0$. **VERIFIED.**

### 4.5 The price of the blow-up

A Seiberg–Witten component on a long end component containing the blown-up cap has monopole index $i=q+2(\Theta-\kappa)$ with $\Theta\ni\frac14(1-\lambda^2)$. Two cases (`c9_freepart.py`):

- *No positive piece.* Realizability needs $(K\cdot e)^2\le4L+C$ (§4.3 with $p\approx L$), so the smallest $|v\cdot e|$ is $\lambda-2\sqrt L$, and at minimal charge $i\approx2L+\frac32(\lambda-2\sqrt L)^2-\frac12\lambda^2$, which is negative for $\frac{\lambda^2}{16}<L<\frac{\lambda^2}4$ with minimum $\approx-\frac{\lambda^2}8$ at $L\approx\frac9{64}\lambda^2$. Exact minima: $-333$, $-1283$, $-5059$ for $\lambda=51,101,201$ (at $L=380,1406,5700$), while $q=1419,5561,22091$.
- *Positive pieces in the small-width region, bits $(1,0)$.* There only $u=0$ is forced (no band is available, since the bounded template pieces of [MS §6] are not known to have nonnegative scalar curvature), and $v_P=(x,0;0,1,0,1)$ has $v_P^2=-2$ (cost $\frac12$), both near halves nonzero, and $K_P^2=4-4x$, arbitrarily large. So realizability is no constraint, $v\cdot e=0$ is allowed, and $i\approx L-\frac12\lambda^2$ ($-4909$, $-4109$, $-2109$ at $\lambda=101$, $L=200,1000,3000$), with $q\ge4$.

These components are harmless at limits without a component in $\mathcal M^{*,0}$ ($q+4\ge8$), but not next to one (§5.3). The order of choices does not remove them. $p'$ may be kept below $\frac{\lambda^2}{16}$, which avoids the first case, but end components that reach past the initial string into positive pieces of small width have dangerous lengths from $p'$ up to about $\frac12\lambda^2$ whatever the order, since $\lambda$ must be large compared with the constants of the short ends. **VERIFIED** (arithmetic); that such Seiberg–Witten components are actually nonempty is **SPECULATIVE** (it needs the obstructed gluings across the exceptional sphere, or the small-width blocks, to be realized).

---

## 5. Broken limits

### 5.1 Without a component in $\mathcal M^{*,0}$

Components are anti-self-dual ($q+4\ge4$ by regularity, [R] (A2)(b)), Seiberg–Witten, or abelian instantons. Outer components contain caps, so they are anti-self-dual or Seiberg–Witten with $q+4\ge8$ (§§4.3–4.4). The other reducible components form chains $\Gamma$; incidence at broken necks uses the nodal degeneration of $V_{S_i}$ ([S] Lemma 3.2, [R] (J4)), and the family adjunction inequality ([R] Lemma 4.4) gives $\kappa_\Gamma\ge\frac12(s^-+m)$, so at spacing four
$$\varepsilon_I(\Gamma)\ge5m-7\ge-2\ (m\ge1),\qquad\varepsilon_I(\Gamma)\ge1\ (m=0)$$
([R] Lemma 4.5, exact minima). With $a+b\ge2$ components outside chains and at most $a+b-1$ chains, $\sum_j(q_j+4)\ge4(a+b)-2(a+b-1)\ge6>4$, contradicting [R] Lemma 1.3. **VERIFIED** as a deduction ([R] Theorem B), inputs as labelled. The minimum $-2$ is attained by an isolated $P$ (bits $(0,1)$, $u=0$, $x=2$, $t=(1,0,-1,0)$, $\kappa=\frac12$, both bounding insertions met; `c5_periods.py`); at the double corner it is controlled by F(c), and, for any corner metric of nonnegative scalar curvature, by F(d) without any tube. Isolated negative pieces have $d_s\le-1$ and no parameter. **VERIFIED.**

### 5.2 With a component in $\mathcal M^{*,0}$: the dimension of its part

Let $\mathfrak F$ be the set of components in $\mathcal M^{*,0}$, $f=|\mathfrak F|$. If the perturbations act componentwise ([M2] Prop. 2.6; [R] (A7′)), the components in $\mathfrak F$ solve their own cut-down problems, the $\mu_c$-sections fall on them (§1.2), and the circle acts freely on their product. If these strata are regular ([R] (A2)(c), with the $\mu_c$-sections transverse on products), the space containing the $\mathcal M^{*,0}$-part has dimension
$$D=\sum_{j\in\mathfrak F}(i_j-\lambda_j)-1-2(n_a-1)=5-4f-\sum_{j\notin\mathfrak F}(i_j+4)-\lambda_{\mathfrak F},$$
by [R] Lemma 1.3 and $k+1=f+\#(\text{others})$. **VERIFIED** (re-derived); regularity and componentwise perturbations **PLAUSIBLE** (80%). The forgotten components enter only through the numbers $i_j$; no regularity is required of them.

Lower bounds: a chain of reducible components without caps has $\delta(\Gamma)=6\kappa_\Gamma-m+L-2s+\Delta\ge-2$ at spacing $\ge2$ ([R] §3.1, Lemma 4.5, with $6\kappa_\Gamma\ge3s^-+3m$); a *short* chain containing a cap has $\delta\ge2$ (§4.3: $|v\cdot e|\ge\lambda-B$); anti-self-dual components have $i\ge Q+6\lceil-Q/8\rceil$ with $Q=8\Theta-3(1+b^+)+p-2s-z$ ([M2] Prop. 3.2(b), formula re-derived), hence $i\ge-2$ away from caps and long negative stretches, and $i\ge0$ far enough from the caps ([M2] (b), (c), not recomputed). Then the count over intervals between components in $\mathfrak F$ gives $D\le-1$: an exhaustive check over arrangements of up to nine components with these bounds gives $\max D=-1$ (`c9_freepart.py`, Part A). **VERIFIED** as a deduction. In particular every limit with a component in $\mathcal M^{*,0}$ whose Seiberg–Witten chains avoid the caps or are short, and whose anti-self-dual components are not of low index, is excluded *without coupled regularity*. This removes [SW1]'s appeal to [R] (A3) for these limits.

### 5.3 Where the count fails

- *Long Seiberg–Witten chains containing a blown-up cap* (§4.5): $\delta$ can be $\approx-\frac{\lambda^2}8$ or $\approx L-\frac12\lambda^2$. With one such chain $D$ is as large as $330$, $1280$, $5056$ ($\lambda=51,101,201$), and with long chains at both ends and $f=1$ the count over arrangements gives $D=13$ for $i=-10$ and $D=193$ for $i=-100$ (Part A). **VERIFIED.** [M2] Prop. 3.2(d) asserts $\delta\ge2$ for every chain containing a cap and a Seiberg–Witten component, citing $|v\cdot e_\pm|\ge\lambda_\pm-B$ from [R] Lemma 4.6(b),(c); that bound is proved there only for short end components. **VERIFIED** (reading).
- *Anti-self-dual components of low index* near the caps or on five or more consecutive negative pieces ([M2] §3.6). Not Seiberg–Witten strata, but they occur in the same limits.

In both cases counting allows componentwise solutions in a space of positive dimension; the Seiberg–Witten chain's normal Dirac operator on $W^+\otimes L_2$ has index $\approx-\frac18\lambda^2$, i.e. a large obstruction. What excludes such limits is coupled regularity: perturbations of the normal equations at the Seiberg–Witten component that depend on the phase of a component in $\mathcal M^{*,0}$ (single-valued, since the Seiberg–Witten circle is compensated by the phase), and the two-valued terms of [M2] (A3′) at anti-self-dual components. With them the coupled problem has index $1-4k-(\text{losses})<0$. These limits lie in end regions of size $O(\lambda_\pm^2+p')$, fixed before $M$. **PLAUSIBLE** (55–60%).

### 5.4 Status of the broken strata in scope

| stratum | count | handled by | status |
|---|---|---|---|
| Seiberg–Witten chains, no component in $\mathcal M^{*,0}$ | $\varepsilon_I\ge-2$; $\sum(q_j+4)\ge6$ | Theorem F, incidence, (J4), [R] Thm. B | VERIFIED given inputs |
| outer Seiberg–Witten components (caps), no component in $\mathcal M^{*,0}$ | $q+4\ge8$ | §§4.3–4.4 | VERIFIED arithmetic; regularity PLAUSIBLE |
| isolated $P$ at the double corner | $\varepsilon_I\ge-2$ | F(c), or F(d) | VERIFIED given inputs |
| with $\mathcal M^{*,0}$: interior or short cap Seiberg–Witten chains, no low-index anti-self-dual component | $D\le-1$ | §5.2 | VERIFIED as deduction; (A2) PLAUSIBLE |
| with $\mathcal M^{*,0}$: long Seiberg–Witten cap chains | $D\gg0$ possible | coupled regularity at the chain | PLAUSIBLE (55–60%) |
| with $\mathcal M^{*,0}$: low-index anti-self-dual components | $D\gg0$ possible | [M2] (A3′) | PLAUSIBLE (60%) |
| broken along $Y_{\pm2}$ | — | none at finite $R$ | VERIFIED |

---

## 6. Dimensions and walls

1. **On $X$.** The families Seiberg–Witten space over $Q$ has dimension $d(\mathfrak s)+n$ when regular; since $n\gg b^+(X)=m+b_0$, a family could meet reducibles, but the caps forbid them (§4.1), so these spaces contain no abelian instantons and cross no wall. **PLAUSIBLE** (85%).
2. **On pieces.** The dimension is $d_s+p_\Gamma$ (plus $4\ell$ for the stratum). It is used twice: at short end components (§4.3) and at the exact double corner (Lemma F(d)). Dimension never excludes a Seiberg–Witten stratum through $\mathcal W$ (§1.2). **VERIFIED.**
3. **On $b^+=1$ pieces.** The two-parameter families on the blocks cross the walls $\{v\cdot H(t)=0\}$ for infinitely many classes; negative pieces ($b^+=0$) carry an abelian instanton of every class for every parameter ([M2] Prop. 2.3). On the walls Seiberg–Witten spaces meet abelian instantons; those belong to the analysis of mixed limits, and in limits without a component in $\mathcal M^{*,0}$ they are covered by $\varepsilon_I\ge-2$, which treats both kinds of reducible alike. **VERIFIED.**
4. **Band classes are nonempty.** By wall-crossing, band classes with $d\ge0$ carry $SW=\pm1$ for generic periods; no choice of metric removes them; emptiness can only come from energy (and they are cheap by F(d)). **VERIFIED** as logic.

---

## 7. Missed strata and attempted counterexamples

*Strata checked one by one.*

| stratum | outcome |
|---|---|
| Seiberg–Witten on $X$, interior $t$, any level | Theorem E |
| Seiberg–Witten on $X\setminus\bigcup\nu S_i$ at lens faces and lens corners | Theorem E with reference fillings; cap charge beyond the filling counted in $\ell$ (PLAUSIBLE) |
| abelian instantons on $X$ or on $X\setminus\bigcup\nu S_i$ | §4.1 |
| Seiberg–Witten or abelian on a lens cap $\hat\nu S_i$ | spinor zero by positive scalar curvature; abelian caps are reference fillings, not main components |
| twisted ($O(2)$) reducibles | impossible, $H_1=0$ (§1.4) |
| trivial flat connection on a piece with $w$ even there | abelian instanton with $v=0$ (stabilizer $\mathrm{SU}(2)$); impossible on $P$ (two $t_b$ odd); covered by $\varepsilon_I\ge-2$ |
| broken limits (§5) | table 5.4 |
| auxiliary collars ($L(8,1)$, $\partial C_{1,i}$, saturated $\partial N_i$, cap and exceptional isolation) | finite, never broken |
| $Y_{\pm2}$-necks | not broken at finite $R$; three-dimensional solutions do not enter the counts |

*Attempted counterexamples.*

1. **Spacing one.** The global inequality fails without bound (§2.3), consistent with the nonzero pairings of $(HB)^M$. Not a counterexample to the claim. **VERIFIED.**
2. **Closed band.** With $\mathrm{Scal}\equiv0$ allowed, $Q_{\{1\}}=6$ (§3.2): strictness is essential, and it is available. **VERIFIED.**
3. **The cusp without the tube.** Bounded-energy band classes with $u\ne0$ survive near the cusp (§3.6); on the approach to the corner every fixed period admits band classes with $v_P^2\ge0$. The tube is needed there. At the corner itself, F(d) suffices. **VERIFIED** / **SPECULATIVE** as marked.
4. **An outer Seiberg–Witten component without the blow-up.** Then $q=8\kappa-3(1+b^+(W))-2s-z$ with $\kappa\ge-\frac14C_W$ can be negative, and two such outer components around a chain can break $\sum(q_j+4)=4$. The blow-up is needed. **VERIFIED** (arithmetic).
5. **A component in $\mathcal M^{*,0}$ next to a long Seiberg–Witten cap component** (§§4.5, 5.3). This defeats the counting argument; only coupled regularity excludes it. It is the one configuration in scope that is not excluded by a verified count. **VERIFIED** (count) / its existence **SPECULATIVE**.

---

## 8. Corrected statements

**Proposition A (reducible strata).** For a spin$^u$ structure $\mathfrak t$ with $w_2(\mathfrak t)\ne0$ on a piece $\hat\Gamma$ with $b_1=0$, the reducible locus of the moduli space of $\mathrm{PU}(2)$ monopoles is $\bigsqcup_{\mathfrak s}\iota(M_{\mathfrak s})$, $M_{\mathfrak s}$ the moduli space of the Seiberg–Witten equations for $K=c_1(\mathfrak s)$ with $\eta=F^+_{A_\Lambda}$; at level $\ell=\kappa+\frac14v^2$ the stratum is $\iota(M_{\mathfrak s})\times\mathrm{Sym}^\ell$; the tangential index is $d_s$ and the normal part completes it to $d_a+2n_a+6\ell$. *(FL2a Lemmas 3.12–3.13, (2.63); FL2b Lemma 3.32, (3.64); Memoir (2.3.14). VERIFIED.)*

**Lemma B (phase sections).** Every section of $\mathbb L_{\mathfrak t}$ vanishes on Seiberg–Witten points; at a broken limit the $\mu_c$-sections restrict to the components in $\mathcal M^{*,0}$. *(VERIFIED.)*

**Lemma C (incidence).** As in §2.1. *(VERIFIED given (J1), (J2), (D4′); lens fillings PLAUSIBLE.)*

**Proposition D (energy with reserved far halves).** As in §2.3; it replaces [S] Prop. 4.2 in the proof of [S] Thm. 4.3. *(VERIFIED as deduction; sharp.)*

**Theorem E (unbroken $X$).** As in §2.4. *(VERIFIED as deduction from D, F, G.)*

**Theorem F (control on the positive pieces).** (a) band; (b) vertex alternative on $\Pi\setminus\{U\}$, with the wall case as stated in §3.4; (c) $u=0$ on components containing a long $U$-tube; (d) at the exact double corner, $v_P^2\le-2$ for every realizable Seiberg–Witten class on the isolated $P$ for any metric of nonnegative scalar curvature; (e) the uniform statement of §3.8 over $\bar Q$ and $R\ge T_0(M)$. *((a), (b), (d) VERIFIED; (c) VERIFIED as computation with PLAUSIBLE inputs; (e) PLAUSIBLE, 65%.)*

**Proposition G (caps).** (a) No abelian instanton contains a cap; (b) $v_W^2,(\Lambda_W+v_W)^2\le C_W$ for Seiberg–Witten components, $C_W$ depending only on the cap; (c) for $\lambda_\pm$ large (after $L_*$), every short end Seiberg–Witten component has $q+4\ge8$; (d) every long one has $q\ge4$; (e) long ones can have monopole index $\approx-\frac18\lambda_\pm^2$ (no positive piece) or $\approx L-\frac12\lambda_\pm^2$ (with positive pieces of small width). *((a), (b) PLAUSIBLE 80–85%; (c), (d) VERIFIED as arithmetic, regularity PLAUSIBLE; (e) VERIFIED as arithmetic.)*

**Theorem H (broken limits without a component in $\mathcal M^{*,0}$).** Given F, G, incidence with (J4), and regularity of anti-self-dual components, no such limit with a reducible component lies in the closure of $\mathcal Z_e$. *(VERIFIED as deduction.)*

**Theorem I (broken limits with a component in $\mathcal M^{*,0}$).** Given F, G, incidence, single-component regularity of the strata in $\mathcal M^{*,0}$ with the $\mu_c$-sections, and componentwise perturbations: (a) every such limit whose Seiberg–Witten chains are interior or short at the caps, and whose anti-self-dual components have $i\ge-2$ ($\ge0$ at a cap), does not exist ($D\le-1$); (b) the remaining limits lie in end regions fixed before $M$, and are excluded under coupled regularity at long Seiberg–Witten cap chains and at low-index anti-self-dual components. *((a) VERIFIED as deduction; (b) PLAUSIBLE, 55–60%.)*

**Corollary J (scope).** Under F(e), G, incidence with (J4), the regularity statements above and the coupled regularity of I(b), for $u=(\phi_*B)^3HB$, all large $M$, and $R\ge\max(R_0(M),T_0(M))$, no Seiberg–Witten stratum of any piece, at any level, zero-spinor part included, meets the closure of $\mathcal Z_e$ except within the mixed limits containing abelian instantons. *(VERIFIED as deduction.)*

---

## 9. Gaps, with confidences

1. **The metric family** of [MS §6]: coupled two-parameter toric family on each block, conformal completions with $\mathrm{Scal}\ge0$, moving interfaces, the tube and corner replacement, the $o(\epsilon^{-1})$ costs uniform under deeper regularization and longer collars. **75%.**
2. **The control on $P$ uniformly** (F(e)): the persistence argument at finite sizes, uniformly over $\bar Q$ and $R\ge T_0$. **85% given 1; about 65% overall.**
3. **The tube inputs** (charge bound $K(M)$, $\int h^2=o(\epsilon^{-1})$). **90% given 1.**
4. **Caps** (generic period, local bound $C_W$, identification of the self-dual projection, long cap necks). **80%.**
5. **Incidence**: (D4′) and the reference fillings at lens faces **90%**; the analytic part of the nodal degeneration (J4) **85%**.
6. **Short-end regularity** in families (no reducibles there; generic $\tau$). **85%.**
7. **Single-component regularity** of strata in $\mathcal M^{*,0}$ with the $\mu_c$-sections, and componentwise perturbations away from the residual regions. **80%.**
8. **Coupled regularity in the end regions**: at long Seiberg–Witten chains containing a blown-up cap (single-valued, phase-coupled) and at low-index anti-self-dual components ([M2] (A3′), two-valued), coherent over faces and corners and compatible with the instanton links and the lens pairing. **55–60%.** Whether the long Seiberg–Witten cap components are nonempty at all is open (**SPECULATIVE**); if they are empty, only (A3′) remains.
9. **Compatibility with the composition law.** The family needed here is not the product of intervals described in [S] §3; [G] Theorem A′ states the composition law for the coupled block families. **70%** (outside the Seiberg–Witten analysis, but the same family must serve both).
10. **Compactness over $\bar Q$** ([R] (A1), [CF]): presupposed throughout. **About 75%** ([CF] 72%).

---

## 10. Verdict and confidence

**Verdict.**

- *(1) Unbroken $X$.* At every $t\in\bar Q$ off the three-sphere faces (lens faces included), every level and every $\mathfrak s$, Seiberg–Witten strata are excluded by incidence ($\ell\ge T(v)$) against Prop. D ($\ell-T(v)\le\frac18(-5M-3p+c_\kappa)+C<0$). The projection form [S] Prop. 4.2 must be replaced by Prop. D. What controls the set of $\mathfrak s$ is three local inequalities, uniform in $t$ and $R$; no basic class enters.
- *(2) Positive pieces.* The needed control is Theorem F: the strict Weitzenböck band at the period of the isolated plumbing $C_2$, the vertex alternative, the lattice lemma, and the $U$-tube in the small-width region. The period stays in $\Pi\setminus\{U\}$ along the whole family except near the corner where both neighbouring three-spheres are stretched; there the tube forces $u=0$. At the exact corner a tube is not needed (Lemma F(d)); on its approach it is. Uniformity in $R$ holds because block metrics do not depend on $R$ and block energies are bounded by the Chern–Simons–Dirac identity.
- *(3) Caps.* No abelian instanton contains a cap; cap classes are bounded by $C_W$; large odd $\lambda_\pm$ is needed only for short end components, where it works, and it creates long end components of very negative monopole index (Prop. G(e)).
- *(4) Dimensions and walls.* $d(\mathfrak s)+n$ on $X$ without walls; walls crossed on every block; dimension used only at short ends and at the exact corner.
- *(5) Broken limits.* Without a component in $\mathcal M^{*,0}$: excluded by the index identity. With one: excluded by the dimension of its part, except in end regions next to long Seiberg–Witten cap chains or low-index anti-self-dual components, which need coupled regularity.

**Confidence.**

| claim | label | confidence |
|---|---|---|
| lattice, arithmetic, numerology, Prop. D and its sharpness, Lemma 3.3, F(b), F(d), the index identities | VERIFIED | 98% |
| band (F(a)), scalar curvature of the Hessian metrics, tube computation, phase sections | VERIFIED | 95% |
| the metric family of [MS §6] | PLAUSIBLE | 75% |
| F(e), the control on $P$ uniformly over $\bar Q$ and $R\ge T_0$ | PLAUSIBLE | 65% |
| caps (G(a), (b)); short-end regularity | PLAUSIBLE | 80%; 85% |
| unbroken $X$ (Theorem E) given compactness | PLAUSIBLE | 55% |
| broken limits without a component in $\mathcal M^{*,0}$ (Theorem H) given compactness | PLAUSIBLE | 50% |
| broken limits with one, outside the end-region residual (Theorem I(a)) | PLAUSIBLE | 45% |
| the end-region residual (Theorem I(b)) | PLAUSIBLE | 55–60% given the rest |
| **all Seiberg–Witten strata in scope absent from the closure of $\mathcal Z_e$, for $u$ and large $M$, by this route** | PLAUSIBLE | **about 35%** (25–45%) |

The rows are positively correlated: the control on $P$, the caps and the regularity statements rest on the same analytic framework of [MS §§6–9]. [SW1] put the whole at 60% while rating an indispensable ingredient, coupled regularity, at 55%; that is incoherent, and it did not see the long cap chains. [M2]'s count is a real improvement for interior chains, but its cap bound (d) holds only for short end components.

---

## 11. Report of the checks

All files are in `round4/swfinal-checks/`, made independently of [SW1], [R] and [M2]; their outputs are the files `out_*.txt`. Exact integer or rational arithmetic throughout, except `c7_corner.py` (decimal arithmetic for the random periods, exact lattice data).

### 11.1 Citations, recomputed from the LaTeX counters

`n1_number.py` (shared theorem counters), `n2_eqnum.py` (equation numbers within sections, counting every numbered line of multi-line displays), `n3_booknum.py` (Memoir, numbered chapter.section.equation).

| citation | content found | status |
|---|---|---|
| FL2a Thm. 2.12, 2.13; Rmk. 2.14; Prop. 2.15, 2.16 | compactness; transversality; $\eta=F^+_{A_\Lambda}$ not generic; compactness of $M_{\mathfrak s}$ for $\|\tau-\mathrm{id}\|<\frac1{64}$; smoothness of $M^0_{\mathfrak s}$ for generic $\tau$ | correct |
| FL2a (2.55), (2.56), (2.63) | Seiberg–Witten equations with $\tau,\vartheta,\eta$; $\eta=F^+_{A_\Lambda}$; $d_s=\frac14(c_1(\mathfrak s)^2-2\chi-3\sigma)$ | correct |
| FL2a Prop. 3.1; Lemma 3.2; Cor. 3.3; Lemma 3.5; Cor. 3.6; Lemma 3.12; Lemma 3.13 | circle-fixed points; Morgan–Mrowka; no zero-section SW points; twisted reducibles; Kuranishi model at zero section; reducibles solve SW with $\eta=F^+_{A_\Lambda}$; reducible locus $=\iota(M_{\mathfrak s})$ | correct |
| FL2b (3.10), (3.12), (3.20), (3.21), (3.25), (3.26) | $\mathbb L_{\mathfrak t}$; $\mu_c$; $\dim\mathcal M^{*,0}$; $d_a,n_a$ (misprint $\chi+2\sigma$ in (3.21)); codimension bound; $\delta_c$ | correct |
| FL2b Lemmas 3.12, 3.13, 3.15; Cor. 3.18; Def. 3.20; Lemmas 3.21, 3.22; Prop. 3.29 | representatives of $\mu_p$ and of $\mu_c$; extension to lower strata; cut-down spaces miss the smooth lower strata; good classes; $\bar M^{\rm asd}=\iota(\bar M^w_\kappa)$; deforming $\mathcal V$; link count $2^{n_a-1}$ | correct |
| FL2b Lemma 3.32; (3.62), (3.63), (3.64), (3.68); Thm. 3.33 | splitting criterion; the one-manifold; $(c_1(\mathfrak t)-c_1(\mathfrak s))^2=p_1(\mathfrak t)+4\ell$; no reducibles; vanishing theorem (a) and link formula (b) | correct |
| FL1 Lemma 4.4; Def. 4.19; Thm. 4.20 | $C^0$ bound; Uhlenbeck topology; sequential compactness | correct |
| Memoir (2.3.12), (2.3.13), (2.3.14) | the embedding $\iota$; gauge inclusion $s\mapsto\mathrm{id}_W\otimes\mathrm{diag}(s,s^{-1})$; $\ell(\mathfrak t,\mathfrak s)=\frac14((c_1(\mathfrak t)-c_1(\mathfrak s))^2-p_1(\mathfrak t))$ | correct |
| [MS §6] theorem on the metric family, lemmas on placement, toric model, curvature, tube, period support, comparison forms; proposition on assembly | as paraphrased in §§3.2–3.6 | read |
| [MS §7] theorem controlling reduced classes on positive bridges (i)–(iii); propositions on tube comparison and on cap constants; corollaries on the small-width test and the order of choices; lemmas on the period inequality and on the vertex test | as paraphrased in §§3–4 | read |
| [MS §8] definition of admissibility (i), (ii); lemma on end exclusion | $d_s+p+4\ell\ge0$; switched spheres need a unit only if both halves vanish; short and long end components | read |

All FL, FL1 and Memoir numbers cited in [SW1] are correct.

### 11.2 Computations

- **`c1_index.py`.** Symbolic: $d_s+\text{normal}=d_a+2n_a$ at level $0$, $+6$ per level; $d_s=n_a+\ell+\frac12\Lambda\cdot v-(1+b^+)$; $2\chi+3\sigma$ of $P$, $\hat N$, chains, $X$; $8\kappa=n+3m+c_\kappa$; $n_a=\frac18(5m-n)+\Theta_0-\frac18c_\kappa$; $8(\ell-T)\le7m-3n+c_\kappa+8C$; $7m-3n=-5M-3p$, $5m-n=M-p$; per period $+1$, $-5$; short-end bounds and examples (with $K\cdot e$ odd: $|K\cdot e|\le7$ resp. $3$ resp. $9$ in the three examples; [SW1]'s value $10$ in its fourth example ignores parity, harmless).
- **`c2_lattice.py`.** Lattice of $P$ from its Gram matrix; $F_r^2=F_l'^2=-2$, $F_r\cdot F'_l=0$, $U\cdot F_r=U\cdot F'_l=1$; $w_2(P)$; the table of §3.1; the three identities for $Q_I$; the lattice lemma on $8{,}909{,}186$ instances: no violation, maxima $-6,-4,-2,2,-2$, exceptions only $(0,0)$/$\{1\}$ and $(1,1)$/$\{2\}$.
- **`c3_convexity.py`.** $840$ rational periods (step $\frac1{24}$ plus $\frac1{97},\frac1{1000}$ and their complements), $|u|\le6$, $|d_i|\le30$: $1{,}240{,}467$ band, $35{,}972$ wall instances; band $\Rightarrow$ alternative, band with $u<0\Rightarrow z_I>0$, wall $\Rightarrow$ abelian alternative, $\Lambda\cdot H<0$: no failure. Maxima of $\Lambda\cdot H$: $-\frac12$, $-\frac1{2000}$, $-1$, $-\frac12$. The strengthened wall statement fails in $1680$ instances, all with $\theta_\varnothing=0$.
- **`c4_scal.py`.** Scalar curvature from Christoffel symbols, Abreu's formula with $2M^{-1}$, and the closed form: exact agreement and positivity at ten configurations (Fubini–Study $12$); tube: $\mathrm{Scal}=4$, fibre area $2\pi$, base area $2\pi$ per unit of $\xi$; the substitution $z=\frac12(1+\cos\varphi)$ gives the round metric of radius $1/\sqrt2$.
- **`c5_periods.py`.** $C_2$: determinant $8$, signature $(1,2)$; periods, vertex values, bilinear interpolation; $\min(H\cdot U)^2/H^2=\frac14$ on the lens face; $\Lambda\cdot H$ at the corners; the cusp class $(2,-2,-4)$ ($-\frac14v^2=\frac98$, band for $0<a=b<\frac13$); the closed-band class ($Q=6$); $(\pi v)_P^2=80,360,1520$; the extremal isolated $P$ ($\varepsilon_I=-2$).
- **`c6_chains.py`.** Exact minima of $-\frac14v^2+T(v)$ by recursion along the chain over the bit and the two half evaluations of each sphere: $\frac12(s^-+m)$ on nine chains, also with the strengthened alternative; spacing one: $-7$, $-\frac{29}2$, $-\frac{43}2$ (within $|h|\le10$, $|u|\le6$, $|t_b|\le8$).
- **`c7_corner.py`.** Harmful band classes on the closed $P$ at $20{,}000$ random periods and five special ones: with [SW1]'s criterion every random period has some; with $d_s\ge0$ imposed, none has any.
- **`c8_lorentz.py`.** Lemma F(d): $852{,}276$ classes with $K^2\ge4$, $v^2\ge0$, $v\ne0$; none with $K\cdot v\le0$.
- **`c9_freepart.py`.** Part A: arrangements of up to nine components: $\max D=-1$ with short cap chains; $13$ and $193$ with long cap chains of index $-10$ and $-100$. Part B: minimal monopole index of long Seiberg–Witten cap components: $-333$, $-1283$, $-5059$ for $\lambda=51,101,201$ without positive pieces; $K_P^2=4-4x$ at cost $\frac12$ for small-width blocks of bits $(1,0)$; $i=-4909,-4109,-2109$ at $\lambda=101$, $L=200,1000,3000$.

### 11.3 Assessment of [SW1]'s computations

- `s1_lattice.py`, `s2_convexity.py`, `s3_global.py`, `s6_periods.py`, `s7_index.py`: reproduced by the independent computations `c1`–`c3`, `c5`, `c6`; agreement everywhere.
- `s8_scal.py`: decimal approximations; superseded by the exact comparison of `c4`.
- `s5_corner.py`, `s5b_special.py`: correct as computations, but the criterion omits $d_s\ge0$, so they do not support the claim made at the exact corner (§3.7).
- `s4_cusp.py`, `s9_bandexamples.py`, `s9c_dsearch.py`: not load-bearing; consistent with Lemma F(d) (all band classes with $d\ge0$ have $v_P^2\le-2$).
