# T5. The ordinary layer as exact-triangle data; $B$ as a distance-four nullhomotopy

Labels: **[V]** verified (computation or argument checked here; numerical checks were run inline with Python), **[P]** plausible, **[S]** speculative.
Literature not in the scratchpad is cited from memory and flagged **(mem)**.
$Y_r=S^3_r(K)$. Manuscript = `src/02-ordinary.tex`, `src/03-negative.tex`. DLME = `dlme/src/triangle-2.tex`, `instanton.tex`.

## 0. Summary

1. The ordinary layer is DLME's distance-two machinery applied to the two triads $\{2,\infty,0\}$ and $\{0,\infty,-2\}$. Each is DLME's triad $\{Z_1,Z_0,Z_{-1}\}$ for the framings $\lambda\pm\mu$. Dictionary: $f_\pm$ are compositions of Floer-triangle maps; DLME's third map is $f_\pm$ up to an $\mathbb{RP}^3$-stretching homotopy; $g_\pm$ is DLME's $g_1$; the manuscript's pentagons are DLME/CDX $h$-maps. One point is new and the manuscript does not state it. On these cobordisms $\mathrm{PD}(S_l)$ and $\mathrm{PD}(S)$ are **divisible by two**. So the two determinant lifts $c$ and $c+\mathrm{PD}(S)$ give the *same* $SO(3)$ bundle, and DLME's two different bundles $\hat c,\check c$ have no analogue. Summing the two lifts amounts to (anti)symmetrising under the $H^1(\,\cdot\,;\mathbb Z/2)$-twists at the two ends: $B=\varepsilon_0(1-s\,\iota)B_0$ with $\iota(T)=\chi\,T\,\chi$ **[V topology, P orientations]**.
2. Composing the two distance-two triangles with the octahedral axiom gives a distance-four triangle $Y_2\to M\to Y_{-2}\xrightarrow{H}Y_2[1]$ **[V formal; P that the third map is $H=f_+f_-$]**. Its middle term $M$ is built from two copies of $I(S^3)\otimes(\text{rank }2)$, so it vanishes. The geometric version has middle term $I(S^3)\otimes V_4$, where $V_4=\langle c,\ c+\mathrm{PD}(S)\rangle\otimes\langle 1,\mu(S)\rangle$ has degrees $0,2,4,6$; its nullhomotopy map is $B$ **[S for a general base; V/P for base $S^3$]**. Three independent reasons force the degree-two insertion **[V]**:
   - degree matching with $g_-g_+$;
   - the minimal trace-zero $L(4,1)$ cap has framed index $2$, against $0$ for the $\mathbb{RP}^3$ cap;
   - the trivial determinants at $Y_{\pm2}$ make every allowed lift even on $S$, so *flat* caps exist at $L(4,1)$ and must be killed.
3. "$B\simeq g_-g_+\simeq H^{-1}$ mod 2" splits into three parts. The first is a chain-level octahedral (associahedral) relation for the path $2,\infty,0,\infty,-2$. The second is a *backtracking* case of CDX's $S^1\times S^2$ ("spherical cut") lemma. The third is the transgression $\mathrm{Hol}_\beta^*[-1]\rightsquigarrow\mu(S)$. Homological algebra alone cannot identify the geometric $B$ with the composite: the octahedral axiom identifies cones, not maps. So some polygon relation with four or more steps, or a distance-four $h$-relation, is unavoidable. The manuscript's 3-dimensional associahedron is the standard one; only the backtracking step is non-standard **[P, high]**.
4. $B$ is DLME's second variation: the middle complex is trivial and $g$ is a chain map, but it is unfavourable. $L-D/8=+\tfrac18-\eta$ for both lifts, against $-\tfrac18-\eta$ for DLME's $g_1$, and the entire $+\tfrac14$ difference comes from the $\mu(S)$ insertion **[V arithmetic, P attribution]**. $g_-g_+$ has exactly the same level shift $+\tfrac18-\eta$ **[V]**.

## 1. Slopes, polygons and cuts

Use slope vectors $w_i$ with $\det(w_i,w_{i+1})=-1$. Define $d_k$ by $w_{k-1}+w_{k+1}=d_kw_k$. An arc between sides $i<j$ cuts off the linear plumbing $[-d_{i+1},\dots,-d_{j-1}]$ (manuscript Lemma `ordinary:polygon`). Computed values **[V]**:

| path | $w$ | $d$ | cuts |
|---|---|---|---|
| $2,\infty,0$ ($g_+$) | $(2,1),(1,0),(0,-1)$ | $2$ | $M_{02}=\mathbb{RP}^3=\partial\nu S_l$ |
| $2,\infty,-2$ ($B$) | $(2,1),(1,0),(2,-1)$ | $4$ | $M_{02}=L(4,1)=\partial\nu S$ |
| $2,\infty,0,\infty,-2$ | $\dots,(-1,0),(-2,1)$ | $2,0,2$ | $M_{13}=S^1\times S^2=\partial\nu U$; $M_{04}$: $[-2,0,-2]$, $\det=4$, $L(4,1)$ |
| $2,\infty,0,1,2$ (compressed $h$) | | $2,1,2$ | $M_{04}$: $[-2,-1,-2]$, $\det 0$, $S^1\times S^2$ |
| $-2,-1,0,1,2$ ($H$) | | $2,2,2$ | $M_{04}$: $A_3=[-2,-2,-2]$, $L(4,3)$ |

The complement of the outermost cap $M_{0k}$ is DLME's "$X$" for the pair $(s_0,s_k)$. It is $[-1,1]\times E(K)$ with two solid tori glued in, and its middle end is a lens space. So DLME's third map $f_2=(X,c)_*$ is a cobordism with a lens-space middle end. Capping that end by the plumbing gives the composite along the path. **[V topology]**

Two slopes at distance one from both $2$ and $-2$: solving $|2b-a|=|{-2b-a}|=1$ gives only $\infty$. Two slopes at distance one from both $2$ and $0$: $\infty$ and $1$. **[V]** So the only triangle on $\{2,-2\}$ with "edge distances $1,1$" has middle $S^3$. The pair $\{2,0\}$ has two distance-two triads, with middle $S^3$ (trivial) or $Y_1$ (nontrivial). This is relevant in §5.

## 2. The dictionary, and what changes from DLME

### 2.1 Dictionary

| manuscript | DLME/CDX | status |
|---|---|---|
| $u_r\colon Y_r\to Y_{r+1}$ ($r=0,1$), $f_+=u_1u_0$, mirror $f_-$ | $f$-maps of Floer's triangle for the triads $(r,r+1,\infty)$. The third vertex $C(S^3)=0$ makes each an isomorphism (DLME Prop. `prop:Floer-triangle`) | [V] structure |
| pentagons on $s\to\infty\to r\to s$, $r\to s\to\infty\to r$ giving $u_rh_1\simeq J_s$, $h_2\tilde u_r\simeq J_r$ | the $h$-relations $f_{i-2}g_i+g_{i-1}f_i+[d,h_i]=q_i\simeq1$ of triangle detection (DLME Prop. `T-detec`). The term through $C(S^3)$ drops, and the $[-1,-1]$ hard cap is the CDX/DLME $q_i$-face | [V] |
| $g_+\colon Y_2\to S^3\to Y_0$: interval from $J$ to the $\mathbb{RP}^3$ split around $S_l=A-F_l$, summed over $c_0,c_0+\mathrm{PD}(S_l)$ | DLME's $g_1$ for the triad $(Z_1,Z_0,Z_{-1})=(Y_2,S^3,Y_0)$, framing $\lambda+\mu$. $W^1_{-1}=-C_2\cup_{S^3}C_0$; $N\cup2B^4=\nu S_l$; $c_0\leftrightarrow\hat c$, $c_0+\mathrm{PD}(S_l)\leftrightarrow\check c$ | [V] topology |
| $g_-$ | DLME's $g_1$ for $(Y_0,S^3,Y_{-2})$, framing $\lambda-\mu$ | [V] |
| compressed pentagon $2,\infty,0,1,2$, $f_+g_+\simeq J_2$ | DLME's $h_i$ with the block $0\to1\to2$ frozen. The $[-2,-1,-2]$ cap with two harmonic paths meeting at $\theta_*$ (the $\mathbb{RP}^3$ end) is DLME's pasting $M(N',\hat c)^{\rm red}\cong[-1,0]$, $M(N',\check c)^{\rm red}\cong[0,1]$ at the $\mathbb{RP}^3$-broken metric (proof of DLME Prop. `prop:h`) | [V] structure |
| DLME's third map $f_2=(X_{0,2},c)_*\colon Y_0\to Y_2$ ($\mathbb{RP}^3$ middle end, $b^+=1$) | $\simeq f_+$ mod 2. The path $0\to1\to2$ has $M_{02}=\mathbb{RP}^3$ cutting off the $(-2)$-sphere at slope $1$. Stretching from the $Y_1$ split to the $\mathbb{RP}^3$ split gives $f_+\simeq(X_{0,2})_*\circ(\text{minimal trace-zero cap})$, and that cap has framed index $0$ and count $1$ (manuscript Lemma `ordinary:cap-shifts`) | [P] |
| $H=f_+f_-$ | the third map of the distance-four triangle (§3.1): $X_{-2,2}$ with its $L(4,3)$ end capped by $A_3$ | [P] |
| $B$ | the nullhomotopy ("$g$") map of the distance-four triangle (§3) | [P]/[S] |

### 2.2 The two lifts are tensor-equivalent

**Proposition 2.1 [V topology].** Let $(W,S)$ be $(-C_2\cup C_0,S_l)$ or $(-C_2\cup C_{-2},S)$. Then $H_1(W)=0$, and in $H^2(W;\mathbb Z)=\mathrm{Hom}(H_2W,\mathbb Z)$:
$$\mathrm{PD}(S_l)=(2,0)\ \text{on }(F_l,A),\qquad \mathrm{PD}(S)=(-2,2)\ \text{on }(F_l,F_r).$$
So $\mathrm{PD}(S)=2a$, and $E_{c+\mathrm{PD}(S)}\cong E_c\otimes L_a$ have the same adjoint bundle. For DLME's $-C_1\cup C_{-1}$, $\mathrm{PD}(S)=(-1,1)$ is odd: $\hat c=(0,1)$ and $\check c=(1,0)$ are different $SO(3)$ bundles.

