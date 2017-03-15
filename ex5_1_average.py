total = 0
count = 0
while True:
	num = input("Enter a number: ")
	if num == "done" :
		break
	try:
		num = int(num)
		count = count + 1
		total = total + num
		continue
	except:
		print ("Invalid input")
		continue
print (total, count, total / count)
