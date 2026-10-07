# The family analogue of the SO(3)-monopole cobordism that the argument needs, and where it goes beyond Feehan–Leness

*Independent draft 1.*

**Sources.** Statements of Feehan–Leness (FL) are taken from the verified extraction notes `a-cobordism.md`, `b-compactness.md`, `c-links.md` and `d-gluing.md` in this directory. Their theorem numbers are those of the arXiv LaTeX sources; published numberings may differ (see the uncertainty lists in those notes). Abbreviations are as there:

- FL1 = dg-ga/9710032; FL2a = math/0007190; FL2b = dg-ga/9712005; FL3 = math/9907107;
- L1 = math/0106238; Memoir = math/0203047 v4; FL6 = math/0609530; Overlap = 1211.0480; F19 = 1910.14580.

The argument is taken from `exposition.tex`, `notes/T1-secondary.md` §§1–4, `notes/D-families.md`, `notes/T2-mu-classes.md` §§2–3, `notes/T3-wallcrossing.md` §§0–4, and the manuscript sections `08-indices`, `09-analysis`, `10-gluing`. Labels such as `analysis:projection` refer to the manuscript.

Statements marked *my check* were not taken from either source.

---

## 0. Dictionary

| FL | Manuscript and project notes |
|---|---|
| $\mathfrak t=(\rho,V)$, $V=W\otimes E$; $\Lambda=c_1(\mathfrak t)=c_1(W^+)+c_1(E)$; $w=c_1(E)$ | $l=c_1(W^+)$, $c=c_1(E)$, $\Lambda=l+c$ |
| $\kappa=-\tfrac14p_1(\mathfrak t)=c_2(E)-\tfrac14c_1(E)^2$ | $\kappa=c_2-c^2/4$ |
| $d_a(\mathfrak t)=-2p_1(\mathfrak t)-\tfrac32(\chi+\sigma)$ | $D_I=8\kappa-3(1+b^+)$, when $b_1=0$ |
| $n_a(\mathfrak t)=\tfrac14\big(p_1(\mathfrak t)+\Lambda^2-\sigma\big)$ | $n_D=\Theta-\kappa$, with $\Theta=(\Lambda^2-\sigma)/4$ |
| $\dim\mathcal M^{*,0}_{\mathfrak t}=d_a+2n_a$ | $D_{\rm sp}=D_I+2n_D$ |
| reducible pair for $V=W'\oplus W'\otimes L$, $\mathfrak s=(\rho,W')$, $c_1(L)=\Lambda-c_1(\mathfrak s)$ | $E=L_1\oplus L_2$, spinor in $W\otimes L_1$, $v=c_1(L_1)-c_1(L_2)$, $K=\Lambda+v=c_1(\mathfrak s)$; so $c_1(L)=-v$ |
| level $\ell(\mathfrak t,\mathfrak s)=\tfrac14\big((\Lambda-c_1(\mathfrak s))^2-p_1(\mathfrak t)\big)$ (Memoir (2.3.14)) | "Feehan–Leness level" $\ell=\kappa+v^2/4$; on pieces with lens ends it also contains cap excess and trajectory charge |
| $d_s(\mathfrak s)=\tfrac14\big(c_1(\mathfrak s)^2-2\chi-3\sigma\big)$ | $d_s$ |
| $\mu_p(\beta)=-\tfrac14p_1(\mathbb F_{\mathfrak t})/\beta$ | Donaldson's $\mu(S)$ on the zero section |
| $\mu_c=c_1(\mathbb L_{\mathfrak t})$, $\mathbb L_{\mathfrak t}=\mathcal C^{*,0}_{\mathfrak t}\times_{(S^1,\times-2)}\mathbb C$; the cut-down $\bar{\mathcal W}^{\eta}$ | the line of phase weight two; the $\eta$ "phase sections" |
| irreducible zero-section pairs, $\iota(M^w_\kappa)$ | type $A$ |
| Seiberg–Witten pairs (reducible, $\Phi\not\equiv0$), $\iota(M_{\mathfrak s})$ | type $S$ |
| reducible zero-section pairs (reducible anti-self-dual connections), which FL exclude by choosing $w$ good | type $R$ |
| irreducible non-zero-section pairs, $\mathcal M^{*,0}_{\mathfrak t}$ | type $P$ ("free") |

Below I use FL's names for the four kinds of pair.

---

## 1. Setting

**1.1 Topology.**

- $X$ is closed, connected, oriented and smooth, with $H_1(X;\mathbb Z)=0$ and $b^+(X)\ge1$. No parity condition is imposed on $b^+$; in the application $b^+(X)=m+b^+(C_-)+b^+(C_+)$.
- $J_1,\dots,J_n\subset X$ are pairwise disjoint separating 3-spheres.
- $S_1,\dots,S_n\subset X$ are embedded 2-spheres with $S_i\cdot S_i=-4$ and closed tubular neighbourhoods $N_i$, so $\partial N_i\cong L(4,1)$. The $N_i$ are pairwise disjoint, $N_i\cap J_j=\emptyset$ for $i\ne j$, and $S_i\cap J_i$ is a circle cutting $S_i$ into discs $D_i^\pm$.
- Cutting $X$ along all the $J_i$ and filling with balls gives pieces $\hat Z_0,\dots,\hat Z_n$. The outer pieces contain the caps $C_\pm$. Each inner piece is negative ($b^+=0$) or positive ($\cong\mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2$, $b^+=1$, containing the plumbing $(-S_j,U,S_{j+1})$ of type $(-4,0,-4)$). Write $m$ for the number of positive pieces.

**1.2 Metrics.** Let $Q=[-1,1]^n$, with a smooth family $\{g_t\}_{t\in\operatorname{int}Q}$ satisfying the following.

- As $t_i\to-1$, $g_t$ contains a round cylinder $J_i\times[-T_i,T_i]$ with $T_i\to\infty$.
- As $t_i\to+1$, $g_t$ contains a cylinder $\partial N_i\times[-T_i,T_i]$ with a fixed metric of positive scalar curvature on $L(4,1)$.
- The family is a product near every face and corner of $\bar Q$. Over an open face it is a family of cylindrical-end metrics on the components of $X$ cut along the corresponding necks.
- All other seams, in particular the $Y_{\pm2}$ seams, have bounded (large, fixed) length. Only necks with positive scalar curvature are ever stretched.
- The metric is fixed and generic on the caps.
- On each positive piece the metrics form the manuscript's toric family: $\operatorname{Scal}\ge0$, the period lies in the polygon $\operatorname{conv}\{H_I\}$, and there is an $S^2\times S^1$ tube at the cusp (Thm `geometry:family`; T3 §§2–3). This is used only for the chamber estimate of §4, item (9).

**1.3 Spin$^u$ structures.** Fix a spin$^c$ structure $(\rho,W)$ with $c_1(W^+)=l$. For $e\in\{0,1\}^n$ let $\mathfrak t_e=(\rho,W\otimes E_e)$, where
$$w_e:=c_1(E_e)=w_0+\sum_ie_i\,\mathrm{PD}[S_i],\qquad \Lambda_e:=c_1(\mathfrak t_e)=\Lambda_0+\sum_ie_i\,\mathrm{PD}[S_i],\qquad p_1(\mathfrak t_e)=p_1(\mathfrak t_0)=-4\kappa,$$
with $\langle w_0,[S_i]\rangle=0$ and $\langle\Lambda_0,[S_i]\rangle=2$.

Since $S_i\cdot S_i=-4$ and $S_i\cdot S_j=0$, one has $\Lambda_e^2=\Lambda_0^2$. Hence $d_a:=d_a(\mathfrak t_e)$ and $n_a:=n_a(\mathfrak t_e)$ do not depend on $e$.

In addition:

- each cap contains a class $A_\pm$ with $A_\pm\cdot A_\pm=0$ and $\langle w_0,A_\pm\rangle$ odd (Prop. `estimates:cap`);
- each cap is blown up once more, with $\langle\Lambda_0,E_\pm\rangle$ odd and large;
- on each positive piece the values $\lambda_I=\langle\Lambda_e,H_I\rangle$ are those of T3 §1.1. In particular $|\lambda_I|\le\tfrac32$ for $I\ne\varnothing$, and $\lambda_\varnothing=\langle\Lambda_e,U\rangle\in\{0,-1,-2\}$.

*Remark on $w_2$ (my check).*

- On each cobordism $W'$ the class $\mathrm{PD}[S]$ is divisible by two (T2 Lemma 5.1). So there the two lifts give the same SO(3) bundle, with end identifications twisted by the flat $\mathbb Z/2$ character of $Y_{\pm2}$.
- On the closed $X$ this is not so, provided every piece into which the $Y_{\pm2}$ seams cut $X$ has $H_1(\,\cdot\,;\mathbb Z/2)=0$. This holds for each $W'$, since $H_1(W')=0$; I have not checked it for the caps and $W_H$. Then the Mayer–Vietoris coboundary $\bigoplus_jH^1(Y_j;\mathbb Z/2)\to H^2(X;\mathbb Z/2)$ is injective. By T2 Lemma 5.1(b), $\mathrm{PD}[S_i]\bmod2$ is the image of the sum of the characters of the two seams of $W'_i$. So the $2^n$ classes $w_2(\mathfrak t_e)$ are pairwise distinct.
- The sum over $e$ is therefore a sum over different SO(3) bundles with a common $p_1$. It is analogous to the sum over $w$ in the Kronheimer–Mrowka structure theorem (FL6 Thm 2.2), not to FL's change of integral lift within one $w_2$ (Memoir (2.5.3)).
- This is also a consistency requirement. Suppose all the $\mathfrak t_e$ had the same $w_2$ and the data did not depend on the lift. Then Memoir (2.5.3) would give $\Omega=\#_{e=0}\prod_i\varepsilon_i(0)(1+s_i)\in\{0,\pm2^n\#_{e=0}\}$, which is incompatible with $\Omega\not\equiv0\pmod{2^N}$ once $n\ge N$.

