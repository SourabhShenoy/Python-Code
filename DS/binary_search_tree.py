#9,11,12,13,14,15,16,17,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38
#ways of representing trees and constructing a tree from them, use google code parsing method and similar methods, linked list to tree, tree to other DS
#https://gist.github.com/bshyong/8205644
import os

class Node(object):

	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

class BinarySearchTree(object):
	def __init__(self, root=None):
		self.root = root
	
	def insert_manually(self,data):
		if self.root is None:
			new_node = Node(data)
			new_node.left = None
			new_node.right = None
			self.root = new_node
		else:
			current = self.root
			new_node = Node(data)
			new_node.left = None
			new_node.right = None
			while True:
				if data < current.data:
					if current.left:
						current = current.left
					else:
						current.left = new_node
						break
				elif data > current.data:
					if current.right:
						current = current.right
					else:
						current.right = new_node
						break
				else:
					break
	
	def insert(self, data):
		if data is None:
			return None
		else:
			(root,left,right) = data
			new_node = Node(root)
			new_node.left = self.insert(left)
			new_node.right = self.insert(right)
		return new_node
		
	def size(self, root):
		if root is None:
			return 0
		else:
			return self.size(root.left) + self.size(root.right) + 1

	def search(self, root, key):
		if root is None:
			return
		else:
			if str(root.data) == str(key):
				print("Found!")
				return
			else:
				self.search(root.left, str(key))
				self.search(root.right, str(key))

	def inorder(self,root):
		if root is None:
			pass
		else:
			self.inorder(root.left)
			print(root.data,end=' ')
			self.inorder(root.right)

	def preorder(self,root):
		if root is None:
			pass
		else:
			print(root.data,end=' ')
			self.preorder(root.left)
			self.preorder(root.right)
			
	def postorder(self,root):
		if root is None:
			pass
		else:
			self.postorder(root.left)
			self.postorder(root.right)
			print(root.data,end=' ')
			
	def minimum(self,root):
		if root is None:
			return float('inf')
		l_min = self.minimum(root.left)
		r_min = self.minimum(root.right)
		return min(l_min,r_min,root.data)
		
	def maximum(self,root):
		if root is None:
			return float('-inf')
		l_min = self.maximum(root.left)
		r_min = self.maximum(root.right)
		return max(l_min,r_min,root.data)

	def max_depth(self,root):
		if root is None:
			return 0
		l_depth = self.max_depth(root.left)
		r_depth = self.max_depth(root.right)
		return max(l_depth + 1,r_depth + 1)

	def min_depth(self,root):
		if root is None:
			return 0
		if root.left is None and root.right is None:
			return 1
		if root.right is None:
			return self.min_depth(root.left) + 1
		if root.left is None:
			return self.min_depth(root.right) + 1
		return min(self.min_depth(root.left),self.min_depth(root.right))+1

def main():
	os.system('clear')
	tree_1 = BinarySearchTree()
	print ("Binary Search Tree created")
	print ("Select your option:")
	print ("\
	0: Insert manually\n \
	1: Insert\n \
	2: Size\n \
	3: Search\n \
	4: Minimum\n \
	5: Maximum\n \
	6: Inorder\n \
	7: Preorder\n \
	8: Postorder\n \
	9: Delete\n \
	10: Empty Tree\n \
	11: Check if BT is BST\n \
	12: Rank (No of keys <= n)\n \
	13: Successor\n \
	14: Check if BST between loKey and highKey\n \
	15: Level Order Traversal\n \
	16: Nodes without sibling\n \
	17: All root to leaf paths\n \
	18: Minimum Depth\n \
	19: Maximum Depth\n \
	20: Second Smallest Element\n \
	21: Second Largest Element\n \
	22: Right View\n \
	23: Sum of all left leaves\n \
	24: Complete BT?\n \
	25: Invert tree\n \
	26: Top View\n \
	27: Lowest common ancestor of two nodes\n \
	28: Successor\n \
	29: Predecessor\n \
	30: DLL to BST\n \
	31: BST to DLL\n \
	32: Paths with specified sum\n \
	33: Closest node to k in BST\n \
	34: Nodes with sum in BST\n \
	35: Path between 2 nodes\n \
	36: Merge 2 BSTs\n \
	37: BF Traversal \n \
	38: DF Traversal \n \
	c: Clear \n \
	p: Print Options\n \
	q: Exit program\n")
	print ("Select your option:")
	option = input()

	while (option != 'q'):
		if option == '0':
			print("Enter elements to be inserted. Press q to quit")
