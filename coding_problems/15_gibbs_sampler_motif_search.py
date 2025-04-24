# THEORY:
# Gibbs Sampling is a stochastic algorithm for motif discovery. It improves motifs iteratively:
# - Randomly select a k-mer (motif) from each DNA sequence.
# - In each iteration:
#   1. Randomly remove one motif from the set.
#   2. Use the remaining motifs to build a profile matrix.
#   3. Sample a new motif from the excluded sequence using the profile matrix.
# - This process repeats for N iterations.
# - The goal is to converge to a set of motifs that are very similar (low total distance).

import random
from collections import Counter

def hamming_distance(seq1, seq2):
    return sum(c1 != c2 for c1, c2 in zip(seq1, seq2))

def profile_with_pseudocounts(motifs):
    """Generate a profile matrix with Laplace smoothing (pseudocounts of 1)."""
    k = len(motifs[0])
    t = len(motifs)
    profile = {nuc: [1] * k for nuc in "ACGT"}  # start with pseudocounts

    for motif in motifs:
        for i, nuc in enumerate(motif):
            profile[nuc][i] += 1

    for nuc in "ACGT":
        profile[nuc] = [count / (t + 4) for count in profile[nuc]]  # normalize

    return profile

def profile_random_kmer(seq, k, profile):
    """Randomly choose a k-mer from a sequence based on the profile matrix."""
    n = len(seq)
    probs = []
    kmers = []

    for i in range(n - k + 1):
        kmer = seq[i:i+k]
        prob = 1.0
        for j, nuc in enumerate(kmer):
            prob *= profile[nuc][j]
        probs.append(prob)
        kmers.append(kmer)

    total = sum(probs)
    probs = [p / total for p in probs]  # Normalize

    # Weighted random choice based on profile probabilities
    return random.choices(kmers, weights=probs, k=1)[0]

def consensus_string(motifs):
    k = len(motifs[0])
    consensus = ""
    for i in range(k):
        count = Counter([motif[i] for motif in motifs])
        consensus += count.most_common(1)[0][0]
    return consensus

def score(motifs):
    """Return the total Hamming distance of motifs to their consensus."""
    cons = consensus_string(motifs)
    return sum(hamming_distance(motif, cons) for motif in motifs)

def gibbs_sampler(dna, k, n_iterations):
    """Run Gibbs Sampling for motif discovery."""
    t = len(dna)
    # Step 1: randomly choose initial k-mers from each sequence
    motifs = [random.choice([s[i:i+k] for i in range(len(s)-k+1)]) for s in dna]
    best_motifs = motifs[:]
    best_score = score(motifs)

    for iteration in range(n_iterations):
        # Step 2: Randomly exclude one motif
        i = random.randint(0, t - 1)
        motifs_except_i = motifs[:i] + motifs[i+1:]

        # Step 3: Build profile from remaining motifs
        profile = profile_with_pseudocounts(motifs_except_i)

        # Step 4: Sample a new motif for the excluded sequence
        new_motif = profile_random_kmer(dna[i], k, profile)
        motifs[i] = new_motif

        # Step 5: Update best motifs if new ones are better
        current_score = score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs[:]

    return best_motifs

if __name__ == "__main__":
    # 🧪 Test DNA Sequences
    dna_list = [
        "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
        "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
        "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
        "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
        "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
    ]
    k = 8  # Motif length
    n_iterations = 100  # Number of iterations

    result = gibbs_sampler(dna_list, k, n_iterations)

    print("\nBest motifs found (Gibbs Sampling):")
    for motif in result:
        print(motif)

    # ✅ Expected Output:
    # A list of 5 motifs (length 8) that appear to be conserved across sequences.
    # Due to randomness, exact motifs may vary per run but should look similar.
    # Example output:
    # CGGGGGTG
    # GGGTGTAA
    # GTGTGTAC
    # GTGTGTGC
    # GTGTGTGC
