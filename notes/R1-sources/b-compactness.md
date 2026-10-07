# (b) Uhlenbeck compactness and the lower strata of the moduli space of SO(3) monopoles: what Feehan and Leness state and prove

## 0. Sources, numbering and notation

### 0.1 Sources (arXiv LaTeX, as downloaded)

| Tag | Paper | File / version read |
|---|---|---|
| [FL1] | Feehan–Leness, *PU(2) monopoles I: regularity, Uhlenbeck compactness, and transversality* | `dg-ga_9710032/main.tex`, dated 29 October 1997 ("J. Differential Geom., to appear") |
| [FL2a] | Feehan–Leness, *PU(2) monopoles and links of top-level Seiberg–Witten moduli spaces* | `math_0007190/main.tex`, version of 9 February 2001 (Crelle) |
| [FL2b] | Feehan–Leness, *PU(2) monopoles II: top-level Seiberg–Witten moduli spaces and Witten's conjecture in low degrees* | `dg-ga_9712005/main.tex`, version of 9 February 2001 (Crelle) |
| [FL3] | Feehan–Leness, *PU(2) monopoles III: existence of gluing and obstruction maps* | `math_9907107/main.tex`, 20 July 1999 |
| [FLL1] | Feehan–Leness, *SO(3) monopoles, level-one Seiberg–Witten moduli spaces, and Witten's conjecture in low degrees* | `math_0106238/main.tex` |
| [FL5] | Feehan–Leness, *An SO(3)-monopole cobordism formula relating Donaldson and Seiberg–Witten invariants* | `math_0203047/FeehanLenessMonopoleCobordism_v4-clean.tex` (amsbook) |
| [FL6] | Feehan–Leness, *Witten's conjecture for many four-manifolds of simple type* | `math_0609530/jems-feehanleness_PF11-22-2014.tex` (JEMS version, 22 Nov 2014) |
| [FLov] | *SO(3)-monopoles: the overlap problem* | `1211.0480/main.tex` (header: "This version: March 15th, 2005. Galley corrections included: May 7th, 2005", and `\date{May 7, 2005}` [corrected by checker]; the source lists both Feehan and Leness as authors) |

Kronheimer–Mrowka's structure paper ([KMStructure], J. Differential Geom. 41 (1995), 573–734) is not on arXiv. Every statement attributed to it below is taken from the restatement in an FL paper, and I say which one. I did not check these against the original. ([corrected by checker] The bibliographies disagree on the volume: [FL5] gives 41 with MR 1338483, while [FL1] and [FL2a] print 43.)

### 0.2 How the numbers were obtained

All numbers are read off the LaTeX counters. In every paper except [FLov], theorem-like environments (Theorem, Lemma, Proposition, Corollary, Definition, Remark, Conjecture, Hypothesis, Convention and Notation) share one counter, which is reset at each section, and equations are numbered within sections. [corrected by checker] In [FLov] Proposition has its own counter (`\newtheorem{prop}{Proposition}[section]`), separate from Theorem/Lemma/Definition/Remark; no [FLov] theorem number is cited in this note, so nothing below is affected. The checker recomputed every theorem, lemma and equation number cited in this note with an independent counting script and found agreement. [FL5] is an `amsbook` with `\numberwithin{section}{chapter}`, so its numbers have the form chapter.section.item; its main theorem has a separate counter and is "Theorem 1". I computed the numbers with a counting script and checked them against cross-citations between the papers. The following agree with the computed numbers: [FL5] cites [FL1, Theorem 1.1], [FL1, Definition 4.19], [FL1, Proposition 2.8] and [FL1, Proof of Proposition 2.28]; it also cites [FL2a, Lemma 3.13], [FL2a, Theorem 3.21], [FL2a, Definition 3.7] and [FL2b, Definition 3.20]. [FL6] cites [FL1, Theorem 4.20]. [FL2b] cites [FL2a, Equations (2.44), (3.5)], and [FL6] cites [FL2a, Equation (2.33)].

Exceptions: [FL2b] cites [FL1, Theorem 1.2] for compactness, [FL1, Proposition 2.12] for the slice theorem and [FL1, Theorem 5.10] for local-to-global reducibility, whereas the arXiv source of [FL1] gives Theorem 1.1, Proposition 2.8 and Theorem 5.11. [FL2a] cites [FL1, Equation (2.37)] for the deformation complex, which is (2.44) in the arXiv source. The published J. Differential Geom. version of [FL1] is probably numbered differently. [corrected by checker] The evidence is mixed: two lines before citing "[FL1, Theorem 5.10]", [FL2b, §3.2.2] cites the same local-to-global result as "[FL1, Theorem 5.11]", and [FL2b] cites "[FL1, Lemma 5.12]" for unique continuation of the Dirac operator, which matches the arXiv source. [FL2b]'s citations of [FL1] are therefore internally inconsistent, and [FL2a] and [FL5] cite [FL1, Proposition 2.8] for the slice result, as in the arXiv source. **Every number in this note refers to the arXiv source.**

### 0.3 Two conventions

**[FL1] convention.** The data are:
- $(X,g)$, a closed, oriented, smooth Riemannian four-manifold;
- a spin$^c$ structure $(\rho,W^+,W^-)$ with a $C^\infty$ spin$^c$ connection on $W=W^+\oplus W^-$;
- a Hermitian two-plane bundle $E$ whose determinant $\det E$ carries a fixed $C^\infty$ unitary connection.

The spaces and groups are:
- $\mathcal A_E$ is the space of $L^2_k$ unitary connections on $E$ inducing the fixed connection on $\det E$ (equivalently, following [KMStructure, §2(i)], $L^2_k$ connections on the SO(3) bundle $\mathfrak{su}(E)$).
- $\mathcal G_E$ is the group of $L^2_{k+1}$ determinant-one unitary gauge transformations, and ${}^\circ\mathcal G_E:=S^1_Z\times_{\{\pm\mathrm{id}\}}\mathcal G_E$, where $S^1_Z$ is the centre of $U(2)$.
- $\tilde{\mathcal C}_{W,E}=\mathcal A_E\times L^2_k(W^+\otimes E)$ and $\mathcal C_{W,E}=\tilde{\mathcal C}_{W,E}/{}^\circ\mathcal G_E$.

Because ${}^\circ\mathcal G_E$ contains the centre, which acts on $\Phi$ by scalars, **[FL1]'s moduli space $M_{W,E}$ is the quotient by the circle action**. It corresponds to $\mathcal M_{\mathfrak t}/S^1$ in the later convention, which is why its dimension formula contains a $-1$. A connection is *irreducible* if its stabiliser in ${}^\circ\mathcal G_E$ is exactly $S^1_Z$. $M^{*,0}_{W,E}$ is the subspace where $A$ is irreducible and $\Phi\not\equiv0$. $E_{-\ell}$ denotes the bundle with $\det E_{-\ell}=\det E$ and $c_2(E_{-\ell})=c_2(E)-\ell$. From §4 onwards $k\ge 3$ is assumed.

**[FL2a]–[FL6] convention (spin$^u$).**
- A spin$^u$ structure is $\mathfrak t=(\rho,V)$, a Hermitian Clifford module of complex rank 8. $\mathfrak g_{\mathfrak t}\subset\mathfrak{su}(V)$ is the SO(3) subbundle commuting with Clifford multiplication. One has $V\cong W\otimes E$ for any spin$^c$ structure $\mathfrak s=(\rho,W)$ ([FL2a, Lemma 2.3]); then $\mathfrak g_{\mathfrak t}=\mathfrak{su}(E)$ and $\det^{1/2}(V^+)=\det W^+\otimes\det E$.
- Characteristic classes ([FL5, (2.1.6)]): $c_1(\mathfrak t)=\tfrac12c_1(V^+)$, $p_1(\mathfrak t)=p_1(\mathfrak g_{\mathfrak t})$, $w_2(\mathfrak t)=w_2(\mathfrak g_{\mathfrak t})$. FL write $\Lambda=c_1(\mathfrak t)=c_1(W^+)+c_1(E)$, $\kappa=-\tfrac14p_1(\mathfrak t)$, and $w$ for an integral lift of $w_2(\mathfrak t)$ (for example $w=c_1(E)$; see [FL6, (3.1)]).
- $A_\Lambda$ is a fixed smooth unitary connection on $\det^{1/2}(V^+)$, and $\mathcal A_{\mathfrak t}$ is the space of $L^2_k$ spin connections on $V$ inducing $2A_\Lambda$ on $\det V^+$. These correspond bijectively to SO(3) connections $\hat A$ on $\mathfrak g_{\mathfrak t}$.
- $\mathcal G_{\mathfrak t}$ is the group of $L^2_{k+1}$ unitary automorphisms of $V$ that commute with Clifford multiplication and have Clifford-determinant one. Then $\tilde{\mathcal C}_{\mathfrak t}=\mathcal A_{\mathfrak t}\times L^2_k(V^+)$ and $\mathcal C_{\mathfrak t}=\tilde{\mathcal C}_{\mathfrak t}/\mathcal G_{\mathfrak t}$.
- The circle acts on $\mathcal C_{\mathfrak t}$ by $\Phi\mapsto e^{i\theta}\Phi$, and $-1$ acts trivially ([FL5, (2.1.9)]).
- The equations, [FL5, (2.1.10)] = [FL2a, (2.32)], with $\tau$ a section of $GL(\Lambda^+)$ close to the identity and $\vartheta$ a complex one-form close to zero, are
$$\mathrm{ad}^{-1}(F^+_{\hat A})-\tau\rho^{-1}(\Phi\otimes\Phi^*)_{00}=0,\qquad D_A\Phi+\rho(\vartheta)\Phi=0.$$
(The display in [FL5, (2.1.10)] drops the $\Phi$ after $\rho(\vartheta)$; [FL2a, (2.32)] has it.)
- $\mathcal M_{\mathfrak t}\subset\mathcal C_{\mathfrak t}$ is the zero set, with subspaces $\mathcal M^*_{\mathfrak t}$ ($\hat A$ irreducible), $\mathcal M^0_{\mathfrak t}$ ($\Phi\not\equiv0$) and $\mathcal M^{*,0}_{\mathfrak t}=\mathcal M^*_{\mathfrak t}\cap\mathcal M^0_{\mathfrak t}$ ([FL5, (2.1.11)]).
- Lower-level spin$^u$ structures, [FL5, (2.1.13)] = [FL2a, (2.43)–(2.45)]: $\mathfrak t(\ell)$ (also written $\mathfrak t_\ell$) has
$$c_1(\mathfrak t(\ell))=c_1(\mathfrak t),\quad p_1(\mathfrak t(\ell))=p_1(\mathfrak t)+4\ell,\quad w_2(\mathfrak t(\ell))=w_2(\mathfrak t),$$
that is, $V_\ell=W\otimes E_\ell$ with $c_1(E_\ell)=c_1(E)$ and $c_2(E_\ell)=c_2(E)-\ell$.
- Expected dimensions, [FL5, (2.1.12)] = [FL2a, (2.51)]:
$$d_a(\mathfrak t)=-2p_1(\mathfrak t)-\tfrac32(\chi+\sigma),\qquad n_a(\mathfrak t)=\tfrac14\big(p_1(\mathfrak t)+c_1(\mathfrak t)^2-\sigma\big).$$
Here $d_a$ is the dimension of $M^w_\kappa$ and $n_a$ is the complex index of the Dirac operator on $V^+$. Also $d_s(\mathfrak s)=\tfrac14(c_1(\mathfrak s)^2-2\chi-3\sigma)$ ([FL5, (2.3.10)]).
- Typo in the source: [FL2b, (3.21)] prints $d_a(\mathfrak t)=-2p_1(\mathfrak t)-\tfrac32(\chi+2\sigma)$. Every other source has $(\chi+\sigma)$, and the index computation in [FL1, proof of Proposition 2.28] confirms $(\chi+\sigma)$.

