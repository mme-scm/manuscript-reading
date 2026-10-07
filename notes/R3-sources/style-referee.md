# Style and naturalness: referee's report on the four Round 3 statements

*Read for this report:* `round3/B-final.md`, `round3/nonvanishing-final.md`, `round3/gluing-final.md`, `round3/relation-final.md` and `strategy.tex`. *Consulted for notation:* Kronheimer–Mrowka, *Khovanov homology is an unknot-detector*, §3.9 (source in `round3/km1005.4346`), and Feehan–Leness, *PU(2) monopoles. II* (source in `lit/dg-ga_9712005`). Below, the four files are cited as **[B]**, **[NV]**, **[G]**, **[R]**, the strategy as **[S]**, and these two sources as **[KM11]** and **[FL2b]**.

**Labels.** **VERIFIED**: checked by reading the files or the cited source, or proved here. **PLAUSIBLE**: argued here but not checked in full. **SPECULATIVE**: a guess. Recommendations and judgements of taste carry no label. Every assertion of fact, whether about the texts or about mathematics, carries one.

---

## 0. Summary

1. **What the files are.** Each of the four files is a referee's record wrapped around a statement. Corrections of earlier drafts, computer verifications, file paths, line numbers and private notes take up most of the text (VERIFIED, Appendix A). Each file nevertheless contains statements of the kind a gauge theorist expects, and they can be extracted by changes that are mostly editorial.
2. **The statements worth keeping**, each reformulated in §§2–5:
   - [B]: the chain map defined by the interval of metrics on $W_B$ (its Theorem A(a), (c), (e)); the closed relation for a sphere of square $-4$ (its Proposition B); the grading constraint on a cosmetic pair (its Corollary 4.4, which is also [NV] Proposition 5.4).
   - [NV]: the caps obtained from the closed symplectic manifold of Kronheimer–Mrowka, and the nonvanishing of their pairing through $H^{-1}$ in genus at least two (its Propositions 4.1–4.2 and Theorem 4.4(a)). Its title theorem (Theorem 1) is linear algebra.
   - [G]: the composition law that expresses the family invariant as a Floer pairing (its Theorem A′, with Theorem A as a step).
   - [R]: the vanishing theorem for $\mathrm{SO}(3)$-monopoles over a cube of metrics (its Theorem A), and its application to $u=(\phi_*B)^3HB$ (its Theorem C). The application rests on one clean lattice inequality (Proposition 6.1 below).
3. **What stands in a reader's way.**
   - (a) Dimension counts are written as an economy: "costs", "supplies", "spends", "saves".
   - (b) There are about twenty invented labels.
   - (c) At least fifteen symbols carry two or more meanings, and four of these clash with the notation of Feehan–Leness or Kronheimer–Mrowka.
   - (d) There are about forty-four named hypotheses, with (B1) and (B2) used in two different senses.
   - (e) Three different closed manifolds are called $X_M$, and two different arguments for nonvanishing (rational and $2$-adic) are used.

   All VERIFIED (§1, Appendix A).
4. **Order** (§6). Floer theory of $Y_{\pm2}$ → the map $B$ → the family invariant and the composition law → nonvanishing → the vanishing theorem in families → absence of reducible limits → proof of the main theorem. As the files stand, eight compatibility conditions between these sections are not met. Two are of substance: the vanishing theorem must be proved for the same composites and the same family of metrics (long necks along $Y_{\pm2}$) for which the composition law and the nonvanishing are proved.
5. **Verdict** (§7). Reformulated and ordered as proposed, the four statements and the Strategy form a coherent proof outline of a conditional theorem. Confidence about 80%.

---

## 1. Remarks that apply to all four files

### 1.1 Material that does not belong in a statement

- [B] cites the manuscript by file and line on 35 lines, for instance "[M, `03-negative.tex` l. 66–77]". VERIFIED.
- Private notes T1–T5 are cited on 54 lines, the "Round 3a" report on 12, and computer files (`f1_lattice.py`, `checks_final.py`, …) on 32. The word "draft" occurs on 87 lines. VERIFIED (Appendix A).
- Whole sections record corrections to drafts: [B] §9, [NV] §§0, 7, [G] §§0, 10, and [R] §5 with its Appendix. VERIFIED.

In an outline these become numbered lemmas of the outline itself, or citations of published work. Take a statement labelled "VERIFIED (`f2_clamp_test.py`, 19,537,612 instances)". It should be replaced by the hand proof that the same file gives ([R] Lemma 4.3 has one), with the enumeration in a footnote at most. The first person and the comparisons with drafts belong to the refereeing record.

### 1.2 Dimension counts written as an economy

[S] and the files describe index and energy counts in the language of payment. Each such sentence is an inequality and should be written as one.

| as written | where | write instead |
|---|---|---|
| "each brings a sphere of square $-4$ whose $\mu$-class costs every Seiberg–Witten stratum more energy than it supplies" | [S] l. 58–59 | "each copy of $W_B$ contains a sphere $S_i$ of square $-4$; cutting down by $\mu(S_i)$ raises the charge of the moduli space by less than the energy it forces on a reducible" |
| "Regard $\kappa$ as the energy available; a stratum spends $-v^2/4$ on its reducible and $\ell$ on bubbles" | [S] l. 102–103 | "a Seiberg–Witten stratum $\iota(M_{\mathfrak s})\times\mathrm{Sym}^\ell(X)$ lies at level $\ell=\kappa+\frac14v^2$" |
| "a degree-two insertion supplies $\frac14$, or $\frac18$ with a parameter" | [S] l. 104–105 | "cutting down by a class of degree two raises by $\frac14$ the charge $\kappa$ at which the cut-down moduli space has dimension zero; over a one-parameter family of metrics it raises it by $\frac18$" |
| "its positive direction supplies $\frac38$"; "the $\frac12$ it saves its neighbours" | [S] l. 143, 152–153 | "raising $b^+$ by one raises that charge by $\frac38$"; "a class on $P$ may pair nontrivially with both adjacent spheres at energy $\frac12$ rather than $1$" |
| "costs $3$", "costs at least $1+3+1$" (at a central flat connection) | [B], [G], [R] | "adds $h^0(\theta)=3$ to the index" (additivity of the index) |
| "a point of concentration costs $8$ and releases at most $2$" | [G] §4.5 | "a point of concentration lowers the dimension by $8$, and the constraints supported at that point have total codimension at most $2$" |
| "each insertion supplies charge $\frac18$ but costs at least $\frac12$" | [R] §4.4 | "each sphere raises $\kappa$ by $\frac18$, and raises by at least $\frac12$ the energy of every reducible that lies in $V_{S_i}$" (Proposition 6.1 below) |
| "the insertion", "a met insertion", "assigned insertions" | all files | "the constraint $V_{S_i}$" or "the class $\mu(S_i)$"; "a reducible lying in $V_{S_i}$"; "the constraints carried by the component" |

"Insertion" is the language of correlation functions. Donaldson and Kronheimer–Mrowka speak of cutting down by a divisor representing $\mu(\Sigma)$. The word occurs on 64 lines. VERIFIED (Appendix A).

**The slogan of [S] Step 3.** It has a precise form, which is also more illuminating, and that form should replace it:

> Over a one-parameter family of metrics, the constraint $V_{S_i}$ raises by $\frac18$ the charge at which the family moduli space has dimension zero, half of what it requires at a fixed metric. It still raises by at least $\frac12$ the energy of every reducible that satisfies it.

With $n$ spheres and $m$ positive pieces this gives three counts:
- the charge is $8\kappa=n+3m+O(1)$;
- the Dirac index is $n_a=\frac18(5m-n)+O(1)$;
- every reducible has $\ell-T(v)\le\frac18(7m-3n)+O(1)$.

So $n_a\to\infty$ and the exclusion of reducibles hold together exactly in the range $\frac15<m/n<\frac37$. At a fixed metric the same counts give $8\kappa=2n+3m+O(1)$. Then $n_a\to\infty$ needs $m/n>\frac25$ and exclusion needs $m/n<\frac27$, an empty range: that is why a family is needed. VERIFIED (I redid the arithmetic from $n_a=\Theta-\kappa$, $\Theta=m+O(1)$, and the energy bound $-\frac14v^2+T(v)\ge\frac12(n-m)-C$ of [R] §4.4).

### 1.3 Invented labels

