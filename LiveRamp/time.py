# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, B, C, D):
	nums = []
	nums.append(A)
	nums.append(B)
	nums.append(C)
	nums.append(D)
	nums.sort()
	l_hour = -999
	r_hour = -999
	l_min = -999
	r_min = -999

	for i in nums:
		if i <=2 and i > l_hour:
			l_hour = i
	try:
		nums.remove(l_hour)
	except:
		return "NOT POSSIBLE"

	for i in nums:
		if l_hour == 2 and i<=3 and i > r_hour:
			r_hour = i

	if r_hour == -999:
		for i in nums:
			if i > r_hour:
				r_hour = i
	try:
		nums.remove(r_hour)
	except:
		return "NOT POSSIBLE"

	for i in nums:
		if i<=5 and i > l_min:
			l_min = i
#	print(l_min)
#	print(nums)
	try:
		nums.remove(l_min)	
	except:
		return "NOT POSSIBLE"

	r_min = nums[0]
	return(str(l_hour)+str(r_hour)+":"+str(l_min)+str(r_min))

print(solution(3,0,7,0))
print(solution(9,1,2,7))