'''
Naive:
By keeping two arrays: one for non-zero numbers and one for all zeroes, we can concatenate them at the
end. Since we just need to traverse the array once, this will give us O(N) time complexity. Space
complexity is O(N) as we need two additional arrays.
'''



#LeetCode. Pythonic 2 pointer solution
def moveZeroes(nums):
	if not nums:
		return
	
	last0 = 0
	for i in xrange(0,len(nums)):
		if (nums[i]!=0):
			nums[i],nums[last0] = nums[last0],nums[i]
			last0+=1
	return nums

print(moveZeroes([0,12,211,1,0,12,23,0,0,3,0]))




'''As you can see, we've already got O(N) time complexity and O(1) space complexity. We also know that O(N)
time complexity is the lower bound, the only way to further improve the algorithm is to reduce the number
of operations, though we still keep O(N) time complexity.
If you think more about the above solution, there are some redundant operations. When we traverse the
array, we don't really need to finish every single number. When we already reach the last count numbers,
there's no need to check zeroes as all of them should be set to 0.
In other words, the iteration should finish when index i >= count.
'''

#Reduced operations. Not so accurate.

def moveZeroes1(nums):
	if not nums:
		return
	
	right = len(nums) - 1
#	while nums[right] == 0:
#		right -= 1
	for left in xrange(len(nums)):
		if left > right:
			nums[left] = 0
			continue

		if nums[left] != 0:
			continue

		nums[left] = nums[right]
		right -= 1
	return nums

print(moveZeroes1([0,12,211,1,0,12,23,0,0,3,0]))




#One Liner: Sort sorts in place. So O(1) Space complexity. May use Tim Sort  (hybrid: merge+insertion)
#internally
#nums.sort(key= lambda x: 1 if x == 0 else 0) # Will ensure that 0 > non-zero
#
#
#Inefficient. Start from end, pop and append all 0s
'''
for n in range(len(nums)-1,-1,-1):
            if(nums[n] == 0):
                nums.append(nums.pop(n))
'''