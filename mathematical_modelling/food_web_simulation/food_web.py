# python3 -m venv forest-venv
# pip install numpy scipy matplotlib

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Species and their indices
species = [
    "Plants", "Insects", "FruitBirds", "Deer", "Monkeys",
    "Frogs", "Spiders", "WildCats", "LargeBirds", "Snakes",
    "BigCats", "PredBirds", "Vultures", "Decomposers"
]
species_index = {name: i for i, name in enumerate(species)}
n = len(species)

# Predator-prey edges
edges = [
    ("Insects", "Plants"),
    ("FruitBirds", "Plants"),
    ("Deer", "Plants"),
    ("Monkeys", "Plants"),
    ("Frogs", "Insects"),
    ("Spiders", "Insects"),
    ("WildCats", "Deer"),
    ("LargeBirds", "Monkeys"),
    ("Snakes", "Frogs"),
    ("Snakes", "Spiders"),
    ("PredBirds", "Snakes"),
    ("BigCats", "WildCats"),
    ("BigCats", "LargeBirds"),
    ("BigCats", "Snakes"),
    ("BigCats", "PredBirds"),
    ("Vultures", "BigCats")
]

# Predation matrix
predation_matrix = np.zeros((n, n))  # [predator][prey]
for predator, prey in edges:
    i, j = species_index[predator], species_index[prey]
    predation_matrix[i, j] = 1

# Parameters
growth_rate = np.zeros(n)
carrying_capacity = np.zeros(n)
death_rate = 0.1 * np.ones(n)
efficiency = 0.1 * np.ones((n, n))
attack_rate = 0.01 * np.ones((n, n))

# Plants grow naturally
growth_rate[species_index["Plants"]] = 0.5
K_max = 1000
beta = 0.01

# Seasonal sunlight function
def R_t(t):
    return 100 + 50 * np.sin(2 * np.pi * t / 50)

def K_plants(R):
    return K_max * (1 - np.exp(-beta * R))

# ODE function with decomposer feedback and external shocks
def food_web_extended(Y, t):
    dYdt = np.zeros(n)
    Rt = R_t(t)
    K = np.copy(carrying_capacity)
    K[species_index["Plants"]] = K_plants(Rt)

    # Drought shock every 70–80 units
    drought_factor = 0.3 if 70 <= (t % 100) <= 80 else 1.0

    # Hunting shock every 150–160 units
    hunting_factor = 0.5 if 150 <= (t % 200) <= 160 else 1.0

    for i in range(n):
        # Plants: logistic growth + decomposer boost
        if i == species_index["Plants"]:
            dYdt[i] += growth_rate[i] * Y[i] * (1 - Y[i] / K[i]) * drought_factor
            dYdt[i] += 0.02 * Y[species_index["Decomposers"]]  # nutrient recycling

        # Gains from prey and prey losses
        for j in range(n):
            if predation_matrix[i, j]:
                pred_gain = efficiency[i, j] * attack_rate[i, j] * Y[i] * Y[j]
                prey_loss = attack_rate[i, j] * Y[i] * Y[j]
                dYdt[i] += pred_gain
                dYdt[j] -= prey_loss

        # Natural death
        natural_death = death_rate[i] * Y[i]
        dYdt[i] -= natural_death

        # Decomposers grow from all dead matter
        if i == species_index["Decomposers"]:
            total_dead = sum(death_rate[j] * Y[j] for j in range(n) if j != i)
            dYdt[i] += 0.05 * total_dead - natural_death

        # Apply hunting to top predators
        if species[i] in ["BigCats", "PredBirds"]:
            dYdt[i] *= hunting_factor

    return dYdt

# Initial populations
Y0 = np.ones(n) * 10
Y0[species_index["Plants"]] = 100

# Time vector
t = np.linspace(0, 200, 1000)

# Solve ODE
solution = odeint(food_web_extended, Y0, t)

# Plotting
plt.figure(figsize=(12, 8))
for i in range(n):
    plt.plot(t, solution[:, i], label=species[i])
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Forest Food Web Dynamics with Seasonal Sunlight, Decomposers, and Shocks")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
