## Eigenvectors

### Example 1: Eigenvectors of a 2×2 Matrix

Let:

```
A = [ 4  1 ]
    [ 2  3 ]
```

#### Step 1: Find the Eigenvalues

Solve the **characteristic equation**:

```
det(A - λI) = 0
```

```
= det([4 - λ, 1; 2, 3 - λ])
= (4 - λ)(3 - λ) - 2
= λ^2 - 7λ + 10
```

Solving:

```
λ = 5, 2
```

#### Step 2: Find Eigenvectors

For λ = 5:

```
(A - 5I)v = 0
=> [-1  1; 2 -2]v = 0
=> y = x
```

Eigenvector:

```
v1 = [1; 1]
```

For λ = 2:

```
(A - 2I)v = 0
=> [2 1; 2 1]v = 0
=> y = -2x
```

Eigenvector:

```
v2 = [1; -2]
```

---

### Example 2: Eigenvectors of a 3×3 Matrix

Let:

```
B = [2 0 0; 0 3 4; 0 4 9]
```

#### Step 1: Find Eigenvalues

```
det(B - λI)
= (2 - λ) * det([3 - λ, 4; 4, 9 - λ])
= (2 - λ)((3 - λ)(9 - λ) - 16)
= (2 - λ)(λ^2 - 12λ + 11)
```

Eigenvalues:

```
λ = 2, 6, 11
```

You can solve for eigenvectors similarly by plugging each λ into (B - λI)v = 0.

---

### Example 3: Rectangular Matrix 4x3 (No Eigenvectors)

For a non-square matrix (e.g., 4x3), classical eigenvectors do not exist.

Use **Singular Value Decomposition (SVD)**:

```
A_{4x3} = U_{4x4} ∙ Σ_{4x3} ∙ V^T_{3x3}
```

* Eigenvectors of A^T A are right singular vectors (V)
* Eigenvectors of A A^T are left singular vectors (U)
