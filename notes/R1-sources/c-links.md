# (c) Links of the instanton and Seiberg–Witten strata in $\bar{\mathcal M}_{\mathfrak t}/S^1$

This note is extracted from the arXiv LaTeX sources of Feehan–Leness (FL). Statements are copied with light cleaning of the LaTeX. Every hypothesis printed in the source is listed. Comments of mine are marked **[gloss]**. Apparent misprints are recorded as printed and listed again at the end.

The source table, the numbering conventions and the general notation are the same as in the companion note `a-cobordism.md`, §§0–1. In brief:

| Short name | arXiv | File | Numbering |
|---|---|---|---|
| Ann. | dg-ga/9709022 (announcement) | `main.tex` | *section.n*, one shared counter |
| FL1 | dg-ga/9710032 (PU(2) monopoles I) | `main.tex` | same |
| FL2a | math/0007190 (PU(2) monopoles and links of top-level SW moduli spaces) | `main.tex` | same |
| FL2b | dg-ga/9712005 (PU(2) monopoles II) | `main.tex` | same |
| FL3 | math/9907107 (PU(2) monopoles III) | `main.tex` | same |
| L1 | math/0106238 (SO(3) monopoles, level-one SW moduli spaces) | `main.tex` | same |
| Memoir | math/0203047 v4 (*Mem. AMS* 256, no. 1226) | `FeehanLenessMonopoleCobordism_v4-clean.tex` | *chapter.section.n*; equations likewise |
| FL6 | math/0609530 | `jems-feehanleness_PF11-22-2014.tex` | *section.n* |
| Overlap | 1211.0480 | `main.tex` | *section.n*; Proposition has its own counter |
| F19 | 1910.14580 (Feehan, gluing via maps of Banach manifolds with corners) | `kuranishi_model_boundary_moduli_space.tex` | main results on a separate counter `mainthm` (Theorem 1, 2, 3, Corollary 4, …) |

I inferred all theorem numbers from the `\newtheorem`/`\numberwithin` declarations. A script counted equation numbers. The equation counts reproduce every cross-citation I could test: FL2a (2.32), (2.47), (3.35), (3.71), (3.72), as cited by FL2b and the Memoir, and FL2b (3.60) and (4.27), as cited by L1. Labels are given verbatim. The Kronheimer–Mrowka structure theorem plays no role in the material on links and is not restated here; see `a-cobordism.md` §8.

[checker] An independent counter recomputed the theorem numbers. It tracks sections, chapters, appendices, shared counters and unnumbered environments, and ignores comments. It reproduces every theorem, lemma, proposition, corollary, definition, remark, conjecture and hypothesis number cited in this note for FL2a, FL2b, L1, FL3, the Memoir, FL6, the Overlap paper, the Announcement and F19. It also reproduces every equation number cited for FL2a, FL2b, L1 and the Memoir. Each quoted statement was compared with the source. Corrections and additions are marked "[corrected by checker]" or "[added by checker]". Statements about LenessWC and the Kronheimer–Mrowka structure paper remain unverifiable here, since neither source is available.

---

## 0. Setting and the two kinds of fixed point

**Notation (FL2a §2, Memoir §2.1).** $X$ is closed, connected, oriented and smooth with $b^+(X)>0$. A spin$^u$ structure is $\mathfrak t=(\rho,V)$ with $V=W\otimes E$. Its adjoint bundle is $\mathfrak g_{\mathfrak t}=\mathfrak{su}(E)$, and $\kappa=-\frac14p_1(\mathfrak t)$, $w\equiv w_2(\mathfrak t)\pmod 2$. The moduli space of solutions $[A,\Phi]$ of the perturbed SO(3)-monopole equations (FL2a eq. `eq:PT` (2.32); Memoir eq. `eq:PerturbedSO3MonopoleEquations` (2.1.10)) is $\mathcal M_{\mathfrak t}$. Its Uhlenbeck closure is $\bar{\mathcal M}_{\mathfrak t}\subset\bigsqcup_\ell\mathcal M_{\mathfrak t(\ell)}\times\mathrm{Sym}^\ell(X)$, where $p_1(\mathfrak t(\ell))=p_1(\mathfrak t)+4\ell$. FL2a writes $\mathfrak t_\ell$ for $\mathfrak t(\ell)$.

$D_{A,\vartheta}=D_A+\rho(\vartheta):C^\infty(V^+)\to C^\infty(V^-)$ is the perturbed coupled Dirac operator. FL2a Theorem 2.13 (`thm:Transversality`) gives, for generic parameters,
$$\dim\mathcal M^{*,0}_{\mathfrak t}=d_a+2n_a,\qquad d_a(\mathfrak t)=-2p_1(\mathfrak t)-\tfrac32(\chi+\sigma),\qquad n_a(\mathfrak t)=\tfrac14\big(p_1(\mathfrak t)+c_1(\mathfrak t)^2-\sigma\big)$$
(eq. `eq:Defndana` (2.51)). There "$n_a(\mathfrak t)$ is the complex index of the Dirac operator on $C^\infty(V^+)$".

**Two circle actions (FL2a §3.1).** The first is scalar multiplication on $V$, $(e^{i\theta},\Phi)\mapsto e^{i\theta}\Phi$ (`eq:ScalarMultAction` (3.1)). The second is defined when $V=W\oplus W\otimes L$: it acts by $\Psi\oplus\Psi'\mapsto\Psi\oplus e^{i\theta}\Psi'$ (`eq:VReducibleAction` (3.2)). The two are related by
$$\mathrm{diag}(1,e^{2i\theta})=e^{i\theta}u,\qquad u=\mathrm{diag}(e^{-i\theta},e^{i\theta})\in\mathcal G_{\mathfrak t},$$
so on $\mathcal C_{\mathfrak t}$ they differ only by multiplicity. **[gloss]** This weight-two relation produces the factor $2$ in the instanton link (§3 below). It is also why the same class $\mu_c$ restricts to $\nu$ rather than $2\nu$ on the SW link (§6).

**FL2a Proposition 3.1** (`prop:ClassificationOfStabilizers`).
> Let $\mathfrak t=(\rho,V)$ be a spin$^u$ structure over a closed, oriented, smooth four-manifold $X$, with $b_2^+(X)\ge1$ and generic Riemannian metric. If $\hat A$ is a non-flat connection on $\mathfrak g_{\mathfrak t}$, then $[A,\Phi]\in\mathcal M_{\mathfrak t}$ is a fixed point with respect to the $S^1$ action on $\mathcal M_{\mathfrak t}$ if and only if one of the following hold:
> 1. The connection $\hat A$ is anti-self-dual, irreducible, and $\Phi\equiv0$. The pair $(A,\Phi)$ is a fixed point with respect to the circle action (3.1).
> 2. The pair $(A,\Phi)$ is reducible with respect to a splitting $V=W\oplus W\otimes L$ but $\Phi\not\equiv0$, $(A,\Phi)=(B\oplus B\otimes A_L,\Psi\oplus0)$. The pair $(A,\Phi)$ is a fixed point with respect to the circle action (3.2). The connection $\hat A$ on $\mathfrak g_{\mathfrak t}$ is reducible with respect to the splitting $\mathfrak g_{\mathfrak t}\cong i\underline{\mathbb R}\oplus L$, with $\hat A=d_{\mathbb R}\oplus A_L$.

Flat connections are excluded by choosing $w$ suitably. FL2a Lemma 3.2 (`lem:MorganMrowka`) gives the Morgan–Mrowka criterion. FL2b Definition 3.20 (`defn:Good`) defines: *$v\in H^2(X;\mathbb Z/2)$ is good if no integral lift of $v$ is torsion.* When $w\pmod2$ is good, the Memoir records the disjoint decomposition $\bar{\mathcal M}_{\mathfrak t}\cong\bar{\mathcal M}^{*,0}_{\mathfrak t}\sqcup\bar M^w_\kappa\sqcup\bar{\mathcal M}^{\rm red}_{\mathfrak t}$ (eq. `eq:StratificationCptPU(2)Space` (2.2.2)). A reducible stratum $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ lies in level
$$\ell(\mathfrak t,\mathfrak s)=\tfrac14\big((c_1(\mathfrak t)-c_1(\mathfrak s))^2-p_1(\mathfrak t)\big)$$
(Memoir eq. `eq:ReducibleLevel` (2.3.14)). FL2a Corollary 3.3 (`cor:NoSWZeroSections`): *if $w_2(\mathfrak t)$ obeys the Morgan–Mrowka criterion, then $M_{\mathfrak s}$ contains no zero-section solutions.*

---

# Part I. The anti-self-dual (zero-section) stratum

## 1. Local structure at a zero-section monopole

### 1.1 FL2a, Lemma 3.4 (`lem:DecompOfZeroSectionDeformation`)

> If $(A,0)$ is a zero-section PU(2) monopole then there are canonical isomorphisms
> $$H^0_{A,0}\cong H^0_{\hat A},\qquad H^1_{A,0}\cong H^1_{\hat A}\oplus\operatorname{Ker}(D_A+\rho(\vartheta)),\qquad H^2_{A,0}\cong H^2_{\hat A}\oplus\operatorname{Coker}(D_A+\rho(\vartheta)).$$

**Hypotheses.** None beyond $(A,0)$ being a zero-section solution. The proof is the splitting of the deformation complex at $(A,0)$ into the ASD complex of $\hat A$ and the Dirac operator (eq. `eq:ASDDeformationComplex` (3.6)).

### 1.2 FL2a, Corollary 3.6 (`cor:ASDKuranishi`)

> Let $\mathfrak t$ be a spin$^u$ structure on a closed, oriented, smooth four-manifold $X$ with $b_2^+(X)>0$ and generic Riemannian metric. Let $[A,0]$ be a point in the image of $M^w_\kappa\hookrightarrow\mathcal M_{\mathfrak t}$, so $H^0_{\hat A}=0=H^2_{\hat A}$ for $[\hat A]\in M^w_\kappa$. Then there are
> * An open, $S^1$-invariant neighborhood $\mathcal O_A$ of the origin in $T_{\hat A}M^w_\kappa\oplus\operatorname{Ker}(D_A+\rho(\vartheta))$ together with a smooth, $S^1$-equivariant embedding $\boldsymbol\gamma_A:\mathcal O_A\hookrightarrow\tilde{\mathcal C}_{\mathfrak t}$, with $\boldsymbol\gamma_A(0,0)=(A,0)$ and $\mathcal M_{\mathfrak t}\cap\boldsymbol\gamma_A(\mathcal O_A)$ an open neighborhood of $[A,0]$ in $\mathcal M_{\mathfrak t}$, and
> * A smooth, $S^1$-equivariant map $\boldsymbol\varphi_A:\mathcal O_A\to\operatorname{Coker}(D_A+\rho(\vartheta))$ such that $\boldsymbol\gamma_A$ restricts to an $S^1$-equivariant, smoothly-stratified diffeomorphism from $\boldsymbol\varphi_A^{-1}(0)\cap\mathcal O_A$ onto $\mathcal M_{\mathfrak t}\cap\boldsymbol\gamma_A(\mathcal O_A)$.

**Hypotheses.** $X$ closed, oriented, smooth, $b_2^+>0$, generic metric. The corollary records $H^0_{\hat A}=0=H^2_{\hat A}$ as a consequence of these ("so …"). FL2a Lemma 3.5 (`lem:TwistedReducibles`, quoting KM) handles twisted reducibles.

**Text following the corollary (FL2a, after Cor. 3.6), verbatim in substance.**
* "If $n_a\le0$, then at a generic point $[A,0]\in\mathcal M_{\mathfrak t}$ where $\operatorname{Ker}(D_A+\rho(\vartheta))=\{0\}$, (*assuming the map from $M^w_\kappa$ to the space of Fredholm operators of index $n_a$ is transverse to the 'jumping lines strata'* as described in [Koschorke]) the Kuranishi model … shows that a neighborhood of $[A,0]$ … contains no elements of $\mathcal M^0_{\mathfrak t}$ … For this reason, we will restrict our attention to the cases where $n_a>0$."
* "Although we can only describe a neighborhood of the anti-self-dual connections *locally*, because of the problem of spectral flow, we can still introduce a global, codimension-one subspace of the compactification $\bar{\mathcal M}_{\mathfrak t}$ which will serve as a link. *This space might not have a fundamental class because it is not known to have locally finite topology near the lower strata* of the Uhlenbeck compactification $\bar{\mathcal M}_{\mathfrak t}$. However, … the local Kuranishi model in Corollary 3.6 will suffice to define intersections under some additional assumptions."

**Role.** This is the only description FL give of a neighbourhood of $M^w_\kappa$. The fibre of the "normal cone" at $[A,0]$ is $\operatorname{Ker}D_{A,\vartheta}$, of complex dimension $n_a+c$ with $c=\dim_{\mathbb C}\operatorname{Coker}D_{A,\vartheta}$. The obstruction space is $\operatorname{Coker}D_{A,\vartheta}$. Both dimensions jump along $M^w_\kappa$.

## 2. Definition of the instanton link and its basic properties

### 2.1 FL2a, Definition 3.7 (`defn:ASDLink`)

> The *link of $\bar M^w_\kappa$* in $\bar{\mathcal M}_{\mathfrak t}$ is given by
> $$\mathbf L^{w,\varepsilon}_{\mathfrak t,\kappa}=\{[A,\Phi,\mathbf x]\in\bar{\mathcal M}_{\mathfrak t}/S^1:\ \|\Phi\|^2_{L^2}=\varepsilon\}.$$
> We write $\mathbf L^w_{\mathfrak t,\kappa}$ when the positive constant $\varepsilon$ is understood.

The Memoir repeats this verbatim as eq. `eq:DefineASDLink` (2.2.3) with notation $\bar{\mathbf L}^w_{\mathfrak t,\kappa}$, "when $w\pmod2$ is good". It adds: "for generic $\varepsilon$, the link $\bar{\mathbf L}^w_{\mathfrak t,\kappa}$ is a smoothly-stratified, codimension-one subspace of $\bar{\mathcal M}_{\mathfrak t}/S^1$." FL2b writes it as $\mathbf L^{w,\varepsilon}_{\mathfrak t,\kappa}=\boldsymbol\ell^{-1}(\varepsilon)\cap\bar{\mathcal M}_{\mathfrak t}/S^1$ with $\boldsymbol\ell([A,\Phi])=\|\Phi\|^2_{L^2}$ (eqs. `eq:DefineNormFunction` (3.42), `eq:ASDLink` (3.43)). The Overlap paper writes $\bar{\mathbf L}^{\rm asd}_{\mathfrak t}$. The announcement (Ann., Definition 3.16) uses the level $\|\Phi\|^2_{L^2}=\varepsilon^2$.

### 2.2 FL2a, Lemma 3.8 (`lem:ContinuousL2Norm`)

> For generic $\varepsilon>0$, the link $\mathbf L^{w,\varepsilon}_{\mathfrak t,\kappa}$ is closed under the $S^1$ action, is a smoothly stratified, closed subspace of $\bar{\mathcal M}_{\mathfrak t}$, and has codimension one in every stratum of $\bar{\mathcal M}_{\mathfrak t}$ which it intersects.

**Hypotheses.** Generic $\varepsilon$. The proof shows that $\boldsymbol\ell$ is continuous on $\bar{\mathcal M}_{\mathfrak t}$, using the universal a priori $C^0$ bound on $\Phi$ of FL1 Lemma 4.4 (`lem:C0EstFAPhi`), and that it is smooth on strata. **[gloss]** The lemma calls the link a subspace of $\bar{\mathcal M}_{\mathfrak t}$, while Definition 3.7 places it in $\bar{\mathcal M}_{\mathfrak t}/S^1$. I read the lemma as applying to the $S^1$-invariant level set upstairs and its quotient.

### 2.3 FL2a, Remark 3.9 (unlabelled): why there is no global projective-bundle model

> In defining a link, it might seem more natural to work with the image of the $\varepsilon$-sphere in the normal bundle given by $\operatorname{Ker}(D_A+\rho(\vartheta))$, at least on the image of $M^w_\kappa\hookrightarrow\mathcal M_{\mathfrak t}$ where the cokernel of the Dirac operator vanishes. This definition would have the disadvantage of not being a global object because of the jumping-line problem (that is, spectral flow). However, it can be shown that the two functions defined on the open set $\mathcal O$ of the Kuranishi model of $[A,0]$ in Corollary 3.6, one given by the $L^2$ norm of the element of $\operatorname{Ker}(D_A+\rho(\vartheta))$, the other defined by $\boldsymbol\ell\circ\boldsymbol\gamma$, are $C^1$ close as $\varepsilon$ goes to zero … As we shall see in §3.4.2 in [FL2b] it is sufficient that these two links are cobordant.

**[gloss] What FL do and do not claim about a projective bundle.** FL never identify $\mathbf L^w_{\mathfrak t,\kappa}$ globally with $\mathbb P(\operatorname{Ker}\mathbf D)\to M^w_\kappa$ or with any projective bundle over $\bar M^w_\kappa$, and Remark 3.9 explains why: $\operatorname{Ker}D_{A,\vartheta}$ need not have constant rank. Two weaker statements appear in the sources:
* **Ann.**, text after Lemma 3.13 (`lem:ASDKuranishi`): "Lemma 3.13 then describes the normal cone to $M^{\rm asd}_E$ at a generic point $[A,0]$ as a cone on $\mathbb{CP}^{n_a-1}$, where $\operatorname{Ker}D_{A,\vec\vartheta}\simeq\mathbb C^{n_a}$." Lemma 3.13 also asserts: "If $\operatorname{Ind}D_{A,\vec\vartheta}>0$ then for generic points $[A]\in M^{\rm asd}_E$, the cokernel of the Dirac operator vanishes for generic perturbations $\vec\vartheta$." The justification offered is transversality of $A\mapsto D_{A,\vec\vartheta}$ to the jumping-line strata. In FL2a this becomes an explicit *assumption* ("assuming … transverse to the 'jumping lines strata'", §1.2 above).
* **FL2b**, §3.4.3 (next section): a local model near each of the finitely many points of $\bar{\mathcal V}(z)\cap M^w_\kappa$. It allows $\operatorname{Coker}D_{A,\vartheta}\neq0$ and needs no jumping-line transversality.

### 2.4 FL2b, Lemma 3.21 (`lem:ASDClosureEquality`)

FL2b first sets $\bar M^{\rm asd}_{\mathfrak t}=\{[A,\Phi,\mathbf x]\in\bar{\mathcal M}_{\mathfrak t}:\Phi=0\}$ (eq. `eq:ZeroSectionCompactification` (3.28)).

> Let $\mathfrak t$ be a spin$^u$ structure on a closed, oriented four-manifold $X$ with generic metric, $b_2^+(X)>0$ and $w_2(\mathfrak t)\equiv w\pmod2$, for $w\in H^2(X;\mathbb Z)$. If $w\pmod2$ is good, then
> $$\bar M^{\rm asd}_{\mathfrak t}=\iota(\bar M^w_\kappa).\tag{3.29}$$

**Hypotheses.** Closed oriented $X$, generic metric, $b_2^+>0$, $w\pmod2$ good. The preceding argument invokes "Taubes' gluing theorem for anti-self-dual SO(3) connections" when "there [are] no obstructions to gluing (for example, when the metric on $X$ is generic in the sense of [DK, FU])".

**Role.** This identifies the zero-section part of $\bar{\mathcal M}_{\mathfrak t}$ with the usual Uhlenbeck compactification. Then $\mathbf L^w_{\mathfrak t,\kappa}$ is a link of $\iota(\bar M^w_\kappa)$, and pairings with it reduce to pairings with $\bar M^w_\kappa$.

## 3. The local computation near $\bar{\mathcal V}(z)\cap M^w_\kappa$ (FL2b §3.4.3)

