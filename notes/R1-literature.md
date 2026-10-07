# R1. Feehan–Leness on the SO(3)-monopole cobordism: what is proved, what is assumed, and the family analogue our argument needs

## 0. Sources, numbering, notation

**Sources (arXiv LaTeX).**
- FL1 = dg-ga/9710032, *PU(2) monopoles I: regularity, Uhlenbeck compactness, and transversality*.
- FL2a = math/0007190, *PU(2) monopoles and links of top-level Seiberg–Witten moduli spaces*.
- FL2b = dg-ga/9712005, *PU(2) monopoles II: top-level Seiberg–Witten moduli spaces and Witten's conjecture in low degrees*.
- FL3 = math/9907107, *PU(2) monopoles III: existence of gluing and obstruction maps*.
- FLL1 = math/0106238, *SO(3) monopoles, level-one Seiberg–Witten moduli spaces, and Witten's conjecture in low degrees*.
- Memoir = math/0203047 v4, *An SO(3)-monopole cobordism formula relating Donaldson and Seiberg–Witten invariants*, Mem. Amer. Math. Soc. 256 (2018), no. 1226.
- FL6 = math/0609530, *Witten's conjecture for many four-manifolds of simple type*, J. Eur. Math. Soc. 17 (2015).
- Overlap = 1211.0480, Feehan–Leness, *SO(3)-monopoles: the overlap problem* (source dated 2005).
- FL19 = 1910.14580, Feehan–Leness, gluing via maps of Banach manifolds with corners.
- KM94 = math/9404232, Kronheimer–Mrowka, *Recurrence relations and asymptotics for four-manifold invariants*, Bull. Amer. Math. Soc. 30 (1994). Their full paper (*Embedded surfaces and the structure of Donaldson's polynomial invariants*, J. Differential Geom. 41 (1995)) is not on arXiv; its Theorem 1.7 is quoted only as restated in FL6.

**Numbering.** Theorem, lemma and equation numbers are those of the arXiv sources. They were computed from the LaTeX counters, and every label used below was re-checked for this note. The equation numbers for FL1 and for FL2b §4 were checked against cross-citations:
- FL2a and FL3 cite FL1 (2.36)–(2.39) and (3.2);
- the Memoir cites FL2b (4.62);
- FLL1 cites FL2b (4.27), (4.52) and (4.55).

Published numberings differ in places. The Memoir and FLL1 cite FL2b Prop. 3.29 as "Lemma 3.30". FL6 cites Memoir Hyp. 7.8.1 as "Conjecture 6.7.1" of an earlier version.

**Notation (Memoir Ch. 2; FL6 (3.1)).**
- $X$ is closed, connected, oriented and smooth. A spin$^u$ structure is $\mathfrak t=(\rho,V)$ with $V=W\otimes E$.
- $\Lambda=c_1(\mathfrak t)=c_1(W^+)+c_1(E)$, $\kappa=-\tfrac14p_1(\mathfrak t)$, and $w=c_1(E)$ is an integral lift of $w_2(\mathfrak t)$.
- The two indices (Memoir (2.1.12)) are
$$d_a(\mathfrak t)=-2p_1(\mathfrak t)-\tfrac32(\chi+\sigma)=\dim M^w_\kappa,\qquad n_a(\mathfrak t)=\tfrac14\big(p_1(\mathfrak t)+\Lambda^2-\sigma\big)=\operatorname{ind}_{\mathbb C}D_{A,\vartheta}.$$
- $\mathcal M_{\mathfrak t}$ is the moduli space of the perturbed SO(3)-monopole equations (Memoir (2.1.10)). The circle acts by $\Phi\mapsto e^{i\theta}\Phi$.
- $\mathcal M^{*,0}_{\mathfrak t}$ is the free part (connection irreducible, $\Phi\not\equiv0$), of dimension $d_a+2n_a$. $\iota(M^w_\kappa)$ is the zero-section stratum.
- $\mathfrak t(\ell)$ has $p_1(\mathfrak t(\ell))=p_1(\mathfrak t)+4\ell$ and the same $c_1$ and $w_2$ (Memoir (2.1.13)).
- A spin$^c$ structure $\mathfrak s$ with $V=W'\oplus W'\otimes L$ gives the Seiberg–Witten pairs $\iota(M_{\mathfrak s})$, with $c_1(L)=\Lambda-c_1(\mathfrak s)$ and $d_s(\mathfrak s)=\tfrac14(c_1(\mathfrak s)^2-2\chi-3\sigma)$. Their *level* is
$$\ell(\mathfrak t,\mathfrak s)=\tfrac14\big((\Lambda-c_1(\mathfrak s))^2-p_1(\mathfrak t)\big)\qquad(\text{Memoir }(2.3.14)).$$
- $\mu_p(\beta)=-\tfrac14p_1(\mathbb F_{\mathfrak t})/\beta$, and $\mu_c=c_1(\mathbb L_{\mathfrak t})$, where $\mathbb L_{\mathfrak t}=\mathcal C^{*,0}_{\mathfrak t}\times_{(S^1,\times-2)}\mathbb C$ is the weight-two line.
- $\bar{\mathcal V}(z)$ and $\bar{\mathcal W}$ are FL's geometric representatives (constructed in FL2b Lemmas 3.12–3.13, named in Def. 3.14).
- $v\in H^2(X;\mathbb Z/2)$ is *good* if no integral lift of $v$ is torsion (FL2b Def. 3.20 = Memoir Def. 2.2.1).
- $O^{\rm asd}(\Omega,w)$ is Donaldson's orientation times the complex orientation of $\det D_{A,\vartheta}$ (FL2b Def. 2.3).

---

## (a) The SO(3)-monopole cobordism formula

**Memoir, Theorem 1 (eq. (1.1.1)).**

*Hypotheses.*
- Hypothesis 7.8.1 holds.
- $b_1(X)=0$ and $b^+(X)$ is odd and $>1$.
- $w-\Lambda\equiv w_2(X)\pmod 2$.
- $0\le m\le[\delta/2]$ and $\delta\equiv-w^2-\tfrac34(\chi+\sigma)\pmod 4$.
- $\delta<i(\Lambda):=\Lambda^2-\tfrac14(3\chi+7\sigma)$.

*Conclusion.*
$$D^w_X(h^{\delta-2m}x^m)=\sum_{\mathfrak s}(-1)^{\frac14(w-\Lambda+c_1(\mathfrak s))^2}SW_X(\mathfrak s)\sum_{i=0}^{\min(\ell,[\delta/2]-m)}\big(p_{\delta,\ell,m,i}(c_1(\mathfrak s),\Lambda)\,Q_X^i\big)(h).$$
Here $\ell=\tfrac14\big(\delta+(c_1(\mathfrak s)-\Lambda)^2+\tfrac34(\chi+\sigma)\big)=\ell(\mathfrak t,\mathfrak s)$. Each $p_{\delta,\ell,m,i}$ is homogeneous of degree $\delta-2m-2i$, and its coefficients are universal functions of $\chi$, $\sigma$, $c_1(\mathfrak s)^2$, $\Lambda^2$, $c_1(\mathfrak s)\cdot\Lambda$, $\delta$, $m$ and $\ell$. The coefficients are not computed. No simple-type hypothesis is made.

**Assembly (Memoir §10.6).** One passes to $\tilde X=X\#\overline{\mathbb{CP}}{}^2$ with $c_1(\tilde{\mathfrak t})=\Lambda$ and $\tilde w=w+\mathrm{PD}[e]$, which is good. Then $n_a(\tilde{\mathfrak t})=\tfrac14(i(\Lambda)-\delta)>0$. Three statements are combined.
1. *Instanton link:* FL2b Prop. 3.29 (eq. (3.60)), restated as Memoir (2.6.2); see (c1). This is the only place where $\delta<i(\Lambda)$ is used.
2. *Cobordism identity (Memoir Thm. 8.1.9, eq. (8.1.21)).* For $w$ good,
$$\#\big(\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{\delta_c}\cap\bar{\mathbf L}^w_{\mathfrak t,\kappa}\big)=-\sum_{\mathfrak s}(-1)^{o_{\mathfrak t}(w,\mathfrak s)}\,\#\big(\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{\delta_c}\cap\bar{\mathbf L}_{\mathfrak t,\mathfrak s}\big),\qquad \deg z+2\delta_c=\dim\mathcal M_{\mathfrak t}-2 .$$
   - The sign is $o_{\mathfrak t}(w,\mathfrak s)=\tfrac14(w-c_1(L))^2$ (Memoir Lemma 8.1.7), and $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}=\emptyset$ when $\ell(\mathfrak t,\mathfrak s)<0$.
   - As printed, (8.1.20)–(8.1.21) pair the exponent $\eta-1$ with the condition $\deg z+2\eta=\dim\mathcal M^{*,0}_{\mathfrak t}-2$. The normalization above is the one the proof of Theorem 1 uses.
   - The identity counts the ends of the one-manifold $\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{\delta_c}\cap\mathcal M^{*,0}_{\mathfrak t}/S^1$. Its ends lie near $M^w_\kappa$ and near the strata $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ of every level (Memoir §2.4; FL2b Cor. 3.18).
   - Implicit hypotheses: $b^+>0$ and a generic metric. For $\ell\ge1$ the identity also needs Hyp. 7.8.1, which enters through the definition of the link (Def. 8.1.3).
