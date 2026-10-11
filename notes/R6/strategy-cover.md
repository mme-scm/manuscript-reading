# The ±2 surgeries seen from the branched double cover: a strategy, what it proves, and where it stops

Labels: **PROVED** (complete argument from stated inputs), **COMPUTED** (exact or high-precision computation, scripts in `r6/cover-code/`), **PLAUSIBLE** (argument with a named gap), **SPECULATIVE** (heuristic). "Assumed" marks the exact triangle, which RULES (c) allows us to assume.

Sources: DLME LaTeX (`scratchpad/dlme/src`, cited by their LaTeX labels), `notes/G-sources/cover-1.md` (cited as cover-1), `notes/G-sources/triangle-1.md` (cited as triangle-1), `rho.tex`.

---

## 0. Summary

**Verdict.** This angle does not give a proof under RULES.md.

**What it proves.** Assume the downstairs exact triangle, whose outer terms are sums over both bundles and whose middle term is the traceless theory. Then the following hold.

1. **A counting form of DLME's argument (PROVED, for filtered complexes with arbitrary differentials; §4).** The drop is controlled by one spectral quantity:
   $$\Lambda(Y_{-2})\ \le\ T_1-\tfrac18,\qquad T_1=\inf\{t:\ N_{Y_2}(t)>\bar P_{\rm tl}(t)\},$$
   where $\Lambda=\min(\lambda_0,\lambda_1)$.
   - $N_{Y_2}(t)$ counts the infinite bars of $I(Y_2)$, both bundles, born at level $\le t$.
   - $\bar P_{\rm tl}(t)$ is the largest number of bars, finite or infinite, of two copies of the traceless theory that are alive at a single level $\le t$.
   - The argument uses only energy $\ge0$.

   Hence the drop is at least $\tfrac18-(T_1-\Lambda(Y_2))$, and it is positive as soon as $T_1<\Lambda(Y_2)+\tfrac18$.
2. **Consequence for a cosmetic pair (PROVED for perfect complexes; a weaker statement in general).** If $Y_2\cong Y_{-2}=:Y$, then $s_{j+r}(Y)-s_j(Y)\ge\tfrac18+\eta$ for every $j$.
   - Here $s_j$ are the spectral values of $I(Y)$ over both bundles, and $r$ is the rank of the χ-reduced traceless homology.
   - In every computed det-1 case, some $r+1$ consecutive spectral values of $Y_{\pm2}$ lie within $0.013$ of each other, about a tenth of the $\tfrac18$ the condition requires. So no computed $Y_{\pm2}$ could be one side of a cosmetic pair.
3. **The −1/16 map is null-homotopic (PLAUSIBLE, by the same analysis as the triangle).**
   - Among the maps built from this configuration, the only one from $Y_2$ to $Y_{-2}$ with topological level $-\tfrac1{16}$ is the exterior of $\nu S$ with the odd flat connection $\gamma_1$ on $L(4,1)$.
   - It is the $L(4,1)$-face of the nonsingular odd family, whose $S^3$-face is empty. So it is a boundary.
4. **A filtered model with zero drop (PROVED, `nogo.py`).** There is an explicit filtered exact triangle with zero drop, and with $Y_2\cong Y_{-2}$ preserving bundles, levels and degrees. It satisfies:
   - every level of the triangle, with strictly positive energies;
   - the degrees mod 4;
   - Euler characteristic $0$;
   - a free χ-action;
   - a lift to the cover satisfying DLME's levels.

   Hence no argument that uses only these formal structures, together with positivity of energy, can prove a drop. The missing input has to be information about the actual spectra.

**What the cover adds, and what it does not.**
- The two lifts of the involution explain why the outer terms are sums over bundles. The two isotropy types along $\tilde S$ explain why the two failed families are halves of one homotopy (§1–2).
- The χ-action is free when $\det K=1$; on the traceless side, exactly then. This rules out exactly the zero-energy absorption at binary dihedral points that produces $m_2=\tfrac1{16}$ for $4_1$ and $\bar T(2,3)$.
- It puts no further constraint on the filtered structure (§6–7).
- The upstairs (DLME) filtration differs from the downstairs one by $\delta/8$, where $\delta$ is the anti-invariant index. So invariant parts of the upstairs *filtered* triangle are not the downstairs filtered triangle (§1.4).

**How 1/16 enters.**
- It is the $L(4,1)$ term $\rho(\gamma_1)/16$. It is also half of DLME's cap energy $1/8$.
- It appears only in the upper levels: the third map ($3/16=1/8+1/16$), the vertex homotopies ($1/16$), and the null-homotopic exterior map ($-1/16$).
- No lower bound for the drop involves $1/16$. Every lower bound comes from the family term $-1/8$ ($i_0=-1$) and the counting.
- A drop $\ge\tfrac1{16}$ would follow from $T_1\le\Lambda(Y_2)+\tfrac1{16}$. The computed cases have $T_1-\Lambda(Y_2)\le\tfrac1{32}$ in all 80 torus-knot cases.

**Data (COMPUTED).**

| test | cases | result |
|---|---|---|
| spectral transfer and counting inequalities | 54 det-1 torus knots ($pq\le120$), 80 torus knots ($pq\le60$), $4_1$ | 0 violations |
| bottom-class conditions that a zero drop would require | all 27 det-1 mirrors | all hold, yet the drop is $\approx\tfrac18$ |
| counting bound on the drop | same 54 det-1 cases | explains the drop with margin: bound $\ge0.0956$, actual $\ge0.1239$ |
| level of $X'=W'\setminus\nu S$ at common points | 1036 same-bundle, 696 mixed | $c(Y_2)-c(Y_{-2})$ is exactly $1/8$ at same-bundle points and exactly $3/16$ at mixed points |

The last row confirms the $\gamma_0$ and $\gamma_1$ terms.

**The missing input, stated precisely (§8; SPECULATIVE; not an energy estimate).** For $\det K=1$, there is a level $t<\Lambda(Y_2)+\tfrac18$ at which $Y_2$ (both bundles) has more classes born by $t$ than two copies of the traceless theory have bars alive at any level $\le t$.

---

## 1. The cover, the two lifts, and χ

Throughout, $K\subset S^3$ has $\det K=1$. This holds for any cosmetic candidate, since then $\Delta_K=1$; that also gives $\sigma(K)=0$, because the Levine–Tristram signature jumps only at roots of $\Delta_K$.

