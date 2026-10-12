# Branched double cover angle: one new triangle, and why this angle cannot meet (1)+(2)

**Verdict.** The answer is negative, and the negative is sharp.

The cover yields exactly one triangle that is not among the four known ones and whose third vertex vanishes structurally: Δ_F, the cover branched along the capped Seifert surfaces. Its level is (4g−3)/8 ≥ +1/8, and the rank data force it to be same-bundle. Four obstructions (O1–O4) show that no modification of the double cover can meet requirements (1) and (2) together:
- an anti-invariant part,
- a twisted local system,
- another lift of τ,
- the χ-twisted ρ.

§(g) states what a viable triangle must do instead.

Labels: PROVED, COMPUTED, PLAUSIBLE, SPECULATIVE.

## (a) The triangle Δ_F (new)

- Write W′ = W_l ∪_J W_r, with W_l = −X_2°, W_r = X_{−2}° and J = S³ the connected-sum sphere.
- Let F_l ⊂ int W_l and F_r ⊂ int W_r be the capped Seifert surfaces (core ∪ pushed-in Seifert surface, genus g) **chosen disjoint from J**.
- Put F = F_l ⊔ F_r.
- **Vertices:** (Y_2, P_i); C(J) = C(S³) = 0; (Y_{−2}, P_j).
- **Maps:**
  - the singular 2-handle maps (W_l, F_l) and (W_r, F_r), at holonomy 1/4 along the *closed* surfaces;
  - the third map: the exterior of νS with F∩E singular, at the L(4,1) end;
  - the connecting map: the one-parameter family on (W′, F), between the J-broken and the ∂νS-broken metrics.
- **Cover picture (PROVED, topology).**
  - The classes F_l, F_r map to (−2,0) and (0,−2) in H_2(W′,∂W′) = H²(W′). So W′ has a double cover branched along F.
  - The meridian of F_l is μ, so the cover restricts to the connected covers Ỹ_± = Σ_{±1}(K̃) on the ends.
  - Since F ∩ J = ∅, the cover restricts to the **trivial** cover on J: J̃ = S³ ⊔ S³. This is DLME's shape, with Σ⊕Σ replaced by S³⊕S³.
  - Price: χ(W̃) = 4g and σ(W̃) = −2, so b⁺(W̃) = 2g−1. The cover W̃ is not a DLME configuration.

## (b) Why it should be exact (SPECULATIVE)

- **J-face: empty** (PROVED dimension count). F avoids J, only θ is flat on J, and h⁰ = 3.
- **∂νS-face:** F_l·S = −2, so the caps on νS are singular along fibre discs. Their uniqueness and the cancellation between the lifts c and c+PD(S) are not established.
- By KM's reduction of monotone (holonomy-1/4) invariants of closed surfaces to μ(F)-insertions, Δ_F should be a decorated form of the divisor triangle (#3).
- Consistency check (PROVED arithmetic): at g = 1 its level is +1/8, which is B's level.

## (c) Why the third vertex vanishes

- Irreducible C(S³) = 0 for **every** K (PROVED).
- That is exactly the problem; see O1.

## (d) Level (PROVED bookkeeping, KM's term s = χ + F·F/2)

- s(F) = 2(2−2g) − 2 = 2 − 4g.
- Level = (i₀ − s)/8 = (4g−3)/8:
  - g = 1: +1/8;
  - g = 2 (the open Δ_K = 1 case): **+5/8**.
