class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
    	l = len(A)
    	summ = l*(l+1)/2
    	asumm = 0
    	b = 0
    	dt ={}
    	for i in A:
    		asumm += i
    	for i in A:
    		try:
    			if dt[i] == 1:
    				b = i
    		except:
    			dt[i] = 1
    	a = summ - asumm + b
    	return [b,a]