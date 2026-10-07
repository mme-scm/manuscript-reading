# Prototype 2. A closed-manifold model of the sphere mechanism

*Scope.* This is an independent attempt at the classical, closed-manifold prototype of mechanism (3) of the strategy: $\mu$-insertions of disjoint $(-4)$-spheres push every Seiberg–Witten class below Feehan–Leness level zero, so a Donaldson invariant must vanish.

*Labels.*
- **[VERIFIED]**: checked against the cited source, by hand, or by the computer check `round3a/checks2/check_prototype.py` (exact rational arithmetic).
- **[PLAUSIBLE]**: standard but not written in the cited sources, or not checked in full.
- **[SPECULATIVE]**: a guess or analogy.
- **†**: cited from memory.

*Sources.* FL2b = dg-ga/9712005 (theorem numbers recomputed from the LaTeX counters; they agree with `notes/R1-literature.md`). FL2a = math/0007190. The Memoir is math/0203047 and FL6 is math/0609530.
- KM94 = math/9404232.
- FS-blowup = alg-geom/9405002 (Ann. of Math. 143 (1996)).
- FS-rbd = alg-geom/9505018 (J. Differential Geom. 46 (1997)).
- OS = Ozsváth–Szabó, *The symplectic Thom conjecture*, Ann. of Math. 151 (2000), arXiv math/9811087.
- FS-imm = Fintushel–Stern, *Immersed spheres in 4-manifolds and the immersed Thom conjecture*, Turkish J. Math. 19 (1995), quoted through OS Remark 1.5.
- T2 = `notes/T2-mu-classes.md`.

The new sources are in `round3a/src_*`.

---

## 0. Findings

1. **The naive statement is false.** The naive statement reads: "if the disjoint $(-4)$-spheres sufficiently outnumber $b^+$, then $D^w_X(\mu(S_1)\cdots\mu(S_n)z)=0$." It fails for every proposed bound, and it fails unconditionally.
   - *Conics in blow-ups.* $D^w_X(\mu(S_1)\cdots\mu(S_n)z)=2^nD^{w_0}_{X_0}(z)$, with $b^+$ fixed and $n$ arbitrary (§2).
   - *Spheres outside definite summands.* It also fails for these: $E(4)$ with nine sections ($b^+=7$), and $K3\#32\overline{\mathbb{CP}}{}^2$ with sixteen spheres ($b^+=3$).
   - **[VERIFIED]**
2. **What fails is the accounting.**
   - In the closed problem an insertion supplies energy $\tfrac14$.
   - For a lone $(-4)$-sphere, and for a conic on which $w$ is odd, a reducible can meet the insertion at a cost of only $\tfrac14$. At best the balance is even, and it is exactly even for the conics.
   - Mechanism (3) needs three features of the manuscript's spheres:
     - (a) each sphere is *split*, $S=F^+-F^-$, into two orthogonal halves of square $-2$;
     - (b) $w$ is even on the halves, so meeting $\mu(S)$ costs $\tfrac12$;
     - (c) $\Lambda$ is *pinned*, so that the halves carry no Dirac index.
   - **[VERIFIED]**
3. **The correct closed statement (Theorem A).**
   - *Content.* This is FL2b Thm. 3.33(a) with its hypothesis "no reducible at any level in $\bar{\mathcal M}_{\mathfrak t}$" weakened to the cut-down statement: every Seiberg–Witten class has Feehan–Leness level smaller than the number of spheres it misses.
   - *Proof.* The proof uses:
     - FL2b Prop. 3.29 at the instanton end;
     - FL2b Lemma 3.15 and Cor. 3.18 at the irreducible lower strata;
     - the jumping-line representatives of $\mu(S_i)$ (T2 Cor. 3.3) at the reducible strata.
   - *Status.*
     - **[VERIFIED]** as an argument.
     - **[PLAUSIBLE, 85–90%]** for the one step that is not in FL2b: transversality of the jumping-line representatives inside FL's compactification.
4. **Numerical form (Corollary C).** For split spheres with $w$ even on the halves, the exclusion holds once
   $$n>\tfrac32(1+b^+)+\tfrac12\deg z'+B,$$
   where $B$ bounds the part of $c_1(\mathfrak s)-\Lambda$ orthogonal to the halves.
   - The constant $\tfrac32$ has a meaning: each sphere loses $\tfrac12-\tfrac14$, and each increase of $b^+$ by one supplies $\tfrac38$.
   - $n_D\ge1$ remains a separate hypothesis.
   - **[VERIFIED given Theorem A]**
5. **Witten form (Proposition D).** On manifolds of simple type satisfying Witten's formula, with $\langle w,S_i\rangle$ even and $z'\perp S_i$, only basic classes with $\langle K,S_i\rangle=\pm2$ for every $i$ contribute.
   - *Adjunction input:* $|K\cdot S|\le4$ (Fintushel–Stern; Ozsváth–Szabó).
   - *Pairing input:* classes with $K\cdot S=\pm4$ cancel in pairs, by the Ozsváth–Szabó/Fintushel–Stern relation $SW(K+2\varepsilon\,\mathrm{PD}(S))=SW(K)$.
   - $b^+$ plays no role, which is why there is no closed vanishing theorem of the naive kind.
   - **[VERIFIED given Witten's formula]**
6. **Tests.** **[VERIFIED by computer]**
   - In $K3\#r\overline{\mathbb{CP}}{}^2$ we tested every type of embedded $(-4)$-sphere built from exceptional spheres and Kummer nodes, with every parity of $w$. The closed Feehan–Leness exclusion holds, with the best $\Lambda$, **if and only if** Witten's formula gives zero.
   - For $E(4)$ with $n$ sections and $r$ further insertions of $\mu(h)$, the exclusion never holds when the invariant is nonzero (all $n,r$).
7. **Why the closed version does not suffice.**
   - (i) *Topology.* The manuscript's $X_M$ is a connected sum along the $J_i\cong S^3$, so every closed invariant of it vanishes, and the cosmetic nonvanishing lives only in the family invariant $\Omega$.
   - (ii) *Arithmetic.* With the manuscript's blocks and no family parameters, the closed requirements are $m/n>\tfrac25$ (for $n_D\ge1$) and $m/n<\tfrac27$ (for exclusion), which are incompatible. The family parameter halves the energy each insertion supplies, from $\tfrac14$ to $\tfrac18$, and opens the window $(\tfrac15,\tfrac37)$.
   - **[VERIFIED]** for the arithmetic, given the block table of `numerology.tex`.

---

## 1. Setting and the two quantities

**Data.**
- $X$ is closed, oriented and simply connected, with $b^+\ge1$ and a generic metric.
- $\mathfrak t=(\rho,W\otimes E)$ is a spin$^u$ structure, with $\Lambda=c_1(\mathfrak t)$, $\kappa=-\tfrac14p_1(\mathfrak t)$ and $w=c_1(E)$. Hence $\Lambda\equiv w+w_2(X)\pmod2$.

Following FL (FL2b (3.20)–(3.21), Memoir (2.1.12), (2.3.14)),
$$d_a=8\kappa-3(1+b^+),\qquad n_D:=n_a=\tfrac14(\Lambda^2-\sigma)-\kappa=\Theta-\kappa,$$
and a spin$^c$ structure $\mathfrak s$ defines reducibles $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$ in $\bar{\mathcal M}_{\mathfrak t}$ exactly at the level
$$\ell(\mathfrak s)=\kappa+\tfrac14v^2,\qquad v=c_1(\mathfrak s)-\Lambda\equiv w\pmod 2$$
(FL2b Lemma 3.32 and (3.64)). With $E=L_1\oplus L_2$ and the spinor in $W\otimes L_1$, one has $v=c_1(L_1)-c_1(L_2)$.
**[VERIFIED]**

**Spheres.**
- $S_1,\dots,S_n$ are disjoint embedded spheres with $S_i^2=-4$ and $\langle w,S_i\rangle$ even, so $\mu(S_i)$ is integral (T2 §2).
- We represent $\mu(S_i)$ by Donaldson's jumping-line divisor $V_{S_i}=\{A:\ E_A|_{S_i}\not\cong\mathcal O\oplus\mathcal O\}$ (T2 Prop. 2.3).
- *The incidence lemma* (T2 Thm. 3.1, Cor. 3.3) is the representative-level form of FL2b Cor. 4.7 and FLL1 Lemma 4.10. It says:
  - a reducible with $\langle v,S_i\rangle\ne0$ lies in $V_{S_i}$;
  - a reducible with $\langle v,S_i\rangle=0$ does not;
  - a limit of points of $V_{S_i}$ at such a reducible must carry an Uhlenbeck point on $S_i$.

  Since the $S_i$ are disjoint, a reducible stratum at level $\ell$ in the closure of the cut-down space satisfies $\ell\ge T(v):=\#\{i:\langle v,S_i\rangle=0\}$.
- **[VERIFIED]** in T2.

**Supply and cost.**
- *Supply.* In the closed problem the cut-down space has dimension zero when $d_a=2n+\deg z'$. So
  $$8\kappa=2n+\deg z'+3(1+b^+).$$
  Each insertion supplies $\tfrac14$ to $\kappa$, and each increase of $b^+$ by one supplies $\tfrac38$.
- *Cost.* A stratum survives only if its level is at least $T(v)$. So each insertion it meets through $\langle v,S_i\rangle\ne0$ must be paid in $-v^2/4$, and each insertion it misses raises the required level by one.
- The whole argument compares these two quantities.

**An identity.** For every $\mathfrak s$ and every $\Lambda$:
$$\ell(\mathfrak s)-n_D=2\kappa+\tfrac14\big(K^2+\sigma\big)-\tfrac12\langle K,\Lambda\rangle,\qquad K=c_1(\mathfrak s).$$
Hence, for a pair $\pm K$,
$$\ell(K)+\ell(-K)=4\kappa+2n_D+\tfrac12(K^2+\sigma).$$
**[VERIFIED]**: expand $(K-\Lambda)^2$ and substitute $\Lambda^2=4(n_D+\kappa)+\sigma$.

*Consequence.* At fixed $\kappa$, raising $n_D$ by changing $\Lambda$ raises the average level of every pair $\pm K$ by the same amount. Exclusion needs both members of the pair below their counts $T(\pm K)$, so changing $\Lambda$ never helps it: whatever is added to $n_D$ is added, on average, to the levels.

---

## 2. The naive statement is false

**Naive statement N.** Let $X$ have $b_1=0$, let $w$ be good, and let $S_1,\dots,S_n$ be disjoint embedded $(-4)$-spheres with $\langle w,S_i\rangle$ even. If $n>C(1+b^+)$, then $D^w_X(\mu(S_1)\cdots\mu(S_n)z)=0$ for every $z$.

**Proposition 2.1 (conics).** Let $X_0$ be closed and simply connected, with $b^+(X_0)\ge2$ and $D^{w_0}_{X_0}(z)\ne0$ for some $z\in\mathbb A(X_0)$; for instance $X_0=K3$.
- Put $X=X_0\#n\overline{\mathbb{CP}}{}^2$, with exceptional classes $e_i$.
- Let $S_i$ be a smooth conic in the $i$-th summand. It is an embedded sphere with $[S_i]=2e_i$ and $S_i^2=-4$.
- Put $w=w_0+\sum_i\mathrm{PD}(e_i)$. Then $w$ is good and $\langle w,S_i\rangle=-2$.

Then
$$D^w_X\big(\mu(S_1)\cdots\mu(S_n)\,z\big)=2^n\,D^{w_0}_{X_0}(z)\neq0\qquad\text{for every }n,$$
while $b^+(X)=b^+(X_0)$. So N fails for every $C$. It fails even though the spheres lie in negative-definite summands.

*Proof.*
- FS-blowup Lemma 2.3(6), due to Kotschick, gives $\hat D_{c+e}(e\,z)=D_c(z)$ for $z\in\mathbb A(X)$, with no simple-type hypothesis.
- Apply it once for each summand, and use $\mu(2e_i)=2\mu(e_i)$. ∎ **[VERIFIED]**
- *Cross-check.* In the simple-type form (FS-blowup §5: $\hat{\mathbf D}_{c+e}=-\mathbf D_c\,e^{-E^2/2}\sinh E$), the factor contributed by each conic is $e^{-2t^2}\sinh 2t$, whose linear coefficient is $2$. The computer check confirms this. **[VERIFIED]**

*Why the mechanism does not see it.* Every reducible has $\langle v,e_i\rangle$ odd, because $v\equiv w$. Hence $\langle v,S_i\rangle=2\langle v,e_i\rangle\ne0$: every insertion is met.
- *Level.* Meeting it costs nothing beyond the $\tfrac14(v\cdot e_i)^2\ge\tfrac14$ that the summand costs anyway. The insertion supplies exactly $\tfrac14$, so levels do not change.
- *Dirac index.* Since $\langle\Lambda,e_i\rangle$ is even, it can be taken to be $0$. Then $\Theta$ rises by $\tfrac14$, which exactly cancels the $\tfrac14$ added to $\kappa$, so $n_D$ does not change either.

Thus, as far as Feehan–Leness levels and $n_D$ are concerned, $X$ behaves exactly like $X_0$. **[VERIFIED]**

**Proposition 2.2 (lone spheres outside definite summands).**

(a) *$E(4)$.* We use:
- KM94 (3): $\mathbf D_{E(4)}=e^{Q/2}\sinh^2F$;
- the structure theorem for general $w$ (FL6 Thm. 2.2, after KM).

Let $\sigma_1,\dots,\sigma_n$ be disjoint sections, with $\sigma^2=-4$ and $F\cdot\sigma=1$; nine of them come from fibre-summing four copies of $E(1)$ along its nine exceptional sections. Put $h=4F+\sum_j\sigma_j$, so that $h\cdot\sigma_i=0$, $h\cdot F=n$ and $h^2=4n$. Write $H_r(a)$ for the coefficient of $u^r/r!$ in $e^{u^2h^2/2+ua}$; for $a>0$ it is a polynomial with positive coefficients, hence non-zero. Since $w\perp F$, the three basic classes carry the same sign. Then:
- the class $2F$ contributes $2^nH_r(2n)$;
- the class $-2F$ contributes $(-2)^n(-1)^rH_r(2n)$;
- the class $0$ contributes nothing, because the factor $\prod_i K\cdot\sigma_i$ vanishes.

The total is $2^nH_r(2n)\big(1+(-1)^{n+r}\big)$ times a non-zero constant. Hence $D^w(\mu(\sigma_1)\cdots\mu(\sigma_n)\mu(h)^r)\ne0$ whenever $n+r$ is even. For $w$ we take a root, or a sum of two orthogonal roots, orthogonal to $F$ and to the $\sigma_i$; this makes $w$ good and gives the right degree. For example $n=9>b^+=7$ with $r=1$.
- **[VERIFIED]** for the computation.
- **[PLAUSIBLE]** for the existence of nine disjoint sections and of such roots (standard).

(b) *$K3\#32\overline{\mathbb{CP}}{}^2$.*
- Let $N_1,\dots,N_{16}$ be the Kummer nodes.
- Put $S_j=N_j+e_{2j-1}+e_{2j}$, obtained by tubing. These are sixteen disjoint embedded $(-4)$-spheres, and $b^+=3$.
- Choose $w$ with $\langle w,N_j\rangle$ odd for all $j$. This is possible because the Kummer code has only the weights $0$, $8$ and $16$.
- Also take $\langle w,e_{2j-1}\rangle$ odd and $\langle w,e_{2j}\rangle$ even.
- Each sphere contributes the linear coefficient of $\sinh t\cosh t$, which is $1$. So $D^w(\mu(S_1)\cdots\mu(S_{16})z')=\pm D^{w_{K3}}_{K3}(z')\ne0$ for suitable $z'\perp S_j$.
- **[VERIFIED]**

*Conclusion.* The number of spheres is not the relevant quantity. What matters is whether meeting an insertion costs more energy than the insertion supplies, and that is decided by the lattice near each sphere and by $w$ modulo $2$.

---

## 3. The correct closed statement

**Theorem A (closed sphere vanishing; cut-down form of FL2b Thm. 3.33(a)).**
Let $X$ be closed, oriented and simply connected, with $b^+(X)\ge1$, a generic metric $g$ and generic perturbation parameters as in FL2b. Let $\mathfrak t$ be a spin$^u$ structure such that:
- the integral lift $w$ of $w_2(\mathfrak t)$ is good;
- $d_a\ge0$;
- $n_D\ge1$.

Let $S_1,\dots,S_n$ be pairwise disjoint embedded spheres with $S_i^2=-4$ and $\langle w,S_i\rangle$ even. Let $z'\in\mathbb A(X)$ be a monomial in the point class and in classes of embedded surfaces, with $2n+\deg z'=d_a$. Assume:

> **(E)** for every spin$^c$ structure $\mathfrak s$ whose moduli space $M_{\mathfrak s}(g)$ of Feehan–Leness-perturbed Seiberg–Witten monopoles is non-empty, the class $v=c_1(\mathfrak s)-\Lambda$ satisfies
> $$\kappa+\tfrac14v^2\ <\ \#\{i:\langle v,S_i\rangle=0\}.$$

Then $D^w_X\big(\mu(S_1)\cdots\mu(S_n)\,z'\big)=0$. If $b^+=1$, this holds in the chamber of $g$.

*Remarks.*
- The left side of (E) is the level of the stratum $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$. Classes of negative level satisfy (E) automatically.
- For $n=0$, (E) is FL2b's hypothesis (3.68), and Theorem A is FL2b Thm. 3.33(a) in degree $d_a$.
- FL2b's (3.68) asks that $\bar{\mathcal M}_{\mathfrak t}$ contain no reducible at any level, so the insertions play no role there. (E) asks only that no reducible stratum, *at any level* $\ell\ge0$, lie in the closure of the cut-down space. Step 4 below treats all levels at once, because the incidence argument uses only Uhlenbeck convergence away from the bubble set.
- The theorem is the case $\dim Q=0$ of Theorem E and Proposition E′ in `R1-literature.md` (e3).

**[VERIFIED]** as a reduction to FL2b. The exception is step 0 below, which is **[PLAUSIBLE]**.

*Proof.*
0. *Representatives.* Represent:
   - $\mu(S_i)$ by the jumping-line divisor $V_{S_i}$;
   - the classes of $z'$ and the weight-two class $\mu_c$ by FL's representatives (FL2b Lemmas 3.12 and 3.13).

   $V_{S_i}$ depends only on the restriction of the connection to $S_i$. It is defined for *all* connections, reducible ones included, and it is closed under $C^0$ convergence on $S_i$. Transversality on the irreducible strata at all levels is obtained in either of two standard ways:
   - holonomy perturbations of the equations; or
   - replacing the section $\det\bar\partial_{A|S_i}$ by $\det(\bar\partial_{A|S_i}+P(A))$, with $P$ small and equivariant and supported away from a neighbourhood of the reducible locus (T2 §4).

   **[PLAUSIBLE, 85–90%]**. This is the only point not in FL2b. FL2b's representatives are generic sections over $\mathcal B^*(\nu(Y\cup D))$, after Kronheimer–Mrowka. Near a reducible with $\langle v,\beta\rangle=0$ their closure is not controlled: FL2b Lemma 3.15(2a) gives only the reverse inclusion $\langle c_1(\mathfrak t)-c_1(\mathfrak s),\beta\rangle\ne0\Rightarrow\iota(M_{\mathfrak s})\subset\bar{\mathcal V}(\beta)$.
1. *The cut-down space.* Put $\delta_c=n_D-1$ and
   $$\mathcal Z=\mathcal V(z)\cap\mathcal W^{\delta_c}\cap\mathcal M^{*,0}_{\mathfrak t}/S^1,\qquad z=S_1\cdots S_n\,z'.$$
   Its dimension is $(d_a+2n_D-1)-d_a-2(n_D-1)=1$. Since $b_1=0$, $z$ is intersection-suitable (FL2b Lemma 3.17). **[VERIFIED]**
2. *Instanton end.* By FL2b Prop. 3.29 ($w$ good, $n_D>0$, $\deg z=d_a$), the ends of $\mathcal Z$ at the link of $M^w_\kappa$ number $2^{n_D-1}\#(\bar{\mathcal V}(z)\cap\bar M^w_\kappa)=2^{n_D-1}D^w_X(z)$. **[VERIFIED]** as a citation.
3. *Irreducible lower strata.* These are the free and zero-section strata at levels $\ell\ge1$. The argument of FL2b Lemma 3.15(1) applies to $V_{S_i}$ verbatim: a limit either satisfies the condition or carries an Uhlenbeck point on $S_i$. The dimension count of FL2b Cor. 3.18 then keeps $\bar{\mathcal Z}$ off these strata. **[VERIFIED]** given step 0.
4. *Reducible strata.* Zero-section reducibles, i.e. abelian anti-self-dual connections, are absent: $w$ is good, $b^+>0$ and the metric is generic (FL2a Prop. 3.1 and Cor. 3.3; Memoir (2.2.2)).

   Suppose $[A_\alpha,\Phi_\alpha]\in\mathcal Z$ converges to a point of $M_{\mathfrak s}\times\mathrm{Sym}^\ell(X)$, with $\ell=\kappa+v^2/4$.
   - Take $i$ with $\langle v,S_i\rangle=0$, and suppose no Uhlenbeck point of the limit lies on $S_i$.
   - Then the convergence is $C^\infty$ near $S_i$, after gauge. Since $V_{S_i}$ is closed, the restriction of the limit to $S_i$ lies in $V_{S_i}$.
   - But that restriction is a sum of two line bundles of degree $\pm\tfrac12\langle v,S_i\rangle=0$. Such a bundle is holomorphically trivial on $\mathbb P^1$, so it is not in $V_{S_i}$. This is a contradiction, so some Uhlenbeck point lies on $S_i$ (T2 Cor. 3.3(ii)).
   - The $S_i$ are disjoint, so these points are distinct, and $\ell\ge\#\{i:\langle v,S_i\rangle=0\}$. This contradicts (E).

   So $\bar{\mathcal Z}$ contains no reducible point, at any level. **[VERIFIED]**
5. *Stokes.* Truncate $\bar{\mathcal Z}$ at $\|\Phi\|^2_{L^2}=\varepsilon$. The result is a compact oriented one-manifold whose boundary lies on the instanton link. So $2^{n_D-1}D^w_X(z)=0$. ∎ **[VERIFIED]**

*What Theorem A does not need.*
- No gluing at reducibles: no stratum is parametrized, and no link is evaluated.
- None of Memoir Hyp. 7.8.1, FL6 Hyp. 3.1 or FL2b Conj. 3.34.

**Theorem A′ (form with basic classes; conditional).** Require (E) only for Seiberg–Witten *basic* classes. The conclusion then holds provided:
- FL2b Conj. 3.34 holds: strata with $SW_{\mathfrak s}\equiv0$ contribute nothing;
- at levels $\ell\ge1$, the gluing hypothesis (Memoir Hyp. 7.8.1) that defines the links holds.

**[PLAUSIBLE; conditional]**. This is the form used in the computer checks of §6, since basic classes are what one can compute.

---

## 4. The cost of a sphere, and the numerical form

**Lemma B (cost of meeting a sphere).** Let $v\in H^2(X;\mathbb Z)$.
1. *Lone sphere.* If $S^2=-4$ and $\langle v,S\rangle$ is even and non-zero, then the projection $v_S$ of $v$ to $\mathbb R\,\mathrm{PD}(S)$ satisfies
   $$-\tfrac14v_S^2=\tfrac1{16}\langle v,S\rangle^2\ge\tfrac14.$$
2. *Split sphere.* Suppose $S=F^+-F^-$ with $F^+\perp F^-$, $(F^\pm)^2=-2$, $\langle v,F^\pm\rangle$ even and $\langle v,S\rangle\ne0$. Then the projection $v_R$ to $R=\mathrm{span}(F^+,F^-)$ satisfies
   $$-\tfrac14v_R^2=\tfrac18\big(\langle v,F^+\rangle^2+\langle v,F^-\rangle^2\big)\ge\tfrac12.$$
3. *Several spheres.* If the halves of $n$ spheres are pairwise orthogonal, these projections are mutually orthogonal and the costs add.

**[VERIFIED]**: projection formulas. Since $v\equiv w$, the evenness in (2) is equivalent to $\langle w,F^\pm\rangle$ even.

*Remarks.*
- The manuscript's spheres are split. Indeed $S=F_l-F_r$, with $F_l,F_r$ the trace classes of square $-2$, and $c$ is even on them (T2 §1). So meeting each insertion costs at least $\tfrac12$, against a supply of $\tfrac14$ in the closed problem, or $\tfrac18$ in the family problem.
- In Proposition 2.1 the cost per insertion is $\tfrac14$, as in part (1) with equality.
- The conics of Proposition 2.1 in $K3\#n\overline{\mathbb{CP}}{}^2$ admit no system of pairwise orthogonal halves.
  - Halves of $S_i=2e_i$ have the form $e_i\pm y_i$ with $y_i^2=-1$ and $y_i\perp e_i$, since $T=2y_i$.
  - Requiring all four products $(e_i\pm y_i)\cdot(e_j\pm y_j)$ to vanish forces $y_i\perp e_j$ for every $j$.
  - Hence $y_i\in H_2(K3)$, which is even, so $y_i^2=-1$ is impossible.
  - **[VERIFIED]** So Lemma B(3) does not apply to them.

**Corollary C (numerical form).** Assume the hypotheses of Theorem A except (E), and assume:
- each $S_i=F_i^+-F_i^-$, where the $2n$ classes $F_i^\pm$ are pairwise orthogonal of square $-2$;
- $\langle w,F_i^\pm\rangle$ is even.

Let $P$ be the span of all the halves and $\pi_\perp$ the orthogonal projection to $P^\perp$, and put
$$B=\max\{(\pi_\perp v_{\mathfrak s})^2:\ M_{\mathfrak s}(g)\neq\emptyset\},$$
a finite maximum. If
$$n\ >\ \tfrac32\,(1+b^+)\;+\;\tfrac12\deg z'\;+\;B,$$
then (E) holds, and hence $D^w_X(\mu(S_1)\cdots\mu(S_n)z')=0$.

*Proof.* Let $T$ be the number of spheres that $v$ misses. Lemma B gives
$$-\tfrac14v^2\ge-\tfrac14(\pi_\perp v)^2+\tfrac12(n-T).$$
Hence
$$\kappa+\tfrac14v^2-T\ \le\ \kappa+\tfrac14B-\tfrac12n-\tfrac12T\ \le\ \tfrac18\big(\deg z'+3+3b^+-2n+2B\big)\ <\ 0.\qquad ∎$$
**[VERIFIED]**

This is mechanism (3) in closed form. Each sphere supplies $\tfrac14$ and costs $\tfrac12$, while each increase of $b^+$ by one supplies $\tfrac38$. So the spheres must outnumber $b^+$ by the factor $\tfrac32$, up to the constant $B$.

**Where $n_D\ge1$ comes from.** Corollary C keeps $n_D\ge1$ as a separate hypothesis. Split $\Theta=\Theta_P+\Theta_\perp$, where
$$\Theta_P=\tfrac14\Big(2n-\tfrac12\sum_{\text{halves}}\langle\Lambda,F\rangle^2\Big)\le\tfrac n2 .$$
There are three possible sources of index.
- *$\Lambda$ orthogonal to all halves.* Then $\Theta_P=n/2$, and $n_D$ grows like $n/4$ for free. Whether such a $\Lambda$ exists is a question about the gluing of the lattice.
  - *Pinning.* In the manuscript, the two halves in a negative piece $N\cong\langle-1\rangle^2$ are $e_1\pm e_2$, and the base bundle has $w_0\equiv0$ on $N$. Then $\Lambda_0$ is characteristic on $N$, one of $\langle\Lambda_0,e_1\pm e_2\rangle$ is $\equiv2\pmod4$, and $\Theta_N\le0$. This is the manuscript's $\langle\Lambda_0,S\rangle=2$ and $\Lambda^2=\sigma$ on negative pieces. **[VERIFIED]**
  - The other bundles of the bit sum use $\Lambda_e=\Lambda_0+\sum e_i\mathrm{PD}(S_i)$. Since $\Lambda_e^2=\Lambda_0^2+4|e|-4|e|=\Lambda_0^2$, they carry the same $\Theta$. For them the pinning is imposed by the bit sum, not by the lattice. **[VERIFIED]**
  - *A region on which $w$ is odd*, as in the conics of §2. There $\Theta$ can be positive, but the blow-up formula shows the gain is exactly cancelled by the insertions needed to keep the invariant non-zero. **[VERIFIED]** for blow-ups; **[PLAUSIBLE]** for general definite regions, via the generalized blow-up formula.
- *Enlarging $\Lambda$ inside $P^\perp$.* This raises $\Theta_\perp=\tfrac14\big((\pi_\perp\Lambda)^2-\sigma_\perp\big)$.
  - For each pair $\pm K$, the average of $(\pi_\perp v)^2$ over the pair is $(\pi_\perp K)^2+(\pi_\perp\Lambda)^2$. So the lower bound $B\ge(\pi_\perp K)^2+(\pi_\perp\Lambda)^2$ rises by four times the gain in $n_D$.
  - Concretely, if $\Theta_P=0$, then $n_D\ge1$ forces $B\ge(\pi_\perp K)^2+n+\sigma_\perp+8c_0+4$, where $8c_0=3+3b^++\deg z'$.
  - The hypothesis of Corollary C can then hold only if $(\pi_\perp K)^2+\sigma_\perp<-(8c_0+4)$ for every basic $K$. That requires a large negative-definite part of $P^\perp$ on which the basic classes are small.
  - This is the pair identity of §1 in another form. **[VERIFIED]**
- *$b^+$*, from pieces whose own Seiberg–Witten classes are confined independently. In the manuscript these are the positive pieces with their chamber conditions.

This is the closed shadow of point (5) of the strategy.

---

## 5. What Witten's formula says (closed, simple type)

**Proposition D.** Assume:
- $X$ is simply connected, with $b^+\ge2$, of Seiberg–Witten simple type;
- Witten's formula holds for $X$, that is
  $$\mathbf D^w_X=e^{Q/2}\sum_K(-1)^{(w^2+K\cdot w)/2}\beta_K e^K\qquad\text{(FL6 (2.9))},\qquad \beta_K=2^{2+(7\chi+11\sigma)/4}SW(K);$$
- the $S_i$ are disjoint embedded $(-4)$-spheres with $\langle w,S_i\rangle$ even;
- $z'$ is a polynomial in $x$ and in classes orthogonal to all $S_i$.

Witten's formula holds, for example, for elliptic surfaces and blow-ups of $K3$ (KM94 and FS-rbd); for projective surfaces with $q=0$ and $p_g>0$ (Göttsche–Nakajima–Yoshioka†, via Mochizuki); and conditionally in general (FL6). Under these assumptions,
$$D^w_X\big(\mu(S_1)\cdots\mu(S_n)z'\big)=\sum_{K:\ \langle K,S_i\rangle=\pm2\ \forall i}(-1)^{(w^2+K\cdot w)/2}\beta_K\prod_i\langle K,S_i\rangle\cdot P_{z'}(K),$$
where $P_{z'}(K)$ is the coefficient of $z'$ in $e^{Q/2+K}$.

*Proof.*
1. *The multilinear coefficient.* Because $S_i\cdot S_j=0$ and $S_i\perp z'$, the coefficient of $t_1\cdots t_n$ in $\prod_ie^{-2t_i^2+t_iK\cdot S_i}$ is $\prod_i K\cdot S_i$.
2. *Adjunction for spheres.* Take OS Thm. 1.3 with $g=0$; its validity for $g=0$ is OS Remark 1.5, citing FS-imm. If $|K\cdot S|>4$, then $K+2\varepsilon\,\mathrm{PD}(S)$ is a basic class of dimension $|K\cdot S|-4>0$, which contradicts simple type, exactly as in OS Cor. 1.7. Moreover $K\cdot S\equiv S^2\equiv0\pmod 2$, so $K\cdot S\in\{0,\pm2,\pm4\}$.
3. *Cancellation at $\pm4$.* If $K\cdot S_i=4\varepsilon$, OS Thm. 1.3 with $m=0$ gives $SW(K')=SW(K)$ for $K'=K+2\varepsilon\,\mathrm{PD}(S_i)$. Moreover:
   - $K'\cdot S_i=-4\varepsilon$;
   - $K'\cdot S_j=K\cdot S_j$ for $j\ne i$, and $P_{z'}(K')=P_{z'}(K)$;
   - the sign changes by $(-1)^{\langle w,S_i\rangle}=+1$.

   So the two terms cancel. Applying this at the first $i$ with $|K\cdot S_i|=4$ defines a fixed-point-free involution that reverses the sign of each such term.
4. *Vanishing at $0$.* Terms with some $K\cdot S_i=0$ vanish. ∎

**[VERIFIED]**, given Witten's formula, OS Thm. 1.3, and FS-imm for $g=0$ as quoted by OS. The sign $+$ in $SW(K')=SW(K)$ is OS's, and it matches the blow-up formula for $(-1)$-spheres: $\cosh$ when $w\cdot E$ is even, $-\sinh$ when it is odd.

*Remarks.*
- **$b^+$ plays no role in Proposition D.** The conics of §2 have $K\cdot S_i=\pm2$ for every basic class and every $i$. So in the closed world of simple type, nothing like "many spheres" can force vanishing. In the Feehan–Leness picture, $b^+$ enters through the supply $3(1+b^+)$ in $d_a$ and through $\Theta$.
- **The bit difference and rational blow-down.** FS-rbd Lemma 5.2 states that $\mathbf D_{X_2}|_{X^*}=\mathbf D_X-\mathbf D_{X,\sigma}$ for the rational blow-down of a $(-4)$-sphere. In Witten's formula the difference $D^w-D^{w+\mathrm{PD}(S)}$ on classes orthogonal to $S$ keeps exactly the $K$ with $K\cdot S\equiv2\pmod4$. These are the classes that descend to the rational blow-down (FS-rbd Thms. 8.2 and 8.4), and they are the same classes that survive $\mu(S)$ in Proposition D. This is the closed shadow of the lens-face cancellation in the bit sum of the family invariant. T2 Remark 1 identifies the lens term with the rational blow-down map. **[VERIFIED]** for the algebra; **[PLAUSIBLE]** for the analogy.
  - *Sign check.* A $(-4)$-sphere in $K3$ has $K\cdot S=0$, which gives $\mathbf D_{X_2}=0$, as FS state.
  - *The sign $s$.* With the opposite sign ($s=-1$), the closed bit sum would kill every class that $\mu(S)$ sees. Whether this says anything about the sign $s$ of the family invariant is **[SPECULATIVE]**. The two comparisons concern different bundles: $w$ and $w+\mathrm{PD}(S)$ have different $w_2$ on $X$, but the same $w_2$ on $W'$.

---

## 6. Tests

All are in `round3a/checks2/check_prototype.py` and use exact arithmetic. The Feehan–Leness side uses the basic-class form (Theorem A′), the best $\Lambda$ in a box, and $n_D$ set to $1$ by the free part of $\Lambda$. Relaxing integrality here only makes exclusion easier, so the test is the stricter one.

1. **Conics** (Proposition 2.1).
   - Per sphere, the linear coefficient is $2$ when $w\cdot e$ is odd and $0$ when it is even.
   - Per sphere, the effective level changes by $0$ when $w\cdot e$ is odd (no exclusion, invariant non-zero). When it is even it changes by $-\tfrac12$ (exclusion, and $\cosh$ is even, so the invariant is zero).
   - **[VERIFIED]**
2. **$K3\#r\overline{\mathbb{CP}}{}^2$.** The sphere types are:
   - $2e$;
   - $\pm e_1\pm e_2\pm e_3\pm e_4$;
   - $N\pm e_1\pm e_2$;
   - $N+N'$.

   We used every parity of $w$ with $\langle w,S\rangle$ even. By the identity of §1, $\max_K(\ell-T)$ splits as a sum over spheres; a brute force over pairs of spheres confirms this.
   - *Neutral spheres.* A sphere changes the effective level by exactly $0$ in two cases: the conic with $w\cdot e$ odd, and $N+e+e'$ with $w\cdot N$ odd and exactly one of $w\cdot e$, $w\cdot e'$ odd. These are exactly the spheres whose Witten factor is non-zero.
   - *All other spheres* change it by $-\tfrac12$ or $-\tfrac32$, and their Witten factor is zero.
   - So, for $\deg z'=0$, **closed exclusion holds if and only if Witten's formula vanishes.** The energy picture is sharp in this family. **[VERIFIED]**
3. **$E(4)$ with $n$ sections and $\mu(h)^r$.**
   - The identity gives $\ell(\pm2F)=\tfrac n2+\tfrac r2-1\mp\langle F,\Lambda\rangle$ and $\ell(0)=\tfrac n2+\tfrac r2-1$, with $T(K)=\#\{i:\langle\Lambda,\sigma_i\rangle=K\cdot\sigma_i\}$.
   - Adding the three conditions shows that exclusion needs $n+3r<6$. The non-vanishing cases ($n+r$ even) with $n+3r<6$ are $(n,r)=(1,1),(2,0),(4,0)$, and none of them is excluded.
   - A computer check confirms this for $n\le7$, $r\le2$.
   - Exclusion does occur at $(1,0)$ and $(3,0)$, where the invariant vanishes for degree reasons.
   - **[VERIFIED]**
4. **$K3\#32\overline{\mathbb{CP}}{}^2$** (Proposition 2.2(b)). This is the neutral case of test 2 sixteen times. There is no exclusion, and the invariant is non-zero. **[VERIFIED]**
5. **Rational blow-down.** We checked that the $K3$ sign in FS-rbd Lemma 5.2 is consistent with Proposition D. **[VERIFIED]**
6. **Not tested.** We found no closed example in which the hypotheses of Corollary C hold while the vanishing is *not* already explained by a reflection or blow-up symmetry.
   - Example: four exceptional spheres per sphere in $K3\#4n\overline{\mathbb{CP}}{}^2$, with $w$ odd on all four.
     - Take $\Lambda\perp$ every $e$ and $\Lambda|_{K3}=0$. Then $B\le0$ for basic classes and $n_D=\tfrac52+\tfrac34n-\tfrac18\deg z'$.
     - Corollary C, in the form of Theorem A′, applies for $n>6+\tfrac12\deg z'$.
     - Witten's formula gives zero already for $n=1$, because the factor $\sinh^4$ is even.
   - Split spheres whose halves are embedded $(-2)$-spheres are killed by the composite of the two Dehn–Seidel twists, which maps $S$ to $-S$ and fixes $w$ modulo $2$ **[PLAUSIBLE]**. The manuscript's halves are not embedded spheres; they are trace classes of a genus-two knot.
   - The closed theorem is therefore true and applicable, but we know no closed case in which it is the *only* proof. **[SPECULATIVE]**: we expect this to be the general situation.
7. **Split spheres alone are not enough.** We expect that no purely numerical closed statement holds even for split spheres with $w$ even on the halves. The reason is the possible gain of $\Theta$ on the halves when $\Lambda$ is not pinned.
   - *Example.* Take $E(3)\#2n\overline{\mathbb{CP}}{}^2$ (odd lattice), with $(-2)$-spheres $C_i=A_i-A'_i$ in fibres and $S_i=C_i-e_i+e'_i$.
   - $S_i$ is split, with halves $A_i-e_i$ and $A'_i-e'_i$.
   - The Witten factor is non-zero for $w\cdot A_i$ and $w\cdot e_i$ odd, $w\cdot A'_i$ and $w\cdot e'_i$ even.
   - Up to $n\approx12$ with $b^+=5$.
   - **[SPECULATIVE]**: the simultaneous lattice decompositions $C_i=A_i-A'_i$ were not checked. Theorem A is not contradicted: the per-sphere balance there is $0$.

---

## 7. Relation to the family version, and why the closed version does not suffice

**Dictionary.** Theorem A is the case $\dim Q=0$ of the family statement (`R1-literature.md` (e3) Theorem E and Proposition E′; `T1-secondary.md` Thm. A and Thm. 4.1).

*Unchanged:*
- the cut-down $\mathrm{SO}(3)$-monopole one-manifold;
- FL2b Prop. 3.29 at the instanton end;
- the incidence lemma (T2 Cor. 3.3), which gives $\ell\ge T(v)$;
- Lemma B, with the halves $F_{l,i}$ and $F_{r,i}$;
- the Stokes argument.

*Added in the family:*
- the cube $Q=[-1,1]^n$ of neck lengths, with one parameter for each sphere;
- $J$-faces (necks $S^3$) and lens faces (necks $L(4,1)$, minimal trace cap $\kappa=\tfrac14$);
- the bit sum over $w_e=w_0+\sum e_i\,\mathrm{PD}(S_i)$, needed because single-bundle counts jump at lens faces;
- broken limits, which force the *local* spacing condition;
- the projection for mixed limits (AP6);
- chamber conditions on the positive pieces, uniform over $\bar Q$.

**Why the closed version does not suffice.**
1. **Topology** **[VERIFIED]**, from `T1-secondary.md` Rem. 1.6.
   - $X_M$ is a connected sum along the spheres $J_i\cong S^3$, with $b^+>0$ on both sides of each, so $D^w_{X_M}\equiv0$ for every $w$. Theorem A applied to $X_M$ proves $0=0$.
   - The cosmetic input gives $\Omega(X_M)=\pm\langle\Psi_+,w^M\Psi_-\rangle\not\equiv0\pmod{2^N}$. This is a secondary invariant over the cube of metrics, not carried by any closed invariant.
2. **Arithmetic.** Even a hypothetical closed manifold with the same local data and no $S^3$ necks could not be handled by Theorem A.
   - *Supply.* Without parameters, $8\kappa=2n+3m+c$: each insertion supplies $\tfrac14$ rather than $\tfrac18$.
   - *Index.* With $\Theta=m+\Theta_0$, one gets $n_D=\tfrac18(5m-2n)+c_1$, so $n_D\ge1$ needs $m/n>\tfrac25$.
   - *Exclusion.* The absorption of two insertions by each positive piece (`numerology.tex` §2) gives $\ell-T\le\tfrac18(7m-2n)+C$, so exclusion needs $m/n<\tfrac27$.
   - These are incompatible. With the parameters, the same accounting gives $\tfrac15<m/n<\tfrac37$.
   - The same conclusion appears at fixed $n_D$. By the identity of §1, each manuscript sphere changes the effective level by $2s-\Theta_R-c$, where $s$ is the energy supplied, $c=\tfrac12$ is the cost of Lemma B, and $\Theta_R$ is the Dirac index carried by its two halves. The pinning gives $\Theta_R=0$. So the change is $2\cdot\tfrac14-\tfrac12=0$ in the closed problem, and $2\cdot\tfrac18-\tfrac12=-\tfrac14$ in the family.
   - **[VERIFIED]**: arithmetic, given the block table of `numerology.tex` and the identity of §1.
3. **Division of labour.** The closed prototype shows that the *exclusion mechanism itself is classical*: incidence plus level, with no gluing at reducibles. The difficulty of the cosmetic argument lies entirely in the family features listed above, chiefly AP6 and the uniform chamber conditions. **[PLAUSIBLE]**

**The four features the mechanism uses**, each visible in the closed prototype:
- (a) split spheres;
- (b) $w$ even on the halves, so cost $\tfrac12$ (Lemma B);
- (c) $\Lambda$ pinned on the negative pieces, so $\Theta_N=0$ and $n_D$ must come from $b^+$ (§4);
- (d) the family parameter, which halves the supply.

What happens when one feature is missing:
- Without (a) or (b), the cost falls to $\tfrac14$, and the conics and $E(4)$ give non-zero invariants (§2).
- Without (c), the halves may carry Dirac index. Then $n_D$ is no longer forced to come from $b^+$, and the accounting depends on the gluing of the lattice rather than on the count of spheres (§4; §6, item 7).
- Without (d), the window is empty (item 2 above).

---

## 8. Status

| Claim | Label | Confidence |
|---|---|---|
| Naive statement N is false for every bound: conics (Prop. 2.1) | VERIFIED | 99% |
| Lone-sphere counterexamples, $E(4)$ and $K3\#32\overline{\mathbb{CP}}{}^2$ (Prop. 2.2) | VERIFIED; $E(4)$ section count PLAUSIBLE | 95% |
| Theorem A as a reduction to FL2b Prop. 3.29, Lemma 3.15, Cor. 3.18 and the incidence lemma | VERIFIED (logic) | 95% |
| Transversality of jumping-line representatives in FL's compactification (step 0) | PLAUSIBLE | 85–90% |
| Theorem A′ (basic classes only) | PLAUSIBLE; conditional on FL2b Conj. 3.34 and Memoir Hyp. 7.8.1 | — |
| Lemma B and Corollary C | VERIFIED | 98% |
| Pinning: $w\equiv0$ on $N\cong\langle-1\rangle^2$ forces $\Theta_N\le0$ | VERIFIED | 98% |
| Identity $\ell-n_D=2\kappa+\tfrac14(K^2+\sigma)-\tfrac12K\cdot\Lambda$ and the pair form | VERIFIED | 99% |
| Proposition D (only $K\cdot S_i=\pm2$ contribute) | VERIFIED given Witten's formula and OS/FS | 90% |
| Computer tests ($K3\#r$: exclusion $\Leftrightarrow$ vanishing; $E(4)$ consistent) | VERIFIED | 95% |
| Closed window empty, family window $(\tfrac15,\tfrac37)$ | VERIFIED (arithmetic) | 95% |
| No closed case where Theorem A is the only proof; split spheres alone insufficient | SPECULATIVE | — |

**Recommended statement for the Strategy section.** Use Theorem A together with Lemma B and Corollary C as the closed prototype. Then state plainly:
- that the naive count is false (conics);
- that the closed accounting is at best even for the manuscript's spheres;
- that the family parameter is what makes it unfavourable.
