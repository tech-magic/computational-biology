import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Patch

# Define the parameters of the simulation
grid_size = (20, 30)  # 2D grid (height x width), representing the nephron network
timesteps = 100  # Number of timesteps to simulate
hydration_level = 0.5  # 0 to 1 scale, 1 being well hydrated
waste_concentration = 0.7  # 0 to 1 scale, higher is more waste
glucose_level = 0.3  # 0 to 1 scale, higher is more glucose in the blood
aldosterone_level = 0.6  # 0 to 1 scale, higher is more aldosterone
adh_level = 0.7  # 0 to 1 scale, higher is more ADH (water reabsorption)

# Initialize the grid (state of the nephron cells)
grid = np.zeros(grid_size)  # All cells initially "filtered" (0)

# Cell state encoding:
# 0 = "Filtered" (fluid has entered the nephron)
# 1 = "Reabsorbed" (fluid is reabsorbed back into the blood)
# 2 = "Excreted" (fluid is excreted as urine)

# Define the rules for the CA (simplified for this model)
def update_cell(state, hydration, waste, glucose, aldosterone, adh, neighbors):
    if state == 0:  # "Filtered" state
        if hydration > 0.5:  # High hydration, reabsorb more water
            if np.random.rand() < 0.7 * adh:  # Higher ADH means more reabsorption
                return 1  # "Reabsorbed"
        if glucose > 0.5:  # High glucose, filter more
            return 0  # Stay "Filtered"
        elif aldosterone > 0.5:  # High aldosterone, reabsorb sodium
            return 1  # "Reabsorbed"
        elif waste > 0.5:  # High waste, excrete
            return 2  # "Excreted"
        else:
            return 2  # "Excreted" if not reabsorbed

    elif state == 1:  # "Reabsorbed"
        if waste > 0.7:  # High waste, increase excretion
            return 2  # "Excreted"
        return 1  # Stay "Reabsorbed"

    return state  # Stay "Excreted"

# Function to get neighbors of a cell
def get_neighbors(grid, i, j):
    neighbors = []
    if i > 0:
        neighbors.append(grid[i-1, j])  # Up
    if i < grid.shape[0]-1:
        neighbors.append(grid[i+1, j])  # Down
    if j > 0:
        neighbors.append(grid[i, j-1])  # Left
    if j < grid.shape[1]-1:
        neighbors.append(grid[i, j+1])  # Right
    return neighbors

# Function to simulate the nephron process
def simulate_nephron(grid, hydration, waste, glucose, aldosterone, adh):
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            # Get the neighbors of the current cell
            neighbors = get_neighbors(grid, i, j)
            # Each cell updates based on its current state and the metabolism parameters
            new_grid[i, j] = update_cell(grid[i, j], hydration, waste, glucose, aldosterone, adh, neighbors)
    return new_grid

# Set up the plot for animation
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, grid_size[1])
ax.set_ylim(0, grid_size[0])
ax.set_xlabel("Nephron Section")
ax.set_ylabel("Cell State")

# Initialize the grid (0 = Filtered, 1 = Reabsorbed, 2 = Excreted)
grid[0, 0] = 0  # Starting point, the fluid is filtered at the glomerulus
grid[-1, -1] = 2  # The final point excretes the fluid (excretion)

# Function to update the plot during the animation
def update_plot(t):
    global grid, hydration_level, waste_concentration, glucose_level, aldosterone_level, adh_level
    # Simulate changes in parameters (e.g., hydration, glucose, hormone levels)
    hydration_level = 0.5 + 0.1 * np.sin(t / 10)  # Simulate hydration changes
    glucose_level = 0.3 + 0.1 * np.sin(t / 12)  # Simulate glucose fluctuations
    aldosterone_level = 0.6 + 0.1 * np.sin(t / 15)  # Simulate aldosterone changes
    adh_level = 0.7 + 0.1 * np.sin(t / 20)  # Simulate ADH fluctuations

    grid = simulate_nephron(grid, hydration_level, waste_concentration, glucose_level, aldosterone_level, adh_level)

    # Plotting the current state of the nephron
    ax.clear()
    ax.set_xlim(0, grid_size[1])
    ax.set_ylim(0, grid_size[0])
    ax.set_xlabel("Nephron Section")
    ax.set_ylabel("Cell State")

    # Create the visual legend
    legend_elements = [
        Patch(facecolor=plt.cm.viridis(0/2), label='Filtered'),
        Patch(facecolor=plt.cm.viridis(1/2), label='Reabsorbed'),
        Patch(facecolor=plt.cm.viridis(2/2), label='Excreted'),
    ]
    ax.legend(handles=legend_elements, loc='upper right')

    # Display the grid with updated state
    ax.imshow(grid, cmap="viridis", aspect="auto", vmin=0, vmax=2)
    ax.set_title(f"Nephron Simulation - Timestep {t}")

# Create the animation
ani = animation.FuncAnimation(fig, update_plot, frames=timesteps, interval=200)
plt.show()
