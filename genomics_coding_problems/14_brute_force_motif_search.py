# THEORY:
# Brute Force Motif Search guarantees finding the best motifs by evaluating every possible
# combination of k-mers (substrings) across the input DNA sequences.
# It chooses the combination that minimizes the total Hamming distance from a consensus sequence.

from itertools import product

def hamming_distance(seq1, seq2):
    """Calculate the number of differences between two sequences (Hamming distance)."""
    return sum(base1 != base2 for base1, base2 in zip(seq1, seq2))

def consensus_string(motifs):
    """Return the most common base at each position (consensus of motifs)."""
    k = len(motifs[0])
    consensus = ""
    for i in range(k):
        count = {base: 0 for base in "ACGT"}
        for motif in motifs:
            count[motif[i]] += 1
        consensus += max(count, key=count.get)
    return consensus

def total_distance(motifs):
    """Sum of Hamming distances of motifs to the consensus string."""
    consensus = consensus_string(motifs)
    return sum(hamming_distance(motif, consensus) for motif in motifs)

def brute_force_motif_search(dna_list, k):
    """
    Brute-force motif search that tries every k-mer combination from all DNA sequences.

    :param dna_list: List of DNA sequences
    :param k: Length of the motif
    :return: List of best motif k-mers (one from each sequence)
    """
    # Generate all possible k-mers for each sequence
    all_kmers = [
        [seq[i:i+k] for i in range(len(seq) - k + 1)]
        for seq in dna_list
    ]

    best_motifs = None
    min_distance = float('inf')

    # Try all combinations of one k-mer from each sequence using Cartesian product
    for motif_combination in product(*all_kmers):
        dist = total_distance(motif_combination)
        if dist < min_distance:
            min_distance = dist
            best_motifs = motif_combination

    return best_motifs


if __name__ == "__main__":
    # Test case
    dna_list = [
        "AGCTAGCAGT",
        "TGCATGCAGT",
        "AGCTTGCAGT",
        "TGCTAGCAGT"
    ]
    k = 3

    best_motifs = brute_force_motif_search(dna_list, k)

    print("Best Motifs (Brute Force):")
    for motif in best_motifs:
        print(motif)

    # ✅ Expected output: A set of k-mers (length 3) that have the minimum total distance
    # from their consensus. For example, something like:
    # ['AGC', 'TGC', 'AGC', 'TGC']
    # (Depends on actual contents of input)
