# A family version of the Feehan–Leness SO(3)-monopole cobordism: the statement the argument needs, and where it goes beyond Feehan–Leness

*Independent draft 2.*

**Sources.** Statements of Feehan–Leness (FL) are taken from the verified extraction notes `a-cobordism.md`, `b-compactness.md`, `c-links.md` and `d-gluing.md` in this directory. I use their abbreviations and their numbering, which was inferred from the counters of the arXiv LaTeX sources and may differ from the published numbering:

| Abbreviation | arXiv |
|---|---|
| FL1 | dg-ga/9710032 |
| FL2a | math/0007190 |
| FL2b | dg-ga/9712005 |
| FL3 | math/9907107 |
| L1 | math/0106238 (level one) |
| Memoir | math/0203047 v4 |
| FL6 | math/0609530 |
| Overlap | 1211.0480 |
| F19 | 1910.14580 |

The argument is taken from the following, and manuscript results are cited by their LaTeX labels (for example Lemma `analysis:projection`):
- `exposition.tex`;
- `notes/T1-secondary.md` §§1–4;
- `notes/D-families.md`;
- `notes/T2-mu-classes.md` §§2–3;
- `notes/T3-wallcrossing.md` §§0–4;
- the manuscript sections `08-indices.tex`, `09-analysis.tex` and `10-gluing.tex`, with three short look-ups in `05-stack.tex` and `07-estimates.tex`.

Works other than FL and the manuscript are cited from memory and marked †.

**Classification used in §5.**
- *Routine*: an extension by known methods with no new idea; a careful write-up suffices.
- *Plausible but substantial*: a genuine piece of analysis that FL do not cover and that no citable theorem supplies. Either a proof is proposed, usually in the manuscript, or the method is standard in a neighbouring setting. I have not checked it independently.
- *Genuinely open*: no proof is available and none is proposed.

---

## 0. Summary

1. **The vanishing form is all that is needed.** The argument needs the *vanishing form* of the SO(3)-monopole cobordism. This is the family analogue of FL2b Theorem 3.33(a) (no reducible ends, hence $2^{n_a-1}$ times the Donaldson count vanishes), together with FL2b Proposition 3.29 (the instanton link). It is not the analogue of Memoir Theorem 1.
   - No Seiberg–Witten contribution is ever evaluated.
   - So nothing like Memoir Hypothesis 7.8.1, FL6 Hypothesis 3.1 or Overlap Theorem 4.2 is needed, and the overlap problem does not arise.
2. **The analogue goes beyond FL in five ways.**
   - A family of metrics over a cube whose faces stretch positive-scalar-curvature necks $S^3$ and $L(4,1)$, each carrying flat connections with stabilizers.
   - Reducible zero-section components (abelian anti-self-dual connections). FL exclude these by genericity of the metric; here they cannot be avoided at the $S^3$-faces.
   - Lens faces, whose ends cancel only after a weighted sum over $2^n$ spin$^u$ structures.
   - Exclusion of the reducible strata by incidence and lattice bounds and by the manuscript's projection, instead of by gluing.
   - Perturbations depending on several pieces at once, some multivalued, hence rational weights.
3. **Only one gluing theorem is needed.** It is an *unobstructed* gluing at the lens ends: an abelian anti-self-dual cap of charge $\tfrac14$, with stabilizer $U(1)$, glued across $L(4,1)$. The instanton end is FL2b Proposition 3.29 essentially verbatim.
4. **Regularity of the reducible strata.** No reducible stratum is required to be regular in FL's sense, namely surjectivity of the normal part of the deformation complex (compare FL2a §3.4: points of $M_{\mathfrak s}$ "might not be regular points of $\mathcal M_{\mathfrak t}$"). There are two qualifications.
   - Broken limits that contain a component in $\mathcal M^{*,0}$ together with a Seiberg–Witten component need regularity of the latter in a *coupled* problem, in which its circle symmetry is broken.
   - Broken limits that contain a reducible zero-section component need the projection.
   - Both are new.
5. **Classification.** Nothing that is needed is genuinely open. Three natural strengthenings are open but are not needed: a family formula with Seiberg–Witten terms, spacing 3, and a Floer-theoretic version. The decisive items are rated *plausible but substantial*:
   - the projection;
   - coupled regularity;
   - Seiberg–Witten localization uniformly up to the faces;
   - lens gluing with its orientation comparison;
   - compactness at faces.

---

## 1. Setting and notation

### 1.1 FL notation and the dictionary with the manuscript

