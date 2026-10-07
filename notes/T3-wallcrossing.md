# T3. The positive piece as a $b^+=1$ Seiberg–Witten problem

Inputs: `06-geometry.tex`, `07-estimates.tex`, Lemma `indices:positive-square` (Sec. 8), Prop. `stack:lattice` (Sec. 5), notes C §3 and D §2.
Labels: **[V]** I checked the computation or the argument (scripts in `agents/T3-checks/`). **[P]** plausible. **[S]** speculative.
**†** marks a citation from memory whose exact form I could not check. Notation: the manuscript's $C_2$ is the $(-4,0,-4)$ plumbing. I write $B_2$ for the Fintushel–Stern rational ball with $\partial B_2=L(4,1)$.

## 0. Summary and verdict

1. **[V]** What Sections 6–7 must supply downstream is the following property. Every reduced field (type R or S) on the component containing a positive bridge has either $u=v\cdot U=0$, or a nonempty $I$ with positive-cell square $Q_I\le-2$, or one exceptional class that forces Feehan–Leness level $\ell\ge1$. The clamp itself is only an intermediate step.
2. **[V]** The period inequality $(vH)(KH)<0$ is the classical $b^+=1$ Weitzenböck band. Type S is the SW equation for $K=\Lambda+v$ with perturbation $\eta=\beta^+$. Type R is the common reducible wall $vH=0$ (SW wall for $(K,\eta)$ and Donaldson wall for $v$). The band says exactly that the segment $t\eta$, $t\in[0,1]$, crosses the $K$-wall.
3. **[V/P]** The band is optimal. On $P=\mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2$ we have $2\chi+3\sigma=4>0$, so there are no walls at zero perturbation. Wall-crossing then gives $SW(K;g,2\pi\Lambda^+)=\pm1$ precisely on the band when $d(K)\ge0$. No choice of metric can remove band classes. They are excluded by energy (Sec. 8), not by geometry.
4. **[V]** Scal $\ge0$ is genuinely needed in the gluing-free architecture, and so is strict positivity at one point. Only the limiting isolated pieces need it; at finite stages, $\int\mathrm{Scal}_-^2\to0$ is enough. Chamber position plus a priori bounds would suffice only together with Feehan–Leness gluing at reducibles, which is not available in families.
5. **[V]** A short proof of the clamp from classical inputs:
   - the Weitzenböck band;
   - a sharpened convexity lemma: for $u<0$ it gives $Q\le-6$, so the exception occurs only for $u=+1$;
   - the lattice lemma (brute-force checked);
   - a Kronheimer–Mrowka / Friedman–Morgan neck-stretching argument along the $S^2\times S^1$ tube, which uses the energy window instead of a fixed spin$^c$ structure.

   Lattice-wise, the clamp holds on all of $\Pi\setminus\{U\}$. The tube is needed only because the family must reach the cusp $U$ of the period disc.
6. **[V]** The vertex classes are forced, not chosen. For $I\ne\varnothing$, $H_I$ spans the positive cone of the corner piece in which the necks $\partial N_i$ ($i\in I$) and $\partial C_{1,i}$ ($i\notin I$) are infinitely long. For $I=\varnothing$ the corner piece is $\nu U$, which has no positive class: this is the cusp. Equivalently, $H_I$ is the orthogonal projection of $U$ to $X_I^\perp$.
   - In toric terms the three face types are the three edge collapses of the moment polygon. The $X_i$-edge collapses to the Wahl point $\tfrac14(1,1)$ (an $L(4,1)$ neck: the lens face $a=\tfrac14$). The sloping edge collapse gives an $S^3$ neck (the $J$ side, $a=0$). The $U$-edge collapse gives the cusp ($S^2\times S^1$ tube).
   - At a one-sided corner the main piece is $\mathbb P(1,1,4)$ punctured at a smooth point. Its $\mathbb Q$-Gorenstein smoothing (the rational blowdown of $X_i\subset F_4$) is $\mathbb{CP}^2$, with $H_i=h/2$ and $\Lambda=K_{\mathbb{CP}^2}$ or $-h$.
   - The only descending band class there is $K=-h$, and it is exactly the exceptional case of the lattice lemma.
