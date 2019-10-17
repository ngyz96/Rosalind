f = open("rosalind_ini4.txt", "r")

lines = f.read()
values = lines.split()
values = [int(x) for x in values]
total = 0
for i in range(values[0], values[1] + 1):
	if (i % 2 == 1):
 		total += i
print(total)

f.close()