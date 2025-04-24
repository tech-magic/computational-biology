# THEORY:
# Expectation Maximization (EM) is an iterative method used for estimating parameters in probabilistic models.
# For motif finding, EM alternates between assigning probabilities (Expectation) and refining the motif profile (Maximization).
# This script implements a simplified EM algorithm to identify a common motif in a list of DNA sequences.

import random

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

def random_kmers(dna_list, k):
    """Randomly select one k-mer from each DNA sequence."""
    return [seq[random.randint(0, len(seq) - k):][:k] for seq in dna_list]


def expectation_step(dna_list, k, profile):
    """Compute most probable k-mers based on current profile (Expectation step)."""
    motifs = []
    for seq in dna_list:
        max_prob = -1
        best_kmer = seq[0:k]
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


def em_motif_finder(dna_list, k, iterations=10):
    """
    EM motif finder: find common motifs in sequences using EM algorithm.

    :param dna_list: List of DNA sequences
    :param k: Motif length
    :param iterations: Number of EM iterations to perform
    :return: Final motif list
    """
    motifs = random_kmers(dna_list, k)  # Step 0: Initialize with random k-mers

    for _ in range(iterations):
        profile = calculate_profile_matrix(motifs)
        motifs = expectation_step(dna_list, k, profile)

    return motifs


if __name__ == "__main__":
    # DNA test sequences
    dna_list = [
        "AGCTAGCAGT",
        "TGCATGCAGT",
        "AGCTTGCAGT",
        "TGCTAGCAGT"
    ]
    k = 3
    motifs = em_motif_finder(dna_list, k, iterations=5)

    print("Motifs from EM:")
    for motif in motifs:
        print(motif)

    # Expected result:
    # Should return a consistent set of 3-mers such as ['AGC', 'TGC', 'AGC', 'TGC'] or similar,
    # depending on random initialization.
