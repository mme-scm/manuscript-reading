# The 1/16 and the branched double cover

Line of attack: the branched double cover. Throughout, $K\subset S^3$ is a knot, $Y_r=S^3_r(K)$, $\Sigma=\Sigma_2(K)$, $\tau$ is the covering involution of $\Sigma$, and $\tilde K=\mathrm{Fix}(\tau)$ is the lift of $K$. Every claim carries one of three labels:

- **VERIFIED**: proved here, computed exactly, or checked against a source.
- **PLAUSIBLE**: supported by an argument with a gap that I have named.
- **SPECULATIVE**: heuristic.

The scripts are in `gap16/cover-code/`. The companion note `gap16/pillowcase-1.md` is cited as "the pillowcase note".

## 0. Summary

1. **The quotient picture (VERIFIED, topology).** Assume $\det K=1$; this holds whenever $\Delta_K=1$, so in the cosmetic case. Then:
   - The connected double cover of $Y_{\pm2}$ is the integer homology sphere $\tilde Y_{\pm2}=\Sigma_{\pm1}(\tilde K)$, and its deck involution is free.
   - The double cover of $W'=(-X^\circ_2)\cup_{S^3}X^\circ_{-2}$ branched along the sphere $S$ ($S\cdot S=-4$) is exactly DLME's composite cobordism $W^1_{-1}$ for the knot $\tilde K\subset\Sigma$.
   - Under this identification:
     - the $(-2)$-sphere $\tilde S$ maps to $S$;
     - $\mathbb{RP}^3=\partial\nu\tilde S$ covers $L(4,1)=\partial\nu S$;
     - DLME's two bundles $\hat c,\check c$ are the pullbacks of the two classes $F_l^*,F_r^*$, which are odd on $S$;
     - DLME's middle manifold $\Sigma$ covers the middle $S^3$, branched along $K$.

   DLME's entire triangle-detection configuration for $(\Sigma,\tilde K)$ is $\tau$-equivariant, and its quotient is the distance-four configuration on $W'$.
2. **Descent (VERIFIED on examples; PLAUSIBLE in general).**
   - Invariant irreducible flat connections on $\tilde Y_{\pm2}$ correspond to flat $SO(3)$ connections on $Y_{\pm2}$ with $w_2=0$ or with $w_2\neq0$. These are the two lifts of the involution.
   - Invariant irreducible flat connections on $\Sigma$ correspond to irreducible traceless representations of $\pi_1(S^3\setminus K)$, which carry order-two isotropy along $\tilde K$.
   - Chern–Simons values and energies double under pullback, while gradings add the index of the $\chi$-twisted operator. Hence
     $$\tilde c(p^*\alpha)=2c(\alpha)+\delta(\alpha)/8,\qquad \delta=i-i_\chi\in\mathbb Z,$$
     where $c=\widetilde{CS}-i/8$.
   - DLME's reducible of energy $1/8$ on the $(-2)$-disc bundle is the pullback of the reducible of energy $1/16$ on $\nu S$ in observation (i). It is also the pullback of a singular reducible of the same energy.
3. **Why the odd-on-$S$ family fails (PLAUSIBLE).**
   - The fixed part of DLME's family upstairs splits by the isotropy along $\tilde S$:
     - trivial isotropy gives nonsingular bundles on $W'$, odd on $S$; these are the family that was tried;
     - order-two isotropy gives singular connections along $S$ with holonomy parameter $1/4$.
   - The $L(4,1)$ wall of the nonsingular count can be cancelled only by the singular count, because the two descend from the two components of the stabiliser $O(2)$ at the $\mathbb{RP}^3$ wall.
   - The $S^3$ wall of the singular count runs through the traceless representations of $K$, which are exactly the fixed points of the middle term $I(\Sigma)$.

   So the obstruction observed downstairs is the $\tau$-quotient of the nonvanishing of DLME's middle term $I(\Sigma_2(K))$.
4. **Where a 1/16 can and cannot come from.**
   - (VERIFIED) Every cobordism or family map between the Floer complexes of $Y_{\pm2}$ shifts $c$ by an element of $\tfrac18\mathbb Z-E$. This holds for either bundle, for nonsingular connections, and for connections singular along $S$ with holonomy $1/4$, because $\chi(S)+S\cdot S/2=0$. So no such map produces a gap of exactly $1/16$.
   - (VERIFIED) DLME's $1/8$ is $\dim G/8$ for the one-parameter family of metrics; the $c^2$ terms cancel. The energy $1/8$ of the $\mathbb{RP}^3$ cap is a different $1/8$.
   - Under descent, the cap energy halves to $1/16$. The family term does not halve in the downstairs normalisation; it does halve in the normalisation $\tilde c/2$ inherited from the cover.
5. **The right statement.** Put $\tilde\ell(Y):=\tfrac12\,\ell(\tilde Y)$, half the $\ell$-invariant of the connected double cover. It is an oriented homeomorphism invariant of $Y_{\pm2}$, and a cosmetic diffeomorphism forces $\tilde\ell(Y_{-2})=\tilde\ell(Y_2)$. The inequality
   $$\tilde\ell(Y_{-2})\le\tilde\ell(Y_2)-\tfrac1{16}$$
   is exactly DLME's $\pm1$ inequality for $\tilde K\subset\Sigma$.
   - **Theorem 1** (VERIFIED as a deduction from DLME). The inequality holds whenever an $\ell$-minimising cycle of $\Sigma_{+1}(\tilde K)$ is killed at chain level by DLME's map $f_1$ to the middle term.
   - **Corollary 2** (VERIFIED). This happens when $\Sigma_{+1}(\tilde K)$ and $\Sigma$ have Floer complexes in opposite parities. That covers all positive torus knots $T(p,q)$ with $p,q$ odd.
   - **Proposition 3** (VERIFIED given a level hypothesis, which I checked numerically). The mirrors satisfy the inequality as well.
   - The constant $1/16$ cannot be improved: along $T(p,2p+1)$ the gap is $1/16+0.185/p+\dots$.
6. **DLME's own $\ell$ does not have the gap (VERIFIED).** This is confirmed independently of the pillowcase note: the enumeration is different, and it reproduces that note's values exactly. Along the same positive torus knots, $\ell(Y_2)-\ell(Y_{-2})$ is negative, tending to $-1/8$. Examples:

   | knot | $\ell(Y_2)-\ell(Y_{-2})$ | $\tilde\ell(Y_2)-\tilde\ell(Y_{-2})$ |
   |---|---|---|
   | $T(3,5)$ | $-21/1768$ | $659/3536$ |
   | $T(3,7)$ | $-141/3496$ | $\approx0.116$ |

   The reason is structural:
   - the descended maps always exchange the bundles, $(Y_2,w)\leftrightarrow(Y_{-2},0)$;
   - the anti-invariant index defect $\delta$ ranges widely, so $\ell$ and $\tilde\ell$ are minimised at different generators.
7. **Cosmetic case (VERIFIED as a deduction; the hypotheses are not checkable).** In the cosmetic case the parity mechanism cannot apply: exactness forces $f_1$ to have rank $\operatorname{rk}I(\Sigma)>0$. Proposition 4 gives a necessary condition for a cosmetic pair: unless $C(\pm\Sigma)$ has boundary depth at least $1/8$, the spectrum of $I(\pm\Sigma_2(K))$ must reach below the bottom of $I(\pm\Sigma_{+1}(\tilde K))$.

**Structural explanation proposed.** The $1/16$ is DLME's sharp $1/8$, the degree shift $\dim G/8$ of the one-parameter family, for $\pm1$ surgery on the lift $\tilde K\subset\Sigma_2(K)$, divided by the degree $2$ of the cover. Chern–Simons values and energies double under pullback, so the natural downstairs normalisation of the cover's filtration is $\tilde c/2$.

