
# 🍰 Baking a Cake: Finding the Jacobian Matrix for 5 Inputs with 3 Outputs

## 🎯 Real-Life Scenario

You're a baker experimenting with a cake recipe. Your cake's **quality** depends on:

### 🎛️ Inputs (5 total)
| Symbol | Variable             | Description                      |
|--------|----------------------|----------------------------------|
| `x₁`   | Oven Temperature     | in °C                            |
| `x₂`   | Sugar Amount         | in grams                         |
| `x₃`   | Flour Amount         | in grams                         |
| `x₄`   | Baking Time          | in minutes                       |
| `x₅`   | Butter Amount        | in grams                         |

### 📤 Outputs (3 total)
| Symbol     | Output Feature         | Description                         |
|------------|------------------------|-------------------------------------|
| `f₁(x)`    | Sweetness              | Higher with more sugar & heat       |
| `f₂(x)`    | Fluffiness             | Depends on flour, butter, time      |
| `f₃(x)`    | Golden Brown Color     | Temperature × Time interaction      |

---

## 🧮 Define the Output Functions

```
f₁(x) = x₁ * log(1 + x₂)
f₂(x) = (x₃ * x₅) / (x₄ + 1)
f₃(x) = sin(π * x₁ * x₄ / 180)
```

---

## 🔢 Jacobian Matrix: Partial Derivatives

The **Jacobian** is the matrix of partial derivatives:

```
           [ ∂f₁/∂x₁  ∂f₁/∂x₂  ∂f₁/∂x₃  ∂f₁/∂x₄  ∂f₁/∂x₅ ]
    J(x) = [ ∂f₂/∂x₁  ∂f₂/∂x₂  ∂f₂/∂x₃  ∂f₂/∂x₄  ∂f₂/∂x₅ ]
           [ ∂f₃/∂x₁  ∂f₃/∂x₂  ∂f₃/∂x₃  ∂f₃/∂x₄  ∂f₃/∂x₅ ]
```

---

## 🔍 Compute Each Partial Derivative

### 🔸 First Row: `f₁(x) = x₁ * log(1 + x₂)`
```
∂f₁/∂x₁ = log(1 + x₂)
∂f₁/∂x₂ = x₁ / (1 + x₂)
∂f₁/∂x₃ = 0
∂f₁/∂x₄ = 0
∂f₁/∂x₅ = 0
```

### 🔸 Second Row: `f₂(x) = (x₃ * x₅) / (x₄ + 1)`
```
∂f₂/∂x₁ = 0
∂f₂/∂x₂ = 0
∂f₂/∂x₃ = x₅ / (x₄ + 1)
∂f₂/∂x₄ = - (x₃ * x₅) / (x₄ + 1)²
∂f₂/∂x₅ = x₃ / (x₄ + 1)
```

### 🔸 Third Row: `f₃(x) = sin(π * x₁ * x₄ / 180)`
Let `θ = π * x₁ * x₄ / 180`
```
∂f₃/∂x₁ = (π * x₄ / 180) * cos(θ)
∂f₃/∂x₂ = 0
∂f₃/∂x₃ = 0
∂f₃/∂x₄ = (π * x₁ / 180) * cos(θ)
∂f₃/∂x₅ = 0
```

---

## 🔢 Jacobian Matrix (Symbolically)

$$
J(x) =
\begin{bmatrix}
log(1 + x₂) &&  x₁ / (1 + x₂) && 0 && 0 && 0 \\
0 && 0 && x₅ / (x₄ + 1) &&  -x₃ x₅ / (x₄ + 1)² && x₃ / (x₄ + 1) \\
(π x₄ / 180) * cos(θ) && 0 && 0 && (π x₁ / 180) * cos(θ) && 0 \\
\end{bmatrix}
$$

---

## 🧪 Plug in Example Values

| Variable | Value |
|----------|-------|
| `x₁ (Oven Temperature in °C)`     | 180   |
| `x₂ (Sugar Amount in grams)`      | 2     |
| `x₃ (Flour Amount in grams)`      | 100   |
| `x₄ (Baking Time in minutes)`     | 30    |
| `x₅ (Butter Amount in grams)`     | 50    |

### 🔢 Final Jacobian Matrix (Numerical)

Using the input values:  
`x = [x₁=180, x₂=2, x₃=100, x₄=30, x₅=50]` \& `θ = π * x₁ * x₄ / 180`

We compute:

$$
J_\text{cake}(x) \approx
\begin{bmatrix}
    \begin{array}{c|ccccc}
        & \text{Oven Temperature} & \text{Sugar Amount} & \text{Flour Amount} & \text{Baking Time} && \text{Butter Amount} \\
        \hline
        \text{Sweetness} & 1.0986 & 60.0000 & 0       & 0        & 0      \\
        \text{Fluffiness} & 0      & 0       & 1.6129  & -5.2029  & 3.2258 \\
        \text{Golden Brown Color} & -0.4535 & 0      & 0       & -2.7207  & 0 \\
    \end{array}
