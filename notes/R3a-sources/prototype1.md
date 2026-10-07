# Round 3a, prototype attempt 1: what a closed four-manifold says about $\mu$-insertions of $(-4)$-spheres

Labels: **[V]** verified, by hand or by the short computations in `round3a/scripts/` (`identities.py`, `examples.py`, `pinned_theta.py`); **[P]** plausible; **[S]** speculative. Theorem numbers are those of the arXiv sources, recomputed from their LaTeX counters. Sources downloaded for this note are in `round3a/src/`.

Abbreviations: KM94 = Kronheimer–Mrowka, math/9404232; FSblow = Fintushel–Stern, *The blowup formula for Donaldson invariants*, alg-geom/9405002; FSrb = Fintushel–Stern, *Rational blowdowns of smooth 4-manifolds*, alg-geom/9505018; FL2b = dg-ga/9712005; FKLM = Feehan–Kronheimer–Leness–Mrowka, *PU(2) monopoles and a conjecture of Mariño, Moore and Peradze*, math/9812125; Memoir = math/0203047.

---

## 0. Verdict

1. **The naive statement is false [V].** "Many disjoint $(-4)$-spheres for each positive direction of the intersection form force $D^w_X(\mu(S_1)\cdots\mu(S_n)z)=0$" fails already for blow-ups of $K3$: $X_n=K3\#n\overline{\mathbb{CP}}{}^2$ has $b^+=3$ and contains $n$ disjoint conics $S_i$, $[S_i]=2e_i$, $S_i^2=-4$, and for $w=\sum e_i$ (which is $\equiv w_2(X_n)$) one has $D^w_{X_n}(\mu(S_1)\cdots\mu(S_n)\,x)=2^n D_{K3}(x)=\pm2^{n+1}$. A minimal example: $E(4)$ has $b^+=7$, nine disjoint sections of square $-4$, and $D_{E(4)}(x\,\mu(\sigma_1)\cdots\mu(\sigma_9)\,\mu(h))\ne0$. (§2, §6.)

2. **The correct closed prototype has two parts, and they do not interact.**
   - **Theorem A (selection rule) [V, unconditional].** For a manifold of Kronheimer–Mrowka simple type the multilinear coefficient of $\mu(S_1)\cdots\mu(S_n)$ is $\sum_K \pm a_K\prod_i\langle K,S_i\rangle$, and Fintushel–Stern's adjunction inequality for embedded spheres of negative square gives $\langle K,S_i\rangle\in\{0,\pm2,\pm4\}$. At the top Feehan–Leness level the analogous selection reads $\langle K-\Lambda,S_i\rangle\neq0$ (FL2b Cor. 4.7). (§3, §4.2.)
   - **Theorem B (energy count) [V as a consequence of FKLM Thm. 1.3, which assumes FKLM Conj. 3.1].** $D^w_X(\mu(S_1)\cdots\mu(S_n)z_0)=0$ for $w\equiv w_2(X)$ whenever $n+\tfrac12\deg z_0\le c(X)-1$, where $c(X)=b^--\tfrac12(9b^++7)$. If the spheres carry $2n$ negative-definite directions (each $S_i$ a difference of two orthogonal classes of square $-2$, as in the cosmetic configuration), this holds as soon as $n\ge \tfrac12\deg z_0+\tfrac12(9b^++9)$. (§5.)
   - **They do not interact [V].** For a conjugate pair $\pm K$ and every $\Lambda$, $2n_D-\ell(K)-\ell(-K)=c(X)-\delta-2d_s(K)$. With the incidence condition for the spheres this shows that in a closed manifold $\mu(S)$-insertions are at best neutral: a closed vanishing theorem is driven by $c(X)$, i.e. by negative-definite directions, not by the insertions. (§4.3.)

3. **Why the family argument needs $b^+$ [V].** The sum over the bundles $c_e=c_0+\sum e_i\,\mathrm{PD}(S_i)$, which the lens faces require, has constant $n_D$ only if $\Lambda\cdot S_i\equiv2\pmod 4$. Under that condition a chain of negative pieces contributes at most $\tfrac12$ to $\Theta=(\Lambda^2-\sigma)/4$, however long it is, whereas without it each negative direction can contribute $\tfrac14$, which is exactly the mechanism behind Theorem B. (§7.1.)

4. **Why families [V, arithmetic].** Without the family parameter each insertion still costs more energy than it supplies ($\tfrac12$ against $\tfrac14$), but it also lowers $n_D$ by $\tfrac14$, and restoring that with positive pieces costs $\tfrac{7}{20}$ per sphere. The admissible range is $\tfrac{8s}{5}<\tfrac mn<\tfrac{4-8s}{7}$, where $s$ is the energy supplied per insertion. It is nonempty iff $s<\tfrac5{24}$: empty for $s=\tfrac14$ (closed), equal to $(\tfrac15,\tfrac37)$ for $s=\tfrac18$ (family). (§7.2.)

5. **FL2b Thm. 3.33(a) with Prop. 3.29 cannot give a nontrivial closed prototype by itself [V as logic].**
   - As published, its hypothesis (3.68) concerns every $\mathfrak s$ with $M_{\mathfrak s}\ne\emptyset$ for the $\Lambda$-perturbed equations, on all of $\bar{\mathcal M}_{\mathfrak t}$; the insertions play no role in it.
   - Its cut-down refinement (no reducible in the closure of the cut-down one-manifold, at any level) does use the insertions, but by item 2 it gains nothing in a closed manifold.