The three phenomena in the brief are the $\tau$-quotients of three features of DLME's distance-two picture for $(\Sigma_2(K),\tilde K)$:

| downstairs phenomenon | upstairs source |
|---|---|
| the $1/16$ | DLME's $1/8$ |
| the suggestion of a branched double cover | the cover itself |
| the obstruction from traceless representations | the nonvanishing of $I(\Sigma_2(K))$ |

The precise conjecture is Conjecture 5: $\tilde\ell(Y_{-2})\le\tilde\ell(Y_2)-1/16$ for every nontrivial $K$ with $\det K=1$. Combined with DLME Cor. 1.4, it would settle the cosmetic surgery conjecture.

---

## 1. Normalisations

**Manifolds and orientations.**
- For integer $r$, $Y_r$ is oriented as the boundary of the trace $X_r(K)$, and $Y_{-r}(K)=-Y_r(\bar K)$.
- $\Sigma=\Sigma_2(K)$ carries the orientation lifted from $S^3$. For the positive torus knot $T(p,q)$ with $p,q$ odd, $\Sigma=+\Sigma(2,p,q)$, the link of $x^2+y^p+z^q=0$.

**Chern–Simons values, energies and gradings** (DLME, `instanton.tex`):
- $\widetilde{CS}$ is the real lift with $\widetilde{CS}(\theta)=0$, in $SU(2)$ normalisation.
- The topological energy is $\mathcal E(A)=\tfrac1{8\pi^2}\int\operatorname{tr}F_0^2=-c^2/4+\widetilde{CS}(\text{in})-\widetilde{CS}(\text{out})$.
- $i(\alpha)$ is the index on $\mathbb R\times Y$ from $\alpha$ to $\theta$.
- $c(\alpha):=\widetilde{CS}(\alpha)-i(\alpha)/8$. It does not depend on the lift, since a lift changes $(\widetilde{CS},i)$ by $(1,8)$.
- The "$d/8$" in $\ell$ is this pairing of the $\mathbb Z$-lift $d$ of the $\mathbb Z/8$ grading with the real lift of CS.
- $\ell(Y)=\inf_d(\kappa(d)-d/8)$. For a perfect complex, $\ell=\min_\alpha c(\alpha)$.
- $c(-Y,\alpha)=\tfrac38-c(Y,\alpha)$, so for perfect complexes $\ell(-Y)=\tfrac38-\max c(Y)$.

**Twisted bundles on $Y_{\pm2}$.**
- $H^2(Y_{\pm2};\mathbb Z/2)=\mathbb Z/2$, so there is one nontrivial $SO(3)$ bundle $w$.
- Its Chern–Simons functional is defined modulo $\tfrac12$ in $SU(2)$ units, and its grading modulo 4.
- I normalise $c^w$ by the cap formula
  $$c(\alpha)=\tfrac38(1+b^+(W))+\tfrac18\bigl(\operatorname{ind}(A)-8\mathcal E(A)\bigr)\qquad(W:\emptyset\to Y,\ b_1(W)=0,\ A\ \text{any connection on any bundle, asymptotic to }\alpha).$$
- (VERIFIED by index additivity: on a closed manifold with $b_1=0$, $\operatorname{ind}-8\mathcal E+3(1+b^+)=0$, so the right side does not depend on the cap.)
- Through the APS theorem this gives $c=(3+\rho_{\rm ad})/16$ for every irreducible flat $SO(3)$ connection, whatever its $w_2$ (pillowcase note, Thm. 3.1).
- On the trivial bundle it agrees with DLME's $c$. Check: on $\Sigma(2,3,5)$ it gives $-7/60$ and $-13/60$, which are DLME's values (VERIFIED, `cover-code/sfs.py`).

**$SU(2)$ against $SO(3)$.** Every irreducible flat $SU(2)$ connection $\rho$ on $Y_{\pm2}$ has a twin $\chi\rho$, where $\chi$ is the central character. The twin has the same adjoint connection and the same $c$. So DLME's $\ell(Y_{\pm2})$ is the $\ell$ of the $SO(3)$ complex taken modulo $\chi$ (VERIFIED; see also the T5 notes, §2.2).

---

## 2. Topology

### 2.1 The lift of $K$ (VERIFIED, standard)

1. $|H_1(\Sigma)|=\det K=|\Delta_K(-1)|$. If $\Delta_K=1$, then $\Sigma$ is an integer homology sphere.
2. A Seifert surface $F$ lifts to two copies $F_1,F_2$ with $\partial F_i=\tilde K$, interchanged by $\tau$. So $\tilde K$ is null-homologous, and its Seifert framing $\tilde\lambda$ is a lift of $\lambda$.
3. On the boundary torus, the unbranched double cover $\tilde T\to T$ corresponds to the lattice $\{a\mu+b\lambda:\ a\ \text{even}\}$. Hence $\tilde\mu=2\mu$ and $\tilde\lambda=\lambda$, both lifted.
4. The infinite cyclic cover of $\Sigma\setminus\tilde K$ is that of $S^3\setminus K$, with deck group $2\mathbb Z$. Hence $\Delta_{\tilde K}(t^2)\doteq\Delta_K(t)\Delta_K(-t)$, and $\Delta_K=1$ gives $\Delta_{\tilde K}=1$.

### 2.2 Double covers of even surgeries (VERIFIED)

**Proposition 2.1.** Let $N$ be even. The connected double cover of $Y_N$ is $\tilde Y_N=\Sigma_{N/2}(\tilde K)$, with surgery measured against $\tilde\lambda$, and the deck involution is free. In particular, if $\det K=1$, then $\tilde Y_{\pm2}=\Sigma_{\pm1}(\tilde K)$ is an integer homology sphere.

*Proof.*
1. The curve $N\mu+\lambda$ has even $\mu$-coefficient, so it lifts to $\tilde T$. In the coordinates $(\tilde\mu,\tilde\lambda)$ it is $\tfrac N2\tilde\mu+\tilde\lambda$.
2. The core $\mu$ of the filling torus maps to $1\in\mathbb Z/2$. So the preimage of the filling torus is a single solid torus, the connected double cover, and its meridian is one lift of $N\mu+\lambda$.
3. The deck transformation translates $\tilde T$ by half of $\tilde\mu$:
   - on $\nu\tilde K$, whose meridian is $\tilde\mu$, this is a rotation of the disc with fixed core;
   - on the new solid torus, whose core is isotopic to $\tilde\mu$, it is a free rotation along the core.
4. Finally, $H_1(\Sigma_{\pm1}(\tilde K))=H_1(\Sigma)$ because $\tilde K$ is null-homologous. ∎

**Corollary 2.2.** An orientation-preserving diffeomorphism $\phi\colon Y_{-2}\to Y_2$ lifts to an orientation-preserving diffeomorphism $\tilde\phi\colon\Sigma_{-1}(\tilde K)\to\Sigma_{+1}(\tilde K)$ that commutes with the deck involutions.

*Proof.* $H^1(Y_{\pm2};\mathbb Z/2)=\mathbb Z/2$, so the connected double cover is unique, and the deck group is $\mathbb Z/2$. ∎

So a cosmetic pair $\pm2$ for $K$ gives a cosmetic pair $\pm1$ for $\tilde K\subset\Sigma$. Here $\tilde K$ is a knot with $\Delta_{\tilde K}=1$ in a homology sphere, and the pair is equivariant.

**Torus knots.** Let $K=T(p,q)$ with $p,q$ odd.
- $Y_N=M\bigl((p,b_1),(q,b_2),(pq-N,-1)\bigr)$ with $b_1q+b_2p=1$ and $e=N/(pq(pq-N))$.
- The double cover unwraps the fibres; the fibre maps to $pq\mu$, which is odd.
- So $\tilde Y_2=-\Sigma(p,q,pq-2)$ and $\tilde Y_{-2}=+\Sigma(p,q,pq+2)$, with $\tilde e=e/2$.
- The deck involution is the antipodal map on fibres. It is isotopic to the identity through the circle action.

