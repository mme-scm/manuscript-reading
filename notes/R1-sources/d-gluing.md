# (d) Gluing at reducible strata and the overlap problem: what Feehan–Leness prove and what they assume

Extraction note from the arXiv LaTeX sources listed in Section 0. Statements are copied with light cleaning of the LaTeX. Nothing has been added to any hypothesis. Where a source is internally inconsistent, or where one paper attributes to another more than that paper states, this is recorded rather than corrected. Theorem numbers are inferred from the LaTeX counters, since the compiled PDFs were not consulted. The `\label` is given in every case. Conventions agree with the companion notes `a-cobordism.md` and `b-compactness.md`.

---

## 0. Sources, authorship and numbering

| Short name | arXiv, file | Authors and date in source | Numbering |
|---|---|---|---|
| FL3 | math/9907107, `main.tex` | Feehan, Leness; "This version: July 20, 1999" | `amsart`; *section.n*; `thm` shared by Lemma, Condition, Corollary, Claim, Proposition, Criterion, Algorithm, Assumption, Conjecture, Convention, Data, Definition, Example, Question, Notation, Remark, Problem |
| FL2a | math/0007190, `main.tex` | Feehan, Leness (J. reine angew. Math. 538 (2001)) | same convention |
| FLLevelOne | math/0106238, `main.tex` | Feehan, Leness (Topology Appl. 124 (2002)) | same convention |
| Overlap paper | 1211.0480, `main.tex` | **Feehan and Leness** (the task lists Feehan alone, but the title page lists both). Dated May 7, 2005; Fields Inst. Commun. 47 (2005), 97–118, per the Memoir bibliography | `amsart`; `thm` within section, shared by Lemma, Definition, Example, Exercise, Conjecture, Remark; **Proposition has its own counter within section** |
| Memoir | math/0203047 v4, `FeehanLenessMonopoleCobordism_v4-clean.tex` | Feehan, Leness; Dec. 26, 2018; Mem. Amer. Math. Soc. 256 (2018), no. 1226 | `amsbook`; *chapter.section.n*; main theorem on a separate counter shared with `mainconj` ("Theorem 1", "Conjecture 2") |
| FL6 | math/0609530, `jems-feehanleness_PF11-22-2014.tex` | Feehan, Leness; Nov. 22, 2014; J. Eur. Math. Soc. 17 (2015) | `article`; *section.n*; one counter shared by Theorem, Corollary, Conjecture, Lemma, Problem, Proposition, **Main Theorem**, Definition, **Hypothesis**, Remark, Example [corrected by checker: Example also shares the counter] |
| Banach-corners paper | 1910.14580, `kuranishi_model_boundary_moduli_space.tex` | **Feehan and Leness** (the task lists Feehan alone, but the source lists both). The date is `\today` | Introduction results on a separate counter `mainthm`, shared by `maincor` and `maindefn`: Theorems 1–3, Corollaries 4–7. The body uses `thm` within section |
| Announcement | dg-ga/9709022, `main.tex` | Feehan, Leness (Topology Appl. 88 (1998)) | `amsart`, *section.n* |

**Works cited as forthcoming, none of which is among the sources.**
- FL3 cites "[FL4] PU(2) monopoles. IV: Surjectivity of gluing maps, in preparation" and "[FLConj] PU(2) monopoles. V: Intersection theory, in preparation".
- The overlap paper cites the same FL4 as "in preparation".
- FLLevelOne writes (§1): "At the time of writing, work on [FL4] and [FL5] is still in progress".
- The 2018 Memoir no longer cites FL4. It cites instead "[Feehan_Leness_monopolegluingbook] P. M. N. Feehan and T. G. Leness, *Gluing maps for SO(3) monopoles and invariants of smooth four-manifolds*, in preparation, based in part on arXiv:math/9812060 and arXiv:math/9907107".
- FLKM1 = math/9812060 (*Donaldson invariants and wall-crossing formulas. I: Continuity of gluing and obstruction maps*) is cited for the anti-self-dual case. It is not among the sources and was not read.

No source in this set cites a completed version of FL4 or of the gluing book.

[added by checker] FL3 itself appears in the 2018 Memoir's bibliography only as "arXiv:math/9907107", with no journal reference (FLLevelOne's bibliography lists it as "submitted to a print journal"). So, as far as these sources show, the existence half of the gluing theory was never published in a journal.

---

## 1. Notation (FL3, §§2–3, §9; Memoir, Chapter 2)

- $(X,g)$ is closed, connected, oriented and smooth, with $b^+(X)>0$.
- $\mathfrak t=(\rho,W^+,W^-,E)$ is a spin$^u$ structure, and $\kappa=c_2(E)-\tfrac14c_1(E)^2$.
- $\mathfrak t_\ell=(\rho,W^+,W^-,E_\ell)$ with $\det E_\ell=\det E$ and $c_2(E_\ell)=c_2(E)-\ell$. The Memoir writes $\mathfrak t(\ell)$, with $p_1(\mathfrak t(\ell))=p_1(\mathfrak t)+4\ell$.
- **The monopole map.**
  $$\mathfrak S(A,\Phi)=\big(F_A^+-\tau\rho^{-1}(\Phi\otimes\Phi^*)_{00},\ D_A\Phi+\rho(\vartheta)\Phi\big)$$
  (FL3 eq. `eq:PT`). Its linearization is $d^1_{A,\Phi}=(D\mathfrak S)_{A,\Phi}$.
- **Moduli and configuration spaces.** $M(\mathfrak t)\subset\mathcal C(\mathfrak t)$ is the moduli space. $\mathcal C^{*,0}(\mathfrak t)$ consists of pairs whose connection is irreducible and whose spinor is not identically zero; equivalently, the stabilizer is $\{\mathrm{id}_E\}$. $M^{*,0}(\mathfrak t)=M(\mathfrak t)\cap\mathcal C^{*,0}(\mathfrak t)$. The Memoir writes $\mathcal M_{\mathfrak t}$ and $\mathcal C_{\mathfrak t}$, and $\bar{\mathcal C}_{\mathfrak t}=\bigsqcup_\ell \mathcal C_{\mathfrak t(\ell)}\times\mathrm{Sym}^\ell(X)$ (eq. `eq:IdealPairs`) with the Uhlenbeck topology.
- **Reducible (Seiberg–Witten) strata.** If $\mathfrak t(\ell)$ splits as $\mathfrak s\oplus\mathfrak s\otimes L$, the Seiberg–Witten moduli space $M_{\mathfrak s}$ embeds in $\mathcal M_{\mathfrak t(\ell)}$ as the set of pairs that are reducible with respect to this splitting. [corrected by checker: FL2a, Lemma 3.13 (`lem:RedAreSW`) gives a topological embedding $\iota:M_{\mathfrak s}\hookrightarrow\mathcal C_{\mathfrak t}$ with this image only under the hypothesis $w_2(\mathfrak t)\neq0$; if $w_2(\mathfrak t)=0$ it says only that zero-section points of $M_{\mathfrak s}$ go to zero-section reducibles, not necessarily injectively when $b_1(X)>0$. The Memoir (§2.3.3) restates it as an embedding of $M^0_{\mathfrak s}$, and of $M_{\mathfrak s}$ when $w_2(\mathfrak t)\neq0$ or $b_1(X)=0$. Lemma 3.13 says nothing about the spinor being non-zero. That conclusion is FL2a Corollary 3.3 (`cor:NoSWZeroSections`), under the Morgan–Mrowka criterion.] It appears in $\bar{\mathcal M}_{\mathfrak t}$ as the ideal stratum $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$. Its level is $\ell=\ell(\mathfrak t,\mathfrak s)=\tfrac14((c_1(\mathfrak t)-c_1(\mathfrak s))^2-p_1(\mathfrak t))$ (Memoir eq. `eq:ReducibleLevel`).
- **Zero-section reducibles** (reducible anti-self-dual connections) are excluded by the hypothesis on $w$ in FL3 §2.1:
  > "we further constrain the class $w$ by requiring that no SO(3) bundle $P$ over $X$ with $w_2(P)\equiv w\pmod 2$ admit a flat, reducible connection … the Morgan-Mrowka criterion ensures that the Uhlenbeck compactification $\bar M(\mathfrak t)$ contains no reducible, zero-section pairs if $b^+(X)>0$ and the metric $g$ is generic (see Propositions 2.9(1) and 3.1(3) and Lemma 3.3 in [FL2a])."
- **Strata of the symmetric product.** $\Sigma\subset\mathrm{Sym}^\ell(X)$ is the smooth stratum given by a partition $\kappa_1\ge\dots\ge\kappa_m\ge1$ of $\ell$.
- **Gluing data (FL3 §3.1.2).**
  - $\mathbf{Fr}(\mathcal U_\ell,\Sigma)\to\mathcal U_\ell\times\Sigma$ is a principal bundle with group $\mathbf G(\Sigma)=\big(\prod_{i=1}^m(SO(3)\times SO(4))\big)\rtimes\mathfrak S(\kappa_1,\dots,\kappa_m)$.
  - The fibre is
    $$\mathbf Z(\Sigma)=\prod_{i=1}^m\big(\tilde M^{\diamond}_{E^i}\times_{\mathcal G_{E^i}}\mathrm{Fr}(\mathfrak g_{E^i})|_s\times\mathbb R^+\big),$$
    built from **genuine** (non-ideal) centred anti-self-dual connections on $S^4$, framed at the south pole, together with a scale.
  - $\mathbf{Gl}(\mathcal U_\ell,\Sigma)=\mathbf{Fr}\times_{\mathbf G(\Sigma)}\mathbf Z(\Sigma)$. The bundle $\mathbf{Gl}(\mathcal U_\ell,\Sigma,\lambda_0)$ requires all scales to be less than $\lambda_0$, and $\mathbf{Gl}^+$ requires $8\sqrt{\lambda_i}+8\sqrt{\lambda_j}<\mathrm{dist}_g(x_i,x_j)$ (eq. `eq:ConstrainedGluingDataBundle`).
- **Small-eigenvalue projection and the extended equation.** $\Pi_{A,\Phi,\mu}$ is the $L^2$-orthogonal projection onto the span of the eigenvectors of $d^1_{A,\Phi}d^{1,*}_{A,\Phi}$ with eigenvalues in $[0,\mu]$. The *extended equation* is $\Pi^\perp_{A,\Phi,\mu}\mathfrak S((A,\Phi)+(a,\phi))=0$, with $(a,\phi)=d^{1,*}_{A,\Phi}(v,\psi)$ and $\Pi_{A,\Phi,\mu}(v,\psi)=0$. The *obstruction equation* is $\Pi_{A,\Phi,\mu}\mathfrak S((A,\Phi)+(a,\phi))=0$ (FL3 §9.1). The partial right inverse is $P_{A,\Phi,\mu}=d^{1,*}_{A,\Phi}G_{A,\Phi,\mu}$.
- **The thickened space $M(\mathfrak t,\mu)$.** FL3 describes it only as "a finite-dimensional thickened or virtual moduli space of PU(2) monopoles which contains $M(\mathfrak t)$, as a submanifold away from singularities, with $\mu>0$ a small-eigenvalue bound arising in the extended PU(2) monopole equations which define $M(\mathfrak t,\mu)$" (FL3 §1.1). FL3 gives no more precise definition. §9.6 defines instead the open set $\mathcal C(\mathfrak t,\mu,\varepsilon)$ (see Section 2).

---

## 2. FL3, Theorem 1.1 (`thm:GluingTheorem1`): existence of local gluing and obstruction maps

**Statement** (FL3 §1.1):

> Let $E$ be a rank-two, Hermitian vector bundle over $X$ with $c_1(E)=w$ and $c_2(E)-\frac14c_1(E)^2=\kappa\ge1$. Let $0<\ell<\lfloor\kappa\rfloor\le\kappa$ be an integer, let $E_\ell$ be the rank-two, Hermitian vector bundle over $X$ with $\det E_\ell=\det E$ and $c_2(E_\ell)=c_2(E)-\ell$. Let $\mathfrak t=(\rho,W^+,W^-,E)$ and $\mathfrak t_\ell=(\rho,W^+,W^-,E_\ell)$. Let $\Sigma\subset\mathrm{Sym}^\ell(X)$ be a smooth stratum and let $\mathcal U_{\ell,\mu}\Subset M(\mathfrak t_\ell,\mu)$ be a finite-dimensional, precompact, open, $S^1$-invariant subset. The space $\mathcal U_{\ell,\mu}$ is a tubular neighborhood of $\mathcal U_{\ell,\mu}\cap M^{*,0}(\mathfrak t_\ell)$, of size $\varepsilon_\ell>0$ via the tubular distance function (`eq:DeformCondn`). Then, for small enough positive constants $\varepsilon_\ell$ and $\lambda_0$, there are
> - A compact Lie group $\mathbf G(\Sigma)$, an $S^1$-equivariant $C^\infty$ principal $\mathbf G(\Sigma)$-bundle $\mathbf{Fr}(\mathcal U_{\ell,\mu},\Sigma)\to\mathcal U_{\ell,\mu}\times\Sigma$, a universal topological $\mathbf G(\Sigma)$-space $\mathbf Z(\Sigma)$, and an $S^1$-equivariant fiber bundle $\mathbf{Gl}(\mathcal U_{\ell,\mu},\Sigma,\lambda_0)=\mathbf{Fr}(\mathcal U_{\ell,\mu},\Sigma)\times_{\mathbf G(\Sigma)}\mathbf Z(\Sigma)\to\mathcal U_{\ell,\mu}\times\Sigma$. Here, $\lambda_0$ is a sufficiently small positive constant, depending at most on $(g,\kappa,\mathcal U_{\ell,\mu})$.
> - An $S^1$-equivariant $C^\infty$ map $\boldsymbol\gamma_{\mu,\Sigma}:\mathbf{Gl}(\mathcal U_{\ell,\mu},\Sigma,\lambda_0)\to M^{*,0}(\mathfrak t,\mu)$, where $\mathbf{Gl}^+(\mathcal U_{\ell,\mu},\Sigma,\lambda_0)\subset\mathbf{Gl}(\mathcal U_{\ell,\mu},\Sigma,\lambda_0)$ is the open subset (`eq:ConstrainedGluingDataBundle`).
> - An $S^1$-equivariant $C^\infty$ section $\boldsymbol\chi_{\mu,\Sigma}$ of an $S^1$-equivariant $C^\infty$ vector bundle $\Xi_\mu$ over $\mathbf{Gl}^+(\mathcal U_{\ell,\mu},\Sigma,\lambda_0)$. The bundle $\Xi_\mu$ has real rank equal to $2\ell$ plus the real codimension of $M^{*,0}(\mathfrak t)\subset M^{*,0}(\mathfrak t,\mu)$.
>
> Together, the map $\boldsymbol\gamma_{\mu,\Sigma}$ and section $\boldsymbol\chi_{\mu,\Sigma}$ have the property that
> $$\boldsymbol\gamma_{\mu,\Sigma}(\boldsymbol\chi^{-1}_{\mu,\Sigma}(0))\subset M^{*,0}(\mathfrak t).$$

