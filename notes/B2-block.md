# B2. Does the reducible exclusion localize to a period block with Floer ends?

Thread B2 of BRIEF.md (round 2). Manuscript labels refer to `src/*.tex`. Tags: **[V]** means checked by hand or by script; **[P]** means plausible; **[S]** means speculative. Scripts: `agents/B2-checks/pprime.py` (lattice of the cut positive cell and the HB candidate) and `agents/B2-checks/runs.py` (brute-force run bounds at a Floer end). Literature is cited from memory.

## 0. Verdict

1. **The budget localizes, but it cannot see φ [V arithmetic, P analysis].** Take a φ-block with irreducible Floer ends, i.e. the macro $BHB$ inside and negative trace halves at both ends.
   - Every S/R fixed tuple is excluded for any length $n_b\ge2$, with no spacing condition (Prop. F).
   - Every mixed P/R tuple is excluded **iff** the end Dirac defects vanish, $\delta_0=\delta_1=0$ (§2.4). If some $\delta_e\neq0$, an explicit tuple survives at one end, whatever the pad lengths (Prop. M).
   - *The same holds for the φ-free block $HB$:* when $\delta=0$, $HB$ has no reducible survivors either (§4). But $HB\simeq\mathrm{id}$ (mod 2) with spin shift $-\tfrac12$, so monotonicity must fail for $HB$.
   - Hence the irreducible-ended budget is not the mechanism that separates φ-blocks from $HB$.
2. **What survives is a localization identity with an end term [P].**
   $$2^{n_*-1}F^{(n_*)}=\partial K+K\partial+\mathcal E,$$
   where $\mathcal E$ counts codimension-one breakings at the $Y_2$ ends through $\mathrm{PU}(2)$ critical points with $\Phi\ne0$, or through $\Phi\ne0$ cylinders between flats.
   - $\mathcal E$ is end-local and is not controlled by any estimate in the manuscript.
   - $Y_2$ has no psc metric, and $HM^{\rm red}(Y_2)\ne0$ forces $\Phi\ne0$ critical points to exist (§3).
   - $HB$ proves that $\mathcal E$, or the failure of $\partial$ to be spin-filtered, is nonzero.
3. **φ enters through θ-throughput, not through a single block [V arithmetic, S as theory].** In the closed stack, Abelian R-runs cross $Y_2$ seams through the central flats $\theta_e$ at no cost. Per block, such a run changes the score by $T_{\rm fix}=3k-7$ and $T_{\rm mix}=k-4$; for $HB$ these are $-4$ and $-3$. So a φ-sensitive block theorem must be stated in a theory that has $\theta_0,\theta_1$ as generators (an equivariant or framed $\mathrm{PU}(2)$ theory). There the condition is $k\ge4$ ($k\ge3$ for the fixed part only), which is exactly the manuscript's spacing.

**Confidence.**

| Claim | Confidence |
|---|---|
| The irreducible-ended exclusion localizes (given $\delta=0$) | ~75% |
| That exclusion does not yield block monotonicity, because the end term $\mathcal E$ is unavoidable | ~80% |
| A DLME-style proof built from block maps on Floer's irreducible complex $C(Y_2)$ alone can work | ≤10% |
| A θ-inclusive $S^1$-equivariant $\mathrm{PU}(2)$ Floer version with $k\ge4$ can work | 20–30% [S]; needs at least three major new constructions (§6) |

**Main obstruction, plainly:** localizing to Floer ends exposes the $\mathrm{PU}(2)$ Floer data of $Y_2$. The manuscript's closed stack exists precisely to avoid that data: its Y-seams stay finite, the $\delta$-terms telescope ($j_L+j_R=0$), and no breaking at $\Phi\ne0$ points can occur.

## 1. Setting

- **The block.** $W_{a,b}$ is, chronologically, $(B\phi)^a$, then $B,H,B,\phi$, then $(B\phi)^b$.
  - It has $n_b=a+b+2$ intervals with cuts $J_1,\dots,J_{n_b}$.
  - Cell $c_i$ lies between $J_i$ and $J_{i+1}$. The positive cell is $c_{a+1}$, the full cell $P$ with $Q_P=H\oplus4\langle-1\rangle$, carrying $U$ and the plumbing $(-4,0,-4)$, hence the clamp.
  - The end halves are $H_L=(-C_2)\setminus B^4$ ($Y_2\to S^3$, class $F_{l,1}$ of square $-2$) and $H_R=C_{-2}\setminus B^4$ ($S^3\to Y_{-2}\cong_\phi Y_2$, class $F_{r,n_b}$ of square $-2$).
  - The spin shift is $(n_b-5)/8$ (brief).
