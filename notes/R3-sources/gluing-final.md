# Iterated composites and a secondary invariant: the gluing theorem

*Round 3. Final version after a hostile correctness review of `gluing-draft1.md`. It supersedes the draft.*

**Labels.**
- **VERIFIED**: proved here, or checked against the LaTeX source named. Theorem and equation numbers were recomputed from the source.
- **PLAUSIBLE**: standard in kind and argued here, but resting on an analytic input that is not re-proved.
- **SPECULATIVE**: unproved.
- A dagger † marks a citation I could not check against a source available in the scratchpad.

**Sources.**
- `strategy.tex` (Steps 2 and 4, Theorem 2.1). The notes T1 (§1, Lemma 3.1, §4), T2 (Props. 2.3, 3.2, Cor. 3.3, Lemma 5.1, Thm. 5.2), C-closed (§§1–2), the Round 3a correctness report, and `nonvanishing-draft1.md` / `nonvanishing-final.md` (the gluing hypothesis (G)).
- The manuscript, cited as [MS]: `src/02-ordinary.tex`, `src/03-negative.tex`, `src/05-*.tex`. Statements are cited by section and title.
- DLME = Daemi–Lidman–Miller Eismeier, arXiv:2410.21248 (`dlme/src/instanton.tex`, `triangle-2.tex`).
- KM11 = Kronheimer–Mrowka, *Khovanov homology is an unknot-detector*, arXiv:1005.4346 (`round3/km1005.4346`).
- KSE = Kronheimer–Mrowka, *Knots, sutures and excision*, arXiv:0807.4891 (`round3/km0807.4891`).
- FL2b = Feehan–Leness, *PU(2) monopoles. II* (`lit/dg-ga_9712005`).
- D02 = Donaldson, *Floer homology groups in Yang–Mills theory*†. D90 = Donaldson, *Polynomial invariants for smooth four-manifolds*†. DK = Donaldson–Kronheimer†. MMR = Morgan–Mrowka–Ruberman†.

**Computer checks.**
- Mine: `round3/gluing-final-checks/checks_final.py`, items (A)–(H) (§10.2).
- The drafter's: `round3/gluing_checks/checks.py`, items (a)–(h), repeated.

**Notation.**
- $Y_r=S^3_r(K)$; $X_r(K)$ is the trace of $r$-surgery; $C_r=X_r(K)\setminus B^4\colon S^3\to Y_r$.
- $\phi\colon Y_{-2}\to Y_2$ is an orientation-preserving diffeomorphism. It is hypothetical; the theorem is used in a proof by contradiction.
- Index means the fixed-limit unframed index with small decaying weights: DLME's $i(A)$, [MS §2, Convention "Relative sectors and fixed-limit index"].

---

## 0. Findings in brief

1. **The theorem is correct as a statement of classical type** in the form of §2, with all the $Y_{\pm2}$-necks long.
   - With all these necks long, every central matching on a $Y_{\pm2}$-neck costs $3$, and every piece has non-negative excess.
   - So no inequality on chains of several pieces (the family adjunction inequality of T1) is needed, and the draft's architecture is right.
   - I re-derived every arithmetic claim independently and found no counterexample to the corrected statement.
2. **A gap in the draft's proof of the boundary description (its Theorem A(1)).**
   - The draft's bound "excess $\ge1$" for a copy of $W'$ split along $J$ with one reducible half is not justified. It needs the face limits of the representatives of $\mu(S_i)$ to be transverse to the moduli spaces of irreducible instantons on the halves.
   - Without this, two adjacent copies of $W'$, each split along its $J$, with reducible halves facing one central flat on the $Y$-neck between them, have total excess $1=d$. So the analysis of one-dimensional moduli spaces does not close (check (D)).
   - Repair, used below: add the transversality to the admissible data, condition (D5). It is a choice of perturbations in model form near the face. Alternatively, deduce invariance from the gluing identity, which needs only zero-dimensional moduli spaces; there the bound holds without (D5).
3. **Citation corrections.**
   - DLME Props. 3.1 and 3.4 concern integer homology spheres. KM11 §3.9 assumes that every cut satisfies the non-integral condition, i.e. carries no reducibles, and its face formula concerns cuts that separate the two ends. KSE §7.1 concerns admissible bundles. None of them covers $Y_{\pm2}$ with its central reducibles, nor the non-separating lens cut.
   - DLME's "general principle" is at the start of §5.4, before Prop. 5.8, not in §5.3.
   - DLME's $g_1$ (Prop. 3.10) and the cancellation of its $\mathbb{RP}^3$-face terms (proof of Prop. 5.11) are over $\mathbb F_2$; DLME say they work over $\mathbb F_2$ "to avoid checking tedious details with signs". The integral cancellation needed here therefore has no precedent in DLME.
4. **Corollary B must assume** odd determinant on free parts for both $B$ and $H$, not $B$ alone. It refers to the map $B$ of §1.3, defined with the jumping-line representative. Its identification with the manuscript's $B$, defined with holonomy representatives, is T2 Cor. 2.4 and is PLAUSIBLE.
5. **The data must be specified more carefully.**
   - The equation data on $W'_i$ must coincide for $e_i=0,1$ off $N_i$.
   - The representatives of $\mu(S_i)$ must be tensor-paired at the lens face.
   - A transversality perturbation of $V_S$ cannot be supported away from all reducibles if it is to cut the minimal lens cap transversely. It must be allowed, equivariantly, near that cap. In a Kähler model no perturbation is needed there (§4.4).