The bundles are identified off $\nu S$ by the canonical section of $\mathcal O(S)=L_a^2$. With that identification, $L_a|_{W\setminus\nu S}$ is the flat $\mathbb Z/2$ bundle with holonomy $-1$ around the meridian $\mu_S$. Here $H_1(W\setminus\nu S)=\mathbb Z/2$: the image of $H_2(W)\to\mathbb Z$, $F\mapsto F\cdot S$, is $2\mathbb Z$. The meridian $\mu_K$ of $K$ on each true end bounds a cocore disk meeting $S$ once, because $S$ contains both cores, so $\mu_K\sim\mu_S$. Hence the twist restricts to the nontrivial character on each end:
- $\chi$ on $Y_{\pm2}$, where $H^1(Y_{\pm2};\mathbb Z/2)=\mathbb Z/2$ and $c_1(\chi)=\beta(\chi)\ne0$;
- $\varepsilon$ on $Y_0$, where $c_1(\varepsilon)=0$.

**Corollary 2.2 [V modulo orientation signs].** On chains, with $\chi$-invariant end perturbations,
$$g_+^{c_0+\mathrm{PD}(S_l)}=\varepsilon\,g_+^{c_0}\,\chi,\qquad B_1=\chi\,B_0\,\chi .$$
Over $\mathbb Z$ the identities hold up to a sign. Over $\mathbb F_2$: $g_+=g^{c_0}_++\varepsilon g^{c_0}_+\chi$, and $B=B_0+\chi B_0\chi$. The manuscript sums the lifts but never states that they are twists of each other.

Two consequences. **[V]**
- $\chi$ shifts $\widetilde{\mathrm{CS}}$ by $\tfrac12$ (mod 1). Indeed $-c^2/4$ changes by $\tfrac12$ for $c=2F_l^*$ on $-C_2$. It shifts the $\mathbb Z/8$ grading by $4$. So $\mathrm{CS}-\mathrm{gr}/8$ is $\chi$-invariant, and DLME's $\ell(Y_{\pm2})$ does not see $\chi$.
- Sanity check of 2.1. If the twist acted at one end only, then $g_+=g(1+\chi)$ with $(1+\chi)^2=0$ over $\mathbb F_2$. Such a map cannot be an isomorphism unless $I(Y_2;\mathbb F_2)=0$. The twist in fact acts at both ends, by $\varepsilon$ on $Y_0$ and $\chi$ on $Y_2$, so there is no clash.

### 2.3 What changes when DLME §5 is transplanted to $Y_{\pm2}$ and to $Y_0^w$

| item | DLME (ZHS ends) | here | status |
|---|---|---|---|
| reducibles on true ends | central $\theta$ | $Y_{\pm2}$: two central flats $\theta,\chi\theta$, both with $(h^0,h^1)=(3,0)$; $Y_0^w$: none | [V] |
| Lemmas `no-irred-only`, `min-index`, `g-bdry0/1` | use only "true-end reducibles are central, $h^0=3$" | unchanged on $Y_{\pm2}$; at $Y_0$ the cases with a reducible piece meeting $Y_0$ disappear | [V] |
| bundles | $\hat c=\varnothing\sqcup c_+$, $\check c=c'_+\sqcup\dots$ | DLME's $\check c$ restricts to $-C_2$ as the cocore class, which is *nontrivial* on $Y_2$ (it would change $I(Y_2)$ into $I^w(Y_2)$). Forced replacement: $c_1=c_0+\mathrm{PD}(S_l)$. Up to tensoring by lines trivial on the ends, it is the only other class that agrees with $c_0$ off $\nu S_l$ and is trivial on $Y_2$. It is odd on $S_l$: $c_e(S_l)=\pm1$ | [V] |
| middle term | $I(Y)\oplus I_{*+2}(Y)$ | $I(S^3)\oplus I_{*+4}(S^3)$, because $c_1|_{-C_2}=2F_l^*$ has $c^2=-2$. It is $0$ anyway | [V] |
| same vs. different $SO(3)$ bundles | different | same (Prop. 2.1) | [V] |
| $\mathbb{RP}^3$-end identity $R^{\hat c}=R^{\check c}$ | identical exteriors | identical exteriors, *and* equivariant under the global twist: $R^{c_1}=\varepsilon R^{c_0}\chi=R^{c_0}$ | [V] |
| coefficients | $\mathbb F_2$ ("expected over any ring") | $\mathbb F_2$ for $g_\pm$. Integral weights are available by the manuscript's own Prop. `negative:local-sign` mechanism (§3.4) | [P] |
| filtration | $g_1$ is an IP-morphism of level $\tfrac14-\eta$ | $g_\pm$ have no level: $Y_0^w$ is not a rational homology sphere. Only composites $Y_2\to Y_{-2}$ ($B$, $g_-g_+$) are filtered | [V] |
| third map | $X$ with $\mathbb{RP}^3$ middle end | $X_{0,2}$; $\simeq f_+$ (§2.1) | [P] |

Analytically nothing new is needed for $g_\pm$ beyond what DLME §5.3–5.5 does. The manuscript's Section 2 is that proof with the reducible bookkeeping redone for $\mathbb Z/2$ ends **[P, high]**.

## 3. Distance four

Convention: a count of fixed-limit index $i_0=\mathrm{codim}-\dim G$ on $(W,c)$ with rational-homology-sphere ends has degree $D=-2c^2-3b^+-i_0$ and level $L=-c^2/4-\eta$. Then $L-D/8=-\eta+\tfrac38b^+-\tfrac18(\dim G-\mathrm{codim})$, independent of $c$. For DLME's $g_1$ this gives $D=3$, $L-D/8=-\tfrac18-\eta$, as in DLME Prop. `prop:pm-one-map`. **[V]**

