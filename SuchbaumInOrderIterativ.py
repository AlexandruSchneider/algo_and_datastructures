class Node:
    # Constructor to create a new node
    def __init__(self, daten):
        self.daten = daten
        self.links = None
        self.rechts = None


def printInOrderIter(wurzel: Node):
    if wurzel is not None:
        stack = []
        fertig = False
        while not fertig:
            if wurzel is not None:
                stack.append(wurzel)
                wurzel = wurzel.links
            else:
                if len(stack) > 0:
                    wurzel = stack.pop()
                    print(f"[{wurzel.daten}]", end=" ")
                    wurzel = wurzel.rechts
                else:
                    fertig = True
    else:
        print("Leerer Baum erhalten!")
    print("\n")


def main():
    wurzel = Node(20)
    wurzel.links = Node(10)
    wurzel.rechts = Node(70)
    wurzel.rechts.links = Node(30)
    wurzel.rechts.rechts = Node(80)
    wurzel.rechts.links.rechts = Node(50)
    wurzel.rechts.links.rechts.links = Node(40)
    wurzel.rechts.links.rechts.rechts = Node(60)

    print("Baum ausgeben: ")
    printInOrderIter(wurzel)

    print("Nur eine Node ausgeben: ")
    printInOrderIter(Node(1))

    print("Nichts mitgeben: ")
    printInOrderIter(None)

    print("Grosser unbalancierter Baum: ")
    wurzel = Node(1)
    wurzel.rechts = Node(2)
    wurzel.rechts.rechts = Node(4)
    wurzel.rechts.rechts.links = Node(3)
    wurzel.rechts.rechts.rechts = Node(6)
    wurzel.rechts.rechts.rechts.links = Node(5)
    wurzel.rechts.rechts.rechts.rechts = Node(10)
    wurzel.rechts.rechts.rechts.rechts.rechts = Node(11)
    wurzel.rechts.rechts.rechts.rechts.rechts.rechts = Node(12)
    wurzel.rechts.rechts.rechts.rechts.rechts.rechts.rechts = Node(13)
    wurzel.rechts.rechts.rechts.rechts.rechts.rechts.rechts.rechts = Node(14)
    printInOrderIter(wurzel)


if __name__ == "__main__":
    main()

'''
Pseudocode:

####################################################################
printInOrderIter(wurzel)
Rückgabe nichts bzw.  Gibt den Suchbaum in korrekter Reihenfolge auf die Konsole aus

1. if wurzel != null then:
2.     stack <-- LISTE ALLOKIEREN
3.     fertig <-- false
4.     while ¬fertig do:
5.         if wurzel != null then:
6.             stack.Einfügen(aktuell)
7.             wurzel --> wurzel.links
8.         else:
9.             if stack.länge > 0 then:
10.                wurzel --> stack.pop()
11.                drucke "[" + wurzel.daten + "]"
12.                wurzel --> wurzel.rechts
13.            else: 
14.                fertig <-- True
15.else:
16.    drucke "Leerer Baum erhalten"
17.drucke neue Zeile
####################################################################

Beschreibung:

Zeile 1: Falls eine Leere Wurzel eingegeben wird

Zeile 2: Allokiere eine Liste (wird als Stack verwendet)

Zeile 3: setze den boolean "fertig" auf false, da das ausgeben des Baumes ja noch nicht fertig ist.

Zeile 4: while loop der solange dauert bis "fertig" auf true gesetzt wird --> somit wird geloopt bis der ganze Suchbaum durchiteriert wurde.

Zeile 5: Falls die angegebene Wurzel nicht null ist mache Zeile 6 & 7

Zeile 6: Füge das aktuelle Element (also die Wurzel) in den Stack

Zeile 7: Setze die Wurzel auf die nächste linke Wurzel, also einen kleineren Wert (so werden wir irgendwann beim kleinsten Wert des Suchbaumes landen)

Zeile 8: Falls nun am kleinsten Werten des aktuellen Suchbaumes (oder Unterbaumes) angelangt wird (also die Wurzel null ist), dann mache die Zeilen 9 bis 14.

Zeile 9: Falls der Stack nicht leer ist führe Zeilen 10, 11 und 12 aus

Zeile 10: schreibe den obersten Wert des Stacks in die wurzel (mit pop()) und entferne diesen Wert aus dem Stack

Zeile 11: gib den obersten Wert aus (also die Kleinste Zahl des gesamten Suchbaumes)

Zeile 12: gehe eine Verzweigung nach rechts im Suchbaum (so beginnt die Suche nach dem zweitkleinsten Element)

Zeile 13: Falls der Stack leer ist, dann wurde der ganze Baum abgesucht und der while loop sollte beendet werden (das beenden findet in der Zeile 14 statt)

Zeile 14: setze den boolean Wert "fertig" auf true, somit bricht der While loop ab.

Zeile 15:  falls der Knoten welcher am Anfang mitgegeben wurde null ist, dann wurde ein leerer Baum mitgegeben (alternativ könnte das am Anfang überprüft werden und so wird das "if" in der Zeile 1 unnötig.

Zeile 16: Gib die Fehlermeldung auf die Konsole aus (an dieser Stelle könnte auch ein error erzeugt werden - ich möchte aber Programmabbrüche vermeiden)

Zeile 17: Nach dem Ausgeben der Werte in der korrekten Reihenfolge des Baumes, mach einen neuen Absatz
'''