**Notation.** $\mathcal V(z)$ and $\mathcal W$ are geometric representatives dual to $\mu_p(z)$ and $\mu_c$ (FL2b Definitions 3.4, 3.14). [corrected by checker: Definition 3.4 (`defn:GeomRepresentative`) is the general notion of geometric representative and Definition 3.14 (`defn:GeomReprClosure`) only names the closures $\bar{\mathcal V}(\beta)$, $\bar{\mathcal W}$ and the products $\bar{\mathcal V}(z)$, $\bar{\mathcal W}^m$. The representatives themselves are constructed in FL2b Lemma 3.12 (`lem:MuP1GeomRepr`), for $\mathcal V(\beta)$, and in eq. `eq:SectionMuC1` with Lemma 3.13 (`lem:DefineC1GeomRepr`), where $\mathcal W$ is the zero locus of a generic section of $\mathbb L_{\mathfrak t}$ pulled back from a neighbourhood $\nu(x)$ of a point.] Here $\mu_p(\beta)=-\frac14p_1(\mathbb F_{\mathfrak t})/\beta$, and $\mu_c=c_1(\mathbb L_{\mathfrak t})$ where
$$\mathbb L_{\mathfrak t}=\mathcal C^{*,0}_{\mathfrak t}\times_{(S^1,\times-2)}\mathbb C,\qquad ([A,\Phi],\zeta)\mapsto([A,e^{i\theta}\Phi],e^{2i\theta}\zeta)$$
(FL2b eqs. `eq:DefineC1LineBundle` (3.10), `eq:C1ClassS1Action` (3.11), `eq:DefineC1` (3.12); Memoir eqs. (2.4.5), (2.4.7)). The class $z\in\mathbb A(X)$ is *intersection-suitable* if suitable neighbourhoods $U_i$ of representatives of its factors satisfy $\sum_{\{i:x\in U_i\}}(4-\dim\beta_i)\le4$. By FL2b Lemma 3.17 (`lem:IntersectionSuitable`), this holds if $z$ contains no $H_3$ factors or no $H_0$ factors, so it holds for $z=h^{\delta-2m}x^m$. Set
$$\mathbf K_{A,\delta}=\{(a,\phi)\in T_{[\hat A]}M^w_\kappa\oplus\operatorname{Ker}D_{A,\vartheta}:\ \|\phi\|^2_{L^2}=\delta\}\qquad(\text{eq. `eq:bKAdelta` (3.46)})$$
and $\mathcal Z_A=\boldsymbol\varphi_A^{-1}(0)\cap\mathcal O_A$ (eq. `eq:sZA` (3.40)). FL2b orients $\mathbf K_{A,\delta}/S^1\cong T_{[\hat A]}M^w_\kappa\times\mathbb{CP}^{k-1}$, $k=\dim_{\mathbb C}\operatorname{Ker}D_{A,\vartheta}$, by an orientation of $T_{[\hat A]}M^w_\kappa$ and the complex orientation of $\mathbb{CP}^{k-1}$.

### 3.1 FL2b, Lemma 3.22 (`lem:DeformingV`)