3. *Link pairings.*
   - Memoir Thm. 10.1.1 (eq. (10.1.1)): each pairing is $SW_X(\mathfrak s)$ times a universal polynomial in $\langle c_1(\mathfrak s)-\Lambda,h\rangle$, $\langle\Lambda,h\rangle$ and $Q_X(h)$, with $Q_X$ to power at most $\ell$.
   - Memoir Thm. 10.1.2: the pairing vanishes if $SW_{X,\mathfrak s}\equiv0$. This is the multiplicity conjecture, FL2b Conj. 3.34.
   - Memoir Lemma 10.6.2 handles the blow-up.
   - All three are conditional on Hyp. 7.8.1 for $\ell\ge1$.

**The gluing-free case actually proved: FL2b, Theorem 3.33.**

*Hypotheses.*
- $b_2^+(X)>0$, and $w\equiv w_2(\mathfrak t)$ is good.
- $d_a\le\deg z\le d_a+2n_a-2$, and $z$ is intersection-suitable.
- Generic metric and parameters (a standing assumption of FL2b).
- Every reducible in $\bar{\mathcal M}_{\mathfrak t}$ lies in the top level, i.e. obeys (3.63), $(\Lambda-c_1(\mathfrak s))^2=p_1(\mathfrak t)$.

*Conclusions.*
- **(a)** If $(\Lambda-c_1(\mathfrak s))^2<p_1(\mathfrak t)$ for every $\mathfrak s$ with $M_{\mathfrak s}\neq\emptyset$ ((3.68): no reducible at any level), then $\#(\bar{\mathcal V}(z)\cap\bar M^w_\kappa)=0$ ((3.69)).
- **(b)** If $\deg z=d_a$, then
$$\#(\bar{\mathcal V}(z)\cap\bar M^w_\kappa)=-2^{1-n_a}\sum_{\mathfrak s}(-1)^{o_{\mathfrak t}(w,\mathfrak s)}\langle\mu_p(z)\smile\mu_c^{n_a-1},[\mathbf L_{\mathfrak t,\mathfrak s}]\rangle\qquad((3.70)),$$
  with level-zero links, which FL2b Thm. 4.13 evaluates.
- **(c)** If $d_a<\deg z\le d_a+2n_a-2$, the corresponding signed sum of link pairings vanishes ((3.71)).

*Proof.* Stokes on the one-manifold (3.62), $\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{\delta_c}\cap\bar{\mathcal M}^{*,\ge\varepsilon}_{\mathfrak t}/S^1$. Cor. 3.18 keeps it off the lower irreducible strata, Prop. 3.29 evaluates the instanton end, and FL2a's level-zero links handle the reducibles (identity (3.65)). No SO(3)-monopole gluing is used. FL2b Cor. 3.35 removes the top-level hypothesis only conditionally on Conj. 3.34.

**FL6.**
- *FL6 Thm. 3.2*, cited from the Memoir, assumes FL6 Hyp. 3.1. Its hypotheses are:
  - $X$ standard ($b_1=0$, $b^+$ odd $\ge3$) and of Seiberg–Witten simple type;
  - $w-\Lambda\equiv w_2(X)\pmod 2$;
  - $I(\Lambda)>\delta$;
  - $\delta\equiv-w^2-3\chi_h\pmod 4$;
  - $\delta\ge2m$.
- *Its conclusion* is
$$D^w_X(h^{\delta-2m}x^m)=\sum_{K\in B(X)}(-1)^{\frac12(w^2-\sigma)+\frac12(w^2+(w-\Lambda)\cdot K)}\,SW'_X(K)\,f_{\delta,m}(\chi_h,c_1^2,K,\Lambda)(h)\qquad((3.4)\text{–}(3.5)),$$
  with $f_{\delta,m}$ universal.
- *Sign.* This sign agrees with the Memoir's $(-1)^{o_{\mathfrak t}(w,\mathfrak s)}$ if and only if $\Lambda^2$ is even. The discrepancy does not depend on $K$.
- *FL6 Main Thm. 1.2.* If $X$ is standard, of Seiberg–Witten simple type, and either abundant or with $c_1^2\ge\chi_h-3$, then Thm. 3.2 implies Witten's conjecture (Conj. 1.1, eq. (1.2)) for $X$.
- *Method.* The universal coefficients are fixed from Fintushel–Park–Stern examples and blow-ups (Lemma 4.5, Prop. 4.8, Thm. 4.11).
- *Logical status.* An implication, conditional on Hyp. 3.1.

**Kronheimer–Mrowka structure theorem.**
- *KM94 Theorem 1* assumes $X$ simply connected with $b^+$ odd $\ge3$, the standing assumption there, and of simple type. It gives finitely many classes $K_1,\dots,K_p$, each an integral lift of $w_2(X)$, and nonzero rationals $a_s$ with
$$q=\exp(Q/2)\sum_s a_se^{K_s}$$
  as analytic functions on $H_2(X;\mathbb R)$, for $w=0$.
- *KM94 Theorem 2.* Every essential embedded surface with $\Sigma\cdot\Sigma\ge0$ satisfies $2g-2\ge\Sigma\cdot\Sigma+\max_sK_s\cdot\Sigma$.
- *FL6 Thm. 2.2*, citing KM's Theorem 1.7(a), is the version for all $w$. For standard $X$ of KM simple type with some nonzero Donaldson invariant,
$$\mathbf D^w_X(h)=e^{Q_X(h)/2}\sum_K(-1)^{(w^2+K\cdot w)/2}\beta_X(K)\,e^{\langle K,h\rangle}\qquad\text{(FL6 (2.9))}.$$
- *Its role in FL:* it enters FL6 only (Lemma 2.3, Prop. 2.5; Thm. 2.4, independence of $w$).
- *Relation to our argument: an analogy only.* Take spheres with $S_i^2=-4$, $w_e=w_0+\sum e_i\mathrm{PD}[S_i]$, and the signs $\varepsilon(e)$ of section (e). On a closed $X$ of simple type, (2.9) gives
$$\sum_e\varepsilon(e)\,\mathbf D^{w_e}_X=\prod_i\varepsilon_i(0)\;e^{Q/2}\sum_K(-1)^{(w_0^2+K\cdot w_0)/2}\beta_X(K)\prod_i\big(1-s_i(-1)^{K\cdot S_i/2}\big)e^{K}.$$
  This projects onto the basic classes with prescribed $K\cdot S_i\bmod 4$. Our $X$ has vanishing Donaldson invariants, and nothing of Kronheimer–Mrowka is used.

---

## (b) Uhlenbeck compactness and the lower strata

**Compactness.**
- *FL1 Thm. 1.1*, with Thm. 4.20 for the sequential form and Def. 4.19 for the convergence. For closed $(X,g)$ with fixed connections on $W$ and $\det E$ there is $N_p$ such that, for $N\ge N_p$, the closure $\bar M_{W,E}$ in $\bigcup_{\ell\le N}\mathbf M_{W,E_{-\ell}}$ is compact, second countable and Hausdorff. $N_p$ depends on these curvatures and on $c_2(E)$.
- *Memoir Thm. 2.1.3* restates this in the spin$^u$ language.
  - $\bar{\mathcal M}_{\mathfrak t}$ lies in the space of ideal monopoles $\bigsqcup_{\ell\le N}\mathcal M_{\mathfrak t(\ell)}\times\mathrm{Sym}^\ell(X)$ (Memoir (2.1.14)).
  - It carries a continuous circle action.
  - Convergence (Memoir Def. 2.1.2) is $L^2_{k,\mathrm{loc}}$ off the points, with $|F_{\hat A_\alpha}|^2\to|F_{\hat A}|^2+8\pi^2\sum_x\delta_x$.
- *Hypothesis.* The perturbations must satisfy FL1 (2.29): $\|\tau-\mathrm{id}\|_{L^\infty}\le\tfrac1{64}$ and $\|\vartheta\|_{L^\infty_1}\le1$, holonomy terms included. The restatements omit this.
- *Where the constants come from.*
  - FL1 Lemmas 4.2–4.3 give the $L^4$ bound on $\Phi$ and the $L^2$ bounds on $F^\pm_A$. Their constants depend on $\|R\|_{L^2}$ (where $R$ is the scalar curvature), on the curvatures of the fixed connections and on $p_1$.
  - FL1 Lemma 4.4 bounds $\Phi$ and $F^+_A$ in $C^0$ in terms of the $C^0$ norms of $R$ and of those curvatures.
- *Bubbles.* By Lemma 4.4 the spinor never bubbles, so every bubble is an anti-self-dual connection on $S^4$ with zero spinor.
- *Product structure of levels.* For FL1's holonomy perturbations the levels are not products (FL1 §1.1.2). For the generic-metric perturbations used in all later papers they are.

