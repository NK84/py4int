lst = list()
counts = dict()
name = input("Enter file:")
handle = open(name)
for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        x = line[5:]
        z = x.find(" ")
        adr = x[:z]
        counts[adr] = counts.get(adr,0) + 1
for k,v in counts.items():
    lst.append((v,k))
lst.sort(reverse =True)
for v,k in lst[:1]:
	print (k,v)