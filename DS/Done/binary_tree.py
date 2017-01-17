import os

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
				self.search(root.left, key)
				self.search(root.right, key)
		
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


def main():
	os.system('clear')
	tree_1 = BinaryTree()
	print ("Binary Tree created")
	print ("Select your option:")
	print ("\
	1: Insert\n \
	2: Size\n \
	3: Search\n \
	4: Minimum\n \
	5: Maximum\n \
	6: Inorder\n \
	7: Preorder\n \
	8: Postorder\n \
	c: Clear \n \
	p: Print Options \n \
	q: Exit program\n")
	print ("Select your option:")
	option = input()

	while (option != 'q'):
		if option == '1':
			data = (25, (19, (12, (4, None, None), None), (22, None, (23, None, None))), (37, (29, None, (30, None, None)), None))
			data1 = (1, (2, (4, None, None), (5, None, None)), (3, None, None))
			tree_1.root = tree_1.insert(data)
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
