# Exact levels and the drop between the ±2 surgeries

This is the account of one line of attack: look for maps from the $Y_2$ side to the $Y_{-2}$ side whose level is negative for topological reasons, and try to prove that one of them is injective, or that its failure to be injective is controlled by the middle term of the exact triangles for structural reasons.

Every claim carries one of four labels:
- **PROVED**: a complete argument from the inputs listed in §1.4. The exact triangles are assumed, as rule (c) allows.
- **COMPUTED**: an exact computation. The scripts are in `r6/exact-code/`.
- **PLAUSIBLE**: an argument with a gap, which is named.
- **SPECULATIVE**: a heuristic.

Scripts:
- `ledger.py`: the levels, and the $\rho$-invariants of the lens end.
- `toy.py`: three abstract filtered models.
- `datatest.py`: the tests on torus knots and on the figure-eight knot. It takes the bound on $pq$ as its argument; its outputs are `datatest30.out` and `datatest40b.out`.
- `bottoms.py`: where the bottoms sit, by determinant. Its output is `bottoms.out`.
- `samerep.py`: whether the exact drops come from a shared representation.
- `rankcheck.py`: a rank consequence of Proposition 4.3.

The remaining outputs are `samerep120.out`, `rankcheck120.out`, `toy.out` and `ledger.out`.

`datatest.py` imports the torus-knot generator code `gap16/triangle-code/tk.py`, which was calibrated in ell-1 and triangle-1.

---

## 0. Verdict

**The theorem the strategy aims at.** For every nontrivial knot $K$,
$$m_1=\lambda_0(Y_2)-\lambda_1(Y_{-2})>0\quad\text{and}\quad m_2=\lambda_1(Y_2)-\lambda_0(Y_{-2})>0,$$
ideally $\ge1/16$; or the weaker both-bundle statement
$$\min(\lambda_0,\lambda_1)(Y_2)>\min(\lambda_0,\lambda_1)(Y_{-2}).$$
A cosmetic pair would make $m_1+m_2=0$ and the both-bundle difference $0$.

**The theorem it actually proves** (Theorem 5.1, given the triangles (I) and (II)):
$$m_i\ \ge\ \tfrac18-\delta_i+\min\bigl(\eta_g,\ \eta_a+\eta_b-\beta_T\bigr).$$
Here $\delta_i$ is the depth of absorption of $P_i$ on $Y_2$ by the traceless theory and $\beta_T$ is the boundary depth of $C^{tl}(K)$. So $m_i>0$ whenever $\delta_i<1/8$ and $T$ has no long bar. Neither condition can be supplied by this angle.

1. **Maps of level $-1/16$ for topological reasons exist, but each is null-homotopic or formal.**
   - The flat connection $\gamma_1$ with $\rho=-1$ on the $L(4,1)$ end is the rotation by $\pi/2$ on $-\partial\nu S$. Through it, the exterior $E=W'\setminus\nu S$ gives a chain map $Y_2\to Y_{-2}$ that exchanges the bundles and has level exactly $-1/16-\eta$.
   - That map is the $L(4,1)$-face of the one-parameter odd family on $W'$, and the other face of that family is empty. So it is null-homotopic and vanishes on homology (§4.1). The same holds for its twist by the central character, and for the even and central exteriors.
   - The one-parameter families of level $-1/8$ are, up to these null-homotopies, exactly the triangle homotopies $g_A,g_A'$ (§4.2).
   - The composites of level $-1/16$ through the traceless theory are chain maps of the type of a Toda bracket. They vanish in the strict cone model, so they are not forced to be nonzero (§4.4).
2. **What the triangles give is a two-sided bound (Theorem 5.1, PROVED given the triangles).**
   - Let $\delta_i\ge0$ be the depth of absorption: the gap between the bottom of $H(Y_2,P_i)$ and the lowest class that the singular 2-handle map does **not** send nontrivially into the traceless theory.
   - Then the mixed difference satisfies
     $$\tfrac18-\delta_i+\min(\eta_g,\ \eta_a+\eta_b-\beta_T)\ \le\ m\ \le\ \tfrac3{16}-\delta_i .$$
     The upper bound holds when the bottom class of the target is not in the image of $b$.
   - So $m$ is pinned to a window of width exactly $1/16$, the term of $\gamma_1$. This window is where the $1/16$ enters.
   - In the sharp example $\bar T(2,3)$ we have $\delta=1/8$, and both ends of the window equal $1/16$, so $m_2=1/16$ exactly (§7.4). The upper end is attained by a flat connection on $-E$; the lower end by the flat exterior glued to the minimal cap of energy $1/16$.
3. **This angle cannot prove a drop. It fails for two separate reasons (Theorems 6.1 and 6.2, PROVED and COMPUTED).**
   - **(a) Absorption.** There are filtered models that satisfy every relation of both triangles, every level bound of the ledger, and every positivity of energy that the rules allow, and that are cosmetic: zero mixed drops and zero both-bundle drop. So the drop is not a formal consequence of the triangles and the topological levels, with or without differentials. Real knots do absorb (all det-1 mirror torus knots tested), so no lemma excluding absorption can be true.
   - **(b) Boundary depth of the traceless complex.** Even when the bottom class is **not** absorbed in homology, a long finite bar of $C^{tl}(K)$ can make the mixed difference negative (Model 3: $m_1=-1/16$).
   - The kernel criterion therefore needs $\beta_T<\tfrac18+\eta_a+\eta_b$. That is an upper bound on energies of the traceless differential, i.e. an energy estimate. It is not equivalent to the drop, but rule (a) forbids it.
4. **What the angle does give.**
   - The exact ledger (§2).
   - The bracket theorem (§5), which reduces the drop to the depth of absorption $\delta_i<1/8$, together with control of $\beta_T$.
   - Necessary conditions for a cosmetic pair (Theorem 5.4):
     - both bottoms of $Y$ lie within $1/16$ above the bottom of the traceless theory;
     - every class of the traceless theory below them lies in $\operatorname{im}a_*\cap\operatorname{im}a'_*$;
     - $\operatorname{im}a_*$ is at least as large near the bottom as $H(Y,P_0)$, and $\operatorname{im}a'_*$ as $H(Y,P_1)$.
   - The relation $\ker b_*=\ker b'_*$, so $\operatorname{im}a_*=\operatorname{im}a'_*$ (PLAUSIBLE). It comes from a composite of level $-1/16$.
   - A counting criterion, $N_{\operatorname{im}a}(\lambda+\tfrac18)<N_{A}(\lambda+\tfrac18)\Rightarrow m>0$ for perfect complexes.
     - It is not an energy estimate, and it holds in every mirror torus-knot instance tested.
     - It must fail in a cosmetic pair (Theorem 5.4(d)), so proving it in general is at least as hard as the theorem.
     - Its plainest spectral form already fails for $4_1$ (§9.2).
5. **What is missing is not an estimate but information that is not formal.** Any proof must use something that distinguishes real Floer data from Models 1–3 (§9). Within the angle as posed (maps of exact topological level, their composites, and the triangle relations) I found no such information. **I do not believe this angle, by itself, can prove a drop $>0$.**

---

## 1. Setting and inputs

### 1.1 Manifolds

