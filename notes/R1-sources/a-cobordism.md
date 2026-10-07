# (a) The SO(3)-monopole cobordism formula: statements, hypotheses, and use

Extraction note from the arXiv LaTeX sources of Feehan–Leness (FL). All statements below are copied, with light cleaning of the LaTeX, from the files listed in Section 0. Nothing has been added to any hypothesis; where the sources are inconsistent, this is recorded rather than silently corrected.

---

## 0. Sources and numbering conventions

| Short name used here | arXiv | File read | Theorem numbering in the source |
|---|---|---|---|
| Memoir | math/0203047 (v4, dated 26 Dec 2018; *Mem. Amer. Math. Soc.* 256 (2018), no. 1226) | `FeehanLenessMonopoleCobordism_v4-clean.tex` | `amsbook`; `thm` numbered within section, section within chapter, so numbers are *chapter.section.n*; all theorem-like environments except `case`, `step`, `ack`, `conc`, `note`, `summ` share the `thm` counter (including the unnumbered-looking `notn`). The main theorem uses a separate counter `mainthm`, shared with `mainconj`: hence "Theorem 1" and "Conjecture 2". Equations are numbered *chapter.section.n*. |
| FL6 | math/0609530 (*J. Eur. Math. Soc.* 17 (2015) 899–923; source dated 22 Nov 2014) | `jems-feehanleness_PF11-22-2014.tex` | `article`; one counter `thm` within section, shared by Corollary, Conjecture, Lemma, Proposition, **Main Theorem**, Definition, Hypothesis, Remark. |
| FL2b | dg-ga/9712005 (PU(2) monopoles II) | `main.tex` | `amsart`; *section.n*, shared counter. |
| FL2a | math/0007190 (PU(2) monopoles and links of top-level SW moduli spaces) | `main.tex` | same convention. |
| FLLevelOne | math/0106238 | `main.tex` | same convention. |
| FL3 | math/9907107 (PU(2) monopoles III) | `main.tex` | same convention. |
| Overlap paper | 1211.0480 (SO(3)-monopoles: the overlap problem; Fields Inst. Commun. 47 (2005)) | `main.tex` | `amsart`; `thm` within section shared by Lemma, Definition, Example, Exercise, Conjecture, Remark; **Proposition has its own counter**. |
| Announcement | dg-ga/9709022 (PU(2) monopoles and relations between four-manifold invariants) | `main.tex` | `amsart`; *section.n*, shared counter. |
| Gluing via corners [added by checker] | 1910.14580 (Feehan–Leness, *Gluing in geometric analysis via maps of Banach manifolds with corners and applications to gauge theory*) | `kuranishi_model_boundary_moduli_space.tex` | `mainthm`/`maincor` share one global counter ("Theorem 1–3", "Corollary 4–7"). |

All theorem and equation numbers below were inferred by me from the LaTeX counters of these files (the compiled PDFs were not consulted). The `\label` is given for each. Equation numbers were obtained by a cruder count and should be treated as indicative; the labels are reliable. [checker: an independent recount of the theorem counters, skipping commented-out and `comment`-environment text, reproduces every theorem, lemma, proposition, definition, hypothesis and conjecture number used in this note for the Memoir, FL6, FL2a, FL2b, FLLevelOne, FL3, the overlap paper and the Announcement. An independent equation counter reproduces every equation number spot-checked: Memoir (1.1.1), (2.1.6), (2.1.10), (2.1.13), (2.1.14), (2.2.3), (2.3.10), (2.3.11), (2.3.14), (2.5.1)–(2.5.4), (2.6.1), (2.6.2), (7.8.1), (8.1.18), (8.1.20), (8.1.21), (10.1.1), (10.6.7)–(10.6.10); FL6 (1.1), (1.2), (2.2), (2.5), (2.6), (2.9), (2.12), (2.13), (3.1)–(3.5), (4.1), (4.4), (4.6), (4.7), (4.13); FL2b (1.6), (1.11), (1.12), (1.19)–(1.21), (3.60), (3.66), (4.62).] There is evidence that published numberings differ from the arXiv ones in places (see the list of uncertainties at the end).

The Kronheimer–Mrowka structure paper (*Embedded surfaces and the structure of Donaldson's polynomial invariants*, J. Differential Geom., 1995) is not on arXiv. Its structure theorem is given below **only as restated in the FL papers**.

---

## 1. Notation needed to read the statements

All of the following is from Memoir, Chapter 2, unless another source is named.

**Four-manifolds.** $X$ is closed, connected, oriented and smooth; $\chi$, $\sigma$ are its Euler characteristic and signature. FL6 calls $X$ *standard* if, in addition, $b_1(X)=0$ and $b^+(X)\ge 3$ is odd (FL6, §1.1). FL6 also writes
$$c_1^2(X):=2\chi+3\sigma,\qquad \chi_h(X):=\tfrac14(\chi+\sigma),\qquad c(X):=\chi_h-c_1^2=-\tfrac14(7\chi+11\sigma)$$
(FL6 eqs. `eq:Definec1SquaredandHolcEulerChar` (1.1), `eq:Defn_c(X)` (2.12); the Memoir and FL2b use $c(X)=-\frac14(7\chi+11\sigma)$ directly).

**Spin$^c$ and spin$^u$ structures.** A spin$^c$ structure is $\mathfrak s=(\rho,W)$ with $c_1(\mathfrak s)=c_1(W^+)$. A spin$^u$ structure is $\mathfrak t=(\rho,V)$ with $V$ of complex rank eight; given $W$ one has $V\cong W\otimes E$ with $E$ of rank two, $\mathfrak g_{\mathfrak t}=\mathfrak{su}(E)$, and
$$c_1(\mathfrak t)=\tfrac12c_1(V^+),\qquad p_1(\mathfrak t)=p_1(\mathfrak g_{\mathfrak t}),\qquad w_2(\mathfrak t)=w_2(\mathfrak g_{\mathfrak t})$$
(Memoir eq. `eq:SpinUCharacteristics`). FL6 (eq. `eq:Defn_Lambda_kappa_w` (3.1)) sets
$$\Lambda:=c_1(\mathfrak t),\qquad \kappa:=-\tfrac14\langle p_1(\mathfrak t),[X]\rangle,\qquad w:=c_1(E).$$

**Moduli spaces and dimensions.** $\mathcal M_{\mathfrak t}$ is the moduli space of solutions of the perturbed SO(3)-monopole equations (Memoir eq. `eq:PerturbedSO3MonopoleEquations` (2.1.10)), with a circle action induced by scalar multiplication on $V$. Memoir Theorem 2.1.1 (`thm:Transv`, quoting Feehan's generic-metric theorem and Teleman) gives, for generic parameters, $\dim\mathcal M^{*,0}_{\mathfrak t}=d_a(\mathfrak t)+2n_a(\mathfrak t)$ with
$$d_a(\mathfrak t)=-2p_1(\mathfrak t)-\tfrac32(\chi+\sigma),\qquad n_a(\mathfrak t)=\tfrac14\big(p_1(\mathfrak t)+c_1(\mathfrak t)^2-\sigma\big).$$
FL6 (§3) writes $\dim M^w_\kappa=2\delta$ with $\delta=-p_1(\mathfrak t)-3\chi_h$, $\dim\mathcal M_{\mathfrak t}=2\delta+2n_a$, and $n_a=\frac14(I(\Lambda)-\delta)$, where (FL6 eq. `eq:DefineIofLa` (3.2))
$$I(\Lambda)=\Lambda^2-\tfrac14(3\chi+7\sigma)=\Lambda^2+5\chi_h-c_1^2 .$$
This is the same quantity as $i(\Lambda)$ in Memoir Theorem 1 and as $i(\Lambda)=\Lambda^2+c(X)+\chi+\sigma$ in FL2b (eq. `eq:PositiveDiracIndexFunction` (1.11)). Thus $\delta<i(\Lambda)$ is exactly the condition $n_a>0$, i.e. that $M^w_\kappa$ has positive codimension in $\mathcal M_{\mathfrak t}$.

**Uhlenbeck compactification and levels.** For $\ell\ge0$, $\mathfrak t(\ell)$ is the spin$^u$ structure with $c_1(V_\ell)=c_1(V)$, $p_1(\mathfrak t(\ell))=p_1(\mathfrak t)+4\ell$, $w_2(\mathfrak t(\ell))=w_2(\mathfrak t)$ (eq. `eq:DefineLowerChargeSpinuStr` (2.1.13)). The space of ideal monopoles is $I\mathcal M_{\mathfrak t}=\bigsqcup_{\ell\ge0}\mathcal M_{\mathfrak t(\ell)}\times\mathrm{Sym}^\ell(X)$ (eq. `eq:idealmonopoles` (2.1.14)); $\bar{\mathcal M}_{\mathfrak t}$ is the closure in the Uhlenbeck topology (Definition 2.1.2, `defn:UhlenbeckConvergence`), and its intersection with $\mathcal M_{\mathfrak t(\ell)}\times\mathrm{Sym}^\ell(X)$ is its *$\ell$-th level*. Memoir Theorem 2.1.3 (`thm:Compactness`, quoting FL1, Theorem 1.1): there is $N$, depending at most on the scalar curvature, the curvature of the fixed connection on $\det(V^+)$, and $p_1(\mathfrak t)$, such that $\bar{\mathcal M}_{\mathfrak t}\subset\bigsqcup_{\ell=0}^N(\dots)$ is second-countable, compact and Hausdorff, with a continuous circle action.

**Reducible (Seiberg–Witten) strata and their level.** A pair is reducible with respect to $V=W\oplus W\otimes L$, with $c_1(L)=c_1(\mathfrak t)-c_1(\mathfrak s)$; the Seiberg–Witten moduli space $M_{\mathfrak s}$ embeds as the corresponding fixed set (Memoir §2.3, quoting FL2a, Lemma 3.13). [corrected by checker: as quoted in Memoir §2.3.3, FL2a Lemma 3.13 gives a topological embedding of $M^0_{\mathfrak s}=M_{\mathfrak s}\cap\mathcal C^0_{\mathfrak s}$ into $\mathcal M_{\mathfrak t}$, and of all of $M_{\mathfrak s}$ only "if $w_2(\mathfrak t)\neq0$ or $b_1(X)=0$". The identification of the image with pairs fixed by the circle action is a separate statement, FL2a Lemma 3.11, quoted in Memoir §2.3.4.] The level at which $M_{\mathfrak s}$ appears is (Memoir eq. `eq:ReducibleLevel` (2.3.14))
$$\ell(\mathfrak t,\mathfrak s)=\tfrac14\Big((c_1(\mathfrak t)-c_1(\mathfrak s))^2-p_1(\mathfrak t)\Big),$$
and then $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)\subset I\mathcal M_{\mathfrak t}$. In FL2b notation, with $r(\Lambda,c_1(\mathfrak s))=-(c_1(\mathfrak s)-\Lambda)^2-\frac34(\chi+\sigma)$ (eq. `eq:SWInTopLevelFunction` (1.12)), this level is $\frac18(d_a-2r(\Lambda,\mathfrak s))$ (FL2b Remark 3.36, `rmk:WhereDoTheSWSpacesLie`).

**Anti-self-dual stratum and its link.** The zero-section stratum is $M^w_\kappa$ with $\kappa=-\frac14p_1(\mathfrak t)$, $w\equiv w_2(\mathfrak t)\pmod 2$. A class $v\in H^2(X;\mathbb Z/2)$ is *good* if no integral lift of $v$ is torsion (Memoir Definition 2.2.1, `defn:Good`, quoting FL2b Definition 3.20). For good $w\pmod 2$ the link of $\bar M^w_\kappa$ in $\bar{\mathcal M}_{\mathfrak t}/S^1$ is $\bar{\mathbf L}^w_{\mathfrak t,\kappa}=\{[A,\Phi,\mathbf x]:\|\Phi\|^2_{L^2}=\varepsilon\}$ (eq. `eq:DefineASDLink` (2.2.3)). In practice goodness is arranged by passing to the blow-up $\tilde X=X\#\overline{\mathbb{CP}}^2$ and replacing $w$ by $w+\mathrm{PD}[e]$.

**Seiberg–Witten invariants.** For $b_1=0$ and odd $b^+>1$, $SW_X(\mathfrak s)=\langle\mu_{\mathfrak s^\pm}^d,[M_{\mathfrak s^\pm}(\tilde X)]\rangle$, $2d=d_s(\mathfrak s)=\frac14(c_1(\mathfrak s)^2-2\chi-3\sigma)$ (eqs. `eq:DimSW` (2.3.10), `eq:DefSW` (2.3.11)). $c_1(\mathfrak s)$ is a *SW basic class* if $\mu_{\mathfrak s}$ is non-trivial; *SW simple type* means all basic classes have $d_s(\mathfrak s)=0$. FL6 sets $B(X)=\{c_1(\mathfrak s):SW_X(\mathfrak s)\neq0\}$ and, to deal with 2-torsion, $SW'_X(K)=\sum_{\mathfrak s\in c_1^{-1}(K)}SW_X(\mathfrak s)$ (eq. `eq:DefineCohomSW` (2.2)).

**Cohomology classes and geometric representatives.** $\mu_p(\beta)=-\frac14p_1(\mathbb F_{\mathfrak t})/\beta$ on $\mathcal C^*_{\mathfrak t}/S^1$ and $\mu_c=c_1(\mathbb L_{\mathfrak t})$ on $\mathcal C^{*,0}_{\mathfrak t}/S^1$; $\bar{\mathcal V}(z)$ and $\bar{\mathcal W}$ are closures of geometric representatives dual to $\mu_p(z)$ and $\mu_c$ (Memoir §2.4, from FL2b §3.2). $\mathbb A(X)=\mathrm{Sym}(H_{\rm even}(X;\mathbb R))\otimes\Lambda^\bullet(H_{\rm odd}(X;\mathbb R))$ with $\deg\beta=4-i$ for $\beta\in H_i$; so $\deg(h^{\delta-2m}x^m)=2\delta$.

**Donaldson invariants.** For $b_1=0$, odd $b^+>1$: $D^w_X(z)=0$ unless $\deg(z)\equiv-2w^2-\frac32(\chi+\sigma)\pmod 8$ (eq. `mod8` (2.5.1)); otherwise, with $\deg(z)=8\kappa-\frac32(\chi+\sigma)$,
$$D^w_X(z)=\#\big(\bar{\mathcal V}(ze)\cap\bar M^{w+\mathrm{PD}[e]}_{\kappa+1/4}(\tilde X)\big)$$
(eq. `eq:DefineDonaldson` (2.5.2)), with $D^{w'}_X=(-1)^{\frac14(w'-w)^2}D^w_X$ for $w'\equiv w$ (eq. `eq:DonaldsonsSignChange` (2.5.3)). The Donaldson series is $\mathbf D^w_X(h)=D^w_X((1+\frac12x)e^h)$ (eq. `eq:DefineDonaldsonSeries` (2.5.4)). FL6 states the parity condition in the form $\delta\equiv-w^2-3\chi_h\pmod 4$ for $D^w_X(h^{\delta-2m}x^m)$ (eq. `eq:DegreeParity` (2.5)).

