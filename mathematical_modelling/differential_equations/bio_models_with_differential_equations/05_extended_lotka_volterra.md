## 🧬 Extended Lotka-Volterra Predator-Prey Model (with Prey Death Rate)

**Equations:**

```bash
dPrey/dt = α * Prey - β * Prey * Predator - μ * Prey  
dPredator/dt = δ * Prey * Predator - γ * Predator
```

* Adds natural death rate of prey to the classic model.
* More realistic for ecosystems where prey have mortality beyond predation.
* **Parameters:**

  * `α`: prey growth rate
  * `β`: predation rate
  * `γ`: predator death rate
  * `δ`: predator growth per consumed prey
  * `μ`: prey natural death rate

#### 🐍 Python Code

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
alpha = 1.1   # Prey growth rate
beta = 0.4    # Predation rate
gamma = 0.4   # Predator death rate
delta = 0.1   # Predator reproduction per prey eaten
mu = 0.1      # Prey natural death rate

# Initial populations
prey0 = 40
predator0 = 9

# Time settings
t_max = 200
dt = 0.1
t = np.arange(0, t_max + dt, dt)

# Arrays to hold values
prey = np.zeros_like(t)
predator = np.zeros_like(t)

# Set initial values
prey[0] = prey0
predator[0] = predator0

# Euler integration loop
for i in range(1, len(t)):
    dPrey = alpha * prey[i-1] - beta * prey[i-1] * predator[i-1] - mu * prey[i-1]
    dPredator = delta * prey[i-1] * predator[i-1] - gamma * predator[i-1]

    prey[i] = prey[i-1] + dPrey * dt
    predator[i] = predator[i-1] + dPredator * dt

# Plotting population over time
plt.figure(figsize=(12, 6))
plt.plot(t, prey, label='🐇 Prey', color='green')
plt.plot(t, predator, label='🦊 Predator', color='red')
plt.title('🧬 Extended Lotka-Volterra Model with Prey Death Rate')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Phase-space plot
plt.figure(figsize=(6, 6))
plt.plot(prey, predator, color='purple')
plt.title('Phase-Space: Predator vs Prey (with Prey Death Rate)')
plt.xlabel('🐇 Prey Population')
plt.ylabel('🦊 Predator Population')
plt.grid(True)
plt.tight_layout()
plt.show()
```

