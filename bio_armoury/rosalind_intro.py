from Bio.Seq import Seq

f = open("rosalind_ini.txt", "r")
my_seq = Seq(f.read())
number = [my_seq.count(x) for x in ["A", "C", "G", "T"]]

for x in number:
	print(x, end=" ")
f.close()