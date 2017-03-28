data = input("Enter file name: ")
fh = open(data)
count = 0
for line in fh:
	line = line.rstrip()
	if line.startswith("From "):
		lst = line.split()
		x = lst[1]
		print (x)
		count = count + 1
print ("There were",  count, "lines in the file with From as the first word")