| label | file | meaning | replacement |
|---|---|---|---|
| types F, A, S, R | [R] (33 lines) | the kinds of components of an ideal limit | Feehan–Leness's terms: irreducible pair with nonzero spinor; irreducible zero-section pair (anti-self-dual); reducible pair (Seiberg–Witten); reducible zero-section pair (abelian instanton). VERIFIED that these are FL's terms ([FL2b] source, lines 1412–1413, 1524–1525) |
| excess $E_\beta$; excesses $\epsilon_I,\epsilon_C,\epsilon_S$ | [G] §5, [R] §3.1 | expected dimension of the cut-down problem on a piece or chain, with or without its parameters | "expected dimension", e.g. $\operatorname{ind}^{\rm asd}(\Gamma)$, $\operatorname{ind}^{\rm mon}(\Gamma)$ |
| segment | [R] (34 lines) | a maximal chain of consecutive reducible components between broken necks | "a chain of reducible components", defined once |
| losses $\Lambda_{\rm loss}$ | [R] §3.4 | codimension of a lower stratum | "the codimension of the stratum" |
| assigned insertions; allocated neck charge; reserved far halves | [R] | | "the constraints $V_{S_i}$ carried by the component"; "the charge on the broken neck"; "the halves $F_{l,j}$, $F_{r,j+1}$ adjacent to $P$" |
| unmatched limit | [R] §3.4 | solutions on the pieces with no matching condition at the broken necks | as in the meaning column |
| necessary projection (A7) | [R] | transversality of the problem obtained by forgetting the abelian components | "transversality after forgetting the abelian-instanton components" |
| coupled regularity (A3) | [R] | transversality of the product problem, modulo the gauge groups and the diagonal circle | "transversality of the product problem" |
| the band; the cusp | [R] Prop. 4.2 | the Weitzenböck inequality on $P$; the estimate on the tube $S^2\times S^1\times[0,L]$ | "the Weitzenböck inequality"; "the estimate on the long tube" |
| the clamp | [NV], [G], [R] | control of the Seiberg–Witten classes on $P$, uniformly over $\bar Q$ | [R]'s own phrase: "control of the Seiberg–Witten classes on $P$" |
| family adjunction inequality | [NV], [R] | $\kappa_\Gamma\ge\frac12(s^-+m)$ | "the energy bound for reducibles in $V_{S_i}$". It comes from the lattice and, on $P$, from the control of Seiberg–Witten classes; no genus enters, so "adjunction" misleads. VERIFIED ([R] Lemma 4.4 and its proof) |
| numerology; window; density; per block; per period | [R], [NV], [S] | dimension count; the range $\frac15<m/n<\frac37$; for each factor of $u$ | as in the meaning column |
| $Y$-necks (20 lines); central matching | [G] | the necks along the copies of $Y_{\pm2}$; matching at a central flat connection | as in the meaning column |
| admissible datum $\mathfrak D$ | [G] Def. 1.3 | metrics, perturbations, divisors, orientations and neck length | "auxiliary data". In Kronheimer–Mrowka's usage, which [NV] §1.1 also follows, "admissible" refers to a bundle whose $w_2$ is nonzero on some surface. VERIFIED |
| face condition (D5); tensor-paired | [G] | transversality of the half moduli spaces to the face divisors; related by tensoring with $L_y$ | as in the meaning column |
| return, no return | [NV] §4, [S] l. 160 | a cobordism $Y_2\to Y_{-2}$ or $Y_{-2}\to Y_2$ | name the cobordism |
| letters $a$, $d$; words $w$ | [NV] §5 | $\phi_*B$, $HB$ and their composites | write composites as composites of maps; $w$ is the determinant class |
| labelled construction | [NV] §4 | the manuscript's Fukaya–Floer construction | define it, or cite it |
| certificate of invertibility | [NV] §2 | a computation modulo two that proves invertibility | "criterion" |
| spin shift, formal spin shift | [B] (9 lines) | $\frac18-\Theta$ | delete: it is not an invariant of the instanton map |
| sector, relative sector | [G] | component of the configuration space with given limits | as in the meaning column |
| cap (for an ASD connection on $\nu(S)$); minimal cap; trace state; central state | [B], [G], [R] | | keep "cap" for a four-manifold bounding $\pm Y$; write "the reducible of energy $\frac14$ on $\nu(S)$", "the flat connection $\gamma$", "a central flat connection" |
| positive cell | [G] | positive piece | "positive piece" throughout |
| closed prototype; the hardest point; route | [S], [R], [B], [NV] | | "the closed case"; "the main analytic difficulty"; "argument" |

**Standard terms that should stay:**
- from Feehan–Leness: spin$^u$ structure, level, Donaldson and Seiberg–Witten strata, link, intersection-suitable;
- from Donaldson: jumping-line divisor;
- from Kronheimer–Mrowka: family of broken metrics, cut, $I$-orientation (VERIFIED: [KM11] source, `def:I-orientation` at l. 2381, and §3.9); tight surface (from their Property P paper);
- from Daemi–Lidman–Miller Eismeier: level and filtered map;
- "distance four", once $\Delta(2,-2)=4$ has been said.

### 1.4 One symbol, several meanings

| symbol | meanings | where | proposal |
|---|---|---|---|
| $\iota$ | involution of $C(Y_{\pm2})$ induced by the flat line bundle $\chi$; inclusion of the Donaldson and Seiberg–Witten strata | [B], [NV], [G]; [R] following FL | keep FL's $\iota$; write $\chi_*$ for the involution |
| $\Phi$ | the counts $\Phi_c$, $\Phi_e$; the spinor | [B], [G]; [R], [S] | keep $\Phi$ for the spinor; write KM's $m_{G,c}$ for the counts |
| $K$ | the knot; basic classes and $c_1(\mathfrak s)$ | everywhere; [B] §3, [NV] §4, [R] §4.3, [S] Steps 4–5 | keep $K$ for the knot; write $c_1(\mathfrak s)$ |
| $H$ | the map of $W_H$; the period point | everywhere; [S] l. 146, [R] §4.3 | write $\omega_g$ for the period point |
| $C_{\pm2}$ vs $C_\pm$ | punctured traces; caps | [NV] §3, [G] Notation; all files | write $X^\circ_{\pm2}$ for the punctured traces |
| $N$ | $\nu(S)$; negative piece; exponent in $2^N$; nilpotent block; number of components | [B], [G]; [R]; [S], [NV], [G]; [NV]; [R] §3.4 | keep $\nu(S)$; write $\hat Z_j$ for the pieces; drop $2^N$ (§6.2(iv)) |
| $s$ | relative sign; number of constraints on a chain; "energy supplied"; binary digit sum | [B], [G]; [R] §3.1; [S] l. 128; [NV] | $\epsilon$ for the sign |
| $m$ | number of positive pieces; the signs $m_c$, $m_e$, which also clash with KM's $m_G$ for the map of a family | [S], [NV], [R]; [B], [G] | keep $m$ for the number of positive pieces and $m_G$ for maps of families |
| $w$ | determinant class; composite ("word") | all; [NV] §5 | do not call composites $w$ |
| $u$ | $(\phi_*B)^3HB$; $v\cdot U$; handle maps $u_0$, $u_1$ | all; [R] §4.3; [B] §4 | keep $u$ for the composite |
| $L$ | $\partial\nu(S)$; $I(Y;\mathbb Z)/\mathrm{Tors}$; number of pieces; level; line bundles | [G]; [NV], [G]; [R]; [B]; [B], [R] | e.g. $\bar I(Y)$ for $I(Y;\mathbb Z)/\mathrm{Tors}$ |
| $Q$ | the cube; the intersection form | [G], [R]; [B], [NV] | $Q_X$ for the form |
| $\Omega$ | the family invariant; a symplectic form | all; [NV] §4 | $\omega$ for the symplectic form |
| $E$ | energy; "excess" $E_\beta$; bundles $E_e$; exceptional classes $E_\pm$ | [B], [G]; [G]; [G], [R]; [R] | keep $E$ for bundles only |
| $T$ | neck length; $T(v)$; classes $T_b$; a cobordism; a formal variable | [G]; [S], [R]; [G], [R]; [NV] Thm. 4.4(b1); [NV] §2 | at least separate $T(v)$ from the neck length |
| $J$ | the middle three-sphere; continuation maps $J_{\pm2}$; Jones polynomial $J_K$ | all; [B] §4; [NV] Cor. 5.3 | keep $J$ for the three-sphere |
| $\Lambda$ | $c_1(\mathfrak t)$; $\log A$; orientation lines | [S], [R]; [NV] Lemma 2.3; [B] Lemma 2.5 | keep FL's $\Lambda$ |
| $\gamma_0$, $\gamma$, "trace state" | the trace-zero flat connection on $L(4,1)$ | [B]; [G]; [R] | one symbol, $\gamma$ |
| $n_D$, $n_a$ | the complex index of the Dirac operator | [S], [NV]; [R] | FL's $n_a$ throughout, since the proofs follow [FL2b] |
| $W'$ | $(-X_2^\circ)\cup_{S^3}X_{-2}^\circ$ | all | $W_B$, parallel to $W_H$; the prime suggests a missing $W$ |
| Theorem A, B, C; (B1), (B2) | three Theorems A. Proposition B, Corollary B, Theorem B and the map $B$. (B1)–(B2) are properties of $B$ in [NV] but hypotheses of Theorem B in [R] | all | number statements by section in the outline |

