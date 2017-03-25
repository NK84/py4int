str = 'X-DSPAM-Confidence: 0.8475'
x = str.find(":")
data = float(str[x+1:])
print (data)
