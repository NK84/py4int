fname = input("Enter file name: ")
if fname == "na na boo boo":
	print ("NA NA BOO BOO TO YOU - You have been punk'd!")
	exit()
try:
	fh = open(fname)
except:
	print ("File cannot be opened: ", fname)
	exit()
count = 0
for line in fh:
    count = count + 1
print ("There were ", count,  "subject lines in ", fname)
