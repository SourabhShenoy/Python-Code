from bitarray import bitarray
import mmh3
import os
import datetime

class BloomFilter:
	def __init__(self,size,no_hash):
		self.size = size
		self.no_hash = no_hash
		self.bit_array = bitarray(size)
		self.bit_array.setall(0)

	def add(self,string):
		for i in range(0,self.no_hash):
			temp = mmh3.hash(string,i) % self.size
			self.bit_array[temp] = 1
			
			
	def search(self,string):
		for i in range(0,self.no_hash):
			temp = mmh3.hash(string,i) % self.size
			if self.bit_array[temp] == 0:
				return 0
		return 1

def print_info():
	print("\
	1: Search a word\n \
	q: Quit\n \
	c: Clear\n \
	p: Print options")
		
def main():
	os.system('clear')
	print_info()
	print ("Enter size and number of hashes")
	n = input()
	m= input()
	bf = BloomFilter(int(n),int(m))
	compare = []
	words = open("/usr/share/dict/words").read().splitlines()
	for i in words:
		bf.add(i)
		compare.append(i)
		
	print ("Select your option")
	option = input()

	while (option != 'q'):
		if option == '1':
			print("Enter the word to search:")
			word = input()

			start = datetime.datetime.now()
			res = bf.search(word)
			if res:
				print("May exist")
			else:
				print("Doesnt exist")
			finish = datetime.datetime.now()
			print ((finish-start).microseconds)

			start = datetime.datetime.now()
			found = 0
			for c in compare:
				if c == word:
					print("Exists")
					found = 1
					break
			if not found:
				print("Does not exist")
			finish = datetime.datetime.now()
			print ((finish-start).microseconds)

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