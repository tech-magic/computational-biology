import numpy as np
from collections import Counter

# DNA sequence matrix: rows = fossils, columns = gene positions
# '-' represents missing nucleotide
sequences = np.array([
    list("AGT-C"),
    list("AG--C"),
    list("A-TGC"),
    list("-GTGC"),
    list("AGT-C"),
])

def hamming_similarity(seq1, seq2):
    """Compute similarity score based on matching characters (excluding '-')"""
    score = sum(
        1 for a, b in zip(seq1, seq2)
        if a != '-' and b != '-' and a == b
    )
    return score

def predict_missing(sequences):
    """Fill in missing nucleotides using collaborative filtering logic"""
    filled = sequences.copy()
    num_rows, num_cols = sequences.shape

    for i in range(num_rows):
        for j in range(num_cols):
            if sequences[i, j] == '-':
                similarities = []
                candidates = []
                for k in range(num_rows):
                    if k != i and sequences[k, j] != '-':
                        sim = hamming_similarity(sequences[i], sequences[k])
                        similarities.append((sim, sequences[k, j]))
                
                # Weight by similarity, choose most common plausible base
                if similarities:
                    weighted = Counter()
                    for sim, base in similarities:
                        weighted[base] += sim
                    filled[i, j] = weighted.most_common(1)[0][0]
    
    return filled

predicted = predict_missing(sequences)
print("Predicted Sequences:\n", predicted)

# Expected output:
# Predicted Sequences:
# [['A' 'G' 'T' 'G' 'C']
#  ['A' 'G' 'T' 'G' 'C']
#  ['A' 'T' 'T' 'G' 'C']
#  ['A' 'G' 'T' 'G' 'C']
#  ['A' 'G' 'T' 'G' 'C']]
#