- **The entry.** An entry is $(\alpha,\alpha')$, a pair of irreducible flats on $Y_2$.
  - The rigid ASD condition is $\mathrm{ind}=n_b$.
  - $n_*=n_D(\alpha,\alpha')\in\Z$, and the number of phase cuts is $\eta=n_*-1$.
- **Limiting tuples.** A tuple has
  - $k$ true $J$-cuts and main components $C_0,\dots,C_k$;
  - **end levels**, i.e. cylinder levels on $\mathbb R\times Y_2$ from $\alpha$ to $\lim C_0$ and from $\lim C_k$ to $\alpha'$;
  - **contacts** at intermediate $Y_2$ critical points $\beta$, with stabilizer dimension $h^0$:
    - $h^0=3$ at the two central flats $\theta_0,\theta_1$ ($H^1(Y_2)=\Z/2$, so these are the only reducible flats);
    - $h^0=0$ at irreducible flats;
    - $h^0=0$ for the gauge group at $\Phi\ne0$ points [P].

## 2. Q1: the index budget with Floer ends

### 2.1 Virtual sums [V]
The total ASD index is $n_b$ and the total spinor index is $2n_*$. The interior is as in `indices:virtual-sums`. Put $c_e:=\sum_{\text{levels}}\mathrm{ind}+\sum_{\text{contacts}}h^0\ge0$ at each end. Then
$$\sum_i(q_i+4)+\sum_{\rm ends}c_e=4,\qquad \sum_i i_i+\sum_{\rm ends}c^{\rm sp}_e-2\eta=2-4k.$$
These are the manuscript's identities. The end costs replace the caps.

Per component, with $f_i\in\{0,1,2\}$ the number of Floer-end halves in $C_i$ (so $p_i=L_i-1+f_i$), and with central ends unframed:
$$q_i+4=8\kappa_i+L_i-3m_i-2s_i+f_i .$$
So a Floer-end half acts like a cell with a retained parameter: it gives $+1$. For R/S components $\kappa_i=-v_i^2/4+\ell_i$ still holds. The reason is that $v\equiv c \pmod 2$ and $2H^2(Y_2)=0$, so $v|_{Y_2}=0$ and the end is a central flat.

### 2.2 What replaces the cap scores

| | Caps (closed stack) | Floer end at an irreducible $\alpha$ |
|---|---|---|
| Outer A | $q+4\ge4$ | same: $q+4\ge4$, with equality iff rigid with limit $\alpha$ |
| Outer R | excluded (generic cap periods) | **allowed.** It needs a level $\alpha\to\theta_e$ (index $\ge1$) and the contact $h^0=3$, so $c_e\ge4$ [V] |
| Outer S | $q+4\ge8$ (large $\Lambda(E_{\rm exc})$) | Same route via $\theta_e$, with $c_e\ge4$. A route through a SW-irreducible $\sigma$ needs an $S^1$-fixed level from $\alpha$, which is impossible, so σ is reached only as $\theta\to\sigma$ inside the S-configuration |
| Spinor budget of an outer R | none | **new end term** $2j_e$ (below) |

**End Dirac defect.** For the central flat $\theta_e$, the corresponding line $L_e$ and the $Y_2$ metric/perturbation $g$, define
$$j_L(e)=\mathrm{ind}_{\mathbb C}D^+\big(H_L;\ E=L_e\oplus L_e,\ \Lambda\big)\quad\text{(APS)},\qquad j_L(e)=2\delta_e,\ \ \delta_e\in\Z .$$
- **[V] The psc model gives $\delta=0$.** Replace $Y_2$ by round $\mathbb{RP}^3$ and $H_L$ by the $(-2)$-disk bundle. The $\mathbb F_2$ versus $\mathbb P(1,1,2)$ comparison gives Dirac index $0$ for $|k(S)|\le2$.
- **[V by excision, given $D_{\theta}$ invertible] $j_R(e)=-j_L(e)$.** The reason is that $H_R\cup_{Y_2}H_L=N_\phi$ (negative cell) has $\Theta=0=\kappa$.
- **[P] Meaning of $\delta_e$.** It is the integer by which the Dirac spectral flow at $\theta_e$ on $(Y_2,g)$ differs from the psc model, i.e. a shift of $n(Y_2,\mathfrak s_e,g)$, the grading of the SW reducible.

### 2.3 Fixed-type exclusion localizes (Prop. F) [V arithmetic]
**Prop. F.** Let $W_{a,b}$ be a φ-block with $n_b\ge2$ and any $a,b\ge0$. Then every fixed-type tuple is a single unbroken A-instanton. No $\delta$ and no spacing condition enter.

*Run bounds.* These come from the manuscript's charge bound $8\kappa\ge4s_N+4m$ (clamp included) plus the extra $f_i$.
- A run of R/S components touching a Floer end has $s=L+\varepsilon$. Its score satisfies
  $$\Sigma(q+4)\ge\max(2s+L-7m+1,\ m+L-2s+1)\ge-1 .$$
  The case $a=0$, $L=1$, $\varepsilon=1$ gives $-1$.
- Brute force (`runs.py`) gives minimum $-1$ for $a=0$ and $+1$ for $a\ge1$.
- A whole-block R/S component has score $\ge\max(3n_b-6,\,2-n_b)\ge0$ for $n_b\ge2$, plus two end costs $\ge8$.

*Conclusion.* Items are A components or R/S Floer-end contacts, each $\ge4$. Runs between them are $\ge-2$ (interior, `indices:fixed-run`, which holds with $m\le1$ for any spacing). So for $k\ge1$ the total is $\ge2\#\text{items}+2\ge6>4$. For $k=0$ the total is $\ge8>4$.

The same budget gives the ordinary rigid count, and agrees with `stack:macro` and `stack:local-excess`.

### 2.4 Mixed exclusion holds iff $\delta=0$ (Prop. M) [V arithmetic, P conventions]
**Projected dimension.** Substitute the sum identity into (`analysis:projection`), with levels retained modulo translation:
$$D=5-4N-\sum_{R}(4+i_i-p_i)-\lambda_{\rm nonR}-3c_\theta-\mathrm{pen}.$$
Here $N$ is the number of non-R main components, $\lambda_{\rm nonR}$ the number of non-R end levels, and $c_\theta$ the number of central contacts.

A Floer end with an R outer component costs $1+3=4$, the same as a non-R component. Hence for $k\ge1$, $N':=N+\#(\text{R-ends})\ge2$. Exclusion requires every R-run to score at least $-2$.

**R-run touching the left end.** By the manuscript's derivation, with $j$ inserted,
$$\Sigma(4+i-p)\ \ge\ r+s-4m+3\,\mathrm{miss}+\Delta+2j_L .$$
- If the positive cell is not in the run ($m=0$), the minimum is $1+4\delta_e$: the run is $H_L$ alone, flat, with no test.
- If $m=1$, the bound is $a-2+4\delta_e$.
- At the right end the bounds are $1-4\delta_e$ and $b-2-4\delta_e$.
- Brute force with $j=0,\pm2$ agrees (`runs.py`).

**Prop. M.**
- If $\delta_0=\delta_1=0$, every mixed tuple in every φ-block with $n_b\ge2$ is excluded, except
  - unbroken free points,
  - single trace-minimum lens ends (cancelling in bit pairs), and
  - the codimension-one Floer breakings of §2.5.
- If $\delta_e\le-1$, the tuple
  $$T_L(e)=\{\text{level }\alpha\to\theta_e,\ \text{flat R on }H_L,\ J_1\text{ cut},\ \text{P on the rest}\}$$
  has $D=-4-4\delta_e\ge0$, so it is not excluded.
- If $\delta_e\ge1$, the mirror tuple $T_R(e)$ has $D=-4+4\delta_e\ge0$.
- In both cases pads do not help, since the $m=0$ run does not involve them.

Whether $\delta=0$ is attainable is open [S]. Two observations:
- Ni–Wu force $V_0=0$, so $d(Y_2)=d(\mathbb{RP}^3)$. This is consistent with $\delta=0$ but does not imply it.
- A translation-invariant (non-small) Dirac perturbation on the ends could shift $\delta$, at the cost of changing the 3D critical set.

### 2.5 Codimension-one breakings that index cannot remove [V]
For $k=0$ with one non-R level at a non-central $\beta$, $D=1-1=0$. These are genuine boundary points of the 1-dimensional space:
- (a) an A-level (Floer differential) times a P-block, which gives $\partial K+K\partial$;
- (b) a P-level times a block, where $\beta$ is a $\Phi\ne0$ critical point or $\beta$ is a flat joined by a $\Phi\ne0$ cylinder. These give $\mathcal E$.

$D$ is independent of $\eta$ and of the interior. Central contacts give $D=1-1-3<0$ and are excluded.

*Analytic defect [V].* The manuscript's phase sections are supported in interior charts. On a configuration of type (P-level)×(A-block), $\Phi\equiv0$ on the block, so all $\eta$ sections vanish identically and are not transverse. Cutting compatibly with breaking needs an $S^1$-equivariant ($u$-map) formalism on $\mathbb R\times Y_2$.

## 3. Q2: spinor asymptotics at the Floer ends

**Nondegeneracy needed.**
- (N1) Irreducible flats are nondegenerate (holonomy perturbations).
- (N2) $D_{\alpha\otimes t}$ is invertible for every irreducible $\alpha$.
- (N3) $D_{\theta_e\otimes t}$ is invertible for both central flats, i.e. for both spin$^c$ structures $t\otimes L_e$ of $Y_2$.
- (N4) The $\Phi\ne0$ critical points are nondegenerate (Morse–Bott along phase orbits for type P).

(N1)–(N3) are generic [P]. They make $n_D$ additive and make $j_R=-j_L$ hold.

**$\Phi\ne0$ critical points exist and cannot be removed [V modulo standard theorems].**
- $Y_2$ admits no psc metric. A psc 3-manifold is a connected sum of spherical space forms and copies of $S^1\times S^2$ (Perelman). With $H_1=\Z/2$ it would be prime and spherical, hence an L-space. But $S^3_2(K)$ is an L-space only if $2\ge2g(K)-1=3$, which is false.
- $HM^{\rm red}(Y_2)\cong HF^{\rm red}\ne0$ in some spin$^c$ structure. Both spin$^c$ structures occur as $t\otimes L_1$ with $L_1|_{Y_2}\in\Z/2$, and the end perturbation $\beta|_{Y_2}$ is exact.
- Therefore irreducible 3D SW solutions, i.e. S-type $\mathrm{PU}(2)$ critical points, exist for every metric and small perturbation.
- P-type points are not controlled at all.

**Exclusion by energy fails.**
- The equations are homogeneous under $\Phi\mapsto\epsilon\Phi$, so there is no small coupling.
- There is no psc metric, so there is no Weitzenböck vanishing.
- The values $\mathrm{CSD}(\beta)=\mathrm{CS}(B_\beta)$ are bounded fixed numbers, giving no gap.
- A DLME-type $\eta$-positivity controls CS energy, not $n_D$.

**Exclusion by index fails.** By §2.5 these breakings are codimension one whatever $\eta$ is.

**The differential itself.** On $\mathbb R\times Y_2$ one has $\Theta=0$ and $n_D(A)=\sigma_t(\beta)-\sigma_t(\alpha)$. So $\partial$ preserves $\sigma_t=\mathrm{CS}-\rho_t$ only if counted trajectories have spectral flow at most their energy, which is not automatic. The cylinder localization meets the same $\mathcal E$-terms. *The spin-filtered complex is therefore itself a new-input statement.*

**What a block theorem needs at the ends.**
- (N1)–(N4).
- An $S^1$-equivariant $\mathrm{PU}(2)$ Floer complex of $Y_2$, with:
  - generators: irreducible flats, $\theta_0,\theta_1$, and the $\Phi\ne0$ points;
  - a $u$-action from phase cuts;
  - a spin filtration preserved by its differential.

  Alternatively, a hypothesis that $\mathcal E\simeq0$, but §4 shows this is false in general.
- A normalization $\delta_e=0$ (or the survivors $T_{L/R}$ treated as θ-entries).

## 4. Q3: the consistency check with $HB$

**Topology [V, `pprime.py`].** In $HB:Y_2\to Y_2$ the right outer piece is $P'=C_{-2}$-half $\cup H$. This is the positive cell with the trace half $F'_l=G-2U$ removed.
- Its lattice is $F_l'^{\perp}=\{u=0\}=\langle G\rangle\oplus4\langle-1\rangle$, with $G^2=2$, determinant 2, $b^+=1$, $\sigma=-3$.
- It contains **neither $U$ nor $X_2$**, so there is no toric period square and no clamp.

**[V] Every φ-free block cuts a positive cell.**
- A φ-free block alternates $B,H$.
- Floer ends must lie at a rational homology sphere seam ($Y_{\pm2}$ or $Y_{\pm1}$). At $Y_0$, $b_1=1$ and the admissible bundle make CS circle-valued, so there is no filtration.
- By periodicity the two outer pieces of the block glue to a positive cell.

φ is the only way to return to $Y_2$ after a $B$ without an $H$.

**Survivors in $HB$ (one cut, $J_1$; components $H_L$ and $P'$).**
- **Fixed, the budget equality case.** Take $H_L$ rigid of type A, $P'$ of type S, and the right end through $\theta$.
  - The class is $v=(x;t)=(2;1,0,-1,0)$. It has $v^2=0$, so $\kappa=0$; $v\equiv c_0\pmod 2$; and $v\cdot F_r=2$, which pays the test.
  - The total is $4+(-4)+(3+1)=4$, so the budget gives equality and does **not** exclude the tuple.
  - The tuple is killed only by the S-band together with the tangential index: $\Lambda^2=v^2=0$ on $P'$, and $K^2=2\Lambda\cdot v$.
  - The band needs $v$ forward-pointing and $\Lambda$ backward-pointing, which forces $\Lambda\cdot v\le0$. Then $d_s(P)\le-1$ (the example gives $-2$), and $d_s(P')=d_s(P)-2\delta$.
  - So the tuple survives iff $\delta\le-1$ [P].
- **Mixed.**
  - R on $H_L$ survives iff $\delta\le-1$ ($D=-4-4\delta$).
  - R on $P'$ has $D=-3-6\kappa+2s+4\delta\le-4+4\delta$, so it survives iff $\delta\ge1$ [V arithmetic].
  - All other cases have $D\le-3$.
- **With $\delta=0$, $HB$ has no reducible survivors.** Since $HB$ monotonicity is false (rational injectivity from `stack:finite-lattice`, $I(Y_2;\mathbb Q)\ne0$, shift $-\tfrac12$), the failure must lie in $\mathcal E$ or in the non-filtration of $\partial$. Both are end-local.

**Adding $B$.** $BHB\phi$ completes $P'$ to $P$, which creates $U$ and $X_2=S_{j+1}$. The clamp then gives $8\kappa\ge4$. The same S tuple now scores $8\kappa+1+1-3-2s\ge-1$, and the total is $\ge7>4$, independent of $\delta$ [V]. So φ kills the *cut-cell* survivors, which exist only when $\delta\ne0$. It does **not** kill the $\delta$-survivors $T_{L/R}$, which φ-blocks share with $HB$.

**Conclusion of the check [V as logic].** Whatever $\delta$ is, the irreducible-ended budget treats $HB$ and φ-blocks alike:
- with $\delta=0$, neither has survivors;
- with $\delta\ne0$, both do.

Therefore the budget is not the mechanism that makes φ-blocks monotone. The brief's expectation is half right: φ removes the cut positive cell, but the decisive φ-dependence is in §5.

## 5. Where φ enters: θ-throughput [V arithmetic; P interpretation]

In the closed stack an R-run crosses a $Y_2$ seam with no cut and no level. The $j$-terms telescope, since $j_R+j_L=0$. Per block of $k$ intervals with one bridge, the run's score changes by:
$$T_{\rm fix}=\Delta\Sigma(q+4)\ge4(k-1)+k-3-2k=3k-7,\qquad T_{\rm mix}=\Delta\Sigma(4+i-p)\ge3(k-1)-1-2k=k-4 .$$
These agree with agent D's table.

| Block | $T_{\rm fix}$ | $T_{\rm mix}$ |
|---|---|---|
| $HB$ ($k=1$) | $-4$ | $-3$ |
| $k=3$ | $+2$ | $-1$ |
| $k=4$ | $+5$ | $0$ |

Long runs through blocks with $T<0$ make $D\ge0$ in composites: these are Kotschick–Morgan-type Abelian chains held at the walls of consecutive positive cells.

In Floer language these are the **θ-entries** ($\theta\to\theta$, $\alpha\to\theta$, $\theta\to\alpha'$) of the block map. Floer's irreducible complex does not see them. Ordinary composition is unaffected, because a central contact costs 3. In the coupled problem with large $\eta$, however, they are not excluded.

So the φ-sensitive statement is: **θ-throughput is nonnegative iff $k\ge4$** ($k\ge3$ for the fixed part only). This is the manuscript's spacing, now read per block. The spin shift is negative iff $k\le4$. The window is the single value $k=4$, i.e. density $1/4$, which is consistent with $m/n\in(1/5,1/4]$.

## 6. Q4: best statements

**Theorem B1 (localized exclusion) [V arithmetic, P analysis].** Assume the following for $W_{a,b}$ ($n_b\ge2$):
- the manuscript's data on the interior: clamp metrics on the macro, sphere tests, lens pairing, and Def. `indices:analytic-hypotheses` (i)–(iii) extended to candidates with end levels;
- (N1)–(N4);
- $\delta_0=\delta_1=0$.

Then, for every entry with $n_*\ge1$:
- the only $S^1$-fixed points of the compactified cut-down 1-dimensional space are unbroken instantons;
- the only face ends are trace-minimum lens ends, cancelling in bit pairs;
- over $\Z$,
$$2^{\,n_*-1}F^{(n_*)}=\partial K+K\partial+\mathcal E,$$
where $\mathcal E$ is the end term of §2.5(b). (The (P-level)×(A-block) part of $\mathcal E$ requires the equivariant phase-cut formalism.)

*Proof outline.* The proof is §2.1–2.5. The fixed part is Prop. F; the mixed part is Prop. M; the lens and Stokes steps are those of the manuscript.

**Corollary [V as logic].** "Block monotonicity" holds for the irreducible complex iff $\mathcal E\simeq0$ over $\Z[\tfrac12]$. It does **not** hold for $HB$ (when $\delta=0$). Coefficients must be $\Z[\tfrac12]$ or $\mathbb Q$: over $\F_2$ the identity is empty once $n_*\ge2$.

**Conjecture B2 (θ-inclusive block monotonicity) [S].** Let $\widetilde C^{\mathbb T}(Y_2)$ be an $S^1$-equivariant $\mathrm{PU}(2)$ Floer complex with $\theta_0,\theta_1$ and the $\Phi\ne0$ points as generators, filtered by $\sigma_t$. For a φ-block with exactly $k=4$ intervals per bridge, the block map is filtered with shift $(k-5)/8=-\tfrac18$ up to filtered homotopy. For $HB$ it is not, because its θ-entries have $T_{\rm mix}=-3$.

The contradiction would then follow if the φ-block induces a rational automorphism of the localized homology and the instanton summand has finite spin depth.

**Genuinely new inputs**, in order of difficulty:
1. The $S^1$-equivariant $\mathrm{PU}(2)$ monopole Floer theory of a rational homology sphere with central reducibles. It needs $u$-maps from phase cuts, a spin filtration, a localization theorem (fixed parts: instanton, SW, θ-towers), and a proof that its differential is filtered (cylinder monotonicity).
2. Budgets for block entries starting at $\Phi\ne0$ generators. They involve SW gradings of $Y_2$, are bounded but unknown, and must fit in the per-block slack (2 for fixed tuples, 1 for mixed).
3. Lifts of $B\simeq g_-g_+$ and of the units to this theory. Without them, the φ-block need not be an automorphism there.
4. Finite spin depth of the cap-detected instanton classes. θ-towers have infinite depth; $HB$ shows the danger.
5. The mixed-projection lemma and incidence (ii) at Floer ends. These carry over from the manuscript [P].

**Weaker statement that survives [V].** This is the closed-form "block additivity": the manuscript's closed exclusion is a sum of per-block scores, $T_{\rm fix}=3k-7$ and $T_{\rm mix}=k-4$, with seams costing nothing. That is the manuscript's own argument, not a Floer-filtered one.

## 7. Where the attempts may break
- **Sign conventions for $\delta$, and $h^0$ at S/P contacts.** If S contacts cost 1, §2.5(b) through S points becomes $D=-1$ and only P points remain. This does not change the verdict.
- **Sharpness of the $T_{L/R}$ survivors.** They are survivors of a necessary projection. Their actual existence is unproved.
- **"$HB\simeq\mathrm{id}$ with shift $-\tfrac12$" relies on the brief's formal values.** If the spin filtration on $C(Y_2)$ is not defined at all, the $HB$ check is vacuous. That outcome is itself fatal to a DLME-style Floer formulation.
- **A cleverer end condition could remove $\mathcal E$ for φ-blocks only.** Examples would be a Dirac perturbation on the ends, or Floer ends at $Y_{\pm1}$ (integral homology spheres with $\theta$ only). The block analysis shows no mechanism for this: the dimension of $\mathcal E$ is independent of the interior.