**KM simple type.** $D^w_X(x^2z)=4D^w_X(z)$ for all $z$: "for some $w$" in the Memoir (§2.5) and FL2b (§1.1); "for all $w$" in FL6 (eq. `eq:KMSimpleType` (2.6)). FL6 Theorem 2.4 (`thm:KMSimpleTypeIndepOfw`, citing Kronheimer–Mrowka and Muñoz, *Basic classes for four-manifolds not of simple type*, Theorem 2): for standard $X$, if it holds for one $w$ it holds for all $w$.

**Abundant.** FL2a Definition 1.2 (no `\label`; citing FKLM p. 169) and FLLevelOne Definition 1.2 (`defn:Abundant`): "the restriction of the intersection form to $B^\perp$ contains a hyperbolic sublattice". FL6 §1.1: "$B(X)^\perp\subset H^2(X;\mathbb Z)$ contains a hyperbolic summand".

**Effective.** FL2a Definition 1.3 (`defn:Effective`) and FLLevelOne Definition 1.3 (`defn:Effective`): $X$ satisfies Conjecture 3.1 of FKLM (the "multiplicity conjecture"), i.e. for a SW stratum $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in any level, the link pairing $\#(\bar{\mathcal V}(z)\cap\bar{\mathcal W}^\eta\cap\bar{\mathbf L}_{\mathfrak t,\mathfrak s})$ is a multiple of $SW_X(\mathfrak s)$. FL2b restates this as Conjecture 3.34 (`conj:Multiplicity`). In the Memoir this becomes Theorem 10.1.2 (Section 6 below), conditional on the gluing hypothesis.

---

## 2. Memoir, Theorem 1 (`thm:MainThm`): the SO(3)-monopole cobordism formula

**Source.** math/0203047, Chapter 1, §1.1 ("Summary of main results"), `\begin{mainthm}[$\SO(3)$-monopole cobordism formula]`. The displayed formula is eq. `eq:MainEquation` (1.1.1).

**Statement.**

> **Theorem 1** (SO(3)-monopole cobordism formula). Assume Hypothesis 7.8.1 holds. Let $X$ be a closed, connected, oriented smooth four-manifold with $b_1(X)=0$, odd $b^+(X)>1$, Euler characteristic $\chi$, and signature $\sigma$. Let $\Lambda,w\in H^2(X;\mathbb Z)$ obey $w-\Lambda\equiv w_2(X)\pmod 2$. Let $\delta,m$ be non-negative integers for which $m\le[\delta/2]$, where $[\,\cdot\,]$ denotes the greatest integer function, and $\delta\equiv-w^2-\frac34(\chi+\sigma)\pmod 4$, with $\Lambda$ and $\delta$ obeying $\delta<i(\Lambda)$, where $i(\Lambda)=\Lambda^2-\frac14(3\chi+7\sigma)$. Then, for any $h\in H_2(X;\mathbb R)$ and generator $x\in H_0(X;\mathbb Z)$, one has the following expression for the Donaldson invariant,
> $$
> D^w_X(h^{\delta-2m}x^m)=\sum_{\mathfrak s\in\mathrm{Spin}^c(X)}(-1)^{\frac14(w-\Lambda+c_1(\mathfrak s))^2}SW_X(\mathfrak s)\times\sum_{i=0}^{\min(\ell,[\delta/2]-m)}\Big(p_{\delta,\ell,m,i}(c_1(\mathfrak s),\Lambda)\,Q_X^i\Big)(h),\tag{1.1.1}
> $$
> where $Q_X$ is the intersection form on $H_2(X;\mathbb R)$, and $\ell=\frac14\big(\delta+(c_1(\mathfrak s)-\Lambda)^2+\frac34(\chi+\sigma)\big)$, and $p_{\delta,\ell,m,i}(\cdot,\cdot)$ is a homogeneous polynomial of degree $\delta-2m-2i$ with coefficients which are universal functions of $\chi$, $\sigma$, $c_1(\mathfrak s)^2$, $\Lambda^2$, $c_1(\mathfrak s)\cdot\Lambda$, $\delta$, $m$, and $\ell$.

**Hypotheses, as listed.**
1. Hypothesis 7.8.1 (the local gluing hypothesis; Section 3 below). This is an explicit assumption of the theorem.
2. $X$ closed, connected, oriented, smooth; $b_1(X)=0$; $b^+(X)$ odd and $>1$ (so $\ge3$).
3. $\Lambda,w\in H^2(X;\mathbb Z)$ with $w-\Lambda\equiv w_2(X)\pmod2$.
4. $\delta,m\in\mathbb Z_{\ge0}$, $m\le[\delta/2]$.
5. $\delta\equiv-w^2-\frac34(\chi+\sigma)\pmod 4$.
6. $\delta<i(\Lambda)=\Lambda^2-\frac14(3\chi+7\sigma)$.

No simple-type hypothesis of either kind is made. No hypothesis on $\Lambda$ relative to the basic classes (such as $\Lambda\in B^\perp$) is made.

**Notation specific to the formula.**
* $\ell$ is the level (Section 1) at which the reducible stratum $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ lies in the compactified moduli space of the spin$^u$ structure $\mathfrak t$ on $X$ with $c_1(\mathfrak t)=\Lambda$ and $\dim M^w_\kappa=2\delta$. Indeed, with $p_1(\mathfrak t)=-\delta-\frac34(\chi+\sigma)$, $\ell(\mathfrak t,\mathfrak s)=\frac14((\Lambda-c_1(\mathfrak s))^2-p_1(\mathfrak t))$ equals the $\ell$ in the theorem. When $\ell<0$ the inner sum is empty, and those $\mathfrak s$ contribute nothing. For $c_1(\mathfrak s)$ characteristic and $w-\Lambda$ characteristic, $(c_1(\mathfrak s)-\Lambda)^2\equiv w^2\pmod 4$, and the parity hypothesis on $\delta$ makes $\ell$ an integer (my check, not stated in the source).
* $\big(p(c_1(\mathfrak s),\Lambda)Q_X^i\big)(h)$ means a homogeneous polynomial in $\langle c_1(\mathfrak s),h\rangle$ and $\langle\Lambda,h\rangle$ multiplied by $Q_X(h)^i$. The overlap paper (Theorem 2.1, Section 7 below) writes the variables as $A=\langle c_1(\mathfrak s)-c_1(\mathfrak t),h\rangle$, $B=\langle c_1(\mathfrak t),h\rangle$.
* The sign $(-1)^{\frac14(w-\Lambda+c_1(\mathfrak s))^2}$ is $(-1)^{o_{\mathfrak t}(w,\mathfrak s)}$ with $o_{\mathfrak t}(w,\mathfrak s)=\frac14(w-c_1(L))^2$, $c_1(L)=\Lambda-c_1(\mathfrak s)$ (Memoir Lemma 8.1.7, `lem:OrientationFactor`, eq. `eq:OrientChangeFactor` (8.1.18), quoting FLLevelOne Lemmas 3.13 and 3.14). Memoir Lemma 8.1.8 (`eq:SWSeriesOrientationFactor`, the `\label` is attached to the lemma), citing FL2b eq. (4.62):
$$o_{\mathfrak t}(w,\mathfrak s)\equiv\tfrac12\big(w^2+c_1(\mathfrak s)\cdot(w-c_1(\mathfrak t))\big)+\tfrac12(\sigma-w^2)\pmod2,$$
and, if $w$ is characteristic and $c_1(\mathfrak t)\cdot c_1(\mathfrak s)=0$, $o_{\mathfrak t}(w,\mathfrak s)\equiv\frac12(w^2+c_1(\mathfrak s)\cdot w)\pmod 2$, which is the sign in Witten's formula.

