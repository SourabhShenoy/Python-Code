------------------------Min subarray len. >= s

class Solution:

def minSubArrayLen(self, s, nums):
    total = left = 0
    result = len(nums) + 1
    for right, n in enumerate(nums):
        total += n
        while total >= s:
            result = min(result, right - left + 1)
            total -= nums[left]
            left += 1
    return result if result <= len(nums) else 0
    


------------------------max subarray sum = k


def maxSubArrayLen(self, nums, k):
    ans, acc = 0, 0               # answer and the accumulative value of nums
    mp = {0:-1}                 #key is acc value, and value is the index
    for i in xrange(len(nums)):
        acc += nums[i]
        if acc not in mp:
            mp[acc] = i 
        if acc-k in mp:
            ans = max(ans, i-mp[acc-k])
    return ans
 
 
 
 
#I keep a hash table whose key is the sum of subarray from index 0 to index i, inclusive, and value is the ending index i. If there are multiple value for a key, then the value is the minimum of them, that is the first index that attain that sum of subarray from index 0.

def maxSubArrayLen(nums, k):
    sum_table = {} # key: sum(nums[:i+1]), value: i
    total = 0
    max_len = 0
    for i in range(0, len(nums)):
        total += nums[i]
        if not sum_table.has_key(total):
            sum_table[total] = i
        remain = total - k
        if remain == 0:
            max_len = max(i+1, max_len)
        elif sum_table.has_key(remain):
            max_len = max(i - sum_table[remain], max_len)
    
    return max_len
    
------------------------max subarray

class Solution:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum