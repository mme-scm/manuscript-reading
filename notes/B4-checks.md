# B4: Adversarial checks of the spin-filtered picture

Labels: **[V]** = I checked it by hand against the manuscript or DLME source, or by script (`agents/B4/checks.py`). **[P]** = plausible. **[S]** = speculative. **†** = a citation from memory.

## 0. Verdicts

| Claim | Verdict | Confidence |
|---|---|---|
| (a) Mod 2, on homology, $B\simeq g_-g_+\simeq H^{-1}$, hence $HB\simeq\mathrm{id}$ | **Correct** | high |
| (b) $n_D=\frac{5m-n}8+$const, with $-\frac18$ per interval and $+\frac58$ per bridge | **Correct** | high |
| (c) Spin table: $B$ $+\frac18$, $H$ $-\frac58$, period $\frac{k-5}8$ | **Correct for the manuscript's spin$^c$ choice.** The DLME $g_1$ row is wrong ($-\frac38$, not $-\frac18$). The period/$n_D$ agreement is a tautology. | high |
| (d) The fixed-type lemma holds at spacing 3; spacing 4 is needed only in `indices:mixed-run` | **Correct** (as a statement about the proofs) | high |
| Q2: the method uses $\phi$ only as a negative-definite mod-2 unit $Y_{-2}\to Y_2$ | **False as stated.** The stack uses $\phi$ only that way, but the caps use $\phi^{-1}$ through $T=f_-\phi^{-1}f_+$. | high |
| Q3: THEOREM? (one-sided $V$) | **(a)/(c): plausibly true and new.** It is the exact $\pm2$ analogue of a statement DLME's argument *does* prove at $\pm1$. No refutation was found. d-invariants restrict to $V_0(K)=V_0(\bar K)=0$. | moderate |
| Q4: minimal lens cap ($\kappa=\frac14$, framed ASD index 2, $\delta_{\rm sp}=2$) | **Correct** | high |

## 1. (a) $B\simeq H^{-1}$ mod 2  [V]

**Conventions** (Conv. `ordinary:index`): paths are chronological and operators compose right to left.
- $f_+:C(Y_0)\to C(Y_2)$ and $g_+:C(Y_2)\to C(Y_0)$.
- $f_-:C(Y_{-2})\to C(Y_0)$ and $g_-:C(Y_0)\to C(Y_{-2})$.

**The two identities.**
- The compressed pentagon gives $f_+g_+\simeq J_2$ (eq. `ordinary:two-step-identity`).
- *Mirror read backwards.* Mirroring sends $Y_r(\bar K)=-Y_{-r}(K)$. Reversal dualizes the counts. The mirror identity $\bar f_+\bar g_+\simeq J$ therefore dualizes to $\bar g_+^{*}\bar f_+^{*}=g_-f_-\simeq J_{-2}$ on $C(Y_{-2})$.
- So the mirror gives $g_-f_-\simeq\mathrm{id}$, **not** $f_-g_-\simeq\mathrm{id}$.
- This is harmless: the theorem proves each of $f_\pm,g_\pm$ is a unit (single-step pentagons, both triples). Hence $g_\pm=f_\pm^{-1}$ on $H(\,\cdot\,;\F_2)$.

**The four-step family** $2\to\infty\to0\to\infty\to-2$ (Lemma `negative:four-topology`).
- The $Z_2$ face is the product of $g_+$ (left half, evaluations $(0,1)$ on $(F_l,A)$) and $g_-$ (right half, evaluations $(1,0)$ on $(A,F_r)$).
- The lifts $e,e'$ sum independently, so the face is $g_-g_+$.
- The boundary relation identifies this face with the $M_{13}$ pentagon count, and then with $B$ (Lemmas `negative:faces`, `negative:pentagon`, `negative:sweeps`).