**Standing hypotheses** (§1.1, §2.1, §3):
- $X$ is closed, connected, oriented and $C^\infty$, with $b^+(X)>0$ and a spin$^c$ structure $\mathfrak s_0$.
- The perturbation parameters are generic, "so the transversality results of [DK], [FeehanGenericMetric], and [FU] ensure that the moduli spaces of PU(2) monopoles, Seiberg-Witten U(1) monopoles, and anti-self-dual SO(3) connections possess the usual smoothness properties and have the expected dimension".
- No SO(3) bundle with $w_2\equiv w\pmod 2$ admits a flat connection (§1.1). [corrected by checker: the original said that §2.1 "strengthens" this to the Morgan–Mrowka condition. In fact §2.1 ("As in the hypothesis of Theorem 1.1, we further constrain the class $w$…") requires only that no such bundle admit a flat, *reducible* connection, which is literally weaker than the §1.1 condition. It then cites the Morgan–Mrowka spherical-class criterion as a *sufficient* condition, which in fact excludes all flat connections (FL2a Lemma 3.2). Either way, the effect used is the one quoted in Section 1: no reducible zero-section pairs in $\bar M(\mathfrak t)$ for generic $g$.]
- The Sobolev index satisfies $k\ge4$.

**Hypotheses in the statement:**
1. $E$ has rank two with $c_1(E)=w$ and $\kappa\ge1$.
2. $\ell$ is an integer with $0<\ell<\lfloor\kappa\rfloor$.
3. $\Sigma$ is a single smooth stratum of $\mathrm{Sym}^\ell(X)$.
4. $\mathcal U_{\ell,\mu}\Subset M(\mathfrak t_\ell,\mu)$ is finite-dimensional, precompact, open and $S^1$-invariant, and is a tubular neighbourhood of size $\varepsilon_\ell$ of $\mathcal U_{\ell,\mu}\cap M^{*,0}(\mathfrak t_\ell)$.
5. $\varepsilon_\ell$ and $\lambda_0$ are small.

The display `eq:DeformCondn`, cited as the "tubular distance function", is in fact the triple of open conditions (FL3 §9.6):
$$\mathrm{Spec}(d^1_{A,\Phi}d^{1,*}_{A,\Phi})\subset[0,\tfrac12\mu)\cup(\mu,\infty),\qquad \|\mathfrak S(A,\Phi)\|_{L^{\sharp,2;2}(X)}<\varepsilon,\qquad \|P_{A,\Phi,\mu}\|_A<C<\infty,$$
where $C=C(\mathcal U_{\ell,\mu},\kappa,\mu,g)$ and $\|\cdot\|_A$ is the operator norm on $\mathrm{Hom}(L^{\sharp,2;2}(X),L^2_{1,A}(X))$.

**How the maps are defined** (FL3 §9.6, "Completion of proof of main theorem"):
- $\boldsymbol\gamma_{\mu,\Sigma}=\boldsymbol\delta_\mu\circ\boldsymbol\gamma'_{\mu,\Sigma}$ on $\mathbf{Gl}^+(\mathcal U_{\ell,\mu},\Sigma,\lambda_0)$, where $\boldsymbol\gamma'$ is the splicing map and $\boldsymbol\delta_\mu(A,\Phi)=(A,\Phi)+d^{1,*}_{A,\Phi}(v,\psi)$ is the solution of the extended equation from Theorem 9.5.
- $\boldsymbol\chi_{\mu,\Sigma}=\boldsymbol\varphi_\mu\circ\boldsymbol\gamma_{\mu,\Sigma}$, where $\boldsymbol\varphi_\mu(A,\Phi)=\Pi_{A,\Phi,\mu}\mathfrak S(\boldsymbol\delta_\mu(A,\Phi))$.
- $\Xi_\mu=\boldsymbol\gamma^*_{\mu,\Sigma}\mathfrak V_\mu$, where $\mathfrak V_\mu$ is the "continuous, finite-rank, pseudovector bundle" with fibres $\mathrm{Ran}\,\Pi_{A,\Phi,\mu}$ over
  $$\mathcal C(\mathfrak t,\mu,\varepsilon)=\{(A,\Phi):\text{(`eq:DeformCondn`) holds}\}/\mathcal G_E.$$
- Smoothness is asserted "upon restriction to $\mathcal C^0(\mathfrak t)$". The constant rank of $\mathfrak V_\mu$ over the image of the splicing map comes from Theorem 8.3 and the choice of $\mathcal U_{\ell,\mu}$.

**What FL3 says it does not prove** (§1.5.1, "Properties of gluing maps"). [corrected by checker: the original said "quoted in full". The final sentence of the paragraph is omitted below. It reads: "In particular, despite an extensive literature on gluing theory for anti-self-dual connections, the existing accounts … even there only address somewhat special cases which do not capture all of the difficulties one encounters when attempting to solve the complete gluing problem for anti-self-dual connections." §1.3 also lists "the embedding property, surjectivity, and Uhlenbeck continuity" as "additional properties required" that it "will take a sequel [FL4] to complete".]

> The reader will note that the main result proved here is at most the first half of a desired "gluing theorem". To be of use for parameterizing neighborhoods of ideal, reducible PU(2) monopoles, we also need the following properties:
> 1. *Continuity.* The local gluing map $\boldsymbol\gamma_{\mu,\Sigma}$ extends to a continuous map on the Uhlenbeck closure of the gluing data, $\bar{\mathbf{Gl}}^+(\mathcal U_{\ell,\mu},\Sigma,\lambda_0)$.
> 2. *Embedding property.* The map $\boldsymbol\gamma_{\mu,\Sigma}$ is a smooth embedding of $\mathbf{Gl}^+(\mathcal U_{\ell,\mu},\Sigma,\lambda_0)$ and a topological embedding of the Uhlenbeck closure of the gluing data, $\bar{\mathbf{Gl}}(\mathcal U_{\ell,\mu},\Sigma,\lambda_0)$.
> 3. *Surjectivity.* The image of $\bar{\mathbf{Gl}}^+(\mathcal U_{\ell,\mu},\Sigma,\lambda_0)\cap\boldsymbol\chi^{-1}_{\mu,\Sigma}(0)$ under $\boldsymbol\gamma_{\mu,\Sigma}$ is an open subset of $\bar M(\mathfrak t)$ and the space $\bar M(\mathfrak t)$ has a finite covering by such open subsets.
>
> These remaining properties (1), (2), (3) are proved in [FL4] and comprise the second half of the gluing theorem. It is important to note that preceding three gluing-map properties are not simple consequences of the proof of existence of solutions to the (extended) PU(2) monopole equations and their justification constitutes the more difficult half of the proof of the full gluing theorem.

Here [FL4] is "PU(2) monopoles. IV: Surjectivity of gluing maps, in preparation".

**Further limitations visible in the source.**
- *(a) One stratum at a time, away from its closure.*
  - The fibre $\mathbf Z(\Sigma)$ contains only genuine centred instantons on $S^4$. It has no ideal points: no bubbling on the sphere and no product-connection strata.
  - The constraint $8\sqrt{\lambda_i}+8\sqrt{\lambda_j}<\mathrm{dist}(x_i,x_j)$ keeps the points of $\Sigma$ apart.
  - Hence Theorem 1.1 says nothing at the boundary of $\Sigma$ in $\mathrm{Sym}^\ell(X)$, at $\lambda_i=0$, or across strata.