### 3.1 The octahedral composite [V formal; P for the identification of the third map]

For a general base (a knot in a homology sphere $Y$; here $Y=S^3$), DLME's triangles for the two triads read
$$T_+:\ C(Y_2)\xrightarrow{a_+}C(Y)\otimes V_+\xrightarrow{b_+}C^w(Y_0)\xrightarrow{c_+}C(Y_2)[1],\qquad T_-:\ C^w(Y_0)\xrightarrow{a_-}C(Y)\otimes V_-\xrightarrow{b_-}C(Y_{-2})\xrightarrow{c_-}C^w(Y_0)[1],$$
with $\operatorname{rk}V_\pm=2$ and $c_\pm\simeq f_\pm$ (§2.1). Apply the octahedral axiom to $c_+\circ c_-$. Since $\mathrm{Cone}(c_\pm)\simeq C(Y)\otimes V_\pm[1]$, there is an exact triangle
$$C(Y_2)\to M\to C(Y_{-2})\xrightarrow{\ c_+c_-\simeq f_+f_-=H\ }C(Y_2)[1].$$
Here $M$ is the twisted complex $C(Y)\otimes V_+\xrightarrow{\ a_-b_+\ }C(Y)\otimes V_-$, whose connecting map runs through $C^w(Y_0)$. Two consequences:
- The octahedral axiom predicts a *distance-four* triangle with middle term of rank $4\cdot\operatorname{rk}I(Y)$, and identifies its third map as $H$.
- For $Y=S^3$, $M=0$. The triangle-detection data of the composite has $g$-component $g_-g_+$, since every other path runs through $M$.

So *the composed triangle's nullhomotopy is $g_-g_+$, not $B$*. The octahedral axiom identifies cones up to non-unique isomorphism. It cannot show that the geometric single-seam map $B$ represents the same class. That needs geometry (§4).

### 3.2 The geometric distance-four triangle [S for a general base]

**Conjecture 3.1.** For $K$ in a homology sphere $Y$ there is an exact triangle (over $\mathbb F_2$, and plausibly over $\mathbb Z$)
$$I(Y_2)\xrightarrow{a}I(Y)\otimes V_4\xrightarrow{b}I(Y_{-2})\xrightarrow{h}I(Y_2),\qquad V_4=\langle c_0,\,c_0{+}\mathrm{PD}(S)\rangle\otimes\langle1,\mu\rangle .$$
- The components of $a$ are $(-C_2,c_e|,\mu(F_l)^\delta)$; their degrees are $0,-2,4,2\equiv\{0,2,4,6\}\pmod8$.
- The components of $b$ are $(C_{-2},c_e|,\mu(F_r)^{1-\delta})$.
- The nullhomotopy of $b\circ a$ is $B$: the $J$-face of $B$'s interval is $b\circ a$. This uses $\mu(S)=\mu(F_l)-\mu(F_r)$ at the $J$ split. The Seifert surface pieces cancel up to a homotopy term $\mu(\Sigma)$ acting on $C(Y)$, which I have not analysed.
- $h=(X_{-2,2},c)_*$ with its $L(4,\cdot)$ middle end capped. By §1 this is $\simeq H$.

For $Y=S^3$ the conjecture reduces to: $B$ is a chain map ([V], manuscript Prop. `negative:invariance`) and $HB\simeq1\simeq BH$. That is the triangle-detection $h$-relation with zero middle, and it is consistent with §4.

Rank sanity check (mem, unsure). I recall Heegaard Floer surgery triangles $\widehat{HF}(Y_p)\to\widehat{HF}(Y)^{\oplus(p-q)}\to\widehat{HF}(Y_q)$ for integers $p>q$, whose case $(1,-1)$ is the one DLME cite. For the unknot, $(2,-2)$ gives ranks $2,4,2$, which is admissible.

SU(2) supplies only two lifts of $c$ that are trivial on both $Y_{\pm2}$: $c(F)\equiv0,2\pmod4$, related by the $\chi$-twist. The missing factor $2$ in rank is supplied by $H^*(S^2)$, through $\mu$. Compare (mem, unverified): CDX's $SU(N)$ triangle (its $N=2$ case is DLME Prop. `prop:CDX-triangle`, as DLME state) has, as I recall, $N$ middle copies indexed by the $\mathbb Z/N$-centre bundle choices $c+k\,\mathrm{PD}(S)$, with $L(N,1)$-type middle ends. If so, SU(2) at distance four is *not* covered by CDX, and $\mu(S)$ is how SU(2) replaces the two missing central bundles. **[S]**

### 3.3 Why a degree-two insertion is forced, and why it must be $\mu(S)$ [V]