> Let $\mathfrak t$ be a spin$^u$ structure over a four-manifold $X$ with $w_2(\mathfrak t)\equiv w\pmod2$, where $w\in H^2(X;\mathbb Z)$ and $w\pmod2$ is good. Suppose that $\deg(z)\ge\dim M^w_\kappa$ and $z$ is intersection-suitable. Denote $\bar{\mathcal V}(z)\cap\bar M^w_\kappa=\{[\hat A_i]\}_{i=1}^N$. Then for each $[\hat A]\in\bar{\mathcal V}(z)\cap\bar M^w_\kappa$ there is an open neighborhood $\mathcal O_A'\subset\mathcal O_A$ of the origin in $T_{[\hat A]}M^w_\kappa\oplus\operatorname{Ker}D_{A,\vartheta}$ … such that:
> 1. There is a smooth, $S^1$-invariant map $f_A:\mathcal O_A'\cap(\{0\}\oplus\operatorname{Ker}D_{A,\vartheta})\to T_{[\hat A]}M^w_\kappa$ with $f_A(0)=0$ and $(Df_A)_0=0$ such that $\boldsymbol\gamma_A^{-1}(\mathcal V(z))\cap\mathcal O_A'=\{(f_A(\phi),\phi)\}$.
> 2. There is $\varepsilon_0>0$ such that for all $\varepsilon<\varepsilon_0$, $\bar{\mathcal V}(z)\cap\mathbf L^{w,\varepsilon}_{\mathfrak t,\kappa}\subset\bigcup_{i=1}^N\boldsymbol\gamma_{A_i}(\mathcal O'_{A_i})/S^1$, where the union is disjoint.
> 3. For each $\varepsilon\in(0,\varepsilon_0)$ there is $\delta>0$ such that all $(a,\phi)\in\boldsymbol\gamma_A^{-1}(\mathcal V(z)\cap\mathbf L^{w,\varepsilon}_{\mathfrak t,\kappa})\cap\mathcal O'_A$ satisfy $\|\phi\|^2_{L^2}>\delta$.

### 3.1a FL2b, Lemma 3.24 (`lem:ComplexASDOrientationComparison`) [added by checker]

> Let $w$ be an integral lift of $w_2(\mathfrak t)$. Fix an orientation $o=o(\Omega,w)$ of $M^w_\kappa$. Let $O=O^{\rm asd}(\Omega,w)$ be the orientation for $\mathcal M^{*,0}/S^1$ in Definition 2.3. Then, the orientations (3.49) and (3.50) for $\mathcal Z_A\cap\mathbf K_{A,\delta}/S^1$ agree, that is $\omega(\mathbf K,o)/\omega(\mathcal Z)=\omega(\mathcal Z\cap\mathbf K,\partial O)$.

Here $\omega(\mathbf K,o)/\omega(\mathcal Z)$ is the "complex orientation" of $\mathcal Z_A\cap\mathbf K_{A,\delta}/S^1$ (orientation of $T_{[\hat A]}M^w_\kappa$, complex orientation of $\mathbb{CP}^{k-1}$, complex orientation of $\operatorname{Coker}D_{A,\vartheta}$ on the normal bundle of $\mathcal Z_A$), and $\omega(\mathcal Z\cap\mathbf K,\partial O)$ is its orientation as a boundary component of $\mathcal M_{\mathfrak t}$ minus a tube around $\iota(M^w_\kappa)$. The proof is said to be "the same as that of Lemma 2.9". This lemma enters the proof of Lemma 3.26 through eq. `eq:CplxBoundaryOrientationEqualityWithV`, and hence the sign in Proposition 3.29. (Equation numbers (3.49), (3.50) are from the counting script; labels `eq:ComplexOrientOfZK`, `eq:BoundaryOrientationKZ`.)

### 3.2 FL2b, Lemma 3.25 (`lem:OrientationOfV`)

> Let $w$ be an integral lift of $w_2(\mathfrak t)$. Let $\varepsilon(A)=\pm1$ be the signed intersection number of $\mathcal V(z)$ and $M^w_\kappa$ at $[\hat A]$, where $M^w_\kappa$ is given the orientation $o(\Omega,w)$. Then the following map is a diffeomorphism,
> $$g_A=f_A\times\mathrm{id}_{\operatorname{Ker}D_{A,\vartheta}}:\ \mathbb{CP}^{k-1}\to\boldsymbol\gamma_A^{-1}(\mathcal V(z))\cap\mathbf K_{A,\delta}/S^1,\tag{3.53}$$
> where $\mathbb{CP}^{k-1}=\mathbb P(\operatorname{Ker}D_{A,\vartheta})$ … If $\mathbb{CP}^{k-1}$ has the complex orientation and [the target] has the orientation $\omega(\mathbf K,o)/\omega(\mathcal V)$ … for $o=o(\Omega,w)$, then $g_A$ preserves orientation if and only if $\varepsilon(A)=1$.

### 3.3 FL2b, Lemma 3.26 (`lem:Cobordism`)

> Continue the assumptions and notation of Lemma 3.22. For $\varepsilon$ sufficiently small and $\delta$ as in Assertion (3) of Lemma 3.22 and generic, there is a smooth, compact, and oriented cobordism between $\boldsymbol\gamma_A^{-1}(\mathcal V(z)\cap\mathbf L^{w,\varepsilon}_{\mathfrak t,\kappa})$, with the orientation $\omega(\mathbf L,\partial O)/\omega(\mathcal V)$ for $O=O^{\rm asd}(\Omega,w)$, and the manifold $\mathcal Z_A\cap\boldsymbol\gamma_A^{-1}(\mathcal V(z))\cap\mathbf K_{A,\delta}/S^1$, with the orientation $(\omega(\mathbf K,o)/\omega(\mathcal Z))/\omega(\mathcal V)$, where $o=o(\Omega,w)$.

This is the precise form of "the two links are cobordant" promised in FL2a Remark 3.9. It is local: it holds only after cutting down by $\mathcal V(z)$ with $\deg z\ge d_a$.

### 3.4 FL2b, Lemma 3.27 (`lem:HomologyOfMonopolesNearASD`)

> Continue the hypotheses and notation of Lemmas 3.22 and 3.25. Assume that $n_a(\mathfrak t)=\operatorname{ind}_{\mathbb C}D_{A,\vartheta}$ is positive and let $c=\dim_{\mathbb C}\operatorname{Coker}D_{A,\vartheta}$. If $\mathbb{CP}^{k-1}\cong\mathbb P(\operatorname{Ker}D_{A,\vartheta})$ has the complex orientation and $h\in H^2(\mathbb{CP}^{k-1};\mathbb Z)$ is the positive generator, then for generic $\delta>0$, there is a smooth submanifold $T$ of $\mathbb{CP}^{k-1}$ which is Poincaré dual to $h^c$ such that the restriction of the map $g_A$ … to $T$ gives a diffeomorphism, $g_A:T\simeq\mathcal Z_A\cap\boldsymbol\gamma_A^{-1}(\mathcal V(z))\cap\mathbf K_{A,\delta}/S^1$. If $T$ is oriented as the Poincaré dual of $h^c$ and [the target] is oriented by … $o=o(\Omega,w)$, then the restriction of $g_A$ to $T$ is orientation preserving if and only if $\varepsilon(A)=1$.

**Proof mechanism.** $\boldsymbol\varphi_A\circ g_A$ is an $S^1$-equivariant map $S^{2k-1}\to\mathbb C^c\cong\operatorname{Coker}D_{A,\vartheta}$ with diagonal action. It is therefore a section of $S^{2k-1}\times_{S^1}\mathbb C^c\to\mathbb{CP}^{k-1}$ (eq. `eq:ASDObstructionVectorBundle` (3.58)). "Because the action is diagonal, the Euler class of this bundle is $h^c$ (see [FL2a, Lemma 3.27] for a further explanation of the sign)." **[gloss]** In Fulton's convention this obstruction bundle is $\mathcal O(1)^{\oplus c}$; FL do not write it that way here.

### 3.5 FL2b, Lemma 3.28 (`lem:CohomOnASDNormalSlice`)

> Continue the notation and assumptions of Lemmas 3.22, 3.25, and 3.27. Then $(\boldsymbol\gamma_A\circ g_A)^*\mu_c=2h$, where $\mu_c$ is the cohomology class (3.12).

**Proof.** $(\boldsymbol\gamma_A\circ g_A)^*\mathbb L_{\mathfrak t}\cong S^{2k-1}\times_{(S^1,\times-2)}\mathbb C\to S^{2k-1}/S^1$ (eq. `eq:PulledBackDetBundle` (3.59)), which "has first Chern class $2h$, the sign being positive because the $S^1$ action is diagonal". **[gloss]** In Fulton's convention $\mu_c$ restricts to $c_1(\mathcal O(2))$ on each fibre $\mathbb P(\operatorname{Ker}D_{A,\vartheta})$.

### 3.6 FL2b, Proposition 3.29 (`prop:LinkOfASD`), eq. `eq:LinkOfASD` (3.60)

> Let $\mathfrak t$ be a spin$^u$ structure on a four-manifold $X$, with $w$ an integral lift of $w_2(\mathfrak t)$ and $w\pmod2$ is good. We further assume that $d_a(\mathfrak t)=\dim M^w_\kappa\ge0$ and that $n_a(\mathfrak t)=\operatorname{ind}_{\mathbb C}D_A>0$. Let $\delta_c$ be a non-negative integer such that
> $$\deg(z)+2\delta_c=d_a+2n_a-2=\dim(\mathcal M^{*,0}_{\mathfrak t}/S^1)-1.$$
> Suppose $z\in\mathbb A(X)$ has degree $\deg(z)\ge d_a$ and is intersection-suitable. If $\mathbf L^{w,\varepsilon}_{\mathfrak t,\kappa}\cap\iota(M^w_\kappa)$ is oriented as the boundary of $\mathcal M^{*,\ge\varepsilon}_{\mathfrak t}/S^1$, where $\mathcal M^{*,0}_{\mathfrak t}/S^1$ is given the orientation $O^{\rm asd}(\Omega,w)$, then there is a positive constant $\varepsilon_0$ such that for generic $\varepsilon\in(0,\varepsilon_0)$,
> $$\#\big(\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{\delta_c}\cap\mathbf L^{w,\varepsilon}_{\mathfrak t,\kappa}\big)=\begin{cases}2^{n_a-1}\#(\bar{\mathcal V}(z)\cap\bar M^w_\kappa),&\deg(z)=d_a,\\0,&\deg(z)>d_a.\end{cases}\tag{3.60}$$
> Moreover, these intersection numbers are independent of the choice of generic $\varepsilon<\varepsilon_0$.

**Hypotheses.**
* Standing assumptions of FL2b: $X$ closed, connected, smooth and oriented with $b_2^+(X)>0$.
* Generic metric and perturbations (needed for Lemma 3.21 and Corollary 3.6).
* $w\pmod2$ good.
* $d_a\ge0$ and $n_a>0$.
* $\deg z+2\delta_c=d_a+2n_a-2$ and $\deg z\ge d_a$.
* $z$ intersection-suitable.

There is no hypothesis on $b_1$ and none on $\operatorname{Coker}D_{A,\vartheta}$.

**Proof.** By Lemma 3.22(2) the pairing is a finite sum of local terms. Each term equals, with $k=n_a+c$ and $q$ the multiplicity of $\bar{\mathcal V}(z)$,
$$q\,\varepsilon(A)\,\big\langle(2h)^{n_a-1}\smile h^c,[\mathbb{CP}^{n_a+c-1}]\big\rangle=q\,\varepsilon(A)\,2^{n_a-1},$$
by Lemmas 3.26, 3.25, 3.27 and 3.28.

**Notation.** $\mathcal M^{*,\ge\varepsilon}_{\mathfrak t}$ is the part with $\|\Phi\|^2_{L^2}\ge\varepsilon$. The orientation $O^{\rm asd}(\Omega,w)$ is FL2b Definition 2.3 (`defn:ASDOrient`). **[gloss]** The phrase "$\mathbf L^{w,\varepsilon}_{\mathfrak t,\kappa}\cap\iota(M^w_\kappa)$ is oriented" is copied as printed. The link does not meet $\iota(M^w_\kappa)$, and the intended object is $\mathbf L^{w,\varepsilon}_{\mathfrak t,\kappa}$ itself.

**Role.** This is the instanton end of the cobordism. The index $n_a$ of the coupled Dirac operator enters in three ways:
* $2n_a$ is the real codimension of $M^w_\kappa$ in $\mathcal M_{\mathfrak t}$, and $n_a>0$ is needed for a non-empty link. [corrected by checker: the sources do not say the link is empty when $n_a\le0$. FL2a (text after Corollary 3.6) says only that if $n_a\le0$ then, at a generic point where $\operatorname{Ker}D_{A,\vartheta}=0$ and *assuming* transversality to the jumping-line strata, a neighbourhood of $[A,0]$ contains no non-zero-section points, "for this reason, we will restrict our attention to the cases where $n_a>0$". Points with $\operatorname{Ker}D_{A,\vartheta}\neq0$ can still occur, and Memoir Remark 2.6.1 asserts, without proof, that for $n_a\le0$ the pairing in (2.6.2) (with $\eta=0$) is "a constant times the spin polynomial invariant". What is true is that $n_a>0$ is a hypothesis of Proposition 3.29 and of Lemma 3.27.]
* $\dim\mathcal M^{*,0}_{\mathfrak t}/S^1=d_a+2n_a-1$ fixes the power $n_a-1$ of $\mu_c$.
* That power, through $\mu_c\mapsto2h$, produces the factor $2^{n_a-1}$.

The Memoir obtains the Donaldson invariant by applying the proposition on $X\#\overline{\mathbb{CP}}^2$.

### 3.7 Restatements and a related result

* **Memoir**, §2.6, eq. `eq:ASDPairing` (2.6.2): "When $\deg(z)=\dim M^w_\kappa$ and $n_a(\mathfrak t)>0$, the intersection … is given by [FL2b, Lemma 3.30]: $2^{1-n_a}\#(\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{n_a-1}\cap\bar{\mathbf L}^w_{\mathfrak t,\kappa})=\#(\bar{\mathcal V}(z)\cap\bar M^w_\kappa)$." Remark 2.6.1 (unlabelled) adds two points. If $\deg z>\dim M^w_\kappa$ (with exponent $\eta$ given by (2.4.8)), the number vanishes. "If $n_a(\mathfrak t)\le0$ … the intersection number … is a constant times the spin polynomial invariant [PTDirac]." L1 eq. `eq:ASDPairing` (2.51) cites the same "[FL2b, Lemma 3.30]". In the arXiv source of FL2b, Lemma 3.30 does not exist under that name: 3.30 is Proposition `prop:PU(2)MonopoleExist`, and the result is Proposition 3.29. FL6 cites it correctly as "[FL2b, Proposition 3.29]".
* **Ann.**, Lemma 3.17 (`lem:LinkOfASD`), attributed to [FL2] (the preprint later split into FL2a and FL2b): the same $2^{n_a-1}D^{c_1(E)}_X(z)$ formula, under "$b^+(X)>0$ and generic Riemannian metric; choose $c_1(E)\pmod2$ so that $\mathfrak{su}(E)$ does not admit a flat connection", with $n_{p_1}+n_{c_1}=d_a+n_a-1$ in its own notation. Ann. Lemma 3.14 (`lem:CohomOnASDNormalSlice`) is the announcement's form of FL2b Lemma 3.28: "$\bar W(x)$ is Poincaré dual to $2h$".
* **FL2b, Proposition 3.30** (`prop:PU(2)MonopoleExist`): "Let $\mathfrak t$ be a spin$^u$ structure on a four-manifold $X$, where we allow $b_2^+(X)\ge0$, and suppose $w_2(\mathfrak t)\equiv w\pmod2$ … Assume that $w\pmod2$ is good. If $n_a(\mathfrak t)>0$, then for a generic, $C^\infty$ pair $(g,\rho)$ … and generic, $C^\infty$ parameters $(\tau,\vartheta)$, the moduli space $\mathcal M^{*,0}_{\mathfrak t}$ … is non-empty if the moduli space $M^{w,*}_\kappa$ … is non-empty." The proof is that the obstruction Euler class $h^c$ of Lemma 3.27 is non-trivial.
* [added by checker] **FL2b, Corollary 3.18** (`cor:IntersectionOfSmoothLowerStrata`). This is what keeps every intersection with every link in the top stratum, and it is where intersection-suitability enters:
  > Let $z\in\mathbb A(X)$ be intersection-suitable and let $\delta_c$ be a non-negative integer satisfying $\deg(z)+2\delta_c=\dim(\mathcal M^{*,0}_{\mathfrak t}/S^1)-1=d_a+2n_a-2$. Then for generic choices of geometric representatives, the intersection $\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{\delta_c}\cap\bar{\mathcal M}^{*,0}_{\mathfrak t}/S^1$ is a collection of one-dimensional manifolds, disjoint from the lower strata of $\bar{\mathcal M}^*_{\mathfrak t}/S^1$.
  
  The argument before it is a dimension count: a point in level $\ell$ lies in $\mathcal V_\ell(z')\cap\mathcal W_\ell^{\delta_c-j}\cap\mathcal M_{\mathfrak t_\ell}/S^1$, of dimension at most $1-\ell$ in general and at most $1-2\ell$ when eq. `eq:CoDimBound2` (3.25) holds. Without intersection-suitability a level-one point is not excluded. The unlabelled Remark 3.19 that follows says: "The restriction that $z\in\mathbb A(X)$ be intersection-suitable is a technical one and it should be possible to remove it; we plan to address this point in a subsequent paper." The proof of L1 Lemma 3.9 cites this corollary, and the proof of Memoir Lemma 8.1.5 "translates immediately" from L1's. Yet L1 Lemma 3.9 is stated "for all $z\in\mathbb A(X)$", and Memoir Theorem 8.1.9 and Lemma 8.1.5 do not list intersection-suitability among their hypotheses either; the Memoir's main theorems use $z=h^{\delta-2m}x^m$, which is intersection-suitable by Lemma 3.17.

---

# Part II. Seiberg–Witten strata in the top level ($\ell=0$)

## 4. Embedding and abstract link

**FL2a, Lemma 3.13** (`lem:RedAreSW`): if $w_2(\mathfrak t)\ne0$ and $\mathfrak t=\mathfrak s\oplus\mathfrak s\otimes L$, then $\iota$ restricts to a topological embedding $M_{\mathfrak s}\hookrightarrow\mathcal C_{\mathfrak t}$ with image the reducibles for $V=W\oplus W\otimes L$. The Memoir (§2.3.3) restates this as "an embedding of $M_{\mathfrak s}$ if $w_2(\mathfrak t)\neq0$ or $b_1(X)=0$". **FL2b, Lemma 3.32** (`lem:SplittingSpinu`): $\mathfrak t$ splits as $\mathfrak s\oplus\mathfrak s'$ iff $(c_1(\mathfrak t)-c_1(\mathfrak s))^2=p_1(\mathfrak t)$ (eq. (3.63)).

**FL2a, Definition 3.14** (`defn:AbstractLink`), copied in full:
> Let $Z$ be a closed subset of a smooth, Riemannian manifold $M$, and suppose that $Z=Z_0\cup Z_1$, where $Z_0$ and $Z_1$ are locally closed, smooth submanifolds of $M$ and $Z_1\subset\bar Z_0$. … Let $N_{Z_1}$ be the normal bundle of $Z_1\subset M$ and let $\mathcal O'\subset N_{Z_1}$ be an open neighborhood of the zero section … such that there is a diffeomorphism $\gamma$, commuting with the zero section of $N_{Z_1}$ (so $\gamma|_{Z_1}=\mathrm{id}_{Z_1}$), from $\mathcal O'$ onto an open neighborhood $\gamma(\mathcal O')$ of $Z_1\subset M$. Let $\mathcal O\Subset\mathcal O'$ be an open neighborhood of the zero section … where $\bar{\mathcal O}=\mathcal O\cup\partial\mathcal O\subset\mathcal O'$ is a smooth manifold-with-boundary. Then $L_{Z_1}=Z_0\cap\gamma(\partial\mathcal O)$ is a *link of $Z_1$ in $Z_0$*.

FL2a explains why this needs a finite-dimensional ambient manifold. $M_{\mathfrak s}$ need not consist of regular points, and "a local model of the link does not suffice as only one of our cohomology classes extend over $M_{\mathfrak s}$ (and that one vanishes in many cases), so we cannot use geometric representatives to cut down to a generic point in $M_{\mathfrak s}$" (FL2a, start of §3.4). [corrected by checker: the two reasons are separate. The quoted sentence, from the start of §3.4, explains why a *global* model along all of $M_{\mathfrak s}$ is needed, in contrast with the local model used at $M^w_\kappa$. On finite-dimensionality, FL2a says after Definition 3.14 that the ambient manifold "is not required to be finite-dimensional, [but] we shall impose this constraint as we need to define a fundamental class for the sphere bundle of $N_{Z_1}$". In the application, $Z_0$ is $\mathcal M^{*,0}_{\mathfrak t}$ near $\iota(M_{\mathfrak s})$ and $Z_1=M_{\mathfrak s}$.]

## 5. The thickened moduli space, the virtual normal bundle and the link

### 5.1 FL2a, Theorem 3.19 (`thm:DefnOfStabilizeBundle`)

> Assume that the moduli space $M_{\mathfrak s}$ contains no zero-section pairs. Then there is an open neighborhood $\mathcal U$ of the subspace $\iota(M_{\mathfrak s})$ in $\mathcal C_{\mathfrak t}$, which does not contain any zero-section pairs or other reducibles, and a finite-rank, smooth, trivial, vector subbundle $\Xi\to\mathcal U$ of $\mathfrak V\to\mathcal U$, which is $S^1$ equivariant with respect to the circle action (3.2), such that the following hold:
> 1. The restriction of $\Xi$ to $\iota(M_{\mathfrak s})$ is a complex vector bundle.
> 2. The smooth bundle map $\Pi_{\Xi^\perp}:\mathfrak V\to\Xi^\perp$ defined by the fiberwise $L^2$-orthogonal projection … restricts to a surjective fiber map $\Pi_{\Xi^\perp}:\operatorname{Ran}(D\mathfrak S)_{A,\Phi}\to\Xi^\perp_{A,\Phi}$ for any point $[A,\Phi]\in\mathcal U$.
> 3. If $(A,\Phi)$ is an $L^2_\ell$ representative of a point in $\mathcal U$, for some integer $k\le\ell\le\infty$, then the fiber $\Xi_{A,\Phi}$ is contained in $L^2_\ell(F_2)=L^2_\ell(\Lambda^+\otimes\mathfrak g_{\mathfrak t})\oplus L^2_\ell(V^-)$.

Here $\mathfrak V=\tilde{\mathcal C}_{\mathfrak t}\times_{\mathcal G_{\mathfrak t}}L^2_{k-1}(F_2)\to\mathcal C_{\mathfrak t}$ is the infinite-rank obstruction bundle and $\mathfrak S$ its section given by the equations (eq. `eq:S1EquivInfRankObstBundle` (3.38)). The construction is the Atiyah–Singer stabilisation, chosen "because one cannot guarantee that $\operatorname{Coker}\mathbf D$ will either vanish or even have constant rank due to spectral flow" (FL2a §3.5).

### 5.2 FL2a, Definition 3.20 (`defn:ThickenedModuliSpace`)

> Assume $M_{\mathfrak s}$ contains no zero-section pairs. Let $\Xi$ be a finite-rank, smooth, $S^1$-equivariant vector bundle over an open neighborhood of $\iota(M_{\mathfrak s})$ in $\mathcal C_{\mathfrak t}$ such that, as in Theorem 3.19, $L^2$-orthogonal projection gives a surjective map of quasi vector bundles $\operatorname{Ran}D\mathfrak S\to\Xi^\perp$ over $M_{\mathfrak s}$. We say that $\Xi$ is a *stabilizing bundle* for $\operatorname{Ran}D\mathfrak S$ and call
> $$\mathcal M_{\mathfrak t}(\Xi,\mathfrak s)=(\Pi_{\Xi^\perp}\mathfrak S)^{-1}(0)\subset\mathcal C_{\mathfrak t}\tag{3.41}$$
> the *thickened moduli space* defined by $\Xi$. … We then define
> $$N_{\mathfrak t}(\Xi,\mathfrak s)=\operatorname{Ker}(\Pi_{\Xi^\perp}\boldsymbol{\mathcal D}^n),\tag{3.42}$$
> a complex, finite-rank, smooth vector bundle over $M_{\mathfrak s}$ with fibers $N_{\mathfrak t}(\Xi,\mathfrak s)|_{[A,\Phi]}\cong\operatorname{Ker}(d^{0,n,*}_{A,\Phi}+\Pi_{\Xi^\perp}d^{1,n}_{A,\Phi})$, noting that $\mathcal D^n_{A,\Phi}=d^{0,n,*}_{A,\Phi}+d^{1,n}_{A,\Phi}$ for $[A,\Phi]\in\iota(M_{\mathfrak s})$.

$\mathcal D^n$ is the *normal* part of the deformation operator at a reducible. Its domain is sections of $(\Lambda^1\otimes L)\oplus(W^+\otimes L)$ and its range $(\Lambda^0\oplus\Lambda^+)\otimes L\oplus W^-\otimes L$ (FL2a eq. `eq:UniversalBundle`). FL2a Lemma 3.15 (`lem:IdentityOfReducibleCohomology`) splits $H^\bullet_{\iota(B,\Psi)}\cong H^\bullet_{B,\Psi}\oplus H^{\bullet,n}_{\iota(B,\Psi)}$, the first summand being the SW deformation cohomology.

### 5.3 FL2a, Theorem 3.21 (`thm:ThickenedModuliSpace`)

> Suppose that the spin$^u$ structure $\mathfrak t$ admits a reduction $\mathfrak t=\mathfrak s\oplus\mathfrak s\otimes L$. Assume $M_{\mathfrak s}$ contains no zero-section pairs. Then the following hold:
> 1. There is an $S^1$-invariant, open neighborhood $\mathcal U$ of $\iota(M_{\mathfrak s})$ in $\mathcal C_{\mathfrak t}$ such that the zero locus $\mathcal U\cap\mathcal M_{\mathfrak t}(\Xi,\mathfrak s)$ is regular and so a manifold of dimension $\dim\mathcal M_{\mathfrak t}+\operatorname{rank}_{\mathbb R}\Xi$.
> 2. The space $M_{\mathfrak s}$ is a smooth, $S^1$-invariant submanifold of $\mathcal M_{\mathfrak t}(\Xi,\mathfrak s)$.
> 3. The bundle $N_{\mathfrak t}(\Xi,\mathfrak s)$ is a normal bundle for the submanifold $\iota:M_{\mathfrak s}\hookrightarrow\mathcal M_{\mathfrak t}(\Xi,\mathfrak s)$ and the tubular map is equivariant with respect to the circle action on $N_{\mathfrak t}(\Xi,\mathfrak s)$ given by the trivial action on the base $M_{\mathfrak s}$ and complex multiplication on the fibers, and the circle action on $\mathcal M_{\mathfrak t}(\Xi,\mathfrak s)$ induced from the $S^1$ action (3.2).
> 4. The restriction of the section $\mathfrak S$ to $\mathcal M_{\mathfrak t}(\Xi,\mathfrak s)$ takes values in $\Xi$ and vanishes transversely on $\mathcal M_{\mathfrak t}(\Xi,\mathfrak s)-\iota(M_{\mathfrak s})$.

**Hypotheses.** A splitting of $\mathfrak t$ and no zero-section pairs in $M_{\mathfrak s}$. Generic parameters (FL2a Theorem 2.13) are used for assertion (4), and SW transversality (FL2a Proposition 2.16, `prop:SmoothFamilyOfReducibles`) for $H^2_{B,\Psi}=0$.

**After the theorem (FL2a §3.5.3).** The equivariant tubular-neighbourhood theorem gives $\boldsymbol\gamma:\mathcal O\hookrightarrow\mathcal C_{\mathfrak t}$ from a neighbourhood of the zero section of $N_{\mathfrak t}(\Xi,\mathfrak s)$ (eq. `eq:NormalBundleNbhdEmbedding` (3.44)). It "descends to a homeomorphism, and a diffeomorphism on smooth strata, from the zero locus $\boldsymbol\varphi^{-1}(0)/S^1$ in $N_{\mathfrak t}(\Xi,\mathfrak s)/S^1$ onto an open neighborhood of $\iota(M_{\mathfrak s})$ in the actual moduli space". Here
$$\boldsymbol\varphi=\Pi_\Xi\mathfrak S\circ\boldsymbol\gamma\quad\text{(3.45)},\qquad\boldsymbol\gamma^*\Xi\to N_{\mathfrak t}(\Xi,\mathfrak s)\quad\text{(3.46)},$$
and "$(\boldsymbol\gamma^*\Xi)/S^1\cong(\pi_N^*\Xi)/S^1\to N_{\mathfrak t}(\Xi,\mathfrak s)/S^1$" on the complement of the zero section.

### 5.4 FL2a, Definition 3.22 (`defn:LinkOfReducible`), eq. `eq:DefineReducibleLink` (3.47)

> Assume $M_{\mathfrak s}$ contains no zero-section pairs. Let $N^\varepsilon_{\mathfrak t}(\Xi,\mathfrak s)\subset N_{\mathfrak t}(\Xi,\mathfrak s)$ be the sphere bundle of fiber vectors of length $\varepsilon$ and set $\mathbb PN_{\mathfrak t}(\Xi,\mathfrak s)=N^\varepsilon_{\mathfrak t}(\Xi,\mathfrak s)/S^1$. The *link of the stratum $\iota(M_{\mathfrak s})\subset\mathcal M_{\mathfrak t}$* of reducible PU(2) monopoles is defined by
> $$\mathbf L_{\mathfrak t,\mathfrak s}=\boldsymbol\gamma\big(\boldsymbol\varphi^{-1}(0)\cap\mathbb PN_{\mathfrak t}(\Xi,\mathfrak s)\big)\subset\mathcal M^{*,0}_{\mathfrak t}/S^1.$$
> The orientation for $\mathbf L_{\mathfrak t,\mathfrak s}$ is defined by the orientation on $M_{\mathfrak s}$ and in turn from the homology orientation $\Omega$ … and the complex structure on the fibers of $N_{\mathfrak t}(\Xi,\mathfrak s)$ given by the $S^1$ action. We treat the quotient $\mathbb PN_{\mathfrak t}(\Xi,\mathfrak s)$ as the complex projectivization of a complex vector bundle; we use the complex orientation on the obstruction bundle $\boldsymbol\gamma^*\Xi$.

### 5.5 FL2a, Lemma 3.23 (`lem:TransverseObstruction`) and eq. (3.48)

> Assume $M_{\mathfrak s}$ contains no zero-section pairs. Then for generic $\varepsilon$, the section $\boldsymbol\varphi$ of the obstruction bundle $\boldsymbol\gamma^*\Xi$ in (3.46) vanishes transversely on $N^\varepsilon_{\mathfrak t}(\Xi,\mathfrak s)$.

Consequently (eq. `eq:DefineHomologyOfReducibleLink` (3.48)):
$$[\mathbf L_{\mathfrak t,\mathfrak s}]=e\big((\boldsymbol\gamma^*\Xi)/S^1\big)\cap[\mathbb PN_{\mathfrak t}(\Xi,\mathfrak s)].$$

**Role of §5.** This is the complete description of a top-level SW link. It is a compact smooth manifold: the zero set of a transverse section of the obstruction bundle $\boldsymbol\gamma^*\Xi/S^1$ over the projectivisation of a genuine complex vector bundle $N\to M_{\mathfrak s}$. "Virtual normal bundle" in the K-theoretic sense means $[N]-[\Xi]$ (Memoir §2.3.5). The Overlap paper (§1) summarises: "the link $\mathbf L_{\mathfrak t,\mathfrak s}$ as the intersection of the zero-locus of an obstruction bundle with the boundary of a disk bundle (or an orbifold disk bundle when $\ell=1$)". No gluing is needed, and nothing in §5 is conditional.

### 5.6 Memoir restatement (§2.3.5, `subsubsec:ThickenedNeighborhood`)

The Memoir restates §§5.1–5.5 with notation $\Xi_{\mathfrak t,\mathfrak s}$, $N_{\mathfrak t,\mathfrak s}$:
* eq. (2.3.19): $\pi_\Xi:\Xi_{\mathfrak t,\mathfrak s}\to M_{\mathfrak s}$, $\pi_N:N_{\mathfrak t,\mathfrak s}\to M_{\mathfrak s}$, with $\Xi_{\mathfrak t,\mathfrak s}\cong M_{\mathfrak s}\times\mathbb C^{r_\Xi}$;
* eq. (2.3.20): the embedding $\boldsymbol\gamma_{\mathfrak s}:N_{\mathfrak t,\mathfrak s}(\varepsilon)\hookrightarrow\mathcal C_{\mathfrak t}$, quoted as "[FL2a, Theorem 3.21]";
* eq. (2.3.22): the homeomorphism $\boldsymbol\chi_{\mathfrak s}^{-1}(0)\cap N_{\mathfrak t,\mathfrak s}(\varepsilon)\cong\mathcal M_{\mathfrak t}\cap\boldsymbol\gamma_{\mathfrak s}(N_{\mathfrak t,\mathfrak s}(\varepsilon))$;
* the dimension and rank relations
$$\dim\mathcal M_{\mathfrak t}=2n_s(\mathfrak t,\mathfrak s)+d_s(\mathfrak s)\quad(2.3.23),\qquad r_N(\mathfrak t,\mathfrak s)=n_s(\mathfrak t,\mathfrak s)+r_\Xi\quad(2.3.25),$$
with $n_s=n_s'+n_s''$ as given in (2.3.24) (see §6.1). The Memoir calls $n_s$ "minus the complex index of the normal deformation operator", whereas FL2a (3.71) writes $\operatorname{ind}_{\mathbb C}\mathcal D^n_{\iota(B,\Psi)}=n_s$. **[gloss]** The two agree if the Memoir's "index" means the index of the normal deformation *complex*, which is minus the index of the rolled-up operator $\mathcal D^n=d^{0,n,*}+d^{1,n}$. The rank relation (2.3.25) and FL2a (3.55) both require $n_s=\operatorname{ind}_{\mathbb C}\mathcal D^n$.

The Memoir also gives the equivariance of the lift $\tilde{\boldsymbol\gamma}_{\mathfrak s}$ for the action (2.3.28): $(B,\Psi,\beta,\psi)\mapsto(B,e^{i\theta}\Psi,\beta,e^{i\theta}\psi)$ on $\tilde N_{\mathfrak t,\mathfrak s}$. It closes: "the Chern character of the bundle $N_{\mathfrak t,\mathfrak s}$ is computed in [FL2a, Theorem 3.29] while the Segre classes of this bundle are computed, under some additional assumptions, in [FL2b, Lemma 4.11]."

## 6. Characteristic classes on the level-zero link

### 6.1 FL2a, Theorem 3.29 (`thm:ChernCharacterOfNormal`) and Corollary 3.30 (`cor:SimpleNormalChernClass`)

In $K(M_{\mathfrak s})$ (eq. `eq:NormalBundleIsNormalStab` (3.55)):
$$\operatorname{ind}\boldsymbol{\mathcal D}^n=[N_{\mathfrak t}(\Xi,\mathfrak s)]-[\Xi]=[N_{\mathfrak t}(\Xi,\mathfrak s)]-[M_{\mathfrak s}\times\mathbb C^{r_\Xi}].$$
The indices are defined by $\operatorname{ind}_{\mathbb C}\mathcal D^n=n_s=n_s'+n_s''$, with $n_s'=\operatorname{ind}_{\mathbb C}(d^*_{A_L}+d^+_{A_L})$ and $n_s''=\operatorname{ind}_{\mathbb C}D''_{B\otimes A_L}$ (eq. `eq:SplittingNormalIndex` (3.71)), and
$$n_s'(\mathfrak t,\mathfrak s)=-(c_1(\mathfrak s)-c_1(\mathfrak t))^2-\tfrac12(\chi+\sigma),\qquad n_s''(\mathfrak t,\mathfrak s)=\tfrac18\big((2c_1(\mathfrak t)-c_1(\mathfrak s))^2-\sigma\big)\tag{3.72}$$
(`eq:DefOfNormalIndices`).

> **Theorem 3.29.** Let $\mathfrak t$ be a spin$^u$ structure over a closed, oriented, Riemannian, smooth four-manifold $X$. Assume $\mathfrak t$ admits a splitting $\mathfrak t=\mathfrak s\oplus\mathfrak s\otimes L$, where $L$ is a complex line bundle. Suppose that there are no zero-section pairs in $M_{\mathfrak s}$. Let $\mu_{\mathfrak s}$ be the Seiberg–Witten $\mu$-map … Let $x\in H_0(X;\mathbb Z)$ be the positive generator and for $\{\gamma_i\}$ a basis for $H_1(X;\mathbb Z)/\mathrm{Tor}$, let $\{\gamma_i^*\}$ be the dual basis … Let $r_\Xi=\operatorname{rank}_{\mathbb C}\Xi$. Then
> $$\begin{aligned}\operatorname{ch}(N_{\mathfrak t}(\Xi,\mathfrak s))&=r_\Xi+n_s''e^{\mu_{\mathfrak s}(x)}+n_s'e^{2\mu_{\mathfrak s}(x)}-8\sum_{i<j}\langle\gamma_i^*\gamma_j^*(c_1(\mathfrak t)-c_1(\mathfrak s)),[X]\rangle e^{2\mu_{\mathfrak s}(x)}\mu_{\mathfrak s}(\gamma_i\gamma_j)\\&\quad+\tfrac12\sum_{i<j}\langle\gamma_i^*\gamma_j^*(2c_1(\mathfrak t)-c_1(\mathfrak s)),[X]\rangle e^{\mu_{\mathfrak s}(x)}\mu_{\mathfrak s}(\gamma_i\gamma_j)\\&\quad+(e^{\mu_{\mathfrak s}(x)}-32e^{2\mu_{\mathfrak s}(x)})\sum_{i<j<k<\ell}\langle\gamma_i^*\gamma_j^*\gamma_k^*\gamma_\ell^*,[X]\rangle\mu_{\mathfrak s}(\gamma_i\gamma_j\gamma_k\gamma_\ell).\end{aligned}\tag{3.73}$$

> **Corollary 3.30.** Continue the hypotheses of Theorem 3.29 and assume that $\alpha\smile\alpha'=0$, for every $\alpha,\alpha'\in H^1(X;\mathbb Z)$. Then, as elements of $H^\bullet(M_{\mathfrak s};\mathbb R)$,
> $$c(N_{\mathfrak t}(\Xi,\mathfrak s))=(1+2\mu_{\mathfrak s}(x))^{n_s'}(1+\mu_{\mathfrak s}(x))^{n_s''}.$$

**[gloss]** The weight-$2$ summand comes from the tangential-to-$L$ part $\Lambda^1\otimes L$, on which $s\in\mathcal G_{\mathfrak s}$ acts by $s^{-2}$. The weight-$1$ summand comes from the Dirac part $W^+\otimes L$, with action $s^{-1}$.

### 6.2 FL2b, Definition 4.3 (`defn:nu`) and Lemma 4.8 (`lem:PullbackOfc1`)

> **Definition 4.3.** Let $\nu\in H^2(\mathbb PN_{\mathfrak t}(\Xi,\mathfrak s);\mathbb Z)$ be the negative of the first Chern class of the $S^1$ bundle $N^\varepsilon_{\mathfrak t}(\Xi,\mathfrak s)\to\mathbb PN_{\mathfrak t}(\Xi,\mathfrak s)$. Restricted to each fiber of $\mathbb PN_{\mathfrak t}(\Xi,\mathfrak s)$, the class $\nu$ is the positive generator of the cohomology. With the conventions of [Fulton, §3.1], the class $\nu$ is the first Chern class of the line bundle $\mathcal O_{\mathbb PN_{\mathfrak t}(\Xi,\mathfrak s)}(1)$, the dual of the tautological bundle.

> **Lemma 4.8.** Continue the hypotheses of Lemma 4.4 and let $\nu$ be the cohomology class in Definition 4.3. Then $\boldsymbol\gamma^*\mu_c=\nu\in H^\bullet(\mathbb PN_{\mathfrak t}(\Xi,\mathfrak s);\mathbb R)$ (4.20).

**[gloss]** Compare FL2b Lemma 3.28 ($\mu_c\mapsto2h$) at the instanton link. The difference comes from the relation $\mathrm{diag}(1,e^{2i\theta})=e^{i\theta}u$: the fibres of $N$ carry the action (3.2), which already has weight two relative to scalar multiplication on $V$.

### 6.3 FL2b, Corollaries 4.6–4.7 (`cor:UniversalPontrjaginClassPullback`, `cor:CohomologyOnReducibleLink`)

> **Corollary 4.6.**
> $$(\boldsymbol\gamma\times\mathrm{id}_X)^*p_1(\mathbb F_{\mathfrak t})=\big(\pi_{\mathbb PN}^*\nu+2(\pi_{\mathfrak s}\times\pi_X)^*c_1(\mathbb L_{\mathfrak s})+\pi_X^*(c_1(\mathfrak t)-c_1(\mathfrak s))\big)^2\in H^2(\mathbb PN_{\mathfrak t}(\Xi,\mathfrak s)\times X;\mathbb Z).\tag{4.18}$$

The degree printed as "$H^2$" should be $H^4$.

> **Corollary 4.7.** … if $x\in H_0(X;\mathbb Z)$ is the positive generator, $\gamma\in H_1(X;\mathbb R)$, $h\in H_2(X;\mathbb R)$, and $[Y]\in H_3(X;\mathbb R)$ …
> $$\begin{aligned}\boldsymbol\gamma^*\mu_p([Y])&=\textstyle\sum_i\langle(c_1(\mathfrak s)-c_1(\mathfrak t))\smile\gamma_i^*,[Y]\rangle\mu_{\mathfrak s}(\gamma_i),\\\boldsymbol\gamma^*\mu_p(h)&=\tfrac12\langle c_1(\mathfrak s)-c_1(\mathfrak t),h\rangle(2\mu_{\mathfrak s}(x)+\nu)-2\textstyle\sum_{i<j}\langle\gamma_i^*\smile\gamma_j^*,h\rangle\mu_{\mathfrak s}(\gamma_i\gamma_j),\\\boldsymbol\gamma^*\mu_p(\gamma)&=-\textstyle\sum_i\langle\gamma_i^*,\gamma\rangle(2\mu_{\mathfrak s}(x)+\nu)\smile\mu_{\mathfrak s}(\gamma_i),\\\boldsymbol\gamma^*\mu_p(x)&=-\tfrac14(2\mu_{\mathfrak s}(x)+\nu)^2.\end{aligned}\tag{4.19}$$

**Hypotheses.** Those of FL2b Lemma 4.4 (`lem:UniversalReduction`): $\mathfrak t=\mathfrak s\oplus\mathfrak s\otimes L$, and $M_{\mathfrak s}$ has no zero-section pairs.

### 6.4 FL2b, Lemma 4.9 (`lem:EulerClassOfObstruction`)

> The vector bundle $\boldsymbol\gamma^*\Xi/S^1$ has Euler class $e(\boldsymbol\gamma^*\Xi/S^1)=\nu^{r_\Xi}$, where $\nu$ is the cohomology class in Definition 4.3, $r_\Xi=\operatorname{rank}_{\mathbb C}\Xi$, and
> $$[\mathbf L_{\mathfrak t,\mathfrak s}]=\nu^{r_\Xi}\cap[\mathbb PN_{\mathfrak t}(\Xi,\mathfrak s)],$$
> where $\mathbf L_{\mathfrak t,\mathfrak s}$ is given the complex orientation of Definition 2.7 and $[\mathbb PN_{\mathfrak t}(\Xi,\mathfrak s)]$ is given the orientation defined by the orientation of $TM_{\mathfrak s}$ and the complex orientation of the fibers.

The proof records $\boldsymbol\gamma^*(\Xi/S^1)\cong N^\varepsilon_{\mathfrak t}(\Xi,\mathfrak s)\times_{(S^1,\times-1)}\mathbb C^{r_\Xi}$, "where the factor $-1$ indicates that the $S^1$ action … is diagonal". **[gloss]** So $\boldsymbol\gamma^*\Xi/S^1\cong\mathcal O(1)^{\oplus r_\Xi}$.

### 6.5 FL2b, Lemma 4.10 (`lem:Segre`) and Lemma 4.11 (`lem:SegreOfN`)

> **Lemma 4.10.** Let $N$ be a complex rank-$r$ vector bundle with Chern classes $c_i$ over an oriented, real $m$-dimensional manifold $M$. … Define Segre classes $s_i$ by $(1+c_1+\cdots+c_r)(s_0+s_1+\cdots)=1$. Let $\pi:\mathbb P(N)\to M$ be the projectivization of $N$ and $h$ the negative of the first Chern class of the bundle $N^\varepsilon\to\mathbb P(N)$. Then, for any $\alpha\in H^{m-2i}(M;\mathbb Z)$,
> $$\langle h^{r+i-1}\smile\pi^*\alpha,[\mathbb P(N)]\rangle=\langle s_i\smile\alpha,[M]\rangle,\tag{4.24}$$
> where $\mathbb P(N)$ is given the orientation arising from that of $M$ and the complex orientation of the fibers of $\pi$.

> **Lemma 4.11.** Suppose that for all $\alpha,\alpha'\in H^1(X;\mathbb Z)$ one has $\alpha\smile\alpha'=0$. Let $\mathfrak t$ be a spin$^u$ structure with $\mathfrak t=\mathfrak s\oplus\mathfrak s\otimes L$ and assume $M_{\mathfrak s}$ contains no zero-section pairs. Then the bundle $N_{\mathfrak t}(\Xi,\mathfrak s)\to M_{\mathfrak s}$ has Segre classes
> $$s_i(N_{\mathfrak t}(\Xi,\mathfrak s))=\mu_{\mathfrak s}(x)^i\sum_{j=1}^i2^j\binom{-n_s'}{j}\binom{-n_s''}{i-j},\qquad i=0,1,2,\dots\tag{4.26}$$

As printed, the sum starts at $j=1$. The proof gives $s(N)=(1+2\mu)^{-n_s'}(1+\mu)^{-n_s''}$, so the correct lower limit is $j=0$. L1 Lemma 2.4 (`lem:TopOfReducibleNormal`) restates the result with $\sum_{j=0}^p$ and the hypothesis "$b_1(X)=0$".

### 6.6 Orientation: FL2b Definition 2.7, Lemma 2.9, Lemma 3.31

* **Definition 2.7** (`defn:ComplexOrientation`). The *complex orientation* of $\mathbf L_{\mathfrak t,\mathfrak s}$ uses the $\Omega$-orientation of $M_{\mathfrak s}$, the complex orientation of $\boldsymbol\gamma^*\Xi\to\mathbb PN$, and the complex orientation of the fibres of $\mathbb PN$.
* **Lemma 2.9** (`lem:ReducibleOrientation`): "The complex orientation … of the link $\mathbf L_{\mathfrak t,\mathfrak s}$ agrees with the boundary orientation (Definition 2.8) of $\mathbf L_{\mathfrak t,\mathfrak s}$ determined by the orientation $O^{\rm red}(\Omega,\mathfrak t,\mathfrak s)$."
* **Lemma 2.6** (`lem:OrientComparison`): $O^{\rm asd}(\Omega,w)=(-1)^{\frac14(w-c_1(L))^2}O^{\rm asd}(\Omega,c_1(L))$ and $O^{\rm asd}(\Omega,c_1(L))=O^{\rm red}(\Omega,\mathfrak t,\mathfrak s)$.
* **Lemma 3.31** (`lem:CohomOnReducibleLink`). Let $\mathfrak t$ be a spin$^u$ structure over a four-manifold $X$, with $w$ an integral lift of $w_2(\mathfrak t)$, and assume $w\pmod2$ is good. If $z\in\mathbb A(X)$ is intersection-suitable and $\deg(z)+2\delta_c=d_a+2n_a-2$, then
$$\#(\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{\delta_c}\cap\mathbf L_{\mathfrak t,\mathfrak s})=(-1)^{\frac14(w-c_1(L))^2}\langle\mu_p(z)\smile\mu_c^{\delta_c},[\mathbf L_{\mathfrak t,\mathfrak s}]\rangle,$$
with the boundary orientation from $O^{\rm asd}(\Omega,w)$ on the left and the complex orientation on the right.

L1 (in the text after Proposition 5.2, which is quoted in §11.3 of this note [corrected by checker: the note had "§10.1"]) remarks that at level zero this "followed trivially from the definition of a geometric representative … because the link of $M_{\mathfrak s}\subset\mathcal M_{\mathfrak t}/S^1$ is a smooth, compact manifold without boundary".

## 7. The level-zero link pairing and the top-level cobordism

### 7.1 FL2b, Theorem 4.13 (`thm:DegreeZeroFormula`)

> Let $X$ be a four-manifold with $\alpha\smile\alpha'=0$ for every $\alpha,\alpha'\in H^1(X;\mathbb Z)$, and let $\Omega$ be a homology orientation. Let $\mathfrak s$ and $\mathfrak t$ be a spin$^c$ and spin$^u$ structure on $X$ for which $\mathfrak t=\mathfrak s\oplus\mathfrak s\otimes L$, and assume $M_{\mathfrak s}$ contains no zero-section pairs. Give $\mathbf L_{\mathfrak t,\mathfrak s}$ the complex orientation, determined by the orientation for $M_{\mathfrak s}$ fixed by $\Omega$ … Let $z\in\mathbb A(X)$ and let $\delta_c$ be a non-negative integer satisfying $\deg(z)+2\delta_c=\dim(\mathcal M^{*,0}_{\mathfrak t}/S^1)-1$. If $z=z'Y$ for some $Y\in H_3(X;\mathbb Z)$ and $z'\in\mathbb A(X)$, then $\langle\mu_p(z)\smile\mu_c^{\delta_c},[\mathbf L_{\mathfrak t,\mathfrak s}]\rangle=0$ (4.28). If $z=x^{\delta_0}\vartheta h^{\delta_2}$, where $h\in H_2(X;\mathbb R)$, $\vartheta\in\Lambda^{\delta_1}(H_1(X;\mathbb R))$, and $x\in H_0(X;\mathbb Z)$ is the positive generator, then $d_s(\mathfrak s)\equiv\delta_1\pmod2$ and if we set $2d=d_s(\mathfrak s)-\delta_1$ (4.29), then
> $$\langle\mu_p(z)\smile\mu_c^{\delta_c},[\mathbf L_{\mathfrak t,\mathfrak s}]\rangle=(-1)^{\delta_0+\delta_1}2^{-\delta_2-2\delta_0}C_{\chi,\sigma}(\deg(z),\delta_c,d_a(\mathfrak t),d_s(\mathfrak s),\delta_1)\,\langle\mu_{\mathfrak s}(x^d\vartheta),[M_{\mathfrak s}]\rangle\,\langle c_1(\mathfrak s)-c_1(\mathfrak t),h\rangle^{\delta_2},\tag{4.30}$$
> where $C_{\chi,\sigma}(\dots)=(-2)^dP^{a,b}_d(0)$ for $a=\delta_c-d-1$ and $b=\frac12(\deg(z)-d_a(\mathfrak t)-d_s(\mathfrak s))-\frac14(\chi+\sigma)$. If $d=0$, then $C_{\chi,\sigma}=1$.

$P^{a,b}_n$ is the Jacobi polynomial (FL2b eq. `defn:JacobiPolyn` (4.27)).

**Proof mechanism [gloss].** The pairing is $\langle\boldsymbol\gamma^*\mu_p(z)\,\nu^{\delta_c}\,\nu^{r_\Xi},[\mathbb PN]\rangle$ by Lemmas 4.8 and 4.9. Corollary 4.7 expresses $\boldsymbol\gamma^*\mu_p(z)$ in $\nu$ and $\mu_{\mathfrak s}$, and Lemmas 4.10–4.11 push the result down to $M_{\mathfrak s}$.

**Remark 4.15** (`rmk:LevelZeroMultConj`): the proof shows that FKLM Conjecture 3.1 (the "multiplicity conjecture") holds for level-zero reducibles "even without the assumption that $\alpha\smile\alpha'=0$".

### 7.2 FL2b, Theorem 3.33 (`thm:CompactReductionFormula`): the cobordism when all reducibles are in the top level

> Let $\mathfrak t$ be a spin$^u$ structure on an oriented, smooth four-manifold $X$ with $b_2^+(X)>0$ and $w_2(\mathfrak t)\equiv w\pmod2$, for $w\in H^2(X;\mathbb Z)$. Assume that $w\pmod2$ is good. Suppose $z\in\mathbb A(X)$ has degree $d_a(\mathfrak t)\le\deg(z)\le d_a(\mathfrak t)+2n_a(\mathfrak t)-2$, and is intersection-suitable. Assume that the set of isomorphism classes of spin$^c$ structures, $\mathfrak s\in\mathrm{Spin}^c(X)$, defining reducible PU(2) monopoles in $\bar{\mathcal M}_{\mathfrak t}$ all obey condition (3.63), and so non-empty Seiberg–Witten moduli strata $\iota(M_{\mathfrak s})$ appear only in the top level, $\mathcal M_{\mathfrak t}$.
> **(a)** If for all $\mathfrak s$ with $M_{\mathfrak s}$ non-empty we have $(c_1(\mathfrak t)-c_1(\mathfrak s))^2<p_1(\mathfrak t)$, so $\bar{\mathcal M}_{\mathfrak t}$ contains no reducible monopoles, then $\#(\bar{\mathcal V}(z)\cap\bar M^w_\kappa(X))=0$.
> **(b)** If $\deg(z)=d_a$ and $o_{\mathfrak t}(w,\mathfrak s)=\frac14(w-c_1(\mathfrak t)+c_1(\mathfrak s))^2$, then
> $$\#(\bar{\mathcal V}(z)\cap\bar M^w_\kappa(X))=-2^{1-n_a}\sum_{\{\mathfrak s:\ \mathfrak s\oplus\mathfrak s'=\mathfrak t\}}(-1)^{o_{\mathfrak t}(w,\mathfrak s)}\langle\mu_p(z)\smile\mu_c^{n_a-1},[\mathbf L_{\mathfrak t,\mathfrak s}]\rangle,\tag{3.70}$$
> where the class $[\mathbf L_{\mathfrak t,\mathfrak s}]$ is defined by the complex orientation.
> **(c)** If $d_a<\deg(z)\le d_a+2n_a-2$ and $\delta_c\in\mathbb N$ is defined by $\deg(z)+2\delta_c=d_a+2n_a-2$, then $\sum_{\mathfrak s}(-1)^{o_{\mathfrak t}(w,\mathfrak s)}\langle\mu_p(z)\smile\mu_c^{\delta_c},[\mathbf L_{\mathfrak t,\mathfrak s}]\rangle=0$ (3.71).

**Role.** This is the cobordism with no gluing at all. Its key hypothesis is that every reducible in $\bar{\mathcal M}_{\mathfrak t}$ lies in the top level. FL2b Corollary 3.35 (`cor:CompactReductionFormula`) relaxes this to "SW moduli spaces with non-trivial SW functions appear only in the top level", conditionally on Conjecture 3.34 (`conj:Multiplicity` = FKLM Conjecture 3.1). In the text after Conjecture 3.34, FL2b says: "The difficulty lies in the appropriate construction of the link $\mathbf L_{\mathfrak t,\mathfrak s}$ of a Seiberg–Witten moduli space when $\ell=\ell(\mathfrak t,\mathfrak s)>0$." [added by checker] The same passage continues: "We show that Conjecture 3.34 holds when $\ell=0$ in Theorem 4.13 and when $\ell=1$ in [FLLevelOne]. By adapting Leness's proof of the wall-crossing formula in [LenessWC], we can also see that the conjecture holds when $\ell=2$." The $\ell=1$ case rests on L1 Theorem 3.8 (§9). The $\ell=2$ claim has no proof in any source read here. For general $\ell$ the conjecture becomes Memoir Theorem 10.1.2, conditional on Hypothesis 7.8.1 (`a-cobordism.md` §6.2). The Overlap paper's Theorem 2.1 (`conj:PTConj`) is the general-$\ell$ link pairing formula. It opens with "Assume the result of Theorem 4.2", that is, the unproved extended gluing theorem.

---

# Part III. Seiberg–Witten strata in the first level ($\ell=1$): L1 (math/0106238)

**Notation of L1, §3.** Here $\mathfrak t$ is the *background* spin$^u$ structure, with $M_{\mathfrak s}\subset\mathcal M_{\mathfrak t}$. The structure $\mathfrak t'=(\rho,V')$ is the spliced spin$^u$ structure $V'=(V|_{X\setminus\{x_0\}})\#(\mathbb V|_{S^4\setminus\{s\}})$ (eq. `eq:SplicedSpinu` (3.38)), with $\mathbb V$ of charge one over $S^4$. So $p_1(\mathfrak t')=p_1(\mathfrak t)-4$, $\ell(\mathfrak t',\mathfrak s)=1$, and the stratum is $M_{\mathfrak s}\times X\subset\bar{\mathcal M}_{\mathfrak t'}$. In Memoir notation, $\mathfrak t'$ is $\mathfrak t$ and $\mathfrak t$ is $\mathfrak t(1)$. $N_{\mathfrak t,\mathfrak s}\to M_{\mathfrak s}$ and $\Xi_{\mathfrak t,\mathfrak s}$ are the bundles of §5 (FL2a Theorem 3.21) for the background $\mathfrak t$.

## 8. Gluing data, virtual moduli space, obstruction bundle

* **Gluing data** (eqs. (3.51), (3.54)): $\mathrm{Gl}_{\mathfrak t}(\delta)=\big(\mathrm{Fr}(\mathfrak g_V)\times_X\mathrm{Fr}(T^*X)\times M_1^{s,\natural}(S^4,\delta)\big)/(\mathrm{SO}(3)\times\mathrm{SO}(4))$. Its cone completion $\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)$ satisfies $\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)-\mathrm{Gl}_{\mathfrak t}(\delta)=X$. The fibre $M_1^{s,\natural}(S^4,\delta)$ consists of framed, mass-centred charge-one instantons with scale in $(0,\delta]$. It satisfies $M^{s,\natural}_1(S^4,\delta)\cong(0,\delta]\times\mathrm{SO}(3)$ (eq. `eq:1InstModIsScaleFrame` (3.23)), and its Uhlenbeck closure is a cone $c(\mathrm{SO}(3))$ (eq. `eq:UhlenbeckInstantonConeHomeo` (3.24)).
* **Virtual moduli space** (eqs. `eq:TopStratumOfSplicingDomain` (3.53), `eq:UhlenbeckCompactifiedSplicingDomain` (3.55)): $\mathcal M^{\rm stab}_{\mathfrak t',\mathfrak s}=\tilde N_{\mathfrak t,\mathfrak s}(\varepsilon)\times_{\mathcal G_{\mathfrak s}}\mathrm{Gl}_{\mathfrak t}(\delta)$ and $\bar{\mathcal M}^{\rm stab}_{\mathfrak t',\mathfrak s}=\tilde N_{\mathfrak t,\mathfrak s}(\varepsilon)\times_{\mathcal G_{\mathfrak s}}\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)$. The splicing map is $\boldsymbol\gamma':\mathcal M^{\rm stab}_{\mathfrak t',\mathfrak s}\to\mathcal C_{\mathfrak t'}$ (3.52). "It can be shown [FL3, FL4] that $\boldsymbol\gamma'$ is a smooth embedding, provided $\varepsilon$ and $\delta$ are sufficiently small."
* **Stratification** (eq. `eq:ModelStratification` (3.70)):
$$\bar{\mathcal M}^{\rm stab}_{\mathfrak t',\mathfrak s}=\tilde N_{\mathfrak t,\mathfrak s}(\varepsilon)\times_{\mathcal G_{\mathfrak s}}\mathrm{Gl}_{\mathfrak t}(\delta)\ \sqcup\ (N_{\mathfrak t,\mathfrak s}(\varepsilon)-M_{\mathfrak s})\times X\ \sqcup\ M_{\mathfrak s}\times X.$$
The strata have dimensions $2r_N+d_s+8$, $2r_N+d_s+4$ and $d_s+4$.
* **L1, Lemma 3.6** (`lem:S1EquivarianceSplicing`): the actions "(1) (2.37) on $\tilde N$ and trivial on $\bar{\mathrm{Gl}}$" and "(2) diagonal with weight two on the fibers of $\tilde N$ and with weight two on $\bar{\mathrm{Gl}}$" are equivalent. "The extended splicing and gluing maps … are circle-equivariant."
* **Obstruction bundle** (eq. `eq:ObstructionDirecSumDecomposition` (3.61)): $\Upsilon_{[(B,\Psi,\eta),\mathbf g]}\cong\Upsilon^s_{[B,\Psi,\eta]}\oplus\Upsilon^i_{[\mathbf A]}$.
  * **Background part** (eq. `eq:ExtendedBackgroundObstruction` (3.64)): $\bar\Upsilon^s_{\mathfrak t',\mathfrak s}\cong\mathbb C^{r_\Xi}\times\tilde N_{\mathfrak t,\mathfrak s}(\varepsilon)\times_{\mathcal G_{\mathfrak s}}\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)$. This is the pull-back of $\pi_N^*\Xi_{\mathfrak t,\mathfrak s}$ ("In [FL3], the Seiberg–Witten component … was identified with the subbundle constructed in [FL2a, §3.5.2]").
  * **Instanton part** (eq. `eq:DefnInstantonObstruction` (3.68)): $\Upsilon^i_{\mathfrak t',\mathfrak s}=\tilde N_{\mathfrak t,\mathfrak s}\times_{\mathcal G_{\mathfrak s}}\mathrm{Fr}_{\mathbb{C}\ell(T^*X)}(V)\times_{\mathrm{Spin}^u(4)}\operatorname{Coker}\mathbf D_{\mathbb V}$. Here $\operatorname{Coker}\mathbf D_{\mathbb V}\to M^{s,\natural}_1(S^4,\delta)$ is the complex line bundle with fibres $\operatorname{Coker}D_{\mathbf A}$ ("$\operatorname{Ker}D_{\mathbf A}=\{0\}$ and as $\operatorname{Ind}_{\mathbb C}D_{\mathbf A}=-1$", eq. (3.65)). It is "non-trivial, but torsion" (eq. (3.66)).
* **L1, Lemma 3.7** (`lem:InstantonObstructionSplicingDomain`): $\tilde{\boldsymbol\varphi}_i$ descends to an embedding of $S^1$-equivariant vector bundles $\Upsilon^i_{\mathfrak t',\mathfrak s}\to\mathfrak V_{\mathfrak t'}$ covering $\boldsymbol\gamma'$.

## 9. L1, Theorem 3.8 (`thm:GluingThm`): the gluing input, and its status

> **Theorem 3.8** [FL3, FL4]. For small enough positive $\varepsilon$ and $\delta$, there is a topological embedding,
> $$\boldsymbol\gamma:\bar{\mathcal M}^{\rm stab}_{\mathfrak t',\mathfrak s}\to\bar{\mathcal C}_{\mathfrak t'}=\mathcal C_{\mathfrak t'}\sqcup(\mathcal C_{\mathfrak t}-M_{\mathfrak s})\times X\sqcup M_{\mathfrak s}\times X,\tag{3.71}$$
> restricting to a smooth embedding of the top stratum of (3.70) into $\mathcal C^{*,0}_{\mathfrak t'}$, the smooth embedding $\boldsymbol\gamma_{\mathfrak t,\mathfrak s}\times\mathrm{id}_X$ of the middle stratum into $\mathcal C^{*,0}_{\mathfrak t}\times X$, and the identity map on the lowest stratum, $M_{\mathfrak s}\times X\subset\mathcal C^0_{\mathfrak t}\times X$. There is a smooth, circle-equivariant section $\boldsymbol\chi_i$ of the instanton obstruction bundle (3.68), $\Upsilon^i_{\mathfrak t',\mathfrak s}\to\mathcal M^{\rm stab}_{\mathfrak t',\mathfrak s}$, and a continuous, circle-equivariant section $\boldsymbol\chi_s$ of the background obstruction bundle (3.64), $\bar\Upsilon^s_{\mathfrak t',\mathfrak s}\to\bar{\mathcal M}^{\rm stab}_{\mathfrak t',\mathfrak s}$, which is smooth when restricted to each stratum … such that, if $\boldsymbol\chi=\boldsymbol\chi_s\oplus\boldsymbol\chi_i$, then
> $$\boldsymbol\gamma(\mathcal M^{\rm stab}_{\mathfrak t',\mathfrak s}\cap\boldsymbol\chi^{-1}(0))=\boldsymbol\gamma(\mathcal M^{\rm stab}_{\mathfrak t',\mathfrak s})\cap\mathcal M_{\mathfrak t'},$$
> and
> $$\boldsymbol\gamma\big(((N_{\mathfrak t,\mathfrak s}(\varepsilon)-M_{\mathfrak s})\times X)\cap\boldsymbol\chi_s^{-1}(0)\big)=\boldsymbol\gamma((N_{\mathfrak t,\mathfrak s}(\varepsilon)-M_{\mathfrak s})\times X)\cap\bar{\mathcal M}_{\mathfrak t'}.$$
> The sections $\boldsymbol\chi_s\oplus\boldsymbol\chi_i$ and $\boldsymbol\chi_s$ of the vector bundles $\bar\Upsilon^s_{\mathfrak t',\mathfrak s}\oplus\Upsilon^i_{\mathfrak t',\mathfrak s}\to\mathcal M^{\rm stab}_{\mathfrak t',\mathfrak s}$ and $\bar\Upsilon^s_{\mathfrak t',\mathfrak s}\to(N_{\mathfrak t,\mathfrak s}-M_{\mathfrak s})\times X$, respectively, vanish transversely.

After the theorem: "We shall formally extend the section $\boldsymbol\chi_i$ over the lower strata … by setting it equal to zero on the lower strata. … we make no assumptions about the continuity or transversality of this formal extension".

**Status (from the sources).**
* L1 gives no proof; the theorem is attributed to "[FL3, FL4]".
* L1's bibliography lists FL4 as "PU(2) monopoles. IV: Surjectivity of gluing maps, in preparation". The L1 introduction says: "At the time of writing, work on [FL4] and [FL5] is still in progress".
* FL3 Theorem 1.1 (`thm:GluingTheorem1`) proves only the existence half. It gives $\boldsymbol\gamma_{\mu,\Sigma}(\boldsymbol\chi^{-1}_{\mu,\Sigma}(0))\subset M^{*,0}(\mathfrak t)$, on a precompact $\mathcal U_{\ell,\mu}$ in a thickened space defined by a small-eigenvalue cut-off $\mu$. FL3 §1.5.1 says this is "at most the first half of a desired 'gluing theorem'". It lists as missing: continuity on the Uhlenbeck closure, the embedding property, and surjectivity ("the image … is an open subset of $\bar M(\mathfrak t)$ and the space $\bar M(\mathfrak t)$ has a finite covering by such open subsets"). These are "proved in [FL4]".
* FL3 Problem 1.5 (`prob:SpectralFlow`): "If $\dim M^{\rm sw}_{\mathfrak s}>0$, one cannot necessarily fix a single, uniform positive upper bound $\mu$ for the small eigenvalues of $d^1_{A,\Phi}d^{1,*}_{A,\Phi}$, due to spectral flow".
* Memoir §7.9 says FL3's method "does not apply without significant modification" near positive-dimensional $M_{\mathfrak s}$. It replaces the small-eigenvalue bundle by $\Xi=\Xi_1\oplus\Xi_2$, with $\Xi_1$ the FL2a stabilizing bundle and $\Xi_2=\operatorname{Coker}\mathbf D$ over the $S^4$ factors.

So: **every statement about level-one links in L1 rests on L1 Theorem 3.8, whose surjectivity, Uhlenbeck-continuity and embedding parts are not proved in any source read here.** The introduction to L1 §5 says which property is used where:
* "$\boldsymbol\gamma$ is a homeomorphism … ensures that the image … contains an open neighborhood of $\bar{\mathcal V}(z)\cap\bar{\mathcal W}\cap\bar{\mathbf L}_{\mathfrak t',\mathfrak s}$";
* smoothness and orientation-preservation on the top stratum is used for transversality and orientations;
* "continuity of $\boldsymbol\gamma$ on $\bar{\mathcal M}^{\rm stab}$" is used for cocycle extensions;
* transversality of $\boldsymbol\chi$ is used in Lemma 5.9;
* continuity of $\boldsymbol\chi_s$ is used in Lemmas 5.17, 5.18.

## 10. The level-one virtual link and link

### 10.1 Definitions (L1 §3.6, `subsec:DefnOfLink`) [corrected by checker: `subsec:DefnOfLink` is L1 §3.8. Section 3 of L1 has subsections 3.1 Clifford modules, 3.2 structure groups, 3.3 connections over $S^4$, 3.4 splicing, 3.5 gluing data and splicing map, 3.6 obstruction bundle, 3.7 construction of the gluing map (containing Theorem 3.8), 3.8 link of a level-one SW stratum, 3.9 orientations.]

* SW and instanton components of the *virtual link* (eq. `eq:DefineSWandInstantonModelThickLink` (3.72)):
$$\bar{\mathbf L}^{{\rm stab},s}_{\mathfrak t',\mathfrak s}=\big(\partial\tilde N_{\mathfrak t,\mathfrak s}(\varepsilon)\times_{\mathcal G_{\mathfrak s}}\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)\big)/S^1,\qquad\mathbf L^{{\rm stab},i}_{\mathfrak t',\mathfrak s}=\big(\tilde N_{\mathfrak t,\mathfrak s}(\varepsilon)\times_{\mathcal G_{\mathfrak s}}\partial\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)\big)/S^1,$$
with $\partial\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)=\big(\mathrm{Fr}(\mathfrak g_V)\times_X\mathrm{Fr}(T^*X)\times\lambda^{-1}(\delta)\cap M_1^{s,\natural}(S^4)\big)/(\mathrm{SO}(3)\times\mathrm{SO}(4))$ (eq. (3.73)), where $\lambda$ is the scale.
* $\bar{\mathbf L}^{\rm stab}_{\mathfrak t',\mathfrak s}=\bar{\mathbf L}^{{\rm stab},s}\cup\mathbf L^{{\rm stab},i}$ (eq. (3.74)). Its top stratum $\mathbf L^{\rm stab}_{\mathfrak t',\mathfrak s}$ "is only a topological and not a smooth manifold because of the 'edge'" $\mathbf L^{{\rm stab},i}\cap\mathbf L^{{\rm stab},s}$ (eq. (3.76)).
* Lower part (eq. `eq:DefineLSing` (3.77)): $\mathbf L^{\rm sing}_{\mathfrak t',\mathfrak s}=\partial N_{\mathfrak t,\mathfrak s}(\varepsilon)/S^1\times X$, "a closed, smooth manifold" when $\ell=1$.
* **The link** (eq. `eq:DefineLink` (3.79)):
$$\bar{\mathbf L}_{\mathfrak t',\mathfrak s}=\boldsymbol\gamma\big(\boldsymbol\chi^{-1}(0)\cap\bar{\mathbf L}^{\rm stab}_{\mathfrak t',\mathfrak s}\big),\qquad\mathbf L_{\mathfrak t',\mathfrak s}=\bar{\mathbf L}_{\mathfrak t',\mathfrak s}\cap\mathcal M^{*,0}_{\mathfrak t'}/S^1.$$
* **Disk-bundle structure** (eqs. (3.82), (3.83)):
$$\mathbf L^{{\rm stab},i}_{\mathfrak t',\mathfrak s}=\tilde N_{\mathfrak t,\mathfrak s}(\varepsilon)\times_{\mathcal G_{\mathfrak s}\times S^1}\partial\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)\to\mathbf{BL}^{{\rm stab},i}_{\mathfrak t',\mathfrak s}:=\tilde M_{\mathfrak s}\times_{\mathcal G_{\mathfrak s}}\partial\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)/S^1\cong M_{\mathfrak s}\times\partial\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)/S^1.$$
This is a complex disk bundle with fibre a fibre of $N_{\mathfrak t,\mathfrak s}(\varepsilon)$.

The L1 introduction (§1.6.1) says: "We define a *virtual link*, $\bar{\mathbf L}^{\rm stab}_{\mathfrak t,\mathfrak s}$, as the boundary of the domain [$N_{\mathfrak t_1,\mathfrak s}(\varepsilon)\times_{S^1}\bar{\mathrm{Gl}}_{\mathfrak t_1}(\delta)$]."

### 10.2 L1, Lemma 3.9 (`lem:GRIntersect0`)

> Assume $w\in H^2(X;\mathbb Z)$ is such that $w\pmod2$ is good … Given a Riemannian metric on $X$ and a pair $(\mathfrak t',\mathfrak s)$ with $\ell(\mathfrak t',\mathfrak s)=1$ and $w_2(\mathfrak t')\equiv w\pmod2$, there are positive constants $\varepsilon_0$ and $\delta_0$ such that the following hold for all generic choices of $\varepsilon\le\varepsilon_0$ and $\delta\le\delta_0$ defining $\bar{\mathbf L}^{\rm stab}_{\mathfrak t',\mathfrak s}$.
> * The link $\bar{\mathbf L}_{\mathfrak t',\mathfrak s}$ is disjoint from $\bar M^w_\kappa$ and $\bar{\mathcal M}^{\rm red}_{\mathfrak t'}$ in the stratification … of $\bar{\mathcal M}_{\mathfrak t'}/S^1$.
> * For all $z\in\mathbb A(X)$, the intersection $\bar{\mathcal V}(z)\cap\bar{\mathcal W}^\eta\cap\bar{\mathbf L}_{\mathfrak t',\mathfrak s}$ is contained in the top stratum $\mathbf L_{\mathfrak t',\mathfrak s}$ … and is disjoint from the image of the edge (3.76) under the gluing map $\boldsymbol\gamma$.

[added by checker] Status: the lemma is about $\bar{\mathbf L}_{\mathfrak t',\mathfrak s}=\boldsymbol\gamma(\boldsymbol\chi^{-1}(0)\cap\bar{\mathbf L}^{\rm stab})$, so it presupposes L1 Theorem 3.8. Its proof places the intersection in the top stratum by citing FL2b Corollary 3.18, which needs $z$ intersection-suitable (see §3.7); the statement "for all $z\in\mathbb A(X)$" drops that hypothesis. The proof also uses $\eta$ without stating the dimension condition it must satisfy.

After the proof: "the construction of the link in this section applies to links $\bar{\mathbf L}_{\mathfrak t',\mathfrak s}$ of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ when $\ell(\mathfrak t',\mathfrak s)>1$. The main difference is that the additional dilation parameters … result in more complicated 'edges' …". This is a remark, not a theorem.

### 10.3 Orientation: L1 Definitions 3.11–3.12, Lemmas 3.13–3.14

The *standard orientation* of $\mathbf L_{\mathfrak t',\mathfrak s}$ (Definition 3.12, `defn:StdOrnLink`) is built from three pieces: the standard orientation of $\mathbf L^{{\rm stab},i}$ (Definition 3.11), the complex orientation of the normal bundle of $\boldsymbol\chi^{-1}(0)\cap\mathbf L^{{\rm stab},i}$, and the diffeomorphism $\boldsymbol\gamma$ on the zero locus.

**Lemma 3.14** (`lem:OrientationFactor`): if $\mathfrak t=\mathfrak s\oplus\mathfrak s\otimes L$, the standard orientation and the boundary orientation from $O^{\rm asd}(\Omega,w)$ differ by $(-1)^{o_{\mathfrak t'}(w,\mathfrak s)}$, $o_{\mathfrak t'}(w,\mathfrak s)=\frac14(w-c_1(L))^2$ (eq. (3.91)). The Memoir restates this for all $\ell$ as Lemma 8.1.7 (`lem:OrientationFactor`).

## 11. Classes and Euler classes on the level-one virtual link

### 11.1 L1, Definition 4.1 (`defn:DefnOfNu`) and Lemma 4.2 (`lem:PullbackMuc1`)

> **Definition 4.1.** Let $\nu$ be the first Chern class of the circle bundle $\bar{\mathcal M}^{{\rm stab},*}_{\mathfrak t',\mathfrak s}\to\bar{\mathcal M}^{{\rm stab},*}_{\mathfrak t',\mathfrak s}/S^1$, where the circle acts diagonally on $\bar{\mathcal M}^{\rm stab}_{\mathfrak t',\mathfrak s}$, acting on $\tilde N_{\mathfrak t,\mathfrak s}(\varepsilon)$ by scalar multiplication on the fibers and on $\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)$ by the action described before equation (3.56).

> **Lemma 4.2.** $\boldsymbol\gamma^*\mu_c=-\iota^*\nu$.

**[gloss]** The sign convention is opposite to FL2b Definition 4.3: FL2b's $\nu$ is minus $c_1$ of the circle bundle, L1's is plus. Then FL2b's $\boldsymbol\gamma^*\mu_c=\nu$ and $e=\nu^{r_\Xi}$ correspond to L1's $-\nu$ and $(-\nu)^{r_\Xi}$.

### 11.1a L1, Lemma 4.10 (`lem:CohomologyOnReducibleLink`) and Lemma 5.23 (`lem:CompareNu`) [added by checker]

These are the level-one counterparts of FL2b Corollary 4.7, and the note omitted them.

> **Lemma 4.10.** Continue the hypotheses of Lemma 4.3. Let $\iota$ be the inclusion (`eq:AnInclusionUsedToExtendCohomClasses`), let $x\in H_0(X;\mathbb Z)$ be the positive generator, and let $h\in H_2(X;\mathbb R)$. Let $\nu,\pi_{\mathfrak s}^*\mu_{\mathfrak s}\in H^2(\bar{\mathcal M}^{{\rm stab},*}_{\mathfrak t',\mathfrak s}/S^1;\mathbb Z)$ be the classes given by Definition 4.1 and (`eq:SWClass`). Then, on $\mathcal M^{\rm stab}_{\mathfrak t',\mathfrak s}/S^1$,
> $$\mu_p(x)=-\tfrac14\iota^*(2\pi_{\mathfrak s}^*\mu_{\mathfrak s}-\nu)^2+\iota^*\pi_X^*\mathrm{PD}[x],\qquad\mu_p(h)=\tfrac12\iota^*\langle c_1(\mathfrak s)-c_1(\mathfrak t),h\rangle(2\pi_{\mathfrak s}^*\mu_{\mathfrak s}-\nu)+\iota^*\pi_X^*\mathrm{PD}[h].\tag{4.24}$$

Compared with FL2b (4.19), there are new terms $\pi_X^*\mathrm{PD}[\beta]$ from the bubble point $x\in X$, and the sign of $\nu$ is reversed (the convention of §11.1). The text after the proof says the results "will extend (with appropriate modifications, though these do not cause undue difficulty)" to $\ell>1$, with the diagonal replaced by the incidence set $\{(\mathbf x,x):x\in|\mathbf x|\}$. That is an assertion, not a proof.

> **Lemma 5.23.** Let $\nu,\nu_{\mathfrak t}$ be the first Chern classes in Definitions 4.1 and 5.22. … Then the restriction of $\nu$ to $M_{\mathfrak s}\times\partial\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)/S^1$ is given by $\nu|=\nu_{\mathfrak t}+2c_1(\mathbb L_{\mathfrak s})$ (5.73), and if $b_1(X)=0$, this simplifies to $\nu|=\nu_{\mathfrak t}+2\mu_{\mathfrak s}$.

This is the Künneth splitting that, together with Lemma 5.24, reduces the pairing on $\mathbf{BL}^{{\rm stab},i}\cong M_{\mathfrak s}\times\partial\bar{\mathrm{Gl}}/S^1$ to SW pairings times instanton-link pairings.

### 11.2 L1, Lemma 4.11 (`lem:EulerOfBackgroundObstruction`) and Lemma 4.12 (`lem:InstantonEuler`)

> **Lemma 4.11.** Continue the hypotheses of Lemma 4.3. Let $\nu$ be the class in Definition 4.1. Let $\bar\Upsilon^s_{\mathfrak t',\mathfrak s}/S^1\to\bar{\mathcal M}^{{\rm stab},*}_{\mathfrak t',\mathfrak s}/S^1$ be the extended Seiberg–Witten obstruction bundle (3.64), and let $r_\Xi$ denote its complex rank. Then
> $$e(\bar\Upsilon^s_{\mathfrak t',\mathfrak s}/S^1)=(-\nu)^{r_\Xi}\in H^{2r_\Xi}(\bar{\mathcal M}^{{\rm stab},*}_{\mathfrak t',\mathfrak s}/S^1;\mathbb Z).\tag{4.25}$$

> **Lemma 4.12.** Let $\nu$ be the class in Definition 4.1. Then the Euler class of the instanton obstruction bundle, $\Upsilon^i_{\mathfrak t',\mathfrak s}/S^1\to\mathcal M^{\rm stab}_{\mathfrak t',\mathfrak s}/S^1$ defined in (3.68), is given as an element of rational cohomology by
> $$e(\Upsilon^i_{\mathfrak t',\mathfrak s}/S^1)=\tfrac12\big(\pi_X^*c_1(\mathfrak t)-\nu\big)\in H^2(\mathcal M^{\rm stab}_{\mathfrak t',\mathfrak s}/S^1;\mathbb Q).\tag{4.28}$$

The proof computes the Euler class of the tensor square, using $(\operatorname{Coker}\mathbf D)^{\otimes2}\cong\mathrm{SO}(3)\times\mathbb C$. The text before the lemma says: "more work is required to extend this calculation to the case $\ell(\mathfrak t',\mathfrak s)>1$." L1 §1.7.1 ("Level two") says that for level two one would need to "compute the Euler class of the instanton obstruction bundle for the level-two case … the description of the cokernel of the twisted Dirac operator [DK, Lemma 3.3.28] might provide a useful starting point".

### 11.3 L1, Proposition 5.2 (`prop:IntersectionNoToCupProduct`): duality

> Assume $w\in H^2(X;\mathbb Z)$ is such that $w\pmod2$ is good … Suppose $(\mathfrak t',\mathfrak s)$ is a pair with $\ell(\mathfrak t',\mathfrak s)=1$ and $w_2(\mathfrak t')\equiv w\pmod2$. Let $[\bar{\mathbf L}^{\rm stab}_{\mathfrak t',\mathfrak s}]\in H_{\max}(\bar{\mathbf L}^{\rm stab}_{\mathfrak t',\mathfrak s};\mathbb Z)$ be the homology class defined in (5.9) [`eq:DefineFundClassOfL`]. Let $z\in\mathbb A(X)$ and $\eta\in\mathbb N$ satisfy $\deg(z)+2(\eta+1)=\dim\mathcal M_{\mathfrak t'}$. Let $\bar\mu_p(z)$ and $\bar\mu_c$ be the extensions … Give $\mathbf L_{\mathfrak t',\mathfrak s}$ the standard orientation … Then,
> $$\#(\bar{\mathcal V}(z)\cap\bar{\mathcal W}^\eta\cap\bar{\mathbf L}_{\mathfrak t',\mathfrak s})=\langle\bar\mu_p(z)\smile\bar\mu_c^\eta\smile\bar e,[\bar{\mathbf L}^{\rm stab}_{\mathfrak t',\mathfrak s}]\rangle,\tag{5.2}$$
> where $\bar e=\bar e_s\smile\bar e_i$ (Definition 5.1, `defn:ExtendedEulerClasses`) is the extension of the Euler classes of Lemmas 4.11 and 4.12.

L1 §1.6.2 says: "The proofs given in §5.1 are specific to the topology of the case $\ell=1$, but the results should hold for all $\ell>0$."

### 11.4 L1, Proposition 5.21 (`prop:LinkSegreFormula`)

> Let $d_s=\dim M_{\mathfrak s}$ and let $r_N$ denote the rank of the complex vector bundle $N_{\mathfrak t,\mathfrak s}$ over $M_{\mathfrak s}$. Assume $b_1(X)=0$ and $b_2^+(X)$ is odd. For integers $0\le i\le d=\frac12d_s$ and $0\le k\le2$ and any class $\alpha\in H^{2k}(X;\mathbb Z)$, we have
> $$\big\langle\nu^{d+r_N+3-k-i}\smile\pi_{\mathfrak s}^*\mu_{\mathfrak s}^i\smile\pi_X^*\alpha,[\bar{\mathbf L}^{\rm stab}_{\mathfrak t',\mathfrak s}]\big\rangle=\sum_{j=0}^{d-i}(-1)^{r_N+j}\big\langle\nu^{d+3-i-j-k}\smile\pi_{\mathfrak s}^*(\mu^i_{\mathfrak s}\smile s_j(N_{\mathfrak t,\mathfrak s}))\smile\pi_X^*\alpha,[\mathbf{BL}^{{\rm stab},i}_{\mathfrak t',\mathfrak s}]\big\rangle.\tag{5.71}$$

It is proved from Proposition 5.20 (`prop:S1Localization`), a formula relating the equivariant Thom class of $N$ to Segre classes.

### 11.5 L1, Definition 5.22 (`defn:NuX`) and Lemma 5.24 (`lem:PairingsWithInstantonLink`): the instanton factor

> **Definition 5.22.** Let $\nu_{\mathfrak t}\in H^2(\partial\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)/S^1;\mathbb R)$ be the first Chern class of the circle bundle $\partial\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)\to\partial\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)/S^1$ …

> **Lemma 5.24.** Let $\nu_{\mathfrak t}$ be the characteristic class in Definition 5.22. Let $\partial\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)/S^1$ have the standard orientation … If $x\in H_0(X;\mathbb Z)$ is the positive generator and $h\in H_2(X;\mathbb R)$, then
> $$\begin{aligned}\langle\nu_{\mathfrak t}\smile\pi_X^*\mathrm{PD}[x],[\partial\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)/S^1]\rangle&=2,\\\langle\nu_{\mathfrak t}^2\smile\pi_X^*\mathrm{PD}[h],[\partial\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)/S^1]\rangle&=-4\langle(c_1(\mathfrak s)-c_1(\mathfrak t))\smile\mathrm{PD}[h],[X]\rangle,\\\langle\nu_{\mathfrak t}^3,[\partial\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)/S^1]\rangle&=6(c_1(\mathfrak s)-c_1(\mathfrak t))^2+2c_1^2(X).\end{aligned}\tag{5.76}$$

**Proof (verbatim in substance).** "In [LenessWC, §3], a rank-two, Hermitian vector bundle, $F\to X'$, where $\pi:X'\to X$ is a finite-degree cover is constructed with $F\to\pi^*\mathrm{Gl}_{\mathfrak t}$ a branched cover of degree negative two. … This implies that the map on quotients, $\mathbb P(F)\to\pi^*\partial\bar{\mathrm{Gl}}_{\mathfrak t}(\delta)/S^1$, has degree negative one and that the class $\nu_{\mathfrak t}$ pulls back to $2h$ where $h$ is the first Chern class of the circle bundle $F/\mathbb R^*\to\mathbb P(F)$." The proof concludes by citing the Segre-class computation of [LenessWC]. [unconfirmed: the statement of Lemma 5.24 is quoted correctly from L1, but its proof consists of citations to LenessWC (dg-ga/9603016). That source is not among the downloaded files, so the three formulas (5.76), and the degree claims $-2$ and $-1$, could not be checked. Theorem 6.1 inherits this dependence.] **[gloss]** This is the only place in the sources where a level-$\ell$ instanton link component is compared with a projective bundle. The comparison is up to a finite cover and a degree $-1$ map, and the computation it relies on is in LenessWC (dg-ga/9603016), which is not among the downloaded sources. [corrected by checker: "the only place" is too strong as phrased; it is the only *explicit* such comparison, and only for $\ell=1$. Three further statements point to LenessWC at $\ell=2$, none with proof in the sources read. FL2b, after Conjecture 3.34: "By adapting Leness's proof of the wall-crossing formula in [LenessWC], we can also see that the conjecture holds when $\ell=2$". L1 §1.7.1 proposes replacing Lemma 5.24 by "the analogous results from [LenessWC] for the boundary of the level-two gluing-data". Memoir §1.2: "it should be possible to adapt the techniques of [LenessWC] to directly compute [the link pairing] for singularities of the form $M_{\mathfrak s}\times\mathrm{Sym}^2(X)$, [but] … direct calculations appear intractable when $\ell\ge3$", and the equivariant cohomology of the fibre "is carried out for the case $\ell=2$ in [LenessWC]".]

### 11.6 L1, Theorem 6.1 (`thm:LevelOne`): the level-one link pairing

> Let $X$ be a four-manifold with $b_1(X)=0$, odd $b_2^+(X)\ge1$. Suppose $X$ has a generic Riemannian metric and a spin$^u$ structure $\mathfrak t'$, where $w_2(\mathfrak t')$ is *good* in the sense of Definition 2.3. Let $\mathfrak s$ be a spin$^c$ structure over $X$ for which $(c_1(\mathfrak t')-c_1(\mathfrak s))^2=p_1(\mathfrak t')+4$. Let $\delta$, $m$, and $\eta$ be non-negative integers satisfying
> $$0\le m\le[\delta/2]\quad\text{and}\quad2(\delta+\eta)=\dim(\mathcal M_{\mathfrak t'}/S^1)-1.\tag{6.1}$$
> If $x\in H_0(X;\mathbb Z)$ is the positive generator, $h\in H_2(X;\mathbb R)$, and $\mathbf L_{\mathfrak t',\mathfrak s}$ has the standard orientation …, then
> $$\begin{aligned}\#\big(\bar{\mathcal V}(h^{\delta-2m}x^m)\cap\bar{\mathcal W}^\eta\cap\mathbf L_{\mathfrak t',\mathfrak s}\big)&=(-1)^{m+1+d_s(\mathfrak s)/2}2^{-\delta}2^{d_s(\mathfrak s)/2}P^{a,b}_{d_s(\mathfrak s)/2}(0)\langle\mu_{\mathfrak s}^{d_s(\mathfrak s)/2},[M_{\mathfrak s}]\rangle\Big(a_0\langle c_1(\mathfrak s)-c_1(\mathfrak t'),h\rangle^{\delta-2m}\\&\quad+b_0\langle c_1(\mathfrak s)-c_1(\mathfrak t'),h\rangle^{\delta-2m-1}\langle c_1(\mathfrak t'),h\rangle+a_1\langle c_1(\mathfrak s)-c_1(\mathfrak t'),h\rangle^{\delta-2m-2}Q_X(h,h)\Big),\end{aligned}\tag{6.2}$$
> where all terms on the right which would have a negative exponent are omitted,
> $$a_0=3(c_1(\mathfrak s)-c_1(\mathfrak t'))^2+c_1^2(X)+2(c_1(\mathfrak s)-c_1(\mathfrak t'))\cdot c_1(\mathfrak t')+4(\delta-2m)-4m,\quad b_0=2(\delta-2m)\frac{P^{a-1,b+1}_{d_s(\mathfrak s)/2}(0)}{P^{a,b}_{d_s(\mathfrak s)/2}(0)},\quad a_1=4\binom{\delta-2m}{2},$$
> and $P^{a,b}_{d_s(\mathfrak s)/2}(0)$ is the constant coefficient of the Jacobi polynomial … with $a=\eta-\frac12d_s(\mathfrak s)+1$ and $b=\frac12(2\delta-d_a(\mathfrak t')-d_s(\mathfrak s))-\frac14(\chi+\sigma)$. If $d_s(\mathfrak s)=0$, then $P^{a,b}_{d_s(\mathfrak s)/2}(0)=1$.

**Hypotheses.** Those printed, plus, implicitly, L1 Theorem 3.8 (§9) through the definition (3.79) of $\mathbf L_{\mathfrak t',\mathfrak s}$ and through Proposition 5.2. L1 §1.5 says the $b_0$ term "has no counterpart" in the ASD wall-crossing formulas: it comes from the obstruction $\operatorname{Coker}$ of the Dirac operator on $S^4$.

---

# Part IV. Seiberg–Witten strata at a general level $\ell\ge1$: the Memoir

**Notation.** For a partition $\mathcal P$ of $N_\ell=\{1,\dots,\ell\}$, $\Sigma(X^\ell,\mathcal P)$ is the corresponding stratum. The fibre of the local splicing data is
$$\bar M(\mathcal P)=\prod_{P\in\mathcal P}\bar M^{s,\natural}_{{\rm spl},|P|}(\delta)\qquad(\text{eq. `eq:DefineGluingDataFiber`}),$$
with $\bar M^{s,\natural}_{{\rm spl},\kappa}$ the framed, mass-centred *instanton moduli space with spliced ends* over $S^4$ (Memoir Chapter 5). The local data are $\bar{\mathrm{Gl}}(\mathfrak t,\mathfrak s,\mathcal P)=\mathrm{Fr}(\mathfrak t,\mathfrak s,\mathcal P)\times_{G(\mathcal P)}\bar M(\mathcal P)$ (eq. `eq:GluingData`). Set $\bar{\mathcal U}(\mathfrak t,\mathfrak s,\mathcal P)=\tilde N_{\mathfrak t(\ell),\mathfrak s}(\delta)\times_{\mathcal G_{\mathfrak s}}\mathcal O(\mathfrak t,\mathfrak s,\mathcal P)$ (eq. `eq:DefineUSet`). It has the projection $\pi(\mathfrak t,\mathfrak s,\mathcal P)$ to $N_{\mathfrak t(\ell),\mathfrak s}(\delta)\times\Sigma$ and the *tubular distance function* $\vec t(\mathfrak t,\mathfrak s,\mathcal P):\bar{\mathcal U}\to[0,1]^{\mathcal P}/\mathfrak S(\mathcal P)$, given on fibres by the scales $\prod_P\tilde\lambda_P$ (eq. `eq:DefineTubularDistanceFunction`). The bundles $N_{\mathfrak t(\ell),\mathfrak s}$ and $\Xi_{\mathfrak t(\ell),\mathfrak s}$ are those of §5 for $\mathfrak t(\ell)$.

## 12. Space of global splicing data (proved in the Memoir)

* **Theorem 6.6.1** (`thm:GlobalSplicingDataOverlaps`). Let $\mathfrak t$ be a spin$^u$ structure and $\mathfrak s$ a spin$^c$ structure with $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)\subset I\mathcal M_{\mathfrak t}$. For every partition $\mathcal P$ there is a neighbourhood $\mathcal O(\mathfrak t,\mathfrak s,\mathcal P)$ of $\Sigma(\mathfrak t,\mathfrak s,\mathcal P)$ in $\bar{\mathrm{Gl}}(\mathfrak t,\mathfrak s,\mathcal P)$ with the following properties. The images under the *crude* splicing maps $\boldsymbol\gamma''_{\mathfrak t,\mathfrak s,\mathcal P}$ of $N_{\mathfrak t(\ell),\mathfrak s}(\delta)\times_{\mathcal G_{\mathfrak s}}\mathcal O(\mathfrak t,\mathfrak s,\mathcal P)$ and of the same set for $\mathcal P'$ are disjoint unless the partitions are comparable. If $[\mathcal P<\mathcal P']\ne\emptyset$, the intersection is contained in the image of the overlap data under the downward map, and this equals its image under the upward map.
* **Global data** (eq. `eq:DefineGlobalGluingDataSpace`): $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}=\bigsqcup_{\mathcal P}(\tilde N_{\mathfrak t(\ell),\mathfrak s}(\delta)\times_{\mathcal G_{\mathfrak s}}\mathcal O(\mathfrak t,\mathfrak s,\mathcal P))/\!\sim$, where points are identified if their crude-splicing images coincide.
* **Corollary 6.6.5** (`cor:GlobalFibration`). There are an $S^1$-equivariant fibration $\pi_N:\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}\to N_{\mathfrak t(\ell),\mathfrak s}(\delta)$ and an $S^1$-equivariant embedding $\boldsymbol\gamma''_{\mathcal M}:\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}\to\bar{\mathcal C}_{\mathfrak t}$ restricting to $\boldsymbol\gamma''_{\mathfrak t,\mathfrak s,\mathcal P}$ on each piece.

These are proved (Memoir Chapters 3–6), and they are what the Memoir and the Overlap paper call the solution of the *overlap problem*. They concern splicing maps (crude, i.e. with metric and background flattened near the splicing points), not gluing maps. Memoir §1.2.1: "Because the SO(3)-monopole gluing maps defined in [FL3] only identify the zero locus of the obstruction section in $\mathrm{Gl}(\Sigma)$ with an open subspace of $\mathcal M_{\mathfrak t}$, the intersection of the images of $\mathrm{Gl}(\Sigma)$ and $\mathrm{Gl}(\Sigma')$ under the gluing map could be quite complicated …".

## 13. Obstruction pseudo-bundles and the gluing hypothesis

* **Definition 7.1.1** (`defn:PseudoBundle`, after Schwartz). Over a stratified $Y$ with strict deformation retractions $r_\Sigma:U_\Sigma\to\Sigma$, a pseudo-bundle is a map $\pi_\Upsilon:\Upsilon\to Y$ satisfying two conditions. Each $\Upsilon_\Sigma=\pi^{-1}_\Upsilon(\Sigma)$ is a vector bundle. There are fibrewise-linear injections $r_\Sigma^*\Upsilon_\Sigma\to\Upsilon|_{U_\Sigma}$ with surjective left inverses. The rank may jump between strata.
* The background pseudo-bundle $\bar\Upsilon^s_{\mathfrak t,\mathfrak s}$ is spliced from $\pi_N^*\Xi_{\mathfrak t(\ell),\mathfrak s}$, which is trivial of rank $r_\Xi$ (§7.3, eq. `eq:DefineBackgroundObstrOverGluing`). The instanton pseudo-bundle $\bar\Upsilon^i_{\mathfrak t,\mathfrak s}$ is spliced from the cokernel bundles of the Dirac operators over the $S^4$ factors (§§7.4–7.7). Memoir §7.9.4 says: "$\operatorname{Ker}\mathbf D^*\cong\operatorname{Coker}\mathbf D$, of complex rank $c_2(E)$ over $M(P,g_{\rm round})$". **[gloss]** Hence complex rank $\ell$ on the top stratum, consistent with Proposition 9.5.7 below ($e\in H^{2\ell}$) and with FL3 (real rank $2\ell$).
* **Hypothesis 7.8.1** (`hyp:Gluing`) is stated in full in `a-cobordism.md` §3. Item 4 asserts that $\boldsymbol\gamma_{\mathcal M}$ restricted to $\bar{\boldsymbol\chi}^{-1}(0)$ is a homeomorphism onto an open neighbourhood of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in $\bar{\mathcal M}_{\mathfrak t}$. This is the surjectivity, injectivity and continuity that FL3 does not prove. The Memoir's bibliography gives the proof as "[Feehan–Leness, *Gluing maps for SO(3) monopoles and invariants of smooth four-manifolds*, in preparation, based in part on arXiv:math/9812060 and arXiv:math/9907107]". F19 (1910.14580) proves local gluing charts for *anti-self-dual* connections near a boundary point: Theorem 3 (`mainthm:Gluing`) and Corollaries 4–7. These numbers come from the shared `mainthm` counter. It says only that the framework "should apply to more challenging gluing problems for anti-self-dual connections or SO(3) monopoles".
* **Overlap paper, Theorem 4.2** (`thm:ExtendedGluingThm`): "There is a section $\mathfrak o$ of a pseudo-vector bundle $\Upsilon\to\mathrm{Gl}(\mathfrak t,\mathfrak s,X)$ and a stratum-preserving deformation of the inclusion $\mathrm{Gl}(\mathfrak t,\mathfrak s,X)\to\bar{\mathcal C}_{\mathfrak t}/S^1$ such that the restriction of this deformation to $\mathfrak o^{-1}(0)$ parameterizes a neighborhood of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in $\bar{\mathcal M}_{\mathfrak t}/S^1$. In addition, the restriction of the obstruction section $\mathfrak o$ to any stratum vanishes transversely." The text before it says: "In [FL4], we will extend the results of [FL3] … giving the following technical result on which the proofs of Theorem 2.1 and Theorem 1.1 rely." Overlap Theorem 3.1 (`thm:GluingThm`) asserts the single-stratum version, "The construction of the map $\mathfrak p$ appears in [FL3] and it follows that …". FL3 §1.5.1 says this property is not proved in FL3.
* **Overlap paper, Definition 1.2** (`defn:LocalConeBundles`) and **Theorem 4.1** (`thm:ConesControlled`): $\mathrm{Gl}(\mathfrak t,\mathfrak s,X)$ "is a union of local cone bundle neighborhoods which satisfy the conditions of Definition 1.2". These are Thom–Mather control ($\pi_i\circ\pi_j=\pi_i$, $t_i\circ\pi_j=t_i$) and compatible compact structure groups. For such spaces, Overlap §1.1 defines the link as $\mathbf L=\partial(\bigcup_i\mathcal O_i)$ and decomposes it as $\mathbf L=\bigcup_i\mathbf L_i$ with $\mathbf L_i=\boldsymbol\gamma_i(t_i^{-1}(\varepsilon_i))-\bigcup_{j\ne i}\boldsymbol\gamma_j(t_j^{-1}[0,\varepsilon_j))$ (eq. `eq:DecomposeL`). It adds: "If the intersection of $\mathbf L$ with the lower strata has codimension greater than or equal to two in $\mathbf L$, then $\mathbf L$ has a fundamental class." Overlap §1.2 describes FL3 as providing only a *virtual* cone bundle neighbourhood: a cone bundle $\mathrm{Gl}(\mathfrak t,\mathfrak s,\Sigma)\to M_{\mathfrak s}\times\Sigma$, an obstruction section $\mathfrak o_\Sigma$ of a pseudo-vector bundle, and "a homeomorphism between $\mathfrak o_\Sigma^{-1}(0)$ and a neighborhood of $M_{\mathfrak s}\times\Sigma$ in $\bar{\mathcal M}_{\mathfrak t}/S^1$". [added by checker: the Overlap paper thus attributes the *homeomorphism* to FL3, and adds that "the existence of … the virtual cone bundle neighborhoods for $M_{\mathfrak s}\times\Sigma$ has been known since [TauIndef, FLKM1, FL3]". Memoir §1.2 likewise says that "[FL3, Theorem 1.1] can be used to define local gluing maps which parameterize neighborhoods of the strata". These descriptions are stronger than FL3's own account. FL3 §1.5.1 lists continuity on the Uhlenbeck closure, the embedding property and surjectivity as not proved there, and FL6 Hypothesis 3.1 and Remark 3.3 assume exactly these per-stratum properties. The per-stratum homeomorphism for SO(3) monopoles should therefore be treated as unproved in the sources read.]

## 14. Virtual link and link at level $\ell$ (Memoir §8.1)

### 14.1 Definitions (Memoir §8.1.1, eqs. (8.1.1)–(8.1.5))

$$t_N:\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}/S^1\to[0,\delta]\quad(8.1.1),\qquad\bar{\mathbf L}^{\rm vir}_{\mathfrak t,\mathfrak s}=\bar{\mathbf L}^{{\rm vir},s}_{\mathfrak t,\mathfrak s}\cup\bar{\mathbf L}^{{\rm vir},i}_{\mathfrak t,\mathfrak s}\quad(8.1.2),$$
$$\bar{\mathbf L}^{{\rm vir},s}_{\mathfrak t,\mathfrak s}=t_N^{-1}(\delta)\quad(8.1.3),\qquad\bar{\mathbf L}^{{\rm vir},i}_{\mathfrak t,\mathfrak s}:=\bigcup_{j=0}^r\bar{\mathbf L}^{{\rm vir},i}_{\mathfrak t,\mathfrak s}(\mathcal P_j)\quad(8.1.4),$$
$$\bar{\mathbf L}^{{\rm vir},i}_{\mathfrak t,\mathfrak s}(\mathcal P_j):=\bar{\mathcal U}(\mathfrak t,\mathfrak s,\mathcal P_j)/S^1\cap\vec t(\mathfrak t,\mathfrak s,\mathcal P_j)^{-1}(\partial\bar D(\mathcal P,\varepsilon_j))\setminus\bigcup_{k\ne j}\vec t(\mathfrak t,\mathfrak s,\mathcal P_k)^{-1}(D(\mathcal P,\varepsilon_k)).\quad(8.1.5)$$
Here $t_N$ is a fibre norm on $N_{\mathfrak t(\ell),\mathfrak s}(\delta)$, the partitions $\mathcal P_0,\dots,\mathcal P_r$ enumerate the strata of $\mathrm{Sym}^\ell(X)$, and $\varepsilon_j$ are generic constants with $\varepsilon_j>\varepsilon_k$ for $j<k$.

### 14.2 Memoir, Lemma 8.1.2 (`lem:BoundaryOfNeigh`)

> There is a decreasing sequence of positive constants $\varepsilon_0>\varepsilon_1>\cdots>\varepsilon_r$ such that the virtual link $\bar{\mathbf L}^{\rm vir}_{\mathfrak t,\mathfrak s}$ defined in (8.1.2), (8.1.3), and (8.1.4) by these constants has the following properties:
> 1. $\bar{\mathbf L}^{\rm vir}_{\mathfrak t,\mathfrak s}$ is the boundary of a neighborhood of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}/S^1$.
> 2. The intersection of $\bar{\mathbf L}^{\rm vir}_{\mathfrak t,\mathfrak s}$ with each stratum $\mathcal S$ of $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}/S^1$ is a Whitney-stratified space whose top stratum is a codimension-one, collared submanifold of $\mathcal S$.
> 3. The intersection of $\bar{\mathbf L}^{\rm vir}_{\mathfrak t,\mathfrak s}$ with the top stratum of $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}/S^1$ is a topological manifold.

**Hypotheses.** None beyond the construction of $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}$ (Theorem 6.6.1). This lemma is independent of the gluing hypothesis.

### 14.3 Memoir, Definition 8.1.3 (`defn:DefineLink`)

> The *link of an ideal Seiberg–Witten moduli space*, $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$, of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in $\bar{\mathcal M}_{\mathfrak t}/S^1$ is
> $$\bar{\mathbf L}_{\mathfrak t,\mathfrak s}=\bar{\boldsymbol\chi}^{-1}(0)\cap\bar{\mathbf L}^{\rm vir}_{\mathfrak t,\mathfrak s},$$
> where $\bar{\boldsymbol\chi}$ is the obstruction section in Hypothesis 7.8.1 and $\bar{\mathbf L}^{\rm vir}_{\mathfrak t,\mathfrak s}$ is the virtual link defined in (8.1.2).

**[gloss]** The definition presupposes Hypothesis 7.8.1, both for the existence of $\bar{\boldsymbol\chi}$ and for the identification of $\bar{\boldsymbol\chi}^{-1}(0)$, via $\boldsymbol\gamma_{\mathcal M}$, with a neighbourhood in $\bar{\mathcal M}_{\mathfrak t}$. For $\ell=0$ the Memoir uses FL2a Definition 3.22 instead (Memoir §2.6).

### 14.4 Memoir, Lemma 8.1.4 (`lem:DefiningLink`) and Lemma 8.1.5 (`lem:GRIntersect0`)

> **Lemma 8.1.4.** For generic values of the constants $\delta,\varepsilon_i$ used to define the virtual link in Lemma 8.1.2, the following hold:
> 1. $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$ is the boundary of a closed neighborhood of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in $\bar{\mathcal M}_{\mathfrak t}/S^1$.
> 2. The intersection of $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$ with each stratum $\mathcal S$ of $\bar{\mathcal M}_{\mathfrak t}/S^1$ is a Whitney-stratified space whose top stratum is a codimension-one, collared submanifold of $\mathcal S$.
> 3. The intersection of $\bar{\mathbf L}^{\rm vir}_{\mathfrak t,\mathfrak s}$ with the top stratum of $\bar{\mathcal M}_{\mathfrak t}/S^1$ is a topological manifold.

The justification printed before it: "From Item 2 of Hypothesis 7.8.1, the intersection of $\bar{\boldsymbol\chi}^{-1}(0)$ with each stratum … is a smooth submanifold … For generic values of $\varepsilon$, the subspaces $H_P(\mathcal P,\varepsilon)$ … will intersect $\bar{\boldsymbol\chi}^{-1}(0)$ transversally. Hence, Lemma 8.1.2 yields". Item 3 reads "$\bar{\mathbf L}^{\rm vir}$" in a statement about $\bar{\mathcal M}_{\mathfrak t}$. I take it to mean $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$; this is a guess.

> **Lemma 8.1.5.** Assume $w\in H^2(X;\mathbb Z)$ is such that $w\pmod2$ is *good* … Given a spin$^u$ structure $\mathfrak t$ on $X$ and a spin$^c$ structure $\mathfrak s$ on $X$ satisfying $\ell(\mathfrak t,\mathfrak s)\ge0$ and $w_2(\mathfrak t)\equiv w\pmod2$, there are positive constants $\varepsilon_0$ and $\delta_0$ such that the following hold for all generic choices of positive constants $\varepsilon_i\le\varepsilon_0$ and $\delta\le\delta_0$ defining $\bar{\mathbf L}^{\rm vir}_{\mathfrak t,\mathfrak s}$:
> 1. $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$ is disjoint from $\bar M^w_\kappa$ and $\bar{\mathcal M}^{\rm red}_{\mathfrak t}$ …
> 2. For all $z\in\mathbb A(X)$ and positive integers $\eta$ satisfying (8.1.20), and for the geometric representatives $\bar{\mathcal V}(z)$ and $\bar{\mathcal W}$ …, the intersection $\bar{\mathcal V}(z)\cap\bar{\mathcal W}^\eta\cap\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$ is a finite collection of points contained in the top stratum $\mathbf L_{\mathfrak t,\mathfrak s}$ …

"The proof … translates immediately from that of [L1, Lemma 3.9]."

[added by checker] **Status of Lemmas 8.1.4 and 8.1.5.** Both are conditional on Hypothesis 7.8.1, because $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$ is defined through $\bar{\boldsymbol\chi}$ (Definition 8.1.3). Lemma 8.1.4 also uses items 2 and 4 of the hypothesis: transversality on strata, and the identification of $\bar{\boldsymbol\chi}^{-1}(0)$ with a neighbourhood in $\bar{\mathcal M}_{\mathfrak t}$. Lemma 8.1.5 inherits the gap noted at L1 Lemma 3.9. Its item 2 needs FL2b Corollary 3.18, hence an intersection-suitable $z$, but the lemma is stated "for all $z\in\mathbb A(X)$". Only Lemma 8.1.2 (the virtual link) is unconditional.

### 14.5 The base subspace (Memoir eq. (8.1.16))

$$\bar{\mathbf{BL}}^{\rm vir}_{\mathfrak t,\mathfrak s}:=\bigcup_{j=0}^r\bar{\mathbf{BL}}^{\rm vir}_{\mathfrak t,\mathfrak s}(\mathcal P_j),\qquad\bar{\mathbf{BL}}^{\rm vir}_{\mathfrak t,\mathfrak s}(\mathcal P_j):=t_N^{-1}(0)\cap\mathbf L^{{\rm vir},i}_{\mathfrak t,\mathfrak s}(\mathcal P_j).$$
This is "defined by replacing $\tilde N_{\mathfrak t(\ell),\mathfrak s}(\delta)$ with $\tilde M_{\mathfrak s}$", and $\bar{\mathbf L}^{{\rm vir},i}$ deformation-retracts onto it. It is the level-$\ell$ analogue of L1's $\mathbf{BL}^{{\rm stab},i}\cong M_{\mathfrak s}\times\partial\bar{\mathrm{Gl}}/S^1$.

## 15. Fibre-bundle structure of the instanton component (Memoir §8.2)

### 15.1 Memoir, Proposition 8.2.1 (`prop:LinkPieceFiberBundleStructure`)

> Let $\boldsymbol\varepsilon=(\varepsilon_0,\dots,\varepsilon_r)$ be the generic constants defining the link in Lemma 8.1.4. Let $K_j\Subset\Sigma(X^\ell,\mathcal P_j)$ be the compact subset defined by those constants as in Lemma 4.8.2 [`lem:CompactSubsetsOfSi`]. For $0\le j\le r$, the subspace $\mathbf L^{{\rm vir},i}_{\mathfrak t,\mathfrak s}(\mathcal P_j)$ of $\bar{\mathcal U}(\mathfrak t,\mathfrak s,\mathcal P_j)/S^1$ defined in (8.1.5) admits a fiber bundle structure
> $$\bar M(\mathcal P_j,\boldsymbol\varepsilon)\to\tilde N_{\mathfrak t(\ell),\mathfrak s}(\delta)\times_{\mathcal G_{\mathfrak s}\times S^1}\mathrm{Fr}(\mathfrak t,\mathfrak s,\mathcal P_j)|_{K_j}\times_{G(\mathcal P_j)}\bar M(\mathcal P_j,\boldsymbol\varepsilon)\xrightarrow{\ \pi(\mathfrak t,\mathfrak s,\mathcal P_j)\ }N_{\mathfrak t(\ell),\mathfrak s}(\delta)/S^1\times K_j,\tag{8.2.2}$$
> where $\bar M(\mathcal P_j,\boldsymbol\varepsilon)$ is defined in (8.2.1).

Here (8.2.1) is
$$\bar M(\mathcal P_j,\boldsymbol\varepsilon):=\bar M(\mathcal P_j)\cap\vec t_f(\mathcal P_j,[\mathcal P_j])^{-1}(\partial\bar D(\mathcal P_j,\varepsilon_j))\setminus\bigcup_{k>j}\vec t_f(\mathcal P_j,[\mathcal P_k])^{-1}\Big(\bigsqcup_{\mathcal P''\in[\mathcal P_j<\mathcal P_k]}D(\mathcal P'',\varepsilon_k)\Big).$$

### 15.2 Memoir, Lemma 8.2.2 (`lem:S1ActionFreeOnFibers`) and Lemma 8.2.3 (`lem:LocalBaseLinkFiberBundle`)

* **Lemma 8.2.2.** The diagonal $\mathrm{SO}(3)$ action on frames, restricted to $\bar M(\mathcal P,\boldsymbol\varepsilon)$, is free.
* **Lemma 8.2.3.** Continue the hypotheses of Proposition 8.2.1. Then $\bar{\mathbf{BL}}^{\rm vir}_{\mathfrak t,\mathfrak s}(\mathcal P_j)=t_N^{-1}(0)\cap\bar{\mathbf L}^{{\rm vir},i}_{\mathfrak t,\mathfrak s}(\mathcal P_j)$ is the restriction of the bundle (8.2.2) to $M_{\mathfrak s}\times K_j$. It is
$$\bar M(\mathcal P_j,\boldsymbol\varepsilon)\to\tilde M_{\mathfrak s}\times_{\mathcal G_{\mathfrak s}\times S^1}\mathrm{Fr}(\mathfrak t,\mathfrak s,\mathcal P_j,g_{\mathcal P_j})\times_{G(\mathcal P_j)}\bar M(\mathcal P,\boldsymbol\varepsilon)\to M_{\mathfrak s}\times K_j.\tag{8.2.5}$$

Memoir §8.3, Proposition 8.3.1 (`prop:LinkCornerdescription`), describes the mutual boundaries $\partial_{k_1}\cdots\partial_{k_p}\bar{\mathbf{BL}}^{\rm vir}(\mathcal P_j)$ as subbundles. I did not extract its statement. [added by checker] The definitions are $\partial_{k_1}\cdots\partial_{k_p}\bar{\mathbf{BL}}^{\rm vir}_{\mathfrak t,\mathfrak s}(\mathcal P_j):=\bar{\mathbf{BL}}^{\rm vir}_{\mathfrak t,\mathfrak s}(\mathcal P_j)\cap\bigcap_{u=1}^p\vec t(\mathfrak t,\mathfrak s,\mathcal P_{k_u})^{-1}(\partial\bar D(\mathcal P_{k_u},\varepsilon_{k_u}))$ (eq. `eq:DefineBoundaryOne`). They satisfy $\partial_k\bar{\mathbf{BL}}^{\rm vir}(\mathcal P_j)=\bar{\mathbf{BL}}^{\rm vir}(\mathcal P_j)\cap\bar{\mathbf{BL}}^{\rm vir}(\mathcal P_k)=\partial_j\bar{\mathbf{BL}}^{\rm vir}(\mathcal P_k)$, and these are empty unless the strata $\Sigma(X^\ell,\mathcal P_j)$, $\Sigma(X^\ell,\mathcal P_k)$ are incident. The fibre and base pieces are $\partial_{i_1}\cdots\partial_{i_v}\bar M(\mathcal P_j,\boldsymbol\varepsilon)$ (eq. (8.3.3)) and $\partial_{k_1}\cdots\partial_{k_p}K_j\subset\Sigma(X^\ell,\mathcal P_j)$. The statement is:
> **Proposition 8.3.1.** For non-negative integers $k_1<\cdots<k_p<j$ and $j<i_1<\cdots<i_v\le r$, the intersection $\partial_{k_1}\cdots\partial_{k_p}\partial_{i_1}\cdots\partial_{i_v}\bar{\mathbf{BL}}^{\rm vir}_{\mathfrak t,\mathfrak s}(\mathcal P_j)$ admits a description as a fiber bundle with fibre $\partial_{i_1}\cdots\partial_{i_v}\bar M(\mathcal P_j,\boldsymbol\varepsilon)$ over $M_{\mathfrak s}\times\partial_{k_1}\cdots\partial_{k_p}K_j$, arising from the equality $\partial_{k_1}\cdots\partial_{k_p}\partial_{i_1}\cdots\partial_{i_v}\bar{\mathbf{BL}}^{\rm vir}_{\mathfrak t,\mathfrak s}(\mathcal P_j)=\tilde M_{\mathfrak s}\times_{\mathcal G_{\mathfrak s}\times S^1}\mathrm{Fr}(\mathfrak t,\mathfrak s,\mathcal P_j)|_{\partial_{k_1}\cdots\partial_{k_p}K_j}\times_{G(\mathcal P_j)}\partial_{i_1}\cdots\partial_{i_v}\bar M(\mathcal P_j,\boldsymbol\varepsilon)$.

So boundaries towards *lower* strata ($k<j$) restrict the base, and boundaries towards *higher* strata ($i>j$) restrict the fibre. Like Proposition 8.2.1, this concerns only the virtual space. Its proof, like that of Proposition 8.2.1, uses only the structure of $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}$ and not Hypothesis 7.8.1. Proposition 8.2.1 does take its constants $\boldsymbol\varepsilon$ from Lemma 8.1.4, whose genericity condition refers to $\bar{\boldsymbol\chi}$.

**[gloss] Role.** At level $\ell$, the instanton part of the virtual link is a union of pieces. Each piece is a fibre bundle over $N/S^1\times K_j$, or over $M_{\mathfrak s}\times K_j$ after retraction, with fibre a truncated product of instanton moduli spaces with spliced ends. The fibre's topology is never computed. The pairing is reduced to it by push-forward and pull-back, which gives universal coefficients. [corrected by checker: "never computed" should read "not computed in the Memoir". Memoir §1.2 says of the $G(\Sigma)$-equivariant cohomology of the fibre: "Such computations are carried out for the case $\ell=2$ in [LenessWC]. We do not address that problem in this monograph. Instead, we use a pushforward-pullback argument … to isolate the topology of these fibers as universal polynomials". The computation in Memoir Chapter 10 replaces $\bar{\mathbf{BL}}^{\rm vir}$ by a quotient ${\mathbf{QL}}^{\rm vir}_{\mathfrak t,\mathfrak s}$ in which the images of the boundaries of Proposition 8.3.1 have codimension at least two, so that the fundamental class splits as a sum over the pieces (§10.1). Its outcome, Theorems 10.1.1 and 10.1.2, is recorded in `a-cobordism.md` §6.]

## 16. Euler classes, duality and reduction to the base (Memoir Chapter 9)

* **Proposition 9.1.1** (`prop:Duality`). For $\beta\in H_\bullet(X;\mathbb R)$, let $\bar\mu_p(\beta),\bar\mu_c\in H^\bullet(\bar{\mathcal M}^{{\rm vir},*}_{\mathfrak t,\mathfrak s}/S^1;\mathbb R)$ be the classes of Definition 9.4.8. Let $\bar e_s=e(\bar\Upsilon^s_{\mathfrak t,\mathfrak s}/S^1)$, and let $\bar e_I$ be the extension of the Euler class of the instanton obstruction bundle. "If $d(\mathfrak t)=\dim\mathcal M^{*,0}_{\mathfrak t,\mathfrak s}$ and $\deg(z)+2\eta=d(\mathfrak t)-2$, then let $[\bar{\mathbf L}^{\rm vir}_{\mathfrak t,\mathfrak s}]\in H_{d(\mathfrak t)-2}(\bar{\mathcal M}^{{\rm vir},*}_{\mathfrak t,\mathfrak s}/S^1;\mathbb R)$ be the homology class defined in [`eq:DefineAmbientLinkFund` (9.3.3)]. Then
$$\#(\bar{\mathcal V}(z)\cap\bar{\mathcal W}^\eta\cap\bar{\mathbf L}_{\mathfrak t,\mathfrak s})=\langle\bar\mu_p(z)\smile\bar\mu_c^\eta\smile\bar e_I\smile\bar e_s,[\bar{\mathbf L}^{\rm vir}_{\mathfrak t,\mathfrak s}]\rangle."\tag{9.1.1}$$
It is "the analogue of [L1, Proposition 5.2]". [added by checker: the left side is the intersection number with $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}=\bar{\boldsymbol\chi}^{-1}(0)\cap\bar{\mathbf L}^{\rm vir}$. The fundamental class $[\bar{\mathbf L}^{\rm vir}]$ is built in §9.3 from Lemma 9.3.1 (`lem:NghOfEnd`), which chooses its neighbourhood $U$ using $\bar{\boldsymbol\chi}$. So Proposition 9.1.1 is conditional on Hypothesis 7.8.1, including item 3 (lower semicontinuity of $|\bar{\boldsymbol\chi}|$), which the Memoir uses for the relative Euler class (Lemma 9.5.13, `lem:ExtendingToThomSection`). By contrast, Lemma 9.5.1, Propositions 9.5.2 and 9.5.7 and Proposition 9.7.3 are statements about bundles and classes on the virtual space.] **[gloss]** The meaning of $d(\mathfrak t)$ is not consistent in the source. Proposition 9.1.1 defines it as "$\dim\mathcal M^{*,0}_{\mathfrak t,\mathfrak s}$" and imposes $\deg(z)+2\eta=d(\mathfrak t)-2$, which is the cut-down condition (8.1.20) only if $d(\mathfrak t)=\dim\mathcal M^{*,0}_{\mathfrak t}$. §9.3 (`sec:FundClassOfAmbLink`) instead says "where $d(\mathfrak t)$ is the dimension of $\mathcal M^{{\rm vir},*}_{\mathfrak t,\mathfrak s}$" and puts $[\bar{\mathbf L}^{\rm vir}]$, and $[\hat{\mathbf L},\partial\hat{\mathbf L}]$ in (9.3.1), in degree $d(\mathfrak t)-2$. That is correct for the virtual link. With that reading, the integrand $\bar\mu_p(z)\bar\mu_c^\eta\bar e_I\bar e_s$ has degree $\dim\mathcal M^{*,0}_{\mathfrak t}-2+2\ell+2r_\Xi$. This equals $\dim\mathcal M^{\rm vir}-2$ when the virtual space has real dimension $\dim\mathcal M_{\mathfrak t}+2\ell+2r_\Xi$, which matches the ranks in §13. So the pairing is consistent if the dimension condition in Proposition 9.1.1 refers to $\dim\mathcal M^{*,0}_{\mathfrak t}$ and the homology degree refers to $\dim\mathcal M^{\rm vir}$.
* **Definition 9.2.3** (`defn:DefineNu`): $\nu=c_1$ of the circle bundle $\bar{\mathcal M}^{{\rm vir},*}_{\mathfrak t,\mathfrak s}\to\bar{\mathcal M}^{{\rm vir},*}_{\mathfrak t,\mathfrak s}/S^1$ for the action (6.6.8) (`eq:DefineGlobalS1Action`). **Corollary 9.4.10** (`cor:CohomClassC1`): $\bar\jmath_\nu^*[c_{\mathcal W}]=-\iota_{x,2}^*\nu$, i.e. $\mu_c\leftrightarrow-\nu$, following L1 Lemma 4.2.
* **Lemma 9.5.1** (`lem:SWObstruction`): "Let $r_\Xi$ be the complex rank of the background obstruction bundle, $\bar\Upsilon^s_{\mathfrak t,\mathfrak s}\to\bar{\mathcal M}^{{\rm vir},*}_{\mathfrak t,\mathfrak s}$. Then $e(\bar\Upsilon^s_{\mathfrak t,\mathfrak s}/S^1)=\iota^*(-\nu)^{r_\Xi}$." Its proof is "identical to that given in [L1, Lemma 4.11]".
* **Proposition 9.5.2** (`prop:LocalInstantonEuler`): "Let $\mathcal U(\mathfrak t,\mathfrak s,\mathcal P)\subset\bar{\mathcal U}(\mathfrak t,\mathfrak s,\mathcal P)$ be the top stratum. The image in real cohomology of the Euler class of the restriction of the obstruction bundle $\Upsilon^i_{\mathfrak t,\mathfrak s}/S^1$ to $\mathcal U(\mathfrak t,\mathfrak s,\mathcal P)$ is given by a polynomial in the cohomology classes $\nu$, $\pi_X^*\iota_{\mathcal P}^*S^\ell(c(\mathfrak t))$, and $\pi_{X,\mathfrak s}^*\iota_{\mathcal P}^*c_{\mathfrak s,\ell,j}$, with coefficients depending only on the partition $\ell=|P_1|+\cdots+|P_r|$." Here $c(\mathfrak t)$ is "any real characteristic class of the bundle $\mathrm{Fr}_{\mathbb{C}\ell(T^*X)}(V)\to X$". The classes $c_{\mathfrak s,\ell,j}\in H^{2j}(M_{\mathfrak s}\times\mathrm{Sym}^\ell(X);\mathbb R)$ are the symmetrised Chern classes of $\bigoplus_i\pi_{\mathfrak s,i}^*\mathbb L_{\mathfrak s}$ (eq. (9.5.3)).
* **Proposition 9.5.7** (`prop:GlobalInstantonEulerClass`): "The Euler class of the instanton obstruction bundle, $\Upsilon^i_{\mathfrak t,\mathfrak s}/S^1\to\mathcal M^{\rm vir}_{\mathfrak t,\mathfrak s}/S^1$, is given by an element in $H^{2\ell}(\mathcal M^{\rm vir}_{\mathfrak t,\mathfrak s}/S^1;\mathbb R)$ that is a polynomial in $\iota^*\nu$, and $\iota^*\pi_X^*S^\ell(c(\mathfrak t))$, and $\iota^*\pi_{X,\mathfrak s}^*c_{\mathfrak s,\ell,i}$, with coefficients which are independent of $X$." The classes are extended as $\bar e_I$ by omitting $\iota^*$ (definition at eq. (9.5.23)). Remark 9.5.9: "the vector bundle $\Upsilon^i_{\mathfrak t,\mathfrak s}/S^1$ does not extend from $\mathcal M^{{\rm vir},*}_{\mathfrak t,\mathfrak s}/S^1$ to $\bar{\mathcal M}^{{\rm vir},*}_{\mathfrak t,\mathfrak s}/S^1$. Indeed, the cohomology class $u_i$ from [DK, Definition 8.3.16] can be seen as an obstruction to such an extension." **[gloss]** For $\ell=1$, L1 Lemma 4.12 makes this explicit ($\frac12(\pi_X^*c_1(\mathfrak t)-\nu)$). For $\ell\ge2$ the polynomial is not computed.
* **Proposition 9.7.3** (`prop:ReductionToBase`): "Continue to denote $d_s=\dim M_{\mathfrak s}$. For $0\le j\le[d_s/2]$, let $s_j(N)$ be the Segre classes of the complex-rank-$r_N$ vector bundle $N_{\mathfrak t(\ell),\mathfrak s}\to M_{\mathfrak s}$. Let $k$ and $m$ be non-negative integers satisfying $k+2m=\dim\mathbf L^{\rm vir}_{\mathfrak t,\mathfrak s}$. For any $\alpha\in H^k(M_{\mathfrak s}\times\mathrm{Sym}^\ell(X);\mathbb R)$ …
$$\langle\nu^m\smile\pi_{X,\mathfrak s}^*\alpha,[\bar{\mathbf L}^{\rm vir}_{\mathfrak t,\mathfrak s}]\rangle=\sum_{j=0}^{d_s/2}(-1)^{r_N+j}\langle\nu^{m-r_N-j}\smile\pi_{\mathfrak s}^*s_j(N)\smile\pi_{X,\mathfrak s}^*\alpha,[\bar{\mathbf{BL}}^{\rm vir}_{\mathfrak t,\mathfrak s}]\rangle."\tag{9.7.16}$$
The proof reads: "See [L1, Section 5.2]." Remark 9.7.4 says the Segre classes "have been computed under some assumptions on $H^1(X;\mathbb R)$ in [FL2a, Lemma 4.11]". That is a mis-citation: the lemma is FL2b Lemma 4.11. In general they are "a universal polynomial in $\mu_{\mathfrak s}(x)$ and $\mu_{\mathfrak s}(\gamma_i)$ with coefficients depending only on the indices $n_s'$ and $n_s''$".

