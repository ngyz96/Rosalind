with open("rosalind_subs.txt", "r") as f:
    data = f.read().strip().split("\n")

dna_seq, substring = data[0], data[1]

if len(dna_seq) > len(substring):
	locations = [x+1 for x in range(len(dna_seq)) if dna_seq.find(substring, x) == x]

	for location in locations:
		print(location, end=" ")