# Uncomment if manually accepting from user
#			data = input()
#			while data != 'q':
#				tree_1.insert_manually(data)
#				data = input()
			data = [25,19,37,12,22,29,4,23,30]
			data1 = [1,2,3,4,5]
			data2 = [8,3,10,1,6,14,4,7,13]
			for e in data1:
				tree_1.insert_manually(e)
		elif option == '1':
			data = (25, (19, (12, (4, None, None), None), (22, None, (23, None, None))), (37, (29, None, (30, None, None)), None))
			data1 = (1, (2, (4, None, None), (5, None, None)), (3, None, None))
			data2 = (8, (3, (1, None, None), (6, (4, None, None), (7, None, None))), (10, None, (14, (13, None, None), None)))
			tree_1 = None 
			tree_1 = BinarySearchTree()
			tree_1.root = tree_1.insert(data2)
		elif option == '2':
			res = tree_1.size(tree_1.root)
			if res:
				print("Size: " + str(res))
		elif option == '3':
			print("Enter the value to Search:")
			data = input()
			tree_1.search(tree_1.root,data)
		elif option == '4':
			print("Minimum: "+str(tree_1.minimum(tree_1.root)))
		elif option == '5':
			print("Maximum: "+str(tree_1.maximum(tree_1.root)))
		elif option == '6':
			tree_1.inorder(tree_1.root)
			print("")
		elif option == '7':
			tree_1.preorder(tree_1.root)
			print("")
		elif option == '8':
			tree_1.postorder(tree_1.root)
			print("")
		elif option == '9':
			print("**********************************************")
			pass
		elif option == '10':
			tree_1 = None 
			tree_1 = BinarySearchTree()			
		elif option == '11':
			print("**********************************************")
			pass
		elif option == '12':
			print("**********************************************")
			pass
		elif option == '13':
			print("**********************************************")
			pass
		elif option == '14':
			print("**********************************************")
			pass
		elif option == '15':
			print("**********************************************")
			pass
		elif option == '16':
			print("**********************************************")
			pass
		elif option == '17':
			print("**********************************************")
			pass
		elif option == '18':
			print("Min Depth: "+str(tree_1.min_depth(tree_1.root)))
			pass
		elif option == '19':
			print("Max Depth: "+str(tree_1.max_depth(tree_1.root)))
			pass
		elif option == '20':
			print("**********************************************")
			pass
		elif option == '21':
			print("**********************************************")
			pass
		elif option == '22':
			print("**********************************************")
			pass
		elif option == '23':
			print("**********************************************")
			pass
		elif option == '24':
			print("**********************************************")
			pass
		elif option == '25':
			print("**********************************************")
			pass
		elif option == '26':
			print("**********************************************")
			pass
		elif option == '27':
			print("**********************************************")
			pass
		elif option == '28':
			print("**********************************************")
			pass
		elif option == '29':
			print("**********************************************")
			pass
		elif option == '30':
			print("**********************************************")
			pass
		elif option == '31':
			print("**********************************************")
			pass
		elif option == '32':
			print("**********************************************")
			pass
		elif option == '33':
			print("**********************************************")
			pass
		elif option == '34':
			print("**********************************************")
			pass
		elif option == '35':
			print("**********************************************")
			pass
		elif option == '36':
			print("**********************************************")
			pass
		elif option == '37':
			print("**********************************************")
			pass
		elif option == '38':
			print("**********************************************")
			pass
		elif option == 'q':
			os.system('clear')
			exit(0)
		elif option == 'c':
			os.system('clear')
		elif option == 'p':
			os.system('clear')
			print_info()
		else:
			print("Invalid Option!\n")

		print ("Select your option:")
		option = input()


if __name__ == '__main__':
	main()
