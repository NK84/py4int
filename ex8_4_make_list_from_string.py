fname = open("romeo.txt")
lst = list()
for line in fname:
    line = line.rstrip().split()
    for word in line:
        if word in lst:
            continue
        lst.append(word)
lst.sort()
print (lst)