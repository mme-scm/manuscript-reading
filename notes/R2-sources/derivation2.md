# Derivation 2: the numerology as two competing inequalities

Independent derivation from the manuscript (`src/05-stack.tex`, `src/08-indices.tex`, with `02`, `03`, `04`, `07`) and from first principles. Labels in backticks are the manuscript's LaTeX labels. Every number below was recomputed by hand and then checked by exhaustive computer enumeration (files in `round2/checks2/`, §7).

## 0. Notation

- $n$ copies of $B$, hence $n$ disjoint $(-4)$-spheres $S_i$, $n$ interval parameters and $n$ tests $\mu(S_i)$ of real degree 2. $m$ positive pieces. $z$ is the total cap probe degree, $b_0=b^+(C_-)+b^+(C_+)$, $\Theta_0=\Theta(C_-)+\Theta(C_+)$.
- Energy $\kappa=c_2-c^2/4$. $\Theta=(\Lambda^2-\sigma)/4$ with $\Lambda=l+c$. Coupled Dirac index $n_D=\Theta-\kappa$. $D_I=8\kappa-3(1+b^+)$ (`indices:closed-indices`).
- Dimension condition $D_I=n+z$ (`stack:ordinary-dimension`), that is, $8\kappa=n+z+3+3b^+$.
- An abelian class (type $R$: zero spinor; type $S$: Seiberg–Witten) has $v=c_1(L_1)-c_1(L_2)\equiv c \pmod 2$, $K=\Lambda+v$, and Feehan–Leness level $\ell=\kappa+v^2/4\in\mathbb Z_{\ge0}$ (`indices:ell`).
- Positive piece: $P=X_{-2}(K)\cup W_H\cup(-X_2(K))$, filled by two balls, where $W_H$ is the cobordism of $H=f_+f_-$ along $-2\to-1\to0\to1\to2$.
  - Its lattice is $\langle G,U\rangle\oplus\langle T_1,\dots,T_4\rangle=\begin{pmatrix}2&1\\1&0\end{pmatrix}\oplus(-I_4)\cong\langle1\rangle\oplus5\langle-1\rangle$, the lattice of $\mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2$ (`stack:positive-lattice`).
  - Its trace classes are $F_r=G-\sum T_b$ and $F'_l=G-2U$, both of square $-2$. $U$ is a sphere of square $0$.
  - Write $v=(x,u;t)=(vG,vU;vT_b)$. Then $v^2=2xu-2u^2-\sum t_b^2$ (`stack:positive-dual-square`). Here $x$ is even, exactly two $t_b$ are odd, and $u\equiv\lambda\pmod2$.
- Spacing $k$: consecutive positive pieces are $k$ intervals apart. One period consists of $k$ copies of $B$, one positive cobordism and $k-1$ cosmetic returns, so $m/n\to1/k$.
- Pattern words such as `PNNP` list consecutive pieces after cutting at the $J_i$: positive pieces $P$, negative pieces $N=X_{-2}\cup\phi\cup(-X_2)$.

## 1. Contributions of the building blocks

**Additivity.** Cut $X$ along the seams $Y_{\pm2}$. These are rational homology spheres, so $H_2(X;\mathbb Q)$ is the orthogonal sum of the blocks' $H_2(\,\cdot\,;\mathbb Q)$. Hence $b^+$, $\sigma$, $\Lambda^2$ and $v^2$ are sums of block terms (relative rational squares, as in `indices:charge`).

The dimension condition is additive too. A block with $p$ interval parameters, tests of total degree $d$ and positive rank $b^+$ adds $d-p+3b^+$ to $8\kappa$. The trivial connection adds a single global $3$.

The manuscript cuts along the $3$-spheres $J_i$ instead (its "cells"). The two bookkeepings differ only in where the trace halves sit, and they agree after the telescope `stack:cell-theta`.

**Table 1.** "Least cost" is the least value of $-v^2/4+(\text{forced level})$ on the block, for an abelian class meeting its tests.