- *(b) Even the splicing map's properties are deferred.* §3.2 ends: "The construction, thus far, yields a splicing map giving a smooth embedding $\boldsymbol\gamma':\mathbf{Gl}(\mathcal U_\ell,\Sigma,\lambda_0)\to\mathcal C^{*,0}(\mathfrak t)$. The fact that the map is a smooth embedding is a fairly straightforward consequence of the definitions; it will follow from the stronger result in [FL4] … Similarly, the fact that the image of $\boldsymbol\gamma'$ contains only irreducible, non-zero-section pairs is also a fairly easy consequence of the definitions; it is proved in [FL4]."
- *(c) Only the extended equation is solved.* §9 says: "Unlike in [TauIndef], we shall not attempt to also solve the obstruction equation for PU(2) monopoles … as this will not be necessary for our topological applications [FLConj]". Transversality of $\boldsymbol\chi_{\mu,\Sigma}$ is not asserted.
- *(d) Spectral flow.* §1.3 states Problem 1.5 (`prob:SpectralFlow`): "If $\dim M_{\mathfrak s}^{sw}>0$, one cannot necessarily fix a single, uniform positive upper bound $\mu$ for the small eigenvalues of $d^1_{A,\Phi}d^{1,*}_{A,\Phi}$, due to spectral flow as the point $[A,\Phi]$ varies in a space $\mathcal U_\ell\subset\mathcal C(\mathfrak t_\ell)$ containing $M_{\mathfrak s}^{sw}$." The theorem avoids this by requiring the spectral gap in `eq:DeformCondn` on $\mathcal U_{\ell,\mu}$. The Memoir (§7.9; see Section 8.2 [corrected by checker: the original pointed to Section 8.4, which is about Hypothesis 11.3.5]) reads this as a restriction to neighbourhoods with small spectral flow, valid near a zero-dimensional $M_{\mathfrak s}$ but not near a positive-dimensional one.
- *(e) The local solutions do not fit together.* §9.2: "solutions $(A+a,\Phi+\phi)$ to (`eq:QuickExtPUMonEqnForvpsi`) corresponding to bundles of gluing data defined by the different strata $\Sigma$ of the symmetric product $\mathrm{Sym}^\ell(X)$ will not fit together (even aside from the jumping-line or spectral flow problem) to form a smooth submanifold of $\mathcal C^{*,0}(\mathfrak t)$". The remedy (a global gluing-data space and a global splicing map, deformed by FL3's method) is deferred to FLConj.
- *(f) Are reducible background pairs allowed?* The statement is phrased through $M^{*,0}(\mathfrak t_\ell)$, the irreducible pairs with non-zero spinor. The abstract and the opening paragraph of §1 [corrected by checker: the quotation is from §1 before §1.1, not from §1.1] say, however, that the purpose is "to provide topological models for neighborhoods of ideal Seiberg-Witten moduli spaces appearing in lower levels". The abstract says this is "the ultimate purpose of the gluing theorem", of which FL3 proves "the first part". The splicing of §3.2 accepts any $(A_0,\Phi_0)\in\mathcal U_\ell\subset\mathcal C(\mathfrak t_\ell)$. Theorem 8.3 allows an obstructed background ($n=\dim\mathrm{Ker}\,d^{1,*}_{A_0,\Phi_0}$). The theorem never says explicitly that reducible backgrounds are covered. Later papers apply FL3 with the background in the Seiberg–Witten virtual neighbourhood $\boldsymbol\gamma_{\mathfrak s}(N_{\mathfrak t(\ell),\mathfrak s})$ of FL2a (overlap paper §3.1; Memoir §7.8; FLLevelOne §3).
- *(g) Internal inconsistencies.*
  - The statement has $0<\ell<\lfloor\kappa\rfloor$, but §3.1.2 has $1\le\ell\le\lfloor\kappa\rfloor$.
  - $\boldsymbol\gamma_{\mu,\Sigma}$ is stated on $\mathbf{Gl}$ but constructed on $\mathbf{Gl}^+$. [added by checker: §3.2 also writes $\mathbf{Gl}(\mathcal U_\ell,\Sigma,\lambda_0)\subset\mathbf{Gl}^+(\mathcal U_\ell,\Sigma)$. That treats the $\lambda_0$-bundle as already satisfying the separation constraint, whereas §3.1.2 defines it only by $\lambda_i<\lambda_0$.]
  - The target $M^{*,0}(\mathfrak t,\mu)$ is never defined. The construction lands in $\mathcal C(\mathfrak t)$ and is cut down by $\boldsymbol\chi$.
  - The "tubular distance function" reference points to the open conditions above.

**Role.** This is the only analytic theorem in the sources that constructs solutions near a lower-level stratum $M_{\mathfrak s}\times\Sigma$ of the SO(3)-monopole compactification. It gives the existence half of a local Kuranishi-type model over one stratum $\Sigma$ at a time, under a uniform spectral gap. The embedding, Uhlenbeck-continuity and surjectivity halves, which are needed to identify $\boldsymbol\chi^{-1}(0)$ with a neighbourhood in $\bar M(\mathfrak t)$, are stated by the authors to be outside the paper.

---

## 3. FL3, Theorem 9.5 (`thm:ExtPUMonExist`) and Corollary 9.3 (`cor:L21AEstPAaphi`): the analytic core

**Theorem 9.5:**

> Let $(X,g)$ be a closed, oriented, $C^\infty$ Riemannian four-manifold. There are constants $C$ and $\varepsilon(C)$, with the dependence indicated in condition (`eq:L21AEstPAaphiConstant`), such that the following holds. Let $(A,\Phi)$ be an $L^2_4$ pair on $(\mathfrak g_E,V^+)$ produced by the splicing construction of §3, with $\|\mathfrak S(A,\Phi)\|_{L^{\sharp,2}(X)}<\varepsilon$. Then there is a unique solution $(v,\psi)\in C^0\cap L^2_2(\Lambda^+\otimes\mathfrak g_E)\oplus L^2_2(V^-)$ to the extended PU(2)-monopole equation such that $\Pi_{A,\Phi,\mu}(v,\psi)=0$ and
> $$\|d^{1,*}_{A,\Phi}(v,\psi)\|_{L^2_{1,A}(X)}\le C\|\mathfrak S(A,\Phi)\|_{L^{\sharp,2}(X)}.$$
> Moreover, if $(A,\Phi)$ is an $L^2_l$ pair, for any $l\ge3$, then the solution $(v,\psi)$ is contained in $L^2_{l+1}$.

(The source has a typographical slip: "$\mathfrak S(A,\Phi)\|_{L^{\sharp,2}(X)}<\varepsilon$" with the opening norm bar missing.) The constant is
$$C=C(\mathcal U_{\ell,\mu},\kappa,\|F_{A_d}\|_{L^\infty},\|F_{A_e}\|_{L^\infty},\|\vartheta\|_{L^\infty},\mu).$$

**Corollary 9.3:** under the hypotheses of Theorem 9.2 (`thm:L21AEstPAaphi`, the $L^2_{1,A}$ estimate for $d^{1,*}_{A,\Phi}$ on spliced pairs), for all $(\xi,\varphi)\in L^{\sharp,2}\oplus L^2$,
$$\|P_{A,\Phi,\mu}(\xi,\varphi)\|_{L^2_{1,A}(X)}\le C\|(\xi,\varphi)\|_{L^{\sharp,2;2}(X)},$$
"where $C$ now also depends continuously on $0<\mu<\infty$".

**Hypotheses.** $(A,\Phi)$ must be a *spliced* pair. §9.2 records that the proof of Theorem 9.2 "assumed that $\Phi'\equiv0$ where the connection $A'$ bubbles: this assumption is used in a crucial way in equation (`eq:LpBoundWorstTerm`)". So the estimate is not available for arbitrary pairs near the stratum. The smallness of $\|\mathfrak S(A,\Phi)\|$ comes from Proposition 5.5 (`prop:CutoffMonoPairEst`) for small $\mathcal U_{\ell,\mu}$ and $\lambda_0$ (Remark 9.6).

**Role.** This is the uniform right-inverse estimate the authors identify as the main difficulty peculiar to SO(3) monopoles. Problem 1.4 (`prob:FA+FA-BochnerProblem`) says that $F_A^-$ enters the Weitzenböck formula for $D_AD_A^*$ and is only $L^{\sharp,2}$-bounded, not small. It is proved, together with existence for the extended equation by the contraction principle. It is the input that later papers call "the solution map".

---

## 4. FL3, Theorem 8.3 (`thm:H2SmallEval`) and Corollary 8.4 (`cor:H2SmallEval`): small eigenvalues

**Theorem 8.3:**

> Continue the notation of Definition 8.1 [`defn:LambdaClosePair`]. Suppose $\lambda\in(0,\lambda_0]$ and let $(A,\Phi)$ be an $L^2_k$ pair on $(\mathfrak g_E,V)$ which is $\lambda$-close to the ideal pair $(A_0,\Phi_0,\mathbf x)$. Assume that the kernel of $d^1_{A_0,\Phi_0}d^{1,*}_{A_0,\Phi_0}$ has dimension $n$ and let $N=n+2\ell$. Let $\{\mu_l[A,\Phi]\}_{l\ge1}$ denote the eigenvalues of the Laplacian $d^1_{A,\Phi}d^{1,*}_{A,\Phi}$ … in ascending order. Then
> $$\mu_l[A,\Phi]\le C(-\log\lambda)^{-3/2}\ (l=1,\dots,N),\qquad \mu_{N+1}[A,\Phi]\le K+C(-\log\lambda)^{-3/4},$$
> $$\mu_l[A,\Phi]\ge K-C(-\log\lambda)^{-3/4}\ (l\ge N+1),$$
> where $K=\min\{\nu_2[A_0,\Phi_0],\nu_2[A_1],\dots,\nu_2[A_m]\}$.

**Hypotheses** (Definition 8.1, `defn:LambdaClosePair`):
- $(A,\Phi)$ is $L^2_{1}$-close to $(A_0,\Phi_0)$ off small balls around $\mathbf x$, carries curvature mass $\approx8\pi^2\kappa_p$ on the ball around $x_p$, and has $\|F_A^{+}\|_{L^2(B_p)}$ small and $\|\Phi\|_{L^\infty}\le C$.
- $\Phi=0$ on the balls $B_p$.
- $C$ and $\lambda_0$ depend on $g$, $\|F_{A_0}\|$, $\|\Phi_0\|$, $\nu_2[A_0,\Phi_0]$, $\nu_2[A_0,\Phi_0]^{-1}$, $\dim\mathrm{Ker}\,d^{1,*}_{A_0,\Phi_0}$ and $\ell$. Here $\nu_2$ is the least positive eigenvalue.

Corollary 8.4 states the limiting version along Uhlenbeck-convergent sequences.

**Role.** This identifies the obstruction space of FL3 near an ideal pair. Its dimension is the background cokernel ($n$) plus a contribution $2\kappa_p$ from the cokernel of the coupled Dirac operator on each sphere, $2\ell$ in total. The dependence of the constants on $\nu_2[A_0,\Phi_0]^{-1}$ is exactly why uniformity fails when the background moves in a positive-dimensional family with spectral flow.

---

## 5. FL2a, Theorems 3.19 (`thm:DefnOfStabilizeBundle`) and 3.21 (`thm:ThickenedModuliSpace`): reducibles in the top level (proved)

**Theorem 3.19:**

> Assume that the moduli space $M_{\mathfrak s}$ contains no zero-section pairs. Then there is an open neighborhood $\mathcal U$ of the subspace $\iota(M_{\mathfrak s})$ in $\mathcal C_{\mathfrak t}$, which does not contain any zero-section pairs or other reducibles, and a finite-rank, smooth, trivial, vector subbundle $\Xi\to\mathcal U$ of $\mathfrak V\to\mathcal U$, which is $S^1$ equivariant …, such that the following hold:
> 1. The restriction of $\Xi$ to $\iota(M_{\mathfrak s})$ is a complex vector bundle.
> 2. The smooth bundle map $\Pi_{\Xi^\perp}:\mathfrak V\to\Xi^\perp$ defined by the fiberwise $L^2$-orthogonal projection … restricts to a surjective fiber map $\Pi_{\Xi^\perp}:\mathrm{Ran}(D\mathfrak S)_{A,\Phi}\to\Xi^\perp_{A,\Phi}$ for any point $[A,\Phi]\in\mathcal U$.
> 3. If $(A,\Phi)$ is an $L^2_\ell$ representative of a point in $\mathcal U$, for some integer $k\le\ell\le\infty$, then the fiber $\Xi_{A,\Phi}$ is contained in $L^2_\ell(\Lambda^+\otimes\mathfrak g_{\mathfrak t})\oplus L^2_\ell(V^-)$.

**Theorem 3.21:**

> Suppose that the spin$^u$ structure $\mathfrak t$ admits a reduction $\mathfrak t=\mathfrak s\oplus\mathfrak s\otimes L$. Assume $M_{\mathfrak s}$ contains no zero-section pairs. Then the following hold:
> 1. There is an $S^1$-invariant, open neighborhood $\mathcal U$ of $\iota(M_{\mathfrak s})$ in $\mathcal C_{\mathfrak t}$ such that the zero locus $\mathcal U\cap\mathcal M_{\mathfrak t}(\Xi,\mathfrak s)$ is regular and so a manifold of dimension $\dim\mathcal M_{\mathfrak t}+\mathrm{rank}_{\mathbb R}\Xi$.
> 2. The space $M_{\mathfrak s}$ is a smooth, $S^1$-invariant submanifold of $\mathcal M_{\mathfrak t}(\Xi,\mathfrak s)$.
> 3. The bundle $N_{\mathfrak t}(\Xi,\mathfrak s)$ is a normal bundle for the submanifold $\iota:M_{\mathfrak s}\hookrightarrow\mathcal M_{\mathfrak t}(\Xi,\mathfrak s)$ and the tubular map is equivariant with respect to the circle action on $N_{\mathfrak t}(\Xi,\mathfrak s)$ given by the trivial action on the base $M_{\mathfrak s}$ and complex multiplication on the fibers, and the circle action on $\mathcal M_{\mathfrak t}(\Xi,\mathfrak s)$ ….
> 4. The restriction of the section $\mathfrak S$ to $\mathcal M_{\mathfrak t}(\Xi,\mathfrak s)$ takes values in $\Xi$ and vanishes transversely on $\mathcal M_{\mathfrak t}(\Xi,\mathfrak s)-\iota(M_{\mathfrak s})$.

**Notation.**
- $\mathcal M_{\mathfrak t}(\Xi,\mathfrak s)=(\Pi_{\Xi^\perp}\mathfrak S)^{-1}(0)$ is the thickened moduli space (Definition 3.20).
- $N_{\mathfrak t}(\Xi,\mathfrak s)=\mathrm{Ker}(\Pi_{\Xi^\perp}\mathbf D^n)$ has fibres $\mathrm{Ker}(d^{0,n,*}_{A,\Phi}+\Pi_{\Xi^\perp}d^{1,n}_{A,\Phi})$.
- The Memoir (§2.3, eqs. `eq:VirtualNormalandObstBundles`, `eq:BackgroundConfigEmbedding`, `eq:HomeoSWEmbedding`) restates the consequence. There are $\boldsymbol\gamma_{\mathfrak s}:N_{\mathfrak t,\mathfrak s}(\varepsilon)\hookrightarrow\mathcal C_{\mathfrak t}$ and $\boldsymbol\chi_{\mathfrak s}$ such that $\boldsymbol\gamma_{\mathfrak s}:\boldsymbol\chi_{\mathfrak s}^{-1}(0)\cap N_{\mathfrak t,\mathfrak s}(\varepsilon)\cong\mathcal M_{\mathfrak t}\cap\boldsymbol\gamma_{\mathfrak s}(N_{\mathfrak t,\mathfrak s}(\varepsilon))$, "citing [FL2a, Theorem 3.21]".

**Role.** This is a complete Kuranishi model at a reducible stratum, but only in the top level: no bubbling. It uses a stabilizing bundle $\Xi$ chosen to be of constant rank along $M_{\mathfrak s}$ rather than a spectral cut-off, so it is insensitive to spectral flow. It provides the "background" factor $N_{\mathfrak t(\ell),\mathfrak s}$ of all later lower-level gluing data. Within these sources, this is the only gluing-type statement at reducible strata that is proved in full.

---

## 6. FLLevelOne, Theorem 3.8 (`thm:GluingThm`): level one, attributed to FL3 and FL4

**Statement** (§3, cited as "[FL3, FL4]"):

> For small enough positive $\varepsilon$ and $\delta$, there is a topological embedding,
> $$\boldsymbol\gamma:\bar{\mathcal M}^{\rm stab}_{\mathfrak t',\mathfrak s}\to\bar{\mathcal C}_{\mathfrak t'}=\mathcal C_{\mathfrak t'}\sqcup(\mathcal C_{\mathfrak t}-M_{\mathfrak s})\times X\sqcup M_{\mathfrak s}\times X,$$
> restricting to a smooth embedding of the top stratum … into $\mathcal C^{*,0}_{\mathfrak t'}$, the smooth embedding $\boldsymbol\gamma_{\mathfrak t,\mathfrak s}\times\mathrm{id}_X$ of the middle stratum into $\mathcal C^{*,0}_{\mathfrak t}\times X$, and the identity map on the lowest stratum, $M_{\mathfrak s}\times X\subset\mathcal C^0_{\mathfrak t}\times X$. There is a smooth, circle-equivariant section $\boldsymbol\chi_i$ of the instanton obstruction bundle $\Upsilon^i_{\mathfrak t',\mathfrak s}\to\mathcal M^{\rm stab}_{\mathfrak t',\mathfrak s}$, and a continuous, circle-equivariant section $\boldsymbol\chi_s$ of the background obstruction bundle $\bar\Upsilon^s_{\mathfrak t',\mathfrak s}\to\bar{\mathcal M}^{\rm stab}_{\mathfrak t',\mathfrak s}$, which is smooth when restricted to each stratum …, such that, if $\boldsymbol\chi=\boldsymbol\chi_s\oplus\boldsymbol\chi_i$, then
> $$\boldsymbol\gamma(\mathcal M^{\rm stab}_{\mathfrak t',\mathfrak s}\cap\boldsymbol\chi^{-1}(0))=\boldsymbol\gamma(\mathcal M^{\rm stab}_{\mathfrak t',\mathfrak s})\cap\mathcal M_{\mathfrak t'},$$
> and
> $$\boldsymbol\gamma\big(((N_{\mathfrak t,\mathfrak s}(\varepsilon)-M_{\mathfrak s})\times X)\cap\boldsymbol\chi_s^{-1}(0)\big)=\boldsymbol\gamma((N_{\mathfrak t,\mathfrak s}(\varepsilon)-M_{\mathfrak s})\times X)\cap\bar{\mathcal M}_{\mathfrak t'}.$$
> The sections $\boldsymbol\chi_s\oplus\boldsymbol\chi_i$ and $\boldsymbol\chi_s$ … vanish transversely.

**Notation.** In this paper $\mathfrak t'$ is the spin$^u$ structure of the cobordism, and $M_{\mathfrak s}\subset\mathcal M_{\mathfrak t}$ with $\mathfrak t=\mathfrak t'(1)$. $\bar{\mathcal M}^{\rm stab}_{\mathfrak t',\mathfrak s}$ is the gluing-data space over $N_{\mathfrak t,\mathfrak s}(\varepsilon)\times X$, stratified as (top) $\sqcup$ $(N_{\mathfrak t,\mathfrak s}(\varepsilon)-M_{\mathfrak s})\times X$ $\sqcup$ $M_{\mathfrak s}\times X$. The paper adds: "We shall formally extend the section $\boldsymbol\chi_i$ over the lower strata … by setting it equal to zero …; we make no assumptions about the continuity or transversality of this formal extension".

**Status.** The theorem is attributed to [FL3, FL4], and FL4 is "in preparation". The paper also says (§1): "At the time of writing, work on [FL4] and [FL5] is still in progress, though we believe we have surmounted most of the difficult technicalities." FL3 proves only the existence part (Section 2), so the embedding, the identification of $\boldsymbol\chi^{-1}(0)$ with the moduli space, and the transversality asserted here rest on FL4. Theorem 6.1 (`thm:LevelOne`, the level-one link pairing) uses Theorem 3.8 throughout (see the references at the definition of the link and in §§5–6).

[added by checker] **What the printed statement does not say.**
- Theorem 3.8 identifies $\boldsymbol\gamma(\boldsymbol\chi^{-1}(0))$ only with the part of $\mathcal M_{\mathfrak t'}$ (resp. $\bar{\mathcal M}_{\mathfrak t'}$) lying *inside the image* of $\boldsymbol\gamma$.
- It does not assert that this image is an open neighbourhood of $M_{\mathfrak s}\times X$ in $\bar{\mathcal C}_{\mathfrak t'}$, i.e. that every point of $\bar{\mathcal M}_{\mathfrak t'}$ Uhlenbeck-close to $M_{\mathfrak s}\times X$ lies in it. This is the surjectivity property (3) of FL3 §1.5.1.
- The paper nevertheless uses the theorem in that sense:
  - §3 introduction: Theorem 3.8 "asserts that the splicing map can be perturbed to a gluing map, thus giving a topological model for an open neighborhood of the stratum".
  - §5: "The fact that $\boldsymbol\gamma$ is a homeomorphism from $\bar{\mathcal M}^{\rm stab}_{\mathfrak t',\mathfrak s}$ into $\bar{\mathcal C}_{\mathfrak t'}$ ensures that the image of $\boldsymbol\gamma$ contains an open neighborhood of $\bar{\mathcal V}(z)\cap\bar{\mathcal W}\cap\bar{\mathbf L}_{\mathfrak t',\mathfrak s}$ in $\bar{\mathcal M}_{\mathfrak t'}$".

**Role.** This is the first lower-level case. There is a single stratum $\Sigma=X$, so no overlap problem arises. The overlap paper (§4) states: "When $\ell=1$, Theorem 3.1 is all we need".

[added by checker] FLLevelOne §1.7.2 ("Higher levels and comparison with the Kotschick-Morgan conjecture") makes a related remark about the anti-self-dual (Kotschick–Morgan) setting. The global gluing-data space is patched from the stratumwise spaces by transition maps obeying a cocycle condition; "the case $\ell=1$ is simplest, as no transition map is needed, while if $\ell=2$ the transition map does not need to satisfy a cocycle condition: the real problem of constructing $\bar{\mathrm{Gl}}_{\xi,\ell}(\delta)$ arises when $\ell\ge3$". It adds that "the construction of the space of global gluing data and the global gluing map — in a form suitable for our purposes — is a difficult analytical and topological problem". The same section states the general-$\ell$ link pairing as a conjecture (Conjecture 1.6 there, `conj:PTConjecture`; numbering by counter), with $\dim M_{\mathfrak s}=0$, and says its proof is "work in progress [FL5]".

---

## 7. The overlap paper (1211.0480)

### 7.1 What the overlap problem is

From §1:

> For $\ell>1$, the link $\mathbf L_{\mathfrak t,\mathfrak s}$ is the intersection of the zero-locus of an obstruction bundle with the boundary of a *union* of cone bundles. … A more profound difficulty is that, as in all Mayer-Vietoris arguments, if one wants to compute the cohomology of a union, one must understand the intersection of the elements of that union. We refer to this problem as the *overlap problem*.

From §4:

> For $\ell>1$, we cannot use Theorem 3.1 … because more than one gluing map is necessary to cover a neighborhood of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$. … The difficulty in understanding these overlaps arises largely from the definition of the gluing perturbation $\mathfrak p$. That is, while the splicing map $\boldsymbol\gamma'_\Sigma$ is quite explicit, the gluing perturbation $\mathfrak p$ arises from an implicit function theorem argument and is thus not sufficiently explicit for us to compute $\boldsymbol\gamma^{-1}_\Sigma\circ\boldsymbol\gamma_{\Sigma'}$.

The proposed solution is "to show that images of the *splicing maps*, rather than the images of the gluing maps, satisfy the conditions of Definition 1.2". This is done by deforming the fibre (the spliced-ends moduli space) and the splicing maps (local flattening of $g$ and $A_0$ near the splicing points), so that overlaps are governed by push-out diagrams.

### 7.2 Definition 1.2 (`defn:LocalConeBundles`)

> A subspace $S$ of a stratified space $Y$ has *smooth, local cone bundle neighborhoods* if the following holds. For each stratum $S_i$, there are
> - A neighborhood $\mathcal O_i$ of $S_i$ in $Y$ with $\mathcal O_i\cap\mathcal O_j$ non-empty if and only if $i<j$ or $j<i$,
> - A fiber bundle $\pi_i:N_i\to S_i$ with fiber $F_i$, a cone, wherein we identify $S_i$ with the section of $\pi_i$ given by the cone point,
> - A homeomorphism $\boldsymbol\gamma_i$ from a neighborhood of $S_i$ in $N_i$ with $\mathcal O_i$.
>
> Let $t_i:\mathcal O_i\to[0,\infty)$ be the function defined by the composition of $\boldsymbol\gamma_i^{-1}$ and the cone parameter on $N_i$. … These maps satisfy the *Thom-Mather control conditions* if
> - The map $(\pi_i,t_i):\mathcal O_i\to S_i\times[0,\infty)$ is a smooth submersion on each stratum,
> - For $i<j$, on $\mathcal O_i\cap\mathcal O_j$, $\pi_i\circ\pi_j=\pi_i$ and $t_i\circ\pi_j=t_i$.
>
> We say the control data $\{(\mathcal O_i,\pi_i,t_i)\}$ has *compatible structure groups* if
> - The structure group of each bundle $\pi_i:N_i\to S_i$ is a compact Lie group $G_i$,
> - For $i<j$, the intersection $\mathcal O_i\cap\mathcal O_j$ is a $G_i$-subbundle of $N_i$ and a $G_j$-subbundle of $N_j$,
> - For $i<j$, on the intersection $\mathcal O_i\cap\mathcal O_j$, the level sets $t_j^{-1}(\varepsilon)$ are $G_i$-subbundles.

The link is $\mathbf L=\partial(\cup_i\mathcal O_i)$. It is decomposed as $\mathbf L_i=\boldsymbol\gamma_i(t_i^{-1}(\varepsilon_i))-\cup_{j\ne i}\boldsymbol\gamma_j(t_j^{-1}[0,\varepsilon_j))$, and pairings are computed by push-forward along $\pi_i$ (eq. `eq:Decomposition`).

The paper also defines a *virtual cone bundle neighborhood* (§1.2, unnumbered): a cone bundle $\mathbf{Gl}(\mathfrak t,\mathfrak s,\Sigma)\to M_{\mathfrak s}\times\Sigma$, an obstruction section $\mathfrak o_\Sigma$ of a pseudo-vector bundle $\Upsilon_{\mathfrak t,\mathfrak s}$, and "a homeomorphism between $\mathfrak o_\Sigma^{-1}(0)$ and a neighborhood of $M_{\mathfrak s}\times\Sigma$ in $\bar{\mathcal M}_{\mathfrak t}/S^1$". It asserts: "The gluing theorems of [FL3] … provide a virtual cone bundle neighborhood".

### 7.3 Theorem 3.1 (`thm:GluingThm`)

Set-up (§3.1). The background pair lies in $\boldsymbol\gamma_{\mathfrak s}(N_{\mathfrak t(\ell),\mathfrak s})$ (FL2a). The fibre is $\prod_i\bar M^{s,\diamond}_{\kappa_i}(S^4)$, "the Uhlenbeck compactification of the moduli space of framed, mass-centered, sufficiently concentrated, anti-self-dual connections". There is a stabilizing bundle $\Upsilon_\Sigma\to\mathbf{Gl}(\mathfrak t,\mathfrak s,\Sigma)$ and a gluing perturbation $\mathfrak p_\Sigma$ with $\mathfrak S((A',\Phi')+\mathfrak p_\Sigma(A',\Phi'))\in\Upsilon_\Sigma|_{(A',\Phi')}$. The gluing map is $\boldsymbol\gamma_\Sigma=\boldsymbol\gamma'_\Sigma+\mathfrak p\circ\boldsymbol\gamma'_\Sigma$, and $\mathfrak o_\Sigma=\mathfrak S\circ\boldsymbol\gamma_\Sigma$. Then: "The construction of the map $\mathfrak p$ appears in [FL3] and it follows that"

> **Theorem 3.1.** The restriction of the gluing map $\boldsymbol\gamma_\Sigma$ to the zero-locus of the obstruction map, $\mathfrak o_\Sigma^{-1}(0)$, parameterizes a neighborhood of $M_{\mathfrak s}\times\Sigma$ in $\bar{\mathcal M}_{\mathfrak t}$.

**Status.** No proof is given. The statement asserts more than FL3 Theorem 1.1, in three ways:
1. It asserts parameterization, which needs the embedding and surjectivity properties that FL3 §1.5.1 assigns to FL4.
2. Its fibre includes ideal instantons on $S^4$, which FL3's fibre $\mathbf Z(\Sigma)$ does not.
3. It is stated for backgrounds in the whole Seiberg–Witten virtual neighbourhood, with no spectral-gap proviso.

**Role.** In the overlap paper this is the local input for each stratum.

### 7.4 Theorem 4.1 (`thm:ConesControlled`)

> The space $\mathbf{Gl}(\mathfrak t,\mathfrak s,X)$ is a union of local cone bundle neighborhoods which satisfy the conditions of Definition 1.2.

Here $\mathbf{Gl}(\mathfrak t,\mathfrak s,X)=\cup_\Sigma\boldsymbol\gamma''_\Sigma(\mathbf{Gl}(\mathfrak t,\mathfrak s,\Sigma))$ (eq. `eq:GlobalSplicingData`) is the union of the images of the deformed ("crude") splicing maps. The domains use the spliced-ends moduli spaces $\bar M^{s,\diamond}_{spl,\kappa}(S^4)$ as fibres.

**Status.** It is introduced with "from this control, one can see that". The paper is an exposition of FL5 (the Memoir). The argument is a sketch here and is carried out in the Memoir (Section 8.3 below).

**Role.** This is the solution of the overlap problem at the level of splicing maps, which are explicit. It is a statement about the *domain* of a global gluing map, not about solutions.

### 7.5 Theorem 4.2 (`thm:ExtendedGluingThm`): the assumed global gluing theorem

> There is a section $\mathfrak o$ of a pseudo-vector bundle $\Upsilon\to\mathbf{Gl}(\mathfrak t,\mathfrak s,X)$ and a stratum-preserving deformation of the inclusion $\mathbf{Gl}(\mathfrak t,\mathfrak s,X)\to\bar{\mathcal C}_{\mathfrak t}/S^1$ such that the restriction of this deformation to $\mathfrak o^{-1}(0)$ parameterizes a neighborhood of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in $\bar{\mathcal M}_{\mathfrak t}/S^1$. In addition, the restriction of the obstruction section $\mathfrak o$ to any stratum vanishes transversely.

**Status: not proved.** It is introduced by "In [FL4], we will extend the results of [FL3] constructing a gluing perturbation of the image of these splicing maps to parameterize a neighborhood of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in $\bar{\mathcal M}_{\mathfrak t}/S^1$, giving the following technical result on which the proofs of Theorem 2.1 and Theorem 1.1 rely". §1 says the proof "should be a routine extension of the results of [FL3], and … will appear in [FL4]". The environment is `thm` although the result is announced, not proved.

### 7.6 Theorems 2.1 (`conj:PTConj`) and 1.1 (`thm:CobordismResult`)

> **Theorem 2.1.** Assume the result of Theorem 4.2. If $b_1(X)=0$, if $\mathfrak t$ is a spin$^u$ structure on $X$ and $\mathfrak s\in\mathrm{Spin}^c(X)$ with $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)\subset I\mathcal M_{\mathfrak t}$, then
> $$\#\big(\bar{\mathcal V}(h^{\delta-2m}x^m)\cap\bar{\mathcal W}^{n-1}\cap\mathbf L_{\mathfrak t,\mathfrak s}\big)=SW_X(\mathfrak s)\sum_{i=0}^kp_{\delta,\ell,m,i}(A,B)Q_X^i(h),$$
> where $k=\min[\ell,(\delta-2m)/2]$, $A=\langle c_1(\mathfrak s)-c_1(\mathfrak t),h\rangle$, $B=\langle c_1(\mathfrak t),h\rangle$, and $p_{\delta,\ell,m,i}$ is a homogeneous polynomial of degree $\delta-2m-2i$ whose coefficients are universal functions of $\chi(X),\sigma(X),c_1(\mathfrak s)^2,c_1(\mathfrak t)^2,c_1(\mathfrak t)\cdot c_1(\mathfrak s),p_1(\mathfrak t),m,\delta,\ell$.

Theorem 1.1 is the resulting cobordism formula. Its printed statement and its omissions are recorded in `a-cobordism.md`, §7. The text says it "relies on a technical result, stated here as Theorem 4.2".

**Logical status.** Theorems 1.1 and 2.1 are conditional on Theorem 4.2. Theorem 2.1 says so explicitly; Theorem 1.1 says so in the surrounding text.

---

## 8. The Memoir (math/0203047)

### 8.1 Hypothesis 7.8.1 (`hyp:Gluing`, "Local gluing hypothesis")

Source: Chapter 7 ("Obstruction bundle"), §7.8 (`sec:GluingThm`).

> There is a continuous, $S^1$-equivariant embedding,
> $$\boldsymbol\gamma_{\mathcal M}:\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}\to\bar{\mathcal C}_{\mathfrak t},$$
> which is homotopic through $S^1$-equivariant, continuous embeddings to the global splicing map $\boldsymbol\gamma'_{\mathcal M}$, smooth on each stratum of $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}$, and equal to the identity on $N_{\mathfrak t(\ell),\mathfrak s}(\delta)\times\mathrm{Sym}^\ell(X)$. In addition, there are $S^1$-equivariant sections $\boldsymbol\chi_s$ and $\boldsymbol\chi_i$ of the pseudo-bundles $\bar\Upsilon^s_{\mathfrak t,\mathfrak s}$ and $\bar\Upsilon^i_{\mathfrak t,\mathfrak s}$ with the following properties:
> 1. The restriction of the section $\bar{\boldsymbol\chi}=\boldsymbol\chi_s\oplus\boldsymbol\chi_i$ of $\bar\Upsilon^s_{\mathfrak t,\mathfrak s}\oplus\bar\Upsilon^i_{\mathfrak t,\mathfrak s}$ to each stratum is smooth.
> 2. The restriction of the section $\bar{\boldsymbol\chi}$ to each stratum of $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}$ vanishes transversely.
> 3. If we pull back the fiber metric (`eq:L2FiberNorm`) to $\bar\Upsilon^s_{\mathfrak t,\mathfrak s}\oplus\bar\Upsilon^i_{\mathfrak t,\mathfrak s}$ by the splicing embeddings $\varphi'_s\oplus\varphi'_i$ defined in (`eq:DefineGlobalBackgroundObstrEmbedd`) and (`eq:XGlobalInstantonObstrSplicing`), then the $L^2$ norm of $\bar{\boldsymbol\chi}$ is lower semi-continuous.
> 4. The restriction of $\boldsymbol\gamma_{\mathcal M}$ to the zero-locus $\bar{\boldsymbol\chi}^{-1}(0)$ is a homeomorphism between $\bar{\boldsymbol\chi}^{-1}(0)$ and an open neighborhood of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in $\bar{\mathcal M}_{\mathfrak t}$.

**Notation.**
- $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}$ is the *space of global splicing data* (eq. `eq:DefineGlobalGluingDataSpace`):
  $$\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}=\bigsqcup_{\mathcal P}\big(\tilde N_{\mathfrak t(\ell),\mathfrak s}(\delta)\times_{\mathcal G_{\mathfrak s}}\mathcal O(\mathfrak t,\mathfrak s,\mathcal P)\big)\big/\!\sim.$$
  Here $\mathcal P$ runs over partitions of $N_\ell=\{1,\dots,\ell\}$, which index the strata of $\mathrm{Sym}^\ell(X)$, and $\mathcal O(\mathfrak t,\mathfrak s,\mathcal P)$ is the neighbourhood of Theorem 6.6.1 inside the gluing-data space $\bar{\mathrm{Gl}}(\mathfrak t,\mathfrak s,\mathcal P)$. Points are identified when their images under the crude splicing maps $\boldsymbol\gamma''_{\mathfrak t,\mathfrak s,\mathcal P}$ agree. The fibres are built from the spliced-ends moduli spaces $\bar M^{s,\natural}_{spl,\kappa}(S^4,\delta)$ of Theorem 5.1.1, which contain ideal points.
