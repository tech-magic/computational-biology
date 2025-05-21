# PCA on a 10×5 Matrix: Find Top 3 Features

🔢 Given:
\(X\) be a 10x5 dataset (10 samples, 5 features) represented as a (10 rows, 5 columns) matrix:

```
X = [x11 x12 x13 x14 x15;
     x21 x22 x23 x24 x25;
     ...
     x10,1 x10,2 x10,3 x10,4 x10,5]
```

$$
  X \in \mathbb{R}^{10 \times 5}
$$

---

### 🧮 Step-by-Step PCA

#### Step 1: Standardize the Data

Subtract mean from each column:

$$
  Z = X - mean(X)
$$

- Z is the standardized matrix of X:
$$
  Z \in \mathbb{R}^{10 \times 5}
$$

##### 🔍 What does "subtract mean from each column" mean?

Let’s focus on **Feature 1** (the first column):

You calculate the **mean of Feature 1**:

$$
\mu_1 = \frac{1}{10} \sum_{i=1}^{10} x_{i1}
$$

Then you subtract this mean from each value in the first column.

So the **new centered values** for Feature 1 will be:

$$
z_{i1} = x_{i1} - \mu_1 \quad \text{for all } i = 1 \text{ to } 10
$$

You do the **same for each feature (column)**:

- Compute mean $$ \mu_2 $$, subtract it from Feature 2.
- Compute mean $$ \mu_3 $$, subtract it from Feature 3.
- And so on…


#### Step 2: Covariance Matrix

$$
C = \frac{1}{n - 1} * Z^T * Z
$$

- \(Z^T\) is the transposed matrix of \(Z\):  
  \[
  Z^T \in \mathbb{R}^{5 \times 10}
  \]

- \(C\) is the covariance matrix of \(Z\):  
  \[
  C \in \mathbb{R}^{5 \times 5}
  \]

- \(n\) is the number of samples (i.e., rows in \(X\) which is 10 in this case)

#### Step 3: Eigen Decomposition

Find eigenvalues and corresponding eigenvectors of C. Order the eigen values in the descending order:

```
Eigenvalues: λ1 ≥ λ2 ≥ λ3 ≥ λ4 ≥ λ5
Eigenvectors: v1, v2, v3, v4, v5
```

- \(v1\) is the corresponding eigenvector (a column vector) for \(λ1\):  
  $$
  v1 \in \mathbb{R}^{5 \times 1}
  $$

- \(v2\) is the corresponding eigenvector (a column vector) for \(λ2\):  
  $$
  v2 \in \mathbb{R}^{5 \times 1}
  $$

- And so on...

#### Step 4: Choose Top 3 Principal Components

```
W = [v1 v2 v3]  // 5x3 matrix
```

- \(v1\) is the top-1st eigenvector (a column vector):  
  $$
  v1 \in \mathbb{R}^{5 \times 1}
  $$

- \(v2\) is the top-2nd eigenvector (a column vector):  
  $$
  v2 \in \mathbb{R}^{5 \times 1}
  $$

- \(v3\) is the top-3rd eigenvector (a column vector):  
  $$
  v3 \in \mathbb{R}^{5 \times 1}
  $$

- \(W\) represents the top-3 eigenvectors:  
  $$
  W \in \mathbb{R}^{5 \times 3}
  $$

#### Step 5: Project Original Data

\[
Z\_proj = Z * W
\]

Now, \[Z\_proj\] contains data projected onto the top 3 most important directions (derived from 3 most important features).
\[
  Z\_proj \in \mathbb{R}^{10 \times 3}
\]


#### 🎯 Summary

* **PCA**:

  1. Standardize
  2. Covariance matrix
  3. Eigen decomposition
  4. Top-k eigenvectors
  5. Project original data

---

### 🔁 **Reconstruct Approximation of Original Matrix**

#### Step 1: Reconstruct Standard Matrix

You want to approximate the original standardized matrix **Z** (10×5) using only the top 3 principal components:

$$
\hat{Z} = Z_{\text{proj}} * W^T \in \mathbb{R}^{10 \times 5}
$$

- \(Z_{\text{proj}}\) is the projection:  
  $$
  Z_{\text{proj}} \in \mathbb{R}^{10 \times 3}
  $$

- \(W^T\) is the transpose of the top-3 (based on the previous example) eigenvectors:  
  $$
  W^T \in \mathbb{R}^{3 \times 5}
  $$

This gives you the best rank-3 approximation of the standardized data in the least squares sense.

#### **Step 2: Recover Approximate Original Data X**  
To approximate the original non-standardized data **X**:

$$
\hat{X} = \hat{Z} + \mu
$$

Where \(\mu\) is the row vector of original feature means (broadcasted across all rows):

