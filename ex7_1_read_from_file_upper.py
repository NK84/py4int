# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fhnew = fh.read()
for line in fhnew:
    fhnew = fhnew.rstrip()
print (fhnew.upper())