**Conclusion.** $B=g_-g_+=f_-^{-1}f_+^{-1}=(f_+f_-)^{-1}=H^{-1}$ on mod-2 homology, so $HB\simeq\mathrm{id}_{Y_2}$ and $BH\simeq\mathrm{id}_{Y_{-2}}$.
- Caveat: this holds up to the fixed end identifications, which the manuscript fixes once.
- One automorphism could in principle enter: the twist $\iota$ by the flat $\Z/2$ line on $Y_{\pm2}$.
  - [P] $\iota$ shifts $\CS$ by $\tfrac12$ mod 1 and the grading by 4 mod 8, so it preserves $\CS-\mathrm{gr}/8$.
  - [P] It exchanges the two spin$^c$ structures, since $\rho_t(\chi\alpha)=\rho_{t+\tau}(\alpha)$.
  - With fixed identifications it does not appear.

**Byproduct [V].** In the period $A^3D$ (with $A=\phi_*B$, $D=HB$), $D\simeq\mathrm{id}$ mod 2. The positive bridges are therefore homologically invisible: they enter only through the index $n_D$.

## 2. (b) $n_D$ bookkeeping  [V]

- From $D_I=8\kappa-3(1+b^+)=n+z$ (eq. `stack:ordinary-dimension`) we get $8\kappa=n+z+3+3m+3b_0$.
- With $\Theta=m+\Theta_0$, this gives $n_D=\frac{5m-n}{8}+\Theta_0-\frac{z+3+3b_0}{8}$.
- **Per interval:** one degree-2 test plus one parameter raises $8\kappa$ by 1, so $n_D$ changes by $-\frac18$.
- **Per bridge:** $\Theta$ rises by 1 and $8\kappa$ by 3, so $n_D$ changes by $+\frac58$.
- **Cell values I rechecked:**
  - Negative cell: $\Lambda_0^2=-2=\sigma$, so $\Theta=0$.
  - Positive cell: $\Lambda_0^2=c_0^2=0$ and $\sigma=-4$, so $\Theta_P=1$.
  - The trace halves contribute $-\frac14$ for $X_{-2}$ (with $\Lambda F_r=-2$) and $+\frac14$ for $-X_2$ (with $\Lambda F'_l=0$). They cancel, so $\Theta_B=\Theta_\phi=0$ and $\Theta_H=1$.
- Note: $\Theta_P=1$ is a *choice*. The lattice $H\oplus4\langle-1\rangle$ is indefinite, and a larger $\Lambda_P^2$ is possible (e.g. $K^2=4$ gives $\Theta=2$). The choice is pinned by the clamp ($|\Lambda H_I|\le\frac32$), not by topology.

## 3. (c) The level table

**Formulas [V].**
- Degree: $D=-2c^2-3b^++\dim G-\mathrm{codim}$. This follows from DLME's (index-form) with $i(W,c;\theta,\theta')=-2c^2-3(1+b^+)$.
- It agrees with Prop. 3.3 ($b^+=\dim G=\mathrm{codim}=0$) and with §5.5 ($D=\dim G-2c^2=3$ for $g_1$).
- The $b^+$ term is an extension outside DLME. It matches the manuscript's (eq. `ordinary:central-index`).
- CS level: $L=-c^2/4-\eta$. Spin level: $L_\sigma=-c^2/4-\Theta$, so the spin shift is $-\Theta+(3b^++\mathrm{codim}-\dim G)/8$.

**Errors and qualifications.**
1. **DLME $g_1$ row is wrong [V].**
   - $W^1_{-1}$ has lattice $\langle-1\rangle^2$ with $c=(0,1)$ (or $(1,0)$), and $l$ is characteristic.
   - So $\Lambda\equiv(1,0)$ mod 2, which forces $\Theta\in\frac14+\Z$, with maximum $\frac14$.
   - The spin shift is therefore $-\frac18-\Theta=-\frac38$ at best. `levels.py` used $\Theta=0$, which is impossible.
   - This is harmless, since $g_1$ is only a comparison row.