---

## 1. [FL1]: the perturbed equations and the lower-level equations

**Paper / place.** [FL1, §1.1.1, equation (1.3)] (`eq:IntroPT`), [FL1, (2.32)] (`eq:PT`), and [FL1, §4.5.2, equation (4.13)] (`eq:PTLowerStratum`).

**Statement.** The holonomy-perturbed PU(2) monopole equations for $(A,\Phi)\in\tilde{\mathcal C}_{W,E}$ are
$$F_A^+-\big(\mathrm{id}+\tau_0\otimes\mathrm{id}_{\mathfrak{su}(E)}+\vec\tau\cdot\vec{\mathfrak m}(A)\big)\rho^{-1}(\Phi\otimes\Phi^*)_{00}=0,\qquad D_A\Phi+\rho(\vartheta_0)\Phi+\vec\vartheta\cdot\vec{\mathfrak m}(A)\Phi=0 .$$
Here $\vec{\mathfrak m}(A)=(\mathfrak m_{j,l,\alpha}(A))$ are holonomy sections ([FL1, (2.23), (2.25)]), defined as follows:
- They are supported in $N_b$ disjoint balls $B(x_j,R_0)$.
- They are cut off by the energy functions $\beta_j[A]$ ([FL1, (2.23)], `eq:ConnEnergyCutoff`), which vanish when $A$ has energy at least $\tfrac12\varepsilon_0^2$ on $B(x_j,2R_0)$.
- They **vanish identically when $A$ is reducible** ([FL1, §1.1.1, after (1.3)]; proof of [FL1, Proposition A.13]).

Uhlenbeck limits are handled as follows. If $A_\beta\to(A,\mathbf x)\in\mathcal A_{E_{-\ell}}\times\mathrm{Sym}^\ell(X)$ in the Uhlenbeck topology, the perturbations converge in $L^2_{k+1}$ to $\vec\tau\cdot\vec{\mathfrak m}(A,\mathbf x)$ and $\vec\vartheta\cdot\vec{\mathfrak m}(A,\mathbf x)$ ([FL1, (1.4)], `eq:GaugeEquivariantExtendedMap`). These limits are continuous and gauge-equivariant, and smooth on each smooth stratum of $\mathrm{Sym}^\ell(X)$. In the limit, $\beta_j[A]$ is replaced by $\beta_j[A_0,\mathbf x]$, computed from the measure $|F_{A_0}|^2+8\pi^2\sum_{x\in\mathbf x}\delta_x$ ([FL1, (4.12)]). The level-$\ell$ moduli space $\mathbf M_{W,E_{-\ell}}\subset\mathcal C_{W,E_{-\ell}}\times\mathrm{Sym}^\ell(X)$ is the space of triples $[A,\Phi,\mathbf x]$ solving
$$F_A^+-\big(\mathrm{id}+\tau_0\otimes\mathrm{id}+\vec\tau\cdot\vec{\mathfrak m}(A,\mathbf x)\big)\rho^{-1}(\Phi\otimes\Phi^*)_{00}=0,\qquad D_A\Phi+\rho(\vartheta_0)\Phi+\vec\vartheta\cdot\vec{\mathfrak m}(A,\mathbf x)\Phi=0\quad\text{[FL1, (4.13)]}.$$

**Hypotheses.** For compactness, the parameters must satisfy [FL1, (2.34)] (`eq:CompactEstPertC0`):
$$\|\tau_0\|_{L^\infty}+\sup_A\|\vec\tau\cdot\vec{\mathfrak m}(A)\|_{L^\infty}\le\tfrac1{64},\qquad \|\vartheta_0\|_{L^\infty_1}+\sup_A\|\vec\vartheta\cdot\vec{\mathfrak m}(A)\|_{L^\infty_{1,A}}\le1.$$
This is guaranteed by $\|\vec\vartheta\|_{\ell^1_\delta(C^r)}<\varepsilon_\vartheta$ and $\|\vec\tau\|_{\ell^1_\delta(C^r)}<\varepsilon_\tau$ ([FL1, (4.1)]), with $k\ge3$ and $r\ge k+1$. [corrected by checker] (4.1) controls only the holonomy terms $\vec\tau\cdot\vec{\mathfrak m}$ and $\vec\vartheta\cdot\vec{\mathfrak m}$ (via [FL1, Proposition A.13]). The bounds on $\tau_0$ and $\vartheta_0$ in (2.34) are a separate requirement: [FL1, §4 introduction] says "The parameters $\tau_0,\vartheta_0,\vec\tau,\vec\vartheta$ are chosen so that the perturbation estimates (2.34) are satisfied." FL1 also remark, after (2.34), that the constant $1$ in the $\vartheta$-bound "do[es] not need to be small"; only the $\tau$-bound $1/64$ is a smallness condition. $N_b$ must be chosen large enough relative to the energy bound (§4.5.2).

**Role.** FL1 say explicitly (§1.1.2) that **$\mathbf M_{W,E_{-\ell}}$ is not a product $M_{W,E_{-\ell}}\times\mathrm{Sym}^\ell(X)$ when $\ell>0$**, because the perturbation depends on $\mathbf x$. It is a product for the unperturbed equations, and for the perturbations of [FeehanGenericMetric] used in all later papers. Because the holonomy terms vanish at reducible $A$ and the equations are homogeneous in $\Phi$, the zero-section and reducible loci at every level are cut out by the equations without holonomy terms.

---

## 2. Ideal monopoles and the Uhlenbeck topology

### 2.1 [FL1, Definition 4.19] (`defn:UhlenbeckTop`), unperturbed case, §4.5.1

**Ideal monopoles.** $IM_{W,E}:=\bigcup_{\ell=0}^N M_{W,E_{-\ell}}\times\mathrm{Sym}^\ell(X)$, with $N\ge N_p$ the constant of [FL1, (4.19)].

**Statement.** Let $[A_\alpha,\Phi_\alpha,\mathbf y_\alpha]$ be a sequence in $IM_{W,E}$ and let $[A_0,\Phi_0,\mathbf x]\in IM_{W,E}$, with $\det E_\alpha=\det E_0=\det E$ and $c_2(E_\alpha),c_2(E_0)\le c_2(E)$. The sequence *converges* to $[A_0,\Phi_0,\mathbf x]$ if all three of the following hold:
1. There are $L^2_{k+1,\mathrm{loc}}$ determinant-one unitary bundle isomorphisms $u_\alpha:E_\alpha|_{X\setminus\mathbf x}\to E_0|_{X\setminus\mathbf x}$ such that $u_\alpha(A_\alpha,\Phi_\alpha)\to(A_0,\Phi_0)$ in $L^2_{k,\mathrm{loc}}$ over $X\setminus\mathbf x$.
2. $|F_{A_\alpha}|^2+8\pi^2\sum_{y\in\mathbf y_\alpha}\delta(y)\to|F_{A_0}|^2+8\pi^2\sum_{x\in\mathbf x}\delta(x)$ weak-$*$ as measures.
3. $c_2(E)=c_2(E_0)+|\mathbf x|$.

FL1 then assert: "The topological space $IM_{W,E}$ is second-countable and Hausdorff." $\bar M_{W,E}$ is the closure of $M_{W,E}$ in $IM_{W,E}$.

**Perturbed case** ([FL1, §4.5.2], unnumbered). The definition is the same, with $IM_{W,E}:=\bigcup_{\ell=0}^N\mathbf M_{W,E_{-\ell}}\subset\bigcup_{\ell=0}^N\mathcal C_{W,E_{-\ell}}\times\mathrm{Sym}^\ell(X)$ and $\mathbf M_{W,E_{-0}}:=M_{W,E}$.

### 2.2 Restatement: [FL5, Definition 2.1.2] (`defn:UhlenbeckConvergence`), with [FL5, (2.1.14)–(2.1.15)]

**Statement.** The space of ideal SO(3) monopoles is
$$I\mathcal M_{\mathfrak t}=\bigsqcup_{\ell=0}^\infty\big(\mathcal M_{\mathfrak t(\ell)}\times\mathrm{Sym}^\ell(X)\big)\quad[\text{FL5},(2.1.14)],$$
and the space of ideal pairs is $\bar{\mathcal C}_{\mathfrak t}=\bigsqcup_\ell\mathcal C_{\mathfrak t(\ell)}\times\mathrm{Sym}^\ell(X)$ ([FL5, (2.1.15)]).

A sequence $[A_\alpha,\Phi_\alpha]\subset\mathcal C_{\mathfrak t}$ converges to $[A_0,\Phi_0,\mathbf x]\in\mathcal C_{\mathfrak t(\ell)}\times\mathrm{Sym}^\ell(X)$ if both of the following hold:
1. There are $L^2_{k+1,\mathrm{loc}}$ spin$^u$ bundle isomorphisms $u_\alpha:V_{\mathfrak t}|_{X-\mathbf x}\to V_{\mathfrak t(\ell)}|_{X-\mathbf x}$ with $u_\alpha(A_\alpha,\Phi_\alpha)\to(A_0,\Phi_0)$ in $L^2_{k,\mathrm{loc}}$ over $X-\mathbf x$.
2. $|F_{\hat A_\alpha}|^2\,d\mathrm{vol}\to|F_{\hat A}|^2\,d\mathrm{vol}+8\pi^2\sum_{x\in\mathbf x}\delta_x$ weak-$*$.

"We call the intersection of $\bar{\mathcal M}_{\mathfrak t}$ with $\mathcal M_{\mathfrak t(\ell)}\times\mathrm{Sym}^\ell(X)$ its $\ell$-th level." [corrected by checker] Equivalent restatements of the convergence definition appear in [FL2a, §2.2] (before equation (2.46), `eq:UhlCompactPUMonModSpace`) and [FL3, §2.2]. There the measure condition is written with $|F_{A_\alpha}|^2$, where $A_\alpha$ is the connection on $V$ (resp. $E$), rather than with $|F_{\hat A_\alpha}|^2$, and [FL3] uses determinant-one unitary isomorphisms of $E$ as in [FL1]. [FLL1, §2.1] does **not** restate the definition: it gives only the space of ideal monopoles ((2.12), `eq:idealmonopoles`) and refers to "an Uhlenbeck topology [FL1, Definition 4.19]". [FLov, §2.4] restates it informally, with smooth convergence on compact subsets of $X-\mathbf x$ and "a multiple of the Dirac delta measure".

**Role.** This is the topology in which compactness holds, and in which every later object (links, neighbourhoods, gluing maps) is required to be continuous. [corrected by checker] For the links of the instanton stratum, continuity is proved ([FL2a, Lemma 3.8]). For the gluing maps at lower levels, continuity in this topology is assumed, not proved (see §7.4). The restatements do not include condition 3 of [FL1, Definition 4.19], because it is built into the choice of $\mathfrak t(\ell)$.

---

## 3. Uhlenbeck compactness

### 3.1 [FL1, Theorem 1.1] (`thm:Compactness`)

**Statement (verbatim, lightly cleaned).** *Let $X$ be a closed, oriented, smooth four-manifold with $C^\infty$ Riemannian metric, spin$^c$ structure $(\rho,W^+,W^-)$ with spin$^c$ connection on $W=W^+\oplus W^-$, and a Hermitian two-plane bundle $E$ with unitary connection on $\det E$. Then there is a positive integer $N_p$, depending at most on the curvatures of the fixed connections on $W$ and $\det E$ together with $c_2(E)$, such that for all $N\ge N_p$ the topological space $\bar M_{W,E}$ is compact, second countable, Hausdorff, and is given by the closure of $M_{W,E}$ in $\bigcup_{\ell=0}^{N}\mathbf M_{W,E_{-\ell}}$.*

