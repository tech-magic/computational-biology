# Characteristic Equation (Second Order)

### 👶 Layman's Explanation

Used in physics (e.g., spring motion). Solve like a quadratic equation using the characteristic roots.

### 🧮 Example

$y'' - 3y' + 2y = 0$
Let $y_1 = y$, $y_2 = y'$ to convert into first-order system.

### 🐍 Python Code

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Convert second-order ODE to first-order system
def characteristic_eq(Y, x):
    y1, y2 = Y  # y1 = y, y2 = y'
    dy1dx = y2
    dy2dx = 3*y2 - 2*y1
    return [dy1dx, dy2dx]

x_vals = np.linspace(0, 5, 200)
initial_conditions = [1, 0]  # y(0) = 1, y'(0) = 0

# Solve system
solution = odeint(characteristic_eq, initial_conditions, x_vals)
y_vals = solution[:, 0]  # extract y from the solution

plt.figure(figsize=(6, 4))
plt.plot(x_vals, y_vals, label="y'' - 3y' + 2y = 0", color='green')
plt.title("3. Characteristic Equation")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
```