- $K\subset S^3$ is a knot, $Y_r=S^3_r(K)$, and $X_N$ is the trace of $N$-surgery.
- On $Y_{\pm2}$ there are two bundles: $P_0$ with $w_2=0$ and $P_1$ with $w_2\ne0$.
- I write
  - $A_0=C(Y_2,P_0)$, $A_1=C(Y_2,P_1)$;
  - $B_0=C(Y_{-2},P_0)$, $B_1=C(Y_{-2},P_1)$;
  - $T=C^{tl}(K)$, the irreducible traceless singular complex of $(S^3,K)$ with holonomy parameter $1/4$, with Seifert-framed levels (triangle-1 §1.3).
- $W'=(-X_2^\circ)\cup_J X_{-2}^\circ\colon Y_2\to Y_{-2}$, with $J\cong S^3$.
  - $W'$ is simply connected, with $b^+=0$ and intersection form $\mathrm{diag}(-2,-2)$.
  - The cores form a sphere $S=D_l\cup D_r$ with $S\cdot S=-4$.
  - $\partial\nu S=L(4,1)$, oriented as the boundary of the disc bundle of Euler number $-4$.
- $E=W'\setminus\nu S$, viewed as a cobordism $Y_2\to Y_{-2}$ with middle end $-\partial\nu S$.
  - $b^+(E)=0$.
  - $\pi_1(E)=\pi_1(S^3\setminus K)/\langle\langle\mu^2\lambda,\mu^{-2}\lambda\rangle\rangle$ and $H_1(E)=\mathbb Z/2$.
  - $H^1(E;\mathbb Z/2)\to H^1(L(4,1);\mathbb Z/2)$ is an isomorphism, because the meridian of $S$ is $\mu$.
- $-E\colon Y_{-2}\to Y_2$ has $b^+=1$ and middle end $+\partial\nu S$.

### 1.2 Levels

- For an irreducible flat connection, $c=(3+\rho)/16$, for both bundles.
- A counted instanton of energy $E$ has
  $$c(\text{out})-c(\text{in})=\frac{3b^+}{8}+\frac{i_0-s(F)}8-E-\sum_j\frac{3-h(\gamma_j)+\rho(M_j;\gamma_j)}{16}.$$
  - Here $s(F)=\chi(F)+F\cdot F/2$ is the term of Kronheimer–Mrowka for a map singular along $F$ (triangle-1 (1.1)); $s=0$ for the cores $D_l,D_r$ and for $S$.
  - The *level* of a map is the supremum of the right side over counted instantons. Its *topological part* is the value at $E=0$.
- On $\partial\nu S$ the flat $SO(3)$ connections with generator acting by rotation through $2\pi k/4$ have $\rho=0,1,2,1$ for $k=0,1,2,3$.
  - This is COMPUTED by the APS formula in `ledger.py`, together with $\rho=0$ on $\mathbb{RP}^3$.
  - $\gamma_0$ ($k=2$) is liftable, and $\gamma_1$ ($k=1$) has $w_2\ne0$.
  - The middle-end terms are:
    - on $+\partial\nu S$: $\gamma_1$ gives $3/16$, $\gamma_0$ gives $1/4$;
    - on $-\partial\nu S$: $\gamma_1$ gives $1/16$, $\gamma_0$ gives $0$;
    - central connections give $0$.

### 1.3 The triangles used

