import os
import random

class PriorityQueue(object):

	def __init__(self):
		self.priority_queue = []

	def insert(self, data, priority):
		self.priority_queue.insert(0,(data,priority))
		
	def delete_max(self):
		max_p = self.priority_queue[0][1]
		e = self.priority_queue[0][0]
		for (i,j) in self.priority_queue:
			if j > max_p:
				max_p = j
				e = i
		ind = self.priority_queue.index((e,max_p))
		print("deleted: "+ self.priority_queue.pop(ind))


	def size(self):
		return len(self.priority_queue)

	def isempty(self):
		if len(self.priority_queue):
			print("Not Empty")
		else:
			print("Empty")
			
	def display(self):
		print(self.priority_queue)

	def peek(self):
		return self.priority_queue[len(self.priority_queue)-1][0]
		
	def clear(self):
		self.priority_queue = []

	
def print_info():
	print ("Select your option:")
	print ("\
	1: Insert\n \
	2: Delete Max\n \
	3: Peek\n \
	4: Display\n \
	5: Size\n \
	6: Is Empty?\n \
	7: Clear\n \
	c: Clear \n \
	p: Print Options \n \
	q: Exit program\n")


def main():
	os.system('clear')
	priority_queue = PriorityQueue()
	print ("Priority Queue created")
	print_info()
	print ("Select your option")
	option = input()

	while (option != 'q'):
		if option == '1':
			print("Enter the element to Insert and the priority")
			n = input()
			p = input()
			priority_queue.insert(n,p)
		elif option == '2':
			priority_queue.delete_max()
		elif option == '3':
			print("Top: " + priority_queue.peek())
		elif option == '4':
			print("Elements:")
			priority_queue.display()
		elif option == '5':
			print("Size: " + str(priority_queue.size()))
		elif option == '6':
			priority_queue.isempty()
		elif option == '7':
			priority_queue.clear()
			priority_queue.display()
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