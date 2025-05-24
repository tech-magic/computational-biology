# 🧬 Gene Expression Analysis Using PCA

## 📊 Step 1: Input Data Matrix (X)

Let’s begin with a **hand-calculated** gene expression matrix.

Each **row** = 1 biological sample (e.g., a tissue from a person).  
Each **column** = 1 gene’s expression level.

For simplicity, let’s say we studied 3 tissue samples (rows) and measured expression levels of 3 genes (columns).

| Sample | Gene 1 | Gene 2 | Gene 3 |
| ------ | ------ | ------ | ------ |
| S1     | 5      | 3      | 2      |
| S2     | 2      | 2      | 4      |
| S3     | 1      | 3      | 6      |


🧠 **Interpretation**:
- Sample S1 has high expression of Gene 1, moderate of Gene 2, and low of Gene 3.
- Sample S3 shows a pattern where Gene 3 is highly expressed.

---

## 🧮 Step 2: Centering the Data (Mean Normalization)

To compare patterns, we subtract the mean of each gene (column):
```
Mean(Gene 1) = (5 + 2 + 1) / 3 = 2.67
Mean(Gene 2) = (3 + 2 + 3) / 3 = 2.67
Mean(Gene 3) = (2 + 4 + 6) / 3 = 4.00
```

📉 **Centered Data Matrix (X_centered)**:

| Sample | Gene 1 | Gene 2 | Gene 3 |
| ------ | ------ | ------ | ------ |
| S1     | 2.33   | 0.33   | -2.00  |
| S2     | -0.67  | -0.67  | 0.00   |
| S3     | -1.67  | 0.33   | 2.00   |

---

## 📐 Step 3: Covariance Matrix

The covariance matrix helps us understand how genes vary **together**.

Let `X_centered` be our centered matrix. The covariance matrix is calculated as:

$$
C = \frac{1}{n - 1} * (X\_centered)^T * (X\_centered)
$$

🧮 Calculated Covariance Matrix:

|    | G1    | G2   | G3    |
| -- | ----- | ---- | ----- |
| G1 | 4.33  | 0.33 | -3.00 |
| G2 | 0.33  | 0.33 | 0.00  |
| G3 | -3.00 | 0.00 | 4.00  |


---

## 🔍 Step 4: Eigenvectors and Eigenvalues

🧠 **What are these?**
- **Eigenvectors** show **directions** of patterns.
- **Eigenvalues** show **importance (variance)** of each direction.

After computing them (via software or math), assume we get:
```
Principal Component 1 (PC1) → explains 80% variance
Principal Component 2 (PC2) → explains 15% variance
Principal Component 3 (PC3) → explains 5% variance
```


---

## 📉 Step 5: Dimensionality Reduction with PCA

We now project the 3D data into a 2D or 1D space without losing too much information.

🎯 **PCA-transformed data** (Project X_centered onto PC1 and PC2):

| Sample | PC1  | PC2  |
| ------ | ---- | ---- |
| S1     | -2.8 | 0.5  |
| S2     | 0.2  | -0.3 |
| S3     | 2.6  | -0.2 |


🧠 This lets us **visualize and cluster** similar samples based on dominant patterns!

---

## 🧪 Why Is This Useful?

- 🔍 **Find patterns** in gene expression across conditions (e.g., cancer vs. healthy).
- 🧠 **Reduce noise** by focusing on the most important variation.
- 🧭 **Discover biomarkers**: PCA helps in identifying which genes contribute the most to sample variation.

---

## 📌 Summary (Layman Terms)

| Concept        | Layman Explanation                            |
|----------------|-----------------------------------------------|
| Input Matrix   | Each row = a sample, each column = a gene     |
| Centering      | Remove average to focus on *relative* patterns |
| Covariance     | See how genes change together 🤝              |
| Eigenvectors   | Main *directions* of gene behavior 📏         |
| Eigenvalues    | How important each direction is 💡             |
| PCA            | Keeps what matters, removes what doesn’t ✂️   |

---

## 🎯 Final Thought

Using **Eigenvalues, Eigenvectors and PCA** in **Gene Expression Analysis** helps scientists to uncover hidden patterns in complex biological data, making it easier to: 
- identify diseases, 
- understand treatment responses, or 
- group patients based on molecular fingerprints.

