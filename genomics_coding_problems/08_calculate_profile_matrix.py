# ---------
# Theory:
# ---------
# The profile matrix is a 4 x k matrix (where k is motif length) representing the frequency or probability
# of each nucleotide (A, C, G, T) at every position in a collection of motifs.
# It is used to identify the most conserved positions in a set of sequences.
#
# ------------------
# A Simple Example
# ------------------
# 1. Input: A set of motifs
# All motifs should be the same length. 
# Example:
# Let's consider below list as the input Motifs:
#   ATCCGA
#   ACCCGA
#   ATTCGA
#   ATCCGA
#   ATTCGA
#
# Motif length: 6
# Number of motifs: 5
#
# 2. Initialize a 4 x k matrix
# Where k is the length of each motif (6 in this case), and the rows correspond to nucleotides A, C, G, T.
# You can start with a count matrix (optionally with pseudocounts, e.g., add 1 to each count to avoid zero probabilities).

# 3. Count nucleotides at each position
# Go column by column and count how many times each base appears.
# For the example above:

# Position	A	C	G	T
# 1	        5	0	0	0
# 2	        0	0	0	5
# 3	        0	0	0	5
# 4	        0	5	0	0
# 5	        0	0	5	0
# 6	        5	0	0	0

# So the Count Matrix:
# A: [5, 0, 0, 0, 0, 5]
# C: [0, 0, 0, 5, 0, 0]
# G: [0, 0, 0, 0, 5, 0]
# T: [0, 5, 5, 0, 0, 0]

# 4. Convert to a Profile Matrix (optional step)
# Divide each count by the number of sequences (e.g., 5) to get the probabilities at each position.
# So the Profile Matrix becomes:
# A: [1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
# C: [0.0, 0.0, 0.0, 1.0, 0.0, 0.0]
# G: [0.0, 0.0, 0.0, 0.0, 1.0, 0.0]
# T: [0.0, 1.0, 1.0, 0.0, 0.0, 0.0]

# 🧠 Pro Tips
# Pseudocounts: Add 1 to each count to avoid 0 in probabilities (important for log-likelihood calculations).


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


if __name__ == "__main__":
    # Example test case
    motifs = [
        "ATGCA",
        "AAGCA",
        "ATGGA",
        "ATGCC"
    ]
    profile = calculate_profile_matrix(motifs)

    # Print profile matrix
    print("Profile Matrix:")
    for base in "ACGT":
        print(f"{base}: {profile[base]}")

    # Expected output (approximately):
    # A: [0.6, 0.4, 0.2, 0.2, 0.4]
    # C: [0.1, 0.1, 0.1, 0.1, 0.3]
    # G: [0.1, 0.1, 0.6, 0.4, 0.1]
    # T: [0.2, 0.4, 0.1, 0.3, 0.2]
