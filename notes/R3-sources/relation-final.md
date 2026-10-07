# A Feehan–Leness vanishing theorem for families of metrics over a cube, and the exclusion of Seiberg–Witten strata for $(\phi_*B)^3HB$

*Round 3, referee's final version. It replaces `relation-draft1.md` and `relation-draft2.md`. The report of my checks is at the end (Appendix).*

**Labels.** Every claim carries one label.
- **VERIFIED**: proved here; or read in the source with the theorem or equation number recomputed from the LaTeX counters; or checked by an exact computation of mine (Appendix, files in `round3/relation-final-checks/`).
- **PLAUSIBLE**: standard in kind, or supported by a written argument (usually the manuscript's) whose structure I checked but which I did not verify line by line.
- **SPECULATIVE**: rests on an unproved statement, or is a guess.

**Sources and numbering.** FL1 = dg-ga/9710032 (*PU(2) monopoles. I*); FL2a = math/0007190 (*PU(2) monopoles and links of top-level Seiberg–Witten moduli spaces*); FL2b = dg-ga/9712005 (*PU(2) monopoles. II*); FL3 = math/9907107 (*PU(2) monopoles. III: existence of gluing and obstruction maps*); Memoir = math/0203047 (Mem. AMS 256, no. 1226); FL6 = math/0609530. The source list given to the drafters calls math/9907107 "FL2a"; that is wrong, and Draft 2 is right to say so (VERIFIED from the titles in the LaTeX). "Strategy" is `strategy.tex`; its Theorem 2.1 is the closed prototype. "The manuscript" is `src/01`–`10`, cited by its internal labels.

**Notation.** Feehan and Leness's $n_a$ is the $n_D$ of `strategy.tex`. $Y_r=S^3_r(K)$; $\phi\colon Y_{-2}\to Y_2$ is the putative orientation-preserving diffeomorphism; $u=(\phi_*B)^3HB$. A piece of $X_M$ is *negative* ($N=X_{-2}(K)\cup_\phi(-X_2(K))$, form $\langle-1\rangle^2$) or *positive* ($P=X_{-2}(K)\cup W_H\cup(-X_2(K))\cong\mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2$). Field types of a main component of an ideal limit are written F (free: irreducible, $\Phi\not\equiv0$), A (anti-self-dual: irreducible, $\Phi\equiv0$), S (Seiberg–Witten: reducible, $\Phi\not\equiv0$ in one summand) and R (abelian instanton: reducible, $\Phi\equiv0$).

---

## 0. Summary

1. **The relation (Theorem A, §2).** Over the cube $Q=[-1,1]^n$ of metrics whose faces stretch the 3-spheres $J_i$ and the lens spaces $\partial\nu(S_i)\cong L(4,1)$, sum the cut-down instanton counts with signs over the $2^n$ spin$^u$ structures $\mathfrak t_e$, $w_e=w_0+\sum_ie_i\,\mathrm{PD}[S_i]$, to get $\Omega$. If $n_a\ge1$ and the closure over $\bar Q$ of the one-dimensional cut-down space $\mathcal Z_e=\mathcal V(z)\cap\mathcal W^{n_a-1}\cap\mathcal M^{*,0}_{\mathfrak t_e}(Q)/S^1$ contains no ideal limit with a main component of type S or R, then $2^{n_a-1}\Omega=0$. This holds under six analytic hypotheses (A1)–(A6), stated in §2.1, and the finiteness (E0) of the cut-down instanton spaces in the interior of the cube. The deduction is VERIFIED; the hypotheses are PLAUSIBLE, and one of them, coupled regularity, is new.
2. **The family-specific content (§1.5, §3).** (i) Faces split $X$ along $S^3$ and $L(4,1)$; each piece of each face has its own Seiberg–Witten strata $\iota(M_{\mathfrak s})\times\mathrm{Sym}^\ell$, whose levels are not controlled by the total charge. (ii) The inequality needed on a segment $\Gamma$ of reducible components between broken necks is $8\kappa_\Gamma-3m+L-2s\ge-3$ when the limit has no free component, and $r+6\kappa_\Gamma-m+\Delta-2s\ge-2$ on segments of abelian instantons next to a free component ($6\kappa_\Gamma-m+L-2s+\Delta\ge-2$ suffices if the perturbations are local in the parameters). (iii) Abelian instantons with zero spinor exist on negative segments for every value of the parameters and cannot be made regular; one must either glue at them (open) or use the *necessary projection* (new, PLAUSIBLE).
3. **The exclusion (Theorem C, §4).** For $X_M$ built from $u$ and $M$ large, the hypothesis of Theorem A holds, given three inputs: the jumping-line incidence, the control of Seiberg–Witten classes on $P$, and the cap estimates. The proof is the family adjunction inequality $\kappa_\Gamma\ge\frac12(s^-(\Gamma)+m(\Gamma))$ plus the numerology. The deduction and all the arithmetic are VERIFIED.
4. **Corrections to the drafts (§5).** Draft 1's exact minimization of segment charges omits a parity condition on negative pieces; its lower bounds stand, but its claim that the closed forms are attained is false when the spacing $k$ and the number $m$ of positive pieces are both even (the true minima are one higher, as Draft 2 says). Draft 2 cites the misprint $\chi+2\sigma$ as FL2b (3.20); it is in (3.21). Both drafts state the regularity of the cut-down instanton count as an analytic hypothesis; part of it is an exclusion that follows from the same segment inequalities, and I state it so.
5. **The single hardest point** is the necessary projection at mixed limits together with the coupled regularity on which it rests (§3.4, §6).
6. **Verdict.** The statement is correct as a conditional theorem: Theorem A follows from (A1)–(A6) and (E0), Theorem B (which also yields the exclusion part of (E0)) from (A1)–(A7) and the five conditions (B1)–(B5), and Theorem C from Theorem B and three inputs. Confidence that, by this route, $2^{n_a-1}\Omega(X_M)=0$ for large $M$: **about 30%** (range 25–35%).

---

## 1. Setting

### 1.1 Cube data

Let $X$ be a closed, oriented, smooth four-manifold with $\pi_1(X)=1$ and $b^+(X)\ge1$.

- **Necks.** $J_1,\dots,J_n\subset X$ are disjoint separating 3-spheres, ordered so that $X\setminus\bigcup J_i$ has components $Z_0,\dots,Z_n$ with $J_i$ between $Z_{i-1}$ and $Z_i$. Write $\hat Z_j$ for $Z_j$ closed up by balls. Each $\hat Z_j$ is simply connected.
- **Spheres.** $S_1,\dots,S_n$ are disjoint embedded spheres with $S_i\cdot S_i=-4$, $S_i\cap J_j=\emptyset$ for $j\ne i$, and $S_i\cap J_i$ a knot. Write $[S_i]=F_{l,i}-F_{r,i}$ with $F_{l,i}\in H_2(\hat Z_{i-1})$, $F_{r,i}\in H_2(\hat Z_i)$ the classes of the two halves capped off in the balls (by maps of spheres), each of square $-2$.
- **Lens neighbourhoods.** $\nu_i\supset S_i$ are disjoint tubular neighbourhoods, $\partial\nu_i\cong L(4,1)$, $\nu_i\cap J_j=\emptyset$ for $j\ne i$.
- **Splitting.** $H^2(X;\mathbb Z)=\bigoplus_jH^2(\hat Z_j;\mathbb Z)$, orthogonally and torsion free. VERIFIED (Mayer–Vietoris across homology spheres).
- **Metrics.** A smooth family $g_t$, $t\in Q=[-1,1]^n$, with product structure near faces and corners. As $t_i\to-1$ a round cylinder $J_i\times[-T,T]$ is stretched; as $t_i\to+1$ a cylinder $\partial\nu_i\times[-T,T]$ carrying a fixed metric of positive scalar curvature is stretched; no other length tends to infinity. Since $\nu_i$ meets $J_i$, the two ends of the $i$-th interval are never stretched together. **Locality:** over a face, the limiting metric on a component depends only on the parameters of the unbroken necks inside it. This is manuscript Thm. `geometry:family`(i). PLAUSIBLE (construction of §6 of the manuscript).

**The example.** $X_M$ caps the composite $C_-\cup(\phi_*B)^{p_-}\cup u^M\cup(\phi_*B)^{p_+}\cup C_+$. The $J_i$ are the middle 3-spheres of the copies of $W'=(-X_2(K))\cup_{S^3}X_{-2}(K)$, and $S_i$ is the union of the cores of their two 2-handles. There are $n=4M+p$ spheres ($p=p_-+p_+$) and $m=M$ positive pieces at mutual distance exactly $4$; all other inner pieces are negative. On $N$, $F_r=a+b$ and $F_l=a-b$ in the basis of $\langle-1\rangle^2$; on $P$, with form $\left(\begin{smallmatrix}2&1\\1&0\end{smallmatrix}\right)\oplus\langle-1\rangle^4$ on $G,U,T_1,\dots,T_4$, $F_r=G-\sum T_b$ and $F_l=G-2U$, and the square-zero sphere $U$ meets each adjacent sphere once. The caps $C_\pm$ are simply connected, have $b^+\ge1$, are blown up once more (exceptional classes $E_\pm$), and contain classes $A_\pm$ of square zero. The lattice data are VERIFIED (`f1_lattice.py`); $P\cong\mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2$ for every $K$ and $\pi_1(X_M)=1$ are VERIFIED by reading `notes/C-closed.md` §1.2 (Kirby calculus and van Kampen; simple connectivity of $C_\pm$ is assumed there).

### 1.2 Spin$^u$ structures

For $e\in\{0,1\}^n$ put $\mathfrak t_e=(\rho,W\otimes E_e)$ with
$$w_e=c_1(E_e)=w_0+\sum_ie_i\,\mathrm{PD}[S_i],\qquad \Lambda_e=c_1(\mathfrak t_e)=c_1(W^+)+w_e,\qquad p_1(\mathfrak t_e)=-4\kappa\ \text{ for all }e,$$
where $\langle w_0,S_i\rangle=0$, $\langle\Lambda_0,S_i\rangle=2$, $w_0$ is even on every half $F_{l,i},F_{r,i}$, and $w_0$ is odd on some class orthogonal to all $S_i$ (in $X_M$, on $A_\pm$). In Feehan and Leness's notation
$$d_a=-2p_1-\tfrac32(\chi+\sigma)=8\kappa-3(1+b^+),\qquad n_a=\tfrac14(p_1+\Lambda^2-\sigma)=\Theta-\kappa,\qquad\Theta=\tfrac14(\Lambda^2-\sigma).$$
These are Memoir (2.1.12) and FL2b (3.20)–(3.21). FL2b (3.21) as posted prints $\chi+2\sigma$, a misprint: FL2b's own §4.6 (proofs of the main theorems) uses $\chi+\sigma$, as do (3.30) and the Memoir. VERIFIED.

**Lemma 1.1.**
- (a) $\Lambda_e^2=\Lambda_0^2$ and $w_e^2=w_0^2-4|e|$, so $d_a$ and $n_a$ do not depend on $e$. Conversely, if $n_a$ is constant over the $2^n$ bundles then $\langle\Lambda_0,S_i\rangle=2$.
- (b) The classes $w_e\bmod2$ are pairwise distinct.
- (c) Each $w_e\bmod2$ is good (FL2b Def. 3.20), and no $\mathrm{SO}(3)$ bundle with $w_2=w_e$ carries a flat connection (FL2a Lemma 3.2, the Morgan–Mrowka criterion; spherical classes exist since $\pi_1=1$).
- (d) $w_e$ is even on every half.

*Proof.* (a) $\Lambda_e^2-\Lambda_0^2=\sum_ie_i(2\langle\Lambda_0,S_i\rangle+S_i^2)$ since $S_i\cdot S_j=0$ for $i\ne j$; this vanishes for all $e$ iff $\langle\Lambda_0,S_i\rangle=2$. (b) On $\hat Z_0$, $\sum_{i\in I}\mathrm{PD}[S_i]$ restricts to $[1\in I]\,\mathrm{PD}(F_{l,1})$, nonzero mod 2 because a class of square $-2$ is not divisible by 2. On a negative piece $F_l\equiv F_r\pmod 2$ (their difference is $-2b$), so the restriction determines $e_j+e_{j+1}\bmod2$; on a positive piece $F_l\not\equiv F_r$ and both are nonzero mod 2. Induction from the left recovers $e$. (c) $H^2(X;\mathbb Z)$ is torsion free and $\langle w_e,A_\pm\rangle$ is odd. (d) $\langle w_e,F\rangle\equiv\langle w_0,F\rangle$ since $F\cdot S_i\in\{0,\pm2\}$. ∎ VERIFIED.

So $\Omega$ is a signed sum over $2^n$ *different* $\mathrm{SO}(3)$ bundles with a common $p_1$.

### 1.3 Representatives

Let $z=S_1\cdots S_n\cdot z_C$, with $z_C$ a monomial in point and surface classes supported in the caps, and
$$\deg z=2n+\deg z_C=d_a+n .$$

- **$\mu_p(S_i)$: the jumping-line divisor.** For a map $f\colon S^2\to X$ with $\langle w,f_*[S^2]\rangle$ even, let $\mathcal E_A=f^*E\otimes(f^*\det E)^{-1/2}$, a holomorphic bundle $\mathcal O(k)\oplus\mathcal O(-k)$ on $\mathbb P^1$ (Grothendieck). The operator $\bar\partial$ on $\mathcal E_A(-1)$ has index zero and kernel $H^0(\mathcal O(k-1)\oplus\mathcal O(-k-1))$, so the canonical section of its determinant line vanishes exactly on $\mathcal V_f=\{k\ge1\}$; its first Chern class is $\pm\mu(f_*[S^2])$.

  **Lemma 1.2.**
  - (J1) $\mathcal V_f$ depends only on $A|_{f(S^2)}$ and is closed under $C^0$ convergence of restrictions (the difference of two $\bar\partial$-operators has order zero).
  - (J2) If $A|_f$ preserves a splitting $L_1\oplus L_2$ and $v=c_1(L_1)-c_1(L_2)$, then $A\in\mathcal V_f$ iff $\langle v,f_*[S^2]\rangle\ne0$ (the splitting type is $|\langle v,f\rangle|/2$).
  - (J3) If $[A_\alpha]\in\mathcal V_f$ converge to an ideal limit reducible along $f$ with $\langle v,f\rangle=0$, the limit carries charge on $f(S^2)$: a bubble on it, or neck charge at a broken neck that $f$ crosses. Distinct disjoint spheres need distinct charges.
  - (J4) As $t_i\to-1$, $\mathcal V_{S_i}$ degenerates to $\mathcal V_{C_l}\cup\mathcal V_{C_r}$, the jumping divisors of the two capped halves; as $t_i\to+1$ it becomes the jumping divisor of $S_i$ in the cap $\hat\nu_i$.

  (J1)–(J3) are VERIFIED: they are the proof of Strategy Thm. 2.1 (checked by the Round 3a referee) and T2 Prop. 2.3, Cor. 3.3; the convergence used in (J3) is FL1 Def. 4.19 and Thm. 4.20 ($C^\infty$ after gauge away from bubbles). In (J4) the algebra on the nodal curve is VERIFIED (the twist degenerates to $(\mathcal O(-1),\mathcal O)$; the glued bundle jumps iff one side jumps; T2 §4, recomputed); the analytic degeneration of the determinant line is PLAUSIBLE. Transversality of a perturbed section on the irreducible strata, with the perturbation supported away from the compact set of restrictions of reducible limits with $\langle v,f\rangle=0$, is PLAUSIBLE (Round 3a: 85–90%).
- **$\mu_p(z_C)$** by the representatives of FL2b Lemma 3.12, supported in the caps.
- **$\mu_c$** by $n_a-1$ sections of $\mathbb L_{\mathfrak t}=\mathcal C^{*,0}_{\mathfrak t}\times_{(S^1,\times-2)}\mathbb C$ (FL2b (3.10), (3.12)). Each section is a sum, over *all* pieces $\hat Z_j$, of weight-two functions of spinor values sampled at finitely many points of $\hat Z_j$ after transport to a base frame; the sample points avoid $\bigcup S_i$, $\bigcup\nu_i$ and the cap supports. The sections for $e$ and $e^{(i)}$ (the index with $e_i$ changed) agree off $\nu_i$. On an ideal limit a section restricts to the sum of the contributions of the components with nonzero spinor.

  This departs from FL2b Lemma 3.13, whose representative is determined by restriction to one ball. At a face where that ball lies in a piece with zero spinor the condition would be empty and the dimension counts below would fail by two per section. With sampling on every piece, the restriction to $\mathbb P(\ker D_A)$ at an instanton is a quadric, which is all that FL2b Lemma 3.28 and Prop. 3.29 use. PLAUSIBLE.

All supports are in general position, so that a bubble releases conditions of total degree at most four (FL2b (3.25), which is what FL2b's count of the background stratum uses) and, for the exact supports used here, its position together with the degrees it releases accounts for at most four dimensions: a sphere or cap surface gives two positions and releases two; a cap point gives no position and releases four; a sample point gives no position and releases two; two transverse cap surfaces meet in points, which give no position and release four. This is FL2b (3.25) for the enlarged set of supports. VERIFIED as a count; general position PLAUSIBLE.

### 1.4 The invariant and the cut-down spaces

$$\Omega=\sum_e\varepsilon(e)\,\#\big(\bar{\mathcal V}(z)\cap\bar M^{w_e}_\kappa(Q)\big),\qquad M^{w}_\kappa(Q)=\bigcup_{t\in\mathrm{int}\,Q}M^{w}_\kappa(g_t),$$
with $M^{w_e}_\kappa$ oriented by $o(\Omega,w_e)$ and $\varepsilon(e)=\prod_i\varepsilon_i(e_i)$, $\varepsilon_i(1)=-s_i\varepsilon_i(0)$, where $s_i$ compares the orientations of the two minimal lens caps on $\nu_i$. That the weighted sum does not jump at lens faces, while single counts do, is PLAUSIBLE (T1 Prop. 1.4). That $\Omega(X_M)=\pm\langle\Psi_+,(\phi_*B)^{p_+}u^M(\phi_*B)^{p_-}\Psi_-\rangle$ is PLAUSIBLE (T1 Prop. 1.5) and is not used in the relation.

Put
$$\mathcal Z_e=\mathcal V(z)\cap\mathcal W_1\cap\dots\cap\mathcal W_{n_a-1}\cap\mathcal M^{*,0}_{\mathfrak t_e}(Q)/S^1,\qquad\dim\mathcal Z_e=(d_a+2n_a+n-1)-(d_a+n)-2(n_a-1)=1 .$$
This is FL2b's one-manifold (3.62), with $\deg z=d_a$ replaced by $\deg z-\dim Q=d_a$, so $\delta_c=n_a-1$ as in FL2b (3.26). VERIFIED.

### 1.5 Faces, ideal limits and the strata of the pieces: hypothesis (i)

A point of $\bar Q$ lies in the relative interior of a face given by disjoint sets $\mathcal J=\{i:t_i=-1\}$ ($k=|\mathcal J|$) and $\mathcal N=\{i:t_i=+1\}$. Cutting along $J_i$ ($i\in\mathcal J$) and $\partial\nu_i$ ($i\in\mathcal N$) gives main pieces $\hat\Gamma_0,\dots,\hat\Gamma_k$ (unions of consecutive $\hat Z_j$, minus the $\nu_i$, $i\in\mathcal N$, with cylindrical ends), caps $\hat\nu_i$ ($i\in\mathcal N$), and necks $\mathbb R\times S^3$, $\mathbb R\times L(4,1)$.

**Ideal limits.** An ideal limit over such a point consists of an ideal $\mathrm{SO}(3)$ monopole $[A_j,\Phi_j,\mathbf x_j]$ on each main piece, exponentially asymptotic on each end to a flat connection with zero spinor; an ideal anti-self-dual connection on each cap; a finite chain of anti-self-dual trajectories on each infinitely long neck; with matching flat limits and total charge $\kappa$.
- On every neck and cap the spinor vanishes (Weitzenböck formula with positive scalar curvature). VERIFIED as an argument; uniform integration on the ends PLAUSIBLE.
- Flat limits: on $S^3$ only the trivial connection (stabilizer $\mathrm{SU}(2)$ in the determinant-one gauge group); on $L(4,1)$, with $w_e|_{\partial\nu_i}=0$ since $\langle w_e,S_i\rangle\equiv0\pmod4$, the two central connections $\pm1$ and the trace-zero connection (stabilizer $\mathrm U(1)$). All have $H^1=0$ and invertible Dirac operator. VERIFIED.
- Charges: trajectories and bubbles carry positive integers; cap charges lie in $\mathbb Z_{\ge1}$ at a central state and in $\frac14+\mathbb Z_{\ge0}$ at the trace state; the minimal trace cap is the abelian instanton of charge $\frac14$ with $\langle v,S_i\rangle=\pm2$. PLAUSIBLE (manuscript Prop. `indices:lens-index`, Lemma `indices:lens-charge`; I checked the arithmetic of the index table, not the orbifold comparison).

**Types.** By the proof of FL2a Prop. 3.1, which is local to a component, each main component is of type F, A, S or R. FL2a Prop. 3.1 excludes type R on a closed manifold with a generic metric (via Donaldson–Kronheimer Cor. 4.3.15); in a family over a cube of dimension $n>b^+(X)$ it cannot be excluded: on a union of negative pieces ($b^+=0$) every class $v\equiv w\pmod 2$ is represented by an abelian instanton for *every* value of the parameters, and on a positive piece along the wall $\langle v,H(t)\rangle=0$. Only the caps, whose periods are fixed and generic, exclude it. VERIFIED.

**Levels (each piece has its own strata).** For a component of type S or R on $\hat\Gamma$ put $v_\Gamma=c_1(L_1)-c_1(L_2)\equiv w|_\Gamma\pmod 2$, so $c_1(\mathfrak s_\Gamma)=\Lambda|_\Gamma+v_\Gamma$. Filling the lens ends by the manuscript's reference abelian connections,
$$\kappa_\Gamma=-\tfrac14v_\Gamma^2+\ell_\Gamma,\qquad\ell_\Gamma\in\mathbb Z_{\ge0},$$
where $\ell_\Gamma$ collects bubbles, allocated neck charge and cap excess. So the component lies in the stratum $\iota(M_{\mathfrak s_\Gamma}(\hat\Gamma;Q_\Gamma))\times\mathrm{Sym}^{\ell_\Gamma}(\hat\Gamma)$ of its own piece, a families Seiberg–Witten space over the parameters internal to $\Gamma$, or in its zero-spinor part. For $k=0$, $\mathcal N=\emptyset$ this is FL2b Lemma 3.32 with (3.63)–(3.64) and Memoir (2.3.14): $\ell(\mathfrak t,\mathfrak s)=\frac14\big((c_1(\mathfrak t)-c_1(\mathfrak s))^2-p_1(\mathfrak t)\big)$. VERIFIED (algebra; reference fillings PLAUSIBLE).

**Piece charges are not bounded by $\kappa$.** A free component may carry negative charge, bounded below only through $\|F^0\|^2=2\|F^{0,+}\|^2+8\pi^2\kappa_j$ and the Weitzenböck bound on $F^{0,+}$. So a piece can carry a stratum at nonnegative level even when every class on $X$ has negative level, and FL's condition "$\ell<0$ for all $\mathfrak s$" must be replaced by conditions that couple the pieces through indices, not energy. VERIFIED as a remark.

**Lemma 1.3 (index identities).** For a main component $j$ let $p_j$ be the number of unbroken necks inside it (restoring one at each of its lens ends), $s_j$ the number of sphere insertions assigned to it (at a broken neck, the side on which the insertion is met), $z_j$ its cap degree, and
$$q_j=d_a(\hat\Gamma_j)+p_j-2s_j-z_j,\qquad i_j=q_j+2n_a(\hat\Gamma_j),$$
with lens ends filled by the reference connections. Then
$$\sum_{j=0}^k(q_j+4)=4,\qquad\sum_{j=0}^ki_j-2(n_a-1)=2-4k .$$
*Proof.* $\sum_jd_a(\hat\Gamma_j)=d_a-3k$ (unframed indices; each broken $S^3$ loses the three dimensions of its stabilizer), $\sum_jn_a(\hat\Gamma_j)=n_a$ (Dirac indices add across $S^3$, where the Dirac operator is invertible), $\sum p_j=n-k$, $\sum s_j=n$, $\sum z_j=\deg z_C$, and $d_a=n+\deg z_C$. ∎ VERIFIED as algebra (`f4_identities.py`); the additivity of indices is PLAUSIBLE (standard APS; manuscript Lemma `indices:virtual-sums`).

Each broken neck costs four: three for the gluing parameter, which the limit does not record, and one for the lost parameter.

---

## 2. The relation

### 2.1 Analytic hypotheses

The equations are perturbed and the representatives and family are chosen generically within a class satisfying:

- **(A1) Compactness.** Every sequence in $\mathcal Z_e$, and in the cut-down instanton space $\bar{\mathcal V}(z)\cap M^{w_e}_\kappa(Q)$, has a subsequence converging to an ideal limit over a point of $\bar Q$, in the sense of FL1 Def. 4.19 on compact subsets of the pieces, with exponential convergence on the necks. PLAUSIBLE: FL1 Thm. 1.1 and Thm. 4.20 treat one closed manifold; on long necks the energy estimate must use only the negative part of the scalar curvature (FL1 Lemma 4.2 uses $\|\mathrm{Scal}\|_{L^2}$, which grows with the neck), and the $C^0$ bound of FL1 Lemma 4.4 is uniform because the neck metrics are fixed.
- **(A2) Regularity of single components.** (a) The cut-down instanton space over $\mathrm{int}\,Q$ is cut out transversely, $\mathcal V(z)$ is smooth and transverse to $M^{w_e}_\kappa(Q)$ at its points (as FL2b Lemma 3.22 requires; for the jumping divisors at the generic points, of splitting type $\mathcal O(1)\oplus\mathcal O(-1)$), and the coupled Dirac operator may be taken onto there. (b) Every component of type A, cut down by its assigned insertions, with its retained parameters, is regular, so $q_j\ge0$, with strict inequality if it carries a bubble, allocated neck charge or a lens end. (c) The free strata of every piece at every level are regular for their cut-down problems. (d) Components of type S are regular for their own families Seiberg–Witten problem: $d_s+p_j+4\ell_j\ge0$. PLAUSIBLE (FL1 Thm. 1.3, FL2a Thm. 2.13; manuscript Prop. `analysis:first-stage`).
- **(A3) Coupled regularity.** At every ideal limit with a free component and no component of type R, the problem formed by all its components (their equations, assigned insertions, retained parameters and the phase sections, modulo the gauge groups of the pieces and the diagonal circle) is regular after an arbitrarily small multivalued perturbation that vanishes near the instanton collars and agrees for $e$ and $e^{(i)}$ off $\nu_i$. The free component restricts the circle to $\{\pm1\}$, so the isotropy is finite; it is nontrivial at type A components (the centre of their gauge group acts by $-1$ on the Dirac cokernel), which is why the perturbations must be multivalued. PLAUSIBLE; new (manuscript Lemma `analysis:samples`, Def. `indices:analytic-hypotheses`(iii)).
- **(A4) Instanton links.** FL2b Prop. 3.29 holds with the cube as parameters. PLAUSIBLE, routine: the parameters enter the Kuranishi model at $(A,0,t)$ only as finite-dimensional variables.
- **(A5) Lens ends.** Every minimal lens limit (a free component on $X\setminus\nu_i$ with no bubbles, the minimal trace cap on $\hat\nu_i$, over an open face $\{t_i=+1\}$) is the limit of exactly one end of $\mathcal Z_e$; and the ends of $\mathcal Z_e$ and $\mathcal Z_{e^{(i)}}$ over the same exterior solution carry opposite $\varepsilon$-weighted orientations. PLAUSIBLE: the gluing is at a flat connection whose stabilizer $\mathrm U(1)$ equals that of the cap, the cap's Dirac operator is invertible by positive scalar curvature, and its normal operator is made onto by a perturbation vanishing at the reducible (manuscript Cor. `indices:trace-minimum`, §10); the orientation comparison across different $w_2$ is new.
- **(A6) Stokes' theorem** for compact oriented branched one-manifolds with rational weights. PLAUSIBLE, standard.

### 2.2 Statement

> **Theorem A (family vanishing).** Let $(X,J,S,\nu,g)$ and $\mathfrak t_e$ be as in §1.1–1.2, with $n_a\ge1$ and $\deg z=d_a+n$, and assume (A1)–(A6). Suppose:
> - **(E0)** for every $e$, the cut-down instanton space $\bar{\mathcal V}(z)\cap\bar M^{w_e}_\kappa(\bar Q)$ consists of finitely many points over $\mathrm{int}\,Q$ in the top stratum; and
> - **(E)** for every $e$, the closure of $\mathcal Z_e$ over $\bar Q$ contains no ideal limit with a main component of type S or R. Equivalently: over no face, on no main piece and at no level $\ell\ge0$, does the closure of the cut-down space meet a Seiberg–Witten stratum $\iota(M_{\mathfrak s}(\hat\Gamma))\times\mathrm{Sym}^\ell(\hat\Gamma)$, including its zero-spinor part. (Caps are not main components; the minimal lens limits are allowed.)
>
> Then $2^{\,n_a-1}\,\Omega=0$, and hence $\Omega=0$.

**Remarks.**
1. *The case $n=0$.* There are no spheres and no faces, (A3) and (A5) are void, (E0) is the Kronheimer–Mrowka finiteness behind the definition of $D^w_X$ (FL2b (3.31)–(3.32); Lemma 3.22 lists $\bar{\mathcal V}(z)\cap\bar M^w_\kappa$ as finitely many points) together with FL2b Lemma 3.21 ($\bar M^{\rm asd}_{\mathfrak t}=\iota(\bar M^w_\kappa)$ for good $w$), and Theorem A is FL2b Thm. 3.33(a) with its hypothesis (3.68), "$(c_1(\mathfrak t)-c_1(\mathfrak s))^2<p_1(\mathfrak t)$ for every $\mathfrak s$ with $M_{\mathfrak s}\ne\emptyset$" (no reducible at any level), weakened to "the closure of the cut-down one-manifold meets none". This is Strategy Thm. 2.1(a) with no spheres. VERIFIED against FL2b Thm. 3.33, whose hypotheses I read in full: $b^+>0$, $w$ good, $d_a\le\deg z\le d_a+2n_a-2$ (which forces $n_a\ge1$ when $\deg z=d_a$), $z$ intersection-suitable, all reducibles in the top level.
2. *No gluing at reducibles.* No stratum of reducibles is parametrized and no link of one is evaluated. Memoir Hyps. 7.8.1 and 11.3.5, FL6 Hyp. 3.1, FL3 and the overlap problem are not used. VERIFIED as logic.
3. *Not claimed.* No formula expressing $2^{n_a-1}\Omega$ through abelian ends is asserted. The formula $2^{n_D-1}\Omega=-\#\{\text{abelian ends}\}$ of `exposition.tex` (and T1 Thm. A) is false as a theorem: without gluing at reducibles, abelian limits are not known to be ends of a one-manifold, so they cannot be counted. Only the vanishing form is used.
4. *Integrality.* Because of the multivalued perturbations of (A3), Stokes gives $2^{n_a-1}\Omega=0$ in $\mathbb Q$, hence $\Omega=0$ in $\mathbb Z$. Over $\mathbb F_2$ the identity is empty once $n_a\ge2$, so the nonvanishing of Step 2 of the Strategy must be integral. VERIFIED.
5. *(E0) is not purely analytic.* Its regularity part is (A2)(a); its exclusion part (no limits at faces, lower levels or with type R components) follows from the same segment inequalities as (E) (Theorem B). Both drafts listed it among analytic hypotheses.

### 2.3 Proof of Theorem A

Fix $e$, write $\mathcal Z=\mathcal Z_e$, and for small generic $\varepsilon>0$ and large $T$ let $\mathcal Z^\circ$ be the part of $\mathcal Z$ where $\|\Phi\|^2_{L^2}\ge\varepsilon$, with the collars beyond neck length $T$ at minimal lens limits removed. The argument is FL2b's proof of Thm. 3.33(a), Stokes' theorem on the one-manifold (3.62), with the faces added.

*Step 1 (compactness).* By (A1) every end of $\mathcal Z$ has an ideal limit over $\bar Q$. $\|\Phi\|^2_{L^2}$ is continuous on ideal limits: the spinor is bounded in $C^0$ (FL1 Lemma 4.4), so it does not concentrate at bubbles, and it decays exponentially on the necks. PLAUSIBLE.

*Step 2 (zero spinor: the instanton ends).* For small $\varepsilon$ the level set $\{\|\Phi\|^2=\varepsilon\}\cap\bar{\mathcal V}(z)$ lies near zero-spinor ideal limits satisfying $\mathcal V(z)$; the phase sections impose nothing there (FL2b Lemma 3.15(2d): $\iota(\bar M^w_\kappa)\subset\bar{\mathcal W}$). Such limits are: points of the cut-down instanton space, which by (E0) are finitely many interior top-stratum points; broken limits all of whose components are of type A, excluded because Lemma 1.3 and (A2)(b) give $4=\sum(q_j+4)\ge4(k+1)$; zero-spinor lens limits with a type A main component, excluded because a lens end makes $q_0>0$ while Lemma 1.3 forces $q_0=0$ when $k=0$; and limits with a type R component, excluded by (E). Near each instanton point, (A4) gives FL2b Lemma 3.22, Lemmas 3.27–3.28 and Prop. 3.29 with parameters: the link is $\mathbb P(\ker D_{A,t})\cong\mathbb{CP}^{n_a+c-1}$, the cokernel contributes $h^c$, $\mu_c$ restricts to $2h$, and the local count is $\pm\langle(2h)^{n_a-1}h^c,[\mathbb{CP}^{n_a+c-1}]\rangle=\pm2^{n_a-1}$ with the sign of the instanton in $o(\Omega,w_e)$. The total is $\sigma_0\,2^{n_a-1}\#(\bar{\mathcal V}(z)\cap\bar M^{w_e}_\kappa(Q))$ with $\sigma_0=\pm1$ independent of $e$ (FL2b Lemmas 3.24–3.25 fix it by the conventions alone). VERIFIED as an adaptation of FL2b; the extension with parameters PLAUSIBLE.

*Step 3 (free strata at lower level, unbroken).* A limit at level $\ell$ satisfies every condition whose support contains no bubble ((J1), FL2b Lemma 3.15(1)). A level costs six dimensions of $\mathcal M/S^1$ and a bubble recovers at most four (§1.3), so the relevant stratum has dimension at most $1-2\ell<0$. This is FL2b's count before Cor. 3.18. VERIFIED as a count, given (A2)(c).

*Step 4 (broken limits with free and type A components only).* Let $\zeta$ have $k\ge1$ broken necks, at least one free component, and otherwise type A components. By (A3) the space of such limits near $\zeta$ is a branched manifold of dimension
$$\sum_ji_j-2(n_a-1)-1-(\text{losses})=1-4k-(\text{losses})<0,$$
so no such limit exists. Coupled regularity is genuinely needed here. A type A component is regular for the anti-self-dual problem but its Dirac operator has cokernel when $n_a(\hat\Gamma_j)<0$, and then the naive dimension of the stratum is $1-4k-2\sum_{\rm A}n_a(\hat\Gamma_j)$, which can be nonnegative. In $X_M$ this happens whenever a type A component contains a blown-up cap, since $\Theta$ of the cap contains $\frac14(1-\langle\Lambda,E_\pm\rangle^2)\ll0$. An obstructed gluing count would give these ends virtual dimension $1-k$, so at codimension-one faces nothing excludes them by counting: with uncoupled perturbations $\mathcal Z_e$ may well have isolated ends there. Their signed number must then be zero. Indeed, a coupled perturbation as in (A3) agrees with the uncoupled one near the instanton links and the lens ends, so Stokes' theorem for the two perturbations shows that the signed number of these ends is the same as with (A3), namely zero. Independently, the obstruction bundle $\mathrm{coker}\,D_{A_j}$ over (space of limits)$\times\mathrm{SO}(3)$ is pulled back from the space of limits, whose dimension is smaller than its rank by $4k-1\ge3$, so its Euler class vanishes. VERIFIED as arithmetic; that (A3) suffices is PLAUSIBLE; the Euler-class remark is SPECULATIVE (it ignores noncompactness of the space of limits). The point was missed in `strategy.tex` and in T1 (AP4 there is labelled verified without it); it is implicit in the manuscript's Def. `indices:analytic-hypotheses`(iii), which applies to every limit containing a free component.

*Step 5 (lens faces).* A lens cap at the trace state with charge $\frac14+h$ lowers the cut-down monopole count by $1+6h$; at a central state by $6\kappa_N-1\ge5$ (the penalty $\delta_{\rm sp}-1$: the filled index drops by $\delta_{\rm sp}$, while the lost parameter and the insertion met on the cap restore one net). The face has codimension one per lens neck. So the only lens limits are the minimal ones, and by (A5) each is the limit of exactly one end. VERIFIED as arithmetic of the manuscript's table; the table PLAUSIBLE.

*Step 6 (Stokes).* By Steps 1–5 and (E), the closure of $\mathcal Z^\circ$ is a compact oriented weighted branched one-manifold whose boundary consists of the link points of Step 2 and the lens collars. By (A6),
$$0=\sigma_0\,2^{n_a-1}\#\big(\bar{\mathcal V}(z)\cap\bar M^{w_e}_\kappa(Q)\big)+\#(\text{lens ends of }\mathcal Z_e).$$
Multiply by $\varepsilon(e)$ and sum over $e$. The exterior problems for $e$ and $e^{(i)}$ on $X\setminus\nu_i$ coincide, because $\mathrm{PD}[S_i]$ is the image of the Thom class of $\nu_i$ and restricts to zero on $X\setminus\nu_i$ (VERIFIED), and because the metrics, sections and perturbations agree there; so by (A5) the lens ends cancel in pairs $e\leftrightarrow e^{(i)}$. Hence $\sigma_0\,2^{n_a-1}\Omega=0$. ∎

The deduction is VERIFIED given (A1)–(A6), (E0) and (E).

---

## 3. A criterion for (E): the segment inequalities and the projection

### 3.1 Segments and excesses

A *segment* is a union $\Gamma$ of consecutive inner pieces of a face lying between two broken necks, carrying $r\ge1$ consecutive main components of an ideal limit (separated by $r-1$ further broken necks) that are all reducible. Put $L$ = number of pieces, $m$ = number of positive pieces, $s$ = number of assigned insertions (all internal ones; a bounding one if its half in $\Gamma$ is the assigned side), $\Delta=e_a-e_b\in\{-1,0,1\}$ for the bundle indices of the two bounding spheres, and $\kappa_\Gamma$ the total charge. Define
$$\epsilon_I(\Gamma)=\sum_{j\in\Gamma}(q_j+4),\qquad\epsilon_C(\Gamma)=\sum_{j\in\Gamma}(4+i_j-p_j),\qquad\epsilon_S(\Gamma)=\sum_{j\in\Gamma}(4+i_j).$$
Since $\Theta$ is $\frac12(e_j-e_{j+1})$ on a negative piece and $1+\frac12(e_j-e_{j+1})$ on a positive piece, $\Theta_\Gamma=m+\frac12\Delta$, and for a segment without caps
$$\epsilon_I=8\kappa_\Gamma-3m+L-2s,\qquad\epsilon_C=r+6\kappa_\Gamma-m+\Delta-2s,\qquad\epsilon_S=6\kappa_\Gamma-m+L-2s+\Delta .$$
VERIFIED (`f1_lattice.py`, `f4_identities.py`).

The weights have a meaning. In $\epsilon_I$ charge enters with weight $8$, each positive piece with $-3$ (its $b^+$), each piece with $+1$ (its parameter), each insertion with $-2$. In the two monopole excesses charge enters with weight $6=8-2$ (raising the charge by one raises the instanton index by eight and lowers the complex Dirac index by one, so the real monopole index by six) and a positive piece with $-3+2\Theta(P)=-1$. $\epsilon_C$ keeps the parameters of the segment (the manuscript's count); $\epsilon_S$ drops them. $\epsilon_I$ and $\epsilon_S$ do not depend on $r$.

### 3.2 Statement

> **Theorem B.** In the situation of Theorem A, assume (A1)–(A6), the projection hypothesis (A7) of §3.4, and:
> - **(B1) Incidence.** The representatives satisfy (J1)–(J4) of Lemma 1.2.
> - **(B2) Caps.** No component of type R contains a cap piece $\hat Z_0$ or $\hat Z_n$, and every component of type S containing one has $q_j\ge0$.
> - **(B3) Global inequality.** For every $t\in\bar Q$ off the $J$-faces and every Seiberg–Witten solution on $X$ at $t$ (lens caps filled by the reference connections) with class $v=c_1(\mathfrak s)-\Lambda$,
> $$\kappa+\tfrac14v^2<T(v):=\#\{i:\langle v,S_i\rangle=0\}.$$
> - **(B4) Segments, no free component.** Every segment $\Gamma$ of consecutive interior reducible components of an ideal limit without free component has $\epsilon_I(\Gamma)\ge-3$.
> - **(B5) Segments next to a free component.** Every maximal segment $\Gamma$ of consecutive type R components of an ideal limit with a free component has $\epsilon_C(\Gamma)\ge-2$; under the locality hypothesis (A7′) of §3.4, $\epsilon_S(\Gamma)\ge-2$ suffices.
>
> Then (E) and the exclusion part of (E0) hold for every $e$, and so $2^{n_a-1}\Omega=0$.

(B3) is the family form of FL2b (3.68), weakened by the incidence term $T(v)$ as in Strategy (2.1). (B4) and (B5) are the family-specific hypothesis (ii); (A7) is hypothesis (iii).

### 3.3 Proof of Theorem B

Let $\zeta$ be an ideal limit in the closure of $\mathcal Z_e$ with a main component of type S or R.

- **$k=0$.** There is one main component. If it is of type R it contains the caps, contrary to (B2). If it is of type S, each insertion with $\langle v,S_i\rangle=0$ forces charge on $S_i$ by (J3) (at a lens face, charge in the cap), and the spheres are disjoint, so $\ell=\kappa+\frac14v^2\ge T(v)$, contrary to (B3). This is the mechanism of Strategy Thm. 2.1, now with $t$ ranging over $\bar Q$; it covers all levels at once, because incidence uses only convergence away from bubbles.
- **$k\ge1$, no free component.** Type A components have $q_j+4\ge4$ by (A2)(b); the two outer components are of type A or S by (B2), and an outer S component has $q_j+4\ge4$. Let $a$ be the number of type A components and $b\le2$ the number of outer type S components; $a+b\ge2$. The other components form at most $a+b-1$ interior segments, each with $\epsilon_I\ge-3$ by (B4). So
$$\textstyle\sum_j(q_j+4)\ge4(a+b)-3(a+b-1)=a+b+3\ge5>4,$$
contradicting Lemma 1.3. The threshold is sharp: with $\epsilon_I=-4$ allowed, two type A components around one segment give $4+4-4=4$.
- **$k\ge1$, free component, no type R.** Some component is of type S. By (A3) the coupled problem, which regularizes the type S and type A components using the free one, is regular of dimension $1-4k-(\text{losses})<0$. No such limit.
- **$k\ge1$, free component and type R components.** By (A7) and (B5), §3.4 below: the projected index is at most $3-2N\le-1$. No such limit.

The same case analysis applied to zero-spinor limits of the cut-down instanton spaces (only the first two cases occur) gives the exclusion part of (E0). ∎ VERIFIED as logic.

### 3.4 Mixed limits with abelian instantons: hypothesis (iii)

**What happens.** Let $\zeta$ be an ideal limit with a free component and a maximal segment $\Gamma$ of type R components. By (B2) $\Gamma$ is interior, so $k\ge2$.
- *They exist in abundance.* On a segment of negative pieces every class carries an abelian instanton for every value of the internal parameters (§1.5). They are the family analogue of the reducibles of Kotschick and Morgan (Memoir Lemma 11.1.1: an ideal reducible $[\Theta\oplus A_L]\times\mathrm{Sym}^\ell$ lies in $\bar M^w_\kappa(g_0)$ iff $c_1(L)^2=-4(\kappa-\ell)$, $c_1(L)\equiv w\pmod2$ and $\omega^+(g_0)\smile c_1(L)=0$; the "$\ge0$" printed there belongs to $\kappa-\ell$). VERIFIED.
- *They cannot be made regular.* The stabilizer of $(d\oplus A_L,0)$ on $\Gamma$ contains its own gauge circle $\mathrm{diag}(z,z^{-1})$. In a broken limit the gauge groups of the pieces are independent, so a free component elsewhere does not reduce this circle (it pins only the common phase). Under the circle the deformation complex splits into weight zero (with $H^2=H^+(\hat\Gamma)$, the wall condition, removable by moving parameters), the off-diagonal anti-self-dual deformations in $L_1L_2^{-1}$ (weight $\pm2$) and the spinor directions in $W^\pm\otimes L_1$, $W^\pm\otimes L_2$ (weights $\pm1$). Equivariant perturbations, single- or multivalued, cannot change the index of a nonzero-weight block, and a finite set of branches permuted by a connected group consists of invariant branches; so a block of negative index keeps its cokernel. The space of such components has dimension up to $p_\Gamma$, while its virtual dimension $i_\Gamma$ may be much smaller. VERIFIED as representation theory.
- *Counting cannot exclude them*, because the virtual count does not bound the actual dimension.

**What is needed.** One of two things.
1. *An obstructed gluing theorem in families with faces*: a Kuranishi model at an abelian segment glued across $S^3$ necks to non-abelian pieces, with gluing parameters in $(\mathrm{SO}(3)\times\mathrm{SO}(3))/\mathrm U(1)$ per component and an equivariant obstruction section in the nonzero-weight cokernels. This is the face analogue of Memoir Hyp. 11.3.5 (gluing at reducible anti-self-dual connections in a path of metrics, used for the Kotschick–Morgan conjecture) and Hyp. 7.8.1 (local gluing for $\mathrm{SO}(3)$ monopoles). Neither is proved even on a closed manifold. OPEN, and not needed. That with such a model and a transverse leading obstruction term limits with $k\ge2$ would not be reached at all (virtual dimension $1-k<0$), so that no spacing condition would be needed, is SPECULATIVE (T1 Rem. 2.4): at infinite neck length the leading term may fail to be transverse at gluing parameters fixed by the circle.
2. *The necessary projection.* An *unmatched limit* over a face is a collection of solutions on the main pieces, each satisfying its equations, assigned insertions and the phase sections, together with nonnegative charge assignments to the omitted caps, trajectories and bubbles in the allowed congruence classes and with total charge $\kappa$; no matching across broken necks is required. Every ideal limit is an unmatched limit (VERIFIED). The hypothesis is:

   **(A7) Necessary projection.** For every unmatched limit with a free component, delete its type R components with their bubbles and assigned insertions. Then the remaining problem
   - (a) does not depend on the deleted fields or bubbles (perturbation terms that sample a type R piece vanish near it; the phase sections restrict to the sum of the remaining contributions, since a weight-two function vanishes on zero spinor);
   - (b) is Fredholm, with finite isotropy (the free component pins the phase; type S and type A components then have finite stabilizers);
   - (c) is regular near the projections of all unmatched limits of the given type, after an arbitrarily small multivalued perturbation as in (A3);
   - (d) has a set of such projections that is compact modulo unmatched limits of strictly more degenerate type (deeper face, larger loss, fewer bubble positions, more dropped insertions, more type R components), so that finitely many perturbation steps suffice, each small enough to preserve the earlier exclusions, the instanton collars and the equality of data for $e$ and $e^{(i)}$ off $\nu_i$.

   PLAUSIBLE; new. It is the manuscript's Lemmas `analysis:projection`, `analysis:R-independence` and Prop. `analysis:finite-induction`; it has no counterpart in Feehan–Leness, who never regularize at reducible points (they build the link of a reducible stratum from a stabilized, thickened moduli space, FL2a §§3.4–3.5, Thms. 3.19 and 3.21, and assume gluing).

**The index.** Let $N$ be the number of non-R main components, $\Gamma_1,\dots,\Gamma_\rho$ the maximal type R segments, and $\Lambda_{\rm loss}\ge0$ the losses on the remaining components (a bubble of charge $c$ costs at least $2c$; a lens end costs $\delta_{\rm sp}-1\ge1$). Regarding the remaining problem as a family over all free parameters of the face (those of the deleted segments included), its index after the phase sections and the circle quotient is
$$I=\sum_{j\notin R}(i_j-\lambda_j)+\sum_{j\in R}p_j-2(n_a-1)-1=5-4N-\sum_\rho\epsilon_C(\Gamma_\rho)-\Lambda_{\rm loss},$$
by Lemma 1.3 and $k+1=N+\#R$. VERIFIED (`f4_identities.py`). Since $k\ge1$, $N\ge2$, and there are at most $N-1$ segments; with (B5) the index is at most $5-4N+2(N-1)=3-2N\le-1$, and (A7)(c) makes the projected problem empty near the projections, so $\zeta$ does not exist. The threshold $-2$ is sharp for the method: a segment with excess $-3$ and $N=2$ gives index $0$. VERIFIED.

**(A7′) Locality in the parameters, and a sharper count.** Suppose that every perturbation term and representative acting on the fields of a set of pieces depends on $t$ only through the parameters of the necks inside the components it samples or acts on. The metric already has this property (§1.1). Then the remaining problem does not depend on the parameters internal to the deleted segments: these change only the metric on the deleted pieces and the insertions met there. Its zero set is the product of a cube with the zero set of the problem in the remaining parameters, which has index
$$I'=I-\sum_{j\in R}p_j=5-4N-\sum_\rho\epsilon_S(\Gamma_\rho)-\Lambda_{\rm loss}.$$
So under (A7′) the condition $\epsilon_S\ge-2$ suffices. VERIFIED as algebra and logic given (A7′). Whether (A7′) can be imposed together with (A7)(c)–(d) is PLAUSIBLE: the manuscript's single-component terms are already parameter-local (§9, "a single-component term between two $J$ cuts uses only the metric parameters retained on that component"), but its coupled terms are allowed to depend on the parameters of type R components ("the parameters of an $R$ component may remain in the projection", Lemma `analysis:R-independence`); the induction of Prop. `analysis:finite-induction` should go through with the coupled terms chosen on the smaller parameter space, since the projections of the unmatched limits to it still form a compact set. Both drafts make this observation; I agree with it and with its label.

**Consequence.** With the coarse count, (B5) holds at spacing $k\ge4$ only; with the sharp count, at every spacing $k\ge2$ (§4.5). The binding local condition then becomes (B4), which needs $k\ge3$, and together with the global window $\frac15<m/n<\frac37$ the admissible spacings become $\{3,4\}$: the period $(\phi_*B)^2HB$ should also serve. PLAUSIBLE, conditional on (A7′).

---

## 4. The exclusion for $u=(\phi_*B)^3HB$

### 4.1 Numerology

**Proposition 4.1.** For $X_M$ and every $e$:
- (a) $b^+=m+b_0$ with $b_0=b^+(C_-)+b^+(C_+)$, and $\Theta=m+\Theta_0$, where $\Theta_0$ comes from the outer pieces.
- (b) $8\kappa=n+3m+c_\kappa$ with $c_\kappa=\deg z_C+3+3b_0$.
- (c) $n_a=\frac18(5m-n)+c_1$ with $c_1=\Theta_0-\frac18c_\kappa$; for $u$, $n=4M+p$, $m=M$, so $n_a=\frac18(M-p)+c_1$ and $3n-7m=5M+3p$.
- (d) Per block: a copy of $B$ (with the negative piece after it) contributes $(\Delta b^+,\Delta\Theta,\Delta\kappa,\Delta n_a)=(0,0,\frac18,-\frac18)$ — one parameter and one insertion of degree two raise $8\kappa$ by one — and replacing that negative piece by a positive piece adds $(1,1,\frac38,\frac58)$.

VERIFIED (`f1_lattice.py`, `f4_identities.py`). The value $\langle\Lambda_0,S_i\rangle=2$ forced by Lemma 1.1(a) makes $\Lambda\cdot F_l$, $\Lambda\cdot F_r$ even with difference $2$, so negative pieces contribute nothing to $\Theta$ beyond the telescoping $\frac12\Delta$; on $P$, $\Theta=1$ for the chamber-compatible lift $\Lambda_0=(-2,-1;0,1,0,-1)$. The Dirac index must therefore come from $b^+$, and raising $b^+$ by one costs $\frac38$ of charge.

### 4.2 Incidence

By (J2)–(J4), for a reducible component every assigned insertion is met by a nonzero (even) half-evaluation of $v_\Gamma$ — the whole evaluation $\langle v,S_i\rangle\ne0$ at an unbroken sphere, the evaluation on the assigned half at a broken neck — or by charge on the sphere. Halves are even because $v\equiv w$ and $w$ is even on halves (Lemma 1.1(d)). Distinct insertions need distinct charges. Hence $\ell_\Gamma\ge T_\Gamma(v)$, the number of assigned insertions not met by $v_\Gamma$. VERIFIED given (B1).

### 4.3 The positive piece

Let $P$ lie between $J_j$ and $J_{j+1}$; put $X_1=-S_j$, $X_2=S_{j+1}$, $H_I=U+\frac14\sum_{i\in I}X_i$ for $I\subset\{1,2\}$, $\lambda_I=\Lambda\cdot H_I$, and, for a reducible component containing $P$ with class $v$: $u=v\cdot U$, $d_i=v\cdot X_i$, $z_I=v\cdot H_I$, and the far halves $h_1=v\cdot F_{l,j}$, $h_2=v\cdot F_{r,j+1}$, which lie in the neighbouring negative pieces. With the bundle indices $(e,f)=(e_j,e_{j+1})$:
$$\lambda_\emptyset=-1-e+f,\quad\lambda_{\{1\}}=-\tfrac32+f,\quad\lambda_{\{2\}}=-\tfrac12-e,\quad\lambda_{\{1,2\}}=-1,\qquad u\equiv\lambda_\emptyset\pmod2 .$$
VERIFIED (`f1_lattice.py`; agrees with manuscript (`estimates:vertex-values`)).

**Proposition 4.2 (control of Seiberg–Witten classes on $P$).** For a component of type R or S containing $P$, at any point of $\bar Q$: either $u=0$, or there is a nonempty set $I$ of sides of $P$ whose necks are unbroken (a separated lens cap counts as unbroken) with
$$\operatorname{sign}(u)\,z_I\le0\quad(\text{R}),\qquad\operatorname{sign}(u)\,z_I<|\lambda_I|\quad(\text{S}).$$
Ingredients and status:
1. *The Weitzenböck band.* On a piece with $\mathrm{Scal}\ge0$, $\mathrm{Scal}>0$ somewhere, $b^+=1$ with period ray $H$, psc cylindrical ends, and the perturbation by the $L^2$-harmonic representative of $2\pi\Lambda$: a type S solution has $(v\cdot H)(K\cdot H)<0$, $K=\Lambda+v$, and a type R solution has $v\cdot H=0$. Proof: integrating the Weitzenböck formula gives $0=\int(|\nabla\psi|^2+\frac14\mathrm{Scal}|\psi|^2)+2\big(\frac{4\pi^2}{H^2}(v\cdot H)(K\cdot H)+\|D_\perp\|^2\big)$ after projecting onto the harmonic self-dual line. VERIFIED as a computation (T3 Thm. A, which I re-derived up to normalization); the integration by parts on the ends PLAUSIBLE. The band is optimal: on $\mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2$, $2\chi+3\sigma=4>0$, there are no walls at zero perturbation, and wall-crossing gives $SW=\pm1$ on the band, so no metric removes band classes (T3 §1.3). VERIFIED as logic.
2. *Convexity.* The periods in the toric region are $H=U+aX_1+bX_2$, $(a,b)\in[0,\frac14]^2\setminus\{0\}$, a convex combination of the $H_I$; $\lambda_I<0$ for $I\ne\emptyset$, and for $u>0$ parity gives $K\cdot U\ge0$. So the band or the wall at some admissible $H$ forces the vertex inequality at some $I\ne\emptyset$. VERIFIED: exhaustively, the band or wall over the exact period square (or segment, when one side is broken) implies the vertex alternative in all 35,152 instances with $|u|\le6$, $|d_i|\le24$ (`f2_clamp_test.py`); by hand as in T3 Lemma B.
3. *The cusp.* Where both adjacent necks are long or broken, a tube $S^2\times S^1\times[0,L]$ in the class of $U$, $L\to\infty$, forces $u=0$: fibrewise Cauchy–Schwarz gives $\int_{\rm tube}|D|^2\ge4\pi^2u^2L$, bounded by the component's charge plus a constant. PLAUSIBLE (T3 Prop. D; the needed upper bound for the charge of a reducible component of a monopole limit is the manuscript's a priori energy bound for the main fields of a limit, in §9 just before Lemma `analysis:finite-data`).
4. *Uniformity.* The toric metrics with $\mathrm{Scal}\ge0$, the corner replacement, the isolation of the positive pieces from one another, and the persistence of the band at faces and corners, all in the right order of choices. PLAUSIBLE; this is manuscript Thm. `estimates:clamp` with §§6–7, rated substantial in R1.

**Lemma 4.3 (the lattice of $P$).** Write $x=v\cdot G$ (even), $u$, $t_b=v\cdot T_b$ (exactly two odd). Then $v_P^2=2xu-2u^2-\sum t_b^2$, $d_1=x-\sum t_b-h_1$, $d_2=x-2u-h_2$. With $I$ as in Proposition 4.2 put $Q_I=v_P^2-\frac12\sum_{i\in I}h_i^2$. Then $Q_I\le-2$, except for type S with $|I|=1$ and $u=z_I=\pm1$, where $Q_I\le2$ and $d_i=0$; and if $u=0$, $v_P^2\le-2$.

*Proof.* Expansion gives
$$Q_{\{1\}}=8z_1u-4u^2-\textstyle\sum_b(t_b-u)^2-\frac12(h_1-2u)^2,\qquad Q_{\{2\}}=8z_2u-4u^2-\sum_bt_b^2-\frac12(h_2-2u)^2,$$
$$Q_{\{1,2\}}=4z_{12}u-2u^2-\textstyle\sum_b(t_b-\frac u2)^2-\frac12\big((h_1-u)^2+(h_2-u)^2\big).$$
For one side, shifting the $t_b$ by $u$ keeps two of them odd, so the third term is at most $-2$; with $a=|u|\ge1$ and $w=\operatorname{sign}(u)z_I\in\frac12\mathbb Z$, $Q\le8aw-4a^2-2$; type R has $w\le0$; type S has $w<\frac12$ or $w<\frac32$, so $w\le1$, and $Q\le-2$ except at $a=w=1$, where $d_i=4(z_I-u)=0$ and $Q\le2$. For two sides, the $t_b-\frac u2$ are integers with two odd, or all half-integers with both $h_i-u$ odd, so the last two terms total at most $-2$; with $w\le\frac12$, $Q\le4aw-2a^2-2\le-2$. If $u=0$, $v_P^2=-\sum t_b^2\le-2$. ∎ VERIFIED: by hand, and exhaustively over $|x|\le14$, $|u|\le5$, $|t_b|\le4$, $|h_i|\le16$, all four index pairs, both types and all admissible $I$ — 19,537,612 instances, no violation; the maxima are $-6$ and $-4$ for type R with one and two sides, $-2$ for type S outside the exception, and $2$ at the exception (`f2_clamp_test.py`).

### 4.4 The family adjunction inequality

**Lemma 4.4.** Let $\Gamma$ be a segment over a point of $\bar Q$ whose positive pieces are at mutual distance at least $2$, carrying reducible components (with bubbles, neck charges and lens caps) that satisfy (J1)–(J4) and Proposition 4.2. Let $s^-(\Gamma)$ be the number of assigned insertions not adjacent to a positive piece of $\Gamma$, and $z_0$ the number of those met only by charge. If $\Gamma$ contains no cap,
$$\kappa_\Gamma\ \ge\ \tfrac12\big(s^-(\Gamma)+m(\Gamma)\big)+\tfrac12z_0 .$$
*Proof.* $v_\Gamma^2=\sum_Zv|_Z^2$ over the pieces (rational orthogonal splitting along rational homology spheres; separated lens caps filled by their references). On a negative piece $-v|_N^2=\frac12(h_r^2+h_l^2)$ for its two (even) halves. An insertion not adjacent to a positive piece is met through a nonzero half of its own, which contributes at least $2$ to $-v^2$, or it carries a charge, which contributes $4$ to $4\ell$. A positive piece together with its two reserved far halves contributes at least $2$ to $-v^2$ by Lemma 4.3, or at least $-2$ in the exceptional case, where the insertion on the selected side is missed and its charge contributes $4$. Distance at least two means no half is reserved twice, and the spheres are disjoint, so the charges are distinct. Summing, $-v_\Gamma^2+4\ell_\Gamma\ge2(s^--z_0)+2m+4z_0$. ∎ VERIFIED given Lemma 1.2 and Proposition 4.2; sharp: the exact minimum of $\kappa_\Gamma-\frac12(s^-+m)$ is $0$ on every segment I computed (§4.5).

In words: in the family each insertion supplies charge $\frac18$ but costs at least $\frac12$ — a nonzero even half costs $\frac18h^2\ge\frac12$, a bubble costs $1$; a positive piece supplies $\frac38$, raises $n_a$ by $\frac58$, and costs $\frac12$ *together with* its two adjacent insertions, because an indefinite piece lets one class pair nontrivially with both. For example, with indices $(0,1)$, $u=0$, $x=2$, $t=(1,0,-1,0)$: $v_P^2=-2$ and both halves in $P$ equal $2$.

On all of $X_M$ (all $n$ insertions assigned, $s^-=n-2m$, each outer piece split rationally into the old cap, its exceptional summands and one trace half): $-\frac14v^2+T(v)\ge\frac12(n-m)-C$, $C=\frac14(C_{W_-}+C_{W_+})$ (T1 Cor. 3.2). VERIFIED given Lemma 4.6(b).

### 4.5 Segment bounds

**Lemma 4.5.** Let $\Gamma$ contain no cap and $m\ge1$ positive pieces at mutual distance at least $k\ge2$; let $a,b$ be the numbers of negative pieces before the first and after the last positive piece, $\epsilon_a,\epsilon_b\in\{0,1\}$ record whether the bounding insertions are assigned to $\Gamma$, and $f=[a=0,\epsilon_a=0]+[b=0,\epsilon_b=0]$. Then $s=L-1+\epsilon_a+\epsilon_b$, $s^+=2m-f$, and Lemma 4.4 gives
$$\epsilon_I\ge(3k-7)m-3k+5,\qquad\epsilon_C\ge(k-4)m-k+2,\qquad\epsilon_S\ge(2k-4)m-2k+2 .$$
For $m=0$: $\epsilon_I\ge1$, $\epsilon_C\ge0$, $\epsilon_S\ge0$. Longer gaps only increase all three.

*Proof.* Substitute $8\kappa_\Gamma\ge4s^-+4m$ and $6\kappa_\Gamma\ge3s^-+3m$ into §3.1, use $L=k(m-1)+1+a+b+g$ with $g\ge0$, and at each end $3a+2\epsilon_a+4f_a\ge2$, $a+\epsilon_a+3f_a\ge1$, $2a+\epsilon_a+3f_a\ge1$, together with $r\ge1$, $\Delta\ge-1$, $r+\Delta\ge0$. ∎ VERIFIED (by hand; and `f4_identities.py` checks that the closed forms are the minima of the bound over all endpoint data for $k=2,\dots,6$, $m=1,\dots,5$).

**Exact minima.** By an independent exact minimization over lattice classes (`f3_segments.py`; negative pieces with the parity condition $\frac12h_r+\frac12h_l\equiv e_j+e_{j+1}\pmod2$, positive pieces with the parities of Lemma 4.3, the vertex alternatives of Proposition 4.2 on unbroken sides, all bundle indices and endpoint assignments, types R, S and mixtures, up to one internal broken neck): see the table in the Appendix. In summary, $\min(\kappa_\Gamma-\frac12(s^-+m))=0$ throughout; $\min\epsilon_I$ equals the closed form; $\min\epsilon_C$ and $\min\epsilon_S$ equal the closed forms except that they are one larger when $k$ and $m$ are both even. At $k=4$:
$$\epsilon_I\ge5m-7\ge-2,\qquad\epsilon_C\ge-2,\qquad\epsilon_S\ge4m-6\ge-2 .$$
The value $-2$ is attained by a single positive piece isolated between two broken necks with both bounding insertions assigned to it: indices $(0,1)$, $u=0$, $x=2$, $t=(1,0,-1,0)$, $\kappa_\Gamma=\frac12$, $\Delta=-1$; then $\epsilon_I=-2$ and $\epsilon_C=\epsilon_S=-2$. VERIFIED.

| spacing $k$ | $8\Delta n_a$ per period | $8\Delta(\ell-T)$ bound per period | $\epsilon_I$ per period | $\epsilon_C$ per period | $\epsilon_S$ per period | fails |
|---|---|---|---|---|---|---|
| 2 | $+3$ | $+1$ | $-1$ | $-2$ | $0$ | (B3), (B4), (B5) coarse |
| 3 | $+2$ | $-2$ | $+2$ | $-1$ | $+2$ | (B5) coarse only |
| 4 | $+1$ | $-5$ | $+5$ | $0$ | $+4$ | nothing |
| 5 | $0$ | $-8$ | $+8$ | $+1$ | $+6$ | growth of $n_a$ |

VERIFIED (`f4_identities.py`).

### 4.6 The caps

**Lemma 4.6.** Choose in order: the caps and their metrics; the number of copies of $\phi_*B$ next to each cap; the odd values $\langle\Lambda_0,E_\pm\rangle$; and only then $M$. Then:
- (a) no type R component contains a cap ($\langle w,A_\pm\rangle$ is odd, so the class restricts nontrivially; the cap periods are fixed and generic and avoid the finitely many walls of classes of bounded square);
- (b) a type S component containing the old cap $W$ has $v_W^2\le C_W$ and $(\Lambda_W+v_W)^2\le C_W$, with $C_W$ independent of $M$ and of $\langle\Lambda_0,E_\pm\rangle$;
- (c) every type S component containing a cap has $q_j+4\ge8$: long ones by Lemma 4.4, short ones because the tangential bound $d_s+p+4\ell\ge0$ and (b) bound $|K\cdot E_\pm|$, so $|v\cdot E_\pm|\ge|\Lambda\cdot E_\pm|-B$ is large.

PLAUSIBLE (manuscript Prop. `estimates:cap`, Lemma `indices:end-exclusion`; T1 §3.5). The classical content is generic periods and the boundedness of $K\cdot E$ for basic classes of a blow-up, the device Feehan and Leness use when they take $c_1(\mathfrak t)$ large.

### 4.7 The exclusion theorem

> **Theorem C.** Let $X=X_M$ with $u=(\phi_*B)^3HB$. Make the choices of Lemma 4.6, and take $M$ in the congruence classes making $c_2(E_e)$ and $n_a$ integral. Assume (B1), Proposition 4.2 and Lemma 4.6, uniformly over $\bar Q$. Then for every sufficiently large $M$:
> - (a) $n_a=\frac18(M-p)+c_1\ge1$;
> - (b) (B3) holds, with $\ell-T(v)\le\frac18(-5M-3p+c_\kappa)+C<0$;
> - (c) (B4) holds, with $\epsilon_I\ge-2$;
> - (d) (B5) holds in both forms, $\epsilon_C\ge-2$ and $\epsilon_S\ge-2$;
> - (e) (B2) holds.
>
> Consequently, under (A1)–(A7), Theorems A and B give $2^{n_a-1}\Omega(X_M)=0$, so $\Omega(X_M)=0$.

*Proof.* (a) Proposition 4.1(c). (b) The global form of Lemma 4.4: $\ell-T(v)\le\kappa-\frac12(n-m)+C=\frac18(7m-3n+c_\kappa)+C$, negative once $5M+3p>c_\kappa+8C$. (c), (d) Lemma 4.5 at $k=4$; segments next to the outer pieces contain the extra negative pieces, which only help, and segments containing a cap are covered by (e). (e) Lemma 4.6. All of (b)–(d) use (B1). ∎ VERIFIED as a deduction; the inputs as labelled.

**Corollary D (outside the relation).** Combined with Step 2 of the Strategy — $\Omega(X_M)\equiv\pm q\not\equiv0\pmod{2^N}$ for $M$ divisible by the exponent of $\mathrm{GL}_r(\mathbb Z/2^N)$ — this contradicts the existence of $\phi$. SPECULATIVE as a whole: besides everything above it needs $\Omega(X_M)=\pm$ the Floer pairing (PLAUSIBLE), computed with the same representatives of $\mu(S_i)$ as in $\mathcal Z_e$ (the manuscript uses holonomy representatives; comparing the two choices needs the same exclusions for the cut-down instanton spaces, PLAUSIBLE), that $B$ is an integral chain map (PLAUSIBLE), and that $B$ inverts $H$ modulo two up to a fixed automorphism, which the Round 3a referee demoted to "expected" (the identity $HB\equiv1$ holds only up to fixed Floer automorphisms, a degree-four twist).

### 4.8 Consistency checks

1. *Spacing one, $(HB)^M$.* Without $\phi$ every copy of $B$ is followed by $H$; Lemma 4.4 fails (each negative half is claimed by two positive pieces) and $3n-7m=-4M$, so (B3) fails without bound (`numerology.tex` §5 exhibits classes at nonnegative level). It must fail, since Step 2 gives nonzero pairings $\langle\Psi_+,(HB)^M\Psi_-\rangle$ with $n_a\to\infty$ for every nontrivial knot. VERIFIED.
2. *Spacing two.* $3n-7m=-M+3p$: (B3) fails. VERIFIED.
3. *Closed manifolds.* Without the family an insertion supplies $\frac14$ rather than $\frac18$; growth of $n_a$ then needs $m/n>\frac25$ and exclusion needs $m/n<\frac27$, an empty window. The family is essential. VERIFIED.
4. *The trivial knot.* For the unknot $Y_{\pm2}\cong\mathbb{RP}^3$ and a $\phi$ exists; nothing in Theorems A–C uses that $K$ is nontrivial, so they predict $\Omega(X_M)=0$ there. This is consistent: Floer's irreducible groups of $\mathbb{RP}^3$ vanish, so $\Omega(X_M)=0$ there for trivial reasons, and Step 2 needs $K$ nontrivial. VERIFIED as logic (the vanishing of the irreducible groups of $\mathbb{RP}^3$ PLAUSIBLE).
5. *A test that could refute the method.* The exclusion uses $\phi$ only as a return $Y_{-2}\to Y_2$ with $b_1=b^+=0$ that is a mod-2 equivalence (T4 §1). A pair of negative-definite mod-2 equivalences $V\colon Y_{-2}\to Y_2$, $V'\colon Y_2\to Y_{-2}$ for a nontrivial knot (with $\pi_1(V')$ normally generated by one end) would therefore contradict Theorems A–C together with Step 2. I found none. Ozsváth–Szabó's inequality for correction terms under negative-definite cobordisms obstructs such $V$ for many knots, apparently for all with $V_0(K)>0$; for a slice knot the homology cobordisms obtained from a concordance to the unknot pass through $\mathbb{RP}^3$, whose irreducible Floer group vanishes, so their composites induce zero. SPECULATIVE.

