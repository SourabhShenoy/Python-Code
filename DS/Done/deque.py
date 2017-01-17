import os

class Deque(object):

	def __init__(self):
		self.deque = []

	def insert_front(self, data):
		self.deque.insert(0,data)
		
	def delete_rear(self):
		return self.deque.pop()

	def insert_rear(self, data):
		self.deque.append(data)
		
	def delete_front(self):
		return self.deque.pop(0)

	def size(self):
		return len(self.deque)

	def isempty(self):
		if len(self.deque):
			print("Not Empty")
		else:
			print("Empty")
			
	def display(self):
		print(self.deque)

	def peek(self):
		return self.deque[len(self.deque)-1]
		
	def clear(self):
		self.deque = []

	def tostring(self):
		print("String is: " + ''.join(self.deque))
		
	def contains_element(self,key):
		if key in self.deque:
			print(str(key) + " exists at location: "+ str(self.deque.index(key)))
		else:
			print("Does not exist")
		
	
def print_info():
	print ("Select your option:")
	print ("\
	1: Insert Front\n \
	2: Insert Rear\n \
	3: Delete Front\n \
	4: Delete Rear\n \
	5: Peek\n \
	6: Display\n \
	7: Size\n \
	8: Is Empty?\n \
	9: Clear\n \
	10: toString\n \
	11: contains element?\n \
	c: Clear \n \
	p: Print Options \n \
	q: Exit program\n")


def main():
	os.system('clear')
	deque = Deque()
	print ("Deque created")
	print_info()
	print ("Select your option")
	option = input()

	while (option != 'q'):
		if option == '1':
			print("Enter the element to Insert")
			n = input()
			deque.insert_front(n)
		elif option == '2':
			print("Enter the element to Insert")
			n = input()
			deque.insert_rear(n)
		elif option == '3':
			try:
				print("Deleted: " + deque.delete_front())
			except:
				print("Nothing to Delete")		
		elif option == '4':
			try:
				print("Deleted: " + deque.delete_rear())
			except:
				print("Nothing to Delete")
		elif option == '5':
			print("Top: " + deque.peek())
		elif option == '6':
			print("Elements:")
			deque.display()
		elif option == '7':
			print("Size: " + str(deque.size()))
		elif option == '8':
			deque.isempty()
		elif option == '9':
			deque.clear()
			deque.display()
		elif option == '10':
			deque.tostring()
		elif option == '11':
			print("Enter element to search")
			key = input()
			deque.contains_element(key)
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