7. **Verdict.**
   - Section 7 is essentially classical and can be cut to about 4–5 pages **[P, 80%]**.
   - Section 6 cannot be replaced by a citation **[P, 90%]**. It can be shortened to about 5–6 pages using the toric dictionary of §3 **[P, 60%]**: the Guillemin metrics have Scal $\ge0$ in every Kähler class, as a general lemma (**[V]** numerically), and edge collapse is neck stretching.
   - What remains genuinely needed:
     - (i) the two-parameter family with moving interfaces and the corner replacement at the cusp;
     - (ii) compactness, uniform over the cube and its genuine faces and in the order of choices;
     - (iii) the bound on the charge of a reduced component inside a $\mathrm{PU}(2)$ limit. This one is $\mathrm{PU}(2)$-specific, not SW.

## 1. What is needed

### 1.1 Local data [V]

- **The macro.** At bridge $j$, put $X_1=-S_j$, $X_2=S_{j+1}$ and $C_2=\nu(X_1\cup U\cup X_2)$.
  - The form $\begin{psmallmatrix}-4&1&0\\1&0&1\\0&1&-4\end{psmallmatrix}\cong H\oplus\langle-8\rangle$, with basis $U$, $X_1+2U$, $X_2-X_1-4U$.
  - $\partial C_2=L(8,1)$, since $[4,0,4]=8$.
- **The pieces.**
  - $C_{1,1}=\nu(U\cup X_2)$ and $C_{1,2}=\nu(U\cup X_1)$ have form $\begin{psmallmatrix}0&1\\1&-4\end{psmallmatrix}$, which is even unimodular. So $C_{1,i}\cong F_4\setminus B^4\cong S^2\times S^2\setminus B^4$, with $\partial C_{1,i}=S^3$.
  - $N_i=\nu X_i=D(-4)$, with $\partial N_i=L(4,1)$.
  - The $X_i$ do not lie in the cell $P$: they cross $J_j$ and $J_{j+1}$.
- **The periods.** $H(a,b)=U+aX_1+bX_2$ with $(a,b)\in[0,\tfrac14]^2$. Put $p=4a$, $q=4b$. Then
$$H=\textstyle\sum_I\theta_IH_I,\qquad \theta=\big((1-p)(1-q),\,p(1-q),\,(1-p)q,\,pq\big),\qquad H_I=U+\tfrac14\textstyle\sum_{i\in I}X_i,\qquad H_I^2=|I|/4 .$$
  Write $\Pi=\mathrm{conv}\{H_I\}$.
- **The background.** On $C_2$, the pairings $(\Lambda X_1,\Lambda U,\Lambda X_2)=(-2+4e_j,\,-1-e_j+e_{j+1},\,2-4e_{j+1})$ give
$$\Lambda=K_t+(1-e_j)\,\mathrm{PD}(X_1)+e_{j+1}\,\mathrm{PD}(X_2).$$
  - Here $K_t=(2,-2,2)$ is the canonical class of the toric structure (adjunction for the three spheres).
  - The vertex values are $\lambda_\varnothing=\lambda=-1-e_j+e_{j+1}$, $\lambda_1=-\tfrac32+e_{j+1}$, $\lambda_2=-\tfrac12-e_j$ and $\lambda_{12}=-1$.
  - Hence $\Lambda H<0$ on $\Pi\setminus\{U\}$, and $\lambda\le0$.
- **The class $v$.**
  - $u=vU\equiv\lambda\pmod 2$, $d_i=vX_i\in2\mathbb Z$, and $z_I=vH_I=u+\tfrac14\sum_{i\in I}d_i\in\tfrac12\mathbb Z$.
  - On $P$: $x=vG$ is even, and exactly two of the $t_b=vT_b$ are odd.
  - $h_1,h_2\in2\mathbb Z$ are the adjacent half evaluations.
  - $Q_I:=2xu-2u^2-\sum t_b^2-\tfrac12\sum_{i\in I}h_i^2$.
  - $K=\Lambda+v$ is characteristic.

### 1.2 The statement used downstream

$(\star)$ For every reduced field on the component containing the bridge, one of three cases holds:
- $u=0$, and then $Q_\varnothing\le-2$ by parity alone;
- there is a nonempty set $I$ of whole sides with $Q_I\le-2$;
- the exceptional case: $|I|=1$, $u=z_I=1$, $d_i=0$, $Q_I\le2$. Here the reduced field does not see the $X_i$ test, which forces $\ell\ge1$ on the component. (The manuscript also allows $u=z_I=-1$; Lemma B below removes that case.)