2. **$B$'s value is spin$^c$-dependent [V].** The two bits need equal $\Theta$, which holds iff $\Lambda\cdot S=+2$.
   - That is the manuscript's choice: mixed end labels, $l\cdot F_l\equiv0$ and $l\cdot F_r\equiv2$ mod 4.
   - With it, both bits give $+\frac18$.
   - For $l\cdot S\in\{0,\pm4\}$ the bits differ (e.g. $\Theta=\pm\frac12$), and the weighted $B$ has shift $\max=\frac58$ or worse.
   - So "$+\frac18$" is the best uniform value, and it is valid only for the labels the stack actually uses: $B$ goes from label 1 on $Y_2$ to label 0 on $Y_{-2}$, and $\phi$ or $H$ returns label 0 to label 1.
3. **$H$ [V].** $c_H^2=0$, $b^+=1$ and $\Theta_H=1$ give $D=-3$, CS shift $\frac38-\eta$ and spin shift $-\frac58$.
4. **The period identity is a tautology [V].**
   - For *any* closed stack, summing the spin shifts over the pieces gives $-\Theta+(3b^++n)/8=-n_D-(z+3)/8$.
   - So "$m/n>\frac15$ iff the period lowers the spin level" is a restatement of $n_D>0$, not independent evidence.
   - The spin-filtered language adds no content beyond the manuscript's $n_D$ count. All content lies in *monotonicity*, i.e. in the PU(2) exclusion.
5. **The $HB$ paradox stands [V].**
   - The labels compose consistently: $(Y_2,1)\to(Y_{-2},0)\to(Y_2,1)$.
   - Per-map monotonicity would give $\ell_t(Y_2)\le\ell_t(Y_2)-\frac12$ for every nontrivial $K$. So per-map monotonicity is false.
6. **New gap for a Floer-theoretic version [P].**
   - $\rho_t(\alpha)$ is gauge invariant (APS $\eta$ of $D_{\alpha\otimes t}$). Hence $\sigma_t=\CS-\rho_t$ is a legitimate IP-type filtration.
   - But a spin-filtered *complex* needs $n_D\le0$ also for **differential** trajectories on $\R\times Y_{\pm2}$, where $n_D=-\mathrm{SF}(D_{a(t)\otimes t})$ can be positive.
   - Localization there must face S-type fixed points that are 3-dimensional SW critical points of $Y_{\pm2}$. These exist whenever $HM_{\rm red}(Y_{\pm2})\neq0$, which is expected for $\Delta=1$ nontrivial knots.
   - The closed stack avoids this because its $Y$-seams are finite. This is the main obstacle to "define $I^t_\bullet$ and $\ell_t$".

## 4. (d) The window  [V]

**Fixed-type run (Lemma `indices:fixed-run`).** Recomputed by script:
- The bound $\max(2s+L-7m,\,m+L-2s)$ with $L-1\le s\le L+1$ is $\ge-2$ at spacing $\ge3$ ($L\ge3m-2$).
- $m=2$, $L=4$: minimum $-2$ (at $s=4$).
- $m=3$, $L=7$: $-2$.
- $m\ge3$: $3L-2-7m\ge2m-8\ge-2$.
- Spacing 2 fails: $(m,L,s)=(2,3,4)$ gives $-3$, and the minimum is unbounded as $m$ grows.

**Mixed run (Lemma `indices:mixed-run`).** The sharp bound $s-4m+r+\Delta+3\,\mathrm{miss}$ on a tight periodic run is:
- the constant $2$ at spacing 4;
- $4-m$ at spacing 3, which is unbounded below.

So the proof needs spacing 4. Whether the *conclusion* fails at 3 is open (cf. D §4.5).

**Geometry.** The geometry already forces spacing $\ge3$: macros (bridge plus two intervals) must be disjoint, with a single interval between them. A $\phi$-free stack ($BHBH\cdots$, spacing 1) is therefore not even constructible. That consistency test is vacuous.

## 5. Q2: every use of $\phi$  [V by grep of `src/*.tex`]

