# tri-orbifold-g: orbifold structures on K and on the surgery cores

Labels: PROVED, PLAUSIBLE, SPECULATIVE. Notation as in BRIEF. Code: `orbg-code/orbg.py`, output in `orbg.out`; these are tests, not proofs.

## Verdict

1. **The new triangle.** I give one new triangle, Δ₀, together with its two orbifold same-bundle twins (§a).
   - Upstairs, the slopes ±1 on (Σ₂(K), K̃) have exactly two common Farey neighbours, ∞ and 0.
   - CDX through ∞ descends to the known triangle (I)⊕(II).
   - CDX through 0 descends to Δ₀. Its side Y₂ → Y₋₂ is the exterior map E_{γ1}, of topological level exactly −1/16.
2. **Δ₀ fails (1), for every K.** Its third vertex is C(Y₀) ⊕ C^w(Y₀), and I^w(Y₀) ≅ I(Y₁) ≠ 0. Since E_{γ1} ≃ 0, the triangle splits. This is the structural reason the −1/16 map dies.
3. **Sharp negative (PROVED from the 4₁ data).** No map A₁ → B₀ of topological level −1/16 is injective at 4₁ if its cobordisms contain E_K×I compatibly, or cross it only along Seifert-type singular surfaces.
   - Such cobordisms cover every construction in directions (i)–(iii).
   - Requirement (2) cannot be met by such maps, so (1)+(2)+(3) cannot be met together.
   - Under the binding rules, a non-strict, uniform m₂ ≥ 1/16 is therefore out of reach. It would need a K-dependent flat connection or an energy bound (§f, §g).

## (a) The triangle Δ₀, and the four single-cone triangles at ±2

**Δ₀** (ε ∈ {0,1}):

  A_ε = C(Y₂,P_ε) --F--> B_{1−ε} = C(Y₋₂,P_{1−ε}) ----> M₀ = C(Y₀,P₀) ⊕ C(Y₀,w) ----> A_ε

- **F** = E_{γ1} + E_{γ1′}. This is the exterior E = W′∖νS with b⁺ = 0, odd at the L(4,1) end. It is the descent of the upstairs third map X_∞: Σ₁(K̃) → Σ₋₁(K̃). X_∞ has interior slope ∞, is negative definite, has an RP³ end, and double-covers E branched along S.
- **The other two maps** are the descents of Σ₋₁ → Σ₀^{⊕2} → Σ₁.
- **The connecting family** runs from B to A on the composite through Y₀.
- **Compare (I).** Its third map is c = −E, which has b⁺ = 1 and is the descent of X₀ (positive definite).

**Pillowcase classification (PROVED as plane geometry; `orbg.out` §5).** Resolve L₂^ε ∪ L₋₂^{ε′} at all of its crossings. The four possible cones are the only single-cone triangles at ±2:

| pairing | crossings (a, b) | smoothing | cone (pillowcase) | theory | side map Y₂↔Y₋₂ | level |
|---|---|---|---|---|---|---|
| mixed | (1/8, 3/4), (3/8, 1/4) | vertical | V_{1/4} ∪ edges | T ⊕ C(S³)²: triangle (I) | c = −E(γ1+γ1′), B→A | 3/16 |
| mixed | same | horizontal | H₀ ∪ H_{1/2} | Y₀ ⊕ Y₀^w: **Δ₀** | E(γ1+γ1′), A→B | **−1/16** |
| same | (0,0), (1/4,1/2), (1/2,0) | vertical | V_{1/8} ∪ V_{3/8} | (S³, K, cone π/2) | −E(γ0+θ), B→A | 1/8, 3/8 |
| same | same | horizontal | H_{1/4} ∪ H_{3/4} | (Y₀, K₀, cone π) | E(γ0+θ), A→B | 0, 0 |

Two of the orbifold vertices asked for in (i) are exactly the same-bundle cones: the cone angle π/2 on K, and the cone angle π on the core of Y₀.

## (b) Why Δ₀ should be exact (PLAUSIBLE, 50%)

- **Descent.** Δ₀ is the descent of CDX(−1, 0, 1) for (Σ₂(K), K̃). This needs two things:
  - CDX with a b₁ = 1 middle vertex Σ₀(K̃), with admissible w;
  - τ-equivariant transversality, with the same status as triangle-1's descent of #4.
- **Pillowcase.** At both mixed crossings, the horizontal resolution gives zigzags between b = 1/4 and b = 3/4. These are Hamiltonian-isotopic to H_{1/2} (Y₀ with w) and to H₀ (untwisted Y₀).
- **Rank test.** E_{γ1} ≃ 0 forces rk H(M₀) = rk A_ε + rk B_{1−ε}.
  - T(2,−3), ε = 0, uncorrected theory: Γ ∩ H_{1/2} is a = 1/6, 1/3, and Γ ∩ H₀ contains bd. The root endpoints a = 1/12, 5/12 are reducible bifurcations. This gives 3 = 2 + 1 ✓.
  - Corrected theory: every rank equals rk I(Y₁) = r, and I^w(Y₀) ≅ I(Y₁). This gives 2r = r + r ✓.

