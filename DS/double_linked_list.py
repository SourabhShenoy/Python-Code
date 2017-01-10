import os
import random

class Node(object):

	def __init__(self, data=None, next_node=None, prev_node=None):
		self.data = data
		self.next_node = next_node
		self.prev_node = prev_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node
		
	def set_next(self, new_next):
		self.next_node = new_next

	def get_prev(self):
		return self.prev_node
		
	def set_prev(self, new_prev):
		self.prev_node = new_prev


class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def insert_beginning(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		new_node.set_prev(None)
		if new_node.get_next():
			new_node.get_next().set_prev(new_node)
		self.head = new_node
		print("Inserted: " + data)

	def insert_middle(self, data, pos):
		new_node = Node(data)
		if self.head == None:
			new_node.set_next(None)
			new_node.set_prev(None)
			self.head = new_node
			print("Inserted first element: " + data)
		else:
			if int(pos) > self.size() or pos < 1:
				print("Cant insert at position. Inserting at beginning")
				self.insert_beginning(data)
			else:
				ct = 1
				current = self.head
				while ct < int(pos):
					current = current.get_next()
					ct += 1
				current.get_next().set_prev(new_node)
				new_node.set_next(current.get_next())
				current.set_next(new_node)
				new_node.set_prev(current)
				print("Inserted: " + data)
		self.display()
				
					


	def insert_end(self, data):
		new_node = Node(data)
		if self.head == None:
			new_node.set_next(None)
			new_node.set_prev(None)
			self.head = new_node
		else:
			current = self.head
			while current.get_next():
				current = current.get_next()
			current.set_next(new_node)
			new_node.set_prev(current)
		print("Inserted: " + data)			
		


	def size(self):
		count = 0
		current = self.head
		while current:
			count+=1
			current = current.get_next()
		return count

	def search(self, key):
		current = self.head
		pos = 1
		if self.size():
			while current:
				if current.get_data() == key:
					return key, pos
					break
				current = current.get_next()
				pos += 1
			return None,None
		else:
			return None,None

	def display(self):
		if self.size():
			current = self.head
			while current:
				print(current.data,end=' ')
				current = current.get_next()
			print("")
		else:
			print("Empty List")

	def delete(self, data):
		current = self.head
		found = False
		if not self.size():
			print("Empty List")
			return
		
		while current:
			if current.get_data() == data:
				if current.get_prev() == None and current.get_next() == None:
					print("Deleted last element: " + data)
					self.head = None
					found = True
					break
					
				if current.get_prev() == None:
					print("Deleted first element: " + data)
					current.get_next().set_prev(None)
					self.head = current.get_next()
					current.set_next(None)
					found = True
					break

				if current.get_next() == None:
					print("Deleted last element: " + data)
					current.get_prev().set_next(None)
					current.set_prev(None)
					found = True
					break
				
				current.get_prev().set_next(current.get_next())
				current.get_next().set_prev(current.get_prev())
				print("Deleted from between: " + data)
				found = True
				break

			current = current.get_next()
		
		if not found:
			print("Does not exist")

	def get_nth_node(self, n):
		current = self.head
		i = 0
		n = int(n)
		if n <= self.size() and self.size():
			while current:
				i += 1
				if i == n:
					print("Node is " + current.get_data())
					return
				current = current.get_next()
		else:
			print("Can't find")
			
	def isempty(self):
		return self.head == None

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
	list = LinkedList()
	for i in range (1,int(n)+1):
		data = random.randrange(1,100)
		list.insert_beginning(str(data))
	return list

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
			print(list_1.isempty())
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
