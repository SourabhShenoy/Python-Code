class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        maxtotal , maxyet = 0,0
        for i in range(len(A)):
            maxtotal += A[i]
            if maxtotal < 0:
                maxtotal = 0
            if maxyet < maxtotal:
                maxyet = maxtotal
        return maxyet
        
#for tackling negative numbers only type of array

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        maxtotal , maxyet = 0,0
        pos,least = 0,-999999999
        for i in A:
            if i > 0:
                pos = 1
        if pos:
            for i in range(len(A)):
                maxtotal += A[i]
                if maxtotal < 0:
                    maxtotal = 0
                if maxyet < maxtotal:
                    maxyet = maxtotal
            return maxyet
        else:
            for i in A:
                if least < i:
                    least = i
            return least