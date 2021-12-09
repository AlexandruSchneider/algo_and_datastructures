def dijkstraAdjazenzListe(adjListe, start):
    laenge = len(adjListe)
    abstand = [float("inf")] * laenge
    vorgaenger = [None] * laenge
    istFertig = [False] * laenge

    abstand[start] = 0

    for i in adjListe:
        u = Naechster_Knoten_Dijkstra(adjListe, istFertig, abstand)
        istFertig[u] = True
        for j in i:
            if isinstance(j, tuple):
                v = j[0]
                distance = j[1]
                if abstand[v] > abstand[u] + distance:
                    # überschreiben
                    abstand[v] = abstand[u] + distance
                    vorgaenger[v] = u
    return abstand, vorgaenger


def Naechster_Knoten_Dijkstra(V: list, istFertig: list, abstand: list):
    minimumWert = float("inf")
    naechster = None
    for i in range(len(V)):
        if abstand[i] < minimumWert and istFertig[i] is False:
            minimumWert = abstand[i]
            naechster = i
    return naechster


def main():
    adjListe = [[0, (1, 4), (7, 8)], [1, (0, 4), (2, 8), (7, 11)], [2, (1, 8), (3, 7), (5, 4), (8, 2)], [3, (2, 7), (4, 9), (5, 14)], [4, (3, 9), (5, 10)], [5, (2, 4), (3, 14), (4, 10), (6, 2)], [6, (5, 2), (7, 1), (8, 6)], [7, (0, 8), (1, 11), (6, 1), (8, 7)], [8, (2, 2), (6, 6), (7, 7)]]
    start = 0
    abstand, vorgaenger = dijkstraAdjazenzListe(adjListe, start)
    print(f"{abstand=}")
    print(f"{vorgaenger=}")


if __name__ == "__main__":
    main()
