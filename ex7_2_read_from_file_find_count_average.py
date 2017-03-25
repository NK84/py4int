# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
pos = 0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        x = line.find(":")
        y = float(line[x+1:])
        pos = pos + 1
        count = count + y
aver = count / pos
print ("Average spam confidence:", aver)
