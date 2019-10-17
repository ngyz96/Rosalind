with open("rosalind_hamm.txt", "r") as f:
    raw_data = f.read().strip().split("\n")

seq_1, seq_2 = raw_data[0], raw_data[1]
hamming_dist = 0
for x, y in zip(seq_1, seq_2):
	if x!= y:
		hamming_dist+=1
	else:
		pass
print(hamming_dist)