**1.4 Classes and representatives.** Put
$$z=\mu_p([S_1])\cdots\mu_p([S_n])\cdot z_{\rm cap},\qquad \deg z=2n+\deg z_{\rm cap}=d_a+n .$$
Here $z_{\rm cap}$ is a product of surface and point classes in the caps, intersection-suitable in the sense of FL2b Lemma 3.17. The equality $\deg z=d_a+n$ is the parametrized form of the condition $\deg(z)=d_a$ in FL2b Prop. 3.29; the family contributes $n=\dim Q$.

The representatives must have the following properties.

- **(a) Representative of $\mu_p([S_i])$.** It is Donaldson's jumping-line divisor $V_{S_i}=\{[A]:E|_{S_i}\not\cong\mathcal O\oplus\mathcal O\}$, perturbed only away from connections that are reducible along $S_i$. It represents $\pm\mu_p([S_i])$ (T2 Prop. 2.3, Cor. 2.4).
- **(b) Dichotomy at reducibles.** Let a pair be reducible along $S_i$, with $v=c_1(L_1)-c_1(L_2)$. Then it lies in $V_{S_i}$ if and only if $\langle v,[S_i]\rangle\ne0$ (T2 Cor. 3.3(i)). The manuscript's holonomy representative needs its zero-winding modification to have this property.
- **(c) Persistence.** Take an Uhlenbeck-convergent sequence of points of $V_{S_i}$. Its limit lies in $V_{S_i}$ unless a point of the limiting $\mathbf x$ lies on $S_i$ (T2 Cor. 3.3(ii)). The supports of distinct $S_i$ are disjoint, so distinct spheres need distinct particles.
- **(d) Faces.** At $t_i=-1$, $V_{S_i}$ degenerates to the union of the half-representatives of $D_i^\pm$, each defined on its own side (T2 §4). At $t_i=+1$ it lies in $N_i$.
- **(e) Particles.** A particle of charge $a$ regains at most $4a$ dimensions through its position and the cuts it releases (Lemma `analysis:incidence`). This is the analogue of intersection-suitability in FL2b Cor. 3.18.
- **(f) Representative of $\mu_c^{\eta}$.** Take $\eta=n_a-1$ sections of $\mathbb L_{\mathfrak t_e}$. They are functions of spinor values sampled on finitely many balls, of phase weight two, and quadratic in $\Phi$ near the instanton points. They must be transverse on every stratum that contains an irreducible non-zero-section component (Prop. `analysis:instanton-link`, Lemma `analysis:samples`).

**1.5 Equations and perturbations.** These are FL's equations (Memoir (2.1.10)) for each $g_t$. To them are added small perturbations of holonomy type with energy cut-offs, as in FL1 (2.23)–(2.34) and (4.12)–(4.13). The perturbations are subject to the following conditions.

- No term uses parallel transport through a neck that separates at a face, and each term involves the parameters of one component only (manuscript §9.1).
- There is no Dirac perturbation on the separated caps. The exterior data for $e$ and $e+\epsilon_i$ coincide.
- All terms vanish near the instanton points.
- Terms that couple different components vanish on tuples without an irreducible non-zero-section component. They do not depend on forgotten reducible zero-section components (Lemma `analysis:R-independence`).
- Finitely many multi-valued terms, with rational weights, are allowed.

---

## 2. The statement

**2.1 The family invariant.**

Let $\mathfrak M^{w_e}_\kappa(Q)=\bigcup_{t\in\operatorname{int}Q}M^{w_e}_\kappa(g_t)\times\{t\}$, of dimension $d_a+n$, oriented by Donaldson's $o(\Omega,w_e)$ and the orientation of $Q$. For generic data the set $\bar{\mathcal V}(z)\cap\mathfrak M^{w_e}_\kappa(Q)$ is finite and lies in the top stratum over $\operatorname{int}Q$ (T1 Prop. 1.4). In the purely anti-self-dual problem this already requires excluding reducible anti-self-dual limits at the $J$-faces, by the same lattice inequality as row 8 of §3. Put
$$\Omega=\sum_{e\in\{0,1\}^n}\varepsilon(e)\,\#\big(\bar{\mathcal V}(z)\cap\mathfrak M^{w_e}_\kappa(Q)\big),\qquad \varepsilon(e)=\prod_i\varepsilon_i(e_i),\quad \varepsilon_i(1)=-s_i\,\varepsilon_i(0),$$
where $s_i$ compares the orientations of the two minimal trace caps on $N_i$ (Prop. `negative:local-sign`).