---

## 1. Conventions

$X$ is closed, oriented, smooth, with $b_1=0$. For a spin$^u$ structure $\mathfrak t$ with $w=c_1(E)$, $\Lambda=c_1(\mathfrak t)\equiv w+w_2(X)\pmod 2$ and $p_1(\mathfrak t)=-4\kappa$ (FL2b, Memoir (2.1.12)):
$$d_a=8\kappa-\tfrac32(\chi+\sigma),\qquad n_D:=n_a=\tfrac14(\Lambda^2-\sigma)-\kappa=\Theta-\kappa,\qquad \ell(K)=\kappa+\tfrac14(K-\Lambda)^2,\qquad d_s(K)=\tfrac14(K^2-2\chi-3\sigma).$$
Here $K=c_1(\mathfrak s)$ is a Seiberg–Witten class, $v=K-\Lambda\equiv w\pmod2$, and $\ell(K)$ is the Feehan–Leness level of the stratum $M_{\mathfrak s}\times\mathrm{Sym}^\ell X$; it is an integer. Write $\delta=\tfrac12\deg z=\tfrac12 d_a$ and $c(X)=-\tfrac14(7\chi+11\sigma)=b^--\tfrac12(9b^++7)$ **[V]**. In FL2b's notation $i(\Lambda)=\Lambda^2+c+\chi+\sigma$, $r(\Lambda,K)=-(K-\Lambda)^2-\tfrac34(\chi+\sigma)$, and **[V]**
$$n_D=\tfrac14\big(i(\Lambda)-\delta\big),\qquad \ell(K)=\tfrac14\big(\delta-r(\Lambda,K)\big).$$
$S_1,\dots,S_n\subset X$ are disjoint embedded spheres with $S_i\cdot S_i=-4$, and $S^\perp=\{h:h\cdot S_i=0\ \forall i\}$.

---

## 2. The naive statement and why it fails

**Naive statement.** If $n$ is large compared with $b^+(X)$, then $D^w_X(\mu(S_1)\cdots\mu(S_n)z)=0$.

**Counterexample 1 (conics in blow-ups) [V].** Let $Z$ be any manifold with $D^{w_Z}_Z(z)\neq0$ and $X_n=Z\#n\overline{\mathbb{CP}}{}^2$. The conic of the $i$-th summand is an embedded sphere $S_i$ with $[S_i]=2e_i$ and $S_i^2=-4$, and the $S_i$ are disjoint.
- FSblow gives $D^{w+e}_{\hat X}(e^kz)=D^w_X(S_k(x)z)$ with $S(x,t)=e^{-t^2x/6}\sigma(t)$, so $S_1=1$.
- Iterating, $D^{w_Z+\sum e_i}_{X_n}(\mu(S_1)\cdots\mu(S_n)z)=2^nD^{w_Z}_Z(z)\neq0$ for every $z\in\mathbb A(Z)$.
- For $Z=K3$ this is the example of §0: $w_Z=0$ and $\mathbf D_{K3}=e^{Q/2}$, so $D_{K3}(x)=2$, up to the global sign convention. Here $b^+=3$ for every $n$, and $w=\sum e_i\equiv w_2(X_n)$.
- The same value follows from Theorem A below (`examples.py`, (E1): the coefficient is $2^n$ times that of $K3$).

**Counterexample 2 (a minimal manifold) [V].** $E(4)$ has $b^+=7$, $b^-=39$, and nine disjoint sections $\sigma_1,\dots,\sigma_9$ with $\sigma_i^2=-4$ (FSrb §7). Its Donaldson series is $e^{Q/2}\sinh^2 f$, with basic classes $0,\pm2f$, and $\langle\pm2f,\sigma_i\rangle=\pm2$. The class $h=4f+\sum\sigma_i$ lies in $S^\perp$ with $f\cdot h=9$. By Theorem A the multilinear coefficient is $2^8e^{Q(h)/2}\sinh(2f\cdot h)$, so $D_{E(4)}(x\,\mu(\sigma_1)\cdots\mu(\sigma_9)\,\mu(h))=2^{10}\cdot 9\neq0$, up to the global sign convention. The rational blowdowns $W_k$ of $k$ of these sections give further examples with $9-k$ spheres. By FSrb §7, $\mathbf D_{W_k}=2^{k-1}e^{Q/2}\cosh\kappa_k$, where $\kappa_k$ descends from $2f$. The remaining sections lie in the complement of the blown-down ones, so $\kappa_k\cdot\sigma_j=2f\cdot\sigma_j=2$.

**What the examples show.** A conic or a section is a "lone" $(-4)$-sphere: it occupies one negative-definite direction, and a basic class pays for meeting it exactly what the insertion supplies (§§4.2–4.3). The cosmetic configuration differs. There each $S_i=F_{l,i}-F_{r,i}$ is a difference of two classes of square $-2$, so each sphere carries two negative-definite directions. Proposition C and Theorem B show that this, and only this, is what makes "many spheres" force vanishing in a closed manifold.

---