**Role of §§12–16.** The Memoir's model of the level-$\ell$ link is:
$$\bar{\mathbf L}_{\mathfrak t,\mathfrak s}=\bar{\boldsymbol\chi}^{-1}(0)\cap\big(t_N^{-1}(\delta)\cup\textstyle\bigcup_j\bar{\mathbf L}^{{\rm vir},i}(\mathcal P_j)\big)\subset\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}/S^1.$$
The virtual normal data are $N_{\mathfrak t(\ell),\mathfrak s}\to M_{\mathfrak s}$, from FL2a applied to the level-$\ell$ moduli space. The obstruction is $\bar\Upsilon^s\oplus\bar\Upsilon^i$, of complex ranks $r_\Xi$ and $\ell$ on the top stratum. Pairings are evaluated by duality (9.1.1), Segre reduction (9.7.16) and push-forward along (8.2.5). The construction of $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}$ and of $\bar{\mathbf L}^{\rm vir}$ is proved; the identification of $\bar{\boldsymbol\chi}^{-1}(0)$ with a neighbourhood in $\bar{\mathcal M}_{\mathfrak t}$ is Hypothesis 7.8.1.

[added by checker] **What this machinery yields (omitted from this note; see `a-cobordism.md` §6).** Memoir Theorem 10.1.1 (`thm:LinkPairing`, eq. (10.1.1)) applies when $b_1(X)=0$, $z=h^{\delta-2m}x^m$ and $\delta-2m+2\eta=\dim\mathcal M_{\mathfrak t}-2$. It states $\#(\bar{\mathcal V}(z)\cap\bar{\mathcal W}^\eta\cap\bar{\mathbf L}_{\mathfrak t,\mathfrak s})=SW_X(\mathfrak s)\sum_{i=0}^{\min(\ell,[(\delta-2m)/2])}(q_{\delta,\ell,m,i}(c_1(\mathfrak s)-c_1(\mathfrak t),c_1(\mathfrak t))Q_X^i)(h)$, with "universal" homogeneous $q$ of degree $\delta-2m-2i$. Theorem 10.1.2 (`thm:Multiplicity`) applies with $b_1>0$ allowed: the pairing vanishes if all $SW_{X,\mathfrak s}(\omega)$ vanish. Both are about $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$ of Definition 8.1.3 and are proved via Proposition 9.1.1, so both are conditional on Hypothesis 7.8.1. The Memoir says (§10.1) that "an explicit formula … is still unknown in general".