**Hypotheses.**
- (i) $X$ is closed, oriented and smooth, with a $C^\infty$ metric.
- (ii) There is a spin$^c$ structure with a $C^\infty$ spin$^c$ connection.
- (iii) $E$ is a Hermitian rank-two bundle with a fixed $C^\infty$ unitary connection on $\det E$.
- Standing assumptions of [FL1, §4]: $k\ge3$; the perturbation bounds [FL1, (2.34)] via (4.1); $N_b$ large.

**Notes.**
- In the proof, $N_p=N_p(c_1(E),c_2(E),g,F(A_{\det W}),F(A_{\det E}))$ ([FL1, (4.19)], `eq:MaxBubblePoints`). The bound is
$$\ell\le\frac1{8\pi^2}\int_X|F_A^-|^2+\frac1{8\pi^2}\int_X|F_{A_0}^+|^2\le N_p.$$
- The $L^2$ bounds on $F_A^\pm$ come from [FL1, Lemma 4.3] (`lem:L2aprioriEstFA`), whose constants depend on the $L^2$ norms of the scalar curvature, $F(A_{\det E})$, $F(A_{\det W^+})$, and on $p_1(\mathfrak{su}(E))$.
- The universal energy bound is [FL1, (4.6)] (`eq:MonopoleEnergyBound`): $\int_X(|F_A|^2+|\Phi|^4+|\nabla_A\Phi|^2)\le K$.
- The conclusion "$\bar M_{W,E}$ is compact" is deduced from Theorem 4.20 "by an entirely routine argument (which we leave to the reader)" ([FL1, §4.6]).

### 3.2 [FL1, Theorem 4.20] (`thm:SeqCompact`), sequential compactness

**Statement.** *With the same hypotheses as Theorem 1.1 and the same $N_p$: for all $N\ge N_p$, any infinite sequence in $M_{W,E}$ has a weakly convergent subsequence, with limit point in $\bigcup_{\ell=0}^N\mathbf M_{W,E_{-\ell}}$.*

**Ingredients.** These are numbered results of [FL1]:
- **Lemma 4.21** (`lem:CharClassLimit`): the limit bundle $E_0$ has $c_1(E_0)=c_1(E)$ and $c_2(E_0)=c_2(E)-\ell$, where $\ell=\sum_i\kappa_i$ and each $\kappa_i$ is a positive integer.
- **Theorem 4.10** (`thm:PTRemovSing`): removable singularities for finite-energy $C^\infty$ solutions over a punctured ball. It is stated with $(\vec\tau,\vec\vartheta)=0$; Remark 4.11 explains that the holonomy perturbations vanish near bubble points.
- **Proposition 4.18** (`prop:LocalUhlenbeck`): local convergence under small curvature in $L^2$.
- **Proposition 4.24** (`prop:TopStratumCpt`): a uniform $L^p$ curvature bound with $p>2$ gives convergence in $M_{W,E}$ with no bubbling.

### 3.3 Restatements in the spin$^u$ language

- **[FL5, Theorem 2.1.3]** (`thm:Compactness`), citing "[FL1, Theorem 1.1]": *Let $X$ be a closed Riemannian four-manifold with spin$^u$ structure $\mathfrak t$. Then there is a positive integer $N$, depending at most on the scalar curvature of $X$, the curvature of the chosen unitary connection on $\det(V^+)$, and $p_1(\mathfrak t)$, such that the Uhlenbeck closure $\bar{\mathcal M}_{\mathfrak t}$ of $\mathcal M_{\mathfrak t}$ in $\bigsqcup_{\ell=0}^N(\mathcal M_{\mathfrak t(\ell)}\times\mathrm{Sym}^\ell(X))$ is a second-countable, compact, Hausdorff space. The space $\bar{\mathcal M}_{\mathfrak t}$ carries a continuous circle action, which restricts to the circle action defined on $\mathcal M_{\mathfrak t_\ell}$ for each level.*
- **[FLL1, Theorem 2.2]** (`thm:Compactness`): identical to [FL5, Theorem 2.1.3], except that $N$ depends "at most on the curvature of the chosen unitary connection on $\det(V^+)$ together with $p_1(\mathfrak t)$", with no mention of scalar curvature. [corrected by checker] It also opens "Let $X$ be a Riemannian four-manifold", omitting "closed"; closedness is a standing assumption of that paper and of [FL1].
- **[FL2a, Theorem 2.12]** (`thm:Compactness`): the same as [FLL1, Theorem 2.2], without the circle-action sentence. FL2a add: "Theorem 2.12 is a special case of the more general result proved in [FL1] for … holonomy perturbations."
- **[FL3, Theorem 2.2]** (`thm:Compactness`): a verbatim transcription of [FL1, Theorem 1.1] into $M(\mathfrak t_\ell)$ notation.
- **[FL6, §3]** (unnumbered text): "$\bar{\mathcal M}_{\mathfrak t}\subset\bigcup_{\ell=0}^N\mathcal M_{\mathfrak t(\ell)}\times\mathrm{Sym}^\ell(X)$ … [FL1, Theorem 4.20]. The $S^1$ action extends continuously over $\bar{\mathcal M}_{\mathfrak t}$. The closure of $M^w_\kappa$ in $\bar{\mathcal M}_{\mathfrak t}$ is the usual Uhlenbeck compactification $\bar M^w_\kappa$."

**Differences between versions.**
- (a) The restatements use the perturbations $(\tau,\vartheta)$ (and generic $(g,\rho)$) of [FeehanGenericMetric], not holonomy perturbations. They justify this as a special case of [FL1], since [FL1]'s proof covers $\vec\tau=\vec\vartheta=0$; see also [FL1, Remark 1.2], which says Theorem 1.1 "yields the standard Uhlenbeck compactification" for the perturbations of [FeehanGenericMetric] and [TelemanGenericMetric].
- (b) The smallness hypothesis is not repeated in the restatements. In the later notation it reads $\|\tau-\mathrm{id}\|_{L^\infty}\le1/64$ and $\|\vartheta\|_{L^\infty_1}\le1$ ([FL1, (2.34)]); compare [FL2a, Proposition 2.15] for the Seiberg–Witten case, where the hypothesis $\|\tau-\mathrm{id}\|_{C^0}<1/64$ is explicit.
- (c) The dependence of $N$ is stated differently in each version; only [FL5] mentions scalar curvature, which does enter through [FL1, Lemmas 4.2–4.3].
- (d) The continuity of the circle action on $\bar{\mathcal M}_{\mathfrak t}$ is asserted in [FL5] and [FLL1] without separate proof. [corrected by checker] [FL1] does not address it at all, because its moduli spaces are already quotients by the central circle; it is not "implicit" there. [FL6, §3] and [FLov, §2.4] repeat the assertion.

**Role.** This theorem is the only global structural result on $\bar{\mathcal M}_{\mathfrak t}$. It gives a compact, second-countable Hausdorff space with finitely many levels $\ell\le N$, each level contained in a product $\mathcal M_{\mathfrak t(\ell)}\times\mathrm{Sym}^\ell(X)$. It says nothing about local structure near points of lower levels.

---

## 4. Transversality: which strata are smooth and regular

### 4.1 [FL1, Theorem 1.3] (`thm:Transversality`), holonomy perturbations, all levels

**Statement.** *Let $X$ be a closed, oriented, smooth four-manifold with $C^\infty$ Riemannian metric, spin$^c$ structure $(\rho,W^+,W^-)$ with spin$^c$ connection on $W$, and a Hermitian line bundle $\det E$ with unitary connection. Then there is a first-category subset of the space of $C^\infty$ perturbation parameters such that the following holds. For each 4-tuple $(\tau_0,\vartheta_0,\vec\tau,\vec\vartheta)$ in the complement of this first-category subset, integer $\ell\ge0$, and smooth stratum $\Sigma\subset\mathrm{Sym}^\ell(X)$, the moduli space $\mathbf M^{*,0}_{W,E_{-\ell}}|_\Sigma(\tau_0,\vartheta_0,\vec\tau,\vec\vartheta)$ is a smooth manifold of the expected dimension*
$$\dim\mathbf M^{*,0}_{W,E_{-\ell}}|_\Sigma=\dim M^{*,0}_{W,E_{-\ell}}+\dim\Sigma=-2p_1(\mathfrak{su}(E_{-\ell}))-\tfrac32(e(X)+\sigma(X))+\dim\Sigma+\tfrac12p_1(\mathfrak{su}(E_{-\ell}))+\tfrac12\big((c_1(W^+)+c_1(E))^2-\sigma(X)\big)-1,$$
*where $\det(E_{-\ell})=\det E$ and $c_2(E_{-\ell})=c_2(E)-\ell$.*

**Notation.** $\mathbf M_{W,E_{-\ell}}|_\Sigma:=\{[A,\Phi,\mathbf x]\in\mathbf M_{W,E_{-\ell}}:\mathbf x\in\Sigma\}$. The superscript $*,0$ means $A$ is irreducible and $\Phi\not\equiv0$. $e(X)$ is the Euler characteristic. The $-1$ comes from dividing by the central circle (§0.3).

**What the proof covers.**
- $\ell=0$ is [FL1, Corollary 5.6] (`cor:GenericSmoothAnalyticProjection`), which rests on [FL1, Theorem 5.2] (`thm:SmoothParamModuliSpace`: the parametrised moduli space is a smooth Banach manifold) and [FL1, Corollary 5.3] (`cor:GenericProjection`, Sard–Smale for $C^r$ parameters); §5.1.2 passes to $C^\infty$ parameters.
- $\ell>0$ is argued in [FL1, §5.1.3] in one paragraph ("The proof of Corollary 5.6 now shows…"), giving [FL1, (5.6)]: $\dim\mathbf M^{*,0}_{W,E_{-\ell}}|_\Sigma=\dim M^{*,0}_{W,E_{-\ell}}+\dim\Sigma$. The same paragraph says the fibres $M^{*,0}_{W,E_{-\ell}}|_{\mathbf x}$ are smooth of the expected dimension for generic $\mathbf x$.
- The essential input is [FL1, Theorem 5.11] (`thm:LocalToGlobalReducible`): a monopole with $\Phi\not\equiv0$ that is reducible on an admissible open set is reducible on $X$.

**What is explicitly not covered.** [FL1, §5 introduction]: "The proof of Theorem 1.3 does not apply to PU(2) monopoles which are zero-sections or which are reducible." [FL1, after Remark 1.4]: for a generic metric, $M^{\mathrm{asd},*}_E$ is smooth of the expected dimension, "although the points of $M^{\mathrm{asd},*}_E$ need not be regular points of $M^*_{W,E}$". For generic $\tau_0$, the reducible non-zero-section loci $M^{\mathrm{red},0}_{W,E,L_1}$ are smooth of the expected dimension, but "the points of $M^{\mathrm{red},0}_{W,E,L_1}$ need not be regular points of $M^0_{W,E}$".

### 4.2 Generic-metric transversality: [FL5, Theorem 2.1.1] (`thm:Transv`), equivalently [FL2a, Theorem 2.13], [FL3, Theorem 2.3], [FLL1, Theorem 2.1]

