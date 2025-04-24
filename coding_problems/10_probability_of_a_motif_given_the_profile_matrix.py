# Consider the following profile matrix Profile:
# A:  0.4  0.3  0.0  0.1  0.0  0.9
# C:  0.2  0.3  0.0  0.4  0.0  0.1
# G:  0.1  0.3  1.0  0.1  0.5  0.0
# T:  0.3  0.1  0.0  0.4  0.5  0.0

# Compute Pr(AAGTTC|Profile). (Express your answer as a decimal and do not round your answer.)

# To compute the probability of the DNA string "AAGTTC" given the profile matrix, you multiply the corresponding probabilities for each nucleotide at each position.

# Given DNA string: AAGTTC
# Length: 6

# We map each base in "AAGTTC" to the corresponding column in the matrix:
#     Position 1: A → Profile['A'][0] = 0.4
#     Position 2: A → Profile['A'][1] = 0.3
#     Position 3: G → Profile['G'][2] = 1.0
#     Position 4: T → Profile['T'][3] = 0.4
#     Position 5: T → Profile['T'][4] = 0.5
#     Position 6: C → Profile['C'][5] = 0.1

# Now multiply all of them:
# Pr(AAGTTC∣Profile) = 0.4×0.3×1.0×0.4×0.5×0.1 = 0.0024

# DNA string
dna = "AAGTTC"

# Profile matrix as a dictionary of lists
profile = {
    'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
    'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
    'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
    'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0],
}

# Compute the probability
prob = 1.0
for i, base in enumerate(dna):
    prob *= profile[base][i]

# Output the result
print(f"Pr({dna}|Profile) = {prob}")
