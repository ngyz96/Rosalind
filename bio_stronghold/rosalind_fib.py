with open("rosalind_fib.txt", "r") as f:
    values = f.read().strip("\n").split(" ")
    num_months = int(values[0])
    multiplier = int(values[1])

num_rabbits = 1
prev_num = 0
if num_months == 1:
    print(num_rabbits)
else:
    for i in range(num_months-1):
        num_rabbits, prev_num = num_rabbits+(prev_num*multiplier),num_rabbits     
print(num_rabbits)