## 3. Theorem A: the selection rule

**Theorem A [V].** Let $X$ be simply connected with odd $b^+\ge3$ and of Kronheimer–Mrowka simple type, with basic classes $K_s$ and coefficients $a_s$ (KM94 Thm. 1; for general $w$, FSrb Thm. 4.1 and FL6 Thm. 2.2):
$$\mathbf D^w_X(h)=D^w_X\big((1+\tfrac x2)e^h\big)=e^{Q(h)/2}\sum_s(-1)^{\frac12(w^2+K_s\cdot w)}a_s\,e^{\langle K_s,h\rangle}.$$
Then for $h\in S^\perp$:
1. The coefficient of $t_1\cdots t_n$ in $\mathbf D^w_X(h+\sum t_iS_i)$ is
$$\sum_{k\ge0}\frac{D^w_X(\mu(S_1)\cdots\mu(S_n)h^k)+\tfrac12D^w_X(x\,\mu(S_1)\cdots\mu(S_n)h^k)}{k!}=e^{Q(h)/2}\sum_s(-1)^{\frac12(w^2+K_s\cdot w)}a_s\prod_{i=1}^n\langle K_s,S_i\rangle\,e^{\langle K_s,h\rangle}.$$
2. (Fintushel–Stern) For every basic class, $\langle K_s,S_i\rangle\in\{0,\pm2,\pm4\}$; the values $\pm4$ occur only in the special case of FSrb Thm. 4.3.
3. Hence $D^w_X(\mu(S_1)\cdots\mu(S_n)z)=0$ for all $z\in\mathbb A(S^\perp)$ if and only if, for each functional $\varphi$ on $S^\perp$, the signed sum of $a_s\prod_i\langle K_s,S_i\rangle$ over the $K_s$ with $K_s|_{S^\perp}=\varphi$ vanishes. In particular it vanishes if every basic class is orthogonal to some $S_i$.

*Proof.*
- (1) Since $h\perp S_i$ and $S_i\cdot S_j=-4\delta_{ij}$, $Q(h+\sum t_iS_i)/2=Q(h)/2-2\sum t_i^2$. The factor $e^{-2\sum t_i^2}$ has no multilinear terms, and $e^{\langle K,h+\sum t_iS_i\rangle}=e^{\langle K,h\rangle}\prod_ie^{t_i\langle K,S_i\rangle}$.
- (2) FSrb Thms. 4.2–4.3, quoting Fintushel–Stern, *Donaldson invariants of 4-manifolds with simple type*, J. Differential Geom. 42 (1995).
  - For a class $u$ represented by an immersed sphere with no positive double points, a basic class either satisfies $-2\ge u^2+|K\cdot u|$, i.e. $|K\cdot u|\le2$ when $u^2=-4$, or satisfies $K\cdot u=\pm u^2=\mp 4$. In the second case a relation $\sum a_se^{K_s+u}-(-1)^{(1+b^+)/2}\sum a_se^{-K_s-u}=0$ holds among such classes.
  - $K\cdot u$ is even because $K$ is characteristic and $u^2$ is even.
- (3) is a restatement of (1). ∎

**Remarks.**
- In the conic examples every basic class has $\langle K,S_i\rangle=\pm2$, so nothing is selected away **[V]**.
- In $K3$ the only basic class is $0$. So for the eight disjoint $(-4)$-spheres obtained by tubing pairs of the sixteen disjoint $(-2)$-spheres of a Kummer surface, $D(\mu(S_1)\cdots\mu(S_n)z)=0$ for every $n\ge1$ and every $z\in\mathbb A(S^\perp)$. This holds for a reason unrelated to counting **[V]**.
- Theorem A is the closed form of the first half of mechanism (3): an insertion is seen only by classes that pair nontrivially with the sphere. It contains no energy and no $b^+$.

---

## 4. The Feehan–Leness count in a closed manifold

### 4.1 Feehan–Leness's vanishing theorem as published

**FL2b Thm. 3.33(a) [V, quoted].**
- *Hypotheses:* $b^+>0$; $w$ good; $d_a\le\deg z\le d_a+2n_D-2$; $z$ intersection-suitable (true when $b_1=0$, FL2b Lemma 3.17); generic data; and, by (3.68), $(\Lambda-c_1(\mathfrak s))^2<p_1(\mathfrak t)$ (that is, $\ell<0$) for *every* $\mathfrak s$ with $M_{\mathfrak s}\neq\emptyset$.
- *Conclusion:* $\#(\bar{\mathcal V}(z)\cap\bar M^w_\kappa)=0$.
- *Proof:* Stokes on the one-manifold $\bar{\mathcal V}(z)\cap\bar{\mathcal W}^{n_D-1}\cap\bar{\mathcal M}^{*,\ge\varepsilon}_{\mathfrak t}/S^1$. Cor. 3.18 keeps it away from the lower irreducible strata, and Prop. 3.29 evaluates the instanton end as $2^{n_D-1}\#(\bar{\mathcal V}(z)\cap\bar M^w_\kappa)$.
- FL2b Thm. 1.2(a) restates it as: $\delta<i(\Lambda)$ and $\delta<r(\Lambda)$ imply $D^w_X(z)=0$, where $r(\Lambda)$ is the minimum of $r(\Lambda,c_1(\mathfrak s))$ over $\mathfrak s$ with $M_{\mathfrak s}\ne\emptyset$. Replacing these $\mathfrak s$ by the basic classes requires "effectiveness", FL2b Conj. 3.34 (= FKLM Conj. 3.1).