**A footnote in the source.** Kronheimer–Mrowka (*Witten's conjecture and Property P*, Theorem 6) used a version with $i(\Lambda)=-\frac14(\chi+\sigma)$; the Memoir says this is a typographical error in an earlier draft, that the value $\Lambda^2-\frac14(3\chi+7\sigma)$ above is correct, and that the error does not affect the results of that paper. (As printed, the footnote says $i(\Lambda)=-\frac14(\chi+\sigma)$ and $-\frac14(3\chi+7\sigma)$, i.e. without the $\Lambda^2$ term.)

**How the proof assembles the formula** (Memoir §10.6, "Proofs of the main theorems").
1. Pass to $\tilde X=X\#\overline{\mathbb{CP}}^2$ and choose $\tilde{\mathfrak t}$ with $c_1(\tilde{\mathfrak t})=\Lambda$ and $\delta+1=-p_1(\tilde{\mathfrak t})-\frac34(\chi(X)+\sigma(X))$. Then $4n_a(\tilde{\mathfrak t})=i(\Lambda)-\delta$, so $\delta<i(\Lambda)$ gives $n_a(\tilde{\mathfrak t})>0$.
2. With $\tilde w=w+e^*$, eq. `eq:ASDPairing` (2.6.2) (quoted from FL2b; see Section 4) and the definition of $D^w_X$ give
$D^w_X(z)=\#(\bar{\mathcal V}(ze)\cap\bar M^{\tilde w}_{\tilde\kappa})=2^{1-n_a}\#(\bar{\mathcal V}(ze)\cap\bar{\mathcal W}^{n_a-1}\cap\bar{\mathbf L}^{\tilde w}_{\tilde{\mathfrak t},\tilde\kappa})$ (eq. `eq:MTProof1` (10.6.9)).
3. The cobordism identity, Theorem 8.1.9 (Section 4), converts this into minus the signed sum over $\tilde{\mathfrak s}\in\mathrm{Spin}^c(\tilde X)$ of the link pairings $\#(\bar{\mathcal V}(ze)\cap\bar{\mathcal W}^{n_a-1}\cap\bar{\mathbf L}_{\tilde{\mathfrak t},\tilde{\mathfrak s}})$ (eq. `eq:MTProof2` (10.6.10)).
4. Theorem 10.1.2 (multiplicity) discards all $\tilde{\mathfrak s}$ that are not SW basic. The SW blow-up formula (cited as Nicolaescu, *Notes on Seiberg–Witten theory*, Theorem 4.6.8) identifies the basic classes of $\tilde X$ with $c_1(\tilde{\mathfrak s}_k)=c_1(\mathfrak s)+(2k-1)e^*$, $c_1(\mathfrak s)\in B(X)$, $d_s(\mathfrak s)-k(k-1)\ge0$, with $SW_{\tilde X}(\tilde{\mathfrak s}_k)=\pm SW_X(\mathfrak s)$.
5. The sign changes as $o_{\tilde{\mathfrak t}}(\tilde w,\tilde{\mathfrak s}_k)=o_{\mathfrak t}(w,\mathfrak s)-k$ [corrected by checker: the source writes "$=$". Since $e^*$ is orthogonal to $H^2(X)$ and $(e^*)^2=-1$, the exact value is $\frac14(w-\Lambda+c_1(\mathfrak s)+2ke^*)^2=o_{\mathfrak t}(w,\mathfrak s)-k^2$. Only the congruence $\equiv o_{\mathfrak t}(w,\mathfrak s)-k\pmod 2$ holds, and that is all the proof uses], the level changes as $\ell(\tilde{\mathfrak t},\tilde{\mathfrak s}_k)=\ell(\mathfrak t,\mathfrak s)-k(k-1)$, and Lemma 10.6.2 (Section 6) evaluates each pairing as $SW_X(\mathfrak s)$ times a universal polynomial. Summing over $k$ gives (1.1.1).

**Role.** This is the formula. The cobordism $\bar{\mathcal M}_{\mathfrak t}/S^1$ relates the Donaldson invariant (through the link of the instanton stratum) to the sum over Seiberg–Witten strata in all levels. The content of the theorem is that each Seiberg–Witten term factors as $SW_X(\mathfrak s)$ times a polynomial that is universal, i.e. depends on $X$ only through $\chi$, $\sigma$ and the listed intersection numbers, even though the coefficients are not computed.

---

## 3. Memoir, Hypothesis 7.8.1 (`hyp:Gluing`): the local gluing hypothesis

**Source.** Chapter 7 ("Obstruction bundle"), §7.8 (`sec:GluingThm`, "Local gluing hypothesis for SO(3) monopoles"). The gluing map is eq. `eq:GluingMap` (7.8.1).

**Statement.**

> **Hypothesis 7.8.1** (Local gluing hypothesis). There is a continuous, $S^1$-equivariant embedding,
> $$\boldsymbol\gamma_{\mathcal M}:\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}\to\bar{\mathcal C}_{\mathfrak t},$$
> which is homotopic through $S^1$-equivariant, continuous embeddings to the global splicing map $\boldsymbol\gamma'_{\mathcal M}$, smooth on each stratum of $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}$, and equal to the identity on $N_{\mathfrak t(\ell),\mathfrak s}(\delta)\times\mathrm{Sym}^\ell(X)$. In addition, there are $S^1$-equivariant sections $\boldsymbol\chi_s$ and $\boldsymbol\chi_i$ of the pseudo-bundles $\bar\Upsilon^s_{\mathfrak t,\mathfrak s}$ and $\bar\Upsilon^i_{\mathfrak t,\mathfrak s}$ with the following properties:
> 1. The restriction of the section $\bar{\boldsymbol\chi}=\boldsymbol\chi_s\oplus\boldsymbol\chi_i$ of $\bar\Upsilon^s_{\mathfrak t,\mathfrak s}\oplus\bar\Upsilon^i_{\mathfrak t,\mathfrak s}$ to each stratum is smooth.
> 2. The restriction of the section $\bar{\boldsymbol\chi}$ to each stratum of $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}$ vanishes transversely.
> 3. If we pull back the fiber metric (`eq:L2FiberNorm`) to $\bar\Upsilon^s_{\mathfrak t,\mathfrak s}\oplus\bar\Upsilon^i_{\mathfrak t,\mathfrak s}$ by the splicing embeddings $\varphi'_s\oplus\varphi'_i$, then the $L^2$ norm of $\bar{\boldsymbol\chi}$ is lower semi-continuous.
> 4. The restriction of $\boldsymbol\gamma_{\mathcal M}$ to the zero-locus $\bar{\boldsymbol\chi}^{-1}(0)$ is a homeomorphism between $\bar{\boldsymbol\chi}^{-1}(0)$ and an open neighborhood of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in $\bar{\mathcal M}_{\mathfrak t}$.

**Notation.**
* $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}$ is the *space of global splicing data* (Memoir Chapter 6; Theorem 6.6.1, `thm:GlobalSplicingDataOverlaps`). It is the pushout of the local gluing-data bundles $\mathrm{Gl}(\Sigma)=\mathrm{Fr}(\Sigma)\times_{G(\Sigma)}M(\Sigma)\to M_{\mathfrak s}\times\Sigma$, over the strata $\Sigma\subset\mathrm{Sym}^\ell(X)$, along overlap maps $\rho^u_{\Sigma,\Sigma'},\rho^d_{\Sigma,\Sigma'}$. The fibers $M(\Sigma)$ are products of the *instanton moduli spaces with spliced ends* over $S^4$ (Chapter 5, Theorem 5.1.1, `thm:ExistenceOfSplicedEndsModuli`), not of the usual Uhlenbeck-compactified spaces $\bar M^s_\kappa(S^4)$.
* $\boldsymbol\gamma'_{\mathcal M}$ is the *global splicing map* built from the crude splicing maps, i.e. splicing done with respect to a metric and a background connection deformed to be flat near the splicing points (Chapter 6).
* $\bar\Upsilon^s_{\mathfrak t,\mathfrak s}$ and $\bar\Upsilon^i_{\mathfrak t,\mathfrak s}$ are the background and instanton obstruction pseudo-bundles (Chapter 7). "Pseudo-bundle" means that the rank may jump between strata.
* $N_{\mathfrak t(\ell),\mathfrak s}(\delta)\to M_{\mathfrak s}$ is the $\delta$-disc bundle of the virtual normal bundle of $M_{\mathfrak s}$ in the level-$\ell$ moduli space (Memoir §2.3.5, from FL2a §3.5, Theorem 3.21).

**Status, as described by the authors.**
* Memoir §7.8, after the statement: the gluing map and obstruction section are "similar to those constructed in" FL3. FL3 proves existence of the solution map, i.e. the existence half (FL3 Theorem 1.1, below). The proof of FL3 "should extend to yield the desired gluing map". Property 2 "follows from a formal argument" and the generic transversality of Feehan. Property 3 (Uhlenbeck continuity) is "expected" to follow as for the ASD gluing map in FL's *Donaldson invariants and wall-crossing formulas I* (math/9812060). Injectivity and surjectivity (property 4) "must also" be shown.
* Memoir §7.9 (`sec:Notes_on_justification_gluing_hypothesis`): the proof is "provided by the authors in" *Gluing maps for SO(3) monopoles and invariants of smooth four-manifolds*. The bibliography lists this as "in preparation, based in part on arXiv:math/9812060 and arXiv:math/9907107". The section points out a specific gap in FL3: FL3 assumed small spectral flow for $d^1_{A,\Phi}d^{1,*}_{A,\Phi}$, which is valid near zero-dimensional $M_{\mathfrak s}$ but not near positive-dimensional ones. It outlines replacing Taubes' small-eigenvalue splitting by a Donaldson–Kronheimer type extrinsic stabilizing bundle $\Xi=\Xi_1\oplus\operatorname{Coker}\mathbf D$.
* Only Theorem 1 says explicitly "Assume Hypothesis 7.8.1 holds". For $\ell\ge1$, however, the link $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$ is *defined* using the obstruction section of the hypothesis (Definition 8.1.3, `defn:DefineLink`: $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}=\bar{\boldsymbol\chi}^{-1}(0)\cap\bar{\mathbf L}^{\rm vir}_{\mathfrak t,\mathfrak s}$). So Theorems 8.1.9, 10.1.1, 10.1.2 and Proposition 10.6.1 also depend on it.

**What FL3 actually proves (for comparison).** FL3 Theorem 1.1 (`thm:GluingTheorem1`). Hypotheses: $E$ rank two with $c_1(E)=w$, $c_2(E)-\frac14c_1(E)^2=\kappa\ge1$; an integer $0<\ell<\lfloor\kappa\rfloor$; a smooth stratum $\Sigma\subset\mathrm{Sym}^\ell(X)$; a finite-dimensional, precompact, open, $S^1$-invariant $\mathcal U_{\ell,\mu}\Subset M(\mathfrak t_\ell,\mu)$ in a *thickened* moduli space, defined with a small-eigenvalue bound $\mu$. Conclusion: for small $\varepsilon_\ell$ and $\lambda_0$ there exist a bundle of local gluing data $\mathbf{Gl}(\mathcal U_{\ell,\mu},\Sigma,\lambda_0)=\mathbf{Fr}\times_{\mathbf G(\Sigma)}\mathbf Z(\Sigma)\to\mathcal U_{\ell,\mu}\times\Sigma$, an $S^1$-equivariant smooth map $\boldsymbol\gamma_{\mu,\Sigma}$ into $M^{*,0}(\mathfrak t,\mu)$, and an $S^1$-equivariant section $\boldsymbol\chi_{\mu,\Sigma}$ of a bundle $\Xi_\mu$ of real rank $2\ell$ plus the codimension of $M^{*,0}(\mathfrak t)$ in $M^{*,0}(\mathfrak t,\mu)$, such that $\boldsymbol\gamma_{\mu,\Sigma}(\boldsymbol\chi^{-1}_{\mu,\Sigma}(0))\subset M^{*,0}(\mathfrak t)$. [corrected by checker: the theorem also carries the standing hypotheses of FL3 §1.1, which are $(X,g)$ closed, connected, oriented with $b^+(X)>0$, generic perturbation parameters, and $w$ chosen so that no SO(3) bundle with $w_2\equiv w\pmod 2$ carries a flat connection. The section $\boldsymbol\chi_{\mu,\Sigma}$ is defined only over an open subset $\mathbf{Gl}^+(\mathcal U_{\ell,\mu},\Sigma,\lambda_0)\subset\mathbf{Gl}(\mathcal U_{\ell,\mu},\Sigma,\lambda_0)$.] FL3 §1.5.1 ("Properties of gluing maps") states explicitly that this is "at most the first half" of a gluing theorem. The missing properties are (1) continuity on the Uhlenbeck closure of the gluing data, (2) the embedding property, and (3) surjectivity onto an open subset of $\bar M(\mathfrak t)$ together with a finite covering by such sets; these are deferred to the sequel.

[added by checker] **Other sources on the gluing step.**
* FLLevelOne (math/0106238), Theorem 3.8 (unlabelled; §3.7 "Construction of the gluing map"). This is the one-bubble ($\ell=1$) gluing theorem: a topological embedding of the compactified level-one splicing domain $\bar{\mathcal M}^{\rm stab}_{\mathfrak t',\mathfrak s}$ into $\bar{\mathcal C}_{\mathfrak t'}$, with obstruction sections whose zero locus maps onto a neighbourhood. It is cited to "[FL3, FL4]" and is not proved in FLLevelOne. FL4, the sequel announced in FL3 §1.5.1, is not among the sources, and the Memoir's bibliography lists no such paper. Its replacement is the book "in preparation". Memoir §7.9 adds that FL3's small-eigenvalue method "does not apply without significant modification" near the positive-dimensional $M_{\mathfrak s}$ that FLLevelOne allows.
* Feehan–Leness, arXiv 1910.14580 (the author list in the source is Feehan *and* Leness), Theorem 3 (`mainthm:Gluing`, on the global `mainthm` counter) and Corollaries 4–7. This gives a $C^1$ gluing chart near a boundary point of the moduli space of **anti-self-dual** connections, for **one** bubble ($X_1=S^4$ with the round metric), near fixed $A_{0\flat}$ and centred $A_{1\flat}$. The chart is an open neighbourhood in the bubble-tree compactification. For SO(3) monopoles the paper says only that the framework "should apply" (§1.2, "Application to other gluing problems"), and it says that more than one bubble would require Banach manifolds with corners. It therefore proves no part of Hypothesis 7.8.1.

