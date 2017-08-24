import re
count = 0
big = 0
first = input('Enter file: ')
x = open(first)
for line in x:
	line = line.rstrip()
	numb = re.findall('^New Rev.*: ([0-9]+)', line)
	if len(numb)>0: 
		for i in numb:
			big = big + float(i)
			count = count + 1
print(big/count)