$(\star)$ is all that Section 8 uses: each positive cell then contributes at least $\tfrac12$ to $-v^2/4$. The clamp inequality \eqref{eq:estimates:clamp} is the intermediate step $(\text{period})\Rightarrow(\text{vertex inequality})\Rightarrow(\star)$.

### 1.3 Dictionary with $b^+=1$ Seiberg–Witten theory [V]

**The equations.** The reduced equations are $\rho(iD^+)=(\psi\psi^*)_0$ and $D_{B}\psi=0$, where $F_B=i(\beta+D)$, $c_1=K=\Lambda+v$, $[\beta/2\pi]=\Lambda$ and $\beta$ is harmonic. These are the SW equations for $K$ with perturbation $\eta=\beta^+$. On an isolated piece with $b^+_{L^2}=1$ and period $H$,
$$\eta=2\pi\,\frac{\Lambda H}{H^2}\,h_H .$$

**Walls and chambers.**
- The reducibles of $(K,\eta)$ are the solutions with $D^+=0$, i.e. $vH=0$. This is also the Donaldson wall for the $U(1)\times U(1)$ reduction with line difference $v$, so type R is the common wall.
- The chamber of $(g,\eta)$ for $K$ is $\operatorname{sign}((2\pi K-\eta)\cdot H)=\operatorname{sign}(vH)$.
- The chamber of $(g,0)$ is $\operatorname{sign}(KH)$.
- So the band $(vH)(KH)<0$ says exactly that the two chambers differ, i.e. the path $t\eta$ crosses the $K$-wall.

**Wall-crossing.** For $b_1=0$ and $b^+=1$, the invariant jumps by $\pm1$ across the wall when $d(K)=\tfrac14(K^2-2\chi-3\sigma)\ge0$ (Kronheimer–Mrowka 1994 for $\mathbb{CP}^2$; Li–Liu 1995; Okonek–Teleman†).

**The closed $P$.**
- Here $2\chi+3\sigma=4$, so $d(K)\ge0$ forces $K^2\ge4>0$. Then $K^\perp$ misses the positive cone, and $\operatorname{sign}(KH)$ is constant on it.
- Hence $SW(K;g,0)$ does not depend on $g$. It vanishes because $P$ carries psc metrics (Witten). The same holds for $\mathbb{CP}^2\#k\overline{\mathbb{CP}}{}^2$ with $k\le9$. For $k\ge10$ one needs Friedman–Morgan's psc-chamber statement†.
- **Consequence.** $SW(K;g,2\pi\Lambda^+)=\pm1$ if and only if $(vH)(KH)<0$ and $d(K)\ge0$.

**Status.** [V] for closed $P$ (arithmetic plus cited theorems). [P] for the isolated pieces with psc rational-homology-sphere ends, where $d$ acquires APS corrections and $k$-parameter families admit $d+k\ge0$.

**Consequence for the manuscript.** The band is the exact obstruction, so no metric construction can shrink it. The exclusion of band classes must come from energy. This is the logic of the manuscript: the clamp localizes, and Section 8 excludes. It is consistent with D §2.2.

### 1.4 Is Scal $\ge0$ needed? [V as logic and arithmetic]

**(i) Emptiness, not counts.** The $\mathrm{PU}(2)$ argument is gluing-free, so it needs reduced strata in the energy window to be empty. Chamber data determine only counts. Emptiness off the band is a pointwise statement and needs the Weitzenböck identity. With Feehan–Leness gluing at reducibles (unavailable in families with neck faces), chamber position would suffice. But the lattice consequence of the band, $(\star)$, would still be needed, because band classes with $d\ge0$ contribute nonzero terms.

**(ii) Strict positivity somewhere is used.**
- If $\mathrm{Scal}\equiv0$ is allowed, a parallel twisted spinor can exist: for a Kähler metric, the canonical spin$^c$ structure has one. The band then closes to $(vH)(KH)\le0$.
- The closed vertex inequality $\operatorname{sign}(u)z_I\le|\lambda_I|$ admits $|I|=1$, $z_I=\tfrac32$, $u=1$. This gives
$$Q\le 8\cdot\tfrac32-4-2=6,$$
  and $(\star)$ fails.

**(iii) Fixed a priori bounds are insufficient.**
- A bound $|vH|<|\Lambda H|+\delta$ with fixed $\delta>0$ has the same effect: $z_I\in\tfrac12\mathbb Z$, so any $\delta>0$ admits $z_I=|\lambda_I|$.
- The energy count has little slack:
  - The closed stratum tolerates $Q\le0$ per positive cell at spacing 4. Per period, $8\kappa$ grows by $n+3m=7$, while two negative-rule sphere tests cost $8$. So one needs $8-2Q>7$.
  - The mixed R-runs at spacing 4 have no slack (D §0.4).

  So the sharp form is required.

