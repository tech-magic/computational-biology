# Code Challenge: Solve the Pattern Matching Problem.

# Input: Two strings, Pattern and Genome.
# Output: A collection of space-separated integers specifying all starting positions where Pattern appears as a substring of Genome.
# Debug Datasets

# Sample Input:
# ATAT
# GATATATGCATATACTT

# Sample Output:
# 1 3 9

def pattern_matching(pattern, genome):
    positions = []
    pattern_length = len(pattern)
    genome_length = len(genome)

    for i in range(genome_length - pattern_length + 1):
        if genome[i:i + pattern_length] == pattern:
            positions.append(i)

    return positions

# Sample input
pattern = "ATAT"
genome = "GATATATGCATATACTT"

# Run and print output
result = pattern_matching(pattern, genome)
print(" ".join(map(str, result)))
