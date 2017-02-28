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

	def reorderList(self, head):
		if not head:
			return
		
		slow = fast = head 
		while fast and fast.get_next():
			slow = slow.get_next()
			fast = fast.get_next().get_next()

		pre, node = None, slow
		while node:
			pre = node
			node = node.get_next()
			node.set_next(pre)
			
		first, second = head, pre
		
		while second.get_next():
			first = first.get_next()
			first.set_next(second)
			second = second.get_next()			
			second.set_next(first)
		return 

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
			
def main():
	list_1 = LinkedList()
	data = [1,2,3,4,5,6,7]
	for i in data:
		list_1.insert_beginning(i)
	list_1.display()
	list_1.reorderList(list_1.head)
	list_1.display()

if __name__ == '__main__':
	main()
