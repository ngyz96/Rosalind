f = open("rosalind_ini5.txt", "r")

lines = f.readlines()
num_lines = len(lines)
output = open("rosalind_ini5_output.txt", "w+")

for i in range(1, num_lines + 1, 2):
	output.write(lines[i])

f.close()
output.close()