| block | $b^+$ | $\Theta$ | $8\kappa$ supplied | $n_D$ | least cost (energy) |
|---|---|---|---|---|---|
| copy of $B$: $W'=(-X_2)\cup_{S^3}X_{-2}$, one interval parameter, $\mu(S)$ | $0$ | $0$ for both bits | $+1$ | $-\tfrac18$ | $\tfrac12$ |
| positive cobordism $W_H$ (makes $P$) | $1$ | $1$ | $+3$ | $+\tfrac58$ | $\tfrac12$ for $P$ together with its two adjacent copies of $B$, i.e. net $-\tfrac12$ |
| definite $V:Y_{-2}\to Y_2$, $b_1=b^+=0$ (or $\phi$) | $0$ | $\Theta_V\le0$, best $0$ | $0$ | $\Theta_V$, best $0$ | $0$ ($-v_V^2/4\ge0$) |
| cap $C_\pm$ (old cap $W_\pm$ plus $E_\pm$) | $b^+(C_\pm)\ge1$ | $\Theta(W_\pm)+\tfrac{1-\Lambda(E_\pm)^2}{4}$ | $z_\pm+3b^+(C_\pm)$ | $\Theta(C_\pm)-\tfrac{z_\pm+3b^+(C_\pm)}8$ | $\ge-\tfrac{C_{W}}4+\tfrac{(vE)^2}4$; no type $R$ |
| trivial connection (global) | – | – | $+3$ | $-\tfrac38$ | – |

Summing the rows gives $b^+=m+b_0$ and $\Theta=m+\Theta_0$ (`stack:total-topology`). It also gives $8\kappa=n+3m+z+3+3b_0$, and
$$n_D=\frac{5m-n}{8}+\Theta_0-\frac{z+3+3b_0}{8}$$
(`stack:dirac-growth`).

