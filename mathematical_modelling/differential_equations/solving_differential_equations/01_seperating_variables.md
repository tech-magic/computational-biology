# Separation of Variables

### 👶 Layman's Explanation

If you can separate variables on either side of the equation, just integrate both sides.
Think of it like moving stuff to opposite sides to make it easier to solve.

### 🧮 Example

$\frac{dy}{dx} = y \Rightarrow \frac{1}{y} dy = dx \Rightarrow \int \frac{1}{y} dy = \int dx$
This gives:
$\ln |y| = x + C \Rightarrow y = Ce^x$

### 🐍 Python Code

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the ODE dy/dx = y
def separation_example(y, x):
    return y

# x values to evaluate over
x_vals = np.linspace(0, 2, 100)
y0 = 1  # Initial condition: y(0) = 1

# Solve ODE numerically
y_vals = odeint(separation_example, y0, x_vals)

# Plot the result
plt.figure(figsize=(6, 4))
plt.plot(x_vals, y_vals, label="y = Ce^x")
plt.title("1. Separation of Variables: dy/dx = y")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
```