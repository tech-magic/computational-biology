# Identify the value of i for which the skew array of "GATACACTTCCCGAGTAGGTACTG" attains a minimum value.
# Report the position of the first occurrence only, with 1-based numeration (i.e. Skew[1] corresponds to "G" here)

# Answer:
# Minimum GC skew score is -4 at position 12 (indexes in the motif start from 1)
#

def find_minimum_skew(dna_sequence):
    # Initialize variables for G and C counts
    g_count = 0
    c_count = 0
    min_skew = float('inf')  # Start with a very high value
    min_position = -1
    
    # Iterate through the DNA sequence
    for i in range(len(dna_sequence)):
        if dna_sequence[i] == 'G':
            g_count += 1
        elif dna_sequence[i] == 'C':
            c_count += 1
        
        # Calculate the current skew
        current_skew = g_count - c_count
        
        # If the current skew is the minimum encountered so far
        if current_skew < min_skew:
            min_skew = current_skew
            min_position = i + 1  # 1-based index
    
    return min_position

# DNA sequence input
dna_sequence = "GATACACTTCCCGAGTAGGTACTG"

# Find the position of the first occurrence of the minimum skew
min_skew_position = find_minimum_skew(dna_sequence)
print(f"The position of the first occurrence of the minimum skew is: {min_skew_position}")
