# ell for S^3_{±2}(4_1): two independent computations

Two independent agents computed this (A: knot group / Kirk–Klassen plus orbifold rho; B: Seifert structure with the Fintushel–Stern arguments redone for H_1 = Z/2).
Scripts are in scratchpad/fig8-A and scratchpad/fig8-B; the reports are reproduced in the session transcript.

## Manifolds

- Y_{+2} = S^3_{+2}(4_1) = M(-1; (2,1),(4,1),(5,1)). It bounds the negative-definite plumbing (-1; -2,-4,-5), with e = -1/20 and H_1 = Z/2.
- Y_{-2} = -Y_{+2}, since 4_1 is amphichiral.
- Identification:
  - B: SnapPy homomorphism counts.
  - A: Regina.
- Orientation:
  - A: Chern–Simons matching and the Euler characteristic.
  - B: Casson–Walker.
- Both find S^3_{+1}(4_1) = Sigma(2,3,7), not S^3_{-1}(4_1).

## Normalisations

- CS is in DLME's sign, E = CS(alpha) - CS(alpha').
- The grading is the index alpha -> theta, with decay weights at theta, mod 8.
- lambda = CS - gr/8 = (3 + rho_APS(ad alpha))/16.
- Duality: lambda(-Y) = 3/8 - lambda(Y).
- Calibration reproduces DLME's Sigma(2,3,5) example: (1/120, 1) and (49/120, 5), with lambda = -7/60 and -13/60.

## Trivial bundle (both agents agree exactly; VERIFIED)

There are no differentials. Each column lists (grading mod 8, lifted CS) for the generators alpha and chi·alpha.

| | Y_{+2} | Y_{-2} |
|---|---|---|
| generators | (7, 9/80 ≡ 89/80 with gr lifted by 8), (3, 49/80) | (6, 71/80), (2, 31/80) |
| lambda | 19/80, 19/80 | 11/80, 11/80 |
| ell | 19/80 | 11/80 |

ell(Y_{-2}) - ell(Y_{+2}) = -1/10.

## Nontrivial bundle (w_2 ≠ 0)

DLME's framework does not apply to this bundle as it stands. The reducible tau is non-central, with stabiliser O(2), and there is no theta to fix the lifts.

There are two dihedral irreducibles. In the "virtual theta" normalisation (3 + rho)/16:
- Y_{+2}: lambda = 1/5 and 3/10, so ell = 1/5.
- Y_{-2}: lambda = 7/40 and 3/40, so ell = 3/40.

Normalising relative to the reducible tau changes the absolute values, and the two agents differ there by a uniform 1/8. In every normalisation the difference is ell(Y_{-2}) - ell(Y_{+2}) = -1/8.

## Pattern

ell(Y_{-1}) = 5/168 < ell(Y_{-2}) = 11/80 < ell(Y_{+2}) = 19/80 < ell(Y_{+1}) = 23/84.

So ell increases with 1/r. The ±2 gap is 1/10 ≥ 1/16 in the trivial bundle and 1/8 in the nontrivial one; the ±1 gap is 41/168 > 1/8.
