#usage: python3 single_linked_list.py
#8.1,8.2,17,18,20,21,22,25,26
import os
import random

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
		print ("Inserted " + str(data))

	def insert_middle(self, data, pos):
		new_node = Node(data)
		current = self.head
		ct = 0

		if current is None:
			print ("Can't insert at given position! Inserting at the beginnning!")
			self.insert_beginning(data)
			return
		pos = int(pos) - 1

		while ct!= pos and current.get_next():
			ct = ct + 1
			current = current.get_next()

		new_node.set_next(current.get_next())
		current.set_next(new_node)
		print ("Inserted " + str(data) + " at position " + str(ct+2))

	def insert_end(self, data):
		new_node = Node(data)
		current = self.head

		while current.get_next():
			current = current.get_next()

		current.set_next(new_node)
		print ("Inserted " + str(data))


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
		empty = 1
		while current:
			empty = 0
			print (current.data,end=' ')
			current = current.get_next()
			if current is None:
				print("")
				return
		if empty:
			print("Empty")


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
		print("Deleted " + str(data))

	def get_nth_node(self, n):
		current = self.head
		ct = 0
		n=int(n)
		while ct < n - 1:
			ct = ct + 1
			if current.get_next():
				current = current.get_next()
			else:
				print("Does not exist")
		self.display()
		print ("Node is " + str(current.get_data()))

	def isempty(self):
		if self.size() == 0:
			print("List is empty")
		else:
			print("List is not empty")

	def skipDelete(self,n,m):
		current = self.head
		while(current):
			for i in range(1,m):
				if current is None:
					return
				current = current.get_next()

			if current is None:
				return

			temp = current.get_next()

			for i in range(1,n+1):
				if temp is None:
					break
				temp = temp.get_next()

			current.set_next(temp)
			current = temp
		self.display()

	def printReverse(self, head):
		if head is None:
			return
		else:
			self.printReverse(head.get_next())

		print(head.get_data(),end=' ')

	def iterativeReverse(self):
		prev = None
		current = self.head

		while current:
			next = current.get_next()
			current.set_next(prev)
			prev = current
			current = next
		self.head = prev

	def recursiveReverse(self, p):
	#https://www.youtube.com/watch?v=KYH83T4q6Vs
		if p.get_next() is None:
			self.head = p
			return
		else:
			self.recursiveReverse(p.get_next())

		q = p.get_next()
		q.set_next(p)
		p.set_next(None)

	def find_mid(self):
		slow = self.head
		fast = self.head

		if self.head is None:
			print("List empty")
			return

		while fast and fast.get_next():
			fast = fast.get_next().get_next()
			slow = slow.get_next()

		print("Mid element is: " + slow.get_data())

	def last_to_first(self):
		if self.head is None or self.head.get_next() is None:
			print("Insufficient Nodes")
			return
		last = self.head
		sec_last = None

		while last.get_next() is not None:
			sec_last = last
			last = last.get_next()

		sec_last.set_next(None)
		last.set_next(self.head)
		self.head = last


	#Aliter: http://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/
	def ispalindrome(self,right):
		global left
		left = self.head
		if right is None:
			return
		else:
			res = self.ispalindrome(right.get_next())

			if res == 0:
				return 0

		if left.get_data() == right.get_data():
			res_1 = 1
		else:
			res_1 = 0
		left = left.get_next()

		return res_1



def random_list(n):
	list = LinkedList()
	for i in range (1,int(n)+1):
		data = random.randrange(1,100)
		list.insert_beginning(data)
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
	print ("Single Linked List created")
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
