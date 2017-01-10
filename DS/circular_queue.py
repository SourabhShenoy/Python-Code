import os
import random


class CircularQueue(object):

    def __init__(self):
        self.c_queue = []

    def enqueue(self, data):
        self.c_queue.insert(0,data)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def isempty(self):
        if not self.queue:
            print ("Empty")
        else:
            print ("Not Empty")

    def display(self):
        print(self.queue)

    def peek(self):
        return self.queue[len(self.queue)-1]

    def clear(self):
        self.queue = []
        queue = Queue()

    def tostring(self):
        str1 = ''.join(self.queue)
        print("String is: " + str1)

    def contains_element(self,key):
        if key in self.queue:
            print (str(key) + " Exists at index "+str(self.queue.index(key)))
        else:
            print("Does not exist")


def random_queue(n):
    queue = Queue()
    for i in range (1,int(n)+1):
        data = random.randrange(1,100)
        queue.enqueue(data)
    return queue

def print_info():
    print ("Select your option:")
    print ("\
    1: Enqueue\n \
    2: Dequeue\n \
    3: Peek\n \
    4: Display\n \
    5: Size\n \
    6: Is Empty?\n \
    7: Clear\n \
    8: toString\n \
    9: contains element?\n \
    10: Random Queue\n \
    c: Clear \n \
    p: Print Options \n \
    q: Exit program\n")


def main():
    os.system('clear')
    queue = CircularQueue()
    print ("Queue created")
    print_info()
    print ("Select your option")
    option = input()

    while option != 'q':
        if option == '1':
            print("Enter the element to Enqueue")
            n = input()
            queue.enqueue(n)
        elif option == '2':
            try:
                print("Deleted: " + queue.dequeue())
            except:
                print("Nothing to Delete")
        elif option == '3':
            try:
                print("Top: " + queue.peek())
            except:
                print("Empty")
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
        elif option == 'q':
            os.system('clear')
            exit(0)
        elif option == '10':
            print("Enter the size of the stack you want to create")
            n = input()
            queue_2 = random_queue(n)
            queue_2.display()
        elif option == 'c':
            os.system('clear')
        elif option == 'p':
            os.system('clear')
            print_info()
        else:
            print("Invalid Option!\n")

        print ("\nSelect your option:")
        option = input()


if __name__ == '__main__':
    main()