Notation:
- $\Sigma=\Sigma_2(K)$, with deck involution $\tau$ and fixed knot $\tilde K$;
- $W'=(-X_2^\circ)\cup_{S^3}X_{-2}^\circ$, and $S$ the $(-4)$-sphere in it;
- $\Lambda(Y):=\min(\lambda_0,\lambda_1)(Y)$, which is $\ell$ of the sum complex $C(Y,P_0)\oplus C(Y,P_1)$ in the uniform normalisation $c=(3+\rho)/16$.

### 1.1 Topology (PROVED; cover-1 §2, where each item is checked)
- The connected double cover of $Y_{\pm2}$ is $\tilde Y_\pm=\Sigma_{\pm1}(\tilde K)$. It is an integer homology sphere, and its deck involution is free.
- The double cover of $W'$ branched along $S$ is DLME's composite $W^1_{-1}$ for $(\Sigma,\tilde K)$. In it:
  - $\tilde S$ is the $(-2)$-sphere;
  - $\partial\nu\tilde S=\mathbb{RP}^3$ double covers $\partial\nu S=L(4,1)$.
- DLME's two bundle classes are $\hat c=p^*F_l^*$ and $\check c=p^*F_r^*$. Both are odd on $\tilde S$.
- DLME's whole family configuration ($G^i_j$, $i-j\le3$) can be chosen $\tau$-invariant. Its quotient is the configuration on $W'$ with cone angle $\pi$ along $S$.

### 1.2 The two lifts of the involution and the two isotropy types (PROVED for flat connections, cover-1 Prop. 3.1 and §3.2; PLAUSIBLE for moduli spaces)
- **On $\tilde Y_\pm$.** An invariant irreducible flat $SO(3)$ connection has a unique lift $\tilde\tau$ to the adjoint bundle. Its $SU(2)$ lift squares to $\pm1$:
  - $+1$ gives $P_0$ on $Y_{\pm2}$, an $SU(2)$ connection defined up to χ;
  - $-1$ gives $P_1$.

  So the invariant part of the outer upstairs terms is the sum over both bundles, counted modulo χ.
- **On $\Sigma$.** The isotropy along $\tilde K$ is either trivial or a rotation by $\pi$.
  - Trivial isotropy descends to $S^3$, where only $\theta$ is flat.
  - Rotation by $\pi$ descends to the irreducible traceless representations $R^*(K;\mathbf i)$, taken modulo χ.

  So the invariant part of DLME's middle term $C(\Sigma)^{\oplus2}$ is $C(S^3)\oplus$ (two copies of the χ-reduced traceless complex). It has the same generators as the full traceless complex $C^{\rm tl}(K)$ generated by $R^*(K;\mathbf i)$.
- **On $\tilde W$.** The isotropy along $\tilde S$ is either trivial or a rotation by $\pi$.
  - Trivial isotropy gives nonsingular $SO(3)$ bundles on $W'$ that are odd on $S$.
  - Rotation by $\pi$ gives connections singular along $S$ with holonomy parameter $1/4$.

  These are the two families the user tried separately (§2.4).

### 1.3 The twist χ
- **Definition.** χ is the character $\pi_1(Y_{\pm2})\to H_1=\mathbb Z/2\to\{\pm1\}$. It acts on $SU(2)$ representations by $\rho\mapsto\chi\rho$.
  - It shifts $CS$ by $1/2$ and the grading by $4$. It fixes $\operatorname{ad}\rho$, so $c(\chi\rho)=c(\rho)$.
  - It exchanges the central reducibles $\theta$ and $\theta_\chi$.
- **Freeness on $Y_{\pm2}$ (PROVED).** χ acts freely on the irreducibles of $Y_{\pm2}$ because $\tilde Y_\pm$ is a homology sphere:
  - If $\chi\rho\cong\rho$ via $u$, then $\rho|_{\pi_1\tilde Y}$ commutes with $u$.
  - So $p^*\rho$ is abelian, hence trivial.
  - So $\rho$ factors through $\mathbb Z/2$ and is reducible.
- **Freeness on the traceless representations (PROVED).** On $R^*(K;\mathbf i)$, χ ($\mu\mapsto-\mu$) is free exactly when there are no binary dihedral representations, that is, when $(\det K-1)/2=0$ (Klassen).
- **On the cobordism (PROVED).** On $W'\setminus S$, χ is the character of the branched cover, with holonomy $-1$ around $S$. Twisting by it maps holonomy parameter $\alpha$ to $\tfrac12-\alpha$. So it preserves the traceless condition $\alpha=\tfrac14$, and it relates the nonsingular counts with $c_1$ and $c_1+\mathrm{PD}(S)$; these are equal as $SO(3)$ counts.
- **Equivariance of the triangle (PLAUSIBLE).** In their $SU(2)/U(2)$ form, all maps of the triangle are χ-equivariant, and the $SO(3)$ outer terms are the χ-quotients.
- **Check (COMPUTED, `spectral.py`).** For all 27 det-1 torus knots with $pq\le120$, and their mirrors, every $c$-value of the $SU(2)$ spectra of $Y_{\pm2}$ (both bundles) and of the traceless theory has even multiplicity.

### 1.4 How filtrations descend: the obstruction to "taking invariant parts" (PROVED, from cover-1 Prop. 3.2)
- For a downstairs generator $\alpha$:
  $$\tilde c(p^*\alpha)=2c(\alpha)+\delta(\alpha)/8,\qquad \delta=i-i_\chi\in\mathbb Z.$$
  cover-1 found $\delta$ ranging from $-2$ to below $-300$ for torus knots.
- An invariant instanton with downstairs index $i^+$ and anti-invariant index $i^-$ is counted:
  - upstairs when $i^++i^-$ equals the upstairs $i_0$;
  - downstairs when $i^+$ equals the downstairs $i_0$.

  These are different conditions. So the τ-invariant part of DLME's *filtered* triangle is not the downstairs filtered triangle.
- Taking invariant parts at the chain level computes $\tilde\ell=\ell(\tilde Y)/2$ (cover-1). That is an invariant of $Y_{\pm2}$, but not one of the RULES targets, and its minimisers differ from those of $\lambda_i$.
- Localisation does not repair this (SPECULATIVE remark). In a Tate model, $\theta$-powers shift $\tilde c$ by multiples of $1/8$; normalising them recovers $2c$ only for index-0 maps. For the family map ($i^+=-1$) it gives $-1/16$ in halved units, not $-1/8$.
- The downstairs triangle must therefore be the orbifold (τ-invariant, downstairs-index) triangle itself. That is what we assume in §2.