---

## 5. Where the drafts err or disagree, and my decisions

1. **Exact segment minima (Draft 1 wrong, Draft 2 right).** Draft 1's minimization (`relation-checks/c3_segments.py`) allows every pair of even halves on a negative piece. But $v\equiv w\pmod2$ on $\langle-1\rangle^2$ forces $v\cdot a\equiv v\cdot b\equiv e_j+e_{j+1}$, i.e. $\frac12h_r+\frac12h_l\equiv e_j+e_{j+1}\pmod 2$ (VERIFIED, `f1_lattice.py`). Its lower bounds are unaffected (it minimized over a larger set), but its statements that the closed forms are attained — "$\min\epsilon'_m=-2m$ ($-8$ at $m=4$)" at spacing two, and the agreement claimed in its Appendix — are false when $k$ and $m$ are both even: the true minima are one higher ($\epsilon_C=-3$, not $-4$, at $k=m=2$, and $-7$, not $-8$, at $k=2$, $m=4$; $\epsilon_S=-1$, not $-2$, in both cases). Dropping the parity condition from my own computation reproduces Draft 1's numbers exactly, so this is the cause. Draft 2's `c3b` imposes the parity and states the "+1 when $k,m$ even" correction; my independent computation agrees (Appendix). Nothing in the exclusion depends on this.
2. **Notation.** The drafts swap primes: Draft 1's $\epsilon'_m$ (parameters kept) is Draft 2's $\epsilon_{\rm mon}$, and Draft 1's $\epsilon_m$ (parameters dropped) is Draft 2's $\epsilon'_{\rm mon}$. I write $\epsilon_C$ and $\epsilon_S$.
3. **The misprint in FL2b.** The formula $d_a=-2p_1-\frac32(\chi+2\sigma)$ is FL2b (3.21), not (3.20) as Draft 2 says; (3.20) is $\dim\mathcal M^{*,0}_{\mathfrak t}=d_a+2n_a$. VERIFIED.
4. **The global inequality.** Draft 1's (E0) asks the inequality for all reducible configurations, broken or not; Draft 2's (B3) asks it only for unbroken Seiberg–Witten solutions and handles broken fully reducible limits by (B2) and (B4). Both suffice; I follow Draft 2, which needs less.
5. **(E0).** Both drafts list the finiteness and interiority of the cut-down instanton spaces as an analytic hypothesis. Its exclusion part is not analytic; it follows from (B2) and (B4) by the same count (§3.3).
6. **Coupled regularity at type A components.** Both drafts observe that broken limits with only free and type A components need (A3). I agree (§2.3 Step 4). It is new relative to `strategy.tex` and T1, but already covered by the manuscript's Def. `indices:analytic-hypotheses`(iii), which applies to every limit containing a free component.
7. **Weights.** Draft 1 says the off-diagonal anti-self-dual cokernel has weight $\pm1$ under the abelian circle; it has weight $\pm2$ under $\mathrm{diag}(z,z^{-1})\subset\mathrm{SU}(2)$ (the spinor summands have weight $\pm1$). Immaterial: only nonzero weight matters.
8. **"Open: nothing the argument strictly needs" (Draft 1) versus a list of new constructions (Draft 2).** Nothing the argument needs is known to be false, and the obstructed gluing alternative is open but unnecessary; but (A3), (A5), (A7) and the uniform clamp are new constructions with no external confirmation. I follow Draft 2.
9. **Confidence.** Draft 1 says about 40%, Draft 2 about 30%. I side with Draft 2 (§7).
10. **Citations.** Every Feehan–Leness, Memoir and FL6 number cited by either draft is correct except item 3 (Appendix A.1).