- $N_{\mathfrak t(\ell),\mathfrak s}(\delta)\to M_{\mathfrak s}$ is the $\delta$-disc bundle of the virtual normal bundle of FL2a (Section 5).
- $\boldsymbol\gamma'_{\mathcal M}$ is the global splicing map of Proposition 6.8.1 (Section 8.3).
- $\bar\Upsilon^s_{\mathfrak t,\mathfrak s}$ (eq. `eq:DefineGlobalBackgroundObstruction`) is the background obstruction bundle, patched from the FL2a stabilizing bundles $\Xi$. $\bar\Upsilon^i_{\mathfrak t,\mathfrak s}$ is the instanton obstruction pseudo-bundle, built from the cokernels of the coupled Dirac operators over $S^4$ (Theorem 7.6.1, §7.7).
- A *pseudo-bundle* (Definition 7.1.1, `defn:PseudoBundle`, after Schwartz) is a vector bundle over each stratum, together with injective bundle maps from the pull-back by a neighbourhood retraction, with left inverses.
- The fibre metric (`eq:L2FiberNorm`) is $\langle[A,\Phi,\mathbf x,\Psi_1],[A,\Phi,\mathbf x,\Psi_2]\rangle=(\Psi_1,\Psi_2)_{L^2(X)}$.

