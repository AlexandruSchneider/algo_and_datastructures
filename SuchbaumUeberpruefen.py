class Node:
    # Constructor to create a new node
    def __init__(self, daten):
        self.daten = daten
        self.links = None
        self.rechts = None


def suchbaum_to_list_in_order(wurzel: Node) -> list:
    if wurzel is None:
        return []
    feld = []
    stack = []
    fertig = False
    while not fertig:
        if wurzel is not None:
            stack.append(wurzel)
            wurzel = wurzel.links
        else:
            if len(stack) > 0:
                wurzel = stack.pop()
                feld.append(wurzel.daten)
                wurzel = wurzel.rechts
            else:
                fertig = True
    return feld


def isSuchbaum(wurzel: Node) -> bool:
    if wurzel is not None:
        liste = suchbaum_to_list_in_order(wurzel)
        for i in range(len(liste)-1):
            if liste[i] >= liste[i+1]:
                return False
    return True


def main():
    wurzel = Node(20)
    wurzel.links = Node(10)
    wurzel.rechts = Node(70)
    wurzel.rechts.links = Node(30)
    wurzel.rechts.rechts = Node(80)
    wurzel.rechts.links.rechts = Node(50)
    wurzel.rechts.links.rechts.links = Node(40)
    wurzel.rechts.links.rechts.rechts = Node(60)
    print(f"Das sollte true sein: ")
    print(f"{isSuchbaum(wurzel)}")

    wurzel = Node(10)
    wurzel.links = Node(20)
    wurzel.rechts = Node(5)
    wurzel.links.links = Node(11)
    wurzel.links.links.rechts = Node(1)
    print(f"Das sollte false sein: ")
    print(f"{isSuchbaum(wurzel)}")

    wurzel = Node(20)
    wurzel.links = Node(10)
    wurzel.rechts = Node(70)
    wurzel.rechts.links = Node(50)
    wurzel.rechts.rechts = Node(80)
    wurzel.rechts.links.rechts = Node(30)
    wurzel.rechts.links.rechts.links = Node(40)
    wurzel.rechts.links.rechts.rechts = Node(60)
    print(f"Das sollte false sein: ")
    print(f"{isSuchbaum(wurzel)}")


if __name__ == "__main__":
    main()

'''
Pseudocode: 

####################################################################
isSuchbaum(wurzel)
Rückgabe Wahr (True) oder Falsch (False)

if wurzel != null then:
    feld <-- allokiere Feld mit der Länge vom Resultat der Funktion suchbaum_to_list_in_order(wurzel)
    feld <-- suchbaum_to_list_in_order(wurzel)
    for i <-- 1, ..., (länge von feld - 1) do
        if feld[i] >= feld[i+1] then:
            return false
return true
####################################################################

Bezüglich suchbaum_to_list_in_order(wurzel):

Gleicher Code wie bei der Funktion printInOrderIter(wurzel) mit 3 Änderungen:

Änderung: Eine Liste namens "feld" erstellen. 1 Zeile oberhalb von stack (Zeile 2 im Pseudocode der Aufgabe 4)
Änderung: Zeile 11 geändert: anstatt Werte auszudrucken, der neu erstellten Liste hinzufügen --> feld.append(wurzel)
Änderung: Zeilen 15 & 16 & 17 durch "return liste" ersetzt, damit die "in order" Liste zurückgeliefert wird.
Beschreibung isSuchbaum(wurzel):

Zeile 1: falls der Baum leer ist, dann ist das ein Suchbaum, da die Regel des Suchbaumes nicht verletzt werden

Zeile 2: Mache das Feld mit der Länge der liste der Knoten aus der Funktion suchbaum_to_list_in_order(wurzel)

Zeile 3: speichere die "in order" Liste des Baumes in der Variable "feld"

Zeile 4: Iteriere durch das Feld bis zum ZWEITLETZTEN Element

Zeile 5: Vergleiche die Werte des aktuellen Elementes mit dem nächsten, das aktuelle Element muss kleiner sein als das nächste Element im Feld.

Zeile 6: Falls ein Element grösser oder gleich gross wie das nächste Element ist, dann ist es kein Suchbaum, somit wird false zurückgegeben

Zeile 7: Wenn an dieser Stelle angelangt wird, bedeutet das, dass das Feld sortiert ist und somit ein Suchbaum existiert, also wird true zurückgegeben.
'''