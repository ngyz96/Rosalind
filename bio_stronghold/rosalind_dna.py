with open("rosalind_dna.txt", "r") as f:
    dna_seq = f.read()

count = [0,0,0,0]
for nucleotide in dna_seq:
    if nucleotide == "A":
        count[0] += 1
    elif nucleotide == "C":
        count[1] += 1
    elif nucleotide == "G":
        count[2] += 1
    elif nucleotide == "T":
        count[3] += 1
    else:
        pass

for number in count:
    print(number, end=" ")