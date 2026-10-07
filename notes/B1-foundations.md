# B1. Foundations of spin-filtered IP-modules

Labels: **[V]** I checked it (by hand, or by script in `agents/B1-checks/`). **[P]** plausible. **[S]** speculative.
Literature is cited from memory; bibliographic details are unverified.
Scripts: `agents/B1-checks/eta.py` (η-invariants), `agents/B1-checks/levels_b1.py` (lattices and levels).

## 0. Verdict

1. **The formal layer is sound [V].** $\rho_t$, $\sigma_t=\mathrm{CS}-\rho_t$, $\ell_t$, the periodicity, the end labels on $Y_{\pm2}$, the levels and the monotonicity lemma are all well defined. They are computable in examples (§4), and they reproduce the manuscript's numerology $n_D=\tfrac{5m-n}8+$const exactly.
2. **The feared formal obstructions do not occur [V].**
   - $\phi^*$ *does* swap the two spin$^c$ structures, relative to their trace labels, and it is forced to (Lemma 2.1).
   - But homogeneity of $B$ forces exactly the same alternation (Lemma 2.2). So $B$ and $\phi$ compose to a self-map of $(Y_2,t_0)$, and the period returns to the same $t$.
   - Periodicity is fine ($\sigma_t\mapsto\sigma_t+1$, $\mathrm{gr}\mapsto\mathrm{gr}+8$).
   - $n_D$ of a matrix entry is topological. It depends on $(W,c,\mathfrak s)$ and the lifted ends, and on nothing else.
3. **Structural surprise [V].** $\sigma_t$ takes values in a single coset $s_t+\mathbb Z$, where $s_t\equiv-d(Y,t)\pmod{2}$. So the "spin filtration" is really an integer grading $j=8\sigma_t-\mathrm{gr}$, in which CS cancels: $j$ is a pure $\eta$-invariant quantity. Hence $\ell_t\in s_t+\tfrac18\mathbb Z$ is a Frøyshov/$d$-type invariant. Strict inequalities therefore come for free from discreteness, so no analogue of DLME's $\eta>0$ is needed.
4. **All the content sits in the monotonicity hypotheses, and per-map monotonicity is false.**
   - Given round 1's $HB\simeq\mathrm{id}$ (mod 2), at least one of $\partial_{Y_{\pm2}}$, $B$, $H(\mathfrak s_0)$ has a nonzero entry carried by instantons with $n_D\ge1$. This holds for *every* nontrivial $K$ (Cor. 3.9) [V, formal].
   - $\Theta(W_H)$ is not determined by the end data: it is a $\mathbb Z$-torsor of values $1-k$ (Lemma 2.4). So "monotonicity of $H$" is a Seiberg–Witten chamber statement about a chosen $\mathfrak s$, not a topological fact.
   - Floer's differential on $Y_{\pm2}$ need not respect $\sigma_t$. Under the cosmetic hypothesis $Y_{\pm2}$ is not an L-space, so a $\mathrm{PU}(2)$ Floer complex of $Y_{\pm2}$ has Seiberg–Witten-type critical points, and nothing available forces cylinder monotonicity [P].
5. **Verdict.**
   - *As a presentation*, the spin-filtered DLME language is accurate and recommended: "the manuscript iterates a spin-level-lowering block of slope $(k-5)/8$". Confidence about 85%.
   - *As an independent Floer-theoretic proof route*, with $I^t_\bullet(Y_2)$ and a block-monotonicity theorem with cylindrical $Y_2$ ends, it is **not plausible with existing technology**. Confidence that such a proof can be completed without in effect redoing the manuscript's closed-stack localization: about 10–15%.
   - The decisive input in either form is a relative $\mathrm{PU}(2)$ localization for a block containing $k\in\{2,3,4\}$ copies of $B$, which needs $\phi$. The closed stack exists precisely to keep the $Y_{\pm2}$ seams finite, so that the 3D Seiberg–Witten points never appear as limits.
   - The theory must also run over $\mathbb Q$, not over $\mathbb F_2$, because localization gives $2^{n_D-1}\cdot\#=\dots$ (Remark 3.11). This is why an *integral* $B$ is needed.