**Strata.**
- *Transversality.*
  - Memoir Thm. 2.1.1 (= FL2a Thm. 2.13; the proof is in Feehan's generic-metric paper): for generic $(g,\rho,\tau,\vartheta)$, $\mathcal M^{*,0}_{\mathfrak t}$ is smooth of dimension $d_a+2n_a$.
  - FL1 Thm. 1.3 (holonomy perturbations): the free strata $\mathbf M^{*,0}_{W,E_{-\ell}}|_\Sigma$ are smooth of the expected dimension for every $\ell$ and every stratum $\Sigma\subset\mathrm{Sym}^\ell(X)$. The case $\ell>0$ is argued in one paragraph (§5.1.3).
  - FL1 §5 (introduction) says that the proof "does not apply to PU(2) monopoles which are zero-sections or which are reducible".
  - Simultaneous transversality at all levels is used but never stated.
- *Fixed points.*
  - FL2a Prop. 3.1 assumes $b_2^+\ge1$, a generic metric and $\hat A$ non-flat. Under these hypotheses a circle-fixed point is either $(A,0)$ with $\hat A$ irreducible anti-self-dual, or reducible for some $V=W'\oplus W'\otimes L$ with $\Phi=\Psi\oplus0\not\equiv0$.
  - Flat connections are excluded by the Morgan–Mrowka criterion (FL2a Lemma 3.2; Cor. 3.3 then gives no zero-section pairs in $M_{\mathfrak s}$).
  - Goodness of $w$ excludes only the flat *reducible* connections.
  - For good $w$, $\bar{\mathcal M}_{\mathfrak t}=\bar{\mathcal M}^{*,0}_{\mathfrak t}\sqcup\bar M^w_\kappa\sqcup\bar{\mathcal M}^{\rm red}_{\mathfrak t}$ (Memoir (2.2.2)).
  - *Reducible zero-section pairs* (abelian anti-self-dual connections) never occur in FL's closed, fixed-generic-metric setting (FL3 §2.1). FL treat them only in a path of metrics, under Memoir Hyp. 11.3.5.
- *Free lower strata.*
  - $\dim\mathcal M_{\mathfrak t(\ell)}=\dim\mathcal M_{\mathfrak t}-6\ell$, so $\mathcal M^{*,0}_{\mathfrak t(\ell)}\times\Sigma$ has codimension at least $2\ell$ (FL2b, text after (3.21); Overlap (2.10)).
  - FL2b Cor. 3.18: let $z$ be intersection-suitable (FL2b Lemma 3.17; e.g. $z$ has no $H_3$ factor or no $H_0$ factor) with $\deg z+2\delta_c=d_a+2n_a-2$. Then, for generic representatives, $\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{\delta_c}\cap\bar{\mathcal M}^{*,0}_{\mathfrak t}/S^1$ is a one-manifold disjoint from the lower strata of $\bar{\mathcal M}^*_{\mathfrak t}/S^1$.
  - FL2b Rem. 3.19 calls intersection-suitability "technical".
- *Instanton stratum.*
  - FL2b Lemma 3.21 assumes $w$ good, a generic metric and $b_2^+>0$. It identifies the zero-section part of $\bar{\mathcal M}_{\mathfrak t}$ with $\iota(\bar M^w_\kappa)$; the reverse inclusion is argued from Taubes' anti-self-dual gluing.
  - FL2a Lemma 3.4: $H^2_{A,0}\cong H^2_{\hat A}\oplus\operatorname{Coker}D_{A,\vartheta}$, so zero-section points are in general not regular.
  - FL2a Cor. 3.6 gives an $S^1$-equivariant Kuranishi model at top-level zero-section points. Its normal space is $\operatorname{Ker}D_{A,\vartheta}$ and its obstruction space is $\operatorname{Coker}D_{A,\vartheta}$.

**Seiberg–Witten strata at every level.**
- *Reducibles are Seiberg–Witten monopoles.* By FL2a Lemmas 3.11–3.13 and 3.16, the reducibles for $V=W'\oplus W'\otimes L$ form exactly $M_{\mathfrak s}$, for the Seiberg–Witten equations with perturbation $\eta=F^+_{A_\Lambda}$ (FL2a (2.56)). The embedding is topological when $w_2(\mathfrak t)\neq0$ and smooth on $M^0_{\mathfrak s}$.
- *Compactness and smoothness.* $M_{\mathfrak s}$ is compact if $\|\tau-\mathrm{id}\|<\tfrac1{64}$ (FL2a Prop. 2.15). For generic $\tau$ it is smooth of dimension $d_s(\mathfrak s)$, provided it has no zero-section pairs (FL2a Prop. 2.16). That proviso holds for $w$ good, $b^+>0$ and a generic metric (FL2a Rem. 2.14).
- *Level formula.* Apply these results to $\mathfrak t(\ell)$, together with FL2b Lemma 3.32 ((3.63)–(3.64)) and Memoir (2.3.14). Then
$$M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)\subset I\mathcal M_{\mathfrak t}\iff\ell=\ell(\mathfrak t,\mathfrak s)\in\mathbb Z_{\ge0}.$$
  Equivalently $\ell=\tfrac18(d_a-2r(\Lambda,c_1(\mathfrak s)))$ (FL2b Rem. 3.36 and (4.56)). Only finitely many $\mathfrak s$ with $M_{\mathfrak s}\ne\emptyset$ occur.
- *Expected codimension.* By Memoir (2.3.23)–(2.3.24), the expected codimension of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in $\bar{\mathcal M}_{\mathfrak t}$ is $2n_s(\mathfrak t(\ell),\mathfrak s)+2\ell$.

**What is proved about the lower strata.**
- Every reducible point of $\bar{\mathcal M}_{\mathfrak t}$ at level $\ell$ lies in some $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ with $\ell(\mathfrak t,\mathfrak s)=\ell$.
- $M_{\mathfrak s}$ is a compact manifold.

**What is not proved.**
- That every point of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ lies in $\bar{\mathcal M}_{\mathfrak t}$. FLL1 (3.1) writes the stratum as $(M_{\mathfrak s}\times\mathrm{Sym}^\ell X)\cap\bar{\mathcal M}_{\mathfrak t}$.
- Regularity of points of $M_{\mathfrak s}$, or of $\iota(M^w_{\kappa-\ell})$, in the ambient moduli space.
  - FL2a §3.4 says the points of $M_{\mathfrak s}$ "might not be regular points of $\mathcal M_{\mathfrak t}$"; see also FL1, after Rem. 1.4.
  - At zero-section points, $H^2$ contains $\operatorname{Coker}D_{A,\vartheta}$ (FL2a Lemma 3.4).
- Any local model of $\bar{\mathcal M}_{\mathfrak t}$ near a lower-level point, except under Hyp. 7.8.1.
- Any stratified-space structure beyond the weak notion of FL2b Def. 3.2. FL2b §3 (introduction) says that "the topology near points in the lower levels of $\bar{\mathcal M}_{\mathfrak t}$ need not be locally finite … it is not known if $\mathbf L^w_{\mathfrak t,\kappa}$ is triangulable and thus it may not have a fundamental class".
- The descriptions of $\bar{\mathcal M}_{\mathfrak t}/S^1$ as a "smoothly-stratified cobordism" (Overlap §§1, 2.4; FL6 §3) are exposition, not theorems.

---

## (c) Links of the instanton and Seiberg–Witten strata

**(c1) Instanton stratum.**

*Definition and properties.*
- FL2a Def. 3.7 (= Memoir (2.2.3)): $\mathbf L^{w,\varepsilon}_{\mathfrak t,\kappa}=\{[A,\Phi,\mathbf x]\in\bar{\mathcal M}_{\mathfrak t}/S^1:\ \|\Phi\|^2_{L^2}=\varepsilon\}$.
- FL2a Lemma 3.8: for generic $\varepsilon$ the link is closed, $S^1$-invariant and smoothly stratified, of codimension one in each stratum it meets. The function $\|\Phi\|^2$ is continuous by FL1 Lemma 4.4.
- FL2a Rem. 3.9: the link is not globally $\mathbb P(\operatorname{Ker}D)$, because $\operatorname{Ker}D_{A,\vartheta}$ jumps.
- FL2a (after Cor. 3.6): the link "might not have a fundamental class".

*Local evaluation.* FL evaluate the link only after cutting down to finitely many points of $M^w_\kappa$.
- FL2b Lemma 3.22: near $\bar{\mathcal V}(z)\cap M^w_\kappa=\{[\hat A_i]\}$, the intersection $\bar{\mathcal V}(z)\cap\mathbf L^{w,\varepsilon}_{\mathfrak t,\kappa}$ lies in the disjoint union of the charts of FL2a Cor. 3.6.
- FL2b Lemmas 3.25–3.27: there it is cobordant to a submanifold $T\subset\mathbb P(\operatorname{Ker}D_{A,\vartheta})\cong\mathbb{CP}^{n_a+c-1}$, Poincaré dual to $h^c$, where $c=\dim_{\mathbb C}\operatorname{Coker}D_{A,\vartheta}$. The obstruction bundle is $\mathcal O(1)^{\oplus c}$.
- FL2b Lemma 3.24 compares the orientations.
- FL2b Lemma 3.28: $\mu_c$ restricts to $2h$, because the circle acts with weight two.
- Each point therefore contributes $\langle(2h)^{n_a-1}h^c,[\mathbb{CP}^{n_a+c-1}]\rangle=2^{n_a-1}$.

> **FL2b, Proposition 3.29 (eq. (3.60)).** Let $w$ be good, $d_a\ge0$, $n_a>0$, $\deg z+2\delta_c=d_a+2n_a-2$ and $\deg z\ge d_a$, with $z$ intersection-suitable. Orient the link as the boundary of $\mathcal M^{*,\ge\varepsilon}_{\mathfrak t}/S^1$, with $O^{\rm asd}(\Omega,w)$. Then for generic small $\varepsilon$,
> $$\#\big(\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{\delta_c}\cap\mathbf L^{w,\varepsilon}_{\mathfrak t,\kappa}\big)=\begin{cases}2^{n_a-1}\#(\bar{\mathcal V}(z)\cap\bar M^w_\kappa),&\deg z=d_a,\\0,&\deg z>d_a.\end{cases}$$
> The standing hypotheses are $X$ closed, $b_2^+>0$, and a generic metric and parameters. There is no hypothesis on $\operatorname{Coker}D$.

