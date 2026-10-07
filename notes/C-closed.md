# C — Can closed-manifold Donaldson theory replace the PU(2) step?

Inputs: digest; Secs. 4, 5, 6 (statements), 7 (clamp, period lemma, vertex test, cap constants), 8.
Labels: **[V]** checked (by hand, and by the small scripts in `agents/C-checks/`), **[P]** plausible, **[S]** speculative.
**†** marks a citation from memory whose exact form I could not check.

## 0. Conclusions

1. **[V]** The stack is a connected sum along the $J_i$:
   $X\cong Z_-\#(n{-}1{-}m)N_\phi\#\,mP\#Z_+$, with $P\cong \mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2$ up to diffeomorphism (independent of $K$) and $N_\phi\approx 2\overline{\mathbb{CP}}{}^2$ up to homeomorphism. Hence $D_X\equiv0$ and $SW_X\equiv0$, whether or not $\phi$ exists.
2. **[V]** $\Omega$ is not a closed invariant. It counts a problem of fixed-metric virtual dimension $-n$ over a cube whose faces are degenerations. It is a relative, *secondary* family invariant, equal to a Floer pairing $\langle y,\Phi x\rangle$. Its only closed-manifold content is $\Omega\equiv\pm D^w_{X'_k}(\text{probes})\pmod{2^N}$, where $X'_k$ is the cap closure of Sec. 4. That invariant is nonzero, and no vanishing theorem applies to it.
3. Rationally blowing down every $S_i$ gives a closed $X_B$ that is no longer visibly a connected sum. Its lattice and descent data match the manuscript's lifts exactly, and the $2^n$-bit sum is the Fintushel–Stern projection (**[V]** algebra, **[P]** identification). Even so:
   - $B$ has odd degree relative to every cobordism map of $W'_B$ **[V]**;
   - $D_{X_B}\equiv0$ **[P]**;
   - $H_*\circ(W'_B)_*$ is singular **[P]**.

   So there is no honest closed reformulation along these lines.
4. Each exclusion in Secs. 7–8 is a family/local form of a classical basic-class constraint (dictionary in §3). The closed shadow of Secs. 7–8 is a three-line lattice argument. It is vacuous here because there are no basic classes.
5. What Secs. 6–10 need is a **family (relative) SO(3)-monopole vanishing theorem with neck faces** plus emptiness of the family SW side. This is genuinely new. Its closed specialization (Feehan–Leness) is known but says nothing about $\Omega$.
6. **[P/S] Falsifiability test.** The argument appears to use $\phi$ only as a $b^+=0$ cobordism $Y_{-2}\to Y_2$ inducing a mod-2 isomorphism. If so, it would also forbid every negative-definite $V$ with that property (§4).

## 1. Topology of the stack (Task 1)

**1.1 Decomposition [V].** Write $W'_i=(-C_2)\cup_{J_i}C_{-2}$, where $J_i\cong S^3$ separates $X$. Cut along all $J_i$ and cap with balls. The summands are:

- $Z_-=C_-\cup_{Y_2}(-X_2(K))$ and $Z_+=X_{-2}(K)\cup_\phi C_+$;
- $N_\phi=X_{-2}(K)\cup_\phi(-X_2(K))$, with $n-1-m$ copies;
- $P=X_{-2}(K)\cup W_H\cup(-X_2(K))$, with $m$ copies and identity gluings.

$S_i=D_l\cup_K D_r$ is the union of the two handle cores, so it meets $J_i$ in $K$ and lies in no summand.

**1.2 The pieces.**

- **$\pi_1$ [V].** Traces are simply connected, and van Kampen over connected boundaries gives $\pi_1(N_\phi)=\pi_1(P)=1$. $Z_\pm$ are simply connected because $C_\pm$ are (Sec. 4). So $\pi_1(X)=1$.
- **$N_\phi$ [V].** $Q=\langle-1\rangle^2$, which contains $F_r=a+b$ and $F'_l=a-b$. Freedman, with $KS=0$, gives $N_\phi\approx2\overline{\mathbb{CP}}{}^2$. Its smooth type is unknown, and it has $b^+=0$, so it carries no Donaldson invariants.
- **$P$ [V].**
  - $X_{-2}(K)\cup W_H$ is the diagram $K^{-2}\cup\mu_1^{-1}\cup\dots\cup\mu_4^{-1}$. Blowing down the four $(-1)$-meridians gives $X_2(K)\#4\overline{\mathbb{CP}}{}^2$, compatibly with the slam-dunk identification of the boundary with $Y_2$.
  - Hence $P\cong D(X_2(K))\#4\overline{\mathbb{CP}}{}^2$. The double of a 0-handle plus a 2-handle is the boundary of a $D^3$-bundle over $S^2$, because knots in $S^4$ are trivial. That bundle is trivial when the framing is even, so $D(X_2(K))\cong S^2\times S^2$.
  - So $P\cong S^2\times S^2\#4\overline{\mathbb{CP}}{}^2\cong\mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2$, a toric rational surface for every $K$.
  - $Q_P=H\oplus4\langle-1\rangle$, with $G$ the doubled trace and $U$ the doubled cocore. This agrees with Prop. 5.1, and $b_2(W_H)=4$, $\sigma(W_H)=-2$.
- **$Z_\pm$ [V].** They are simply connected, have $b^+=b^+(C_\pm)>0$, and odd forms (because of $E_{\rm exc}$).
- **Totals.** $b^+(X)=m+b_0$ and $b^-(X)=b^-(Z_-)+b^-(Z_+)+2n+3m-2$. So $X\approx(m+b_0)\mathbb{CP}^2\#b^-(X)\,\overline{\mathbb{CP}}{}^2$.

**1.3 Vanishing [V].** $b^+(X)\ge2$. Donaldson's connected-sum theorem (Donaldson 1990; DK §9.3†) applies with $b^+>0$ on at least $m+2$ summands, so $D^w_X\equiv0$ for every $w$; likewise $SW_X\equiv0$. Independently, $X\cong X''\#\mathbb{CP}^2$ and contains essential spheres of square $0$ ($U$) and $+1$.

**1.4 What $\Omega$ is.**

- **(a) Dimension [V].** $D_I=n+z$, with $n$ parameters and $n$ degree-2 tests. At a fixed metric the problem has virtual dimension $-n$. So $\Omega$ is not $D_X$ of any insertion.
- **(b) Faces [V].**
  - $t_i=0$ is the long $J_i$-neck, i.e. the connected-sum degeneration. The manuscript kills these faces because a central contact costs 3. That is Donaldson's $SO(3)$-gluing-parameter argument run on a face.
  - $t_i=1$ splits $N_i=\nu S_i$ off along $L(4,1)$. These faces cancel between the two bits.
  - $\Omega$ is therefore invariant only under deformations that keep this face structure. It is an invariant of the decorated data $(X;J_i,\partial N_i;\text{sweeps},\text{caps})$, not of $X$.
- **(c) Closed families would not help [V].** $b^+(X)=m+b_0\approx n/4<n+1$, so generic $n$-parameter families meet reducibles, which have codimension $b^+$. Every loop of metrics bounds. A closed family invariant would need a nontrivial family of diffeomorphisms, and there is none here.
- **(d) Algebraic type [V given the manuscript's claims].**
  - Stretching the $Y$-seams gives $\Omega=\pm\langle y,\Phi x\rangle$, where $\Phi$ is a word in $\phi_*B$ and $H$.
  - $B$ is *secondary*. The fixed-metric operation "$\mu(S)\cdot[W']$" (an index-2 count) has two independent nullhomotopies: the $J$-split, via $C(S^3)=0$, and the lens split, via bit cancellation of the trace-zero, $\kappa=\tfrac14$ caps. The interval count is the cycle these two produce.
  - Its index is $i=1$ ($i+1+1-3=0$), whereas cobordism maps use $i=0$. It belongs to the same species as the quasi-isomorphisms in triangle proofs (Floer; Kronheimer–Mrowka–Ozsváth–Szabó; Culler–Daemi–Xie) and DLME's $g_1$.
  - Mod 2, $B\simeq g_-g_+\simeq f_-^{-1}f_+^{-1}=H^{-1}$ on homology.
- **(e) Closed content [V].**
  - $\Omega\equiv\pm q=\pm D^w_{X'_k}(\text{probes})\pmod{2^N}$, where $X'_k$ is the closure of Sec. 4 with $T^k$ inserted.
  - Every honest closed manifold assembled from $f_\pm,H,\phi$ with nonzero pairing is of this type, since $H\phi^{-1}=f_+Tf_+^{-1}$.
  - These invariants are nonzero (Kronheimer–Mrowka nonvanishing plus Cayley–Hamilton), and no vanishing theorem applies to them.

## 2. Closed reformulations (Task 2)

**2.1 Local model [V].** $\nu S=h_l\cup(\nu K\times I)\cup h_r$, so
$$W'=(E_K\times I)\cup_{T^2\times I}C_2,\qquad W'_B:=(E_K\times I)\cup B_2 .$$
$W'_B:Y_2\to Y_{-2}$ has $b^+=0$ and $b_2=1$, with $H_2\otimes\mathbb Q=\langle F_l+F_r\rangle$ of square $-4$.

$X_B$ is the stack with every $W'$ replaced by $W'_B$. Since $J_i\cap\nu S_i=\nu K$, the $J_i$ do not survive, and $X_B$ is not visibly a connected sum.

**2.2 Topology of $X_B$.**

- **$H_1$ [V].** The map $x\mapsto(x\cdot S_i)_i$ from $H_2(X)$ onto $\mathbb Z^n$ is surjective. By induction across cells: $Z_-$ supplies $e_1$; a negative cell supplies $(1,\pm1)$; a positive cell supplies $e_i$ and $e_{i+1}$ (from $T_b$ and $U$). This was also machine-checked on small stacks. So $H_1(X\setminus\cup\nu S_i)=0$, and Mayer–Vietoris gives $H_1(X_B)=0$.
- **$\pi_1$ [P].** $\pi_1(X_B)=1$ is plausible: the meridians die successively from the simply connected $C_+$ end.
- **Invariants [V].**
  - $b^+(X_B)=m+b_0$, $b^-(X_B)=b^-(X)-n$, $\sigma(X_B)=\sigma(X)+n$.
  - The lattice is the unimodular index-$2^n$ overlattice of $S^\perp$. It is odd, because $E_{\rm exc}\in S^\perp$, so it is $\cong(m+b_0)\langle1\rangle\oplus(b^-(X)-n)\langle-1\rangle$.

**2.3 Descent [V].**

- A spin$^c$ structure on $C_2$ with $c_1=K$ restricts to $L(4,1)$ according to $K\cdot S\bmod 8$.
- $B_2\simeq\mathbb{RP}^2$ has two spin$^c$ structures. They are conjugate, because $w_2(B_2)\neq0$.
- The example $\overline{\mathbb{CP}}{}^2=C_2\cup(\text{rational ball})$, a conic with $K=(2k+1)h$ and $K\cdot S\equiv\pm2\pmod 8$, shows these are the ones that extend.
- So **$K$ descends iff $K\cdot S\equiv2\pmod4$.**

In the manuscript $l\cdot S_i=\Lambda_0S_i-c_0S_i=2$, so the Dirac spin$^c$ structure $l$ descends. Also $c_e\cdot S_i\equiv0\pmod4$ and $c_e^2=\bar c^2-4|e|$, so all $2^n$ bits restrict to one class $\bar c$ on $X_B$.

**2.4 The bit sum is the FS projection.**

- **[V] Algebra.** In KM's convention $D^w=e^{Q/2}\sum(-1)^{(w^2+Kw)/2}a_Ke^K$, and $w\cdot S$ is even. Flipping $w\mapsto w+PD(S)$ multiplies each term by $(-1)^{K\cdot S/2}$. Hence
  $$\sum_e(-1)^{|e|}D^{\,w+\sum e_iS_i}_X=2^n e^{Q/2}\!\!\sum_{K\cdot S_i\equiv2\,(4)\ \forall i}\!\!(\cdots).$$
  With $|K\cdot S|\le4$ this keeps exactly $K\cdot S_i=\pm2$, i.e. the classes that descend.
- **[P] Identification.** By Fintushel–Stern these are $2^n$ times the coefficients of $D_{X_B}$.
- **[P] Gauge side.** The cancelled classes $K\cdot S\equiv0\pmod 4$ are exactly the trace states: $v\cdot S=\pm2$ gives $K\cdot S=\Lambda S\pm2\in\{0,\pm4\}$. The survivors are the central states. This is the same split the manuscript's lens-face cancellation makes, with $\varepsilon_1=-s\varepsilon_0$.

**2.5 Index test [V].**

- Excise and compare $C_2\cup(-B_2)=\overline{\mathbb{CP}}{}^2$ with $B_2\cup(-B_2)$. Both have $b_1=b^+=0$, so a bundle trivial on the swapped piece has the same index in either. The other $B_2$ sector, with $w_2=a^2\neq0$, shifts the index by $\pm2\pmod 8$.
- $B$ counts $i=1$, and every map of $W'_B$ counts $i=0$. So **$\deg B\not\equiv\deg(W'_B)_*\pmod 2$ in every bundle sector**: $B$ is not a rational-blowdown cobordism map.
- Globally the shift is $n$. The manuscript's choice $n\equiv0\pmod 8$ lets $D^{\bar c}_{X_B}$ live in the probe degree, with $\bar\kappa=\kappa-n/8$.
- On $X_B$, $\Theta$ is unchanged: $\bar\Lambda^2=\Lambda^2+n$ and $\sigma_B=\sigma+n$. Hence $n_D(X_B)=n_D(X)+n/8$.

**2.6 Value [P].**

- $SW_{X_B}(\bar k)=SW_X(k)=0$ by FS97 (the rational blowdown formula for SW invariants†). Then $D_{X_B}\equiv0$ follows from Witten's conjecture (Feehan–Leness, JEMS 2015†); $X_B$ is abundant, being odd, indefinite and of rank at least 3.
- So $\Omega=\pm D_{X_B}$ is false whenever $\Omega\ne0$, consistently with 2.5.
- **Corollary.** Apply the same argument to the $\phi$-free stack $C_-\cup(W'_BW_H)^k\cup C_+$, the blowdown of a connected sum. It gives $D=0$ for all $k\ge1$, while $\langle y,x\rangle=q\ne0$. Graded Cayley–Hamilton, as in Lemma 4.x, then shows **$H_*\circ(W'_B)_*$ is singular on $I(Y_2;\mathbb Q)$**. So $W'_B$ cannot replace $B$ even rationally, whereas $B\simeq H^{-1}\pmod 2$.

**2.7 Other honest cobordisms $Y_2\to Y_{-2}$.**

- $W'$ itself factors through $J$, so its map is zero **[V]**.
- $W'_B$: see 2.5–2.6.
- $-W_H$ read backwards has $b^+=3$. Whether its map is a unit is unknown, and no vanishing theorem is visible for the closed manifolds it produces **[S]**.

**Verdict:** no closed reformulation of $\Omega\ne0$ exists beyond 1.4(e).

## 3. Exclusion inequalities vs basic-class constraints (Task 3)

| Manuscript (family, local) | Classical counterpart | |
|---|---|---|
| Reference fillings with $\lvert K\cdot S_i\rvert\le4$; the Dirac index on $N$ is $0$ for $\lvert k(S)\rvert\le4$ and $-1$ at $\pm6$ (table, Prop. 8.x) | Adjunction for spheres of negative square, SW simple type, $b^+\ge2$: $\lvert K\cdot S\rvert\le-S^2=4$; at $K\cdot S=\pm4$ the reflected class $K\pm2PD(S)$ is also basic (FS95†). The table is exactly the local index behind this. The two $d=\pm4$ references in the manuscript are the reflection pair. | V table / P |
| Bit sum with lens-face cancellation | FS rational-blowdown projection onto $K\cdot S\equiv2\pmod 4$ (2.4) | V / P |
| Test cost: $v\cdot S_i\ne0$ (even) gives $-v^2\ge2$ per half; $v\cdot S_i=0$ forces a unit of $\ell$ | The localized contribution of a reducible stratum $\zeta=v$ carries $\prod_i\langle\zeta,S_i\rangle$, since $\mu(S_i)$ restricted to the link is $\propto(\zeta\cdot S_i)h$. At level $\ell\ge1$, point (bubble) terms can absorb $\mu(S_i)$. | P |
| Small-width test: the $S^2\times S^1$ tube in class $U$ forces $u=v\cdot U=0$ | Neck-stretching proof of adjunction for a square-zero $U$. For an essential sphere, SW vanishes identically. | V (same argument) |
| Period inequality $(vH)(KH)<0$ | Rewrites as $\Lambda\cdot H<K\cdot H<0$ (R type: $K\cdot H=\Lambda\cdot H$). This is $b^+=1$ SW wall-crossing with $s\ge0$: the psc chamber is empty, and solutions exist iff the perturbation path from $0$ to $\Lambda^+$ crosses the $K$-wall. R type is the Donaldson wall $v\cdot H=0$. | V |
| Vertex classes $H_I=U+\tfrac14\sum_{i\in I}X_i$; clamp at the vertices | $H_I$ is the projection of $U$ off $\{X_i\}_{i\in I}$, i.e. the class of $U$ after rationally blowing down those $X_i$, with $H_I^2=\lvert I\rvert/4$. The clamp is convexity of the wall-crossing condition over the period polygon $\mathrm{conv}\{H_I\}$. The lens face $a=\tfrac14$ is the period becoming orthogonal to $X_1$, the blowdown position. Also $\Lambda\cdot H_I<0$ for all $I\ne\varnothing$ and all bits. | V |
| Square estimate $Q\le-2$ on $P$ | Light-cone lemma in the $b^+=1$ lattice plus $w_2$-parity ($v_P^2$ is even, and two $t_b$ are odd). For R type, $v_P\cdot H=0$ gives $v_P^2\le-2$ outright; S type is a refined version. | V (R) / P (S) |
| Caps: no R; S has $v_W^2,K_W^2\le C_W$ | A generic period avoids walls (since $w\cdot A$ is odd); a priori bound and finiteness of basic classes | V / P |
| Large odd $\Lambda(E_{\rm exc})$ with $\lvert K(E_{\rm exc})\rvert\le B$ | Blowup formula: basic classes are $K\pm E$, so $\lvert v\cdot E\rvert\ge\lvert\Lambda\cdot E\rvert-1$ and the level $\ell$ becomes negative | P |
| $\sum(q_i+4)=4$, $\ell_i\ge0$, $d_s+p_i+4\ell_i\ge0$ | Feehan–Leness: a stratum $K$ contributes only if $\ell(K)=\kappa+(K-\Lambda)^2/4\in\mathbb Z_{\ge0}$; in simple type $K^2=2\chi+3\sigma$ | P† |

**Would-be classical theorem (closed shadow) [V arithmetic].** Let $Z$ be closed with the stack's lattice data, $b_1=0$ and $b^+\ge3$, and suppose $D^w_Z(\prod_i\mu(S_i)\,z)\neq0$.

1. **A basic class with $K\cdot S_i\ne0$.** By the KM structure theorem and polarization ($Q(S_i,\cdot)=0$ off the diagonal), there is a basic $K$ with $\prod_i K\cdot S_i\neq0$. So $K\cdot S_i\in\{\pm2,\pm4\}$, or $\pm2$ after the bit projection.
2. **$K\cdot U_j=0$.** Adjunction for $U_j$ forces $K\cdot U_j=0$; for a sphere $U_j$ there are in fact no basic classes at all.
3. **Upper bound on $K^2$.** Negative cells contribute at most $-2$ each (odd coefficients). Positive cells with $u=0$ contribute $-\sum t_b^2\le-4$. Hence $K^2\le-2n-2m+C$.
4. **Simple-type requirement.** Simple type requires $K^2=2\chi+3\sigma=2m-2n+C'$: $P$ contributes 4, $N$ contributes 2, and each neck subtracts 4.
5. **Contradiction for large $m$.** Steps 3 and 4 are incompatible once $4m>C-C'$.

This shadow needs neither the spacing nor $n_D$, and it is vacuous for the stack.

**Why the family version is harder.** In the family, simple type's $K^2=2\chi+3\sigma$ is replaced by $d_s(K)+p_i+4\ell_i\ge0$. That allows $K^2\ge2\chi+3\sigma-4p_i-16\ell_i$, with up to $n$ parameters. Also, the period of $P$ moves over a polygon instead of being fixed. The budget $\sum(q_i+4)=4$, the spacing $\ge4$, and the window $1/5<m/n\le1/4$ forced by $n_D>0$ are exactly what compensates. The window is tight and should be rechecked independently.

## 4. What would replace Secs. 6–10 (Task 4)

No closed-manifold theorem suffices:

- every closed manifold here that keeps the $J_i$ has $D\equiv0$ for trivial reasons;
- $X_B$ has $D\equiv0$ as well, and its Floer decomposition uses the wrong maps (§2);
- the only nonzero closed invariant is $D_{X'_k}$, and nothing forces it to vanish.

The needed statement is:

**(F) Family SO(3)-monopole vanishing with neck faces.** Let $g_t$, $t\in[0,1]^n$, be metrics with product necks along psc links at the faces ($S^3$ at $t_i=0$, $L(4,1)$ at $t_i=1$). Let $\Omega$ be the bit-summed family instanton count, with face terms vanishing or cancelling, and suppose $n_D>0$. Then $2^{n_D-1}\Omega$ equals the sum of family reducible contributions (S and R strata, including faces). In particular $\Omega=0$ if there are none.

**(E) Emptiness.** For the stack there are no S or R strata in the family (Secs. 6–8, i.e. the dictionary above).

**Status.**

- **(F)** For $n=0$ this is the Feehan–Leness cobordism formula (Mem. AMS 2018†, relying on their gluing theorem). The family relative version — with broken-metric faces, monopole lens-wall gluing, multisections, and "projection away from R" — is not in the literature to my knowledge. It is a plausible extension in spirit, but **genuinely new** as a theorem.
- **(E)** New. Each ingredient is a family version of a known constraint (§3), and the combination is new.

**Test [P/S].** (F) and (E) appear to use $\phi$ only through two facts:

- the cell lattice is negative definite (only upper bounds on $v^2$ and $\Lambda^2=\sigma$ on cells are used);
- $\phi_*$ is a mod-2 unit.

If that is right, the same argument would prove: *no negative-definite $V:Y_{-2}\to Y_2$ with $b_1=0$ induces an $\mathbb F_2$-isomorphism on $I$* (for $K$ where the caps exist). First check the manuscript for any other use of $\phi$. Then search for such a $V$. A known filter is the Heegaard Floer inequality $c_1^2+b_2\le4d(Y_2)-4d(Y_{-2})$†. A single example would refute Secs. 6–10.
