with open("rosalind_gc.txt", "r") as f:
    raw_data = f.read().split(">")


db={}
raw_data = raw_data[1:]
raw_data = [i.replace("\n", "") for i in raw_data]
for data in raw_data:
	db[data[0:13]] = (data[13:].count("G") +data[13:].count("C")) / len(data[13:]) * 100

max_pair = max(zip(db.values(), db.keys()))
print(max_pair[1]+"\n"+str(max_pair[0]))

