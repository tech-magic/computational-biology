## 🧮 Eigenvectors

### 📘 Example 1: Eigenvectors of a 2×2 Matrix

Let:

```
A = [ 4  1 ]
    [ 2  3 ]
```

#### 🔍 Step 1: Find the Eigenvalues

Solve the **characteristic equation**:

```
det(A - λI) = 0
```

```
= det([4 - λ, 1; 2, 3 - λ])
= (4 - λ)(3 - λ) - 2
= λ² - 7λ + 10
```

🧠 Solving:

```
λ = 5, 2
```

#### 🔓 Step 2: Find Eigenvectors

For **λ = 5**:

```
(A - 5I)v = 0
=> [-1  1; 2 -2]v = 0
=> y = x
```

📐 Eigenvector:

```
v₁ = [1; 1]
```

For **λ = 2**:

```
(A - 2I)v = 0
=> [2 1; 2 1]v = 0
=> y = -2x
```

📐 Eigenvector:

```
v₂ = [1; -2]
```

---

### 📘 Example 2: Eigenvectors of a 3×3 Matrix

Let:

```
B = [2 0 0; 0 3 4; 0 4 9]
```

#### 🔍 Step 1: Find Eigenvalues

```
det(B - λI)
= (2 - λ) * det([3 - λ, 4; 4, 9 - λ])
= (2 - λ)((3 - λ)(9 - λ) - 16)
= (2 - λ)(λ² - 12λ + 11)
```

🧠 Eigenvalues:

```
λ = 2, 6, 11
```

🛠️ You can solve for eigenvectors similarly by plugging each λ into:

```
(B - λI)v = 0
```

---

### 📘 Example 3: Rectangular Matrix 4x3 (No Eigenvectors)

For a non-square matrix (e.g., 4x3), classical eigenvectors do not exist.

🧠 Use **Singular Value Decomposition (SVD)**:

$$
A_{4x3} = U_{4x4} ∙ Σ_{4x3} ∙ V^T_{3x3}
$$

- **Eigenvectors of (A<sup>T</sup> ∙ A)<sub>3x3</sub>** are right singular vectors in **V<sub>3x3</sub>**
- **Eigenvectors of (A ∙ A<sup>T</sup>)<sub>4x4</sub>** are left singular vectors in **U<sub>4x4</sub>**

#### 🔢 Singular Value Decomposition of A (4×3)

Given:

$$
A =
\begin{bmatrix}
3 & 2 & 2 \\
2 & 3 & -2 \\
2 & -2 & 3 \\
1 & 1 & 1
\end{bmatrix}
$$

##### 🔍 Step 1: Compute A<sup>T</sup> A

$$
A^T A =
\begin{bmatrix}
18 & 13 & 9 \\
13 & 18 & -1 \\
9 & -1 & 18
\end{bmatrix}
$$

##### 🔓 Step 2: Compute eigenvalues of A<sup>T</sup> A:

$$
\lambda_1 = 36, \quad \lambda_2 = 16, \quad \lambda_3 = 4
$$

##### 📐 Step 3: Singular values (square roots):

$$
\sigma_1 = 6, \quad \sigma_2 = 4, \quad \sigma_3 = 2
$$

##### 🛠️ Step 4: Form Σ (4×3):

$$
\Sigma =
\begin{bmatrix}
6 & 0 & 0 \\
0 & 4 & 0 \\
0 & 0 & 2 \\
0 & 0 & 0
\end{bmatrix}
$$
