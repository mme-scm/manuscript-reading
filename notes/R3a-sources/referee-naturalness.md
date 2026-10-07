# Naturalness report on `round3a/strategy-draft.tex`

The reader I have in mind is a gauge theorist who knows instanton Floer homology, Donaldson invariants and the Feehan–Leness papers, and who has seen nothing except this draft. Line numbers refer to `strategy-draft.tex`. Equation and theorem numbers refer to the compiled PDF (`build/strategy-draft.pdf`).

---

## 1. Verdict

Such a reader will recognise most of the individual steps:

- the contrapositive of [FL2b, Thm. 3.33(a)];
- Donaldson's jumping-line divisor, and bubbles forced onto spheres;
- the vanishing of the invariants of a connected sum;
- family maps obtained as the difference of two null-homotopies;
- a Nakayama-type argument giving $2$-local invertibility;
- the closing check that the argument proves nothing for $(HB)^M$.

Section 2 is natural. Theorem 2.1 is exactly the closed statement one would want, and the conic example of Remark 2.3 is well chosen.

The section does not yet read naturally, but the mathematics is not the reason. The problems are the order in which the story is told and the language around it.

1. **No opening paragraph.** The first paragraph promises "a contradiction of the following kind", but the contradiction is never stated in a single sentence, at the start or at the end.
2. **The energy language changes sign.** This language carries the main idea. Yet an increase of $\kappa$ is called a "supply" in Step 3 and in Section 2, and a "cost" in Step 5 (l.138).
3. **The decisive reason for families is deferred to Remark 2.4(b).** That reason is that in a closed manifold with $\Lambda$ constrained, the spheres gain nothing. Step 4 gives only the weaker reason, that the closed invariants vanish.
4. **$B$ is defined piecemeal**, across Steps 2, 3 and 4.
5. **One heuristic claim will strike an expert as wrong.** The draft says the $SO(3)$-monopole cobordism "performs the same selection" as Witten's formula. In fact it selects by $\langle c_1(\mathfrak s)-\Lambda,S\rangle$, not by $\langle c_1(\mathfrak s),S\rangle$, and the draft insists on $\Lambda\cdot S=2$.
6. **Vocabulary and labels.**
   - Several terms are invented, or borrowed from physics: "weight-two class", "selection rule", "meets/misses", "pinned", "cosmetic map", "family adjunction inequality".
   - Labels clash: in the PDF, "(1)" means both Step 1 and the inequality of Theorem 2.1.
7. **Length.** I compiled the Strategy alone with the default amsart layout, and it fills two full pages. The request was for one page; the 1.8 cm margins hide the overrun.

With the changes below, I believe an expert would follow the Strategy without effort and would see why one looks for this contradiction.

---

## 2. Is the contradiction motivated?

**What an expert will understand without help**

- **Step 1.** A nonzero Donaldson count forces the cut-down one-manifold of $SO(3)$-monopoles to reach a Seiberg–Witten stratum. This is a familiar contrapositive.
- **Step 2.** The chain of reasoning is clear: invertible modulo $2$, hence invertible over $\mathbb Z_{(2)}$, hence of finite order modulo $2^N$, hence the pairings are $\equiv q$. The remark that integrality is essential because of the factor $2^{n_D-1}$ is excellent and should stay.
- **Step 4, first half.** $X_M$ is a connected sum with $b^+>0$ on several summands, so the pairing has to be a count over a family.
- **The end of Step 6.** With $(HB)^M$ the exclusion must fail, since otherwise the argument would apply to every nontrivial knot. This is the best sentence in the section: it shows that the argument is calibrated.

**What is missing**

(a) **Context.** An instanton-homology expert will ask at once why the slopes are $\pm2$, and why a new idea is needed. One sentence answers both questions.
- By Ni–Wu, Hanselman and [DLME], $\pm2$ is the only remaining case.
- For $\pm1/n$, [DLME] get their contradiction from the Chern–Simons filtration of a family map over a negative-definite cobordism.
- In the remark on $\pm2$ surgery at the end of [DLME, §1.2], they explain that for $\pm2$ one variation gives a chain map that "behaves unfavorably with respect to the Chern–Simons filtration".
- If $B$ is that map (please check), say so. The reader then knows at once what the new idea replaces: the filtration gives way to an obstruction from $SO(3)$-monopoles.

(b) **The idea in one paragraph, before the details.** Proposed text in §11.1.

(c) **"Used in reverse" appears in the heading of Step 1 but never in its body.** The body should end: "We use this in reverse: a nonzero count forces the one-manifold to reach some Seiberg–Witten stratum. We shall produce a nonzero count in a situation where no stratum can be reached."

(d) **The contradiction itself.** Add at the end of Step 6: "For this $u$ and $M$ large, the family version of (1) gives $2^{n_D-1}\Omega(X_M)=0$, while (2) gives $\Omega(X_M)\not\equiv0\pmod{2^N}$." The proposed text is in §11.6.

(e) **Where the nontriviality of $K$ enters.** An expert always asks this. For the unknot, $Y_2$ and $Y_{-2}$ are both $\mathbb{RP}^3$, which has an orientation-reversing diffeomorphism, so the hypothesis of the Strategy holds; and Floer's $I(\mathbb{RP}^3)=0$. So presumably nontriviality enters only through the caps with $q\neq0$. One clause in Step 2 would settle the point.

That clause should also say where the caps come from. At l.70–71 "two caps" appear from nowhere, introduced by "Hence", which does not follow from what precedes it.

(f) **Status.** The Strategy should say in one sentence that the family version of Step 1 is not in the literature, and that Section 2 proves its closed model. At present this is said only in Remark 2.4 (l.356–360).

