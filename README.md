
# 🧬 Computational Biology & Cellular Automata Project

Welcome to an integrated project exploring **computational biology**, **multi-omics data modeling**, and **cellular automata (CA)** simulations across various biological systems. This repository includes theoretical foundations, problem-solving scripts, and simulation engines for genomics, nephrology, and personalized Ayurveda.

---

## 📁 Project Structure

```
├── background/                    # Theory and reference documents
├── cellular_automata/            # CA-based simulations in bio systems
├── genomics_coding_problems/     # Python-based coding challenges in genomics
└── README.md                     # You're here!
```

---

## 📚 1. Background

This section provides theoretical foundations and algorithmic guides for understanding computational biology.

### Files:
- `cellular_automata_basics.md`  
  Intro to basic concepts of cellular automata for computational applications.

- `computational_biology_basic_concepts.md`  
  Intro to molecular biology concepts for computational applications.

- `computational_biology_io_file_formats.md`  
  Overview of key bioinformatics file formats like FASTA, FASTQ, VCF, etc.

- `profile_matrix_and_motif_search_algorithms.md`  
  Detailed explanation of motif search strategies (used in `genomics_coding_problems`).

---

## 🧬 2. Genomics Coding Problems

Python scripts solving practical problems in genomics. Ideal for hands-on practice, assignments, or interviews.

### Topics Include:
- Motif finding, profile matrix, consensus sequence
- Hamming distance, reverse complements
- Randomized, Greedy, Gibbs Sampling, EM motif search

### Quick Start:
```bash
cd genomics_coding_problems
python 01_count_motif_occurances.py
```

Each file is self-contained and documented.

---

## 🧪 3. Cellular Automata Applications

Using CA to simulate and model biological systems in various domains.

### Modules:

#### 🔬 `multi_omics/`
Simulates biological systems using omics data (genomics, proteomics, metabolomics).
- `automaton.py` — Core CA logic
- `data/*.csv` — Omics datasets
- `README.md` — Documentation

#### 🧫 `nephrons/`
Simulates nephron behavior using CA.
- `simulating_nephrons.py`
- `README.md`

#### 🌿 `personalized_ayurveda/`
Models Ayurvedic medicine personalization with CA logic.
- `ayurvedic_ca.py`
- `README.md`

## 📄 License

MIT License.

---

## 🙌 Acknowledgements

Inspired by coursework in computational biology, synthetic biology modeling, and multi-omics data integration.

---

## 🔗 Related

- [Rosalind Coding Problems](http://rosalind.info/)
- [BioPython](https://biopython.org/)
- [NetLogo for CA](https://ccl.northwestern.edu/netlogo/)
