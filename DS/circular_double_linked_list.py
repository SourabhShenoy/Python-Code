import os
import random

class Node(object):

	def __init__(self, data=None, next_node=None):
		pass

	def get_data(self):
		pass

	def get_next(self):
		pass
		
	def set_next(self, new_next):
		pass

class LinkedList(object):
	def __init__(self, head=None):
		pass

	def insert_beginning(self, data):
		pass

	def insert_middle(self, data, pos):
		pass

	def insert_end(self, data):
		pass


	def size(self):
		pass

	def search(self, key):
		pass

	def display(self):
		pass

	def delete(self, data):
		pass

	def get_nth_node(self, n):
		pass
		
	def isempty(self):
		pass

	def skipDelete(self,n,m):
		pass
		
	def printReverse(self, head):
		pass

	def iterativeReverse(self):
		pass

	def recursiveReverse(self, p):
		pass

	def find_mid(self):
		pass

	def last_to_first(self):
		pass

	def ispalindrome(self,right):
		pass



def random_list(n):
	pass

def print_info():
	print ("Select your option:")
	print ("\
	1: Insert at the beginning\n \
	2: Insert After\n \
	3: Insert at the end\n \
	4: Display\n \
	5: Size\n \
	6: Search\n \
	7: Delete Node\n \
	8: Sort\n \
	9: Reverse Iteratively\n \
	10: Reverse using Recursion\n \
	11: Empty List\n \
	12: Get Nth Node\n \
	13: IsEmpty? \n \
	14: IsPalindrome? \n \
	15: Delete N nodes after M nodes \n \
	16: Print elements in reverse without reversing \n \
	17: Remove Duplicates from unsorted list\n \
	18: Swap every 2 nodes \n \
	19: Move last node to front \n \
	20: Detect and remove loop \n \
	21: Intersection of 2 Linked Lists \n \
	22: Merge 2 sorted Linked Lists \n \
	23: Create a random list of size n \n \
	24: Find Middle \n \
	25: Remove Duplicates from sorted list\n \
	26: Swap 2 nodes\n \
	c: Clear \n \
	p: Print Options \n \
	q: Exit program\n")


def main():
	os.system('clear')
	list_1 = LinkedList()
	print ("Double Linked List created")
	print_info()
	print ("Select your option")
	option = input()

	while (option != 'q'):
		if option == '1':
			print("Enter the value to insert:")
			data = input()
			list_1.insert_beginning(data)
		elif option == '2':
			print("Enter the value to insert:")
			data = input()
			print("Enter the position to insert after:")
			pos = input()
			list_1.insert_middle(data,pos)
		elif option == '3':
			print("Enter the value to insert:")
			data = input()
			list_1.insert_end(data)
		elif option == '4':
			list_1.display()
		elif option == '5':
			res = list_1.size()
			if res:
				print("Size: " + str(res))
			else:
				print("List Empty")
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
				print("QS et to be implemented!\n")
			elif choice == '2':
				print("MS Yet to be implemented!\n")
			else:
				print("Incorrect Choice!\n")
		elif option == '9':
			list_1.iterativeReverse()
			list_1.display()
		elif option == '10':
			list_1.recursiveReverse(list_1.head)
			list_1.display()
		elif option == '11':
			list_1 = None
			list_1 = LinkedList()
			print("Emptied List")
		elif option == '12':
			print("Enter value of n")
			n = input()
			list_1.get_nth_node(n)
		elif option == '13':
			list_1.isempty()
		elif option == '14':
			ans = list_1.ispalindrome(list_1.head)
			if ans:
				print("Palindrome!")
			else:
				print("Not a Palindrome!")
#			temp = random_list(10)
#			temp.display()
#			temp.ispalindrome(temp.head)
		elif option == '15':
			print("Enter values of n and m")
			n = input()
			m = input()
			list_1.skipDelete(int(n),int(m))
		elif option == '16':
			list_1.printReverse(list_1.head)
			list_1.display()
		elif option == '17':
			print("unsorted Dup Yet to be implemented!\n")
		elif option == '18':
			print("Swap every 2 nodes Yet to be implemented!\n")
		elif option == '19':
			list_1.last_to_first()
			list_1.display()
		elif option == '20':
			print("Loop Yet to be implemented!\n")
		elif option == '21':
			print("Intersection Yet to be implemented!\n")
		elif option == '22':
			print("Merge lists Yet to be implemented!\n")
		elif option == '23':
			print("Enter the size of the list you want to create")
			n = input()
			list_2 = random_list(n)
			list_2.display()
		elif option == '24':
			list_1.find_mid()
		elif option == '25':
			print("sorted dup Yet to be implemented!\n")
		elif option == '26':
			print("Swap 2 nodes Yet to be implemented!\n")
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
