# Numerical Methods (Euler-like with `odeint`)

### 👶 Layman's Explanation

When exact solutions are hard, let the computer estimate the function step-by-step.

### 🧮 Example

$\frac{dy}{dx} = x + y, \quad y(0) = 1$

### 🐍 Python Code

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def numerical_example(y, x):
    return x + y

x_vals = np.linspace(0, 2, 100)
y0 = 1

# Numerical solve
y_vals = odeint(numerical_example, y0, x_vals)

plt.figure(figsize=(6, 4))
plt.plot(x_vals, y_vals, label="dy/dx = x + y", color='red')
plt.title("4. Numerical Method using odeint")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
```