$$
\mu \in \mathbb{R}^{1 \times 5}
$$

---

### 🐍 Python Code

```python
import numpy as np

# Generate a random 10x5 matrix X with real values
# (10 rows -> 10 samples, 5 columns -> 5 features)
X = np.random.rand(10, 5)

# Center the data by subtracting the mean of each column (feature)
# This step is important for PCA because PCA is affected by the scale and mean of data
X_centered = X - X.mean(axis=0)

# Compute the covariance matrix of the centered data
# rowvar=False means each column represents a variable (feature),
# and each row represents an observation/sample
cov = np.cov(X_centered, rowvar=False)

# Perform eigen decomposition of the covariance matrix
# Use np.linalg.eigh because covariance matrices are symmetric
# np.linalg.eigh guarantees real eigenvalues and eigenvectors,
# and is more efficient for symmetric/hermitian matrices than np.linalg.eig
eigvals, eigvecs = np.linalg.eigh(cov)

# The eigenvalues/eigenvectors are not necessarily sorted
# Sort them in descending order based on eigenvalues (largest first)
idx = np.argsort(eigvals)[::-1]
eigvals = eigvals[idx]
eigvecs = eigvecs[:, idx]

print("Sorted Eigenvalues:", eigvals)

# Calculate the proportion of variance explained by each component
explained_variance_ratio = eigvals / np.sum(eigvals)
cumulative_variance_ratio = np.cumsum(explained_variance_ratio)

print("\nExplained Variance Ratio:", explained_variance_ratio)
print("Cumulative Explained Variance:", cumulative_variance_ratio)

# Project the centered data onto the principal components (eigenvectors)
# This gives the representation of data in the principal component space
# Each row of Z_proj is the coordinates of the corresponding original sample
Z_proj = X_centered @ eigvecs

# To approximate the original data from the projection, multiply
# Z_proj by the transpose of the eigenvector matrix, then add back the mean
# This reconstructs data in the original feature space (but some info may be lost if fewer PCs used)
X_approx = Z_proj @ eigvecs.T + X.mean(axis=0)

print("\nOriginal Data (X):")
print(X)
print("\nProjection onto Principal Components (Z_proj):")
print(Z_proj)
print("\nApproximate Reconstruction of Original Data (X_approx):")
print(X_approx)
```

---

## 📚 Key Notes: 

### 🔍 What if Eigenvalues are Complex Numbers in PCA?

In **Principal Component Analysis (PCA)**, you're working with the **covariance matrix**:

$$
C = \frac{1}{n - 1} * Z^T * Z
$$

where:
- \( Z \) is your standardized data matrix,
- \( C \) is **real-valued** (because your data is real),
- \( C \) is also **symmetric**, since \( C = C^T \).

##### Key Linear Algebra Fact

> All eigenvalues of a **real symmetric matrix** are **guaranteed to be real**.

##### 📌 Therefore, in standard PCA:

- **Eigenvalues will always be real.**
- **Eigenvectors will also be real and orthogonal.**

### 🔍 Explained Variance Ratio

To understand how much information is retained by the principal components, we use the **explained variance ratio**.

##### 🔸 Formula:

For the $i$-th principal component:

$$
\text{Explained Variance Ratio} = \frac{\lambda_i}{\sum_{j=1}^{5} \lambda_j}, \quad i = 1, 2, 3
$$

This helps determine **how many components to keep** by showing the proportion of total variance captured by each.

##### 🧠 What Do the Terms Mean?

- $\lambda_i$: The eigenvalue corresponding to the $i$-th principal component (i.e., variance captured by that component).
- $\sum_{j=1}^{5} \lambda_j$: The total variance in the data (sum of all eigenvalues of the covariance matrix $C$).

The set of eigenvalues:

$$
\{\lambda_1, \lambda_2, \lambda_3, \lambda_4, \lambda_5\}
$$

are typically **sorted in descending order**:

$$
\lambda_1 \geq \lambda_2 \geq \lambda_3 \geq \lambda_4 \geq \lambda_5
$$

Each eigenvalue represents the variance explained by its associated eigenvector (principal component).

##### 📌 Summary:

- **Numerator**: $\lambda_i$ — the variance explained by the $i$-th component.  
- **Denominator**: $\sum_{j=1}^{5} \lambda_j$ — total variance in the dataset.

The **explained variance ratio** tells you the **contribution of component $i$** to the overall variance.

##### ✅ Example:

To find the proportion of total variance explained by the **top 3 components**:

$$
\frac{\lambda_1 + \lambda_2 + \lambda_3}{\lambda_1 + \lambda_2 + \lambda_3 + \lambda_4 + \lambda_5}
$$

