# T1. Secondary Donaldson invariants, a secondary Feehan–Leness relation, and a family adjunction inequality

Labels: **[V]** verified (computation or argument checked by me, by hand or by the scripts in `agents/T1-checks/`); **[P]** plausible; **[S]** speculative. Percentages are my confidence.
**†** marks literature cited from memory; titles, venues and theorem numbers are unverified.
Manuscript labels (`indices:…`, `analysis:…`, `gluing:…`, `stack:…`, `estimates:…`) refer to `src/*.tex`.
Notation: $Y_r=S^3_r(K)$, $g(K)=2$, $\phi\colon Y_{-2}\to Y_2$ orientation preserving. Field types: $A$ (irreducible instanton, $\Phi=0$), $R$ (abelian, $\Phi=0$), $S$ (Seiberg–Witten type: abelian with $\Phi\neq0$ in one summand), $F$ (free; the manuscript's $P$). Positive and negative *pieces* are topological, not field types.

Checks: `T1-checks/cell.py` (positive-piece estimate, brute force), `T1-checks/runs_dp.py` + `check_runs.py` (exact minimisation of the abelian energy on segments by dynamic programming), `T1-checks/endpoint.py` (closed forms).

---

## 0. Results and verdicts

The argument has three layers, each a statement of a classical type.

1. **A secondary invariant.** $\Omega$ is a bit-summed count of instantons over a cube of metrics whose faces stretch the psc rational homology spheres $S^3$ and $L(4,1)$, cut down by $\mu(S_1)\cdots\mu(S_n)$ and cap insertions. It equals $\langle\Psi_+,w^M\Psi_-\rangle$ and is $\equiv q\not\equiv0\pmod{2^N}$.
2. **A secondary Feehan–Leness relation** (Pidstrigach–Tyurin localization over the cube). If $n_D\ge1$, then $2^{n_D-1}\Omega$ equals a signed count of ends of the one-dimensional free $\mathrm{PU}(2)$-monopole space at *abelian* ideal limits, i.e. at Seiberg–Witten classes $K=\Lambda+v$ of non-negative Feehan–Leness level and at Kotschick–Morgan-type abelian instantons on segments. Face terms at $J$-faces vanish and face terms at lens faces cancel in pairs.
3. **A family adjunction inequality.** Every abelian configuration on a segment $\Gamma$ satisfies $\kappa_\Gamma\ge\tfrac12\big(s^-(\Gamma)+m(\Gamma)\big)$: each insertion costs charge $\tfrac12$, and each $b^+=1$ piece costs $\tfrac12$ but may absorb its two adjacent insertions. Globally this reads $-v^2/4+\#\{\text{missed insertions}\}\ge\tfrac{n-m}2-C$, against $\kappa=\tfrac{n+3m}8+C'$.

| Piece | Statement | Label | Conf. |
|---|---|---|---|
| Def. 1.3, Prop. 1.4 | $\Omega$ is a well-defined integer, invariant under admissible deformations; single-bit counts are not | P | 80% |
| Prop. 1.5 | gluing: $\Omega(X_M)=\pm\langle\Psi_+,\,w^M\Psi_-\rangle$ (with pads) | P | 80% |
| Prop. 1.7 | $\Omega(X_M)\equiv\pm q\not\equiv0\pmod{2^N}$ for $\varepsilon\mid M$ | V (algebra, given the mod-2 isomorphisms and $q\ne0$) | 95% |
| Thm. A | secondary FL relation, localization form, given AP1–AP6 | P (structure V) | 70% |
| AP1–AP4 | compactness, regularity, instanton links, $J$-faces | standard extensions of FL, PT, MMR, Donaldson | 80–90% each |
| AP5 | lens ends cancel in bit pairs in the monopole problem | P, new in detail | 70% |
| AP6 | necessary projection for mixed limits with abelian zero-spinor segments | P, the main new analytic lemma | 55–60% |
| Lemma 3.1 | local family adjunction inequality | V (given the clamp and the holonomy representatives); sharp | 95% as lattice statement |
| Lemma 3.3 | positive-piece estimate | V (brute force) | 99% |
| Prop. 3.4 | one endpoint count replaces Lemmas `indices:fixed-run`, `indices:mixed-run`, `indices:component-score` | V (closed form + DP) | 95% |
| §3.4 | spacing 3 suffices for broken fixed limits; for mixed limits the projection method needs exactly spacing $\ge4$ | V (closed form; DP shows the bound is attained at spacing 3) | 95% |
| §3.7 | counting wall codimension would give spacing 3 | S/P | 40% |
| Rem. 2.4 | with full obstructed gluing at abelian segments, no local spacing would be needed | S | 30% |
| Thm. 4.3 | the cosmetic theorem follows from Thm. 4.1 + Lemma 4.2 in one page | V as logic | 90% |
| Overall | the reorganized argument is a correct proof | P | 35–45% |

The weakest points are AP6, the clamp (manuscript Thm. `estimates:clamp`, uniformity across faces), and persistence of the zero-winding representatives under Uhlenbeck limits. None of them is touched by the reorganization below; the reorganization isolates them.

---

## 1. The secondary invariant

### 1.1 Data

**Definition 1.1 (admissible cube data).**
- $X$ closed, oriented, $H_1(X;\mathbb Z)=0$, $b^+(X)\ge1$.
- Disjoint separating 3-spheres $J_1,\dots,J_n$, and embedded 2-spheres $S_i$ with $S_i^2=-4$, $S_i\cap J_j=\emptyset$ for $i\ne j$, and $S_i=D_i^-\cup_{K}D_i^+$ meeting $J_i$ in a knot (the two 2-handle cores). Tubular neighbourhoods $N_i=\nu S_i$, $\partial N_i=L(4,1)$, pairwise disjoint and disjoint from $J_j$ for $j\ne i$.
- Cutting along all $J_i$ and filling by balls gives outer pieces $Z_0\supset C_-$, $Z_n\supset C_+$ and inner pieces $Z_1,\dots,Z_{n-1}$. In our application each inner piece is *negative* ($Z\cong N_\phi=X_{-2}(K)\cup_\phi(-X_2(K))$, lattice $2\langle-1\rangle$) or *positive* ($Z\cong P\cong\mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2$, lattice $H\oplus4\langle-1\rangle$, containing a square-zero sphere $U$ and the plumbing $(-S_j,U,S_{j+1})$ of type $(-4,0,-4)$). Write $m$ for the number of positive pieces. [V: Prop. `stack:lattice`; C-closed §1.2.]
- $Q=[-1,1]^n$ and a smooth family $g_t$, $t\in\operatorname{int}Q$, such that $t_i\to-1$ stretches a round neck $J_i\times[-T,T]$, $t_i\to+1$ stretches a psc collar $\partial N_i\times[-T,T]$, and the family has product structure near each face. All other seams (in particular the $Y_{\pm2}$ seams) stay finite.
- Bundles $c_e=c_0+\sum_ie_i\,\mathrm{PD}(S_i)$, $e\in\{0,1\}^n$, with $c_0\cdot S_i=0$; a characteristic class $l$ with $\Lambda_e=l+c_e$, $\Lambda_0\cdot S_i=2$. Then [V]
$$\Lambda_e^2=\Lambda_0^2,\qquad c_e^2=c_0^2-4|e|,$$
so $\kappa=c_2-c_e^2/4$, $\Theta=(\Lambda^2-\sigma)/4$, $D_I=8\kappa-3(1+b^+)$ and $n_D=\Theta-\kappa$ are independent of $e$.
- Insertions: $\mu(S_1),\dots,\mu(S_n)$ (degree 2) and cap insertions of total degree $z$, with $D_I=n+z$.

**Lemma 1.2 (holonomy representatives of $\mu(S)$) [P, 75%; manuscript Lemmas `analysis:zero-winding`, `analysis:segmentation`, `analysis:incidence`, `stack:tests`].** There is a representative $V(S)\subset\mathcal B$ of $\mu(S)$ ("the normalized holonomy of a sweep of loops across $S$ passes through $-1$") with:
1. $V(S)$ has codimension 2 and is transverse on irreducibles.
2. At a connection reducible as $L_1\oplus L_2$, $v=c_1(L_1)-c_1(L_2)$, the sweep is a loop in $U(1)$ of degree $v\cdot S/2$. If $v\cdot S\ne0$ the configuration lies in $V(S)$. If $v\cdot S=0$ it stays a uniform distance away from $V(S)$.
3. Along Uhlenbeck limits, membership in $V(S)$ persists unless an instanton particle lies on the 2-dimensional support of the sweep; distinct $S_i$ have disjoint supports.
4. At a $J_i$-face, $V(S_i)$ is the union of two half-representatives on $D_i^\pm$, each defined intrinsically on its side. After filling, the halves represent the classes $F_{l,i},F_{r,i}$ of square $-2$, by maps of spheres (the punctured traces are simply connected).

The cohomological content of (2)–(3) is classical: on the link of an abelian configuration at Feehan–Leness level $\ell$, $\mu(S)$ restricts to $\tfrac12\langle v,S\rangle\,h$ plus terms carried by the symmetric product $\mathrm{Sym}^\ell X$ (Kotschick–Morgan; Feehan–Leness†). The holonomy representative makes this geometric: a missed insertion must be paid by a particle on $S$.

### 1.2 Definition and invariance

**Definition 1.3.** For generic data put
$$\Omega(X;g)=\sum_{e\in\{0,1\}^n}\varepsilon(e)\,\#\Big\{(t,[A]) : t\in\operatorname{int}Q,\ A\ \text{ASD for }g_t\text{ on }E_e,\ [A]\in\textstyle\bigcap_iV(S_i)\cap V(z)\Big\},$$
where $\varepsilon(e)=\prod_i\varepsilon_i(e_i)$ and $\varepsilon_i(1)=-s_i\,\varepsilon_i(0)$, with $s_i$ the orientation comparison of the two minimal trace caps on $N_i$ (Prop. `negative:local-sign`).

**Proposition 1.4 (integrality and invariance) [P, 80%].**
1. The count is finite, and $\Omega\in\mathbb Z$.
2. $\Omega$ is unchanged under change of perturbations, of the representatives in Lemma 1.2, and of $g$ through admissible families (homotopies preserving the face structure).
3. The single-bit counts are *not* invariant: they jump by lens-face terms.
4. Changing the lengths of the finite $Y_{\pm2}$ seams is an admissible deformation; in the long-seam limit Prop. 1.5 applies. Changing the face structure (e.g. not stretching $\partial N_i$, or omitting the sum over $e_i$) changes the problem and is not covered.

*Proof sketch.* Consider the 1-dimensional parametrized moduli space of a deformation. Its ends are of three kinds.
- **$J$-faces.** The cut-down data do not depend on the $SO(3)$ gluing parameter at $J_i$ (Donaldson's connected-sum argument†). So the face moduli fibre over the space of limits, whose virtual dimension follows from $\sum_j(q_j+4)=5$ (Lemma 2.1 with one extra parameter). With irreducible components this forces some $q_j<0$, so the face is empty. [V as dimension count]
- **Lens faces.** These consist of (main piece) $\times$ (minimal trace cap of charge $\tfrac14$, holonomy degree $\pm1$). By the choice of $\varepsilon$ the two bits contribute oppositely (manuscript Prop. `negative:local-sign`). [P]
- **Abelian limits.** At $k=0$ these are excluded because the cap metrics are generic and the caps have $b^+>0$. At $J$-faces: for clamped families they are excluded by §3. In the ordinary 1-parameter problem $\sum_j(q_j+4)=5$; with $\alpha\ge2$ instanton components and abelian inner segments of $e_I\ge-2$ (Prop. 3.4) the left side is $\ge2\alpha+2\ge6$. For general admissible families use Prop. 1.5 and Floer-theoretic invariance of each block. [P] ∎

**Proposition 1.5 (gluing description) [P, 80%; Prop. `stack:composition`].** Let $X_M$ be the 4-manifold obtained by capping the composite cobordism
$$C_-\ \cup\ (\phi B)^{p_-}\ \cup\ \big((\phi B)^3(HB)\big)^M\ \cup\ (\phi B)^{p_+}\ \cup\ C_+ ,$$
with $n=4M+p_-+p_+$ intervals and $m=M$ positive pieces. Here:
- $\Psi_-\in I(Y_2;\mathbb Z)$ is the relative invariant of $C_-$ with its insertions, and $\Psi_+\in\mathrm{Hom}(I(Y_2;\mathbb Z),\mathbb Z)$ that of $C_+$;
- $B$ is the secondary relative invariant of $W'=(-C_2)\cup_{S^3}C_{-2}$ over $[-1,1]$ (the bit sum over $e\in\{0,1\}$);
- $H=f_+f_-$;
- $w=(\phi_*B)^3\circ(H\circ B)\in\mathrm{End}\,I(Y_2;\mathbb Z)$.

Then, for admissible cube families with sufficiently long finite $Y_{\pm2}$ seams,
$$\Omega(X_M)=\pm\big\langle\Psi_+,\ (\phi_*B)^{p_+}\,w^M\,(\phi_*B)^{p_-}\,\Psi_-\big\rangle .$$

*Proof sketch.* Define the secondary relative invariant of a cobordism with an admissible cube family as the count at index $i$ with $i+\dim Q-\sum\deg=0$. It is a chain map, because:
- its $J$-faces factor through Floer's irreducible complex $C(S^3)=0$;
- its lens faces cancel in bit pairs.

It is functorial for composites carrying product families, since the faces of a product are products. Stretching the finite $Y_{\pm2}$ seams uses only Floer's irreducible theory. Central flats on $Y_{\pm2}$ cost 3 in dimension, and the manuscript checks that no composite recovers this (Lemma `stack:local-excess`). ∎

**Remark 1.6 (why "secondary") [V].**
- $X_M$ is a connected sum along each $J_i$ with $b^+>0$ on both sides, so all ordinary Donaldson and Seiberg–Witten invariants of $X_M$ vanish (C-closed §1.3).
- $B$ is itself secondary. The index-2 operation $\mu(S)\cdot[W']$ has two nullhomotopies: the $J$-split (through $C(S^3)=0$) and the lens split (through the bit cancellation). $B$ is the difference cycle.
- Families over cubes and associahedra whose faces are neck-stretchings are the device of the surgery triangles (Floer; Kronheimer–Mrowka–Ozsváth–Szabó†; Culler–Daemi–Xie; DLME's $g_1$) and of Kronheimer–Mrowka's cube complexes in the unknot-detector paper†. Ruberman's 1-parameter metric-family invariants† are the closest closed-manifold analogue.
- The bit sum over $c_0+\sum e_i\mathrm{PD}(S_i)$ is the analogue of the sum over $w$ in the Kronheimer–Mrowka structure theorem, and of DLME's $\hat c-\check c$.

**Proposition 1.7 (nonvanishing) [V, given the inputs].** Inputs: $B,H,\phi_*$ are integral chain maps that are isomorphisms mod 2 (Thms `ordinary:units`, `negative:unit`), and $q=\langle\Psi_+,\Psi_-\rangle\neq0$ (Thm `caps:pairing`). Let $L=I(Y_2;\mathbb Z)/\mathrm{Tor}$ and $2^N\nmid q$.
1. An integral chain map that is a quasi-isomorphism mod 2 has a cone with finite odd-order integral homology (universal coefficients). Hence $w$ and $\phi_*B$ lie in $GL(L\otimes\mathbb Z_{(2)})$.
2. Let $\varepsilon$ be the exponent of $GL(L/2^NL)$. For $\varepsilon\mid M$ and $\varepsilon\mid p_\pm$ we get $\Omega(X_M)\equiv\pm q\not\equiv0\pmod{2^N}$.

This is B3's Lemma C. Over $\mathbb F_2$ the statement would be useless, since the localization below yields $2^{n_D-1}\Omega$.

---

## 2. The secondary Feehan–Leness relation

### 2.1 $\mathrm{PU}(2)$-monopoles over the cube

**Setup.**
- Spin$^u$ structures $\mathfrak t_e=(\mathfrak s,E_e)$, $V=W\otimes E_e$, with determinant connection fixed and determinant-one gauge.
- Equations $D_A\Phi=0$ and $\rho(F_A^{0,+})=(\Phi\Phi^*)_{00}$, plus perturbations.
- The circle $S^1$ acts on $\Phi$; $-1$ acts as the central gauge.

**Fixed points** [V, Def. `indices:types`].
- Type $A$: instantons.
- Type $S$: $E=L_1\oplus L_2$ with $\Phi$ in $W\otimes L_1$. These are Seiberg–Witten solutions for $K=\Lambda+v$, $v=c_1(L_1)-c_1(L_2)\equiv c\pmod 2$, perturbed by $2\pi i\Lambda^+$.
- Type $R$: abelian ASD with $\Phi=0$.

**Indices** [V, Lemma `indices:closed`, agreeing with FL†]:
$$D_I=8\kappa-3(1+b^+),\quad n_D=\Theta-\kappa,\quad D_{\rm sp}=D_I+2n_D,\quad d_s=\tfrac14\big(K^2-(2\chi+3\sigma)\big),\quad \kappa=-\tfrac{v^2}4+\ell .$$
$\ell\in\mathbb Z_{\ge0}$ is the **Feehan–Leness level** (the total charge of particles, cylinder levels and lens-cap excess). In FL's normalization† this is the condition that $M^{SW}_K\times\mathrm{Sym}^\ell$ lies in the Uhlenbeck closure.

**The cut-down free space.** Let $\mathcal Z$ be the free locus over $\operatorname{int}Q$, summed over $e$ with weights $\varepsilon(e)$, divided by $S^1$, and cut down by:
- the $V(S_i)$,
- the cap insertions,
- $\eta=n_D-1$ sections of the weight-two line.

Then [V]
$$\dim\mathcal Z=(D_I+n-2n-z)+2n_D-1-2\eta=1 .$$

### 2.2 Ideal limits and the dimension identities

An **ideal limit** has:
- a set of $k$ cut necks $J_i$;
- components $\hat X_0,\dots,\hat X_k$ (filled by balls), each of type $A$, $R$, $S$ or $F$;
- losses (particles, cylinder levels, separated lens caps).

For each component define its virtual cut-down instanton index $q_j=D_{I,j}+p_j-2s_j-z_j$ (with $p_j$ the retained interval parameters and $s_j$ the insertions assigned to it), and $i_j=q_j+2n_{D,j}$.

**Lemma 2.1 (dimension identities) [V, Lemma `indices:virtual-sums`].**
$$\sum_{j}(q_j+4)=4,\qquad\sum_j i_j-2\eta=2-4k,\qquad \kappa_j=-\tfrac{v_j^2}4+\ell_j\ \ (j\in R\cup S).$$
A $J$-cut costs 4: three for the $SO(3)$ gluing parameter, which is not recorded by the limit, and one for the lost interval parameter.

### 2.3 Statement

**Theorem A (secondary Feehan–Leness relation).** Assume the data of §1.1, $n_D\ge1$, and the analytic package AP1–AP6 of §2.4. Then $\mathcal Z$ has a compactification by ideal limits, and its ends are:
1. **instanton links**, contributing $2^{n_D-1}\operatorname{sign}(A)\,\varepsilon(e)$ for each counted instanton, in total $2^{n_D-1}\Omega$;
2. **lens ends**, which cancel in pairs under $e_i\leftrightarrow1-e_i$;
3. **abelian ends**: ends at ideal limits with at least one component of type $R$ or $S$.

$J$-face ends with no abelian component do not occur. Consequently
$$2^{\,n_D-1}\,\Omega\;=\;-\sum_{\zeta\ \text{abelian end}}\pm w(\zeta)\qquad(\text{rational weights }w).$$
Every abelian end is of one of the following kinds.
- **(a) Seiberg–Witten classes on $X$** ($k=0$). Type $S$ on all of $X$ at some $t\in Q$, for a class $K=\Lambda+v$ at Feehan–Leness level $\ell=\kappa+v^2/4\ge\#\{i : v\cdot S_i=0\}$, with all lens-cap excess counted in $\ell$. Type $R$ cannot occur at $k=0$ (generic cap periods).
- **(b) Broken fixed limits** ($k\ge1$, no $F$ component). Lemma 2.1 holds with $q_j\ge0$ on $A$ components; outer abelian components are of type $S$.
- **(c) Mixed limits** ($k\ge2$; an $F$ component and abelian zero-spinor segments $\Gamma_1,\dots,\Gamma_\rho$). These satisfy
$$5-4N-\sum_{j=1}^\rho e_{PU}(\Gamma_j)\ \ge\ 0,$$
where $N$ is the number of non-$R$ components and $e_{PU}$ is the excess of Def. 3.2.

**Corollary B (secondary vanishing).** If no configuration of kinds (a)–(c) exists, then $2^{n_D-1}\Omega=0$.

The right side of Theorem A is a sum over Seiberg–Witten classes and abelian walls at non-negative Feehan–Leness level. This makes it the family analogue of the FL formula $2^{n_D-1}D^w(z)=\sum_K SW(K)\,f(K)$†. Evaluating the abelian ends as Seiberg–Witten numbers times universal coefficients would need FL's gluing at abelian strata of all levels. We do not need it: Lemma 3.1 shows that the set of contributing classes is empty.

### 2.4 Proof of Theorem A, in the Pidstrigach–Tyurin structure

$\mathcal M\supset\mathcal M^{S^1}=\{A\}\sqcup\{R,S\}$. $\mathcal Z$ is the cut-down quotient of the free part, and $\partial\bar{\mathcal Z}$ = (links of fixed components) $\sqcup$ (face ends). The proof is Stokes on $\bar{\mathcal Z}$.

| Step | Content | Inputs | Status |
|---|---|---|---|
| AP1 | Uhlenbeck compactness of $\mathrm{PU}(2)$-monopoles, parametrized over $\bar Q$; on psc necks the spinor dies (Weitzenböck) and the connection converges exponentially to a flat ($H^1(Y;\mathrm{ad}\rho)=0$ on $S^3$, $L(4,1)$) | FL-I†; Morgan–Mrowka–Ruberman†; Donaldson's Floer book†; Lemmas `analysis:compactness`, `analysis:neck` | standard extension, P 85% |
| AP2 | regularity: $A$ components with retained insertions are transverse ($q_j\ge0$; strict with losses); $S$ components tangentially transverse ($d_s+p+4\ell\ge0$); the free stratum is transverse; Dirac surjective at the counted instantons | Donaldson–Kronheimer†; FL-I/Teleman holonomy perturbations†; Prop. `analysis:first-stage` | standard, P 85% |
| AP3 | instanton links: $\mathbb P(\ker D_A)=\mathbb{CP}^{n_D-1}$; the weight-two line is $\mathcal O(2)$; $\langle(2h)^{n_D-1},[\mathbb{CP}^{n_D-1}]\rangle=2^{n_D-1}$ | PT†; FL-II link lemma†; Prop. `analysis:instanton-link` | V (computation), P 90% (analysis) |
| AP4 | $J$-face ends without abelian components: the space of limits has dimension $\sum_ji_j-2\eta-1=1-4k<0$ | Lemma 2.1; Donaldson's $SO(3)$ argument | V |
| AP5 | lens ends: regular gluing of the minimal trace cap ($\kappa_N=\tfrac14$, $\Phi=0$, Dirac invertible by psc, $U(1)$ stabilizer absorbed); opposite orientations for the two bits with the same $\varepsilon$ as for $\Omega$ (the Dirac factor is complex) | gluing at reducible flats (Donaldson†, MMR†); Props. `gluing:regular-cap`, `gluing:signs` | new in detail, P 70% |
| AP6 | mixed limits with $R$ segments: necessary projection (Lemma 2.3) | Lemmas `analysis:projection`, `analysis:R-independence`, Prop. `analysis:finite-induction` | **new**, P 55–60% |
| — | bubbling in the free stratum: a particle costs 6 and recovers at most 4 through position and released insertions | Lemma `indices:loss-budget` | V (count), P (analysis) |
| — | Stokes on a weighted branched 1-manifold | McDuff†; Cieliebak–Mundet–Salamon†; Lemma `analysis:stokes` | standard, P 90% |

*Proof.*
1. By AP1, every end of $\mathcal Z$ has an ideal limit.
2. If the limit is an unbroken loss-free instanton, AP3 gives the link contribution.
3. Unbroken $F$ limits are interior points.
4. A limit with particles on an $F$ component has dimension $\le1-2<0$.
5. A limit at $J$-faces with only $A$ and $F$ components is excluded by AP4. With $S$ components (retained and regular) the same count applies.
6. Lens ends are handled by AP5.
7. All remaining ends are abelian. Kind (b) is Lemma 2.1 together with AP2.
8. For kind (c), the space of projections of such limits has dimension at most $5-4N-\sum_je_{PU}(\Gamma_j)-(\text{losses})$ by Lemma 2.3, and it is empty when this is negative (AP6).
9. Stokes gives the identity. ∎ [Structure V; overall P 70%]

**Remark 2.2 (equivariant form) [P].** Over $\mathbb Q[u]$ the same argument reads $2^{n_D-1}\Omega\,u^{-1}+\sum_{\rm abelian}\mathrm{Res}=\text{polynomial}$, an Atiyah–Bott residue identity (B3 §1.6). The instanton residue is $u^{-n_D}(2u)^{n_D-1}$.

### 2.5 The mixed limits, and what the projection costs

**Lemma 2.3 (necessary projection) [P, 55–60%; Lemma `analysis:projection`].** Let $\zeta$ be a mixed ideal limit whose $R$ components form segments $\Gamma_1,\dots,\Gamma_\rho$. Discard the $R$ fields, their particles and their insertions, but retain their interval parameters. Assume that perturbations and phase sections do not couple through $R$ components (Lemma `analysis:R-independence`). Then:
- the retained components satisfy their own equations, their own insertions, and *all* $\eta$ phase sections, since a weight-two section vanishes on a zero spinor;
- the projected problem is Fredholm with finite isotropy (the $F$ component kills the phase);
- after the phase quotient its index is
$$\sum_{j\notin R}i_j+\sum_{R}p_j-2\eta-1\;=\;5-4N-\sum_{j=1}^{\rho}e_{PU}(\Gamma_j)\quad(\text{minus losses}),$$
using Lemma 2.1 and $k+1=N+\#R$;
- for generic multisections the projected problem is empty when the index is negative.

**Why it is needed.**
- An $R$ segment is never cut out transversely. Its obstruction space has a weight-zero part $H^+(\hat \Gamma)$ (the wall condition, removable by moving parameters) and parts of non-trivial weight under its $U(1)$ stabilizer (the cokernels of the normal ASD operator on $L_1L_2^{-1}$ and of the Dirac operator). Equivariant perturbations cannot remove the latter at the abelian point.
- Its actual moduli therefore has *excess* dimension: up to its $p$ parameters, while its virtual index $i-p$ may be very negative.
- The projection uses only the bound "an $R$ segment contributes at most its parameters". It prices the segment by its virtual $\mathrm{PU}(2)$ index $i(\Gamma)-p(\Gamma)=e_{PU}(\Gamma)-4$ (for $r=1$). Hence charge enters as $6\kappa$ (8 from ASD, $-2$ from Dirac), and each discarded insertion gives back 2.

**Classical alternative.** Obstructed gluing of an abelian segment to non-abelian pieces across $S^3$ necks, with gluing parameter in $SO(3)/U(1)$, in the style of Donaldson's connected-sum theorem, Kotschick–Morgan, and FL's gluing at SW strata. This is of FL difficulty and is not available in families with faces.

**Remark 2.4 [S, 30%].** Assume a Kuranishi model at mixed limits, i.e. an obstructed gluing theorem transverse on the free part, where the combined stabilizer is finite. Then every ideal limit with $k$ cuts has virtual codimension $k$ in the 1-manifold $\bar{\mathcal Z}$, so limits with $k\ge2$ are not reached. $R$ segments need $k\ge2$, because outer pieces are never of type $R$. So mixed limits, and broken fixed limits with $k\ge2$, would be excluded with no local spacing condition. Only (a) and the $k=1$ limits with an $S$ outer component would remain. Those are controlled by global density and the caps (§3.5).
- If correct, spacing 4 is the price of avoiding obstructed gluing, not an intrinsic feature.
- The global density range $\tfrac15<m/n<\tfrac37$ (§3.4) would remain, and it is where $\phi$ is genuinely used.
- Main risk: at $T=\infty$ the obstruction section is independent of the gluing parameter, so transversality comes only from the leading interaction term. Its genericity in families with psc faces is unproved.

---

## 3. The family adjunction inequality

### 3.1 Statement

Fix an abelian component of an ideal limit, supported on a **segment** $\Gamma=Z_a\cup\dots\cup Z_b$ of consecutive inner pieces, possibly divided by $r(\Gamma)-1$ further cut necks into $r(\Gamma)$ abelian components of the same limit. Put:
- $L(\Gamma)$ = number of pieces; $m(\Gamma)$ = number of positive pieces;
- $s(\Gamma)$ = number of insertions $\mu(S_i)$ assigned to $\Gamma$ (internal ones always; a bounding one if its half lies in $\Gamma$);
- $s^+(\Gamma)$ = assigned insertions adjacent to positive pieces of $\Gamma$, and $s^-(\Gamma)=s(\Gamma)-s^+(\Gamma)$;
- $f(\Gamma)=2m(\Gamma)-s^+(\Gamma)\in\{0,1,2\}$, the adjacent insertions assigned across the bounding necks;
- $v_\Gamma\in H^2(\hat \Gamma)$ the line difference, with $\kappa_\Gamma=-v_\Gamma^2/4+\ell_\Gamma$, where $\ell_\Gamma$ includes particles, $J$-cylinder charges and lens-cap excess.

**Lemma 3.1 (family adjunction inequality, local form).** Assume the clamp (Thm `estimates:clamp`) and Lemma 1.2. Then for every abelian configuration on $\Gamma$, of type $R$ or $S$, including Uhlenbeck limits, separated lens caps and half-insertions at cut necks,
$$\boxed{\ \kappa_\Gamma\ \ge\ \tfrac12\big(s^-(\Gamma)+m(\Gamma)\big)+\tfrac12 z_0(\Gamma)\ }$$
where $z_0$ counts insertions not adjacent to positive pieces that are met only through particles.
- **[V]** as a lattice statement, given the clamp alternatives and Lemma 1.2(2)–(4).
- It is sharp: the DP minimum of $\kappa_\Gamma-\tfrac12(s^-+m)$ is $0$ on every segment tested (§3.6).

**Corollary 3.2 (global form) [V given the cap bounds].** For an abelian class $v$ on $X$ (kind (a)) meeting all $n$ insertions, let $T(v)$ be the number of insertions met only through particles. Then
$$-\tfrac{v^2}4+T(v)\ \ge\ \tfrac{n-m}2-C,\qquad C=\tfrac14(C_{W_-}+C_{W_+}),$$
with $C_W$ the cap constants of Prop. `estimates:cap`. Since $8\kappa=n+3m+c_\kappa$ with $c_\kappa=z+3+3b_0$, the effective Feehan–Leness level satisfies
$$\ell-T(v)=\kappa-\Big(-\tfrac{v^2}4+T(v)\Big)\ \le\ \frac{7m-3n+c_\kappa}{8}+C .$$
**No Seiberg–Witten class contributes once $3n-7m>c_\kappa+8C$.**

**Definition 3.2 (index excesses).** For a segment $\Gamma$ with abelian configuration, write $\Delta(\Gamma)=e_a-e_b\in\{-1,0,1\}$ for its endpoint bits. Set
$$e_I(\Gamma)=8\kappa_\Gamma-3m+L-2s=q(\hat \Gamma)+4,\qquad e_{PU}(\Gamma)=r+6\kappa_\Gamma-m+\Delta-2s .$$
For $r=1$, $e_{PU}(\Gamma)-4=i(\hat \Gamma)-p(\hat \Gamma)$. So $e_I-4$ and $e_{PU}-4$ are the virtual cut-down instanton and $\mathrm{PU}(2)$ dimensions of the segment, the latter with its parameters removed. $e_I$ does not depend on $r$ [V].

### 3.2 Proof of Lemma 3.1

**(a) Lattice [V].** $\hat \Gamma$ splits rationally and orthogonally over the rational homology spheres, so $v_\Gamma^2=\sum_{Z\subset \Gamma}v|_Z^2$.
- On a negative piece, $v|_Z^2=-\tfrac12(h^2+h'^2)$, with $h=v\cdot F_r$ and $h'=v\cdot F'_l$ even (since $v\equiv c\pmod2$ and $c$ is even on the trace classes).
- On a positive piece, in the basis $G,U,T_1..T_4$,
$$v|_P^2=2xu-2u^2-\textstyle\sum_bt_b^2,\qquad x\ \text{even},\ \text{exactly two } t_b \text{ odd},\qquad v\cdot F_r=x-\textstyle\sum t_b,\quad v\cdot F'_l=x-2u .$$

**(b) Insertions [P, via Lemma 1.2].** $\mu(S_i)$ evaluates on $v$ through $v\cdot S_i=v\cdot F_{l,i}-v\cdot F_{r,i}$, the difference of two halves in adjacent pieces (at a cut neck, only the assigned half counts). An insertion is either met, in which case its relevant half is a non-zero even number, or missed, in which case it is paid by a particle (a distinct one for each insertion, by disjoint supports). An insertion not adjacent to a positive piece has both halves in negative pieces, so a met one contributes at least $2$ to $-v^2$.

**(c) Positive pieces.** Each positive piece reserves the two negative halves adjacent to it, $h_1$ and $h_2$; these belong to its two adjacent insertions. The clamp says: either $u=0$, or for some non-empty $I$ among the adjacent *uncut* sides,
$$\operatorname{sign}(u)\,v\cdot H_I\le0\ (R),\qquad \operatorname{sign}(u)\,v\cdot H_I<|\Lambda\cdot H_I|\ (S),\qquad H_I=U+\tfrac14\textstyle\sum_{i\in I}X_i .$$
(It comes from Weitzenböck on toric $\mathrm{Scal}\ge0$ metrics with period $H(a,b)=U+aX_1+bX_2$ in the vertex hull.)

**Lemma 3.3 (positive piece) [V, `cell.py`; Lemma `indices:positive-square`].** $Q:=v|_P^2-\tfrac12\sum_{i\in I}h_i^2\le-2$, except for type $S$ with $|I|=1$ and $u=v\cdot H_I=\pm1$. In that case $Q\le2$ and the insertion on the side $I$ is missed.
- Brute force over $|x|\le14$, $|u|\le5$, $|t_b|\le4$, $|h_i|\le16$, all four bit pairs, both types and every admissible $I$ gives no violation.
- Maxima: $R$: $-6$ ($|I|=1$), $-4$ ($|I|=2$); $S$: $2$ (the exception), $-2$ ($|I|=2$).

**(d) Assembly [V].** The reserved halves and the halves used by the other insertions are disjoint, because positive pieces are at distance $\ge2$. Let $e_0$ be the number of exceptional positive pieces. Then
$$-v_\Gamma^2\ \ge\ 2\big(s^--z_0\big)+2m-4e_0,\qquad \ell_\Gamma\ge z_0+e_0,$$
so $\kappa_\Gamma\ge\tfrac12(s^-+m)+\tfrac12z_0$. Insertions adjacent to positive pieces are not used at all, which is the source of the slack exploited by $f(\Gamma)$ below.

**(e) Limits [P].** Every ingredient survives degeneration:
- the lattice identity is topological;
- Lemma 1.2(3) charges each missed insertion to a particle;
- a separated lens cap is filled by its reference connection ($d=v\cdot S\in\{0,\pm2,\pm4\}$, charges $0,1,\tfrac14$) and its excess is added to $\ell$, as in Prop. `indices:lens-index`; the insertion on $N_i$ is whole and is met iff $d\ne0$;
- at a cut neck only the assigned half counts, and the clamp uses only uncut sides; this is the manuscript's switching convention;
- the clamp persists in the limit (Lemma `estimates:vertices`).

So the inequality holds for every abelian component of every ideal limit. ∎

### 3.3 Consequences for broken limits: one endpoint count

**Proposition 3.4 [V; closed form in `endpoint.py`, DP in `check_runs.py`].** Suppose positive pieces are at mutual distance $\ge k$. For a segment with $m\ge1$, let $a,b$ be the numbers of negative pieces before the first and after the last positive piece, $\epsilon_a,\epsilon_b$ the endpoint assignments, and $g\ge0$ the excess gaps. Then $L=k(m-1)+1+a+b+g$, $s=L-1+\epsilon_a+\epsilon_b$, $f=[a{=}0,\epsilon_a{=}0]+[b{=}0,\epsilon_b{=}0]$, and Lemma 3.1 gives
$$e_I\ \ge\ 2s-7m+L+4f\ \ge\ (3k-7)m-3k+5,\qquad e_{PU}\ \ge\ r+s-4m+\Delta+3f\ \ge\ (k-4)m-k+2 .$$
The only inequality used is the endpoint count
$$3a+2\epsilon_a+4[a{=}0,\epsilon_a{=}0]\ge2,\qquad a+\epsilon_a+3[a{=}0,\epsilon_a{=}0]\ge1$$
at each end. For $m=0$: $e_I\ge2s+L\ge1$ and $e_{PU}\ge r+s+\Delta\ge0$. Hence:
- $e_I(\Gamma)\ge-2$ for every abelian segment as soon as $k\ge3$;
- $e_{PU}(\Gamma)\ge-2$ for every $R$ segment as soon as $k\ge4$.

**Proposition 3.5 (empty contributing set for broken limits) [V given Lemma 3.1, AP2, AP6 and §3.5].** With spacing $\ge4$ and the outer estimate $e_I\ge8$ of §3.5, there are no ends of kinds (b) and (c).
- **(b).** Let $\alpha$ be the number of $A$ components ($q+4\ge4$ each) and $\beta\le2$ the number of outer $S$ components ($q+4\ge8$ each); $\alpha+\beta\ge2$ since $k\ge1$. Abelian inner segments between them number at most $\alpha+\beta-1$, each with $e_I\ge-2$. So $\sum(q_j+4)\ge2\alpha+6\beta+2\ge6>4$, contradicting Lemma 2.1. (For $k=0$ see kind (a).)
- **(c).** Outer pieces are never of type $R$, so $N\ge2$ and $5-4N-\sum e_{PU}\le5-4N+2(N-1)=3-2N<0$.

This replaces Lemmas `indices:component-score`, `indices:fixed-run` and `indices:mixed-run` and the first half of `indices:end-exclusion` by Lemma 3.1 plus one endpoint count.

### 3.4 Why the broken limits need a *local* density condition, and why 4

**One period, i.e. $k$ intervals carrying one positive piece [V]:**

| quantity | increment per period | positive iff |
|---|---|---|
| available charge $8\kappa=n+3m+c_\kappa$ | $k+3$ | — |
| minimal abelian charge $8\kappa_{\min}=4s^-+4m$ | $4(k-2)+4=4k-4$ | — |
| $n_D=\Theta-\kappa$ | $(5-k)/8$ | $k<5$ |
| global level bound $8(\ell-T)$ | $7-3k$ | $k<7/3$ (bad) |
| $e_I$ (broken fixed limits) | $3k-7$ | $k\ge3$ |
| $e_{PU}$ (mixed limits) | $k-4$ | $k\ge4$ |

**Observations.**
1. The fixed-limit excess per period equals minus the global level increment. **The broken-fixed condition is the global Feehan–Leness condition localized to segments.**
2. Broken limits can isolate *any* segment: the free or instanton components choose where the necks are cut. Every segment must therefore be outside the contributing set, not just $X$. A segment ending at a positive piece has lost the insertion beyond the neck. This is the end term $f$, and it is the only place where short segments behave differently from long ones. A global density $m/n<\tfrac37$ does not control segments, but local spacing does.
3. In mixed limits the abelian segment is weighted by its $\mathrm{PU}(2)$ index: charge enters as $6\kappa$, and a positive piece contributes $-3+2\Theta=-1$ instead of $-3$, since its Dirac index $\Theta=1$ feeds back into the spinor count. Per period:
   - each insertion not adjacent to the positive piece nets $+3-2=+1$;
   - the positive piece with its two adjacent insertions nets $3-1-4=-2$;
   - total $k-4$.

   So spacing 4 is forced *for this method*. The DP confirms the bound is attained: with spacing 3 the segment $PNNPNNPNNP$ ($m=4$) reaches $e_{PU}=-5=(k-4)m-k+2$, so mixed limits cannot be excluded by projection at spacing 3.
4. Integral period lengths: $n_D>0$, the global condition, and broken-fixed exclusion allow $k\in\{3,4\}$. The projection allows only $k=4$, i.e. density $\to\tfrac14$, inside $(\tfrac15,\tfrac14]$.
5. **Where $\phi$ enters [V].** Without $\phi$, every $B$ must be followed by $H$, so $k=1$ and $m\approx n$. Then the global level bound grows like $+4$ per period, the contributing set is non-empty, and Theorem A predicts non-zero abelian terms. This is consistent with $HB\simeq\mathrm{id}$ (mod 2) and a non-zero $\Omega$. $\phi$ is what makes $k>7/3$ possible.

### 3.5 Outer pieces (caps)

For a segment $\Gamma$ containing a cap $W$ and the exceptional class $E$ [P; Lemma `indices:end-exclusion`]:
$$8\kappa_\Gamma\ \ge\ 4s^-+4m+2\textstyle\sum_Ev(E)^2-C_1,\qquad e_I(\Gamma)\ \ge\ 3L-7m+2\textstyle\sum_Ev(E)^2-C_2 .$$
- **Pads.** Positive pieces are at distance $\ge L_*$ from the caps. A long outer segment then has $e_I\ge8$.
- **Short outer segments** contain no positive piece. The tangential bound $d_s+p+4\ell\ge0$ and the cap bound on $K_W^2$ give $|K\cdot E|\le B$. So $|v\cdot E|\ge|\Lambda\cdot E|-B$, and a large odd $\Lambda\cdot E$ makes $e_I\ge8$.
- **Classical reading.** On a blow-up the Seiberg–Witten classes have bounded $K\cdot E$ (blow-up formula†). Choosing $\Lambda\cdot E$ large pushes them to very negative Feehan–Leness level. FL use the same device† when choosing $c_1(\mathfrak t)$.

### 3.6 Machine checks [V]

- `cell.py`: Lemma 3.3, no violations.
- `check_runs.py` (exact minimum of $-v^2/4+\#\text{missed}$ over a box, subject to the clamp alternatives, by dynamic programming along the segment, over all bits and endpoint assignments):
  - spacing 4, $L\le11$, no internal cuts: $\min\big(\kappa-\tfrac12(s^-+m)\big)=0$, $\min e_I=-2$, $\min e_{PU}=-2$;
  - spacing 3, $L\le10$: $\min e_I=-2$, $\min e_{PU}=-5$ (at $PNNPNNPNNP$);
  - spacing 4, $L\le7$, up to 2 internal cut necks (every assignment of the cut insertions to either side; clamp restricted to uncut sides): again $\min\big(\kappa-\tfrac12(s^-+m)\big)=0$, $\min e_I=-2$, $\min e_{PU}=-2$. (A longer run, $L\le9$ with one cut plus spacings 3 and 2, hit the 10-minute limit and was stopped; it is not needed for the statements.)
  - Box: halves $|h|\le10$, $|x|\le12$, $|u|\le3$, $|\sum t_b|\le9$. Minima are attained at small values (e.g. the single positive piece with $\kappa=\tfrac12$), well inside the box.
- `endpoint.py`: the closed forms of Prop. 3.4 agree with enumeration for $k=2..5$, $m\le6$.

### 3.7 Relaxation by wall codimension [S/P, 40%]

On a positive piece an $R$ configuration requires $v\cdot H(a,b)=0$, an affine condition in the two adjacent interval parameters. These parameters are retained by the projection.
- If $v\cdot X_1$ or $v\cdot X_2$ is non-zero, the wall has codimension 1 and adds $+1$ to the projected count.
- Otherwise both adjacent insertions are missed, which costs at least $12$ in $6\kappa$.

Either way $e_{PU}$ gains at least $m(\Gamma)$, i.e. $k-3$ per period, so spacing 3 would suffice and the admissible density range would widen to $(\tfrac15,\tfrac13]$. This needs transversality of the period map to the walls in the retained parameters, uniformly near faces, which I have not checked. It agrees with D-families §4.5.

---

## 4. The main argument as it would appear in a paper

**Theorem 4.1 (secondary vanishing).** Let $(X;J_i,S_i;c_0,\Lambda_0;g)$ be admissible cube data as in §1.1, with clamped metrics on the positive pieces (Thm `estimates:clamp`), generic cap metrics, and the representatives of Lemma 1.2. Assume:
1. $n_D=\Theta-\kappa\ge1$;
2. positive pieces are at mutual distance $\ge4$ and at distance $\ge L_*$ from $Z_0,Z_n$, and $|\Lambda_0\cdot E_\pm|$ is sufficiently large and odd;
3. $3n-7m> C_0$, where $C_0$ depends only on the caps.

Then $2^{n_D-1}\,\Omega(X;g)=0$.

*Proof.* By Theorem A it suffices to exclude abelian ends.
- (a): Corollary 3.2 and (3).
- (b), (c): Proposition 3.5, using Lemma 3.1, Proposition 3.4 and §3.5. ∎

**Lemma 4.2 (family adjunction inequality).** Every abelian configuration on a segment $\Gamma$ that meets its assigned insertions and satisfies the chamber conditions on the positive pieces has $\kappa_\Gamma\ge\tfrac12\big(s^-(\Gamma)+m(\Gamma)\big)$. On $X$ this gives $-v^2/4+T(v)\ge\tfrac{n-m}2-C$.

**Theorem 4.3.** Let $K\subset S^3$ be a knot of genus 2. There is no orientation-preserving diffeomorphism $S^3_{-2}(K)\to S^3_2(K)$. Consequently, the purely cosmetic surgery conjecture holds.

*Proof.* By Hanselman† and DLME Cor. 1.4, a purely cosmetic pair must be $\{\pm2\}$ with $g(K)=2$. Suppose $\phi\colon Y_{-2}\to Y_2$ is an orientation-preserving diffeomorphism.

1. *Floer input.* In Floer's irreducible determinant-one theory, the maps $B\colon I(Y_2)\to I(Y_{-2})$ (the secondary invariant of $W'$ over the interval from the $S^3$-split to the $L(4,1)$-split, summed over $c$ and $c+\mathrm{PD}(S)$), $H=f_+f_-$ and $\phi_*$ are integral and are isomorphisms mod 2. The caps $C_\pm$ give $\Psi_\pm$ with $q=\langle\Psi_+,\Psi_-\rangle\neq0$.
2. *Choices.* Choose the caps, their constants, $L_*$ and $\Lambda\cdot E_\pm$. Choose $N$ with $2^N\nmid q$, and let $\varepsilon$ be an exponent of $GL(L/2^NL)$, $L=I(Y_2;\mathbb Z)/\mathrm{Tor}$, enlarged to be divisible by 8. Take pads $p_\pm\in\varepsilon\mathbb Z$, $p_\pm\ge L_*$, and $M\in\varepsilon\mathbb Z$. Then $n,m\equiv0\pmod8$; relative to the cap pairing, $8\kappa$ changes by $n+3m$, so $c_2$ is integral in every bit sector (Thm `stack:nonzero`).
3. *Nonvanishing.* Let $X_M$ be the 4-manifold obtained by capping $C_-\cup(\phi B)^{p_-}\cup\big((\phi B)^3HB\big)^M\cup(\phi B)^{p_+}\cup C_+$. By Props. 1.5 and 1.7, $\Omega(X_M)\equiv\pm q\not\equiv0\pmod{2^N}$.
4. *Topology.* $X_M$ has $n=4M+p$ intervals ($p=p_-+p_+$) and $m=M$ positive pieces at mutual distance exactly 4. By the telescope ($\Theta$ gains 1 per positive piece; $8\kappa=n+3m+c_\kappa$),
$$n_D=\frac{5m-n}8+c_1=\frac{M-p}{8}+c_1,\qquad 3n-7m=5M+3p .$$
   The constant $c_1$ depends on the caps and on $\Lambda\cdot E_\pm$ (a large $|\Lambda\cdot E|$ lowers $\Theta$ by $\Lambda(E)^2/4$), all fixed before $M$. So for $M$ large, both $n_D\ge1$ and $3n-7m>C_0$ hold.
5. *Vanishing.* Theorem 4.1 gives $2^{n_D-1}\Omega(X_M)=0$, so $\Omega(X_M)=0$, a contradiction. ∎

*Where $\phi$ is used.* Only in step 4: it lets three of every four intervals return to $Y_2$ without a $b^+=1$ piece. That puts the density of positive pieces in $(\tfrac15,\tfrac37)$ globally and spaces them 4 apart locally.

*Remark (coefficients).* Steps 3 and 5 need $\mathbb Z$ (or $\mathbb Z_{(2)}$). Over $\mathbb F_2$, step 5 is empty once $n_D\ge2$.

---

## 5. Verdict

1. **Secondary invariant (§1): sound, P 80%.**
   - The definition, its invariance under admissible deformations, and the gluing description are standard in kind. They are cube families with stretching faces, as in Floer, KMOS, KM and DLME.
   - The non-standard input is the integral lens cancellation behind $B$. I did not re-verify it here.
   - Nonvanishing mod $2^N$ is V given the mod-2 isomorphisms and $q\ne0$.
2. **Secondary Feehan–Leness relation (§2): P 70% for Theorem A given AP1–AP6.**
   - Standard (routine extensions): FL compactness, transversality and instanton links; PT structure; MMR/Donaldson psc necks; Donaldson's $SO(3)$-gluing count at $J$-faces; weighted Stokes.
   - New:
     - AP5, the lens cancellation carried into the monopole problem (70%);
     - AP6, the necessary projection for mixed limits with abelian zero-spinor segments (55–60%). This is the only genuinely new analytic idea, and it replaces FL-type obstructed gluing.
   - The FL-type evaluation of abelian terms is never needed.
3. **Family adjunction inequality (§3): V as a lattice statement, and sharp.**
   - One inequality (Lemma 3.1) and one endpoint count (Prop. 3.4) replace the case analysis of Section 8.
   - The broken limits need *local* density because cut necks can isolate any segment. The value 4 rather than 3 comes from weighting abelian segments by their $\mathrm{PU}(2)$ index in the projection. The DP shows the projection bound is attained at spacing 3, so this is not slack in the arithmetic.
   - Counting wall codimension (40%) or full obstructed gluing (30%) would remove or weaken it.
4. **Paper-form argument (§4): V as logic (90%).** Its correctness reduces to Theorem A's package, the clamp (P 65–70%), Lemma 1.2's persistence (P 70–75%), and the Floer inputs of Sections 2–4 of the manuscript (P 70–75%).
   - Overall confidence that the reorganized argument proves the theorem: **35–45%**.
   - The decisive checks are AP6, the clamp's uniformity at faces, and Lemma 1.2(3).
