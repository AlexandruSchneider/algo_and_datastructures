class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

def bubblesort(anker):
	toChange = True
	while toChange:
		toChange = False
		tmpAnker = anker
		while tmpAnker.nextval is not None:
			if tmpAnker.dataval > tmpAnker.nextval.dataval:
				toChange = True
				# Swap
				value = tmpAnker.dataval
				tmpAnker.dataval = tmpAnker.nextval.dataval
				tmpAnker.nextval.dataval = value
			else:
				tmpAnker = tmpAnker.nextval

	printNodes(anker)


def printNodes(node):
	if node:
		print(node.dataval, end=" ")
		printNodes(node.nextval)

anker = Node(1)
node1 = Node(3)
node2 = Node(6)
node3 = Node(4)
node4 = Node(2)
node5 = Node(11)
node6 = Node(5)

anker.nextval = node1
node1.nextval = node2
node2.nextval = node3
node3.nextval = node4
node4.nextval = node5
node5.nextval = node6

printNodes(anker)
print("\n")
bubblesort(anker)