**(iv) What suffices.**
- Scal $\ge0$ and Scal $\not\equiv0$ on the limiting isolated main pieces.
- At finite stages, $\int\mathrm{Scal}_-^2\to0$ on those pieces, plus compactness for the finitely many classes allowed by the charge bound. This is what Lemma `estimates:vertices` does.
- No positivity is needed on the $Y_j$ middles: there the energy is controlled by the Chern–Simons(–Dirac) values at the ends (Lemma `estimates:cylinder`; for SW fields this is the classical CSD energy identity†).

## 2. A classical proof of the clamp

**Theorem A (Weitzenböck band; Witten, LeBrun, Kronheimer–Mrowka†) [V].**
- **Hypotheses.**
  - $(M,g)$ is complete, with cylindrical ends on rational homology spheres with psc.
  - $\mathrm{Scal}\ge0$, and $\mathrm{Scal}>0$ at some point.
  - $b^+_{L^2}=1$, with period ray $H$.
  - $\beta$ is $L^2$-harmonic with $[\beta/2\pi]=\Lambda$.
- **Conclusion.** A finite-energy solution for $K=\Lambda+v$ with perturbation $i\beta^+$ has $vH=0$ if $\psi\equiv0$, and $(vH)(KH)<0$ otherwise.
- **Proof.**
  - Integrate $D_B^*D_B\psi=0$ against $\psi$. The exponential decay on psc rational ends justifies the integration [P, standard]. This gives
  $$0=\int\left(|\nabla\psi|^2+\tfrac{\mathrm{Scal}}4|\psi|^2\right)+2\int\langle\beta^++D^+,D^+\rangle .$$
  - Project $D^+$ onto $\mathbb Rh_H$. The second term becomes $(2\pi)^2(vH)(KH)/H^2+\|D_\perp\|^2$.
  - The first term is $>0$ unless $\psi$ is parallel and vanishes where $\mathrm{Scal}>0$, i.e. $\psi\equiv0$. ∎

This is Lemma `estimates:projection` verbatim; it is correct.

**Lemma B (convexity, sharpened) [V].** Let $H\in\Pi\setminus\{U\}$ with weights $\theta_I$, and $u\ne0$.
- (S, $u>0$) Some $I\ne\varnothing$ with $\theta_I>0$ has $K\cdot H_I<0$, i.e. $z_I<|\lambda_I|$.
- (S, $u<0$) Some $I\ne\varnothing$ with $\theta_I>0$ has $v\cdot H_I>0$.
- (R) Some $I\ne\varnothing$ with $\theta_I>0$ has $\operatorname{sign}(u)z_I\le0$.

*Proof.*
- Since $\Lambda H<0$, the band is $0<vH<-\Lambda H$. This is the intersection of two half-spaces, $\{vH>0\}$ and $\{KH<0\}$, and both functionals are linear in $H$.
- At the empty vertex, $K\cdot U=\lambda+u\ge0$ when $u>0$, by parity: $u\equiv\lambda$ and $\lambda\in\{0,-1,-2\}$. Also $v\cdot U=u<0$ when $u<0$.
- So in each case the inequality must hold at a nonempty supported vertex.
- (R) $\theta_\varnothing u+\sum_{I\ne\varnothing}\theta_Iz_I=0$ forces some nonempty supported $I$ with $\operatorname{sign}(u)z_I\le0$. ∎

The manuscript's version uses the weaker condition $\operatorname{sign}(u)z_I<|\lambda_I|$ for $u<0$.

**Lemma C (lattice) [V].** Let $u\ne0$, and let $I$ be as in Lemma B. Then:
- $Q_I\le-2$, except when $u=z_I=1$, $|I|=1$ and $d_i=0$, in which case $Q_I\le2$;
- in case (S, $u<0$), in fact $Q_I\le-6$.

The exception occurs only for $(e_j,e_{j+1})=(0,0)$ with $I=\{1\}$, and for $(1,1)$ with $I=\{2\}$.