*Not proved.* Memoir Rem. 2.6.1 asserts a value for $n_a\le0$, without proof.

**(c2) Seiberg–Witten strata at level zero (unconditional).**

*Kuranishi model.*
- FL2a Thm. 3.19: there is a finite-rank $S^1$-equivariant stabilizing bundle $\Xi$ over a neighbourhood of $\iota(M_{\mathfrak s})$. A stabilizing bundle is used, rather than the cokernel, because the cokernel can jump.
- FL2a Def. 3.20 defines the thickened moduli space $\mathcal M_{\mathfrak t}(\Xi,\mathfrak s)$ and the virtual normal bundle $N_{\mathfrak t}(\Xi,\mathfrak s)\to M_{\mathfrak s}$.
- FL2a Thm. 3.21:
  - the thickened space is regular;
  - $M_{\mathfrak s}$ is a submanifold of it, with normal bundle $N$;
  - the section takes values in $\Xi$ and is transverse off $M_{\mathfrak s}$.
  
  Hence the obstruction zero set is homeomorphic to a neighbourhood of $\iota(M_{\mathfrak s})$ (Memoir (2.3.22)).

*The link and its homology class.*
- FL2a Def. 3.22: $\mathbf L_{\mathfrak t,\mathfrak s}=\boldsymbol\gamma\big(\boldsymbol\varphi^{-1}(0)\cap\mathbb PN_{\mathfrak t}(\Xi,\mathfrak s)\big)$.
- FL2a Lemma 3.23 and (3.48): $[\mathbf L_{\mathfrak t,\mathfrak s}]=e(\boldsymbol\gamma^*\Xi/S^1)\cap[\mathbb PN]$.

*Cohomology on the link.*
- FL2b Lemma 4.8: $\mu_c\mapsto\nu=c_1(\mathcal O(1))$, not $2h$. The fibres of $N$ carry the action FL2a (3.2), which has weight two relative to scalar multiplication.
- FL2b Cor. 4.7 ((4.19)): $\boldsymbol\gamma^*\mu_p(h)=\tfrac12\langle c_1(\mathfrak s)-\Lambda,h\rangle(2\mu_{\mathfrak s}(x)+\nu)-2\sum_{i<j}\langle\gamma_i^*\gamma_j^*,h\rangle\mu_{\mathfrak s}(\gamma_i\gamma_j)$.
- FL2b Lemma 4.9: $e=\nu^{r_\Xi}$.
- FL2b Lemma 4.11 computes the Segre classes. The printed lower limit $j=1$ should be $j=0$.

*Evaluation.* FL2b Thm. 4.13 ((4.30)) evaluates the pairing explicitly: $SW$ times a Jacobi-polynomial constant times $\langle c_1(\mathfrak s)-\Lambda,h\rangle^{\delta_2}$.

*Hypotheses.* A splitting of $\mathfrak t$, and no zero-section pairs in $M_{\mathfrak s}$. The explicit Segre classes also need $\alpha\smile\alpha'=0$ on $H^1$.

**(c3) Level one (conditional on FLL1 Thm. 3.8).**
- *The link.* FLL1 (3.79) defines $\bar{\mathbf L}_{\mathfrak t',\mathfrak s}=\boldsymbol\gamma\big(\boldsymbol\chi^{-1}(0)\cap\bar{\mathbf L}^{\rm stab}_{\mathfrak t',\mathfrak s}\big)$. The virtual link is the boundary of $N(\varepsilon)\times_{\mathcal G_{\mathfrak s}}\bar{\mathrm{Gl}}(\delta)$.
- *Classes on the link.*
  - Lemma 4.2: $\mu_c\mapsto-\nu$.
  - Lemma 4.10: $\mu_p$, which now has a bubble term $\pi_X^*\mathrm{PD}[h]$.
  - Lemmas 4.11–4.12: the Euler classes $(-\nu)^{r_\Xi}$ and $\tfrac12(\pi_X^*c_1(\mathfrak t)-\nu)$.
- *Evaluation.* Duality is Prop. 5.2. The instanton factor is Lemma 5.24; its proof rests on Leness's wall-crossing paper, which is not among the sources. The pairing is Thm. 6.1.
- *Status.* All of this rests on Thm. 3.8, which is attributed to "[FL3, FL4]". FL4 (*Surjectivity of gluing maps*) is listed as "in preparation" in every source that cites it, and the 2018 Memoir no longer cites it.

**(c4) Level $\ell\ge1$ (Memoir).**
- *Definition.* Def. 8.1.3: $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}=\bar{\boldsymbol\chi}^{-1}(0)\cap\bar{\mathbf L}^{\rm vir}_{\mathfrak t,\mathfrak s}$, where $\bar{\boldsymbol\chi}$ is the obstruction section of Hyp. 7.8.1.
- *Statements about the virtual space, proved without the gluing hypothesis.* (Prop. 8.2.1 takes its constants from Lemma 8.1.4, whose genericity condition refers to $\bar{\boldsymbol\chi}$.)
  - Lemma 8.1.2: the virtual link is the boundary of a neighbourhood of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in the space of global splicing data. It is Whitney stratified, with collared top strata.
  - Prop. 8.2.1, Lemma 8.2.3 and Prop. 8.3.1: the virtual link splits into pieces. Each piece fibres over $N/S^1\times K_j$ (or, after retraction, over $M_{\mathfrak s}\times K_j$), with fibre a truncated product of instanton moduli spaces with spliced ends.
  - Lemma 9.5.1: the background Euler class is $(-\nu)^{r_\Xi}$.
  - Prop. 9.5.7: the instanton Euler class is a universal polynomial, not computed for $\ell\ge2$.
  - Prop. 9.7.3: Segre-class reduction to the base.
- *Statements conditional on Hyp. 7.8.1.*
  - Lemmas 8.1.4–8.1.5: the link bounds a neighbourhood in $\bar{\mathcal M}_{\mathfrak t}/S^1$, and the cut-down intersections are finite and lie in the top stratum.
  - Prop. 9.1.1 (duality).
  - Thms. 10.1.1–10.1.2.

---

## (d) Gluing at reducibles and the overlap problem: logical status

**Proved.**
1. **Top level.** FL2a Thms. 3.19 and 3.21 give the Kuranishi model at a top-level Seiberg–Witten stratum, where no bubbles occur. Within the sources this is the only gluing-type statement at reducibles that is proved in full.
2. **FL3 Thm. 1.1, the existence half of local gluing.**
   - *Hypotheses:*
     - $b^+>0$ and generic parameters;
     - no SO(3) bundle with $w_2\equiv w$ carries a flat connection;
     - $\kappa\ge1$ and $0<\ell<\lfloor\kappa\rfloor$;
     - a single smooth stratum $\Sigma\subset\mathrm{Sym}^\ell(X)$;
     - backgrounds in a precompact set $\mathcal U_{\ell,\mu}$ of a thickened space, defined by a small-eigenvalue cut-off $\mu$ with a uniform spectral gap;
     - the fibre uses genuine centred instantons on $S^4$ (no ideal ones), with separated points.
   - *Conclusion:* $\boldsymbol\gamma_{\mu,\Sigma}(\boldsymbol\chi_{\mu,\Sigma}^{-1}(0))\subset M^{*,0}(\mathfrak t)$.
   - *What is missing, by FL's own account.*
     - FL3 §1.5.1 calls the result "at most the first half" of a gluing theorem. It lists three properties as not proved: Uhlenbeck continuity, the embedding property, and surjectivity onto open sets covering $\bar M(\mathfrak t)$.
     - FL3 Prob. 1.5: no uniform $\mu$ exists near a positive-dimensional $M_{\mathfrak s}$, because of spectral flow.
     - It is never stated that reducible backgrounds satisfy the literal hypotheses.
     - The metric is fixed throughout. FL3 §9.3 explains why long-cylinder models are avoided.
3. **The overlap problem for splicing maps (Memoir Chs. 5–7).**
   - *Results.*
     - Thm. 5.1.1: instanton moduli spaces with spliced ends on $S^4$.
     - Thm. 6.6.1: images of the crude splicing maps for two partitions are disjoint unless the partitions are comparable, and the overlaps are governed by explicit maps between gluing data.
     - Lemma 6.6.4 and Cor. 6.6.5: the space of global splicing data $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}$, fibred over $N_{\mathfrak t(\ell),\mathfrak s}(\delta)$.
     - Thm. 7.6.1 and Lemmas 7.6.3, 7.7.1: obstruction pseudo-bundles compatible with the overlaps.
   - *Caveats.*
     - Prop. 6.8.1 (the global splicing embedding) is asserted after a sketch ("technical but straightforward") with no written proof.
     - The embedding property of FL3's splicing maps is used, although FL3 §3.2 defers its proof.
     - Thm. 5.1.1 uses anti-self-dual gluing on $S^4$ and, for the embedding property, the book in preparation.