VERIFIED: each entry was located in the file named.

### 1.5 Hypotheses

The four files name about forty-four hypotheses:
- [NV]: (T), (Gl), (B1), (B$_\mathbb Q$), (B2′), (B2), (B2\*), (G), (F), (N);
- [R]: (A1)–(A7), (A7′), (E0), (E), (B1)–(B5), (J1)–(J4);
- [G]: (D1)–(D8), (I1)–(I4);
- [B]: (J1)–(J3).

VERIFIED. Feehan and Leness state a conditional theorem as "Assume Hypothesis 7.8.1 holds". The outline should do the same, with five hypotheses:

- **(H1)** Floer theory at $Y_{\pm2}$ over $\mathbb Z$, where every reducible flat connection is central; maps of cobordisms with $b_1=0$; and the meridional handle maps are isomorphisms over $\mathbb F_2$. [NV (T), (Gl); G §7.2(1)]
- **(H2)** $B\otimes\mathbb Q$ is an isomorphism. [NV (B$_\mathbb Q$); B Conjecture C]
- **(H3)** Witten's formula for the closed symplectic manifold $X_0\supset Y_0$ of Kronheimer–Mrowka (*Witten's conjecture and Property P*, Prop. 15). [NV §4; rests on FL Memoir Hyp. 7.8.1]
- **(H4)** Gluing at irreducible nondegenerate limits and at the reducible of energy $\frac14$ on $\nu(S)$, with orientations over $\mathbb Z$. [B Lemmas 2.4–2.5; G Gaps 1–4]
- **(H5)** The analytic hypotheses of the vanishing theorem in families, together with the control of Seiberg–Witten classes on $P$ and the estimates on the caps. [R (A1)–(A7), Prop. 4.2, Lemma 4.6]

The remaining items, (J1)–(J4), (D1)–(D8) and (I1)–(I4), are lemmas or definitions and should be stated as such.

---

## 2. The map $B$ ([B])

### 2.1 Interest

**Theorem A.** [B] Theorem A constructs, for every knot, an integral chain map $C(Y_2)\to C(Y_{-2})$ between the surgeries at distance four. It does so in the manner of the maps of the surgery exact triangles, and of the distance-two map $g_1$ of Daemi–Lidman–Miller Eismeier. That is of intrinsic interest.

As stated it is not yet attractive, for three reasons (VERIFIED, by reading):
- it has five parts, and part (b) is a lemma;
- part (d) concerns the Chern–Simons filtration and the Dirac index $\Theta$, neither of which has anything to do with the chain property;
- the property a reader wants, that $B$ is an isomorphism, is only a conjecture, stated two sections later (Conjecture C).

**Proposition B** is a pleasant statement. It belongs with the relations for spheres of square $-1$ (Kotschick), $-2$ (Ruberman) and $-3$ (Fintushel–Stern), and [B]'s table of the four relations (§3) is the clearest page of the file.

**Corollary 4.4** is, of all the statements in the four files, the closest to a theorem: a necessary condition for a cosmetic pair $\pm2$ that depends only on (H1).

### 2.2 Formulation

**Lead with the conceptual description.** [B] gives it only in Theorem A(e) and §5, and [S] in Step 4:

> At a fixed metric, the map $\mu(S)\cdot W_{B*}$, which counts index-two instantons in $V_S$, is a chain map of degree $-2$. It is null-homotopic for two independent reasons:
> - stretching $J\cong S^3$, because the only flat connection on $S^3$ is trivial and has a three-dimensional stabilizer;
> - after the signed sum over the bundles with $c_1=c$ and $c+\mathrm{PD}(S)$, stretching $\partial\nu(S)\cong L(4,1)$, because the two bundles agree off $\nu(S)$ and their reducibles of energy $\frac14$ on $\nu(S)$ contribute with opposite signs.
>
> $B$ is the difference of the two null-homotopies.

VERIFIED as a reading of [B] Theorem A(e) and [G] §3.3.

**Then state the theorem in Kronheimer–Mrowka's notation.** [KM11] §3.9 defines the map $m_G$ of a family of metrics $G$ and proves $m_{\partial G}+(-1)^{\dim G}m_G\circ\partial=\partial\circ m_G$ (VERIFIED, source lines 2536–2548):

> **Theorem 2.1.** Let $K\subset S^3$ be a knot. Let $W_B=(-X_2^\circ)\cup_JX_{-2}^\circ\colon Y_2\to Y_{-2}$ with $J\cong S^3$, and let $S\subset W_B$ be the sphere formed by the cores of the two $2$-handles, so that $S\cdot S=-4$ and $\partial\nu(S)\cong L(4,1)$. Let $G=[0,1]$ parametrize metrics on $W_B$ that are broken along $J$ at $0$ and along $\partial\nu(S)$ at $1$, and let $V_S$ be the jumping-line divisor representing $\mu(S)$. For $c\in H^2(W_B;\mathbb Z)$ vanishing on $Y_{\pm2}$, let $m_{G,c}\colon C(Y_2;\mathbb Z)\to C(Y_{-2};\mathbb Z)$ count the instantons over $G$, on the $U(2)$-bundle with $c_1=c$, that lie in $V_S$. Then there is a sign $\epsilon$, depending only on orientation conventions, such that
> $$m_G=m_{G,c}-\epsilon\,m_{G,c+\mathrm{PD}(S)}$$
> is a chain map of degree $-1-2c^2\pmod 8$. Its chain-homotopy class does not depend on the choices. Changing $c$ changes it, up to sign and homotopy, by composition with $\chi_*$ on either side. Put $B=m_G$ for $c=0$.

*Proof from the right lemmas.* With $\dim G=1$, KM's formula reads
$$\partial m_{G,c}+m_{G,c}\partial=m_{\{1\},c}-m_{\{0\},c},$$
where $m_{\{t\},c}$ counts index-two solutions in $V_S$ for the broken metric at $t$.
- At $t=0$, every broken solution with irreducible limits has index at least $3$, since the matching at the trivial connection on $S^3$ adds $h^0=3$ ([B] Lemma 2.2). So $m_{\{0\},c}=0$.
- At $t=1$, the only broken solutions of index two in $V_S$ are a rigid irreducible solution on $W_B\setminus\nu(S)$ with limit $\gamma$ on $L(4,1)$, glued to the reducible of energy $\frac14$ on $\nu(S)$, which meets $V_S$ with local degree $\pm1$ ([B] Lemmas 1.2, 2.3). So $m_{\{1\},c}=\epsilon_c R$, where $R$ does not depend on $c$ because $\mathrm{PD}(S)$ vanishes off $\nu(S)$.

If $\epsilon_{c+\mathrm{PD}(S)}=\epsilon\,\epsilon_c$, the signed sum has no boundary term. ∎

PLAUSIBLE. The dimension counts are VERIFIED in [B] §§2.1–2.3; the gluing at $\gamma$ and the constancy of $\epsilon$ are (H4).

### 2.3 Generality

The generality is right as stated: every knot, and slopes exactly $\pm2$. A sentence should say why these slopes are special. The construction uses three facts:
- (i) every reducible flat connection on $Y_{\pm2}$ is central, since $H_1=\mathbb Z/2$;
- (ii) the flat connections on $L(4,1)$ are nondegenerate, and the smallest framed index of a non-flat ASD connection on $\nu(S)$ with $w_2=0$ is $2$. So one constraint of codimension two supported in $\nu(S)$ makes the face at $t=1$ rigid, and that constraint must be $\mu(S)$, because $H_2(\nu(S))=\mathbb Z[S]$;
- (iii) $\mathrm{PD}(S)=2y$ on $W_B$, so the two bundles differ by a flat line bundle off $\nu(S)$.

For $\pm p$ with $p\ge3$, (i) fails: $S^3_{\pm p}(K)$ carries reducible flat connections with stabilizer $U(1)$. VERIFIED: (i) is [B] §1.2; (ii) is [B] Lemma 1.2, §5(2) and [G] Lemma 4.4; (iii) is [B] Lemma 1.1; the failure for $p\ge3$ is [G] §7.1.