*Proof.*
- The maximum over $(x,t,h)$ is $Q_I^{\max}=8z_Iu-4u^2-2$ for $|I|=1$ and $4z_{12}u-2u^2-2$ for $I=\{1,2\}$. Both are attained. The $-2$ is the parity minimum of $\sum(t_b-u)^2$ or $\sum(t_b-u/2)^2+\tfrac12\sum(h_i-u)^2$.
- The cases then follow by case analysis.
- `clamp.py` checks the three closed forms of Lemma `indices:positive-square` on random data, and checks that the parity maximum is exactly $-2$.
- `clamp_fast.py` and `clamp_sharp.py` check, for all bits, $|u|\le9$, $|d_i|\le60$ and a $24\times24$ grid on $\Pi\setminus\{U\}$ (down to $a+b=1/96$):
  - band ⇒ Lemma B ⇒ Lemma C, with 0 failures;
  - the worst bound is $2$ for $u>0$ (the exception only) and $-6$ for $u<0$. ∎

**Proposition D (the cusp; Kronheimer–Mrowka / Friedman–Morgan neck stretching) [V as argument, P for constants].**
- **Hypotheses.**
  - The component contains a product tube $S^2(1/\sqrt2)\times S^1\times[0,L]$ with fibre $U$, $\mathrm{Scal}=4$, and background flux $|\lambda_U|\le2$. Hence $V=\mathrm{Scal}/4+\tfrac12\rho(\beta)\ge0$ on the tube.
  - $C_0$ bounds $\int V_-^2$ off the tube and the $Y_j$ middles, plus the Chern–Simons–Dirac endpoint terms. $C_0$ is independent of $L$.
- **Conclusion.** A reduced field of charge $\kappa_i$ with $\ell_i\ge0$ satisfies $4\pi^2u^2L\le C_1(C_0)+16\pi^2\kappa_i$. So $u=0$ once $L$ is large relative to the charge bound.
- **Proof.**
  - Fibrewise Cauchy–Schwarz with $\int_{S^2}D=2\pi u$ gives $\int_{\rm tube}|D|^2\ge4\pi^2u^2L$.
  - Globally, $\int|D|^2=2\|D^+\|^2-4\pi^2v^2$.
  - The window gives $-v^2\le4\kappa_i$.
  - The cutoff Weitzenböck estimate (Lemma `estimates:local` with $\zeta\equiv1$) gives $\|D^+\|^2=\tfrac18\|\psi\|_4^4\le C\int V_-^2$. ∎

This replaces Prop. `estimates:energy` and Cor. `estimates:tube` for the clamp. The only non-SW input is the upper bound on $\kappa_i$ for a component of a $\mathrm{PU}(2)$ limit, which is the role of Lemma `estimates:cylinder` and (7.29).

**Why the tube is local to the cusp [V].**
- A $U$-tube of length $L$ forces $H^2\ge cL(H\cdot U)^2$, by fibrewise Cauchy–Schwarz for the harmonic form.
- On the lens faces, $(H\cdot U)^2/H^2\ge\tfrac14$ (`toric.py`). So the tube cannot be used globally.
- Conversely, Lemmas B–C hold lattice-wise on all of $\Pi\setminus\{U\}$. The tube is needed only because:
  - no metric has period $U$ (since $U^2=0$), yet the family must reach the corner $(J_1,J_2)$, where the main piece degenerates to $\nu U\cong S^2\times D^2$ with $b^+=0$;
  - the walls accumulate at the cusp. On $b=0$, the number of band values $(u,d_1)$ with $|u|\le3$ is exactly $2/a$ (`cusp.py`). So compactness is not uniform there.

**Which classes appear [V].**

At the vertices the band classes are:

| vertex | band condition | bits with band classes | possible values |
|---|---|---|---|
| $H_1$ | $0<z_1<\tfrac32-e_{j+1}$ | $e_{j+1}=0$ only | $z_1\in\{\tfrac12,1\}$ |
| $H_2$ | $0<z_2<\tfrac12+e_j$ | $e_j=1$ only | $z_2\in\{\tfrac12,1\}$ |
| $H_{12}$ | $0<z_{12}<1$ | all | $z_{12}=\tfrac12$ |

- All of them have $Q\le-2$, except $u=z_i=1$, which is the class $-h$ of §3.3.
- $Q=-2$ is attained, e.g. at $H_{12}$ with $u=1$, $z_{12}=\tfrac12$. So Lemma C is sharp, and these classes lie inside the band.
- In the interior of $\Pi$ there are many more band classes (their number grows like $1/(a+b)$ near the cusp; see Prop. D), all with $Q\le-2$ or the exception.