**(R1) Degree.** View $g_-g_+$ as the count on the composite $W_4$: $\dim G=2$, $b^+=1$, $c=\mathrm{PD}(U)$, $c^2=0$. Its degree is $D=-1$. A count on $W'$ over the interval with no insertion has $D=-2c^2+1\equiv1\pmod 8$ for $c^2\in\{0,-4\}$. Matching requires $\mathrm{codim}\equiv2\pmod 8$. Since $b_1(W')=0$, the degree-two classes are $\mu(\Sigma)$ for $\Sigma\in\langle F_l,F_r\rangle$. Level check: $L-D/8=\tfrac18-\eta$ both for $g_-g_+$ on $W_4$ and for $B$ (both lifts). Surgery on $U$ changes the shift by $-\tfrac38$ (losing $b^+=1$), then $+\tfrac18$ (losing one parameter), then $+\tfrac28$ (gaining a codimension-two insertion). The net change is $0$. Script: $D,\ L-D/8+\eta$ = $(3,-\tfrac18)$ for $g_1$; $(-1,\tfrac18)$ and $(7,\tfrac18)$ for $B$; $(-1,\tfrac18)$ for $g_-g_+$; $(1,-\tfrac18)$ for the insertion-free interval.

**(R2) Flat caps.** Triviality at $Y_{\pm2}$ forces $c(F_l),c(F_r)$ even, hence $c(S)$ even. So every allowed bundle restricts to $\nu S$ with $w_2=0$, and $\nu S$ (simply connected) carries flat caps, with boundary $\pm1$ central and framed index $0$. In an insertion-free interval count the $L(4,1)$ end therefore contains the terms (rigid exterior with central $L(4,1)$ limit) $\times$ (flat cap). Index check: $i_{\rm ext}-3+3=0$. These terms are $R(\theta)$ for $c_0$ and $R(-1)$ for $c_1$, two different exterior counts, and they do not cancel. Consequently the insertion-free interval is only a homotopy $W'_*(g_{L(4,1)})\simeq W'_*(g_J)=0$, not a chain map. Contrast distance two: there $c(S_l)=c(A)-c(F_l)$ is odd (admissibility at $Y_0$), so no flat caps exist at $\mathbb{RP}^3$; likewise in DLME's $\pm1$ case. An insertion supported in $\nu S$ kills flat caps, because flat holonomy on the simply connected $\nu S$ is $+1$. The only degree-two class supported in $\nu S$ is $\mu(S)$.

**(R3) Framed index of the minimal non-flat cap.** Use DLME's index formula (Lemma `min-index`) with $h^0=1$: framed index $=8E-1+\rho/2$, where $\rho$ is the APS invariant of the adjoint character $\lambda^2$ of the trace-zero flat. Here $\rho(L(p,q),k)=-\tfrac4p\sum_j\cot\tfrac{\pi j}p\cot\tfrac{\pi qj}p\sin^2\tfrac{\pi kj}p$ (standard formula, mem).
- $\mathbb{RP}^3$: $E=\tfrac18$, $\rho(L(2,1),1)=0$, framed index $0$.
- $L(4,1)$: $E=\tfrac14$, $|\rho(L(4,1),2)|=2$, framed index $1\pm1$.

The manuscript's independent $\mathbb F_4/\mathbb P(1,1,4)$ computation (complex normal index $1$) fixes the sign, giving framed index $\mathbf 2$; this also agrees with Fintushel–Stern's unframed dimension $1$ (mem). So the distance-two lens end is *rigid*: that is DLME's cancelling $\mathbb{RP}^3$ term. The distance-four minimal cap instead comes in a framed $2$-dimensional family (one complex normal direction), and a rigid, cancellable lens end appears only after cutting by a codimension-two class supported on $S$.

On this family $\mu(S)$ has degree $\pm1$. It is the $\langle d,S\rangle/2=1$ instance of "$\mu(\Sigma)$ on an abelian locus is $\langle c_1(L),\Sigma\rangle$ times the generator", which is the manuscript's eigenvalue-winding computation in Lemma `negative:cap`. Status: [V] for the $\rho$-sums and $E$; [P] for the sign.

**Conclusion.** (R1) forces a degree-two insertion. (R2)+(R3) force it to be supported in $\nu S$ and nonzero on the minimal trace-zero cap, which leaves $\mu(S)$ up to a scalar. $\mu(F_l+F_r)$ is orthogonal to $S$ and vanishes on the cap family. $\mu(F_l)$ alone does not kill flat caps. So the insertion is not a choice. **[V/P]**

### 3.4 Integral cancellation at $L(4,1)$, and the comparison with $\mathbb{RP}^3$

The manuscript's mechanism (Prop. `negative:local-sign`) has three steps.
1. The two lifts have identical exterior data. The caps are related by tensoring with $L_a$, $a=-2x$, $2a=\mathrm{PD}(S)|_{\nu S}$.
2. The relative orientation $s$ of corresponding terms is a single sign, independent of the exterior. The reasons: orientation transport over connected reference spaces; orientability on the determinant-one quotient; and the even framed cap index, which rules out an exterior-dependent interchange sign.
3. Choose the weights $\varepsilon_1=-s\varepsilon_0$.

**Reformulation [V, given 2.2].** Let $\iota(T)=\chi T\chi$. The $L(4,1)$ term of $B_0$ satisfies $\iota R_0=R_1=sR_0$: the first equality is the global twist, the second the local comparison. Hence
$$B=\varepsilon_0(1-s\iota)B_0,\qquad (1-s\iota)R_0=0\ \text{ over }\mathbb Z,\qquad \iota B=-sB.$$
"Summing over $w$ and $w+\mathrm{PD}(S)$" is projection onto an eigenspace of the twist involution. It kills exactly the lens wall, because the lens wall lies in the opposite eigenspace. Over $\mathbb F_2$ this reads $\chi B=B\chi$.

