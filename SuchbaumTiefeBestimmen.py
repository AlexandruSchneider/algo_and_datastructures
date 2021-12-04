class Node:
    # Constructor to create a new node
    def __init__(self, daten):
        self.daten = daten
        self.links = None
        self.rechts = None


def Tiefe(wurzel: Node) -> int:
    if wurzel is None:
        return -1
    linksTiefe = Tiefe(wurzel.links)
    rechtsTiefe = Tiefe(wurzel.rechts)
    if linksTiefe > rechtsTiefe:
        return linksTiefe + 1
    return rechtsTiefe + 1


def main():
    wurzel = Node(20)
    wurzel.links = Node(10)
    wurzel.rechts = Node(70)
    wurzel.rechts.links = Node(30)
    wurzel.rechts.rechts = Node(80)
    wurzel.rechts.links.rechts = Node(50)
    wurzel.rechts.links.rechts.links = Node(40)
    wurzel.rechts.links.rechts.rechts = Node(60)

    print(f"Die Tiefe des Baumes ist: {Tiefe(wurzel)}")


if __name__ == "__main__":
    main()


'''
Pseudocode: 

####################################################################
Tiefe(Wurzel wurzel)
Rückgabe Tiefe des Baumes als Ganzzahl

1. if wurzel = null then: 
2.     return -1
3. linksTiefe <-- Tiefe(wurzel.links)
4. rechtsTiefe <-- Tiefe(wurzel.rechts)
5. if linksTiefe > rechtsTiefe then:
6.     return linksTiefe + 1
7. return rechtsTiefe + 1
####################################################################

Beschreibung:

Zeile 1: Falls die angegebene Wurzel leer ist (z.B. Baum ist leer) dann:

Zeile 2: gib -1 zurück (da wir einen Schritt zu viel gemacht haben)

Zeile 3: gehe alle linken Unterbäume durch

Zeile 4: danach gehe 1 zurück und dann 1 nach rechts und gehe wieder nach links bis es nicht mehr geht (rekursiver Aufruf)

Zeile 5: Ist der Linke oder der Rechte Baum grösser?

Zeile 6: gib mir die linke Tiefe zurück und addiere 1

Zeile 7: gib mir die rechte Tiefe zurück und addiere 1


Zusammenfassung Zeile 5 - 7:
Gib das Maximum des Maximums der linken und rechten Unterbäume aus und addiere 1 für den aktuellen Knoten
'''