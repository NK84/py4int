hours = input ('How many hours? ')
rate = input ('What is your rate? ')
try:
	h = float(hours)
	r = float(rate)
except:
	h = -1
if h > 40:
	s = (40 * r) + (h - 40) * (1.5 * r)
	print ('You will be paid: ', s)
elif 0 <= h <= 40:
	s = h * r
	print ('You will be paid: ', s)
else:
	print ('Error! Input numbers')
