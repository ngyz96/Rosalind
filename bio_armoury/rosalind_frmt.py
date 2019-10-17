from Bio import Entrez, SeqIO

with open("rosalind_frmt.txt", "r") as f:
    genes = f.read().strip("\n").split(" ")
    #print(genes)

Entrez.email = "your@gmail.com"
handle = Entrez.efetch(db="nucleotide", id=genes, rettype="fasta")
records = list(SeqIO.parse(handle,"fasta"))

length = []
for x in records:
    length.append(len(x.seq))
shortest = length.index(min(length))
print(records[shortest].format("fasta"))