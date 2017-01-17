import os
import random

class CircularQueue(object):

	def __init__(self):
		self.circular_queue = []

	def insert(self, data):
		self.circular_queue.insert(0,data)
		
	def delete(self):
		return self.circular_queue.pop()
			
	def display(self):
		print(self.circular_queue)

	def rotate(self):
		self.circular_queue.insert(0,self.circular_queue.pop())
		self.display()

	
def print_info():
	print ("Select your option:")
	print ("\
	1: Insert\n \
	2: Delete\n \
	3: Display\n \
	4: Rotate \n \
	c: Clear \n \
	p: Print Options \n \
	q: Exit program\n")


def main():
	os.system('clear')
	circular_queue = CircularQueue()
	print ("Circular Queue created")
	print_info()
	print ("Select your option")
	option = input()

	while (option != 'q'):
		if option == '1':
			print("Enter the element to Insert")
			n = input()
			circular_queue.insert(n)
		elif option == '2':
			try:
				print("Deleted: " + circular_queue.delete())
			except:
				print("Nothing to Delete")
		elif option == '3':
			print("Elements:")
			circular_queue.display()
		elif option == '4':
			circular_queue.rotate()
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