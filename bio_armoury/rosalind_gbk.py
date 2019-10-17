from Bio import Entrez

f = open("rosalind_gbk.txt", "r")
lines = f.read().split("\n")
genus_name, start_date, end_date = lines[0], lines[1], lines[2]
f.close()

Entrez.email = "your_name@gmail.com"
handle = Entrez.esearch(db="nucleotide", term=f'"{genus_name}"[Organism] AND ("{start_date}"[PDAT] : "{end_date}"[PDAT])')
record = Entrez.read(handle)
print(record["Count"])