**Remove from the theorem:**
- part (b), which is Lemma 2.2;
- part (d). Its filtered statements become one remark explaining why the Chern–Simons filtration gives nothing for $B$ ($L-D/8=\frac18-\eta$ has no known sign). Its "spin" item belongs to the Dirac-index count of §6 of the outline.

### 2.4 The closed relation, and the grading constraint

> **Proposition 2.2.** Let $X$ be closed, oriented and simply connected with $b^+\ge2$. Let $S\subset X$ be an embedded sphere with $S\cdot S=-4$, and let $w\in H^2(X;\mathbb Z)$ with $w\cdot S$ even. Then
> $$D^{w+\mathrm{PD}(S)}_X(Sz)=-D^w_X(Sz)$$
> for every $z$ in the subalgebra generated by the point class and $S^\perp$.

*Proof for simple type.*
- Write $\mathbf D^w_X=e^{Q_X/2}\sum_K(-1)^{(w^2+K\cdot w)/2}a_Ke^{K}$ (structure theorem).
- Since $(w+\mathrm{PD}S)^2=w^2+2w\cdot S-4$ and $w\cdot S$ is even, replacing $w$ by $w+\mathrm{PD}(S)$ multiplies the sign of the $K$-term by $(-1)^{K\cdot S/2}$.
- Differentiating along $S$ at a point of $S^\perp$ multiplies the $K$-term by $K\cdot S$. So the sum $D^{w+\mathrm{PD}S}(S\,\cdot)+D^w(S\,\cdot)$ receives contributions only from basic classes with $K\cdot S\equiv0\pmod4$ and $K\cdot S\neq0$. By the Fintushel–Stern inequality for spheres, these have $K\cdot S=\pm4$.
- Fintushel and Stern pair these classes: those with $K\cdot S=-4$ are exactly the $K+2\,\mathrm{PD}(S)$ with $K\cdot S=4$, and they have the same coefficient.
- Paired classes have the same restriction to $S^\perp$, the same sign and opposite values of $K\cdot S$, so their terms cancel. ∎

VERIFIED as a deduction; I recomputed the sign change. The two Fintushel–Stern facts are as checked against [FS-RB, Thms. 4.1, 4.3] in [B] §9.3, together with $a_{-K}=\pm a_K$, which [B] cites from memory.

> **Corollary 2.3 (grading constraint).** Assume (H1). Suppose there is a cobordism $V\colon Y_{-2}\to Y_2$ with $b_1(V)=b^+(V)=0$ that induces an isomorphism on $I(\,\cdot\,;\mathbb F)$ for the trivial bundle, where $\mathbb F=\mathbb F_2$ or $\mathbb Q$; for instance, the mapping cylinder of an orientation-preserving diffeomorphism. Then $\dim I_j(S^3_2(K);\mathbb F)$ is independent of $j\in\mathbb Z/8$. In particular $\dim I(S^3_1(K);\mathbb F)\equiv0\pmod8$ and $\Delta''_K(1)=0$.

*Proof.*
- $V_*$ has degree $0$. $H$ has degree $-2c_H^2-3$, which is odd because $b^+(W_H)=1$.
- So $H\circ V_*^{-1}$ is an automorphism of $I(Y_2;\mathbb F)$ of odd degree, and odd numbers generate $\mathbb Z/8$.
- The isomorphism $I(Y_1)\cong I(Y_2)$ has even degree, so the Euler characteristics agree, and $\chi(I(Y_1))=\pm2\lambda(Y_1)=\pm\Delta''_K(1)$. ∎

VERIFIED given (H1) and the degree formula. The degree formula is VERIFIED for the mapping cylinder, and PLAUSIBLE for general $V$ by the index additivity of [NV] §1.2. The statement should be made in this generality, which is [NV] Proposition 5.4's. Whether the condition modulo $8$ is new is SPECULATIVE; both files say it "appears to be new".

### 2.5 Conjecture C

Only (H2) is used later. Conjecture C as written introduces $\vartheta$, $H''$, $f^{(1)}_\pm$, $J_{\pm2}$, $\tau$ and "end twists". Its content fits in a sentence that a reader of Daemi–Lidman–Miller Eismeier will recognize:

> **Conjecture 2.4.** Over $\mathbb F_2$, $B$ is chain homotopic to $g_-\circ g_+$. Here $g_+\colon C(Y_2)\to C(Y_0^w)$ and $g_-\colon C(Y_0^w)\to C(Y_{-2})$ are the distance-two maps of [DLME, Prop. 3.10] for the triads $(Y_2,S^3,Y_0)$ and $(Y_0,S^3,Y_{-2})$, composed through the identification at $Y_0$ fixed by the family. In particular $B\otimes\mathbb F_2$ is an isomorphism, and hence so is $B\otimes\mathbb Q$.

[B] Proposition 4.1 should stand beside it. For the bundle $c_H$ used later, $\deg H\equiv-3$ and $\deg HB\equiv4$. So "$B$ inverts $H$" is false for that bundle, and that is harmless, since only the invertibility of $B$ is used. VERIFIED ([B] Prop. 4.1; [NV] Prop. 3.1(4) agrees). The implication from $\mathbb F_2$ to $\mathbb Q$ is [NV] Lemma 2.1 (VERIFIED: an integral chain map that is a quasi-isomorphism modulo two has a cone with finite homology of odd order).

### 2.6 Further terms in [B]

| as written | write instead |
|---|---|
| "the $\mu(S)$-cut count", "$\mu(S)$-cut interval counts" | "the count over $G$ of instantons in $V_S$" |
| "lifts" (46 lines) | define once: "an integral lift $c$ of $w_2=0$, that is, a $U(2)$-bundle with $c_1=c$, with the determinant-one gauge group"; then "the bundle $c$" |
| "the twist $\iota$", "end twists" | "the involution $\chi_*$", "the involutions induced by $\chi$ on the ends" |
| "framed cap", "reducible cap", "minimal cap" | "framed ASD connection on $\nu(S)^\wedge$", "the reducible of energy $\frac14$" |
| "the period $t^{-1}$" | "the factor $t^{-1}$" |
| "favourable", "trivial-middle variation" | for the first, cite "satisfies the inequality of [DLME, Lemma 2.7(b)]"; drop the second |
| "four-step family", "compressed pentagon", "two-step identities", "slope vectors", "arc cuts" | define them through the polygon families of Culler–Daemi–Xie, or cite numbered lemmas |
| "Route 1", "Route 2" | "first argument", "second argument" |
| "the secondary map of the two vanishings" | keep, after the paragraph of §2.2 |

---

## 3. Nonvanishing ([NV])

### 3.1 Interest

- **Theorem 1** (the title theorem).
  - Part (i) says that a linear recurrence with nonzero constant coefficient, whose initial term is nonzero, cannot vanish at $r$ consecutive terms.
  - Part (ii) is Skolem's method at the prime $2$, with a sharp bound on the number of zeros.

  Neither concerns gauge theory, and [NV] itself says that only (i) is used. VERIFIED ([NV] §0(1), Remark 3.2(4)). For the reader of this outline it has no intrinsic interest: (i) is a three-line lemma and (ii) a digression.
- **Corollary 2** is natural once stated plainly. *For a negative-definite cobordism $W\colon Y\to Y$, the Donaldson invariants of $C_-\cup W\cup\cdots\cup W\cup C_+$ (with $M$ copies of $W$) satisfy the linear recurrence given by the characteristic polynomial of $W_*$ on $I(Y;\mathbb Q)$.* That is a pleasant remark.
- **Propositions 4.1–4.2 and Theorem 4.4** are of genuine interest, and natural: they adapt Kronheimer and Mrowka's argument for Property P to $Y_{\pm2}$. The genus enters once, through a short argument a reader will enjoy:
  - $(K_\omega+2t\,\mathrm{PD}\hat\Sigma)^2=K_\omega^2+4t(2g-2)$;
  - so for $g\ge2$ the class $K_\omega+2t\,\mathrm{PD}(\hat\Sigma)$ has a Seiberg–Witten moduli space of negative dimension when $t<0$, and of positive dimension when $t>0$ (excluded by simple type);
  - so the restriction of $\mathbf D^w_{X_0}$ to $\hat\Sigma^\perp$ has coefficient $\pm c(X_0)\,SW(K_\omega)\ne0$ at $e^{K_\omega}$.

  VERIFIED (I redid the computation).
- **Theorems 5.1–5.2 and Corollary 5.3** are the main theorem of the whole outline, conditional on the other three files. They do not belong in a section on nonvanishing.
- **Proposition 5.4** duplicates [B] Corollary 4.4, in the better generality (Corollary 2.3 above).