\end{bmatrix}
$$

---

## 📊 Visualizing Jacobian: Relation to Slopes and Eigenvectors

### 🧠 Intuition about Jacobian and slopes  
The Jacobian generalizes the derivative (slope) of a multivariable function.

- For a single-variable function **𝑓(𝑥)**, the derivative **𝑓′(𝑥)** tells you the slope of the tangent line.  
- For multivariable functions, the **Jacobian** tells you the slope in every input direction — i.e., how the output changes if you wiggle each input variable slightly.

### 🌐 Geometric interpretation  
For a scenario with 2 inputs and 2 outputs; imagine a **tiny circle** in a 2D input space around a point **𝑥<sub>1</sub>, 𝑥<sub>2</sub>**.

The Jacobian maps this **tiny circle** into an **ellipse** in 2D output space.

The shape and orientation of this **ellipse** describe how the value of a given output function **stretches** or **squashes** based on small input changes at point **𝑥<sub>1</sub>, 𝑥<sub>2</sub>**.

For a scenario with 3 inputs and 3 outputs in a 3D space, a similar analogy can be provided by the Jacobian mapping from:
- a **tiny sphere** in a 3D input space into 
- an **ellipsoid** in the output space.

### 🔍 Eigenvectors and eigenvalues of Jacobian  
- **Eigenvectors** of the Jacobian indicate directions in input space where the function stretches or compresses.  
- The corresponding **eigenvalues** tell you the scale factor of stretching/compression in those directions.

If an eigenvalue is:  
- **Large (>1):** the function **expands** inputs along that eigenvector direction.  
- **Small (<1):** the function **contracts** inputs along that eigenvector direction.  
- **Negative:** the function **flips** the direction along that eigenvector.

### ❓ Why eigenvectors of Jacobian matter?  
- In **dynamical systems**, eigenvectors show stable/unstable directions.  
- In **optimization**, they reveal curvature for faster convergence.  
- In **machine learning**, Jacobian eigenvalues relate to sensitivity and stability of models.

---

### 🐍 Python Code

```python
import numpy as np
import matplotlib.pyplot as plt

# 🎛️ Inputs: x = [x1, x2, x3, x4, x5]
# x₁: Oven Temp (°C), x₂: Sugar (g), x₃: Flour (g), x₄: Time (min), x₅: Butter (g)

def cake_outputs(x):
    x1, x2, x3, x4, x5 = x
    f1 = x1 * np.log1p(x2)  # Sweetness
    f2 = (x3 * x5) / (x4 + 1)  # Fluffiness
    f3 = np.sin(np.pi * x1 * x4 / 180)  # Golden Brown Color
    return np.array([f1, f2, f3])

def numerical_jacobian(f, x, eps=1e-5):
    """Numerical Jacobian: df_i/dx_j"""
    n = len(x)
    m = len(f(x))
    J = np.zeros((m, n))
    for j in range(n):
        dx = np.zeros_like(x)
        dx[j] = eps
        J[:, j] = (f(x + dx) - f(x - dx)) / (2 * eps)
    return J

# 🎛️ Input vector
x0 = np.array([180.0, 2.0, 100.0, 30.0, 50.0])

# 🧮 Compute Jacobian at x0
J = numerical_jacobian(cake_outputs, x0)

print("🧮 Jacobian matrix (3 outputs × 5 inputs):\n")
print(J)

# 🔍 Eigen decomposition (on J * Jᵀ for output space analysis)
JJT = J @ J.T
eigenvalues, eigenvectors = np.linalg.eig(JJT)

print("\n🔍 Eigenvalues (J * Jᵀ):")
print(eigenvalues)
print("🔁 Corresponding Eigenvectors:")
print(eigenvectors)

# 📊 Visualize how a small ball in input space changes in output space
def plot_output_ellipse(J):
    theta = np.linspace(0, 2 * np.pi, 100)
    circle = np.array([np.cos(theta), np.sin(theta), np.zeros_like(theta)])
    ellipse = J @ circle[:J.shape[1]]

    plt.figure(figsize=(6,6))
    plt.plot(circle[0], circle[1], 'b--', label='Unit Circle in Input Space')
    plt.plot(ellipse[0], ellipse[1], 'r-', label='Mapped Ellipse in Output Space')
    plt.xlabel("Sweetness")
    plt.ylabel("Fluffiness")
    plt.title("📊 Transformation of Input Perturbations to Output Effects")
    plt.legend()
    plt.axis('equal')
    plt.grid(True)
    plt.show()

# Optional: reduce to 2D for visualization (first two input dimensions)
plot_output_ellipse(J[:, :2])
```