**Hypotheses.** Those of Chapter 2: $\mathfrak t$ a spin$^u$ structure, $\mathfrak s$ with $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)\subset I\mathcal M_{\mathfrak t}$, generic parameters, and $M_{\mathfrak s}$ containing no zero-section pairs. [added by checker: Hypothesis 7.8.1 lists no hypotheses of its own. These are the standing assumptions under which its objects are defined: §2.3.5 for $N_{\mathfrak t,\mathfrak s}$ and Theorem 6.6.1 for $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}$.]

**Remarks on the formulation.**
- Although called "local", the hypothesis concerns one map defined on the whole space of global splicing data. The local maps of FL3 and the overlap control of Chapter 6 are combined into it.
- The splitting it uses ($\bar\Upsilon^s\oplus\bar\Upsilon^i$: a stabilizing bundle for the background plus Dirac cokernels on the spheres) is not the Taubes small-eigenvalue splitting of FL3. §7.9 describes it as a modification of the approach of FL3.

**Where it is used.**
- *Explicitly:* Theorem 1 (`thm:MainThm`) begins "Assume Hypothesis 7.8.1 holds".
- *Implicitly:* Definition 8.1.3 (`defn:DefineLink`) defines the link of a level $\ell\ge1$ Seiberg–Witten stratum as $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}=\bar{\boldsymbol\chi}^{-1}(0)\cap\bar{\mathbf L}^{\rm vir}_{\mathfrak t,\mathfrak s}$, "where $\bar{\boldsymbol\chi}$ is the obstruction section in Hypothesis 7.8.1".
- *Consequently,* Theorem 8.1.9 (`thm:CobordismThm`), Theorems 10.1.1 (`thm:LinkPairing`) and 10.1.2 (`thm:Multiplicity`), Proposition 10.6.1 and Lemma 10.6.2 depend on it whenever $\ell\ge1$, although their statements do not mention it. See `a-cobordism.md`, §§3–6.
- *The authors' description:*
  - Abstract: "we prove — modulo a gluing theorem which is an extension of our earlier work in [FL3] — that these intersection pairings can be expressed in terms of topological data and Seiberg–Witten invariants".
  - Introduction: "we reduce the computation to a *local gluing theorem* which extends that of [FL3], stated here as Hypothesis 7.8.1".
  - §7.1: "state the properties of a gluing map (to be proved in the forthcoming [Feehan_Leness_monopolegluingbook])".
  - §6.8: "The analytical underpinnings required to replace Hypothesis 7.8.1 by a theorem that yields its assertions will be provided in the forthcoming [Feehan_Leness_monopolegluingbook]".
  - [added by checker] §7.8, after the statement: "We give proofs of the properties of the gluing map $\boldsymbol\gamma_{\mathcal M}$ and obstruction section $\boldsymbol\chi$ asserted by Hypothesis 7.8.1 in [Feehan_Leness_monopolegluingbook]".
  - [added by checker] §7.9, first sentence: "The purpose of this section is to summarize the justification of Hypothesis 7.8.1 as a theorem, whose proof is provided by the authors in [Feehan_Leness_monopolegluingbook]".
  - These are the strongest status claims in the Memoir, and both are in the present tense. The book they cite is listed in the bibliography as "in preparation". Within the sources, Hypothesis 7.8.1 therefore remains an assumption.

**Role.** This is the exact analytic input on which the cobordism formula is conditional. It is what one would need to know about gluing $SO(3)$ monopoles at the reducible strata $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ for all $\ell\ge1$ simultaneously.

### 8.2 The authors' account of what Hypothesis 7.8.1 requires beyond FL3 (§7.8 after the statement, and §7.9)

Paraphrase of §7.8, with quotations:
- FL3 shows that a solution map exists at each spliced pair. It uses FL3 Proposition 5.5 and FL3 §9.1. "Our proof of existence of the solution map in [FL3] should extend to yield the desired gluing map, $\boldsymbol\gamma_{\mathcal M}$, in Hypothesis 7.8.1 and identify the zero locus of the obstruction section, $\bar{\boldsymbol\chi}$, with an open neighborhood in $\bar{\mathcal M}_{\mathfrak t}$."
- Item 1 (smoothness) "follow[s] by the construction of the gluing map".
- Item 2 (transversality) "follows from a formal argument and the result in [FeehanGenericMetric]".
- Item 3 (lower semicontinuity) is to come from Uhlenbeck continuity: "We expect that the continuity of the gluing map with respect to Uhlenbeck limits will follow along lines similar to the proof of the same property for the gluing map for anti-self-dual SO(3) connections given in [FLKM1]."
- "One must also show the map is injective and surjective where by the latter we mean Property (4)". "In special cases", these properties for anti-self-dual connections are in [DK, §§7.2.5–7.2.6] and Taubes.

§7.9 ("Notes on the justification of the local gluing hypothesis"), first paragraph:

> In [FL3], we had restricted our attention to the case of gluing anti-self-dual connections over $S^4$ and SO(3) monopoles over $X$ that varied in an open neighborhood with the property that spectral flow for the Laplace operator, $d^1_{A,\Phi}d^{1,*}_{A,\Phi}$, is small. This assumption is valid, for example, when considering small open neighborhoods of a *zero*-dimensional moduli space of Seiberg–Witten monopoles … However, in this monograph and our previous articles such as [FL2a] (where no bubbling is allowed) or [FLLevelOne] (where one bubble allowed), we must allow for moduli spaces of Seiberg–Witten moduli spaces that are *positive*-dimensional. In those cases, we cannot assume that spectral flow for $d^1_{A,\Phi}d^{1,*}_{A,\Phi}$ is small and thus our method of gluing [FL3] does not apply without significant modification. [added by checker: the paragraph continues: "Indeed, the rank of the obstruction vector bundle constructed in [FL3], by an analogue of the small-eigenvalue decomposition that Taubes developed in [TauIndef], necessarily jumps as eigenvalues of $d^1_{A,\Phi}d^{1,*}_{A,\Phi}$ cross the small-eigenvalue cut-off parameter $\mu\in(0,1]$ …".]

§7.9.4 (`subsec:Virtual_neighborhood_moduli_space_SO3_monopoles_lower_level`):

> The gluing theory described in Section 7.9.3 for solutions to the anti-self-dual equation generalizes *formally* to the case of the SO(3)-monopole equations. However, the analysis required to prove that the gluing map $\boldsymbol\gamma_{\mathcal M}$ and obstruction map $\bar{\boldsymbol\chi}$ have all the properties asserted by Hypothesis 7.8.1 is considerable and the details of that analysis do *not* extend in a straightforward manner from those previously encountered in the case of the anti-self-dual equation … We summarized the principal new analytical difficulties in our article [FL3] and address them fully in [Feehan_Leness_monopolegluingbook].