**Version in FL6.** FL6 Hypothesis 3.1 (`hyp:Local_gluing_map_properties`, "Properties of local SO(3)-monopole gluing maps"): "The local gluing map, constructed in [FL3], gives a continuous parametrization of a neighborhood of $M_{\mathfrak s}\times\Sigma$ in $\bar{\mathcal M}_{\mathfrak t}$ for each smooth stratum $\Sigma\subset\mathrm{Sym}^\ell(X)$." FL6 says it is "recorded, in greater detail, as Conjecture 6.7.1 in [FL5]" (an earlier version of math/0203047). [unconfirmed: FL6's bibliography gives FL5 only as "Memoirs AMS, in press, arXiv:math/0203047". Earlier arXiv versions are not among the sources, so it cannot be checked that their "Conjecture 6.7.1" has the same content as Hypothesis 7.8.1 of v4.] FL6 also says that assembling the local maps into a global one (the overlap problem) is "difficult … but one which we do solve in [FL5]". FL6 Remark 3.3 (`rmk:GluingThmProperties`) lists the assumed properties: continuity with respect to Uhlenbeck limits, injectivity, and surjectivity in the sense that points of $\bar{\mathcal M}_{\mathfrak t}$ sufficiently close to $M_{\mathfrak s}\times\Sigma$ lie in the image of at least one local gluing map. It adds that "the authors are currently developing a proof".

**Version in the overlap paper.** Overlap paper, Theorem 4.2 (`thm:ExtendedGluingThm`): "There is a section $\mathfrak o$ of a pseudo-vector bundle $\Upsilon\to\mathrm{Gl}(\mathfrak t,\mathfrak s,X)$ and a stratum-preserving deformation of the inclusion $\mathrm{Gl}(\mathfrak t,\mathfrak s,X)\to\bar{\mathcal C}_{\mathfrak t}/S^1$ such that the restriction of this deformation to $\mathfrak o^{-1}(0)$ parameterizes a neighborhood of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in $\bar{\mathcal M}_{\mathfrak t}/S^1$. In addition, the restriction of the obstruction section $\mathfrak o$ to any stratum vanishes transversely." The text before it says it will be proved in FL4 by extending FL3, and that the proofs of the overlap paper's Theorems 1.1 and 2.1 "rely" on it. Its Theorem 3.1 (`thm:GluingThm`) asserts that, for each single stratum, the gluing map restricted to the zero locus of the obstruction map parameterizes a neighborhood of $M_{\mathfrak s}\times\Sigma$ in $\bar{\mathcal M}_{\mathfrak t}$. That paper attributes this to FL3, although FL3 itself says surjectivity is not proved there.

**Role.** This is the analytic input that is assumed rather than proved. It is what turns the purely topological space of global splicing data (whose overlap structure the Memoir *does* construct) into a model for a neighborhood of the whole ideal stratum $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$, with an obstruction section whose zero set is the actual moduli space. Every statement about links of SW strata in levels $\ell\ge1$ passes through it.

---

## 4. The cobordism identity and the instanton link

### 4.1 Memoir, Theorem 8.1.9 (`thm:CobordismThm`)

**Source.** Chapter 8, §8.1, subsection "An equality of intersection numbers provided by the SO(3)-monopole cobordism". The displayed equations are `eq:DimensionCondition` (8.1.20) and `eq:RawCobordismSum1` (8.1.21).

> **Theorem 8.1.9.** Let $\mathfrak t$ be a spin$^u$ structure on a closed, oriented, smooth four-manifold $X$. Let $z\in\mathbb A(X)$ and $\eta$ be a non-negative integer satisfying
> $$\deg(z)+2\eta=\dim\mathcal M^{*,0}_{\mathfrak t}-2.\tag{8.1.20}$$
> Assume that there is a class $w\in H^2(X;\mathbb Z)$ satisfying $w_2(\mathfrak t)\equiv w\pmod 2$ and which is good in the sense of Definition 2.2.1. Then the intersection numbers (`eq:IntNumber`) obey
> $$\#\big(\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{\eta-1}\cap\bar{\mathbf L}^w_{\mathfrak t,\kappa}\big)=-\sum_{\mathfrak s\in\mathrm{Spin}^c(X)}(-1)^{o_{\mathfrak t}(w,\mathfrak s)}\,\#\big(\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{\eta-1}\cap\bar{\mathbf L}_{\mathfrak t,\mathfrak s}\big),\tag{8.1.21}$$
> where $\bar{\mathbf L}^w_{\mathfrak t,\kappa}$ is the link of the moduli space of anti-self-dual connections in $\bar{\mathcal M}_{\mathfrak t}/S^1$ specified in [FL2a, Definition 3.7].

**Hypotheses.** $\mathfrak t$ a spin$^u$ structure; $X$ closed, oriented, smooth (no hypothesis on $b_1$, $b^+$); the dimension condition (8.1.20); $w\equiv w_2(\mathfrak t)$ good. For $\ell\ge1$, implicitly, Hypothesis 7.8.1, through Definition 8.1.3. [corrected by checker: "no hypothesis on $b^+$" holds only for the statement as printed. The $\ell=0$ links are those of FL2a Definition 3.22, and FL2a and FL2b assume throughout that $b_2^+(X)>0$ (FL2a §1.1; FL2b §1.1 and Theorem 3.33). The Memoir itself uses $b^+(X)>0$ and a generic metric to exclude zero-section pairs from $M_{\mathfrak s}$ (§2.3.2). So $b^+(X)>0$ is an implicit hypothesis of Theorem 8.1.9.]

**Notation.** $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$ is empty if $\ell(\mathfrak t,\mathfrak s)<0$. For $\ell=0$ it is the link of FL2a, Definition 3.22. For $\ell\ge1$ it is Definition 8.1.3: the intersection of the *virtual link* $\bar{\mathbf L}^{\rm vir}_{\mathfrak t,\mathfrak s}$ (the boundary of a neighborhood of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}/S^1$, cut out by a fiber norm $t_N$ on $N_{\mathfrak t(\ell),\mathfrak s}(\delta)$ and the tubular distance functions $\vec t(\mathfrak t,\mathfrak s,\mathcal P_j)$ attached to the strata) with $\bar{\boldsymbol\chi}^{-1}(0)$. Lemma 8.1.4 (`lem:DefiningLink`): for generic constants, $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$ is the boundary of a closed neighborhood of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in $\bar{\mathcal M}_{\mathfrak t}/S^1$, and its intersection with each stratum is Whitney stratified with a collared codimension-one top stratum. Lemma 8.1.5 (`lem:GRIntersect0`): for good $w$, $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$ misses $\bar M^w_\kappa$ and $\bar{\mathcal M}^{\rm red}_{\mathfrak t}$, and $\bar{\mathcal V}(z)\cap\bar{\mathcal W}^\eta\cap\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$ is a finite set in the top stratum. Intersection numbers are counted with the *standard* orientation of $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$ (FLLevelOne, Definition 3.12). It differs from the boundary orientation induced by $O^{\rm asd}(\Omega,w)$ by $(-1)^{o_{\mathfrak t}(w,\mathfrak s)}$ (Lemma 8.1.7).

**Internal inconsistency in the source.** Under (8.1.20) the natural exponent of $\bar{\mathcal W}$ is $\eta$, not $\eta-1$. The proof of Theorem 1 applies (8.1.21) with exponent $n_a-1$ and $\dim\mathcal M_{\mathfrak t}=\deg(z)+2n_a$, i.e. with the exponent $e$ satisfying $\deg(z)+2e=\dim\mathcal M_{\mathfrak t}-2$. The unsigned version, eq. `eq:RawCobordismSum` (2.6.1) in §2.6, uses exponent $n_a-1$.

**Role.** This is the cobordism itself. The one-manifold $\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{e}\cap\bar{\mathcal M}^{*,0}_{\mathfrak t}/S^1$ has ends only near $M^w_\kappa$ and near the reducible strata $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in every level (Memoir §2.4, quoting FL2b, Corollary 3.18). The identity is the count of its boundary points.

### 4.2 The instanton link: Memoir eq. (2.6.2) / FL2b Proposition 3.29

The Memoir (§2.6, eq. `eq:ASDPairing` (2.6.2)) quotes "[FL2b, Lemma 3.30]": when $\deg(z)=\dim M^w_\kappa$ and $n_a(\mathfrak t)>0$,
$$2^{1-n_a}\#\big(\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{n_a-1}\cap\bar{\mathbf L}^w_{\mathfrak t,\kappa}\big)=\#\big(\bar{\mathcal V}(z)\cap\bar M^w_\kappa\big).$$
In the arXiv source of FL2b this is **Proposition 3.29** (`prop:LinkOfASD`, eq. `eq:LinkOfASD` (3.60)); FL6 also cites it as FL2b Proposition 3.29. Statement: let $w$ be an integral lift of $w_2(\mathfrak t)$ with $w\pmod2$ good, $d_a(\mathfrak t)\ge0$, $n_a(\mathfrak t)>0$, and $\deg(z)+2\delta_c=d_a+2n_a-2$ with $\deg(z)\ge d_a$ and $z$ intersection-suitable. If the link is oriented as the boundary of $\mathcal M^{*,\ge\varepsilon}_{\mathfrak t}/S^1$ (orientation $O^{\rm asd}(\Omega,w)$), then for generic small $\varepsilon$,
$$\#\big(\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{\delta_c}\cap\mathbf L^{w,\varepsilon}_{\mathfrak t,\kappa}\big)=\begin{cases}2^{n_a-1}\#(\bar{\mathcal V}(z)\cap\bar M^w_\kappa),&\deg(z)=d_a,\\0,&\deg(z)>d_a.\end{cases}$$
The Memoir's Remark 2.6.1 records the second case. It also notes that when $n_a\le0$ the pairing is a multiple of a spin polynomial invariant.

**Role.** This identifies the instanton end of the cobordism with $2^{n_a-1}$ times a Donaldson invariant. It is where the hypothesis $\delta<i(\Lambda)$ of Theorem 1 is used.

---

## 5. Theorem 1 in the simple-type form used to prove Witten's conjecture: FL6, Theorem 3.2 (`thm:Cobordism`)

**Source.** math/0609530, §3 ("The SO(3) monopole cobordism formula"), `\begin{thm}[$\SO(3)$-monopole cobordism formula]`, citing FL5 = math/0203047. Displayed equations: `eq:MainEquation` (3.4) and `eq:Coefficients` (3.5).

> **Theorem 3.2** (SO(3)-monopole cobordism formula). Let $X$ be a standard four-manifold of Seiberg–Witten simple type. Assume that Hypothesis 3.1 holds. Assume further that $w,\Lambda\in H^2(X;\mathbb Z)$ and $\delta,m\in\mathbb N$ satisfy
> 1. $w-\Lambda\equiv w_2(X)\pmod 2$,
> 2. $I(\Lambda)>\delta$, where $I(\Lambda)$ is defined in (3.2),
> 3. $\delta\equiv-w^2-3\chi_h\pmod 4$,
> 4. $\delta-2m\ge0$.
>
> Then, for any $h\in H_2(X;\mathbb R)$ and generator $x\in H_0(X;\mathbb Z)$, we have
> $$D^w_X(h^{\delta-2m}x^m)=\sum_{K\in B(X)}(-1)^{\frac12(w^2-\sigma)+\frac12(w^2+(w-\Lambda)\cdot K)}SW'_X(K)\,f_{\delta,m}(\chi_h,c_1^2,K,\Lambda)(h),\tag{3.4}$$
> where the map
> $$f_{\delta,m}(h):\mathbb Z\times\mathbb Z\times H^2(X;\mathbb Z)\times H^2(X;\mathbb Z)\to\mathbb Q[h],$$
> taking values in the ring of polynomials in the variable $h$ with rational coefficients, is universal (independent of $X$) and given by
> $$f_{\delta,m}(\chi_h,c_1^2,K,\Lambda)(h):=\sum_{i+j+2k=\delta-2m}a_{i,j,k}(\chi_h,c_1^2,K\cdot\Lambda,\Lambda^2,m)\,\langle K,h\rangle^i\langle\Lambda,h\rangle^jQ_X^k(h),\tag{3.5}$$
> and, for each triple of non-negative integers $i,j,k\in\mathbb N$, the coefficients
> $$a_{i,j,k}:\mathbb Z\times\mathbb Z\times\mathbb Z\times\mathbb Z\times\mathbb N\to\mathbb Q$$
> are real analytic (independent of $X$) in the variables $\chi_h$, $c_1^2$, $c_1(\mathfrak s)\cdot\Lambda$, $\Lambda^2$, and $m$ with rational coefficients.