4. **The overlap paper.**
   - It defines the overlap problem in §§1 and 4. For $\ell\ge2$ several local gluing maps are needed. Their gluing perturbations come from an implicit function theorem, so $\boldsymbol\gamma_\Sigma^{-1}\circ\boldsymbol\gamma_{\Sigma'}$ cannot be computed.
   - The proposed solution imposes Def. 1.2 (local cone-bundle neighbourhoods with Thom–Mather control and compatible structure groups) on *splicing* images. This is Thm. 4.1, an exposition of the Memoir.
   - "When $\ell=1$, Theorem 3.1 is all we need" (§4).
5. **FL19.**
   - Thm. 3 and Cors. 4–7 give a $C^1$ gluing chart near one boundary point, for anti-self-dual connections with one bubble.
   - It covers no SO(3) monopoles, no several bubbles and no overlaps.
   - The arXiv source contains comments marking the proofs as unfinished. The written proof of Thm. 3 checks only the transversality hypothesis at the boundary point.

**Assumed (no proof in the sources).**
- **Memoir Hyp. 7.8.1.** It asks for the following.
  - A continuous $S^1$-equivariant embedding $\boldsymbol\gamma_{\mathcal M}:\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}\to\bar{\mathcal C}_{\mathfrak t}$, homotopic through such embeddings to the global splicing map and equal to the identity on $N_{\mathfrak t(\ell),\mathfrak s}(\delta)\times\mathrm{Sym}^\ell(X)$.
  - Sections $\boldsymbol\chi_s$, $\boldsymbol\chi_i$ of the background and instanton obstruction pseudo-bundles, with four properties:
    - (1) smooth on each stratum;
    - (2) vanishing transversely on each stratum;
    - (3) with lower-semicontinuous $L^2$ norm;
    - (4) $\boldsymbol\gamma_{\mathcal M}$ maps their common zero set homeomorphically onto an open neighbourhood of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in $\bar{\mathcal M}_{\mathfrak t}$.
  - Memoir §7.9 says that FL3's method "does not apply without significant modification" near a positive-dimensional $M_{\mathfrak s}$. The proof is referred to a book "in preparation".
- **FL6 Hyp. 3.1 (with Rem. 3.3).** FL3's local gluing map continuously parametrizes a neighbourhood of $M_{\mathfrak s}\times\Sigma$, for each stratum $\Sigma$; this means continuity, injectivity and surjectivity. FL6 says the global assembly is done in the Memoir; there it is built into Hyp. 7.8.1.
- **Overlap Thms. 4.2 and 3.1.** Thm. 4.2 is the global gluing theorem with stratumwise transversality; the text says it "will appear in [FL4]". Thm. 3.1 is asserted to follow from FL3 but exceeds FL3 Thm. 1.1.
- **FLL1 Thm. 3.8**, the level-one gluing theorem.
- **Memoir Hyp. 11.3.5.** The same kind of hypothesis at *reducible anti-self-dual* connections $[A]\times\mathrm{Sym}^\ell(X)$, in a path of metrics with $b^+=1$. This is FL's only treatment of gluing at reducible zero-section configurations.

**Logical status.**
- *Unconditional:* FL1; FL2a; and the top-level results of FL2b (Prop. 3.29, Thm. 3.33, Thm. 4.13).
- *Conditional on Hyp. 7.8.1:*
  - Memoir Thm. 1;
  - Thm. 8.1.9, whenever a stratum of level $\ell\ge1$ enters;
  - Thms. 10.1.1–10.1.2, Prop. 10.6.1 and Lemma 10.6.2;
  - the consequences the Memoir lists. These are Witten's conjecture for Seiberg–Witten simple type (arXiv 1408.5085), superconformal simple type (1408.5307), and Kronheimer–Mrowka's use of the formula in their Property P paper. Property P itself has an independent proof (FL6 Rem. 3.4).
- *Conditional on FL6 Hyp. 3.1:* FL6 Thm. 3.2 and Main Thm. 1.2.
- *Conditional on FLL1 Thm. 3.8:* FLL1 Thm. 6.1.
- *Conditional on Hyp. 11.3.5:* Memoir Thm. 11.6.1 (Kotschick–Morgan), although it is stated without proviso.
- No source glues SO(3) monopoles across long necks or over multi-parameter families of metrics. No source proves any case $\ell\ge1$ of the SO(3)-monopole gluing hypothesis.

---

## (e) The analogue our argument needs

The argument is the manuscript's (its §§8–10), as reorganized in `exposition.tex`. Names in typewriter font are the manuscript's LaTeX labels.

### (e1) Setting, in FL's notation

**Topology.**
- $X$ is closed and oriented, with $H_1(X;\mathbb Z)=0$ and $b^+(X)\ge1$ (no parity condition).
- Disjoint separating 3-spheres $J_1,\dots,J_n$ give $X=\hat Z_0\#\cdots\#\hat Z_n$.
- The outer pieces contain the caps $C_\pm$. The caps carry fixed generic metrics and classes $A_\pm$ with $A_\pm^2=0$ and $\langle w_0,A_\pm\rangle$ odd. Each cap is blown up once more, with exceptional class $E_\pm$.
- Each inner piece is either negative definite or diffeomorphic to $\mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2$. There are $m$ pieces of the second kind (the *positive* pieces).
- There are embedded spheres $S_i$ with $S_i^2=-4$. $S_i$ meets $J_i$ in a circle and misses $J_j$ for $j\ne i$.
- $[S_i]=F_{l,i}-F_{r,i}$, where $F_{l,i}\in H_2(\hat Z_{i-1})$ and $F_{r,i}\in H_2(\hat Z_i)$ have square $-2$.
- The tubular neighbourhoods $N_i$ are disjoint, with $\partial N_i\cong L(4,1)$.

**Metrics.** $Q=[-1,1]^n$ carries metrics $g_t$ with these properties.
- As $t_i\to-1$, a round neck $J_i\times[-T,T]$ is stretched.
- As $t_i\to+1$, a neck $\partial N_i\times[-T,T]$ is stretched, with a fixed metric of positive scalar curvature on $\partial N_i$.
- The family is a product near the faces and corners.
- All other necks stay bounded.

**Spin$^u$ structures and $w_2$.**
- For $e\in\{0,1\}^n$ let $\mathfrak t_e=(\rho,W\otimes E_e)$ with $w_e=w_0+\sum_ie_i\mathrm{PD}[S_i]$, $\Lambda_e=c_1(W^+)+w_e$ and $p_1(\mathfrak t_e)=-4\kappa$, where $\langle w_0,S_i\rangle=0$ and $\langle\Lambda_0,S_i\rangle=2$.
- Then $\Lambda_e^2=\Lambda_0^2$, so $d_a$ and $n_a$ do not depend on $e$.
- **The $w_2(\mathfrak t_e)$ are pairwise distinct.**
  - Since $H_1=0$, $H^2(X;\mathbb Z/2)=\bigoplus_jH^2(\hat Z_j;\mathbb Z)\otimes\mathbb Z/2$.
  - A class of square $-2$ is not divisible by $2$, so each $F_{l,i}$ and $F_{r,i}$ is nonzero mod $2$.
  - Suppose $\sum_{i\in I}\mathrm{PD}[S_i]\equiv0$. The $\hat Z_0$-component is $F_{l,1}$ if $1\in I$, so $1\notin I$. Inductively, the $\hat Z_j$-component then reduces to $[j+1\in I]\,F_{l,j+1}$, so $j+1\notin I$. Hence $I=\emptyset$.
