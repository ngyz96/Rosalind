with open("rosalind_iprb.txt", "r") as f:
    raw_data = f.read().strip().split(" ")

domi, hetero, rece = int(raw_data[0]), int(raw_data[1]), int(raw_data[2])
total = rece + domi + hetero

prob = 1 - ((rece)/(total)*(rece-1)/(total-1) 
	+ (rece)/(total)*(hetero)/(total-1)
	+ (hetero)/(total)*(hetero-1)/(total-1)*1/4)
print(prob)