### 3.2 Formulation

> **Lemma 4.1.** Let $A$ be an invertible endomorphism of an $r$-dimensional rational vector space, $\psi_-$ a vector and $\psi_+$ a covector with $\psi_+(\psi_-)\ne0$. For every $k\ge1$, the sequence $\psi_+(A^{kM}\psi_-)$, $M\ge0$, does not vanish at $r$ consecutive values of $M$.

*Proof.* The characteristic polynomial of $A^k$ has nonzero constant term. So the sequence satisfies a recurrence of order $r$ that determines each term from the $r$ terms following it, and $r$ consecutive zeros would propagate back to $M=0$. ∎ VERIFIED.

> **Proposition 4.2 (caps, after Kronheimer–Mrowka).** Let $K$ be a knot of genus $g\ge2$, and let $X_0=X^-\cup_{Y_0}X^+$ be the closed symplectic manifold of Kronheimer–Mrowka (Prop. 15 of their Property P paper) containing $Y_0=S^3_0(K)$, with $w$ odd on the capped Seifert surface. Assume (H1) and (H3). Then there are classes $z_\pm$ supported in $X^\pm$ such that the caps $C_-=X^-\cup W_{0\to2}$ of $Y_2$ and $C_+=W_{-2\to0}\cup X^+$ of $-Y_{-2}$ satisfy
> $$\langle\Psi_{C_+}(z_+),\,H^{-1}\,\Psi_{C_-}(z_-)\rangle=\pm D^w_{X_0}(z_-z_+)\ne0\quad\text{in }\mathbb Q.$$

This is the clean form of [NV] Theorem 4.4(a). Once the caps pair nontrivially through $H^{-1}$, any invertible map can be inserted between them, by Lemma 4.1. VERIFIED as a restatement: the identity is gluing at the admissible $Y_0$, with $H=f_+f_-$, $\Psi_{C_-}=f_+\Psi_{X^-}$ and $\Psi_{C_+}=\Psi_{X^+}f_-$, as [NV] §4 says.

> **Corollary 4.3.** Assume (H1)–(H4) and $g(K)\ge2$, and suppose $\phi\colon Y_{-2}\to Y_2$ exists. Then for every $p_0$ there are $p\in 8\mathbb Z$ and a composite $\Pi_0$ of the maps $\phi_*B$ and $HB$ with the following properties:
> - $\Pi_0$ begins and ends with at least $p_0$ factors $\phi_*B$;
> - consecutive factors $HB$ in $\Pi_0$ are separated by at least three factors $\phi_*B$;
> - $\Omega\big(X(B\,\Pi_0\,u^M(\phi_*B)^p)\big)\ne0$ for infinitely many $M\in8\mathbb Z$.

*Proof.* This is [NV] Theorem 5.1, Steps 1–4: Cayley–Hamilton spaces out the factors $HB$, and Lemma 4.1 is applied twice. Then apply the composition law of §3. ∎ VERIFIED as logic (I re-read the four steps).

### 3.3 Generality

[NV] Theorem 5.1 excludes every cobordism $V\colon Y_{-2}\to Y_2$ with $b_1=b^+=0$, $w_2=0$ and $V_*\otimes\mathbb Q$ an isomorphism, not only diffeomorphisms. That is a more interesting statement than the cosmetic one, in the spirit of results on ribbon homology cobordisms.

But the vanishing side, [R] §4, uses the lattice of the negative piece $X_{-2}\cup_\phi(-X_2)$: the form $\langle-1\rangle^2$, with $F_r=a+b$ and $F_l=a-b$. It does so in [R] Lemma 1.1(b), Proposition 4.1 and Lemma 4.4. VERIFIED (by reading).

For a general $V$ with $H_1(V)=0$:
- the closed-up negative piece is negative definite with $H_1=0$, so its form is diagonal by Donaldson's theorem;
- the energy bound on a negative piece survives as an inequality;
- $\Theta$ is unchanged if $c_1(\mathfrak t)$ is $\pm1$ on the new diagonal classes;
- but $F_l$ and $F_r$ may now have disjoint supports ($e_1+e_2$ and $e_3+e_4$). That changes the parity argument for distinct $w_2$, and the contribution of a negative piece to $\Theta$.

PLAUSIBLE that the argument extends to $H_1(V)=0$; SPECULATIVE beyond that. **Recommendation:** state the main theorem for $\phi$, which is the generality the other files support, and state the extension as a remark that names what must be rechecked.

[NV] Theorem 5.2 (two-sided, any genus) depends, in genus one, on the undefined "labelled construction", and the cosmetic corollary does not need it. VERIFIED ([NV] §5, "How the genus enters"). Drop it from the outline, or state it as a remark.

### 3.4 Further terms in [NV]

| as written | write instead |
|---|---|
| "Persistence of Floer pairings under iteration"; "2-adically continuous in the number of iterations" | "Lemma 4.1"; omit the second |
| "the Kronheimer–Mrowka closure" | "the closed symplectic manifold of Kronheimer–Mrowka, Prop. 15" |
| "hypersurface numerics", "sextic numerics" | "the Euler characteristic and signature of a smooth hypersurface of even degree $\ge6$ in $\mathbb{CP}^3$" |
| "No return" / "With a return" | "Without a cobordism $Y_2\to Y_{-2}$" / "Given a cobordism $V'\colon Y_2\to Y_{-2}$ with …" |
| "What is needed of $B$" (Proposition 3.1) | a remark rather than a proposition; its content is that (H2) suffices |
| "Floer theory supplies the integrality and the mod-two certificate of invertibility" | "Floer theory provides integrality; a computation modulo two then proves invertibility" |
| "kind (a)", "kind (b)" | acceptable |

---

## 4. The composition law ([G])

### 4.1 Interest