- So the sum below runs over $2^n$ *distinct* SO(3) bundles with common $p_1$, not over the integral lifts of one $w_2$, to which Memoir (2.5.3) would apply. (On the cobordism $W'$ itself $\mathrm{PD}[S]=2y$ is even; that is a separate statement.)
- Every $w_e$ is good, since $\langle w_e,A_\pm\rangle$ is odd and $H^2(X;\mathbb Z)$ is torsion-free.

**Classes and representatives.**
- $z=z_C\cdot S_1\cdots S_n\in\mathbb A(X)$, where $z_C$ is a monomial in point and surface classes of the caps, and $\deg z=d_a+n$.
- $\bar{\mathcal V}(z)=\bar{\mathcal V}(z_C)\cap\bigcap_i\mathcal V(S_i)$. Here $\mathcal V(S_i)$ is Donaldson's jumping-line divisor $\{E|_{S_i}\not\cong\mathcal O\oplus\mathcal O\}$; the manuscript instead uses a holonomy representative.
- The $\eta=n_a-1$ sections of $\mathbb L_{\mathfrak t_e}$ are built from spinor values sampled on several pieces. FL2b Lemma 3.13 instead uses a single ball, and that construction degenerates at faces.

**Equations and perturbations.** These are the equations of Memoir (2.1.10) for each $g_t$, with small perturbations of FL1's holonomy type. They are of two kinds.
- *Single-piece terms*, depending only on that piece's parameters.
- *Coupled terms*, sampling several pieces. They are supported where the sampled data have finite isotropy, so they vanish near circle-fixed configurations and near reducible zero-section ones. Finitely many of them are multivalued, with rational weights.

All terms on $X\setminus N_i$ agree for $e$ and $e^{(i)}$, where $e^{(i)}$ is $e$ with $e_i$ replaced by $1-e_i$.

**The invariant.**
$$\Omega=\sum_e\varepsilon(e)\,\#\big(\bar{\mathcal V}(z)\cap M^{w_e}_\kappa(Q)\big),\qquad M^{w_e}_\kappa(Q)=\bigsqcup_{t\in{\rm int}\,Q}M^{w_e}_\kappa(g_t).$$
- $M^{w_e}_\kappa(Q)$ is oriented by $o(\Omega,w_e)$ and the orientation of $Q$.
- $\varepsilon(e)=\prod_i\varepsilon_i(e_i)$ with $\varepsilon_i(1)=-s_i\varepsilon_i(0)$, where $s_i$ compares the orientations of the two minimal trace caps on $N_i$.
- $\Omega$ is the family analogue of $D^w_X(z)$ (Memoir (2.5.2)).
- Its finiteness, its invariance, and the non-vanishing $\Omega\not\equiv0\bmod 2^N$ are the manuscript's; they lie outside FL.

**The cut-down free space.**
$$\mathcal Z_e=\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{\,n_a-1}\cap\mathcal M^{*,0}_{\mathfrak t_e}(Q)/S^1,\qquad\dim\mathcal Z_e=(d_a+2n_a+n-1)-(d_a+n)-2(n_a-1)=1 .$$
This is the family form of the one-manifold FL2b (3.62), with "$\deg z=d_a$" replaced by "$\deg z-\dim Q=d_a$".

### (e2) The compactification over $\bar Q$

**Ideal tuples.** Fix a point of an open face where the necks $J_i$ ($i\in\mathcal J$) and $\partial N_i$ ($i\in\mathcal N$) are infinitely long, and put $k=|\mathcal J|$. An *ideal tuple* consists of:
- on each main piece $P_0,\dots,P_k$ of $X\setminus(\bigcup_{\mathcal J}J_i\cup\bigcup_{\mathcal N}N_i)$, completed by half-cylinders, an ideal SO(3) monopole $[A_j,\Phi_j,\mathbf x_j]$ of finite energy, exponentially asymptotic to flat connections with $\Phi=0$;
- on each completed cap $\hat N_i$, an ideal anti-self-dual connection. Its spinor vanishes by the Weitzenböck formula.
- on each infinitely long neck, a finite chain of non-constant anti-self-dual connections on $\mathbb R\times J_i$ or $\mathbb R\times\partial N_i$, with zero spinor.

The flat limits must match, and the total charge is $\kappa$.

**Flat limits and charges.**
- On $S^3$ the only flat connection is the trivial one, with stabilizer SO(3).
- On $L(4,1)$ there are two central flats, with stabilizer SO(3), and one with trace-zero holonomy, with stabilizer U(1).
- All have $H^1=0$ and invertible Dirac operator.
- Ideal points and $S^3$-trajectories carry positive integer charges. Lens data carry charges in $\tfrac14\mathbb Z$.

**Kinds of main component.**
- *free*: connection irreducible and $\Phi\not\equiv0$; FL's $\mathcal M^{*,0}$.
- *anti-self-dual*: $\Phi\equiv0$ and $\hat A$ irreducible; FL's $\iota(M^w)$.
- *Seiberg–Witten*: reducible for some $V=W'\oplus W'\otimes L$, with $\Phi=\Psi\oplus0\not\equiv0$; FL's $\iota(M_{\mathfrak s})$.
- *reducible zero-section*: $\Phi\equiv0$ and $\hat A=d_{\mathbb R}\oplus A_L$, i.e. an abelian anti-self-dual connection.

(The manuscript's letters for these are $P,A,S,R$.)

**Levels of reducible components.** Write $v_j=c_1(L_1)-c_1(L_2)$, so $c_1(\mathfrak s_j)=\Lambda+v_j$. Fill the lens ends by the reference abelian connections. Then
$$\kappa_j=-\tfrac14v_j^2+\ell_j,\qquad \ell_j\in\mathbb Z_{\ge0}.$$
$\ell_j$ collects the ideal points, the trajectory charge and the excess cap charge. For $k=0$ with no lens face it is $\ell(\mathfrak t_e,\mathfrak s)$ of Memoir (2.3.14).

**Bubbles and reducible pieces.**
- Bubbles and neck chains are irreducible. There is no non-flat finite-energy abelian anti-self-dual connection on $S^4$, $\mathbb R\times S^3$ or $\mathbb R\times L(4,1)$.
- The spinor does not bubble (the $C^0$ bound of FL1 Lemma 4.4).
- So reducible pieces appear only in three ways:
  - as separated caps;
  - as components between $J$-cuts;
  - as reducible backgrounds of SU(2) bubbles. These are FL's $M_{\mathfrak s}\times\mathrm{Sym}^\ell$ and its zero-section analogue.

**Index identities.** Let $p_j$ be the interval parameters retained on component $j$, with one restored for each lens end. Let $s_j$ be the sphere classes assigned to component $j$; at a $J$-cut the class goes to the side carrying the event. Let $z_j$ be its cap degree. With ends filled as above, put
$$q_j=d_a(\mathfrak t_j)+p_j-2s_j-z_j,\qquad i_j=q_j+2n_a(\mathfrak t_j).$$
Then
$$\sum_j(q_j+4)=4,\qquad\sum_ji_j-2\eta=2-4k .$$
Each $J$-cut costs 3 for the SO(3) gluing parameter and 1 for the lost interval parameter.

**Losses.**
- An ideal point of charge $a$ lowers $d_a$ by $8a$ and $d_a+2n_a$ by $6a$, and it restores at most $4a$ dimensions.
- A separated lens costs $\delta_I-1$ in the instanton count and $\delta_{\rm sp}-1$ in the monopole count, both at least $1$.
  - At a central flat the costs are $\ge7$ and $\ge5$.
  - At the trace-zero flat with cap charge $\tfrac14+h$, the monopole cost is $\delta_{\rm sp}-1=1+6h$.

### (e3) Statements

> **Theorem E (family SO(3)-monopole cobordism, vanishing form).** Let the data be as in (e1), with $n_a\ge1$ and with generic perturbations and representatives in the class described. Assume:
> 1. *(instanton points)* $\mathcal I_e:=\bar{\mathcal V}(z)\cap\bar M^{w_e}_\kappa(\bar Q)$ is a finite set of regular points of the parametrized cut-down anti-self-dual problem. It lies in the top stratum over ${\rm int}\,Q$, and $D_{A,\vartheta}$ is onto at each of its points.
> 2. *(exclusion)* For every $e$, $\bar{\mathcal Z}_e\setminus\mathcal Z_e$ consists only of the points $\iota(\mathcal I_e)$ and of *minimal lens tuples*. A minimal lens tuple lies over a face with exactly one coordinate $t_i=+1$ and no other coordinate equal to $\pm1$. It consists of a free main component on $X\setminus N_i$ with no ideal points, together with the reducible anti-self-dual connection of charge $\tfrac14$ on $\hat N_i$ asymptotic to the trace-zero flat, with no ideal points and no trajectories.
>
> Truncate $\sum_e\varepsilon(e)\mathcal Z_e$ at $\{\|\Phi\|^2_{L^2}<\varepsilon\}$ near $\iota(\mathcal I_e)$ and at neck length $>D$ near the minimal lens tuples. For generic small $\varepsilon$ and large $D$ the result is a compact oriented one-dimensional branched manifold with rational weights. Its boundary is as follows.
> - Near $\iota(\mathcal I_e)$ there are $2^{n_a-1}$ points for each instanton, with total $\sigma_0\,2^{n_a-1}\,\Omega$, where $\sigma_0=\pm1$ does not depend on $e$.
> - At the minimal lens tuples there is one collar end for each main solution and each cap crossing. The ends for $e$ and $e^{(i)}$ over the same main solution cancel after weighting by $\varepsilon(e)$.
>
> Hence $2^{n_a-1}\Omega=0$ in $\mathbb Q$, and so $\Omega=0$.

**Relation to FL.**
- For $n=0$ (closed $X$, fixed generic metric), Theorem E is FL2b Thm. 3.33(a) in cut-down form. FL's hypothesis (3.68), that $\bar{\mathcal M}_{\mathfrak t}$ contains no reducible at any level, is weakened to hypothesis 2, that the closure of the cut-down space contains none.
- The proof is FL's: Stokes, Prop. 3.29 at the instanton ends, and Cor. 3.18 (here, the loss count) at the free lower strata.
- Theorem E is not a family form of Memoir Thm. 1 or Thm. 8.1.9: no reducible stratum is linked or evaluated.
- Hypothesis 1 is arranged by perturbation. If $\operatorname{Coker}D_{A,\vartheta}\ne0$ were allowed, FL2b Lemma 3.27 would give the same count.

> **Proposition E′ (exclusion).** Hypothesis 2 of Theorem E holds if the following conditions are satisfied.
> 1. **(single-component regularity)** Every anti-self-dual component, with its retained parameters and cuts, is regular, so $q_j\ge0$, strictly if it has any loss. Every Seiberg–Witten component is regular for its own Seiberg–Witten problem, so $d_s(\mathfrak s_j)+p_j+4\ell_j\ge0$.
> 2. **(incidence)** The representatives $\mathcal V(S_i)$ satisfy four conditions.
>    - (a) They represent $\pm\mu_p(S_i)$.
>    - (b) A connection that is reducible along $S_i$ with split class $v$ lies in $\mathcal V(S_i)$ if and only if $\langle v,[S_i]\rangle\ne0$.
>    - (c) Membership persists under Uhlenbeck limits unless an ideal point lies on $S_i$. Distinct $S_i$ need distinct ideal points.
>    - (d) At $t_i=-1$, $\mathcal V(S_i)$ splits into half-representatives of $F_{l,i}$ and $F_{r,i}$. At $t_i=+1$ it is a condition on $\hat N_i$.
>
>    All representatives obey the loss count of (e2).
> 3. **(Seiberg–Witten localization, uniformly over $\bar Q$)** On every face, every Seiberg–Witten or reducible zero-section configuration on a union of consecutive pieces satisfies three conditions.
>    - *The chamber condition on positive pieces:* $(v\cdot H)(c_1(\mathfrak s)\cdot H)<0$, respectively $v\cdot H=0$, for the periods $H$ of the toric metrics. The manuscript's Theorem `estimates:clamp` extends this over the hull of the vertex classes $H_I$.
>    - $\langle v,U\rangle=0$ near the cusp.
>    - On a piece containing a cap there is no reducible zero-section configuration, and $v_W^2,(\Lambda_W+v_W)^2\le C_W$.
> 4. **(numerics)** Positive pieces are at mutual distance $\ge4$ and at distance $\ge L_*$ from the caps. $\langle\Lambda_0,E_\pm\rangle$ is odd and large. $3n-7m>C_0$.
> 5. **(projected regularity)** Call a tuple of main components a *candidate* if the components solve their equations and retained cuts, are given admissible charges for the omitted caps and trajectories, and are not required to match. Let a candidate contain a free component. Delete its reducible zero-section components, their ideal points and their cuts, but keep their parameters. The resulting problem must be Fredholm, with finite isotropy for the common circle, independent of the deleted data, and transverse near the projections of all candidates. In particular it must be fully regular at its Seiberg–Witten and anti-self-dual components.

**Mechanism.** The arithmetic input is the manuscript's family adjunction inequality. For an abelian configuration on consecutive pieces $\Gamma$,
$$\kappa_\Gamma\ge\tfrac12\big(s^-(\Gamma)+m(\Gamma)\big),$$
where $s^-$ counts the assigned spheres not adjacent to positive pieces. This is a lattice statement, checked by machine and sharp. Every actual limit is a candidate in the sense of condition 5, so excluding candidates suffices, and no stratum is ever parametrized. The cases are as follows.
- *Unbroken Seiberg–Witten limits, at every level $\ell\ge0$.* Incidence gives $\ell\ge T(v)$, the number of spheres met only through ideal points. The inequality gives $-\tfrac14v^2+T(v)\ge\tfrac12(n-m)-C$. With $8\kappa=n+3m+c$, this forces $\ell-T(v)\le\tfrac18(7m-3n)+C'<0$. No regularity is used.
- *Unbroken reducible zero-section limits.* Excluded by the cap: $\langle w_0,A\rangle$ odd forces $v\ne0$ on the cap, and the generic cap period, with long isolation necks, prevents $v$ from being anti-self-dual.
- *Broken tuples with no free component.* Let $a$ be the number of anti-self-dual components, each contributing at least $4$ to $\sum(q_j+4)$, and $b\le2$ the number of outer Seiberg–Witten components, each contributing at least $8$. Then $a+b\ge2$. There are at most $a+b-1$ maximal runs of consecutive reducible components between them, and each contributes at least $-2$ at spacing $\ge3$. Hence $\sum(q_j+4)\ge2a+6b+2\ge6$, which contradicts the identity $\sum(q_j+4)=4$.
- *Tuples with a free component.*
  - Write $N$ for the number of main components that are not reducible zero-section components. The projected dimension is at most
$$5-4N-\sum_{\rm runs}\sum_{j\in\text{run}}(4+i_j-p_j)-(\text{losses}).$$
    Each run contributes at least $-2$ at spacing $\ge4$. At spacing $3$ a run can contribute $-5$, so the bound fails there.
  - For $k\ge1$ the outer components are never reducible zero-section components (by the caps), so $N\ge2$, there are at most $N-1$ runs, and the projected dimension is at most $5-4N+2(N-1)=3-2N<0$.
  - For $k=0$ it is at most $1-N_{\rm lens}-2w$, which leaves only the unbroken free stratum and the minimal lens tuples.

### (e4) Strata to be excluded

| Stratum meeting the closure of the cut-down space | FL counterpart | Exclusion | Regularity used |
|---|---|---|---|
| free component with ideal points (lower level), any face | $\mathcal M^{*,0}_{\mathfrak t(\ell)}\times\Sigma$; FL2b Cor. 3.18 | loss of $6$ per unit charge, at most $4$ regained | free strata |
| anti-self-dual components other than $\iota(\mathcal I_e)$ (lower level, faces, lens ends) | $\iota(M^w_{\kappa-\ell})\times\Sigma$; FL2b Lemma 3.21 | $q_j\ge0$, strict with loss, against $\sum(q_j+4)=4$ | anti-self-dual components |
| $J$-faces, all components free or anti-self-dual | none (no necks in FL) | $\sum i_j-2\eta-1=1-4k<0$ (Donaldson's connected-sum count) | those components |
| lens faces other than the minimal one | none | lens cost $\delta_{\rm sp}-1$ | main component |
| unbroken Seiberg–Witten, $M_{\mathfrak s}(g_t)\times\mathrm{Sym}^\ell(X)$, every $\ell\ge0$, interior and lens faces | ends of Memoir Thm. 8.1.9 (links; Hyp. 7.8.1 for $\ell\ge1$); hypothesis (3.68) of FL2b Thm. 3.33(a) | incidence and the adjunction inequality | none |
| unbroken reducible zero-section | excluded in FL by good $w$ and a generic metric (FL2a Prop. 3.1; Memoir (2.2.2)); Memoir Hyp. 11.3.5 in a path | cap class $A$ with a generic cap period, uniform over $\bar Q$ | none |
| $k\ge1$, no free component | none | $\sum(q_j+4)\ge6$ | anti-self-dual; tangential Seiberg–Witten only |
| $k\ge1$, free and Seiberg–Witten components, no reducible zero-section component | none (FL never meet Seiberg–Witten components in broken limits) | $1-4k-(\text{losses})<0$ | full regularity at Seiberg–Witten components in the coupled problem |
| $k\ge1$, free and reducible zero-section components | none; compare Memoir Hyps. 7.8.1 and 11.3.5 | projection: dimension $\le3-2N<0$ | none at the zero-section reducibles; the projected problem regular |

Two kinds of tuple are kept: the points $\iota(\mathcal I_e)$ and the minimal lens tuples.

FL's local-finiteness caveat (FL2b §3, introduction) does not arise here. The closure of $\mathcal Z_e$ meets the lower strata only at points with explicit local models. The price is that the exclusion must be exhaustive.

### (e5) Remarks

1. **The reducible strata exist.**
   - On the positive pieces, classes in the Weitzenböck band carry Seiberg–Witten solutions; wall-crossing gives $SW=\pm1$ across the band.
   - On runs of negative pieces at $J$-faces, reducible zero-section configurations exist for every parameter value.
   - What is excluded is their meeting the closure of $\mathcal Z_e$.
   - The exposition's formula "$2^{n_D-1}\Omega=-\#\{\text{abelian ends}\}$" (exposition, Theorem `thm:FL`) is not a theorem: without gluing at reducibles, abelian limits are not known to be ends of a one-manifold. Only the vanishing form, Theorem E with Proposition E′, is available, and it is all the argument uses.
2. **How $n_a>0$ is obtained.** In FL, $n_a>0$ is the hypothesis $\delta<i(\Lambda)$ of Memoir Thm. 1, which FL6 arranges by taking $\Lambda^2$ large (proof of Main Thm. 1.2). Here $\Lambda$ is constrained by $\Lambda_0\cdot S_i=2$ and by $|\Lambda\cdot H_I|\le\tfrac32$ for the vertex classes $H_I$, $I\ne\emptyset$, of the positive pieces, and $n_a=\tfrac18(5m-n)+c$ comes from topology. Enlarging $\Lambda$ would widen the band.
3. **A families Seiberg–Witten vanishing theorem would not substitute.**
   - Turning a vanishing count into vanishing ends needs gluing.
   - The invariant is undefined here, since $b^+(X)\approx n/4<\dim Q$ and walls are crossed.
4. **Coefficients.**
   - Working over $\mathbb Q$ suffices, because $\Omega$ is an integer computed from single-valued data.
   - Over $\mathbb F_2$ the identity is empty once $n_a\ge2$, so the non-vanishing must be integral.

---

## (f) Where (e) goes beyond FL

Classification: *routine extension* means known methods with no new idea, though possibly not written for SO(3) monopoles. *Substantial* means a genuine piece of analysis or geometry with no citable proof; a proof may be proposed in the manuscript. *Open* means no proof is proposed.

1. **Compactness over $\bar Q$ with neck faces of positive scalar curvature.**
   - *Extends:* FL1 Thm. 1.1, Thm. 4.20, Def. 4.19 and Lemmas 4.2–4.4; Memoir Thm. 2.1.3 and Def. 2.1.2. All of these are for a closed manifold with a fixed metric.
   - *New:*
     - cylindrical ends with flat limits whose stabilizers are SO(3) and U(1). FL have no ends, and they exclude flat connections on $X$ altogether (FL3 §1.1; FL2a Lemma 3.2);
     - neck chains and quantized charges;
     - corners of $Q$.
   - *A uniformity point.* FL1 Lemmas 4.2–4.3 depend on $\|R\|_{L^2}$, which grows with neck length, so FL1's energy bound (4.2) is not uniform as stated. One needs the standard variant in which only the negative part of $R$ enters, together with $L^2$ bounds on the fixed curvatures and the perturbations along the necks. Lemma 4.4 is uniform as stated.
   - **Routine extension.** The neck analysis is standard for anti-self-dual connections (Donaldson's Floer book; Morgan–Mrowka–Ruberman), and the spinor decays on necks of positive scalar curvature by the Weitzenböck formula. It is not written for SO(3) monopoles.
2. **Index and level bookkeeping across faces.**
   - *Content:* the identities $\sum(q_j+4)=4$ and $\sum i_j-2\eta=2-4k$, the levels $\kappa_j=-\tfrac14v_j^2+\ell_j$, and the lens corrections.
   - *Extends:* Memoir (2.1.12), (2.3.14) and (2.3.23)–(2.3.24); FL2b (3.20)–(3.25); Overlap (2.10).
   - **Routine** (Atiyah–Patodi–Singer with excision). The manuscript's lens table was not rechecked here.
3. **Single-component transversality in families.**
   - *Content:*
     - anti-self-dual components with cuts;
     - free strata at all levels;
     - tangential Seiberg–Witten regularity;
     - the Dirac operator onto at $\mathcal I_e$.
   - *Extends:* Memoir Thm. 2.1.1 (= FL2a Thm. 2.13); FL1 Thm. 1.3; FL2a Prop. 2.16.
   - **Routine.** FL never state simultaneous transversality at all levels.
4. **Instanton ends and the factor $2^{n_a-1}$.**
   - *Extends:* FL2b Prop. 3.29 with Lemmas 3.22 and 3.24–3.28; FL2a Cor. 3.6, Def. 3.7 and Lemma 3.8; Memoir (2.6.2).
   - *Changes:* the parameters $t$ become extra finite-dimensional variables; with $\operatorname{Coker}D=0$ the class $h^c$ becomes $1$; only neighbourhoods of $\iota(\mathcal I_e)$ are used, not the global link.
   - **Routine.**
5. **$J$-face ends without reducible components** ($1-4k<0$).
   - No FL counterpart.
   - **Routine**: Donaldson's dimension count for connected sums. It requires perturbations, representatives and phase sections to be local to the pieces at such faces.
6. **Representatives of $\mu_p(S_i)$ at reducible limits and at faces** (condition 2 of E′).
   - *Extends:* FL2b Lemmas 3.12, 3.15, 3.17, Def. 3.14 and Cor. 3.18. These control closures only on irreducible lower strata; at reducibles FL work through links (FL2b Cor. 4.7; FLL1 Lemma 4.10, with its bubble term).
   - **Routine** with the jumping-line divisor.
     - Property (b) is Grothendieck's theorem on $\mathbb P^1$.
     - Property (c) holds because non-invertibility of $\bar\partial$ is closed in $C^0$ and convergence is $C^0$ on $S_i$ away from ideal points.
     - Property (d), the nodal degeneration of the determinant line, still has to be written.
   - **Substantial** if the manuscript's holonomy representative is kept.
7. **Seiberg–Witten localization uniformly over $\bar Q$** (condition 3 of E′).
   - *Status relative to FL:* outside FL's scope. FL take Seiberg–Witten invariants as given and never use emptiness of Seiberg–Witten moduli spaces.
   - *Nearest FL results:* FL2a Props. 2.15–2.16; FL2b Rem. 3.36; the blow-up mechanism of Memoir §10.6, where exceptional classes push Seiberg–Witten classes to negative level.
   - *Needed:*
     - the Weitzenböck chamber estimates for toric metrics with $\mathrm{Scal}\ge0$, persisting through the degenerations at the lens faces and the corners;
     - the cap bounds;
     - the order of choices.
   - **Substantial.**
8. **Exclusion of unbroken Seiberg–Witten strata at every level, and of broken tuples with no free component.**
   - *Replaces:* the *hypothesis* of FL2b Thm. 3.33(a) by a theorem. The strata are non-empty but miss the closure of the cut-down space.
   - **Routine** given items 6 and 7. The lattice inequality has been checked by machine.
9. **Reducible zero-section configurations.**
   - *FL:* excluded by FL2a Prop. 3.1, Lemma 3.2 and Cor. 3.3, by Memoir (2.2.2) and by FL3 §2.1; met only under Memoir Hyp. 11.3.5.
   - *Here they are unavoidable* at $J$-faces, on pieces with $b^+=0$, and on walls $\langle v,H\rangle=0$ of the positive pieces, because $\dim Q=n>b^+(X)$.
   - Exclusion at $k=0$ by the caps: **routine**.
   - Exclusion in broken tuples without a free component: **routine** (item 8).
   - Exclusion with a free component: item 11.
10. **Coupled regularity in mixed tuples** (condition 5 of E′, and the phase sections).
    - *Content:* full regularity at Seiberg–Witten and anti-self-dual components, using perturbations that sample a free component. These have finite isotropy and are multivalued with rational weights.
    - *No FL counterpart:*
      - FL never regularize at Seiberg–Witten points (FL2a §3.4);
      - FL1 Thm. 1.3 excludes reducible and zero-section points (FL1 §5);
      - FL1's holonomy perturbations vanish at reducible connections (FL1 §1.1.1);
      - FL stabilize instead (FL2a Thms. 3.19, 3.21; FL3 Thm. 8.3).
    - **Substantial (new).**
11. **The projection for tuples with free and reducible zero-section components.**
    - *It replaces*, rather than extends, the step FL would need here: a gluing theorem, in families with faces, for a reducible zero-section component glued to non-abelian components across $S^3$ necks. The gluing parameter would lie in $\mathrm{SO}(3)/\mathrm{U}(1)$, and the obstructions would include the normal anti-self-dual cokernel and the Dirac cokernel. This is the face analogue of Memoir Hyp. 11.3.5 and of a Hyp. 7.8.1-type gluing at mixed strata. Neither is proved even on closed manifolds.
    - *It needs:*
      - independence of the retained equations from the deleted data;
      - item 10 for the projected problem;
      - compactness of the candidate projections, by induction over degeneration types;
      - the run bound $\ge-2$, which needs spacing $\ge4$.
    - *Proposed proof:* the manuscript's Lemma `analysis:projection`, with Lemmas `analysis:R-independence`, `analysis:samples` and `analysis:finite-data` and Prop. `analysis:finite-induction`.
    - **Substantial (new; the decisive step).** It is not open: an argument is written, and its structure checks. What is open is the gluing theorem it replaces, which is not needed.
12. **Lens faces.**
    - *Gluing and exhaustion.* The minimal trace cap has charge $\tfrac14$ and stabilizer U(1), equal to that of the flat. Its Dirac operator is invertible by positive scalar curvature. Its normal complex index is one, made onto by a perturbation vanishing at the reducible. The scalar cokernel is removed by changing the weight. **Routine** in kind (gluing at reducible flats with matching stabilizers), but nowhere written for SO(3) monopoles.
    - *The orientation comparison* that makes the $\varepsilon(e)$-weighted ends of $e$ and $e^{(i)}$ cancel: **substantial (new)**.
      - The two structures have different $w_2$.
      - FL's comparisons (FL2b Lemma 2.6, Memoir Lemma 8.1.7, Memoir (2.5.3)) concern lifts of a fixed $w_2$.
      - Kronheimer–Mrowka's sum over $w$ (FL6 Thm. 2.2) is not used.
13. **Rational weights and Stokes on weighted branched one-manifolds.**
    - *FL:* integral counts and single-valued data (FL2b Def. 3.2).
    - **Routine** (McDuff; Cieliebak–Mundet–Salamon). The conclusion is needed only over $\mathbb Q$.
14. **Not needed.**
    - Memoir Hyp. 7.8.1, FL6 Hyp. 3.1, Overlap Thm. 4.2, FL3, Memoir Thms. 10.1.1–10.1.2, FL6, and Kronheimer–Mrowka.
    - The overlap problem. It arises only when neighbourhoods of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$, $\ell\ge2$, are parametrized. Here no reducible stratum is parametrized, and the only glued ends carry no ideal points.
    - **Open but not needed:**
      - a family formula with Seiberg–Witten terms;
      - gluing at reducible zero-section components in families with faces;
      - exclusion at spacing $3$;
      - an $S^1$-equivariant SO(3)-monopole Floer theory.

**Overall judgement: the most serious gap is item 11.**
- *No counterpart in the literature.* It has none in FL or elsewhere. It does the work of a gluing theorem at reducibles, which FL never prove even for one closed manifold (Hyps. 7.8.1 and 11.3.5 remain assumptions).
- *Several new ingredients at once:*
  - perturbations independent of discarded data;
  - finite-isotropy multisections across strata where the isotropy jumps;
  - a compactness and induction argument for candidates without matching.
- *No numerical slack.*
  - The run bound is attained at spacing $3$.
  - At spacing $4$ the projected index is at most $-1$ when $N=2$. An error of one in any lens, particle or phase count would leave an unexcluded zero-dimensional stratum.
- *Next in seriousness:*
  - item 7, the uniform Seiberg–Witten localization at faces, where FL offer nothing;
  - item 12, the lens orientation comparison.
