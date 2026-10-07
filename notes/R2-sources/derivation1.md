# Derivation 1. The numerology as two competing inequalities

Independent derivation from the manuscript TeX (`src/05-stack.tex`, `src/08-indices.tex`, with `02`, `03`, `06`, `07`) and first principles; our notes were used only for comparison.
Labels in code font are the manuscript's LaTeX labels.
Every number below was recomputed by hand and checked by exhaustive search over finite ranges of lattice evaluations (§7).

**Notation.** $X$ is the closed manifold obtained by capping the composite cobordism: caps $C_\pm$, then $n$ copies of $B$ (the cobordisms $W'_i$ with $(-4)$-spheres $S_i$), each followed by a return $Y_{-2}\to Y_2$. Of these returns, $m$ are the positive cobordism of $H=f_+f_-$ and the rest are $\phi$ (or a definite $V$).
$\Lambda=l+c$ with $l$ characteristic; $\Theta=(\Lambda^2-\sigma)/4$; energy $\kappa=c_2-c^2/4$; coupled Dirac index $n_D=\Theta-\kappa$ (eq. `indices:closed-indices`).
The dimension condition is $D_I=8\kappa-3(1+b^+)=n+z$ (eq. `stack:ordinary-dimension`).
An abelian class has $v=c_1(L_1)-c_1(L_2)\equiv c \pmod 2$ and $K=\Lambda+v$ (eq. `indices:split-classes`). Its Feehan–Leness level $\ell=\kappa+v^2/4$ must be a nonnegative integer (eq. `indices:ell`). This is Feehan–Leness's $((\Lambda-K)^2-p_1)/4$ with $p_1=-4\kappa$ (notes R1 §0, §(e2)).
Bits: $c_e=c_0+\sum e_i\,\mathrm{PD}(S_i)$, $\Lambda_e=\Lambda_0+\sum e_i\,\mathrm{PD}(S_i)$ (eq. `stack:bit-lifts`).

**Additivity.** Cut $X$ along the seams $Y_{\pm2}$ rather than along the $J_i$. The $Y_{\pm2}$ are rational homology spheres, so $H^2(X;\mathbb Q)$ splits orthogonally over the blocks; $b^+$, $\sigma$, $\Lambda^2$ and $v^2$ add, with relative rational squares on each block (convention after eq. `indices:charge`).
$\mathrm{PD}(S_i)$ is supported in the $i$-th copy of $B$. With this cut the bits never leave a copy of $B$, and the telescoping of Lemma `stack:telescope` disappears.

---

## 1. Contributions of the building blocks

### 1.1 A copy of $B$
$W'=(-X_2(K))\cup_{S^3}X_{-2}(K)\colon Y_2\to Y_{-2}$. Here $H_2=\langle F_l,F_r\rangle$, $F_l^2=F_r^2=-2$, $F_lF_r=0$, so $b^+=0$ and $\sigma=-2$. The $(-4)$-sphere is $S=F_l-F_r$ (eq. `negative:sphere`).
- **$\Theta=0$ for both lifts.** On every cell $(\Lambda_0F_r,\Lambda_0F'_l)=(-2,0)$ (Lemma `stack:lifts`). Hence $\Lambda_0F_l=0$, $\Lambda_0F_r=-2$ and $\Lambda_0S=2$ (eq. `stack:sphere-pairings`).
  - $\mathrm{PD}(S)$ evaluates $(-2,+2)$ on $(F_l,F_r)$. So the lift $e\in\{0,1\}$ has $(\Lambda_eF_l,\Lambda_eF_r)=(-2e,\,-2+2e)$ and $\Lambda_eS=2-4e=\pm2$.
  - $\Lambda_e^2=-\tfrac12(4e^2)-\tfrac12(2-2e)^2=-2=\sigma$, so $\Theta(W')=0$.
  - This is eq. `stack:global-bit-squares` localized. In the cell bookkeeping the same zero is the cancellation of the two trace halves, $(-\tfrac14+\tfrac e2)+(\tfrac14-\tfrac e2)$.
- **Energy $1/8$.** The copy contributes one interval parameter and one class $\mu(S)$ of degree 2: $i+1_t+1_s-3=0$ (eq. `negative:dimension`). The cut-down dimension $D_I+n-2n-z$ must vanish, so $8\kappa$ rises by $1$.
- **$n_D=-1/8$.**
- **Energy cost $1/2$.**
  - $c_e$ is even on $F_l,F_r$, so $h_l=vF_l$ and $h_r=vF_r$ are even, and $v^2|_{W'}=-\tfrac12(h_l^2+h_r^2)$ (eq. `stack:negative-dual-square`).
  - The class $\mu(S)$ is met at an abelian configuration iff $vS=h_l-h_r\neq0$ (Lemma `stack:tests`; Def. `indices:analytic-hypotheses`(ii)).
  - If it is met, some half is a nonzero even integer, so $-v^2/4\ge\tfrac12$, with equality at $(h_l,h_r)=(\pm2,0)$ or $(0,\pm2)$.
  - If it is missed, a point of the limit must lie on $S$. This raises the Feehan–Leness level by at least one, with distinct points for distinct spheres.
  - Manuscript: eq. `stack:negative-test-cost` ($8\kappa\ge4s$), and the "negative rule" in Lemma `indices:component-score`.

### 1.2 A positive cobordism (the positive piece)
$W_H\colon Y_{-2}\to Y_{2}$ is the path $-2\to-1\to0\to1\to2$, with four 2-handles.
- Each half $f_\mp$ has one negative and one null direction (proof of Cor. `ordinary:bridge`). Across $Y_0$ the null directions give the hyperbolic summand $\begin{pmatrix}2&1\\1&0\end{pmatrix}$ of $Q_P$ below. So $b^+(W_H)=1$ and $\sigma(W_H)=-4-2(-1)=-2$, by Novikov additivity from $P$, since each trace half has $\sigma=-1$.
- Filled with the adjacent trace halves, $W_H$ becomes the positive piece $P\cong\mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2$ with:
  - $Q_P=\begin{pmatrix}2&1\\1&0\end{pmatrix}\oplus(-I_4)$;
  - $F_r=G-\sum T_b$, $F'_l=G-2U$;
  - $b^+(P)=1$, $\sigma(P)=-4$ (Prop. `stack:lattice`).
- **$\Theta=1$.**
  - Take $\Lambda_0=(-2,-1;0,1,0,-1)$ and $c_0=(2,1;1,0,1,0)$ in evaluations on $(G,U;T_b)$ (eq. `stack:base-lifts`).
  - By $v^2=2xu-2u^2-\sum t_b^2$ (eq. `stack:positive-dual-square`), $\Lambda_0^2=4-2-2=0$ and $c_0^2=0$. Hence $\Theta(P)=(0+4)/4=1$.
  - Removing the trace halves (which contribute $-2$ and $0$) gives $\Lambda_0|_{W_H}^2=2$ and $\Theta(W_H)=(2+2)/4=1$. This holds for all bits, because bits act only inside copies of $B$. This is $m_{\rm cell}=1$ in eq. `stack:cell-theta`.
  - Check: $l=\Lambda_0-c_0=(-4,-2;-1,1,-1,-1)$ is characteristic, and $l^2=4=2\chi(P)+3\sigma(P)$.
- **Energy $3/8$.** $b^+$ rises by $1$ in $3(1+b^+)$.
- **$n_D=1-3/8=+5/8$.**
- **Energy cost $1/2$, which also pays for both adjacent $(-4)$-spheres.**
  - Write $x=vG$, $u=vU$, $t_b=vT_b$. Then $v\equiv c_e$ forces $x$ even, exactly two $t_b$ odd, and $u\equiv\lambda=\Lambda U=-1-e_j+e_{j+1}\pmod 2$ (eq. `estimates:vertex-values`). So $u$ is odd iff the two adjacent bits agree.
  - On $P$, $v^2=Q_0=2xu-2u^2-\sum t_b^2$ (eq. `indices:positive-square`).
  - **(a) $vU=0$.** This is forced on the long $S^2\times S^1$ tube (Cor. `estimates:tube`). Then $Q_0=-\sum t_b^2\le-2$, so $P$ alone costs $\ge\tfrac12$.
    - The two odd $t_b$ are $w_2$: the determinant is odd on $T_2-T_1$. This is forced by the odd determinant at $Y_0$, since $c_0F_0=1$ for $F_0=G-T_3-T_4$ (eq. `stack:middle-class`; proof of Lemma `stack:charge-costs`).
  - **(b) $u\neq0$.** The chamber condition (Thm. `estimates:clamp`(i)) holds for a nonempty set $I$ of whole adjacent sides:
    - $\mathrm{sign}(u)\,z_I\le0$ (zero spinor), or $\mathrm{sign}(u)\,z_I<|\lambda_I|$ (nonzero spinor);
    - here $z_I=vH_I$, $H_I=U+\tfrac14\sum_{i\in I}X_i$, $\lambda_1=-\tfrac32+e_{j+1}$, $\lambda_2=-\tfrac12-e_j$, $\lambda_{12}=-1$.

    Lemma `indices:positive-square` gives $Q:=Q_0-\tfrac12\sum_{i\in I}h_i^2\le-2$, where $h_i$ are the far halves of the two adjacent $(-4)$-spheres. So the positive cobordism *together with its two adjacent copies of $B$* costs $\ge\tfrac12$.
    - The single exception is a nonzero spinor with $|I|=1$ and $u=z_I=\pm1$. There $Q\le2$, but the selected sphere is missed ($d_i=0$), which forces level $\ge1$. The net cost is again $\ge-\tfrac12+1=\tfrac12$.
  - Two free copies of $B$ would cost $1$, so the marginal cost of the positive cobordism is $-\tfrac12$: it absorbs $\mu(S_j)$ and $\mu(S_{j+1})$.
  - Manuscript form: $8\kappa_i\ge4(s_N-z_0)+4m_i-8e_0+8\ell_i\ge4s_N+4m_i$ (eq. `indices:incidence-charge`).

### 1.3 A definite cobordism $V\colon Y_{-2}\to Y_2$ with $b_1=b^+=0$ (in place of $\phi$)
- $b^+=0$. No parameter and no class, so **energy $0$**.
- **$\Theta\le0$, with equality for a suitable lift**, hence **$n_D=0$**.
  - $N_V=X_{-2}\cup V\cup(-X_2)$ is closed and negative definite with $b_1=0$, hence diagonal $-I_r$ by Donaldson's theorem.
  - A characteristic class with all coordinates $\pm1$, $\Lambda_0F_r=-2$ and $\Lambda_0F'_l=0$ exists. It gives $\Lambda_V^2=\sigma(V)$ (notes T4 Lemma 3.1).
  - For $\phi$, $H_2=0$ and everything vanishes.
  - Manuscript analogue: $\langle-1\rangle^2$ with $\Lambda_0^2=-2=\sigma$, $m_{\rm cell}=0$ (eq. `stack:negative-lattice`, Lemma `stack:telescope`).
- **Energy cost $\ge0$.** $v^2|_V\le0$, and there is nothing to meet.
  - On $N_V$, Cauchy–Schwarz gives $-v^2\ge\tfrac12(h_r^2+h_l'^2)$, which is the only form in which §8 uses eq. `stack:negative-dual-square`.
- **Index of reducible flats on $V$.** Reducible flats on $V$ are central at both ends and have index $-3$ (notes T4 Prop. 3.4). The closed composition argument therefore survives.

### 1.4 A cap
- **$b^+\ge1$ each.** Each cap contains $A$ with $A^2=0$ and $cA$ odd (Prop. `estimates:cap`, proof). Write $b_0=b^+(C_-)+b^+(C_+)$.
- **Probes** of total degree $z$.
- **Energy $(z+3+3b_0)/8$.** The $3$ is the "1" in $3(1+b^+)$.
- **$\Theta=\Theta_0$**, which includes $(1-\Lambda(E_{\rm exc})^2)/4$ for each extra exceptional class. It is very negative once $|\Lambda(E_{\rm exc})|$ is chosen large.
- **$n_D=c_1:=\Theta_0-(z+3+3b_0)/8$.** This constant is fixed before the repetitions (Table `stack:choices`).
- **Energy cost.**
  - No zero-spinor abelian component contains a cap.
  - For a nonzero spinor, $v_W^2\le C_W$ and $(\Lambda_W+v_W)^2\le C_W$ (Thm. `estimates:clamp`(ii), eq. `estimates:cap-squares`). So a cap lowers the cost by at most $C_W/4$, independently of $n$, $m$ and $\Lambda(E_{\rm exc})$.
  - On short outside components, $|K E_{\rm exc}|\le B$ forces $|vE_{\rm exc}|\ge|\Lambda E_{\rm exc}|-B$. The exceptional class alone then costs $\ge(|\Lambda E_{\rm exc}|-B)^2/4$. This gives $q+4\ge8$ for outside components (Lemma `indices:end-exclusion`, eq. `indices:end-score`).

### 1.5 Table (energy and indices per block; costs are for an abelian class meeting the block's classes)

| block | $b^+$ | $\Theta$ | energy supplied | $n_D$ | minimal energy cost $-v^2/4$ (+ forced level) |
|---|---|---|---|---|---|
| copy of $B$ | $0$ | $0$ (both lifts) | $1/8$ | $-1/8$ | $1/2$ if $\mu(S)$ is met; level $\ge1$ if missed; $0$ if adjacent to a positive piece |
| positive cobordism $H$ | $1$ | $1$ | $3/8$ | $+5/8$ | $1/2$ for $H$ with both adjacent copies of $B$ (marginal $-1/2$); exception $-\tfrac12$ + level $1$ |
| definite $V$ (or $\phi$) | $0$ | $0$ (never $>0$) | $0$ | $0$ | $\ge0$ |
| caps (together) | $b_0$ | $\Theta_0$ | $(z+3+3b_0)/8$ | $c_1$ | $\ge-(C_{W_-}+C_{W_+})/4$; no zero-spinor case; $+(\lvert\Lambda E\rvert-B)^2/4$ on short outside components |

The sums of the table entries are:
$$b^+=m+b_0,\qquad \Theta=m+\Theta_0\ (\text{eq. `stack:total-topology`}),\qquad 8\kappa=n+3m+c_\kappa,\quad c_\kappa:=z+3+3b_0,$$
$$n_D=\frac{5m-n}{8}+c_1\ \ (\text{eq. `stack:dirac-growth`}),\qquad -\frac{v^2}{4}+T(v)\ \ge\ \frac{n-m}{2}-C,\quad C=\tfrac14(C_{W_-}+C_{W_+}).$$
Here $T(v)\le\ell$ counts the spheres met only through points of the limit. The last inequality is eq. `indices:incidence-charge` summed over $X$: $s_N=n-2m$, and the positive pieces contribute $4m$.

---

## 2. The two global inequalities

**(I) $n_D\to+\infty$.** This holds iff $5m-n\to+\infty$, i.e. asymptotically $m/n>1/5$.

**(II) No Seiberg–Witten class has nonnegative level.** For a class that occurs, $\ell\ge T(v)$. But
$$\ell-T(v)=\kappa-\Big(-\tfrac{v^2}{4}+T(v)\Big)\le\frac{n+3m+c_\kappa}{8}-\frac{n-m}{2}+C=\frac{7m-3n+c_\kappa}{8}+C .$$
The right side is negative once $3n-7m>c_\kappa+8C$, i.e. asymptotically $m/n<3/7$. Under this condition no class occurs on the unbroken manifold, at any level. (Below, $k_J$ denotes the number of true $J$-cuts of a limit, to keep $k$ for the spacing.)

In the manuscript, (II) is eq. `indices:end-lower`: a component containing a cap has $q\ge3L-7m+2\sum v(E_{\rm exc})^2-C$.
- With no cut ($k_J=0$) the single component has $q_1=0$ (eq. `indices:phase-count`), so a Seiberg–Witten class forces $3L-7m\le C$.
- Spacing gives $m\le(L+3)/4$, hence $3L-7m\ge(5L-21)/4$, which yields $q_1+4\ge8$ (eq. `indices:end-score`; Prop. `indices:fixed-exclusion`, case $k_J=0$).

**Why they compete.**
- A positive piece raises $n_D$ by $5/8$. It also raises the best possible level by $3/8+1/2=7/8$: it supplies $3/8$ and absorbs two spheres' worth of demand.
- A copy of $B$ lowers $n_D$ by $1/8$ and changes the level bound by $1/8-1/2=-3/8$.
- So $n_D\approx(5m-n)/8$ and $\ell-T\lesssim(7m-3n)/8$. The first must grow and the second must decrease: $\tfrac15<m/n<\tfrac37$.

**Per period of spacing $k$** ($k$ copies of $B$, one positive cobordism, $k-1$ copies of $V$), all multiplied by $8$:
- supplied: $8\Delta\kappa=k+3$;
- Dirac capacity: $8\Delta\Theta=8$;
- demanded: $(k-2)\cdot4+4=4k-4$.

Then (I) $\iff k+3<8\iff k<5$, and (II) $\iff k+3<4k-4\iff k>7/3$.
With the manuscript's spacing 4, $n=4m+p$. Then $n_D=(m-p)/8+c_1$ and $3n-7m=5m+3p$ (Thm. `stack:nonzero`).

---

## 3. Local versions

**Why local.**
- The faces of the cube cut $X$ along any subset of the $J_i$. A limit can be abelian on any segment of consecutive pieces, while free or ASD components carry the rest.
- The segment's energy is then constrained by the dimension identities $\sum(q_i+4)=4$ and $\sum i_i-2\eta=2-4k_J$ (eq. `indices:virtual-sums`), not by the global supply.
- So each segment needs its own inequality, and only the *local* spacing of positive pieces enters. A global density below $3/7$ says nothing about a segment on which positive pieces are crowded.

**Two weightings of a segment $\Gamma$.** Let $\Gamma$ have $L$ pieces, $m$ of them positive, $s$ assigned spheres, and endpoint bit difference $\Delta\in\{-1,0,1\}$.

- **(F) ASD and Seiberg–Witten limits** (no free component). The filled segment has
  $q_\Gamma+4=8\kappa_\Gamma-3m+L-2s$ (proof of Lemma `indices:component-score`).
  The weights are: energy $8$, each piece $+1$ (interval parameter), positive piece $-3$, sphere $-2$.
  - A free copy of $B$ contributes $4+1-2=+3$.
  - A positive cobordism with its two copies contributes $4+2-4-3=-1$.
  - Per period: $3(k-2)-1=\mathbf{3k-7}$. This is exactly minus the per-period change $7-3k$ of the level bound in (II): (F) is (II) localized.
- **(M) Mixed limits** (a free SO(3)-monopole component and zero-spinor abelian segments). The projection forgets the zero-spinor fields but keeps their interval parameters. A segment is therefore charged
  $4+i-p=6\kappa_\Gamma+1-m+\Delta-2s$ (proof of Lemma `indices:mixed-run`).
  The weights are: energy $6=8-2$ (instanton index plus twice the coupled Dirac index), positive piece $-3+2\Theta=-1$, sphere $-2$, parameters $0$.
  - A free copy of $B$ contributes $3-2=+1$.
  - A positive cobordism with its two copies contributes $3-1-4=-2$.
  - Per period: $(k-2)-2=\mathbf{k-4}$.
- **Coupled Dirac index:** $\Delta n_D=\mathbf{(5-k)/8}$ per period.

**Endpoint count (exact segment minima).** Let $\Gamma$ have $m\ge1$ positive pieces at mutual distance $k$, plus $g\ge0$ extra negative pieces in wider gaps. Let $a,b$ be the numbers of negative pieces before the first and after the last positive piece, and let $\varepsilon_a,\varepsilon_b\in\{0,1\}$ record whether the two boundary spheres are assigned to $\Gamma$. Then
- $L=k(m-1)+1+a+b+g$ and $s=L-1+\varepsilon_a+\varepsilon_b$;
- $f=[a=\varepsilon_a=0]+[b=\varepsilon_b=0]$ counts end positive pieces whose outer sphere is assigned outside;
- the spheres not adjacent to positive pieces number $s-2m+f$ (valid for $k\ge2$);
- eq. `indices:incidence-charge` gives $8\kappa_\Gamma\ge4(s-2m+f)+4m$.

Substituting:
$$q+4\ \ge\ (3k-7)m-3k+1+\big[3a+2\varepsilon_a+4f_a\big]+\big[3b+2\varepsilon_b+4f_b\big]+3g\ \ge\ (3k-7)m-3k+5,$$
$$4+i-p\ \ge\ (k-4)m-k+r+\Delta+g+\big[a+\varepsilon_a+3f_a\big]+\big[b+\varepsilon_b+3f_b\big]\ \ge\ (k-4)m-k+2 .$$
Each bracket in the first line is $\ge2$; each in the second is $\ge1$; and $r\ge1$, $\Delta\ge-1$. For $m=0$ the bounds are $\ge1$ and $\ge0$.
- At $m=1$ both minima equal $-2$: a lone positive piece with both adjacent spheres assigned to it, $\kappa=\tfrac12$.
- An exact minimisation with all parities, bits and chamber conditions (§7) shows:
  - the first bound is attained for all $m$;
  - the second is attained for all $m$ when $k$ is odd, but only for odd $m$ when $k$ is even. For even $k$ and even $m$ the minimum is one larger.

**Bit parity.** Attaining the second bound needs $\Delta=-1$, i.e. an odd number of bit changes along $\Gamma$. At minimal cost these changes come from two sources:
- every positive piece changes the bit, since $u=0$ needs $e_j\ne e_{j+1}$ (a zero-spinor piece with $u\ne0$ has $Q\le-4$);
- a negative piece changes it iff its evaluations $(va,vb)$ are odd. Paying the $k-2$ inner spheres of a gap with one nonzero half each makes the number of odd pieces $\equiv k-2\pmod 2$.

So the number of changes is $\equiv m+(m-1)k\pmod2$. This is odd for all $m$ when $k$ is odd, and odd only for odd $m$ when $k$ is even.

**What the exclusions require.**
- **(F)** ASD components have $q+4\ge4$, and outside Seiberg–Witten components have $q+4\ge8$ (Lemma `indices:end-exclusion`). When $k_J>0$ there are $\alpha+\beta\ge2$ such components ($\alpha$ ASD, $\beta$ outside Seiberg–Witten) and at most $\alpha+\beta-1$ abelian segments between them.
  - If every segment is $\ge-3$, then $\sum(q_i+4)\ge4\alpha+8\beta-3(\alpha+\beta-1)=\alpha+5\beta+3\ge5>4$, contradicting the required total $4$.
  - The manuscript proves $\ge-2$ and gets $\ge6$ (Lemma `indices:fixed-run`, Prop. `indices:fixed-exclusion`).
  - Requirement: $(3k-7)m-3k+5\ge-3$ for all $m$, i.e. **$k\ge3$**.
- **(M)** The projected dimension is $\le5-4N-\sum(4+i-p)-(\text{losses})$ (eq. `indices:projected-dimension`). When $k_J>0$, $N\ge2$ (no outside component has zero spinor), and there are at most $N-1$ zero-spinor segments.
  - Segments $\ge-2$ give $3-2N<0$ (Prop. `indices:mixed-exclusion`).
  - A segment at $-3$ with $N=2$ gives $0$, which is not excluded.
  - Requirement: $(k-4)m-k+2\ge-2$ for all $m$, i.e. **$k\ge4$**.

---

## 4. Spacing by spacing

**Explicit lattice data** for a positive piece between bits $e$ (left) and $f$ (right), and for a negative piece:
- $P_*$: $u=0$ (needs $e\ne f$), $x=2$, and $t=(1,0,-1,0)$ if $e=0$, $t=(0,1,0,-1)$ if $e=1$. Then $Q_0=-2$, and both halves $vF_r=vF'_l=2$.
- On a negative piece, $(va,vb)$ with $va\equiv vb\equiv e+f\pmod2$. This follows from $c_e|_N=-e\,\mathrm{PD}(F_r)+f\,\mathrm{PD}(F'_l)$ and $a,b=(F_r\pm F'_l)/2$.
  - $N_0=(0,0)$: equal bits, halves $(0,0)$, cost $0$.
  - $N_1=(1,-1)$: different bits, halves $(vF_r,vF'_l)=(0,2)$, cost $\tfrac12$.

All configurations below were checked for parity, incidence and the chamber condition. Columns (I) and (II) list eight times the change per period.

| $k$ | (I) $8\Delta n_D$ | (II) supply $-$ demand | (F) min | (M) min | verdict |
|---|---|---|---|---|---|
| 1 | $+4$ | $4-4=0$ at best | — | — | (II) fails; local estimates unavailable |
| 2 | $+3$ | $5-4=+1$ | $-m-1$ | $-2m$ ($m$ odd), $-2m+1$ ($m$ even) | (II), (F), (M) fail |
| 3 | $+2$ | $6-8=-2$ | $2m-4\ge-2$ | $-m-1$ | only (M) fails |
| 4 | $+1$ | $7-12=-5$ | $5m-7\ge-2$ | $-2$ ($m$ odd), $-1$ ($m$ even) | all hold; (M) does not grow |
| 5 | $0$ | $8-16=-8$ | $8m-10$ | $m-3$ | (I) fails |
| $\ge6$ | $5-k<0$ | $7-3k$ | | | (I) fails, $n_D\to-\infty$ |

- **$k=1$ (no $\phi$ or $V$).**
  - $n_D$ grows by $1/2$ per period.
  - (II) fails. Crudely, $3n-7m\approx-4m$. Sharply, no copy of $B$ is free, so the guaranteed demand per period is only the positive piece's $\tfrac12$, which equals the supply $(1+3)/8$.
  - Explicit class: $u=0$, $x=0$, $t=(1,0,1,0)$ and $(0,1,0,1)$ alternately, bits alternating. Every sphere is met with $vS=2$, and $-v^2=2$ per piece. So $\ell=(n-m+c_\kappa)/8+(\text{cap terms})$ does not decrease with $m$.
  - Even this is optimistic. Consecutive positive pieces share a $(-4)$-sphere, so their plumbings $X_1\cup U\cup X_2$ overlap. The toric family (Thm. `geometry:family`) and the chamber condition are not available, and the neighbouring halves reserved in Lemma `indices:positive-square` are shared.
  - Per-piece chamber inequalities alone allow the chain $u=1$, $x_j=4+2j$, $t=(1,0,-1,0)$, bits $0$, with the last piece taking $u=0$. Each piece satisfies the chamber condition with $I=\{2\}$, $z_2=0$, for either type. The chain has $-v^2\to-\infty$, so no local energy bound survives.
- **$k=2$.**
  - (II) fails: the supply is $5$ and the demand $4$ per period. The periodic class ($P_*$ on positive pieces, $N_0$ on negative pieces, bits $\dots0,1,1,0,0,1,1,0\dots$) meets every sphere with $vS=\pm2$ and has $\ell$ growing like $m/8$.
  - (F) fails. Take the segment $P\,N\,P\,N\,P$ with bits $0,1,1,0,0,1$, configurations $P_*,N_0,P_*,N_0,P_*$, and both boundary spheres inward. Then $-v^2=6$, $\kappa_\Gamma=\tfrac32$, $L=5$, $s=6$, $m=3$, and $q+4=12-9+5-12=-4$. The limit ASD $|\,\Gamma\,|$ ASD has total $4-4+4=4$, as required, so it is not excluded. ($P\,N\,P$ has $-3$ and is still excluded.)
  - (M) fails.
  - The ordinary layer also fails. No single copy of $B$ separates consecutive cobordisms $BHB$, so one external seam borders two of them. Then $A\le S$ in Prop. `stack:composition` fails, and $3S-2A=-1$ is possible (notes T4 Prop. 3.5).
- **$k=3$.**
  - (I), (II) and (F) hold.
  - (M) fails. Take $P\,N\,N\,P$ with configurations $P_*,N_1,N_0,P_*$, bits $0,1,0,0,1$, zero spinor, and both boundary spheres inward. Then $-v^2=6$, $s=5$, $\Delta=-1$, and $4+i-p=9+1-2-1-10=-3$. With $N=2$ the projected dimension bound is $5-8+3=0$, not negative.
  - $(P\,N_1\,N_0)^3P$ gives $-5=(k-4)m-k+2$ at $m=4$. This agrees with notes T1 §3.4.
  - **Genuine or artifact?** It is an artifact of the method used for mixed limits, not a demonstrated obstruction:
    - (I), (II) and (F) all hold at $k=3$, so every Seiberg–Witten class and every limit without a free component is excluded.
    - No consistency argument forces failure (contrast $k=1$).
    - The projection charges a zero-spinor segment its full virtual SO(3)-monopole index and keeps all its interval parameters. It ignores the wall condition: on a positive piece, zero spinor forces $vH=u+a\,d_1+b_0\,d_2=0$ (Lemma `estimates:projection`; period eq. `geometry:period`).
    - In every configuration attaining the bound, $u=0$ and $d_1,d_2$ have the same sign (cost $\tfrac12$ forces $\sum t_b^2=2$ and zero reserved halves). So $vH\ne0$ on the whole positive-width toric region, and such zero-spinor configurations can occur only in the small-width region. The manuscript does not address whether they fill an open set of parameters there.
    - Counting one wall condition per positive piece would give mixed excess $k-3$ per period, and spacing 3 would suffice (notes D §4.5, T1 §3.7). This needs an unproved transversality statement.
    - The bound is attained by explicit classes, so no sharper arithmetic within the projection method helps.
- **$k=4$.**
  - Everything holds: $n_D$ grows by $+1/8$ and the level falls by $-5/8$ per period.
  - The per-period excess of (M) is $0$. Its exact minimum is $-2$ for odd $m$ and $-1$ for even $m$ (bit parity). Spacing 4 is the minimum for the method.
- **$k=5$.**
  - $8\Delta\kappa=8=8\Delta\Theta$, so $n_D=\Theta_0-(p_-+p_++z+3+3b_0)/8$ is independent of the number of periods.
  - $\Theta_0$ was made very negative by the large $|\Lambda E_{\rm exc}|$, chosen first, and the pads are long. So $n_D<1$: no instanton link $\mathbb{CP}^{n_D-1}$ and no relation.
  - All exclusions hold.
- **$k\ge6$.** $n_D$ falls by $(k-5)/8$ per period.
- **Mixed gaps.** Every gap must be $\ge4$ and the average gap $<5$. The manuscript uses all gaps equal to $4$.

---

## 5. Why positive pieces, why $\phi$ (or $V$), and $HB\equiv1$

**Positive pieces are needed.**
- Energy cannot be made negative at $\pm2$: each copy of $B$ adds $1/8$. (At $\pm1$ each interval lowers $8\kappa$ by $1$; notes T4 §4.3.) So the only vanishing mechanism is $n_D\ge1$.
- Copies of $B$ have $n_D=-1/8$.
- Definite blocks cannot raise $\Theta$. A closed smooth negative-definite piece has diagonal form (Donaldson; for $N_\phi=\langle-1\rangle^2$ directly). Every characteristic $\Lambda$ there has odd coordinates, so $\Lambda^2\le-\mathrm{rank}=\sigma$ and $\Theta\le0$. Bits only move $\Theta$ between the two halves of a copy of $B$.
  - "Definite" alone is not enough: $-E_8$ has $\Lambda=0$ with $\Lambda^2-\sigma=8$. Diagonality is what is used.
- Hence $b^+>0$ is necessary. $P$ gives $\Theta=1$ for $b^+=1$, a net $+5/8$ worth five copies of $B$: this is the $1/5$.
- $\Theta(P)=1$ is a choice, not forced by topology.
  - Keep the trace evaluations $(\Lambda F_r,\Lambda F'_l)=(-2,0)$ fixed. Then $x=2u$, $\sum t_b=2u+2$ and $\Lambda|_P^2\approx u^2$, where $u=\Lambda U$. For example $\Lambda=(-6,-3;-2,-1,0,-1)$ gives $\Lambda|_P^2=12$ and $\Theta(P)=4$.
  - But then $\lambda=\Lambda U=-3$ and $|\lambda_1|=\tfrac72$. The chamber band widens and Lemma `indices:positive-square` fails, since it uses $|\lambda_I|\le\tfrac32$ (eq. `estimates:vertex-values`).
  - The narrow band, not the lattice, pins $\Theta(P)=1$.

**$\phi$ or $V$ is needed.**
- (II) needs most copies of $B$ to be followed by a return $Y_{-2}\to Y_2$ with $b^+=0$.
- Without $\phi$ the available returns are $H$ ($b^+=1$, through $Y_0$) and the reversed interval $-W'=(-X_{-2}(K))\cup_{S^3}X_2(K)$. The latter has two classes of square $+2$, so it is positive definite with $b^+=2$, which is worse.
- So every copy of $B$ is followed by $H$: $k=1$, $m/n\to1>3/7$, and (II) fails (§4).
- $\phi$, or $V$ with $b_1=b^+=0$ inducing an isomorphism mod 2, is a return with $b^+=0$, $\Theta=0$, energy $0$, $n_D=0$ and cost $\ge0$. It allows $k-1$ free returns per period.
- The operator of one period is $\mathcal A^3\mathcal D$ with $\mathcal A=\phi_*B$ and $\mathcal D=HB$ (Thm. `stack:nonzero`).
- $b_1(V)=b^+(V)=0$ is what keeps central contacts on $V$ costing $3$.

**$HB\equiv1$ mod 2.**
- Over $\mathbb F_2$, $f_+g_+\simeq J_2$ (a continuation; eq. `ordinary:two-step-identity`), and the mirror gives the analogue for $f_-,g_-$ (Thm. `ordinary:units`). All four maps are isomorphisms mod 2.
- The four-step family identifies $B$ mod 2 with $g_-g_+$ (Lemma `negative:four-topology`, proof of Thm. `negative:unit`).
- Hence $B\equiv g_-g_+=f_-^{-1}f_+^{-1}=H^{-1}$, i.e. $HB\equiv1$ up to the fixed end identifications. The manuscript does not state this; it is a consequence (notes B4 §1).
- Consequence: the positive pieces are invisible to the nonvanishing argument and enter only through the indices.
- Consistency check:
  - A $\phi$-free composite $(HB)^M$ has operator $\equiv1$, so $\Omega\equiv\pm$(cap pairing) mod $2^N$, while $n_D\to\infty$.
  - If the exclusions held at $k=1$, this would force the cap pairing of $\phi$-free caps to vanish mod $2^N$ for every knot, with no cosmetic hypothesis.
  - So the exclusions must fail at $k=1$, and §4 shows that they do.
  - Caveat: the manuscript's caps contain $\phi^{-1}$ through $T=f_-\phi^{-1}f_+$ (Cor. `ordinary:bridge`). The check applies to $\phi$-free caps whose pairing is nonzero, and that pairing is not computed anywhere.

---

## 6. Verification against the manuscript

| number | value | manuscript reference | status |
|---|---|---|---|
| $b^+(P),\sigma(P)$ | $1,-4$ | Prop. `stack:lattice` | agrees |
| $\Lambda_0^2$ on $P$; on $N$ | $0$; $-2=\sigma$ | eqs. `stack:base-lifts`, `stack:positive-dual-square`; proof of Lemma `stack:telescope` | agrees |
| $\Theta$: cell; $B$; $H$; $V$ | $m_{\rm cell}+\tfrac{e_j-e_{j+1}}2$; $0$; $1$; $0$ | eq. `stack:cell-theta` (block values derived) | agrees |
| $\Lambda_eS_i$; $\Lambda_e^2$ | $\pm2$; independent of $e$ | eqs. `stack:sphere-pairings`, `stack:global-bit-squares` | agrees |
| $8\kappa$ | $n+3m+z+3+3b_0$ | eq. `stack:ordinary-dimension`; proof of Thm. `stack:nonzero` | agrees |
| $n_D$ | $(5m-n)/8+c_1$; $q_0/8+\dots$ | eq. `stack:dirac-growth`; Thm. `stack:nonzero` | agrees |
| cost of a sphere; of a positive piece | $8\kappa\ge4$; $\kappa\ge\tfrac12$ | eqs. `stack:negative-test-cost`, `stack:positive-charge`, `indices:incidence-charge` | agrees |
| $Q\le-2$; exception $Q\le2$ | | Lemma `indices:positive-square` | agrees; maxima $-2$ ($u=0$), $-6/-4$ (zero spinor), $-2$ and $2$ (nonzero spinor) |
| $\lambda,\lambda_1,\lambda_2,\lambda_{12}$; $u\equiv\lambda$ | $-1-e+f,\ -\tfrac32+f,\ -\tfrac12-e,\ -1$ | eqs. `estimates:vertex-values`, `indices:lambda-values` | agrees |
| identities | $\sum(q_i+4)=4$; $\sum i_i-2\eta=2-4k_J$ | eq. `indices:virtual-sums` | agrees |
| fixed-limit lower bound; table | $\ge-2$; $(1,1)$: $2,0,-2$; $(1,2)$: $1,-1,1$ | Lemma `indices:fixed-run` | agrees |
| mixed-limit lower bound | $\ge s-4m+r+\Delta+3\,{\rm miss}\ge-2$ | eqs. `indices:mixed-run`, `indices:mixed-run-sharp` | agrees |
| exclusions | $2\alpha+6\beta+2\ge6$ (manuscript's $2a+6b+2$); $3-2N\le-1$ | Props. `indices:fixed-exclusion`, `indices:mixed-exclusion` | agrees |
| inequality (II), manuscript form | $q\ge3L-7m+2\sum v(E)^2-C$; $3L-7m\ge(5L-21)/4$ | eqs. `indices:end-square`, `indices:end-lower`, `indices:end-score` | agrees with $(7m-3n+c_\kappa)/8+C$ |
| spacing | positive pieces at least 4 apart; $L\ge4m-3+a+b$ | §5 opening; Cor. `stack:interior` | agrees |

**Flags.**
1. **Spacing 4 is used throughout, but only one lemma needs it.**
   - The manuscript states spacing 4 everywhere. Only Lemma `indices:mixed-run` needs it.
   - The conclusion of Lemma `indices:fixed-run` holds at spacing 3. Its proof uses $L\ge4m-3$, but with $L\ge3m-2$ its bound $\max(2s+L-7m,\,m+L-2s)$ still has minimum $-2$.
   - Prop. `stack:composition` needs spacing $\ge3$, so that a single copy of $B$ lies between positive pieces.
   - This is slack, not an error.
2. **"$\Lambda^2\le\sigma$ on definite lattices" needs diagonal.** This is automatic for $\langle-1\rangle^2$. For $N_V$ it uses Donaldson's theorem.
3. **$HB\equiv1$ mod 2 is not stated in the manuscript.** It follows from the cited results up to fixed end identifications.
4. **Our notes overstate the $k=1$ failure.**
   - T1 §3.4(5) and exposition §7 say the level bound "grows like $+4$ per period" at $k=1$. That uses the bound $(n-m)/2$, which is not the right demand at $k=1$. The sharp per-period balance is $0$, or worse given the overlap; the conclusion (no exclusion) is unchanged.
   - Exposition's "Seiberg–Witten classes do contribute" should read "cannot be excluded".
5. **Notes D §4.4** says "three negative-rule tests" per positive piece at $k=4$. The correct count is two spheres not adjacent to the positive piece (three negative pieces).
6. **Notes B4 §4** gives the sharp mixed bound as "$2$" at spacing 4 and "$4-m$" at spacing 3. The exact minima are $-2$ and $-m-1$. The conclusion is unchanged.
7. **The fixed exclusion tolerates $-3$, not only $-2$.** So at spacing 2 the first failing segment has $m=3$ ($-4$). D §4.3's example $(m,L,s)=(2,3,4)$ with $-3$ breaks the lemma but not the exclusion.

---

## 7. Checks performed

All checks are in `round2/checks/`.
- `lattice.py`: all lattice and index values of §1 in exact rational arithmetic, including $\Theta$ of cells for all bit pairs, parities and the $\lambda_I$.
- `positive_square.py`: exhaustive check of Lemma `indices:positive-square` over $|x|\le16$, $|u|\le6$, all $\sum t_b$ (with minimal $\sum t_b^2$), $|h_i|\le18$, all bits and types. No violation; the maxima are as in §6.
- `endpoint.py`: the closed forms of §3 against all endpoint data for $2\le k\le7$, $m\le8$. Also the manuscript's own fixed-limit bound at $k=2,3,4$.
- `segment_dp.py`: exact minimisation, recursive along the segment, over evaluations with all parities, bits, incidences and chamber conditions, for $k=2,3,4,5$, $m\le4$, all end data. Output is in `dp_table.txt`.
  - The minima agree with the closed forms of §3.
  - The one exception is the bit-parity shift of $+1$ in $4+i-p$ for even $k$ and even $m$.
- `verify_config.py` and `explicit.py`: the explicit configurations of §4 and the per-period demand $4k-4$ for $k=2,\dots,5$ (increments $4,8,12,16$).
