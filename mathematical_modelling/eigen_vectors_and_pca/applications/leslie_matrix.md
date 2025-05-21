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

- \( f_i \): **Fertility rate** of age class *i* (average number of offspring per individual per time step)
- \( s_i \): **Survival rate** from age class *i* to age class *i+1* (probability of surviving to the next age group)

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

- Fertility: \( f_1 = 0, f_2 = 1.2, f_3 = 1.8 \)
- Survival: \( s_1 = 0.5, s_2 = 0.8 \)

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
- \( P_t \): population vector at time *t*, where each element represents the number of individuals in each age class

Then:
- \( P_{t+1} = L \cdot P_t \)

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
    L[0, :] = fertility
    for i in range(1, n):
        L[i, i-1] = survival[i-1]
    return L

# Example fertility and survival rates
fertility = [0, 1.2, 1.8]
survival = [0.5, 0.8]

# Build Leslie matrix
L = build_leslie_matrix(fertility, survival)
print("Leslie Matrix:\n", L)

# Initial population vector
P0 = np.array([100, 50, 30])  # 100 young, 50 middle-aged, 30 old

# Simulate 5 time steps
population = P0
for t in range(5):
    print(f"Population at time {t}: {population}")
    population = L @ population
```
