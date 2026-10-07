# The distance-four map $B\colon I(S^3_2(K))\to I(S^3_{-2}(K))$

*Round 3, final version. It replaces `round3/B-draft1.md`. The referee's report on that draft, with every check that was made, is §9.*

**Labels.** **VERIFIED**: proved here, checked against the cited source, or checked by explicit computation. **PLAUSIBLE**: a proof sketch whose missing steps are standard analysis not written in the literature for these ends, or a statement with independent supporting evidence. **SPECULATIVE**: conjecture or heuristic. A dagger † marks a reference cited from memory.

**References.**
- [DLME] Daemi–Lidman–Miller Eismeier, *Filtered instanton homology and cosmetic surgery*, arXiv:2410.21248 (source in `dlme/src`). The numbering used is: §2, Lemma 2.7 (`lemma:kappa-ineq`); §3, Prop. 3.4 (`prop:IP-morphism`), Prop. 3.9 (`prop:CDX-triangle`), Prop. 3.10 (`prop:pm-one-map`); §5, Prop. 5.1 (triangle detection), Lemma 5.6 (`lemma:min-index`), Lemma 5.7 (`lemma:N-reducibles`), Lemma 5.10 (`lemma:g-bdry1`), Prop. 5.11 (`prop:g`), Prop. 5.18 (`prop:h`).
- [FS-RB] Fintushel–Stern, *Rational blowdowns of smooth 4-manifolds*, J. Differential Geom. 46 (1997), alg-geom/9505018 (source fetched to `round3/Bref-fs9505018`). Lemma 2.1 (the rational ball $B_p$), Thm. 4.1 (structure theorem, after Kronheimer–Mrowka), Thms. 4.2–4.3 (adjunction for immersed spheres; extremal basic classes, both quoted from [FS-ST]), Lemma 5.2 (blowdown of a $(-4)$-sphere), Lemma 5.3 (dimensions of reducible moduli on $C_p$).
- [FS-BU] Fintushel–Stern, *The blowup formula for Donaldson invariants*, Ann. of Math. 143 (1996), alg-geom/9405002 (source in `round3/Bref-fs9405002`). Thm. 2.1 (Ruberman), Thm. 2.2 (its $\mathrm{SO}(3)$ form), Lemma 2.3 (blowup relations; item (6) is Kotschick's), Thm. 2.4 ($(-3)$-spheres).
- [FS-ST] Fintushel–Stern, *Donaldson invariants of 4-manifolds with simple type*, J. Differential Geom. 42 (1995)†. [KM-ST] Kronheimer–Mrowka, *Embedded surfaces and the structure of Donaldson's polynomial invariants*, J. Differential Geom. 41 (1995)†. [CDX] Culler–Daemi–Xie, *Surgery, polygons and SU(N)-Floer homology*†. [D-FH] Donaldson, *Floer homology groups in Yang–Mills theory*†. [MMR] Morgan–Mrowka–Ruberman, *The $L^2$-moduli space and a vanishing theorem for Donaldson polynomial invariants*†. [BL] Boyer–Lines, *Surgery formulae for Casson's invariant and extensions to homology lens spaces*†.
- [M] the manuscript, cited by file and line in `src/`: §2 is `02-ordinary.tex`, §3 is `03-negative.tex`, §5 is `05-stack.tex`, §10 is `10-gluing.tex`. Notes: T2 = `notes/T2-mu-classes.md`, T5 = `notes/T5-triangles.md`.

---

## 0. Verdict in brief

1. **Theorem A** (§2) is the proposition of intrinsic interest. For every knot $K$, the $\mu(S)$-cut count over the interval of metrics on $W'=(-X_2(K))\#X_{-2}(K)$ that stretches $S^3$ at one end and $L(4,1)=\partial\nu S$ at the other, summed with a relative sign over the two lifts $c$ and $c+\mathrm{PD}(S)$, is a chain map over $\mathbb Z$. The face at $S^3$ is empty for index reasons: the trivial connection there has a three-dimensional stabilizer. The faces at $L(4,1)$ of the two lifts coincide and cancel. **PLAUSIBLE**, 80%. Every dimension count and every piece of arithmetic is **VERIFIED**; what is not verified is the gluing at the trace-zero flat connection with a divisor through the reducible cap, together with the orientation comparison.
2. **Degree and levels.** Up to sign and homotopy there are exactly two such maps, $B$ of degree $-1$ and $B'\simeq\pm B\iota$ of degree $3$. Every counted instanton moves $\widetilde{\mathrm{CS}}-\mathrm{gr}/8$ by $\frac18-E(A)$. The filtered lift of $B$ needs the period $t^{-1}$ on its second summand, and both maps have $L-D/8=\frac18-\eta$. **VERIFIED** (arithmetic).
3. **Proposition B** (§3), the closed counterpart: $D^{w+\mathrm{PD}(S)}_X(Sz)=-D^w_X(Sz)$ for a $(-4)$-sphere. **VERIFIED** for simple type, **PLAUSIBLE** in general.
4. **Relation with $H$** (§4).
   - **VERIFIED:** for the lift of $W_H$ used in [M, §5] one has $c_H^2=0$ and $\deg H=-3$. So $HB$ has degree $4$ and is never chain homotopic to the identity when $I(Y_2)\neq0$.
   - **VERIFIED:** the lifts of $W_H$ split into two classes, of degrees $-3$ and $+1$.
   - **Expected (Conjecture C):** over $\mathbb F_2$, $B\simeq g_-g_+$, and $B$ inverts the lift of degree $+1$ that the families induce. Equivalently $HB\simeq\tau$, with $\tau$ a degree-four product of end twists.
   - **Corollary 4.4:** if $Y_{-2}\cong Y_2$, then all eight groups $I_d(Y_2;\mathbb F_2)$ have the same dimension, so $\dim I(Y_1;\mathbb F_2)\equiv0\pmod 8$. **VERIFIED** given that $H$ is an isomorphism over $\mathbb F_2$.
5. **Errors in the draft.** Corrected in this version (§9.1):
   - a wrong spin comparison with DLME's $g_1$: the spin shifts differ by $\frac12$, not $\frac14$;
   - an unproved claim that $B$ can never be favourable;
   - one mislabelled citation;
   - several overstated labels.

   A shorter route to the relation with $H$, through the manuscript's own two-step identities, replaces the transplanted DLME argument (§4.3).

---

## 1. Setting

Throughout, $K\subset S^3$ is any knot (the unknot included), $Y_r=S^3_r(K)$, $Y_\infty=S^3$, and $X_n$ is the trace of $n$-surgery.

**1.1 The cobordism.** Put
$$W'=(-X_2)\#X_{-2}=W_l\cup_J W_r\colon Y_2\to Y_{-2},$$
with $J\cong S^3$ the connected-sum sphere.
- $H_2(W')=\mathbb ZF_l\oplus\mathbb ZF_r$, where $F_l,F_r$ are the capped Seifert surfaces.
- $Q_{W'}=\mathrm{diag}(-2,-2)$, $\pi_1(W')=1$ and $b^+(W')=0$.
- The cores of the two 2-handles glue along $K\subset J$ to an embedded sphere $S$, with $[S]=F_l-F_r$ and $S\cdot S=-4$.
- $N=\nu S$ is the disk bundle of Euler number $-4$, with $\partial N\cong L(4,1)$. Put $W'_\circ=W'\setminus\operatorname{int}N$. [M, `03-negative.tex` l. 17–31]

**Lemma 1.1** (topology). **VERIFIED.**
- On $(F_l,F_r)$, $\mathrm{PD}(S)=(-2,2)=2y$ with $y=(-1,1)$ and $y^2=-1$. The class $y$ restricts nontrivially to $Y_2$ and to $Y_{-2}$.
- $H_1(W'_\circ)=\mathbb Z/2$, since $F\mapsto F\cdot S$ has image $2\mathbb Z$.
- $H^2(W'_\circ)=H^2(W')/\langle\mathrm{PD}(S)\rangle\cong\mathbb Z\oplus\mathbb Z/2$.
- $y|_{W'_\circ}$ is the torsion class, $y|_{\partial N}=2\in\mathbb Z/4$, and $\mathrm{PD}(S)|_{W'_\circ}=0$.

*Proof.* The exact sequence $H^2(N,\partial N)\to H^2(W')\to H^2(W'_\circ)\to H^3(N,\partial N)=0$. Moreover $y(S)=-2$. ∎

**1.2 Floer complexes and the twist.** $C(Y_{\pm2})=C(Y_{\pm2};\mathbb Z)$ is the irreducible complex of the $\mathrm U(2)$-bundle with trivial determinant, taken modulo determinant-one gauge.
- *Reducibles.* Because $H_1=\mathbb Z/2$, the only reducible flat connections are the central ones, $\theta$ and $\theta'$. Both have $(h^0,h^1)=(3,0)$. **VERIFIED** [M, `02-ordinary.tex` l. 56–80].
- *Grading.* $C(Y_{\pm2})$ is $\mathbb Z/8$-graded relative to $\theta$. It is the reduction at $t=1$ of a $\mathbb Z$-graded, $\widetilde{\mathrm{CS}}$-filtered $\mathbb Z[t^{\pm1}]$-complex, in which $t$ raises the grading by $8$ and $\widetilde{\mathrm{CS}}$ by $1$ [DLME, §3; for $Y_{\pm2}$ see DLME §1.2.2].
- *The twist.* Let $\chi$ be the flat real line bundle with holonomy $-1$, and $\iota(\alpha)=\alpha\otimes\chi$. For twist-invariant perturbations $\iota$ is a chain involution. It has degree $4$ and changes $\mathrm{CS}$ by $\frac12$. **VERIFIED**: on $-X_2$ the reducible $L\oplus L^{-1}$ with $c_1(L)$ the generator ends at $\theta'$, and has energy $-c_1(L)^2=\frac12$, hence relative index $4$. Invariant perturbations exist: **PLAUSIBLE**; use functions of the adjoint holonomy.

**1.3 Flat connections and caps on $N$.** Let $\xi\in H^2(N)$ with $\xi(S)=1$, so that $\xi^2=-\frac14$.

**Lemma 1.2.** **VERIFIED.**
- *(i) Flat connections on $L(4,1)$.* For the determinant-one theory with trivial determinant they are $\theta_L$ and $\theta'_L$ (central, $h^0=3$) and $\gamma_0=[\mathrm{diag}(i,-i)]$ ($h^0=1$). All have $h^1=0$. Moreover $\mathrm{ad}\,\gamma_0=\underline{\mathbb R}\oplus\mathbb C_{-1}$ and $\gamma_0\otimes\chi\cong\gamma_0$.
- *(ii) Reducible caps.* For $c(S)$ even, the reducible ASD connections on $N$ have splitting class $v=2m\xi$. Each has energy $E=m^2/4$ and normalized restriction $\mathcal O(m)\oplus\mathcal O(-m)$ to $S$. Its boundary value is central for $m$ even and $\gamma_0$ for $m$ odd.
- *(iii) Index.* For every cap with $w_2=0$, the framed index is $\delta=8E$: it is $0,2,8,18$ for $|m|=0,1,2,3$.

*Proof of (iii).*
- Use the APS index $-2v^2-\frac32-\frac12(h+\rho)$ with $\rho_k(L(4,1))=-\frac44\sum_{j=1}^{3}\cot^2(\frac{\pi j}4)\sin^2(\frac{\pi kj}4)=0,-1,-2,-1$ for $k=0,1,2,3$, and add $h^0$ to frame.
- This reproduces the dimensions $2t-1$ of [FS-RB, Lemma 5.3] for $p=2$, $e=\langle t+1\rangle$. The minimal $w_2=0$ cap is $t=1$, of unframed dimension $1$.
- FS's *displayed* formula $-2e^2-2-\frac\rho2$, with their displayed $\frac\rho2=\frac{1+2t-t^2}2$, gives $-2,-1,2$ instead. The sign of their $\rho$ is opposite to the APS orientation used in their own computation. Their stated values are correct. ∎

So every non-flat cap with $w_2=0$ has $\delta\ge2$, with equality only for the energy-$\frac14$ reducible with boundary $\gamma_0$.

**1.4 The family, the lifts, the insertion.**

*The family.* $G=[0,1]\ni t\mapsto g_t$, with:
- $g_0$ broken along $J$ and $g_1$ broken along $\partial N$, with round metrics on both;
- $g_t$ unbroken for $0<t<1$;
- fixed cylindrical ends;
- perturbations vanishing on the necks.

In the polygon model the slope vectors are $(2,1),(1,0),(2,-1)$ with $w_0+w_2=4w_1$. So $J$ and $\partial N$ are the two arc cuts of the path $2\to\infty\to-2$, and $G$ is its one-dimensional associahedron [M, `02-ordinary.tex` l. 211–255; `03-negative.tex` l. 27–31]. **VERIFIED.**

*The lifts.* $\mathcal C=\{c\in H^2(W'):c(F_l),c(F_r)\text{ even}\}$, the classes that are trivial on $Y_{\pm2}$. Since $\mathrm{PD}(S)$ is supported in $N$, $E_{c+\mathrm{PD}(S)}$ is identified with $E_c$ over $W'_\circ$, ends included. The second bundle is obtained by gluing the cap $E_c|_N\otimes L_{-2\xi}$ to the unchanged exterior [M, `03-negative.tex` l. 33–42, 233–254].

*The insertion.* For $c\in\mathcal C$, $c(S)$ is even.
- So $\bar\partial_A$ makes $E_A|_S\otimes(\det E_A|_S)^{-1/2}$ a holomorphic bundle $\mathcal O(k)\oplus\mathcal O(-k)$.
- $V_S=\{k\ge1\}$ is the zero set of the canonical section of the determinant line of $\bar\partial_A\otimes\mathcal O(-1)$, which has index $0$. Its Poincaré dual is $\pm\mu(S)$ (T2, Prop. 2.3).
- *(J1)* $V_S$ depends only on $A|_S$, and is closed under $C^0$-convergence of these restrictions.
- *(J2)* A connection that is reducible along $S$ with $\langle v,S\rangle=0$ is not in $V_S$.
- *(J3)* At a connection reducible along $S$ with $k=\frac12\langle v,S\rangle\neq0$, the effective stabilizer acts on the determinant line with weight $\mp k$. So an equivariant section, restricted to a weight-one normal line, has local degree $\pm k$ wherever its zero is isolated (T2, Prop. 3.2).
- All three are **VERIFIED**.
- The manuscript's sweep condition $\mathrm{Hol}_0(a,\gamma_s)=-1$ [M, `03-negative.tex` l. 43–52] represents the same class (T2, Thm. 2.2). **VERIFIED.**

*The counts.* $\mathcal M_c(\alpha,\beta)_k$ is the space of pairs $(t,[A])$ with $A$ a $g_t$-instanton on $E_c$ from $\alpha$ to $\beta$ of unframed index $k$; it has dimension $k+1$. Put
$$\Phi_c(\alpha)=\textstyle\sum_\beta\#\bigl(\mathcal M_c(\alpha,\beta)_1\cap V_S\bigr)\,\beta .$$

---

## 2. The distance-four map

> **Theorem A.** Let $K\subset S^3$ be a knot and $c\in\mathcal C$.
>
> **(a) Chain property.** For generic data $\mathcal M_c(\alpha,\beta)_1\cap V_S$ is finite and
> $$\partial\Phi_c+\Phi_c\partial=m_c\,R_c ,\qquad m_c=\pm1 .$$
> - $R_c\colon C(Y_2)\to C(Y_{-2})$ counts rigid irreducible instantons on $W'_\circ$, for the metric $g_1$ and the bundle $E_c|_{W'_\circ}$, with limits $\alpha$, $\gamma_0$ on $\partial N$, and $\beta$.
> - One has $R_{c+\mathrm{PD}(S)}=R_c$ and $m_{c+\mathrm{PD}(S)}=s\,m_c$, with $s=\pm1$ determined by orientation conventions (and at most by $c(S)\bmod4$).
> - Consequently
> $$B_c=\Phi_c-s\,\Phi_{c+\mathrm{PD}(S)}\colon C(Y_2;\mathbb Z)\longrightarrow C(Y_{-2};\mathbb Z)$$
> is a chain map, of degree $-1-2c^2$.
>
> **(b) The face at $S^3$.** The trivial connection $\theta_J$ is the only flat connection on the neck $J$, and it has stabilizer $\mathrm{SU}(2)$.
> - Every (possibly broken) $g_0$-instanton on $E_c$ with irreducible limits has index at least $3$.
> - Equality holds only for pairs of rigid irreducible instantons on $W_l$ and $W_r$ with common limit $\theta_J$, glued with the parameter $\mathrm{SO}(3)=\mathrm{SU}(2)/\{\pm1\}$.
> - Hence no instanton of index at most $2$ exists for $t$ near $0$, whatever the insertion. Neither $\Phi_c$ (index $1$) nor its boundary relation (index $2$) has a term from this face.
> - The term through $\theta_J$ would appear only for insertions of degree at least $3$.
>
> **(c) Twisting.**
> - $\Phi_{c+\mathrm{PD}(S)}=\pm\,\iota\,\Phi_c\,\iota$, and for every $a\in H^2(W')$, $B_{c+2a}\simeq\pm\,\iota^{a(F_r)}B_c\,\iota^{a(F_l)}$. In particular $\iota B_c\iota=\pm B_c$.
> - Up to sign and homotopy there are exactly two such maps:
> $$B=B_0\ (\text{lifts }0,\ \mathrm{PD}(S);\ \deg -1),\qquad B'=B_{-\mathrm{PD}(F_l)}\ (\text{lifts }-\mathrm{PD}(F_l),-\mathrm{PD}(F_r);\ \deg 3),\qquad B'\simeq\pm B\iota .$$
>
> **(d) Levels.**
> - *Energy.* If $A$ is counted by $B_c$ between lifts $\tilde\alpha,\tilde\beta$, then
> $$\bigl(\widetilde{\mathrm{CS}}-\tfrac18\mathrm{gr}\bigr)(\tilde\beta)-\bigl(\widetilde{\mathrm{CS}}-\tfrac18\mathrm{gr}\bigr)(\tilde\alpha)=\tfrac18-E(A),\qquad E(A)\ge\eta(W',S)>0 .$$
> - *Filtered lift.* $\tilde B_c=\tilde\Phi_c-s\,t^{(c(S)-2)/2}\tilde\Phi_{c+\mathrm{PD}(S)}$ is a filtered chain map of the $\mathbb Z$-graded complexes. It is homogeneous of degree $-1-2c^2$ and level $-\frac14c^2-\eta$, so $L-D/8=\frac18-\eta$.
> - For $B$ the factor is $t^{-1}$, and the uncorrected sum is not a chain map of the $\mathbb Z[t^{\pm1}]$-complexes. For $B'$ the factor is $1$.
> - *Spin.* With $\Lambda=l+c$, $l$ characteristic, and $\Theta=\frac14(\Lambda^2-\sigma(W'))$, the two lifts have equal $\Theta$ if and only if $\Lambda\cdot S=2$. Then $\Theta\le0$, with equality exactly at $\Lambda(F_l,F_r)\in\{(2,0),(0,-2)\}$, and the formal spin shift $\frac18-\Theta$ is at least $\frac18$.
>
> **(e) The lens face.** Let $\Psi_c(g)$ be the count at an unbroken metric $g$ of index-two instantons cut by $V_S$.
> - $\Psi_c(g)$ is null-homotopic, and $R_c$ is a null-homotopic chain map.
> - $B_c$ is the difference of two null-homotopies of $\Psi_c-s\Psi_{c+\mathrm{PD}(S)}$: the one obtained by stretching $J$, and the one obtained by stretching $\partial N$, where this map vanishes identically.

**Status.**
- (a): **PLAUSIBLE**, 80%.
  - The compactness and dimension counts of Lemmas 2.1–2.3 are **VERIFIED**.
  - The gluing at $\gamma_0$ with a divisor through the reducible framed cap (Lemma 2.4), and the orientation comparison (Lemma 2.5), are standard in kind but are not in the literature for these ends.
  - This is [M, `03-negative.tex` l. 66–77, 223–446].
- (b): **VERIFIED** as an index statement; index additivity is [DLME, Def. 5.4] and the argument is that of [DLME, Lemma 5.9]; see also [D-FH]†.
- (c): **VERIFIED** for the topology. **PLAUSIBLE** for perturbations and invariance; 85% given (a).
- (d): **VERIFIED** as arithmetic, given (a) and DLME's formulas [DLME, Prop. 3.4, eq. (energy-rel)].
- (e): follows from (a); **PLAUSIBLE**.

### 2.1 Compactness

**Lemma 2.1.** A sequence in $\mathcal M_c(\alpha,\beta)_k\cap V_S$ with $k\le2$ has a subsequence chain-converging to one of the following [D-FH, Ch. 5]†, [DLME, §5.3]:
- (1) a breaking at $Y_{\pm2}$ through irreducible flat connections;
- (2) a breaking at $Y_{\pm2}$ through $\theta$ or $\theta'$;
- (3) a limit with bubbles;
- (4) a limit over $t=0$;
- (5) a limit over $t=1$.

Cases (2) and (3) do not occur. **VERIFIED.**
- *Case (2).* It costs at least $1+3+1>2$: a trajectory to the reducible, the stabilizer, and a $W'$-piece meeting $V_S$ in the family.
- *Case (3).* $\ell$ bubbles leave index $k-8\ell$. If none lies on $S$, the insertion persists by (J1) and the dimension is at most $k-8\ell+1+4\ell-2<0$. If one lies on $S$, the dimension is at most $k-8+1+2<0$.

### 2.2 The face at $S^3$: where the trivial connection enters

**Lemma 2.2.** For $k\le2$, $\mathcal M_c(\alpha,\beta)_k$ has no point over $t=0$, with or without the insertion. Hence it is empty over $[0,t_*)$ for some $t_*>0$. **VERIFIED.**

*Proof.* A configuration over $t=0$ consists of pieces on $W_l$ and $W_r$, and possibly on cylinders, matched across $J$. The only flat connection on $S^3$ is $\theta_J$, which is nondegenerate with $h^0=3$. The cases:
- *Both pieces irreducible.* Index additivity gives $i(A)=i(A_l)+3+i(A_r)$. Here $i(A_l),i(A_r)\ge0$ by regularity: the pieces carry no parameter.
- *A reducible piece.* A reducible $A_l$ must reach $\alpha$ through a central limit on $Y_2$. Since $b^+(W_l)=0$ it has index at least $-3$ [DLME, Lemma 5.6], so $i(A)\ge1+3-3+3+0=4$. The same holds for $A_r$.
- *Neck instantons* on $\mathbb R\times S^3$ cost at least $5$.

So $i(A)\ge3>2$. ∎

**Where the trivial connection enters, and why it gives no correction.**
- Every limit as $t\to0$ passes through $\theta_J$. A composite "through $S^3$" therefore has two possible parts.
  - The part through the irreducible complex $C(S^3)$ vanishes, because $C(S^3)=0$ ($I(S^3)=0$).
  - The part through $\theta_J$ is, in a reducible-aware theory, the composite of the count on $W_l$ ending at $\theta_J$, the gluing parameter $\mathrm{SO}(3)$, and the count on $W_r$ starting at $\theta_J$.
- That fibre has dimension $h^0(\theta_J)=3$, so the second part occurs only in index at least $3$.
- An insertion of degree $d$ over the interval is counted in index $d-1$, and its boundary relation lives in index $d$.
  - For $d=2$, the case of $\mu(S)$, the face is empty.
  - For an insertion of degree $3$ or $4$ (for instance the point class) the face would contribute. The degree two of $\mu(S)$ is exactly what makes $S^3$ invisible.
- The insertion plays no role in Lemma 2.2, although $S$ crosses $J$ along $K$.

### 2.3 The face at $L(4,1)$

**Lemma 2.3.** For $k\le2$, the points over $t=1$ in the closure of $\mathcal M_c(\alpha,\beta)_k\cap V_S$ are as follows. **VERIFIED** for the dimension count; the regularity used in the last step is **PLAUSIBLE**.
- For $k=1$ there are none.
- For $k=2$ they are the pairs $(A_\circ,A_N^{\min})$, where:
  - $A_\circ$ is a rigid irreducible instanton on $W'_\circ$ with limits $\alpha,\gamma_0,\beta$;
  - $A_N^{\min}$ is the energy-$\frac14$ reducible cap, at its unique point of $V_S$.

*Proof.*
- *The cap is not flat.* The limit satisfies the insertion by (J1), since bubbles were excluded. A flat cap is trivial as an $\mathrm{SO}(3)$ connection on the simply connected $N$, so it misses $V_S$ by (J2).
- *Index count.* By Lemma 1.2, the cap (neck pieces included) has $\delta\ge2$, with equality only for energy $\frac14$ and boundary $\gamma_0$. Moreover $i(A)=i(A_\circ)+\delta$. A rigid irreducible exterior has $i(A_\circ)\ge0$. A reducible exterior reaches $Y_{\pm2}$ only through central limits and costs at least $4$ more. Hence $i(A)\ge2$, with equality only as stated.
- *Irreducible caps.* The unframed irreducible caps of energy $\frac14$ have dimension $1$, so they miss the divisor $V_S$, of codimension $2$, for generic data.
- *The reducible cap.* It lies in $V_S$ with $k=1$. By (J3) and T2, Prop. 2.3(d), it is an isolated zero of local degree $\pm1$ in its weight-one normal line. ∎

**Lemma 2.4** (gluing). Each pair $(A_\circ,A_N^{\min})$ is the limit of exactly one end of the one-manifold $\mathcal M_c(\alpha,\beta)_2\cap V_S$, and that end carries the sign $\varepsilon(A_\circ)\,m_c$. **PLAUSIBLE.** The ingredients:
- $\gamma_0$ is nondegenerate.
- The stabilizer of the cap is all of $\Gamma_{\gamma_0}=\mathrm U(1)$, so the gluing parameter $\Gamma_{\gamma_0}/(\Gamma_{A_\circ}\Gamma_{A_N})$ is a point.
- The framed cap is regular. It has real tangent index $0$ because $H^1(N)=H^+(N)=0$. Its normal operator has complex index $1$ and is made surjective by an equivariant perturbation that vanishes at the reducible [M, `02-ordinary.tex` l. 405–420, item (ii)].
- The divisor is transverse in the normal line.

References: [D-FH, Ch. 4]†, [MMR]† for gluing along reducible flat connections with stabilizers. The manuscript's version is [M, `03-negative.tex` l. 94–221, 391–409].

**Lemma 2.5** (relative sign). Identify $E_{c+\mathrm{PD}(S)}$ with $E_c$ over $W'_\circ$. Then $R_{c+\mathrm{PD}(S)}=R_c$, and $m_{c+\mathrm{PD}(S)}/m_c=s$ does not depend on $\alpha$, $\beta$ or $A_\circ$. **PLAUSIBLE.**

*Sketch.*
- *Same exterior.* The two minimal caps differ by tensoring with $L_{-2\xi}$ followed by a Weyl conjugation at the boundary, since $\mathrm{diag}(i,-i)\sim\mathrm{diag}(-i,i)$. So their exteriors solve the same problem.
- *Excision.* The orientation line over $A_\circ\#A_N$ is $\Lambda(A_\circ)\otimes\Lambda^{\mathrm{fr}}(A_N)$, and the comparison of the two cap lines is local to $N$.
- *Constancy.* Orientability on the determinant-one quotient, which is connected, makes the comparison a single sign.
- *The divisor.* $V_S$ sees only the $\mathrm{SL}_2$-bundle on $S$, which tensoring does not change.

This is [M, `03-negative.tex` l. 223–344].

*Proof of (a).* By Lemmas 2.1–2.5,
$$\partial B_c+B_c\partial=m_cR_c-s\cdot(s\,m_cR_c)=0 .$$
∎

*Proof of (e).*
- $\Psi_c(g)$ is a chain map for unbroken $g$.
- By Lemma 2.2, $\Psi_c(g)=0$ at chain level for $g$ near $g_0$.
- By Lemmas 2.3–2.4, $\Psi_c(g)=m_cR_c$ at chain level for $g$ near $g_1$.
- The family count $\Phi_c$ is a homotopy between the two, so $R_c\simeq0$.
- $\Psi_c-s\Psi_{c+\mathrm{PD}(S)}$ vanishes identically near $g_1$. So $B_c$ is a self-homotopy of the zero map of degree $\deg\Psi+1$, that is, a chain map: the secondary map of the two vanishings. ∎

### 2.4 Twisting

- **The tensor identity.** For $a\in H^2(W')$, $E_{c+2a}\cong E_c\otimes L_a$, where $L_a$ is flat near the ends with holonomy $\chi^{a(F_l)}$ on $Y_2$ and $\chi^{a(F_r)}$ on $Y_{-2}$. Restriction $H^2(W')\to H^2(Y_{\pm2})=\mathbb Z/2$ is evaluation on $F_{l,r}$ modulo two.
  - Tensoring preserves the projective ASD equation, the family and $V_S$.
  - It changes the end identifications by $\chi$.
  - Hence $\Phi_{c+2a}=\pm\iota^{a(F_r)}\Phi_c\iota^{a(F_l)}$. Any two end identifications of the same bundle differ by determinant-one gauge transformations of $Y_{\pm2}$, classified by degree, so this holds up to the choice of lifts in the $\mathbb Z$-graded theory.
- **The two lifts.** For $a=y$ one gets $\Phi_{c+\mathrm{PD}(S)}=\pm\iota\Phi_c\iota$. Hence $B_c=\Phi_c\mp s\,\iota\Phi_c\iota$, and $\iota B_c\iota=\pm B_c$.
- **Exactly two maps.** For $c=(2a,2b)$ on $(F_l,F_r)$, $B_c\simeq\pm\iota^bB\iota^a$, which leaves $B$ and $B\iota=\pm\iota B$. Further:
  - $\deg B_c=-1-2c^2\equiv-1+4(a+b)\pmod8$, consistent with $\deg\iota=4$ (§9.4, item 2);
  - $B'=B_{(2,0)}\simeq\pm B\iota$.

**VERIFIED** (topology). The existence of twist-invariant perturbations and the invariance under change of data (by a two-parameter family) are **PLAUSIBLE**.

### 2.5 Gradings and levels

The DLME conventions [Prop. 3.4 and its proof]: a count of fixed-limit index $i_0=\mathrm{codim}-\dim G$ on $(W,c)$, with rational homology sphere ends, has
- degree $D=-2c^2-3b^+-i_0$,
- level $L=-\frac14c^2-\eta$,

and $E(A)=-\frac14c^2+\widetilde{\mathrm{CS}}(\tilde\alpha)-\widetilde{\mathrm{CS}}(\tilde\beta)$.

- **Degree.** For $B_c$: $i_0=1$, so $D=-1-2c^2$.
  - $B$: the summands have degrees $-1$ and $7\equiv-1$.
  - $B'$: both summands have degree $3$.
- **Levels.** $\widetilde{\mathrm{CS}}-\mathrm{gr}/8$ changes by $-\frac14c^2-E-\frac D8=\frac18-E$.
- **The same instanton in both lifts.** The traceless curvature does not change under tensoring, so $E$ is unchanged. The outgoing lift is therefore multiplied by $t^{-\frac14((c+\mathrm{PD}(S))^2-c^2)}=t^{1-c(S)/2}$. Hence the wall terms are $\tilde R$ and $t^{1-c(S)/2}\tilde R$, and the factor $t^{(c(S)-2)/2}$ restores both cancellation and homogeneity.
- **Positivity.** $\eta>0$ because $W'$ is simply connected and the limits are irreducible.
- **Spin.** $\Lambda=(p,q)$ on $(F_l,F_r)$ is even, and $\Lambda'^2=\Lambda^2+2\Lambda\cdot S-4$. So equal $\Theta$ means $p-q=2$, and then $\Theta=\frac{p(2-p)}4\le0$.
  - Writing $n_D(A)=\Theta-E(A)+\rho(\alpha)-\rho(\beta)$ (notes B1, B4), $\widetilde{\mathrm{CS}}-\rho-\mathrm{gr}/8$ changes by $\frac18-\Theta+n_D(A)$.
  - This agrees with the data $(b^+,\Theta,E,\Delta n_D)=(0,0,\frac18,-\frac18)$ for a copy of $B$.

All of this is **VERIFIED** (§9.4, items 1–3).

**Table 2.6** (degree, $L-D/8+\eta$, formal spin shift).

| map | cobordism, parameters, insertion | degree mod 8 | $L-D/8+\eta$ | spin shift |
|---|---|---|---|---|
| DLME $g_1$ | $(-X_1)\#X_{-1}$, interval, none; $c^2=-1$ | $3$ | $-\frac18$ | $-\frac38$ (max $\Theta=\frac14$) |
| $B$ | $W'$, interval, $\mu(S)$; $c^2\in\{0,-4\}$ | $-1$ | $\frac18$ | $\frac18$ |
| $B'$ | $W'$, interval, $\mu(S)$; $c^2=-2$ | $3$ | $\frac18$ | $\frac18$ |
| $g_-g_+$ | $W'\#(S^2\times S^2)$, square, none; $c^2=0$ | $-1$ | $\frac18$ | $\frac18$ |
| $H$ (lift of [M, §5]) | $W_H$, none; $c^2=0$, $b^+=1$ | $-3$ | $\frac38$ | $-\frac58$ |
| $\iota$ | twist | $4$ | $0$ | $0$ |

- $B'$ and DLME's $g_1$ both have degree $3$.
- Their Chern–Simons shifts differ by $\frac14$, which is the codimension-two insertion.
- Their spin shifts differ by $\frac12$: the insertion contributes $\frac14$, and the drop of the largest admissible $\Theta$ from $\frac14$ to $0$ contributes the other $\frac14$. **VERIFIED.**
- $L-D/8=\frac18-\eta$ is negative only if $\eta>\frac18$, and no lower bound for $\eta$ is known. So $B$ is not *a priori* favourable for DLME's inequality [DLME, Lemma 2.7(b)]. This is consistent with DLME's remark that the trivial-middle variation for $\pm2$ surgery "behaves unfavorably" [DLME, §1.2.2]. That $B$ *is* the variation DLME had in mind is **SPECULATIVE**.

---

## 3. The closed counterpart

> **Proposition B** (the $(-4)$-sphere relation). Let $X$ be closed, oriented and simply connected with $b^+(X)\ge2$, let $S\subset X$ be an embedded sphere with $S\cdot S=-4$, and let $w\in H^2(X;\mathbb Z)$ with $w\cdot S$ even. Then for every $z\in\mathbb A(S^\perp)=\mathrm{Sym}_*(H_0(X)\oplus S^\perp)$,
> $$D_X^{\,w+\mathrm{PD}(S)}(S\,z)=-\,D_X^{\,w}(S\,z),$$
> with the sign conventions of [FS-RB, Thm. 4.1].

**Status.** For $X$ of simple type: **VERIFIED**. In general: **PLAUSIBLE**, 75%.

*Proof for simple type.*
- **The sign change.** By the structure theorem [FS-RB, Thm. 4.1] (after [KM-ST]), $\mathbf D^w_X=e^{Q/2}\sum_K(-1)^{(w^2+K\cdot w)/2}a_Ke^K$. With $w\cdot S$ even and $S^2=-4$, the sign for $w+\mathrm{PD}(S)$ is the sign for $w$ times $(-1)^{K\cdot S/2}$; note that $K\cdot S$ is even, as $K$ is characteristic.
- **The sum.** For $h\in S^\perp$,
$$\partial_S\bigl(\mathbf D^{w+\mathrm{PD}(S)}+\mathbf D^{w}\bigr)(h)=e^{Q(h)/2}\sum_K(-1)^{\frac{w^2+K\cdot w}2}a_K\,(K\cdot S)\bigl(1+(-1)^{K\cdot S/2}\bigr)e^{K\cdot h}.$$
  Only classes with $K\cdot S\equiv0\pmod4$ and $K\cdot S\neq0$ contribute.
- **The extremal classes.** By [FS-RB, Thm. 4.3] (quoted from [FS-ST]), a basic class with $|K\cdot S|>2$ has $K\cdot S=\pm4$, and
$$\textstyle\sum_{K\cdot S=4}a_Ke^{K+S}=(-1)^{(1+b^+)/2}\sum_{K\cdot S=4}a_Ke^{-K-S}.$$
  Distinct exponentials are linearly independent. Together with $a_{-K}=(-1)^{(1+b^+)/2}a_K$ [KM-ST]†, this says:
  - the classes with $K\cdot S=-4$ are exactly the $K+2\mathrm{PD}(S)$ with $K\cdot S=4$;
  - $a_{K+2\mathrm{PD}(S)}=a_K$.
- **Cancellation.** Such a pair has equal signs, since $2\,w\cdot S\equiv0\pmod4$, and equal restrictions to $S^\perp$. Its two terms carry $K\cdot S=\pm4$, so they cancel. The point class enters only through the simple-type relation. ∎

Checks (§9.4, item 6):
- In $K3\#2\overline{\mathbb{CP}}{}^2$, with $S=\sigma+e_1+e_2$ and $x=\sigma-e_1-e_2$, one has $D^0(Sx)=-2$ and $D^{\mathrm{PD}(S)}(Sx)=+2$ (by hand).
- In $31$ random lattices satisfying the conclusion of [FS-RB, Thm. 4.3], $18$ of them with classes $K\cdot S=\pm4$ and both residues $w\cdot S\equiv0,2\pmod4$, the relation holds exactly.
- It fails as soon as one class with $K\cdot S=4$ is given without its partner. So, for simple type, Proposition B is equivalent to the Fintushel–Stern pairing of extremal classes.

*Sketch in general.*
- Write $X=X_0\cup N$ and stretch $\partial N=L(4,1)$, with $V_S$ in $N$ and the classes of $z$ in $X_0$. The latter is possible because $S^\perp$ is the image of $H_2(X_0)$.
- As in Lemma 2.3, the cap meets $V_S$, so it is the minimal reducible, of local degree $\pm1$. The exterior is rigid after cutting by $z$, and has no reducibles since $b^+(X_0)\ge2$.
- Hence $D^w_X(Sz)=m_w\,D_{X_0}[\gamma_0](z)$. The relative invariant is the same for $w$ and $w+\mathrm{PD}(S)$, because $\mathrm{PD}(S)|_{X_0}=0$ and $\gamma_0\otimes\chi\cong\gamma_0$.
- So $m_{w+\mathrm{PD}(S)}/m_w$ is a universal sign, by excision as in [FS-BU, proof of Thm. 2.4], and the example fixes it to be $-1$.

**The family of sphere relations.** In each case one splits along $\partial\nu S=L(p,1)$ and finds the minimal reducible cap that meets the insertion; the cases differ in how its boundary flat connection is recapped by the other lift.

| $S\cdot S$ | relation ($z\in\mathbb A(S^\perp)$, $c\cdot S$ even where relevant) | source |
|---|---|---|
| $-1$ | $D_{c+e}(e\,z)=D_c(z)$ | Kotschick; [FS-BU, Lemma 2.3(6)] |
| $-2$ | $D_c(S^2z)=2D_{c+S}(z)$ | Ruberman; [FS-BU, Thms. 2.1–2.2] |
| $-3$ | $D_c(S\,z)=-D_{c+S}(z)$ | [FS-BU, Thm. 2.4] |
| $-4$ | $D_{c+S}(S\,z)=-D_c(S\,z)$ | Proposition B |

- At $p=2$ the boundary $-1$ is recapped flatly.
- At $p=3$ the boundary $\eta^2=\eta$ is recapped by a cap of dimension $-1$.
- At $p=4$ the boundary $\gamma_0$ is recapped only at the same dimension, so the two lifts produce the same exterior term with opposite signs. That is the cancellation at the lens face in Theorem A. **VERIFIED** against [FS-BU].

---

## 4. Relation with $H$ and with DLME's $g_1$

**Notation.**
- $f_+=u_1u_0\colon C(Y_0^w)\to C(Y_2)$ and $f_-\colon C(Y_{-2})\to C(Y_0^w)$ are the rigid maps along $0\to1\to2$ and $-2\to-1\to0$; $W_H$ is their composite cobordism.
- $g_+\colon C(Y_2)\to C(Y_0^w)$ and $g_-\colon C(Y_0^w)\to C(Y_{-2})$ are the paired interval maps on $2\to\infty\to0$ and $0\to\infty\to-2$ [M, `02-ordinary.tex` l. 16–43]. They are DLME's $g_1$ for the triads $(Z_1,Z_0,Z_{-1})=(Y_2,S^3,Y_0)$ and $(Y_0,S^3,Y_{-2})$, that is, for the framings $\lambda\pm\mu$, except that the second lift is the manuscript's $c+\mathrm{PD}(S_l)$ rather than DLME's bundle $\check c$, which is nontrivial on $Y_2$.
- $H=f_+f_-$ is the composite of [M, §5, l. 19–27], with fixed determinant transitions at $Y_0$.

### 4.1 What is proved

> **Proposition 4.1.** **VERIFIED.**
> (i) $H_2(W_H)$ has the basis $R_1,R_2,R_3,F_0$ with
> - $R_i^2=-2$ and $R_iR_{i+1}=1$,
> - $F_0^2=0$, $F_0R_2=-1$, $F_0R_1=F_0R_3=0$,
> - $\det=-4$ and $b^+(W_H)=1$.
>
> (ii) The lifts $c=\mathrm{PD}(z)$ that are trivial on $Y_{\pm2}$ and odd on the Seifert class $F_0$ of $Y_0$ satisfy $c^2\equiv0$ or $2\pmod 4$, according as the $F_0$-coefficient of $z$ is odd or even. Accordingly $\deg(W_H,c)_*=-2c^2-3\equiv5$ or $1\pmod8$. The two classes differ by a twist at one of $Y_2$, $Y_0$, $Y_{-2}$, each of degree $4$.
>
> (iii) The lift of [M, §5] is $c_H=\mathrm{PD}(G-T_1-T_3)$, from the evaluations $(2,1;1,0,1,0)$ of [M, §5, l. 184–190]. It has $c_H^2=0$ and $\deg H=-3$.
>
> (iv) Hence $HB$ has degree $4$. If $I(Y_2)\neq0$ then $HB\not\simeq\mathrm{id}$, and $B$ can be a homotopy inverse only of a lift of degree $+1$.

*Proof.*
- (i) $W_H$ is the orthogonal complement of $F_r=G-\sum T_b$ and $F_l'=G-2U$ in the lattice $\begin{pmatrix}2&1\\1&0\end{pmatrix}\oplus(-I_4)$ of [M, §5, l. 67–95]. Put $R_i=T_i-T_{i+1}$ and $F_0=G-T_3-T_4$.
- (ii) Write $z=aR_1+bR_2+c'R_3+dF_0$ with $b$ odd. Then $z^2\equiv2(1+d)\pmod4$.
- (iii)–(iv) are then immediate (§9.4, item 5). ∎

This is the precise content of the established fact that "$HB$ is the identity modulo two only up to a degree-four twist". The statement "$B_*=H_*^{-1}$" (T5, Thm. 4.1) is false for this $H$.

**Example** (trefoil).
- For either trefoil, $I(Y_2)\cong I(Y_1)$ has rank $2$, by Floer's triangle with $I(S^3)=0$. For the right-handed trefoil $Y_1=-\Sigma(2,3,5)$ [DLME, Example 3.7]; for the left-handed one $Y_1=\pm\Sigma(2,3,7)$†.
- $\iota$ is an automorphism of degree $4$, so the two generators lie in degrees $d$ and $d+4$ and are exchanged by $\iota$.
- So $HB$, of degree $4$, can be an isomorphism only by exchanging them, as $\iota$ does. This is consistent with $\tau=\iota$.

### 4.2 The expected statement

> **Conjecture C** (over $\mathbb F_2$; expected).
> 1. $g_+$ and $g_-$ are chain homotopy equivalences, and $B\simeq g_-\,\vartheta\,g_+$, where $\vartheta$ is the fixed identification at $Y_0$ induced by the four-step family.
> 2. $B\circ H''\simeq\mathrm{id}$ and $H''\circ B\simeq\mathrm{id}$ up to continuation isomorphisms, where $H''=f^{(1)}_+\,\vartheta\,f^{(1)}_-$ is the rigid map of $W_H$ for the lift induced by the compressed pentagons. By Proposition 4.1 it then necessarily has degree $+1$, so $c''^2\equiv2\pmod4$.
> 3. Consequently $HB\simeq\tau:=H(H'')^{-1}$, a product of an odd number of the degree-four twists $\iota$, $H\iota H^{-1}$ and $f_+\varepsilon f_+^{-1}$. Here $\varepsilon$ is the twist of $C(Y_0^w)$ by the flat $\mathbb Z/2$ bundle, and $\varepsilon$ has degree $4$ because $w\cup\varepsilon\neq0$.
> 4. In particular $B$ and $B'$ are isomorphisms over $\mathbb F_2$, and also over $\mathbb Z_{(2)}$ and $\mathbb Q$, since an integral chain map that is an isomorphism mod $2$ has acyclic cone over $\mathbb Z_{(2)}$.
> 5. If $\tau=\iota$, then $HB'\simeq\mathrm{id}$. Then $B'$, of degree $3$, is to $H$, of degree $-3$, exactly what DLME's $g_1$ is to the third map of their triangle [DLME, Prop. 3.9–3.10].

**Status.**
- Part 1: **PLAUSIBLE**, 60% for $B\simeq g_-\vartheta g_+$; 85% for $g_\pm$ being isomorphisms.
- Part 2: **PLAUSIBLE**, 70% given part 1.
- Part 3: about 50%.
- Which twist $\tau$ is remains undetermined, so $HB'\simeq\mathrm{id}$ has about 35%.

**Answers to the two questions.**
- *Is $B$ chain homotopic to $g_-g_+$?* Expected yes, over $\mathbb F_2$. More precisely $B\simeq g_-\vartheta g_+$, with $\vartheta$ the identification at $Y_0$ fixed by the four-step family. Both sides have degree $-1$, level shift $\frac18-\eta$, spin shift $\frac18$, and the same pair of lifts.
- *Is $g_-g_+$ inverse to $H$ modulo two up to fixed automorphisms?* Expected yes: $g_-\vartheta g_+\simeq J_{-2}(H'')^{-1}J_2$, and $H''=\tau^{-1}H$ with $\tau$ a degree-four product of end twists.
  - For the lift of $H$ used in [M, §5] the twist cannot be removed: degree four is forced (Proposition 4.1, **VERIFIED**).
  - With the other class of lifts it is absent.

### 4.3 Evidence

**Route 1: the manuscript's identities.**
- *(a) The four-step family.* On $W_4=W_{2\to\infty\to0}\cup_{Y_0}W_{0\to\infty\to-2}=W'\#(S^2\times S^2)$ (the double of $X_0$ is $S^2\times S^2$), consider the associahedral family of the path $2,\infty,0,\infty,-2$ with lifts $c=\mathrm{PD}(U)+e\,\mathrm{PD}(S_l)+e'\mathrm{PD}(S_r)$. Its facets give $g_-\vartheta g_+\simeq q_{13}$ over $\mathbb F_2$ [M, `03-negative.tex` l. 448–597]:
  - the $S^3$ facets $Z_1,Z_3$ are empty (Lemma 2.2);
  - the $\mathbb{RP}^3$ facets cancel in pairs;
  - the facets $[-2,0]$ (boundary $S^3$) and $[-2,0,-2]$ (boundary $L(4,1)$) are excluded by charge;
  - only $M_{13}$, the $S^1\times S^2$ facet, remains.

  Rechecked (§9.4, item 7):
  - all four lifts have $c^2=0$, degree $-1$ and $c(U)=e+e'$;
  - the $[-2,0,-2]$ cap has $\det 4$, $b^+=1$ and reducible energies in $\frac14\mathbb Z$ with minimum $\frac14$, so its framed shift is $8E-3\ge-1>-2$;
  - the $[-2,0]$ cap has $v^2=2b(b+d)\in4\mathbb Z$, so its shift is at least $5$.
- *(b) The facet $M_{13}$ is $B$ modulo two* [M, `03-negative.tex` l. 616–879].
  - Only $e=e'$ survives, because projectively flat connections on $S^1\times S^2$ have $w_2=0$ on $S^2$.
  - Root mismatch: $c(A)=1$ is odd, so the matching occurs at the central flat connection $-1$.
  - Replacing $\nu U$ by $S^1\times D^3$ returns $W'$ with lifts $0$ and $\mathrm{PD}(S)$ and the condition $\mathrm{Hol}_\beta=-1$.
  - Contracting $\beta$ through two disks $\Delta_l,\Delta_r$ with $\Delta_l\cup\Delta_r=\pm S$ transgresses $\mu(\beta)$ into $\mu(S)$ on an arc from the $L(4,1)$ edge to an $S^3$ edge. That arc is exactly $B$'s interval.
- *(c) Two-step identities.* The compressed pentagon on $2,\infty,0,1,2$ gives $f_+^{(1)}g_+\simeq J_2$ [M, `02-ordinary.tex` l. 1617–1644], and its mirror gives $g_-f_-^{(1)}\simeq J_{-2}$ (l. 1646–1655), with $J_{\pm2}$ continuation isomorphisms. Hence, on homology,
$$g_-\vartheta g_+\simeq J_{-2}\bigl(f_+^{(1)}\vartheta f_-^{(1)}\bigr)^{-1}J_2 .$$
- *(d) Conclusion.* Together, (a)–(c) give parts 1–2 of Conjecture C. Then $\deg H''=-\deg B=+1$ by Proposition 4.1, which forces the twist in part 3.

**Route 2: DLME and CDX.**
- Triangle detection [DLME, Prop. 5.1, with the argument of §5.5], applied to the triads $(Y_2,S^3,Y_0^w)$ and $(Y_0^w,S^3,Y_{-2})$, whose middle terms $C(S^3)^{\oplus2}$ vanish, makes $g_\pm$ inverse to the third maps $F_\pm$. These are counts on the exteriors $X_{0,\pm2}$ of the $\mathbb{RP}^3$ caps.
- The exterior depends only on the outer slopes $\{0,\pm2\}$, so an interval on $W_{0\to1\to2}=X_{0,2}\cup\nu R$ joins its $Y_1$-split, which gives $u_1u_0$, to its $\mathbb{RP}^3$-split. That split gives $F_+$ times the unique minimal abelian cap: energy $\frac18$, framed index $0$, $c(R)=1$ [M, `02-ordinary.tex` l. 322]. Hence $F_+\simeq f_+$.
- This route needs DLME's reducible analysis [Lemmas 5.6–5.10] and the CDX analysis at $S^1\times S^2$ [Prop. 5.18] transplanted from integer homology spheres to $Y_{\pm2}$ and $Y_0^w$, with the manuscript's pair of lifts in place of $(\hat c,\check c)$. **PLAUSIBLE**, 75%. It is independent of route 1 and agrees with it.

**What cannot be done by homological algebra.** The octahedral axiom applied to the two distance-two triangles produces a triangle $C(Y_2)\to M\to C(Y_{-2})\xrightarrow{H^{\rm ind}}C(Y_2)[1]$ with $M\simeq0$. It identifies cones, not maps, and says nothing about the geometric $B$. Any identification of $B$ needs a family containing $B$ itself, as in (a)–(b). **VERIFIED** (logical).

A two-dimensional alternative, an $h$-relation on the loop $2,\infty,-2,-1,0,1,2$ with $\mu(S)$ inserted, is **SPECULATIVE**. Its hard cap $[-4,-1,-2,-2,-2]$ blows down to $[0]$, and its radical is $S+4T+3R_1+2R_2+R_3$ (**VERIFIED**). It would need the $\mu(S)$-weighted degree of the reducible family on that cap, which has not been computed.

### 4.4 A consequence for cosmetic surgery

> **Corollary 4.4.** Suppose $H$ (for any lift) is an isomorphism over $\mathbb F_2$, as [M, `02-ordinary.tex` l. 16–43] asserts, and suppose there is an orientation-preserving diffeomorphism $\phi\colon Y_{-2}\to Y_2$. Then:
> - $\dim_{\mathbb F_2}I_d(Y_2;\mathbb F_2)$ is independent of $d\in\mathbb Z/8$;
> - $\dim I(Y_1;\mathbb F_2)=\dim I(Y_2;\mathbb F_2)\equiv0\pmod8$;
> - the Euler characteristic of $I(Y_1)$ vanishes, so $\lambda(S^3_1(K))=\frac12\Delta_K''(1)=0$.

*Proof.*
- $\phi_*$ preserves the absolute grading, which is defined by $\theta$.
- Every lift of $W_H$ has $c^2\in\mathbb Z$, because $c$ is trivial on the ends. So $H\phi_*^{-1}$ is an automorphism of odd degree, and odd numbers generate $\mathbb Z/8$.
- $u_1$ has even degree and is an isomorphism, by Floer's triangle with $I(S^3)=0$.
- Taubes' theorem gives $\chi(I(Y_1))=\pm2\lambda(Y_1)$†. ∎

**VERIFIED** given its hypothesis, which is **PLAUSIBLE** (85%). The last conclusion recovers the Boyer–Lines condition $\Delta''_K(1)=0$ [BL]†; the condition modulo $8$ appears to be new. It can also be read off from $B$ (degree $-1$) once Conjecture C holds.

---

## 5. Why $B$ is the natural object

1. **The secondary map of two vanishings.** $\Psi_c=\mu(S)\cdot[W']$ vanishes for two independent reasons.
   - Stretching $S^3$: the trivial connection costs three, and $C(S^3)=0$.
   - Stretching $L(4,1)$: the two lifts produce the same exterior term at the energy-$\frac14$ cap, with opposite signs.

   $B$ is the difference of the two null-homotopies (Theorem A(e)). It is the instanton analogue of a one-parameter invariant over a path between two degenerations along spherical space forms. **VERIFIED** as a description.
2. **The insertion is forced** (T5, §3.3; rechecked).
   - Every admissible lift is even on $S$, so flat caps exist at $L(4,1)$. Without an insertion supported in $N$, the two lifts contribute $R(\theta_L)$ and $R(\theta_L')=\pm\iota R(\theta_L)\iota$, which do not cancel.
   - The minimal non-flat cap has framed index $2$, against $0$ for DLME's $\mathbb{RP}^3$ cap. So a rigid lens face needs a codimension-two condition supported in $N$.
   - $H_2(N)=\mathbb Z S$, so that condition is $\mu(S)$.

   **VERIFIED.**
3. **It is the Floer form of the $(-4)$-sphere relation** (Proposition B). It is adjacent to the rational blowdown: [FS-RB, Lemma 5.2] pairs the lifts $c$ and $c+\mathrm{PD}(S)$ through the flat connections $\pm1$ on $B_2$, and [FS-RB, Lemma 5.3] is the minimal cap. Here $\mu(S)$ kills those flat connections, and the face is carried by $\gamma_0$.
4. **It is the composite of two triangle maps, and $B'$ is the distance-four $g_1$** (Conjecture C, Table 2.6).

**Remark** (rational blowdown; **SPECULATIVE**, 50%).
- $\mathrm{ad}\,\gamma_0$ has order two, and $\pi_1(L(4,1))\to\pi_1(B_2)=\mathbb Z/2$ is onto [FS-RB, Lemma 2.1]. So $\mathrm{ad}\,\gamma_0$ extends flatly over $B_2\simeq\mathbb{RP}^2$, with $w_2=w_1^2\neq0$, framed index $0$ and stabilizer $\mathrm O(2)$.
- Stretching then suggests $R_c=\pm(W'_\flat,P_\rho)_*$ for the rational blowdown $W'_\flat=W'_\circ\cup B_2$. This would make that map null-homotopic for every knot.
- The closed analogue would read $D_{X_\flat,P_\rho}(z)=\pm D^w_X(Sz)$. This is nonzero in $K3\#2\overline{\mathbb{CP}}{}^2$, so the null-homotopy of $R_c$ would be a feature of the $S^3$ neck of $W'$, not of the blowdown.

---

## 6. Location in the manuscript

- The definition is §3, `src/03-negative.tex` ("The negative interval ..."). The words "distance" and "$L(4,1)$" do not occur there; the lens space is "the corresponding lens space of order four" (l. 29).
- $W'=(-C_2)+C_{-2}$ (l. 17–20).
- The sphere (l. 21–26).
- The interval from $J$ to the lens split (l. 27–31).
- The lifts $c_e=e\,\mathrm{PD}(S)$ (l. 33–42).
- The insertion $\mathrm{Hol}_0(a,\gamma_s)=-\mathrm{id}$ (l. 43–52).
- The dimension count $i+1+1-3=0$ and $B=B_0+B_1$ (l. 54–64).
- The main theorem of §3: $B$ is an integral chain map inducing an isomorphism modulo two (l. 66–77).
- The cap lemma (l. 94–221); the local signs (l. 223–344); the chain property (l. 356–446); the four-step family (l. 448–879).
- $B$ is used in §5 ([M, §5], l. 19–21, "the signed negative interval map") and in the gluing tables of `src/10-gluing.tex` (l. 694, 745).
- The manuscript claims that $B$ is an isomorphism modulo two, not that it inverts $H$.

All locations were **VERIFIED** by direct inspection.

---

## 7. Gaps

1. **Gluing at $\gamma_0$** (Lemma 2.4): gluing a rigid exterior to a reducible framed cap that is cut by a divisor through the reducible point. It needs equivariant regularity of the normal operator, by a perturbation vanishing at the reducible, and transversality of $V_S$ in the normal line. Standard in kind; not written for these ends.
2. **Orientations** (Lemma 2.5): the excision comparison of the two cap lines, its independence of the exterior, and its compatibility with the coherent orientations of $C(Y_{\pm2};\mathbb Z)$.
3. **Twist-invariant perturbations** on $Y_{\pm2}$, needed for $\iota$ to be a chain map at chain level and for §2.4.
4. **The four-step family** (Conjecture C, part 1). Gluing at the degenerate central flat connection on $S^1\times S^2$ (where $h^0=h^1=3$), the endpoint case of the CDX spherical cut. Uniform avoidance of $-1$ by the contracting loops along the long $S^1\times D^3$ neck.
5. **Transplanting DLME and CDX** to $Y_{\pm2}$ and $Y_0^w$ (route 2), if that route is used.
6. **Identifying $\tau$**: tracking the relative lifts of $f_\pm^{(1)}$ and the identification $\vartheta$ through the three families, against $c_H=\mathrm{PD}(G-T_1-T_3)$. Proposition 4.1(ii) reduces it to a parity check on $W_\pm$ and at $Y_0$.
7. **Integral versions** of Conjecture C. These need oriented versions of gaps 4 and 6.
8. **Proposition B beyond simple type**: the closed analogue of gaps 1–2.

---

## 8. Verdict and confidence

**The statement.** For every knot $K$, the signed sum over $c$ and $c+\mathrm{PD}(S)$ of the $\mu(S)$-cut interval counts on $W'$ is an integral chain map (Theorem A(a)).
- The face at $S^3$ is empty because $\theta_J$ costs three in index. A correction through $\theta_J$ would require an insertion of degree at least three.
- The faces at $L(4,1)$ of the two lifts are the same exterior count $R_c$, with opposite relative sign.
- Up to sign and homotopy there are exactly two such maps, $B$ (degree $-1$) and $B'\simeq\pm B\iota$ (degree $3$).
- Every counted instanton moves $\widetilde{\mathrm{CS}}-\mathrm{gr}/8$ by $\frac18-E(A)$. The filtered lift of $B$ requires the period $t^{-1}$ on its second summand.
- The closed counterpart, Proposition B, holds for simple type.
- $B$ is expected to invert, modulo two, the lift of $W_H$ of degree $+1$. It cannot invert the lift of degree $-3$ used in [M, §5], with which $HB$ is a degree-four twist.

**Confidence.**
- Theorem A(a): 80%. Theorem A(b): VERIFIED as an index count (about 95%). Theorem A(c)–(e): 80% given (a); the arithmetic in (d) is VERIFIED.
- Proposition B: simple type VERIFIED (about 95%, resting on [FS-RB, Thms. 4.1, 4.3] and $a_{-K}=\pm a_K$); general 75%.
- Proposition 4.1 (degree obstruction): VERIFIED (about 97%).
- Conjecture C: $g_\pm$ isomorphisms 85%; $B\simeq g_-\vartheta g_+$ 60%; $B$ inverts $H''$ about 55%; $HB\simeq\tau$ about 50%; $\tau=\iota$ (so that $HB'\simeq\mathrm{id}$) about 35%.
- Corollary 4.4: 85% (conditional only on the isomorphism property of $H$).

**For the statement as a whole** (Theorem A with Proposition B, Proposition 4.1 as proved, Conjecture C as expected): **75%**.

---

## 9. Referee's report on `B-draft1.md`

### 9.1 Errors found and corrected

1. **Spin comparison with DLME's $g_1$** (draft §7(d)). The draft says that "the difference of $\frac14$ in both shifts is the codimension-two insertion", and labels this VERIFIED. That is false for the spin shift.
   - The spin shifts are $+\frac18$ for $B'$ and $-\frac38$ for $g_1$: the difference is $\frac12$.
   - The insertion accounts for $\frac14$, and the drop of the largest admissible $\Theta$ from $\frac14$ (for $g_1$) to $0$ (for $B$) for the other $\frac14$.
   - Only the Chern–Simons shifts differ by $\frac14$.
   - Corrected in Table 2.6.
2. **"None is favourable"** (draft §7(d)). The draft concludes that among such chain maps "none is favourable for the Chern–Simons filtration". Not proved: $L-D/8=\frac18-\eta$ is negative whenever $\eta>\frac18$, and nothing excludes that. Corrected to "not a priori favourable".
3. **Identification with DLME's unnamed variation** (draft §4.3). The draft states that "$B$ is DLME's 'trivial middle, chain map, unfavourable' variation". DLME do not describe that variation [§1.2.2], so the identification is SPECULATIVE. Only consistency was checked.
4. **Mislabelled citation** (draft §5.2). The draft defines FS97 as *Rational blowdowns* and then cites "FS97 Thm. 4.3 (Fintushel–Stern, Donaldson invariants of 4-manifolds with simple type)". Theorem 4.3 is in *Rational blowdowns* and is quoted there from [FS-ST]. The symmetry $a_{-K}=(-1)^{(1+b^+)/2}a_K$ was used without a source; it is from [KM-ST]† and is not stated in [FS-RB]. Both are corrected.
5. **Perturbation citation** (draft §1.1). "DLME §5.2" for perturbations vanishing on middle ends should be §5.3, where the choice of perturbation is made.
6. **The lift dependence of "the twist is forced"** (draft §§1.4, 6.4). The degree obstruction holds for the lift $c_H^2=0$. Another lift of $W_H$ has degree $+1$, and for that lift no twist is forced (Proposition 4.1(ii), new). The draft's formulation, "$\tau$ a fixed automorphism", is correct but hides that the twist is a comparison between two lifts. Restated as Conjecture C(2)–(3).
7. **Route to $Hg_-g_+\simeq\tau$.** The draft derives it from DLME triangle detection transplanted to $Y_{\pm2}$, plus an identification of the third maps. The manuscript's own two-step identity [M, `02-ordinary.tex` l. 1641] and its mirror give it directly from facts already claimed in the manuscript. The draft mentions the identity but does not use it. Both routes are now given.

### 9.2 Labels downgraded

- Theorem A(a), "VERIFIED modulo the standard package", becomes PLAUSIBLE. Lemma 3.3 of the draft, on which it rests, was itself labelled PLAUSIBLE.
- Lemma 3.4 of the draft (the relative sign), "VERIFIED modulo excision", becomes PLAUSIBLE.
- Draft §6.2, "VERIFIED by reading DLME §§5.3–5.5", becomes PLAUSIBLE. The reading identifies the inputs, but DLME's Lemma 5.6 and the pasting in Prop. 5.18 use integer homology sphere ends and the bundles $(\hat c,\check c)$, which differ here.
- Theorem A(d), the rational blowdown identification (65% in the draft), becomes SPECULATIVE (50%) and is moved to a remark. The closed analogue shows that the relevant invariant is nonzero in general.

### 9.3 Citations checked against the sources

- **[FS-RB]** (source fetched to `round3/Bref-fs9505018`). The theorem counter is per section.
  - §2: Lemma 2.1 = `ratball` ($B_p$, with $\pi_1=\mathbb Z_p$ and a surjection from $\pi_1$ of the lens space).
  - §4: Thm. 4.1 = `KMstruct`, Thm. 4.2 = `FSadj`, Thm. 4.3 = `FSadjspecial`; statements as used.
  - §5: Lemma 5.2 = `C2` ($\mathbf D_{X_2}|_{X^*}=\mathbf D_X-\mathbf D_{X,\sigma}$, flat connections $\pm1$ on $B_2$); Lemma 5.3 = `dim` ($\dim\mathcal M_e=2t-1$, $0\le t\le p$). Confirmed.
  - The sign inconsistency in the displayed formula of Lemma 5.3 was recomputed (item 4 of §9.4) and confirmed.
- **[FS-BU]** (source fetched to `round3/Bref-fs9405002`). Thm. 2.1 (Ruberman, $D(t^2z)=2D_t(z)$); Thm. 2.2 ($D_c(t^2z)=2D_{c+t}(z)$); Lemma 2.3(6) ($\hat D_{c+e}(ez)=D_c(z)$, due to Kotschick); Thm. 2.4 ($D_\omega(tz)=-D_{\omega+t}(z)$ for $t^2=-3$). Confirmed, with the draft's numbering.
- **[DLME].**
  - Prop. 5.1 (triangle detection) and the $g_1$ construction and RP³ cancellation [Lemma 5.10, Prop. 5.11].
  - Prop. 3.10: $g_1$ of degree $3$ and level $\frac14-\eta$, from $c^2=-1$.
  - Prop. 3.4: degree $-2c^2$, level $-c^2/4-\eta$.
  - Lemma 2.7(b): $\ell(B_\bullet)\le\ell(A_\bullet)+(L-D/8)$.
  - §1.2.2: the remark on $\pm2$ surgery.

  All confirmed. One internal inconsistency in DLME, not affecting anything here: Prop. 3.10 writes the induced map as $I_d\to I_{d-1}$ while asserting degree $3$. These agree only modulo $4$, and the proof gives $D=3$.
- **[M].** All the line references of §6 and §4 were confirmed:
  - `02-ordinary.tex`: l. 16–43, 56–80, 211–255, 305–330, 405–420, 1617–1655;
  - `03-negative.tex`: l. 17–879;
  - §5: l. 19–27, 67–95, 184–190;
  - `10-gluing.tex`: l. 694, 745.

  The words "distance" and "L(4" do not occur in `03-negative.tex`.

### 9.4 Computations

The arithmetic was redone independently in `round3/Bfinal-checks/referee_checks.py`, with its record in `referee_checks.out`.

1. **$W'$ lattice.** $S^2=-4$, $\mathrm{PD}(S)=2y$, $y^2=-1$, $H_1(W'_\circ)=\mathbb Z/2$, $y|_{\partial N}=2\in\mathbb Z/4$. Confirmed.
2. **All lifts $c=(2a,2b)$, $|a|,|b|\le3$.**
   - After the factor $t^{(c(S)-2)/2}$ both summands are homogeneous, of the same degree and level.
   - $\deg B_c\equiv-1+4(a+b)\pmod8$, matching $B_c\simeq\iota^bB\iota^a$.
   - $L-D/8=\frac18-\eta$ in every case.
   - $B$: degrees $(-1,7)$, factor $t^{-1}$. $B'$: degrees $(3,3)$, factor $1$.
3. **Spin.** $\Theta$ is equal for both lifts if and only if $\Lambda\cdot S=2$; the maximum is $0$, at $(0,-2)$ and $(2,0)$. Confirmed.
4. **Caps on $N$.** $\rho_k(L(4,1))=0,-1,-2,-1$. For $w_2=0$ the framed index equals $8E$: $0,2,8,18$ for $m=0,2,4,6$, with $v=m\xi$ in this computation. The APS-sign formula reproduces FS's $2t-1=-1,1,3$, while FS's displayed formula gives $-2,-1,2$.
5. **$W_H$.**
   - Basis $R_1,R_2,R_3,F_0$, Gram determinant $-4$, $b^+=1$.
   - The manuscript's lift is $c_H=\mathrm{PD}(G-T_1-T_3)$ with $c_H^2=0$, $c_H(F_r)=c_H(F_l')=0$ and $c_H(F_0)=1$.
   - Lifts with $F_0$-coefficient odd have $c^2\equiv0$ (degree $5\equiv-3$); even, $c^2\equiv2$ (degree $1$). This is new: the draft did not determine which lifts have which degree.
   - The discriminant group $H^2(W_H)/\mathrm{PD}\,H_2(W_H)\cong H^2(Y_{-2})\oplus H^2(Y_2)$ has two nonzero classes with $a^2\equiv\frac12\pmod1$ (a twist at one end, which changes $c^2$ by $2\bmod4$ and the degree by $4$) and one with $a^2\in\mathbb Z$ (twists at both ends, no change). The twist at $Y_0$ is $c\mapsto c+\mathrm{PD}(F_0)$, which changes $c^2$ by $2c(F_0)\equiv2\pmod4$. This confirms that each single twist has degree $4$.
6. **Proposition B.** The draft's examples, $K3\#2\overline{\mathbb{CP}}{}^2$ (five choices of $w$, including $w\cdot S\equiv2\pmod4$) and $K3\#4\overline{\mathbb{CP}}{}^2$, were reconfirmed. Further:
   - The value $D^0(Sx)=-2$, $D^{\mathrm{PD}(S)}(Sx)=2$ in $K3\#2\overline{\mathbb{CP}}{}^2$ was recomputed by hand from the basic classes $\pm e_1\pm e_2$ with $a=\frac14$.
   - $31$ random lattice examples satisfying the pairing of [FS-RB, Thm. 4.3] (in $18$ of which classes with $K\cdot S=\pm4$ occur) satisfy the relation exactly.
   - Control: classes with $K\cdot S=4$ given without their partners leave a nonzero defect.
7. **Four-step family.**
   - The four lifts: $c^2=0$, degree $-1$, $c(U)=e+e'$, $c(A)=1$, $c(S_{l,r})=\pm1$.
   - $M_{04}$ cap $[-2,0,-2]$: $\det4$, eigenvalues $-2,-1\pm\sqrt3$ (so $b^+=1$, $\sigma=-1$). Chain square $b^2+b(d_l+d_r)-\frac14(d_l-d_r)^2$, as in [M, l. 529]. Reducible energies lie in $\frac14\mathbb Z$ with minimum $\frac14$, so the shift is $8E-3\ge-1$.
   - $M_{03}$ cap: $v^2=2b(b+d)$, as in [M, l. 552].
8. **Hard cap $[-4,-1,-2,-2,-2]$.** $\det0$; $(1,4,3,2,1)$ spans the radical; the blow-downs are $[-3,-1,-2,-2]\to[-2,-1,-2]\to[-1,-1]\to[0]$.
9. **Comparison with $g_1$.** $g_1$: $D=3$, $L-D/8+\eta=-\frac18$, largest common $\Theta=\frac14$, spin shift $-\frac38$ (the given fact). $B'$: $D=3$, $\frac18$, $0$, $+\frac18$. So the differences are $\frac14$ (Chern–Simons) and $\frac12$ (spin).
10. **Gradings.** $\deg(HB)=4$, $\deg(HB')=0$, $\deg(H''B)=0$.
    - Odd degree of every lift of $W_H$, hence Corollary 4.4.
    - Consistency with Boyer–Lines through the Casson invariant.
    - The trefoil: $I(Y_2)$ has rank $2$ (for the right-handed trefoil $Y_1=-\Sigma(2,3,5)$, [DLME, Example 3.7]). Since $\iota$ has degree $4$, its generators lie in degrees $d$ and $d+4$, so $HB$ must exchange them.

### 9.5 Attempted counterexamples

1. **Extra ends at $L(4,1)$.** Considered: a flat cap with a bubble on $S$ (dimension $\le-3$); central non-flat caps ($\delta\ge8$); a broken exterior ($\ge3$); irreducible caps of energy $\frac14$ (dimension $1<2$). None survives. **VERIFIED.**
2. **A contribution of $\theta_J$ for low insertion degree.** None occurs. The face does contribute for insertions of degree at least $3$, which locates exactly where $I(S^3)=0$ stops being the whole story. **VERIFIED.**
3. **Proposition B when $\mathrm{PD}(S)$ is primitive in a closed manifold** (unlike on $W'$, where $\mathrm{PD}(S)=2y$). It still holds ($K3\#2\overline{\mathbb{CP}}{}^2$). When $\mathrm{PD}(S)=2y$ is divisible in a closed manifold (for instance a conic in a $\overline{\mathbb{CP}}{}^2$ summand), the sign convention of [FS-RB, Thm. 4.1] gives $D^{w+2y}=(-1)^{K\cdot y}D^w=(-1)^{y^2}D^w=-D^w$ identically, since $K$ is characteristic and $y^2=-1$. This is consistent with Proposition B.
4. **$B\equiv0$ modulo two for symmetry reasons?** Over $\mathbb F_2$, $B=(1+\mathrm{Ad}_\iota)\Phi_0$ lies in the image of the norm map. But $\Phi_0$ is not itself a chain map (its boundary is $m_0R_0$, which need not vanish), so nothing forces $[B]=0$. No contradiction.
5. **$HB\simeq\mathrm{id}$ for some knot?** Impossible by degree whenever $I(Y_2)\neq0$ (Proposition 4.1). For the trefoil the only possibility is the exchange of the two generators, consistent with $\tau=\iota$.
6. **Distinct second Stiefel–Whitney classes in the closed setting.** The fact that the $2^n$ bundles $w_0+\sum e_i\mathrm{PD}[S_i]$ have pairwise distinct $w_2$ in the closed manifold of [M, §5] is consistent with $\mathrm{PD}(S)=2y$ on $W'$. The class $y$ does not extend across the capped ends: on a negative cell, $S_i\cdot\frac12(F_r+F'_l)=1$ is odd.
