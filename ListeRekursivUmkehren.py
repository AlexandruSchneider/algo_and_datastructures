import copy
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

def makeList():
    # Erstellt eine Liste: 1 --> 2 --> 3 --> 4 --> 5 --> 6 --> 7
    anker = Node(1)
    anker.next = Node(2)
    anker.next.next = Node(3)
    anker.next.next.next = Node(4)
    anker.next.next.next.next = Node(5)
    anker.next.next.next.next.next = Node(6)
    anker.next.next.next.next.next.next = Node(7)
    return anker

# Durch die Liste iterieren und dann von hinten nach vorne die zuweisungen machen
def listeKehrRekAlex(node):
    if node == None or node.next == None:
        return node
    newNode = listeKehrRekAlex(node.next)
    # Der "anker" muss nun der letzte Wert werden, also ist der nächste Wert auf sich selbst zeigen
    node.next.next = node
    # setze den nächsten wert auf null
    node.next = None
    return newNode

# Abagabe André (Problem erkann siehe Funktion listKehrRekAndrVerbessert)
def listKehrRekAndr(vorherigeNode, node):
    if node != None:
        if vorherigeNode != None:
            tmpNode = node.next
            node.next = vorherigeNode
            return listKehrRekAndr(node, tmpNode)
        else:
            print("Element nicht gefunden")
            # Hier sollte eine Exception geschmissen werden, aber aufgrund der Ausgabe nicht implementiert
            return node
    else:
        return None

# Abgabe im Unterricht (Problem erkannt )
def listKehrRekUnte(el1, el2):
    if el1 == None:
        return el2
    aktuell = el1
    el1.next = el1
    aktuell.next = el2
    return listKehrRekUnte(el1, aktuell)

def listKehrRekAndrVerbessert(vorherigeNode, node):
    if node != None:
        tmpNode = copy.deepcopy(node.next)
        node.next = copy.deepcopy(vorherigeNode)
        return listKehrRekAndrVerbessert(node, tmpNode)
    else:
        return vorherigeNode

def listKehrRekUnteVerbessert(el1, el2):
    if el2 == None:
        return el1
    aktuell = copy.deepcopy(el2.next)
    el2.next = copy.deepcopy(el1)
    return listKehrRekUnteVerbessert(el2, aktuell)

# Gibt die Werte einer Liste bzw. einer Node aus
def printList(node):
    print(node.data)
    if node.next != None:
        printList(node.next)

# Hier beginnt das Ausgeben bzw. testen (ist kein gutes Testing, aber eine veranschaulichung der Methoden)
anker = makeList()

print(f"Originale Liste")
printList(anker)

print(f"Gekehrte Liste Alex:")
anker = listeKehrRekAlex(anker)
printList(anker)

anker = makeList()

print(f"Gekehrte Liste André:")
anker = listKehrRekAndr(None, anker)
printList(anker)

anker = makeList()

print(f"Gekehrte Liste André Verbessert:")
anker = listKehrRekAndrVerbessert(None, anker)
printList(anker)

anker = makeList()

print(f"Gekehrte Liste Unterricht:")
anker = listKehrRekUnte(None, anker)
printList(anker)

anker = makeList()

print(f"Gekehrte Liste Unterricht Verbessert:")
anker = listKehrRekUnteVerbessert(None, anker)
printList(anker)