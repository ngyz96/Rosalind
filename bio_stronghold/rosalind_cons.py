import numpy as np

with open("rosalind_cons.txt","r") as f:
    lines = f.read()

lines = lines.replace("\n", "").split(">")[1:]
dna_string = [seq[13:] for seq in lines]

seq_length = len(dna_string[0])
num_seq = len(dna_string)
profile = np.zeros((4,seq_length), dtype=int)

for seq in dna_string:
    for i in range(seq_length):
        base = seq[i]
        if base == "A":
            profile[0,i] += 1
        elif base == "C":
            profile[1,i] += 1
        elif base == "G":
            profile[2,i] += 1
        elif base == "T":
            profile[3,i] += 1



consensus = np.argmax(profile, axis=0)
for base in consensus:
    if base == 0:
        print("A", end="")
    elif base == 1:
        print("C", end="")
    elif base == 2:
        print("G", end="")
    elif base == 3:
        print("T", end="")

print("\n")
print("A: ", end='')
for i in profile[0]:
    print(i, end=" ")
print("\n")
print("C: ", end='')
for i in profile[1]:
    print(i, end=" ")
print("\n")
print("G: ", end='')
for i in profile[2]:
    print(i, end=" ")
print("\n")
print("T: ", end='')
for i in profile[3]:
    print(i, end=" ")