The outlined replacement uses an extrinsic splitting in the manner of Donaldson–Kronheimer. Over $X$, $\Xi=\Xi_1\oplus\Xi_2$, with $\Xi_1$ the FL2a stabilizing bundle and $\Xi_2=\mathrm{Coker}\,\mathbf D$ the Dirac cokernel bundle over the $S^4$ moduli space. Its complex rank is $c_2(E)$, using FL3 Lemma 8.12: on $S^4$, $\mathrm{Ker}\,D_A=0$ and the least positive eigenvalue of $D_AD_A^*$ is $3$. §7.9.3 states the ASD analogue for one connected sum $X_1\#X_2$, citing [DK, Theorems 7.2.62 and 7.2.63]. It says the extension to multiple and tree connected sums is in [DK, Ch. 8], [FL3], [FeehanGeometry], [Peng], [TauFrame]. No proof for SO(3) monopoles is given in the Memoir. [added by checker: §7.9.4 ends by noting that, for trees whose summands other than $(X,g)$ are all round $S^4$'s, "we may use the Taubes small-eigenvalue decomposition to construct obstruction bundles corresponding to connected sums of copies of $(S^4,g_{\rm round})$ since there is no spectral flow for the Dirac Laplacians, $D_AD_A^*$, over $(S^4,g_{\rm round})$". So the proposed splitting is extrinsic (as in FL2a) on the background and spectral on the bubbles. Note also that the anti-self-dual model in §7.9.3 is phrased for a connected sum along a small neck, with a metric on $X_1\#X_2$ that agrees with $g_i$ outside the neck. This differs from FL3's fixed-metric splicing.]

### 8.3 What the Memoir proves unconditionally: the overlap problem for splicing maps

All of the following are stated in the Memoir without Hypothesis 7.8.1. They concern spliced, approximate pairs only. [corrected by checker: the original said "proved". Most have proofs in the Memoir, but Proposition 6.8.1 is stated with no proof environment (see below). Several items also take as given that FL3's standard splicing maps are smoothly-stratified embeddings. FL3 §3.2 called this "a fairly straightforward consequence of the definitions" but deferred its proof to FL4.]

- **Theorem 5.1.1** (`thm:ExistenceOfSplicedEndsModuli`): existence of the instanton moduli space with spliced ends, $\bar M^{s,\natural}_{spl,\kappa}(S^4,\delta)\subset\bar{\mathcal B}^s_\kappa(S^4,2\delta)$. It is closed under $SO(3)\times SO(4)$ and has four properties:
  1. A smoothly-stratified equivariant homeomorphism $\bar M^{s,\natural}_{spl,\kappa}(S^4,\delta)\cong\bar M^{s,\natural}_\kappa(S^4,\delta)$, equal to the identity on the levels $[\Theta]\times\mathrm{Sym}^{\kappa,\natural}_\delta(\mathbb R^4)$.
  2. Agreement with $\bar M^{s,\natural}_\kappa$ off an Uhlenbeck neighbourhood $W_\kappa$ of the punctured centred symmetric product.
  3. Near each product-connection stratum $[\Theta]\times\Sigma$, equality with the image of the splicing map $\boldsymbol\gamma'_{\Theta,\mathcal P}$.
  4. The bound $\|F_A^+\|_{L^{\sharp,2}(S^4)}\le C\delta$.

  *Caveat.* The construction (§5.8, Lemma 5.8.1 `lem:SplicedEndIsotopy`, and Proposition 5.6.1 `prop:ExistenceOfSplicedEnd`) uses the anti-self-dual gluing map on $S^4$ of [FLKM1, Proposition 7.6]. FLKM1 is not among the sources. The chapter introduction states that this gluing map "is a smoothly stratified embedding [Feehan_Leness_monopolegluingbook]". So the anti-self-dual part of the construction also leans on the book in preparation, at least for the embedding property.
- **Theorem 6.6.1** (`thm:GlobalSplicingDataOverlaps`): for every partition $\mathcal P$ there is a neighbourhood $\mathcal O(\mathfrak t,\mathfrak s,\mathcal P)$ of the product-connection stratum $\Sigma(\mathfrak t,\mathfrak s,\mathcal P)$ in the gluing-data space $\bar{\mathrm{Gl}}(\mathfrak t,\mathfrak s,\mathcal P)$ such that the following hold.
  - The images of the crude splicing maps $\boldsymbol\gamma''$ for $\mathcal P$ and $\mathcal P'$ are disjoint unless $\mathcal P<\mathcal P'$ or $\mathcal P'<\mathcal P$.
  - If $[\mathcal P<\mathcal P']$ is non-empty, the intersection is *contained in* the image of the overlap data under $\boldsymbol\gamma''_{\mathcal P}\circ\rho^d$, which equals its image under $\boldsymbol\gamma''_{[\mathcal P<\mathcal P']}\circ\rho^u$. [corrected by checker: the original said the intersection "is" this image; the theorem says "is contained in". The disjointness condition is stated as emptiness of the sets of conjugate refinements $[\mathcal P<\mathcal P']$ and $[\mathcal P'<\mathcal P]$.]
  - The images for $\mathcal P'=\sigma(\mathcal P)$ coincide.
- **Lemma 6.6.4** (`lem:StatifiedSpaceStr`): $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}$ is a smoothly-stratified space, and $(\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s},\Sigma)$ is an NDR pair, where $\Sigma$ is the complement of the top stratum.
- **Corollary 6.6.5** (`cor:GlobalFibration`): $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}$ admits an $S^1$-equivariant fibration over $N_{\mathfrak t(\ell),\mathfrak s}(\delta)$ (eq. `eq:GlobalProjectionToN`). [added by checker: the corollary also asserts an $S^1$-equivariant embedding $\boldsymbol\gamma''_{\mathcal M}:\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}\to\bar{\mathcal C}_{\mathfrak t}$, the global crude splicing map. The proof says it "is an embedding by the definition of the equivalence relation", which takes for granted that each local crude splicing map $\boldsymbol\gamma''_{\mathfrak t,\mathfrak s,\mathcal P}$ is an embedding.]
- **Section 6.7.** Thom–Mather relations for the tubular distance functions on overlaps: Lemmas 6.7.1–6.7.6 and Corollary 6.7.7.
- **Proposition 6.8.1** (`prop:GlobalSplicingMap`): "There is a smoothly-stratified, $S^1$-equivariant embedding, $\boldsymbol\gamma'_{\mathcal M}:\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}\to\bar{\mathcal C}_{\mathfrak t}$, such that the restriction of $\boldsymbol\gamma'_{\mathcal M}$ to $N_{\mathfrak t(\ell),\mathfrak s}(\delta)\times\mathrm{Sym}^\ell(X)$ is equal to the product of the embedding $N_{\mathfrak t(\ell),\mathfrak s}(\delta)\to\mathcal C_{\mathfrak t(\ell)}$ with the identity on $\mathrm{Sym}^\ell(X)$." The text before it says "The proof of the following proposition is then technical but straightforward". [added by checker: no proof environment follows; the next line of the source begins §6.9. The preceding construction patches isotopies between $\boldsymbol\gamma''_{\mathfrak t,\mathfrak s,\mathcal P}$ and the standard splicing maps $\boldsymbol\gamma'_{\mathfrak t,\mathfrak s,\mathcal P}$ by induction over partitions, using cut-off functions $\beta_{\mathcal P}$. It asserts without proof that the standard and crude splicing maps "give smoothly-stratified embeddings" of $\bar{\mathcal U}(\mathfrak t,\mathfrak s,\mathcal P)$, and that the inductively modified isotopies are again isotopies of embeddings. Status: asserted with a sketched construction, not proved in the source.]
- **Theorem 7.6.1** (`thm:ExistenceOfSplicedEndsIndex`): an $\mathrm{Spin}^u(4)$-invariant pseudo-bundle $\bar\Upsilon^i_{spl,\kappa}\to\bar M^{s,\natural}_{spl,\kappa}(\delta)$. It is of complex rank $\kappa$ on the top stratum and compatible with splicing near product-connection strata. Off $W_\kappa$ it equals the Dirac index pseudo-bundle.

- [added by checker] **Lemma 7.6.3** (`lem:OverlapObstructionCommuting`) and **Lemma 7.7.1** (`lem:InstantonObstrCommDiagr`) make the instanton obstruction pseudo-bundles compatible with the overlap maps. They state commutative diagrams of pseudo-bundles covering the splicing overlap diagrams: over $S^4$ for partitions of $N_\kappa$, and over $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}$ for partitions of $N_\ell$. The background obstruction bundle $\bar\Upsilon^s_{\mathfrak t,\mathfrak s}$ (eq. `eq:DefineGlobalBackgroundObstruction`, §7.3) is patched from the bundles $\Xi_s(\mathfrak t,\mathcal P)$ by an analogous overlap diagram. These give the global domain *and* the global obstruction bundles on which Hypothesis 7.8.1 is formulated. They say nothing about the true obstruction section.

**Role.** These results solve the overlap problem in the sense of the overlap paper's Definition 1.2, for the explicit spliced (approximate) pairs. This holds modulo the embedding properties of splicing maps noted above [corrected by checker]. They thereby construct the domain $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}$ and the obstruction pseudo-bundles on which Hypothesis 7.8.1 is formulated. Deforming spliced pairs into true monopoles, and identifying the result with a neighbourhood in $\bar{\mathcal M}_{\mathfrak t}$, is exactly what remains hypothetical.

### 8.4 Hypothesis 11.3.5 (unlabelled): reducible anti-self-dual connections in a path of metrics

Source: Chapter 11 ("Kotschick–Morgan Conjecture"), §11.3 (`sec`: "Neighborhoods of gauge-equivalence classes of ideal reducible connections"). Here $b^+(X)=1$, $b_1(X)=0$, $g_I$ is a path of metrics, and $[A]$ is a reducible anti-self-dual connection for a splitting $\mathfrak g=\underline{\mathbb R}\oplus L$.

> There is a smoothly-stratified, continuous embedding, $\boldsymbol\gamma_L:\widetilde{\mathcal U}^w_\kappa(L)/S^1\to\bar{\mathcal B}^w_\kappa$, and a smoothly-stratified section $\boldsymbol\chi_L$ of the vector bundle $\widetilde\Xi^w_\kappa(L)/S^1\to\widetilde{\mathcal U}^w_\kappa(L)/S^1$ defined in (`eq:KoMGlobalObstructionBundle`) with the following properties:
> 1. The restriction of $\boldsymbol\gamma_L$ to $[A]\times\mathrm{Sym}^\ell(X)$ is the identity map.
> 2. There is a homotopy, through smoothly-stratified embeddings, between $\boldsymbol\gamma'_L$ and $\boldsymbol\gamma_L$.
> 3. The image $\boldsymbol\gamma_L(\boldsymbol\chi_L^{-1}(0))$ is an open neighborhood of $[A]\times\mathrm{Sym}^\ell(X)$ in $\bar M^w_\kappa(g_I)$.
> 4. The restriction of the section $\boldsymbol\chi_L$ to each stratum of $\mathcal U^{w,*}_\kappa(L)/S^1$ vanishes transversely.

**Status.** The chapter opens: "the proof of the Kotschick–Morgan Conjecture … can be reduced to the proof of a gluing theorem analogous to Hypothesis 7.8.1". Theorem 11.6.1 (unlabelled) reads "Conjecture 11.2.1 is true" with no explicit proviso. Its proof, however, uses the neighbourhood $\bar U^w_\kappa(L)=\boldsymbol\gamma_L(\boldsymbol\chi_L^{-1}(0)\cap\widetilde{\mathcal U}^w_\kappa(L)/S^1)$ (eq. `eq:DefineNghOfReduciblesInParamModuli`), which is defined through Hypothesis 11.3.5.

**Role.** This is the only place in the sources where FL treat gluing at *zero-section* (anti-self-dual) reducibles in a lower level, here in a one-parameter family of metrics. It is conditional in exactly the same way as Hypothesis 7.8.1.

[added by checker] **Discrepancy with the overlap paper.** The overlap paper (§1.2) treats the anti-self-dual case as known. It says that "the gluing maps of Taubes, [TauIndef, FLKM1], give the smooth, local cone bundle neighborhoods of $[A_0]\times\Sigma$ in $\bar M^w_\kappa(g_I)$". It also says that "the existence of cone bundle neighborhoods for $[A_0]\times\Sigma$ and the virtual cone bundle neighborhoods for $M_{\mathfrak s}\times\Sigma$ has been known since [TauIndef, FLKM1, FL3]". The 2018 Memoir instead *assumes* the anti-self-dual statement as Hypothesis 11.3.5, and the SO(3)-monopole statement as Hypothesis 7.8.1. The second quoted claim also exceeds what FL3 §1.5.1 says FL3 proves (Section 2).

---

## 9. FL6 (math/0609530): dependence of the Witten-conjecture results on the gluing hypothesis

**Hypothesis 3.1** (`hyp:Local_gluing_map_properties`, "Properties of local SO(3)-monopole gluing maps"):

> The local gluing map, constructed in [FL3], gives a continuous parametrization of a neighborhood of $M_{\mathfrak s}\times\Sigma$ in $\bar{\mathcal M}_{\mathfrak t}$ for each smooth stratum $\Sigma\subset\mathrm{Sym}^\ell(X)$.

Text that follows: "Hypothesis 3.1 is recorded, in greater detail, as Conjecture 6.7.1 in [FL5]. The question of how to assemble the *local* gluing maps … into a *global* gluing map … is itself difficult — involving the so-called 'overlap problem' described in [FLMcMaster] — but one which we do solve in [FL5]."

**Theorem 3.2** (`thm:Cobordism`, "SO(3)-monopole cobordism formula", cited from [FL5]). Its hypotheses:
- $X$ is a standard four-manifold (closed, connected, oriented, smooth, $b_1=0$, odd $b^+\ge3$) of Seiberg–Witten simple type.
- **"Assume that Hypothesis 3.1 holds."**
- $w-\Lambda\equiv w_2(X)\pmod2$.
- $I(\Lambda)>\delta$.
- $\delta\equiv-w^2-3\chi_h\pmod4$.
- $\delta-2m\ge0$.

The formula is recorded in `a-cobordism.md`, §5.

