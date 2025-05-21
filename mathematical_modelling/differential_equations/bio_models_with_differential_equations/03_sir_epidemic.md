## 🦠 SIR Epidemic Model

**Equations:**

```mathematica
dS/dt = -β * S * I / N  
dI/dt = β * S * I / N - γ * I  
dR/dt = γ * I
```

* Models disease spread in a population.
* **S**: Susceptible, **I**: Infected, **R**: Recovered.
* **Parameters:**

  * `β`: infection rate
  * `γ`: recovery rate
  * `N`: total population

#### 🐍 Python Code

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 1000          # Total population
beta = 0.3        # Infection rate
gamma = 0.1       # Recovery rate

# Initial conditions
I0 = 1            # Initial infected
R0 = 0            # Initial recovered
S0 = N - I0 - R0  # Initial susceptible

# Time parameters
t_max = 160
dt = 0.1
t = np.arange(0, t_max + dt, dt)

# Arrays to hold values
S = np.zeros_like(t)
I = np.zeros_like(t)
R = np.zeros_like(t)

# Set initial values
S[0], I[0], R[0] = S0, I0, R0

# Euler integration
for i in range(1, len(t)):
    dS = -beta * S[i-1] * I[i-1] / N
    dI = beta * S[i-1] * I[i-1] / N - gamma * I[i-1]
    dR = gamma * I[i-1]
    
    S[i] = S[i-1] + dS * dt
    I[i] = I[i-1] + dI * dt
    R[i] = R[i-1] + dR * dt

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, S, label='Susceptible (S)', color='blue')
plt.plot(t, I, label='Infected (I)', color='red')
plt.plot(t, R, label='Recovered (R)', color='green')
plt.title('🦠 SIR Epidemic Model')
plt.xlabel('Time')
plt.ylabel('Population')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
```