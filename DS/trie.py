#https://nickstanisha.github.io/2015/11/21/a-good-trie-implementation-in-python.html
class Node:
	def __init__(self,label=None,data=None):
		self.data = data
		self.label = label
		self.children = dict()
	
	def addChild(self,key,data=None):
		