---

## 6. What is proved, what is plausible, what is open

**Proved here or checked against sources (VERIFIED).**
- Lemma 1.1 (constancy of $d_a,n_a$; distinct, good $w_2$; even halves), Lemma 1.3 (index identities, as algebra), $\dim\mathcal Z_e=1$.
- Theorem A as a deduction from (A1)–(A6), (E0), (E); Theorem B as a deduction from (A1)–(A7) and (B1)–(B5); both thresholds sharp for the method.
- The excess formulas, the projected indices $I$ and $I'$, and the sharper count as logic given (A7′).
- Lemma 4.3 (by hand and exhaustively), the convexity step, Lemma 4.4 given Lemma 1.2 and Proposition 4.2, Lemma 4.5 and the exact segment minima, Proposition 4.1 and the per-block data, Theorem C as a deduction, the consistency checks 1–3.
- The Feehan–Leness, Memoir and FL6 citations (Appendix A.1).

**Plausible, routine extensions (PLAUSIBLE).**
- (A1) compactness over $\bar Q$; (A2) single-component regularity; (A4) instanton links with parameters; (A6) weighted Stokes.
- Transversality of the jumping-line representatives, the analytic part of (J4), general position of supports, the lens index table and reference fillings, additivity of indices.

**Plausible, substantial and new (PLAUSIBLE).**
- (A3) coupled regularity, by multivalued perturbations sampling a free component.
- (A7) the necessary projection, and (A7′) its parameter-local form.
- (A5) the lens ends in the monopole problem: gluing the minimal trace cap, and the orientation comparison across different $w_2$.
- Proposition 4.2 uniformly over the cube (toric metrics with $\mathrm{Scal}\ge0$, the cusp tube, isolation, persistence at faces and corners); Lemma 4.6 (caps).

