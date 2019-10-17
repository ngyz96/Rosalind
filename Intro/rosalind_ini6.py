f = open("rosalind_ini6.txt", "r")

lines = f.read().split()

dic = dict((x,lines.count(x)) for x in set(lines))
for key, value in dic.items():
	print(key, value)

f.close()