- **Relation to FL.** $\Omega$ is the family analogue of $D^w_X(z)=\#(\bar{\mathcal V}(z)\cap\bar M^w_\kappa)$ (Memoir (2.5.2), without the blow-up), summed over $e$.
- **Not an invariant of $X$.** $\Omega$ is invariant only under deformations that preserve the face structure, and the separate summands are not invariant (T1 Prop. 1.4).
- **In the application.** $X=X_M$ is a connected sum along each $J_i$ with $b^+>0$ on both sides, so $D^w_X$ vanishes, whereas $\Omega\equiv\pm q\not\equiv0\pmod{2^N}$ (T1 Prop. 1.7).
- **Scope.** The definition and the non-vanishing of $\Omega$ lie outside FL's work. Only the cobordism is compared below.

**2.2 The cut-down free stratum and its compactification.**

With $\mathcal M^{*,0}_{\mathfrak t_e}(Q)=\bigcup_t\mathcal M^{*,0}_{\mathfrak t_e}(g_t)\times\{t\}$, put
$$\mathcal Z_e=\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{\,n_a-1}\cap\big(\mathcal M^{*,0}_{\mathfrak t_e}(Q)/S^1\big),\qquad \dim\mathcal Z_e=(d_a+2n_a+n-1)-(d_a+n)-2(n_a-1)=1 .$$
In FL's normalization this reads $\deg(z)+2\eta=\dim\big(\mathcal M^{*,0}_{\mathfrak t_e}(Q)/S^1\big)-1$ with $\deg(z)-\dim Q=d_a$. It is the family form of the one-manifold of FL2b Cor. 3.18.

The compactification $\bar{\mathcal M}_{\mathfrak t_e}(\bar Q)$ is defined as follows.

- **Over $t\in\operatorname{int}Q$.** It is FL's Uhlenbeck closure $\bar{\mathcal M}_{\mathfrak t_e}(g_t)\subset\bigsqcup_\ell\mathcal M_{\mathfrak t_e(\ell)}\times\mathrm{Sym}^\ell(X)$ (Memoir Def. 2.1.2, (2.1.14)).
- **Over an open face of $\bar Q$.** Let the necks $J_i$ ($i\in I^-$, $k=|I^-|$) and $\partial N_i$ ($i\in I^+$) be infinitely long. The points are tuples consisting of:
  - ideal pairs $[A_j,\Phi_j,\mathbf x_j]$, $0\le j\le k$, on the completed *main components* of $X\setminus\big(\bigcup_{I^-}J_i\cup\bigcup_{I^+}N_i\big)$. They solve the equations with the particle-dependent perturbations of FL1 (4.13), and on each end they converge exponentially to a flat connection with zero spinor;
  - for $i\in I^+$, an ideal zero-section pair on the completed *separated cap* $N_i$. The spinor vanishes there by the Weitzenböck formula;
  - finitely many non-constant anti-self-dual trajectories, with zero spinor, on $\mathbb R\times S^3$ and $\mathbb R\times L(4,1)$.

  The flat limits must match, and the total charge is $\kappa$.

By the *window* I mean the set of points with a reducible main component, at non-negative level, that lie in the closure of the cut-down free stratum. The theorem asserts that the window is empty and draws the consequence.

> **Theorem 2.3 (family cobordism with neck faces, empty-window form).** Let $X$, $(J_i,S_i,N_i)$, $\{g_t\}_{t\in Q}$, $(\mathfrak t_e)_{e\in\{0,1\}^n}$ and $z$ be as in §1, with $\deg z=d_a+n$. Assume:
> 1. $n_a\ge1$;
> 2. each cap contains a class $A_\pm$ with $A_\pm^2=0$ and $\langle w_0,A_\pm\rangle$ odd, and the cap metrics are generic;
> 3. the positive pieces lie at mutual distance $\ge4$ and at distance $\ge L_*$ from the caps; $\langle\Lambda_0,E_\pm\rangle$ is odd and sufficiently large; and $3n-7m>C_0$, where $L_*$ and $C_0$ depend only on the caps;
> 4. the chamber estimate on the positive pieces (Thm `estimates:clamp`) holds uniformly over $\bar Q$, faces included.
>
> Then, for generic sufficiently small perturbations and representatives with the properties of §§1.4–1.5, the following hold.
> - (i) The closure of $\mathcal Z_e$ in $\bar{\mathcal M}_{\mathfrak t_e}(\bar Q)/S^1$ contains no point with a reducible main component, whether a Seiberg–Witten pair or a reducible zero-section pair, at any Uhlenbeck level and over any face.
> - (ii) Its only other limit points are of two kinds:
>   - (α) the points of $\bar{\mathcal V}(z)\cap\mathfrak M^{w_e}_\kappa(Q)$ (top level, $t\in\operatorname{int}Q$);
>   - (β) tuples over a single lens face $t_i=+1$, consisting of an irreducible non-zero-section main pair with trace-zero limit on $\partial N_i$ together with the minimal trace cap of charge $\tfrac14$ on $N_i$, with no particles, no trajectories and no other cut.
> - (iii) Remove from $\bigsqcup_e\varepsilon(e)\,\mathcal Z_e$ the sets $\{\|\Phi\|^2_{L^2}<\varepsilon\}$ near the points (α), as in FL2a Def. 3.7 and FL2b Lemma 3.22, and the collars of neck length $>D_0$ at (β). For generic small $\varepsilon$ and large $D_0$, what remains is a compact, oriented, one-dimensional weighted branched manifold with boundary.
>   - Near each point of kind (α) the signed count of boundary points is $2^{n_a-1}$, times $\sigma_0\varepsilon(e)$, times the sign of that point. Here $\sigma_0=\pm1$ is the same for all points.
>   - The boundary points of kind (β) for $e$ and for $e+\epsilon_i$ cancel.
> - (iv) Consequently $2^{n_a-1}\,\Omega=0$ in $\mathbb Q$. Since $\Omega\in\mathbb Z$, it follows that $\Omega=0$.

**Its place relative to FL.** Theorem 2.3 is a family version, with faces, of FL2b Thm 3.33(a). That theorem proves without any gluing hypothesis that if $\bar{\mathcal M}_{\mathfrak t}$ contains no reducible monopoles, then $\#(\bar{\mathcal V}(z)\cap\bar M^w_\kappa)=0$. The analogue differs in four ways:

- the family and its faces;
- the sum over $e$;
- the hypothesis "no reducibles in $\bar{\mathcal M}_{\mathfrak t}$" is replaced by conclusion (i), "no reducibles in the closure of the cut-down". The weaker form is forced, because the reducible strata here are not empty: band classes on the positive pieces carry Seiberg–Witten pairs (T3 §1.3), and on negative segments reducible anti-self-dual connections exist for every metric;
- (i) is proved, not assumed. The proof uses inequalities on characteristic classes together with a dimension count for a problem from which the reducible zero-section components have been forgotten (§3).

It is *not* an analogue of Memoir Thm 1 or Thm 8.1.9 in their general form: no reducible stratum is ever linked or evaluated.

**2.4 Constituents and their FL counterparts.**

- **(A) Compactness and strata over $\bar Q$.** Every sequence in $\mathcal Z_e$ has a subsequence converging to a tuple as in §2.2. Charges lie in discrete sets:
  - $\mathbb Z_{>0}$ for particles and for $S^3$ trajectories;
  - $\tfrac14+\mathbb Z_{\ge0}$ for trace caps;
  - $\mathbb Z_{\ge1}$ for central caps that carry their cut (Lemma `indices:lens-charge`).

  Counterparts: FL1 Thm 1.1, Thm 4.20; Memoir Thm 2.1.3; FL2a Prop. 3.1; Memoir (2.2.2).