**Open.**
- Obstructed gluing at abelian segments in families with faces (not needed).
- Outside the statement, for the contradiction: $B$ inverts $H$ modulo two up to a fixed automorphism (expected); $\Omega(X_M)=\pm$ the pairing.

**The single hardest point.** The necessary projection at mixed limits, (A7), together with the coupled regularity (A3) on which it rests.
1. It replaces a gluing theorem that Feehan and Leness leave as a hypothesis even on a closed manifold (Memoir Hyps. 7.8.1, 11.3.5).
2. It needs multivalued perturbations coupling distant pieces through the phase of a free component, vanishing wherever the sampled data have positive-dimensional isotropy, compatible with Uhlenbeck compactness at faces and corners, with the instanton links and with the lens pairing, chosen inductively over the degenerations.
3. Nothing in the literature covers it; the manuscript writes an argument whose structure checks, without external confirmation.
4. It has a margin of exactly one dimension: at a single positive piece isolated between two broken necks next to two non-R components, the projected index is $-1$ in both counts. (That extremal configuration needs an abelian instanton on a piece with no free parameter, i.e. $v\cdot H=0$ at a fixed period, which a generic choice of the corner metric excludes; the argument does not use this, and for the coarse count other extremal segments, such as a positive piece between two negative pieces, do occur on walls.) PLAUSIBLE for the parenthesis.

