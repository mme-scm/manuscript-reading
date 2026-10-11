# Towards a gauge-theoretic CFK^∞

These are research notes (LaTeX, compiled to `main.pdf`). They take the Heegaard Floer full knot complex
`CFK^∞` (equivalently `CFK` over `F[U,V]`) apart into the mechanisms that produce it. They then propose an
analogue of it in monopole and instanton Floer theory, built on Atiyah–Floer principles. No such complex
exists on the gauge side yet; Li–Ye state explicitly that they cannot construct the `CFK^∞` differential.

## Main points

* **Specification (Lemma 4.2).** `CFK_{F[U,V]}` is `CF^-(Y)` plus two pieces of knot data:
  * an integer Alexander function on generators;
  * a one-sided positivity condition, `n_z ≥ 0`.

  So the base complex must be that of the closed manifold `Y`. The knot enters only through weights.
* **Monopole model (§4.3).** Take the KM complex of `Y`, with the metric stretched along a doubly pointed
  Heegaard surface, and weight trajectories by `V^{n_z}`.
  * `n_z` counts zeros of the vortex component of the spinor along the strip swept by the `z`-arc of `K`.
  * That component is the `E_-(K')` eigenline of Clifford multiplication by the tangent of `K`.
  * Positivity comes from vortex holomorphicity in the adiabatic limit, via an integrality bootstrap.
* **Instanton model (§4.4).** The `z`-charge is a relative Dirac index with a unit `U(1)` flux string along the `z`-arc.
  * In the Atiyah–Floer limit it becomes intersection with a theta-type divisor in `R(Σ)`.
  * The knot enters through how the determinant line is trivialised over the handlebody Lagrangians, because
    `L_α ⊂ R(Σ)` does not see the α-curves.
* **Local model at the knot (§5.3).** Critical Aharonov–Bohm holonomy `β = 1/2`.
  * The two `r^{-1/2}` edge modes are the components seen by `w` and `z`.
  * The two arcs of `K` meet at "creases"; on cobordisms, the creases become Zemke's dividing sets.
  * There is a consistency check with the Hanselman–Rasmussen–Watson marked torus: the Dirac-kernel point
    of the dual torus plays the role of the marked point.
* **Singular variant (§4.5–4.6).** A separate theory, on the Khovanov side rather than an analogue of `CFK`.
  * Parabolic moduli of a twice-punctured Heegaard surface have no walls (Prop. 4.10).
  * The two variables are the nef ends of the segment of Kähler classes (Prop. 4.12), with `t = 4α`.
  * This gives an instanton analogue of Υ.
* **Analysis, tests and roadmap (§5–6).** Genus one is proposed as the first rigorous case: the pillowcase
  with two marked points, and `Sym^1 T^2`.

Statements labelled Theorem, Proposition or Lemma are proved in the notes or are standard. Everything else is
labelled Conjecture, Heuristic or Problem.

## Build

```
pdflatex main.tex && pdflatex main.tex
```

Sources: `main.tex`, `sec1-cfk.tex` … `sec6-instanton-tests.tex`, `refs.tex`.
