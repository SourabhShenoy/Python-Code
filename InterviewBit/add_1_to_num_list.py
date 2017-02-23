class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        ans = int((''.join(map(str,A))))
        ans += 1
        return [int(i) for i in str(ans)]