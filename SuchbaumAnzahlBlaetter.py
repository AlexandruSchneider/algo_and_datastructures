class Node:
    # Constructor to create a new node
    def __init__(self, daten):
        self.daten = daten
        self.links = None
        self.rechts = None


def AnzahlBlaetter(wurzel: Node) -> int:
    if wurzel is None:
        return 0
    anzLinks = AnzahlBlaetter(wurzel.links)
    anzRechts = AnzahlBlaetter(wurzel.rechts)

    if wurzel.links is None and wurzel.rechts is None:
        return 1
    return anzLinks + anzRechts


def AnzahlBlaetter_Im_Unterricht(wurzel: Node) -> int:
    if wurzel is None:
        return 0
    if wurzel.links is None and wurzel.rechts is None:
        return 1
    anzLinks = AnzahlBlaetter(wurzel.links)
    anzRechts = AnzahlBlaetter(wurzel.rechts)
    return anzLinks + anzRechts


def main():
    wurzel = Node(20)
    wurzel.links = Node(10)
    wurzel.rechts = Node(70)
    wurzel.rechts.links = Node(30)
    wurzel.rechts.rechts = Node(80)
    wurzel.rechts.links.rechts = Node(50)
    wurzel.rechts.links.rechts.links = Node(40)
    wurzel.rechts.links.rechts.rechts = Node(60)

    print(f"Die Anzahl der Blätter des Baumes ist: {AnzahlBlaetter(wurzel)}")
    print(f"Die Anzahl der Blätter des Baumes ist: {AnzahlBlaetter_Im_Unterricht(wurzel)}")

    wurzel = Node(20)
    print(f"Die Anzahl der Blätter des Baumes ist: {AnzahlBlaetter(wurzel)}")


if __name__ == "__main__":
    main()

'''
Pseudocode:

####################################################################
AnzahlBlätter(wurzel)
Rückgabe Anzahl der Knoten ohne Nachfolger als Ganzzahl

1. if wurzel = null then:
2.     return 0
3. anzLinks <-- AnzahlBlätter(wurzel.links)
4. anzRechts <-- AnzahlBlätter(wurzel.rechts)
5. if wurzel.links = null und wurzel.rechts = null then:
6.     return 1
7. return anzLinks + anzRechts
####################################################################

Beschreibung zu Pseudocode:

Zeile 1: Falls der Baum leer ist, dann existieren 0 Blätter, also wird 0 zurückgegeben (Zeile 2)

Zeile 2: 0 wird zurückgegeben

Zeile 3 & 4: gehe alle Knoten des Baumes durch

Zeile 5: Falls dieser Knoten ein Blatt ist (also links und recht sind null) dann

Zeile 6: gib 1 zurück (weil das 1 Blatt ist)

Zeile 7: Zähle die Blätter des linken und rechten Unterbaumes zusammen
'''