**$\mathbb{RP}^3$ [P].** Steps 1–3 hold verbatim for the $(-2)$-cap: $a=-x$ is integral and the framed index $0$ is even. So the "mod 2 only" status of $g_\pm$ in DLME and in the manuscript is a choice made for convenience (only $\mathbb F_2$-invertibility of $g_\pm$ is used), not a structural asymmetry.

For an integral $h$-relation $f_+g_+\simeq\pm J_2$, the two harmonic paths on the $[-2,-1,-2]$ cap must concatenate at $\theta_*$ into an oriented path from $0$ to $\pi$. That concatenation uses the same corner-orientation datum as the $M_{02}$ cancellation, so the weights that cancel $M_{02}$ also orient the concatenation. This is DLME's pasting $[-1,0]\cup_0[0,1]$ read with orientations.

A difference is possible only in the *natural* value of $s$. The boundary Weyl conjugation acts on the complex normal kernel by complex conjugation, with sign $(-1)^k$, where the complex normal index $k$ is $0$ for $\mathbb{RP}^3$ and $1$ for $L(4,1)$. So with untwisted orientations one wall plausibly cancels in the sum and the other in the difference **[S]**. This is immaterial, since the weights are chosen.

Fintushel–Stern link (mem) **[P]**. The minimal trace-zero cap has $|\langle d,S\rangle|=2=-S^2-2$. That is the adjunction-extremal class for a $(-4)$-sphere, the kind of class that survives rationally blowing down $\nu S$ (the $p=2$ case of FS 1997). The lift pairing $c\leftrightarrow c+\mathrm{PD}(S)$ is the Floer-level form of their projection.

## 4. $B\simeq g_-g_+\simeq H^{-1}$ mod 2, in triangle language

**Theorem 4.1.** Over $\mathbb F_2$, $B\simeq g_-g_+$, and on homology $g_-g_+=(f_+f_-)^{-1}$ up to continuation isomorphisms. Hence $B_*=H_*^{-1}$.

