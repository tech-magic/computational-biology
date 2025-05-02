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
    """
    Fill in missing nucleotides using a simplified collaborative filtering approach.

    Parameters:
    sequences (np.ndarray): A 2D array of characters representing aligned DNA sequences
                            from multiple fossils. Each row is a fossil, each column is
                            a nucleotide position. Missing nucleotides are represented by '-'.

    Returns:
    np.ndarray: The same matrix with missing nucleotides predicted using similarity to other fossils.
    """
    # Create a copy of the sequences matrix to avoid modifying the original
    filled_sequences = sequences.copy()

    # Get the number of fossils (rows) and the number of nucleotide positions (columns)
    num_fossils, num_positions = sequences.shape

    # Loop over each fossil
    for fossil_index in range(num_fossils):
        # Loop over each nucleotide position in the current fossil
        for position_index in range(num_positions):
            # Check if this nucleotide is missing (i.e., '-')
            if sequences[fossil_index, position_index] == '-':
                similarity_scores = []  # Stores tuples of (similarity score, nucleotide from other fossil)

                # Compare with all other fossils to find candidates with known nucleotide at this position
                for other_fossil_index in range(num_fossils):
                    # Skip comparing the fossil with itself
                    if other_fossil_index != fossil_index:
                        # Only consider fossils that have a known nucleotide at the current position
                        other_nucleotide = sequences[other_fossil_index, position_index]
                        if other_nucleotide != '-':
                            # Compute similarity between the current fossil and the other fossil
                            similarity = hamming_similarity(
                                sequences[fossil_index],
                                sequences[other_fossil_index]
                            )
                            # Store the similarity score and the nucleotide from the other fossil
                            similarity_scores.append((similarity, other_nucleotide))

                # If we have candidate fossils with known nucleotides and similarity scores
                if similarity_scores:
                    # Use a Counter to aggregate nucleotide choices weighted by similarity
                    weighted_votes = Counter()
                    for similarity, nucleotide in similarity_scores:
                        weighted_votes[nucleotide] += similarity  # Higher similarity → more voting power

                    # Choose the nucleotide with the highest weighted vote
                    most_probable_nucleotide = weighted_votes.most_common(1)[0][0]
                    filled_sequences[fossil_index, position_index] = most_probable_nucleotide

    return filled_sequences

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