(VERIFIED by computer: `cover.py` derives the Seifert invariants of the cover and checks them against the Brieskorn data for 14 cases. A Casson check also passes: $\lambda(\Sigma_{\pm1}(\tilde K))=\lambda(\Sigma)\pm\tfrac12\Delta''_{\tilde K}(1)$, which for $T(3,5)$ gives $-1\pm8\in\{7,-9\}$.)

### 2.3 The branched double cover of $W'$ (VERIFIED)

Let $W'=(-X^\circ_2)\cup_JX^\circ_{-2}$ with $J\cong S^3$.
- $H_2(W')$ has basis $F_l,F_r$ with form $\langle-2\rangle\oplus\langle-2\rangle$.
- $S=F_l-F_r$ is the union of the two cores, with $S\cdot S=-4$ and $S\cap J=K$.
- In the dual basis, $\mathrm{PD}(S)=(-2,2)$. It is even, and it vanishes in $H_2(W',\partial W';\mathbb Z/2)$. So the double cover branched along $S$ exists.
- It restricts to the connected double cover on each end, and to $\Sigma\to S^3$ on $J$.

**Proposition 2.3.** Let $p\colon\tilde W\to W'$ be the double cover branched along $S$. Then:

1. $\tilde W=(-\tilde X^\circ_2)\cup_\Sigma\tilde X^\circ_{-2}$, where $\tilde X^\circ_{\pm2}$ is the cobordism from $\Sigma$ to $\Sigma_{\pm1}(\tilde K)$ given by one 2-handle along $\tilde K$ with framing $\pm1$. This is DLME's $W^1_{-1}$ for $(Y,K)=(\Sigma,\tilde K)$.
2. $\mathrm{Fix}(\tau)=\tilde S$ is a sphere with $\tilde S\cdot\tilde S=-2$, and $\partial\nu\tilde S=\mathbb{RP}^3$ is DLME's $M^1_{-1}$. The covering $\mathbb{RP}^3\to L(4,1)=\partial\nu S$ is free.
3. DLME's piece $N$ ($\nu\tilde S$ minus two balls) covers $\nu S$ minus two orbifold balls. DLME's exterior $X=\overline{W^{-1}_{-2}}$ covers $W'\setminus\nu S$ freely; downstairs this is the cobordism $Y_2\to Y_{-2}$ with middle end $L(4,1)$.
4. The pieces of cohomology match as in the table below.

| | downstairs $W'$ | upstairs $\tilde W$ |
|---|---|---|
| intersection form on $F_l,F_r$ | $\operatorname{diag}(-2,-2)$ | $\operatorname{diag}(-1,-1)$ |
| self-intersection of the sphere | $S\cdot S=-4$ | $\tilde S\cdot\tilde S=-2$ |
| $\mathrm{PD}$ of the sphere | $(-2,2)$, even | $(-1,1)$, odd |
| classes $F_l^*,F_r^*$ | squares $-\tfrac12$, value $\pm1$ on $S$ | pullbacks $\tilde F_l^*,\tilde F_r^*$, squares $-1$ |
| restriction to the ends | $F_l^*\mapsto(w,0)$ on $(Y_2,Y_{-2})$; $F_r^*\mapsto(0,w)$ | $0$ |
| signature, Euler characteristic | $\sigma=-2$, $\chi=2$ | $\sigma=-2=2(-2)-\tfrac12(-4)$, $\chi=2=2\cdot2-\chi(S)$ |

   DLME's two bundles are $\hat c=p^*F_l^*$ and $\check c=p^*F_r^*$. Both have $c^2=-1$ and are odd on $\tilde S$, and $\hat c-\check c=-\mathrm{PD}(\tilde S)$.

*Proof.*
- The double cover of a 2-handle $D^2\times D^2$ branched along its core is $D^2\times D^2$, via $(x,z)\mapsto(x,z^2)$.
- The attaching framing $\lambda\pm2\mu$ lifts to $\tilde\lambda\pm\tilde\mu$ by §2.1.
- The fixed set is the union of the lifted cores, glued along $\tilde K$.
- $p$ maps each lifted core, and one lift $F_1$ of the Seifert surface, diffeomorphically onto its image. So $p_*\tilde F_\bullet=F_\bullet$ and $p^*F_\bullet^*=\tilde F_\bullet^*$.
- $\tau$ acts trivially on $H_2(\tilde W)$, because $F_1-F_2$ is null-homologous in $\Sigma$.
- The signature and Euler characteristic follow from the branched-cover formulas $\sigma(\tilde W)=2\sigma(W')-\tfrac12S\cdot S$ and $\chi(\tilde W)=2\chi(W')-\chi(S)$.
- DLME's $\hat c,\check c$ are the two classes of square $-1$ that agree on $X$ and differ on $N$ (`triangle-2.tex`, §5.2). ∎

### 2.4 Equivariance of DLME's whole configuration (VERIFIED, topology)

In DLME's model, $W^i_j$ is $[-a,a]\times E(\tilde K)$ with solid tori glued in at the slopes $+1$, $\infty$ and $-1$.
- $\tau$ acts on $E(\tilde K)$ as the deck transformation.
- It acts on the $\infty$ solid torus (the one in $\Sigma$) by rotating the disc, and on the $\pm1$ solid tori freely along the core.
- The $S^3$ middle ends are rotated about an unknot, and $\tau$ extends over the filling 4-balls.
- All the stretching hypersurfaces are $\tau$-invariant: $Z_i$, $M^i_{i-2}$ ($S^3$ or $\mathbb{RP}^3$) and $M^i_{i-3}\cong S^2\times S^1$, the last with free action.

So every family $G^i_j$ for $i-j\le3$ can be chosen $\tau$-invariant. The quotient configuration is the distance-four configuration on $W'$, with orbifold metrics of cone angle $\pi$ along $S$.

---

## 3. Flat connections and instantons under the cover

### 3.1 The free covers: two lifts of the involution (VERIFIED)

**Proposition 3.1.** Let $\det K=1$. Pullback induces a bijection
$$R^*(Y_{\pm2})/\chi\ \sqcup\ R^*_w(Y_{\pm2})/\chi\ \longrightarrow\ R^*(\tilde Y_{\pm2})^\tau,$$
from $SU(2)$ representations modulo $\chi$ and twisted ($w_2\ne0$) projective representations modulo $\chi$ to $\tau$-invariant irreducible flat connections upstairs.

*Proof.*
1. Let $\beta$ be invariant and irreducible. Its $SO(3)$ lift $\tilde\tau$ is unique, and $\tilde\tau^2=1$.
2. The $SU(2)$ lift of $\tilde\tau$ squares to $\pm1$.
   - If $+1$, $\beta$ descends to two $SU(2)$ connections $\rho$ and $\chi\rho$.
   - If $-1$, it descends to an $SO(3)$ connection with $w_2\ne0$.
3. Conversely, $p^*\rho$ is irreducible. If it were abelian, it would be trivial because $\tilde Y$ is a homology sphere, and then $\rho$ would factor through $\mathbb Z/2$. ∎

In pillowcase coordinates, a representation of the knot group with boundary holonomy $(\alpha,\beta)$ pulls back with
$$(\tilde\alpha,\tilde\beta)=(2\alpha,\beta)\ \text{(untwisted)}\qquad\text{or}\qquad(2\alpha+\tfrac12,\beta)\ \text{(twisted, after the character }\varepsilon\text{ of }\pi_1(E(\tilde K))\text{ with }\varepsilon(\tilde\mu)=-1\text{)}.$$
The surgery conditions $\pm\tilde\alpha+\tilde\beta\in\mathbb Z$ are then exactly $\pm2\alpha+\beta\in\mathbb Z$ and $\pm2\alpha+\beta\in\tfrac12+\mathbb Z$.

**Check (VERIFIED, `cover.py`).** For $T(p,q)$ with $p,q$ odd, all upstairs generators are invariant, since $\tau\simeq\mathrm{id}$. The explicit descent rule on Seifert rotation numbers is a bijection in all 14 cases. For example, for $T(3,5)$:
- $\#R^*(-\Sigma(3,5,13))=14=16/2+12/2$;
- $\#R^*(\Sigma(3,5,17))=18=16/2+20/2$.

### 3.2 The branched cover $\Sigma\to S^3$: isotropy and traceless representations (VERIFIED)

The isotropy of $\tilde\tau$ along $\tilde K$ is either trivial or a rotation by $\pi$.
- **Trivial isotropy.** The connection descends to a flat connection on $S^3$, so it is $\theta$.
- **Rotation by $\pi$.** It descends to an $SO(3)$ representation of $\pi_1(S^3\setminus K)$ with meridian of order two, that is, to a traceless $SU(2)$ representation. The correspondence is $\rho\mapsto\varepsilon\cdot\rho|_{\pi_1E(\tilde K)}$, and $\varepsilon(\tilde\mu)\rho(\mu)^2=(-1)(-1)=1$.

Consequences:
- The abelian traceless representation $\theta_K$ (meridian $\mapsto i$) pulls back to $\tilde\theta$ with the $\pi$-rotation lift.
- If $\det K=1$, there are no binary dihedral representations; there are $(\det K-1)/2$ of them (Klassen). Then
  $$R^*(\Sigma)^\tau\cong R^*(K;\mathbf i)/\chi,$$
  the irreducible traceless representations modulo $\chi$.
- So the fixed part of DLME's middle term $C(\Sigma)$ is the traceless singular instanton complex of $(S^3,K)$. Its reducible is $\theta_K$, as in Daemi–Scaduto's setting.

### 3.3 Chern–Simons values, energies and gradings (VERIFIED)

**Proposition 3.2.** For a flat connection $\alpha$ on $Y=Y_{\pm2}$ (either bundle) and its pullback $p^*\alpha$:
1. $\widetilde{CS}(p^*\alpha)=2\widetilde{CS}(\alpha)$. More generally, the energy of an invariant instanton upstairs is twice the orbifold energy downstairs.
2. $i(p^*\alpha)=i(\alpha)+i_\chi(\alpha)$, where $i_\chi$ is the index of the operator twisted by the real line bundle $\chi$ of the cover.
   - $H^0$ and $H^1$ of $Y$ with $\mathrm{ad}\,\theta\otimes\chi$ coefficients vanish, since $H^1(\tilde Y;\mathbb R)=0$. So $\theta$ is nondegenerate for the twisted operator as well.
3. Consequently
   $$\tilde c(p^*\alpha)=2c(\alpha)+\frac{\delta(\alpha)}8,\qquad \delta(\alpha)=i(\alpha)-i_\chi(\alpha)=\tfrac12\bigl(\rho^\chi_{\rm ad}(\alpha)-\rho_{\rm ad}(\alpha)-3\bigr)\in\mathbb Z,$$
   where $\rho^\chi_{\rm ad}=\eta(\mathrm{ad}\,\alpha\otimes\chi)-3\eta(\chi)$.
   - Equivalently, $\tilde c-c=\rho^\chi_{\rm ad}/16$, from $\eta_{\tilde Y}(p^*E)=\eta_Y(E)+\eta_Y(E\otimes\chi)$.

*Proof.* CS is multiplicative under finite covers, along the pulled-back path from $\tilde\theta$. The deformation complex of $p^*\alpha$ splits into $\pm1$ eigenspaces, and these are the deformation complexes of $\mathrm{ad}\,\alpha$ and of $\mathrm{ad}\,\alpha\otimes\chi$. The rest is substitution. ∎

**Check (VERIFIED, `compare.py`).** In every case computed, $\delta$ is an integer: $\tilde c$ and $c$ are computed from different Seifert data, so this is a strong test of the dictionary.
- $\delta$ is even on $Y_2$ and odd on $Y_{-2}$.
- Its values range from $-2$ to below $-300$.

So $\tilde c/2=c+\delta/16$ is far from $c+\text{const}$. Along an invariant instanton counted with downstairs index $i^+$ and anti-invariant index $i^-$,
$$\delta(\alpha')-\delta(\alpha)=i^--i^+ .$$
This is how the anti-invariant directions enter.

### 3.4 Reducibles on the disc bundles: $1/8\mapsto1/16$ (VERIFIED)

Let $\xi\in H^2(\nu S)$ with $\langle\xi,S\rangle=1$, so $\xi^2=1/(S\cdot S)=-\tfrac14$. Upstairs, $\tilde\xi=p^*\xi$ has $\tilde\xi^2=-\tfrac12$.

Energies of reducibles:

| where | connection | energy |
|---|---|---|
| upstairs $\nu\tilde S$ | $SO(3)$ reducible with $v=n\tilde\xi$ | $n^2/8$ |
| downstairs $\nu S$, trivial isotropy | nonsingular $SO(3)$ reducible with $v=n\xi$ | $n^2/16$ |
| downstairs $\nu S$, order-two isotropy | singular reducible, holonomy $-1$ on the adjoint line around $S$ | $n^2/16$; curvature class $(m+2)\xi$, $n=m+2$ |

- Each upstairs reducible has two equivariant lifts, acting by $\pm1$ on the fibres of the line over $\tilde S$; these give the second and third rows.
- The singular reducibles with $n$ even are KM's $SU(2)$ reducibles with holonomy $1/4$, of action $(j+1)^2/4$. Those with $n$ odd are $SO(3)$-singular.
- So DLME's cap $\hat A_N$ ($n=1$, energy $1/8$) has two descents of energy $1/16$:
  - the nonsingular one of observation (i), with $w_2$ odd on $S$;
  - a singular one.
- Both have framed index $0$, like DLME's cap. This is PLAUSIBLE: it follows if the upstairs cap is acyclic, since then both eigen-parts of its deformation complex are acyclic.
- It agrees with APS. The framed index is $8\mathcal E-1+\rho/2$ with $|\rho(L(4,1),k{=}1)|=1$. With the sign convention of the T5 notes (§3.3), the one that gives framed index $2$ for the energy-$\tfrac14$ cap, $\rho=+1$ here and the framed index is $\tfrac12-1+\tfrac12=0$.
- The restrictions to $L(4,1)$ are the flat connections with holonomy a rotation by $\mp\pi/2$, conjugate in $SO(3)$ by a perpendicular rotation by $\pi$.

### 3.5 The fixed part of DLME's family and its $\mathbb{RP}^3$ wall (PLAUSIBLE)

The isotropy of an invariant connection along the connected fixed sphere $\tilde S$ is constant. So the $\tau$-fixed part of each DLME count splits into two parts:
- **trivial isotropy:** nonsingular $SO(3)$ bundles on $W'$. By Proposition 2.3, $w_2=F_l^*$ for $\hat c$ and $w_2=F_r^*$ for $\check c$, and these are nontrivial on exactly one end;
- **order-two isotropy:** singular along $S$ with holonomy parameter $1/4$, the orbifold point of view of KM, `yaft_paper.tex` §2.

Two facts organise the walls.
- **Middle term.** The trivial-isotropy part has no irreducible fixed generators in the middle (only $\theta$ on $S^3$). The order-two part has middle term $R^*(K;\mathbf i)/\chi$.
- **$\mathbb{RP}^3$ wall.** At the $\mathbb{RP}^3$-broken metric the limit is the abelian flat connection with $w_2\neq0$. Its $SO(3)$ stabiliser is $O(2)$, which has two components. Gluing the exterior instanton to the unique minimal cap therefore produces two global bundles, $\hat c$ and $\check c$: this is the $SO(3)$ reason DLME's two walls coincide.
  - Equivariantly, the component of the gluing parameter decides whether the descended restrictions to $L(4,1)$ agree (rotation by $+\pi/2$ on both sides) or differ by the perpendicular rotation by $\pi$. That is, it decides whether the cap is the trivial-isotropy one or the order-two one.
  - Hence, for an invariant exterior instanton descending to $(W'\setminus\nu S,F_l^*)$, the trivial-isotropy wall of $\hat c$ equals the order-two wall of $\check c$. Symmetrically, for an exterior descending to $(W'\setminus\nu S,F_r^*)$, the trivial-isotropy wall of $\check c$ equals the order-two wall of $\hat c$.

The descended map therefore splits into two off-diagonal blocks:
$$g^{w\to0}=\hat g^{\rm triv}-\check g^{\rm ord2}\colon C^w(Y_2)\to C(Y_{-2}),\qquad g^{0\to w}=\check g^{\rm triv}-\hat g^{\rm ord2}\colon C(Y_2)\to C^w(Y_{-2}),$$
with $dg+gd=f_0^{\rm ord2}f_1^{\rm ord2}$ through the traceless complex.

**The gaps in this argument.**
- Equivariant gluing at the $O(2)$-stabilised wall.
- The reducible analysis of DLME §5.3 redone for orbifolds. In particular, breakings through $\theta_K$ must be handled with Daemi–Scaduto's $S^1$-equivariant framework.
- The cone-angle continuity between orbifold and smooth metrics for the nonsingular part.

**Parity check.** For the bundle $F_l^*$ the canonical degree of the descended family map is not the naive $\dim G-2c^2=2$. The topological energy relative to the twisted reducible $\theta^w$, which has $CS=\tfrac18$ on $Y_2$, is $\kappa\equiv0\pmod{\tfrac12}$, so $D\equiv8\kappa-i^+\equiv1\pmod4$. The map goes from even to odd degrees, matching the parities computed for torus knots, and it gives $i^-=0$ and $\delta'=\delta+1$, as observed (VERIFIED arithmetic).

### 3.6 Why the odd-on-$S$ family on $W'$ fails (PLAUSIBLE; the topology is VERIFIED)

The family that was tried is the trivial-isotropy count $\hat g^{\rm triv}$.
1. Its $S^3$ wall is harmless: only $\theta$ is flat on $S^3$.
2. Its $L(4,1)$ wall is the capped exterior map $(W'\setminus\nu S,F_l^*)\circ(\text{cap of energy }1/16)$. Nothing nonsingular cancels it:
   - (VERIFIED) $H^2(W';\mathbb Z/2)\to H^2(W'\setminus\nu S;\mathbb Z/2)$ is injective, since $\mathrm{PD}(S)$ is even. So there is exactly one nonsingular $SO(3)$ bundle extending the exterior.
   - The minimal odd cap is unique.
   - The two $U(2)$ lifts $c$ and $c+\mathrm{PD}(S)$ give identical $SO(3)$ moduli spaces.
3. The only cancelling partner is the order-two count $\check g^{\rm ord2}$, whose $S^3$ wall runs through the irreducible traceless representations of $K$.

So "the irreducibles on $(S^3,K)$" are forced, as the fixed points of DLME's middle term $I(\Sigma_2(K))$. Upstairs, DLME's $g_1$ for $(\Sigma,\tilde K)$ fails to be a chain map for the same reason.

---

## 4. Where a 1/16 can come from

### 4.1 Bookkeeping (VERIFIED)

**Lemma 4.1.** Let $W\colon Y\to Y'$ have $b_1(W)=0$ and rational homology sphere ends. Let the bundle be arbitrary, possibly singular along closed surfaces $F\subset\operatorname{int}W$ with holonomy parameter $1/4$. For an instanton $A$ of index $\operatorname{ind}(A)$ (for a family count, $-\dim G+\operatorname{codim}$) between irreducibles,
$$c(\alpha')-c(\alpha)=\tfrac38b^+(W)-\mathcal E(A)+\tfrac18\bigl(\operatorname{ind}A-s(F)\bigr),\qquad s(F)=\chi(F)+\tfrac12F\cdot F .$$

*Proof.*
- Glue a cap and use the cap formula of §1, together with additivity of index and energy; $h^0=0$ at irreducible limits.
- For the singular case, use KM's closed formulas: index $=8k+4l+\chi(F)-3(b^+-b^1+1)$ and action $k+2\lambda l-\lambda^2F\cdot F$ with $\lambda=\tfrac14$ (KM 0806.1053, `yaft_paper.tex` around l. 1410). These give $\operatorname{ind}-8\kappa+3(1+b^+)=s(F)$. ∎

For the sphere $S$, $s(S)=2-2=0$, and every surface in $W'$ has even square. Hence:
- every cobordism or family map between the complexes of $Y_{\pm2}$, for either bundle, nonsingular or singular along $S$, has $L-D/8\in\tfrac18\mathbb Z-\eta$;
- a gap of exactly $1/16$ cannot come from such a map, unless an a priori energy bound $\eta\equiv\tfrac1{16}\pmod{\tfrac18}$ is available;
- such a bound does exist at the $L(4,1)$-stretched metric (the odd caps cost $\ge\tfrac1{16}$). But there the map is the capped $W'$ map, which is null-homotopic.

**Remark.** In KM's theory, a $\tfrac1{16}\mathbb Z$ shift arises only from singular surfaces with $s(F)\in\tfrac12+\mathbb Z$, that is, of odd square. KM's monotonicity condition is exactly what makes $\operatorname{ind}-8\kappa$ topological.

### 4.2 Two different eighths (VERIFIED)

DLME's $g_1$ has degree $D=\dim G-2c^2=3$ and level $L=-c^2/4-\eta=\tfrac14-\eta$. So
$$L-\tfrac D8=-\tfrac{\dim G}8-\eta ,$$
and the $c^2$ terms cancel. The $1/8$ in DLME's inequality is the family dimension. The energy $1/8$ of the $\mathbb{RP}^3$ cap serves only to make the $\hat c$ and $\check c$ walls equal.

Under descent:
- the cap energy halves to $1/16$, because CS is multiplicative;
- the family term stays $1/8$ in the downstairs normalisation: a descended rigid invariant instanton with $i^+=-1$ lowers $c$ by $\mathcal E+\tfrac18$;
- but it lowers $\tilde c/2$ by $\mathcal E+\tfrac1{16}$ when $i^-=0$: upstairs, $\tilde c$ drops by $2\mathcal E+\tfrac18$.

So $1/16=\dim G/(8\deg p)$ in the normalisation inherited from the cover.

### 4.3 The halved invariant of the double cover

**Definition.** For a rational homology sphere $Y$ with $H_1(Y)=\mathbb Z/2$ whose connected double cover $\tilde Y$ is an integer homology sphere, put
$$\tilde\ell(Y)=\tfrac12\,\ell(\tilde Y)=\min_{\text{generators of }\tilde Y}\tfrac12\tilde c .$$
On $\tau$-invariant generators this equals $c+\delta/16$, minimised over both bundles at once.
- It is an invariant of $Y$ (VERIFIED: canonical cover, and DLME's invariance of $\ell$).
- By Corollary 2.2, a cosmetic $\pm2$ pair has $\tilde\ell(Y_{-2})=\tilde\ell(Y_2)$.

### 4.4 A pillowcase remark (VERIFIED arithmetic; the significance is SPECULATIVE)

The pillowcase note (Conj. 5.1, verified for torus knots) writes $c(Y_N,x)=\Phi(x)+(3\operatorname{sgn}N-N)/16+N(\alpha-\tfrac14)^2-\iota/8$. Applying the same formula to $\tilde K\subset\Sigma$, with $\tilde N=N/2$ and $\tilde\alpha=2\alpha$, and halving gives
$$\tfrac12\tilde c=\Phi_2+\frac{3\operatorname{sgn}N-N/2}{32}+N(\alpha-\tfrac18)^2-\tilde\iota/16,\qquad d\Phi_2=2(\alpha-\tfrac18)\,d\beta .$$
The slope constants of the two normalisations agree only at $|N|=2$:
$$(3-|N|)/16=(3-|N|/2)/32\iff|N|=2,$$
and the common value is $\pm\tfrac1{16}$. So at $\pm2$ surgery the downstairs filtration and the halved filtration of the cover place generators at the same offset $\pm\tfrac1{16}$ around their centres; the centres are $\alpha=\tfrac14$ and $\alpha=\tfrac18$ respectively. This plausibly explains why a $1/16$ is visible downstairs, and why it points to the cover.

---

## 5. Theorems and a conjecture

Throughout this section, $J$ is a knot in an integer homology sphere $Y$, and we use DLME's distance-two triangle-detection data for $(Y,J)$ over $\mathbb F_2$. DLME Prop. 3.10 is stated and proved for an arbitrary integer homology sphere $Y$. The data consist of chain maps $f_1=W_*\oplus(W,c)_*\colon C(Y_1)\to C(Y)\oplus C(Y)$ and $f_0$, together with $g_1$, which satisfies $dg_1+g_1d=f_0f_1$. The map
$$(f_1,g_1)\colon C(Y_1)\to\mathrm{Cone}(f_0)=C(Y)^{\oplus2}\oplus C(Y_{-1})[1]$$
is a quasi-isomorphism.

The degree $3$ and level $\tfrac14-\eta$ of $g_1$ are computed as in DLME Prop. 3.11. That computation uses only $b_1=b^+=0$ of $W^1_{-1}$, rational homology sphere ends, and $c^2=-1$. Here $\eta\ge0$; it is $>0$ if $\pi_1(W^1_{-1})=\pi_1(Y)/\langle\langle J\rangle\rangle$ is trivial. The components of $f_1$ and $f_0$ have $L-D/8\le-\eta_i\le0$ (DLME §3).

### 5.1 The kernel criterion

**Theorem 1 (VERIFIED as a deduction from DLME Props. 3.10–3.11).** Let $x$ be a cycle in $C_d(Y_1(J))$ at level $r$ with nonzero class and $r-d/8=\ell(Y_1(J))$. If $f_1(x)=0$ at the chain level, then
$$\ell(Y_{-1}(J))\le\ell(Y_1(J))-\tfrac18-\eta .$$
In particular, for $J=\tilde K\subset\Sigma_2(K)$ with $\det K=1$:
$$\tilde\ell(Y_{-2})\le\tilde\ell(Y_2)-\tfrac1{16}-\tfrac\eta2 .$$

*Proof.*
1. $(f_1,g_1)$ is a chain map to the cone. With $f_1x=0$, the cone cycle condition gives $dg_1x=g_1dx-f_0f_1x=0$.
2. So $g_1x$ is a cycle. Its image in $H(\mathrm{Cone})$ is the image of $[x]$ under the quasi-isomorphism, which is nonzero. Hence $[g_1x]\neq0$ in $H(Y_{-1})$.
3. $g_1x$ lies in degree $d+3$ at level $\le r+\tfrac14-\eta$. So $\kappa_{Y_{-1}}(d+3)\le r+\tfrac14-\eta$, and
   $$\ell(Y_{-1})\le r+\tfrac14-\eta-\tfrac{d+3}8=\ell(Y_1)-\tfrac18-\eta .$$
4. For $J=\tilde K$, use Proposition 2.1 and the definition of $\tilde\ell$. ∎

**Variant (VERIFIED).** It suffices that $f_1x=dy$ with the boundary depth $\beta=\mathrm{lev}(y)-\mathrm{lev}(f_1x)\le\eta_0+\eta_1$. Replace $g_1x$ by $g_1x-f_0y$. The degree shift $+1$ of $y$ supplies the $-\tfrac18$, and the conclusion becomes $\ell(Y_{-1})\le\ell(Y_1)-\tfrac18+\max(-\eta,\beta-\eta_0-\eta_1)$.

### 5.2 The parity case; positive torus knots

**Corollary 2 (VERIFIED).** Suppose $C(Y_1(J))$ is supported in even degrees and $C(Y)$ in odd degrees, or the other way round. Then:
- both complexes have zero differential, and $f_1=0$, since its components have even degrees $0$ and $2$;
- $g_1$ is an injective filtered chain map;
- Theorem 1 holds for every minimiser.

This applies to all positive torus knots $T(p,q)$ with $p,q$ odd. Here $C(\Sigma(2,p,q))$ is odd and $C(-\Sigma(p,q,pq-2))$ is even. (VERIFIED with Fintushel–Stern: DLME's $i=R_{FS}-3$ is odd on $+\Sigma$; `parity_check.py` checks eight Brieskorn spheres.) Hence
$$\ell\bigl(\Sigma(p,q,pq+2)\bigr)\le\ell\bigl(-\Sigma(p,q,pq-2)\bigr)-\tfrac18,\qquad \tilde\ell(Y_{-2}(T_{p,q}))\le\tilde\ell(Y_2(T_{p,q}))-\tfrac1{16}.$$

**Consistency (VERIFIED).** Exactness with $f_1=0$ forces
$$\operatorname{rk}I(\Sigma_{-1}(\tilde K))=\operatorname{rk}I(\Sigma_{+1}(\tilde K))+2\operatorname{rk}I(\Sigma(2,p,q)).$$
This holds for every $T(p,q)$ with $p,q$ odd, $p<q$, $p\le15$, $q\le29$ (`ranks.py`). For example, for $T(3,5)$: $18=14+2\cdot2$.

### 5.3 The mirrors

**Proposition 3 (VERIFIED as a deduction, under a level hypothesis that I checked numerically).** In the situation of Corollary 2:
1. $I(Y_{-1})=\operatorname{im}g_1\oplus\operatorname{im}f_0$, because $f_0$ is injective by exactness and $(0,g_1)$ is onto $\operatorname{coker}f_0$.
2. Hence, for perfect complexes,
   $$\max c(Y_{-1})\le\max\bigl(\max c(Y_1)-\tfrac18-\eta,\ \max c(Y)-\eta_0\bigr).$$
3. If $\max c(Y)\le\max c(Y_1)-\tfrac18$, then using $\ell(-Z)=\tfrac38-\max c(Z)$, the mirror knot satisfies $\tilde\ell(Y_{-2}(\bar K))\le\tilde\ell(Y_2(\bar K))-\tfrac1{16}$.

The hypothesis holds with a wide margin for all 26 torus knots tested (`mirror_check.py`). So both chiralities of every tested torus knot with $\det=1$ satisfy the $\tfrac1{16}$ gap for $\tilde\ell$.

### 5.4 The cosmetic case: what remains

**Proposition 4 (VERIFIED as a deduction).** Let $x$ realise $\ell(Y_1(J))$. Then one of the following holds.
- (i) $f_1[x]\neq0$, and then $\ell(Y)\le\ell(Y_1(J))-\min_i\eta_i$.
- (ii) $f_1[x]=0$, and then the variant of Theorem 1 applies.

**Corollary (necessary condition for a cosmetic pair).** Suppose $S^3_{\pm2}(K)$ are orientation-preservingly diffeomorphic. Then $\Delta_K=1$, $\Sigma=\Sigma_2(K)$ is a homology sphere, and $\ell(\Sigma_{-1}(\tilde K))=\ell(\Sigma_{+1}(\tilde K))$. Apply Proposition 4 to $K$, and to $\bar K$ (which is also cosmetic, with $\Sigma_2(\bar K)=-\Sigma$). If $C(\pm\Sigma)$ has boundary depth $<\tfrac18$, then
$$\ell(\Sigma)\le\ell(\Sigma_{+1}(\tilde K))\quad\text{and}\quad \ell(-\Sigma)\le\ell(-\Sigma_{+1}(\tilde K)).$$
In words, the spectrum of $I(\Sigma_2(K))$ must straddle the extreme bars of $I$ of the double cover of $Y_{\pm2}$.

**Why the parity mechanism cannot help here (VERIFIED).** In the cosmetic case the ranks of the two ends agree. Exactness then gives $\operatorname{rk}f_1=\operatorname{rk}f_0=\operatorname{rk}I(\Sigma)$. So $f_1\ne0$ unless $I(\Sigma)=0$. Also, Casson's formula with $\Delta_{\tilde K}=1$ gives $\lambda(\Sigma_{\pm1}(\tilde K))=\lambda(\Sigma)$. If $C(\Sigma)$ were odd and $C(\Sigma_{+1}(\tilde K))$ even, this would force $I(\Sigma_{+1}(\tilde K))=0$.

### 5.5 The conjecture

**Conjecture 5 (SPECULATIVE, about 40%).** For every nontrivial knot $K$ with $\det K=1$,
$$\ell(\Sigma_{-1}(\tilde K))\le\ell(\Sigma_{+1}(\tilde K))-\tfrac18,\qquad\text{equivalently}\qquad\tilde\ell(Y_{-2})\le\tilde\ell(Y_2)-\tfrac1{16},$$
and the constant is sharp.

Together with Corollary 2.2 and DLME Cor. 1.4, it implies the cosmetic surgery conjecture. This is modulo the nonvanishing of $I(\Sigma_{\pm1}(\tilde K))$, which follows from the triangle if $I(\Sigma)\neq0$.

Evidence:
- It is a theorem for positive torus knots (Corollary 2), and holds for their mirrors under a checked hypothesis (Proposition 3).
- It is sharp along $T(p,2p+1)$ (§6.3).
- It is literally DLME's theorem (in its form for a homology-sphere base) whenever the middle term does not see the minimiser (Theorem 1).

Against:
- For cosmetic candidates the middle term must see half of everything (§5.4).
- DLME's inequality fails for general knots in homology spheres, for example unknotted ones, though those are not lifts.

### 5.6 Eigenspaces of $\tau$ (SPECULATIVE)

Suppose the triangle-detection data can be made $\tau$-equivariant over $\mathbb Q$. This needs equivariant transversality, which generally fails, and DLME work over $\mathbb F_2$. Then the $\varepsilon$-eigenparts form a triangle, and $I(\Sigma)^\varepsilon=0$ gives the $\tfrac18$ inequality for the $\varepsilon$-parts of $I(\tilde Y_{\pm2})$.
- For torus knots, $\tau\simeq\mathrm{id}$, so all $(-)$-parts vanish and the statement is vacuous.
- For $\Delta_K=1$, localisation suggests that the graded trace of $\tau_*$ on $I(\Sigma_2(K))$ is a multiple of the Casson–Lin invariant $\sigma(K)/2=0$. I recall Collin–Saveliev's equivariant Casson invariant $\sigma(K)/8$ from memory and have not checked it.
- If so, one eigenspace can vanish only if $\lambda(\Sigma_2(K))=0$, i.e. only if $V_K'(-1)=0$ by Mullins' formula.

---

## 6. Computations (`gap16/cover-code/`)

### 6.1 Method and validation (VERIFIED)

**Formula.** $c=\bigl(3+3\operatorname{sgn}e-2\sum_is(l_i;a_i,b_i)\bigr)/16$ on $M((a_i,b_i))$, with $s(l;a,b)=\tfrac2a\sum_k\cot\tfrac{\pi k}a\cot\tfrac{\pi bk}a\sin^2\tfrac{\pi lk}a$. This is the orbifold formula of the pillowcase note. Generators are enumerated by Seifert rotation numbers and strict triangle inequalities. This enumeration is independent of the pillowcase note's arc enumeration. Exact values are recovered with denominator $16a_1a_2a_3$.

**Validations.**
- DLME's $\Sigma(2,3,5)$: $\{-7/60,-13/60\}$.
- The classical Fintushel–Stern values contain ours.
- The upstairs Seifert data derived in `cover.py` reproduce the Brieskorn multisets in all 14 cases.
- The descent rule is a bijection (Proposition 3.1).
- $\delta\in\mathbb Z$ for all generators.
- The rank identity (§5.2) holds.
- DLME's three proven inequalities hold (`dlme_check.py`).
- The pillowcase note's values are reproduced exactly: $T(2,3)$: $3/32$; $T(2,5)$: $1/32$; $T(2,7)$: $-1/192$; $T(3,4)$: $3/280$.
- All complexes are perfect:
  - $Y_2$ is even and $Y_{-2}$ odd, for both bundles;
  - $+\Sigma$ is odd and $-\Sigma$ even.

### 6.2 The three gaps for $T(p,q)$ with $p,q$ odd (VERIFIED; `tables.py`, `scan.py`)

Let $D=\ell(Y_2)-\ell(Y_{-2})$ (DLME's $\ell$), $D^w$ the same difference for the twisted bundle (formula normalisation), and $\tilde D=\tilde\ell(Y_2)-\tilde\ell(Y_{-2})$.

| $K$ | $D$ | $D^w$ | $\tilde D$ | mirror: $D$, $D^w$, $\tilde D$ |
|---|---|---|---|---|
| $T(3,5)$ | $-21/1768$ | $631/1768$ | $659/3536=0.1864$ | $0.1239,\ 0.0854,\ 0.1247$ |
| $T(3,7)$ | $-141/3496$ | $1279/3496$ | $0.1155$ | $0.1244,\ 0.1244,\ 0.1249$ |
| $T(5,7)$ | $-701/9768$ | $3631/9768$ | $0.1730$ | $0.1248,\ 0.1248,\ 0.1249$ |
| $T(3,11)$ | $-597/8680$ | $3223/8680$ | $3251/17360$ | $\approx\tfrac18$ (all three) |
| $T(5,11)$ | $-727/8056$ | $9031/24168$ | $0.0965$ | $\approx\tfrac18$ (all three) |
| $T(9,19)$ | $-0.1135$ | $0.3749$ | $0.0822$ | $\approx\tfrac18$ (all three) |

Over 32 knots with $pq<200$ (and their mirrors):
- $\min D=-0.115$;
- $\min D^w=0.0854$ (mirror of $T(3,5)$);
- $\min\tilde D=0.0822$ (at $T(9,19)$).

Hence:
- $\tilde D\ge\tfrac1{16}$ always, as the theorem requires;
- $D^w\ge\tfrac1{16}$ in all examples, consistent with the brief's claim for the nontrivial bundle;
- $D<0$ for every positive torus knot tested. The claim for DLME's $\ell$ fails, confirming the pillowcase note.

### 6.3 Sharpness (VERIFIED numerically; `family.py`, `dlme_sharp.py`)

Along $T(p,2p+1)$, for $p=3,5,\dots,39$, $\tilde D$ is

$$0.1155,\ 0.0965,\ 0.0875,\ 0.0822,\ 0.0788,\ 0.0764,\ \dots,\ 0.0672\ (p=39),$$

and $p(\tilde D-\tfrac1{16})\to0.185$. So $\tilde D\downarrow\tfrac1{16}$. On the cover this is DLME's own sharpness. For knots in $S^3$, $\ell(Y_1)-\ell(Y_{-1})$ is

| knot | $\ell(Y_1)-\ell(Y_{-1})$ |
|---|---|
| $T(5,11)$ | $0.1382$ |
| $T(11,23)$ | $0.12794$ |
| $T(21,43)$ | $0.12583$ |

and tends to $\tfrac18$. In both cases the minimisers approach $\ell(+1\text{ side})\to\tfrac12$ and $\ell(-1\text{ side})\to\tfrac38$.

### 6.4 The minimisers (VERIFIED; `minimizers.py`)

Along $T(p,2p+1)$:
- $\ell(Y_{\pm2})$ is realised by generators with $\delta=-2$ and $\delta=-3$, with $c\approx\tfrac12$ and $c\approx0.62$.
- $\tilde\ell(Y_{\pm2})$ is realised by entirely different generators:
  - on $Y_2$ a twisted one, and on $Y_{-2}$ an untwisted one;
  - with downstairs $c=(p^2-1)/8+\tfrac38$ up to $O(1/p)$, and $\delta=-2p^2$ on $Y_2$, $\delta=-2p^2-1$ on $Y_{-2}$ (exactly, for $p=3,\dots,13$). Then $\tfrac12\tilde c=c+\delta/16\to\tfrac14$ on $Y_2$.

So $\ell$ and $\tilde\ell$ are not comparable generator by generator. The halved filtration rewards generators far along the lifted path; heuristically $\delta\approx4(N\alpha+\beta)+\text{const}$ (SPECULATIVE).

---

## 7. Answers to the questions in the brief

1. **Lifts, isotropy and singular connections.**
   - Lifts: §3.1 (two lifts give $w=0$ and $w\neq0$).
   - Isotropy: §3.2 and §3.5. Trivial isotropy gives nonsingular bundles odd on $S$; order-two isotropy gives singular connections with parameter $1/4$ along $S$, and traceless representations along $K$.
2. **Halving.** Chern–Simons values and energies halve exactly (Proposition 3.2). Gradings do not: $\tilde c=2c+\delta/8$.
3. **How DLME's $1/8$ descends.** It descends to $1/16$ in $\tilde\ell$ (§4.2, Theorem 1). The cap's $1/8$ descends to the $1/16$ cap, but that is not the source of the gap.
4. **What goes wrong.**
   - (a) The middle term $I(\Sigma_2(K))$. Its fixed part is the traceless complex of $K$, and for cosmetic candidates it must interact with half of everything (§5.4).
   - (b) Downstairs, all descended maps exchange bundles, $(Y_2,w)\leftrightarrow(Y_{-2},0)$. So the same-bundle difference $\ell(Y_2)-\ell(Y_{-2})$ is contaminated by the offset $\ell^w(Y)-\ell(Y)$, which is about $0.2$ on $Y_2$ for the torus knots computed.
   - (c) The anti-invariant index enters through $\delta$, and equivariant transversality fails in general.
5. **Is $\ell(Y_{\pm2})$ comparable with an equivariant $\ell$ upstairs?** No, beyond $\tilde c\equiv2c\pmod{\tfrac18}$. The minimisers differ (§6.4).
6. **The right equivariant statement.** It is the statement for $\tilde\ell$: Theorem 1, Corollary 2, Proposition 3 and Conjecture 5. Localisation does not remove the middle term, because the fixed points of $I(\Sigma)$ are the traceless representations, which are nonempty for nontrivial $K$ by Kronheimer–Mrowka.

---

## 8. Conclusion

**Structural explanation.** Pull everything back to the connected double cover.
- $Y_{\pm2}$ becomes $\pm1$ surgery on the lift $\tilde K\subset\Sigma_2(K)$, and $W'$ branched along $S$ becomes DLME's distance-two cobordism.
- There, DLME's one-parameter family produces a gap of $\dim G/8=1/8$ between the $\pm1$ surgeries, whenever the middle term $I(\Sigma_2(K))$ does not intervene.
- Chern–Simons values and energies double under the cover. Downstairs, the gap is therefore $1/16$ in the halved invariant $\tilde\ell=\ell(\tilde Y)/2$.
- No cobordism or family map downstairs can produce $1/16$, since all of them shift $c$ by $\tfrac18\mathbb Z-\mathcal E$. This is why "no factor of $1/16$ appears in the index formulas".
- The same quotient sends DLME's $1/8$ cap to the $1/16$ cap. It sends DLME's middle term to the traceless representations of $K$, which obstruct the odd-on-$S$ family.

**Precise statements and status.**

| statement | status | confidence |
|---|---|---|
| (A) Proposition 2.1, Corollary 2.2, Proposition 2.3: covers, lifts, $W'$ branched along $S$ equals DLME's $W^1_{-1}$, $\hat c,\check c=p^*F_{l,r}^*$ | VERIFIED | 97% |
| (B) Propositions 3.1–3.2: two lifts, traceless fixed points, $\tilde c=2c+\delta/8$ with $\delta\in\mathbb Z$, $1/8\mapsto1/16$ caps | VERIFIED (numerically on 14 cases; formally) | 92% |
| (C) §3.5–3.6: isotropy decomposition of DLME's fixed part, wall pairing, why the odd-on-$S$ family must meet the traceless representations | PLAUSIBLE | 70% |
| (D) Lemma 4.1: $\tfrac18\mathbb Z$ bookkeeping, including singular along $S$ | VERIFIED | 90% |
| (E) Theorem 1 and Corollary 2: $\tilde\ell(Y_{-2})\le\tilde\ell(Y_2)-\tfrac1{16}-\tfrac\eta2$ when the minimiser dies under $f_1$, hence for all positive $T(p,q)$ with $p,q$ odd; Proposition 3 for their mirrors | VERIFIED as deductions from DLME Props. 3.10–3.11 for a homology-sphere base, plus a numerically checked hypothesis for mirrors | 85% |
| (F) Sharpness of $1/16$ along $T(p,2p+1)$ | VERIFIED numerically | 90% |
| (G) The gap fails for DLME's $\ell$ (positive torus knots) | VERIFIED, conditional on the orbifold $c$-formula, which was validated in six independent ways | 92% |
| (H) Proposition 4 and its corollary (necessary condition for a cosmetic pair) | VERIFIED as deduction | 85% |
| (I) Conjecture 5: $\tilde\ell(Y_{-2})\le\tilde\ell(Y_2)-\tfrac1{16}$ for all nontrivial $\det$-one $K$; would settle the cosmetic surgery conjecture | SPECULATIVE | 40% |

**Overall.** The $1/16$ is a halved $1/8$. The mechanism is DLME's family on the double cover, and the obstruction is $I(\Sigma_2(K))$. Confidence in this explanation: about 75%. The open problem is reduced to one point: show that the bottom bar of $I(\Sigma_{+1}(\tilde K))$ is not seen by DLME's map $f_1$ into $I(\Sigma_2(K))$, or exploit $\tau$ to that end.

---

### Scripts (`gap16/cover-code/`)

| script | what it does |
|---|---|
| `sfs.py` | Seifert enumeration, orbifold $c$-formula with exact recovery, classical Fintushel–Stern cross-check |
| `cover.py` | Seifert data of the double cover, descent of untwisted and twisted representations, bijection check |
| `compare.py` | $\delta=8(\tilde c-2c)$ integrality; cross-check with the pillowcase note's enumeration; parities |
| `scan.py`, `tables.py`, `mixed.py` | gap tables |
| `family.py`, `dlme_sharp.py` | sharpness |
| `minimizers.py` | minimising generators |
| `ranks.py` | rank identity of the triangle |
| `parity_check.py` | Brieskorn parities |
| `mirror_check.py` | level hypothesis for mirrors |
| `dlme_check.py` | DLME's inequalities |

KM source used for the singular index and action formulas: `gap16/src-km0806/x/yaft_paper.tex`.