**Step 0 (formal) [V, given the $h$-relations].** The compressed pentagon gives $f_+g_+\simeq J_2$ (DLME's $h$-relation with zero middle), and $f_+$ is an isomorphism (Floer). So $g_+=f_+^{-1}J_2$ on homology, and the mirror argument gives $g_-=f_-^{-1}$. This proves the second equality. The first equality is not formal (§3.1), and the remaining steps prove it.

**Step 1 (the chain-level octahedral relation) [P; facet bookkeeping V].** Take the path $(2,\infty,0,\infty,-2)$ on $W_4$, the 3-dimensional associahedral family, and the sectors $c=\mathrm{PD}(U)+e\,\mathrm{PD}(S_l)+e'\mathrm{PD}(S_r)$ with product weights. This is the four-step polygon relation of the surgery-cube formalism (Ozsváth–Szabó link surgery, Kronheimer–Mrowka unknot detector; mem). It is the chain-level form of composing two exact triangles. The nine facets contribute as follows (numbers from manuscript Lemma `negative:faces`, rechecked):

| facet | cap / split | contribution |
|---|---|---|
| $Z_1,Z_3$ | $S^3$ | $0$, since $C(S^3)=0$ |
| $Z_2$ | $Y_0$ | $g_-g_+$; the lift sums factor |
| $M_{02},M_{24}$ | $\mathbb{RP}^3$, $(-2)$-caps | cancel in lift pairs $e\leftrightarrow1-e$ (resp. $e'$), as in DLME's proof of Prop. `prop:g` |
| $M_{03},M_{14}$ | $[-2,0]$, $\det=-1$, $S^3$ | $d^2=2b(d+b)\in4\mathbb Z$, so $E\in\mathbb Z_{>0}$ and shift $\ge5$: empty |
| $M_{04}$ | $[-2,0,-2]$, $\det 4$, $L(4,1)$ | $E\ge\tfrac14$, shift $8E-3\ge-1>-2$: empty |
| $M_{13}$ | $[0]=\nu U$, $S^1\times S^2$ | the backtracking face (Step 2) |

Hence $g_-g_+\simeq(\text{count at }M_{13})$.

**Step 2. Lemma 4.2 (backtracking spherical cut) [P].** Suppose a path of slopes contains $s\to t\to s$ with $\Delta(s,t)=1$. The composite then contains a square-zero sphere $U$ (the side $t$) with a dual capped surface $A$, $A\cdot U=1$. Let $W_U$ be the result of replacing $\nu U=S^2\times D^2$ by $S^1\times D^3$; this shortcuts the path. Let $\beta=S^1\times0$. Suppose $c\cdot A$ is odd. Then the facet $M_U$ is computed as follows:
- sectors with $c\cdot U$ odd contribute $0$;
- sectors with $c\cdot U$ even contribute, with coefficient one, the count on $W_U$ over the facet's remaining parameters with the codimension-three condition $\mathrm{Hol}_\beta=-1$. Holonomy is normalised by a determinant root on $W_U$.

*Sketch.*
- (a) If $w_2(U)\neq0$ there is no projectively flat limit on $S^1\times S^2$.
- (b) The charge on $\nu U$ is integral, so nonflat caps cost $8$; only flat caps survive.
- (c) The roots on $\nu U$ and on $W_U$ differ by the class in $H^1(S^1\times S^2;\mathbb Z/2)$ whose Mayer–Vietoris image is $c\bmod2\neq0$, because $c\cdot A$ is odd. So the flat cap sits at the central value $-1$.
- (d) At a central flat on $S^1\times S^2$ we have $h^0=h^1=3$. The flat cap absorbs the stabiliser, and matching imposes exactly three conditions, $\mathrm{Hol}_\beta=-1$.
- (e) The replacement changes $\chi$ by $-2$, which raises the index by $3$; this balances the codimension.

These steps are the manuscript's Lemmas `negative:root` and `negative:pentagon`.

**Relation to CDX.** CDX's spherical cut (DLME Lemma `h5` and Prop. `prop:h`) is the *full-loop* case $s\to\cdots\to s$. There the cap carries a one-parameter reducible family mapping with degree one onto $\mathfrak X(S^1\times S^2)=[-1,1]$, and $W_U$ is the identity cylinder, giving $q\simeq1$. In the backtracking case the cap carries no parameter, and its only flat lies at the central point $-1$ ("degree one onto a point"); that is, it gives a codimension-three condition. And $W_U$ is the shortcut $W'=-C_2\cup C_{-2}$, not a cylinder. It is the same lemma with degenerate data.

**Step 3 (transgression) [P].** In $W'$ the loop $\beta$ bounds two disks $\Delta_l,\Delta_r$, the preimages of the two halves of the merged $\infty$-side, and $\Delta_l\cup\Delta_r=\pm S$. Sweeping $\Delta$ by loops from $\beta$ to a constant loop exhibits $\{\mathrm{Hol}_\beta=-1\}$ as a boundary, $\mathrm{Hol}^*_\beta[-1]=\delta\,x(\Delta)$, wherever the collapsed end avoids $-1$.

Use $\Delta_l$ on the part of the pentagon $P$ adjacent to the ball edge $M'_{03}$, where $\Delta_l$ lies in the simply connected cap. Use $\Delta_r$ near $M'_{14}$. These two edges are incompatible, so the two choices must disagree along an interval $I\subset P$ running from a primary $J$-edge to the $M'_{04}$-edge. Along $I$ the difference of the two contractions is $x(\Delta_l)-x(\Delta_r)=x(S)=\mu(S)$. After the replacement, $M'_{04}$ is exactly $\nu S$ with boundary $L(4,1)$. **So $I$ is $B$'s interval.**

This explains *why* $B$ is an interval from the $S^3$ split to the $L(4,1)$ split. It is the seam, in the pentagon left by the backtracking cut, between the two incompatible contractions of $\beta$.

Concatenating the steps:
$$g_-g_+\ \overset{(1)}{\simeq}\ M_{13}\ \overset{(2)}{\simeq}\ \bigl(P,\ \mathrm{Hol}_\beta=-1\ \text{on }W'\bigr)\ \overset{(3)}{\simeq}\ \bigl(I,\ \mu(S)\ \text{on }W'\bigr)=B .$$

**Can the 3-dimensional associahedron be avoided? [V as a logical point.]** Not by homological algebra. The octahedral axiom produces *some* distance-four triangle, with nullhomotopy $g_-g_+$. Identifying it with the geometric $B$ is a chain-level statement about $B$, and it needs either Step 1, which is the standard 4-step polygon and not bespoke, or a distance-four $h$-relation. What is genuinely non-standard is only Lemma 4.2, together with Step 3.

**Alternative route: distance-four triangle detection [S].** One could prove $HB\simeq J$ directly with a compressed pentagon on the cycle $2\to\infty\to-2\Rightarrow_H2$, with $\mu(S)$ inserted. Its faces would be:
- $J$: empty;
- the $Y_{-2}$ split: $H\circ B$;
- the cap around $\infty$: the $L(4,1)$ wall, which cancels in the $\iota$-eigenspace exactly as in $B$'s chain-map proof;
- the cut from $\infty$ to the end: a unimodular $S^3$ cap, since $\Delta(\infty,2)=1$, presumably excluded by charge;
- the hard $S^1\times S^2$ cap.

The hard cap is the chain $[-4,-1,-2,-2,-2]$, which has $\det 0$ (computed via $d$-values $4,1,2,2,2$). It blows down to $[0]$, and it contains $S$. The missing input is that the $\mu(S)$-cut reducible family on this cap has odd degree onto $\mathfrak X(S^1\times S^2)$; a blow-up-formula computation seems feasible but has not been done. This route is 2-dimensional, and it is literally the $h$-relation of Conjecture 3.1 for base $S^3$.

## 5. DLME's remark on $\pm2$

DLME (end of the introduction) say that one variation has a nontrivial middle complex, so $g_1$ is not a chain map, and that another has a trivial middle and $g_1$ is a chain map but "behaves unfavorably with respect to the Chern–Simons filtration". We cannot know which constructions they meant. The following reading is consistent with everything above.

**The second variation is $B$ (equivalently $g_-g_+$) [V arithmetic, P attribution].**
- The middle is copies of $C(S^3)=0$, and $B$ is a chain map.
- $L-D/8=+\tfrac18-\eta$ for both lifts. For DLME's $g_1$ it is $-\tfrac18-\eta$. The difference $+\tfrac14$ is exactly the codimension-two insertion. By §3.3 the insertion is forced, so no favourable chain-map variation exists among trivial-middle distance-four constructions of this type.

Precisely, "unfavourable" means the following. Composing with $\phi$, $B\phi\colon Y_{-2}\to Y_{-2}$ is injective, and DLME's Lemma `kappa-ineq` gives only $\eta_B\le\tfrac18$. A contradiction would need the a priori bound $\eta_B>\tfrac18$ on the least energy of instantons with irreducible limits over the family. Contrast DLME, where $\eta>-\tfrac18$ is automatic. Likewise $HB\simeq1$ forces $\eta_H+\eta_B\le\tfrac12$, since $H$ has $L-D/8=\tfrac38-\eta_H$. This is a sanity check showing that the CS level of the block $HB$ is non-negative, which is why the spin-coupled level of the brief is needed **[P]**.

**The first variation [S].** The best candidate is the *other* distance-two triad on $\{2,0\}$ (§1: slope $1$ is at distance one from $2$ and from $0$):
$$I(Y_2)\to I(Y_1)\oplus I(Y_1)\to I^w(Y_0)\to,$$
and its mirror $(Y_0,\ Y_{-1}^{\oplus2},\ Y_{-2})$. This is literally DLME's triangle for the dual knot $K'\subset Y_1$ with the non-Seifert framing $\lambda'=\mu_K$: indeed $\mu'\pm\lambda'=(\mu+\lambda)\pm\mu$ gives the slopes $2$ and $0$. The middle complex is $C(Y_1)^{\oplus2}\neq0$, so its $g$ is not a chain map. Other candidates are a $(Y_2,\ Y_0\otimes V,\ Y_{-2})$ "distance $(2,2)$" triangle (slope $0$ is at distance two from both $\pm2$) and the insertion-free distance-four interval of §3.3(R2), whose flat $L(4,1)$ caps act as a nonzero lens "middle".

## 6. Verdict

| claim | status | confidence |
|---|---|---|
| Dictionary: $f_\pm$ = Floer-triangle composites; $g_\pm$ = DLME $g_1$ for framings $\lambda\pm\mu$ with middle $C(S^3)^{\oplus2}=0$; pentagons = DLME/CDX $h$-maps; compressed hard cap = DLME's pasted $[-1,0]\cup[0,1]$ | V (topology/bookkeeping), P (analysis, already in the manuscript) | 90% |
| The two lifts are tensor-equivalent: $\mathrm{PD}(S_l),\mathrm{PD}(S)$ are even, and $B=\varepsilon_0(1-s\iota)B_0$, $g_+=g^0+\varepsilon g^0\chi$; "sum over $w,w+\mathrm{PD}(S)$" = projection onto an eigenspace of the end twist | V (topology), P (orientation constancy) | 85% |
| DLME's $\check c$ is illegal at $Y_2$, and $c_0+\mathrm{PD}(S_l)$ is the forced replacement | V | 95% |
| Octahedral composite: distance-four triangle with third map $H$, middle of rank $4\cdot\operatorname{rk}I(Y)$, nullhomotopy $g_-g_+$ | V formal, P ($c_\pm\simeq f_\pm$) | 80% |
| Geometric distance-four triangle $(Y_2,\ I(Y)\otimes V_4,\ Y_{-2})$ with $V_4=\{\text{2 lifts}\}\otimes\{1,\mu\}$ and $g$-map $B$ | S for a general base; for base $S^3$ it is "B chain map, $HB\simeq BH\simeq1$", which holds mod 2 | 40% / 85% |
| $\mu(S)$ insertion forced: by degree, by framed index $2$ (vs. $0$) of the minimal trace-zero cap, and by flat caps at $L(4,1)$ | V ($\rho$ sums, parity, degrees), P (sign of $\rho$ taken from the manuscript) | 90% |
| Integral cancellation at $L(4,1)$ via constant relative sign; the same mechanism makes $g_\pm$ integral | P | 75% |
| $B\simeq g_-g_+\simeq H^{-1}$ mod 2 via 4-step polygon relation + backtracking spherical cut + transgression | P (it is the manuscript's proof, re-derived) | 80% |
| The 3-dimensional associahedron is not removable by homological algebra; a distance-four $h$-relation (pentagon with hard cap $[-4,-1,-2,-2,-2]$) is the only alternative | V (logic), S (feasibility) | — |
| $B$ = DLME's "trivial middle, chain map, unfavourable" variation | V (arithmetic), P (attribution) | 75% |

**Bottom line.** $B$ is not an ad hoc family count. It is the distance-four nullhomotopy: the $\mu(S)$-weighted count over the canonical interval of $W'=-C_2\cup C_{-2}$ between its two psc splittings ($S^3$ and $L(4,1)$), projected onto an eigenspace of the $H^1(\,\cdot\,;\mathbb Z/2)$ end twist. Its third-map partner is $H$. The manuscript's Section 3 can be stated in about two pages, with three standard inputs and one new lemma. The standard inputs are triangle detection, the 4-step polygon relation, and the transgression $\mathrm{Hol}^*\leadsto\mu$. The new lemma is Lemma 4.2, the backtracking case of CDX's spherical cut. Its central-flat matching at $S^1\times S^2$ ($h^0=h^1=3$) is the one analytic point that is in neither DLME nor (to my recollection) CDX.

The framework does **not** improve the filtration problem. $B$ and $g_-g_+$ both shift the CS level by $+\tfrac18-\eta$, and the insertion responsible for this is forced. So this reorganises the ordinary layer; it does not replace the spin-coupled argument.