---

# Part V. Status summary: what each link description rests on

| Stratum | Definition of the link | Model | Classes on the model | What it rests on |
|---|---|---|---|---|
| $\bar M^w_\kappa$ (zero-section) | FL2a Def. 3.7: $\{\|\Phi\|^2_{L^2}=\varepsilon\}/S^1$ | No global model (FL2a Rem. 3.9). Locally, near each point of $\bar{\mathcal V}(z)\cap M^w_\kappa$, cobordant to $T\subset\mathbb P(\operatorname{Ker}D_{A,\vartheta})\cong\mathbb{CP}^{n_a+c-1}$ dual to $h^c$ (FL2b L. 3.26–3.27) | $\mu_c\mapsto2h$ (L. 3.28); obstruction Euler class $h^c$; pairing $2^{n_a-1}D$ (Prop. 3.29) | Proved, given: $w\pmod2$ good; $n_a>0$; $d_a\ge0$; $\deg z\ge d_a$; $z$ intersection-suitable; generic metric and parameters; $b_2^+>0$. Lemma 3.21 uses Taubes' ASD gluing at a generic metric. No hypothesis on $\operatorname{Coker}D_A$. |
| $M_{\mathfrak s}$, $\ell=0$ | FL2a Def. 3.22: $\boldsymbol\gamma(\boldsymbol\varphi^{-1}(0)\cap\mathbb PN_{\mathfrak t}(\Xi,\mathfrak s))$ | Zero set of a transverse section of $\boldsymbol\gamma^*\Xi/S^1\cong\mathcal O(1)^{\oplus r_\Xi}$ over $\mathbb PN$; $[N]-[\Xi]=\operatorname{ind}\boldsymbol{\mathcal D}^n$ | $\mu_c\mapsto\nu=c_1(\mathcal O(1))$ (FL2b L. 4.8); $\mu_p$ via Cor. 4.7; $e=\nu^{r_\Xi}$ (L. 4.9); $\operatorname{ch}N$ (FL2a Thm. 3.29) | Proved (FL2a Thms. 3.19, 3.21, L. 3.23), given no zero-section pairs in $M_{\mathfrak s}$ (e.g. $w$ good) and generic parameters. Explicit Segre classes need $\alpha\smile\alpha'=0$ on $H^1$. |
| $M_{\mathfrak s}\times X$, $\ell=1$ | L1 (3.79): $\boldsymbol\gamma(\boldsymbol\chi^{-1}(0)\cap\bar{\mathbf L}^{\rm stab})$ | Virtual link = boundary of $N(\varepsilon)\times_{\mathcal G_{\mathfrak s}}\bar{\mathrm{Gl}}(\delta)$; instanton piece is a disk bundle over $M_{\mathfrak s}\times\partial\bar{\mathrm{Gl}}/S^1$ | $\mu_c\mapsto-\nu$ (L. 4.2); $e_s=(-\nu)^{r_\Xi}$ (L. 4.11); $e_i=\frac12(\pi_X^*c_1(\mathfrak t)-\nu)$ (L. 4.12); $\partial\bar{\mathrm{Gl}}/S^1$ pairings (L. 5.24, via LenessWC) | L1 Thm. 3.8, attributed to [FL3, FL4]. FL4 ("Surjectivity of gluing maps") is listed as in preparation; FL3 proves only existence. |
| $M_{\mathfrak s}\times\mathrm{Sym}^\ell X$, $\ell\ge1$ | Memoir Def. 8.1.3: $\bar{\boldsymbol\chi}^{-1}(0)\cap\bar{\mathbf L}^{\rm vir}$ | $\bar{\mathbf L}^{\rm vir}=t_N^{-1}(\delta)\cup\bigcup_j\bar{\mathbf L}^{{\rm vir},i}(\mathcal P_j)$; pieces fibre over $N/S^1\times K_j$ with fibre $\bar M(\mathcal P_j,\boldsymbol\varepsilon)$ (Prop. 8.2.1) | $e_s=(-\nu)^{r_\Xi}$ (L. 9.5.1); $e_I$ a universal polynomial, not computed (Prop. 9.5.7); Segre reduction (Prop. 9.7.3) | Overlap structure proved (Thm. 6.6.1, L. 8.1.2, Prop. 8.2.1). Analytic identification is Hypothesis 7.8.1, whose proof is deferred to an unpublished monograph. FL6 instead assumes the per-stratum Hypothesis 3.1 (`hyp:Local_gluing_map_properties`) and takes the global assembly from the Memoir. |

