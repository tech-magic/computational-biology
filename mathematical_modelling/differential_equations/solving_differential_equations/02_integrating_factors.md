# Integrating Factor Method

### 👶 Layman's Explanation

If you can't separate variables, we multiply both sides by something clever (called an *integrating factor*) to make it solvable.

### 🧮 Example

$\frac{dy}{dx} + y = x$
Multiply both sides by $e^x$, solve like normal.

### 🐍 Python Code

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# dy/dx + y = x
def integrating_factor_example(y, x):
    return x - y  # rearranged as dy/dx = x - y

x_vals = np.linspace(0, 2, 100)
y0 = 0  # y(0) = 0

# Solve ODE
y_vals = odeint(integrating_factor_example, y0, x_vals)

# Plot
plt.figure(figsize=(6, 4))
plt.plot(x_vals, y_vals, label="dy/dx + y = x", color='orange')
plt.title("2. Integrating Factor Method")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
```