**Hypotheses.** Standard ($b_1=0$, odd $b^+\ge3$); SW simple type; FL6 Hypothesis 3.1; conditions 1–4.

**Relation to Memoir Theorem 1.**
* Simple type is used to remove the level from the statement. On a basic class $K^2=c_1^2(X)$, so $\ell=\frac14(\delta+K^2-2K\cdot\Lambda+\Lambda^2+3\chi_h)$ is a function of $\delta$, $c_1^2$, $K\cdot\Lambda$, $\Lambda^2$, $\chi_h$. Likewise the bound $k\le\ell$ on the power of $Q_X$ disappears into the coefficients. $\delta$ does not appear among the arguments of $a_{i,j,k}$ because $\delta=i+j+2k+2m$.
* ~~The sign agrees with $(-1)^{o_{\mathfrak t}(w,\mathfrak s)}$ modulo 2, by Memoir Lemma 8.1.8 (Section 2), since $\frac12(\sigma-w^2)\equiv\frac12(w^2-\sigma)\pmod 2$.~~ [corrected by checker] The two exponents are $\frac12(w^2-\sigma)+\frac12(w^2+(w-\Lambda)\cdot K)$ in FL6 and $\frac12(\sigma-w^2)+\frac12(w^2+K\cdot(w-\Lambda))$ in Memoir Lemma 8.1.8, which is FL2b eq. (4.62). Their difference is $w^2-\sigma$. Because $w-\Lambda$ is characteristic, $w^2\equiv\Lambda^2+\sigma\pmod 2$, so the difference is $\equiv\Lambda^2\pmod 2$. Hence FL6's sign equals $(-1)^{o_{\mathfrak t}(w,\mathfrak s)}$ **if and only if $\Lambda^2$ is even**. When $\Lambda^2$ is odd, which conditions 1–4 of Theorem 3.2 allow, the two signs differ by $-1$. Example: $X=K3\#\overline{\mathbb{CP}}^2$, $\Lambda=e^*$, $w=0$, $K=\pm e^*$. When $\Lambda^2$ is odd, moreover, $\frac12(w^2-\sigma)$ is not an integer, so FL6's exponent has to be read as a single sum. The discrepancy $(-1)^{\Lambda^2}$ does not depend on $K$ and can be absorbed into the $a_{i,j,k}$, which depend on $\Lambda^2$. So the two theorems are equivalent up to renormalising the coefficients, but the signs are not literally the same. In every application in FL6, $\Lambda^2$ is even ($\Lambda^2=2y$ in Proposition 4.8, $8a$ in the proof of Main Theorem 1.2). FL6 itself derives $\frac12(\tilde w^2-\sigma)\equiv\frac12\Lambda^2\pmod 2$ under that assumption in the proof of Proposition 4.8.
* [added by checker] FL6's coefficients carry more structure than the Memoir's. The Memoir (Theorem 1, Theorem 10.1.1) asserts only that the coefficients are "universal functions" of the listed quantities. FL6 Theorem 3.2 asserts that the $a_{i,j,k}$ are rational-valued and "real analytic … with rational coefficients". Neither property is stated or proved in the Memoir, and FL6 cites no further source for them. FL6 is also not internally consistent on this point: just before eq. (4.4) it calls the combined coefficients $b_{i,j,k}$ "a universal polynomial map", while the comment at (3.5) says the dependence is "not necessarily polynomial". The proofs in FL6 §4 use the coefficients only at integer points, so analyticity does not seem to be used.
* The sum is over $K\in B(X)$ with $SW'_X(K)$, which handles 2-torsion. The Memoir sums over $\mathrm{Spin}^c(X)$.
* The source comment at "real analytic" reads (TL, 6.6.2013): "Not necessarily polynomial dependence (there may be exponentials, e.g.)". The meaning of "real analytic" on $\mathbb Z^4\times\mathbb N$ is not further specified.

**Role.** FL6 uses this form as a black box. It is the only input from the SO(3)-monopole cobordism in that paper, apart from FKLM Theorem 1.1 (itself derived from the same formula).

---

## 6. Memoir, Theorems 10.1.1 and 10.1.2, Proposition 10.6.1, Lemma 10.6.2: the link pairings

### 6.1 Theorem 10.1.1 (`thm:LinkPairing`)

**Source.** Chapter 10, §10.1. Displayed equation `eq:LinkIntersectionFormula` (10.1.1).

> **Theorem 10.1.1.** Let $X$ be a closed, connected, oriented, smooth, Riemannian four-manifold with $b_1(X)=0$ and $\mathfrak t$ be a spin$^u$ structure on $X$. Suppose that $\ell\ge0$ is an integer and $\mathfrak s$ is a spin$^c$ structure on $X$ such that $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ is a subset of the space of gauge-equivalence classes of ideal monopoles $I\mathcal M_{\mathfrak t}$. Let $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$ be the link of the stratum of gauge-equivalence classes of reducible SO(3) monopoles determined by $\mathfrak s\in\mathrm{Spin}^c(X)$ as in Definition 8.1.3. For non-negative integers $m,\delta,\eta$ satisfying
> $$\delta-2m+2\eta=\dim\mathcal M_{\mathfrak t}-2,$$
> a class $h\in H_2(X;\mathbb R)$, and a generator $x\in H_0(X;\mathbb Z)$, let $z=h^{\delta-2m}x^m\in\mathbb A(X)$ and $\bar{\mathcal V}(z)$ and $\bar{\mathcal W}^\eta$ be the geometric representatives defined in Section 2.4. Then
> $$\#\big(\bar{\mathcal V}(z)\cap\bar{\mathcal W}^\eta\cap\bar{\mathbf L}_{\mathfrak t,\mathfrak s}\big)=SW_X(\mathfrak s)\sum_{i=0}^{\min(\ell,[\frac{\delta-2m}2])}\Big(q_{\delta,\ell,m,i}\big(c_1(\mathfrak s)-c_1(\mathfrak t),c_1(\mathfrak t)\big)Q_X^i\Big)(h),\tag{10.1.1}$$
> where $q_{\delta,\ell,m,i}$ are degree $\delta-2m-2i$ homogeneous polynomials which are universal functions of the constants given in Theorem 1.

**Remarks.**
* The dimension condition as printed, $\delta-2m+2\eta=\dim\mathcal M_{\mathfrak t}-2$, does not match $\deg(z)=2\delta$. Proposition 10.6.1 uses $2(\delta+\eta)=\dim\mathcal M_{\mathfrak t}-2$, which is the consistent normalization. I read the printed condition as a misprint.
* Hypothesis 7.8.1 is not mentioned in the statement but enters through Definition 8.1.3 and Proposition 9.1.1 (`prop:Duality`). The latter rewrites the pairing as $\langle\bar\mu_p(z)\smile\bar\mu_c^\eta\smile\bar e_I\smile\bar e_s,[\bar{\mathbf L}^{\rm vir}_{\mathfrak t,\mathfrak s}]\rangle$, where $\bar e_s$ and $\bar e_I$ are the Euler classes of the background and the instanton obstruction pseudo-bundles.
* The source remarks that the analogue without $b_1(X)=0$, or for general $z$, holds but is more complicated. It also says that an explicit formula is unknown in general and has been computed in special cases (FL2b, FLLevelOne, FL6, FL7, FL8).
* Mechanism of proof (§10.6). After duality, the pairing reduces to pairings over the base subspaces $\bar{\mathbf{BL}}^{\rm vir}_{\mathfrak t,\mathfrak s}(\mathcal P_j)$, which fiber over $M_{\mathfrak s}\times K_j$ (Lemma 8.2.3, `lem:LocalBaseLinkFiberBundle`). A quotient $\mathbf{QL}^{\rm vir}_{\mathfrak t,\mathfrak s}$ collapses the mutual boundaries to codimension $\ge2$ (§10.2), and the computation finishes by pushforward and pullback along each fiber bundle. Because $b_1=0$, the pairing over $[M_{\mathfrak s}]\times[\Delta(X^\ell,\mathcal P_k)]$ vanishes unless it contains $\mu_{\mathfrak s}(x)^{d_s/2}$. This produces the factor $SW_X(\mathfrak s)$. Pairing the classes $S^\ell(h)$ on products of copies of $X$ produces $Q_X(h)^a$ with $a\le\ell$.

### 6.2 Theorem 10.1.2 (`thm:Multiplicity`): the multiplicity conjecture

> **Theorem 10.1.2.** Assume the hypotheses of Theorem 10.1.1, but allow $b_1(X)>0$. If $SW_{X,\mathfrak s}(\omega)$ vanishes for all $\omega\in\mathbb A_2(X)$, then
> $$\#\big(\bar{\mathcal V}(z)\cap\bar{\mathcal W}^\eta\cap\bar{\mathbf L}_{\mathfrak t,\mathfrak s}\big)=0.$$

Here $SW_{X,\mathfrak s}(\omega):=\langle\mu_{\mathfrak s}(\omega),[M_{\mathfrak s}]\rangle$ for $\omega\in\mathbb A_2(X)=\mathrm{Sym}(H_0)\otimes\Lambda^\bullet(H_1)$. The source states that this is the result "referred to as the Multiplicity Conjecture in FL2b, FKLM, FLLevelOne" and that it "holds without any additional hypotheses", meaning without hypotheses beyond those of Theorem 10.1.1, which include the implicit dependence on Hypothesis 7.8.1. In the older terminology it says that every $X$ is *effective* (FL2a Definition 1.3), conditionally on Hypothesis 7.8.1.

### 6.3 Proposition 10.6.1 (`prop:theorem_LinkPairing_dim_Ms_zero`)

Recorded "in a form which is used in the proof of Witten's Conjecture [FL7, FL8]". Assume the hypotheses of Theorem 10.1.1 and, in addition, $\dim M_{\mathfrak s}=0$ and $2(\delta+\eta)=\dim\mathcal M_{\mathfrak t}-2$. Write $\mathfrak s_h=\langle c_1(\mathfrak s),h\rangle$ and $\lambda_h=\langle c_1(\mathfrak t),h\rangle$. Then
$$\big\langle\nu^{\delta+\eta-2m-i}\smile\pi_X^*S^\ell(h)^i\smile\bar\mu_p(x)^m\smile\bar e_I\smile e_s,[\bar{\mathbf L}^{\rm vir}_{\mathfrak t,\mathfrak s}]\big\rangle=SW_X(\mathfrak s)\sum_{j=0}^{\min(\ell,[i/2])}f_{\delta,\ell,m,\eta,i,j}(\mathfrak s_h,\lambda_h)Q_X(h)^j$$
(eq. `eq:ReducedForm` (10.6.7)), with $f_{\delta,\ell,m,\eta,i,j}=\sum_{k=0}^{i-2j}a_{\delta,\ell,m,\eta,i,j,k}\,\mathfrak s_h^{i-2j-k}\lambda_h^k$. The coefficients depend on $\delta,\ell,m,\eta,i,j,k,\chi,\sigma,c_1(\mathfrak t)^2,c_1(\mathfrak s)\cdot c_1(\mathfrak t),c_1(\mathfrak s)^2$.

### 6.4 Lemma 10.6.2 (`lem:BlowUpLinkPairing`)

