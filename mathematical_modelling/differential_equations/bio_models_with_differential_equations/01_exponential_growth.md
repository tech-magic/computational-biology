## 📈 Exponential Growth

**Equation:**

```bash
dy/dt = r * y
```

* Models unrestricted population growth.
* Assumes no environmental limits or death.
* Used for early-stage bacterial or cell growth.

#### 🐍 Python Code

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
r = 0.3          # Growth rate
y0 = 10          # Initial population
t_max = 20       # Time duration
dt = 0.1         # Time step

# Time points
t = np.arange(0, t_max + dt, dt)

# Exponential growth solution: y(t) = y0 * exp(r * t)
y = y0 * np.exp(r * t)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, y, label=f'Exponential Growth (r={r})', color='green')
plt.title('📈 Exponential Growth: dy/dt = r * y')
plt.xlabel('Time')
plt.ylabel('Population')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
```