Two features matter here.
1. The set $\{\mathfrak s:M_{\mathfrak s}\neq\emptyset\}$ depends on the metric and on the perturbation $F^+_{A_\Lambda}$, and it can contain classes with zero invariant and positive-dimensional moduli spaces. So the hypothesis cannot be checked from Seiberg–Witten invariants alone **[V for the dependence; P that such classes occur when $\Lambda^2$ is large]**.
2. The hypothesis is on all of $\bar{\mathcal M}_{\mathfrak t}$. The insertions $\mu(S_i)$ enter only through $\deg z$, where they raise $\kappa$ by $\tfrac14$ each and so make (3.68) harder to satisfy **[V]**.

### 4.2 The incidence condition (how $\mu(S_i)$ excludes reducibles)

The proof of Thm. 3.33(a) needs only that no reducible lies in the closure of the cut-down one-manifold. That is a weaker hypothesis, and it is where the insertions act.

**Incidence.** A stratum $M_{\mathfrak s}\times\mathrm{Sym}^\ell X$ with $v=c_1(\mathfrak s)-\Lambda$ can meet that closure only if $\ell\ge T(v):=\#\{i:\langle v,S_i\rangle=0\}$. Each sphere with $\langle v,S_i\rangle=0$ needs one of the $\ell$ points on it, and disjoint spheres need distinct points.
- *At level $0$ [V]:* this holds cohomologically. FL2b Cor. 4.7 gives, for $b_1=0$, $\gamma^*\mu_p(h)=\tfrac12\langle c_1(\mathfrak s)-\Lambda,h\rangle(2\mu_{\mathfrak s}(x)+\nu)$ on the link. FL2b Thm. 4.13 then evaluates the link pairing of $z_0\prod\mu(S_i)$ with the factor $\prod_i\langle v,S_i\rangle$, by polarizing $\langle c_1(\mathfrak s)-c_1(\mathfrak t),h\rangle^{\delta_2}$. So under the standing hypothesis of FL2b Thm. 3.33 (all reducibles at level $0$), Thm. 3.33(b) is a top-level selection rule with $\langle K-\Lambda,S_i\rangle$ in place of Witten's $\langle K,S_i\rangle$.
- *At level $\ell\ge1$ [P]:* cohomologically this needs the Memoir's links, which are conditional on Memoir Hyp. 7.8.1. At the level of representatives it is the jumping-line incidence of `notes/T2` Cor. 3.3. The resulting cut-down form of Thm. 3.33(a) is R1's Theorem E with no parameters; its proof is FL's, but it is not published.
- *Two selection rules [P].* With $\Lambda\cdot S_i=2$ the classes missed by the Feehan–Leness incidence are those with $K\cdot S_i=2$, not $K\cdot S_i=0$. The two rules are reconciled by the bubble terms at positive level, which the cohomological formulas contain (FLL1 Lemma 4.10 at level one).

**Cost of meeting a sphere [V].** Assume, as in the cosmetic setting, that $w\cdot S_i$ is even. If $\langle v,S_i\rangle\neq0$ then $|\langle v,S_i\rangle|\ge2$, because $v\equiv w\pmod 2$.
- The component of $v$ in the span of the $S_i$ contributes at least $\tfrac14$ to $-\tfrac14v^2$ for each met sphere, since $\langle v,S_i\rangle^2/16\ge\tfrac14$. The orthogonal component is not controlled by the spheres.
- If $S_i=A_i-B_i$ with $A_i,B_i$ orthogonal of square $-2$ and $w\cdot A_i$, $w\cdot B_i$ even, one of $\langle v,A_i\rangle,\langle v,B_i\rangle$ is a nonzero even number. Then the component of $v$ in the span of the $A_i,B_i$ contributes at least $\tfrac12$ to $-\tfrac14v^2$ for each met sphere. This is the "$\tfrac12$" of the strategy.
- A missed sphere costs one whole level, through its bubble.

### 4.3 Proposition C: the balance identity

**Proposition C [V] (`identities.py` [1]).** For every closed $X$ with $b_1=0$, every $\Lambda\equiv w+w_2(X)$, every $z$ with $\deg z=d_a$ and every class $K$,
$$2n_D-\ell(K)-\ell(-K)=c(X)-\delta-2d_s(K).$$
The left side does not depend on $\Lambda$. For basic classes of Seiberg–Witten simple type, $d_s(K)=0$.

*Proof.*
- $\ell(K)+\ell(-K)=2\kappa+\tfrac12(K^2+\Lambda^2)$, and $2n_D=\tfrac12(\Lambda^2-\sigma)-2\kappa$, so $\Lambda^2$ cancels.
- Substitute $4\kappa=\delta+\tfrac34(\chi+\sigma)$. ∎

