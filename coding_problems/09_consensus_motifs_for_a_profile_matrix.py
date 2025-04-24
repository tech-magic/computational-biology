# ----------
# Question:
# ----------
# Consider the following profile matrix:
# A:  0.4  0.3  0.0  0.1  0.0  0.9
# C:  0.2  0.3  0.0  0.4  0.0  0.1
# G:  0.1  0.3  1.0  0.1  0.5  0.0
# T:  0.3  0.1  0.0  0.4  0.5  0.0

# Which of the following strings is a consensus string for this profile matrix?  (Select all that apply.)
# 1. AAGCTA
# 2. ATGCTA
# 3. ACGTTA
# 4. ACGTTT
# 5. TCGCGA
# 6. AGGTGA

# ------------------
# Correct Answers:
# ------------------
# 1. AAGCTA
# 3. ACGTTA
# 6. AGGTGA

# --------------
# Explanation:
# --------------
# To determine the consensus string from a profile matrix, we select the nucleotide with the highest frequency at each position (i.e., column).

# Let's go through each position (column) in the given matrix:

# Position:      1    2    3    4    5    6
# ------------------------------------------
# A:           0.4  0.3  0.0  0.1  0.0  0.9
# C:           0.2  0.3  0.0  0.4  0.0  0.1
# G:           0.1  0.3  1.0  0.1  0.5  0.0
# T:           0.3  0.1  0.0  0.4  0.5  0.0

# Now, pick the nucleotide with the highest value at each column:
#     Position 1: A (0.4)
#     Position 2: A/C/G all have 0.3 — so A, C, or G could be correct.
#     Position 3: G (1.0)
#     Position 4: C and T (0.4) — so C or T are acceptable
#     Position 5: G and T (0.5) — either is acceptable
#     Position 6: A (0.9)

# So, valid consensus strings must have:
#     Position 1: A
#     Position 2: A, C, or G
#     Position 3: G
#     Position 4: C or T
#     Position 5: G or T
#     Position 6: A
#

from itertools import product

# Profile matrix as a dictionary
profile = {
    'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
    'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
    'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
    'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0],
}

# Step 1: For each position, find the nucleotide(s) with the max probability
positions = list(zip(profile['A'], profile['C'], profile['G'], profile['T']))
nucleotides = ['A', 'C', 'G', 'T']

consensus_options = []
for pos in positions:
    max_val = max(pos)
    consensus_nucs = [nuc for nuc, val in zip(nucleotides, pos) if val == max_val]
    consensus_options.append(consensus_nucs)

# Step 2: Generate all possible consensus strings
all_consensus_strings = [''.join(p) for p in product(*consensus_options)]

# Given candidate strings
candidate_strings = [
    "AAGCTA",
    "ATGCTA",
    "ACGTTA",
    "ACGTTT",
    "TCGCGA",
    "AGGTGA",
]

# Step 3: Filter which candidates are valid consensus strings
valid_candidates = [s for s in candidate_strings if s in all_consensus_strings]

# Output
print("All possible consensus strings:")
print(all_consensus_strings)
print("\nMatching candidate strings:")
print(valid_candidates)
