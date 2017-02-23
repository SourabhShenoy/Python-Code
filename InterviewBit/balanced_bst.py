# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        if self.getheight(A) == -1:
            return 0
        else:
            return 1
    
    def getheight(self,A):
        if not A:
            return 0
        left = self.getheight(A.left)
        right = self.getheight(A.right)
        
        if left == -1 or right == -1:
            return -1
        
        if abs(left - right) > 1:
            return -1
        
        return max(left,right) + 1
        
        