The next two points, in order, are the uniform control of Seiberg–Witten classes on $P$ over the cube and its corners (Proposition 4.2, ingredient 4) and the orientation comparison in (A5).

---

## 7. Verdict and confidence

**Verdict.**
- *Formulation.* The family version of FL2b Thm. 3.33(a) is Theorem A. It is stated in Feehan and Leness's terms: the classes $\mu_p$ and $\mu_c$ (the latter by sections sampling every piece), the link $\{\|\Phi\|^2=\varepsilon\}$ of the instanton stratum with the count $2^{n_a-1}$ of FL2b Prop. 3.29, levels $\ell=\kappa_\Gamma+\frac14v_\Gamma^2$ computed piece by piece, and Seiberg–Witten strata $\iota(M_{\mathfrak s})\times\mathrm{Sym}^\ell$ on the pieces of every face, zero-spinor part included. Its proof is Feehan and Leness's Stokes argument plus three family-specific ingredients: the index identities at $S^3$-faces, the cancellation of lens ends in pairs, and coupled regularity. No gluing at reducibles is used. Correct as a conditional theorem.
- *Family-specific hypotheses.* (i) is the description of §1.5; (ii) is (B4) with threshold $-3$ and (B5) with threshold $-2$, both sharp for the method; (iii) is the necessary projection (A7), or an obstructed gluing theorem that nobody has.
- *Exclusion.* For $u$ and large $M$ all the inequalities hold, by the family adjunction inequality (proved here, sharp) and the numerology, given the incidence of the jumping-line divisors, the control of Seiberg–Witten classes on $P$ and the cap estimates. Correct as a deduction.
- *New observation, endorsed.* With parameter-local perturbations the mixed-limit condition holds at every spacing $\ge2$, so spacing four is an artifact of keeping the parameters of the deleted segments; spacings three and four would both serve. PLAUSIBLE.

