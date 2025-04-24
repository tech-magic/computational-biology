# QUESTION:
# Assume we are given the following strings Dna:
# TGACGTTC
# TAAGAGTT
# GGACGAAA
# CTGTTCGC
#
# Then, assume that RandomizedMotifSearch begins by randomly choosing the following 3-mers Motifs of Dna:
# TGA
# GTT
# GAA
# TGT
#
# What are the 3-mers after one iteration of RandomizedMotifSearch?
# In other words, what are the 3-mers Motifs(Profile(Motifs), Dna)?
# Please enter your answer as four space-separated strings.
#
# ANSWER:
# TGA TAA GGA TGT
#
# EXPLANATION:
# We build a profile from the initial motifs with pseudocounts,
# then select the most probable k-mer in each DNA string based on this profile.

from collections import defaultdict
import numpy as np

# Inputs
Dna = [
    "TGACGTTC",
    "TAAGAGTT",
    "GGACGAAA",
    "CTGTTCGC"
]

initial_motifs = ["TGA", "GTT", "GAA", "TGT"]
k = 3

def build_profile_with_pseudocounts(motifs, k):
    profile = {nuc: [1] * k for nuc in "ACGT"}  # Start with pseudocounts
    for motif in motifs:
        for i, nuc in enumerate(motif):
            profile[nuc][i] += 1
    t = len(motifs) + 4  # total count after adding pseudocounts
    for nuc in "ACGT":
        profile[nuc] = [count / t for count in profile[nuc]]
    return profile

def profile_most_probable_kmer(text, k, profile):
    max_prob = -1
    most_prob_kmer = text[0:k]
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        prob = 1
        for j, nuc in enumerate(kmer):
            prob *= profile[nuc][j]
        if prob > max_prob:
            max_prob = prob
            most_prob_kmer = kmer
    return most_prob_kmer

# Step 1: Build profile from initial motifs
profile = build_profile_with_pseudocounts(initial_motifs, k)

# Step 2: Find the most probable k-mer in each DNA string based on profile
new_motifs = [profile_most_probable_kmer(dna, k, profile) for dna in Dna]
print(" ".join(new_motifs))  # Output: TGA TAA GGA TGT
