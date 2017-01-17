def printActivities(s,f):
	n = len(f)
	i = 0
	print (i)
	for j in range(n):
		if s[j] >= f[i]:
			print j
			i = j
	

#0,2,3,6
s = [1,2,4,6,7,12,15]
f = [3,4,5,13,14,15,18]
printActivities(s,f)