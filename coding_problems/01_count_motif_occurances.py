# Compute Count(ACTGTACGATGATGTGTGTCAAAG, TGT)
#
# Answer:
# 4 (we have to find overlapping occurances of TGT)

from Bio.Seq import Seq

def count_motif(sequence: str, motif: str) -> int:
    """
    Count overlapping occurrences of a motif in a sequence using Biopython's Seq object.
    """
    seq = Seq(sequence)
    count = 0
    for i in range(len(seq) - len(motif) + 1):
        if seq[i:i+len(motif)] == motif:
            count += 1
    return count

# Example usage
sequence = "ACTGTACGATGATGTGTGTCAAAG"
motif = "TGT"
result = count_motif(sequence, motif)

print(f"The motif '{motif}' occurs {result} times in the sequence.")