**Consequences [V].**
1. *Feehan–Leness exclusion has a fixed range.* Excluding a conjugate pair ($\ell(\pm K)\le-1$) with $n_D\ge1$ requires $c(X)-\delta\ge4$.
   - For $w\equiv w_2(X)$ and odd $b^+$ the degree condition $2\delta\equiv-2w^2-\tfrac32(\chi+\sigma)\pmod 8$ gives $\delta-c(X)\equiv\chi+\sigma=2+2b^+\equiv0\pmod4$. So this reads $\delta<c(X)$.
   - This is the range of FKLM Thm. 1.3. With $\Lambda\perp K$ it is FL2b's identity $i(\Lambda)+r(\Lambda)=2c(X)$.
2. *Insertions are at best neutral in a closed manifold.* Take $z=z_0\prod_i\mu(S_i)$, so $\delta=\delta_0+n$, and use incidence: what must be negative is $\ell-T$.
   - If $\langle K,S_i\rangle\ne0$ for all $i$, then $\langle v(K),S_i\rangle$ and $\langle v(-K),S_i\rangle$ differ by $2\langle K,S_i\rangle\neq0$, so $T(K)+T(-K)\le n$.
   - Hence $2n_D-[\ell(K)-T(K)]-[\ell(-K)-T(-K)]=c(X)-\delta_0-2d_s(K)-\big(n-T(K)-T(-K)\big)$, and the bracket is $\ge0$.
   - So for the classes that Theorem A selects, excluding $\pm K$ with the insertions requires $c(X)-\delta_0\ge4$, which is the condition for excluding $\pm K$ in the problem with $z_0$ alone. The $n$ insertions never relax it. At best (each sphere missed by exactly one of $\pm K$) they are neutral.
   - The classes with some $\langle K,S_i\rangle=0$ are those that Theorem A already discards.
3. *Where vanishing comes from.* $c(X)$ grows by $1$ for each negative-definite direction and falls by $\tfrac92$ for each positive direction. A closed vanishing theorem for $\mu(S_i)$-insertions is therefore a theorem about $b^-$ against $b^+$, in which the spheres matter only through the negative-definite directions they occupy.
4. *In a family.* With one interval parameter per insertion, $\deg z-\dim Q=d_a$ gives $\delta=\delta_0+\tfrac n2$. The incidence gain $T(K)+T(-K)$, of size up to $n$, can then exceed the $\tfrac n2$ consumed, so the closed obstruction disappears. This is only a necessary condition: in families $d_s$ can be negative on walls, and the actual exclusion is the family adjunction inequality of `notes/T1` Lemma 3.1 **[V for the identity; P for its use]**.

---

## 5. Theorem B: the closed prototype of the energy count

**Theorem B [V as a consequence of FKLM Thm. 1.3].** Let $X$ be closed, oriented and smooth, with $b_1=0$ and $b^+>1$, of Seiberg–Witten simple type and abundant ($B^\perp$ contains a hyperbolic sublattice), and assume FKLM Conj. 3.1 for $X$.
- *Data.* Let $S_1,\dots,S_n$ be disjoint embedded spheres of square $-4$, anywhere in $X$. Let $w\equiv w_2(X)\pmod 2$, and $z_0=h_1\cdots h_jx^m$ with $\delta_0=j+2m$.
- *Conclusion.* If
$$n+\delta_0\le c(X)-1=b^-(X)-\tfrac12\big(9b^+(X)+9\big),$$
then $D^w_X(\mu(S_1)\cdots\mu(S_n)z_0)=0$.
- *Configuration of the cosmetic argument.* Suppose each $S_i=A_i-B_i$ with $A_1,B_1,\dots,A_n,B_n$ pairwise orthogonal of square $-2$, so that $b^-\ge2n$. Then the hypothesis holds as soon as
$$n\ \ge\ \delta_0+\tfrac12(9b^++9).$$

*Proof.*
- FKLM Thm. 1.3 states $D^w_X(h^{d-2m}x^m)=0$ for $0\le d\le c(X)-1$, $m\ge0$ and every $w\equiv w_2(X)$. Polarization gives the multilinear form, with $d=n+j+2m$.
- $c(X)=b^--\tfrac12(9b^++7)$ when $b_1=0$, and $b^-\ge2n$ in the second case **[V]** (`identities.py` [3]).
- *Status.* FKLM Conj. 3.1 says that strata with $SW=0$ contribute nothing at any level. It is proved at level $0$ (FL2b Thm. 4.13) and follows from the Memoir's cobordism formula, i.e. from Memoir Hyp. 7.8.1 (see also arXiv 1408.5307). Without it, FL2b Thm. 1.2(a) gives the same conclusion provided no $\mathfrak s$ with $M_{\mathfrak s}\neq\emptyset$ and zero invariant lies at nonnegative level. ∎

**Feehan–Leness reading [V for the arithmetic].** Take $\Lambda$ even, in $B^\perp$, with $\Lambda^2=-(\chi+\sigma)$; abundance supplies such classes when the parity allows, and FL2b Thm. 1.1 uses the neighbouring choice $\Lambda^2=2-(\chi+\sigma)$. Then
$$\Theta=\tfrac14(\Lambda^2-\sigma)=\tfrac14(b^--3b^+-2),\qquad \ell(K)=\kappa+\tfrac14(K^2+\Lambda^2),\qquad K^2=2\chi+3\sigma=4+5b^+-b^-.$$
So each negative-definite direction raises $n_D$ by $\tfrac14$ through $-\sigma$, and lowers the level of every basic class by $\tfrac14$ through $K^2$. Each degree-two insertion does the opposite, raising $\kappa$ by $\tfrac14$. A sphere with two negative directions therefore gains $\tfrac14$ in both $n_D$ and level, and a lone sphere gains nothing.

