# Use words.txt as the file name
fname = input("Enter file name: ")
fhnew = open(fname)
for line in fhnew:
	line = line.rstrip()
	print (line.upper())
	