## (c) Injectivity: fails for every K (PROVED, given (b) and strategy-exact Prop. 4.1)

- F = E_{γ1} + ιE_{γ1}ι = ∂g^ns + ι∂g^ns ι, so F_* = 0.
- The third vertex contains I^w(Y₀) ≅ I(Y₁), which is nonzero by Floer and Kronheimer–Mrowka.
- **Direction (ii), PLAUSIBLE.** None of the four single cones is supported in the edge collars.
  - An edge-supported third vertex needs the iterated cone σ₀σ_{1/2}³, with four copies of S³.
  - Its quasi-isomorphism A_ε ≅ B_{1−ε} is a composite through Y₁, Y₀^w and Y₋₁, of level ≥ +1/8 (BRIEF).

## (d) Levels, term by term, with the orbifold corrections

The level formula is (i₀ + 3b⁺)/8 − s/8 − Σ(3 − h + ρ)/16. The ρ-values are from APS, and ρ(−∂νS) takes the values 0, −1, −2, −1.

- **E_{γ1}:**
  - (i₀ + 3b⁺)/8 = 0;
  - end term t(γ1, −∂νS) = (3 − 1 − 1)/16 = 1/16;
  - so the level is **−1/16 exactly**. E_{γ0} and E_θ have level 0.
- **Orbifold blow-down W′_orb = X′ ∪ B⁴/Z₄ (Kawasaki).** Let the isotropy act on ad by rotation 2πk/4. The cone point has defect
  δ_k = ¼ Σ_{j=1}^{3} χ_ad(g^j) · (−½)(1 − cot²(πj/4)) = −χ_ad(g²)/8.
  - δ₁ = +1/8 and δ₀ = δ₂ = −3/8.
  - s_orb = δ_k − δ₀ gives 1/2, 0, 0. This agrees with the APS route s_orb/8 = (i_cone + h)/8 + t, with i_cone = −dim ad^{Z₄}.
  - The rigid orbifold levels are therefore −1/16 (γ1) and 0 (γ0, θ).
  - Check on Z₂ (the ±1 case): s_orb = 1, giving level −1/8. That is DLME's RP³ face.
- **Cone angle π/2 along a surface** (Kawasaki equals KM at α = 1/8): s(l) = 2l + χ + F·F/8.
  - Cores: s = 2l + 3/4.
  - S: s = 2l + 3/2.
  - The family on (W′, S) has level −(2l + 5/2)/8, which is 7/16, 3/16, −1/16, −5/16 for l = −3, …, 0.
  - So **−1/16 appears only as the l = −1 sector**. The sectors l ≤ −2 cannot be excluded without an energy bound: the theory is non-monotone.
  - At cone angle π (α = 1/4), s = χ + F·F/2 = 0. This is monotone, with level −1/8.
- **Flat connections carried by F.** The exterior E is E_K-compatible. F is flat only at mixed common points, with gap 1/16 − i_{X′}/8. So it never joins different representations.

## (e) Pillowcase picture

- **Mixed pairings.** The crossings q₁, q₂ are resolved horizontally rather than vertically (which would give (I)). The zigzags average to b = ½ (Y₀ with w) and to b = 0 (untwisted Y₀, the reducible arc).
- **Same-bundle pairings.** The crossings at a ∈ {0, ¼, ½} resolve to V_{1/8} ∪ V_{3/8} (cone angle π/2 on K) or to H_{1/4} (cone angle π on the core of Y₀).
- **V_{1/8} ∪ V_{3/8}.** It passes through all four mixed points. So (L₂^w, V_{1/8}, L₋₂⁰) is concurrent at q′₁: a degenerate triangle with no area. The π/2 vertex cannot serve the mixed pairing.

## (f) Checks: the sharpness test fails, and fails for every E_K-compatible triangle

**Lemma 1 (flat pairing; PROVED).**
- *Data* (census-final §6, exact). 4₁ has σ = 0, so there is no ζ-correction, and d = 0 on A₁ and B₀ by the ranks.
  - A₁ = {bd₊ = (1,2,1): 1/5, (1,2,2): 3/10}.
  - B₀ = {z = (1,1,2): 11/80}.
- *Statement.* Suppose F: A₁ → B₀ counts only instantons whose topological level is ≤ −1/16. Then a nonzero coefficient ⟨F bd₊, z⟩ needs c-shift −1/16 = ℓ_top − E. So E = 0, and the instanton is flat.