This is mechanism (3) in closed form, with one essential difference: **the cost is automatic.** It is paid because $K$ is characteristic on the negative directions while $\Lambda$ can be taken orthogonal to them. In a blow-up, $\Lambda\in B^\perp$ forces $\Lambda\cdot e_j=0$, and then $w\cdot e_j$ is odd. The insertions do not cause the cost.

**Sharpness on examples [V]** (`examples.py`, order of vanishing).
- $K3\#4n\overline{\mathbb{CP}}{}^2$ with $S_i=e_{4i-3}-e_{4i-2}-e_{4i-1}+e_{4i}$ (halves $e_a-e_b$, $e_c-e_d$) and $w$ odd on every $e_j$, i.e. $w\equiv w_2$: the multilinear coefficient vanishes to order exactly $3n=c-2-n$ in $h\in S^\perp$, for $n=1,2$. Theorem B predicts vanishing below that order, so it is sharp.
- $K3\#2n\overline{\mathbb{CP}}{}^2$ with $n$ conics: the order is exactly $n=c-2-n$ for $n=1,2,3$.
- $K3\#n\overline{\mathbb{CP}}{}^2$ with $n$ conics: the order is $0$, and Theorem B predicts nothing. This is Counterexample 1.

**A degenerate closed case [V].** If the halves $A_i,B_i$ are embedded $(-2)$-*spheres* and $w\cdot A_i$, $w\cdot B_i$ are even, then $D^w(\mu(S_1)\cdots\mu(S_n)z)=0$ for every $n\ge1$ and every $z\in\mathbb A(\langle A_i,B_i\rangle^\perp)$. The reflections in $A_1$ and $B_1$ are realised by diffeomorphisms. They act trivially on $H^+$, fix $w$ modulo $2$ with sign $(-1)^{((Rw-w)/2)^2}=+1$, fix the other $S_j$ and $z$, and send $S_1\mapsto-S_1$. Checked on the blow-up model (`examples.py`, refined grouping). In the cosmetic configuration the halves $F_l,F_r$ are classes of square $-2$ that need not be represented by spheres, so this symmetry is not available in general. Whether an analogous symmetry acts on the family count when they are spheres is not examined here **[S]**.

---

## 6. Tests against examples

Here $c=c(X)$, and "prediction" refers to Theorem B, for $w\equiv w_2$.

| $X$ | $b^+$ | $(-4)$-spheres | $w$ | $D^w(\prod\mu(S_i)z)$ | naive statement | Theorem B |
|---|---|---|---|---|---|---|
| $K3\#n\overline{\mathbb{CP}}{}^2$ | 3 | $n$ conics $2e_i$ | $\sum e_i\ (\equiv w_2)$ | $2^nD_{K3}(z)\ne0$ | fails | silent ($c-1=n+1<n+2$) |
| same | 3 | same | $e_i$-even | $0$ (FSblow $B_1=0$) | holds | not applicable |
| $K3\#2n\overline{\mathbb{CP}}{}^2$ | 3 | $n$ conics | $\equiv w_2$ | $0$ for $z\in\mathbb A(K3)$; order $n$ in $S^\perp$ | holds | holds, sharp |
| $K3\#4n\overline{\mathbb{CP}}{}^2$ | 3 | $n$ spheres with $(-2)$-halves | $\equiv w_2$ | $0$ on $\langle A,B\rangle^\perp$; order $3n$ | holds | holds, sharp |
| $E(4)$ | 7 | 9 sections | $0$ | $\neq0$ | fails ($9>7$) | silent ($c=4$) |
| $W_k$ (FSrb) | 7 | $9-k$ sections | $0$ | $\ne0$ | fails | silent ($c=4-k$) |
| Kummer $K3$ | 3 | 8 tubed pairs | any | $0$ (only basic class $0$) | holds, but not by counting | silent ($c=2$) |

The blow-up entries rest on FSblow and on Theorem A, both **[V]**. $E(4)$ and $W_k$ rest on FSrb §7 **[V]**. The orders of vanishing were computed by exact rational arithmetic **[V]**.

**Conclusion of the tests.** The closed statement that is true is Theorem B. Its threshold involves $b^-$ against $b^+$, not the number of spheres as such. It becomes a statement about spheres outnumbering $b^+$ only when each sphere brings two negative-definite directions.

---

## 7. Relation to the family version, and why the closed version does not suffice

### 7.1 Lemma D: pinning removes the Dirac index of negative pieces

*Why $\Lambda$ is pinned.* The lens-face cancellation sums over the bundles $c_e=c_0+\sum e_i\,\mathrm{PD}(S_i)$, with $\Lambda_e=l+c_e$ for a fixed characteristic $l$. Since
$$\Lambda_e^2=\Lambda_0^2+\sum_ie_i\big(2\Lambda_0\cdot S_i-4\big),$$
$n_D$ is the same for all $2^n$ bundles iff $\Lambda_0\cdot S_i=2$ **[V]**. More generally, $\Lambda_e=\Lambda_0+\sum e_ik_i\,\mathrm{PD}(S_i)$ with $k_i$ odd forces $\Lambda_0\cdot S_i=2k_i\equiv2\pmod4$. The chamber condition on the positive pieces is a separate constraint on $\Lambda|_P$.

