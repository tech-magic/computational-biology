## 🧪 Logistic Growth

**Equation:**

```bash
dy/dt = r * y * (1 - y/K)
```

* Adds carrying capacity `K`.
* Models population growth with resource limits.
* Used in ecology and resource-limited population studies.

#### 🐍 Python Code

```python

import numpy as np
import matplotlib.pyplot as plt

# Parameters
r = 0.5           # Intrinsic growth rate
K = 100           # Carrying capacity
y0 = 10           # Initial population
t_max = 50        # Total time
dt = 0.1          # Time step

# Time array
t = np.arange(0, t_max + dt, dt)
y = np.zeros_like(t)
y[0] = y0

# Euler's method for numerical solution
for i in range(1, len(t)):
    y[i] = y[i-1] + r * y[i-1] * (1 - y[i-1] / K) * dt

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, y, label=f'Logistic Growth (r={r}, K={K})', color='blue')
plt.title('🧪 Logistic Growth: dy/dt = r * y * (1 - y/K)')
plt.xlabel('Time')
plt.ylabel('Population')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

```