Assume the notation and hypotheses of Theorem 10.1.1. Let $\tilde{\mathfrak t}$ on $\tilde X$ satisfy $p_1(\tilde{\mathfrak t})=p_1(\mathfrak t)-1$, $c_1(\tilde{\mathfrak t})=c_1(\mathfrak t)$, $w_2(\tilde{\mathfrak t})\equiv w_2(\mathfrak t)+\mathrm{PD}[e]$, and let $\tilde{\mathfrak s}_k$ have $c_1(\tilde{\mathfrak s}_k)=c_1(\mathfrak s)+(2k-1)e^*$. Then
$$\#\big(\bar{\mathcal V}(ze)\cap\bar{\mathcal W}^\eta\cap\bar{\mathbf L}_{\tilde{\mathfrak t},\tilde{\mathfrak s}_k}\big)=SW_X(\mathfrak s)\sum_{i=0}^{\min(\ell,[\frac{\delta-2m}2])}\Big(\tilde q_{\delta,\ell,m,i,k}\big(c_1(\mathfrak s)-c_1(\mathfrak t),c_1(\mathfrak t)\big)Q_X^i\Big)(h)$$
(eq. `eq:BlownUpLinkIntersectionFormula` (10.6.8)), with universal $\tilde q$. The proof uses $\ell(\tilde{\mathfrak t},\tilde{\mathfrak s}_k)=\ell(\mathfrak t,\mathfrak s)-k(k-1)$ and $SW_{\tilde X}(\tilde{\mathfrak s}_k)=\pm SW_X(\mathfrak s)$ if $d(\mathfrak s)\ge k(k-1)$ and $0$ otherwise.

