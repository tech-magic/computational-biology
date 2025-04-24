# Find the most frequent 3-mer (substring of length 3) in the DNA sequence:
# CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT
#
# Answer:
# Most frequent 3-mer(s): ['CCT']
# Frequency: 4

from Bio.Seq import Seq
from collections import Counter

# Define the sequence
sequence = Seq("CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT")

# Set the k-mer length
k = 3

# Generate all 3-mers
kmers = [str(sequence[i:i+k]) for i in range(len(sequence) - k + 1)]

# Count frequencies
kmer_counts = Counter(kmers)

# Find the maximum frequency
max_freq = max(kmer_counts.values())

# Extract most frequent 3-mers
most_frequent = [kmer for kmer, count in kmer_counts.items() if count == max_freq]

# Output
print(f"Most frequent 3-mer(s): {most_frequent}")
print(f"Frequency: {max_freq}")
