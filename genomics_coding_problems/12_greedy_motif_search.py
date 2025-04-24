# THEORY:
# Greedy motif search is a heuristic algorithm for motif discovery in biological sequences.
# It iteratively refines a motif by selecting the most likely k-mers from each sequence based on a profile matrix.
# This file includes the greedy motif search method, which finds a motif by selecting k-mers that maximize the motif's profile.

def calculate_profile_matrix(motifs, pseudocount=1):
    """
    Calculate the profile matrix from a list of motifs.
    Optionally add pseudocounts to avoid zero probabilities.

    :param motifs: List of strings, each string is a DNA motif of the same length.
    :param pseudocount: Integer, added to each count to prevent zero probabilities.
    :return: Dictionary with keys A, C, G, T mapping to lists of probabilities.
    """
    # Determine the length of motifs (all motifs are assumed to be of the same length)
    k = len(motifs[0])

    # Initialize a profile dictionary for A, C, G, T with pseudocounts to avoid zero probabilities
    profile = {base: [pseudocount] * k for base in "ACGT"}

    # Count the occurrences of each nucleotide at each position across all motifs
    for motif in motifs:
        for index, base in enumerate(motif):
            profile[base][index] += 1  # Increment the count of base at position 'index'

    # Compute the total number of sequences plus added pseudocounts at each position
    total = len(motifs) + 4 * pseudocount  # each position is normalized across all 4 bases

    # Convert counts to probabilities by dividing each count by the total at that position
    for base in profile:
        profile[base] = [count / total for count in profile[base]]

    return profile

def greedy_motif_search(dna_list, k, iterations=10):
    """
    Perform Greedy Motif Search to find a common motif in a set of DNA sequences.

    :param dna_list: List of DNA sequences
    :param k: Length of motif
    :param iterations: Number of iterations to refine the motif
    :return: Final motif list
    """
    # Randomly initialize the motif by selecting the first k-mer of each DNA sequence
    motifs = [seq[:k] for seq in dna_list]  # Initialize with the first k-mer from each sequence

    for _ in range(iterations):
        # Calculate profile matrix based on current motifs
        profile = calculate_profile_matrix(motifs)

        # Update motifs by choosing the best matching k-mers from each sequence
        motifs = []
        for seq in dna_list:
            max_prob = -1
            best_kmer = seq[:k]  # Initialize with the first k-mer
            for i in range(len(seq) - k + 1):
                kmer = seq[i:i + k]
                prob = 1
                for j, base in enumerate(kmer):
                    prob *= profile[base][j]
                if prob > max_prob:
                    max_prob = prob
                    best_kmer = kmer
            motifs.append(best_kmer)

    return motifs

if __name__ == "__main__":
    # Example test case
    dna_list = [
        "AGCTAGCAGT",
        "TGCATGCAGT",
        "AGCTTGCAGT",
        "TGCTAGCAGT"
    ]
    k = 3
    motifs = greedy_motif_search(dna_list, k, iterations=5)

    # Print found motifs
    print("Motifs from Greedy Search:")
    for motif in motifs:
        print(motif)

    # Expected output: 
    # A consistent set of motifs such as ['AGC', 'TGC', 'AGC', 'TGC'],
    # depending on the randomness in motif initialization.