---

## 2. The triangles used, with all levels

### 2.1 Upstairs: DLME's distance-two triangle for $(\Sigma,\tilde K)$ (PROVED by DLME for any integer homology sphere base)
- The triangle is `prop:CDX-triangle`, from the triangle-detection lemma `T-detec`:
  $$C(\tilde Y_+)\xrightarrow{f_1=W_*\oplus(W,c)_*}C(\Sigma)\oplus C(\Sigma)\xrightarrow{f_0}C(\tilde Y_-)\xrightarrow{f_{-1}=(X,\hat c)_*}C(\tilde Y_+).$$
- The homotopies are:
  - $g_1=(W^1_{-1},\hat c)_*-(W^1_{-1},\check c)_*$ over the interval of metrics;
  - $g_0$, $g_{-1}$, and the pentagon maps $h_i$, with $q_i\simeq\mathrm{id}$.
- DLME's ±1 theorem is the case where the base is $S^3$, so the middle term vanishes. There $g_1$ is a chain map and a quasi-isomorphism of level $-\tfrac18-\eta$ (`prop:pm-one-map`).

### 2.2 Downstairs: the sum triangle T (Assumed; construction PLAUSIBLE in triangle-1 §4.2)
- **Triangle (I):**
  $$C(Y_2,P_0)\xrightarrow{a}C(S^3)\oplus C^{\rm tl}_{\chi}(K)\xrightarrow{b}C(Y_{-2},P_1)\xrightarrow{c}C(Y_2,P_0).$$
- **Triangle (II):** the same with $P_0$ and $P_1$ exchanged on both ends.
- $C^{\rm tl}_\chi(K)$ is the χ-reduced traceless complex, with rank $r=|R^*(K;\mathbf i)|/2$ when $\det K=1$.
- $C(S^3)=0$ as an irreducible complex; its reducible $\theta$ is excluded by DLME's index counts (`lemma:g-bdry1`, case $i\not\equiv1$).
- **T = (I) ⊕ (II).** It has:
  - $A:=C(Y_2,P_0)\oplus C(Y_2,P_1)$;
  - $M:=$ two copies of $C^{\rm tl}_\chi(K)$, which has the generators of $C^{\rm tl}(K)$, of rank $m=2r$;
  - $B:=C(Y_{-2},P_0)\oplus C(Y_{-2},P_1)$.
- The bundles: $a$ and $b$ are the singular 2-handle maps, of odd degree. The third map $c$ and the homotopy $g_A$ exchange $P_0$ and $P_1$, because they carry a class that is odd on $S$.
- **Rank check (COMPUTED in triangle-1 §4.6, reproduced here).** In $SO(3)$ counts for $T(3,5)$: $A$ has $8+6=14$, $B$ has $8+10=18$, and $m=4$. Parity forces $a=0$, so $18=14+4$.
- **Triangle detection.** The relations are
  $$b a=dg_A+g_Ad,\qquad c b\simeq0\ (g_M),\qquad a c\simeq0\ (g_B),$$
  $$c\,g_A+g_M\,a\simeq\mathrm{id}_A,\qquad a\,g_M+g_B\,b\simeq\mathrm{id}_M,\qquad b\,g_B+g_A\,c\simeq\mathrm{id}_B .$$

### 2.3 Levels (PROVED as bookkeeping from the level formula of the brief, with KM's term $s(F)=\chi(F)+F\cdot F/2$, which is $0$ for $D_l$, $D_r$, $S$)

