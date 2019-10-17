with open("rosalind_revc.txt", "r") as f:
    dna_seq = f.read()

revc_seq = ""

for nucleotide in reversed(dna_seq):
    if nucleotide == "A":
        revc_seq += "T"
    elif nucleotide == "T":
        revc_seq += "A"
    elif nucleotide == "G":
        revc_seq += "C"
    elif nucleotide == "C":
        revc_seq += "G"
    else:
        pass

print(revc_seq)