**[gloss] Points to carry forward to (d).**
1. *Instanton link.* FL never prove a global projective-bundle structure, and nothing in their argument needs one. A global statement is replaced by a local cobordism after cutting down by $\mathcal V(z)$ with $\deg z\ge d_a$. Then $\bar{\mathcal V}(z)\cap\bar M^w_\kappa$ is finite, or empty if $\deg z>d_a$. Any argument that pairs with the whole link $\bar{\mathbf L}^w_{\mathfrak t,\kappa}$ as a cycle, or takes $\deg z<d_a$ so that this intersection is not finite, goes beyond FL. FL2a explicitly says the link "might not have a fundamental class". [corrected by checker: this needs one qualification. Memoir Theorem 8.1.9 (`thm:CobordismThm`) states the cobordism identity (8.1.21) between the intersection numbers $\#(\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{\eta-1}\cap\bar{\mathbf L}^w_{\mathfrak t,\kappa})$ and the SW link numbers for every $z$ with $\deg(z)+2\eta=\dim\mathcal M^{*,0}_{\mathfrak t}-2$. It imposes neither $\deg z\ge d_a$ nor intersection-suitability. So the Memoir *states* the identity for the instanton-link intersection number also when $\deg z<d_a$. That number is a count of points in the top stratum, not a pairing with a fundamental class. The Memoir's own applications use $\deg z=d_a$ on the blow-up. What FL never do is *evaluate* that number when $\deg z<d_a$. The only evaluations are FL2b Proposition 3.29 (with $\deg z\ge d_a$, $n_a>0$, $z$ intersection-suitable) and the unproved assertion in Memoir Remark 2.6.1 about $n_a\le0$. The relation to Donaldson invariants also requires $\deg z=d_a$. Note too that (8.1.21) as printed pairs $\bar{\mathcal W}^{\eta-1}$ with the condition $\deg(z)+2\eta=\dim\mathcal M^{*,0}_{\mathfrak t}-2$; see `a-cobordism.md` §4.1.]
2. *Level zero.* Unconditional and explicit.
3. *Level one.* Explicit modulo L1 Theorem 3.8. Only the Euler classes for $\ell=1$ are computed.
4. *Level $\ge2$.* The proved part is topological: the space of global splicing data, its virtual link and the fibre-bundle structures. The analytic part, Hypothesis 7.8.1, is assumed. The instanton obstruction Euler class and the fibre pairings are left as universal unknowns.

---

## Uncertainties

1. **Numbering.** All theorem numbers were inferred from LaTeX counters, and all equation numbers were obtained by a script that counts numbered display environments. Spot checks agree with every cross-citation tested. Published versions may differ. In particular, L1 eq. (2.51) and Memoir eq. (2.6.2) both cite "[FL2b, Lemma 3.30]" for the instanton link pairing, which in the arXiv source of FL2b is **Proposition 3.29** (`prop:LinkOfASD`). FL6 cites Proposition 3.29. I cannot tell whether the published FL2b renumbered it.
2. **FL2b Lemma 4.11, eq. (4.26).** The sum is printed as $\sum_{j=1}^i$. The proof and L1 Lemma 2.4 show it should be $\sum_{j=0}^i$. L1 restates the lemma with hypothesis "$b_1(X)=0$" in place of "$\alpha\smile\alpha'=0$ on $H^1$".
3. **FL2b Corollary 4.6** prints the target as $H^2(\cdots;\mathbb Z)$ for a degree-four class.
4. **Memoir Remark 9.7.4** cites "[FL2a, Lemma 4.11]" for Segre classes. The result is FL2b Lemma 4.11.
5. **Memoir Lemma 8.1.4(3)** refers to $\bar{\mathbf L}^{\rm vir}_{\mathfrak t,\mathfrak s}$ in a statement about $\bar{\mathcal M}_{\mathfrak t}/S^1$. I read it as $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$; this is a guess.
6. **Memoir Proposition 9.1.1.** The symbol $d(\mathfrak t)$ is used in two senses: "$\dim\mathcal M^{*,0}_{\mathfrak t,\mathfrak s}$" in the proposition, and "the dimension of $\mathcal M^{{\rm vir},*}_{\mathfrak t,\mathfrak s}$" in §9.3. The proposition uses the same letter both in the dimension condition and in the homology degree. My reading, by a degree count, is in §16 of this note. It is my interpretation, not something the text states.
7. **Sign conventions for $\nu$.** FL2b Def. 4.3 takes $\nu=-c_1$ of the circle bundle, which is $c_1(\mathcal O(1))$. L1 Def. 4.1 and Memoir Def. 9.2.3 take $\nu=+c_1$ of a circle bundle with a different, diagonal action. I checked that the stated pull-backs and Euler classes are consistent under $\nu_{\rm FL2b}=-\nu_{\rm L1}$, but I did not check the circle actions in detail.
8. **FL2b Proposition 3.29 wording.** It says "$\mathbf L^{w,\varepsilon}_{\mathfrak t,\kappa}\cap\iota(M^w_\kappa)$ is oriented as the boundary …". The intended object is presumably the link itself. FL2a Lemma 3.8 places the link in $\bar{\mathcal M}_{\mathfrak t}$, whereas Definition 3.7 places it in $\bar{\mathcal M}_{\mathfrak t}/S^1$.
9. **Projective-bundle description of the instanton link.** The task asked for an identification with a projective bundle over the instanton moduli space. No such theorem exists in the sources. The nearest statements are:
   * Ann., after Lemma 3.13: at a *generic* point, a cone on $\mathbb{CP}^{n_a-1}$. This relies on transversality to jumping-line strata, which FL2a states as an assumption.
   * FL2b Lemma 3.25: $\mathbb P(\operatorname{Ker}D_{A,\vartheta})\cong\mathbb{CP}^{k-1}$ locally at the finitely many points of $\mathcal V(z)\cap M^w_\kappa$.
   
   I have reported these and not invented a global statement.
10. **L1 Lemma 5.24.** The proof rests on constructions and Segre-class computations in Leness, *Donaldson wall-crossing formulas via topology* (dg-ga/9603016), which was not provided. I could not check the "branched cover of degree negative two" and "degree negative one" claims, or the three formulas (5.76).
11. **Status of FL4 and of the "gluing maps" monograph.** In the sources, FL4 is "in preparation" in L1 (2001). The Memoir v4 (2018) lists *Gluing maps for SO(3) monopoles and invariants of smooth four-manifolds* as "in preparation". F19 (2019) treats only ASD connections. I have no source after these, so I cannot say whether a proof of L1 Theorem 3.8 or Memoir Hypothesis 7.8.1 has since appeared.
12. **Statements not extracted.** I did not extract the statement of Memoir Proposition 8.3.1 (`prop:LinkCornerdescription`), which describes the corners $\partial_{k_1}\cdots\partial_{k_p}\bar{\mathbf{BL}}^{\rm vir}(\mathcal P_j)$. The numbers of L1 eq. (5.9) and Memoir Lemma 4.8.2 and eq. (6.6.8) come from the counting scripts. [checker: Proposition 8.3.1 is now stated in §15.2. An independent counter confirms L1 (5.9), Memoir Lemma 4.8.2 and Memoir (6.6.8).]
13. **Theorem statements omitted.** I did not reproduce FL2a Lemma 3.27 (`lem:DiagonalQuotient`), on which the sign "$+h^c$" and "$+2h$" in FL2b Lemmas 3.27–3.28 depend. I did not reproduce FL2b Definition 2.3 ($O^{\rm asd}(\Omega,w)$). [checker: FL2a Lemma 3.27 says the following. (1) If $S^1$ acts on $Q_1\times_MV$ by $(e^{i\theta}q_1,e^{ik\theta}v)$, then $(Q_1\times_MV)/S^1\cong L_1^{-k}\otimes V$. (2) The analogous statement holds for $c_1$ of $(Q_1\times_MQ_2)/S^1$, namely $c_1(Q_2)-kc_1(Q_1)$. For the Hopf bundle $Q_1=S^{2k-1}\to\mathbb{CP}^{k-1}$ with $h=-c_1(Q_1)$, part (1) with $k=1$ gives a diagonal quotient $\cong\mathcal O(1)$, with Euler class $h$. This is consistent with FL2b's $h^c$ and $2h$ and with the glosses in §§3.4–3.5. FL2b Definition 2.3 orients $\mathcal M_{\mathfrak t}$ by the complex orientation of $\det D_{A,\vartheta}$ together with Donaldson's orientation $o(\Omega,w)$ of $\det(d^*_{\hat A}+d^+_{\hat A})$.]
14. **Sign of $n_s$.** The Memoir (§2.3.5) calls $n_s$ "minus the complex index of the normal deformation operator", while FL2a (3.71) sets $\operatorname{ind}_{\mathbb C}\mathcal D^n=n_s$. I resolved this as described in §5.6, by reading the Memoir's "index" as that of the complex. This is an interpretation.
15. **Overlap paper conventions.** §2.3 of the Overlap paper writes "$\kappa=p_1(\mathfrak t)$". Elsewhere FL use $\kappa=-\frac14p_1(\mathfrak t)$. I take this as a misprint there.
16. **Kronheimer–Mrowka.** The KM structure theorem is not used in the material on links. Its statement as restated by FL is in `a-cobordism.md` §8.