**Confidence.**

| claim | label | confidence |
|---|---|---|
| arithmetic: Lemma 1.1, Lemma 1.3, Prop. 4.1, Lemma 4.3, Lemma 4.4 given its inputs, Lemma 4.5, exact minima | VERIFIED | 97% |
| Theorem A as a deduction; Theorem B as a deduction; Theorem C as a deduction | VERIFIED | 90% |
| (A1), (A2), (A4), (A6) | PLAUSIBLE | 80–85% each, correlated |
| (A5) lens ends with orientations | PLAUSIBLE | 70% |
| (A3) and (A7), exclusion of mixed and of free-plus-instanton limits | PLAUSIBLE | 50–55% |
| (A7′) and the sharper count | PLAUSIBLE | 65% |
| Proposition 4.2 uniformly over $\bar Q$; Lemma 4.6 | PLAUSIBLE | 65% |
| incidence (J1)–(J3); (J4) | VERIFIED / PLAUSIBLE | 95% / 80% |
| **the statement as a whole**: for $u$ and large $M$, the hypotheses of Theorem A hold and $2^{n_a-1}\Omega(X_M)=0$, by this route | PLAUSIBLE | **about 30%** (25–35%) |

A naive product of the rows gives 10–15%. The rows are positively correlated — the routine extensions, (A3), (A5) and (A7) all rest on one perturbation framework and stand or fall together — so I put the whole at about 30%. The part concerning indices and lattices is not in doubt. The contradiction with the existence of $\phi$ needs in addition the Floer-theoretic inputs of Step 2, of which "$B$ inverts $H$ modulo two" is only expected.

