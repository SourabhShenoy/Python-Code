#Do inorder and compare array elements

def isValidBST(self, root):
	output = []
	self.inOrder(root, output)
	
	for i in range(1, len(output)):
		if output[i-1] >= output[i]:
			return False

	return True

def inOrder(self, root, output):
	if root is None:
		return
	
	self.inOrder(root.left, output)
	output.append(root.val)
	self.inOrder(root.right, output)
	
	
	
#	----------
	



class Solution(object):
    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
               self.isValidBST(root.right, lessThan, max(root.val, largerThan))