6. **Scope.**
   - The statement needed downstream is not Theorem A but Theorem A′ (the draft's Remark 6.4). There the necks inside each $W'\cup W_H\cup W'$ stay finite, so that prescribed metrics can be used on the positive pieces.
   - Theorem A′ rests on the manuscript's local analysis of that piece, and it genuinely needs spacing $\ge3$: at spacing $2$, a chain of $k$ adjacent such pieces reaches excess $3-k$ (check (E)).
   - The draft's remark that "the clamp and the spacing are not needed" applies to Theorem A only.
   - The vanishing side, the hypothesis (F) of the nonvanishing reports, must then be proved for metrics whose other $Y_{\pm2}$-necks are long. Invariance under shortening those necks is not available.
7. **Independent verifications added.**
   - $\delta=8E$ for every reducible cap on $\nu S$, by closing up in $\overline{\mathbb{CP}}{}^2$. In particular the minimal cap has $\delta=2$.
   - In the holomorphic model, $V_S$ cuts the framed minimal cap transversely: a non-split extension of $\mathcal O(1)$ by $\mathcal O(-1)$ on $\mathbb P^1$ is trivial.
   - The nodal algebra of Lemma 4.2.
   - Distinct $w_2$ for arbitrary composites.
   - The degrees, the integrality condition, and the order of $u$ modulo $2^N$.
8. **Confidence.**
   - Theorem A: 80% over $\mathbb Z$, 88% over $\mathbb F_2$.
   - Theorem A′: 70%.
   - Corollary B: VERIFIED as algebra, given Theorem A and its hypotheses.
   - Proposition C: 95%.

---

## 1. Setting

### 1.1 Flat connections on the three-manifolds that occur

**Lemma 1.1.** Flat connections are taken on the trivial $SU(2)$-bundle, or on a $U(2)$-bundle with fixed determinant connection and the determinant-one gauge group.
1. $S^3$ carries only the trivial connection $\theta$, with $(h^0,h^1)=(3,0)$. Hence $C(S^3)=0$.
2. On $Y_{\pm2}$ (and on $Y_{\pm1}$) every reducible flat connection is central: $\theta$, and on $Y_{\pm2}$ also $\chi\theta$, where $\chi$ is the flat $\mathbb Z/2$-character. Both have $(h^0,h^1)=(3,0)$. After a small holonomy perturbation that fixes them, the irreducible critical points are nondegenerate.
3. $L(4,1)$ carries exactly $\theta$, $-\theta$ (central, $h^0=3$) and $\gamma=\mathrm{diag}(i,-i)$ (stabilizer $U(1)$, $h^0=1$). All three have $h^1=0$.

**VERIFIED.**
- A reducible representation is abelian and factors through $H_1$, which is $0$, $\mathbb Z/2$ or $\mathbb Z/4$; on $L(4,1)$ the generator goes to $\pm1$ or to a conjugate of $\mathrm{diag}(i,-i)$.
- $H^1(Y;\mathrm{ad}\rho)=0$ at every reducible, since $\pi_1$ is finite in (1) and (3), and the adjoint system is trivial with $b_1=0$ in (2). Compare [MS §2, Lemma "Reducibles at the ordinary ends"].

### 1.2 The pieces and the closed manifold

**The cobordism $W'$.** Put $W'=(-C_2)\cup_JC_{-2}\colon Y_2\to Y_{-2}$, where $J\cong S^3$.
- $H_1(W')=0$ and $\pi_1(W')=1$.
- $H_2(W')=\mathbb ZF_l\oplus\mathbb ZF_r$ with $F_l^2=F_r^2=-2$ and $F_l\cdot F_r=0$. So $b^+(W')=0$, $\chi(W')=2$, $\sigma(W')=-2$.
- The two handle cores form a sphere $S=D_l\cup_KD_r$ with $[S]=F_l-F_r$, $S^2=-4$ and $S\cap J=K$.
- Put $N=\nu S$ and $L=\partial N\cong L(4,1)$. Then $J\cap N=\nu_JK$, so $J$ and $L$ cross and are never stretched together.
- $\mathrm{PD}(S)|_{W'}$ evaluates as $(-2,2)=2y$ on $(F_l,F_r)$.

**VERIFIED** (check (A); T2 §1).

**The cobordism $W_H$.** $W_H\colon Y_{-2}\to Y_2$ is the composite of the four meridional $2$-handle cobordisms along $-2\to-1\to0\to1\to2$.
- It carries the class $c_H$, which is odd on the capped Seifert surface $\hat F\subset Y_0$ and trivial on $Y_{\pm2}$. Put $H=(W_H,c_H)_*$.
- $H_1(W_H)=0$, $b_2=4$, $b^+=1$, $\sigma=-2$, $\chi=4$.
- Filled with the adjacent trace halves, it is the positive piece $P=X_{-2}(K)\cup W_H\cup(-X_2(K))\cong\mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2$. In the basis $(G,U;T_1,\dots,T_4)$ of [MS §5, Prop. "Cell lattices"], $c_0=(2,1;1,0,1,0)$ has $c_0^2=0$, $c_0(F_r)=c_0(F'_l)=0$ and $c_0(F_0)=1$.

**VERIFIED** (check (A); C-closed §1.2).

**The caps.** $C_-\colon\emptyset\to Y_2$ and $C_+\colon Y_2\to\emptyset$ satisfy:
- $H_1(C_\pm)=0$ and $b^+(C_\pm)\ge1$;
- they carry classes $c_\pm$ that are trivial on $Y_2$, with classes $A_\pm$ on which $c_\pm$ is odd;
- their metrics are fixed, with generic periods;
- they carry insertions $z_\pm$, products of $\mu$-classes of surfaces and of points, supported in the interior.

That such caps exist with $q=\langle\Psi_+,\Psi_-\rangle\neq0$ is an input from Step 2 and is not discussed here.

**The closed manifold.** Put $u=(\phi_*B)^3HB$. Its cobordism, in the order in which the factors act, is
$$W_u=W'_1\cup_{Y_{-2}}W_H\cup_{Y_2}W'_2\cup_\phi W'_3\cup_\phi W'_4\cup_\phi .$$
Let $X_M=C_-\cup_{Y_2}W_u\cup\cdots\cup W_u\cup_{Y_2}C_+$, with $M$ copies of $W_u$. It contains $n=4M$ copies $W'_i$, with spheres $S_i$, three-spheres $J_i$ and lens spaces $L_i$, and $m=M$ copies of $W_H$. The copies of $Y_{\pm2}$ along which consecutive pieces are glued are called the $Y$-necks.

**Proposition 1.2 (topology).**
1. $H_1(X_M)=0$ and $b^+(X_M)=b^+(C_-)+b^+(C_+)+M$.
2. Each $J_i$ separates $X_M$, and $X_M\cong Z_0\#Z_1\#\cdots\#Z_n$, where:
   - $Z_0=C_-\cup(-X_2(K))$ and $Z_n=X_{-2}(K)\cup_\phi C_+$ have $b^+\ge1$;
   - each $Z_j$ with $0<j<n$ is either $N_\phi=X_{-2}(K)\cup_\phi(-X_2(K))$ (lattice $\langle-1\rangle^2$) or $P$.
3. The classes $\mathrm{PD}(S_i)\bmod2$ are linearly independent in $H^2(X_M;\mathbb F_2)$. So the $2^n$ classes $c_e=c_0+\sum_ie_i\mathrm{PD}(S_i)$ have pairwise distinct $w_2$. The same holds for every composite word in §2(iv).
4. $c_e^2=c_0^2-4|e|$, and $c_2(E_e)=c_2(E_0)-|e|$ keeps $\kappa=c_2-c_e^2/4$ independent of $e$.

**VERIFIED.**
- (1) and (2) are Mayer–Vietoris over rational homology spheres (C-closed §1.1).
- For (3), each $Z_j$ is closed with $H_1=0$, hence has a unimodular form.
  - A class of square $-2$ is primitive, hence nonzero in $H_2(Z_j;\mathbb F_2)$.
  - In $Z_0$ and $Z_n$, a class pairing oddly with $F_{l,1}$, respectively $F_{r,n}$, gives the coordinate vectors $e_1$ and $e_n$.
  - In $Z_j$ ($0<j<n$) the map $x\mapsto(x\cdot F_{r,j},\,x\cdot F_{l,j+1})\bmod2$ contains $(1,1)$ in its image, whether the two classes agree modulo $2$ (as they do in $N_\phi$, where $F_r=a+b$ and $F'_l=a-b$) or not (as in $P$). This gives $e_j+e_{j+1}$.
  - These vectors span $\mathbb F_2^n$. The argument uses nothing about the cell type, so it applies to every composite (check (C), 300 random words).
- (4) holds because $S_i^2=-4$, $S_i\cdot S_j=0$ for $i\ne j$, and $c_0\cdot S_i=0$.

**Energy.**
- There is a unique $c_0$ restricting to $c_\pm$, $c_H$ and $0$ on the pieces, since $H^1(Y_{\pm2})=0$.
- The cut-down family problem has dimension $8\kappa-3(1+b^+(X_M))+n-2n-\deg z$. It vanishes exactly when $8(\kappa-\kappa_0)=n+3m=7M$, where $\kappa_0$ is the energy of the cap pairing.
- Since every cell contributes $0$ to $c_0^2$, $c_2(E_0)$ is integral iff $8\mid M$.

**VERIFIED** (check (H)).

### 1.3 Floer groups and the maps

**Floer groups.** $C(Y_{\pm2};\mathbb Z)$ is Floer's complex. Its generators are the irreducible critical points of a perturbed Chern–Simons functional; it uses the determinant-one gauge group, coherent orientations, and the $\mathbb Z/8$-grading relative to $\theta$. On $Y_{-2}$ the perturbation is pulled back from $Y_2$ by $\phi$, so $\phi_*$ is an isomorphism of complexes; it preserves the grading because $\phi^*\theta=\theta$.
- $\partial^2=0$: a broken trajectory through $\theta$ or $\chi\theta$ in a one-dimensional space costs at least $1+3+1=5>2$.
- **PLAUSIBLE, standard.** For integer homology spheres this is Floer's theory, [D02, Chs. 2–5]†. The extension to rational homology spheres whose reducibles are central and nondegenerate changes no argument. [MS §2] cites KSE §7.1 for the determinant-one convention (VERIFIED: KSE §7.1 treats admissible bundles only) and Ghosh–Sivek–Zentner, Thm. 2.3† for the two-torsion case. DLME Prop. 3.1 does not cover it: it concerns integer homology spheres and admissible homology $S^1\times S^2$'s.

**Relative invariants.**
- $\Psi_-\in C(Y_2)$ counts rigid instantons on $(C_-,c_-)$ cut down by $z_-$; $\Psi_+$ is defined likewise from $C_+$.
- $\Psi_-$ is a cycle and $\Psi_+$ a cocycle. A breaking through a central flat costs at least $0+3+1>1$. Reducibles on the caps lie on walls of codimension $b^+(C_\pm)\ge1$, avoided by generic periods.
- Each $\Psi_\pm$ is concentrated in one degree modulo $8$.

**The map $B$.** Let $h_t$, $t\in[-1,1]$, be an interval of metrics on $W'$ in the model form of KM11 §3.9: a $J$-neck whose length tends to infinity as $t\to-1$, an $L$-neck whose length tends to infinity as $t\to+1$, and product form near the ends.
- For $e\in\{0,1\}$ let $E_e$ be the $U(2)$-bundle with $c_1=e\,\mathrm{PD}(S)$, identified with $E_0$ off $N$, the ends included.
- Let $\Phi_e\colon C(Y_2)\to C(Y_{-2})$ count pairs $(t,[A])$ with $t\in(-1,1)$, $A$ an index-one instanton on $(E_e,h_t)$ with irreducible limits, and $[A]\in V^t_S$ (§4.2). The dimension is $1+1-2=0$.
- Put $B=\Phi_0-s\,\Phi_1$, where $s$ is the relative sign of §4.5. Equivalently $B=\Phi_0-s'\iota\Phi_0\iota$, where $\iota$ is the twist by $\chi$ (T2 Lemma 5.1, Thm. 5.2).

**The other maps.** $H$ counts index-zero instantons on $(W_H,c_H)$ for a fixed generic metric. It is chain homotopic to $f_+f_-$ (§7.2, item 4).

**Degrees.** By index additivity at the ends ($h^0=3$ at $\theta$), a count of index-$i$ instantons on a cobordism with $b_1=0$ has degree $-2c_1^2-3b^+-i$; over a $p$-parameter family with insertions of codimension $c$ one has $i=c-p$. This is DLME's proof of Prop. 3.4, which treats $b^+=0$; the same argument gives the $b^+$ term.
- $\deg B\equiv-1$ for both lifts: here $i=1$ and $-2c_1^2\in\{0,8\}$.
- $\deg H\equiv-3$ and $\deg u\equiv1\pmod 8$.

**VERIFIED** (check (H)).

### 1.4 Admissible data

**Definition 1.3.** An admissible datum $\mathfrak D$ for $X_M$ consists of the following.
- **(D1) Metrics on $W'_i$.** An interval $h^i_t$ as in §1.3, broken along $J_i$ at $t=-1$ and along $L_i$ at $t=+1$, and a product near $\partial W'_i$.
- **(D2) Fixed metrics** on the copies of $W_H$ and on $C_\pm$. Those on the caps are fixed once and for all, with generic periods.
- **(D3) Perturbations.**
  - Floer's perturbations on $Y_2$, transported to $Y_{-2}$ by $\phi$.
  - Secondary holonomy perturbations on the pieces, in the model form of KM11 §3.9 near the faces.
  - None on the $S^3$- and $L(4,1)$-necks, where all flat connections are nondegenerate.
  - On $W'_i$, the equation data coincide for $e_i=0$ and $e_i=1$ outside $N_i$.
- **(D4) Representatives $V^{t}_{S_i}$ of $\mu(S_i)$.**
  - They are jumping-line divisors for complex structures $j_t$ on $S_i$. Near $t_i=-1$, $j_t$ degenerates conformally to the nodal curve $f_{l,i}\cup_pf_{r,i}$ of Lemma 4.2.
  - Transversality perturbations of the canonical section are small and depend only on $A|_{N_i}$. They vanish near connections reducible along $S_i$ with $v\cdot S_i=0$.
  - Near the minimal reducible lens cap they are equivariant (or absent, §4.4), and they are tensor-paired between $e_i=0$ and $e_i=1$.
  - Near $t_i=-1$ they have product form under the splitting $\mathcal L_{S}\to\mathcal L_{f_l}\otimes\mathcal L_{f_r}$.
- **(D5) The face condition.** The moduli spaces of irreducible instantons on the completed halves $(-C_2)^\wedge$ and $(C_{-2})^\wedge$ of each $W'_i$ (with irreducible or central outer limit and limit $\theta$ on $J_i$) are transverse to the face limits $V_{f_{l,i}}$, $V_{f_{r,i}}$ of the representatives. This holds for generic half-perturbations in model form, because $V_{f}$ is a fixed divisor, smooth off a set of codimension six (T2 Prop. 2.3(c)).
- **(D6) Cap insertions** in general position, so that no point lies in supports of total codimension greater than four, with each $S_i$ counting two. This is the inequality [FL2b, (3.25)].
- **(D7) Orientations.** I-orientations of the pieces [KM11, Def. 3.9] and Floer orientations. Weights $\varepsilon(e)=\prod_i\varepsilon_i(e_i)$, with $\varepsilon_i(0)=1$ and $\varepsilon_i(1)=-s$.
- **(D8) A neck length $T$** for all $Y$-necks.

The family $g^{\mathfrak D_T}$ over $Q=[-1,1]^n$ compactifies over $\bar Q$ to a family of broken metrics in the sense of KM11 §3.9. A face of codimension $k$ is broken along $k$ pairwise disjoint hypersurfaces $J_i$ or $L_i$. Over $\bar Q\times[T_0,\infty]$, the face $T=\infty$ breaks all $Y$-necks at once.

### 1.5 The secondary count

For $e\in\{0,1\}^n$ put
$$\mathcal M^e(\mathfrak D_T)=\Big\{(t,[A]):\ t\in\mathrm{int}\,Q,\ A\ \text{ASD for }g_t\text{ on }E_e,\ [A]\in\textstyle\bigcap_iV^{t_i}_{S_i}\cap V(z_-)\cap V(z_+)\Big\},
\qquad
\Omega_M(\mathfrak D_T)=\sum_e\varepsilon(e)\,\#\mathcal M^e(\mathfrak D_T),$$
when these are finite sets of regular points.

---

## 2. Statements

**Theorem A (gluing for iterated composites, long necks).** Let $K\subset S^3$ be a knot, $\phi\colon Y_{-2}\to Y_2$ an orientation-preserving diffeomorphism, and $C_\pm,\Psi_\pm,B,H,u$ as in §1. Let $M\ge1$. For every admissible datum $\mathfrak D$ there is $T_0$ such that the following hold for all $T\ge T_0$.

1. **(Finiteness and gluing.)**
   - Each $\mathcal M^e(\mathfrak D_T)$ is a finite set of regular points.
   - Its points correspond bijectively to the choices of one rigid irreducible solution on each piece, with matching irreducible limits on all $Y$-necks. Each copy $W'_i$ contributes a point counted by $\Phi_{e_i}$, over an interior parameter.
   - Consequently
   $$\Omega_M(\mathfrak D_T)=\varepsilon_0\,\langle\Psi_+,u^M\Psi_-\rangle$$
   at chain level, with the chain maps of $\mathfrak D$. Here $\varepsilon_0=\pm1$ depends only on the orientation conventions.
   - If $8\nmid M$, both sides are zero.
   - This part does not use (D5).
2. **(Invariance.)** $\Omega_M(\mathfrak D_T)$ is independent of $T\ge T_0$ and of $\mathfrak D$ among data with the given caps, up to the overall sign fixed by the orientation data. It depends on the caps only through the classes $[\Psi_\pm]$, which for $b^+(C_\pm)=1$ may depend on the chambers of the cap metrics.
3. **(The boundary contributions; uses (D5).)** Along a generic path of admissible data with $T\ge T_0$, the one-dimensional moduli spaces over $Q\times[0,1]$ have ends of only two kinds.
   - Ends over the endpoints of the path.
   - Ends over faces $\{t_i=+1\}$, of the form (rigid irreducible solution on $X_M\setminus N_i$ with limit $\gamma$) $\times$ (minimal cap on $N_i$). These cancel in pairs between $e$ and $e+e_i$.

   There are no ends over the faces $\{t_i=-1\}$ and none from bubbling. The counts $\#\mathcal M^e$ for a single $e$ are in general not invariant.
4. **(Other composites.)** Parts (1)–(3) hold verbatim for every composite $Y_2\to Y_2$ of copies of $W'$ (each with its interval and sphere), $W_H$, $\phi$ and $\phi^{-1}$ that is defined, i.e. whose consecutive ends match. The right side is the corresponding word in $B$, $H$ and $\phi_*^{\pm1}$; in particular this includes $(HB)^M$. With $n$ copies of $W'$ and $m$ of $W_H$, both sides vanish unless $n+3m\equiv0\pmod 8$. No condition on the spacing of the copies of $W_H$ is needed.

**[PLAUSIBLE, 80% over $\mathbb Z$; 88% over $\mathbb F_2$.]** It is proved in §§4–6 modulo the standard inputs of §7 and Gaps 1–4 of §8.

**Theorem A′ (finite necks inside the positive pieces).** Suppose the copies of $W_H$ in a word are at mutual distance at least $3$, measured in copies of $W'$. Equivalently, consecutive composites $W'_a\cup W_H\cup W'_{a+1}$ are separated by at least one further copy of $W'$; the word $u^M$ has distance $4$.
- Keep finite the two $Y$-necks inside each such composite, and let the other $Y$-necks have length $T$.
- The metrics on these composites may be the prescribed metrics required by the vanishing argument, with their two-parameter families.

Then, for $T\ge T_0$, parts (1) and (2) of Theorem A hold with the same right side. The count of each such composite is chain homotopic to $BHB$ [MS §5, the proposition identifying the two-parameter count with $BHB$].

**[PLAUSIBLE, 70%.]** It is conditional on the manuscript's local analysis of the positive piece [MS §5, Lemmas "Local charge costs" and "Local excess, including central outer limits"]. The spacing hypothesis is necessary for this argument (§5.3).

**Corollary B (nonvanishing modulo $2^N$; conditional).** Let $L(Y)=I(Y;\mathbb Z)/\mathrm{Tor}$. Suppose $B$ and $H$ induce isomorphisms of $L(Y_{\pm2})\otimes\mathbb Z_{(2)}$. This holds if they induce isomorphisms on $I(\cdot\,;\mathbb F_2)$ [MS §5, Lemma "The finite-lattice argument"]. The statement for $H$ is the manuscript's theorem on the ordinary handle maps (§2); the statement for $B$ was demoted to "expected" by the Round 3a referee.

Let $e_N$ be the order of $u$ in $GL(L(Y_2)/2^N)$. Then $8\mid e_N$ if $L(Y_2)\ne0$, and if $2^N\nmid q$, then for every $M\in e_N\mathbb Z_{>0}$
$$\Omega_M\equiv\pm q\not\equiv0\pmod{2^N}.$$
**[VERIFIED given Theorem A and the hypotheses]** (§6.6; check (H) for $8\mid e_N$).

**Proposition C (the primary invariants vanish).**
1. For every $w$ and every $z'$, $D^w_{X_M}(z')=0$, and all Seiberg–Witten invariants of $X_M$ vanish.
2. At a fixed metric $g_t$, the problem cut down by $\mu(S_1)\cdots\mu(S_n)z$ has virtual dimension $-n$.

**[VERIFIED as topology; classical theorem† (D90; DK §9.3†); 95%.]**

---

## 3. Why the invariant is secondary

### 3.1 $X_M$ is a connected sum

Each $J_i$ separates $X_M$ into a part containing $C_-$ and a part containing $C_+$, both with $b^+\ge1$ (Prop. 1.2). Donaldson's argument is as follows.
- Stretch $J_i$. Instantons converge to pairs on the two sides, each with limit $\theta$ on $S^3$.
- Nearby solutions are parametrized by the pairs together with the gluing parameter, which lies in the stabilizer $SO(3)$ of $\theta$. Insertions supported away from $J_i$ do not see that parameter.
- So a zero-dimensional cut-down space would fibre over a space of dimension $-3$, and is empty for long necks. Generic metrics exclude reducibles on either side because $b^+\ge1$ there.

The neck kills the invariant because $\theta$ has a three-dimensional stabilizer and $S^3$ has no irreducible flat connections, so that the irreducible part of the face factors through $C(S^3)=0$. **[VERIFIED as an argument; the theorem is classical†.]**

### 3.2 The cube as a relative cycle

At a fixed metric the problem with all $n$ sphere insertions has dimension $-n$ (Prop. C), and the $n$ parameters of $Q$ restore dimension zero.
- No closed $n$-cycle of metrics is available: the space of metrics is contractible.
- Moreover $b^+(X_M)=b^+(C_-)+b^+(C_+)+M<n$ for large $M$, so a generic $n$-parameter family meets reducibles.

$Q$ is instead a relative cycle whose faces each contribute nothing for a different reason.
- At $t_i=-1$ the reason is that of §3.1, applied on a face of the family.
- At $t_i=+1$ each bundle contributes, but $c$ and $c+\mathrm{PD}(S_i)$ contribute oppositely.

A family count over a manifold with corners whose face terms vanish in total is an invariant of that face structure. This is the precise sense in which $\Omega_M$ is secondary. **[VERIFIED as logic, given Theorem A.]**

### 3.3 $B$ as the difference of two null-homotopies

Fix $t_0\in(-1,1)$ and let $P_e=\Phi^{t_0}_e$ count index-two instantons on $(W',E_e,h_{t_0})$ in $V_S$. This is a chain map of degree $-2$: reducibles on $W'$ have central limits, and the breakings through them cost at least $8$.
- Let $K_{J,e}$ and $K_{L,e}$ be the counts over $[-1,t_0]$ and $[t_0,1]$. By the boundary formula of KM11 §3.9, together with §4:
  - $\partial K_{J,e}\pm K_{J,e}\partial=\pm P_e$, since the $J$-face is empty;
  - $\partial K_{L,e}\pm K_{L,e}\partial=\pm(m_eR-P_e)$, where $m_eR$ is the lens term (§4.5).
- So each $P_e$ is null-homotopic through $K_{J,e}$, i.e. through $C(S^3)=0$. The weighted sum $P_0-sP_1$ is null-homotopic a second time, through $K_{L,0}-sK_{L,1}$, because the lens terms cancel.
- $B=(K_{J,0}-sK_{J,1})+(K_{L,0}-sK_{L,1})$ is the difference of the two null-homotopies, a cycle of degree $-1$.
- The second null-homotopy exists only for the weighted sum over $c$ and $c+\mathrm{PD}(S)$ (Round 3a report, 1.6).

**[VERIFIED as algebra, given §4.]** Over the cube, $\Omega_M$ is the $n$-fold iterate of this construction, capped by $\Psi_\pm$. None of the fixed-metric counts, face counts or single-bundle counts is invariant; only the weighted total over $Q$ is.

### 3.4 Comparison with the surgery triangles

The device of an interval of metrics joining two incompatible degenerations, summed over two bundles, is that of the surgery exact triangles: Floer; Braam–Donaldson†; Kronheimer–Mrowka–Ozsváth–Szabó†; Culler–Daemi–Xie†; and DLME.
- In DLME's $g_1$ [DLME, Prop. 3.10], the interval on $W^1_{-1}$ goes from the split along $Z_0=S^3$ (where $C(S^3)=0$) to the split along $\mathbb{RP}^3$. The map is the difference of the counts for $\hat c$ and $\check c$.
- The $\mathbb{RP}^3$-face terms are equal at chain level and cancel [DLME, Lemma 5.10 and proof of Prop. 5.11], over $\mathbb F_2$.
- $B$ is the distance-four analogue (T2, table in §5), with three differences:
  - the minimal cap now has framed index $2$, so $\mu(S)$ must be inserted;
  - the two bundles have the same $w_2$ on $W'$ (since $\mathrm{PD}(S)=2y$) and differ by the twist $\iota$ at the ends;
  - the cancellation must hold over $\mathbb Z$, because the eventual contradiction is with a factor $2^{n_D-1}$.

KM11's face formula (the last display of §3.9) is the relative statement of which Theorem A(1) is a closed, capped form, applied at the $Y$-necks, which are separating cuts.

---

## 4. A single copy of $W'$

### 4.1 Index conventions

- **(I1) Additivity.** Matching two fixed-limit pieces across a nondegenerate flat $\rho$ adds $h^0(\rho)$. **VERIFIED as citation**: DLME's proof of Prop. 3.4 cites [D02, (3.2), Prop. 3.10]† for this, and [MS §2, Convention "Relative sectors and fixed-limit index"] states it.
- **(I2) Dimensions.**
  - At a regular irreducible solution the unframed moduli space has dimension equal to the index, also when a limit is reducible. Framing an end with limit $\rho$ adds $h^0(\rho)$.
  - Example: the charge-one instanton on $\mathbb R^4$ with a cylindrical end has index $5=8-3+3-3$ and framed dimension $8$.
  - **VERIFIED in model cases.**
- **(I3) Reducibles.** On a piece with $b_1=0$ and only central limits, a reducible has index $8E-3(1+b^+)$ [MS §2, Lemma "Charge and index bookkeeping"; DLME, Lemma 5.6, quoting MMR (82)†]. **VERIFIED as citation.**
- **(I4) Trajectories.** A nonconstant irreducible trajectory has index $\ge1$. Abelian trajectories on $\mathbb R\times Y$ with $b_1(Y)=0$ are flat, hence constant. **VERIFIED.**

### 4.2 The jumping-line representative

**Lemma 4.1.** Let $f\colon\mathbb P^1\to W$ be a smooth map, where $\mathbb P^1$ carries a complex structure $j$, and let $\langle c,f_*[\mathbb P^1]\rangle$ be even. Let $V^j_f$ be the set of $[A]$ for which the index-zero operator $\bar\partial$ on $\big(f^*E\otimes(f^*\det E)^{-1/2}\big)\otimes\mathcal O(-1)$ has a kernel, i.e. for which $f^*E\otimes(\det)^{-1/2}\cong\mathcal O(k)\oplus\mathcal O(-k)$ with $k\ge1$. Then:
1. $V^j_f$ is the zero set of the canonical section of a determinant line with first Chern class $\pm\mu(f)$. It depends only on $f^*A$, and it is closed under $C^0$-convergence of $f^*A$.
2. A connection reducible along $f$ with difference class $v$ lies in $V^j_f$ iff $v\cdot f\ne0$. Near a compact set of such connections with $v\cdot f=0$, the canonical section is bounded away from zero.
3. Under Uhlenbeck convergence, membership is lost only if a point of concentration lies on $f(S^2)$.
4. At a reducible with $v\cdot f\neq0$ and a one-dimensional complex normal slice, the local degree is $\pm v\cdot f/2$.

**VERIFIED.**
- T2 Props. 2.3 and 3.2, Cor. 3.3.
- The Round 3a referee accepted (1)–(3), with the correction that the operator is the index-zero one.
- That $c_1$ of the line is $\pm\mu(f)$ is the families index theorem on $\mathbb P^1$ (T2 Prop. 2.3(a); DK Ch. 5†).

**Lemma 4.2 (nodal degeneration at the $J$-face).** Near $t=-1$, let $j_t$ degenerate $S$, with the annulus $K\times[-R,R]$ in the $J$-neck, to the nodal curve $f_l\cup_pf_r$. Here $f_l=D_l\cup(K\times[0,\infty))\cup\{\infty\}$ maps to the completion $(-C_2)^\wedge$ and represents $F_l$; $f_r$ is defined likewise in $(C_{-2})^\wedge$. Suppose:
- $[A_\nu]\in V^{j_{t_\nu}}_S$ with $t_\nu\to-1$;
- $A_\nu$ converges to $(A_L,A_R)$ matched at $\theta$ on $J$;
- there is no concentration on $S$ and no instanton on the $J$-neck.

Then $A_L\in V_{f_l}$ or $A_R\in V_{f_r}$.

*Proof.*
- On the annulus, $A_\nu$ converges exponentially to $\theta$ up to a constant gluing element $g_\nu\in SU(2)$, because $h^1(\theta)=0$.
- The twisted operators therefore converge to the nodal operator. The twist $\mathcal O(-1)$ degenerates to $\mathcal O(-1)$ on one component and $\mathcal O$ on the other.
- The nodal operator has index $0+2-2=0$ and kernel
$$\{(\sigma_l,\sigma_r):\sigma_l\in H^0(E_l(-1)),\ \sigma_r\in H^0(E_r),\ \sigma_l(p)=g\,\sigma_r(p)\}.$$
  This kernel is zero iff $E_l\cong E_r\cong\mathcal O^2$, for every $g$.
- An invertible limit operator gives invertible operators for large $\nu$.

**Status.** The algebra is VERIFIED (check (G), every $g$ and all splitting types up to $\mathcal O(3)\oplus\mathcal O(-3)$). The convergence of the operators across the long neck is linear gluing of Cauchy–Riemann operators, which is **PLAUSIBLE, standard** (McDuff–Salamon†). With product-form perturbations (D4), the same holds for the perturbed divisors.

**Where Lemma 4.2 and (D5) are used.**
- Lemma 4.2 is needed for limits in which both halves are reducible. Without it, a chain of $b$ copies of $W'$ split along $J$ with trivial halves has total excess $3-b$, which fails the zero-dimensional analysis already at $b=3$ (§5.3).
- (D5) is needed only for the boundary description in Theorem A(3).

### 4.3 The $S^3$-face

**Lemma 4.3.** A limit over $t=-1$ with halves $\zeta_L,\zeta_R$ has $\mathrm{ind}(\zeta)=\mathrm{ind}(\zeta_L)+\mathrm{ind}(\zeta_R)+3$.
- If both halves are irreducible and regular, $\mathrm{ind}\ge3$; with (D5) and the insertion retained, $\mathrm{ind}\ge5$.
- In the moduli spaces of index $\le2$ that define $B$ and prove the chain property, the outer limits are irreducible, so both halves are irreducible, and the face is empty.

**VERIFIED** by (I1) and $h^0(\theta)=3$. The irreducible part of the face would factor through $C(S^3)=0$. Compare DLME, Lemma 5.10, case $i\not\equiv1\pmod3$ (the $S^3$ case, index $\ge2$ there), and T2 Thm. 5.2(a).

### 4.4 The $L(4,1)$-face: the minimal cap

**Lemma 4.4.** Let $\xi\in H^2(N)$ with $\xi(S)=1$, and let $c|_N\in\{0,-4\xi\}$. The reducible caps on $N^\wedge$ have $v=2k\xi$, with energy $E=k^2/4$ and limit $\gamma$ ($k$ odd) or central ($k$ even). For every $k$ their framed index is
$$\delta=\mathrm{ind}+h^0(\text{limit})=8E .$$
Moreover:
- Flat caps miss $V_S$.
- For each $e$, generically the only cap of framed index $\le2$ meeting $V_S$ is the reducible with $|k|=1$: energy $\tfrac14$, limit $\gamma$, $\delta=2$.
- Caps meeting $V_S$ with central limit have $\delta\ge8$.
- Irreducible framed caps of framed index $2$ in $V_S$ would form free $U(1)$-orbits in a zero-dimensional space, so they do not occur generically.

**VERIFIED (index).** Close $N$ up as $\overline{\mathbb{CP}}{}^2=N\cup_{L(4,1)}(-B)$, where $B=D(T^*\mathbb{RP}^2)$ and $S$ is a conic, $S=2h$ (check (F)).
- The reducible with $v=kh$ has complex off-diagonal index $k^2-1$ on $\overline{\mathbb{CP}}{}^2$.
- On $-B$ the off-diagonal line is flat, and its complex index there is $-1$:
  - for $k$ odd it is the twisted line $\epsilon$, with $H^0=H^1=0$ and $H^+(-B;\epsilon)=\mathbb R$. The twisted class of $\mathbb{RP}^2$ has square $-1$ in $B$; the double cover $T^*S^2$ has zero section of square $-2$ and the deck transformation acts by $-1$, so the square is $+1$ in $-B$;
  - for $k$ even it is trivial, and the constants lie in the cokernel.
- The matching term is $0$ at $\gamma$ and $1$ at a central limit.
- Hence the off-diagonal index on $N$ is $k^2-[k\text{ even}]$, the diagonal index is $-1$, and $\delta=-1+2(k^2-[k\text{ even}])+h^0=2k^2=8E$.

This agrees with [MS §3, Lemma "The order-four cap"] and with T2 Ex. 3.5. The draft's check (h) is the case $k=1$.

**VERIFIED as holomorphic algebra, PLAUSIBLE as analysis (regularity and transverse cut).** On $N^\wedge\cong\mathrm{Tot}\,\mathcal O(-4)$ with a Kähler metric that is conformally cylindrical near infinity, the minimal cap is the split bundle $L_1\oplus L_2$ with $L_1|_S=\mathcal O(1)$ and $L_2|_S=\mathcal O(-1)$.
- Its decaying deformations are the extensions $0\to L_2\to E_t\to L_1\to0$, $t\in H^1(\mathbb P^1;\mathcal O(-2))=\mathbb C$. This is the complex normal index $1$; the other direction $H^1(\mathcal O(2))$ vanishes.
- For $t\ne0$ the restriction $E_t|_S$ is the non-split extension of $\mathcal O(1)$ by $\mathcal O(-1)$, which is $\mathcal O\oplus\mathcal O$. So $V_S$ meets the framed normal slice exactly at $t=0$, where the canonical section vanishes to first order (T2 Prop. 2.3(d)). The local degree is $\pm1$ (Lemma 4.1(4)).
- The analytic inputs are the correspondence between this holomorphic description and the framed ASD moduli near the reducible (a Kobayashi–Hitchin correspondence on the orbifold compactification†), and the vanishing of the obstruction. [MS §3, Lemma "The order-four cap"] obtains regularity instead by an equivariant perturbation.

### 4.5 The relative sign, and the chain property of $B$

**Lemma 4.5 (cancellation at the lens face).** Over $t$ near $+1$, the ends of the one-dimensional moduli spaces defining $\Phi_e$ (index $2$) are exactly
$$(\text{rigid irreducible exterior on }W'\setminus N\text{ with limit }\gamma)\times(\text{minimal cap}).$$
Their signed count is $m_eR$, where $m_e=\pm1$ and $R\colon C(Y_2)\to C(Y_{-2})$ counts the rigid exteriors. The exterior moduli spaces for $e=0,1$ coincide, by (D3). There is one sign $s$, independent of the exterior solution, of its limits and of its energy sector, such that $m_1=s\,m_0$ in the induced orientations. Hence $\Phi_0-s\Phi_1$ has no lens ends.

*Proof.*
1. *Only the minimal cap occurs.* The index is $2=\mathrm{ind}_{\rm ext}+\delta$, with $\mathrm{ind}_{\rm ext}\ge0$ and $\delta\ge2$ for caps meeting $V_S$ (Lemma 4.4).
2. *Gluing.* Gluing at $\gamma$, where the framed cap absorbs the stabilizer $U(1)$, gives exactly one end per pair (exterior, crossing) [MS §2, Lemma "Regular matching at an auxiliary reducible end"; D02, Ch. 4†]. **PLAUSIBLE, standard.**
3. *The sign is constant* (PLAUSIBLE, 85–90%).
   - By T2 Lemma 5.1, $E_1\cong E_0\otimes L_y$, with $2y=\mathrm{PD}(S)$; the end identifications are twisted by $\chi$.
   - On $W'\setminus N$ the class $y$ is $2$-torsion, so $L_y$ is flat there. It restricts to $\chi$ on $Y_{\pm2}$ and to the order-two character on $L(4,1)$, which carries $\gamma$ to a Weyl conjugate of $\gamma$.
   - Tensoring by a line bundle acts as the identity on $\mathrm{ad}E$. It therefore identifies the deformation complexes, the determinant lines and the jumping divisors canonically. This gives $\Phi_1=\sigma\iota\Phi_0\iota$ and $\iota R\iota=s'R$.
   - The signs $\sigma$ and $s'$ compare two orientations of a determinant line over a configuration space that is connected in each relative sector: an affine space modulo gauge.
   - Across sectors and limits, they are transported by the I-orientation conventions [KM11 §3.8, Def. 3.9, and the paragraph following it], which are compatible with gluing at the ends. The generator signs are absorbed into $\iota$.
   - So $s=\sigma s'$ is one constant, and $\partial B+B\partial=m_0R-s'^2m_0R=0$ (T2 Thm. 5.2(c)).
   - The same comparison is local at $N$ and commutes with gluing on all other necks [MS §3, Prop. "Local relative signs"]. In $X_M$ the weights therefore have the product form $\varepsilon(e)=\prod\varepsilon_i(e_i)$.

The draft cites KM11 §3.8 for triviality of the determinant lines. That statement is made there in the singular, admissible setting; for the present one cite [D02, §5.4]† or DK†. The conclusion is unaffected.

**Proposition 4.6.** $B$ is an integral chain map. Its chain-homotopy class does not depend on the interval of metrics, the perturbations, or the representative of $\mu(S)$ within (D4).

*Proof.* Count the ends of the one-dimensional moduli spaces (index $2$; index $1$ for a homotopy).
- The Floer breakings give $\partial B\pm B\partial$.
- The $J$-face is empty (Lemma 4.3).
- The lens ends cancel (Lemma 4.5).
- A point of concentration costs $8$ and releases at most $2$ here.
- A breaking through a central flat costs at least $1+3+0=4$, and at least $1+3+0+3+1=8$ if the configuration on $W'$ is reducible. This is the estimate before DLME, Lemma 5.6.

**PLAUSIBLE, 85%.** The framework is KM11 §3.9 and DLME §5.4. The non-standard inputs are Lemmas 4.4 and 4.5.

---

## 5. The excess identity and the estimates on the pieces

### 5.1 The identity

The pieces of $X_M$ are $C_\pm$, the copies $W'_i$ and the copies of $W_H$. Take a sequence in a cut-down moduli space of dimension $d\in\{0,1\}$ over $Q$ (or $Q\times[0,1]$), with $T_\nu\to\infty$. It has an ideal limit $\zeta$ consisting of:
- on each piece $\beta$, a configuration $\zeta_\beta$, possibly broken along $J_i$ or $L_i$, with trajectories on those necks and points of concentration;
- chains of trajectories $\tau$ on the $Y$-necks;
- flat limits throughout.

This is Uhlenbeck–Floer compactness for families of broken metrics [KM11 §3.9, in the non-integral case; D02, Ch. 5†, and DLME §5.3 with reducible cuts]. **PLAUSIBLE, standard.**

Put
$$E_\beta(\zeta)=\mathrm{ind}(\zeta_\beta)+p_\beta-c_\beta ,$$
where:
- $\mathrm{ind}(\zeta_\beta)$ includes $h^0$ at matchings inside $\beta$ and $8$ for each point of concentration;
- $p_\beta=1$ for a copy of $W'$ and $0$ otherwise;
- $c_\beta$ is $2$, $\deg z_\pm$ or $0$.

Then
$$d=\sum_\beta E_\beta(\zeta)+\sum_\tau\mathrm{ind}(\tau)+3\,C_Y(\zeta),$$
where $C_Y$ is the number of matchings at central flats on the $Y$-necks. **VERIFIED**: this is (I1) applied to the closed index, with $\sum p_\beta=n$ and $\sum c_\beta=2n+\deg z$.

### 5.2 Lower bounds on the pieces

The key fact is the energy cost of a met insertion. A reducible class $v$ on $W'$, or on one half of it, satisfies $v\equiv c\pmod 2$, so its evaluations on $F_l$ and $F_r$ are even.
- If $v\cdot S\ne0$, or if a half meets its half-divisor, then $-v^2\ge2$, so $E\ge\tfrac12$ and the index $8E-3$ is $\ge1$.
- If the insertion is not met, a point of concentration lies on $S$ (Lemmas 4.1(3), 4.2), which costs $8$ and releases at most $2$.

| piece and limit | $E_\beta\ge$ | central outer limits forced |
|---|---|---|
| cap, or $W_H$ (fixed generic metric: no reducibles) | $0$ | none |
| $W'$, unbroken, irreducible | $0$ | none |
| $W'$, unbroken, reducible | $8E-4\ge0$ | both |
| $W'$ split along $J$, halves irreducible | $4$ (with (D5)); $2$ (without) | none |
| $W'$ split along $J$, one half reducible | $1$ (with (D5)); $-1$ (without) | that half's |
| $W'$ split along $J$, both halves reducible | $0$ (needs Lemma 4.2); $-4$ (without it) | both |
| $W'$ split along $L$, exterior irreducible | $\mathrm{ind}_{\rm ext}+\delta-1\ge1$ | none |
| $W'$ split along $L$, exterior reducible | $8E-4\ge0$ (since $v\cdot S=\pm2$) | both |

Each nonconstant trajectory on a neck adds at least $1$; each point of concentration adds at least $4$, by (D6) and [FL2b, (3.25)].

**VERIFIED** as index arithmetic (checks (D) and (e)), given Lemmas 4.1–4.4 and regularity of irreducible strata for generic data.
- For the caps, a reducible would have $v\cdot A_\pm$ odd, hence $v\ne0$, and would lie on a wall of codimension $b^+(C_\pm)\ge1$.
- For $W_H$, any reducible class with central limits is odd on $\hat F$ and satisfies $v^2\le-2$ (check (B)). It lies on a wall of codimension one, which a fixed generic metric avoids.
- In a one-parameter deformation of the metric on $W_H$, a wall-crossing reducible has index $8E-6\ge-2$. With the parameter and its two central matchings it costs at least $5>1$, so the map of $W_H$ is metric-independent up to chain homotopy.

### 5.3 Consequences, and why each hypothesis is needed

Every piece whose limit contains a reducible part other than a lens cap has a central outer limit.
- With Lemma 4.2 and (D5), every piece has excess $\ge0$, so $\sum_\beta E_\beta+3C_Y\ge3C_Y$, and $C_Y=0$ whenever $d\le2$ (check (D)(i): the minimum is $3$).
- With Lemma 4.2 alone, the only negative excess is $-1$, for a copy split along $J$ with one reducible half. Such a copy forces a central outer limit, and a central neck borders at most two copies, so the total is $\ge C_Y$. Hence $C_Y=0$ when $d=0$.

**Corollary 5.1.** Part (1) assumes Lemma 4.2; parts (2) and (3) assume also (D5).
1. For $d=0$:
   - every piece is unbroken and rigid;
   - every copy of $W'$ lies over an interior parameter;
   - there are no trajectories and no points of concentration.
2. For $d=1$, exactly one of the following occurs, and otherwise the limit is as in (1):
   - one piece moves in a one-dimensional family;
   - one $Y$-neck carries one index-one trajectory between irreducibles;
   - one copy of $W'$ is at a minimal lens end.
3. No face $t_i=-1$ is reached (for $d=0$ this already follows from Lemma 4.2 alone).

**VERIFIED.** For (1) without (D5): once $C_Y=0$, a copy split along $J$ has excess $\ge2$ and one split along $L$ has excess $\ge1$, so excess $0$ forces an unbroken rigid irreducible solution on every piece.

**The three hypotheses are sharp** (checks (D), (E)).
- **Without Lemma 4.2:** a chain of $b$ copies of $W'$ split along $J$ with trivial halves, with $b+1$ central necks, has total excess $3-b$. At $b=3$ this already admits $d=0$.
- **Without (D5), but with Lemma 4.2:**
  - The total excess is $\ge C_Y$, since each central neck borders at most two copies, each at excess $\ge-1$. The bound is attained: two adjacent copies split along $J$, with reducible halves facing a common central flat and rigid irreducible halves carrying the insertions non-transversally, give total $1$.
  - For $d=0$ this is still a contradiction ($1>0$), so Theorem A(1) and (2) do not need (D5).
  - For $d=1$ it is not, so the draft's direct proof of the boundary description needs (D5). **This is a gap in the draft.**
- **Finite necks inside the positive pieces (Theorem A′):**
  - Here a positive piece has excess $\ge0$ with no central outer limit (and $\ge2$ if it contains a reducible part), $\ge-1$ with one central outer limit, and $\ge-4$ with two [MS §5, Lemma "Local excess, including central outer limits"]. I recomputed this case analysis.
  - At distance $\ge3$, each central neck borders at most one positive piece, and the total is $\ge2>1$.
  - At distance $2$, a chain of $k$ adjacent positive pieces with $k+1$ central necks has total $3-k$. So the spacing hypothesis of Theorem A′ is needed, by this argument at least.

---

## 6. Proofs

### 6.1 Compactness

Fix $\mathfrak D$. For $T_\nu\to\infty$ and points of $\mathcal M^e(\mathfrak D_{T_\nu})$, pass to an ideal limit (§5.1). At the faces of $Q$ the incidence conditions hold in the form of Lemmas 4.1(3) and 4.2. **PLAUSIBLE, standard.**

### 6.2 Theorem A(1)

1. By Corollary 5.1(1), which uses Lemma 4.2 but not (D5), any limit consists of one rigid irreducible solution on each piece, matched at irreducible flats. Each $W'_i$ lies over an interior $t_i$ and is a point of $\Phi_{e_i}$; the caps are points of $\Psi_\pm$; each $W_H$ is a point of $H$.
2. Conversely, such a choice glues, for $T$ large, to exactly one regular point of $\mathcal M^e(\mathfrak D_T)$, oriented by the product orientation. All matchings are at irreducible nondegenerate flats ($h^0=h^1=0$).
   - The relevant gluing theorem is that for families of broken metrics, applied neck by neck to product families: KM11 §3.9, in particular the last display there, valid for separating cuts. Its hypothesis of non-integral cuts is replaced by the index exclusions of §5, as in DLME §5.4.
   - **PLAUSIBLE, standard.**
3. By compactness there are no other points for $T\ge T_0$. There are finitely many choices, so one $T_0$ suffices.
4. The weights factor, and $B=\sum_{e_i}\varepsilon_i(e_i)\Phi_{e_i}$. So $\sum_e\varepsilon(e)\#\mathcal M^e=\varepsilon_0\langle\Psi_+,u^M\Psi_-\rangle$, the matrix product of the chain maps of the pieces.
5. If $8\nmid M$, no bundle has the required energy, so $\Omega_M=0$. The chain-level pairing vanishes by degree, since $\deg u^M\equiv M$ and $\Psi_\pm$ are concentrated in one degree each.

### 6.3 Theorem A(2) and A(3)

**(2).** By (1), $\Omega_M(\mathfrak D_T)=\varepsilon_0\langle\Psi_+,u_{\mathfrak D}^M\Psi_-\rangle$, and the right side depends only on the homology classes:
- $\Psi_-$ is a cycle and $\Psi_+$ a cocycle;
- $B$ is a chain map, invariant up to homotopy (Prop. 4.6);
- so is $H$ (§5.2);
- $\phi_*$ is an isomorphism of complexes.

This is the proof I adopt. It uses only zero-dimensional moduli spaces on $X_M$.

**(3).** Assume (D5). Along a generic path $\mathfrak D_s$ with $T\ge T_0$ (uniform, by compactness of $[0,1]$), consider the one-dimensional moduli spaces at fixed $T$. If ends of any other kind than those listed existed for arbitrarily large $T$, a diagonal limit would contradict Corollary 5.1(2)–(3). Hence:
- **Faces $t_i=-1$: no ends.** With both halves irreducible the excess is $\ge4$. With a reducible half there is a central $Y$-neck, which costs $3$ on top of an excess $\ge0$, using (D5) and Lemma 4.2.
- **Faces $t_i=+1$.** The only ends are (rigid solution on $X_M\setminus N_i$ with limit $\gamma$) $\times$ (minimal cap). The exterior spaces for $e$ and $e+e_i$ coincide: same bundle off $N_i$, same data by (D3) and (D4). Their weighted signs are opposite by Lemma 4.5 and its locality, so they cancel.
- **Bubbling:** excess $\ge4$, so none.
- **$Y$-necks:** at finite $T$ these are not broken, and a trajectory in the limit is an interior point.

### 6.4 Theorem A(4)

Corollary 5.1 uses only the lower bounds of §5.2 for each kind of piece, and that a piece with a reducible part other than a lens cap has a central outer limit. Both hold for any composite word. Prop. 1.2(3) and the energy count hold for any word as well (§1.2). **VERIFIED as logic.**

### 6.5 Theorem A′

Replace each composite $W'_a\cup W_H\cup W'_{a+1}$ by a single piece with a two-parameter family, finite internal necks and the prescribed metrics.
- Its count with irreducible outer limits is chain homotopic to $BHB$ [MS §5, the proposition identifying the two-parameter count with $BHB$, proved by stretching its three internal three-manifolds].
- In the long-neck limit, the excess of this piece obeys the bounds quoted in §5.3, which rest on [MS §5, Lemmas "Local charge costs" and "Local excess, including central outer limits"]. The first gives energy $\ge\tfrac12$ for a reducible containing the positive cell, by parity of $v^2$ and an odd sphere $\pm(T_2-T_1)$; I re-verified the parity (§10.2).
- With spacing $\ge3$ the total excess is $\ge2$ once a neck is central (check (E)). Corollary 5.1(1) then holds, and the argument of §6.2 applies.

This is [MS §5, Prop. "Closed composition in the final metrics"], whose final estimate "$3S-2A\ge S$" suffices for $d=0$. The sharper bound $-1$ for one central outer limit is needed only for one-dimensional moduli spaces. **PLAUSIBLE, 70%.**

### 6.6 Corollary B and Proposition C

**Corollary B.**
1. Under the hypotheses, $u$ is invertible on $L(Y_2)\otimes\mathbb Z_{(2)}$.
2. For $M\in e_N\mathbb Z$, $u^M\equiv1$ on $L/2^N$. Since $\Psi_+$ kills torsion, $\langle\Psi_+,u^M\Psi_-\rangle\equiv q\pmod{2^N}$.
3. $8\mid e_N$: $u$ is homogeneous of degree $1$ on the $\mathbb Z/8$-graded free module $L$. If $u^k\equiv1\pmod{2^N}$ with $8\nmid k$, then every graded piece $L_j$ satisfies $L_j\subset2^NL_j$, so $L=0$ (check (H)).
4. Theorem A(1) converts the congruence into one for $\Omega_M$.

**Proposition C.**
- (1) is Donaldson's connected-sum theorem (D90†; DK §9.3†) and its Seiberg–Witten analogue, applied along $J_1$. Note $b^+(X_M)\ge3$.
- (2) is the dimension count of §1.2.

---

## 7. Reducibles, and the standard results that suffice

### 7.1 Where reducibles need care

| reducible | where | treatment | glued? |
|---|---|---|---|
| $\theta$ on $J_i\cong S^3$ ($h^0=3$) | faces $t_i=-1$ | Excluded by index: matching adds $3$, plus $1$ for the lost parameter. The irreducible part factors through $C(S^3)=0$. Reducible halves have central outer limits and are paid for by the energy of a met half-insertion (Lemma 4.2). | never |
| $\pm\theta$ on $L_i$ ($h^0=3$) | faces $t_i=+1$ | Caps meeting $V_S$ with central limit have $\delta\ge8$; flat caps miss $V_S$. | never |
| $\gamma$ on $L_i$ (stabilizer $U(1)$, $h^0=1$) | faces $t_i=+1$ | The minimal cap ($E=\tfrac14$, $\delta=2$) gives genuine ends of excess $1$. They are glued with the stabilizer absorbed by the framed cap, cut by $V_S$ with degree $\pm1$, and cancel in the weighted sum. | yes, at a regular framed reducible cap |
| $\theta,\chi\theta$ on $Y_{\pm2}$ ($h^0=3$) | $Y$-necks as $T\to\infty$ | Each matching costs $3$; every piece has excess $\ge0$, including the reducibles on copies of $W'$, which exist for all metrics. | never |
| reducibles on pieces | $W'$ always; $W_H$ and caps on walls | $W'$: energy of a met insertion. $W_H$, caps: odd determinant on $\hat F$, resp. $A_\pm$, and fixed generic metrics. | never |
| $\theta$ on $Y_{\pm1}$; $Y_0$ | inside $W_H$, never stretched | Only through $H\simeq f_+f_-$: composition through $Y_{\pm1}$ costs $3$ at $\theta$; $Y_0$ is admissible. | never |

A non-central reducible flat on a $Y$-neck (stabilizer $U(1)$) would cost only $1$, and the argument would fail. $S^3_{\pm p}(K)$ with $p\ge3$ has such flats, e.g. $\mathrm{diag}(\zeta,\zeta^{-1})$ with $\zeta$ a primitive $p$-th root of unity. **VERIFIED.**

### 7.2 Standard results used, with citations

1. **Floer's instanton homology over $\mathbb Z$** for $Y_{\pm2}$, with central nondegenerate reducibles, and cobordism maps for $b_1=0$.
   - [D02, Chs. 2–5]† (integer homology spheres); the determinant-one convention, KSE §7.1 (VERIFIED: admissible bundles only); Ghosh–Sivek–Zentner, Thm. 2.3†, as cited by [MS §2].
   - The grading and degree conventions are those of DLME's proof of Prop. 3.4 (VERIFIED), extended to $b^+=1$.
   - **PLAUSIBLE.**
2. **Families of broken metrics.**
   - KM11 §3.9 (VERIFIED by reading): the genericity Prop. 3.10, the boundary formula $m_{\partial G}+(-1)^{\dim G}m_G\partial=\partial m_G$, the face formula $m_{G_j}=(-1)^{\dim G''_j\dim G'_j}m''_j\circ m'_j$ (last display of §3.9), and compactness in dimension $<4$.
   - Its standing hypotheses are that cuts satisfy the non-integral condition and, for the face formula, that they separate the ends. Here the formula is applied only at the separating $Y$-necks with irreducible limits. The reducible cuts are handled by the index exclusions of §5, following DLME's general principle (§5.4, before Prop. 5.8; VERIFIED) and the index bounds of DLME Lemmas 5.5, 5.6 and 5.10 (VERIFIED).
3. **Index additivity** with $h^0$ at matchings, and the index of reducibles: [D02, (3.2), Prop. 3.10]† and MMR (82)†, both as quoted by DLME (VERIFIED as citations: proof of Prop. 3.4 and Lemma 5.6).
4. **Gluing at irreducible nondegenerate limits** in families: [D02, Ch. 4]†; KM11 §3.9. **PLAUSIBLE, standard.** The identification $H\simeq f_+f_-$ is this result plus the cost $3$ of $\theta$ on $Y_{\pm1}$.
5. **Gluing at a flat with stabilizer $U(1)$** against a regular framed reducible cap: [MS §2, Lemma "Regular matching at an auxiliary reducible end"] (read); D02†; MMR†. **PLAUSIBLE.**
6. **Determinant-line orientations, excision, and I-orientations:** KM11 §3.8, Def. 3.9 (VERIFIED as a definition); [D02, §5.4, Prop. 5.11, §5.6]†, as cited by the manuscript. **PLAUSIBLE.**
7. **The jumping-line representative of $\mu(S)$:** Birkhoff–Grothendieck, and the determinant line of the coupled $\bar\partial$-operator [D90†; DK Ch. 5†]. VERIFIED for the properties used (T2; Round 3a report).
8. **Intersection suitability:** [FL2b, (3.25)], the inequality $\sum_{x\in U_i}(4-\dim\beta_i)\le4$. VERIFIED: equation counter recomputed from the source.
9. **Linear gluing of Cauchy–Riemann operators** on degenerating rational curves, for Lemma 4.2: McDuff–Salamon†. **PLAUSIBLE.**
10. **Donaldson's connected-sum theorem**, for Proposition C only: D90†, DK §9.3†.

**Not needed:** gluing at central reducibles, obstructed gluing, Kuranishi models at reducibles, the family adjunction inequality, the clamp (for Theorem A), and anything from Feehan–Leness beyond (3.25).

---

## 8. Gaps, in order of weight

1. **Gap 1: the integral relative sign** (Lemma 4.5(3); [MS §3, Prop. "Local relative signs"]).
   - The argument is the canonical identification of determinant lines under tensoring by a line bundle, connectedness of each relative sector, and I-orientation transport across sectors.
   - The points not written out are the effect of the Weyl conjugation of $\gamma$ on the cap's framed determinant line, and the bookkeeping of generator signs in $\iota$.
   - DLME's analogue is only over $\mathbb F_2$. If this failed, $B$ would be a chain map only modulo $2$, which is useless against the factor $2^{n_D-1}$.
   - **PLAUSIBLE, 85–90%.**
2. **Gap 2: the minimal cap** — regularity of the framed reducible, and the transverse cut by $V_S$.
   - The index is VERIFIED for all charges.
   - The transverse cut is VERIFIED in the holomorphic model; transferring it to the ASD setting needs a Kobayashi–Hitchin correspondence on the orbifold compactification and a comparison of decay conditions, or the manuscript's equivariant perturbation.
   - **PLAUSIBLE, 90%.**
3. **Gap 3: nodal degeneration of $V_S$ (Lemma 4.2), and the face condition (D5).**
   - The algebra is VERIFIED; the linear gluing is PLAUSIBLE.
   - (D5) is a genericity statement for perturbations in model form near the face. It is needed only for Theorem A(3), and was missing from the draft.
   - **PLAUSIBLE, 85–90%.**
4. **Gap 4: standard analysis.**
   - Floer theory over $\mathbb Z$ for $Y_{\pm2}$ with central reducibles.
   - Compactness and gluing for families of broken metrics whose cuts carry reducibles (several necks at once, with corners $T=\infty$, $t_i=\pm1$).
   - Transversality of the cut-down spaces for the jumping-line representatives.
   - None of this is in the cited sources in the generality needed; all of it is standard in kind.
   - **PLAUSIBLE, 90%.**
5. **Gap 5 (Theorem A′ only): the manuscript's local analysis of the positive piece** with finite necks and prescribed metrics: [MS §5, Lemmas "Local charge costs", "Local excess" and the identification with $BHB$]. I recomputed the case analysis, not the analytic inputs. **PLAUSIBLE, 75%.**
6. **Interface with the vanishing side.**
   - Theorem A′ fixes the number $\Omega_M$ only for data with long external $Y$-necks.
   - The vanishing hypothesis (F) must be established for such data, or else invariance under shortening those necks must be proved. The latter is not claimed here; it would need inequalities on chains of pieces or obstructed gluing.
   - This is not a gap in Theorem A, but it constrains how (F) is stated.

**Not claimed.**
- Invariance for short $Y$-necks.
- That $B$ is invertible modulo two.
- That $D_{X_B}=0$ for the rational blow-down; this is C-closed §2.6, conditional on Witten's conjecture.

---

## 9. Verdict and confidence

The statement asked for is a theorem of classical type, and the draft proves it in essentially the right way.
- **What it is.** It is the closed, capped form of the Kronheimer–Mrowka composition law for families of broken metrics, applied to a product of intervals whose faces contribute nothing in the weighted sum.
- **What it needs:**
  - Floer's theory for $Y_{\pm2}$, where all reducibles are central;
  - gluing at irreducible limits;
  - one gluing at a $U(1)$-reducible minimal cap on $\nu S$;
  - the energy of a met $\mu(S)$ on a single copy of $W'$, with its nodal persistence;
  - an integral comparison of orientations between $c$ and $c+\mathrm{PD}(S)$.
- **Long necks.** Taking every $Y_{\pm2}$-neck long removes all dependence on inequalities for chains of pieces and on the clamp.
- **Secondary nature.** $X_M$ is a connected sum along the $J_i$ with $b^+>0$ on both sides, so all its primary invariants vanish. $B$ is the difference of the two null-homotopies of the weighted operation $\mu(S)\cdot W'_*$: one through $I(S^3)=0$, the other through the cancellation over $c$ and $c+\mathrm{PD}(S)$.

**Corrections made.**
- The boundary description needs the face condition (D5); the identity and the invariance do not.
- Several citations overstate what KM11, DLME and KSE cover.
- Corollary B needs $H$ as well as $B$.
- The version used downstream is Theorem A′, which needs spacing $\ge3$ and the manuscript's local analysis.

**Confidence.**
- Theorem A (long necks): **80% over $\mathbb Z$; 88% over $\mathbb F_2$.**
- Theorem A′ (finite necks inside the positive pieces, spacing $\ge3$): **70%.**
- Corollary B: VERIFIED given Theorem A and invertibility of $B$ and $H$ on free parts localized at $2$. The hypothesis on $B$ remains "expected".
- Proposition C: 95%.
- **For the statement as a whole (Theorem A with Corollary B and Proposition C, as stated in §2): 80%.**

---

## 10. Report of the checks

### 10.1 Citations checked against the sources

| cited | source and location | finding |
|---|---|---|
| I-orientation | KM11 §3.8, Def. 3.9 (counter recomputed: Def. 3.1, Props. 3.2, 3.3, Lemma 3.4, Prop. 3.5, Hyp. 3.6, Def. 3.7, Prop. 3.8, **Def. 3.9**, Prop. 3.10) | correct |
| families of broken metrics, face formula | KM11 §3.9: Prop. 3.10 (genericity); boundary formula; face formula in the last display | correct, but the section assumes non-integral cuts and separating cuts for the face formula; the draft's "stated there for bundles without reducibles" is right, but the non-separating lens cut is outside it |
| determinant lines trivial | KM11 §3.8, first paragraph | correct for their singular setting; for ours cite D02 §5.4† |
| Floer framework for $Y_{\pm2}$ | DLME Prop. 3.1 | **incorrect attribution**: Prop. 3.1 concerns integer homology spheres and admissible homology $S^1\times S^2$ |
| degree convention | DLME, proof of Prop. 3.4 ($D=-2c^2$, $b_1=b^+=0$, integer homology spheres) | correct, extended here to $b^+=1$ and rational homology spheres |
| $g_1$ | DLME Prop. 3.10 (counter: Props. 3.1, 3.2, Rem. 3.3, Prop. 3.4, Rem. 3.5, Def. 3.6, Ex. 3.7, Props. 3.8, 3.9, **3.10**) | correct; **over $\mathbb F_2$** |
| boundary relation of $g_1$ | DLME Prop. 5.11, with Lemma 5.10 (`g-bdry1`) | correct; cancellation of $\mathbb{RP}^3$-faces at chain level, over $\mathbb F_2$ |
| MMR (82) | DLME Lemma 5.6 (`min-index`) | correct as quoted ($b_1(W)=0$; $\rho=0$ on $S^3$, $\mathbb{RP}^3$) |
| estimate $i(A)\ge8+i(A_W)$ | DLME, before Lemma 5.6 | correct |
| "general principle" | DLME §5.4, first paragraph, before Prop. 5.8 | **draft says §5.3**; minor |
| [D02, (3.2), Prop. 3.10] | as cited in DLME's proof of Prop. 3.4 | citation chain correct; D02 itself not available† |
| intersection-suitable | FL2b (3.25) (equation counter recomputed: (3.24) is the bound $\le5$, (3.25) the bound $\le4$) | correct |
| determinant-one convention | KSE §7.1 | treats admissible bundles only |
| [MS §2] Convention "Relative sectors and fixed-limit index"; Lemmas "Regular matching at an auxiliary reducible end", "The primary central-group estimate", "Reducibles at the ordinary ends" | `02-ordinary.tex` | read; consistent with the use made here |
| [MS §3] Lemma "The order-four cap"; Props. "Local relative signs", "Chain property and invariance" | `03-negative.tex` | read; $\delta=2$ re-derived independently; sign argument summarized in Lemma 4.5 |
| [MS §5] Prop. "Cell lattices"; Lemmas "Existence and restrictions of the lifts", "Local charge costs", "Local excess"; Props. "Closed composition", the $BHB$ identification; Lemma "The finite-lattice argument" | `05-*.tex` | lattices and parities re-verified; case analysis of local excess recomputed (check (E)) |
| T2 Props. 2.3, 3.2; Cor. 3.3; Lemma 5.1; Thm. 5.2 | `notes/T2-mu-classes.md` | read; used as stated |
| C-closed §§1.1, 1.3, 2.5, 2.6 | `notes/C-closed.md` | §1.1 decomposition and §2.5 degree mismatch correct; §2.6 conditional on Witten's conjecture |

### 10.2 Computations

**My checks: `round3/gluing-final-checks/checks_final.py`. All pass.**
- **(A)** $W'$ lattice; $\mathrm{PD}(S)=2y$; $P$ unimodular; $c_0^2=0$, $c_0(F_r)=c_0(F'_l)=0$, $c_0(F_0)=1$. $F_r\equiv F'_l\pmod2$ in a negative cell but not in $P$.
- **(B)** For all four choices of $(e_j,e_{j+1})$, every reducible class on $W_H$ with central limits is odd on $F_0$, and every such class with $v^2<0$ has $v^2\le-2$, so $E\ge\tfrac12$.
  - My first version took the maximum over all $v$, including $v^2\ge0$, and failed. Such classes are never anti-self-dual; the corrected check agrees with the drafter's (b).
- **(C)** $\mathrm{PD}(S_i)\bmod2$ is independent for 300 random composite words. Only the outer classes and the vector $(1,1)$ in each cell are used.
- **(D)** Exhaustive minimization of the total excess over chains of pieces with at least one central $Y$-neck:
  - with Lemma 4.2 and (D5): minimum $3$;
  - with Lemma 4.2, without (D5): minimum $1$, attained by two adjacent copies of $W'$ split along $J$;
  - without Lemma 4.2: $3-b$ for $b=1,\dots,8$ copies.
- **(E)** The positive-piece model with finite internal necks:
  - the local minima are $0$ (no central limit; $2$ if a reducible part is present), $-1$ (one) and $-4$ (two);
  - the global minimum with a central neck is $2$ at spacing $4$ and $3$, and $3-k$ for $k$ adjacent positive pieces at spacing $2$.
- **(F)** Framed index of every reducible cap on $\nu S$ by closing up in $\overline{\mathbb{CP}}{}^2$: $\delta=2k^2=8E$ for $k=0,\dots,8$; $\delta=2$ at $k=1$ and $\delta=8$ at $k=2$.
- **(G)** Nodal operator: the kernel vanishes iff both components are trivial, for all splitting types up to $\mathcal O(3)\oplus\mathcal O(-3)$ and for random gluing elements.
- **(H)**
  - $\deg B\equiv-1$ for both lifts, $\deg H\equiv-3$, $\deg u\equiv1\pmod 8$.
  - $8(\kappa-\kappa_0)=n+3m$, consistent with the degree count.
  - For 40 random degree-one automorphisms of $\mathbb Z/8$-graded free modules, the order modulo $2^N$ ($N\le3$) is divisible by $8$.

**The drafter's checks** (`round3/gluing_checks/checks.py`, items (a)–(h)) were repeated and all pass. Item (e) contains the draft's bound "$\ge1$" for a copy split along $J$ with one reducible half, which presupposes (D5); with the weaker regularity it is $-1$, see (D) above.

### 10.3 Attempted counterexamples

1. **Chains of copies of $W'$ split along $J$ with trivial halves.** A counterexample if the insertion were not forced onto a half. Excluded by Lemma 4.2; the algebra is verified.
2. **Two adjacent copies split along $J$, reducible halves facing a central flat.** A genuine counterexample to the draft's one-dimensional analysis as written. Excluded by (D5); harmless for the identity and for invariance.
3. **Adjacent positive pieces with finite internal necks.** A counterexample to Theorem A′ at spacing $2$. Excluded by the spacing hypothesis.
4. **Wall-crossing on $W_H$.** A reducible on a wall with its two central matchings costs $\ge5>1$. No counterexample.
5. **Non-minimal or central-limit lens caps; irreducible caps of framed index $2$ in $V_S$.** $\delta\ge8$ for central limits, and free $U(1)$-orbits for irreducibles. No counterexample.
6. **Dependence of the relative sign on the exterior, its limits or its sector.** Ruled out by canonical identifications and I-orientation transport (Gap 1). No counterexample found.
7. **Replacing $B$ by a map of the rational blow-down.** Impossible by parity of degrees (C-closed §2.5): $\deg B$ is odd, while every map of $W'_B$ has even degree.
8. **Conflict with Proposition C.** None. $\Omega_M$ is not a count over a closed family, and its two kinds of face terms vanish for different reasons.
9. **Non-central flats on the $Y$-necks.** For $\pm p$ with $p\ge3$ they exist and would cost only $1$. This explains why the argument is specific to $\pm2$, and does not affect it.

### 10.4 Itemized corrections to the draft

1. **Theorem A(1), boundary description.** Add (D5) to the admissible data. The bound "$\ge1$" for a copy split along $J$ with one reducible half is false without it; it is $-1$. Prove invariance from the gluing identity: the draft's "second proof", made primary here.
2. **Definition 1.3.**
   - Add that the equation data on $W'_i$ coincide for $e_i=0,1$ off $N_i$.
   - Add that the representatives are tensor-paired at the lens face and in product form near the $J$-face.
   - Allow equivariant perturbation of $V_S$ near the minimal cap, contrary to the draft's "supported away from the reducible locus".
3. **§1.3 and §7.2(1).** DLME Prop. 3.1 does not cover $Y_{\pm2}$. Cite [D02]† for integer homology spheres, KSE §7.1 for the determinant-one convention, and Ghosh–Sivek–Zentner, Thm. 2.3† as in [MS §2].
4. **§7.2(2).** DLME's general principle is in §5.4. KM11 §3.9 assumes non-integral cuts, and its face formula is for separating cuts. Say so, and use the formula only at the $Y$-necks.
5. **§3.4.** DLME's $g_1$ and its face cancellation are over $\mathbb F_2$. The integral cancellation is new and is the content of Gap 1.
6. **Lemma 4.5(3).** The triviality of determinant lines in KM11 §3.8 is stated for the singular setting; cite D02 §5.4† instead. The argument is unchanged.
7. **Corollary B.** Assume odd determinant on free parts for $H$ as well as for $B$, and state that $B$ is the map of §1.3.
8. **§7.1 table, $W_H$ row.** The wall-crossing cost is $\ge5$, not $\ge4$. Harmless.
9. **Remark 6.4 becomes Theorem A′.**
   - It is the version used downstream.
   - Its dependence on the manuscript's local analysis and its need for spacing $\ge3$ are now explicit, with the counterexample at spacing $2$.
   - The remarks "no clamp, no spacing" apply to Theorem A only.
10. **Lemma 4.4.** $\delta=8E$ is now verified for every reducible cap, not only $k=1$. Regularity and the transverse cut of the minimal cap are verified in the holomorphic model.
