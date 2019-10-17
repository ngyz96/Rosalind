f = open("rosalind_fibo.txt", "r")

num = int(f.read())

def fibo(x):
	term1 = 0
	term2 = 1

	if (x <= 0):
		raise ValueError('Number must be more than 0!')
	elif (x == 0):
		return(term1)
	elif (num == 1):
		return(term2)
	else:
		for i in range(2,x+1):
			term1, term2 = term2, term1+term2
		return(term2)

print(fibo(num))
f.close()