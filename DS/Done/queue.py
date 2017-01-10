import os
import random

class Queue(object):

	def __init__(self):
		self.queue = []

	def insert(self, data):
		self.queue.insert(0,data)
		
	def delete(self):
		return self.queue.pop()

	def size(self):
		return len(self.queue)

	def isempty(self):
		if len(self.queue):
			print("Not Empty")
		else:
			print("Empty")
			
	def display(self):
		print(self.queue)

	def peek(self):
		return self.queue[len(self.queue)-1]
		
	def clear(self):
		self.queue = []

	def tostring(self):
		print("String is: " + ''.join(self.queue))
		
	def contains_element(self,key):
		if key in self.queue:
			print(str(key) + " exists at location: "+ str(self.queue.index(key)))
		else:
			print("Does not exist")

def random_queue(n):
	queue = Queue()
	for i in range(int(n)):
		queue.insert(random.randrange(1,100))
	return queue

def stack_2queues(n):
	n = int(n)
	queue1=[]
	queue2=[]
	for i in range(n):
		data = random.randrange(1,100)
		print("Inserted: "+str(data))
		queue1.insert(0,data)
	print (queue1)
	print("Dequeueing")
	for i in range(len(queue1)-1):
		try:
			e=queue1.pop()
			queue2.insert(0,e)
			print(e)
		except:
			pass
			
	try:
		e = queue1.pop()
		print("Deleted:" +str(e))
	except:
		print("Queue Empty")
	queue1=queue2
	queue2 = []
	print(queue1)
		
		
	
def print_info():
	print ("Select your option:")
	print ("\
	1: Insert\n \
	2: Delete\n \
	3: Peek\n \
	4: Display\n \
	5: Size\n \
	6: Is Empty?\n \
	7: Clear\n \
	8: toString\n \
	9: contains element?\n \
	10: Random Queue\n \
	11: Stack from 2 queues\n \
	c: Clear \n \
	p: Print Options \n \
	q: Exit program\n")


def main():
	os.system('clear')
	queue = Queue()
	print ("Queue created")
	print_info()
	print ("Select your option")
	option = input()

	while (option != 'q'):
		if option == '1':
			print("Enter the element to Insert")
			n = input()
			queue.insert(n)
		elif option == '2':
			try:
				print("Deleted: " + queue.delete())
			except:
				print("Nothing to Delete")
		elif option == '3':
			print("Top: " + queue.peek())
		elif option == '4':
			print("Elements:")
			queue.display()
		elif option == '5':
			print("Size: " + str(queue.size()))
		elif option == '6':
			queue.isempty()
		elif option == '7':
			queue.clear()
			queue.display()
		elif option == '8':
			queue.tostring()
		elif option == '9':
			print("Enter element to search")
			key = input()
			queue.contains_element(key)
		elif option == '10':
			print("Enter the size of the queue you want to create")
			n = input()
			queue_2 = random_queue(n)
			queue_2.display()
		elif option == '11':
			print("Enter the size of the queue you want to create")
			n = input()
			stack_2queues(n)
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