**(i) A copy of $B$.**
- *Dimension.* $i+1_t+1_s-3=0$ (`negative:dimension`). Each copy adds one interval parameter and one test of real degree two. The closed family has dimension $D_I+n-2n-z$ (text before `stack:ordinary-dimension`), so each copy adds $1$ to $8\kappa$, and $n_D$ changes by $-\tfrac18$.
- *$b^+$ and $\Theta$.* $H_2(W')=\langle F_l,F_r\rangle\cong\mathrm{diag}(-2,-2)$ and $S=F_l-F_r$ (`negative:sphere`), so $b^+=0$ and $\sigma=-2$.
  - Every interval has $(\Lambda_0F_l,\Lambda_0F_r)=(0,-2)$ (`stack:lifts`). With $\Lambda_e=\Lambda_0+e\,\mathrm{PD}(S)$ this gives $(\Lambda F_l,\Lambda F_r)=(-2e,-2+2e)$.
  - Hence $\Lambda^2=-\big((\Lambda F_l)^2+(\Lambda F_r)^2\big)/2=-2=\sigma$ for $e=0,1$, and $\Theta=0$ for both bits.
  - This is where $\Lambda_0S=2$ (`stack:sphere-pairings`) is needed: it is exactly the condition $\Lambda_1^2=\Lambda_0^2$ (`stack:global-bit-squares`).
- *Cost.* Since $v\equiv c\pmod 2$ and $cF_l,cF_r\in\{0,\pm2\}$, the halves $h=vF_l$ and $h'=vF_r$ are even, and $v_{W'}^2=-(h^2+h'^2)/2$.
  - At a split connection the holonomy sweep has winding $vS/2$ (`stack:tests`). So the test is met iff $vS=h-h'\neq0$. Then one half is a nonzero even number and $-v_{W'}^2/4\ge\tfrac12$, with equality at $(h,h')=(\pm2,0)$ or $(0,\pm2)$.
  - If $vS=0$, the test can be met only by an ideal point (bubble) on the sweep support. That forces $\ell\ge1$ (Def. `indices:analytic-hypotheses`(ii)).
  - So the least cost is $\tfrac12$, i.e. $8\kappa\ge4$ per test (`stack:negative-test-cost`). Distinct tests use distinct halves.

**(ii) The positive cobordism.**
- *$b^+$ and $\Theta$.* $b^+(P)=1$ and $\sigma(P)=-4$ (Prop. `stack:lattice`).
  - $\Lambda_0=(-2,-1;0,1,0,-1)$ and $c_0=(2,1;1,0,1,0)$ (`stack:base-lifts`) have $\Lambda_0^2=c_0^2=0$, so $\Theta(P)=1$ (`stack:cell-theta`).
  - In block form: $\sigma(W_H)=-4+1+1=-2$ and the rational $\Lambda_0^2$ on $W_H$ is $0+2+0=2$, so $\Theta(W_H)=1$.
  - $\Theta=1$ is the largest value compatible with $\Lambda F_r=-2$, $\Lambda F'_l=0$ and $\Lambda U=-1$. These force $x=-2$, $u=-1$ and $\sum t=0$ with two odd $t_b$, so $\Lambda^2=2-\sum t^2\le0$.
  - The value $\Lambda U=-1$ keeps every chamber narrow: $|\Lambda H_I|\in\{\tfrac12,1,\tfrac32\}$ (`estimates:vertex-values`).
- *$8\kappa$ and $n_D$.* $8\kappa$ gains $3$ (from $b^+=1$; no parameter, no test), so $n_D$ gains $1-\tfrac38=\tfrac58$.
- *Chamber condition* (Thm. `estimates:clamp`(i)): either $u=0$ (forced on long tubes), or for some nonempty set $I$ of adjacent whole tests
  $$\operatorname{sign}(u)z_I\le0\ (R),\qquad \operatorname{sign}(u)z_I<|\lambda_I|\ (S),$$
  where $z_I=vH_I$, $H_I=U+\tfrac14\sum_{i\in I}X_i$, $X_1=-S_j$, $X_2=S_{j+1}$, and $\lambda_1=-\tfrac32+e_{j+1}$, $\lambda_2=-\tfrac12-e_j$, $\lambda_{12}=-1$ (`indices:lambda-values`).
- *Square estimate* (Lemma `indices:positive-square`). Combine $v_P^2$ with the outer halves $h_i$ of the selected adjacent copies of $B$. The result is $Q\le-2$, except for type $S$ with $|I|=1$ and $u=z_I=\pm1$. In that exceptional case $Q\le2$, and the selected test is missed ($d_i=0$), which forces $\ell\ge1$.
- *Cost.* The square of $P$ together with both adjacent copies of $B$ is $v_P^2-(h_1^2+h_2^2)/2\le Q$.
  - So $P$ together with its two adjacent copies of $B$ costs at least $\tfrac12$ ($8\kappa\ge4$), whatever happens to the two adjacent tests. The ordinary analogue is `stack:positive-charge`.
  - The value $\tfrac12$ is attained: $u=0$, $x=2$, $t=(1,0,-1,0)$, $Q=-2$.
  - Two copies of $B$ elsewhere would cost $1$. So each positive piece lowers the least cost by $\tfrac12$ net.
  - This accounting needs each copy of $B$ to be adjacent to at most one positive piece, i.e. $k\ge2$.

**(iii) A definite $V$ in place of $\phi$.**
- $b^+=b_1=0$, with no parameter and no test, so $8\kappa$ gains $0$.
- *$\Theta_V\le0$.* The closed piece $N_V=X_{-2}\cup V\cup(-X_2)$ is negative definite, hence diagonal by Donaldson's theorem. A characteristic class has odd coordinates, so $\Lambda^2\le-\operatorname{rank}=\sigma$, i.e. $\Theta(N_V)\le0$, with equality iff all coordinates are $\pm1$.
  - Equality can be arranged with $(\Lambda F_r,\Lambda F'_l)=(-2,0)$ (notes T4, Lemma 3.1).
  - With these trace values $\Theta(N_V)=\Theta_V$. So $n_D$ gains $\Theta_V\le0$, best $0$.
- *Cost.* $-v_V^2/4\ge0$, with no test and no forced level. The only estimate the argument uses on a negative piece is $v^2\le-\big((vF_r)^2+(vF'_l)^2\big)/2$, which holds by orthogonal projection.
- For $\phi$ itself $H_2=0$, and every entry of the row is $0$.
- Reducible flats on $V$ have index $-3(1-b_1+b^+)=-3$, so central contacts still cost $3$ in the gluing argument (T4 Props. 3.4–3.5; manuscript `stack:composition`).

**(iv) A cap.**
- $b^+(C_\pm)>0$ (`caps:pairing`(i)). The old pairing has $8\kappa=z+3(1+b^+)$ (proof of `caps:periods`).
- *$\Theta$.* The extra exceptional summand has $E^2=-1$, $cE=0$ and $\Lambda E$ odd (`caps:pairing`(ii); `stack:lifts`), so it contributes $(1-\Lambda(E)^2)/4$. A large $|\Lambda(E)|$ therefore lowers $\Theta_0$ by about $\Lambda(E)^2/4$.
- *Cost.*
  - No type $R$ component contains a cap (`estimates:clamp`(ii)).
  - For type $S$, $v_W^2\le C_W$ and $K_W^2\le C_W$ (`estimates:cap-squares`). So a cap can supply at most $C_W/4$ of energy, independently of $n$ and $m$.
  - The exceptional summand costs $(vE)^2/4$ with $vE$ even. On a short end component $|KE|\le B$, so $|vE|\ge|\Lambda(E)|-B$ (`indices:end-exclusion`). This excludes short end components. Long end components are excluded by (II) below, because the positive pieces are kept at least $L_*$ intervals away from the caps.

## 2. The two global inequalities

**(I) Index inequality.** The link argument needs $\eta=n_D-1\ge0$ phase cuts (`indices:phase-count`). By Table 1, $n_D=\frac{5m-n}{8}+c_1$, where $c_1$ is fixed before the repetitions and is made very negative by the end choices. So we need $5m-n\to+\infty$, i.e.
$$m/n>1/5 .$$

**(II) Level inequality.** Let $v$ be an abelian class on $X$ meeting all $n$ tests, $T(v)$ of them only through ideal points, so $\ell\ge T(v)$.
- Add the least costs of Table 1:
  - $n-2m$ copies of $B$ not adjacent to a positive piece, at $\tfrac12$ each;
  - $m$ positive pieces with their adjacent copies of $B$, at $\tfrac12$ each;
  - the caps, at least $-C$ with $C=\tfrac14(C_{W_-}+C_{W_+})$.
- This gives $-v^2/4+T(v)\ge\frac{n-m}{2}-C$.
- The supplied energy is $\kappa=\frac{n+3m+z+3+3b_0}{8}$. Hence
$$\ell-T(v)=\kappa-\Big(-\frac{v^2}4+T(v)\Big)\le\frac{7m-3n}{8}+C' ,$$
  and no Seiberg–Witten class has nonnegative level once $3n-7m>8C'$, i.e.
$$m/n<3/7 .$$
- In the manuscript this is `indices:end-lower` for the single component containing both caps ($L=n$): it gives $q\ge3n-7m-C$, which contradicts $q=0$.

**The competition.** Per block, the pair $\big(\Delta n_D,\ \text{upper bound for }\Delta(8\ell)\big)$ is:
- copy of $B$: $(-\tfrac18,\,1-4)=(-\tfrac18,-3)$;
- positive piece: $(+\tfrac58,\,3+4)=(+\tfrac58,+7)$;
- $V$: $(0,0)$.

Positive pieces feed (I) and starve (II); copies of $B$ do the reverse. Both inequalities hold iff
$$\tfrac15<m/n<\tfrac37 .$$
The window is nonempty because $\tfrac58/7>\tfrac18/3$: the ratio of index gained to level bound given away is larger for a positive piece than for a copy of $B$.

## 3. Local versions

**3.1 Why every segment must satisfy (II).** In a limit along the faces of the family with $k\ge1$ cuts at the spheres $J_i$, the components are the filled pieces between consecutive cuts.
- The cuts can sit at any of the $n$ faces. So any segment of consecutive pieces can carry abelian components, and it can be chosen to begin and end at positive pieces and to take the tests at its two cuts.
- The dimension identities are $\sum(q_i+4)=4$ and $\sum i_i-2\eta=2-4k$ (`indices:virtual-sums`), with $i_i=q_i+2n_{D,i}$.
- A global density bound therefore cannot control these limits. A local one is needed.

*Fixed limits* (anti-self-dual and Seiberg–Witten: types $A$, $R$, $S$ only).
- An irreducible anti-self-dual component has $q+4\ge4$. An outside $S$ component has $q+4\ge8$ (`indices:end-score`). Between these distinguished components lie at most (number of distinguished components $-1$) segments.
- So it suffices that every segment have $\sum(q+4)\ge-3$. The manuscript proves $\ge-2$ and gets $2a+6b+2\ge6>4$ (`indices:fixed-exclusion`).
- $-4$ is not enough: two rigid anti-self-dual components around a segment of excess $-4$ satisfy $\sum(q_i+4)=4$.

*Mixed limits* (a free $SO(3)$-monopole with zero-spinor abelian segments).
- The projection discards the type $R$ fields but keeps their parameters. A segment is therefore priced by $e_{PU}=\sum(4+i_i-p_i)$.
- The projected dimension is at most $5-4N-\sum e_{PU}-(\text{losses})$ (`indices:projected-dimension`), with $N\ge2$ components not of type $R$ and at most $N-1$ segments.
- $N=2$ already forces $e_{PU}\ge-2$ for every segment, and $-2$ suffices since $3-2N<0$ (`indices:mixed-exclusion`). The threshold $-2$ is exact.

**3.2 Fixed excess.** Take a segment with $L$ pieces, $m$ positive pieces and $s$ assigned tests, $L-1\le s\le L+1$.
$$e_I:=\sum(q_i+4)=8\kappa-3m+L-2s$$
(proof of `indices:component-score`; independent of internal cuts). The weights are: $8$ per unit of energy, $-3$ per positive piece, $+1$ per piece (its interval parameter), $-2$ per test.

From §1, $8\kappa\ge4(s-2m)+4m$, so $e_I\ge2s+L-7m$; also $e_I\ge m+L-2s$ (`indices:q-score`).
- *Per period* ($s=L=k$, $m=1$): $e_I$ changes by $3k-7$. This is $-1$ times the per-period change $7-3k$ of the bound for $8\ell$ in (II). **The fixed condition is (II) applied to segments.**
- *Exact minima over segments* (computer; they equal the closed form $(3k-7)m-3k+5$ of notes T1 Prop. 3.4):
  - $k=2$: $-m-1$;
  - $k=3$: $2m-4$;
  - $k=4$: $5m-7$;
  - $k=5$: $8m-10$.
- So every segment has $e_I\ge-2$ iff $k\ge3$. The value $-2$ comes from a single positive piece that takes both cut tests.
- The proof of `indices:fixed-run` assumes $L\ge4m-3$. It goes through with $L\ge3m-2$ if both bounds of `indices:q-score` are used for $m\le3$ (the minimum over $s$ is then $L-3m$); the minimum is again $-2$, at $m=1,2,3$, and $2m-8\ge0$ for $m\ge4$.

**3.3 Mixed excess.**
$$e_{PU}=r+6\kappa-m+\Delta-2s$$
(proof of `indices:mixed-run`), with $r$ components and $\Delta=e_a-e_b\in\{-1,0,1\}$ the telescoped bit difference. The $SO(3)$-monopole weights are:
- $6$ per unit of energy ($8$ from $D_I$, $-2$ from twice $n_D$);
- $-1$ per positive piece ($-3$ from $b^+$, $+2$ from $2\Theta=2$);
- $-2$ per test;
- parameters are retained, so they do not count.

From $6\kappa\ge3(s-s_P)+3m$ one gets $e_{PU}\ge s-4m+r+\Delta+3(2m-s_P)$ (`indices:mixed-run-sharp`), where $s_P$ counts the assigned tests adjacent to positive pieces.
- *Per period:*
  - a copy of $B$ not adjacent to a positive piece contributes $6\cdot\tfrac12-2=+1$;
  - a positive piece with its two adjacent copies of $B$ contributes $6\cdot\tfrac12-1-4=-2$;
  - in total $k-4$.
- *Lower bound:* $(k-4)(m-1)-2$, from the end inequality $a+\epsilon_a+3[a=0,\epsilon_a=0]\ge1$ at each end.
- *Exact minima:*
  - $k=3$: $-m-1$, attained (`PNNP`: $-3$; `PNNPNNPNNP`: $-5$);
  - $k=4$: $-2$ for odd $m$, $-1$ for even $m$;
  - $k=5$: $m-3$;
  - $k=2$: $-2,-3,-6,-7$ for $m=1,\dots,4$.
- So every segment has $e_{PU}\ge-2$ iff $k\ge4$.

**3.4 Per-period increments.** For $k\ge2$ the least cost $4k-4$ is attained (exact minimisation over periodic segments, $k=2,\dots,5$). So the level and fixed-excess columns are exact.

| $k$ | $\Delta n_D$ | $8\kappa$ supplied | least $8\kappa$ cost | $\Delta(8\ell)$ bound | fixed excess | mixed excess |
|---|---|---|---|---|---|---|
| 1 | $+\tfrac12$ | 4 | unbounded below | unbounded above | unbounded below | unbounded below |
| 2 | $+\tfrac38$ | 5 | 4 | $+1$ | $-1$ | $-2$ |
| 3 | $+\tfrac14$ | 6 | 8 | $-2$ | $+2$ | $-1$ |
| 4 | $+\tfrac18$ | 7 | 12 | $-5$ | $+5$ | $0$ |
| 5 | $0$ | 8 | 16 | $-8$ | $+8$ | $+1$ |
| $k\ge2$ | $\tfrac{5-k}8$ | $k+3$ | $4k-4$ | $7-3k$ | $3k-7$ | $k-4$ |

The conditions are: (I) $k\le4$; (II) and fixed limits $k\ge3$; mixed limits $k\ge4$. **Only $k=4$ satisfies all of them**, and the manuscript uses exactly $k=4$ ("at least four intervals apart", §5.1; Thm. `stack:nonzero`).

## 4. What goes wrong at each spacing

**$k=1$ (no cosmetic map: $C_-(HB)^MC_+$).** (I) holds, at $+\tfrac12$ per period. The abelian side fails, and more strongly than the formal count $7-3k=+4$ suggests.
- *Why.* Each copy of $B$ is adjacent to two positive pieces. The outer halves used in `indices:positive-square` then lie in positive pieces, and there is no negative square left to absorb $v_P^2$.
- *Explicit Seiberg–Witten classes.* Put all bits $0$ and take $v=(-2N,-1;1,0,1,2)$ on every positive piece, $N\ge2$.
  - Every test is met: $vS_i=6$.
  - $v^2=4N-8$ per piece.
  - The chamber condition holds with $I=\{2\}$: $\operatorname{sign}(u)z_2=-\tfrac12<|\lambda_2|=\tfrac12$.
  - The actual band $0<vH<-\Lambda H$ holds at $(a,b)=(\tfrac1{64},\tfrac3{16})$, since $vH=-1-6a+6b$ and $\Lambda H=-1-2a+2b$.
  - $K=\Lambda+v$ has $K^2=8N-4$ on each piece, i.e. Seiberg–Witten dimension $2N-2\ge0$.
  - Per period $\kappa$ grows by $\tfrac12$ while $-v^2/4$ falls by $N-2$, so $\ell=(N-\tfrac32)m+O(1)\to+\infty$. For $N=2$: $v^2=0$ and $\ell\approx m/2$.
- So (II) fails, and so do both local conditions.
- The manuscript's construction is not even available here: positive pieces must have disjoint neighbourhoods separated by single intervals (§5.1, `stack:composition`).

**$k=2$.** (I) holds, at $+\tfrac38$ per period.
- *(II) fails.* Per period the dimension condition supplies $\tfrac58$ of energy, while the least cost is exactly $\tfrac12$. This cost is attained with:
  - $u=0$, $x=2$, $\sum t=0$ on each positive piece;
  - both halves $0$ on each negative piece;
  - bits flipping across each positive piece.

  These classes have $\ell=m/8+O(1)$ (density $\tfrac12>\tfrac37$).
- *Fixed limits fail.* `PNPNP`, with both cut tests assigned to it, has $v^2=-6$, $\kappa=\tfrac32$, $s=6$ and $e_I=-4$. So the limit [rigid anti-self-dual | `PNPNP` | rigid anti-self-dual] satisfies $\sum(q_i+4)=4-4+4=4$ and is not excluded. `PNP` already gives $-3<-2$.
- *Mixed limits fail* ($-2$ per period).
- *The gluing identification fails.* Two neighbourhoods of positive pieces meet at a seam, so $A\le S$ in `stack:composition` is lost. The local bound becomes $(-2)+(-2)+3=-1<0$ (`stack:macro-excess`).

**$k=3$.** Most of the argument survives:
- (I) holds ($+\tfrac14$ per period);
- (II) holds ($-2$ in $8\ell$ per period);
- fixed segments have $e_I\ge-2$ (exact minimum $-2$);
- the gluing argument and the end exclusion hold.

Only the mixed inequality fails.
- *Explicit failure.* Take `PNNP` with bits $(0,1,0,0,1)$ and both cut tests assigned:
  - $u=0$, $x=2$, $t=(1,0,-1,0)$ on both positive pieces;
  - halves $(0,2)$ and $(0,0)$ on the two negative pieces.

  Then $\kappa=\tfrac32$, $\ell=0$, $s=5$, $\Delta=-1$, and $e_{PU}=1+9-2-1-10=-3$. The limit [free | `PNNP` | not $R$] has projected dimension at most $5-8+3=0$, so it is not excluded. In general the minimum is $-m-1\to-\infty$.
- *Genuine obstruction or artifact?* **An artifact of the method used for mixed limits, not a known obstruction.**
  1. The lattice minimum is attained, so no sharper counting within the projection method reaches $k=3$. The method genuinely needs $k=4$.
  2. Everything else (the global inequalities at density $\tfrac13$, the fixed limits, which carry the actual Seiberg–Witten ends, and the gluing) works at $k=3$.
  3. The loss comes from pricing a zero-spinor abelian segment as if it occurred for every value of its retained parameters. A type $R$ class must satisfy $vH=0$ on each positive piece, where $H$ is the period of that piece. This is a wall in the adjacent interval parameter, of codimension one whenever an adjacent test is met ($vS\ne0$, as in `PNNP`).
  4. Counting the walls would add $1$ per positive piece, giving $k-3$ per period. `PNNP` would then have excess $-1\ge-2$. This needs transversality of the period map to the walls, uniformly near faces, which is not proved (notes T1 §3.7, D §4.5).

**$k=5$.** The abelian side holds with room ($+8$ and $+1$ per period). (I) fails: $\Delta n_D=0$.
- With $n=5m+p$, $n_D=\Theta_0-(p+z+3+3b_0)/8$ is independent of the number of periods and fixed before them.
- The end choices push this constant down: large odd $\Lambda(E_\pm)$ (each lowers $\Theta_0$ by $(\Lambda(E)^2-1)/4$), and pads $p\ge2L_*$.
- So $n_D\ge1$ cannot be reached by repetition.

**$k\ge6$.** $n_D$ decreases by $(k-5)/8$ per period.

## 5. Why positive pieces, why the cosmetic map, and the check $HB\equiv1\pmod2$

**Positive pieces are needed.** Each copy of $B$ lowers $n_D$ by $\tfrac18$.
- A negative-definite piece cannot raise $\Theta$: its closed form is diagonal, a characteristic class has odd coordinates, so $\Lambda^2\le-\operatorname{rank}=\sigma$ and $\Theta\le0$.
- So a composite of copies of $B$ with definite returns has $n_D\le\Theta_0-(n+z+3+3b_0)/8\to-\infty$.
- $\Theta>0$ needs $b^+>0$. Raising $b^+$ by one costs $\tfrac38$ in $\kappa$, so a piece helps only if $\Theta>3b^+/8$. The positive piece has $\Theta=1$, giving $+\tfrac58$.

**The cosmetic map (or a definite $V$) is needed.** $B$ goes $Y_2\to Y_{-2}$, so composing copies of $B$ needs a return $Y_{-2}\to Y_2$. The returns available from surgery cobordisms are:
- $H$, with $b^+=1$ (increasing paths pass through $Y_0$, whose hyperbolic pair gives $b^+\ge1$);
- the reversed interval $-W'$, with form $\mathrm{diag}(2,2)$, i.e. $b^+=2$;
- $\phi$ or $V$, with $b^+=0$ and all five entries of Table 1 equal to $0$.

Without $\phi$ every copy of $B$ is followed by $H$: $k=1$ and $m/n\approx1>\tfrac37$, so §4 applies. The cosmetic map is exactly the device that dilutes positive pieces into the window $(\tfrac15,\tfrac37)$ while respecting the local spacing $4$.

**Consistency check.**
- On Floer homology mod 2, $B=g_-g_+$: the $Z_2$ face of the four-step family (Lemma `negative:four-topology` and the proof of Thm. `negative:unit`).
- $f_+g_+\simeq1$ (`ordinary:two-step-identity`), and the mirror construction gives $g_-f_-\simeq1$.
- Hence $B=(f_+f_-)^{-1}=H^{-1}$, so $HB=1$ mod 2, up to the fixed end identifications (only isomorphism mod 2 is used).

So a positive cobordism together with the preceding copy of $B$ is invisible to $\Omega$ mod 2; positive pieces enter only through $n_D$. The composite $C_-(HB)^MC_+$ has $\Omega\equiv\pm q\pmod{2^N}$ for suitable $M$ and $n_D\approx M/2\to\infty$, with no cosmetic map in the middle. If the vanishing half survived at $k=1$, the argument would prove too much. The numerology passes this test: at $k=1$ (II) fails in the strongest way (§4).

This is a check on the numerology only. At $k=1$ the manuscript's construction is unavailable anyway, and the caps still use $\phi^{-1}$ (notes B4 §4–5, T4 §2.2).

## 6. Verification against the manuscript

Each number used above, with the place where it is stated or implied:

| number | manuscript reference | check |
|---|---|---|
| $S^2=-4$, $F_l^2=F_r^2=-2$ | `negative:sphere` | ✓ |
| one parameter and one degree-2 test per copy of $B$ | `negative:dimension`; text before `stack:ordinary-dimension`; `indices:phase-count` | ✓ |
| $\Lambda_0S_i=2$, $c_0S_i=0$; $\Lambda_e^2=\Lambda_0^2$ | `stack:sphere-pairings`, `stack:global-bit-squares` | ✓ |
| negative cell $\Lambda_0^2=\sigma=-2$; positive cell $\Lambda_0^2=c_0^2=0$, $\sigma=-4$ | proof of `stack:telescope`; `stack:base-lifts`, `stack:positive-dual-square`, `stack:lattice` | ✓ |
| $\Theta$ per cell $m_{\rm cell}+\frac{e_j-e_{j+1}}2$; $\Theta=m+\Theta_0$; $b^+=m+b_0$ | `stack:cell-theta`, `stack:total-topology` | ✓ |
| $n_D=\frac{5m-n}8+\Theta_0-\frac{z+3+3b_0}8$ | `stack:dirac-growth`; Thm. `stack:nonzero` ($n=p_-+4q_0+p_+$, $m=q_0$) | ✓ |
| $8\kappa$ changes by $n+3m$ relative to the cap pairing; $8\kappa_{\rm closed}=z+3(1+b^+)$ | proof of `stack:nonzero`; proof of `caps:periods` | ✓ |
| $8\kappa\ge4s$ (negative pieces); $\kappa\ge\tfrac12$ on a positive piece | `stack:negative-test-cost`, `stack:positive-charge` | ✓ |
| $Q\le-2$, exception $Q\le2$ with $d_i=0$; $\lambda$ values | `indices:positive-square`, `indices:lambda-values`, `estimates:vertex-values` | ✓ (enumeration: maxima $R$: $-6,-4$; $S$: $2,-2$) |
| $8\kappa_i\ge4s_N+4m_i$; $q_i+4\ge\max(2s+L-7m,\,m+L-2s)$ | `indices:incidence-charge`, `indices:q-score` | ✓ |
| fixed segments $\ge-2$; $2a+6b+2\ge6$ | `indices:fixed-run`, `indices:fixed-exclusion` | ✓ |
| $i-p=6\kappa-3-m+\Delta-2s$; $e_{PU}\ge s-4m+r+\Delta+3\,\mathrm{miss}$; $3-2N\le-1$ | proof of `indices:mixed-run`, `indices:mixed-run-sharp`, `indices:mixed-exclusion` | ✓ |
| $\sum(q_i+4)=4$, $\sum i_i-2\eta=2-4k$, $\kappa_i=-v_i^2/4+\ell_i$ | `indices:virtual-sums`, `indices:ell` | ✓ |
| caps: no $R$, $v_W^2,K_W^2\le C_W$; $q+4\ge8$; $q\ge3L-7m+\dots$, $(5L-21)/4$ | `estimates:clamp`(ii), `estimates:cap-squares`, `indices:end-score`, `indices:end-lower` | ✓ |
| $L\ge4m-3+a+b$ | Cor. `stack:interior` | ✓ |
| $A\le S$, $3S-2A\ge S$; local excess $\ge-2a$ | `stack:composition`, `stack:macro-excess` | ✓ |
| $B=g_-g_+$, $f_+g_+\simeq1$ mod 2 | `negative:four-topology`, `ordinary:two-step-identity` | ✓ |

**Discrepancies and flags.** No numerical discrepancy was found in the manuscript. Points of slack, and corrections to our notes:
1. *Slack in the fixed-limit threshold.* `indices:fixed-run`'s threshold $-2$ could be $-3$. Its proof, `indices:end-exclusion` and `stack:composition` all hold at spacing $3$. Spacing $4$ is used only in `indices:mixed-run`, whose threshold $-2$ is exact and attained ($k=4$, $m=1$).
2. *Correction to notes T1 §3.4, Observation 5.* It applies the $k\ge2$ count at $k=1$ ("level bound grows like $+4$"). At $k=1$ the estimate behind that count is unavailable, and $-v^2/4$ is unbounded below (§4).
3. *Refinement of notes B4 §4.* "Spacing 2 fails: $(2,3,4)$ gives $-3$" is correct against the manuscript's $-2$. But $-3$ alone yields no broken limit; the first one not excluded is `PNPNP` ($-4$).
4. *Closed forms.* The mixed closed form $(k-4)m-k+2$ is a lower bound. It is attained for $k=3$ and $k=5$, and for odd $m$ at $k=4$ (bit parity); harmless.
5. *Unverified detail.* At $k=1$ I did not check that the actual-band parameters can be chosen compatibly along the shared intervals. The vertex test used by the manuscript holds regardless.

## 7. Computer checks (`round2/checks2/`)

- `lattice.py`: positive and negative cell data, characteristic $l$ with $l^2=4$, $\Theta$ per cell for all bit pairs, $\lambda_I$, $u\equiv\lambda$, $\Theta(W')=0$, $\Theta(W_H)=1$, $\sigma(W_H)=-2$, per-block $n_D$.
- `positive_square.py`: Lemma `indices:positive-square`, by exhaustive enumeration over $|x|\le14$, $|u|\le5$, $|t_b|\le4$, $|h|\le16$, both types and all bits. No violation.
- `segments.py`: exact minimisation of the energy of abelian classes on segments, enforcing parity, test incidence, chamber condition and end assignments. Output in `table_k5_m4.txt`.
- `periods.py`: least cost per period is exactly $4k-4$ for $k=2,\dots,5$, and unbounded below for $k=1$. Output in `periods_out.txt`.
- `explicit.py`: checks the configurations quoted in §4 (`PNPNP`, `PNNP`, `PNNPNNPNNP`, the $k=1$ family, the $k=2$ periodic class).
- `k1_search.py`, `k1_small.py`, `k1_band.py`: spacing-one periodic classes meeting every test, in the chamber (and in the actual band at some $(a,b)$), with Seiberg–Witten dimension $\ge0$ and $v^2\ge0$ per positive piece.
