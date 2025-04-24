# Which of the following RNA strings could translate into the amino acid string PRTEIN? (Select all that apply.)
# 1. CCCAGGACUGAGAUCAAU
# 2. CCGAGGACCGAAAUCAAC
# 3. CCCAGUACCGAAAUUAAC
# 4. CCAAGUACAGAGAUUAAC

# Correct Answers:
# 1. CCCAGGACUGAGAUCAAU
# 2. CCGAGGACCGAAAUCAAC

# Define the standard codon table (RNA to amino acids)
codon_table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

# List of RNA sequences
rna_sequences = [
    "CCCAGGACUGAGAUCAAU",
    "CCGAGGACCGAAAUCAAC",
    "CCCAGUACCGAAAUUAAC",
    "CCAAGUACAGAGAUUAAC"
]

# Target amino acid sequence
target = "PRTEIN"

# Function to translate mRNA to protein
def translate_rna(rna):
    protein = ""
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        amino_acid = codon_table.get(codon, "?")
        protein += amino_acid
    return protein

# Check which RNA strings match the target protein
for rna in rna_sequences:
    protein = translate_rna(rna)
    print(f"RNA: {rna} → Protein: {protein} → Match: {protein == target}")


