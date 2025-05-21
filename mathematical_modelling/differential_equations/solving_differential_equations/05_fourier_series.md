# Fourier Series / Transforms

### 👶 Layman's Explanation

Used to break complex patterns into simple waves (like heat, sound or temperature). We use sine/cosine functions that evolve over time.

### 🧮 Example

Simulate solution to:
$u(x, t) = \sin(\pi x) e^{-\pi^2 t}$
This is a solution to the heat equation.

### 🐍 Python Code

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)
time_points = [0.0, 0.1, 0.2, 0.5, 1.0]

plt.figure(figsize=(6, 4))
for t in time_points:
    u_xt = np.sin(np.pi * x) * np.exp(-np.pi**2 * t)
    plt.plot(x, u_xt, label=f"t={t}")

plt.title("5. Fourier Heat Equation")
plt.xlabel("x")
plt.ylabel("u(x, t)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
```
