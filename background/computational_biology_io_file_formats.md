
# 🧬 Computational Biology I/O File Format Cheatsheet

This cheatsheet includes examples and field explanations for the most commonly used file formats in computational biology.

---

## 🧬 1. Sequence Data

### **FASTA (.fasta, .fa)**

```
>seq1 description here
ATGCGTACGTAGCTAGCTAGCTAGCTA
```

- `>`: Starts the header line.
- `seq1`: Sequence ID.
- `ATGC...`: Nucleotide or protein sequence.

---

### **FASTQ (.fastq, .fq)**

```
@SEQ_ID
GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAAT
+
!''*((((***+))%%%++)(%%%%).1***-+*''))**
```

- `@SEQ_ID`: Sequence identifier.
- Second line: Raw sequence.
- `+`: Separator (can include ID).
- Fourth line: ASCII-encoded quality scores.

---

### **VCF (.vcf)**

```
##fileformat=VCFv4.2
#CHROM POS ID REF ALT QUAL FILTER INFO
chr1  10177  rs367896724  A  AC  100  PASS  AC=1;AF=0.425
```

- `CHROM`: Chromosome.
- `POS`: Position.
- `ID`: Variant ID.
- `REF/ALT`: Reference and alternate alleles.
- `QUAL`: Quality score.
- `FILTER`: Filter status.
- `INFO`: Additional info.

---

### **GFF (.gff) / GTF (.gtf)**

```
chr1  HAVANA  gene  11869  14409  .  +  .  gene_id "ENSG00000223972"; gene_name "DDX11L1";
```

- `chr1`: Sequence name.
- `HAVANA`: Source.
- `gene`: Feature type.
- `11869 14409`: Start and end.
- `+`: Strand.
- `gene_id`, `gene_name`: Attributes.

---


