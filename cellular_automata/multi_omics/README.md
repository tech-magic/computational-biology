# Multi-Omics Cellular Automata Simulation

This project simulates biological interactions using a Cellular Automata (CA) model
with data from genomics, proteomics, and metabolomics layers.

Each cell in the grid represents a biological unit, whose state evolves based on neighbor states and influence from real biological data. Omics data is read from standard CSV formats.

## Files

- `data/genomics_data.csv`: Gene expression data.
- `data/proteomics_data.csv`: Protein abundance data.
- `data/metabolomics_data.csv`: Metabolite concentration data.
- `ca/automaton.py`: Main simulation script.

## How to Run

Install dependencies:

```bash
pip install numpy pandas
```

Run the simulation by importing the class and calling `run()`:

```python
from ca.automaton import MultiOmicsCellularAutomaton

ca = MultiOmicsCellularAutomaton(
    "data/genomics_data.csv",
    "data/proteomics_data.csv",
    "data/metabolomics_data.csv"
)
ca.run(steps=5)
```
