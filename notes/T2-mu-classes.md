# T2. Donaldson's $\mu(S)$ in the negative interval map

Labels: **[V]** checked by hand, or by `agents/T2-checks/checks.py` (lattice facts, cap energies, Grothendieck strata, crossing counts). **[P]** plausible. **[S]** speculative. **†** marks a citation from memory whose details I could not check. Manuscript labels refer to `src/*.tex`.

## 0. Verdict

1. **$x(S)=\varepsilon\,\mu(S)$ [V].** The manuscript's insertion asks that the normalized holonomy along a sweep of $S$ equal $-1$. It is the pull-back of the cohomology suspension of $[\mathrm{SU}(2)]$ under the sweep-holonomy map $\mathcal B\to\Omega\mathrm{SU}(2)$. It equals Donaldson's $\mu(S)=-\tfrac14p_1(\mathbb P)/[S]$ up to a universal sign $\varepsilon$, with no factor of $2$, whenever $\langle c_1(E),S\rangle$ is even. That holds for every bundle used, since $c_e(S)=-4e$. The same class is $c_1(\mathcal L_S)$ for the determinant line of $\bar\partial$ on $S$. The canonical section of $\mathcal L_S$ vanishes exactly on the **jumping-line divisor** $V_S=\{A: E|_S\not\cong\mathcal O\oplus\mathcal O\}$.
2. **Restriction formula [V].** At an abelian reducible $L_1\oplus L_2$ with $v=c_1(L_1)-c_1(L_2)$:
   - $\mu(S)$ restricts to the link $\mathbb P(N)$ as $\pm\tfrac{v\cdot S}{2}\,h$;
   - the stabilizer acts on the fibre of $\mathcal L_S$ with weight $\mp\tfrac{v\cdot S}2$;
   - so the local contribution at a reducible with one-dimensional complex normal space is $\pm\tfrac{v\cdot S}2$.

   This gives the manuscript's dichotomy: $V_S$ contains the reducible iff $v\cdot S\neq0$. Otherwise a sequence in $V_S$ can only converge to it with a bubble on $S$, which raises the Feehan–Leness level by one. The minimal lens cap ($v\cdot S=2$, $\kappa=\tfrac14$) contributes $\pm1$, which recovers Lemma `negative:cap`.
3. **The zero-winding modification is an artifact of holonomy representatives [V for the representative statements, P for the standard transversality].** With holonomy representatives it is genuinely needed: a commuting sweep of winding $0$ can pass through $-1$. With $V_S$ it is not needed:
   - $V_S$ misses *every* connection that is reducible along $S$ with $v\cdot S=0$, whatever its curvature, because a degree-0 line bundle on $\mathbb P^1$ is $\mathcal O$.
   - Compactness is the standard one: the condition persists unless a bubble lies on $S$.
   - The manuscript's segmentation at $J$ is the multiplicativity of the determinant line under nodal degeneration of the domain sphere.
