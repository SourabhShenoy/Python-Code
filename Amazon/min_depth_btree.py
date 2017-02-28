class Node(object):

	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

class BinaryTree(object):
	def __init__(self, root=None):
		self.root = root

	def insert(self, data):
		if data is None:
			return None
		else:
			(root,left,right) = data
			new_node = Node(root)
			new_node.left = self.insert(left)
			new_node.right = self.insert(right)
		return new_node
		
	def maxDepth(self, root):
		return 1 + max(map(self.maxDepth,(root.left,root.right))) if root else 0

	def minDepth1(self, root):
		if not root: return 0
		d = map(self.minDepth1, (root.left, root.right))
		return 1 + (min(d) or max(d))

	def minDepth2(self, root):
		if not root: return 0
		d, D = sorted(map(self.minDepth2, (root.left, root.right)))
		return 1 + (d or D)
    
def main():
	tree_1 = BinaryTree()
	data = (25, (19, (12, (4, None, None), None), (22, None, (23, None, None))), (37, (29, None, (30, None, None)), None))
	data1 = (1, (2, (4, None, None), (5, None, None)), (3, None, None))
	tree_1.root = tree_1.insert(data)
	print(tree_1.maxDepth(tree_1.root))
	print(tree_1.minDepth1(tree_1.root))
	print(tree_1.minDepth2(tree_1.root))
	
if __name__ == '__main__':
	main()
	
	
'''
DFS 2-liner:

        h = map(self.minDepth, [root.left, root.right]) if root else [-1]
        return 1 + (min(h) or max(h))
        
BFS 4-liner:

        l, i = [root], 1
        while l and root and all(n.left or n.right for n in l):
            l, i = [kid for n in l for kid in [n.left, n.right] if kid], i+1
        return i if root else 0
'''