import random

class Node:
	def __init__(self, data=None, anzEbenen=0):
		self.data = data
		self.anzEbenen = anzEbenen
		self.next = [None]


def search(head, key):
	el = head
	for ebene in range(head.anzEbenen, -1, -1):
		while el.next[ebene] != None and el.next[ebene].data < key:
			el = el.next[ebene]
		ebene -= 1
	if el.next[0] == None or el.next[0].data != key:
		raise Exception("Element nicht gefunden!")
	else: 
		return el.next[0]


def previous(head, key):
	el = head
	# Erstellt eine Liste mit Ebenenanzahl an Elementen (also falls 3 Ebenen, gibt es 3 mal None in der Liste)
	prev = [None]*(len(head.next))

	for ebene in range(len(head.next)-1, -1, -1):
		while el.next[ebene] != None and el.next[ebene].data < key:
			el = el.next[ebene]
		prev[ebene] = el
	return prev


def insertInSkipList(head, newData):
	vorher = previous(head, newData)
	anzEbenen = 3
	el = vorher[0]

	if el.next[0] != None and el.next[0].data == newData:
		raise Exception("Element schon enthalten!")

	else:
		knotenEbene = 0
		while random.random() < 0.5 and knotenEbene < len(head.next)-1:
			knotenEbene += 1
		if knotenEbene > anzEbenen:
			for ebene in range(anzEbenen+1, knotenEbene):
				vorher[ebene] = anker
				anker.next[ebene] = None
			anzEbenen = knotenEbene
		neuesElem = Node(newData, knotenEbene)
		for ebene in range(knotenEbene):
			neuesElem.next[ebene] = vorher[ebene].next[ebene]
			vorher[ebene].next[ebene] = neuesElem


def printSkipList(head):
	stringresult = ""
	for i in range(len(head.next)):
		temp = head
		string = ""
		lastValues = 0
		while temp.next[i] != None:
			if i > 0:
				anzZeichen = len(str(temp.data))
				if head.data == temp.data:
					string += " [" + " "*anzZeichen + "] "
				else:
					anzStriche = 0
					iterator = head
					while iterator.next[0].data != temp.data:
						anzStriche += 1
						iterator = iterator.next[0]
					string += ("-------"*(anzStriche-lastValues)) + "-> [" + (" "*anzZeichen) + "] "
					lastValues = anzStriche + 1
			else:
				string += " [" + str(temp.data) + "] --"
			
			# Am Ende (also falls es der letzte Wert dieser Ebene ist)
			if temp.next[i].next[i] == None:
				if i > 0:
					anzZeichen = len(str(temp.next[i].data))
					anzStriche = 0
					iterator = head
					while iterator.next[0].data != temp.next[i].data:
						anzStriche += 1
						iterator = iterator.next[0]
					string += "------"*(anzStriche-lastValues+1) +"[" + (" "*anzZeichen) + "] --|"
				else:
					string += " [" + str(temp.next[i].data) + "] --|"

			# Den Iterator erweitern
			temp = temp.next[i]

		# Ebene wird dem finalen output hinzugefügt wird 
		stringresult = "Ebene " + str(i) + ": " + string + "\n" + stringresult 
	print(stringresult)


head = Node(1, 2)
node1 = Node(2, 0)
node2 = Node(3, 1)
node3 = Node(4, 0)
node4 = Node(7, 0)
node5 = Node(8, 2)
node6 = Node(9, 0)
node7 = Node(10, 0)
node8 = Node(11, 2)
node9 = Node(12, 0)

head.next = [node1, node2, node5]
node1.next = [node2]
node2.next = [node3, node5]
node3.next = [node4]
node4.next = [node5]
node5.next = [node6, node8, node8]
node6.next = [node7]
node7.next = [node8]
node8.next = [node9, None, None]
node9.next = [None]

print("Skiplist Anfang: ")
printSkipList(head)

zahl = int(input("Nach welcher Zahl soll gesucht werden? "))

if search(head, zahl) != None:
	print(f"Die Zahl {zahl} wurde gefunden!")

insertInSkipList(head, 5)

print("\nDie Skiplist am Ende: ")
printSkipList(head)