4. **Classical $B$ [V topology, P analysis].** Let $\Phi_c$ be the family map of $(W',c)$ over the interval $G$ (from the $S^3$-split to the $L(4,1)$-split) with $\mu(S)$ inserted. Then
   $$B=\Phi_0-s\,\Phi_{\mathrm{PD}_c(S)}=\Phi_0-s'\,\iota\,\Phi_0\,\iota ,$$
   where $\iota$ is the twist by the flat $\mathbb Z/2$ line on $Y_{\pm2}$. The point is that $\mathrm{PD}(S)=2y$ in $H^2(W')$, so the two "bundles $w$ and $w+\mathrm{PD}(S)$" are the *same* $\mathrm{SO}(3)$-bundle with both end identifications twisted.
   - In DLME's $g_1$, $\hat c-\check c=\mathrm{PD}(S)$ is odd, so the two $w_2$'s really differ.
   - Degree $-1$ (mod 8), level $L-D/8=\tfrac18-\eta$, integral chain map: all as claimed.
   - Mod 2, $B\equiv(\Phi_0\iota+\iota\Phi_0)\iota$.
   - The lens-end term is (P) the cobordism map of the rational blow-down $(W'\setminus\nu S)\cup B_2$.

| Claim | Status | Confidence |
|---|---|---|
| $x(S)=\varepsilon\mu(S)=\varepsilon c_1(\mathcal L_S)=\varepsilon\,\mathrm{PD}[V_S]$ | V | 90% |
| $\mu(S)\vert_{\rm link}=\pm\frac{v\cdot S}{2}h$; stabilizer weight; localization $\pm\frac{v\cdot S}2$ | V | 90% |
| Dichotomy with bubble on $S$ for $V_S$ | V | 85% |
| Zero-winding and segmentation lemmas are replaceable by $V_S$ with standard analysis | P | 75% |
| $\Phi_{\mathrm{PD}_c(S)}=\pm\iota\Phi_0\iota$; $B=\Phi_0\mp\iota\Phi_0\iota$ | V (topology), P (signs) | 85% |
| Lens-end term $=\pm$ map of the rational blow-down $W'_\flat$ | P | 60% |

## 1. Setting

- **The cobordism.** $W'=(-C_2)\cup_{S^3}C_{-2}\colon Y_2\to Y_{-2}$, with $H_1(W')=0$, $b^+=0$, $H_2=\langle F_l,F_r\rangle$ and $Q=\mathrm{diag}(-2,-2)$.
- **The sphere.** $S=F_l-F_r$, $S^2=-4$, $N'=\nu S$, $\partial N'\cong L(4,1)$. Let $\xi\in H^2(N')$ with $\xi(S)=1$, so $\xi^2=-\tfrac14$.
- **The metrics.** $G=[0,1]$ is the interval of metrics: $t=0$ is broken along $J\cong S^3$, and $t=1$ along $\partial N'$.
- **The class $y$.** $y\in H^2(W';\mathbb Z)$ is defined by $y(F_l)=-1$, $y(F_r)=1$. [V]
  - $\mathrm{PD}(S)=(S\cdot F_l,S\cdot F_r)=(-2,2)=2y$.
  - The compactly supported class $\mathrm{PD}_c(S)\in H^2(W',\partial W')\cong H_2(W')$ is *primitive*.
  - $y|_{Y_{\pm2}}\ne0$ in $H^2(Y_{\pm2})=\mathbb Z/2$, because $y(F_l),y(F_r)$ are odd.
  - $y|_{N'}=-2\xi$, which is an order-2 character on $L(4,1)$.
  - $y$ is torsion on $W'\setminus N'$, where $H_2\otimes\mathbb Q=\langle F_l+F_r\rangle$ and $y(F_l+F_r)=0$.
- **Bundles.** $E$ is a $\mathrm U(2)$-bundle with fixed determinant connection and $c_1(E)=c\in\{0,\mathrm{PD}_c(S)\}$. Gauge group: determinant one. $\mathcal B^*$ denotes irreducible configurations with fixed limits, and $\tilde{\mathcal B}$ the configurations framed at a base point.
- **The twist $\iota$.** $\chi\to Y_{\pm2}$ is the flat line with holonomy $\pm1$, and $\iota\colon C(Y_{\pm2})\to C(Y_{\pm2})$ is $\alpha\mapsto\alpha\otimes\chi$. It is a chain involution of Floer's $\mathrm{SU}(2)$ complex, up to orientation signs absorbed into $\iota$.

## 2. The holonomy class is $\mu(S)$

Let $f\colon S^2\to X$ be a sweep $\gamma_s$, $s\in[0,1]$, of based loops from the constant loop to the constant loop, of degree one onto $S$. Equivalently, $f$ is a map $[0,1]^2\to X$ sending $\partial[0,1]^2$ to $x_0$, so $S^2=[0,1]^2/\partial$.

**Lemma 2.1 (normalized holonomy) [V].** The manuscript's $\mathrm{Hol}_0(A,\gamma_s)$ is the holonomy of $E$ divided by the continuous square root of the determinant holonomy, started at $1$. It is the unique lift to $\mathrm{SU}(2)$, starting at $1$, of the path $s\mapsto\mathrm{hol}^{\rm ad}_A(\gamma_s)\in\mathrm{SO}(3)$. Its endpoint is $(-1)^{\langle w_2(\mathrm{ad}E),S\rangle}$. Hence the sweep closes up iff $\langle c,S\rangle$ is even. Then $A\mapsto H_A:=\mathrm{Hol}_0(A,\gamma_\bullet)$ is a conjugation-equivariant map $\tilde{\mathcal B}\to\Omega\mathrm{SU}(2)$ that depends only on $\mathrm{ad}A$.

*Proof.* Divide by a square root of the determinant holonomy; the resulting path lies in $\mathrm{SU}(2)$ and covers the adjoint path. The class of a closed loop in $\pi_1\mathrm{SO}(3)=\mathbb Z/2$, in the sweep trivialization, is the clutching class of $\mathrm{ad}E|_S$, namely $w_2[S]$. ∎

**Definition.** Let $\omega\in H^3(\mathrm{SU}(2))$ be the generator and $\sigma\colon H^3(\mathrm{SU}(2))\to H^2(\Omega\mathrm{SU}(2))$ the cohomology suspension, $\sigma(\omega)=\mathrm{ev}^*\omega/[0,1]$. It is an isomorphism (path–loop Serre spectral sequence) [V]. Set $x_{\rm hol}(S):=H^*\sigma(\omega)$. Its Poincaré dual is represented by
$$V^{\rm hol}_S=\{A:\ -1\in H_A((0,1))\}=\pi(\mathrm{ev}^{-1}(-1)),$$
because $\mathrm{PD}[\{-1\}]=\omega$ and $-1$ is fixed by conjugation. This is exactly the manuscript's $x(S)$.

**Theorem 2.2 [V].** Let $X$ be any oriented 4-manifold, possibly with cylindrical ends, and $f$ as above with $\langle c,f_*[S^2]\rangle$ even. Then on $\mathcal B^*$
$$x_{\rm hol}(S)=\varepsilon\,\mu(S),\qquad \mu(S):=-\tfrac14p_1(\mathbb P)/[S],\qquad \varepsilon\in\{\pm1\}.$$
- The sign $\varepsilon$ depends only on orientation conventions (for $S^2=[0,1]^2/\partial$ and for $\mathrm{SU}(2)$).
- The identity holds in $H^2_{\mathrm{SU}(2)}(\tilde{\mathcal B}^*;\mathbb Z)$, hence in $H^2(\mathcal B^*;\mathbb Z)$ modulo 2-torsion, and $\mu(S)$ is integral here.
- If one uses the $\mathrm{SO}(3)$ holonomy instead, the degree-3 pull-back of $[\mathrm{SO}(3)]$ gives $2x_{\rm hol}$.

*Proof.*
1. *Removing the determinant.* On $\tilde{\mathcal B}\times X$ the framed universal bundle $\tilde{\mathbb E}$ exists and is $\mathrm{SU}(2)$-equivariant, with $c_1(\tilde{\mathbb E})=\mathrm{pr}_X^*c$. So $-\tfrac14p_1(\mathrm{ad}\tilde{\mathbb E})=c_2(\tilde{\mathbb E})-\tfrac14\mathrm{pr}_X^*c^2$. The last term slants to $0$ against $[S]$, since it has no $\tilde{\mathcal B}$-degree. Over $\tilde{\mathcal B}\times S$, twisting by $(\det)^{-1/2}|_S$ (which exists because $c(S)$ is even) does not change $c_2$: the cross terms lie in $H^4(S)=0$. So $\mu(S)=c_2(\mathcal E)/[S]$, where $\mathcal E$ is the $\mathrm{SU}(2)$-normalized bundle on $\tilde{\mathcal B}\times S^2$.
2. *Clutching.* Let $T\to\tilde{\mathcal B}^*_{h\mathrm{SU}(2)}$ be a closed oriented surface; $\mathcal E|_{T\times\{x_0\}}$ is trivial because $\pi_1\mathrm{SU}(2)=0$.
   - Trivialize $\mathcal E$ over $T\times[0,1]^2$ by parallel transport along $t\mapsto\gamma_s(t)$ from the frame at $x_0$.
   - On $\partial[0,1]^2$ this frame is the base frame, except on the edge $t=1$, where it is the base frame times $H_A(s)$.
   - So $\mathcal E$ is the clutching of the trivial bundle on $T\times D^2$ to $T\times\{x_0\}$ by $g\colon T\times\partial D^2\to\mathrm{SU}(2)$, with $g=H$ on one edge and $1$ elsewhere.
   - Hence $\langle c_2(\mathcal E),[T\times S^2]\rangle=\pm\deg g=\pm\langle H^*\omega,[T\times(I,\partial I)]\rangle=\pm\langle x_{\rm hol}(S),[T]\rangle$. This is the standard fact $c_2=\pm\deg(\text{clutching})$, or $c_2=d\,\mathrm{CS}$ with $\int g^*\tfrac1{24\pi^2}\mathrm{tr}(g^{-1}dg)^3$.
3. *Integrality.* With $w_2\cdot S=0$, the Pontryagin square gives $p_1(\mathbb P)/[S]\equiv0\pmod4$, so $\mu(S)$ is integral. ∎

**The loop form (transgression) [V].** For a based loop $\gamma$ along which the determinant has a fixed root, the same clutching argument over $T^3\times S^1$ gives $\mu(\gamma):=-\tfrac14p_1/[\gamma]=\pm\mathrm{hol}_\gamma^*\omega\in H^3$. This is the classical holonomy description of $\mu$ on $H_1$ (DK†, §5.1–5.2).

Theorem 2.2 is its transgression. With $G\colon(I,\partial I)\times S^1\to X$ the sweep, naturality of slant products gives
$$\mu(S)=\big(\mu(\gamma_\bullet)\in H^3(\tilde{\mathcal B}\times(I,\partial I))\big)\big/[I,\partial I].$$

In the four-step proof of the manuscript, the $M_{13}$ face carries exactly $\mu(\beta)$, $\beta=S^1\times0\subset S^1\times D^3$ (Lemma `negative:pentagon`). The contraction of $\beta$ through $\Delta_l,\Delta_r$ (Lemma `negative:sweeps`) is the chain-level identity $\partial V_{\Delta}=V_{\partial\Delta}$ for these representatives, which turns $\mu(\beta)$ over a 2-parameter face into $\mu(\Delta_l\cup\Delta_r)=\mu(\pm S)$ over a 1-parameter edge [P].

**Proposition 2.3 (determinant line; jumping divisor) [V, standard†].** Fix the complex structure on $\mathbb P^1=S^2$. Let $\mathcal E_A=f^*E\otimes(f^*\det)^{-1/2}$ with $\bar\partial_A$; it is of type $\mathcal O(k)\oplus\mathcal O(-k)$, $k\ge0$ (Grothendieck). Put $\mathcal L_f=(\det\mathrm{ind}\,\bar\partial_{\mathcal E_A(-1)})^{-1}$ (Quillen; equivalently, the Dirac operator on $S^2$ coupled to $\mathcal E_A$ — the $\mathcal L_\Sigma$ of DK† §5.2). Then:
- (a) $c_1(\mathcal L_f)=\mu(S)$.
- (b) The canonical section $\det\bar\partial$ vanishes exactly on $V_S:=\{k\ge1\}$, the jumping-line divisor.
- (c) The stratum $\{k\}$ has complex codimension $h^1(\mathcal O(-2k))=2k-1$. So $V_S$ is a complex divisor, smooth off a set of real codimension $\ge6$.
- (d) $\det\bar\partial$ vanishes to first order along $\{k=1\}$.

*Proof.*
- (a) By families Riemann–Roch on the $\mathbb P^1$ fibres: $c_1(\mathrm{ind})=\int_{S^2}\mathrm{ch}_2(\mathcal E)=-c_2(\mathcal E)/[S]=-\mu(S)$, using $c_1(\mathcal E)=0$ and step 1 above.
- (b) Index $0$; the kernel is $H^0(\mathcal O(k-1)\oplus\mathcal O(-k-1))$, nonzero iff $k\ge1$.
- (c) Direct.
- (d) The versal deformation of $\mathcal O(1)\oplus\mathcal O(-1)$ is the extension family $0\to\mathcal O(-1)\to E_t\to\mathcal O(1)\to0$, $t\in H^1(\mathcal O(-2))=\mathbb C$. After twisting by $\mathcal O(-1)$, the kernel-to-cokernel map $H^0(\mathcal O)\to H^1(\mathcal O(-2))$ is the connecting map, i.e. multiplication by $t$. ∎

**Corollary 2.4 [V modulo loop-group facts†].** $x_{\rm hol}(S)$, $\mu(S)$, $c_1(\mathcal L_S)$ and $\mathrm{PD}[V_S]$ agree up to universal signs.

Both $V^{\rm hol}_S$ and $V_S$ are pulled back, under restriction to $S$, from codimension-2 representatives of the generator $u\in H^2(\Omega\mathrm{SU}(2))=\mathbb Z$, using $\tilde{\mathcal B}_{S^2}\simeq\Omega\mathrm{SU}(2)\simeq\mathrm{Gr}_{SL_2}$ (Atiyah†, Pressley–Segal† Ch. 8):
- the evaluation divisor $\{\gamma\ni-1\}$, giving $V^{\rm hol}_S$;
- the Birkhoff–Schubert divisor (the complement of the big cell of trivial bundles), giving $V_S$.

On the parametrized moduli of $B$ the zero-dimensional counts agree once each representative satisfies the compactness properties of §4. The interpolating cobordism must avoid a neighbourhood of the flat connection on $S$; that neighbourhood is contractible in $\tilde{\mathcal B}_{S^2}$, so this costs nothing cohomologically [P].

## 3. Restriction to abelian reducibles

Let $R=\lambda_1\oplus\lambda_2$ be a reducible connection, not necessarily ASD, with $\lambda_1\ne\lambda_2$. Write $v=c_1(L_1)-c_1(L_2)$. The determinant-one stabilizer $\{\mathrm{diag}(z,z^{-1})\}$ acts effectively through $\Gamma=\{u=z^2\}\cong S^1$. The normal space $N_R$ (any finite-dimensional $\Gamma$-invariant subspace of the off-diagonal slice $\Omega^1(\mathrm{Hom}(L_2,L_1))$) has weight $1$, and $\mathbb P(N_R)=S(N_R)/\Gamma$.

**Theorem 3.1 (link restriction) [V].**
$$\mu(\Sigma)|_{\mathbb P(N_R)}=\pm\tfrac{v\cdot\Sigma}{2}\,h,\qquad \nu|_{\mathbb P(N_R)}=-\tfrac14h^2,$$
with $h$ the hyperplane class and universal signs. In particular $\mu(\Sigma)$ is half-integral on links iff $v\cdot\Sigma$ is odd, i.e. iff $w_2\cdot\Sigma\ne0$. This is consistent with §2.

*Proof.* Over $\mathbb P(N_R)\times X$ the universal adjoint bundle is $S(N_R)\times_\Gamma(\mathbb R\oplus L_v)=\mathbb R\oplus(\mathcal O(\pm1)\boxtimes L_v)$, where $L_v=\mathrm{Hom}(L_2,L_1)$ has weight 1. So $p_1=(v\pm h)^2=v^2\pm2h\,v+h^2$. Slanting with $[\Sigma]$ kills $v^2$ and $h^2$ and leaves $\pm2(v\cdot\Sigma)h$; with $[\mathrm{pt}]$ it leaves $h^2$. Multiply by $-\tfrac14$. ∎

This is the restriction formula of Kotschick–Morgan† (their $\zeta=v$, with leading wall-crossing terms $(\zeta\cdot\Sigma/2)^{a}(-\tfrac14)^b$). The Fintushel–Stern† rational-blowdown computation uses its framed form (Prop. 3.2).

**Proposition 3.2 (stabilizer weight, local multiplicity) [V].**
- (a) $\Gamma$ acts on $\mathcal L_S|_R$ by the character $u^{-k}$, where $k=v\cdot S/2=\deg\lambda_1|_S$ in the normalized splitting.
- (b) Hence every $\Gamma$-equivariant section of $\mathcal L_S$ vanishes at $R$ if $k\neq0$. The canonical section is nonzero at $R$ iff $k=0$.
- (c) If the framed normal kernel at $R$ is a complex line of weight $1$, the zero of any equivariant section (canonical or a small equivariant perturbation), restricted to that line, has local degree $\pm k$ whenever it is isolated.
- (d) Equivalently, $\int^{\Gamma}_{\mathbb C}c_1^\Gamma(\mathcal L_S)=c_1^\Gamma|_0/e^\Gamma=\pm k$.

*Proof.*
- (a) At $R$, $\ker=H^0(\mathcal O(k-1))$ has weight $z$ and $\mathrm{coker}=H^1(\mathcal O(-k-1))$ has weight $z^{-1}$, each of dimension $k$ for $k\ge0$. So $\det\mathrm{ind}$ has weight $z^{2k}=u^{k}$.
- (c) An equivariant map $\mathbb C_{(1)}\to\mathbb C_{(-k)}$ has the form $w\mapsto\bar w^kF(|w|^2)$. A generic equivariant perturbation makes $F\colon[0,\epsilon)\to\mathbb C$ nonvanishing, giving degree $-k$. With the complex structure of $H^1(S,\mathrm{Hom}(L_1,L_2))$ instead of $\mathrm{Hom}(L_2,L_1)$, it is $+k$. ∎

The holonomy representative agrees. At $R$ the normalized sweep is $\mathrm{diag}(\lambda(s),\lambda(s)^{-1})$, where $\lambda$ has winding $k$, so its signed crossings of $-1$ sum to $k$ [V, `checks.py`]. When $k=0$ the path may still cross $-1$, in cancelling pairs. That is the defect of $V^{\rm hol}$.

**Corollary 3.3 (dichotomy) [V].** Let $f$ be a sphere map with $c(f)$ even.
- (i) A connection reducible along $f(S^2)$ (i.e. $f^*A=\lambda\oplus\lambda^{-1}$) lies in $V_S$ iff $v\cdot S\ne0$. No condition on curvature or the equation is needed: $\deg\lambda=0$ forces $\lambda\cong\mathcal O$ on $\mathbb P^1$.
- (ii) Suppose $A_n\in V_S$ and $A_n\to(A_\infty;x_1,\dots,x_\ell)$ in the Uhlenbeck sense, with $A_\infty$ reducible along $f$ and $v\cdot S=0$. Then some $x_j\in f(S^2)$. Indeed, otherwise $f^*A_n\to f^*A_\infty$ in $C^0$ after gauge, and $\{\bar\partial\text{ not invertible}\}$ is closed in $C^0$, since $\bar\partial_A-\bar\partial_{A'}$ is $0$-th order.
- (iii) Let $f_1,\dots,f_n$ have pairwise disjoint images. Then at an abelian limit of Feehan–Leness level $\ell$,
  $$\#\{i:\ v\cdot S_i=0\}\le\ell,\qquad \kappa=-\tfrac{v^2}{4}+\ell\ \ge\ -\tfrac{v^2}4+\#\{i:v\cdot S_i=0\}.$$
- (iv) A bubble on $f(S^2)$ costs $8$ in dimension. It regains $2$ from its position on $S$ and $2$ from the dropped insertion, for a net cost of $4$, as in Lemma `analysis:incidence`.

This is the manuscript's dichotomy, Definition `indices:analytic-hypotheses`(ii): a sphere insertion meets a reducible either because $v\cdot S\ne0$ or because there is a bubble on $S$, and distinct spheres use distinct bubbles.

**Remark 3.4 (Feehan–Leness form) [P†].** On the link of $M^{\rm red}_v\times\mathrm{Sym}^\ell X$, Feehan–Leness† (PU(2)-monopole cobordism memoir) write $\mu_p(h)$ as $\tfrac{\langle v,h\rangle}2e+\nu_\ell(h)$. Here $\nu_\ell(h)$ is pulled back from $\mathrm{Sym}^\ell X$ and is dual to "some point lies on $h$". Corollary 3.3 is the representative-level version, which is all the manuscript uses. I did not recheck their normalization.

**Example 3.5 (the minimal lens cap; Lemma `negative:cap`) [V].**
- On $N'$, $d=v=2m\xi$ (since $v\equiv c\bmod2$ and $\xi^2=-\tfrac14$), so $\kappa=m^2/4$ and $E|_S\cong\mathcal O(m)\oplus\mathcal O(-m)$.
- $m=0$: flat, central $+$; it misses $V_S$.
- $m=\pm1$: $\kappa=\tfrac14$, trace-zero boundary flat, the first cap to meet $V_S$, with local contribution $\pm1$ by Proposition 3.2.
- $m=\pm2$: $\kappa=1$, central $-$.
- The same table holds for $c=\mathrm{PD}_c(S)|_{N'}=-4\xi$, with summands $(-\xi,-3\xi)$ at $m=1$ [`checks.py`].
- Irreducible framed caps in $V_S$ would form free $\Gamma$-orbits in a 0-dimensional framed cut-down, so they are absent generically.

So the manuscript's statements (charges, "flat caps miss", signed total $\pm1$) follow from Theorem 3.1 and Proposition 3.2, with no holonomy bookkeeping.

**Example 3.6 (energy per sphere on a negative piece; Lemma `stack:charge-costs`) [V].** On a negative cell, $-v^2=\tfrac12((vF_r)^2+(vF'_l)^2)$ with even evaluations. A sphere seen through a nonzero half costs $-v^2/4\ge\tfrac12$; one seen through a bubble costs $\ell\ge1$. In both cases the contribution to $8\kappa$ is at least $4$, which recovers (`stack:negative-test-cost`).

## 4. Zero-winding: an artifact

**Lemma 4.1 (jumping representative).** Let $f\colon S^2\to X$ be any smooth map; immersion is not needed, so the Hurewicz spheres for $F_l,-F_r$ are allowed. Assume $c(f)$ is even. Then $V_f=\{\mathcal E_A\text{ jumps}\}$ has the following properties.
- (a) $\mathrm{PD}=\pm\mu(f)$ [V, Prop. 2.3].
- (b) It is $\mathrm{Ad}$-invariant and depends only on $\mathrm{ad}A|_{f}$ [V].
- (c) It misses every connection reducible along $f$ with $v\cdot f=0$. On any $C^0$-compact family of such connections it has a uniform neighbourhood gap: $\|\bar\partial^{-1}\|$ is bounded [V].
- (d) It contains every connection reducible along $f$ with $v\cdot f\neq0$, with local multiplicity $\pm v\cdot f/2$ [V, Prop. 3.2].
- (e) Uhlenbeck persistence: the condition is lost only at a bubble on $f(S^2)$ [V, Cor. 3.3].
- (f) Nodal degeneration, below [V for the algebra, P for the analysis].

Properties (a)–(e) are exactly what Lemmas `analysis:zero-winding`, `stack:tests` and `analysis:incidence` (its sphere part) are built to provide.

**What `analysis:zero-winding` really proves [V].** At reducibles the holonomy map lands in $\Omega T$, with $\pi_0\Omega T=\mathbb Z$ given by $k$. The equivariant generator restricts to $\Omega_kT\simeq\mathrm{pt}$ as $k\cdot t\in H^2_T$. At $k=0$ the restriction vanishes, so some equivariant representative avoids $\Omega_0T$. The lemma constructs one by hand for the evaluation divisor. The Birkhoff–Schubert divisor already avoids $\Omega_0T$, since degree-0 torus loops are trivial holomorphic bundles. **So the modification is needed for holonomy representatives and unnecessary for $V_S$.**

**Segmentation as nodal degeneration (Lemma `analysis:segmentation`) [V algebra; P analysis].** At a $J$-split, take domain spheres $P^1_T$ that degenerate to $C_l\cup_pC_r$. The long domain neck maps to a whisker in the $S^3$-neck, where the pulled-back bundle is canonically trivial. The twist $\mathcal O(-1)$ degenerates to $(\mathcal O(-1),\mathcal O)$. Direct computation on the nodal curve:
- $(\mathcal O\oplus\mathcal O,\ \mathcal O\oplus\mathcal O)$ has $H^0(\cdot)=0$: no jump.
- If either side is $\mathcal O(1)\oplus\mathcal O(-1)$, then $H^0\ne0$.

So $\mathcal L_{f_T}\to\mathcal L_{f_l}\otimes\mathcal L_{f_r}$, and the zero set tends to $V_{f_l}\cup V_{f_r}$. A generic point lies on exactly one side, which gives the manuscript's "assigned to exactly one side". A reducible with $v\cdot F_l=v\cdot F_r=0$ is trivial on every $P^1_T$ and on both components, so it is avoided throughout, with no interpolation of logarithms. A reducible with $v\cdot F_l=v\cdot F_r\ne0$ is avoided for $T<\infty$ and seen at the split. That is harmless, because seeing it through a nonzero half already pays the energy of Example 3.6.

**What remains [P, standard].**
- *Transversality of the cut-downs on irreducible strata.* Perturb either the ASD equation (holonomy perturbations), or the section to $\det(\bar\partial_{A|f}+P(A))$ with $P$ small, equivariant, and supported away from a neighbourhood of the relevant compact set of reducible limits. This is the DK†/KM† (JDG 1995) construction of $V_\Sigma$ via sections of $\mathcal L_\Sigma$.
- *Higher genus.* For a surface of genus $g\ge1$ the canonical section is a theta divisor and does *not* automatically avoid $v\cdot\Sigma=0$ reducibles; one would need genericity. The manuscript's use of Hurewicz sphere maps is therefore the right choice, and $V_f$ is canonical there.

**Verdict on item 3.** The zero-winding modification is an artifact. Replace Lemmas `analysis:zero-winding` and `analysis:segmentation`, and the avoidance part of `stack:tests`, by Lemma 4.1. The dimension count becomes $i+1-2=0$ in place of $i+1+1-3=0$.

## 5. The negative interval map in classical terms

**Lemma 5.1 (the second bundle is the $\iota$-conjugate) [V topology; sign P].**
- (a) $\mathrm{PD}(S)=2y\in H^2(W')$. Hence $w_2$ is the same for $c=0$ and $c=\mathrm{PD}_c(S)$.
- (b) The relative classes differ: $\mathrm{PD}_c(S)\bmod2=\delta(\chi_{Y_2}+\chi_{Y_{-2}})$ under $\delta\colon H^1(\partial W';\mathbb Z/2)\to H^2(W',\partial W';\mathbb Z/2)$. Pair $\mathrm{PD}_c(F_l)$ with the cocore of $F_l$.
- (c) Let $E_1$ be the manuscript's bundle: equal to $E_0$ off $N'$, ends included. Then $E_1\cong E_0\otimes L_y$ as $\mathrm U(2)$-bundles. The end identifications differ by the twist $\chi$, and $\otimes(L_y,B_y)$ preserves:
  - projective ASD;
  - the family $G$;
  - holonomy perturbations;
  - the normalized holonomy and $V_S$.

  Hence
  $$\Phi_{\mathrm{PD}_c(S)}=\sigma\,\iota\,\Phi_0\,\iota,\qquad\sigma=\pm1 .$$
- (d) On $W'_\circ=W'\setminus N'$ the class $y$ is $2$-torsion, so $(L_y,B_y)$ can be taken flat with $B_y^2$ trivial. It restricts to $\chi$ on $Y_{\pm2}$ and to $\chi_4$ (order 2) on $L(4,1)$, and the trace-zero flat satisfies $\gamma\otimes\chi_4\sim\gamma$. Hence the lens-end exterior map satisfies $\iota R_0\iota=s'R_0$ at chain level. That $s'$ is a single constant sign is the content of Prop. `negative:local-sign` [P].

*Proof of (c).* $H^1(\partial W';\mathbb Z)=0$, so $H^2(W',\partial)\to H^2(W')$ is injective. Both bundles therefore have the same relative $c_1$; choose the sector by $\kappa$. A determinant-compatible isomorphism $\psi\colon E_0|_Y\otimes\chi\to E_0|_Y$ carries $\alpha\otimes\chi$ to $\iota\alpha$. ∎

**Theorem 5.2 (classical form of Theorem `negative:unit`).** For $c\in\{0,\mathrm{PD}_c(S)\}$ define $\Phi_c\colon C_*(Y_2;\mathbb Z)\to C_{*-1}(Y_{-2};\mathbb Z)$ by
$$\langle\Phi_c\alpha,\beta\rangle=\#\{(t,[A]):\ t\in G,\ A\in M_{g_t}(W',c;\alpha,\beta),\ \mathrm{ind}A=1,\ [A]\in V_S\}.$$
Then:
- **(a)** [V dims, P gluing] $\ \partial\Phi_c+\Phi_c\partial=m_c\,R_c$.
  - $R_c$ counts index-0 instantons on $W'_\circ$ with trace-zero limit at $L(4,1)$; $R_{\mathrm{PD}_c(S)}=R_0$ in the manuscript's convention.
  - $m_c=\pm1$ is the localization of $\mu(S)$ at the minimal reducible cap (Ex. 3.5).
  - The $J$-end contributes nothing: there $\mathrm{ind}\ge0+0+h^0(\theta)=3>2$, even without $V_S$ (DLME's Lemma for $S^3$-broken metrics†).
  - Bubbles are excluded: $8-4>1$.
- **(b)** [V] $\ \Phi_{\mathrm{PD}_c(S)}=\sigma\iota\Phi_0\iota$ (Lemma 5.1).
- **(c)** [V given (a),(b), Lemma 5.1(d)] $\ B:=\Phi_0-s\,\Phi_{\mathrm{PD}_c(S)}=\Phi_0-s'\iota\Phi_0\iota$, with $s=s'\sigma$, is an integral chain map. Indeed
  $$\partial B+B\partial=m_0R_0-s'm_0\,\iota R_0\iota=m_0R_0-s'^2m_0R_0=0 .$$
  Moreover $\iota B\iota=-s'B$.
- **(d)** [V] Degree $D=\dim G-\mathrm{codim}-2c^2-3b^+$, giving $1-2-0=-1$ for $c=0$ and $1-2+8=7\equiv-1$ for $c^2=S^2=-4$. Level $L=-c^2/4-\eta$, so $L-D/8=\tfrac18-\eta(W')$ for both bundles, as the brief states.
- **(e)** [P] Up to chain homotopy, $B$ is independent of the metric interval and of the representative of $\mu(S)$ (homotopies through sections of $\mathcal L_S$ satisfying Lemma 4.1(c)–(e)).
- **(f)** [manuscript; logic checked in B4] $B\otimes\mathbb F_2\simeq g_-g_+$, an isomorphism mod 2. Mod 2, $B\equiv\Phi_0+\iota\Phi_0\iota=(\Phi_0\iota+\iota\Phi_0)\iota$. So the isomorphism mod 2 is the statement that the mod-2 chain map $\Phi_0\iota+\iota\Phi_0$ (a chain map although $\Phi_0$ is not) is invertible on homology.

**Comparison with DLME's $g_1$ [V against `triangle-2.tex`].**

| | DLME $g_1$ | $B$ |
|---|---|---|
| sphere in the lens cap | $S^2=-2$ (in $N$) | $S^2=-4$ ($N'$) |
| split | $\mathbb{RP}^3$ | $L(4,1)$ |
| $\langle c,S\rangle$ | odd | even |
| minimal cap energy | $\tfrac18$ | $\tfrac14$ |
| minimal cap | unframed index $-1$, rigid, no insertion | framed index 2, cut by $\mu(S)$; contributes $v\cdot S/2=1$ |
| second bundle | $\check c=\hat c-\mathrm{PD}(S)$, odd: different $w_2$ | $\mathrm{PD}_c(S)$, even in $H^2(W')$: same $w_2$, equal to $\iota$-twist at both ends |
| lens terms | equal, cancel in $\hat c-\check c$ | equal up to $s$, cancel in $\Phi_0-s\Phi_{\mathrm{PD}_c S}$ |
| degree $D$ | $3$ | $-1$ |
| $L-D/8$ | $-\tfrac18-\eta$ | $+\tfrac18-\eta$ |

So $B$ is the $p=4$ analogue of DLME's $p=2$ family map: the same pairing "$c$ and $c+\mathrm{PD}_c(S)$, equal off $\nu S$", plus one $\mu(S)$ because the minimal reducible cap now has framed dimension 2. The client's phrase "summed over $w$ and $w+\mathrm{PD}(S)$" is literally DLME's $\hat c/\check c$ pattern. The new feature at $p=4$ is that the second summand is $\iota$-conjugate to the first.

**Remarks.**
1. **Rational blow-down [P].**
   - The trace-zero flat $\gamma$ on $L(4,1)$ has adjoint of order 2. It extends flatly over the rational ball $B_2$ ($\pi_1=\mathbb Z/2$) with stabilizer $O(2)\supset U(1)$, $H^1=0$ and $H^+=0$ on the double cover $T^*S^2$. The flat $\mathrm{SO}(3)$ connection obtained this way has $w_2|_{B_2}\ne0$.
   - The framed dimension count gives $0=i_{\rm ext}+0$, and neck-stretching $W'_\flat=W'_\circ\cup B_2$ (with this $w_2$) leaves only $\{\text{ext}\}\times\{\rho\}$.
   - Hence $R_0=\pm(W'_\flat,P_\rho)_*$. In words: $\Phi_0$ alone fails to be a chain map by the cobordism map of the rational blow-down of $S$, which is negative definite with $b_2=1$.
2. **Orientation sign [S].** For closed manifolds, Donaldson's rule changes the orientation by $(-1)^{a^2}$ when the integral lift changes by $2a$ (DK† Ch. 7). Here $a=y$ with $y^2=-1$, which suggests $s=-1$. A relative version with end corrections would be needed; the manuscript avoids computing $s$, correctly.
3. **The 4-manifold obtained by capping [V].** In it, $S_i\cdot a_i=1$ for the negative-cell class $a=(F_r+F'_l)/2$. So $\mathrm{PD}(S_i)\not\equiv0\pmod2$, and the $2^n$ bundles $c_e=c_0+\sum e_i\mathrm{PD}(S_i)$ have pairwise distinct $w_2$. The relative twists $\iota$ glue across the $\phi$-seams ($\iota\phi=\phi\iota$, $\iota^2=1$) into these absolute classes. Hence
   $$\Omega=\sum_{e}\pm D^{\,c_e}_{X,\ \square^n}\big(\mu(S_1)\cdots\mu(S_n)\cdot z\big),$$
   a families Donaldson invariant over the cube of metrics $\square^n=\prod G_i$, summed over the coset $w_0+\mathrm{span}\{\mathrm{PD}(S_i)\}$.

## 6. Dictionary (manuscript → classical)

| Manuscript | Classical replacement |
|---|---|
| $x(S)$: normalized sweep holonomy $=-1$ | $\mu(S)$; representative $V_S$ (jumping lines), or $V^{\rm hol}_S$ (Thm 2.2) |
| eigen-winding $v(S)/2$ | stabilizer weight on $\mathcal L_S$ (Prop. 3.2); link formula (Thm 3.1) |
| Lemma `negative:cap` | Ex. 3.5 (localization $=v\cdot S/2=1$) |
| Prop. `negative:local-sign` | $\iota R_0\iota=s'R_0$ (Lemma 5.1(d)) |
| $B=B_0+B_1$ with weights | $B=\Phi_0-s'\iota\Phi_0\iota$ (Thm 5.2) |
| Lemmas `analysis:zero-winding`, `analysis:segmentation` | Lemma 4.1, nodal degeneration of $\mathcal L_f$ |
| Def. `indices:analytic-hypotheses`(ii) | Cor. 3.3 (bubble on $S$ or $v\cdot S\ne0$) |
| "a particle pays for one test" | disjoint spheres need distinct bubble points (Cor. 3.3(iii)) |
| $M_{13}$ face with $\mathrm{Hol}(\beta)=-1$, contraction | $\mu(\beta)$ for a loop; $V_{\partial\Delta}=\partial V_\Delta$ (§2, [P]) |

## 7. Weak points

- **Signs.** $\varepsilon$, $\sigma$, $s'$ are universal but not computed. Only the existence of a cancelling choice is used, as in the manuscript.
- **Transversality.** Equivariant transversality of $V_f$-cut-downs near the lens cap and on irreducible strata is asserted from the standard DK/KM technique, not reproved. The manuscript's own argument (its "cut variations") adapts verbatim with $\det(\bar\partial+P)$.
- **Loop-group identification.** Corollary 2.4's identification of the two divisors in $\Omega\mathrm{SU}(2)$ is from memory. It is not used in Theorem 2.2, whose clutching proof is self-contained.
- **Rational blow-down.** Remark 1 (§5) relies on a dimension count with stabilizers $U(1)\subset O(2)$ that I checked only at the level of framed dimensions.
- **Not re-examined.** Nothing here touches the mod-2 identity $B\simeq g_-g_+$ (four-step family) or the PU(2) exclusion. The replacements above change representatives, not those arguments.