**(I)** $A_0\xrightarrow{a}T\xrightarrow{b}B_1\xrightarrow{c}A_0$, and **(II)** $A_1\xrightarrow{a'}T\xrightarrow{b'}B_0\xrightarrow{c'}A_1$.

The maps:
- $a,a'$ are $(-X_2^\circ,D_l)$, singular along the core with holonomy $1/4$.
- $b,b'$ are $(X_{-2}^\circ,D_r)$.
- $c,c'$ are $-E$ with the bundle that is odd on $\partial\nu S$, so the limit there is $\gamma_1$.

The triangle-detection data (DLME Prop. 5.1) for (I):
- homotopies $g_A\colon A_0\to B_1$, $g_M\colon T\to A_0$, $g_B\colon B_1\to T$, with
  $$dg_A+g_Ad=ba,\quad dg_M+g_Md=cb,\quad dg_B+g_Bd=ac;$$
- pentagon maps $h$ with $dh+hd+fg+gf=q$, and $q=\mathrm{id}+dk+kd$.

For (II) the same, with primes.

The bundles: in (I) the trivial bundle on $Y_2$ and the nontrivial one on $Y_{-2}$; in (II) the reverse. **The sum (I)$\oplus$(II) is the triangle whose outer terms are the sums over both bundles.** Its middle term is $T\oplus T$: one copy of the $\tau$-fixed part $C(S^3)\oplus C^{tl}(K)$ for each of the two middle summands $C(\Sigma_2(K))$ of DLME's distance-two triangle upstairs (cover-1 §3.5). Here $C(S^3)=0$ in the irreducible theory.

The rank check fixes this. For positive torus knots,
$$\operatorname{rk}(B_0\oplus B_1)-\operatorname{rk}(A_0\oplus A_1)=2\operatorname{rk}T$$
(for example $5-3=2\cdot1$ for $T(2,3)$, and $36-28=2\cdot4$ for $T(3,5)$). This is impossible with one copy of $T$, since $|\operatorname{rk}B-\operatorname{rk}A|\le\operatorname{rk}(\text{middle})$.

Status: assumed (rule (c)); PLAUSIBLE in triangle-1 §4.2, which names three analytic gaps. Levels: §2.

### 1.4 Other inputs

| input | status |
|---|---|
| The level formula, from the APS index theorem with index additivity [DLME, (index), Def. 5.4] | standard |
| KM's index/action formula for singular connections at holonomy $1/4$ [KM 0806.1053] | standard |
| $\eta>0$ for counted instantons when no flat (or flat singular) connection exists on the cobordism with the given limits; in particular for $W'$ (simply connected) and for the singular mixed family (no traceless representation sends $\lambda$ to $-1$ and to $+1$ at once) | allowed by rule (a); the second is triangle-1 §4.3 |
| Triangle detection [DLME Prop. 5.1] and the filtered vertex lemma (Lemma 3.2) | standard, and PROVED here |
| Faces of the odd nonsingular family on $W'$: the $J$-face is empty and the $L(4,1)$-face is (exterior at $\gamma_1$)$\times$(minimal cap of energy $1/16$) | PLAUSIBLE: dimension count PROVED (§4.1); the gluing at $\gamma_1$ with stabiliser $U(1)$ is not written in the literature (triangle-1 gap 1) |
| B-final Theorem A(e): the even exterior $R_0$ at $\gamma_0$ is null-homotopic, via the $\mu(S)$-cut family $\Phi_c$ of level $+1/8$ | PLAUSIBLE (B-final, 80%) |
| Same-bundle singular family $g_S$ on $(W',S)$ with $dg_S+g_Sd=b'a+R_0$ | PLAUSIBLE (triangle-1 §3.2) |

---

## 2. The ledger of topological levels (PROVED as bookkeeping; COMPUTED in `ledger.py`)

"Level" means the topological part. Every counted instanton lies below it by its energy $\eta\ge0$.

| map | cobordism, family | $b^+$ | $i_0$ | middle end | level | what it is |
|---|---|---|---|---|---|---|
| $a,a'$ | $(-X_2^\circ,D_l)$ | 0 | 0 | – | $0$ | singular 2-handle; $\eta=0$ only at a flat singular connection, i.e. a traceless representation with $\lambda\mapsto-1$ (for $P_0$) or $+1$ (for $P_1$) |
| $b,b'$ | $(X_{-2}^\circ,D_r)$ | 0 | 0 | – | $0$ | the same |
| $c,c'$ | $-E$, odd | 1 | 0 | $\gamma_1$ on $+\partial\nu S$: $3/16$ | $3/16$ | the third map; flat at mixed common points |
| $g_A,g_A'$ | $W'$, interval, nonsingular + singular | 0 | $-1$ | – | $-1/8$ | $\eta>0$ |
| $g_M,g_B$ | $(X_{-2}^\circ,D_r)\cup(-E)$, interval | 1 | $-1$ | $3/16$ | $1/16$ | vertex homotopies |
| $h$ | pentagons | 1 | $-2$ | $3/16$ | $-1/16$ | |
| $k$ | product, interval | 0 | $-1$ | – | $-1/8$ | $q\simeq\mathrm{id}$ |
| $\mathcal E_{\gamma_1}$ | $E$, rigid, odd | 0 | 0 | $\gamma_1$ on $-\partial\nu S$: $1/16$ | $\mathbf{-1/16}$ | the exterior map; null-homotopic (§4.1) |
| $\mathcal E_{\gamma_1}$, one parameter | $E$ | 0 | $-1$ | $1/16$ | $-3/16$ | flat at mixed common points |
| $\mathcal E_{\gamma_0}=R_0$ | $E$, rigid, even | 0 | 0 | $\gamma_0$ on $-\partial\nu S$: $0$ | $0$ | null-homotopic via $\Phi_c$ |
| $\mathcal E_{\gamma_0}$, one parameter | $E$ | 0 | $-1$ | $0$ | $-1/8$ | flat at same-bundle common points |
| $\mathcal E_\theta=R_\theta$ | $E$, central limit | 0 | 0 | $0$ | $0$ | null-homotopic via the even family |
| $g^{ns}$ | $W'$, interval, odd, nonsingular | 0 | $-1$ | – | $-1/8$ | $dg^{ns}+g^{ns}d=\mathcal E_{\gamma_1}$ |
| $g_S,g_S'$ | $(W',S)$, interval, same bundle | 0 | $-1$ | – | $-1/8$ | $dg_S+g_Sd=b'a+R_0$ |
| $\Phi_c$ | $W'$, interval, $\mu(S)$ | 0 | $+1$ | – | $+1/8$ | $d\Phi_c+\Phi_cd=R_0$; $B=\Phi_c-\Phi_{c+PD(S)}$ |
| $H$ | $W_H\colon Y_{-2}\to Y_2$ | 1 | 0 | – | $3/8$ ($\le1/8$ after stretching $L(4,3)$) | the upper bound |
| $\sigma_{+1}$ | $(-X_1^\circ,\text{core})\colon Y_1\to(S^3,K)$ | 0 | 0 | – | $-1/16$ | $s=1/2$ |
| $\sigma_{-1}$ | $(X_{-1}^\circ,\text{core})\colon(S^3,K)\to Y_{-1}$ | 0 | 0 | – | $-1/16$ | $s=1/2$ |

**Exact gaps at common representations (COMPUTED).** Let $x$ be a representation of the knot group that defines generators on both sides. The gap equals the level of the flat connection on $E$ (index $-1$), or equivalently on $-E$ (index $0$). The index is inferred from the gaps; it is the transversality statement E of ell-1. The gaps are:
- $c(Y_2,x)-c(Y_{-2},x)=1/8$ for the same bundle;
- $c(Y_2,x)-c(Y_{-2},x)=3/16$ for the mixed pairs.

The common points are:
- same bundle: $(\alpha,\beta)=(1/4,1/2)$ untwisted and $(1/4,0)$ twisted;
- mixed: $\alpha\in\{1/8,3/8\}$.

`datatest.py` confirms these values exactly for all four ordered pairs of bundles, in every torus knot with $pq\le40$, both chiralities (§7.1). `samerep.py` checks the cases with $pq\le120$ (§7.6).

**Where odd sixteenths come from.** Every level in the ledger lies in $\tfrac18\mathbb Z$ except those carrying a $\gamma_1$-end, and $\sigma_{\pm1}$, whose $s=1/2$ comes from the odd square of the $\pm1$ cores. In $W'$ every surface has even square, so between $Y_{\pm2}$ and $(S^3,K)$ the only odd sixteenth is $\rho(\gamma_1)/16$.

---

## 3. Filtered algebra with nonzero differentials (PROVED)

Work over $\mathbb F_2$ with the $\mathbb Z$-graded lifts of DLME. For a homogeneous chain $x$ of lifted degree $k$, put $\mathrm{CS}(x)=\max$ over its generators, and $c(x)=\mathrm{CS}(x)-k/8$; this does not depend on the lift.

For a nonzero homogeneous class $\xi$, put $c(\xi)=\min$ of $c(x)$ over cycles $x$ representing $\xi$.

The invariants:
- $\lambda(C)=\min_\xi c(\xi)$. This is DLME's $\ell$, or its twisted analogue.
- $V_r(C)=\bigoplus_k\{\xi\in H_k: \xi=0\text{ or }c(\xi)\le r\}$ and $N_C(r)=\dim V_r(C)$, the number of infinite bars born at $c\le r$.
- $\beta(C)$ is the boundary depth in the CS filtration (Usher): the least $\beta$ such that every homogeneous boundary $z$ has a primitive $y$ with $\mathrm{CS}(y)\le\mathrm{CS}(z)+\beta$.

A homogeneous map of degree $D$ and CS-level $L$ has $c$-level $L-D/8$. This is the "level" of §2.

**Lemma 3.1 (energy of the differential).**
- An index-one trajectory from $\alpha$ to $\beta$ counted by $d$ has energy $\mathcal E=\tfrac18+c(\alpha)-c(\beta)$. *Proof:* the level formula on $\mathbb R\times Y$ with $i_0=1$.
- Hence $d$ raises $c$ by less than $1/8$, but it does **not** preserve $c$.
- The length of a finite bar in the CS filtration is $\tfrac18+c(y)-c(z)$, where $dy=z$.
- In particular $\beta(T)\le\tfrac18+(\max c-\min c)$ over $T$, and nothing better follows from topology.

*Remark.* So $c$ is not a filtration of the $\mathbb Z/8$-graded complex, contrary to ell-1 §2.2. The sibling note `r6/critic.md` makes the same correction independently. $\lambda$ is unaffected, because it only involves homogeneous classes. Boundary depth must be measured in the CS filtration within one degree.

**Lemma 3.2 (vertex lemma).**
- *Hypotheses.*
  - $f\colon C\to C'$ and $f'\colon C'\to C''$ are chain maps.
  - $g\colon C\to C''$ satisfies $dg+gd=f'f$.
  - $(f,g)\colon C\to\mathrm{Cone}(f')$ is a quasi-isomorphism.
  - The maps have $c$-levels $\ell_f,\ell_g,\ell_{f'}$.
- *Conclusion.* If $0\ne\xi\in H(C)$ and $f_*\xi=0$, there is a nonzero class $\zeta\in H(C'')$ with
  $$c(\zeta)\le c(\xi)+\max\bigl(\ell_g,\ \ell_f+\ell_{f'}+\beta(C')-\tfrac18\bigr).$$
- *Proof.*
  - Choose a cycle $x$ with $c(x)=c(\xi)$.
  - Write $fx=dy$ with $\mathrm{CS}(y)\le\mathrm{CS}(fx)+\beta(C')$. Since $\deg y=\deg fx+1$, this gives $c(y)\le c(x)+\ell_f+\beta(C')-\tfrac18$.
  - Then $w=gx+f'y$ is a cycle.
  - In the cone, $(fx,gx)-D(y,0)=(0,w)$. Its class is the image of $\xi$, which is nonzero. So $w$ is not a boundary of $C''$. ∎

The $-1/8$ in the second term is the degree shift of the primitive. It is the same $-1/8$ as cover-1's variant of DLME's argument.

**Lemma 3.3 (counting).** If $F\colon C\to C'$ is a chain map of $c$-level $\ell$ and $F_*$ is injective on $V_r(C)$, then $N_{C'}(r+\ell)\ge N_C(r)$. Hence, if $N_{\operatorname{im}F_*}(r+\ell)<N_C(r)$, some nonzero class of $\ker F_*$ has $c\le r$. ∎

**Lemma 3.4.** A chain map of the form $dK+Kd$ is zero on homology, whatever the level of $K$. ∎

---

## 4. Maps of negative topological level from the $Y_2$ side to the $Y_{-2}$ side

### 4.1 Through the $L(4,1)$ end: the exterior map of level $-1/16$

**Proposition 4.1.**
- (a) $\mathcal E_{\gamma_1}\colon A_i\to B_{1-i}$, which counts index-$0$ instantons on $E$ with limit $\gamma_1$ on $-\partial\nu S$, is a chain map of level $-1/16-\eta$. It exchanges the bundles, since $\gamma_1$ has $w_2\ne0$.
  - PROVED as bookkeeping.
  - The chain property is PLAUSIBLE: breaking along the $L(4,1)$ end requires exterior instantons of negative index.
- (b) $\mathcal E_{\gamma_1}=dg^{ns}+g^{ns}d$, where $g^{ns}$ is the one-parameter odd nonsingular family on $W'$. Hence $(\mathcal E_{\gamma_1})_*=0$.
  - PLAUSIBLE: the face count below is PROVED, and the gluing at $\gamma_1$ is the gap of triangle-1.
- (c) Write $\gamma_1'=\gamma_1\otimes\chi$ for the other odd flat connection of the fixed-determinant theory. Then $\mathcal E_{\gamma_1'}=\iota\,\mathcal E_{\gamma_1}\,\iota$, where $\iota$ is the twist by the central character on $Y_{\pm2}$. So $(\mathcal E_{\gamma_1'})_*=0$ as well.
  - PROVED given (b).
  - This answers ell-1's open question 1 in the negative.

*Proof of (b).* The family runs from the metric broken along $J$ to the metric broken along $\partial\nu S$.
- **The $J$-face.** Only the trivial connection is flat on $S^3$, and gluing there costs $h^0=3$. So configurations have index at least $3$ [DLME Lemma 5.9], and the face is empty.
- **The $L(4,1)$-face.**
  - Consider index-$0$ configurations $A_{ext}\#A_{cap}$ with $i_{ext}+i_{cap}+h^0(\gamma)=0$. Caps on $\nu S$ that are odd on $S$ bound $\gamma_1$ or $\gamma_1'$.
  - For $\gamma_1$ the index is $8\mathcal E-\tfrac32$ with $\mathcal E\in\{1/16,9/16,\dots\}$, so it is $-1,3,\dots$. Only the minimal reducible (index $-1$) can occur, and it forces $i_{ext}=0$.
  - For $\gamma_1'$ the least cap has energy $9/16$ and index $3$, so $i_{ext}=-4$, which is excluded.
  - The gluing parameter is $U(1)/(1\times U(1))=\mathrm{pt}$.
- **Conclusion.** The boundary of $g^{ns}$ is $1\cdot\mathcal E_{\gamma_1}$, with no other face (no reducibles, and bubbling drops the index by $8$).

*Proof of (c).* $\chi$ extends over $E$, because $H^1(E;\mathbb Z/2)\cong H^1(L(4,1);\mathbb Z/2)$ (§1.1). On $\partial\nu S$ it restricts to the order-two line bundle, and on $Y_{\pm2}$ it gives $\iota$. Tensoring identifies the two moduli spaces with the same energy and index. ∎

**The other exteriors.**
- $\mathcal E_\theta$ is the face of the even interval family on $W'$ (flat cap, $h^0=3$), so it is null-homotopic at level $-1/8$.
- $\mathcal E_{\gamma_0}=R_0=\partial\Phi_c$ (B-final A(e)), so it is null-homotopic at level $+1/8$.

**The rational blow-down.** Replace $\nu S$ by the rational ball $B_2$, with $\partial B_2=L(4,1)$ and $\pi_1=\mathbb Z/2$. This gives a cobordism $W''\colon Y_2\to Y_{-2}$ with $b^+=0$, $b_1=0$ and flat connections at the same-bundle common points.
- It carries **no mixed bundle**. The class in $H^2(L(4,1);\mathbb Z/2)$ does not extend over $B_2$: the map $\mathrm{Ext}(\mathbb Z/2,\mathbb Z/2)\to\mathrm{Ext}(\mathbb Z/4,\mathbb Z/2)$ induced by the surjection $\mathbb Z/4\to\mathbb Z/2$ is multiplication by $2$, which is $0$.
- Stretching $\partial B_2$ gives $W''_*\simeq\mathcal E_\theta+\mathcal E_{\gamma_0}\cdot(\text{flat }B_2\text{-cap of index }-1)$, which is $\simeq0$.
- Status: PROVED topology; PLAUSIBLE gluing.

**Conclusion of 4.1.** The exact $-1/16$ of the $\rho=-1$ connection is carried only by maps that vanish on homology.

### 4.2 Families with $i_0=-1$ (level $-1/8$)

The one-parameter families between $Y_2$ and $Y_{-2}$, and their boundaries:

| family | boundary | chain map? |
|---|---|---|
| $g_A$, $g_A'$ (mixed: nonsingular + singular) | $ba$, $b'a'$ | no; triangle homotopies |
| $g^{ns}$ (mixed, nonsingular) | $\mathcal E_{\gamma_1}$ | no; null-homotopy |
| $g^{sing}$ (mixed, singular) | $ba+\mathcal E_{\gamma_1}$ | no |
| even nonsingular | $\mathcal E_\theta$ | no |
| $g_S$, $g_S'$ (same bundle, singular) | $b'a+R_0$, $ba'+R_0'$ | no |
| $\Phi_c$ with $\mu(S)$ ($i_0=+1$) | $R_0$ | $B=\Phi_c-\Phi_{c+PD(S)}$ is a chain map, of level $+1/8$ |

Status: PLAUSIBLE, as in the cited notes.

Up to adding null-homotopic maps, the only chain-level structure of level $-1/8$ between the two sides is $(a,g_A)\colon A_0\to\mathrm{Cone}(b)$ and its primed partner. This is triangle detection, and it is DLME's mechanism with $C(S^3)\oplus C(S^3)=0$ replaced by $T$.

### 4.3 The exterior family at $-3/16$: how $g_A$ acts at mixed common points (PROVED as bookkeeping; COMPUTED)

Near the $L(4,1)$ end of its interval, an instanton counted by $g_A$ is an exterior instanton with limit $\gamma_1$ and index $-1$, glued to the minimal cap (index $-1$, energy $1/16$). Its level is therefore
$$-\tfrac18-\tfrac1{16}-\mathcal E_{ext}.$$
At a mixed common representation the exterior is flat of index $-1$. So $g_A$ (or $g_A'$) maps the generator on the $Y_2$ side to the same representation on the $Y_{-2}$ side at the exact level $-3/16$, and $c$ (or $c'$) maps it back at the exact level $+3/16$, through the flat connection on $-E$ of index $0$.

So the triangle maps are computed exactly by topology on mixed common points, and the mixed gap there is exactly $3/16$ (§7.1). This is the only place where the angle produces an exact sixteenth on actual classes.

### 4.4 Composites through the traceless theory (level $-1/16$)

**Proposition 4.2 (PROVED from the triangle relations).** Put
$$\Phi=g_Ag_M+bh_0+h_{-1}b+bk_0+k_{-1}b\colon T\to B_1 .$$
- $\Phi$ is a chain map of level $\le-1/16$.
- In the strict cone model ($B_1=\mathrm{Cone}(a)$, $g_M=h=k=0$) one has $\Phi=0$, and $\Phi=0$ in Models 1–2 of §6.
- So $\Phi_*$ is a secondary composite of Toda-bracket type, and **it is not forced to be nonzero**.

*Proof.* Use $dg_A+g_Ad=ba$, $dg_M+g_Md=cb$, $\partial h_0=q_0+ag_M+g_Bb$, $\partial h_{-1}=q_{-1}+bg_B+g_Ac$ and $q=\mathrm{id}+\partial k$. Then
$$\partial(g_Ag_M)=bag_M+g_Acb,$$
$$\partial(bh_0+h_{-1}b)=bq_0+q_{-1}b+bag_M+g_Acb,$$
$$\partial(bk_0+k_{-1}b)=bq_0+q_{-1}b$$
over $\mathbb F_2$. ∎

So $A_0\xrightarrow{a}T\xrightarrow{\Phi}B_1$ is a chain of maps from the $Y_2$ side to the $Y_{-2}$ side, exchanging the bundles, of level $-1/16$ for topological reasons:
- $-1/8$ from $i_0=-1$ in $g_A$;
- $+1/16$ from $b^+=1$, $i_0=-1$ and the $\gamma_1$-term in $g_M$.

If $\Phi_*$ were nonzero on the bottom class $\tau$ of $T$, we would get $\lambda_1(Y_{-2})\le\mu-1/16$. In the absorbed case ($\mu\le\lambda_0(Y_2)$) that would give $m_1\ge1/16$. This is the cleanest form of what the angle would want. It fails because nothing forces $\Phi_*\tau\ne0$.

**Proposition 4.3 (PLAUSIBLE: needs $g_S$, $g_S'$ and B-final A(e)).**
- $b'\simeq Yb$ for the chain map $Y=b'g_B+g_Sc+\Phi_cc\colon B_1\to B_0$, with homotopy $g_Sg_M+\Phi_cg_M+b'h_0+\dots$.
- The leading term $g_Sg_M$ has level $-1/16$.
- Symmetrically $b\simeq Y'b'$.
- Hence $\ker b_*=\ker b'_*$, and by exactness $\operatorname{im}a_*=\operatorname{im}a'_*\subset H(T)$.
- In a cosmetic pair this forces $\operatorname{rk}a_*=\operatorname{rk}a'_*=\operatorname{rk}b_*=\operatorname{rk}b'_*$ and $\operatorname{rk}I(Y,P_0)=\operatorname{rk}I(Y,P_1)$.

*Proof sketch.* With $\partial g_S=b'a+R_0$ and $R_0=\partial\Phi_c$, the same algebra as in Proposition 4.2 gives $\partial(g_Sg_M+\Phi_cg_M+b'h_0+\dots)=b'+Yb$.

The levels of $Y$ are $1/16$, $1/16$ and $5/16$, the last coming from $\Phi_c$. So the relation carries no useful filtered information, only the equality of kernels.

A consequence that does not need a cosmetic pair: $\operatorname{rk}a_*=\operatorname{rk}a'_*$ and $\operatorname{rk}b_*=\operatorname{rk}b'_*$, so
$$\operatorname{rk}B_1-\operatorname{rk}A_0=\operatorname{rk}B_0-\operatorname{rk}A_1 .$$
This holds in all 44 torus-knot cases with $pq\le40$ and for $4_1$ (`rankcheck.py`, COMPUTED). It is a weak test, since it also follows from triangle-1's rank identities. It is consistent with all data: $a=a'=0$ for positive torus knots, $b=b'=0$ for mirrors, and $\operatorname{rk}a=\operatorname{rk}a'=1$ for $4_1$. ∎

### 4.5 The other exact $-1/16$: odd cores of $\pm1$ surgery

$\sigma_{+1}\colon Y_1\to T$ and $\sigma_{-1}\colon T\to Y_{-1}$ have level $-1/16$ from $s=1/2$. Any route from $Y_2$ to $Y_{-2}$ through them uses a handle map in the positive direction:
- $Y_2\to Y_1$ by the downward map, of level $1/4$;
- or $Y_{-1}\to Y_{-2}$, which has $b^+=1$.

Every such route has level $\ge3/16$. PROVED as bookkeeping.

**Conclusion of §4.** Every map of negative topological level that I can build between the two sides is one of the following:
- null-homotopic (the exteriors and $W''$);
- a triangle homotopy ($g_A$, $g_A'$, at $-1/8$);
- a formal secondary composite ($\Phi$, at $-1/16$).

So the drop has to come from the triangle relations themselves. §5 says what they give, and §6 says that it is not enough.

---

## 5. What the triangles give: the drop is pinned by the depth of absorption

**Notation.**
- $\lambda_i=\lambda_i(Y_2)$, $\lambda_i'=\lambda_i(Y_{-2})$, $\mu=\lambda(T)$.
- $m_1=\lambda_0-\lambda_1'$ and $m_2=\lambda_1-\lambda_0'$.
- $\kappa_0=\min\{c(\xi):0\ne\xi\in\ker a_*\subset H(A_0)\}$, and $\kappa_1$ likewise with $a'$.
- $\delta_i=\kappa_i-\lambda_i\ge0$, the **depth of absorption**. It is $0$ exactly when some bottom class of $A_i$ is not absorbed.
- $\eta_g>0$ is the least energy counted by $g_A$; it is positive because no flat connection contributes (§1.4). $\eta_a,\eta_b\ge0$ are the least energies of $a$ and $b$ on the relevant instantons.

**Theorem 5.1 (PROVED, given (I); the same with primes for (II) and $m_2$).**
- (i) $m_1\ge\tfrac18-\delta_0+\min\bigl(\eta_g,\ \eta_a+\eta_b-\beta(T)\bigr)$.
- (ii) Let $\zeta$ be a class realising $\lambda_1'$.
  - If $c_*\zeta\ne0$, then $m_1\le\tfrac3{16}-\delta_0$.
  - If $c_*\zeta=0$, then $\mu\le\lambda_1'+\tfrac1{16}+\beta(A_0)$.

*Proof.*
- (i) Apply Lemma 3.2 to $(a,g_A)$ at a class of $\ker a_*$ with $c=\kappa_0$.
- (ii)
  - $c_*\zeta\in\ker a_*$ by exactness, and it has $c\le\lambda_1'+3/16$. So $\kappa_0\le\lambda_1'+3/16$.
  - Otherwise apply Lemma 3.2 to $(c,g_B)\colon B_1\to\mathrm{Cone}(a)$. ∎

**Corollary 5.2 (kernel criterion, PROVED).** If $\delta_0=0$ and $\beta(T)\le\eta_a+\eta_b$ (for instance if $T$ is perfect), then $m_1>1/8$.

**Corollary 5.3 (counting criterion, PROVED).**
- If $N_{\operatorname{im}a_*}(\lambda_0+r)<N_{A_0}(\lambda_0+r)$, then $\delta_0\le r$, so $m_1\ge\tfrac18-r+\min(\eta_g,\eta_a+\eta_b-\beta(T))$.
- For $r=1/8$ and perfect $T$ this gives $m_1>0$; for $r=1/16$ it gives $m_1>1/16$.
- Here $N_{\operatorname{im}a_*}\le\min(N_T,\operatorname{rk}a_*)$.

**How the $1/16$ enters.** It enters in three places, all of which are the same $\rho(\gamma_1)/16$:
- **The width of the bracket in Theorem 5.1** is $\mathrm{level}(c)+\mathrm{level}(g_A)=\tfrac3{16}-\tfrac18=\tfrac1{16}$. In terms of the ledger this is $\tfrac38-\tfrac{3-1+\rho(\gamma_1)}{16}-\tfrac18$.
- **The absorbed window of Theorem 5.4(b)** has width $\mathrm{level}(g_M)-\mathrm{level}(a)=1/16$.
- **The exact gap at mixed common points** is $1/8+1/16$.

Nothing in the triangle forces $\delta_i$ to be small, so no lower bound $m\ge1/16$, nor $m>0$, follows.

**Theorem 5.4 (necessary conditions for zero both-bundle drop; PROVED for perfect complexes, with $\beta$-corrections in general).**

Suppose $\min(\lambda_0',\lambda_1')\ge M:=\min(\lambda_0,\lambda_1)$. For (b), suppose also $\eta_a>0$; this holds, for example, when no irreducible traceless representation sends $\lambda$ to $\pm1$. Then:
- (a) $\kappa_0,\kappa_1>M+\tfrac18$. Every class of $H(Y_2,P_0)$ and of $H(Y_2,P_1)$ below $M+1/8$ is absorbed.
- (b) $\mu<M\le\max(\lambda_0,\lambda_1)\le\mu+\tfrac1{16}$. This is the window of triangle-1 Prop. 5.6.
- (c) Every class of $H(T)$ with $c<M$ lies in $\ker b_*\cap\ker b'_*=\operatorname{im}a_*\cap\operatorname{im}a'_*$.
- (d) $N_{\operatorname{im}a_*}(r)\ge N_{A_0}(r)$ and $N_{\operatorname{im}a'_*}(r)\ge N_{A_1}(r)$ for $r<M+1/8$.
- In a cosmetic pair the dual statements (for $\ell^+$, and for $\bar K$) hold too.

*Proof.*
- (a) Theorem 5.1(i).
- (c) A class $\tau$ with $b_*\tau\ne0$ gives $\lambda_1'\le c(\tau)-\eta_b$.
- (b) Apply (c) to the bottom of $T$; then the vertex lemma at $T$ gives $\lambda_0,\lambda_1\le\mu+1/16$. Absorption of the bottom gives $\mu\le M-\eta_a$.
- (d) Lemma 3.3. ∎

---

## 6. The formal obstruction

**Theorem 6.1 (PROVED; COMPUTED in `toy.py`).** There are perfect filtered complexes $A_0=B_0$, $A_1=B_1$ and $T$, with maps $a,b,c,a',b',c'$ and homotopies $g$, satisfying all of the following:
- every relation of triangle detection for (I) and (II), with $q=\mathrm{id}$ and $h=0$;
- exactness of both triangles;
- the extra relations of the ledger: $b'a=0=ba'$, which is $\partial g_S$ with $R_0=0$, and $\mathcal E_{\gamma_1}=0$;
- odd degrees for all maps, and a balanced grading (Euler characteristic $0$);
- every level bound of §2, with **strict** negativity of energy where the rules grant it ($a,a',b,b'$, $g_A$, $g_A'$);
- the windows $W$ and $W^+$ of triangle-1 at both ends.

And yet $\lambda_0=\lambda_1=\lambda_0'=\lambda_1'$: all mixed differences and the both-bundle drop are $0$.

*Model 2* (levels in $c$-units):
- $A_0=\langle x_0\ (0),x_1\ (5/32)\rangle$, $A_1=\langle y_0\ (0),y_1\ (5/32)\rangle$, $T=\langle t_1\ (-1/32),t_2\ (3/16)\rangle$.
- (I): $a(x_0)=t_1$, $b(t_2)=y_1$, $c(y_0)=x_1$, $g_A(x_1)=y_0$, $g_M(t_1)=x_0$, $g_B(y_1)=t_2$.
- (II): the same with $x\leftrightarrow y$.

Model 1 is the special case with $c=0$. Tensoring with an $8$-dimensional space concentrated at one level makes all eight gradings equal, as DLME's corollary for a cosmetic pair requires (B-final Cor. 4.4). It also gives every generator its $\iota$-partner.

**Theorem 6.2 (PROVED; COMPUTED: Model 3).** There is a single mixed triangle (I) with the following properties:
- $T=\langle w\ (3/32),t\ (-1/32)\rangle$ with $dw=t$ (energy $1/4$ by Lemma 3.1);
- $A_0=\langle x\ (0)\rangle$, $B_1=\langle z\ (1/16)\rangle$;
- $a(x)=t$, $b(w)=z$, $c(z)=x$, $g_A=0$, $g_M(t)=x$, $g_B(z)=w$;
- every relation and every level bound holds;
- $a_*[x]=0$, so the bottom class is **not** absorbed in homology;
- and $m_1=-1/16$.

The sibling note `r6/critic.md` (Appendix, Examples 1–3, script `r6/critic_toys.py`) reached models of the same two kinds independently: a cosmetic configuration, and a negative drop carried by a finite bar of an acyclic middle term.

**Consequences.**
1. No argument that uses only the following can prove $m_1>0$, $m_2>0$, or a positive both-bundle drop:
   - the triangles (I) and (II);
   - the ledger;
   - positivity of energy;
   - the null-homotopies of §4;
   - the composites of §4.4.

   Such an argument would apply verbatim to Models 1–2. This holds whether or not the differentials vanish.
2. The kernel criterion itself needs $\beta(T)<\tfrac18+\eta_a+\eta_b$ once $T$ has a differential.
   - By Lemma 3.1 this is the statement that the traceless differential has no trajectory of energy $\ge\tfrac18+\eta_a+\eta_b$ ending on the image of the bottom class.
   - It is an upper bound on energy, so it is excluded by rule (a). It is not equivalent to the drop, but it is an energy estimate.
   - For the Seifert examples $T$ is perfect, so this is invisible in the data.

---

## 7. Tests on the data (COMPUTED; `datatest.py`, `bottoms.py`, `samerep.py`, `rankcheck.py`)

All complexes here are perfect (Seifert examples), so $\beta=0$ and the boundary-depth terms vanish.

Conventions:
- Counts are $SU(2)$ counts, as in triangle-1.
- "Instance" means one knot, one chirality and one of the triangles (I), (II).
- The traceless levels are Seifert-framed, computed through the flat singular connections (triangle-1 §3.3).

### 7.1 Exact gaps at common representations

For every torus knot with $pq\le40$ in both chiralities (`datatest40b.out`; for the bottoms with $pq\le120$ see §7.6), every representation of the knot group that defines generators on both sides gives:

| pair of bundles | $c(Y_2,x)-c(Y_{-2},x)$ |
|---|---|
| $(P_0,P_0)$ | $1/8$ |
| $(P_1,P_1)$ | $1/8$ |
| $(P_0,P_1)$ | $3/16$ |
| $(P_1,P_0)$ | $3/16$ |

No other value occurs. These are the levels of the flat connections on $\mp E$ (§2). The index ($-1$ on $E$, $0$ on $-E$) is inferred from the gaps, and is a transversality statement (ell-1, E).

### 7.2 Where the bottoms sit (`bottoms.out`: all 210 torus knots with $pq\le120$, both chiralities)

| class of knots | number | both-bundle drop | bottoms at common representations |
|---|---|---|---|
| positive torus knots | 105 | $>1/8$; minimum $0.131$ | in 1 case, $T(2,3)$: both bottoms at mixed common points, drop $3/16$ |
| mirrors with $\det>1$ | 78 | **exactly $1/8$ in all 78** | in all 78 |
| mirrors with $\det=1$ | 27 | $\tfrac18-\tfrac1{4(n^2-4)}$, $n=pq$; minimum $219/1768=\tfrac18-\tfrac1{884}$ at $\bar T(3,5)$ | in none; realised by $P_0$ on both sides |

So exact topological levels decide the both-bundle drop exactly when the bottoms are common representations:
- the $1/8$ is the level of the flat connection on $E$ with limit $\gamma_0$;
- for $\det>1$ the bottoms are the binary dihedral or $\lambda\mapsto-1$ traceless representations.

For $\det K=1$, the case of every cosmetic candidate, this never happens in the data.

### 7.3 Depth of absorption and the bracket of Theorem 5.1 (`datatest40b.out`, $pq\le40$, 88 instances)

**Positive knots.** $a=a'=0$ by parity, so $\delta=0$ and $m\in(1/8,3/16]$. The bracket holds in all 44 instances.

**Mirrors.** $b=b'=0$ by parity and $a,a'$ are surjective. Absorption of the bottom class is forced, in every level-compatible configuration, in 27 of 44 instances:

| triangle | absorption forced | bottom not absorbed |
|---|---|---|
| (II) | 19 | 3 |
| (I) | 8 | 14 |

**The bracket.** $\tfrac18-\delta\le m\le\tfrac3{16}-\delta$ holds for some feasible $\delta$ in every instance (0 failures).

**$\det=1$ mirrors.** Absorption is forced in **both** triangles. The depth of absorption is tiny:

| knot | $\delta$ in (I) | $\delta$ in (II) | $m_1$, $m_2$ |
|---|---|---|---|
| $\bar T(3,5)$ | $[1/20,27/340]$ | $1/34$ | $m_1=151/1768$, $m_2=219/1768$ |
| $\bar T(3,7)$ | $1/46$ | $1/46$ | both $435/3496$ |
| $\bar T(5,7)$ | $1/74$ | $1/74$ | both $1219/9768$ |
| $\bar T(3,11)$ | $1/70$ | $1/70$ | both $1083/8680$ |
| $\bar T(3,13)$ | $1/82$ | $1/82$ | both $1515/12136$ |

Except for $\bar T(3,5)$ in (I), the pattern is $\delta=1/(2(pq+2))$. The drop is $\tfrac18-\delta+\eta_g$, which is close to $1/8$ except for $\bar T(3,5)$ in (I). It is carried by the class just above the absorbed bottom.

The bottoms of $P_0$ and $P_1$ on $Y_2$ coincide level for level (`datatest40b.out` §5). So these knots satisfy the bottom-of-spectrum necessary conditions (b)–(c) of Theorem 5.4: they are "half cosmetic" in triangle-1's sense. Only (a) fails, because $\delta<1/8$.

### 7.4 The two sharp examples

**$\bar T(2,3)$, triangle (II).** $H^w(Y_2)=\{-1/24,\,1/12,\,1/12\}$, $H(Y_{-2})=\{-5/48,-5/48\}$, $T=\{-1/24\}$.
- The bottom $-1/24$ is binary dihedral and is absorbed at energy $0$, by a flat singular connection.
- The kernel classes $1/12$ sit at mixed common representations, so $\delta=1/8$ exactly.
- Theorem 5.1 gives $\eta_g\le m_2\le 3/16-1/8=1/16$.
- At the mixed common points:
  - $c'$ is computed by a flat connection on $-E$ of level exactly $3/16$;
  - $g_A'$ is computed by the flat exterior of index $-1$ glued to the minimal cap, at level exactly $-1/8-1/16$, so $\eta_g=1/16$.
- **Both ends of the bracket equal $1/16$**:
  $$m_2=\tfrac3{16}-\delta=\tfrac1{16}.$$
  The term $3/16=\tfrac18+\rho(\gamma_1)/16$ is topological. The depth $\delta=1/8$ is the gap, on $Y_2^w$, between the binary dihedral generator and the mixed generators, and that is a property of this knot.
- COMPUTED; the identification of the counted instantons is PLAUSIBLE.

**$4_1$, triangle (II).** $H^w(Y_2)=\{1/5,3/10\}$, $H(Y_{-2})=\{11/80,11/80\}$.
- Ranks force $\operatorname{rk}a'_*=1$, and triangle-1 places the kernel at $3/10$, so $\delta=1/10$.
- The bracket is $[1/40+\eta_g,\ 7/80]$, and $m_2=5/80$ lies in it, with $\eta_g=13/80-1/8=3/80$.
- Nothing topological makes $m_2$ equal to $1/16$ here; triangle-1 calls it a coincidence, and I agree.

### 7.5 The counting criterion (Corollary 5.3)

- **$pq\le40$.** With $N_T$ in place of $N_{\operatorname{im}a_*}$, the criterion at $d=1/8$ holds in 86 of 88 instances, including **every** mirror instance. The two failures are positive knots, where $a=0$ anyway.
- **$d=1/16$.** It holds in 81 of 88.
- **$4_1$.** The $N_T$-form fails at $d=1/8$, with $N_T=N_A=2$ for either assignment of the traceless levels. The form with $\operatorname{rk}a'_*=1$ holds.

So on the data the counting criterion would prove $m>0$ wherever the triangles alone do not. But Theorem 5.4(d) shows that in a cosmetic pair it must fail for both bundles. Proving it for all knots therefore amounts to proving the theorem.

### 7.6 The full range $pq\le120$

Over all 210 torus knots with $pq\le120$, both chiralities:
- `samerep120.out`: the both-bundle drop equals $1/8$ or $3/16$ in 79 cases (the 78 mirrors with $\det>1$, and $T(2,3)$). In **all 79** the two bottoms are the **same representation** of the knot group. So the exact drop is the level of one flat connection on $E$:
  - $\gamma_0$-end, index $-1$, level $-1/8$, for the 78 mirrors;
  - $\gamma_1$-end, index $-1$, level $-3/16$, for $T(2,3)$.
- `rankcheck120.out`: $\operatorname{rk}B_1-\operatorname{rk}A_0=\operatorname{rk}B_0-\operatorname{rk}A_1$ holds in all 210 cases (Proposition 4.3).
- `bottoms.out`: as in §7.2.
- The bracket and counting tests (§7.3, §7.5) were run in full for $pq\le40$ (88 instances). Extending them to $pq\le120$ is a matter of running `datatest.py 120`. That run is slow, because of the matching search over large spectra, and was stopped.

---

## 8. Step by step: what holds, what fails, what needs energy

| step | content | status | on the data | hidden energy? |
|---|---|---|---|---|
| 1 | Ledger of levels (§2) | PROVED as bookkeeping; lens $\rho$ COMPUTED | exact gaps $1/8$, $3/16$ at all common points | no |
| 2 | Find a chain map $Y_2\to Y_{-2}$ of level $\le-1/16$ | exists: $\mathcal E_{\gamma_1}$ (and $\Phi$ through $T$) | – | no |
| 3 | Injectivity of that map | **fails**: $\mathcal E_{\gamma_1}\simeq0$ (PLAUSIBLE, gluing); $\Phi$ formal, $=0$ in Models 1–2 | – | no |
| 4 | Fall back to the families at $-1/8$ (triangle detection) | PROVED given triangles | $m\ge1/8$ in every non-absorbed instance | needs $\beta(T)<\frac18+\eta_a+\eta_b$ when $T$ has a differential (Theorem 6.2) — an **energy upper bound** |
| 5 | Control absorption structurally | **fails**: Models 1–2 | absorption is forced in 27 of the 88 instances with $pq\le40$, all of them mirrors, including both triangles of every det-1 mirror | a lemma excluding it would be **false**; a lemma bounding $\delta<1/8$ is **equivalent to** $m>0$ up to $1/16$ |
| 6 | Counting criterion | PROVED as implication | holds in every mirror instance with $pq\le40$; fails for $4_1$ in the form with $N_T$, holds there with $\operatorname{rk}a'_*=1$ | none; but it must fail in a cosmetic pair (Theorem 5.4(d)), so proving it is at least as hard as the theorem; its spectral form fails for $4_1$ |
| 7 | Both-bundle version | same as 4–6 | drop $\ge1/8-1/884$; exactly $1/8$ whenever both bottoms are at same-bundle common points (all 78 mirrors with $\det>1$) | same |

---

## 9. What a proof along these lines would still need

A proof must use information that Models 1–3 violate. Here is what that information could be, and why the angle does not supply it.

1. **A non-formal computation of a map on the bottom classes.**
   - At common representations the maps are computed by flat connections, exactly and topologically (§4.3).
   - A proof could therefore succeed for knots whose bottom generators sit at common points. In the data this happens:
     - for every mirror torus knot with $\det>1$, whose two bottoms sit at same-bundle common points, and for $4_1$; in all of these the both-bundle drop is exactly $1/8$;
     - for $\bar T(2,3)$, where $m_2=1/16$ exactly.
   - For $\det K=1$ (every cosmetic candidate) there are no binary dihedral representations. The bottoms of the det-1 torus knots are not at common points (§7.2).
   - So this route does not reach the cosmetic case.
2. **A structural bound on the depth of absorption, $\delta_i<1/8$.**
   - By Theorem 5.1 this is equivalent to $m>0$ up to an error of $1/16$. So it is a reformulation, not an input.
   - The counting criterion is the closest non-energy sufficient condition. Theorem 5.4(d) shows that it, too, must fail in a cosmetic pair, so it cannot be proved for all knots without proving the theorem.
   - Its plainest form is a statement about spectra alone, with no maps:
     $$\#\{\text{classes of }H(T)\text{ with }c\le\lambda_i+\tfrac18\}<\#\{\text{classes of }H(Y_2,P_i)\text{ with }c\le\lambda_i+\tfrac18\}.$$
     It would be a genuinely different kind of input: a density comparison of Chern–Simons spectra, perhaps accessible through the pillowcase, where $T$ counts $C^*\cap V$ and $Y_2$ counts $C^*\cap L_2$.
   - On the data it holds in every mirror torus-knot instance, with a wide margin for $\det K=1$ (for example $6$ against $20$ for $\bar T(5,7)$). It fails, with equality $2=2$, for $4_1$.
   - So it could at best hold under $\det K=1$. Even then it gives $m>0$ only together with the control of $\beta_T$ in item 3. I know no mechanism for it. (SPECULATIVE.)
3. **Control of $\beta(T)$.** This is an energy statement about the traceless differential (Lemma 3.1), so the rules exclude it.
4. **Extra structure not encoded in the triangles.** Candidates:
   - the module structure over $\mu(\mathrm{pt})$;
   - the $\chi$-twist on $T$;
   - equivariance on the branched cover.

   Each can be imposed on Models 1–2 (double every generator, let $\mu(\mathrm{pt})$ act by zero over $\mathbb F_2$). So none of them, used formally, breaks the obstruction. (SPECULATIVE that a finer use could.)
5. **The diffeomorphism itself.** In a cosmetic pair every map becomes an endomorphism, and one could compose, e.g. $g_A\circ\phi\circ g_A$, and neck-stretch along hypersurfaces of $W'\cup_\phi W'$ that the triangle does not see.
   - This is genuinely non-formal.
   - It depends on the unknown $\phi$.
   - I see no way to extract a level from it. (SPECULATIVE.)

**Bottom line.** The exact topological levels are fully accounted for by the ledger, and the triangle relations organise them into the bracket of Theorem 5.1. The drop is then decided by the depth of absorption and by the boundary depth of $T$. Neither is topological, and the first is not even bounded in the data by anything better than $1/8$ (attained by $\bar T(2,3)$). The angle gives a sharp *description* of the $1/16$, but **not a proof** of $m>0$.

---

## 10. Claims and labels

| claim | label |
|---|---|
| Ledger (§2), and the values $\rho=0,1,2,1$ on $\partial\nu S$ | PROVED as bookkeeping / COMPUTED |
| Exact common-point gaps $1/8$ (same bundle), $3/16$ (mixed) | COMPUTED (torus knots, $pq\le40$, both chiralities, all common points; $pq\le120$ for the bottoms); PROVED as bookkeeping given index $-1$ / $0$ of the flat exteriors |
| Prop. 4.1: $\mathcal E_{\gamma_1}$ has level $-1/16$ and is null-homotopic; so is its $\chi$-twist | dimension count PROVED; null-homotopy PLAUSIBLE (gluing at $\gamma_1$); $\chi$-twist PROVED given it |
| The rational blow-down carries no mixed bundle; $W''_*\simeq0$ | PROVED / PLAUSIBLE |
| Prop. 4.2: $\Phi\colon T\to B_1$ is a chain map of level $\le-1/16$, and it vanishes in the strict cone model | PROVED |
| Prop. 4.3: $\ker b_*=\ker b'_*$, $\operatorname{im}a_*=\operatorname{im}a'_*$ | PLAUSIBLE |
| Lemmas 3.1–3.4 | PROVED |
| Theorem 5.1 and Corollaries 5.2–5.3 | PROVED given the triangles |
| Theorem 5.4 | PROVED for perfect complexes given the triangles |
| Theorems 6.1–6.2 (formal obstruction, boundary-depth obstruction) | PROVED; COMPUTED |
| "This angle alone cannot prove a drop" | PROVED in the sense of Theorems 6.1–6.2: it holds for every argument built from the listed ingredients |
| Some non-formal input (§9.1, 9.4, 9.5) could break the obstruction | SPECULATIVE |