**Lemma D [V] (by hand; brute force in `pinned_theta.py`).**
- *Setting.* Let $N_1,\dots,N_L$ be negative pieces, $H_2(N_j)=\langle a_j,b_j\rangle\cong\langle-1\rangle^2$, with halves $F_{r,j}=a_j+b_j$ and $F_{l,j+1}=a_j-b_j$, and $S_i=F_{l,i}-F_{r,i}$ for $2\le i\le L$.
- *Hypotheses.* $w$ pairs evenly with every half, and $\Lambda\cdot S_i\equiv2\pmod4$ for $2\le i\le L$.
- *Conclusion.* $\sum_j\tfrac14\big(\Lambda|_{N_j}^2-\sigma(N_j)\big)\le\tfrac12$.
- *Without the hypothesis on $\Lambda\cdot S_i$*, the sum can be $\tfrac L2$, by taking $\Lambda=0$ on pieces where $w$ is odd.

*Proof.*
- Put $\alpha_j=\Lambda\cdot a_j$ and $\beta_j=\Lambda\cdot b_j$. Since $\Lambda\equiv w+w_2$ and $w\cdot(a_j\pm b_j)$ is even, $\alpha_j\equiv\beta_j\pmod2$. So $p_j=\alpha_j-\beta_j$ and $q_j=\alpha_j+\beta_j$ are even.
- $\Lambda\cdot S_i=p_{i-1}-q_i\equiv2\pmod4$ forces one of $p_{i-1},q_i$ to be $\equiv2\pmod4$, so $p_{i-1}^2+q_i^2\ge4$.
- The pairs $(p_{i-1},q_i)$ are disjoint, so $\sum_j(\alpha_j^2+\beta_j^2)=\tfrac12\sum_j(p_j^2+q_j^2)\ge2(L-1)$, and $\sum_j\tfrac14(2-\alpha_j^2-\beta_j^2)\le\tfrac12$. ∎

**Consequence.**
- In the closed prototype the Dirac index comes from the negative-definite directions, at $\tfrac14$ each, because $\Lambda$ is free to be orthogonal to them.
- In the family argument the sum over $c_e$ forbids this. Negative pieces contribute at most a bounded amount to $n_D$, so $n_D$ must come from positive pieces: $\Theta(P)=1$ for $b^+(P)=1$, a net $+\tfrac58$.
- This is the precise form of strategy item (5). One correction for the Strategy text: $\Lambda\cdot S_i=2$ is forced already by the sum over bundles (constant $n_D$); the chamber condition is an additional constraint on $\Lambda|_P$, and it is what prevents enlarging $\Lambda$ there.

### 7.2 Proposition E: the admissible range of $m/n$, closed against family

**Proposition E [V] (`identities.py` [4]).**
- *Inputs.* A copy of $B$ adds $s$ to $\kappa$, with $s=\tfrac14$ for the bare insertion and $s=\tfrac18$ with its interval of metrics. A positive piece adds $\tfrac38$ to $\kappa$ and $1$ to $\Theta$; negative pieces add nothing (Lemma D). The family adjunction inequality (`notes/T1` Lemma 3.1, sharp) gives $-\tfrac14v^2+T(v)\ge\tfrac12(n-m)-C$.
- *Index.* $n_D=\tfrac58m-sn+O(1)$.
- *Level.* The level bound is $\ell-T\le(s-\tfrac12)n+\tfrac78m+O(1)$.
- *Range.* Both conditions hold for large $n$ iff $\tfrac{8s}5<\tfrac mn<\tfrac{4-8s}7$. This range is nonempty iff $s<\tfrac5{24}$.

| | $s$ | level per sphere | $n_D$ per sphere | range of $m/n$ |
|---|---|---|---|---|
| closed, $\Lambda$ pinned | $\tfrac14$ | $-\tfrac14$ | $-\tfrac14$ | $(\tfrac25,\tfrac27)$: empty |
| family, $\Lambda$ pinned | $\tfrac18$ | $-\tfrac38$ | $-\tfrac18$ | $(\tfrac15,\tfrac37)$ |
| closed, $\Lambda$ free (Theorem B) | $\tfrac14$ | $-\tfrac14$ | $+\tfrac14$ | no positive pieces needed |

A positive piece contributes $+\tfrac78$ to the level bound and $+\tfrac58$ to $n_D$, closed or family.

So "an insertion costs more energy than it supplies" is true with or without the family parameter ($\tfrac12>\tfrac14$). What fails without the parameter is the index. Each insertion lowers $n_D$ by $\tfrac14$, and restoring it with positive pieces costs $\tfrac{7}{20}$ of level per sphere, more than the $\tfrac14$ the sphere gains. With the parameter the gain is $\tfrac38$ and restoring the index costs $\tfrac7{40}$. I suggest the Strategy section add this: the family parameter matters because of the Dirac index, not because of the level alone.

### 7.3 Dictionary