**Lemma 2 (representation rigidity; PROVED).**
- (i) Suppose the flat part contains E_K × I compatibly with both ends. Then a flat connection restricts to the same representation of π₁(E_K) at both ends. This covers:
  - every surgery or CDX cobordism and every family on one;
  - orbifold or singular structures on K or on the cores, orbifold fillings, and orbifold vertices: (S³,K,π/2), (Y₀,K₀,π), Y_{±2} with cone cores;
  - lens and orbifold caps, and τ-quotients;
  - composites through vertices that are E_K-fillings.
- (ii) Suppose the singular locus crosses E_K × I in a level Seifert surface F. Then ρ₁ = ρ₀ on π₁(E_K∖F), and ρ₁(μ) = ρ₀(μ)g with g centralising ρ₀(π₁F).
  - If ρ₀ is binary dihedral and det K > 1, then π₁F → H₁(Σ₂) is onto, so ρ₀(π₁F) ⊄ {±1} and g ∈ U(1).
  - So ρ₁ is again binary dihedral, with a = ¼.

**Corollary (PROVED).**
- bd₊ is binary dihedral with a = ¼.
- z has a ≈ 0.322, so it is not binary dihedral, and z|E_K ≠ bd₊|E_K. Flat steps of type (i) keep the E_K-representation; type (ii) keeps binary-dihedral type.
- So every F of these types has F(bd₊) = 0, hence F_*[bd₊] = 0.
- **So no such map of topological level −1/16 is injective at 4₁. (2) is unrealisable within (i)–(iii), so (1)+(2)+(3) cannot hold together.**
- The same holds at T(2,−3) (bd → Q, with a = ¼ against ⅛), in the uncorrected theory. Caveat: the corrected theory's extra generator sits at ζ = (¼, 0), the pillowcase point of bd, and may move λ₁(Y₂). So 4₁ is the robust test.

**Tightness (PLAUSIBLE, 85%).** Consider an argument that uses only these maps, triangle relations, filtered algebra and E ≥ 0.
- If it attains m₂ = 1/16 at 4₁, every instanton on its critical chain from [bd₊] to [z] must be flat.
- At 4₁, A₁, T, B₀ and B₁ all have d = 0. A primitive of a nonzero differential elsewhere needs a bound on boundary depth, which is a position hypothesis.
- Flat steps keep bd₊, so the chain can never reach z.
- Hence such arguments give only m₂ > c at 4₁, with a topological c < 1/16.
- The "J-face / composite" escape b′∘a′, with E(b′) = 1/16, is an energy statement.

**Relation to prove.md.**
- Δ₀'s −1/16 map is E_{γ1} again (prove.md §2.1). The new information is why: E_{γ1} is the side of a split triangle whose third vertex, Y₀ ⊕ Y₀^w, never vanishes.
- Same-point rigidity is extended from "π₁ = π₁(X′)" to all E_K-compatible cobordisms and to Seifert-surface crossings.

**Direction (iii).**
- An R3 family (2 parameters, b⁺ = 1, γ1 end) has level (−2 + 3)/8 − 3/16 = −1/16 ✓.
- But to pass the test it must carry a flat bd₊ → z (Lemma 1). By Lemma 2 it then cannot be any of the cobordisms in (i)–(iii).
- At 4₁ it would need a flat SO(3) connection with restrictions (1,2,1) on Y₂ and (1,1,2) on Y₋₂ = −Y₂. These are representations of the (2,4,5) triangle group with different angles at the order-4 and order-5 fibres, and no automorphism of that group relates them.
- Numerically the equality is m₂(4₁) = (ρ(1,2,1) + ρ(1,1,2))/16 = (1/5 + 4/5)/16.

## (g) Hardest step and plausibility

| claim | status / plausibility |
|---|---|
| Δ₀ exists. Hardest step: descent of CDX through slope 0, with a b₁ = 1 middle vertex and equivariant transversality. | 50% |
| Δ₀ is useful for (1)–(3) | 0% (split) |
| Lemmas 1–2 | 95%; weakest point is whether the intended theory at 4₁ differs from the irreducible one (σ = 0, so it should not) |
| Tightness | 85% |
| Some K-uniform triangle meets (1)+(2)+(3) | < 3% |

The only exits:
- (α) an energy lower bound of type (D), η_g ≥ δ − 1/16 (Rule 1 forbids it);
- (β) a K-dependent cobordism carrying a flat (1,2,1) → (1,1,2) connection;
- (γ) dropping non-strictness at 4₁, i.e. accepting that the 4₁ equality is the identity ρ(1,2,1) + ρ(1,1,2) = 1 and not a topological level.

## Working log (kept for recovery)
- Steps 0–2: inputs read; BRIEF update absorbed (σ ≠ 0 twisted data are uncorrected, so 4₁ is the robust test).
- Step 3: `orbg.py` gives ρ(L(4,1)) = 0, 1, 2, 1. Kawasaki s_orb for Z₄ is 1/2, 0, 0, and for Z₂ it is 0, 1, both matching APS. The α = 1/8 sectors and the four smoothings are as tabulated above.