**Remark 3.3** (`rmk:GluingThmProperties`). [corrected by checker: the original said "in full", but citations and one sentence are elided below. The elided sentence reads: "In special cases, proofs of these properties for the local gluing maps for anti-self-dual SO(3) connections (namely, continuity with respect to Uhlenbeck limits, injectivity, and surjectivity) have been given in [DK, §7.2.5, 7.2.6], [TauSelfDual, TauIndef, TauFrame]."]

> The proof of Theorem 3.2 in [FL5] assumes the hypothesis [FL5, Conjecture 6.7.1] that the local gluing map for a neighborhood of $M_{\mathfrak s}\times\Sigma$ in $\bar{\mathcal M}_{\mathfrak t}$ gives a continuous parametrization of a neighborhood of $M_{\mathfrak s}\times\Sigma$ in $\bar{\mathcal M}_{\mathfrak t}$, for each smooth stratum $\Sigma\subset\mathrm{Sym}^\ell(X)$. These local gluing maps are the analogues for SO(3) monopoles of the local gluing maps for anti-self-dual SO(3) connections constructed by Taubes … and Donaldson and Kronheimer …. We have established the existence of local gluing maps in [FL3] and expect that a proof of the continuity for the local gluing maps with respect to Uhlenbeck limits should be similar to our proof in [FLKM1] of this property for the local gluing maps for anti-self-dual SO(3) connections. The remaining properties of local gluing maps assumed in [FL5] are that they are injective and also surjective in the sense that elements of $\bar{\mathcal M}_{\mathfrak t}$ sufficiently close (in the Uhlenbeck topology) to $M_{\mathfrak s}\times\Sigma$ are in the image of at least one of the local gluing maps. … The authors are currently developing a proof of the required properties for the local gluing maps for SO(3) monopoles. Our proof will also yield the analogous properties for the local gluing maps for anti-self-dual SO(3) connections.

**Main Theorem 1.2** (`thm:WittenSimpleType`):

> Let $X$ be a standard four-manifold with Seiberg-Witten simple type which is abundant or has $c_1^2(X)\ge\chi_h(X)-3$. Then the SO(3)-monopole cobordism formula (Theorem 3.2) implies that Conjecture 1.1 holds for $X$.

The introduction adds: "In [FL5], we proved that a formula (restated in this article in Theorem 3.2) relating Donaldson and Seiberg-Witten invariants followed from certain properties, described in Remark 3.3, of the gluing map for SO(3) monopoles constructed in [FL3]. A proof of the required SO(3)-monopole gluing-map properties is currently being developed by the authors."

**Logical status.** Main Theorem 1.2 is an implication: (Theorem 3.2) $\Rightarrow$ Witten's conjecture for $X$. Theorem 3.2 is conditional on Hypothesis 3.1. Hence Main Theorem 1.2 is conditional on Hypothesis 3.1.

**Discrepancies between FL6 and the 2018 Memoir.**
- FL6 refers to "Conjecture 6.7.1 in [FL5]"; in v4 of math/0203047 the hypothesis is Hypothesis 7.8.1. FL6 presumably cites an earlier version, which I could not check.
- FL6 Hypothesis 3.1 is *local*: one stratum $\Sigma$ at a time, continuity, injectivity and surjectivity of FL3's maps. Memoir Hypothesis 7.8.1 is *global*. It asks for one embedding of $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}$ homotopic to the global splicing map, with obstruction sections in the Memoir's pseudo-bundles, stratumwise transversality, and lower semicontinuity of $|\bar{\boldsymbol\chi}|$. FL6 says the passage from local to global (the overlap problem) is solved in FL5. The Memoir solves it for splicing maps (Section 8.3) and builds the remaining step into Hypothesis 7.8.1. So FL6's Hypothesis 3.1 is not literally the hypothesis used in the 2018 version of the proof of Theorem 3.2.

**Role.** FL6's contribution is algebraic. It determines enough of the universal coefficients of the cobordism formula, using Fintushel–Park–Stern examples and blow-up formulas. [corrected by checker: the original said "the only gauge-theoretic input is Theorem 3.2". FL6 also uses established gauge-theoretic results that do not depend on any gluing hypothesis:
- the Kronheimer–Mrowka structure theorem (FL6 Theorem 2.2, `thm:KMStructure`, citing [KMStructure, Theorem 1.7(a)]);
- independence of KM simple type from $w$ (Theorem 2.4);
- the Seiberg–Witten blow-up formula (Theorem 2.1);
- blow-up invariance of KM simple type (Proposition 2.6);
- blow-up invariance of Witten's formula (Theorem 2.7, citing Fintushel–Stern).

The only input that depends on the gluing hypothesis is Theorem 3.2.] So, as far as gluing is concerned, the analytic status of FL6 is exactly that of the Memoir's Theorem 1.

[added by checker] **Other results that FL6 and the Memoir say rest on the cobordism formula.**
- *FL6 Remark 3.4* (`rmk:PropertyP`): Kronheimer–Mrowka [KMPropertyP] use Theorem 3.2, together with [KMStructure], to prove Witten's conjecture for "a suitably restricted class of standard four-manifolds [KMPropertyP, Corollary 7] and hence prove the Property P conjecture for knots". The remark adds: "Kronheimer and Mrowka also gave a proof of Property P which did not rely on Theorem 3.2 — see [KMKnotsSuturesExcisions, Corollary 7.23]". The FL6 introduction says [KMPropertyP, Corollary 7] is "also assuming Theorem 3.2".
- *Overlap paper, §1.3*: "Kronheimer and Mrowka's proof [KMPropertyP] of Property P relies on Equation (`eq:ReducibleLink`)".
- *Memoir, §1.1*: lists as consequences of Theorem 1, and hence conditional on Hypothesis 7.8.1:
  - the superconformal simple type conjecture [FL8 = arXiv:1408.5307];
  - Witten's conjecture for all closed, oriented, smooth four-manifolds with $b_1=0$, odd $b^+>1$ and Seiberg–Witten simple type [FL7 = arXiv:1408.5085];
  - [KMPropertyP, Theorem 6];
  - Sivek's non-vanishing result for symplectic four-manifolds;
  - the multiplicity conjecture (Theorem 10.1.2).
  FL7, FL8, [KMPropertyP] and Sivek are not among the sources; their own statements of dependence were not checked. See also `a-cobordism.md`, §12.
- *FL6 introduction*: Göttsche–Nakajima–Yoshioka, building on Mochizuki's formula, "prove an explicit formula for complex projective surfaces … and from this formula deduce Witten's Conjecture". FL6 presents this as a route that does not pass through the SO(3)-monopole cobordism. It was not checked here.

---

## 10. The Banach-corners paper (1910.14580)

**Theorems 1 and 2** (`mainthm:Preimage_submanifold_under_transverse_map_and_implied_embedding`, `mainthm:Preimage_point_under_submersion_and_implied_embedding`) are abstract preimage and implicit-function theorems for $C^p$ maps of Banach manifolds *with boundary*, after Margalef Roig and Outerelo Domínguez. Theorem 1:

> Let $X$ and $X'$ be $C^p$ Banach manifolds with boundary ($p\ge1$), and $X''\subset X'$ be a neat $C^p$ Banach submanifold, and $f:X\to X'$ be a $C^p$ map, and $x_0\in f^{-1}(X'')$ be a point. If $f\pitchfork_{x_0}X''$, then there are a chart $(V,\psi,(E,\alpha))$ for $X$ with $\psi(x_0)=0$, a closed subspace $L:=d\psi(x_0)((df(x_0))^{-1}(T_{f(x_0)}X''))\subset E$ with closed complement in $E$ …, and a $C^p$ embedding $g\equiv\psi^{-1}\circ\iota_L|_{\psi(V)\cap L}$ … onto a $C^p$ submanifold $\psi^{-1}(\psi(V)\cap L)\subset X$. Moreover, $\psi^{-1}(\psi(V)\cap L)=V\cap f^{-1}(X'')$ and $T_x(f^{-1}(X''))=(df(x))^{-1}(T_{f(x)}X'')$ …. Finally, $f^{-1}(X'')\cap V$ is a neat $C^p$ Banach submanifold of $V$.

Transversality at a boundary point is required of the restriction $\partial f$ (Definition `defn:Transversality_maps_Banach_manifolds_boundary`). The remark after Theorem 1 says the extension to manifolds with corners "can be easily extended … Such extensions are required in many applications, including to the development of gluing theory for anti-self-dual connections and SO(3) monopoles over four-dimensional manifolds in [FL5, FL7, FL8]". The extension is not carried out.

**Theorem 3** (`mainthm:Gluing`, "Existence of local gluing chart near a boundary point of the moduli space of anti-self-dual connections"):

> Let $(X,g)$ denote a closed, connected, four-dimensional, oriented, smooth Riemannian manifold, $G$ denote a compact Lie group, $P_0$ denote a smooth principal $G$-bundle over $X$, and $P_1$ denote a smooth principal $G$-bundle over $S^4$. Let $A_{0\flat}$ be a smooth anti-self-dual connection over $(X,g)$ and $A_{1\flat}$ be a smooth centered anti-self-dual connection on $P_1$ over $(S^4,g_{\rm round})$. Assume further that
> $$\mathbf H^2_{A_{0\flat}}(X;\mathrm{ad}P_0)=0,\qquad \mathbf H^0_{A_{0\flat}}(X;\mathrm{ad}P_0)=0,\qquad g\text{ is conformally flat on }B_{\varrho_0}(x_{0\flat}),$$
> for some point $x_{0\flat}\in X$ and constant $\varrho_0\in(0,1]$. Then there is a constant $\delta\in(0,\varrho_0]$ with the following significance. Let $p\in(2,\infty)$ … [$\mathbf C_\delta(A_{0\flat})$ and $\mathbf C^\diamond_\delta(A_{1\flat})$ are the $W^{1,2}$-$\delta$-balls of anti-self-dual connections in Coulomb gauge, the latter also centred with scale one] … Then there is a *gluing map*,
> $$\boldsymbol\gamma:\mathbf C_\delta(A_{0\flat})\times\mathbf C^\diamond_\delta(A_{1\flat})\times\mathrm{Gl}_{x_{0\flat}}\times B_\delta(x_{0\flat})\times(0,\lambda_0)\to\mathcal A(P),\qquad \mathrm{Gl}_{x_{0\flat}}:=\mathrm{Isom}_G(P_0|_{x_{0\flat}},P_1|_s)\cong G,$$
> with the following properties:
> 1. The map $\boldsymbol\gamma$ is a $C^1$ embedding.
> 2. The image of $\boldsymbol\gamma$ is an open subset of the moduli space of anti-self-dual connections on $P$: $\mathrm{Imag}\,\boldsymbol\gamma\subset M(P,g)$.
> 3. The map $\boldsymbol\gamma$ extends to a continuous embedding of manifolds with boundary [with $(0,\lambda_0)$ replaced by $[0,\lambda_0)$] … when the codomain has the Uhlenbeck topology.
> 4. The image of $\boldsymbol\gamma$ in (`eq:Gluing_map_extended`) is an open neighborhood of the boundary portion $\mathbf C_\delta(A_{0\flat})\times\mathbf C^\diamond_\delta(A_{1\flat})\times\mathrm{Gl}_{x_{0\flat}}\times B_\delta(x_{0\flat})\times\{0\}$ in the bubble tree compactification $\widehat M(P,g)$ of $M(P,g)$.

**Corollaries 4–7:**
- *Corollary 4* (`maincor:Gluing_smooth`): $\boldsymbol\gamma$ is the restriction of a $C^1$ map of Banach manifolds with boundary, equal to the identity on the boundary face.
- *Corollary 5* (`maincor:Gluing_HA2_non-zero`): drops $\mathbf H^2_{A_{0\flat}}=0$. It adds a $C^1$ obstruction section $\boldsymbol\chi$ with values in $\mathbf H^2_{A_{0\flat}}(X;\mathrm{ad}P_0)$; $\boldsymbol\gamma(\boldsymbol\chi^{-1}(0))\subset M(P,g)$ is open; and $\boldsymbol\gamma$ is a homeomorphism from $\boldsymbol\chi^{-1}(0)$ (with $\lambda\in[0,\lambda_0)$) onto an open neighbourhood of the corresponding boundary portion in the bubble-tree compactification.
- *Corollary 6* (`maincor:Gluing_HA2_and_HA0_non-zero`): also drops $\mathbf H^0=0$, giving $\mathrm{Stab}(A_{0\flat})$-equivariance and the quotient statement.
- *Corollary 7* (`maincor:Gluing_HA2_and_HA0_non-zero_and_non-flat_metric`): also drops conformal flatness.