---

## Appendix: report of the checks

All files are in `round3/relation-final-checks/`. All computations use exact integer or rational arithmetic and are independent of the drafts' computations and of T1's.

### A.1 Citations, recomputed from the LaTeX counters

Numbering was recomputed with `num.py` (sections) and `numbook.py` (chapters), which follow `\newtheorem` with shared counters, `\numberwithin`, and numbered `equation`/`align` lines.

| citation | content found | status |
|---|---|---|
| FL1 Thm. 1.1, Thm. 1.3 | compactness; transversality | correct |
| FL1 Lemma 4.2, Lemma 4.4 | $L^4$ bound via $\|\mathrm{Scal}\|_{L^2}$; $C^0$ bound via $\|\mathrm{Scal}\|_{C^0}$ | correct |
| FL1 Def. 4.19, Thm. 4.20 | Uhlenbeck topology; sequential compactness | correct |
| FL2a Thm. 2.13; Prop. 3.1; Lemma 3.2; Cor. 3.3; Lemma 3.13 | transversality; classification of fixed points (excludes zero-section reducibles for generic metric, via DK Cor. 4.3.15); Morgan–Mrowka criterion; no zero-section SW points; reducibles are SW | correct |
| FL2b (3.10), (3.12) | $\mathbb L_{\mathfrak t}$; $\mu_c=c_1(\mathbb L_{\mathfrak t})$ | correct |
| FL2b (3.20), (3.21) | $\dim\mathcal M^{*,0}=d_a+2n_a$; formulas for $d_a,n_a$ with the misprint $\chi+2\sigma$ | misprint is in (3.21) |
| FL2b Lemmas 3.12, 3.13, 3.15; (3.24)–(3.26); Lemma 3.17; Cor. 3.18 | representatives; extension to lower strata; codimension bounds 5 and 4; $\deg z+2\delta_c=d_a+2n_a-2$; intersection-suitability; one-manifolds disjoint from lower strata | correct |
| FL2b Def. 3.20; Lemma 3.21; Lemma 3.22 | good classes; $\bar M^{\rm asd}_{\mathfrak t}=\iota(\bar M^w_\kappa)$; deforming $\mathcal V$ near instantons | correct |
| FL2b Lemmas 3.24–3.25, 3.27, 3.28; Prop. 3.29; (3.60) | orientations; cokernel gives $h^c$; $\mu_c=2h$; link count $2^{n_a-1}\#$ | correct |
| FL2b (3.62); Lemma 3.32; (3.63)–(3.64); Thm. 3.33; (3.67)–(3.69); Conj. 3.34 | the one-manifold; splitting criterion; lower-level reducibles; vanishing theorem (a) under (3.68); multiplicity conjecture | correct |
| Memoir (2.1.12), (2.3.14); Hyp. 7.8.1; Lemma 11.1.1; Hyp. 11.3.5 | $d_a,n_a$; $\ell(\mathfrak t,\mathfrak s)$; local gluing hypothesis; reducibles in $\bar M^w_\kappa(g_0)$; parametrized gluing hypothesis | correct |
| FL6 Hyp. 3.1 | local gluing map properties | correct |
| math/9907107 | *PU(2) monopoles. III* (FL3), not FL2a | source list wrong |