## 1. The APS formula

**Setting.**
- $W\colon Y\to Y'$ with $\partial W=-Y\sqcup Y'$, where $Y,Y'$ are rational homology spheres, with cylindrical ends and product metrics there.
- $E$ is a $U(2)$ bundle with $c=c_1(E)$ and a fixed determinant connection that is flat on the ends.
- $c|_Y=c|_{Y'}=0$. This holds at every rational seam of the stack (Lemma stack:lifts), so $E|_Y$ is trivial and the flats $\alpha$ are $SU(2)$, possibly holonomy-perturbed.
- $\mathfrak s$ is a spin$^c$ structure with $l=c_1(\mathfrak s)$, and its connection $B$ is flat on the ends. Put $\Lambda=l+c$.
- Squares are rational relative squares, $\Theta=(\Lambda^2-\sigma(W))/4$, and $D_A\colon W^+\otimes E\to W^-\otimes E$.
- On $\mathbb R\times Y$ write $D^+=\partial_t+D_Y$.

**Weight convention ($\mathcal W_\delta$).** Conjugate by $e^{\delta t}$, where $t$ is a global time function. Equivalently, every end gets the boundary operator $D_Y-\delta$, with $0<\delta\ll1$: sections decay at outgoing ends and may grow at rate at most $\delta$ at incoming ends.

**Definition 1.0.** For a critical point $\alpha$ on $(Y,g,t)$,
$$\rho_t(\alpha):=\tfrac12\big(\eta(D_{\alpha,t})-h(D_{\alpha,t})\big)+\tfrac14\,\eta_{\rm sign}(Y),$$
where $D_{\alpha,t}$ is the spin$^c$ Dirac operator of $(Y,g,t,B|_Y)$ twisted by $\alpha$ on $S_t\otimes\mathbb C^2$, $h=\dim\ker$, and $\eta_{\rm sign}$ is the odd-signature $\eta$ (rank 2 gives the factor $2\cdot\tfrac18$). Set $\sigma_t:=\widetilde{\mathrm{CS}}-\rho_t$, with DLME's lift $\widetilde{\mathrm{CS}}(\theta)=0$.

**Proposition 1.1 [V].** In $\mathcal W_\delta$,
$$n_D(A):=\operatorname{ind}_{\mathbb C}D_A=\Theta-\mathcal E(A)+\rho_t(\alpha)-\rho_{t'}(\alpha'),\qquad \mathcal E(A)=-\tfrac{c^2}{4}+\widetilde{\mathrm{CS}}(\alpha)-\widetilde{\mathrm{CS}}(\alpha').$$
Equivalently, $n_D(A)=\Theta+\tfrac{c^2}4-\sigma_t(\alpha)+\sigma_{t'}(\alpha')$. No spin$^c$ Chern–Simons term is needed.

*Proof.*
1. APS gives $\operatorname{ind}=\int_W[\mathrm{ch}(E)e^{l/2}\hat A]_4-\tfrac12(\eta+h)(\text{outgoing op})-\tfrac12(\eta+h)(\text{incoming op})$. The boundary operators are $D_{Y'}-\delta$ and $-(D_Y-\delta)$.
2. For small $\delta$: $\eta(D-\delta)=\eta(D)-h$ and $\eta(-D+\delta)=-\eta(D)+h$, while both shifted operators have $h=0$.
3. The integrand is $\tfrac14\Lambda_{\rm form}^2-\tfrac1{12}p_1-(c_2-\tfrac14c_1^2)_{\rm form}$.
4. $\int\Lambda_{\rm form}^2=\Lambda^2$ exactly. The connections are flat at the ends, $H^1(Y)=0$ makes them gauge-unique, and $L^{\otimes N}$ is flat-trivial at the ends, so $\int=(\text{integral relative square})/N^2$.
5. $\tfrac13\int p_1=\sigma+\eta_{\rm sign}(Y')-\eta_{\rm sign}(Y)$ (APS signature theorem), and $\int(c_2-c^2/4)=\mathcal E(A)$, as in DLME's (3.2).
6. Collecting terms gives the formula. $\square$

*Remarks.*
- With "decay at all ends" (the manuscript's fixed-limit convention) one gets $n_D-h(\alpha')$ instead, which is not additive. This is harmless at the psc cuts $S^3$ and $L(4,1)$, where $h=0$, but a Floer theory on $Y_{\pm2}$ must use $\mathcal W_\delta$.
- The overall sign convention is pinned down by three independent checks in §4.

**Proposition 1.2 (gluing; closed case) [V].**
- In $\mathcal W_\delta$, $n_D$ is exactly additive under gluing along $(Y',\alpha')$: $D_{Y'}-\delta$ is invertible, and $\Theta$, $c^2$, $\mathcal E$ are additive across rational homology spheres (Novikov), so the $\rho$ terms telescope.
- On a closed $X$, $n_D=\Theta-\kappa$, which is Lemma indices:closed.
- A cut at $J=S^3$ costs nothing, since round $\rho(\theta)=0$.

**Proposition 1.3 (integrality, gauge) [V].**
- (a) For any path $A$ on $\mathbb R\times Y$, $n_D(A)=\sigma_t(\beta)-\sigma_t(\alpha)\in\mathbb Z$. Hence $\sigma_t$ takes values in $s_t+\mathbb Z$, where $s_t:=\sigma_t(\theta)=-\rho_t(\theta)=-2n(Y,t,g)$ and $n=\tfrac12(\eta(D_t)-h)+\tfrac18\eta_{\rm sign}$ is the Kronheimer–Mrowka/Frøyshov spectral correction.
- (b) $s_t\equiv-d(Y,t)\pmod{2\mathbb Z}$. *Proof:* filling $(Y,t)$ by $(W,\mathfrak s)$ gives $n\equiv(c_1^2-\sigma)/8\pmod{\mathbb Z}$, and $(c_1^2-\sigma)/4\equiv d\pmod 2$. Equality holds for the elliptic examples in §4.
- (c) A degree-one gauge change sends $\widetilde{\mathrm{CS}}\mapsto\widetilde{\mathrm{CS}}+1$ and $\mathrm{gr}\mapsto\mathrm{gr}+8$, and leaves $\rho_t$ unchanged. So $j:=8\sigma_t-\mathrm{gr}\in 8s_t+\mathbb Z$ is gauge invariant, and $\sigma_t-\mathrm{gr}/8=j/8$ is the correct combination.
- (d) CS cancels in $j$: $j(\beta)-j(\alpha)=8n_D+\operatorname{ind}_{\rm ASD}$, and the integrand $8(\Theta-\kappa)+8\kappa-3(1+b^+)$ is charge-free. So $j$ is an APS $\rho$-invariant of the flat connection, combining $8D_{\alpha,t}$ with the ASD boundary operator of $\mathrm{ad}\,\alpha$.

**Proposition 1.4 (degenerate cases) [V].**
- Along a family $\rho_t$ jumps only by integers. With the $(\eta-h)$ convention, a zero mode moving to $+$ raises $\rho_t$ by 1, and one moving to $-$ changes nothing.
- Since $\sigma_t$ is continuous off these jumps and lies in a discrete coset, small holonomy perturbations give *exactly* $\sigma_t(\alpha_\pi)\in\{\sigma_t(\alpha)-h(\alpha),\dots,\sigma_t(\alpha)\}$, and $\sigma_t(\alpha_\pi)=\sigma_t(\alpha)$ if $D_{\alpha,t}$ is invertible. This replaces DLME's $|\mathrm{CS}(\alpha_\pi)-\mathrm{CS}(\alpha)|<\epsilon$.
- A change of metric shifts $\sigma_t(\alpha)$ by an $\alpha$-dependent spectral flow in $\mathbb Z$. So $\ell_t$ is an invariant of $(Y,g,\pi)$ only, unless continuation maps are spin-monotone. A cyclic argument does not need invariance: use one $(Y_2,g,\pi)$ throughout and $\phi^*g$ on $Y_{-2}$.

## 2. Spin$^c$ bookkeeping on $Y_{\pm2}$ and $Y_0$

$\mathrm{Spin}^c(Y_{\pm2})$ is in bijection with $\mathrm{Spin}(Y_{\pm2})$ and has two elements; both have $c_1=0$ and both are self-conjugate. Let $t_0$ be the restriction of the spin structure of the trace $X_{\pm2}(K)$, i.e. $k\cdot F\equiv0\pmod 4$, and let $t_1$ be the other one, $k\cdot F\equiv2\pmod 4$.

**Lemma 2.1 ($\phi$ swaps the labels) [V].** For every orientation-preserving $\phi\colon Y_{-2}\to Y_2$, $\phi^*t_a(Y_2)=t_{1-a}(Y_{-2})$.
- *Proof.* $N_\phi=X_{-2}\cup_\phi(-X_2)$ has $H_1=0$ and the odd form $\langle-1\rangle^2$ (Prop. stack:lattice: the unique integral overlattice of $\mathrm{diag}(-2,-2)$). If $\phi$ preserved $t_0$, the two trace spin structures would glue to a spin structure on $N_\phi$, which is impossible. $\square$
- *Cross-checks.* (i) $d$-invariants: for the unknot, $\phi\colon\partial D_{-2}\to\partial D_2$ sends $d=\tfrac14$ to $d=\tfrac14$, so it swaps labels. (ii) The manuscript's $l$ has $l\cdot F_r=-2$ and $l\cdot F'_l=0$ on every cell, so the labels differ across every seam.

**Lemma 2.2 ($B$ forces the same alternation) [V, script].**
- On $W'$, give $l$ the end labels $(a,b)$. The two lifts $c_e=e\,\mathrm{PD}(S)$ have equal $\Theta$ iff $\Lambda_0\cdot S=\pm2$, and this forces $b=1-a$.
- The maximum is then $\Theta(B)=0$, at $\Lambda_0=(0,-2)$ (the manuscript's choice) or $(2,0)$.
- With $b=a$ there is no homogeneous choice, and the best inhomogeneous shift (DLME Lemma 2.6 type) is $5/8$.
- Hence in the stack $B\colon(Y_2,t_0)\to(Y_{-2},t_1)$, $\phi\colon(Y_{-2},t_1)\to(Y_2,t_0)$ and $H\colon(Y_{-2},t_1)\to(Y_2,t_0)$. The period $P_k=H\circ B\circ(\phi\circ B)^{k-1}$ is an endomorphism of $(Y_2,t_0)$. Index $\ell$ as $\ell_{t_a}(Y_2)$ and $\ell_{t_{1-a}}(Y_{-2})$; then $\phi$ gives $\ell_{t_a}(Y_2)=\ell_{t_{1-a}}(Y_{-2})$.

**Proposition 2.3 ($\chi$-involution) [V for the $\rho$/CS identities; P for the chain level].**
- Let $\chi$ be the order-2 flat line. Then $t_1=t_0\otimes\chi$ and $D_{\alpha,t_1}=D_{\alpha\otimes\chi,t_0}$, so $\rho_{t_1}(\alpha)=\rho_{t_0}(\alpha\otimes\chi)$.
- $\mathrm{CS}(\alpha\otimes\chi)-\mathrm{CS}(\alpha)$ is locally constant (the adjoint connection is unchanged), and it equals $\mathrm{CS}(\theta')=\tfrac12$ mod 1.
- With $\chi$-invariant perturbations, $\alpha\mapsto\alpha\otimes\chi$ is a chain isomorphism (Floer's $H^1(Y;\mathbb Z/2)$-action). Hence $\ell_{t_1}(Y)=\ell_{t_0}(Y)+c_\chi(Y)$, a constant shift, so the choice of $a$ is immaterial.
- §4 verifies the $\rho$-identity numerically on $S^3/O^*=Y_{-2}(\mathrm{LHT})$.

**Lemma 2.4 ($Y_0$ inside $H$) [V].**
- Since $l\cdot A$ is even and $c\cdot A$ is odd, $\Lambda|_{Y_0}$ is non-torsion. So on $(Y_0,w)$ the twisted Dirac operator always has non-flat central coupling.
- $\sigma$ on $Y_0$ is defined only relatively. Its absolute normalization moves by $(\Lambda\cdot A)k$ under the $H^1(Y_0;\mathbb Z)$-action on central connections.
- The spin$^c$ structures on $W_H$ with the fixed end labels form a $\mathbb Z$-torsor $\mathfrak s_k=\mathfrak s_0+2k\,\mathrm{PD}(F_0)$, where $F_0$ is the middle 0-trace class (the $Y_0$ direction, with $F_0^2=0$ and $F_0\perp F_r,F'_l$). Then $\Lambda_k^2=\Lambda_0^2+4k\,\Lambda_0\cdot F_0=-4k$ and $\Theta(W_H,\mathfrak s_k)=1-k$, unbounded above.
- The manuscript takes $k=0$. Nothing topological forces this; the choice is made in the reducible exclusion (the clamp's background values).
- **Rule:** never cut at $Y_0$. Treat $W_H$ as a single cobordism and do not define $\ell_t(Y_0)$. Note also that 3D Seiberg–Witten points with $|K\cdot A|=2$ exist on $Y_0$ [P: $HF^+(Y_0,\mathfrak s_{\pm1})\neq0$ for $g=2$].

## 3. Definitions and the formal monotonicity lemma

**Definition 3.1.**
- The input is $(Y,t,g,\pi)$ with $Y=Y_{\pm2}$ (only central reducibles) and DLME-admissible Floer data. $C_*(Y;R)$ is Floer's irreducible complex on lifts $\tilde\alpha\in\widetilde{\mathcal B}$, with $R\in\{\mathbb Q,\mathbb F_2\}$.
- The data are **spin-monotone** if $\langle\partial\tilde\alpha,\tilde\beta\rangle\ne0$ implies $\sigma_t(\tilde\beta)\le\sigma_t(\tilde\alpha)$. Equivalently, the counted trajectories have $n_D\le0$, or again $j(\beta)\le j(\alpha)+1$. Since $j(\beta)=j(\alpha)+1+8n_D$, a violation means $n_D\ge1$.

**Definition 3.2.**
- $F_rC_d:=\langle\tilde\alpha:\mathrm{gr}=d,\ \sigma_t\le r\rangle$ and $F_rI^t_d(Y):=H_d(F_rC)$.
- The periodicity map $\varphi$ is the deck shift.

**Lemma 3.3 [V].** If the data are spin-monotone, $I^t_\bullet(Y)$ is an IP-module (DLME Def. 2.3) whose jumps lie in $s_t+\mathbb Z$.
- *Proof.* Each degree has finitely many lifts. The deck shift raises $\sigma_t$ by 1 and $\mathrm{gr}$ by 8, which gives axioms (a) and (b). $\square$

**Definition 3.4.** $\kappa^\sigma(d)$ and $\ell_t(Y):=\inf_d(\kappa^\sigma(d)-d/8)$, exactly as in DLME's Definition 2.4.

**Proposition 3.5 [V].** $\ell_t(Y)=\tfrac18\min_{0\ne x\in I(Y)}\ \min_{z\in x}\ \max_{\alpha\in\mathrm{supp}\,z}j(\alpha)\in s_t+\tfrac18\mathbb Z$. It is finite iff $I(Y;R)\neq0$.
- *Proof.* A cycle is homogeneous in $\mathrm{gr}$, and $\sigma_t-\mathrm{gr}/8=j/8$ is gauge invariant. $\square$

**Definition 3.6.**
- The input is a cobordism $(W,c,\mathfrak s)$ with QHS ends, a compact family $G$ of dimension $g$, and an insertion of real codimension $v$. This includes $b^+>0$, provided the map is a chain map, e.g. $H=f_+f_-$.
- The count of $A$ with $\operatorname{ind}A+g-v=0$ defines $f$, of degree $D=-2c^2-3b^++g-v$ and formal spin level $L_\sigma=-c^2/4-\Theta(\mathfrak s)$.
- $f$ is **spin-monotone** if every counted $A$ has $n_D(A)\le0$.

**Lemma 3.7 (monotonicity, family/insertion version) [V].** Suppose both ends and $f$ are spin-monotone. Then $f$ is an IP-morphism $I^t_\bullet(Y)\to I^{t'}_\bullet(Y')$ of degree $D$ and level $L_\sigma$. If $f_\infty$ is injective, then
$$\ell_{t'}(Y')\le\ell_t(Y)+(L_\sigma-D/8),$$
and the min-max $j$ moves by at most $8L_\sigma-D\in\mathbb Z$.
- *Proof.* By Prop. 1.1, $n_D(A)\le0$ is equivalent to $\sigma_{t'}(\alpha')\le\sigma_t(\alpha)+L_\sigma$, so $F_r\mapsto F_{r+L_\sigma}$. Deck shifts commute with $f$. Then apply DLME Lemma 2.5(b), or Lemma 2.6 for sums over determinant lifts with different $\Theta$.
- The family and the insertion change only $D$; $n_D$ does not see $G$ or the cut.
- $L_\sigma-D/8$ is additive under composition and gluing along rational homology spheres. $\square$
- Because of discreteness, "shift $<0$" means a drop of at least $1/8$, so no analogue of $\eta(W)>0$ is needed.

**Table 3.8 (recomputed from Prop. 1.1, Lemmas 2.2 and 2.4) [V, `levels_b1.py`].**

| map | $c^2$ | $b^+$ | $g$ | $v$ | $\Theta$ | $D$ | $L_\sigma-D/8$ | brief |
|---|---|---|---|---|---|---|---|---|
| $B$, either lift | $0$ / $-4$ | 0 | 1 | 2 | 0 (maximum, forced labels) | $-1$ / $7$ | $+1/8$ | $+1/8$ ✓ |
| $H(\mathfrak s_k)$ | 0 | 1 | 0 | 0 | $1-k$ | $-3$ | $k-5/8$ | $-5/8$ at $k=0$ ✓ |
| DLME $g_1$ | $-1$ | 0 | 1 | 0 | $\tfrac14$ for $l=(-1,-1)$; otherwise $\le-\tfrac34$ | 3 | $-3/8$ | $-1/8$ ✗ |
| period ($k$ copies of $B$, one $H(\mathfrak s_0)$) | | | | | | | $(k-5)/8$ | ✓ |

- **Discrepancy at $g_1$.** On $\mathrm{diag}(-1,-1)$ with $c=(1,0)$ (not even), $\Theta\in\tfrac14+\mathbb Z$, and the two lifts agree iff $\Lambda\cdot S=1$. So $\Theta=0$ is impossible. The spin shift of $g_1$ is $-3/8$, i.e. $-\tfrac18-\Theta$ with $\Theta$ playing $\eta$'s role. This is more favourable than the brief's $-1/8$. The CS column ($-\tfrac18-\eta$) is unaffected.
- The closed-stack identity $n_D(X)=-\sum(L_\sigma-D/8)+\text{const}=\tfrac{5m-n}8+\text{const}$ checks [V].

**Corollary 3.9 (per-map no-go) [V, formal; inputs: round 1's $HB\simeq\mathrm{id}$ mod 2, and $I(Y_2)\neq0$].**
- If $\partial_{Y_{\pm2}}$ and $B$ are spin-monotone, then $H(\mathfrak s_k)$ can be spin-monotone only for $k\ge1$. *Proof:* $HB$ is injective with shift $k-\tfrac12$, and $\ell_t$ is finite.
- Hence, for every nontrivial $K$, some entry of $\partial_{Y_{\pm2}}$, $B$ or $H(\mathfrak s_0)$ is carried by instantons with $n_D\ge1$.
- Any per-map-monotone package has period shift at least $(k+3)/8>0$, which is unfavourable.

**Proposition 3.10 (block form of the contradiction) [V, formal].** Assume:
- (a) $(Y_2,t_0,g,\pi)$ is spin-monotone over $\mathbb Q$;
- (b) for some $k\le4$, the period $P_k$ (the count on the glued $W_{P_k}$ with its product family) is spin-monotone at its formal level;
- (c) $P_k$ is injective on $I(Y_2;\mathbb Q)$. This holds because every factor is integral with odd determinant on $L=I(Y_2;\mathbb Z)/\mathrm{Tor}$.

Then $\ell\le\ell+(k-5)/8<\ell$, a contradiction. Hypothesis (b) is refuted for $k=1$ (Cor. 3.9), so it must use $k\ge2$, and hence $\phi$.

**Remark 3.11 (coefficients) [V, logic].** $\mathrm{PU}(2)$ localization yields $2^{n_D-1}\cdot\#=(\text{reducible and face terms})$. This kills counts over $\mathbb Z$ or $\mathbb Q$, but over $\mathbb F_2$ it says nothing once $n_D\ge2$. DLME's $\mathbb F_2$ framework must therefore be lifted to $\mathbb Q$, which needs integral $B$ and $H$. This matches the manuscript.

## 4. Sanity computations [V]

All computations use round metrics, so $h=0$ by psc. $\eta$ comes from the holomorphic Lefschetz / Donnelly formula $\eta(D_V)=\tfrac{2}{|\Gamma|}\sum_{g\ne1}\chi_V(g^{-1})/\det_{\mathbb C}(1-g)$ on links of $\mathbb C^2/\Gamma$.

| $Y$ | data | result |
|---|---|---|
| $S^3$ | — | $\rho(\theta)=0$, so $s=0=-d$ |
| $\mathbb{RP}^3=\partial D_{-2}$ | $\eta(D_{t_0})=\tfrac14$, $\eta(D_{t_1})=-\tfrac14$, $\eta_{\rm sign}=0$ | $\sigma_{t_0}(\theta)=-\tfrac14$, $\sigma_{t_1}(\theta)=\tfrac14$ ($=-d$). $\sigma_{t_0}(\theta')=\widetilde{\mathrm{CS}}(\theta')+\tfrac14$, which is integral relative to $\sigma_{t_0}(\theta)$ iff $\mathrm{CS}(\theta')\equiv\tfrac12$ ✓ |
| $L(4,1)=\partial D_{-4}$ | $\eta_{\rm sign}=-\tfrac12$; $n_k=(1-k^2/4)/8$ for $k\in\{-2,0,2,4\}$ | For $\Lambda S=2$: $\rho(\pm1)=0$ and $\rho(\text{trace})=n_0+n_4=-\tfrac14$. This reproduces the lens table "$-\kappa_N$, $-\kappa_N$, $\tfrac14-\kappa_N$" of Prop. indices:lens-index, by a method independent of $\mathbb F_4$ vs $\mathbb P(1,1,4)$ |
| $\Sigma(2,3,5)=\partial(-E_8)$ | $\eta(D)=\tfrac{1079}{720}$, $\eta_{\rm sign}=\tfrac{361}{180}$; $\rho(\theta)=2=d$; $\rho(V_1)=\tfrac{121}{120}$, $\rho(V_2)=\tfrac{49}{120}$ | With DLME's CS values: $\sigma(\alpha)=\tfrac1{120}-\tfrac{121}{120}=-1$ and $\sigma(\beta)=0$. Both are integers, as Prop. 1.3 predicts; the wrong pairing gives non-integers, which identifies $V_1\leftrightarrow\alpha$. The differential is 0, so the complex is spin-monotone. $j(\alpha)=-9$, $j(\beta)=-5$, so $\ell_t=-\tfrac98$, attained at $\alpha$. DLME's $\ell=-\tfrac{13}{60}$ is attained at $\beta$: the two filtrations rank the generators differently |
| $S^3/O^*=\partial(-E_7)=Y_{-2}(\mathrm{LHT})$ | $\rho_{t_0}$: $\theta=\tfrac74$, $\theta'=\tfrac14$, $\alpha=\tfrac{37}{48}$, $\alpha\otimes\chi=\tfrac{13}{48}$. $\rho_{t_1}$ is the same list with $\theta\leftrightarrow\theta'$ and $\alpha\leftrightarrow\alpha\otimes\chi$ | $s_{t_0}=-\tfrac74$ and $s_{t_1}=-\tfrac14$ ($=-d$). Integrality forces $\mathrm{CS}(\alpha)\equiv\tfrac1{48}$ and $\mathrm{CS}(\alpha\otimes\chi)\equiv\tfrac1{48}+\tfrac12$, consistent with Prop. 2.3 and the pattern $\mathrm{CS}=1/|\Gamma|$ |

These are the requested sanity cases: all values are finite and explicitly computable, and the integrality of $\sigma$ is a nontrivial check of the conventions. For general $K$, $\rho_t$ on $Y_{\pm2}(K)$ is a real number that depends on $g$; it is computable numerically, but not in closed form. Modulo $2\mathbb Z$, $s_t=-d(Y_{\pm2},t)$. The cyclic argument needs no explicit values.

**Does $n_D(\text{entry})$ depend only on the endpoints and $W$?** Yes [V], in the following sense:
- It depends on $(W,c,\mathfrak s)$ and the *lifted* ends, with their $g$ and $\pi$. It does not depend on the family parameter, the insertion or the solution.
- Three caveats:
  1. $\mathfrak s$ is extra data; on $W_H$ it is a $\mathbb Z$-torsor (Lemma 2.4).
  2. The weight convention matters at Dirac-degenerate ends (use $\mathcal W_\delta$).
  3. The end values $\sigma$ depend on $(g,\pi)$ through integers (Prop. 1.4).

## 5. Obstructions, decisive points, and what is new

- **O1 (the differential) [P].** Cylinder monotonicity (Def. 3.1) has no mechanism behind it, since Weitzenböck gives no sign. Seifert examples cannot test it, because their differentials vanish. Under the cosmetic hypothesis, Ni–Wu give $\tau(K)=0$, so $K$ is not an L-space knot and $Y_{\pm2}$ is not an L-space. Then $HM_{\rm red}\ne0$, so 3D Seiberg–Witten points exist in some $t\otimes L$, and these are critical points of any $\mathrm{PU}(2)$ Floer complex of $Y_{\pm2}$.
- **O2 (per map) [V, formal].** Cor. 3.9.
- **O3 (blocks) [P].** Block monotonicity is a relative $\mathrm{PU}(2)$ localization on $W_{P_k}$ with cylindrical $Y_2$ ends, so O1's Seiberg–Witten limits enter. The manuscript's finite seams avoid this. The two forms are equivalent in content, and the closed form is technically easier.
- **O4 (choice of $\mathfrak s$) [V].** The favourable $H$ level depends on $k=0$ in Lemma 2.4. Monotonicity must fail for $k\ll0$, so it is a chamber condition. It is supplied, if at all, by the reducible exclusion (other threads).
- **Not obstructions [V].** $\phi$'s swap of labels (Lemmas 2.1 and 2.2), periodicity, the topological nature of $n_D$, perturbation control (Prop. 1.4), and $Y_0$ (Lemma 2.4: never cut there).

**What is new, minimally [P].**
1. The integer-valued grading $j=8(\mathrm{CS}-\rho_t)-\mathrm{gr}$ on instanton generators, normalized by the Kronheimer–Mrowka correction $n(Y,t,g)$. With it, $\ell_t$ is a $d$-type invariant on instanton homology. It resembles Frøyshov's $h$ and the $u$-adic level of equivariant theories.
2. A block-monotonicity / relative localization theorem for $W_{P_k}$, $k\in\{2,3,4\}$.

Everything else is DLME §2 verbatim.

**Decisive next steps.**
- (i) Test O1 on a 3-manifold with nonzero Floer differential, e.g. surgery on a hyperbolic knot, by computing $j$ for its flats.
- (ii) Test Cor. 3.9 on $K=$ trefoil. $Y_{-2}(\mathrm{LHT})=S^3/O^*$ is elliptic, so the $\rho$ values are already computed above. Determine which of $B$, $H(\mathfrak s_0)$ carries $n_D\ge1$ entries; this needs the $\mathrm{SL}_2$ side $Y_{2}(\mathrm{LHT})$.
- (iii) Any proof must state the block localization theorem with hypotheses on $\mathfrak s$ and $k$. That is where its confidence should be judged.
