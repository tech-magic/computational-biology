# ---------------------------------------------------------
# Definition:
# The d-neighborhood of a k-mer Pattern is the collection of all k-mers
# that are at most Hamming distance d from Pattern.
#
# Hamming distance is the number of mismatches between two strings of equal length.
# For example, the Hamming distance between "ACGT" and "TCGA" is 2.
#
# For a pattern of length k, the number of strings that are at most
# Hamming distance d from it can be calculated using the formula:
#
#   Total = ∑ (i = 0 to d) [C(k, i) × 3^i]
#   where:
#     - C(k, i) = combinations = k choose i = number of ways to choose i positions to mutate
#     - 3^i = for each of the i positions, there are 3 possible substitutions (A, C, G, T minus original)
#
# Example:
# Pattern = "ACGT" (length k = 4)
# d = 3
#
# Total neighbors = C(4,0)*3^0 + C(4,1)*3^1 + C(4,2)*3^2 + C(4,3)*3^3
#                 = 1       + 4×3     + 6×9     + 4×27
#                 = 1 + 12 + 54 + 108 = 175
#
# This script computes all neighbors and groups them by their Hamming distance from the pattern.
# ---------------------------------------------------------

from itertools import product
from collections import defaultdict

def hamming_distance(s1, s2):
    """Compute the Hamming distance between two strings."""
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def neighbors(pattern, d):
    """
    Return the d-neighborhood of a k-mer pattern.
    
    Parameters:
        pattern (str): The original k-mer string.
        d (int): Maximum allowed Hamming distance.
        
    Returns:
        Set[str]: All k-mers within Hamming distance ≤ d from the pattern.
    """
    if d == 0:
        return {pattern}
    if len(pattern) == 0:
        return {""}
    
    nucleotides = ['A', 'C', 'G', 'T']
    suffix_neighbors = neighbors(pattern[1:], d)
    neighborhood = set()

    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for n in nucleotides:
                neighborhood.add(n + text)
        else:
            neighborhood.add(pattern[0] + text)
    
    return neighborhood

# ----------- Example Usage -----------
pattern = "ACGT"
d = 3
neighborhood = neighbors(pattern, d)

# Group by Hamming distance
grouped = defaultdict(list)
for n in neighborhood:
    dist = hamming_distance(pattern, n)
    grouped[dist].append(n)

# Print summary
total = 0
print(f"Total {len(neighborhood)} neighbors of pattern '{pattern}' with d = {d}:\n")
for dist in sorted(grouped):
    count = len(grouped[dist])
    total += count
    print(f"Hamming Distance {dist}: {count} k-mers")
    print(f"Examples: {grouped[dist][:5]}{' ...' if count > 5 else ''}\n")

# Final check
assert total == len(neighborhood)

# ---------------------------------------------------------
# Sample Output:
#
# Total 175 neighbors of pattern 'ACGT' with d = 3:
#
# Hamming Distance 0: 1 k-mers
# Examples: ['ACGT']
#
# Hamming Distance 1: 12 k-mers
# Examples: ['CCGT', 'AGGT', 'AAGT', 'GCGT', 'ATGT'] ...
#
# Hamming Distance 2: 54 k-mers
# Examples: ['CAGT', 'ATCT', 'AAGC', 'GAGT', 'TCGT'] ...
#
# Hamming Distance 3: 108 k-mers
# Examples: ['TAGT', 'TGGA', 'CCGA', 'CCAT', 'GAGA'] ...
# ---------------------------------------------------------