The interest is modest, and the result is necessary. It is the closed, capped form of Kronheimer and Mrowka's composition law for families of broken metrics. VERIFIED: [KM11], equation `eq:chain-homotopy-faces`, expresses the face terms of a product family as composites $m''_j\circ m'_j$ with sign $(-1)^{\dim G''_j\dim G'_j}$, and [G] §9 says the same.

The one idea of independent interest deserves a remark of its own. When every neck along $Y_{\pm2}$ is long, a matching at a central flat connection adds $3$ to the index. So no gluing at a reducible is needed anywhere, except at the reducible of energy $\frac14$ on each $\nu(S_i)$. VERIFIED ([G] §0(1), §7.1).

### 4.2 Formulation

[G] writes its theorem in four parts. The third part (the ends of one-dimensional moduli spaces along a path of data) is a step of a proof. The natural statement is:

> **Theorem 3.2.** Let $X$ be a closed four-manifold obtained from copies of $W_B$, copies of $W_H$ and two caps $C_\pm$ (with $H_1=0$, $b^+\ge1$, carrying classes $z_\pm$), by gluing consecutive pieces along orientation-preserving diffeomorphisms of their ends, which are copies of $Y_2$ or $Y_{-2}$. Suppose that consecutive copies of $W_H$ are separated by at least three copies of $W_B$.
>
> Let $Q=G^n$, where $n$ is the number of copies of $W_B$. Let $g^T$ be the family over $Q$ in which the necks along the gluing three-manifolds have length $T$, except the two necks inside each $W_B\cup W_H\cup W_B$, which stay fixed.
>
> Then for $T$ large the weighted count $\Omega(X;g^T)$ is defined, and it is independent of $T$ and of the choices. Moreover
> $$\Omega(X;g^T)=\pm\big\langle\Psi_{C_+}(z_+),\,\Pi\,\Psi_{C_-}(z_-)\big\rangle .$$
> Here $\Pi$ is the composite, in order, of $B$ for each copy of $W_B$, $H$ for each copy of $W_H$, and the induced isomorphism for each gluing diffeomorphism.

PLAUSIBLE (70%, as in [G]); it combines [G] Theorem A(1), (2), (4) and Theorem A′.

### 4.3 Generality

- [G] Theorem A assumes the diffeomorphism $\phi$, which the outline proves cannot exist. A reader will find a theorem with an eventually contradictory hypothesis odd. The composition law holds, if at all, for every composite of the pieces along diffeomorphisms of the ends, and it has content without $\phi$, for instance for $(HB)^M$. Part (4) of [G] Theorem A nearly says so. VERIFIED (part (4) lists "copies of $W'$ …, $W_H$, $\phi$ and $\phi^{-1}$"). Including cobordisms $V$ with $b_1=b^+=0$ among the pieces is PLAUSIBLE: the trivial connection on $V$ has index $-3$ but forces two matchings at central flat connections, each adding $3$.
- Theorem A′ (finite necks inside the positive pieces, and at least three copies of $W_B$ between copies of $W_H$) is the version used downstream, and should be the theorem. Theorem A (all necks long) is a step. VERIFIED ([G] §0(6)).
- Corollary B (a congruence modulo $2^N$) should be deleted (§6.2(iv)).
- Proposition C (all Donaldson and Seiberg–Witten invariants of $X_M$ vanish) should become one sentence after the definition of $\Omega$, explaining why a family is needed.

### 4.4 Further terms in [G]

| as written | write instead |
|---|---|
| "Iterated composites and a secondary invariant: the gluing theorem" | "The family invariant and the composition law" |
| "admissible datum $\mathfrak D$", (D1)–(D8) | "auxiliary data", listed in a definition |
| "$Y$-necks"; "central matching"; "excess" | see §1.3 |
| "a met insertion"; "costs"; "releases" | see §1.2 |
| "secondary invariant" | acceptable with one sentence of definition: "it is defined by a family of metrics whose faces contribute zero in total". Otherwise "the family invariant" |
| "the nodal algebra" | "the computation on the nodal curve" |
| "with the chain maps of $\mathfrak D$" | "at chain level, for the chain maps defined by the same data" |

---

## 5. The vanishing theorem in families ([R])

### 5.1 Interest

[R] Theorem A is, for a gauge theorist, the most interesting statement in the four files. It is the vanishing theorem of Feehan and Leness, [FL2b] Thm. 3.33(a), for a family of metrics parametrized by a cube whose faces split $X$ along $S^3$ and along $L(4,1)$. It is proved as the original is, by Stokes' theorem on the cut-down one-manifold of $\mathrm{SO}(3)$-monopoles, and without gluing at reducibles. It is formulated in Feehan and Leness's own terms: $\mu_p$, $\mu_c$, the link of the Donaldson stratum, levels, and the strata $\iota(M_{\mathfrak s})\times\mathrm{Sym}^\ell$.

VERIFIED against the [FL2b] source:
- "Donaldson stratum $\iota(M^w_\kappa)$" and "Seiberg–Witten strata $\iota(M_{\mathfrak s})$" are at lines 1412–1413;
- Theorem 3.33(a), at lines 4907–4935, assumes $(c_1(\mathfrak t)-c_1(\mathfrak s))^2<p_1(\mathfrak t)$ for every $\mathfrak s$ with $M_{\mathfrak s}\ne\emptyset$, "so $\bar{\mathcal M}_{\mathfrak t}$ contains no reducible monopoles", and concludes $\#(\bar{\mathcal V}(z)\cap\bar M^w_\kappa(X))=0$.

Theorems B and C are technical. They are hard to read because of the invented vocabulary of §1.3, not because of their content, which rests on one lattice inequality (Proposition 6.1 below).

[R] also records a point that the Strategy missed, in Step 4 of its proof of Theorem A. Broken limits whose components are all irreducible, some of them with zero spinor, need transversality of the product problem; the Dirac operator of a zero-spinor component can have cokernel. VERIFIED (by reading). This belongs in (H5). It does not arise in the closed case, [S] Theorem 2.1, which has no broken limits.

### 5.2 Formulation

> **Theorem 5.2 (vanishing in families).** Let $X$ be a closed, oriented, simply connected four-manifold with $b^+(X)\ge1$, containing:
> - disjoint separating three-spheres $J_1,\dots,J_n$;
> - disjoint embedded spheres $S_1,\dots,S_n$ with $S_i\cdot S_i=-4$, such that $S_i$ meets $J_i$ in a knot and misses $J_j$ for $j\ne i$.
>
> Write $[S_i]=F_{l,i}-F_{r,i}$ for the classes of its two halves, each of square $-2$. Let $\{g_t\}_{t\in\bar Q}$, with $\bar Q=[-1,1]^n$, be a family of metrics that stretches $J_i$ as $t_i\to-1$, and stretches $\partial\nu(S_i)\cong L(4,1)$, with a metric of positive scalar curvature, as $t_i\to+1$.
>
> Let $\mathfrak t_e$, $e\in\{0,1\}^n$, be spin$^u$ structures with $w_2(\mathfrak t_e)\equiv w_0+\sum_ie_i\,\mathrm{PD}[S_i]$ and $p_1(\mathfrak t_e)$ independent of $e$. Here $w_0$ is even on every half and odd on some class orthogonal to all the $S_i$, and $\langle c_1(\mathfrak t_0),S_i\rangle=2$ for all $i$, so that $n_a$ does not depend on $e$. Assume $n_a\ge1$. Let $z=\mu(S_1)\cdots\mu(S_n)\,z'$ with $\deg z=d_a+n$, and let $\Omega$ be the weighted count over $Q$ of instantons in $\mathcal V(z)$.
>
> Suppose that for every $e$ the closure over $\bar Q$ of the cut-down one-manifold of $\mathrm{SO}(3)$-monopoles contains no ideal monopole that is reducible on one of the pieces into which the broken necks cut $X$. (The reducibles of energy $\frac14$ on the $\nu(S_i)$ are allowed.) Then, assuming (H5), $\Omega=0$.

Remarks to go with it:
- **The conclusion.** It should read $\Omega=0$, as Feehan and Leness write their conclusion as a count equal to zero. The factor $2^{n_a-1}$ belongs to the proof, where Stokes' theorem with rational weights gives $2^{n_a-1}\Omega=0$ in $\mathbb Q$. VERIFIED ([FL2b] Thm. 3.33(a); [R] Remark 2.2(4)).
- **Finiteness.** [R] lists as a hypothesis, (E0), that the instanton count is finite. That is part of the definition of $\Omega$, and for the family of the outline it is supplied by the composition law (Theorem 3.2). VERIFIED ([R] Remark 2.2(5); [G] Theorem A(1)).
- **Special cases first.** The case $n=0$ is [FL2b] Thm. 3.33(a), with its hypothesis weakened from "no reducible at any level" to "the closure of the one-manifold meets none". The case of $n$ spheres without a family is [S] Theorem 2.1. Both should be stated before the family version. VERIFIED ([R] Remark 2.2(1); [S] §2).
- **(A3) and (A7).** These should be stated as transversality statements. For every ideal limit of the given kind, the product of the moduli spaces of its components — with their constraints and remaining parameters, modulo the gauge groups and the diagonal circle — is cut out transversely after a small multivalued perturbation. The same holds after forgetting the abelian-instanton components.

### 5.3 The lattice inequality at the heart of Theorems B and C

> **Proposition 6.1.** Let $X$ be as in Theorem 5.2, and let $v\in H^2(X;\mathbb Z)$ with $v\equiv w_0\pmod2$. Suppose the halves are pairwise orthogonal, and let $\pi$ be the orthogonal projection to the complement of their span. Then
> $$-\tfrac14v^2\ \ge\ -\tfrac14(\pi v)^2+\tfrac12\,\#\{i:\langle v,S_i\rangle\ne0\}.$$

*Proof.*
- Since the halves are orthogonal of square $-2$, $\;-v^2=-(\pi v)^2+\frac12\sum_i\big(\langle v,F_{l,i}\rangle^2+\langle v,F_{r,i}\rangle^2\big)$.
- The evaluations of $v$ on the halves are even, because those of $w_0$ are.
- If $\langle v,S_i\rangle=\langle v,F_{l,i}\rangle-\langle v,F_{r,i}\rangle\ne0$, one of the two evaluations is a nonzero even number, so the $i$-th term is at least $2$. ∎

VERIFIED (the proof of [S] Theorem 2.1(b), redone).

**How it is used.** A reducible with $\langle v,S_i\rangle=0$ satisfies the constraint $V_{S_i}$ only if it has a point of concentration on $S_i$, by the jumping-line property. Combined with Proposition 6.1 this gives $\ell\ge T(v)$, and then the bound $\ell-T(v)\le\kappa-\frac12(n-m)+O(1)$ that drives Theorem C.

On a positive piece $P$ the orthogonal complement of the two adjacent halves is indefinite, so $-(\pi v)^2$ has no sign there. [R] Lemma 4.4 therefore replaces the proposition by a bound for each piece, using the control of Seiberg–Witten classes on $P$. The point to explain to the reader is that a class on the indefinite piece $P$ can pair nontrivially with both adjacent spheres at energy $\frac12$ instead of $1$. VERIFIED ([R] Lemma 4.4 and its proof, read).

> **Theorem 6.4 (no reducible limits).** Let $X=X(B\,\Pi_0\,u^M(\phi_*B)^p)$ be the closed manifold of a composite from Corollary 4.3, with the caps of §4 blown up once and $|\langle c_1(\mathfrak t),e_\pm\rangle|$ large and odd on the exceptional classes. Assume (H5), and the control of Seiberg–Witten classes on the positive pieces and the cap estimates, uniformly over $\bar Q$ and in the neck length. Then for all sufficiently large $M$ in the congruence class for which $c_2$ and $n_a$ are integers, $n_a\ge1$ and the hypothesis of Theorem 5.2 holds. Hence $\Omega(X)=0$.

[R] Theorem C is stated for $X_M$ built from $u^M$ with $p_\pm$ factors $\phi_*B$ at the two ends. The nonvanishing, however, uses composites $B\,\Pi_0\,u^M(\phi_*B)^p$ with an arbitrary fixed $\Pi_0$. VERIFIED (the two files use different composites). [R] Lemma 4.5 notes that longer gaps between positive pieces only help, so the extension is PLAUSIBLE, and it should be the statement.

### 5.4 Generality

Theorem A is in the right generality for its use. Of the faces, the proof uses only two things:
- they split $X$ along rational homology spheres of positive scalar curvature whose flat connections are nondegenerate;
- the face terms cancel in the weighted sum, in both theories.

A remark saying so would show the reader what is special to $S^3$ and $L(4,1)$. PLAUSIBLE.

### 5.5 Further terms in [R]

| as written | write instead |
|---|---|
| the title | "A vanishing theorem for $\mathrm{SO}(3)$-monopoles over a cube of metrics", and separately "Reducible limits for the composites of $u$" |
| "a main component of type S or R" | "a reducible pair on one of the pieces" |
| "the family-specific content", "hypothesis (i), (ii), (iii)" | name the three phenomena: the pieces of a face carry their own Seiberg–Witten strata; chains of reducible components need an index inequality; abelian instantons on negative pieces cannot be made regular |
| "the trace state", "the central state", "filling the lens ends by the manuscript's reference abelian connections" | "the flat connection $\gamma$", "a central flat connection", "capping the lens ends by fixed reducible connections" |
| "VERIFIED (`f1_lattice.py`, `f4_identities.py`)" inside statements | "(direct computation)" |
| "The single hardest point"; "margin of exactly one dimension" | "The main analytic difficulty"; keep the second |

---

## 6. Order and connections

### 6.1 The outline

| § | content | taken from | [S] |
|---|---|---|---|
| 0 | Main theorem, conditional on (H1)–(H5); the scheme | [S], first paragraph | — |
| 1 | Floer homology of $S^3_{\pm2}(K)$: complexes over $\mathbb Z$, central reducibles, the $\mathbb Z/8$-grading, the free involution $\chi_*$, degrees, the handle maps | [B] §1.2; [NV] §§1.1–1.2, Lemma 1.1; [G] §§1.1, 1.3 | Step 2 |
| 2 | The map $B$: Theorem 2.1; Proposition 2.2; the degrees of $B$, $H$ and $u$; Corollary 2.3; Conjecture 2.4 | [B] §§1–4; [NV] Prop. 5.4 | Steps 2, 4 |
| 3 | The family invariant: $X(\Pi)$, $Q$, the bundles $E_e$, the weights, $\Omega$; why the primary invariants vanish; Theorem 3.2 | [G] §§1–6 | Step 4 |
| 4 | Nonvanishing: Lemma 4.1, Proposition 4.2, Corollary 4.3 | [NV] §§2, 4, 5 | Step 2 |
| 5 | Vanishing in families: the closed case, Theorem 5.2, the criterion | [S] §2; [R] §§1–3 | Step 1 |
| 6 | No reducible limits for the composites of §4: Proposition 6.1, the control on $P$, the inequalities for chains, Theorem 6.4 | [R] §4; [S] Steps 3, 5, 6 | Steps 3, 5, 6 |
| 7 | Proof of the main theorem: for the same composite and the same family, and for large $M\in8\mathbb Z$, §4 gives $\Omega\ne0$ and §6 gives $\Omega=0$ | [NV] Thm. 5.1 Step 5, Cor. 5.3 | Step 6 |

Each section depends only on earlier ones. The one exception is §5, which uses nothing from §§2–4 and could come first. I prefer it after §4, so that $B$, $u$, $X(\Pi)$ and $\Omega$ are defined before the theorem about them. VERIFIED (dependencies, by reading which results each proof cites).

With this order the main theorem has a two-line proof. Its full statement is: *let $K\subset S^3$ be a knot of genus at least two, and assume (H1)–(H5); then there is no orientation-preserving diffeomorphism $S^3_{-2}(K)\to S^3_2(K)$.* Together with Ni–Wu, Hanselman (Thm. 2) and [DLME] (Thms. 1.2–1.3, Cor. 1.4), this would give the cosmetic surgery conjecture in $S^3$ under (H1)–(H5). VERIFIED as logic ([NV] Cor. 5.3 and its checks against Hanselman and [DLME]).

### 6.2 Compatibility conditions between the sections

- **(i) One closed manifold.** The three files build three different manifolds. VERIFIED ([G] §1.2; [R] §1.1; [NV] §5).
  - [G] builds $X_M$ from $u^M$ alone, with $n=4M$ spheres.
  - [R] builds it from $(\phi_*B)^{p_-}u^M(\phi_*B)^{p_+}$, with $n=4M+p$.
  - [NV] uses $B\,\Pi_0\,u^M(\phi_*B)^{p}$, capped by $\bar C_+$ after one more copy of $W_B$.

  The outline needs one definition of $X(\Pi)$, and §§3, 4 and 6 must all be stated for the composites of Corollary 4.3.
- **(ii) One family of metrics.**
  - The composition law holds for necks along $Y_{\pm2}$ of length $T\ge T_0$, where $T_0$ depends on $M$, with finite necks and prescribed metrics inside each $W_B\cup W_H\cup W_B$. [G] says that invariance under shortening the long necks is not available.
  - [R] fixes a family in which "no other length tends to infinity", and makes its choices "in order: the caps and their metrics; …; and only then $M$".

  VERIFIED ([G] Theorem A′, §8(6); [R] §1.1, Lemma 4.6). So Theorem 6.4 must be stated for $g^T$ with $T\ge T_0(M)$, and its constants must not depend on $T$. PLAUSIBLE that they do not: the long necks lie in the negative pieces, where the argument is lattice-theoretic, and in the outer pieces, whose estimates must be checked uniformly in $T$.
- **(iii) One set of constraints and signs.** The jumping-line divisors $V_{S_i}$, with their degeneration at the $J$-faces, and the weights $\varepsilon(e)$ must be the same in §§2, 3 and 5. VERIFIED that [B], [G] and [R] all use jumping-line divisors; [R] Corollary D notes that the manuscript uses holonomy representatives instead.

  The cancellation of the monopole ends at the lens faces ([R] (A5)) must use the same sign $\epsilon$ as Theorem 2.1. PLAUSIBLE that it does: at those ends the spinor vanishes on $\nu(S_i)$ because of positive scalar curvature, and along the Donaldson stratum the orientation of the monopole space is induced from that of the instanton space ([FL2b] Lemmas 3.24–3.25). This should be a lemma.
- **(iv) One hypothesis on $B$, and no congruences.** [S] Step 2, [G] Corollary B and [R] Corollary D obtain the nonvanishing from $u^M\equiv1\pmod{2^N}$, which needs $B$ invertible over $\mathbb Z_{(2)}$. [NV] shows that rational invertibility (H2) and Lemma 4.1 suffice, because the vanishing holds for all large $M$. VERIFIED ([NV] §0(1) and the proof of Theorem 5.1).

  Delete the congruences, but keep the integrality remark, in its correct form:
  - the monopole argument yields $2^{n_a-1}$ times an oriented count, so $\Omega$ must be an oriented, integral count, and $B$ an integral chain map;
  - nothing is known about the parity of the initial pairing $q$, so its nonvanishing must be propagated over $\mathbb Q$, not modulo $2$.
- **(v) One bundle on $W_H$.** Fix $c_H$ with $c_H^2=0$, so that $\deg H\equiv-3$ and $\deg u\equiv1\pmod8$. [S] Step 2 says "$B$ is expected to invert [$H$] up to a fixed automorphism". For this $c_H$, $HB$ has degree $4$, so the sentence should say "$B$ is expected to be an isomorphism modulo two". VERIFIED ([B] Prop. 4.1; [G] §1.3).
- **(vi) One set of caps.** The three files treat the caps differently. VERIFIED ([NV] Thm. 4.4; [R] §1.1; [G] §1.2).
  - The caps of §4 come from Kronheimer–Mrowka's Prop. 15 and have $H_1=0$.
  - [R] assumes $X$ simply connected, and the caps blown up once, with classes $A_\pm$ on which $w$ is odd.
  - [G] does not blow up.

  Blowing up does not change the relative invariants on the old classes (the blow-up formula, with the determinant extended by zero). Simple connectivity is used in [R] Lemma 1.1(c), to exclude flat connections by means of spherical classes. Whether $H_1=0$ suffices: PLAUSIBLE, to be checked.
- **(vii) Congruence classes.** Take $M\in8\mathbb Z$, so that $c_2(E_e)$ is integral and the pairing does not vanish for degree reasons. Choose $p$ and $\langle c_1(\mathfrak t),e_\pm\rangle$ so that $n_a\in\mathbb Z$. These are stated separately in [G] Prop. 1.2 and §6.2, in [R] Theorem C and in [NV] Theorem 5.1. VERIFIED. State them once, in §3.
- **(viii) Spacing.** The three requirements are consistent; state them once. VERIFIED ([G] Theorem A′; [R] §3.4 "Consequence" and Lemma 4.5; [NV] (F)).
  - The composition law needs at least three copies of $W_B$ between consecutive copies of $W_H$.
  - [R] Theorem C needs four, or three under its parameter-local refinement (A7′).
  - The composites of §4 have at least four.

### 6.3 Duplications

| content | appears in | keep in |
|---|---|---|
| Floer theory at $Y_{\pm2}$; the free involution | [B] §1.2; [NV] §1.1, Lemma 1.1; [G] §§1.1, 1.3 | §1 |
| chain property of $B$ | [B] Theorem A(a), Lemmas 2.1–2.5; [G] Lemmas 4.3–4.5, Prop. 4.6 | §2 |
| jumping-line divisors, properties (J1)–(J4) | [B] §1.4; [G] Lemmas 4.1–4.2; [R] Lemma 1.2; [S] proof of Thm. 2.1 | §2 |
| reducibles on $\nu(S)$, framed index $8E$ | [B] Lemma 1.2; [G] Lemma 4.4; [R] §1.5 | §2 |
| degrees of $B$, $H$, $u$ | [B] §2.5, Prop. 4.1; [NV] §1.2, Prop. 3.1(4); [G] §1.3 | §2 |
| grading constraint | [B] Cor. 4.4; [NV] Prop. 5.4 | §2 |
| distinct $w_2$ of the $2^n$ bundles | [G] Prop. 1.2(3); [R] Lemma 1.1(b); [NV] §5 | §3 |
| dimension count $8\kappa=n+3m+c$, $n_a=\frac18(5m-n)+c_1$ | [G] §1.2; [R] Prop. 4.1; [S] Steps 5–6 | §6 |
| congruences modulo $2^N$ | [S] Step 2; [NV] Thm. 1(ii); [G] Cor. B; [R] Cor. D | delete |

VERIFIED (each location read).

### 6.4 Changes to the Strategy

1. Step 2: replace the congruence by the rational argument (§6.2(iv)), and "invert $H$" by "is an isomorphism" (§6.2(v)).
2. Steps 3, 5 and 6: replace the economic vocabulary (§1.2), and state the slogan in the form given at the end of §1.2.
3. Step 4 ("$\ell(K)+\ell(-K)-2n_D$") and Step 5 ("$K\cdot H$", "$H$ the period point"): write $c_1(\mathfrak s)$ and $\omega_g$ (§1.4).
4. Step 6: "the only return supplied by the triangles is $W_H$" becomes "the only cobordism $Y_{-2}\to Y_2$ that the exact triangles provide is $W_H$".
5. Step 1: "In reverse" becomes "Contrapositively".
6. §2, "A closed prototype", becomes "The closed case" and opens §5 of the outline. It extends [FL2b] Thm. 3.33(a) by sphere classes, and is of some independent interest. Its proof follows [FL2b]; I read it and found nothing to correct. PLAUSIBLE: transversality is not written out, as the text itself says.
7. Each Step should end with a pointer to the section of the outline that proves it.

---

## 7. Verdict and confidence

**Verdict.**
- **Interest.** Three statements are of intrinsic interest as statements: the vanishing theorem in families ([R] Theorem A), the $(-4)$-sphere relation ([B] Proposition B) and the grading constraint ([B] Corollary 4.4). The map $B$ is of interest as a construction, whose value rests on Conjecture C. The nonvanishing ([NV] §4) is a natural adaptation of Kronheimer–Mrowka. The composition law ([G]) is necessary and standard in kind. The title theorem of [NV] is linear algebra and should be a lemma.
- **Naturalness.** None of the four is yet stated as Donaldson, Kronheimer–Mrowka or Feehan–Leness would state it. The changes needed are mostly editorial (§§1–5):
  - Kronheimer–Mrowka's $m_G$ for the maps of families;
  - Feehan–Leness's vocabulary for limits of monopoles;
  - inequalities in place of the economic vocabulary;
  - one meaning per symbol;
  - five named hypotheses.
- **Generality.**
  - [B] and [R] Theorem A have the right generality.
  - [G] should drop $\phi$ from its hypotheses.
  - [R] Theorem C should cover the composites that [NV] uses.
  - [NV] Theorem 5.1 claims more (any negative-definite cobordism inducing a rational isomorphism) than the vanishing side checks, and should be stated for $\phi$.
- **As an outline.** Ordered as in §6.1, the four statements and the Strategy form a coherent proof outline of a conditional theorem: under (H1)–(H5), no knot of genus at least two has $S^3_2(K)\cong S^3_{-2}(K)$. The two compatibility conditions of substance are (i) and (ii) of §6.2: the vanishing theorem must be proved for the composites and the family of metrics for which the composition law and the nonvanishing are proved.

**Confidence.**
- The factual statements about the texts (occurrences, collisions, mismatches): VERIFIED, about 97%.
- That the reformulations of §§2–5 are faithful to the mathematics of the files: PLAUSIBLE, about 85%. I re-derived the proof of Theorem 2.1 from KM's formula and [B]'s lemmas, Proposition 2.2 for simple type, Corollary 2.3, Lemma 4.1, Proposition 6.1, and the ranges of §1.2. The rest I restated without re-proving.
- That the order of §6.1 and conditions (i)–(viii) are what is needed for a coherent outline: PLAUSIBLE, about 80%. There may be a further condition that I have not found; the most likely place is the comparison of orientations between the instanton and monopole lens ends (§6.2(iii)).
- **For the report as a whole** — that the four statements, reformulated as proposed and ordered as in §6, form with the Strategy a natural and coherent proof outline: **about 80%**. This is a judgement of form. Nothing here changes the files' own estimate for the mathematics (15–25% that the main theorem holds by this route), which I did not re-derive; that estimate is SPECULATIVE as far as this report is concerned.

---

## Appendix A. Counts

Number of lines containing each expression, case-insensitive. Totals: [B] 582 lines, [NV] 522, [G] 710, [R] 472, [S] 290.

| expression | [B] | [NV] | [G] | [R] | [S] | total |
|---|---|---|---|---|---|---|
| "insertion" | 21 | 5 | 12 | 21 | 5 | 64 |
| "cost(s)", "supply/supplies/supplied", "spend(s)", "save(s)" | 5 | 6 | 21 | 6 | 12 | 50 |
| notes T1–T5 | 7 | 18 | 16 | 13 | 0 | 54 |
| "Round 3a" | 0 | 5 | 5 | 2 | 0 | 12 |
| computer files (`.py`) | 1 | 5 | 4 | 22 | 0 | 32 |
| "draft" | 17 | 28 | 21 | 21 | 0 | 87 |
| citations by file and line ("l. $n$") | 35 | 0 | 0 | 0 | 0 | 35 |
| "type F/A/S/R" | 0 | 0 | 0 | 33 | 0 | 33 |
| "segment" | 0 | 0 | 0 | 34 | 1 | 35 |
| "excess" | 0 | 0 | 22 | 6 | 0 | 28 |
| "lift(s)" | 46 | 8 | 3 | 1 | 0 | 58 |
| "spin shift" | 9 | 0 | 0 | 0 | 0 | 9 |
| "clamp", "band", "cusp" | 0 | 1 | 4 | 9 | 0 | 14 |
| "$Y$-neck(s)" | 0 | 0 | 20 | 0 | 0 | 20 |

VERIFIED (counted with `grep -ci` on the five files, 7 October 2026).
