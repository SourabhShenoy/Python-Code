def answer(start, length):
	xsum = 0
	limit = start + length * length
	val = start
	ct = 0
	cons = length
	skip = 0

	while val < limit:
   		if ct % cons == 0 and ct != 0:
   			ct = 0
   			cons -= 1
   			val += skip
   			skip += 1
		ct += 1  
		if val < limit:
	   		xsum = xsum ^ val
   		val += 1 	
	return xsum

#print(answer(0,3))
print(answer(17,4))