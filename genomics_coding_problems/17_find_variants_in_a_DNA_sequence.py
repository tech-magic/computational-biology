from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

# Step 1: Generate reference and sample FASTA files
def write_fasta_files():
    # Reference sequence
    ref_seq = SeqRecord(Seq("ATCGGATTACAGGCT"), id="chr1", description="Reference sequence")
    SeqIO.write(ref_seq, "reference.fasta", "fasta")

    # Sample sequence with:
    # SNP at position 5 (T → G)
    # Insertion of 'TT' after position 8
    # Deletion of 'C' at position 13
    sample_seq = SeqRecord(Seq("ATCGGAGTTTACAGT"), id="chr1", description="Sample sequence")
    SeqIO.write(sample_seq, "sample.fasta", "fasta")

# Step 2: Compare sequences to find SNPs, insertions, deletions
def find_variants(ref, sample):
    variants = []
    i, j, pos = 0, 0, 1  # 1-based position
    while i < len(ref) and j < len(sample):
        if ref[i] == sample[j]:
            i += 1
            j += 1
            pos += 1
        elif i + 1 < len(ref) and j + 1 < len(sample) and ref[i+1] == sample[j+1]:
            # SNP
            variants.append((pos, ref[i], sample[j]))
            i += 1
            j += 1
            pos += 1
        elif sample[j:j+2] and ref[i] == sample[j+2:j+3]:
            # Insertion
            inserted = sample[j:j+2]
            variants.append((pos-1, ref[i-1], ref[i-1] + inserted))
            j += 2
        elif i + 1 < len(ref) and ref[i+1] != sample[j]:
            # Deletion
            del_seq = ref[i:i+2]
            variants.append((pos, del_seq, ref[i]))
            i += 1
            pos += 1
        else:
            # Fallback for unexpected mismatch
            variants.append((pos, ref[i], sample[j]))
            i += 1
            j += 1
            pos += 1
    return variants

# Step 3: Write variants to a VCF file
def write_vcf_file(variants):
    with open("variants.vcf", "w") as vcf:
        vcf.write("##fileformat=VCFv4.2\n")
        vcf.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n")
        for pos, ref_base, alt_base in variants:
            vcf.write(f"chr1\t{pos}\t.\t{ref_base}\t{alt_base}\t.\tPASS\t.\n")

# Main pipeline
def main():
    write_fasta_files()

    ref = str(SeqIO.read("reference.fasta", "fasta").seq)
    sample = str(SeqIO.read("sample.fasta", "fasta").seq)

    variants = find_variants(ref, sample)
    write_vcf_file(variants)

    print("FASTA and VCF files generated successfully.")

if __name__ == "__main__":
    main()
