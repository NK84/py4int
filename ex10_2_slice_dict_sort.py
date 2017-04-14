lst = list()
counts = dict()
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        x = line.find(":")
        z = x-2
        hour = line[z:x]
        counts[hour] = counts.get(hour,0) + 1
for k,v in counts.items():
    lst.append((k,v))
lst.sort()
for k,v in lst:
    print (k, v)