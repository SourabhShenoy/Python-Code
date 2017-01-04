import os
import random

class Stack(object):

	def __init__(self):
		self.stack = []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		return self.stack.pop()

	def size(self):
		return len(self.stack)

	def isempty(self):
		if self.stack == []:
			print ("Empty")
		else:
			print("Not Empty")

	def display(self):
		print (self.stack)

	def peek(self):
		return self.stack[len(self.stack)-1]
		
	def clear(self):
		self.stack = []

	def tostring(self):
		str1 = ''.join(self.stack)
		print("String is: " + str1)
			
	def contains_element(self,key):
		if key in self.stack:
			print (str(key) + " Exists at index "+str(self.stack.index(key)))
		else:
			print("Does not exist")
	
	
def get_min(n):
	n = int(n)
	min_stack = []
	while n:
		if len(min_stack) == 0:
			min = None
		else:
			min = min_stack[len(min_stack)-1][1]
		data = random.randrange(1,100)
		if min == None or min > data:
			min = data
		min_stack.append((data, min))
		n = n - 1
	print (min_stack)
	print(min_stack.pop()[0])
	

def random_stack(n):
	stack = Stack()
	for i in range (1,int(n)+1):
		data = random.randrange(1,100)
		stack.push(data)
	return stack

def queue_2stacks():
	stack1 = []
	stack2 = []
	n = 0
	while n:
		data = random.randrange(1,100)
		stack1.append(data)
		n = n - 1
	print (stack1)
	
	print("Popping:")
	l = len(stack1)
	while(l):
		try:
			e = stack1.pop()
		except:
			print("Stack empty")
		stack2.append(e)
		l = l - 1
	
	try:
		e = stack2.pop()
	except:
		print("Stack empty")
	
	
def balanced_paren(expr):
	open = set('([{')
	close = set (')]}')
	match = set([('(',')'),('{','}'),('[',']')])
	stack = []
	for e in expr:
		if e in open:
			stack.append(e)
		elif e in close:
			try:
				last = stack.pop()
			except:
				print("Empty Stack")
				last = None
			if (last,e) not in match:
				return False
		else:
			pass
	
	if len(stack) == 0:
		print ("Matches")
	else:
		print ("Does not match")
	
	
def print_info():
	print ("Select your option:")
	print ("\
	1: Push\n \
	2: Pop\n \
	3: Peek\n \
	4: Display\n \
	5: Size\n \
	6: Is Empty?\n \
	7: Clear\n \
	8: toString\n \
	9: contains element?\n \
	10: Random Stack\n \
	11: Minimum in O(1) time\n \
	12: Queue from 2 stacks\n \
	13: Check if paranthesis are balanced\n \
	c: Clear \n \
	p: Print Options \n \
	q: Exit program\n")


def main():
	os.system('clear')
	stack = Stack()
	print ("Stack created")
	print_info()
	print ("Select your option")
	option = input()

	while (option != 'q'):
		if option == '1':
			print("Enter the element to push")
			n = input()
			stack.push(n)
		elif option == '2':
			try:
				print("Popped: " + stack.pop())
			except:
				print("Nothing to pop")
		elif option == '3':
			print("Top: " + stack.peek())
		elif option == '4':
			print("Elements:")
			stack.display()
		elif option == '5':
			print("Size: " + str(stack.size()))
		elif option == '6':
			stack.isempty()
		elif option == '7':
			stack.clear()
			stack.display()
		elif option == '8':
			stack.tostring()
		elif option == '9':
			print("Enter element to search")
			key = input()
			stack.contains_element(key)
		elif option == '10':
			print("Enter the size of the stack you want to create")
			n = input()
			stack_2 = random_stack(n)
			stack_2.display()
		elif option == '11':
			print("Enter the size of the stack you want to create")
			n = input()
			get_min(n)
		elif option == '12':
			queue_2stacks()
		elif option == '13':
			print("Enter the expression")
			expr = input()
			balanced_paren(expr)
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