**Statement ([FL5]).** *(See Feehan [FeehanGenericMetric, Theorem 1.1] and Teleman [TelemanGenericMetric].) Let $X$ be a closed, oriented, smooth four-manifold and let $V$ be a complex rank-eight Hermitian vector bundle over $X$. Then for parameters $(\rho,g,\tau,\vartheta)$ which are generic in the sense of [FeehanGenericMetric], and $\mathfrak t=(\rho,V)$, the space $\mathcal M^{*,0}_{\mathfrak t}$ is a smooth manifold of the expected dimension*
$$\dim\mathcal M^{*,0}_{\mathfrak t}=d(\mathfrak t)=d_a(\mathfrak t)+2n_a(\mathfrak t)\quad[\text{FL5},(2.1.12)].$$
[FL2a, Theorem 2.13] says "for a generic, $C^\infty$ pair $(g,\rho)$ … and generic, $C^\infty$ parameters $(\tau,\vartheta)$". Here genericity of $(g,\rho)$ means $(g,\rho)=(f^*g_0,f^*\rho_0)$ with $f\in C^\infty(GL(T^*X))$ generic ([FL2a, §2.2]).

**Hypotheses.** Only the genericity of $(g,\rho,\tau,\vartheta)$. The proof is in [FeehanGenericMetric], which is not among the sources and was not read.

**Lower levels in this setting.** The theorem is stated for one spin$^u$ structure. For the finitely many $\mathfrak t(\ell)$, $0\le\ell\le N$, smoothness of every $\mathcal M^{*,0}_{\mathfrak t(\ell)}$ follows by intersecting finitely many residual sets of parameters. Each lower level is contained in a product $\mathcal M_{\mathfrak t(\ell)}\times\mathrm{Sym}^\ell(X)$ (no $\mathbf x$-dependence), so each $\mathcal M^{*,0}_{\mathfrak t(\ell)}\times\Sigma$ is then a smooth manifold. I found no place where FL state this for all $\ell$ simultaneously. They use it: [FL2b, §3.3, after (3.20)–(3.21)], [FL2b, Corollary 3.18], and [FLov, (2.10)].

### 4.3 Seiberg–Witten moduli spaces with FL's perturbations: [FL2a, Proposition 2.15, Proposition 2.16, Remark 2.14]

**Equations.** [FL2a, (2.55)] = [FL5, (2.3.4)], for $\mathfrak s=(\rho,W)$:
$$\mathrm{Tr}(F_B^+)-\tau\rho^{-1}(\Psi\otimes\Psi^*)_0-\eta=0,\qquad D_B\Psi+\rho(\vartheta)\Psi=0.$$
To match reducible SO(3) monopoles, one must take $\eta=F^+_{A_\Lambda}$ ([FL2a, (2.56)], Remark 2.14).

