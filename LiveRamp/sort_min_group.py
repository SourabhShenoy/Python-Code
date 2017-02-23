# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
	leng = len(A)
	start = 0
	end = leng-1
	for i in range(leng-1):
		if A[i] > A[i+1]:
			break
	start = i
	for i in range(leng-1,0,-1):
		if A[i] < A[i-1]:
			break
	end = i
	max,min = A[start],A[start]
	
	for i in range(start+1,end+1):
		if A[i] > max:
			max = A[i]
		if A[i] < min:
			min = A[i]
	for i in range(start):
		if A[i] > min:
			start = i
			break
	for i in range(leng-1,end,-1):
		if A[i] < max:
			end = i
			break
	return end-start+1
print(solution([1,2,6,5,5,8,9]))