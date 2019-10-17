with open("rosalind_rna.txt", "r") as f:
    dna_seq = f.read()
rna_seq = ""
for nucleotide in dna_seq:
    if nucleotide == "T":
    	rna_seq += "U"
    else:
    	rna_seq += nucleotide

print(rna_seq)
