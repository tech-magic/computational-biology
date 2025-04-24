import numpy as np
import pandas as pd

class MultiOmicsCellularAutomaton:
    """
    A simple cellular automaton that integrates genomics, proteomics, and metabolomics data.
    Each cell in a 3x3 grid evolves based on the state of its neighbors and the influence of omics data.
    """

    def __init__(self, genomics_file, proteomics_file, metabolomics_file):
        # Load omics data from CSV files and set the index to the identifier column
        self.genomics = pd.read_csv(genomics_file).set_index("Gene")
        self.proteomics = pd.read_csv(proteomics_file).set_index("Protein")
        self.metabolomics = pd.read_csv(metabolomics_file).set_index("Metabolite")

        # Initialize a 3x3 grid representing cellular states (1 for active, 0 for inactive)
        self.state = np.random.choice([0, 1], size=(3, 3))

    def update_state(self):
        """
        Updates the state of each cell based on its neighbors and omics influence.
        - Neighbors are considered in a Moore neighborhood.
        - Influence is calculated from the average values in each omics dataset.
        """
        new_state = self.state.copy()
        for i in range(3):
            for j in range(3):
                # Extract the neighborhood (including current cell)
                neighbors = self.state[max(i-1, 0):min(i+2, 3), max(j-1, 0):min(j+2, 3)]
                active_neighbors = np.sum(neighbors) - self.state[i, j]

                # Omics influence scores (averaged for simplification)
                genomic_influence = self.genomics.ExpressionLevel.mean()
                proteomic_influence = self.proteomics.Abundance.mean()
                metabolomic_influence = self.metabolomics.Concentration.mean()

                # Rule: activate if at least 2 active neighbors or high omics influence
                if active_neighbors >= 2 or (genomic_influence + proteomic_influence + metabolomic_influence) > 4:
                    new_state[i, j] = 1
                else:
                    new_state[i, j] = 0
        self.state = new_state

    def run(self, steps=5):
        """
        Runs the simulation for the specified number of steps.
        Prints the grid state after each update.
        """
        print("Initial state:")
        print(self.state)
        for step in range(steps):
            self.update_state()
            print(f"State at step {step + 1}:")
            print(self.state)