The energy comparison is from round 2 [P]. Each sphere test costs $\ge\tfrac12$ in $-v^2/4$. Each positive cell costs $\ge\tfrac12$, or forces $\ell\ge1$. Hence
$$-v^2/4\ \ge\ \tfrac{n-m}2-C\quad\text{against}\quad\kappa=\tfrac{n+3m}8+C',$$
so no class fits once $3n>7m$. The SW classes exist on the piece, but they need more energy than the window provides.

**Assessment of the suggested inputs.**
- **(a) Prescribed periods.** This gives the band pointwise in $H\in\Pi^\circ$.
  - For each $(a,b)$ in the open square, the Guillemin metric of the labelled polygon $\mathcal P(a,b)$, plus $\tfrac14\xi^2$, is a toric Kähler orbifold metric of class $H$ with $\mathrm{Scal}\ge0$ and $\mathrm{Scal}>0$ on the interior.
  - The manuscript's Lemma `geometry:scalar` is in fact a general fact: for any positive affine $l_\nu$ with spanning gradients, arbitrary integral normals, and constant $C\ge0$, one has $\mathrm{Scal}\ge0$ [V numerically, `abreu.py`, `abreu2.py`].
    - 20,000 random configurations give no negative value.
    - The identity agrees with finite differences of Abreu's formula.
    - $\mathbb{CP}^2$ gives the constant $6$.
    - I know no reference for this lemma; its Schur-product proof is half a page.
  - Conformal blowup of the $A_7$ point to a psc cylindrical $L(8,1)$ end is standard. A cone with $\mathrm{Scal}\ge0$ has a link with $\mathrm{Scal}\ge6$; then use the factor $1+c/R$.
  - LeBrun-type existence of psc Kähler metrics in Kähler classes of rational surfaces† would give the same pointwise statement on closed models, but not the face behaviour.
  - **So (a) proves the clamp pointwise in $H$, not for the family.**
- **(b) Wall-crossing numerics.** These show that the band is sharp and list its classes. They give no emptiness.
- **(c) The tube.** This settles the cusp only.