$\phi$ appears only in §2 (Cor. `ordinary:bridge`), §4 (caps) and §5 (stack); §1 and §10 only state it.

**(A) Stack (§5).** Here $\phi$ enters as follows.
- $\mathcal A=\phi_*B$: needs a mod-2 unit and an integral chain map.
- The negative-cell lattice $\langle-1\rangle^2$ (Prop. `stack:lattice`, which notes the $H_1$ action is automatically trivial).
- $\Lambda_0$ on negative cells: $\Theta_{\rm cell}=0$, mixed labels.
- The closed-composition budget: a central contact on a $b^+=0$ piece costs 3.

Replace $\phi$ by $V$ (negative definite, $b_1=0$). Let $Z_V=X_{-2}\cup V\cup -X_2$; it is closed and negative definite, hence **diagonal by Donaldson**†.
- $F_r,F'_l$ have the form $e_1\pm e_2$, or the disjoint pair $e_1+e_2,\ e_3+e_4$.
- Every use is an *upper* bound $v^2\le-((vF_r)^2+(vF'_l)^2)/2$. This holds in any negative-definite lattice by Cauchy–Schwarz; extra summands only help.
- Parity is unchanged.
- $\Theta_{\rm cell}=0$ is attained by an all-$\pm1$ characteristic class with $l\cdot F_r=-2$, $l\cdot F'_l=0$. Then $\Theta_V=0$ (see §6).
- The tuple-type numerology ($d_s=-1$ on such cells) is unchanged.
- **Extra hypothesis needed:** every reducible flat on $V$ must be central, e.g. $H_1(V)$ an elementary 2-group generated by the images of $H_1(Y_{\pm2})$. Otherwise $U(1)$-stabilizer flats weaken the "cost $\ge3$" in Prop. `stack:composition`. [P]
- Metric families are untouched ($\phi$-cells carry no geometry).

**(B) Caps (§4).** These use $\phi^{-1}$, through $T=f_-\phi^{-1}f_+$ inserted as $T^k$ into $X_0$ to create a $Y_2$ seam.
- $T$ must be a rigid, integral, $b^+=0$ rational quasi-isomorphism with simply connected handle halves (Lemma `caps:positive-power`, Cayley–Hamilton).
- Chronologically $C_+$ begins with $\phi^{-1}$, which cancels the stack's last return. So $X$ contains $\phi^{-1}$ only inside the cap copies of $T$, while $q$ is computed on $X'_k$, which contains $k$ copies of $\phi^{-1}$.
- **Nothing in $\{f_+,f_-,V,H\}$ reaches $Y_2$ and comes back.** These are all the forward rigid maps, and $Y_2$ is a sink among them. The only return is the family map $B$.
- $\phi$-free caps $C_-=W_-\cup f_+$ and $C'_+=f_-\cup W_+$ give $\Omega\equiv q_B:=\langle y_0,T_Bx_0\rangle$ mod $2^N$, with $T_B=f_-Bf_+\equiv\mathrm{id}$ mod 2 [V, from §1].
- Then $q_B\equiv q_0$ mod 2. But $q_0$ is probably even in the manuscript's integral normalization: the $k=0$ coefficient carries a factor $4^{a+m}$ [P]. Its parity is not intrinsic, and I could not decide it.
- Forcing nonvanishing via $T_B^{2^j}$ inserts a dense $(HB)^{2^j-1}$ cluster. The run lemmas cannot absorb it (an A-type cap component scores only 4) [V], unless the caps are allowed families [S].

**Answer to Q2.** If the method is correct, it proves the following, not the one-sided THEOREM?.

> **THEOREM?$_2$.** For nontrivial $K$, there is no pair $V:Y_{-2}\to Y_2$, $V':Y_2\to Y_{-2}$ such that:
> - both are negative definite with $b_1=0$, and all their reducible flats are central;
> - both induce $\F_2$-isomorphisms on irreducible $I$;
> - $V'$ is compatible with simply connected caps.

It also proves the one-sided THEOREM?$_1$ under an extra cap nonvanishing input (N): $\langle y_0,f_-B\,W\,f_+x_0\rangle\neq0$ for some spacing-$\ge4$ word $W$.

A Floer-theoretic spin-filtered version would need only $I(Y_2)\ne0$, and so would give THEOREM?$_1$ directly. The genus is not used outside the caps and the reduction [P], so these statements would hold for *all* nontrivial $K$.

## 6. Q3: probing THEOREM?

**Prop. 1 (d-shadow) [V, modulo OS Thm 9.6† and the Ni–Wu formula†].** If a negative-definite $V:Y_{-2}(K)\to Y_2(K)$ with $b_1=0$ exists, then $V_0(K)=V_0(\bar K)=0$. No unit hypothesis is needed.

*Proof.*
1. $Z_V$ is diagonal, so it carries characteristic classes with all coordinates $\pm1$. These have $c^2+b_2(Z)=0$.
2. Split along the QHS seams; squares add. Apply the OS inequality to $X_{-2}(K)$ (from $S^3$), to $V$, and to $-X_2(K)$ (to $S^3$). The three inequalities sum to $\le0$, so each is an equality.
3. As $c$ varies, $c\cdot F_r$ and $c\cdot F'_l$ take both residues mod 4, in either Donaldson case.
4. Label $i$ corresponds to $c\cdot F\equiv2-2i$ (mod 4), and $d(Y_2,i)=\pm\frac14-2V_i(K)$, $d(Y_{-2},i)=\mp\frac14+2V_i(\bar K)$.
5. Sharpness of the traces then gives $V_0(K)=V_1(K)=V_0(\bar K)=V_1(\bar K)=0$. ∎

Corollaries:
- For $\phi$ itself this recovers the known constraint, and forces the spin$^c$ label swap the manuscript's $\Lambda_0$ uses (0 to 1).
- Under that equality, $V$'s mixed-label spin$^c$ has $c_V^2+b=0$, i.e. $\Theta_V=0$. The (0,0) and (1,1) labels give $\Theta_V=\pm\frac12$; they occur only in the disjoint Donaldson case.
- **d-invariants cannot refute THEOREM? for candidate knots.** They make it trivially true when $V_0(K)+V_0(\bar K)>0$, e.g. for $\tau\ne0$.
- $\Delta_K=1$ is *not* forced, because DLME's proof uses Casson–Walker on double covers, which is not monotone under $V$. So THEOREM? concerns e.g. slice knots and $4_1$.

**Prop. 2 (DLME proves the $\pm1$ analogue) [V from DLME Lemma 2.x(b) and Prop. 3.3].**
- Let $V:S^3_{-1}(K)\to S^3_1(K)$ be negative definite with $b_1=0$ and $F_2$-injective.
- Then $L-D/8=-\eta(V,c)\le0$, so $\ell(Y_1)\le\ell(Y_{-1})$.
- DLME's $\ell(Y_{-1})<\ell(Y_1)-\frac18$ then gives a contradiction for nontrivial $K$.

So THEOREM?$_1$ at $\pm2$ is the literal $\pm2$ analogue of a theorem already implicit in DLME. This is strong support for verdict (a).

**DLME-CS constraints at $\pm2$ [V formally, P for IP-structures on $Y_{\pm2}$, which DLME assert in their intro].**
- $V$ gives $\ell(Y_2)\le\ell(Y_{-2})-\eta_V$. $B$ gives $\ell(Y_{-2})\le\ell(Y_2)+\frac18-\eta_B$.
- Hence $\eta_V+\eta_B\le\frac18$. Here $\eta_B>0$, since $W'$ is simply connected.
- **The CS route alone proves THEOREM?$_1$ if $\eta_B>\frac18$:** every $B$-counted instanton would need energy $>\frac18$ relative to $-c^2/4$.
- For pairs: $\eta_V=\eta_{V'}=0$ and $\ell(Y_2)=\ell(Y_{-2})$. So **THEOREM?$_2$ with either $V$ or $V'$ simply connected is already a DLME-type consequence.** The manuscript's new content is the case of non-simply-connected pairs carrying SO(3)-flats that are irreducible at both ends, like $\phi$'s mapping cylinder.

**Natural candidates all fail.**
- **Integral handle paths [V].**
  - The step $r\to r\pm1$ has square $\mp r(r\pm1)$.
  - Increasing paths from $-2$ to $2$ pass through $Y_0$, so $b^+\ge1$ (the $A,U$ hyperbolic pair). Decreasing paths are positive definite and pass through $S^3$.
  - No Farey edge crosses 0 or $\infty$, so general slope paths behave the same way [P].
- **Slice $K$ [V].** $V$ = homology cobordism through $\pm\mathrm{RP}^3=Y_{\pm2}(U)$, which is negative definite. Its map factors through $C_{\rm irr}(\mathrm{RP}^3)=0$ with central matching cost 3, so it is zero. Since $I(Y_2)\cong I^w(Y_0)\ne0$, it is not a unit.
- **Interior sums $P\#P$ [V].** These have zero map for the same reason.
- **Rational blowdowns [P].**
  - The blowdown $W'_B$ of $W'$ goes the wrong way, and C reports $H_*(W'_B)_*$ singular.
  - Blowdowns inside $W_H$ cannot remove its $b^+=1$.
- **Double branched covers** of tangle replacements reduce to slope paths [P].

**Verdict on THEOREM?$_1$: (a), plausibly true and new.**
- It is DLME-style, since it is DLME's theorem at $\pm1$.
- It is consistent with $d$ and with CS invariants.
- No counterexample is visible.
- It is undetermined in the strict sense.
- [P] Frøyshov-type invariants are "balanced" for candidates, as $d$ is, and cannot obstruct.

The V-test therefore does **not** kill the route. It does show that the method (closed form) needs $\phi^{-1}$ in the caps.

## 7. Q4: minimal lens cap  [V by script]

- $\chi(\mathbb F_4,\mathcal O(aT))=a+1$ and $\chi(\mathbb P(1,1,4),\mathcal O(a))=H(a)+H(-a-6)$.
- **Normal ASD index** at $d=2$: $[-3-(-1)]-[-3-0]=1$ complex, so the framed real index is $2$. The table for $d=0,2,4$ is $0,2,8$.
- **Charge:** $E=-d^2/4=\frac14$, since $x\cdot S=1$ and $x^2=-\frac14$.
- **Dirac table** for $k(S)=-6,\dots,6$: $-1,0,0,0,0,0,-1$. This matches (eq. `indices:dirac-table`).
- **At $\Lambda S=2$, $d=2$:** the evaluations $4,0$ have index sum $0$, so $\delta_D=\frac14-\kappa_N=0$ and $\delta_{\rm sp}=2+0=2$.
- **Lens penalty:** $\delta_{\rm sp}-1=1$, so the projected dimension is $1-1=0$.
- **Kawasaki check:** $\chi(\mathbb P(1,1,4),\mathcal O(a))=a^2/8+3a/4+1+(\text{orbifold term})$, with the term vanishing at $a=\pm2$.

## 8. Weak points of this report

- Prop. 1 relies on the OS inequality and the Ni–Wu formula as recalled†. The label/mod-4 dictionary was checked against the unknot ($X_{\pm2}(U)$ sharp).
- The "only central reducibles on $V$" hypothesis is an educated reading of Prop. `stack:composition`, not a full re-proof.
- That genus 2 is unused outside §4 is [P]: by grep, the only genus mention in §§5–10 is the final reduction.
- The claim in §3.6 that $HM_{\rm red}(Y_{\pm2})\ne0$ obstructs per-map monotonicity is [P]. The link to the mixed P/R projection on cylinders was not worked out.
