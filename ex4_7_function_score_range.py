def computegrade(s):
	if s < 0.0:
		print ("Bad score")
	elif s > 1.0:
		print("Bad score")
	elif s > 0.9:
		print("A")
	elif s > 0.8:
		print("B")
	elif s > 0.7:
		print("C")
	elif s > 0.6:
		print("D")
	elif s <= 0.6:
		print("F")

score = input("Enter score: ")
try:
	s = float(score)
	computegrade(s)
except:
	print ("Bad score")