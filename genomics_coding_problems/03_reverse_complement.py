# What is the reverse complement of GCTAGCT?
#
# Answer:
# AGCTAGC

def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reversed_dna = dna[::-1]
    return ''.join(complement[base] for base in reversed_dna)

# Sample input
input_dna = "AAAACCCGGT"
print(reverse_complement(input_dna))  # Output: ACCGGGTTTT
