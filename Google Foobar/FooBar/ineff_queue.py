def answer(start, length):
    xsum = 0
    col = length
    row = length + 1
    val = start
    ct = 0
    
    for _ in range(col):
    	val = start + ct * length
    	ct += 1
    	row -= 1
    	for _ in range(row):
    		xsum = xsum ^ val
    		val +=1
    		
    return xsum

print(answer(0,3))
#print(answer(17,4))