All levels are $c$-shifts ("$L-D/8$" in DLME's language), minus energy.

| map | cobordism, family | $b^+$ | $i_0$ | middle end, limit, term | level downstairs | upstairs analogue (DLME) |
|---|---|---|---|---|---|---|
| $a$ | $(-X_2^\circ,D_l)$ | 0 | 0 | — | $-\eta_a\le0$ | $f_1$: $\le0$ |
| $b$ | $(X_{-2}^\circ,D_r)$ | 0 | 0 | — | $-\eta_b\le0$ | $f_0$: $\le0$ |
| $c$ | $-(W'\setminus\nu S)$, class odd on $S$ | 1 | 0 | $L(4,1)$, $\gamma_1$: $(3-1+1)/16$ | $\tfrac38-\tfrac3{16}=\tfrac3{16}$ | $f_{-1}$: $\tfrac38-\tfrac18=\tfrac14$ ($\mathbb{RP}^3$, $\rho=0$) |
| $g_A$ | $W'$, interval; nonsingular odd family plus singular family | 0 | $-1$ | — | $-\tfrac18-\eta_g$, $\eta_g>0$ | $g_1$: $-\tfrac18-\eta$ |
| $g_M$, $g_B$ | composites through $-(W'\setminus\nu S)$, interval | 1 | $-1$ | $\gamma_1$: $3/16$ | $\tfrac14-\tfrac3{16}=\tfrac1{16}$ | $g_0,g_{-1}$: $\tfrac14-\tfrac18=\tfrac18$ |
| $h$ | pentagon | 1 | $-2$ | $\gamma_1$: $3/16$ | $-\tfrac1{16}$ | $0$ |
| $F$ (§2.4) | $X':=W'\setminus\nu S$, class odd on $S$ | 0 | 0 | $L(4,1)$ with the other orientation, $\gamma_1$: $(3-1-1)/16$ | $-\tfrac1{16}$ | $\mathbb{RP}^3$-face: $-\tfrac18$ |

- **$\eta_g>0$ (PROVED).**
  - The nonsingular part lives on the simply connected $W'$, where every flat connection is trivial and so has reducible limits.
  - A flat connection in the singular part would be a traceless representation sending $\lambda$ to $-1$ (for $P_0$ on $Y_2$) and to $+1$ (for $P_1$ on $Y_{-2}$) at once.
- **$\eta_a,\eta_b$.** They are positive exactly when no irreducible traceless representation sends $\lambda$ to $\pm1$ (no common points). When $\det K=1$ there are no binary dihedral representations, so there are no χ-fixed common points; but common points that are not binary dihedral are not excluded. The argument below never needs $\eta_a,\eta_b>0$.
- **Where 1/16 comes from (PROVED as bookkeeping).** It is the difference between the downstairs and upstairs middle-end terms, $\tfrac3{16}-\tfrac18$. Equivalently, it is the halving of the minimal odd cap energy, $\tfrac18\mapsto\tfrac1{16}$, since $E_{\rm cap}=1/(4|S\cdot S|)$ and Chern–Simons values double under the cover. The family term $i_0/8=-1/8$ does not halve.
- **Check at common points (COMPUTED, `lensterm.py`).** A representation that is a generator of both $Y_2$ and $Y_{-2}$ is a flat connection on $X'$. The level formula with $E=0$ gives
  $$c(Y_2)-c(Y_{-2})=\frac{3-h+\rho_{\partial X'}(\gamma)}{16}-\frac{\operatorname{ind}}8,$$
  which is $\equiv0\pmod{\tfrac18}$ for $\gamma_0$ and $\equiv\tfrac1{16}\pmod{\tfrac18}$ for $\gamma_1$. Over the torus knots $T(p,q)$ with $p\le11$, $q<40$, $pq\le120$:
  - at all 1036 same-bundle common points ($\alpha=\tfrac14$) the difference is exactly $\tfrac18$;
  - at all 696 mixed common points ($\alpha\in\{\tfrac18,\tfrac38\}$) it is exactly $\tfrac3{16}$.

  So at mixed points the flat connection has index $-1$ on $X'$ and index $0$ on $-X'$. It contributes to $c$, which attains its level $3/16$, and never to $F$.

### 2.4 The two halves of $g_A$, and the −1/16 map (PLAUSIBLE: same gluing and reducible analysis as T, cover-1 §3.5–3.6, triangle-1 §4.2)
- Write $g_A=g^{\rm ns}+g^{\rm sing}$:
  - $g^{\rm ns}$: trivial isotropy along $\tilde S$, nonsingular, bundle odd on $S$;
  - $g^{\rm sing}$: order-two isotropy, singular along $S$.
- Their faces:
  - **$S^3$-face of $g^{\rm ns}$:** empty. Only $\theta$ is flat on $J\cong S^3$, and broken configurations through $\theta$ have index $\ge2$, as in DLME `lemma:g-bdry1`.
  - **$S^3$-face of $g^{\rm sing}$:** $b\circ a$, through the traceless theory.
  - **$L(4,1)$-faces of both:** the exterior map $F$ on $X'$ with limit $\gamma_1$, glued to the nonsingular cap and to the singular cap respectively. Both caps have energy $1/16$ and index $-1$, so the two faces are the same chain-level count $F$.
- Hence
  $$dg^{\rm ns}+g^{\rm ns}d=F,\qquad dg^{\rm sing}+g^{\rm sing}d=ba+F .$$
- So $F$ is a chain map of level $-\tfrac1{16}$, and it is **null-homotopic** through $g^{\rm ns}$, which has level $-\tfrac18$.
- Consequence: the only map of this configuration from $Y_2$ to $Y_{-2}$ with topological level exactly $-\tfrac1{16}$ is zero on homology. A mixed inequality $m\ge\tfrac1{16}$ cannot be obtained from it.
- Upstairs, the corresponding $\mathbb{RP}^3$-face is homotopic to $f_0^{\hat c}f_1^{\hat c}$, which factors through $C(\Sigma)$. Downstairs, the trivial-isotropy part of that factorisation runs through $C(S^3)=0$. That is why $F\simeq0$ downstairs, a localisation of DLME's cancellation.

---

## 3. The theorem aimed at

**Target theorem.** Let $\det K=1$. Then $\Lambda(S^3_{-2}(K))<\Lambda(S^3_2(K))$. Quantitatively, the drop is at least $\tfrac18-(T_1-\Lambda(Y_2))$, and it is at least $\tfrac1{16}$ when $T_1\le\Lambda(Y_2)+\tfrac1{16}$; here $T_1$ is defined in §4.

Hence $S^3_2(K)\not\cong S^3_{-2}(K)$, orientation-preservingly.

The mixed version is the same statement applied to (I) and (II) separately, with $m_1,m_2$ in place of the both-bundle drop.

**Status.** It follows from T together with one input, Input X of §8, which is SPECULATIVE. Everything else in the chain is PROVED (§4) or COMPUTED (§7).

---

## 4. Filtered algebra (PROVED; general filtered complexes, nonzero differentials allowed)

### Conventions
- Complexes are IP-modules in DLME's sense (`def:I-module`): filtered by $\widetilde{CS}$ in each degree, periodic. For the $SO(3)$ and traceless theories the period is $(\tfrac12,4)$.
- A map of degree $D$ and level $L$ has **$c$-level** $\lambda=L-D/8$.
- For a complex $X$ and $t\in\mathbb R$, sum over one period of degrees $d$:
  - $N_X(t)=\sum_d\dim\operatorname{im}\big(H(F_{t+d/8}X_d)\to H(X_d)\big)$, the infinite bars born at $c$-level $\le t$;
  - $P_X(t)=\sum_d\dim H(F_{t+d/8}X_d)$, all bars alive at $c$-level $t$;
  - $\bar P_X(t)=\sup_{s\le t}P_X(s)$.
- The spectral values $s_1\le s_2\le\cdots$ of $X$ are the jumps of $N_X$, so $s_1=\ell(X)$.
- For perfect complexes (zero differential), $N_X=P_X=\bar P_X$ counts generators of $c$-value $\le t$.

### Lemma 4.1 (elementary)
1. If $V\subset H$ has codimension $k$ (with the induced filtration), then $s_j(V)\ge s_j(H)$ and $s_j(V)\le s_{j+k}(H)$.
2. If $Q=H/U$ has the quotient filtration, then $s_j(H)\le s_j(Q)\le s_{j+\dim U}(H)$.
3. A filtered linear isomorphism of $c$-level $\lambda$ gives $s_j(\text{target})\le s_j(\text{source})+\lambda$.

*Proof.* Compare $\dim F_tV$, $\dim F_tQ$ and $\dim F_tH$. ∎

### Lemma 4.2 (vertex lemma at the bottom of $A$, general)
Let $\hat x$ be a cycle of $A$ in degree $d$, at $c$-level $\Lambda_A=\Lambda(Y_2)$, representing a nonzero class.
- If $a\hat x=dy$, then
  $$\Lambda(Y_{-2})\le\max\big(\Lambda_A-\tfrac18-\eta_g,\ c(y)-\eta_b\big),$$
  where $c(y)$ is the $c$-level of $y$ in its own degree $d+D_a+1$.
- If $a\hat x=0$, the second term is absent.

*Proof.*
- $w:=g_A\hat x+by$ is a cycle, since $dw=ba\hat x+b\,dy=0$ over $\mathbb F_2$.
- Its class is nonzero: $(0,w)$ is homologous in $\mathrm{Cone}(b)$ to $(a\hat x,g_A\hat x)$, which is the image of $[\hat x]\ne0$ under the quasi-isomorphism $(a,g_A)$.
- The degrees work out: $\deg w=d+D_a+D_b+1$. In $c$-terms, $by$ has level $c(y)-\eta_b$ and $g_A\hat x$ has level $\Lambda_A-\tfrac18-\eta_g$. ∎

So the bottom class is **absorbed** exactly when every primitive $y$ of every representative has $c(y)\ge\Lambda_A+\eta_b$. This includes $y$ not existing at all ($a_*[\hat x]\ne0$). Absorption into a *finite* bar of $M$ obstructs just as an infinite bar does; this is where nonzero differentials enter.

### Lemma 4.3 (counting inequality, general)
Put $\mu_0=\min(\eta_g,\eta_a)\ge0$. For every $t$,
$$N_B\big(t-\tfrac18-\mu_0\big)\ \ge\ N_A(t)-P_M(t-\mu_0)\ \ge\ N_A(t)-\bar P_M(t).$$

*Proof.*
1. **The filtered cone.** Filter $\mathrm{Cone}(b)_e=M_{e-D_b-1}\oplus B_e$ by $F_r=F_{r-D_b/8}M\oplus F_rB$. This is a filtered complex, because $b$ has level $D_b/8-\eta_b$. In $c$-terms its $M$-part is shifted by $+\tfrac18$, which is the degree shift of the cone.
2. **The map $\Phi=(a,g_A)\colon A\to\mathrm{Cone}(b)$.** It is filtered of $c$-level $\max(-\tfrac18-\eta_g,\ -\eta_a-\tfrac18)=-\tfrac18-\mu_0$. It is a quasi-isomorphism by `T-detec`.
3. **The long exact sequence.** The filtered short exact sequence $0\to F_sB\to F_s\mathrm{Cone}\to F_{s'}M\to0$ gives an exact sequence $H(F_sB)\to H(F_s\mathrm{Cone})\to H(F_{s'}M)$, with $s'$ at $c$-level $t-\mu_0$.
4. **Counting.** Let $U$ be the kernel of $H(F_tA)\to H(F_{s'}M)$; then $\dim U\ge\dim H(F_tA)-P_M(t-\mu_0)$. Classes of $U$ lift to $H(F_sB)$. Of them, at least $N_A(t)-P_M(t-\mu_0)$ survive to $H(A)\cong H(\mathrm{Cone})$. That image factors through $H(B)\to H(\mathrm{Cone})$, so it bounds $N_B(t-\tfrac18-\mu_0)$ from below. ∎

### Lemma 4.4 (perfect complexes)
Let $k=\operatorname{rk}a_*=(\operatorname{rk}A+\operatorname{rk}M-\operatorname{rk}B)/2$, which is forced by exactness. If $A$, $M$, $B$ have zero differential, then for every $j$:
$$s_j(B)\ \le\ T_j-\tfrac18-\eta_g,\qquad T_j:=\inf\{t:\ N_A(t)-\min(N_M(t),k)\ge j\},$$
and in particular $s_j(B)\le s_{j+k}(A)-\tfrac18-\eta_g$. Also $s_j(A)\le s_{j+m-k}(B)+\tfrac3{16}$.

*Proof.*
- **First inequality.** $a$ maps $F_tA$ into $F_tM\cap\operatorname{im}a$, which has dimension $\le\min(N_M(t),k)$. Hence $\dim(\ker a\cap F_tA)\ge N_A(t)-\min(N_M(t),k)$.
  - On $\ker a$, the map $g_A$ (of $c$-level $-\tfrac18-\eta_g$) followed by $B\to B/\operatorname{im}b$ is injective. This uses the exact sequence $0\to\operatorname{coker}b_*\to H(\mathrm{Cone}\,b)\to\ker b_*\to0$ and $\Phi_*$.
  - Then apply Lemma 4.1.
- **Second inequality.** $c$ induces $B/\operatorname{im}b\cong\ker a$ at level $3/16$. Use Lemma 4.1(1) with codimension $m-k$. ∎

### Corollary 4.5 (kernel criterion; drop off absorption)
1. If the bottom class of $A$ is not absorbed in the sense of Lemma 4.2, the drop is at least $\min(\tfrac18+\eta_g,\ \Lambda_A+\eta_b-c(y))>0$.
2. If $a=0$, the drop is at least $\tfrac18+\eta_g$. This is the case for positive torus knots, by parity (triangle-1 §3.4).
3. In general, $\text{drop}\ \ge\ \tfrac18+\mu_0-(T_1-\Lambda_A)$, with $T_1=\inf\{t:N_A(t)>\bar P_M(t)\}$ (Lemma 4.3 at $j=1$).

### Corollary 4.6 (a zero drop forces absorption and a window; perfect complexes; compare triangle-1 Prop. 5.6)
Suppose $\Lambda(Y_{-2})\ge\Lambda(Y_2)$ and $\eta_a+\eta_b>0$. Then:
1. the bottom classes of both bundles of $Y_2$ are absorbed;
2. every class of $M$ below $\Lambda_A+\eta_b$ lies in $\operatorname{im}a_*$;
3. $\mu\le\min(u_2,v_2)-\eta_a$ and $\max(u_2,v_2)\le\mu+\tfrac1{16}-\eta$, where $\mu=\ell(C^{\rm tl}_\chi)$ and $u_2,v_2$ are $\lambda_0(Y_2),\lambda_1(Y_2)$. With $\eta_a>0$ this is the window $\mu<\min(u_2,v_2)\le\max(u_2,v_2)<\mu+\tfrac1{16}$.

The copies of $M$ in (I) and (II) are the same complex, which gives item 3 for both bundles.

*Proof.*
- **Item 2.** If $b_*y\neq0$ for a class $y$ of $M$ at level $<\Lambda_A+\eta_b$, then $\Lambda(Y_{-2})\le\operatorname{lev}(y)-\eta_b<\Lambda_A$.
- **Item 1, lower bundle.** Lemma 4.2 shows that the lower of the two bottom classes is absorbed. Its image gives $\mu\le\Lambda_A-\eta_a$.
- **Item 3.** Since $\mu\le\Lambda_A-\eta_a<\Lambda_A+\eta_b$, item 2 shows that the bottom class of $M$ is killed by $b$. This holds in (I) and in (II), which have the same middle complex.
  - Applying $(b,g_M)\colon M\to\mathrm{Cone}(c)$ to that class in each triangle gives a class of $A$, outside $\operatorname{im}c_*$, in the bundle of that triangle. Its level is $\le\mu+\tfrac1{16}-\eta$.
  - So $u_2$ and $v_2$ are both $\le\mu+\tfrac1{16}-\eta$.
- **Item 1, other bundle.** If its bottom class were not absorbed, Lemma 4.2 in the other triangle would give a class of $Y_{-2}$ at level $\le\mu+\tfrac1{16}-\eta-\tfrac18-\eta_g<\mu\le\Lambda_A$, a drop. ∎

### Corollary 4.7 (a cosmetic pair)
Suppose $Y_2\cong Y_{-2}=Y$, preserving orientation. The diffeomorphism preserves $P_0$, $P_1$, $\rho$ and the degrees, so $A\cong B$ as filtered complexes.
- **General case:** $N_Y(t-\tfrac18-\mu_0)\ge N_Y(t)-P_M(t-\mu_0)$ for all $t$.
- **Perfect case:** $k=m/2=r$ (exactness with $\operatorname{rk}A=\operatorname{rk}B$), and
  $$s_{j+r}(Y)-s_j(Y)\ \ge\ \tfrac18+\eta_g\quad\text{for all }j,$$
  where $r$ is the rank of the χ-reduced traceless homology.
- In particular $\operatorname{rk}I(Y)\ge r$. If $\operatorname{rk}I(Y)\ge r+1$, the spectrum must spread over at least $\lfloor(\operatorname{rk}I(Y)-1)/r\rfloor/8$.
- Orientation reversal ($c\mapsto\tfrac38-c$) gives the same gaps, so the top of the spectrum adds nothing.

---

## 5. The argument, step by step

**Step 0. Hypotheses.**
- $\det K=1$.
- T with the levels of §2.3 (Assumed).
- IP-module structure on all three vertices (standard, DLME `prop:IP-mod`, `prop:IP-morphism`; for $SO(3)$ and traceless theories PLAUSIBLE, with the same construction).

**Step 1. The bottom vertex (PROVED, Lemma 4.2).**
- Either the drop is at least $\tfrac18+\eta_g$ (no primitive needed), or it is positive (primitive below $\Lambda_A+\eta_b$),
- or the bottom of $Y_2$ is absorbed into a bar of the traceless theory that is still alive at $\Lambda_A+\eta_b$.
- *Test.* Positive torus knots ($a=0$): the actual drop minus $\tfrac18$ lies in $[0.0061,0.0396]$ over the 27 det-1 cases. That is $\eta_g$, realised.

**Step 2. Counting (PROVED, Lemma 4.3).** $\text{drop}\ge\tfrac18+\mu_0-(T_1-\Lambda_A)$. This needs no energy input beyond $\eta\ge0$.

**Step 3. Cosmetic case (PROVED, Corollary 4.7).**
- A cosmetic pair needs $N_Y(t)-N_Y(t-\tfrac18-\mu_0)\le P_M(t-\mu_0)$ for every $t$.
- In the perfect case this is the spectral gap condition with $r$.

**Step 4. Use of the cover-specific structure (§6).**
- χ makes every multiplicity even, and $M$ the generator set of $C^{\rm tl}(K)$, with no fixed points. This changes no inequality of Steps 1–3; it only removes χ-fixed zero-energy contributions.
- The two lifts and the two isotropy types organise T and show $F\simeq0$.
- The upstairs triangle gives the same shape of statement for $\tilde\ell$.

**Step 5 (missing). Input X (§8).** Show $T_1<\Lambda(Y_2)+\tfrac18$ for $\det K=1$. In the cosmetic case it suffices to show that some $r+1$ consecutive spectral values of $Y$ lie within $1/8$ (perfect case), or the general analogue.

**Conclusion.** T, together with Input X, implies the target theorem. A version with $1/16$ follows from Input X with $\tfrac1{16}$ in place of $\tfrac18$.

---

## 6. What the cover-specific structure gives, item by item

1. **The two lifts of τ to bundles (PROVED for flat connections).**
   - They explain why the natural statements are both-bundle or mixed.
   - The two halves $g^{\rm ns}$ and $g^{\rm sing}$ of the homotopy are the two isotropy types along $\tilde S$, and their $L(4,1)$ faces coincide because the stabiliser $O(2)$ at the $\mathbb{RP}^3$ wall has two components (cover-1 §3.5).
   - This is structural; it does not by itself produce an inequality.
2. **χ (PROVED: freeness).**
   - Every zero-energy contribution to $a$ or $b$ sits at a common point. For $\det K=1$ the binary dihedral common points ($\lambda\mapsto+1$) are absent, because they are exactly the χ-fixed representations.
   - Both examples with $m_2=\tfrac1{16}$ ($4_1$ and $\bar T(2,3)$) are zero-energy absorptions at binary dihedral points (brief; triangle-1 §5.4).
   - Test (COMPUTED, `mixed_counting.py`). Over the mixed triangles of all torus knots with $pq\le60$, the counting bound of Lemma 4.4 (perfect form, with $k$) is $0$ only for $\bar T(2,3)$ (II), the χ-fixed case. Every det-1 case has bound $\ge0.0456$ ($\bar T(3,5)$ (I); actual value $0.0854$).
   - So χ-freeness is the qualitative reason the det-1 data sit well above $1/16$. It gives no quantitative input: tensoring any filtered model with $\mathbb F_2[\mathbb Z/2]$, with χ of level 0, satisfies all constraints (§7).
3. **DLME's ±1 argument with $I(\Sigma)$ handled equivariantly.**
   - The trivial-isotropy part of the middle term is $C(S^3)=0$, and there DLME's argument goes through verbatim. This is the content of $\partial g^{\rm ns}=F$ with an empty $S^3$-face.
   - The order-two part is the traceless theory, and it is the only obstruction.
   - Upstairs, the corresponding statements are cover-1's Theorem 1 and Corollary 2, for $\tilde\ell$: the kernel criterion, and parity for positive $T(p,q)$ with $p,q$ odd.
   - Equivariant localisation does not remove the middle term. Its fixed points are the traceless representations, which exist for nontrivial $K$ (KM).
   - The Lefschetz/eigenspace route needs equivariant transversality and an instanton Smith inequality, neither available (SPECULATIVE). With $\sigma(K)=0$, the expected equal Euler characteristics of the two eigenspaces of $\tau_*$ on $I(\Sigma)$ give no reason for either to vanish.
4. **The 1/16 map $F$ (PLAUSIBLE).** It is null-homotopic (§2.4), so no mixed bound comes from it.

---

## 7. Filtered models with zero drop (PROVED by explicit verification, `cover-code/nogo.py`)

### Proposition 7.1
Take $0<\varepsilon,t\le\tfrac1{16}-\eta$ (for example $\varepsilon=t=\tfrac1{40}$, $\eta=\tfrac1{80}$). Over $\mathbb F_2$, with zero differentials, define, for each bundle $i\in\{0,1\}$ and each of two parity copies:
- **Generators:** $A\ni x_i$ at level $0$; $B\ni z_i$ at level $0$; $M_i\ni y_1$ at level $-\varepsilon$ and $y_2$ at level $t$.
- **Maps:** $a(x_i)=y_1$; $b(y_2)=z_{1-i}$; $g_M(y_1)=x_i$; $g_B(z_{1-i})=y_2$; $c=g_A=0$.

Then:
- **Triangle detection holds exactly:** $ba=cb=ac=0$, and $cg_A+g_Ma=\mathrm{id}$, $ag_M+g_Bb=\mathrm{id}$, $bg_B+g_Ac=\mathrm{id}$.
- **Levels:** all those of §2.3 hold with *strictly positive* energies ($a,b\le-\eta$; $g_M,g_B\le\tfrac1{16}-\eta$).
- **Degrees:** $a,b,c$ have degree 1 and the homotopies degree 3 mod 4.
- **Euler characteristics** are $0$, as forced when $\sigma(K)=0$: $\chi(I^{\rm tl})=-\sigma/2$ by Herald and Lin, and $\chi(A)+\chi(M)+\chi(B)=0$.
- **Bundles:** (I) and (II) use isomorphic middle copies, and the identification $B\cong A$ preserves bundles, levels and degrees.
- **χ:** tensoring with $\mathbb F_2[\mathbb Z/2]$ gives a free χ.
- **Upstairs:** the lift $\tilde c=2c$ ($\delta=0$) respects DLME's upstairs levels.
- **Drop:** both-bundle drop $=m_1=m_2=0$.

In this model $\operatorname{rk}I(Y)=r$, so $c=0$ on homology and the spectral gap condition is vacuous.

**Model 2 (also verified).** Take the spectrum $\{0,s\}$ in each bundle, with $\tfrac18+\eta\le s\le\tfrac3{16}$ (for example $s=\tfrac5{32}$), and $c\neq0$. Both-bundle, the spectrum is $\{0,0,s,s\}$ with $r=2$. All of the above holds again with zero drop.

This shows that the spectral gap condition of Corollary 4.7 is the operative formal constraint. Once the spectrum satisfies it, the formal structure does not exclude a cosmetic pair.

### Consequence (PROVED)
No proof of "drop > 0" can use only the following:
- the exact triangles with their levels (upstairs and downstairs);
- positivity of energy;
- the χ- and τ-symmetries;
- degrees and Euler characteristics.

It needs information about the actual spectra of $I(Y_2)$ and of the traceless theory, or an absorption energy bound. RULES (a) forbids the latter.

The data show such spectral information is what actually produces the drop. For all 27 det-1 mirrors, the bottom-class conditions of Corollary 4.6 that a zero drop would require *all hold*, yet the drop is $\approx\tfrac18$. Two examples (COMPUTED):
- $\bar T(3,5)$: the bottom of $A$ is $-0.6255$ (both bundles), $-0.5961$, $-0.5755$ ($\times2$); the traceless theory $M$ is $2\times\{-0.6292,-0.5792\}$; and $\mu=-0.6292<-0.6255\le\mu+\tfrac1{16}$.
- What rescues the drop is counting. At $t=-0.5961$, $A$ has 3 classes and $M$ only 2, so $\Lambda(Y_{-2})\le-0.5961-\tfrac18=-0.7211$ (actual $-0.7494$).

---

## 8. The missing input, precisely

**Input X (SPECULATIVE; not an energy estimate).** Let $\det K=1$. Let $A$ be the instanton complex of $S^3_2(K)$, summed over both bundles, and $M$ two copies of the χ-reduced traceless complex of $K$. Then there is $t<\Lambda(Y_2)+\tfrac18$ with
$$N_A(t)>\bar P_M(t).$$
- In words: before level $\Lambda(Y_2)+\tfrac18$, the surgery $Y_2$ has more classes born than the traceless theory has bars alive.
- **Perfect form:** $N_A(t)>\min(N_M(t),k)$.
- **Cosmetic form, perfect:** some $r+1$ consecutive spectral values of $Y$ lie within $\tfrac18$.
- **Version with 1/16:** the same with $\tfrac1{16}$ in place of $\tfrac18$. It gives drop $\ge\tfrac1{16}$.

**Why it is not an energy estimate.**
- It compares birth levels of bars, which are ρ-invariants of flat connections when the complexes are perfect, and counts of bars. No instanton energy appears.
- It is not equivalent to the drop; its general form is strictly stronger. Example: for the figure-eight with the first choice of traceless levels, the both-bundle drop is $\tfrac18$, yet $N_A(t)\le N_M(t)$ for every $t$. The perfect form with $k$ does hold there ($T_1=\tfrac{19}{80}$).

**Evidence (COMPUTED).**

| data set | script | result |
|---|---|---|
| 54 det-1 torus knot cases, $pq\le120$ | `capacity.py` | $T_1-\Lambda(Y_2)\le0.0294$ (largest at $\bar T(3,5)$); predicted drop $\ge0.0956$, actual $\ge0.1239$; 0 violations of $s_j(B)<T_j-\tfrac18$ |
| 80 torus knots of any determinant, $pq\le60$, $SU(2)$ counts | `capacity_all.py` | $T_1-\Lambda\le\tfrac1{32}$ (largest at $\bar T(2,3)$); 0 violations |
| figure-eight, both choices of traceless levels | `fig8.py` | (I): bound $m_1\ge\tfrac18$ (actual $13/80$); (II): $m_2\ge\tfrac1{40}+\eta$ (actual $1/16$); sum: drop $\ge\tfrac7{80}$ (actual $1/8$) |
| cosmetic gap $G_r(Y)=\min_j(s_{j+r}-s_j)$ over all 54 det-1 $Y_{\pm2}$ | `spectral.py` | $\le0.013$, against the required $\ge\tfrac18$; no $Y_{\pm2}$ in the data passes |

For the figure-eight, the sum counts treat the χ-fixed generators once.

**Why it is not proved, and what would be needed.**
- There is no a priori comparison between the bottom of the spectrum of $Y_2$ and the bars of the traceless theory.
- In the cosmetic case it would suffice to know $\operatorname{rk}I(Y)>r$ and a clustering of $r+1$ spectral values within $\tfrac18$. Neither is known for hyperbolic $\Delta_K=1$ knots.
- Possible sources (SPECULATIVE):
  - the two single-twist triangles through $Y_0$ ($L_0=\tau_V(L_2)$, $L_{-2}=\tau_V(L_0)$; upstairs, Floer's triangles for slopes $1,0,\infty$ and $0,-1,\infty$ on $\tilde K$), which might bound $\bar P_M$ near $\Lambda(Y_2)$ by bars of $Y_0$;
  - a pillowcase count of $Y_2$-generators near each traceless point.

**Steps that would secretly need an energy estimate.**
1. Bounding the drop below by $\tfrac1{16}$ through "absorption costs $>\tfrac1{16}$" (triangle-1 Thm. 5.7, rho.tex Step 4). Not used here; forbidden.
2. With nonzero differentials, the full $\tfrac18$-gap in Corollary 4.7 holds only if absorption into finite bars of $M$ is excluded. Excluding it by comparing the boundary depth of $M$ with $\eta_a+\eta_b$ would be an energy estimate. Lemma 4.3 avoids this by counting all bars alive ($P_M$) instead, at the price of a weaker statement.
3. Strictness when $T_1=\Lambda_A+\tfrac18$ exactly needs $\mu_0>0$. $\eta_g>0$ always holds; $\eta_a>0$ is the hypothesis that there are no traceless points with $\lambda\mapsto\pm1$, an extra hypothesis even when $\det K=1$.

No step of §4–5 uses any energy fact beyond $E\ge0$, and $E>0$ for $g_A$ on the simply connected $W'$.

---

## 9. Inputs and their status

| input | status | source |
|---|---|---|
| Topology of the cover: $\tilde Y_\pm=\Sigma_{\pm1}(\tilde K)$; branched cover of $W'$ is $W^1_{-1}$; $\hat c,\check c=p^*F^*_{l,r}$ | PROVED | cover-1 §2 |
| Two lifts give $P_0/P_1$; two isotropy types give $S^3$/traceless (flat connections) | PROVED | cover-1 §3.1–3.2 |
| The same for moduli spaces (equivariant gluing at the $O(2)$ wall) | PLAUSIBLE | cover-1 §3.5 |
| χ: degree 4, CS shift $1/2$, $c$-invariant, free when $\det K=1$; Klassen's count | PROVED / standard | §1.3 |
| χ-equivariance of the maps of T | PLAUSIBLE | §1.3 |
| $\tilde c=2c+\delta/8$; upstairs and downstairs counting conditions differ | PROVED | cover-1 Prop. 3.2, §1.4 |
| DLME's upstairs triangle and its levels | PROVED | DLME `prop:CDX-triangle`, `prop:pm-one-map`, `T-detec` |
| Downstairs sum triangle T and the levels of §2.3 | Assumed (RULES (c)); construction PLAUSIBLE | triangle-1 §4 |
| Level formula; lens-space terms $0,\tfrac18,\tfrac14/0,\tfrac3{16}/\tfrac1{16}$ | PROVED (APS) / COMPUTED | brief, rho.tex; `lensterm.py` checks the $\gamma_0,\gamma_1$ terms |
| $\eta_g>0$ | PROVED | §2.3 |
| $F\simeq0$ via $g^{\rm ns}$ | PLAUSIBLE | §2.4 |
| IP-modules, barcodes, DLME `lemma:kappa-ineq`, `lemma:inhomog-ineq` | standard | DLME §3 |
| Lemmas 4.1–4.4, Corollaries 4.5–4.7 | PROVED (given T) | §4 |
| $\chi(I^{\rm tl})=-\sigma/2$ (Herald, Lin); $\sigma=0$ when $\Delta_K=1$ | standard | used only for the models |
| Zero-drop models | PROVED | `nogo.py` |
| Input X | SPECULATIVE | §8 |

---

## 10. Code (`scratchpad/r6/cover-code/`)

All scripts import the generator machinery of `gap16/triangle-code/tk.py`, which was calibrated in gap16 against DLME Example 3.7, Fintushel–Stern and the brief's data.

| file | what it does |
|---|---|
| `spectral.py` (output `spectral.out`) | Both-bundle spectra for det-1 torus knots ($pq\le120$) and their mirrors; χ-multiplicity check; spectral transfer (Lemma 4.4); cosmetic gap $G_r$; bottom-class zero-drop conditions |
| `capacity.py` (output `capacity.out`, cache `spectra_cache.pkl`) | The counting inequality (Lemma 4.3/4.4) for the det-1 cases: $T_1-\Lambda$, predicted versus actual drop |
| `capacity_all.py` (output `capacity_all.out`) | The same for all torus knots with $pq\le60$, in $SU(2)$ counts |
| `mixed_counting.py` (output `mixed_counting.out`) | The counting inequality for the separate triangles (I), (II): bounds for $m_1,m_2$ |
| `fig8.py` | The counting inequality on $4_1$, both choices of traceless levels |
| `lensterm.py` | Level-formula check at common points: exactly $1/8$ for $\gamma_0$, exactly $3/16$ for $\gamma_1$ |
| `nogo.py` | The two filtered models with zero drop of §7, verified mechanically |
