# PCA on a 10×5 Matrix: Find Top 3 Fields

Let X be a 10x5 dataset (10 samples, 5 features):

```
X = [x11 x12 x13 x14 x15;
     x21 x22 x23 x24 x25;
     ...
     x10,1 x10,2 x10,3 x10,4 x10,5]
```

### Step-by-Step PCA

#### Step 1: Standardize the Data

Subtract mean from each column:

```
Z = X - mean(X)
```

#### Step 2: Covariance Matrix

```
C = (1 / (n - 1)) ∙ Z^T Z  // 5x5 matrix
```

#### Step 3: Eigen Decomposition

Find eigenvalues and eigenvectors of C:

```
Eigenvalues: λ1 ≥ λ2 ≥ λ3 ≥ λ4 ≥ λ5
Eigenvectors: v1, v2, v3, v4, v5
```

#### Step 4: Choose Top 3 Principal Components

```
W = [v1 v2 v3]  // 5x3 matrix
```

#### Step 5: Project Original Data

```
Z_proj = Z ∙ W  // 10x3 matrix
```

Now, `Z_proj` contains data projected onto the top 3 most important directions.

---

## Summary

* **Eigenvectors**: Solve det(A - λI) = 0 and find null space of (A - λI)
* **PCA**:

  1. Standardize
  2. Covariance matrix
  3. Eigen decomposition
  4. Top-k eigenvectors
  5. Project original data