- **(B) Index identities.** Consider a tuple with $k$ cuts at $J$-faces. For its main component $\hat Z_j$ (lens caps filled by the reference fillings of Prop. `indices:lens-index`), let:
  - $p_j$ be the number of retained interval parameters;
  - $q_j=d_a(\hat Z_j)+p_j-\deg z_j$ be the virtual cut-down instanton index, where $z_j$ is the part of $z$ assigned to $\hat Z_j$;
  - $i_j=q_j+2n_a(\hat Z_j)$ be the virtual cut-down index of the SO(3)-monopole problem, before the phase quotient and the $\eta$ phase cuts.

  Then
$$\sum_j(q_j+4)=4,\qquad \sum_ji_j-2\eta=2-4k .$$
  Each cut at a $J$-face costs $3$ for the SO(3) gluing parameter and $1$ for the lost interval parameter. A *run* is a maximal set of consecutive interior main components that are all reducible (Seiberg–Witten or zero-section), as used in row 8 of §3; in row 10 it is a maximal set of consecutive reducible zero-section components. For a reducible component, $\kappa_j=-v_j^2/4+\ell_j$ with $\ell_j\in\mathbb Z_{\ge0}$ (Lemma `indices:virtual-sums`, Prop. `indices:lens-index`). Counterparts: FL2b (3.20)–(3.25); Memoir (2.3.14), (2.3.23)–(2.3.24).
- **(C) Instanton end.** This is the parametrized FL2b Prop. 3.29 (with Lemmas 3.22–3.28 and FL2a Cor. 3.6). Near each point of kind (α) the cut-down $\mathcal Z_e$ ends in $2^{n_a-1}$ signed points.
- **(D) Faces at the $J_i$.** No end of $\mathcal Z_e$ lies over such a face. FL have no counterpart.
- **(E) Lens faces.** Ends of kind (β) are collars obtained by regular gluing, and they cancel in pairs. FL have no counterpart.
- **(F) Exclusion of every other limit (§3).** For lower-level free strata the counterpart is FL2b Cor. 3.18. For reducible strata it is the hypothesis of FL2b Thm 3.33(a). For faces FL have none.
- **(G) Stokes on a weighted branched one-manifold** (Lemma `analysis:stokes`). FL count with integers and single-valued generic data, so they have no counterpart.

---

## 3. Noncompactness: which strata must be excluded, and by what

