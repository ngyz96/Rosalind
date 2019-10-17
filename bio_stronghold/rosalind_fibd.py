with open("rosalind_fibd.txt", "r") as f:
    values = f.read().strip("\n").split(" ")
    num_months = int(values[0])
    survival_rate = int(values[1])

num_rabbits = [0 for x in range(survival_rate)]
num_rabbits[0] = 1
if num_months == 1:
    print(sum(num_rabbits))
else:
    for i in range(1,num_months):
        new_rabbits = sum(num_rabbits[1:])
        num_rabbits[1:] = [num_rabbits[x] for x in range(survival_rate-1)]
        num_rabbits[0] = new_rabbits
        #print(num_rabbits)

print(sum(num_rabbits))