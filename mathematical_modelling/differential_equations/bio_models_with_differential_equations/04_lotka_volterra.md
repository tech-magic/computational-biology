## 🐇🦊 Lotka-Volterra Predator-Prey Model

**Equations:**

```bash
dPrey/dt = α * Prey - β * Prey * Predator  
dPredator/dt = δ * Prey * Predator - γ * Predator
```

* Describes cyclical dynamics between prey and predator.
* **Parameters:**

  * `α`: prey growth rate
  * `β`: predation rate
  * `γ`: predator death rate
  * `δ`: predator growth per consumed prey

#### 🐍 Python Code

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
alpha = 1.1   # Prey birth rate
beta = 0.4    # Predation rate
gamma = 0.4   # Predator death rate
delta = 0.1   # Predator reproduction rate per prey eaten

# Initial populations
prey0 = 40     # Initial prey population (e.g., rabbits)
predator0 = 9  # Initial predator population (e.g., foxes)

# Time settings
t_max = 200
dt = 0.1
t = np.arange(0, t_max + dt, dt)

# Arrays to store values
prey = np.zeros_like(t)
predator = np.zeros_like(t)

# Set initial values
prey[0] = prey0
predator[0] = predator0

# Euler's method for numerical integration
for i in range(1, len(t)):
    dPrey = alpha * prey[i-1] - beta * prey[i-1] * predator[i-1]
    dPredator = delta * prey[i-1] * predator[i-1] - gamma * predator[i-1]
    
    prey[i] = prey[i-1] + dPrey * dt
    predator[i] = predator[i-1] + dPredator * dt

# Plotting the populations over time
plt.figure(figsize=(12, 6))
plt.plot(t, prey, label='🐇 Prey', color='green')
plt.plot(t, predator, label='🦊 Predator', color='red')
plt.title('🐇🦊 Lotka-Volterra Predator-Prey Model')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Phase-space plot (Prey vs Predator)
plt.figure(figsize=(6, 6))
plt.plot(prey, predator, color='purple')
plt.title('Phase-Space: Predator vs Prey')
plt.xlabel('🐇 Prey Population')
plt.ylabel('🦊 Predator Population')
plt.grid(True)
plt.tight_layout()
plt.show()
```