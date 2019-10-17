f = open("rosalind_ini3.txt", "r")

lines = f.readlines()
sentence = lines[0]
nums = lines[1].split()
nums = [int(x) for x in nums]
first = sentence[nums[0]:nums[1]+1]
second = sentence[nums[2]:nums[3]+1]
print(first, second)
f.close()