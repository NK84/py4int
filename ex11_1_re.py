import re
count = 0
y = input('Enter a regular expression: ')
x = open('mbox.txt')
for line in x:
	line= line.rstrip()
	if re.search(y, line):
		count = count+1
print('mbox.txt had', count, 'lines that matched', y)