| | closed prototype (Theorems A, B) | family argument (cosmetic) |
|---|---|---|
| invariant | $D^w_X(\mu(S_1)\cdots\mu(S_n)z_0)$ | secondary count $\Omega$ over the cube of metrics, summed over the $c_e$ |
| $\Lambda$ | free; $\Lambda\in B^\perp$ | pinned, $\Lambda\cdot S_i=2$ (sum over $c_e$), chamber condition on $P$ |
| source of $n_D$ | negative directions, $\tfrac14$ each | positive pieces, $\tfrac58$ each (Lemma D) |
| cost to a Seiberg–Witten class | automatic: $K^2=2\chi+3\sigma$ | forced by incidence: $\langle v,S_i\rangle\ne0$ ($\tfrac12$) or a bubble on $S_i$ ($1$) |
| role of $\mu(S_i)$ | degree only (Prop. C); selection (Thm. A) | selection and degree |
| energy per insertion | $\tfrac14$ | $\tfrac18$ |
| vanishing condition | $\delta\le c(X)-1$ | $\tfrac15<\tfrac mn<\tfrac37$, spacing $4$ |
| analytic input | FKLM Thm. 1.3 / FL2b Thms. 1.2, 3.33 (closed, published; Conj. 3.1) | R1 Theorem E with Prop. E′ (family, unpublished) |

### 7.4 Why the closed version alone does not suffice

1. **Nonvanishing is not a closed statement [V].** The capped composite $X_M$ is a connected sum along the $J_i$, with $b^+>0$ on several summands, so $D^w_{X_M}\equiv0$ for every $w$ (Donaldson's connected-sum theorem). The cosmetic input enters through the family map $B$, and only the secondary invariant $\Omega$ sees it.
2. **The closed mechanism is unavailable [V].**
   - Theorem B obtains its index from negative-definite directions, with $\Lambda$ orthogonal to them.
   - Lemma D shows that the sum over the bundles $c_e$, which is forced by the lens faces of $B$, removes this source.
3. **The closed analogue of the family mechanism has no admissible range [V].** With $\Lambda$ pinned, the range of $m/n$ is empty when $s=\tfrac14$ (Prop. E). Independently, Prop. C shows that insertion-driven exclusion is at best neutral in any closed manifold.
4. **What the closed prototype does test [V/P].**
   - It tests the selection rule: Theorem A, and FL2b Cor. 4.7 at the top level.
   - It tests the arithmetic: Prop. C is exact, and Prop. E is checked.
   - It also shows by example that Theorem B is sharp, so the energy count is the right one.
   - It does not test the analytic content of the family theorem: compactness over the cube, the lens-face ends, incidence at positive level, and the projection for mixed limits.

---

## 8. Two sentences for the Strategy section (suggestion)

"In a closed manifold of simple type, Witten's formula (or the Kronheimer–Mrowka structure theorem) shows that $\mu(S_1)\cdots\mu(S_n)$ selects the basic classes with $\langle K,S_i\rangle\ne0$, and the Feehan–Leness count shows what this selection costs. That cost is repaid exactly in a closed manifold ($2n_D-\ell(K)-\ell(-K)=c(X)-\delta$ for every $\Lambda$), so the closed vanishing theorem of this kind is the low-degree theorem $\delta<c(X)=b^--\tfrac12(9b^++7)$, in which spheres help only through the negative-definite directions they carry. The cosmetic argument needs a family because its nonvanishing is a family statement, and because the lens faces pin $\Lambda\cdot S_i=2$, which removes the closed source of Dirac index; with one parameter per sphere the insertion supplies $\tfrac18$ instead of $\tfrac14$, which is exactly what opens the range $\tfrac15<\tfrac mn<\tfrac37$."

---

## 9. Status

| Claim | Label | Confidence |
|---|---|---|
| Counterexamples (conics in $K3\#n\overline{\mathbb{CP}}{}^2$; $E(4)$; $W_k$) | V | 95% |
| Theorem A (multilinear coefficient; $\langle K,S_i\rangle\in\{0,\pm2,\pm4\}$) | V (citing KM94, FSrb Thms. 4.1–4.3) | 95% |
| Top-level selection by $\langle K-\Lambda,S_i\rangle$ (FL2b Cor. 4.7, Thm. 4.13) | V | 90% |
| Incidence at positive level; cut-down form of FL2b 3.33(a) | P | 75% |
| Reconciling $\langle K-\Lambda,S\rangle$ with $\langle K,S\rangle$ via bubble terms | P | 65% |
| Proposition C (balance identity) and its consequences | V | 99% (identity), 90% (consequences) |
| Theorem B (from FKLM Thm. 1.3; conditional on FKLM Conj. 3.1 / Memoir Hyp. 7.8.1) | V as implication | 90% |
| Sharpness of Theorem B on blow-up models | V | 95% |
| Degenerate case: $(-2)$-sphere halves give vanishing by reflection | V | 90% |
| Lemma D (pinning; assumes the choice $\Lambda_e=l+c_e$) | V | 95% |
| Proposition E (range of $m/n$; threshold $s<\tfrac5{24}$) | V given T1 Lemma 3.1 and $\Theta(P)=1$ | 95% |
| "Closed version alone does not suffice" (four reasons, §7.4) | V for items 1–3, P for the reading of item 4 | 90% |