(g) **Two senses of "Seiberg–Witten class".**
- At l.45 ("determined by its Seiberg–Witten classes") it means basic classes.
- At l.58–60, l.103 and l.151 it means any $c_1(\mathfrak s)$ with $M_{\mathfrak s}\neq\emptyset$.

Theorem 2.1 needs the second sense, and the paragraph at l.209–214 makes a point of the difference. Define the term once: "by a Seiberg–Witten class we mean $c_1(\mathfrak s)$ for any $\mathfrak s$ whose perturbed moduli space $M_{\mathfrak s}$ is nonempty". Use "basic class" for the other sense.

---

## 3. Does each step follow from the previous one?

Mostly yes. The exceptions are all matters of order.

- **$B$ is defined in three places.**
  - Step 2 introduces $B$ "over an interval of metrics" and does not mention $\mu(S)$.
  - Step 3 says "$B$ carries $\mu(S)$".
  - Step 4 (l.116–119) finally says what $B$ is.

  Define $B$ once, in Step 2, together with $S$, $F_l$ and $F_r$ (proposed text in §11.2). Step 3 can then be about energy alone, and Step 4 about families alone.
- **The family parameter appears before the family.** Step 3 uses it at l.98–101 ("an insertion with its interval of metrics supplies only $\frac18$"), before Step 4 explains why there is a family. Either give the closed count first ($\frac14$ against $\frac12$) with $\frac18$ as a forward reference, or say in Step 2 that $B$ is defined over an interval.
- **The heading of Step 3 invites a question that Step 4 does not answer.** The heading says that a sphere costs more than it supplies. That is already true in a closed manifold ($\frac12>\frac14$). A careful reader will therefore ask at once why families are needed for anything beyond the vanishing of the closed invariants. The answer, which involves the Dirac index, should appear in Step 4 in two sentences rather than being deferred at l.119–121. Proposed text in §11.4.
- **A reference to something not yet introduced.** The second reason in Step 5 (l.129–131) refers to "the positive pieces introduced below", inside the same paragraph. Move it after $P$ has been introduced (l.135–138).
- **The shape of $u$ is never connected to Step 6.** Step 6 arrives at one positive piece for every four copies of $B$, but never says that this is the shape of $u=(\phi_*B)^3HB$. Step 2 introduced $u$ without explanation. Close the loop in both places:
  - in Step 2, add "(the exponent is explained in (6))";
  - in Step 6, add "which is the word $u$ of (2)".
- **Section 2 refers back to the Strategy as "(1) and (3)" (l.168).** In the PDF, "(1)" means the inequality of Theorem 2.1 four lines later (see §7).

---

## 4. Motivation asserted rather than explained

1. **l.45–46**, "Its mechanism gives a vanishing theorem that needs much less than the formula." Say what "much less" means.
   - The vanishing theorem is proved, and needs neither gluing at the reducibles nor the multiplicity conjecture.
   - Witten's formula is proved only modulo a gluing hypothesis.

   This contrast is what makes the approach credible to an expert. ("Its mechanism" also has no proper antecedent: a conjecture has no mechanism; the cobordism does.)
2. **l.63–64**, "Surgery exact triangles give integral maps that are isomorphisms with $\mathbb F_2$ coefficients."
   - Which triangles? Which third term vanishes, and why only with $\mathbb F_2$ coefficients?
   - Say which instanton homology $I$ is meant: Floer's, generated by irreducible flat connections, as in [DLME]. The equation $I(S^3)=0$ at l.117 fixes this only implicitly.
   - Also say what "a cobordism through $Y_0$" (l.67) is.
