

with open("rosalind_iev.txt", "r") as f:
    parental_phenotypes = f.read().strip().split(" ")

parental_phenotypes = list(map(int,parental_phenotypes))

expected_phenotype = [1, 1, 1, 0.75, 0.5, 0]

expected_num = sum([a*b for a,b in zip(parental_phenotypes,expected_phenotype)]) * 2

print(expected_num)