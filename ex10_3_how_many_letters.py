lst = list()
counts = dict()
name = input("Enter file:")
handle = open(name)
for line in handle:
    line = line.rstrip().lower()
    for i in line:
    	try:
    		x = i.isalpha()
    		if x is True:
    			counts[i] = counts.get(i,0) + 1
    	except:
    		continue
for key,val in counts.items():
	lst.append((val,key))
lst.sort(reverse=True)
for val,key in lst:
	print(key,val)