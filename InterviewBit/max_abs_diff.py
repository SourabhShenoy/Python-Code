'''
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.

'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        maxsum = 0
        for i in xrange(len(A)-1):
            for j in xrange(i+1,len(A)):
                temp = self.getsum(A[i],A[j],i,j)
                if temp > maxsum:
                    maxsum = temp
        return maxsum
    
    def getsum(self, i,j,k,l):
        return abs(i-j) + abs(k-l)
        
#O(n) solution
        
'''
int Solution::maxArr(vector<int> &A) {
int n=A.size(),max1=INT_MIN,max2=INT_MIN,max3=INT_MIN,max4=INT_MIN,ans=INT_MIN;
for(int i=0;i<n;i++){
    max1=max(max1,A[i]+i);
    max2=max(max2,-A[i]+i);
    max3=max(max3,A[i]-i);
    max4=max(max4,-A[i]-i);
}
for(int i=0;i<n;i++){
    ans=max(ans,max1-A[i]-i);
    ans=max(ans,max2+A[i]-i);
    ans=max(ans,max3-A[i]+i);
    ans=max(ans,max4+A[i]+i);
}
return ans;}
'''