- **[FL2a, Proposition 2.15]** (`prop:U1MonopoleCompact`): *if $\|\tau-\mathrm{id}_{\Lambda^+}\|_{C^0}<1/64$, then $M_{\mathfrak s}(g,\eta,\tau,\vartheta)$ is compact.*
- **[FL2a, Proposition 2.16]** (`prop:SmoothFamilyOfReducibles`): *for any fixed $\eta,\vartheta$ there is a first-category subset of $\Omega^0(GL(\Lambda^+))$ such that for all $C^\infty$ $\tau$ in its complement, $M^0_{\mathfrak s}(g,\tau,\eta,\vartheta)$ is a smooth manifold of the expected dimension $d_s(\mathfrak s)$* ([FL2a, (2.63)]).
- **[FL2a, Remark 2.14]**: $\eta=F^+_{A_\Lambda}$ is *not* generic if $c_1(\mathfrak s)-\Lambda$ is torsion. If it is not torsion, $b_2^+>0$ and $g$ is generic, there are no zero-section solutions (citing Morgan's notes, Proposition 6.3.1).

**Role.** [corrected by checker] Proposition 2.16 gives smoothness of $M^0_{\mathfrak s}$ only, and Proposition 2.15 gives compactness of $M_{\mathfrak s}$ only when $\|\tau-\mathrm{id}\|_{C^0}<1/64$. The Seiberg–Witten stratum $M_{\mathfrak s}$ is therefore a smooth compact manifold of dimension $d_s(\mathfrak s)$ for generic $\tau$ with $\|\tau-\mathrm{id}\|_{C^0}<1/64$, *provided $M_{\mathfrak s}$ contains no zero-section pairs*. Zero-section pairs are excluded, for $b_2^+>0$ and generic $g$, when $c_1(\mathfrak s)-\Lambda$ is not torsion ([FL2a, Remark 2.14]; [FL5, §2.3.2], citing Morgan's notes, Proposition 6.3.1), or by [FL2a, Corollary 3.3] under the Morgan–Mrowka criterion. This is smoothness of the stratum itself, not regularity of its points in $\mathcal M_{\mathfrak t}$ (see §5).

---

## 5. Strata of the top level

### 5.1 Fixed points of the circle action: [FL2a, Proposition 3.1] (`prop:ClassificationOfStabilizers`)

**Statement.** *Let $\mathfrak t=(\rho,V)$ be a spin$^u$ structure over a closed, oriented, smooth four-manifold $X$, with $b_2^+(X)\ge1$ and generic Riemannian metric. If $\hat A$ is a non-flat connection on $\mathfrak g_{\mathfrak t}$, then $[A,\Phi]\in\mathcal M_{\mathfrak t}$ is a fixed point of the $S^1$ action if and only if one of the following holds:*
- *(1) $\hat A$ is anti-self-dual and irreducible, and $\Phi\equiv0$. Then $(A,\Phi)$ is fixed by scalar multiplication.*
- *(2) $(A,\Phi)$ is reducible with respect to a splitting $V=W\oplus W\otimes L$, $\Phi\not\equiv0$, and $(A,\Phi)=(B\oplus B\otimes A_L,\Psi\oplus0)$. Then $(A,\Phi)$ is fixed by the action $\Psi\oplus\Psi'\mapsto\Psi\oplus e^{i\theta}\Psi'$, and $\hat A=d_{\mathbb R}\oplus A_L$ is reducible with respect to $\mathfrak g_{\mathfrak t}\cong i\underline{\mathbb R}\oplus L$.*

**Hypotheses.** $b_2^+\ge1$; a generic metric (used to exclude reducible ASD connections, [DK, Corollary 4.3.15]); $\hat A$ not flat.

### 5.2 Excluding flat connections: [FL2a, Lemma 3.2] (`lem:MorganMrowka`) and [FL2a, Corollary 3.3] (`cor:NoSWZeroSections`)

- **Lemma 3.2**, citing [MorganMrowkaPoly, p. 226]: if $\langle w,e\rangle\not\equiv0\pmod 2$ for a spherical class $e$, then no SO(3) bundle with $w_2\equiv w$ admits a flat connection. In particular this holds on $X\#\overline{\mathbb{CP}}^2$ with $w+e^*$. FL note that this applies "simultaneously to all levels of the Uhlenbeck compactifications $\bar M^w_\kappa$ and $\bar{\mathcal M}_{\mathfrak t}$".
- **Corollary 3.3**: *if $M_{\mathfrak s}\hookrightarrow\mathcal M_{\mathfrak t}$ is a Seiberg–Witten moduli subspace and $w_2(\mathfrak t)$ obeys the Morgan–Mrowka criterion, then $M_{\mathfrak s}$ contains no zero-section solutions.*
- **[FL2b, Definition 3.20]** = **[FL5, Definition 2.2.1]** (`defn:Good`): *a class $v\in H^2(X;\mathbb Z/2)$ is good if no integral lift of $v$ is torsion.* FL assert in the text after Definition 3.20 that $v$ is good if and only if no line bundle $L$ with $c_1(L)\equiv v$ admits a flat connection, "or if and only if no SO(3) bundle over $X$ with second Stiefel–Whitney class $v$ admits a flat connection".
  - [corrected by checker] The second equivalence, as stated, is too strong. "Good" excludes flat *reducible* SO(3) connections $d_{\mathbb R}\oplus A_L$, since $A_L$ flat forces $c_1(L)$ to be torsion and $c_1(L)\equiv v$. It does not exclude flat connections with finite holonomy that are irreducible in the sense $H^0=0$.
  - Example: on $T^2$, the representation sending the generators to $\mathrm{diag}(1,-1,-1)$ and $\mathrm{diag}(-1,1,-1)$ defines a flat SO(3) bundle with $w_2\neq0$. Its lifts to SU(2) are $i,j$, which anticommute. Pulled back to $T^4$, it gives a flat bundle with $w_2=v\ne0$. Since $H^2(T^4;\mathbb Z)$ is torsion-free, $v$ is good.
  - The Morgan–Mrowka criterion of [FL2a, Lemma 3.2] *does* exclude all flat SO(3) connections. In the blown-up situation $(X\#\overline{\mathbb{CP}}^2,w+\mathrm{PD}[e])$ that FL actually use, both conditions hold. Where this note uses "good" only to exclude flat or zero-section *reducibles*, the weaker condition suffices.

### 5.3 Reducibles are Seiberg–Witten monopoles: [FL2a, Lemmas 2.9, 3.11, 3.12, 3.13, 3.16]

- **Lemma 2.9** (`lem:ReducibleSpinu`): $A$ is reducible with respect to $V=W\oplus W'$ if and only if $\hat A$ is reducible with respect to $\mathfrak g_{\mathfrak t}=i\underline{\mathbb R}\oplus L$ with $W'=W\otimes L$. Then $\hat A=d_{\mathbb R}\oplus A_L$, with $A_L=A_\Lambda\otimes(B^{\det})^*$.
- **Lemma 3.11** (`lem:TopU1Embedding`). For $V=W\oplus W\otimes L$, the map
$$\iota:\tilde{\mathcal C}_{\mathfrak s}\to\tilde{\mathcal C}_{\mathfrak t},\qquad(B,\Psi)\mapsto(B\oplus B\otimes A_L,\Psi\oplus0)\quad[\text{FL2a},(3.9)]$$
is a smooth embedding. It is equivariant for $\varrho:s\mapsto s\,\mathrm{id}_W\oplus s^{-1}\mathrm{id}_{W\otimes L}$, and its image contains all pairs fixed by the second circle action. The induced map $\mathcal C_{\mathfrak s}\to\mathcal C_{\mathfrak t}$ is continuous. It is a topological embedding on $\mathcal C^0_{\mathfrak s}$, and on all of $\mathcal C_{\mathfrak s}$ if $w_2(\mathfrak t)\ne0$. If $w_2(\mathfrak t)=0$, zero-section points go to zero-section reducibles, not necessarily injectively when $b_1>0$.
- **Lemma 3.12** (`lem:RestrictionOfPU2MonopoleEquation`): a reducible pair solves the SO(3) monopole equations if and only if $(B,\Psi)$ solves the Seiberg–Witten equations with $\eta=F^+_{A_\Lambda}$.
- **Lemma 3.13** (`lem:RedAreSW`): *if $w_2(\mathfrak t)\ne0$, then $\iota:M_{\mathfrak s}\hookrightarrow\mathcal C_{\mathfrak t}$ is a topological embedding whose image is the subspace of $\mathcal M_{\mathfrak t}$ of pairs reducible with respect to $V=W\oplus W\otimes L$.* ([FL2a, (3.16)].)
- **Lemma 3.16** (`lem:ReducibleSubmanifold`): *$\iota:\mathcal C^0_{\mathfrak s}\to\mathcal C^0_{\mathfrak t}$ is a smooth immersion, and $\iota:M^0_{\mathfrak s}\hookrightarrow\mathcal C^0_{\mathfrak t}$ is a smooth embedding, so $M^0_{\mathfrak s}$ is a submanifold of $\mathcal C^0_{\mathfrak t}$.*

### 5.4 The top-level stratification: [FL2a, (3.17)] (`eq:TopLevelStratification`)

$$\mathcal M_{\mathfrak t}\cong\mathcal M^{*,0}_{\mathfrak t}\cup M^w_\kappa\cup\bigcup_{\mathfrak s}M_{\mathfrak s}.$$
The union is over the finitely many $\mathfrak s$ with $M_{\mathfrak s}\ne\emptyset$ and $\mathfrak t=\mathfrak s\oplus\mathfrak s'$. FL state that the lower strata "do not intersect when $\mathcal M_{\mathfrak t}$ contains no reducible, zero-section solutions". The opening paragraph of [FL2a, §3] says: "As we shall see in this section, the moduli space $\mathcal M_{\mathfrak t}$ … is a smoothly stratified space."

### 5.5 The zero-section (instanton) stratum at the top level: [FL2a, (3.5), Lemma 3.4, Lemma 3.5, Corollary 3.6]

- **[FL2a, (3.5)]**: the map $\iota:M^w_\kappa(X)\hookrightarrow\mathcal C_{\mathfrak t}$, $[\hat A]\mapsto[A,0]$, is a "smoothly stratified embedding" onto the zero-section solutions. Here $\kappa=-\tfrac14p_1(\mathfrak t)$ and $w\equiv w_2(\mathfrak t)$. For generic $g$, $M^{w,*}_\kappa$ is smooth of dimension $d_a(\mathfrak t)$ ([DK, Corollary 4.3.18]; [FU]); also [FL5, (2.2.1)].
- **Lemma 3.4** (`lem:DecompOfZeroSectionDeformation`). At $(A,0)$:
$$H^0_{A,0}\cong H^0_{\hat A},\qquad H^1_{A,0}\cong H^1_{\hat A}\oplus\ker(D_A+\rho(\vartheta)),\qquad H^2_{A,0}\cong H^2_{\hat A}\oplus\mathrm{coker}(D_A+\rho(\vartheta)).$$
So **zero-section points are in general not regular points of $\mathcal M_{\mathfrak t}$**.
- **Lemma 3.5** (`lem:TwistedReducibles`), *stated as a citation of [KMStructure, Lemma 2.4 & Corollary 2.5]*. Let $\lambda$ be a non-trivial real line bundle and $F=\lambda\oplus N$ with $p_1(F)=-4\kappa\ne0$.
  - (1) If $b^+(\lambda)=0$, then $b^1(\lambda)=-(b^+-b^1+1)$, and $M^w_\kappa$ contains twisted reducibles for this splitting for all metrics. If in addition $b^1(\lambda)\ge0$, then $-2p_1(F)-3(1-b^1+b^+)>b^1(\lambda)$, and for a generic metric each such twisted reducible has $H^2_{\hat A}=0$.
  - (2) If $b^+(\lambda)\ge1$, then for generic metrics $M^w_\kappa$ contains no twisted reducibles for this splitting.

  (Restated in [FL2a]; not checked against the original.) It matters only when $b_1(X)>0$ or $H_1$ has 2-torsion.
- **Corollary 3.6** (`cor:ASDKuranishi`). Assume $b_2^+>0$ and a generic metric, and let $[A,0]$ be a point in the image of $M^w_\kappa\hookrightarrow\mathcal M_{\mathfrak t}$. [corrected by checker] FL write "so $H^0_{\hat A}=0=H^2_{\hat A}$": the vanishing is presented as a consequence of the hypotheses (Freed–Uhlenbeck genericity, and [FL2a, Lemma 3.5] for twisted reducibles), not as an extra hypothesis. Then there are an $S^1$-equivariant smooth embedding $\boldsymbol\gamma_A:\mathcal O_A\subset T_{\hat A}M^w_\kappa\oplus\ker(D_A+\rho(\vartheta))\to\tilde{\mathcal C}_{\mathfrak t}$ and an $S^1$-equivariant obstruction map $\boldsymbol\varphi_A:\mathcal O_A\to\mathrm{coker}(D_A+\rho(\vartheta))$. $\boldsymbol\gamma_A$ is an $S^1$-equivariant "smoothly-stratified diffeomorphism" from $\boldsymbol\varphi_A^{-1}(0)$ onto a neighbourhood of $[A,0]$ in $\mathcal M_{\mathfrak t}$.

  This is a local model at **top-level** zero-section points only.

---

## 6. The strata of the compactification

### 6.1 Three-part decomposition: [FL5, (2.2.2)] (`eq:StratificationCptPU(2)Space`) = [FLL1, (2.13)]

**Statement.** If $w\pmod 2$ is good, there is a disjoint union
$$\bar{\mathcal M}_{\mathfrak t}\cong\bar{\mathcal M}^{*,0}_{\mathfrak t}\sqcup\bar M^w_\kappa\sqcup\bar{\mathcal M}^{\mathrm{red}}_{\mathfrak t}.$$
Here $\bar{\mathcal M}^{*,0}_{\mathfrak t}$ consists of the triples whose SO(3) connection is irreducible and whose spinor is not identically zero, and $\bar{\mathcal M}^{\mathrm{red}}_{\mathfrak t}=\bar{\mathcal M}_{\mathfrak t}-\bar{\mathcal M}^*_{\mathfrak t}$ consists of the triples whose SO(3) connection is reducible ([FL5, §2.2]; [FL2b, (3.18)] for $\bar{\mathcal M}^*_{\mathfrak t}$ and $\bar{\mathcal M}^0_{\mathfrak t}$). In practice FL replace $(X,w)$ by $(X\#\overline{\mathbb{CP}}^2,w+\mathrm{PD}[e])$ to make $w$ good.

### 6.2 The instanton stratum of the compactification: [FL2b, Lemma 3.21] (`lem:ASDClosureEquality`)

**Statement.** *Let $\mathfrak t$ be a spin$^u$ structure on a closed, oriented four-manifold $X$ with generic metric, $b_2^+(X)>0$ and $w_2(\mathfrak t)\equiv w\pmod 2$, for $w\in H^2(X;\mathbb Z)$. If $w\pmod2$ is good, then*
$$\bar M^{\mathrm{asd}}_{\mathfrak t}=\iota(\bar M^w_\kappa)\quad[\text{FL2b},(3.29)],$$
*where $\bar M^{\mathrm{asd}}_{\mathfrak t}:=\{[A,\Phi,\mathbf x]\in\bar{\mathcal M}_{\mathfrak t}:\Phi=0\}$ ([FL2b, (3.28)]).*

**Proof as given.** The inclusion $\iota(\bar M^w_\kappa)\subset\bar M^{\mathrm{asd}}_{\mathfrak t}$ follows from the definitions. The reverse inclusion is argued from Taubes' gluing theorem for ASD SO(3) connections "when there are no obstructions to gluing (for example, when the metric on $X$ is generic)". FL give an example of how it can fail when flat connections are present. The lemma is stated "the preceding discussion yields"; there is no separate proof.

[corrected by checker] The discussion before the lemma deduces "if $w_2(\mathfrak t)$ is good, there are no flat SO(3) connections in $\bar{\mathcal M}_{\mathfrak t}$" from the equivalence questioned in §5.2. Goodness alone excludes only flat *reducible* connections. Flat connections can occur only at a level $\ell=\kappa$, so this matters only when $\kappa\le N$ is an integer. The argument is sound under the Morgan–Mrowka criterion ([FL2a, Lemma 3.2]), which holds in the blown-up setting FL actually use. As literally stated with "good", the lemma is [unconfirmed] by the checker.

**Consequence.** The instanton strata at level $\ell$ are $\iota(M^w_{\kappa-\ell})\times\Sigma$, for $\Sigma$ a stratum of $\mathrm{Sym}^\ell(X)$ (the usual strata of $\bar M^w_\kappa$, [DK, §4.4]). [corrected by checker] Strictly, Lemma 3.21 and the definitions give only that the level-$\ell$ zero-section part of $\bar{\mathcal M}_{\mathfrak t}$ is $\iota$ of the level-$\ell$ part of $\bar M^w_\kappa$, which is contained in $\iota(M^w_{\kappa-\ell})\times\mathrm{Sym}^\ell(X)$. That every point of $M^w_{\kappa-\ell}\times\Sigma$ is an Uhlenbeck limit is the standard Taubes gluing statement for unobstructed ASD connections (generic metric). FL invoke it in the discussion before Lemma 3.21 but do not prove it. The dimension of $\iota(M^w_{\kappa-\ell})\times\Sigma$ is $d_a(\mathfrak t)-8\ell+\dim\Sigma$ (my arithmetic from (2.1.12)). The extension $\iota:\bar M^w_\kappa\hookrightarrow\bar{\mathcal M}_{\mathfrak t}$, $[\hat A,\mathbf x]\mapsto[A,0,\mathbf x]$, is called a "smoothly stratified embedding" ([FL2b, §3.4.1], citing [FL2a, §2.2], [FL1, §4], [DK, §4.4]). With $w$ good one has $\bar{\mathcal M}_{\mathfrak t}=\bar{\mathcal M}^0_{\mathfrak t}\cup\iota(\bar M^w_\kappa)$ ([FL2b], after Lemma 3.21).

### 6.3 Dimensions of the levels: [FL2b, (3.20)–(3.21)] and the text after them; [FLov, (2.10)]

**[FL2b], quoted.** "[…] $p_1(\mathfrak t_\ell)=p_1(\mathfrak t)+4\ell$ and so equation (3.20) implies $\dim\mathcal M_{\mathfrak t_\ell}=\dim\mathcal M_{\mathfrak t}-6\ell$. The strata of $\mathcal M_{\mathfrak t_\ell}/S^1\times\mathrm{Sym}^\ell(X)$ then have codimension at least $2\ell$ relative to the top stratum."

**[FLov, (2.10)]** (`eq:LowerStrataDimen`): $\dim(\mathcal M^{*,0}_{\mathfrak t(\ell)}\times\mathrm{Sym}^\ell(X))=\dim\mathcal M^{*,0}_{\mathfrak t}-2\ell$.

**Check.** $d_a(\mathfrak t(\ell))=d_a(\mathfrak t)-8\ell$ and $n_a(\mathfrak t(\ell))=n_a(\mathfrak t)+\ell$, so $d(\mathfrak t(\ell))=d(\mathfrak t)-6\ell$. A stratum $\Sigma$ indexed by a partition of length $r$ has $\dim\Sigma=4r\le4\ell$. Hence $\dim(\mathcal M^{*,0}_{\mathfrak t(\ell)}\times\Sigma)=d(\mathfrak t)-6\ell+4r\le d(\mathfrak t)-2\ell$.

### 6.4 What FL mean by "smoothly stratified"

- **[FL2b, Definition 3.2]** (`defn:Stratifications`), citing [GorMacPh], [Mather], [MMR]: *A smoothly stratified space $Z$ is a topological space with a smooth stratification given by a disjoint union $Z=Z_0\cup Z_1\cup\cdots\cup Z_n$, where the strata $Z_i$ are smooth manifolds. There is a partial ordering among the strata, given by $Z_i<Z_j$ if $Z_i\subset\bar Z_j$. There is a unique stratum of highest dimension, $Z_0$, such that $\bar Z_0=Z$, called the top stratum.* The definition then defines smoothly stratified maps and subspaces.
- **[FL2b, Remark 3.3]** (`rmk:StratSubspace`): if $f:Z\to\mathbb R$ is continuous and smooth on each stratum, then $f^{-1}(\varepsilon)$ is a smoothly stratified subspace for generic $\varepsilon$. (This is the only property used for the instanton link, [FL2a, Lemma 3.8].)
- **[FL5, §4.1]** (unnumbered paragraph) uses a stronger definition: a locally finite decomposition into locally closed smooth manifolds satisfying the *condition of the frontier* ("Whitney pre-stratified", citing [Mather 2012, p. 480]). It then defines Thom–Mather control data. [FL5] applies this definition to $\mathrm{Sym}^\ell(X)$ and to the space of global splicing data $\bar{\mathcal M}^{\mathrm{vir}}_{\mathfrak t,\mathfrak s}$, not to $\bar{\mathcal M}_{\mathfrak t}$ itself.
- **Explicit caveat, [FL2b, §3, introduction].** "Second, the topology near points in the lower levels of $\bar{\mathcal M}_{\mathfrak t}$ need not be locally finite (for example, there may be infinitely many path-connected components). Hence, it is not known if $\mathbf L^w_{\mathfrak t,\kappa}$ is triangulable and thus it may not have a fundamental class […]. This problem also leads us to work in the category of smoothly stratified spaces rather than that of piecewise-linear spaces." Compare [FL2a, §3.2]: the instanton link "might not have a fundamental class because it is not known to have locally finite topology near the lower strata of the Uhlenbeck compactification".
- **Expository claims.** These are stronger than anything proved for $\bar{\mathcal M}_{\mathfrak t}$ itself:
  - [FLov, §1]: "In [FL1, FL2a, FL2b, FLLevelOne], we proved that … $\bar{\mathcal M}_{\mathfrak t}/S^1$ defines a smoothly-stratified cobordism…"
  - [FLov, §2.4]: "The space $\bar{\mathcal M}_{\mathfrak t}/S^1$ defines a smoothly-stratified cobordism between the link of $\bar M^w_\kappa$ … and the links of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$."
  - [corrected by checker: added] [FL6, §3]: "then $\bar{\mathcal M}_{\mathfrak t}/S^1$ defines a compact, orientable cobordism between $\bar{\mathbf L}^w_{\mathfrak t,\kappa}$ and the union, over $\mathfrak s\in\mathrm{Spin}^c(X)$, of the links $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$." In the same section [FL6] asserts, with no hypothesis on $w$ or $g$, that "The closure of $M^w_\kappa$ in $\bar{\mathcal M}_{\mathfrak t}$ is the usual Uhlenbeck compactification". [FL5, §2.6] ((2.6.1)) likewise describes $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$ as "the boundary of an open neighborhood of the Seiberg–Witten stratum $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in $\bar{\mathcal M}_{\mathfrak t}/S^1$". For $\ell\ge1$ that neighbourhood is constructed only under [FL5, Hypothesis 7.8.1].

  What [FL1]–[FL2b] actually establish is listed in §9 below.

### 6.5 Geometric representatives avoid lower strata: [FL2b, Lemma 3.15] (`lem:CyclesExtension`) and [FL2b, Corollary 3.18] (`cor:IntersectionOfSmoothLowerStrata`)

**Corollary 3.18.** *Let $z\in\mathbb A(X)$ be intersection-suitable and $\delta_c\ge0$ an integer with $\deg(z)+2\delta_c=\dim(\mathcal M^{*,0}_{\mathfrak t}/S^1)-1=d_a+2n_a-2$. Then for generic choices of geometric representatives, the intersection $\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{\delta_c}\cap\bar{\mathcal M}^{*,0}_{\mathfrak t}/S^1$ is a collection of one-dimensional manifolds, disjoint from the lower strata of $\bar{\mathcal M}^*_{\mathfrak t}/S^1$.*

**Role.** This is a dimension count on the lower-level irreducible strata $\mathcal M^{*,0}_{\mathfrak t_\ell}/S^1\times\Sigma$, using (3.20) and the codimension bounds [FL2b, (3.24)–(3.25)]. It presupposes that these strata are smooth of the expected dimension. It concerns only the irreducible, non-zero-section part. FL remark that the description of the closures of the representatives in the lower strata "is incomplete, as it does not give the multiplicities".

---

## 7. Seiberg–Witten strata at every level, and the level formula

### 7.1 Splitting criterion: [FL2b, Lemma 3.32] (`lem:SplittingSpinu`)

**Statement.** *A spin$^u$ structure $\mathfrak t$ on $X$ admits a splitting $\mathfrak t=\mathfrak s\oplus\mathfrak s'$ if and only if*
$$(c_1(\mathfrak t)-c_1(\mathfrak s))^2=p_1(\mathfrak t)\quad[\text{FL2b},(3.63)].$$

**Text that follows.** "If $c_1(\mathfrak s)$ obeys
$$(c_1(\mathfrak t)-c_1(\mathfrak s))^2=p_1(\mathfrak t)+4\ell\quad[\text{FL2b},(3.64)]$$
for some non-negative integer $\ell$, then there is a topological embedding of $M_{\mathfrak s}$ into the lower-level PU(2)-monopole moduli space $\mathcal M_{\mathfrak t_\ell}\times\mathrm{Sym}^\ell(X)$."

### 7.2 Level formula: [FL5, §2.3.3, equation (2.3.14)] (`eq:ReducibleLevel`)

**Statement.** "If $\mathfrak g_{\mathfrak t(\ell)}\cong i\underline{\mathbb R}\oplus L$ where $c_1(L)=c_1(\mathfrak t)-c_1(\mathfrak s)$, then $p_1(\mathfrak g_{\mathfrak t(\ell)})=(c_1(\mathfrak t)-c_1(\mathfrak s))^2$. Hence, for
$$\ell(\mathfrak t,\mathfrak s)=\tfrac14\big((c_1(\mathfrak t)-c_1(\mathfrak s))^2-p_1(\mathfrak t)\big),$$
the embedding (2.3.12) gives an inclusion of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ into $I\mathcal M_{\mathfrak t}$, where $\ell=\ell(\mathfrak t,\mathfrak s)$."

**Equivalent forms in the sources.** Each is checked against (2.3.14):
- With $\Lambda=c_1(\mathfrak t)$ and $\kappa=-\tfrac14p_1(\mathfrak t)$: $\ell(\mathfrak t,\mathfrak s)=\kappa+\tfrac14(c_1(\mathfrak s)-\Lambda)^2$.
- [FL5, Theorem 1] (`thm:MainThm`), with $\dim M^w_\kappa=2\delta$: $\ell=\tfrac14\big(\delta+(c_1(\mathfrak s)-\Lambda)^2+\tfrac34(\chi+\sigma)\big)$. This agrees because $p_1(\mathfrak t)=-\delta-\tfrac34(\chi+\sigma)$.
- [FL2b, Remark 3.36] (`rmk:WhereDoTheSWSpacesLie`): $\ell(\mathfrak t,\mathfrak s)=\tfrac18\big(d_a-2r(\Lambda,\mathfrak s)\big)$, with $r(\Lambda,c_1(\mathfrak s))=-(c_1(\mathfrak s)-\Lambda)^2-\tfrac34(\chi+\sigma)$ ([FL2b, (1.12)]). Seiberg–Witten strata with non-trivial invariants lie in levels $0\le\ell\le\tfrac18(d_a-2r(\Lambda))$.
- [FL2b, §1.3] (the subsection "Remarks and conjectures for formulas for Donaldson invariants involving Seiberg–Witten strata in arbitrary levels", text after (1.21)): $\ell=\tfrac14(\delta-r(\Lambda,c_1(\mathfrak s)))$.
- [FLov, §2.4]: $\mathrm{Red}_\ell(\mathfrak t)=\{\mathfrak s:(c_1(\mathfrak s)-c_1(\mathfrak t))^2=p_1(\mathfrak t)+4\ell\}$ and $\overline{\mathrm{Red}}(\mathfrak t)=\bigcup_{\ell\ge0}\mathrm{Red}_\ell(\mathfrak t)$. "A level-$\ell$ reducible is of the form $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)\subset\mathcal M_{\mathfrak t(\ell)}\times\mathrm{Sym}^\ell(X)$."
- [FL6, §3]: top-level Seiberg–Witten spaces satisfy $(c_1(\mathfrak s)-\Lambda)^2=p_1(\mathfrak t)$, and $\delta=-p_1(\mathfrak t)-3\chi_h$.

**Integrality** (my remark, not stated by FL). $\Lambda-c_1(\mathfrak s)\equiv w_2(\mathfrak t)\pmod 2$ for every spin$^c$ structure $\mathfrak s$, and $p_1(\mathfrak t)\equiv w^2\pmod 4$. Hence $(c_1(\mathfrak t)-c_1(\mathfrak s))^2-p_1(\mathfrak t)\in4\mathbb Z$, so $\ell(\mathfrak t,\mathfrak s)$ is always an integer. Only $\mathfrak s$ with $0\le\ell(\mathfrak t,\mathfrak s)\le N$ and $M_{\mathfrak s}\ne\emptyset$ contribute. There are finitely many ([FL2b], after Theorem 3.33).

### 7.3 Dimensions: [FL5, (2.3.10), (2.3.23), (2.3.24)]

The Seiberg–Witten moduli space has $\dim M_{\mathfrak s}=d_s(\mathfrak s)=\tfrac14(c_1(\mathfrak s)^2-2\chi-3\sigma)$ ([FL5, (2.3.10)]). For generic perturbations it is a compact, orientable smooth manifold if it contains no zero-section pairs.

For $\mathfrak t=\mathfrak s\oplus\mathfrak s\otimes L$ ([FL5, (2.3.23)–(2.3.24)], citing [FL2a, (2.47), (3.35)]):
$$\dim\mathcal M_{\mathfrak t}=2n_s(\mathfrak t,\mathfrak s)+d_s(\mathfrak s),\qquad n_s'=-(c_1(\mathfrak t)-c_1(\mathfrak s))^2-\tfrac12(\chi+\sigma),\qquad n_s''=\tfrac18\big((c_1(\mathfrak s)-2c_1(\mathfrak t))^2-\sigma\big).$$
Here $n_s=n_s'+n_s''$ is minus the complex index of the normal deformation operator. The source has an unbalanced parenthesis in $n_s''$; the reading above is the one consistent with $n_s''$ being the index of the Dirac operator on $W^+\otimes L$, and it makes (2.3.23) agree with (2.1.12) (checked).

**Derived for level $\ell$** (my arithmetic, not stated in this form by FL). Apply (2.3.23) to $\mathfrak t(\ell)=\mathfrak s\oplus\mathfrak s\otimes L$. Then $\dim\mathcal M_{\mathfrak t(\ell)}=2n_s(\mathfrak t(\ell),\mathfrak s)+d_s(\mathfrak s)$, and $n_s$ is given by the same expressions, because they involve only $c_1(\mathfrak t)$ and $c_1(\mathfrak s)$. The stratum $M_{\mathfrak s}\times\Sigma$ has dimension $d_s(\mathfrak s)+\dim\Sigma$. The top stratum of $\bar{\mathcal M}_{\mathfrak t}$ has dimension $d(\mathfrak t)=2n_s(\mathfrak t(\ell),\mathfrak s)+d_s(\mathfrak s)+6\ell$. So the expected codimension of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ (top stratum of $\mathrm{Sym}^\ell$) in $\bar{\mathcal M}_{\mathfrak t}$ is $2n_s(\mathfrak t(\ell),\mathfrak s)+2\ell$. [FLL1, §3] gives the corresponding dimensions for $\ell=1$, in terms of $r_N$: $\dim(M_{\mathfrak s}\times X)=d_s(\mathfrak s)+4$.

### 7.4 What is, and is not, asserted about the Seiberg–Witten strata

**Proved at every level, as sets and manifolds.** [corrected by checker] For $\ell\ge1$, the items below are the top-level results of [FL2a] applied to the spin$^u$ structure $\mathfrak t(\ell)$. FL do not state them separately for lower levels, but no new analysis is needed.
- $M_{\mathfrak s}$ is a compact smooth manifold of dimension $d_s(\mathfrak s)$ (§4.3). [corrected by checker] Zero-section points are absent when $w$ is good, $b_2^+>0$ and $g$ is generic, because then $c_1(\mathfrak s)-\Lambda\equiv w$ is not torsion ([FL2a, Remark 2.14]; [FL5, §2.3.2]). [FL2a, Corollary 3.3], cited here previously, assumes the Morgan–Mrowka criterion of [FL2a, Lemma 3.2], not goodness. Both hold in the blown-up setting.
- It embeds topologically in $\mathcal M_{\mathfrak t(\ell)}$ as the reducible locus for the splitting ([FL2a, Lemma 3.13], applied to $\mathfrak t(\ell)$), and smoothly in $\mathcal C^0_{\mathfrak t(\ell)}$ ([FL2a, Lemma 3.16]).
- Hence $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)\subset I\mathcal M_{\mathfrak t}$ ([FL5, (2.3.14)]). Each $M_{\mathfrak s}\times\Sigma$ is a smooth manifold.
- By [FL2a, Proposition 3.1] (applied at level $\ell$) and good $w$, every reducible point of $\bar{\mathcal M}_{\mathfrak t}$ at level $\ell$ lies in some $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ with $\ell(\mathfrak t,\mathfrak s)=\ell$.

**Not proved: regularity.** Points of $M_{\mathfrak s}$ are not known to be regular points of $\mathcal M_{\mathfrak t(\ell)}$, and FL say they need not be [corrected by checker: FL do not prove non-regularity] ([FL1, after Remark 1.4]; [FL2a, §3.4]: "the linearization … need not be surjective at a reducible solution and so the points of $M_{\mathfrak s}$ might not be regular points of $\mathcal M_{\mathfrak t}$").

**Proved only at the top level: neighbourhood structure.** For $\ell=0$, a topological model of a neighbourhood of $M_{\mathfrak s}$ in $\mathcal M_{\mathfrak t}$ is given by [FL2a, Theorem 3.21] (`thm:ThickenedModuliSpace`), restated in [FL5, §2.3.5]. It has a virtual normal bundle $N_{\mathfrak t,\mathfrak s}$, an obstruction bundle $\Xi_{\mathfrak t,\mathfrak s}$ and a section $\boldsymbol\chi_{\mathfrak s}$, with
$$\boldsymbol\gamma_{\mathfrak s}:\boldsymbol\chi_{\mathfrak s}^{-1}(0)\cap N_{\mathfrak t,\mathfrak s}(\varepsilon)\cong\mathcal M_{\mathfrak t}\cap\boldsymbol\gamma_{\mathfrak s}(N_{\mathfrak t,\mathfrak s}(\varepsilon))\quad[\text{FL5},(2.3.22)].$$
This is a homeomorphism, and a diffeomorphism off $M_{\mathfrak s}$. [corrected by checker] Both [FL2a, Theorem 3.21] and [FL5, §2.3.5] assume that $M_{\mathfrak s}$ contains no zero-section pairs. The homeomorphism (2.3.22) is [FL5]'s formulation. [FL2a, Theorem 3.21] itself states four things:
1. Regularity of the thickened moduli space $\mathcal M_{\mathfrak t}(\Xi,\mathfrak s)$ near $\iota(M_{\mathfrak s})$.
2. $M_{\mathfrak s}$ is a smooth submanifold of it.
3. $N_{\mathfrak t}(\Xi,\mathfrak s)$ is its normal bundle, with equivariant tubular map.
4. The restriction of $\mathfrak S$ takes values in $\Xi$ and vanishes transversely off $\iota(M_{\mathfrak s})$.

**Not proved: neighbourhood structure at lower levels.** For $\ell\ge1$, no neighbourhood structure is proved in these sources:
- [FL3, Theorem 1.1] constructs local gluing maps and obstruction sections on a bundle of gluing data $\mathbf{Gl}^+(\mathcal U_{\ell,\mu},\Sigma,\lambda_0)\to\mathcal U_{\ell,\mu}\times\Sigma$ for each stratum $\Sigma$, with $\boldsymbol\gamma(\boldsymbol\chi^{-1}(0))\subset M^{*,0}(\mathfrak t)$.
  - [corrected by checker: hypotheses added] It assumes the following: $b^+(X)>0$; generic parameters; no SO(3) bundle with $w_2\equiv w$ admits a flat connection; $\kappa\ge1$ and $0<\ell<\lfloor\kappa\rfloor$.
  - The base $\mathcal U_{\ell,\mu}$ is a precompact open subset of a *thickened* moduli space $M(\mathfrak t_\ell,\mu)$, described as "a tubular neighborhood of $\mathcal U_{\ell,\mu}\cap M^{*,0}(\mathfrak t_\ell)$". The theorem does not say explicitly that reducible backgrounds in $M_{\mathfrak s}$ are allowed [unconfirmed]. [FL6, Remark 3.3] states that "We have established the existence of local gluing maps in [FL3]" for neighbourhoods of $M_{\mathfrak s}\times\Sigma$.
  - [FL3, §1.5.1] lists continuity on the Uhlenbeck closure of the gluing data, the embedding property and surjectivity as *not* proved there, and defers them to [FL4].
- Continuity in the Uhlenbeck topology, injectivity and surjectivity onto a neighbourhood are assumed: [FL5, Hypothesis 7.8.1] (`hyp:Gluing`); [FL6, Hypothesis 3.1] (`hyp:Local_gluing_map_properties`) and [FL6, Remark 3.3].
  - [corrected by checker] [FL5, Hypothesis 7.8.1] assumes more than this. It posits a continuous $S^1$-equivariant embedding $\boldsymbol\gamma_{\mathcal M}:\bar{\mathcal M}^{\mathrm{vir}}_{\mathfrak t,\mathfrak s}\to\bar{\mathcal C}_{\mathfrak t}$ that is homotopic through such embeddings to the global splicing map, smooth on strata, and equal to the identity on $N_{\mathfrak t(\ell),\mathfrak s}(\delta)\times\mathrm{Sym}^\ell(X)$. It also posits sections $\boldsymbol\chi_s,\boldsymbol\chi_i$ with four properties:
    - (1) the restriction of $\bar{\boldsymbol\chi}=\boldsymbol\chi_s\oplus\boldsymbol\chi_i$ to each stratum is smooth;
    - (2) that restriction vanishes transversely on each stratum;
    - (3) the $L^2$ norm of $\bar{\boldsymbol\chi}$ is lower semi-continuous;
    - (4) $\boldsymbol\gamma_{\mathcal M}$ restricts to a homeomorphism of $\bar{\boldsymbol\chi}^{-1}(0)$ onto an open neighbourhood of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in $\bar{\mathcal M}_{\mathfrak t}$.
  - [FL6, Hypothesis 3.1] asserts only that the local gluing map "gives a continuous parametrization of a neighborhood of $M_{\mathfrak s}\times\Sigma$ in $\bar{\mathcal M}_{\mathfrak t}$". [FL6] says this is "recorded, in greater detail, as Conjecture 6.7.1 in [FL5]". In the [FL5] version read here (Memoirs AMS, December 2018) it is Hypothesis 7.8.1.
- [FLL1, Theorem 3.8] (`thm:GluingThm`, $\ell=1$) is attributed to "[FL3, FL4]". [FL4] ("PU(2) monopoles IV: surjectivity of gluing maps") is listed as "in preparation" in every bibliography consulted.
- [corrected by checker: added] [FL5, §7.9] ("Notes on the justification of the local gluing hypothesis") says its purpose is "to summarize the justification of Hypothesis 7.8.1 as a theorem, whose proof is provided by the authors in [Feehan_Leness_monopolegluingbook]". That reference is listed in the [FL5] bibliography as "in preparation, based in part on arXiv:math/9812060 and arXiv:math/9907107". [FL5, §7.9.4] (lower-level singular stratum) says that the anti-self-dual gluing theory "generalizes *formally*" to SO(3) monopoles, but that the analysis needed for all the properties in Hypothesis 7.8.1 "do[es] not extend in a straightforward manner". It outlines only the construction of a stabilizing bundle $\Xi=\Xi_1\oplus\mathrm{Coker}\,\mathbf D$ over spliced pairs.

These matters belong to items (c) and (d) of the round.

**My reading, flagged.** The compactness results show only that the reducible points of $\bar{\mathcal M}_{\mathfrak t}$ at level $\ell$ lie *in* $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$. I found no statement in (b)-level results that every point of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ lies in the closure $\bar{\mathcal M}_{\mathfrak t}$. FL nonetheless speak of "the Seiberg–Witten stratum $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in $\bar{\mathcal M}_{\mathfrak t}/S^1$" ([FL5, §2.6]; [FL6, §3]). [FL5, Hypothesis 7.8.1(4)] speaks of "an open neighborhood of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in $\bar{\mathcal M}_{\mathfrak t}$". Whether all of it lies in the closure would be a gluing statement. [corrected by checker: supporting evidence added] [FLL1, §3] (opening of "Gluing SO(3) monopoles", display (3.1)) is careful on this point: it writes the Seiberg–Witten stratum as $(M_{\mathfrak s}\times\mathrm{Sym}^\ell(X))\cap\bar{\mathcal M}_{\mathfrak t}\subset\bar{\mathcal M}_{\mathfrak t}$. This confirms that the inclusion $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)\subset\bar{\mathcal M}_{\mathfrak t}$ is not taken for granted there.

### 7.5 [corrected by checker: added] How [FL2b] treats lower-level reducibles: Theorem 3.33, Conjecture 3.34, Corollary 3.35

- **[FL2b, Theorem 3.33]** (`thm:CompactReductionFormula`) is the cobordism formula proved in [FL2b]. Its hypotheses are $b_2^+>0$, $w\pmod 2$ good, $z$ intersection-suitable with $d_a\le\deg z\le d_a+2n_a-2$, and the following explicit assumption: "Assume that the set of isomorphism classes of spin$^c$ structures, $\mathfrak s$, defining reducible PU(2) monopoles in $\bar{\mathcal M}_{\mathfrak t}$ all obey condition (3.63), and so non-empty Seiberg–Witten moduli strata $\iota(M_{\mathfrak s})$ appear only in the top level." In other words, the only theorem in [FL2b] relating the invariants *assumes* that there are no reducibles in the lower levels.
- **[FL2b, Conjecture 3.34]** (`conj:Multiplicity`, citing [FKLM, Conjecture 3.1]) concerns $\mathfrak t_\ell=\mathfrak s\oplus\mathfrak s'$ with $\iota(M_{\mathfrak s})$ in level $\ell$. It conjectures that the pairing with $\mathbf L_{\mathfrak t,\mathfrak s}$ is a multiple of $SW_X(\mathfrak s)$.
  - FL write that "The difficulty lies in the appropriate construction of the link $\mathbf L_{\mathfrak t,\mathfrak s}$ of a Seiberg–Witten moduli space when $\ell=\ell(\mathfrak t,\mathfrak s)>0$". They say the conjecture holds for $\ell=0$ ([FL2b, Theorem 4.13]) and for $\ell=1$ in [FLL1].
  - [FLL1] rests on [FLL1, Theorem 3.8], which is attributed to [FL3, FL4] (see §7.4). FL also say it can be seen for $\ell=2$ "by adapting Leness's proof of the wall-crossing formula"; no proof is given.
- **[FL2b, Corollary 3.35]** relaxes the top-level hypothesis of Theorem 3.33, *conditionally on Conjecture 3.34*.
- **[FL2b, §3, introduction]**: "A description of neighborhoods the strata of lower-level reducibles, sufficient to define links, will be given in [FL3], [FL4]." [FL2b, §1.3] presents the formulas for Seiberg–Witten strata in arbitrary levels as conjectures ("their conservatively-stated current status as conjectures rather than firm assertions").
- [FL2b, (4.61)] (`eq:LevelOfReducible`) gives one more form of the level formula: $4\ell(\mathfrak t,\mathfrak s)=\tfrac12 d_a(\mathfrak t)-r(\Lambda,c_1(\mathfrak s))\le\tfrac12d_a(\mathfrak t)-r(\Lambda)$, consistent with §7.2.


---

## 8. Strata of $\mathrm{Sym}^\ell(X)$: [FL5, §3.1–3.2]

**Definitions.**
- For a partition $\mathcal P=\{P_1,\dots,P_r\}$ of $N_\ell=\{1,\dots,\ell\}$ ([FL5, (3.1.4)]), $\Delta^\circ(X^\ell,\mathcal P)=\{(x_i):x_i=x_j\iff i,j\text{ lie in a common }P\in\mathcal P\}$, and $\Delta(X^\ell,\mathcal P)$ is its closure ([FL5, (3.1.5)]).
- The stratum is $\Sigma(X^\ell,\mathcal P):=\tilde\pi_\ell(\Delta^\circ(X^\ell,\mathcal P))=\Delta^\circ(X^\ell,\mathcal P)/W(\mathcal P)$ ([FL5, (3.1.8)–(3.1.9)]). It has dimension $4r$.

**[FL5, Lemma 3.2.4]** (`lem:IncidenceRelationInSymmetricProduct`): $\Sigma(X^\ell,\mathcal P)\subset\mathrm{cl}\,\Sigma(X^\ell,\mathcal P')$ if and only if some conjugate of $\mathcal P'$ refines $\mathcal P$.

**Related statements.** [FL1, §1.1.3]: "The space $\mathrm{Sym}^\ell(X)$ is smoothly stratified, the strata being enumerated by partitions of $\ell$." [FL5, §4.1] notes that $\mathrm{Sym}^\ell(X)$ is Whitney stratified ([Pflaum, Theorem 4.3.7]) and constructs an explicit *partial* Thom–Mather structure in Chapter 4. Only the first control condition holds exactly; the failure of the second is controlled.

---

## 9. Summary: what is proved smooth or regular, and what is only described topologically

| Object | Smooth manifold? | Points regular in the ambient moduli space? | Local structure of $\bar{\mathcal M}_{\mathfrak t}$ near it | Source |
|---|---|---|---|---|
| $\mathcal M^{*,0}_{\mathfrak t}$ (top level, irreducible, $\Phi\ne0$) | Yes, dimension $d_a+2n_a$, generic $(g,\rho,\tau,\vartheta)$ | Yes | It is the top stratum | [FL5, Thm 2.1.1] = [FL2a, Thm 2.13] (proof in [FeehanGenericMetric]); [FL1, Thm 1.3] for holonomy perturbations |
| $\mathcal M^{*,0}_{\mathfrak t(\ell)}\times\Sigma$, $\ell\ge1$ | Yes, dimension $d(\mathfrak t)-6\ell+\dim\Sigma$ | Yes, in $\mathcal C_{\mathfrak t(\ell)}$ | Neighbourhoods in $\bar{\mathcal M}_{\mathfrak t}$ (that is, gluing) are not described | [FL1, Thm 1.3] and §5.1.3 (outline only, holonomy setting); in the generic-metric setting, implicit by applying [FL2a, Thm 2.13] to each $\mathfrak t(\ell)$ |
| $M^w_\kappa$ (top-level zero-section) | Yes for generic $g$ ($b_2^+>0$, $w$ good; twisted reducibles per [FL2a, Lemma 3.5]) | No in general: $H^2_{A,0}\supset\mathrm{coker}(D_A+\rho(\vartheta))$ | Local Kuranishi model at each point | [FL2a, Lemma 3.4, Cor 3.6] |
| $M^w_{\kappa-\ell}\times\Sigma$, $\ell\ge1$ | Yes (usual Uhlenbeck strata, generic $g$) | Not guaranteed (same Dirac cokernel issue as at level 0) [corrected by checker] | None given; FL use only the continuous function $\lVert\Phi\rVert_{L^2}^2$ to define the instanton link | [FL2b, Lemma 3.21]; [FL2a, Def 3.7, Lemma 3.8] |
| $M_{\mathfrak s}$ in level 0 | Yes, compact, dimension $d_s$, generic $\tau$ with $\|\tau-\mathrm{id}\|_{C^0}<1/64$, provided there are no zero-section pairs [corrected by checker]; smooth submanifold of $\mathcal C^0_{\mathfrak t}$ | Not claimed; FL say they need not be regular [corrected by checker] | Topological: homeomorphism from obstruction zero set in the virtual normal bundle | [FL2a, Prop 2.16, Lemma 3.16, Thm 3.21] |
| $M_{\mathfrak s}\times\Sigma$ in level $\ell=\ell(\mathfrak t,\mathfrak s)\ge1$ | Yes (product) | Not claimed; not guaranteed [corrected by checker] | Only under a gluing hypothesis (local gluing maps exist by [FL3, Thm 1.1], stated for $0<\ell<\lfloor\kappa\rfloor$ with background in a thickened moduli space; continuity, injectivity, surjectivity, and in [FL5] also stratumwise transversality of the obstruction section and lower semicontinuity of its norm, are assumed [corrected by checker]) | [FL5, (2.3.14), Hyp 7.8.1]; [FL6, Hyp 3.1]; [FLL1, Thm 3.8] (attributed to [FL3, FL4]) |
| $\bar{\mathcal M}_{\mathfrak t}$ as a whole | Compact, second-countable, Hausdorff | n/a | A disjoint union of the pieces above (with $w$ good, [FL5, (2.2.2)]). The condition of the frontier, local finiteness, Whitney or Thom–Mather conditions and local conical structure are **not proved**. FL warn that the topology near lower levels "need not be locally finite" | [FL1, Thm 1.1]; [FL2b, §3 intro] |

---

## 10. Where a (b)-type statement would go beyond FL

This section is a neutral list for comparison with whatever analogue is needed; the manuscript's argument is not addressed here. Any of the following would be a statement FL do not prove in the sources read:

1. Regularity (vanishing $H^2$) at points of $M_{\mathfrak s}\times\Sigma$ or of $M^w_{\kappa-\ell}\times\Sigma$, at any level. [corrected by checker] FL do not claim regularity there. They state that it "need not" hold: points of $M_{\mathfrak s}$ "might not be regular points" ([FL2a, §3.4]), and zero-section points have $H^2_{A,0}\supset\mathrm{Coker}(D_A+\rho(\vartheta))$. They identify the cokernels ([FL2a, Lemma 3.4]; [FL2a, §3.5, Theorem 3.21] for $\ell=0$, via a stabilizing bundle). They do not prove that regularity fails in any particular case.
2. A local description (cone, Kuranishi or gluing model) of $\bar{\mathcal M}_{\mathfrak t}$ near a lower-level point. Such a description exists only near top-level zero-section points ([FL2a, Corollary 3.6]) and top-level reducibles ([FL2a, Theorem 3.21]). For $\ell\ge1$ it is hypothesised ([FL5, Hypothesis 7.8.1]; [FL6, Hypothesis 3.1]). [corrected by checker] The proof is deferred to a monograph listed as "in preparation" ([FL5, §7.9]).
3. That $\bar{\mathcal M}_{\mathfrak t}$, or $\bar{\mathcal M}_{\mathfrak t}/S^1$, is a stratified space with the condition of the frontier, locally finite topology, or Whitney or Thom–Mather conditions. Only the weak decomposition of [FL2b, Definition 3.2] is available. [FL2b, §3] explicitly leaves local finiteness open.
4. That every point of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$, $\ell\ge1$, lies in the closure $\bar{\mathcal M}_{\mathfrak t}$. Only the inclusion of the reducible part of the closure into $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ follows from the compactness results.
5. Simultaneous transversality of all lower levels in the generic-metric setting. This is implicit (applying [FL2a, Theorem 2.13] to each $\mathfrak t(\ell)$) but not stated as a theorem. In the holonomy setting it is [FL1, Theorem 1.3], proved for $\ell>0$ only in outline (§5.1.3).
6. Compactness with perturbations that are not small. [FL1]'s proof needs $\|\tau-\mathrm{id}\|_{L^\infty}\le1/64$ and $\|\vartheta\|_{L^\infty_1}\le1$ (more precisely [FL1, (2.34)]). The restatements omit this.

---

## 11. Uncertainties

1. **Published numbering of [FL1].** All [FL1] numbers are from the arXiv source of 29 Oct 1997. [FL2b] cites [FL1, Theorem 1.2] for compactness, [FL1, Proposition 2.12] (slice) and [FL1, Theorem 5.10] (local-to-global), and [FL2a] cites [FL1, Equation (2.37)] for the deformation complex. The arXiv source gives Theorem 1.1, Proposition 2.8, Theorem 5.11 and (2.44). The J. Differential Geom. version probably differs, and I could not check it.
2. **Numbering method.** Numbers were computed from counters by script, and the equation numbering assumes standard amsmath behaviour for align-type environments. Spot checks against cross-citations agree, except for the [FL1] citations in item 1 and [FL5]'s "[FL2b, Lemma 3.30]" for the instanton pairing, which is Proposition 3.29 in the [FL2b] source read ([FL6] cites it correctly as Proposition 3.29).
3. **[FeehanGenericMetric].** The proof of the generic-metric transversality theorem ([FL5, Theorem 2.1.1] = [FL2a, Theorem 2.13]) is in [FeehanGenericMetric] and [TelemanGenericMetric]. Neither was among the sources, so the precise class of generic parameters is taken from the restatements.
4. **Simultaneous transversality for all $\mathfrak t(\ell)$.** In the generic-metric setting this is my inference, from the countable intersection of residual sets and the product structure of the levels; FL use it without stating it.
5. **[FL2b, Lemma 3.21].** Its proof is a sketch that appeals to Taubes' gluing theorem for unobstructed ASD connections. Whether "generic metric" suffices for all lower-level ASD strata to be unobstructed is asserted, not proved, in that text.
6. **Dependence of $N$.** The versions differ: [FL1] (curvatures of the connections on $W$ and $\det E$, $c_2(E)$; in the proof also $g$); [FL5] (scalar curvature, $\det V^+$ connection, $p_1$); [FL2a] and [FLL1] (no scalar curvature). The proof supports [FL5]'s version.
7. **[FLov].** Its §2 is expository. It writes the unperturbed equations, says "$\kappa=p_1(\mathfrak t)$" (a slip for $-\tfrac14p_1$), and calls $\bar{\mathcal M}_{\mathfrak t}/S^1$ a "smoothly-stratified cobordism". None of these should be cited as theorems.
8. **Typos in the sources.** [FL2b, (3.21)] has $(\chi+2\sigma)$ for $(\chi+\sigma)$. [FL5, (2.3.24)] has an unbalanced parenthesis. [FL5, (2.1.10)] omits $\Phi$ in $\rho(\vartheta)\Phi$.
9. **[KMStructure].** The twisted-reducibles statement ([FL2a, Lemma 3.5]) and the generic-metric refinement ([KMStructure, Lemma 2.4], cited in [FL1, remark after Corollary 5.6]) are taken from FL's restatements. I did not check them against Kronheimer–Mrowka.
10. **[FLL1].** I read [FLL1] only for its restatements (§2) and the statement of Theorem 3.8. I did not check whether its level-one link construction depends on unproved properties beyond those attributed to [FL4].