- **Flat connections.** A flat singular connection has meridian of F of order two in SO(3). So it sits at a = 1/4 on Y_{±2}, the points (1/4, 0) and (1/4, 1/2). Thom genericity excludes these for Δ = 1. The map is therefore strict and never flat.
- **Lemma T (trade-off; PROVED as bookkeeping).** Let F ⊂ W′ be closed and connected, with [F] = aF_l + bF_r.
  - (i) The branched cover gives Ỹ_± on the ends iff a and b are odd. Then F·F = −2(a²+b²) ≡ −4 (mod 16) and s(F) = χ(F) − (a²+b²) is **even** and ≤ 0.
  - (ii) The one-parameter family on (W′, F) has level (−1−s)/8 ∈ −1/8 + ¼ℤ_{≥0}. This contains **no sixteenths**. The level is −1/8 iff F is a sphere in class ±F_l ± F_r.
  - (iii) Such a sphere meets J in a link L whose sides are planar surfaces in the core classes. The middle term is then the traceless theory of (S³, L) downstairs, or C(Σ₂(L)) upstairs.
    - It vanishes structurally only if π₁(S³∖L) is abelian, i.e. L is the unknot or the Hopf link.
    - L = unknot ⟺ K is 2-shake-slice, and then Y_2 is homology cobordant to L(2,1).
    - L = Hopf needs a core-class disc system, for example from unknotting number one. Its reducible has h⁰ = 1, so the J-face is not automatically empty.
    - **Both are K-dependent.**
    - F = S is the case L = K, which is the known triangle #4.
- So, in the double-cover world, a structurally vanishing middle and level ≤ −1/8 exclude each other. An odd sixteenth can enter only through a lens end, the ρ(γ₁) term.

## (e) Pillowcase

- **Where Γ_K lies.** For every K, Γ_K lies in the band [δ, ½−δ] × S¹_b; irreducibles never reach a ∈ {0, ½}. For Δ_K = 1 it is a closed multicurve that also misses the reducible arc.
- **The structurally missed set is the two edge collars, and nothing else.**
- **Edge half-twists.**
  - σ_{1/2}(a,b) = (a, b+a) sends L_N to L_{N−1}. It is the half-twist at the a = ½ edge.
  - σ_0 = σ_{1/2}∘(b ↦ b−½) sends L_N to L_{N−1}^w.
  - Hence L_{−2}^{ε′} = σ_0^i σ_{1/2}^{4−i} L_2^ε with **i ≡ ε+ε′ (mod 2)**. Mixed bundles ⟺ an odd number of half-twists at each edge.
  - Each half-twist is a Floer step through S³ = 0. Merged pairs are DLME's g₁ (σ_0², middle C(S³)², gain −1/8) and B ≃ g₋ϑg₊ (net +1/8).
  - So every structurally vanishing route is an edge route. These are the known triangles #1–#3.
- **Cover (PROVED arithmetic).** The cover acts by (a,b) ↦ (2a, b) and by (2a+½, b).
  - It sends **V_{1/4} onto the upstairs edges**. Upstairs, Γ meets the edges exactly at the traceless points, which are nonempty by KM.
  - **The upstairs structurally missed set is therefore empty.**
  - V_{1/8} ∪ V_{3/8}, which carries the mixed points Q, maps to the upstairs traceless circle. The one-copy traceless triangle at ±1 fails the rank test (triangle-1 §2.4).

## (f) Checks, and the obstructions

**O1 (ranks; COMPUTED data, triangle-1 §4.6; perfect complexes).** For T(3,5), which has det = 1, the SU(2) ranks are:

| | P0 | P1 |
|---|---|---|
| Y_2 | 16 | 12 |
| Y_{−2} | 16 | 20 |

- A quasi-isomorphism (Y_2, P_i) → (Y_{−2}, P_j) exists only for (i, j) = (0, 0). The mixed pairings (16 vs 20, 12 vs 16) and the both-bundle sum (28 vs 36) are all ruled out.
- Hence any triangle whose third vertex vanishes for all K, or for all det-1 K, is exact **only P0→P0**. That is same-bundle, which is useless by (3). This applies to Δ_F, and B is consistent with it.
- T(3,5) has everything the double cover sees: Σ = Σ(2,3,5) is a homology sphere, χ acts freely, there are no binary dihedral representations, and the τ-isotropy types are the same.
- **So no cover-based vanishing can give a mixed or both-bundle triangle.** A vanishing statement must use Δ_K = 1 at every holonomy α, i.e. no roots of Δ_K on the unit circle. The cover sees only α = ¼, that is, det K.

