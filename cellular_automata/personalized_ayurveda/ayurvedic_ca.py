# 🍃 Ayurvedic Cellular Automata Simulation (Personalized Body-Level Model)
# -------------------------------------------------------------
# 👤 This script simulates a 100x100 grid representing regions of a human body.
# 🧬 Each cell in the grid corresponds to a tissue patch with its own Ayurvedic dosha values:
#     - Vatha (movement)
#     - Pitha (transformation)
#     - Kapha (structure)
# ➕ Plus, each cell has physiological features: age, stress, diet impact, and toxins.
# 🧠 Transition rules are hand-coded to demonstrate how internal dosha imbalance and external
#    factors lead to localized health states (like inflammation, stagnation, or respiratory issues).
# 🔁 The simulation runs for multiple time steps, showing how health conditions evolve over time.
# -------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Define grid size (100x100 body patches)
GRID_SIZE = 100
NUM_STEPS = 10

# Each cell contains:
# [Vatha, Pitha, Kapha, Age, Stress, Diet, Toxins, Condition]
# Condition: 0=healthy, 1=inflammation, 2=sluggishness, 3=respiratory issue
state = np.zeros((GRID_SIZE, GRID_SIZE, 8), dtype=np.float32)

# ---------------------------------------
# Initialize synthetic Ayurvedic body data
# ---------------------------------------
np.random.seed(42)

# Synthesize tissue types (simplified model)
def initialize_body_grid(state):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            # Example: torso might have higher Kapha; head more Pitha; limbs more Vatha
            if 30 < i < 70 and 30 < j < 70:  # Torso
                kapha = np.random.uniform(0.5, 0.9)
                vatha = np.random.uniform(0.1, 0.3)
                pitha = 1.0 - kapha - vatha
            elif i < 20:  # Head
                pitha = np.random.uniform(0.5, 0.8)
                vatha = np.random.uniform(0.2, 0.4)
                kapha = 1.0 - vatha - pitha
            else:  # Limbs
                vatha = np.random.uniform(0.6, 0.9)
                kapha = np.random.uniform(0.1, 0.3)
                pitha = 1.0 - vatha - kapha

            # Normalize VPK
            vpk_total = vatha + pitha + kapha
            vatha /= vpk_total
            pitha /= vpk_total
            kapha /= vpk_total

            # Assign doshas + features
            state[i, j, 0] = vatha
            state[i, j, 1] = pitha
            state[i, j, 2] = kapha
            state[i, j, 3] = np.random.uniform(25, 50)      # Age (local tissue aging)
            state[i, j, 4] = np.random.uniform(0.0, 1.0)     # Stress level
            state[i, j, 5] = np.random.uniform(0.0, 1.0)     # Diet influence (0 = bad, 1 = good)
            state[i, j, 6] = np.random.uniform(0.0, 1.0)     # Toxins (Ama)
            state[i, j, 7] = 0                               # Initial condition = healthy

    return state

# --------------------------------------------
# Define hand-crafted transition rule function
# --------------------------------------------
def update_state(state):
    new_state = np.copy(state)
    for i in range(1, GRID_SIZE - 1):
        for j in range(1, GRID_SIZE - 1):
            cell = state[i, j]
            neighbors = state[i-1:i+2, j-1:j+2, :]

            v, p, k = cell[0], cell[1], cell[2]
            age, stress, diet, toxins = cell[3:7]

            # Rule: Inflammation (high pitha + vatha + stress)
            if v + p > 1.3 and stress > 0.6:
                new_state[i, j, 7] = 1

            # Rule: Sluggishness (high kapha + bad diet + toxins)
            elif k > 0.5 and diet < 0.4 and toxins > 0.5:
                new_state[i, j, 7] = 2

            # Rule: Respiratory/joint issues (high kapha + vatha + age)
            elif k + v > 1.2 and age > 40:
                new_state[i, j, 7] = 3

            else:
                new_state[i, j, 7] = 0  # Remains or returns to healthy

    return new_state

# -----------------------------------------
# Run simulation and plot health heatmaps
# -----------------------------------------
state = initialize_body_grid(state)
history = []

for step in range(NUM_STEPS):
    state = update_state(state)
    history.append(state[:, :, 7])  # Store health state

# Plot health evolution at each step
fig, axs = plt.subplots(2, NUM_STEPS // 2, figsize=(20, 5))
for i in range(NUM_STEPS):
    ax = axs[i // (NUM_STEPS // 2), i % (NUM_STEPS // 2)]
    ax.imshow(history[i], cmap='viridis', vmin=0, vmax=3)
    ax.set_title(f"Step {i}")
    ax.axis('off')

plt.suptitle("Health Evolution Over Time (0=Healthy, 1=Inflammation, 2=Sluggish, 3=Respiratory)")
plt.tight_layout()
plt.show()