Following FL (Memoir (2.1.6), (2.1.12), (2.3.10), (2.3.14); FL6 (3.1)): $\mathfrak t=(\rho,V)$ is a spin$^u$ structure with $V=W\otimes E$, and
$$\Lambda=c_1(\mathfrak t)=\tfrac12c_1(V^+),\qquad \kappa=-\tfrac14p_1(\mathfrak t),\qquad w=c_1(E),$$
$$d_a(\mathfrak t)=-2p_1(\mathfrak t)-\tfrac32(\chi+\sigma),\qquad n_a(\mathfrak t)=\tfrac14\big(p_1(\mathfrak t)+c_1(\mathfrak t)^2-\sigma\big),\qquad d_s(\mathfrak s)=\tfrac14\big(c_1(\mathfrak s)^2-2\chi-3\sigma\big),$$
$$\ell(\mathfrak t,\mathfrak s)=\tfrac14\big((c_1(\mathfrak t)-c_1(\mathfrak s))^2-p_1(\mathfrak t)\big).$$
A reducible pair is reducible with respect to $V=W'\oplus W'\otimes L$, with $\mathfrak s=(\rho,W')$ and $c_1(L)=c_1(\mathfrak t)-c_1(\mathfrak s)$. Then $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)\subset I\mathcal M_{\mathfrak t}$ with $\ell=\ell(\mathfrak t,\mathfrak s)$. Further notation:
- geometric representatives: $\bar{\mathcal V}(z)$ and $\bar{\mathcal W}$ (FL2b Definition 3.14);
- instanton link: $\mathbf L^{w,\varepsilon}_{\mathfrak t,\kappa}=\{\|\Phi\|^2_{L^2}=\varepsilon\}/S^1$ (FL2a Definition 3.7; Memoir (2.2.3));
- orientation: $O^{\rm asd}(\Omega,w)$ (FL2b Definition 2.3).

| FL | manuscript and notes |
|---|---|
| $w=c_1(E)$ | $c$ (or $c_e$) |
| $c_1(W^+)$, where $\mathfrak t=(\rho,W\otimes E)$ | $l$, the spin$^c$ determinant |
| $\Lambda=c_1(W^+)+w$ | $\Lambda=l+c$ |
| $\kappa$ | $\kappa=c_2(E)-c^2/4$ |
| $d_a(\mathfrak t)$ | $D_I=8\kappa-3(1+b^+)$ (equal when $b_1=0$) |
| $n_a(\mathfrak t)$ | $n_D=\Theta-\kappa$, with $\Theta=(\Lambda^2-\sigma)/4$ |
| $c_1(\mathfrak s)$ for a reducible | $K=\Lambda+v=l+2c_1(L_1)$ |
| $c_1(\mathfrak s)-c_1(\mathfrak t)=-c_1(L)$ | $v=c_1(L_1)-c_1(L_2)$ |
| $\ell(\mathfrak t,\mathfrak s)$ | $\ell=\kappa+v^2/4$, the "Feehan–Leness level" (the identity $\kappa=-v^2/4+\ell$) |
| $\mathcal M^{*,0}_{\mathfrak t}$ (irreducible, $\Phi\not\equiv0$) | type $P$ (T1 writes $F$) |
| $\iota(M^w_\kappa)$ (irreducible, $\Phi\equiv0$) | type $A$ |
| $\iota(M_{\mathfrak s})$ (reducible, $\Phi\not\equiv0$) | type $S$ |
| reducible zero-section pairs (FL3 §2.1) | type $R$ |
| $\mu_p(S_i)$, $\bar{\mathcal V}(S_i)$ | the sphere tests $x(S_i)$ |
| $\mu_p(z)$, $\bar{\mathcal V}(z)$ | the cap probes |
| $\mu_c=c_1(\mathbb L_{\mathfrak t})$, $\bar{\mathcal W}$, with exponent $n_a-1$ | the $\eta=n_D-1$ phase cuts, of character two |

In what follows the main components of a limit are called
- *$\mathcal M^{*,0}$-components*;
- *anti-self-dual components*;
- *Seiberg–Witten components*;
- *reducible zero-section components*.

### 1.2 Topology

1. $X$ is closed, connected, oriented and smooth, with $H_1(X;\mathbb Z)=0$ (so $H^2(X;\mathbb Z)$ is torsion-free) and $b^+(X)\ge1$.
2. $J_1,\dots,J_n\subset X$ are disjoint separating 3-spheres in linear order.
   - The components of $X\setminus\bigcup J_i$ are $Z_0,\dots,Z_n$, and $\hat Z_j$ is $Z_j$ with balls attached. Thus $X=\hat Z_0\#\cdots\#\hat Z_n$.
   - The outer pieces contain the caps, $C_-\subset\hat Z_0$ and $C_+\subset\hat Z_n$.
   - In the application each inner piece has $H_1=0$ and is of one of two kinds (Proposition `stack:lattice`):
     - negative definite with lattice $\langle-1\rangle^2$ and basis $a=\tfrac12(F_r+F'_l)$, $b=\tfrac12(F_r-F'_l)$;
     - $\mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2$ (the $m$ *positive pieces*).
3. $S_1,\dots,S_n$ are embedded 2-spheres with $S_i\cdot S_i=-4$.
   - $S_i$ meets $J_i$ in a circle, $S_i=D_i^-\cup D_i^+$, and $S_i\cap J_j=\emptyset$ for $j\neq i$.
   - The tubular neighbourhoods $N_i$ are pairwise disjoint, $N_i\cap J_j=\emptyset$ for $j\ne i$, and $\partial N_i\cong L(4,1)$.
   - Capping $D_i^\mp$ in $\hat Z_{i-1}$ and $\hat Z_i$ gives classes $F_{l,i}$ and $F_{r,i}$ of square $-2$, with $[S_i]=F_{l,i}-F_{r,i}$.

### 1.3 The family of metrics

Let $Q=[-1,1]^n$. For disjoint $\mathcal J,\mathcal N\subset\{1,\dots,n\}$ the open face is
$$F_{\mathcal J,\mathcal N}=\{t:\ t_i=-1\ (i\in\mathcal J),\ t_i=+1\ (i\in\mathcal N),\ |t_i|<1\text{ otherwise}\},\qquad F_{\emptyset,\emptyset}=\operatorname{int}Q.$$
For $t\in F_{\mathcal J,\mathcal N}$, $X_t$ is the complete manifold obtained by cutting $X$ along $J_i$ ($i\in\mathcal J$) and $\partial N_i$ ($i\in\mathcal N$) and attaching half-cylinders. The metric $g_t$ on $X_t$ has the following properties.
- It is a product with a round metric of positive scalar curvature on every half-cylinder.
- It is smooth in $t$ on each open face.
- Near $F_{\mathcal J,\mathcal N}$ it is obtained from the face metrics by inserting necks $[-T_i,T_i]\times J_i$ and $[-T_i,T_i]\times\partial N_i$, with $T_i\to\infty$ at the face. These necks are independent at corners (product collars).
- All other necks have bounded length on $\bar Q$. These include the seams along $Y_{\pm2}$ and the isolation necks next to the caps.

Since $J_i\cap\partial N_i\ne\emptyset$, these two are stretched at the opposite ends $t_i=\mp1$ of the same interval.

The following conditions are used only for Seiberg–Witten localization (condition 3 of Proposition 8):
- the positive pieces carry toric Kähler metrics with $\mathrm{Scal}\ge0$, positive somewhere;
- their periods are $H(a,b)=U+aX_1+bX_2$ with $(a,b)\in[0,\tfrac14]^2$, the lens faces being $a=\tfrac14$ and $b=\tfrac14$;
- the corner at which both adjacent $J$'s are stretched is replaced by a product tube $S^2\times S^1\times[0,L]$;
- the caps carry fixed generic metrics.

These are manuscript Theorem `geometry:family` and Section 7; see T3 §§1–3.

### 1.4 The spin$^u$ structures $\mathfrak t_e$

**Data.** Fix:
- a spin$^c$ structure $\mathfrak s_0=(\rho,W)$ with $\langle c_1(\mathfrak s_0),[S_i]\rangle=2$;
- a class $w_0$ with $\langle w_0,[S_i]\rangle=0$;
- $\kappa$ with $\kappa+\tfrac14w_0^2\in\mathbb Z$.

For $e\in\{0,1\}^n$ put
$$w_e=w_0+\sum_ie_i\,\mathrm{PD}[S_i],\qquad c_2(E_e)=\kappa+\tfrac14w_e^2=\kappa+\tfrac14w_0^2-|e|,\qquad \mathfrak t_e=(\rho,W\otimes E_e).$$

**Invariance of the indices.** $\Lambda_e=c_1(\mathfrak s_0)+w_e$ and $\Lambda_e^2=\Lambda_0^2$ (since $\Lambda_0\cdot S_i=2$, $S_i^2=-4$ and $S_i\cdot S_j=0$). Also $p_1(\mathfrak t_e)=-4\kappa$. Hence $d_a(\mathfrak t_e)$ and $n_a(\mathfrak t_e)$ do not depend on $e$ (T1 Definition 1.1).

**Second Stiefel–Whitney classes.** $w_2(\mathfrak t_e)\equiv w_e\pmod2$, and these classes *do* depend on $e$.
- $\mathrm{PD}[S_i]$ restricts to $0$ on $X\setminus N_i$ and to $-4$ times the generator on $N_i$.
- Modulo 2 it is the image of the nonzero class of $H^1(\partial N_i;\mathbb Z/2)$.
- It is nonzero in $H^2(X;\mathbb Z/2)$, because a half $F_{l,i}$ or $F_{r,i}$ pairs oddly with a lattice generator. For example $F_r\cdot a=-1$ on a negative piece (Proposition `stack:lattice`).

So the $\mathfrak g_{\mathfrak t_e}$ are in general $2^n$ different SO(3) bundles with the same $p_1$. Write $e^{(i)}$ for $e$ with $e_i$ replaced by $1-e_i$. The bundles for $e$ and $e^{(i)}$ agree over $X\setminus N_i$ and over $N_i$, and are clutched along $\partial N_i$ by the order-two character. On the cobordism $W'$ itself $\mathrm{PD}(S)=2y$, and the two bundles coincide there (T2 §1).

**Goodness.** Each cap contains a class $A$ with $A^2=0$ and $\langle w_0,A\rangle$ odd (proof of Proposition `estimates:cap`), and the $S_i$ miss the caps. So every $w_e$ is good in the sense of Memoir Definition 2.2.1.

### 1.5 Equations, perturbations, moduli spaces

**Equations.** For $g_t$ we use the perturbed SO(3)-monopole equations of Memoir (2.1.10), with holonomy terms as in FL1 (1.3). In the manuscript's form (`eq:indices:equations`) they read $D_a\Phi=P_D$ and $\rho(F_a^{0,+})=(\Phi\Phi^*)_{00}+P_+$.

**Perturbation terms.** There are three kinds (manuscript §§9.1–9.3).
1. *Single-piece terms.* These are holonomy perturbations of the kind used in FL1 §2: graphs in one piece, energy cut-offs as in FL1 (2.23), and dependence on $t$ only through the parameters retained on that piece.
   - At $\Phi\equiv0$ they reduce to the perturbation of the anti-self-dual equation used for the instanton count. So $\iota\colon M^w_\kappa\hookrightarrow\mathcal M_{\mathfrak t}$ persists, as in FL2a (3.5).
   - At the finitely many counted instantons they include terms complex-linear in $\Phi$ that make the Dirac operator onto (Proposition `analysis:first-stage`).
2. *Several-piece terms.* These are invariant functions of holonomies and transported spinor values on graphs in several pieces, with one base frame per piece, and with localized outputs.
   - They are supported where the stabilizer of the sampled data is finite. Here the relevant group is the product of the gauge groups of the pieces and the common circle acting on $\Phi$.
   - In particular they vanish near every circle-fixed configuration.
   - They also vanish near every configuration whose sampled piece carries a reducible zero-section configuration (Lemma `analysis:R-independence`).
3. *Multivalued terms.* Finitely many terms of the second kind are multivalued: finite lists of branches with rational weights (Lemma `analysis:samples`).

All terms are small in norms that decay exponentially along the necks, compatible with faces and corners, and equal on $X\setminus N_i$ for $e$ and $e^{(i)}$ (Theorem `analysis:regularization`).

**Moduli spaces.**
$$\mathcal M_{\mathfrak t}(Q)=\{(t,[A,\Phi]):\ t\in\operatorname{int}Q,\ (A,\Phi)\ \text{solves the equations for }g_t\}$$
is taken modulo determinant-one gauge transformations. The circle acts by $\Phi\mapsto e^{i\theta}\Phi$, and $-1$ acts trivially (Memoir (2.1.9)). It contains the subspaces
- $\mathcal M^{*,0}_{\mathfrak t}(Q)$, of dimension $d_a+2n_a+n$ for generic data;
- $\iota(M^w_\kappa(Q))$, where $M^w_\kappa(Q)=\{(t,[\hat A]):\hat A\ \text{anti-self-dual for }g_t\}$ (perturbed);
- the reducibles.

### 1.6 Cohomology classes and their representatives

**(a) The classes $\mu_p(S_i)$, of degree 2.** These need representatives $\mathcal V(S_i)$ of real codimension two with five properties.
1. They are transverse to the irreducible strata.
2. A connection that is reducible over $S_i$, $\mathfrak g|_{S_i}=i\underline{\mathbb R}\oplus L$ with $\langle c_1(L),[S_i]\rangle=0$, does not lie in the closure of $\mathcal V(S_i)$.
3. If $[A_\alpha,\Phi_\alpha]\in\mathcal V(S_i)$ converges to an ideal limit none of whose points lies on the support of $\mathcal V(S_i)$, then the limiting connection lies in the closure of $\mathcal V(S_i)$.
4. At a $J_i$-face, $\mathcal V(S_i)$ is the union of half-representatives of $\mu_p(F_{l,i})$ and $\mu_p(F_{r,i})$, each defined on its own piece. Note that $\langle w_e,F_{l,i}\rangle$ and $\langle w_e,F_{r,i}\rangle$ are even.
5. At an $N_i$-face, $\mathcal V(S_i)$ is a condition on the cap alone.

The supports of different $\mathcal V(S_i)$ are disjoint from each other and from the cap cuts. There are two candidates.
- *The determinant-line divisor.* This is the zero set of the canonical section of the determinant line of $\bar\partial$ on $E|_{S_i}\otimes(\det E|_{S_i})^{-1/2}$ over $S_i\cong\mathbb P^1$ (the jumping-line divisor). It represents $\pm\mu_p(S_i)$ (T2 Proposition 2.3 and Corollary 3.3; Donaldson–Kronheimer §5.2†).
- *The manuscript's representative.* This uses normalized holonomy with the zero-winding modification (Lemmas `analysis:zero-winding`, `analysis:segmentation` and `analysis:incidence`). It represents $\pm\mu_p(S_i)$ by T2 Theorem 2.2.

**(b) The cap classes.** $z$ is a monomial in point classes and surface classes of the caps, with FL's representatives $\bar{\mathcal V}(z)$ (FL2b Lemma 3.12 and Definition 3.14). It is intersection-suitable by FL2b Lemma 3.17, since it has no $H_3$ factor.

**(c) The phase cuts.** These are $\eta=n_a-1$ sections of the circle-weight-two line $\mathbb L_{\mathfrak t}$, whose first Chern class is $\mu_c$ (FL2b (3.10)–(3.12)).
- They are built from spinor samples on all pieces, rather than pulled back from a neighbourhood of one point as in FL2b Lemma 3.13.
- They are quadratic near the counted instantons (Proposition `analysis:instanton-link`).

**The cut-down free space.**
$$\mathcal Z_e=\bar{\mathcal V}(z)\cap\textstyle\bigcap_i\bar{\mathcal V}(S_i)\cap\bar{\mathcal W}^{\,\eta}\cap\mathcal M^{*,0}_{\mathfrak t_e}(Q)/S^1 .$$
When $\deg z=d_a-n$ its dimension is $(d_a+2n_a+n-1)-\deg z-2n-2\eta=1$.

### 1.7 The secondary invariant

$$D^{w_0}_{X,Q}(z\,S_1\cdots S_n)=\sum_{e\in\{0,1\}^n}\varepsilon(e)\,\#\Big(\bar{\mathcal V}(z)\cap\textstyle\bigcap_{i}\bar{\mathcal V}(S_i)\cap M^{w_e}_\kappa(Q)\Big),\qquad \deg z=d_a(\mathfrak t_0)-n.$$
Here:
- the count uses Donaldson's orientation $o(\Omega,w_e)$ and the orientation of $Q$;
- $\varepsilon(e)=\prod_i\varepsilon_i(e_i)$ with $\varepsilon_i(1)=-s_i\varepsilon_i(0)$;
- $s_i$ is the orientation comparison sign of the two minimal trace caps on $N_i$ (Proposition `negative:local-sign`).

This is the manuscript's $\Omega$. Its properties:
- It is an integer.
- It is not a diffeomorphism invariant of $X$, since it depends on the face structure of the family.
- The individual summands are not invariant under deformations of the family. The weighted sum is invariant under deformations that preserve the faces (T1 Proposition 1.4, rated plausible).

It is the family counterpart of $D^w_X(z)=\#(\bar{\mathcal V}(ze)\cap\bar M^{w+\mathrm{PD}[e]}_{\kappa+1/4}(\tilde X))$ (Memoir (2.5.2)).

---

## 2. Ideal limits

### 2.1 Ideal tuples

Let $t\in F_{\mathcal J,\mathcal N}$ and $k=|\mathcal J|$. The *pieces* of $X_t$ are:
- the components $P_0,\dots,P_k$ of $X\setminus\big(\bigcup_{\mathcal J}J_i\cup\bigcup_{\mathcal N}N_i\big)$, completed with cylindrical ends;
- the completed caps $\hat N_i$, $i\in\mathcal N$.

An *ideal tuple over $t$* consists of the following.
1. *Main components.* For each $j$, $[A_j,\Phi_j,\mathbf x_j]$, where $(A_j,\Phi_j)$ is a finite-energy solution on $(P_j,g_t)$ for the restricted spin$^u$ structure, converging exponentially on each end to a flat connection with zero spinor, and $\mathbf x_j$ is a finite set of points of $P_j$ with positive integer weights.
2. *Caps.* For each $i\in\mathcal N$, a finite-energy anti-self-dual connection $[B_i]$ on $\hat N_i$ with weighted points $\mathbf y_i$.
3. *Neck chains.* For each cut neck $Y=J_i$ or $\partial N_i$, a finite, possibly empty, chain of nonconstant finite-energy anti-self-dual connections on $\mathbb R\times Y$ with zero spinor.
4. *Matching.* The flat limits match, and the charges add up to $\kappa$.

Convergence is the analogue of Memoir Definition 2.1.2 and FL1 Definition 4.19, with three additions:
- $L^2_{k,\mathrm{loc}}$ convergence after gauge on compact subsets of the pieces away from the points;
- weak convergence of the curvature densities, with atoms $8\pi^2\cdot$(weight);
- convergence of translates on the necks to the chains, and convergence of the parameters.

**Theorem 1 (compactness; analogue of FL1 Theorems 1.1 and 4.20 and Memoir Theorem 2.1.3).** Let the data be as in §§1.2–1.5, with perturbations in a sufficiently small ball. The smallness is of the type FL1 (2.34), uniform in $t$, with exponentially decaying tails along the necks. Then the following hold.
1. Every sequence in $\mathcal M_{\mathfrak t}(Q)$ has a subsequence converging to an ideal tuple over some $t\in\bar Q$. Only finitely many faces, charge assignments and numbers of points occur.
2. The spinor does not concentrate: $|\Phi|^4\,d\mathrm{vol}$ has no atoms in a weak limit (Lemma `analysis:compactness`). For FL's perturbations, FL1 Lemma 4.4 even gives a $C^0$ bound, and it is uniform here because the scalar curvature is bounded below uniformly. Consequently the rescaled limits at points are anti-self-dual with zero spinor. On caps and neck chains $\Phi\equiv0$, by the Weitzenböck formula and positive scalar curvature.
3. *Charges and flats.*
   - Points carry positive integer charges.
   - Nonconstant neck connections carry positive charges, integral on $\mathbb R\times S^3$ and in $\tfrac14\mathbb Z$ on $\mathbb R\times L(4,1)$.
   - The flat limits are among finitely many: the trivial flat on $S^3$, with stabilizer $SO(3)$; on $L(4,1)$, two central flats with stabilizer $SO(3)$ and the flat with holonomy of trace zero, with stabilizer $U(1)$.
   - All of these flats are nondegenerate ($H^1(Y;\mathrm{ad}\rho)=0$), with invertible flat Dirac operator.
   - Along stretches without loss, convergence to the flat is exponential (Lemma `analysis:neck`).
4. The space $\bar{\mathcal M}_{\mathfrak t}(\bar Q)$ of limits is compact, Hausdorff and second countable. The circle action and $\|\Phi\|^2_{L^2}$ extend continuously.

**Proposition 2 (circle-fixed components and levels; analogue of FL2a Proposition 3.1 and Lemmas 3.11–3.13, Memoir (2.2.2) and (2.3.14), FL2b Lemma 3.32).**
1. **Fixed tuples.** The circle acts on an ideal tuple through its main components, so a tuple is fixed if and only if every main component is fixed. A main component is fixed if and only if it is of one of three kinds:
   - (a) $\Phi_j\equiv0$ and $\hat A_j$ irreducible: an *anti-self-dual component*;
   - (b) $A_j$ reducible with respect to $V=W'\oplus W'\otimes L$ and $\Phi_j=\Psi\oplus0\not\equiv0$, so that $(B,\Psi)$ solves the Seiberg–Witten equations for $\mathfrak s=(\rho,W')$ with perturbation $F^+_{A_\Lambda}$ (FL2a Lemma 3.12): a *Seiberg–Witten component*;
   - (c) $\Phi_j\equiv0$ and $\hat A_j=d_{\mathbb R}\oplus A_L$: a *reducible zero-section component*, that is, an abelian anti-self-dual connection.
2. **Kind (c) in FL and here.**
   - On a closed manifold with $b^+\ge1$, a generic metric and $\hat A$ non-flat, FL2a Proposition 3.1 shows that only (a) and (b) occur. FL exclude (c) by genericity together with the choice of $w$ (FL2a Lemma 3.2 and Corollary 3.3; FL3 §2.1).
   - Here (c) does occur when $\mathcal J\ne\emptyset$. On a union of consecutive negative pieces ($b^+=0$, $H^1=0$), every class $v\equiv w\pmod2$ carries a unique abelian anti-self-dual connection for every value of the parameters.
   - On a positive piece these connections occur on walls $\langle v,H(a,b)\rangle=0$, which have codimension at most one in the parameters.
   - The caps exclude (c) on every piece that contains a cap (§4, row 6).
3. **Levels.** Let a component be of kind (b) or (c), with line difference $v_j$. Fill its lens ends by the reference abelian connections of Proposition `indices:lens-index`, which have charges $0,\tfrac14,1$ when $\langle v_j,S_i\rangle=0,\pm2,\pm4$. Then
$$\kappa_j=-\tfrac14v_j^2+\ell_j,\qquad \ell_j\in\mathbb Z_{\ge0},$$
where $\ell_j$ is the sum of three contributions:
   - the weights of the points on $P_j$;
   - the neck charges allocated to $P_j$;
   - the excess of the actual cap charges over the reference charges (Lemma `indices:virtual-sums`).

   For $k=0$, $\mathcal N=\emptyset$ and kind (b), $\ell_0=\ell(\mathfrak t,\mathfrak s)$, and the component is a point of $M_{\mathfrak s}(g_t)\times\mathrm{Sym}^{\ell}(X)$, as in Memoir (2.3.14).
4. **Bubbles and neck connections are irreducible.** There is no non-flat reducible anti-self-dual connection on $S^4$, on $\mathbb R\times S^3$ or on $\mathbb R\times L(4,1)$, because their $H^2$ is torsion.

**Lemma 3 (index identities; analogue of FL2b (3.20)–(3.25) and Overlap (2.10); Lemmas `indices:virtual-sums` and `indices:loss-budget`).** Consider a tuple, with or without matching, over $F_{\mathcal J,\mathcal N}$ with main components $j=0,\dots,k$. For each $j$ let:
- $p_j$ be the parameters retained on $P_j$, restoring one for each lens end;
- $s_j$ be the sphere cuts assigned to $P_j$ (at a $J_i$-cut, the half on whose side its event lies);
- $z_j$ be the cap degree on $P_j$.

On the virtually filled piece put
$$q_j=d_a(\mathfrak t_j)+p_j-2s_j-z_j,\qquad i_j=q_j+2n_a(\mathfrak t_j).$$
Then
$$\sum_{j=0}^k(q_j+4)=4,\qquad \sum_{j=0}^ki_j-2\eta=2-4k .$$

Losses are accounted for as follows.
- A point of weight $a$ lowers $d_a$ by $8a$ and $d_a+2n_a$ by $6a$. Compare $\dim\mathcal M_{\mathfrak t(\ell)}=\dim\mathcal M_{\mathfrak t}-6\ell$ in FL2b, after (3.21).
- Such a point restores at most $4a$ dimensions, through its position and the cuts it releases.
- A separated lens cap of charge $\kappa_N$ costs $\delta_I-1$ in the instanton count and $\delta_{\rm sp}-1$ in the monopole count. Here $\delta_{\rm sp}=6\kappa_N$ at the central flats, and $\delta_{\rm sp}=2+6(\kappa_N-\tfrac14)$ at the trace-zero flat (Proposition `indices:lens-index`).

---

## 3. The statements the argument needs

**Theorem 4 (instanton link over the cube; analogue of FL2b Proposition 3.29 with Lemmas 3.22 and 3.24–3.28, FL2a Corollary 3.6, Memoir (2.6.2)).** Let $\mathfrak t=\mathfrak t_e$ with $n_a(\mathfrak t)\ge1$ and $\deg z=d_a(\mathfrak t)-n$. Assume:
1. $\mathcal I_e:=\bar{\mathcal V}(z)\cap\bigcap_i\bar{\mathcal V}(S_i)\cap\bar M^{w_e}_\kappa(\bar Q)$ is a finite set of points of $M^{w_e,*}_\kappa(\operatorname{int}Q)$: top level, irreducible, not on a face. At these points the parametrized cut-down problem is regular.
2. At each point of $\mathcal I_e$ the perturbed Dirac operator $D_{A,\vartheta}$ on $V^+$ is surjective, so $\dim_{\mathbb C}\ker D_{A,\vartheta}=n_a$.
3. Every limit of $\mathcal Z_e$ all of whose main components have $\Phi\equiv0$ lies in $\iota(\mathcal I_e)$.

Then, for small generic $\varepsilon$:
- The part of $\bar{\mathcal Z}_e$ with $\|\Phi\|^2_{L^2}\le\varepsilon$ is a disjoint union of half-open arcs ending on $\iota(\mathcal I_e)$.
- The normal link at a point of $\mathcal I_e$ is $\mathbb P(\ker D_{A,\vartheta})\cong\mathbb{CP}^{n_a-1}$.
- $\mu_c$ restricts there to $2h$, the class of $\mathcal O(2)$, by FL2b Lemma 3.28.
- With the boundary orientation from $O^{\rm asd}(\Omega,w_e)$ and the orientation of $Q$,
$$\#\Big(\bar{\mathcal V}(z)\cap\textstyle\bigcap_i\bar{\mathcal V}(S_i)\cap\bar{\mathcal W}^{\,n_a-1}\cap\mathbf L^{w_e,\varepsilon}_{\mathfrak t_e,\kappa}(Q)\Big)=\sigma_0\,2^{\,n_a-1}\,\#\Big(\bar{\mathcal V}(z)\cap\textstyle\bigcap_i\bar{\mathcal V}(S_i)\cap M^{w_e}_\kappa(Q)\Big),$$
with $\sigma_0\in\{\pm1\}$ independent of $e$ (FL2b Lemmas 3.24 and 3.25).

On the hypotheses:
- Hypotheses 1 and 2 are arranged by perturbation (Propositions `analysis:first-stage` and `analysis:instanton-link`). Because of 2, FL2b Lemma 3.27 is needed only in the case $c=\dim\operatorname{Coker}D_{A,\vartheta}=0$.
- Hypothesis 3 is the analogue of FL2b Lemma 3.22(2). It is part of the exclusion (Proposition 8).

**Definition 5 (permitted tuples).** The *permitted* part of $\bar{\mathcal M}_{\mathfrak t_e}(\bar Q)$ consists of three kinds of tuple.
1. The points of $\mathcal M^{*,0}_{\mathfrak t_e}(\operatorname{int}Q)$.
2. The points of $\iota(\mathcal I_e)$.
3. For each $i$, tuples over $F_{\emptyset,\{i\}}$ such that:
   - the main component is an $\mathcal M^{*,0}$-component on $X\setminus N_i$, with no points and no neck chain;
   - the cap is the reducible anti-self-dual connection on $\hat N_i$ of charge $\tfrac14$, asymptotic to the trace-zero flat, with no points.

Every other ideal tuple is *non-permitted*.

**Theorem 6 (secondary SO(3)-monopole cobordism, vanishing form).** Let the data be as in §1, and assume:
1. $H_1(X;\mathbb Z)=0$, $b^+(X)\ge1$, and every $w_e$ is good;
2. $\langle c_1(\mathfrak s_0),[S_i]\rangle=2$ and $\langle w_0,[S_i]\rangle=0$ for $1\le i\le n$;
3. $n_a(\mathfrak t_0)\ge1$, and $\deg z=d_a(\mathfrak t_0)-n$ with $z$ a monomial in point and surface classes of the caps;
4. the perturbations and representatives are as in §§1.5–1.6, are generic, and satisfy hypotheses 1 and 2 of Theorem 4;
5. for every $e$, the closure of $\mathcal Z_e$ in $\bar{\mathcal M}_{\mathfrak t_e}(\bar Q)/S^1$ contains no non-permitted tuple.

Truncate $\sum_e\varepsilon(e)\,\mathcal Z_e$ at the instanton links and at the lens collars of Proposition 7. The result is a compact, oriented, weighted one-manifold with rational weights. Its boundary consists of two kinds of point.
- The instanton-link points, which contribute $\sigma_0\,2^{n_a-1}D^{w_0}_{X,Q}(zS_1\cdots S_n)$.
- The lens-collar points, which cancel in the pairs $\{e,e^{(i)}\}$.

Consequently
$$2^{\,n_a(\mathfrak t_0)-1}\,D^{w_0}_{X,Q}(z\,S_1\cdots S_n)=0\quad\text{in }\mathbb Q,$$
and therefore $D^{w_0}_{X,Q}(zS_1\cdots S_n)=0$, since it is an integer.

*Proof outline.*
1. By Theorem 1 and hypothesis 5, $\bar{\mathcal Z}_e\setminus\mathcal Z_e$ consists of tuples of the second and third kinds in Definition 5. In particular hypothesis 3 of Theorem 4 holds.
2. Theorem 4 describes the ends at the second kind, and Proposition 7 those at the third.
3. Weighted Stokes for branched one-manifolds (Lemma `analysis:stokes`; McDuff†, Cieliebak–Mundet–Salamon†) gives total weighted boundary zero.
4. Item 4 of Proposition 7 cancels the lens collars. ∎

*Relation to FL.* Take $n=0$: a closed $X$ with a fixed generic metric, no family and no sphere cuts. Then Theorem 6 is a *cut-down* form of FL2b Theorem 3.33(a).
- FL2b Theorem 3.33(a) assumes $(c_1(\mathfrak t)-c_1(\mathfrak s))^2<p_1(\mathfrak t)$ for every $\mathfrak s$ with $M_{\mathfrak s}\neq\emptyset$; that is, there is no reducible in $\bar{\mathcal M}_{\mathfrak t}$ at any level. Its conclusion is $\#(\bar{\mathcal V}(z)\cap\bar M^w_\kappa)=0$, and it is proved without any gluing hypothesis.
- Hypothesis 5 is weaker in one respect: Seiberg–Witten strata at non-negative level may exist, provided they miss the closure of the cut representatives.
- Hypothesis 5 is stronger in another: it covers the faces of $\bar Q$.
- The general identity with reducible ends is Memoir Theorem 8.1.9 (8.1.21). For level $\ge1$ it requires Hypothesis 7.8.1, through Definition 8.1.3.

**Proposition 7 (lens ends; no FL counterpart; Propositions `gluing:regular-cap`, `gluing:collar`, `gluing:signs`, Lemma `indices:lens-charge`, Corollary `indices:trace-minimum`).** Fix $i$ and $e$.
1. **The cap.** Consider the framed problem on $\hat N_i$: anti-self-dual connections of charge $\tfrac14$, asymptotic to the trace-zero flat $\gamma$, cut by $\mathcal V(S_i)$.
   - Its solutions lie on the abelian connection with $\langle v,S_i\rangle=\pm2$. For the holonomy representative they are the crossings of its sweep with $-1$; for the determinant-line divisor, the abelian connection itself, with local multiplicity $\pm1$ (T2 Proposition 3.2).
   - They are regular after a perturbation of the normal operator that vanishes at the abelian connection (the normal complex index is one).
   - Each is fixed by $H=\mathrm{Stab}(\gamma)\cong U(1)$, and their oriented count is $\pm1$.
   - The coupled Dirac operator is invertible there: positive scalar curvature, index $0$.
2. **The main problem.** Over $F_{\emptyset,\{i\}}$ the main problem on $X\setminus N_i$ (an $\mathcal M^{*,0}$-component, no points) is regular of dimension zero, with all cuts except $\mathcal V(S_i)$ and with the phase cuts. Its data for $e$ and $e^{(i)}$ coincide.
3. **Gluing and exhaustion.** Each pair (main point, cap point) is the limit of exactly one end of $\mathcal Z_e$. This end is a collar parametrized by the neck length. Every sequence in $\mathcal Z_e$ converging to the pair eventually lies in the collar. Branch weights are preserved, and no factor from $H$ appears.
4. **Orientations.** The collars for $e$ and $e^{(i)}$ over the same main point satisfy $\varepsilon(e)\,o_e=-\varepsilon(e^{(i)})\,o_{e^{(i)}}$.
   - The anti-self-dual part of the comparison is the one that defines $\varepsilon$ in the instanton count.
   - The Dirac part is complex-linear (the caps differ by tensoring with a line) and contributes $+1$.

**Proposition 8 (exclusion: sufficient conditions for hypothesis 5 of Theorem 6; Theorem `indices:exclusion`, Theorem `analysis:regularization`, T1 Theorem 4.1).** Let hypotheses 1–4 of Theorem 6 hold. Hypothesis 5 then follows from the conditions below.
1. **Regularity.**
   - (a) Every anti-self-dual main component, with its retained parameters and cuts, is regular. Hence $q_j\ge0$, strictly if it has a lens end, a point or a neck loss.
   - (b) Every Seiberg–Witten main component is regular for its own Seiberg–Witten deformation complex. Hence $d_s(\mathfrak s_j)+p_j+4\ell_j\ge0$; only this tangential statement is used.
   - (c) Consider a tuple that contains an $\mathcal M^{*,0}$-component, with matching forgotten. Its *projected problem* is formed by deleting its reducible zero-section components, their points and their cuts, while keeping their parameters. This problem has finite isotropy, and it is regular near the projections of all such tuples (Lemma `analysis:projection`, Proposition `analysis:finite-induction`).
2. **Representatives.** The sphere representatives have properties 1–5 of §1.6(a). Points that meet cuts obey the loss budget of Lemma 3: a missed sphere cut must be paid for by a point on its support, and different spheres by different points.
3. **Seiberg–Witten localization.** On every face, every Seiberg–Witten or reducible zero-section configuration on a union of consecutive pieces satisfies four conditions:
   - the chamber condition on its positive pieces (Theorem `estimates:clamp`(i); T3 Proposition E);
   - $\langle v,U\rangle=0$ near the cusp (T3 Proposition D);
   - on pieces containing a cap: no reducible zero-section configuration, and $v_W^2\le C_W$, $(\Lambda_W+v_W)^2\le C_W$ (Proposition `estimates:cap`);
   - all of this uniformly over $\bar Q$, including the faces.
4. **Numerical conditions.**
   - Positive pieces are at mutual distance at least $4$ and at distance at least $L_*$ from the caps.
   - $|\langle\Lambda_0,E_\pm\rangle|$ is odd and sufficiently large.
   - $3n-7m>C_0$, with $C_0$ depending only on the caps.

How each stratum is excluded is recorded in §4.

**Lemma 9 (family adjunction inequality; T1 Lemma 3.1, Corollary 3.2 and Proposition 3.4; the exposition's Lemma `lem:adj`).** Assume conditions 2 and 3 of Proposition 8. Let $\Gamma$ be a union of consecutive pieces carrying a Seiberg–Witten or reducible zero-section component, including limits with points, separated lens caps and halves at cut necks. Let:
- $s^-(\Gamma)$ be the number of sphere cuts assigned to $\Gamma$ that are not adjacent to a positive piece;
- $m(\Gamma)$ be the number of positive pieces in $\Gamma$.

Then
$$\kappa_\Gamma=-\tfrac14v_\Gamma^2+\ell_\Gamma\ \ge\ \tfrac12\big(s^-(\Gamma)+m(\Gamma)\big).$$
Two consequences follow.
1. *The unbroken case.* For $k=0$, let $T(v)$ be the number of $i$ with $\langle v,S_i\rangle=0$. Then $-\tfrac14v^2+T(v)\ge\tfrac{n-m}2-C$. Since $\kappa=\tfrac{n+3m}8+C'$, this gives $\ell-T(v)\le\tfrac{7m-3n}8+C''<0$. But incidence requires $\ell\ge T(v)$.
2. *The broken case.* With spacing $k_0$ between positive pieces, every maximal run of reducible components has
   - $\sum(q_j+4)\ge(3k_0-7)m-3k_0+5$, which is $\ge-2$ for $k_0\ge3$;
   - $\sum(4+i_j-p_j)\ge(k_0-4)m-k_0+2$, which is $\ge-2$ for $k_0\ge4$.

On its status:
- T1 records the lattice statement as checked by machine (§3.6) and as sharp. The bound in the second consequence is attained at spacing $3$.
- It has no counterpart in FL. Its role is that of the Seiberg–Witten input of Memoir Theorem 1: knowledge of the basic classes, together with the choice of $\Lambda$ (compare FL6 §4).

### 3.7 What is not claimed

1. **No formula with Seiberg–Witten terms.** There is no formula $2^{n_a-1}D^{w_0}_{X,Q}=\sum(\text{Seiberg–Witten terms})$ for the case in which reducible ends occur.
   - Such terms need links of the reducible strata. FL define these only through Hypothesis 7.8.1 (Memoir Definition 8.1.3), and only for a closed manifold with fixed metric.
   - In the family one would need, in addition, gluing at reducible zero-section components across necks.
   - The phrase "$2^{n_D-1}\Omega=-\#\{\text{abelian ends}\}$" (exposition, Theorem `thm:FL`; T1 Theorem A) should therefore be read only in the vanishing case of Theorem 6.
2. **The cancellation needs the weighted sum.** An individual $\mathcal Z_e$ has lens ends that do not cancel. Only the weighted sum over $e$ is a one-cycle relative to the instanton links.

---

## 4. Noncompactness: which strata must be excluded, and how

Every end of $\mathcal Z_e$ has an ideal limit (Theorem 1). Since no gluing theorem is available at the excluded strata, the exclusion must cover every face, level and kind of component. The manuscript therefore works with a class of *candidates* that is larger than the set of actual limits (§`analysis:candidates`). A candidate has:
- main components solving their own equations and assigned cuts;
- arbitrary admissible charge assignments for the omitted caps and neck chains;
- *no matching* across cut necks.

Every actual limit is a candidate. Because only necessary conditions are used, no stratum ever has to be parametrized, so no surjectivity or injectivity of a gluing map is needed anywhere except at the permitted ends.

**Strata of $\bar{\mathcal M}_{\mathfrak t_e}(\bar Q)$ that must be excluded from $\bar{\mathcal Z}_e$:**

| # | Stratum (meeting the closure of the cut representatives) | FL counterpart | Mechanism of exclusion | Regularity used | Status |
|---|---|---|---|---|---|
| 1 | Points on an $\mathcal M^{*,0}$-component (lower level), on any face | $\mathcal M^{*,0}_{\mathfrak t(\ell)}\times\Sigma$; FL2b Corollary 3.18 (codimension $\ge2\ell$) | Net loss $\ge2$ per unit of charge: $6$ lost, at most $4$ restored | Lower-level $\mathcal M^{*,0}$ strata with cuts | Routine |
| 2 | $k\ge1$ $S^3$-cuts, all main components $\mathcal M^{*,0}$ or anti-self-dual | None: FL have no necks | $\sum i_j-2\eta-1=1-4k<0$: each cut loses the 3-dimensional gluing parameter in $SO(3)$ and one neck parameter | Those components | Routine, given Theorem 1 |
| 3 | Anti-self-dual main components other than $\iota(\mathcal I_e)$: lower level, lens ends, $S^3$-cuts | $\bar M^w_\kappa$ in $\bar{\mathcal M}_{\mathfrak t}$; FL2b Lemma 3.21 | $q_j\ge0$, strictly with any loss, against $\sum(q_j+4)=4$ ($q=0$ forced when $k=0$) | Anti-self-dual components with cuts | Routine |
| 4 | Lens faces other than the third kind in Definition 5 | None | Penalty $\delta_{\rm sp}-1$: at least $5$ at central flats, $1+6h$ at trace charge $\tfrac14+h$; two caps give a negative dimension | The main component | Routine, given Lemma 3 |
| 5 | Unbroken Seiberg–Witten strata $M_{\mathfrak s}(g_t)\times\mathrm{Sym}^\ell(X)$ for *all* $\ell\ge0$ (interior or lens faces) | The reducible ends of Memoir Theorem 8.1.9, evaluated through links | Incidence needs $\ell\ge T(v)$ (§1.6(a), properties 2–3); Lemma 9 gives $\ell<T(v)$ when $3n-7m>C_0$. **The stratum need not be empty; its intersection with the closure of the cut representatives is.** | None, not even tangential | Deduction routine; condition 3 of Proposition 8 plausible but substantial |
| 6 | Unbroken reducible zero-section configurations | Excluded in FL by a generic metric and the choice of $w$ (FL2a Proposition 3.1, Lemma 3.2) | The single main component contains a cap; $\langle v,A\rangle$ odd forces $v|_W\neq0$; a generic cap metric with long isolation necks has no wall (Proposition `estimates:cap`) | None | Routine to plausible |
| 7 | $k\ge1$, no $\mathcal M^{*,0}$-component | None | $\sum(q_j+4)=4$ against lower bounds: $\ge4$ per anti-self-dual, $\ge8$ per outer Seiberg–Witten, $\ge-2$ per maximal run of reducible components (Lemma 9), so the sum is $\ge6$ | Anti-self-dual components; tangential regularity of Seiberg–Witten components, used only for short end components (Lemma `indices:end-exclusion`) | Routine, given Lemma 9 |
| 8 | $k\ge1$, with an $\mathcal M^{*,0}$-component and Seiberg–Witten components, no reducible zero-section component | None: FL never meet Seiberg–Witten components in broken limits | $1-4k-(\text{losses})<0$, using the full monopole index $i_j$ of each Seiberg–Witten component | **Full regularity at the Seiberg–Witten components in the coupled problem**, where the common circle is pinned by the $\mathcal M^{*,0}$-component and the isotropy is finite | Plausible but substantial (new) |
| 9 | $k\ge1$, with an $\mathcal M^{*,0}$-component and reducible zero-section components | None; compare Memoir Hypothesis 11.3.5 (reducible anti-self-dual connections in a path of metrics, assumed) | Projection: dimension $\le5-4N-\sum_{\text{runs}}\sum(4+i_j-p_j)\le3-2N<0$, where $N\ge2$ is the number of other components (the outer components are never of this kind) and each run contributes $\ge-2$ at spacing $\ge4$ | **None at the reducible zero-section components**; regularity of the projected problem near the projections of candidates | Plausible but substantial (new; decisive) |

**Strata that are kept:**
- $\iota(\mathcal I_e)$: Theorem 4 (routine).
- The minimal trace lens ends: Proposition 7 (plausible but substantial).

**Points over reducible components, and the spinor.**
- *The spinor never bubbles.* $|\Phi|^4$ has no atoms (Theorem 1, item 2), so bubbles are anti-self-dual connections on $S^4$ with zero spinor. This is also the situation in FL, where the $C^0$ bound of FL1 Lemma 4.4 gives it.
- *Points over a reducible component.* Points sitting over a Seiberg–Witten or reducible zero-section component (FL's factor $\mathrm{Sym}^\ell(X)$) are counted in $\ell_j$.
  - A point lying on the support of $\mathcal V(S_i)$ may pay for a missed cut $\mu_p(S_i)$. This is property 3 of §1.6(a), and it is the representative-level form of the term $\pi_X^*\mathrm{PD}[S_i]$ that appears in $\mu_p$ on level-one links (L1 Lemma 4.10).
  - Distinct spheres need distinct points, because their supports are disjoint.
  - Points elsewhere only increase the deficit.
- *Reducibles cannot bubble off.* By Proposition 2, item 4, no reducible configuration can appear as a bubble or as a neck connection.
- *Neck chains and cap excess* enter $\ell_j$ or the penalties of Lemma 3.

So "the abelian part bubbles" is always an increase of $\ell_j$, and rows 5–9 cover it.

**Does dimension counting exclude the reducible strata without regularity of those strata?**
- **Unbroken Seiberg–Witten strata (row 5).** Yes. In fact no dimension count is used: the incidence-compatible candidate set is empty for lattice reasons. This depends only on the a priori conditions 2–3 of Proposition 8, not on any transversality.
- **Unbroken reducible zero-section configurations (row 6).** Yes, by the period of the cap.
- **Broken tuples without an $\mathcal M^{*,0}$-component (row 7).** Yes. The identity $\sum(q_j+4)=4$ is topological. The reducible components enter only through lower bounds on their virtual indices, forced by incidence and the lattice. Regularity is needed only at anti-self-dual components, plus tangential regularity at short Seiberg–Witten end components.
- **Broken tuples with Seiberg–Witten but no reducible zero-section components (row 8).** No, in the following precise sense. The count uses the full index $i_j$ at Seiberg–Witten components, so their full regularity is required.
  - This is achieved by several-piece multivalued perturbations that break their circle symmetry. In the coupled problem they are no longer circle-fixed.
  - This regularity is not available in FL: FL2a §3.4, and FL1 §5 introduction, where Theorem 1.3 "does not apply to PU(2) monopoles which are zero-sections or which are reducible".
  - It is not in conflict with FL either, because FL's statement concerns the single-piece problem.
  - An alternative that avoids it would bound a Seiberg–Witten component by its tangential dimension $d_s+p_j+4\ell_j$. I have not checked whether the budget survives that weaker bound.
- **Broken tuples with reducible zero-section components (row 9).** Yes. These components are discarded and contribute at most their parameter count. They need neither regularity nor even a description of their moduli spaces. Their only role is to *consume charge*: incidence forces $\kappa_\Gamma$ to be large, which leaves the other components too little index.

**FL's local-finiteness caveat.** FL warn that the topology near lower levels "need not be locally finite", so links may lack fundamental classes (FL2b §3 introduction; FL2a after Corollary 3.6). This caveat plays no role here: the closure of the one-manifold meets lower strata only at points with explicit local models, namely the instanton Kuranishi charts and the lens collars with exhaustion. The price is that the exclusion must be exhaustive. One stratum left unexcluded would produce ends that the argument has no means to evaluate.

---

## 5. Where the analogue goes beyond FL

Each item below states what is needed, which FL result it extends, and how I classify it.

**5.1 Families of metrics over a cube, and compactness at faces and corners (Theorem 1).**
- *FL.* FL1 Theorem 1.1, Theorem 4.20 and Definition 4.19; Memoir Theorem 2.1.3 and Definition 2.1.2. All are for a closed manifold with a fixed metric.
  - FL use parametrized moduli spaces only over perturbation parameters, for transversality (FL1 §5; FL2a §2.2).
  - They use a path of metrics only for anti-self-dual connections, in Memoir Chapter 11, conditionally on Hypothesis 11.3.5.
  - FL3 §9.3 deliberately avoids long necks.
- *Classification.*
  - Over $\operatorname{int}Q$ the extension is **routine**. The constants of FL1 (4.19), (4.6) and Lemma 4.4 depend on the negative part of the scalar curvature, on $p_1$ and on the fixed connections, and these are uniform because the necks have positive scalar curvature.
  - At faces and corners it is **plausible but substantial**. One needs the neck analysis, quantization of the loss, exponential convergence and Hausdorffness of the space of tuples, all uniformly under simultaneous approach to several faces. This is Lemmas `analysis:compactness`, `analysis:neck` and `analysis:finite-data`; the anti-self-dual analogue is classical (Donaldson's book on Floer homology†). T1 rates it 85%.

**5.2 Positive-scalar-curvature necks along $S^3$ and $L(4,1)$ with flat reducibles, and index bookkeeping (Theorem 1, item 3; Lemma 3).**
- *FL.* None. FL exclude flat connections altogether (FL2a Lemma 3.2 and Corollary 3.3; FL2b Definition 3.20; FL3 §2.1, which requires that no SO(3) bundle with $w_2\equiv w$ admit a flat connection). Here flats on the necks are unavoidable. Weighted Fredholm theory with stabilizers $SO(3)$ and $U(1)$ at the ends, and the unframed convention, have no FL counterpart.
- *Classification.*
  - The identities of Lemma 3 are **routine**: Atiyah–Patodi–Singer† and Lockhart–McOwen†, with careful matching of stabilizers.
  - The lens table of Proposition `indices:lens-index` is a **routine** computation that I have not rechecked.
  - The analytic neck theory (spinor decay, a spectral gap uniform in the neck length, exponential estimates) is **plausible but substantial**. It is new for SO(3) monopoles, although positive scalar curvature removes the spinor and leaves essentially the anti-self-dual problem.

**5.3 Transversality in families.**
- *Needed.*
  - (a) Anti-self-dual components with cuts, on pieces, in families.
  - (b) The $\mathcal M^{*,0}$ stratum and its lower levels.
  - (c) Tangential regularity of Seiberg–Witten components.
  - (d) Surjectivity of the Dirac operator at the counted instantons.
  - (e) Regularity of the coupled problem at candidates containing an $\mathcal M^{*,0}$-component, including full regularity at Seiberg–Witten components (row 8) and at the projected problems (row 9), with the phase cuts transverse there.
- *FL.*
  - Memoir Theorem 2.1.1 (FL2a Theorem 2.13, quoting Feehan's generic-metric theorem), for a closed manifold and one spin$^u$ structure.
  - FL1 Theorem 1.3 (holonomy perturbations). Levels $\ell>0$ are treated there only in outline, in §5.1.3, and the theorem excludes zero-section and reducible points.
  - FL2a Proposition 2.16 (tangential smoothness of $M_{\mathfrak s}$).
  - FL1's holonomy perturbations are supported in balls and vanish at reducible configurations (FL1 §1.1.1).
- *Classification.*
  - (a)–(d) are **routine**.
  - (e) is **plausible but substantial and new**. It needs perturbations that sample several pieces with independent frames and a common circle, multivalued at points of finite isotropy. It also needs phase cuts built from samples of the $\mathcal M^{*,0}$-component. These replace FL's $\bar{\mathcal W}$, which is pulled back from a neighbourhood of a point (FL2b Lemma 3.13), and FL's intersection-suitability device (FL2b Lemma 3.17, Remark 3.19).

**5.4 Representatives of $\mu_p(S_i)$ at reducible limits (§1.6(a)).**
- *FL.*
  - FL2b Lemma 3.12, Definition 3.14, Lemma 3.15, Lemma 3.17 and Corollary 3.18. FL call the description of the closures "incomplete, as it does not give the multiplicities".
  - FL never need representatives at reducible limits, because reducible ends are handled by links. The cohomological counterparts are on the links:
    - FL2b Corollary 4.7, which gives $\boldsymbol\gamma^*\mu_p(h)=\tfrac12\langle c_1(\mathfrak s)-c_1(\mathfrak t),h\rangle(2\mu_{\mathfrak s}(x)+\nu)$ when $b_1=0$; this vanishes when $\langle v,h\rangle=0$;
    - L1 Lemma 4.10, which adds $\pi_X^*\mathrm{PD}[h]$ from the bubble point.
- *Classification.*
  - With the determinant-line divisor this is **routine**.
    - Property 2 is Grothendieck's theorem on $\mathbb P^1$: a degree-zero line bundle is trivial, so $\mathcal O\oplus\mathcal O$ does not jump.
    - Property 3 holds because Uhlenbeck convergence is $C^0$ on $S_i$ away from the points, and non-invertibility of $\bar\partial$ is closed in $C^0$ (T2 Corollary 3.3).
    - Properties 4–5 (multiplicativity of the determinant line under nodal degeneration, T2 §0) are plausible.
  - With the manuscript's holonomy representative it is **plausible but substantial**: the zero-winding modification, segmentation and persistence are flagged as weak points in T1 §0 and in the exposition.
  - Changing representatives requires the cobordism comparison of T2 Corollary 2.4, which avoids a neighbourhood of the flat connection on $S_i$ (rated plausible).

**5.5 The instanton link and the factor $2^{n_a-1}$ (Theorem 4).**
- *FL.* FL2b Proposition 3.29 with Lemmas 3.22 and 3.24–3.28; FL2a Corollary 3.6, Definition 3.7, Lemma 3.8 and Remark 3.9; Memoir (2.6.2), which cites it as "[FL2b, Lemma 3.30]".
- *Differences.* There are parameters. The Dirac cokernel is removed by perturbation, so FL's obstruction class $h^c$ becomes $1$. The global link $\{\|\Phi\|^2=\varepsilon\}$ is not needed, only its intersection with a neighbourhood of $\iota(\mathcal I_e)$. Hypothesis 3 of Theorem 4 comes from §4.
- *Classification.* **Routine.**
- The factor $2^{n_a-1}$ (from $\mu_c\mapsto2h$, FL2b Lemma 3.28) is why integral coefficients are needed. Over $\mathbb F_2$ the identity is empty once $n_a\ge2$, so nonvanishing of $D^{w_0}_{X,Q}$ must be shown over $\mathbb Z$ (modulo $2^N$).

**5.6 The weighted sum over $e$, and lens ends (Proposition 7).**
- *FL.* Nothing on lens faces. The related items are:
  - Memoir (2.5.3), which compares $D^{w'}$ and $D^w$ only for $w'\equiv w\pmod2$, whereas here the $w_2$ differ (§1.4);
  - the orientation comparisons of FL2b Definition 2.3 and Lemma 2.6, and Memoir Lemma 8.1.7;
  - on the gluing side, FL3 Theorem 1.1 (bubbles on $S^4$, existence only) and F19 Theorem 3 (anti-self-dual connections, one bubble);
  - Memoir Hypothesis 11.3.5 (reducible anti-self-dual connections in a path of metrics, assumed).

  The weighted sum over $w$ in the Kronheimer–Mrowka structure theorem (FL6 Theorem 2.2) plays no role here.
- *Classification.* **Plausible but substantial.**
  - It is an unobstructed gluing at a reducible whose stabilizer $H=U(1)$ equals that of the boundary flat, so the gluing parameter $H/H$ is a point. The obstruction is the scalar cokernel $\int_N\langle\tau,\cdot\rangle$, which is removed by changing the weight (Lemma `gluing:blocks`).
  - Exhaustion follows from exponential convergence on the neck (Proposition `gluing:collar`).
  - The orientation comparison is in Proposition `gluing:signs`. T1 rates it 70%.
- This is the only gluing at a reducible that the argument uses.

**5.7 Seiberg–Witten strata at every level.**
- *FL.*
  - FL2b Theorem 3.33(a): no reducibles at any level implies vanishing. It is proved.
  - Memoir Theorem 8.1.9, Definition 8.1.3 and Theorems 10.1.1–10.1.2: contributions of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$, conditional on Hypothesis 7.8.1 for $\ell\ge1$.
  - FL2b Theorem 4.13 (level $0$) and L1 Theorem 6.1 (level $1$, conditional on L1 Theorem 3.8).
- *What is new.*
  - (a) The cut-down refinement: strata that are non-empty but miss the closure of the representatives are allowed. Given 5.4 this is **routine**.
  - (b) The Seiberg–Witten localization (condition 3 of Proposition 8) is outside FL's scope, since FL take Seiberg–Witten invariants as given. Here *emptiness* is needed, not counts (T3 §1.4). Band classes do exist (T3 §1.3), so they must be excluded by energy, and the chamber condition must hold uniformly up to the faces. This is **plausible but substantial**; T3 and the exposition list the uniformity at faces as a risk.
  - (c) The broken cases are rows 7–8 of §4.
- *FL's gluing hypotheses are not needed.* No counterpart of Hypothesis 7.8.1, of FL6 Hypothesis 3.1 or of Overlap Theorem 4.2 is needed. The overlap problem (Overlap §§1 and 4; Memoir Chapter 6) arises only when several strata $\Sigma\subset\mathrm{Sym}^\ell$ must be glued at once. Here the only glued ends have no points.

**5.8 Reducible zero-section components (Proposition 2, item 2).**
- *FL.* They are excluded (FL2a Proposition 3.1, Lemma 3.2 and Corollary 3.3; FL3 §2.1). They are treated only in Memoir Chapter 11, under Hypothesis 11.3.5.
- *Here.* They cannot be avoided on inner segments at $S^3$-faces, because $\dim Q=n$ while $b^+(X)=m+b_0\approx n/4$, with $b_0$ coming from the caps (D-families §0). Negative segments have $b^+=0$, so every admissible class is a wall for every parameter value.
- *Classification.*
  - Exclusion when $k=0$, by the caps: **routine to plausible**. It needs isolation necks uniformly long over $\bar Q$.
  - Exclusion in broken limits without an $\mathcal M^{*,0}$-component, by Lemma 3 and Lemma 9: **routine**.
  - Exclusion in broken limits with an $\mathcal M^{*,0}$-component: see 5.9.

**5.9 Mixed limits: the projection, compared with gluing at reducibles.**
- *FL's route, adapted.* One would need:
  - a Kuranishi model at the reducible zero-section component, with $U(1)$ stabilizer and obstructions of nonzero weight (the normal anti-self-dual cokernel on $\Omega^1(L)$ and the Dirac cokernel);
  - gluing to the irreducible pieces across $S^3$-necks, with gluing parameter in $SO(3)/U(1)$;
  - all of this in a family with faces.

  This combines the zero-section analogue of Memoir Hypothesis 7.8.1, Memoir Hypothesis 11.3.5 and neck gluing. None of it is available. T1 Remark 2.4 (rated 30%) sketches what such a model would give: no local spacing condition at all. It also notes that the needed transversality comes only from a leading interaction term, whose genericity in families with faces is unproved.
- *The projection.* Delete the reducible zero-section components, keeping their parameters, and work in the coupled problem, which has finite isotropy. Compute the projected index from Lemma 3 as $5-4N-\sum(4+i_j-p_j)$, and bound each run below by Lemma 9 (incidence forces charge onto the reducible segments).
  - Ingredients: independence of the retained equations from the deleted data (Lemma `analysis:R-independence`); compactness of the candidate projections in a finite ordering of degenerations (Lemma `analysis:finite-data`); finitely many multivalued terms, with openness of the earlier exclusions (Proposition `analysis:finite-induction`).
  - The zero set of the loosened problem need not be compact, and nothing is claimed about it. Regularity is needed only near the compact set of projections of candidates. This is correct.
  - The projection only excludes; it never evaluates. Its cost is the local spacing $\ge4$. At spacing $3$ the bound is attained (T1 §3.4), so the spacing is not slack.
- *Classification.* **Plausible but substantial; this is the decisive new analytic step.** T1 rates it 55–60%. It does not replace Memoir Hypothesis 7.8.1, which concerns Seiberg–Witten strata and is made unnecessary by 5.7. It replaces a gluing theorem at reducible zero-section components in families with faces, which is **genuinely open** and which the argument does not need.

**5.10 Rational weights, multisections and Stokes.**
- *FL.* Integral counts, single-valued perturbations, smoothly stratified spaces (FL2b Definition 3.2).
- *Classification.* **Routine** (weighted branched one-manifolds; Lemma `analysis:stokes`).
- The conclusion over $\mathbb Q$ suffices because $D^{w_0}_{X,Q}\in\mathbb Z$ is computed from single-valued data. The several-piece terms vanish on the zero-section locus and near the instanton collars, where the branch weights add up to one.

**5.11 Orientations.**
- *FL.* FL2b Definition 2.3 and Lemmas 2.6, 2.9, 3.24 and 3.25; Memoir Lemma 8.1.7.
- *Classification.* **Routine** (orientation of $Q$, common $\sigma_0$), except for the comparison of lens pairs (5.6).

**5.12 Not needed, and open.**
1. A family formula with Seiberg–Witten terms, that is, Memoir Theorem 1 over a cube with faces: **genuinely open**.
2. Exclusion of mixed limits at spacing $3$: **open**. Possible routes are counting the codimension of walls in the retained parameters (T1 §3.7; D §4.5; rated 40%) or obstructed gluing (T1 Remark 2.4).
3. An $S^1$-equivariant SO(3)-monopole Floer theory (exposition, Assessment): **open**.

**Summary of classifications**

| Item | Routine | Plausible but substantial | Open |
|---|---|---|---|
| Compactness over $\operatorname{int}Q$ (5.1) | ✓ | | |
| Compactness at faces and corners; neck analysis (5.1, 5.2) | | ✓ | |
| Index identities, lens table (5.2) | ✓ (table to be rechecked) | | |
| Transversality (a)–(d) (5.3) | ✓ | | |
| Coupled multivalued regularity, phase cuts (5.3(e), row 8) | | ✓ | |
| Representatives: determinant-line divisor / holonomy version (5.4) | ✓ / | / ✓ | |
| Instanton link, $2^{n_a-1}$ (5.5) | ✓ | | |
| Lens gluing, exhaustion and orientation (5.6) | | ✓ | |
| Unbroken Seiberg–Witten exclusion, given localization (5.7(a)) | ✓ | | |
| Seiberg–Witten localization uniformly up to faces (5.7(b)) | | ✓ | |
| Reducible zero-section components: $k=0$ and fixed broken (5.8) | ✓ | | |
| Projection for mixed limits (5.9) | | ✓ | |
| Multisections, Stokes, orientations (5.10, 5.11) | ✓ | | |
| Family Seiberg–Witten formula; spacing 3; Floer version (5.12) | | | ✓ (not needed) |

---

## 6. Remarks on the exposition's Theorem `thm:FL`

1. **The ends at abelian limits.** Item 3 and the conclusion "$2^{n_D-1}\Omega=-\#\{\text{abelian ends}\}$" treat abelian ends as isolated boundary points with weights. Without gluing at reducibles this is not defined (§3.7). What the inputs give is Theorem 6: if there are no abelian ends, then $2^{n_D-1}\Omega=0$. This is all that §§7–8 of the exposition use.
2. **The inputs called standard.** "Feehan–Leness compactness, transversality and instanton links" are proved by FL for a closed manifold with a fixed metric. The instanton link extends routinely. Compactness and transversality at the neck faces are not in FL (5.1–5.3).
3. **What the projection replaces.** "Replaces Feehan–Leness's obstructed gluing at reducibles" should be made precise. The projection replaces gluing at *reducible zero-section* components in families, which FL do not treat for SO(3) monopoles. FL's gluing at *Seiberg–Witten* strata (Hypothesis 7.8.1) is not replaced; it becomes unnecessary because of the a priori exclusion in 5.7.
4. **Compactness of the one-manifold.** "Compact oriented 1-manifold" holds after truncation at the instanton and lens collars, with rational weights.
5. **The remaining claims are consistent with this note.** These are: "ends at the $S^3$-faces without an abelian piece vanish for dimensional reasons" (row 2), the lens cancellation (Proposition 7) and "rational multisection weights" (5.10).

---

## 7. Uncertainties

1. FL theorem and equation numbers are those inferred from the arXiv LaTeX sources in the extraction notes. Published numbering may differ; for example, the Memoir cites FL2b Proposition 3.29 as "Lemma 3.30".
2. That $\mathrm{PD}[S_i]\not\equiv0\pmod 2$ in $X$ (§1.4) is my deduction from the lattice of Proposition `stack:lattice` ($F_r\cdot a=-1$ on a negative piece). The manuscript does not state it in this form. It changes nothing in the argument but corrects the impression that the $\mathfrak t_e$ have a common $w_2$.
3. I have not re-verified the manuscript's proofs of compactness at faces, coupled regularity, projection, lens gluing or Seiberg–Witten localization. The classifications are judgments based on the statements, the proofs as read, and the T-notes' assessments.
4. I have not rechecked the lens index table, the cap charge congruences, or the claim that the minimal trace cap's normal operator can be made surjective by perturbations vanishing at the reducible.
5. Whether the determinant-line divisor satisfies properties 4–5 of §1.6(a) with the manuscript's face structure is plausible but unchecked. Replacing the holonomy representative also requires recomputing, or comparing, the Floer-theoretic maps $B$ that are built with it.
6. Row 8 uses full regularity of Seiberg–Witten components in the coupled problem. I have not checked whether the numerical budget would survive bounding them only by their tangential dimension, which would make that step independent of 5.3(e).
7. Citations marked † are from memory: Donaldson's book on Floer homology, Morgan–Mrowka–Ruberman, Donaldson–Kronheimer, Atiyah–Patodi–Singer, Lockhart–McOwen, McDuff, Cieliebak–Mundet–Salamon.
