#Longest Increasing Subsequence, Longest Common Subsequence, Edit Distance, Min Cost Path
#Coin Change, Matrix Chain, 0-1 Knapsack, Egg Dropping, Longest Palindromic Subsequence
#Rod Cutting, Longest Bitonic Subsequence, Floyd Warshall, Palindrome Partitioning
#Word Wrap Problem, Box Stacking, Fibonacci numbers, Largest Sum Contiguous Subarray
#Bellman–Ford Algorithm for Shortest Paths, Optimal Binary Search Tree
#Largest Independent Set Problem, Subset Sum Problem, Maximum sum rectangle in a 2D matrix
#Count number of binary strings without consecutive 1s?, Boolean Parenthesization Problem
#Count ways to reach the n’th stair, Minimum Cost Polygon Triangulation
#Mobile Numeric Keypad Problem, Count of n digit numbers whose sum of digits equals to given sum
#Minimum Initial Points to Reach Destination, Total number of non-decreasing numbers with n digits
#Find length of the longest consecutive path from a given starting character, Tiling Problem
#Minimum number of squares whose sum equals to given number n, Shortest Common Supersequence
#Compute sum of digits in all numbers from 1 to n, Count possible ways to construct buildings
#Find the minimum cost to reach destination using a train
#Vertex Cover Problem | Set 2 (Dynamic Programming Solution for Tree)
#Count number of ways to reach a given score in a game, Weighted Job Scheduling
#Longest Even Length Substring such that Sum of First and Second Half is same
import os

class Node(object):

	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def insert_beginning(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head=new_node
		print ("Inserted " + data)

	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next()
		return count


	def search(self, key):
		current = self.head
		found = False
		ct = 0
		while current and found is False:
			ct += 1
			if current.get_data() == key:
				found = True
			else:
				current = current.get_next()

		if current is None:
			return
		else:
			return current, ct

	def display(self):
		current = self.head
		print ("List is:")
		while current:
			print (current.data,end=' ')
			current = current.get_next()
			if current is None:
				print("") 
				return


	def delete(self, data):
		current = self.head
		previous = None
		found = False
		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				previous = current
				current = current.get_next()
		if current is None:
			return
		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())
		print("Deleted " + data)

def main():
	os.system('clear')
	list_1 = LinkedList()
	print ("Single Linked List created")
	print ("Select your option:")
	print ("\
	1: Insert at the beginning\n \
	2: Insert in the middle\n \
	3: Insert at the end\n \
	4: Display\n \
	5: Size\n \
	6: Search\n \
	7: Delete Node\n \
	8: Sort\n \
	9: Reverse\n \
	10: Reverse using Recursion\n \
	11: Delete List\n \
	12: Get nth Node\n \
	13: IsEmpty? \n \
	14: IsPalindrome? \n \
	15: Delete N nodes after M nodes \n \
	16: Print elements in reverse without reversing \n \
	17: Remove Duplicates \n \
	18: Swap every 2 nodes \n \
	19: Move last node to front \n \
	20: Nth node from end \n \
	21: Detect and remove loop \n \
	22: Intersection of 2 Linked Lists \n \
	23: Merge 2 sorted Linked Lists \n \
	q: Exit program\n")
	option = input()

	while (option != 'q'):
		if option == '1':
			print("Enter the value to insert:")
			data = input()
			list_1.insert_beginning(data)
		elif option == '2':
			print("Yet to be implemented!\n")
		elif option == '3':
			print("Yet to be implemented!\n")
		elif option == '4':
			list_1.display()
		elif option == '5':
			res = list_1.size()
			if res:
				print("Size: " + str(res))
		elif option == '6':
			print("Enter the value to Search:")
			data = input()
			res, i = list_1.search(data)
			if res:
				print("Element Found at pos: " + str(i))
			else:
				print("Element does not exist")
		elif option == '7':
			print("Enter the value to delete:")
			data = input()
			list_1.delete(data)
		elif option == '8':
			print ("1: Quick Sort\n2: Merge Sort")
			choice = input()
			if choice == '1':
				print("Yet to be implemented!\n")
			elif choice == '2':
				print("Yet to be implemented!\n")
			else:
				print("Incorrect Choice!\n")
		elif option == '9':
			print("Yet to be implemented!\n")
		elif option == '10':
			print("Yet to be implemented!\n")
		elif option == '11':
			print("Yet to be implemented!\n")
		elif option == '12':
			print("Yet to be implemented!\n")
		elif option == '13':
			print("Yet to be implemented!\n")
		elif option == '14':
			print("Yet to be implemented!\n")
		elif option == '15':
			print("Yet to be implemented!\n")
		elif option == '16':
			print("Yet to be implemented!\n")
		elif option == '17':
			print("Yet to be implemented!\n")
		elif option == '18':
			print("Yet to be implemented!\n")
		elif option == '19':
			print("Yet to be implemented!\n")
		elif option == '20':
			print("Yet to be implemented!\n")
		elif option == '21':
			print("Yet to be implemented!\n")
		elif option == '22':
			print("Yet to be implemented!\n")
		elif option == '23':
			print("Yet to be implemented!\n")
		elif option == 'q':
			exit(0)
		else:
			print("Invalid Option!\n")

		print ("Select your option:")
		option = input()


if __name__ == '__main__':
	main()