**What the paper does not do.**
1. *Only anti-self-dual connections.* It treats only anti-self-dual connections, not SO(3) monopoles. There is no spinor, and no cokernel of the coupled Dirac operator on $S^4$, which is the instanton obstruction $\bar\Upsilon^i$ of the Memoir. The remark on other gluing problems (§1.2) says only that the framework "should apply to more challenging gluing problems for anti-self-dual connections or SO(3) monopoles".
2. *One bubble.* It treats one bubble at one point, with $(X_1,g_1)=(S^4,g_{\rm round})$, and manifolds with boundary only. It says: "a generalization of this article to allow for more than one bubble would require us to avail of the methods and results of [Margalef-Roig–Outerelo-Domínguez] in the case of Banach manifolds with corners", and calls this generalization "purely technical". It is not carried out. Neighbourhoods of points of $\mathrm{Sym}^\ell(X)$ with $\ell\ge2$, of colliding points, or of strata of $\bar M_\kappa(S^4)$ are not treated, and neither are overlaps between strata.
3. *Bubble-tree neighbourhoods, near a single background point.* Its neighbourhoods are in the bubble-tree compactification, and the background varies in a $\delta$-ball $\mathbf C_\delta(A_{0\flat})$ about one point. Positive-dimensional families of obstructed (reducible) backgrounds with spectral flow are treated only through the local Kuranishi stabilization by $\mathbf H^2_{A_{0\flat}}$ at that point.
4. *Proofs incomplete in the source.* The arXiv source contains LaTeX comments, not visible in the compiled text, indicating that the proofs are incomplete:
   - The proof of Theorem 3 (§9) ends with "`% TODO - Complete`", followed by further TODO lines about centring and the factored codomain.
   - §12 ("Boundary points with non-trivial isotropy groups", the proof of Corollary 6) contains "`% TODO Still need to explain how we take the residual quotient to get Stab(A_0) x Stab(A_1)-equivariant gluing and obstruction maps`".
   - After the statement of Corollary 6 there is "`% TODO - Above codomain for gluing map is surely based moduli or quotient space?`".
   - The proofs of Corollaries 5 and 7 are one-paragraph reductions to Theorem 3 and to calculations in [FeehanGeometry] and Peng.

   In all, the source contains 61 lines with "TODO".

   [added by checker] The compiled text has the same gap. The proof of Theorem 3 in §9 verifies the boundary transversality hypothesis of Theorem 1 at $(A_{0\flat},A_{1\flat},\rho_0,x_{0\flat},0)$ and computes $\mathrm{Ker}\,d(\widehat F^+\circ\widehat{\mathcal S})$ there, and then ends. It gives no separate argument for:
   - item 2 (the image is open in $M(P,g)$);
   - item 3 (continuous extension in the Uhlenbeck topology);
   - item 4 (the image is a neighbourhood of the boundary portion in $\widehat M(P,g)$, i.e. surjectivity).

   Among the preamble comments is "`% TODO Do we need to consider bubble tree convergence to argue that our gluing map is surjective?`".

**Status relative to Hypothesis 7.8.1.** The paper does not claim to prove, and does not prove, any part of Memoir Hypothesis 7.8.1, FL6 Hypothesis 3.1, or overlap-paper Theorem 4.2. In the authors' own description it is a new method that "should apply" to the SO(3)-monopole case.

**Role.** It is a template for the embedding, Uhlenbeck-continuity and surjectivity properties (items 1, 3, 4 of Theorem 3), which are the properties FL3 lacks. It gives them for anti-self-dual connections with one bubble.

---

## 11. Summary of logical status

| Statement | Content | Status in the sources |
|---|---|---|
| FL2a Thms 3.19, 3.21 | Kuranishi model at a top-level reducible stratum $M_{\mathfrak s}\subset\mathcal M_{\mathfrak t}$ (no bubbles) | Proved |
| FL3 Thm 1.1 (with Thms 8.3, 9.2, 9.5) | Existence of local gluing map and obstruction section over one smooth stratum $\Sigma$, genuine $S^4$ instantons, uniform spectral gap; $\boldsymbol\gamma(\boldsymbol\chi^{-1}(0))\subset M^{*,0}(\mathfrak t)$ | Proved (the existence half). Embedding, Uhlenbeck continuity and surjectivity are explicitly not proved and are assigned to FL4 (in preparation) |
| FLLevelOne Thm 3.8 | Level-one gluing model: topological embedding and identification of $\boldsymbol\chi^{-1}(0)$ with the moduli space | Attributed to [FL3, FL4]. Only FL3's part is proved in the sources. As printed, it does not assert that the image of $\boldsymbol\gamma$ is a neighbourhood of $M_{\mathfrak s}\times X$, i.e. surjectivity, although the paper uses it in that sense [corrected by checker] |
| Overlap paper Thm 3.1 | Local gluing map parameterizes a neighbourhood of $M_{\mathfrak s}\times\Sigma$ | Stated as following from FL3, without proof. It exceeds FL3 Thm 1.1 |
| Overlap paper Thm 4.1 / Memoir Thm 6.6.1, Lemma 6.6.4, Prop. 6.8.1 | Overlap control for (crude) splicing maps; space of global splicing data; global splicing embedding | Proved in the Memoir, except Prop. 6.8.1, which is stated after a sketched construction with no written proof ("technical but straightforward") [corrected by checker]. The embedding property of the standard and crude splicing maps is used without proof (FL3 §3.2 deferred it to FL4). The spliced-ends construction (Thm 5.1.1) cites the anti-self-dual gluing of FLKM1 and, for the embedding property, the book in preparation |
| Overlap paper Thm 4.2 | Global gluing theorem with stratumwise transversality | Not proved ("will appear in [FL4]") |
| Memoir Hypothesis 7.8.1 | Global gluing embedding of $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}$, obstruction sections, transversality, lower semicontinuity, homeomorphism onto a neighbourhood of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ | Assumed. To be proved in a book "in preparation" |
| Memoir Thm 1; Thms 8.1.9, 10.1.1, 10.1.2 (for $\ell\ge1$) | Cobordism formula; cobordism sum; link pairings; multiplicity | Conditional on Hypothesis 7.8.1 (explicitly for Thm 1, through Definition 8.1.3 for the others) |
| Memoir Hypothesis 11.3.5; Thm 11.6.1 | Gluing at reducible ASD connections in a path of metrics; Kotschick–Morgan | Assumed; Thm 11.6.1 conditional on it, though stated without proviso. The overlap paper (§1.2) instead calls the anti-self-dual cone-bundle neighbourhoods known from [TauIndef, FLKM1] [added by checker] |
| FL6 Hypothesis 3.1; Thm 3.2; Main Thm 1.2 | Local gluing properties; cobordism formula; Witten's conjecture for abundant or $c_1^2\ge\chi_h-3$ | Hypothesis assumed. Thm 3.2 explicitly conditional on it. Main Thm 1.2 is the implication "Thm 3.2 $\Rightarrow$ Witten's conjecture for $X$" |
| 1910.14580 Thm 3, Cors 4–7 | Gluing chart (embedding, Uhlenbeck/bubble-tree continuity, openness) for anti-self-dual connections, one bubble | Claimed. The source has unfinished-proof comments. Does not address SO(3) monopoles, several bubbles, or overlaps |

---

## 12. Facts from these sources that bear on the comparison step

These are statements about the FL framework only. They are not claims about any other argument.

1. **Where gluing at reducibles enters the cobordism identity.**
   - The level-$0$ link of a Seiberg–Witten stratum is defined in FL2a (Definition 3.22) without any gluing hypothesis.
   - For $\ell\ge1$, the link $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$ is defined (Memoir Definition 8.1.3) through the obstruction section of Hypothesis 7.8.1.
   - Memoir §2.6, in the cobordism identity (`eq:RawCobordismSum`) that anticipates Theorem 8.1.9, takes $\bar{\mathbf L}_{\mathfrak t,\mathfrak s}$ to be empty when $\ell(\mathfrak t,\mathfrak s)<0$. [corrected by checker: the original attributed this convention to Theorem 8.1.9 as well; Theorem 8.1.9 itself sums over all $\mathfrak s$ without stating it.] When $M_{\mathfrak s}$ itself is empty, the stratum $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ is empty and has nothing to link.
   - On my reading of the text, therefore, the hypothesis is invoked only for strata $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$, with $\ell\ge1$, that are non-empty and meet $\bar{\mathcal M}_{\mathfrak t}$. The source contains no separate statement saying so.
2. **Zero-section reducibles.** In FL's closed, fixed-metric setting, zero-section reducibles never occur in $\bar{\mathcal M}_{\mathfrak t}$, by the condition on $w$ and genericity. See FL3 §2.1, and FL2a Lemma 3.2 (`lem:MorganMrowka`) and Corollary 3.3 (`cor:NoSWZeroSections`: "If $M_{\mathfrak s}\hookrightarrow\mathcal M_{\mathfrak t}$ is a Seiberg-Witten moduli subspace and $w_2(\mathfrak t)$ obeys the Morgan-Mrowka criterion …, then $M_{\mathfrak s}$ contains no zero-section solutions"). The Memoir works with "good" $w$ and blows up to arrange it. The only FL treatment of gluing at reducible anti-self-dual connections in a lower level is Memoir Chapter 11, for a path of metrics with $b^+=1$, and it is conditional on Hypothesis 11.3.5.
3. **No necks, no ends.** FL3's gluing is on a closed $X$ with fixed metric $g$, and bubbles are glued in on small balls; FL3 §9.3 explains why conformally varying metrics or long necks were avoided. None of the sources glues SO(3) monopoles on manifolds with cylindrical ends, under neck-stretching, or over multi-parameter families of metrics. [corrected by checker, as a clarification: families of metrics do appear in the sources, but not in gluing. FL1 and FL2a use parametrized moduli spaces over perturbation parameters ($\tau$, $\vartheta$ and holonomy perturbations, not metrics), for transversality only. The Memoir's crude splicing maps use locally flattened metrics $g_{\mathcal P,\mathbf x}$ that depend on the splicing points, but only inside the splicing construction; the SO(3)-monopole equations stay those of the fixed $g$. Memoir Chapter 11 uses a path of metrics $g_I$ for anti-self-dual connections only.]
4. **What would have to be supplied** by anyone who needs FL's description of neighbourhoods of non-empty strata $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ with $\ell\ge1$ (from Sections 2, 8.1, 8.2). In FL notation, at least all of the following are missing for SO(3) monopoles:
   - Uhlenbeck continuity of the gluing map up to ideal $S^4$ data and up to $\lambda=0$.
   - Injectivity and topological embedding.
   - Surjectivity onto a neighbourhood in $\bar{\mathcal M}_{\mathfrak t}$.
   - Stratumwise transversality of the obstruction section.
   - A construction valid along positive-dimensional $M_{\mathfrak s}$ with spectral flow.
   - Compatibility of the solution map with the overlap structure of $\bar{\mathcal M}^{\rm vir}_{\mathfrak t,\mathfrak s}$, i.e. a single global map homotopic to $\boldsymbol\gamma'_{\mathcal M}$.
   - [added by checker] Even at the level of approximate solutions: a proof that the standard and crude splicing maps are smoothly-stratified embeddings with irreducible, non-zero-section image (FL3 §3.2 defers this to FL4), and a written proof of Memoir Proposition 6.8.1.

   FL3 supplies only the existence of the solution map near one stratum, under a uniform spectral gap.

---

## 13. Uncertainties

1. **Numbering** is inferred from LaTeX counters in the arXiv sources, not from compiled or published versions.
   - The published Memoir, FL6 and the overlap paper may number differently. FL6 already cites "Conjecture 6.7.1 in [FL5]" for what v4 calls Hypothesis 7.8.1, so at least one earlier version of math/0203047 numbered it differently. I could not check which version FL6 means.
   - Hypothesis 11.3.5 and Theorem 11.6.1 of the Memoir have no `\label`. Their numbers rest only on the counter count.
2. **Background pairs in FL3 Theorem 1.1.** Whether reducible background pairs, i.e. points of $M_{\mathfrak s}\subset\mathcal C(\mathfrak t_\ell)$, are within the literal hypotheses cannot be decided from the statement. The statement refers to $M^{*,0}(\mathfrak t_\ell)$ and to an undefined $M(\mathfrak t_\ell,\mu)$, while the abstract and later papers apply it at Seiberg–Witten points. I have reported both.
3. **The range of $\ell$ in FL3.** The statement has $0<\ell<\lfloor\kappa\rfloor$; §3.1.2 has $1\le\ell\le\lfloor\kappa\rfloor$. I do not know which is intended.
4. **Published versions.** The overlap paper's arXiv source is dated May 7, 2005 and was posted in 2012. Whether the published Fields Institute version differs (for instance in the wording of Theorem 3.1 or 4.2) I cannot tell.
5. **Is the gluing book or FL4 available elsewhere?** No web access was used. I cannot say whether the book "Gluing maps for SO(3) monopoles and invariants of smooth four-manifolds", or FL4, has appeared since. Statements above that something is "not proved" mean not proved in the listed sources.
6. **FLKM1 was not read** (math/9812060; not among the sources). Hence:
   - I cannot say exactly what anti-self-dual gluing properties Memoir Theorem 5.1.1 imports from FLKM1 Proposition 7.6 beyond existence of the deformation. The Memoir itself cites the book in preparation for the embedding property of the anti-self-dual gluing maps on $S^4$.
   - I cannot confirm FL's claim that Uhlenbeck continuity for anti-self-dual gluing maps is proved there.
7. **The level-one paper.** FLLevelOne Theorem 3.8 is cited from "[FL3, FL4]". I have not checked whether the published 2002 version contains a proof of its embedding and surjectivity parts. In the arXiv source no such proof appears; the theorem is quoted, not proved.
8. **1910.14580.** My statement that it is incomplete rests on (i) its own scope statements and (ii) "TODO" comments in the arXiv LaTeX source. The comments are not part of the compiled text, and a later revision or the published version (if any) may differ. I counted 61 lines containing "TODO"; some of them are editorial rather than mathematical.
9. **The level-zero claim in Section 12, item 1.** The claim that the gluing hypothesis enters only through links at levels $\ell\ge1$ of non-empty strata is my reading of Definitions 8.1.3 and FL2a 3.22 and of §2.6 of the Memoir. FL do not state it as a separate result.
10. **The rank of $\Xi_\mu$ in FL3 Theorem 1.1** ("$2\ell$ plus the real codimension of $M^{*,0}(\mathfrak t)\subset M^{*,0}(\mathfrak t,\mu)$") is quoted as printed. It agrees with Theorem 8.3 only if the background cokernel dimension $n$ is identified with that codimension, which FL3 does not spell out.