**O1′ (PLAUSIBLE; consistent with data).** If Γ_K is closed, the SU(2) ranks agree in all four pairings.
- Mechanism: take a holonomy perturbation f along the dual knot of Y_{−2}, with f′(a) = −4a + k on the band (k ∈ ℤ for the same bundle, k ∈ ½+ℤ for mixed). It makes L_{−2}^{ε′} equal to L_2^ε on the band. No generator bifurcates from a reducible, so the continuation map is a quasi-isomorphism.
- Data: 4_1 gives SU(2) counts 2 = 2 in both (I) and (II); T(3,5) fails, as it should. So for Δ = 1 ranks are not an obstruction.
- But the level of this continuation map is a Hofer oscillation of f, about ½ across the band. It gives only windows, as in slope2.tex.

**O2 (flat support; PROVED bookkeeping given transversality of Γ_K to both lines at P; COMPUTED values).**
- Suppose a cobordism contains E_K × I compatibly with both ends. Every ledger map does, and so does every descent of a τ-equivariant cobordism, since (Σ∖νK̃) × I descends to E_K × I.
- Then a flat connection on it pairs a common point with itself. The gap there is 1/8 (same bundle) or 3/16 (mixed); this is 1/16 − ind_E/8 with ind_E = −1.
- So its topological level, when flats are supported, is −1/8 or −3/16, **never −1/16**.
- The T(2,−3) equality pairs two *different* points of Γ: (¼, 0) on Y_2^w and (⅛, ¼) on Y_{−2}. In the data, its 1/16 is −3/16 (flat exterior plus the 1/16 cap) plus the absorption depth δ = 1/8.
- So a mixed map of level exactly −1/16 that supports flats needs a cobordism whose π₁ decouples the two copies of π₁(E_K). That lies outside every cover construction.

**O3 (sixteenths).** By Lemma T, all cover-compatible singular surfaces have even s. The level-−1/16 options in the ledger are:
- (b⁺, i₀, end) = (0, 0, γ₁ on −∂νS): this is E_{γ₁}, which is null-homotopic, and its flats have index −1;
- (1, −2, γ₁ on +∂νS): the pentagon h, which maps a vertex to itself.

**O4 (the other variants; PLAUSIBLE).**
- **τ-eigenspaces.** They need equivariant transversality. The (−1)-part has nonzero Euler characteristic in general, and is empty for torus knots.
- **Local systems.** Σ is a homology sphere, and meridional systems give the singular theory (Σ, K̃, α), which Γ meets.
- **Other lifts of τ.** These are exactly the two isotropy types along S̃. The O(2) wall forces both to appear, which brings back C(S³) ⊕ T(K).
- **Tate / χ-localisation.** χ is free on all three vertices when det = 1, so everything becomes 0.
- **c̃/2 = c + δ/16.** An upstairs-counted invariant instanton has (i⁺, i⁻) with i⁺ + i⁻ = −1. It shifts c̃/2 by −1/16 − E uniformly, but shifts c by i⁺/8 − E. So upstairs g₁ is a mixture of downstairs families of different dimensions, and it controls ℓ̃, not λ_i.

## (g) The hardest step, plausibility, and what a viable triangle must do

- **Δ_F.**
  - Exactness: 40%. The hardest step is the ∂νS-face with F_l·S = −2.
  - Usefulness: about 0%. It is same-bundle by O1, with level ≥ +1/8.
- **The negative.** Confidence 85% that no branched-double-cover modification meets (1)+(2).
  - The weakest link is O2's transversality value 3/16 at mixed points for non-torus knots.
- **Requirements forced on any new triangle.**
  - (R1) Its vanishing must see the roots of Δ on the whole unit circle, not just det. In practice that means the edge collars.
  - (R2) Its connecting cobordism must not contain E_K × I compatibly, if flats are to give level −1/16.
  - (R3) Its sixteenth must come from a γ₁ end in a two-parameter, b⁺ = 1 family (pentagon type) on a cobordism *between* Y_2 and Y_{−2}. The ledger has no such cobordism.
- R1 pushes towards K-independent modifications near the surgery torus. Those preserve E_K × I and so violate R2.
- **Under the pillowcase dictionary, (1) and (2) are therefore in tension.** The way out I see is to weaken "flat" in (2) to "attained by flat-exterior + minimal-cap limits". That is η_g = 1/16, as in T(2,−3), and it is an energy statement.
