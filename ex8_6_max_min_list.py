lst = list()
while True:
	x = input("Enter a number:")
	if x == "done":
		break
	lst.append(x)
maximum = max(lst)
minimum = min(lst)
print ("Maximum: ", maximum)
print ("Minimum: ", minimum)