**3.1 The strata.** A *limit point* is a point of $\overline{\mathcal Z_e}\setminus\mathcal Z_e$. The table lists every kind of point of $\bar{\mathcal M}_{\mathfrak t_e}(\bar Q)/S^1$ that could be a limit point, what happens to it, and what regularity its exclusion uses. "Particle" means a point of $\mathbf x$ (FL's level $\ell\ge1$).

| Stratum | Over | Fate | Mechanism | Regularity used |
|---|---|---|---|---|
| 1. $\iota(M^{w_e}_\kappa(g_t))$, level 0 | $\operatorname{int}Q$ | end (α), only at the finitely many points of $\bar{\mathcal V}(z)\cap\mathfrak M^{w_e}_\kappa(Q)$ | Kuranishi model (FL2a Cor. 3.6; FL2b Lemmas 3.22–3.28) | cut-down parametrized ASD problem (standard) |
| 2. $\iota(M^{w_e}_{\kappa-\ell}(g_t))\times\Sigma$, $\ell\ge1$, flat backgrounds ($\ell=\kappa$) included | interior, lens faces | excluded | cut-down ASD count: a unit of charge costs 8 and regains at most 4 | irreducible zero-section strata at lower levels (standard) |
| 3. $\mathcal M^{*,0}_{\mathfrak t_e(\ell)}(g_t)\times\Sigma$, $\ell\ge1$ | interior, lens faces | excluded | spinor count: a unit costs 6 and regains at most 4 (FL2b (3.20), Cor. 3.18) | lower-level free strata (FL1 Thm 1.3) |
| 4. $\iota(M_{\mathfrak s}(g_t))\times\Sigma$, $\ell=\ell(\mathfrak t_e,\mathfrak s)\ge0$, every level including $\ell=0$ | no cut at any $J_i$ | excluded | properties (b), (c) give $\ell\ge T(v)$, where $T(v)$ counts the spheres met only through particles; the chamber estimate and the cap bounds give $-v^2/4+T(v)\ge\tfrac{n-m}2-C$; against $\kappa=\tfrac{n+3m}8+C'$ this is impossible once $3n-7m>C_0$ (T1 Cor. 3.2) | none; it uses only that the limit solves the Seiberg–Witten equations |
| 5. reducible zero-section pairs on a component containing a cap, any level | no cut at any $J_i$; outer components | excluded | $\langle v,A_\pm\rangle$ is odd, so $v\ne0$ on the cap, and the generic cap period makes $v$ not anti-self-dual (Prop. `estimates:cap`) | none |
| 6. lens-face tuples with an irreducible non-zero-section main component other than (β) | lens faces, $k=0$ | excluded | each separated cap costs $\delta_{\rm sp}-1\ge1$ (trace charge $\tfrac14+h$ costs $1+6h$; central costs $\ge5$); particles cost $\ge2$ | main problem with lens ends (standard) |
| 7. the tuples (β) | single lens face | end; cancels against $e+\epsilon_i$ | regular gluing (Prop. `gluing:collar`); orientation comparison (Prop. `gluing:signs`) | main problem and framed cap |
| 8. $k\ge1$ with no irreducible non-zero-section main component | $J$-faces | excluded | $\sum(q_j+4)=4$ against: $q_j\ge0$ for irreducible zero-section components; $q_j+4\ge8$ for outer Seiberg–Witten components; $\ge-2$ for each run of reducible components (lattice, spacing $\ge3$). With $a$ irreducible zero-section components and $b\le2$ outer Seiberg–Witten components, $a+b\ge2$, and at most $a+b-1$ runs, the total is $\ge2a+6b+2\ge6$ | irreducible zero-section components; tangential regularity ($d_s+p_j+4\ell_j\ge0$) of Seiberg–Witten components; nothing in normal directions at any reducible |
| 9. $k\ge1$, with an irreducible non-zero-section main component and no reducible zero-section component | $J$-faces | excluded | the full count $\sum_ji_j-2\eta-1-(\text{losses})=1-4k-(\text{losses})<0$ | every component, *including Seiberg–Witten components in normal directions*. This is obtained by perturbations coupled through the irreducible non-zero-section component |
| 10. $k\ge1$, with an irreducible non-zero-section component and at least one reducible zero-section component | $J$-faces | excluded | forget the reducible zero-section components and keep their parameters. With $N\ge2$ the number of remaining components (the outer ones are never reducible zero-section pairs, by row 5), the remaining problem has index $5-4N-\sum_{\rm runs}\sum_{j\in\rm run}(4+i_j-p_j)-(\text{losses})\le3-2N<0$, using the lattice bound $\ge-2$ per run, valid at spacing $\ge4$ (Lemma `analysis:projection`, Prop. `analysis:finite-induction`) | the forgetful problem only; nothing at the reducible zero-section components |
| 11. trajectory levels on $\mathbb R\times S^3$ and $\mathbb R\times L(4,1)$ | faces | absorbed into the charge counts of rows 6–10 | non-constant levels have positive charge. Abelian trajectories between flats on a rational homology sphere are constant | none |

**3.2 Bubbling of the spinor, and of abelian pieces.**

- **The spinor does not bubble.** FL1 Lemma 4.4 gives a universal a priori $C^0$ bound on $\Phi$ (FL2a uses it in Lemma 3.8). The bound is uniform over $\bar Q$, since the scalar curvature is bounded below on the whole family and the perturbations are uniformly small. Hence $|\Phi|^4\,d\mathrm{vol}$ has no atoms, and every bubble is an anti-self-dual SU(2) connection on $S^4$ with zero spinor (Lemma `analysis:compactness`(2)).
- **The spinor can vanish on a component of the limit.** The limiting main component is then a zero-section pair, irreducible or reducible. This is not bubbling. It is accounted for by rows 1, 2, 5, 8 and 10.
- **The spinor cannot escape down a neck.** Necks of positive scalar curvature force exponential decay. The $Y_{\pm2}$ seams are never stretched in the monopole problem. Stretching them would introduce the irreducible flats and the three-dimensional Seiberg–Witten points of $Y_{\pm2}$, which the argument avoids.
- **Abelian pieces split off, but not as bubbles on $S^4$** (there is no nontrivial line bundle on $S^4$). They occur in three ways:
  - as separated lens caps carrying abelian anti-self-dual connections. The minimal trace cap of charge $\tfrac14$ is *not* excluded: it is end (β). Larger caps are excluded by row 6;
  - as reducible zero-section components between two cuts at $J$-faces (rows 8, 10);
  - as reducible backgrounds carrying SU(2) bubbles, which are FL's strata $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ and their zero-section analogues (rows 4, 5).

**3.3 Does dimension counting exclude these strata without regularity of the reducible strata?**

- **Rows 4 and 5.** No dimension count is used. The exclusion is an inequality between characteristic numbers that holds for every solution. It rests on two pointwise inputs: the Weitzenböck formula, which gives the chamber estimate and the cap bounds, and the closedness properties (b) and (c) of the representatives at reducibles.
- **Row 8.** The identity $\sum(q_j+4)=4$ is an identity of virtual indices. A reducible component enters only through a lower bound for its virtual index, derived from the lattice. Regularity is used only at irreducible zero-section components (standard) and in the tangential directions of Seiberg–Witten moduli spaces (standard, FL2a Prop. 2.16). Normal regularity at reducible points of the SO(3)-monopole moduli space is never used. FL say it may fail (FL1, after Remark 1.4; FL2a §3.4).
- **Row 9.** Normal regularity at Seiberg–Witten components *is* needed. It is not assumed: it is produced by perturbations that sample the irreducible non-zero-section component. That component restricts the common phase to $\pm1$, so the combined isotropy group is finite.
- **Row 10.** The reducible zero-section components are forgotten, so no regularity is needed there. Their circle stabilizer survives the restriction of the phase, and equivariant perturbations cannot remove their normal obstructions. The price is twofold. First, the forgetful problem must be regular near the projections of all candidates, by perturbations that do not depend on forgotten data. Second, the spacing must be $4$ rather than $3$, because a forgotten run is priced by an upper bound (its parameters), not by its true codimension.
- **No fundamental class is needed.** As in FL2b Thm 3.33, one cuts down first and then needs only (A) and collars at the ends (α), (β). The local-finiteness problem that FL flag for $\bar{\mathcal M}_{\mathfrak t}$ near lower levels (FL2b §3, introduction; FL2a §3.2, after Cor. 3.6) therefore does not arise. The global instanton link $\{\|\Phi\|^2_{L^2}=\varepsilon\}$ is never used; only its parts near the finitely many points (α) are.

---

## 4. Where the analogue goes beyond FL

Each item names what is needed and the FL result it extends, and classifies the extension as *routine*, *plausible but substantial*, or *genuinely open*.

**(1) Parametrized moduli spaces and transversality over $\operatorname{int}Q$.**
- *Needed.* Generic small perturbations for the prescribed family $\{g_t\}$, which is not generic on the positive pieces. They must make regular:
  - the free strata $\mathcal M^{*,0}_{\mathfrak t_e(\ell)}(Q)\times\Sigma$ at every level;
  - the cut-down parametrized strata of anti-self-dual connections;
  - the parametrized Seiberg–Witten moduli spaces, as Seiberg–Witten moduli spaces.
- *FL.*
  - Memoir Thm 2.1.1 = FL2a Thm 2.13 (generic $(g,\rho,\tau,\vartheta)$ for one metric; the proof is in Feehan's generic-metric paper).
  - FL1 Thm 1.3 (holonomy perturbations, fixed metric, all levels). Its $\ell>0$ case is argued in one paragraph (FL1 §5.1.3), and it excludes zero-section and reducible points from its scope.
  - FL2a Prop. 2.16 (Seiberg–Witten, generic $\tau$).
- *Status: routine.* Genericity must come from perturbations of FL1's holonomy type, not from the metric. Sard–Smale applies with the parameters $t$. FL never state simultaneous transversality at all levels (b-compactness §4.2); it is needed here too.

**(2) Compactness over $\bar Q$ with neck-stretching faces.**
- *Needed.* Item (A) of §2.4.
- *FL.* FL1 Thm 1.1 and Thm 4.20 (closed $X$, one metric); Memoir Thm 2.1.3; FL1 Lemmas 4.3 and 4.4 and Thm 4.10; the smallness condition FL1 (2.34).
- *Outside FL.* Analysis on necks (Morgan–Mrowka–Ruberman; Donaldson's book on Floer homology), together with three facts:
  - the spinor vanishes on cylinders of positive scalar curvature (Weitzenböck);
  - the flats on $S^3$ and on $L(4,1)$ are nondegenerate ($H^1(Y;\mathrm{ad})=0$);
  - the flat Dirac operators are invertible.
- *Status: routine.* There is no account for SO(3) monopoles in FL; the manuscript writes one (Lemmas `analysis:compactness`, `analysis:neck`). FL1's constants depend on $\|\operatorname{Scal}_-\|$ and on the perturbation bound (2.34), and both are uniform here.

**(3) Fixed points of the circle action at faces: reducible zero-section pairs.**
- *Needed.* The classification of fixed points on each main component, without the hypotheses "generic metric" and "$b^+\ge1$". Both fail for components at faces, many of which have $b^+=0$, and for a family of dimension $n>b^+(X)$.
- *FL.*
  - FL2a Prop. 3.1 (needs $b_2^+\ge1$, a generic metric and a non-flat $\hat A$); FL2a Lemma 3.2 and Cor. 3.3 (Morgan–Mrowka).
  - FL2b Def. 3.20 and Lemma 3.21, Memoir (2.2.2) (good $w$); FL3 §2.1.
  - FL meet reducible zero-section pairs only in Memoir Ch. 11 (a path of metrics, $b^+=1$, anti-self-dual connections only), where they assume Hyp. 11.3.5.
- *What replaces it.* Hypothesis 2 of Theorem 2.3 is a localized form of goodness. It excludes reducible zero-section pairs on every component that contains a cap (row 5).
- *Status.* The cap part is routine. The phenomenon itself is new relative to FL: on components without a cap, which occur only at $J$-faces, these pairs exist for every metric whenever the charge allows. They must be excluded as limits through items (10) and (12).

**(4) Index and level bookkeeping across faces.**
- *Needed.* Item (B) of §2.4:
  - $\sum_jd_a(\hat Z_j)=d_a-3k$ and $\sum_jn_a(\hat Z_j)=n_a$, in the unframed convention;
  - the lens corrections $\delta_I$, $\delta_{\rm sp}$;
  - the reference fillings that make $\ell_j\in\mathbb Z_{\ge0}$;
  - the particle costs (net $\le-4$ in the ASD count, $\le-2$ in the spinor count).
- *FL.* Memoir (2.1.12)–(2.1.13), (2.3.14), (2.3.23)–(2.3.24); FL2b (3.20)–(3.25), Lemma 3.17, Cor. 3.18.
- *Status: routine.* It follows from the index theorem of Atiyah–Patodi–Singer with Donaldson's framing conventions. The lens table is an explicit computation through $\mathbb F_4$ and $\mathbb P(1,1,4)$.

**(5) Geometric representatives.**
- *Needed.* Properties (a)–(f) of §1.4.
- *FL.*
  - FL2b Lemmas 3.12, 3.13, 3.15, Def. 3.14 and Cor. 3.18. These describe closures at lower levels only. FL remark that the description "does not give the multiplicities", and that intersection-suitability is a technical restriction (Remark 3.19).
  - FL2b Cor. 4.7 and L1 Lemma 4.10. These restrict $\mu_p(h)$ to links of reducibles *in cohomology*, with leading term $\tfrac12\langle c_1(\mathfrak s)-c_1(\mathfrak t),h\rangle$ and, at level one, the term $\pi_X^*\mathrm{PD}[h]$ from the bubble.
- *The difference.* FL's representatives are generic sections defined on configurations that are irreducible near the cycle, and their behaviour at reducibles is used only through links, i.e. through gluing. The argument needs the pointwise dichotomy (b) at reducibles.
  - (b) holds for the canonical jumping-line divisor of a *sphere*: a degree-zero bundle on $\mathbb P^1$ is trivial.
  - (b) fails for theta divisors of surfaces of positive genus (T2 §4).
- *Status.*
  - (a), (b), (c), (e): routine (Grothendieck, Quillen; closedness in $C^0$).
  - (d): plausible (nodal degeneration of the determinant line).
  - (f): plausible but substantial. FL's $\bar{\mathcal W}$ is built from one ball $\nu(x)$ (FL2b Lemma 3.13). At a face where $\nu(x)$ lies on a component with zero spinor it degenerates, so sections sampled across components are needed, and they must be transverse at every broken stratum with an irreducible non-zero-section component.

**(6) The instanton end and the factor $2^{n_a-1}$.**
- *Needed.* Item (C) of §2.4.
- *FL.* FL2b Prop. 3.29 with Lemmas 3.22 and 3.24–3.28; FL2a Cor. 3.6 and Remark 3.9; Memoir (2.6.2).
- *Status: routine.*
  - The parameters $t$ are extra finite-dimensional variables in FL2a's Kuranishi model.
  - At an isolated regular point the link is $\mathbb P(\ker D_{A,\vartheta})$ cut by $h^c$ (FL2b Lemma 3.27), or $\mathbb{CP}^{n_a-1}$ if the Dirac operator is made surjective by a complex-linear perturbation, as the manuscript does (Prop. `analysis:first-stage`).
  - $\mu_c$ restricts to $2h$ (FL2b Lemma 3.28), so $\langle(2h)^{n_a-1},[\mathbb{CP}^{n_a-1}]\rangle=2^{n_a-1}$. FL's hypothesis $n_a>0$ is hypothesis 1.
  - Goodness of $w$, which FL2b uses through Lemma 3.21, is replaced by the requirement that the zero-section limit points of $\mathcal Z_e$ be exactly the points (α) (rows 2, 5, 8 and 10).
  - The sign $\sigma_0$ is common to all $e$ because $O^{\rm asd}(\Omega,w_e)$ is, for every $e$, the instanton orientation times the complex Dirac orientation (FL2b Def. 2.3).

**(7) No ends at the faces $t_i=-1$ from tuples whose main components are all irreducible.**
- *Needed.* Item (D) of §2.4 for tuples whose main components are irreducible, with or without spinor. This is row 9 of §3 without Seiberg–Witten components. Tuples with reducible components are items (10)–(12).
- *FL.* None, since FL work only on closed manifolds. The classical model is Donaldson's vanishing theorem for connected sums: the SO(3) gluing parameter is invisible to the cuts, so the limits form a space of dimension $1-4k<0$.
- *Status: routine,* provided that perturbations, representatives and phase sections are local to the components at such a face (§1.5; property (d)). The representatives of $\mu_c$ must be built from gauge-invariant quantities of phase weight two on each side, so that they do not depend on the gluing parameter.

**(8) Lens faces: regular gluing of the minimal trace cap, and cancellation.**
- *Needed.* Two statements.
  - (a) Over each regular main solution at a lens face, $\mathcal Z_e$ has exactly one end for each crossing in the cap, and nearby points of $\mathcal Z_e$ lie on these ends. This is gluing at a reducible flat on $L(4,1)$ with stabilizer $U(1)$. It is unobstructed:
    - the cap is psc and the Dirac operator on it is invertible;
    - the normal ASD index is one complex dimension, cut by $\mu_p([S_i])$;
    - the cap's $U(1)$ absorbs the gluing parameter.
  - (b) After weighting by $\varepsilon(e)$, the ends for $e$ and $e+\epsilon_i$ have opposite signs. The reasons:
    - the exterior data coincide, including the branch lists of multi-valued perturbations;
    - the two caps differ by tensoring with the line on $N_i$ with $c_1=-2x$, where $x(S_i)=1$;
    - the complex Dirac determinant contributes no sign, so the comparison sign is the ordinary $s_i$.
- *FL.* None. The nearest results are:
  - the change of orientation under change of integral lift (FL2b Lemma 2.6; Memoir Lemma 8.1.7) and the sign rule for lifts of the same $w_2$ (Memoir (2.5.3)). The latter does not apply here (§1.3);
  - the sum over $w$ in the Kronheimer–Mrowka structure theorem (FL6 Thm 2.2);
  - gluing at reducible flats for anti-self-dual connections (Donaldson's book; Morgan–Mrowka–Ruberman).
- *Status.* (a) is routine in kind, but no account exists for SO(3) monopoles apart from the manuscript (Props `gluing:regular-cap`, `gluing:collar`). (b) is plausible but substantial (Prop. `gluing:signs`).

**(9) Exclusion of reducible limits with no cut at any $J_i$, at every level (rows 4, 5).**
- *Needed.* There is no point of $M_{\mathfrak s}(g_t)\times\mathrm{Sym}^\ell(X)$ with $\ell=\ell(\mathfrak t_e,\mathfrak s)\ge0$, and no reducible zero-section pair at any level, that satisfies the incidence conditions inherited from $\bar{\mathcal V}(z)$. This must hold for every $t$ in $\operatorname{int}Q$ and on the lens faces.
- *FL.*
  - The hypothesis of FL2b Thm 3.33(a): no $\mathfrak s$ with $M_{\mathfrak s}\ne\emptyset$ and $\ell(\mathfrak t,\mathfrak s)\ge0$.
  - FL2b Remark 3.36 and (4.61), which bound the levels where Seiberg–Witten strata can lie.
  - The behaviour of exceptional classes in the level formula. In the proof of Memoir Thm 1 (§10.6), the basic classes $c_1(\mathfrak s)+(2k-1)e^*$ of the blow-up lie at level $\ell(\mathfrak t,\mathfrak s)-k(k-1)$, so a large exceptional evaluation forces negative level. Here the same mechanism works through a large odd $\langle\Lambda_0,E_\pm\rangle$ against a bounded $\langle K,E_\pm\rangle$ (Lemma `indices:end-exclusion`).
- *The difference.* FL's hypothesis asks for empty Seiberg–Witten moduli at non-negative level. Here those moduli spaces are typically non-empty. Wall-crossing on $\mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2$ gives $SW=\pm1$ on the whole Weitzenböck band, which is sharp (T3 §1.3). The exclusion is therefore relative to the cut-down: it uses (b) and (c), and the energy balance $3n-7m>C_0$.
- *Regularity.* None is used, neither for $M_{\mathfrak s}$ nor for the reducible zero-section strata.
- *What it does use.* A pointwise input with no FL counterpart: the chamber estimate on the positive pieces, *uniformly over $\bar Q$ including faces*. In FL-compatible terms: a Seiberg–Witten pair for $K=\Lambda+v$ with perturbation $F^+_{A_\Lambda}$ (FL2a (2.56)) on a positive piece with period $H$ exists only if $(v\cdot H)(K\cdot H)<0$, and a reducible zero-section pair only if $v\cdot H=0$. With the vertex classes $H_I$ this gives $v_P^2-\tfrac12\sum_{i\in I}h_i^2\le-2$, or else the exceptional case, which costs a unit of level (T3 Thm A, Lemmas B, C, Prop. D). FL use only counts of Seiberg–Witten solutions, never emptiness off a chamber.
- *Status.*
  - The lattice inequality is arithmetic and has been checked.
  - The cap bounds are routine.
  - The uniform chamber estimate is plausible but substantial. It needs the specific family, uniform compactness, and the order of choices of Cor. `estimates:choices`; the exposition lists it among the weak points.

**(10) Exclusion of tuples at $J$-faces with no irreducible non-zero-section component (row 8).**
- *Needed.* The inequality chain of row 8.
- *FL.* None, since there are no faces. The nearest results are the dimension count of FL2b Cor. 3.18 and the level bounds of FL2b (4.61).
- *Status: routine,* given items (1), (4), (5) and the chamber estimate of (9). The tangential bound for outer Seiberg–Witten components is parametrized FL2a Prop. 2.16 on a manifold with a psc cylindrical end. Spacing $3$ would suffice here (D-families §4.3).

**(11) Exclusion of mixed tuples at $J$-faces with no reducible zero-section component (row 9).**
- *Needed.* Normal regularity at Seiberg–Witten components inside mixed tuples.
  - It is obtained by equivariant perturbations whose inputs sample the irreducible non-zero-section component and whose outputs lie on the Seiberg–Witten component.
  - The coupling goes through gauge-invariant quantities of phase weight two, so it never compares frames across a neck.
  - Where the finite isotropy group acts nontrivially, the perturbations are multi-valued.
- *FL.* FL never regularize at Seiberg–Witten points:
  - at the top level they stabilize and keep the obstruction bundle (FL2a Thms 3.19, 3.21; Memoir §2.3.5);
  - at lower levels the background cokernel is part of FL3's obstruction space (FL3 Thm 8.3);
  - FL1's holonomy perturbations vanish at reducible connections (FL1 §1.1.1), so they cannot do this.
- *Status: plausible but substantial.* The technique is new. It needs a precise perturbation space and a Sard–Smale argument across strata where the isotropy group jumps (Lemma `analysis:samples`).

**(12) Exclusion of mixed tuples at $J$-faces containing reducible zero-section components (row 10).**
- *The manuscript's argument* (Lemma `analysis:projection`, Prop. `analysis:finite-induction`). Forget the reducible zero-section components, with their particles and cuts, but keep their parameters. The remaining components, with the common phase, form a Fredholm problem with finite isotropy whose index is negative. Perturbations that do not depend on the forgotten data make it transverse near the projections of all candidate limits. So the projections, and hence the limits, do not exist.
- *What it replaces in FL.* FL's method would need a model of a neighbourhood of such a tuple: obstructed gluing of a reducible zero-section component to nonabelian components across an $S^3$ neck. The gluing parameter would lie in $SO(3)/U(1)$, and the obstruction space would contain the cokernels of the normal ASD operator on $L_1\otimes L_2^{-1}$ and of the Dirac operator. That is the analogue at a face of two hypotheses:
  - Memoir Hyp. 7.8.1, for Seiberg–Witten strata (FL6 Hyp. 3.1 is the stratum-by-stratum version);
  - Memoir Hyp. 11.3.5, for reducible anti-self-dual connections in a path of metrics.

  Neither is proved in the sources, even on closed manifolds. FL3 Thm 1.1 proves only the existence half (FL3 §1.5.1), on a closed $X$ with a fixed metric, and it explicitly avoids long necks (FL3 §9.3). F19 treats anti-self-dual connections with one bubble.
- *What it does not need.* None of the following: continuity, injectivity or surjectivity of a gluing map; an obstruction section; transversality at the reducible component; an overlap construction.
- *What it needs.* Four ingredients:
  - (a) every retained equation, cut and energy cut-off is independent of the forgotten data (Lemma `analysis:R-independence`);
  - (b) the forgetful problem is transverse near the projections of all candidates, including Seiberg–Witten components as in (11);
  - (c) the set of candidate projections is compact. This is proved by induction over an ordering of degeneration types, each step's perturbation being small enough to preserve the earlier exclusions and the collars of the instanton points (Lemma `analysis:finite-data`);
  - (d) a lower bound $4+i-p\ge-2$ for the virtual index of each run of reducible zero-section components. This bound is arithmetic, has been checked, holds at spacing $4$, and is sharp: it fails at spacing $3$, where $-5$ is attained.
- *Status: genuinely open.* The argument is new and has no counterpart in FL; I know of no other source for it. The manuscript's proof is the only one, it is unverified, and this is the main analytic risk. Its cost is the local spacing $4$. T1 Remark 2.4 conjectures that obstructed gluing would remove the need for local spacing.

**(13) Multi-valued perturbations, weighted Stokes, coefficients.**
- *Needed.* The multi-valued terms of (11) and (12) make $\overline{\mathcal Z_e}$ a weighted branched one-manifold with rational weights, and Stokes' theorem is needed for such spaces. The weights must be $1$ near the points (α), since all such terms vanish there, and equal at paired ends of kind (β).
- *FL.* None. FL use single-valued generic data and integer (or real) counts throughout.
- *Status: routine.* The theory is standard (McDuff; Cieliebak–Mundet–Salamon; Lemma `analysis:stokes`). It is possibly avoidable, since the free stratum has stabilizer $\{\pm1\}$, which acts trivially.
- *Coefficients.*
  - The conclusion is needed only in $\mathbb Q$, because $\Omega$ is an integer computed from single-valued data.
  - The factor $2^{n_a-1}$ makes the identity useless over $\mathbb F_2$ once $n_a\ge2$. This is why the non-vanishing must be integral ($\Omega\not\equiv0\bmod2^N$, $2^N\nmid q$), and why the interval map $B$ must be integral. FL's own coefficients are rational as well (Memoir (2.6.2); FL6 Thm 3.2).

**(14) Order of choices and uniformity.**
- *Needed.* The constants must be chosen in an order compatible with all the above, and compactness and the chamber estimate must be uniform in that order. The order is: cap bounds, then delays, then exceptional evaluations, then the number of repetitions $M$, then lengths of the $Y$ seams and isolation lengths, then perturbation sizes.
- *FL.* None; their genericity is for one closed manifold.
- *Status: plausible* (Lemma `indices:end-exclusion`, Cor. `estimates:choices`).

---

## 5. The general form, and why only the empty form is available

**5.1 What FL's method would give in general.** Suppose the window were not empty. The analogue of Memoir Thm 8.1.9 would then read
$$\sigma_0\,2^{n_a-1}\,\Omega=-\sum_e\varepsilon(e)\sum_\zeta(-1)^{o(\zeta)}\,\#\big(\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{\,n_a-1}\cap\bar{\mathbf L}_\zeta\big),$$
where $\zeta$ runs over:

- (a) parametrized Seiberg–Witten strata $M_{\mathfrak s}(Q)\times\mathrm{Sym}^\ell(X)$, at all levels and faces;
- (b) strata of reducible zero-section pairs in the family, which are Kotschick–Morgan walls, and at faces these occur on components without caps;
- (c) mixed strata at $J$-faces.

Defining the links $\bar{\mathbf L}_\zeta$ requires:

- for (a) with $\ell=0$, a parametrized FL2a Thm 3.21 (routine);
- for (a) with $\ell\ge1$, a parametrized Memoir Hyp. 7.8.1, which is open even for one metric;
- for (b), a family version of Memoir Hyp. 11.3.5, which is open;
- for (c), obstructed gluing across a psc neck at a reducible component, for which I know no source.

Evaluating the links as $SW(\mathfrak s)$ times universal polynomials (Memoir Thms 10.1.1, 10.1.2) would also need the overlap construction of Memoir Ch. 6 (Overlap Thms 4.1, 4.2) in families.

**5.2 Consequence for the statement in the exposition.** The exposition's version (Theorem `thm:FL`; T1 Thm A) says "$2^{n_D-1}\Omega=-\#\{\text{abelian ends}\}$". That is not available as a theorem: without the gluing in 5.1, the abelian limits are not known to be ends of a one-manifold, so their number is undefined. What is proved, and all that is used, is Theorem 2.3. Its content is that the closure of $\mathcal Z_e$ never reaches an abelian limit. The phrase "the reducible strata do not occur" should accordingly read "no reducible stratum meets the closure of the cut-down free stratum". The reducible strata themselves are non-empty.

**5.3 Structural differences from FL.**

- **Source of $n_a$.** FL make $n_a$ positive by taking $\Lambda$ large (FL6, proof of Main Thm 1.2). Here $\Lambda$ is constrained ($\Lambda_0\cdot S_i=2$, and $|\Lambda\cdot H_I|\le\tfrac32$ for $I\ne\varnothing$ on the positive pieces), and $n_a$ comes from topology: each positive piece adds $\tfrac58$ and each interval subtracts $\tfrac18$. Enlarging $\Lambda$ on the positive pieces would widen the Weitzenböck band and admit Seiberg–Witten classes (D-families §1.3).
- **No families Seiberg–Witten vanishing.** The vanishing of a families Seiberg–Witten invariant would not substitute for (9): converting a vanishing count into vanishing contributions needs the gluing of 5.1. Moreover such an invariant is undefined here, since $b^+(X)\approx n/4<\dim Q$ (D-families §2.3).

**5.4 The overlap problem.** In FL's sense it arises only for neighbourhoods of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ with $\ell\ge2$ (Overlap §§1, 4; Memoir Thm 6.6.1), and it is not needed here. What remains is compatibility of the perturbations at the corners of $\bar Q$, which the product collars provide, and across degeneration types, which the induction of (12)(c) provides. No two gluing maps are ever compared.

---

## 6. Assessment

**What Theorem 2.3 extends.** It extends the *unconditional* part of FL's theory: FL1, FL2a, and FL2b Prop. 3.29 and Thm 3.33(a). It does not extend the Memoir's conditional formula. It needs none of Hyp. 7.8.1, the overlap problem, FL3, or the link pairings of Memoir Ch. 10.

**Classification of the extensions.**

| Class | Items |
|---|---|
| Routine | (1) parametrized transversality; (2) compactness with psc neck faces; (3) exclusion of reducible zero-section pairs on components containing a cap; (4) index bookkeeping; (5)(a)(b)(c)(e) representatives; (6) instanton end and $2^{n_a-1}$; (7) $J$-faces; (8)(a) lens gluing, in kind; (10) fixed tuples at $J$-faces; (13) multi-valued perturbations and rational Stokes |
| Plausible but substantial | (5)(d)(f) behaviour of the representatives at faces; (8)(b) cancellation at the lens faces; (9) the uniform chamber estimate, which is the input that replaces Seiberg–Witten invariants; (11) normal regularity at Seiberg–Witten components inside mixed tuples; (14) order of choices |
| Genuinely open | (12) exclusion of mixed limits containing reducible zero-section components, by forgetting them. This is the one place where the argument replaces, rather than extends, a step of FL (their gluing at reducibles) |

**Precisely where it goes beyond FL.**

- FL never have faces, ends, sums over $w_2$, or reducible zero-section pairs in their compactifications, except in the conditional Memoir Ch. 11.
- FL never regularize at Seiberg–Witten points.
- FL never use emptiness of Seiberg–Witten moduli spaces.
- FL never exclude a stratum by forgetting part of it.

---

## 7. Uncertainties

1. **Numbering.** FL theorem numbers follow the arXiv sources, as in the extraction notes; published numberings may differ (for instance, "FL2b Lemma 3.30" in the Memoir is Proposition 3.29 in the arXiv source).
2. **The $w_2$ remark in §1.3** is my Mayer–Vietoris computation. It assumes that every piece into which the $Y_{\pm2}$ seams cut $X$ has $H_1(\,\cdot\,;\mathbb Z/2)=0$. This holds for $W'$; I have not checked it for the caps, for $W_H$, or for a general negative-definite $V$ with $b_1(V)=0$. Where it fails, the conclusion that all $w_2(\mathfrak t_e)$ are distinct may fail too, and the consistency remark then constrains the corresponding subsums.
3. **Proofs not checked.** I have not checked the manuscript's proofs of Lemma `analysis:projection`, Lemma `analysis:R-independence`, Lemma `analysis:finite-data`, Prop. `analysis:finite-induction` or Prop. `gluing:signs`. Their structure is reported as stated; items (8)(b), (11) and (12) rest on them.
4. **Coupled perturbations in row 9.** That they can be both independent of forgotten data (row 10) and effective at Seiberg–Witten components (row 9) is asserted by the manuscript (Lemma `analysis:samples`) and was not checked.
5. **Exclusion of reducible zero-section pairs on cap components** (row 5) rests on the class $A$ with $A^2=0$ and $c\cdot A$ odd in each cap (Prop. `estimates:cap`). I did not check that the caps constructed in the manuscript contain such a class.
6. **Kronheimer–Mrowka.** The structure theorem is used only as an analogy (§1.3, item (8)), in the form restated in FL6 Thm 2.2; the original was not consulted.
7. **The claim that no source contains (12)** means no source among those read, and none known to me.