3. **l.68**, the exponent $3$ in $u$ (see §3).
4. **l.70–72**, the caps with $q\neq0$ (see §2(e)).
5. **l.96–97**, "Since $v\equiv w$ is even on $F_l$ and $F_r$". That $w$ is even on each half is a choice of bundle, and Section 1 never states it as one. Write "we take $w$ even on $F_l$ and $F_r$", and give the reason if there is one.
6. **l.115**, "The counts for single bundles are not invariant; the signed sum is." Give the reason here. The faces that stretch $L(4,1)$ carry ends, coming from the reducible of energy $\frac14$ on $\nu S$, which cancel only between $c$ and $c+\mathrm{PD}(S)$. This reason is already in Remark 2.4 (l.345–348).
7. **l.126–127**, "the sum over the bundles $c_e$ needs $n_D$ to be the same for all of them". Why?
   - Presumably the cancellation on the lens-space faces is between the $SO(3)$-monopole moduli spaces for $c_e$ and for $c_{e'}$. These must then have the same dimension $d_a+2n_D$. If so, say it.
   - $\Lambda_e$ is never defined. Write $\Lambda_e=\Lambda_0+\sum_ie_i\mathrm{PD}(S_i)$, or simply "changing $e_i$ changes $\Lambda^2$ by $2\Lambda\cdot S_i-4$".
8. **l.129–131**, "a chamber condition bounds $\Lambda$, because enlarging $\Lambda$ widens the band of Seiberg–Witten classes there". "Band" is opaque. Say which classes appear on $P$, and how that set depends on $\Lambda$.
9. **l.133–135**, "a chain of negative-definite pieces contributes at most $\frac12$ to $\Theta$". Where does $\frac12$ come from? The ends of the chain? One clause would do.
10. **l.139–142**, two bare assertions:
    - "They are confined by a family of toric metrics of nonnegative scalar curvature and by a square-zero sphere in $P$". Say what each does. For example, positive scalar curvature kills solutions in one chamber, and a sphere of square zero forces $\langle c_1(\mathfrak s),\cdot\rangle$ to vanish on it, as in the adjunction inequality.
    - "a class on $P$ can meet both adjacent spheres at a total cost of $\frac12$ instead of $1$". Say why. Presumably the positive direction of $P$ lets a class there recover part of what it spends on the two halves that lie in $P$.
11. **l.155–156**, "This requires the positive pieces to be at least four copies of $B$ apart." Asymptotic counts with $O(1)$ errors cannot produce the number four. Either give the local inequality on a segment containing one positive piece, or refer to the place where it is proved.

---

## 5. Unnatural wording and jargon, with replacements

### Step 1 (l.40–60)

- **l.37** "We explain why one should look for a contradiction of the following kind": no "kind" follows. See §11.1.
- **l.41–45** The first sentence packs the attribution, the scope and the caveat into a single relative clause. Replace by:
  > "Witten's conjecture [W] says that the Donaldson invariants of a closed four-manifold are determined by its Seiberg–Witten invariants. Feehan and Leness derive it for large classes of four-manifolds from the $SO(3)$-monopole cobordism of Pidstrigach and Tyurin, assuming a gluing theorem [PT, FLM, FL6]."

  Mention once that these are the "$PU(2)$ monopoles" of [FL1, FL2a, FL2b], since the bibliography uses that name.
- **l.45** "Its mechanism". Replace by "The cobordism also gives a vanishing theorem, which is proved and needs no gluing at the reducibles:".
- **l.46** "$w=c_1(E)$": $E$ is never introduced. Write "a spin$^u$ structure $\mathfrak t$, that is, a spin$^c$ structure twisted by a $U(2)$-bundle $E$; put $w=c_1(E)$, …".
- **l.47** "energy $\kappa$". Say once in what sense, for example "$\kappa=-\frac14p_1(\mathfrak t)$, the energy of the bundle (the Yang–Mills energy divided by $8\pi^2$)". See §6.
- **l.47–48**
  - "coupled Dirac index $n_D=\dots\ge1$" mixes a definition with a hypothesis. Write "…, and suppose $n_D\ge1$".
  - At first use, "the index of the Dirac operator coupled to an anti-self-dual connection" is clearer than "coupled Dirac index".
- **l.48–49** "The instantons are fixed by the circle action on the $SO(3)$-monopoles": "fixed by" can be read as "repaired by". Replace by:
  > "The circle acts by scalar multiplication on the spinor. Its fixed points are the anti-self-dual connections and the reducible monopoles, which are Seiberg–Witten monopoles."
- **l.49–50** "The link of an instanton is modelled on the projectivized kernel…". Replace by "The link of the instanton stratum is a bundle over $M^w_\kappa$ with fibre $\mathbb P(\ker D_A)\cong\mathbb{CP}^{n_D-1}$ over a generic $[A]$, …".
- **l.51–52, l.240** "weight-two class", "weight-two line": not a standard name. Use Feehan–Leness's notation: "the class $\mu_c$ (the first Chern class of the circle action, whose stabiliser is $\pm1$) restricts to twice the hyperplane class on each fibre".
- **l.52–53** "the instantons contribute $2^{n_D-1}D^w_X(z)$ ends to a one-manifold": introduce the one-manifold first.
  > "Cut the quotient by the circle down to a one-manifold by representatives of $z$ and of $\mu_c^{\,n_D-1}$. Its ends at the instanton stratum count $2^{n_D-1}D^w_X(z)$ [FL2b, Prop. 3.29]."
- **l.55–56** "the Feehan–Leness level". Replace by "its level, the number of instantons that have bubbled off". Feehan and Leness just say "level".
- **l.56** "If none of these is reached". Replace by "If the one-manifold reaches none of these strata".
- **l.57** "with no gluing at reducibles". Replace by "and the proof needs no gluing at the reducibles".
- **l.59** "the argument produces". Replace by "we shall produce".

### Step 2 (l.62–74)

- **l.63** "integral maps". Replace by "maps defined over $\mathbb Z$".
- **l.68** "lets them compose indefinitely". Replace by "lets us compose them indefinitely".
- **l.69** "$I(Y_2;\mathbb Z)/\mathrm{Tor}$": "Tor" can be misread as the functor. Write "$I(Y_2;\mathbb Z)$ modulo torsion, tensored with $\mathbb Z_{(2)}$".
- **l.70** "Hence the relative invariants $\Psi_\pm$ of two caps": "Hence" does not follow. Replace by:
  > "Let $Z_\pm$ be four-manifolds bounded by $\pm Y_2$ (…) whose relative invariants $\Psi_\pm$ satisfy $\langle\Psi_+,\Psi_-\rangle=q\neq0$. Then …"

### Step 3 (l.76–103)

- **l.78** "$F_l,F_r$ are orthogonal of square $-2$". Write "orthogonal classes of square $-2$", say what they are (the cores capped off by Seifert surfaces), and call them the halves of $S$ here, since "the halves" is used from l.133 on.
- **l.79** "$B$ carries Donaldson's class $\mu(S)$". Replace by "$B$ is cut down by $\mu(S)$", or better, move this into the definition of $B$ (§11.2).
- **l.80–81** "acts as a selection rule": physics language. Replace by:
  > "In Witten's formula, inserting $\mu(S)$ multiplies the contribution of each basic class $K$ by $\langle K,S\rangle$, so the classes orthogonal to $S$ drop out."
- **l.81–88** The display.
  - I would drop it. The sentence above is enough, and dropping it saves six lines toward the one-page target.
  - If it stays, note that the clause "because $e^{Q/2}$ has no multilinear terms in the $S_i$" hangs on "where $\mathbf D^w_X(z)=\dots$", so it reads as the reason for the definition. Split it:
    > "Here $\mathbf D^w_X(z)=D^w_X((1+\frac x2)z)$. The formula follows from Witten's on replacing $h$ by $h+\sum_it_iS_i$ and taking the coefficient of $t_1\cdots t_n$; since the $S_i$ are disjoint and orthogonal to $h$, the factor $e^{Q/2}$ contributes no such term."
- **l.89–90** "performs the same selection geometrically". This is inaccurate; see §9(a). Replace by "performs a selection of the same kind, by $\langle c_1(\mathfrak s)-\Lambda,S\rangle$ instead of $\langle c_1(\mathfrak s),S\rangle$".
- **l.90, l.232** "split class $v$". Replace by "the class $v=c_1(\mathfrak s)-\Lambda$ of the splitting". "Split" is used later for "split sphere", which is a different notion (§7).
- **l.94–95** "the insertion can be met only by a bubble at a point of $S$". Replace by "a limit can lie in $V_S$ only if one of its bubbles sits on $S$".
- **"Misses"**, at l.96 ("the number of spheres it misses"), l.207 ("every sphere that the stratum misses") and l.270 ("missed by $v$"). Replace by "the number of spheres orthogonal to $v$" and "every sphere orthogonal to $v$".
- **"Meet"**, at l.97 ("meeting $S$"), l.141 ("meet both adjacent spheres"), l.324–325 ("meets every insertion") and l.381 ("Both $\pm K$ meet $S_i$"). Replace by "pairs nontrivially with". "Meet" suggests a geometric intersection, but this is a pairing.
- **l.97–98** "meeting $S$ costs at least $\frac12$ in $-\frac14v^2$". Replace by "if $\langle v,S\rangle\neq0$, the span of the halves contributes at least $\frac12$ to $-\frac14v^2$".
- **l.99** "supplies only $\frac18$ of energy". Replace by "raises $\kappa$ by only $\frac18$" (§6).

### Step 4 (l.105–121)

- **l.110** "$\Omega(X_M)$": the count depends on the decomposition of $X_M$ along the necks, not on $X_M$ alone. $\Omega_M$ would not suggest an invariant of the manifold.
- **l.114** "the $2^n$ bundles $c_e$". Write "the $2^n$ bundles with $c_1=c_e$"; a class is not a bundle.
- **l.116** "The operation $\mu(S)\cdot[W']$". Replace by "The map of $W'$ cut down by $\mu(S)$".

### Step 5 (l.123–142)

- **l.124** "The relation of (1) exists only when $n_D\ge1$". Replace by:
  > "The argument of (1) needs $n_D\ge1$: otherwise the coupled Dirac operator has no kernel at a generic instanton, the instanton stratum has empty link, and the cobordism says nothing about it."
- **"pinned"** (l.126, l.348, l.380, l.387). Replace by "constrained". It is informal, and it is used as a heading in Remark 2.4.
- **l.133** "the halves carry no Dirac index". Replace by "the two negative directions spanned by the halves add nothing to $\Theta=\frac14(\Lambda^2-\sigma)$". Also define $\Theta$ before this sentence, not after it.
- **l.136** "obtained by filling the cobordism through $Y_0$ with the adjacent traces". Replace by "obtained by capping off the cobordism of $H$ with the traces $X_{-2}(K)$ and $-X_2(K)$". "Filling" has a specific meaning in contact topology.
- **l.138** "since $b^+=1$ costs $\frac38$ of energy". Replace by "since its positive direction raises $\kappa$ by $\frac38$" (§6).
- **l.139** "They are confined by". Replace by "They are controlled by", and see §4, item 10.

### Step 6 (l.144–164)

- **l.148–149** "plus the $\frac12$ saved on its neighbours". Replace by "plus the $\frac12$ by which it lowers the cost of the two neighbouring spheres".
- **l.152–153** "and one of them fails when $\frac mn$ stays outside": an overclaim; see §9(c).
- **"Abelian"**, at l.154 ("abelian configuration"), l.349 ("abelian components") and l.359 ("abelian zero-section components"). Replace by "reducible limit", "reducible components" and "reducible components with vanishing spinor".
- **"Cosmetic"**, at l.158 ("The cosmetic map") and l.332 ("The cosmetic argument"). On its own, "cosmetic" reads as "superficial". Replace by "The diffeomorphism $\phi$" and "The argument of Section 1".
- **l.159** "the only useful return $Y_{-2}\to Y_2$". Replace by "the only useful cobordism from $Y_{-2}$ back to $Y_2$".

### Section 2 (l.166 onward)

- **l.168** "has a closed form": "closed form" means an explicit formula. Replace by "can already be seen on a closed four-manifold".
- **l.168–169** "a cut-down version of [FL2b, Thm. 3.33(a)]" is ambiguous: a weaker version, or one with cutting down? "Do the excluding" is informal. Replace by "a version of [FL2b, Thm. 3.33(a)] in which the insertions $\mu(S_i)$ exclude the reducibles".
- **l.177** "$\mathfrak t$ has $w=c_1(E)$": $E$ again.
- **l.205–207** "Each also allows a stratum to reach the cut-down space only if a bubble sits on every sphere that the stratum misses". Replace by "Each also forces a bubble onto every sphere orthogonal to $v$ before the stratum can be reached; this gives the right side."
- **l.236, l.255** "free strata". Define them: "the strata on which the circle acts freely, that is, irreducible monopoles with nonzero spinor".
- **l.237** "a small equivariant perturbation": equivariant for what? A perturbation that depends only on $A$ is automatically invariant under the circle; say so.
- **l.244** $\mathcal V(z)$ and $\mathcal W$ are undefined. Add "where $\mathcal V(z)$ and $\mathcal W$ are the geometric representatives of $\mu_p(z)$ and $\mu_c$ of [FL2b]".
- **l.246** "intersection-suitable" is Feehan–Leness's term; a parenthetical gloss would help.
- **l.257** "satisfies $V_i$". Replace by "lies in $V_i$".
- **l.260–261** "a bubble absorbs conditions of codimension at most four". Replace by "the conditions that a single bubble can relieve have total codimension at most four".
- **l.264** "$w$ is good" sits beside "$w\not\equiv0\pmod 2$" in the theorem. Use one form, for example "$w\not\equiv0$, which for simply connected $X$ means that $w$ is good in the sense of [FL2b]".
- **l.306–308** "So the spheres must outnumber $b^+$ by the factor $\frac32$". Replace by "So it suffices that $n$ exceed $\frac32(1+b^+)$, up to the constant $c_\perp$". See §9(d).
- **l.324–325** "so every class meets every insertion". Replace by "so every $v$ pairs nontrivially with every $S_i$, and no bubble is forced".
- **l.337** "The bundle $\mathfrak t$". Replace by "The spin$^u$ structure $\mathfrak t$".
- **l.345** "limits whose cap is the reducible of energy $\frac14$". Replace by "limits whose restriction to $\nu S_i$ is the reducible of energy $\frac14$". At l.70, "cap" meant a four-manifold bounded by $Y_2$.
- **l.346** "the trace-zero flat connection". An expert will understand it, but "the flat connection on $L(4,1)$ whose holonomy has trace zero" costs only four words.
- **l.352** "family adjunction inequality". In families Seiberg–Witten theory (work of Baraglia and of Konno, for example), this name refers to adjunction inequalities for surfaces in families. Here it is an energy estimate generalising the proof of Corollary 2.2. Replace by "the family analogue of the estimate in the proof of Corollary 2.2".
- **l.358** "the cancellation of lens ends in the coupled problem". Replace by "the cancellation of the ends on the faces that stretch $L(4,1)$, for $SO(3)$-monopoles rather than instantons".
- **l.358–359** "abelian zero-section components sit next to free ones". Replace by "some components are reducible with vanishing spinor and others are irreducible".
- **l.364–365** "the 3-spheres $J_i$": $J_i$ is never used again. Drop it.
- **l.369** "with the same local data". Replace by "built from the same pieces".
- **l.386–389** The sentence beginning "In other words" is the hardest sentence in the draft. See §11.7.
- **l.401** "that the lens faces force". Replace by "that the faces stretching $L(4,1)$ force".
- **l.411–412** The [DLME] entry has no title. Add "Filtered instanton homology and cosmetic surgery".

---

## 6. The energy language

The heading of Step 3 promises an account of energy, and that account is the heart of the Strategy. It should be set up in one sentence and then used with a fixed sign. I propose:

> Regard $\kappa$ as the energy available. A Seiberg–Witten stratum with class $v$ spends $-\frac14v^2$ on its abelian connection and the remainder, $\ell=\kappa+\frac14v^2$, on bubbles. It can be reached only if it can afford the $T(v)$ bubbles that the insertions force.

With this convention the vocabulary is as follows:

- an insertion of degree two supplies $\frac14$, or $\frac18$ when it comes with a parameter;
- a positive direction of the intersection form supplies $\frac38$;
- a sphere costs every stratum at least $\frac12$;
- the Dirac index $n_D=\Theta-\kappa$ loses whatever is supplied.

Line 138 should then read "its positive direction supplies $\frac38$, which the Dirac index loses". This agrees with l.306–308 and with l.148 ("its energy $\frac38$").

Two further sentences would make Steps 5 and 6 read as consequences rather than as a list of numbers.

1. Since $n_D=\Theta-\kappa$, whatever raises $\kappa$ helps the strata and hurts the Dirac index at the same time. This one observation is why the balance in Step 6 is delicate.
2. The heading "costs more energy than it supplies" is true in a closed manifold too ($\frac12$ against $\frac14$). Say so in Step 3, so that the reader is not puzzled by Step 4.

---

## 7. Labels and notation

1. **The "(1)" clash.**
   - In the PDF, the inequality of Theorem 2.1 is numbered (1). That is how "(1)" reads at l.202, in Corollary 2.2 and in proof step (v) ("contradicting (1)").
   - Line 168, however, uses "(1)" and "(3)" for Steps 1 and 3 of the Strategy.

   Add `\numberwithin{equation}{section}` (the comment block already calls the inequality (2.1)), and refer to the Strategy points as "Step 1", …, or as §1.1–§1.6.
2. **"(a)" and "(b)" are used twice.** They label the properties of $V_i$ in step (i) of the proof, cited as "By (a)" in (iv) and (v). They also label the two reasons in Remark 2.4, cited as "Remark 2.4(b)" after Corollary 2.2. Rename one pair; for example, state the properties of $V_i$ as a lemma.
3. **The halves have two names:** $F_l,F_r$ in Section 1 and $F_i^{\pm}$ in Corollary 2.2. Use one notation.
4. **$n_D$ sits next to Feehan–Leness's $d_a$.** FL2b, whose statements are cited, write $n_a$ for the Dirac index. Either use $n_a$, or avoid $d_a$ and write $\dim M^w_\kappa$; the mixture looks accidental.
5. **"Split" has two meanings:** the "split class" of a reducible (l.90, l.232) and a "split sphere" (the heading at l.313, and l.397). Keep "split sphere", define it at Corollary 2.2, and drop "split class".
6. **"Cap" has two meanings:** the caps of $Y_2$ (l.70, l.113) and the piece $\nu S_i$ (l.345).
7. **Undefined and unused symbols.** $\Lambda_e$ (l.128), $\mathcal V(z)$ and $\mathcal W$ (l.244) are undefined. $J_i$ (l.365) is defined and never used.
8. **Inconsistent reference style.** The italic paragraph headings "1." to "6." are cited as "(1)" to "(6)". Use the same form for both.

---

## 8. Section 2 (closed prototype)

**What works**

- The prototype is natural and well chosen, and Theorem 2.1 is the statement an expert would formulate.
- The key observation is explained cleanly in steps (i) and (v). The jumping-line divisor is closed under $C^0$ convergence away from bubbles, and it misses reducibles of degree zero. Hence a bubble must sit on every sphere orthogonal to $v$.
- The paragraph after the theorem ("The insertions enter (2.1) on both sides") is exactly the right gloss.
- Remark 2.3 is good, and "A conic occupies one negative direction, not two orthogonal halves" is the right summary.

**What to add or change**

- **Say at the start of Section 2 what the prototype is for, and what it is not for.** It isolates the mechanism. It cannot by itself give the contradiction, and Remark 2.4(b) shows that on a closed manifold with $\Lambda$ constrained it cannot be combined with $n_D\ge1$. A reader who is not told this will look for the application and be disappointed.
- **Give the natural precedents for the cancellation along $L(4,1)$.** An expert will think at once of:
  - Ruberman's relation for spheres of square $-2$, and Fintushel–Stern's for spheres of square $-3$ ([FS, Thms. 2.1, 2.4]). Both are proved by splitting along $\partial\nu S=L(p,-1)$ and analysing reducibles on $\nu S$.
  - The Fintushel–Stern rational blow-down of a $(-4)$-sphere, whose boundary is $L(4,1)$.

  One sentence citing these would anchor Step 4 and the second bullet of the dictionary in Remark 2.4.
- **Corollary 2.2: control of $c_\perp$.** A reader will ask how $c_\perp$ is controlled. Otherwise the corollary looks as hard to verify as (2.1) itself; FKLM §3 makes exactly this complaint about conditions involving all nonempty moduli spaces. Add one sentence: $c_\perp$ is finite because only finitely many $\mathfrak s$ have $M_{\mathfrak s}(g)\neq\emptyset$, and say what it depends on.
- **After Corollary 2.2**, the paragraph should say "it suffices", not "must" (§9(d)).
- **Remark 2.4(b): give the identity a conceptual sentence.** The identity is the conceptual heart of the remark.
  - Basic classes come in pairs $\pm K$, by the conjugation $\mathfrak s\mapsto\bar{\mathfrak s}$, and the $SO(3)$-monopole picture breaks this symmetry through $\Lambda$.
  - The quantity $\ell(K)+\ell(-K)-2n_D=4\kappa+\frac12(K^2+\sigma)$ does not involve $\Lambda$ at all. So no choice of $\Lambda$ lowers the levels of both $K$ and $-K$ without lowering $2n_D$ by as much.
  - Adding a sphere with its two halves changes this quantity by $4s-1$: by $0$ in a closed manifold and by $-\frac12$ in a family.

  That is the reason a family is forced, stated without bookkeeping. Proposed text in §11.7.
- **l.209–214.** The multiplicity conjecture originates as [FKLM, Conj. 3.1]; FL2b cites it that way. FL2b also says it is known at level one, by Feehan and Leness's level-one paper. Cite accordingly.
- **The LaTeX comment block (l.446–481)** refers to drafts and internal files. Delete it before circulating the source.

---

## 9. Points that also bear on correctness (for the correctness referee)

(a) **l.88–90, "performs the same selection geometrically".**
- By [FL2b, Cor. 4.7] (I checked the source), $\mu_p(h)$ restricts to the link of the reducible $\mathfrak s$ as $\frac12\langle c_1(\mathfrak s)-c_1(\mathfrak t),h\rangle(2\mu_{\mathfrak s}(x)+\nu)$. So the geometric selection is by $\langle c_1(\mathfrak s)-\Lambda,S\rangle$, whereas Witten's formula selects by $\langle c_1(\mathfrak s),S\rangle$.
- The two agree when $\Lambda\cdot S=0$. With the draft's $\Lambda\cdot S=2$ they disagree. For example, a class orthogonal to $S$ is killed by the formula but not by the divisor.
- Remark 2.4(b) actually relies on this difference.

(b) **l.224–226, "the canonical section of the determinant line bundle of $\bar\partial$ on $S_i$".**
- On $E|_{S_i}\otimes(\det E|_{S_i})^{-1/2}$, which has rank two and degree zero, $\bar\partial$ has index $2$, so there is no canonical section.
- One needs the twist by $\mathcal O(-1)=K^{1/2}$, which gives index $0$; that is, the Dirac operator on $S_i$ coupled to $A$, as in Donaldson's construction.
- That operator is invertible exactly when $E|_{S_i}\cong\mathcal O\oplus\mathcal O$, which is what property (b) uses.

(c) **l.150–153, "one of them fails when $\frac mn$ stays outside $[\frac15,\frac37]$".** Only an upper bound for $\ell-T(v)$ is available. Outside the window the count no longer guarantees exclusion, but it does not show that exclusion fails. Say "the count no longer guarantees one of them".

(d) **l.306–308, "the spheres must outnumber $b^+$ by the factor $\frac32$".** The corollary gives a sufficient condition, and the relevant quantity is $1+b^+$.

(e) **l.155–157.** The number four cannot follow from the asymptotic counts quoted.

(f) **l.96–97.** Section 1 uses the evenness of $w$ on each half without ever imposing it.

(g) **l.382–386, "At fixed $n_D$".** Say how $n_D$ is held fixed: by changing $\Lambda$ elsewhere, with $\kappa$, $K$ and $\sigma$ otherwise unchanged. Without that, the value $4s-1$ cannot be checked. I checked it: without restoring $n_D$, adding a sphere with its halves changes $\ell(K)+\ell(-K)$ by $2s-1$ and $n_D$ by $-s$; restoring $n_D$ through $\Lambda$ gives $4s-1$.

(h) **The equation-number clash (§7.1)** lets "contradicting (1)" in step (v) be read as a reference to Step 1.

**What I verified.** By hand and by exact arithmetic, I checked:
- the identity of Remark 2.4(b) and its equivalent form;
- the window $(\frac15,\frac37)$, and that the closed window is empty ($\frac25>\frac27$);
- the algebra in the proof of Corollary 2.2;
- the index count in (b).

I also checked these citations against the sources: [FL2b, Prop. 3.29, Thm. 3.33(a), Conj. 3.34, Cor. 4.7], [FL6, (1.2)], and [FS, Lemma 2.3(6)], which is Kotschick's relation.

---

## 10. Length

**Measurements.** I compiled the Strategy alone with the default amsart layout, and it fills two full pages. At the draft's 1.8 cm margins it is 1.3 pages.

**Cuts that reach about one page at the draft's margins**, even with the opening of §11.1 added:

1. Replace the display in Step 3 by one sentence.
2. Shorten the attribution sentence in Step 1.
3. Define $B$ once, in Step 2. This removes l.116–119.
4. Reduce the $\Lambda_e^2$ formula and the description of the Seiberg–Witten classes of $P$ (l.138–142) to one sentence each, and move the details to the body.

**Standard margins.** A genuinely one-page Strategy at standard margins would also need Step 6 compressed into a small table:
- rows: a copy of $B$; a positive piece; an insertion in a closed manifold;
- columns: change in $n_D$; change in the bound for $\ell-T(v)$;
- the two windows written under the table.

---

## 11. Proposed replacement passages

### 11.1 Opening (replaces l.35–38)

```latex
Let $K\subset S^3$ be a nontrivial knot, write $Y_r=S^3_r(K)$, and suppose that
$\phi\colon Y_{-2}\to Y_2$ is an orientation-preserving diffeomorphism. By the
work of Ni--Wu, Hanselman and Daemi--Lidman--Miller Eismeier \cite{DLME}, this
is the only case of the cosmetic surgery conjecture that remains open. For the
slopes $\pm1/n$, \cite{DLME} obtain a contradiction from the Chern--Simons
filtration of a family map over a negative-definite cobordism; for $\pm2$ the
analogous map $B$ below exists, but the filtration argument does not apply to
it [check against the end of DLME, \S1.2]. We replace the filtration by an
obstruction coming from $\SO(3)$-monopoles. The idea is this. The
diffeomorphism $\phi$ lets us compose the maps between $I(Y_2)$ and $I(Y_{-2})$
given by surgery exact triangles as often as we like, and since these maps are
isomorphisms modulo two, the resulting pairings never vanish. Each passage from
$Y_2$ to $Y_{-2}$ through $B$ adds an embedded sphere of square $-4$, together
with an insertion of its class $\mu$. By the $\SO(3)$-monopole cobordism, a
nonzero instanton count must be supported by a Seiberg--Witten stratum, and
each such insertion takes more energy from every Seiberg--Witten stratum than
it adds to the moduli space. With enough spheres no stratum can support the
count; this is the contradiction. The points below explain each step, why the
argument has to be carried out over families of metrics, why it then needs
pieces with $b^+>0$, and how these requirements are balanced.
```

Ni–Wu and Hanselman should be added to the bibliography.

### 11.2 Definition of $B$ (replaces the second sentence of Step 2, l.64–66, and absorbs l.77–79 and l.116–119)

```latex
One is the map $B\colon I(Y_2)\to I(Y_{-2})$ of the negative-definite cobordism
$W'=(-X_2(K))\cup_{S^3}X_{-2}(K)$. The cores of its two $2$-handles form a
sphere $S$ with $[S]=F_l-F_r$, where the halves $F_l$ and $F_r$ (the cores
capped off by a Seifert surface) are orthogonal classes of square $-2$; thus
$S\cdot S=-4$ and $\partial\nu S=L(4,1)$. The map of $W'$ cut down by $\mu(S)$
is null-homotopic in two ways: by stretching the neck $S^3$, since
$I(S^3)=0$, and by stretching $L(4,1)$, where the contributions of the bundles
$c$ and $c+\PD(S)$ cancel. The map $B$ is the difference of these two
null-homotopies, that is, the count over the interval of metrics joining the
two stretched metrics, summed over the two bundles. It is a distance-four
analogue of the map $g_1$ of \cite{DLME}.
```

### 11.3 Step 3 (replaces l.79–103)

```latex
\point{3. An insertion costs more energy than it supplies.}
Regard $\kappa$ as the energy available. A Seiberg--Witten stratum with class
$v$ spends $-\frac14v^2$ on its abelian connection and the remainder
$\ell=\kappa+\frac14v^2$ on bubbles. Since the instanton moduli space has
dimension $8\kappa-3(1+b^+)$, an insertion of $\mu(S)$, of degree two, raises
$\kappa$ by $\frac14$; when it comes with a one-parameter family of metrics,
as in $B$, the parameter provides one of the two dimensions and $\kappa$ rises
by only $\frac18$. On the other hand every stratum must spend at least
$\frac12$ on the insertion. Represent $\mu(S)$ by Donaldson's divisor
$V_S=\{[A]:E_A|_S\not\cong\mathcal O\oplus\mathcal O\}$ of connections whose
restriction to $S$ is a jumping line. A reducible with class $v$ lies in $V_S$
exactly when $\langle v,S\rangle\neq0$. In that case one of $\langle
v,F_l\rangle$, $\langle v,F_r\rangle$ is a nonzero even number (we take $w$
even on both halves, and $v\equiv w$), so the span of the halves contributes at
least $\frac12$ to $-\frac14v^2$. If $\langle v,S\rangle=0$, a limit can lie in
$V_S$ only if one of its bubbles sits on $S$, which raises by one the level the
stratum needs. Thus a stratum can be reached only if $\ell\ge T(v)$, the number
of spheres orthogonal to $v$, and each sphere lowers $\ell-T(v)$ by at least
$\frac12-\frac18=\frac38$, whatever $v$ is; enough spheres put every stratum out
of reach. (Without the parameter the sphere still costs more than it supplies,
$\frac12$ against $\frac14$; why this is not enough is explained in (4).) This
is the geometric counterpart of the fact that in Witten's formula $\mu(S)$
multiplies the contribution of a basic class $K$ by $\langle K,S\rangle$; the
difference is that the $\SO(3)$-monopoles see $\langle K-\Lambda,S\rangle$.
```

### 11.4 End of Step 4 (replaces l.119–121)

```latex
The family has a second effect, and it is the decisive one: the parameter
lowers the energy that an insertion supplies from $\frac14$ to $\frac18$, while
the energy it costs every stratum is unchanged. In a closed manifold with
$\Lambda$ constrained as in (5), a sphere lowers the levels of a pair of
classes $\pm K$ only by as much as it lowers twice the Dirac index, so the
spheres gain nothing (Remark~\ref{rem:family}(b)); in a family each sphere gains
$\frac12$.
```

### 11.5 Beginning of Step 5 (replaces l.124–135)

```latex
\point{5. Why $b^+$.}
The argument of (1) needs $n_D\ge1$: otherwise the coupled Dirac operator has
no kernel at a generic instanton, the instanton stratum has empty link, and the
cobordism says nothing about it. Feehan and Leness obtain $n_D\ge1$ by taking
$\Lambda$ large \cite[Thm.~1]{FLM}, \cite{FL6}. Here $\Lambda$ is constrained.
The ends on the faces that stretch $L(4,1)$ cancel between the
$\SO(3)$-monopole moduli spaces of $c_e$ and of the bundle obtained by changing
$e_i$, so these moduli spaces must have the same dimension, hence the same
$n_D$. Changing $e_i$ changes $\Lambda^2$ by $2\Lambda\cdot S_i-4$, so
$\Lambda\cdot S_i=2$. Since $\Lambda\cdot F_l$ and $\Lambda\cdot F_r$ are even
with difference $2$, one of them is nonzero, and the two negative directions
spanned by the halves add nothing to $\Theta=\frac14(\Lambda^2-\sigma)$. A chain
of negative-definite pieces therefore contributes at most $\frac12$ to $\Theta$,
however long it is, and the Dirac index must come from $b^+$.
```

The reason given here for requiring the same $n_D$ (cancellation between moduli spaces of equal dimension) is my reading; please check it before adopting the sentence. The second reason, the chamber condition on $P$, then follows the introduction of $P$, in the words asked for in §4, item 8.

### 11.6 End of Step 6 (replaces l.155–158 and adds the conclusion)

```latex
\dots together with $\frac mn>\frac15$ it leaves one positive piece for every
four copies of $B$, which is the shape of $u=(\phi_*B)^3HB$ in (2). The
diffeomorphism $\phi$ is what permits so sparse an arrangement. [\dots as in the
draft, through ``for every nontrivial knot''.] For $u$ as in (2) and $M$ large,
the family version of (1) gives $2^{n_D-1}\Omega(X_M)=0$, while (2) gives
$\Omega(X_M)\not\equiv0\pmod{2^N}$; this is the contradiction.
```

### 11.7 Remark 2.4(b), first bullet (replaces l.380–389)

```latex
\item \emph{$\Lambda$ constrained.} Basic classes come in pairs $\pm K$, and
the $\SO(3)$-monopole equations break this symmetry through $\Lambda$. The
first identity says that
$\ell(K)+\ell(-K)-2n_D=4\kappa+\frac12(K^2+\sigma)$ does not involve
$\Lambda$: no choice of $\Lambda$ lowers the levels of both $K$ and $-K$
without lowering $2n_D$ by as much. Take $\Lambda\cdot S_i=2$ and $K$
orthogonal to the halves of $S_i$. Then $\langle\pm K-\Lambda,S_i\rangle=-2$,
so neither $K$ nor $-K$ needs a bubble on $S_i$, and adding $S_i$ with its two
negative directions leaves $T(\pm K)$ unchanged. It changes
$4\kappa+\frac12(K^2+\sigma)$ by $4s-1$, where $s$ is the increase of $\kappa$
caused by the insertion: by $0$ in a closed manifold ($s=\frac14$), and by
$-\frac12$ in a family ($s=\frac18$). So in a closed manifold the sphere lowers
the levels of $\pm K$ only at the price of the same amount of Dirac index; the
parameter is what breaks this. With the pieces of (5)--(6) and no parameters,
$n_D=\frac18(5m-2n)+O(1)$ and $\ell-T(v)\le\frac18(7m-2n)+O(1)$, which would
need $\frac25<\frac mn<\frac27$, an empty range, against
$\frac15<\frac mn<\frac37$ in the family.
```
