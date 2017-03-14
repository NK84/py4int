def computepay(h, r):
	if h > 40:
		s = (40 * r) + (h - 40) * (1.5 * r)
	else:
		s = h * r
	return s

try:
	hours = input ('How many hours? ')
	h = float(hours)
	rate = input ('What is your rate? ')
	r = float(rate)
	s = computepay(h,r)
	print ('You will be paid: ', s)
except:
	print ('Error! Enter a number')
	exit()


		