**Role of §6.** These are the "technical heart" (the source's phrase) of the Memoir. Each Seiberg–Witten end of the cobordism, at any level $\ell$, contributes $SW_X(\mathfrak s)$ times a universal polynomial in $\langle c_1(\mathfrak s)-c_1(\mathfrak t),h\rangle$, $\langle c_1(\mathfrak t),h\rangle$ and $Q_X(h)$, with $Q_X$ appearing to power at most $\ell$.

---

## 7. Earlier formulations of the same statement

* **Announcement** (dg-ga/9709022), Conjecture 4.1 (`conj:ReductionFormula`, attributed to Pidstrigach and Tyurin): $2^{n_a-1}D^{c_1(E)}_X(z)=\sum_{L_1}\bar V(z)\cap\bar W(x^{n_a-1})\cap\mathbf L_{W,E_{-\ell},L_1}$ if $\deg z=2d_a$, and $0=\sum(\dots)$ if $\deg z>2d_a$. Conjecture 4.2 (`conj:PTConjecture`, same attribution): the pairing on the right "is given by a universal formula depending only on $\ell$, $F$, $L_1$, $SW(\mathfrak s_0\otimes L_1)$, the intersection form $Q_X$, and invariants of the homotopy type of $X$." FL3 calls this the "homotopy version" of Witten's conjecture.
* **FL2b §1.3**, eqs. `eq:RawGeneralCobordismFormula` (1.20) and `eq:GeneralFormulaForPairing` (1.21). These are stated as expectations, not theorems: $D^w_X(z)=-2^{-\delta_c}\sum_{\mathfrak s}(-1)^{\frac14(w-\Lambda+c_1(\mathfrak s))^2}\langle\mu_p(z)\smile\mu_c^{\delta_c},[\mathbf L_{\mathfrak t,\mathfrak s}]\rangle$ with $\delta_c=\frac14(i(\Lambda)-\delta)-1$. For $b_1=0$, $z=x^mh^{\delta-2m}$ the pairing should equal $SW_X(\mathfrak s)\sum_{i=0}^r\boldsymbol\delta_{d,i}(\langle c_1(\mathfrak s),h\rangle,\langle\Lambda,h\rangle)Q_X^{\ell-i}(h,h)$, with $r=\min(\ell,[\delta/2]-m)$, $\ell=\frac14(\delta-r(\Lambda,c_1(\mathfrak s)))$, $d=\delta-2(m+\ell-i)$.
* [added by checker] **FLLevelOne, Conjecture 1.6** (`conj:PTConjecture`, eq. `eq:PTConjecture`). This is the closest precursor of Memoir Theorem 10.1.1. Hypotheses: $X$ closed, oriented, smooth with $b_1=0$ and odd $b_2^+>1$; $w-\Lambda\equiv w_2(X)$; $m\le[\delta/2]$; $\delta\equiv-w^2-\frac34(\chi+\sigma)\pmod4$; $c_1(\mathfrak t)=\Lambda$ and $\delta=-p_1(\mathfrak t)-\frac34(\chi+\sigma)$; $\dim M_{\mathfrak s}=0$; $\ell=\frac14(\delta-r(\Lambda,c_1(\mathfrak s)))\ge0$; $\eta=\frac14(p_1(\mathfrak t)+\Lambda^2-\sigma)-1$. The conjectured conclusion is $\#(\bar{\mathcal V}(z)\cap\bar{\mathcal W}^\eta\cap\bar{\mathbf L}_{\mathfrak t,\mathfrak s})=\pm2^{a(\chi,\sigma,\delta,m,\ell)}SW_X(\mathfrak s)\sum_{j=0}^{q}p_{\delta,m,\ell,j}(\langle c_1(\mathfrak s),h\rangle,\langle\Lambda,h\rangle)Q_X^j(h)$, with $q=\min(\ell,[\delta/2]-m)$, $a$ linear, and $p_{\delta,m,\ell,j}$ homogeneous of degree $\delta-2m-2j$ **whose coefficients are polynomials of degree $\ell-j$** in $2\chi\pm3\sigma$, $(c_1(\mathfrak s)-\Lambda)^2$, $\Lambda^2$ and $(c_1(\mathfrak s)-\Lambda)\cdot c_1(\mathfrak s)$. This is strictly stronger than what the Memoir proves (Theorem 10.1.1 gives only "universal functions"). The polynomiality and degree bound on the coefficients therefore remain conjectural in the sources. **FLLevelOne, Conjecture 1.7** (`conj:PUKotschickMorganImpliesWitten`): "Witten's formula is implied by Conjecture 1.6". Both are stated as conjectures.
* **Overlap paper**, Theorem 1.1 (`thm:CobordismResult`, eq. `eq:MainThm` (1.1)). As printed: "Let $X$ be a smooth, oriented manifold with $b^1(X)=0$. Let $\mathrm{Char}(X)\subset H^2(X;\mathbb Z)$ be the set of integral lifts of $w_2(X)$. Then, for $h\in H_2(X;\mathbb R)$, $w\in H^2(X;\mathbb Z)$, and generator $x\in H_0(X;\mathbb Z)$, $D^w_X(h^{\delta-2m}x^m)=-\sum_{c\in\mathrm{Char}(X)}SW_X(c)\,g^w_{X,\delta,m,c}(h^{\delta-2m}x^m)$, where … $g^w_{X,\delta,m,c}:\mathrm{Sym}(H_0(X;\mathbb Z)\oplus H_2(X;\mathbb Q))\to\mathbb Q$ is a universal function depending only on $\delta$, $m$, $w$, $c$ and the homotopy type of $X$." The statement as printed omits closedness, the condition on $b^+$, the condition on $\delta$ and $i(\Lambda)$, and the gluing assumption. The text says it "relies on" Theorem 4.2 (`thm:ExtendedGluingThm`), to be proved in FL4. Theorem 2.1 (`conj:PTConj`; the environment is `thm`) is the link-pairing formula, with the same content as Memoir Theorem 10.1.1. It begins "Assume the result of Theorem 4.2" and has the coefficient list $\chi,\sigma,c_1(\mathfrak s)^2,c_1(\mathfrak t)^2,c_1(\mathfrak t)\cdot c_1(\mathfrak s),p_1(\mathfrak t),m,\delta,\ell$ and upper limit $k=\min[\ell,(\delta-2m)/2]$.

---

## 8. Kronheimer–Mrowka structure theorem, as restated by FL

The original (Kronheimer–Mrowka, *Embedded surfaces and the structure of Donaldson's polynomial invariants*) is not on arXiv and was not consulted. Three FL restatements follow.

**FL6, Theorem 2.2** (`thm:KMStructure`, "Structure of Donaldson invariants", cited as KM Theorem 1.7(a); FL6 adds "see also [Fintushel–Stern, Donaldson invariants of 4-manifolds with simple type, Theorems 5.9 and 5.13] for a proof by a different method"):

> Let $X$ be a standard four-manifold with KM-simple type. Suppose that some Donaldson invariant of $X$ is non-zero. Then there is a function $\beta_X:H^2(X;\mathbb Z)\to\mathbb Q$ such that $\beta_X(K)\neq0$ for at least one and at most finitely many classes $K$, which are integral lifts of $w_2(X)\in H^2(X;\mathbb Z/2\mathbb Z)$ (the KM-basic classes), and for any $w\in H^2(X;\mathbb Z)$, one has the following equality of analytic functions of $h\in H_2(X;\mathbb R)$:
> $$\mathbf D^w_X(h)=e^{Q_X(h)/2}\sum_{K\in H^2(X;\mathbb Z)}(-1)^{(w^2+K\cdot w)/2}\beta_X(K)e^{\langle K,h\rangle}.\tag{2.9}$$

**Memoir, §2.5** (unnumbered; the `\label`s `Kronheimer-Mrowka_basic_classes` and `Kronheimer-Mrowka_structure_theorem` are index labels), citing KM Theorem 1.7: when $X$ (with $b_1=0$, odd $b^+>1$) has KM simple type, $\mathbf D^w_X(h)$ is an analytic function of $h$, and there are finitely many characteristic classes $K_1,\dots,K_m$ and non-zero rationals $a_1,\dots,a_m$ independent of $w$ with
$$\mathbf D^w_X(h)=e^{\frac12h\cdot h}\sum_{i=1}^r(-1)^{\frac12(w^2+K_i\cdot w)}a_ie^{\langle K_i,h\rangle}.$$
The source has the index mismatch $m$ versus $r$. It does not state the hypothesis that some Donaldson invariant is non-zero.

**FL2b, §1.1** (unnumbered), citing KM Theorem 1.7: the same statement, with constants $a_1,\dots,a_m$ independent of $w$ and sum $\sum_{r=1}^s$; again an index mismatch. **FL3 §1.2** gives the same formula with "$w\in H_2(X;\mathbb Z)$", a misprint for $H^2$.

**Supporting facts quoted by FL.** KM simple type is independent of $w$ (FL6 Theorem 2.4) and invariant under blow-up (FL6 Proposition 2.6, `prop:KMBlowUpInvariance`, using Friedman–Morgan Theorem III.8.4 and KM Proposition 1.9). KM Proposition 1.9, as quoted in FL2a §1: $\mathbf D^{w+\mathrm{PD}[e]}_{\tilde X}(h)=-\mathbf D^w_X(h)\exp(-\frac12e\cdot e)\sinh(e\cdot h)$.

**Role.** It reduces Witten's conjecture, for manifolds already known to have KM simple type, to an identity of the coefficients $\beta_X(K)$. In FL6 it enters through Lemma 2.3 (unlabelled: if (1.2) holds, KM and SW basic classes coincide) and Proposition 2.5 (unlabelled: Witten's conjecture for one $w$ implies it for all $w$).

---

## 9. Witten's conjecture, as stated by FL

**Memoir, Conjecture 2** (`conj:WC`, environment `mainconj`, which shares the counter with Theorem 1):

> Let $X$ be a closed, connected, oriented, smooth four-manifold with $b_1(X)=0$ and odd $b^+(X)>1$. Assume that $X$ has Seiberg–Witten simple type. Then $X$ has Kronheimer–Mrowka simple type, the Kronheimer–Mrowka basic classes coincide with the Seiberg–Witten basic classes, and the Donaldson series of $X$ is given by
> $$\mathbf D^w_X(h)=2^{2-c(X)}e^{Q_X(h)/2}\sum_{\mathfrak s}(-1)^{\frac12(w^2+w\cdot c_1(\mathfrak s))}SW_X(\mathfrak s)e^{\langle c_1(\mathfrak s),h\rangle},$$
> where $c(X)=-\frac14(7\chi+11\sigma)$.

**FL6, Conjecture 1.1** (`conj:WittenSimpleType`, eq. `eq:WConjecture` (1.2)):

> Let $X$ be a standard four-manifold with Seiberg–Witten simple type. The four-manifold $X$ then has Kronheimer–Mrowka simple type and the Kronheimer–Mrowka and Seiberg–Witten basic classes coincide. For any $w\in H^2(X;\mathbb Z)$ and $h\in H_2(X;\mathbb R)$, one has
> $$\mathbf D^w_X(h)=2^{2-(\chi_h-c_1^2)}e^{Q_X(h)/2}\sum_{\mathfrak s\in\mathrm{Spin}^c(X)}(-1)^{\frac12(w^2+c_1(\mathfrak s)\cdot w)}SW_X(\mathfrak s)e^{\langle c_1(\mathfrak s),h\rangle}.\tag{1.2}$$

The two are the same statement, since $\chi_h-c_1^2=c(X)$. FL2b (§1.1, eq. `eq:WittenConjSeries` (1.6)), FLLevelOne (§1) and FL3 (Conjecture 1.2, unlabelled) state the conjecture as "$X$ has KM simple type **if and only if** it has SW simple type; if $X$ has simple type then [the same formula]". The Memoir and FL6 state only the direction SW simple type $\Rightarrow$ KM simple type.

**Equivalent coefficientwise form.** FL6 Lemma 2.8 (`lem:DInvarForWSTManifolds`): for standard $X$, Witten's formula holds and $X$ has KM simple type if and only if $D^w_X(h^{\delta-2m}x^m)=0$ when $\delta\not\equiv-w^2-3\chi_h\pmod4$, and otherwise
$$D^w_X(h^{\delta-2m}x^m)=\sum_{i+2k=\delta-2m}\ \sum_{K\in B(X)}(-1)^{\varepsilon(w,K)}\frac{SW'_X(K)(\delta-2m)!}{2^{k+c(X)-2-m}k!\,i!}\langle K,h\rangle^iQ_X^k(h),\qquad\varepsilon(w,K)=\tfrac12(w^2+w\cdot K)$$
(eq. `eq:DInvarForWC` (2.13)). This is the form compared, coefficient by coefficient, with (3.4).

---

## 10. FL6, Main Theorem 1.2 (`thm:WittenSimpleType`): Witten's conjecture for many manifolds of simple type

**Statement.**

> **Main Theorem 1.2.** Let $X$ be a standard four-manifold with Seiberg–Witten simple type which is abundant or has $c_1^2(X)\ge\chi_h(X)-3$. Then the SO(3)-monopole cobordism formula (Theorem 3.2) implies that Conjecture 1.1 holds for $X$.

**Class of manifolds, precisely.** The theorem covers $X$ closed, connected, oriented, smooth, with $b_1(X)=0$ and odd $b^+(X)\ge3$, of SW simple type, and satisfying either
* (i) $X$ is abundant ($B(X)^\perp$ contains a hyperbolic summand), or
* (ii) $c_1^2(X)\ge\chi_h(X)-3$, i.e. $c(X)\le3$.

The conclusion is conditional on Theorem 3.2, hence on Hypothesis 3.1 (equivalently, in the Memoir, Hypothesis 7.8.1). [corrected by checker: "equivalently" is too strong. FL6 identifies Hypothesis 3.1 with "[FL5, Conjecture 6.7.1]", but Hypothesis 3.1 is phrased stratum by stratum and its literal content differs from Hypothesis 7.8.1; see Uncertainty 7. The accurate statement is that Main Theorem 1.2 is conditional on FL6 Theorem 3.2, which FL6 attributes to FL5 under its Hypothesis 3.1. The Memoir proves its version of the formula under Hypothesis 7.8.1.] "Effective" does **not** appear among the hypotheses of FL6. The effectiveness/multiplicity property is part of the conclusion of the cobordism formula: only basic classes appear in (3.4). The abstract says "$c_1^2\ge\chi_h-3$ or is abundant". FL6 §1.1 adds that the abundant case includes elliptic surfaces and surfaces of general type and, by FL2a §A.2, all simply connected closed complex surfaces with $b^+\ge3$. It also notes that Kronheimer–Mrowka (*Witten's conjecture and Property P*, Corollary 7) earlier proved the conjecture for a more restricted class, also assuming Theorem 3.2.

**Structure of the proof** (FL6 §4).
1. Lemma 4.1 (`lem:AlgCoeff`): if $T_1,\dots,T_n\in V^*$ are linearly independent and the quadratic form $Q$ is non-zero on $\bigcap\ker T_i$, then $T_1,\dots,T_n,Q$ are algebraically independent.
2. Lemma 4.2 (`lem:ReduceDFormToB'Sum`): Lemma 2.8 rewritten as a sum over a fundamental domain $B'(X)$ for $\pm1$ on $B(X)$, with weight $n(K)=\frac12$ if $K=0$ and $1$ otherwise (eq. `eq:DInvarForWCB'Sum` (4.1)).
3. Lemma 4.3 (`lem:ReduceCobordismFormToB'Sum`): Theorem 3.2 rewritten over $B'(X)$ with the combined coefficients
$$b_{i,j,k}(\chi_h,c_1^2,K\cdot\Lambda,\Lambda^2,m)=(-1)^{c(X)+i}a_{i,j,k}(\chi_h,c_1^2,-K\cdot\Lambda,\Lambda^2,m)+a_{i,j,k}(\chi_h,c_1^2,K\cdot\Lambda,\Lambda^2,m)$$
(eqs. `eq:DefineCombinedCoeff` (4.4), `eq:CompareCoeff2` (4.7)) and sign exponent $\tilde\varepsilon(w,\Lambda,K)=\frac12(w^2-\sigma)+\frac12(w^2+(w-\Lambda)\cdot K)$ (eq. `eq:DefineTildeEps` (4.6)).
4. Definition 4.4 (`defn:Useful`, "Useful four-manifolds"): a standard $X$ that has SW simple type with $|B'(X)|=1$, satisfies Witten's equation (4.1), has $f_1,f_2\in B(X)^\perp$ with $f_i^2=0$, $f_1\cdot f_2=1$ and $\{f_1,f_2\}\cup B'(X)$ linearly independent, and on which $Q_X$ is non-zero on $\ker f_1\cap\ker f_2\cap\bigcap_{K\in B'(X)}\ker K$.
5. Lemma 4.5 (`lem:UsefulWithc=3`): for every $h\ge2$ there is a useful $Y_h$ with $\chi_h=h$, $c_1^2=h-3$, $c(Y_h)=3$. These are the Fintushel–Park–Stern manifolds (rational blow-downs of $E(2p-4)$, $E(2p-5)$), with $Y_2=K3\#\overline{\mathbb{CP}}^2$ and $Y_3=E(3)$.
6. Lemma 4.7 (`lem:BlowUpCobordism`): the comparison of (4.1) with (4.7) on the blow-ups $\tilde X(n)$ of a useful $X$ (eq. `eq:BlownUpUsefulCobordismFormula` (4.13)). It uses Lemma 4.6 (`lem:PermutationSumAsDifferenceOperator`, sums over $(\mathbb Z/2)^n$ as iterated difference operators).
7. Proposition 4.8 (`prop:HighDegreeCoefficients`): for integers $x,y$, $m\ge0$, $n>0$, $\chi_h\ge2$, and $i+j+2k=\delta-2m$ with $i\ge n$ and $2y>\delta-4\chi_h-3-n$,
$$b_{i,j,k}(\chi_h,\chi_h-3-n,2x,2y,m)=\begin{cases}(-1)^{x+y}\dfrac{(\delta-2m)!}{k!\,i!}2^{m-k-n},&j=0,\\0,&j>0.\end{cases}$$
8. Remark 4.9 (`rmk:LowerCoeffProb`): only the $b_{i,j,k}$ with $i\ge\chi_h-c_1^2-3$ are determined. The remark says that the early version math/0609530v1 overlooked this: for small $i$ the relations are trivial. Remark 4.10 (unlabelled, "Determining the remaining coefficients") explains why the method, with these examples, cannot determine $b_{0,j,k}$, and that progress would need manifolds with $c>3$ whose basic classes satisfy few linear relations.
9. Theorem 4.11 (`thm:LowDegVanishingForAbundant`, citing FKLM Theorem 1.1): "Theorem 3.2 implies that if $Y$ is a standard and abundant four-manifold and $w$ is characteristic, then $SW^w_{Y,i}$ vanishes for $i<c(Y)-2$", where $SW^w_{Y,i}(h)=\sum_{K\in B(Y)}(-1)^{\varepsilon(w,K)}SW'_Y(K)\langle K,h\rangle^i$.
10. *Case $c_1^2\ge\chi_h-3$.* Blow up $Y$ (allowed by Theorem 2.7, `thm:WCBlowDownInvariance`, which cites Fintushel–Stern, *Rational blowdowns*, Theorem 8.9: Witten's formula holds for $X$ if and only if it holds for $\tilde X$) until $c_1^2(Y)=c_1^2(X_h)$, then blow up once more. Choose $\Lambda=2(af_1+f_2)$ with $\Lambda^2=8a$ and $I(\Lambda)>\delta$. Proposition 4.8 with $n=1$ gives all $b_{i,j,k}$ with $i\ge1$, and the $i=0$ terms cancel in pairs $K_i\pm e^*$. The resulting expression matches (4.1) with $c(\tilde Y)=4$.
11. *Abundant case.* Blow up until $c_1^2=\chi_h-3-n$ with $n\ge1$. Choose $\Lambda=2af_1+2f_2\in B^\perp$ with $8a>\delta-5\chi_h-c_1^2$. Then $K\cdot\Lambda=0$ for all $K$, so the $b_{i,j,k}$ do not depend on $K$, and Theorem 4.11 kills the terms with $i\le n=c(Y)-3$. Proposition 4.8 supplies the rest.

**Role.** FL6 shows how the *qualitative* formula of Theorem 3.2 (universal but unknown coefficients) becomes Witten's formula: the coefficients are determined by examples that already satisfy Witten's formula, together with blow-up and algebraic independence. This works only where enough coefficients are pinned down: $i\ge c-3$ in general, with abundance or $c\le3$ disposing of the rest.

---

## 11. Precursors: the "effective" and low-degree results

These are stated because the task asks about "effective" and $b^+$ conditions. They are proved in the top level ($\ell=0$) or the first level ($\ell=1$), where FL compute the link pairings directly, and they *assume* effectiveness.

* **FL2b, Theorem 1.1** (`thm:DSWSeriesRelation`), also FL2a Theorem 1.1 (same label): "Let $X$ be [a] four-manifold with $b_1(X)=0$ and odd $b_2^+(X)\ge3$. Assume $X$ is abundant, SW-simple type, and effective. For any $\Lambda\in B^\perp$ and $w\in H^2(X;\mathbb Z)$ for which $\Lambda^2=2-(\chi+\sigma)$ and $w-\Lambda\equiv w_2(X)\pmod 2$, and any $h\in H_2(X;\mathbb R)$, one has $\mathbf D^w_X(h)\equiv0\equiv\mathbf{SW}^w_X(h)\pmod{h^{c(X)-2}}$, $\mathbf D^w_X(h)\equiv2^{2-c(X)}e^{\frac12Q_X(h,h)}\mathbf{SW}^w_X(h)\pmod{h^{c(X)}}$." The vanishing assertion is attributed to FKLM.
* **FL2b, Theorem 1.2** (`thm:Main`). General top-level formula: $b_2^+\ge1$; $\alpha\smile\alpha'=0$ on $H^1$; $X$ effective; $w-\Lambda\equiv w_2(X)$; goodness of $w$ if $b_2^+=1$. It has parts (a) vanishing if $\delta<i(\Lambda)$ and $\delta<r(\Lambda)$; (b) an explicit formula if $\delta<i(\Lambda)$, $\delta=r(\Lambda)$, with Jacobi-polynomial coefficients $H_{\chi,\sigma}$; (c) a vanishing range. **FL2b, Theorem 1.4** (`thm:FLthm`) is its specialization to $b_1=0$, odd $b_2^+\ge3$, SW simple type, $\Lambda\in B^\perp$ [corrected by checker: the statement of Theorem 1.4 also assumes that $X$ is effective, and requires $w-\Lambda\equiv w_2(X)$ and $0\le m\le[\delta/2]$]. In case (b):
$$D^w_X(h^{\delta-2m}x^m)=2^{1-\frac12(c(X)+\delta)}(-1)^{m+1+\frac12(\sigma-w^2)}\sum_{\mathfrak s}(-1)^{\frac12(w^2+c_1(\mathfrak s)\cdot w)}SW_X(\mathfrak s)\langle c_1(\mathfrak s)-\Lambda,h\rangle^{\delta-2m}$$
(eq. `eq:DSWrel` (1.19)). **FL2b, Corollary 1.5** (`cor:FLthm`, = FKLM Theorem 1.1, with "effective, abundant, SW-simple type, $c(X)\ge3$"): $\mathbf{SW}^w_X(h)\equiv0\pmod{h^{c(X)-2}}$ [checker: for $w\equiv w_2(X)\pmod 2$]. [added by checker] After Remark 1.3, FL2b states that the effectiveness hypothesis in its Theorems 1.1, 1.2, 1.4 and Corollary 1.5 "can be eliminated" if $S(X)$ in the definition of $r(\Lambda)$ is replaced by the set of all $\mathfrak s$ with $M_{\mathfrak s}$ non-empty. So the top-level results hold unconditionally in that weaker form.
* **FL2b, Theorem 3.33** (`thm:CompactReductionFormula`). The top-level cobordism formula, valid when all reducibles lie in the top level. It is stated with the orientation factor $o_{\mathfrak t}(w,\mathfrak s)=\frac14(w-c_1(\mathfrak t)+c_1(\mathfrak s))^2$ (eq. `eq:OrientationFactor` (3.66)), the same sign as in Memoir Theorem 1. **FL2b, Conjecture 3.34** (`conj:Multiplicity`, = FKLM Conjecture 3.1) is the multiplicity statement. FL2b proves it for $\ell=0$ and says FLLevelOne proves it for $\ell=1$. [added by checker: FL2b also says the conjecture "holds when $\ell=2$" by adapting Leness's wall-crossing proof. No proof is given, so this is unconfirmed.] **FL2b, Corollary 3.35** (`cor:CompactReductionFormula`): given Conjecture 3.34, only SW strata with non-trivial invariants need lie in the top level.
* **FLLevelOne, Theorem 1.1** (`thm:WCL1`). Same hypotheses as FL2b Theorem 1.1 (b_1=0, odd $b_2^+\ge3$, abundant, SW simple type, effective), but with $\Lambda^2=4-(\chi+\sigma)$. Conclusion: Witten's formula modulo $h^{c(X)+2}$.

**Role.** These show what was proved before the Memoir *without* any gluing hypothesis for $\ell=0$, and with only the one-bubble gluing for $\ell=1$, and where "effective" had to be assumed. [corrected by checker: the phrase "with only the one-bubble gluing" should not be read as "proved". The $\ell=1$ results of FLLevelOne (Theorem 1.1 and the level-one case of the multiplicity conjecture) rest on FLLevelOne Theorem 3.8, a one-bubble gluing theorem cited to "[FL3, FL4]". FL3 proves only existence (FL3 §1.5.1), and FL4 does not appear among the sources (Section 3 above). Memoir §7.9 says FL3's method needs significant modification near positive-dimensional $M_{\mathfrak s}$, which is exactly the case FLLevelOne treats. So only the $\ell=0$ results (FL2a, FL2b) are unconditional. The $\ell=1$ results depend on unproved continuity, embedding and surjectivity properties of the one-bubble gluing map.] In the Memoir, "effective" becomes Theorem 10.1.2, conditional on Hypothesis 7.8.1.

---

## 12. Other applications claimed in the Memoir (not checked against sources)

The Memoir's Preface and §1.1 claim the following, none of which is among the provided sources:
* Kronheimer–Mrowka (*Witten's conjecture and Property P*, Geom. Topol. 8 (2004)) use Theorem 1 (their Theorem 6) to prove Witten's conjecture for a large family (their Corollary 7), and hence Property P. [added by checker: FL6 Remark 3.4 (`rmk:PropertyP`) adds that Kronheimer and Mrowka "also gave a proof of Property P which did not rely on Theorem 3.2", citing *Knots, sutures, and excision*, J. Differential Geom. 84 (2010), Corollary 7.23. So Property P itself does not depend on the gluing hypothesis.]
* FL, *The SO(3) monopole cobordism and superconformal simple type* (arXiv 1408.5307), and *Superconformal simple type and Witten's conjecture* (arXiv 1408.5085), proving the superconformal simple type conjecture of Mariño–Moore–Peradze and Witten's conjecture "in full generality for all closed, oriented, smooth four-manifolds with $b_1(X)=0$, odd $b^+(X)\ge3$ [stated as $>1$ in §1.1], and Seiberg–Witten simple type". These are consequences of Theorem 1 and the Memoir's methods, so also conditional on Hypothesis 7.8.1. [added by checker: the bibliography of arXiv 1910.14580 gives both as published in Adv. Math. 356 (2019): 1408.5085 (Witten's conjecture) and 1408.5307 (superconformal simple type). Their content is not checked here.]
* Sivek (IMRN 2015): non-vanishing of Donaldson invariants of symplectic four-manifolds with $b_1=0$ and odd $b^+>1$.
* The Kotschick–Morgan conjecture: Memoir Conjecture 11.2.1 (`conj:KoM`) is asserted true in Theorem 11.6.1 (no `\label`). The proof uses the analogous ASD gluing hypothesis, Hypothesis 11.3.5 (no `\label`), which is not mentioned in the statement of Theorem 11.6.1.

---

## Uncertainties

1. **Numbering is inferred from the arXiv LaTeX, not from published versions.** There is direct evidence that published numberings differ:
   * FL6 cites the gluing hypothesis as "[FL5, Conjecture 6.7.1]"; in math/0203047v4 it is Hypothesis 7.8.1.
   * The Memoir cites "[FL2b, Lemma 3.30]" for the instanton-link pairing; in the arXiv source of FL2b it is Proposition 3.29 (which is how FL6 cites it).
   * FL6 cites "[FL2a, Corollary A.3]" for "if $X$ is simply connected and the SW basic classes are all multiples of a single class then $X$ is abundant". In the arXiv source of FL2a, Corollary A.3 (`cor:OneBasicClassEven`) covers only simply connected **spin** manifolds with $b_2^+\ge3$. The odd case is Corollary A.7 (`cor:OneBasicClassOdd`, with conditions on $b_2^\pm$ and characteristic $K$), and the combined statement is Proposition A.8 (`prop:OneBasicClass`).
2. **Memoir main-theorem numbering.** `mainthm` and `mainconj` share a counter that is not reset by chapter or section, so I infer "Theorem 1" and "Conjecture 2". The compiled Memoir could display these differently, for example as "Theorem 1.1".
3. **FL6 "Main Theorem 1.2".** The environment name is "Main Theorem" and it shares the section counter, so it displays as "Main Theorem 1.2"; I have not seen the compiled text.
4. **Internal inconsistencies in the Memoir's dimension conditions.**
   * Theorem 8.1.9 imposes $\deg(z)+2\eta=\dim\mathcal M^{*,0}_{\mathfrak t}-2$ but uses $\bar{\mathcal W}^{\eta-1}$.
   * Theorem 10.1.1 imposes $\delta-2m+2\eta=\dim\mathcal M_{\mathfrak t}-2$ although $\deg(h^{\delta-2m}x^m)=2\delta$.
   
   The consistent normalization, used in Proposition 10.6.1 and in the proof of Theorem 1, is $\deg(z)+2e=\dim\mathcal M_{\mathfrak t}-2$ for the exponent $e$ of $\bar{\mathcal W}$. I have reported the statements as printed.
5. **Implicit dependence on Hypothesis 7.8.1.** Only Theorem 1 states it as an assumption. Theorems 8.1.9 (for $\ell\ge1$), 10.1.1 and 10.1.2 and Proposition 10.6.1 depend on it through Definition 8.1.3 and Proposition 9.1.1, but do not say so in their statements. Theorem 11.6.1 likewise depends on Hypothesis 11.3.5.
6. **Status of the gluing hypothesis.** None of the provided sources contains a proof of Hypothesis 7.8.1, of FL6 Hypothesis 3.1, or of the overlap paper's Theorem 4.2. The Memoir (Dec 2018) refers to a book "in preparation". FL3 Theorem 1.1 proves only existence (no continuity, injectivity or surjectivity). It also has the restriction $0<\ell<\lfloor\kappa\rfloor$ and works in a thickened moduli space with a small-eigenvalue cut-off, which the Memoir (§7.9) says is inadequate near positive-dimensional $M_{\mathfrak s}$. Everything in Sections 2, 5, 6, 10, 12 is therefore conditional. [added by checker: the same applies to the $\ell=1$ results of FLLevelOne, through its Theorem 3.8, cited to "[FL3, FL4]"; FL4 is not among the sources and is not cited in the Memoir. The 2019 paper arXiv 1910.14580 proves a one-bubble gluing chart for anti-self-dual connections only, and says only that its method "should apply" to SO(3) monopoles. So no provided source proves any level-$\ell\ge1$ case of the SO(3)-monopole gluing hypothesis.]
7. **FL6 Hypothesis 3.1 versus Memoir Hypothesis 7.8.1.** The FL6 hypothesis is phrased stratum by stratum and is weaker on its face. The Memoir hypothesis is global over the space of global splicing data and includes transversality on every stratum, lower semicontinuity of the obstruction norm, and a homotopy to the global splicing map. The sources do not say whether FL6's phrasing alone suffices for the Memoir's argument.
8. **Kronheimer–Mrowka statement.** Taken only from FL restatements, which differ:
   * FL6 Theorem 2.2 includes the hypothesis that some Donaldson invariant is non-zero and cites "Theorem 1.7(a)". The Memoir and FL2b omit that hypothesis and cite "Theorem 1.7", with index misprints.
   * KM simple type is defined "for some $w$" in the Memoir and FL2b, and "for all $w$" in FL6; FL6 Theorem 2.4 reconciles the two.
   * The journal volume is given as J. Differential Geom. **41** (1995), 573–734 in the Memoir's bibliography and as **43** in FL6's. I cannot settle this from the sources.
9. **Meaning of "real analytic" for $a_{i,j,k}$** (FL6 Theorem 3.2). The domain is $\mathbb Z^4\times\mathbb N$, and a source comment says the dependence is "not necessarily polynomial". The precise sense is not stated.
10. **The FL6 proof of the case $c_1^2\ge\chi_h-3$** asserts, citing FL2a Corollary A.3, the existence of $f_1,f_2\in H^2(Y;\mathbb Z)$ with $K_1\cdot f_i=0$, $f_i^2=0$, $f_1\cdot f_2=1$ for an arbitrary standard $Y$ in that range. The cited corollary's hypotheses, in the arXiv FL2a, do not obviously cover such $Y$. I have not determined whether orthogonality to $K_1$ is actually used in that step: the subsequent argument seems to use only $\Lambda^2=8a$ and $\Lambda\equiv0\pmod2$.
11. **The Memoir's footnote on the Kronheimer–Mrowka Property P paper** prints the "wrong" and "correct" values of $i(\Lambda)$ without the $\Lambda^2$ term. The theorem's own statement has $i(\Lambda)=\Lambda^2-\frac14(3\chi+7\sigma)$.
12. **Preface versus introduction of the Memoir.** The preface says the superconformal simple type conjecture and Witten's conjecture in full generality appear in [FL7] and [FL8] "respectively". The introduction attributes superconformal simple type to [FL8] and Witten's conjecture to [FL7], which matches the bibliography titles. These papers are not among the sources, and their claims are unverified here.
13. **Equation numbers** were computed with a simple counter (it handles `equation`, `align`, `multline`, `gather`, `\notag`). They may be off where the source uses unusual constructions; the labels are reliable. [checker: an independent recount agrees on every equation number spot-checked; see the remark in Section 0.]
14. **Integrality of $\ell$** in Theorem 1 under the stated parity hypothesis is my own verification, not a statement in the source. [checker: re-verified. Two integral lifts of $w_2(X)$ differ by an element of $2H^2(X;\mathbb Z)$, so $c_1(\mathfrak s)-\Lambda=2a-w$ for some integral class $a$, and hence $(c_1(\mathfrak s)-\Lambda)^2\equiv w^2\pmod 4$.]
15. [added by checker] **Sign conventions, FL6 versus the Memoir.** FL6 Theorem 3.2's sign equals the Memoir's $(-1)^{o_{\mathfrak t}(w,\mathfrak s)}$ only when $\Lambda^2$ is even; otherwise the two differ by the $K$-independent factor $-1$ (Section 5). The difference can be absorbed into the coefficients, and it never arises in FL6's applications, but it must be kept in mind when FL6's coefficients $a_{i,j,k}$ are compared with the Memoir's $p_{\delta,\ell,m,i}$.
