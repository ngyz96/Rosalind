from Bio import ExPASy, SwissProt

f = open("rosalind_dbpr.txt", "r")
prot_name = f.read().split("\n")
f.close()
#print(prot_name[0])
handle = ExPASy.get_sprot_raw(prot_name[0])
record = SwissProt.read(handle)

go = list(filter(lambda x: x[0] == 'GO', record.cross_references))
for x in go:
	if x[2][0] == "P":
		print(x[2][2:])