### A.2 Computations

- **`f1_lattice.py`.** On $P$: halves orthogonal of square $-2$, each meeting $U$ once; $\Theta=1+\frac12(e-f)$; parities $x$ even, $u\equiv1+e+f$, $t\equiv(1,0,1,0)+e$ (exactly two odd); the vertex values $\lambda_I$. On $N$: $\Theta=\frac12(e-f)$ and $v\cdot a\equiv v\cdot b\equiv e+f\pmod2$. $\Lambda_e^2$ constant iff $\langle\Lambda_0,S_i\rangle=2$. All pass.
- **`f2_clamp_test.py`.** (i) The exact test for the band or wall over the admissible period set agrees with a $41\times41$ rational grid on 20,000 random instances. (ii) Band or wall $\Rightarrow$ vertex alternative: 35,152 instances, 0 violations. (iii) Lemma 4.3: 19,537,612 instances, 0 violations, maxima as stated.
- **`f3_segments.py`** (with the variants `f3k_segments.py`, `f3m_segments.py`, which select the spacing and the number of positive pieces, and `f3k_noparity.py`, which drops the parity condition on negative pieces). Exact minimization of $4\kappa_\Gamma=-v_\Gamma^2+4\,\#(\text{missed assigned insertions})$ over all lattice classes in a box (halves $|h|\le8$, $|x|\le10$, $|u|\le3$, $|t_b|\le4$; minima are attained well inside), by recursion along the segment, for every word with positive pieces at exact spacing $k$ and up to two extra negative pieces at each end, all bundle indices, both assignments of each bounding insertion, types R, S and mixtures, and up to one internal broken neck. Output: the minima of $\kappa_\Gamma-\frac12(s^-+m)$, $\epsilon_I$, $\epsilon_C$, $\epsilon_S$ (table below).
- **`f5_examples.py`.** The explicit configurations quoted in the text.
- **`f6_dp_validate.py`.** The recursion of `f3` against brute-force enumeration on short segments.
- **`f4_identities.py`.** Symbolic checks of Lemma 1.3, $\dim\mathcal Z_e=1$, the excess formulas, the projected indices $I$ and $I'$, the numerology, and the closed-form minima of the lower bound over endpoint data.

**Exact minima** (vertex form of Proposition 4.2; closed forms in brackets):

| $k$ | $m$ | $\min\big(\kappa_\Gamma-\frac12(s^-+m)\big)$ | $\min\epsilon_I$ | $\min\epsilon_C$ | $\min\epsilon_S$ | scope |
|---|---|---|---|---|---|---|
| any | 0 | 0 | 1 [1] | 1 [0] | 1 [0] | a |
| 2 | 1 | 0 | $-2$ [$-2$] | $-2$ [$-2$] | $-2$ [$-2$] | a |
| 2 | 2 | 0 | $-3$ [$-3$] | $-3$ [$-4$] | $-1$ [$-2$] | a |
| 2 | 3 | 0 | $-4$ [$-4$] | $-6$ [$-6$] | $-2$ [$-2$] | a |
| 2 | 4 | 0 | $-5$ [$-5$] | $-7$ [$-8$] | $-1$ [$-2$] | b |
| 3 | 1 | 0 | $-2$ [$-2$] | $-2$ [$-2$] | $-2$ [$-2$] | a |
| 3 | 2 | 0 | $0$ [$0$] | $-3$ [$-3$] | $0$ [$0$] | a |
| 3 | 3 | 0 | $2$ [$2$] | $-4$ [$-4$] | $2$ [$2$] | a |
| 4 | 1 | 0 | $-2$ [$-2$] | $-2$ [$-2$] | $-2$ [$-2$] | a |
| 4 | 2 | 0 | $3$ [$3$] | $-1$ [$-2$] | $3$ [$2$] | a |
| 4 | 3 | 0 | $8$ [$8$] | $-2$ [$-2$] | $6$ [$6$] | c, d |
| 4 | 4 | 0 | $13$ [$13$] | $-1$ [$-2$] | $11$ [$10$] | b |
| 5 | 1 | 0 | $-2$ [$-2$] | $-2$ [$-2$] | $-2$ [$-2$] | a |
| 5 | 2 | 0 | $6$ [$6$] | $-1$ [$-1$] | $4$ [$4$] | a |
| 5 | 3 | 0 | $14$ [$14$] | $0$ [$0$] | $10$ [$10$] | e |

Scope: (a) up to two extra negative pieces at each end and at most one internal broken neck (for $m=0$: one to three negative pieces, at most one internal broken neck); (b) no extra pieces and no internal broken neck; (c) no extra pieces and at most one internal broken neck; (d) up to two extra pieces at each end and no internal broken neck; (e) up to one extra piece at each end and no internal broken neck. The exact band-or-wall form of Proposition 4.2 (instead of its vertex consequence), computed for $k=2,3,4$, $m\le3$ with scope (b), gives the same minima in every case (`out_f3_band_off0.txt`). With the parity condition on negative pieces removed, the minima at $k=2$ drop to $\epsilon_C=-4,-8$ and $\epsilon_S=-2,-2$ for $m=2,4$, which are Draft 1's numbers (`f3k_noparity.py`). The recursion was checked against brute-force enumeration on 656 short segments (`f6_dp_validate.py`, 0 mismatches), and the explicit configurations quoted in §4.5 and §5 were recomputed (`f5_examples.py`: isolated positive piece $\kappa_\Gamma=\frac12$, $\epsilon_I=\epsilon_C=\epsilon_S=-2$; $PNNP$ with indices $(0,1,0,0,1)$: $\kappa_\Gamma=\frac32$, $\epsilon_I=0$, $\epsilon_C=-3$, $\epsilon_S=0$).

### A.3 The drafts' computations

- Draft 1, `relation-checks/c3_segments.py`: no parity condition on negative pieces (list `NOPT`); hence the error of §5.1. Its positive-piece check `c2_positive_piece.py` imposes the correct parities.
- Draft 2, `relation2-checks/c3b_segments_fast.py`: parity imposed (`Ndata[(e0+e1)%2]`), no internal broken necks; `c6` adds one. Its output agrees with mine where they overlap.
