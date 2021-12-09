def dijkstra(V, E, start):
    abstand = [float("inf")] * len(V)
    vorgaenger = [None] * len(V)
    istFertig = [False] * len(V)

    abstand[V.index(start)] = 0

    while Knoten_vorhanden_Dijkstra(V, istFertig, abstand):
        naechster = Naechster_Knoten_Dijkstra(V, istFertig, abstand)
        istFertig[V.index(naechster)] = True
        # bis dahin ist alles wie im Pseudocode
        # ab hier gibt es eine Änderung, da es Tripel sind
        for kante in E:
            # überprüfen ob der nächste wert auch die aktuelle kante hat
            if naechster == kante[0]:
                # die kante holen
                v = kante[1]
                # abstand von nächster zu v
                gewicht = kante[2]
                # überprüfen welches ob das minimum erreicht wurde
                if abstand[V.index(v)] > abstand[naechster] + gewicht:
                    # überschreiben
                    abstand[V.index(v)] = abstand[V.index(naechster)]+gewicht
                    vorgaenger[V.index(v)] = naechster
    return abstand, vorgaenger


def Knoten_vorhanden_Dijkstra(V: list, istFertig: list, abstand: list) -> bool:
    for knoten in V:
        if abstand[V.index(knoten)] < float("inf") and istFertig[V.index(knoten)] is False:
            return True
    return False


def Naechster_Knoten_Dijkstra(V: list, istFertig: list, abstand: list):
    minimumWert = float("inf")
    naechster = None
    for knoten in V:
        if not istFertig[V.index(knoten)] and abstand[V.index(knoten)] < minimumWert:
            minimumWert = abstand[V.index(knoten)]
            naechster = knoten
    return naechster


def main():
    V = [i for i in range(9)]
    E = [(0, 1, 4), (0, 7, 8), (1, 0, 4), (1, 2, 8), (1, 7, 11), (2, 1, 8), (2, 3, 7), (2, 5, 4), (2, 8, 2), (3, 2, 7), (3, 4, 9), (3, 5, 14), (4, 3, 9), (4, 5, 10), (5, 2, 4), (5, 3, 14), (5, 4, 10), (5, 6, 2), (6, 5, 2), (6, 7, 1), (6, 8, 6), (7, 0, 8), (7, 1, 11), (7, 6, 1), (7, 8, 7), (8, 2, 2), (8, 6, 6), (8, 7, 7)]
    start = V[0]
    abstand, vorgaenger = dijkstra(V, E, start)
    print(f"{abstand=}")
    print(f"{vorgaenger=}")


if __name__ == "__main__":
    main()