**Alternative [S].** On a compact Kähler surface with $p_g=0$ and $\eta\in\mathbb R\omega$, SW solutions correspond to effective divisors in $|(K+K_t)/2|$ or $|(K_t-K)/2|$, according to the sign (Witten; Friedman–Morgan; Morgan's book†). This needs no Scal $\ge0$. However, the conformal cylindrical completion destroys the Kähler condition. Using it would mean working on the compact toric orbifold and comparing with the isolated piece, which is not obviously shorter.

## 3. Vertex classes, lens faces, rational blowdown

**3.1 The vertex classes are forced [V].**
- Stretching a neck along a rational homology sphere splits $H^2(\,\cdot\,;\mathbb R)$ orthogonally, and the $L^2$ self-dual form lives on the $b^+$ side (APS).
- At the four corners the main piece $M_I$, and the only positive ray it carries, are:

| corner | $M_I$ | positive ray |
|---|---|---|
| $(N_1,J_2)$ | $C_{1,2}\setminus N_1$ | $X_1^\perp\cap\langle U,X_1\rangle=\mathbb R H_1$ |
| $(J_1,N_2)$ | $C_{1,1}\setminus N_2$ | $\mathbb RH_2$ |
| $(N_1,N_2)$ | $C_2\setminus(N_1\sqcup N_2)$ | $\{X_1,X_2\}^\perp=\mathbb RH_{12}$ |
| $(J_1,J_2)$ | $\nu U$ | none: $U^2=0$, the cusp |

- So $H_I$ is the projection of $U$ to $X_I^\perp$, and $a=\tfrac14$ is the solution of $H\cdot X_1=1-4a=0$.
- The bilinear interpolation is a choice. Lemma B needs only $H(t)\in\Pi$ with the correct supported vertices.
- $\Pi$ is the closure of the normalized Kähler cone of the toric orbifold: all five edges have length $\ge0$.

**3.2 Edge collapse is neck stretching [V, fan computations in `toric.py`].**
- The edges of $\mathcal P(a,b)$ have affine lengths $(a,\,1-4a,\,a+b,\,1-4b,\,b)$ for $(p,X_1,U,X_2,q)$.
- The outer vertex is $\tfrac18(1,7)=A_7$, with link $L(8,7)=-\partial C_2$.
- Gluing in the $A_7$ chain gives a smooth toric surface $Z=C_2\cup_{L(8,1)}\nu(A_7)\cong\mathbb{CP}^2\#9\overline{\mathbb{CP}}{}^2$. Its cycle of self-intersections is $(-1,-4,0,-4,-1,-2^{7})$.

| collapsing edge | parameter | new vertex | neck | face |
|---|---|---|---|---|
| $X_i$ | $a=\tfrac14$ | Wahl point $\tfrac14(1,1)$ (contracting the $(-4)$-curve $X_i$) | $L(4,1)$ | lens |
| sloping $p$ | $a=0$ | outer vertex becomes smooth ($\det(n_q,n_1)=1$); $X_1$ is pushed into the end | $S^3=\partial C_{1,1}$ | $J$ side |
| $U$ | $a+b\to0$ | polygon degenerates to a segment | tube of length $1/(a+b)$ | cusp |

- These interfaces intersect pairwise. For example, $\partial C_{1,1}\cap\partial N_1\ne\varnothing$, since $X_1$ meets $U$. So no single metric has product collars on all of them.
- This is the real reason Section 6 needs a moving family. The toric picture handles it, because each interface is the preimage of a curve in the polygon.

**3.3 The corners as rational blowdowns ($\mathbb Q$-Gorenstein smoothings).**
- **One-sided corner [V topology; P identifications†].**
  - $\overline{C_{1,2}}=F_4$, with $X_1$ the negative section and $U$ the fibre, and $F_4=D(-4)\cup_{L(4,1)}D(+4)$.
  - The vertex polygon $(a,b)=(\tfrac14,0)$ is the triangle with normals $(1,4),(-1,0),(0,-1)$ and relation $n_p+n_o+4n_2=0$. This is $\mathbb P(1,1,4)$, punctured at a smooth vertex.
  - Rationally blowing down $X_1$ gives $D(+4)\cup B_2=\mathbb{CP}^2$ (conic neighbourhood and $\mathbb{RP}^2$ neighbourhood). This is the $\mathbb Q$-Gorenstein smoothing of the Wahl point, i.e. the degeneration $\mathbb{CP}^2\rightsquigarrow\mathbb P(1,1,4)$ (Manetti; Hacking–Prokhorov†). Its Milnor fibre is $B_2$ (Wahl; FS†).
  - Under this identification $4H_1=s_+=2h$, so $H_1=h/2$.
  - $\Lambda\cdot h=2\lambda_1=-3+2e_{j+1}$, so $\Lambda|=K_{\mathbb{CP}^2}$ or $-h$.
  - $K$ descends exactly when $K\cdot X_1\equiv2\pmod 4$, i.e. $d_1\equiv0\pmod4$ (FS†; C §2.3). In that case $K\cdot h=2(\lambda_1+z_1)$.
  - So for descending classes the vertex inequality at $H_1$ is the Kronheimer–Mrowka chamber structure of $\mathbb{CP}^2$ with perturbation $2\pi\Lambda^+$. The band is $K\cdot h\in(\Lambda\cdot h,0)\cap(2\mathbb Z+1)$: this is $\{-1\}$ if $\Lambda=-3h$, and $\varnothing$ if $\Lambda=-h$.
  - **The unique descending band class is $K=-h$, with $d_{\mathbb{CP}^2}=-2$, which becomes $0$ in the two-parameter family. It is exactly the exceptional case of Lemma C** [V arithmetic].
- **Two-sided corner [V].** The vertex $(\tfrac14,\tfrac14)$ has normals $(1,4),(-1,0),(1,-4)$ with relation $n_p+n_q+2n_o=0$. They span an index-4 sublattice. So the corner is the fake weighted projective plane $\mathbb P(1,1,2)/\mu_4$, with two Wahl points and the $A_7$ point. Here $H_{12}^2=\tfrac12$ (double rational blowdown).

**3.4 What the blowdown language gives.**

*Proposition E (clean form of the clamp) [V, given Theorem A and Lemma B].* At a parameter with period $H=\sum\theta_IH_I$, a reduced field forces, at some corner $I\ne\varnothing$ with $\theta_I>0$, the one-sided chamber inequality of the corner piece $M_I$:
$$K\cdot H_I<0\ (u>0),\qquad v\cdot H_I>0\ (u<0),\qquad \operatorname{sign}(u)\,v\cdot H_I\le0\ (\mathrm R).$$
For descending $K$ and $|I|=1$, this is the KM chamber inequality on $\mathbb{CP}^2=(F_4)_{X_i}$.

*Limits [V as logic].*
- Non-descending classes ($d_i\equiv2\pmod4$, $z_i\in\tfrac12+\mathbb Z$) do not extend over $B_2$. They are not seen by the blowdown, yet the clamp must handle them.
- The bit sum, which is the Fintushel–Stern projection onto descending classes (C §2.4), acts on instanton ends at lens faces, not on the reduced fields of the clamp.
- So rational blowdown explains the vertices, the lens faces and the exceptional class. It does not replace the lattice lemma.

## 4. Verdict

**Citable or classical, about 2 pp.**
- Theorem A.
- Lemma B.
- Proposition D, given the charge bound.
- Caps: a generic period avoiding the countably many walls (Donaldson's period argument†), together with the standard a priori $F^+$ bound. This is Prop. `estimates:cap` with its constants.

**Needs a written proof but is short and classical in style, about 4 pp.**
- The Guillemin–Abreu lemma $\mathrm{Scal}\ge0$ (1 p).
- Conformal cylindrical completion of cone points (½ p).
- Edge collapse equals neck stretching: the satellite rescaling and cone annulus, with uniform $C^k$ bounds (2 pp; Lemma `geometry:collars` and Prop. `geometry:assembly`, trimmed).
- Hodge theory on long rational necks (cite APS, ½ p).

**Genuinely needed, not supplied by any classical theorem I know [P].**
- **(1) The family.** A two-parameter family on each macro with periods in $\Pi$ and the prescribed genuine faces ($J_i$ round, $N_i$ psc and independent of the tangential parameters, compatible with both bits). It must include the moving interfaces of 3.2 and the corner replacement at the cusp (Lemma `geometry:tube`). The toric model is the natural construction; I see no shortcut.
- **(2) Uniform compactness.** Over the cube, at genuine faces, and in the order of choices: $C_W$, then $\epsilon$, then the regularization and isolation lengths, then the $Y$ lengths, then the perturbations.
- **(3) The charge of a reduced component** inside a $\mathrm{PU}(2)$ Uhlenbeck limit (Prop. `estimates:energy`, Lemma `estimates:cylinder`). This is the only input to Prop. D that is not SW, and it belongs with Sections 9–10.

**Suggested rewrite of Sections 6–7, about 9–11 pp in total [P].**
- §6.1 The toric dictionary (3.2): Guillemin metrics, the Scal lemma, cone points.
- §6.2 The family theorem, stated as in Thm. `geometry:family`, with the proof organized by edge collapse.
- §7.1 Theorem A + Lemma B + Lemma C, as Proposition E.
- §7.2 Proposition D at the cusp.
- §7.3 Caps.
- §7.4 Persistence and the order of choices.

**Confidence.**

| claim | label |
|---|---|
| The SW content of Section 7 is classical | [V] |
| The rewrite saves most of Section 7 | [P, 80%] |
| Section 6 is irreducible input but can be halved or better | [P, 60%] |
| A short citation-only replacement of Section 6 exists | [S, <10%] |

## 5. Checks (`agents/T3-checks/`)

- `abreu.py`, `abreu2.py`: Abreu scalar curvature for $M=C+\sum nn^t/l$.
  - The formula agrees with finite differences to about $10^{-3}$ relative.
  - 20,000 random samples give no negative value.
  - $\mathbb{CP}^2$ gives the constant $6$.
  - On the main polygon the minimum is about $0.36$ in the tips, and $\mathcal S=2$ (i.e. Scal $=4$) on the tube.
- `clamp.py`: the closed forms of Lemma `indices:positive-square`, and the parity maximum $-2$.
- `clamp_fast.py`: band or R wall ⇒ the manuscript's vertex test ⇒ $Q\le-2$ or the exception. 0 failures.
- `clamp_sharp.py`: the sharpened Lemma B. Worst bound $2$ for $u>0$ and $-6$ for $u<0$. The exception occurs only for $(0,0)$ with $d_1=0$, and for $(1,1)$ with $d_2=0$.
- `toric.py`: the singularity types $\tfrac18(1,7)$, $\tfrac14(1,1)$ and smooth; the Euler numbers $-4,0,-4$; $Z$ with 12 rays; $C_2\cong H\oplus\langle-8\rangle$; the $\Lambda=K_t+\dots$ table; $(H\cdot U)^2/H^2\ge\tfrac14$ on the lens face.
- `cusp.py`: the number of band values near the cusp is $2/a$.
