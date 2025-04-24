# Compute the Hamming distance between "TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC" and
# "GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA".
#
# Answer is 50.
#

def hamming_distance(str1, str2):
    # Check if the lengths of the strings are the same
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")
    
    # Compute the number of differing positions
    distance = sum(1 for a, b in zip(str1, str2) if a != b)
    
    return distance

# DNA sequences
seq1 = "TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC"
seq2 = "GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA"

# Compute the Hamming distance
try:
    distance = hamming_distance(seq1, seq2)
    print(f"The Hamming distance is: {distance}")
except ValueError as e:
    print(e)
