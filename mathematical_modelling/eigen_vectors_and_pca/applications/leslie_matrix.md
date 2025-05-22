# 🧬 Leslie Matrix Model in Population Dynamics

## 📌 What is a Leslie Matrix?

The **Leslie matrix** is a square matrix used in **population dynamics** to model **age-structured population growth**. It captures how individuals in different age groups contribute to future generations through:

- **Fertility rates** (births)
- **Survival rates** (aging to the next group)

---

## 🔧 Construction of the Leslie Matrix

Suppose there are **n age classes**:  
- Age class 1 = youngest (e.g., newborns)  
- Age class n = oldest (e.g., seniors)

We define:

- f<sub>i</sub>: **Fertility rate** of age class *i* (average number of offspring per individual per time step)
- s<sub>i</sub>: **Survival rate** from age class *i* to age class *i+1* (probability of surviving to the next age group)

---

### ✅ Matrix Structure

$$
L =
\begin{bmatrix}
f_1 & f_2 & f_3 & \cdots & f_n \\
s_1 & 0   & 0   & \cdots & 0 \\
0   & s_2 & 0   & \cdots & 0 \\
\vdots & \ddots & \ddots & \ddots & \vdots \\
0 & \cdots & 0 & s_{n-1} & 0 \\
\end{bmatrix}
$$

- **Top row**: fertility rates — represents newborns produced by each age group.
- **Subdiagonal**: survival rates — represents individuals aging into the next class.
- All other elements are zero.

---

## 🧮 Example: 3 Age Classes

Given:

- Fertility: ( f<sub>1</sub> = 0, f<sub>2</sub> = 1.2, f<sub>3</sub> = 1.8 )
- Survival: ( s<sub>1</sub> = 0.5, s<sub>2</sub> = 0.8 )

Then the Leslie matrix is:

$$
L =
\begin{bmatrix}
0 & 1.2 & 1.8 \\
0.5 & 0 & 0 \\
0 & 0.8 & 0 \\
\end{bmatrix}
$$

---

## 🧠 How to Use the Leslie Matrix

If:
- P<sub>t</sub> : population vector at time *t*, where each element represents the number of individuals in each age class

Then:
- P<sub>{t+1}</sub> = L . P<sub>t</sub>

You can iterate this to model how the population evolves over time.

---

## 📈 Biological Interpretation

- **Top row**: births contributed by existing individuals.
- **Subdiagonal**: individuals aging into the next group.
- **Eigenvalues**: indicate long-term growth or decline rate.
- **Dominant eigenvector**: gives the stable age distribution.

---

## 🐍 Python Example

```python
import numpy as np

def build_leslie_matrix(fertility, survival):
    n = len(fertility)
    L = np.zeros((n, n))
    L[0, :] = fertility  # Top row: births contributed by all age groups
    for i in range(1, n):
        L[i, i-1] = survival[i-1]  # Subdiagonal: survival from one age group to the next
    return L

# Fertility and survival rates
fertility = [0, 1.2, 1.8]
survival = [0.5, 0.8]

# Build Leslie matrix
L = build_leslie_matrix(fertility, survival)
print("Leslie Matrix:\n", L)

# Biological Interpretation
print("\nBiological Interpretation:")
print("- Top row (births):", L[0])
print("- Subdiagonal (aging/survival):")
for i in range(1, L.shape[0]):
    print(f"  From age group {i-1} to {i}: survival rate = {L[i, i-1]}")

# Initial population vector
P0 = np.array([100, 50, 30])  # Young, middle-aged, old
population = P0

# Simulate population over 5 time steps
print("\nPopulation Dynamics:")
for t in range(5):
    print(f"  Time {t}: {population}")
    population = L @ population

# Eigenvalue analysis
eigenvalues, eigenvectors = np.linalg.eig(L)
dominant_index = np.argmax(np.real(eigenvalues))
dominant_eigenvalue = np.real(eigenvalues[dominant_index])
stable_age_distribution = np.real(eigenvectors[:, dominant_index])
stable_age_distribution /= stable_age_distribution.sum()  # Normalize

print("\nEigenvalue Analysis:")
print("  Eigenvalues:", np.round(eigenvalues, 3))
print("  Dominant eigenvalue (growth rate):", round(dominant_eigenvalue, 3))
print("  Stable age distribution (dominant eigenvector):", np.round(stable_age_distribution, 3))
```

### 📌 Output Explanation:

- Top Row (Births): Shows how many offspring each age group contributes (fertility).
- Subdiagonal: Survival probabilities from one age class to the next.
- Eigenvalues:
    - Dominant eigenvalue > 1 → population grows.
    - Dominant eigenvalue < 1 → population declines.
    - = 1 → stable size.
- Dominant Eigenvector:
    - Represents the stable age distribution — the relative proportions of individuals in each age class after many generations.
